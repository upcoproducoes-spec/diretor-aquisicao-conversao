# sistema: o diretor e o time de agentes

`skills/` e `agents/` são **atalhos** para `C:\Users\User\.claude\skills` e `C:\Users\User\.claude\agents`. O original fica lá porque é de lá que o Claude Code carrega o diretor, os agentes, os revisores e as skills em **qualquer pasta** (Pedro, Bia, rotinas). Editar por aqui é editar o original.

**Nunca apague a pasta `skills/` ou `agents/` daqui nem rode limpeza recursiva nelas**: apagaria o sistema de verdade. Para tirar o atalho, use `Remove-Item` só no atalho (sem -Recurse) ou `cmd /c rmdir`.

O backup no GitHub fica em `C:\Users\User\Documents\diretor-aquisicao-conversao` (`skills/`, `agents/`, `memoria/`, `central/`).
