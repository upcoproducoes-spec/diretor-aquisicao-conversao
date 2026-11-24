---
name: reference-up-aba-trafego
description: "Aba Tráfego do Up (leva 1, 24/11/2026): frentes por lançamento/funil, MER, CPA real x alvo, rastreio Hotmart x pixel; comando só leitura node up.cjs trafego"
metadata:
  node_type: memory
  type: reference
  originSessionId: fbd7c86b-ed6c-4a5c-a793-88daa6198b6c
  modified: 2026-11-24T20:04:31.792Z
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
  - morfoguide BR e ES: CPA alvo de 25% do ticket, com alerta acima de 30%;
  - presença na live = só o comparecimento do YouTube;
  - **Dash Fácil segue como conferência**.
- **Comandos (só leitura):**
  - `node up.cjs trafego` lista as frentes;
  - `node up.cjs trafego "<nome>" [1|3|7|fase]` gera o relatório.
- **Situação em 24/11:** `trafego` deu "Erro 500" porque ainda faltava conectar o token do Meta e criar as frentes.
- **Limite:** o Up só LÊ o Meta. Ligar, pausar, mudar verba ou excluir continua pelo Gerenciador ou pelo conector na conversa principal, com pedido ou aprovação do Anderson para aquela ação naquele dia.
- **Leva 2 (ainda não feita):**
  - quebra por conjunto e anúncio;
  - fases por prefixo CAP_/CAR_;
  - comparação com o lançamento anterior;
  - visão do expert;
  - comparecimento automático do YouTube.

Relacionado: [[feedback-dashfacil-vs-meta-atribuicao]], [[feedback-gatilho-olhe-campanhas]], [[project-black-morfologic-2026]].
