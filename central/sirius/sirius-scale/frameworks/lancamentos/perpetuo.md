# Framework — Perpétuo (operação contínua de funil)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered dos perpétuos que a casa montou e tocou num período de cerca de seis meses: dois de
infoproduto com número (experts A e B), um de SaaS, dois em montagem (experts C e D) e o que o Rodrigo
disse sobre como roda perpétuo em sete calls. Escrito no fim desse período.

> **ALCANCE: TESTADO EM 2 CLIENTES (proposto, a confirmar pelo Rodrigo)** (os experts A e B) nas seções
> cujo título traz os dois. Os dois são do mesmo nicho técnico: o que
> o §7 trata como transferível ainda não foi testado fora desse nicho. O resto é **NÃO TESTADO FORA**: o
> funil de SaaS (assinatura com teste grátis, de outra empresa da casa) entra só na leitura e no
> desligamento; os dois perpétuos em montagem (C, VSL de um livro; D, low ticket) entram só em preço e
> produção. Nenhum perpétuo de infoproduto da casa tem rotina de leitura rodando.
>
> **Força:** no título de cada seção. *CONSISTENTE (proposto)* quer dizer que repetiu em 3 ou
> mais unidades desta base; promover a CONSISTENTE de verdade é decisão do Rodrigo
> (`sirius-scale/REGRAS.md` §4). Quase tudo que está marcado assim é **prática repetida**, não resultado
> validado: o único perpétuo com gasto e venda na mesma base é o do B.
>
> **Quem é quem neste arquivo:** A, B, C e D são quatro experts de infoproduto atendidos pela casa (as
> letras são as mesmas de `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md`). "O funil de SaaS" é
> um produto de software por assinatura de outra empresa da casa.

## 0. Resumo

1. Perpétuo é o motor de quem não produz conteúdo: grava uma vez (VSL, criativos, upsell,
   downsell) e depois só criativo novo. Quem produz conteúdo roda perpétuo junto com lançamento.
2. O funil mora em `funis/<nome>/`, sem data, e o `desempenho.md` faz o papel do debriefing,
   só que contínuo.
3. Antes de produzir, mede o ponto de partida, isolando o que é de lançamento ou de outro
   produto na mesma conta. Nos três perpétuos que rodaram, a primeira leitura misturou o funil
   com outra coisa e saiu errada.
4. A matriz de preços é a fonte única do número. O que muda durante a vida do funil (preço,
   parcela, botão, nome de aluno, mercado) fica fora do corpo gravado.
5. Liga baixo, lê em duas janelas (a curta pra alerta, o mês pra decisão), renova criativo
   antes de o atual morrer e pausa quando o mês vai pro prejuízo, depois de conferir a medição.

## 1. Escopo e base de evidência

### 1.1 Fontes (o que cada uma contém, quantas unidades e quanto pesa)

| Fonte | O que é | Unidades | Peso |
|---|---|---|---|
| **A** · expert A | os arquivos do funil (briefing, desempenho, matriz de preços, banco de ângulos, plano de produção, análise da VSL e dos hooks, achados da frente do outro mercado), a análise do perpétuo, recortes de duas reuniões e o README do cliente (evidência no caso de origem) | 1 perpétuo rodando havia mais de um ano (centenas de vendas aprovadas, base Dash), frentes em dois mercados; 7 arquivos do funil | forte: decisões do Rodrigo registradas no dia do plano de produção (na matriz, no plano e no banco); correções dele no mesmo dia; uma decisão dele duas semanas e meia depois |
| **B** · expert B | os arquivos do funil (briefing, desempenho), o debriefing do perpétuo, o checklist de montagem do funil e atas de seis calls (evidência no caso de origem) | 1 perpétuo, no ar por cerca de quatro meses, depois pausado; religar foi combinado numa call pra começar no dia seguinte, não conferido na conta de anúncios (ROAS acumulado de 2,19 no período inteiro, com o imposto da Meta no gasto) | forte no debriefing e nas decisões de call; médio no checklist (documento interno, sem registro de aprovação) |
| **C** · expert C | o funil de VSL de um livro (README, briefing) | 1 perpétuo de VSL em montagem, duas frentes; não rodou | forte nas decisões de preço, escassez e gravação (Rodrigo, em três dias seguidos); sem resultado |
| **D** · expert D | o briefing do perpétuo de low ticket e a ata de uma call | 1 perpétuo de low ticket em planejamento | decisão de call; sem execução |
| **E** · funil de SaaS | o desempenho do funil, o diagnóstico e a rotina de leitura dia sim, dia não | 1 perpétuo de SaaS (pouco mais de duas semanas no ar; depois a rotina passou a ler uma campanha nova); 1 rotina | forte na leitura e no desligamento (decisão do Rodrigo; rotina combinada com ele); o produto é assinatura com teste grátis, não infoproduto |
| **F** · falas do Rodrigo | atas com transcrição: duas calls com o gestor de um projeto, uma com a equipe, uma com a gerente de operação, uma com um prospect, uma com dois prospects de outro nicho e uma consultoria | 7 calls | forte como declaração de método; não é resultado |
| **G** · distribuição de conteúdo do expert C | o desempenho do funil de distribuição e a rotina semanal dele | 1 funil contínuo (não é perpétuo de venda) | entra só como segunda prova do formato do `desempenho.md` e da rotina |
| **H** · vizinhos | `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7, `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md`, `sirius-scale/frameworks/trafego/_metodologia.md` §6, `sirius-scale/frameworks/trafego/nomenclatura.md`, `sirius-scale/frameworks/lancamentos/low-ticket.md`, `sirius-scale/frameworks/lancamentos/produto-de-entrada.md`, `sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md`; os irmãos escritos no mesmo dia: `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md`, `sirius-scale/frameworks/lancamentos/diagnostico-de-operacao.md`, `sirius-scale/frameworks/pesquisa/pesquisa-e-avatar.md`, `sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md` e o de coprodução e parceria (não faz parte deste kit); correções já registradas pela casa | — | regra já escrita; aqui só citada |

Deduplicado: a mesma reunião aparece no recorte do projeto e na ata completa; contei uma vez.

### 1.2 Excluído de propósito

- **Montagem do banco de ângulos, pesquisa e avatar**: `sirius-scale/frameworks/pesquisa/pesquisa-e-avatar.md`
  (§3.11 e §3.12). Aqui entra só o uso do banco no perpétuo (§3.5).
- **Escrita, gravação e edição da VSL e dos hooks**: `sirius-scale/frameworks/copy/producao-de-vsl.md`,
  `sirius-scale/frameworks/lhto.md`, `sirius-scale/frameworks/copy/great-leads.md`,
  `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`.
- **A escada e a lógica de oferta do upsell e do downsell** (degraus, preço relativo, tese, blocos,
  script, medição por oferta): `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md`. Aqui entra só a
  matriz como fonte do número (§3.4).
- **Limpar e delimitar o dado de uma operação que a casa não montou** (as armadilhas de painel,
  CNPJ, venda de teste, UTM): `sirius-scale/frameworks/lancamentos/diagnostico-de-operacao.md` Passos 2 a 8.
  Aqui entra o que fica gravado no `desempenho.md` do funil (§3.3).
- **Mecânica de low ticket** (ticket baixo, order bumps, página de 13 blocos, réguas):
  `sirius-scale/frameworks/lancamentos/low-ticket.md`. Valor por comprador:
  `sirius-scale/frameworks/lancamentos/produto-de-entrada.md`.
- **Telas, API e configuração do Dash de perpétuo**: `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.
- **Distribuição de conteúdo**: `sirius-scale/frameworks/conteudo/conteudo-que-alimenta-o-funil.md`.
- **LPSG**, que tem comportamento de perpétuo mas ciclo semanal: `sirius-scale/frameworks/lancamentos/lpsg.md`.
- **Parceria e coprodução** (split, fixo mais percentual, contrato, quem paga o tráfego,
  compromisso de gravação no contrato): o que as calls falam de modelo de negócio fica fora (os
  frameworks de coprodução e parceria e de remuneração e escopo não fazem parte deste kit).
- **Pós-compra, entrega, suporte e a causa do reembolso**:
  `sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md`.
- **O SaaS como produto** (teste grátis, onboarding, fluxo de e-mail do trial): fora do público de
  infoproduto. Entram só a rotina de leitura e o desligamento.
- **Roteiros do B**: vieram de um projeto do próprio expert no Claude, sem edição, e não se sabe
  qual versão está no ar. Fracos; só a lista de erros do briefing entra (§3.4).
- **Prática de terceiros citada nas calls** (benchmark com outro coprodutor, imersões que o gestor
  de um projeto assistiu, exemplos de mercado numa consultoria): não é o que a casa faz.
- **Números de caixa da casa** citados numa ata: irrelevantes aqui e sensíveis.

### 1.3 Base: ressalva estrutural

- **Três perpétuos rodaram com número, de três empresas**: A, B e o funil de SaaS. Só dois são de
  infoproduto. Dois outros estão em montagem (C, D).
- **Só o B tem gasto e venda na mesma base.** O A tem venda sem gasto (a conta de anúncios só foi
  conectada no dia do plano de produção, e o ROAS dele nunca foi calculado nos arquivos do funil). O
  SaaS tem gasto sem venda do produto.
- **Nenhum perpétuo de infoproduto tem rotina de leitura rodando.** A única rotina de perpétuo é a
  do SaaS, e as duas primeiras rodadas dela morreram no primeiro comando (§8, item 10).
- **O que está CONSISTENTE (proposto) é decisão e prática que se repetiram**, quase sempre sem
  medição do efeito. Onde há efeito medido, é de um funil só e está marcado ISOLADA.

### 1.4 Veredito da extração (FASE 1 de `sirius-scale/frameworks/_extracao-de-frameworks.md`)

| Parte do artefato | Unidades | Funis / clientes | Aprovação | Resultado | Veredito |
|---|---:|---|---|---|---|
| Decidir que é perpétuo | 3 decisões + 4 falas | A, B, D | sim (call) | parcial | EXTRAÍVEL FORTE |
| Pasta e briefing | 5 pastas, 4 briefings | A, B, C, D, SaaS | parcial | — | EXTRAÍVEL FORTE |
| `desempenho.md` | 4 arquivos | A, B, SaaS, distribuição | sim (debriefing usado na proposta ao B; SaaS desligado pelo Rodrigo) | sim | EXTRAÍVEL FORTE |
| Matriz de preços | 1 arquivo + 2 seções | A, C, B | sim (decisões do Rodrigo) | não | EXTRAÍVEL COM RESSALVA |
| Banco de ângulos no perpétuo | 1 arquivo + 1 ranking | A, B | sim | parcial | EXTRAÍVEL COM RESSALVA |
| Plano de produção | 1 completo + 1 parcial + 1 cadência semanal | A, C, B | sim | não | EXTRAÍVEL COM RESSALVA |
| Rotina de leitura | 1 rotina (SaaS) + 1 contínua de conteúdo + 4 falas | SaaS, distribuição | sim | — | FRAGMENTO pra infoproduto; descrita como VARIAÇÃO ISOLADA |
| Matar, pausar, escalar, renovar | 3 decisões + 5 falas | B, SaaS, A | sim | sim (B) | EXTRAÍVEL FORTE |

**Veredito geral: EXTRAÍVEL FORTE** (dois clientes de infoproduto com perpétuo rodando, mais de
8 unidades), **com ressalva**: plano de produção e rotina de leitura têm base de um funil, e a
rotina nunca rodou num perpétuo de infoproduto.

## 2. A fórmula, em ordem

1. **Decidir que é perpétuo** e de que tipo: VSL com escada ou low ticket de página escrita.
2. **Abrir a pasta `funis/<nome>/` e o briefing**, com um bloco do que não está definido.
3. **Medir o ponto de partida no `desempenho.md`**, isolando o perpétuo do resto da conta.
4. **Fechar a matriz de preços**: escada, mercado, parcela do checkout. É a fonte do número de
   toda peça.
5. **Escolher os ângulos do lote** no banco de ângulos, com o que vendeu no próprio funil.
6. **Plano de produção**: o que gravar, em que ordem de dependência, em quantas sessões; o que
   muda fica fora do corpo gravado.
7. **Ligar o tráfego** baixo, com o Dash configurado e a conferência feita antes da verba.
8. **Ler** em duas janelas: a curta pra alerta, o mês pra decisão. A rotina lê e propõe.
9. **Decidir**: achar a etapa que vaza, renovar criativo, escalar pelo retorno marginal, pausar
   pelo mês.
10. **Registrar**: uma linha por período no `desempenho.md`; debriefing quando fecha um período.

**Os dois modos que se repetiram:**

- **VSL perpétuo** (A, B, C): criativo de conteúdo com chamada pra aula completa → VSL → front (o
  produto de entrada) → upsell de um clique → downsell.
- **Low ticket perpétuo** (D, e a linha de low ticket do C): página escrita, sem vídeo, produto
  ferramental. A mecânica é a do `sirius-scale/frameworks/lancamentos/low-ticket.md`; daqui valem os
  passos 2, 3, 7 a 10.

Os dois compartilham a pasta, o `desempenho.md`, a matriz, a leitura e os critérios de decisão.

## 3. As etapas (força marcada em cada uma: CONSISTENTE, ISOLADA ou INCONCLUSIVO)

### 3.1 Decidir que é perpétuo — PADRÃO CONSISTENTE (proposto) · A, B, D + 4 falas

**O que entra.** A pergunta é se o expert produz conteúdo e topa evento. Quem grava pouco e não
faz live vai pro perpétuo. Quem produz conteúdo roda perpétuo junto com lançamento, não no
lugar. Decide também o modo (VSL com escada ou low ticket) e o primeiro produto: o que está
mais pronto pra rodar.

**Por quê.** Lançamento pede conteúdo, lives e aquecimento que esse expert não entrega. Na leitura
do Rodrigo, os lançamentos daquele ano dos dois experts do mesmo nicho (A e B) pagaram o tráfego e
sobrou pouco, enquanto o funil de VSL vendeu. E o perpétuo de VSL distribui conteúdo enquanto vende,
porque o criativo é conteúdo: cresce a base de quem não posta.

**Variações aceitáveis.**
- Low ticket pra público frio quando ainda não existe VSL nem produto do meio (D).
- Produto de entrada que já existe vira front do perpétuo (o livro do B; o material físico de apoio do A).
- Pós-graduação no perpétuo, com time comercial: o Rodrigo afirmou em duas calls. Não rodou;
  fica como hipótese (§8).

**Trecho real.**
- "minha conclusão é, quem não faz conteúdo, velho, só faz sentido deixar no perpétuo, sem estresse
  de lançamento" — Rodrigo, numa call com um prospect
- "Aí, esses experts que não fazem conteúdo, a gente tá meio que rodando mais perpétuo, sabe?" —
  Rodrigo, numa call com dois prospects de outro nicho
- "Tem que ter perpétuo e lançamento. Só viver de lançamento é muito difícil hoje." — Rodrigo, numa
  consultoria
- "Então, rodar a VSL aumenta a base de seguidores, porque você está distribuindo conteúdo
  enquanto você vende." — idem
- "é pegar essas pessoas que tem potencial, mas não se dedica tanto, pra gente ficar rodando
  perpétuo" — Rodrigo, numa call com a equipe
- Decisão com o expert B: "Foco volta para o perpétuo e o low ticket, aproveitando o funil do
  livro que já funciona, em vez de novo lançamento gratuito." (evidência no caso de origem)
- Decisão no D: "O projeto começa pelo perpétuo, não por lançamento." (evidência no caso de origem)

### 3.2 Abrir a pasta e o briefing — PADRÃO CONSISTENTE (proposto) na pasta e no briefing · 5 pastas, 4 briefings · VARIAÇÃO ISOLADA no bloco do que não está definido

**O que entra.**
- Pasta `funis/<nome>/`, sem data. Quem roda os dois modelos tem as duas pastas (`lancamentos/` pro
  lançamento, datado; `funis/` pro perpétuo). No caso de origem, o produto da própria empresa (o SaaS)
  usava a mesma estrutura.
- `briefing.md` com: o que vende e em que ordem (o preço mora na matriz, §3.4), as páginas, onde
  o funil mora no Dash e, quando a casa escreve a VSL, a tese.
- Um bloco do que **não** está definido, escrito como pergunta: verba, meta, cadência, quem
  opera, validação do expert, qual versão está no ar. Como bloco próprio, só em 2 dos 4 briefings
  (A e D); o C tem as pendências do script no README; o B não tem bloco, só dois "não confirmado"
  soltos no texto.
- O briefing não carrega número de resultado: aponta pro `desempenho.md`.

**Por quê.** O agente lê arquivo, não a conversa: decisão que fica só na conversa não chega na
próxima peça, e o agente escreve em cima da versão velha. O que não está definido vira pergunta em vez
de chute (`sirius-scale/REGRAS.md` §2). No perpétuo isso pesa mais, porque a peça vive meses: um preço
ou uma versão errada no briefing contamina tudo que vem depois.

**Variações aceitáveis.**
- Briefing com a tese inteira (A: vilão, premissas, régua de crença).
- Briefing magro quando o funil chegou pronto (B: o que vende, o que tem na pasta e os erros
  conhecidos dos roteiros).
- Briefing de partida, antes de o expert validar (D).

**Trecho real.**
- "Perpétuo não tem edição datada: o funil é um só e evolui no lugar, então datar a pasta criaria
  histórico falso." — regra de estrutura da casa
- "O que este briefing NÃO define (perguntar antes de executar)" — título de seção no briefing do A;
  o item 1: "Não há orçamento, meta de faturamento nem CAC alvo em documento nenhum. Sem isso não dá
  pra montar plano de mídia."
- "O que falta antes de escrever qualquer peça" (título de seção), "Ainda não é um briefing
  pronto pra produção" e "Nada de promessa, preço ou tema sem essa validação." — briefing do D
- "Pendências do script da [frente 1] (antes de gravar)" — título de seção no README do C
- Sem bloco, solto no texto: "Qual versão de cada vídeo está no ar: não confirmado." — briefing do B

### 3.3 Medir o ponto de partida no `desempenho.md` — PADRÃO CONSISTENTE (proposto) · A, B, SaaS + distribuição

**O que entra**, antes de produzir peça nova (como limpar o dado está em
`sirius-scale/frameworks/lancamentos/diagnostico-de-operacao.md` Passos 2, 4 e 8; aqui é o que fica
gravado):
1. **Cabeçalho com a fonte** (arquivo e data) e a **base de faturamento** (Dash, contratado da
   Hotmart, bruto), e se o gasto tem o imposto da Meta. A base está escrita em 3 dos 4.
2. **Venda por mês e por produto ou frente**; com gasto, a **sobra** (faturamento menos taxa da
   plataforma e tráfego, antes de imposto de nota e de split) e o ROAS.
3. **O perpétuo isolado do resto da conta**: tirar o que é de lançamento, de outra porta de
   entrada ou de outro produto. Aconteceu nos 3 perpétuos que rodaram.
4. **Taxa de subida do front pro upsell, por oferta**, dizendo se é o upsell de um clique ou
   compra depois. No B, os 11,3% do debriefing (17 de 151) são 11 vendas pela oferta de
   upsell, 5 pela de downsell e 1 pelo preço cheio, cerca de 87 horas depois da compra do livro
   (`sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.15). No A, o 7,7% cruza e-mail de
   comprador dos dois produtos sem janela e junta o upsell com compra em lançamento.
5. **Rastreio**: quanto da venda tem UTM e o que está quebrado. Nos 3 perpétuos o rastreio
   cegava parte da leitura (A, 26% sem `utm_source`; B, 21% sem `utm_term`; SaaS,
   nenhuma venda com UTM de tráfego pago).
6. **Reembolso por produto** e por mês quando sobe (método da causa em
   `sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md` §3.10), tempo de carregamento da
   página e o criativo que vendeu.
7. **Pontos em aberto do próprio arquivo**: o que o dado não responde.

**Por quê.** Sem o ponto de partida, a produção vai pra alavanca errada. No A, a queda de 86%
do funil da VSL era o criativo de venda direta contado junto; separado, a VSL estava estável. No
SaaS, a tela mostrou ROAS 13,21 no mês analisado com vendas de outro funil, e o funil foi desligado
com um painel que media outro produto. O método do debriefing de perpétuo já existe
(`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §3, linha VSL/perpétuo); o da
tela do Dash também (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.2 a §7.5). Este passo é
aplicar os dois antes da primeira peça nova e deixar o resultado gravado no funil.

**Variações aceitáveis.**
- Retrato inteiro de uma vez (A); tabela mês a mês com link pro último debriefing (B); uma entrada
  por período, do mais novo pro mais velho (SaaS); histórico de apurações semanais (distribuição de
  conteúdo).
- Sem gasto, vale publicar só a venda, dizendo que não existe CAC nem ROAS (A).

**Trecho real.**
- "Todo número aqui é reproduzível a partir desses dois arquivos — nada foi estimado." —
  desempenho do A
- "Este arquivo é o debriefing contínuo do funil — uma linha por período analisado, do mais novo
  pro mais velho." — desempenho do SaaS
- "Cada apuração cita a pasta dados/ de onde saiu; número sem pasta não entra." — desempenho da
  distribuição de conteúdo do C
- "O [workshop] ([N] vendas, ticket baixo) é isca de lançamento e não faz parte do perpétuo —
  está aqui só pra fechar o total." — desempenho do A
- "As [N] vendas [do curso] [daquele mês] são do [lançamento que rodou na mesma conta] (quase todas
  em dois dias), não deste funil." — debriefing do B
- O mesmo erro, registrado como caso na leitura do Dash: as vendas eram do mesmo produto, vindas de
  outro funil (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.2)
- "A VSL não caiu 86%. Ela subiu." — análise da VSL e dos hooks do A
- "precisa dizer se é one-click com desconto ou compra posterior; a análise [anterior] trocou um
  pelo outro." — debriefing do B
- "Um quarto do faturamento não é atribuível." — desempenho do A

### 3.4 Fechar a matriz de preços — PADRÃO CONSISTENTE (proposto) · A, C, B

**O que entra.**
- Uma tabela por mercado: peça × produto × preço à vista × parcela, com a data e quem decidiu.
  Ela substitui qualquer preço anterior.
- Os degraus da escada (front, upsell de um clique, downsell; segundo upsell onde houver). A
  escada é a mesma nos 3 funis de VSL e a razão de cada degrau está em
  `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.1 a §4.3; a matriz guarda o número.
- A aritmética entre degraus, conferida antes de a copy afirmar proporção. Nos 3 funis o downsell
  tem metade do acesso; metade do preço, só em 1 (57% e 58% nos outros dois).
- A parcela tirada do checkout ou das vendas reais da conta, nunca de cabeça.
- As decisões que mudam o que é verdade na copy: o preço fora desta compra que vira âncora
  honesta, a âncora que não vale noutro mercado.
- A propagação: produto (`expert/produtos/<produto>.md`) primeiro, depois procurar o preço velho em
  todos os arquivos que o citam.

**Por quê.** O perpétuo roda meses e o preço muda no meio: no dia do plano, o upsell do A passou do
preço registrado pra 1,7 vez ele, com um terceiro preço rodando na página naquele dia. Roteiro com
número dentro envelhece: nos roteiros do B, a âncora do upsell e o preço do downsell não batiam
com a Hotmart. E no perpétuo o produto caro quase não vende cheio (no A, 21 das 25 vendas pelo preço
cheio caíram em janela de lançamento; no B, 1 dos 151 compradores do livro levou o curso pelo preço
cheio, cerca de 87 horas depois), então ele entra como upsell com condição. ⚠️ O debriefing do B diz o
contrário ("Nenhum comprador do livro comprou [o curso] cheio"); a contagem por oferta nos dados do
próprio debriefing acha essa uma venda, pelo preço cheio, no 3º mês do funil (conferido no dia da
extração; `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.15 chega nas mesmas 11, 5 e 1).

**Variações aceitáveis.**
- Mais de um mercado (A): uma tabela por mercado, sem parcelamento onde ele não existe, e a
  âncora de custo do problema só onde ela é verdade (no outro mercado ela saiu).
- Duas frentes com os produtos trocando de lugar (C): o preço cheio de uma frente é a âncora
  real do upsell da outra.
- Simetria de preço como decisão de margem: se a copy quer dizer metade, o preço tem que ser
  metade (no A, o downsell teria de cair de 58% pra 50% do upsell, nos dois mercados). VARIAÇÃO
  ISOLADA.

**Trecho real.**
- "Substitui qualquer preço anterior registrado no repo." — matriz de preços do A
- "O downsell NÃO é metade do upsell." — idem
- "Serve pra derivar parcela de qualquer preço novo deste cliente sem precisar abrir o checkout —
  mas conferir antes de gravar, porque tabela de gateway muda." — idem
- "neste cliente, o ticket [alto] vende com máquina de lançamento (lives, aquecimento, turma), não
  em perpétuo." — idem
- "A estrutura de duas frentes transforma a âncora interna do prompt de upsell em fato, não em
  argumento." — README do C
- No briefing do B, erros conhecidos, item 5: o roteiro anunciava um preço e uma parcela, e a oferta
  configurada na Hotmart era 14% mais cara, com outra parcela nas vendas (evidência no caso de origem)
- "O valor sai do fator medido nas vendas da própria conta, nunca de tabela" —
  `sirius-scale/frameworks/lancamentos/low-ticket.md` §10 (a mesma regra no low ticket)
- "[…], fora de lançamento, que é o valor do perpétuo mesmo" — Rodrigo ao expert C, sobre o preço de
  um curso

### 3.5 Escolher os ângulos do lote pelo banco — VARIAÇÃO ISOLADA · A, B

**O que entra.** A estrutura do banco (ângulos com evidência e status, proibidos com o porquê,
prova social com fonte, uma peça um ângulo) está em
`sirius-scale/frameworks/pesquisa/pesquisa-e-avatar.md` §3.11, e a regra de mantê-lo vivo em §3.12. No
perpétuo, o que muda é o uso:
- **O lote novo se distribui pelos ângulos com lastro**, com mais peças nos que venderam no
  próprio funil.
- **A venda do funil sobe ou derruba o status do ângulo**, dentro do banco, com data.
- **A decisão sai do desempenho atual**, não do histórico de outra época nem de outro funil.
- **O vocabulário de quem comprou fecha a peça** quando existe pesquisa de comprador; no
  perpétuo ela é possível porque há venda todo dia (raio-x do A, 37 compradores;
  `sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md` §3.9).

**Por quê.** No perpétuo o criativo morre e precisa ser reposto (§3.9); o banco é o estoque de
onde sai o próximo lote sem recomeçar a pesquisa.

**Variações aceitáveis.**
- Banco como arquivo próprio, com a distribuição do lote por ângulo no plano de produção (A).
- Ranking de venda por ângulo dentro do debriefing, virando a pauta do lote seguinte (B).

**Trecho real.**
- "Distribuição proposta pelos ângulos que têm lastro" — plano de produção do A
- "Hoje a VSL usa só o primeiro, do começo ao fim. Esse é o erro a não repetir." — banco de
  ângulos do A
- "Três ângulos fazem 84 das 144 vendas com termo." — debriefing do B; e o passo seguinte:
  "Gravar volume de criativo nos 3 ângulos que venderam (pelo menos 4/semana)" — idem
- "Decida pelo desempenho atual, não pelo histórico de [mês anterior]." — rotina do SaaS

### 3.6 Plano de produção — VARIAÇÃO ISOLADA no documento · PADRÃO CONSISTENTE (proposto) em três regras dele

**O que entra**, na ordem em que o plano do A foi escrito:
1. As decisões do Rodrigo já tomadas, no topo, com data.
2. A checagem da premissa: de que tráfego veio a taxa que vai virar meta. No A, a conversão
   da VSL era de seguidor do link da bio, e o plano proibiu construir meta em cima dela.
3. A tabela do que precisa ser escrito, em ordem de dependência, com o que está travado e por quê.
4. A distribuição do lote de criativos pelos ângulos (§3.5).
5. A divisão de ativo entre as peças (o que a VSL usa e o que fica pro upsell); o critério é do
   framework de upsell.
6. O que gravar e em quantas sessões.
7. O formato pro expert: só o que ele lê, separado da direção.
8. A ordem recomendada e o risco dela. O Rodrigo pode inverter; a inversão entra registrada.

**As três regras que se repetiram — PADRÃO CONSISTENTE (proposto):**

a) **A gravação do expert é o recurso escasso.** O plano minimiza sessão e o compromisso de
   gravar fica explícito. Dois clientes, sete registros (o plano do A, uma decisão do Rodrigo sobre o
   A e cinco calls com o B). O lado de contrato desse compromisso está no framework de coprodução e
   parceria (não faz parte deste kit).

b) **O que muda durante a vida do perpétuo fica fora do corpo gravado**: preço, parcela, texto do
   botão, nome de aluno, mercado e apelo a quem já conhece o expert. Seis decisões em dois funis
   (A e C), mais os erros de preço dos roteiros do B como prova do problema. Nas peças de upsell e
   downsell o detalhe está em `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.14. O efeito
   na conversão não foi medido: `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §0.1 segue
   INCONCLUSIVO pra gravação única em vários mercados.

c) **O criativo do perpétuo é conteúdo com uma chamada no fim**; no de VSL, a chamada é pra aula
   completa, que é a VSL. Três funis (A em dois lotes, B, C) e quatro falas do Rodrigo (em quatro
   calls, ao longo de cerca de três semanas). Os fechamentos de chamada do D ficam fora da conta:
   foram suspensos antes de rodar. Gravar o corpo uma vez e duas caudas, com chamada pro pago e sem
   pro orgânico, só o A fez: VARIAÇÃO ISOLADA.

**Por quê.** O expert de perpétuo é justamente quem grava pouco (§3.1); cada sessão perdida trava
o funil inteiro. E a peça gravada precisa sobreviver a meses de mudança de preço e de público:
o que muda e está dentro dela obriga a regravar. Pelo mesmo motivo, não se investe tempo criando
material novo pro expert enquanto ele não grava o que falta.

**Variações aceitáveis.**
- Testar o ângulo no anúncio antes de gravar a VSL (`sirius-scale/frameworks/lhto.md` §5.7, o que o
  plano propôs) ou gravar tudo de uma vez (o que o Rodrigo decidiu no mesmo dia).
- Pacote semanal pronto pro expert só gravar (B, decisão do Rodrigo).
- Estático de venda direta apontando pra página escrita, sem VSL: foi o maior faturamento da conta
  do A em frio, e a frente do outro mercado vendeu assim sem nunca ter VSL. VARIAÇÃO ISOLADA (uma
  conta), mas ali é o caminho provado e a VSL é a aposta: mantém os dois rodando.

**Trecho real.**
- "O recurso escasso aqui é o tempo de gravação do [expert] — é a própria razão de a base crescer
  devagar. Então o plano minimiza sessões." — plano de produção do A
- "Em ordem de dependência. O que está travado não pode começar." — idem
- "Nenhuma meta deve ser construída sobre esse número." — idem
- "Não vamos testar criativos antes de gravar a VSL: escreve e grava tudo hoje." — idem (decisão do
  Rodrigo)
- "Peça 2 — depende do que a peça 1 gastou (o upsell não repete argumento, depoimento nem número
  da VSL)." — briefing do C
- "a gente promete gerar um resultado e você promete gravar com constância, tipo assim,
  principalmente criativo, sabe?" — Rodrigo ao expert B
- "senão amarra a peça a um público que acaba e obriga a regravar." — plano do A
- "nenhum nome de aluno na fala da copy (só nos marcadores de produção), pra trocar depoimento sem
  regravar" — README do C
- "botão não é mais falado nos scripts" e "nos cinco, sem regravar se o texto do botão mudar
  depois" — idem
- "Grava o corpo uma vez e as duas caudas em seguida; a edição monta as duas versões." — plano do A
- "A pega conteúdo, impulsiona o conteúdo e coloca um CTA no final." — Rodrigo, na call com dois
  prospects
- "Se você vê, aqueles que a gente gravou é um criativo que tem conteúdo e depois chama pra aula
  completa, que é o VSL." — Rodrigo ao expert B
- "SUSPENSO" e "só depois de validar os low tickets" — sobre os fechamentos de chamada do D
- "Mas inverte a ordem de risco: a aposta é a VSL; o conhecido é o estático." — análise da VSL e dos
  hooks do A

### 3.7 Ligar o tráfego — PADRÃO CONSISTENTE (proposto) em começar baixo e em conferir antes da verba · VARIAÇÃO ISOLADA nos números e em cada item da conferência

**O que entra.**
- **Verba baixa, em faixa, subindo pelo retorno.** O número de partida variou entre os dois casos
  em que foi dito em call (no B, o teto da faixa de partida era o piso da faixa do D). A faixa medida
  como mais eficiente, num funil (B), ficou entre um quinto e dois quintos da verba diária do mês de
  pico (§3.9). Verba em faixa é regra da casa
  (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §7, item 6): piso, alvo e
  teto, nunca um número só.
- **Nome de campanha da família perpétuo**, sem tag de edição, fases VENDA e RMKT
  (`sirius-scale/frameworks/trafego/nomenclatura.md`).
- **O perpétuo cadastrado no Dash** com o produto certo, o imposto da Meta ligado e o filtro que
  pega as campanhas (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.5).
- **Conferência antes da verba**: compra teste passando pela escada inteira (o que ela prova está
  em `sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md` §3.1); a página rolada como o
  visitante vê; o anúncio conferido contra a oferta real de cada mercado; a checagem da conta antes
  de ativar (teto × gasto real, anúncio gastando com entrega restrita, expansão de público ligada em
  remarketing); e a regra de escrita em plataforma paga (`sirius-scale/REGRAS.md` §6: nasce pausado,
  confirmação escrita de quem é dono da verba, leitura de volta, teto).

**Por quê.** No perpétuo o retorno aparece no dia e o prejuízo de um começo ruim é pequeno, então
o risco não está em começar baixo: está em começar alto e em ligar com medição ou página errada.
Os três tropeços registrados foram de conferência: dois no SaaS (a página mostrou só a primeira
dobra por 4 dias com tráfego pago; o painel media outro produto) e um no A (o anúncio do outro
mercado prometia produto físico pra um produto digital). No B, a compra teste está no checklist de
montagem do funil.

**Variações aceitáveis.**
- Pixel separado por mercado (A, outro mercado).
- Religar um perpétuo que já vendia do jeito que estava, sem refazer nada, e produzir criativo
  novo em paralelo (B: combinado numa call, não conferido na conta de anúncios).

**Trecho real.**
- "se tratando um perpétuo seria bom a gente pensar entre […] por dia pra começar" e "Vai
  começando aos poucos e aumentando." — Rodrigo, na call de planejamento do D
- "a vai começar colocando […] por dia, para ir testando." — Rodrigo ao expert B
- Na nomenclatura, perpétuo e distribuição não levam tag de lançamento, porque não têm edição
  (`sirius-scale/frameworks/trafego/nomenclatura.md`)
- Produto errado no cadastro do perpétuo invalida todo retorno da tela
  (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.5)
- "Só a primeira dobra aparecia; o resto ficava em branco. Rodou assim por 4 dias, com tráfego
  pago." — rotina do SaaS
- "O erro está no anúncio, que é onde a expectativa se forma — antes de a pessoa ler a página." —
  achados da frente do outro mercado do A
- "Fazer compra teste completa passando por todo o funil" — checklist de montagem do funil do B

### 3.8 Ler — VARIAÇÃO ISOLADA na rotina (só o SaaS) · PADRÃO CONSISTENTE (proposto) na necessidade e nas duas janelas

**O que entra.**
- **Uma rotina agendada por funil**, no desenho da casa: a parte automática lê e calcula, o Claude
  julga, entrega o relatório e para. Ela não pausa, não ativa e não mexe em verba
  (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §2.3, que já prevê o `rotinas.json`
  dentro de `funis/<nome>/`).
- **As fontes**: venda (pela plataforma, pelo id da oferta quando o nome mistura produtos),
  gasto (Meta com imposto e Google), funil e página (Dash de perpétuo), VSL (o player). A do SaaS
  lê quatro pontas e deixa o Dash de fora de propósito, porque ali ele mistura dois produtos.
- **Duas janelas**: a curta (2 a 7 dias) pra alerta e pra julgar criativo; o mês pra decidir
  pausa. Perpétuo se analisa por período de 7 ou 30 dias
  (`sirius-scale/frameworks/trafego/_metodologia.md` §6).
- **Volume mínimo pra julgar criativo** (no SaaS, um piso fixo de gasto ou 2 cadastros) e a espera do
  tempo do funil antes de chamar de fracasso (no SaaS, os 7 dias do teste grátis).
- **Relatório**: estado atual primeiro, o que mudou, decisões ranqueadas pelo valor em reais
  separando certeza de hipótese, o que precisa de decisão do dono. Se nada mudou, três linhas.
- **O que não é rotina vira tarefa que repete** na ferramenta de tarefas da equipe (o checklist
  semanal do perpétuo).

**Por quê.** Perpétuo é esquecido quando outro projeto está em lançamento, e a perda é silenciosa:
vende menos e ninguém viu. O Rodrigo pediu leitura com resumo e alerta e voltou ao assunto em duas
calls nas cinco semanas seguintes. A rotina carrega o método, nunca o diagnóstico de ontem:
diagnóstico congelado na instrução reinjeta premissa falsa na rodada seguinte.

**Variações aceitáveis** (a cadência ainda não está fechada, §8):
- Dia sim, dia não (SaaS).
- Semanal, toda segunda (a distribuição de conteúdo; o checklist que o Rodrigo pediu).
- Diária (o que ele disse na call mais recente; a casa já tinha um painel interno gravando venda e
  gasto por produto a cada 3 horas).

**Trecho real.**
- "Quando vê, passou uma semana, você não olhou mais o perpétuo." — Rodrigo, numa call com o gestor
  de um projeto
- "resuminho bem breve, investindo tanto, faturou tanto, aí algum alerta, está caindo tal coisa
  aqui, observar." — idem
- "Todo dia tem que olhar todos os projetos, tem que ter rotina disso, né?" — Rodrigo, em outra call
  com o mesmo gestor
- "Cara, toda segunda-feira pode estar escrito aí." — Rodrigo, numa call com a gerente de operação
- "Esse [script] é a metade burra: ele só lê e calcula ([as fontes]). O julgamento é seu." — rotina
  do SaaS
- "Compare a janela curta com o acumulado." — idem
- "Só julgue quem tem [o piso de gasto] ou 2+ cadastros — abaixo disso é ruído." — idem
- "Se nada mudou e não há decisão a tomar, diga isso em três linhas. Relatório inflado gasta o
  crédito da rotina." — idem

### 3.9 Decidir: renovar, escalar, pausar — PADRÃO CONSISTENTE (proposto) em renovar e pausar · VARIAÇÃO ISOLADA em escalar · A, B, SaaS

**O que entra**, nesta ordem:
1. **Achar a etapa que vaza antes de mexer em verba ou criativo** (a tabela de vazamento do
   `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §6; o maior vazamento em
   reais do `sirius-scale/frameworks/lancamentos/diagnostico-de-operacao.md` Passo 5). Nos 3 perpétuos
   a leitura por etapa mudou a decisão: no A, o hook era o maior vazamento, mas os 40,6% que abriam a
   página e nunca davam play eram o conserto mais barato; no SaaS, o gargalo era a página, não o
   criativo; no B, o maior vazamento em reais foi a escala do mês de pico, não um criativo. E
   perguntar o que falta no funil: com o outro mercado do A no prejuízo, a resposta do Rodrigo foi a
   VSL que ainda não existia ali.
2. **Renovar criativo antes de o atual morrer.** O criativo que vende satura; esperar ele parar
   pra produzir obriga a parar o tráfego. Nos dois perpétuos de infoproduto o volume de criativo
   foi o gargalo declarado. O operador olha criativo antes de verba. Venda que trava no
   checkout se recupera na hora, com outra forma de pagar
   (`sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.16).
3. **Escalar enquanto o real a mais devolve**, não pelo ROAS médio. No B, a verba do mês de pico
   (cerca de 2,4 vezes o alvo proposto depois) devolveu cerca de 1,05 real por real a mais e quase
   nenhuma sobra extra; a regra proposta ficou: piso, alvo no dobro do piso, e teto só com ROAS de 2
   ou mais por 7 dias seguidos. Um funil, e o mês seguinte não foi controle limpo: VARIAÇÃO ISOLADA.
4. **Pausar pelo mês, não pelo dia.** Três ou quatro dias de prejuízo num mês no lucro não
   desligam; o mês caminhando pro prejuízo desliga. Antes de desligar, conferir se a medição é
   do produto certo (o caso do SaaS). Nunca pausar por padrão estrutural
   (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §7, item 5).
5. **Religar o que vendia do jeito que estava** e pôr criativo novo em paralelo (B: decidido numa
   call e não feito; combinado de novo cinco semanas depois pra começar no dia seguinte, não
   conferido na conta de anúncios).

**Por quê.** O perpétuo dá retorno no dia, o que convida a reagir ao dia. O Rodrigo separa o ruído
(dia) da decisão (mês). E desligar com a medição errada custa sem que ninguém veja: o SaaS foi
desligado por um painel que creditava venda de outro produto (o gasto do período inteiro, com
imposto, e a venda do SaaS nunca foi medida). Ficar parado também custa: pra religar o B, o
debriefing estima de volta a sobra média dos dois melhores meses (estimativa, não medição).

**Variações aceitáveis.**
- Pausar porque um lançamento na mesma conta está rodando (B, no 5º mês do funil). Se o lançamento
  atrapalha o perpétuo não foi medido (§8).
- **Em aberto, não variação:** diminuir em vez de desligar. No outro mercado do A, o gestor do
  projeto girava criativo sem mexer em verba e a escolha entre diminuir e desligar ficou pendente
  ("Decidir se começa a diminuir o orçamento ou desligar [o outro mercado]", ata).

**Trecho real.**
- "ficou 3, 4 dias dando prejuízo, mas a gente sempre olha o mês, então tá no lucro ainda" e "mas
  tem uma linha, né, um piso, assim, cara, que começou a ficar ruim o suficiente pra ter prejuízo
  no mês, aí é ou pausar" — Rodrigo, numa call com o expert B
- "a gente não pode se acomodar no perpétuo, a gente tem que estar sempre fazendo criativo novo e
  coisa nova, porque uma hora satura, o criativo que tá vendendo hoje, daqui a mês parou de
  vender" — idem
- "Aí […], que começou mal pra caramba, daí eu já pausei, né?" e "e também o problema dela ali
  era poucos criativos, gravar mais." — Rodrigo, numa call com a equipe
- "O perpétuo é bom, porque começou mal, é só desligar." — Rodrigo, na call de planejamento do D
- "Agora, na hora de parar de vender no perpétuo, eu vou para, pausar a campanha." — Rodrigo, na
  call com um prospect
- "se eu tô colocando X, tá voltando 2X, pode ir investindo mais, vai investindo mais." —
  Rodrigo ao expert B
- "o que dá um retorno marginal de ~1,05 e praticamente zero de sobra extra." — debriefing do B
- "O público é de nicho e pequeno, então o volume de criativo novo é o que destrava escala." — idem
- "Depois deles, nenhum criativo sustentou mais de 8 dias." e "[O último mês] rodou com 5 anúncios
  (contra 8 [no anterior]) e 53% das vendas vieram de um só." — análise do perpétuo do A
- "a decisão de desligar saiu de um painel que media outro produto." — registro do caso do SaaS
- "Estou rotacionando os criativos e não estou mexendo em orçamento." — o gestor do projeto do A;
  e o Rodrigo em seguida: "Tem que pôr a VSL, né?"

### 3.10 Registrar — PADRÃO CONSISTENTE (proposto) · A, B, SaaS + distribuição

**O que entra.**
- Uma linha por período ou por rodada no `desempenho.md`, com data e fonte.
- Quando um período fecha ou a pergunta é grande, o debriefing completo em `entregas/` (método do
  `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md`, a skill `/debriefing`),
  citando a análise anterior e o recorte em que difere; o `desempenho.md` aponta pra ele.
- Número antigo corrigido com todas as letras, inclusive o que foi dito em call.
- A versão pro expert é outra peça, feita em cima da interna
  (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §6).
- Decisão nova no arquivo de origem (matriz, briefing, banco), com data.

**Por quê.** O `desempenho.md` é a memória do perpétuo; sem ele cada análise recomeça do zero e
vira fonte que diverge da anterior (`sirius-scale/frameworks/trafego/_metodologia.md` §6.1).

**Variações aceitáveis.** Uma linha por mês (B), por período analisado (SaaS) ou por rodada
semanal (distribuição de conteúdo).

**Trecho real.**
- "Perpétuo: também atualiza `funis/<nome>/desempenho.md`, que é o debriefing contínuo desse
  modelo." — `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §6 (caminho
  adaptado pra estrutura de vocês)
- "com a data, o que entrou no teste, o que graduou e o gasto da semana" — rotina semanal da
  distribuição de conteúdo do C
- "Esta corrige três números dela" e "A versão pro [expert] mostra [o mês ruim] como ele foi." —
  debriefing do B (cabeçalho e §8)

## 4. O que muda em relação a lançamento — CONSISTENTE (proposto) em 5 dos 9 itens, o resto ISOLADA ou regra da casa

| # | Lançamento | Perpétuo | Força | De onde |
|---:|---|---|---|---|
| 1 | Pasta datada por edição, debriefing por edição | `funis/<nome>/` sem data, `desempenho.md` contínuo | regra da casa | estrutura de pastas da casa |
| 2 | Leitura por edição | por período de 7 ou 30 dias; o mês pra decidir pausa | CONSISTENTE (proposto) | `sirius-scale/frameworks/trafego/_metodologia.md` §6, §3.8, §3.9 |
| 3 | Nome de campanha com a tag da edição | sem tag; família PP, VSL, LT, HT | regra da casa | `sirius-scale/frameworks/trafego/nomenclatura.md` |
| 4 | Abre o carrinho e pode não vender | retorno visto no dia; começo ruim dá prejuízo pequeno | CONSISTENTE (proposto), 3 falas | 3 calls do Rodrigo |
| 5 | Expert faz conteúdo, lives, aquecimento | grava uma vez, depois só criativo | CONSISTENTE (proposto) | §3.1, §3.6 |
| 6 | Pode falar com a base | escrito pra frio e pra durar meses | CONSISTENTE (proposto), 3 funis | A, C, D |
| 7 | Escassez pela data do carrinho | só a verdadeira: o botão de um clique dentro da compra, o bônus que sai de fato | CONSISTENTE (proposto) | C, B, `sirius-scale/frameworks/lancamentos/low-ticket.md` §9, `sirius-scale/frameworks/lhto.md` §11 |
| 8 | Lead casa com venda no Dash; verba por custo por MQL | o Dash de perpétuo não tem lista de leads; a régua é venda e sobra | VARIAÇÃO ISOLADA (2 funis) | `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.4, B, A |
| 9 | Pesquisa de lead | dá pra pesquisar quem comprou | VARIAÇÃO ISOLADA | A (raio-x, 37 compradores) |

**Trechos reais.**
- "O perpétuo, você colocou 100 reais hoje, você já vê quanto que voltou desses 100 reais,
  entendeu?" e "Não é um negócio que dá prejuízo igual ao lançamento." — Rodrigo ao expert B
- "Lançamento, o cara tem que fazer conteúdo, tem que fazer live de aquecimento, sabe?" — Rodrigo,
  na call com dois prospects; e na mesma call: "se você faz só lançamento é cada dois meses, é aquele
  negócio que parece uma aposta"
- "Toda copy deste funil é escrita para TRÁFEGO FRIO (decisão do Rodrigo)" — banco de ângulos do A
- "Criativos de conteúdo puro pra quem não conhece [o expert]." — revisão dos leads do C
- "Low ticket ferramental, de dor específica, pra público frio" — briefing do D; e "Perpétuo,
  para o público frio." — Rodrigo, na call com dois prospects
- "o botão de um clique do upsell e do downsell só existe dentro de um processo de compra ativo."
  — README do C
- "Num perpétuo só vale se a página tirar o bônus de fato; senão é escassez falsa." — briefing do
  B, erro 7
- "Produto perpétuo digital não tem vaga limitada de verdade." — `sirius-scale/frameworks/lhto.md` §11
- Em perpétuo não dá pra casar venda com lead por e-mail
  (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.4)
- "Não há dado de investimento em mídia. Sem isso, não existe CAC, ROAS nem custo por lead — só
  faturamento." — desempenho do A

## 5. Regras transversais

1. **Número com fonte e base declarada.** Sem o dado, a frase é "não medido", não estimativa
   (`sirius-scale/REGRAS.md` §2; `sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`).
2. **Rotina e agente não escrevem em plataforma paga.** Entregam o plano; quem é dono da verba
   confirma por escrito (`sirius-scale/REGRAS.md` §6). Vale pras duas rotinas contínuas que existiam
   no caso de origem.
3. **Toda copy passa pelo `copy` e pelo `/humanizer`** (`sirius-scale/REGRAS.md` §3), inclusive a cauda de
   chamada do criativo e o bloco de preço.
4. **Decisão entra no arquivo do funil, com data.** Os três funis com decisão registram assim: as
   decisões no topo do plano e da matriz do A, o histórico de decisões no README do C.
5. **Estado atual primeiro, histórico no fim**, no arquivo e no relatório (README do C;
   rotina do SaaS).
6. **Filtrar o que é de outro cliente ou produto antes de salvar** (export global do Dash no
   A; venda do SaaS lida pelo id da oferta).
7. **O expert recebe só o que grava** (teleprompter e direção em arquivos separados no A).
8. **O que saiu da peça, e quem tirou**: apelo a quem já conhece o expert num funil de frio
   (decisão do Rodrigo, no A); preço, botão e nome de aluno falados no corpo (decisões do
   Rodrigo no C, em dois dias seguidos; no A, o preço saiu do corpo na correção da matriz); escassez
   de vaga ou cronômetro (regra da casa: `sirius-scale/frameworks/lancamentos/low-ticket.md` §9, README do
   C, erro 7 do briefing do B). Proporção de preço que a conta não fecha é caso único: no A o
   Rodrigo tinha aprovado metade do preço, quem cortou foi a conferência do agente, e a matriz deixou
   a volta oferecida a ele. E o debriefing corrigiu a fala de call que arredondou o resultado do mês
   pra cima.

**Trecho real.**
- "Sempre filtrar — não versionar dado de outro cliente na pasta deste." — README do A
- "Estado atual primeiro; histórico de decisões no fim." — README do C
- "Decisão do Rodrigo: amarra a peça a um público que acaba e obriga a regravar." — banco de
  ângulos do A, tabela de proibidos
- "Se o Rodrigo preferir a simetria de volta" — matriz de preços do A

## 6. Exemplos consolidados (adaptados do caso: número e produto trocados por relação)

**A pasta de um perpétuo que roda** (o funil do A, no fim da extração):

```
achados-<frente>-<AAAA-MM-DD>.md
analise-vsl-hooks-<AAAA-MM-DD>.md
avatar-comprador.md
avatar.md
banco-angulos.md
briefing.md
desempenho.md
matriz-de-precos.md
plano-producao-<AAAA-MM>.md
atas/            (recortes das reuniões do projeto)
```

**O `desempenho.md` mês a mês** (o do B; valores em índice, com o faturamento do mês 2 = 100, pra não
expor o número do caso; o arquivo de verdade traz os valores em reais):

```
| Mês | Livros + upsell | Faturamento | Tráfego | Sobra | ROAS |
|---|---:|---:|---:|---:|---:|
| mês 1 (2 dias) | 3 + 0 | 3,4 | 0,6 | +2,5 | 6,0 |
| mês 2 | 78 + 5 | 100 | 56,7 | +35,1 | 1,76 |
| mês 3 | 28 + 6 | 53,2 | 12,2 | +36,7 | 4,35 |
| mês 4 | 37 + 6 | 55,4 | 22,9 | +28,0 | 2,42 |
| mês 5 | 2 + 0 | 2,3 | 7,0 | −4,9 | 0,32 |
| mês 6 (parcial) | 3 + 0 | 3,4 | 0 | +3,1 | — |

Estado no dia do debriefing: tráfego pausado desde o mês 5. Faixa de verba medida como
mais eficiente: [faixa diária do caso] (VARIAÇÃO ISOLADA, 1 funil).
```

**A matriz** (a do A, mercado principal; preços trocados por relação):

```
| Peça | Produto | Preço |
|---|---|---|
| Criativos do curso | o curso caro | [cheio] |
| Criativos do front | o material físico (front) | [preço do front] |
| VSL do front | o material físico (front) | [preço do front] |
| **Upsell** do curso | o curso caro | de [cheio] por **[48% do cheio]** à vista · **12× [parcela do checkout]** |
| **Downsell** do curso | o curso caro, 6 meses | **[58% do upsell]** à vista · **12× [parcela do checkout]** |
```

**A decisão ranqueada que sai do desempenho** (debriefing do B §9):

```
| # | Ação | Vale (por mês, estimativa) | Custo de testar | Sustentação |
|---|---|---:|---|---|
| 1 | Religar o perpétuo na faixa de verba medida como eficiente, com os 3 criativos que mais venderam e variações novas dos 3 ângulos | ~a sobra média dos dois melhores meses | verba do expert; 7 dias | os dois melhores meses, ISOLADA |
| 2 | Gravar volume de criativo nos 3 ângulos que venderam (pelo menos 4 por semana) | destrava escala acima do teto da faixa (não estimável) | tempo do expert | frequência 5,85 + ranking por ângulo |
```

**O relatório da rotina** (rotina do SaaS, passo 3):

```
1. Estado atual primeiro (o Rodrigo lê pelo celular — nada de tabela larga)
2. O que mudou desde a última rodada
3. Decisões ranqueadas pelo valor em reais, separando o que é certeza do que é hipótese
4. O que precisa dele
```

## 7. O que transfere e o que é do caso

**Transfere** (é de modelo de funil; como os dois clientes são do mesmo nicho, que transfira pra
outro nicho é hipótese, não medida):
- A decisão de quando é perpétuo (§3.1) e o par perpétuo mais lançamento pra quem produz conteúdo.
- A pasta sem data, o `desempenho.md` com fonte e base, e o corte do perpétuo contra o resto da
  conta (§3.2, §3.3).
- A matriz como fonte única, a parcela do checkout e a conferência da aritmética (§3.4).
- As três regras do plano de produção (§3.6): gravação como recurso escasso, o que muda fora do
  corpo, criativo de conteúdo com cauda.
- Começar baixo, conferir antes da verba, ler em duas janelas, pausar pelo mês, renovar antes de
  morrer (§3.7 a §3.9).

**É do caso** (não generalizar sem medir):
- **Os números**: a faixa de verba diária, o retorno marginal do mês de pico, ROAS 2,19, subida de
  11,3% (upsell, downsell e uma venda pelo preço cheio, somados) e de 7,7%, reembolso de 12,7%, o
  fator de parcelamento de 1,2411. São de uma conta, um nicho e um ano.
- **O preço alto do produto físico de entrada** no A (cerca de 2,5 vezes o do mesmo formato no C): o
  Rodrigo atribui ao nicho e ao material físico de apoio.
- **O segundo mercado do A**: a versão feita pra ele, a gravação única, a âncora que não transfere. Um
  mercado, uma conta.
- **A régua do SaaS** (custo-alvo por cadastro, 7 dias de teste grátis): é de assinatura, não de
  infoproduto. O que transfere dele é a forma da rotina e o caso do desligamento.
- **O estático de venda direta como caminho provado**: uma conta.

## 8. Pontos em aberto

1. **A cadência da leitura de perpétuo de infoproduto não está decidida, e a rotina não existe.**
   O Rodrigo pediu diária, semanal e as duas na mesma fala ("Aí liga a rotina de otimização
   diária." e "Sei lá, semanal, né?", numa call com o gestor de um projeto). Só o SaaS tem rotina,
   dia sim, dia não. O `sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §2.2 já prevê o
   arquivo "funil perpétuo em funis/<nome>/", e nenhum perpétuo tem `rotinas.json`.
2. **A linha de pausa não tem número.** "Prejuízo no mês" é a regra; "começou mal, é só desligar"
   também é. Quantos dias, contra qual piso, não está escrito. O B tem teto pra escalar
   (ROAS de 2 por 7 dias) e não tem o espelho pra pausar.
3. **Venda pelo link da bio: tráfego ou orgânico?** O debriefing do B conta como orgânico:
   "Orgânico (bio) = ~10% do faturamento, sem custo de mídia." O Rodrigo, sobre o A: "Vende um
   monte pela Bill e a gente, pô, só pode ser do tráfego." ("Bill" é o ASR de "bio"). A análise do A
   diz que "A mídia paga pra VSL parou em [um mês]." e que a VSL vive da bio desde o mês seguinte. As
   três leituras não fecham. PADRÃO INCONCLUSIVO.
4. **Perpétuo e lançamento na mesma conta: atrapalha ou ajuda?** No A, "O perpétuo foi melhor
   durante o lançamento. Ele só morreu quando o lançamento acabou." No B, a hipótese do mês ruim é
   "concorrência de público com o [lançamento] (mesma conta, mesmo nicho, mesma semana)". O gestor de
   um dos projetos teme "emburrecer campanha". Nada medido. PADRÃO INCONCLUSIVO.
5. **Criativo esgota ou cansa?** O plano do A registrou "Criativo de remarketing esgota, não
   cansa" como INCONCLUSIVO com base no criativo campeão. A mesma análise depois corrigiu: o criativo
   campeão nunca rodou em remarketing, ele vendeu em FRIO. O mecanismo escrito (estoque de remarketing
   acabando) não bate mais com o caso que o sustentava. Falta medir alcance incremental.
6. **Qual régua de upsell e de VSL a casa usa?** O Rodrigo deu como meta, numa consultoria:
   "a meta é até 30% chegar no pitch, aí também você quer ter 20% de conversão do upsell, 15% do
   downsell". O prompt de upsell (externo) trata 8 a 12% como bom e o próprio arquivo avisa que é
   número de mercado (`sirius-scale/frameworks/copy/video-de-upsell.md`). Medido na casa: 7,8% dos
   plays chegando ao pitch e retenção de 16 a 20% no minuto 1 (A); no B, contados por
   oferta, 7,3% no upsell (11 dos 151 compradores do livro) e 3,6% no downsell (5 dos 140 que não
   levaram o upsell), a base que o `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.15 usa;
   os 11,3% do debriefing somam upsell, downsell e uma venda pelo preço cheio; no A, 7,7% com janela
   misturada. O plano do A chama os 7,7% de bom, abaixo da faixa que ele mesmo cita. O
   `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.15 também deixa a régua em aberto.
   PADRÃO INCONCLUSIVO.
7. **Checkout e recuperação não estão medidos.** No B, "O abandono de carrinho registrado foi
   de 65, e não existe fonte de quanto a recuperação trouxe." No A, numa call: "Ela vai pro
   checkout, tem uma galera que vai pro checkout e não compra." A IA de recuperação no WhatsApp do
   A (`sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.16) não tem resultado registrado.
8. **Outro mercado ainda não deu certo nem errado com número.** O outro mercado do A estava no
   prejuízo, sem VSL ("Semana ruim: [o outro mercado] dando prejuízo e o outro parou."). O B combinou
   levar VSL, livro e curso pra um segundo mercado. Sem resultado.
9. **Webinário perpétuo pra quem comprou o front e não o upsell**: ideia de uma call ("Só ideia,
   nada fechado."), que o Rodrigo também citou ao expert B e no plano de uma consultoria. Não rodou.
10. **A única rotina de perpétuo nasceu quebrada**: as duas primeiras rodadas da rotina do SaaS
    terminaram num comando sem retorno
    (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §1). Não há registro de rodada boa
    depois disso.
11. **Três lacunas de framework que este arquivo encontrou e não corrige**: o
    `sirius-scale/frameworks/lancamentos/briefing.md` manda escrever a variante de perpétuo ("Cliente de
    perpétuo/VSL preenche menos e ganha campos próprios") e ela nunca foi escrita; o
    `sirius-scale/frameworks/copy/criativos.md` §3 (VSL / Evergreen) está adiado, e é onde caberia o
    criativo de conteúdo com cauda; o backlog de ideias da casa pede "um modelo de árvore de pastas por
    tipo de funil (lançamento clássico, pago semanal, perpétuo)".
12. **O `desempenho.md` do perpétuo principal da casa nunca recebeu gasto.** O do A tem venda
    desde o começo do funil e a conta de anúncios conectada desde o dia do plano de produção, e o ROAS
    dele não foi calculado nos arquivos do funil. A correção da queda de 86% (feita na análise da VSL e
    dos hooks, §3.3) só chegou nele quinze dias depois. Correção que leva duas semanas pra propagar é
    o risco que a §3.10 tenta cortar.
13. **Reembolso alto sem causa**: 12,7% no livro do B, e "o motivo do reembolso não vem na
    API." No A, a causa do problema do outro mercado foi achada no anúncio (§3.7); no B, não se
    procurou. O método de procurar está em `sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md`
    §3.10.
14. **Produto caro direto no perpétuo**: os dois funis mostram que ele quase não vende cheio fora
    de lançamento (§3.4), mas a VSL do curso caro no outro mercado do A continua como "Ideia do
    Rodrigo, ainda não decidida." VARIAÇÃO ISOLADA nos dois lados.
