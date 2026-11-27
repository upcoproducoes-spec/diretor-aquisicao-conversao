# Metodologia de Análise de Tráfego

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** mista — leia o §7 antes de aplicar em cliente novo.
> **Alcance:** as **regras de leitura** (§1, §2, §4, §5) são UNIVERSAIS: são mecânica de
> plataforma e higiene de análise, valem pra qualquer cliente e qualquer negócio. Os **números de
> corte** (§3.1, §3.1.1) são NÃO TESTADO FORA — vêm de 1 cliente (o caso-base, um expert de
> educação), 1 lançamento (o L4), poucos dias de dado, e já estão marcados ISOLADA no corpo.
> **Não confunda os dois.** "Não decidir por CPL do gerenciador" transfere; "R$ 15/dia de piso" e
> "2,5x pra cortar" não transferem sem revalidar.

> Regras que valem pra qualquer plataforma (Meta, Google, o que vier). Os lançamentos gratuitos do
> caso-base aparecem como **L1 a L4**, em ordem.

## 1. O nome nunca diz o que está sendo medido

**Regra dura: sempre confirmar a ação de conversão real na plataforma antes de qualquer análise.
Nunca inferir pelo nome da campanha, nem pelo objetivo do nível de cima.**

Isso já nos mordeu duas vezes:

**Meta.** O `optimization_goal` do conjunto aparecia como `OFFSITE_CONVERSIONS` nos dois lançamentos
analisados — mas um otimizava pra `PURCHASE` e o outro pra `LEAD`. A diferença só aparece no
`promoted_object.custom_event_type`. Objetivo da campanha (`OUTCOME_SALES`, `OUTCOME_LEADS`) também
não serve: um conjunto dentro de campanha de venda pode estar otimizando por cadastro.

**Google.** Campanhas nomeadas `[INSCRIÇÃO]` rastreavam a ação "Compra" (categoria `PURCHASE`).
Estava correto — "inscrição" ali significa comprar ingresso do lançamento pago — mas o nome sugeria
captação de lead. Só a consulta em `segments.conversion_action_name` revelou.

### Onde checar

| Plataforma | Campo |
|---|---|
| Meta | `promoted_object.custom_event_type` (no conjunto de anúncios) |
| Google | `segments.conversion_action_name` + `segments.conversion_action_category` |

Sem API ou conector, a mesma checagem é na tela: na Meta, o evento de conversão do **conjunto** (não
o objetivo da campanha); no Google, a ação de conversão que a campanha usa e a categoria dela.

## 2. Nunca somar conversões de objetivos diferentes

Conversão de engajamento e conversão de compra não vão no mesmo total. O número agregado fica sem
sentido e, pior, **parece bom**.

**Caso real (Google, uma conta do caso-base, 30 dias):**

| Cálculo | Custo por "conversão" (só compra = 100) |
|---|---:|
| Total misturado (compra + inscrito de canal) | ~10 |
| Só compra (real) | **100** |

Dez vezes de diferença. As campanhas de `[DISTRIBUIÇÃO]` contavam inscrito de canal (categoria
`ENGAGEMENT`), o que é o objetivo correto **delas** — mas somadas às campanhas de venda, distorciam
tudo.

**Sempre segmentar por objetivo real de conversão antes de agregar.**

## 3. CPL/CPA não mede qualidade de lead

O relatório da plataforma diz **quanto custou**, não **o que converteu depois**.

**Caso real (Meta, L3):** as campanhas de teste 1-1-1 foram as que mais trouxeram vendas na abertura
do carrinho — mesmo não sendo as de menor CPL.

📌 Julgar campanha de captação só por CPL pode matar justamente a que sustenta o faturamento. A
qualidade do lead só aparece no cruzamento com MQL/lead score (Dash Fácil). Tratar o CPL da
plataforma como **indicador parcial**, nunca como veredito.

### 3.1 A régua de otimização (regra dura)

> **Otimizar sempre por custo por MQL ou por lead score — nunca só pelo CPL do gerenciador.**

O cruzamento deixou de ser manual: na casa, uma rotina diária puxa o Dash e as duas plataformas e
devolve custo por MQL por campanha. Do lado de vocês, o mesmo cruzamento sai pelo MCP do Dash
Fácil: o `tabela_utm_captacao` já traz investimento, leads, MQL e o `potencial` por campanha ou
conteúdo (cuidado com o imposto da Meta e com as fases que a tela de captação deixa de fora,
`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.2). Então a régua passa a ser essa, em
três camadas:

| Métrica | Vale pra quê |
|---|---|
| **CPL do gerenciador** | Sinal de entrega, nunca de decisão. Infla o lead real — no L4 a Meta reportou **+19%** de leads sobre os cadastros de fato, porque conta clique 7d e o Dash é last-click real. |
| **CPA real** = gasto bruto da plataforma ÷ lead real do Dash | Piso da análise. Já corrige a atribuição, mas ainda não enxerga qualidade. |
| **Custo por MQL** = gasto ÷ (leads × taxa de MQL) · e a distribuição de faixa A/B/C/D | **É por aqui que se decide verba.** |

Três cuidados que não são opcionais:

1. **A taxa de MQL é sobre quem respondeu a pesquisa, não sobre a base.** No L4, 39% dos leads têm
   MQL vazio. Projete pro total (`leads × taxa`) e **declare que projetou** — cai na regra do §4.
2. **Exija volume antes de agir.** Custo por MQL entre duas unidades com poucas dezenas de leads não
   decide nada — ver `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §3, que mostra o sinal
   invertendo de direção entre lançamentos quando o N é de criativos. Diferença pequena com base
   fina = observar mais um dia, não cortar.
3. **Custo por MQL é o melhor proxy disponível ANTES da venda, não um preditor validado de venda.**
   Depois que o carrinho abre, quem manda é venda e ROAS.

**Caso que originou a regra (L4, começo da captação):** por CPL do gerenciador a campanha de público
quente parecia aceitável. Por custo por MQL ela aparece como o pior uso de verba da conta — **~4× o
custo por MQL das campanhas frias** (de 3,8 a 4,0×), consumindo 27% do orçamento diário. O CPL
sozinho não mostrava isso.

> Nível de confiança: **PADRÃO CONSISTENTE** para "não decidir por CPL do gerenciador" (o §3 acima já
> vinha do L3 e replicou aqui).
> **VARIAÇÃO ISOLADA** para os números de custo por MQL do L4 — um cliente, um lançamento, um dia e
> meio de dado.

### 3.1.1 A escada de verba — o corte tem PISO, não proporção · *VARIAÇÃO ISOLADA*

**VARIAÇÃO ISOLADA** — um cliente, um lançamento. Escrita a partir do que o Rodrigo *de fato fez* em
duas rodadas de verba, não de regra teórica. Se repetir em outro cliente/lançamento, sobe pra
CONSISTENTE.

Comparando cada unidade contra o **melhor custo por MQL da rodada**:

| vs. melhor | Ação |
|---|---|
| ≤ 1,15x | **subir +30%** — degrau, não dobra |
| 1,15x – 1,5x | manter (zona de ruído) |
| 1,5x – 2,5x | **baixar ~40%**, até o piso de verba |
| ≥ 2,5x | **baixar ~50%**, até o piso de verba |
| volume abaixo do piso | observar |
| conjunto em LEARNING | segurar o corte até sair da fase |

**O piso de verba** é o mínimo diário em que a plataforma ainda entrega: R$ 15/dia na conta medida
(Meta; valor da época, conferir na plataforma).

**Os dois achados que sustentam isso** vieram da segunda rodada (o melhor da conta era um criativo em
teste, chamado aqui de criativo 1):

| Campanha | vs. melhor | O que foi feito |
|---|---:|---|
| Criativo 1, teste | 1,00x | +30% |
| Criativo 2, teste | 1,05x | +30% |
| Mix quente `[PQ]` | 2,61x | −44% |
| Outro criativo, fora do teste | 2,83x | −50% (até o piso) |
| Pré-escala do criativo 2 | 4,57x | −40% |
| Pré-escala do criativo 1 | 5,87x | −40% |

1. **Pausar não é o padrão.** Nada foi pausado, nem a 5,87x. Na rodada anterior, a `[PQ]` a 2,2x
   levou −64% com a decisão escrita de "reduz, não pausa". A única pausa do lançamento foi por
   "0 venda" e pelo tema do criativo — razão de oferta, não de custo por MQL.
2. **O corte não escala com a gravidade — ele tem piso.** 5,87x levou −40% e 2,83x levou −50%. Não é
   proporção: espreme o ruim até ~R$ 15–30/dia e para ali, porque abaixo disso a Meta não entrega e o
   dado morre junto.

**Quando pausar então:** quando as três coisas baterem juntas — criativo novo na fila esperando
teste, verba do plano sem folga, e a unidade ≥ 2,5x. Aí pausar não é punição, é como se financia o
teste. Decisão de contexto, nunca automática.

O +30% de aumento não é arbitrário: acima disso arrisca resetar a fase de aprendizado do Advantage+
(mecânica documentada da Meta).

Na casa, essa escada roda numa régua automática, com os cortes ajustáveis num lugar só. Do lado de
vocês, ela entra como ponto de partida ao pedir a leitura de verba ao agente `gestor-trafego` (§7),
e a decisão de mexer continua de quem é dono da verba (`sirius-scale/REGRAS.md` §6).

### 3.2 No Dash, UTM TERM mistura plataforma quando o nome do anúncio se repete

> Atualização: com o padrão de UTM do Google da casa (`sirius-scale/frameworks/trafego/nomenclatura.md`
> §3, regra 7), o nome do anúncio fica em TERM na Meta e em CONTENT no Google. Comparar criativo
> entre plataformas não cabe numa coluna só; ver
> `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §10.

**VARIAÇÃO ISOLADA** — observado uma vez (L4), ao ler a aba Origem do Dash Fácil pra achar o melhor
criativo por custo por MQL.

Quando o mesmo criativo roda em Meta E Google com o nome de anúncio idêntico (ex.:
`AD - <código do criativo> - <gancho>`, usado nos dois porque o código do criativo é do cliente, não
da plataforma — ver `sirius-scale/frameworks/trafego/nomenclatura.md`), a tabela **UTM TERM** do Dash
mostra a MESMA contagem de leads e os MESMOS % de MQL/faixa A-B-C-D nas abas "Meta Ads" e "Google
Ads" — só o Valor Gasto muda (cada aba puxa o gasto da plataforma certa). Ou seja: o número de
leads/MQL ali é o total cruzado por nome, **somando as duas plataformas**, não o lead daquela
plataforma sozinha.

**Consequência prática:** custo por MQL calculado a partir da tabela UTM TERM pra um criativo que
roda nas duas plataformas fica errado se você pegar o gasto de uma aba e a taxa de MQL "daquela aba"
— na real a taxa é a combinada. **Usar UTM CAMPAIGN ou UTM CONTENT em vez de UTM TERM** quando for
comparar por plataforma — essas duas tabelas são calculadas corretas por aba, porque o nome de
campanha/content carrega tag de plataforma (ex.: `03-YT-ADV-<lançamento>-<criativo>` no Google vs
`03 - ADVANTAGE+ <lançamento>-<criativo>` na Meta) e não colide entre as duas. Pelo MCP vale o
mesmo: no `tabela_utm_captacao`, `nivel` = `utm_campaign` ou `utm_content` pra comparar por `fonte`
(meta × google), até medir que o `utm_term` dele não repete o comportamento da tela.

## 4. Declarar aproximação sempre que houver

Se a análise precisou assumir, mapear ou aproximar algo, **dizer isso no resultado**. Nunca entregar
número como certeza quando ele foi inferido.

Exemplo do que fazer: "mapeei resultado pelos action_types X, Y e Z; isso é uma aproximação do que a
API expõe — vale cruzar com o Gerenciador antes de decisão de budget maior."

## 5. Rate limit: cache e batch desde a primeira leitura

| Plataforma | Limite |
|---|---|
| Meta | Score acumulado por conta — estoura com chamada em sequência |
| Google (Explorer Access) | 2.880 operações/dia (valor da época, conferir) |

**Regras:**
- Buscar campos adicionais **na mesma chamada** em vez de fazer chamada nova (pedir
  `optimization_goal` junto de nome/status custa quase nada).
- Cachear insights já buscados; reusar dentro de uma janela de algumas horas.
- Usar endpoints de lote quando existirem, em vez de um-por-um. No MCP do Dash, a mesma ideia: pedir
  a tabela inteira do nível certo numa chamada (`tabela_utm_captacao` com `limite` alto), não uma
  chamada por campanha.
- Filtrar por **ativas** por padrão; histórico completo só quando pedido.

## 6. Períodos de análise

- **Lançamento:** analisar por edição (a tag do lançamento delimita).
- **Perpétuo em geral:** analisar por período (7/30 dias).
- **LPSG:** a semana começa **segunda-feira à meia-noite** (início da captação da semana). Filtrar de
  segunda 00:00 a domingo 23:59 — "últimos 7 dias" mistura dois ciclos de conversão diferentes.

---

### 6.1 Antes de reanalisar um lançamento passado, procure a análise que já existe

**Gatilho de consulta.** Antes de levantar "quais foram os campeões do lançamento X", procurar a
análise que já existe (em `entregas/`, pela tag ou pelo nome do lançamento) e abrir o que aparecer.
No caso de origem, os campeões do L3 foram levantados do zero (Google + Dash, ~40 min de API) quando
o debriefing de criativos do L3, feito 11 dias antes, já tinha a mesma conclusão — três criativos =
76% das vendas pagas. A análise nova acrescentou coisa útil (recorte só-Google, custo por MQL,
config campo a campo), então não foi perdida; mas devia ter **partido** do debriefing e declarado a
diferença de método (lá Meta+Google pela UTM do anúncio; aqui só Google, venda casada por e-mail) em
vez de parecer um segundo número pra mesma pergunta.

Regra: análise nova de lançamento passado **cita** a anterior no cabeçalho e diz em que recorte
difere. Duas análises do mesmo lançamento sem esse elo viram "fontes que divergem" — o pior caso pro
`/pente-fino` (duplicata é pior que ausência).

### 6.2 Projetar conversão de um lançamento sobre outro: usar LIFT, nunca a taxa absoluta

**Gatilho de consulta.** Antes de multiplicar a conversão de um lançamento fechado pelo CPL de hoje
pra estimar custo por venda — inclusive **por plataforma**, não só por criativo —, abrir
`sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §3.8. O método já existe: `LIFT = taxa do
segmento ÷ conversão GLOBAL do lançamento-base`, aplicado como índice sobre a conversão global do
lançamento novo. "O que viaja entre lançamentos é o lift; a taxa absoluta não" já está escrito lá.

No caso de origem, a conversão absoluta do L3 por plataforma (Meta 1,26%, Google 2,20%) foi
multiplicada direto pelo CPL do L4, sem passar pelo lift — o conhecimento estava certo e acessível,
só não foi consultado no momento de fazer a conta. O erro não chegou a virar decisão errada (a
conclusão qualitativa segurou), mas o número (custo por venda projetado) saiu sem o ajuste que o
método já provê.

**Quando o lift cai igual em todo corte, a causa não é a composição da base — *VARIAÇÃO ISOLADA (1
par de edições)*.** No L4 a conversão lead→venda caiu pra 0,52× a do L3, e o lift por corte ficou
entre 0,35 e 0,67 em quase tudo (Google 0,67 · Meta 0,49 · orgânico 0,49 · faixa A **0,38** · faixa B
0,63 · respondeu pesquisa 0,54 · não respondeu 0,44). A ordem dos cortes não mudou (A > B > C > D,
Google > Meta, pesquisa > sem pesquisa) — só a altura. Se a explicação fosse "captamos lead pior", a
queda apareceria na composição (mais faixa C/D, menos pesquisa) e **não** dentro de cada faixa; aqui
a faixa A do L4 (3,5%) converteu menos que a faixa B do L3 (3,6%). O teste, portanto, é olhar o lift
**por corte**, não a taxa total: queda uniforme aponta pra algo que atingiu todo mundo (evento,
oferta, calendário), e "lead pior" só entra quando os cortes caem de forma desigual. Fonte: o
debriefing do L4 (evidência no caso de origem).

## 7. O que transfere e o que é do caso

**Transfere pra qualquer cliente/negócio (mecânica e higiene):**

- §1 inteiro — confirmar a ação de conversão na plataforma, nunca inferir pelo nome. Os campos
  (`promoted_object.custom_event_type`, `segments.conversion_action_name`) são da plataforma, não do
  cliente.
- §2 — nunca somar conversões de objetivos diferentes.
- §4 — declarar aproximação sempre que houver.
- §5 — cache e batch desde a primeira leitura (limites são da plataforma).
- §3 e o topo do §3.1 — **a lógica em camadas** (CPL do gerenciador é sinal de entrega; CPA real é
  piso; custo por MQL decide verba) e os três cuidados (projetar taxa de MQL e declarar, exigir volume
  antes de agir, custo por MQL é proxy pré-venda e não preditor de venda).
- §3.2 — o comportamento de UTM TERM no Dash é do produto, não do cliente: vale pra qualquer conta
  que use a ferramenta.
- O teto de **+30% por aumento**: é mecânica documentada da Meta (reset de fase de aprendizado do
  Advantage+), não número do caso-base.

**Não transfere sem revalidar (1 cliente, 1 lançamento, dado curto):**

- Todos os **números** do §3.1 e §3.1.1: os múltiplos de corte (1,15x / 1,5x / 2,5x), os percentuais
  (−40%, −50%), o piso de R$ 15/dia e a tabela de campanhas da rodada. Vieram do L4 e já estão
  marcados ISOLADA.
- O gap de atribuição de **+19%** (leads da Meta x cadastros no Dash) é daquela conta, naquele
  período. O *fenômeno* (plataforma infla vs. last-click) é geral; o número não.
- O **39% de MQL vazio** é da pesquisa daquele lançamento.
- A regra "pausar não é o padrão" nasceu de uma operação com fila de criativos cheia e verba
  apertada. O critério de quando pausar (3 condições juntas) é transferível como *raciocínio*; o
  comportamento observado, não.

**Do caso, por depender do modelo de negócio:**

- A regra de período do LPSG (§6) só existe pra quem roda LPSG semanal. Cliente com lançamento
  clássico usa a tag da edição; perpétuo usa 7/30 dias.

⚠️ Em cliente novo, os cortes do §3.1.1 entram como **ponto de partida a observar**, não como
automação. A régua que transfere é "decidir por custo por MQL"; a escala de quanto cortar precisa da
primeira rodada de dado do cliente.
