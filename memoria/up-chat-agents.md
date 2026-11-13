---
name: up-chat-agents
description: "Como as conversas da aba Conversa do Up (diretor, copywriter, design, vídeo, gestor de tráfego) se ligam às skills e agentes pessoais do usuário"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-05T18:42:40.069Z
---

Conversas do Up (ids no banco): director, strategist (Estrategista: diagnóstico, posicionamento, oferta e funil), copy (Copywriter: e-mails, mensagens, roteiros, scripts e copy), design, video, traffic (Gestor de tráfego). Não há resposta automática: o Claude lê a fila (`GET /v1/chat/pending`, chave de agente) e responde (`POST /v1/chat/<id>/messages`).

Ligação combinada com o usuário (2026-10-05): ao processar uma mensagem, usar as skills e agentes dele:
- Diretor → skill `diretor-aquisicao-conversao` (orquestra estratégia, growth, psicologia, persuasão, copywriting, vendas); funil de VSL também a `funil-vsl-thiago-roas`. Revisão: agentes `revisor-*`.
- Estrategista → skills `estrategia-negocios`, `marketing-digital-growth`, `psicologia-consumidor` e `funil-vsl-thiago-roas`; revisão com `revisor-estrategia`, `revisor-growth` e `revisor-funil-vsl`.
- Copywriter → `copywriting-publicidade` + `persuasao-gatilhos`, agente `copy-writer`, revisão com `revisor-copy`.
- Design → agente `visual-designer` e skills de design/anúncios.
- Vídeo → ainda sem skill (a criar com o usuário).
- Gestor de tráfego → agentes e skills do Claude Ads (`ads-*`, `audit-*`, `creative-strategist`).
Entregas viram tarefa "Aguardando aprovação" no Up, com textos anexados, para o fluxo de revisão com comentários.

Exceção à regra do CLAUDE.md da pasta ECC Repository (não acionar diretor/revisores/skills de marketing sem pedido): vale para processar a fila da Conversa do Up, a pedido do usuário.

Decisão final (2026-10-05): sem API paga por enquanto. O usuário mantém uma sessão fixa na pasta `C:\Users\User\Documents\Claude\Up Operador` (CLAUDE.md com as regras e o atalho `up.cjs`: fila, responder, entregar, revisar, tarefas). Ele chama sempre o diretor ali e a sessão manda o resultado para o Up (tarefa em Aprovações + registro na Conversa); quando diz "fila", a sessão responde o que foi deixado na aba Conversa. A tarefa agendada `up-responder-conversa` (5 em 5 min) está PAUSADA de propósito: a cota semanal do plano Pro estava em 88% e uso extra desligado; ligar depois com frequência calma (ex.: 30 min). Avaliar API paga e custos mais adiante (preços de referência: Haiku 4.5 US$1/5, Sonnet 5 US$2/10 por milhão de tokens). Pendente: skill de Vídeo.

**Why:** o usuário quer que o chat do Up use o time de agentes e skills que ele já montou.
**How to apply:** ao receber "responda a fila" ou similar, consultar a fila, escolher a skill pelo id da conversa e postar a resposta na própria conversa. Veja [[up-requested-features]].

**Regra de 07/11/2026 (Anderson):** dentro do aplicativo Up (Conversa e qualquer chamada de agente feita pelo app), dá para chamar o Diretor ou direto um agente (design, tráfego...); o agente chamado direto SEMPRE comunica ao Diretor o que foi pedido e entregue (diário do projeto), para o Diretor saber de tudo depois (cartão acbb07d9 no projeto Up). Aqui no Claude Code (pasta ECC Repository) continua a regra do CLAUDE.md: o Diretor só entra quando o Anderson pedir pelo nome.
