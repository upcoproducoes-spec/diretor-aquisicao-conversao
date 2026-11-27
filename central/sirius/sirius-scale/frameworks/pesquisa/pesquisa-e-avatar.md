# Framework — Pesquisa, avatar e banco de ângulos (o insumo que o agente `copy` exige)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered de 11 conjuntos de pesquisa e avatar e de 3 bancos de ângulos da casa, de 5 donos (4
clientes e um produto SaaS), mais as falas do Rodrigo em 3 reuniões com experts de fora.

> **ALCANCE (proposto): TESTADO EM 3 CLIENTES no núcleo do processo, com uma etapa em 2.**
> Registrar a base (§3.3) e separar quem entra de quem paga (§3.5) rodaram em três clientes da casa (o
> caso-base, o segundo cliente e o cliente de perpétuo). Casar a resposta com a venda por e-mail (§3.4)
> rodou em 2 deles (o caso-base e o segundo cliente); no cliente de perpétuo o comprador veio da pesquisa
> pós-compra, que é o segundo caminho da §3.4. Confirmar esse alcance é decisão do Rodrigo.
> **NÃO TESTADO FORA** no resto: formulário, sub-avatares, linguagem e régua de qualificação têm base
> quase toda no caso-base; o banco de ângulos tem um segundo cliente (o de perpétuo). Todo número citado é
> do caso. A base de cada etapa vem na primeira linha dela; no título vai só a força.
>
> **Metodologia externa que falta:** a Pesquisa Inteligente (não faz parte deste kit). Nada aqui
> reconstrói o método, as categorias ou as perguntas dela. O lugar dela é a §0.
>
> **Quem usa este arquivo:** quem monta `pesquisa.md`, `avatar.md` e `banco-angulos.md` de um
> lançamento (`lancamentos/<AAAA-MM-nome>/`) ou de um perpétuo (`funis/<nome>/`). Os modelos em branco
> estão em `sirius-scale/modelos/pesquisa.md`, `sirius-scale/modelos/avatar.md` e
> `sirius-scale/modelos/banco-angulos.md`. O agente `copy` lê os três antes de escrever e para se faltar
> algum; o `/revisar` confere a copy contra eles.
>
> As citações vêm dos arquivos do caso de origem; nome, produto e dado de cliente estão trocados por um
> marcador entre colchetes.
>
> As contagens são da base que aparece aqui. Os rótulos de força são os da base completa da casa, e alguns dos
> casos dela não aparecem neste kit.

---

## 0. Referência externa que falta: Pesquisa Inteligente (slot vazio)

Na casa, o `pesquisa.md` foi especificado pra trazer N, fonte e as 6 categorias da Pesquisa Inteligente
(metodologia externa, não faz parte deste kit), e o `avatar.md` pra trazer sub-avatares, dores, desejos,
objeções, nível de consciência e linguagem real. A segunda parte a casa faz (§3.6 a §3.9). A primeira não
tem como: o método não está no kit, e a regra é perguntar em vez de inventar (`sirius-scale/REGRAS.md` §2).

O que os arquivos da casa fizeram enquanto isso (5 deles, de 4 donos):

1. Caso-base, funil de VSL: "Enquanto não estiver, este arquivo se organiza pelo que o dado sustenta."
2. Caso-base, evento pago (LPSG): "As categorias abaixo são as que existem de verdade nos formulários, não
   um formato imposto."
3. Segundo cliente, um lançamento: "As 6 categorias da Pesquisa Inteligente: o framework ainda não existe"
4. Produto SaaS e expert sem pesquisa: o mesmo aviso; o do SaaS se compromete a revisitar o arquivo quando
   a metodologia entrar.

**Se a metodologia entrar um dia** (numa versão nova do kit, ou do lado de vocês, em `frameworks-da-casa/`):

1. Ler o método e comparar, seção por seção, com as §3.1 a §3.9 daqui.
2. Onde ele mandar outra coisa e colidir com regra da casa (anti-invenção, `sirius-scale/REGRAS.md` §2),
   a casa vence. No resto, o método manda.
3. Responder a pergunta da §3.2: os formulários do caso-base saíram dele ou não (isso é do lado da casa).
4. Reorganizar os arquivos de pesquisa sem apagar o que o dado já mediu.
5. Subir o alcance deste arquivo só pelo que transferiu de fato.

---

## 1. Escopo e base de evidência

### 1.1 Fontes

**Nomes usados neste arquivo:** o **caso-base** (o cliente com mais peças na base, um expert de educação;
os lançamentos gratuitos dele são contados em ordem, do 1º ao 4º, e ele tem também um evento pago semanal,
o LPSG, um funil de VSL de um produto de entrada e uma Black de colheita); o **segundo cliente** (outro
expert da casa, de lançamento); o **cliente de perpétuo** (um expert com funil de VSL perpétuo); o
**produto SaaS** (um software, e um segundo produto da mesma empresa, voltado a negócio local); e o **expert
sem pesquisa** (um projeto que começou com avatar provisório).

| Fonte | O que é | Unidades | Peso |
|---|---|---|---|
| A | Caso-base, evento pago (LPSG): `pesquisa.md` (5 fontes, incluindo 490 respostas de uma pesquisa do LPSG processadas), `avatar.md` (com a camada de conversão do 3º lançamento gratuito), `banco-angulos.md`, e as 5 ideias de criativo tiradas da pesquisa de compradores | 3 arquivos + 1 lote de ideias | forte onde há correção ou aprovação registrada (escopo da pesquisa, nome do entregável, ideias 1 a 3); média no resto |
| B | Caso-base, funil de VSL: `pesquisa.md` e `avatar.md` (1.778 respostas filtradas de 7.776) e um script de segmentação por tema | 2 | forte nas duas decisões do Rodrigo registradas; média no resto |
| C | Caso-base, Black: `pesquisa.md` (sem pesquisa própria), `avatar.md`, `banco-angulos.md`, o levantamento do formulário anterior, o formulário novo e o retrato das respostas | 6 | forte: decisões do Rodrigo registradas, formulário no ar |
| D | Caso-base, 4º lançamento gratuito: `briefing.md` (fontes e diretrizes de tráfego tiradas de pesquisa × venda) e o acompanhamento diário da pesquisa (8 leituras) | 2 | média; as diretrizes foram pra planilha de planejamento |
| E | Cliente de perpétuo: `avatar.md` (lead, N=316), `avatar-comprador.md` (37 compradores no mercado principal + 17 num segundo mercado), `banco-angulos.md`, e o mapa de ângulos de uma análise de hooks da VSL (§7 dela) | 4 | forte nas decisões do Rodrigo; média no resto |
| F | Segundo cliente: `pesquisa.md` de dois lançamentos (um gratuito e a Black do ano anterior, lidas do Dash pelo MCP), os dois `avatar.md` que vieram prontos do projeto dele, e o briefing da Black seguinte | 5 | média nas pesquisas; fraca nos avatares externos, que as vendas desmentiram |
| G | Falas do Rodrigo em 3 reuniões com experts de fora: **G1**, uma consultoria; **G2**, uma call comercial; **G3**, uma demonstração do Dash Fácil | 3 | forte |
| H | Sem pesquisa própria ou com material pronto: o avatar provisório do expert sem pesquisa (N=0), os avatares do produto SaaS (lead × comprador) e do produto de negócio local (decisão do Rodrigo), e um avatar aprofundado que chegou pronto pro caso-base | 4 | média (expert sem pesquisa, SaaS); fraca (o material que chegou pronto) |

Peso da evidência: **forte** é o que foi ao ar, o que o Rodrigo decidiu ou o cliente corrigiu;
**média** é entregável da operação sem registro de aprovação; **fraca** é material que chegou pronto ou
rascunho. Regra que aparece só em fonte fraca não está aqui como regra.

### 1.2 Excluído de propósito

1. **MQL, faixa de score e o uso da pesquisa na verba**: moram em
   `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` (§1, §2, §3.6 a §3.10) e em
   `sirius-scale/frameworks/trafego/_metodologia.md`. Aqui só se cita.
2. **Leitura técnica do Dash** (denominador de cada métrica, planilha compartilhada, ligar a pesquisa,
   telefone que vive na pesquisa): `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.1, §2.9,
   §8.2 e §8.3.
3. **A pergunta "quem veio × quem comprou" do debriefing**:
   `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §4.8.
4. **Desejo primário, desejo necessário e mecanismo**: `sirius-scale/frameworks/lhto.md` §2 e §3. O avatar
   não faz esse mapeamento; quem faz é o documento de estratégia da peça (no caso-base, o documento de
   peças estratégicas da VSL; no cliente de perpétuo, o briefing).
5. **Os níveis de consciência em si**: `sirius-scale/frameworks/copy/great-leads.md` §0. A Escada de
   Consciência de Schwartz como arquivo próprio não faz parte deste kit.
6. **Ficha do expert** (`dna-expert.md`, `brand.md`, `produtos/`): é outro framework,
   `sirius-scale/frameworks/expert/ficha-do-expert.md`.
7. **O método externo da Black** usado como eixo do banco da Black: é de
   `sirius-scale/frameworks/lancamentos/black-friday.md`, com decisão pendente do Rodrigo. Citado só como
   origem.
8. **Resposta individual de lead, conversa de suporte, nome de respondente e de depoente**: dado
   pessoal. Não entra nem como exemplo. As frases citadas abaixo são de texto da casa, de formulário ou
   agregadas.
9. **A decisão de público do produto SaaS** (quem ele quer atender): é do produto. O SaaS entra só como
   unidade de método.

### 1.3 Ressalva estrutural e veredito da base

- **Unidades:** 11 conjuntos de pesquisa e avatar (18 arquivos), 3 bancos de ângulos, 1 formulário de
  lançamento desenhado e no ar, 3 reuniões com fala do Rodrigo sobre o método.
- **Donos:** o caso-base (4 conjuntos), o segundo cliente (3), o produto SaaS (2), o cliente de perpétuo
  (1) e o expert sem pesquisa (1).
- **Metade das peças é do caso-base**, e quase tudo que vai além do núcleo (§3.3 a §3.5) só tem ele como
  base.
- **Resultado:** nenhum banco de ângulos tem venda por ângulo medida, fora o do cliente de perpétuo (5
  hooks). As pesquisas têm resultado indireto: a mira de criativo e de segmentação do 4º lançamento do
  caso-base saiu delas, e o convite segmentado do downsell desse lançamento também.
- **Veredito do método:** **EXTRAÍVEL FORTE** (mais de 8 unidades; o núcleo rodou em 3 clientes, uma das
  etapas dele em 2), com a ressalva de que a metodologia externa de referência não está no kit.
- **Nesta versão do kit**, alguns casos não aparecem no texto. As contagens são da base que aparece aqui, e
  a força marcada em cada etapa é a da base completa.

---

## 2. A fórmula, em ordem

1. **Coletar** a pesquisa onde ela vem em volume: página de obrigado, com reforço nos canais de boas-vindas.
2. **Manter o formulário** entre lançamentos e mexer só no fim.
3. **Registrar a base** no `pesquisa.md`: fonte, N, escopo e o que ela não mede.
4. **Cruzar com a venda** por e-mail: conversão por resposta.
5. **Separar quem entra de quem paga**: avatar de lead e avatar de comprador.
6. **Montar os sub-avatares** pela situação real, com tamanho e conversão.
7. **Dores, desejos e objeções** com número e origem, em ranking.
8. **Linguagem real**: contagem nas abertas, dicionário e verbatim com origem.
9. **Nível de consciência** como leitura com lastro.
10. **Sem pesquisa própria ou com material pronto**: emprestar declarando, marcar a camada, conferir contra a venda.
11. **Banco de ângulos**: ângulo com rastro, regra de uso e o que não usar.
12. **Manter vivo**: camada nova por cima, correção que propaga.

Modos: **lançamento** (pesquisa por edição, em `lancamentos/<AAAA-MM-nome>/`), **perpétuo** (`funis/<nome>/`,
o avatar vai sendo trocado pelo `desempenho.md` quando o funil roda) e **colheita** (Black: base que já foi
pesquisada, o sub-avatar é o ponto da relação com o expert). Os três compartilham as etapas 3, 4, 7, 8 e 11.

---

## 3. Etapas detalhadas · força marcada em cada uma (CONSISTENTE / ISOLADA / INCONCLUSIVO)

### 3.1 Coletar onde a resposta vem em volume · PADRÃO CONSISTENTE (proposto)

**Base:** caso-base (1º, 3º e 4º lançamentos gratuitos e a Black) e a fala do Rodrigo em 3 reuniões.

**O que entra**
1. A pesquisa abre na página de obrigado, logo depois do cadastro, sem outro botão competindo: uma
   pergunta por tela, e o botão de enviar da última leva pro grupo de WhatsApp.
2. Os canais de boas-vindas reforçam: o e-mail de reforço traz o passo de responder, com linha de escape
   pra quem já fez (`sirius-scale/frameworks/copy/email.md`, Fase 2); no WhatsApp oficial, primeiro o
   grupo, depois a pesquisa.
3. Nome, e-mail e WhatsApp chegam por campo oculto, com o nome do campo igual ao do formulário. No 4º
   lançamento do caso-base o nome não bateu e a pesquisa ficou com 0 de 7.741 telefones
   (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.9).
4. Resultado que o Rodrigo relata na operação dele: de 60% a 80% de resposta (fala na G1, é resultado
   observado, não meta escrita). Nos arquivos: 66% no 3º lançamento e 68,49% no 4º (caso-base), 81% num
   lançamento do segundo cliente.

**Por quê**
- MQL e faixa só existem pra quem respondeu.
- Responder marca quem compra: 2,95% contra 0,83% no 3º lançamento do caso-base (3,5x). Taxa de resposta
  é alavanca de faturamento, e a base da pesquisa é a carteira de WhatsApp (o telefone vive nela:
  `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.9).

**Variações aceitáveis**
- Pesquisa por WhatsApp: foi o 1º lançamento do caso-base (451 respostas com abertas, contra 135 do
  obrigado, só fechadas). No 3º, já no obrigado, foram 4.717 respondentes de 7.139 leads; no 4º, 68,49% na
  tela do Dash; num lançamento do segundo cliente, 1.882 de 2.323.
- Presente pra quem responde (uma apostila no 4º lançamento; "Responder a pesquisa e retirar seu presente"
  no e-mail de boas-vindas). **VARIAÇÃO ISOLADA**: dois lançamentos de um cliente, efeito nunca medido.
- Duas versões (aluno e não aluno, na Black): numa planilha só, as colunas duplicaram e as respostas de
  não aluno foram pro fim da tabela (reunião da equipe na preparação da Black). A solução não foi fechada.

**Trecho real**
- Rodrigo (Fonte G1): "a pessoa cai na página de obrigado, só com a pesquisa direto para ele ir
  respondendo. Ela vai clicando, vai indo para a próxima." ... "na última pergunta, o botão de enviar vai
  para o grupo. Então, obviamente, tem uma queda no grupo." ... "As minhas pesquisas aqui batem entre 60% e
  80% de resposta."
- Rodrigo (Fonte G3): "quando você tem uma taxa de resposta alta, o teu MQL vai ficar mais assertivo,
  porque o MQL é baseado em quem responde a pesquisa"
- Briefing do 4º lançamento do caso-base (diretrizes de tráfego, item 5): "Quem responde a pesquisa
  converte 3,5x mais. Aumentar a TAXA DE RESPOSTA é a alavanca de faturamento mais barata identificada."

### 3.2 Manter o formulário e mexer só no fim · PADRÃO CONSISTENTE (proposto); pergunta nova no fim: VARIAÇÃO ISOLADA

**Base:** caso-base, 4 lançamentos com o mesmo formulário (2º, 3º e 4º lançamentos gratuitos e a Black);
a pergunta nova no fim, 1 lançamento (a Black).

**O que entra**
1. Texto e opções das perguntas fechadas iguais de um lançamento pro outro. No caso-base, as mesmas 13
   perguntas rodaram no 2º lançamento, no 3º (em outra ordem), no 4º e na Black.
2. As perguntas do MQL não mudam de texto nem de opção. O Dash junta as perguntas da regra por E, então
   mudar uma desmonta a comparação (`sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §1).
3. Pergunta nova vai no fim, marcada como nova, fora do MQL e da nota. Na Black: uma de preferência de
   produto, pedida pelo Rodrigo, e uma de idade, proposta pela gerente de operação e aceita por ele, com as
   faixas do relatório de idade da Meta e do Google pra cruzar com a campanha sem reagrupar.
4. Fechada é filtro; aberta é vocabulário.
5. Quem já comprou responde outra pesquisa (pós-compra): uma de preferência entre alunos na Black do
   caso-base, o raio-x de compradores do cliente de perpétuo, o onboarding do produto SaaS.

**Por quê**
Comparar lançamentos só funciona com o mesmo formulário. No 4º lançamento do caso-base, a leitura diária
contra o 3º mostrou desde a primeira leitura uma base mais fria: mais gente que nunca comprou, menos gente
com compra frustrada (Fonte D).

**Variações aceitáveis**
Famílias de pergunta que se repetem nos formulários lidos. Isto é o que apareceu nos formulários, não a
lista de categorias da Pesquisa Inteligente, e quem escreveu cada formulário não está registrado (§0).
- O momento da pessoa com o problema hoje (caso-base; no segundo cliente, no formato "Qual dessas situações
  mais parece a sua HOJE com [o problema]?").
- Se já comprou curso do mesmo problema (caso-base, segundo cliente, raio-x do cliente de perpétuo).
- O que trava além de dinheiro e tempo (caso-base, segundo cliente; no cliente de perpétuo, "O que impede
  (tirando dinheiro)").
- O tema ou a etapa que mais trava (caso-base, segundo cliente).
- O que a conquista significaria (caso-base; impacto na carreira no segundo cliente; objetivo e desejo no
  cliente de perpétuo).
- Intenção: ser avisado da próxima turma (caso-base, segundo cliente).
- Relação com o expert: há quanto tempo conhece e por onde chegou (cliente de perpétuo, Black do ano
  anterior do segundo cliente).
- Uma pergunta direta pro expert (caso-base), a aberta mais rica no funil de VSL.
- Perfil: renda, escolaridade, atuação, idade (idade e gênero ficaram de fora num lançamento do segundo
  cliente).
- Pergunta nova amarrada a uma decisão de copy que hoje é chute (funil de VSL, 7 perguntas propostas pra
  pesquisa própria; **VARIAÇÃO ISOLADA**, não rodou).

**Trecho real**
- Levantamento do formulário anterior (Black do caso-base): "Se o texto ou as opções dessas duas mudarem, o
  MQL da Black deixa de ser comparável e a regra do Dash precisa ser refeita."
- Formulário novo da Black do caso-base: "As 13 não se editam, nem pra corrigir." e "A 14 e a 15 são
  novas, marcadas NOVA. Vão no fim e ficam fora do MQL e da nota." Nas notas de montagem: "Pergunta nova no
  fim não pode custar a pesquisa inteira"
- `pesquisa.md` do evento pago do caso-base (antes de padronizar): "Inconsistência sinalizada: opções de
  pergunta variaram entre formulários de lançamentos diferentes, o que dificulta cruzamento histórico —
  vale padronizar."
- Rodrigo (Fonte G2): "Eu coloquei outra pergunta também, você gostaria de ser avisado quando abrir uma
  nova turma?"
- Resultado da pergunta nova da Black (retrato das respostas): o programa principal vitalício foi o mais
  querido por 151 de 197 não alunos (77%) e por 40 de 57 alunos (70%).

### 3.3 Registrar a base no `pesquisa.md` · PADRÃO CONSISTENTE (proposto)

**Base:** caso-base, segundo cliente e cliente de perpétuo, e também o produto SaaS. A regra de zero
invenção está escrita nos arquivos de mais de um dono.

**O que entra**, no topo do arquivo:
1. A fonte: arquivo, ferramenta e data da leitura (CSV em `dados/` do lançamento, Dash pelo MCP, planilha).
2. O N: respostas, de quantos inscritos, quantas únicas por e-mail.
3. O escopo: de que funil e de que momento é a base (lead do gratuito, comprador do ingresso, comprador
   do produto, aluno) e pra qual oferta ela foi feita.
4. O que a base não traz: pergunta que não existia, idade e gênero não perguntados, abertas que não vêm
   pelo MCP, nenhuma venda casada.
5. A regra do arquivo: zero invenção, número sem fonte não entra.

Depois: uma seção por fonte quando há mais de uma; a tabela das perguntas com o uso de cada uma no
avatar; os cortes rodados e como (planilha, script ou tela do Dash); notas de método.

**Por quê**
- O `copy` para se o arquivo faltar e escreve errado se o escopo estiver errado. A correção que o cliente
  registrou no evento pago do caso-base é o exemplo: a pesquisa era de comprador do ingresso barato e não
  podia ser lida como perfil de quem compra o programa, que custa de 30 a 40 vezes mais.
- Número sem arquivo não sobrevive: a pesquisa do 3º lançamento chegou a ser descrita com um N sem fonte
  (evidência no caso de origem).

**Variações aceitáveis**
- Arquivo que não repete as tabelas e só diz o que sustenta cada número do avatar (funil de VSL).
- Arquivo com as tabelas e a coluna de quantos compraram por resposta, quando a fonte é o Dash pelo MCP
  (segundo cliente).
- Arquivo de lançamento sem pesquisa própria, com tabela das fontes emprestadas (Black do caso-base, §3.10).

**Trecho real**
- `pesquisa.md` do evento pago do caso-base (registrado como correção do cliente): "Não tratar o perfil
  daqui como igual ao perfil de quem compra o [programa] — são dois patamares de decisão diferentes, mesmo
  sendo o mesmo funil."
- `pesquisa.md` do funil de VSL: "o registro de onde vêm os números do avatar.md — fontes, N, método e
  limites. Não repete as tabelas; diz o que sustenta cada uma."
- `pesquisa.md` de um lançamento do segundo cliente: "Idade e gênero não foram perguntados." e "Onde os
  números divergem, valem os desta página."

### 3.4 Cruzar a pesquisa com a venda · PADRÃO CONSISTENTE (proposto)

**Base:** casamento da resposta com a venda por e-mail em 5 bases de 2 clientes: caso-base (2º e 3º
lançamentos e o muro do dia 1 do 4º; o recorte do funil de VSL reusa os dois primeiros) e segundo cliente
(dois lançamentos, um com 16 compradores e outro com 9). O segundo caminho (item 6) rodou no cliente de
perpétuo (raio-x de 37 compradores contra a pesquisa de lead) e no produto SaaS (onboarding); no cliente
de perpétuo não houve casamento por e-mail.

**O que entra**
1. Casar cada resposta com a venda pelo e-mail (minúsculo, sem espaço). Uma resposta por pessoa por
   lançamento, a mais recente.
2. Conversão por resposta: pra cada opção de cada pergunta fechada, quantos responderam e quantos
   compraram. É a tabela de vendas por resposta na pesquisa, que o Rodrigo usa no debriefing.
3. Respondente contra não respondente.
4. Quantas vendas não casaram (e-mail diferente no checkout). No 3º lançamento do caso-base foram 71 de
   230: a direção vale, o número absoluto fica por baixo.
5. Célula com menos de 10 compradores é direção, não número, e vem marcada. Pra afirmar que uma resposta
   converte mais que outra, teste: z de duas proporções no caso-base.
6. Se existe pesquisa pós-compra, um segundo caminho: o peso da resposta entre compradores dividido pelo
   peso entre leads.

**Por quê**
É o cruzamento que diz quem é o comprador, e dele sai a mira da copy, do criativo e da segmentação (as
diretrizes de tráfego do 4º lançamento do caso-base saíram dele). Volume não diz isso (§3.5).

**Variações aceitáveis**
- Pelo Dash: a tela de pesquisa × vendas do debriefing (`pesquisa_debriefing` pelo MCP), como num
  lançamento do segundo cliente. Número que vai pra peça sai da tela, não do cruzamento por fora (regra da
  casa).
- Por fora (planilha ou script próprio): casar a coluna pelo texto da pergunta, não pela posição, e juntar
  lançamentos. Foi o que a casa fez no funil de VSL.
- A faixa de score do Dash (A a D) entra como corte de comportamento ao lado das respostas: no 3º
  lançamento do caso-base, faixa A converteu 9,13% e D 0,88% (camada de conversão do avatar do evento pago).
  É cálculo do Dash sobre quem respondeu; o Rodrigo (Fonte G2): "isso aqui você tem que ter muitos
  clientes que responderam a pesquisa pra fazer sentido". Leitura e uso na verba:
  `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` e
  `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.1.
- Os usos já têm dono: perfil por criativo e projeção pelo mix em
  `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §3.6 e §3.8; a pergunta do debriefing em
  `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` §4.8.

**Trecho real**
- Rodrigo (Fonte G1): "E esse cruzamento, né, pra vocês fazerem que é importante, não sei se vocês já
  fizeram, não achei nos documentos ali, que é por vendas por resposta na pesquisa."
- Rodrigo (Fonte G3): "Aí você saber a conversão que cada resposta te deu." ... "Isso aqui vai te dar
  inteligência para você criar as copies do teu semente."
- `pesquisa.md` do funil de VSL, §5: "Direção confiável, absoluto subestimado." e "Célula com menos de 10
  compradores está marcada no avatar e não sustenta afirmação sozinha."

### 3.5 Separar quem entra de quem paga · PADRÃO CONSISTENTE (proposto)

**Base:** caso-base, cliente de perpétuo e segundo cliente, e o produto SaaS (4 casos medidos, abaixo).

**O que entra**
1. Dois retratos lado a lado: o do lead (quem respondeu na captação) e o do comprador (cruzamento da §3.4
   ou pesquisa pós-compra), com a tabela dos cortes em que divergem.
2. A regra de uso escrita no arquivo: captação, hook e primeiros segundos falam com o lead; meio e fim da
   VSL, página, oferta e fundo de funil falam com o comprador.
3. O lançamento se formata pro comprador e conecta o resto com uma frase de inclusão. No caso-base, o
   qualificado era 27% de quem respondeu, e o foco de conteúdo, criativo e lançamento é nele.
4. Comprador deduzido da pesquisa antes de existir venda é hipótese até a venda confirmar.
5. O avatar comprador vira a regra de qualificação do lançamento seguinte: as respostas que o comprador
   marca viram as respostas ideais do MQL no Dash (régua e validação em
   `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §1 e §2).

**Por quê**
Nos 4 casos em que deu pra medir, quem entra e quem paga eram pessoas diferentes:
- Caso-base, 3º lançamento: o iniciante sem método, sub-avatar 1 pelo volume no topo do arquivo, foi o que
  menos converteu (2,57%, N = 1.792); o grupo que tem base mas não é consistente tinha menos da metade do
  tamanho dele e converteu 5,76%. O maior grupo da camada de conversão é o reincidente (2.196, 3,51%).
- Cliente de perpétuo: 71% dos leads conheciam o expert havia menos de 1 mês; 65% dos compradores já o
  conheciam. Renda e idade também divergiram.
- Segundo cliente: o comprador núcleo do avatar não se confirmou (6 dos 9 compradores nunca tinham
  investido em curso do tema), e as turmas de dois anos seguidos discordaram no perfil de quem comprou.
- Produto SaaS: 76% dos leads estavam na faixa de faturamento anual mais baixa da pesquisa; entre
  compradores, 23%.

**Variações aceitáveis**
- Dois arquivos (`avatar.md` do lead e `avatar-comprador.md`), como no cliente de perpétuo, quando a
  pesquisa de comprador é outro formulário.
- Uma camada de conversão por cima do avatar de volume, no mesmo arquivo (caso-base, avatar do evento pago).

**Trecho real**
- `avatar.md` do cliente de perpétuo: "aqui está quem entra no funil, lá está quem paga." e "Copy de
  captação usa este; copy de VSL e de fundo de funil usa o outro."
- `avatar.md` do evento pago do caso-base: "A ordem por volume inverte a ordem por conversão. Isso é o
  achado central" e "Não é o perfil mais numeroso da base — é o que paga."
- Rodrigo (Fonte G1): "o lançamento é todo formatado pro avatar comprador e eu conecto com quem não é
  comprador" ... "99% dos 27%, 1% eu conecto. Você que está começando, é pra você também."
- `pesquisa.md` de um lançamento do segundo cliente: "que foi deduzido da intenção e do histórico de compra
  declarados, antes de existir venda" e "9 compradores é amostra pequena demais pra regra."
- Rodrigo (Fonte G2), sobre o avatar comprador que configura o MQL: "Eu sei isso baseado no debrief, no
  histórico e tal."

### 3.6 Sub-avatares pela situação real, com tamanho e conversão · PADRÃO CONSISTENTE (proposto); por ponto da relação: VARIAÇÃO ISOLADA

**Base:** caso-base (evento pago, funil de VSL, 4º lançamento) e a fala do Rodrigo; o sub-avatar por ponto
da relação, 1 lançamento (a Black do caso-base).

**O que entra**, por sub-avatar:
1. O nome tirado da situação que a pessoa marcou (uma opção fechada, ou a soma de duas).
2. Tamanho (% e N) e conversão, quando há venda casada.
3. Como ele fala (§3.8), a objeção que carrega e o que a copy faz com ele.
4. A ordem de prioridade pra copy, que é conversão, volume e o que a pessoa disse, nessa conta. O grupo
   grande que converte pouco fica registrado como volume sem prioridade, com a hipótese escrita pra medir
   (no funil de VSL: converte pouco no preço do programa e pode converter bem num produto de cerca de um
   sexto desse preço).
5. Sobreposição dita no arquivo: o mesmo lead cabe em mais de um sub-avatar.

Em lançamento de colheita (a Black do caso-base), o sub-avatar é o ponto da relação com o expert: aluno do
produto, aluno recente, comprador de outro produto, lead que viu a oferta e não comprou, lead novo. Cada
um com quantos são, o que move, o que trava, o preço e, onde precisa, o que nunca dizer pra ele.

**Por quê**
Sub-avatar decide mira e verba. No 4º lançamento do caso-base, a pesquisa × venda do 3º virou duas listas
no briefing (público a priorizar e a despriorizar, cada um com corte, conversão e N) e foi pra planilha de
planejamento.

**Variações aceitáveis**
- Núcleo, pontes e cauda (avatar de um lançamento do segundo cliente, que veio pronto): o mesmo desenho,
  mas o núcleo foi deduzido antes da venda e não se confirmou.
- Sub-avatar provisório por produto, sem pesquisa, com a origem de cada frase (expert sem pesquisa, um por
  ferramenta do produto de entrada; §3.10).
- Observação, sem regra registrada: nos avatares escritos pela casa, nenhum sub-avatar tem nome de pessoa.
  Nome de pessoa inventado só aparece no avatar que veio pronto do projeto do segundo cliente, e apelido de
  arquétipo, no avatar aprofundado que chegou pronto pro caso-base. Ver Pontos em aberto.

**Trecho real**
- `avatar.md` do funil de VSL, §4: "Ordem = conversão × volume × o que a pessoa disse. Os seis se
  sobrepõem; não são caixas." e, no grupo grande que converte pouco: "volume, não prioridade"; "Não
  descartar; medir."
- `avatar.md` da Black do caso-base: "O que a Black acrescenta é em que ponto da relação cada pessoa está —
  é isso que decide preço, mensagem e canal."
- Briefing do 4º lançamento do caso-base: "Isto NÃO é sugestão: é padrão medido, no mesmo produto e
  [mesmo expert]."
- Rodrigo (Fonte G2): "Eu faço criativo específico para [um segmento da pesquisa]."

### 3.7 Dores, desejos e objeções com número e origem · PADRÃO CONSISTENTE (proposto) no ranking; desejo do comprador e camadas de desejo: VARIAÇÃO ISOLADA

**Base:** ranking em 2 donos com evidência forte ou média (caso-base, cliente de perpétuo). Desejo do
comprador: 1 caso.

**O que entra**
1. Cada dor, desejo e objeção com o número e a pergunta de onde saiu (fechada: %; aberta: quantas
   respostas mencionam).
2. Objeções em ranking pelo dado, e ao lado o que a resposta pede: prova de quem tinha o mesmo histórico,
   diferença de método, condição de pagamento quando a oferta permite.
3. Objeção que só existe na cabeça da equipe sai do ranking. No funil de VSL do caso-base, a objeção de a
   prova da pessoa não cobrar o tema do produto foi rebaixada: nenhuma resposta a sustentava, e o Rodrigo
   decidiu que esse público não é o avatar. Virou pergunta pra pesquisa própria.
4. Desejo: o mais citado pela base nem sempre é o de quem compra. No raio-x do cliente de perpétuo, 1
   comprador em 37 citou dinheiro. **VARIAÇÃO ISOLADA** (1 caso).
5. A dor raiz que não vira frase de copy mas decide regra: a autoimagem de quem acha que não nasceu pra
   aquilo é o motivo pra Regra de Crença (`sirius-scale/frameworks/lhto.md` §2.3) ser inegociável, não
   material de anúncio.
6. Quando já existe peça, a tabela de objeção ganha a coluna de como a peça trata hoje (raio-x do cliente
   de perpétuo; as 8 leads da VSL do caso-base contra o avatar).

**Por quê**
É o que o `copy` usa e o que o `/revisar` confere. E a ordem das objeções muda a ordem dos blocos: no dia 1
de carrinho do 4º lançamento do caso-base, o muro (faixa A/B que respondeu e não comprou) era de
reincidente frustrado, e a live de objeção foi reordenada a partir disso
(`sirius-scale/frameworks/lancamentos/cpl-3-aulas.md`, live de objeção no dia 1).

**Variações aceitáveis**
- Desejo em duas camadas, material e de identidade (funil de VSL). **VARIAÇÃO ISOLADA**.
- Menção espontânea mede o que a pessoa lembra de escrever. No segmento do funil de VSL, tempo apareceu em
  26,8% das abertas e o branco na hora da prova em 1,6%; o arquivo não concluiu que era pra cortar o pânico,
  só que o roteiro falava apenas do momento da prova. **VARIAÇÃO ISOLADA**.

**Trecho real**
- `avatar.md` do evento pago do caso-base: "Neutralizar com prova social segmentada por perfil (idade,
  tempo sem estudar, histórico de fracasso)" e "nunca com desconto ou pressão".
- `avatar.md` do funil de VSL, §5, §6 e §8: "Ressalva honesta: menção espontânea não é ressonância."; "Isso
  não vira copy. Vira o motivo de a Regra de Crença (LHTO §2.3) ser inegociável nesta VSL: o vilão é o
  ensino, nunca a pessoa."; e a decisão do Rodrigo, registrada lá, de que quem não tem o tema do produto na
  prova não é o avatar.
- `avatar-comprador.md` do cliente de perpétuo, §4, cabeçalho da tabela: "Como a VSL trata hoje".
- `.claude/skills/revisar/checklists/copy.md`, bloco A: "Cada dor, desejo, objeção e número tem fonte."

### 3.8 Linguagem real e verbatim · PADRÃO CONSISTENTE (proposto)

**Base:** 2 donos com evidência forte ou média (caso-base, cliente de perpétuo).

**O que entra**
1. Contagem por termo nas abertas (radical sem acento, ou expressão regular por tema com a regra salva),
   declarada como contagem por baixo: dá ordem de grandeza.
2. Com venda casada, o tema citado por lead contra o citado por comprador.
3. Um dicionário em três listas: as palavras deles (usar), as que sinalizam objeção (endereçar), e as que
   a equipe ou o roteiro usa e eles não usam. Quando a palavra da equipe perde pra do avatar na contagem,
   troca, inclusive na promessa.
4. Verbatim: literal, sem edição, com origem (lançamento, arquivo, linha) e contexto (sobre o que a pessoa
   falava). Frase real fora do assunto original é erro: uma vez, uma frase sobre um tema geral da matéria
   entrou numa peça sobre outro conteúdo.
5. Três tipos de fala separados no arquivo: a do lead (pesquisa), a recontada pelo expert, e a reconstruída
   por quem escreveu o documento, marcada. Frase do expert vai pro banco de ângulos, não pro dicionário do lead.
6. Nos avatares lidos, o verbatim de lead aparece sem nome. O rastro até a linha do CSV fica na revisão.

**Por quê**
O `copy` escreve com "a palavra é a do cliente, não a sua", e lead e comprador falam diferente: no cliente
de perpétuo, o lead falava em se sentir mediano e em insegurança; o comprador, em reproduzir o resultado
técnico (cerca de 25 de 37), padronização e protocolo reproduzível. A VSL usava só a primeira língua.

**Variações aceitáveis**
- Pergunta de uma palavra só sobre o sentimento com o próprio resultado (cliente de perpétuo): contagem
  limpa. **VARIAÇÃO ISOLADA**.
- Ler na íntegra uma amostra das abertas mais ricas (120 perguntas diretas pro expert, no funil de VSL) e
  deixar o resto só na contagem.
- Vocabulário do lead pra parar o scroll e do comprador pra fechar (cliente de perpétuo; o produto SaaS tem
  a mesma divisão). **VARIAÇÃO ISOLADA**.

**Trecho real**
- `pesquisa.md` do funil de VSL, §7: "A categorização de texto aberto é por termo. Serve pra ordem de
  grandeza (tempo 27% × trava 1,6%), não pra decimal."
- `.claude/agents/copy.md`: "Verbatim só entra com a origem e o contexto"
- `avatar.md` do evento pago do caso-base: "Falas reconstruídas no doc de avatar estão marcadas
  [reconstruído]"
- Rodrigo (Fonte G1): "As palavras que saem de quem compra." ... "Isso aqui já traz ideia de criativo
  também."

### 3.9 Nível de consciência como leitura com lastro · PADRÃO CONSISTENTE (proposto)

**Base:** a leitura declarada como leitura em 4 arquivos de 3 donos (caso-base ×2, expert sem pesquisa,
produto SaaS); a pergunta que mede, nos formulários de 2 donos (cliente de perpétuo, segundo cliente).

**O que entra**
1. O nível predominante e a fração que está noutro nível, escritos como leitura de quem montou o arquivo,
   não como número da pesquisa. A régua dos níveis é a do `sirius-scale/frameworks/copy/great-leads.md` §0
   (é a mesma do modelo `sirius-scale/modelos/avatar.md`).
2. Os sinais do dado que sustentam a leitura: quantos estudaram sem método, quantos nunca ouviram falar da
   solução, há quanto tempo conhecem o expert, se já compraram dele.
3. Base de colheita: a base inteira está consciente do produto, e o lead novo da captação é a exceção que
   as lives de aquecimento levam até lá (Black do caso-base).
4. Quando o formulário tem, a pergunta que mede: há quanto tempo conhece o expert e por onde chegou
   (cliente de perpétuo, Black do ano anterior do segundo cliente); ou se a pessoa já conhece o tipo de
   solução que o produto oferece.

**Por quê**
O `copy` escolhe o ângulo pelo nível, e o `sirius-scale/frameworks/copy/great-leads.md` §5 manda
posicionar o avatar na escala a partir do `avatar.md`. E a temperatura do lead e a do comprador se leem
separadas: no cliente de perpétuo, 71% dos leads conheciam o expert havia menos de 1 mês, e o avatar de
lead registrou que a tese do funil "pressupõe um lead mais maduro do que a base medida"; o raio-x de
comprador mostrou depois que, pra quem paga, a mesma premissa acerta (`avatar-comprador.md` §1).

**Variações aceitáveis**
- "Não encontrado", quando não há sinal nenhum.

**Trecho real**
- `avatar.md` do evento pago do caso-base: "Observação: o nível de Schwartz é leitura a partir dos dados,
  não um número declarado na pesquisa."
- `avatar.md` do funil de VSL, §9: "Leitura a partir dos dados, não número declarado."
- `avatar.md` do cliente de perpétuo: "É público frio, recém captado por Instagram."
- `avatar.md` da Black do caso-base: "A base inteira está consciente do produto"
- `sirius-scale/frameworks/copy/great-leads.md` §5: "Antes de escrever a lead, posicionar o avatar na escala"

### 3.10 Sem pesquisa própria, ou com material que chegou pronto · PADRÃO CONSISTENTE (proposto)

**Base:** 4 donos (caso-base, produto SaaS, expert sem pesquisa, segundo cliente). A evidência aqui é o
cabeçalho que a casa escreveu em cima do material, não o material de fora.

**O que entra**

*A. Sem pesquisa própria*
1. Emprestar a base mais próxima de mesma estrutura e dizer que é empréstimo. Casos: o 4º lançamento do
   caso-base usou o 3º enquanto a própria era imatura; a Black usou quatro lançamentos e a base de
   compradores da Hotmart; o funil de VSL usou o recorte de quem marcou o tema do produto nas pesquisas do
   programa (decisão do Rodrigo); o produto de negócio local usou a pesquisa de outro funil (decisão do
   Rodrigo).
2. Dizer o que o empréstimo não mede (no funil de VSL, a compra medida é de outro produto) e o que o
   substitui quando o funil rodar (`funis/<nome>/desempenho.md`, no perpétuo; modelo em
   `sirius-scale/modelos/desempenho.md`).
3. Listar as perguntas que a pesquisa própria deveria ter.
4. O arquivo existe mesmo emprestado, porque é ele que deixa o `copy` trabalhar. Sem ele, a copy trava:
   na Black seguinte do segundo cliente, pesquisa e avatar não existiam e a decisão ficou pendente entre
   três caminhos.

*B. Camadas de confiança.* Quando as fontes pesam diferente, o avatar diz a camada (dado real emprestado,
diagnóstico de quem conhece o mercado, hipótese da página) e a copy diz em qual se ancora (produto de
negócio local).

*C. Avatar provisório (N = 0).* Só frase que existe no material do expert, com a origem; o que não dá pra
inventar listado; e o que falta pra virar avatar de verdade (expert sem pesquisa).

*D. Material que chegou pronto*
1. Avatar de outro projeto: copiado sem edição, com um cabeçalho da casa em cima (origem, de que
   lançamento é, base, o que as vendas disseram, o que fere regra da casa). Segundo cliente, dois arquivos.
2. Análise pronta feita por terceiro: entra como resumo, dizendo que a análise não é da casa.
3. Documento gerado por IA: serve de apoio pra ler o resto, nunca como pesquisa primária.
4. Percentual com til de análise feita fora dos arquivos é estimativa (no evento pago do caso-base, o mapa
   comprador × não comprador do programa); a camada contada vem por cima quando há venda casada.
5. Documento com falas reconstruídas: a fala usada vem marcada como reconstruída (o avatar aprofundado que
   chegou pronto pro caso-base).

**Por quê**
`sirius-scale/REGRAS.md` §2: "Faltou dado? Pergunta e para. Nunca preenche buraco com suposição." O
empréstimo declarado deixa a operação andar sem fingir que a base é própria. E material pronto erra: o
comprador núcleo de um lançamento do segundo cliente, deduzido antes da venda, foi desmentido pelos 9
compradores.

**Variações aceitáveis**
- Pesquisa de modelo, não de edição: no LPSG, que roda toda semana, "Pesquisa e avatar não precisam ser
  refeitos por edição" (`sirius-scale/frameworks/lancamentos/lpsg.md`).

**Trecho real**
- Briefing do 4º lançamento do caso-base (fontes): "A pesquisa do [lançamento atual] ainda está imatura (44
  respostas [no 1º dia da captação paga])." e "a referência é a base do [lançamento anterior] — mesma
  estrutura de perguntas"
- `pesquisa.md` da Black do caso-base: "A Black não teve pesquisa própria. Ela é colheita de uma base que
  já foi pesquisada em quatro lançamentos; este arquivo junta o que vale pra ela, com a fonte de cada
  número."
- `avatar.md` do funil de VSL, §0: "é proxy de propensão, não medição do funil"
- `avatar.md` do produto de negócio local: "Decisão do Rodrigo [...]: usar o que já foi pesquisado sobre
  negócio local antes do lançamento." e "Ao entregar copy do [produto], dizer em qual camada ela se ancora."
- Avatar provisório do expert sem pesquisa: "É um avatar PROVISÓRIO, não é pesquisa." e "Tudo isso é a
  versão dele do que o público diz, e não o público falando."
- `avatar.md` de um lançamento do segundo cliente, cabeçalho da casa: "é dedução da pesquisa, feita antes
  da venda"
- Briefing da Black seguinte do segundo cliente: "Pesquisa e avatar da Black: não existem. O que há pra
  decidir"

### 3.11 O banco de ângulos · PADRÃO CONSISTENTE (proposto)

**Base:** 3 bancos de 2 clientes (caso-base: evento pago e Black; cliente de perpétuo).

**O que entra**, nesta ordem (as partes 1, 2, 3 e 5 estão nos três bancos; a 4 em dois):
1. Cabeçalho com as fontes e a regra de uso: que oferta e que público a peça vende, e o que fica de fora.
   Ângulo do produto caro fica separado e marcado pra não entrar na peça que vende a entrada.
2. Os ângulos, um por um, cada um com a evidência (número da pesquisa ou da venda, verbatim com origem,
   trecho do conteúdo) e o status: testado em venda, ou só matéria-prima.
3. Frases do expert, rastreáveis, sem parafrasear.
4. Mapa ângulo × sub-avatar (× público, na Black).
5. O que não usar, com o porquê: ângulo que perdeu em venda, ângulo sem lastro, o que não entra em copy
   nenhuma, decisão do Rodrigo.
6. Prova social que pode ser usada: número, fonte, e o que precisa de pergunta antes. Conflito entre
   fontes vira pergunta (cliente de perpétuo).
7. Pontos em aberto.

Regra da peça: cada peça declara um ângulo principal, e ângulo fora do banco precisa de lastro novo.

**De onde sai o ângulo**, um tipo de fonte em cada banco:
- o conteúdo que o expert entregou (scripts e transcrições das aulas do evento): evento pago do caso-base;
- a pesquisa de comprador e a conversão medida por hook: cliente de perpétuo;
- decisões do briefing, base medida, reuniões com o expert e o eixo do método externo de Black
  (`sirius-scale/frameworks/lancamentos/black-friday.md`; só citado como origem): Black do caso-base.

**Por quê**
O `copy` lê o banco antes de inventar ângulo, e é no banco que entrada e produto caro se separam. O agente
diz isso em uma linha: "Nunca misture entregável ou bônus do produto caro numa peça que vende só a entrada."
(`.claude/agents/copy.md`).

**Variações aceitáveis**
- Mapa por etapa em vez de por sub-avatar (cliente de perpétuo: língua do lead no hook, do comprador no
  fechamento).
- Banco tirado de uma análise de hooks (cliente de perpétuo). O mapa da análise tinha como forte o ângulo
  de quem acompanha o expert e nunca comprou; no banco ele virou proibido por decisão do Rodrigo.

**Trecho real**
- `banco-angulos.md` do evento pago do caso-base: "Ângulo de venda do [programa] está separado no fim e não
  entra em criativo de aquisição de ingresso." e "Tudo aqui é matéria-prima validada como conteúdo, não
  como criativo vencedor." No Bloco E: "Todas ditas por [o expert], rastreáveis. Não parafrasear sem
  necessidade."
- `banco-angulos.md` do cliente de perpétuo: "Cada peça declara um ângulo principal. Ângulo sem lastro
  nesta lista não entra" e, na tabela de proibidos: "Decisão do Rodrigo [...]: amarra a peça a um público
  que acaba e obriga a regravar."
- `banco-angulos.md` da Black do caso-base: "Tudo aqui rastreia até um dado real", e a seção "O que não
  entra em copy nenhuma".

### 3.12 Manter vivo · camada por cima: PADRÃO CONSISTENTE (proposto); acompanhamento diário na captação: VARIAÇÃO ISOLADA

**Base:** camada por cima em 2 donos (caso-base, segundo cliente); acompanhamento diário, 1 lançamento (o
4º do caso-base).

**O que entra**
1. Venda nova entra como camada nova, datada, por cima, e a camada diz o que corrige no que está escrito
   antes (o avatar do evento pago ganhou a camada de conversão do 3º lançamento, e ela corrigiu duas
   afirmações).
2. Quando a base final difere da que gerou o avatar, o `pesquisa.md` diz que os números dele valem por
   cima (segundo cliente). Quando aparece fonte melhor, o arquivo abre com o aviso e diz qual prevalece.
3. Correção propaga: buscar o número ou a afirmação em todos os arquivos (`expert/`, `lancamentos/`,
   `funis/`, `entregas/`) e corrigir avatar, banco e peças.
4. Na captação do 4º lançamento do caso-base houve leitura diária da pesquisa contra o lançamento anterior:
   N e ritmo por dia, marcos de N, tema novo nas abertas por frequência de termo e teste z de cada corte.
   No padrão de rotinas da casa ela saiu: a qualificação entra no relatório de tráfego, casada por e-mail.

**Por quê**
Correção que fica num lugar só é desmentida pelo outro. Caso vivo: a camada de conversão do evento pago
corrigiu que um segmento profissional não era de baixa conversão, e o banco do evento pago e o avatar da
Black continuam mandando não priorizar (Pontos em aberto).

**Variações aceitáveis**
- O banco também se corrige no próprio arquivo, com a nota do erro: a Black teve uma conta de preço falsa
  pra quem não é aluno, apontada pelo `copy` e corrigida.

**Trecho real**
- `avatar.md` do evento pago do caso-base: "É a primeira vez que o avatar tem taxa de compra medida por
  corte" e "Corrige duas coisas do que está escrito acima neste arquivo"
- Correção registrada na casa sobre número sem fonte: "a primeira correção pegou 1 de 4 lugares"
- Acompanhamento diário da pesquisa do 4º lançamento, leitura 1: "Marco cruzado: 3.000. A pesquisa já tem
  massa pra guiar copy."
- `sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §6: "sai como rotina: a qualificação já
  entra no relatório de tráfego, casada por e-mail"
- `banco-angulos.md` da Black do caso-base: "erro meu nesta versão do banco, apontado pelo agente de copy
  [...] e corrigido."

---

## 4. Regras transversais

1. **Zero invenção.** Número com arquivo de origem; faltou dado, pergunta e para. No avatar não existe
   suposição plausível: o `sirius-scale/frameworks/lhto.md` §10 deixa o marcador de assumido liberado só
   pra decisão de forma, nunca pra dor, número, depoimento ou preço.
2. **Leitura vem marcada como leitura.** O funil de VSL diz no topo: "Citação real vem entre aspas com a
   origem. Leitura minha vem marcada como leitura."
3. **Dado pessoal fica no CSV de `dados/`.** O avatar mostra agregado e frase sem nome. A planilha da
   pesquisa tem nome, e-mail e WhatsApp (`sirius-scale/frameworks/trafego/leitura-dash-facil.md`).
4. **Número que vai pra peça sai da tela do Dash.** "Cruzamento próprio serve pra entender o padrão e
   decidir o ângulo — nunca pra virar o número falado." (regra da casa).
5. **Escopo de cada base sempre dito** (lead, comprador do ingresso, comprador do produto, aluno).
6. **Base de lançamento anterior informa ângulo, não decide verba.** "Conversão de venda de um lançamento
   passado pode informar ângulo de copy e prioridade de teste, mas não decide se um criativo sobe ou desce
   verba hoje." (regra da casa).
7. **Sem pesquisa em volume, sem MQL.** "Não force MQL onde não há pesquisa."
   (`sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §6).
8. **O briefing só aponta.** Dado de pesquisa mora em `pesquisa.md` e `avatar.md`
   (`sirius-scale/frameworks/lancamentos/briefing.md`, o que não vai no briefing).

---

## 5. Exemplos reais consolidados

**Retrato de um parágrafo que rastreia** (funil de VSL, `avatar.md` §1; forma do caso-base, com o conteúdo
trocado por marcador): "Trabalha e estuda nas horas vagas. Tem [escolaridade], ganha até [faixa de renda],
mira [o objetivo]." Logo abaixo: "Cada frase desse parágrafo rastreia até um corte abaixo."

**Sub-avatar reordenado pela venda** (evento pago do caso-base, camada do 3º lançamento, 5.454 respostas
cruzadas):

| Sub-avatar | Conversão | N |
|---|---:|---:|
| Tem base, já fez cursos, não é consistente | 5,76% | 799 |
| Reincidente sem método e sem resultado | 3,51% | 2.196 |
| Já domina o básico, quer o gabarito | 3,19% | 407 |
| Iniciante sem método | 2,57% | 1.792 |

O topo do mesmo arquivo, por volume, punha o iniciante como sub-avatar 1.

**Quem entra × quem paga** (cliente de perpétuo, `avatar-comprador.md` §1):

| Corte | Lead (N=316) | Comprador (N=37) |
|---|---|---|
| Já conhecia o expert | 71% há menos de 1 mês | 65% já conheciam |
| Renda | 48% na faixa mais baixa ou sem renda | 70% dos que informaram na faixa mais alta |
| Já fez curso do tema | não medido | 70% fizeram 1 ou mais |

**Dicionário em três listas** (funil de VSL, §12): "Palavras deles (usar)", "Palavras que sinalizam
objeção (endereçar, não ignorar)" e "Palavras que o script usa e eles não usam".

**Formulário que se mantém e cresce no fim** (Black do caso-base): da 1 à 13, o texto do 4º lançamento
"sem mudar uma letra nem uma opção"; a 13 é metade do MQL: "Você gostaria de ser avisado(a) quando abrir
uma nova turma do [programa]?"; a 14 é nova: "Na [nome da Black], qual destes você MAIS quer?"

**Ideia de criativo com rastro, aprovada** (lote de ideias tiradas da pesquisa de compradores do evento
pago, v2): "Ideias 1, 2 e 3 aprovadas como estavam, sem alteração." Cada ideia traz a linha de rastro
("Rastro: 42,3% (207 de 489) marcaram", na ideia 1) e o lote abre com a ressalva de escopo: "Os números
abaixo descrevem quem converteu, não a base fria."

**Resposta da pesquisa como gancho de convite**
(`sirius-scale/frameworks/lancamentos/live-de-downsell.md` §4): as 1.632 pessoas que marcaram o tema do
produto de downsell como maior dificuldade e não compraram a oferta principal foram a lista do convite do
downsell. "Só quem respondeu a pesquisa pode receber o gancho da pesquisa." E a forma: "Escrever como fato
do formulário".

**Ângulo proibido por venda** (cliente de perpétuo, banco): future pacing foi o último dos 5 hooks em
conversão (0,21%); pergunta paradoxal teve a melhor retenção da série (18,77%) e foi a 4ª em conversão
(0,38%).

---

## 6. O que transfere e o que é do caso

**Transfere (visto em mais de um cliente):**
- Registrar fonte, N, escopo e o que a base não mede (§3.3).
- Cruzar pesquisa com venda e tratar célula pequena como direção (§3.4; casamento por e-mail em 2 clientes).
- Separar quem entra de quem paga, e escrever no arquivo qual peça fala com qual (§3.5).
- Contar a língua das abertas, comparar lead com comprador e usar verbatim só com origem e contexto (§3.8).
- Emprestar base declarando, marcar camada de confiança, conferir material pronto contra a venda (§3.10).
- A estrutura do banco: regra de uso, ângulo com rastro, frases rastreáveis, o que não usar (§3.11; 2 clientes).
- Responder a pesquisa marca quem compra (caso-base), o que faz da taxa de resposta uma alavanca (§3.1).
- As famílias de pergunta da §3.2 se repetem nos formulários de 3 donos. A origem dos formulários não está
  registrada (Pontos em aberto, item 2), então transferem como lista do que já apareceu, não como formulário.

**É do caso:**
- A régua de MQL do caso-base (duas perguntas) e os 27% de qualificado.
- **Já ter comprado curso do problema como o melhor separador de comprador.** No caso-base repetiu no 2º
  e no 3º lançamentos, no segmento do funil de VSL e no muro do 4º. Fora dele não se confirmou: no segundo
  cliente, 6 dos 9 compradores nunca tinham investido. O
  `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §6 chama isso de "hipótese forte pra testar
  primeiro, não regra pronta". Os dois sinais contra não fecham a questão (9 compradores), mas pedem medir
  antes de usar.
- O tamanho do efeito de responder (3,5x no 3º lançamento) e os 60% a 80% de resposta que o Rodrigo relata
  na operação dele.
- O texto e as opções das 13 perguntas do caso-base.
- O tema do produto de downsell fora da captação do caso-base (o criativo de topo com esse ângulo zerou
  vendas no 3º lançamento).
- Os dois vocabulários do cliente de perpétuo, a divisão por ponto da relação da Black (colheita) e o eixo
  do método da Black.
- Toda conversão por área, renda ou escolaridade.

---

## 7. Pontos em aberto

1. **Pesquisa Inteligente fora do kit** (§0). Tudo aqui pode mudar quando ela entrar no método da casa.
2. **Quem escreveu os formulários.** As 13 perguntas do caso-base e as do segundo cliente têm famílias
   parecidas; não há registro de onde vieram. Se forem do método externo, a §3.2 vira citação dele.
3. **N mínimo.** Não existe regra da casa. O que existe: célula com menos de 10 compradores é direção; o 4º
   lançamento do caso-base marcou 3.000 respostas como massa pra guiar copy (**VARIAÇÃO ISOLADA**); o
   cliente de perpétuo tratou 37 compradores como inconclusivo por corte e suficiente quando os cortes
   apontavam pro mesmo lado.
4. **Já comprou e não resolveu, fora do caso-base** (§6). Hipótese a medir no próximo cliente com pergunta
   igual e mais compradores.
5. **Presente pra quem responde**: usado no caso-base, efeito na taxa de resposta nunca medido.
6. **Nenhum banco tem venda por ângulo**, fora o do cliente de perpétuo (5 hooks). O do evento pago se
   declara matéria-prima; o da Black só terá número depois do fechamento.
7. **Persona com nome**: nenhum avatar escrito pela casa usa nome de pessoa; o que veio pronto do projeto
   do segundo cliente usa. Não há decisão registrada.
8. **Contradição viva: um segmento profissional.** A camada de conversão do evento pago corrigiu: "A flag
   era de outra base e não se sustenta neste N." O banco do evento pago (Bloco F) e o avatar da Black
   seguem com a flag; o da Black diz "historicamente convertem pouco — não priorizar". O
   `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §3.6 também mostra esse segmento acima de
   outros dois.
9. **O 4º lançamento do caso-base rodou sem `pesquisa.md` e `avatar.md` próprios**; o briefing lista os
   dois como pendentes. Não está escrito se era o combinado (empréstimo, §3.10) ou se ficou faltando.
10. **A Black seguinte do segundo cliente**: qual avatar usar (o do último lançamento, o da Black anterior
    ou pesquisa própria na captação) é decisão pendente do Rodrigo e trava a copy.
11. **Duas versões da pesquisa na mesma planilha** (aluno e não aluno, Black do caso-base): conserto não
    fechado.
12. **Tema novo nas abertas durante a captação**: na casa, a leitura diária saiu como rotina e a
    qualificação foi pro relatório de tráfego, que lê a pesquisa só pra regra de MQL. A varredura de tema
    novo nas abertas não está em nenhuma rotina do padrão novo.
13. **Desejo de quem compra × desejo mais citado** (§3.7): 1 caso. Precisa de mais casos pra virar padrão.
