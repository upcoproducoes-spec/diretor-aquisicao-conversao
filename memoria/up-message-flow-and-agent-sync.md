---
name: up-message-flow-and-agent-sync
description: Fluxo de mensagens (estilo ManyChat) mora em Automações; Comentários só inbox e SDR; sincronizar skills/agentes do Claude com os agentes do Up fica para depois
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-08T18:39:42.869Z
---

Decisões do usuário (2026-10-08):
- Fluxo de mensagens por palavra-chave (resposta pública, DM com até 3 botões, caminhos por botão, esperas, "digitando") fica em Automações com gatilho "Comentário". A aba Comentários fica só com a entrada de comentários e o envio ao SDR/Camila. As regras antigas por palavra-chave continuam funcionando até serem convertidas em automações.
- Pendente depois: o mesmo fluxo no WhatsApp (mais um passo no mesmo editor).
- Agentes do chat do Up (diretor, estrategista, copy, design, vídeo, tráfego e o futuro "Criador de Conteúdo"/social media do expert) devem ter o mesmo conhecimento das skills do Claude Code. Plano: ao usuário dizer "atualize no Up", enviar o texto das skills para as instruções de cada agente (PUT /v1/ai/agents/:agent). As skills grandes (copywriting 65 KB + 185 arquivos de referência) exigem uma biblioteca de conhecimento com busca de trechos. Não fazer agora: primeiro montar os agentes de design, vídeo e conteúdo.
- O agente de conteúdo do expert (ideias, pesquisa de viral, roteiros, carrosséis, upload de vídeo bruto e imagens para a pasta compartilhada no Drive) é uma das últimas coisas: o dono comanda tudo primeiro.

**Why:** muita ideia parando na metade; o usuário quer terminar uma coisa por vez.
**How to apply:** não puxar o assunto do agente de conteúdo antes de o fluxo de mensagens estar fechado; ver [[up-ai-realtime-and-keys]] e [[up-chat-agents]].

Atualização (2026-10-09), ordem combinada e visão dos agentes:
- Ordem do trabalho: 1) terminar a API oficial do WhatsApp com o Pedro (login da Meta, META_WA_CONFIG_ID no Render, Pedro como testador do app UpLaunch); 2) Amazon SES (para parar de pagar o FullFunnel); 3) biblioteca de conhecimento; 4) montar os agentes.
- O Diretor do Up deve fazer lá tudo o que faz aqui: o usuário conversa com o Diretor, aprova, e o Diretor chama os revisores e encaminha para quem precisa (copy aprovada vai para o Design, e assim por diante), de forma quase automática, mas SEMPRE com aprovação do usuário em cada etapa.
- "Novo conteúdo" deve virar um agente (Criador de Conteúdo): o usuário chama, conta a ideia e o agente ajuda a compor, depois manda para o Design ou o editor de vídeo; hoje é um formulário com título.
- Design e vídeo sempre consultam a identidade visual de cada projeto (montar depois).
- Claude é o padrão nos agentes; GPT só como opção e para comentários simples.
