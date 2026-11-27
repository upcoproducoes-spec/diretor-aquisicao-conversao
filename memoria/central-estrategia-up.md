---
name: central-estrategia-up
description: Estrategia UP é a sede do sistema (playbook, kit da Sirius, atalhos do diretor/agentes, estruturas como Camila, fontes); projetos guardam só o que é deles
metadata:
  type: project
---

Desde 27/11/2026 `C:\Users\User\Documents\Claude\Estrategia UP` é a sede: playbook/ (estratégia comum), projetos/ (fichas), decisoes.md ("levar para o outro?"), sirius/ (o KIT da Sirius mora aqui: sirius-scale/, sirius-scale-agentes/, checagens/, ADAPTADOR), sistema/ (atalhos para ~/.claude/skills e ~/.claude/agents, que continuam lá porque o Claude Code carrega de lá em qualquer pasta), estruturas/ (Camila a mover do Pedro quando a rodada atual acabar), fontes/ (entrada de livros, aulas, Sirius). Pedro e Bia têm atalhos (junctions) sirius-scale/, sirius-scale-agentes/ e .claude/skills/<checagem> apontando para a central, e cada um tem o próprio sirius-scale-mapa.md e frameworks-da-casa/.

Sirius liberada pelo Anderson para todos os projetos, agentes e GitHub (ele e o Rodrigo constroem juntos). A LICENCA.md do kit ainda tem o texto antigo.

**Why:** o Anderson quer atualizar tudo (diretor, agentes, Sirius) num lugar só e decidir caso a caso o que replicar entre projetos (a Bia tem mais produtos).

**How to apply:** atualização de sistema e estratégia acontece na central; nos projetos só o que é do projeto. Nunca apagar/limpar recursivamente sistema/skills ou sistema/agents (são atalhos para o original). No backup, central/ vai sem sistema/, .claude/ e fontes originais. Relaciona-se com [[vale-para-todos-os-projetos]] e [[camila-recuperacao]].

**Acesso ao Up (27/11/2026):** a central tem up.cjs proprio com UP_ACCOUNT_KEY (chave de conta da conta de dono "Anderson", label "Central de estrategia", criada com create-account --owner-of pedro-sachet --env-file). Comandos: projetos, projeto criar, <slug> rotas, <slug> <METODO> v1/<rota>; entra em cada projeto com chave de sessao de 12 h guardada em .sessoes.json. Acoes de dono so com o "pode" do Anderson na conversa. Os CLIs create-api-key (--env-file) e create-account (--owner-of, --env-file, --env-name) gravam chaves direto no .env de outra pasta (commit 700ee68 do Up). Projeto novo: projeto criar, chaves no .env da pasta nova, Drive (raiz + Anderson clica permitir no Google + PUT v1/google/root).
