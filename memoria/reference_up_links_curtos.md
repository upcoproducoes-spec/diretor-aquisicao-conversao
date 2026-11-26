---
name: reference-up-links-curtos
description: "Links curtos do Up (26/11/2026): ficam em Páginas > Links curtos; comandos node up.cjs links / link criar / link editar / link ver; nunca criar página para redirecionar"
metadata:
  type: reference
---

Desde 26/11/2026 o Up tem **links curtos** próprios, em Páginas → Links curtos. **Nunca crie página só para redirecionar.**

- `node up.cjs links` lista: destino, UTMs, situação e cliques.
- `node up.cjs link criar <link.json>` com `{"nome","caminho","destino":"pagina:black-venda" ou "https://...","utm":{...},"campanha"?,"nota"?}`. Fica esperando o dono aprovar.
- `node up.cjs link editar <linkId> <link.json>` propõe outro destino ou UTMs; o que está no ar só muda quando o dono aprovar.
- `node up.cjs link ver <linkId>` mostra destino, cliques por dia e histórico.
- O link com destino `pagina:` segue a versão publicada da página: mudou a página, o link acompanha.
- As 5 páginas de redirecionamento da Black (/venda-grupos, /venda-yt, /venda-chat, /black-grupos, /black-yt) já viraram links curtos.

Relacionado: [[reference-up-aba-trafego]].
