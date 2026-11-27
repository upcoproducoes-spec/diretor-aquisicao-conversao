# Hotmart Developers API — notas técnicas (leitura de vendas)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma
> **Alcance:** UNIVERSAL — API da Hotmart, igual pra qualquer produtor e
> qualquer empresa. Sem eixo de força: é fato de API. Credencial e IDs de
> produto é que são por conta/cliente.
> **Fato de plataforma:** endpoint, campo, limite e taxa são os da época da
> medição. A Hotmart muda sem avisar: conferir na doc antes de confiar.

> Documenta a API oficial da Hotmart (developers.hotmart.com), pesquisada
> direto na doc, e o que já foi confirmado rodando de verdade. Igual ao padrão
> dos arquivos técnicos de tráfego (`sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`
> e `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`): tudo aqui é o
> que a doc/API real mostra, não é achismo. O que ainda não foi testado com dado
> real está marcado como tal — atualizar assim que confirmar.

**Como usar do lado de vocês:** pelo MCP oficial da Hotmart, se conectado, ou
pela API com a credencial de vocês (abaixo). Na casa, desta API saem o
relatório de faturamento por lançamento, o comparativo entre janelas de
lançamento e o ritmo de vendas por hora dentro de um dia (`order_date` já vem
com hora: dá pra manter a hora e comparar datas diferentes alinhadas pela 1ª
venda, em vez de só agregar por dia). Os scripts da casa não fazem parte do
kit; o que eles calculam e as armadilhas que corrigem estão nas seções abaixo.
Só leitura — nenhum endpoint de escrita é usado.

## Autenticação

OAuth2 `client_credentials`. Credenciais geradas em `app.hotmart.com` →
Ferramentas → Credenciais Developers → Criar Credencial → escolher ambiente
**produção** (não marcar sandbox). Gera 3 valores, mostrados só uma vez:
`client_id`, `client_secret` e um token `Basic` pronto (já em base64).

```
POST https://api-sec-vlc.hotmart.com/security/oauth/token
  ?grant_type=client_credentials&client_id=:client_id&client_secret=:client_secret
  header: Authorization: Basic :basic_token
```

Retorna `access_token` (`expires_in` ~172799s, ~48h). Só o access_token
expira — client_id/client_secret/basic continuam válidos. Em 401, regerar o
token (não precisa recriar as credenciais).

⚠️ **O token `Basic` da tela já vem com o prefixo `Basic ` incluso.** Montar o
cabeçalho como `Authorization: Basic {token}` acrescenta outro, vira
`Basic Basic …`, e a API responde **401 sem explicar**. Aceitar o valor com ou
sem o prefixo e normalizar antes de montar o cabeçalho. E a credencial de
**API** (Client ID + Secret + Basic, que serve em script e em tarefa agendada)
é separada da de **MCP** (uma chave só, que só vale no chat).

Uma credencial vale pra conta inteira, não por produto: cada lançamento se
distingue pelo `product_id` na query, não pela credencial. A mesma conta é a
que o MCP da Hotmart enxerga.
⚠️ **O papel da conta muda por produto.** Onde ela é **coprodutora**
(`commission_as: COPRODUCER`) e não dona, o endpoint de produtos não lista o
produto (armadilha 13). Onde ela é **produtora** (`PRODUCER`), lista. A casa já
registrou isso errado uma vez (dizia que a conta era coprodutora em todos):
conferir no `commission_as` das vendas, produto a produto, em vez de supor.

## Rate limit

500 chamadas/minuto (leitura+escrita somadas), bem mais folgado que o da
Meta (que é por isso que aqui o cache é conveniência, não sobrevivência).
Estourar o limite responde 429 com `error: too_many_requests`. Headers de
controle vêm na resposta: `RateLimit-Limit`, `RateLimit-Remaining`,
`RateLimit-Reset` (e as versões `X-RateLimit-*-Minute`).

## GET /payments/api/v1/sales/summary

Totais agregados por moeda — `total_items` e `total_value.value` — sem
precisar paginar item por item. Parâmetros principais: `product_id`,
`start_date`/`end_date` (**milissegundos** desde 1970-01-01 UTC, não
segundos), `transaction_status`, `payment_type`, `offer_code`,
`affiliate_name`, `sales_source`.

**Sem informar `transaction` nem `transaction_status`, a API só retorna os
status `APPROVED` e `COMPLETE`** — pra pegar parcela futura/boleto em
aberto/atraso é obrigatório filtrar por `transaction_status` explicitamente.

**Não confirmado ainda (a doc não deixa claro):** se `transaction_status`
aceita múltiplos valores numa chamada só (separado por vírgula, ou repetindo
o query param) ou se é estritamente 1 status por chamada. Enquanto isso não
for testado, fazer **uma chamada por produto x status** — redundante se
múltiplo valor funcionar, mas nunca erra. Barato de qualquer forma, dado
o rate limit de 500/min.

⚠️ **`total_value` aqui é COMISSÃO, não faturamento bruto** — ver a seção de
armadilhas reais mais abaixo.

## GET /payments/api/v1/sales/history

Lista detalhada por transação — mesmos filtros de query do `/summary`, mais
`buyer_name`/`buyer_email`/`transaction` pra busca pontual. Paginado via
`page_token`/`next_page_token` (`max_results` controla o tamanho da página).

Campos relevantes por item (caminho no JSON):
- `purchase.transaction` — código único da transação
- `purchase.status` — o `transaction_status` real dessa transação
- `purchase.order_date` / `purchase.approved_date` — em ms
- `purchase.price.value` + `.currency_code`
- `purchase.payment.type` / `.method` / `.installments_number`
- `purchase.recurrency_number`, `purchase.is_subscription`
- `buyer.name`, `buyer.email`
- `purchase.commission_as` — `PRODUCER`/`COPRODUCER`/`AFFILIATE` (como a
  conta consultada foi comissionada nessa venda)

## `transaction_status` — o que cada valor significa pra faturamento

Valores possíveis (todos): `APPROVED`, `BLOCKED`, `CANCELLED`, `CHARGEBACK`,
`COMPLETE`, `EXPIRED`, `NO_FUNDS`, `OVERDUE`, `PARTIALLY_REFUNDED`,
`PRE_ORDER`, `PRINTED_BILLET`, `PROCESSING_TRANSACTION`, `PROTESTED`,
`REFUNDED`, `STARTED`, `UNDER_ANALISYS`, `WAITING_PAYMENT`.

Agrupamento usado no relatório de faturamento:

| Grupo | Status | Por quê |
|---|---|---|
| Confirmado | `APPROVED`, `COMPLETE` | já é receita certa — é o que o Dash Fácil também reflete |
| A receber | `WAITING_PAYMENT`, `PRINTED_BILLET`, `PRE_ORDER`, `PROCESSING_TRANSACTION`, `UNDER_ANALISYS` | parcela futura ou boleto emitido ainda dentro do prazo — é o valor que o Dash Fácil NÃO mostra e motivou o relatório da casa |
| Em atraso | `OVERDUE` | boleto vencido sem pagamento — inadimplência, tratado separado do "a receber" porque não tem garantia de entrada |
| Fora do faturamento | `CANCELLED`, `CHARGEBACK`, `EXPIRED`, `NO_FUNDS`, `REFUNDED`, `PARTIALLY_REFUNDED`, `PROTESTED`, `BLOCKED`, `STARTED` | nunca virou receita, ou deixou de ser (estorno/contestação) |

`PARTIALLY_REFUNDED` fica de fora do total mesmo tendo recebido uma parte —
simplificação inicial; se aparecer volume relevante desse status num
lançamento real, vale abrir esse valor separado em vez de zerar.

## Armadilhas reais (confirmadas com dado de produção)

As três primeiras foram encontradas rodando contra um lançamento real do
caso-base (dois produtos); as seguintes, nas apurações que vieram depois.
Cada uma produzia um número errado que *parecia* plausível — por isso estão
registradas.

### 1. `/sales/summary` devolve COMISSÃO, não faturamento bruto

A doc diz, literalmente, que o endpoint exibe "os valores de comissões
totalizados por moeda" — é fácil ler `total_value` como faturamento e errar.
Num lançamento real o summary deu bem menos que a soma de `purchase.price.value`
no `/sales/history`: era a fatia de coprodução da conta consultada, não o
faturamento.

**Regra:** faturamento bruto sai SEMPRE de `/sales/history` (e, pela
armadilha 4, do campo `hotmart_fee.base`, não de `purchase.price.value`).
`/sales/summary` serve pra saber quanto a conta consultada de fato recebe —
número útil, mas outro número.

### 2. Boleto/Pix parcelado gera UMA TRANSAÇÃO POR PARCELA

Essa é a causa raiz do debriefing furado. No Hotmart Parcelado (boleto ou
Pix), cada parcela é uma transação separada, com `order_date` na data do
próprio vencimento, `price.value` igual ao valor **daquela parcela** (não da
venda inteira) e `recurrency_number` dizendo qual parcela é (1, 2, 3...).

Ou seja: uma venda 6x feita no mês do lançamento aparece como 1 transação
naquele mês e outras 5 espalhadas pelos cinco meses seguintes. **Filtrar
`order_date` no mês do lançamento pega só a primeira parcela** — é exatamente
por isso que o faturamento do debriefing sai menor que a venda contratada.

**Regra:** pra faturamento de lançamento, contar só transações com
`recurrency_number` em (`None`, `1`) — o nascimento da venda — e multiplicar
`price.value` pelo `installments_number` pra chegar no contratado.
*(Refinada nas armadilhas 4, 8 e 12: o valor é `hotmart_fee.base`, e só
multiplica quando `recurrency_number == 1`.)*

### 3. Cartão de crédito NÃO segue a regra acima

Cartão parcelado vem como **1 transação com o valor cheio**, mesmo em 12x
(a Hotmart antecipa o valor pro produtor). Confirmado num lançamento real: 110
de 111 transações de `CREDIT_CARD` com `recurrency_number = None`, com parcelas
de 1x a 12x e `price.value` já no valor total.

**Multiplicar cartão por `installments_number` infla o faturamento
absurdamente** — foi o erro que deu ~5,6x o faturamento medido na época, numa
primeira tentativa de cálculo.

**Regra:** só multiplicar por parcela quando `payment.type` estiver em
`{BILLET, FINANCED_BILLET, PIX, FINANCED_INSTALLMENT}` **e**
`installments_number > 1`. Cartão entra pelo valor cheio, direto.
*(A regra de multiplicar foi substituída na armadilha 12: o sinal confiável é
`recurrency_number`, não o meio de pagamento. A observação continua valendo:
cartão com `rec = null` vem cheio.)*

### 4. `price.value` INCLUI os juros do parcelamento no cartão

Descoberta no dia seguinte à primeira apuração, e é a armadilha mais cara
das quatro primeiras — ela inflou o faturamento de um lançamento em ~10% antes
de ser pega.

Numa venda parcelada em 12x no cartão, a API devolve (proporção real,
escalada pra uma oferta de 100):

```
price.value      = 124.11   ← o que o comprador paga, COM juros
hotmart_fee.base = 100.00   ← o preço da oferta (bate exato com o Dash)
```

O endpoint `/sales/price/details` confirma a decomposição: `base` + `fee` =
`total` (100,00 + 24,11 = 124,11 na mesma escala). A diferença é juro de
financiamento da Hotmart — **não é receita de nenhum dos coprodutores**.

**Regra:** faturamento = **`hotmart_fee.base`**, com `price.value` só como
fallback se `base` vier ausente. Nunca somar `price.value` direto.

### 5. Comissão de coprodução: a fatia é do LÍQUIDO, não do bruto

Confirmado no `/sales/commissions`: a Hotmart tira 9,9% + R$ 1 por venda, o
Hotmart Club tira uma taxa fixa pequena (R$ 2,49 na época) — valores da época,
conferir na plataforma — e o que sobra é dividido na proporção da coprodução.
Cada lado (uma conta `COPRODUCER`, o expert `PRODUCER`) fica com a fatia do
acordo aplicada ao **líquido**, então a parte dele sobre o bruto sai sempre
**abaixo** da fatia combinada. E a distância muda com o ticket, porque parte da
taxa é fixa: quanto menor o ticket, mais pesa a parte fixa e menor a fração do
bruto que sobra pra dividir.

Fórmula usada no comparativo: `(base - hotmart_fee.total) × a fatia do acordo`.

⚠️ O `total_value` do `/sales/summary` **não serve** pra isso: numa janela
testada ele deu ~16% a menos que a comissão real calculada pela
fórmula — provavelmente porque só conta comissão já liberada, e cartão
parcelado libera aos poucos.

### 6. Parcela futura tem data futura — não filtrar por período do lançamento

Consequência da nº 2: a parcela que ainda vai vencer tem `order_date` no
futuro. Buscar pendências (`PRINTED_BILLET`, `OVERDUE`, etc.) com o filtro de
data do lançamento esconde justamente o que se quer ver. A lista de cobrança
deve ser buscada **sem filtro de data**.

## Números de referência (um lançamento real do caso-base, em proporção)

Servem de sanity check pra futuras mudanças no cálculo. Os valores absolutos
ficam no caso de origem; o que se confere são as relações:

| Métrica | Em relação ao contratado |
|---|---|
| Faturamento contratado (regra corrigida) | **100%** |
| Já entrou (à vista + 1ª parcela) | ~81% |
| Parcelas futuras a vencer | ~19% |
| Comissão de um coprodutor | a fatia do acordo sobre o líquido: sempre abaixo da fatia aplicada ao contratado (armadilha 5) |
| Export do Dash Fácil, mesmo período | ~84% |

⚠️ **As duas correções.** A primeira medição deu ~14% acima do contratado
certo: ~10 pontos vinham de somar `price.value` (com juros de cartão) em vez
de `hotmart_fee.base` (armadilha 4), e ~4 pontos do NuPay multiplicado
(armadilha 12). Documento antigo com número de antes das correções está
desatualizado.

Sobre a diferença contra o Dash (o "já entrou" daqui ficou ~4% abaixo do
export do Dash): os dois medem coisas diferentes e **os dois estão certos**.
O Dash conta dinheiro que ENTROU no mês (incluindo parcela de venda nascida
dois meses antes); este relatório conta venda NASCIDA no mês (incluindo
parcela que só vence cinco meses depois). O Dash também conta transação
`PROTESTED` — num lançamento pago apareceu um comprador contado duas vezes,
uma delas contestada.

### 7. `/sales/history` mistura MOEDAS — somar sem filtrar infla o faturamento

Encontrada apurando as vendas de um segundo cliente. O endpoint devolve venda
internacional na moeda do comprador, sem converter, no mesmo campo. Uma única
venda em peso colombiano veio assim:

```
price.value      = <valor na casa dos milhões>   (COP)
hotmart_fee.base = <o mesmo valor>               (COP)
price.currency_code = "COP"
```

Somada junto com as BRL, essa venda sozinha multiplicou o faturamento de um
produto por ~23x e inflou o total da conta inteira. Passa despercebido porque
o número "parece" plausível num produto de Black Friday.

**Regra:** todo somatório de faturamento filtra
`purchase.price.currency_code == "BRL"` (ou converte explicitamente, o que a
API **não** faz por você). As vendas fora do BRL se contam à parte — no
levantamento do segundo cliente eram 16 de 693 (~2%), então zerá-las não
distorce, mas somá-las cruas destrói o número. O campo
`exchange_rate_currency_payout` aparece em `/sales/commissions` e é o caminho
pra converter, se um dia valer.

⚠️ O mesmo vale pra comissão: `commissions[].commission.currency_code`
também vem na moeda de origem.

### 8. Cartão TAMBÉM pode vir registrado parcela a parcela

Complementa (não substitui) a armadilha 3. Ela continua valendo pro caso
comum — cartão parcelado com `recurrency_number = null` e valor cheio. Mas
existe o outro caso, confirmado no mesmo produto e no mesmo dia:

```
<transação A>  CREDIT_CARD 12x  rec=null  base=<preço cheio>        ← valor cheio (armadilha 3)
<transação B>  CREDIT_CARD 12x  rec=1     base=<~1 doze avos dele>  ← valor da PARCELA
<transação C>  CREDIT_CARD 12x  rec=11    base=<igual à B>          ← parcela 11 da mesma venda
```

Ou seja: **`recurrency_number` é o sinal confiável, não o meio de pagamento.**
Quando `rec` vem preenchido, a Hotmart registrou aquela venda parcela a
parcela, seja qual for o `payment.type`.

**Regra revisada (SUBSTITUÍDA depois — ver armadilha 12):** ~~multiplicar
`base` por `installments_number` quando `recurrency_number == 1` **ou**
`payment.type` em `{BILLET, FINANCED_BILLET, PIX, FINANCED_INSTALLMENT}`~~. O
"ou `payment.type`" multiplicava o NuPay, que vem cheio. **A regra que vale é
só `recurrency_number == 1` com `installments_number > 1`.** Ignorar `rec > 1`
(parcela seguinte de venda já contada).

Medido contra um lançamento do caso-base (dois produtos), usando como
referência o contratado da época (que ainda estava inflado pelo NuPay, ver
armadilha 12):

| Regra | Desvio |
|---|---:|
| Só `payment.type` (armadilha 3) | −0,19% |
| Só `rec == 1` | −3,96% |
| **`rec == 1` OU `payment.type`** | **+0,33%** |

No caso-base a diferença entre as regras é de 0,5% — irrelevante. **Nos
produtos do segundo cliente não é:** lá o cartão-por-parcela aparece com
força, e a regra antiga conta uma parcela (um doze avos da venda) onde a venda
foi de 12 parcelas.

> **Nível de confiança: VARIAÇÃO ISOLADA.** As duas armadilhas (7 e 8) saíram
> de uma apuração só (uma conta Hotmart, 14.624 transações de vários anos). A
> mecânica é de plataforma e deve valer pra qualquer conta. Na casa, todo
> cálculo de faturamento passou a usar uma regra só (só `rec == 1` multiplica)
> e a ler `hotmart_fee.base` em vez de `price.value` (armadilha 4), por decisão
> do Rodrigo. Ver armadilha 12.

---

### 9. `/sales/history` SEM `start_date` devolve só os últimos ~2 meses — calado

*(Medido montando a lista de alunos do programa principal do caso-base pra
exclusão de remarketing. UNIVERSAL — comportamento da API, não do cliente.)*

Chamar `/sales/history` só com `product_id` e `transaction_status` **não devolve
o histórico**: devolve uma janela recente, sem avisar e sem erro.

Medido no programa principal do caso-base:

| chamada | transações |
|---|---:|
| sem `start_date` | **57** (só os 2 últimos meses) |
| `start_date` no 1º de janeiro do ano anterior | **522** |

**9,2x de diferença, e nada na resposta indica que houve corte.** Quem monta
lista de e-mail, público de exclusão ou qualquer consolidado histórico com a
chamada curta produz um resultado errado que parece certo.

**Regra: sempre passar `start_date` e `end_date` explícitos.** Janela larga
funciona — testado até 615 dias numa chamada só.

⚠️ **Mas `start_date` mais antiga respondeu `400 Bad Request`:** no teste,
qualquer data do ano retrasado (em relação à data da consulta). Não é limite
de tamanho de janela (615 dias passa); é a data inicial que a API recusa. Do
1º de janeiro do ano anterior em diante funcionou. Se precisar de dado mais
antigo, quebrar em janelas e testar o limite real antes de confiar (medido uma
vez; conferir, a plataforma muda).

### 10. Filtrar por produto é obrigatório quando a conta tem vários

*(Mesma sessão.)*

No caso-base convivem, na mesma conta:

| produto | é aluno do programa principal? |
|---|---|
| **o programa principal** | **sim** |
| um curso menor | **não** — é o downsell |

Montar público de exclusão de "quem já comprou" sem filtrar o `product_id`
tiraria do remarketing os compradores do **downsell**, que são justamente quem
ainda deve receber anúncio do programa principal. Medido: 20 compradores do
downsell, dos quais só 3 também compraram o programa principal.

O mesmo vale pro pixel: um público de site de "Purchase 180 dias" junta
**qualquer** compra do domínio e não distingue produto. Pra exclusão por
produto, a fonte é a API (ou uma lista de CRM), nunca o evento de pixel.

### 11. Venda feita em outra plataforma não está na Hotmart

No caso-base, um lançamento anterior foi **vendido na Eduzz**, e a API da
Hotmart devolve **zero** transação daquele período pro produto. Consolidado
histórico que consulte só a Hotmart perde esse lançamento inteiro.

⚠️ **E o export da Eduzz não substitui:** 56% dos e-mails vêm **mascarados**
(`nome****@provedor`), inúteis pra casar público na Meta. A fonte que serve é o
**export de vendas do Dash Fácil** daquele lançamento, que traz o e-mail
inteiro.

### 12. NuPay vem com o valor CHEIO e `recurrency_number` vazio — não multiplicar

*(Medido no debriefing de um lançamento do caso-base, 9 transações NuPay da
conta em cerca de quatro meses. UNIVERSAL — mecânica de API, não do cliente.)*

`payment.type = BILLET` com `payment.method = NUPAY` (financiamento do Nubank) chega
como **uma transação com o preço da oferta inteiro**, `recurrency_number = null` e
`installments_number` = nº de parcelas que o comprador paga ao NuPay — exatamente
como cartão (armadilha 3). Três exemplos reais (`price` em proporção da `base`):

```
<transação>  BILLET/NUPAY 12x  rec=null  base=<preço da oferta>  price=~1,24 x base  ← preço da oferta
<transação>  BILLET/NUPAY  4x  rec=null  base=<preço da oferta>  price=~1,09 x base
<transação>  BILLET/NUPAY 12x  rec=null  base=<preço da oferta>  price=~1,24 x base
```

A regra da armadilha 3 ("multiplicar quando `payment.type` está em BILLET/PIX/… e
`installments_number > 1`") **multiplica essas três por 12, 4 e 12**: uma venda vira
doze. Num lançamento, a inflação foi de **~17%** sobre o contratado certo; noutro, de
**~3,9%** (três NuPay de 4x, 3x e 6x). Conferido: todo caso `rec = null` + tipo
parcelado + parcelas > 1 da conta, naqueles quatro meses, era NuPay.

**Regra corrigida: só multiplica por `installments_number` quando `recurrency_number == 1`**
(a venda registrada parcela a parcela — boleto, Pix ou o cartão-por-parcela da armadilha 8).
`rec = null` é sempre valor cheio, seja qual for o `payment.type`. Isso **substitui** a
regra revisada da armadilha 8 ("`rec == 1` OU `payment.type`"): o desvio de +0,33%
medido lá era contra uma referência que já estava inflada pelo NuPay — o desvio real
da regra "só `rec == 1`" (−3,96% na tabela) era a correção, não o erro.

✅ **Na casa, a regra virou fonte única (decisão do Rodrigo).** Uma função só calcula o
contratado, com teste que inclui o caso NuPay real — e a regra antiga falha nele. Todo
relatório, painel e comparativo de faturamento usa essa função. Os números históricos foram
recalculados, e os documentos antigos ganharam nota datada dizendo que estavam na regra
antiga. O simulador de um lançamento que já tinha rodado não foi refeito; o lançamento
seguinte partiu do ticket corrigido.
**Pra vocês:** se calcularem faturamento pela API ou pelo MCP, ponham a regra num lugar só e
confiram com um caso NuPay real (`rec = null`, `BILLET/NUPAY`, parcelas > 1): a regra
errada multiplica, a certa não.

### 13. `/products` só lista o que a conta produz — coprodução não aparece, e a lista vazia não dá erro

*(Conferido ao vivo, pelo MCP e pela credencial da API. UNIVERSAL — mecânica de API.)*

`GET /products/api/v1/products` devolve os produtos **criados na conta**. Produto em
que a conta é só coprodutora **não aparece**: consultado pelo id (`?id=<produto>`),
volta `items: []`, **sem erro**, embora `/sales/history` desse mesmo produto traga
vendas com `commission_as: COPRODUCER`. É a mesma família da armadilha 9: resposta
vazia que parece "não existe".

**Consequência prática:** *o produto novo já foi criado na conta do expert?* **não se
confere pela API da conta coprodutora.** Confere-se na tela da conta dele ou por uma
compra de teste que apareça em `/sales/history`.

### 14. O pixel da Hotmart dispara o InitiateCheckout quando a página de pagamento carrega

*(Fonte: Central de Ajuda da Hotmart, "configurações avançadas do pixel de rastreamento":
o evento sai quando a página de pagamento carrega e não é abandono de carrinho.
Ilustração no pixel do caso-base, 7 dias: 1.909 InitiateCheckout × 240 PaymentGenerated
× 117 Purchase, todos os produtos misturados, o programa principal (ticket alto)
incluso. A proporção é VARIAÇÃO ISOLADA; o mecanismo é da plataforma.)*

"Custo por finalização de compra" no gerenciador, com checkout da Hotmart, é **custo por visita ao
checkout**, não por intenção de pagar. Régua de verba é a **compra** (Purchase), conferida na venda real
da Hotmart. Vale pra low ticket, LPSG com checkout direto, Black e perpétuo. Público de remarketing por
InitiateCheckout = quem abriu o checkout, e a URL chega como `pay.hotmart.com/`, sem separar produto.

**Pixel compartilhado: o checkout de um produto puxa evento do outro** (*VARIAÇÃO ISOLADA*). Dois produtos no mesmo
pixel, um deles com carrinho aberto: os anúncios do outro passaram a contar bem mais InitiateCheckout por pessoa que
clicou no botão da página, e ganharam AddToCart, evento que só a página do primeiro disparava. Lido como gente, o evento fez
parecer que o checkout perdia mais, e não perdia: contando pessoa (clique gravado no Clarity e pedido + abandono na
Hotmart e no Dash), quem chegou pediu e pagou na mesma proporção. Com pixel compartilhado, checkout se mede por pessoa,
nunca pelo evento.

### 15. Inadimplência de boleto e de parcelamento: como medir — *método da casa; a proporção é VARIAÇÃO ISOLADA*

Método que a casa usa pra acompanhar inadimplência por forma de pagamento (e que os frameworks de Black
citam ao decidir boleto e parcelamento: `sirius-scale/frameworks/lancamentos/black-da-casa.md` e
`sirius-scale/frameworks/lancamentos/black-friday.md`):

- **Janela:** parcelas cujo vencimento (`order_date`, que na venda registrada parcela a parcela é a data da
  própria parcela, armadilha 2) caiu nos últimos 60 dias.
- **Taxa** = `OVERDUE` ÷ (`OVERDUE` + `APPROVED`/`COMPLETE`). "A receber" (ainda dentro do prazo) fica fora
  da conta.
- **Dois recortes, não excludentes:** boleto (`BILLET`/`FINANCED_BILLET`) e parcelamento
  (`recurrency_number` ≥ 2, qualquer forma de pagamento).
- **"Recorrência" aqui é parcelamento, não assinatura.** Numa conta que não vende assinatura formal,
  `is_subscription` vem `false` em quase tudo (1.644 de 1.646 transações medidas); o que tem
  `recurrency_number` preenchido é venda parcelada registrada parcela a parcela (armadilhas 2 e 8).
- **Só os produtos do expert que se está medindo** (filtrar `product_id`, armadilha 10).
- **Medido no caso-base:** o parcelamento inadimpliu **~3x mais** que o boleto. Achado que vale acompanhar.

### 16. Compra de teste interna vem como venda comum, e a Hotmart não marca — *VARIAÇÃO ISOLADA*

Compras de teste internas (com cupom de desconto quase total) aparecem no `/sales/history` como venda normal, `COMPLETE` ou
`REFUNDED`, e entram na contagem de vendas, no contratado e no Dash. Não existe campo que diga "teste", e o `tracking`
vem vazio. Antes de contar venda ou taxa de reembolso:
1. Valor abaixo do menor preço real da oferta é suspeito.
2. E-mail do comprador contra o domínio e os e-mails de quem faz teste, dentro do script, sem imprimir o dado.
3. Na dúvida, o e-mail contra as listas de alunos: quem está lá é cliente.

O teste sai da contagem de vendas e da taxa de reembolso: o valor não pesa, a contagem pesa. E `CANCELLED` não é
reembolso: quase sempre é cartão que não passou, com o mesmo comprador tentando de novo minutos antes de a venda
aprovar. `EXPIRED` é Pix ou boleto que venceu sem pagar.

### 17. Reembolso e recompra: o e-mail não diz quem é a pessoa — *VARIAÇÃO ISOLADA; os campos são da plataforma*

No caso medido, o cruzamento pelo e-mail achou bem menos reembolsos com recompra do que o cruzamento pelo CPF. Quem
reembolsa muitas vezes compra de novo em seguida, por outra forma de pagamento, com outro e-mail ou com o nome escrito
de outro jeito. Por transação, a taxa de reembolso sai bem maior que a venda perdida por pessoa. As duas contas estão
certas: a primeira mede pedido de reembolso, a segunda o que saiu do caixa.

Onde está o dado:
1. `/sales/history` traz do comprador só nome, e-mail e `ucode`.
2. CPF e celular vêm de `/sales/users` (`role: BUYER`): `documents`, com `type: "DOCUMENT"` e não `"CPF"` (filtrar
   `"CPF"` não acha nenhum), e `cellphone`. Uma busca paginada por produto e status traz todos, sem chamada por
   transação.
3. A ordem é CPF, e-mail e celular (DDD + 8 últimos dígitos, com ou sem o 55 e o 9). O nome não liga duas compras
   sozinho: homônimo existe, e o nome vem escrito diferente.
4. A API não tem data de reembolso: o `/sales/history` devolve `order_date`, `approved_date` e `warranty_expire_date`.
   Quando o dinheiro voltou pro comprador, só a tela da Hotmart diz.

### 18. Cartão recorrente e boleto parcelado: o valor registrado leva o acréscimo do parcelamento — *VARIAÇÃO ISOLADA*

No cartão parcelado comum, a venda vem numa transação só, com `hotmart_fee.base` igual ao preço da oferta, e o juro do
comprador fica fora. Nas duas formas que a Hotmart registra parcela a parcela, a base de cada parcela já vem acima do
preço dividido pelas parcelas:

| Forma | Por parcela | Base × parcelas |
|---|---|---|
| Cartão recorrente | `base` = `price` | acima do preço, tanto mais quanto mais parcelas |
| Boleto parcelado | `price` acima da `base` | a `base` já fica acima do preço |

A diferença sai do juro do parcelamento do produto: meçam no de vocês antes de usar.

A taxa da Hotmart é calculada sobre a `base`. No boleto, a diferença entre `price` e `base` é o que o comprador paga a
mais e não chega na base. Quem calcula o contratado multiplicando a base pelas parcelas soma esse acréscimo nessas duas
formas. Qual valor conta (o cheio da oferta ou o registrado) é decisão de vocês: declarar na entrega qual foi usado.
