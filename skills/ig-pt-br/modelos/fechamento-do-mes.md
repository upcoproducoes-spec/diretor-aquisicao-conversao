# Fechamento do mês: <cliente> · <AAAA-MM>

Rodar no 1º dia útil do mês, na conversa principal, com o usuário presente. Duração: ~45 min.

1. **Pesquisa (ig-viral):** 6 a 12 contas (4 diretas, 4 vizinhas, 2 a 4 grandes só de formato). Colete o TSV (conta, seguidores, mediana, views, gancho). `swipe_pt.py ... --out instagram/swipe.md`. Diga a amostra (quantos reels, quantas contas) e que o "gancho" sem login é a primeira linha da legenda.
2. **Auditoria (ig-audit):** preencha `posts.tsv` com os posts do mês (30+ no acumulado dos últimos meses) e rode `auditoria_pt.py posts.tsv --out instagram/auditoria-AAAA-MM.md`. Separe PERFIL (alcance sem seguir) de GANCHO (sem alcance).
3. **Perfil (ig-profile):** só em cliente novo, ou se a auditoria apontar perfil.
4. **Plano:** reescreva `plan.md` com as conclusões (só amostra conclusiva) e as hipóteses do mês, uma mudança por vez.
5. **Casos validados:** passe para `casos-validados.md` só o que se repetiu em 3 ciclos ou em 30+ posts, com data e evidência. O resto fica em hipótese.
6. **Registro:** `log.md` atualizado; se uma regra valeu em mais de um cliente, avise o diretor para promover à skill.

Sempre: nada é postado; sem login por ninguém; número só com fonte.
