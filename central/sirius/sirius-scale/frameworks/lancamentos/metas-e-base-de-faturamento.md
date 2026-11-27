# Framework — Metas e base de faturamento

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método (financeiro)
> **Base:** 1 cliente (o caso-base, um expert de educação) · 3 lançamentos medidos (L1, L2 e L3)
> · 2 plataformas de venda (Eduzz e Hotmart)
> **Alcance:** **o raciocínio é UNIVERSAL** — três bases de faturamento coexistem em qualquer
> operação que venda com boleto parcelado, e declarar qual base está em uso é higiene, não
> preferência. **Os fatores numéricos são NÃO TESTADO FORA e nem estáveis dentro da própria base**
> (0,68 a 0,82 entre lançamentos do mesmo cliente). Ver a seção final antes de aplicar.
> ⚠️ Este é o framework onde copiar número dá o prejuízo mais direto: um fator errado vira meta
> errada, que vira verba errada.

> **Nível de confiança: VARIAÇÃO ISOLADA.** Extraído de uma medição real (caso-base · L3 ·
> Hotmart), no rebase do simulador de verba do L4. A mecânica que gera o efeito — boleto parcelado
> registrado por parcela — vale pra qualquer produto na Hotmart, mas o **fator numérico** é desta
> operação e deste mix de pagamento. Sobe pra CONSISTENTE quando o mesmo descolamento aparecer em
> outro cliente ou outro lançamento.
>
> Os lançamentos gratuitos do caso-base aparecem como **L1 a L4**, em ordem. Fonte: o briefing e o
> plano de verba da captação do L4 (evidência no caso de origem).

## O problema

Uma meta em reais, sozinha, não quer dizer nada. O mesmo lançamento tem **três faturamentos
diferentes ao mesmo tempo**, e eles não são pequenas variações — o descolamento medido entre o
maior e o menor foi de **19%**.

| Base | O que é | L3 (contratado = 100) |
|---|---|---:|
| **CONTRATADO** | tudo que o aluno se comprometeu a pagar, incluindo parcela futura de boleto | 100 |
| **DASH** | o que o Dash Fácil registra — só a **primeira** parcela de boleto parcelado | 81 |
| **LÍQUIDO** | contratado menos imposto, gateway e reembolso | não medido |

Fator medido: **Dash = 0,8095 × contratado** (L3).

**De onde sai cada base, do lado de vocês:** o que o MCP do Dash Fácil devolve
(`debriefing_lancamento`, `vendas_lancamento`) é a base **DASH**. O **contratado** sai da
plataforma de venda (na Hotmart, pelo MCP dela ou pelo relatório da tela; as armadilhas de leitura
estão em `sirius-scale/frameworks/hotmart/hotmart-api-tecnica.md`). O **líquido** precisa de
imposto, taxa do gateway e reembolso, que nenhuma das duas telas entrega pronto.

**Atualização — o fator foi medido nos três lançamentos, e ele varia muito mais do que se supunha:**

| | L1 | L2 | L3 |
|---|---:|---:|---:|
| **Fator Dash/contratado** | **0,6818** | **0,8151** | **0,8095** |

> **Coluna do L1 refeita — os dois valores anteriores estavam errados.** O contratado antigo não se
> reproduzia em recorte nenhum da plataforma de venda; o medido (paga + em recuperação, todos os
> produtos) ficou ~3% abaixo dele. E o Dash antigo era export velho: o correto, conferido contra a
> tela do Dash em sete indicadores, ficou ~1,7% acima.
>
> Comparando maçã com maçã — só o produto principal dos dois lados (Dash ÷ relatório oficial da
> plataforma de venda) — o fator fica em **0,7167**. Seja 0,68 ou 0,72, a conclusão não muda:
> **o L1 destoa de 10 a 13 pontos dos outros dois, e o fator está longe de ser constante.**
>
> ⚠️ **O L1 rodou na Eduzz e tem inadimplência medida de 17,7%** (do contratado, nunca pago). L2 e
> L3 vieram da Hotmart e não têm esse número apurado — então o fator do L1 não é estritamente
> comparável com os outros dois enquanto a inadimplência deles não for medida.

Com os números de antes da correção, o L1 destoava em 16 pontos percentuais dos outros dois. Isso
confirma a ressalva 1 abaixo com dado, não só com raciocínio: converter o Dash do L1 pelo fator do
L3 (0,8095) daria um contratado **19,5% abaixo do real** — quase um quinto do lançamento sumindo da
conta. Com os números corrigidos o erro fica em ~16%, e a conclusão não muda. Fonte: o simulador de
cenários do L4 e o debriefing comparativo de L1, L2 e L3 (evidência no caso de origem). No L3, o
ticket médio no Dash ficou em 0,81 do ticket contratado.

## A regra

**1. Toda meta declara a base, sempre.** "Meta de X" é ambíguo; "meta de X contratado" não é. Vale
pro briefing, pro simulador, pro painel do cliente e pra qualquer conversa de meta.

**2. Nunca comparar número de bases diferentes sem converter.** Meta em contratado contra realizado
do Dash é comparação errada — e erra pra baixo, o que faz um lançamento bem-sucedido parecer
fracasso no meio do caminho.

**3. Todo derivado herda a base.** Ticket médio, conversão, ROAS e a verba de captação inteira mudam
junto. No L4, o rebase de Dash pra contratado derrubou o alvo em 22,6% sem que uma única premissa de
performance mudasse:

| (índice: base Dash = 100) | Base Dash | Base contratado |
|---|---:|---:|
| Ticket médio | 100 | 129 |
| Vendas necessárias | 100 | 77 |
| Leads necessários | 100 | 77 |
| Verba de captação | 100 | 77 |

> **Nota posterior.** O ticket contratado usado acima saiu do L3 com uma regra antiga de parcelas,
> que multiplicava o NuPay (`sirius-scale/frameworks/hotmart/hotmart-api-tecnica.md` §12: o NuPay vem
> com o valor cheio e não se multiplica). Na regra corrigida, o ticket do L3 cai ~3,8% (todos os
> produtos), o do produto principal sozinho fica ~1% acima do antigo, e o L4 realizado ficou ~0,7%
> abaixo do antigo. A tabela fica como registro da decisão; o próximo simulador parte do corrigido.

**4. Se a meta digitada no painel ficar em base diferente da meta de negócio, registrar o fator no
briefing.** É a decisão que o Rodrigo tomou no L4: manter a meta de negócio (em contratado) literal
no Dash, sabendo que o painel vai marcar ~81% mesmo com a meta batida. Funciona — desde que esteja
escrito, senão vira susto no meio do lançamento ou decisão de verba tomada em cima de leitura
errada.

## Qual base usar pra quê

| Decisão | Base | Por quê |
|---|---|---|
| Meta de faturamento do lançamento | **contratado** | é a receita que a operação de fato contratou; parcela futura é dinheiro real |
| Acompanhamento diário no painel | **Dash** | é o que atualiza em tempo real — convertendo pelo fator |
| Verba, CPL e ROAS do simulador | **contratado** | tem que ser coerente com o ticket médio usado no cálculo |
| Comissão, divisão com parceiro e caixa | **líquido** | imposto e gateway não são receita |

Regra que amarra tudo: **ticket médio e faturamento têm que sair da mesma base.** Ticket contratado
dividindo faturamento do Dash (ou o contrário) é a forma mais fácil de errar a verba inteira de
captação — no L4, só a troca de base mexeu 22,6% no alvo.

### A receita da empresa é outra base

Faturamento do lançamento não é receita da empresa. O resultado da empresa (DRE) registra o que de
fato entra pra ela, por competência (o mês em que o cliente pagou) — e por isso **nunca vai bater**
com a meta do lançamento nem com o Dash. Isso é esperado, não é erro de apuração. Como a casa conta
a própria receita depende do modelo de negócio dela e fica fora deste kit.

## Ressalvas

1. **O fator 0,8095 não é constante.** Ele é o mix de pagamento daquele lançamento — quanto mais
   boleto parcelado, mais o Dash subestima. Recalcular a cada debriefing, não reaproveitar.
   *(11/2026, VARIAÇÃO ISOLADA: o cartão recorrente entra na mesma conta do boleto parcelado. Num carrinho medido o
   Dash registrou só a 1ª parcela das vendas no cartão recorrente; sem boleto no carrinho, o fator ficou perto de 1.
   O Dash também pode contar a mais: venda repetida e venda contestada (`PROTESTED`). Medido casando as vendas do Dash com o
   histórico de vendas da Hotmart pelo `purchase_id`. O contratado do recorrente e do boleto parcelado leva o acréscimo
   do parcelamento: decidam qual valor conta e escrevam no `CLAUDE.md` de vocês.)*
2. **O fator já foi medido três vezes, mas num cliente só** (o caso-base: L1, L2 e L3). A direção é
   confiável e se confirmou nas três medições — o Dash sempre subestima, nunca superestima. O
   **valor**, não: a faixa observada vai de 0,65 a 0,82 (0,68 depois da correção do L1). Nunca
   reaproveitar o fator de um lançamento em outro sem recalcular.
   *(11/2026, VARIAÇÃO ISOLADA: no perpétuo o Dash contou a mais. Ele conta a venda contestada (`PROTESTED`) como
   venda e repete o order bump nos painéis dos outros produtos da mesma conta. O "nunca superestima" vale pro boleto
   parcelado de lançamento; o status de cada venda se confere na Hotmart, pedindo todos os status
   (`prompts-sistema/debriefing-funil.md`, passo 3).)*
3. **O líquido nunca foi medido nesta operação.** Enquanto taxa de reembolso, imposto e gateway
   estiverem vazios no simulador, todo resultado é BRUTO — e isso também precisa estar declarado na
   entrega.
4. Isto não conflita com a regra de que o Dash é a fonte da verdade de **quem** comprou
   (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1). O que este framework diz é que
   ele não é a fonte da verdade de **quanto** foi contratado.

---

## Custo de ferramenta no orçamento do lançamento — *VARIAÇÃO ISOLADA (1 cliente, 3 lançamentos medidos)*

> Registrado no L4, a partir do export completo da carteira da ferramenta de disparo de WhatsApp
> (ManyChat, cobrança via BSP; uma linha por mensagem, cobrindo L1 a L3 e o começo do L4).
> Evidência no caso de origem.

**A regra: custo de disparo entra no orçamento por MEDIÇÃO, nunca por PLANO.**

No L4, a linha de disparo de WhatsApp entrou no simulador pela soma do plano de disparos da
planilha (12 envios). O custo real medido dos três lançamentos anteriores foi:

| Lançamento | **US$/lead** |
|---|---:|
| L1 | 0,0510 |
| L2 | 0,0640 |
| L3 | 0,0390 |

O plano superestimava em **4,8x o custo real do lançamento anterior**, e o erro não era pequeno: a
diferença saía da verba de captação e, no CPL realista do lançamento, custava em faturamento
projetado ~7 vezes o próprio valor do erro.

**Como orçar, na ordem:**

1. **Régua US$/lead**, não total em reais. A faixa medida é **0,039 a 0,064 US$/lead**. Ancorar no
   teto quando o plano tiver muitos disparos em base cheia.
2. **O que move o custo é número de disparo em base cheia, não volume de lead.** O L2 custou mais
   que o L3 com 37% menos lead, porque bateu ~6x na base inteira contra ~3x. Contar os disparos antes
   de aplicar a régua.
3. **Marketing é exceção, não linha de base.** A política medida é: aprovar utility sempre que
   possível, marketing só quando não tem jeito. Marketing custa **9,2x** o utility (US$ 0,0718 x
   US$ 0,0078 por mensagem; tabela da época, conferir no BSP). A trajetória real de marketing como %
   das mensagens: 8,0% (L1) → 3,8% (L2) → 3,5% (L3) → 0,86% (L4, parcial). Qualquer plano acima de
   ~5% de marketing está errado até prova em contrário.
4. **Guardar a linha em dólar.** A cobrança do BSP é em USD; converter só na hora de reportar, com o
   câmbio efetivo da fatura (spread + IOF), nunca com câmbio estimado. Câmbio chutado é número sem
   fonte rastreável com outro nome (`sirius-scale/REGRAS.md` §2).
5. **Conferir o saldo da carteira antes da semana de pico.** Recarga automática tem teto diário; um
   dia de disparo em base cheia pode passar do teto e travar a fila no meio do lançamento.
6. **Assinatura da ferramenta é custo à parte** e sobe em mês de lançamento (ManyChat: ~US$ 90 em
   mês de lançamento contra US$ 25 parado; preço da época, conferir). Vai no resultado da empresa
   como ferramenta; o incremental é atribuível ao lançamento.

⚠️ **Um cliente só, um BSP só (ManyChat).** A régua US$/lead é da operação do caso-base. Ao aplicar
em outro cliente, sinalizar — e refazer a medição, porque tarifa de BSP e número de disparos por
fase mudam por operação.

**Consequência pra comparação histórica:** o "Investimento total" registrado nos debriefings do
caso-base é **só mídia** — não inclui disparo. Somar API no investimento de um lançamento e não nos
outros quebra a série de ROAS. Ou soma em todos, ou em nenhum, e a entrega declara qual base está
usando (mesma lógica da regra 1 deste framework).

---

## O que transfere e o que é do caso

**Transfere pra qualquer cliente/negócio (é raciocínio, não medida):**

- **A distinção das três bases** — CONTRATADO, DASH e LÍQUIDO — e o fato de coexistirem no mesmo
  lançamento. Qualquer operação com boleto parcelado tem isso.
- **A mecânica que gera o descolamento:** o Dash registra só a primeira parcela do boleto parcelado.
  Vale pra qualquer produto na Hotmart, e o mesmo tipo de descolamento aparece em qualquer gateway
  que registre por parcela.
- **A regra de declarar a base** em toda entrega. "Meta de X" sem dizer qual base é número sem
  significado.
- **A regra de série consistente:** ou soma custo de ferramenta em todos os lançamentos, ou em
  nenhum — nunca em alguns. Vale pra qualquer comparação histórica, não só pra ROAS.
- **O hábito de medir em vez de herdar o fator** — que é a lição real deste arquivo (ver abaixo).

**NÃO transfere — e aqui o aviso é mais forte que nos outros arquivos:**

- **Todos os fatores** (0,8095 · 0,8151 · 0,6818 · 0,7167). Eles não são estáveis nem **dentro do
  mesmo cliente**: variaram 13 pontos entre lançamentos do caso-base, por mudança de plataforma
  (Eduzz → Hotmart) e de mix de pagamento. Um fator que não é constante em 3 lançamentos do mesmo
  cliente não tem chance de ser constante em cliente novo.
- **A inadimplência de 17,7%** do L1 (medida na Eduzz) e os valores absolutos de faturamento e
  investimento do caso-base (que nem entram neste kit).
- **A régua de US$/lead de disparo** — é da operação do caso-base, num BSP só (ManyChat). O próprio
  arquivo já manda refazer a medição.
- **A base contratual do caso-base.** O modelo de remuneração muda por negócio: co-produção,
  prestação de serviço e participação societária contam receita de jeitos diferentes. Antes de usar
  este framework, confirme qual base o **contrato** usa — é ela que define a meta, não o costume do
  caso-base.

**Regra de aplicação em cliente novo:** não importe fator nenhum. Meça o primeiro lançamento nas
duas bases (contratado na plataforma de venda, registrado no Dash), declare que a primeira meta usa
fator **não medido** e corrija depois do primeiro debriefing. Herdar 0,81 do caso-base é o erro que
este arquivo existe pra impedir.
