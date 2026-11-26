---
name: up-producao-conteudo
description: Painel de produção no Up (Quero produzir → fila → revisar/ajustar/aprovar no mesmo painel); rotina diária 10h/10h15 só com fila; IA de comentários por botão
metadata:
  node_type: memory
  type: project
  originSessionId: bc99cf1b-f068-4c2c-91e5-523ad26e92b5
  modified: 2026-11-26T17:15:35.938Z
---

Decidido em 26/11/2026 pelo Anderson:
- **Criador de conteúdo não usa API do Claude no Up.** Produção = rotina local DIÁRIA (`up-producao-conteudo-pedro` 10h, `up-producao-conteudo-bia` 10h15; decisão A de 26/11: roda todo dia mas para na hora se a fila estiver vazia). Lê `up api GET v1/content-suggestions/queue` (kind new = pedido novo; kind changes = ajuste pedido no painel, com o texto do ajuste). Novo: cria post, `up sugestoes produzida <sug> <post>`, `up posts enviar`. Ajuste: PUT no post (agente pode editar changes_requested) e reenviar. Não usa mais a conversa.
- **Painel de produção (26/11, commit 8e2a029):** "Quero produzir" (dono em Conteúdo, expert em Conteúdo > Sugestões) põe na fila e abre um painel lateral (js/production-sheet.js) com etapa, lâminas, legenda, histórico, Pedir ajustes e Aprovar e agendar. Lista "Em produção" no topo das sugestões. Princípio do Anderson: **a tarefa começa e termina no mesmo lugar**.
- **API no Up fica só para responder comentários:** botão "Gerar resposta com IA" por comentário (rota /social/comments/:id/ai-draft); opção "Gerar respostas automaticamente" em Integrações (campo sdr_realtime) — padrão desligado. Pedro tem chave OpenAI; Bia ainda sem chave (Anderson cola).
- Sugestão tem status `produced` + post_id (migração 0104).

**Why:** custo e controle — o Anderson quer clicar para gerar e escolher quando automatizar.
**How to apply:** não ligar IA automática nem agente de conteúdo por API no Up sem ordem; ajustes de volume/horário vão nas duas tarefas. Relacionado: [[up-chat-agents]], [[up-backlog-and-social-flow]].
