# Framework — Diagnóstico de operação de terceiro (entrar numa operação que a casa não montou)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered de 3 diagnósticos escritos em menos de dois meses, em 3 operações de 3 donos
diferentes, mais 3 fontes de apoio (uma triagem oral, dois diagnósticos de trabalho feito por outra
pessoa, uma coleta de orgânico). É o método de entrar numa operação que não foi montada por quem
diagnostica e achar onde ela perde dinheiro.

> **ALCANCE: TESTADO EM 3 CLIENTES (proposto, a confirmar pelo Rodrigo):** aqui aparecem B e C.
> Uma operação de apoio, que não é cliente, rodou o mesmo processo: A (um produto próprio de uma
> empresa ligada à casa).
> Cada passo diz em quantos destes 3 diagnósticos aparece; pra saber se o passo apareceu em cliente,
> as letras B e C são as de cliente.
>
> As contagens são da base que aparece neste kit. O alcance e os rótulos de força são os da base
> completa da casa, que tem casos que não aparecem aqui.
>
> **A parte do plano é NÃO TESTADO.** Nenhum dos 3 tem resultado medido depois do diagnóstico. Os
> planos foram apresentados e alguns viraram decisão; nenhum fechou ciclo com número.
>
> **Força (eixo 1):** PADRÃO CONSISTENTE (proposto) = apareceu em 3 ou mais diagnósticos da base
> completa; quem promove a regra é o Rodrigo (`sirius-scale/REGRAS.md` §4). VARIAÇÃO ISOLADA = 1 ou 2.
> PADRÃO INCONCLUSIVO = sinal sem base, declarado como hipótese.
>
> **Vizinhos, que este arquivo cita e não reescreve:**
> `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` (dimensões, travas,
> formato, ranking em reais), `sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`
> (contratado × Dash × líquido), `sirius-scale/frameworks/trafego/_metodologia.md` (leitura de
> tráfego, lift), `sirius-scale/frameworks/trafego/leitura-dash-facil.md` (armadilhas do painel).

## 0. Como usar

- **Use quando** a operação não foi montada por quem vai diagnosticar, ou o dado dela não é
  controlado por quem diagnostica: vem do dono (export, planilha, painel, dossiê do time dele),
  chega pela metade, não tem plano escrito pra comparar, e as fontes não batem entre si. O pedido
  é saber onde o negócio perde dinheiro e o que fazer.
- **Não use** pra funil montado por quem diagnostica, com dado limpo e plano: aí é o
  `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` (skill `/debriefing`).
  Conferência técnica de campanha que outra pessoa subiu é `/revisar`.
- **O que muda em relação ao debriefing:** este arquivo é a camada de antes e a de depois. Antes:
  acesso, catálogo, limpeza e conferência de dado de terceiro, régua sem plano. Depois: perguntas
  que só o dono responde, plano com ordem de execução, apresentação. No meio, a leitura usa as
  dimensões e as travas do debriefing (§4 e §5 de lá).

## 1. Escopo e base de evidência

### Fontes

| Apelido | O que é | Material | Peso |
|---|---|---|---|
| A | Primeiro diagnóstico de um perpétuo com teste grátis de um produto próprio de uma empresa ligada à casa, sem análise anterior e com o painel configurado no produto errado desde a criação | o diagnóstico, o `desempenho.md` do funil, a correção registrada e a campanha consolidada que saiu dele | Forte: fatos confirmados pelo Rodrigo no dia, e o diagnóstico virou ação em pouco mais de duas semanas (campanha consolidada, perpétuo novo com imposto ligado) |
| B | Debriefing do perpétuo de um produto de entrada de um expert da casa, com o dado da conta misturado no mesmo CNPJ com produtos de outro expert | a comparação de dois funis, o debriefing do perpétuo e a ata de uma reunião com o expert | Forte nos números (o Rodrigo confirmou a atribuição) e nas decisões da reunião |
| C | Entrada num perpétuo que já rodava havia mais de um ano, montado fora da casa (a base do cliente foi montada de 43 arquivos que o projeto já tinha) | o catálogo do cliente, o `desempenho.md` do funil e a análise do perpétuo | Média: entregável sem registro de aprovação; uma inferência foi corrigida pelo Rodrigo três dias depois (regra da casa: não atribuir causa sem medir) |
| D | Triagem oral numa call, sem dado em mãos | a transcrição da call | Forte como fala do Rodrigo; é uma conversa só |
| E | Dois diagnósticos de coisa feita por outra pessoa dentro da operação de um cliente da casa: o playbook comercial e o orgânico | os dois diagnósticos | Média |
| F | Coleta do orgânico de um expert novo, feita de fora | duas coletas (perfil e últimos 90 dias) | Fraca: coleta sem a análise guardada e sem aprovação registrada |

Também entram correções do Rodrigo que viraram regra da casa: não atribuir causa sem medir, número
sem fonte rastreável não entra, número de dinheiro só com fonte oficial, e o acesso à conta de
anúncios do cliente.

### Excluído de propósito

- Auditorias de configuração de campanha que um gestor subiu: é conferência técnica (`/revisar`,
  `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`,
  `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`), não diagnóstico de vazamento.
- Debriefings de funil da casa: dado limpo e plano. São a base do
  `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md`.
- Calls sem diagnóstico escrito e um workshop de terceiro, que é aula de outra pessoa.

### Ressalva estrutural da base

- 3 diagnósticos de 3 donos. Cliente, pra efeito de alcance, aqui são 2 (B, C); A é produto próprio
  de uma empresa ligada à casa. Um diagnóstico por operação; ninguém foi diagnosticado duas vezes,
  então não existe antes × depois de plano.
- Em C o dono é de fora da casa. A é produto de uma empresa do Rodrigo, num painel configurado com
  o produto errado e sem análise anterior; B é um cliente da casa com dado herdado e misturado. Os
  dois entram porque o dado chegou como chega de terceiro: sem histórico guardado e sujo.
- Tudo em menos de dois meses, já com o sistema de agentes rodando.
- Análises avulsas que o Rodrigo faz fora destes diagnósticos não estão na base. A base são os 3.

### Veredito da FASE 1

| Item | Resposta |
|---|---|
| Unidades | 3 diagnósticos (A a C) em 10 documentos, mais 3 fontes de apoio (D, E, F) |
| Clientes e funis | 2 clientes (B, C) e 1 operação de apoio (A); lançamento, perpétuo de VSL, perpétuo com teste grátis, low ticket |
| Aprovação ou decisão dele | Sim em A e B; parcial em C |
| Resultado depois do plano | Não, em nenhum |
| Veredito | **EXTRAÍVEL FORTE** pro processo de leitura, pela base completa da casa (a régua está em `sirius-scale/frameworks/_extracao-de-frameworks.md`). O plano fica NÃO TESTADO |
| O que falta pra subir | Um ciclo fechado: o mesmo dono diagnosticado de novo depois de rodar o plano |

## 2. A fórmula, em ordem

Dois modos, que mudam o tamanho, não a ordem:

- **Modo operação inteira**: o dono não sabe onde dói. Lê funis, base, caixa e estrutura.
- **Modo funil ou peça** (A, B, C): o dono traz uma pergunta fechada (a escala, a queda de venda).
  Lê o funil e responde a pergunta.

Os dois compartilham os passos 0 a 5 e 7 a 12. O passo 6 é só do modo operação inteira.

0. Enquadrar: a pergunta que chegou e as hipóteses que já estão na mesa.
1. Acesso e catálogo: o que veio, o que dá, o que não dá, o que falta.
2. Delimitar o objeto e limpar o dado.
3. Conferir uma fonte contra a outra.
4. Declarar a base e escolher a régua.
5. Achar o maior vazamento, em reais.
6. A conta do negócio, além do funil (só no modo operação inteira).
7. Separar causas com cortes independentes.
8. Medição quebrada vira achado, e o conserto vai na frente.
9. O que só o dono sabe: perguntas, reunião, documento atualizado com data.
10. Do diagnóstico ao plano.
11. Apresentar.
12. Registrar.

A ordem é a do trabalho nos casos: catálogo e limpeza antes de qualquer leitura, leitura antes das
perguntas, perguntas e reunião antes do plano final. Entre os passos 2 e 8 a ordem é de dependência
(não dá pra dizer o vazamento antes de declarar a base), não de calendário. O documento entregue
abre pelo resultado em uma tela, como manda o
`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §6.

## Passo 0 — Enquadrar a pergunta e as hipóteses · PADRÃO CONSISTENTE (proposto), 3 de 3

**O que entra.** A pergunta do dono, nas palavras dele, no topo do documento (A, B, C). Se vieram
duas, as duas (B trouxe duas: se o produto de entrada se sustentava e quanto dava pra investir).
As hipóteses que já estão na mesa, do dono, do time e do próprio Rodrigo, cada uma escrita
como afirmação que o dado vai confirmar ou derrubar (C foi procurar saturação de criativo). E o status: rodando ou fechado, com
janela declarada em toda frase quando está rodando (A). Rodando × fechado já
é regra do `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §1.

**Por quê.** Em 2 dos 3, a pergunta que chegou não apontava pro lugar do problema. O diagnóstico
respondeu a pergunta e mostrou que o gargalo estava em outro lugar: A (escalar? não, medição e
página) e C (saturação? não, a conta parou de entregar, como hipótese). Com a pergunta escrita, o
documento é obrigado a responder, e a dizer que o problema não está ali mostrando o dado que
descarta.

**Variações aceitáveis.** Pergunta fechada leva ao modo funil ou peça; pergunta aberta (o negócio
parou de dar dinheiro?) leva ao modo operação inteira.

**Trecho real.**
- "Antes de tudo, o enquadramento honesto: o pedido era achar como escalar." (A, diagnóstico §8)
- "Foi o que eu fui procurar, e o dado não sustenta." (C, análise do perpétuo §2)
- B abriu com as duas perguntas no cabeçalho do debriefing: se o produto de entrada se sustentava
  e quanto dava pra investir, com que retorno.

## Passo 1 — Acesso e catálogo das fontes · PADRÃO CONSISTENTE (proposto), 3 de 3

**O que entra.**
1. Pedir acesso à fonte primária, não ao print: conta de anúncios, painel de lead e venda,
   plataforma de venda, Drive. Na Meta o caminho é a conta do cliente compartilhada como parceira
   do Business Manager de quem diagnostica (regra da casa).
2. Um catálogo com uma linha por fonte: arquivo, período que cobre, o que dá pra tirar, o que não
   dá (A, B). É o inventário do
   `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §2.3 aplicado a dado
   que não é da casa.
3. A lista do que não veio e faz falta, separada do catálogo.
4. Antes do primeiro número, o que dá e o que não dá pra responder com o que chegou (C fez isso
   numa tabela de perguntas com sim e não).

O acesso foi parcial nos 3: em A, a
conta de anúncios chegou no meio da análise; em B, a conta não libera o usuário de sistema da casa;
em C, a mídia não estava conectada no painel.

**Que dado pedir.** Não existe, nos 3 casos, uma lista de pedido enviada ao dono (ver Pontos em
aberto). O que existe é o que foi usado:

| Fonte | Usada em | O que destrava | Faltou em |
|---|---|---|---|
| Lista de vendas com e-mail, produto, data, forma de pagamento e UTM | 3 de 3 | casar venda com lead e com origem; ticket; parcela | — |
| Gasto por plataforma, de preferência por dia e anúncio | 2 de 3 (A, B) | custo por lead e por venda, vazamento em reais | C |
| Lista de leads com e-mail, data de criação e UTM | 1 de 3 (C) | conversão lead → venda; lead novo × base antiga | A (o painel não entrega a lista) |
| Pesquisa de lead e de comprador | 1 de 3 (C) | quem veio × quem comprou | A, B |
| As peças: scripts, página, criativos, planilha de criativos | 3 de 3 (A, C; B só pelo nome dos criativos e pelo tempo de carga da página) | ligar o número à mensagem | — |
| Painel, planilha ou dossiê que o dono já usa | 2 de 3 (A, B) | a conferência do passo 3 | — |
| Orgânico (perfil, vídeos) | E e F, de apoio | base que cresce sem anúncio | — |
| O que só o dono sabe (custo fixo, outras receitas) | 3 de 3, como pergunta | o tamanho de tudo | nunca está no arquivo |

A única ordem de pedido registrada é a da triagem oral (D): primeiro se já existe leitura feita
(debriefing), depois o rastreio (UTM), depois o cruzamento da pesquisa com o criativo.
**VARIAÇÃO ISOLADA** (1 conversa).

**Por quê.** Em dado de terceiro o acesso é o primeiro gargalo e define o que dá pra concluir.
Dizer antes dos números o que não dá pra responder evita entregar metade com cara de inteiro. Aqui
o diagnóstico não para por falta de plano, como o debriefing pararia (§2.4 de lá): em nenhum dos 3
havia plano pra série inteira. Segue com o escopo declarado e com a régua
do passo 4.

**Variações aceitáveis.** Leitura de fora quando não há acesso (F), sempre dizendo o que de fora não aparece. Fonte que chega
no meio entra no mesmo documento, em seção nova com data (A).

**Trecho real.**
- "Não existe CPM, gasto ou CTR neste dado — e não existe no Dash também, porque Meta e Google ainda não estão conectados na conta [...]." (C, análise do perpétuo)
- "foi liberada pelo Rodrigo [...] no meio desta análise" (A, diagnóstico, seção Fontes)
- Na triagem de D, nesta ordem: "Vocês fizeram o debrief?", depois "UTM?", depois "E aí, você consegue ver, assim, tipo, o que que a pessoa, o que que os caras que vieram de tal criativo respondem na pesquisa?" (Rodrigo, transcrição da call)

## Passo 2 — Delimitar o objeto e limpar o dado · PADRÃO CONSISTENTE (proposto), 3 de 3

**O que entra.**
1. **Delimitar:** qual produto, qual CNPJ, qual funil, qual janela pertencem ao que está sendo
   analisado. B tinha produtos de outro expert no mesmo CNPJ; A tinha o painel apontando pra outro
   produto e uma janela real diferente do filtro de data; C separou a frente principal das frentes
   de outros mercados.
2. **Limpar:** venda de teste, parcela no lugar do total, juros, reembolso.
3. **Escrever a limpeza** no documento, com quantas linhas cada regra mexeu e o efeito no número.

**Por quê.** Nos 3 casos a limpeza mudou uma conclusão. Em A, o ROAS do painel virou zero venda do
produto, e foi com o número errado que o funil tinha sido desligado. Em B, o resultado do expert
mudou de patamar com só os produtos dele na conta. Em C, a diferença de reembolso entre dois
produtos era da mesma oferta renomeada, em dois períodos.

**Armadilhas vistas** (o conjunto serve de checklist; a força vai na linha: VARIAÇÃO ISOLADA quando
veio de uma ferramenta ou de um CRM só, e a força que o vizinho já dá quando ele já registrou):

| Armadilha | Onde | Como se pega | Efeito medido | Força |
|---|---|---|---|---|
| Gasto sem imposto | A | campo de imposto do painel; fatura | em A, o custo por cadastro subiu 12% (o imposto da Meta) | regra da casa (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §5, item 13); o campo do painel, `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.5 |
| Painel apontando outro produto; venda identificada pelo nome do produto, não pela oferta | A | preço das vendas creditadas contra a página | as 2 vendas eram de outro produto | CONSISTENTE no `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.5 |
| Janela do perpétuo diferente do filtro de data | A | reconciliar visão mensal × diária | 8 vendas de um mês que não eram do funil | CONSISTENTE no `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.2 |
| Venda de teste contada como venda e parcelamento que grava só a parcela | A (uma venda de teste) | filtrar teste; refazer o total | em A, uma venda de teste no meio das do período; a parcela no lugar do total está registrada no vizinho | CONSISTENTE no `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §4.5 |
| CNPJ com produtos de outro expert | B | atribuir pelo recebedor da comissão, não pelo nome | o resultado do expert mudou de patamar com só os produtos dele na conta | ISOLADA |
| Mesmo produto com dois nomes, mesmo criativo com duas grafias, macro de UTM não resolvida, ID no lugar do nome | C | normalizar antes de agrupar | 76% das vendas sem criativo identificável pelo nome | ISOLADA |
| Buraco de período (mês sem gasto ou sem venda) | C | tabela de cobertura por ano | C: um mês sem venda, lacuna de dado ou mês parado, a conferir | ISOLADA (1 caso) |

As três bases de faturamento e a armadilha do NuPay na Hotmart estão em
`sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md` e
`sirius-scale/frameworks/hotmart/hotmart-api-tecnica.md` §12; aqui não se repetem.

**Trecho real.**
- "o painel está medindo o produto errado." (A, diagnóstico §1)

## Passo 3 — Conferir uma fonte contra a outra · PADRÃO CONSISTENTE (proposto), 2 de 3 (A, B)

**O que entra.**
- O painel, a planilha ou o dossiê que o dono já usa, contra o export bruto, item a item: bate, não
  bate, e por quê.
- Plataforma de anúncio × painel × plataforma de venda (A: conta de anúncios e painel no centavo;
  B: painel e Hotmart a 2,6%, diferença de juros).
- Duas telas da mesma ferramenta (A: a visão mensal discorda das outras duas).
- Número que vira dinheiro confere com documento oficial, fatura ou extrato (B guardou a fatura da
  Meta junto dos dados). Regra da casa: `sirius-scale/REGRAS.md` §6 (número de dinheiro sempre
  com a fonte: a tela ou o relatório da plataforma).

**Por quê.** O dono e o time dele já têm uma leitura. Com a conferência feita, a conversa sai de qual número está certo; quando não bate, a
diferença é achado (juros).

**Variações aceitáveis.** Fonte única, sem nada pra conferir: declarar no topo (C). Sem documento
oficial: o número sai marcado como estimativa.

**Trecho real.**
- "o gasto que ela reporta fecha no centavo com o do Dash" (A, diagnóstico, seção Fontes)
- "Faturamento do Dash no período [...] fecha com a Hotmart a 2,6% — diferença de juros de parcelamento." (B, debriefing do perpétuo §2)

## Passo 4 — Declarar a base e escolher a régua · PADRÃO CONSISTENTE (proposto)

Três regras, cada uma com a sua contagem:

1. **A base de faturamento vai no cabeçalho**, com o que ela inclui, o que falta pra ser líquido e
   pra que lado o número erra (3 de 3). Todo derivado herda a base
   (`sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`, regras 1 a 3).
2. **Sem plano, a régua é a história do próprio dono** (2 de 3): a
   série de anos e o mês típico (B), antes, durante e depois de um evento (C). Sem história
   nenhuma, primeiro período, a régua é a conta que tem que fechar (A: receita por cadastro contra
   custo por cadastro).
3. **Número de outro cliente da casa nunca é régua.** O framework da casa entra como método de
   leitura; a comparação com outro cliente, quando aparece, é de estrutura (2 de 3: A, C).

**Por quê.** Bases misturadas erram, e em terceiro a base vem com coisa que a casa não usa (juros).
Sem plano (nenhum dos 3 tinha um pra série inteira), a régua do próprio auge
compara o dono com ele mesmo, sem trazer número de outro mercado. E os números da casa nasceram de
um cliente só (`sirius-scale/REGRAS.md` §4, alcance).

**Trecho real.**
- "receita por cadastro = (trial → pago) × [preço mensal] × meses de permanência" (A, diagnóstico §3; o preço saiu)
- "Mas isso é hipótese: medir, não herdar." (C, `desempenho.md`, sobre o fator de faturamento)
- "não tenho referência da conta nem do nicho pra cravar isso" (A, diagnóstico §8, sobre o CPM)

## Passo 5 — O maior vazamento, em reais · PADRÃO CONSISTENTE (proposto) no princípio, 2 de 3 (A, B); a forma varia

**O que entra.** O maior vazamento dito em reais no resultado em uma tela, sustentado por uma
tabela. Duas formas apareceram:

1. **Por etapa do funil** (A): quanto se gastou em quem passou de uma etapa e não fez a seguinte,
   e a ordem de grandeza do conserto se a etapa convertesse um pouco mais. É a tabela de vazamento
   do `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §4.1, aplicada.
2. **Retorno marginal da verba** (B, VARIAÇÃO ISOLADA): verba a mais entre dois meses contra
   faturamento a mais, com a ressalva de que os meses não são controle limpo.

Onde não saiu: em C não havia gasto (o documento diz que custo e ROAS não dá pra afirmar).

**Por quê.** É a resposta que o dono veio buscar (onde o negócio perde dinheiro), e é por ele que
o plano se ranqueia (passo 10).

**Variações aceitáveis.** As formas acima, conforme o dado que existe: funil por etapa, ou meses
com verba diferente. Sem gasto, o documento diz que o vazamento
em reais não sai e por quê (C).

**Trecho real.**
- "[...] foram gastos em gente que abriu a página e não fez a única coisa que a página pede." (A, diagnóstico §2: 97% do gasto do período)
- B: a verba a mais de um mês comprou quase o mesmo tanto de faturamento a mais, um retorno marginal de ~1,05, e o mês seguinte "não é controle limpo" (B, debriefing do perpétuo §2)

## Passo 6 — A conta do negócio, além do funil · VARIAÇÃO ISOLADA (os casos de origem não aparecem neste kit)

**O que entra** (só no modo operação inteira): faturamento contra mídia por mês e por ano; o que
paga as contas, inclusive receita que não está nos arquivos; a estrutura e o custo fixo; e se
o negócio depende de um motor só.

**Por quê.** O funil sozinho pode não explicar a dor do dono. A conta do negócio dá o tamanho de
tudo, e nos casos de origem o número que faltava era o da estrutura.

## Passo 7 — Separar causas com cortes independentes · PADRÃO CONSISTENTE (proposto), 2 de 3 (A, C)

**O que entra.**
- Pegar a causa suspeita e medir em cortes que ela não deveria afetar. Se cai tudo junto (frentes,
  plataformas, perfis, criativos), a causa atinge todos: evento, oferta, calendário, entrega da
  conta. Se uma unidade cai e as outras não, aí sim é a unidade.
- A checagem que fecharia a dúvida, com nome (C: gasto diário da conta).

O raciocínio do lift que cai igual em todo corte está em `sirius-scale/frameworks/trafego/_metodologia.md`
§6.2; a trava de causa concorrente, no
`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §5, item 16.

**Por quê.** Em terceiro, cada pessoa da operação já chega com uma explicação. O corte independente derruba ou sustenta a explicação sem virar
opinião contra opinião.

**Variações aceitáveis.** Com N pequeno, teste de proporções antes de dizer que dois criativos são
diferentes (A: p = 0,47 e p = 0,52; `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §3.7).

**Trecho real.**
- "Saturação de criativo é fenômeno por criativo. Não derruba três frentes independentes na mesma semana." (C, análise §2)
- "Cinco criativos diferentes, cinco ângulos diferentes, e todos batem na mesma parede de 3,6%–6,7%." (A, diagnóstico §6.1)
- "Número certo e rastreável ainda não é explicação." (regra da casa)

## Passo 8 — Medição quebrada vira achado, e o conserto vai na frente · PADRÃO CONSISTENTE (proposto): achado em 3 de 3, conserto antes do próximo ciclo em 2 de 3

**O que entra.**
- Quanto do resultado está fora do que a medição enxerga, em porcentagem: venda sem UTM, venda
  que não casa com lead, UTM errada (A, B, C).
- O que isso trava: decisão de verba, ranking de criativo, qualquer leitura de origem.
- O conserto, que costuma ser barato, recomendado antes do próximo ciclo (A, C) e, onde há
  ordem de execução, no começo dela (A, C).

Clique sem UTM como achado de primeira linha e venda que não casa declarada já são travas do
`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §5 (itens 9 e 21).

**Por quê.** Em A, a decisão de desligar o funil saiu de um painel que media outro produto. Escalar
em cima disso só repete o erro com mais verba.

**Variações aceitáveis.** Quando o conserto depende de outra equipe, ele entra no plano com quem
faz e quanto custa (A: separar o produto pedia uma conversa com o time do produto e uma
configuração no painel, sem mídia).

**Trecho real.**
- "escalar em cima de número errado multiplica o erro junto com a verba." (A, diagnóstico §5)
- "a decisão de desligar saiu de um painel que media outro produto." (A, a correção registrada)
- "Isso é barato de arrumar e destrava toda a análise de criativo daqui pra frente." (C, análise §4)

## Passo 9 — O que só o dono sabe · PADRÃO CONSISTENTE (proposto), 3 de 3

**O que entra.**
- Uma seção de perguntas pro dono, com o que cada resposta muda (E traz essa seção).
- As categorias que apareceram: o custo da estrutura; receita e custo fora dos arquivos (o que passa
  por outro caixa); o que mudou na execução (em B, o formato do evento); confirmar o objeto (A: se o
  funil era só daquele público).
- Número antigo corrigido diz qual e por quê (B). Fonte que chega no meio vira seção
  datada (A). Decisão do Rodrigo vai pro arquivo do cliente, com a reversão escrita quando houver
  (regra da casa).

**Por quê.** Em B a conversa trouxe uma explicação concorrente pra leitura do ingresso barato, hoje registrada em
`sirius-scale/frameworks/lancamentos/produto-de-entrada.md`.

**Variações aceitáveis.** A pergunta pode ser respondida pelo próprio Rodrigo, sem reunião com o
dono (A traz "confirmado pelo Rodrigo" com data; B, "o Rodrigo confirmou"). Pergunta sem resposta
fica listada como aberta, com o que ela trava.

**Trecho real.**
- "A ressalva caiu: a imersão foi ONLINE" (B, comparação dos dois funis)
- "Isso é uma explicação concorrente à leitura de que o ingresso barato não qualifica." (B, ata da reunião)

## Passo 10 — Do diagnóstico ao plano · PADRÃO CONSISTENTE (proposto) na ordem e no que não fazer; VARIAÇÃO ISOLADA nos motores

O diagnóstico de terceiro termina em plano porque é isso que o dono leva: em B a reunião
terminou em decisão (o que fazer primeiro, o que fica de fora). O debriefing da casa termina em
decisão ranqueada (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §0 e
§7); aqui o plano ganha mais três partes: a ordem de execução, o que não fazer agora e, no modo
operação inteira, a arquitetura nova.

### 10.1 Ranking em reais, com hipóteses separadas · PADRÃO CONSISTENTE (regra do vizinho), 2 de 3 (A, B)

Cada item com quanto vale, o dado que sustenta, quanto custa testar e o que mede sucesso; o que
não tem número vai em hipóteses, fora do ranking. Está inteiro no
`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §7; aqui só se aplica. C
traz o mesmo bloco de "o que não dá pra afirmar hoje" quando falta dado.

### 10.2 A ordem de execução não é a ordem do ranking · PADRÃO CONSISTENTE (proposto), 2 de 3 (A, C) e E

**O que entra.** Depois do ranking, uma ordem de execução própria. Primeiro o que estanca e o que
mede, que é barato; depois o caixa; depois o crescimento; e o que é teste fica pra quando houver
medição. C começa pela checagem mais barata; A
põe medição e página antes de qualquer escala; E traz a mesma seção.

**Por quê.** O item que mais vale costuma depender de outro que vem antes.

**Variações aceitáveis.** Pelo custo da checagem
quando falta dado (C); medição antes de escala quando o painel está errado (A).

**Trecho real.**
- "É a checagem mais barata e a que muda tudo." (C, análise, o que eu faria)
- "Os quatro primeiros itens não são escala — são o que precisa estar de pé para que escalar signifique alguma coisa." (A, diagnóstico §8)

### 10.3 O que não fazer agora · PADRÃO CONSISTENTE (proposto), 1 de 3 (A)

**O que entra.** Uma lista do que o dono talvez queira fazer e o dado diz pra não fazer agora,
cada item com o número que sustenta: escalar verba com
medição quebrada (A).

**Por quê.** É o que estava na mesa: em A o pedido era escalar.

**Variações aceitáveis.** Não há evidência suficiente além desse caso.

**Trecho real.**
- "escalar verba agora multiplica o prejuízo." (A, diagnóstico §8)

### 10.4 Motores · VARIAÇÃO ISOLADA

A ideia de ter um motor contínuo, e não só o pico, apareceu em B (a reunião decidiu voltar o
foco pro perpétuo e o low ticket, em vez de novo lançamento gratuito) e como conselho falado em D.
É 1 plano escrito; segue VARIAÇÃO ISOLADA.

### 10.5 Verba em faixa quando o plano religa tráfego · VARIAÇÃO ISOLADA (A, B)

Piso, alvo e teto, com a condição pra subir; nunca um número travado. É regra da casa
(`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §7, item 6).

**Trecho real.**
- "Religar o tráfego em faixa, não em número" (A, diagnóstico §8)
- B, no debriefing do perpétuo §9: escala em faixa, com o alvo no dobro do piso e o teto "só com ROAS ≥ 2 por 7 dias seguidos".

## Passo 11 — Apresentar · VARIAÇÃO ISOLADA (forma vista em 1 caso: B)

**Por quê.** A reunião é onde o passo 9 acontece.

**O que entra e variações aceitáveis.** A forma que apareceu:

- **Documento interno + apresentação + reunião** (B, com o debriefing interno). O documento interno
  guarda o raciocínio inteiro; a versão do dono é outra peça, feita em cima dele. A regra de que a
  versão do cliente é outra peça já está no
  `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §6.

**O ponto de partida** (PADRÃO INCONCLUSIVO): abrir pelo que o dado mostrou do negócio do dono, não
pelo resultado de quem diagnostica.

## Passo 12 — Registrar · PADRÃO CONSISTENTE nos itens que já são regra da casa; VARIAÇÃO ISOLADA no que é de dono de fora

**O que entra.**
- A pasta do dono no lugar certo, com um arquivo que cataloga as fontes (C); dado puxado salvo
  junto com o jeito de refazer, a consulta, o filtro ou o export (B; em A, os arquivos do dia
  junto da análise); `funis/<nome>/desempenho.md` quando é perpétuo (A, B). É o que pede o
  `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §2.3 e §6.
- Candidatos a regra listados, não escritos (A, B), pela regra de registro
  (`sirius-scale/REGRAS.md` §5).

**Por quê.** O próximo diagnóstico do mesmo dono parte deste
(`sirius-scale/frameworks/trafego/_metodologia.md` §6.1), e no debriefing a regra é dura: "número
cuja origem morreu com a sessão não é número." Dado de cliente de empresa diferente não se mistura.

## Regras transversais

1. **Todo número tem arquivo e o jeito de refazer** (A, B, C). Regra da casa
   (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §2.3; número sem
   fonte rastreável não entra). C diz no topo: "Todo número aqui é reproduzível a partir desses
   dois arquivos" (`desempenho.md`).
2. **Medido e hipótese em blocos separados**, e hipótese fora do ranking (A, B, C). C marca os
   títulos com MEDIDO e HIPÓTESE. Regra do
   `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §7, item 4.
3. **Framework da casa entra como método, nunca como número** (passo 4, regra 3).
4. **A versão do dono mostra o número como foi**, inclusive quando contradiz o que se disse antes
   (B: a versão pro expert mostrou o mês ruim como ele foi). VARIAÇÃO ISOLADA.
5. **Sem projeção que o dono vá ler como promessa** quando o cenário vai mudar (B: o Rodrigo vetou
   a projeção do resultado do produto de entrada). VARIAÇÃO ISOLADA.
6. **Tom do vizinho**: estado atual antes do histórico, uma conclusão por parágrafo, tabela curta
   (`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §0).
7. **Em operação rodando, janela em toda frase** (A). Regra do
   `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §1.

## Exemplos reais consolidados

Os diagnósticos que aparecem neste kit, do que chegou ao primeiro passo do plano (resumo; os
números ficam no caso de origem).

| Caso | O que chegou | O que o dado mostrou | Maior vazamento ou gargalo | Primeiro passo da ordem | O que veio depois |
|---|---|---|---|---|---|
| A | como escalar | zero venda do produto do funil; o painel media outro produto; imposto desligado | visita → cadastro: 97% do gasto do período | separar o produto na medição, ligar o imposto, tirar da página o bônus vencido | campanha consolidada e perpétuo novo, sem o produto errado e com imposto, em pouco mais de duas semanas |
| B | o produto de entrada se sustenta? quanto dá pra investir? | parte dos produtos do CNPJ era de outro expert; o livro de entrada qualifica (17 de 151 sobem no upsell), o ingresso não (2 de 335) | a escala de um mês: retorno marginal perto de 1 | religar o perpétuo do livro em faixa | o foco voltou pro perpétuo |
| C | as vendas caíram? é saturação? | degrau num dia só em três frentes; o lançamento acabou no mesmo dia; o perpétuo não tinha sido canibalizado; 76% das vendas sem criativo nomeado | não medido: sem gasto no painel | conectar a conta de anúncios e olhar o gasto diário do mês | conta conectada três dias depois |

Dois esqueletos que se repetiram e servem de molde:

- **A tabela do que fazer** (A, B): número, o que fazer, quanto vale em reais, sustentação,
  custo de testar, como se sabe que deu certo. Seguida da ordem de execução e das hipóteses.
- **A tabela do limite** (C): cada pergunta do dono numa linha, com dá pra responder hoje, sim ou
  não, e por quê.

## O que é reutilizável e o que é do caso

**Reutilizável (é de processo, apareceu em donos e nichos diferentes):**
- Os passos 0 a 5 e 7 a 12, com as dependências da fórmula.
- A tabela de armadilhas do passo 2 como checklist de entrada. Cada armadilha nasceu de uma
  ferramenta, então serve pra procurar, não pra presumir.
- As categorias de pergunta do passo 9.
- A régua do próprio histórico quando não há plano, e a conta que tem que fechar quando não há
  histórico.
- A ordem de execução separada do ranking, com medição e estanque na frente.

**É do caso (não levar sem medir):**
- Todos os números, inclusive os efeitos da tabela de armadilhas.
- As armadilhas específicas do Dash Fácil (janela do perpétuo, venda de teste, parcelamento): valem
  pra quem usa o painel (`sirius-scale/frameworks/trafego/leitura-dash-facil.md`).

## Pontos em aberto

1. **Nenhum plano tem resultado.** Os planos de A a C foram apresentados ou viraram decisão, e
   nenhum foi medido depois. O passo 10 inteiro é NÃO TESTADO até um ciclo fechar.
2. **Não existe lista de pedido de dado.** O passo 1 reconstrói o que pedir pelo que chegou nos 3
   casos e pela ordem de uma triagem oral (D). Se o Rodrigo tem uma lista fixa, ela entra no lugar.
3. **Parar ou seguir sem dado de gasto.** O
   `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §2.4 manda parar sem
   lead casável, gasto e plano. C seguiu sem gasto, com o escopo declarado, e terminou numa
   checagem concreta (o gasto diário da conta). Não está decidido se isso vale como entrega.
4. **Por onde abrir a reunião de apresentação** (passo 11): PADRÃO INCONCLUSIVO.
5. **Horizonte do plano.** O inventário da casa
   fala em plano de 30 dias, e não há evidência de um.
6. **Tempo e esforço.** Nos casos, o trabalho escrito saiu no mesmo dia ou no seguinte ao dado
   estar em mãos, e, no caso com reunião registrada (B), ela veio em até uma semana. Horas de trabalho
   não foram medidas.
7. **Motor contínuo como recomendação recorrente** (10.4): 1 plano escrito e um conselho falado.
   Hipótese a confirmar no próximo diagnóstico de negócio que dependa de pico.
8. **Análises avulsas que o Rodrigo faz fora destes diagnósticos** não estão na base. Com
   algumas delas, os passos ganhariam contagem e as armadilhas, frequência.
