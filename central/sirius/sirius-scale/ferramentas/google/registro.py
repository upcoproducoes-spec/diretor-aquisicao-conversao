"""
Biblioteca do `subir_campanha.py`: o que fala com a API do Google Ads. Não é script.

O DESENHO:
  1. A cadeia inteira (imagens, orçamento, campanha, grupo, público, geo, anúncios) vai num
     único `GoogleAdsService.Mutate` com IDs TEMPORÁRIOS (-1, -2...). Com `validate_only=True`
     o Google valida TUDO sem criar nada, e a prévia roda isso de verdade, contra a API.
  2. A lista de regra nova é criada ANTES e SOZINHA, e lida de volta: lookback de CADA operando
     (a duração real; o `membership_life_span` é ignorado em lista por regra), operador OU,
     regra e pré-população. O validate_only aceita calado operandos em E e lookback 0: só a
     leitura pega. Se não bater, para antes de qualquer campanha.
  3. Depois vem a cadeia, validada de novo e escrita no MESMO pedido com `validate_only=False`:
     atômica, tudo ou nada. Nunca sobra campanha pela metade.
  4. Tudo nasce PAUSED: campanha, grupo e anúncio. Ligar não existe aqui.
  5. Escrita só conta com leitura de volta: status dos três níveis, geo, segmentação otimizada,
     públicos e exclusões são LIDOS DA PLATAFORMA depois de criar.

Toda escrita de campanha passa por `mutate()`. É lá que mora a trava do teto: sem TETO_CAMPANHA_DIA no
.env, nenhuma campanha é escrita. Subir vídeo não gasta verba e fica no `subir_campanha.py`. A receita e as armadilhas estão em
`sirius-scale/frameworks/trafego/google-criacao-tecnica.md` (citado abaixo só como §N).
"""

import hashlib
import json
import os
import struct
import sys

import comum

PISO_DIARIO = 25.40          # §1: valor da época, em BRL. O Google diz o atual no erro da validação


def carrega(arq):
    with open(arq, encoding="utf-8") as f:
        return json.load(f)


class Temp:
    """Gerador de IDs temporários (-1, -2...) pro Mutate em lote."""
    def __init__(self):
        self.n = 0

    def __call__(self, cid, recurso):
        self.n -= 1
        return f"customers/{cid}/{recurso}/{self.n}"


def dim_png(arq):
    with open(arq, "rb") as f:
        cab = f.read(24)
    if cab[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", cab[16:24])


# ── listas ───────────────────────────────────────────────────────────────

def listas_existentes(g, cid):
    out = {}
    for r in g.search(customer_id=cid, query="""
            SELECT user_list.id, user_list.name, user_list.type,
                   user_list.size_for_display, user_list.membership_life_span
            FROM user_list WHERE user_list.membership_status = 'OPEN'"""):
        u = r.user_list
        out[str(u.id)] = {"nome": u.name, "tipo": u.type_.name,
                          "disp": u.size_for_display, "vida": u.membership_life_span}
    return out


def op_lista_regra(cli, cid, spec, rn=None):
    """Lista por regra de URL, "visitou QUALQUER um destes trechos": UM OPERANDO POR TRECHO, ligados
    por OU (§30). Um operando só com um grupo por trecho volta 'inclusive_operands: Too many', e itens
    no MESMO grupo são E: a lista fica vazia. Pré-população opcional (§27)."""
    op = cli.get_type("MutateOperation")
    ul = op.user_list_operation.create
    if rn:
        ul.resource_name = rn
    ul.name = spec["nome"]
    ul.description = (spec.get("descricao") or "")[:250]
    dias = int(spec["membership_life_span"])
    # Em lista por REGRA o `membership_life_span` é IGNORADO: a duração real é o
    # `lookback_window_days` de CADA operando, e sem ele a lista lê 540 dias, com
    # nome de 30. O span fica igual só por coerência; quem manda é o lookback.
    ul.membership_life_span = dias
    f = ul.rule_based_user_list.flexible_rule_user_list
    f.inclusive_rule_operator = cli.enums.UserListFlexibleRuleOperatorEnum.OR
    for parte in spec["contem"]:
        item = cli.get_type("UserListRuleItemInfo")
        item.name = "url__"
        item.string_rule_item.operator = cli.enums.UserListStringRuleItemOperatorEnum.CONTAINS
        item.string_rule_item.value = parte
        grupo = cli.get_type("UserListRuleItemGroupInfo")
        grupo.rule_items.append(item)
        regra = cli.get_type("UserListRuleInfo")
        regra.rule_item_groups.append(grupo)
        operando = cli.get_type("FlexibleRuleOperandInfo")
        operando.rule = regra
        operando.lookback_window_days = dias
        f.inclusive_operands.append(operando)
    if spec.get("prepopulation"):
        ul.rule_based_user_list.prepopulation_status = \
            cli.enums.UserListPrepopulationStatusEnum.REQUESTED
    return op


def le_lista(g, cid, list_id):
    for r in g.search(customer_id=cid, query=f"""
            SELECT user_list.id, user_list.name, user_list.membership_life_span,
                   user_list.rule_based_user_list.prepopulation_status,
                   user_list.rule_based_user_list.flexible_rule_user_list.inclusive_rule_operator,
                   user_list.rule_based_user_list.flexible_rule_user_list.inclusive_operands
            FROM user_list WHERE user_list.id = {list_id}"""):
        u = r.user_list
        f = u.rule_based_user_list.flexible_rule_user_list
        grupos = []
        for op in f.inclusive_operands:
            for grp in op.rule.rule_item_groups:
                grupos.append([it.string_rule_item.value for it in grp.rule_items])
        return {"id": str(u.id), "nome": u.name, "vida": u.membership_life_span,
                "lookbacks": [o.lookback_window_days for o in f.inclusive_operands],
                "prepop": u.rule_based_user_list.prepopulation_status.name, "grupos": grupos,
                "operador": f.inclusive_rule_operator.name, "n_operandos": len(f.inclusive_operands)}
    return None


def problemas_lista(lida, spec):
    """A lista lida da plataforma bate com a receita? Lista vazia = ok. A retenção conferida é o
    `lookback_window_days` de CADA operando, nunca o `membership_life_span`."""
    p = []
    if lida is None:
        return ["lista não encontrada na leitura de volta"]
    pedido = int(spec["membership_life_span"])
    if not lida["lookbacks"] or any(x != pedido for x in lida["lookbacks"]):
        p.append(f"retenção (lookback por operando) lida {lida['lookbacks']}, pedida {pedido} em cada")
    if sorted(lida["grupos"]) != sorted([[x] for x in spec["contem"]]):
        p.append(f"regra lida {lida['grupos']} != {[[x] for x in spec['contem']]} (um trecho por operando)")
    if lida["n_operandos"] > 1 and lida["operador"] != "OR":
        p.append(f"operandos ligados por {lida['operador']} (tem que ser OR: visitou QUALQUER um)")
    if spec.get("prepopulation") and lida["prepop"] not in ("REQUESTED", "FINISHED"):
        p.append(f"pré-população {lida['prepop']}")
    return p


def cria_lista_e_confere(cli, g, cid, spec):
    """Escrita REAL da lista nova, sozinha: valida, cria, lê de volta. Para se não bater."""
    mutate(cli, cid, [op_lista_regra(cli, cid, spec)], validar=True, rotulos=[f"lista {spec['nome']}"])
    r = mutate(cli, cid, [op_lista_regra(cli, cid, spec)], validar=False, rotulos=[f"lista {spec['nome']}"])
    rn = r.mutate_operation_responses[0].user_list_result.resource_name
    lida = le_lista(g, cid, rn.split("/")[-1])
    prob = problemas_lista(lida, spec)
    print(f"  lista criada: {rn} · lida: lookback por operando {lida and lida['lookbacks']} · "
          f"operador {lida and lida['operador']} · pré-população {lida and lida['prepop']} · "
          f"grupos {lida and lida['grupos']}")
    if prob:
        print("  !!! A LISTA NASCEU DIFERENTE DO PEDIDO. Parei antes de criar campanha:")
        for x in prob:
            print(f"     - {x}")
        sys.exit(1)
    return rn


# ── imagens ──────────────────────────────────────────────────────────────

def nome_asset(arq):
    """O nome leva o hash do conteúdo: mesma imagem na conta é reaproveitada, imagem nova não colide."""
    with open(arq, "rb") as f:
        h = hashlib.sha256(f.read()).hexdigest()[:10]
    return f"{os.path.basename(arq)[:100]} {h}"


def assets_existentes(g, cid, nomes):
    out = {}
    if not nomes:
        return out
    lista = ",".join("'" + n.replace("'", "\\'") + "'" for n in nomes)
    for r in g.search(customer_id=cid, query=f"""
            SELECT asset.resource_name, asset.name FROM asset
            WHERE asset.type = 'IMAGE' AND asset.name IN ({lista})"""):
        out[r.asset.name] = r.asset.resource_name
    return out


def op_imagem(cli, rn, arq):
    op = cli.get_type("MutateOperation")
    a = op.asset_operation.create
    a.resource_name = rn
    a.name = nome_asset(arq)
    a.type_ = cli.enums.AssetTypeEnum.IMAGE
    with open(arq, "rb") as f:
        a.image_asset.data = f.read()
    return op


# ── pedaços comuns da campanha ───────────────────────────────────────────

def op_orcamento(cli, rn, nome, valor_dia):
    op = cli.get_type("MutateOperation")
    b = op.campaign_budget_operation.create
    b.resource_name = rn
    b.name = f"BUDGET {nome}"
    b.amount_micros = int(round(valor_dia * 1e6))
    b.delivery_method = cli.enums.BudgetDeliveryMethodEnum.STANDARD
    b.explicitly_shared = False
    return op


# ── escrita ──────────────────────────────────────────────────────────────

def mutate(cli, cid, ops, validar, rotulos):
    """Um pedido só, atômico, e a única porta de escrita. `rotulos[i]` diz o que é a operação i, pro
    erro apontar o objeto, não um índice."""
    if not validar:
        comum.teto_campanha()        # sem teto combinado, escrita nenhuma sai, por caminho nenhum
    from google.ads.googleads.errors import GoogleAdsException
    req = cli.get_type("MutateGoogleAdsRequest")
    req.customer_id = cid
    req.mutate_operations.extend(ops)
    req.validate_only = validar
    req.partial_failure = False
    try:
        return cli.get_service("GoogleAdsService").mutate(request=req)
    except GoogleAdsException as e:
        print(f"\n  !!! O GOOGLE RECUSOU ({'validação a seco' if validar else 'escrita'}), "
              f"request_id {e.request_id}. Nada foi criado neste pedido:")
        for err in e.failure.errors:
            idx = None
            for el in err.location.field_path_elements:
                if el.field_name == "mutate_operations":
                    idx = el.index
                    break
            onde = rotulos[idx] if idx is not None and idx < len(rotulos) else "?"
            campo = ".".join(el.field_name for el in err.location.field_path_elements[1:])
            print(f"     - [{onde}] {campo}: {err.message}")
        sys.exit(1)


def id_temporario_para_real(resp, rotulos, prefixo):
    """Resource names reais das operações cujo rótulo começa com `prefixo`."""
    out = []
    for i, r in enumerate(resp.mutate_operation_responses):
        if rotulos[i].startswith(prefixo):
            campo = r._pb.WhichOneof("response")
            out.append(getattr(r, campo).resource_name)
    return out


# ── leitura de volta ─────────────────────────────────────────────────────

def le_campanha(g, cid, camp_id):
    q = lambda s: list(g.search(customer_id=cid, query=s))
    d = {"id": str(camp_id), "grupos": {}, "ads": [], "horarios": [], "geo_campanha": set()}
    for r in q(f"""SELECT campaign.name, campaign.status, campaign.advertising_channel_type,
            campaign.bidding_strategy_type, campaign.end_date_time, campaign.start_date_time,
            campaign.frequency_caps,
            campaign_budget.amount_micros FROM campaign WHERE campaign.id = {camp_id}"""):
        c = r.campaign
        d.update(nome=c.name, status=c.status.name, canal=c.advertising_channel_type.name,
                 lance=c.bidding_strategy_type.name, fim=c.end_date_time, inicio=c.start_date_time,
                 orcamento=r.campaign_budget.amount_micros / 1e6,
                 frequencia=[(f.key.event_type.name, f.key.time_unit.name, f.key.time_length, f.cap)
                             for f in c.frequency_caps])
    for r in q(f"""SELECT campaign_criterion.type, campaign_criterion.negative,
            campaign_criterion.location.geo_target_constant, campaign_criterion.ad_schedule.day_of_week,
            campaign_criterion.ad_schedule.start_hour, campaign_criterion.ad_schedule.end_hour
            FROM campaign_criterion WHERE campaign.id = {camp_id}"""):
        c = r.campaign_criterion
        if c.type_.name == "LOCATION" and not c.negative:
            d["geo_campanha"].add(c.location.geo_target_constant.split("/")[-1])
        elif c.type_.name == "AD_SCHEDULE":
            d["horarios"].append((c.ad_schedule.day_of_week.name, c.ad_schedule.start_hour,
                                  c.ad_schedule.end_hour))
    for r in q(f"""SELECT ad_group.id, ad_group.name, ad_group.status,
            ad_group.optimized_targeting_enabled, ad_group.cpc_bid_micros
            FROM ad_group WHERE campaign.id = {camp_id} AND ad_group.status != 'REMOVED'"""):
        d["grupos"][str(r.ad_group.id)] = {
            "nome": r.ad_group.name, "status": r.ad_group.status.name,
            "ot": r.ad_group.optimized_targeting_enabled, "cpc": r.ad_group.cpc_bid_micros / 1e6,
            "geo": set(), "inclui": [], "exclui": [], "audiences": []}
    for r in q(f"""SELECT ad_group.id, ad_group_criterion.type, ad_group_criterion.negative,
            ad_group_criterion.location.geo_target_constant, ad_group_criterion.user_list.user_list,
            ad_group_criterion.audience.audience
            FROM ad_group_criterion WHERE campaign.id = {camp_id}
            AND ad_group_criterion.type IN ('LOCATION','USER_LIST','AUDIENCE')"""):
        gr = d["grupos"].get(str(r.ad_group.id))
        if not gr:
            continue
        c = r.ad_group_criterion
        t = c.type_.name
        if t == "LOCATION" and not c.negative:
            gr["geo"].add(c.location.geo_target_constant.split("/")[-1])
        elif t == "USER_LIST":
            (gr["exclui"] if c.negative else gr["inclui"]).append(c.user_list.user_list.split("/")[-1])
        elif t == "AUDIENCE":
            gr["audiences"].append(c.audience.audience.split("/")[-1])
    for gr in d["grupos"].values():
        for aid in gr["audiences"]:
            for r in q(f"""SELECT audience.id, audience.dimensions, audience.exclusion_dimension
                    FROM audience WHERE audience.id = {aid}"""):
                for dim in r.audience.dimensions:
                    for s in dim.audience_segments.segments:
                        if s.user_list.user_list:
                            gr["inclui"].append(s.user_list.user_list.split("/")[-1])
                for e in r.audience.exclusion_dimension.exclusions:
                    if e.user_list.user_list:
                        gr["exclui"].append(e.user_list.user_list.split("/")[-1])
    for r in q(f"""SELECT ad_group.id, ad_group_ad.ad.name, ad_group_ad.status, ad_group_ad.ad.type,
            ad_group_ad.ad.final_urls FROM ad_group_ad
            WHERE campaign.id = {camp_id} AND ad_group_ad.status != 'REMOVED'"""):
        a = r.ad_group_ad
        d["ads"].append({"grupo": str(r.ad_group.id), "nome": a.ad.name, "status": a.status.name,
                         "tipo": a.ad.type_.name, "url": list(a.ad.final_urls)[0] if a.ad.final_urls else ""})
    return d


def resumo_leitura(d):
    """A linha lida de volta, por nível. É ela que se entrega, nunca a intenção do script."""
    linhas = [f"  lido: {d.get('nome')} · {d.get('status')} · {d.get('canal')} · {d.get('lance')} · "
              f"{comum.brl(d.get('orcamento', 0))}/dia · início {d.get('inicio')} · fim {d.get('fim')}"]
    for gr in d["grupos"].values():
        linhas.append(f"        grupo {gr['nome']}: {gr['status']} · otimizada={gr['ot']} · "
                      f"geo {sorted(gr['geo']) or '-'} · inclui {len(set(gr['inclui']))} / "
                      f"exclui {len(set(gr['exclui']))}")
    for a in d["ads"]:
        linhas.append(f"        anúncio {a['nome']}: {a['status']} · {a['tipo']}")
    return "\n".join(linhas)


def campanha_por_nome(g, cid, nome, canal):
    for r in g.search(customer_id=cid, query=f"""
            SELECT campaign.id, campaign.name FROM campaign
            WHERE campaign.status != 'REMOVED' AND campaign.advertising_channel_type = '{canal}'"""):
        if r.campaign.name == nome:
            return str(r.campaign.id)
    return None


def grupo_e_anuncios(g, cid, camp_id, nome_grupo):
    """(resource_name do grupo, {nome: status} dos anúncios não removidos) da campanha existente."""
    rn_ag = None
    for r in g.search(customer_id=cid, query=f"""
            SELECT ad_group.resource_name, ad_group.name FROM ad_group
            WHERE campaign.id = {camp_id} AND ad_group.status != 'REMOVED'"""):
        if r.ad_group.name == nome_grupo:
            rn_ag = r.ad_group.resource_name
    ja = {}
    if rn_ag:
        for r in g.search(customer_id=cid, query=f"""
                SELECT ad_group_ad.ad.name, ad_group_ad.status FROM ad_group_ad
                WHERE ad_group.resource_name = '{rn_ag}' AND ad_group_ad.status != 'REMOVED'"""):
            ja[r.ad_group_ad.ad.name] = r.ad_group_ad.status.name
    return rn_ag, ja
