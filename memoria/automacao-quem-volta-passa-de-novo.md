---
name: automacao-quem-volta-passa-de-novo
description: "Automações do Up rodam de novo para quem volta (inscrição repetida, compra repetida); \"uma vez só\" só quando marcado"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-07T12:13:54.698Z
---

Regra do Anderson (07/11/2026): quem se inscreve de novo ou compra de novo recebe de novo as boas-vindas e a mensagem de compra aprovada ("se eu me inscrever 15 vezes na Black, as 15 vezes eu tenho que receber"). Nunca montar automação de boas-vindas ou de compra como "uma vez por contato".

Feito no commit 1d372c7 (migração 0085): padrão de reentrada "always"; tags_on_complete do formulário e o passo add_tag reaplicam a tag (tag.added com again: true). Tags de engajamento (email:abriu) e de origem não repetem.

**Why:** o teste de inscrição dele não disparou porque o contato já tinha a tag de um teste anterior.
**How to apply:** ao criar automação, não marcar reentry "once" salvo pedido explícito; ao diagnosticar "não recebi", conferir primeiro se a tag já existia e se o 1d372c7 já está no ar. Ver [[up-task-links]].
