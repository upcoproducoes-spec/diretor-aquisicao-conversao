---
name: feedback-limite-perda-rotacao
description: "Regras de corte do perpétuo (BR e ES), aprovadas pelo Anderson em 13/11/2026: por criativo 1× e 1,5× o CPA alvo, por campanha 2× o alvo desde a última venda paga (trocar o lote, não pausar)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 00a9b8ee-5065-46a6-b0dc-a3ff43114298
  modified: 2026-11-13T19:22:46.562Z
---

Regras aprovadas pelo Anderson em 13/11/2026.
**Atualização 25/11/2026 (Anderson): o CPA alvo passa a ser 30% do ticket** (o mesmo número que o Up mostra como "limite" na frente; no Up a frente ainda está com alvo 25% e limite 30%, o Anderson ajusta lá). Em 25/11: BR R$ 149,59 (cortes 150 / 224 por criativo, 299 por campanha) e ES R$ 103,07 (103 / 155 / 206). Substitui os alvos fixos abaixo (R$ 235 BR e R$ 150 ES, e os de dezembro e janeiro): o alvo acompanha o ticket do Up. As regras (1×, 1,5×, 2×) continuam as mesmas.

**Tolerância para criativo com potencial (Anderson, 25/11/2026):** o alvo é 30% do ticket (~R$ 150 no BR), mas um criativo que **já vende** e mostra potencial de virar vencedor pode rodar com CPA de até **R$ 250** (Dash, 7 dias) antes de ser pausado. Sinais de potencial: vendas recentes, custo por checkout bom, gancho e CTR que seguram, tendência de 3 dias melhor que a de 7. Acima de R$ 250, ou sem sinal de potencial, vale o corte normal. A tolerância não vale para criativo sem venda: esse segue as regras de 1× e 1,5×. Origem: em 25/11 a rotina sugeriu pausar o ADV01 (CPA ~R$ 200 a 238); o Anderson aceitou e depois mandou cancelar.
 Elas substituem os limites antigos de R$ 620 (BR) e R$ 710 (ES), que valiam por campanha e foram considerados altos demais. Todo gasto é o da Dash Fácil (com imposto) e toda venda é venda paga confirmada na Dash.

**Por criativo:**
- Desligar se gastar **1× o CPA alvo** sem venda **e** com custo por checkout acima de R$ 25.
- Desligar se gastar **1,5× o CPA alvo** sem venda, mesmo com checkouts bons.
- Trocar se o Meta não entregar: menos de ~R$ 10 em 3 dias. Exceção: o ADV07, que vende com pouca verba.

**Por campanha:** se gastar **2× o CPA alvo** desde a última venda paga, **trocar o lote**. Isso significa desligar os criativos da rodada que gastaram sem vender e ligar outros 2 ou 3, nesta ordem de preferência:
1. Os que já tiveram venda real na Dash.
2. Os de melhor custo por checkout.
3. Os que ficaram sem verba.

Mantém a campanha ligada (não pausar), para não reiniciar o aprendizado do conjunto.

**Valores em novembro/2026:**
- BR: alvo R$ 235 → 235 / 350 por criativo, R$ 470 por campanha.
- ES: alvo R$ 150 (150 / 225 / 300), confirmado pelo Anderson em 13/11. O ES também tem cupom de 25%, e o ticket cai de ~R$ 380 para ~R$ 285. Os R$ 200 aprovados antes eram com o preço cheio.
- Dezembro (cupom de 20%): BR alvo ~R$ 250 (250 / 375 / 500); ES ~R$ 160 (160 / 240 / 320).
- Janeiro em diante (sem cupom): BR alvo R$ 310 (310 / 465 / 620); ES R$ 200 (200 / 300 / 400). Em janeiro, revisar com o CPA real: se estiver abaixo do alvo, baixar o alvo, porque o Anderson quer o CPA cada vez menor.
- Orçamento não segue esses valores: ES continua em R$ 50/dia, e só sobe +20% por vez pela regra do Thiago.

**Antes de julgar:** respeitar a janela de 3 a 5 dias ([[feedback-janela-teste-criativo]]) e um gasto mínimo de ~R$ 50 por criativo.

**Why:** o limite antigo deixava um criativo ruim gastar quase 3× o alvo antes de sair. A lógica do ads-meta-gestao é dar ao criativo gasto suficiente para ser julgado, mas não além do que a venda paga. O Anderson quer baixar o CPA cada vez mais.

**How to apply:**
- Em toda análise, mostrar o gasto de cada criativo sem venda contra 1× e 1,5× o alvo, e o gasto da campanha desde a última venda paga contra 2× o alvo.
- Pedir OK antes de executar qualquer troca.
- Escala segue a regra do Thiago ([[project-regra-graduacao-escala-atual]]).
- A Black (captação) tem regra própria, por custo por inscrito.
- Relacionados: [[project-cupom-perpetuo-nov-dez]], [[feedback-dashfacil-vs-meta-atribuicao]].
