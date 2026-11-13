---
name: up-project-folders
description: "Cada projeto do Up tem pasta própria com CLAUDE.md, up.cjs e .env (chave de agente do projeto); rotinas de 30 min do Criador de conteúdo"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-15T22:21:12.720Z
---

Desde 15/10/2026 o dono conversa com o diretor em pastas por projeto: `C:\Users\User\Documents\Claude\Pedro Sachet` (projeto pedro-sachet) e `...\Full Concepty Academy` (beatriz-vieira). Cada uma tem `CLAUDE.md` (diretor e skills de marketing autorizados, envio automático de entregas, comandos "manda pro Up", "status do Up", "fila"), `up.cjs` (status, fila [conversa], responder, entregar, revisar, tarefas) e `.env` local com UP_API_URL + UP_API_KEY de agente só daquele projeto. `Up Operador` é a versão antiga (lê `..\Up\.env`).

O expert conversa no Up só com o Criador de conteúdo (id `content`); a rotina agendada de 30 min por projeto (`up-conteudo-beatriz` criada pausada; a do Pedro foi barrada pelo modo automático e precisa ser criada com aprovação do usuário) responde a fila e manda entregas + briefing de design para aprovação. Enquanto `auto_reply` do content estiver ligado no projeto, o próprio Up responde na hora e a fila fica vazia.

Regra do usuário (15/10): o Criador de conteúdo **coordena** e aciona todo agente necessário (copy, design, vídeo/edição, estrategista) para estático, carrossel, vídeo, roteiros e ideias; entrega única com texto, roteiro, roteiro de edição e briefing de design. Está nos dois CLAUDE.md e no prompt da rotina.

Decisão do usuário (15/10): **IA em tempo real desligada em tudo** (auto_reply=false em todos os agentes; comentários com `workspace_ai.sdr_realtime=false`, migração 0058, commit 0112b51); a chave OpenAI do projeto fica só para imagens/design. Comentários: rotina de 1 h por projeto (`up-comentarios-pedro`/`-beatriz`; migração 0058 aplicada e publicada em 15/10; as 4 rotinas — conteúdo 30 min e comentários 1 h, Pedro e Beatriz — ligadas) usa `up.cjs comentarios` → `rascunho` (comentário fora da fila: rascunho do dono) ou `sugerir` (na fila do SDR: vai para aprovação).

Pedido do usuário (15/10): rotina **diária** de sugestões de conteúdo para o expert (`up-sugestoes-pedro` 8h, `up-sugestoes-beatriz` 8h10): usa `up.cjs resultados` (insights do Instagram/Facebook) + pesquisa web do nicho, manda 3 a 5 sugestões (Reels, carrossel, estático, com gancho e como fazer) na conversa content; o expert responde o número e a rotina de 30 min desenvolve. Aprovações: aprovar item por item; tarefa sai de Aprovações só com todos os itens aprovados ou "Aprovar tudo" (itens aprovados ficam recolhidos).

Campanhas (15/10, migração 0059, commit 4e9e067): tarefas, disparos e criativos têm `campaign_id`; seletor no topo de Tarefas, Aprovações, Disparos e Criativos (some no projeto Up/painel); `up.cjs entregar` aceita `"campanha"` (cria se não existir) e `up.cjs campanhas` lista. Automações já tinham campo de campanha nas pastas (0020).

"Sair" do WhatsApp (15/10, commit 4d5b90e): mensagem "sair" (sem diferença de maiúscula/acento/pontuação) tira whatsapp_opt_in, grava opt_out "whatsapp:sair", manda confirmação e não dispara automação; disparos e modelos já na fila pulam. Nova inscrição por formulário/checkout reautoriza e registra de novo. O "Responda SAIR" vai só nos modelos que o usuário escolher. Trava contra duplicidade de rotinas: dispensada por ora (tudo roda na máquina do usuário).

**Why:** pedido do usuário: ele usa o Claude Code, o expert usa o Up. **How to apply:** nova pasta de cliente = copiar o modelo e gerar chave de agente com `--write-env` e mover para o `.env` da pasta. Ver [[up-operating-model]] e [[up-chat-agents]].
