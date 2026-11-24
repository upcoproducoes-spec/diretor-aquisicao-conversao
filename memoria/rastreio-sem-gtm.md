---
name: rastreio-sem-gtm
description: "Páginas no Up (Pedro e Bia) não usam GTM; pixel, Dashfácil e UTM→checkout vão direto no HTML, porque o Up não injeta nada"
metadata:
  node_type: memory
  type: feedback
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-24T14:57:26.236Z
---

Decisão do Anderson em 24/11/2026: nenhuma página publicada pelo Up usa GTM ("vamos esquecer o GTM... igual a gente faz com o Pedro"). O rastreio vai no próprio `<head>` da página:
- Pixel da Meta direto. Pedro: 631367086356674. Bia: 663381787741763 (Pixel de Beatriz Vieira) + 823602845323275 (Pixel de Full concept academy), os dois da conta 535326207056162.
- Dashfácil: `df.dfq('init', '<subconta>')`. Pedro 1012, Bia 19.
- Página com checkout: script que leva `utm_*`, `src` e `sck` para os links `pay.hotmart.com` e marca `InitiateCheckout` no clique.
- Lead: no formulário do Up (`data-pixel="Lead"`) ou no obrigado de inscrição.

**Why:** o Up NÃO injeta pixel na publicação. A regra antiga "o Up cuida disso" fez a /black-friday da Bia ir ao ar sem pixel nenhum (achado em 24/11). O GTM da Bia (GTM-PRTJDTX) é do Rodrigo e tinha gatilhos que não batiam com as páginas novas.
**How to apply:** toda página nova ou versão nova no Up: confira se o bloco de rastreio está no HTML antes de enviar. Página importada com GTM: troque pelo bloco "Rastreio do Up". Ver [[bia-paginas-porteiro]] e [[vale-para-todos-os-projetos]].
