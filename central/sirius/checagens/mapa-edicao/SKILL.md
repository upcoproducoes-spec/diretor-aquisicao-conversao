---
name: mapa-edicao
description: Gera o Mapa de Edição de um vídeo a partir da copy/roteiro — o documento trecho a trecho que diz ao editor (humano ou no CapCut) o que fazer de visual, áudio e ritmo em cada bloco. Dispara SEMPRE que mandarem a copy de uma VSL ou o roteiro de um criativo curto pedindo pra editar, preparar a edição, briefar o editor, "montar o mapa", "transformar isso em edição" — mesmo sem citar a skill pelo nome e sem colar instrução nenhuma junto. Também dispara quando o vídeo já foi gravado e o editor precisa do mapa ancorado no tempo real da gravação. Não reescreve a copy: transforma copy em instrução de edição.
---

> Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
> são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
> ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.


# Mapa de Edição — copy vira instrução pro editor

A pessoa manda a copy. Eu devolvo o Mapa de Edição pronto. **Ninguém cola prompt
nenhum** — as instruções de sistema já estão no kit, e esta skill é quem as carrega.

## Passo 0 — Classificar antes de escrever

Duas perguntas, respondidas por mim, não pela pessoa:

**1. Que formato é?**

| Se | Prompt-fonte a carregar |
|---|---|
| VSL / vídeo de venda longo (5 min+) | `sirius-scale/frameworks/copy/prompts-sistema/gerador-mapa-edicao-vsl.md` |
| Criativo curto, vertical, 15–90s (Reels/TikTok/Stories/anúncio) | `sirius-scale/frameworks/copy/prompts-sistema/gerador-mapa-edicao-video-curto.md` |

Na dúvida entre os dois, o critério é a **duração**, não a plataforma: peça de
90s pra baixo usa o de curto, mesmo que seja "uma VSL curtinha". O de curto
comprime a taxonomia (4–6 blocos, não 16) — usar o de VSL numa peça de 60s
gera bloco de 2 segundos, que não é instrução útil pra editor.

**2. A gravação já existe?** Isso muda de onde vem o tempo, e é a diferença
que mais estraga mapa (`sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §0):

| | O mapa é | Tempo vem de |
|---|---|---|
| **Antes de gravar** | briefing: quantos blocos, o que mostrar, quanto deve durar | estimativa por contagem de palavras (140–160 ppm) |
| **Depois de gravar** | o mapa **ancorado**: cada bloco no tempo real da gravação | **timestamp real** (transcrição com tempo ou a linha do tempo do corte) |

⚠️ Depois de gravado, a estimativa por palavra **morre**. Mapa pré-gravação que
sobrevive com os tempos estimados é fonte de erro — reancorar no tempo medido.

## Passo 1 — Ler, nesta ordem

1. **O prompt-fonte** do formato (tabela acima) — é ele que define o formato de
   output: Visão Geral → Instruções Globais → ficha por bloco → Notas Finais.
2. **`sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`** — sempre, nos dois formatos.
   É a versão confrontada com edição real e **ela vence o prompt-fonte** onde
   os dois divergem (tabela do Passo 3).
3. **`frameworks-da-casa/`** — o que vocês já corrigiram em edição vale mais que os dois
   acima (`sirius-scale/REGRAS.md` §4).
4. **Os arquivos de vocês**, pra não perguntar o que já está escrito
   (`sirius-scale/REGRAS.md` §2, `mapa-de-edicao-vsl.md` §7):
   - `expert/dna-expert.md` → voz e jeito de falar
   - `expert/produtos/<produto>.md` → oferta, bônus, preço, garantia, mecanismo
   - `expert/brand.md` → paleta e tipografia (**substitui** a tabela de cor por
     nicho do prompt-fonte)
   - `lancamentos/<AAAA-MM-nome>/avatar.md` → nível de consciência, dor, objeção
   - `lancamentos/<AAAA-MM-nome>/briefing.md` → objetivo, temperatura de tráfego
   - perpétuo: os mesmos arquivos em `funis/<nome>/`
5. Se for peça vertical: **`sirius-scale/frameworks/design/margens-seguranca-vertical.md`** e
   **`sirius-scale/frameworks/copy/edicao-video-receita.md`** (os números de legenda,
   headline, logo e áudio aprovados no caso de origem — ponto de partida, não estilo
   inventado; ver a regra dura 4).

## Passo 2 — Perguntar só o buraco

O prompt-fonte abre com 11 perguntas de contexto. **Metade já está nos arquivos
acima** — perguntar o que já está escrito queima a confiança do time.

Sobram, tipicamente: formato de gravação, presença de câmera do expert, que
b-roll e depoimento existem de fato, player, e duração já gravada.

🔴 **Regra dura que sobrepõe o prompt-fonte:** ele manda "deduzir e registrar
suposições" quando falta dado. **Aqui não.** `sirius-scale/REGRAS.md` §2: faltou dado,
pergunta e para. `[[ASSUMIDO]]` só vale pra decisão de **forma** (duração de
bloco, ordem de dois argumentos) — **nunca** pra número, preço, depoimento,
prova ou dor de avatar. O dado real de vocês está a um arquivo de distância.

## Passo 3 — Onde o framework sobrescreve o prompt-fonte

Estas já foram resolvidas. Não re-litigar, não seguir o prompt-fonte nelas:

| Tema | O prompt-fonte diz | O que vale |
|---|---|---|
| Níveis de áudio | voz −6/−3 dB, trilha −18/−24 dB (fader) | a cadeia da receita, em **LUFS** (`loudnorm I=-16:TP=-1.5:LRA=11` + `alimiter:level=disabled` → `volume=2dB` → `alimiter=0.97`); trilha ≈ `volume=0.06`. Unidades diferentes — não comparar direto. **Medir no master, nunca por clipe**. Quem edita no CapCut ou com editor humano persegue o mesmo alvo, medido no arquivo exportado |
| Ducking | (não trata) | **nunca** abaixar a trilha automaticamente pela voz (`sidechaincompress`) — reprovado, a trilha oscila na respiração |
| Palavras por tela | máximo 7 | 7 vale pra **card de apoio**; **legenda queimada = até 3** (aprovado em vertical) |
| Entrada de texto | fade 0,2–0,3s, nunca bounce | no **gancho**, frame 0 em opacidade cheia (tem que estar legível antes do scroll). Fade só depois do gancho. O pop de escala 90→100% em 120ms da receita **não é bounce** — mantém |
| Texto solto sobre vídeo | branco com sombra resolve | **card de apoio sobre footage exige placa/fundo sólido**. Onde houver medidor de contraste, **o número decide, não o olho** |
| Posição do texto | "centro" | **medir onde está o rosto** num frame do próprio corte antes de posicionar. Zona segura de plataforma ≠ zona livre de rosto — já custou 3 renders |
| Cor e tipografia por nicho | tabela por nicho | `expert/brand.md`. Tabela só se não existir `brand.md`, **e dizendo isso na entrega** |
| Metas de retenção | >70% / >40% / >25% / CTR 5–10% | **não citar como meta** — fonte não nomeada, nunca medida na base de origem |
| Persona | "10 anos, VSLs de milhões" | descartar — não muda o output e colide com `sirius-scale/REGRAS.md` §1 |
| Ritmo em peça curta | tabela de segundos por bloco da VSL | não se aplica; ver `mapa-de-edicao-vsl.md` §2.1 — a régua medida é **plano estático não passa de 6–8s sem evento visual**, e vale como N=1 |

## Passo 4 — Escrever o mapa

Formato exatamente como o prompt-fonte manda (Partes 1 a 4). Por cima disso:

- **Cada bloco recebe o código da taxonomia** (HK, PB, AG, MC, PS-1…) de
  `mapa-de-edicao-vsl.md` §1, o **trecho literal** da copy e o objetivo do bloco (o
  porquê deste take). São os campos com que o editor acha o momento e decide o corte.
  Não inventar formato novo.
- **Toda instrução cita o trecho literal da copy** a que se refere. Sem isso o
  editor não acha o momento na linha do tempo.
- **Toda afirmação forte rastreia até dado real de vocês** (`sirius-scale/REGRAS.md` §2).
  Se um bloco de prova pede número e o número não está em arquivo, o mapa diz
  "falta o dado" — não inventa depoimento nem estatística.
- **Dois tetos que evitam poluição:** nada passa de 30s sem mudança visual
  (VSL longa), e no máximo **1 SFX a cada 15–20s** — numa peça de 60s isso é
  2 SFX na peça inteira.
- **Marcar o nível de confiança** do que for hipótese: a tabela de velocidade
  de corte por bloco não foi medida na base de origem, e a régua de peça curta é
  N=1. Entregar como alvo inicial, dito na cara, não como regra.

## Passo 5 — Salvar e entregar

Salvar sempre, sem perguntar:

```
entregas/<lançamento>/mapa-de-edicao-<slug>-v1.md
```

É a mesma pasta onde o agente `copy` salva o roteiro, então o mapa fica ao lado da copy
que ele dirige e quem for editar acha os dois juntos. Se o vídeo ainda não foi gravado,
salvar mesmo assim: depois da gravação, o mapa é reancorado no tempo real e vira `-v2`.

Ao entregar no chat, **não colar o mapa inteiro**: resumo em lista numerada
(quantos blocos, duração total, os 2–3 pontos que exigem decisão de vocês) + o
caminho do arquivo. Mapa completo é documento, não mensagem.

Se a gravação já existe, esse mapa **é a porta de aprovação antes da edição**: ele
corta, funde e limita antes de qualquer render. Uma aprovação por etapa (corte → mapa →
gráficos → som → b-roll): duas variáveis mudando juntas não deixam saber qual quebrou.
Oferecer o próximo passo em vez de esperar alguém lembrar — "aprovado o mapa, ele vai
pro editor?".

Sem conferência automática do lado de vocês, o lado técnico do vídeo pronto também
fica com quem edita: frame nos pontos de corte, estalo de áudio, legenda escondida atrás
de card, duração batendo com o mapa. As Notas Finais do mapa dizem isso, junto do lado
editorial de `mapa-de-edicao-vsl.md` §8 (ortografia e legibilidade no celular, trilha
sem competir com a voz, 3 primeiros segundos com estímulo, CTA com tela limpa, vídeo
assistido inteiro sem pausar).

## Regras duras

1. **Não reescrever a copy.** A copy entra como está. Se ela tem problema de
   estrutura, isso é assunto do agente `copy` (`sirius-scale/REGRAS.md` §3), em
   separado — dizer numa linha e seguir, não corrigir por dentro do mapa.
2. **Não inventar dado de vocês.** Falta, pergunta (Passo 2).
3. **Depois de gravado, tempo real manda.** Nunca entregar mapa pós-gravação
   com timestamp estimado por contagem de palavras.
4. **Peça vertical não inventa estilo.** Os números da `edicao-video-receita.md` foram
   aprovados no caso de origem; negócio novo refaz o passo 0 dela (pedir uma peça de
   referência já editada pelo editor de vocês) em vez de herdar os números de lá.
5. **Padrão novo que aparecer aqui volta pro framework**, não fica só no mapa
   entregue — vai pra `frameworks-da-casa/` (`sirius-scale/REGRAS.md` §5). O
   `mapa-de-edicao-vsl.md` §2.1 nasceu exatamente assim, de uma peça medida.
