---
name: ig-pt-br
description: "Camada em português do Brasil para o pacote de skills ig-* (instagram-agent-skill). Use sempre que o conteúdo de Instagram for em português e o trabalho pedir nota de gancho, cronômetro de roteiro, arquivo de referências do nicho (swipe), humanizador, painel de cara de IA ou conferência de legenda: as ferramentas originais são em inglês e erram em português (acento, R$ 18.000, saudação, Ninguém te conta que). Traz 27 fórmulas de gancho em PT, léxico de clichês em PT e versões em PT dos scripts. Não altera nenhum arquivo do pacote original."
---

# ig-pt-br: o pacote Instagram em português

As skills `ig-*` (reel, carrossel, legenda, stories, plano, auditoria, perfil, comentário, resposta, DM, reaproveitamento, humanizador, pesquisa) são o **método**: continuam valendo e devem ser lidas. Esta camada troca só o que é **idioma**: as ferramentas que pontuam texto e os dados (fórmulas e léxico). Em português as originais dão resultado errado: partem palavra com acento, ignoram "R$ 18.000", dão nota 40 para "Ninguém te conta que…" (a melhor fórmula do pacote) e dizem "0 termos de enchimento" numa legenda cheia de clichê.

## Qual script usar (original → português)

Pasta: `C:\Users\User\.claude\skills\ig-pt-br\` (em outro computador, `~/.claude/skills/ig-pt-br/`). Comando: `python <script> ...` (os scripts já forçam UTF-8 na saída).

| Para quê | Original (inglês) | Use em português |
|---|---|---|
| Nota e ranking de ganchos | `ig-reel/hookscore.py` | `hookscore_pt.py ganchos.txt` (ou `--hook "..."`, `--wpm 175`) |
| Fórmulas de gancho | `ig-reel/hooks.json` (26) | `hooks.pt.json` (26 + 1 local) |
| Cronômetro do roteiro | `ig-reel/beats.py` | `beats_pt.py roteiro.txt --target 30 --wpm 175` |
| Referências do nicho (swipe) | `ig-viral/swipe.py` | `swipe_pt.py coletado.tsv --out <pasta do cliente>/instagram/swipe.md` |
| Humanizar um rascunho | `ig-human/humanize.py` | `humanize_pt.py rascunho.txt --report` |
| Painel de cara de IA | `ig-human/detect.py` | `detect_pt.py rascunho.txt` (ou `antes.txt depois.txt`) |
| Léxico de clichês | `ig-human/slop.json` | `slop.pt.json` |
| Conferir legenda | `ig-caption/caption.py` | `caption_pt.py legenda.txt --keywords "termo1,termo2"` |
| Nota do perfil | `ig-profile/rubric.json` | o original (é critério de leitura, não de idioma) |

`ig-comment`, `ig-reply`, `ig-dm`, `ig-story`, `ig-plan`, `ig-carousel`, `ig-repurpose` e `ig-audit` não têm script de idioma: escreva **direto em português do Brasil**, no tom do `voice.md` do cliente (pra, né, a gente, quando o expert fala assim). Os scripts originais que não dependem de idioma continuam valendo.

## Onde fica o estado (cliente x conta própria)
As skills `ig-*` dizem `~/.claude/instagram/voice.md`, `swipe.md`, `log.md`, `plan.md`. **Para trabalho de cliente, troque esse caminho pela pasta `instagram/` da pasta do cliente** (como já está em `Pedro Sachet` e `Full Concepty Academy`), em toda leitura e gravação. `~/.claude/instagram/` só vale para a conta do próprio Anderson/UP. Se `voice.md` não existir, peça três reels ou legendas do expert e escreva a voz antes de roteirizar (o modelo é `voice-modelo.md` na pasta `instagram/` do cliente). Informe o ritmo real de fala com `--wpm`.

## Regras do pacote que continuam valendo
- **Nada é postado, seguido, curtido ou enviado.** Entrega texto; quem posta é o usuário (ou a ferramenta aprovada dele, só para resposta automática a palavra-chave).
- **Nunca fazer login no Instagram pelo usuário nem pedir senha.** A pesquisa (`ig-viral`) lê perfis públicos no ritmo humano, com o usuário presente quando pedir login, no máximo uma vez por mês. Sem raspagem em volume e sem serviço de coleta. Copie a **fórmula**, nunca o vídeo, o roteiro, a voz ou a edição; cite a conta de cada linha.
- **DM só para quem agiu primeiro** (comentou a palavra, respondeu o Story). Dois follow-ups, no máximo.
- **Nunca inventar** número, cliente, resultado ou depoimento: deixe `{{seu número}}` e avise.
- Humanize e confira antes de mostrar qualquer texto.

## Como ler as notas (o que a camada mede e o que não mede)
- `hookscore_pt` **barra gancho fraco** (saudação, preâmbulo, "pare de rolar", sem número, sem nada em jogo). Ele **não escolhe** qual de dois ganchos bons vai render: isso o gráfico de retenção diz. O autor do original mediu isso em inglês (separa ruim de real, AUC 0,83; separa acerto de erro do mesmo criador, AUC 0,56, quase moeda).
- Teste local em português (`testes/test_pt.py`, 42 verificações, todas passam): 14 ganchos bons e 12 ruins, **escritos por quem fez a camada** (não são reais): os bons ganham em 100% dos pares e todos os ruins ficam abaixo de 50. É prova de que a camada não erra mais por acento e idioma, **não** de poder de previsão.
- Teste com dados reais, só local: 17 reels do nicho do Pedro. A camada nomeou fórmula em 9 (o original, em 0) e concordou com a leitura manual (demonstração sem fala = #18, pergunta literal = #16, série com nome fixo). Correlação entre nota do gancho e views: 0,37, com n = 17, **sem significância**. Trate como indício.
- `swipe_pt`: o que não vira fórmula (**sem fórmula**) é a coluna mais valiosa: leia à mão, ali mora a fórmula que falta. Sem login, o "gancho" costuma ser a primeira linha da legenda, não a fala: diga isso no relatório.
- `detect_pt`: os limites das notas foram herdados do inglês; use para **comparar rascunho antes e depois**, não como nota absoluta. Os checks de caracteres invisíveis, travessão e aspas curvas não dependem de idioma e são confiáveis.
- `humanize_pt` só troca ou apaga **expressões fixas** (saudação, "neste vídeo eu vou te mostrar", "marque alguém que precisa ver isso"). Estruturas como "não é só X, é Y" e vocabulário de IA são **sinalizados**: reescreva você. Depois de humanizar, releia: apagar uma isca pode tirar o único pedido da legenda, e a legenda precisa ter **um** pedido.
- `caption_pt` e `beats_pt` mantêm os rótulos e alertas em inglês (PASS/WARN/FAIL, "Beat 2 runs past 4s"): ao entregar, traduza. O limite de 5 hashtags e a janela de ~125 caracteres são regras de plataforma citadas pelo autor do original; plataforma muda, **confirme** antes de tratar como fato.

## Estender e manter
- Nova fórmula: acrescente em `hooks.pt.json` (id novo, `match` **sem acento e em minúsculas**, e o id em `classify_order`). A classificação roda sobre o gancho normalizado (minúsculo, sem acento).
- Novo clichê: acrescente em `slop.pt.json` (`phrases` só para expressão fixa sem gênero e número; o resto em `structures`, que só sinaliza).
- Depois de qualquer mudança: `python testes/test_pt.py`. Se atualizar o pacote original, rode de novo: as versões `humanize_pt`, `caption_pt` e `beats_pt` importam o original em tempo de execução, e se ele mudar de estrutura o teste acusa.
- Autoria e licença: ver `NOTICE.md` (derivado do pacote MIT de Jake Schincariol).
