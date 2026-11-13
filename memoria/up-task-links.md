---
name: up-task-links
description: "Tarefa do Up que pede um item (automação, regra, post, disparo, página, criativo) nasce com links para o quadro andar sozinho"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-06T15:59:52.503Z
---

Toda tarefa criada no Up que pede ação sobre um item do próprio Up (ligar automação ou regra de comentário, publicar post, enviar disparo, publicar página, aprovar criativo) vai com `links: [{kind, id}]` no POST/PUT /v1/tasks (kinds: automation, comment_rule, post, broadcast, page, asset; e wa_template com id = nome do modelo, desde o commit 50839f8: análise da Meta vira aviso na caixinha, aprovados → Entregue, recusa → Em execução). Existe desde o commit cbbba2c (06/11/2026, migração 0084).

**Why:** o Anderson ligou as regras de comentário BLACK e a tarefa não andou no quadro; ele quer que a caixinha se mova sozinha conforme a coisa acontece e que o clique abra direto o lugar de fazer.

**How to apply:** ao criar a tarefa, primeiro crie o item (ou pegue o id) e passe o vínculo. Sem vínculo, a tarefa só anda à mão. Relacionado: [[up-approval-roles]], [[up-backlog-and-social-flow]].
