---
name: up-producao-conteudo
description: Produção de conteúdo só do que foi escolhido em Quero produzir, segunda 10h (Pedro) e 10h15 (Bia); IA de comentários manual com opção automática
metadata:
  node_type: memory
  type: project
  originSessionId: bc99cf1b-f068-4c2c-91e5-523ad26e92b5
  modified: 2026-11-26T17:15:35.938Z
---

Decidido em 26/11/2026 pelo Anderson:
- **Criador de conteúdo não usa API do Claude no Up.** Produção = rotina local SEMANAL (`up-producao-conteudo-pedro` seg 10h, `up-producao-conteudo-bia` seg 10h15, 2h depois das sugestões das 8h/8h15). Só produz o que foi marcado em "Quero produzir" (lê `up fila content`): carrossel/estático/stories viram post pronto (HTML→PNG→JPG, imagem OpenAI medium só se precisar, máx 2/pedido) aguardando aprovação; reels viram roteiro final na conversa. Responde na conversa do Criador. Não pega sugestão sozinha (decisão de 26/11: rodar 3x/dia gastava demais).
- **API no Up fica só para responder comentários:** botão "Gerar resposta com IA" por comentário (rota /social/comments/:id/ai-draft); opção "Gerar respostas automaticamente" em Integrações (campo sdr_realtime) — padrão desligado. Pedro tem chave OpenAI; Bia ainda sem chave (Anderson cola).
- Sugestão tem status `produced` + post_id (migração 0104).

**Why:** custo e controle — o Anderson quer clicar para gerar e escolher quando automatizar.
**How to apply:** não ligar IA automática nem agente de conteúdo por API no Up sem ordem; ajustes de volume/horário vão nas duas tarefas. Relacionado: [[up-chat-agents]], [[up-backlog-and-social-flow]].
