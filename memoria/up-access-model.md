---
name: up-access-model
description: Regra de acesso do Up — só o dono usa chave; todos os outros entram com e-mail e senha; Claude opera por eles
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-29T13:32:35.792Z
---

**Acessos do dono (15/10/2026, pedido do usuário):** chave de dono = projeto **Up** (painel do dono: tabela `account_hubs`, migração 0056; o Resumo mostra "Todos os projetos" com atividade e custos de cada um, `/v1/hub/overview`). **Correção do usuário no mesmo dia: chave de dono e e-mail dão o MESMO acesso** (os 3 projetos, botão Projetos para trocar; a chave do painel abre a conta por `POST /v1/hub/account-session`, migração 0057; "Trocar senha" com a conta aberta troca a senha da conta). E-mail e senha = login da **conta Anderson** (kind account), abre **Pedro Sachet, Beatriz Vieira e Up** (`account_workspaces`); a chave de dono entra direto no Up; no Resumo de cada projeto aparece "Custos deste projeto" (`/v1/costs`, só papel user). As chaves de dono do Pedro foram revogadas; e-mail de recuperação da chave ("Esqueci minha chave") está no projeto Up. "Trocar minha chave" troca a chave do projeto aberto e some para sessões por senha. Consumo de IA gravado em `ai_usage` (migração 0055) desde 15/10.

No Up, só o dono (Anderson/Upco) usa chave de acesso (acesso irrestrito); agentes e integrações também usam chave. Clientes, experts (ex.: Pedro Sachet) e, no futuro, coprodutores assinantes entram só com e-mail e senha e nunca veem chave. O Claude opera o Up por eles como opera pelo dono.

**Why:** o usuário quer simplicidade para quem não é técnico e planeja vender o Up por assinatura a coprodutores (card em Tarefas > Ideias).

**Separação por cliente (pedido de 28/10/2026):** tudo da Beatriz fica sempre separado do Pedro (e de qualquer outro cliente), inclusive sugestões de tela; nada de nome de cliente fixo no código. Membro da equipe deve poder ser limitado a projetos específicos (ex.: só Beatriz). **Construído em 29/10/2026 (commit 1f40f47, migração 0077_team_accounts):** "conta de equipe" = accounts.owner_account_id (dono que convidou) + login kind account + account_workspaces.role por projeto; Equipe > card "Equipe em vários projetos" (só o dono vê): convidar com projetos marcados e papel, mudar projetos (derruba sessões na hora), reenviar convite, remover. Conta de equipe não cria projeto nem abre o painel do dono; `owner_account_of_key` decide quem é dono (também fechou a brecha em que qualquer "pessoa" do projeto Up abria a conta de dono). Ainda não há limite por área dentro do projeto (só equipe completa ou expert).

**How to apply:** convites sempre por e-mail (Equipe > Convidar por e-mail, link para criar senha); não oferecer nem mostrar chave a cliente/expert; rever no modelo de assinatura se algum assinante precisará de chave para integração. Cliente (role client) só vê Para gravar e Posts; abas previstas: Início, Calendário, Arquivos. Ver [[up-backlog-and-social-flow]] e [[up-operating-model]].
