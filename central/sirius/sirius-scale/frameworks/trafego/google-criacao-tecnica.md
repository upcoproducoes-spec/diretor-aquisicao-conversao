# Google Ads API — notas técnicas de criação/escrita

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma
> **Alcance:** UNIVERSAL — comportamento da API do Google Ads, igual pra
> qualquer cliente e qualquer empresa. Sem eixo de força: é fato de plataforma,
> não padrão observado. Ressalva: números em BRL (piso de orçamento) valem pra
> conta em real — conta em outra moeda tem outro piso. Onde uma seção traz
> rótulo próprio (VARIAÇÃO ISOLADA, CONSISTENTE), o rótulo da seção vale: o que
> é VARIAÇÃO ISOLADA foi medido só na conta do caso-base (a exceção é o §33).

> Equivalente do `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`, para
> o Google. Armadilha técnica real encontrada ao **construir/editar** campanha
> via API — não teoria. Armadilha nova que vocês acharem vai em
> `frameworks-da-casa/` (`sirius-scale/REGRAS.md` §4).
>
> **De onde vêm os casos:** de uma conta só, a do caso-base (um expert de
> educação, num nicho de concurso). "O 1º lançamento" é o lançamento gratuito de
> referência dessa conta; "o 2º lançamento" é o seguinte, onde quase tudo deste
> arquivo foi medido. Também aparecem, na mesma conta, a distribuição de
> conteúdo, um lançamento pago semanal e a captação de uma Black. As datas
> viraram relativas à fase do 2º lançamento (captação, semana de aulas,
> carrinho, downsell). Onde o texto conta um erro, é erro da operação da casa,
> contado pra não se repetir. O §33 é a exceção: veio da conta de outro expert
> da casa, reativada pra uma Black.
>
> **Pra quem é:** pro Claude que lê a conta pelo conector do Google e monta o
> pacote de campanha, e pra quem sobe a campanha. Escrita em plataforma segue
> `sirius-scale/REGRAS.md` §6: no Google, o Claude lê pelo conector e, com pedido
> escrito e pacote aprovado, monta a campanha PAUSADA pelas ferramentas de
> `sirius-scale/ferramentas/google/`; ligar é da pessoa dona da conta. As receitas de código abaixo são da SDK
> oficial do Google Ads em Python e valem pra quem escreve pela API; as
> armadilhas valem igual pra quem monta pela interface; as consultas de leitura
> (GAQL) servem pro Claude conferir a conta.
>
> **"Conferência" e "leitura diária":** no caso de origem, essas checagens
> rodavam em script, lendo a conta pela API. Aqui elas viram o checklist do §32,
> que o Claude roda lendo a conta pelo conector (se estiver ligado) ou que quem
> sobe a campanha confere na tela.

## 0. RECEITA — criar uma campanha Demand Gen do zero, na ordem certa

> **Esta seção é o índice de uso do arquivo.** As outras são armadilhas isoladas,
> ordenadas por data de descoberta; esta é a ordem em que as coisas acontecem.
> Executada de verdade na captação do 2º lançamento (uma campanha nova de mix
> quente, criada a partir da campanha de escala de público quente).

⚠️ **Escreva estágio por estágio, do mais barato pro mais caro.** `validate_only`
(§4) só cobre o primeiro estágio: campanha, grupo e anúncio referenciam IDs que
ainda não existem, então só validam no momento da escrita. Um estágio que falha
deixa os anteriores criados — quem escreve tem que saber continuar de onde
parou, e não recriar do começo (senão sobra orçamento órfão na conta). *(A
exceção apareceu depois, no §30: mandando a cadeia inteira num só
`GoogleAdsService.Mutate` com IDs temporários, o `validate_only` valida tudo de
uma vez.)*

| # | Passo | Não esqueça | Onde |
|---|---|---|---|
| 0 | **Ler a config completa da campanha de referência** | Nunca criar do zero: o default da conta muda dentro do mesmo lançamento | §10 |
| 1 | `CampaignBudget` | `amount_micros`, `STANDARD`, `explicitly_shared=False`. Piso R$ 25,40 (valor da época, conferir na plataforma) | §1 |
| 2 | `Campaign` | `advertising_channel_type=DEMAND_GEN`, lance copiado da referência, **`contains_eu_political_advertising`**, `status=PAUSED` | §8 |
| 3 | **Metas de conversão** | O Google cria as 8 categorias sozinho. Ler `campaign_conversion_goal` e pôr `biddable=True` **só na que importa** | §2, §10 |
| 4 | `AdGroup` | Depois, num update separado: `optimized_targeting_enabled=True` | §10 |
| 5 | **Público** | `Audience` agrupada — `user_list` solto é recusado | §11 |
| 6 | `AdGroupAd` | `DEMAND_GEN_VIDEO_RESPONSIVE_AD` — estrutura abaixo | §9, §12 |
| 7 | Geo | Demand Gen recusa geo na campanha; vai no grupo, e a ausência é silenciosa | §6, §7 |
| 8 | **Ativar** | Passo separado, depois do checklist do §32 e de conferir na tela | `sirius-scale/REGRAS.md` §6 |

**Erros do dia em que a receita foi executada, que esta ordem teria evitado:**
`contains_eu_political_advertising` (já estava no §8 — falha de consulta, não de
conhecimento) e `user_list` solto (§11, genuinamente novo). Os dois derrubaram a
criação inteira no meio.

⚠️ **E o erro que a ordem NÃO evitou, no mesmo dia:** a cadeia parou no passo 5
(§11), quem completou refez 5, 4 e 6 — e **pulou o 7 (geo)**. A campanha foi
ativada assim e gastou **83% do dia fora do Brasil** (nas primeiras ~10h:
Índia, México, Paquistão, +130 países; 3 conversões). O §6 e o §7 já registravam
exatamente isso dois dias antes. **Regra que nasceu daí (decisão do Rodrigo):**

1. Cadeia que para no meio → quem completa **reexecuta a receita do passo onde
   parou até o 8**, não só o passo que falhou.
2. O passo 8 (ativar) só acontece depois de a **conferência campo a campo contra
   a campanha de referência** passar sem FAIL (checklist do §32). Ela confere
   esta tabela item a item contra a referência (lance, metas, rede,
   segmentação, público, **geo por grupo**, vídeo/aprovação/UTM por anúncio).
3. Toda trava antes de ativar barra grupo Demand Gen ativo sem LOCATION, e a
   leitura diária da conta também mede o gasto do dia por país (§7).

## 1. Piso de orçamento diário: R$ 25,40 em BRL (valor da época, conferir na plataforma)

**Observado na 1ª semana de captação do 2º lançamento**, campanha Demand Gen.
Tentativa de colocar um orçamento um pouco abaixo do piso foi recusada:

```
campaign_budget_error: BUDGET_BELOW_PER_DAY_MINIMUM
details.budget_per_day_minimum_error_details {
  currency_code: "BRL"
  budget_per_day_minimum_micros: 25400000    <- o piso
  failed_budget_amount_micros: 25000000      <- o valor tentado
}
```

O valor exato do piso vem **no detalhe do erro**, não na documentação — se
bater nisso de novo, ler `budget_per_day_minimum_micros` em vez de chutar.

📌 **Consequência de planejamento:** ao ratear verba entre muitas campanhas
(ex: 1-1-1 por criativo x 2 canais), nenhuma fatia pode ficar abaixo do piso
(arredonde pra cima). Numa leva de 10 campanhas, o piso do Google sozinho já é
10× o piso diário, mesmo que o plano peça menos.

## 2. Demand Gen define meta de conversão em `campaign_conversion_goal`, não em `selective_optimization`

**Erro real de leitura cometido na 1ª semana de captação do 2º lançamento** —
vale registrar porque quase virou uma "correção" que teria quebrado algo que
estava certo.

Ao auditar as campanhas do 2º lançamento, `campaign.selective_optimization.
conversion_actions` voltou **vazio** em todas as 10. A leitura apressada foi:
"as campanhas não têm meta própria, então herdam a mistura da conta — e a
conta tem 5 ações marcadas `primary_for_goal=True`, incluindo Visualização de
Página, então o Target CPA vai perseguir o evento mais barato".

**Estava errado.** Demand Gen usa outro recurso:

```sql
SELECT campaign_conversion_goal.category,
       campaign_conversion_goal.origin,
       campaign_conversion_goal.biddable
FROM campaign_conversion_goal
WHERE campaign.id = ...
```

O resultado real mostrou 8 categorias listadas, mas **só `SUBMIT_LEAD_FORM`
com `biddable=True`** — todas as outras (PURCHASE, PAGE_VIEW, CONTACT,
BEGIN_CHECKOUT, DOWNLOAD, ENGAGEMENT, YOUTUBE_FOLLOW_ON_VIEWS) em `False`.
Ou seja: a otimização já estava correta.

📌 **Isto é a regra 1 do `sirius-scale/frameworks/trafego/_metodologia.md` ("o
nome nunca diz o que está sendo medido") aplicada a si mesma:** o campo vazio
também não diz. Antes de concluir que uma meta está errada, confirmar no
recurso certo da plataforma.

| Plataforma | Onde a meta real mora |
|---|---|
| Meta | `promoted_object.custom_event_type` (no conjunto) |
| Google — Search/Display | `campaign.selective_optimization.conversion_actions` |
| Google — Demand Gen | `campaign_conversion_goal` + campo `biddable` |

## 3. GAQL não deixa cruzar `campaign_budget` com `ad_group_ad`

```
query_error: PROHIBITED_RESOURCE_TYPE_IN_SELECT_CLAUSE
"Cannot select fields from the following resource: 'CAMPAIGN_BUDGET',
 since the resource is incompatible with the resource in FROM clause."
```

Puxar orçamento e anúncio de uma vez só não funciona. São duas queries: uma
`FROM campaign` (para orçamento) e outra `FROM ad_group_ad` (para anúncio),
juntando por `campaign.id` no código.

**Mais duas de GAQL, ambas do dia em que a receita do §0 foi executada (UNIVERSAL):**

- **Filtro por campo de outro recurso numa view exige o campo no SELECT.**
  `SELECT ... FROM user_location_view WHERE campaign.status = 'ENABLED'` volta
  `"The following field must be present in SELECT clause: 'campaign.status'"`.
  Põe `campaign.status` no SELECT e passa.
- **Colchete dentro de `LIKE` quebra a query.** `LIKE '%<TAG>%CAPTACAO][ESCALA%'`
  devolve `INVALID_VALUE_WITH_LIKE_OPERATOR` ("may only be used with non-empty
  strings of valid Google SQL syntax"). A nomenclatura da casa usa colchetes em
  todo nome de campanha (`sirius-scale/frameworks/trafego/nomenclatura.md`),
  então isso morde sempre: filtre por trechos **sem** o colchete
  (`'%<TAG>%ESCALA%'`, onde `<TAG>` é a tag do lançamento).

- **Intervalo de data precisa dos DOIS lados** (UNIVERSAL).
  `WHERE segments.date >= 'AAAA-MM-DD'` sozinho devolve
  `EXPECTED_FILTERS_ON_DATE_RANGE` ("Expects filters on the following field to
  limit a finite date range: 'segments.date'"). Use `BETWEEN 'X' AND 'Y'` ou
  `DURING LAST_7_DAYS` — lembrando que `DURING LAST_7_DAYS` **exclui o dia
  corrente** (§7).

- **Alcance e frequência por campanha Demand Gen** (medido na captação de uma
  Black). `metrics.unique_users` e `metrics.average_impression_frequency_per_user`
  saem no recurso `campaign`, com a data no WHERE: a campanha de alunos devolveu
  os dois já no 1º dia. Ressalvas, de ajuda do Google e de fonte secundária
  ainda não conferidas na referência oficial: janela de até 92 dias, não soma
  entre campanhas, não existe no nível de cliente. A frequência é a do período
  inteiro. Dividir pelos dias só faz sentido com dias cheios, e ela **não** é a
  "impressão por pessoa do público" de um plano de verba: essa é impressões ÷
  tamanho do público ÷ dias cheios, e a frequência da plataforma é impressões ÷
  alcance (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §5).
  *UNIVERSAL (métrica da plataforma).*


## 3.2 `[` quebra o operador `LIKE` do GAQL

`CONSISTENTE` (fato de plataforma).

A nomenclatura da casa põe colchete em tudo (`[LC] [<PRODUTO>] [YT] [<TAG>]…`),
e filtrar por um pedaço que inclua colchete **não funciona**:

```
LIKE '%<TAG>] [CPL%'
  → query_error: INVALID_VALUE_WITH_LIKE_OPERATOR
    "Value: %<TAG>] [CPL% is invalid. The LIKE operator may only be used
     with non-empty strings of valid Google SQL syntax."
```

Filtre por um trecho **sem colchete** (o pedaço do momento ou da fase, sem o
colchete), ou resolva o id antes e filtre por `campaign.id`.

⚠️ **O erro nem sempre vem.** `campaign.name LIKE '%[<TAG>]%'`, com o colchete
fechado, rodou sem erro pelo conector e voltou campanhas de anos atrás, nenhuma do
lançamento: o colchete foi tratado como conjunto de letras. Resultado estranho
num filtro com colchete é esse caso, não falta de campanha.

⚠️ **A armadilha de verdade não é o erro — é como ele morre.** A conferência do
caso de origem saía com erro quando o filtro casava com != 1 campanha. Rodada
num laço de shell com `| grep`, o `$?` é o código do **grep**, não o da
conferência: isso devolveu "7 tags, 0 FAIL" com **zero item conferido**, e
quase foi lido como aprovação. Ou pega o status do primeiro comando do pipe
(`PIPESTATUS` no bash, `pipestatus` no zsh), ou não pipa a saída da
conferência. Conferência que não confere nada é pior que conferência nenhuma,
porque parece verde — por isso o último item do §32 é contar quantos itens
foram de fato conferidos.

## 3.1 `change_event` exige `LIMIT` explícito na query — sem ele, erro

Medido montando inventário de mudanças pra uma revisão técnica. Query sem
`LIMIT`:

```
error_code { change_event_error: LIMIT_NOT_SPECIFIED }
message: "Change event requests must specify a LIMIT in query and LIMIT
should be less than or equal to 10k."
```

Diferente do resto do GAQL, onde `LIMIT` é opcional. Em `change_event`
especificamente é **obrigatório**, e tem que ser ≤ 10.000. Sempre incluir
`LIMIT <n>` na query, mesmo que a intenção seja pegar tudo.

Alcance: **UNIVERSAL** — comportamento da API, sem dimensão de cliente.

**Adendo: a última edição de cada campanha.** A documentação oficial do
`change_event` aceita no máximo **30 dias** de janela e avisa até ~3 min de
atraso. É a leitura que dá a **última edição real** de cada campanha, que é de
onde se conta o intervalo entre mexidas de verba no mesmo objeto (a regra
atual da casa é uma mexida de verba por objeto por dia, contada da última
edição real — `sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md`
§5). A receita:

```sql
SELECT change_event.change_date_time, change_event.campaign FROM change_event
WHERE change_event.change_date_time >= '<hoje - 29 dias>' AND change_event.change_date_time <= '<hoje> 23:59:59'
  AND change_event.campaign IN ('customers/<cid>/campaigns/<id>', ...)
ORDER BY change_event.change_date_time DESC LIMIT 200
```

⚠️ *(11/2026, VARIAÇÃO ISOLADA)* Os 30 dias contam do relógio de verdade, não da data que você está lendo: refazer a
leitura de um dia anterior pedindo "data lida − 29" deu o erro de data antiga ("cannot be older than 30 days"). Use o
mais recente entre `<data lida> - 29` e `<hoje de verdade> - 29`.
O filtro `change_event.campaign IN (...)` não aparece na documentação, mas
funcionou: devolveu a última mudança das 3 campanhas de uma Black, e a de leads
bateu com o histórico do registro da operação.

## 4. `validate_only` é request object, não keyword

A SDK Python não aceita `validate_only=True` como argumento solto:

```python
# NÃO funciona
svc.mutate_campaign_budgets(customer_id=CID, operations=[op], validate_only=True)
# TypeError: got an unexpected keyword argument 'validate_only'

# Funciona
req = client.get_type("MutateCampaignBudgetsRequest")
req.customer_id = CID
req.operations.append(op)
req.validate_only = True
svc.mutate_campaign_budgets(request=req)
```

📌 **Usar isso sempre antes de escrita real.** No 2º lançamento as três mutações
(orçamento, `final_urls`, textos do anúncio) foram validadas assim antes de
rodar — confirmou que os campos eram editáveis sem precisar recriar anúncio,
e sem escrever nada na conta.

Também não existe `client.get_type("FieldMask")` — a máscara vem do protobuf:

```python
from google.protobuf import field_mask_pb2
op.update_mask.CopyFrom(field_mask_pb2.FieldMask(paths=["amount_micros"]))
```

## 5. O que É editável in-place num anúncio Demand Gen

Confirmado por escrita real na captação do 2º lançamento, sem recriar anúncio e
sem perder o ID (ou seja, sem quebrar o histórico do Dash):

| Campo | Editável | Máscara |
|---|---|---|
| Orçamento diário | sim | `amount_micros` (em `CampaignBudgetOperation`) |
| URL final / UTMs | sim | `final_urls` |
| Headlines | sim | `demand_gen_video_responsive_ad.headlines` |
| **Nome do anúncio (`ad.name`)** | **não** — `IMMUTABLE_FIELD` (medido ao renomear as campanhas de um lançamento pago semanal). Nome de campanha e de grupo mudam; o ID do criativo vai no `utm_term` da URL | — |
| Long headlines | sim | `demand_gen_video_responsive_ad.long_headlines` |
| Descriptions | sim | `demand_gen_video_responsive_ad.descriptions` |

Headline, long headline e description podem ir na **mesma** `AdOperation` que
a `final_urls`, com todos os paths na mesma `update_mask` — 1 chamada por
anúncio em vez de 3.

**Acrescentado por escrita real, na 3ª semana de captação:**

| Campo | Editável | Máscara |
|---|---|---|
| Vídeos do anúncio (acrescentar o vertical, trocar o 16:9) | sim | `demand_gen_video_responsive_ad.videos` — a lista inteira, o que ficar de fora sai |
| Content network da campanha | sim | `network_settings.target_content_network` (em `CampaignOperation`) |

⚠️ **`AdOperation` vai no `AdService`, e o resource name é
`customers/{cid}/ads/{ad_id}`** — não o caminho do `ad_group_ad`
(`customers/{cid}/adGroups/{g}/ads/{id}`), que é o que você tem na mão depois de
listar. Errar dá `RESOURCE_NAME_MALFORMED` e custou uma rodada.

📌 **Vídeo recém-subido no YouTube vira asset na hora:** os 6 uploads do dia
viraram `youtube_video_asset` no Google Ads no minuto seguinte, sem esperar
processamento (havia nova tentativa com espera por precaução, não precisou).
Cota da Data API zera à **meia-noite do Pacífico** (04h de Brasília no horário
de verão de lá; 05h fora dele) — 6 uploads (9.600 de 10.000 unidades) cabem num
dia de cota, sem folga pra um 7º. *(Pra criar o anúncio logo depois do upload,
ver o §28: a duração do vídeo leva minutos pra resolver.)*

### ⚠️ O nome óbvio do campo devolve VAZIO, não erro

A tabela acima usa `demand_gen_video_responsive_ad`. O nome que qualquer um
escreve de primeira é `video_responsive_ad` — e ele **existe** no esquema,
então o GAQL aceita:

```sql
-- ACEITO, e devolve headlines: []  para TODO anuncio Demand Gen
SELECT ad_group_ad.ad.video_responsive_ad.headlines FROM ad_group_ad

-- O CERTO
SELECT ad_group_ad.ad.demand_gen_video_responsive_ad.headlines FROM ad_group_ad
```

Não há erro, não há aviso: volta lista vazia para todos os anúncios. A leitura
natural disso é *"os anúncios estão sem headline"* — e foi exatamente essa a
conclusão errada, ao auditar a copy no ar da campanha de aquecimento.

📌 É a **mesma armadilha do §2** deste arquivo, com outro campo:
`selective_optimization` também volta vazio em Demand Gen e levou a quatro
relatórios afirmando que a meta de conversão estava quebrada. O padrão é o
mesmo e vale como reflexo:

> **Campo vazio em Demand Gen é primeiro suspeito de recurso errado, nunca
> prova de que a coisa não está configurada.** Antes de reportar ausência,
> procure o campo com prefixo `demand_gen_*` — o Demand Gen duplica nomes de
> recursos antigos em vez de reusá-los.

Quem lê a tabela do §5 acerta por sorte. Quem escreve um `SELECT` do zero cai.

## 6. Demand Gen RECUSA segmentação geográfica no nível de campanha

**Descoberto na 2ª semana de captação do 2º lançamento**, ao corrigir campanhas
que estavam servindo fora do Brasil. Tentativa de criar `campaign_criterion` do
tipo LOCATION recusou as 7 campanhas de uma vez:

```
request_error: UNKNOWN
message: "The error code is not in this version."
trigger { string_value: "OWNED_AND_OPERATED" }
location { field_path_elements { field_name: "location" } }
```

Demand Gen serve inventário próprio do Google (YouTube, Discover, Gmail) e a
geo não mora na campanha. **É no `ad_group_criterion`**, e foi assim que o
1º lançamento sempre fez — 14 critérios `LOCATION = geoTargetConstants/2076`
(Brazil, target_type=Country), um por grupo.

📌 O erro por trás do erro: a operação tinha o padrão que funcionava na frente
(o 1º lançamento, na mesma conta) e sobrepôs com "campanha é o lugar padrão da
geo no Google Ads". Para Search e Display é. Para Demand Gen não. **Quando a
conta já tem um objeto equivalente funcionando, ele manda — não a regra geral.**

## 7. A ausência de geo não aparece em lugar nenhum, e custa caro

Consequência prática do §6, medida nas duas primeiras semanas de captação do
2º lançamento:

| | Gasto no Brasil | Gasto fora |
|---|---:|---:|
| 1º lançamento, campanhas TESTE (com geo no grupo) | **100,0%** | 0,0% |
| 2º lançamento, bloco frio `[PF]` (sem geo) | 80,8% | **19,2%** |
| 2º lançamento, bloco quente `[PQ]` (com geo) | 94,7% | 5,3% |

**O vazamento somou ~15% do gasto desses dois blocos, em 146 países** —
Venezuela, Índia e Peru no topo, depois Bolívia, Colômbia, Indonésia,
Bangladesh, Paquistão, Argélia. Só **0,1%** foi pra país lusófono. Um vídeo em
português, de um nicho brasileiro, rodou na Índia.

E **nenhum dos dois lançamentos tinha critério de LANGUAGE** — zero, nos dois.
O que segurou o 1º lançamento no Brasil foi só a geo. Idioma seria cinto além do
suspensório; a geo é o suspensório.

📌 **Como isso passou 14 dias despercebido:** o campo simplesmente não existe.
`campaign_criterion` volta com `{'DEVICE': 4}` e `ad_group_criterion` volta sem
LOCATION — não há erro, alerta ou aviso. E o efeito no CPL parece problema de
criativo: o bloco frio marcava um CPL **2,5×** o do quente, o que levou a uma
conclusão errada ("público frio no Google é caro") quando a causa era
vazamento. Sem o vazamento o CPL do frio cai ~19% e fica ~5% abaixo do CPL de
equilíbrio do lançamento.

**Segunda ocorrência, no dia em que a receita do §0 foi executada:** a campanha
nova de mix quente, criada duplicando a `[ESCALA][PQ]` (§10) e mesmo assim sem
geo, porque a criação em cadeia parou antes do passo 7 e quem completou não
voltou nele. Em ~10h: **83% do gasto fora do Brasil**, CPM entre um quarto e um terço
do das irmãs, 3 conversões (1 no Brasil, 1 no México, 1 na Costa Rica). A
assinatura é sempre a mesma: **CPM muito abaixo das irmãs + CTR normal +
conversão quase zero = vazamento de geo, não criativo ruim.** A checagem abaixo
entra na conferência antes de ativar (config) e na leitura diária (efeito) —
§32.

**Checagem obrigatória, por EFEITO e não por campo** (regra da casa: escrita e
configuração se conferem pelo efeito, não pelo campo), antes de dar qualquer
campanha do Google como saudável:

```sql
SELECT campaign.name, user_location_view.country_criterion_id, metrics.cost_micros
FROM user_location_view WHERE campaign.name LIKE '%TAG%'
  AND segments.date BETWEEN 'X' AND 'Y'
```

Se o país 2076 (Brasil) não for ~100% do gasto, falta geo em algum grupo.

⚠️ **`DURING LAST_7_DAYS` EXCLUI o dia corrente** (UNIVERSAL). A checagem diária
do caso de origem montava a lista de campanhas "vivas" com esse intervalo, então
a campanha criada de madrugada — a única sem geo, com 83% do gasto fora do
Brasil — ficou fora de **todas** as checagens, e a leitura rodou limpa com o
problema no ar. Campanha nova é justamente a mais provável de estar mal
configurada: toda varredura de "o que está gastando" soma `DURING TODAY` ao
`LAST_7_DAYS`.

⚠️ A Meta **não** tem esse problema: `targeting.geo_locations.countries` vem
`['BR']` por padrão nos conjuntos, e o gasto medido por país deu 100,0% Brasil
em todo o gasto de Meta do 2º lançamento. Isto é armadilha só do Google.

### 7.1 Em lista de REMARKETING, a mesma ausência de geo dá dano ZERO

**VARIAÇÃO ISOLADA — 2º lançamento, medido na semana de aulas.** A checagem
diária acusou 6 grupos Display sem LOCATION (os momentos "gravação da aula 1",
"é hoje" da aula 2 e "gravação da aula 2"). Medido por país no mesmo período:
**0,0% do gasto fora do Brasil**.

| | Público | Fora do BR |
|---|---|---:|
| Campanha nova de mix quente (captação, §0) | captação fria | **83%** |
| Display remarketing (semana de aulas) | listas de inscritos e de envolvimento | **0%** |

**Por que:** sem geo, o Google serve pra quem couber na segmentação restante.
Em campanha fria a segmentação restante é o mundo. Em remarketing, a lista JÁ é
o limite — e a lista é de brasileiros. A geo vira redundante, não protetora.

📌 **O que isso NÃO autoriza:** dizer que falta de geo é inofensiva. Continua
sendo erro de criação e continua entrando na checagem — o risco é o molde se
propagar (aqui foi de 2 grupos pra 6 em um dia, conforme campanhas Display novas
foram saindo do mesmo modelo) e um dia esse molde ser usado em público aberto.
O que muda é a **classificação do achado**: em remarketing é dívida técnica a
corrigir na próxima criação, não sangria a estancar no meio do lançamento.

⚠️ **Decisão do Rodrigo: NÃO corrigir no meio da fase.** Editar segmentação de
campanha em veiculação reinicia aprendizado, e o Display estava entregando
clique a menos da metade do CPC que o Demand Gen da mesma conta pagava. Trocar
performance comprovada por um campo que não está causando dano não paga.
Corrigir na criação do próximo lançamento.

**Regra que fica:** ao achar geo ausente, medir o gasto por país ANTES de
classificar. Público fechado (Customer Match, engajamento, site) = medir e
provavelmente conviver; público aberto = estancar na hora.

⚠️ **Correção no dia seguinte — o geo NÃO estava ausente.** As 7 campanhas
Display do 2º lançamento são do tipo `DISPLAY` padrão (não Demand Gen), e nesse
tipo o geo mora na **campanha**: todas as 7 têm `campaign_criterion.location
= Brasil (2076)`. A checagem diária só lia LOCATION no **grupo** — regra que
vale pra Demand Gen, onde a campanha não aceita geo — e por isso acusou 6 grupos
num dia e 10 no seguinte que estavam certos. Os 0% fora do Brasil (cinco dias
medidos) se explicam pelo geo da campanha, não só pela lista. A checagem passou
a ler os dois níveis (conferido: nenhuma das 7 Demand Gen vivas tem geo na
campanha, então a vigilância delas não mudou). O que segue valendo da seção:
**medir por efeito antes de classificar** — foi isso que impediu o falso
positivo de virar edição em campanha no ar.

## 8. `contains_eu_political_advertising` virou obrigatório na criação

**Visto na 2ª semana de captação do 2º lançamento**, ao criar 5 campanhas Demand
Gen. Sem o campo, a criação falha inteira:

```
field_error: REQUIRED
message: "The required field was not present."
location { field_path_elements { field_name: "contains_eu_political_advertising" } }
```

É a regra de publicidade política da UE. Vale mesmo pra conta brasileira que
nunca vai anunciar política. Na criação de campanha:

```python
c.contains_eu_political_advertising = (
    client.enums.EuPoliticalAdvertisingStatusEnum
        .DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING)
```

📌 Campo novo que não existia nos objetos antigos da conta — ou seja, copiar a
estrutura de uma campanha existente **não** teria pego isso. É o inverso do
§6: lá o objeto antigo tinha a resposta, aqui ele não tem. Por isso o
`validate_only` (§4) é o que separa os dois casos — mas note que na criação em
cadeia ele só cobre o estágio que não depende de ID novo. Campanha, grupo e
anúncio referenciam IDs que ainda não existem, e por isso só são validados no
momento da escrita: **escreva estágio por estágio, do mais barato pro mais
caro, com o status nascendo PAUSED.** (A saída pra validar a cadeia inteira de
uma vez está no §30.)

## 9. Anúncio Demand Gen aceita 1 vídeo — 2 é escolha, não exigência

Testado a seco contra um grupo existente, sem criar nada:
`demand_gen_video_responsive_ad` com **1 vídeo** e com **2 vídeos**, os dois
ACEITOS. Os anúncios do **1º lançamento** usavam 2 no mesmo anúncio (asset "YT"
16:9 + asset "REELS" 9:16), o que parecia obrigatório e não é. *(Correção
posterior: a linha anterior dizia 2º lançamento; conferido campo a campo, as
`[ESCALA]` do 2º usam **1 vídeo por anúncio**, separadas em duas campanhas
`[YT]` e `[SHORTS]` — ver §13.)*

📌 Serve pra destravar subida quando falta um formato: sobe com o que tem, e
anexa o outro depois — `videos` é editável in-place (§5), sem recriar anúncio
nem perder o ID que o Dash usa pra casar o lead.

⚠️ **Cota do YouTube limita isso na prática:** upload pela Data API custa
~1.600 de 10.000 unidades/dia, ou seja ~6 vídeos por dia. Upload manual pelo
youtube.com **não** consome cota nenhuma — quando a cota travar e houver
pressa, subir à mão e só referenciar o ID pela API é o caminho.

📌 **O caminho do sistema é outro: a própria API do Google Ads sobe o vídeo.** É o
comando `videos` de `sirius-scale/ferramentas/google/subir_campanha.py`
(`YouTubeVideoUploadService`), com as credenciais de sempre. Sem canal informado, o vídeo
vai pra um canal gerenciado pelo Google, ligado à conta (ele aparece como "Video ad upload
channel for" + o número da conta), e só pode ser não listado. O id só existe depois que o
estado chega em `PROCESSED`. A cota acima é da Data API do YouTube, que pede token por canal;
e, pela documentação do YouTube, projeto do Google Cloud criado depois de julho de 2020 e sem
auditoria tem o vídeo restrito a privado por esse caminho. *VARIAÇÃO ISOLADA: um vídeo de
teste no caso de origem, subido, lido de volta, aceito a seco como asset e apagado.*

## 10. Campanha nova nasce dos DEFAULTS da conta — duplicar a referência, nunca criar do zero

**Medido no 2º lançamento, na 3ª semana de captação.** Consultando
`campaign_conversion_goal.biddable` (o campo certo, ver §2) nas campanhas de
captação do MESMO lançamento, apareceram **três configurações diferentes**,
conforme a data em que cada uma foi criada:

| Campanhas | Metas com `biddable=True` |
|---|---|
| `[ESCALA]` YT e Shorts | **só `SUBMIT_LEAD_FORM`** ✅ |
| três campanhas de criativo de uma leva anterior (uma delas consolidada) | `DOWNLOAD` + `SUBMIT_LEAD_FORM` |
| quatro campanhas de criativo criadas dois dias antes da medição | `PURCHASE`, `PAGE_VIEW`, `DOWNLOAD`, `BEGIN_CHECKOUT`, `CONTACT` + `SUBMIT_LEAD_FORM` |

Ninguém decidiu nenhuma das três. Cada campanha herdou o **default da conta no
momento da criação**, e o default mudou ao longo do lançamento (ações de conversão
novas entram como principais). O efeito prático: os quatro criativos mais novos
passaram a semana dando lance por **visualização de página e compra** em vez de
lead — e o custo por MQL alto deles **não mede o criativo**, mede a configuração
errada.

A mesma deriva atingiu a estratégia de lance: as `[TESTE]` foram corrigidas pra
`TARGET_CPA` (com o alvo de CPA do lançamento, o mesmo do 1º lançamento) na 2ª
semana de captação, e as duas `[ESCALA]` ficaram em `MAXIMIZE_CONVERSIONS` sem
teto porque a correção não cobriu todas.

📌 **Regra (decisão do Rodrigo): campanha nova durante um lançamento se cria
DUPLICANDO a campanha mais parecida que já está funcionando — nunca do zero.**
Criar do zero é aceitar em silêncio o default da plataforma naquele dia, e o
default nem é estável dentro do mesmo lançamento.

Nem o Google nem a Meta têm "duplicar" na API: duplicar significa **ler a
configuração completa da campanha de referência e replicar campo a campo**. O que
precisa vir junto, no mínimo:

- `bidding_strategy_type` e o teto (`target_cpa` / `maximize_conversions.target_cpa_micros`)
- `campaign_conversion_goal` — todas as categorias, com `biddable` explícito (§2)
- `ad_group.optimized_targeting_enabled` (a "segmentação automática", equivalente
  do Advantage+ — ver `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.6)
- públicos anexados, geo (§6 e §7), e os campos obrigatórios da §8

⚠️ **Duplicar não dispensa conferir.** As duas plataformas descontinuam campo sem
removê-lo dos objetos antigos, então uma campanha antiga pode carregar um campo
que hoje quebra a criação. O ciclo completo é **duplicar → comparar campo a
campo com a referência → `validate_only` (§4) → escrever**. Duplicar reduz o que
você precisa lembrar de setar; não elimina a conferência.

📌 **E vale como diagnóstico:** quando o custo subir sem causa aparente, comparar
`campaign_conversion_goal` e `bidding_strategy_type` campanha a campanha **dentro
do mesmo lançamento** — não só contra o lançamento anterior. Configuração
divergente entre irmãs é sinal de deriva de default, e foi assim que isto apareceu.

⚠️ **"Irmã" é da mesma FASE, não qualquer campanha que esteja funcionando** ·
*VARIAÇÃO ISOLADA*. Divergência de lance entre `[TESTE]` e `[ESCALA]` pode ser
desenho, não deriva: teste controla custo com teto, escala tira o teto pra
ganhar volume. O §10 acima registra que as `[TESTE]` foram corrigidas pra
`TARGET_CPA` e as `[ESCALA]` ficaram em `MAXIMIZE_CONVERSIONS` — e **não diz
qual das duas é a intenção**.

O que isso custou: no dia seguinte à receita do §0, a campanha nova de mix
quente (uma `[TESTE]`) foi comparada contra a `[ESCALA][PQ]` YT, o FAIL de lance
foi tratado como config errada, e o lance foi trocado pra `MAXIMIZE_CONVERSIONS`.
A `[TESTE]` irmã (um criativo consolidado da etapa de teste) estava em
`TARGET_CPA` o tempo todo — o estado original já era o consistente. Revertido no
mesmo dia, com **dois resets de aprendizado em duas horas**.

**Ao conferir contra a referência, escolha a referência pela fase e pela etapa
do nome** (`[TESTE]` com `[TESTE]`, `[ESCALA]` com `[ESCALA]`). Se não existir
irmã da mesma fase, isso é a informação — diga que não há base de comparação
pra lance, em vez de usar a de outra fase e tratar a diferença como erro.

## 11. Demand Gen novo recusa `user_list` solto — exige `Audience` agrupada

**Visto no dia da receita do §0**, ao duplicar a `[ESCALA][PQ]` (§10). A campanha
de referência tem 12 `ad_group_criterion.user_list` anexados um a um. Replicar
isso numa campanha nova falha:

```
criterion_error: CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET
"Audience segment attachment is not allowed when use audience grouped bit is set to true."
```

Campanha Demand Gen criada hoje nasce com "audience grouped" ligado. O caminho é
criar um recurso `Audience` com os segmentos dentro e anexar **esse** ao grupo:

```python
op = client.get_type("AudienceOperation")
d = client.get_type("AudienceDimension")
for lid in listas:
    seg = client.get_type("AudienceSegment")
    seg.user_list.user_list = f"customers/{CID}/userLists/{lid}"
    d.audience_segments.segments.append(seg)
op.create.dimensions.append(d)
# depois: ad_group_criterion.audience.audience = <resource_name da Audience>
```

⚠️ **Ao copiar as listas da referência, copie o flag `negative` junto.** A
campanha nova de mix quente recebeu "as 12 listas" da campanha de mix quente de
referência — só que 3 delas eram **exclusão** na referência (visita à página de
captura do lançamento, visita à página de obrigado do lançamento e quem viu os
vídeos dos anúncios nos últimos 30 dias) e entraram como **inclusão**: a
campanha passou o dia pagando pra mostrar anúncio de inscrição a 2.500 pessoas
que já tinham se inscrito. O listing de `ad_group_criterion` devolve positivos e
negativos misturados; quem lê só o ID não vê a diferença. A mesma coisa vale pra
faixa etária: o grupo quente da referência tem 25–44 positivas e as outras 5
**negativas** — copiar só as positivas abre a idade inteira. Desde então a
conferência antes de ativar compara os negativos e a idade contra o grupo
equivalente da referência (§32).

**Consequência, medida a seco ao corrigir a campanha nova:** num grupo "audience
grouped" a segmentação inteira mora no recurso `Audience`, e o que o listing de
`ad_group_criterion` devolve é **projeção somente-leitura**:

| Tentativa | Resposta |
|---|---|
| Remover `USER_LIST` ou `AGE_RANGE` positivo do grupo | `MUTATE_NOT_ALLOWED` |
| Criar `AGE_RANGE` negativo no grupo | `OPERATION_NOT_PERMITTED_FOR_CONTEXT` |
| Criar `USER_LIST` negativo no grupo | `CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET` |
| Criar `USER_LIST` negativo na campanha | `CANNOT_EXCLUDE_CRITERION` |
| **`AudienceOperation.update` em `dimensions`** (listas + `age` com `age_ranges` e `include_undetermined`) | ✅ e a projeção do grupo muda junto |
| **`AudienceOperation.update` em `exclusion_dimension.exclusions`** (só aceita `user_list`) | ✅ — máscara tem que ser o subcampo; `exclusion_dimension` sozinho dá `FIELD_HAS_SUBFIELDS` |

Ou seja: **incluir, excluir e restringir demografia é tudo edição da Audience**,
in-place, sem tocar em critério do grupo. Grupo criado pela interface antes
disso (as `[ESCALA]` do 2º lançamento, o 1º lançamento) ainda aceita critério
negativo solto — por isso a referência "funciona" e a cópia campo a campo não.

✅ **Confirmado depois num caso diferente: trocar o público de uma campanha JÁ
EM ANDAMENTO.** O grupo de envolvimento curto + base do aquecimento do 2º
lançamento — criado por script na 1ª semana de captação, não pela interface —
também nasce com `use_audience_grouped = True`, e devolveu os mesmos dois erros
da tabela acima ao tentar remover as `user_list` do grupo. Funcionou pelo
`AudienceOperation.update` em `dimensions`, exatamente como registrado — agora
pro caso "trocar a lista inteira de uma vez".

📌 Isto **não** é regra nova — é a mesma linha da tabela, cobrada de novo. O
que a repetição mostra é que a divisão não é "interface x script", e sim
**a data em que o grupo nasceu**: qualquer grupo Demand Gen recente é
grouped, tenha sido criado por onde for. E vale o registro de processo: este
erro foi cometido de novo porque o arquivo não foi aberto antes de escrever o
código — o custo foi uma tentativa perdida, e é exatamente o gargalo que o
`/pente-fino` no modo consulta existe pra fechar (abrir o que já está escrito
antes de agir).

📌 **É o §10 mordendo a própria cauda:** duplicar é a regra certa, e mesmo assim a
estrutura antiga não é replicável campo a campo, porque a plataforma mudou o
mecanismo entre a criação da referência e hoje. Duplicar reduz o risco; não zera.

⚠️ **Armadilha de proto-plus, custou duas rodadas:** campo repetido da SDK **não
tem `.add()`**. `d.headlines.add().text = x` estoura
`'RepeatedComposite' object has no attribute 'add'`. Constrói o objeto com
`client.get_type("AdTextAsset")` e usa `.append(obj)`.

## 12. Estrutura do `DEMAND_GEN_VIDEO_RESPONSIVE_AD`

Levantada da campanha de escala de público quente no YouTube do 2º lançamento
(`[YT][<TAG>][CAPTACAO][ESCALA][PQ]`) e usada pra criar 5 anúncios.

| Campo | Tipo | O que a referência usa |
|---|---|---|
| `business_name` | `AdTextAsset` | 1 |
| `headlines` | `AdTextAsset[]` | 5 |
| `long_headlines` | `AdTextAsset[]` | 3 |
| `descriptions` | `AdTextAsset[]` | 3 |
| `videos` | `AdVideoAsset[]` | 1 (§9: 2 é escolha, não exigência) |
| `logo_images` | `AdImageAsset[]` | 1 |
| `call_to_actions` | `AdCallToActionAsset[]` | 1 |

`final_urls` fica no **anúncio**, não no asset, e leva as UTMs (desde a captação
de uma Black, a UTM do Google foi pro sufixo: §31).

### 12.1 Mínimos e obrigatoriedade — MEDIDO com `validate_only`

`VARIAÇÃO ISOLADA` — sondado na conta do caso-base, criando as 14 campanhas de
remarketing do 2º lançamento. A sonda mandou combinações contra um grupo real e
leu o que a API recusa:

| Campo | Mínimo real | Observação |
|---|---|---|
| `headlines` | **1** | a referência usa 5, mas 1 passa |
| `long_headlines` | **1** | a referência usa 3 |
| `descriptions` | **1** | a referência usa 3 |
| `logo_images` | **1 — OBRIGATÓRIO** | sem ele: `collection_size_error: TOO_FEW` |
| `call_to_actions` | **0 — opcional** | passou sem |

⚠️ **`AdCallToActionAsset` não tem campo de enum.** O único campo é `asset`, e
ele aponta pra um asset de CTA que já existe na conta (leia o id do asset de
CTA da própria conta antes, ex.: o `LEARN_MORE`). `c.call_to_action =
"LEARN_MORE"` levanta `AttributeError: Unknown field` antes mesmo de sair da
máquina.

⚠️ **Limites de caractere seguem NÃO confirmados no teto.** 40 (headline) e 90
(long headline e description) passaram de novo — é o que cabe, não o teto.
Quem precisar do teto real descobre com `validate_only` (§4) e registra.

📌 **O que fazer com isso:** mínimo 1 não é permissão pra mandar 1. Menos
variação é menos material pro Google combinar. Vale saber o mínimo porque copy
derivada de peça aprovada nem sempre rende 5 headlines — e aí a escolha é entre
mandar menos variação ou **inventar copy**, que `sirius-scale/REGRAS.md` §2 e
§3 proíbem. Nas 14 do 2º lançamento saíram de 2 a 4 headlines por peça, todas
frases inteiras da legenda que o Rodrigo já tinha aprovado.

⚠️ **Campo repetido de proto-plus não tem `.add()`** — ver §11. Vale pra todos os
`AdTextAsset`/`AdVideoAsset`/`AdImageAsset` desta tabela.

## 13. Formato vertical + horizontal: no 1º lançamento iam no MESMO anúncio, no 2º foram separados em duas campanhas

**Conferido campo a campo** (a pedido do Rodrigo, que lembrava do 1º lançamento
"com Shorts e YouTube na mesma campanha").

| | 1º lançamento (captação, campeãs) | 2º lançamento `[ESCALA]` | 2º lançamento, mix quente novo (§0) |
|---|---|---|---|
| Campanhas por criativo/público | **1** | **2** (`[YT]` e `[SHORTS]`) | 1 |
| Vídeos por anúncio | **2** (YT 16:9 + REELS 9:16) | 1 | 1 (só 16:9) |
| Lance | `TARGET_CPA` no **alvo de CPA** do lançamento | `MAXIMIZE_CONVERSIONS` sem teto | `MAXIMIZE_CONVERSIONS` sem teto |
| Rede: content (Discover/Gmail) | ligada | ligada | **desligada** |
| Headlines / long / desc | 5 / 5 / 5 | 5 / 3 / 3 | 5 / 5 / 5 (um dos criativos: 2 / 2 / 2) |
| Geo no grupo | Brasil | Brasil | **nenhuma nas primeiras ~10h** |
| Segmentação otimizada | ligada | ligada | ligada |
| Metas biddable | só `SUBMIT_LEAD_FORM` | só `SUBMIT_LEAD_FORM` | só `SUBMIT_LEAD_FORM` |

**Fato de plataforma (UNIVERSAL):** num `DEMAND_GEN_VIDEO_RESPONSIVE_AD`, o
vídeo vertical no campo `videos` é o que habilita o posicionamento Shorts; o
horizontal cobre in-stream/in-feed. Um anúncio com os dois formatos concorre nos
dois inventários com o **mesmo sinal de conversão** — dividir em duas campanhas
divide o sinal (mesma mecânica do
`sirius-scale/frameworks/trafego/lancamento-gratuito.md` §2.4: Demand Gen
aprende por campanha). `videos` é editável in-place (§5), então dá pra anexar o
vertical num anúncio que já roda sem perder o ID.

**Sobre performance (VARIAÇÃO ISOLADA, 1 cliente, 2 lançamentos, com outras
variáveis mudando junto — lance e público):** as 3 campeãs do 1º lançamento, com
2 formatos e tCPA, fizeram CPA de plataforma entre ~0,4× e ~0,6× o alvo de CPA,
e CPA real no Dash entre ~0,55× e ~0,85× o alvo; as mesmas 3 no 2º lançamento,
com 1 formato e sem tCPA, ficaram entre ~1,4× e ~1,6× o alvo nas `[TESTE]` e em
~0,75× (YT) / ~0,86× (Shorts) nas `[ESCALA]`. Não dá pra atribuir a diferença só
ao formato — mas a estrutura do 1º lançamento é a que tem resultado comprovado,
e é a que se replica por padrão (§10).

📌 **Regra de criação daqui em diante:** anúncio Demand Gen de captação nasce com
os **2 formatos no mesmo anúncio**, na **mesma campanha** (o `[YT]` da
nomenclatura passa a significar "YouTube, todos os posicionamentos"; `[SHORTS]`
fica pra campanha que tem só vertical de propósito). Faltou o vertical? Sobe com
o horizontal e anexa depois (§9) — mas a conferência antes de ativar avisa
(§32).

## 14. Demand Gen não tem ABO: o orçamento só existe na campanha

`VARIAÇÃO ISOLADA` — 2º lançamento, remarketing da semana de aulas.

O Rodrigo desenhou o remarketing com **orçamento no conjunto** (ABO), pra dar
peso maior ao público de inscritos e peso menor ao de envolvimento curto:

> "Nesse cenário o orçamento deve estar em nível de conjunto de anúncios e não
> na campanha" (Rodrigo)

Na Meta isso é uma flag. **No Demand Gen não existe**: `campaign_budget` é da
campanha, e o grupo não tem orçamento próprio. Só há duas saídas, e as duas
custam algo:

| Saída | O que custa |
|---|---|
| 2 grupos numa campanha | perde o controle de peso — quem divide é o Google |
| 1 campanha por público | dobra a contagem e **cada uma paga o piso do §1** |

No 2º lançamento a segunda era inviável por aritmética, não por preferência:
28 campanhas × o piso do §1 dariam **quase 1,5× a verba diária da fase inteira
só de piso**. Ficou 2 grupos por campanha, e a diferença de peso entre Meta e
Google foi dita ao cliente em vez de escondida.

📌 **A regra que fica:** diretriz de estrutura vinda da Meta não se traduz
sozinha pro Google. Quando não traduzir, dizer qual foi a perda — e, se a saída
alternativa foi descartada por custo, mostrar a conta. A conta vai no plano,
antes de pedir confirmação, pra decisão não depender de alguém lembrar de
explicar.

## 15. Conferir contra referência de OUTRA FASE gera FAIL que é desenho

`VARIAÇÃO ISOLADA`.

A conferência compara a campanha nova contra uma referência que funciona. No 2º
lançamento não existia remarketing anterior no Google — é a primeira vez —
então a referência disponível era a campanha de **aquecimento**. As 14
campanhas novas deram **70 FAIL**, todos em 3 categorias, e **nenhum era
defeito**:

| FAIL | Quantos | Por que é desenho |
|---|---|---|
| `metas biddable` diferentes | 14 | decisão do §2: aquecimento otimiza `ENGAGEMENT`, remarketing não |
| `listas de EXCLUSÃO` presentes | 28 | o cliente pediu excluir os alunos do programa principal; a referência não exclui |
| `politica UNKNOWN` | 28 | `REVIEW_IN_PROGRESS` — anúncio recém-criado, o Google ainda revisa |

⚠️ **Isso não torna a conferência inútil — torna a leitura dela um trabalho.**
O valor está em *"FAIL fora das categorias conhecidas: 0"*. Classificar cada
FAIL contra a decisão que o gerou é o passo que não dá pra pular, e é o mesmo
erro que já custou dois resets de aprendizado quando se comparou `[TESTE]` com
`[ESCALA]` (§10: comparar sempre contra irmã da mesma fase).

📌 A categoria `politica UNKNOWN` é a única **temporária**: some quando o
Google termina a revisão. Ela precisa ser reconferida antes de ativar — anúncio
reprovado que ativa não entrega, e a leitura diária só pega isso depois que já
gastou.

**Quanto a revisão demora. VARIAÇÃO ISOLADA.** Dois anúncios Demand Gen novos,
cada um na sua campanha de teste, criados pausados num domingo à tarde, saíram
da análise uns 35 minutos depois. Um voltou `APPROVED_LIMITED`, o mesmo estado
que ele já tinha na campanha principal: o criativo reaproveitado traz a
restrição junto. Logo depois de ligar, a campanha do outro aparecia `PENDING` /
`MOST_ADS_UNDER_REVIEW` com o anúncio já `APPROVED`. O que prova a entrega é o
custo por `segments.date`, nunca o status (§22).

## 16. Datas de campanha: nome novo, e o Google não tem janela por hora

`CONSISTENTE` (fato de plataforma) — medido com `validate_only`.

**O nome do campo mudou.** Na v25 é `start_date_time` / `end_date_time`:

```
SELECT campaign.start_date, campaign.end_date
  → query_error: UNRECOGNIZED_FIELD
```

O nome antigo (`start_date`/`end_date`) ainda aparece em tutorial e em código
de exemplo espalhado, então é fácil copiar errado.

**E há três regras que só aparecem no `validate_only`:**

| Erro | O que significa |
|---|---|
| `DATE_RANGE_ERROR_START_TIME_MUST_BE_THE_START_OF_A_DAY` | início só `00:00:00` |
| `DATE_RANGE_ERROR_END_TIME_MUST_BE_THE_END_OF_A_DAY` | fim só `23:59:59` |
| `CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED` | depois de começar, o início não se mexe |

🔴 **CORREÇÃO — o que estava escrito aqui de manhã estava errado.** A primeira
versão desta seção dizia *"o Google não faz janela por hora"*. Isso vale só pro
par `start_date_time`/`end_date_time`. **`campaign_criterion.ad_schedule` faz
janela por hora**, e os minutos aceitam `ZERO`, `FIFTEEN`, `THIRTY` e
`FORTY_FIVE` — então 20:30 é perfeitamente possível. Testado com `validate_only`
e aplicado nas 14 campanhas de remarketing do 2º lançamento, com leitura de
volta.

```python
o = cli.get_type("CampaignCriterionOperation")
o.create.campaign = rn_camp
s = o.create.ad_schedule
s.day_of_week  = cli.enums.DayOfWeekEnum.MONDAY
s.start_hour   = 0;  s.start_minute = cli.enums.MinuteOfHourEnum.ZERO
s.end_hour     = 20; s.end_minute   = cli.enums.MinuteOfHourEnum.THIRTY
```

📌 **E isso destrava o problema do `start_date_time` que não se altera.** Com
schedule, a campanha pode ficar `ENABLED` fora da faixa **sem gastar** — então
dá pra ligar tudo de uma vez e cada momento entra sozinho na hora dele. Era o
que faltava: sem schedule, a ativação era o único controle de início, e ligar a
campanha do "é hoje" da aula 2 na segunda a faria anunciar "a aula 2 é HOJE"
por três dias.

No 2º lançamento ficou assim, nas 14:

| Momento | Faixa |
|---|---|
| "é hoje" de cada aula | dia da aula, 00:00 → **20:30** (para sozinha quando a aula começa) |
| gravação de cada aula | dia da aula **21:00** → 24:00, depois dia inteiro até o fim |
| todas as aulas liberadas | sex/sáb/dom, dia inteiro |

⚠️ O que continua valendo do parágrafo original: `end_date_time` **só** aceita
`23:59:59` e `start_date_time` não se altera depois que a campanha começou. O
schedule é a camada que resolve a hora; a data continua sendo de dia inteiro.
E a pausa manual às 20:30 **deixou de ser necessária** — pausar na hora vira
rede de segurança, não rotina.

⚠️ **Campanha criada sem `end_date_time` roda pra sempre.** As 14 do 2º
lançamento nasceram assim, e só apareceu porque alguém foi conferir: no caso de
origem, criar a campanha e setar a data eram dois passos separados, e só os dois
juntos fecham a campanha — conferir `end_date_time` na leitura de volta (§32).
Como o início não se altera depois, **quem controla o começo de verdade é a
ativação**: a campanha sai do PAUSED no dia dela.

**Tirar o fim de uma campanha que já tem fim** (*VARIAÇÃO ISOLADA*, validado a seco
e lido de volta): `end_date_time = "2037-12-30 23:59:59"`, que é o "sem fim" da API
pra campanha que já existe (apagar o campo não funciona). A janela por hora
(`ad_schedule`) sai à parte, com `CampaignCriterionOperation.remove` em cada
critério. Tirar as janelas antes do fim: a campanha volta a entregar no instante em
que o fim muda. Ela continua ENABLED o tempo todo; quem segurava a entrega era o fim
vencido (§22).

## 17. `POLITICAL_ADS_RESTRICTIONS_IN_BRAZIL` pega criativo de concurso público

`VARIAÇÃO ISOLADA` — 2º lançamento, semana de aulas.

Dos 28 anúncios criados, 26 foram aprovados e **2 reprovados**, os dois da
campanha do "é hoje" da aula 2 no YouTube:

```
approval_status = DISAPPROVED
topic = POLITICAL_ADS_RESTRICTIONS_IN_BRAZIL
type  = FULLY_LIMITED          → não veicula
```

**O que descarta as explicações fáceis:**

- A copy não tem nada eleitoral: o texto era do molde *"os [N pilares] que você
  precisa [desenvolver] pra conquistar a sua aprovação"*, mais temas da própria
  matéria.
- **O Shorts da mesma peça, com o texto idêntico, foi APROVADO.** Só mudou o
  vídeo (16x9 vs 9x16), então não é o texto.

Duas hipóteses vivas, e a diferença importa: ou o classificador reagiu ao
conteúdo do vídeo 16x9, ou é ruído — anúncios equivalentes podem ter destinos
diferentes na revisão automática. O ano era eleitoral no Brasil e o filtro
estava agressivo; num nicho de concurso, "aprovação" tem duplo sentido em
português.

⚠️ **NÃO EXISTE APPEAL POR API.** Procurado na v25: `AdGroupAdOperation` tem
`policy_validation_parameter`, mas ele só serve **na criação** (pra ignorar
tópicos já isentos), não pra contestar reprovação. Não há
`AppealService`/`PolicyReviewService`. O caminho é a interface do Google Ads,
recriar o anúncio, ou trocar o vídeo.

📌 **O que fica pro próximo lançamento:** conferir `policy_summary` **por
anúncio** depois da revisão terminar, não por amostra. Neste caso a primeira
query olhou só o grupo `00` e reportou *1* reprovado; eram *2* — o mesmo
anúncio existe nos dois grupos. Amostra em conferência de política esconde
metade do problema.

## 18. Display recusa Customer Match — e isso derruba a exclusão de compradores

`CONSISTENTE` (política de plataforma) — medido com `validate_only`, lista por
lista.

```
user_list CRM_BASED  → "Targeting is not allowed for Customer Match lists
                        as per Customer Match policy"
user_list RULE_BASED → OK
```

Na campanha de Display do 2º lançamento isso tirou **duas** coisas:

1. A lista CRM de inscritos do lançamento ficou fora do grupo 00 — sobraram as
   listas por regra de visita à página de obrigado e às páginas das aulas.
2. **A exclusão dos alunos do programa principal virou impossível**, porque a
   lista de alunos também é CRM. No Demand Gen ela está aplicada; no Display não
   há como.

📌 **A consequência não é técnica, é de verba:** quem já comprou vê o anúncio e
gasta clique. Em peça de aula gratuita o dano é pequeno (não é mensagem errada,
é público errado); em peça de **venda** seria caro. Antes de rodar Display na
fase de carrinho, criar uma lista **rule-based** equivalente — quem visitou a
área de membros, por exemplo — porque a CRM não serve nesse canal.

## 19. Estático e vídeo cabem na MESMA campanha Demand Gen

`VARIAÇÃO ISOLADA` — medido no 2º lançamento.

O tipo é **`demand_gen_multi_asset_ad`** (não `demand_gen_multi_asset_responsive_ad`,
que não existe e levanta `AttributeError`). Ele convive com o
`demand_gen_video_responsive_ad` **no mesmo grupo de anúncios**, então não é
preciso separar canal pra ter as duas mídias.

Exige `marketing_images` (1.91:1) **e** `square_marketing_images` (1:1) — com só
uma das duas, a API devolve `media_upload_error: ASPECT_RATIO_NOT_ALLOWED`, e a
mensagem fala de aspect ratio sem dizer que o problema é a **falta do outro
formato**.

📌 **O que isso resolve:** a pergunta "preciso de 3 campanhas por momento (YT,
Shorts, Display)?" tem resposta **não**. YouTube in-stream/in-feed, Shorts,
Discover, Gmail e estático cabem numa campanha Demand Gen só. Campanha separada
mesmo, só a **rede de Display** (sites parceiros), que é `AdvertisingChannelType.DISPLAY`.

## 20. `APPROVED_LIMITED` não é `DISAPPROVED` — e o ativador precisa saber a diferença

`CONSISTENTE`.

| Estado | Entrega? | O que fazer |
|---|---|---|
| `DISAPPROVED` | **não** | bloqueia ativação — orçar sem entregar |
| `APPROVED_LIMITED` | **sim, restrito** | avisa; o `sirius-scale/frameworks/copy/criativos.md` §0.10 mediu 2,4x no CPV |
| `UNKNOWN` / `REVIEW_IN_PROGRESS` | ainda não | esperar antes de julgar |

⚠️ **E a query da trava tem que filtrar `status != 'REMOVED'`.** A trava antes
de ativar do caso de origem barrou uma campanha saudável porque contava dois
anúncios **já apagados** — os reprovados que tinham sido removidos na correção.
Trava que lê lixo é trava que impede operação legítima, e o custo disso é a
pessoa aprender a ignorar o bloqueio.

📌 **Caso medido de recriação:** os 2 anúncios `DISAPPROVED` /
`POLITICAL_ADS_RESTRICTIONS_IN_BRAZIL` / `FULLY_LIMITED` do "é hoje" da aula 2
foram recriados com ID novo (editar in-place não dispara revisão,
`sirius-scale/frameworks/copy/criativos.md` §0.10). Resultado: subiram para
**`APPROVED_LIMITED`** — melhorou, não limpou. Os anúncios **estáticos** criados
no mesmo grupo, com a mesma copy e o mesmo destino, saíram **`APPROVED`**
limpos. Isso isola a causa no **vídeo 16:9**, não na copy nem na página de
destino.

## 21. `manual_cpc` sem lance no grupo entrega ZERO, e a API não avisa

`CONSISTENTE` (fato de plataforma) — custou um dia de Display.

As 7 campanhas de Display do 2º lançamento foram criadas com `manual_cpc` na
campanha e **sem `ad_group.cpc_bid_micros`**. O Google preencheu com o mínimo,
**um centavo** (`cpc_bid_micros = 10000`), e com um centavo de lance não se
ganha leilão nenhum.

**O sintoma é mudo em todos os lugares onde se costuma olhar:**

```
campaign.serving_status  = SERVING
campaign.primary_status  = ELIGIBLE
primary_status_reasons   = []          ← nenhum aviso
metrics.cost_micros      = 0           ← só isto denuncia
```

Anúncios aprovados, geo certa, público anexado, horário certo, orçamento certo.
Nada acusa. Quem percebeu foi o Rodrigo, olhando que o gasto não saía do zero.

📌 **A regra: estratégia manual precisa de DUAS escritas.** A estratégia vai na
campanha, o lance vai no **grupo** — uma sem a outra entrega zero em silêncio.
Estratégia automática (`maximize_conversions`, `target_cpa`) não tem esse
problema, porque o lance é a própria estratégia. Foi exatamente por isso que, no
mesmo dia e na mesma conta, o Demand Gen entregou normalmente e o Display, zero.

⚠️ **Ancorar o lance em dado da conta, não em chute.** Aqui o lance ficou ~12%
abaixo do CPC médio que o Demand Gen desta conta pagou nos 30 dias anteriores
(medido sobre dezenas de milhares de cliques). Não havia histórico de Display
pra usar; o CPC do Demand Gen é a referência mais próxima, e Display costuma
sair abaixo.

✅ **Checagem que fica:** campanha com `bidding_strategy_type = MANUAL_CPC` e
algum grupo com `cpc_bid_micros <= 10000` (um centavo) é candidata a entrega
zero. É calculável, então entra na conferência antes de ativar e na leitura
diária (§32) — com a régua de só apontar o que gastou (ou deveria ter gastado)
nos últimos 7 dias ou hoje: checagem que lista a conta inteira enterra o que
importa e ninguém lê.

## 22. `ad_schedule` funciona — medido na entrega, não só na configuração

`VARIAÇÃO ISOLADA` — 2º lançamento, dia da Aula 1.

O §16 registra que o `ad_schedule` aceita janela por hora. Isto aqui é a
confirmação pelo **efeito**, que é o que a regra da casa de conferir pelo efeito
exige — ler o campo de volta prova que gravou, não que funciona.

Gasto por hora do dia da Aula 1, com `segments.hour`:

| Campanha | Faixa configurada | Gastou às |
|---|---|---|
| "é hoje" da aula 1 | seg 00:00 → **20:30** | 12h e 13h · **zero das 21h em diante** |
| gravação da aula 1 | seg **21:00** → 24:00 | **21h** |

A "é hoje" parou sozinha antes da aula começar, e a gravação entrou depois da
transmissão — sem ninguém pausar nada. Isso encerra a necessidade da pausa
manual às 20:30 que o §16 previa como paliativo.

📌 `segments.hour` é a forma de conferir schedule. Sem ele, o total do dia
esconde a distribuição, e uma campanha que entregou toda no horário errado
parece idêntica a uma que respeitou a faixa.

**Confirmado que vale pro Display também (no dia da aula 3).** As 7 campanhas
Display do 2º lançamento (criadas depois das 14 originais) nasceram com o mesmo
`ad_schedule` — o "é hoje" da aula 3 roda quinta 00:00→20:30, igual ao par
YT/Shorts. E `end_date_time` também já corta sozinho: as campanhas do "é hoje"
das aulas 1 e 2 (YT e Display, as 4) tiveram custo e impressão **zerados no dia
seguinte ao fim**, com `status` ainda `ENABLED` — o campo não muda, a entrega
para.

⚠️ **Erro que isso corrigiu, registrado pra não repetir:** a leitura do
remarketing pegou `status=ENABLED` + `end_date_time` vencido e reportou ao
Rodrigo, duas vezes num mesmo dia, que campanhas vencidas "continuavam gastando"
— sem medir gasto por dia, e sem ter lido este próprio §22 antes (o framework já
respondia e ninguém consultou). O Rodrigo corrigiu perguntando "você mesmo
programou o fim, não é óbvio que já parou?". A checagem certa da higiene de
janela é **gasto por dia após o fim**, nunca `status` (regra da casa: conferir
pelo efeito, não pelo campo).

## §23 — Demand Gen com estático GERA vídeo sozinho — *VARIAÇÃO ISOLADA*

*(medido entre a carta de vendas e o 1º dia de carrinho do 2º lançamento)*

Anúncio `demand_gen_multi_asset_ad` (só imagem) faz o Google criar, **horas
depois e sem pedir**, um `demand_gen_video_responsive_ad` no mesmo grupo,
chamado "Annuncio video generato automaticamente (<nome do estático>)": a arte
animada sobre um fundo cinza-claro genérico, 3–5 vídeos por grupo, ENABLED e
APPROVED. `campaign.asset_automation_settings` volta vazio (= opt-in por
padrão). Ele **não aparece** na criação nem no resumo de ativação — só na
leitura de volta feita depois.

Medido: na campanha da carta de vendas, os automáticos levaram **64% do
gasto** com CPC de ~metade do estático (entram no in-stream do YouTube, onde
imagem não vai). No carrinho, no primeiro dia, CPC ~2× o do estático (24
cliques — cedo). Decisão do Rodrigo: **deixar rodar** ("se é um recurso podemos
deixar"), com o preço de a marca aparecer em fundo claro.

O que fazer ao criar Demand Gen estático: (1) saber que ele vai existir;
(2) reler os anúncios do grupo algumas horas depois (`ad_group_ad.ad.type`);
(3) decidir por campanha — pausar os automáticos (os nomes são os do estático,
entre parênteses) ou deixar — e ler o CPC por tipo de anúncio na leitura
diária, nunca a campanha inteira somada.

## §24 — v25 renomeou as métricas de vídeo: `video_views` virou `video_trueview_views` — *UNIVERSAL*

*(medido com a SDK google-ads 31.4 / API v25, no debriefing da distribuição de
conteúdo)*

```
SELECT metrics.video_views, metrics.video_view_rate, metrics.average_cpv ...
  → query_error: UNRECOGNIZED_FIELD
```

| antes | v25 |
|---|---|
| `metrics.video_views` | `metrics.video_trueview_views` |
| `metrics.video_view_rate` | `metrics.video_trueview_view_rate` (+ `_in_feed`, `_in_stream`, `_shorts`) |
| `metrics.average_cpv` | **não existe** — custo ÷ `video_trueview_views` |
| `campaign.start_date` / `end_date` | `start_date_time` / `end_date_time` (já no §16 — e o nome velho foi usado de novo depois) |

Lista completa sai do `GoogleAdsFieldService`
(`SELECT name, selectable WHERE name LIKE 'metrics.video%'`) — é o jeito de
conferir nome de campo antes de escrever query nova, em vez de chutar pelo
tutorial.

🔴 **Isso corrige uma conclusão anterior** (de uma leitura das lives de
aquecimento): "Demand Gen NÃO expõe `metrics.video_views` nem `average_cpv`".
Não era a Demand Gen — era o nome. Com `video_trueview_views` a Demand Gen
devolve views normalmente (a campanha de distribuição de conteúdo em Shorts
mostrou as views dela). O custo por view "derivado" daquela leitura pode voltar
a ser o oficial.

Três limites de GAQL que apareceram junto, todos com erro explícito:

- **`WHERE` não aceita `OR` nem parênteses** (`unexpected input OR`; `invalid
  field name '('`). Filtro por várias campanhas é `campaign.id IN (...)`.
- **`FROM video` exige `campaign.id` no SELECT** quando o WHERE filtra por
  campanha (`The following field must be present in SELECT clause`).
- **`FROM video` não segmenta por `segments.conversion_action_name`** — inscrito
  no canal por vídeo não sai da API; só por campanha (`FROM campaign` com o
  segmento). Ação de inscrito: `YouTube channel subscriptions`, categoria
  `ENGAGEMENT`, contada em `all_conversions`.

E um de SDK: `proto-plus` devolve enum como `IntEnum` — `isinstance(x, int)`
é verdadeiro e o `.name` some se a checagem de int vier antes. Testar
`isinstance(x, enum.Enum)` primeiro, senão a categoria da conversão vira `19`
em vez de `ENGAGEMENT`.

## §25 — Grupo Demand Gen novo é `use_audience_grouped = true`: copiar critérios soltos da referência dá erro — *UNIVERSAL*

*(medido na distribuição de conteúdo)*

Ao duplicar o grupo de uma campanha de referência (§10), `ad_group_criterion`
dela devolve, além de `LOCATION` e `AUDIENCE`, também `CUSTOM_AUDIENCE`,
`USER_LIST` negativos e `AGE_RANGE` positivos/negativos. **Esses três são a
materialização da `Audience` agrupada** (lista + custom audience + idade +
exclusões vivem dentro dela — `audience.dimensions` e
`audience.exclusion_dimension`). Recriar eles soltos no grupo novo falha em
lote:

```
criterion_error: CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET
```

e como o `mutate` é atômico, nem o `LOCATION` entra — a campanha fica sem geo
(o caso do §7). Receita que passa: no grupo novo, só `LOCATION` +
`AUDIENCE` (a mesma resource da referência). Se a referência não tiver
`AUDIENCE`, aí sim os soltos. Com essa receita, a conferência contra a
referência mostrou geo, exclusões e idade iguais às dela depois.

Duas notas do mesmo dia: campanha nova nasce com
`network_settings.target_content_network = False` enquanto todas as outras
da conta rodam `True` (1 chamada corrige: update em
`network_settings.target_content_network`, §5); e o item de UTM da conferência
(`utm_campaign` = nome) é regra de captação — anúncio de distribuição aponta pro
canal do YouTube sem UTM, igual à referência, então esse FAIL é desenho (§15),
não erro.

## §26 — Demand Gen apontando pra TRANSMISSÃO AO VIVO não entrega clique — *VARIAÇÃO ISOLADA (4 campanhas, 2º lançamento)*

*(Medido no debriefing do 2º lançamento.)*

As quatro campanhas Demand Gen do "é hoje" das aulas (destino = link da live no
YouTube, janela 00:00→20:30 por `ad_schedule`) fizeram **3, 3, 28 e 2 cliques**
— um custo por clique de **~50 a ~100 vezes** o do Display no mesmo momento. As
irmãs da gravação (destino = página da aula) fizeram 635, 445 e 281 cliques, e o
Display do "é hoje", 538, 352 e 407 cliques, as duas com custo por clique de
centavos. Mesma verba, mesmo público, mesmo dia: o que muda é o destino ser uma
transmissão agendada. O porquê não foi medido (leilão de DG pra URL de live? o
vídeo "agendado" sem conteúdo?); o que dá pra dizer é que **"é hoje" no Google
vai pra Display ou não vai** até alguém testar DG com destino em página que
embute a live. Na Meta, o mesmo momento custou ~2× o clique do Display (por
clique de link).

## §27 — Customer Match não sobe mais pela Google Ads API (este developer token) — e a exclusão de comprador sai por lista de regra de site — *UNIVERSAL (política da plataforma)*

`OfflineUserDataJobService.create_offline_user_data_job` com `CUSTOMER_MATCH_USER_LIST`
devolveu `not_allowlisted_error: CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE` — "Customer
Match uploads aren't supported in the Google Ads API for the developer token of the
request. Use the Data Manager API". Na semana de aulas do 2º lançamento o mesmo código
parecia ter funcionado; a regra teria mudado no meio (o adendo abaixo contradiz isso).
Criar a lista CRM continua possível (ela nasce vazia); **subir e-mail não**. Caminho
oficial: Data Manager API — escopo OAuth novo (`datamanager`), que exige autorizar de
novo.

**Saída que não depende disso (aplicada num lançamento pago semanal):** lista **por
regra de site**, que o Google preenche sozinho: `url__ CONTAINS <trecho do endereço da
página de obrigado>` (as páginas de obrigado têm a tag do Google Ads da conta),
`prepopulation_status = REQUESTED` (puxa os últimos 30 dias), 540 dias. Entra no
`exclusion_dimension` do público agrupado (§25 e a tabela do §11: máscara
`exclusion_dimension.exclusions`) — vale pra todo grupo que usa aquele público. O upload
CRM fica como caminho separado, pra quando o acesso existir. Limite honesto: só exclui
quem **abriu** a página de obrigado com a tag disparando; quem pagou e não passou por ela
escapa. Lista por regra também é a única que o **Display** aceita (§18).

**Adendo do mesmo dia, mais tarde — data e fonte do erro:**
- O primeiro registro da recusa **não é do dia em que esta seção foi escrita**: está no
  log da criação de públicos da semana de aulas do 2º lançamento, com o mesmo
  `CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE`. Isso contradiz o "o mesmo código
  funcionou" acima. A lista CRM de leads do 2º lançamento foi criada nessa rodada,
  estava em 0 no dia e aparece com alguns milhares de pessoas quatro dias depois — por
  um caminho que não está registrado.
- Revalidado com `validate_only` (não cria nada): mesma recusa.
- ~~Uma lista por regra lia `membership_life_span = 0`, então não guardava ninguém~~ —
  **leitura errada, corrigida no mesmo dia** (por GAQL e `validate_only`): em lista por
  **regra** o `membership_life_span` é **ignorado** (doc da lib, v21–v25,
  `resources/types/user_list.py`); a duração real é o **`lookback_window_days` de cada
  operando** (`FlexibleRuleOperandInfo`). A lista tinha lookback **540** — a retenção é
  540 — e as 0 pessoas eram a pré-população ainda `REQUESTED` (lista criada naquela
  madrugada). Não precisou recriar. Prova do outro lado: uma lista "SITE - PAGE VIEW
  QUALQUER PAGINA 30D", criada com span 30 e sem lookback, lê lookback 540 — é uma lista
  de 540 dias com nome de 30. **Regra:** lista por regra grava e confere o lookback em
  cada operando; conferir pelo span dá alarme falso (lê 0) e deixa passar um 540 no
  lugar de 40.

## §28 — Vídeo recém-subido no YouTube: o anúncio só aceita depois que a duração resolve — *CONSISTENTE (3 vídeos, em dois dias diferentes)*

Anúncio Demand Gen com vídeo subido pela API minutos antes volta
`asset_link_error: YOUTUBE_VIDEO_DURATION_NOT_DEFINED`. Não é erro de arquivo: o YouTube
ainda está processando. Resolveu em 2 a 5 minutos nas três vezes. Quem sobe e cria
anúncio em seguida precisa de nova tentativa espaçada (4 min) — e o laço de nova tentativa
tem que olhar o **resultado** (o anúncio existe na conta), nunca o texto da saída: numa
das vezes, um `grep "anúncio criado"` casou com a linha de código mostrada no traceback e
o laço parou achando que tinha criado.

## §29 — A tag do Google Ads é POR PÁGINA, não por domínio: conferir a página de destino antes de planejar lista por URL — *VARIAÇÃO ISOLADA (downsell do 2º lançamento)*

A tag do Ads desta conta (o `conversion_tracking_id` da conta) não fica solta no HTML:
vem dentro de um **container do Google Tag Manager** (`GTM-…`), colado página a página. A
tag do Site Kit do WordPress (um `GT-…`), que aparece em todas as páginas, **só entrega
pro GA4** — quem lê "tem gtag na página" e conclui "tem tag do Google" erra.

Medido por `curl`, página por página, na montagem do downsell:

| Página | Tinha o container? |
|---|---|
| inscrição, aula 1, página das lives de aquecimento e obrigado do evento pago (este, nos dois domínios) | sim |
| página de venda do downsell | **sim, só depois de colado naquela noite** (num widget HTML da página, com backup antes; conferido no navegador: as chamadas de conversão, de remarketing e de lista de usuários saindo pra conta) |
| cópia da página do downsell no outro domínio | **não** |
| obrigado do lançamento, aulas 2 a 4, carta de vendas, página do grupo | **não** |
| página de venda do lançamento (e a cópia), obrigado das duas compras | **não** |

Efeito na API: lista por regra de página sem o container fica em **zero** (uma lista de
540 dias de visita ao obrigado de compra: disp 0, srch 0), e a ação `Visualização de
página` marcou 0 em 7 dias. Demand Gen com meta `PAGE_VIEW` apontando pra essas páginas
otimiza sem sinal nenhum. ⚠️ Exceção que não se explica pela tabela: a lista de 540 dias
do obrigado do lançamento tem alguns milhares de pessoas e a página hoje não tem o
container — a lista é de 540 dias e pode ter enchido quando a tag estava lá; não medido.

**Regra de consulta:** antes de planejar remarketing de Google por visita a uma página
(ou exclusão por página de obrigado), `curl` a página e procurar o ID do container da
conta. Sem ele, a lista não existe na prática. A `prepopulation` do §27 só recupera o
que a tag viu, então visita anterior à instalação não volta. No downsell do 2º
lançamento isso bloqueou Display e Demand Gen até a tag ir pra página do downsell naquela
noite — o que veio antes disso se perdeu pro Google (evidência no caso de origem).

⚠️ **Colar o GTM em página de obrigado de COMPRA contamina a conversão de lead.** O
container dispara a conversão do Ads **`Enviar formulário de lead`** (categoria
`SUBMIT_LEAD_FORM`, **primária**, uma por clique) em qualquer URL que contenha "obrigado"
(gatilho conferido; ação identificada pelo rótulo no `tag_snippets` da API). Em página de
obrigado de compra, compra passaria a contar como lead nas campanhas que otimizam lead.
Antes de colar lá, o gatilho precisa excluir essas páginas.

**Outro efeito do mesmo container:** ele também dispara `PageView` num pixel antigo da
Meta (fora de uso, da mesma conta de anúncios), no rastreador do Dash Fácil e no Clarity.
Nenhum público de site da Meta usado no 2º lançamento está nesse pixel (todos no pixel
principal, conferido regra a regra).

**Dá pra virar checagem** (no caso de origem ainda não era automática): para cada URL
final de campanha Google gastando, baixar a página e acusar se não tiver o container.
Está no checklist do §32.

## §30 — Lista por regra com VÁRIOS endereços: um operando por endereço, ligados por OU — *VARIAÇÃO ISOLADA (validate_only, downsell do 2º lançamento)*

A receita que estava em uso pra "visitou qualquer um destes endereços" (**um** operando,
um grupo por URL, "grupos = OU", corrigida nove dias antes) é **recusada** pela v25
quando há mais de um endereço:

```
user_list_operation.create.rule_based_user_list.flexible_rule_user_list.inclusive_operands: Too many.
```

Medido com `validate_only` na montagem do downsell do 2º lançamento (3 endereços: o
trecho comum das páginas do lançamento, a página do grupo e a página de venda do
downsell). A forma aceita: `inclusive_rule_operator = OR` e **um
`FlexibleRuleOperandInfo` por endereço**, cada um com um grupo, um item e o
**`lookback_window_days`** (a retenção real — ver o adendo do §27: o
`membership_life_span` é ignorado em lista por regra). A leitura de volta confere o
lookback de cada operando, o operador OU e a regra antes de qualquer campanha —
porque o `validate_only` **aceita calado** operandos em E e lookback 0 (lookback 541 ele
recusa). As listas de um endereço só (ex.: a do obrigado do evento pago) não esbarram no
`TOO_MANY`. Uma lista antiga das aulas (15 dias) segue com a regra E da primeira versão;
a recriação dela nove dias antes (receita de um operando com vários grupos) foi recusada
com `TOO_MANY` e **nunca existiu** — medido pela mesma sessão. Nada foi mexido nelas.

Na mesma montagem: o `GoogleAdsService.Mutate` aceita a cadeia inteira com IDs temporários
— lista nova, imagens, orçamento, campanha, geo, horário, grupo, audience, critérios e
anúncios — e referência a lista temporária dentro da audience e do critério no mesmo
pedido. Com `validate_only=True` valida tudo sem criar nada (conferido depois por leitura:
nenhuma campanha, lista, imagem ou audience nova). É o caminho pra validar a cadeia de
criação inteira antes de escrever (a exceção ao "estágio por estágio" do §0 e do §8).

## §31 — Captação Demand Gen: UTM no sufixo, content network na criação, conferência atualizada — *VARIAÇÃO ISOLADA (captação de uma Black)*

- **A UTM do Google mora no `final_url_suffix`**, com as variáveis do próprio Google (regra
  do Rodrigo, `sirius-scale/frameworks/trafego/nomenclatura.md` §3.7): o URL final fica
  limpo (a página) e o Google troca `{campaignid}`, `{network}`, `{creative}` e
  `{adgroupid}` no clique. A conferência que lia a UTM só do URL final e comparava com o
  NOME da campanha passou a ler o sufixo também e a aceitar `utm_campaign={campaignid}`.
- **Content network ligada já na criação.** As 3 campanhas da Black nasceram com
  `target_content_network = False` (o mesmo do §25) e a conferência barrou; corrigido com
  1 chamada e, dali em diante, criando com `True`.
- **[PQ] fora da igualdade de segmentação otimizada.** A referência de captação quente do
  2º lançamento tem a otimizada LIGADA (é anterior à regra do
  `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.6); conferir uma [PQ] nova
  contra ela dava FAIL por estar certa. A conferência agora deixa a [PQ] só com a regra
  dela (otimizada desligada, seja qual for a referência), sem exigir igualdade.
- **Um anúncio por criativo**, cada um com os textos dele, pra `utm_content={creative}`
  separar a venda por peça no Dash; o 16:9 entra depois no MESMO anúncio (anexar, §5/§13),
  sem perder o id.
- Os anúncios novos ficam em `REVIEW_IN_PROGRESS` mesmo PAUSADOS, e a revisão anda com eles
  pausados.

## §32 — Checklist de conferência: antes de ativar e na leitura diária

> No caso de origem, estas conferências rodavam em script, lendo a conta pela API. Aqui
> elas são o checklist que o Claude roda lendo a conta pelo conector do Google (se estiver
> ligado) ou que quem sobe a campanha confere na tela. Nada aqui é regra nova: cada item
> junta o que as seções acima já dizem e aponta o porquê. Conta nova ou reativada passa
> antes pelo §33.

**Antes de ativar** — campanha nova contra a irmã da mesma fase e etapa (§10), com a
config **lida da plataforma**, não da intenção:

1. **Geo.** Demand Gen: `LOCATION` em todo grupo ativo, porque a campanha recusa geo
   (§6). Display padrão: na campanha (§7.1). Grupo Demand Gen ativo sem LOCATION barra a
   ativação.
2. **Metas.** `campaign_conversion_goal`: `biddable=True` só na categoria que a fase
   otimiza. Em Demand Gen, nunca concluir nada por `selective_optimization` vazio (§2,
   §10).
3. **Lance.** `bidding_strategy_type` e teto iguais aos da irmã da mesma fase e etapa
   (§10). Manual CPC: `cpc_bid_micros` setado em todo grupo, acima do mínimo (§21).
4. **Rede.** `network_settings.target_content_network` igual ao das irmãs; campanha nova
   nasce `False` (§25, §31).
5. **Segmentação otimizada.** `ad_group.optimized_targeting_enabled` igual ao da
   referência; em público quente, desligada, seja qual for a referência (§31;
   `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.6).
6. **Público.** A `Audience` agrupada com as mesmas listas da referência, as exclusões
   como exclusão (flag `negative`) e a mesma faixa etária (§11, §25). No Display, só
   lista por regra (§18); lista por regra conferida pelo lookback de cada operando (§27,
   §30).
7. **Anúncio.** Na captação, os 2 formatos de vídeo no mesmo anúncio (§13); logo presente
   e pelo menos 1 de cada texto (§12.1); UTM no `final_url_suffix` (§31).
8. **Aprovação.** `policy_summary` de **todo** anúncio, não por amostra, filtrando
   `status != 'REMOVED'`: `DISAPPROVED` barra, `APPROVED_LIMITED` avisa, revisão em
   andamento espera (§15, §17, §20).
9. **Datas e horário.** `end_date_time` setado; `ad_schedule` quando a fase tem janela por
   hora (§16).
10. **Página de destino.** Tem o container da tag do Google Ads da conta; e a página de
    obrigado de compra não dispara a conversão de lead (§29).
11. **A conferência conferiu?** Contar quantos itens ela leu de fato: conferência que não
    leu nada parece verde (§3.2). Diferença contra referência de outra fase é classificada
    contra a decisão que a gerou antes de virar correção (§15).

**Depois de ativar** — leitura diária, só o que gastou (ou deveria ter gastado) nos últimos
7 dias ou hoje: `DURING TODAY` somado ao `LAST_7_DAYS` (§7, §21):

12. **Gasto por país** (`user_location_view`): o país do público (no caso-base, Brasil,
    2076) perto de 100% (§7). Em lista fechada, medir antes de classificar (§7.1).
13. **Gasto por hora** (`segments.hour`) em campanha com janela (§22), e **gasto por dia
    depois do `end_date_time`** — nunca `status` (§22).
14. **Manual CPC com gasto zero** (§21).
15. **Demand Gen estático:** reler os anúncios do grupo horas depois (vídeo automático) e
    ler o CPC por tipo de anúncio (§23).
16. **Canais do grupo e rede da campanha** iguais aos da referência (`channel_controls` e
    `network_settings`; o Shorts é o que mais some, §35).

## §33 — Conta de cliente novo ou reativada: o que ligar antes da primeira campanha — *VARIAÇÃO ISOLADA (conta de outro expert da casa, reativada pra uma Black)*

Caso de origem: a conta estava `CANCELED` na MCC, com o último gasto dois anos antes.

- **Quem reativa é a pessoa dona da conta, na tela:** Administrador → Configurações da conta
  → Status da conta → Reativar. O navegador controlado pelo Claude caiu na reautenticação do
  Google ("Confirme que é você"), e senha é da pessoa.
- **A API abre alguns minutos depois da tela.** Medido: o `customer_client` da MCC virou
  `ENABLED` na hora, mas a conta respondeu `CUSTOMER_NOT_ENABLED` ("not yet enabled or has
  been deactivated") por ~5 minutos. Foram 4 tentativas de 1 em 1 minuto até abrir. Esperar
  em laço, sem concluir que a reativação falhou.
- **Conta antiga chega com conversão velha marcada como primária** (dezenas, de anos antes).
  Se nenhuma página tem a tag delas, elas não disparam e não fazem dano: não se mexe. A
  campanha nova marca `biddable` só no lead (§2).
- **O gerenciador de tags do cliente pode não ter o Google Ads.** Ler o
  `gtm.js?id=<container>` público antes de supor que a tag existe (como no
  `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §11). No caso, ele tinha só os
  pixels da Meta, o GA4 e o Clarity, e a tag foi direto pro HTML das páginas.
- **A preparação da conta** (na casa, um script só, que rodar de novo reaproveita o que já
  existe):
  - criar a conversão de lead copiando, campo a campo, a de uma conta que funciona, lida da
    plataforma;
  - criar as listas por URL;
  - validar a seco, confirmar e ler tudo de volta;
  - guardar o `send_to` num arquivo do lançamento, de onde a montagem da página lê.
- **Conferir pelo efeito, sem abrir o obrigado.** Abrir a página e procurar
  `viewthroughconversion/<id>` e `rmkt/collect/<id>` no
  `performance.getEntriesByType('resource')`. A lista de rede do navegador controlado pelo
  Claude só mostrou o documento. O obrigado não se abre, porque dispara Lead no pixel da Meta.
- `campaign.start_date` voltou a aparecer na leitura (é `start_date_time` na v25, §16 e §24),
  junto com `DURING LAST_90_DAYS`, que não é literal válido. Erro barato, que a API recusa na
  hora. Fica o registro de que foi a terceira vez com o nome velho.

**A primeira campanha da conta.** O que faltava pra conta nova rodar Demand Gen, na ordem em
que apareceu:

- **Vídeo.** Pelo comando `videos` do sistema não existe token de canal (§9). Quem sobe pela
  Data API do YouTube precisa de um, e aí o canal é do cliente, e o token também: subir com
  o token de outro canal publica no canal errado. O canal certo sai da própria conta: os
  assets `YOUTUBE_VIDEO` dela → `videos.list` → `channelId`. Vale um token por canal (na casa,
  o gerador de token só grava se o canal escolhido na tela do Google for aquele). A cota de 6
  uploads por dia é do projeto do Google Cloud, a mesma pros dois canais.
- **Logo e botão não existem em conta que nunca rodou Demand Gen** (zero anúncio multi-asset
  ou de vídeo responsivo). Criar os dois antes do primeiro anúncio e ler de volta; a
  ferramenta de subida faz isso (`sirius-scale/ferramentas/google/subir_campanha.py`). O logo
  do caso foi a foto do canal (1200×1200), decisão de forma.
- **Estático no mesmo grupo dos vídeos:** criativo de imagem com as versões paisagem e
  quadrada vira `demand_gen_multi_asset_ad` no grupo (§19); feed 4:5 e story 9:16 são os
  arquivos da Meta. Com isso a campanha nasce só com os estáticos, e os vídeos entram depois
  no mesmo grupo.
- **Lista do YouTube mede o tamanho em `size_for_search`**, não em `size_for_display`: as
  listas de 540 dias do YouTube leram display 0 e pesquisa na casa do milhar.
- **Referência de outra conta:** a conferência aceita comparar com uma campanha de outra
  conta (`sirius-scale/ferramentas/google/conferir_campanha.py`). Logo depois de criar, o item
  de política dá FAIL com `UNKNOWN` (a revisão ainda não começou); rodar de novo antes de
  ligar (§15).
- **Lista de cliente:** a criação vazia passou no `validate_only` numa conta sem nenhuma lista
  CRM. O envio vai pela Data Manager API (§27; planilha → hash → lista), que declara os termos
  do Customer Match como aceitos. Conta que nunca teve lista de cliente não aceitou esses termos
  na tela: o envio aceita em nome dela, então pede o ok do dono da conta antes.

## §34 — Display: UTM do Google no sufixo, fim às 23:59:59 e uma campanha por dia — *VARIAÇÃO ISOLADA (contagem regressiva de uma Black, criada pausada)*

- **UTM:** a URL final fica limpa (a página) e a UTM vai no `final_url_suffix` do anúncio, com
  as variáveis do próprio Google. É a regra de
  `sirius-scale/frameworks/trafego/nomenclatura.md` §3.7, a mesma da captação (§31), valendo
  também no Display. Nome escrito à mão na UTM foi o desvio do 2º lançamento.
- **Fim:** o `end_date_time` às 20h foi recusado na validação a seco ("The date time string
  must end with 23:59:59 to indicate the end of the day"). O "é hoje" termina às 23:59:59 e
  quem para às 20h é o horário (`WEDNESDAY 00:00 → 20:00`), como no §16 e no §22.
- **Uma campanha por dia** quando a mensagem muda de um dia pro outro ("faltam 2 dias", "é
  amanhã"): o Google também não agenda anúncio nem grupo, só campanha. Cada uma paga o piso de
  orçamento por dia (§1), e a verba do plano pro Display ficava abaixo dele.
- **Rodou** (a contagem criada de verdade, pausada): as 3 campanhas passaram na validação a
  seco, na leitura de volta e na conferência. O único FAIL antes disso foi `politica UNKNOWN`.
  Os 3 anúncios responsivos, com texto desenhado na imagem (data, chamada, botão), voltaram
  `APPROVED` / `REVIEWED` uns 37 minutos depois de criados. Estavam pausados, e a revisão andou
  mesmo assim, como a do Demand Gen do §15 (35 min). O texto na imagem não barrou a aprovação.
- **Campanha de hoje vai sem data de início:** o Google não aceita início no passado. Sem o
  campo, a data de início fica no dia da criação.
- **Lista nova numa campanha e reaproveitada nas outras:** a lista por regra criada na campanha
  do primeiro dia, com pré-população, foi achada pelo nome nas campanhas dos dias seguintes. Por
  isso a ordem de criação é a dos dias.

## §35 — Copiar de uma campanha de referência: canais do grupo e rede também — *VARIAÇÃO ISOLADA (campanhas de vídeo de um lançamento pago)*

- **O grupo nasce com os canais padrão da conta, e a campanha com a rede padrão.** Um criador que copiava lance, metas,
  geo e público da referência, mas não `channel_controls` (do grupo Demand Gen) nem `network_settings` (da campanha),
  subiu grupos sem o Shorts. Ao copiar de referência: ler os dois, copiar, ler de volta e parar antes do anúncio se
  faltar um canal que a referência tinha. Na conferência antes de ativar, comparar os canais do grupo com os da
  referência (item novo do §32).
- **Vídeo pro canal do próprio cliente pela API do Google Ads:** num teste, o início do upload com o `channel_id` do
  canal do expert voltou `Request contains an invalid argument`; sem ele, passou e o vídeo caiu no canal gerenciado pelo
  Google. O motivo não foi investigado (o vínculo do canal com a conta é o primeiro suspeito). No canal gerenciado, quem
  assiste ao anúncio não entra nas listas de público do canal do expert; o campo `videos` do anúncio troca sem perder o
  id, então dá pra trocar pelo vídeo no canal dele depois.
- **Lote de vídeos:** enviar todos antes e esperar depois. 20 vídeos (2,3 GB) ficaram `PROCESSED` em uns 15 min. A Data
  API do YouTube não serve pra lote: a cota padrão é de poucas subidas por dia.
- **Lista de comprador vazia derruba a exclusão calada.** Antes de contar com "exclui quem comprou", ler o tamanho da
  lista na busca e no display. Lista com tamanho 0 é a tag do Google faltando na página de obrigado (§29).
