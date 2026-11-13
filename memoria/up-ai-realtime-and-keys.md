---
name: up-ai-realtime-and-keys
description: "IA do Up deve rodar em tempo real (API), não em rotinas; assinante usa a própria chave e escolhe o modelo; anexos nas conversas e aprendizado dos agentes"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-08T11:44:11.541Z
---

Pedido do usuário (2026-10-08): tudo que depende de IA no Up (sugestões do SDR, conversas com agentes) roda em tempo real via API, sem rotinas/laços agendados e sem "ligar tudo" de uma vez.

- Chave: o usuário acha melhor cada assinante colocar a própria API (Claude e/ou OpenAI) e pagar separado; o Up só alimenta skills e agentes. Pediu minha sugestão (alternativa: crédito dentro do Up). Assinante escolhe o modelo (ex.: Sonnet ou Opus; GPT para imagem).
- Conversas com agentes: aceitar anexos (arquivos, imagens, documentos, áudio), como no Claude.
- Aprendizado: arquivo/estratégia de assinante útil para as skills aparece no painel do dono como sugestão; vai para uma pasta no Drive e o dono decide se usa.

**Why:** reduzir custo fixo e fazer os agentes evoluírem com o uso dos assinantes.
**How to apply:** IA no servidor = chamada síncrona por evento (não cron) com cofre de chave por workspace; ver [[up-chat-agents]] e [[up-backlog-and-social-flow]].
