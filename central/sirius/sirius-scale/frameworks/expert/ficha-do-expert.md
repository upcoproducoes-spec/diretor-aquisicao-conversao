# Framework — Ficha do expert (expert/dna-expert.md, expert/brand.md e expert/produtos/<produto>.md)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered dos 7 DNAs, 6 `brand.md`, 4 arquivos de identidade e 30 fichas de produto que a casa montou em cerca de dois meses, de 5 clientes e 3 marcas próprias, e da fala do Rodrigo em duas calls.

Do lado de vocês, os três arquivos moram em `expert/`: `expert/dna-expert.md`, `expert/brand.md` e uma ficha por produto em `expert/produtos/<produto>.md`. Os modelos em branco estão em `sirius-scale/modelos/dna-expert.md`, `sirius-scale/modelos/brand.md` e `sirius-scale/modelos/produto.md`. Os modelos têm o mínimo; este arquivo diz o que vai em cada parte e o que a casa acrescentou na prática.

> **ALCANCE: TESTADO EM 5 CLIENTES (proposto), como montagem de arquivo.** Cinco clientes, de mais de uma
> empresa da casa, mais 3 marcas próprias (a pessoal do Rodrigo, uma empresa dele e a marca da casa). O que se
> repete entre eles está marcado em cada seção; o que apareceu num só leva o caso. Mexer no alcance é decisão
> do Rodrigo, e a ressalva pesa: a ficha foi montada nos 5, mas só no caso-base ela rodou de verdade. Nos
> outros quatro ela existe e rodou pouco.
>
> Contagens e rótulos são os da base completa da casa; alguns dos casos não aparecem neste kit.
>
> **O que não está testado:** o efeito da ficha na copy. Ninguém mediu peça escrita com DNA contra peça
> sem DNA. A prova é de uso (arquivos que citam o DNA, por busca do nome do arquivo no fim da montagem: 146
> no caso-base e de 0 a 9 nos outros donos) e a fala do Rodrigo sobre o que acontece quando o expert lê a
> copy.
>
> **Quem escreveu o quê:** quase todo o texto das fichas foi o Claude da casa que montou, lendo o material
> do cliente. Do Rodrigo são as travas e as decisões datadas que estão dentro delas, e a descrição do método
> nas duas calls. Por isso as seções que dão consistente vêm marcadas "(proposto)": promover é decisão dele
> (`sirius-scale/REGRAS.md` §4).
>
> **Vizinhos, que este arquivo cita e não repete:** `CLAUDE.md` de vocês (quem é quem, produtos,
> ferramentas); `.claude/agents/copy.md` (o que o `copy` exige e o que faz quando falta);
> `sirius-scale/frameworks/lancamentos/briefing.md` (o que é do lançamento);
> `sirius-scale/frameworks/lancamentos/roma-e-promessa.md` (promessa, Roma, entregável × bônus);
> `sirius-scale/frameworks/oferta-14-secoes.md` (arquitetura da oferta);
> `sirius-scale/frameworks/design/impresso-editorial.md` (TASTE de material impresso);
> `.claude/agents/designer.md` (qual identidade vale na arte).

## 0. O que é a ficha e por que ela vem antes da primeira copy — PADRÃO CONSISTENTE (proposto)

São três arquivos estáveis no topo da pasta do expert (`expert/`): o DNA (voz, história, crenças, regras de fala), o brand (identidade visual que vale entre eventos) e uma ficha por produto. Todo agente que produz lê pelo menos um deles antes de começar: o `copy` lê o DNA e o produto; o `designer`, o brand; o `webdesigner`, o `gestor-trafego` e a skill `/mapa-edicao`, os três; e o `/revisar` confere a peça contra eles.

O que o DNA é, nas palavras do Rodrigo, na call de começo de projeto com o cliente D (01:15:47 e 01:16:17):

- "Porque é bom a gente criar um DNA do expert, que é um documento que fala tudo sobre ele."
- "Mas então, eu crio um documento que é o DNA do Expert, que é o que vai guiar toda a copy, deixar do jeito que ele fala, vai ficar bem parecido com o jeito que ele fala, e ele vê que na hora de ler a copy, ele fala, pô, parece que você nunca escrevi."

E o efeito que ele espera, numa call com dois lançadores de fora, duas semanas depois (00:20:00): "então a gente cria aí DNA do expert aí a cópia sai bem do jeito que ele fala é assim que eu faço com os experts aí o expert começa a ler e parece que tá naturalzão porque usa os termos que ele já usa".

**Vem antes da copy.** Nos três clientes que já entraram com a pasta montada pela casa, a ficha nasceu junto com a pasta, antes de qualquer peça. Nos dois que vieram de projeto anterior no claude.ai (o caso-base e o cliente B) já existia um DNA lá, que virou fonte do daqui; no cliente B, a ficha da casa foi montada antes da primeira copy da Black. No cliente D a pendência ficou na ata como "montar a base de copy (DNA do expert) a partir da planilha de reels, antes de escrever copy", e a fala foi "primeiro eu vou criar a base dele aqui, das copies primeiro, para daí começar a ser copy boa, senão vai sair qualquer coisa" (01:33:24; a transcrição automática atribui essa linha a outra pessoa da call, mas a ata põe a pendência no nome do Rodrigo, e quem cria a área citada na mesma frase é ele).

O agente para sem ela: faltou DNA, produto, pesquisa ou avatar, o `copy` para e pergunta (`.claude/agents/copy.md`). E o Rodrigo cobra o uso: "você tá usando o dna da [expert]? e passou a skill humanizer?" (correção registrada no caso de origem).

## 1. Escopo e base de evidência

### Fontes

| Fonte | O que contém | Unidades |
|---|---|---|
| **A. O caso-base** (educação, nicho de concurso) | `dna-expert.md`; `brand.md`; a identidade visual de 3 lançamentos (um pago, um gratuito e a Black); 15 fichas de produto; o DNA anterior, de um projeto no claude.ai, guardado sem edição | 1 DNA + 1 anterior, 1 brand + 3 identidades, 15 fichas |
| **B. Um segundo cliente** | `dna-expert.md` e 7 fichas, montados em cima do zip do projeto dele no Claude; o DNA anterior, sem edição | 1 DNA + 1 anterior, 7 fichas, sem brand |
| **C. Um terceiro cliente** (um nicho técnico, de outra empresa da casa) | `dna-expert.md`, `brand.md`, 2 fichas e o arquivo geral do projeto, montados de 43 documentos do Drive (um deles era um DNA anterior, que não foi guardado) | 1 DNA, 1 brand, 2 fichas |
| **D. Um quarto cliente** (um nicho técnico) | `dna-expert.md` (medido em 317 reels) e o arquivo geral do projeto | 1 DNA, sem brand, sem ficha |
| **E. Marcas próprias** | a pessoal do Rodrigo (`dna.md`, `brand.md`); uma empresa dele (DNA dos fundadores, `brand.md`, 4 fichas de oferta, a identidade de um produto); a marca da casa (`brand.md`) | 2 DNAs, 3 brand, 1 identidade, 4 fichas |
| **F. Fala e decisão do Rodrigo** | as duas calls e as decisões datadas que estão dentro dos arquivos A a E (exemplos na §8) | 2 calls |
| **G. Correções do Rodrigo registradas na casa** | material do expert é intocável; validação do expert só com o que é dele; decisão tomada na tarefa entra no arquivo; preço mudou, propaga; procurar no Drive antes de dizer que não existe; peça real aprovada antes de estilo; o `/humanizer` roda de verdade depois do `copy`; depoimento em arte só com print real | 8 |
| **H. Quem lê** | os agentes e skills da §0, e as peças que citam o DNA | 146 arquivos no caso-base; de 0 a 9 nos outros donos |

Somando: 7 DNAs (7 pessoas com voz registrada), 2 DNAs anteriores, 6 `brand.md`, 4 arquivos de identidade de lançamento ou produto e 30 fichas de produto.

**Peso de cada fonte.** Forte: a fala do Rodrigo (F), as decisões dele gravadas nos arquivos e as correções registradas (G). Média: as fichas do caso-base e da empresa da casa, citadas por peças que o Rodrigo revisou ou gravou (uma VSL do caso-base, revisada por ele; criativos da empresa da casa, gravados por ele), e a do cliente C, citada pela direção de VSL e de criativos, que ainda tem decisões pendentes. Nenhuma ficha teve aprovação formal dela mesma. Fraca: as fichas do cliente B (recentes, ainda sem peça) e o DNA do cliente D (que se declara não validado).

### Veredito da base (FASE 1 de `sirius-scale/frameworks/_extracao-de-frameworks.md`)

| Artefato | Unidades | Clientes | Passou pelo Rodrigo? | Resultado registrado? | Veredito |
|---|---:|---|---|---|---|
| DNA do expert | 7 (+2 anteriores) | 5 + 2 marcas próprias | parcial: decisões dele dentro do DNA do caso-base, do dele e do da empresa da casa; respostas dele no do cliente C; nenhum DNA de cliente validado inteiro pelo expert | não; uso, sim | **EXTRAÍVEL FORTE** |
| `brand.md` e identidade | 6 + 4 | 3 clientes + 3 marcas | parcial: a cor do produto principal (decisão do Rodrigo), a identidade da Black (reunião e pedido da gerente de operação), a regra de uma cor proibida | não | **EXTRAÍVEL FORTE** |
| Ficha de produto | 30 | 4 clientes + a empresa da casa | parcial: preço, nome e bônus decididos por ele em várias | vendas reais dentro de 10 fichas | **EXTRAÍVEL FORTE** |

Por que não é CONTAMINADO: as travas centrais (fala espontânea como fonte, zero invenção, o dono trava o número, a plataforma vence o roteiro, decisão volta pro arquivo) saem de fala ou decisão do Rodrigo e de correção dele. O que só a prática repetida da casa sustenta está dito na seção. O que falta pra subir de nível: um expert de cliente ler e aprovar o próprio DNA, e alguma medida de efeito na copy.

### Excluído de propósito

- `pesquisa.md` e `avatar.md`: mudam a cada lançamento e são outro framework (`sirius-scale/frameworks/pesquisa/pesquisa-e-avatar.md`). O "para quem" e o "quem comprou" que aparecem dentro de algumas fichas ficam com ele.
- `briefing.md` e o bloco `fontes:` dele: `sirius-scale/frameworks/lancamentos/briefing.md`.
- O que é promessa, Roma, mecanismo e entregável × bônus: `sirius-scale/frameworks/lancamentos/roma-e-promessa.md` e `sirius-scale/frameworks/lhto.md`. Aqui entra só onde a ficha guarda isso.
- Arquitetura de oferta (`sirius-scale/frameworks/oferta-14-secoes.md`), inclusive a de um produto do próprio Rodrigo, montada pelas 14 seções, que não é ficha de produto vendido.
- Como a copy usa o DNA (credencial uma vez por peça, primeira pessoa, verbatim com contexto): `.claude/agents/copy.md`, `sirius-scale/frameworks/copy/criativos.md` §0, `sirius-scale/frameworks/oferta-14-secoes.md` §4. Cito quando a regra mora dentro do DNA.
- Criar identidade nova (o kit visual de um produto de IA da casa, as direções da Black): é design (`.claude/agents/designer.md`, `sirius-scale/frameworks/design/impresso-editorial.md`). Aqui entra só o registro do que foi aprovado.
- Conhecimento técnico do expert guardado junto das fichas (os critérios e a calibração de uma ferramenta de IA): base de produto de IA, outro artefato (não faz parte deste kit).
- Os blocos próprios da linha de produtos de entrada dentro das fichas (régua, validação, nome na página): `sirius-scale/frameworks/lancamentos/low-ticket.md`.
- Audiência, pilares e destinos da marca pessoal do Rodrigo: `sirius-scale/frameworks/conteudo/conteudo-que-alimenta-o-funil.md`.

### Ressalva estrutural da base

- 5 clientes, de mais de uma empresa, e 3 marcas próprias, mas o peso é desigual: o caso-base concentra quase todo o uso e quase todas as decisões. Nos outros quatro a ficha existe e rodou pouco.
- Nenhum DNA de cliente foi lido e aprovado inteiro pelo expert. O do cliente D diz isso de si mesmo.
- Nenhuma medida de efeito. O "parece que tá naturalzão" é a experiência do Rodrigo, não um número.

## 2. A fórmula, em ordem

1. **Juntar a fala real e marcar de que tipo ela é** (§3).
2. **Abrir o arquivo com fontes, data, a regra e o cuidado de leitura** (§4).
3. **Escrever o DNA, seção por seção** (§5).
4. **Escrever o `brand.md` só com o que é estável** e mandar o que muda pro arquivo do evento ou do produto (§6).
5. **Escrever uma ficha por produto** (§7).
6. **Travar o dado que diverge** (§8).
7. **Manter vivo:** decisão nova entra no arquivo de origem, com data (§9).
8. **Separar o que vai pro expert confirmar, o que se combina com ele em conversa e o que não vai pra aprovação dele** (§10).

Dois modos usam o mesmo esqueleto:

- **Expert de cliente** (os cinco clientes): o material dele é a fonte e a lacuna vira pergunta.
- **Marca própria** (E): o que é posicionamento não sai de arquivo. O `brand.md` do Rodrigo abre com "Posicionamento de marca pessoal não se deriva de arquivo — sai de decisão." e deixa a essência como decisão pendente, com os candidatos que o material sustenta e o risco de cada um. VARIAÇÃO ISOLADA (1 arquivo).

Os dois compartilham: fonte declarada, zero invenção, lacuna escrita e decisão com data.

## 3. Passo 1 — Juntar a fala real e marcar de que tipo ela é — PADRÃO CONSISTENTE (proposto)

**O que entra.** Primeiro, tudo em que o expert fala sem ler copy nossa: aula gravada, live, reel sem roteiro, transcrição. Depois, o que foi escrito pra ele gravar (roteiro de aula, CPL, VSL), o texto oficial dele (bio, página) e análises feitas antes em outro projeto. Cada fala que entra no DNA leva a marca de onde veio.

**Por quê.** O DNA existe pra copy soar como ele. Roteiro escrito por nós ensina a nossa voz, não a dele. E transcrição automática erra nome, termo técnico e número: serve pra pegar o jeito de falar, não pra citar.

**Variações aceitáveis.**
- Fonte grande (centenas de aulas ou reels): conta a frequência dos bordões. Fonte pequena (três lives, um script, um documento): lista sem contar e diz isso no arquivo (§5.5).
- Já existe um DNA feito em outro lugar: entra como fonte, não como verdade. O original fica guardado sem edição e o arquivo da casa é montado por cima, com o que envelheceu marcado (o caso-base e o cliente B guardam o original; o do cliente C não foi guardado). Do lado de vocês: o original fica numa subpasta de originais dentro de `expert/`, e o `expert/dna-expert.md` é montado por cima.

**Trecho real.**
- Rodrigo, na call de começo de projeto: "Por exemplo, se tiver vídeo dele dando aula ou transcrição dessas aulas." e "Então, para isso, precisa ter alguns vídeos, principalmente se ele estiver mais natural, sem estar seguindo uma copy."
- Caso-base, aviso de leitura do DNA: "a maioria das falas abaixo vem de ROTEIROS escritos para a [expert] gravar (CPLs, criativos)". Depois de baixar as 136 aulas do programa principal: "Base 23× maior que a original." e "Nenhum número abaixo foi contradito pela base maior; todos subiram de ISOLADA pra CONSISTENTE."
- Cliente D: contado em "317 reels com fala longa e sem legenda de carrossel"; sobre a transcrição: "Serve pra captar o jeito de falar, nunca pra citar de volta sem conferir o vídeo."
- Cliente B: os roteiros de aulas antigas entram como "a fonte mais próxima da fala dela".
- Rodrigo, marca própria: a VSL dele é "a melhor base que existe".
- DNA anterior, no leia-me dos documentos-base do cliente B: "Os arquivos estão aqui sem edição" e "As versões que os agentes leem foram montadas em cima deles e corrigem o que está velho".

**Contagem.** Fala gravada (aula, live, reel, VSL) é a base declarada em 5 dos 7 DNAs; o do cliente C e um da empresa da casa saem de documento escrito sobre eles. A origem de cada trecho vem marcada em 5 dos 7.

## 4. Passo 2 — Cabeçalho com fontes, data, a regra e o cuidado de leitura — PADRÃO CONSISTENTE (proposto)

**O que entra.** No topo: de onde saiu cada parte e quando foi lida; a regra do arquivo (zero invenção; campo sem dado fica `não encontrado` ou `a definir`); e o cuidado de leitura que o próximo agente precisa saber antes de usar (transcrição automática, roteiro × fala, nada validado pelo expert, regra de publicidade do nicho).

**Por quê.** Quem lê depois é um agente sem a conversa. Se o arquivo não diz de onde veio e o que não foi conferido, a frase vira fato na peça seguinte.

**Variações aceitáveis.** `não encontrado` (procurou e não achou) e `a definir` (depende de decisão do dono) são estados diferentes; o DNA do Rodrigo usa os dois.

**Trecho real.**
- Caso-base: "Regra deste arquivo: zero invenção. Campo sem dado real". A mesma linha, com pequena variação, está em mais quatro DNAs e no `brand.md` da marca da casa.
- Cliente D: "É retrato do que ele já publicou, não declaração dele."
- Cliente B: "o que estava desatualizado ou em conflito vem marcado com" um sinal de alerta no próprio texto.

**Contagem.** Fontes no cabeçalho em 7 de 7 DNAs e em 28 de 30 fichas de produto. A regra de zero invenção escrita em 5 de 7 DNAs e em 26 de 30 fichas (contagem por busca de termo, não leitura linha a linha).

**`não encontrado` diz onde procurou (PADRÃO CONSISTENTE, proposto; 4 clientes).** A regra é do Rodrigo: "você tem que sempre procurar no drive. Não afirmar que não tem." (correção registrada). Nas fichas: cliente C ("Os 43 documentos do Drive do projeto não trazem nenhum ativo de marca"), caso-base ("Não há atalho: não está escrito em lugar nenhum do Project.") e cliente B, sobre os vídeos de depoimento ("procurar no Drive antes de usar").

## 5. Passo 3 — O DNA, seção por seção — PADRÃO CONSISTENTE (proposto)

Presença de cada seção nos 7 DNAs:

| Seção | Em quantos | Onde falta |
|---|---:|---|
| Como se apresenta, na fala literal | 6 | C (resumo em terceira pessoa) |
| Trajetória e credencial, só do material | 7 | nenhum |
| História | 6 (em passos numerados: 3) | D (tem casos de terceiros, não arco próprio) |
| Crenças e o que combate | 4 + 1 pendente | a empresa da casa; o do Rodrigo, pendente |
| Padrões de linguagem com exemplo real | 7 | nenhum |
| Frequência contada | 2 | os outros 5 |
| Como ensina, explica e vende | 5 | Rodrigo, empresa da casa |
| Vocabulário do nicho | 4 dos 5 clientes | — |
| O que evitar (seção própria ou lacuna declarada) | 7 | nenhum |
| Quem fala: expert, sócio, bastidor | 4 | caso-base, C, D (no D isso está no arquivo geral do projeto, não no DNA) |
| O que falta | 6 | caso-base |
| Arquétipo | 4 + 1 a definir | C |

### 5.1 Como se apresenta, na fala literal — PADRÃO CONSISTENTE (proposto), 6 de 7

**O que entra.** A frase com que ele se apresenta, verbatim, com a fonte. Quando há duas versões (aula × live, VSL × site), as duas.
**Por quê.** É a linha que abre peça e bio. Parafraseada, perde o jeito dele e às vezes o número.
**Variações aceitáveis.** Bio da página oficial; fórmula repetida com frequência medida.
**Exemplos (em molde, reescritos dos casos).** Caso-base (aula 1 do evento gratuito): "Eu sou [nome]. Há mais de [tempo] eu ajudo [o público] a [o resultado]." Cliente B (aulas antigas): "Eu sou [nome], [profissão] há mais de [tempo], especialista em [especialidade]." Cliente D: "Eu sou [nome], [profissão e especialidades]". Rodrigo: "Meu nome é [nome]. Sou [profissão] desde [ano]."

### 5.2 Trajetória e credencial, só o que está no material — PADRÃO CONSISTENTE (proposto), 7 de 7

**O que entra.** Formação, tempo de carreira e o que o credencia, cada item com a fonte. O que não tem fonte vai numa lista de "não temos".
**Por quê.** Credencial e volume de alunos são onde o material antigo mais trouxe número sem fonte (§5.10), e número sem lastro vira afirmação pública.
**Variações aceitáveis.** A credencial pode carregar regra de uso decidida pelo Rodrigo (quantas vezes por peça, conforme o tamanho da peça).
**Trecho real.** Cliente D, título da seção: "Trajetória e o que o credencia (só o que está nos materiais)", com a lista do que falta: "quantos [clientes] atendeu, tempo exato de formado". Caso-base, a regra de uso, revista na revisão de uma VSL: "pra criativos curtos faz sentido, mas não precisa ser algo cravado na pedra" (Rodrigo).

### 5.3 A história, na ordem dele — PADRÃO CONSISTENTE (proposto), 6 de 7

**O que entra.** O arco que ele conta (origem, dificuldade, virada, método), em passos e na ordem dele, com a fala de cada passo quando houver; e o que ainda não foi usado em peça nenhuma.
**Por quê.** É a parte da VSL e da CPL que só ele tem. Em passos, o roteirista não relê a fonte inteira e não reordena o que é dele.
**Variações aceitáveis.** Anotar o ativo narrativo ainda não usado; avisar quando o arco já foi gasto em peça gravada.
**Trecho real.** Cliente C: "[Um episódio da história dele] como gatilho da origem é um ativo narrativo forte e ainda não apareceu em nenhuma copy". Rodrigo: "marca pessoal que conta uma história só cansa rápido".

### 5.4 Crenças e o que ele combate — PADRÃO CONSISTENTE (proposto), 4 de 7

**O que entra.** O que ele defende e contra o quê, cada item com frase dele.
**Por quê.** Define o vilão da copy. Vilão errado ofende o próprio público: no cliente C, o vilão do funil foi escolhido "pra não invalidar nada que o lead já fez".
**Variações aceitáveis.** Quando a crença não está documentada, fica pendência, não dedução.
**Trecho real.** Caso-base, dito aqui com outras palavras: a culpa é do método (o jeito de ensinar e de estudar que o expert combate), nunca da pessoa. Cliente C, em molde: a culpa é de [o vilão: o método, a falta de ferramenta], nunca de [quem compra]. Cliente D, em molde: "[o dado técnico do nicho] é contexto", seguido dos tipos de dado que ele cita. Rodrigo, como pendência: "o que ele defende e contra o que ele se opõe, além do achismo. Não documentado."

### 5.5 Padrões de linguagem com exemplo real — PADRÃO CONSISTENTE (proposto), 7 de 7; frequência contada — VARIAÇÃO ISOLADA, 2 de 7

**O que entra.** Cada padrão (saudação, bordão, analogia, marcador de virada, fecho) com um exemplo real. Com base grande, quantas vezes aparece. Com base pequena, o aviso de que não foi contado.
**Por quê.** O exemplo mostra o padrão na boca dele; a contagem separa o que é dele do que apareceu uma vez.
**Variações aceitáveis.** O bordão pode sumir de uma amostra por escolha de tom daquele evento, sem deixar de ser dele.
**Trecho real.** Caso-base: "Padrões de linguagem específicos (com exemplo real de cada)" e a tabela "Bordões medidos (frequência real, 136 aulas do [programa principal])". Cliente D: "Medidos nos 317 reels de fala longa." Cliente B: "a lista saiu da leitura de 3 lives, sem medir. Usar como tempero, não como bordão obrigatório." A saudação do caso-base que não aparecia no evento de ingresso: "cada contexto tem a abertura que já era esperada dele".

### 5.6 Como ele ensina, explica e vende — PADRÃO CONSISTENTE (proposto), 5 de 7

**O que entra.** A sequência que ele repete pra explicar e pra vender, em passos.
**Por quê.** Em peça longa, imitar o raciocínio dele pesa mais que espalhar bordão.
**Variações aceitáveis.** Padrão de análise de caso, ordem de explicação.
**Trecho real.** Caso-base: "Pra soar como ela em peça longa (CPL, VSL, página): usar o padrão de 5 movimentos, não só espalhar bordão." Cliente C, em molde: [reconhece o que a pessoa fez] → [corrige com o porquê] → [propõe o que mudar]. Cliente D, primeiro passo: "Dá o veredito primeiro". Cliente B: "Três estruturas que ela repete".

### 5.7 Vocabulário do nicho, escrito certo — PADRÃO CONSISTENTE (proposto), 4 de 5 clientes

**O que entra.** Os termos técnicos e jargões dele na grafia certa, e o erro de transcrição conhecido ao lado.
**Por quê.** Em nicho técnico, o termo certo é parte da autoridade (regra do projeto do cliente B: "O público é técnico e pragmático: termo técnico certo dá autoridade"), e a transcrição automática erra justamente o termo: no cliente D ela "erra nome e termo"; no cliente B, dois termos técnicos da especialidade saíram deformados.
**Variações aceitáveis.** Lista do que é dele e do que não é (palavra de quem ele critica).
**Trecho real.** Cliente B: "Termos técnicos que ela usa com naturalidade (escrever certo; a transcrição das lives errou alguns)". Cliente C: "Vocabulário técnico (usar; é a linguagem do nicho)". Caso-base, sobre a saudação: "era erro de transcrição/extração — não existe essa variante". O erro que escapou: o DNA do cliente C grafava um termo técnico com uma letra a menos, e a peça corrigiu ("É erro de digitação nos dois [...]"). Aqui não foi a transcrição (o DNA do cliente C saiu de documento escrito): foi digitação, e a correção ficou só na peça por semanas, até voltar pro DNA com nota (§9.1).

### 5.8 O que evitar: regra nossa, escrita separada da fala dele — PADRÃO CONSISTENTE (proposto), 7 de 7

**O que entra.** As regras de produção de copy pra aquele expert (palavra proibida, escassez que não vale, número que não se usa, frase que soa a outra pessoa), cada uma com a data e quem decidiu, num título próprio, longe da fala dele.
**Por quê.** Regra misturada com fala vira "ele diz isso", e o agente passa a escrever a regra como se fosse voz.
**Variações aceitáveis.** Quando o dono nunca escreveu a lista, o que foi deduzido por observação fica "a validar" e não vale como regra.
**Trecho real.** Caso-base: "O que evitar na voz dela (regras de produção de copy — não são declarações da [expert])". Cliente B: "O que evitar (regras de produção de copy, não são falas dela)". Rodrigo: "Esta seção é a maior pendência do arquivo." e o que foi deduzido "precisa ser validado por ele". Cliente D, a coerência com o que ele critica: "Um produto dele com essas palavras na página destrói a autoridade que o vende." Caso-base, regra que mudou: "A regra anterior aqui proibia qualquer menção a vaga, e ela contradizia" o framework de criativos, e o que ficou: "O que continua proibido é escassez de capacidade falsa".

### 5.9 Quem fala: o expert, o sócio e o bastidor — PADRÃO CONSISTENTE (proposto), 4 casos

**O que entra.** Quem é o rosto da marca e quem é o contato com a gente. Fala de sócio ou equipe registrada como bastidor. Jargão interno que não vai pro público.
**Por quê.** Quem fala com a operação nem sempre é quem aparece pro avatar; misturar dá a voz errada à peça.
**Variações aceitáveis.** Vários sócios, cada um com voz própria; o que um não é, pra não ocupar o espaço do outro. Quando isso não está no DNA, fica no arquivo geral do projeto (do lado de vocês, o `CLAUDE.md`, que diz quem é quem).
**Trecho real.** Empresa da casa: "Não presumir que são intercambiáveis nem que um fala pelo outro." Cliente B, sobre o termo Roma: "Nunca aparece em roteiro falado nem em material pro público."

### 5.10 Afirmação sem fonte e número que não entra — PADRÃO CONSISTENTE (proposto), 5 donos

**O que entra.** A lista do que circula no material antigo e não pode ir pra copy até alguém mostrar o dado, com o porquê.
**Por quê.** Material do expert e análise anterior trazem número de efeito sem lastro. Se não fica escrito que não vale, o agente usa.
**Variações aceitáveis.** A lista mora no DNA (credencial, volume de alunos) ou na ficha do produto (resultado de aluno, prova social).
**Trecho real.** Cliente B: "Afirmações sem fonte, que não entram até alguém mostrar o dado". Cliente C: "não usar em copy sem o [expert] confirmar de onde sai o número". Empresa da casa: "Números que apareceram nas calls e NÃO podem ser usados". Cliente D: "Ainda não temos, e não se inventa".

### 5.11 Arquétipo — PADRÃO INCONCLUSIVO (uso)

Aparece em 4 de 7 DNAs (caso-base, B, D e um da empresa da casa); o do Rodrigo está "a definir". Nenhuma peça entregue cita o arquétipo como fonte (busca no fim da montagem). A empresa da casa já marca o dela como bastidor: "Arquétipo (bastidor — não vai cru pro público)". Fica como hipótese: se ele ajuda quem escreve ou é peso morto no arquivo.

### 5.12 O que falta, escrito no próprio DNA — PADRÃO CONSISTENTE (proposto), 6 de 7

**O que entra.** A lista do que não existe e de quem depende cada item.
**Por quê.** Lacuna escrita vira pergunta na hora certa; lacuna calada vira suposição na peça.
**Variações aceitáveis.** Seção no fim, ou a lacuna no próprio campo.
**Trecho real.** Cliente C: "O que este arquivo AINDA NÃO tem (não inventar)". Cliente B: "O que ainda falta na pasta dela". O do caso-base é o único sem a seção.

### 5.13 Campos que apareceram uma vez — VARIAÇÃO ISOLADA

- **Como o expert grava** (cliente C): "Isso muda o formato de entrega da copy"; resolvido dias depois: teleprompter. O Rodrigo, sobre VSL: "liga a câmera ali, liga o teleprompter e sai lendo".
- **Segundo mercado sem voz registrada** (cliente C): "É a lacuna mais importante, porque a [versão do segundo mercado] já fatura".
- **Registro por canal** (cliente D): reel, carrossel, legenda, story e livro, cada um com o seu.
- **Limite de publicidade do nicho** (cliente D): entrou conhecimento geral, com o aviso "Isto não vem dos arquivos do projeto", e o título da seção diz que falta validar. Nos 7 DNAs, é o único trecho que não sai do material do cliente, e é o único que diz isso de si.
- **Caso de terceiro como matéria-prima** (cliente D): "já estão públicas nos reels, mas num anúncio muda o contexto".
- **Contatos oficiais** (cliente B): "Confirmar se ainda valem antes de usar."
- **Referências que o expert cita e depoimentos nomeados dentro do DNA** (cliente B). No caso-base os depoimentos moram na ficha do produto.

## 6. Passo 4 — `brand.md` só com o que é estável — PADRÃO CONSISTENTE (proposto)

### 6.1 O que muda por evento ou por produto mora fora do brand.md — PADRÃO CONSISTENTE (proposto), 2 donos, 8 arquivos

**O que entra no `expert/brand.md`.** Nome e assinatura da marca guarda-chuva, perfis oficiais, fotos, onde a identidade vive de fato. Cor e logo de evento vão na identidade visual do lançamento (`lancamentos/<AAAA-MM-nome>/identidade-visual.md`); a do produto, na ficha do produto ou num arquivo do produto.
**Por quê.** Paleta fixa no `brand.md` faz a peça de venda sair com a roupa do evento gratuito, ou o produto sair com a marca de outra pessoa.
**Variações aceitáveis.** Identidade do produto como seção da ficha; arquivo próprio do produto.
**Trecho real.** Caso-base: "não tem uma paleta única de marca", e o `brand.md` "guarda só o que é genuinamente estável entre todos os eventos". Programa principal do caso-base: "Confundir as duas veste a peça de venda com a roupa do evento gratuito.", com a decisão do Rodrigo: "é importante agora a gente inverter as cores para as cores do [programa principal]". Um produto da empresa da casa: "lendo o manual de [outra pessoa] como se fosse o do produto"; "Estavam bonitos e fora da marca." Quem desenha segue a regra: o arquivo do lançamento prevalece sobre o `brand.md` genérico do cliente, não o contrário (`.claude/agents/designer.md`).

### 6.2 Cor medida, fonte só confirmada — PADRÃO CONSISTENTE (proposto), 5 arquivos

**O que entra.** Hex extraído do arquivo original (PNG do logo, peça aprovada, CSS da página no ar), com o método. Tipografia só quando confirmada; senão, a aproximação com o aviso.
**Por quê.** Cor no olho erra, e chute escrito vira identidade oficial na peça seguinte.
**Variações aceitáveis.** Amostragem de pixel da peça; cor computada da página renderizada.
**Trecho real.** Identidade de um lançamento pago do caso-base: "Cor extraída por amostragem de pixel"; tipografia "não confirmado, só aproximação visual". Marca da casa: "Extraídas por amostragem de pixel dos PNGs (PIL), não por chute visual." Produto da empresa da casa: "Não é suposição nem manual herdado." Caso-base, o chute que ficou registrado como chute: "Chute NÃO confirmado (não usar como oficial)".

### 6.3 Asset real antes de qualquer estilo — PADRÃO CONSISTENTE (proposto), 4 donos

**O que entra.** Onde estão a peça já aprovada pelo cliente, o logo original e as fotos reais do expert.
**Por quê.** A regra veio de correção do Rodrigo, nas primeiras peças da casa: "peça real aprovada > qualquer suposição de estilo".
**Variações aceitáveis.** A peça aprovada é barra de qualidade, não molde: "Não é pra clonar esta peça em toda variação." (identidade do lançamento pago).
**Trecho real.** Cliente C, o que pedir: "arquivo original em PNG com fundo transparente, nas versões clara e escura". Caso-base: a origem da cor nas instruções antigas era "usar as mesmas cores do site (capturar da página)". Rodrigo: a pasta de fotos dele tem 2 arquivos, registrado como base visual fraca.

### 6.4 Canais oficiais confirmados — PADRÃO CONSISTENTE (proposto), 4 arquivos

**O que entra.** Os perfis e domínios que são do expert, confirmados por alguém, com a data.
**Por quê.** Perfil e domínio entram em toda página e peça; nos dois casos sem confirmação (Rodrigo e a empresa da casa), o handle não estava em material nenhum.
**Trecho real.** Caso-base: "Perfis oficiais (confirmados pelo Rodrigo [...])" e "São os dois únicos perfis oficiais." Rodrigo: "Handles não encontrados em nenhum lugar do material do Drive." Empresa da casa: handles do rodapé do site, a confirmar.

### 6.5 brand.md vazio de propósito (inteiro ou na parte visual), com o que falta pedir — PADRÃO CONSISTENTE (proposto), 3 de 6

**O que entra.** O pouco que se sabe, a lacuna declarada e o que pedir ao cliente pra fechar.
**Por quê.** Arquivo vazio com aviso faz o designer parar e pedir; arquivo preenchido com chute vira identidade na primeira peça.
**Variações aceitáveis.** Vazio inteiro (cliente C); vazio só na identidade visual, com o resto preenchido (Rodrigo: o arquivo tem o posicionamento e as decisões pendentes, e a seção visual diz "Identidade visual — PENDENTE").
**Trecho real.** Cliente C: "Este arquivo está praticamente vazio, e isso é proposital." e "[...] não invento — registro a lacuna." (a regra de nada inventado, `sirius-scale/REGRAS.md` §2), seguidos de cinco itens a pedir (logo, paleta, tipografia, peça de referência, banco de imagem). Dois clientes não têm `brand.md` nenhum (B e D).

### 6.6 Regra do manual de outra pessoa não se herda — VARIAÇÃO ISOLADA (empresa da casa, 3 episódios)

O manual de marca de uma pessoa não vale pra outra nem pro produto. Nos 3 episódios, um rótulo, uma paleta e uma cor proibida vinham do manual de outra pessoa da mesma empresa: antes de herdar, perguntar pra quem aquela regra foi escrita. O próprio `brand.md` da empresa avisa que as regras dele não valem automaticamente pros outros.

## 7. Passo 5 — A ficha de produto — PADRÃO CONSISTENTE (proposto)

A regra da casa define a ficha como "uma oferta por produto: promessa, mecanismo, entregáveis, preço/ancoragem, bônus, garantia" (o modelo em branco é o `sirius-scale/modelos/produto.md`). As 30 fichas acrescentam o que segue. Presença por busca de termo: preço em 30 de 30, entregáveis em 25, garantia em 23 (preenchida ou marcada `não encontrado`), bônus em 18, pendência em 17, aviso de nome em 10, vendas reais em 10, bônus de ação rápida em 5.

### 7.1 O nome e o aviso de confusão — PADRÃO CONSISTENTE (proposto), 10 de 30, 4 donos

**O que entra.** O nome oficial no topo e, quando existe um irmão de nome parecido (evento × produto, livro × curso, aula grátis × curso pago, nome velho × nome novo), o aviso, com o erro que já aconteceu.
**Por quê.** Nome trocado vaza pra roteiro que vai pro expert gravar.
**Trecho real.** Caso-base: "erro real, corrigido [...], depois de vazar pra roteiro que já tinha ido pro expert" e, na ficha irmã, "Nunca fazer busca-e-troca cega entre os dois nomes". Empresa da casa: "São três coisas diferentes que costumam ser confundidas."

### 7.2 O que é e o papel no funil — PADRÃO CONSISTENTE (proposto)

**O que entra.** Tipo (curso, kit físico, e-book, evento, assinatura), papel (front, backend, upsell, downsell, isca, bônus, componente) e o que ele não é.
**Por quê.** Peça que vende a entrada não pode prometer o que só o produto caro entrega (regra do agente `copy`); a ficha é onde essa fronteira fica escrita. Entregável que a promessa não anuncia é bônus (`sirius-scale/frameworks/lancamentos/roma-e-promessa.md`).
**Trecho real.** Cliente C: "kit físico (apostila + [material físico de apoio]). Não é curso." Caso-base, sobre um bônus que estava registrado no produto errado: "Não é entregável do ingresso [...] e não deve aparecer em criativo de venda de ingresso." E o assistente de IA do programa principal: "Componente (não é produto à parte)".

### 7.3 Promessa verbatim, da fonte mais recente — PADRÃO CONSISTENTE (proposto)

**O que entra.** A promessa como o expert falou ou como está na página, com a fonte e desde quando vale; a anterior marcada como substituída.
**Por quê.** A promessa se repete igual nas peças do funil (`sirius-scale/frameworks/lancamentos/roma-e-promessa.md`, e `sirius-scale/frameworks/lancamentos/cpl-3-aulas.md` §4.2: a Roma é dita do mesmo jeito em toda aula, e só a aula 1 ganha uma cláusula a mais); parafraseada, cada peça promete uma coisa.
**Trecho real.** Caso-base (DNA): a promessa "é usada verbatim, não parafraseada". Evento de ingresso: "Substitui qualquer promessa anterior usada nos criativos deste lançamento." Cliente C: "Transformação prometida (verbatim da oferta)".

### 7.4 Entregáveis pela fonte mais perto da plataforma — PADRÃO CONSISTENTE (proposto), 25 de 30

**O que entra.** Módulos e aulas pela área de membros, pelo manual do vendedor ou pelo print da plataforma. O que o roteiro disse, só se não houver outra coisa, e marcado.
**Por quê.** Roteiro arredonda e envelhece; a revisão confere a peça contra esta lista (o `/revisar` alerta que o produto pode já entregar, como bônus, exatamente o que a peça diz que falta).
**Trecho real.** Caso-base: "Estrutura real na plataforma (print da Hotmart". Cliente C, a grade resolvida pelo manual do vendedor, "que traz a grade aula a aula". Cliente B: "A lista oficial dos 14 módulos: não encontrada".

### 7.5 Bônus e bônus de ação rápida — PADRÃO CONSISTENTE (proposto)

**O que entra.** Cada bônus com o valor que o expert declarou e, quando dá, a objeção que ele ataca. Ação rápida com a mecânica (prazo, ordem de chegada), a janela e de que turma é.
**Por quê.** Bônus e escassez de uma turma ficam no roteiro gravado e no material antigo; a ficha é onde se diz se ainda valem (cliente B, a escassez de turmas anteriores que "não vale mais e não pode ser repetida").
**Variações aceitáveis.** Registrar a falta de bônus como pendência da oferta, com o motivo.
**Trecho real.** Caso-base: "Bônus da turma (aula 06, com valor atribuído por ela)". Cliente B: "Bônus de ação rápida (só daquela turma; não repetir sem decidir de novo)". Um curso do caso-base: "Não existe bônus de ação rápida." Regra do Rodrigo gravada nas fichas da linha de produtos de entrada: "toda oferta tem que ter um bônus".

### 7.6 Preço por contexto; a plataforma vence o roteiro — PADRÃO CONSISTENTE (proposto), regra escrita em 3 donos

**O que entra.** Uma linha por contexto (cheio, primeiro dia, upsell, downsell, perpétuo, recuperação), cada uma com fonte e data; parcelado conferido na plataforma; histórico separado; preço velho marcado como velho.
**Por quê.** O vídeo gravado envelhece e o checkout é o que cobra; o `/revisar` confere preço, garantia e bônus contra a ficha, caractere a caractere.
**Variações aceitáveis.** A plataforma é a que vende: Hotmart no caso-base e no cliente B; a empresa da casa vende por outra plataforma.
**Trecho real.** Cliente B: "e o preço da Hotmart vence o do roteiro"; "Vale a Hotmart. Se os vídeos foram gravados com esses números, estão errados." Cliente C: "Preço real (medido, não declarado)" e "O que o Dash registra é outra coisa". Caso-base: "mas o número final sai da Hotmart, não desta conta"; o preço antigo "está superado — não é uma terceira faixa de preço, era registro desatualizado". Decisão do Rodrigo gravada com as palavras dele: "a gente vai manter no perpétuo a [...]".

### 7.7 Ancoragem e garantia como foram ditas — PADRÃO CONSISTENTE (proposto)

**O que entra.** A ancoragem na ordem em que o expert construiu, com os números dele; a garantia verbatim e a da plataforma; quando houver, o reembolso real.
**Por quê.** Âncora inventada é número sem fonte (`sirius-scale/REGRAS.md` §2). A garantia falada tem que bater com a configurada na plataforma, e o roteiro do upsell do cliente B já marca isso pra conferir ("o upsell 2 diz 7 e o próprio roteiro pede pra confirmar"). Que a divergência gere reembolso ou reclamação é PADRÃO INCONCLUSIVO: não há caso registrado na base.
**Trecho real.** Caso-base: "Ancoragem (real, como foi construída)". Cliente B: "Ancoragem (como ela construiu [...])". Cliente C: "Ancoragem de valor já usada pela casa", com a lacuna: "Não há âncora externa de mercado documentada". Cliente C, garantia ao lado do dado: "Reembolso real medido: 2,6%".

### 7.8 Depoimento só com fonte e com o dado junto — PADRÃO CONSISTENTE (proposto)

**O que entra.** Os depoimentos que existem em print, vídeo ou fala gravada, com o resultado específico e onde está o arquivo. Os que circulam sem origem, marcados como proibidos.
**Por quê.** Depoimento é dado de cliente (`sirius-scale/REGRAS.md` §2); em arte, só print real (correção do Rodrigo: cartão com aspas montado por nós é vetado).
**Variações aceitáveis.** A versão certa de uma história de aluno escrita uma vez, com a lista das peças que contam a errada.
**Trecho real.** Caso-base: usar sempre com o dado específico junto (a prova, o cargo, a nota). Empresa da casa, regra do Rodrigo sobre depoimentos de página sem print: "Não usar em nenhum lugar além daquela página." Cliente B: "não existe outro depoimento nomeado do [produto] nas fontes"; a história de um aluno na versão certa, com a frase que desfaz a versão errada, e o aviso: "Se algum desses está no ar, está com a versão que a regra proíbe."

### 7.9 Vendas reais dentro da ficha — PADRÃO CONSISTENTE (proposto), 4 donos

**O que entra.** O que a plataforma ou o Dash registram: vendas, ticket praticado, reembolso, de onde a venda vem.
**Por quê.** Preço declarado e preço praticado divergem, e o comprador real pode desmentir o perfil deduzido.
**Trecho real.** Cliente B: "o perfil de quem compra o [produto] é hipótese, não fato". Cliente C: "boa parte do [produto] não é vendida pelo funil de upsell".

### 7.10 Produto que ainda não existe também tem ficha — PADRÃO CONSISTENTE (proposto), 3 clientes, 6 fichas

**O que entra.** O que já foi decidido, de onde saiu, e o resto como `não encontrado`.
**Por quê.** Sem a ficha, o primeiro roteiro que citar o produto preenche o vazio.
**Trecho real.** Cliente B: "Este arquivo existe pra ninguém preencher o vazio com suposição" e "Sem conteúdo definido, a copy da Black não pode prometer entregável específico deste curso." Caso-base, livros digitais: "Estágio de estratégia, não produzidos."

### 7.11 A limitação declarada, que vira ponte pro próximo produto — PADRÃO CONSISTENTE (proposto), 5 fichas de 2 clientes

**O que entra.** O que o produto não cobre, dito pelo próprio material, e pra onde isso leva.
**Por quê.** É a base honesta do upsell (cliente C: "O material declara a limitação de propósito, e ela é o gancho do upsell"), e impede que a página do produto de entrada prometa o que ele não tem.
**Trecho real.** Cliente C, em molde: "[o produto] mostra [o que ele cobre]. Ele não [o que fica pro produto seguinte]." Caso-base, nas quatro fichas de produto de entrada: "O que este produto NÃO promete (ponte honesta)".

## 8. Passo 6 — Travar o dado que diverge — PADRÃO CONSISTENTE (proposto)

**O que entra.** Seis movimentos, nesta ordem:

1. Registrar as versões, cada uma com a fonte, e não usar nenhuma até travar.
2. Se uma das fontes é a oficial, ela vence: plataforma de venda pra preço e garantia; tela do Dash pra número de venda e lead (onde o cliente tem Dash); o arquivo do expert pro texto dele.
3. Se o dado é do dono (número da bio, nome, grafia, idade), quem trava é ele.
4. A trava entra com data, quem decidiu e o que era antes.
5. O que ficou velho continua visível, marcado como superado ou morto.
6. Listar onde a versão errada ainda circula (roteiro gravado, criativo, página).

**Por quê.** O agente lê o que está escrito. Divergência deixada aberta se resolve pelo arquivo que ele abrir primeiro.

**Variações aceitáveis.** As duas versões podem estar certas em tempos diferentes (anos de carreira) ou serem dados diferentes com o mesmo nome (duas provas sociais, duas calls).

**Trecho real, os casos da base:**

| Dado | As versões | Como travou |
|---|---|---|
| Experts lançados (Rodrigo) | VSL × site | primeiro: "ele já tinha trocado 15 por 20 à mão" num criativo; depois: "24 experts (ele contou)" |
| Análises de lançamento (Rodrigo) | mais de 2 mil × mais de mil | "perto de 2 mil, talvez já passou"; na bio, quase 2 mil |
| Anos de carreira (cliente B) | o número do material antigo × o de dois anos depois | as duas certas no seu tempo: "estava certo na época e ficou velho"; a idade numa data da história fica pra ela |
| Prova social (cliente C) | dois números de alunos | com o dado, viraram afirmações diferentes (compradores de um produto, alunos de outro); "Não somar: sobreposição desconhecida." |
| Volume de alunos (caso-base) | centenas × milhares | primeiro "centenas", quatro dias depois "milhares": "o número real não mudou, a escolha de palavra é que virou" |
| Preço do downsell (cliente B) | roteiro × Hotmart | vale a Hotmart; o vídeo com o número errado está errado |
| CPL de um case (empresa da casa) | três números | "Eram calls diferentes, não números conflitantes." |
| Preço do ingresso (caso-base) | em vigor × redução planejada | usar o em vigor "até o cliente confirmar que a mudança já entrou em vigor" |
| Tabelas de preço antigas (empresa da casa) | três tabelas em material interno | "Tabelas MORTAS que ainda circulam no material (não usar)" |

Regra de cabeçalho que resume: "Onde as fontes divergem, as duas versões estão registradas." (ficha de oferta da empresa da casa). E a escolha da versão mais precisa, mesmo quando a menos precisa é mais forte: "Usar a versão precisa — é mais exata e menos agressiva com uma cliente que aparece no print."

## 9. Passo 7 — Manter a ficha viva — PADRÃO CONSISTENTE (proposto)

**O que entra.** Toda decisão que muda a ficha volta pro arquivo de origem (em `expert/`) no mesmo turno, com data, quem decidiu e a pendência riscada.
**Por quê.** O agente lê os arquivos, não a conversa de cada tarefa, e tarefa concluída não avisa ninguém. No caso de origem, a identidade da Black estava aprovada na tarefa e o arquivo ainda dizia proposta (correção registrada; o arquivo agora registra: "Já estava decidida.").
**Variações aceitáveis.**
- Revisão que muda regra de voz atualiza o DNA no mesmo dia. Numa VSL do caso-base, a regra de credencial "vira regra de criativo curto (dna-expert.md atualizado)" (leia-me do funil).
- Preço mudou: a ficha primeiro, porque "é a fonte que o /revisar usa pra conferir página e copy", depois a busca do nome e do preço velho em todos os arquivos (correção registrada). VARIAÇÃO ISOLADA como procedimento (1 caso).
**Trecho real.** O DNA do caso-base guarda cada regra com o dia e o autor (três datas diferentes). Na ficha de um curso do caso-base, cada linha de preço traz a fonte e a data: o downsell vem como "Rodrigo, [data] (volta ao combinado de [data anterior]".

### 9.1 A trava que não propagou — PADRÃO CONSISTENTE (proposto), 4 casos em 3 donos

- Os números da bio do Rodrigo foram travados no `dna.md` dele e na ficha de um produto dele, e não chegaram no DNA dos fundadores da empresa da casa (que seguia com as análises em aberto), no `brand.md` dele (que seguia com a faixa antiga de experts) nem na §7 do próprio `dna.md`. Este levantamento achou no dia seguinte à trava, e a correção foi feita no mesmo dia nos três.
- O termo técnico grafado errado foi corrigido na peça do cliente C semanas antes e só voltou pro DNA neste levantamento (§5.7).
- O `brand.md` do caso-base fala em "13 fotos profissionais reais dela"; a pasta tem 15, e o arquivo de identidade da Black já diz "São 15 fotos em" `fotos/`.
- O preço novo de dois produtos de entrada do caso-base não chegou em quem o usava como âncora ou soma: o preço novo não chegou na âncora da Black (correção registrada).

O padrão nos quatro: o mesmo dado em mais de um arquivo; a trava entra num e o agente pode ler o outro. Os três primeiros apareceram nesta leitura; o quarto, duas semanas e meia antes. Pela regra da casa ("dá pra virar checagem que roda sozinha?"), é candidato a checagem automática. Hoje não existe.

## 10. Passo 8 — O expert: o que vai pra ele confirmar, o que se combina com ele e o que não vai pra aprovação dele — força em cada parte (10.1 e 10.2 PADRÃO CONSISTENTE, 10.3 VARIAÇÃO ISOLADA)

São três coisas diferentes. Oferta e preço não ficam do lado de fora: nas fontes, eles se combinam com o expert em conversa. O que fica fora é a peça.

### 10.1 O que é dele vai pra ele confirmar — PADRÃO CONSISTENTE (proposto), 5 donos

**O que entra.** Grafia do nome e do produto, números da bio, idade e datas da história, contatos, o texto e o nome do material que ele escreveu, o conteúdo dos bônus, a voz.
**Por quê.** São dados dele, e só ele trava: nome e texto do material não mudam sem ele ("eu não posso simplesmente alterar o nome do low ticket sem antes conversar com ela", Rodrigo, correção registrada).
**Variações aceitáveis.** Levar pronto e pedir só o ok (cliente D, "levar pronto pra ele só validar"). Ideia nossa sobre o material dele sai marcada: "o que for sugestão, você tem que indicar bem claramente" (regra completa em `sirius-scale/frameworks/design/impresso-editorial.md` §2.1).
**Trecho real.** Cliente C, grafia da marca: "isso é decisão de marca, não de gosto". Cliente B: "Confirmar com ela antes de usar a idade." Empresa da casa: a bio é a "versão que ele mesmo pediu", e o número cru saiu porque ele "achou que não conectava". Cliente D, ainda pendente: "o DNA precisa da leitura [do expert]".

### 10.2 Oferta e preço se combinam em conversa com ele — PADRÃO CONSISTENTE (proposto), 4 episódios em 3 clientes

**O que entra.** Os itens da oferta, o preço e as condições, combinados numa call com o expert, e a decisão gravada na ficha ou no briefing com quem estava e o que mudou.
**Por quê.** Nos episódios da base, o expert opina e muda o número: no caso-base, o preço do não aluno subiu depois da fala do expert e do sócio dele; no cliente B, o expert queria uma opção mais barata e a oferta fechou na conversa, com o Rodrigo preferindo melhorar a oferta a baixar o preço.
**Variações aceitáveis.** A conversa pode ser pedida pelo expert (caso-base); a decisão pode ficar dependendo dele quando ainda não houve conversa (cliente D).
**Trecho real.** Cliente B, ata da reunião da oferta da Black: "Rodrigo, [o gerente do projeto] e [a expert] fecharam a oferta da Black" e "[a expert] queria opção mais barata; Rodrigo prefere melhorar a oferta a baixar preço". Caso-base, briefing da Black: a oferta foi fechada pelo Rodrigo, o expert e o sócio dele (itens, preço, vitalício, prazo), e três semanas depois o preço do não aluno subiu cerca de 13%, porque "[o expert] e [o sócio] voltaram na fala da [gerente de operação] de que a oferta estava barata." Cliente D, cabeçalho do DNA: "Preço, promessa e tema de produto continuam dependendo dele".

### 10.3 A peça não vai pra aprovação dele — VARIAÇÃO ISOLADA (2 falas e 1 episódio)

**O que fica fora.** Página, checkout, criativo e estratégia. O que vai pro expert da peça é o texto que ele grava: o documento que vai pra quem grava é só o texto de gravação (`.claude/agents/copy.md`).
**Por quê.** Rodrigo, numa reunião sobre o desenho de acesso do expert às aprovações (00:54:12): "Só que o expert não tem que ter acesso pra aprovar criativo, não." Na call de começo de projeto, sobre estratégia: "o que eu não gosto, assim, de mesmo é de ficar decidindo como expert, coisa que é de estratégia." E ao tirar da página de validação do expert do caso-base o que era de checkout e de acesso: "isso é decisão minha [...]" (correção registrada).
**Como as duas partes convivem.** A correção diz que preço é decisão do Rodrigo e não entra na validação do expert. No mesmo dia, o preço da Black do caso-base foi revisto com o expert numa call. A leitura que fecha com as duas fontes: o preço não vai pra página de validação dele; ele se combina em conversa (§10.2).

## 11. Regras transversais

1. **Zero invenção, e a lacuna diz onde procurou** (§4). Antes de `não encontrado`, procurar no Drive (ou onde o material do cliente mora).
2. **Uma coisa em um lugar.** A identidade do evento não vai pro `brand.md` (§6.1). A regra que o projeto do expert e a casa dizem igual aparece uma vez: "Onde o projeto dela e a casa dizem a mesma coisa, a regra aparece uma vez só." O recorte de outra marca não se repete na marca pessoal (`dna.md` do Rodrigo: "e não se repete aqui"). Quando o dado precisa morar em dois arquivos, a trava vai nos dois (§9.1).
3. **Frase real só com a origem e o contexto.** É regra do agente `copy`: verbatim só entra com a origem e o contexto. Por isso o DNA cita a fonte de cada fala.
4. **A voz vence o template.** Decisão do Rodrigo: a voz vence (`sirius-scale/frameworks/oferta-14-secoes.md` §4: a regra de voz do caso-base contra a anáfora do template de oferta). Quando o DNA proíbe uma forma, a estrutura vale pelo conteúdo, não pela forma.
5. **Regra do DNA que bate de frente com framework CONSISTENTE não se resolve calada:** vai pra quem decide (no caso de origem, o Rodrigo), e o DNA é reescrito com a data (caso-base, vagas, §5.8). Do lado de vocês, a decisão fica registrada em `frameworks-da-casa/` (`sirius-scale/REGRAS.md` §4).
6. **Escassez: a ficha diz qual urgência é real naquele produto.** Caso-base, o corte do ingresso: "É prazo real, não escassez fabricada". Cliente B, a escassez antiga que "não vale mais e não pode ser repetida". O princípio é da casa (`sirius-scale/frameworks/copy/criativos.md` §0.5, `sirius-scale/frameworks/oferta-14-secoes.md` §14).
7. **Dado de aluno, de cliente atendido e de lead não entra na ficha além do que já é público na peça.** Caso de terceiro pede o ok do expert (cliente D, §5.13); a calibração de uma ferramenta de IA guarda os resultados por código e avisa: "Neste arquivo nenhum aluno é identificado." VARIAÇÃO ISOLADA (2 arquivos).

## 12. Exemplos consolidados (reescritos dos casos)

**Cabeçalho com cuidado de leitura** (DNA do cliente D): "Nada aqui foi validado pelo [expert]." / "É retrato do que ele já publicou, não declaração dele.".

**Regra de voz datada, com o porquê** (DNA do caso-base): "Credencial [do expert]: uma vez por peça em criativo curto (anúncio, e-mail, disparo)." / "Em roteiro longo (VSL, CPL, live), uma por bloco onde for natural" / "pra criativos curtos faz sentido, mas não precisa ser algo cravado na pedra".

**Número travado pelo dono** (`dna.md` do Rodrigo): experts, "24 experts (ele contou)"; análises, "perto de 2 mil, talvez já passou".

**Conflito de preço na ficha** (cliente B): "O cheio na Hotmart é [preço], e o lançamento vendeu a [esse preço] a partir do segundo dia." / "Vale a Hotmart. Se os vídeos foram gravados com esses números, estão errados."

**Brand vazio de propósito** (cliente C): "Este arquivo está praticamente vazio, e isso é proposital." / "Os 43 documentos do Drive do projeto não trazem nenhum ativo de marca" / "[...] não invento — registro a lacuna."

**Produto que ainda não existe** (cliente B): "Este arquivo existe pra ninguém preencher o vazio com suposição" / "Sem conteúdo definido, a copy da Black não pode prometer entregável específico deste curso."

## 13. O que é reutilizável e o que é do caso

**Transfere (é do processo, e apareceu em mais de um cliente):**

- Os três arquivos e a fronteira: o estável na ficha (`expert/`), o que muda por lançamento no briefing, na pesquisa e no avatar (`lancamentos/<AAAA-MM-nome>/`).
- A ordem das fontes de voz e a marca de origem em cada fala.
- O esqueleto do DNA (§5.1 a §5.10 e §5.12).
- Regra nossa separada da fala dele; bastidor separado da voz pública.
- `brand.md` só com o estável, cor medida, vazio de propósito com a lista do que pedir.
- Ficha de produto: aviso de nome, papel no funil, plataforma vence roteiro, superado visível, bônus de turma não se repete, produto inexistente com ficha.
- Os seis movimentos de trava (§8) e as três partes do §10: o que é dele vai pra ele, oferta e preço se combinam com ele, a peça não vai pra aprovação dele.

**É do caso (não generalizar):**

- Os bordões, as contagens e os 5 movimentos do caso-base; as 3 estruturas do cliente B; o padrão de análise de caso do cliente C. Transfere o formato (contar, descrever a sequência), não o conteúdo.
- Credencial uma vez por peça, "vagas", "ao vivo": regras de copy do caso-base.
- Identidade que muda a cada evento: é o caso-base. A marca da casa tem uma cor só; a empresa da casa tem a dela.
- A plataforma de referência (Hotmart ou outra) e o Dash como registro de venda, onde o cliente tem Dash.
- Limites de publicidade do nicho: cliente D, e ainda a validar.
- Segundo mercado: cliente C.

**O que se viu transferir (medido nesta leitura, não suposto):** o cabeçalho com a regra e o `não encontrado` passaram pros 5 clientes; a contagem de frequência passou do caso-base pro cliente D; o "o que evitar" separado da fala passou do caso-base pro cliente B. **O que não transferiu:** o uso. Fora do caso-base, as fichas foram pouco citadas por peça, e o arquétipo, presente em 4 DNAs, não é citado por nenhuma.

## 14. Pontos em aberto

1. **O expert lê o DNA dele?** Nenhum expert de cliente leu e aprovou o próprio DNA. O arquivo geral do cliente D diz que o DNA precisa da leitura do expert; a regra do Rodrigo é levar pronto e não puxar o expert pra estratégia. Não está decidido se a ficha vai pro expert, e em que forma.
2. **Efeito na copy não medido.** Não existe peça com DNA contra peça sem DNA, nem retorno de expert registrado sobre a copy soar como ele, além da fala do Rodrigo.
3. **Arquétipo** (§5.11): fica no modelo ou sai?
4. **Contagem de frequência** (§5.5): obrigatória quando a base é grande? Qual o mínimo? Só 2 de 7 contaram.
5. **Cliente sem `brand.md`** (B e D): monta-se pelo material que existe ou espera o cliente mandar? No B não há peça visual guardada; no D, imagem e vídeo são da agência que cuida das redes dele.
6. **Dado em dois arquivos** (§9.1): falta definir qual é a fonte única da bio do Rodrigo (o `dna.md` dele, o DNA dos fundadores da empresa, o `brand.md`) e se isso vira checagem automática.
7. **Regra de publicidade do nicho:** a do cliente D entrou de conhecimento geral e espera o jurídico. Nos clientes B e C não há regra desse tipo registrada.
8. **DNA anterior não guardado:** o do cliente C não foi guardado; 2 de 3 guardam o original.
9. **Como o expert grava** (§5.13): só o DNA do cliente C tem o campo, e o Rodrigo trata o teleprompter como decisão que muda a copy. Vira campo padrão?
10. **Marca própria do Rodrigo:** "o que evitar", crenças e essência seguem pendentes, e um produto novo dele já usa a bio.
