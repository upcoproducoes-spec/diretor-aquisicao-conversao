---
name: up-migracao-manual
description: "O deploy do Up no Render NÃO aplica migrações; depois do push com migração nova, rodar npm run db:migrate na pasta Up"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-24T20:07:12.314Z
---

O Render só roda `npm ci` e `start:prod`; as migrações de `db/migrations` são aplicadas à mão com `npm run db:migrate` (na pasta Up, usa o DATABASE_ADMIN_URL do .env).

**Why:** em 24/11/2026 a aba Tráfego foi ao ar sem a tabela `traffic_fronts` e o Anderson viu "erro interno" na tela.
**How to apply:** toda entrega com migração nova: push → esperar o deploy → `npm run db:migrate` → abrir a tela no ar antes de avisar que está pronto. Ver [[prompt-de-novidades-do-up]].
