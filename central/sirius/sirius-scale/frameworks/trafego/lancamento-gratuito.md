# Framework de Tráfego — Lançamento Gratuito

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método
> **Base:** 1 cliente (o caso-base, um expert de educação) · principalmente o 1º
> lançamento analisado, com medições do 2º
> **Alcance:** NÃO TESTADO FORA. E tem um limite a mais que os outros: este
> arquivo é do **modelo** lançamento gratuito. Cliente de perpétuo, VSL, low
> ticket ou negócio local **não usa este framework** — a arquitetura de 6 fases
> não existe lá. Ver §7 antes de aplicar.

> Ponto de partida validado, não lei. Atualizar conforme os testes mostrarem coisa nova.
> Base: operação da casa + dados do 1º lançamento analisado.
>
> **Como o caso aparece aqui:** tudo vem de uma conta só, a do caso-base. "O 1º
> lançamento" é o lançamento gratuito de referência; "o 2º lançamento" é o
> seguinte, na mesma conta, onde foi medido quase tudo do §2.4 e do §3; "o
> lançamento anterior" é o que veio antes dos dois e só aparece nas comparações
> de remarketing do §3.7. As datas viraram relativas à fase do lançamento.

## Como usar este documento

Este é o padrão pra **iniciar** um lançamento gratuito. Cada seção diz o que já é
validado e o que ainda é hipótese. Quando um teste de vocês contrariar algo daqui,
registre em `frameworks-da-casa/` (que vale mais que este arquivo,
`sirius-scale/REGRAS.md` §4) — dizendo se o item passa de "validado" pra "em teste"
ou o contrário.

⚠️ Não confundir com os outros frameworks de tráfego: lançamento pago (venda de
ingresso), perpétuo e distribuição de conteúdo têm lógicas próprias. Lançamento
gratuito é o único que roda remarketing pesado em múltiplas fases.

---

## 1. As 6 fases

| # | Fase | Quando roda | O que faz |
|---|---|---|---|
| 1 | **Captação de leads** | Início até o fim da captação | Traz lead novo pro lançamento |
| 2 | **Aquecimento** | Durante toda a captação (em paralelo) | Esquenta quem já se inscreveu |
| 3 | **Antecipação** | Última semana da captação | Contagem regressiva pro evento |
| 4 | **CPLs / Aulas** | Durante os 7 dias do evento | Leva pra cada aula e pras gravações |
| 5 | **Carta de vendas** | Sábado antes do carrinho abrir | Prepara a venda |
| 6 | **Carrinho aberto** | 3–4 dias de carrinho | Converte |

Downsell roda depois do carrinho e da reabertura, na semana da live de downsell (ver seção 3.6).

---

## 2. Captação (público frio + quente)

Objetivo: `OUTCOME_LEADS`. Otimização por conversão de pixel — **sempre conferir o
`promoted_object.custom_event_type`**, porque o nome do goal sozinho não diz o que
está sendo otimizado (ver `sirius-scale/frameworks/trafego/_metodologia.md` §1).

**Regra que vale pra todas as campanhas de captação:** excluir os leads já cadastrados.

### 2.1 Escada de escala (a espinha da captação)

Esta é a abordagem principal, validada no 1º lançamento analisado:

1. **Teste — 1-1-1**
   Uma campanha por criativo. 1 campanha → 1 conjunto → 1 anúncio.
   Advantage+ ligado, sem público selecionado. Segmentação só de país e,
   eventualmente, idade.

2. **Pré-escala — 1-3-1**
   Critério de validação no teste (confirmado pelo Rodrigo):
   **custo por MQL ou lead score faixa A+B na média geral** (ver
   `sirius-scale/frameworks/trafego/_metodologia.md` §3.1 — é a mesma régua que
   decide verba no dia a dia, não CPL isolado). Validou → 1 campanha → 3
   conjuntos iguais (mesma config do teste) → 1 anúncio cada.
   Campanha quase toda Advantage+ — exceto os Advantage+ de anúncio, que ainda não
   parecem funcionar tão bem.

3. **Escala**
   Validou nos 3 conjuntos da pré-escala (mesmo critério: custo por MQL ou
   faixa A+B na média): multiplicar a campanha de pré-escala **3x, 5x ou
   10x**, o grau depende do quanto o lançamento precisa escalar naquele
   momento — não é sempre o mesmo múltiplo.

> 📌 Escalar por **duplicação de campanha**, não subindo orçamento no mesmo conjunto.
> Confirmado nos dados do 1º lançamento (conjuntos vencedores clonados em campanhas
> `[ESCALA] ...-1/-2/-3`). **Nível de confiança: VARIAÇÃO ISOLADA** — um
> lançamento, um cliente. Não estava marcado antes; corrigido depois.
>
> **CORREÇÃO DO RODRIGO:** discorda da regra acima como norma fixa —
> e aponta que o próprio 1º lançamento (a fonte citada) também escalou campanha
> de teste subindo orçamento direto no conjunto, e funcionou. Ou seja, a
> regra original, que se dizia confirmada nos dados do 1º lançamento, capturou só
> metade do que aconteceu lá — duplicação E aumento direto convivendo, não
> duplicação como único caminho válido. Decisão: aumentar orçamento direto no
> conjunto que já está indo bem (custo por MQL medido no Dash) é válido, a
> duplicação vira uma opção a mais, não obrigação. Ressalva técnica que segue de
> pé: alta muito grande de uma vez (Meta cita >20-30%) pode reiniciar a fase de
> aprendizado do Advantage+/Demand Gen — mecânica documentada da própria
> plataforma. Na prática: subir em degraus (~20-30% por vez) evita resetar.

**Por que um criativo por campanha em todos os degraus — *VARIAÇÃO ISOLADA* (11/2026):** quando a campanha leva
vários criativos, a Meta escolhe a peça pelo lead mais barato, e no caso medido essa foi a de pior MQL
(`publicos-e-advantage.md` §4.10, item 1). Na escada, quem escolhe é o custo por MQL no Dash.

**O teste que ganha sobe a verba junto com a pré-escala — *VARIAÇÃO ISOLADA* (decisão do Rodrigo, 11/2026).** A
pré-escala não substitui a verba do próprio teste: o teste pode acabar sendo o que mais escala. Fala dele: "não pode
simplesmente ignorar e manter ela ligada. Tem que aumentar a verba." O objetivo da captação é "captar o máximo de lead
possível com MQL".
- Como foi escrito na primeira aplicação: o teste com custo por MQL abaixo da média da escada sobe até 30% por noite, e
  com 50 leads vai também pra pré-escala.
- **Regra:** na otimização da escada, a linha de verba do teste vencedor é obrigatória. A correção logo acima já dizia
  que subir direto no conjunto vale.

**Na escada, o orçamento é da campanha (CBO), nunca do conjunto — *decisão do Rodrigo, 11/2026*.** Fala dele: "esses
testes, essa escada, é tudo CBO" e "o orçamento não é no conjunto".
- Vale pro teste (1-1-1), pra pré-escala (1-3-1, com o orçamento dos três conjuntos somado na campanha) e pra escala. A
  estratégia de lance vai junto, na campanha (`meta-criacao-tecnica.md`, "`bid_strategy` mora no mesmo nível do
  ORÇAMENTO").
- **O quente em hierarquia é a exceção:** fica com orçamento por conjunto, porque cada degrau precisa da verba garantida
  (§2.2).

### 2.1.1 Rampa de verba na captação — *VARIAÇÃO ISOLADA* (decisão do Rodrigo, 11/2026)

A verba da captação não começa no diário cheio. Ela começa abaixo e sobe em degraus, conforme a otimização, com a
projeção calculada pra fechar o total planejado. Fala do Rodrigo: "quando a gente começa com o investimento diário no
talo, no máximo, me parece que o lead fica mais caro. Quando eu vou aumentando aos poucos, conforme a otimização, eu vou
aumentando, mas calculando que a projeção final, para que eu bata o que eu quero investir, parece que assim o lead sobe
mais controlado." Ele decidiu que vale daqui em diante em todo lançamento clássico.

**Como montar:**
- 3 dias de aprendizado no primeiro degrau, depois um degrau de ~20% a cada 2 dias. Os 2 dias são a **projeção** pra
  fechar o total, não espera mínima: a régua verde pode trazer o degrau antes. É o mesmo limite de 20% a 30% da nota
  acima, que evita reiniciar o aprendizado. O último degrau segura até o fim da captação.
- **O degrau só sobe se a régua deixar:** custo por MQL verde sobe, amarelo segura, vermelho volta um degrau. O que entra a
  mais vai pro que passou na régua (pré-escala, a melhor semente, a melhor versão do quente).
- **Degrau de até ~30%, à noite.** Fala dele: "um pouco mais de 30%, talvez não tenha problema, se for feito isso de
  noite, de madrugada". O que se evita é dobrar de uma vez.
- **Calcular duas rampas, alvo e teto.** A de alvo com degraus de 20%; a de teto com degraus de 30%, usada só se a régua
  estiver verde no dia 4.

- **Captação que já ligou acima do primeiro degrau não volta pra ele** (decisão do Rodrigo, *VARIAÇÃO ISOLADA*). Quando
  entram mais testes na escada e a captação liga acima do degrau 1, ela segue dali, e a
  régua reajusta nas otimizações seguintes.

**Confiança:** VARIAÇÃO ISOLADA. O efeito no custo do lead ainda não foi medido. Pra medir: custo por MQL de cada dia
contra a verba do dia, comparando uma captação em rampa com uma que começou no diário cheio.
### ⚠️ As 3 etapas COEXISTEM — não se substituem

A escada diz onde colocar **dinheiro novo**, não o que desligar. Teste e pré-escala
continuam rodando enquanto estiverem indo bem. Não desligamos o teste porque ele
"graduou" pra pré-escala, nem a pré-escala porque virou escala.

**Por que isso importa (1º lançamento):** as campanhas de **teste 1-1-1** foram as
que mais trouxeram **vendas na abertura do carrinho**. Ou seja: o lead vindo dos
testes converteu melhor lá na frente.

📌 **Consequência prática:** não avaliar campanha de captação só por CPL. A campanha
com CPL mais alto pode estar trazendo o lead que compra. Julgar por CPL isolado pode
matar justamente a campanha que sustenta o faturamento.

*Nota:* essa qualidade de lead não aparece na análise da Meta sozinha — é o
cruzamento com MQL/lead score (Dash) que revela. Ver
`sirius-scale/frameworks/trafego/_metodologia.md` §3.

### 2.2 Campanha de mix quente

Roda em paralelo à escada acima.

- Todos os públicos quentes, o mais amplo possível, num só.
- Vários criativos dentro da mesma campanha.
- Otimização diária (ajuste manual frequente).
- Rodar **duas versões**: uma com Advantage+ ligado, outra desligado.
- Dentro da mesma campanha, adicionar um conjunto com: quem caiu na página de
  inscrição **ou** viu os vídeos dos anúncios.

**Quais públicos quentes entram (o kit do Rodrigo, 11/2026):** engajamento e seguidores, no Instagram e na página do
Facebook, mais quem viu os vídeos, as listas de leads antigas e quem visitou o site. Fala dele: "Geralmente eu uso só esses
dois, engajamento e seguidores. Tanto no Instagram quanto no Meta. Fora isso tem os video view, lista de leads e page view."
- **No Instagram, um público basta:** o "todos que interagiram com a conta" (regra `ig_business_profile_all`) já contém
  visitou, mensagem, salvou, clicou e engajou. Seguidores entram como público à parte.
- **Conferir o tamanho de cada janela antes de escolher:** a de 540 dias já saiu menor que a de 365
  (`publicos-e-advantage.md` §4.10, item 5). Janela curta é público pequeno e satura.

**Quente em hierarquia, numa campanha só — *VARIAÇÃO ISOLADA* (decisão do Rodrigo, 11/2026; primeira aplicação, sem
resultado ainda).** Cada conjunto exclui os públicos dos anteriores:
- 00: página de inscrição e quem viu os vídeos dos anúncios;
- 01: o quente curto (engajamento de 30 a 90 dias, qualquer página do site, listas de leads e vídeo 95%);
- 02: o resto dos públicos quentes.
O porquê, na fala dele: "se for adicionar todos juntos. As chances de impactar os mais quentes acaba diminuindo, não é?"
00 e 01 vão com Advantage e sugestão desligados, porque, ligados, a lista vira sugestão e a hierarquia some. Ainda não
substitui o "num só" acima.

Como montar cada degrau (decisões do Rodrigo, 11/2026, *VARIAÇÃO ISOLADA*, primeira aplicação):
- **Cada degrau é um conjunto só, com vários criativos.** Fala dele: "cada um com varios (praticamente todos) criativos
  dentro, alguns ligados, e outros esperando para ligar durante a otimizacao, sempre mantendo no max 6 ligados".
  - Fica assim: 00, 01 e 02, três conjuntos. Em cada um, quase todos os criativos entram como anúncio, de 4 a 6 ligados
    e o resto pausado, esperando a vez.
  - Por que não um conjunto por criativo: com o mesmo público, os conjuntos disputam as mesmas pessoas, e com pouca
    verba cada um nenhum sai do aprendizado. Testar criativo é o trabalho da escada (§2.1); o quente colhe com o que já
    funciona.
  - O cuidado: num conjunto com vários criativos, a Meta põe a verba no lead mais barato, não no que traz MQL (no caso
    medido, quase toda a verba de um degrau foi pra um criativo só). Por isso só liga criativo com MQL bom, lido por criativo
    no Dash, e quem puxa verba com MQL baixo dá lugar a outro da fila.
- **O 02 também vai com Advantage e sugestão desligados.** Fala dele: "vai ter que criar o amplo como está, com o
  advantage desligado". Ligado, a lista vira sugestão (`publicos-e-advantage.md` §1) e o 02 vira um segundo aberto,
  misturando frio na leitura.
- **Rotação diária.** Fala dele: "a gente tenta manter de 4 a 6 ligados o tempo inteiro. Vamos sempre desligando um que
  não está dando muito bom e ligando o outro." Toda noite, lê o custo por MQL de cada criativo no Dash. Sai o pior que
  já teve volume (pelo menos 10% do gasto do conjunto nos dias em que esteve ligado, a régua de exposição do
  `otimizacao-em-tres-niveis.md` §3; se só um passa disso, ele fica e sai o que menos gastou). Entra o melhor da fila
  na escada. Criativo que quase não gastou não é ruim, é não testado. Trocar um por conjunto a cada rodada: ligar
  anúncio novo é edição que pode reiniciar o aprendizado.
- **Criativo novo entra no quente junto com a escada.** Fala dele: "sempre que surgir, a gente tem que colocar na
  escada, mas tem que colocar também nos públicos paralelos que estão rodando, nas campanhas quente". Entra como anúncio
  em cada conjunto e liga na próxima troca, enquanto o teste 1-1-1 dele roda em paralelo.
- **Verba entre os conjuntos do quente** entra na mesma leitura: até 30% por noite, do mais caro pro mais barato por
  MQL. No 00 e no 01, só com a frequência de 7 dias abaixo de 3, porque o público deles é pequeno. Se o quente roda nas
  duas versões (Advantage ligado e desligado), a ligada também entra na divisão.
- Ele acha que vale também pro frio ("inclusive até do frio talvez"): o semelhante num conjunto só, com a mesma
  rotação. *PADRÃO INCONCLUSIVO.*
### 2.3 Campanha de frio com semelhantes

- Público frio, só semelhantes (lookalike).
- Ver hipótese em aberto na seção 5 — ainda não há definição sobre Advantage+ aqui.

### 2.4 Teste de PÚBLICO no Google não usa 1-1-1

**VARIAÇÃO ISOLADA** — medido uma vez, num cliente, numa plataforma
(2º lançamento, Google Demand Gen, 1ª semana de captação). Ainda não é regra.

O 1-1-1 da seção 2.1 está validado pra testar **criativo**, na **Meta**.
Aplicar a mesma estrutura pra testar **público no Google Demand Gen** produz
o efeito oposto do pretendido.

**O caso real:** o 2º lançamento subiu 10 campanhas Demand Gen (8 de frio no
formato 1-1-1 + 2 de quente). No primeiro dia completo elas fizeram **22
conversões no total — 2,2 por campanha**. As 10 ficaram presas em
`BIDDING_STRATEGY_LEARNING` e usaram **10,9% do orçamento**.
A qualidade estava boa (CPA ~23% abaixo do alvo, fora um outlier): faltava
ENTREGA, não eficiência.

**Por quê:** o Demand Gen aprende por campanha. Cada campanha precisa de
volume próprio de conversão pra sair do aprendizado e competir. Fragmentar em
1-1-1 divide o sinal por N e nenhuma das N chega ao volume necessário.

**Estrutura a usar pra testar público:**

> **Uma campanha por público, com os criativos já validados dentro** (no
> 2º lançamento: os 3 criativos campeões do 1º).

- A variável isolada é o público — o criativo é constante *entre* as
  campanhas, que é o que importa na comparação.
- O sinal de conversão dos 3 criativos se soma numa campanha só.
- Mais criativo = mais inventário = mais chance de entregar, que é
  justamente o gargalo.

📌 **Um ou dois públicos por vez, não cinco.** Testar muitos simultaneamente
refragmenta o orçamento e recria o problema.

📌 **A leitura por criativo não se perde:** ela continua vindo das campanhas
de frio em 1-1-1, que rodam em paralelo. O teste de público não precisa
responder a mesma pergunta duas vezes.

⚠️ Isto NÃO invalida o 1-1-1 da seção 2.1. São perguntas diferentes: 1-1-1
pra ler criativo, 1 campanha por público pra ler público.

---

### 2.5 Conta com histórico: base garantida + teste em paralelo — *VARIAÇÃO ISOLADA* (Rodrigo, 11/2026)

Em conta que já roda (troca de agência, conta herdada), a primeira estrutura não
é a ideal da casa. Ela **replica a configuração que já vendeu** e põe o resto em paralelo. Fala do Rodrigo: "a gente
tem que replicar o que mais deu certo para ele, a mesma configuração de campanha que já deu certo no passado ... para
pelo menos garantir o mínimo. E aí, em paralelo, fazer o restante das recomendações."

**Como montar:**
1. **Achar o molde pela venda.** Cruzar a venda casada do Dash por conjunto (`tabela_utm_debriefing`, `utm_content`) com a
   configuração da Meta (`targeting`, Advantage, posicionamentos, evento, lance, orçamento). Ler o `targeting` na
   plataforma, porque o nome do conjunto engana.
2. **Replicar o molde inteiro**, trocando só os criativos pelos que venderam.
3. **O que é novo roda em paralelo** e com verba própria, como a escada da §2.1.
4. **Quente num conjunto só ou em hierarquia?** Decidir pelo tamanho do público (o tamanho real vem da API no público de
   engajamento; no lookalike a API devolve um marcador de 1.000) e pelo que a hierarquia já entregou na conta.
   Conjuntos por janela que não se excluem são sobreposição, não hierarquia.

---
## 3. Os 5 tipos de remarketing

**Regra geral:** remarketing **não** passa pela escada de escala (1-1-1 → 1-3-1 →
multiplicar). Sobe direto na estrutura final, porque o público é limitado.
Escada de escala é exclusiva da captação.

Todos têm o mesmo público principal: **inscritos no lançamento**.

### 3.1 Aquecimento
- **Principal:** inscritos no lançamento
- **Secundários possíveis:** envolvimento curto (ex: 30D), visitou páginas do
  lançamento, video view
- **Advantage+:** vale testar ligado
- **Quando:** durante todo o período de captação
- **Materiais impulsionados:** gravação das lives de aquecimento, banner chamando
  pras lives (destino: página com todas elas), e conteúdos específicos quando houver

#### Verba por live só dilui se você fragmentar — VARIAÇÃO ISOLADA

*(2º lançamento, 2ª semana de captação. Um lançamento, um cliente — confirmar
antes de virar regra.)*

Ao decidir quais lives impulsionar, a conta *verba total ÷ número de lives* **não
é o critério certo**, e é fácil cair nela. No 2º lançamento ela quase cortou os 10
depoimentos de aluno: a verba da fase dividida por 20 lives dava uma fatia por live
fina demais pra mover ponteiro.

O erro é que essa divisão **só acontece se cada live virar campanha ou conjunto
próprio**. Como **anúncio dentro do mesmo conjunto**, não há divisão nenhuma: o
algoritmo concentra entrega no que engaja e ignora o resto sozinho. A peça fraca
não consome a fatia dela — ela simplesmente não recebe entrega.

Consequência prática: **peça de aquecimento adicional entra sem custo fixo de
oportunidade**, desde que entre como anúncio. O que limita quantas peças entram
não é a verba — é a leitura (muitos anúncios com pouca verba = nenhum junta
volume pra você saber qual funcionou).

⚠️ **O que essa lógica NÃO resolve sozinha:** se o objetivo é o inscrito
consumir *várias* lives diferentes, o leilão trabalha contra por padrão — ele
concentra na peça vencedora, porque otimiza o objetivo declarado, não
variedade. Isso é o comportamento default, **não um limite do tráfego pago**.

*(Parágrafo corrigido a pedido do Rodrigo. A versão anterior, de antes de o
método ser registrado, concluía que quem entrega variedade é a página com todas
as lives, e que o caminho mais barato é e-mail e WhatsApp, não tráfego pago. Isso
extrapolava: descrevia o default do leilão como se fosse teto da mídia paga.)*

Há **dois caminhos**, e eles somam em vez de competir:

1. **Rotacionar no tráfego.** Ligar e desligar peças em ciclo força a
   distribuição que o leilão não faz sozinho. Custa operação diária, e o
   ganho depende de o objetivo da campanha estar certo — rotacionar peça
   numa campanha que otimiza pro evento errado só espalha o erro (ver a nota
   sobre meta de conversão do aquecimento, abaixo).
   📌 **Isto virou regra operacional com número poucos dias depois** — quanto o
   leilão concentra de fato (75,9% numa peça), o limite que dispara o ciclo
   (40%) e a ressalva de não desligar vencedor estão em *"Conjunto único
   concentra a verba numa peça só"*, mais abaixo nesta mesma seção.
2. **Página com todas as lives**, alimentada por e-mail e WhatsApp. Continua
   sendo o caminho de **menor custo marginal** pra variedade (base inteira,
   sem CPM), e não depende de rotina nenhuma.

Regra prática: o pago entrega **alcance** e o próprio ciclo de rotação;
e-mail/WhatsApp entregam **profundidade de catálogo** de graça. Escolher um só
por achar que o outro não funciona é perder metade.

E o inverso continua valendo: separar por **campanha** para ler tipos diferentes
(conteúdo x depoimento) é o pior dos dois mundos — duas campanhas no mesmo
público de inscritos disputam o mesmo inventário e encarecem uma à outra. A
leitura por tipo sai do **nome do anúncio** (`AD - LIVE NN` x `AD - PROVA NN`),
que é de graça.

#### A métrica do aquecimento é VIEW, não CTR nem MQL — PADRÃO CONSISTENTE

*(Definido pelo Rodrigo, corrigindo análise que tinha usado CTR.)*

Aquecimento se lê por: **views**, **custo por view** e **retenção (25% / 50% /
75% / 100%)**. Não por CTR, e não por custo por MQL.

Por quê: aquecimento roda em objetivo de ENGAJAMENTO/THRUPLAY sobre quem **já
é inscrito**. Não existe lead novo pra gerar, então custo por MQL — que é a
régua de decisão da **captação** — não tem o que medir aqui. E CTR mede vontade
de clicar, não tempo de tela: a peça que interessa é a que o inscrito
*assiste*, e isso só aparece na retenção.

Ao ranquear peça de aquecimento, comparar custo por view entre elas e olhar
onde a retenção cai. Peça cara por view ou que despenca antes dos 25% é
candidata a sair; CTR alto com retenção baixa é isca, não conteúdo.

#### Vantagem de largada trava a verba no Google — VARIAÇÃO ISOLADA

*(2º lançamento, medido no 8º dia das peças no ar. Um lançamento, um cliente.)*

Em campanha Demand Gen com várias peças no mesmo grupo, **a peça que sobe
primeiro acumula histórico e trava a verba**, mesmo sendo pior que as que
entram depois. Medido: `AD - LIVE 01` e `AD - LIVE 02` subiram no dia 1 e, 8
dias depois, seguravam **78% do gasto** com o **pior CTR do conjunto** (4,83% e
4,93% contra 7,84% da melhor).

A confirmação veio de fora: as mesmas peças na **Meta**, onde todas subiram
juntas no mesmo dia, produziram ranking **oposto** — lá o algoritmo escolheu
sozinho um depoimento (`PROVA 02`) e a `LIVE 05`, exatamente as duas de melhor
CTR no Google e que lá recebiam migalhas. Duas plataformas, mesmo criativo,
escolhas opostas: o que separa não é qualidade, é ordem de entrada.

**O que fazer:** subir todas as peças de aquecimento **no mesmo dia**, pra
nenhuma ganhar histórico antes das outras. Quando não der (live que só existe
depois), pausar a peça travada é o que libera a entrega — não adianta
esperar o algoritmo redistribuir sozinho.

⚠️ **Demand Gen não tem controle de rotação.** `ad_group.ad_rotation_mode`
volta `UNSPECIFIED` — *girar uniformemente* é recurso de Search/Display e não
existe aqui. E dividir em mais grupos de anúncio **não** força rateio: em
Demand Gen o orçamento é de **campanha**, não de grupo. Só campanha separada
forçaria, e isso fragmenta o sinal (ver 2.4). Conferido na API.

#### A régua de plataforma no aquecimento é PROFUNDIDADE, não custo — VARIAÇÃO ISOLADA

*(Decidido pelo Rodrigo, depois de a medição contrariar a recomendação que
tinha sido dada. 2º lançamento, um cliente, um lançamento.)*

Medido na primeira semana das peças de aquecimento no ar, só nelas, com janelas
casadas (números e método na evidência do caso de origem):

| | parte do gasto | custo por minuto assistido | minutos por view |
|---|---:|---:|---:|
| Google/YouTube | ~82% | ~1,8× o da Meta | **2,0 min** |
| Meta | ~18% | **o mais barato (1×)** | 0,25 min |

**Por custo, a Meta ganha:** ~1,8x mais barata por minuto assistido — e a
estimativa dela ainda foi generosa (15s por thruplay é piso, não teto).

**Por profundidade, o Google ganha por 8x:** 2,0 minutos por view contra 0,25.

A decisão da casa é **profundidade**, e o motivo é a missão da fase: o
aquecimento existe pra o inscrito *consumir a live*, não pra somar minutos
espalhados. As lives têm 19 a 83 minutos, então "view de 25%" são 5 a 21
minutos de atenção — nenhuma das duas plataformas chega lá pelo pago, mas só o
YouTube entrega tempo contínuo por pessoa. Minuto picado em 15 segundos com
mil pessoas não aquece ninguém.

⚠️ **O erro que produziu a recomendação errada, pra não repetir:** a primeira
comparação deu "empate" porque cruzou **11 dias de gasto com 7 dias de
resultado** — o Analytics do YouTube não tinha processado o resto (ver
armadilhas abaixo). Comparação entre plataformas exige **janela idêntica nos
dois lados**, conferida, não assumida.

**Diretriz permanente (Rodrigo):** daqui pra frente, aumento de
verba de aquecimento segue **sempre a lógica da profundidade** — vai mais
dinheiro pra onde o minuto assistido é **contínuo por pessoa**, mesmo que o
minuto avulso saia mais caro. Aplicado no 2º lançamento como split **70/30 pro
Google**.

Quando for decidir o próximo split, a pergunta **não** é *onde o minuto é mais
barato?*, é ***onde a pessoa fica mais tempo por sessão?***. Métrica de decisão:
`estimatedMinutesWatched / views` do tráfego `ADVERTISING`, comparado contra o
tempo médio por play da Meta. Custo por minuto entra só como desempate quando
a profundidade for parecida.

#### A Meta não otimiza além de 15 segundos — UNIVERSAL

*(Fato de plataforma, sem dimensão de cliente. Conferido na API.)*

O objetivo mais profundo que a Meta oferece pra vídeo é **THRUPLAY = 15
segundos** (ou o fim do vídeo, o que vier primeiro). Não existe otimização por
25%, 50% ou tempo assistido.

Consequência dura: **pra vídeo longo a Meta é estruturalmente incapaz de
perseguir consumo profundo.** Ela não está falhando quando entrega 6 a 16
segundos de tempo médio — está entregando exatamente o que foi pedido. Medido
no 2º lançamento: 40.142 impressões, 37.422 "plays" (autoplay mudo, métrica sem
valor), 4.733 thruplay, e **58 pessoas** passando de 25% do vídeo em 11 dias.

Isso não desqualifica a Meta no aquecimento — desqualifica **cobrar dela**
profundidade. Se a peça é curta (reel, corte de 60s), o teto de 15s não
aperta e a conta muda.

#### Três armadilhas de medição do YouTube — UNIVERSAL

*(Fatos de plataforma. Eram três quando a seção nasceu; a 4 e a 5 entraram
depois. As duas primeiras fizeram a operação afirmar coisa errada no mesmo dia.
Evidência no caso de origem.)*

**1. O YouTube Analytics tem ~4 dias de defasagem.** No dia da medição, o último
dia processado era o de 4 dias antes. Uma consulta pedindo os últimos 11 dias
devolve só os 7 primeiros **sem avisar** — não erra, não alerta, só entrega menos
período do que você pediu. Toda comparação contra gasto (que é do dia) fica
inflada contra o lado do YouTube. **Antes de comparar, peça `dimensions="day"` e
olhe qual foi o último dia com dado.**

**2. A contagem pública de views inclui as pagas.** O número que aparece no
vídeo (o `viewCount` público, que a Data API devolve) é o total — pago +
orgânico. Não serve pra falar de audiência orgânica. O split real só sai do
Analytics, com `dimensions="insightTrafficSourceType"`, onde `ADVERTISING` é o
pago e todo o resto é orgânico. E o filtro de vídeo é obrigatório: sem ele a
consulta devolve o **canal inteiro**, incluindo os criativos de captação, que
são muito mais impulsionados.

Medido nas peças de aquecimento (primeira semana no ar), e repare que a média
esconde dois comportamentos opostos:

| | views | % pago |
|---|---:|---:|
| Live 04 | 9.711 | 2,5% |
| Live 05 | 9.354 | 1,8% |
| Depoimento 02 | 1.220 | **39,3%** |
| Depoimento 03 | 1.020 | **41,9%** |
| **total das peças** | **16.812** | **5,0%** |

Nas lives longas o orgânico carrega quase tudo e o pago é ruído. **Nos
depoimentos o pago é quase metade da audiência.** Falar "o pago é 5%" como
regra da fase é média enganosa — separe por tipo de peça.

**3. Não dá pra pedir fonte de tráfego POR VÍDEO numa consulta só.** A
combinação `dimensions="video"` + `filters="...;insightTrafficSourceType==ADVERTISING"`
volta **HTTP 400** `The query is not supported`. O caminho que funciona é
inverter e rodar **uma consulta por vídeo**:

```python
svc.reports().query(
    ids="channel==MINE", startDate=DE, endDate=ATE,
    metrics="views,estimatedMinutesWatched",
    dimensions="insightTrafficSourceType",     # dimensao = fonte
    filters=f"video=={vid}")                   # filtro = 1 video
```

⚠️ **Isso custa o batching.** N vídeos = N chamadas, o oposto da regra de ler
API em lote (vários objetos por chamada, com cache). Então guarde o resultado em
cache e não rode isso dentro de laço de rotina diária sem necessidade. E uma
leitura que já batcha por vídeo sem recorte de fonte não aceita esse recorte
depois: quem quiser acrescentar `ADVERTISING` nela vai bater no 400.

**4. Dimensão `month`: startDate E endDate no dia 1.** `endDate` no último dia
do mês devolve `400 "end-date does not align to chosen date dimension"`;
`endDate` no dia 1 do mês corrente funciona e traz o mês parcial.

**5. Inscrito não separa pago de orgânico.** `subscribersGained` com
`dimensions="insightTrafficSourceType"` volta `"The query is not supported"`,
e `month` + `insightTrafficSourceType` juntos também. Views por fonte e por
mês sai com **uma chamada por mês** só com a dimensão de fonte. Quem quer
saber os inscritos que vieram de anúncio fica com a atribuição do Google Ads
(`YouTube channel subscriptions`) como teto e o líquido do canal como piso —
são medidas diferentes e não se somam.

#### Conjunto único concentra a verba numa peça só — VARIAÇÃO ISOLADA

*(2º lançamento, 3ª semana de captação.)*

Verba mora no **conjunto** (Meta) e na **campanha** (Google), nunca no anúncio.
Um conjunto com 12 anúncios **não distribui — ele elege**. Medido na Meta em
três dias: `AD - LIVE 06` levou **75,9%** da verba e **7 dos 12** anúncios
ficaram com gasto residual. No Google, no mesmo dia, o topo levou 18,4% — bem
mais espalhado, mas ali o vício é outro (vantagem de largada, acima).

Isso trabalha contra a missão da fase: aquecimento quer **a mesma audiência
vendo várias lives**, o que exige várias rodando.

**O ciclo, decidido pelo Rodrigo** (escolhido no lugar de reestruturar em um
conjunto por peça, que resolve de vez mas exige remontar a estrutura): quem
concentrou num dia é desligado no dia seguinte, a verba escorre pras outras, e
depois ele volta. Na leitura diária da fase, o alerta dispara quando uma peça
passa de **40%** da verba do conjunto.

⚠️ **O alerta não é ordem de desligar — quem concentra às vezes concentra por
ser o melhor.** A `LIVE 06`, que disparou o alerta com 73%, é o vídeo de
**maior retenção do canal**: 30,5% e 22,6 minutos de tempo médio. A plataforma
concentrou nela porque ela segura gente. Cruzar com a retenção antes de pausar
é obrigatório; pausar por concentração pura mata vencedor.

**Também é regra da fase (revogação registrada):** impulsionar **todas** as
peças, live de conteúdo **e** depoimento de aluno. Existiu por pouco mais de uma
semana, na captação do 2º lançamento, uma regra de "paga só nas de conteúdo,
depoimento fica no orgânico" — foi **revogada pelo Rodrigo**. Depoimento aquece
tanto quanto live de tema, e os números acima mostram que é justamente nele que
o pago faz diferença. Se essa regra aparecer escrita em algum lugar, está errada.

#### Fim da fase: as peças saem do ar (privadas no YouTube) — *VARIAÇÃO ISOLADA*

Aquecimento morre na Aula 1: depois dela a peça compete com a aula em vez de
puxar pra ela, e conteúdo gratuito de 20h no ar enfraquece a oferta na semana
de venda. **Ao entrar a Aula 1, as peças de aquecimento viram `private` no
YouTube** — as 10 lives de conteúdo *e* os 10 depoimentos, mesmo escopo do
impulsionamento (regra acima).

Repetiu-se em dois lançamentos da mesma base: o 1º e o 2º (no 2º, privadas no
dia da Aula 1, 20 peças, ~245 mil views somadas). Dois é padrão da casa, ainda
não é 3+ — por isso ISOLADA.

`private` e não `unlisted`: `unlisted` mantém o link direto abrindo, e o link
circula em grupo de WhatsApp de lead. Se a intenção é tirar o conteúdo do ar,
`unlisted` não tira. Privar é **reversível** — dá pra voltar pra `public`, e
views, likes e comentários ficam.

**Executar seguindo a checagem abaixo, peça por peça — nunca no olho, na
interface** (no caso de origem, quem fazia isso era um script com estas travas):

1. Achar as peças pelo **padrão de título**, direto no canal — não por lista de
   id guardada em arquivo.
2. Tocar só no que está `public`.
3. **Não privar vídeo que esteja em anúncio de campanha `ENABLED`** — privar em
   veiculação derruba o anúncio.
4. Reler cada vídeo depois de escrever e conferir que virou `private`.

⚠️ **Conferir a campanha de aquecimento ANTES.** No 2º lançamento ela já estava
`PAUSED` e os remarketings ativos eram todos de site/CRM, então privar não
custou entrega nenhuma. Se a campanha ainda estiver no ar, a ordem é pausar
primeiro — o item 3 bloqueia, mas depender dele é depender do erro acontecer.

### 3.2 Antecipação
- **Principal:** inscritos no lançamento
- **Secundários:** caiu na página de inscrição, envolvimento curto
- **Quando:** última semana de captação
- **Mensagem:** contagem regressiva — faltam X dias

### 3.3 CPLs / Aulas
- **Principal:** inscritos no lançamento
- **Secundários:** caiu na página de inscrição, envolvimento curto
- **Advantage+:** talvez valha testar
- **Quando:** durante toda a semana do evento (7 dias)
- **Destinos diferentes por momento:**
  - *Aula X é hoje / ao vivo agora* → link da aula programada no YouTube
  - *"Aula X liberada"* → blog do lançamento (gravações, botões etc.)
  - *"Todas as aulas liberadas"* → mesmo blog
  - *Volta pro grupo* → remarketing só pra inscritos, oferecendo um benefício

#### Calendário padrão da semana de aulas

Declarado pelo Rodrigo como o padrão da operação (não é hipótese medida — é como a
casa roda):

| Dia | O que acontece |
|---|---|
| Segunda | Aula 1 |
| Quarta | Aula 2 |
| Quinta | Aula 3 |
| Sexta | Entra o "todas as aulas liberadas" |
| Sábado | Carta de vendas |
| Domingo (noite) | Aula 4 — encerramento + sorteio |
| Segunda seguinte | Abre o carrinho |

#### Duração: "é hoje" dura 1 dia, "gravação liberada" dura vários

Erro fácil de cometer ao montar as etapas: tratar cada CPL como se rodasse
só no dia da aula. **Não é assim.** Cada aula tem dois anúncios com vidas
diferentes:

- **"Aula X é hoje"** → roda **só no dia** da aula.
- **"Aula X liberada"** (a gravação) → roda **por vários dias depois**,
  porque muita gente ainda não assistiu e precisa continuar sendo lembrada.
  Na prática a gravação da aula 1 fica no ar praticamente a semana inteira.

Ou seja, as janelas se **empilham**: na quinta-feira estão rodando ao mesmo
tempo a gravação da aula 1, a da aula 2 e o "aula 3 é hoje". A partir de
sexta o "todas as aulas liberadas" entra e passa a carregar o conjunto.

📌 **Consequência prática:** ao configurar etapas no Dash (ou ao ratear verba
por fase), a janela de cada CPL vai da data da aula até a sexta-feira, não
até o dia seguinte. Quem corta no dia da aula subfinancia justamente o
anúncio que recupera quem não assistiu ao vivo.

#### O "é hoje" roda em campanha própria — regra do Rodrigo (11/2026)

> "Isso aí pode se tornar uma regra. A campanha do É Hoje tem que ser separada de campanhas com outro objetivo, eu acredito."

- **Uma campanha por "é hoje"**, com início e fim no dia da aula, separada da gravação e de qualquer campanha com outro
  objetivo. A plataforma desliga sozinha no fim marcado (no Google, o `status` continua ENABLED depois do fim:
  `google-criacao-tecnica.md` §22).
- **Rotina ligando e desligando anúncio dentro de uma campanha só fica de fora**, pelo risco: "pode ser que abre brecha
  para coisa errada, acontecer erros".
- **No Google, o "é hoje" vai pro Display ou não vai.** Demand Gen apontando pra transmissão ao vivo não entrega clique
  (`google-criacao-tecnica.md` §26).
- **O que se viu com a separação:** o "é hoje" trouxe a visita mais barata das aulas, sem sinal de saturação.
- **Não contradiz o §3.1**, que condena separar campanha só pra ler tipo de conteúdo no mesmo público. Aqui o "é hoje"
  tem outro destino (a transmissão) e uma janela de um dia. E o risco de juntar está no próprio §3.1: um conjunto único
  elege uma peça só, então o "é hoje" pode ficar sem entrega justo no dia em que ele vale.
- **Em aberto** (*PADRÃO INCONCLUSIVO*): uma campanha só pras aulas aprenderia melhor? E a frequência somada seria um
  problema? Nenhuma das duas foi medida.

### 3.4 Carta de vendas
- Roda no sábado antes do carrinho abrir
- **Destino:** página estilo carta

### 3.5 Carrinho
- **Principal:** inscritos no lançamento
- **Secundários:** caiu na página de inscrição, envolvimento curto
- **Advantage+:** talvez valha testar
- **Quando:** durante os dias de carrinho (3–4 dias)

### 3.6 Downsell
- **Principal:** inscritos no lançamento
- **Secundários:** caiu na página de inscrição, envolvimento curto
- **Advantage+:** talvez valha testar
- **Quando:** depois do carrinho e da reabertura, na semana da live de downsell
- ⚠️ A casa não faz captação pra downsell (ainda)

### 3.7 Quanto investir em cada fase: alcance × frequência × CPM — *VARIAÇÃO ISOLADA*

*(2º lançamento, medido e construído na véspera da semana de aulas. Primeira vez
que a operação calcula isso. Um cliente, um lançamento.)*

Até aqui a verba de remarketing era repartida por **percentual** — no 2º
lançamento, 77,4% captação / 22,6% remarketing, número herdado do 1º lançamento e
nunca calculado. Percentual não responde a pergunta que importa (*dá pra impactar
todo mundo quantas vezes?*) e, quando finalmente foi confrontado com a conta,
**não pagava nem o cenário mais magro**.

A conta certa tem três variáveis, e as três se medem:

```
custo da fase = alcance × frequência ÷ 1000 × CPM
```

- **alcance** — quantas pessoas a plataforma consegue impactar. **Não é o
  número de leads.** Na Meta sai de `delivery_estimate` (nunca de
  `approximate_count`, ver `sirius-scale/frameworks/trafego/publicos-e-advantage.md`
  §4.2); no Google, de `user_list.size_for_display`.
- **frequência** — quantas vezes cada lead vê um anúncio *daquela fase* no
  período inteiro dela, não por dia.
- **CPM** — medido na própria conta, na fase mais parecida que já rodou.

**O que isso destrava:** a decisão de verba vira faixa explícita (piso/alvo/teto
diferindo só na frequência) em vez de sobra, e dá pra responder *antes de subir*
se o plano cabe. Também dá a barra de retorno: custo ÷ ticket médio = quantas
vendas a fase precisa pra empatar. No 2º lançamento o remarketing inteiro se
pagava movendo a conversão da base em **0,08 ponto percentual** — o que
reposiciona remarketing como a aposta mais barata do lançamento, não como o que
sobra.

📌 **Consequência de método:** planejar remarketing por percentual do tráfego é
um atalho que envelhece mal. O percentual deve ser **consequência** da conta,
não a regra que a define. No 2º lançamento a conta devolveu 28,9% onde o herdado
dizia 22,6%.

**Implementação:** no caso de origem, uma planilha viva (muda alcance, CPM ou
frequência e tudo recalcula), com a análise do plano de remarketing ao lado
(evidência no caso de origem).

⚠️ **A parte fraca, e ela precisa ser dita:** a **régua de frequência** é a
única das três variáveis que não é medida. Ninguém mediu quantos impactos por
lead saturam. Os números de partida do 2º lançamento (CPL 14 · carta 4 · carrinho
18 · reabertura 6 · downsell 9 = 51 impactos por lead) são **decisão declarada,
não ótimo apurado**. O ganho é a decisão ficar explícita e recalculável.

#### O CPM medido não sobrevive à concentração do público

Ao usar CPM histórico pra projetar, conferir **em que público ele foi medido**.
CPM medido num público grande e morno **sobe** quando aplicado a um público
concentrado: menos inventário, mais competição pelas mesmas pessoas. No 2º
lançamento o CPM de referência veio de um público 3,2x maior que o alvo do plano
— a projeção foi feita com esse número e marcada como a incerteza principal, com
reconferência agendada pra 2 dias depois de subir.

#### Secundário em OR vira maioria — e ninguém percebe pelo nome

*(Medido no 2º lançamento, na véspera da semana de aulas; ver
`sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.2 pro método de
medir tamanho.)*

O §3.1 a §3.6 listam "envolvimento curto", "caiu na página de inscrição" e
"video view" como públicos **secundários possíveis** das fases de remarketing.
Montados todos em OR **dentro do mesmo conjunto**, o secundário deixa de ser
secundário:

| Público no conjunto `00 - [INSCRITOS]` | Tamanho | É lead? |
|---|---:|---|
| `IG - ENGAJARAM 30D` | 20.000 | não |
| `SITE - PAGE VIEW CAPTURA` (viu e não se inscreveu) | 11.150 | não |
| `SITE - PAGE VIEW OBRIGADO` | 5.150 | sim |
| CRM de leads | 6.300 | sim |
| **união — o que o conjunto mira de fato** | **30.500** | |
| **só inscritos** | **9.500** | |

**3,2x o núcleo, e 69% do dinheiro indo pra quem não é lead do lançamento** —
com Advantage Audience desligado, ou seja, não é expansão automática: é o
próprio público. O nome do conjunto dizia `[INSCRITOS]`.

**Regra:** público secundário em fase de remarketing entra em **conjunto
separado, com verba e leitura próprias** — nunca em OR com o núcleo. Junto, ele
não é secundário, é a maioria, e não dá pra ler nem controlar quanto foi pra
cada um. E o teste que revela isso é o mesmo do
`sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.3: comparar
**alcance realizado contra tamanho do público**, nunca ler o nome do conjunto.

**Como ficou no 2º lançamento (decisão do Rodrigo):** dois conjuntos por
campanha, com o orçamento em nível de **conjunto (ABO)** — `00 - [INSCRITOS]`
com 75% da verba, `01 - [SECUNDARIOS]` com 25% e **exclusão do conjunto 00**,
pra os dois não disputarem a mesma pessoa e encarecerem um ao outro. O
secundário recebe pouco de propósito: público 2,2x maior com um terço da verba
dá frequência baixa — secundário lembra, não martela.

#### ⚠️ CORRIGIDO NO MESMO DIA — o cap NÃO é a alavanca de frequência; o GOAL é

*(Esta seção foi escrita e corrigida no mesmo dia. A versão original dizia que o
limite de frequência era "a trava dura". Está errado, e a correção veio de medir
os 66 conjuntos de remarketing de dois lançamentos — o 1º e o anterior a ele —
em vez de 2.)*

**O que manda na frequência é o `optimization_goal`, não o cap e não o público:**

| goal | conj. | alcance | impressões | **freq real** | custo por clique (`LANDING_PAGE_VIEWS` = 1) | CTR |
|---|---:|---:|---:|---:|---:|---:|
| `IMPRESSIONS` | 17 | 41.537 | 162.529 | **3,91** | ~3,1 | 0,33% |
| `THRUPLAY` | 5 | 3.470 | 13.156 | 3,79 | ~6,6 | 0,38% |
| `LANDING_PAGE_VIEWS` | 13 | 37.112 | 113.321 | **3,05** | **1** | **1,63%** |
| `REACH` | 30 | 210.736 | 274.370 | **1,30** | ~2,8 | 0,41% |

E há **quatro pares perfeitos** no 1º lançamento (três estão abaixo) — mesma
peça, mesma campanha, mesmo público, gasto parecido, só o goal muda:

| peça | goal | cap | gasto (`IMPRESSIONS` do par = 1) | alcance | freq |
|---|---|---:|---:|---:|---:|
| É HOJE | `IMPRESSIONS` | — | 1 | 4.871 | **3,38** |
| É HOJE - Alcance | `REACH` | 3 | ~0,78 | 8.330 | **1,09** |
| 3 DIAS | `IMPRESSIONS` | — | 1 | 869 | **4,07** |
| 3 DIAS - Alcance | `REACH` | 1 | ~0,73 | 1.404 | **1,11** |
| 5 DIAS | `IMPRESSIONS` | — | 1 | 795 | **3,90** |
| 5 DIAS — ALCANCE | `REACH` | **10** | ~1,57 | 1.558 | **1,17** |

📌 **Repare na última linha: cap de 10 entregando frequência 1,17.** O cap é
**teto, não piso** — e `REACH` procura pessoa nova por desenho, então nunca
chega perto do teto. Configurar cap alto numa campanha de `REACH` não produz
frequência nenhuma.

**A escolha certa depende do que a fase precisa** — e o CTR mostra que não é
frequência bruta:

- **Quer clique barato (o caso normal em remarketing):** `LANDING_PAGE_VIEWS`.
  Ganha em tudo — clique 3x mais barato que `IMPRESSIONS`, visita 6x mais
  barata, CTR 5x melhor — e ainda entrega frequência 3,05.
- **Destino sem pixel (YouTube, WhatsApp):** `LANDING_PAGE_VIEWS` não funciona,
  porque a Meta não consegue medir o carregamento da página. O análogo é
  `LINK_CLICKS` — **sem histórico nesta conta**, portanto INCONCLUSIVO.
- **Quer alcance amplo e barato (avisar todo mundo uma vez):** `REACH`.
- **`IMPRESSIONS` compra frequência cara e vazia** (CTR 0,33%). Só faz sentido
  quando o objetivo é lembrete visual puro, sem clique.

**O que sobra da versão original:** o cap continua sendo um **teto** útil pra
impedir superexposição em público pequeno. Só não é o que produz frequência.

#### A versão original desta seção (mantida como registro do erro)

*(Medido comparando o 1º lançamento com o anterior a ele, na mesma conta. Dois
lançamentos, um cliente.)*

Planejar frequência pelo orçamento assume que o dinheiro vira impacto. Na Meta
não vira: campanha de alcance tem **`frequency_control_specs`**, e ele é uma
trava **dura** — acima do cap, a plataforma simplesmente não entrega, por mais
verba que exista no conjunto.

| Lançamento | Cap | Alcance | Gasto (1º lançamento = 1) | **Frequência realizada na fase** |
|---|---:|---:|---:|---:|
| 1º lançamento `[RMKT][CPLS]` | **2/dia** | 33.922 | 1 | **5,57** |
| lançamento anterior `[RMKT][CPLS]` | **5/dia** | 6.996 | ~1,4 | **14,43** |

2,6x mais frequência com público 4,8x menor e gasto parecido. As duas causas
somam — cap mais alto **e** público concentrado —, e nenhuma delas é orçamento.

**Regra:** ao planejar por alcance × frequência, **configurar o cap junto**.
Cap e régua têm que ser o mesmo número; se o cap for menor, a régua é ficção. A
prática já existe na casa (31 conjuntos com cap configurado nesses dois
lançamentos, valores de 2 a 10/dia) — o que faltava era ligá-lo ao planejamento
em vez de escolher no olho.

⚠️ **Só a Meta expõe isso desse jeito.** No Display do Google há controle de
frequência por campanha; em **Demand Gen não existe** — lá a frequência sai do
orçamento contra o tamanho do público, e a única forma de controlá-la é a conta
desta seção.

#### Display é o canal de frequência: um quarto do CPM da Meta — *VARIAÇÃO ISOLADA*

*(CPM medido no 1º lançamento, confirmado no anterior a ele. Um cliente.)*

Quando a régua pede frequência alta (7+ impactos/dia), o canal decide se ela
cabe no orçamento:

| Canal | CPM (Meta remarketing = 1) | Base |
|---|---:|---|
| **Google Display — fase de CPL** | **~0,25** | 110.880 impressões (4 campanhas do 1º lançamento) |
| Google Demand Gen | ~0,57 | 224.889 impressões (aquecimento do 2º lançamento) |
| Meta — remarketing | 1 | 69.249 impressões (antecipação do 2º lançamento) |
| Google Display — fase de vendas | ~0,89 | 20.106 impressões — N pequeno, INCONCLUSIVO |

**A divisão de trabalho que sai daí:** Display carrega o **volume de
frequência**; Meta e Demand Gen carregam a **atenção** (vídeo com som, feed,
YouTube). Somam, não competem — e é o Display que faz uma régua de 10/dia caber
num teto que a Meta sozinha estouraria (no 2º lançamento: só de Meta, a 7/dia, a
conta dava ~1,2× o plano inteiro nos três canais).

📌 **Custo escondido:** Display pede formatos próprios (300x250, 336x280,
728x90, 300x600, 320x100) ou responsivo (1200x628 + 1200x1200). Peça de feed e
stories **não serve**. Ao planejar Display, contar a derivação das artes como
pré-requisito — senão o canal mais barato do plano é o que trava a subida.

#### Faixa de score só se corta no CRM, nunca no pixel — *UNIVERSAL*

*(Apontado pelo Rodrigo. É mecânica de plataforma.)*

O score do lead mora no Dash. O **pixel não sabe nada disso** — ele registra
quem visitou a página de obrigado e mais nada. Então cortar a faixa D do
remarketing só existe no público **CRM**, subindo a lista sem os D.

E aí vem a armadilha: se o conjunto usa **CRM OU pixel** (que é o desenho certo
pra maximizar alcance), quem é D e passou pela página de obrigado **volta pelo
pixel**. O corte vira parcial sem avisar.

**Consequência de desenho:** segmentação por qualidade de lead e maximização de
alcance **brigam entre si**. Quem quer cortar por faixa precisa decidir isso na
arquitetura do conjunto desde o começo — CRM segmentado como público principal,
pixel em conjunto separado — não como ajuste no meio do lançamento.


---

## 4. O que os dados do 1º lançamento mostraram

Análise de 47 conjuntos ativos, todos otimizando para evento LEAD via pixel.

| Padrão | Custo médio/lead (Advantage+ = 1) | Variação (× a média do Advantage+) |
|---|---|---|
| Advantage+ / amplo, 1 criativo (43 conjuntos) | 1 | ~0,4 – ~3,4 |
| Lookalike/custom, múltiplos criativos (4 conjuntos) | ~1,2 | ~0,73 – ~1,7 |

⚠️ **Não generalizar:** o padrão lookalike tem só 4 conjuntos — amostra fina demais
pra virar regra. E dentro dele, volume de criativo, gasto e período estão colados,
então não dá pra isolar a causa.

Nenhum conjunto de "interesse puro" apareceu neste lançamento.

---

## 5. Hipóteses em teste (ainda não são regra)

### Fragmentar em campanha de ENGAJAMENTO custa o mesmo que em CONVERSÃO? — PADRÃO INCONCLUSIVO

*(Levantado discutindo como garantir verba por peça no aquecimento.
**Raciocínio sobre mecanismo, zero medição** — por isso está aqui e não no §3.1.)*

O §2.4 registra que fragmentar mata o sinal em Demand Gen, e o motivo que ele
mesmo dá é específico: *"cada campanha precisa de volume próprio de
**conversão** pra sair do aprendizado"*. A hipótese é que, numa campanha de
**engajamento** — o aquecimento roda ENGAGEMENT/THRUPLAY e não tem evento de
conversão pra aprender —, esse mecanismo não tem o que dividir, e fragmentar
custaria bem menos. Se for verdade, muda a resposta pro problema de
concentração do §3.1: um conjunto por peça deixaria de ser "caro demais".

**Por que ainda NÃO é regra:**

- Nunca foi medido nenhum aquecimento fragmentado. Zero dado.
- ENGAGEMENT/THRUPLAY **também** é evento de otimização e **também** tem fase
  de aprendizado própria. O mecanismo do §2.4 pode se aplicar igual, só com
  outro evento.
- No Google o orçamento é de **campanha**, então fragmentar por peça significa
  N campanhas — o jeito mais caro possível de testar isto.

*Como resolver, barato:* testar **na Meta**, onde a verba mora no conjunto.
Dois conjuntos com metade das peças cada, contra o conjunto único de hoje,
mesma verba total. Comparar concentração (share do maior anúncio) e retenção.
Se a concentração cair sem a retenção piorar, a hipótese ganha corpo.

⚠️ **Isto não altera o §2.4**, que segue valendo como está — inclusive a linha
dele na §7 ("transfere como mecânica"). Restringir aquele texto a campanhas de
conversão é mexer no **alcance** de um registro existente, e isso é decisão do
Rodrigo, não de quem aplica. Aqui é hipótese nova, não correção da antiga. Se o
teste de vocês der outra coisa, o registro vai em `frameworks-da-casa/`
(`sirius-scale/REGRAS.md` §4).

### Semelhante + Advantage+: ligar ou desligar?
Dúvida em aberto. O raciocínio: se deixar o Advantage+ ligado em cima de um
semelhante, vira *semelhante do semelhante*. Se for esse o caso, talvez seja melhor
sugerir um público quente e deixar o Advantage+ ligado, em vez de usar semelhante.

*Como resolver:* acumular dado de 2–3 lançamentos com as duas configurações e
comparar CPL. Não decidir no achismo.

### Advantage+ nos remarketings
Marcado como "vale testar" / "talvez valha testar" em aquecimento, CPLs, carrinho e
downsell — ou seja, ainda não é padrão nem descartado.

### Advantage+ de anúncio
Observação da operação: os Advantage+ **de anúncio** ainda não parecem funcionar tão
bem, por isso ficam de fora na pré-escala. Ainda é percepção, não medição.

### Públicos de interesse
Em queda de uso — não está funcionando como funcionava antes. Não apareceu no
1º lançamento.

---

## 6. Relação com outros frameworks

A **distribuição de conteúdo** (impulsionar posts pra crescer base e públicos)
alimenta diretamente os públicos quentes usados aqui — tanto no mix quente da
captação quanto nos remarketings. Que cortar distribuição hoje piora o custo dos
lançamentos seguintes é **PADRÃO INCONCLUSIVO** (a força foi marcada depois; antes
a frase vinha sem força). É a leitura do Rodrigo pra um ciclo: numa reunião ele
chamou de teoria ("e aí até minha teoria, assim, né") e, três semanas depois,
contou como teste. O debriefing do 2º lançamento diz que o bolo não cresceu e
deixa INCONCLUSIVO, porque o mesmo número aceita outra causa. Detalhe em
`sirius-scale/frameworks/conteudo/conteudo-que-alimenta-o-funil.md`, ponto em
aberto 5.

---

## 7. O que transfere e o que é do caso

**Pré-requisito:** este framework pressupõe **lançamento gratuito com evento de
aulas**. Se o cliente novo roda outro modelo, pare aqui — o que transfere dele
são só os itens marcados "mecânica" abaixo.

**Transfere como mecânica (vale em qualquer cliente e modelo):**

- **§2.4** — Demand Gen aprende **por campanha**, então 1-1-1 fragmenta o sinal
  e prende tudo em aprendizado. Isso é como o Google funciona, não é do caso-base.
  Corolário: 1-1-1 é estrutura pra testar **criativo na Meta**, não público no
  Google.
- A ressalva de **subir orçamento em degraus (~20–30%)** pra não resetar a fase
  de aprendizado — mecânica documentada da própria Meta.
- Conferir `promoted_object.custom_event_type` antes de confiar no objetivo
  (repetido de `sirius-scale/frameworks/trafego/_metodologia.md` §1).
- Excluir leads já cadastrados na captação fria.
- **§3.1 — a Meta não otimiza vídeo além de 15s (THRUPLAY).** Não existe
  otimização por 25%/50% nem por tempo assistido. Vale em qualquer conta:
  pra vídeo longo, cobrar profundidade da Meta é cobrar o que ela não faz.
- **§3.1 — as duas armadilhas de medição do YouTube.** O Analytics tem ~4 dias
  de defasagem e entrega janela menor do que a pedida **sem avisar**; e a
  contagem pública de views **inclui as pagas**, então não serve pra falar de
  orgânico. As duas são comportamento de plataforma, não do caso-base, e as duas
  já produziram conclusão errada aqui.
- **§3.1 — verba mora no conjunto/campanha, nunca no anúncio.** Conjunto com
  muitos anúncios elege um em vez de distribuir. Aritmética de leilão, não
  característica de cliente.

**Transfere como método (adaptar, não copiar):**

- **§1, a arquitetura de 6 fases** e o papel de cada uma — é o desenho do
  modelo, e é o que mais vale levar pra outro cliente que rode lançamento
  gratuito.
- **§2.1, a escada teste → pré-escala → escala** e, principalmente,
  **§"as 3 etapas COEXISTEM"**: a escada diz onde colocar dinheiro novo, não o
  que desligar. Essa regra evita o erro mais caro já registrado na casa (matar o
  teste que sustentava a venda).
- O critério de graduação ser **custo por MQL / faixa A+B**, nunca CPL isolado.
  Em cliente sem pesquisa, cai pro CPA real (ver
  `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §6).
- **§2.2 e §2.3** — mix quente amplo com vários criativos, e frio com
  semelhantes.
- **§3, os 5 tipos de remarketing** — a semântica de cada régua (aquecimento,
  antecipação, CPL, carta, carrinho, downsell).
- **§6** — distribuição de conteúdo alimenta o público quente do lançamento
  seguinte; cortar hoje encarece depois.

**Do caso (o caso-base), não copiar:**

- Todos os números do **§4** (o que o 1º lançamento mostrou) e do §2.4 (22
  conversões, 10,9% do orçamento, CPA ~23% abaixo do alvo). São daquela conta,
  naquele nicho, naquele orçamento.
- Os múltiplos de escala (3x/5x/10x) — dependem de quanto o lançamento precisa
  escalar, que é decisão de meta, não constante.
- O **§5 (hipóteses em teste)** é a agenda de dúvidas *daquela* operação. Em
  cliente novo, as dúvidas provavelmente são outras — não herde a lista, monte
  a sua.

⚠️ **Cuidado com a correção do Rodrigo no §2.1.** Ela é um bom exemplo de por que
não copiar cru: a regra original (escalar só por duplicação) foi extraída de
meia leitura do 1º lançamento — na prática duplicação **e** aumento direto
conviveram. Em cliente novo, as duas formas estão abertas; o que não está aberto
é a alta grande de uma vez.
