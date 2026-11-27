# Rotinas de lançamento: uma por função, o lançamento é dado

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** operação (como as tarefas agendadas do Claude Code trabalham um lançamento).
> **Alcance:** `NÃO TESTADO FORA`. Base: as 12 rotinas de um lançamento gratuito do caso de origem
> (da captação ao carrinho) e a primeira rotina no desenho novo, a de tráfego da captação de uma Black
> do mesmo cliente. O desenho (rotina por função + calendário no lançamento) é mecânica de operação e
> deve transferir pra qualquer cliente; a régua da captação (§5) é do caso e vem com rótulo linha a linha.
> **Pedido que originou** (Rodrigo): "eu quero criar um padrão de rotinas sempre que a
> gente for fazer uma ação... se eu for criando várias e várias rotinas, vai ficando um monte aqui, e
> eu acabei tendo que deletar as rotinas do lançamento [...]".
>
> **Do lado de vocês, só a rotina de tráfego vem pronta** (`sirius-scale/rotinas/trafego-diario.md`). Os
> scripts e as outras rotinas da casa dependem das contas e da máquina de lá e não fazem parte do kit. O que
> está aqui é o **desenho**, pra montar com tarefas agendadas do Claude Code se vocês quiserem (§8), e os
> erros que custaram rodada na casa. Escrita em plataforma de anúncio segue `sirius-scale/REGRAS.md` §6: o
> Claude lê e propõe, quem aplica é o dono da conta.

## 1. O problema, medido no lançamento anterior

No lançamento anterior cada função virou uma rotina com o nome do lançamento, e cada rodada de verba
virou um script:

- **12 rotinas com o código do lançamento no id**: otimização (2 versões), relatório de tráfego,
  orçamento do remarketing, exclusão de público, WhatsApp, lives, pesquisa, uma conferência financeira do
  cliente, conferência do downsell e a mensagem de bom dia. Acabou o lançamento, sobraram rotinas pra
  apagar à mão. O app tira a rotina da lista, mas a pasta dela continua no disco.
- **Nenhum script das rotinas recebia o lançamento como parâmetro.** Trocar de lançamento era editar
  código: o código do lançamento, a pasta de dados e o nome do público, no topo de cada um.
- **Um script de verba por dia:** cinco versões do script de otimização, uma por rodada, cada uma com a
  decisão escrita no código. Era código novo de escrita, sem teste, toda rodada.

E o que custou rodada (fonte: o mapa das rotinas feito no dia do pedido, com o caso de cada uma):

| Lição | O que aconteceu |
|---|---|
| Rotina com navegador do usuário falha e custa caro | a otimização pelo navegador real, logado, foi pausada ("muito longo e um pouco falho") e refeita só com script e credenciais num arquivo de ambiente. Rotina agendada não tem garantia de achar o navegador aberto e logado |
| Diagnóstico escrito no prompt se reinjeta | "nenhuma campanha do Google tem meta de conversão própria" era leitura do campo errado e apareceu em 4 relatórios seguidos. A instrução da rotina carrega **método** (o que conferir e como ler), nunca a conclusão de um dia |
| Lista fixa de fase cega a rotina | o acompanhamento de gasto parava na última fase de uma lista escrita no código; no primeiro dia do carrinho teria reportado só uns poucos reais de gasto, porque as campanhas do carrinho não estavam na lista |
| Rotina sem data de fim roda depois de perder o sentido | a de lives rodou até a noite da 1ª aula; a de orçamento parou com fases ainda no envelope; três calendários divergentes |
| Caminho fixo quebra quando a pasta muda | a pasta do cliente mudou de lugar e 6 rotinas ficaram no caminho velho |
| Run que morre no 1º comando | três rotinas (a conferência financeira, a pesquisa e a conferência do downsell) acabaram sem texto nem arquivo. Medido depois: a 1ª rodada da rotina de tráfego e duas rodadas de outra rotina terminam num comando sem retorno, com status "succeeded" e menos de 1 min. Em cada uma, o comando que parou é o primeiro fora da lista de permissões do projeto (o `settings.local.json` da pasta `.claude`). A tarefa criada num turno que não foi digitado no app não guarda o modo de permissão (aviso da própria ferramenta). O pedido de aprovação não aparece na transcrição: causa por inferência forte, mecanismo conferido em 5 transcrições de 4 tarefas |
| Regra de verba escrita com um número só | a rampa da Black usou o corte de um segmento (não aluno na Meta) em todos os conjuntos, com as linhas por segmento já no plano de tráfego e a decisão do Rodrigo de pagar mais pelo aluno já registrada. Ele repetiu no dia seguinte |
| O Dash pelo navegador é o elo fraco | seletor de lançamento preso em outro lançamento, export sem parte dos leads, perfil logado na conta de outra pessoa (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §4.3) |
| Computador desligado é rotina parada | um funil ficou 28 h sem rodar. A tarefa agendada do Claude Code roda na máquina onde foi criada, com o app aberto |

## 2. O desenho

### 2.1 Rotina é por FUNÇÃO, permanente

A tarefa agendada tem o nome do que ela faz (a de vocês é a `trafego-diario`), nunca o do lançamento. Ela é
criada uma vez e fica. A cada rodada ela pergunta **quem está em qual fase hoje** e trabalha só nesses.
Sem lançamento na fase, sai em segundos ("nada a fazer"). Fim de lançamento não exige apagar nada.

### 2.2 O lançamento declara o próprio calendário: `rotinas.json`

**A tabela abaixo é o arquivo completo da casa. Do lado de vocês, vale o modelo simples,
`sirius-scale/modelos/rotinas.json`:** `lancamento`, `dash`, `contas`, `fases` (`inicio`, `fim`, `rotinas`),
`verba_dia` (`piso`, `alvo`, `teto`), `segmentos.<seg>` (`filtro_no_nome`, `linha_escala`, `linha_corte`,
`custo_por_mql_ref`) e `_historico`. É em cima desses campos que a rotina de vocês foi escrita
(`sirius-scale/rotinas/trafego-diario.md`). O resto deste §2.2 mostra até onde o arquivo chegou na casa, não
o que vocês têm que preencher.

Mora na pasta do lançamento (`lancamentos/<AAAA-MM-nome>/rotinas.json`; funil perpétuo em
`funis/<nome>/`). É o interruptor e é onde ficam os números da régua, cada um com a fonte:

| Campo | O que é |
|---|---|
| `lancamento`, `empresa`, `cliente` | identificação; com mais de um negócio ou expert na mesma pasta, é o que impede de cruzar dado de um com o outro |
| `dash.subconta_id`, `dash.lancamento_id` | de onde vem o lead (o Dash é a fonte do lead) |
| `contas.meta`, `contas.google` | contas de anúncio. Com mais de uma conta na operação, o token da Meta sai da conta, nunca de um token padrão: dois clientes da casa abrem com tokens diferentes (`sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`, seção do erro 403). Sem `google`, a rotina lê só a Meta |
| `fases.<fase>` | `inicio`, `fim`, `registro` (o JSON das campanhas da fase) e `rotinas` (quais trabalham nela). Fases: `antecipacao`, `captacao`, `aquecimento`, `cpl`, `carrinho`, `downsell`, `conteudo` |
| `captacao.unidades` | cada conjunto (Meta) ou campanha (Google) com o `segmento` e a chave da `faixa` no registro |
| `segmentos.<seg>` | `linhas` de escala e corte por plataforma, `qualificacao` (`mql` ou nada), `base_fechada` (lista que limita o público) e `frequencia_dia` do plano |
| `qualificacao` | planilha da pesquisa, abas e a regra de MQL (E entre perguntas) |
| `regua` | só o que muda da régua padrão (§5), com a fonte |
| `saida` | pasta e prefixo dos relatórios |
| `_historico` | toda mudança de número, com data e quem decidiu |

Conferir sempre antes de a rotina usar o arquivo (na casa, um script faz isso; do lado de vocês, peça ao
Claude que confira): data fora de formato, fase inventada, tráfego sem id do Dash = ERRO, e a rotina não
usa o arquivo.

**Perpétuo, na casa: o que o `rotinas.json` do funil tem a mais.** A rotina de vocês cobre lançamento;
perpétuo ainda não. Na casa, a conferência cobra os três primeiros quando a fase `perpetuo` tem a rotina de
tráfego:

- `contas.meta` e `filtro_meta`: a leitura da Meta é por nome de campanha (CONTAIN), e o filtro de cada
  front tem que conter o `filtro_meta`, senão a leitura não traz o front;
- `frentes.<front>`: `filtro` (nome de campanha), `preco` e `custo_maximo`. Custo máximo `null` deixa a
  régua só observando e o relatório diz que falta: foi o caso de um funil de outro expert da casa, que
  não tinha o número em arquivo nenhum. A régua padrão é a do low ticket
  (`sirius-scale/frameworks/lancamentos/low-ticket.md` §8) e não transfere sozinha pra outro ticket;
- `utm_anuncio`: o campo da UTM que traz o nome do anúncio na venda do Dash. Num dos funis é o `utm_term`
  (o `utm_content` é o conjunto); no outro é o contrário. Errado, a venda conta na peça e some da leitura
  por criativo (o relatório avisa quantas);
- `leitura_dias` (opcional): lê só os últimos N dias, pra funil antigo;
- `planejamento.verba_dia` (opcional): piso, alvo e teto por dia na plataforma, com a fonte, e `dias` (o
  horizonte). A simulação projeta essa faixa no custo por venda medido na janela; funil com planilha usa
  a planilha, igual aos lançamentos. Sem nenhum dos dois, o relatório diz que falta o planejamento.

Casamento da venda: uma compra = os itens com o mesmo `sck` (front + bumps), presa à peça pelo
`utm_campaign` e ao anúncio pelo `utm_anuncio`. VARIAÇÃO ISOLADA (2 funis, de dois clientes).

**Antes da campanha existir.** A captação pode entrar no `rotinas.json` com as datas antes de ter
campanha, Dash ou planejamento. Na casa, enquanto a fase não tem o registro das campanhas, a rotina não lê
inscrito nem aplica régua: ela escreve "o que falta pra captação rodar" (campanha, planejamento, Dash, conta
da Meta abrindo com o token certo, Google). Por isso, lá, o id do Dash só é obrigatório depois do registro (ou
em perpétuo). Do lado de vocês, arquivo sem o id do Dash fica de fora da rodada, e a rotina diz qual e por quê.
VARIAÇÃO ISOLADA (1 lançamento).

### 2.3 Três metades, cada uma com um dono

1. **Leitura e cálculo (a metade burra):** lê plataforma, Dash e pesquisa, calcula, aplica a régua e
   escreve o relatório + o **plano em arquivo com o lote proposto**. Nunca escreve em plataforma. Na casa
   é um script; numa rotina de vocês, o Claude lendo pelos conectores e seguindo a régua do `rotinas.json`.
2. **Claude na rotina:** confere o relatório, julga o que a parte de cálculo não julga (o que a instrução
   da rotina manda olhar), escreve o resumo pro dono da verba. Carrega **método**, nunca o diagnóstico de
   ontem.
3. **O dono da verba:** confirma o lote por escrito, na conversa. A confirmação é dele, ou de quem ele
   liberar naquele cliente; quem foi liberado confirma só dentro da faixa do plano. Do lado de vocês, quem aplica verba é sempre a pessoa
   dona da conta, no Gerenciador (`sirius-scale/REGRAS.md` §6): o Claude monta pausado, mas não mexe em verba.
   Na casa, a aplicação passa por **um executor só**, o mesmo pra qualquer lançamento, com as travas abaixo.
   Do lado de vocês, elas servem de checklist pra quem aplica à mão:
   - a prévia mostra o **código do lote**, e a aplicação exige esse código. Se o arquivo mudou entre a
     prévia e o ok, recusa;
   - recusa plano de outro dia, valor "de" que não bate com a conta, teto, piso do Google, orçamento
     compartilhado, objeto parado e subida acima de 50% (essa, só com uma autorização a mais, explícita);
   - valida o Google a seco antes de qualquer escrita, escreve a Meta em lote, para se a Meta falhar e lê
     tudo de volta;
   - grava a mexida num arquivo de estado, atualiza o orçamento no registro da fase (as conferências
     comparam conta × registro) e deixa um plano de reversão.
   **Sem resposta viva do dono, nada roda** (rotina não se autoriza).

**Pausar várias campanhas em série esbarra no limite da conta (VARIAÇÃO ISOLADA).** A decisão de pausar
do executor é uma campanha por chamada, e cada uma custa umas 5 chamadas à Meta: a leitura de campanha
passa antes por uma busca de conjunto que volta vazia, e roda antes e depois da escrita. Numa noite, num
funil de low ticket do caso de origem, 10 prévias e, logo depois, 7 pausas em 24 segundos (uns 55 pedidos
no total) bateram o erro 17 (subcódigo 2446079) na 7ª.
A espera de 5 minutos do próprio executor não bastou: a escrita saiu e a leitura de volta não. A conta voltou a
responder em menos de 15 minutos. Até o executor aceitar várias decisões num lote só (o padrão da casa pra API
da Meta é juntar pedidos num lote, guardar a leitura em cache e esperar cada vez mais quando der erro 17),
pausar várias é uma de cada vez, com um minuto entre elas. Leitura de volta que falhou se confere com uma
leitura só antes de repetir a decisão; repetir numa campanha que já pausou não escreve nada, o executor recusa
como decisão velha.

As peças, na casa: um interruptor (lê o calendário dos `rotinas.json`), a leitura da captação, a régua
(cálculo puro, sem ler nem escrever nada), a leitura do Dash pelo MCP e o executor. Cada peça tem teste, e a
rotina roda os testes antes de ler qualquer conta e para se um falhar.

### 2.4 O Dash entra pelo MCP, não pelo navegador

Desde o desenho novo a rotina lê os inscritos com UTM pelo MCP do Dash. Sem perfil de navegador, sem
seletor de lançamento, sem export. O que o MCP não cobre (configurar lançamento) fica em
`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §9.

Na rodada das 5h a rotina **pede ao Dash pra buscar dado novo antes de ler** (`atualizar_dados_lancamento`, a
única ação que ela usa fora das de leitura, porque não muda configuração) e espera até 10 min. Sem isso, os
inscritos do fim do dia podem faltar enquanto o gasto já está completo, e o CPL do dia sai inflado.

**Por que 5h, e não meia-noite** (decisão do Rodrigo, depois de pesquisa nas fontes oficiais). Nem a Meta nem
o Google indicam horário pra mexer em verba; na Meta, o que pesa no aprendizado é o tamanho e a frequência da
mudança, não a hora. O que existe de oficial é sobre a hora de LER o dado: a solução de scripts do Google Ads
manda agendar o relatório diário às 3h ou depois, porque a estatística atrasa; a conversão do Google leva horas
pra aparecer e entra no dia do clique; e o insight da Meta segue assentando depois que o dia fecha. À meia-noite
a rotina lia um ontem incompleto nas últimas horas. Às 5h o dado está mais fechado, e o lote ainda fica pronto
antes de o dia de trabalho começar. Fontes: a solução "Account Summary" da documentação de scripts do Google Ads
· developers.google.com/google-ads/api/docs/conversions/reporting ·
developers.facebook.com/docs/marketing-api/insights/best-practices/. *UNIVERSAL nos fatos de plataforma; o
horário é escolha da casa.*

Conferido uma vez, logo depois de uma atualização do Dash, na captação da Black: o `captacao_geral` do MCP e
os números que a tela do Dash usa bateram nos 10 campos (inscritos totais, pagos, orgânicos, sem UTM,
investido, CPA e inscritos e gasto por plataforma). *VARIAÇÃO ISOLADA (1 conferência).* A lista de inscritos
do MCP (`leads_lancamento`) separa pago de orgânico por `utm_medium`. O cartão da tela separa por `category`:
1 inscrito de uma campanha do Google pra alunos era `paid` sem `utm_medium`, com `gad_campaignid` na URL, e a
rotina passou a casá-lo por esse id.

## 3. O catálogo padrão

| Rotina (função) | Fases | Cadência | O que faz | Na casa |
|---|---|---|---|---|
| Tráfego | captação (e depois remarketing) | todo dia, 5h (começou às 8h e passou pela meia-noite; o Rodrigo fixou em 5h: o dia que decide já fechou e o dado assentou, ver "Por que 5h" no §2.4) | relatório + lote de verba proposto, por segmento, unidade e criativo | **captação pronta** (rodou numa Black). Remarketing: a construir, herdando a régua da rotina de orçamento do remarketing do lançamento anterior (custo por visita na página de destino, por momento) |
| Tráfego do perpétuo | perpetuo (sem fim) | todo dia, na mesma rotina | por peça (campanha CBO): venda real do Dash pela UTM e a régua do low ticket do caso de origem. Ciclo de 72 h a partir da 1ª impressão, agindo só no fim do ciclo; gasto abaixo de 2× o custo máximo por venda observa mais um ciclo; 2 vendas ou mais, em dias diferentes, e ROI ≥ 1,8 sobe 30%; 1 venda, ou ROI entre 1,0 e 1,8, segura; 2 vendas ou mais com ROI abaixo de 1,0 desce 40%. Pausar = decisão do dono (`sirius-scale/frameworks/lancamentos/low-ticket.md` §1, §7, §8 e §11) | **pronta**, num funil de low ticket e, depois, no perpétuo de outro expert da casa |
| Públicos de exclusão | captação, carrinho | a cada 4h | joga inscritos e compradores nas listas de exclusão | a construir. No lançamento anterior era um script que lia o CSV do Dash pelo navegador; o MCP já entrega os inscritos sem navegador. A única escrita permitida é adicionar pessoas àquela lista (`add_users`) |
| Panorama | captação | todo dia, 9h | panorama acumulado no grupo do cliente | a construir. No lançamento anterior era um script amarrado ao lançamento no código (pasta, metas, datas) |
| Recuperação de inscrição | captação | de 3 em 3 h, 8h15 a 20h15 | quem o Dash viu digitar a inscrição e o formulário não recebeu ganha a etiqueta de incompleta no Full Funnels; o e-mail sai por fluxo nativo do Full Funnels, disparado pela etiqueta | declarada no calendário, ainda sem tarefa agendada: é rotina que escreve em contato, então espera o ok do Rodrigo. Pedido dele: "será que temos também que criar um fluxo pra enviar pra quem preenche e não envia?" |

**O que a rotina de públicos herda da versão antiga** (regras duras de uma rotina que escreve):
- a única escrita é adicionar pessoas àquele público: não cria público, não toca em campanha, conjunto,
  anúncio, verba nem status, e não aplica a exclusão em conjunto nenhum;
- incremental por estado guardado na máquina, só com o e-mail em hash (SHA-256), nunca em texto puro: manda só
  o que ainda não foi enviado;
- trava de volume: acima de 10.000 e-mails novos numa rodada, ou de 3.000 numa rodada agendada com o estado já
  populado, ela **para**. Salto desse tamanho é sinal de lista de outro lançamento ou estado perdido, não de
  captação;
- dado velho não passa: confere o lançamento da lista e a data do lead mais novo, e recusa lista cujo lead
  mais recente tenha mais de 1 dia. Leitura falhou = rodada falha, sem cair pro arquivo velho.

**O que a rotina de panorama herda da versão antiga:**
- é **panorama acumulado** desde o início da captação, não recorte de um dia (decisão do Rodrigo): número
  diário oscila com problema pontual de veiculação, e a equipe lê ruído como tendência;
- custo por MQL não entra no agregado do dia, de propósito: verba se decide por custo por MQL por campanha e
  criativo, e o número agregado convidaria a equipe a decidir por ele;
- o resumo em texto sai por regra, não é escrito na hora: cada frase vem de uma comparação explícita (média
  realizada × ritmo necessário, CPL × alvo), pra nunca afirmar o que o número não sustenta;
- os denominadores são os da tela do Dash (CPA e taxa de pesquisa sobre os leads pagos, faixa A/B sobre quem
  tem faixa; `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.1). Usar a base toda erra os três
  números, sempre pro lado bonito;
- se o dado não cobrir o dia fechado por inteiro, recusa enviar;
- nada sai sem o envio pedido de forma explícita. O envio pelo WhatsApp e as armadilhas dele estão em
  `sirius-scale/frameworks/automacao/whatsapp-baileys.md`.

Conferências pontuais (aprovação de anúncio novo, gasto no primeiro dia) **não viram rotina avulsa**:
entram como passo da rotina de tráfego quando há objeto criado há menos de 48h (a construir na casa).

Rotinas transversais, que não são de lançamento (leitura de reunião, painel diário, fechamento financeiro do
mês, distribuição de conteúdo, radar de conteúdo do nicho), ficam como estão. A de distribuição de conteúdo
já era movida a registro e foi o exemplo que inspirou este desenho.

## 4. Ligar e desligar um lançamento

**Planejar antes de executar (regra da casa, decisão do Rodrigo).** Nas palavras dele: "a gente pode sempre
fazer o planejamento antes de executar as campanhas, porque eu acho que isso aí podia ser uma regra". Antes de
qualquer campanha subir, o lançamento (ou funil) tem a planilha de planejamento com a verba em faixa (piso, alvo,
teto) e o resultado de cada cenário: leads, vendas, faturamento e retorno. Do lado de vocês, a planilha fica na
pasta do lançamento, e a faixa dela, por dia, entra em `verba_dia` no `rotinas.json`. Na casa, a planilha fica
ligada ao arquivo: a rotina lê os cenários a cada rodada e mostra onde o ritmo de hoje cai entre eles. Sem
planejamento, o agente de tráfego monta um antes de montar a campanha. VARIAÇÃO ISOLADA (primeiro caso: uma
Black do cliente de origem).

**A venda simulada sai dos inscritos, nunca da base inteira (decisão do Rodrigo).** Nas palavras dele: "a
conversão deve ser simulada de acordo com o número de LEADS CAPTADOS, e não simplesmente do público todo da
base". Cada linha de venda do planejamento é inscrito × conversão: lead novo da captação, lead da base que se
inscreveu de novo (re-cadastro) e aluno inscrito. A base de quem não se inscreveu não entra. O que o plano não
projeta entra medido: na casa, a rotina conta no Dash e escreve na planilha antes de ler. O dado que sustenta:
num lançamento do cliente de origem, 8 das 11 vendas da base vieram de quem se inscreveu de novo (0,94% deles),
e a base inteira de outro lançamento converteu 0,15%. Na Black, a troca derrubou o cenário provável pra uns 30%
do que era. VARIAÇÃO ISOLADA.

**E pelos leads de agora, com o ritmo até o fim da captação (Rodrigo).** Nas palavras dele: "leads é leads, não
precisa pensar em recadastro" e "você pode fazer uma projeção futura do ritmo que a gente está na captação até o
final da captação". A simulação parou de vender pelo lead que o plano projetava (verba ÷ CPL) e passou a vender
pelo que está no Dash agora + a média dos últimos 7 dias fechados × os dias até o fim da captação. Aluno e
não-aluno ficam separados só porque convertem diferente. Na casa, a rotina das 5h escreve isso no bloco do
resultado, e as colunas viraram faixas de conversão, não de lead. No caso de origem:

- provável = o benchmark que ele trouxe da Black de outro expert do mercado, alunos 30% e não-alunos 6%;
- otimista = os 10% de não-aluno que ele lembrou primeiro;
- pessimista = o do plano (1% e 10%).

VARIAÇÃO ISOLADA: a conversão de Black na casa continua sem medida própria.

**Planejamento pedido por quem cuida do tráfego sem ser gestor.** Pedido do Rodrigo: "Ele pode preencher quanto
vai investir, o mínimo e o máximo, e mais alguma coisa [...] quanto menos cliques, melhor." Na casa isso é um
formulário no quadro do lançamento; do lado de vocês, é um pedido ao agente `gestor-trafego`. O caminho é o mesmo:

1. quem cuida do tráfego diz o mínimo e o máximo do lançamento inteiro, a meta de faturamento (opcional), se a
   lista de alunos existe e o que o agente precisa saber. Datas e conta já estão no `rotinas.json`;
2. o agente propõe a estrutura pelo framework da fase: a verba de cada fase, por dia, as campanhas, os conjuntos
   com o público e os criativos;
3. quem pediu valida a estrutura, e a faixa (`verba_dia`) e os segmentos entram no `rotinas.json`;
4. o agente monta pausado, e a pessoa dona da conta liga depois de ler o resumo tirado da conta
   (`sirius-scale/REGRAS.md` §6).

VARIAÇÃO ISOLADA (primeiro caso: a Black de outro expert da casa; nenhuma estrutura validada ainda).

**Ligar (nenhuma rotina nova é criada):**
0. O planejamento existe, e a faixa dele, por dia, está em `verba_dia` (acima).
1. Criar o `rotinas.json` na pasta do lançamento, copiando o do último lançamento como molde (no primeiro,
   partindo de `sirius-scale/modelos/rotinas.json`).
2. Fases com data. Fase sem data fechada fica fora de `fases` até fechar, nunca com data chutada.
3. `filtro_no_nome` de cada segmento, com o trecho que aparece no nome dos conjuntos (Meta) e das campanhas
   (Google) daquele público (no modelo, `[PF]` e `[PQ]`). É por ele que a rotina acha cada unidade.
4. `linha_escala` e `linha_corte` de cada segmento, e `custo_por_mql_ref` onde houver, copiados do plano de
   tráfego, com a fonte em `_historico`. Ninguém decidiu, fica `null`: a rotina mostra o número e não sugere
   subir nem cortar. Toda regra de verba, rampa ou corte sai daqui, nunca de um número só pra tudo (foi o erro
   da rampa da Black, §1). Na casa a linha também é por plataforma; o modelo de vocês tem uma por segmento.
5. A pesquisa e a regra de MQL ficam no Dash, não neste arquivo: conferir lá (copiar do lançamento anterior, se
   a pesquisa repete).
6. Conferir o arquivo (§2.2) → OK.
7. Rodar a rotina uma vez à mão e ler o relatório.
8. Na primeira rodada agendada (ou num "Run now"), conferir o histórico de rodadas da tarefa: rodada com
   menos de 1 min e sem resumo parou pedindo permissão. Liberar só os comandos de leitura (a lista de vocês
   está em `sirius-scale/rotinas/trafego-diario.md`). **Nunca "sempre permitir" comando que escreve em
   plataforma**: isso anularia a trava "rotina não se autoriza".

**Desligar:** a data da fase passa e a rotina ignora o lançamento. Não se apaga rotina.

## 5. A régua da captação (o que a rotina aplica)

| Regra | Fonte | Confiança |
|---|---|---|
| CPL real = gasto da plataforma (na Meta, o gasto lido pela API vem sem o imposto, que se soma por fora) ÷ inscrito do Dash; janela de 3 dias cheios; hoje parcial fica fora | `sirius-scale/frameworks/trafego/_metodologia.md` §3.1; plano de tráfego da Black do caso de origem; `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.1 | CONSISTENTE |
| Linha absoluta por segmento e plataforma: abaixo da escala sobe, entre escala e corte mantém, acima do corte baixa | plano de tráfego da Black | VARIAÇÃO ISOLADA |
| O aluno paga mais: a linha dele é k × a do não aluno **médio** (no caso de origem, k = 4). Contra as linhas por plataforma, sai ~7,5x a da Meta e ~3x a do Google. Só pelo CPL, sem MQL | plano de tráfego (decisão do Rodrigo) | VARIAÇÃO ISOLADA; a conversão de aluno numa Black desse cliente nunca foi medida. Nas Blacks de outros experts da casa o plano mediu 1,9% (comprador recente, 8 de 414), contra os 10–30% que o plano supõe |
| No não aluno, custo por MQL contra a referência do lançamento anterior vence o CPL quando tem volume (≥ 25 respondentes) | plano de tráfego; `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §6 | VARIAÇÃO ISOLADA |
| Corte só com volume (30 inscritos na unidade); nunca cortar uma frente pelo CPL de um dia | plano de tráfego; o relatório diário de tráfego da casa | VARIAÇÃO ISOLADA (o número não transfere) |
| Subida com N baixo só quando CPL × (1 + 2/√N) fica abaixo da linha de escala, com N ≥ 5 | nasceu num dia em que o aluno da Black estava 17x abaixo da linha com 12 inscritos e a régua anterior mandava "observar" | VARIAÇÃO ISOLADA (1 dia, 1 lançamento) |
| Degrau de 20–30% | `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §2.1 (aprendizado do Advantage+/Demand Gen) | mecânica de plataforma, transfere |
| **Uma mexida de verba por objeto por dia** (calendário de Brasília), contada da **última edição real**: a mexida do executor ou, sem ela, a última edição significativa lida da plataforma (Meta: `learning_stage_info.last_sig_edit_ts` pela API; pelo conector, que não traz esse campo, o `updated_time` do conjunto. Google: `change_event`). Mexeu ontem, a rodada do dia já propõe; mexeu hoje, trava até amanhã. Serve pra não somar duas subidas de 30% no mesmo dia (rodar a rotina de novo depois de aplicar) | o Rodrigo derrubou as 48h ("nada a ver isso, vamos mudar"). As 48h vinham de uma leitura errada do briefing da Black ("começar com uma verba menor e ir aumentando conforme os dias", lido como "a cada 2–3 dias"); com a rodada à meia-noite e a aplicação de madrugada, uma mexida às 2h30 travou o lote seguinte por duas horas e o executor recusou o ok dele | regra de código |
| ~~48h entre mexidas~~ e ~~subida que libera de madrugada com "aplicar a partir de"~~ | saíram juntas (linha acima) | histórico |
| **A faixa que manda é a da FASE** (piso e teto da captação: na casa, no registro da fase; do lado de vocês, em `verba_dia`): é o mínimo e o máximo de investimento. Dentro dela, a régua sobe sem teto por unidade: subida boa vai pro lote (degrau de 30%, uma mexida por dia, abaixo do teto de segurança; na casa, um teto fixo no código; do lado de vocês, o teto de verba combinado antes, `sirius-scale/REGRAS.md` §6). A faixa por unidade do plano vira referência, e só o piso dela continua valendo. Vira decisão do dono da verba só o que estoura o teto da fase, e com a solução pronta: as subidas entram por ordem de folga contra a linha até caber no teto, e a que sobra chega com o teto da fase que faria caber tudo, ou a opção de deixar a subida pro dia seguinte. Projeção abaixo do piso da fase sai com quanto falta por dia e onde pôr; acima do teto no ritmo de hoje, com quanto tirar por dia e de onde (na casa, a régua faz as duas contas; do lado de vocês, peça as duas ao Claude no relatório). Unidade parada não entra na projeção, e o corte do mesmo lote não abre espaço pra subida, porque o lote pode ser aplicado em parte (achado numa revisão de olhos frescos). Depois de troca ou rotação, a janela que fala de criativo que saiu (menos da metade do gasto vindo de quem continua ligado) não decide verba: a unidade segura até os novos rodarem (na casa, a régua mede essa fatia da janela; do lado de vocês, peça a conta ao Claude antes de mexer na verba. Caso: uma subida de 30% do aluno da Black, no dia seguinte a uma rotação, saía do CPL de três criativos que a rotação da noite anterior tinha pausado) | Rodrigo, na análise do tráfego da Black: "Você não pode ficar batendo na régua e não dando soluções, porque o ideal é a gente sempre ter um mínimo e um máximo de investimento para trabalhar. Se o negócio está bom, o cenário está bom, a gente vai aumentando, sem muita trava, sabe? Deixar um range maior." Caso: as faixas por unidade do plano de tráfego estavam 2 a 3x abaixo do orçamento real no ar, e a rotina devolvia "decisão sua" toda noite sem propor nada. Regra da casa: investimento se apresenta em faixa | decisão do Rodrigo (regra); substitui a linha de baixo |
| ~~A faixa do plano por unidade (piso/alvo/teto) segura a proposta; régua mandando subir com a unidade no teto vira **decisão do dono da verba**, não item do lote~~ | valeu por duas semanas, da primeira rotina no desenho novo até a decisão da linha de cima (registro da fase, verba por conjunto por dia) | histórico |
| O ajuste ao piso/teto nunca inverte o veredito (unidade abaixo do piso não sobe num "baixar") | defeito pego no teste (uma campanha do Google abaixo do piso, que o ajuste fazia subir num "baixar") | regra de código |
| Criativo: escada relativa dentro da unidade (≤ 1,15x sobe, 1,15–1,5x mantém, ≥ 2,5x corte forte), referência = melhor com volume (15 inscritos); qualidade só com teste z | o relatório diário de tráfego da casa; `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §3.7 | escada VARIAÇÃO ISOLADA; teste z CONSISTENTE |
| Troca de criativo com N baixo (abaixo de 15): sugere trocar quando CPL ÷ (1 + 2/√N) ainda fica acima da linha de corte do segmento (N ≥ 5), ou quando gastou 3x a linha de corte sem inscrito. Sai numa seção própria do relatório, com a reserva pausada da unidade; nunca entra no lote. **Exceção: criativo com qualidade ">" contra a referência (teste z) não entra na troca**, sai como "Fica, apesar do CPL" e decide por custo por MQL. Caso: um vídeo no conjunto de envolvimento da Meta, com 3x o CPL do melhor e 7 MQL em 14 respondentes contra 0 em 9; a seção de troca mandava pausar e o resumo repetiu | pedido do Rodrigo sobre a otimização de criativos ("essa rotina também precisa olhar pra isso") | VARIAÇÃO ISOLADA |
| Público fechado (ex.: alunos): medir quanto da base já se inscreveu e as **impressões por pessoa do público por dia** contra o plano. Acima do teto vira **atenção**, não trava. A unidade é impressões ÷ público ÷ dias cheios, não a frequência do gerenciador (impressões ÷ alcance). A 1ª versão comparou a frequência do gerenciador e acusou "acima do teto" num público que estava abaixo do piso; corrigido no pente fino | Black: na Meta, uns 0,2 impressão por pessoa do público de alunos por dia, contra frequência do gerenciador de 1,65; no Google, uns 0,45, contra 2,14. Plano: 0,5 · 0,8 · 1,2 (piso, alvo, teto). Na mesma madrugada, uns 7% da base de alunos já tinham se inscrito, de qualquer origem | VARIAÇÃO ISOLADA |
| Ritmo da fase contra a faixa (piso/alvo/teto ÷ dias) e quanto precisa por dia daqui pra frente | regra da casa: investimento em faixa, nunca número travado | CONSISTENTE |
| **Rotação de criativo em público saturado.** Sinal: frequência do gerenciador (impressões ÷ alcance da fase) ≥ 4 **e** CPL da janela ≥ 1,5x o acumulado da unidade. A rotina propõe troca 1 por 1 na mesma unidade: sai quem mais gastou na janela (o mais visto agora; quem acabou de voltar do descanso e ainda não gastou não sai de novo), e só quem levou pelo menos 10% do gasto acumulado da unidade (quem quase não recebeu verba não saturou ninguém: um estático do aluno da Black, com 2% do gasto do conjunto desde o início da captação e o melhor CPL, saía como "o mais visto" na 1ª versão) e entra, nesta ordem, o que nunca rodou ali (do mesmo tipo, depois de outro tipo) e o que descansou (pausado e sem gasto na janela), com o melhor CPL primeiro. Criativo que não serve praquele público fica numa lista de fora da rotação (do lado de vocês, em `frameworks-da-casa/`; na Black, um vídeo no público de aluno: o gancho, que pergunta se a pessoa já comprou um curso [da matéria] e não resolveu, lê mal pra quem já é aluno). Antes de propor, espera ler a troca anterior: com menos da metade do gasto dos dias de leitura vindo de criativo que continua ligado, ou com anúncio ativo que começou a gastar dentro deles, não propõe outra. **Os dias de leitura encolhem com o fim da captação:** no máximo 3 e no máximo um terço dos dias que faltam, nunca menos de 1 (21 dias → 3; 6 → 2; 3 → 1). Rodrigo, no dia seguinte: "Ela sempre tem que levar em consideração também quantos dias ainda temos de captação". Com o sinal ligado, a subida de verba da unidade também espera (criativo antes de verba, `sirius-scale/frameworks/trafego/otimizacao-em-tres-niveis.md` §1 e `sirius-scale/frameworks/lancamentos/perpetuo.md` §3.9). Unidade parada não entra. No Google, reserva em revisão fica listada e entra quando for aprovada; reprovada não entra. Sai como decisão do dono da verba, nunca no lote (na casa, um botão de decisão; do lado de vocês, quem pausa e ativa é a pessoa dona da conta, no gerenciador, `sirius-scale/REGRAS.md` §6) | Rodrigo, na mesma análise do tráfego da Black: "a gente vai ter que fazer rotação de criativos para mudar o estímulo, que já alcançou todo mundo com essa frequência alta, só criativos que vai poder ajudar a gente. Então, vamos rodar o que a gente não rodou ainda, fazer a alternância aí de criativos." Caso: aluno da Black. Na Meta, o alcance chegou a 70%–80% do público de aluno, com frequência 8,4 e CPL da janela 2,2x o acumulado; no Google, a uns 66% da base, com frequência 18,3 e 3,8x. A rotação foi aplicada na mesma noite | VARIAÇÃO ISOLADA (decisão do Rodrigo, 1 caso); os limiares 4 e 1,5x são PADRÃO INCONCLUSIVO, e o resultado da 1ª rotação ainda não foi medido |

### 5.1 A régua do carrinho — o desenho (VARIAÇÃO ISOLADA, 1 carrinho, 11/2026)

O carrinho de um lançamento se lê como perpétuo: unidade = conjunto na Meta, campanha no Google, achada na conta pelo
nome (lista fixa deixa a célula nova de fora). Leitura completa de manhã, com o dia anterior fechado, e um alarme no fim
da tarde (gasto de hoje contra o faturamento de hoje, anúncio reprovado, unidade ligada sem entrega) que não mexe em nada.
- **Quem decide é a venda casada no Dash** (a UTM da própria venda, último clique).
- **Sinal antecipado (AddToCart, início de checkout) só decide com dois portões passados há 48 h:** a página disparar o
  evento e o anúncio ter o pixel no rastreio (`trafego/meta-criacao-tecnica.md`). Sem os dois, o zero é falso e a régua
  cortaria por ele. O início de checkout no domínio da Hotmart é de todo checkout que dispara o pixel, não só deste.
- **Célula que gastou menos de 70% da verba do ciclo é "não testada"**; anúncio sem verba ao lado de outros nunca é
  perdedor ("ligar não é testar").
- **Gasto do dia contra o faturamento do dia** (toda venda da oferta, de qualquer origem): com o gasto de ontem acima do
  limite (20% no caso), nenhuma subida; dois dias seguidos, aviso pra decisão.
- **Exclusão de compradores todo dia**, e a fila de criativos conferida: peça com data passada e fora do ar é "atrasada".

O que transfere é o desenho. É do caso: as linhas de custo por venda, o tamanho do ciclo e o limite de gasto, tirados do preço
e do plano daquele lançamento.
## 6. Do lançamento anterior pro padrão: onde cada função foi parar

| Rotina do lançamento anterior | No padrão |
|---|---|
| otimização de tráfego (duas versões), relatório de tráfego | rotina de tráfego (captação) |
| orçamento do remarketing | rotina de tráfego (remarketing, a construir) |
| exclusão de público | rotina de públicos de exclusão (a construir) |
| relatório no WhatsApp, mensagem de bom dia | rotina de panorama (a construir) |
| pesquisa diária | sai como rotina: a qualificação já entra no relatório de tráfego, casada por e-mail |
| lives de aquecimento | módulo de aquecimento da rotina de tráfego, quando houver fase de lives no `rotinas.json` |
| conferência financeira do cliente | transversal por cliente (já era: só tinha o lançamento no nome) |
| conferência do remarketing do downsell | passo da rotina de tráfego (objeto criado há menos de 48h) |

## 7. O que transfere e o que é do caso

**Transfere:** rotina por função; calendário no lançamento; leitura que só lê e propõe; executor único
com plano versionado em arquivo; Dash pelo MCP; uma mexida de verba por objeto por dia, contada da última
edição real (as 48h entre mexidas saíram, §5); a faixa da FASE como mínimo e máximo, com a unidade subindo sem
teto próprio e a solução pronta quando passa do teto da fase (antes era a faixa por unidade como trava e "decisão
do dono", §5); medir cobertura quando o público é fechado; rotação de criativo quando o público satura (o
desenho; os limiares são do caso).

**É do caso (o cliente de origem, a Black):** os números das linhas (custo por inscrito de escala e corte, por
plataforma e por segmento), o k = 4, o mínimo de 30 inscritos, a regra de MQL (2 perguntas da pesquisa daquele
cliente), a frequência por dia do plano de aluno e os limiares da rotação (frequência 4, CPL da janela 1,5x o
acumulado), tirados de um público fechado de pouco mais de mil alunos. Lançamento novo traz os dele no
`rotinas.json`, com a fonte.

## 8. Montar do lado de vocês (se quiserem) — desenho, não testado fora da casa

A rotina de tráfego já vem pronta pra virar tarefa agendada: `sirius-scale/rotinas/trafego-diario.md`, com a
instrução inteira. Pra qualquer outra função, é o mesmo desenho, sem os scripts da casa:

1. **Comece sem rotina.** O agente `gestor-trafego` lê o Dash pelo conector e propõe o lote numa conversa.
   Rotina só vale a pena quando essa leitura diária ficar repetitiva.
2. **Uma tarefa agendada por função**, criada uma vez no Claude Code e com o nome da função
   (`trafego-diario`), nunca com o nome do lançamento (§2.1).
3. **A instrução da tarefa carrega método:** ler os `rotinas.json` de `lancamentos/`, achar quem
   está em fase hoje, pedir ao Dash a atualização e esperar (§2.4), ler pelo conector, aplicar a régua do
   arquivo (§5), escrever relatório e lote proposto em `entregas/` e parar. Nunca o diagnóstico de ontem
   (§1), nunca escrita em plataforma.
4. **Permissões:** liberar só a leitura. A aplicação continua com o dono da conta, no gerenciador
   (`sirius-scale/REGRAS.md` §6).
5. **Conferir a primeira rodada** (§4, passo 8): rodada curta e sem resumo parou pedindo permissão.
6. **A máquina tem que estar acordada e com o app aberto** no horário da rotina (§1).
