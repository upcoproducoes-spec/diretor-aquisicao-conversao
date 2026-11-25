---
name: periodo-personalizado-sempre
description: "Toda tela do Up com seletor de período (7/30 dias, hoje, fase...) precisa ter também 'Personalizado' com data de / até"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-25T15:29:56.194Z
---

Toda tela do Up que mostra números por período precisa ter, além dos períodos prontos, a opção **Personalizado** (data de / até). Pedido do Anderson em 25/11/2026 ("em todo lugar que tiver esses períodos").

**Why:** ele quer escolher exatamente de quando a quando olhar (ex.: 19 a 25 no Tráfego), não só os atalhos.

**How to apply:** em tela nova com período, use o componente `apps/web/public/js/period-picker.js` (`periodPicker` + `periodQuery`) e, no servidor, `resolveWindow`/`windowFromQuery` de `packages/db/src/date-window.ts` (rota aceita `since` e `until` em AAAA-MM-DD, fuso de São Paulo). Feito em 25/11 no Tráfego, Resumo, Resultados (máx. 30 dias, limite da Meta) e Envios que falharam (commit 008b99b). Ver [[up-aba-trafego-decisoes]].
