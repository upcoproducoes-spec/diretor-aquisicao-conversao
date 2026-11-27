---
name: preflight
description: Confere a saúde das contas de anúncio (Meta e Google) lendo a plataforma, numa lista fixa de 12 itens: gasto contra o teto, anúncio com entrega restrita, expansão de público ligada onde não pode, país, idade, lance, UTM, rastreio da página, decisão vencida, pixel no rastreio do anúncio e nota do pixel. Use antes de subir ou ligar campanha, no começo de todo `/revisar` de tráfego e todo dia na rotina de tráfego. Só lê: não muda nada em plataforma nenhuma. Dispara quando pedirem "preflight", "saúde da conta", "confere a conta antes de subir", "tem algo errado na conta".
---

> Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
> são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
> ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.


# Preflight: a saúde da conta

Roda igual toda vez. Ele nasceu de um dia com três erros cometidos com o conhecimento certo **já escrito e
já lido**: teto que barrava operação normal, anúncio limitado por política e expansão de público ligada
contra a decisão registrada. A conclusão foi que documento que depende de alguém lembrar falha, e
conferência que roda igual toda vez não.

**Rode a lista inteira, nunca de memória e nunca só o item que parece ter a ver com o pedido.**

Regras do preflight:

1. **Só leitura.** Nada de criar, editar, pausar ou ativar, em plataforma nenhuma. Achou erro, aponta.
2. **A régua do que entra:** só o que **gastou nos últimos 7 dias ou hoje**. Os itens 3 e 10 olham também o
   conjunto pausado ou criado nos últimos 14 dias, porque o erro nasce na criação. O item 5 olha o que
   deveria estar gastando e não está. No caso de origem, a primeira versão varreu a conta inteira e cuspiu
   44 anúncios "restritos", quase todos de lançamentos encerrados, e os 2 que importavam ficaram
   enterrados. Checagem ruidosa é checagem que ninguém lê.
3. **O "últimos 7 dias" do Google exclui hoje**, e campanha criada hoje é a mais provável de estar errada:
   inclua hoje numa leitura à parte.
4. **Item que não deu pra conferir vira NÃO VERIFICADO, com o motivo.** Nunca se pula calado, e nunca vira
   OK. Sem conector, peça print ou export da tela, ou deixe NÃO VERIFICADO.
5. **O dado vem da plataforma**, nunca do pacote, do briefing ou do relatório de ontem.

## De onde vem o teto

O item 1 precisa do teto combinado: por campanha e, se houver, da conta. Procure no `CLAUDE.md` (seção
Ferramentas), no briefing do lançamento e em `frameworks-da-casa/`. Não achou, o item 1 fica NÃO VERIFICADO
e a entrega pergunta qual é o teto. Não invente.

## Como ler

Testado no caso de origem, lendo só pelos conectores, numa Black em captação.

**Meta (conector).** A conta sai de `ads_get_ad_accounts`, e o `ad_account_id` é só o número, sem `act_`.
Confirme os campos com `ads_get_field_context`.

- **Gasto e entrega:** `ads_get_ad_entities`, `level=adset`, `date_preset=last_7d`, filtro `amount_spent`
  maior que 0, campos `name`, `campaign_name`, `effective_status`, `daily_budget`, `lifetime_budget`,
  `amount_spent`, `created_time`, `delivery`. Repita com `date_preset=today`.
- **Ativo sem gastar (item 5):** a mesma leitura, sem o filtro de gasto, com `effective_status IN ACTIVE`,
  `impressions` e o período inteiro da fase.
- **Configuração (itens 3, 4 e 10):** o `targeting` volta enorme. Um conjunto só chega perto de 30 KB, porque
  traz a regra de cada público excluído, e não dá pra pedir pedaço dele: `targeting.age_min` volta em
  `unknown_fields`. Peça `id`, `name` e `targeting` por `object_ids`, poucos conjuntos por vez, uma vez só por
  conjunto, e olhe só `age_min`, `age_max`, `geo_locations`, `targeting_automation.advantage_audience`,
  `targeting_relaxation_types`, `custom_audiences` e `excluded_custom_audiences`.
- **Pausados ou criados nos últimos 14 dias (itens 3 e 10):** filtro `created_time GREATER_THAN <data>`, e
  `updated_time GREATER_THAN <data>` com `effective_status NOT_EQUAL ACTIVE`.
- **Anúncios (item 2):** `level=ad`, com filtro de gasto, campos `name`, `effective_status`, `delivery`,
  `amount_spent`. Entrega restrita aparece em `effective_status` e nos `substatuses` de `delivery`.
- **UTM (item 6):** o conector não devolve `url_tags`, mas devolve o link do criativo de vídeo (`link_url`). Procure
  `{{campaign.id}}`, `{{adset.id}}` e `{{ad.id}}` no link; o que estiver no `url_tags` não aparece, então a prova
  final é a tabela de UTM do Dash (o lead chega com nome nos três níveis, ou não).

**Google (conector `google-ads-mcp`, ferramenta `search_search`).** `customer_id` só com números. Sempre com
data: GAQL sem `segments.date` soma a vida inteira da conta, sem erro, e volta anúncio de anos atrás. Nunca
filtre por nome com colchete: `LIKE '%[TAG]%'` pode voltar campanha errada, também sem erro. Filtre por
`campaign.id` ou por um trecho sem colchete.

| Pra quê | Resource | Campos | Condições |
|---|---|---|---|
| Campanhas com gasto | `campaign` | `campaign.id`, `campaign.name`, `campaign.status`, `campaign.bidding_strategy_type`, `campaign_budget.amount_micros`, `metrics.cost_micros` | `segments.date DURING LAST_7_DAYS` e `metrics.cost_micros > 0`; repita com `TODAY` |
| Segmentação otimizada | `ad_group` | `campaign.name`, `ad_group.name`, `ad_group.optimized_targeting_enabled` | `ad_group.status = 'ENABLED'`, `campaign.status = 'ENABLED'` |
| Geografia | `ad_group_criterion` | `campaign.name`, `ad_group.name`, `ad_group_criterion.negative`, `ad_group_criterion.location.geo_target_constant` | `ad_group_criterion.type = 'LOCATION'`, `ad_group.status = 'ENABLED'`, `campaign.status = 'ENABLED'` |
| Gasto por país | `user_location_view` | `campaign.name`, `user_location_view.country_criterion_id`, `metrics.cost_micros` | `segments.date DURING TODAY` |
| Política | `ad_group_ad` | `ad_group_ad.ad.id`, `ad_group_ad.policy_summary.approval_status`, `ad_group_ad.policy_summary.policy_topic_entries`, `metrics.cost_micros` | `segments.date DURING LAST_7_DAYS` e `metrics.cost_micros > 0`; repita com `TODAY` |
| Gasto por hora | `campaign` | `campaign.name`, `segments.hour`, `metrics.cost_micros` | `segments.date DURING TODAY` e `metrics.cost_micros > 0` |
| Gasto depois do fim | `campaign` | `campaign.name`, `campaign.end_date_time`, `segments.date`, `metrics.cost_micros` | `segments.date DURING LAST_30_DAYS` e `metrics.cost_micros > 0` |
| Lance manual sem lance | `ad_group` | `campaign.name`, `campaign.status`, `campaign.bidding_strategy_type`, `ad_group.name`, `ad_group.cpc_bid_micros` | `campaign.bidding_strategy_type = 'MANUAL_CPC'`, `campaign.status = 'ENABLED'`, `ad_group.cpc_bid_micros <= 10000` |
| Anúncio gerado sozinho | `ad_group_ad` | `ad_group_ad.ad.id`, `ad_group_ad.ad.name`, `ad_group_ad.ad.type`, `ad_group_ad.status` | `campaign.id = <id>`, `ad_group_ad.status != 'REMOVED'` |
| Criada nos últimos dias | `campaign` | `campaign.id`, `campaign.name`, `campaign.status`, `campaign.start_date_time` | `campaign.status != 'REMOVED'` |
| UTM | `ad_group_ad` | `ad_group_ad.ad.final_urls`, `campaign.tracking_url_template` | `metrics.cost_micros > 0` e `segments.date DURING LAST_7_DAYS`, com `metrics.cost_micros` nos campos |

O que cada consulta quer dizer está no §32 de `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`. Sem o
conector do Google, o Dash Fácil cobre gasto e lead, mas não cobre configuração: os itens 2, 3, 4, 5 e 6 do
Google ficam NÃO VERIFICADOS. Como ligar: `sirius-scale/instalacao/google-ads.md`.

**Dash Fácil.** `configuracoes_lancamento` traz as páginas (`paginas_cap`). `resumo_saude_lancamento` traz os
alertas de rastreio. `tabela_utm_captacao` traz inscritos e investimento por campanha, conjunto e anúncio.

## Os 12 itens

| # | Conferir | Exceção à régua | Onde está a regra |
|---|---|---|---|
| 1 | **Gasto diário somado** (Meta com imposto + Google) contra a verba e o teto aprovados, e campanha ou conjunto acima do teto por campanha. A soma sai da plataforma, nunca de cabeça. O teto é com imposto. Se o Dash estiver com `add_meta_tax` ligado, o gasto dele já vem com imposto | — | `sirius-scale/REGRAS.md` §6 |
| 2 | **Anúncio gastando com entrega restrita** ou limitada por política. No Google, aprovado com limitação não é reprovado: são tratamentos diferentes | — | `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §20 |
| 3 | **Expansão de público ligada em todo conjunto de público quente (`[PQ]`), em qualquer fase:** remarketing, aquecimento, aulas, carrinho e captação pra quem já é da casa. Na Meta são dois interruptores, e desligar um não desliga o outro; no Google, a segmentação otimizada liga sozinha | inclui conjunto pausado ou criado nos últimos 14 dias: o erro nasce na criação, e no minuto em que o conjunto ativa o dinheiro já vaza | `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.3 e §4.6 |
| 4 | **País.** Na Meta, `geo_locations` contra o briefing. No Google, grupo gastando sem segmentação geográfica, pela configuração (Demand Gen só aceita no grupo; Display e Pesquisa, na campanha) e pelo efeito (gasto de hoje fora do país acima de 5%) | — | `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §6 e §7 |
| 5 | **Ativo com orçamento e gasto zero.** Na Meta, conjunto ativo sem impressão: olhe `delivery` (`warning`, `learning_exit_unsuccessfully`). No Google, lance manual sem lance no grupo. Tudo o que se costuma olhar parece certo (status, aprovação, público); só o gasto zerado denuncia | olha o que **deveria** estar gastando e não está | `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §21 |
| 6 | **UTM quebrada em anúncio ativo.** Espaço é `%20`; com `+` cru, o Dash não junta o gasto com o lead. No Google, leia `final_urls`. Na Meta, procure `+` no nome de campanha e conjunto (a macro copia o nome pra UTM) e compare no Dash os inscritos da campanha com a soma dos conjuntos: inscrito fora de conjunto é o sinal. Também é UTM quebrada id no lugar do nome (`{{campaign.id}}`, `{{adset.id}}`, `{{ad.id}}`): o Dash não liga o lead ao criativo. Isso costuma vir de `creative_id` antigo reaproveitado | — | `sirius-scale/frameworks/trafego/nomenclatura.md` §3 |
| 7 | **Defasagem do YouTube Analytics:** até que dia o dado já foi processado, antes de comparar com gasto do dia ou afirmar qualquer coisa sobre view. Só vale se a análise do dia usa view do YouTube; sem isso, marque "não se aplica" | — | `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.1 |
| 8 | **Página no ar sem o rastreio.** O endereço sai de `paginas_cap`, no Dash. Baixe o HTML e procure o pixel (`fbevents.js` ou `fbq(`), a tag do Google (`gtag(` ou `AW-`) e o script do Dash (`dfq(`). Só o gerenciador de tags (`gtm.js`) no HTML não prova nada: fica NÃO VERIFICADO, com a prova pelo efeito ao lado (inscritos entrando no Dash, evento no pixel e os alertas do `resumo_saude_lancamento`). No caso de origem, o gerenciador foi publicado vazio e o Dash ficou 2 dias sem lead com a captação rodando; só quem olhou o gráfico viu | — | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7 |
| 9 | **Decisão temporária com data de validade** (ex.: "sem exclusão de alunos até a próxima fase começar"): a data passou e o objeto continua no estado temporário? | — | o briefing (campo "Decisões temporárias") ou `frameworks-da-casa/` |
| 10 | **Idade do conjunto na Meta contra o briefing.** A idade mínima é controle: a plataforma respeita e não entrega abaixo dela. A faixa etária é sugestão: com o Advantage+ ligado, a Meta pode entregar fora dela. A mínima tem que bater com o briefing; faixa que o briefing trata como limite não segura com o Advantage+ ligado | inclui conjunto pausado ou criado nos últimos 14 dias, como no item 3 | `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §1 |
| 11 | **Anúncio que leva pra site sem o pixel no rastreio.** Leia o `tracking_specs` de cada anúncio da Meta (uma chamada pra conta, com filtro de nome): precisa ter `offsite_conversion` com o pixel. Campanha de cadastro põe sozinha; anúncio de tráfego ou alcance criado por API sai sem, e aí a Meta não credita compra, checkout nem AddToCart a ele. Com esse anúncio no ar, zero de conversão por anúncio não quer dizer zero venda | só o que roda hoje: a Meta deixa ACTIVE o anúncio de conjunto que já acabou, então olhe também o status e o fim do conjunto | `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`, "Anúncio de tráfego criado por API sai sem o pixel" |
| 12 | **Nota do pixel dos eventos que conjunto ativo otimiza** (`ads_get_dataset_quality`, ou a tela de qualidade do evento): queda de 1 ponto ou mais contra a mediana dos 7 dias anteriores, ou evento que perdeu a nota. Leitura que falha é NÃO VERIFICADO, nunca nota boa | conjunto encerrado não conta, mesmo ACTIVE (como no item 11) | o Gerenciador de Eventos da Meta |

Os itens 4, 9 e 10 comparam com o briefing. Sem país, idade ou decisões temporárias no briefing, mostre o que a
plataforma tem, marque NÃO VERIFICADO e peça o campo.

## Como entregar

Sempre no mesmo formato, com a data e a hora da leitura e as contas lidas:

```
Saúde da conta · <data e hora> · <contas lidas>
1. Gasto x teto: OK | ACHADO | NÃO VERIFICADO · <uma linha com o número e a fonte>
2. Entrega restrita: ...
...
10. Idade: ...
11. Pixel no rastreio: ...
12. Nota do pixel: ...
```

Depois da lista, um parágrafo por ACHADO: qual objeto, o que a plataforma mostra, a regra e o que decidir.

**O que acusar abre a entrega e entra como achado de verdade**, não como observação: pela régua acima, tudo
que aparece é acionável agora. Achado não proíbe mexer na conta; proíbe mexer **sem decidir**. Cada um vai
pra conversa com o resumo antes de qualquer ação, e mexer em objeto ativo é com vocês, nas plataformas
(`sirius-scale/REGRAS.md` §6).

O preflight não substitui o `/revisar`, e o `/revisar` não substitui o preflight. Ele pega o que dá pra
conferir igual toda vez; o `/revisar` pega o que exige julgamento (nome, verba contra briefing, público
contra pesquisa).

Salve em `entregas/analises/preflight-<AAAA-MM-DD>.md` quando rodar pela rotina ou antes de subir campanha.
