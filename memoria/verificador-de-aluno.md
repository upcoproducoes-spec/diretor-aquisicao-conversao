---
name: verificador-de-aluno
description: "Verificador 'Sou aluno' das páginas do Pedro: o Up responde aluno=true se o e-mail tem tag terminada em -compra-aprovada; histórico Hotmart completado em 24/11/2026"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-25T01:04:45.454Z
---

O botão "Sou aluno" da página da Black do Pedro chama `POST /public/students/pedro-sachet/check` (apps/api/src/public-forms.ts). Passa quem tem qualquer tag terminada em `-compra-aprovada` (só no projeto com `workspaces.student_check` ligado; limite de 10 consultas por IP a cada 10 min).

Em 24/11/2026 a conferência contra a Hotmart (vendas concluídas e aprovadas desde 2025; a conta do Anderson é coprodutora e só mostra as vendas do Pedro a partir de 2025) achou 61 de 711 compradores sem a tag. Todos eram de antes de 04/10/2026, quando o webhook começou. Foram completados direto no banco, sem evento (sem disparar automação): 44 contatos novos com `source = 'hotmart-historico'` e 63 tags de compra do produto certo (tag nova: `workshop-posteriores-br-compra-aprovada`). Depois disso, 0 ficaram fora. Do webhook em diante, todo comprador sem reembolso passa.

**Why:** o Anderson pediu para garantir que todo aluno da Hotmart passe no verificador durante a condição de aluno da Black.
**How to apply:** se aparecer aluno reclamando, conferir se a compra é anterior a 2025 (depende da importação do GoHighLevel, ver [[up-tag-model]]) ou se é de um produto que não é do Pedro (a mesma conta Hotmart tem Botox 360, Microbotox e outros). Para desfazer o completamento: contatos com `source = 'hotmart-historico'`.
