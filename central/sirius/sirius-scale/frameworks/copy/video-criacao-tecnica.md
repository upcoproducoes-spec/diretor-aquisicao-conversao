# Vídeo — armadilhas técnicas da cadeia de render

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** ferramenta. Aqui só entra o que é **fato da ferramenta**, sem
> dimensão de cliente: ffmpeg, libass/ASS, HyperFrames, Unicode.
> **Alcance: UNIVERSAL por construção.** Número que depende do editor ou da
> marca **não entra aqui** — mora em `sirius-scale/frameworks/copy/edicao-video-receita.md` (estilo aprovado
> pelo cliente) ou no kit de scripts de quem edita (valor operacional).
>
> Segue a convenção dos outros arquivos técnicos do kit
> (`sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`, `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`,
> `sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md`): a "plataforma" aqui é a cadeia de render.
>
> **Ferramentas:** ffmpeg (com libass) e HyperFrames (composição de vídeo em
> HTML/GSAP, com CLI própria) são ferramentas externas, instalam à parte. Quem
> edita no CapCut ou com editor humano usa as entradas de áudio (§2), de texto
> (§5) e de escala (§6) como checklist do arquivo exportado; o resto só morde
> quem renderiza por comando.

## Como ler cada entrada

Todas seguem quatro campos, e o quarto é o que separa playbook de lista de erros:

**sintoma observável** → **o que estava no comando** → **o que corrige** →
**como confirmar que corrigiu**

## §0. Antes de renderizar — carimbe a versão

Metade destas armadilhas é dependente de versão. Sem carimbo, a nota apodrece e
alguém descarta a solução certa achando que é superstição.

| Ferramenta | Versão em que foi medido | Como conferir |
|---|---|---|
| ffmpeg | 6.0 (build estático arm64) | `ffmpeg -version` |
| HyperFrames | 0.8.30 | `npx hyperframes --version` |
| Fontes | a pasta de fontes do projeto (Poppins, no caso de origem) | passar sempre `fontsdir` |

⚠️ **O pipeline do caso de origem chamava `hyperframes@latest`** — alvo móvel. Ao
revisitar §4, confira a versão antes de concluir que a armadilha sumiu (ou que voltou).

---

## §1. ffmpeg — imagem parada como overlay

### 1.1 `fade` não roda em stream de UM frame

- **Sintoma:** o overlay simplesmente não aparece. Sem erro, sem aviso, código 0.
- **No comando:** `-i logo.png` + `fade=t=in:st=2.36:d=0.35:alpha=1`
- **Corrige:** `-loop 1 -i logo.png`. Um PNG sozinho é um stream de 1 frame, e
  filtro que depende de tempo não tem frames onde acontecer.
- **Confirma:** extrai um frame dentro da janela do fade e conta pixels visíveis.

### 1.2 …mas `-loop 1` sem `-t` é input INFINITO

- **Sintoma:** o render não termina. Medido no caso de origem: arquivo passou de
  **692 MB** e continuava crescendo, para um vídeo de 48s a 12 Mbps (~72 MB
  esperados).
- **No comando:** `-loop 1 -i logo.png`
- **Corrige:** `-loop 1 -t <duração_da_peça> -i logo.png`
- ⚠️ **`-shortest` NÃO segura.** Ele fecha no menor stream **finito**; com dois
  inputs infinitos na cadeia (o `-loop 1` e uma trilha em `-stream_loop -1`),
  não há finito pra fechar.
- **Confirma:** o tamanho do arquivo bate com `duração × bitrate`.

---

## §2. ffmpeg — áudio

### 2.1 `alimiter` vem com `level=true` e reamplifica pra 0 dB 🔴

**A mais cara desta família: o filtro roda, aparece no comando e não faz o que
o nome diz.**

- **Sintoma:** o pico não cai. Pior: o **loudness sobe**.
- **No comando:** `alimiter=limit=0.84` (ou qualquer `limit` sem `level`)
- **Corrige:** `alimiter=limit=0.84:level=disabled`
- **Por quê:** o default `level=true` normaliza o sinal de volta pra 0 dB depois
  de limitar — ele comprime e reamplifica.
- **Medido (ffmpeg 6.0):** mesmo arquivo, mesmo `limit`.
  Com o default: `volumedetect` → `0.0 dB`, true peak **+0,7 dBFS**, loudness
  **2 LU mais alto**. Com `level=disabled`: `volumedetect` → **−1,5 dB**.
- **Confirma:** `ffmpeg -i saida.mp4 -af volumedetect -f null -` e
  `-af ebur128=peak=true`. Se o `max_volume` não caiu, o limiter não atuou.

⚠️ Esta armadilha já estava **prescrita errada** em 5 lugares da biblioteca do caso
de origem (a receita §2, o framework de edição de criativos, o mapa de edição, o
prompt de sistema do gerador e a skill `/mapa-edicao`). Todos foram corrigidos. Se
achar `alimiter` sem `level=disabled` em qualquer receita, é este erro.

### 2.2 O AAC introduz overshoot intersample DEPOIS do limiter

- **Sintoma:** o sample peak está correto e o **true peak passa de 0 dBFS**.
- **Por quê:** o limiter atua no PCM; a codificação AAC acontece depois e
  reconstrói picos entre amostras.
- **Corrige:** deixar margem. `limit=0.84` (≈ −1,5 dBFS) — que é o mesmo alvo de
  `TP` que a cadeia de voz já usa no `loudnorm`.
- **Medido:** com sample peak em −0,54 dBFS, o true peak saiu em **+0,3 dBFS**.
- **Confirma:** `-af ebur128=peak=true`, e olhar **True peak**, não `max_volume`.

### 2.3 `-v error` apaga a saída do `volumedetect` (e de todo filtro de medição)

- **Sintoma:** o parse da medição volta **vazio**, a função cai no valor padrão
  e segue como se tivesse medido. Nenhum erro.
- **No comando:** `ffmpeg -v error -i x.mp3 -af volumedetect -f null -`
- **Por quê:** `volumedetect`, `ebur128` e afins imprimem em nível **info**;
  `-v error` filtra tudo abaixo de erro, inclusive o resultado.
- **Corrige:** rodar a medição **sem** `-v error` e parsear o `stderr`.
- **Confirma:** imprimir a linha crua antes de converter pra número — se vier
  lista vazia, é isto.
- ⚠️ Vale só pra **medir**. No render, `-v error` continua certo.

### 2.4 O limiter da voz não protege o mix

Se a trilha entra por `amix` **depois** do `alimiter` da voz, o pico final não
está limitado por nada. Ordem correta: `amix` → `alimiter:level=disabled` →
`aresample=48000`.

### 2.5 `loudnorm` devolve áudio em 96/192 kHz

*(migrado de `sirius-scale/frameworks/copy/edicao-video-criativos.md` §9.2)*

- **Sintoma:** o MP4 final sai fora do padrão de 48 kHz que as plataformas
  esperam.
- **Corrige:** fechar a cadeia com `aresample=48000` **e** `-ar 48000`.
- **Confirma:** `ffprobe -show_entries stream=sample_rate` no arquivo entregue.

---

## §2.9 Reaproveitar vídeo JÁ EDITADO como fonte

Três coisas que só aparecem quando a fonte não é bruto, e todas foram medidas
numa peça de carrinho do caso de origem (montagem de 5 depoimentos tirados de um
reel de um lançamento anterior). `ALCANCE: UNIVERSAL` — é da natureza do material,
não do cliente.

**Sintoma:** a trilha do vídeo de origem fica "esquisita" depois dos cortes.
**O que estava no comando:** os trechos foram extraídos direto do mp4 final,
com o áudio como ele veio.
**O que corrige:** separar a voz antes (`demucs --two-stems=vocals`, ferramenta
externa) e usar só a faixa `vocals` nos cortes; a música é a NOSSA, contínua sob a
peça inteira. Cortar 5 trechos de lugares diferentes pica a música de origem em 5
pedaços sem relação nenhuma entre si — e nenhum ajuste de volume conserta isso,
porque o problema é a descontinuidade, não o nível.
**Como confirmar:** medir `volumedetect` num vão entre falas antes e depois. Na
peça: o vão em 79,5s tinha −48,9 dB de música e foi a −81,3 dB na faixa separada,
enquanto a fala em 168s ficou intacta (−23,2 → −23,4 dB). Se a voz caiu junto,
a separação errou.
⚠️ `demucs` precisa de `soundfile` instalado, senão morre **na hora de gravar**
com `Couldn't find appropriate backend` — depois de já ter feito todo o trabalho.

**Sintoma:** o crossfade entre dois trechos fica ilegível no meio.
**O que estava no comando:** `xfade=transition=fade` (dissolve).
**O que corrige:** `transition=fadeblack`. Vídeo já editado costuma ter legenda
**queimada**, e o dissolve mostra as duas legendas sobrepostas durante toda a
transição. Passando pelo preto, some uma antes de a outra entrar.
**Como confirmar:** extrair o frame do MEIO da transição (`offset + duração/2`),
não os das pontas — nas pontas o defeito não existe.

**Sintoma:** áudio e vídeo escorregam ao longo de uma montagem de N trechos.
**O que estava no comando:** `xfade` no vídeo (offset absoluto) com
`acrossfade` encadeado no áudio.
**O que corrige:** `adelay` na posição absoluta de cada trecho + `amix`, e
`apad` no fim de cada clipe pra o áudio nunca ficar mais curto que o vídeo.
`acrossfade` cruza sempre no FIM do stream anterior, então qualquer diferença
entre duração de áudio e de vídeo vira dessincronia — que **soma** a cada
emenda. Usar a duração medida por `ffprobe` de cada clipe já encodado, nunca a
duração pedida: `-r 30` arredonda pro frame.
**Como confirmar:** transcrever o render e comparar o tempo de uma palavra de
cada trecho com a posição calculada. Na peça os 6 pontos bateram (ex.: "décimo"
previsto em 15,56s, medido em 15,56s).

## §2.10 `-ss` no input + `-stream_loop` — o `t` do filtro atrasa

**Sintoma:** a trilha "demora a subir" no end card — o card entra e a música
só cresce ~1,8s depois. O Rodrigo ouviu; estava assim em todas as 19 peças do lote.
**O que estava no comando:** `-stream_loop -1 -ss 2.0 -i trilha.mp3` e, no
filtro, `volume='if(lt(t,46.5),0.045,…)':eval=frame`.
**O que corrige:** tirar o `-ss` do input e cortar dentro do filtergraph:
`-stream_loop -1 -i trilha.mp3` + `atrim=start=2.0,asetpts=PTS-STARTPTS,volume=…`.
Com `-ss` no input e loop em mp3, o `t` que o filtro enxerga não é o tempo
de saída — chega deslocado por quase o valor do `-ss`. `asetpts` sozinho
depois do `-ss` **não** conserta (testado); só o `atrim` conserta.
**Como confirmar:** isolar a trilha com o mesmo filtro (`-f null` não serve —
gravar um wav) e medir `volumedetect` em janelas de 0,2s ao redor do ponto de
subida. Antes: −37 dB em 47,0s e −15 dB só em 49,0s. Depois: −23 dB em 46,6s,
−18 dB em 47,0s.

## §3. libass / formato ASS

### 3.1 Sem `fontsdir`, o libass cai em fonte substituta SEM avisar

*(migrado de `sirius-scale/frameworks/copy/edicao-video-criativos.md` §9.2 — era UNIVERSAL
morando num arquivo de um cliente só)*

- **Sintoma:** a peça inteira sai na fonte errada, sem nenhum erro no log.
- **Por quê:** `-vf subtitles=x.ass` resolve o `Fontname` via fontconfig, ou
  seja, só acha fonte **instalada no sistema**. Baixar o `.ttf` numa pasta não
  basta.
- **Corrige:** `subtitles=x.ass:fontsdir=/caminho/das/fontes`. O `Fontname` é o
  nome da **família** (`Poppins`), com `Bold: -1` pra escolher o peso — não
  "Poppins Bold".
- **Confirma:** ampliar um frame entregue. (O "a" da Poppins é de um andar,
  geométrico; o do Helvetica é de dois.) Ou comparar pixel a pixel contra um
  re-render com a fonte esperada.

### 3.2 O formato ASS não tem controle de entrelinha

- **Sintoma:** as duas linhas de um bloco ficam com um vão grande demais, e não
  há parâmetro pra mudar.
- **Por quê:** quebrando com `\N`, a distância entre linhas vem da **métrica da
  fonte**. A Poppins tem métrica generosa.
- **Corrige:** cada linha vira um evento `Dialogue` próprio, com
  `{\an5\pos(x,y)}` e o `y` calculado como múltiplo do corpo da fonte.
- **Nota:** o mesmo mecanismo morde fora do ASS. Em PIL, somar
  `ascender + descender` da Poppins mais padding dá altura de linha **2,0× o
  corpo**; usar múltiplo do corpo (1,45) resolve. *(O multiplicador é da Poppins
  — VARIAÇÃO ISOLADA; o mecanismo é universal.)*

---

## §4. HyperFrames

> Medido na **0.8.30**. Confira a versão antes de concluir que mudou.

### 4.1 `--format webm` sai VAZIO quando a composição tem alpha 🔴

- **Sintoma:** arquivo pequeno (11,5 KB para 102 frames), `ffprobe` lê normal,
  e **zero pixels com alpha > 10** em qualquer frame. Sem erro, sem aviso.
- **Corrige:** `--format png-sequence` (escreve frames RGBA) e ler no ffmpeg com
  `-framerate 30 -i frames/frame_%06d.png`.
- **Confirma:** abrir um frame do meio e contar pixels com alpha > 10.
- *(Com 5 `filter: drop-shadow()` empilhados o alpha também vinha zerado; não
  separamos esse efeito do bug do formato — não trate como causa própria.)*

### 4.2 `-o` é resolvido relativo ao cwd do RENDER

- **Sintoma:** o arquivo não aparece onde você pediu, e uma árvore de diretórios
  inteira surge dentro do projeto HyperFrames.
- **No comando:** `render . -o /caminho/absoluto/saida.mp4` com `cwd=<projeto>`
- **Corrige:** passar nome simples e mover depois.

### 4.3 O `check` pega o que o olho não pega

Vale rodar sempre antes de renderizar. Dois achados reais no caso de origem:
`transform` no CSS sendo sobrescrito por um tween GSAP que anima `y` (a
centralização era descartada), e estado inicial em `tl.set(...)` na posição 0 —
que **não renderiza** com o playhead parado em 0, deixando o frame 0 com tudo
visível. Correções: `xPercent` no GSAP em vez de `transform` no CSS, e
`gsap.set()` imediato (fora da timeline) para estados iniciais.

### 1.3 Overlay em `-loop 1` é decodificado em TODO frame, mesmo escondido

*(migrado de `sirius-scale/frameworks/copy/edicao-video-criativos.md` §9.2.1 — já era UNIVERSAL lá)*

- **Sintoma:** o render projeta mais de uma hora onde deveria levar minutos.
- **Medido (num segundo negócio):** 23 PNGs de 1080×1920 passados assim num criativo
  de 85s → ~49 mil decodes; 18 MB em 13 min, com projeção de +1h.
- **Por quê:** o `enable` esconde o overlay na composição, mas o decode acontece
  de qualquer jeito.
- **Corrige:** pré-compor **todos** os overlays num único vídeo com alpha (PIL
  frame a frame → `rawvideo rgba` no stdin do ffmpeg → `qtrle -pix_fmt argb`) e
  passar **um** overlay pro render final.
- **Confirma:** tempo de render por minuto de vídeo.

### 1.4 `crop` NÃO reavalia `w`/`h` por frame — só `x`/`y`

*(migrado de `sirius-scale/frameworks/copy/edicao-video-criativos.md` §9.2.1)*

- **Sintoma:** zoom via `crop=w='iw/(1+0.03*t)'` fica **parado no primeiro
  valor**, em silêncio.
- **Corrige:** `scale=w='...t...':h=-2:eval=frame` seguido de `crop=<w>:<h>`, ou
  `zoompan`. Vale igual pra "linha crescendo" — não é `crop` com `t`.
- **Confirma:** extrair dois frames distantes e comparar o enquadramento.

---

## §4.7 Posicionar clip por `right`/`bottom` — o elemento sai do quadro

**Sintoma:** o logo aparece no canto SUPERIOR, cortado pela metade, num card
onde o CSS manda ele pro canto inferior.
**O que estava no comando:** `#logo { right: 70px; bottom: 58px; }`.
**O que corrige:** `#logo { left: 1420px; top: 828px; }` — sempre `left`/`top`,
com o número calculado. O container do `#root` não tem altura resolvida no
runtime, então `bottom: 58px` ancora 58px acima de uma caixa de altura zero, que
fica no topo da página. `top` funciona porque a origem do container é 0 — por
isso a composição vertical (que usa `top`) nunca mostrou o problema.
**Como confirmar:** extrair um frame do card e olhar. Vale a régua da zona
segura junto (`sirius-scale/frameworks/design/margens-seguranca-vertical.md`): `drawbox` nas duas linhas antes
de aprovar.
⚠️ Isto passou por **oito peças renderizadas, subidas na nuvem** e só foi
percebido pelo cliente. O `check` não pega — do ponto de vista dele o elemento
está posicionado, só que fora da tela.

## §4.8 `Math.random()` numa composição — a animação pisca

**Sintoma:** um efeito com fase aleatória (faísca, partícula, ruído) treme ou
pisca em vez de correr.
**O que estava no comando:** `el.dataset.fase = -L * Math.random()`.
**O que corrige:** PRNG com semente derivada do índice do elemento — mulberry32
resolve em 6 linhas. O render é **frame a frame** e reexecuta o script, então
`Math.random()` devolve valor diferente a cada frame: cada frame nasce de um
layout diferente.
**Como confirmar:** `hyperframes check .` acusa como `non_deterministic_code` —
é erro, não aviso. Rodar o `check` DEPOIS de cada mudança de script, não só ao
criar a composição.

## §4.9 `repeat: -1` numa composição — o loop não roda

**Sintoma:** animação contínua (pulso, loop de fundo) sai congelada no render,
sem erro nenhum.
**O que estava no comando:** `repeat: -1` num tween da timeline.
**O que corrige:** `repeat` finito que cubra a duração do card
(`Math.ceil(dur / duração_do_ciclo)`).
**Por quê:** o render move o playhead de uma timeline pausada, frame a frame.
Duração infinita não tem posição definida pra seekar.

## §5. Texto e Unicode

### 5.1 Faixa larga de emoji engole pontuação tipográfica

- **Sintoma:** um caractere **some da peça entregue**, sem erro.
- **No código:** `if ord(c) > 0x2000` para detectar emoji.
- **Por quê:** `…` (U+2026), travessão e aspas curvas caem nessa faixa, viram
  "emoji", e o rasterizador devolve vazio.
- **Corrige:** testar contra as faixas reais — U+1F300–1FAFF, U+2600–27BF,
  U+2B00–2BFF, U+1F1E6–1F1FF, mais o seletor U+FE0F.

### 5.2 Apple Color Emoji só rasteriza em 96 ou 160px

Já na receita §2 (`sirius-scale/frameworks/copy/edicao-video-receita.md`). Renderizar em 160 com
`embedded_color=True` e reduzir.

---

## §6. Escala e nitidez

### 6.1 Corte que cruza a orientação perde a folga de downscale

**A regra que transfere:** quando o destino tem orientação diferente da fonte, a
dimensão comum fica travada e **não sobra folga de downscale** — o material sai
quase 1:1 e o ruído do sensor passa direto pro encode.

Medido no caso de origem, mesma fonte 4K vertical (2160×3840):

| Destino | Corte → saída | Razão linear | Bitrate a `crf 18` |
|---|---|---|---|
| Vertical 1080×1920 | 1912×3400 → 1080×1920 | **1,77** | 11,5 Mbps |
| 16:9 1920×1080 | 2160×1215 → 1920×1080 | **1,13** | **7,75 Mbps** |

*(razão linear por eixo; em área são 3,14 contra 1,27)*

O 16:9 gastou 34% menos bits no mesmo `crf` porque tinha menos detalhe real e
mais ruído — e o resultado **parece pior**, mesmo vindo de 4K.

- **Corrige:** `hqdn3d` antes do encode (o codec para de gastar bits em grão),
  `scale=...:flags=lanczos` no lugar do bilinear padrão, e `unsharp` leve pra
  devolver micro-contraste.
- **Confirma:** comparar em **zoom 1:1** (pixels reais, sem reescala) numa região
  de detalhe fino — sobrancelha, cílios, textura de cabelo.
- ⚠️ Os valores usados (`hqdn3d=2:1.5:3:3`, `unsharp=5:5:0.55:3:3:0.0`, 20 Mbps)
  são **VARIAÇÃO ISOLADA / NÃO TESTADO FORA** e moram na receita, não aqui. O que
  é universal é o mecanismo.

---

## §7. Geração em lote a partir de template

**Tudo que muda por peça precisa ser parametrizado, e a conferência é do LOTE.**

Num lote do caso de origem, o end card foi parametrizado por peça e o título 16:9
não: as 8 peças em 16:9 saíram com a headline da peça 01 — inclusive as das Aulas
2 e 3. Só apareceu porque a conferência foi um contact sheet com as 8 lado a lado.
Conferindo uma peça só, teria ido pra nuvem.

Parente de uma regra da casa ("ao auditar depois, conferir o universo inteiro, não
uma amostra") — a novidade aqui é a geração em lote: **duas peças do lote com o
mesmo asset de texto é sinal de parâmetro esquecido**, e isso dá pra checar por
hash, não por olho.

## §8. Mais armadilhas medidas (11/2026) — *VARIAÇÃO ISOLADA; versões medidas: HyperFrames 0.9.x, ffmpeg 9*

**Cor**
1. **O ffmpeg converte pela matriz errada (bt601) quando você não declara.** Na ida pra RGB, `scale=...:in_color_matrix=bt709:in_range=tv` antes do `format=rgb24`; na volta de PNG/RGB pra YUV, `out_color_matrix=bt709`. Sem isso o tom desvia (no remendo medido, o PSNR foi de 23 pra 44 dB depois de declarar).
2. **`<video>` H.264 dentro do render do HyperFrames sai ~1,75 nível de luma abaixo do master.** Pra emenda master → placa ficar igual, use essa janela como MOV com PNG (sem perda, bt709 explícito; ~240 MB por 6 s). O `hyperframes check` não enxerga esse MOV e acusa `canvas_covered` falso: rode o check com uma cópia H.264 e renderize com o MOV.
3. **`fade=...:color=` passa por RGB e desvia a luma do clipe inteiro.** Faça o fade em YUV com `geq` + `enable` só nos últimos quadros (no `geq` o número do quadro é `N`; no `enable`, `n`).
4. **Gradiente radial com elipse maior que a caixa vira linha reta no fundo** (1-2 níveis, só aparece com a luma esticada). Raio ≤ distância do centro à borda.

**Emenda, áudio e quadros**
5. **`alimiter` atrasa o áudio pelo tempo de ataque** (~5 ms medidos). Use `latency=1` ou apare as amostras iniciais.
6. **Emendar sem recodificar: o concat demuxer converte H.264 pra Annex B por padrão.** Use `-auto_convert 0`; pra igualar ao original, declare `-pix_fmt yuv420p`, as etiquetas bt709/tv e `setsar=1`.
7. **AAC não se copia no meio de um fluxo:** o priming (~1024 amostras) vira ~21 ms de atraso e um estalo. Decodifique tudo pra PCM e codifique uma vez só. Prova de "áudio igual" é no PCM do mix, nunca nos bytes do mp4 (WAV float leva carimbo de hora: compare amostras, não `cmp`).
8. **`select`+`trim`+`concat` descarta segmentos de 1 quadro sem erro.** Pra reordenar quadros, trabalhe com quadros crus e codifique uma vez. Sempre confira a contagem de quadros esperada contra a de saída.
9. **Imagem com `-loop 1` sem `-t` num grafo com `overlay`+`concat` travou o ffmpeg em 0% de CPU.** Dê sempre um `-t`.
10. **Baixar trecho de vídeo de plataforma:** em formato HLS, `-ss` de entrada perde de 1 a 5 s sem erro (só a contagem de quadros denuncia). Use pré-rolagem de ~12 s, `-ss` de saída e `fps` fixo. Com `-c copy` cada formato começa no próprio keyframe: compare qualidade no mesmo instante.
11. **ffmpeg 9:** não aceita `-vsync` (use `-fps_mode passthrough`) e não adivinha formato por extensão estranha (`x.wav.novo`: use `-f wav`). **zsh:** `${VAR:A}` resolve o link do venv até o Python sem pacotes (use `:a`); `inputs=$N:layout` aplica o modificador `:l` (escreva `${N}`).

**HyperFrames, CSS e GSAP (a prévia passa, o mp4 não)**
12. **`background-clip: text` no pai some no render quando os filhos animam.** Degradê só em elemento cujo texto é dele e sem filho animado; brilho na letra vai por um retângulo com degradê dentro do SVG, com `clipPath`. Fonte condensada de linha baixa dá `text_box_overflow` sem nada cortado: `data-layout-allow-overflow`.
13. **`mask-image` recorta tudo o que sai da caixa do elemento** (o `mask-clip` padrão é a caixa de borda): símbolo de fundo aparece cortado em linha reta no meio do quadro. Símbolo de marca aparece inteiro, ou só a borda da tela corta. Nenhum portão numérico pega isso: olhe a folha de contato no tamanho de celular.
14. **Pegadinhas que só a prévia 1:1 pega:** `filter: blur()` no mesmo tween de um `back.out` (a ultrapassagem dá blur negativo e o quadro congela no valor anterior); pulso de escala ≥1,06 numa palavra do meio da linha come os espaços (máximo ~1,03); `inline-block` cria ponto de quebra (prenda aspas e vírgula com `white-space: nowrap`); `z-index` vence a ordem do DOM; classe com o mesmo nome de um modificador de outro componente pinta o elemento errado; variável CSS do original não chega num clone anexado em outro pai; tween com `duration: DUR - x` muda de velocidade quando o fim cresce; `tl.set` em 0 não pinta no `seek(0)` (use `gsap.set` no build).
15. **Falsos positivos do `hyperframes check`**, e o check roda na composição FINAL de cada peça, não só na primeira: `text_occluded` em células escondidas de um rolo (`data-layout-allow-occlusion`); contraste baixo em legenda branca com borda escura (o check ignora a borda: confirme no quadro); `line_unread` pede 2 s legíveis pra linha que fica até o fim.
16. **O `snapshot` do HyperFrames:** as 2 primeiras capturas de cada rodada saem no estado inicial. Não julgue transição por elas. Número que rola (contador) passa por valores errados no meio do rolo, justo quando a fala diz outro: confira o quadro do meio.

**Transcrição e alinhamento**
17. **Transcreva por ilha de fala** (corte nos silêncios ≥0,45 s, uma transcrição por ilha), não o arquivo inteiro, que junta retomadas numa frase só. O Whisper turbo pode pular uma frase inteira (compare com a legenda automática da plataforma ou rode large-v3 só nas janelas de fala) e alucina fala em silêncio e em música ("E aí", "Amém"): meça o nível do mix antes de ler como fala. Palavra ambígua: alinhamento forçado das duas frases candidatas no mesmo trecho; a maior verossimilhança ganha.
18. **O alinhamento forçado (MMS) erra em casos previsíveis:** algarismo e sigla (troque pela pronúncia só no alinhamento; a legenda mantém a grafia); duas letras iguais seguidas ("o o", "a ação"); fala baixa ou depois de trecho mudo (sinal: trecho que se sobrepõe ao vizinho ou folga de 0,00-0,04 s; conserte com janela, `word_timestamps` e perfil de energia). O fim surdo de palavra fica abaixo do limiar de silêncio: a pausa nunca começa antes do fim alinhado + 40 ms.

## §8.1 Mais armadilhas medidas (fim de 11/2026) — *VARIAÇÃO ISOLADA; versões medidas: HyperFrames 0.9.x, ffmpeg 9*

**Render e arquivos**
19. **Render lançado com `nohup … &` de dentro do shell do Claude morre em 1-2 s** (`render_cancelled_parent_exited`): o
    HyperFrames fotografa no começo a cadeia inteira de processos acima dele e cancela se qualquer um morrer, e o shell da
    chamada morre quando ela volta. Fila de render vai como tarefa em segundo plano da própria ferramenta (o shell fica vivo
    até acabar) ou com `HYPERFRAMES_RENDER_DETACHED=1`.
20. **Mídia criada por JavaScript depois do carregamento não entra no render como clipe:** o compilador só marca o
    `video[src]` que está no HTML. Ponha o elemento no HTML estático.
21. **Prévia ou capa dentro da pasta da composição** faz o `hyperframes check` dar `multiple_root_compositions`: vão numa pasta
    irmã, com link pros `assets/`. O relatório do check tem nome aleatório (`.hyperframes/artifacts/checks/<uuid>.json`):
    ache pela data. E rode o check mesmo com os seus portões passando: ele pega o que eles não pegam.
22. **PNG de quadro 100% opaco sai RGB (3 canais) no render em `png-sequence`:** colagem e conferência de alfa tratam 3
    canais como opaco.
23. **Duração arredondada que passa do quadro** (`round(dur, 3)` de 1481/30 vira 49,367) faz o render sair com 1 quadro a
    mais, e o módulo seguinte entra 33 ms atrasado contra o som. Corte cada parte em `round(dur × fps)` quadros.
24. **Deslocamento de áudio em número inteiro de amostras** (a 48 kHz, -11,7 ms = 561,6 amostras saiu 1 amostra curta).
25. **`ffmpeg -y` em cima de hardlink reescreve os dois arquivos.** A v2 nunca grava no caminho da v1; pra copiar uma pasta
    de trabalho, clone (`cp -c` no APFS), não hardlink. No ffmpeg 9, as etiquetas de cor só saem com `setparams` no fim da
    cadeia; o `ffprobe` 9 põe vírgula no fim do csv (`"1190,"`: corte antes do `int()`).
26. **Portão que imprime FAIL e sai com código 0 não barra nada.** Portão novo só vale se o lote confere o código de saída.
    Portão por amostragem também não vê sobreposição curta (um bloco de legenda esticado pro mínimo cobria o seguinte por
    0,06 s): confira o intervalo inteiro.
27. **puppeteer:** `waitForFunction` que devolve o objeto da timeline do GSAP não resolve; com `!!(...)` resolve.

**Layout, legenda e animação**
28. **Elemento fora da página mede 0** e a função que encolhe pra caber não encolhe: meça depois de `appendChild`, com teto
    abaixo do limite (a ultrapassagem do `back.out` passa de 1).
29. **Escala de entrada ou pulso num elemento quase da largura da zona** passa da margem: encolha (0,96), nunca cresça, e
    pulse a parte de dentro.
30. **Seta num `<path>` só com curva e ponta** aparece com a ponta inteira antes de a curva chegar nela: curva e ponta em
    dois paths, a ponta desenhada quando a curva termina. Seta que sai do lado da palavra, na altura da linha, lê como
    parêntese: saia de cima.
31. **Texto escondido só pela máscara de escrita** ainda é medido pelo `check` (acusa sobreposição): `autoAlpha` 0 até a
    escrita começar.
32. **FLIP de palavra entre corpos diferentes** escala pela razão dos corpos, não das caixas (o `line-height` diferente dá
    4% a mais).
33. **Legenda palavra por palavra:** os spans vão colados no HTML (`"".join`) e o vão é só a margem
    (`.w + .w { margin-left: 0.25em }`). Espaço de texto mais margem dobra o vão, e a mesma frase sai com dois espaçamentos
    quando quebra. Nenhum portão mede isso: olhe o quadro.
34. **O quadro 0 é a capa quando o publicador não escolhe capa:** olhos abertos e a legenda do 1º bloco na tela.
35. **Hífen longo em algumas fontes pesadas** (meia-risca no lugar de hífen, também nos U+2010/2011): nas formas
    pronominais ("pegá-la") ele vai num `inline-block` com `scaleX(0.6)` e margem negativa.
36. **OCR do macOS (Vision) devolve letra cirílica igual à latina** ("Voсê") e erra letra dourada com borda numa escala e
    acerta noutra: normalize homóglifos e faça 2ª leitura em 1,5x e 2x, colorido e cinza invertido, só nos segundos que
    faltaram. Busca de termo proibido é por palavra inteira (substring acha "bio" dentro de "advérbio").

**Imagem e cor**
37. **Tone-map de HLG pra SDR (`npl=203` + hable) em parede clara com luz de janela** deixou a pele quase da cor da parede:
    alvo de pele pela curva de meio-tom, com teto de luma. Tela de computador filmada pede `npl=100` (com 203 o papel fica
    cinza).
38. **Moiré de monitor filmado:** desfoque gaussiano de ~1,3 px no 4K antes de reenquadrar tira a grade sem mexer na letra, e
    um realce leve na saída devolve o traço. Clarear o papel com curva comum estica o moiré. A trama pesa no arquivo: suba
    o CRF.
39. **Nome de aluno em tela gravada** (aba do PDF, barra de título da janela): rode OCR em todos os quadros e apague antes de
    entregar. Escapa fácil na conferência a olho.

**Som e transcrição**
40. **Tom de sala só de silêncio de verdade.** Pegar "o trecho mais quieto de 0,8 s" numa gravação sem pausa desse tamanho
    pôs fala dentro do tom, e no fecho ficou "uma palavra sendo repetida no fundo". Régua: RMS de 10 ms; silêncio abaixo do
    piso (p5) + 8 dB, com 80 ms de folga de qualquer bloco mais alto; trechos de 0,15 s ou mais; o mais longo em laço com
    fusão de potência constante. Reprove se um bloco do tom passar do piso + 10 dB. Estalo de boca no tom vira tique em laço
    (o whisper lê como "E aí"): máximo ≤ -55 dB.
41. **Fim cortado que a legenda esconde:** o corte pode acabar no meio da última palavra e a legenda ainda mostrá-la. Rode o
    whisper nos últimos 4 s da voz com 1,5 s de silêncio depois e compare com as últimas palavras da legenda.
42. **Corte antes de oclusiva** (terminar no fecho do /p/) deixa a vogal anterior colorida e a palavra soa errada: termine no
    meio da vogal final, com fade de ~45 ms.
43. **Cruzamento com fonte muito limpa abre buraco:** a cauda depois da última palavra a -75/-88 dBFS soa como silêncio
    digital. Leve o ruído de sala das pausas por baixo, no mesmo nível.
44. **Efeito sonoro com cauda come a 1ª consoante da fala** que entra junto: confira o efeito contra a sílaba.
45. **O whisper do arquivo inteiro junta duas tomadas iguais numa frase, engole palavra repetida ("Não, não") e some com o
    pronome que retoma o sujeito** ("público, ele acaba"). Em gravação com diretor dizendo "volta", rode o large-v3 por cima
    antes do corte e confira cada "volta" no perfil de energia. A legenda automática do YouTube marca o começo da linha, não
    da palavra: "pausa de 3 s" lida nela pode não existir.

**Fonte, Drive e referência**
46. **Reel sem bruto: a fonte limpa é a live, achada pelo som.** Janelas de 4 s do reel procuradas no áudio de cada live
    (mel em 40 faixas, correlação por faixa): a live certa casa em todas as janelas e as erradas ficam bem abaixo; a sequência
    dos achados é a lista de cortes do editor. Áudio leve do YouTube: formato 139 do `yt-dlp`.
47. **Trecho direto do Drive, sem baixar o bruto inteiro:** o ffmpeg lê o arquivo pela API com o token no cabeçalho, pedido
    por pedaço, e o áudio saiu idêntico (md5) ao do arquivo baixado. Baixar inteiro, quando precisar: várias conexões com
    Range dobram a velocidade.
48. **Música da biblioteca do Instagram não entra no vídeo:** ele vai pronto, sem a faixa, e quem posta escolhe a música no
    app, com a orientação de qual é.

**Vídeo inteiro de IA a partir de um reel de referência** (1 peça, VARIAÇÃO ISOLADA)
49. **A análise da referência descreve a mecânica, não só o visual:** o que cada pessoa faz, passo a passo. A v1 anotou
    cenário, rótulos e câmera, perdeu a ação e saiu "nada a ver". Nada por cima da referência (relógio, balão, falas
    escritas) que ela não tem.
50. **"Cara de IA" se mede:** tamanho do rosto na tela, para onde ele olha e o brilho do quadro, contra a referência. Rosto
    grande posando pra câmera e luz dramática denunciam; o que entrou no prompt foi plano aberto, olho na tarefa e nunca na
    câmera, rosto calmo. Quadro em números medidos na referência, não "mais perto" ou "mais longe".
51. **Gerador de vídeo por trechos encadeados** (medido no Seedance): escurece o 1º quadro ~5% em relação à imagem de
    partida, aperta o quadro ~1% na horizontal e aumenta o ruído de parede lisa a cada trecho regerado; a imagem de
    partida não garante o 1º quadro; e a IA não guarda a geometria de uma imagem-chave pra outra (meça o cenário em cada
    uma). O modelo se escolhe gerando o mesmo trecho nos candidatos e medindo.
52. **Cruzamento entre dois trechos que partem do mesmo quadro dobra a pessoa** (cabeça e corpo duplos em 6 quadros): use
    cruzamento de 2 quadros ou o quadro que sai parado. Contraste de rótulo se mede no vídeo, não na imagem parada (cai de
    3,2:1 pra 2,6:1).
