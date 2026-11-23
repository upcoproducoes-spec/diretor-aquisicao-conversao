---
name: instagram-agent-skill
description: "Skills ig-* (instagram-agent-skill, MIT) instaladas em 23/11/2026 e usadas nas rotinas semanais de sugestões do Pedro e da Bia; dados por expert na pasta instagram/ de cada projeto"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-23T13:52:19.140Z
---

Em 23/11/2026, a pedido do Anderson, instalei as 13 skills de github.com/Jakeschincariol/instagram-agent-skill (commit d03c56b, MIT, só biblioteca padrão do Python, sem rede) em `~/.claude/skills/ig-*`: ig-viral (pesquisa por múltiplo fora da curva = views ÷ mediana da conta; >3× é sinal), ig-plan, ig-reel (26 fórmulas de gancho em hooks.json, hookscore.py, beats.py), ig-carousel, ig-story, ig-caption (caption.py), ig-human, ig-audit, ig-profile, ig-comment, ig-reply, ig-dm, ig-repurpose.

As rotinas `up-sugestoes-pedro` (segunda 8h) e `up-sugestoes-beatriz` (segunda 8h15) foram reescritas para usar o método e LIGADAS. Adaptações: dados por expert em `<pasta do projeto>/instagram/` (voice.md, swipe.md refeito a cada 28 dias, log.md), nunca em `~/.claude/instagram`; `python` (não python3); scripts afinados para inglês, nota só como pista; sem login no Instagram, sem senha, leitura em ritmo humano (até 12 contas × 12 posts); sem yt_dlp.

**Why:** o Anderson quer sugestões baseadas no que está funcionando no nicho de cada expert.
**How to apply:** pedidos de Reels, ganchos, carrossel, stories e legenda do Pedro ou da Bia podem usar as ig-*, sempre em português e com a pasta instagram/ do expert. voice.md nasce como rascunho para o Anderson revisar. Ver [[up-backlog-and-social-flow]] e [[vale-para-todos-os-projetos]].
