# MQL e qualificação de lead — o que os dados sustentam e o que não sustentam

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** mista — método estatístico (transfere) + calibração do caso-base (não transfere). Ler
> o §6 antes de aplicar em cliente novo.
> **Base:** 1 cliente (o caso-base, um expert de educação) · 2 lançamentos (L2 e L3) + medições no
> L4 · milhares de respostas de pesquisa
> **Alcance:** o **raciocínio** é UNIVERSAL — é estatística, não marketing de nicho. Os **números e
> a definição de MQL** são NÃO TESTADO FORA e são do nicho do caso-base. Em cliente novo, o método
> vem junto; a régua de MQL é construída do zero com a pesquisa dele.

> Base: L2 (3.300 respostas de pesquisa, 146 vendas) e L3 (5.454 respostas, 230 vendas), os dois do
> caso-base, cruzados por e-mail com venda real do Dash Fácil. Os lançamentos gratuitos do caso-base
> aparecem como **L1 a L4**, em ordem.
>
> Nível de confiança: **PADRÃO CONSISTENTE** para a parte de lead (replicou nos dois lançamentos).
> **PADRÃO INCONCLUSIVO** para a parte de criativo — e a seção 3 explica por que isso importa mais do
> que parece.

---

## 1. Como o MQL do Dash Fácil funciona (semântica)

O Dash monta o MQL selecionando respostas de uma a três perguntas da pesquisa. A composição é **E,
não OU**: se você seleciona duas perguntas, a pessoa precisa responder as duas com uma das respostas
marcadas. Responder uma certo e a outra errado **não** qualifica.

Consequência prática: cada pergunta adicionada **estreita** o público marcado. Errar isso muda toda
a leitura — uma regra que parece marcar 79% da base na verdade marca 27%.

## 2. MQL como qualificador de LEAD — o que replicou

Definição usada no caso-base: *já comprou curso do assunto* **E** *quer ser avisado de nova turma*.

| Regra | L2 conv / lift | L3 conv / lift |
|---|---|---|
| **comprou E aviso (atual)** | 4,59% / 2,07x | 6,20% / 2,42x |
| comprou (só) | 4,13% / 2,01x | 5,84% / 2,82x |
| comprou E renda na faixa de cima | 5,39% / 1,96x | 9,31% / 2,94x |
| comprou E superior | 4,68% / 1,91x | 7,03% / 2,90x |
| aviso (só) | 3,47% / 2,03x | 3,99% / 1,52x |

**O que é consistente nos dois lançamentos:**

1. **"Já comprou curso e não resolveu" é o sinal forte.** Aparece em toda regra de topo. Quem já
   gastou dinheiro e se frustrou compra mais que quem nunca comprou — a objeção "já comprei e não
   funcionou" é a assinatura do bom comprador, não um obstáculo.
2. **"Quer ser avisado" é sinal fraco isolado.** ~66% da base responde sim nos dois lançamentos — é
   resposta de educação. Só agrega quando combinado.
3. **A definição atual marca ~27% da base nos dois** e entrega lift ~2x. É uma régua bem calibrada:
   estreita o bastante pra ser útil, larga o bastante pra ter volume.
4. **Cruzar com renda ou escolaridade aumenta a precisão** mas encolhe muito o público (5–6% da base
   no caso da renda).

**Conclusão:** não há motivo nos dados para trocar a definição atual. Se o objetivo for uma lista
curta de alta prioridade (contato humano, recuperação de venda), `comprou E renda na faixa de cima`
é mais denso — mas isso é uma **lista**, não o MQL do painel.

## 3. MQL como sinal de OTIMIZAÇÃO DE CRIATIVO — não validado

Esta é a parte importante, e o resultado é negativo.

A pergunta era: durante a captação, a taxa de MQL por criativo prevê qual criativo vai vender mais?
Se previsse, daria pra cortar criativo ruim antes de a venda acontecer.

Correlação (Spearman) entre taxa de MQL do criativo e conversão real em venda, considerando **só
criativos pagos**:

| Lançamento | comprou E aviso | comprou | MQL do Dash |
|---|---|---|---|
| L3 (11 criativos) | **+0,427** | +0,291 | +0,173 |
| L2 (9 criativos) | **−0,517** | −0,600 | −0,600 |

**O sinal inverteu entre um lançamento e outro.** Não é uma diferença de magnitude — é troca de
direção.

### Por que isso acontece: o N é de criativos, não de leads

Teste de permutação (20 mil embaralhamentos), medindo que correlação o **puro acaso** produz:

| Nº de criativos | \|rho\| mediano do acaso | \|rho\| no percentil 95 | Chance de o acaso dar \|rho\| ≥ 0,43 |
|---|---|---|---|
| 9 | 0,250 | 0,683 | **25,0%** |
| 11 | 0,227 | 0,609 | **19,6%** |
| 14 | 0,196 | 0,538 | 12,9% |
| 25 | 0,139 | 0,395 | 3,4% |
| 40 | 0,109 | 0,307 | 0,5% |

Com 11 criativos, o acaso sozinho produz correlação de 0,43 ou mais em **1 de cada 5 tentativas**. Ou
seja: tanto o +0,427 quanto o −0,517 estão dentro do ruído. Nenhum dos dois é evidência de nada.

**A armadilha:** a pesquisa tem milhares de respostas, o que dá uma falsa sensação de robustez. Mas
quando o objeto de análise vira o **criativo**, o N cai de 5.454 para 11. É esse N que manda na
confiabilidade, não o outro.

### O que fazer na prática

- **Não use MQL para escolher o criativo campeão.** Diferença de 1–3 pontos percentuais de MQL entre
  dois criativos não decide nada.
- **MQL serve para descartar o desastre óbvio.** Um criativo com taxa de MQL muito abaixo dos demais
  (metade ou menos) é sinal de que atraiu público errado. Diferença pequena, ignore.
- **A decisão de matar criativo continua sendo por venda e CPA**, não por MQL.
- **Para tornar isso decidível no futuro:** acumular criativos entre lançamentos num único conjunto.
  Com 30–40 criativos pooled, a análise passa a distinguir sinal de ruído. Com 9–14 por lançamento,
  nunca vai.

### 3.5 TAXA de MQL e CUSTO por MQL são coisas diferentes — só a primeira está proibida aqui

> **Delimitação escrita a pedido do Rodrigo**, depois de descobrir que a rotina diária de otimização
> da casa tinha importado o §3 pro lugar errado e estava se recusando a ranquear criativo.

O que este §3 derruba é ranquear criativo por **taxa de MQL** (a % de qualificados) **como previsor
de venda** — e a razão continua de pé: o sinal inverteu de direção entre o L3 e o L2, e com 9–14
criativos o acaso produz essa correlação em 1 de cada 5 tentativas.

Isso **não** se estende a **custo por MQL** (gasto ÷ MQL projetado), que é outra métrica e outra
pergunta:

| | Taxa de MQL | Custo por MQL |
|---|---|---|
| O que é | % de qualificados entre respondentes | gasto ÷ (leads × taxa) |
| Pergunta que responde | "este criativo prevê venda?" | "onde a verba compra lead qualificado mais barato?" |
| Status | **não validado** — é o que este §3 derruba | **é a régua oficial de verba** (`sirius-scale/frameworks/trafego/_metodologia.md` §3.1) |
| No Dash | coluna % MQL (no MCP, `mql_percentual`) | é a bolinha 🟢/🔴 da coluna Potencial (no MCP, o campo `potencial`) |

**Ranquear criativo, campanha e público por custo por MQL é o procedimento padrão da operação.** O
que sobrevive do §3 pra esse uso é só o **piso de volume**: base fina não decide, só observa. Na
rotina diária da casa, esse piso era de 15 leads no nível de criativo e 30 no nível de campanha.

E vale o alerta que o próprio Rodrigo levantou ao fechar isso: como **custo por MQL = CPL ÷ taxa de
MQL**, dá pra ter ótimo custo por MQL com CPL péssimo, sustentado por uma taxa alta. Isso ganha
qualidade e perde volume — e o lançamento tem meta dos dois lados. Olhar as duas réguas juntas,
sempre.

## 3.6 Cruzar a pesquisa com o lead dá o PERFIL por criativo — *VARIAÇÃO ISOLADA*

**VARIAÇÃO ISOLADA** — montado no L4, um cliente, um lançamento. A mecânica do cruzamento é sólida
(medida); o valor preditivo ainda não foi validado contra venda deste lançamento.

A pesquisa de avatar e a lista de leads **casam por e-mail**: **92,9%** das respostas no L4. A
pesquisa mora numa planilha (Google Sheets, no caso); a lista de leads vem do Dash. Com o join, cada
resposta carrega junto a UTM que trouxe aquele lead — ou seja, dá pra saber **que tipo de gente cada
criativo atrai**.

Pelo MCP do Dash há um atalho: o `pesquisa_lancamento` aceita os filtros de UTM (campanha, conteúdo,
termo) e devolve a distribuição de cada resposta só dos leads daquela origem — o perfil por criativo
sem montar o cruzamento à mão. Só vêm as perguntas fechadas (medido num lançamento de um segundo
expert); o que depender de pergunta aberta continua no cruzamento por e-mail com a planilha.

Isso responde uma pergunta que custo por MQL não responde. Custo por MQL diz **qual** criativo
ganha; o perfil diz **quem** ele traz e **por que** ganha — que é o que vira briefing do próximo
criativo.

**Taxas históricas usadas pra projetar valor de perfil** (L3, pesquisa cruzada com venda real por
e-mail — **5.004 respostas únicas** na base do corte "já comprou", 4.817 na do corte por área; as
áreas são as respostas da pergunta "qual área você quer", com nome trocado por letra):

| Área desejada | Conversão | Já comprou curso? | Conversão |
|---|---:|---|---:|
| Área A | 4,4% | já comprou e não resolveu | **4,9%** |
| Área B | 4,3% | nunca comprou / só gratuito | 1,6% |
| Área C | 3,2% | | |
| Área D | 2,7% | | |
| Área E | 2,1% | | |

A segunda pergunta discrimina mais que a primeira — **3x contra 2x**. Quem já gastou e não resolveu é
o melhor comprador da base.

> **Correção de base registrada.** Este bloco chegou a descrever a base com um número de "respostas"
> que era, na verdade, da ordem de **leads** — e que nem como leads batia, nem tinha fonte em arquivo
> nenhum. A pesquisa do L3 tem 5.454 linhas e **5.004 e-mails únicos**; a lista de leads do Dash tem
> 7.139 leads, dos quais 4.717 responderam. As taxas da tabela foram reconferidas contra os três arquivos
> (leads, pesquisa e vendas) e **se sustentam** — reproduzem na ordem e na ordem de grandeza (uma das
> áreas bate no decimal). O que estava errado era o rótulo da base, não as taxas. Lição: base de taxa
> se declara pelo que ela é (respostas únicas, leads ou submissões) e com a fonte.

**Duas ressalvas que não podem sumir da entrega:**

1. **É projeção de outro lançamento.** A conversão real do L4 só existe depois que o carrinho fecha.
   Serve pra ordenar perfil, nunca como previsão de venda.
2. **O spread dentro da mesma plataforma é estreito** (~2,6% a 3,0% no L4). Não decide verba. Entre
   plataformas é mais claro e vale como reforço — e aí cai no uso autorizado do §3 (comparar canal,
   não ranquear criativo).

### 3.6.1 O score é cego pra uma área inteira (a área B) — *VARIAÇÃO ISOLADA*

**VARIAÇÃO ISOLADA** — L4. Cruzando a faixa de score (A/B/C/D, que é o que decide corte de verba por
perfil) com a área desejada (pesquisa) e a conversão real do L3 por área:

| Área | N | A+B | Conversão L3 |
|---|---:|---:|---:|
| Área A | 824 | **67,4%** | **4,4%** |
| Área C | 629 | 45,5% | 3,2% |
| Área E | 1.777 | 44,6% | 2,1% |
| **Área B** | **386** | **29,8%** | **4,3%** |
| Área D | 1.883 | 28,2% | 2,7% |

A área A bate nos dois eixos (melhor A+B, melhor conversão) — score e venda concordam. **A área B
não**: 2ª melhor conversão da tabela (4,3%, atrás só da A), mas 2º pior A+B (29,8%, quase empatado
com o pior). O score de lead **subestima sistematicamente quem quer a área B** — decisão de verba que
corta por faixa A/B sozinha corta um perfil que, pela conversão real do lançamento anterior,
converte quase tão bem quanto o melhor.

⚠️ Conversão é do L3 (lançamento anterior); score é do L4 (lançamento atual) — é comparação entre
bases, não medição direta. Confirmar com a conversão real do L4, disponível só depois do carrinho.

**Como aplicar:** ao decidir corte de verba por faixa de score, checar se a unidade cortada tem
concentração do segmento que converte bem com score baixo (no caso-base, a área B) antes de tratar
A+B baixo como sentença — pode estar julgando um perfil bom pela métrica errada.

## 3.7 Ranquear criativo por MQL: o N depende da PERGUNTA, e o teste decide

> **Delimitação levantada pelo Rodrigo** e verificada com teste de proporções no L4. Estreita o
> alcance do §3 — não o derruba.

O argumento do Rodrigo: *"a gente quase não segmenta público, nem na Meta nem no Google; as
campanhas são muito similares, então a diferença é o criativo."* Ele está certo, e isso tem
consequência metodológica. Com Advantage+ dos dois lados, mesmo público amplo e mesma estrutura, o
criativo é praticamente a única variável que muda — a atribuição causal fica muito mais limpa do que
num setup segmentado.

**O erro que isso corrigiu:** o §3 mede a correlação entre o *ranking de MQL* e o *ranking de venda*,
e ali o N é o número de criativos (~11). Mas "o criativo C1 traz mais MQL que o C2?" é outra
pergunta, e o N dela é o número de **leads**. São escalas diferentes, e importar a objeção de uma pra
outra proibia comparação que o dado sustenta com folga.

**Medido no L4, taxa de MQL sobre respondentes** (C1 a C4 são quatro criativos da captação):

| Par | Taxas | Diferença | z | Veredito |
|---|---|---:|---:|---|
| C1 x C2 | 27,9% x 18,1% (n=365 e 360) | 9,9 pp | **3,16** | real, p<0,002 |
| C1 x C3 | 27,9% x 21,0% | 6,9 pp | 1,92 | ruído |
| C1 x C4 | 27,9% x 20,2% | 7,8 pp | 1,59 | ruído |
| C3 x C4 | 21,0% x 20,2% | 0,8 pp | 0,17 | ruído |

**O ranking separa os extremos e não separa o meio.** C3, C2 e C4 são empate técnico entre si.
Ordenar 1º-2º-3º e tratar as posições como reais seria inventar precisão que o dado não tem.

### A regra prática

1. **Ranquear por MQL: pode.** Ordenar a lista é barato e informa.
2. **Afirmar que um criativo qualifica mais que outro: só passando no teste** (z de duas proporções,
   |z| > 1,96). Na rotina da casa isso virou uma coluna de veredito no relatório — `<` é pior de
   verdade, `=` é empate técnico. Peça o mesmo ao Claude quando ele ranquear criativo pra vocês.
3. **O teste substitui o piso arbitrário de volume**, e melhor: ele já embute o N. Base pequena não
   passa no teste sozinha, sem precisar de corte fixo.
4. **Corte por custo continua valendo mesmo em empate técnico** — são coisas diferentes. Um criativo
   com `=` e custo por MQL ~4,5× o do melhor é cortado por CUSTO, e a entrega tem que dizer isso, não
   alegar qualidade pior.

### O que do §3 continua de pé

Nada aqui valida MQL como **previsor de venda**. Aquilo foi testado em dois lançamentos e o sinal
inverteu. "Melhor por MQL" ≠ "vai vender mais" — e no L4 só dá pra saber depois que o carrinho
fecha. O que o §3.7 autoriza é afirmar **qualidade de lead**, que é o que o MQL mede de fato.

## 3.8 Projetar FATURAMENTO pelo mix da base: o modelo de lift por segmento — *VARIAÇÃO ISOLADA (1 calibração, 1 validação)*

> Construído no L4, a pedido do Rodrigo, com a captação ainda aberta.

Isto **não** contradiz o §3. O §3 proíbe usar MQL pra prever qual CRIATIVO vai vender (N = número de
criativos, ~11). Aqui a unidade de análise é a BASE INTEIRA (N = milhares de leads), que é
exatamente o uso que o §2 marca como CONSISTENTE. São perguntas diferentes com N diferentes — a regra
do §4.

### O método, em 4 passos

1. **Calibrar** num lançamento fechado: cruzar leads × vendas por e-mail e medir a conversão de cada
   segmento (MQL Sim/Não/sem resposta; faixa A/B/C/D).
2. **Corrigir o casamento por e-mail.** No L3 só 165 das 230 vendas casaram com um lead. As taxas
   medidas subestimam ~28%. O modelo redistribui as vendas órfãs na proporção das casadas (fator =
   vendas totais ÷ vendas casadas; 1,3939 no caso), de modo que o modelo reproduza o total real.
   **Premissa declarada**, não fato: assume que venda sem lead casado se distribui como as demais.
3. **Converter taxa em LIFT** (segmento ÷ conversão global do lançamento). O que viaja entre
   lançamentos é o lift; a taxa absoluta não.
4. **Aplicar o lift ao mix do lançamento novo** → índice de qualidade da base →
   `conversão projetada = conversão global do lançamento-base × índice`.

### Lifts medidos (L3, corrigidos)

| Por MQL | Lift | | Por faixa | Lift |
|---|---:|---|---|---:|
| Sim | 2,35x | | A | 4,12x |
| Não | 0,94x | | B | 1,66x |
| Não respondeu | 0,39x | | C | 0,86x |
| | | | D | 0,38x |
| | | | Sem faixa | 0,39x |

**Os dois modelos convergem.** No L4 (4.654 leads, no meio da captação) o índice deu 0,951 por MQL e
0,940 por faixa — campos diferentes, mesma resposta. Convergência é o melhor sinal de que o modelo
não está inventando.

### O erro do modelo é conhecido: **+11,5%**

Validação fora da amostra — lifts do L3 aplicados na base do L2: previu 163 vendas, foram 146. **O
modelo erra pra cima.** Toda entrega tem que trazer o cenário conservador = central × 0,885, e chamar
ele pelo nome: é o erro medido, não pessimismo.

### Regras de uso

- **Só vale no nível da base, campanha ou plataforma** — nunca no nível do criativo (§3 continua
  valendo inteiro).
- **Sempre rodar os dois modelos** (MQL e faixa). Se divergirem mais que ~3 pontos de índice, tem
  algo errado na lista de leads — não escolha o que você prefere.
- **Sempre publicar as três faixas** (conservador / central / otimista) e o ticket nas duas bases
  (Dash e contratado, `sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`). Número
  único vira promessa.
- **Depende do §4.4 de `sirius-scale/frameworks/trafego/leitura-dash-facil.md`** (score não
  amadurece). Se aquilo cair, a projeção com base em captação cai junto.
- A conversão histórica **inclui o downsell** (21 das 230 vendas do L3). Se o desenho do downsell
  mudar, essa parcela muda.

## 3.9 Score e custo por MQL não diferenciam PLATAFORMA — só diferenciam DENTRO dela · *VARIAÇÃO ISOLADA*

**VARIAÇÃO ISOLADA** — L3. Cruzamento de 230 vendas com 7.139 leads por e-mail (159 casaram), aberto
por plataforma:

| plataforma | leads | respondentes | MQL% | A+B%* | vendas | **conversão real** |
|---|---:|---:|---:|---:|---:|---:|
| Google | 2.730 | 1.779 | 27,2% | 44,7% | 60 | **2,20%** |
| Meta | 3.885 | 2.533 | 23,7% | 44,0% | 49 | **1,26%** |

*A+B sobre quem TEM faixa (regra de `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.1).

A diferença de conversão é real (teste z de duas proporções: z=2,95, p=0,003) — o Google converteu
**75% mais**. Mas **A+B é praticamente idêntico** entre as duas (44,7% x 44,0%, 0,7 ponto) e o MQL%
tem um gap pequeno (3,5 pontos) que não chega perto de explicar 75%.

**Isso não contradiz o §3.7.** Dentro do L3, o score continua prevendo venda com gradiente de 10x
entre faixas (A 9,13% até D 0,88% — §3.6.1). O que este item mostra é um eixo diferente: o mesmo
score que separa bem faixas *dentro* de uma plataforma fica **cego** quando a pergunta muda pra "qual
plataforma traz o comprador".

**Por que isso importa pra decisão de verba:** custo por MQL e % faixa A+B são os dois indicadores da
régua de otimização (`sirius-scale/frameworks/trafego/_metodologia.md` §3.1) — e são exatamente os
que este item mostra não terem autoridade sobre split entre plataformas. Ranquear campanha *dentro*
de uma plataforma por eles continua valendo (é o uso normal da régua). Decidir se sobe Meta ou Google
**usando esses dois indicadores** não tem base — nem pra favorecer, nem pra provar que não faz
diferença.

**O que teria autoridade aqui, e já está registrado:** a conversão projetada por perfil de pesquisa
(§3.6) e a conversão real medida — o §3.6 já dizia que "entre plataformas [a projeção] é mais claro e
vale como reforço", exatamente porque é outro indicador, calibrado em venda, não em score. Este item
só fecha o porquê o score não serve pro mesmo papel.

**O que não dá pra concluir daqui:** por que o Google converte mais — o dado não separa leilão,
qualidade de tráfego, página de destino ou atribuição. Só diz que não é o score que explica.

Fonte: o debriefing comparativo de L1, L2 e L3 (conversão e score por plataforma, já auditados) e um
recorte de MQL% e A+B% por `utm_medium` na lista de leads do L3 (evidência no caso de origem).

## 3.10 No lançamento pago (LPSG), o MQL da pesquisa de comprador prevê fraco a venda do programa principal · *PADRÃO INCONCLUSIVO*

**PADRÃO INCONCLUSIVO** — 1 cliente, turmas do lançamento pago de um mesmo mês. No LPSG o "lead" é
quem já pagou o ingresso, e a pesquisa (Tally na página de obrigado) é respondida depois da compra.
MQL do Dash = "já comprou curso do assunto e não resolveu" **E** "quer ser avisado da nova turma do
programa principal" (a regra do Dash com duas perguntas é **E** — conferido em 32 de 32
respondentes).

Dos 377 compradores de ingresso que tinham respondido até a leitura, compraram o programa principal:

| Corte | Sim | Não | z |
|---|---:|---:|---:|
| MQL (regra E) | 16,4% (23/140) | 10,1% (24/237) | **1,79** |
| Regra OU | 12,8% | 10,8% | 0,46 |
| Só "quer ser avisado" | 14,3% | 9,4% | 1,40 |
| Só "já comprou curso" | 13,6% | 11,0% | 0,73 |
| Renda na faixa de cima | 16,4% | 10,7% | 1,53 |

Lift de 1,6× no limite da significância (p ≈ 0,07). **Uso:** desempate entre unidades de custo
parecido, nunca régua principal — no LPSG a régua é custo por ingresso real e líquido
(`sirius-scale/frameworks/lancamentos/lpsg.md`). Cartões gerais de taxa de resposta e MQL do Dash
ficam errados quando a planilha da pesquisa é compartilhada entre turmas
(`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §8.3). Fonte: a análise de tráfego de uma
turma do lançamento pago (evidência no caso de origem).

## 3.11 Achar o qualificador do nicho: testar cada resposta contra o resto · *VARIAÇÃO ISOLADA* (segundo nicho, 11/2026)

Medido em lançamentos gratuitos de outro nicho.
1. **O MQL como qualificador de lead se repetiu** somando lançamentos; lançamento a lançamento, nem sempre separou
   sozinho.
2. **Uma resposta sozinha separou mais que o MQL inteiro.** Testando cada resposta da pesquisa contra o resto, por
   lançamento, uma delas (ligada ao momento de vida do avatar) converteu bem acima do resto em todos os lançamentos,
   com uma fatia grande da base.
3. **Pra escolher criativo, a fatia dessa resposta que cada anúncio traz previu venda melhor que o MQL% dele**
   (pesquisa filtrada por `utm_term`). Reforça a §3: o substituto do MQL% por criativo é a fatia da resposta que mais
   separa no lead, medida por anúncio.

**O que transfere:** o método (testar cada resposta contra o resto, por lançamento, e usar a que separa como MQL e como
régua de criativo). **O que é do caso:** qual resposta separa muda de nicho pra nicho.
## 4. Regra geral que sai daqui

> **MQL de qualificação de lead e MQL de otimização de criativo são perguntas diferentes, com N
> diferentes, e não devem ser respondidas com a mesma análise.**

- Qualificar lead: N = milhares de respostas. Estável, replica, dá pra confiar.
- Otimizar criativo: N = número de criativos, quase sempre abaixo de 15. Não dá pra confiar sem
  juntar vários lançamentos.

Antes de tirar conclusão de qualquer corte, pergunte **qual é o N da unidade de análise** — não o N
da base. Foi exatamente esse erro que quase virou uma recomendação errada de trocar a régua de MQL.

## 5. Ressalvas de dado

- 71 das 230 vendas do L3 não casaram com lead por e-mail (159 casaram); no L2, 95 de 146. A direção
  dos cortes é confiável; os absolutos subestimam.
- O campo `temperatura` do Dash está inconsistente no L3 (leads `cold` converteram mais que `hot`).
  Não usar para decidir.
- A faixa do score veio vazia no export do L2 — a análise por faixa de score só existe para o L3.
- O L1 não entra nesta análise: as vendas exportadas não têm UTM nenhum (66 vendas, todas sem
  `utm_id`), e não há lista de leads.
- O Dash só registra a primeira parcela de venda em boleto parcelado — todo faturamento aqui está
  subestimado.

---

## 6. O que transfere e o que é do caso

Este arquivo é o mais "estatístico" da biblioteca, e por isso o corte é mais limpo que nos outros:
**o raciocínio viaja inteiro, os números não viajam nenhum.**

**Transfere pra qualquer cliente/negócio:**

- **§4, a regra geral** — perguntar qual é o N da *unidade de análise*, não o N da base. É o item
  mais transferível da biblioteca inteira. Vale pra criativo, campanha, público, e-mail, o que for.
- **§1, a semântica do MQL no Dash** — composição por **E**, cada pergunta adicional estreita o
  público. É comportamento do produto, vale pra qualquer conta que use a ferramenta.
- **§3, a armadilha** — base grande não salva análise cujo objeto é um item de N pequeno. E o teste de
  permutação como forma de medir o que o acaso produz.
- **§3.5, a distinção** taxa de MQL x custo por MQL: perguntas diferentes, status diferentes. Junto
  com o alerta de que `custo por MQL = CPL ÷ taxa`, então ótimo custo por MQL pode esconder CPL
  péssimo — olhar as duas réguas.
- **§3.7, o procedimento** — ranquear pode; *afirmar* que um qualifica mais que outro exige teste z
  de duas proporções (|z| > 1,96); o teste substitui piso arbitrário de volume porque já embute o N;
  corte por custo vale mesmo em empate técnico, e a entrega tem que dizer que cortou por custo, não
  alegar qualidade pior.
- **§3.8, o método em 4 passos** — calibrar em lançamento fechado, corrigir o casamento por e-mail
  (declarando a premissa), **converter taxa em lift**, e aplicar o lift ao mix novo. A frase-chave já
  está escrita lá e é exatamente a regra de transferência: *o que viaja entre lançamentos é o lift; a
  taxa absoluta não.* Junto com as regras de uso: rodar os dois modelos e desconfiar se divergirem,
  publicar as três faixas, nunca no nível do criativo.
- **§3.9, a distinção** — score e custo por MQL rankeiam bem dentro de uma plataforma e não têm
  autoridade sobre split entre plataformas. É consequência do mesmo raciocínio do §3.7 (N depende da
  pergunta), aplicado a mais um nível.
- **§5, o hábito** de listar ressalva de dado antes de concluir.

**Não transfere — é do caso-base e do nicho dele:**

- **A definição de MQL** (*já comprou curso* **E** *quer ser avisado*). Essa é a régua do caso-base.
  Em cliente novo, as perguntas da pesquisa são outras e a composição precisa ser medida de novo. O
  que transfere é *como escolher*: a pergunta que discrimina mais é a que separa quem já gastou
  dinheiro no problema de quem nunca gastou — isso é hipótese forte pra testar primeiro, não regra
  pronta.
- **Todos os lifts e taxas** (2,35x MQL Sim; 4,12x faixa A; as conversões por área). Nicho puro.
- **O erro do modelo, +11,5%**, e o fator de correção 1,3939. São medidos na base do caso-base;
  cliente novo precisa da própria validação fora da amostra antes de publicar cenário conservador.
- **Os pisos de 15 leads (criativo) e 30 leads (campanha)** — e, de todo modo, o §3.7 já os torna
  secundários em favor do teste z.
- **As ressalvas de dado do §5** são daqueles exports (campo `temperatura` inconsistente, faixa vazia
  no L2, L1 sem UTM).

**Cuidado ao levar pra outro negócio:** a base inteira é de um cliente de **infoproduto de educação,
com pesquisa de avatar respondida em volume**. Cliente sem pesquisa em volume não tem MQL nenhum pra
calibrar — aí a régua de verba volta pro CPA real (`sirius-scale/frameworks/trafego/_metodologia.md`
§3.1, camada do meio) até existir base. Não force MQL onde não há pesquisa.
