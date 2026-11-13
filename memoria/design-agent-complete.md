---
name: design-agent-complete
description: "Agente de Design completo (aqui e no Up) — skill agente-design, revisor-design, briefing obrigatório, Pacote do Copy, atualização via GitHub só a pedido"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-29T14:40:23.145Z
---

O usuário quer UM agente de Design 100% completo: web (sites, páginas do Up), criativos, conteúdo, YouTube, Hotmart, logo/identidade e apresentações. Ele sempre usa as skills de design instaladas, revisa antes de entregar e **pede o que falta** do briefing antes de produzir. Texto que vem do Copy (ou do Criador de conteúdo) chega no "Pacote para o Design"; incompleto volta com a lista do que falta.

Montado em 29/10/2026:
- Aqui: skill `~/.claude/skills/agente-design` (5 etapas: briefing → design read → produção pela skill certa → revisão → entrega; referências: briefing-por-tipo, pacote-copy-para-design, roteamento-skills, revisao, atualizacao) e subagente `~/.claude/agents/revisor-design.md` (só leitura).
- No Up (commit c44801a): docs/agentes/design.md (escopo completo, briefing obrigatório, método), copywriter.md e criador-de-conteudo.md (Pacote para o Design). O dono recarrega o "conhecimento recomendado" de cada agente em cada projeto.

Geração de imagem é **nativa do agente** (pedido do usuário: funcionar igual aqui e no Up, inclusive para clientes fora do Up, ex.: Ana Paula, design de interiores): script `~/.claude/skills/agente-design/scripts/gerar-imagem.mjs` (gpt-image-1, --ref para estilizar foto real, --transparent para logo), chave em `C:\Users\User\.claude\openai.env` colada pelo usuário (nunca no chat, nunca impressa). No Up, a geração usa a chave do projeto (Integrações > IA).

**Why:** o usuário quer o agente sempre no nível mais alto e sem trabalhar com briefing pela metade.
**How to apply:** em pedido de design, carregar a skill agente-design. Atualizar skills/agentes (GitHub público, sem acesso necessário) só quando ele pedir, propor antes de instalar, sem rotina agendada. Veja [[up-approval-roles]] e [[up-chat-agents]].
