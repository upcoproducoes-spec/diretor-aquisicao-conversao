# Framework — Mapa de Edição de VSL

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** direção de pós-produção — a ponte entre a copy e a edição
> **Base:** o documento "INSTRUÇÃO DE SISTEMA — Gerador de Mapa de Edição para
> VSL" v1.0, escrito pelo Rodrigo pra briefar editor humano (está inteiro em
> `sirius-scale/frameworks/copy/prompts-sistema/gerador-mapa-edicao-vsl.md`), confrontado com
> `sirius-scale/frameworks/copy/edicao-video-receita.md`, com as regras do video-use (ferramenta externa de
> corte de vídeo por transcrição) e com um método externo de edição automatizada por
> IA, estudado a partir de um vídeo público do criador (não faz parte deste kit).
> **Alcance:** NÃO TESTADO FORA. Nenhuma **VSL longa** passou por este mapa
> ainda; um **criativo curto** passou inteiro (um criativo vertical de 85s de um
> segundo negócio) e é de onde vêm as seções §2.1, §4.1 e §4.3.
> **Confiança:** PADRÃO INCONCLUSIVO no geral. As linhas marcadas ✅ são
> **confirmação cruzada** — duas ou três fontes independentes caindo no mesmo
> lugar — e por isso são as mais seguras do arquivo.
> **Fusão:** este arquivo absorveu um documento irmão de direção de edição, que
> tinha nascido do mesmo documento numa outra ponta da mesma sessão. O que veio
> de lá: a nota de que "corte" é mudança visual (§2), a **primeira medição real
> em criativo curto** (§2.1), o contraste emocional por bloco (§2.2), a medição
> de áudio (§3) e as regras de faixa de texto e marca em transição (§4.1, §4.2).
> **Ferramentas citadas:** video-use (corte por transcrição, gera um EDL em
> `edl.json`), HyperFrames (animação em HTML/GSAP, com o comando `check`) e
> ElevenLabs Scribe (transcrição com tempo por palavra) — externas, instalam à
> parte. A skill `/mapa-edicao` deste kit carrega este arquivo junto com os dois
> prompts de sistema.

## 0. Duas direções, nunca misturar

O documento original vai **copy → mapa** (antes de gravar). O pipeline de edição
por IA da casa vai **bruto → transcrição → corte → mapa ancorado** (depois de
gravar). São usos diferentes do mesmo artefato:

| Quando | O que o mapa é | Tempo vem de |
|---|---|---|
| Antes da gravação | briefing: quantos blocos, o que mostrar, quanto dura | estimativa por contagem de palavras (140–160 ppm) |
| Depois da gravação | **o passo de outline do pipeline de edição** (transcrição → corte → mapa → animação → som → b-roll, uma porta de aprovação por etapa) | **timestamp real do Scribe** |

⚠️ Depois de gravado, a estimativa por palavra **morre**. Vale o número medido
(receita §3.8: *medir o que foi renderizado, não calcular*). Um mapa
pré-gravação que sobreviva com os tempos estimados é fonte de erro.

## 0.1 Gravação única pra múltiplos mercados (PADRÃO INCONCLUSIVO)

> **Alcance:** NÃO TESTADO FORA — decidido e escrito num cliente de perpétuo que
> vende em mais de um mercado, zero conversão real ainda. É decisão de arquitetura de
> roteiro, não resultado medido.

Quando o mesmo funil vende em mais de um mercado com **oferta real diferente**
(produto físico num, digital noutro; moeda, parcelamento, frete diferentes), a
saída que evita gravar o vídeo inteiro de novo por mercado é separar o roteiro
em duas camadas:

- **CORPO — gravado uma vez, serve a todos os mercados.** Regra dura: **zero**
  menção a preço, moeda, forma de entrega ou "chega na sua casa" em qualquer
  linha do corpo. E **neutro de gênero**, se o público variar de composição
  entre mercados (medido: no mercado principal, 65% das compras eram de mulheres; o
  segundo mercado tinha outro público, e lá 82% eram de homens, mesmo produto).
- **BLOCO DE PREÇO E ENTREGA — gravado separado, um por mercado.** Entra num
  ponto marcado no meio do vídeo (`>>> AQUI ENTRA O BLOCO DE PREÇO <<<`), com
  o preço, a moeda, o parcelamento e o que de fato chega pra aquele comprador.

**Por que isso não é luxo, é a causa de um problema real:** no mesmo cliente, um
anúncio pro segundo mercado prometia que o produto chegava na casa da pessoa, e ali
ele é 100% digital — cópia da versão do primeiro mercado sem reconferir a oferta
do mercado de destino (ver `sirius-scale/frameworks/copy/criativos.md` §4). Separar
preço/entrega do corpo é a prevenção estrutural pro mesmo erro não se repetir na VSL.

**O que ainda não se sabe:** se a técnica prejudica a conversão por perder
especificidade de mercado no corpo (a peça fica genérica de propósito). Só
testar depois de rodar.

## 1. A taxonomia de blocos — a peça que faltava no pipeline

HK hook · PB problema/dor · AG agitação · HS história · MC mecanismo ·
PS prova social · RV revelação do produto · OF oferta · BN bônus ·
PR preço/ancoragem · GT garantia · UR urgência · CT CTA ·
OB quebra de objeção · TR transição · RC recapitulação.
Bloco repetido numera: PS-1, PS-2.

**Por que isso importa aqui e não é só nomenclatura:** o EDL do video-use já
tem os campos exatos pra receber isso. Encaixe direto, sem inventar formato:

| Campo do `edl.json` | O que recebe do mapa |
|---|---|
| `beat` | o código do bloco (`HK`, `PB`, `PS-2`…) |
| `quote` | o trecho literal da copy daquele bloco |
| `reason` | o objetivo do bloco **+** por que este take e não outro |

Com isso o corte deixa de ser "tirei 1min24 de ar morto" e vira "o HK ficou em
12s, a AG perdeu 40s de repetição" — que é a conversa que dá pra ter com o
cliente.

## 2. Densidade: quanto propor por bloco

O método externo de edição por IA citado no cabeçalho propõe de mais de propósito
e o humano poda. Isso funciona, mas é caro. A tabela de velocidade de corte dá
**alvo em vez de poda**:

| Bloco | Tempo entre mudanças visuais |
|---|---|
| Hook | 2–4s |
| Problema | 4–8s |
| Agitação | 3–5s |
| História | 6–12s |
| Mecanismo | 5–8s |
| Prova social | 4–6s |
| Oferta | 3–6s |
| Bônus | 2–4s |
| Garantia | 6–10s |
| CTA | 5–8s |

Mais a **regra dos 30 segundos**: nenhum trecho passa de 30s sem mudança
visual significativa. Numa VSL de 20 min isso é o piso de ~40 eventos visuais —
número que dimensiona o trabalho antes de começar.

⚠️ **"Corte" aqui é mudança visual** (troca de plano, b-roll, card), não jump
cut de remoção de pausa no mesmo enquadramento. Num expert em plano único, o
que cria a mudança é **texto em tela, push-in, b-roll** — o jump cut o
espectador nem registra como corte.

**Contraponto honesto:** essas faixas não foram medidas na nossa base. São o
alvo inicial, não regra. A primeira VSL editada aqui vira o teste.
O primeiro **criativo curto** já foi medido — é o §2.1.

### 2.1 Primeira medição real, num criativo curto — *VARIAÇÃO ISOLADA (um criativo de 85s de um segundo negócio)*

Peça de 85s, expert em plano único + insert de depoimento, medida contra a
tabela acima:

| Bloco | Medido | Alvo VSL | |
|---|---|---|---|
| Hook | 1,73s | 2–4s | rápido |
| Problema/Mecanismo | 2,52s | 4–8s | **muito rápido** |
| Prova (insert de depoimento) | 15,48s | 4–6s | **muito lento** |
| Fechamento | 1,61s | 5–8s | rápido |

O que isso ensinou:

1. **Cortar pausa por limiar único achata o ritmo.** Um limiar de pausa fixo pra
   peça inteira dá a mesma respiração a hook, mecanismo e fechamento. A
   correção é limiar **por bloco** — limiar maior funde mais blocos de fala,
   clipe mais longo, ritmo mais lento. Valores que ficaram:
   **hook 0,42s · corpo 0,62s · fechamento 0,75s** (contra 0,35s uniforme).
2. **Insert de depoimento é o ponto cego.** 19s de rosto parado: não dá pra
   cortar a fala de um cliente sem picotar o depoimento, e a tabela pede 4–6s.
   Saída: **mudança visual sem corte** — push-in lento (`zoompan` de 1,00 a
   1,07 ao longo do trecho) e número em tela entrando na hora em que a pessoa
   fala o número.
3. **Peça curta comprime tudo.** Em 80s não cabe hook de 4s + problema de 8s.
   A tabela vale como *proporção entre blocos*, não como valor absoluto.

### 2.2 Contraste emocional por bloco — a monotonia é o que mata retenção

| Bloco | Emoção | Como editar |
|---|---|---|
| Problema | Tensão | Trilha grave, cor fria, ritmo lento, close |
| Agitação | Frustração | Corte rápido, impacto sonoro, texto vermelho |
| Solução | Alívio | Trilha positiva, cor quente, plano aberto |
| Prova | Confiança | Depoimento, screenshot, número destacado |
| Oferta | Excitação | Stack animado, trilha crescente |
| Urgência | Pressão | Timer visual, trilha acelerada |
| CTA | Clareza | **Tela limpa, foco total, zero distração** |

Depois de bloco tenso, orientar alívio. Depois de calmo, acelerar. E **cada
corte tem um porquê** — redirecionar atenção, quebrar monotonia, enfatizar,
contrastar, facilitar compreensão. Nunca por estética.

## 3. Camadas de áudio — o que bate com o aprovado e o que não bate

O documento original dá: voz −6 a −3 dB, trilha −18 a −24 dB, SFX −12 a −18 dB,
ambiente −30 dB.

⚠️ **Não são a mesma unidade que a receita usa.** A receita mede em LUFS
integrado (`loudnorm=I=-16`), que é média percebida; −6/−3 dB é nível de
fader/pico. Comparar os dois números direto dá erro.

O que transfere é a **hierarquia e a distância entre camadas**, não o valor
absoluto:

- Voz sempre dominante — mantém a corrente medida da receita
  (`loudnorm I=-16:TP=-1.5:LRA=11` → `volume=2dB` → `alimiter=limit=0.97:level=disabled` ⚠️ **`level=disabled` não é opcional** — o default do filtro é `level=true`, que normaliza o sinal de volta pra 0 dB depois de limitar (ver `sirius-scale/frameworks/copy/video-criacao-tecnica.md` §2)).
- ✅ **Trilha ~18–24 dB abaixo da voz.** Bate com o `volume=0.06` da receita
  (≈ −24 dB), que veio de medição na peça de referência. Duas fontes
  independentes no mesmo lugar — é a linha mais confiável desta seção.
- SFX entre a voz e a trilha. **Novo, adotar:** teto de **1 SFX a cada 15–20s**.
  A receita não tem regra de SFX; o pipeline também não tinha.
- ⚠️ Continua valendo: **nunca `sidechaincompress`/ducking** (reprovado, a
  trilha oscila na respiração). Volume fixo e baixo.
- ⚠️ **Medição real (segundo negócio):** as duas peças cortadas saíram a **−19,4 e
  −21,4 LUFS** — nível de trilha de fundo, não de narração. A corrente da
  receita corrige; **aplicar no master, nunca por clipe** (por clipe, o volume
  oscila a cada corte).

## 4. Texto em tela — onde os dois documentos discordam

Três tensões, e nenhuma delas é "um está errado":

1. **7 palavras (dele) × 3 palavras (receita).** Objetos diferentes: o dele é
   card/apoio em VSL horizontal; o da receita é **legenda queimada em
   vertical**, aprovada no caso-base (pelo Rodrigo). Regra: legenda queimada = até 3;
   card de apoio = até 7.
2. **"Nunca bounce ou spin" (dele) × pop de escala da receita**
   (`{\fscx90\fscy90\t(0,120,\fscx100\fscy100)}`). O pop **não é bounce**: vai
   de 90% a 100% em 120ms e para — não passa de 100% nem volta. Não trocar o
   aprovado citando essa linha.
3. **Fade de entrada 0,2–0,3s (dele) × frame 0 em opacidade cheia (receita).**
   Contradição real, e a receita ganha **no gancho**: o texto tem que estar
   legível antes do scroll. Fade de entrada só depois do gancho.
4. ✅ **Branco com sombra** (dele) = `Outline 0, Shadow 6` da receita
   (contorno preto foi o que dava cara amadora). Confirmação cruzada.

### 4.1 Onde o texto entra num plano fechado de expert — *VARIAÇÃO ISOLADA (um criativo de 85s de um segundo negócio)*

O mapa dizia "texto no centro" e a zona segura do formato (y 295–1625)
permitia. Na primeira renderização, **tudo que estava no centro caiu em cima
da boca do expert** — e, no insert de depoimento, nos óculos da pessoa do
depoimento. Zona segura de plataforma não é zona livre de rosto: quem manda é o
enquadramento.

⚠️ **O mecanismo é UNIVERSAL, o número é desta gravação.** "Medir onde está o
rosto antes de posicionar texto" não depende de cliente nenhum. Os valores
abaixo são daquele enquadramento e **não se copiam pra outra peça**.

📌 **No caso de origem, os valores moravam numa fonte única:** o gerador de cards
daquele kit de vídeo, com uma trava que quebrava se uma faixa invadisse a zona do
rosto ou saísse da zona segura. Não repetir número em vários documentos (README,
briefing, framework) — três cópias já divergiram entre si (achado num pente fino) e
duas mandariam o card pro lugar errado.

Medido no vídeo (1080×1920, expert gravando fechado):

- **Rosto ocupa y≈840–1400.** Nada de texto ali, em nenhum bloco.
- **Faixa superior** — hook empilhado, quebra de objeção, gráfico, número do
  depoimento. Fica "na parede", acima da cabeça.
- **Faixa inferior** — impacto de uma linha, reforço, marca no RV, CTA. Abaixo
  do queixo, dentro da zona segura, e só cabe **uma** linha.
- **Insert 9:16 feito de fonte 16:9** (painel nítido no meio, bandas
  desfocadas em cima e embaixo): número na **banda desfocada de cima** —
  contraste pronto, rosto livre, legenda segue na banda de baixo.
- **Overlay e legenda disputam a faixa inferior.** Quando o overlay já diz a
  frase, ou é momento de marca/CTA, a legenda sai naquela janela. Nunca os
  dois no mesmo lugar.

Regra prática: **antes de posicionar qualquer texto, extrair um frame do
próprio corte e medir onde está o rosto.** Custa 1 segundo; evitou 3 renders.

**Abaixo do queixo não é colado no queixo** — *VARIAÇÃO ISOLADA (criativo vertical, 11/2026)*. Card posto no queixo
medido + uns 17 px passava em todo portão (texto fora do rosto, dentro da zona segura) e foi devolvido pedindo os cards
mais abaixo. O queixo medido é o **piso** (o card nunca sobe dele), não a posição. O card senta na linha em que a
legenda sozinha se centra, com a legenda que entra embaixo dele na conta, e não passa do pé da zona segura. Descer até
encostar no pé foi testado e descartado: o card cai na faixa que o botão do anúncio de Stories cobre (seção de story de
anúncio do `frameworks/design/margens-seguranca-vertical.md`).

### 4.2 Marca em transição de nome — *VARIAÇÃO ISOLADA (segundo negócio)*

O asset "logo horizontal" era o wordmark do **nome antigo** do produto; a peça diz
o **nome novo** do começo ao fim. Wordmark antigo no frame do produto contradiz a
copy. Saída: **ícone da marca (só a forma, tingido de off-white) + o nome novo em
ouro** — a forma é a mesma nas duas fases, o nome é o novo. Conferir em toda peça
enquanto durar a transição.

### 4.3 Texto solto sobre vídeo não segura contraste — *princípio UNIVERSAL, paleta VARIAÇÃO ISOLADA (um criativo de 85s de um segundo negócio)*

A primeira versão da peça pôs texto ouro e vermelho direto sobre o vídeo (parede
de ripas, camiseta preta, banda desfocada clara). Com sombra e tudo, o Rodrigo
reprovou: "pouco contraste e ruim para ler". A versão que passou põe **todo
texto em placa** (preto 86% + barra ouro, ou vermelho sólido no impacto) — e o
`check` do HyperFrames mede isso: 10/10 em WCAG AA.
**UNIVERSAL** (é legibilidade, não gosto — mesma natureza do
`sirius-scale/frameworks/design/margens-seguranca-vertical.md`): card de apoio sobre footage precisa de fundo
sólido; texto solto fica só pra legenda queimada, que tem a sombra aprovada da
receita. E quando a ferramenta tem medidor de contraste, **quem decide é o
número, não o olho**.

**VARIAÇÃO ISOLADA (segundo negócio):** a paleta desta placa — preto 86% + barra
ouro, e vermelho sólido no bloco de impacto.

## 5. ✅ Hierarquia de atenção — três fontes, mesma conclusão

*Ouve > lê > vê*, e nunca sacrificar clareza de áudio por estética visual
(dele) = *"audio is primary, visuals follow"* e corte nascendo de fronteira de
palavra e silêncio (video-use). É a base de todo o pipeline: a decisão de corte
é decisão de texto e de áudio; imagem entra depois.

## 6. ✅ Nada antes do gancho — três fontes

Sem logo, sem vinheta, sem "olá, tudo bem" (dele, regra 9) + legenda e headline
no frame 0 em opacidade cheia (receita) + b-roll marcante nos 3 primeiros
segundos em vez de animação (o método externo de edição por IA citado no cabeçalho).

**Candidato a CONSISTENTE** — três fontes independentes, uma delas aprovada no
caso-base. Promoção pendente de decisão do Rodrigo.

### 6.1 Hook novo emendado numa VSL que já roda — *VARIAÇÃO ISOLADA (um cliente de perpétuo, 6 hooks; sem dado de conversão ainda)*

Saiu da revisão de olhos frescos dos 6 hooks (evidência no caso de origem):

- **O quadro 0 é a capa do player.** 3 dos 6 brutos abriam de olho fechado (piscada nos 0,2 s iniciais).
  Conferir os 10 primeiros quadros; se a voz ainda não começou, segurar o primeiro quadro de olho aberto
  (congelar o quadro de abertura). Com a fala já correndo, não congela — descasa a boca.
- **A última palavra tem que ser lida antes da transição.** O corte encaixado no silêncio deixava 0,00–0,11 s
  depois da fala, e o flash de emenda engolia o "é." final. ~0,5 s de respiro antes do flash.
- **Legenda até 3 palavras por bloco.** Medido na VSL do editor do cliente: 1–3 por vez. Com 4–9 o bloco
  pesava justamente nos segundos em que mais se perde gente.
- **Estímulo visual antes de 3 s sem tirar a leitura do quadro 0:** a headline continua cheia no quadro 0 e
  anda com a fala (a palavra-chave pulsa quando é dita, a barra corre na palavra).
- **Emenda sem recomprimir o corpo:** o hook termina num flash, o corpo começa dentro do flash do editor, e
  os dois lados saem do x264 com os mesmos parâmetros → concat por cópia (0 erro de decodificação nas 6).

## 7. Perguntar só o que não está em arquivo

O documento original abre com 11 perguntas de contexto. Aqui, metade já está
escrita: nicho, ticket, oferta e bônus estão em `expert/produtos/<produto>.md`;
temperatura de tráfego e objetivo estão no `briefing.md` do lançamento
(`lancamentos/<AAAA-MM-nome>/briefing.md`); paleta e tipografia estão no
`expert/brand.md`; nível de consciência está no `avatar.md` do lançamento.

**Regra:** ler os arquivos primeiro, perguntar só o buraco (`sirius-scale/REGRAS.md` §2).
Perguntar o que já está escrito queima a confiança do time.
Sobram, tipicamente: formato da VSL, presença de câmera do expert, que b-roll
e depoimento existem, player, e duração já gravada.

## 8. Checklist de entrega — os dois lados

Lado técnico: frame nos pontos de corte, estalo de áudio, legenda escondida
atrás de overlay, duração batendo com o EDL. No caso de origem, quem conferia
isso era o video-use (ferramenta externa). Editando no CapCut ou com editor, sem
ele, quem edita confere esses quatro itens à mão, no vídeo exportado. O
documento cobre o lado editorial, que nenhuma ferramenta olha:

- [ ] Ortografia de todo texto em tela, e legibilidade **no celular**
- [ ] Trilha mixada sem competir com a voz
- [ ] 3 primeiros segundos com estímulo visual e sonoro
- [ ] CTA com tela limpa, zero distração
- [ ] VSL assistida do início ao fim, sem pausar

Os dois rodam. Nenhum substitui o outro.

## 9. O que NÃO adotar

- **Tabela de cor/tipografia por nicho** (saúde = azul, finanças = dourado…).
  A marca vem do `expert/brand.md` do cliente. Usar a tabela só se não existir
  `brand.md`, e **dizer isso na entrega**.
  *(A linha "marketing digital" da tabela coincide com duas decisões já
  tomadas num segundo negócio — tela real em vez de depoimento escrito, e descarte
  dos depoimentos sem lastro. Coincidência, não fonte.)*
- **As metas de retenção** (>70% em 0–30s, >40% no meio, >25–30% até o CTA,
  CTR 5–10%). Fonte não nomeada e não medida na nossa base — não citar como
  meta nossa antes de medir. Ficam na lista de medições pendentes.
- **A persona** ("10 anos, VSLs que geram milhões"). Não muda o output e colide
  com o tom da casa (`sirius-scale/REGRAS.md` §1).
- **Estimativa de 140–160 ppm depois de gravado** (ver §0).

## 10. O que transfere e o que é do caso

**Transfere pra qualquer cliente:** a taxonomia de blocos, o encaixe no EDL
(§1), a hierarquia de atenção (§5), a regra de nada antes do gancho (§6), o
teto de SFX, o checklist editorial (§8) e a disciplina de perguntar só o buraco
(§7). Nada disso depende de quem é o cliente.
Também transfere **como mecanismo** o §4.1 (rosto manda, não a zona segura) e
o §4.2 (marca em transição) — os valores de `y` são deste enquadramento.

**Transfere inteiro, e é o mais transferível do arquivo:** o princípio do §4.3
(card sobre footage em placa; medidor de contraste decide, não o olho). Só a
paleta é do segundo negócio.

**É do caso (o caso-base):** todo número da receita citado aqui — nível de
áudio, 3 palavras por bloco de legenda, `Shadow 6`, Poppins. São o padrão do
editor do expert do caso-base, aprovados **pelo Rodrigo**. Em cliente novo estão
errados por definição: o jeito de achar os certos é o passo 0 da receita (pedir
peça de referência).

**Ainda sem base nenhuma:** as faixas de velocidade de corte por bloco (§2) e
os níveis relativos de SFX (§3). São alvo inicial, não regra.
