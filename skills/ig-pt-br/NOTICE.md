# Aviso de autoria e licença

Esta camada em português é **derivada** do pacote **instagram-agent-skill**, de Jake Schincariol, licença **MIT**: https://github.com/Jakeschincariol/instagram-agent-skill

Copyright (c) 2026 Jake Schincariol (pacote original). O texto completo da licença MIT está em `docs/licencas/instagram-agent-skill-MIT.txt`, no repositório do diretor, e se aplica ao código e aos dados originais dos quais esta camada deriva.

## O que é derivado e o que é novo
- **Derivados (reimplementados em português a partir do original):** `hookscore_pt.py`, `swipe_pt.py`, `detect_pt.py`, `hooks.pt.json` (as 26 fórmulas adaptadas), e as seções `invisible` e `typographic` de `slop.pt.json` (copiadas).
- **Camadas finas que importam o original em tempo de execução (o original não é copiado nem alterado):** `humanize_pt.py`, `caption_pt.py`, `beats_pt.py`.
- **Novos desta camada:** `ptlib.py`, o léxico em português de `slop.pt.json` (frases, palavras, estruturas), a fórmula local de id 27, `testes/`.

Os arquivos do pacote original (`ig-*`) ficam **sem nenhuma alteração**, para poderem ser atualizados a partir do repositório de origem.
