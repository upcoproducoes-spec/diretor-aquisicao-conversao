---
name: feedback-up-tarefas-separadas-e-ajuste
description: "No Up, uma tarefa por peça (post separado de mensagens); ajuste não empilha versão embaixo; post de feed vai para Conteúdo (posts criar) para o Anderson agendar"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fbd7c86b-ed6c-4a5c-a793-88daa6198b6c
  modified: 2026-11-24T01:43:13.470Z
---

Regras do Anderson (23/11/2026) para entregas no Up:
1. **Uma tarefa por peça.** Post do feed (imagem + legenda) é uma coisa; mensagens dos grupos são outra; e-mails, outra. Nunca juntar tudo numa tarefa só.
2. **Ajuste não empilha.** O `revisar` só ANEXA versão nova embaixo, e ele não consegue descartar os itens antigos nem aprovar só o novo. O agente não tem rota para trocar ou apagar item de tarefa. Então, quando houver ajuste: crie uma tarefa NOVA só com a versão atual, completa, e mude o título da antiga com `editar` para começar com "SUBSTITUÍDA, descartar:" (descartar é dele). Use `revisar` só quando ele pedir ajuste pelo próprio Up.
3. **Post de feed/reels/carrossel vai para Conteúdo**, não só para Aprovações: `node up.cjs posts criar <post.json>` com {"title","platforms":["instagram","facebook"],"format":"feed|reels|carousel|story|video","caption","media":[{"ref":"/m/<id>.png","kind":"image","label"}]}. Cria em rascunho, e lá ele aprova e agenda. Tarefa aprovada NÃO vira post sozinha.
4. **Roteiro de live ou vídeo vai inteiro num item só** (mudou em 23/11: o Anderson quer clicar em teleprompter e ver do começo ao fim). Entregue dois itens: "Roteiro inteiro (com slides)" e "Teleprompter (só a fala)", este sem nenhuma marcação ([SLIDE], [VÍDEO], títulos de bloco, [PEDRO CONFIRMA]). O limite de 5.000 caracteres por item foi aumentado por ele no Up em 23/11 (roteiro de 30 mil caracteres entrou). Mensagens continuam uma por horário; notas da equipe, uma por seção.

**Why:** em 23/11, o criativo "É amanhã", a legenda e as mensagens foram numa tarefa só, com as revisões empilhadas embaixo. Ele não conseguiu separar o que aprovar e não achou a imagem para agendar (não estava em Conteúdo).

**How to apply:** em toda entrega no Up, separe por peça; post sempre em Conteúdo (posts criar). Relacionado: [[feedback-aprovacao-up-aviso]], [[feedback-up-salvar-versao-confirm]].
