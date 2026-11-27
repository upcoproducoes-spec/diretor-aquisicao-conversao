# Checklist — Criativo (prompt de arte, peça gerada, vídeo editado)

## Leia antes de abrir o entregável

1. `.claude/agents/designer.md` — o que o agente entrega e como ele confere a peça
2. `expert/brand.md` **e** `lancamentos/<AAAA-MM-nome>/identidade-visual.md` se existir —
   a do lançamento **prevalece**
3. `sirius-scale/frameworks/design/margens-seguranca-vertical.md`
4. A copy aprovada da peça, em `entregas/<lançamento>/`
5. `frameworks-da-casa/` — o que vocês já corrigiram em arte e vídeo vale mais que o resto
6. Se o estático foi montado em HTML: `sirius-scale/frameworks/design/estatico-anuncio-html.md`
7. Se for vídeo: `.claude/agents/video.md` (os dois modos, a régua e o que a entrega tem que
   trazer), `sirius-scale/frameworks/copy/edicao-video-receita.md` e
   `sirius-scale/frameworks/copy/edicao-video-criativos.md`
8. Se for peça de captação da Black: `sirius-scale/frameworks/design/captacao-da-black-arte-do-estatico.md`
   (arte) ou `sirius-scale/frameworks/copy/captacao-da-black-edicao-de-video.md` (vídeo)

---

## A. Texto da peça (onde mais dá erro)

- [ ] **Cada palavra do texto embutido bate com a copy aprovada**, letra por letra.
      Compare os dois lado a lado, não de memória.
- [ ] **Acentuação correta em tudo.** É a falha histórica do gerador de imagem: no caso
      de origem, um gerador antigo errou acento em 2 de 2 testes (palavra sem acento,
      acento trocado, cifrão virando "RS"). Erro de escrita na arte derruba a
      credibilidade de quem ensina: é 🔴, não estética.
- [ ] **Nenhum texto de cena inventado.** O gerador acrescenta texto que ninguém
      pediu — placa, cartaz, rótulo, tela, papel com letras, legenda no fundo. É o risco
      que sobrou nos geradores atuais, que acertam o texto pedido. Audite a peça
      **inteira**, não só a headline: qualquer texto visível que não está na copy é achado.
- [ ] Nenhum texto cortado, sobreposto ou ilegível no tamanho real.

## B. Identidade visual

- [ ] Cor, tipografia e estilo vêm da fonte certa — `identidade-visual.md` do
      lançamento na frente do `expert/brand.md` genérico, quando existir.
- [ ] Logo correto do evento/lançamento, não o genérico da marca.
- [ ] **Os assets reais de vocês foram inventariados antes de desenhar.** Peça já
      aprovada parada numa pasta vale mais que suposição de estilo — se existia e foi
      ignorada, é achado.

## C. Formato e margens

- [ ] Dimensão exata do formato pedido (feed 1:1, story 9:16, capa, etc.).
- [ ] Margens de segurança conforme `margens-seguranca-vertical.md` — e **sem
      inflar "pra garantir"**, que é o erro registrado lá.
- [ ] Elemento crítico (headline, CTA, logo) fora da zona que a interface come, no
      topo e na base.
- [ ] **Story que roda como anúncio:** texto, logo e botão desenhado terminam em y≈1536,
      não em 1625, porque o botão da Meta cobre os ~20% de baixo. Dali pra baixo só fundo.

## D. Conceito

- [ ] A peça comunica o ângulo do conceito aprovado, não um ângulo novo que o
      designer resolveu criar.
- [ ] Arte de dor retrata **emoção real do avatar**, não metáfora abstrata.
- [ ] A copy foi aprovada **antes** de a arte ser gerada — não o contrário.

## E. Se for vídeo

- [ ] Seguiu os números de `edicao-video-receita.md` §2 (legenda, headline, logo,
      áudio, motion) — não valores reinventados. Os de lá foram aprovados no caso de
      origem: aqui valem os que vocês aprovaram a partir da peça de referência do
      editor de vocês (passo 0 da receita), se já existirem em `frameworks-da-casa/`.
- [ ] Se a edição foi por comando (ffmpeg): master em 2 passos, conforme a receita §1.
- [ ] Sincronia feita pelo método que funciona: **transcrição automática só pelo
      tempo, copy pelo texto**. Legenda com o texto da transcrição automática é achado.
- [ ] As armadilhas conhecidas foram conferidas no arquivo exportado, não presumidas:
      - fonte trocada em silêncio (o renderizador troca a fonte que não achou sem
        avisar) → confira a fonte num frame ampliado
      - taxa de amostragem → o áudio sai a 48 kHz (a normalização de volume já devolveu
        96 kHz sem avisar)
      - ducking fazendo a trilha oscilar → escute, não confie no parâmetro. Ducking não
        entra, mesmo a skill `hyperframes-audio` oferecendo: a trilha fica em volume fixo
- [ ] **Corte limpo e legenda lisa sozinhos não são entrega.** Sem motivo dito, a peça tem
      motion de verdade, áudio tratado e fecho com a marca. O que ficou de fora foi dito,
      com o porquê.
- [ ] Se foi montado aqui (modo B): as ferramentas foram confirmadas antes de prometer
      render, a peça-mãe foi olhada em quadros antes do render final e as irmãs herdaram
      dela, mudando só o que o conteúdo pede.
- [ ] Nome do arquivo carrega o ID do criativo (`VDNN`) da copy, sem renumerar.

## F. Entrega

- [ ] A entrega é a que o agente `designer` promete (`.claude/agents/designer.md`):
      prompt completo pronto pra colar no gerador, com o texto embutido, ou a peça
      montada em HTML a partir de material real. Vídeo: a que o agente `video` promete
      (`.claude/agents/video.md`, "Entrega"), com a peça de partida, o que foi conferido
      item por item, a pasta do projeto e o que a conferência não cobre.
- [ ] Se a imagem foi gerada (no ChatGPT ou em qualquer gerador), a auditoria de
      ortografia foi feita com zoom, palavra por palavra, contra a copy aprovada — e
      cobriu o texto de cena, não só a headline.
- [ ] Dimensão e destino da peça declarados.
