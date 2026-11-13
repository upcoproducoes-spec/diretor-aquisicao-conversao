---
name: up-webhooks-and-visual-identity
description: "Webhooks de entrada/saída do Up (design e segurança), nova identidade visual do foguete e pedido de integrar o WordPress"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-07T00:02:01.920Z
---

**Identidade visual (out/2026):** paleta tirada do foguete que o usuário mandou: preto azulado, azul elétrico (principal), dourado e laranja de chama (detalhes). O amarelo antigo foi abandonado por "exagerado". Favicon é o foguete (`favicon.ico`, `img/rocket-*.png`); a logo UP continua no menu. A mensagem do pedido do favicon veio cortada ("configure o fav com"); assumi o foguete, o usuário confirmou que funcionou.

**Webhooks (decisão "decida por mim", out/2026):**
- Saída: passo `webhook` do motor só enfileira em `webhook_outbox` (migration 0025); ciclo de 10 s (`sendDueWebhooks`) faz a chamada fora de transação, 5 tentativas (1 min, 5 min, 30 min, 2 h), 4xx não repete. Só https, bloqueia IPs internos (BlockList v4 e v6 separadas: a regra `::ffff:0:0/96` junto com IPv4 bloquearia a internet toda), fixa o IP depois de resolver o DNS, não segue redirecionamento. Segredos ficam em Variáveis (`{{var.nome}}` só nos cabeçalhos, resolvido no envio, nunca gravado na fila).
- Entrada: `POST /webhooks/custom/:token` com segredo em `X-Up-Secret` ou `Authorization: Bearer`; vira evento `webhook.<nome>` que dispara automações; endereço criado/trocado só com chave de usuário (`/v1/webhook-in`), segredo aparece uma vez.
- Painel: botão "Webhooks" e "+ Nova automação" na lista de Automações; módulos no menu "Adicionar módulo".

**Pergunta do usuário:** quer manter o site no WordPress e integrar com o Up. Caminho: formulários do WP (Elementor, CF7, WPForms) e WooCommerce mandam webhook para "Receber webhook"; Up avisa o WP com "Enviar webhook"; formulários públicos do Up podem ser incorporados. **Why:** ainda não conectado; falta saber qual plugin de formulário o site usa. **How to apply:** perguntar o plugin e montar o primeiro fluxo junto com o usuário, usando o endereço de entrada.

Relacionado: [[up-domain-and-meta-app]], [[up-operating-model]].
