# Estático de anúncio montado em HTML → PNG

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de execução (designer).
> **Alcance:** NÃO TESTADO FORA. A base é uma leva (a 5ª leva de estáticos dos produtos de entrada do caso-base, um
> expert de educação, montada em dois dias). O item 4 é comportamento do navegador (UNIVERSAL).
> **Quando usar:** a arte é feita de peças reais (capa, página do PDF, foto do expert, logo) e o texto vem pronto do
> agente `copy`. Monta em HTML, renderiza no Chrome e passa num portão antes de virar PNG. Não vale pra arte gerada por
> IA, que segue o fluxo de imagem do agente `designer` (`.claude/agents/designer.md`).
> **Como o caso de origem fez:** um script monta o HTML de cada peça; outro renderiza o PNG, roda o portão e monta a
> folha de contato; um teste estraga uma peça boa de 5 jeitos e confere que o portão reprova; e um quarto refaz uma
> peça existente mudando só a logo. Esses scripts não vêm neste kit. O que vem é o que eles conferem, escrito como
> checklist: dá pra conferir à mão ou pedir ao Claude que leia o HTML renderizado e meça.

## O portão (o que já é checagem)

Antes de sair PNG, confira:
- **texto:** cada texto renderizado contra a tabela da copy aprovada (no caso de origem, um `esperado.json`), e o texto
  do guia que aparece na arte contra o arquivo do expert, palavra por palavra;
- **tamanho:** letra de pelo menos 34 px, margem de 50 px, logo de pelo menos 560 px;
- **composição:** nada sobreposto, fontes carregadas.

O teste no caso ruim prova que o portão reprova: acento tirado, logo com 480 px, fonte quebrada, faixa sobre a foto e
título fora da margem. Se vocês automatizarem alguma dessas checagens, ela só vale depois de reprovar uma peça ruim
feita de propósito.

## Quatro armadilhas medidas que o portão NÃO pega

1. **"Logo de 560 px" não é uma altura só** (*VARIAÇÃO ISOLADA*). As logos dos 4 livros digitais têm proporção de 2,5:1
   a 4,5:1. A 560 px de largura, a altura vai de 224 a 125 px. O pé de cada peça, onde a logo mora, se mede por livro;
   não se copia de uma peça pra outra.
2. **Página atrás da capa mostra uns 45% dela** (*VARIAÇÃO ISOLADA*). Com a capa no tamanho do molde, a parte da
   direita da página some. Escolha a página pelo que aparece na metade da esquerda, ou reduza a escala (num dos guias,
   a página foi a 1,08×; noutro, 1,46×). A página é prova visual: o que precisa ser lido vai no rótulo grande.
3. **Seta branca sobre papel branco some** (*VARIAÇÃO ISOLADA*). A ponta da seta termina no fundo colorido, nunca em
   cima da página.
4. **O Chrome quebra a palavra no hífen** (*UNIVERSAL, comportamento do navegador*). "segunda-feira" ou
   "bem-vindos" no fim da linha viram "segunda-/feira" e "bem-/vindos"; o caso medido foi um verbo com pronome
   ligado por hífen. Na frase da peça, envolva com `white-space: nowrap`. É vizinha das "Armadilhas do Chrome ao
   imprimir" de `sirius-scale/frameworks/design/impresso-editorial.md`.

⚠️ Frágil: nenhuma das quatro virou checagem. Depende de quem monta ler isto.

## Foto recortada sobre fundo escuro e rosto na frente da headline (toscão da Black, no dia em que a captação abriu)

No caso de origem: um script de recorte (RVM), um de montagem, um de render e um teste do portão. Três armadilhas
medidas na mesma tarefa:

1. **O RVM deixa o fio da borda com a cor do fundo de estúdio** (*VARIAÇÃO ISOLADA*, sessão de fotos do expert do
   caso-base). Sobre preto vira contorno claro no topo da cabeça e véu arroxeado entre os fios. Pintar a borda com a
   cor do interior vizinho tirou o contorno, mas atrás da orelha, numa das fotos, o vizinho era a orelha e o cabelo
   virou mancha cor de pele. O que ficou: desfazer a mistura com o fundo estimado (pele, blusa) e, no cabelo escuro,
   cor do cabelo vizinho com o alpha recalculado. Conferir em 100% sobre preto, branco e ouro, não só sobre a cor da
   peça.
2. **EXIF errado numa das fotos da sessão** (*VARIAÇÃO ISOLADA* no arquivo; o comportamento é *UNIVERSAL*): a tag diz
   girar 90°, o pixel já está em pé. O Chrome respeita EXIF num `<img>` e `ImageOps.exif_transpose` também: a foto sai
   deitada. Ler o pixel sem EXIF; o PNG do recorte sai sem a tag.
3. **Rosto na frente da headline se mede por letra, não por linha** (*VARIAÇÃO ISOLADA*). Um "EXCLUSIVO" de teste
   passou com 20% da linha coberta, mas o L perdeu 51% (sem o pé, vira I) e o U 68%. Virou checagem: o alpha real da
   foto na peça sai de duas capturas (foto sozinha sobre preto e sobre branco, já com a máscara do CSS), a tinta da
   headline de uma terceira, e o portão reprova letra acima de 45% escondida (teto da coordenação, decidido no dia
   seguinte, a véspera do tráfego pago).
4. **Gesto de braço esticado não aceita esfumado na base** (*VARIAÇÃO ISOLADA*, captação da Black, véspera do tráfego
   pago). Nas fotos de estúdio do caso-base, apontar e oferecer a palma fazem um V: ombro, cotovelo lá embaixo do
   quadro, mão pra cima, a quase duas alturas de cabeça do rosto. Esfumar a base apagou o cotovelo e deixou a mão solta
   no ar (A2). O que resolveu: cortar a foto (clip-path) na borda de uma faixa opaca, a do rodapé e do botão, com fio
   de ouro em cima; o antebraço "passa por trás" dela. No caso de origem, a montagem do A2 e do N2 faz isso, com teste
   do portão (`sirius-scale/frameworks/design/captacao-da-black-arte-do-estatico.md`).
5. **Degradê recortado no texto corta o acento** (*UNIVERSAL, comportamento do navegador*; visto na véspera do tráfego
   pago no BÔNUS do N1). Com `background-clip: text` o fundo só pinta dentro da caixa da linha; com `line-height: 1`,
   o circunflexo do Ô fica acima dela e sai como uma barra reta. Conserto: folga vertical na linha (`padding: .32em 0`)
   e as paradas do degradê em `em`, não em %, pra a cor cair no mesmo ponto da letra (a A1 aprovada saiu idêntica,
   diferença máxima de 1 nível de cor). Virou checagem: o portão compara, letra por letra, a tinta da headline numa
   captura em branco puro com a peça, e reprova letra que perde mais de 6%.
6. **Texto que vaza da caixa colorida** (*VARIAÇÃO ISOLADA*, A3, véspera do tráfego pago). No story, "NA BLACK" e
   "Vitalício" passaram da borda da coluna de ouro e o portão não via (o medidor guardava a caixa de cada texto, mas
   nenhuma regra conferia). Virou checagem: texto com `data-dentro` fica dentro da caixa com 6 px de folga, e o layout
   encolhe o texto da coluna até caber.
7. **Comparativo em que a foto encosta no quadro foi reprovado** (*VARIAÇÃO ISOLADA*, Rodrigo, véspera do tráfego
   pago: "ficou um pouco confuso, misturou muito... evidenciar o quadro"). A v1 tinha a foto em cima da coluna NA BLACK
   e a headline ao lado da foto. A v2 separa três faixas: headline numa linha; o quadro como cartão inteiro; a foto
   pequena embaixo, ao lado do botão. *Sem veredito da v2 ainda.* Antes da v2, três direções foram testadas em
   miniatura (evidência no caso de origem).

## Capa vertical em série pra vitrine (área de membros da Hotmart, uma semana depois), sem veredito ainda

No caso de origem: um JSON das capas → um script de montagem → um de render com portão, e um teste que estraga 5
casos e confere a reprovação. 9 capas 720×1040 + 3 da alternativa + 2 banners com **3 gerações de IA** no total: a
IA faz só a placa de fundo neutra (sem pessoa, sem texto) e o código tinge em duotom por produto. Foto real recortada,
logo oficial em PNG, ícone da marca em tom sobre tom atrás do expert. Sistema é *hipótese*: o Rodrigo ainda não viu.

Armadilhas medidas nessa tarefa:
1. **`drop-shadow` e `mask-image` no mesmo elemento** (*UNIVERSAL, Chrome*): a máscara vale só pra caixa do elemento e
   corta o brilho, e aparece um retângulo claro em volta do ícone. A máscara vai num envelope com folga maior que o
   brilho. Não virou checagem (o portão não sabe o que é "borda reta no fundo"); a folga mora no código.
2. **`img.decode()` não resolve no `--dump-dom` com `--virtual-time-budget`** (*UNIVERSAL, Chrome headless*): o medidor
   nunca terminava. Esperar `img.complete` em laço, como o toscão já fazia, funciona.
3. **OCR do macOS (Vision) como portão de texto** (*VARIAÇÃO ISOLADA*): pega acento e texto inventado na peça inteira,
   inclusive dentro de PNG de logo, que o DOM não vê. Duas medidas: palavra curta muito espaçada ("GUIA" a .42em, azul
   sobre azul-escuro) virou "GULA", e a .3em/26 px leu certo; letra grande estilizada de logo (o nome curto do produto)
   às vezes não é lida na miniatura de 180 px. Por isso o OCR da miniatura é aviso, e o de 720 px trava.
4. **Linha miúda de logo vira ruído abaixo de ~100 px de largura** (*VARIAÇÃO ISOLADA*): o nome por extenso da marca
   de um evento, escrito miúdo dentro da logo, saiu ilegível no OCR. Na capa entra a versão reduzida (símbolo + sigla).
5. **Luz de recorte igual em toda a borda da foto vira contorno de adesivo** (*VARIAÇÃO ISOLADA*): concentrada no alto
   da cabeça (peso pela altura) e a 38% de opacidade, o cabelo assenta no fundo.

### Série com a mesma roupa (banner do checkout da Black, 11 dias depois), sem veredito ainda

Com 11 capas lado a lado no banner, o Rodrigo reprovou a série: "achei todas as fotos das capas muito
iguais, com a mesma camiseta". Todas as fotos de estúdio do expert eram da mesma sessão, com a mesma
roupa. O que ficou (*VARIAÇÃO ISOLADA*):
1. **Gesto diferente não basta: a roupa também varia.** Numa série que aparece junta, nenhuma peça
   repete a roupa da vizinha.
2. **Primeiro a foto real com outra roupa, procurada no Drive do cliente** (lá estava um pacote de fotos
   que os arquivos do projeto não tinham). Pra capa, só serve a foto em que o expert sorri e olha pra
   câmera, sozinho. Foto dando aula pega ele falando e não serve, mesmo com a roupa certa. Pra escolher,
   recorta o rosto pela caixa do Vision e faz uma folha por look.
3. **Onde falta foto real, troca a cor da roupa, sem IA generativa.** A máscara é a projeção do croma
   (Lab) na direção da cor da roupa, e a luz é multiplicativa, então o rosto, a pele e o cabelo ficam com
   o pixel original. Deslocar a luz média em vez de multiplicar manchou o tecido entre as mechas de
   cabelo. O branco pede contraste comprimido, senão vira cetim.
4. **Foto de evento tem duas armadilhas no recorte.** Um telão colorido atrás da cabeça deixa franja
   azul e rosa no contorno do cabelo (tirar a cor fria acima da testa). A mão apoiada num móvel sai
   borrada no recorte: some pelo enquadramento ou por um esfumado.

## Cópia da peça aprovada e quadro de vídeo como foto (6ª leva de estáticos dos produtos de entrada, 12 dias depois da 5ª), sem veredito ainda

Na leva há:
- duas variações de uma peça aprovada de quadro comparativo e duas de uma peça aprovada de lousa, trocando só o
  exemplo;
- um banner e um carrossel com um quadro de um vídeo que já tinha ido ao ar.

No caso de origem: um script de montagem lê o texto das tabelas do doc da copy, confere guia e fala e tira os quadros;
outro renderiza o PNG e roda o portão; um teste estraga peças boas de 13 jeitos.

O que virou checagem (*VARIAÇÃO ISOLADA*):
1. **"Trocando só o que muda" se mede.** O portão confere três coisas:
   - Os blocos de texto (`<p>`, na ordem) da peça nova são os do molde com só as trocas declaradas.
   - A faixa que não muda sai igual pixel a pixel ao molde renderizado na mesma hora.
   - O molde renderizado hoje sai igual ao PNG aprovado. Isso pega mudança de versão do Chrome.

   Na 6ª leva, as quatro variações e o card 5 copiado saíram com diferença zero na parte fixa.
2. **Quadro de vídeo entra pelo master, em 1:1.** O master é o mesmo 1080 x 1920 que foi ao ar, sem a placa do produto
   por cima. O mesmo quadro no arquivo final difere em menos de 1 nível de cor. O portão confere:
   - a escala 1:1 (o tamanho natural do arquivo é igual ao da peça);
   - que o recorte termina acima da caixa da legenda queimada do reel;
   - que o rosto inteiro (detecção de rosto do pipeline de vídeo) fica na parte que não esfuma.

   Entre os quadros que passam no critério do olho, o mais nítido no rosto sai pela variância do laplaciano.

Armadilhas medidas:
1. **Caixa queimada se acha pela linha mais estreita** (*VARIAÇÃO ISOLADA*). O título queimado do reel é uma caixa em
   degraus, e a 1ª linha é a mais estreita (x 280 a 847). Exigir branco em x 200–880 achou a 2ª linha, 89 px abaixo do
   topo real (y 944). Mede-se numa faixa que só a caixa cobre inteira, e que o quadro branco do cenário não alcança.
2. **URL de fundo em `data:` com ")" dentro** (*UNIVERSAL, regex do medidor*). A textura da lousa é um SVG embutido com
   `url(%23n)` dentro. O leitor da leva anterior cortava no primeiro ")" e dava a textura como não carregada. Lê-se o
   `url("...")` com aspas inteiro.
3. **SVG semitransparente com preenchimento e contorno sai "vazado"** (*UNIVERSAL, comportamento do navegador*). A cor
   com alfa soma na borda. A transparência vai no `opacity` do SVG inteiro, e a cor fica opaca.
4. **Linha nova da lousa (Chalkduster) não coube em 2 linhas** (*VARIAÇÃO ISOLADA*). A frase de exemplo nova pede uns
   442 px na 1ª linha, e a coluna da peça de lousa tem 430. O bloco dos exemplos avançou 30 px no respiro direito da
   lousa, mantendo corpo da letra e os começos de coluna. Medir a largura com a fonte real antes de escolher o exemplo
   poupa a volta.

## Formato novo do Demand Gen a partir do molde vertical, e feed em que só o botão muda (Black de um segundo expert, 8ª versão das peças), sem veredito ainda

No caso de origem: um script monta o HTML de cada formato (story, feed, quadrado 1080 e paisagem 1200 x
628); outro renderiza o PNG e roda o portão; um teste estraga peças boas de 10 jeitos e testa o refazer
da captura; e um último lê o PNG final por OCR.

São 16 peças com o botão novo mais 8 com o antigo. Nenhuma imagem nova: as cenas são as da versão
anterior.

O que virou checagem (*VARIAÇÃO ISOLADA*):
1. **Quando só o botão muda, a prova é pixel a pixel.** O código novo refaz a peça aprovada, e ela sai
   igual ao PNG dela (diferença 0). A peça nova sai igual à aprovada fora da área do botão e da sombra
   dele (1.323.360 px por feed, diferença 0).
2. **O Chrome às vezes varia o pontilhado do degradê.** 1 captura em cerca de 20 saiu com até 4 níveis
   de cor numa faixa de 200 x 40 px. O portão refaz a captura (até 3 vezes) quando a diferença é só
   ruído (até 8 níveis) e reprova na hora diferença maior. O teste prova as duas coisas.
3. **Cena de lado na paisagem.** O portão reprova bloco de texto dentro do painel da cena e cena que não
   chega ao pé da tela. A escala mínima é 628/1080 = 0,582: uma cena a 0,58 parou em y 626.

Armadilhas medidas:
1. **O molde vertical não cabe no quadrado com a cena na largura toda.** Os objetos das cenas ocupam de
   600 a 760 px de altura em 1080 de largura, e logo, frase, data e botão pedem uns 460. No quadrado a
   cena encolhe (de 0,71 a 0,88) e some nas laterais e no pé.
2. **Na paisagem, o degradê do lado do texto só pode cair em parte que não importa.** O recorte de cada
   cena foi escolhido olhando a imagem, com o objeto principal fora do degradê.
3. **Cena com fundo liso embaixo mostra a emenda se o degradê for curto.** As cenas desta leva acabam
   numa faixa lisa. Com 110 px de degradê, a emenda apareceu na paisagem. O que resolveu foi o degradê
   na proporção da cena: de 175 px acima a 20 px abaixo do pé dos objetos, medidos na cena original, o
   mesmo dos verticais.
4. **O OCR do macOS lê "todas" como "todos"** na segunda linha do botão do story (Poppins SemiBold 30 px
   sobre a pílula dourada, 1080 x 1920). Ampliado 2x, lê certo, e o DOM confere o texto. O ícone da logo
   sai como letra solta. No canvas grande, o OCR é aviso, não trava (a mesma conclusão da vitrine sobre a
   miniatura).

## Cinco mecânicas novas, quadro de aula e página com linha vetada (7ª leva de estáticos dos produtos de entrada, uma semana depois da 6ª), sem veredito ainda

No caso de origem: um script de montagem lê o doc da copy, confere os fatos da arte e tira os quadros e
as páginas; outro renderiza o PNG, roda o portão e monta a folha; um teste estraga peças boas de 14
jeitos; e um último acha rosto e lê texto pelo Vision do macOS.

São 12 peças (preço, aula em vídeo, o que vem no guia, horas vagas, já comprou), com um leia-me contando
onde cada uma saiu do doc.

O que virou checagem (*VARIAÇÃO ISOLADA*):
1. **Página com linha vetada se mede pelo OCR do PNG final.** A folha de consulta de um dos guias tem uma
   expressão que está fora das artes desde a 5ª leva. O OCR do macOS lê essa linha a partir de 360–380 px
   de largura (conforme a inclinação, de 4° a 9°, e o fundo) e não lê com 340 px ou menos. O portão trava
   a expressão lida no PNG das peças daquele guia, e o teste prova com a folha a 600 px.
2. **Quadro de aula, sem ampliação.** Ele sai do master pelo número do quadro, recortado em 1:1, e o
   portão confere três coisas: que o recorte não pega a sigla queimada da marca nem a do slide, que o
   rosto inteiro fica na foto, e que nenhum texto chega a menos de 12 px dele.
3. **Fatos da arte conferidos antes de montar.** O número de exercícios que a arte promete é contado no
   guia montado, e o preço tem que estar na ficha do guia, na decisão registrada e na parcela medida
   (`sirius-scale/frameworks/lancamentos/low-ticket.md` §14.5).

Armadilhas medidas:
1. **Achar o quadro de aula sem OpenCV.** Sem `cv2` no ambiente, o Vision do macOS (pyobjc) dá o rosto,
   o yaw e a qualidade de captura em 2,9 mil quadros de 960 px em ~20 s. Depois vêm os marcos do rosto: a
   largura da boca sobre o rosto separa o sorriso, e a pupila no meio do olho separa quem olha pra
   câmera. A aula é quase toda fala séria: dois dos três sorrisos escolhidos estavam entre os
   quadros-chave (varredura a 2 qps), não nos quadros-chave.
2. **Selo girado dá sobreposição falsa no portão.** A caixa da tinta é retângulo alinhado aos eixos. Num
   selo a −7°, o preço em 128 px e a linha de baixo "encostavam" sem nenhum pixel se tocar. A saída foi
   girar menos (−5°) e afastar as linhas (44 px), sem relaxar o portão.
3. **Rótulo colado no objeto pede linha de chamada, não seta de mão.** Com quatro rótulos em volta de um
   grupo de objetos, a seta de traço de mão ficava com 40 a 60 px e embolava. Funcionou uma linha branca
   com um ponto no objeto, o ponto fora do texto da página.
4. **Logo de 560–580 px come o "dois terços de cima".** Com a logo no pé e o título numa faixa colorida,
   o quadro da aula fica entre 620 e 700 px (46–52% da peça).

## Banner da página do curso na área de membros da Hotmart (produtos de entrada do caso-base, dois dias depois da 7ª leva), sem veredito ainda

No caso de origem: um script monta, passa o portão e faz a folha de prévia do topo do curso (computador e
celular); um registro guarda cor, logo, desenho e curso de cada banner; um teste estraga uma peça de 8
jeitos e confere que o portão reprova.

São 4 banners 1920 × 640 sem IA e sem texto nosso: a logo e o desenho oficiais (PNG) sobre cor chapada.
No computador a Hotmart escreve em branco por cima da metade esquerda, e no celular o banner aparece
inteiro, com o texto embaixo. A identidade é a das capas de módulo que ficam na mesma página, não a da
vitrine.

O que virou checagem (*VARIAÇÃO ISOLADA*):
1. **Metade esquerda lisa, medida no pixel.** Até a emenda, nenhum pixel se afasta mais de 2 níveis da
   cor escura, e o branco tem contraste de pelo menos 15:1 contra ela.
2. **Peça sem texto nosso se prova no DOM, não só no OCR.** O texto vivo da peça tem de ser vazio, e todo
   texto que o OCR lê precisa morar dentro da logo ou do desenho. O teste prova os dois caminhos: texto
   no HTML e letra dentro de imagem (a sigla da marca solta no painel).
3. **A logo é a oficial pelo hash.** O sha256 da logo e do desenho oficiais fica no registro, e arquivo
   trocado reprova.

Armadilhas medidas:
1. **Lanczos deixa halo em emenda dura de cor chapada** (*UNIVERSAL, filtro de reamostragem*). Na redução
   da captura 2x pra 1x, a coluna vizinha da emenda saiu 3 níveis fora da cor lisa, e o portão reprovou.
   Em arte chapada, a redução é pela média de blocos 2 × 2 (`Image.reduce(2)`): a emenda fica exata e a
   esquerda sai com uma cor só.
2. **O OCR do macOS pode não ler nada na peça inteira** (*VARIAÇÃO ISOLADA*). Num dos banners, o nível
   preciso não devolveu texto nenhum, e o mesmo cartão recortado da captura 2x leu a logo. Leitura vazia
   não prova peça sem texto: o portão junta o nível preciso e o rápido na peça inteira, lê a logo no
   recorte 2x e confere o DOM (item 2 acima).
3. **A logo limpa e o PNG original dela diferem só no alfa** (*VARIAÇÃO ISOLADA*). São até 11 níveis, nos
   pixels semitransparentes do fundo, e a cor é idêntica: é a mesma logo com o fundo limpo.

## Peça que destoa da série se refaz pelo gerador da irmã (capas de módulo e aula de um dos guias, mesmo dia), sem veredito ainda

As capas de um dos guias, feitas semanas antes, eram de outro desenho e destoavam das dos outros três.
Saíram de novo pelo gerador da irmã, parametrizado, não por script novo. O gerador não tinha portão e
ganhou um, com um teste que estraga a capa de 5 jeitos.

O que virou checagem (*VARIAÇÃO ISOLADA*):
1. **A irmã sai igual.** O HTML dela gerado pelo código novo é o anterior byte a byte.
2. **Mesma família se mede.** O portão renderiza a irmã na mesma hora e exige painel, cartão, série,
   assinatura e sigla no mesmo lugar dela (0,5 px), e o selo e a logo na mesma coluna.
3. **A página usa o arquivo oficial.** O hash do arquivo oficial não basta: o portão confere também que o
   `src` das imagens da página é esse arquivo (o teste troca a logo de um guia pela de outro).

Armadilhas medidas:
1. **Fonte do Google por `@import` muda a borda da letra com o tempo** (*VARIAÇÃO ISOLADA*). O mesmo HTML
   da irmã, renderizado 3 semanas depois, saiu diferente do PNG aprovado em 0,09% dos pixels (até 51
   níveis), na borda das letras da série, do selo e da assinatura. Fora dessas linhas, só 15 pixels a 1
   nível; desenho, logo e cores saíram iguais. A conferência da 6ª leva, que renderiza o molde de novo e
   compara com o PNG aprovado, não fecha com fonte da web: compara-se o HTML e a moldura, ou se usa fonte
   local.
2. **O OCR do macOS lê a aspa curva de fechamento como asterisco** (*VARIAÇÃO ISOLADA*, Manrope 700 a 30
   px). A comparação com o OCR ignora aspas; quem confere a aspa letra por letra é o DOM.
3. **Desenho mais largo pede outro tamanho, não outra página** (*VARIAÇÃO ISOLADA*). O desenho dessa capa
   é largo (1,6:1). No cartão ele entrou pela largura (folga de 42 px). Na aula, entrou com a altura do
   desenho da irmã (158 a 159 px), e os vãos entre série, desenho, logo, selo e assinatura ficaram a até
   5 px dos dela.

## Peça em cena: superfície lisa gerada, texto e letreiro por cima (remarketing da Black, mesmo dia), sem veredito ainda

Pedido do Rodrigo sobre as peças sem foto: "esses que não tem a foto da […], poderia ser mais criativo".
Saíram duas (um aviso num mural, um painel aceso de ponto de ônibus), 4 formatos cada, como um estilo
novo da linha de montagem que já existia. 9 gerações de imagem no total. O HTML das 24 peças dos outros
estilos saiu igual byte a byte.

O que virou checagem (*VARIAÇÃO ISOLADA*):
1. **A superfície se mede na imagem.** A folha é o maior branco pouco saturado; o painel aceso, o maior
   azul. As bordas saem pela mediana das linhas e colunas (a tachinha do canto não puxa o retângulo). O
   texto tem de ficar dentro dela.
2. **O letreiro se confere pelo efeito, não pelo CSS.** Arquivo oficial, sem transform, sem filtro, sem
   mistura, mesma proporção do PNG, e os pixels opacos dele na peça iguais aos do arquivo (diferença média
   de 0,3 nível). O respiro que o manual da logo pede fica sem texto, botão ou post-it.
3. **Texto de cena inventado se pega pelo OCR da peça inteira** (1x e 2x): tudo o que ele lê tem de morar
   no nosso texto ou no letreiro. O teste prova com uma placa "FARMÁCIA" pintada na calçada.
4. **Pessoa pequena no fundo só aparece em blocos ampliados.** O Vision não achou um pedestre de ~30 px no
   calçadão da cena inteira; em blocos de 300 px ampliados 3x, achou (confiança 0,6), sem falso positivo
   nas outras 6 cenas. QR e código de barras: o detector do Vision na peça inteira.

Armadilhas medidas:
1. **O gerador põe o objeto onde quer.** O post-it pedido "metade no papel" veio com 78% sobre a folha,
   cobrindo a quina onde o letreiro de 560 px tinha de ficar. O que resolveu: recortar o post-it liso
   dessa cena (contorno convexo do amarelo + a tachinha, borda antisserrilhada) e pôr ele por formato, à
   direita do letreiro + respiro.
2. **O gerador faz a superfície menor que a pedida** (54 a 63% da largura, pedidos 65 a 75%). Entra com
   zoom, e o story e o quadrado ficaram até 1,43x acima do tamanho que o gerador entrega (941 x 1672 no
   9:16; 1122 x 1402 no 4:5; 1254 no 1:1; 1740 x 904 no 27:14). O portão anota essa ampliação em cada
   peça.
3. **O til do Caveat Brush é um traço quase reto e lê como "ā".** O OCR leu "amanhā" em 2 de 4 peças.
   Virou uma variante da fonte com o "~" ondulado da própria Caveat Brush no lugar do acento do ã e do õ.
   O OCR não serve de trava pra isso: com o til reto, ele ainda achava "amanhã" em alguma escala. A
   conferência do til fica no olho; o OCR das palavras acentuadas à mão é só aviso.
4. **Span em bloco mede a linha inteira.** O fato quebrado em duas linhas com `<span>` em bloco tinha
   caixa da largura da folha, e o portão acusou o post-it encostando num texto que não estava lá. Com
   `width: fit-content` a caixa é a da letra.
5. **A margem transparente do PNG do letreiro conta na área.** No story, a parte visível começava em x
   100 e a caixa do PNG em 91: fora da coluna segura. Mexer o recorte 10 px pra corrigir pôs a sombra de
   um papel cortado na borda esquerda; a solução foi a margem interna da folha.

## Mais armadilhas medidas em peças de HTML (11/2026), sem veredito de resultado ainda

O que virou checagem, *VARIAÇÃO ISOLADA*:
1. **Print com tarja se prova por pixel.** Fora da tarja, a peça é igual ao print original ampliado (diferença zero), então
   o texto do print não tem como mudar. Dentro dela, a cor é lisa.
2. **Tarja que corta letra ao meio reprova.** Mancha de tinta do original que entra na tarja e sai dela é foto, letra ou
   nome pela metade.
3. **Print e foto entram 1:1 no pixel**, em posição inteira. Título de altura fracionada deixou o print em y quebrado.
4. **OCR com o contraste estourado** (histograma equalizado) pega o @ quase da cor do fundo, que o olho não vê.
5. **Story de anúncio usa a faixa de anúncio** (x 100–940, y 295–1536, `margens-seguranca-vertical.md`), não a do Reels
   (até 1625).
6. **Versão de anúncio que só troca o botão se prova pixel a pixel:** a diferença contra a peça aprovada fica só dentro do
   botão.
7. **Capa de carrossel lida em miniatura:** reduzida a 200 px de largura, o OCR tem de ler todas as palavras do título.
8. **Encosto se mede letra por letra**, não pela caixa da linha inteira; marca-texto cobre a tinta inteira da palavra
   (acento e perna incluídos); desenho à mão (círculo, seta) fica dentro do cartão.
9. **Defeito plantado no teste do portão entra antes do layout** (área, medida), não por cima dele com `transform`: a função
   que posiciona mede já com o transform e compensa, e o teste passa sem provar nada.

Armadilhas, *VARIAÇÃO ISOLADA*:
1. **O detector de rosto do macOS (Vision) não prova que o rosto saiu da tarja**: na peça inteira ele não achou o rosto que
   estava lá. Quem prova é a tarja lisa, a mancha de tinta e o olho.
2. **Cor por linha não sai da mediana de uma linha com texto** (vira a cor da letra). Tire a cor de uma faixa sem texto.
3. **Tarja que para antes da borda mostra degrau** em fundo degradê com granulado: vá de borda a borda.
4. **Letra sozinha no fim da linha** ("E", "o", número): espaço inseparável depois dela resolve sem mudar palavra.
5. **A caixa do OCR do macOS é uns 10 px mais larga que a tinta:** texto mora 12 a 14 px pra dentro da área segura.
6. **O OCR troca letra com o corpo da fonte** ("No" por "Na" num tamanho, certo noutro) e devolve letra cirílica de mesmo
   desenho: normalize os homóglifos e confira a letra de verdade no DOM.
7. **Fonte cursiva com til quase reto** lê "nāo": troque o glifo do til por um de outra fonte, ou escolha outra cursiva.
8. **Faixa de altura fixa pede folga pra acento e perna** (o til do "NÃO" passa em cima; "f", "j" descem embaixo).
9. **Peça feita por IA e aprovada se remonta em HTML** quando a geração não está disponível: fundo e brilho em CSS nas
   cores medidas na peça aprovada, o recorte de foto que ela já usava e a logo oficial; o texto sai do arquivo da copy.
## Objeto desenhado em HTML no lugar de imagem gerada (ficha, carimbo, folha, agenda), sem veredito ainda

Peças sem imagem gerada: o objeto da cena é HTML e SVG, com semente fixa pro que é aleatório. Pra empilhar texto pela
tinta, `text-box: trim-both cap alphabetic` (Chrome recente) faz a caixa do texto ir do topo da maiúscula à linha de
base, sem o espaço interno da fonte.

O que virou checagem, *VARIAÇÃO ISOLADA*:
1. **Rótulo de desenho é texto previsto no briefing.** Os números e letras de uma folha desenhada e as horas de uma agenda
   saem registrados com a origem na copy, e o portão exige exatamente esse conjunto, com corpo mínimo. O teste planta um
   texto legível a mais no desenho pra ver o portão reprovar.
2. **Caixa girada se mede no sistema dela.** `offsetLeft` e `offsetTop` não sofrem o transform: o carimbo cabe na ficha
   conferido pelos cantos girados, e os rótulos de uma folha girada se comparam no sistema da folha.
3. **O maior número da peça se mede.** Se a peça vende uma hora, a hora tem de sair maior que o preço e que os outros
   números do desenho.

Armadilhas medidas:
1. **Linha com corpos diferentes contava como duas.** Agrupar os retângulos do texto pelo centro, de 10 em 10 px, separava
   a palavra pequena do preço grande na mesma linha. Junte as faixas por sobreposição vertical.
2. **O OCR do macOS pode ler errado o cifrão de uma fonte condensada grande** (*VARIAÇÃO ISOLADA*): normalize o "R$"
   antes de comparar, e confira o preço pelo DOM e pelos dígitos.
3. **Recorte de foto pega o móvel em volta** (*VARIAÇÃO ISOLADA*). Tirar tudo que é "cinza" na região come a sombra e
   abre buraco em acessório. O que funcionou: sai só o neutro (R ~ B) que encosta no fundo; pele e tons quentes (R > B)
   ficam. O vão que o recorte fecha sai por região.
4. **Objeto centrado logo abaixo do queixo vira placa** (*VARIAÇÃO ISOLADA*, sem veredito). No story, o objeto vai pra
   primeiro plano, de lado, cobrindo só a base do braço.

## Ligado a

- `sirius-scale/frameworks/copy/criativos.md` §0.7.6: a página do produto que aparece na arte sai do arquivo à venda,
  na hora de montar.
- `sirius-scale/frameworks/copy/criativos.md` §0.11: pesquisa na Biblioteca de Anúncios antes de desenhar.
- `sirius-scale/frameworks/lancamentos/low-ticket.md`, "Estáticos v5": o que a 5ª leva decidiu, como logo grande, sem
  preço e com rosto.
- `sirius-scale/frameworks/design/captacao-da-black-arte-do-estatico.md`: a arte do estático de captação da Black, que
  usa este portão.
- `sirius-scale/frameworks/design/margens-seguranca-vertical.md`: a zona segura do story.
