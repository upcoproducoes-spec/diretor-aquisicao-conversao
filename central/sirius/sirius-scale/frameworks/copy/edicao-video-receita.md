# Receita de edição — criativo em vídeo vertical (Reels/Stories)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> 📐 **Antes deste arquivo, ler `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`** — ele decide *o quê*
> e *por quê* (bloco, ritmo, emoção, camadas de áudio); este aqui é o *como*.

> **Camada:** execução (com ferramental universal embutido)
> **Base:** 1 cliente (o caso-base, um expert de educação) · 1 lançamento · 1 peça (um corpo + um CTA) ·
> 5 rodadas de correção
> **Alcance:** NÃO TESTADO FORA. **O processo transfere; os números não.**
> Os valores do §2 ("números validados") são o padrão visual **do editor do
> expert do caso-base**, medido no arquivo dele e **aprovado pelo Rodrigo** (não pelo
> expert, que nunca validou esses números) — não são boas práticas de
> mercado. São números aprovados no caso de origem: **ponto de partida, não regra
> da marca de vocês**. Em cliente novo eles estão errados por definição: o passo 0
> (pedir peça de referência do editor do cliente) é justamente como se descobre os
> números certos. Ver o §4 do fim ("O que transfere e o que é do caso").

> **Ferramentas e como usar este arquivo.** Os comandos daqui são de **ffmpeg** com
> **libass** (legenda em `.ass`) e, na sincronia, **mlx-whisper**: ferramentas
> externas, instalam à parte. Quem edita no CapCut ou com editor humano não precisa
> rodar comando nenhum: os números do §2 viram o alvo a reproduzir na ferramenta (ou a
> conversa com o editor), e as armadilhas viram checklist pra conferir o arquivo
> exportado (fonte certa num frame ampliado, áudio a 48 kHz, nível médio da fala,
> nada de trilha que sobe e desce sozinha).

> Companheiro prático de `sirius-scale/frameworks/copy/edicao-video-criativos.md`. Aquele registra **por
> que** cada decisão existe e as armadilhas; **este é o passo a passo pra
> executar**, com os números já validados. Ao editar um criativo novo, seguir
> daqui e só voltar ao outro se algo fugir do previsto.
>
> Base: a primeira peça de captação do caso-base (um corpo + um CTA), 5 rodadas
> de correção com o Rodrigo. Confiança: **VARIAÇÃO ISOLADA** — um cliente, um
> lançamento. Ao aplicar em cliente diferente, sinalizar na entrega.

## 0. Antes de tocar em qualquer arquivo

1. **Pedir uma peça de referência já editada pelo editor do cliente.**
   Isso encurta rodadas mais que qualquer outra coisa — foi só ao receber
   um reel já editado pelo editor do expert, de um lançamento anterior, que o
   padrão real (fonte, posição, transição, nível de áudio) ficou claro. Sem
   referência, o resto é chute.
2. **Pedir os ativos de marca originais** (logo em PNG transparente, nas
   versões clara e escura). Recortar logo de peça pronta é retrabalho.
3. **Ler `sirius-scale/frameworks/design/margens-seguranca-vertical.md`** antes de
   posicionar qualquer texto. Os números de lá são de teste real.
4. Medir a referência: `volumedetect` no trecho falado, e um frame ampliado
   da legenda pra ver fonte/peso/sombra.

## 1. Arquitetura de render (não pular)

Dois passos, sempre. Editar direto do 4K custa ~12 min de CPU **por
tentativa** e trava a máquina de edição.

| Passo | O que faz | Custo |
|---|---|---|
| **1. Master** | 4K HDR → 1080p limpo (tone-map + crop + corte), `crf 18`, sem texto | ~12 min, uma vez |
| **2. Texto/áudio** | overlays + legenda + junção + mix, em cima do master | segundos |

Guardar `master_<clipe>.mp4` até a peça ser aprovada.

## 2. Números validados — aprovados no caso de origem; ponto de partida, não regra da marca de vocês

### Vídeo
- Canvas **1080×1920**, 30fps, `yuv420p`, `crf 19-20`, `+faststart`.
- Tone-map HDR do iPhone (obrigatório, senão sai lavado):
  `zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv`
- Reenquadramento usado no bruto do caso-base (celular alto, muito teto vazio):
  `crop=1568:2790:296:1050,scale=1080:1920`

### Legenda (o que o Rodrigo aprovou)
- Fonte **Poppins Bold**, `Fontsize 96`, `Bold: -1`, família `Poppins`.
- **`Outline: 0`, `Shadow: 6`**, `BackColour &HC8000000`. Contorno preto é o
  que dava cara amadora — não usar.
  - ⚠️ **Escopo, aberto depois: isto vale no VERTICAL.** No 16:9 o Rodrigo
    pediu o oposto, com print: a palavra de destaque em cyan sobre a roupa clara
    do expert ficava ilegível só com sombra. Lá vale **borda fina** (`Outline 1.3`,
    `Shadow 0.6`). Não é reversão da regra — é gatilho: **quando o destaque falha
    em contraste sobre fundo claro, borda fina entra**. Cruza com
    `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §4.3, que já declara UNIVERSAL que quem decide
    legibilidade é a medição, não o olho.
- `Alignment 2`, `MarginL/R 80`, **`MarginV 560`**, `WrapStyle 0`.
  - ⚠️ **A peça no ar diverge deste número (medido depois, na própria peça).**
    Baixei a versão REELS da peça aprovada e medi por detecção de pixel em 5
    frames: headline em `y=840–1040` (esta seção manda `topo = 240`) e legenda
    com base em `y≈1150`, ou seja **MarginV ≈ 770**. Os controles da mesma seção
    **fecham**: fonte ~99px de altura (`Fontsize 96` ✓) e áudio a −16,6 dB
    (alvo ~−16,7 ✓) — só a posição vertical diverge.
    **RESOLVIDO — a peça aprovada ganha.** O Rodrigo: *"eu quando
    fazia preferia duplicar o que já tinha feito e revisado, estando com todas as
    configs certas, e aí só altero o vídeo e a copy/link se necessário"*.
    Consequência pra este arquivo: **os números aqui são o porquê, não o ponto de
    partida.** Peça nova sai de cópia da última aprovada (na prática: o mesmo
    projeto, com o vídeo e o texto trocados). Quando doc e peça divergem, a
    divergência entra como nota com data — como esta — em vez de o número ser
    trocado às cegas, porque medir o arquivo diz quais pixels estão lá, não quem
    os pôs. É regra da casa: peça nova sai da cópia da última peça aprovada.
- Blocos de **até 3 palavras**, quebra em pausa ≥0,28s ou fim de frase.
  - *VARIAÇÃO ISOLADA (um criativo de 85s de um segundo negócio):* o "até 3" é
    teto, não alvo. Cortar por contagem deixa resto de 1 palavra e frase partida
    no lugar errado (a última palavra sozinha na tela). Dividir a **frase** em grupos
    balanceados (4→2+2, 5→3+2, 7→3+2+2) resolve — no caso de origem, quem fazia
    isso era o script de legenda do kit de vídeo (morava no kit, não na pasta da
    peça, que é apagável).
  - *Mesma peça:* legenda com texto cru do ASR saiu com "2.11%", "4.7", "quinze
    mil setecentos e quinze" e as gaguejadas de quem falava. Vale o §3:
    ASR só pelo tempo; o texto é revisado frase a frase (número em formato
    brasileiro, disfluência fora), e quando a contagem de palavras muda, o tempo
    do bloco é repartido na proporção dos tokens.
- Destaque **1 palavra por bloco no máximo**, na cor de destaque da marca (no
  caso-base, um cyan), por prioridade: número > termo do evento > negação.
  ⚠️ No `.ass` a cor vai ao contrário (BGR): `#RRGGBB` vira `&H00BBGGRR&` (ex.:
  `#FF8800` → `&H000088FF&`).
- **Sempre passar `subtitles=x.ass:fontsdir=<pasta>`** — sem isso o libass
  troca a fonte em silêncio (ver armadilha em `sirius-scale/frameworks/copy/edicao-video-criativos.md`).

### Headline (sticker nativo do IG)
- **Uma caixa branca por linha**, cada uma abraçando a largura do próprio
  texto, **coladas** (sem respiro entre elas). Raio 16px, padding 26×14.
- Poppins Bold **54px**, texto quase-preto `#121212`, emoji inline no começo.
- **`topo = 240`** — abaixo dos 220–290px que a UI da rede ocupa no topo.
- Texto = **o mesmo que está entre aspas no doc de copy**, verbatim.
- Emoji: Apple Color Emoji só rasteriza em 96 ou 160px (137 falha) —
  renderizar em 160 com `embedded_color=True` e reduzir.

### Logo do evento
- PNG oficial **transparente**, versão **clara** (texto navy) porque o expert
  grava contra parede clara.
- **Sem cartão de fundo.** Halo branco em volta (blur gaussiano do alpha,
  raio 16, 6 passadas) pra destacar sobre a roupa escura.
- Largura 560px, **y ≈ 760 (altura do peito)** — nunca na frente do rosto.
- Entra **só enquanto o expert fala o nome do evento** (tempo vindo do
  alinhamento, não chutado).
- ⚠️ **O que veio depois, no mesmo caso (VARIAÇÃO ISOLADA, evidência no caso de
  origem):** numa leva seguinte, com logo navy e dourado sobre parede bege, o halo
  branco não resolveu o contraste (reprovado duas vezes), e uma placa escura atrás
  do logo branco também saiu ("brega, fundo preto", nas palavras do Rodrigo). O que
  passou foi uma **pílula branca** com o logo, 400px de largura, entrando quando o
  expert fala o nome, por ~4s, abaixo do bloco de legenda e dentro da zona segura. A regra que ficou na
  casa: **marca sobre vídeo vai em placa ou não vai** — borda ou halo no glifo não
  substitui placa (mesmo princípio de `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §4.3).

### Áudio
- Voz: `loudnorm=I=-16:TP=-1.5:LRA=11` → `volume=2dB` → `alimiter=limit=0.97:level=disabled` ⚠️ **`level=disabled` não é opcional** — o default do filtro é `level=true`, que normaliza o sinal de volta pra 0 dB depois de limitar (ver `sirius-scale/frameworks/copy/video-criacao-tecnica.md` §2).
  Alvo: **~-16,7 dB** de média no trecho falado (é o nível da referência).
- Música: **`volume=0.06`**, constante, `afade` de 2s na entrada e 2,5s na
  saída.
- ⚠️ **Nunca usar `sidechaincompress`/ducking.** Foi reprovado: a trilha
  sobe nas respirações e fica oscilando. Volume fixo e baixo. Subir a trilha
  só nas pausas longas é a mesma coisa; pausa longa se resolve no corte
  (regra reforçada depois, numa leva de reels transformados em anúncio). Vale em
  qualquer ferramenta: nada de recurso que abaixa a trilha sozinho quando a voz entra.
- Fechar sempre com `aresample=48000` **e** `-ar 48000` (o `loudnorm`
  devolve 96/192 kHz).
- Depois, no mesmo caso, a trilha passou a ser medida também **na faixa que o
  celular toca (300 Hz–4 kHz), contra a voz na mesma faixa**: trilha só de grave
  some no alto-falante do celular mesmo "medindo bem" em loudness. Números e
  contexto em `sirius-scale/frameworks/copy/captacao-da-black-edicao-de-video.md` §2.

### Transição corpo → CTA
- ⚠️ **O mergulho curto no preto (0,25 s de cada lado) não serve:** lê como corte seco, e não fica claro que entrou
  outro vídeo. A transição tem que ser leve **e** visível, e o som cruza sem buraco e sem estalo.
- **O que foi aprovado no lugar** (VARIAÇÃO ISOLADA, uma leva): fusão com desfoque de 0,6 s (o "Blur Crossfade" médio
  do catálogo do HyperFrames), com três ajustes pra vídeo:
  1. desfoque de 15 px (com 10 px as duas legendas ficavam legíveis uma por cima da outra no meio);
  2. mistura normalizada (as duas camadas sobre preto escurecem ~45% no meio, o que volta a ler como mergulho);
  3. a borda do quadro que entra preenchida por espelhamento.
- **A voz do CTA não muda de lugar; quem anda é a fusão.** Reel acabado costuma desfocar pro fecho dele 1 a 9 quadros
  antes do corte: a fusão começa no último quadro limpo, o corpo fica parado nele enquanto desfoca, e o 1º quadro do CTA
  segura até 6 quadros dentro da fusão. A pausa entre as falas vira 0,4 a 0,7 s. O último bloco de legenda do corpo
  não apaga antes da fusão.
- **O som cruza:** o do corpo sai em cosseno de 0,3 s, terminando 0,15 s depois de o CTA começar, nunca além do que a
  fonte tem.
- *Antes:* `fade=t=out:st=<fim-0.25>:d=0.25` no fim do corpo e `fade=t=in:st=0:d=0.25` no início do CTA, só no vídeo,
  com o áudio concatenado direto (`concat`, sem `acrossfade`).

### Reel orgânico como corpo de anúncio
Reel que já foi ao ar com uma edição antiga queimada na imagem (legenda miúda no meio do quadro, cartão branco de
exemplo com letra pequena, headline que some em 2 a 3 s) não serve como corpo de anúncio do jeito que está: a
diferença de tamanho entre a legenda do corpo e a do CTA é o primeiro defeito que se vê. VARIAÇÃO ISOLADA. O que vale:
- **Corpo e CTA com legenda do mesmo tamanho.** O salto de tamanho entre os dois é o defeito que se vê primeiro. Meça
  a altura-x da legenda no quadro, nos dois: abaixo de 90% da do CTA, refaça.
- **Exemplo vira esquema na tela, acompanhando a explicação**, nunca cartão branco com texto pequeno: o que o expert
  mostra no quadro, a tela mostra junto.
- **Headline no tempo de leitura.** A regra dos ~7,6 s (abaixo, "Timing de entrada e saída") vale também pro reel
  reaproveitado: headline que sai antes disso não dá tempo de ler.
- **Letra grande quando o avatar é mais velho** (confira a idade na pesquisa de vocês). Na manchete em 1080×1920, altura-x de pelo menos ~49 px por linha e nenhuma linha miúda; ~35 px foi
  reprovado.
- **Linha vermelha (sublinhado, risco, círculo) sem borda branca:** com borda, polui a tela.
- **Reel com edição fora do padrão não entra como está.** Refaz-se a partir da fonte limpa. Antes de montar, compare a
  edição do corpo com a do CTA, não só o texto da tela.

### Timing de entrada e saída (ajuste fino aprovado)
- **Legenda e headline aparecem no frame 0**, em opacidade cheia. Nada de
  fade-in nos primeiros frames: o gancho tem que estar legível antes do
  scroll. A headline **não** leva animação de entrada por isso.
- **Headline fica ~7,6s na tela** (fade out em 7,10s, d=0,50). Antes estava
  em 4,7s e o cliente pediu mais tempo de leitura.
- **Cortar o respiro antes da primeira palavra**, em cada clipe. Não estimar:
  medir a energia do áudio em janelas de 40ms e achar onde a fala real
  começa. No CTA da peça o respiro ficava em 0,28–0,60s e a fala só em 0,76s —
  cortar 0,60s deixou a entrada direta. Respiro fica ~15-25 dB abaixo da
  fala, fácil de separar.
  Ao cortar N segundos do início de um clipe, **deslocar em -N**: as linhas
  do `.ass` daquele trecho e os tempos de entrada/saída de todos os overlays.

### Encoder: usar hardware no passo de texto — *medido na máquina do caso de origem (um Mac)*
| Passo | libx264 | h264_videotoolbox |
|---|---|---|
| Texto/motion (1080p) | 38s real / 74s CPU | **10s real / 12s CPU** |
| Master (4K HDR→1080p) | **102s real** / 174s CPU | 133s real / 126s CPU |

- **Passo de texto: `-c:v h264_videotoolbox -b:v 12M`** (o encoder de hardware
  do Mac). 3,7x mais rápido e 6x menos CPU. Qualidade conferida em close de rosto:
  sem perda visível.
- **Passo master: manter `libx264 -crf 18`.** Lá o gargalo é o tone-map
  (CPU puro), e o hardware sai até mais lento.
- Com isso o ciclo inteiro de texto+motion+mix caiu para **~47s** no criativo
  de 2min22.

### Motion (o que dá o acabamento)
- **Legenda:** pop de entrada via tag ASS
  `{\fscx90\fscy90\t(0,120,\fscx100\fscy100)}` no início de cada bloco.
- **Headline:** entra descendo, `overlay` com y animado de -34 a 0 em 0,35s,
  junto com `fade` de alpha.
- **Logo e botão:** entram subindo (+26/+30 → 0 em 0,35-0,40s) com fade.
- Fórmula de deslocamento no `overlay`:
  `y='if(lt(t,T0),D, D-D*min(1,(t-T0)/DUR))'`

## 3. Sincronia de legenda — o único jeito que funciona

Estimar tempo por contagem de palavra **não funciona** (duas rodadas
perdidas nisso). O método correto, mesmo tendo a copy do teleprompter:

1. Extrair o áudio do trecho já cortado (`pcm_s16le`, 16 kHz, mono).
2. Rodar ASR com timestamp por palavra (`mlx-whisper`, modelo
   `mlx-community/whisper-small-mlx`, `word_timestamps=True`, `language="pt"`).
   ⚠️ o mlx-whisper chama `ffmpeg` do PATH — criar symlink do binário do
   `imageio-ffmpeg` em `venv/bin/ffmpeg`.
3. **Alinhar** as palavras da copy com as do ASR por Needleman-Wunsch,
   comparando a forma normalizada (minúscula, sem acento, sem pontuação).
   Cada palavra da copy herda o tempo da palavra do ASR com que casou;
   lacunas recebem tempo interpolado entre as âncoras vizinhas.
4. Conferir a taxa de casamento — **abaixo de ~85% é sinal de problema**.
   Na primeira peça deu 93% (corpo) e 96% (CTA).
5. Validar antes de renderizar: comparar, em 5 pontos espalhados, o que o
   ASR diz naquele segundo com o que a legenda mostra.

O ASR entra **só pelo tempo**; o texto exibido é sempre o da copy (grafia,
acento e termos da marca corretos — o ASR escreve "20 horas" onde a copy diz
"20h").

**Dígito x extenso — o critério é a tela concordar com ela mesma**
*(VARIAÇÃO ISOLADA)*: **dígito** quando o número é o dado ou a
promessa da peça, o mesmo que aparece na headline (`5 erros`, `3 aulas`, `99%`,
`20h`); **extenso** no resto (`duas alternativas`, `uma vaga`). Não é norma
gramatical: ficaria estranho a headline dizer "Os 5 erros" e a legenda logo
abaixo dizer "cinco erros". A revisão técnica do lote achou exatamente esse
caso ("20 horas" numa peça contra "20h" nas outras sete).

## 3.1 O expert não lê o teleprompter ao pé da letra — a legenda segue a fala

Confirmado em todos os clipes do lançamento do caso-base: o expert improvisa.
Fala o nome comprido do assunto onde a copy escreve o nome curto, "20 horas" onde
a copy escreve "20h", "online gratuito" sem o "e". Se a legenda vier da copy crua,
mostra uma coisa enquanto o áudio diz outra.

⚠️ **Uma exceção, aberta depois (num segundo negócio):** disfluência que o ASR
ouviu **não vai pra tela** — gaguejo e palavra cortada no meio ("de dor--",
"E te--"). Não é palavra, é ruído de fala. Fora isso a regra abaixo vale
inteira, e a exceção não autoriza reescrever frase.

**Regra:** a sequência exibida é a do **ASR** (o que saiu da boca do expert); cada
palavra que casou com a copy é trocada pela **grafia da copy** (acento,
pontuação, termos de marca). Palavra que não casou fica como o ASR ouviu.
No caso de origem, o script de legenda fazia isso e imprimia os desvios
encontrados. Quem gerar a legenda (script, agente ou editor) entrega essa lista, e
ela se confere sempre — é o sinal mais rápido de que o clipe é o roteiro certo.

Taxa de casamento observada: 91–96%. **Abaixo de 80% é sinal de que o clipe
não corresponde ao roteiro** — parar e reconferir.

## 3.2 Identificar clipe × roteiro: transcrever, não estimar

Duração x contagem de palavras serve pra separar corpo de CTA, mas **não**
pra dizer qual roteiro é qual (os roteiros têm tamanhos parecidos demais).
Transcrever os primeiros ~13s de cada clipe resolve em definitivo e é
barato. No caso-base, o mapa levantado primeiro por heurística de duração foi
**reconfirmado por transcrição real** (ElevenLabs Scribe, ferramenta externa, nos
14 brutos) uns dias depois. O que os 14 arquivos (nome genérico do iPhone, sem
dizer qual roteiro é qual) continham:

| Clipes | O que eram |
|---|---|
| 8 | os 8 roteiros de corpo, um por clipe (um deles com o take completo num arquivo e o falso início em outro) |
| 4 | os 4 CTAs: pago (controle, sem menção a sorteio), a variação do pago com sorteio, orgânico e de conteúdo |
| 1 | take furado (2,6s, só "Olha") — não é nenhum roteiro |
| 1 | falso início de um roteiro (o expert troca de ideia e recomeça, 6,3s) |

**Dois roteiros do plano não foram gravados** nesta leva — os 14 arquivos da
sessão cobrem 100% do corpo + CTAs + 2 takes furados, e nenhum abre com a fala
de nenhum dos dois. Confiança **alta**, por conteúdo de fala — deixou de ser
inferência por exclusão de duração.

## 3.3 CTA como módulo solto (decisão do Rodrigo)

Cada CTA é montado uma vez como **peça independente**, já com legenda, logo e
botão, normalizada em `loudnorm I=-16` — o mesmo alvo do corpo, pra emendar sem
degrau de volume. Assim troca-se o CTA sem reprocessar o corpo.

**O módulo sai SEM trilha.** A música entra só na montagem final; se cada
módulo trouxesse a sua, ao concatenar ficariam duas trilhas sobrepostas e
com corte seco no meio.

**Botão muda por CTA** — é a ação que o expert pede em voz:
| CTA | Fala | Botão |
|---|---|---|
| Pago | [pede o toque no botão SAIBA MAIS] | `SAIBA MAIS` |
| Orgânico | [pede o comentário com a palavra] | `COMENTE: [PALAVRA]` |
| Conteúdo | [pede o toque no botão SAIBA MAIS] | `SAIBA MAIS` |

## 3.4 Trilha: alternar entre criativos

**Atualização posterior (pedido literal do Rodrigo): uma trilha por peça,
nenhuma repetida.** Antes eram 4 faixas alternando em 8 peças (cada uma 2×);
baixamos mais 4 pra ter 8 distintas. ⚠️ **O preço:** a revisão técnica do mesmo
lote mediu **8 dB de variação entre trilhas** e **9 LU no fecho** com o mesmo
ganho — masterizações diferentes não respondem igual a um ganho único. Quanto
mais faixas, mais o problema aparece. A correção certa é normalizar cada faixa
(`loudnorm`) na entrada do kit de trilhas, não caçar ganho peça a peça. **Pendente
no caso de origem.**

Rodar os 10 com a mesma música faz o conjunto soar como um vídeo só.
Biblioteca montada no caso-base (todas Pixabay Content License, sem exigência de
atribuição):

1. `01-motivational-pop.mp3` (2:28)
2. `02-upbeat-happy-corporate.mp3` (2:02)
3. `03-upbeat-corporate.mp3` (2:07)
4. `04-corporate-upbeat.mp3` (2:03)

Trilha mais curta que o vídeo não é problema: a montagem usa
`-stream_loop -1` e corta na duração exata (cuidado ao juntar isso com `-ss` no
input: `sirius-scale/frameworks/copy/video-criacao-tecnica.md` §2.10).

Pra pegar o arquivo no Pixabay: o botão de download não expõe URL no HTML
(é gerado por JS). Dar play e ler
`document.querySelector('audio').currentSrc` devolve o link direto em
`cdn.pixabay.com`.

⚠️ **Licença, o que veio depois no mesmo caso (VARIAÇÃO ISOLADA, evidência no caso
de origem):** no Pixabay, conferir na página da faixa se ela é "Content ID
Registered" (está no JSON-LD da página). A licença continua comercial e sem
atribuição, mas faixa registrada pode gerar reivindicação automática na rede — numa
busca de trilhas de suspense, 18 de 19 eram registradas. Avisar na entrega. As levas
seguintes da casa passaram a usar Mixkit, conferindo a licença clipe a clipe.

## 3.5 Scripts prontos (é só trocar argumento)

> 🔴 **CORREÇÃO, feita depois: os scripts desta seção NÃO EXISTEM MAIS no disco
> do caso de origem.** Foram procurados nas pastas de trabalho e nenhum foi
> encontrado, nem a pasta de trilhas. Quem seguisse esta seção perdia uma sessão
> descobrindo isso. O substituto vivo foi um kit vertical de scripts,
> reconstruído do zero na mesma data (montagem vertical e 16:9, headline, logo,
> revisão de legenda, end cards, títulos).
> Mesma doença que o `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §4.1 já diagnosticou: **o doc aponta
> pra código, o código some, e o doc continua prometendo.** Fonte única do valor
> é o kit; o doc guarda o porquê.

Nenhum desses scripts faz parte deste kit. Fica o desenho, que serve de mapa pra
quem for automatizar (ou pra dividir o trabalho com um editor):

| Peça do pipeline | O que faz |
|---|---|
| Legenda (recebe: o master, a peça, a saída, palavras extras de destaque) | ASR + alinhamento + `.ass` com pop e destaque |
| Overlays (recebe: o texto da headline, o emoji, um prefixo) | headline/logo/botão do criativo |
| Montagem (recebe: master do corpo, legenda, overlays, master do CTA, legenda do CTA, ponto de corte, duração do CTA, trilha, saída, tempo do logo e do botão) | criativo completo (~45s) |
| Módulo de CTA (recebe: master, legenda, overlays, tempo do logo e do botão, saída) | módulo de CTA solto |

⚠️ O shell das sessões do caso de origem é **zsh**: `set -- $var` não separa por
espaço como no bash. Não usar esse padrão em laço — escrever as chamadas
explícitas.

## 3.6 Ênfase: critério vem da copy, dose vem de curadoria — *VARIAÇÃO ISOLADA*

Duas rodadas foram reprovadas por causa disso. O que ficou:

**O critério não pode ser inventado.** Eu tinha criado uma lista de ~25
"palavras-chave" (termos do assunto do expert) e pintava tudo que
batesse — dava **41% dos blocos coloridos**, e o Rodrigo leu como
"mecânico, sem critério". O certo já estava no material: **a copy marca a
ênfase em CAIXA ALTA** (NÃO, MINHA, CERTEZA...). É a escolha
do copywriter, não palpite do editor. Com isso caiu pra ~12%.

**Mas a dose não pode ser automática.** Os 8 roteiros do lançamento têm de
**0 a 5** palavras em caixa alta:

| Peça 1 | Peça 2 | Peça 3 | Peça 4 | Peça 5 | Peça 6 | Peça 7 | Peça 8 |
|---|---|---|---|---|---|---|---|
| 5 CAPS + 7 nº | 3 + 0 | 2 + 1 | 1 + 2 | 1 + 1 | 1 + 1 | 1 + 0 | **0 + 1** |

Aplicar a mesma regra nos 8 não deixa "tudo igual" — deixa **desigual**: a
peça 1 sai rica e a peça 8 sai pelada. Por isso existia uma etapa de
**curadoria** no lote: 1-3 palavras por vídeo, escolhidas lendo o roteiro (a
palavra que carrega a tese daquele texto), sempre conferindo que a palavra
**existe no texto**. Nivela em 3-5 destaques por vídeo.

**Movimento segue a mesma lógica.** Fazer todo bloco deslizar (rodízio de
4 direções) foi reprovado como "engessado": o movimento não significava
nada. Regra: **bloco comum só respira** (fade + micro-escala com
desaceleração); **deslize é reservado ao bloco de ênfase**.

**Teto de marcação:** 3 sublinhados e 2 círculos por vídeo. Marcar as 10
palavras polui tanto quanto não marcar nenhuma.

## 3.7 Onde parar de automatizar — *decisão do Rodrigo*

Tentei transformar uma enumeração do roteiro (quatro conceitos do assunto) numa
lista que monta item a item com emoji. Reprovado, e o motivo importa mais que a
peça: **eu escolhi os emojis** (um por conceito) sem critério nenhum — decoração
arbitrária. E rodar isso nos outros 7 roteiros produziria mais escolhas
ruins, porque decidir *se aquele momento merece* é julgamento editorial.

Regra: recurso que depende de "este trecho merece um tratamento especial?"
**não entra na batelada**. Fica como sugestão pra um humano decidir por
peça. O pipeline cuida do sistemático (sincronia, enquadramento, áudio,
formatos, estilo); a curadoria fica com gente.

## 3.8 Medir o que foi renderizado, não calcular — *VARIAÇÃO ISOLADA*

Pra desenhar sublinhado/círculo em cima da palavra é preciso saber onde ela
caiu. Calcular a largura do texto com PIL **não bate com o libass**: deu
447px onde o real era 244px, e o traço saía comprido demais.

Solução: a palavra de ênfase é colorida, então **renderiza-se um frame e
procura-se o pixel daquela cor** — a caixa delimitadora é a posição exata.
Custa ~10 frames por vídeo/formato. Cuidado: o limiar de nº de pixels
precisa ser baixo (~110), senão número de **um dígito** (do tipo "5 horas")
não é detectado e o vídeo sai sem círculo.

Traço deve terminar **antes** da legenda (`fim - 0.06`), nunca depois —
senão fica órfão na tela depois que a palavra some.

## 3.9 Armadilhas de shell e de log que custaram rodada

- **zsh aborta a linha inteira quando um glob não casa.** `rm -f a_*.x b_*.y`
  com `b_*.y` vazio **não apaga nem `a_*.x`**. Resultado: os vídeos antigos
  sobreviveram e a batelada os deu por prontos, "corrigindo" nada. Usar um
  `rm` por padrão, ou `setopt NULL_GLOB`.
- **O script de upload pra nuvem imprimia uma palavra diferente ao substituir
  arquivo** ("Sobrescrito", não "Enviado"). Checar só a palavra de sucesso do
  envio novo fazia **toda correção** aparecer como falha no log, mesmo tendo
  funcionado — quase reportei erro que não existia. Aceitar as duas palavras (ou
  conferir pelo arquivo no destino).
- **Processo morto no meio da escrita deixa mp4 truncado**, e "o arquivo
  existe" não significa "está pronto". Validar abrindo (`ffmpeg -v error -i
  arq -f null -t 1 -`) antes de reaproveitar em execução retomada.

## 3.9.0 Número de layout não se move sozinho

Baixar a legenda (MarginV 770 → 620, a pedido do Rodrigo) moveu a faixa de texto
de y 1010–1150 pra **1235–1375**. O logo do evento estava em 1215–1410: passou a
ficar **por cima da legenda** nas peças em que aparece. As 8 já tinham sido
renderizadas e conferidas — o defeito só apareceu no contact sheet do lote,
porque o logo entra por 3,4s e não está no frame que se olha por padrão.

**Regra:** todo número de posição vertical vive num orçamento compartilhado de
1920px. Ao mexer em um, listar o que mais ocupa a coluna e conferir num frame em
que os dois coexistem — não no primeiro frame da peça.

No kit vertical do caso-base, depois da correção: headline 240–464 · logo
880–1075 · legenda ~1235–1375 · piso da zona segura 1625.

## 3.9.1 Headline: onde ela mora numa peça de várias vozes — *VARIAÇÃO ISOLADA*

A regra até aqui era **headline o tempo todo na tela** (§2), e ela continua
valendo — mas nasceu nas peças em que o expert está em cena do primeiro ao
último frame. Numa peça que **troca de dono no meio** (abertura do expert →
depoimentos de alunos → fecho do expert), manter a headline no miolo foi reprovado:

> "A headline ainda fica aparecendo em cima dos depoimentos e ficou bem
> esquisito." — Rodrigo

Dois motivos, e os dois transferem:

1. **Material de terceiro costuma trazer legenda queimada.** No miolo passam a
   existir dois sistemas de texto na mesma tela, e nenhum manda.
2. **A headline costuma ser a CONCLUSÃO da peça.** Aqui era uma headline do tipo
   [o que os casos não têm / o que eles têm em comum], e a peça inteira é a
   demonstração disso. Deixá-la na tela o tempo todo entrega o final antes da prova.

**Regra:** a headline vive nas janelas em que o expert está em cena. Sai quando
a prova entra, **reentra com a mesma animação** quando ele volta — e a reentrada
cai junto com a frase que ela resume, virando selo em vez de placa. No kit do
caso-base isso era automático: as janelas saíam dos trechos marcados como "do
expert" na montagem.

## 3.9.2 Chip: só quando carrega fato — *VARIAÇÃO ISOLADA*

O chip abaixo da headline existe pra dar **fato que muda a decisão** — prazo,
novidade, nome do produto. `AULA [N] · [DIA] [HORA] · AO VIVO` é fato. `MATRÍCULAS
ABERTAS` durante o carrinho aberto **não é**: se o anúncio está no ar naquela
fase, estão abertas, e o end card já diz isso com a data. Chip redundante gasta
área nobre e, sobre material de terceiro, ainda compete com a legenda dele.

Aplicado nas 11 peças de carrinho do lançamento do caso-base: o chip ficou em 6
(o dia 1 do carrinho, o boleto, o prazo em duas peças, a reabertura e o nome do
produto) e saiu das outras 5, que só diziam `MATRÍCULAS ABERTAS`.

## 3.9.3 Headline animada: a hierarquia é do layout, não do efeito — *VARIAÇÃO ISOLADA*

Duas caixas do mesmo corpo empilhadas foi reprovado como "muito padrãozinho":
nada na peça dizia qual das duas linhas importa. O que resolveu **não foi mais
efeito** — foi degrau de layout: L1 a 44px em caixa navy (contexto, caixa alta,
letra espaçada) e L2 a 86px em caixa dourada com texto navy (a virada da frase),
mais um filete que cresce sob a L2. (Navy e dourado são as cores do caso-base.)

O motion entra por cima disso, um elemento de cada vez: cada linha sobe **de
dentro de uma máscara** (não aparece com fade, que é o efeito barato), a L2 mais
lenta e com mais curso que a L1 porque é ela que carrega a frase, e o chip pousa
por último. Entrada de 2,6s, depois congela.

⚠️ As duas linhas ficam **sobre caixa**, não soltas: o fundo alterna entre a
parede clara do expert e o preto dos depoimentos, e texto solto perde contraste
num dos dois — que é exatamente o que já tinha sido reprovado antes.

## 3.10 Versão 16:9 (YouTube) — o que muda *(VARIAÇÃO ISOLADA)*

> ⚠️ Esta receita se declara "criativo vertical (Reels/Stories)" no título. A
> seção existe pra o arquivo parar de mentir sobre o que cobre: no caso-base
> saíram 8 peças em 16:9 do mesmo material.

**O 16:9 não é o vertical reenquadrado.** O vertical tem headline, chip e legenda
queimados em posição de 9:16; qualquer zoom os corta. O 16:9 é **cortado do 4K
original**, com overlays e legenda próprios.

| | Vertical (Instagram) | 16:9 (YouTube) |
|---|---|---|
| Imagem | crop 9:16 do 4K | corte 16:9 do 4K, **sem borrão lateral** |
| Título | headline fixa a peça inteira | entra, fica ~4,5s e **sai** |
| Legenda | blocos de até 3 palavras | **frase inteira**, 1–2 linhas |
| Quebra da legenda | contagem de palavras | **pausa real da fala** |
| Contorno | sombra, sem outline | **borda fina** (ver §2) |

**Por que a legenda muda:** tela pequena com scroll lê em blocos curtos; tela
grande, com a pessoa sentada assistindo, não — bloco de 3 palavras pisca sem
parar. Medido no mesmo material: **44 blocos no vertical contra 14 no 16:9**.
⚠️ Isso é argumento de legibilidade, **não medição de efeito** — ninguém comparou
retenção nem compreensão entre os dois formatos.

**Em bloco de 2 linhas, cada linha entra quando a fala chega nela**, não as duas
juntas: com as duas nascendo ao mesmo tempo, a de baixo fica parada esperando e a
legenda deixa de acompanhar a leitura.

**Movimento na legenda foi testado e reprovado**: destaque correndo
palavra a palavra (`\kf` do ASS, sincronizado pelos tempos do Scribe). Mesma
família do §3.6 — movimento tem que significar alguma coisa. **O que acompanha a
fala é a entrada da linha, não o preenchimento.**

**Qualidade:** o corte 16:9 quase não tem folga de downscale (1,13 pixel de origem
por pixel final, contra 1,77 do vertical). Sem tratamento, o ruído do sensor passa
pro encode e a peça **parece pior mesmo vindo de 4K**. Valores usados:
`hqdn3d=2:1.5:3:3` antes do encode, `scale=...:flags=lanczos`,
`unsharp=5:5:0.55:3:3:0.0`, bitrate final de 20 Mbps (era 12). O mecanismo está em
`sirius-scale/frameworks/copy/video-criacao-tecnica.md` §6.

**End card entra DEPOIS da fala, não sobreposto** *(decisão do Rodrigo)*. Eu tinha
implementado cobrindo os últimos segundos, com o argumento de que esconder a boca
do expert viabilizaria trocar o áudio do CTA na versão orgânica. Ele preferiu
preservar o fecho que o expert gravou: *"ela precisa falar a copy até o
final, aparecendo ela, e depois que ela acaba de falar o banner entra, o som
aumenta e fica só a música e o banner"*. A peça estica em vez de encolher. ⚠️
Consequência aberta: a versão orgânica precisa de outra solução pra dessincronia
labial.

## 4. Onde entregar

Na pasta de criativos do lançamento, no drive do cliente, dentro da fase:
`1) BRUTO` (gravação crua) e `2) EDITADO/<formato>` (`STORIES`, `FEED`,
`YOUTUBE`, `REELS`). Usar a estrutura que o cliente já tem, sem criar pasta nova.
Nome: `<lançamento>-<peça> - REELS - <gancho>.mp4`.
Bruto fica na nuvem — baixar só o arquivo necessário, processar numa pasta
temporária, subir, apagar a cópia local.

## 5. Ordem de execução

```
1. baixar o bruto da nuvem (só o que precisa)
2. identificar clipe x roteiro (duração x contagem de palavras, confirmar por transcrição e frame)
3. detectar silêncio pra achar o corte limpo (início/fim)
4. render dos MASTERS 1080p            <- passo caro
5. extrair áudio -> ASR -> alinhar com a copy -> .ass
6. gerar overlays (headline, logo, botão) em PIL
7. aplicar texto+motion nos masters, juntar, mixar   <- passo rápido, itera aqui
8. conferir: sincronia em 5 pontos, volume, frames-chave
9. subir pra nuvem, limpar local
```

## 6. Pendências / próximos passos

- **Motion mais avançado** (seta desenhando, texto que "digita", zoom sutil
  no clipe) ainda não implementado — a referência do editor tem isso.
- **B-roll:** a referência do editor **não usa nenhum**. Antes de investir em
  geração por IA, testar uma peça com e uma sem, e comparar por custo por MQL.
- **Geração de vídeo por IA** (b-roll com controle de câmera, avatar) depende de
  conector autorizado na conta; no caso de origem ficou de fora por isso. Sem
  autorização, b-roll gerado por IA não entra.

---

## 4. O que transfere e o que é do caso

**Transfere como processo (qualquer cliente, qualquer empresa):**

- **§0, o passo que mais economiza rodada:** pedir uma peça já editada pelo
  editor do cliente **antes** de tocar em arquivo. Foi assim que o padrão real
  apareceu aqui, e é assim que se descobre o padrão do próximo. Em cliente novo,
  este passo não é opcional — é o que substitui os números do §2.
- **§1, a arquitetura de render em 2 passos** (master limpo primeiro, texto
  depois). Vale pra qualquer peça.
- **§3, o método de sincronia** — ASR só pro tempo, copy pro texto — e o §3.1
  (a legenda segue a fala real, não o teleprompter). Isso é sobre como pessoa
  fala, não sobre este expert.
- **§3.2** — identificar clipe × roteiro transcrevendo, nunca estimando por
  nome de arquivo ou duração.
- **§3.3** — CTA como módulo solto, pra recombinar corpo e CTA sem reeditar.
- **§3.6** — critério de ênfase vem da copy, dose vem de curadoria.
- **§3.7** — onde parar de automatizar.
- **O encoder de hardware no passo de texto** e o ferramental (`imageio-ffmpeg`
  com binário estático) — técnico, vale em qualquer projeto numa máquina igual (Mac).

**Transfere, apesar de morar no §2:** as duas notas de legenda abertas depois
(bloco balanceado em vez de corte por contagem; e repartir o tempo na
proporção dos tokens quando a revisão muda a contagem de palavras). São
**método**, vieram de um segundo negócio e não do caso-base, e valem em qualquer
cliente — o que continua sendo padrão do editor do caso-base é só o número "3".

**Não transfere — é o padrão visual do editor do caso-base:**

- **Todo o §2.** Fonte, corpo, posição da legenda, cor, tamanho e posição da
  headline, tratamento do logo, níveis de áudio, tipo de transição, timings de
  entrada/saída e a dose de motion. Cada um desses números foi calibrado
  olhando **aquela** referência do editor do expert e aprovado **pelo Rodrigo** —
  o expert nunca validou nenhum deles. Em outro cliente, copiar isso entrega
  uma peça que parece de outra marca.
- **§3.4** (alternância de trilha entre criativos) e a decisão sobre B-roll —
  são escolhas daquela linha criativa.
- As convenções de pasta e nomenclatura de entrega do cliente.

**Regra de aplicação em cliente novo:** rode o §0, meça a referência do editor
dele como está feito em `sirius-scale/frameworks/copy/edicao-video-referencia-editor.md`, e **escreva um §2
novo** com os números dele. Não edite os números daqui — escreva o §2 de vocês em
`frameworks-da-casa/` (este arquivo é trocado inteiro a cada versão do kit, e o
padrão do caso-base continua valendo como referência).
