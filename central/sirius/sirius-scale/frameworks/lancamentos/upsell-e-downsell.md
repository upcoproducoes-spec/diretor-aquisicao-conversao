# Framework — Upsell e downsell (a oferta depois da compra ou da recusa, em vídeo e página)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> Reverse-engineered de 3 funis de VSL em perpétuo: 10 roteiros de backend (5 de upsell, 5 de downsell),
> os documentos de arquitetura e de preço, a única medição de backend da casa e as falas e decisões do
> Rodrigo ao longo de cerca de seis semanas. Escrito no fim desse período.
>
> **ALCANCE: TESTADO EM 3 CLIENTES (proposto)** (de duas empresas da casa; aqui, os experts A, B e C).
> "Testado" aqui é **por execução**: a escada foi desenhada e os roteiros foram escritos nos três, sem
> resultado medido em dois deles. **No ar e medido, um só:** o perpétuo do livro do B. Os roteiros do C
> ficaram em roteiro; os do A foram gravados, editados e aprovados, sem publicação confirmada em arquivo.
> Mexer no alcance é decisão do Rodrigo. Cada seção diz de qual cliente vem o padrão; o que está num
> cliente só é marcado assim. Ao aplicar no negócio de vocês, ler a §8 e dizer na entrega que a regra
> ainda não foi testada nele (`sirius-scale/REGRAS.md` §4).
>
> **Quem é quem:** A, B e C são três experts de infoproduto atendidos pela casa (as letras são as mesmas
> de `sirius-scale/frameworks/lancamentos/perpetuo.md`). O C tem duas frentes com os produtos trocando de
> lugar: **C1** (livro na frente, curso no upsell) e **C2** (curso na frente, livro no upsell). D é um
> quarto expert, citado só de passagem.
>
> **Método externo por trás de 3 dos 5 roteiros de upsell:** o prompt
> `sirius-scale/frameworks/copy/video-de-upsell.md` (11 blocos, fases 1 a 3). Aqui ele é citado, não
> repetido. O que a casa mudou nele está na §8.2.
>
> **Vizinhos, não duplicados aqui:** live de downsell depois do carrinho de lançamento →
> `sirius-scale/frameworks/lancamentos/live-de-downsell.md`; order bump e upsell de um clique dos guias de
> low ticket → `sirius-scale/frameworks/lancamentos/low-ticket.md` §2, §3 e §11.

---

## 1. Escopo e base de evidência

| Fonte | O que tem | Unidades | Peso |
|---|---|---|---|
| **A. Expert A, perpétuo do material físico** | o plano de produção, a matriz de preços e o desempenho do funil; a direção e o teleprompter do upsell e do downsell; a revisão de copy do funil; o projeto de edição dos vídeos; a página que o cliente já rodava antes da casa (evidência no caso de origem) | 1 upsell, 1 downsell (+ a página anterior, que não é da casa) | **forte**: decisões do Rodrigo no dia do plano, revisão, gravação pelo expert e aprovação do gestor do projeto pouco mais de cinco semanas depois. Publicação não confirmada |
| **B. Expert B, perpétuo do livro** | o briefing do funil (a escada e os erros conhecidos dos roteiros), o desempenho, os roteiros do upsell 1, do upsell 2 e do downsell; o debriefing do perpétuo; os dados de venda (evidência no caso de origem) | 2 upsells, 1 downsell | **forte** na escada e no número (foi ao ar, vendas na Hotmart); **média** nos roteiros (vieram de um projeto do próprio expert no Claude, sem edição, e a versão no ar não está confirmada) |
| **C. Expert C, funil VSL do livro** | o README (a oferta, a escassez verdadeira e o histórico de decisões de duas semanas), o briefing, as fases 1 e 2 e os scripts dos upsells C1 e C2 (com as mudanças da v1 pra v2), a arquitetura dos upsells e dos downsells, os scripts dos downsells, a revisão do upsell C1 e o arquivo do curso (evidência no caso de origem) | 2 upsells (C1, C2) e 3 downsells (C1 v1 descartada, C1 v2, C2) | **forte** nas decisões do Rodrigo; **média** nos roteiros (escritos, revisados, docs de gravação prontos; não gravados) |
| **D. Falas do Rodrigo em reunião** | o modelo de VSL explicado a dois prospects; duas calls com o B (downsell da Black e digital como downsell); uma consultoria (o funil recomendado e a leitura de um downsell de mercado); outra call com o B (só um vídeo de upsell testado); uma terceira com o B (vender o livro porque cai no upsell); uma com o gestor do projeto do A (venda de upsell perdida no cartão); a ata de uma prévia com o B (o preço pode limitar o upsell) | 8 reuniões | **forte**. Nas transcrições a fala dele aparece com o nome de uma conta de vídeo; o ASR escreve "dar um céu" no lugar de downsell |
| **E. Expert C, linha de low ticket** (o desenho dos funis, o pós-compra e o relatório de um turno da noite) | o lugar do upsell e do downsell na linha, e a decisão de não montar o upsell agora | 1 desenho | **média** (desenho; decisão relatada no turno da noite, sem aprovação registrada) |
| **F. Método externo** | `sirius-scale/frameworks/copy/video-de-upsell.md`, recebido do Rodrigo na época do plano do A e guardado na casa pouco depois | — | origem, não evidência de resultado |
| **G. Referência de mercado do downsell encenado** | o downsell de uma expert de outro nicho, mandado pelo Rodrigo | — | só origem do formato; não se reproduz |

**Contagem:** 10 roteiros distintos. A v1 e a v2 do upsell C1 contam uma vez (mesmo produto); o
downsell C1 v1 conta à parte porque vendia outro produto e vale como prova da correção do Rodrigo, não
como modelo. **Veredito da fase 1: EXTRAÍVEL FORTE** pela régua do método
(`sirius-scale/frameworks/_extracao-de-frameworks.md`: 8+ unidades e 3 clientes), com a ressalva de que a
única medição é da escada, não de um roteiro.

**Excluído de propósito:**

- **Live de downsell depois do carrinho de lançamento.** Outro artefato, com framework próprio
  (`sirius-scale/frameworks/lancamentos/live-de-downsell.md`). O mesmo vale pro tráfego e pro remarketing
  do downsell de lançamento (`sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.6,
  `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §29,
  `sirius-scale/frameworks/copy/criativos.md` §0.7.4).
- **Order bump e a mecânica de upsell dos guias de low ticket.** Já estão em
  `sirius-scale/frameworks/lancamentos/low-ticket.md` §2, §3 e §11; aqui só se cita.
- **O texto do prompt de upsell** (os 11 blocos, os 7 princípios, os anexos). Está em
  `sirius-scale/frameworks/copy/video-de-upsell.md`; aqui entra o que a casa fez com ele.
- **Downsell da próxima Black do B** (cursos separados a 50% depois do combo, decisão do Rodrigo). É
  downsell de lançamento e ainda não rodou: só entra na §9.
- **Material de terceiro:** funis de outros experts, a Black de outro lançador citada em reunião e
  material de método de outras empresas. Nada disso é prática da casa.
- **Ideias sem decisão:** o webinário diário pra quem não levou o upsell (numa reunião, "só ideia") e o
  livro como upsell no projeto do expert D (numa análise).

**Ressalva estrutural:** 3 clientes de 2 empresas, 3 funis de VSL em perpétuo, nenhum lançamento. Um único
funil foi ao ar com número, e mesmo nele não se sabe qual versão do vídeo rodou. **Nenhum roteiro escrito
pela casa tem resultado medido.**

---

## 2. Status: o que foi ao ar e o que ficou em roteiro

Os preços estão como relação, não em reais.

| Funil | A escada | Estado no fim da extração | Número em arquivo |
|---|---|---|---|
| **B, perpétuo do livro** | livro digital (front) → upsell 1: o curso principal a 2,3 vezes o front (o cheio na Hotmart é 8,4 vezes o front) → quem recusa: o mesmo curso com 6 meses, a 57% do upsell → quem compra: upsell 2, outro curso a 53% do cheio dele | **No ar** por cerca de quatro meses; tráfego pausado desde o 5º mês, religar combinado numa call. Qual vídeo está no ar: não confirmado | 17 de 151 compradores do livro levaram o curso (11,3%); upsell 2: 0 vendas (§4.15) |
| **A, perpétuo do material físico** | material físico de apoio (front) → upsell: o curso caro a 48% do cheio (2,4 vezes o front) → quem recusa: o mesmo curso com 6 meses, a 58% do upsell | Antes da casa rodava a página do próprio cliente, com o upsell 17% abaixo do preço novo, e vídeos de meses antes. Os roteiros da casa foram **gravados, editados (4:50 e 2:12) e aprovados** pelo gestor do projeto pouco mais de cinco semanas depois do plano. Página nova e preço novo no ar: não confirmado | 7,7% da base do front comprou o curso (compra cruzada do período todo, não só o um clique) |
| **C1** | livro (front) → upsell: o curso a 2 vezes o front (fora daqui, 2,5 vezes) → quem recusa: o mesmo curso com 6 meses, a cerca de 50% do upsell | **Roteiro.** Docs de gravação prontos; VSL não lançada | — |
| **C2** | curso (front) → upsell: o livro a 30% do front (fora daqui, 40%) → quem recusa: o livro com desconto, a 66% do upsell | **Roteiro** | — |
| **C, linha de low ticket** | livro digital de ticket baixo + 3 bumps → slot de upsell vazio | **Desenho;** upsell não montado de propósito | — |

---

## 3. A fórmula, em ordem

1. **Montar a escada:** o que se oferece pra quem, em que ordem e a que preço (§4.1 a §4.7).
2. **Conferir na plataforma tudo o que vai ser dito:** preço cheio público, oferta de 6 meses, parcela,
   garantia, mecânica do um clique (§4.8).
3. **Ler o que o front entrega** e separar os ativos da VSL e do upsell antes de escrever (§4.9, §4.10).
4. **Escrever o upsell** (§4.11).
5. **Escrever o downsell** (§4.12).
6. **Montar as duas páginas** (§4.13).
7. **Tirar da fala o que pode mudar** (texto do botão, preço por mercado) e conferir a gravação contra o
   roteiro (§4.14).
8. **Revisar contra a oferta configurada** na véspera de gravar e de publicar (§5, regra 1).
9. **Medir por oferta**, não por produto (§4.15), e recuperar a venda que trava no checkout (§4.16).

**Os modos que se repetem:**

- **Upsell degrau** (o ticket sobe e o formato muda: livro → curso, material físico → curso): 3 de 5 roteiros.
- **Upsell complemento:** 2 de 5. No C2 o ticket desce (curso → livro); no B é o 2º upsell, outro
  curso que aprofunda um tema do primeiro.
- **Downsell do mesmo curso com menos acesso:** 3 de 4 downsells válidos, nos 3 clientes.
- **Downsell do mesmo produto, só com desconto:** 1 de 4, produto físico sem acesso pra cortar.

**O que todos compartilham:** o upsell num formato diferente do front; botão de um clique dentro da compra;
condição que só existe nesta compra; quem recusa o upsell vê o downsell; o downsell não é anunciado antes da
recusa; nada de cronômetro.

---

## 4. Etapa por etapa (força no título de cada uma: CONSISTENTE, ISOLADA ou INCONCLUSIVO)

### 4.1 A escada: produto de entrada na frente, o upsell em outro formato — PADRÃO CONSISTENTE (proposto)

- **O que entra.** Na frente, o produto de entrada (livro ou material físico; numa das frentes, o próprio
  curso). Logo depois do pagamento, na mesma compra, o upsell de um clique: o próximo degrau, **num formato
  diferente do front** (livro → curso, material físico → curso, curso → livro), num preço que só existe ali.
  A página tem dois botões, o de querer e o de não querer; quem recusa vê o downsell; quem compra segue (pro
  2º upsell, onde houver, §4.5). O desenho se repete nas 4 escadas da base, e nas 4 o upsell muda de formato
  em relação ao front.
- **Por quê.** O funil de VSL ganha no backend: o objetivo declarado é o ticket médio do funil inteiro. Quem
  acabou de comprar um curso não tem motivo pra comprar outro curso agora; quem comprou um livro compra o
  curso. E o curso caro não se vende sozinho em perpétuo pra público frio: num dos casos ele só vendia cheio
  com máquina de lançamento, então no perpétuo entra pelo upsell. O mesmo vale pra lead morno: vende-se o front
  porque quem compra o front cai no upsell.
- **Variações aceitáveis.** Duas frentes com os produtos trocando de lugar (C, VARIAÇÃO ISOLADA): o
  curso é front numa e upsell na outra, o que torna verdadeira a fala sobre o preço de fora (§4.8).
  Upsell que desce o ticket (§4.11, tese de complemento). Upsell de produto pronto ou serviço depois de um
  curso (o "peixe assado"): recomendado pelo Rodrigo numa consultoria, nunca rodou na casa, PADRÃO
  INCONCLUSIVO.
- **Trecho real.**
  - Rodrigo, numa consultoria: "a pessoa compra o front, ela vai receber uma oferta de […]." e "Só que
    aqui, o importante é que o formato seja diferente do front." e "porque a pessoa acabou de comprar um
    curso ela não tem um motivo pra comprar outro curso agora se ela comprar um livro, ela vai comprar um
    curso depois" e "Aí, tem dois botões na página de Opcel, quero e não quero." ("Opcel" é o ASR de
    upsell).
  - Rodrigo, numa call com dois prospects: "O Low ticket não tem vídeo, é só página escrita e tal, e só que
    daí a VSL te ganha no funil, porque aí tem o produto de entrada, de front ali, que é […], aí a pessoa
    compra aquele e cai no upsell." e "Então, a gente busca ganhá-lo o funil inteiro, aumentar o ticket
    médio, sabe?" ("ganhá-lo" é o ASR de *ganhar*).
  - A, decisão do Rodrigo no dia do plano: "[O cheio do curso] é ticket alto demais pra vender por VSL no
    BR." e "neste cliente, o ticket de [o curso] vende com máquina de lançamento" (matriz de preços do A).
  - B, leads de um congresso, Rodrigo: "Acho que é melhor vender o livro mesmo, que daí quem comprar o livro
    cai no upsell do curso."
  - C, as duas frentes: "A estrutura de duas frentes transforma a âncora interna do prompt de upsell em
    fato, não em argumento." (README do C).

### 4.2 Preço relativo: o upsell custa 2 a 2,4 vezes o front, abaixo do cheio — PADRÃO CONSISTENTE (proposto) na forma; efeito não medido

| Escada | Upsell ÷ front | Cheio fora daqui ÷ front | Upsell ÷ cheio |
|---|---:|---:|---:|
| B | 2,3 | 8,4 (o roteiro dizia 6,7) | 28% |
| A | 2,4 | 5,0 | 48% |
| C1 | 2,0 | 2,5 | 80% |
| C2 (desce) | 0,3 | 0,4 | 75% |

- **O que entra.** Nas 3 escadas que sobem, o upsell custa 2 a 2,4 vezes o front. A faixa que o Rodrigo
  diz em voz alta, posta em proporção, é mais larga: de 1,2 a 2,35 vezes o front, e o upsell do A fica fora
  dela. O desconto sobre o cheio não tem padrão (de 20% a 72%).
- **Por quê.** Não há medição que explique a razão. O que existe é a hipótese do Rodrigo de que o preço
  pode estar segurando a taxa do único upsell medido, e o check do prompt de que o preço não pode
  canibalizar o front nem desvalorizar o cheio (`sirius-scale/frameworks/copy/video-de-upsell.md`, Anexo B).
- **Variações aceitáveis.** Upsell acima do que já rodava: no A, o upsell novo ficou 20% acima do que
  rodava na página anterior do cliente; a casa avisou antes ("é aumento, não desconto") e a peça saiu com o
  preço novo.
- **Trecho real.**
  - A faixa, na fala do Rodrigo (call com dois prospects): "O upsell daí é outro produto de […], e aí com
    desconto, uma condição que só tem naquela página, sabe?"
  - B, ata de uma prévia: "o Rodrigo levantou que os 11% de conversão podem estar limitados pelo preço".
  - A: "[O preço novo] é 20% ACIMA do upsell que está no ar." (plano de produção) e "[O preço novo] é
    exatamente a mediana real das 81 vendas do [curso] no Dash" (direção do upsell).

### 4.3 O downsell: o mesmo curso, metade do acesso, preço menor — PADRÃO CONSISTENTE (proposto)

| Funil | Downsell ÷ upsell recusado | Acesso | Bônus |
|---|---:|---|---|
| B (no ar) | 57% na Hotmart (o roteiro anunciava 50%) | 6 meses | o curso completo |
| A | 58% | 6 meses em vez de 1 ano | todos, mesmos módulos |
| C1 | cerca de 50% | 6 meses em vez de 12 | os dois bônus |

- **O que entra.** Pra quem recusou o upsell de um curso: o **mesmo curso, inteiro**, com metade do tempo de
  acesso e um preço bem menor. Nada de conteúdo tirado; o que muda é o prazo. Em 2 dos 3 casos foi decisão
  do Rodrigo, no mesmo dia; no terceiro a escada já rodava assim desde o começo do funil (quem decidiu ali
  não está registrado).
- **Por quê.** O Rodrigo dá o desenho, não o porquê. O porquê registrado é a **recomendação do agente** no
  plano do A, que virou a base da peça: é verdade e é conta (não inventa escassez, não desmerece o cheio,
  não cria motivo pra desconfiar do upsell recusado segundos antes), ataca a objeção de tempo e protege a
  escada (quem quer acesso longo continua tendo motivo pra pagar o cheio). Não é razão medida nem dita por
  ele.
- **Variações aceitáveis.** Produto que não tem acesso pra cortar (livro físico) leva só desconto (§4.4).
  O Rodrigo usou a mesma lógica ao ler um downsell de mercado de produto pronto: ali não cabia metade do
  preço, cabia um desconto fixo. **O que foi tentado e caiu:** o downsell que troca de produto (vender
  sozinho um pedaço do curso recusado, a cerca de um quarto do preço do upsell), escrito num dia e
  descartado no seguinte; e um plano anterior de uma "versão reduzida" com entregáveis tirados, superado
  pela decisão de manter todos os bônus.
- **Trecho real.**
  - Rodrigo, numa consultoria, descrevendo o próprio funil: "no downsell a gente vende o mesmo curso só que
    com 6 meses de acesso e a metade do preço"; e as duas opções que ele dá: "Desconto do produto do Opcel
    ou o mesmo produto com menos acesso, mais barato."
  - C1, decisão do Rodrigo: "na minha cabeça a gente ia vender o mesmo curso pela metade do preço e metade
    do acesso" (downsell C1 v2). A v1 registra o porquê do descarte: "o Rodrigo não reconheceu essa
    decisão".
  - A, decisão do Rodrigo no dia do plano: "Downsell: mesmo curso, metade do preço, metade do tempo de
    acesso." e, na recomendação do agente, "downsell longo levanta suspeita sobre o preço cheio".
  - B, roteiro: [três frases curtas que repetem que é o mesmo curso] + [frase que diz que só o prazo muda].
  - Leitura do Rodrigo sobre o downsell de mercado (na mesma consultoria): "aí como é um peixe assado, ela
    não vai dar metade do preço".
  - **Resultado:** 5 das 17 vendas do curso feitas por compradores do livro do B saíram pela oferta de
    downsell (§4.15).

### 4.4 Downsell só de desconto, nada tirado — VARIAÇÃO ISOLADA

- **O que entra.** Quando o upsell é um produto físico, sem prazo de acesso pra cortar: o mesmo produto,
  pelo mesmo caminho, com desconto dito em reais. A peça prova que nada saiu.
- **Por quê.** Decisão do Rodrigo pra um livro físico (C2), com o risco aceito por escrito. É a primeira
  das duas opções que ele mesmo dá pro downsell (§4.3): desconto no produto do upsell.
- **Variações aceitáveis.** Nenhuma observada na casa.
- **Trecho real.** "Downsell [da C2] = mesmo livro, só desconto" (Rodrigo) e o risco aceito: "quem espera
  dez segundos ganha [o desconto]" (README do C); na fala: [frase curta que diz que nada saiu, só o preço]
  (downsell C2).

### 4.5 Segundo upsell, só pra quem comprou o primeiro — PADRÃO INCONCLUSIVO

- **O que entra.** Quem aceita o upsell 1 vê um upsell 2 (outro curso, complemento do primeiro). Quem recusa
  o upsell 1 vai pro downsell e depois pro obrigado, sem o upsell 2. Existe num funil só (B).
- **Por quê.** Não há evidência suficiente: zero vendas e ninguém sabe se a página chegou a ser exibida. É
  também o único passo da casa em que um curso vem logo depois de outro curso, o que bate de frente com a
  regra de formato da §4.1; com zero vendas e sem saber se foi exibido, não dá pra separar uma causa da
  outra.
- **Variações aceitáveis.** Não há base.
- **Trecho real.** "Contexto: Aparece APÓS compra do Upsell 1 ([curso] — [preço])" (roteiro do upsell 2
  do B) e, no debriefing: "Não sei se chegou a ser oferecido."

### 4.6 Downsell de formato: o físico na frente, o digital pra quem não leva — PADRÃO INCONCLUSIVO

- **O que entra.** Quando existe versão física e digital do mesmo produto, vende-se só o físico e o digital
  vira o degrau mais barato pra quem não comprou.
- **Por quê.** Reembolso de quem comprou o PDF e reclamou que era só um arquivo (fala do Rodrigo na mesma
  reunião).
- **Variações aceitáveis.** Decidido pro B, ainda não rodou. No A, segundo o gestor do projeto, o digital
  chega a quem abandona o carrinho do físico, por e-mail e mensagem ao longo de uma semana; não é um clique
  dentro da compra.
- **Trecho real.** Rodrigo, numa call com o B: "Então, acho que a hora de vender, a hora que tiver o
  físico, é só o físico." e "E aí o digital nessa estratégia, ali no máximo, pra dar um céu, né?" e "Pra
  quem não comprar, na verdade." O gestor do projeto do A, na mesma call: "aí sim ele recebe como se fosse
  um downsell, né?"

### 4.7 Quando não montar o upsell — VARIAÇÃO ISOLADA

- **O que entra.** O slot de upsell fica vazio quando todo candidato bate em outra oferta próxima: o produto
  que vai estar dentro da próxima oferta grande (comprar agora vira reembolso depois) ou um combo que é a
  soma dos order bumps (ensina a pular o bump). O guia externo de low ticket já mandava não pôr bump nem
  upsell antes de validar a oferta (`sirius-scale/frameworks/lancamentos/low-ticket.md` §11).
- **Por quê.** Numa linha de low ticket (a do C), as duas ideias do Rodrigo pro upsell batiam na oferta
  grande seguinte (a Black) e nos bumps.
- **Variações aceitáveis.** O próximo passo vai por e-mail depois da oferta grande, em vez do um clique.
- **Trecho real.** "Quem comprasse o curso agora levaria o mesmo curso de novo no combo, três semanas depois.
  Isso vira pedido de reembolso." e "Se o combo sair mais barato, ensina a pular o bump." e "Upsell de 1
  clique de verdade entra depois da Black" (relatório do turno da noite da linha de low ticket do C).

### 4.8 Verdade antes da copy: o que se diz tem que estar configurado — PADRÃO CONSISTENTE (proposto)

- **O que entra.** Antes de escrever (e de novo na véspera de gravar e de publicar), conferir na plataforma:
  1. **a mecânica do um clique:** na Hotmart o botão só existe dentro da compra em andamento. Esse fato é a
     escassez inteira do backend (fato de plataforma, confirmado pelo Rodrigo);
  2. **o preço cheio fora desta compra** é o preço público de hoje, não um preço antigo ou de lançamento;
  3. **a oferta reduzida existe** como oferta própria (o curso com 6 meses), com o prazo configurado;
  4. **a parcela** sai do checkout, nunca de conta;
  5. **a garantia** da oferta reduzida é a mesma que a peça promete.
- **Por quê.** Nos 3 clientes, a maior parte do que foi corrigido em revisão era frase que deixou de ser
  verdade (§6). No backend a pessoa acabou de pagar e confere na hora.
- **Variações aceitáveis.** Quando o dado ainda não existe, a peça grava sem ele: a fala marcada como
  `[[INSERIR]]` vira pick-up depois, nunca número estimado.
- **Trecho real.**
  - "o botão de um clique do upsell e do downsell só existe dentro de um processo de compra ativo" e "Não é
    tempo, é mecanismo." (README do C, decisão do Rodrigo).
  - Âncora conferida contra o preço real: no C, a conferência achou que nenhum pedido tinha sido cobrado,
    até aquela data, pelo preço cheio que a âncora usava (evidência no caso de origem); no B, a revisão do
    briefing achou o upsell ancorado num cheio 20% abaixo do configurado na Hotmart e o downsell anunciando
    um preço 12% abaixo da oferta configurada, com outra parcela nas vendas.
  - A oferta de 6 meses: "a oferta de 6 meses precisa existir na Hotmart como oferta própria (180 dias)"
    (downsell C1 v2).

### 4.9 Ler o que o front entrega antes de escrever a tese — PADRÃO CONSISTENTE (proposto)

- **O que entra.** A tese do upsell diz o que o front não faz. Então, antes dela, ler a lista do que o
  comprador recebe no front (entregáveis, bônus, presente) e o conteúdo real do produto, não a descrição.
- **Por quê.** Nos 3 clientes a primeira versão afirmou como novidade algo que o comprador já tinha ou
  prometeu o que o produto não entrega: o curso que "resolvia" todos os exercícios do livro (C1), a aula que
  o vídeo dizia não caber no front e que o front já dava de presente (A), bônus do upsell 1 repetidos no
  upsell 2 (B).
- **Variações aceitáveis.** **A amostra como tese** (A, VARIAÇÃO ISOLADA): quando o front já entrega um
  pedaço do backend, a tese se apoia nele ("confira o que você já tem") em vez de num buraco.
- **Trecho real.**
  - C1, correção do Rodrigo: "tem que conferir se ela resolve tudo isso, onde você viu?" (fases 1 e 2 do
    upsell C1); a revisão seguinte achou o mesmo erro na última frase antes do botão: "Implicava que o curso
    resolve [todos os exercícios] do caderno".
  - A, 2º passe: "Documento de produto diz o que o produto é; manual do vendedor diz o que o cliente
    recebe." e a regra que saiu dali: "antes de escrever qualquer peça que afirme o que um produto NÃO tem,
    ler a lista de entregáveis e bônus daquele produto" (direção do upsell do A).
  - B, v2 do upsell 2: "Bônus repetidos removidos" (os dois bônus que o upsell 1 já dava).

### 4.10 Separar os ativos da VSL e do upsell antes de escrever — VARIAÇÃO ISOLADA (2 clientes)

- **O que entra.** Uma tabela, antes de escrever as duas peças, dizendo pra onde vai cada ativo: número de
  autoridade, história, dor, depoimento. O que a VSL gasta não volta no upsell.
- **Por quê.** O prompt manda não repetir nada da VSL; alocar antes evita descobrir depois que a VSL queimou
  tudo.
- **Variações aceitáveis.** O C fez depois da VSL pronta (lista de números e frases queimados, tabela de
  depoimentos por peça); o A fez antes de escrever qualquer uma.
- **Trecho real.** "O que a VSL guarda para o upsell (planejar agora evita retrabalho)" (plano de produção
  do A); "quem entra na VSL do front não repete no upsell da mesma frente" (README do C, "Depoimentos — quem
  vai onde").

### 4.11 O roteiro do upsell — 9 elementos PADRÃO CONSISTENTE (proposto), 3 VARIAÇÃO ISOLADA, 2 PADRÃO INCONCLUSIVO

A ordem dos blocos de 3 dos 5 roteiros (C1, C2, A) é a do prompt externo
(`sirius-scale/frameworks/copy/video-de-upsell.md`, Fase 3). Os 2 do B seguem outra ordem: parabéns, ponte
do front pro curso, apresentação, diferencial, prova social, bônus, suporte, oferta, escassez, garantia,
fechamento. ⚠️ **O único upsell ligado a número é o do B**, e não se sabe qual versão rodou. Fala de roteiro
vem em molde: o colchete diz o que a frase faz, e vocês escrevem a de vocês. Entre aspas ficam só anotações de
direção e de revisão e falas do Rodrigo.

| Elemento | O que entra | Por quê | Força | Trecho (fala em molde) |
|---|---|---|---|---|
| **Abertura** | Confirma que a compra está feita e que não falta pagar nada; promete a janela de tempo | quem acabou de pagar espera confirmação; dizer que a compra está incompleta mente e troca alívio por arrependimento | **CONSISTENTE (proposto)**: 5 de 5 reconhecem a compra; 3 de 5 dizem que não falta nada | [frase que diz que o front já está garantido] + [frase que diz que isto não é cobrança nem etapa pendente] (C1); [frase que confirma a compra] + [frase que diz que não falta nada e que nada deu errado] (A); [frase que reconhece a compra do front] (B). Leitura do Rodrigo sobre um upsell de mercado, numa consultoria: "Ela é muito agressiva, Só compra e não está completa." (ASR) |
| **Janela dita** | Os minutos ditos na abertura batem com o corte | é a primeira frase que pede confiança | **CONSISTENTE (proposto)**: 3 de 3 do prompt | "a janela dita tem que ser verdade" (upsell C1 v2); no A a revisão pegou "quatro minutos" numa peça de ~5:45: "Erra por 30%" |
| **Big Claim e autoridade** | Um número que a VSL não usou (de produto ou de autoridade) e nenhuma credencial repetida | o comprador já ouviu a autoridade da VSL; repetir gasta a atenção | **VARIAÇÃO ISOLADA**: 2 de 3, um cliente só (C). No A o número guardado pro upsell já estava na VSL no ar e voltou num hook novo montado na VSL completa; a direção do upsell avisou | C1 e C2: um número de produto (a quantidade de exercícios do caderno do livro), e a credencial da VSL zerada: "A autoridade desta peça é o ato" (ficha do upsell C1 v2). A, no upsell: [frase com o número de alunos que já praticaram com o expert, com a ferramenta do ofício]; o mesmo número de alunos já estava na VSL no ar e num hook novo da rodada seguinte, montado na VSL completa; o aviso da direção: "já aparece na VSL atual" |
| **Tese** | O que o **formato** do front não faz, com o front elogiado na mesma frase | o upsell não pode desvalorizar o que a pessoa acabou de comprar | **CONSISTENTE (proposto)**: 4 de 5 | [frase que diz que isso não é falha do front] + [o que esse formato dá] + [o que esse formato não faz: acompanhar a pessoa depois que ela fez] (C1); [frase que separa o que a pessoa já garantiu, ver, do que falta, fazer] (C2); [o que o front dá, elogiado] + [o que só a aula dá] (A); [frase que elogia o front pelo que ele é e diz que sem ele a pessoa se perde] (B, upsell 1) |
| **Tese quando o ticket desce** | Complemento, não degrau: o curso é ver, o livro é fazer | com o ticket descendo, "mais profundidade" não cola | **VARIAÇÃO ISOLADA** (C2) | "upsell A sobe ticket e vende profundidade; upsell B desce ticket e vende complemento" (briefing do C; ali "upsell A" e "upsell B" são o C1 e o C2) |
| **Dor ativa** | Uma pergunta de memória com dor que a VSL não usou | sem dor ativa o produto vira luxo (princípio 4 do prompt); a casa exige que a dor seja nova | **CONSISTENTE (proposto)**: 4 de 5 | [pergunta de memória: quantas vezes a pessoa terminou o trabalho e ficou insegura esperando o sinal de que deu certo] (A); [par de frases curtas que contrapõe o resultado que chegou à explicação que não veio] (C1) |
| **Negação tripla** | As três negações do prompt com tamanhos diferentes | a casa proíbe tríade sincronizada (ficha de voz do expert do caso de origem); a casa vence o prompt | **CONSISTENTE (proposto)**: 3 de 3 do prompt | [negação curta do conselho de sempre] + [negação curta de fazer mais] + [negação bem mais longa do que todo mundo repete] (C1, com os tamanhos do original); "A negação tripla entra com ritmo quebrado — três negações de tamanhos diferentes, não três frases gêmeas." (fases 1 e 2 do upsell C1) |
| **Âncoras** | Só as verdadeiras: o preço cheio fora desta compra e um custo do problema novo. Sem âncora externa inventada; quando falta, declara | número sem fonte não entra (`sirius-scale/REGRAS.md` §2) | **CONSISTENTE (proposto)**: nenhuma das 3 peças do prompt tem âncora externa, e as 3 declaram quantas âncoras têm e por quê | "Preferimos duas verdadeiras a três com uma inventada." (upsell C1 v2); "Sem âncora externa (não existe pesquisa de livro × livro em arquivo)" (arquitetura do upsell C2); no A o custo do problema não atravessa mercado e o bloco do outro mercado saiu com 2 âncoras (matriz de preços) |
| **Escassez** | A condição só existe nesta compra / nesta página; nada de cronômetro, vaga ou "a página sai do ar" | é a única urgência verdadeira do backend | **CONSISTENTE (proposto)**: 5 de 5 dizem que é só aqui | [frase que diz que o botão de um clique só existe dentro desta compra e dispensa digitar o cartão] (C1); [frase que contrapõe o preço cheio, que segue no site, a este, que não segue] (A); [frase curta que diz que esta condição só existe nesta página] (B). ⚠️ A nota de edição do upsell 1 do B sugere o contrário: "Se a plataforma permitir, incluir barra ou contador indicando que a oferta é temporária" |
| **Escassez que sobrevive ao downsell** | Prender a escassez ao pacote ([o preço] com [o prazo inteiro de acesso]), não ao preço solto | "nunca mais" vira mentira quando o downsell oferece o mesmo curso mais barato | **PADRÃO INCONCLUSIVO** (A, registrado assim lá) | "Escassez de upsell tem que ser escrita pra sobreviver ao downsell." e [frase que amarra o preço ao prazo inteiro de acesso e ao fato de a pessoa ter entrado pelo front] (A) |
| **Downsell não se anuncia** | Nenhuma menção ao que vem se a pessoa recusar | avisar que existe uma opção mais barata mata a decisão | **CONSISTENTE (proposto)**: 5 de 5 não anunciam; 3 de 5 escrevem a regra | "destrói a decisão agora" (fases 1 e 2 do upsell C1); "Depois vem o downsell (o mesmo livro [com desconto]). Não se anuncia." (arquitetura do upsell C2) |
| **Fechamento** | Três caminhos com número (ficar só com o front; comprar depois pelo preço de fora; agora) e volta ao loop da abertura | dicotomia financeira do prompt; o caminho 2 só pode ser dito porque o preço de fora é real | **CONSISTENTE (proposto)**: 3 de 3 do prompt; o B fecha com dois caminhos sem número | [frase que volta à amostra do gancho] (A); [frase que diz que esperar não informa nada e custa a diferença em reais] (C1); [pergunta entre seguir sozinho e seguir com o expert] (B) |
| **Ecossistema** | Uma frase dizendo o que o curso não é (não é o programa principal) | protege o produto grande e ganha credibilidade | **VARIAÇÃO ISOLADA** (C1) | [frase que diz o que o curso resolve e que ele não é o programa principal] |
| **Depoimento e duração** | Prompt: até 6 min, depoimento opcional e o primeiro a sair. B: 6 a 8 min, com 3 depoimentos | o prompt diz que a atenção cai; o B aposta que prova social pesa | **PADRÃO INCONCLUSIVO**: os dois caminhos existem e o medido não tem versão confirmada | "se passar de 6:00 o Bloco 11 sai" (C1; o Bloco 11 do prompt é o de depoimentos); "Bloco 11 fora por falta de material novo" (A); "Recomendação: testar versão COM depoimentos primeiro (prova social pesa nessa decisão)" (B) |

### 4.12 O roteiro do downsell — 8 elementos PADRÃO CONSISTENTE (proposto), 3 VARIAÇÃO ISOLADA

Não existe ordem única: o C usou uma encenação de atendente em 10 batidas (formato tirado da referência
de mercado da Fonte G), o A uma conversa em 5 blocos (aceite, razão, condição, parte honesta, garantia e
CTA) e o B uma interceptação curta. Os elementos das 4 peças válidas, com a força de cada um (a fala vem em
molde, como no §4.11):

| Elemento | O que entra | Por quê | Força | Trecho (fala em molde) |
|---|---|---|---|---|
| **Não re-vende** | Nenhum argumento novo sobre o produto; a peça só renegocia um termo | a pessoa acabou de ouvir minutos de argumento e disse não | **CONSISTENTE (proposto)**: 4 de 4 | "O curso não precisa ser re-vendido: a pessoa acabou de ouvir 6 minutos sobre ele." (arquitetura dos downsells do C); "100% condição, 0% tese" (direção do downsell do A); [frase que promete não repetir o argumento] (A) |
| **Acolhe o não** | Abre aceitando a recusa, sem culpa e sem confronto | quem recusou vai ser abordado de novo em segundos | **CONSISTENTE (proposto)**: 4 de 4 | "o humor da encenação é cúmplice, nunca contra a pessoa que recusou" (arquitetura dos downsells do C); "não faz sentido humilhar quem você vai abordar de novo em 5 segundos" (direção do upsell do A); [frase que reconhece a decisão e diz que está tudo bem] (B) |
| **O que muda e o que fica** | Diz com número o que foi tirado (o prazo) e prova item por item o que ficou | todo downsell cria a suspeita "se é mais barato, o que foi cortado?" | **CONSISTENTE (proposto)**: 4 de 4 | [frase curta que contrapõe menos tempo a mesmo curso] (C1); [frase curta que diz que nada saiu, só o preço] (C2); [três negações: nada de versão resumida, de módulo bloqueado, de aula reservada] (A); [frase que diz que só o prazo muda] (B) |
| **A razão do preço** | Paga menos porque leva menos tempo de acesso | é aritmética, não convencimento (raciocínio do plano do A) | **CONSISTENTE (proposto)**: 3 de 3 downsells de curso | [frase que liga o preço menor ao prazo menor] (A); no C1 e no B, as frases da linha de cima |
| **Ritmo de estudo** | Não dizer em quanto tempo se faz o curso sem dado que sustente | promessa de ritmo sem dado é número inventado | **VARIAÇÃO ISOLADA**: 1 de 3. Só o C evita; o A diz que seis meses dão com folga; o B promete 2 a 3 meses sem fonte | "não temos duração das aulas" (arquitetura dos downsells do C); "só se existir o dado, senão é número inventado" (plano do A). A: [frase que diz que o prazo dá folga pro curso inteiro]. B: [frase que promete em quantos meses os alunos terminam] |
| **Desconto com número, a partir do preço recusado** | O desconto dito em reais ("[X] reais a menos"); o de/por parte do upsell recusado, e o cheio entra, no máximo, como fato de fora | é o número que a pessoa acabou de ver e é ele que fecha a conta | **CONSISTENTE (proposto)**: 3 de 4 (o B só diz o preço novo) | [o desconto em reais, dito duas vezes] + [de: o preço recusado] + [por: o preço novo] (C1); [frase que lembra o preço recusado, por extenso, com o prazo dele] (A) |
| **"Metade" não vai pra copy** | A intenção de preço é "metade"; na fala e na tela vai o número | no A o downsell é 58% do upsell; no C1 a metade exata dava um valor quebrado; o roteiro do B anunciava a metade do upsell e a Hotmart cobra 57% dele | **CONSISTENTE (proposto)**: nos 3 clientes a metade do desenho não bateu com o preço configurado ou teve de sair da copy | "O downsell NÃO é metade do upsell." (matriz de preços do A); "É como o Rodrigo descreveu a oferta, mas [o preço do downsell] não é metade [do upsell]. Na tela fica o número, nunca a fração." (downsell C1 v2) |
| **Curto, sem prova** | Bem mais curto que o upsell; sem depoimento e sem autoridade nova | prova social convence quem duvida do produto, e essa pessoa duvida do preço | **CONSISTENTE (proposto)**: 4 de 4 sem depoimento; ~90 s (C1), 2:12 editado (A), 2 a 3 min (B) | "Prova social convence quem duvida do produto. Essa pessoa não duvida do produto — ela já decidiu que não quer pagar aquele preço." (A); "Não inserir depoimentos — mantém a brevidade." (B) |
| **Escassez** | A mesma da casa: a condição só existe aqui | o fato é o mesmo do upsell | **CONSISTENTE (proposto)**: 3 de 4 dizem | [frase curta que diz que a condição só existe nesta página] (A); [frase que diz que o botão só existe com a compra aberta] (C1) |
| **Parte honesta** | Diz pra quem a condição não serve | troca empurrão por confiança; hipótese de reembolso menor, não medida | **VARIAÇÃO ISOLADA** (A) | [frase que diz pra quem a condição não serve: quem quer comprar agora e só olhar muito depois do prazo] |
| **Encenação** | O expert em personagem de atendente, ligação ouvida de um lado só; o setor nomeia a situação ("deixa eu pensar", "agora não"), não a pessoa | quebra o "lá vem outra venda" e cada "ah, entendi" responde à objeção de quem assiste | **VARIAÇÃO ISOLADA** (C, 2 peças; a própria peça se marca como INCONCLUSIVO até medir) | [frase que diz que quem ficou não desistiu, está decidindo] (C1); [frase que diz que o não foi pro momento, não pro produto] (C2) |

### 4.13 As páginas — PADRÃO CONSISTENTE (proposto) nas 3 peças com anexo de página; o B diverge

- **O que entra.**
  - **Página do upsell.** O esqueleto vem do anexo de página do prompt (barra de progresso com rótulo
    neutro, headline com curiosidade e sem entregar a oferta, o vídeo, botão com produto e preço; sem
    cronômetro, sem headline dizendo que a compra está incompleta, sem barra que entrega a oferta). A casa
    acrescentou: **microcopy de um clique** (sem digitar o cartão de novo, a garantia), **recusa em link de
    texto discreto, sem culpa**, **o preço do front fora da tela** e **nenhuma menção ao downsell**.
  - **Página do downsell.** O prompt não tem; é toda da casa: visivelmente mais curta que a do upsell;
    headline sem confronto; bloco de preço com o de/por a partir do preço recusado e o prazo de acesso
    escrito; um botão; recusa discreta.
- **Por quê.** Página longa no downsell grita segunda tentativa e reabre a suspeita sobre o cheio. Prazo de
  acesso só no vídeo vira reembolso.
- **Variações aceitáveis.** A do A não usa o de/por a partir do cheio no downsell; a do C1 usa de/por a
  partir do upsell recusado, com o preço de fora numa linha abaixo e o prazo junto.
- **O que o B faz diferente:** a headline do upsell 1 entrega o desconto e o botão aparece desde o
  início, embaixo do player. A página anterior do A (do cliente, antes da casa) também entregava a oferta
  na headline e dizia que a oferta nunca mais volta; a casa mandou trocar as duas coisas.
- **Trecho real.** "Prazo de acesso escondido é reembolso." (downsell C1 v2); "visivelmente mais curta que
  a do upsell" (direção do downsell do A); "Headline dizendo que a compra não está completa. Ela está, e
  dizer o contrário mente tecnicamente e transforma alívio em arrependimento." (upsell C1 v2); B: [headline
  que anuncia o desconto desbloqueado, com o valor] (upsell 1); página anterior do A: [headline que anuncia
  uma condição desbloqueada e exclusiva] e o veredito da casa: "entrega a oferta antes do vídeo — mata o
  curiosity gap do Bloco 1" (direção do upsell do A).

### 4.14 Produção: o que fica fora da fala — PADRÃO CONSISTENTE (proposto)

- **O que entra.**
  1. **O texto do botão não é falado**: a fala diz "clica no botão aqui embaixo" e o texto exato fica com a
     página, que pode mudar sem regravar. Exceção: quando o preço no botão faz parte da âncora falada
     (C1, do cheio pra condição). Decisão do Rodrigo no C; o A e o B também não nomeiam o botão.
  2. **Preço por mercado em bloco gravado à parte** (A, VARIAÇÃO ISOLADA): o corpo é gravado uma vez e
     serve também à versão do segundo mercado; só os blocos de preço de cada mercado são gravados duas
     vezes. A régua da auditoria é a verdade em cada mercado, não só o dinheiro.
  3. **Um documento de gravação por vídeo, só com o texto** (upsell e downsell de cada frente em docs
     separados; regra do Rodrigo).
  4. **Conferir a fala gravada contra o roteiro** (A, VARIAÇÃO ISOLADA): na gravação, o expert trocou o
     número de autoridade (o dobro do que estava no roteiro), uma ponta da âncora e o preço na moeda do
     outro mercado; a legenda seguiu a fala.
- **Por quê.** Número e texto de botão mudam mais rápido que o vídeo. Gravação errada só se descobre
  ouvindo.
- **Trecho real.** "texto exato do botão é trabalho da estratégia de página, não da copy do roteiro" e "o
  preço no botão ali é parte da âncora falada ([cheio]→[condição])" (README do C); "A auditoria de gravação
  única do upsell olhou só dinheiro." e "essa frase é verdade nos [...] mercados?" (revisão de copy e direção
  do upsell do A); "esse documento é importante ter só o texto para […] revisar e depois gravar" (Rodrigo).

### 4.15 Medir por oferta, não por produto — VARIAÇÃO ISOLADA (1 funil com número)

- **O que entra.** A taxa do upsell se mede pela oferta de um clique (o código da oferta na Hotmart) e na
  janela da compra. Contar quantos compradores do front compraram o curso mistura o um clique com compra
  posterior e com lançamento.
- **Os números que existem:**
  - **B** (debriefing do perpétuo): "Upsell [do curso]: 17 de 151 (11,3%), [entre o preço do downsell e o do
    upsell], 15 das 17 no mesmo minuto da compra." Upsell 2: 0 vendas. Reembolsos do upsell: 4.
    **Por oferta** (contagem feita pra este framework, no dia da extração, sobre as vendas normalizadas do
    debriefing, cruzadas com os nomes de oferta na Hotmart): **11 pela oferta "Upsell 1 funil", 5 pela
    "Downsell 1 funil", 1 pelo cheio**. Pelo tempo desde a compra do livro: das 11 do upsell, 9 saíram em até
    35 minutos, 1 cerca de 4 horas depois e 1 seis dias depois; as 5 do downsell, em até 20 minutos; a do
    cheio, cerca de 87 horas depois. O "15 das 17 no mesmo minuto" do debriefing é, no cálculo dele, o mesmo
    **dia**.
  - **As taxas, com a base dita:** na janela da compra (o mesmo dia), **10 de 151 no upsell (6,6%)**;
    contando a de seis dias, 11 de 151 (7,3%), que é o número do
    `sirius-scale/frameworks/lancamentos/perpetuo.md`. Downsell: **5 de 141** que não levaram o upsell no
    mesmo dia (3,5%); 5 de 140 (3,6%) se a base tirar as 11; 5 de 151 (3,3%) sobre todos os compradores do
    livro. Todas supõem que todos viram as duas páginas: ninguém mediu quantos viram cada uma.
  - ⚠️ **Divergência com o debriefing:** ele diz "Nenhum comprador do livro comprou [o curso] cheio" depois;
    a recontagem acha 1, pelo preço cheio.
  - **A** (desempenho do funil): 7,7% da base do front comprou o curso, mas é cruzamento de e-mail do
    período todo, e metade das vendas do curso nem passa pelo funil.
- **Por quê.** O debriefing do B achou uma análise anterior lendo compra posterior como upsell.
- **A régua.** A meta que o Rodrigo diz em voz alta é 20% no upsell e 15% no downsell; de onde ela vem não
  está em arquivo, e o único funil medido fica bem abaixo dela (6,6% e 3,5% na janela da compra). A faixa do
  prompt (5–20%) e a do roteiro do B (8–15%) são de mercado, não medidas aqui.
- **Variações aceitáveis.** Não há base pra uma segunda régua.
- **Trecho real.** "precisa dizer se é one-click com desconto ou compra posterior" (debriefing do B);
  "Metade do [curso] não vem do funil de upsell." (desempenho do A); "o take-up de referência (5–20%) é
  genérico de mercado, não medido aqui" (`sirius-scale/frameworks/copy/video-de-upsell.md`, cabeçalho); "E
  a gente testou só um vídeo de upsell, que tava vendendo o curso." (Rodrigo, numa call com o B); "aí também
  você quer ter 20% de conversão do upsell, 15% do downsell" (Rodrigo, numa consultoria).

### 4.16 Venda que trava no checkout do upsell — VARIAÇÃO ISOLADA

- **O que entra.** Quem tentou comprar o upsell e o pagamento travou recebe outra forma de pagar (Pix,
  entrada) na hora.
- **Por quê.** Era venda pronta: a compradora tentou três ou quatro vezes e o cartão foi bloqueado.
- **Variações aceitáveis.** No A, o gestor do projeto montou fluxos de WhatsApp com IA pra recuperar a venda
  do front e vender o upsell a quem levou só o front (follow-up em 2 h e 4 h); o Rodrigo achou as mensagens
  longas e pediu curtas (ata da call). No B, 2 das 17 vendas do curso vieram dias depois do livro e podem
  ter vindo por e-mail.
- **Trecho real.** Rodrigo, na call com o gestor do projeto do A: "Fala, dá uma entrada aqui, manda o Pix." e
  "Não pode perder a venda, velho." e "Se a mulher tá querendo, você não pode perder a venda."

---

## 5. Regras transversais (a força vai em cada regra)

1. **Toda frase do backend é conferida contra a oferta configurada e contra o que o front entrega**, na
   véspera de gravar e na de publicar. **Força:** PADRÃO CONSISTENTE (proposto): as correções dos 3 clientes
   foram quase todas desse tipo (§6).
2. **Escassez só a verdadeira**: a condição desta compra, o botão que some, o preço de fora. Nunca
   cronômetro, vaga, "a página sai do ar" ou "nunca mais". **Força:** PADRÃO CONSISTENTE (regra da casa, já
   marcada assim em `sirius-scale/frameworks/lancamentos/live-de-downsell.md` §2, item 2; fontes: a ficha
   de voz do expert do caso de origem, `sirius-scale/frameworks/oferta-14-secoes.md` §14,
   `sirius-scale/frameworks/lancamentos/low-ticket.md` §9), aplicada nos 3 clientes; o único desvio é a
   nota de edição do upsell 1 do B.
3. **Não listar os truques dos outros pra negar.** A régua nasceu na Seção 14 da VSL do C: "Nomear
   cronômetro e sorteio em três frases planta a ideia; em meia frase, sinaliza e passa." (mudanças da v2 da
   VSL). Lá ficou meia frase, que nega o cronômetro e o limite de pessoas de passagem (VSL v5,
   Seção 14). No upsell C1, aplicando a "mesma régua", a frase saiu inteira, também pra ganhar uns 3
   segundos (histórico da v1 do upsell C1). **Força:** VARIAÇÃO ISOLADA (C).
4. **O backend nunca vende como novidade o que o comprador já tem** (conteúdo, bônus, presente). **Força:**
   PADRÃO CONSISTENTE (proposto), 3 clientes (§4.9). No A: "Um bônus que o lead já possui é pior que fraco."
5. **"Metade" é intenção de preço; na copy vai o número.** **Força:** PADRÃO CONSISTENTE (proposto), 3
   clientes (§4.12).
6. **Sem culpa e sem confronto com quem recusou**, nem no link de recusa. **Força:** PADRÃO CONSISTENTE
   (proposto), 4 de 4 downsells e as 3 páginas com anexo.
7. **Parcela e prazo saem da plataforma.** Faltou, a fala fica marcada e entra como pick-up. **Força:**
   PADRÃO CONSISTENTE (proposto): os 4 roteiros do C com `[[INSERIR]]`; no A, parcela derivada e marcada
   pra conferir; no B, parcela errada no upsell 1 e no downsell (achado na revisão do briefing).
8. **Primeira pessoa, nenhum nome de aluno na fala** (nome só no marcador de produção, pra trocar
   depoimento sem regravar). **Força:** VARIAÇÃO ISOLADA: regra do C (decisão do Rodrigo); os roteiros do B
   nomeiam aluno.
9. **Nada que só é verdade num mercado vai no corpo gravado** (entrega física, valor em moeda de um mercado
   só). **Força:** VARIAÇÃO ISOLADA (A, gravação única em dois mercados).

---

## 6. O que mudou entre versões — PADRÃO CONSISTENTE (proposto): 10 de 12 correções foram de verdade, não de estilo

| Peça | De → para | Por quê | Fonte |
|---|---|---|---|
| C1, downsell | um pedaço do curso vendido sozinho, a cerca de um quarto do upsell → o mesmo curso, 6 meses, cerca de metade do upsell, com os bônus | o Rodrigo não reconheceu a decisão registrada antes | downsell C1 v1 e v2 |
| C1, upsell v1 → v2 | 3 âncoras → 2: saiu a âncora do pedaço do curso vendido sozinho | esse pedaço deixou de ser vendido sozinho | mudanças da v2 do upsell C1 |
| C1, upsell v1 | o fechamento que prometia resolver todos os exercícios do livro na frente da pessoa → o que o curso de fato mostra (o expert resolvendo prova real, um tipo de prova por vez) | overclaim derrubado pelo Rodrigo; bloqueio do `/revisar` | revisão do upsell C1 |
| C, 5 peças | botão falado → "clica no botão aqui embaixo" (o upsell C1 mantém) | texto do botão é da página | README do C |
| C1, upsell v1 | saiu a frase que negava cronômetro e vaga | a régua da Seção 14 da VSL (listar o truque planta a ideia; lá ficou meia frase) e 3 segundos de duração | histórico do upsell C1 v2 |
| A, upsell, 2º passe | [frase que dizia que um assunto não cabia no front] → [frase que diz que a aula do front não é brinde, é amostra] | o front já entregava a aula | direção do upsell do A |
| A, upsell | "quatro minutos" → "cinco"; frases que só valiam num mercado saíram do corpo; bônus que o front já dava saiu | duração real ~5:48; o corpo serve também à versão do segundo mercado; bônus repetido | idem e revisão de copy |
| A, downsell | "metade do preço" → "um preço bem menor" (o "metade do tempo de acesso" ficou) | o downsell é 58% do upsell | matriz de preços do A |
| A, página | preço anterior → 20% acima; saem a headline que entrega a oferta e o aviso de que ela nunca mais seria vista | o preço é a decisão do Rodrigo; o "nunca mais" briga com o downsell; a headline matava a curiosidade do vídeo | direção do upsell do A |
| A, gravação | número de autoridade dobrado na fala; preço na moeda do outro mercado diferente do roteiro (bloco não usado) | o expert falou diferente do roteiro | projeto de edição dos vídeos do A |
| B, upsell 2 v1 → v2 | erro técnico de conteúdo corrigido; bônus repetidos removidos | erro de conteúdo; bônus que o comprador já tinha | roteiro do upsell 2 do B |
| B, revisão do briefing | upsell 1 ancorado num cheio 20% abaixo do configurado na Hotmart; downsell anunciando um preço 12% abaixo do configurado; downsell terminando com frase do upsell 2 | roteiro e oferta configurada divergiam | briefing do funil do B |

**Leitura:** 10 das 12 linhas corrigem frase, número ou entregável que não batia com a oferta decidida, com
o produto ou com a gravação. As outras 2 são de produção (o botão fora da fala) e de persuasão (não listar o
truque). Nenhuma foi de estilo.

---

## 7. Exemplos consolidados, em molde

Fala de roteiro não vai literal: cada item diz o que a frase faz, e o colchete é o que vocês escrevem.

**Aberturas de upsell (a compra confirmada primeiro):**

> [Palavra de parada.] [Frase que pede pra não fechar a página.] [Frase que diz que o front já está garantido.]
> [Frase que diz que isto não é cobrança nem etapa pendente.] — C1 (frases curtas, em parágrafos separados)

> [Frase que diz que o curso já está garantido.] [Frase que diz que não falta pagar nada.] [Frase que avisa
> que o que vem agora é outra coisa.] — C2

> [Frase que diz pra quem o vídeo foi gravado: só pra quem acabou de fazer essa compra.] — A

**Teses (o formato do front, sem desvalorizar o front):**

> [Frase que contrapõe o que a pessoa faz no front ao que ela vê o expert fazer no upsell.] — C1

> [Frase que contrapõe quem faz em cada produto: no curso, o expert; nos exercícios do livro, a pessoa.] — C2

> [Frase que liga o conceito à aula que veio com a compra.] [Frase que diz que ela foi colocada ali de
> propósito.] — A

**Escassez verdadeira:**

> [Frase que anuncia honestidade sobre o botão.] [Frase que diz que é mecanismo, não pressão.] [Frase com o
> fato: o botão só existe com a compra aberta.] [Frase que diz o que acontece se a pessoa fechar a página.] — C1

> [Frase que esclarece o botão: ele existe com a compra aberta.] [Frase que diz o que muda ao fechar: ele some,
> e o produto volta ao preço de fora, pelo caminho normal.] — C2

> [Frase que nega a pressão e diz que é só a realidade.] — B, upsell 1

**Downsell: o que muda e o que fica:**

> [Frase que diz que o curso é o mesmo.] [Os módulos e as aulas, com número.] [Os bônus que vêm junto, com
> número.] — C1

> [Uma frase curta por item que fica: módulos, aulas, apostila, certificado, suporte.] — A (uma por linha no
> teleprompter)

> [Frase que oferece o curso completo.] — B, downsell

**Downsell: o fechamento:**

> [Frase que aceita a recusa e diz que o front já é da pessoa e funciona sozinho.] — A

> [Frase curta que manda clicar no botão.] — C1

---

## 8. O que é reutilizável e o que é do caso

### 8.1 O que transfere, porque já apareceu em mais de um cliente

- A escada: produto de entrada na frente, o upsell de um clique num formato diferente do front e com
  condição desta compra, o downsell só pra quem recusou (3 clientes).
- O downsell de curso como o mesmo curso com metade do acesso, sem tirar conteúdo, e o número na copy em vez
  da palavra "metade" (3 clientes).
- Conferir na plataforma e no que o front entrega antes de escrever, e de novo antes de publicar (3
  clientes).
- Abertura que confirma a compra, tese que elogia o front e mostra o que o formato dele não faz, escassez do
  botão, downsell não anunciado (3 clientes).
- O downsell curto, que acolhe o não, não re-vende e não usa prova (3 clientes).

### 8.2 Onde a casa vence o prompt externo — PADRÃO CONSISTENTE (proposto) nas 3 peças feitas por ele, menos a linha do Big Claim (VARIAÇÃO ISOLADA)

| O prompt manda | A casa faz | Por quê |
|---|---|---|
| Negação tripla ("não é A, não é B, não é C") | três negações de tamanhos diferentes | tríade sincronizada é proibida (ficha de voz do expert do caso de origem) |
| 3 a 4 âncoras, uma delas externa | 2 ou 3, todas verdadeiras; a externa não existe em nenhuma das 3 peças e isso vai declarado | `sirius-scale/REGRAS.md` §2 |
| Escassez repetida 3 vezes | as 3 menções são da mesma verdade (o botão, a página, o preço de fora) | não existe outra escassez verdadeira no backend |
| Atribuição com percentual ("80% do meu resultado") | atribuição singular sem percentual | o percentual não existe em arquivo |
| Vídeo de 4 a 5 minutos | 5:15 a 6:00 estimados (C1); 4:50 editado (A) | os pisos dos blocos do próprio prompt não cabem na meta: "a soma dos pisos declarados dos 11 blocos do prompt já é 5:55" (C1) e "somando o piso de cada faixa dos 10 blocos obrigatórios dá 5:25" (A) |
| Big Claim de autoridade | no C, sem número novo de autoridade, número de produto (a quantidade de exercícios do caderno) e a autoridade pelo ato. No A não se cumpriu: o número de autoridade guardado pro upsell já estava na VSL no ar | a autoridade da VSL já foi gasta e o número que faltava não existia. Só no C: VARIAÇÃO ISOLADA |

### 8.3 O que é do caso — VARIAÇÃO ISOLADA (não generalizar sem medir)

- **As taxas** (11,3% e a divisão em 11, 5 e 1 do B; 7,7% do A): um nicho, um produto e um preço cada.
- **A encenação de atendente** no downsell: vem de uma referência de mercado de outro nicho e foi adaptada à
  voz do C. O mecanismo é dele; nunca rodou.
- **As duas frentes** que transformam o preço de fora em fato: depende de o cliente ter dois produtos que
  podem ser front um do outro, no ar ao mesmo tempo.
- **A amostra como tese** (A): só existe quando o front já entrega um pedaço do backend.
- **A gravação única com bloco de preço por mercado**: só em cliente com frente num segundo mercado.
- **O upsell que desce o ticket** (curso → livro): uma peça, um cliente, não gravada.

---

## 9. Pontos em aberto

1. **Qual versão de vídeo e de página rodou no B.** O roteiro de upsell disponível tem 6 a 8 minutos,
   3 depoimentos, headline que entrega o desconto e âncora no preço errado. Se foi ele que fez os 11,3%, as
   regras do prompt que a casa aplicou no C e no A (até 6 min, depoimento opcional, headline sem
   spoiler) não têm prova a favor. Hoje é **PADRÃO INCONCLUSIVO** qual dos dois caminhos converte mais.
2. **Os vídeos novos do A estão no ar, e a que preço?** Aprovados pelo gestor do projeto; não há registro de
   página nova nem da oferta nova configurada. É a segunda medição possível da casa. Numa consultoria, o
   Rodrigo descreveu um funil com front físico e upsell do curso completo num preço que bate com o upsell do
   B; mas o front físico é o do A, e no A esse mesmo preço é o do downsell (o upsell está bem acima). Não dá
   pra saber de qual funil ele falava.
3. **O 2º upsell** do B chegou a ser exibido? Zero vendas sem saber se alguém viu.
4. **A taxa do downsell não tem denominador**: ninguém mediu quantos viram a página do downsell. A conta
   de 3,5% assume que todos os que recusaram o upsell passaram por ela (as bases das outras contas estão na
   §4.15). E a meta de 20% e 15% que o Rodrigo usa não tem fonte em arquivo.
5. **Preço do upsell:** a hipótese do Rodrigo de que o preço do upsell limita a taxa do B nunca foi testada.
6. **Como o um clique se comporta pra quem pagou o front no Pix.** Aberto no low ticket do C (pós-compra da
   linha) e no downsell do A ("O checkout do downsell é 1-clique ou pede o cartão de novo?"). O roteiro do B
   afirma que a condição de pagamento do front se repete no backend; não há conferência em arquivo.
7. **A escassez que sobrevive ao downsell** (A) e **o fechamento de baixa pressão** como redutor de
   reembolso (o A tem 6,9% de reembolso no curso): hipóteses, sem medição.
8. **Downsell de formato** (físico → digital, §4.6): decidido pro B, não rodou; no A é recuperação
   de carrinho, não um clique.
9. **Downsell de lançamento da próxima Black do B:** cursos separados a 50% do cheio, depois do combo.
   Rodrigo: "Faz um downsell, cara, os cursos separados." e "Dá um desconto de metade do preço, eu acho."
   Quantos dias de carrinho antes do downsell ficou em aberto. Quando rodar, o lugar dele é junto da
   `sirius-scale/frameworks/lancamentos/live-de-downsell.md` (downsell de lançamento), não aqui.
10. **Pontas soltas nos roteiros que vão pro ar:** as frases de ritmo de estudo sem dado nos downsells do
    B (2 a 3 meses) e do A (seis meses com folga); a nota de edição que sugere contador no upsell 1 do B; a
    duração real do upsell do C1 (só estimada).
11. **O slot vazio de upsell no low ticket** (§4.7) foi decisão relatada num turno da noite; não há
    aprovação do Rodrigo registrada.
