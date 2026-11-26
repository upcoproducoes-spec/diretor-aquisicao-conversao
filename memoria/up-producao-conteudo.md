---
name: up-producao-conteudo
description: "Rotina diária de produção de conteúdo (Pedro 10h, Bia 10h15) e IA de comentários manual com opção automática"
metadata:
  node_type: memory
  type: project
  originSessionId: bc99cf1b-f068-4c2c-91e5-523ad26e92b5
  modified: 2026-11-26T17:15:35.938Z
---

Decidido em 26/11/2026 pelo Anderson:
- **Criador de conteúdo não usa API do Claude no Up.** Quem produz é a rotina local (tarefas agendadas `up-producao-conteudo-pedro` 10h e `up-producao-conteudo-bia` 10h15, modo Auto). Ela pega 1 sugestão/dia da lista da semana (só carrossel, estático, stories que NÃO dependem do expert gravar ou mandar foto), escreve texto (skills ig-*), monta arte em HTML→PNG (Chrome headless)→JPG (ffmpeg), imagem OpenAI só se precisar (medium, máx 2/dia, nunca rosto/mão), sobe no Up, `posts criar` + `posts enviar` (aguardando aprovação) e `sugestoes produzida`.
- **API no Up fica só para responder comentários:** botão "Gerar resposta com IA" por comentário (rota /social/comments/:id/ai-draft); opção "Gerar respostas automaticamente" em Integrações (campo sdr_realtime) — padrão desligado. Pedro tem chave OpenAI; Bia ainda sem chave (Anderson cola).
- Sugestão tem status `produced` + post_id (migração 0104).

**Why:** custo e controle — o Anderson quer clicar para gerar e escolher quando automatizar.
**How to apply:** não ligar IA automática nem agente de conteúdo por API no Up sem ordem; ajustes de volume/horário vão nas duas tarefas. Relacionado: [[up-chat-agents]], [[up-backlog-and-social-flow]].
