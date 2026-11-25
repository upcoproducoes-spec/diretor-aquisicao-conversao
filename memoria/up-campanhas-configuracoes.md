---
name: up-campanhas-configuracoes
description: "Campanhas do Up se gerenciam em Configurações → Campanhas; o seletor do topo só escolhe; agente nunca cria campanha sozinho"
metadata:
  type: project
---

Decisão do Anderson (25/11/2026): campanha se cria, renomeia, liga a páginas, ganha pasta do Drive, arquiva e **exclui** em **Configurações → Campanhas** (tela `#/campanhas`). No topo de Tarefas, Aprovações, Disparos, Criativos e Páginas o seletor **só escolhe** a campanha, com uma engrenagem ⚙ ao lado que abre essa tela. Excluir é do dono e move tudo (tarefas, disparos, criativos, páginas, planilhas de formulário) para a campanha escolhida ou deixa sem campanha (commit 8cc7d2c, migração 0100).

Origem: uma rotina criou a campanha "Black da Lógica" no Pedro em 24/11 só porque o nome do evento não batia com "Black Friday 2026" (são a mesma coisa). Desde 25/11 o `up.cjs` do Pedro e da Bia não cria campanha sozinho (para e lista as que existem; nova só com `"campanha_nova": true` quando o Anderson pedir) e o CLAUDE.md das duas pastas diz isso.

**Why:** duas campanhas para a mesma coisa espalham tarefas e aprovações.
**How to apply:** entregas usam uma campanha que já existe; na dúvida, perguntar. Ver [[vale-para-todos-os-projetos]].
