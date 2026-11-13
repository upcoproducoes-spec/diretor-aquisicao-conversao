---
name: up-tag-model
description: "Modelo de tags do Pedro Sachet e regras de automação por produto (compra aprovada tira só o funil do mesmo produto), grafia dos produtos e IDs Hotmart"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-10-05T17:23:06.400Z
---

Grafia dos produtos: **morfoguide** e **morfologic** (nunca "morphoguide"). Há também o Workshop Morfologia de Dentes Posteriores. Em português o morfologic também existe.

Formato das tags: só hífen entre as partes, minúsculas, sem colchetes (o CSV antigo do GoHighLevel vinha como `[morfoguide][br][compra-aprovada]`; o importador agora vira `morfoguide-br-compra-aprovada`). Padrão: `<produto>-<idioma>-<estado>`; lançamentos levam o código na frente (`lc-ago/25-...` clássico, `ls-jun/25-...` semente, `lp-ago/26-...` pago, `lr-fev/26-...` relâmpago; mês em 3 letras e a barra só na data). Tags `hotmart:...` são sempre descartadas (importação e webhook); o Up reage aos eventos da Hotmart.. Estados vistos: inscrito, compra-aprovada, abandono-de-carrinho, pagamento-pendente, lista-de-espera, grupo, gravacao, up1, down1, hibrido, reembolsado.

Regras de automação combinadas (2026-10-05):
- Compra aprovada de um produto remove só as tags de funil **daquele produto e idioma** (abandono de carrinho, pagamento pendente...). Nunca as de outro produto (carrinho abandonado do morfologic fica se ele compra o morfoguide).
- Reembolso ou chargeback: sai a tag de compra, entra `...-reembolsado`.
- "Morfo.Guide +" (combo BR, físico + digital), "Bônus morfo.Guide" e o Morfoguide Híbrido contam como **morfoguide**, sem tag própria de bônus ou combo.
- O passo `remove_tags` (lista e/ou prefixo, com exceções) já existe no motor.

IDs Hotmart (2026-10-05, enviados pelo usuário em captura de tela). Vendas ativas: 7330221 Morfo.Guide + (combo BR: morfo.Guide 5516907 + Bônus 7329799); 7377587 morfo.Guide híbrido + (combo: híbrido 7377456 + modelo anatômico morfo.Guide 5517006); 7143292 morfo.Guide - Spanish; 7283129 morfo.Guide - english; 5339025 morfo.Logic (BR); 7946690 morfo.Logic - Spanish; 8059584 Gravação do Workshop; 6495135 Modelo anatômico morfo.Logic (físico). Vendas suspensas: 7329799 Bônus, 5516907 morfo.Guide (físico), 6387795 morfo.Guide Digital BR (ebook), 7377456 morfo.Guide Híbrido, 8059491 Workshop Morfologia de Dentes Posteriores. Não apareceu morfo.Logic em inglês na captura.
Compra de combo chega como o ID do combo (ex.: 7330221); os componentes aparecem em eventos de área de membros e entrega, não de compra.

Ofertas Hotmart (códigos lidos de capturas de tela em 2026-10-05; conferir antes de usar em regra): 
- 7377587 híbrido +: base R$349 u4gmvjw3; OrderBump - Workshop weu1ex7g; Funil VSL - Downsell 5nr3z3vw.
- 7330221 Morfo.Guide +: base R$497 sto0ti4s; Funil - vsl wctgpqk5.
- 8059584 Gravação do Workshop: base R$249 1zljbm81 (única oferta; não indica o lançamento).
- 5517006 modelo anatômico morfo.Guide: base R$229 zt7nk14r; Vitrine Hotmart Club R$149 i1eapc6r; OrderBump - VSL R$149 f4p854oi.
- 6495135 modelo anatômico morfo.Logic: base R$229 gwi8j5kk; Vitrine Hotmart Club R$149 ia1cvxdl; OrderBump R$149 z15t580p.
- 7283129 morfo.Guide english: US$67 en7igygo. 7143292 morfo.Guide Spanish: US$67 tla1tdkh.
- 5339025 morfo.Logic BR: base R$2.497 5rj3hh1v; HOTMART PARCELADO WORKSHOP R$2.497 wvugm86a; Especial 50% - VSL R$697 9uq22j7w; Especial - VSL R$1.197 j5ad8mb9.
- 7946690 morfo.Logic Spanish: base US$479 xj3zb7fq; Downsell US$164 t3hx6wvo; Upsell US$239,50 xd55m6wb.
O código da oferta chega no evento (campo offer_code do payload); order bump chega como evento de compra próprio com order_bump.is_bump.

Funil de VSL do Pedro (explicado pelo usuário em 2026-10-05): compra do morfoguide BR (Morfo.Guide +, físico+digital) ou do híbrido leva ao upsell do morfologic (R$1.197, oferta "Especial - VSL"); se recusa, ao downsell (R$697, "Especial 50% - VSL"). Quem abandona o carrinho do morfoguide é levado ao downsell do morfoguide, que é o híbrido (R$349, "Funil VSL - Downsell"); se compra o híbrido, recebe de novo o upsell 1.197 do morfologic e, se recusa, o downsell. O morfoguide ES e o morfologic ES funcionam igual (upsell US$239,50 e downsell US$164). O morfoguide inglês não tem funil. As ofertas base e "Hotmart parcelado" (R$2.497) do morfologic BR são vendas diretas (time de vendas). Decisão: não criar tags de origem da venda (direta, upsell, downsell, order bump): o produto comprado basta; o código da oferta fica no evento para relatório.

Importação feita em 2026-10-05: 3.668 contatos do GoHighLevel (3.662 novos) sem as tags `hotmart:*` antigas. Todos entraram como inscritos por e-mail; falta importar a lista de descadastrados/"não perturbar" do GoHighLevel antes de qualquer disparo em massa.

**Why:** o usuário quer tags limpas por produto e funil sem poluição entre produtos.
**How to apply:** ao criar automações, usar esses nomes e IDs; propor ao usuário antes de ativar. Veja [[up-requested-features]] e [[up-drive-pedro-sachet]].

**Black 2026 (21/10/2026, decisão do usuário):** inscrito na Black = `black-nov/26-br-inscrito` (padrão próprio da Black: `black-<mês>/<ano>-<idioma>-<estado>`, sem o nome do produto). Usar o mesmo padrão para as outras tags da Black (ex.: VIP), confirmando o nome com o usuário.
