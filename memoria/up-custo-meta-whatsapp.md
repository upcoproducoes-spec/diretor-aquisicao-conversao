---
name: up-custo-meta-whatsapp
description: "Por que o Up não mostra o custo real da Meta no WhatsApp, onde estão os pagamentos e o que vale para nota"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-13T17:20:16.900Z
---

Custo do WhatsApp no Up (13/11/2026):
- O Up entra no WhatsApp do Pedro como **parceiro** (negócio "Anderson Vieira", controle total); a conta (+55 45 9849-7863, WABA 1519960359943389) é do negócio Pedro Sachet (329214668338518). O app UpLaunch (1402503241511899) JÁ TEM as duas permissões do WhatsApp aprovadas (análise de 28/10/2026); não precisa de nova análise nem vídeo. Mesmo assim a Meta recusa o custo ao parceiro (pricing_analytics com COST → "Application does not have permission"; sem pedir COST vinha custo 0): o custo só aparece para o negócio dono/pagador. **Decisão do Anderson (13/11): NÃO** fazer token/app por cliente (daria trabalho em cada conexão). Fica: estimativa automática para acompanhar + **rotina mensal**: no fim de cada mês, junto com a exportação dos recibos, o Claude lê o Cobrança e pagamentos de cada cliente e lança/atualiza em `meta_payments` (o que já foi cobrado; saldo a cobrar vira cobrado), avisando o Anderson do que foi cobrado e da estimativa. Cuidado no Gerenciador: "Conectar um ID do app" transfere o app; nunca usar para o UpLaunch.
- A estimativa do Up (R$ 0,035 × cobradas) bateu com a Meta: 13/11 pago R$ 85,87 + saldo R$ 43,39 + R$ 5,99 imposto ≈ R$ 118,84 sem imposto vs estimativa R$ 115,96 em 30 dias. Imposto da Meta ≈ 13,8%. Conta em BRL, cartão final 2054.
- Para nota e cobrança vale o que a Meta cobrou: tabela `meta_payments` (migração 0092), cartão "Pagamentos à Meta (valor real)" no Resumo; o dono lança. Lido em business.facebook.com > Cobrança e pagamentos (conta "Pedro Sachet - Anderson Vieira").
- Qualidade do número do Pedro: **Média** em 13/11 — cuidado com Camila e disparos.

**Why:** o Anderson cobra o cliente e emite nota com esse valor; estimativa não serve.
**How to apply:** nunca apresentar a estimativa como valor da Meta; conferir pagamentos no Cobrança e pagamentos; vale também para a Bia ([[vale-para-todos-os-projetos]]).
