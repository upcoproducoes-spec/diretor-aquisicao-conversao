# Capítulo 113: Lost Chapters — O Problema do Cliente Caro: CFA, CAC, LTGP e Payback
*(Fonte: $100M Lost Chapters, Alex Hormozi — Seção B "The Expensive Customer Problem": "Customer Financed Acquisition", "The Three Levers of CFA", "Know The Levers", "CAC", "LTGP", "Payback Period" e "Levels of Customer Financed Acquisition")*

## Core Idea
Clientes custam dinheiro; quem recupera esse dinheiro mais rápido adquire clientes mais rápido, e quem consegue gastar mais que o concorrente para adquirir um cliente ganha o leilão de atenção. O capítulo (cortado do $100M Money Models por ser "conceitual") formaliza a matemática por trás da engenharia de oferta: **Customer Financed Acquisition (CFA — aquisição financiada pelo cliente)**, em que o lucro bruto de 30 dias de um cliente supera o custo de adquiri-lo. O ganho prático para a Fase 7: uma oferta não é boa só por converter; é boa se seu **modelo de pagamento** faz o cliente financiar o crescimento. Aqui estão as três métricas e os três níveis.

## Frameworks Introduzidos
- **CFA (Customer Financed Acquisition)**: condição **30 dias de Lucro Bruto (GP) > CAC**; o mínimo "de vida real" do autor é **30D GP > 2x CAC**, caso em que cada cliente financia dois novos e só o primeiro precisa ser pago do próprio bolso. A janela de 30 dias vem do financiamento sem juros que um cartão de crédito dá: o saldo gasto em anúncios é quitado com o lucro bruto dos clientes adquiridos antes do vencimento; o limite de crédito vira o orçamento de anúncios.
- **As três alavancas da CFA**: (1) **↓ CAC** (custo de adquirir cliente); (2) **↑ LTGP** (lucro bruto durante a vida do cliente); (3) **↓ PPD** (período de payback). Lógica: crescer é ter mais clientes ou torná-los mais valiosos, e a velocidade importa tanto quanto os dois.
- **CAC (Cost to Acquire a Customer)**: soma de anúncios, folha de mídia/criativo/vendas, software e comissões, dividida pelo número de novos clientes. Exemplos: outbound (US$3.000 de emailer + US$200 de software + US$800 de comissões = US$4.000 / 8 clientes = US$500); conteúdo (US$10.000 de equipe + US$1.000 de comissão / 10 = US$1.100); anúncios pagos (US$4.000 + US$20.000 + US$1.000 + US$10.000 / 10 = US$3.500). Ação: calcular o CAC real **por canal**; erro comum: contar só o gasto em anúncios ou considerar o conteúdo "grátis". Uma diferença de US$200 para US$500 por venda pode separar negócios de ordens de grandeza diferentes.
- **LTGP (Lifetime Gross Profit)**: lucro bruto × número médio de transações; ou, em recorrência, **lucro bruto mensal ÷ churn**. Exemplos: produto (US$80 de lucro bruto × 4 transações = US$360); serviço (US$2.400 / 5% de churn = US$48.000). **Churn** = clientes que saíram ÷ clientes no início do período (novos clientes não alteram o churn). Estime sempre: dados de CRM costumam ser imprecisos e o número de transações cresce com a idade do negócio. Sintetizando: "LTGP é a corrida armamentista dos negócios" — o CAC só pode ir a zero, o LTGP pode crescer sem limite; segundo o autor, é mais fácil tornar a publicidade mais eficiente do que fazer as pessoas ficarem mais tempo. CAC é sobre conseguir clientes; LTGP, sobre mantê-los.
- **Payback Period (PPD)**: tempo para o lucro bruto de um novo cliente superar o CAC. Exemplo: US$50 de lucro bruto/mês e CAC US$100 → payback 31 dias. Dobrar o dinheiro em 1 mês vs. em 3 meses significa crescer 4x mais rápido. **30D Cash**: o lucro bruto que se extrai de um novo cliente nos primeiros 30 dias — "métrica mais valiosa" do autor.
- **Os três níveis da CFA**: **Nível 1** — o GP de 30 dias é menor que o CAC (você precisa de poupança, empréstimos ou linhas de crédito; arriscado); **Nível 2** — GP de 30 dias igual ao CAC (você usa o crédito do cartão como capital de giro; o limite do cartão limita a aquisição); **Nível 3** — GP de 30 dias maior que o dobro do CAC (você pode dobrar o negócio por mês e o dinheiro deixa de ser um problema). Simulação do autor: a 2x CAC, de 1 cliente a 4.095 em 12 meses, pagando só o primeiro (limite: algo mais cedo ou mais tarde vira gargalo, como operação — o objetivo é que o gargalo não seja caixa).
- **Exemplo normal vs. maravilhoso (limonada)**: CAC US$20 e payback de 2 meses = crescimento lento e dependente de capital; CAC US$1 e payback de 7 dias = reinvestimento imediato do lucro, crescimento exponencial com apenas US$1 do próprio bolso.

## Key Concepts
- **Dinheiro hoje vale mais que amanhã**: velocidade de recuperação compõe.
- **Back end informa front end**: quanto mais se ganha por cliente, mais se pode gastar para adquirir.
- **Alternativas ao CFA**: empréstimos e investidores servem no momento certo; entrar cedo demais cobra um preço depois.
- **Ressalvas do próprio autor**: os números de crescimento (de US$60 mil a US$1,7 milhão por mês em seis meses etc.) são relatos do autor; a simulação do nível 3 ignora churn, capacidade de entrega e saturação do mercado.

## Mental Models
- Use "CAC real por canal, LTGP por coorte, 30D cash" como três números de painel da oferta; decida a oferta de entrada olhando para eles, não só para a conversão.
- Use o teste "30D GP ≥ 2x CAC?" ao desenhar front-end + upsell + order bump em funil perpétuo: some a margem bruta do front-end e dos upsells de checkout/OTO nos 30 primeiros dias, descontando reembolsos.
- Use a lógica do cartão: se a plataforma de anúncios é paga imediatamente (cartão), o ciclo de caixa é a variável crítica; maximize receita nos primeiros dias (OTOs, order bumps, parcelamento com antecipação), com cuidado com taxas e reembolsos.
- Para infoprodutos: lucro bruto = receita líquida de taxas, impostos, comissão de afiliados/gateway e custo de entrega/suporte — e não o preço de tabela.

## Anti-patterns
- Medir CAC só pelo gasto em anúncios.
- Usar receita em vez de lucro bruto no LTV.
- Contar novos clientes na conta do churn.
- Escalar anúncios no nível 1 sem capital de giro.
- Ignorar reembolsos, chargebacks e taxas no cálculo do GP de 30 dias.
- Supor que a simulação exponencial vale sem gargalos (suporte, capacidade, saturação da audiência).
- Financiar o crescimento com dívida de alto risco pessoal sem entender o impacto de um erro de cálculo; o próprio autor descreve o nível 1 como perigoso.

## Key Takeaways
1. A meta é 30D GP ≥ 2x CAC; mínimo 30D GP > CAC.
2. CAC real inclui toda a folha e o software de aquisição, por canal.
3. LTGP = GP × transações (ou GP ÷ churn); churn é medido sobre a base original.
4. Payback curto multiplica a velocidade de crescimento.
5. Nível 3 elimina o caixa como gargalo; o novo gargalo será a operação.

## Connects To
- **Ch 97 (Commodity e matemática da oferta)**: as definições iniciais de gross profit e LTV.
- **Ch 114 (Value Grid e Offer Stacking)**: como empilhar ofertas para elevar o 30D cash.
- **Ch 99-100 (Preço e Equação de Valor)**: preço e valor determinam o GP.
- **Ch 54 (O Volante, Collins)**: a CFA é o volante econômico da aquisição.
- **Skill `marketing-digital-growth`, ch54 (Run Paid Ads — LTGP:CAC e Client Financed Acquisition) e ch59 (Money Model e Regra dos 30 Dias)**: versão principal do mesmo conceito nos capítulos de $100M Leads e Money Models; este capítulo traz a matemática expandida e os níveis. Também (Hacking Growth — LTV/CAC/ARPU) e **`estrategia-trafego-funil`** (custo por finalização/ticket médio): as mesmas métricas no contexto de funil; compare as definições antes de aplicá-las.
