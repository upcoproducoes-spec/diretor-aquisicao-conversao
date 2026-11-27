# /// script
# requires-python = ">=3.10"
# dependencies = ["google-ads>=35"]
# [tool.uv]
# exclude-newer = "2026-11-05T00:00:00Z"
# ///
"""
Monta campanha Demand Gen no Google Ads a partir do registro JSON do lançamento, sempre PAUSADA.
Ligar não existe aqui: quem liga é o dono da conta, na tela do Google Ads (`sirius-scale/REGRAS.md` §6).

O REGISTRO: o formato `google.campanhas[]` + `criativos`, com exemplo comentado em
modelos/campanhas.exemplo.json. Uma campanha por grupo (Demand Gen não tem orçamento por grupo, §14),
um anúncio por criativo (o Dash separa a venda por anúncio), o vídeo vertical e o 16:9 no MESMO anúncio
(§13), estático como `demand_gen_multi_asset_ad` no mesmo grupo (§19). O anúncio aponta pro `youtube_id` do
registro: quem chega com ele é o comando `videos`, ou alguém que subiu à mão, não listado.

OS COMANDOS, na ordem em que costumam rodar:
  listas  cria as listas por regra de URL de `google.listas_novas` e lê de volta cada uma.
  marca   cria a logo (`logo_arquivo`) e o botão (`cta`) que a conta ainda não tem e grava os ids.
  videos  sobe no YouTube, sempre não listados, os vídeos do registro que têm `arquivo` e ainda não têm id.
          Vai pela API do Google Ads, com as credenciais de sempre, espera o YouTube processar e grava o
          `youtube_id`. Rodar de novo só continua: o que já subiu não sobe duas vezes.
  criar   a cadeia inteira num Mutate só (registro.py): orçamento, campanha, grupo, audience, geo no
          grupo, assets e anúncios. Depois as metas de conversão (só as do registro ficam biddable, §2)
          e a leitura de volta. Se a campanha já existe, só acrescenta os anúncios novos, pausados.
  anexar  põe no anúncio os vídeos que o criativo ganhou depois (o 16:9, por exemplo). O anúncio
          continua o mesmo e volta pra revisão do Google (§5), por isso anúncio no ar fica de fora.

AS TRAVAS:
  - Sem --executar nada é escrito, e a prévia roda a validação a seco (validate_only) de verdade. A exceção é
    o `videos`: o Google não tem validação a seco de upload, então a prévia dele confere arquivo, título e canal.
  - Com --executar, mostra o resumo e pede `confirmo` digitado, ou --confirmado-no-chat depois do ok
    escrito de quem decide. Sem TETO_CAMPANHA_DIA no .env, para antes de tudo.
  - Orçamento acima do teto não tem confirmação que passe: é bloqueio.
  - Tudo nasce PAUSED nos três níveis, e depois de escrever lê de volta da plataforma.
  - `videos` não gasta verba, então não pede teto. Pede o mesmo ok, e o id só entra lido de volta.

Os §N são de `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`.

Uso (caminhos relativos à raiz da pasta do sistema):
  uv run sirius-scale/ferramentas/google/subir_campanha.py listas --registro <json> [--executar] [--confirmado-no-chat]
  uv run sirius-scale/ferramentas/google/subir_campanha.py marca  --registro <json> [--executar] [--confirmado-no-chat]
  uv run sirius-scale/ferramentas/google/subir_campanha.py videos --registro <json> [--espera <minutos>] [--executar] [--confirmado-no-chat]
  uv run sirius-scale/ferramentas/google/subir_campanha.py criar  --registro <json> [--campanha <trecho>] [--executar] [--confirmado-no-chat]
  uv run sirius-scale/ferramentas/google/subir_campanha.py anexar --registro <json> [--executar] [--confirmado-no-chat]
"""

import argparse
import json
import os
import re
import sys
import time

import comum
import registro as gr

LIMITES = {"headlines": 40, "long_headlines": 90, "descriptions": 90}
# lance do registro -> como a plataforma devolve em bidding_strategy_type
LANCES = {"MAXIMIZE_CONVERSIONS": "MAXIMIZE_CONVERSIONS", "MAXIMIZE_CLICKS": "TARGET_SPEND"}
OBRIGATORIOS = ("customer_id", "geo", "lance", "metas_biddable", "fim", "business_name",
                "final_url_suffix", "campanhas")
# formato do estático -> campo do demand_gen_multi_asset_ad e proporção (largura / altura)
CAMPOS_IMAGEM = (("paisagem", "marketing_images", 1.91), ("quadrado", "square_marketing_images", 1.0),
                 ("feed", "portrait_marketing_images", 0.8), ("story", "tall_portrait_marketing_images", 0.5625))
# formato do vídeo -> onde mora o arquivo, o id no YouTube e o upload ainda sem resposta
FORMATOS_VIDEO = (("vertical", "arquivo", "youtube_id", "youtube_upload"),
                  ("16:9", "arquivo_169", "youtube_id_169", "youtube_upload_169"))
EXTENSOES_VIDEO = {".3gp", ".avi", ".flv", ".mkv", ".mov", ".mp4", ".mpeg", ".mpg", ".ogg", ".webm", ".wmv"}
ESTADOS_RUINS = ("FAILED", "REJECTED", "UNAVAILABLE")
ESPERA_VIDEOS_MIN = 8        # minutos lendo o processamento. Vídeo mais longo: rode `videos` de novo, ele continua
PAUSA_LEITURA_SEG = 20


def confirmar(texto, executar, no_chat):
    if not executar:
        print("\nPRÉVIA: nada foi escrito. Com o ok escrito de quem decide, rode de novo com --executar.")
        return False
    if no_chat:
        print(f"\n[confirmado no chat depois deste resumo] {texto}")
        return True
    try:
        r = input(f"\n{texto}\nDigite exatamente: confirmo\n> ").strip().lower()
    except EOFError:
        print("\nSem terminal pra digitar. Mostre o resumo, espere o ok escrito e rode com "
              "--confirmado-no-chat. Nada foi escrito.")
        return False
    if r != "confirmo":
        print(f'Cancelado: recebi "{r}". Nada foi escrito.')
        return False
    return True


def carregar(arq, chaves=("customer_id",)):
    reg = gr.carrega(arq)
    reg.setdefault("criativos", {})
    G = reg.get("google") or {}
    faltam = [f"google.{k}" for k in chaves if not G.get(k)]
    if faltam:
        sys.exit("PAREI: o registro não tem " + ", ".join(faltam) + ". Modelo em "
                 "sirius-scale/ferramentas/google/modelos/campanhas.exemplo.json.")
    return reg, G, comum.so_digitos(G["customer_id"])


def salvar(arq, reg):
    """Grava num temporário e troca de uma vez: processo morto no meio não deixa o registro pela metade."""
    tmp = f"{arq}.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=2, ensure_ascii=False)
        f.write("\n")
    os.replace(tmp, arq)


def checar_textos(an, campos=LIMITES):
    faltas = []
    for campo, lim in campos.items():
        if not an.get(campo):
            faltas.append(f"anúncio sem {campo}")
        for t in an.get(campo) or []:
            if len(t) > lim:
                faltas.append(f"{campo} com {len(t)} > {lim}: {t!r}")
    return faltas


def asset_video(g, cid, yt_id):
    for r in g.search(customer_id=cid, query=f"""SELECT asset.resource_name FROM asset
            WHERE asset.type = 'YOUTUBE_VIDEO' AND asset.youtube_video_asset.youtube_video_id = '{yt_id}'"""):
        return r.asset.resource_name
    return None


def aplicar_metas(cli, g, cid, camp_id, pares):
    """O Google cria as metas sozinho. Só as do registro ficam biddable, e o que vale é o lido depois (§2)."""
    quer = {tuple(p) for p in pares}
    ops = []
    for r in g.search(customer_id=cid, query=f"""SELECT campaign_conversion_goal.category,
            campaign_conversion_goal.origin, campaign_conversion_goal.biddable
            FROM campaign_conversion_goal WHERE campaign.id = {camp_id}"""):
        cat, org = r.campaign_conversion_goal.category.name, r.campaign_conversion_goal.origin.name
        op = cli.get_type("MutateOperation")
        o = op.campaign_conversion_goal_operation
        o.update.resource_name = f"customers/{cid}/campaignConversionGoals/{camp_id}~{cat}~{org}"
        o.update.biddable = (cat, org) in quer
        o.update_mask.paths.append("biddable")
        ops.append(op)
    if ops:
        gr.mutate(cli, cid, ops, validar=False, rotulos=["meta de conversão"] * len(ops))
    return sorted((r.campaign_conversion_goal.category.name, r.campaign_conversion_goal.origin.name)
                  for r in g.search(customer_id=cid, query=f"""SELECT campaign_conversion_goal.category,
                     campaign_conversion_goal.origin, campaign_conversion_goal.biddable
                     FROM campaign_conversion_goal WHERE campaign.id = {camp_id}""")
                  if r.campaign_conversion_goal.biddable)


def nome_anuncio(i, cr):
    return f"AD - {i} - {cr['slug']}"


def videos_do(cr):
    return [x for x in (cr.get("youtube_id"), cr.get("youtube_id_169")) if x]


def imagens_do(cr):
    """Arquivos do estático por formato. Paisagem e quadrado moram em `google`; feed e story são os da Meta."""
    gg = cr.get("google") or {}
    arqs = {"paisagem": gg.get("paisagem"), "quadrado": gg.get("quadrado"), "feed": cr.get("feed"),
            "story": cr.get("story")}
    return {k: v for k, v in arqs.items() if v}


def problemas_imagens(cr):
    """Sem paisagem E quadrado a API recusa com ASPECT_RATIO_NOT_ALLOWED, sem dizer que falta um formato (§19)."""
    p, arqs = [], imagens_do(cr)
    for k, _, prop in CAMPOS_IMAGEM:
        arq = arqs.get(k)
        if not arq:
            if k in ("paisagem", "quadrado"):
                p.append(f"estático sem {k} (o Google exige paisagem e quadrado)")
            continue
        caminho = comum.caminho(arq)
        dim = gr.dim_png(caminho) if os.path.exists(caminho) else None
        if not dim:
            p.append(f"{k}: arquivo não existe ou não é PNG ({arq})")
        elif abs(dim[0] / dim[1] - prop) > 0.02:
            p.append(f"{k}: {dim[0]}x{dim[1]} fora da proporção do formato")
    return p


def pronto(cr):
    return not problemas_imagens(cr) if cr.get("tipo") == "imagem" else bool(videos_do(cr))


def resolve_listas(G, existentes):
    """incluir/excluir do grupo de cada campanha -> ids de lista. Chave numérica = id; '[TAG]' = o incluir
    do grupo cujo nome tem [TAG] (em qualquer campanha do registro); outro texto = NOME da lista (pendente
    se ainda não existe: o comando `listas` cria). Devolve (inc, exc, faltas, pendentes)."""
    grupos = [c["grupo"] for c in G["campanhas"]]
    por_nome = {}
    for k, v in existentes.items():
        por_nome.setdefault(v["nome"], []).append(k)
    faltas, pendentes = [], []

    def chave(gn, k, v):
        if k.isdigit():
            if k not in existentes:
                faltas.append(f"{gn}: lista {k} ({v}) não existe na conta")
                return []
            return [k]
        ach = por_nome.get(k, [])
        if not ach:
            pendentes.append(f"{gn}: lista '{k}' ainda não existe na conta (comando `listas`)")
            return []
        if len(ach) > 1:
            faltas.append(f"{gn}: lista '{k}' existe {len(ach)}x na conta")
            return []
        return ach

    inc = {}
    for gp in grupos:
        ids = []
        for k, v in gp["incluir"].items():
            ids += chave(gp["nome"], k, v)
        inc[gp["nome"]] = list(dict.fromkeys(ids))
    exc = {}
    for gp in grupos:
        ids = []
        for k, v in (gp.get("excluir") or {}).items():
            if k.startswith("[") and k.endswith("]"):
                alvo = next((x for x in grupos if k in x["nome"]), None)
                if not alvo:
                    faltas.append(f"{gp['nome']}: excluir '{k}' não acha grupo {k}")
                else:
                    ids += inc[alvo["nome"]]
            else:
                ids += chave(gp["nome"], k, v)
        exc[gp["nome"]] = [i for i in dict.fromkeys(ids) if i not in inc[gp["nome"]]]
    return inc, exc, faltas, pendentes


def op_anuncio(cli, cid, G, C, rn_ag, i, cr, rn_videos):
    op = cli.get_type("MutateOperation")
    x = op.ad_group_ad_operation.create
    x.ad_group = rn_ag
    x.status = cli.enums.AdGroupAdStatusEnum.PAUSED
    x.ad.name = nome_anuncio(i, cr)
    x.ad.final_urls.append(C["pagina"])
    x.ad.final_url_suffix = G["final_url_suffix"]
    d = x.ad.demand_gen_video_responsive_ad
    d.business_name.text = G["business_name"]
    for rn in rn_videos:
        v = cli.get_type("AdVideoAsset"); v.asset = rn; d.videos.append(v)
    lg = cli.get_type("AdImageAsset"); lg.asset = f"customers/{cid}/assets/{G['logo_asset']}"; d.logo_images.append(lg)
    if G.get("cta_asset"):
        ct = cli.get_type("AdCallToActionAsset"); ct.asset = f"customers/{cid}/assets/{G['cta_asset']}"
        d.call_to_actions.append(ct)
    for campo in ("headlines", "long_headlines", "descriptions"):
        for t in cr["google"][campo]:
            ta = cli.get_type("AdTextAsset"); ta.text = t; getattr(d, campo).append(ta)
    return op


def op_anuncio_imagem(cli, cid, G, C, rn_ag, i, cr, rns):
    """Estático: demand_gen_multi_asset_ad (§19). O formato não tem título longo nem asset de botão."""
    op = cli.get_type("MutateOperation")
    x = op.ad_group_ad_operation.create
    x.ad_group = rn_ag
    x.status = cli.enums.AdGroupAdStatusEnum.PAUSED
    x.ad.name = nome_anuncio(i, cr)
    x.ad.final_urls.append(C["pagina"])
    x.ad.final_url_suffix = G["final_url_suffix"]
    m = x.ad.demand_gen_multi_asset_ad
    m.business_name = G["business_name"]
    for k, campo, _ in CAMPOS_IMAGEM:
        if k in rns:
            im = cli.get_type("AdImageAsset"); im.asset = rns[k]; getattr(m, campo).append(im)
    lg = cli.get_type("AdImageAsset"); lg.asset = f"customers/{cid}/assets/{G['logo_asset']}"; m.logo_images.append(lg)
    for campo in ("headlines", "descriptions"):
        for t in cr["google"][campo]:
            ta = cli.get_type("AdTextAsset"); ta.text = t; getattr(m, campo).append(ta)
    return op


def op_asset_video(cli, rn, nome, yt):
    op = cli.get_type("MutateOperation")
    a = op.asset_operation.create
    if rn:
        a.resource_name = rn
    a.name = nome
    a.youtube_video_asset.youtube_video_id = yt
    return op


def ops_midia_e_anuncios(cli, g, cid, G, C, rn_ag, reg, ids, T):
    """Os assets que faltam (vídeo do YouTube ou imagem do estático, com id temporário) e um anúncio por
    criativo, na ordem do registro. Imagem com o mesmo conteúdo já na conta é reaproveitada (o nome leva o hash)."""
    ops, rot, rn_por_yt, rn_por_arq = [], [], {}, {}
    for i in ids:
        cr = reg["criativos"][i]
        if cr.get("tipo") == "imagem":
            rns = {}
            for k, arq in imagens_do(cr).items():
                caminho = comum.caminho(arq)
                if caminho not in rn_por_arq:
                    n = gr.nome_asset(caminho)
                    rn = gr.assets_existentes(g, cid, [n]).get(n)
                    if not rn:
                        rn = T(cid, "assets")
                        ops.append(gr.op_imagem(cli, rn, caminho)); rot.append(f"imagem {i} ({k})")
                    rn_por_arq[caminho] = rn
                rns[k] = rn_por_arq[caminho]
            ops.append(op_anuncio_imagem(cli, cid, G, C, rn_ag, i, cr, rns)); rot.append(f"anuncio {nome_anuncio(i, cr)}")
            continue
        rns = []
        for yt in videos_do(cr):
            if yt not in rn_por_yt:
                rn = asset_video(g, cid, yt)
                if not rn:
                    rn = T(cid, "assets")
                    ops.append(op_asset_video(cli, rn, f"{reg.get('lancamento', 'video')} · {i} · {yt}", yt))
                    rot.append(f"asset do video {i} ({yt})")
                rn_por_yt[yt] = rn
            rns.append(rn_por_yt[yt])
        ops.append(op_anuncio(cli, cid, G, C, rn_ag, i, cr, rns)); rot.append(f"anuncio {nome_anuncio(i, cr)}")
    return ops, rot


def cadeia(cli, g, cid, G, C, inc, exc, reg, ids):
    """A campanha inteira, com IDs temporários, nascendo PAUSED nos três níveis."""
    T = gr.Temp()
    ops, rot = [], []
    rn_bud = T(cid, "campaignBudgets")
    ops.append(gr.op_orcamento(cli, rn_bud, C["nome"], C["orcamento_dia_brl"])); rot.append("orcamento")
    rn_camp = T(cid, "campaigns")
    op = cli.get_type("MutateOperation")
    c = op.campaign_operation.create
    c.resource_name = rn_camp
    c.name = C["nome"]
    c.advertising_channel_type = cli.enums.AdvertisingChannelTypeEnum.DEMAND_GEN
    c.status = cli.enums.CampaignStatusEnum.PAUSED
    c.campaign_budget = rn_bud
    if G["lance"] == "MAXIMIZE_CLICKS":
        c.target_spend.target_spend_micros = 0
    else:
        c.maximize_conversions.target_cpa_micros = 0
    c.network_settings.target_content_network = True                # campanha nova nasce False (§25, §31)
    c.end_date_time = C.get("fim") or G["fim"]
    c.contains_eu_political_advertising = (
        cli.enums.EuPoliticalAdvertisingStatusEnum.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING)   # §8
    ops.append(op); rot.append("campanha")
    gp = C["grupo"]
    rn_ag = T(cid, "adGroups")
    op = cli.get_type("MutateOperation")
    ag = op.ad_group_operation.create
    ag.resource_name = rn_ag
    ag.name = gp["nome"]
    ag.campaign = rn_camp
    ag.status = cli.enums.AdGroupStatusEnum.PAUSED
    ag.optimized_targeting_enabled = False                           # o Advantage+ do Google
    ops.append(op); rot.append(f"grupo {gp['nome']}")
    rn_aud = T(cid, "audiences")
    op = cli.get_type("MutateOperation")
    au = op.audience_operation.create
    au.resource_name = rn_aud
    au.name = gp["audience_nome"]
    dim = cli.get_type("AudienceDimension")
    for lid in inc[gp["nome"]]:
        sg = cli.get_type("AudienceSegment")
        sg.user_list.user_list = f"customers/{cid}/userLists/{lid}"
        dim.audience_segments.segments.append(sg)
    au.dimensions.append(dim)
    if exc[gp["nome"]]:
        exd = cli.get_type("AudienceExclusionDimension")
        for lid in exc[gp["nome"]]:
            ex = cli.get_type("ExclusionSegment")
            ex.user_list.user_list = f"customers/{cid}/userLists/{lid}"
            exd.exclusions.append(ex)
        au.exclusion_dimension = exd
    ops.append(op); rot.append(f"audience {gp['audience_nome']}")
    op = cli.get_type("MutateOperation")
    op.ad_group_criterion_operation.create.ad_group = rn_ag
    op.ad_group_criterion_operation.create.audience.audience = rn_aud
    ops.append(op); rot.append(f"grupo {gp['nome']} usa a audience")
    op = cli.get_type("MutateOperation")
    op.ad_group_criterion_operation.create.ad_group = rn_ag
    op.ad_group_criterion_operation.create.location.geo_target_constant = f"geoTargetConstants/{G['geo']}"  # §6
    ops.append(op); rot.append(f"geo no grupo {gp['nome']}")
    o2, r2 = ops_midia_e_anuncios(cli, g, cid, G, C, rn_ag, reg, ids, T)
    return ops + o2, rot + r2


def le_anuncios(g, cid, camp_id):
    out = {}
    for r in g.search(customer_id=cid, query=f"""SELECT ad_group_ad.ad.name, ad_group_ad.status,
            ad_group_ad.ad.final_urls, ad_group_ad.ad.final_url_suffix,
            ad_group_ad.ad.demand_gen_video_responsive_ad.videos,
            ad_group_ad.ad.demand_gen_video_responsive_ad.call_to_actions,
            ad_group_ad.ad.demand_gen_video_responsive_ad.headlines,
            ad_group_ad.ad.demand_gen_multi_asset_ad.marketing_images,
            ad_group_ad.ad.demand_gen_multi_asset_ad.square_marketing_images,
            ad_group_ad.ad.demand_gen_multi_asset_ad.portrait_marketing_images,
            ad_group_ad.ad.demand_gen_multi_asset_ad.tall_portrait_marketing_images,
            ad_group_ad.ad.demand_gen_multi_asset_ad.headlines,
            ad_group_ad.policy_summary.approval_status
            FROM ad_group_ad WHERE campaign.id = {camp_id} AND ad_group_ad.status != 'REMOVED'"""):
        a = r.ad_group_ad
        d = a.ad.demand_gen_video_responsive_ad
        m = a.ad.demand_gen_multi_asset_ad
        out[a.ad.name] = {"status": a.status.name, "url": list(a.ad.final_urls), "sufixo": a.ad.final_url_suffix,
                          "videos": len(d.videos), "cta": len(d.call_to_actions),
                          "headlines": len(d.headlines) or len(m.headlines),
                          "imagens": sum(len(getattr(m, campo)) for _, campo, _ in CAMPOS_IMAGEM),
                          "aprov": a.policy_summary.approval_status.name}
    return out


def problemas_lidos(d, ads_lidos, G, C, inc, exc, reg, esperados, nova=True, novos=()):
    """Compara o que a plataforma devolveu com o registro. `nova`: a campanha acabou de nascer, então ela e o
    grupo têm que estar PAUSED; campanha que já existia pode estar ligada. Anúncio criado nesta rodada (`novos`)
    tem que estar PAUSED sempre."""
    p = []
    if nova and d.get("status") != "PAUSED":
        p.append(f"campanha {d.get('status')} (esperado PAUSED)")
    if nova and d.get("lance") != LANCES[G["lance"]]:
        p.append(f"lance {d.get('lance')} (esperado {LANCES[G['lance']]})")
    if d.get("fim", "")[:16] != (C.get("fim") or G["fim"])[:16]:
        p.append(f"fim {d.get('fim')} (esperado {C.get('fim') or G['fim']})")
    if abs(d.get("orcamento", 0) - C["orcamento_dia_brl"]) > 0.01:
        p.append(f"orçamento {d.get('orcamento')} (esperado {C['orcamento_dia_brl']})")
    gp = C["grupo"]
    x = next((v for v in d["grupos"].values() if v["nome"] == gp["nome"]), None)
    if not x:
        return p + [f"grupo {gp['nome']} não voltou na leitura"]
    if nova and x["status"] != "PAUSED":
        p.append(f"grupo {x['status']} (esperado PAUSED)")
    if x["ot"]:
        p.append("segmentação otimizada LIGADA")
    if x["geo"] != {str(G["geo"])}:
        p.append(f"geo {sorted(x['geo']) or 'NENHUMA'}")
    if sorted(set(x["inclui"])) != sorted(set(inc[gp["nome"]])):
        p.append(f"inclui {sorted(set(x['inclui']))} (esperado {sorted(set(inc[gp['nome']]))})")
    if sorted(set(x["exclui"])) != sorted(set(exc[gp["nome"]])):
        p.append(f"exclui {sorted(set(x['exclui']))} (esperado {sorted(set(exc[gp['nome']]))})")
    for i in esperados:
        cr = reg["criativos"][i]
        a = ads_lidos.get(nome_anuncio(i, cr))
        if not a:
            p.append(f"anúncio {nome_anuncio(i, cr)} não voltou na leitura")
            continue
        if a["url"] != [C["pagina"]]:
            p.append(f"{nome_anuncio(i, cr)}: url final {a['url']}")
        if a["sufixo"] != G["final_url_suffix"]:
            p.append(f"{nome_anuncio(i, cr)}: sufixo {a['sufixo']!r}")
        if cr.get("tipo") == "imagem":
            if a["imagens"] != len(imagens_do(cr)):
                p.append(f"{nome_anuncio(i, cr)}: {a['imagens']} imagem(ns) (esperado {len(imagens_do(cr))})")
        else:
            if a["videos"] != len(videos_do(cr)):
                p.append(f"{nome_anuncio(i, cr)}: {a['videos']} vídeo(s) (esperado {len(videos_do(cr))})")
            if G.get("cta_asset") and a["cta"] != 1:
                p.append(f"{nome_anuncio(i, cr)}: sem botão")
        if i in novos and a["status"] != "PAUSED":
            p.append(f"{nome_anuncio(i, cr)}: anúncio novo {a['status']} (esperado PAUSED)")
    return p


def imprimir_bloqueios(faltas):
    print("\n  !!! BLOQUEIOS (nada foi escrito):")
    for f in faltas:
        print(f"     - {f}")
    sys.exit(1)


def cmd_criar(args):
    reg, G, cid = carregar(args.registro, OBRIGATORIOS)
    teto = comum.teto_campanha(obrigatorio=False)
    cli = comum.cliente()
    g = cli.get_service("GoogleAdsService")
    existentes = gr.listas_existentes(g, cid)
    inc, exc, faltas, pendentes = resolve_listas(G, existentes)
    campanhas = [C for C in G["campanhas"] if not args.campanha or args.campanha in C["nome"]]
    if not campanhas:
        return print(f"  nenhuma campanha do registro tem '{args.campanha}' no nome")
    da_rodada = lambda x: any(x.startswith(C["grupo"]["nome"] + ":") for C in campanhas)
    faltas = [x for x in faltas if da_rodada(x)]
    pendentes = [x for x in pendentes if da_rodada(x)]
    if args.executar:
        faltas += pendentes
    if G["lance"] not in LANCES:
        faltas.append(f"google.lance {G['lance']}: aceito {', '.join(LANCES)}")
    if not G.get("logo_asset"):
        faltas.append("google.logo_asset vazio: rode o comando `marca` antes")
    plano = []
    for C in campanhas:
        gp = C["grupo"]
        if teto is not None and C["orcamento_dia_brl"] > teto:
            faltas.append(f"{C['nome']}: {comum.brl(C['orcamento_dia_brl'])}/dia acima do teto de {comum.brl(teto)}/dia")
        if not inc[gp["nome"]] and not any(x.startswith(gp["nome"] + ":") for x in pendentes):
            faltas.append(f"{gp['nome']}: grupo sem lista em `incluir`")
        camp_id = gr.campanha_por_nome(g, cid, C["nome"], "DEMAND_GEN")
        prontos, sem_midia = [], []
        for i in C["anuncios"]:
            cr = reg["criativos"].get(i)
            if not cr:
                faltas.append(f"{C['nome']}: anúncio {i} não está em `criativos`")
                continue
            imagem = cr.get("tipo") == "imagem"
            for x in checar_textos(cr.get("google") or {}, {k: LIMITES[k] for k in LIMITES if not (imagem and k == "long_headlines")}):
                faltas.append(f"{i}: {x}")
            if imagem:
                faltas += [f"{i}: {x}" for x in problemas_imagens(cr)]
            (prontos if pronto(cr) else sem_midia).append(i)
        ja, rn_ag = {}, None
        if camp_id:
            rn_ag, ja = gr.grupo_e_anuncios(g, cid, camp_id, gp["nome"])
            if not rn_ag:
                faltas.append(f"{C['nome']}: a campanha existe ({camp_id}) mas o grupo {gp['nome']} não")
        novos = [i for i in prontos if nome_anuncio(i, reg["criativos"][i]) not in ja]
        plano.append((C, camp_id, rn_ag, novos, sem_midia, ja))
    print("=" * 84 + f"\nGOOGLE DEMAND GEN · {reg.get('lancamento', '')} · {reg.get('fase', '')}\n" + "=" * 84)
    print(f"  Conta : {cid} · tudo nasce PAUSADO · quem liga é o dono da conta, na tela do Google Ads")
    print(f"  Lance : {G['lance']} · metas biddable {[tuple(x) for x in G['metas_biddable']]} · fim {G['fim']}")
    print(f"  UTM   : sufixo {G['final_url_suffix']}")
    print(f"  Teto  : {comum.brl(teto) + '/dia por campanha' if teto is not None else 'TETO_CAMPANHA_DIA não está no .env: a prévia roda, mas --executar vai parar'}")
    for C, camp_id, rn_ag, novos, sem_midia, ja in plano:
        gp = C["grupo"]
        print(f"\n  CAMPANHA {C['nome']} {'(já existe: ' + camp_id + ')' if camp_id else '(nova)'}")
        print(f"    {comum.brl(C['orcamento_dia_brl'])}/dia · destino {C['pagina']} · grupo {gp['nome']} · "
              f"segmentação otimizada DESLIGADA · geo {G['geo']}")
        print(f"    inclui {len(inc[gp['nome']])}: " + "; ".join(f"{existentes[i]['nome']} ({existentes[i]['disp']})" for i in inc[gp["nome"]]))
        if exc[gp["nome"]]:
            print(f"    exclui {len(exc[gp['nome']])}: " + "; ".join(existentes[i]["nome"] for i in exc[gp["nome"]]))
        for i in C["anuncios"]:
            cr = reg["criativos"].get(i)
            if not cr:
                continue
            n = nome_anuncio(i, cr)
            st = "já existe" if n in ja else ("cria agora, pausado" if i in novos else "SEM MÍDIA (entra depois)")
            midia = f"imagens {sorted(imagens_do(cr))}" if cr.get("tipo") == "imagem" else f"vídeos {videos_do(cr)}"
            print(f"      {n:<40} {st} · {midia}")
    for x in pendentes:
        print(f"\n  ⚠ {x}: pré-requisito do --executar")
    if faltas:
        imprimir_bloqueios(faltas)
    lotes = []
    for C, camp_id, rn_ag, novos, sem_midia, ja in plano:
        gp = C["grupo"]
        if not camp_id and not novos:
            print(f"\n  --  {C['nome']}: nenhuma peça pronta ainda (vídeo no YouTube ou estático; o comando `videos` sobe o vídeo); a campanha espera a primeira")
            continue
        if not novos:
            continue
        if not camp_id and not inc[gp["nome"]]:
            print(f"\n  --  {C['nome']}: não validei, o grupo ainda não tem nenhuma lista existente")
            continue
        if camp_id:
            ops, rot = ops_midia_e_anuncios(cli, g, cid, G, C, rn_ag, reg, novos, gr.Temp())
        else:
            ops, rot = cadeia(cli, g, cid, G, C, inc, exc, reg, novos)
        gr.mutate(cli, cid, ops, validar=True, rotulos=rot)
        print(f"  ok  validação a seco (validate_only): {C['nome']}: {len(ops)} operações aceitas pelo Google")
        lotes.append((C, camp_id, ops, rot, novos))
    if not lotes:
        return print("\n  nada a criar")
    n_camp = sum(1 for C, camp_id, *_ in lotes if not camp_id)
    n_ads = sum(len(x[4]) for x in lotes)
    if not confirmar(f"Isto cria {n_camp} campanha(s) e {n_ads} anúncio(s) no Google, TUDO PAUSADO.",
                     args.executar, args.confirmado_no_chat):
        return
    criadas = []
    for C, camp_id, ops, rot, novos in lotes:
        nova = not camp_id
        r = gr.mutate(cli, cid, ops, validar=False, rotulos=rot)
        if nova:
            camp_id = gr.id_temporario_para_real(r, rot, "campanha")[0].split("/")[-1]
            C["id"] = camp_id                # grava antes de seguir: daqui em diante a campanha existe
            print(f"  ok  {C['nome']}: cadeia escrita (atômica), campanha {camp_id}")
        else:
            print(f"  ok  {C['nome']}: {len(novos)} anúncio(s) novo(s) na campanha {camp_id}")
        reg.setdefault("historico", []).append({"data": time.strftime("%Y-%m-%d"),
                                                "o_que": f"Google: {C['nome']} ({camp_id}) · anúncios criados PAUSADOS: {', '.join(novos)}"})
        salvar(args.registro, reg)
        criadas.append(camp_id)
        if nova:
            metas = aplicar_metas(cli, g, cid, camp_id, G["metas_biddable"])
            print(f"      metas biddable lidas de volta: {metas}")
            if sorted(tuple(x) for x in G["metas_biddable"]) != metas:
                print("  !!! as metas lidas não batem com o registro. A campanha fica PAUSADA e parei aqui.")
                sys.exit(1)
        d = gr.le_campanha(g, cid, camp_id)
        ads_lidos = le_anuncios(g, cid, camp_id)
        esperados = [i for i in C["anuncios"] if nome_anuncio(i, reg["criativos"][i]) in ads_lidos or i in novos]
        print(gr.resumo_leitura(d))
        probs = problemas_lidos(d, ads_lidos, G, C, inc, exc, reg, esperados, nova=nova, novos=novos)
        if probs:
            print("  !!! LEITURA DE VOLTA reprovou:")
            for x in probs:
                print(f"     - {x}")
            sys.exit(1)
    print(f"\n  Tudo PAUSADO e lido de volta. Falta a conferência: conferir_campanha.py --conta {cid} --id "
          f"<id> (--referencia <id da irmã> ou --sem-referencia), em {', '.join(criadas)}.")
    print("  Quem liga é o dono da conta, na tela do Google Ads.")


def cmd_marca(args):
    """Logo e botão dos anúncios (`logo_asset` e `cta_asset` do registro) numa conta que ainda não tem. Cria a
    partir de `logo_arquivo` (PNG 1:1) e `cta` (o tipo do botão: SIGN_UP = "Inscreva-se", LEARN_MORE = "Saiba
    mais"); reaproveita a imagem com o mesmo conteúdo e o botão do mesmo tipo que já existirem. Grava os ids."""
    reg, G, cid = carregar(args.registro)
    cli = comum.cliente()
    g = cli.get_service("GoogleAdsService")
    ops, rot, achados = [], [], {}
    if not G.get("logo_asset"):
        if not G.get("logo_arquivo"):
            sys.exit("PAREI: o registro não tem google.logo_arquivo nem google.logo_asset.")
        arq = comum.caminho(G["logo_arquivo"])
        dim = gr.dim_png(arq) if os.path.exists(arq) else None
        if not dim or dim[0] != dim[1] or dim[0] < 128:
            sys.exit(f"PAREI: a logo precisa ser PNG quadrado de 128 px ou mais: {G['logo_arquivo']} ({dim})")
        n = gr.nome_asset(arq)
        rn = gr.assets_existentes(g, cid, [n]).get(n)
        if rn:
            achados["logo_asset"] = rn.split("/")[-1]
        else:
            ops.append(gr.op_imagem(cli, gr.Temp()(cid, "assets"), arq)); rot.append("logo_asset")
        print(f"  logo : {G['logo_arquivo']} ({dim[0]}x{dim[1]}) · {'já existe na conta' if rn else 'cria'}")
    if not G.get("cta_asset") and G.get("cta"):
        tipo = cli.enums.CallToActionTypeEnum[G["cta"]]
        rn = next((r.asset.resource_name for r in g.search(customer_id=cid, query=f"""SELECT asset.resource_name
                FROM asset WHERE asset.type = 'CALL_TO_ACTION'
                AND asset.call_to_action_asset.call_to_action = '{G['cta']}'""")), None)
        if rn:
            achados["cta_asset"] = rn.split("/")[-1]
        else:
            op = cli.get_type("MutateOperation")
            op.asset_operation.create.call_to_action_asset.call_to_action = tipo
            ops.append(op); rot.append("cta_asset")
        print(f"  botão: {G['cta']} · {'já existe na conta' if rn else 'cria'}")
    if not ops and not achados:
        return print("  nada a fazer: o registro já tem logo_asset e cta_asset")
    if ops:
        gr.mutate(cli, cid, ops, validar=True, rotulos=rot)
        print(f"  ok  validação a seco aceita ({len(ops)} asset(s))")
    if not confirmar(f"Isto cria {len(ops)} asset(s) na conta {cid} (logo/botão, não mexe em campanha) e grava os ids no registro.",
                     args.executar, args.confirmado_no_chat):
        return
    if ops:
        r = gr.mutate(cli, cid, ops, validar=False, rotulos=rot)
        for chave, resp in zip(rot, r.mutate_operation_responses):
            achados[chave] = resp.asset_result.resource_name.split("/")[-1]
    lidos = {}
    for chave, aid in achados.items():
        for x in g.search(customer_id=cid, query=f"""SELECT asset.id, asset.type, asset.name,
                asset.call_to_action_asset.call_to_action FROM asset WHERE asset.id = {aid}"""):
            lidos[chave] = f"{x.asset.type_.name} {x.asset.call_to_action_asset.call_to_action.name if chave == 'cta_asset' else x.asset.name}"
        print(f"  ok  {chave} = {aid} · lido de volta: {lidos.get(chave, 'NÃO VOLTOU')}")
    if len(lidos) != len(achados):
        print("  !!! nem todo asset voltou na leitura; não gravei no registro")
        sys.exit(1)
    G.update(achados)
    reg.setdefault("historico", []).append({"data": time.strftime("%Y-%m-%d"),
                                            "o_que": f"Google: logo/botão da conta {cid}: {achados}"})
    salvar(args.registro, reg)


def cmd_listas(args):
    """Cria as listas por regra de URL de google.listas_novas que ainda não existem (pelo nome), pela receita
    do registro.py (um operando por trecho, OU; lookback = dias; pré-populada), e lê de volta."""
    reg, G, cid = carregar(args.registro)
    cli = comum.cliente()
    g = cli.get_service("GoogleAdsService")
    nomes = {v["nome"] for v in gr.listas_existentes(g, cid).values()}
    specs = []
    for l in G.get("listas_novas") or []:
        if l["nome"] in nomes:
            print(f"  --  já existe: {l['nome']}")
            continue
        specs.append({"nome": l["nome"], "descricao": l.get("_por_que", ""), "membership_life_span": l["dias"],
                      "contem": l["urls"], "prepopulation": True})
    if not specs:
        return print("  nada a criar")
    for s in specs:
        print(f"  +   {s['nome']}: visitou URL com {' OU '.join(repr(u) for u in s['contem'])} · "
              f"{s['membership_life_span']} dias · pré-populada")
        gr.mutate(cli, cid, [gr.op_lista_regra(cli, cid, s)], validar=True, rotulos=[f"lista {s['nome']}"])
    print(f"  ok  validação a seco aceita ({len(specs)} lista(s))")
    if not confirmar(f"Isto cria {len(specs)} lista(s) de público no Google Ads (não mexe em campanha).",
                     args.executar, args.confirmado_no_chat):
        return
    for s in specs:
        rn = gr.cria_lista_e_confere(cli, g, cid, s)
        reg.setdefault("historico", []).append({"data": time.strftime("%Y-%m-%d"),
                                                "o_que": f"lista criada no Google: {s['nome']} ({rn.split('/')[-1]})"})
        salvar(args.registro, reg)


def ops_anexar(cli, g, cid, reg, trocas):
    """Assets que faltam + um update por anúncio, num Mutate só: dá pra validar a seco e a escrita é atômica.
    `videos` é editável in-place, a lista inteira (§5)."""
    T = gr.Temp()
    ops, rot, rn_por_yt = [], [], {}
    for camp_id, aid, nome, st, i, quer in trocas:
        rns = []
        for yt in quer:
            if yt not in rn_por_yt:
                rn = asset_video(g, cid, yt)
                if not rn:
                    rn = T(cid, "assets")
                    ops.append(op_asset_video(cli, rn, f"{reg.get('lancamento', 'video')} · {i} · {yt}", yt))
                    rot.append(f"asset do video {i} ({yt})")
                rn_por_yt[yt] = rn
            rns.append(rn_por_yt[yt])
        op = cli.get_type("MutateOperation")
        o = op.ad_operation
        o.update.resource_name = f"customers/{cid}/ads/{aid}"
        for rn in rns:
            v = cli.get_type("AdVideoAsset"); v.asset = rn
            o.update.demand_gen_video_responsive_ad.videos.append(v)
        o.update_mask.paths.append("demand_gen_video_responsive_ad.videos")
        ops.append(op); rot.append(f"anuncio {nome}")
    return ops, rot


def videos_a_subir(reg):
    """Cada vídeo do registro que tem arquivo e ainda não tem id no YouTube, na ordem do registro."""
    fila = []
    for i, cr in reg["criativos"].items():
        if cr.get("tipo") == "imagem":
            continue
        for formato, c_arq, c_id, c_up in FORMATOS_VIDEO:
            if (cr.get(c_arq) or cr.get(c_up)) and not cr.get(c_id):
                fila.append({"i": i, "cr": cr, "formato": formato, "arquivo": cr.get(c_arq), "c_id": c_id, "c_up": c_up,
                             "rotulo": f"{i} ({formato})"})
    return fila


def anotar_video(arq, v, o_que=None, **campos):
    """Subir demora: relê o registro do disco e mexe só nos campos deste vídeo, pra não desfazer o que alguém editou
    no arquivo nesse meio-tempo. Valor None apaga o campo."""
    reg = gr.carrega(arq)
    cr = reg.get("criativos", {}).get(v["i"])
    for alvo in (v["cr"], cr):
        for k, val in campos.items():
            if alvo is None:
                continue
            if val is None:
                alvo.pop(k, None)
            else:
                alvo[k] = val
    if o_que:
        reg.setdefault("historico", []).append({"data": time.strftime("%Y-%m-%d"), "o_que": o_que})
    salvar(arq, reg)


def problema_arquivo(v):
    caminho = comum.caminho(v["arquivo"])
    if not os.path.isfile(caminho):
        return f"{v['rotulo']}: o arquivo não existe ({v['arquivo']})"
    if os.path.splitext(caminho)[1].lower() not in EXTENSOES_VIDEO:
        return f"{v['rotulo']}: formato que o YouTube não aceita ({v['arquivo']})"
    if not os.path.getsize(caminho):
        return f"{v['rotulo']}: o arquivo está vazio ({v['arquivo']})"
    return None


def sem_sinais(texto):
    """O YouTube recusa < e > no título e na descrição."""
    return str(texto).replace("<", "").replace(">", "")


def titulo_video(reg, v):
    """Só quem abre o vídeo vê: lançamento, peça e formato, pra achar depois. O YouTube limita a 100."""
    partes = [reg.get("lancamento"), v["i"], v["cr"].get("slug"), "16x9" if v["formato"] == "16:9" else None]
    return sem_sinais(" · ".join(str(p) for p in partes if p))[:100]


def motivo(e):
    """A subida vai por REST: a URL abre a mensagem do erro, e o motivo de verdade fica no fim dela."""
    falhas = getattr(getattr(e, "failure", None), "errors", None)
    return "; ".join(x.message for x in falhas) if falhas else str(e)[-500:]


def subir_video(cli, cid, reg, v, canal):
    """Sobe um arquivo pela API do Google Ads e devolve o resource_name do upload. Sempre não listado: vídeo público
    é decisão de conteúdo. Sem `canal`, o vídeo fica num canal gerenciado pelo Google, ligado à conta de anúncios."""
    req = cli.get_type("CreateYouTubeVideoUploadRequest")
    req.customer_id = cid
    up = req.you_tube_video_upload
    up.video_title = titulo_video(reg, v)
    textos = (v["cr"].get("google") or {}).get("descriptions") or []
    if textos:
        up.video_description = sem_sinais(textos[0])
    up.video_privacy = cli.enums.YouTubeVideoPrivacyEnum.UNLISTED
    if canal:
        up.channel_id = canal
    sessao = cli.get_service("YouTubeVideoUploadService").create_you_tube_video_upload(request=req)
    with open(comum.caminho(v["arquivo"]), "rb") as f:
        return sessao.upload(f).resource_name


def le_upload(g, cid, rn):
    for r in g.search(customer_id=cid, query=f"""SELECT you_tube_video_upload.state, you_tube_video_upload.video_id,
            you_tube_video_upload.video_privacy, you_tube_video_upload.channel_id FROM you_tube_video_upload
            WHERE you_tube_video_upload.resource_name = '{rn}'"""):
        return r.you_tube_video_upload
    return None


def aguardar_videos(g, cid, arq, andamento, canal, minutos):
    """Lê cada upload até o YouTube responder. O id só entra no registro depois de PROCESSED e lido de volta (não
    listado e, se o registro pediu canal, no canal certo). Devolve o que deu errado; o que segue em `andamento`
    ficou sem resposta dentro da espera, e o upload continua gravado no registro."""
    ruins, fim = [], time.time() + minutos * 60
    while andamento:
        for v in list(andamento):
            try:
                lido = le_upload(g, cid, v["cr"][v["c_up"]])
            except Exception as e:              # leitura que cai não perde nada: o upload está no registro
                v["nota"] = f"a leitura falhou: {motivo(e)}"
                continue
            v["nota"] = None if lido else "o upload não aparece na conta. Se foi apagado, tire o campo do upload do criativo"
            st = lido.state.name if lido else None
            if st in ESTADOS_RUINS:
                anotar_video(arq, v, **{v["c_up"]: None})
                andamento.remove(v)
                ruins.append(f"{v['rotulo']}: o YouTube devolveu {st}. Esse vídeo não entrou; confira o arquivo. "
                             "Rodar de novo sobe outra vez")
            elif st == "PROCESSED" and lido.video_id:
                andamento.remove(v)
                errado = [] if lido.video_privacy.name == "UNLISTED" else [f"visibilidade {lido.video_privacy.name}"]
                if canal and lido.channel_id != canal:
                    errado.append(f"canal {lido.channel_id}")
                if errado:
                    ruins.append(f"{v['rotulo']}: LEITURA DE VOLTA reprovou ({', '.join(errado)}, vídeo "
                                 f"{lido.video_id}). O id não entrou no registro. Mostre isto a quem decide")
                    continue
                anotar_video(arq, v, o_que=f"YouTube, não listado: {v['rotulo']} -> {lido.video_id}",
                             **{v["c_id"]: lido.video_id, v["c_up"]: None})
                print(f"  ok  {v['rotulo']}: {lido.video_id}, não listado, lido de volta e gravado no registro", flush=True)
        if not andamento or time.time() >= fim:
            return ruins
        time.sleep(PAUSA_LEITURA_SEG)
    return ruins


def cmd_videos(args):
    """Põe no YouTube os vídeos que o registro tem em arquivo. Roda antes do `criar`: o anúncio precisa do id."""
    reg, G, cid = carregar(args.registro)
    canal = (G.get("youtube_canal") or "").strip()
    fila = videos_a_subir(reg)
    andamento = [v for v in fila if v["cr"].get(v["c_up"])]
    novos = [v for v in fila if not v["cr"].get(v["c_up"])]
    if not fila:
        return print("  nada a subir: todo vídeo com arquivo no registro já tem id no YouTube")
    faltas = [p for p in map(problema_arquivo, novos) if p]
    if canal and not re.fullmatch(r"UC[\w-]{22}", canal):
        faltas.append(f"google.youtube_canal {canal!r}: id de canal tem 24 caracteres e começa com UC")
    destino = f"no canal {canal}" if canal else "num canal gerenciado pelo Google, ligado à conta de anúncios"
    print("=" * 84 + f"\nVÍDEOS PRO YOUTUBE: sempre NÃO LISTADOS, {destino}\n" + "=" * 84)
    for v in novos:
        caminho = comum.caminho(v["arquivo"])
        tam = f"{os.path.getsize(caminho) / 1e6:6.0f} MB" if os.path.isfile(caminho) else "   ??? MB"
        print(f"  {v['rotulo']:<22} {tam} · '{titulo_video(reg, v)}'")
    for v in andamento:
        print(f"  {v['rotulo']:<22} já subiu, falta a resposta do YouTube")
    if faltas:
        imprimir_bloqueios(faltas)
    if not args.executar:
        return confirmar("", False, False)
    if novos and not confirmar(f"Isto sobe {len(novos)} vídeo(s) no YouTube, não listados.", True, args.confirmado_no_chat):
        return
    cli = comum.cliente()
    g = cli.get_service("GoogleAdsService")
    falhou = None
    for v in novos:
        print(f"  subindo {v['rotulo']}...", flush=True)
        try:
            rn = subir_video(cli, cid, reg, v, canal)
        except Exception as e:                  # a queda de um não apaga o que os anteriores já gravaram
            falhou = f"{v['rotulo']}: {motivo(e)}"
            break
        anotar_video(args.registro, v, **{v["c_up"]: rn})
        andamento.append(v)
    ruins = aguardar_videos(g, cid, args.registro, andamento, canal, args.espera)
    if andamento:
        print("\n  ⏳ o YouTube ainda processa: " + ", ".join(v["rotulo"] for v in andamento) + ". Nada se perdeu. "
              "Rode `videos --executar` de novo daqui a alguns minutos, e ele só lê a resposta")
        for v in andamento:
            if v.get("nota"):
                print(f"     - {v['rotulo']}: {v['nota']}")
    if ruins:
        print("\n  !!! Fora do esperado:")
        for r in ruins:
            print(f"     - {r}")
    if falhou:
        print(f"\n  !!! A SUBIDA PAROU em {falhou}\n     O que subiu antes está no registro. Rodar de novo continua daqui.")
    if ruins or falhou:
        sys.exit(1)
    if andamento:
        sys.exit(3)                             # igual ao ESPERA do conferir_campanha.py: falta resposta, não é erro


def cmd_anexar(args):
    """Põe em cada anúncio os vídeos que o criativo dele tem hoje (vertical + 16:9). O anúncio continua o mesmo
    (o Dash não perde o id) e volta pra revisão do Google. Por isso anúncio NO AR fica de fora: mudar o que
    está rodando é com o dono da conta (`sirius-scale/REGRAS.md` §6)."""
    reg, G, cid = carregar(args.registro, ("customer_id", "campanhas"))
    cli = comum.cliente()
    g = cli.get_service("GoogleAdsService")
    trocas, no_ar = [], []
    for C in G["campanhas"]:
        camp_id = C.get("id") or gr.campanha_por_nome(g, cid, C["nome"], "DEMAND_GEN")
        if not camp_id:
            continue
        por_nome = {nome_anuncio(i, reg["criativos"][i]): i for i in C["anuncios"]}
        for r in g.search(customer_id=cid, query=f"""SELECT campaign.status, ad_group.status, ad_group_ad.ad.id,
                ad_group_ad.ad.name, ad_group_ad.status, ad_group_ad.ad.demand_gen_video_responsive_ad.videos
                FROM ad_group_ad WHERE campaign.id = {camp_id} AND ad_group_ad.status != 'REMOVED'"""):
            i = por_nome.get(r.ad_group_ad.ad.name)
            if not i:
                continue
            quer = videos_do(reg["criativos"][i])
            if len(r.ad_group_ad.ad.demand_gen_video_responsive_ad.videos) >= len(quer):
                continue
            ligado = all(x.name == "ENABLED" for x in (r.campaign.status, r.ad_group.status, r.ad_group_ad.status))
            (no_ar if ligado else trocas).append((camp_id, r.ad_group_ad.ad.id, r.ad_group_ad.ad.name,
                                                  r.ad_group_ad.status.name, i, quer))
    for camp_id, aid, nome, st, i, quer in trocas:
        print(f"  campanha {camp_id} · {nome} [{st}] -> vídeos {quer}")
    for camp_id, aid, nome, st, i, quer in no_ar:
        print(f"  ⚠ campanha {camp_id} · {nome}: anúncio NO AR, fica de fora. Trocar vídeo manda de volta pra revisão, "
              "e quem decide isso é o dono da conta")
    if not trocas:
        return print("  nada a anexar" + (" fora do que está no ar" if no_ar else ": todo anúncio já tem os vídeos do criativo"))
    ops, rot = ops_anexar(cli, g, cid, reg, trocas)
    gr.mutate(cli, cid, ops, validar=True, rotulos=rot)
    print(f"  ok  validação a seco aceita ({len(ops)} operações)")
    if not confirmar(f"Isto troca a lista de vídeos de {len(trocas)} anúncio(s), que voltam pra revisão do Google.",
                     args.executar, args.confirmado_no_chat):
        return
    gr.mutate(cli, cid, ops, validar=False, rotulos=rot)
    for camp_id, aid, nome, st, i, quer in trocas:
        lidos = le_anuncios(g, cid, camp_id).get(nome, {})
        print(f"  {'ok ' if lidos.get('videos') == len(quer) else '!!!'} {nome}: {lidos.get('videos')} vídeo(s) lidos "
              f"de volta · {lidos.get('status')} · {lidos.get('aprov')}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for nome, fn in (("listas", cmd_listas), ("marca", cmd_marca), ("videos", cmd_videos), ("criar", cmd_criar),
                     ("anexar", cmd_anexar)):
        p = sub.add_parser(nome)
        p.add_argument("--registro", required=True)
        if nome == "criar":
            p.add_argument("--campanha", help="só as campanhas cujo nome tem este trecho")
        if nome == "videos":
            p.add_argument("--espera", type=int, default=ESPERA_VIDEOS_MIN, help="minutos lendo o processamento")
        p.add_argument("--executar", action="store_true")
        p.add_argument("--confirmado-no-chat", action="store_true", dest="confirmado_no_chat")
        p.set_defaults(fn=fn)
    args = ap.parse_args(argv)
    args.registro = comum.caminho(args.registro)
    if args.executar and args.cmd != "videos":   # subir vídeo não gasta verba
        comum.teto_campanha()                # para aqui, antes de qualquer chamada à API
    args.fn(args)


if __name__ == "__main__":
    main()
