---
name: user-working-style
description: "Como o usuário quer trabalhar - Claude faz as coisas no navegador em vez de pedir, mas nunca expõe senhas no chat"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-03T12:06:24.171Z
---

O usuário quer que Claude acesse o navegador e execute as tarefas (Neon, Hotmart, GitHub, Meta) em vez de pedir para ele fazer passo a passo.

**Why:** ele disse explicitamente "não fique me pedindo para fazer isso... eu quero que você acesse o navegador e faça". Prefere delegar.

**How to apply:**
- Usar o Chrome dele (extensão) quando a sessão logada for necessária; o navegador embutido do app não tem as sessões dele.
- Para credenciais: copiar do campo com o botão de copiar do site e gravar direto no `.env` via área de transferência, sem imprimir o valor no chat. Foi o método usado com a senha do Neon.
- Pedir confirmação clara antes de ações externas ou de mudar credenciais, mesmo que ele já tenha autorizado em termos gerais.
- O usuário fala em português do Brasil e responde rápido por mensagens curtas.

Ver também [[up-operating-model]].
