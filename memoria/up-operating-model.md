---
name: up-operating-model
description: "Modelo operacional da plataforma Up - Claude opera, o usuário só aprova; multi-cliente com várias contas por cliente"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-03T12:06:01.247Z
---

A plataforma Up (pasta `C:\Users\User\Documents\Claude\Up`, repo privado `upcoproducoes-spec/up`, banco no Neon) é operada por Claude. O usuário conversa com Claude e aprova ações; pode, se quiser, entrar manualmente para ver mensagens, e-mails, caminhos de automação e editar à mão.

**Why:** o objetivo é uma "agência" dirigida pelo diretor de aquisição e pelos agentes, com o usuário só como aprovador.

**How to apply:**
- Toda ação que Claude faz passa pela mesma API que a interface manual, com `audit_log` marcando o ator como agente. Tudo que o agente faz precisa existir também na UI para o usuário conferir e editar.
- Ação com efeito externo (disparo para a base, publicar página, subir campanha, gastar verba) fica pendente até o usuário aprovar; leitura e rascunho não precisam.
- Cada cliente (workspace) terá várias conexões próprias: contas de anúncio, Instagram, e mais de um número de WhatsApp. O modelo de canais precisa suportar N por cliente (hoje `integrations` já permite vários por tipo via `label`).
- O usuário vai lembrando de requisitos aos poucos e quer que Claude diga se algo novo precisa entrar na plataforma.

Ver também [[user-working-style]].
