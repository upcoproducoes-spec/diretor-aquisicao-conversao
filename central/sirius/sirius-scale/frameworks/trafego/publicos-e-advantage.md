# Públicos e Advantage+ — o que é limite e o que é palpite

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** majoritariamente técnica de plataforma
> **Alcance:** **a mecânica é UNIVERSAL** — como o Advantage+ trata controle x
> sugestão, os dois interruptores, o público desatualizado que mente o tamanho,
> o marco percentual em vídeo longo. Nada disso é do caso-base: é comportamento
> da Meta, e vários itens se provam por aritmética (alcance > público é impossível).
> **Os números e as decisões** (tamanhos de público, CPM, a escolha de semente
> do lançamento de referência) são NÃO TESTADO FORA. Ver §6.
> Este é, junto com `sirius-scale/frameworks/trafego/nomenclatura.md`, **o
> framework mais transferível da biblioteca** — leve inteiro pra cliente novo de
> qualquer negócio.

> Levantado nas fontes oficiais da Meta, a pedido do Rodrigo, antes de decidir se
> valia testar lookalike/interesse num lançamento do caso-base. A mecânica abaixo
> é **CONSISTENTE** (documentação oficial + fontes técnicas convergentes). A
> decisão de teste que sai dela é **VARIAÇÃO ISOLADA** — um cliente, um
> lançamento, ainda não medida.

> **Como ler as checagens.** Os nomes de campo (`advantage_audience`,
> `targeting_relaxation_types`…) são o que o Claude lê pela API quando a conta
> está conectada. Junto vai o que conferir na tela do Gerenciador, porque quem
> ativa a campanha é a pessoa dona da conta (o Claude monta pausado,
> `sirius-scale/REGRAS.md` §6). A Meta
> muda rótulo de tela sem aviso: se um nome não bater, confira pelo efeito (§4.3),
> não pelo rótulo.

## 1. A distinção que decide tudo: controle x sugestão

Com **Advantage+ audience ligado**, a Meta separa o que você informa em duas
categorias, e elas se comportam de forma completamente diferente:

| Entra como | O que é | Comportamento |
|---|---|---|
| **Controle (limite duro)** | localização, idade mínima, idioma, **exclusões**, Special Ad Category | A Meta **não** entrega fora disso |
| **Sugestão (palpite)** | faixa etária, gênero, interesses/detailed targeting, público personalizado, **lookalike** | A Meta entrega fora quando prevê performance melhor |

**Consequência prática, e ela é grande:** "lookalike com Advantage+ ligado" e
"interesse com Advantage+ ligado" **não são testes de público**. A Meta pode
ignorar os dois e entregar no mesmo lugar do amplo. Pra virar restrição de
verdade é preciso desmarcar as caixas — o que desliga o Advantage+ e devolve
o comportamento de público original.

**Medido no gênero (VARIAÇÃO ISOLADA, 1 lançamento, divisão por gênero da própria Meta):**
- Conjuntos marcados só mulher, mas com o Advantage ligado, gastaram com homem a mesma fatia (perto de 2%) que conjuntos
  sem gênero nenhum e com o Advantage ligado.
- Os conjuntos com o Advantage desligado gastaram 0% com homem.
- Ou seja: marcar o gênero com o Advantage ligado não muda nada. Produto que é só de um gênero precisa do gênero como
  controle, e isso desliga o Advantage do público.
- A prova é a divisão por gênero da Meta, não a pesquisa: pesquisa com pouca resposta mostra o público que respondeu.

**Exclusão é a exceção, e por isso é a alavanca mais valiosa:** ela continua
sendo limite duro mesmo com o Advantage+ ligado. É a única forma de mexer em
público sem tocar no que já funciona.

## 2. Os números oficiais da Meta

Melhora mediana de CPA com Advantage+ audience, 99,9% de confiança:

| Etapa de funil | Melhora mediana de CPA |
|---|---:|
| Topo | **14,8%** |
| Meio | 9,7% |
| Fundo | 7,2% |

E **8% menor custo por lead** em campanhas de lead com formulário instantâneo,
contra o público original, em anunciantes pequenos.

⚠️ **A Meta mede CPA e CPL — não qualidade de lead.** Essa é exatamente a
métrica que esta operação usa pra decidir
(`sirius-scale/frameworks/trafego/_metodologia.md` §3.1). Existe sinal recorrente
entre praticantes de que o Advantage+ degrada qualidade justamente em campanha de
lead. Ou seja: os números oficiais dizem que desligar piora o custo, e não dizem
nada sobre o que acontece com o MQL.

## 3. A decisão da casa — *VARIAÇÃO ISOLADA*

Contexto: a estrutura em uso (amplo + Advantage+, deixando a Meta trabalhar no
criativo) veio de uma aula de outro cliente da casa sobre lançamento **pago**, foi
adaptada pro **gratuito**, e ganhou o lançamento anterior do caso-base. Não há
motivo nos dados pra reestruturar.

**O que fazer:**

1. **Exclusão dos leads na captação fria** — não é teste, é correção. Limite
   duro, funciona com Advantage+ ligado, risco estrutural zero. Sem isso se
   paga pra readquirir quem já está na base.
   Na prática: um público de lista (CRM) com todos os leads do lançamento,
   aplicado como **exclusão** em todo conjunto de captação fria. Lista de
   clientes é **estática**: não cresce sozinha. Sem reenviar ao longo da
   captação, todo lead que entra depois da criação continua sendo readquirido
   a peso de ouro, porque a exclusão não o conhece.
   **O que conferir:** o público de exclusão está na parte de exclusão de cada
   conjunto de captação fria, e o tamanho dele acompanha a base (a lista foi
   reenviada). E-mail sobe normalizado e em SHA-256 (§4).
2. **UMA célula com Advantage+ desligado**, lookalike de semente de qualidade
   (MQL ∪ faixa A/B, pouco mais de mil e-mails na época), **julgada por taxa de
   MQL com o teste z** (`sirius-scale/frameworks/trafego/mql-e-qualificacao.md`
   §3.7) — nunca por CPL. Testar por CPL é perder de antemão: os números da Meta
   acima já dizem que o CPL piora. A hipótese sob teste é qualidade, então a
   leitura tem que ser de qualidade.
3. **Não testar público genérico com Advantage+ ligado.** Gasta verba num
   teste que, pela §1, não é teste.

**O que rende mais que qualquer um dos três:** volume de criativo. Contas de
topo sobem 12–19 criativos novos por semana e acertam ~9% de vencedores;
medianas sobem 6–7 e acertam ~4%. Quando houver fila de criativo parada e
verba curta, a fila ganha da matriz de públicos.

## 4. Semente de lookalike: use o sinal de qualidade, não a base toda

Medido num lançamento do caso-base, no meio da captação (base de ~3,7 mil leads):

| Semente | E-mails (aprox.) | Da base | Serve? |
|---|---:|---:|---|
| Todos os leads | ~3.700 | 100% | só pra **exclusão** — nunca como semente |
| MQL | ~550 | ~15% | serve (piso da Meta é 100) |
| Faixa A+B | ~950 | ~26% | serve |
| **MQL ∪ faixa A/B** | **~1.090** | **~29%** | **preferir esta** — maior pool de qualidade |
| MQL ∩ faixa A/B | ~410 | ~11% | mais puro, pouco alcance |

A taxa de casamento no upload costuma ficar em 50–70%, então ~1.090 enviados
viram ~600–750 casados. Acima do mínimo, abaixo do recomendado (1.000+) — a
semente melhora sozinha conforme a captação anda, então vale reenviar perto
do fim da captação.

**Privacidade:** o e-mail nunca sai em texto puro. Normaliza (minúscula, sem
espaço) e envia SHA-256, que é o formato que a Meta exige pra casar lista.

## 4.1 Advantage+ por FASE, não por conta — *VARIAÇÃO ISOLADA*

Levantado a pedido do Rodrigo, no mesmo lançamento, no dia seguinte. A seção 3
tratou de **captação fria**; esta trata do resto do funil, e a regra se inverte.

**A regra:** Advantage+ audience **ligado em captação, desligado em toda fase
que mira quem já está dentro** — aquecimento, antecipação, CPL, carrinho,
downsell, remarketing. Vale nas duas plataformas: no Google o equivalente é a
**segmentação otimizada** (`ad_group.optimized_targeting_enabled`, no grupo de
anúncios; ver §4.6).

**Por quê:** pela seção 1, com Advantage+ ligado o público personalizado é
sugestão, não limite. Em captação isso é o objetivo — expandir é o trabalho.
Em fase posterior é o oposto: a mensagem ("FALTAM 7 DIAS", "começa amanhã",
"assista à aula 2") só faz sentido pra quem já sabe o que vai acontecer.
Entregar isso pra frio é verba perdida e mensagem sem contexto.

**O argumento quantitativo, que é mais forte que o conceitual:** o público
declarado da antecipação media **~6 a 7 mil pessoas** (`delivery_estimate`), e o
orçamento diário do maior conjunto, ao CPM real da conta, comprava ~7.300
impressões por dia — **115% do público**. A conta é sempre esta: verba do dia ÷
(CPM ÷ 1.000) = impressões; impressões ÷ tamanho do público = quanto do público a
verba de um dia cobre. A Meta não tinha como gastar aquilo dentro do público
mantendo performance; com o Advantage+ ligado, expandir era a saída de menor
resistência. Quanto menor o público quente em relação ao orçamento, mais o
Advantage+ ligado vira entrega ampla.

⚠️ **Ressalva sobre esse número, levantada pelo Rodrigo no mesmo dia:** um dos
quatro públicos do combo (o de engajamento no IG de 30 dias) estava com o tamanho
travado no stub de 1.000 por estar desatualizado (ver §4.2). O público real da
antecipação é maior que ~6 a 7 mil — provavelmente na faixa de 15 a 25 mil, por
interpolação entre o de 15 dias (~7 mil reais) e o de 90 dias (~22 mil). **Os
"115% do público" estavam inflados.** A decisão de desligar continua de pé pelo
argumento conceitual (mensagem de antecipação não pode ir pra frio) e porque a
razão orçamento/público continua apertada, mas o número exato só sai depois que
o público voltar a atualizar em veiculação. Refazer a medição quando isso
acontecer.

> **Atualização (fim do mesmo dia):** o público de engajamento de 30 dias voltou
> a atualizar e passou a reportar **~13 a 15 mil** (status Normal). A
> interpolação acima chutou 15 a 25 mil — ficou na faixa certa, um pouco
> alta. Confirma a §4.2 duas vezes: o "1.000" era stub mesmo, e o jeito de
> descobrir o tamanho real foi colocar em veiculação, não estimar. O tamanho
> do combo da antecipação ainda não foi remedido.

**Corolário de orçamento:** desligar resolve metade. A outra metade é
dimensionar o orçamento ao público (ou ampliar o público com quente de
verdade). Com Advantage+ desligado e orçamento maior que o público comporta, a
Meta sobe frequência ou subentrega — ambos preferíveis a entregar pra frio,
mas nenhum dos dois é de graça.

**Onde parar ao ampliar:** o critério não é tamanho, é se a mensagem faz
sentido. Público que teve contato com **este** lançamento (viu o criativo,
visitou a página, se inscreveu) aceita contagem regressiva. Público de marca em
geral (seguidores, engajamento de 365D, video view de distribuição) nunca ouviu
falar do lançamento — pra esses a peça tem que ser **convite**, não contagem
regressiva. Ampliar sem trocar o criativo recria na mão o problema que
desligar o Advantage+ resolveu.

**Estado no caso-base, depois da execução:**

| Plataforma | Fase | Situação |
|---|---|---|
| Meta | captação | Advantage+ ligado ✅ |
| Meta | aquecimento (`00 - INSCRITOS`) | ~~já estava desligado ✅~~ **errado — só um dos dois interruptores estava desligado. Ver §4.3** |
| Meta | antecipação (6 conjuntos `FALTAM X DIAS`) | **estava ligado — desligado no mesmo dia** |
| Google | captação (20 grupos) | otimizada ligada ✅ |
| Google | aquecimento (`01 - ENVOLVIMENTO CURTO + BASE`) | otimizada desligada ✅ |

**A causa raiz não foi decisão, foi omissão.** A criação do aquecimento passava
`"targeting_automation": {"advantage_audience": 0}` de propósito. A da antecipação
não passava `targeting_automation` nenhum — **e a Meta aplica o default
LIGADO**. Regra dura pra qualquer criação nova de fase posterior: deixar o
Advantage+ desligado **explicitamente** (pela API, `advantage_audience: 0`; à mão,
conferir o card Público de cada conjunto antes de publicar). Não passar não é
neutro.

A correção no caso-base cobriu de uma vez todas as fases posteriores (`[CPL]`,
`[CARRINHO]`, `[DOWNSELL]` e `[REMARKETING]`, inclusive as que ainda iam subir) e
nunca tocou em `[CAPTACAO]`.

## 4.2 Público personalizado "desatualizado" mente o tamanho — *CONSISTENTE*

Achado levantado pelo Rodrigo, no mesmo lançamento. **Público que não é usado
num anúncio há 30 dias (ou foi criado há mais de 90 e nunca foi usado) para de
ser atualizado, e a Meta passa a reportar o tamanho como 1.000** — tanto em
`approximate_count` quanto em `delivery_estimate`. Não é o tamanho real, é
piso.

Como pegar: ler `operation_status` e `delivery_status` do público, nunca só a
contagem. Na tela, em Públicos, ler o status do público, não só o tamanho.

- `operation_status.description` = *"Esse público não foi usado em um anúncio
  por pelo menos 30 dias ou foi criado há mais de 90 dias e nunca foi usado.
  Por esse motivo, o seu público está desatualizado."*
- `delivery_status.description` = *"O público é muito pequeno para ser usado na
  criação da campanha."*

Medido no caso-base (a série prova o ponto sozinha — janela **menor** com **10x
mais** gente é logicamente impossível):

| Público de engajamento no IG | Tamanho reportado | Status |
|---|---:|---|
| 15 dias | ~10 a 12 mil | Normal |
| 30 dias | **1.000** | desatualizado |
| 60 dias | **1.000** | desatualizado |
| 90 dias | ~22 a 26 mil | Normal |
| 365 dias | ~60 a 71 mil | Normal |

**Consequência prática, e ela custa dinheiro:** decidir troca de público olhando
só a contagem leva a descartar público bom. No caso-base, a recomendação inicial
foi trocar o público de 30 dias pelo de 90 por causa do "1.000" — o Rodrigo
recusou apontando que o público estava fora de veiculação, e estava certo. O
público volta a atualizar assim que entra em entrega.

**Regra:** antes de descartar ou trocar público por tamanho, conferir
`operation_status` (ou o status na tela). Se estiver desatualizado, o número não
vale — e a forma de descobrir o tamanho real é colocá-lo em veiculação, não
estimar.

## 4.3 Advantage+ tem DOIS interruptores — desligar um não desliga — *VARIAÇÃO ISOLADA*

> 🔁🔁 **TERCEIRA VEZ, duas semanas depois da primeira — e a resposta deixou de
> ser texto.** Os 12 conjuntos da fase de carrinho nasceram com
> `custom_audience = 1`; 8 ativaram às 08:00 assim e vazaram até 08:2x. A
> checagem automática de antes de ativar rodou às 07:08 e **não acusou**:
> classificava a fase por substring do nome (`"CARRINHO"`) e a fase subiu com
> outra tag (`[CAR-*]`). O ativador novo conferia só o primeiro interruptor.
>
> O que mudou de verdade na casa (não é mais uma nota): o targeting de
> remarketing passou a sair de **uma fonte única** (o molde que monta, a
> validação e o resumo lido da plataforma moram no mesmo lugar); quem cria lê de
> volta e se recusa a seguir se a leitura não passar; quem ativa e a checagem de
> antes de ativar chamam a mesma validação; a fase passou a ser classificada pelo
> vocabulário `[PQ]`/`[PF]` (`sirius-scale/frameworks/trafego/nomenclatura.md`
> §2), nunca por substring; e a checagem tem teste que a vê passar num caso bom e
> falhar num ruim antes de alguém confiar nela. Esta seção fica como registro do
> erro; a trava mora no processo ("O que conferir antes de ativar", no fim desta
> seção).

> 🔁 **ACONTECEU DE NOVO uma semana depois, com esta seção já escrita.** Ao criar
> os 18 conjuntos da fase [CPL], o agente setou `advantage_audience = 0` e **não
> setou** `targeting_relaxation` — exatamente a metade que esta seção existe pra
> avisar. Quem pegou foi o Rodrigo, olhando o painel: o bloco Público mostrava
> "Advantage+ ativado" e a caixa **"Usar como sugestão" marcada**, enquanto o
> bloco Orçamento mostrava "Advantage+ desativado". Os dois rótulos na mesma
> tela, dizendo coisas opostas — é assim que o erro se parece.
>
> **A lição não é sobre a Meta, é sobre método:** o agente tinha lido este
> arquivo na mesma sessão (usou o §4.1 e o §4.5), e mesmo assim escreveu o
> `targeting` do zero em vez de partir de um checklist. Ler o framework
> **antes** não basta se a checagem não estiver no processo.
>
> ⚠️ **O NOME DO CAMPO É `targeting_relaxation_types`.** Não
> `targeting_relaxation`. Esse par de nomes errou **duas vezes no mesmo dia**,
> nas duas pontas:
>
> | Onde | O que aconteceu |
> |---|---|
> | **escrita** | o agente mandou `targeting_relaxation`; a Graph API respondeu **200 e descartou o campo em silêncio**. O relatório da correção disse "18 corrigidos · 0 falhas" tendo corrigido zero |
> | **leitura** | a checagem automática lia `targeting_relaxation`, que a API **nunca devolve**: vinha `None` sempre, e ela acusou 44 conjuntos "AUSENTE" com os dois interruptores comprovadamente em `0` |
>
> Corrigido nos dois lados. O jeito de não cair de novo é não confiar no nome de
> memória: pedir o `targeting` inteiro e **listar as chaves que voltaram** —
> `sorted(targeting.keys())` responde em uma linha qual dos dois existe.
>
> 📌 **E a lição de segunda ordem:** um verificador que lê o campo errado é pior
> que verificador nenhum. Ele grita em 100% dos casos, vira ruído, e checagem
> ruidosa é checagem que ninguém roda. **Checagem nova só conta depois de ver ela
> passar em caso bom E falhar em caso ruim** — aquela só tinha sido vista
> falhando.
>
> ✅ **O que ficou em vez de mais um aviso:** a regra da casa é transformar
> aprendizado em checagem que roda sozinha sempre que der, e "conjunto de
> remarketing com o segundo interruptor ligado" é exatamente o tipo de coisa que
> se calcula. Do lado de vocês, isso vira o pedido fixo ao Claude antes de ativar
> (com a conta conectada) ou a conferência da tela, conjunto por conjunto (no fim
> desta seção).


Achado levantado pelo Rodrigo olhando a interface, logo depois de a §4.1 declarar
o aquecimento "já desligado". Estava ligado.

**A mecânica.** O que a §1 chama de "controle x sugestão" é governado por
**dois campos independentes** da API, e zerar só o primeiro não faz nada:

| Campo | Efeito |
|---|---|
| `targeting_automation.advantage_audience` | o Advantage+ audience "de capa" |
| `targeting_relaxation_types.custom_audience` | **trata público personalizado como sugestão e entrega fora dele** |
| `targeting_relaxation_types.lookalike` | idem, pro lookalike |

Com `advantage_audience = 0` e `relaxation.custom_audience = 1`, a interface
mostra o selo **"Advantage+ ativado"** no card Público e a etiqueta **"Sua
sugestão"** ao lado de "Públicos personalizados". Esse par na tela é o sintoma
— e é mais confiável que ler um campo só na API.

**A prova de que não é detalhe cosmético** — conjunto de inscritos do lançamento,
2 dias no ar, público declarado de ~2,7 a 3,2 mil:

| | |
|---|---:|
| Alcance em 2 dias | **~23,5 mil pessoas** (~8× o público) |
| Frequência | 1,03 |
| CPM | ~um oitavo do CPM médio da conta |

Alcançar ~23,5 mil pessoas dentro de um público de ~3 mil é impossível. O CPM a
um oitavo do da conta diz onde a entrega foi parar: inventário barato e amplo. E
o alcance caiu quase exatamente na faixa (~23 a 27 mil) que o planejamento do
aquecimento tinha previsto "se incluíssemos os públicos de envolvimento" — a Meta
ampliou sozinha pro tamanho do público que a decisão tinha recusado, escolhendo
quem por conta própria.

**A regra:** ao desligar Advantage+ em fase posterior, zerar os **dois**.
Verificação que não mente: `alcance > tamanho do público` é entrega fora da
lista, ponto. Auditar por esse número, não pelo campo.

⚠️ Candidato a **CONSISTENTE** — é mecânica de plataforma, não julgamento, e a
impossibilidade aritmética prova sozinha. Fica ISOLADA até o Rodrigo decidir
subir.

A correção do caso-base passou a olhar os dois campos. A versão anterior da
conferência olhava só o primeiro, reportava "já OK", e por isso o achado passou.

### O que conferir antes de ativar (fase posterior, conjunto por conjunto)

O resumo que a pessoa dona da conta confere antes de ligar vira **uma linha por
conjunto**, lida da conta e não da intenção de quem montou:

`advantage_audience=0 · sugestao(custom=0, lookalike=0) · geo=['BR'] · N inclui / M exclui`

- **Na tela do Gerenciador:** card Público **sem** o selo "Advantage+ ativado";
  ao lado de "Públicos personalizados", **sem** a etiqueta "Sua sugestão" (caixa
  "Usar como sugestão" desmarcada, e o mesmo pro semelhante); localização certa;
  quantos públicos incluídos e quantos excluídos.
- **Pela API (conta conectada):** o Claude lê `targeting_automation` e
  `targeting_relaxation_types` de cada conjunto e devolve a linha acima. Problema
  em um conjunto barra o lote inteiro.
- **Classificar a fase pela tag de público** (`[PQ]` = público quente, onde os
  dois interruptores têm que estar em zero), nunca por pedaço do nome da fase:
  tag nova não pode cegar a conferência.
- **Depois de 1–2 dias no ar:** alcance ≤ tamanho do público. Se passou, está
  entregando fora da lista, diga o painel o que disser.
- Num conjunto de público interno há mais lugares do Advantage+ (posicionamento e
  melhorias do criativo): ver `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`,
  seção "Impulsionar post do Instagram por API, com o Advantage+ desligado nos
  quatro lugares".

## 4.4 Vídeo longo: 25% não vira público — use ThruPlay/15s — *VARIAÇÃO ISOLADA*

Levantado quando o Rodrigo perguntou se valia criar um público de video view 25%
das lives de aquecimento.

Medido no conjunto de aquecimento de um lançamento do caso-base, 2 dias, 10
anúncios:

| Marco | Eventos |
|---|---:|
| Plays | ~22,5 mil |
| **ThruPlay (15s)** | **~2,5 mil** |
| 25% | **20** |
| 50% | 12 |
| 75% | 4 |
| 100% | 2 |

**Por que 25% morre:** o marco é percentual, e as lives passam de uma hora.
25% de uma live de 1h são **~15 minutos assistidos**. Vinte pessoas fizeram
isso em dois dias — a projeção pro aquecimento inteiro fica em ~100–200,
contra o **piso de 1.000** da Meta pra público de engajamento. O público
nunca sairia do chão.

O histórico já dizia isso e ninguém tinha lido: o público de video view de 3
segundos das lives de um lançamento anterior, com janela de 365 dias, estava em
**1.000** (o piso) — aquelas lives não encheram um público nem no corte de **3
segundos**.

**A regra:** em vídeo longo (live, aula, CPL), público de engajamento se monta
por **marco de tempo** (ThruPlay/15s), nunca por percentual. Percentual só
serve em criativo curto, onde 25% são segundos. No caso-base, ThruPlay
projetava ~12 mil eventos ao longo do aquecimento — público utilizável, e com
sinal de qualidade melhor que a lista de leads (é comportamento, não cadastro).

⚠️ Duas ressalvas antes de usar como semente de lookalike (§4): (1) os ~2,5 mil
ThruPlays daquele momento vinham de entrega ampliada indevidamente (§4.3) — depois
da correção o volume cai e a qualidade sobe; (2) público de engajamento de vídeo
captura orgânico **e** pago, então o alcance orgânico das lives na página
entra junto, o que ajuda o volume.

## 4.5 Público de vídeo é lista CONGELADA de vídeos — criativo novo não entra sozinho — *VARIAÇÃO ISOLADA*

Levantado a pedido do Rodrigo, no mesmo lançamento.

**A mecânica.** Público de engajamento de vídeo na Meta **não** é "quem viu
vídeo da página". A regra é uma **lista explícita de `object_id` de vídeo**,
gravada no dia em que alguém montou o público na interface:

```
rule = [{"event_name": "video_view_15s", "object_id": <id do vídeo>}, ...]
```

Criativo que sobe depois **não entra**. O público não quebra nem avisa — ele
simplesmente para de crescer no ritmo da veiculação, e vira retrato do primeiro
lote de criativo. É o mesmo problema da lista de clientes (§3, item 1), que é
estática e não cresce sozinha, só que na camada de vídeo.

**A parte que a interface esconde, e que custa mais caro:** cada criativo vira
**mais de um `object_id`** — a Meta cria um objeto de vídeo por variação de
proporção/posicionamento. No caso-base, 32 dos 38 vídeos de captação eram 2 ids
para 16 criativos. Adicionar "o vídeo" na mão pela interface pega um id e deixa
o irmão de fora, então metade da audiência do criativo some sem ninguém ver.

**Medido no caso-base** — o público de view de 15s da captação (o nome terminava
em "180D"):

| | |
|---|---:|
| Vídeos em anúncio de captação | 38 |
| Deles, na regra do público | **6** |
| Ids na regra sem anúncio vivo | 41 de 47 |

Os 41 são objetos de vídeo dos anúncios do **primeiro lote**, todos
deletados/arquivados dois dias depois na troca de criativo. O público estava
rastreando o passado: 47 ids, e só 6 correspondiam ao que estava no ar. Tudo do
segundo lote em diante — a fila inteira de criativo que subiu depois — estava
fora.

⚠️ **O nome mente sobre a retenção.** O público se chamava "- 180D" e a API
devolvia `retention_days = 365`. Ler o campo (ou a retenção configurada, abrindo
o público na tela), nunca o nome.

**A regra:** todo criativo novo que sobe entra no público de vídeo no mesmo
passo em que sobe o anúncio — e entra com **todos** os `object_id` dele, não
com um. No caso-base isso virou passo automático, que só adiciona e nunca remove:
quem assistiu assistiu, e o evento continua valendo dentro da janela de retenção.
À mão, pela interface, esse passo não fecha (§4.7: a tela só oferece vídeo
publicado na Página). Sem a conta conectada ao Claude, registre a pendência em vez
de montar pela tela um público que parece o mesmo e não é.

**Formato do update, testado a seco** (público descartável criado, atualizado e
apagado antes de tocar no real): a Meta aceita a lista plana acima em
`api_update(params={"rule": json.dumps(...)})` e devolve exatamente o que
recebeu. O update **substitui a regra inteira** — por isso a união tem que ser
feita antes de mandar, nunca só o delta.

**No Google/YouTube a mecânica é OUTRA — e é por isso que ninguém percebe o
problema da Meta.** Lá a lista de "viu vídeo" pendura na **conta do YouTube
vinculada**, não numa lista de ids do gerenciador: uma lista de "viu vídeo de
anúncio" de 30 dias cresce sozinha conforme anúncio novo roda. Não existe passo
de manutenção equivalente. Duas ressalvas: (1) a API do Google **não expõe** a
regra dessas listas (`rule_based_user_list` volta só com `prepopulation_status`),
então conferir se a lista é do canal inteiro ou de vídeos escolhidos só dá na
interface; (2) por isso mesmo, "no Google não precisa" vale para a lista de
canal — lista montada com vídeos selecionados teria o mesmo problema da Meta.

## 4.6 O equivalente do Advantage+ no Google se chama outra coisa — e liga sozinho — *VARIAÇÃO ISOLADA*

*(Caso-base, auditado a pedido do Rodrigo. Um cliente, uma conta.)*

O Rodrigo pediu pra conferir se o Advantage+ estava desligado **nas duas
plataformas**, achando que estivesse. Resultado: certo na Meta, **errado no
Google**.

| plataforma | campo | esperado | achado |
|---|---|---|---|
| Meta | `targeting_automation.advantage_audience` | 0 | **0** ✅ |
| Meta | `targeting_optimization_types` (detailed, lookalike) | 0 | **0** ✅ |
| Google | `ad_group.optimized_targeting_enabled` | False | **True** ❌ |
| Google | `campaign.audience_setting.use_audience_grouped` | — | True |

**Por que passou despercebido por 10 dias:** o equivalente do Advantage+ no
Google **não se chama Advantage nada** — é "segmentação otimizada"
(`optimized_targeting_enabled`), e mora no **grupo de anúncio**, não na
campanha. Quem audita procurando "advantage" no Google não acha, e conclui que
está limpo.

Pior: a campanha tinha sido criada com a decisão explícita de **não** expandir
— estava escrita no registro de decisões da criação, decisão nº 2. A intenção
estava documentada, o objeto na plataforma dizia outra coisa, e nada acusou a
divergência. **Documentar a decisão não é o mesmo que verificar o objeto** — é a
mesma lição de auditar pelo efeito, não pelo campo (§4.3), por outro caminho.

**Regra prática:** em auditoria de expansão de público, conferir os **quatro**
campos da tabela acima, por nome, um a um. E em fase de **aquecimento**
desligar sempre: aquecimento busca **frequência na mesma audiência** (o mesmo
inscrito vendo várias peças), e expandir trabalha contra isso duas vezes —
gasta com quem não é do lançamento e dilui a frequência de quem é.

**O que conferir no Google Ads, à mão:** a segmentação otimizada desligada em
**cada grupo de anúncios** da fase de aquecimento, grupo por grupo (é no grupo,
não na campanha).

## 4.7 Público de vídeo aponta pra DARK POST — e por isso o painel mostra a lista vazia — *UNIVERSAL*

*(Levantado pelo Rodrigo olhando o painel: o público de view de 15s da captação
tinha ~50 a 59 mil pessoas, e a tela "Selecionar vídeos" mostrava **nenhum
vídeo**.)*

Não é bug e não é público quebrado. Os vídeos usados como criativo de anúncio
sobem como **dark post** — `published = False`. Conferido nos 65 IDs da regra:
todos válidos, todos acessíveis, **todos não publicados**.

E a tela **"Selecionar vídeos → Fonte: Página do Facebook"** lista só o que está
**publicado na Página**. Então:

| | |
|---|---|
| o que o público contém | 65 vídeos de anúncio (`published=False`) |
| o que a tela mostra | os vídeos publicados na Página |
| interseção | **zero** — daí a lista vazia |

📌 **E é assim que tem que ser.** Um público de video-view de captação existe pra
pegar quem assistiu **os anúncios**. Se ele apontasse pros vídeos publicados,
pegaria audiência orgânica — outra gente, e misturada.

⚠️ **Consequência prática:** criar esse tipo de público **pela interface** pega o
público errado, porque a interface só oferece o que está publicado. O caminho
certo é a API, com os `video_id` extraídos dos criativos dos anúncios.

⚠️ **Vídeo enviado pela API pra conta de anúncio não serve** (captação de uma
Black do caso-base, *VARIAÇÃO ISOLADA*):
- Os vídeos dessa captação subiram direto pra conta de anúncios
  (`create_ad_video`). Por isso o `video_id` do criativo é o do arquivo na conta
  de anúncio.
- A Meta recusou criar o público com ele: "(#2654) ... this video isn't
  associated with a Page".
- O que funcionou foi o vídeo do post escuro que a Meta cria na Página quando o
  anúncio vai pro ar: `creative.effective_object_story_id` → `attachments{target}`,
  lido com o token da Página.
- É um vídeo por anúncio, então o mesmo criativo em 3 conjuntos vira 3 ids, e a
  lista do público leva os 3. Na Black, foram 25.

**Como conferir, então:** pela API — número de `object_id` na `rule` e
`approximate_count`. Nunca pela tela de seleção de vídeos, que vai mentir por
omissão. Vale a mesma régua do §4.2: **o painel não é a fonte pra tamanho e
composição de público personalizado.**

## 4.8 Remarketing por MOMENTO compete consigo mesmo — o público é o mesmo — *VARIAÇÃO ISOLADA*

`VARIAÇÃO ISOLADA` — caso-base, medido num dia da semana de aulas, nas duas
plataformas.

O remarketing do lançamento foi desenhado em **7 momentos** (aula 1 "é hoje",
aula 1 "gravação", aula 2…, "todas liberadas"), cada um com criativo e janela
próprios. Só que os 7 apontam para **exatamente os mesmos públicos**:

| Conjunto | Públicos (idênticos em todos os 7 momentos) |
|---|---|
| `00 - [INSCRITOS]` | todos os leads do lançamento · visita à página das aulas · visita à página de obrigado |
| `01 - [ENVOLVIMENTO]` | envolvimento no FB 30D · engajamento no IG 30D · visita à página de captura · video view 75% |

**A consequência prática, que não é óbvia:** os momentos ativos ao mesmo tempo
disputam o mesmo inventário. Quem tem mais orçamento e mais tempo de janela
domina a entrega e **sufoca os outros**, mesmo com todos "ativos" e com verba
sobrando no papel. Medido num dia com 3 momentos no ar:

| Momento | Alcance | Frequência | Orçamento usado |
|---|---:|---:|---|
| Aula 1 (gravação) | ~10,5 mil | **2,56** | ~85% do orçado |
| Aula 2 (gravação) | ~2,7 mil | 1,26 | ~30% do orçado |
| Aula 3 (é hoje) | ~3,5 mil | 1,45 | ~30% na Meta |

**O erro de leitura que isso causa:** olhando só a aula 2, a conclusão fácil é
"o público é pequeno, não adianta pôr verba". Errado — o público dela é o mesmo
da aula 1, que alcançou ~10,5 mil. O que faltava era espaço, não gente. Foi o
Rodrigo que apontou primeiro, por ver anúncio da aula 1 ainda rodando.

📌 **A regra que fica:** em estrutura de remarketing por momento, **verba não se
aumenta isolada — se transfere.** Aumentar o momento novo sem cortar o velho não
muda quase nada, porque o velho continua ganhando o leilão. E a frequência que
importa não é a de cada campanha: é a **soma no público**, que nenhuma tela
mostra somada.

⚠️ **O que NÃO está medido:** se o desenho alternativo (1 campanha, criativo
trocando por data) entregaria melhor. Aqui só se mediu o efeito da competição,
não o contrafactual.

## 4.9 Novo, engajado ou cliente: a quebra `user_segment_key` — *UNIVERSAL (plataforma), medido uma vez (11/2026)*

Numa campanha `ADVANTAGE_PLUS_SALES` com o público aberto, a quebra `user_segment_key` dos insights separa a entrega
em gente nova, público engajado e cliente existente. É assim que se mede quanto da verba foi pra gente nova.

- **"Cliente existente" é configuração da conta**, não da plataforma (um público de compradores escolhido na conta).
  Ler na conta antes de interpretar.
- **A definição de "engajado" não sai por API:** os campos `audience_segments` e `engaged_audience` deram erro #100
  ("nonexisting field") e, depois, voltaram só com o id da conta.

## 4.10 O que um segundo nicho mostrou sobre aberto, lookalike e quente · *VARIAÇÃO ISOLADA (11/2026)*

Lançamento gratuito, Meta, retorno medido por venda casada com o lead no Dash.
1. **Com vários criativos na mesma campanha, quem escolhe a peça é a Meta, pelo lead mais barato.** Num aberto com
   Advantage+, a maior fatia da verba foi pro criativo de pior MQL; noutro, quase toda a verba foi pra um criativo só, e
   a escolha sai cedo e não julga a peça (o mesmo anúncio levou fatias muito diferentes em duas campanhas iguais). Leitura do
   Rodrigo: "o segredo maior da campanha Advantage é o criativo. E a gente otimizar baseado nas UTMs e no MQL". É por
   isso que a escada tem um criativo por campanha em todos os degraus (`lancamento-gratuito.md` §2.1).
2. **Lookalike de semente de qualidade (MQL ou compradores), com Advantage desligado, foi a melhor célula fria** em 2
   de 3 lançamentos. Primeira medição da célula de semelhantes.
3. **Conjunto quente com Advantage+ ligado vira amplo** (a lista de engajamento vira sugestão, §1), e partindo de uma
   lista quente grande foi a melhor célula de um lançamento. O aberto sem público, não. Na leitura, separar os dois.
4. **Lookalike com Advantage ligado × desligado — *PADRÃO INCONCLUSIVO*:** o desligado converteu mais, mas o N do ligado
   não fecha.
5. **Janela maior não deu público maior no Instagram** (fato de plataforma, medido uma vez): o "todos que interagiram"
   de uma janela mais longa saiu menor que o de uma mais curta. Antes de escolher a janela,
   conferir o tamanho de cada uma na conta; não supor que a mais longa é a maior.
## 5. Em aberto (no caso-base)

- **Google (Customer Match): tem preço medido.** No caso-base, sem a lista CRM,
  **o remarketing do Google alcançava ~33% da base** de leads. O resto fica
  inalcançável por mais dinheiro que se coloque, porque o pixel só conhece quem
  passou por ele. A referência de quanto uma lista CRM entregava na mesma conta:
  uma lista da base total, de tamanho parecido, chegava a ~69% de cobertura —
  **mais que o dobro do pixel sozinho**.
  📌 A leitura que importa: **isto não é otimização, é teto de alcance.** Subir
  a lista não custa nada e é a única coisa que move o teto. Ao planejar
  remarketing no Google, medir o tamanho da lista da fase ANTES de ratear verba
  (pela API, `user_list.size_for_display`; na tela, o tamanho da lista no
  gerenciador de públicos) — orçamento acima do que o público comporta não vira
  alcance, vira frequência em cima dos mesmos 33%.
  Quando for construir, validar a seco antes de escrever (`validate_only`, ver
  `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`); Customer Match
  tem requisito de elegibilidade de conta ainda não verificado.
- Se o Advantage+ realmente degrada MQL nesta conta — é o que a célula do
  item 3.2 vai responder.
- **Remedir o combo da antecipação** agora que o público de engajamento de 30
  dias voltou a reportar tamanho real (§4.1, atualização).
- **Criar o público ThruPlay das lives de aquecimento** (§4.4) e decidir se
  entra como semente de lookalike ou como público de antecipação/CPL.
- **§4.5:** decidir se os 14 criativos de aquecimento (7 de live e 7 de outro
  formato) entram no público de captação ou ganham público próprio, e se a
  sincronização vira rotina ou passo do fluxo de subir criativo.
- **§4.5, Google:** conferir na interface se a lista de view de vídeo de anúncio
  de 30 dias é do canal inteiro ou de vídeos escolhidos — a API não conta.
- **Auditar o resto da conta pelo teste da §4.3** (`alcance > público`): só o
  aquecimento foi conferido. `00 - PAGE VIEW CAPTURA + VIDEO 15` e
  `01 - MIX QUENTE`, na captação, também estavam com `relaxation.custom_audience
  = 1` — pausados no nível de campanha, então não urgente.

---

## 6. O que transfere e o que é do caso

**Transfere inteiro (é mecânica da Meta, não padrão de cliente):**

- **§1** — controle x sugestão, e o corolário: "lookalike/interesse com
  Advantage+ ligado" não é teste de público. Exclusão como único limite duro
  que sobrevive ao Advantage+ ligado, e por isso a alavanca mais barata.
- **§2** — os números oficiais da Meta (14,8% topo / 9,7% meio / 7,2% fundo,
  8% em lead form) são publicação dela, valem pra qualquer conta. Junto com a
  ressalva que importa: **a Meta mede CPA/CPL, não qualidade de lead.**
- **§4.1, o raciocínio** — Advantage+ ligado em captação, desligado em toda
  fase que mira quem já está dentro; no Google, `optimized_targeting_enabled`.
  E os dois corolários: dimensionar orçamento ao público, e "onde parar ao
  ampliar" (se a mensagem não faz sentido pro público novo, troque o criativo
  antes de ampliar).
- **A causa raiz do §4.1** — a Meta aplica o default **LIGADO** quando a criação
  não passa `targeting_automation`. Regra dura pra qualquer criação nova, em
  qualquer cliente: deixar `advantage_audience: 0` explícito em fase posterior
  (e conferir na tela). Não passar não é neutro.
- **§4.2 inteiro** — público sem uso há 30 dias reporta 1.000 (piso, não
  tamanho). Conferir `operation_status`/`delivery_status`, nunca só a contagem.
  A série 15D/30D/60D/90D prova por impossibilidade lógica.
- **§4.3 inteiro** — os dois interruptores (`targeting_automation
  .advantage_audience` **e** `targeting_relaxation_types.custom_audience` /
  `.lookalike`), o sintoma na tela ("Advantage+ ativado" + "Sua sugestão"), a
  verificação que não mente (**`alcance > tamanho do público` = entrega fora da
  lista**; auditar por efeito, não por campo) e a linha por conjunto de antes de
  ativar.
- **§4.4, a regra** — em vídeo longo (live, aula, CPL) o público de engajamento
  se monta por marco de tempo (ThruPlay/15s), nunca por percentual. É
  aritmética: 25% de 1h são 15 minutos assistidos.
- **§4.5 inteiro** — público de vídeo na Meta é lista congelada de `object_id`,
  criativo novo não entra sozinho, e cada criativo vira mais de um id (um por
  proporção). O update substitui a regra inteira, então a união se faz antes de
  mandar. E o contraste com o Google, onde a lista pendura no canal do YouTube
  e cresce sozinha — o que explica por que o buraco da Meta passa batido.
- **§4, o critério de semente** — a base toda serve pra exclusão, nunca como
  semente; semente sai do sinal de qualidade. E a privacidade: e-mail
  normalizado + SHA-256, nunca texto puro.

**Não transfere (números de uma conta, um lançamento):**

- Todos os tamanhos de público (a base de leads, a semente de pouco mais de mil,
  o alcance de ~8× o público, as faixas dos públicos de engajamento), o CPM da
  conta e os orçamentos por conjunto.
- A **decisão do §3** (qual célula testar no lançamento de referência) — é escolha
  de contexto: estrutura herdada, fila de criativo, verba daquele momento.
- O benchmark "contas de topo sobem 12–19 criativos/semana" é de mercado, não
  medido aqui — usar como referência, não como meta contratada.

**Nota de confiança:** o §4.3 está marcado ISOLADA mas é mecânica de plataforma
e se prova por aritmética — está declarado no próprio arquivo como candidato a
CONSISTENTE, aguardando decisão do Rodrigo. Não foi subido sem ele. Na prática,
ao aplicar em cliente novo, trate como mecânica: o risco de ignorar é entregar
pra frio pagando por isso.
