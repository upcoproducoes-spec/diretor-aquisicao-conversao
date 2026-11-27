# Framework — Produto de entrada (o que qualifica e o que só enche lista)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método (arquitetura de funil)
> **Alcance:** **NÃO TESTADO FORA** — base de 1 cliente (outro expert da casa, com
> perpétuo de livro digital), 1 ano, primeira vez que os dois formatos rodaram
> lado a lado.
> **Força:** **VARIAÇÃO ISOLADA.** Não promover a regra geral sem um segundo
> caso. Ver a seção "o que transfere e o que é do caso".
>
> ⚠️ **Números do livro corrigidos** depois do debriefing do perpétuo, que já
> tinha corrigido a fonte: compradores **151** (líquido de reembolso, não 156),
> subida **11,3%** (17 de 151, não 10,9%) e valor por comprador **cerca de 16%
> menor** que na primeira conta (a base antiga era anterior à correção da
> armadilha do NuPay, `sirius-scale/frameworks/hotmart/hotmart-api-tecnica.md`
> §12, e incluía vendas reembolsadas). A "subida" do livro é quase toda **oferta
> de um clique**: na recontagem por oferta
> (`sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.15, conferida
> de novo no mesmo dia sobre o export de vendas), 11 no upsell e 5 no downsell,
> 14 dessas 16 em até 35 minutos, e **1 no curso cheio**, cerca de 87 h depois.
> A fonte corrigida mantém a conclusão: o livro qualifica e o ingresso não.

## O achado

Dois produtos de entrada rodaram na mesma base, no mesmo ano, com o mesmo
back-end (o curso completo do expert) — e o resultado foi quase 19× de
diferença na taxa de subida:

| Front-end | Preço (relativo) | Compradores | Subiram pro back-end | Valor por comprador (relativo) |
|---|---:|---:|---:|---:|
| Livro digital | 8 a 11× o do ingresso | 151 | **11,3%** (16 pelas ofertas de um clique, 1 pelo cheio) | **7,7×** |
| Ingresso de imersão online | 1× | 335 | **0,6%** | **1×** |

O ingresso vendeu **mais que o dobro** de unidades e gerou **quase oito vezes
menos valor por comprador**.

## Explicação concorrente, levantada na conversa com o expert — não descartar

Na conversa com o expert, ele e o Rodrigo chegaram juntos a outra leitura do
mesmo fracasso, e ela é forte: **a oferta do carrinho não era o que o evento
prometeu.** O evento entregou exatamente o que o ingresso vendeu (uma técnica
específica, de escopo estreito) e o carrinho abriu com outro produto. Nas
palavras do Rodrigo: *"a pessoa ficou feliz, mas não tinha desejo de comprar
nada mais, porque ela queria saber de [...]"* — e o corte é justamente a
técnica que o evento ensinou.

Ou seja: o comprador do ingresso pode não ter subido **não porque o preço baixo
não qualifica**, mas porque a promessa era estreita demais e foi cumprida por
inteiro no evento — não sobrou problema para o produto caro resolver.

As duas explicações levam a decisões opostas:

| Se o problema é o **preço de entrada** | Se o problema é a **promessa estreita** |
|---|---|
| Sobe o preço do ingresso para qualificar | Mantém o ingresso barato e **amplia a promessa do evento** |
| Ingresso barato não volta | Ingresso volta, com evento de visão geral ("evolua um ano em dois dias") |

**Não dá para decidir entre elas com os dados atuais** — houve um evento só. O
teste que separa: rodar de novo com ingresso do mesmo preço e promessa ampla.
Se subir, o preço nunca foi o problema.

Enquanto isso não for testado, o número que fica de pé é o comparativo de
valor por comprador — que é medição, não interpretação.

## A leitura

**Preço de entrada não é só barreira de aquisição — é filtro de intenção.**
O ingresso, a pouco mais de 1% do preço cheio do curso, é barato o suficiente
pra ser comprado por curiosidade; o livro, de 8 a 11 vezes mais caro que o
ingresso, exige uma decisão que já se parece com a decisão do produto caro. A
lista maior do ingresso era, em grande parte, lista de curioso.

Corolário de verba: comprar tráfego pro produto de menor valor por comprador
derruba o ROAS consolidado sem que nenhum criativo tenha piorado. Na base
medida, o ROAS de 2,23× no período era a média de um funil que sobe com outro
que não sobe — olhar só o consolidado escondia isso.

**Regra prática que sai daqui:** todo produto de entrada é avaliado por
**valor por comprador** (receita direta + back-end gerado ÷ compradores),
nunca por unidades vendidas nem por receita direta. Unidade vendida de produto
de entrada não é resultado, é hipótese.

## A ressalva do evento presencial não se aplica aqui

Um ingresso de evento **presencial** teria outra função além de qualificar
(pagar a sala, garantir presença) e a venda de palco poderia sair da
plataforma medida, invalidando o cruzamento. **Não foi o caso: o evento era
online**, o pitch aconteceu dentro dele e qualquer venda cairia na mesma
plataforma onde os 335 compradores foram rastreados.

Ou seja, o ingresso tinha **uma** função — qualificar comprador para o
back-end — e a cumpriu em 0,6% dos casos.

Continua em aberto se o achado vale para ingresso de evento **presencial**,
onde a economia do ingresso é outra. Não medido.

## O que transfere e o que é do caso

**Provavelmente transfere:** a métrica (valor por comprador, não unidades) e a
ideia de que preço de entrada filtra intenção. Isso é mecânica de funil, não
particularidade de nicho.

**É do caso:** os números. 11,3% e 0,6% são desta base, deste nicho, deste
back-end e deste ano. A faixa de preço que qualifica muda com o ticket do
back-end — um livro a cerca de 12% do preço cheio do curso qualificou pra uma
oferta de um clique entre 16% e 28% desse preço cheio, num curso vendido na
Hotmart; não se sabe o que qualifica pra um back-end com o dobro do preço.

**Não medido:** a janela de subida (quantos dias entre a compra do livro e a
do back-end), que é o que diz quando o remarketing deve entrar. *(Na
recontagem citada no topo: no livro, 14 das 16 compras pelas ofertas de um
clique saíram em até 35 minutos e 1 pessoa comprou o curso cheio cerca de 87 h
depois. Uma compra posterior só não dá janela.)*

> Fonte: a análise do funil desse expert (livro × imersão), cruzando
> `buyer.email` entre front e back-end na API da Hotmart (evidência no caso de
> origem).
