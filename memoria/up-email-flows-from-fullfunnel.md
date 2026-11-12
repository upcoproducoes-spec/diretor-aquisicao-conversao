---
name: up-email-flows-from-fullfunnel
description: As 4 automações de e-mail do FullFunnel (morfoGuide BR) já replicadas no Up como rascunho desligado; mapa de esperas/tags e pendências para ligar
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-11-12T23:38:30.912Z
---

Em 2026-10-05 o workflow do FullFunnel "morfoGuide - BR | E-MAIL | Boas vindas / Recuperação de carrinho" foi lido nó a nó e replicado no Up como **4 rascunhos desligados** (status `draft`, v2). FullFunnel continua LIGADO.

Gatilho = tag adicionada. Cada uma checa "ainda não comprou" (tem a tag de compra → encerra) antes de cada e-mail de abandono.
- Físico compra: `morfoguide-br-compra-aprovada` → tira `morfoguide-br-abandono-de-carrinho`, e-mail "Parabéns! Sua jornada começou!", espera 5 min, e-mail "preparei mais um presente".
- Híbrido compra: `morfoguide-br-hibrido-compra-aprovada` → tira só `morfoguide-br-hibrido-abandono-de-carrinho` (no FullFunnel tirava a tag do físico; no Up segue a regra "só o funil do mesmo produto").
- Físico abandono (`morfoguide-br-abandono-de-carrinho`, 9 e-mails): esperas 30min (janela 8h-19h), 3h (sem janela), 12h e 24h x6 (janela diária 9h-10h).
- Híbrido abandono (`morfoguide-br-hibrido-abandono-de-carrinho`, 6 e-mails): 30min (janela 8h-19h), 0min com janela seg-sex 19:45-20:15 (NÃO é erro: é "janela de avanço"), 12h com janela 9h-10h, depois 12h sem janela x3.
- ES (criado 2026-10-06, pasta "morfoGuide ES"): compra `morfoguide-es-compra-aprovada` (tira `morfoguide-es-abandono-de-carrinho`, e-mail, 5 min, e-mail 2 com assunto em PORTUGUÊS no FullFunnel); abandono `morfoguide-es-abandono-de-carrinho` com 8 e-mails: 0min janela 8h-19h → e1 (sem verificação antes) → 0min janela 19:45-20:15 → verifica → e2, depois 12h sem janela até o e8 (e7 = cupom PSMF15ES, 15%, de $67 a $56,95, texto fixo).
**Variáveis do projeto (2026-10-06):** o Up tem `{{var.nome}}` nos e-mails (tela "Variáveis"; agente cria, só chave de usuário muda/apaga). ES usa `preco_es` ($67), `preco_es_cupom` ($56,95), `desconto_es_valor` ($10,05), `cupom_es` (PSMF15ES), `cupom_es_percentual` (15%). Os e-mails do BR ainda têm preços fixos (ex.: R$1.238/R$497 no físico e4); migrar para variáveis quando o usuário pedir. Assunto do e-mail 2 da compra ES foi traduzido para espanhol com autorização do usuário.
**Lição:** nas esperas do FullFunnel, rolar o painel até o fim: "Janela de avanço" (dias da semana + faixa de horário) fica abaixo de Período/Unidade. O Up tem `window` no passo wait (fuso America/Sao_Paulo assumido; confirmar com o usuário).
O Up passou a aceitar `{{unsubscribe_link}}` (link assinado; dispensa o rodapé do Up) e `{{year}}`. Imagens dos e-mails ainda apontam para o CDN do FullFunnel (assets.cdn.filesafe.space): mover para o banco de imagens antes de desligar o FullFunnel.
Pré-cabeçalho: o físico já vem escondido no HTML; no híbrido só e2, e3 e e6 foram injetados (e1, e4 e e5 estavam cortados na tela do FullFunnel, ficaram sem).

**12/11/2026: FullFunnel encerrado** (ver [[fullfunnel-encerrado]]). As 6 automações de e-mail do morfoGuide (BR físico/híbrido e ES, boas-vindas e recuperação) estão LIGADAS no Up. Conferido em 12/11: as versões no ar (Pedro e Bia) usam só imagens do Up (app.upcoproducoes.com.br/m/...); os endereços do FullFunnel (assets.cdn.filesafe.space) existem apenas nas versões antigas v1-v3 da "Recuperação de carrinho — Físico", que não são enviadas.

**Why:** os e-mails do híbrido o usuário reescreve depois à mão.
**How to apply:** o mapa acima serve de referência das esperas e tags; não há mais nada a "desligar no FullFunnel". Veja [[up-requested-features]] e [[up-tag-model]].
