---
name: link-com-utm-vai-em-botao
description: "Link longo (com UTMs) em mensagem/direct/WhatsApp vai sempre dentro de um botão, nunca solto no texto"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-11-05T15:05:15.958Z
---

Sempre que uma mensagem levar um link longo (com UTMs etc.) — direct do Instagram, regra de comentário, WhatsApp, e-mail —, o link vai dentro de um **botão** (ex.: "Quero minha vaga"), nunca colado solto no texto. Link solto no texto só quando o Anderson avisar que é um link encurtado. **Exceção (05/11/2026):** em mensagem de grupo de WhatsApp, que não tem botão, vai o link do checkout inteiro, sem encurtar (decisão do Anderson para o downsell do morfoguide). **Links curtos (05/11/2026):** link de PÁGINA com UTM em texto solto (grupos, descrição do YouTube) vira link curto no domínio do expert: uma página do Up só de redirecionamento (meta refresh + location.replace) no caminho curto, ex.: pedrosachet.com.br/black-grupos, /black-yt, /venda-grupos, /venda-yt. Checkout da Hotmart não precisa encurtar.

**Why:** pedido do Anderson em 04/11/2026 (ajuste do direct do "comenta BLACK"): link com UTM no texto fica grande e estranho.
**How to apply:** no Up, regra de comentário usa dm_flow com botão tipo link; WhatsApp usa botão de URL/cta_url. A copy aponta para o botão ("toca no botão abaixo"). Veja [[up-domain-and-meta-app]].
