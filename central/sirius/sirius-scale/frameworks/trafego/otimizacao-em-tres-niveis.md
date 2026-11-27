# Otimização de tráfego em três níveis: orçamento, público e criativo

> **Desde a v0.5: quatro níveis.** A página entrou como quarto nível (§7.1), por decisão do Rodrigo: "a otimizacao nao
> deve ser só de trafego". O nome do arquivo ficou, pra não quebrar quem aponta pra ele.

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método de otimização (decisão do Rodrigo) e o que já foi medido em cima dele.
> **Alcance:** o método vale pra qualquer campanha, nas palavras dele (§1). Os limiares, os
> números e os casos são NÃO TESTADO FORA: base de um lançamento só, a captação de uma Black do
> caso-base (um expert de educação, no nicho de concurso).
> **Origem:** conversa do Rodrigo sobre a leitura diária de tráfego. As falas são literais, de
> transcrição de áudio, por isso o português falado.
> **Do lado de vocês:** na casa, a régua e as contas rodam em código, lendo Meta, Google e Dash.
> Aqui quem lê é o agente `gestor-trafego`, pelos conectores, e quem aplica verba, liga e pausa é a
> pessoa dona da conta (`sirius-scale/REGRAS.md` §6). Rotina agendada é opcional
> (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §8).

## 1. Os três níveis — decisão do Rodrigo, regra da casa; o que foi medido em cima dela é VARIAÇÃO ISOLADA

"na minha opinião, existem três níveis de otimização de tráfego. Primeiro, orçamento. Tirar do
que está caro e colocar no que está barato. Resumidamente é isso. Segundo, público. Testar novos
públicos, agregar públicos, aglomerar ou expandir. Testar públicos que ainda não foram usados."
E o terceiro: "E o terceiro nível de otimização são os criativos, que é desligar o que está caro
e ligar o que não rodou ainda."

| Nível | O que faz | O que a leitura pergunta todo dia | Onde está a regra |
|---|---|---|---|
| 1. Orçamento | tira do caro, põe no barato, dentro da faixa da fase | quem está abaixo da linha de escala sobe; quem passou do corte desce | lote e decisões de verba (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §5) |
| 2. Público | testa o que nunca rodou, junta, abre (Advantage onde a fase deixa) | sobrou verba até o alvo ou algum público saturou? Que público da conta o lançamento não usa? | sugestão de público (§5 deste arquivo) |
| 3. Criativo | desliga o caro, liga o que não rodou, procura o campeão | quem está caro, quem está ligado e não recebe verba, quem nunca rodou, quem ganha numa unidade e não está na outra | troca e rotação (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §5); sem verba, nunca rodou e campeão (§3 e §4 deste arquivo) |

**Os três, sempre, nessa ordem de leitura.** Numa unidade com público cansado, o criativo vem
antes da verba: a subida fica segurada enquanto a rotação está em curso
(`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §5). Isso já estava dito semanas
antes ("olha os criativos antes de mexer em verba") e demorou a virar regra de leitura.

**Alcance, nas palavras dele:** "essa lógica de otimização serve para qualquer tipo de campanha".
Lançamento gratuito, pago, perpétuo, low ticket, distribuição: muda a régua de cada nível (CPL,
custo por MQL, ROI), não os três níveis.

## 2. Por que o criativo pesa mais — decisão do Rodrigo; o caso contado é relato, PADRÃO INCONCLUSIVO pra nós

"eu acredito que o criativo é o 80-20 do tráfego hoje em dia, porque os públicos, né, a maioria a
gente já é uma configuração padrão". E: "você muitas vezes está a um criativo de dobrar o seu
resultado. Porque um criativo pode derrubar o custo por lead pela metade e a gente dobrar a lista."

O caso que ele contou é **relato, não medição nossa**: na Black de outro expert do mercado, dois
anos antes, um estático feito pela equipe de tráfego, apelidado de toscão, baixou o custo do lead de
aluno pra menos da metade, e eles escalaram muito mais no público de aluno. É a referência do molde
de toscão em `sirius-scale/frameworks/design/captacao-da-black-arte-do-estatico.md` §2.3.

## 3. Ligar não é testar: o criativo sem verba — VARIAÇÃO ISOLADA (uma Black do caso-base)

Num conjunto com vários anúncios, a plataforma escolhe cedo onde pôr a verba e o resto quase não
roda. Ligar um criativo novo dentro de um conjunto assim não garante que ele seja testado.

**Medido em duas semanas de captação (Meta, com imposto):**

- Os estáticos levaram 3,7% do gasto, com CPL na mesma faixa dos vídeos (uns 10% mais barato).
- O toscão de aluno ficou ligado desde o primeiro dia e levou uns 2% do gasto do conjunto: 7 inscritos,
  a menos de um quinto do CPL do vídeo que dominava esse conjunto.
- O toscão de não aluno nunca foi ligado.

Com 7 inscritos nada se afirma sobre esse estático. O achado é outro: **ele nunca foi testado**, e a
rotina chamava isso de "observar". Daqui em diante, criativo ligado que não recebe verba é um
achado com nome próprio ("sem verba"), não um "observar".

**A regra (limiares PADRÃO INCONCLUSIVO, um caso; cada lançamento pode trocar os dele, com a fonte, em
`frameworks-da-casa/`):**

- **Sem verba:** criativo ativo numa unidade com 2 ou mais ativos, com gasto em pelo menos 3 dias
  diferentes (prova de que estava ligado) e fatia do gasto acumulado da unidade abaixo de 10%. Se o
  CPL dele, mesmo com a margem de erro pro lado ruim, ainda fica abaixo da linha de escala do
  segmento, ele é **promissor**.
- **O que se propõe:** teste de verdade, com verba própria, montado pausado pelo agente de tráfego e
  ligado por quem é dono da conta. Na Meta há dois caminhos: o teste de criativo nativo dentro da
  campanha (verba separada pros anúncios em teste, pela API em `ad_studies`) ou um conjunto por
  criativo com o mesmo público. No Google, o experimento A/B de criativo do Demand Gen. Os dois estão
  em `sirius-scale/frameworks/trafego/radar-plataformas.md`.
- **Ligar também tem custo:** na Meta, a página oficial diz que ligar anúncio novo num conjunto faz
  ele voltar pro aprendizado (a medição que conta contra está em
  `sirius-scale/frameworks/trafego/radar-plataformas.md`). Por isso a leitura propõe ligar no máximo um
  por unidade por dia.
- **A rotação não tira quem não foi visto.** A rotação só deixa sair quem levou pelo menos 10% do
  gasto acumulado da unidade. Antes disso, o toscão de aluno sairia como "o mais visto" sendo o menos
  visto da unidade.

**Primeiro teste com verba própria. VARIAÇÃO ISOLADA, resultado pendente.**

- Medido antes: a imagem levava de 0% a 6% do gasto nos conjuntos com vídeo. O toscão de aluno estava
  ligado e gastou zero no dia.
- Caminho escolhido: um conjunto por criativo, com um anúncio só.
  - Aluno: um conjunto só de estático, mesmo público do principal. O público de aluno é fechado e não
    tem como ser dividido.
  - Não aluno: um conjunto de público quente de 14 dias (quem se envolveu com a Black ou com o perfil
    e não se inscreveu), desenho do Rodrigo.
- Os conjuntos de leads e de envolvimento não excluem o público quente. Como o conjunto novo só tem
  imagem, excluir tiraria da pessoa mais quente o vídeo que converte. Vira exclusão se o quente gastar
  menos de 70% do orçamento no primeiro dia, que é o sinal de que a sobreposição está travando a
  entrega.
- Como decidir: depois de 2 dias, ou de um gasto mínimo definido antes, comparar o CPL com a linha do
  segmento. Abaixo da linha de escala, entra a segunda imagem no mesmo conjunto.

**Segundo lote, agora com vídeo e no Google. VARIAÇÃO ISOLADA, resultado pendente.** Ligado com o ok do
Rodrigo, depois de ver a verba de cada um.

- Meta: um conjunto por criativo, no público e nas exclusões do conjunto principal de leads, com a
  mesma verba por dia. Entraram o vídeo com o melhor CPL desse conjunto (3,4% do gasto), uma imagem que
  nunca tinha rodado no público de leads e um vídeo com 1,7% do gasto no conjunto de envolvimento. A
  verba repete a do conjunto quente: no piso, nenhuma célula chegaria aos 15 inscritos da escada em
  2,5 dias.
- Google: uma campanha por criativo, porque o Demand Gen não tem orçamento por grupo
  (`sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §14). Um vídeo no aluno e um no não
  aluno, cada um no piso de orçamento. O experimento A/B do Demand Gen ficou de fora por três motivos:
  com lance por conversão ele pede 50 conversões por braço, duplica a campanha com o orçamento dela, e
  nenhuma ferramenta da casa cria experimento.
- Antes de montar, o agente de tráfego tirou dois dos criativos pedidos: no Google, já levavam 27% e
  34% da campanha desde que entraram. O alarme de "sem verba" usou a fatia do acumulado desde o início,
  que conta os dias em que eles estavam pausados (ponto em aberto 1).
- Como ler: o inscrito do Dash por conjunto (`utm_content`) na Meta e por campanha (`utm_campaign`) no
  Google. Célula que gastou menos de 70% do orçamento fica "não testada", nunca perdedora.

## 3.1 Criativo cansando com a frequência baixa: o sinal vem antes da venda cair — PADRÃO INCONCLUSIVO (1 anúncio, 1 semana)

A troca por público saturado (frequência alta e custo subindo) foi pensada pra público fechado. No público aberto a
frequência fica baixa (perto de 1,5) e o criativo cansa do mesmo jeito. Dois sinais medidos no único anúncio que vendia:
1. **Gancho (3 s ÷ impressão), metade contra metade da janela.** Caiu de 35,9% pra 33,4% (z = 2,39), dentro de cada
   posicionamento, então não era a Meta mudando onde entrega. Cair em 4 de 5 dias, sozinho, não prova nada.
2. **Gente nova por impressão caindo:** o alcance que cresceu no dia dividido pelas impressões do dia. Foi de 76% pra
   53–56% em 5 dias. A entrega passa a repetir quem já viu.

**O que fazer com o sinal:** ter o próximo criativo pronto e no ar com verba própria (§3), não pausar o que vende.
## 4. Nunca rodou e campeão — VARIAÇÃO ISOLADA

- **Nunca rodou:** reserva pausada, aprovada, sem gasto na unidade, fora da lista de fora da rotação
  do segmento (a lista de quem não serve praquele público; do lado de vocês, em `frameworks-da-casa/`). Propõe ligar (sem pausar ninguém)
  quando a unidade não tem troca nem rotação no dia, não ligou criativo novo nos dias de leitura e tem
  menos de 6 anúncios ligados (número do caso). Um por unidade por dia, preferindo o formato que a
  unidade não está rodando (estático onde só roda vídeo, e vice-versa: é a lição do toscão). Mesmos
  filtros e mesma espera da rotação, pra nunca propor duas ações pro mesmo criativo.
- **Campeão:** a referência de uma unidade (melhor CPL com volume, ou melhor custo por MQL quando a
  pesquisa tem respondentes) que existe pausada e sem gasto em outra unidade do mesmo segmento e da
  mesma plataforma vira proposta de ligar lá. Se ele nem existe na outra unidade, vira sugestão de
  subir o anúncio.
- **O id do criativo inclui a versão.** Regravação ou arte nova ganha sufixo
  (`sirius-scale/frameworks/trafego/nomenclatura.md` §1, regra 2) e é outro anúncio: o `IMG 07.1` é a
  correção do `IMG 07` (números inventados, os mesmos exemplos da nomenclatura). A leitura por criativo, o campeão e a lista de fora da rotação comparam o id
  inteiro. Quando o ponto cortava o id, a leitura mostrava o mesmo `IMG 07` duas vezes nas unidades que
  tinham as duas artes, e um campeão `IMG 07.1` levaria a arte antiga pra outra unidade. A lista de
  fora é por id exato: `"IMG 07"` tira só a arte antiga. Versão nova de um criativo que está fora (um
  `VD 24.1`) não herda a exclusão, porque versão pode trocar o gancho (num lançamento pago, três
  versões do mesmo vídeo eram ganchos diferentes rodando juntos). Se mantiver o gancho, entra na lista
  à parte. Isso depende de alguém lembrar; não virou checagem.
- ⚠️ **Reserva não sabe que uma versão aposentou a outra.** A reserva sai pela ordem do nome, e
  `AD - IMG 07 - …` vem antes de `AD - IMG 07.1 - …`. Num conjunto, a reserva tinha as duas artes nunca
  ligadas ali, e o "nunca rodou" escolheria a antiga. Enquanto não houver marca de aposentado no
  registro, a arte superada vai na lista de fora do segmento. No caso, a arte antiga já tinha ido pro
  ar por outro caminho: entrou no conjunto num pedido de pôr todos os estáticos de cada campanha no
  conjunto de estáticos, e foi ligada junto com as outras reservas pelo Gerenciador. Montar conjunto
  com todos os estáticos leva a versão superada se ninguém tirar, e a lista de fora não desliga
  anúncio ligado. Isso também não virou checagem.

## 5. Proativo no público — VARIAÇÃO ISOLADA

"tem que ter esse olhar proativo de pensar, pô, será que temos verba e possibilidade de testar
novos públicos? Seja com advantage ativado em um lançamento gratuito, ou no caso da Black,
verificar se estamos usando todos os públicos, inclusive os de vídeo view".

**Gatilho:** a projeção da fase fecha abaixo do alvo (sobra verba) ou alguma unidade está saturada
(no caso, frequência do gerenciador a partir de 4). Sem nenhum dos dois, não se sugere público: teste
sem verba pra rodar ou sem motivo vira ruído.

**Candidatos:** públicos da conta que o lançamento não usa em nenhuma unidade (inclui nem exclui),
do tipo que serve à família do segmento (vídeo, engajamento, site e lista de lead pra não aluno;
lista e pixel de compra pra aluno), com tamanho mínimo e em uso pela plataforma. A sugestão diz o
gatilho, a verba que sobra e os candidatos com tamanho. **A leitura nunca cria conjunto nem liga
Advantage sozinha:** o agente monta pausado e quem é dono da conta decide.

**Limites que não se negociam:** a exclusão da família vem sempre junto (aluno fora do não aluno,
lead fora do envolvimento, inscrito da fase fora de tudo), e Advantage de público só em captação
fria: em fase que mira quem já está dentro, os dois interruptores desligados
(`sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.1 e §4.3).

**Na Black do caso-base:** ela já usava video view. Na Meta, o conjunto de envolvimento incluía 25%
de todos os vídeos e 25% e 75% da distribuição em 365 dias, mais os 15 segundos das captações de três
lançamentos anteriores. No Google, o de envolvimento incluía quem viu vídeo, se inscreveu, curtiu ou
acessou o canal. E sobrava verba: no ritmo do dia, a captação fechava uns 25% abaixo do alvo.

**Primeiro teste de público. VARIAÇÃO ISOLADA, resultado pendente.**

- Dos cinco públicos candidatos, dois entraram na Meta: o video view de 15 s da captação de um
  lançamento anterior e o de 3 s das lives de outro. Foram pra um conjunto de verba baixa na campanha
  de não alunos, que exclui também tudo o que o conjunto de envolvimento inclui, pra não disputar o
  leilão com ele (`sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.8). Gente nova abaixo de
  ~1.000 pessoas: a estimativa da Meta ficou no piso.
- Os dois de site saíram: um pode ter comprador dentro, o outro é subconjunto da exclusão de leads.
  Uma lista ficou de fora porque a origem dela não está documentada.
- No Google, o pacote recomendou não subir. Os públicos já estavam no conjunto de envolvimento, e a
  verba que sobrava foi pra ele no mesmo dia.
- O que já dá pra tirar, antes do resultado: nessa Black a sobra de verba não vinha de falta de
  público. O envolvimento da Meta tinha alcançado cerca de um quinto do público estimado, com
  frequência de 2,58. O que aproxima do alvo é o degrau de verba nos conjuntos grandes.

## 6. Pesquisar o que mudou nas plataformas — decisão do Rodrigo; o processo é recente, VARIAÇÃO ISOLADA

"vale a pena, de vez em quando, também analisar a central de ajuda e pesquisar na internet o que
vem funcionando no momento, uma nova configuração, porque o Meta vive mudando, não só o Meta, o
Google também".

- Na casa, uma tarefa agendada lê toda semana a central de ajuda da Meta e do Google Ads e as notícias
  da semana, uma entrada por novidade, com link e data. O resultado está em
  `sirius-scale/frameworks/trafego/radar-plataformas.md`.
- **Fato só com fonte oficial**; blog e agência entram marcados como opinião de terceiro.
- Novidade que muda como se testa criativo ou público vira sugestão de teste, com a fonte. Nunca vira
  configuração ligada sem passar pelo dono da verba.

## 7. No relatório do dia — VARIAÇÃO ISOLADA

O relatório segue os três níveis: as ações de hoje (lote de verba, decisões e sugestões) ficam numa lista
só, agrupada por orçamento, público e criativo, e, por unidade, aparece a fatia de verba de cada criativo,
marcando campeão, sem verba, nunca rodou e caro. Peçam o relatório do `gestor-trafego` nesse formato. O que
monta coisa nova vira pedido ao agente, que monta pausado; aplicar segue com a pessoa dona da conta, na
plataforma.

## 7.1 Quarto nível, a página, e o pedido de criativo novo — decisão do Rodrigo; o que foi medido é VARIAÇÃO ISOLADA

Pedido dele: "a otimizacao nao deve ser só de trafego", e o que faltava no relatório: "so tem um cirativo rodando, por que
nao sugere novos? novos publicos se fizer sentido", e "propor melhoria ou teste a/b de pagina".

| Nível | O que o relatório pergunta |
|---|---|
| 2. Público | sobra verba até o alvo do planejamento? Que público da conta o funil não usa? |
| 3. Criativo novo | o funil tem menos criativos no ar que o mínimo dele? Pede ao `copy`, partindo do que vendeu e longe do que gastou sem vender |
| 1 e 3, funil esvaziado | a verba no ar está abaixo do piso do planejamento? Quais peças pausadas já venderam? Algum front sem nada no ar? (A régua por peça só julga peça ligada e fica muda quando tudo foi pausado.) |
| 4. Página | o que o Microsoft Clarity mostra (rolagem, clique morto, erro de script, volta rápida) e a conversão da visita paga em venda |

- **Sempre um teste A/B por página com amostra** (30 sessões ou mais em 3 dias). Rolagem baixa propõe o teste da primeira
  tela. As variações que já existem sem tráfego entram no texto, pra não criar outra igual.
- **A régua de comportamento é PADRÃO INCONCLUSIVO** (erro de script 2%, clique de raiva 3%, clique morto 10%, volta
  rápida 15%): chute de partida, serve pra mandar olhar as gravações, não pra concluir.
- **A rolagem da exportação do Clarity é média por sessão**, não "quantos chegam ao botão". No tráfego pago, cada
  endereço com `fbclid` é uma sessão: filtrando os endereços com uma sessão só, dá pra contar quantos chegam ao botão.
- **"Erro de script" do Clarity costuma ser do navegador do Instagram/Facebook, não da página** (só aparece em sessão
  com `fbclid`, na mesma taxa em páginas diferentes). Separar a taxa por origem antes de mexer na página.
  Como provar (VARIAÇÃO ISOLADA, 1 página): no MCP do Clarity (`query-analytics-dashboard`), pedir "erros de
  JavaScript por navegador" e "mensagens de erro". No caso medido, todos os erros vinham do navegador de dentro do
  Instagram e do Facebook, quase todos `Error invoking postMessage: Java object is gone` (a ponte do navegador do app no
  Android). Com o código da página conferindo se cada elemento existe e o botão de compra sendo link puro, o número não
  mede defeito. A exportação não separa por navegador; as duas consultas entram nas 10 por dia.
- **Cota:** o Clarity dá 10 chamadas por projeto por dia. A exportação traz todos os endereços do projeto numa só.
- **Quem monta:** página vai pro `webdesigner` (texto novo passa pelo `copy` e pelo `/humanizer`), criativo novo pro
  `copy`, público pro `gestor-trafego`. Nada liga nem vai pro ar sem a pessoa dona da conta.
- O mínimo de criativos no ar é do funil (o low ticket pede 3). Funil sem esse número no briefing não recebe a sugestão.
## 8. O que transfere e o que é do caso

**Transfere (decisão do Rodrigo pra qualquer campanha):** os três níveis e a postura proativa
(§1, §5, §6); perguntar, em qualquer conjunto com vários anúncios, se o criativo ligado está
mesmo recebendo verba (§3); a rotação que não tira quem não foi visto.

**É do caso (uma Black, um lançamento):** todos os números do §3 e do §5; os limiares (fatia e dias de
"sem verba", máximo de anúncios ligados, exposição mínima da rotação); o toscão como formato que ganha.
Ao aplicar, dizer na entrega que o limiar veio de lá.

## 9. Excluído de propósito

- **Escolher campeão por MQL com poucos criativos.** O campeão aqui é a referência da unidade
  (melhor CPL com volume, ou custo por MQL quando a pesquisa tem respondentes); MQL sozinho não
  ranqueia criativo (`sirius-scale/frameworks/trafego/mql-e-qualificacao.md`).
- **Venda como régua na captação.** Na captação a régua é a do plano (CPL e custo por MQL contra
  as linhas do segmento); venda fecha o lançamento no debriefing, não decide criativo no meio.
- **Semente de lookalike e interesse.** Ficam em
  `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4; aqui só entra a pergunta de que
  público a conta tem e o lançamento não usa.

## 10. Pontos em aberto

1. Os limiares de "sem verba" (fatia e dias com gasto) não foram medidos: saíram de um caso. E a fatia
   é calculada sobre o acumulado da unidade, então criativo que entrou tarde aparece "sem verba" mesmo
   levando um terço da campanha. Foi o caso de dois vídeos no Google. A proposta é contar a partir do
   primeiro dia com gasto, ou só na janela.
2. Teste com verba própria em público pequeno e fechado (aluno) disputa a mesma pessoa com o conjunto
   principal. Pode encarecer os dois; ninguém mediu ainda.
3. Se a Meta e o Google têm recurso oficial de teste de criativo que a API alcance: a primeira leitura
   está em `sirius-scale/frameworks/trafego/radar-plataformas.md`.
4. O resultado da rotação no público de aluno e o do toscão ainda não foram lidos.
