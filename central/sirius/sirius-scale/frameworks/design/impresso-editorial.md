# Framework — Material impresso com cara de designer (e-book, PDF de bônus, apostila)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método (execução visual de peça de várias páginas).
> **Alcance:** **NÃO TESTADO FORA** — 1 cliente (o caso-base, um expert de
> educação); 1 peça aprovada em direção (o 1º guia, dias 0 a 2) e 4 guias do
> expert em prova (dias 4 a 11), desde o dia 11 em texto corrido (§3).
> **Força:** VARIAÇÃO ISOLADA.
> **Datas:** contam a partir da primeira reprovação, o v0 do 1º guia, com
> "cara de IA" (dia 0, §1). "Dia 12" é 12 dias depois.
> **Onde mora cada coisa:** o *gosto* de cada cliente fica num `TASTE.md`
> próprio, em `frameworks-da-casa/`, com a folha de estilo (`estilo.css`) e os
> limites de gosto da conferência ao lado. O TASTE do caso-base não vem neste
> kit: é gosto de outro cliente. O *portão* é a conferência do §4: no caso de
> origem ele era um gerador da casa (HTML → PDF, sem PASS não saía PDF), que
> não vem neste kit; aqui ele está escrito como checklist, e o HTML vira PDF
> pelo próprio navegador (§3).
> Mesmo desenho que a casa usa em vídeo: arquivo de gosto + portão medido
> antes de mostrar.

---

## 0. Antes de diagramar: o cliente tem TASTE?

- **Tem** → ler o `TASTE.md` dele e **duplicar a última peça aprovada** que
  ele aponta. Nunca começar do zero.
- **Não tem** → passo 0: pedir referência a quem aprova, **ou** montar 2–3
  direções sobre a **página mais importante** da peça (a ferramenta, não a
  capa) e recomendar uma. Nunca entregar o "template padrão" primeiro: foi o
  que custou a reprovação do dia 0. A escolha vira o TASTE do cliente.

Não herdar o TASTE de outro cliente. O acento de cor ligado ao ofício do
expert e as notas com a fala dele são do caso-base (§5).

## 1. O que dá cara de IA (medido na reprovação do dia 0)

O v0 do 1º guia, nas palavras do Rodrigo: *"ficou com cara de IA"*. O que
ele tinha, e o que substitui cada item:

| Cara de IA | O que usar no lugar |
|---|---|
| Caixa com fundo pra tudo (exemplo, teste, dica, aviso): **16 numa página só** | fio fino (0,5 pt) e espaço; zero ou quase zero caixa |
| Faixa escura de título em cada bloco (cartão → faixa → corpo) | rótulo pequeno em caixa alta espaçada, sem fundo |
| Duas ou mais cores de destaque com o mesmo peso | **um acento só**, com função definida (o que ele marca) |
| Etiqueta/tag em todo elemento | referência só onde ajuda a navegar |
| Todo título no peso máximo (tudo grita) | hierarquia por tamanho, peso e itálico; uma família com personalidade nos títulos |
| Capa como banner de anúncio (bloco chapado, selo) | capa de livro: tipografia grande, respiro, assinatura discreta |

E o que faz parecer feito pra *aquela* pessoa: o **conteúdo real como
protagonista** (o exemplo da prova em destaque, a frase literal do expert na
margem), não a moldura.

## 2. Divisão de trabalho

- **Texto que o comprador lê** → agente `copy` (`sirius-scale/REGRAS.md` §3).
  O designer não escreve copy nem "melhora" texto do expert.
- **Conteúdo técnico** (questão de prova, gabarito, regra técnica) → o expert.
  Nunca inventado.
- **Diagramação, sistema, capa** → `designer`.
- O que falta fica **visível e marcado** na peça (`.pend`), com dono e o que
  falta, até alguém responder. Nunca preencher com suposição
  (`sirius-scale/REGRAS.md` §2).

### 2.1 Material que o expert escreveu: texto e nome intocáveis (dia 4)

Quando a peça é o material do próprio expert (e-book, guia, apostila que ele
mandou), a diagramação **não edita**. Nasceu de uma reprovação: o v1 do 1º
guia saiu com um nome nosso no título, com a ordem e os títulos do expert
trocados e páginas nossas sem marca. O Rodrigo: *"eu não posso simplesmente
alterar o nome do low ticket sem antes conversar com ela"* e *"o que for
sugestão, você tem que indicar bem claramente"*, no documento e no PDF.

- O arquivo dele fica guardado intocado numa pasta `original/`, dentro da
  pasta da peça, e a peça é **montada a partir dele** (o texto lido do .docx
  bloco a bloco), nunca redigitada.
- Texto dele = `.orig`; mapa ou infográfico dele redesenhado = `.orig-img` +
  transcrição da imagem. A conferência de fidelidade confere os dois (§4).
- Nome, título, série e assinatura são os do arquivo. Inconsistência entre
  peças (o nome dele escrito de três jeitos, por exemplo) vira pergunta, não
  padronização.
- Tudo que é nosso fica numa **camada de revisão visível e numerada**, em
  cor fora da paleta:
  - **C**: ponto do texto dele pra conferir, que continua como veio, mesmo
    quando é erro;
  - **S**: sugestão;
  - **D**: mudança de desenho que ele precisa saber.

  A prova abre com uma página de legenda e fecha com a lista pra ele marcar.
  O mesmo conteúdo vai num documento separado.
- Texto novo pro leitor final (página "como usar", promessa) só depois do ok
  dele, e pelo agente `copy`. **A página "como usar" foi vetada pelo expert do
  caso-base no dia 17**, depois de aprovada em princípio (dia 12) e lida
  pronta: "tal guia irá gerar dúvida para os alunos e, consequentemente,
  retrabalho para o atendimento". Página de método nossa dentro do material
  dele é risco de suporte, e quem decide é ele; não reapresentar sem ele
  pedir. VARIAÇÃO ISOLADA (1 expert, 4 peças). O que dependia dela (e-mail de
  boas-vindas, página de obrigado) caiu junto.
- **Material que chega em mais de um arquivo** (dia 17: os exercícios do 1º e
  do 2º guia vieram num .docx à parte do guia). Os dois ficam em `original/`,
  e uma lista (`ordem.txt`) diz quais entram e em que ordem; a conferência
  passa por um depois do outro. Toda correção dele passa a dizer o arquivo
  (`"arquivo": "<nome>"`). Sem a lista, dois arquivos de nome diferente são
  erro: no caso de origem, antes disso o portão escolhia o .docx e deixava o
  outro de fora, calado. O mesmo documento em .docx e .pdf (mesmo nome)
  continua sendo um só, e vale o .docx.
- **Correção pedida pelo próprio expert** (dia 12): o arquivo dele continua
  intocado; a troca entra num registro de correções do autor
  (`correcoes-da-autora.json`: código, de, para, quantas vezes, onde: `texto`
  ou `transcricao:<desenho>`, e a fonte: a mensagem ou o checklist dele). A
  conferência passa a comparar com "arquivo + correções" e trava se a troca
  não acontecer exatamente o número de vezes declarado. Texto que ele define
  fora do arquivo (a assinatura da capa) vai num campo à parte (a moldura do
  autor). **Se a correção dele cria erro novo** (rótulos trocados, frase sem
  oração principal, advérbio sem verbo), não aplica o erro nem conserta
  calado: aplica o que está certo e volta pra ele com a correção mínima pronta
  pra sim ou não. VARIAÇÃO ISOLADA (1 expert, 4 peças, 19 correções; 4
  voltaram como pergunta).
- **Pedido do expert numa peça que ele aprovou muda só o que ele pediu** (dia
  13). Ao trocar a assinatura da capa (pedido do expert), a linha de série da
  capa aprovada (D3 "ok") saiu junto, sem ele pedir; um revisor pegou e
  voltou. Elemento aprovado que sai é item aprovado saindo do lote (regra da
  casa; foi o 2º caso). Dá pra virar checagem: comparar o texto da capa da
  proposta nova com o da última aprovada.
- **Na entrega pro comprador, redesenho sem o ok do expert não substitui o
  original** (dia 35). O mapa mental do 1º e do 2º guia foi redesenhado (S2),
  ficou sem resposta do expert desde o dia 12, e o PDF de entrega saiu com o
  redesenho no lugar da imagem dele: a versão de proposta aplica a sugestão
  como versão final, e a conferência final só trava o que está marcado
  `.sug`/`.pend`, não um desenho que trocou o do expert. Ele achou que faltava:
  nos dois livros, os mapas mentais que estavam nos arquivos enviados como
  bônus. Resolvido com a imagem dele inteira numa página depois da capa e o
  redesenho mantido, como ele pediu ("seria apenas acrescentar os mapas
  mentais"). Regra: enquanto a sugestão que troca material dele não tem
  resposta, a entrega leva o original. VARIAÇÃO ISOLADA (1 expert, 2 peças).
  Dá pra virar checagem: a conferência final recusar marca S/D pendente cujo
  trecho substitui `.orig`/`.orig-img`.
- **Desenho refeito vai em `.folha`, nunca em `.prancha`** (dia 12). A
  `.prancha` tem a altura fixa da área útil, feita pra esticar a imagem do
  expert; o que passa dela cai por cima da página seguinte. O mapa redesenhado
  do 2º guia fez isso (o resumo em cima do título do "como usar") com o portão
  em PASS, e daí nasceram as duas travas do §4, item 7.

## 3. Pipeline

1. A peça é HTML com a folha de estilo do TASTE do cliente
   (`<link rel="stylesheet" href="…/estilo.css">` — nunca copiar o CSS pra
   dentro da peça). Material do expert: o HTML é montado a partir do arquivo
   dele, com os componentes do TASTE (§2.1). Dois modelos de página:
   - **Texto corrido (padrão desde o dia 11):** sem `.page`. O texto corre e o
     Chrome pagina sozinho pelo `@page { size: A4; margin: … }` do estilo, com
     a mesma margem em todas as páginas. Cabeçalho e rodapé nas caixas de
     margem (`@top-left`, `@bottom-right`…), com texto que existe no arquivo
     do expert. Abre página (`break-before/after: page`) só o que é de abrir
     página: capa, rosto, revisão, carta, sumário, página sugerida inteira,
     lista de validação. Número de página que depende do layout (sumário,
     lista) é `<a href="#alvo" data-pagina>`: imprime uma vez, lê no PDF onde
     o alvo caiu e escreve o número numa segunda passada.
   - **Folha fixa (até o dia 6):** uma `<section class="page">` por página A4,
     conteúdo distribuído à mão. Sobrava página pela metade (a reclamação do
     dia 11). Fica pro que é mesmo uma folha só (pôster, cola avulsa).
2. **O HTML vira PDF pelo navegador:** Chrome sem janela (headless, com
   `--print-to-pdf`) ou a impressão em PDF do próprio Chrome (tamanho A4,
   margens as do CSS, sem os cabeçalhos e rodapés do navegador, com os
   gráficos de plano de fundo ligados).
3. Checklist do §4 limpo → mostrar a **folha de contato** (todas as páginas
   numa imagem só). Quem aprova revisa pelo celular: folha, não descrição (no
   caso de origem, o Rodrigo).
4. Entrega pro comprador só com a conferência final (§4, item 6) limpa.

Convenção de marcação (o portão do caso de origem lia essas classes, e é ela
que deixa a conferência possível, à mão ou pelo Claude): `.page` (folha fixa),
`.foot` (rodapé da folha fixa), `.pend` (pendência interna), `.prov` (capa
provisória), `.orig`/`.orig-img`/`.moldura` (fidelidade, §2.1),
`.sug`/`.sug-pagina`/`.sug-marca` (camada de revisão) e `a[data-pagina]`
(número de página calculado, texto corrido).

## 4. O portão

**Sem o checklist limpo, não sai PDF.** Confere-se dentro do Chrome, depois
das fontes carregarem: à mão, no PDF e na folha de contato, ou pedindo ao
Claude que leia o HTML renderizado e o PDF e meça.

No texto corrido, confere-se **o PDF impresso**, não o HTML, porque a página
só existe depois de impressa (e o número de página pede duas passadas: a
primeira lê onde cada coisa caiu, a segunda escreve os números).

**Trava (FALHA):**

1. **Estouro:** folha fixa — conteúdo por cima do rodapé, dentro da folga
   mínima, ou fora da folha. A página tem `overflow:hidden`, então no PDF o
   texto é cortado sem aviso. Aconteceu no dia 2 (o passo 8 do 1º guia sumiu)
   e o v0 tinha dois estouros que passaram na conferência pela imagem. Texto
   corrido — duas checagens no PDF, vindas da edição celular do dia 6 (§6):
   **documento encolhido** (o texto mais comum do PDF tem de ter o tamanho que
   tem na página; procurar a peça mais larga que a área útil) e **texto fora
   da área útil** (na margem só pode estar o `content` das caixas de margem).
2. **Fonte:** família usada no texto que a página não carregou. Se o Google
   Fonts não responde, o Chrome troca pela do sistema sem avisar. É a mesma
   família de erro do libass trocando a fonte no vídeo
   (`sirius-scale/frameworks/copy/edicao-video-criativos.md`).
3. **A4:** página fora de 210 × 297 mm, ou PDF com número de páginas diferente
   (folha fixa); toda página do PDF em 210 × 297 mm e margem igual em todas
   (texto corrido). E **número de página**: cada número impresso num
   `a[data-pagina]` tem de ser a página do destino do próprio link. Número
   errado é pior que número nenhum.
4. **Imagem:** `<img>` que não carregou.
5. **Fidelidade** (peça com `original/`): cada palavra do texto `.orig` tem de
   bater com o arquivo do expert, na ordem. O `.docx` é lido por bloco. No
   PDF, o cabeçalho e o rodapé que se repetem viram moldura e saem da
   comparação. Cada `.orig-img` tem de bater com a transcrição da imagem.
   Todo texto sem marca (cabeçalho, rodapé, capa — no texto corrido, também o
   `content` das caixas de margem) tem de existir no arquivo dele ou no nome
   do arquivo. Pega palavra trocada, título reescrito, nome trocado e item
   faltando no desenho.
6. **Conferência final** (antes de ir pro comprador): nenhuma pendência, capa
   provisória, marca de revisão (`.sug`), `[[ ]]` nem "rascunho interno / não
   distribuir" (no texto corrido, também no rodapé das caixas de margem, que
   não está no DOM).
7. **Impresso de verdade** (texto corrido, dia 12): a fidelidade do item 5 lê
   o DOM, e o DOM pode ter o que a folha não mostra. Por isso, no PDF:
   **palavra do texto fiel que não chegou** (`.orig` e desenhos, menos o
   `.oculto`; pega corte por altura fixa ou `overflow:hidden`, que o Chrome
   descarta do PDF) e **texto por cima de texto** (duas linhas que se cobrem
   em 20% da altura ou mais; linhas normais se tocam no máximo 4%, medido nos
   4 livros digitais do caso-base, e a sobreposição real do mapa do 2º guia
   deu de 28% a 100%). A conferência fecha dizendo "as N palavras do texto
   fiel estão no PDF".
8. **Páginas declaradas:** a peça que diz quantas páginas tem (um checklist de uma folha só, um guia de 10 páginas)
   tem de sair com esse número. Sem essa checagem, se o texto cresce, a 2ª página passa, porque o aviso de branco não
   olha a última página. Declare o número no HTML (ex.: `<meta name="impresso-paginas" content="1">`) e confira no PDF.

**Avisa (gosto; os limites ficam no TASTE do cliente):** mais famílias de cor
de destaque que o sistema permite; mais caixas com fundo por página que o
permitido; e, no texto corrido, **branco no meio do texto** — página com menos
de 60% da área útil ocupada (o uso mínimo da página) cuja página seguinte não
abre com quebra forçada (bloco que não parte, empurrado pra frente). É aviso e
não trava porque é heurística (às vezes o branco é o preço de não partir um
mapa). Vale anotar o uso da área de cada página. Quem decide gosto é quem
aprova, na folha (no caso de origem, o Rodrigo).

**Teste:** no caso de origem, cada checagem do portão tem uma peça boa que
passa e uma peça ruim pra cada defeito, mais o v0 real; no texto corrido, as
peças de teste são a boa, a larga demais, a com texto fora da área útil, a com
branco no meio e a de fidelidade, mais variações estragadas delas. Se vocês
automatizarem alguma checagem, a regra é a mesma: ela só entra com um caso
ruim que a faça falhar.

**O que ele não mede:** se a tipografia está bonita, se o exemplo escolhido é
o melhor, se a capa vende. A cada reprovação nova, a pergunta é "dá pra
medir?". Se dá, entra no portão, com o caso ruim que a prova.

## 6. Leitura no celular: uma versão só, A4 com letra maior (decisão do Rodrigo, dia 11)

**O problema, medido no 3º guia do caso-base (dia 6).** Com o A4 inteiro na
tela do celular, a página fica a ~0,65 do tamanho: o texto de 9,7 pt aparecia
com 6,4 pt, as questões (8,9 pt) com 5,8 pt, e a Apple recomenda no mínimo 11.
O Rodrigo viu isso abrindo o link no celular.

**A edição celular foi recusada.** O protótipo do dia 6 (a mesma peça numa
folha de 90 × 160 mm, o texto aparecendo com ~15 pt sem zoom) resolvia a
leitura, mas criava duas versões. O Rodrigo, no dia 11: *"não acho que deve
ter duas versões [...] tem que ter uma versão focada na impressão mesmo, só
que não pode ser tão pequena ao ponto de ficar ruim de olhar pelo celular
[...] tem que preencher melhor a tela, talvez aumentar um pouco a fonte [...]
pode deletar a versão do celular."* O protótipo foi arquivado, e as três
checagens que valiam (folha do tamanho certo, documento encolhido, texto fora
da área útil) entraram no portão.

**O que ficou:** A4 em texto corrido (§3), uma coluna na largura da página,
corpo de 12 pt (aparece com ~7,9 pt na tela, era 6,4), sem página pela metade
fora das quebras de abrir página. Não chega aos 11 pt da Apple sem zoom (pra
isso o corpo teria de ir a ~17 pt e o impresso viraria livro de letra
gigante); é o meio-termo que o Rodrigo pediu. Os números e o porquê de cada
escolha ficam no TASTE de cada cliente. **VARIAÇÃO ISOLADA** (4 peças de 1
cliente; ele ainda não tinha visto o resultado quando isto foi escrito).

**Armadilhas do Chrome ao imprimir (UNIVERSAL, medidas; valem pra qualquer peça):**
1. **Um elemento mais largo que a página encolhe o documento INTEIRO**, não só
   a página dele (dia 6: os mapas em grade de 3 e 4 colunas do 4º guia
   derrubaram o texto pra 6,3 pt). Medir a largura com a página presa por CSS
   (`html,body{width:<largura útil>}`), porque o Chrome sem tela no Mac não
   abre janela com menos de 500 px. As caixas de margem (cabeçalho/rodapé) não
   encolhem junto.
2. **Acento de maiúscula no topo de uma página é pintado no pé da página
   anterior** (o "Ã" de uma palavra em caixa alta, dia 6). No PDF, a linha
   inteira aparece no pé da página de cima, atravessando a borda da área útil.
   Um respiro em cima do título (`padding-top`) resolve.
3. **Extração de texto do PDF:** título com espaçamento largo entre letras sai
   soletrado ("e x e m p lo :") — no celular, a busca e a cópia do texto
   quebram; manter o espaçamento de rótulo em caixa alta em no máximo ~.06em.
   Palavra com hífen quebrada no fim da linha sai partida, com recuo depois da
   quebra.
4. **`counter-reset` num título do meio do documento não reiniciou a
   numeração** (a parte II do 2º guia saiu 7 e 8); `counter-set: <contador> 0`
   funcionou.
5. **Caixa de margem: a declarada por último vence** (dia 11, Chrome 154). Um
   `@page :first { @top-left { content: none } }` declarado ANTES do
   `@page { @top-left { content: "…" } }` não desliga nada, apesar de `:first`
   ser mais específico. O desligar (capa, página nomeada sem cabeçalho) vem
   depois do conteúdo. Página nomeada (`page: nome` + `@page nome {}`)
   funciona.
6. **`string-set` não existe no Chrome**: o cabeçalho corrido não muda por
   seção. Cabeçalho fixo.
7. **O `@page` de uma folha de estilo local não se lê pelo CSSOM** sem
   `--allow-file-access-from-files` (o Chrome trata cada arquivo como origem
   própria). Com a flag, `CSSPageRule` e `CSSMarginRule` (com o `content` de
   cada caixa) aparecem.
8. **Link interno vira destino com nome no PDF**, com a página:
   `<a href="#x">` faz o Chrome gravar o destino `x`, e o PyMuPDF lê com
   `doc.resolve_names()`. É assim que se sabe em que página cada coisa caiu. O
   `document.title` vira o título do PDF (canal pra passar dado de uma passada
   de medição).
9. **Fundo:** o fundo do `html` só pinta a área útil; `@page { background }`
   pinta a folha inteira, margem incluída. `box-decoration-break: clone`
   funciona em bloco partido entre páginas (cada pedaço leva a borda inteira),
   e o `thead` se repete quando a tabela continua na outra página.
11. **Capa sangrada (dia 17; a capa que pediu isso não ficou, voltou a
    anterior no dia 19, mas a técnica vale):** o Chrome corta na margem da
    página tudo o que não é a cor de fundo do `@page`: o elemento posicionado
    pra fora some, e até o `background-image` do `@page` fica preso na área
    útil. Cor e desenho só chegam na borda com uma página nomeada sem margem
    (`@page capa{margin:0}` + `page: capa` na seção, que leva o próprio fundo,
    porque o do `html` cobre o do `@page`). O portão aceita margem própria SÓ
    pra página `capa`, confere que o texto dela fica dentro da área útil das
    outras páginas e deixa a paleta dela fora do limite de cor de destaque
    (que é do miolo).
12. **Nome de classe que já existe no estilo.css (dia 17):** a tabela longa
    marcada `.parte` (pra continuar na página seguinte) herdou o estilo do
    título `.parte` do 2º guia: negrito, espaçamento entre letras, margem de
    título. O quadro de exemplos do 4º guia saiu assim na proposta do dia 13,
    e ninguém viu por uma semana. Virou `.continua`. Antes de batizar classe
    nova, procurar o nome no estilo.css. Frágil (não virou checagem): o portão
    não sabe qual estilo cada elemento deveria ter.
13. **Página de resumo que a venda promete "numa folha só" (dia 21, VARIAÇÃO
    ISOLADA, 1 peça: o mapa mental do 1º guia):** o mapa redesenhado no dia
    17 correu por 3 páginas, e a página de vendas, a descrição da Hotmart e
    uma arte de anúncio diziam "numa página". Em vez de mexer na promessa, o
    mapa voltou pra uma página só, com a abertura dele em cima: corpo a 7 pt
    (é a densidade da imagem original do expert impressa em A4, medida pela
    altura da linha) e os 8 primeiros cards em **colunas que correm**
    (`column-count:4` no grupo, card com `break-inside:avoid`), em vez de
    grade: a grade paga a altura do card mais alto de cada linha, e a coluna
    não (economizou ~14 mm, que fez a última seção caber). A ordem de leitura
    fica 1-2 | 3-4 | 5-6 | 7-lembre, natural com os números. Seções curtas em
    grade de 4 e 5 colunas, a "Dica final" numa faixa. Conferir em 150 dpi que
    o 7 pt lê bem antes de mandar. **Regra que fica:** quando a peça muda de
    tamanho, procurar as promessas de tamanho dela fora do PDF (página,
    Hotmart, anúncio, arte) antes de decidir entre mudar a peça ou a promessa.
10. **Fonte Type3 no PDF do Chrome:** o PyMuPDF lê a cor do texto como preta
    (0) em quase todo trecho; não dá pra separar texto por cor no PDF (a
    camada azul da revisão, por exemplo). Separar pelo DOM.

## 5. O que transfere e o que é do caso

**Transfere** (mecânica, não depende do nicho):
- a lista do §1;
- o passo 0 das direções;
- o pipeline HTML → portão → folha → PDF, em texto corrido (§3) — e as
  armadilhas do Chrome do §6;
- a divisão de trabalho;
- a pendência visível no lugar de buraco preenchido;
- a regra do §2.1 com a checagem de fidelidade: vale pra qualquer expert que
  mande o próprio material;
- um TASTE por cliente, em `frameworks-da-casa/`, que nunca se herda de outro.

**É do caso** (caso-base): serifa + Inter + letra à mão; um acento de cor só,
tirado do ofício do expert (vale porque a cor remete à credencial dele); a
coluna de notas com a fala literal dele. Essa coluna só funciona pra expert com
voz forte **e** transcrição disponível. Cliente sem transcrição não tem de onde
tirar nota, e aí a margem fica vazia ou sai do sistema.

Quando um segundo cliente passar pelo passo 0 e aprovar uma peça, o que se
repetiu entra aqui, e o alcance sobe pra `TESTADO EM 2 CLIENTES`.

## Revisão com o expert: PDF proposto + documento à parte (decisão do Rodrigo, dia 11)

Decisão do Rodrigo depois de ver os quatro livros digitais do caso-base com a
camada azul no meio do texto ("fica ruim esses montes de comentário em
azul"): o expert recebe **a versão final que a gente propõe, sem nada azul**,
e os comentários vão num **documento "o que conferir" por peça**, com o
checklist no fim. Ele bate o olho no PDF; se algo gerar dúvida, acha o ponto
no documento pelo código, pela página e pelo trecho. Responde por áudio.

- **PDF de proposta:** esconde todo `.sug` e as páginas de revisão, mantém as
  páginas sugeridas sem a faixa, e não pode sobrar rótulo de revisão
  ("Conferir ·", "Sugestão ·"…) no texto do PDF: buscar esses rótulos no PDF
  antes de mandar. Número de página escondido não conta como alvo da
  conferência.
- **Documento "o que conferir":** sai do mesmo HTML (notas `.sug.nota`,
  marcas `.sug-marca`, lista de validação), com a página de cada ponto achada
  no PDF da proposta.
- O texto do expert continua intocado na proposta: ponto C (possível erro
  dele) fica como veio e só aparece no documento. VARIAÇÃO ISOLADA (1 expert,
  4 peças).
- **Rodada seguinte não sobrescreve o documento** (dia 12). Depois que o
  expert marca o checklist, o documento é dele: as marcações moram lá (o
  histórico mostrava o expert como último a editar os quatro). A versão nova
  do PDF entra no mesmo link; o que ainda falta vai num **documento novo, um
  só pra todas as peças**, só com os pontos abertos, cada um com a correção
  mínima proposta pra ele marcar sim ou não, e um resumo curto do que já
  entrou. Página sugerida na proposta sai sem a moldura tracejada azul (a
  versão de proposta tira a borda da `.sug-pagina`).

## Revisão de livro inteiro: documento numerado + prova marcada — *VARIAÇÃO ISOLADA (1 livro, 11/2026)*

Com muitos pontos em material pronto (no caso, mais de cem num livro de ~200 páginas), aplicar tudo antes da resposta do expert seria
trabalho dobrado, e ele teria de caçar cada trecho na página. A revisão vai em dois arquivos, com a mesma numeração:
- **Documento:** uma coluna em branco por ponto, para o que ele quiser mudar. Ele também pode comentar no PDF ou mandar
  áudio citando o número.
- **Regra do silêncio, combinada com o expert antes de enviar:** quem concorda não precisa responder, e o ponto sem
  resposta entra como proposto. Ponto sem proposta fechada vem marcado "Precisa da sua resposta" e fica como está se ele
  não responder. A conferência final do livro inteiro continua depois, antes da gráfica.
- **Prova marcada:** cada folha traz a página com os pontos grifados e, ao lado, como está, a proposta e a observação. Só
  entram as páginas com ponto. Nada altera o livro: a página entra inteira, com o grifo por cima.
- Ordem dos blocos: primeiro o que muda o que o leitor aprende, por último a digitação. Bloco aprovado de uma vez pede
  revisor de olhos frescos antes de ir.
- Decisão da operação (CTA, gráfica, ISBN, preço) não entra: fica nas NOTAS.
- **Depois da aprovação, o arquivo fecha.** Correção nova vai pra uma versão 2.0; no arquivo entram só ficha
  catalográfica, código de barras e o que o órgão do ISBN pedir.
- **ISBN e ficha pela CBL** (fato da plataforma, *UNIVERSAL*, lido no Portal de Serviços da CBL em 11/2026): a Lei
  10.753/2003, art. 6º, pede o ISBN e a ficha catalográfica, e o número do ISBN vai na quarta capa. A ficha pode ser
  pedida junto com o ISBN; pela tabela, o ISBN sai em 2 dias úteis e a ficha em 1. A ficha sai no nome do titular do
  ISBN, e o titular (CPF ou CNPJ) não muda depois de emitido: antes do pedido, confira que ele é a editora que a folha
  de rosto imprime. O código de barras é o próprio ISBN-13 em EAN-13: dá pra gerar a partir do número em vez de comprar
  o arquivo, em PDF vetorial só em preto, com fundo branco cobrindo as zonas claras (entra em capa de qualquer cor), e
  lido de volta por um leitor de código de barras antes da gráfica. Fontes: `cblservicos.org.br/catalogacao/perguntas-frequentes-ficha/`
  e `cblservicos.org.br/precos/`.

**Armadilhas de editar o PDF do InDesign aplicando os pontos** (medidas num livro):
- O InDesign pode mapear um caractere pra "�" numa fonte embutida: a letra sai certa na página e quebra a busca. Escolha a
  fonte letra a letra, preferindo a que tem a letra no mapa de texto.
- **Itálico falso:** a fonte reta com a matriz inclinada. O extrator não mostra; sem ler a matriz, a linha refeita sai reta.
- **Ligadura fi/fl:** o extrator devolve "f" e um "i" sem avanço; reescrever as duas letras separadas deixa "classif cação".
- Corpo da linha pela moda, não pelo máximo; espaço novo numa linha justificada pega a largura dos espaços daquela linha.
- Troca que não cabe refaz o parágrafo a partir da linha dela e para quando a quebra volta a coincidir; parágrafo que
  encolhe sobe o texto abaixo, sem buraco; antes de repaginar uma seção, ache onde ela termina de verdade.
- Página de altura diferente (capa): converta a posição pela matriz da própria página.
- Fonte de display da capa com subconjunto: só tem as letras que a capa usa. Letra nova pede a mesma família noutro peso
  que tenha a letra.
- "Nome completo em todas as páginas" é varrer o miolo e a capa inteira (frente, lombada, quarta capa, orelhas).
- **Imagem sem original em alta:** ampliação fiel sem IA é a opção segura; redesenho por IA muda o desenho e vai pra
  conferência do expert, comparado lado a lado com o original.
- Cada rodada de correção entra no mesmo script de aplicação (nunca remendo no PDF já saído), e o diff contra a versão
  anterior tem de mostrar só as páginas que mudaram.
## PDF final do InDesign sem o arquivo aberto (dia 47)

Caso: um livro de cerca de 200 páginas do caso-base (InDesign 21.4, sem o `.indd` à mão), com o sumário
feito à mão e 2 páginas atrás do miolo. VARIAÇÃO ISOLADA (1 peça).

- **Antes de pedir o arquivo aberto, medir o PDF:** fonte embutida? Texto vivo ou imagem? O número está
  num `Tj` só? Nesse livro cada linha é um comando de texto, com as fontes TrueType em WinAnsi, então
  trocar um número é trocar o texto dentro do stream da página.
- **Salvar incremental.** O arquivo novo começa com o original inteiro, byte a byte, e a conferência
  compara as páginas por pixel: fora das páginas tocadas, nada pode mudar.
- **Sumário manual se confere por três caminhos:** ler o sumário do PDF corrigido, procurar cada título
  na página apontada (texto do PDF + OCR do que é imagem) e olhar o que sobrar. O OCR do Vision, no Mac,
  vem sem correção de idioma (`usesLanguageCorrection = false`), e isso importa em revisão: ele não
  conserta o erro que se quer achar.
- **Largura do dígito:** na Garamond-Bold o "1" é mais estreito (396 contra 469). Número em direita
  alinhada compensa com kerning no `TJ`. Número que ganha dígito tira pontos do pontilhado.
- **Texto em imagem é o limite real.** Quadro que veio como imagem não muda no PDF, e pode nem mudar no
  `.indd`, se o arquivo de origem do quadro não vier junto. Por isso o pedido a quem diagramou é o pacote
  do InDesign (com os links), não só o `.indd`.
- **Versão antiga é fonte.** Uma versão anterior, ainda em Word, tinha os quadros como texto. Foi dela
  que saiu um quadro que a rediagramação perdeu e a explicação certa de um item. Diff com versão
  anterior acha o que leitura corrida não acha: um fecha-parêntese perdido, reticências que viraram
  ponto.
- **Boxes novos no branco da página** usam as fontes que o PDF já embutiu e não mudam paginação, sumário
  nem lombada. Só funciona se todo caractere existir no subconjunto da fonte: a montagem tem que parar
  se faltar.
