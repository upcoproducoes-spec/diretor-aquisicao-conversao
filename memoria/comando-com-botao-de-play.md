---
name: comando-com-botao-de-play
description: Comando que o Anderson precisa rodar vem sempre em UMA linha num bloco powershell, para aparecer o botao de play
metadata:
  type: feedback
---

Quando o Anderson precisar rodar algo (permissoes, configuracoes, instalacao), entregar o comando pronto em um bloco powershell de uma linha so, sem quebra de linha nem here-string, um bloco por comando.

**Why:** pedido de 27/11/2026: ele quer so clicar no botao de play que o app mostra ao lado do comando; bloco de varias linhas nao ganha o botao.

**How to apply:** juntar o comando numa linha (JSON compacto, ; entre partes); se forem varios passos, um bloco por passo, na ordem. Decisoes de permissao sao dele: preparar o comando e ele clica.
