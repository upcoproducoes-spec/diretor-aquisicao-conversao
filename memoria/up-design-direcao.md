---
name: up-design-direcao
description: Redesenho do Up — estilo A (Apple refinado), regras de organização e ordem de aplicação aba por aba
metadata:
  type: project
---

Decidido em 26/11/2026 pelo Anderson: o Up segue o **estilo A · Apple refinado** (o visual atual, com os tokens do app.css, só que arrumado e com os mesmos componentes em todas as telas). 21st.dev serve só de referência (é React; o Up é JS puro). Prévia aprovada: `Up/docs/prototipos/prototipo-design-up.html`.

Regras para qualquer tela:
1. A tarefa começa e termina no mesmo lugar (painel lateral `dialog.sheet` na própria tela; nada de ir à Conversa e voltar).
2. Liga/desliga é sempre interruptor (toggleSwitch); ações (tirar, arquivar, excluir) no menu "⋯", excluir com confirmação.
3. Um só jeito de abas e de filtros.
4. Criar algo novo no painel lateral, nunca em prompt() do navegador.
5. Aprovações reúne tudo o que espera decisão (inclusive posts, criativos, tráfego) e abre o mesmo painel da tela de origem.
6. Título da tela igual ao nome no menu.

**Why:** o Anderson achou o Up desorganizado (ex.: botão "Desligar" grande em Campanhas; "Quero produzir" passava por 3 telas).
**How to apply:** feito: painel de produção. Próximos: Campanhas (menu ⋯ no lugar do Desligar), depois aba por aba pelo mapa de fluxos quebrados. Relacionado: [[up-producao-conteudo]], [[up-campanhas-configuracoes]].
