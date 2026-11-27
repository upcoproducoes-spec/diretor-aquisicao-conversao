# Framework — Criativos (por funil e fase)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** execução e voz (com dois blocos de mecânica de plataforma)
> **Base:** 1 cliente (o caso-base, um expert de educação) · vários lançamentos · documento vivo
> **Alcance:** NÃO TESTADO FORA. Este é o guarda-chuva de criativo e o arquivo
> mais impregnado da voz do expert do caso-base: **a fundação (0.1–0.9) transfere
> como princípio, o conteúdo não transfere nada.** A **0.10** (clickbait / Demand
> Gen) é exceção: é mecânica de plataforma e vale em qualquer cliente. Ver §4
> no fim.

Reverse-engineered a partir das peças de criativo produzidas nas conversas e nos arquivos de projeto do caso-base. Documento vivo: começa pela fundação (DNA + mapa de CTA) e é preenchido fase por fase, atualizado com o tempo.

## Como este doc é organizado

Hierarquia: **funil → fase dentro do funil → formato (vídeo / estático / carrossel)**.

Três funis:

- **Funil 1 — Lançamento gratuito** (o evento de aulas gratuitas / CPLs). Vende o programa principal. Promessa: a do programa principal.
- **Funil 2 — Lançamento pago** (o evento pago / LPSG). Vende o ingresso do evento pago. Promessa: própria do produto (definida depois, ver 0.3).
- **Funil 3 — VSL / Evergreen** (um livro de entrada). Adiado.

Fora dos três funis, a **Black da casa** (colheita de base) tem arquivo próprio pra
criativo de captação. A entrada é `sirius-scale/frameworks/copy/criativos-captacao-da-black.md`
(as regras de conteúdo e o índice), e cada peça tem arquivo próprio: roteiro de
vídeo, texto de anúncio, texto do estático, arte do estático e edição. O
processo da Black está em `sirius-scale/frameworks/lancamentos/black-da-casa.md`. Antecipação
e carrinho da Black ainda não têm framework de criativo da casa, **mas o método
tem**: criativo de carrinho da Black segue os mapas do método de Black Friday de um
programa externo, que estão em `sirius-scale/frameworks/lancamentos/black-friday.md`
(ordem do Rodrigo: "é importante que siga a metodologia da Black que eu enviei"). As
torres e a régua estão no §6 de lá. A copy de carrinho está no mapa de tráfego do
método (FASE 4: direto ao ponto, foco no vitalício, quebra de objeções, escassez). Os 10
melhores criativos de carrinho do método foram transcritos, com o tipo de cada um, numa
fonte bruta da casa (não faz parte deste kit). A primeira aplicação foi a v2 de um
carrinho de Black do caso-base, ainda sem resultado. A v1 foi escrita sem os mapas,
porque esta linha dizia só "não têm framework": quando a casa usa um método externo
numa fase, a linha que diz "não tem framework" aponta pro método.

Marcação de confiança, no título de cada seção:

- **PADRÃO CONSISTENTE** — aparece em 3+ unidades, de preferência em mais de uma fonte. É regra.
- **VARIAÇÃO ISOLADA** — aparece em 1 ou 2 unidades. Só se o contexto pedir.
- **PADRÃO INCONCLUSIVO** — tem sinal, mas a base não sustenta. É hipótese a testar.

Status de base por fase: **[FORTE]** · **[RESSALVA]** um lançamento · **[FRAGMENTO]** base fina · **[VERIFICAR]** cavar antes de cravar · **[REVISAR]** existe mas não validado.

---

## 0. DNA comum (vale pro doc inteiro)

### 0.1 Cabeçalho e formato de entrega — *PADRÃO CONSISTENTE (regra de produção do Rodrigo)*

Cada peça vem com **nome do criativo — headline** no topo. Abaixo, só a copy limpa que o expert lê. Sem rótulo de bloco ("hook", "CTA", "desenvolvimento"), sem duração sugerida, sem direção de cena. Motivo: o expert copia e cola no teleprompter, e qualquer coisa a mais atrapalha a leitura.

### 0.1.1 Cabeçalho de roteiro de fala (live, pitch, aula) — *PADRÃO CONSISTENTE (decisão do Rodrigo)*

> ⚠️ **Atualizado depois:** a forma completa do roteiro de fala (as versões de leitura e de operação, as notas em doc separado, as marcas `[SLIDE]`/`[TELA]` e o cabeçalho sem "Como ler") está em `sirius-scale/frameworks/copy/formatacao-de-roteiro.md`. Onde este item diverge daquele, vale aquele (§6 de lá).

Roteiro que o expert lê ao vivo (live de carrinho, pitch, aula com oferta) é diferente do criativo do 0.1: tem blocos, porque ele precisa saber quando passar o slide ou trocar de assunto. O cabeçalho é compacto: **quem lê é ele**, e tabela grande atrapalha (a v1 de um pitch de reabertura tinha uma tabela de 6 linhas com "o quê", "garantia" e "tom"; o Rodrigo pediu pra enxugar).

Formato, nesta ordem:

```
# <Peça> — <contexto> (vN)

**<Produto> · <Lançamento> · <Fase> · <Peça e pra quem>**

<Dia, data> · **<Fechamento/urgência real, se houver>** · <duração alvo e unidade: um bloco por slide / por dúvida>
Página: <link de destino> (<onde o link aparece: chat, grupo, QR>)
Preço: <só se a fala cita, com as parcelas exatas do checkout>

**Como ler:** <uma linha: o que é cada marcação e o que acontece antes e depois do roteiro>
```

- **Entra:** produto/lançamento/fase/peça (uma linha em negrito), data, fechamento, duração, link, preço (se citado), "como ler".
- **Não entra:** "o quê" (já está no título), garantia (está na fala), tom (é ele que lê), tabela.
- **Corpo:** blocos com título entre colchetes — `[SLIDE N — título]` quando há deck, `[BLOCO]` quando não há — e a fala limpa embaixo. Sem rótulo de hook/CTA e sem direção de cena (mesma regra do 0.1). Instrução pro expert que não é fala vai entre parênteses, marcada como instrução.
- **Notas pra quem aprova** (no caso-base, o Rodrigo: decisões, divergências, o que ficou fora e por quê, rastreio das fontes) ficam numa seção separada **no fim**, nunca no cabeçalho. *(Depois, viraram doc separado: `sirius-scale/frameworks/copy/formatacao-de-roteiro.md` §6.)*

Primeiro uso: um pitch de reabertura do caso-base (evidência no caso de origem).

### 0.2 Gancho nos 3 primeiros segundos — *PADRÃO CONSISTENTE (todos os criativos)*

A primeira fala prende antes do scroll. Em captação, fisga por dor ou promessa. Em remarketing, reengaja quem já conhece o expert.

### 0.3 A grande promessa entra uma vez por peça, e é a promessa do funil — *PADRÃO CONSISTENTE, com a distinção por funil que o Rodrigo cravou*

- **Funil 1 (gratuito):** a promessa é a do programa principal, porque esse funil existe pra vender ele. Aparece na captação e no carrinho. Formulação da casa no caso-base: o resultado que o público mais quer, num prazo, pelo mecanismo do método (o que é a promessa e como ela entra em cada etapa: `sirius-scale/frameworks/lancamentos/roma-e-promessa.md`).
- **Funil 2 (pago):** o ingresso/evento já é um produto próprio, então precisa de **promessa própria**. ✅ **Resolvido depois** (esta questão estava aberta quando o doc foi escrito): a promessa oficial do evento pago passou a existir, no molde [o jeito errado que a pessoa abandona] + [o resultado que ela passa a alcançar] + [o mecanismo do expert]. Ela foi registrada verbatim, com a quebra de linha pretendida, no arquivo do produto, seção "Promessa central" (`expert/produtos/<produto>.md`). Usar de lá, não reescrever.

Entra uma vez, onde encaixa natural. Repetir na mesma peça gasta.

### 0.4 A credencial que só o expert tem entra uma vez — *PADRÃO CONSISTENTE (guia de captação)*

É o maior diferencial do expert do caso-base e aparece pouco no orgânico. Uma menção por peça, onde cabe. O guia de captação do caso-base manda mencionar essa credencial justamente porque ela aparece pouco no conteúdo orgânico, e dá uma frase-modelo do tipo [o que todo professor do assunto faz] + [a credencial que nenhum concorrente tem]. Frases assim posicionam de um jeito que nenhum outro professor consegue.

### 0.5 Urgência só quando é real — *PADRÃO CONSISTENTE (guia de captação)*

Urgência ancora em fato: prazo, janela de inscrição, encerramento marcado. A distinção que vale: urgência de **prazo real** ("encerra hoje", "última chance", "garanta sua vaga" em carrinho aberto) a casa usa; escassez de **capacidade falsa** ("últimas vagas") não, porque não é íntegra, ainda mais em evento gratuito. As frases exatas que entram e saem vivem no framework de copy de cada peça, não aqui. No DNA fica só o princípio. Trecho real do guia de captação:

> Não usar linguagem de escassez falsa. "Últimas vagas" para um evento gratuito soa falso. Usar urgência temporal real.

### 0.6 Um CTA por peça, e o CTA é a próxima ação possível naquele ponto do funil — *PADRÃO CONSISTENTE (o eixo do doc)*

Cada criativo pede uma ação só, e essa ação é o que dá pra fazer naquele momento do funil. Antes da aula não dá pra assistir, então ativa lembrete. Na fase de carta não dá pra comprar, então lê a carta. No carrinho, matricula. O destino do clique muda junto. O mapa completo está em 0.9.

### 0.7 Voz do expert: professor que convida, não vendedor — *PADRÃO CONSISTENTE (guia de captação)*

Valida a dor antes de redirecionar, culpa o método nunca o aluno, fala direto. O guia de captação do caso-base, sem o nome do expert:

> Falar como professor, não como vendedor. O expert ensina e convida. Ele não "vende vagas": ele abre a porta.

> Culpar o método, nunca o aluno. O inimigo é o método ruim, o ensino falho. Nunca dizer ou insinuar que o aluno é o problema.

> Validar antes de redirecionar. Quando falar de dores, primeiro reconhecer o sentimento ("Eu sei como é") e só depois apresentar a solução.

### 0.7.1 Criativo não fala valor — *VARIAÇÃO ISOLADA · escopo: LANÇAMENTO GRATUITO (diretriz do Rodrigo num lançamento gratuito do caso-base · escopo delimitado no dia seguinte)*

> ⚠️ **O escopo desta diretriz é o Funil 1 (lançamento gratuito).** Ela nasceu num
> lançamento gratuito do caso-base e foi escrita como se fosse geral. No dia seguinte,
> o Rodrigo delimitou: *"sobre valor em criativo acredito que funciona mais para
> perpétuo, low ticket, ou ingresso de lançamento pago."* Ou seja: **o que separa não
> é o cliente, é o tipo de funil e de oferta.** Ver a contrapartida em 0.7.2.

Em lançamento gratuito, nenhum criativo cita preço, desconto em reais, número de
parcelas ou ancoragem de valor, nem na fase de carrinho, onde a tentação é maior. O
número mora no checkout e na página de vendas. Onde o preço seria o argumento, o
argumento vira a **condição** ([a melhor condição que a pessoa vai ver], [a forma de pagamento
que acabou de liberar]) ou o **mecanismo**.

Vale também pra objeção financeira: em vez de defender o preço, reposicionar o
que está sendo comparado. Formulação do Rodrigo, sobre o programa principal do
caso-base, em molde: [o produto não é da categoria com que ele está sendo comparado] +
[o nome da categoria maior] + [o que ela tem a mais: suporte, acompanhamento]. A comparação
deixa de ser curso x curso e passa a ser curso solto x programa acompanhado.

Nasce ISOLADA: é diretriz de cliente, de um lançamento, sem teste A/B contra
criativo com preço. Antes de virar regra geral, confirmar em outro lançamento **do mesmo
funil**. O que aconteceu num SaaS de outra empresa do Rodrigo, no dia seguinte, **não**
confirmou isso: delimitou o escopo. Ver 0.7.2 e a seção 4.

### 0.7.2 Onde o valor PODE entrar no criativo — *PADRÃO INCONCLUSIVO (crença declarada do Rodrigo, sem teste)*

Contrapartida da 0.7.1, na formulação dele:

> *"Sobre valor em criativo acredito que funciona mais para perpétuo, low ticket, ou ingresso
> de lançamento pago."*

| Contexto | Valor no criativo | Por quê (leitura, não teste) |
|---|---|---|
| **Lançamento gratuito** (Funil 1) | ❌ não | O criativo vende a inscrição, que é grátis. Preço ali antecipa uma objeção que ainda não existe |
| **Ingresso de lançamento pago** (Funil 2) | ✅ tende a funcionar | O ticket baixo é o argumento: esconder o número esconde a facilidade da entrada |
| **Low ticket** | ✅ tende a funcionar | Mesma lógica: o preço É a oferta |
| **Perpétuo / assinatura** | ✅ tende a funcionar | Compra sem evento, sem escassez de data: o número ajuda a qualificar quem clica |

⚠️ **INCONCLUSIVO de propósito.** É crença de especialista com 8 anos de operação, não
resultado medido: **nenhum dos quatro contextos teve teste A/B com e sem preço**. Vale como
hipótese de partida, e como aviso de que aplicar a 0.7.1 fora do lançamento gratuito é
extrapolação.

**Contraexemplo dentro da própria casa:** num SaaS perpétuo de outra empresa do Rodrigo
(que pela tabela acima seria "tende a funcionar"), o Rodrigo mandou **tirar** o preço dos 10
criativos daquela leva. Ele disse *"vamos tirar preço por enquanto"*: decisão tática desta
leva, não regra. Registrado pra ninguém ler a tabela como automatismo.

**Segundo contraexemplo (downsell de um lançamento gratuito do caso-base, remarketing
estático):** o curso do downsell é produto pago avulso de ticket baixo, perto de "low
ticket" na tabela, e o Rodrigo mandou tirar o preço dos três anúncios: *"Não precisa falar
preço no anúncio."* No lugar, ele sugeriu um valor de desconto em reais ou "desconto
especial". **Desconto só entra com preço de referência que foi cobrado de verdade:** na
Hotmart, os 28 pedidos do curso em 12 meses saíram todos pelo preço menor, nenhum pelo preço
"cheio" que o desconto usaria de referência, então o anúncio ficou sem preço e sem desconto
até ele decidir. Antes de escrever "X de desconto", conferir o histórico de preço na Hotmart
(o histórico de vendas por produto, `/sales/history`): desconto sobre preço que nunca existiu
é o mesmo erro da escassez falsa (§0.5).

### 0.7.3 Número que a câmera vai mostrar sai da TELA, não de arquivo — *VARIAÇÃO ISOLADA (um SaaS de outra empresa do Rodrigo, custou duas regravações)*

Quando o criativo é gravado **em cima de uma interface** (painel, dashboard, relatório),
todo número falado sai da **tela no momento da produção**. Não de PDF exportado, não de
planilha, e não de cruzamento calculado por fora.

**O que aconteceu (um criativo de aquisição gravado em cima de um painel de resultados):**

1. A conversão por resposta de pesquisa foi calculada direto dos CSVs, e o roteiro saiu com
   **5,99%**. A tela mostrava **5,06%**. Quem gravava percebeu e se corrigiu ao vivo, e a
   edição cortou a correção certa, mantendo o número errado. Causa: o painel aplica dois
   filtros que o cruzamento ignorava (**só vendas do produto principal** e **dedup de
   respostas por e-mail**). Com os dois, o cálculo bate com 2–4 pessoas de diferença: o
   método estava certo, faltavam os filtros. **Mesmo batendo, na peça vai o da tela.**
2. Pior: o **PDF de debriefing arquivado envelheceu**. Dizia ROAS **7,41**; a tela, quatro
   meses depois, dizia **5,47**, porque a plataforma passou a somar no gasto um imposto de
   12,15% (valor da época, conferir). PDF é foto de um instante; o painel recalcula.

**Por que é regra e não preferência:** a peça é gravada em cima da tela. Fala e imagem estão no
mesmo quadro. Se divergirem, o espectador vê a contradição, e num criativo cujo tema é *parar
de decidir no achismo* isso destrói a peça inteira.

**Como aplicar:**
- Antes de escrever número em roteiro, pedir o print da tela ou abrir o painel.
- Sem conferir, escrever marcador (`[ROAS — CONFERIR NA TELA]`) e entregar assim. Não estimar.
- **Não afirmar direção** ("caiu um pouco", "voltou a subir") sobre números não conferidos:
  direção é afirmação sobre dois números, e erra em dobro.
- Quando duas linhas da tela têm valores próximos, **falar o rótulo exato da linha**, não
  "quem já comprou". Senão o espectador lê o número da linha vizinha.
- Cruzamento próprio serve pra **entender o padrão e escolher o ângulo**, nunca pra virar o
  número falado.

Alcance: nasceu num SaaS, mas o mecanismo (fala x interface no mesmo quadro) vale pra qualquer
cliente que grave demo de produto, prova em VSL ou criativo com painel na tela. (Evidência no
caso de origem.)

### 0.7.4 Depoimento em peça estática só com print real — *VARIAÇÃO ISOLADA (decisão do Rodrigo, downsell de um lançamento gratuito do caso-base)*

Na arte estática (anúncio, banner, story), depoimento só entra como **print real**: captura de
mensagem, comentário ou avaliação que existe. **Cartão de citação** (a frase do aluno entre
aspas, com nome, montada em design) está vetado. Palavras dele, vendo os cartões de duas alunas
nas artes do remarketing do downsell: *"texto em aspas não parece passar muita
credibilidade"*.

- Sem print real, a arte fica sem depoimento. Simular print continua proibido (regra
  anti-alucinação vale pra imagem).
- Frase que liga vários prints só afirma o que todos eles dizem. No caso medido, a frase que juntava os prints
  por um método valia pra metade deles; os outros nem citavam método. Saiu uma frase no molde "Em comum: <o que todos
  os prints de fato dizem>". VARIAÇÃO ISOLADA.
- Nome de aluno pode (ele confirmou no mesmo dia).
- No **texto** do anúncio, a fala entre aspas ficou (foi aprovada antes). Se a regra vale pro
  texto também está em aberto: perguntar antes de assumir.
- Número de depoimento só entra se for do mesmo recorte. O antes e depois de uma aluna juntava
  duas notas de provas diferentes (como no deck da live) e saiu a pedido dele.

Nasce ISOLADA: é uma leva, um cliente. Vira regra quando se repetir em outra peça ou cliente.

### 0.7.5 A promessa central não carrega a ressalva — *VARIAÇÃO ISOLADA (decisão do Rodrigo, Black do caso-base)*

Nas peças que saem antes da oferta (roteiro, anúncio, página de captura, e-mail e WhatsApp de
lista), a promessa vai inteira, sem a palavra que lembra o limite dela. Na Black do caso-base a
promessa citava o formato das aulas. O Rodrigo tirou essa palavra: *"não precisa a gente falar a
palavra videoaulas. Para não gerar objeção"*. Ficou [a promessa só com a vantagem de acesso]. A
ressalva continua verdadeira e continua escrita, só que no FAQ da página de vendas
e na live, onde quem pergunta já está decidindo. O mesmo vale pra prazo de produção (a data em
que o expert termina de gravar): ele aparece na oferta, não na captação.

- Não é licença pra prometer mais do que existe. O que tem prazo (suporte, ferramenta,
  simulado) continua sem a palavra "pra sempre" perto, e a peça não diz "tudo é vitalício".
- Antes de escrever, procure no briefing a palavra que o cliente vetou. Peça nova com a palavra
  antiga é a forma mais comum de ela voltar: no dia seguinte à regra ainda havia 65 ocorrências
  em seis peças escritas antes dela.

Nasce ISOLADA: um lançamento, um cliente.

### 0.7.6 A página do produto que aparece na arte sai do arquivo à venda, na hora de montar — *VARIAÇÃO ISOLADA (um produto de entrada do caso-base)*

Mesmo mecanismo do §0.7.3, aplicado a imagem. Quando a arte mostra o material por dentro (página na mão, na tela do celular, atrás da capa), a página é renderizada do PDF que o comprador recebe **no momento de montar a peça**. Não sai de mockup salvo antes.

**O que aconteceu:** um estático (v4) mostrava a p. 3 de um guia com o cabeçalho da assinatura antiga do expert. No mesmo dia o expert escolheu outra assinatura, e o PDF mudou. Nove dias depois os mockups das capas foram refeitos, mas essa página veio de uma imagem de mockup salva antes da troca, e passou. A peça subiu assim na v4, pausada, e foi arquivada sem rodar. Quase subiu de novo na v5, com a logo nova. Achado na revisão, dois dias depois; a página foi trocada pela p. 3 do PDF à venda. A função de montagem foi conferida antes: com a página antiga, ela reproduz a foto antiga pixel a pixel. Então a única diferença da peça nova é a página (1,27% dos pixels, todos dentro do papel).

**Como aplicar:**
- Arte que mostra página busca a página no PDF de entrega (o que o comprador recebe), nunca na pasta de mockup.
- Mudou nome, capa ou texto do PDF à venda: procure as artes que mostram página dele e refaça junto. Vale o mesmo raciocínio do "mudou o preço, propaga".

⚠️ **Frágil, e é a 2ª vez do mesmo erro.** Antes disso, os mockups das páginas de venda tinham saído com a assinatura antiga, e nasceu na casa uma checagem que compara a capa do mockup com o PDF de proposta. Só que ela confere só a capa; a página interna que entra em arte segue sem checagem. O portão do `designer` confere o texto da arte, não o conteúdo da imagem embutida. Jeito barato de virar checagem: avisar quando a imagem de mockup é mais velha que o PDF à venda. Regra da casa pra esse tipo de lição: se dá pra virar checagem que roda sozinha, vira; se não dá, é frágil, e isso se diz na entrega.

Nasce ISOLADA: uma peça, um cliente.

### 0.7.7 Estático montado em HTML: armadilhas de render

Moram em `sirius-scale/frameworks/design/estatico-anuncio-html.md`: altura da logo por proporção, página atrás da capa, seta branca no papel e o Chrome quebrando verbo+"-se" no hífen.

### 0.8 Formato é pra testar, não pra cravar — *PADRÃO INCONCLUSIVO (diretriz do Rodrigo, sem teste rodado)*

Vídeo, estático e carrossel. Tendência observada no framework de estático (`sirius-scale/frameworks/copy/criativos-venda-ingresso.md`): emocional puxa mais pro vídeo, direto/informativo puxa pro estático. Mas é tendência, não lei: um carrossel bem construído pode segurar emoção, e a gente ainda não testou carrossel. Regra prática: testar formato por ângulo, não assumir.

**Antes de recomendar formato, confira como a Meta monta** (`sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`, índice RECEITA). Vale pra várias imagens num anúncio, carrossel e imagem por posicionamento. O `DEGREES_OF_FREEDOM` aceita 1 imagem por criativo; N imagens viram anúncios irmãos no mesmo conjunto; carrossel é `child_attachments` com 1 texto. Sem conferir, a decisão sai marcada `[CONFERIR NA PLATAFORMA]`, como o marcador do §0.7.3. *Nasceu quando a copy v5 de um produto de entrada propôs "as 3 imagens num anúncio só", e a recomendação foi pro Rodrigo sem esse cruzamento. O fato já estava escrito havia semanas. É frágil: depende de alguém abrir o arquivo.*

### 0.9 Mapa mestre de CTA por funil e fase — *PADRÃO CONSISTENTE dentro dos lançamentos observados; INCONCLUSIVO fora deles*

**Funil 1 — Lançamento gratuito (promessa: a do programa principal)**

| Fase | Objetivo | CTA falado | Destino do clique |
|------|----------|------------|-------------------|
| Captação | inscrição grátis | pago: [toque no botão do anúncio] + [deixa os dados] + [entra no grupo] / orgânico: [comenta a palavra] + [recebe o link no direct] | página de inscrição → grupo WhatsApp |
| Aquecimento | levar pra live de aquecimento | [entra na live agora] ou [vê a lista das lives] | a live, no YouTube ou no IG, ou a página que reúne as lives |
| Remarketing evento, antes da aula | ativar lembrete | [toque no botão do anúncio] + [ativa o lembrete] | transmissão ao vivo no YouTube |
| Remarketing evento, depois da aula | assistir gravação | [toque no botão do anúncio] + [assiste à gravação] | gravação no blog de lançamento |
| Remarketing evento, revisão geral + sorteio | ir pra live final | [toque no botão do anúncio] + [ativa o lembrete] | live de revisão geral (regras do sorteio já ditas nos CPLs) |
| Pré-carrinho / carta (sáb e dom, antes de abrir na segunda) | ler a carta | [toque no botão do anúncio] + [lê a carta] | página da carta → grupo VIP (não matrícula) |
| Carrinho aberto | matrícula | [toque no botão do anúncio] + [faz a matrícula agora] | checkout |
| Carrinho fechando | matrícula com urgência real | [faz a matrícula] + [o prazo verdadeiro] | checkout |

**Funil 2 — Lançamento pago (promessa: própria, ver 0.3)**

| Fase | Objetivo | CTA falado | Destino do clique |
|------|----------|------------|-------------------|
| Venda de ingresso | comprar o ingresso do evento pago | pago: [toque no botão do anúncio] → página / orgânico: [comenta a palavra] | página de venda do ingresso |

Sem remarketing e sem carrinho no Funil 2. O pós-compra é API oficial de WhatsApp + grupo, que vive no framework de WhatsApp (`sirius-scale/frameworks/copy/disparo-whatsapp.md`).

⚠️ **Nota — "sem carrinho" precisa de nuance.** O cliente
confirmou que **a venda do ingresso encerra toda semana num horário fixo** (no
caso-base, domingo às 23h59), véspera do início das aulas. Não é carrinho no sentido
clássico (não tem abertura/fechamento de turma com semanas de intervalo), mas é um
**corte de prazo real e semanal**, o que habilita copy de urgência legítima, sem
escassez fabricada. Já existe peça produzida em cima disso (evidência no caso de
origem). Ou seja: o Funil 2 tem sim uma fase de fechamento recorrente, ela só não se
parece com o carrinho do Funil 1. Ver `sirius-scale/frameworks/lancamentos/lpsg.md` pra
mecânica completa (3 turmas em paralelo, ciclo semanal).

**Funil 3 — VSL / Evergreen:** adiado.

---

### 0.10 Curiosity gap em anúncio de plataforma é CLICKBAIT e limita a entrega — *VARIAÇÃO ISOLADA (Google Ads, lançamento gratuito do caso-base)*

O Google reprovou um anúncio de depoimento (a peça de prova 2 da campanha) com
`policy_topic: CLICKBAIT`, tipo `PROHIBITED`, e devolveu o anúncio como
`APPROVED_LIMITED`, ou seja, **rodando com entrega restrita**, sem erro visível e sem
avisar ninguém. O texto que causou isso, em molde:

> ❌ [há quanto tempo a pessoa tentava] + [promete contar o que mudou, sem contar].
> ❌ [há quanto tempo a pessoa tentava] + [aí veio o método], sem dizer o resultado.

Os dois prometem uma revelação que só o clique entrega. A correção mantém o
mesmo ângulo, mas diz o que aconteceu:

> ✅ [o que a pessoa mudou] + [o resultado a que ela chegou].
> ✅ [o resultado] + [depois de quanto tempo tentando].

**Regra que fica, para depoimento:** dizer O QUE a pessoa fez e QUAL foi o
resultado. Nunca insinuar que existe algo a ser descoberto clicando.

⚠️ **O sintoma é silencioso.** `APPROVED_LIMITED` não aparece como erro em
lugar nenhum: o anúncio sobe, fica ativo e simplesmente entrega menos.
Conferir `policy_summary.approval_status` algumas horas depois de subir
criativo novo; `UNKNOWN` só quer dizer que a revisão ainda está rodando.

Correção sem recriar (preserva o ID e o histórico no painel de resultados): editar o
texto do anúncio no lugar, pela API ou pela interface. O que é editável in-place está em
`sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §5, e a escrita segue
`sirius-scale/REGRAS.md` §6.

#### Reincidência dois dias depois — e o mecanismo por trás

A peça de prova 6 caiu no MESMO `policy_topic: CLICKBAIT / PROHIBITED`, dois dias
depois da peça 2. Das 12 peças da campanha de aquecimento, foi a única limitada, e a
única escrita direto na conversa, sem passar pelo agente `copy` (`sirius-scale/REGRAS.md`
§3). A linha culpada, em molde:

> ❌ [a crença que a pessoa tinha], sem o desfecho.
> ✅ [a crença que a pessoa tinha] + [o resultado a que ela chegou].

**O mecanismo (é isto que explica os dois casos):** no Demand Gen o Google
serve **cada asset sozinho**: ele monta combinações, não exibe a peça inteira.
Então não basta a peça resolver a promessa em algum lugar: **cada headline e
cada descrição precisa se resolver sozinha**. É por isso que a peça 6 parecia ok
lida de cima a baixo (a long headline dizia o desfecho) e ainda assim
voltou limitada: a headline sozinha na tela enunciava a crença e escondia o
desfecho.

Regra operacional: leia cada linha **isolada**, como se fosse a única coisa que
a pessoa vai ver. Se sozinha ela abre um loop que só o clique fecha, é
clickbait, mesmo que outra linha da peça já entregue a resposta.

#### `approval_status` é status, não motivo — confira o motivo antes de reescrever

Erro de método cometido na casa: a peça 6 foi diagnosticada como clickbait
**por semelhança com a peça 2**, sem verificar, e quase foi reescrita perseguindo o
alvo errado. O agente `copy` barrou e exigiu a confirmação. O motivo real só
aparece aqui:

```sql
SELECT ad_group_ad.policy_summary.policy_topic_entries
FROM ad_group_ad WHERE ...
```

No caso, confirmou CLICKBAIT. Mas se tivesse voltado política de **publicidade
personalizada**, o alvo seria a menção de **idade**, não o suspense, e a copy
nova, que apoia o ângulo justamente na idade da aluna, teria **piorado** a
restrição. Mesmo sintoma, correções opostas.

📌 Isto é a regra 1 de `sirius-scale/frameworks/trafego/_metodologia.md` ("o nome nunca diz
o que está sendo medido") aplicada a política de anúncio: o status diz que há um
problema, não qual é.

*(As duas entradas acima seguem VARIAÇÃO ISOLADA: os dois casos vieram do
mesmo cliente e do mesmo lançamento. Repetição dentro do mesmo
lançamento não promove a CONSISTENTE: falta ver noutro cliente.)*

#### ⚠️ Corrigir o texto NÃO destravou a limitação — VARIAÇÃO ISOLADA

*(A ressalva que ficou aberta aqui foi respondida dois dias depois, e a resposta é
negativa. Dado nas medições do aquecimento do caso-base: evidência no caso de origem.)*

A copy da peça 6 foi reescrita e aplicada in-place. Dois dias depois o anúncio
seguia `APPROVED_LIMITED` por CLICKBAIT/PROHIBITED, entregando restrito a um
**custo por view 2,4× o do melhor anúncio da campanha**. Mesmo caso num anúncio de
live que nunca foi editado.

**Duas hipóteses, e o dado disponível NÃO separa as duas:**

1. o texto novo ainda é clickbait pro Google; ou
2. editar in-place **não dispara nova revisão**: a limitação gruda no ID do
   anúncio, e nenhuma reescrita a tira.

⚠️ **`review_status` não serve pra desempatar.** No mesmo dia os **16** anúncios da
campanha voltaram `REVIEWED`, incluindo dois criados naquele dia. É estado
terminal de tudo, não prova de que a revisão rodou sobre o texto novo.

**O que o dado sustenta, e é o mais útil daqui:** peça **criada** com copy do
agente `copy` volta aprovada; peça **corrigida** continuou limitada. Placar
daquele dia: cinco peças criadas e `APPROVED` (uma delas inclusive com a linha que o
próprio agente marcou como de maior risco residual); a única `APPROVED_LIMITED`
entre as editadas/antigas é a peça 6.

**Consequência prática, até alguém separar as hipóteses:** quando uma peça
voltar `APPROVED_LIMITED`, **não conte com a edição de texto pra resolver**.
Corrigir o texto continua certo (a peça errada não deve ficar no ar do jeito
que está), mas trate a limitação como possivelmente permanente naquele ID e
decida se vale recriar, o que custa o histórico no painel de resultados, exatamente o
que a correção in-place existe pra preservar.

**Como fechar a dúvida** (não feito ainda, custa uma peça): recriar a peça 6 com o
texto já corrigido, sob nome novo, e comparar o `approval_status` das duas.
Se a nova passar, a hipótese 2 está provada e a receita de "corrigir sem
recriar" ganha uma ressalva pesada, que vale registrar também em
`sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §5, na tabela de editável
in-place.

**Terceiro dado, no mesmo dia, e ele pesa contra a hipótese 2.** Um anúncio de vídeo de
outra campanha estava `APPROVED_LIMITED` / CLICKBAIT de manhã. As
**15 linhas** (5 headlines, 5 long, 5 descriptions) foram reescritas pelo agente
`copy` pela regra "cada linha sozinha" e aplicadas **in-place** uns 45 minutos depois,
ID preservado. Uns 50 minutos depois disso o anúncio lia **`APPROVED`**. Ou seja: edição
in-place **disparou nova revisão e destravou**. A diferença pra peça 6 que o dado
permite ver: na peça 6 a correção foi de **uma linha** (a suspeita), no outro anúncio foi o
conjunto inteiro. Leitura mais provável agora: hipótese 1 (na peça 6 sobrou linha que,
lida isolada, ainda abre loop), não hipótese 2. Ainda não fecha (N=2, direções
opostas), mas a "consequência prática" acima ganha nuance: **reescreva o
conjunto inteiro, não só a linha que parece culpada**, e só depois de umas
horas decida se recria. Recriar continua sendo o último recurso.

📌 **E não adianta pedir à API qual linha foi:**
`ad_group_ad_asset_view.policy_summary.*` é `UNRECOGNIZED_FIELD` na v25 da API (versão da
época, conferir na atual): a política vem só no anúncio inteiro
(`ad_group_ad.policy_summary.policy_topic_entries`, sem `evidences`). Achar a linha
culpada é leitura humana, uma linha por vez, pela regra desta seção. Por isso
reescrever o conjunto sai mais barato que adivinhar a linha.

### 0.11 Pesquisa de estático na Biblioteca de Anúncios: tempo no ar como sinal — *processo TESTADO EM 2 EMPRESAS; valor preditivo PADRÃO INCONCLUSIVO*

Quando o estático é reprovado ou não há referência, olhe o que dura no ar no nicho antes de desenhar.
- **Por que tempo no ar:** a Biblioteca não tem API nem gasto pra anúncio comum no Brasil (fato da plataforma na época). Ela é lida pela tela (páginas de concorrente e buscas por termo, só anúncios ativos). Tempo no ar (hoje menos o início de veiculação) é o único sinal de que o anúncio se paga.
- **O que classificar:** os de 90+ dias, por gancho, formato, logo, rosto, preço na arte, texto na arte, CTA, consciência e lead. Toda frase do resumo tem que bater com uma contagem feita sobre a coleta, nunca com impressão.
- **Limites, ditos na entrega:** ativo não é lucrativo; poucos anunciantes dominam os veteranos (num dos usos, 61 de 77 vinham de 4); vídeo só se lê pelo 1º quadro; a nota de encaixe é julgamento.
- **Usos:** dois, em dois negócios (266 e 956 anúncios coletados). Nos dois, o gatilho foi um estático reprovado. Nenhum criativo derivado rodou ainda: o valor preditivo de "veterano = paga" é hipótese.

## Headline de peça que promove AULA: a fonte é o título oficial

*(VARIAÇÃO ISOLADA — lançamento gratuito do caso-base)*

Quando a peça leva pra uma **aula de evento** (CPL, live, aula aberta), a
headline é o **título oficial daquela aula, condensado pra caber**, não um
ângulo novo tirado do miolo do conteúdo.

O Rodrigo explicitou o critério assim: *"mais relacionada ao título da aula, acho
melhor ser perto do que é o título"*. E a evidência mais forte não é a frase: é
que ele **escreveu a headline da peça 1 com as próprias mãos**, e ela é
literalmente o título do CPL1 no briefing, cortado. Em molde (o título real fica com o caso):

- Título oficial: *"[Número] [erros] que [verbo] seu [resultado] em [assunto]"*
- Headline dele: `❌ *[Número] [erros]* que [VERBO EM CAIXA ALTA]` / `seu [resultado] em [assunto]`

O que a headline fez com o título: manteve as palavras dele, cortou o fim, pôs o ❌ na frente, o itálico no número com o substantivo e a caixa alta no verbo.

**Por que funciona:** o lead se inscreveu vendo esses títulos. A headline devolve
a ele o que ele reconhece, em vez de apresentar um assunto novo.

Isso não substitui a regra geral (headline sai do doc de copy aprovado): é o
caso particular de peça que promove aula, onde a fonte do texto é o briefing.

Vale pro texto que vai **dentro do anúncio** (headline, descrição), não pro
roteiro do vídeo: no vídeo o gancho continua valendo (0.2).


## 1. Funil 1 — Lançamento gratuito

_(a preencher: 1.1 Captação, 1.2 Aquecimento, 1.3 Remarketing de evento, 1.4 Pré-carrinho/carta, 1.5 Remarketing de carrinho)_

## 2. Funil 2 — Lançamento pago

**Estático de venda de ingresso já está detalhado em arquivo próprio:**
`sirius-scale/frameworks/copy/criativos-venda-ingresso.md` — 9 famílias de headline, os
2 modos (DOR e INFORMATIVO), etapas do layout e regras transversais, tudo
com marcação de confiança. Esse arquivo é o aprofundamento desta seção pro
formato estático; ler os dois juntos, não um no lugar do outro.

Modelo de funil (cadência semanal, 3 turmas em paralelo, corte semanal no domingo
à noite): `sirius-scale/frameworks/lancamentos/lpsg.md`.

_(a preencher: vídeo e carrossel de venda de ingresso. A questão aberta da
promessa própria foi resolvida: ver 0.3.)_

## 3. Funil 3 — VSL / Evergreen

_(adiado; o processo de VSL está em `sirius-scale/frameworks/copy/producao-de-vsl.md`)_

---

## Pedir criativo novo: o pedido sai da análise, não do gosto — *VARIAÇÃO ISOLADA (11/2026)*

Quando o criativo é gravado por outra pessoa (o expert, um editor, o time), o pedido de peça nova vai com o dado:
1. **A régua é quem o criativo traz,** medido pela pesquisa filtrada por anúncio (`utm_term`). Pede-se mais do ângulo que
   traz o comprador e se para o que traz quem não compra, com o número de cada um no pedido.
2. **O criativo vencedor sem nome de ângulo precisa ser assistido antes de virar pedido.** Assistir, anotar em 3 linhas o
   gancho, a promessa e a prova, e variar uma coisa por vez.
3. **Nome do anúncio com o ângulo, não só número** (ex.: `ADV-<ANGULO>_<VARIACAO>`), senão o próximo debriefing não lê o
   ângulo.
4. **Um texto por ângulo, não um texto pra todos.** Com o mesmo texto em todos os anúncios, o efeito dele não dá pra
   medir. E confira se o texto não chama justamente quem compra menos.
5. **O pedido cobre também a chamada e a narrativa** quando o dado aponta perfil que compra menos atraído por elas.
## 4. O que transfere e o que é do caso

**Transfere como mecânica de plataforma (qualquer cliente, qualquer empresa):**

- **Anúncio adaptado pra outro mercado/versão de produto nunca é cópia
  automática da copy original.** Conferir contra a **oferta real** daquele mercado antes
  de publicar, não contra a versão original de onde ele foi copiado. *(Achado real,
  num cliente de outra empresa do Rodrigo: o anúncio da versão do segundo mercado
  prometia material físico de apoio entregue em casa pra um produto que nesse mercado é 100%
  digital, arquivo + PDF. A copy foi adaptada da versão do mercado original, que é
  física, sem reconferir contra a entrega real do mercado de destino. Causa provável do
  reembolso subindo nesse mercado, com verbatim de comprador confirmando expectativa
  frustrada.)* VARIAÇÃO ISOLADA — NÃO TESTADO FORA (1 cliente, 1 mercado).
- **No Demand Gen o Google serve cada asset sozinho.** Por isso cada headline e
  cada descrição precisa se resolver sozinha: se a linha isolada abre um loop
  que só o clique fecha, é clickbait, mesmo que outra linha da peça entregue a
  resposta. Regra operacional: ler cada linha como se fosse a única na tela.
- **`APPROVED_LIMITED` é sintoma silencioso.** O anúncio sobe, fica ativo e
  entrega menos, sem erro visível. Conferir `policy_summary.approval_status`
  algumas horas depois de subir criativo.
- **`approval_status` é status, não motivo.** Ler
  `policy_summary.policy_topic_entries` antes de reescrever: mesmo sintoma
  pode ter correções opostas (clickbait pede desfecho explícito; publicidade
  personalizada pediria tirar a menção de idade, e a mesma correção pioraria).
- **Para depoimento:** dizer o que a pessoa fez e qual foi o resultado, nunca
  insinuar revelação atrás do clique.
- Correção de copy de anúncio **sem recriar**, pra preservar ID e histórico no
  painel de resultados.

**Transfere como princípio de copy (adaptar à voz do novo expert):**

- **0.6, o eixo do documento:** um CTA por peça, e o CTA é a **próxima ação
  possível naquele ponto do funil**, com o destino do clique mudando junto.
  É o item mais reaproveitável daqui; a *estrutura* do mapa de CTA transfere,
  as células não.
- **0.2** — gancho nos 3 primeiros segundos, fisgando por dor/promessa em
  captação e reengajando em remarketing.
- **0.3** — a grande promessa entra **uma vez** por peça, e é a promessa **do
  funil**; funil que vende produto próprio precisa de promessa própria.
- **0.5** — urgência só quando é real. A distinção transfere inteira: prazo
  real vale, escassez de capacidade fabricada não. E vale mais ainda em evento
  gratuito, onde "últimas vagas" é mentira óbvia.
- **0.1, o princípio** (não o formato): o documento que vai pro expert contém só
  o que ele lê em voz alta. Rótulo de bloco, duração e direção de cena atrapalham
  quem está no teleprompter. Como o expert lê muda por pessoa: confirme com o
  novo antes de assumir.
- **0.8** — formato (vídeo/estático/carrossel) é pra testar por ângulo, não pra
  cravar.
- **A postura de voz de 0.7** (validar a dor antes de redirecionar e culpar o
  método, nunca a pessoa) transfere bem pra qualquer expert de ensino. Mas as
  **frases** são do expert do caso-base.

**Não transfere (é o caso-base e o nicho dele):**

- A promessa do programa principal, a promessa do evento pago e o inimigo que o
  expert do caso-base combate.
- A **credencial do expert do caso-base**: é o diferencial dele. O que transfere é a
  pergunta: qual é a credencial que só este expert tem, e ela está aparecendo uma vez
  por peça?
- Os três funis como recorte (gratuito/pago/VSL) e o mapa de CTA preenchido: as
  fases dependem do modelo que o cliente roda.
- O conteúdo dos exemplos de copy reprovada e aprovada (os do §0.10).
- **0.7.1 (criativo não fala valor)** é diretriz do Rodrigo pra este cliente,
  marcada ISOLADA e sem teste A/B. **Escopo delimitado por ele: vale pra lançamento
  gratuito.** Em perpétuo, low ticket e ingresso de lançamento pago, a leitura dele é
  a oposta (ver 0.7.2). Em cliente ou funil novo, é hipótese a combinar, não regra
  herdada.

⚠️ **Ao levar pra um negócio sem expert que grava** (SaaS, negócio local): este arquivo
pressupõe **expert que grava a própria copy** (teleprompter, voz, credencial pessoal).
Produto sem rosto quebra a fundação inteira de 0.1, 0.3, 0.4 e 0.7. Nesse caso,
aproveite 0.2, 0.5, 0.6, 0.8 e a mecânica de plataforma, e escreva a fundação nova em
vez de adaptar esta.

#### Primeira execução fora da base — um SaaS de outra empresa do Rodrigo (registro de lacuna, não de padrão)

*Anotado pela regra de registro ao fechar peça grande (`sirius-scale/REGRAS.md` §5).*

A primeira leva de criativo pra esse SaaS foi de 10 roteiros de vídeo de aquisição
(5 pra frente de infoproduto + 5 pra frente de negócio local). **Não há resultado
nenhum ainda**: nada aqui é padrão, é registro de que a execução existe pra quem
escrever a próxima não começar do zero.

Duas observações que já valem, e que refinam o aviso acima:

1. **O caso é intermediário, não "sem rosto".** O aviso trata SaaS como produto sem
   rosto, mas quem grava é o Rodrigo, sócio, com credencial própria de quem opera
   lançamento há anos. Então **0.1, 0.3 e 0.4 voltam a valer em parte**: a credencial
   existe, ela só não é a do expert-cliente. O que realmente não transfere é o
   **conteúdo** (dor, promessa, vocabulário), como o arquivo já diz.
2. **As duas frentes desse SaaS exigem vocabulários incompatíveis entre si.** Na
   frente de negócio local, **nenhuma sigla de marketing** pode aparecer (ROAS,
   CPL, CAC, atribuição, funil, criativo): a página dessa frente não usa uma
   sequer, e o avatar reclama de ferramenta que não ajuda a ler o negócio
   dele. Na frente de infoproduto o jargão é nativo e obrigatório. **Uma
   leva só de criativo não serve as duas frentes**: foi por isso que a
   produção rodou em dois agentes separados.

**Diretriz 0.7.1 (criativo não fala valor) nesse SaaS: RESOLVIDO no dia seguinte, e o
resultado foi melhor que uma confirmação: foi uma delimitação de escopo.**

Os roteiros nasceram citando o preço da assinatura nas duas frentes, porque nessas
ofertas o preço parecia ser o argumento. O Rodrigo mandou **tirar** e, ao justificar,
delimitou a regra: *"sobre valor em criativo acredito que funciona mais para perpétuo,
low ticket, ou ingresso de lançamento pago."*

**O que isso ensina, e é o mais valioso:** a 0.7.1 estava escrita como regra de
**cliente** quando na verdade é regra de **funil**. Ela nasceu num lançamento gratuito
e foi generalizada sem que ninguém notasse o recorte. Virou 0.7.1 (escopo: lançamento
gratuito) + 0.7.2 (onde o valor pode entrar).

⚠️ **Isto NÃO promove o alcance do arquivo.** Não houve confirmação em segundo
cliente: houve descoberta de que a regra era mais estreita do que parecia. O
cabeçalho continua `NÃO TESTADO FORA`. **Delimitar escopo e transferir padrão são
coisas diferentes**, e confundir as duas é como uma variação isolada vira "regra
geral" sem nunca ter sido testada.

**Efeito prático na peça:** um dos roteiros da frente local era uma conta de margem que
terminava no preço. Sem o número, foi reconstruído trocando o eixo, de **quanto custa** pra
**como cobra** ([preço único, que não muda com o tamanho do time]), com o resultado da conta em aberto pro espectador. Ficou mais alinhado
com o plano maior do produto, que nem tem preço público. Registro de que a saída do preço
não precisa enfraquecer a peça: às vezes força um argumento melhor.

**O que continua não existindo:** framework de **estrutura de roteiro de vídeo
de aquisição** (o que vai em 0–3s, o que vai no meio, como fecha, por duração).
Os 10 roteiros usam uma estrutura, mas ela saiu do avatar e da voz do Rodrigo,
não de padrão validado. Vira candidato a framework quando houver resultado de
veiculação, não antes.
