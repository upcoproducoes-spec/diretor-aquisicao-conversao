# Extração de framework dos Projects do claude.ai

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Prompt de mão única pra rodar **onde o trabalho real de vocês mora**: dentro de
cada Project no claude.ai, numa conversa que tem o histórico do trabalho, ou
aqui no Claude Code, em cima das pastas `entregas/`, `lancamentos/` e `funis/`.
Serve pra transformar o que vocês já produziram e aprovaram em framework de
vocês, em `frameworks-da-casa/`, e pra trazer pro Claude Code o que ficou em
Projects antigos. É o mesmo método que a casa usou pra escrever boa parte de
`sirius-scale/frameworks/` a partir do trabalho dela.

Como usar:

1. Abre o Project (ou a conversa, ou a pasta aqui no Claude Code). Cola o
   prompt inteiro (as duas fases juntas — a trava faz ele parar sozinho na
   fase 1).
2. Lê a tabela. Responde com os artefatos que quer, por nome ou número.
3. Ele entrega um documento por mensagem. Passa cada um pelo checklist de aceite
   no fim deste arquivo.
4. Salva em `frameworks-da-casa/<tipo>/<slug>.md` (o tipo é `copy`,
   `lancamentos`, `design` ou o que fizer sentido pra vocês) e adiciona uma
   linha no `CLAUDE.md` de vocês: o que o framework cobre, onde ele está e o
   alcance do cabeçalho. **Nunca** salva em `sirius-scale/`: a atualização do
   kit troca essa pasta inteira e apagaria o arquivo (`sirius-scale/REGRAS.md`
   §4).
5. Repete em cada Project (ou conversa) onde houver trabalho real.

Se o mesmo artefato aparecer em dois Projects, roda a fase 2 uma vez só, colando
as duas bases juntas — o que se repete nos dois ganha lastro de verdade pra
CONSISTENTE (quem confirma é quem é dono da operação).

---

## O PROMPT

---INÍCIO---

Você vai me ajudar a transformar o trabalho que já existe aqui (copy,
criativo, página, lançamento) em frameworks reutilizáveis. Isso é
reverse-engineering do que foi realmente produzido aqui — não é aula de copy,
não é boas práticas de mercado, não é o que você sabe sobre o assunto. Se uma
regra não está sustentada por peça real deste Project (ou desta conversa, ou
destas pastas), ela não entra em lugar nenhum.

O trabalho tem duas fases. Você vai executar a FASE 1 e PARAR. Não comece a
escrever framework nenhum antes de eu responder.

## FASE 1 — inventário

Varre este Project inteiro (ou a conversa, ou as pastas que eu indicar):
- todos os arquivos anexados
- todas as conversas, incluindo trabalho que ficou só no chat e nunca virou
  arquivo
- versões que eu reescrevi ou aprovei valem mais como evidência que a primeira
  versão que você tinha proposto

Agrupa por artefato, não por tema. Artefato é a peça que alguém vai reproduzir
depois. Artefatos distintos, por exemplo:
- roteiro de CPL (aula 1, 2 e 3 são etapas do mesmo artefato, não artefatos
  diferentes)
- roteiro de live de aquecimento
- pitch de fechamento
- página de captura / de vendas / de obrigado (cada uma é um artefato)
- sequência de e-mail (aquecimento, carrinho aberto, carrinho fechando)
- disparo de WhatsApp ou Telegram
- criativo estático de captação (evento gratuito)
- criativo estático de venda de ingresso (evento pago)
- criativo em vídeo / reels
- roteiro de VSL, script de stories, headline de anúncio

Regra dura: não junte artefatos diferentes só porque o assunto é o mesmo.
Criativo de captação e criativo de venda de ingresso são frameworks separados.
Estático e vídeo são frameworks separados. Na dúvida, separa e me avisa.

Pra cada artefato encontrado, me devolve numerado:

1. Nome do artefato
2. Quantas unidades distintas existem (conta peça a peça: 12 estáticos = 12
   unidades; 6 aulas de CPL = 6 unidades)
3. Onde estão — arquivo anexado (qual) ou conversa (qual)
4. De quantos lançamentos (ou funis) e de quantos produtos vem essa base
5. Passou por reescrita ou aprovação minha? sim / não / parcial
6. Tem resultado registrado aqui (CPL, conversão, faturamento)? sim / não
7. Veredito, com esta régua:
   - EXTRAÍVEL FORTE — 8+ unidades OU 2+ lançamentos/produtos diferentes
   - EXTRAÍVEL COM RESSALVA — 5 a 7 unidades, um lançamento só. Dá pra escrever,
     mas o documento vai declarar que nasceu de uma execução só
   - FRAGMENTO — menos de 5 unidades. Não vira framework agora
   - CONTAMINADO — a maior parte é material que você gerou e eu nunca revisei.
     Sinaliza, não extrai
8. O que falta pra subir de nível (ex: "com mais um lançamento vira FORTE")

Formato: tabela ranqueada do mais extraível pro menos, e embaixo um parágrafo
curto por artefato EXTRAÍVEL explicando a base de evidência.

Proibições nesta fase:
- Não inventar artefato que não está aqui. Se não tem copy de e-mail neste
  Project, a resposta é "não tem copy de e-mail neste Project"
- Não contar a mesma peça duas vezes porque apareceu em duas conversas.
  Deduplica e diz que deduplicou
- Não estimar número "aproximado" pra parecer mais volumoso. Conta o que dá pra
  contar e declara o que não deu

Termina a FASE 1 com: qual você extrairia primeiro e por quê. Depois PARA e
espera minha resposta. Eu vou te dizer quais números quero.

## FASE 2 — só depois do meu OK

Quando eu escolher, você escreve um documento por mensagem, na ordem que eu
pedir. Não emenda dois no mesmo texto. Se eu pedir três, entrega o primeiro e
pergunta se pode seguir.

São **dois eixos independentes**, e confundir os dois é o erro clássico aqui:
força do padrão conta repetições DENTRO da base (lançamentos ou peças); alcance
diz de que negócio a base vem. Um padrão pode ser fortíssimo dentro de um
lançamento e nunca ter rodado em outro — as duas coisas são verdade ao mesmo
tempo.

**Eixo 1 — FORÇA DO PADRÃO (dentro da base).** Conta lançamentos ou peças.
Marca TODO elemento com um destes, e a marcação vai no próprio título da seção:
- PADRÃO CONSISTENTE — se repetiu em 3 ou mais (lançamentos ou peças), de
  preferência em mais de uma fonte. É regra **dentro desta base**. Escreve
  "PADRÃO CONSISTENTE (proposto)": quem tira o "(proposto)" é quem é dono da
  operação, depois de ler e dar o ok, nunca você. Até lá, vale como VARIAÇÃO
  ISOLADA
- VARIAÇÃO ISOLADA — aparece em 1 ou 2 unidades. Só se o contexto pedir
- PADRÃO INCONCLUSIVO — tem sinal, mas a base não sustenta. É hipótese a testar,
  e tem que estar declarada como hipótese

**Eixo 2 — ALCANCE.** Vale pro documento inteiro, vai no cabeçalho, não no
título de cada seção:
- DA CASA — a base é o negócio de quem está colando este prompt. É o alcance de
  todo framework que sai daqui. Junto dele, o cabeçalho diz de quantos
  lançamentos e de quantos produtos a base veio, e quais (ex.: "DA CASA —
  1 lançamento (<qual>)")
- UNIVERSAL — não tem dimensão de negócio (fato de plataforma: campo de API,
  limite de orçamento, margem de formato). Não precisa de eixo 1

⚠️ CONSISTENTE **não** quer dizer "vale pra qualquer lançamento". Quer dizer
"se repetiu dentro desta base". Três peças do mesmo lançamento dão
CONSISTENTE, mas não dizem nada do próximo lançamento: por isso o cabeçalho
diz de quantos lançamentos a base veio.

Estrutura de cada documento, nesta ordem:

1. Título: "Framework — <artefato> (<contexto>)" e, logo abaixo, uma linha
   dizendo de onde foi reverse-engineered e qual a base

2. Escopo e base de evidência
   - O que foi analisado: as fontes com apelido (Fonte A, Fonte B...), o que cada
     uma contém e quantas unidades
   - O que foi excluído de propósito e por quê (artefato diferente, framework
     diferente, material não revisado)
   - Ressalva estrutural: quantos lançamentos e quantos produtos formam a base.
     Se é um só, escreve com todas as letras

3. A fórmula, em ordem — o esqueleto da peça em passos numerados, do começo ao
   fim. Se existem modos que se repetem (ex: modo dor x modo informativo),
   declara os modos aqui e diz o que eles compartilham

4. Cada etapa detalhada — uma subseção por etapa, e dentro dela sempre estes
   quatro blocos:
   - O que entra
   - Por quê (a função da etapa na peça, não elogio)
   - Variações aceitáveis
   - Trecho real — copiado literal da fonte, entre aspas, com a fonte
     identificada

5. Regras transversais — o que vale pra peça inteira: tom, tamanho, o que nunca
   aparece, o que eu cortei toda vez que apareceu

6. Exemplos reais consolidados — peças completas ou trechos-chave, verbatim,
   agrupados por ângulo ou tipo, cada um com a fonte

7. O que é reutilizável e o que é do caso — separa o que funciona em qualquer
   lançamento do que só funciona nesse público, nesse produto ou nessa oferta

8. Pontos em aberto — o que a base não respondeu, o que precisa de mais um
   lançamento pra confirmar, e as hipóteses INCONCLUSIVAS reunidas

Regras de escrita:
- Português brasileiro informal e direto
- Zero linguagem de IA: nada de "não é apenas X, é Y", "mergulhe", "eleve",
  "desvende", frase de efeito, adjetivo empilhado
- Todo trecho citado é verbatim. Se não consegue copiar literal, não cita. Nunca
  escreve exemplo "ilustrativo" — isso é alucinação com outro nome
- Se faltou base pra fechar uma etapa, escreve "não há evidência suficiente" e
  joga pra Pontos em aberto. Não preenche buraco com suposição
- Quantifica sempre que der: "aparece em 9 das 12 unidades" vale mais que "quase
  sempre"
- Nenhum dado pessoal: nome de aluno ou de lead, e-mail, telefone, CPF. Depoimento
  entra pelo padrão que ele prova, não pela pessoa

Entrega cada documento como um bloco único de markdown, pronto pra salvar como
arquivo, e sugere o nome no padrão frameworks-da-casa/<tipo>/<slug>.md

Começa pela FASE 1.

---FIM---

---

## Checklist de aceite (antes de salvar em `frameworks-da-casa/`)

Recusa e manda refazer se qualquer item falhar:

1. Toda seção tem nível de confiança marcado no título. (Não precisam: escopo e
   base, excluído de propósito, fórmula, regras transversais, exemplos, o que
   transfere e pontos em aberto.)
2. Todo trecho citado é verbatim e tem fonte identificada. Não reconheceu a
   frase? Provavelmente foi inventada — confere na origem. Na casa de origem
   isso virou um script; aqui a conferência é manual e **não é opcional**. Peça
   ao Claude: "pra cada citação entre aspas deste framework, abra a fonte
   indicada e procure a frase palavra por palavra; liste as que não achou".
   Como conferir:
   - espaço, quebra de linha, negrito/itálico e aspas curvas não contam como
     diferença; reticências partem a citação em pedaços, e cada pedaço tem que
     existir na fonte;
   - texto entre colchetes dentro da citação ([o produto], [sic]) é de quem
     cita, não da fonte; código entre crases não é citação;
   - a fonte é o material de origem (peça, conversa, pesquisa, ata), nunca
     outro framework novo da mesma rodada: confira os arquivos novos juntos,
     pra um não validar a citação do outro;
   - citação não achada sai, ou volta pra frase exata da fonte. Sem todas
     achadas, não salva;
   - na mesma passada, nenhum dado pessoal: nome de aluno ou de lead, e-mail,
     telefone, CPF, CNPJ, token.
   A conferência não pega regra escrita sem aspas que ninguém fez: isso
   continua sendo leitura (item 6).
3. A ressalva de base (quantos lançamentos, quantos produtos) está explícita, e
   o alcance (eixo 2) está no cabeçalho, nas primeiras linhas do arquivo.
4. Tem seção de "excluído de propósito". Se não tem, o modelo misturou artefato.
5. "Pontos em aberto" tem coisa de verdade dentro. Documento sem ponto em aberto
   é documento que fingiu certeza.
6. Nenhuma regra genérica de copy de internet entrou como se fosse padrão de
   vocês.
7. Leu em voz alta e não soou como IA (`sirius-scale/REGRAS.md` §1; o
   `/humanizer` ajuda a achar o que passou batido).

Depois do checklist, rode o `/revisar` no framework novo, com olhos frescos:
quem escreveu valida as próprias suposições sem perceber
(`sirius-scale/REGRAS.md` §5).

## Quando um framework vira "forte"

Framework nascido de um lançamento carrega a ressalva no topo pra sempre. Quando
o mesmo artefato for executado num segundo lançamento, roda a fase 2 de novo com
as duas bases e reescreve.

O alcance continua `DA CASA`. O que muda no cabeçalho é a base declarada: sai
`DA CASA — 1 lançamento (<primeiro>)`, entra `DA CASA — 2 lançamentos
(<primeiro>, <novo>)`. O eixo 1 (força) é recalculado sobre a base somada,
contando lançamentos ou peças — o que se repetiu nos dois segue CONSISTENTE
(proposto), agora com lastro de verdade; o que apareceu só num cai pra VARIAÇÃO
ISOLADA e ganha a etiqueta de qual lançamento. Tirar o "(proposto)" continua
sendo decisão de quem é dono da operação.

E a seção "o que transfere e o que é do caso" é reescrita: ela era hipótese
(você *supôs* o que ia transferir) e agora vira medida (você *viu*). Se algo
que estava listado como transferível não transferiu, isso é achado — registra
com todas as letras em vez de apagar em silêncio.

## O que a casa aprendeu extraindo

1. **Evidência tem peso.** Forte é o que rodou, foi aprovado ou foi decidido
   por quem manda; média é o que foi entregue sem aprovação; fraca é rascunho.
   FRAGMENTO não vira arquivo.
2. **CONSISTENTE sai como "(proposto)"** até quem é dono da operação ler e dar
   o ok. Até lá, vale como VARIAÇÃO ISOLADA.
3. **Decisão do dono é regra naquele lançamento, não CONSISTENTE automático.**
   Rotular decisão como CONSISTENTE subiu de força quatro regras que a casa
   tinha como ISOLADA, e a revisão pegou.
4. **A base é o que vocês executaram.** A força conta lançamento ou peça de
   vocês; material de mentoria ou de programa de terceiro não conta como base
   de vocês.
5. **A fala "literal" das notas pode estar corrigida.** Cite a transcrição ou
   a peça original, não a nota de quem resumiu.
6. **Framework antigo corrigido se confere antes e depois:** o número de
   citações não achadas não pode subir.
7. **O que a evidência não fecha vira pergunta**, numerada, pra quem decide
   responder em uma linha.
