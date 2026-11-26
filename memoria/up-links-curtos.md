---
name: up-links-curtos
description: Links curtos do Up (26/11/2026): redirecionamento 302 no domínio do expert, separado de Páginas, porteiro novo publicado no Pedro e na Bia, 5 páginas do Pedro convertidas
metadata:
  type: project
---

Em 26/11/2026 os links curtos ficaram prontos (Páginas → aba Links curtos; commit 892fa72, migração 0101).
- Cada link: caminho, destino (página do Up, que segue a versão no ar, ou URL), UTMs (utm_*, src, sck), campanha, histórico e cliques por dia.
- O porteiro da Cloudflare responde 302: leva os parâmetros da visita (fbclid; os da visita valem mais) e conta o clique no Up em segundo plano (`POST /l/hit`). Robôs de prévia e HEAD não contam.
- O porteiro novo foi publicado pelo editor da Cloudflare em 26/11:
  - Pedro: Worker `porteiro`, conta do Anderson;
  - Bia: Worker `porteiro-up`, conta do Rodrigo; o cabeçalho de diagnóstico `x-porteiro` dele foi mantido.
  - A API do painel recusa gravar (403); por isso publica-se colando o código no editor e clicando em Implantar.
- As 5 páginas de redirecionamento do Pedro viraram links curtos, no mesmo caminho e com as mesmas UTMs: /venda-grupos, /venda-yt, /venda-chat, /black-grupos e /black-yt. Os 5 cliques de 26/11 foram testes.
- O agente cria ou propõe pelo up.cjs (`links`, `link criar`, `link editar`, `link ver`); o dono aprova.

**Why:** links curtos poluíam a lista de Páginas e não levavam o fbclid.
**How to apply:** link curto novo vai em Links curtos, nunca como página. Ao mudar o porteiro, publicar nos dois Workers (Pedro e Bia). Ver [[bia-paginas-porteiro]] e [[rastreio-sem-gtm]].
