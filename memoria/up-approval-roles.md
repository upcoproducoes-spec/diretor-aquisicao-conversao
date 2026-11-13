---
name: up-approval-roles
description: "Quem aprova o quê no Up — expert só conteúdo; criativos só dono e equipe; imagem gerada pelo agente, não por quadro solto"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-29T14:04:35.506Z
---

Regra do usuário (2026-10-14):
- **Conteúdo** (posts, carrosséis, roteiros orgânicos): quem toca é o **expert** (Pedro). Ele conversa com o Criador de conteúdo, define e aprova. O dono só manda ideias e sugestões.
- **Criativos** (imagens e vídeos de anúncio): **só o dono e a equipe** veem e aprovam. O expert não vê a aba, não recebe aviso, não aprova. Já aplicado no código (commit f11b7b3): sem rotas `/v1/client/assets`, `decideAsset` só papel user, aviso e contador escondidos do expert.
- **Geração de imagem** não fica num quadro solto na página Imagens. Ela acontece dentro do fluxo: o agente (Design ou Criador de conteúdo), depois do conteúdo definido, gera; a imagem vai para a biblioteca e entra em Criativos (ou no conteúdo, para o Pedro aprovar, quando for conteúdo).

**Agente de Design construído (29/10/2026, commit d4d8f74, migração 0078_designs):** aba **Peças** (#/pecas, só equipe): peça = receita (formatos, telas com cabeçalho/selo/headline/sub/CTA/rodapé, fundo, foto real, logo, cores, fontes); o painel monta em camadas e exporta PNG no tamanho exato (feed, stories, quadrado, anúncio paisagem, thumb YouTube, 6 peças da Hotmart, carrossel até 10 telas) → Banco de imagens + Criativos. Fundo pela OpenAI sem letras (POST /v1/designs/:id/background), logo com fundo transparente (POST /v1/design/logos), fontes do Google via /fonts no próprio Up. Na Conversa, resposta do Design com bloco ```peca {json}``` vira botão "Montar peça". O conhecimento do Design foi atualizado em docs/agentes/design.md; o dono precisa recarregar o conhecimento recomendado do Design em cada projeto.

**Why:** o usuário achou confuso o quadro "Gerar imagem com IA" e deixou claro que criativo é decisão interna, não do expert.
**How to apply:** em qualquer tela ou fluxo novo, separar conteúdo (expert aprova) de criativo (dono e equipe aprovam); nunca expor criativos ao papel client. Veja [[up-access-model]] e [[up-backlog-and-social-flow]].
