# /// script
# requires-python = ">=3.10"
# dependencies = ["google-ads>=31"]
# [tool.uv]
# exclude-newer = "2026-11-05T00:00:00Z"
# ///
"""
Confere a campanha contra a receita de `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`
§0 e o checklist do §32. Roda DEPOIS de criar e ANTES de ligar. Leitura pura.

Por que existe: receita que depende de alguém lembrar falha. Uma cadeia que para no meio e é
completada à mão pula passo calado, e campanha Demand Gen sem geo gasta quase tudo fora do país
sem nenhum aviso (§7). Aqui cada item é lido da plataforma, não da intenção de quem subiu.

DOIS MODOS (um dos dois é obrigatório):
  --referencia <id>   compara item a item com uma campanha que funciona, da mesma fase (§10, §15).
  --sem-referencia    só as conferências absolutas, pra conta sem campanha irmã.

SEMPRE CONFERE (cada item cita o passo da receita §0):
  [8]   status: campanha, grupos e anúncios pausados. Coisa ligada é AVISO: confirmar com o dono
  [1]   orçamento entre o piso (R$ 25,40, §1) e TETO_CAMPANHA_DIA
  [6/7] LOCATION em todo grupo ativo (ou na campanha, no Display)
  [4]   público quente ([PQ] no nome) com segmentação otimizada DESLIGADA (§31)
  [6]   anúncio: pelo menos 1, vídeo no anúncio de vídeo, política e UTM (no sufixo ou no URL)
  [8]   com --frequencia e --fim-ate: limite de frequência e data de fim lidos da campanha
  [3]   sem referência, pelo menos 1 meta biddable em campanha que otimiza conversão (§2)

SÓ COM --referencia, contra ela:
  [2]   canal, lance e teto de CPA, network_settings
  [3]   metas de conversão: exatamente as mesmas categorias biddable
  [4]   segmentação otimizada igual (menos em [PQ], que tem regra própria)
  [5]   público anexado, listas de exclusão e faixa etária
  [6/7] os mesmos países, e AVISO se a referência usa 2 formatos de vídeo e a nova usa 1
  [8]   horário: pelo menos 1 faixa de ad_schedule, se a referência tem

SAÍDA: um veredito por item e o resumo no fim.
  PASS    conferido e certo
  AVISO   não bloqueia, mas alguém precisa olhar
  ESPERA  o Google ainda está revisando o anúncio. Não é defeito, mas não dá pra ligar ainda (§15, §20)
  FAIL    não ligue
Código de saída: 0 sem nada pendente, 1 com FAIL, 3 sem FAIL mas com ESPERA.

Uso (ligar é do dono da conta, na tela do Google Ads, `sirius-scale/REGRAS.md` §6):
  uv run sirius-scale/ferramentas/google/conferir_campanha.py --conta <conta> --id <id> --sem-referencia
  uv run sirius-scale/ferramentas/google/conferir_campanha.py --conta <conta> --filtro <trecho do nome> --referencia <id>
  uv run sirius-scale/ferramentas/google/conferir_campanha.py --conta <conta> --id <id> --conta-referencia <outra> --referencia <id>
"""

import argparse
import sys
import urllib.parse

import comum
from registro import PISO_DIARIO


def utm_bate(utm, nome):
    """utm_campaign confere com o nome da campanha? Compara ignorando espaço, e só espaço. A variável
    do próprio Google (`{campaignid}`, §31) o Google troca pelo id DESTA campanha: ela também bate."""
    if (utm or "").strip() == "{campaignid}":
        return True
    return "".join((utm or "").split()) == "".join((nome or "").split()) and bool(utm)


def utm_dispensada(url, nome):
    """Distribuição de conteúdo ([DC]) manda pro canal do YouTube, sem página e sem Dash: a UTM não se
    aplica (§25). Só [DC] e só destino youtube.com: lançamento apontando pro YouTube continua falhando."""
    n = (nome or "").upper()
    host = urllib.parse.urlparse(url or "").netloc.lower()
    return "[DC]" in n and (host == "youtube.com" or host.endswith(".youtube.com"))


def lance_confere(nova, ref, esperado=None, tcpa_esperado=0.0):
    """Sem `esperado`: igual ao da referência (a regra). Com `esperado`: o lance que o registro declara,
    quando ele é diferente da referência por desenho. Devolve (ok, texto)."""
    if esperado:
        ok = nova["lance"] == esperado and abs(nova["tcpa"] - tcpa_esperado) < 0.01
        return ok, f"lance {nova['lance']} tCPA={nova['tcpa']} (o registro pede {esperado} tCPA={tcpa_esperado}; ref {ref['lance']} tCPA={ref['tcpa']})"
    ok = nova["lance"] == ref["lance"] and abs(nova["tcpa"] - ref["tcpa"]) < 0.01
    return ok, f"lance {nova['lance']} tCPA={nova['tcpa']} (ref {ref['lance']} tCPA={ref['tcpa']})"


def ot_confere(nome, ot, ot_ref):
    """Otimizada igual à da referência. [PQ] fica de fora: a regra dela é desligada, seja qual for a
    referência. Sem isso, toda [PQ] nova contra uma referência antiga dava FAIL por estar certa (§31)."""
    if "[PQ]" in (nome or "").upper():
        return True
    return (ot in ot_ref) if ot_ref else True


def checa_frequencia(caps, esperado):
    """caps = [(evento, unidade, duracao, cap)] lidos da campanha. `esperado` = N impressões/dia ou None."""
    if esperado is None:
        return True, f"limite de frequência {caps or 'nenhum'} (não exigido)"
    alvo = ("IMPRESSION", "DAY", 1, int(esperado))
    return alvo in caps, f"limite de frequência {caps or 'NENHUM'} (exigido {esperado} impressões/dia)"


def checa_horario(n_nova, fim_nova, n_ref, fim_ate):
    """Pelo menos 1 faixa de ad_schedule se a referência tem, e fim até `fim_ate` quando exigido."""
    ok = (n_nova >= 1 or n_ref == 0)
    if fim_ate:
        ok = ok and bool(fim_nova) and fim_nova[:19] <= fim_ate[:19]
    return ok, (f"horário: {n_nova} faixa(s) de ad_schedule, fim {fim_nova or 'SEM FIM'} "
                f"(ref {n_ref} faixa(s); fim exigido até {fim_ate or '-'})")


def checa_ot_quente(nome, ot):
    """Campanha [PQ] fala com quem já é da casa: otimizada DESLIGADA, seja qual for a referência. No Google
    ela nasce ligada se omitida (`sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.6)."""
    pq = "[PQ]" in (nome or "").upper()
    return not (pq and ot), f"otimizada={ot} ({'[PQ]: tem que ser False' if pq else 'não é [PQ]'})"


CANAIS_DG = ("gmail", "discover", "display", "youtube_in_feed", "youtube_in_stream", "youtube_shorts")


def canais_de(cc):
    """Canais de um grupo Demand Gen (channel_controls) como tupla comparável: (config, estratégia, canais escolhidos)."""
    cfg = cc.channel_config.name if cc.channel_config else "UNSPECIFIED"
    if cfg == "SELECTED_CHANNELS":
        return (cfg, None, tuple(k for k in CANAIS_DG if getattr(cc.selected_channels, k)))
    return (cfg, cc.channel_strategy.name if cc.channel_strategy else None, ())


def tem_shorts(canais):
    """ALL_CHANNELS e ALL_OWNED_AND_OPERATED_CHANNELS incluem o YouTube inteiro, Shorts também."""
    cfg, est, sel = canais
    if cfg == "SELECTED_CHANNELS":
        return "youtube_shorts" in sel
    return est in ("ALL_CHANNELS", "ALL_OWNED_AND_OPERATED_CHANNELS")


def checa_canais(nova, ref):
    """Grupo criado sem copiar os canais da referência nasce com os padrão da conta. Canais diferentes da referência
    é FAIL; referência com Shorts e a nova sem também (`google-criacao-tecnica.md` §35)."""
    ok = nova == ref and (tem_shorts(nova) or not tem_shorts(ref))
    desc = lambda c: f"{c[0]} {c[1] or ', '.join(c[2]) or '-'}"
    return ok, f"canais {desc(nova)} (ref {desc(ref)})" + ("" if tem_shorts(nova) else " · SEM Shorts")


def veredito_exclusao(nova, ref):
    """(ok, aviso). Igual = PASS. Nova SEM exclusão e referência COM = FAIL. Nova com exclusão diferente,
    inclusive a mais, = AVISO: id de lista muda por lançamento, e excluir a mais não é erro."""
    if nova == ref:
        return True, False
    return False, bool(nova)


def veredito_politica(aprov, revisao):
    """PASS, AVISO, ESPERA ou FAIL pro estado de política do anúncio (§20). Anúncio recém-criado fica
    UNKNOWN / REVIEW_IN_PROGRESS mesmo pausado: não é defeito, é espera, e reconfere antes de ligar (§15)."""
    if aprov == "APPROVED":
        return "PASS"
    if aprov == "APPROVED_LIMITED":
        return "AVISO"
    if aprov == "DISAPPROVED":
        return "FAIL"
    if revisao == "REVIEW_IN_PROGRESS" or aprov in ("UNKNOWN", "UNSPECIFIED"):
        return "ESPERA"
    return "FAIL"


def ler(ga, cid, conta):
    """Lê a config completa de uma campanha: campanha, metas, grupos, critérios, anúncios."""
    q = lambda s: list(ga.search(customer_id=conta, query=s))
    d = {"id": cid}
    for r in q(f"""SELECT campaign.name, campaign.status, campaign.advertising_channel_type,
        campaign.bidding_strategy_type, campaign.target_cpa.target_cpa_micros,
        campaign.maximize_conversions.target_cpa_micros, campaign_budget.amount_micros,
        campaign.network_settings.target_youtube, campaign.network_settings.target_content_network,
        campaign.network_settings.target_google_tv_network, campaign.end_date_time,
        campaign.frequency_caps
        FROM campaign WHERE campaign.id = {cid}"""):
        c = r.campaign
        d.update(nome=c.name, status=c.status.name, canal=c.advertising_channel_type.name,
                 lance=c.bidding_strategy_type.name,
                 tcpa=(c.target_cpa.target_cpa_micros or c.maximize_conversions.target_cpa_micros) / 1e6,
                 orcamento=r.campaign_budget.amount_micros / 1e6,
                 rede=(c.network_settings.target_youtube, c.network_settings.target_content_network,
                       c.network_settings.target_google_tv_network),
                 fim=c.end_date_time,
                 frequencia=[(f.key.event_type.name, f.key.time_unit.name, f.key.time_length, f.cap)
                             for f in c.frequency_caps])
    if "nome" not in d:
        sys.exit(f"Campanha {cid} não encontrada na conta {conta}.")
    d["n_horarios"] = len(q(f"""SELECT campaign_criterion.ad_schedule.day_of_week FROM campaign_criterion
        WHERE campaign.id = {cid} AND campaign_criterion.type = 'AD_SCHEDULE'"""))
    d["metas"] = sorted(r.campaign_conversion_goal.category.name for r in q(
        f"SELECT campaign_conversion_goal.category, campaign_conversion_goal.biddable "
        f"FROM campaign_conversion_goal WHERE campaign.id = {cid}") if r.campaign_conversion_goal.biddable)
    d["grupos"] = {}
    cc = "ad_group.demand_gen_ad_group_settings.channel_controls"
    for r in q(f"""SELECT ad_group.id, ad_group.name, ad_group.status, ad_group.optimized_targeting_enabled,
        {cc}.channel_config, {cc}.channel_strategy, {', '.join(f'{cc}.selected_channels.{k}' for k in CANAIS_DG)}
        FROM ad_group WHERE campaign.id = {cid} AND ad_group.status != 'REMOVED'"""):
        d["grupos"][str(r.ad_group.id)] = {"nome": r.ad_group.name, "status": r.ad_group.status.name,
                                           "ot": r.ad_group.optimized_targeting_enabled,
                                           "canais": canais_de(r.ad_group.demand_gen_ad_group_settings.channel_controls),
                                           "geo": set(), "publico": 0, "ads": [],
                                           "neg_listas": set(), "idade_pos": set(), "idade_neg": set()}
    for r in q(f"""SELECT ad_group.id, ad_group_criterion.type, ad_group_criterion.negative,
        ad_group_criterion.location.geo_target_constant, ad_group_criterion.age_range.type,
        ad_group_criterion.audience.audience, ad_group_criterion.user_list.user_list
        FROM ad_group_criterion WHERE campaign.id = {cid}
        AND ad_group_criterion.type IN ('LOCATION','AUDIENCE','USER_LIST','AGE_RANGE')"""):
        g = d["grupos"].get(str(r.ad_group.id))
        if not g:
            continue
        c = r.ad_group_criterion
        # Negativo entra na conferência: copiar listas sem olhar o flag `negative` transforma
        # exclusão em inclusão, e a conferência que não olha negativo dá PASS nisso.
        if c.type_.name == "AGE_RANGE":
            (g["idade_neg"] if c.negative else g["idade_pos"]).add(c.age_range.type_.name)
            continue
        if c.type_.name == "USER_LIST" and c.negative:
            if c.user_list.user_list:
                g["neg_listas"].add(c.user_list.user_list.split("/")[-1])
            continue
        if c.negative:
            continue
        if c.type_.name == "LOCATION":
            g["geo"].add(c.location.geo_target_constant.split("/")[-1])
        else:
            g["publico"] += 1
            if c.type_.name == "AUDIENCE":
                g.setdefault("audiences", []).append(c.audience.audience.split("/")[-1])
    # Grupo com audience agrupada (§25): exclusão de lista não é critério do grupo, mora em
    # Audience.exclusion_dimension.
    aud_ids = sorted({x for g in d["grupos"].values() for x in g.get("audiences", []) if x})
    if aud_ids:
        for r in q(f"""SELECT audience.id, audience.exclusion_dimension FROM audience
            WHERE audience.id IN ({','.join(aud_ids)})"""):
            excl = {e.user_list.user_list.split("/")[-1] for e in r.audience.exclusion_dimension.exclusions}
            for g in d["grupos"].values():
                if str(r.audience.id) in g.get("audiences", []):
                    g["neg_listas"] |= excl
    # Geo na CAMPANHA: Display guarda a LOCATION lá; Demand Gen só no grupo (§7.1).
    d["geo_campanha"] = set()
    for r in q(f"""SELECT campaign_criterion.location.geo_target_constant, campaign_criterion.negative
        FROM campaign_criterion WHERE campaign.id = {cid} AND campaign_criterion.type = 'LOCATION'"""):
        if not r.campaign_criterion.negative:
            d["geo_campanha"].add(r.campaign_criterion.location.geo_target_constant.split("/")[-1])
    for r in q(f"""SELECT ad_group.id, ad_group_ad.ad.id, ad_group_ad.ad.name, ad_group_ad.status,
        ad_group_ad.ad.type, ad_group_ad.ad.final_urls, ad_group_ad.policy_summary.approval_status,
        ad_group_ad.policy_summary.review_status,
        ad_group_ad.ad.demand_gen_video_responsive_ad.videos, ad_group_ad.ad.final_url_suffix
        FROM ad_group_ad WHERE campaign.id = {cid} AND ad_group_ad.status != 'REMOVED'"""):
        g = d["grupos"].get(str(r.ad_group.id))
        if not g:
            continue
        ad = r.ad_group_ad.ad
        url = list(ad.final_urls)[0] if ad.final_urls else ""
        utm = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get("utm_campaign", [""])[0]
        if not utm and ad.final_url_suffix:   # a UTM do Google mora no sufixo (§31)
            utm = urllib.parse.parse_qs(ad.final_url_suffix).get("utm_campaign", [""])[0]
        g["ads"].append({"nome": ad.name, "status": r.ad_group_ad.status.name,
                         "tipo": ad.type_.name,
                         "aprov": r.ad_group_ad.policy_summary.approval_status.name,
                         "revisao": r.ad_group_ad.policy_summary.review_status.name,
                         "videos": len(ad.demand_gen_video_responsive_ad.videos),
                         "utm_campaign": utm, "url": url})
    return d


def conferir(nova, ref, teto, frequencia=None, fim_ate=None, lance_esperado=None, tcpa_esperado=0.0):
    """Devolve [(passo, veredito, texto)]. `ref` None = só as conferências absolutas."""
    itens = []

    def item(passo, ok, texto, aviso=False):
        itens.append((passo, "PASS" if ok else ("AVISO" if aviso else "FAIL"), texto))

    status = {g["status"] for g in nova["grupos"].values()} | {ad["status"] for g in nova["grupos"].values() for ad in g["ads"]}
    status.add(nova["status"])
    texto = (f"status: campanha {nova['status']}, grupos {sorted({g['status'] for g in nova['grupos'].values()})}, "
             f"anúncios {sorted({ad['status'] for g in nova['grupos'].values() for ad in g['ads']})}")
    if nova["status"] == "REMOVED":
        item("8", False, texto)
    else:
        item("8", status == {"PAUSED"}, texto + ("" if status == {"PAUSED"} else ": tem coisa ligada, confirme que foi o dono da conta"), aviso=True)
    if ref:
        item("2", nova["canal"] == ref["canal"], f"canal {nova['canal']} (ref {ref['canal']})")
        item("2", *lance_confere(nova, ref, lance_esperado, tcpa_esperado))
        item("2", nova["rede"] == ref["rede"], f"network_settings yt/content/gtv {nova['rede']} (ref {ref['rede']})")
        item("3", nova["metas"] == ref["metas"], f"metas biddable {nova['metas']} (ref {ref['metas']})")
    else:
        item("3", bool(nova["metas"]) or nova["lance"] != "MAXIMIZE_CONVERSIONS",
             f"metas biddable {nova['metas'] or 'NENHUMA'} · lance {nova['lance']} (confira contra o registro)")
    if teto is None:
        item("1", False, f"orçamento {comum.brl(nova['orcamento'])}/dia: sem TETO_CAMPANHA_DIA no .env não dá pra conferir")
    else:
        item("1", PISO_DIARIO <= nova["orcamento"] <= teto,
             f"orçamento {comum.brl(nova['orcamento'])}/dia (piso {comum.brl(PISO_DIARIO)}, teto {comum.brl(teto)})")
    if ref or fim_ate:
        item("8", *checa_horario(nova["n_horarios"], nova.get("fim"), ref["n_horarios"] if ref else 0, fim_ate))
    if ref or frequencia is not None:
        item("8", *checa_frequencia(nova.get("frequencia", []), frequencia))

    grupos_ref = ref["grupos"] if ref else {}
    geo_ref = set().union(*(g["geo"] for g in grupos_ref.values())) if grupos_ref else set()
    geo_ref_efetiva = geo_ref or (ref.get("geo_campanha", set()) if ref else set())
    ot_ref = {g["ot"] for g in grupos_ref.values() if g["status"] == "ENABLED"}
    ref_tem_publico = any(g["publico"] for g in grupos_ref.values())
    ref_videos = max((ad["videos"] for g in grupos_ref.values() for ad in g["ads"]), default=0)

    ativos = {k: g for k, g in nova["grupos"].items() if g["status"] == "ENABLED"} or nova["grupos"]
    if not ativos:
        item("4", False, "campanha sem nenhum grupo")
    for g in ativos.values():
        pref = f"grupo '{g['nome'][:28]}'"
        geo_efetiva = g["geo"] or nova.get("geo_campanha", set())
        onde = "grupo" if g["geo"] else ("campanha" if nova.get("geo_campanha") else "NENHUMA")
        item("6/7", bool(geo_efetiva) and (not geo_ref_efetiva or geo_efetiva == geo_ref_efetiva),
             f"{pref}: LOCATION {sorted(geo_efetiva) or 'NENHUMA'} ({onde})" + (f" (ref {sorted(geo_ref_efetiva)})" if ref else ""))
        if ref:
            item("4", ot_confere(nova["nome"], g["ot"], ot_ref),
                 f"{pref}: otimizada={g['ot']} (ref {ot_ref})")
        ok_pq, txt_pq = checa_ot_quente(nova["nome"], g["ot"])
        item("4", ok_pq, f"{pref}: {txt_pq}")
        if ref:
            item("5", (g["publico"] > 0) if ref_tem_publico else True,
                 f"{pref}: {g['publico']} critério(s) de público (ref usa público: {ref_tem_publico})")
            # grupo equivalente da referência: o de mesmo nome, senão o primeiro ativo
            rg = next((x for x in grupos_ref.values() if x["nome"] == g["nome"]), None) or \
                next((x for x in grupos_ref.values() if x["status"] == "ENABLED"), None)
            if (rg and nova["canal"] == "DEMAND_GEN" and ref["canal"] == "DEMAND_GEN"
                    and g.get("canais") and rg.get("canais")):
                item("4", *checa_canais(g["canais"], rg["canais"]))
            if rg:
                ok_ex, aviso_ex = veredito_exclusao(g["neg_listas"], rg["neg_listas"])
                item("5", ok_ex,
                     f"{pref}: listas de EXCLUSÃO {sorted(g['neg_listas']) or 'nenhuma'} (ref '{rg['nome'][:20]}': {sorted(rg['neg_listas']) or 'nenhuma'})",
                     aviso=aviso_ex)
                item("5", (g["idade_pos"] == rg["idade_pos"]) and (g["idade_neg"] == rg["idade_neg"]),
                     f"{pref}: idade positiva {sorted(g['idade_pos'])} / negativa {len(g['idade_neg'])} (ref: {sorted(rg['idade_pos'])} / {len(rg['idade_neg'])})")
        item("6", bool(g["ads"]), f"{pref}: {len(g['ads'])} anúncio(s)")
        for ad in g["ads"]:
            eh_video = "VIDEO" in ad.get("tipo", "")
            if eh_video:
                item("6", ad["videos"] >= 1, f"    {ad['nome'][:34]}: {ad['videos']} vídeo(s)")
            else:
                item("6", True, f"    {ad['nome'][:34]}: {ad.get('tipo', '?').lower()} (estático, sem vídeo por desenho)")
            if eh_video and ref_videos >= 2 and ad["videos"] < 2:
                item("6", False, f"    {ad['nome'][:34]}: referência usa {ref_videos} formatos "
                                 f"(horizontal+vertical), este tem {ad['videos']}", aviso=True)
            itens.append(("6", veredito_politica(ad["aprov"], ad.get("revisao")),
                          f"    {ad['nome'][:34]}: política {ad['aprov']} · revisão {ad.get('revisao')}"))
            if utm_dispensada(ad.get("url"), nova["nome"]):
                item("6", True, f"    {ad['nome'][:34]}: destino é o canal do YouTube (distribuição), UTM não se aplica")
                continue
            bate = utm_bate(ad["utm_campaign"], nova["nome"])
            item("6", bate, f"    {ad['nome'][:34]}: utm_campaign {'bate' if bate else 'DIFERENTE do nome'}")
    return itens


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--conta", required=True, help="conta da campanha a conferir")
    p.add_argument("--id", help="id da campanha a conferir")
    p.add_argument("--filtro", help="ou: trecho do nome da campanha a conferir")
    modo = p.add_mutually_exclusive_group(required=True)
    modo.add_argument("--referencia", help="id da campanha de referência, a que funciona")
    modo.add_argument("--sem-referencia", action="store_true", help="só as conferências absolutas")
    p.add_argument("--conta-referencia", default=None, help="conta da referência (padrão: a mesma de --conta)")
    p.add_argument("--frequencia", type=int, default=None, help="exige limite de N impressões/dia")
    p.add_argument("--fim-ate", default=None, help='exige fim até este momento, ex.: "2031-03-15 23:59:59"')
    p.add_argument("--lance-esperado", default=None,
                   help="o lance que o registro declara quando difere da referência por desenho (ex.: MAXIMIZE_CONVERSIONS)")
    p.add_argument("--tcpa-esperado", type=float, default=0.0, help="o tCPA que o registro declara junto (padrão 0 = sem tCPA)")
    a = p.parse_args(argv)
    if not a.id and not a.filtro:
        sys.exit("Passe --id ou --filtro.")
    conta = comum.so_digitos(a.conta)
    teto = comum.teto_campanha(obrigatorio=False)
    ga = comum.cliente().get_service("GoogleAdsService")

    cid = a.id
    if not cid:
        # Filtro em Python: colchete quebra o LIKE do GAQL, e nome da casa tem colchete (§3.2).
        achadas = [(r.campaign.id, r.campaign.name) for r in ga.search(customer_id=conta, query="""
            SELECT campaign.id, campaign.name FROM campaign WHERE campaign.status != 'REMOVED'""")
                   if a.filtro in r.campaign.name]
        if len(achadas) != 1:
            sys.exit(f"--filtro '{a.filtro}' casou com {len(achadas)} campanha(s): {achadas}")
        cid = achadas[0][0]

    nova = ler(ga, cid, conta)
    ref = ler(ga, a.referencia, comum.so_digitos(a.conta_referencia) or conta) if a.referencia else None
    print("=" * 78)
    print(f"CONFERIR  {nova['nome']}")
    print(f"   contra  {ref['nome'] if ref else 'nada: só as conferências absolutas (--sem-referencia)'}")
    print("=" * 78)
    itens = conferir(nova, ref, teto, a.frequencia, a.fim_ate, a.lance_esperado, a.tcpa_esperado)
    for passo, veredito, texto in itens:
        print(f"  [{passo:>3}] {veredito:6s} {texto}")
    n = {v: sum(1 for _, x, _ in itens if x == v) for v in ("FAIL", "AVISO", "ESPERA")}
    print("-" * 78)
    print(f"  {len(itens)} itens lidos · {n['FAIL']} FAIL · {n['ESPERA']} ESPERA · {n['AVISO']} AVISO")
    if n["FAIL"]:
        print("  NÃO LIGUE. Corrija os FAIL e rode de novo.")
        sys.exit(1)
    if n["ESPERA"]:
        print("  Sem defeito, mas o Google ainda revisa anúncio. Não ligue ainda: rode de novo quando a revisão acabar.")
        sys.exit(3)
    print("  Receita conferida. Quem liga é o dono da conta, na tela do Google Ads.")


if __name__ == "__main__":
    main()
