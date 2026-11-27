# Framework — Edição técnica de criativo em vídeo (corpo + CTA)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> 📐 **Antes deste arquivo, ler `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`** — ele decide *o quê*
> e *por quê* (bloco, ritmo, emoção, camadas de áudio); este aqui é o *como*.

> **Camada:** mista — armadilha de ferramenta (UNIVERSAL) + padrão visual do
> cliente (não transfere)
> **Base:** 1 cliente (o caso-base, um expert de educação) · 1 lançamento · 1 execução completa
> **Alcance:** as **armadilhas técnicas do §9.2** são UNIVERSAIS — são
> comportamento de `ffmpeg`/`libass`/`loudnorm` e do arquivo do iPhone, não têm
> dimensão de cliente. Custaram rodada aqui e vão custar em qualquer projeto.
> Todo o resto (correções do Rodrigo, padrão "nativo de Instagram", convenções
> de pasta) é NÃO TESTADO FORA. Ver §11.

> **Ferramentas:** ffmpeg (com libass) e Python (PIL, numpy, scipy, moviepy) —
> ferramentas externas, instalam à parte. Quem edita no CapCut ou com editor humano
> usa este arquivo pelo porquê de cada decisão e como checklist do que conferir no
> arquivo exportado. O passo a passo com os números está em
> `sirius-scale/frameworks/copy/edicao-video-receita.md`.

Reverse-engineered da primeira edição completa feita pelo Claude Code no caso de
origem: um criativo de captação (corpo com o gancho "últimos 30 dias antes da
prova" + CTA 1) de um lançamento do caso-base. Documento vivo — cada linha marcada
como **VARIAÇÃO ISOLADA** (1 execução, 1 cliente) até repetir em outro
lançamento/cliente e virar CONSISTENTE.

## Contexto de origem

O expert do caso-base grava os 10 roteiros do corpo e os CTAs em arquivos
separados (iPhone, `.MOV`, nome genérico tipo `IMG_1234.MOV` — sem indicação de
qual roteiro é qual). O texto completo dos roteiros e o raciocínio dos ângulos
ficam no caso de origem (o doc de copy dos criativos e o plano de criativos do
lançamento).

## 1. Identificar qual bruto é qual roteiro — *VARIAÇÃO ISOLADA*

Sem transcrição disponível (MacWhisper CLI travou por causa da quarentena
do macOS em app baixado fora da App Store — matar o processo e tentar de
novo não resolveu, e remover quarentena em massa foi bloqueado pelo
classificador de segurança do Claude Code, corretamente). Alternativa que
funcionou: cruzar a **duração real** de cada bruto (`ffprobe`/`ffmpeg -i`)
com a **contagem de palavras** de cada roteiro no doc de copy, calibrando
o ritmo de fala (palavras/segundo) pelo par de maior confiança (roteiro
mais longo × bruto mais longo). Com o ritmo calibrado (~1,95-1,96
palavras/seg nesta gravação), todos os outros pares bateram dentro de
±2s — inclusive os 4 CTAs (CTA1, CTA1-B, CTA2, CTA3), que têm contagem de
palavras bem distinta entre si. Confirmação final por frame extraído
(tone-map aplicado) pra checar visualmente que é o expert falando pra
câmera, não b-roll/take descartado. Método rastreável e sem inventar
conteúdo — mas é heurística, não transcrição; sinalizar isso na entrega
quando a identificação não for 100% óbvia.

⚠️ Depois, no mesmo caso, a heurística foi reconfirmada por transcrição real, e a
regra passou a ser **transcrever os primeiros ~13s de cada clipe** em vez de
estimar (`sirius-scale/frameworks/copy/edicao-video-receita.md` §3.2).

## 2. HDR do iPhone precisa de tone-map antes de qualquer corte — *VARIAÇÃO ISOLADA*

iPhone recente grava em Dolby Vision (HDR10/BT.2020, perfil 8) por padrão.
Sem converter pra SDR/Rec.709 antes de cortar/exportar, a cor sai lavada
(cinza, sem contraste). Cadeia que funcionou no `ffmpeg`:

```
zscale=t=linear:npl=100,format=gbrpf32le,zscale=p=bt709,tonemap=hable:desat=0,zscale=t=bt709:m=bt709:r=tv
```

Aplicar **antes** do crop/scale, em todo clipe de iPhone gravado em HDR.

## 3. Corte de bruto de tomada única — *VARIAÇÃO ISOLADA*

Quando o expert grava limpo (sem erro no meio), o "corte necessário" é só
aparar o silêncio morto do início e do fim do arquivo — não há o que
cortar no corpo. Usar `silencedetect` (`noise=-30dB:d=0.8`) pra achar os
limites reais em vez de chutar por olho: nesta gravação, ~1.7-2.2s de
silêncio antes de o expert começar a falar e ~4s de silêncio depois da última
frase. Pausas naturais de até ~0,8s no meio da fala **não** são cortadas —
cortar toda pausa deixa a fala com cadência robótica.

## 4. Reenquadramento do bruto vertical do iPhone — *VARIAÇÃO ISOLADA*

Bruto vertical do iPhone (celular preso mais alto que a altura do rosto)
sai com excesso de teto vazio acima da cabeça. Como o expert se mantém
estável no enquadramento ao longo da tomada inteira (checado com frames em
4 pontos da timeline), um crop estático — sem tracking dinâmico — resolve:
cortar a faixa de cima até sobrar ~15-20% de margem sobre a cabeça, manter
a mesma proporção 9:16 no crop pra não distorcer, escalar pro tamanho
final. Verificar a estabilidade do enquadramento com frames de amostra
antes de cravar o crop — só funciona porque o expert não se move muito.

## 5. Headline nos primeiros 5s — *VARIAÇÃO ISOLADA*

Texto on-screen é a versão curta/gritada do gancho que o expert já fala (não
inventa claim novo) — aqui, a fala com [o prazo até o objetivo do público]
virou [o prazo / a pergunta sobre o objetivo] em duas linhas. Estilo: caixa alta,
fonte bold geométrica (usei `Arial Rounded Bold.ttf` do sistema como
aproximação de Poppins/Montserrat ExtraBold, que é o registrado na
identidade visual do lançamento), caixa navy semitransparente atrás
pra legibilidade sobre qualquer fundo, uma linha branca + uma linha cyan
(o par navy/cyan já documentado na identidade do lançamento). Some depois
de 5s, não fica cravado na tela o vídeo inteiro.

## 6. B-roll de abertura quando não há filmagem contextual — *VARIAÇÃO ISOLADA*

Pedido: b-roll/imagem na abertura. Não havia filmagem ou imagem real que
ilustrasse o tema do roteiro (prova, caderno, etc.) nem ferramenta de
geração de imagem plugada neste fluxo. Em vez de usar uma foto genérica do
expert fora de contexto ou inventar uma imagem, entrei com uma **cartela de
marca** (fundo navy + wordmark do evento + data), 100% dado real
(a identidade visual do lançamento), rotulada como isso mesmo (cartela, não
b-roll de verdade) — e avisei o cliente. Se o cliente tiver preferência por
b-roll de imagem real ou quiser imagem gerada por IA, ajustar aqui na próxima.

## 7. Trilha de fundo original sintetizada — *VARIAÇÃO ISOLADA*

Em vez de baixar uma faixa "royalty-free" de terceiro (risco de direito
autoral remanescente mesmo em bibliotecas "livres", e exigiria permissão
explícita pra baixar arquivo externo), compus uma trilha instrumental
simples direto em Python (progressão de acordes + pad + arpejo leve,
`numpy`/`scipy`, sem nenhuma amostra de terceiro). Zero risco de direito
autoral porque não existe fonte externa. Mixada bem baixo (peso 0,16 no
`amix`, medição final ~-28dB médio no trecho falado) pra não competir com
a voz. Não tem sidechain/ducking dinâmico nesta primeira versão — é
volume baixo constante, funciona mas fica menos "vivo" que ducking de
verdade; considerar `sidechaincompress` se o cliente notar falta de
respiro.

⚠️ **Superado depois (§9 e receita):** a trilha sintetizada foi rejeitada na v1
("música lenta, não combinou"), e o ducking foi testado e **reprovado** — a trilha
sobe nas respirações e fica oscilando. Regra que ficou: volume fixo e baixo, nunca
`sidechaincompress` (`sirius-scale/frameworks/copy/edicao-video-receita.md` §2, "Áudio").

## 9. Correção do Rodrigo na v1 — o que muda a partir daqui — *VARIAÇÃO ISOLADA*

Depois de ver a v1 (headline parafraseada, sem legenda, corte seco pro CTA,
música sintetizada lenta, sem logo/data/botão na tela), o Rodrigo pediu uma
v2 mais "nativa de rede social". O que mudou, todo com dado real, zero
invenção:

- **Headline é a mesma que está no doc de copy, verbatim** — no doc, o
  texto entre aspas depois do nome da peça (`### <peça> — "..."`) já funciona como
  headline (ver `sirius-scale/frameworks/copy/criativos.md` §0.1). Não parafrasear pra virar hook de
  tela; usar exatamente esse texto.
- **Antes de estilizar qualquer coisa "no escuro", pedir uma peça de
  referência já editada pelo editor de vídeo do cliente** e extrair o
  padrão real dela (fonte, posição da legenda, tipo de transição, cores) —
  economiza rodadas de chute. Nesta v2, a referência (um reel já editado pelo
  editor do expert, de um lançamento anterior) revelou: legenda em
  blocos curtos (2-4 palavras) sem caixa de fundo, só contorno/sombra pra
  legibilidade, com 1 palavra de destaque colorida por vez (tema = azul,
  negação = vermelho); cartela cheia navy+grade com a logo real entre o
  corpo e o CTA (não corte seco); fechamento reprisando a logo.
- **Legenda embutida sem transcrever** — se o expert leu de teleprompter, o
  texto falado já é 100% conhecido (o doc de copy). Não precisa Whisper
  nem nenhum reconhecimento de voz: estima o tempo de cada palavra
  proporcional ao nº de caracteres dela, calibrado pela duração real do
  corte (`ritmo = nº total de caracteres / duração do trecho`). Gera
  arquivo `.ass` (libass, `ffmpeg -vf subtitles=arquivo.ass`), que estiliza
  cor por palavra via tag `{\c&HBBGGRR&}` — muito mais leve e controlável
  que sobrepor N imagens com `overlay`. Só recorrer a transcrição de
  verdade quando o texto falado **não** for conhecido de antemão (ex.:
  fala solta, sem roteiro).
  ⚠️ **Superado depois:** a estimativa sem transcrever custou duas rodadas, e a
  receita passou a usar ASR só pelo tempo, com o texto da copy, mesmo quando há
  teleprompter — e o expert não lê o teleprompter ao pé da letra
  (`sirius-scale/frameworks/copy/edicao-video-receita.md` §3 e §3.1).
- **Ativo de marca de verdade > gerado do zero.** Baixar da nuvem uma peça
  real já produzida pelo designer pro mesmo lançamento (aqui, um criativo
  estático do mesmo lançamento) e recortar dali a
  logo, os chips de data/formato — em vez de redesenhar isso na mão. Ao
  colar o recorte num fundo próprio, aplicar borda com pena
  (`ImageFilter.GaussianBlur` na máscara alpha) pra não deixar costura
  visível entre o recorte e o fundo gerado.
- **Transição entre blocos = crossfade curto (~0,6s), nunca corte seco**,
  quando o pedido for "mais suave" — usar `xfade` (vídeo) +
  `acrossfade` (áudio) encadeados, não `concat`.
- **Botão de CTA na tela** — pra CTA pago (o toque no botão Saiba Mais), desenhar
  um botão pill cyan com o texto, imitando o botão nativo da plataforma,
  na cartela de fechamento. Não inventar imagem de botão — desenhar com
  retângulo arredondado (`ImageDraw.rounded_rectangle`) na cor de marca.
- **Trilha sintetizada foi rejeitada** ("música lenta, não combinou").
  Corrigido baixando uma faixa real de banco royalty-free (Pixabay Music,
  Pixabay Content License, sem exigência de atribuição) — o link de
  download real do Pixabay não aparece no HTML da página (é gerado por
  JS), mas o elemento `<audio>` da própria página expõe a URL direta em
  `cdn.pixabay.com` via `document.querySelector('audio').src`.

## 9.1 Correção da v2 — o padrão "nativo de Instagram" de verdade — *VARIAÇÃO ISOLADA*

O Rodrigo reprovou a v2 ("headline brega, parece feita por criança";
"legenda dessincronizada"; "música ruim e muito alta"; "falta toque de
editor profissional") e mandou peças de referência do Instagram (feitas
pela equipe do expert e por um perfil de referência de outro nicho). O que o
padrão real exige:

- **Headline = sticker nativo do IG:** caixa branca `#FFFFFF` de cantos
  arredondados (raio ~20px em 1080), texto **preto** bold centralizado,
  padding generoso, emoji inline no começo. Não é caixa navy com texto
  colorido (isso é peça de designer, não sticker de rede social). Nas
  referências, headlines do tipo "❌ [o jeito errado de fazer algo]",
  "😱 [o que aconteceu com ela depois de algo]", "Veja se você tem isso ⚠️".
- **Emoji colorido no macOS:** `Apple Color Emoji.ttc` só rasteriza em
  tamanhos específicos — 137px **falha** com "invalid pixel size", 96 e
  160 funcionam. Renderizar em 160 com `embedded_color=True`, recortar
  pelo bbox e reduzir pro tamanho desejado.
- **Legenda:** branco puro, **sem contorno preto** (`Outline: 0`), só
  sombra (`Shadow: 5` + `BackColour` preto semitransparente). O contorno
  grosso é o que dava cara amadora. Fonte geométrica bold (Poppins Bold),
  ~84px em 1080. Destaque **esparso**: no máximo 1 palavra colorida por
  bloco.
- **Sem cartela de tela cheia.** A da v2 era reciclagem de outro criativo
  ("gambiarra", palavras do Rodrigo). O certo: logo entra na tela **só no
  momento em que o expert fala o nome do evento**, e as demais infos (datas,
  horário, "gratuito", "SAIBA MAIS") ganham **destaque na legenda** no
  instante em que são ditas — não cartela.
- **Transição:** dip-to-black **rápido** (~0,25s de fade out + 0,25s de
  fade in), aplicado só no **vídeo**, com o áudio concatenado direto e
  contínuo. Nunca `acrossfade` (deixa buraco de áudio). Serve pra
  disfarçar a troca de cenário/roupa entre corpo e CTA.

## 9.2 Armadilhas técnicas que custaram rodada — *VARIAÇÃO ISOLADA*

> 📌 **As armadilhas de FERRAMENTA desta seção migraram para
> `sirius-scale/frameworks/copy/video-criacao-tecnica.md`** (decisão do Rodrigo):
> libass sem `fontsdir` (§3.1), `loudnorm` em 96/192 kHz (§2.5), overlay em
> `-loop 1` decodificado em todo frame (§1.3) e `crop` que não reavalia `w`/`h`
> (§1.4). Elas são fato de ferramenta, sem dimensão de cliente — e estavam num
> arquivo cujo cabeçalho diz "1 cliente, reverse-engineered da primeira peça", onde
> ninguém ia procurá-las ao montar vídeo de outro cliente.
> **O que fica aqui é o que é do caso-base:** o método de sincronia sem transcrever,
> os níveis medidos contra a referência do editor do expert, e o ativo de marca.

- **⚠️ libass cai em fonte substituta SEM avisar.** `-vf subtitles=x.ass`
  resolve o `Fontname` via fontconfig, ou seja, só acha fontes
  **instaladas no sistema**. Baixar o `.ttf` numa pasta não basta: a v2
  saiu inteira em Helvetica achando que era Poppins, sem nenhum erro no
  log. **Sempre passar `subtitles=x.ass:fontsdir=/caminho/das/fontes`** e
  **conferir ampliando um frame** (o "a" da Poppins é de um andar,
  geométrico; o do Helvetica é de dois). Nome no `Fontname` é o da
  **família** (`Poppins`), com `Bold: -1` pra escolher o peso — não
  "Poppins Bold".
- **Legenda sincronizada sem transcrever:** distribuir as palavras
  uniformemente pela duração **não funciona** (foi o erro da v2 — atrasa e
  adianta, porque ignora as pausas). O certo, com o texto já conhecido do
  teleprompter: rodar `silencedetect` (`noise=-33dB:d=0.18`) pra achar os
  trechos **com fala**, montar uma linha do tempo "só-fala" concatenando
  esses trechos, distribuir as palavras nela proporcional ao tamanho de
  cada palavra, e mapear de volta pro tempo real. Quebrar bloco em pausa
  ≥0,30s ou fim de frase. Na primeira peça isso deu 53 trechos de fala e
  alinhamento correto (1º bloco em 0,20s, batendo com o início real).
  *(O método que a receita adotou depois, ASR só pelo tempo, está em
  `sirius-scale/frameworks/copy/edicao-video-receita.md` §3.)*
- **`loudnorm` devolve áudio em 96/192 kHz.** Se não forçar, o MP4 final
  sai fora do padrão de 48 kHz que as plataformas esperam. Sempre fechar a
  cadeia com `aresample=48000` **e** `-ar 48000`.
- **Nível de áudio:** medir a referência do editor antes de mixar. A do
  cliente estava a **-16,8 dB** de média; a v1/v2 saíam a -27,8 dB (baixas
  demais, e por isso a música parecia alta). Cadeia que acertou:
  `loudnorm=I=-16:TP=-1.5:LRA=11` na voz → música em `volume=0.18` com
  `sidechaincompress` (threshold 0.015, ratio 12) usando a voz como
  sidechain, pra a trilha abaixar sozinha quando o expert fala → `volume=2dB` +
  `alimiter` no fim.
  ⚠️ **Depois:** o ducking foi reprovado (trilha oscilando na respiração), a música
  ficou em `volume=0.06` fixo, e o `alimiter` precisa de `level=disabled`
  (`sirius-scale/frameworks/copy/edicao-video-receita.md` §2 e
  `sirius-scale/frameworks/copy/video-criacao-tecnica.md` §2.1).
- **Ativo de marca: pedir o original antes de improvisar.** Eu vinha
  recortando a logo de um `.png` de peça pronta (fundo navy embutido,
  exigindo chroma-key e pena na borda). O Rodrigo mandou os PNGs oficiais
  com fundo transparente, em duas versões — **clara** (texto navy, pra
  fundo claro) e **escura** (texto branco, pra fundo escuro). Escolher a
  versão pelo fundo do vídeo: o expert grava contra parede clara, então
  entra a versão navy.

### 9.2.1 Duas armadilhas novas (num segundo negócio — custaram ~1h de render perdido) — *UNIVERSAL*

- **Overlay como `-loop 1 -i png` é decodificado em TODO frame, mesmo escondido pelo
  `enable`.** Passei 23 PNGs de 1080×1920 assim num criativo de 85s: o ffmpeg decodificava
  os 23 a cada frame (~49 mil decodes), e o render projetou **mais de uma hora** (18 MB em
  13 min). Correção: **pré-compor todos os overlays num único vídeo com alpha** (PIL frame a
  frame → `rawvideo rgba` no stdin do ffmpeg → `qtrle -pix_fmt argb`) e passar **um**
  overlay pro render final. Fades, linha crescendo e flash ficam no PIL, não no filtergraph.
  Mesmo resultado, minutos em vez de hora — e qualquer correção depois custa minutos de novo.
- **`crop` NÃO reavalia `w`/`h` por frame** — só `x`/`y`. Zoom via
  `crop=w='iw/(1+0.03*t)'` fica parado no primeiro valor, em silêncio. Pra animar escala por
  tempo: `scale=w='...t...':h=-2:eval=frame` seguido de `crop=1080:1920`, ou `zoompan`.
  Vale igual pra "linha crescendo" — não é `crop` com `t`, é `scale ... eval=frame` ou máscara
  no PIL.

## 9.3 Arquitetura de render: master limpo primeiro — *VARIAÇÃO ISOLADA*

Cada correção de texto estava custando ~12 min de CPU **da máquina do
Rodrigo**, porque todo render refazia o tone-map do 4K HDR. Separar em
dois passos resolve:

1. **Passo caro, uma vez:** 4K HDR → master 1080p limpo (tone-map + crop +
   corte), `crf 18`, **sem nenhum texto**. Guardar `master_<clipe>.mp4`.
2. **Passo barato, quantas vezes precisar:** aplicar legenda, headline e
   overlays em cima do master 1080p, juntar e tratar áudio. Roda em
   segundos.

Enquanto o estilo ainda estiver em validação com o cliente, **sempre**
montar assim. Só descartar os masters quando a peça for aprovada.

## 10. Onde fica bruto e entrega de vídeo — *VARIAÇÃO ISOLADA, mas já é convenção existente do cliente*

Confirmado no caso de origem: a estrutura de pastas do cliente na nuvem já
resolve isso, não é preciso inventar pasta nova. A pasta de criativos de vídeo
do lançamento tem, por fase, `1) BRUTO` (gravação crua) e `2) EDITADO/<formato>`
(`STORIES`, `FEED`, `YOUTUBE`, `REELS`) — usar exatamente essas subpastas, não
criar "ENTREGAS" ou equivalente. (A estrutura é a do cliente do caso-base; o que
transfere é usar a que o cliente já tem.) Fluxo de disco mínimo local: baixar da
nuvem só o(s) arquivo(s) bruto(s) necessário(s) pra uma pasta temporária da
sessão, processar, subir o resultado final pra `2) EDITADO/<formato>/`, apagar a
cópia local (bruto + intermediários) depois de confirmar o upload. Nunca
manter lote de bruto duplicado permanentemente em `Downloads` nem dentro
da pasta do projeto — o disco local é pequeno, a nuvem tem espaço de sobra.
A pasta `entregas/` segue valendo pra entregável leve (HTML, doc); pra vídeo, a
casa é a nuvem.

⚠️ **Este item chegou a conflitar com a regra de pastas do pipeline de vídeo do
caso de origem**, que punha bruto e trabalho dentro da pasta do projeto. Medido:
uma peça de 85s deixou 1,3 GB de intermediários ali. O Rodrigo resolveu depois, na
direção deste item: **bruto e final moram na nuvem, o computador só edita.** Baixa
pra editar; o bruto local sai assim que existe o master cortado; o intermediário
sai no fim de cada peça; o final aprovado sobe, confere que chegou (mesmo nome e
mesmo tamanho em bytes) e sai do local. Apagar continua pedindo confirmação, e é
definitivo (mandar pra lixeira não libera disco).

⚠️ **Num caso, ~800 MB de vídeos soltos de uma sessão anterior** pareciam
redundantes com a nuvem — o mesmo tipo de duplicação que este item existe pra
evitar. Não foram apagados sem confirmar com o Rodrigo primeiro: cópia que parece
redundante só sai conferida no destino e com o ok de quem é dono.

## 8. Ferramental (nenhum estava pronto no ambiente) — *VARIAÇÃO ISOLADA*

Máquina não tinha `ffmpeg`/Homebrew instalado. Caminho que funcionou sem
precisar de sudo/brew: `pip install moviepy imageio-ffmpeg` num venv —
`imageio-ffmpeg` traz um binário de `ffmpeg` estático pronto
(`imageio_ffmpeg.get_ffmpeg_exe()`). MacWhisper (app baixado, não veio do
sistema) tem CLI (`mw transcribe`) mas trava por causa de app translocation
de quarentena do Gatekeeper — não vale a pena insistir nele sem o app
primeiro ser movido/aberto manualmente pelo usuário.

---

## 9.4 Conferência e áudio: o que a transcrição não mostra (11/2026) — *VARIAÇÃO ISOLADA*

**Áudio**
1. **Trilha ou whoosh podem engolir sílaba fraca.** Rode o mesmo Whisper na voz sozinha e no mix: palavra que a voz tem e
   o mix não está mascarada. Remédio: trilha ≥24 dB abaixo da fala (mínimo 18), compressor leve na voz antes do
   `loudnorm`, EQ no efeito sonoro.
2. **Música do cartão final se mede contra o FIM do corpo**, na faixa que o celular toca (300 Hz-4 kHz), não contra a
   média. Música que entra 0,10 s antes evita buraco de silêncio.
3. **Gravação de celular com ruído alto:** o limiar de silêncio "fala − 27 dB" não acha pausa. Use
   `max(fala − 27, ruído p10 + 7)`.

**Imagem e OCR**
4. **Só os quadros mostram:** legenda ou selo queimado antigo que muda antes da fala (confira os quadros em volta do
   corte) e imagem da frase anterior colada na abertura.
5. **OCR (Vision no macOS) a 1 quadro por segundo**, amostrando por número de quadro (`select=eq(mod(n,30),15)`), não por
   `-ss` + `fps=1`, que lê o bloco seguinte. Ele erra letra e muda com a escala: "letra por letra" se prova em camadas
   (texto da copy = arquivo de parâmetros = composição renderizada, e OCR em várias escalas com pelo menos uma leitura
   exata). Em letra cursiva, serve só pra achar texto que sobrou.

**Correção de peça já entregue: provar que só X mudou**
6. Confira primeiro que o master e a composição no disco são os da versão entregue (hora dos arquivos; master contra o
   final onde nenhuma camada cobre).
7. Render de outra sessão não devolve o mesmo md5: a prova de "começo igual" é render × render na mesma sessão, refazendo
   junto o controle da versão anterior. Compare bloco a bloco (60×60) contra o ruído do próprio codec, e o PCM do mix.
8. Pra corrigir um elemento sem regenerar a composição, troca exata de texto, cada trecho achado exatamente 1 vez; senão,
   aborte.
9. Ao copiar os scripts de uma peça irmã (ou retomar uma rodada que morreu), procure o identificador da irmã nos
   arquivos copiados antes do render: rodar como estava renderizaria a OUTRA peça.

## 11. O que transfere e o que é do caso

**Transfere inteiro — é comportamento de ferramenta, não do cliente (§9.2):**

- **`libass` cai em fonte substituta SEM avisar.** Passar sempre
  `subtitles=x.ass:fontsdir=...` e conferir ampliando um frame. Nome no
  `Fontname` é o da **família**, com `Bold: -1` pro peso. Esta é a armadilha
  mais cara do arquivo: a peça sai inteira na fonte errada, sem erro no log.
- **`loudnorm` devolve 96/192 kHz.** Fechar a cadeia com `aresample=48000` **e**
  `-ar 48000`, ou o MP4 sai fora do padrão das plataformas.
- **Legenda não sincroniza distribuindo palavra uniformemente.** O método com
  `silencedetect` → linha do tempo "só-fala" → mapear de volta é o que funciona,
  e funciona com qualquer voz.
- **HDR do iPhone precisa de tone-map antes de qualquer corte** (§2), e o
  reenquadramento do vertical do iPhone (§4).
- **§9.3, master limpo primeiro** — economiza render em qualquer projeto.
- **Ferramental** (§8): `imageio-ffmpeg` traz binário estático; MacWhisper CLI
  trava por app translocation do Gatekeeper.
- **O princípio de "pedir o ativo original antes de improvisar"** — recortar
  logo de peça pronta gera chroma-key desnecessário. Vale pra qualquer marca.

**Não transfere — é o padrão desta marca e deste cliente:**

- Os **níveis de áudio calibrados** (-16,8 dB da referência, `loudnorm=I=-16`,
  música a 0.18, sidechain 0.015/12). Isso é a assinatura sonora do editor do
  expert do caso-base. O que transfere é o método: **medir a referência do editor
  antes de mixar**, e a ordem da cadeia (voz normalizada → música → limiter; o
  sidechain caiu depois, ver §9.2).
- **§9 e §9.1** — as correções do Rodrigo e o padrão "nativo de Instagram" como
  ele o definiu. São a régua estética deste cliente.
- Os PNGs de logo (clara/escura), a escolha da versão navy porque o expert grava
  contra parede clara, e o §10 (convenção de pastas do cliente).
- Os roteiros, a peça de origem, e o fato de o expert gravar em `.MOV` com nome
  genérico.

⚠️ **A distinção que importa neste arquivo:** quase tudo está marcado
VARIAÇÃO ISOLADA, mas por motivos diferentes. As armadilhas do §9.2 são ISOLADA
só porque **foram encontradas uma vez** — não porque dependam do cliente
(`libass` vai trocar a fonte em silêncio pra qualquer um). Já as correções do
§9/§9.1 são ISOLADA **e** dependentes do cliente. Ao levar pra outro projeto:
leve as armadilhas com confiança, e refaça a estética do zero.
