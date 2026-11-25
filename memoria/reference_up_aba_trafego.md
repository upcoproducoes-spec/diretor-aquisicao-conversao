---
name: reference-up-aba-trafego
description: "Aba Tráfego do Up (leva 1, 24/11/2026): frentes por lançamento/funil, MER, CPA real x alvo, rastreio Hotmart x pixel; comando só leitura node up.cjs trafego"
metadata:
  node_type: memory
  type: reference
  originSessionId: fbd7c86b-ed6c-4a5c-a793-88daa6198b6c
  modified: 2026-11-25T15:07:10.935Z
---

Aba **Tráfego** do Up (leva 1, 24/11/2026), em Canais > Tráfego, só para o dono.

- **Frentes:** cada lançamento ou funil vira uma frente (ex.: Black do Pedro, morfoguide BR, morfoguide ES). Cada uma tem conta de anúncios, texto do nome das campanhas, IDs Hotmart, datas, metas e CPA alvo (valor fixo ou % do ticket).
- **O que mostra:** por janela (hoje, 3 dias, 7 dias, fase), comparado ao período anterior:
  - investimento e faturamento (total da venda na Hotmart, sem reembolsos);
  - resultado, MER e vendas;
  - CPA real x alvo e ticket médio;
  - custo do modelo (por inscrito, ingresso ou início de checkout).

  Mostra também metas, campanhas com venda ligada por src/sck, conferência Hotmart x pixel e alertas.
- **Decisões do Anderson (24/11):**
  - faturamento = total da venda, não a parte da coprodução;
  - **CPA alvo da Black do Pedro: R$ 300**;
  - morfoguide BR e ES: CPA alvo de 25% do ticket, com alerta acima de 30% (em 25/11 o alvo das regras de corte passou a 30% do ticket; ver [[feedback-limite-perda-rotacao]]);
  - presença na live = só o comparecimento do YouTube;
  - **Dash Fácil segue como conferência**.
- **Comandos (só leitura):**
  - `node up.cjs trafego` lista as frentes;
  - `node up.cjs trafego "<nome>" [1|3|7|fase]` gera o relatório.
- **Situação:** em 24/11 `trafego` dava "Erro 500"; em 25/11 já funciona, com as frentes Black, Funil BR e Funil ES. Limite visto em 25/11: a ligação de vendas por src/sck veio 0 em todas as campanhas (o alerta "gasto sem venda" não vale), então a venda por anúncio vem da Dash. A análise diária é publicada com `trafego-analise` pela skill `up-trafego`.
- **Conversão de moeda (25/11):**
  - vendas da Hotmart em outra moeda são convertidas para a moeda da frente (BRL) e entram em vendas, faturamento, ticket, CPA e alvo;
  - fontes, em ordem: PTAX do dia (Banco Central), referência do Banco Central Europeu e, para moedas que os dois não têm (DOP, PEN, CRC, PAB...), a ExchangeRate-API;
  - o relatório traz `totals.converted` (moeda, quantidade, valor original, fonte), e as notas explicam a conversão.
  - **Funil ES:** as vendas chegam em várias moedas latino-americanas, não em dólar. Use os números convertidos do Up para CPA e alvo, e diga no resumo quantas vendas foram convertidas.
- **Limite:** o Up só LÊ o Meta. Ligar, pausar, mudar verba ou excluir continua pelo Gerenciador ou pelo conector na conversa principal, com pedido ou aprovação do Anderson para aquela ação naquele dia.
- **Leva 2 (ainda não feita):**
  - quebra por conjunto e anúncio;
  - fases por prefixo CAP_/CAR_;
  - comparação com o lançamento anterior;
  - visão do expert;
  - comparecimento automático do YouTube.

Relacionado: [[feedback-dashfacil-vs-meta-atribuicao]], [[feedback-gatilho-olhe-campanhas]], [[project-black-morfologic-2026]].
