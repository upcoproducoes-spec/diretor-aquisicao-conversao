---
name: mensagem-com-quebra-de-linha
description: Directs e WhatsApp do Up devem chegar com as quebras de linha e linhas em branco exatamente como escritas
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-07T12:52:36.862Z
---

O Anderson quer que a mensagem chegue com a mesma formatação em que foi escrita: Enter vira nova linha, linha em branco separa parágrafos, tanto no direct do Instagram/Facebook quanto no WhatsApp ("tudo de uma vez só" é erro).

Corrigido no commit 3f63c1c (renderReply/instagramDirectMessage em packages/db/src/social.ts só juntam espaços na mesma linha).

**Why:** a mensagem do grupo da Black chegou num bloco só no WhatsApp dele (07/11/2026).
**How to apply:** ao escrever textos de automação, DM, modelo ou disparo, quebrar em parágrafos curtos com linha em branco; ao revisar uma mensagem recebida, conferir a formatação. Modelos de WhatsApp aprovados na Meta têm o texto fixo: a quebra precisa estar no corpo enviado para análise. Ver [[whatsapp-utility-e-saudacao]].
