# Framework — Produção de VSL (do dossiê ao roteiro gravável, funil perpétuo)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered do trabalho de VSL em três funis perpétuos, de três clientes de duas empresas do Rodrigo, ao
longo de umas sete semanas, e das falas do Rodrigo em nove reuniões. Base: 5 roteiros de VSL, 11 versões,
7 registros de mudança, 29 leads e hooks escritos, 2 revisões de lead e hook.

**Os três casos, no arquivo inteiro:**
- **caso A (o caso-base):** um expert de educação; funil de VSL de um livro de entrada, com uma segunda frente
  pra um curso do mesmo tema.
- **caso B:** um expert que vende um curso técnico pra profissionais, cliente de outra empresa do Rodrigo; o
  curso é vendido em mais de um mercado.
- **caso C:** um segundo expert da casa; funil de VSL de um livro de entrada.

> **ALCANCE (proposto): TESTADO EM 3 CLIENTES só em quatro pontos: etapa 1, itens 1, 4 e 5; etapa 2; etapa 3,
> item 1; regra transversal 1.** Nesses, o mesmo passo aparece de fato nos três. **TESTADO EM 2 CLIENTES
> (proposto), casos A e B,** nos itens que dizem isso: o resto das etapas 1 e 3, os itens 1, 4, 5 e 6 da etapa 9
> (no item 1, no caso C, há só a regra escrita, e a VSL dele traz as notas pra equipe no mesmo arquivo), as
> etapas 4, 6 e 10.
> **O resto é NÃO TESTADO FORA:** o ciclo de versões com registro (etapa 5), a revisão por Great Leads (etapa 6)
> e as duas VSLs com tronco comum (etapa 8) são de um cliente só, o caso A. Promover alcance é decisão do
> Rodrigo. "Testado", aqui, quer dizer executado, não provado por resultado. **Nenhuma VSL feita pelo processo
> inteiro tinha sido gravada quando este arquivo fechou.** As duas que foram ao ar (casos B e C) são anteriores
> ao registro da casa e não têm registro de versão. O quadro de status está no §1.
> O caso B é de outra empresa do Rodrigo: padrão de um negócio aplicado em outro é sinalizado na entrega
> (`sirius-scale/REGRAS.md` §4).
>
> **Vizinhos, citados e não repetidos:** a estrutura (Lead, História, Tese, Oferta, as 15 perguntas, os
> entregáveis de uma VSL) mora em `sirius-scale/frameworks/lhto.md`; o bloco de oferta, em
> `sirius-scale/frameworks/oferta-14-secoes.md`; os tipos de lead, em `sirius-scale/frameworks/copy/great-leads.md`;
> a edição (mapa por bloco, gravação única por mercado, emenda de hook novo no corpo que já roda), em
> `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`. Vídeo de upsell e de downsell é outro arquivo:
> `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` (o roteiro do vídeo de upsell está em
> `sirius-scale/frameworks/copy/video-de-upsell.md`).
> Este arquivo cobre o processo do meio: o que entra antes de escrever, como sai cada versão, como se revisa
> lead e hook, como se desenha a gravação e o que vai pro expert gravar.
>
> Contagens e rótulos são os da base completa da casa; alguns dos casos não aparecem neste kit.

---

## 1. Escopo e base de evidência

### Fontes

**Fonte A — caso A, funil de VSL do livro de entrada.** Roteiro da Frente A (o livro) em cinco versões (a v1 é
anterior ao registro da casa; v2 a v5 saíram em dois dias seguidos), Frente B (o curso) em três versões, entre o
segundo e o terceiro dia, sete registros de mudança (na Frente A, 83 entradas numeradas em sequência), a revisão
das leads pelo Great Leads, o documento de arquitetura da Frente B, o briefing, o avatar, a pesquisa, um dossiê do
segmento, o documento de peças estratégicas e o histórico de decisões datado do funil. Junto: o `/revisar` da
v2, os docs de gravação e o gerador que monta esses docs a partir do roteiro. Peso: as decisões do Rodrigo no
histórico, datadas, são **fortes**; as versões, escritas por agente em cima dessas decisões e não gravadas, são
**médias**.

**Fonte B — caso B, funil do curso técnico.** A VSL que estava no ar (5 hooks + corpo), os 6 hooks novos escritos
pelo Rodrigo, a análise de retenção e venda por hook (com os dados exportados do player), o plano de produção com
as decisões dele, a VSL enxuta nova (um arquivo de direção e um de teleprompter), a revisão e o pente fino do
pacote de peças e o registro da edição dos hooks. Peso: VSL no ar com número e hooks escritos por ele e gravados
são **fortes**; o conteúdo da VSL enxuta é **fraco** (ver Excluído de propósito).

**Fonte C — caso C, funil do livro de entrada.** A estrutura estratégica e a VSL v1.0 com 10 leads (vindas do
projeto do expert no Claude), o briefing com os erros conhecidos dos roteiros, o desempenho do funil, o
debriefing, o checklist operacional do funil e as regras de trabalho que o Rodrigo usava naquele projeto (forma
de trabalho e regras de copy). Peso: VSL que foi ao ar e regras dele são **fortes**; qual versão está no ar não
está confirmado.

**Fonte D — falas do Rodrigo em reunião** (todas **fortes**), em ordem de data:
- D1, com a gerente de operação;
- D2, com o gerente do projeto do caso B;
- D3, com o expert do caso C;
- D4, com a equipe de conteúdo;
- D5, com o expert do caso A;
- D6, mentoria com um coprodutor de fora da casa;
- D7, uma reunião com gente de fora da casa (na ata, a fala do Rodrigo aparece sob o nome de uma conta de
  vídeo, e a atribuição foi feita pelo conteúdo);
- D8, com o gerente do projeto do caso B, sobre papéis e acordo;
- D9, conversa com produtores de fora da casa.

**Fonte E — correções do Rodrigo registradas na casa:** o doc de copy vai enxuto (só o texto de gravação); um doc
por peça, corrigido no mesmo link, sem versão no nome; retenção não é proxy de conversão; o `/humanizer` roda de
verdade, no texto inteiro, depois do `copy`; o expert valida só o que é dele; mudou o preço, propaga; decisão
dita fora do arquivo entra no arquivo.

**Fonte F — regras já escritas na casa:** o agente `copy` (a parte de roteiro, em `.claude/agents/copy.md`), as
regras de tom, de nada inventado e de copy pelo `copy` (`sirius-scale/REGRAS.md` §1 a §3) e a ficha de voz do
expert do caso A (o `dna-expert.md` dele).

### Status: o que foi ao ar e o que ficou em roteiro (no fechamento deste arquivo)

| Peça | Cliente | Feita em | Status | Número com arquivo |
|---|---|---|---|---|
| VSL no ar, 5 hooks + corpo | caso B | antes do registro da casa | no ar; uns três meses de mídia paga, depois quase só pelo link da bio | somando os 5 hooks: 6.818 plays e 39 vendas; o melhor converteu 1,05% por play; no split de 3 hooks, retenção de 16% a 20% no minuto 1 (Fonte B, análise §1 e §3) |
| 6 hooks da rodada 2, escritos pelo Rodrigo | caso B | junto do pacote de peças | gravados pelo expert e editados; os verticais montados no corpo que roda, os horizontais entregues depois, só como hook | nenhum no registro |
| VSL enxuta nova, direção + teleprompter | caso B | junto do pacote de peças | só roteiro; duas semanas e meia depois, não gravada e sem revisão do Rodrigo | — |
| VSL v1.0, 10 leads | caso C | antes do registro da casa, no projeto do expert no Claude | foi ao ar e foi editada por editor externo com o mapa de edição (D4); qual versão está no ar: não confirmado; tráfego pausado havia uns dois meses | só do funil: ROAS 2,19 e 0,81% de conversão da página (Fonte C, debriefing §1 e §3) |
| VSL Frente A (livro), v1 a v5 | caso A | v1 antes do registro; v2 a v5 em dois dias | candidata a gravação; quase três semanas depois, "ainda está para ser gravada", depois das peças da Black (D5) | — |
| VSL Frente B (curso), v1 a v3 | caso A | entre o segundo e o terceiro dia | idem | — |

### Excluído de propósito

- **A estrutura e o recheio dos blocos.** Lead, História, Tese, as 14 seções, os tipos de lead: estão nos
  vizinhos citados no cabeçalho. Aqui entra só como o processo usa cada um.
- **Edição.** Mapa de edição, corte, legenda, emenda do hook no corpo, gravação única por mercado do ponto de vista
  da edição: `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` (§0.1 e §6.1),
  `sirius-scale/frameworks/copy/edicao-video-receita.md` e `sirius-scale/frameworks/copy/edicao-video-criativos.md`.
  Aqui o processo para no bruto conferido contra o roteiro.
- **Vídeo de upsell e de downsell** dos casos A e B, mesmo seguindo o mesmo ciclo de versões e registro: outro
  arquivo. Aqui só aparece o lado da VSL (o que ela não pode gastar).
- **Criativos que levam pra VSL** e a configuração do player e da página (VTurb, headline em teste, botão que
  aparece no pitch): `sirius-scale/frameworks/copy/criativos.md` e
  `sirius-scale/frameworks/paginas/estrutura-de-pagina.md`. Entram só como o que o roteiro entrega pra frente.
- **Live de downsell:** `sirius-scale/frameworks/lancamentos/live-de-downsell.md`.
- **Como montar pesquisa e avatar:** `sirius-scale/frameworks/pesquisa/pesquisa-e-avatar.md`. Aqui entra só o que o
  roteiro consome deles.
- **O conteúdo da VSL enxuta do caso B como regra de copy.** O Rodrigo disse em D2 que não revisou as cópias
  daquele pacote e que as criou em cima da hora. Entram dela só as decisões de processo que ele tomou (gravação
  única, teleprompter, escrita pra frio) e o que a revisão técnica apontou.
- **A VSL do coprodutor de fora (D6):** não é trabalho da casa. Entra só a fala do Rodrigo.
- **Decisões de produto e preço do funil do caso A** (formato do livro, seeding, preço de upsell e downsell) além
  do que muda o roteiro.

### Base: quantos clientes, quantas unidades

- **3 clientes, 2 empresas** (casos A e C numa, caso B noutra), **3 funis perpétuos**, todos no mesmo desenho:
  criativo de conteúdo → VSL → produto de entrada → upsell de um clique.
- **5 roteiros de VSL e 11 versões**: caso A, Frente A (5) e Frente B (3); caso B, a VSL no ar (1) e a enxuta (1);
  caso C (1). **29 leads e hooks**: 8 do caso A, 10 do caso C, 5 + 6 do caso B.
- **7 registros de mudança**, todos do caso A. **2 revisões de lead e hook** (caso A pelo Great Leads; caso B por
  dado medido). **2 revisões técnicas** antes da gravação (caso A, v2; as peças do caso B).
- **Ressalva estrutural, com todas as letras:** o processo completo (dossiê, estratégia, versões com registro,
  revisão de leads, doc de gravação) foi executado num cliente só, e nada dele foi gravado. Os únicos números de
  VSL da base são de duas peças feitas antes do registro da casa, e só uma delas (caso B) tem número por hook.

---

## 2. A fórmula, em ordem

0. Se já existe VSL no ar, ler os números dela antes de escrever.
1. Montar o dossiê: os insumos que o roteiro consome, todos com arquivo de origem.
2. Escrever a estratégia LHTO antes do roteiro.
3. Desenhar a gravação antes do texto: o que se grava uma vez e o que se troca sem regravar.
4. Primeira versão pelo agente `copy`, com marcador no lugar de qualquer fato que falte.
5. Fechar cada versão com conferência, registro e revisão; a decisão do dono abre a passada seguinte.
6. Revisar leads e hooks contra o público, antes de gravar.
7. Hooks: de 5 a 10 por gravação, curtos, escolhidos por venda.
8. Quando o mesmo avatar entra por dois produtos: duas VSLs com tronco comum.
9. Doc de gravação só com texto, direção à parte, texto escrito pra teleprompter na voz do expert.
10. O expert valida o que é dele, completa o que só ele tem e grava; o bruto é conferido contra o roteiro.

**Dois modos de entrada, as mesmas etapas.** Lapidar um roteiro que já existe (caso A, v1 → v5: a etapa 4 é uma
lapidação com registro) ou escrever do zero com a VSL antiga como dado (caso B: a etapa 0 é obrigatória). Etapas
6 e 8 só existem quando cabem.

---

## Etapa 0 — Ler a VSL que já está no ar · VARIAÇÃO ISOLADA (1 VSL medida; a régua é do Rodrigo)

**O que entra.** A cascata do player, por hook: visualização → play → quem fica no minuto 1 → quem chega ao pitch
→ clique → venda, com o tamanho de cada vazamento em pessoas e o custo de mexer nele. Por cima, a régua que o
Rodrigo usa: play rate baixo é headline e capa; retenção do minuto 1 abaixo de 60% é hook; o que passa disso é
corpo e oferta. No caso medido (split simultâneo de 3 hooks do caso B): 7.579 visualizações, 4.503 plays, 788
pessoas no minuto 1, 350 no pitch, 232 cliques, 20 vendas.

**Por quê.** Decide o que reescrever. No caso B, o diagnóstico de partida do Rodrigo (o problema era o hook) se
confirmou, com duas correções que só o número deu: 40,6% de quem abria a página nunca apertava play, o que é
página e capa, não hook; e o corpo segurava, porque 66% de quem chegava ao pitch clicava. A análise fechou assim:
"O gargalo é exclusivamente pôr gente do outro lado do minuto 1." Quando uma VSL enxuta nova entrou no plano, foi
por outro motivo, que o plano escreveu: "Encurtar não é conserto de retenção." e "Mas frio não investe 25
minutos." (Fonte B, plano de produção §0.3).

**Variações aceitáveis.** Sem VSL no ar, a etapa não existe (caso A). Com o funil medido e o vídeo não (caso C:
faturamento, ROAS e conversão da página, nenhum play rate nem retenção registrados), dá pra dizer se o funil se
paga, não onde o vídeo perde gente. Declarar isso.

**Trecho real.**
- "O hook é o maior vazamento, mas não é o mais barato." (Fonte B, análise de hooks §2)
- "quem sobrevive ao primeiro minuto gosta do que vê e compra." (mesma análise, §2)
- "A VSL entrega 16% a 20%." (mesma análise, §1, contra o piso de 60% de `sirius-scale/frameworks/lhto.md` §5.6)
- Rodrigo, D7: "se o play rate estiver baixo, já está ruim, tem que melhorar a headline, melhorar a thumb da VSL"
  e "Se a retenção do primeiro minuto estiver abaixo de 60%, então o hook está péssimo, você precisa trocar o
  hook."
- Rodrigo, D2, sobre a mesma VSL: "O problema tá aqui no hook mesmo."

⚠️ Na mesma fala (D7) ele dá a meta do pitch: "a meta é até 30% chegar no pitch". Nenhuma VSL da base foi medida
perto disso: a do caso B levou 7,8% dos plays ao pitch.

**Achou o que vende, o teste continua · VARIAÇÃO ISOLADA (perpétuo, 11/2026).** O vencedor fica com 90%
do tráfego, e hook, headline ou VSL nova entra com 10% ou menos. Na mesma call ele deu os alvos: play rate de 60% e hook
rate de 70%. Trechos: "Deixa 90 na que já tá vendendo validado e joga 10%" e "O playrate nosso tinha que bater 60%".
Não medido: nenhum teste rodou nesse formato ainda.

---

## Etapa 1 — Montar o dossiê · PADRÃO CONSISTENTE (proposto); itens 1, 4 e 5 em 3 clientes, 2, 3 e 6 em 2, o 7 em 1

**O que entra.** Os arquivos que o agente `copy` lê antes da primeira linha, cada um com origem:

1. **Pesquisa e avatar do público do produto** (3 clientes), com sub-avatares, objeções ranqueadas e a linguagem
   literal deles. Sem pesquisa do produto, um recorte de outra pesquisa com o limite declarado (caso A: a pesquisa
   do programa principal filtrada por quem marcou o tema do livro, 1.778 respostas cruzadas com venda). Com
   pesquisa de quem comprou, ela entra ao lado da de lead (caso B: lead N=316, comprador N=37). No caso C, a base
   do funil é uma pesquisa de lançamento de 780 respostas.
2. **O produto lido na fonte** (2 clientes): a lista de aulas na plataforma, o PDF do livro, o manual do vendedor.
   No caso A, o PDF final do livro e a lista real de aulas derrubaram o presente surpresa da oferta (Seção 14 de
   `sirius-scale/frameworks/oferta-14-secoes.md`), que repetia um capítulo do livro e quatro aulas do curso, e
   tiraram o número de páginas da fala até a gráfica fechar; no caso B, a revisão técnica achou a soma dos bônus
   da VSL contradizendo o manual do vendedor.
3. **O catálogo de depoimentos** (2 clientes), com a frase verbatim e a objeção que cada um quebra.
4. **A voz do expert em documento, tirada da fala dele** (3 clientes): como ele fala, os bordões, o que ele nunca
   diz (`expert/dna-expert.md`; o método da ficha está em `sirius-scale/frameworks/expert/ficha-do-expert.md`). No
   caso A, com o bordão contado nas aulas; no caso C, a partir de três lives.
5. **O que o expert já falou e serve de matéria-prima** (3 clientes): roteiro de live anterior, semente, CPL. Frase
   dele entra como ele disse, sem paráfrase.
6. **As decisões do dono, datadas** (2 clientes), no `briefing.md` ou no plano: preço, garantia, termos proibidos,
   o que é verdade sobre escassez em cada página.
7. **Se houver, os números da VSL anterior** (1 cliente; etapa 0).

**Por quê.** É o que separa roteiro que soa certo de roteiro ancorado no dado do cliente (`sirius-scale/REGRAS.md`
§3). E é o que deixa a casa pedir ao expert só o buraco: o que existe em arquivo a IA executa, o que falta ela
pergunta, e o que só o expert tem chega dele (D8). Decisão dita numa conversa ou num comentário e não gravada no
arquivo de origem não existe pra quem escreve depois (Fonte E).

**Variações aceitáveis.** Avatar por proxy, desde que declarado: no caso A a conversão do recorte é de compra do
programa principal, e por isso a taxa do reincidente (4,28% × 1,79%) ficou fora do roteiro como afirmação. Base de
conhecimento herdada de outro projeto, corrigida antes de usar (caso C). A frase-fonte pode estar num roteiro de
live (a Lead 1 do caso A usa frases verbatim do roteiro de uma live anterior), num semente (a âncora de preço do
caso B) ou num CPL (a História do caso C foi ajustada ao CPL 1).

**Trecho real.**
- Rodrigo, D8: "O que faltar, ela vai perguntar, ó, faltam essas informações aqui, vai atrás." e "vamos escrever
  uma história aqui na VSL, tem que ter um áudio dele contando a história, pra gente encaixar lá dentro, né?"
- O avatar do caso A declara no §0 que a conversão do recorte é de compra do programa principal, não do produto da
  VSL; o registro da v2 (item 22) usa esse proxy declarado pra deixar o número de fora.
- "A tese da VSL está certa e a linguagem está no público errado." (Fonte B, análise de hooks §5)
- [Frase do expert que compara o preço com o de outro curso dele] (o expert do caso B numa live de semente;
  recuperada como âncora na direção da VSL enxuta, §11)
- "Base de validação: 276 respostas de pesquisa de avatar" (cabeçalho da VSL que estava no ar, Fonte B)
- "Avatar da pesquisa de 780 respostas, base do funil." (Fonte C, briefing) e "Baseado na análise de 3 lives
  completas" (Fonte C, DNA do expert)

---

## Etapa 2 — Escrever a estratégia antes do roteiro · PADRÃO CONSISTENTE (proposto), 3 clientes

**O que entra.** Um documento com a lógica de `sirius-scale/frameworks/lhto.md` preenchida com o dado do dossiê:
ponto A → B → C, regra de crença, desejos e mecanismos, conclusão inevitável, premissas e pontos lógicos, tipo de
tese, ângulos de lead, quadro de objeções. O roteiro executa esse documento. Nos três clientes ele existe: o
documento de peças estratégicas (caso A), a estrutura estratégica da VSL (caso C) e o briefing do caso B, montado
a partir da fundação estratégica do funil.

**Por quê.** O método põe essa lógica "antes de escrever uma linha" (`sirius-scale/frameworks/lhto.md` §2), e o
Rodrigo deixou a mesma ordem escrita como regra de processo no projeto do caso C: "Entregar rascunho antes de ter
contexto completo é falha de processo." Na prática, o documento estratégico é o que o `copy` recebe como fonte de
ângulo e o que a revisão usa pra conferir: o briefing do caso A manda o `copy` ler as seções de tese, de leads e
criativos e de objeções do documento estratégico, e uma dúvida do `/revisar` da v2 caiu porque o revisor não
tinha aberto esse documento, que tinha as três respostas.

**Variações aceitáveis.** O documento estratégico pode ser mais velho que a oferta. No caso A ele seguiu valendo
pra tese, premissas, pontos lógicos e objeções, e os números de oferta dele foram declarados superados numa tabela
"lá × hoje" no briefing, pra ninguém copiar preço velho.

**Trecho real.**
- "mapa da jornada emocional, conclusão inevitável, premissas da tese e regras de crença vêm antes dos roteiros."
  (Fonte C, forma de trabalho)
- "Aquele documento é a estratégia LHTO desta VSL e continua valendo em tese, premissas, pontos lógicos e quadro de
  objeções." (Fonte A, briefing)
- O briefing do caso B aponta como fonte da tese a cópia da fundação estratégica do funil.

---

## Etapa 3 — Desenhar a gravação antes do texto · PADRÃO CONSISTENTE (proposto); item 1 em 3 clientes, 2 e 3 em 2, o 4 ISOLADA

**O que entra.**

1. **Leads intercambiáveis + corpo fixo** (3 clientes). Cada lead é um take separado, todas terminam na mesma
   transição, e o corpo começa numa frase que funciona depois de qualquer uma. Na edição, troca-se a lead e o resto
   fica. Foi o formato das três VSLs da base. (Quantos hooks e de que tamanho: etapa 7.)
2. **O que vai mudar depois não fica na fala** (2 clientes, casos A e B). O que se espera trocar (o depoimento na
   tela, o texto do botão, o público morno que acaba) sai do áudio, pra trocar sem regravar. Decisões do Rodrigo,
   uma de cada vez, em passadas seguidas: nenhum nome de aluno na fala; a fala descreve o que o depoimento prova e
   não conta o caso (regra completa em `sirius-scale/frameworks/oferta-14-secoes.md` §5); o botão não é falado, a
   fala aponta pro botão sem dizer o texto dele (a exceção, num vídeo de upsell, está em
   `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md`); VSL escrita pra frio, sem "você já me acompanha"
   (caso B).
3. **Bloco compartilhado não carrega o que muda entre versões** (2 clientes, casos A e B). Quando a mesma gravação
   serve a mais de uma versão, o trecho comum não cita produto, preço, moeda, entrega ou, se o público muda de
   composição, gênero. Três casos: duas VSLs com tronco comum (etapa 8, caso A); corpo único com bloco de preço por
   mercado (caso B, `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §0.1); VSL enxuta com blocos de costura pra
   versão longa (caso B, direção §9).
4. **O que a VSL gasta e o que guarda** (VARIAÇÃO ISOLADA, 2 clientes). Antes de escrever, separar quais provas,
   autoridades e dores ficam na VSL e quais ficam pra próxima peça do funil, pra VSL não queimar o que o upsell vai
   precisar. A VSL é escrita primeiro. ⚠️ No caso B a separação ficou no papel: o plano guardou um número de
   autoridade do expert pro upsell, e o número já estava na VSL no ar e no hook 2 que o Rodrigo escreveu. A
   revisão dos hooks editados devolveu isso pra decisão dele.

**Por quê.** O recurso escasso é a sessão de gravação do expert (regra transversal 1). Cada item acima existe pra
uma gravação durar mais e servir a mais testes.

**Variações aceitáveis.** O número de leads (5 a 10). Tronco comum só onde um produto não contém o outro (o curso
do caso A não contém o livro). Corpo neutro de gênero só quando o público das versões muda (no caso B, o segundo
mercado tinha outro público: lá o comprador é 82% masculino, e o roteiro antigo era escrito no feminino).

**Trecho real.**
- "Todas terminam no mesmo gancho de transição para a História." e "Na edição, basta trocar a lead e manter o
  restante intacto." (Fonte A, a v1)
- "Formato: 5 Hooks independentes + 1 Corpo único" (Fonte B, a VSL no ar)
- "Esse bloco entra logo após a lead escolhida. A transição deve ser natural" (Fonte C, VSL v1.0, no começo da
  História)
- "Pra gente testar outros depoimentos" (Rodrigo, Fonte A, registro da v4 §Q)
- "texto exato do botão é trabalho da estratégia de página, não da copy do roteiro" e "sem regravar se o texto do
  botão mudar depois" (Fonte A, histórico de decisões)
- "senão amarra a peça a um público que acaba e obriga a regravar" (Fonte B, plano de produção §0)
- "a fala descreve o que o depoimento prova, não quem é a pessoa." (Fonte A, registro da v5, cabeçalho)
- "depende do que a peça 1 gastou" (Fonte A, briefing, ordem de trabalho) e "O que a VSL guarda para o upsell
  (planejar agora evita retrabalho)" (Fonte B, plano de produção §3.2)
- O furo do item 4, no caso B: o mesmo número de autoridade estava na VSL no ar e no hook 2, e a revisão dos
  hooks editados registrou que os planos "guardavam esse número pro upsell".

---

## Etapa 4 — Primeira versão pelo `copy`, com marcador no lugar do que falta · PADRÃO CONSISTENTE (proposto)

*3 roteiros escritos no registro da casa (2 clientes), contra 3 roteiros anteriores a ele (3 clientes).*

**O que entra.** O agente `copy` recebe o dossiê, a estratégia, a peça, a duração e as regras duras, e entrega o
roteiro inteiro, pronto pra teleprompter, com tempo por bloco (`.claude/agents/copy.md`, a parte de roteiro). O que
depende do cliente e não está em arquivo vira marcador visível, no ponto exato: `[[INSERIR]]` pra prova que entra
na tela, `[[CONFIRMAR COM <pessoa>]]` pra pergunta, `[A CONFIRMAR]` pra número que só fecha depois (as páginas do
livro, que dependiam da gráfica). Marcador novo leva o motivo escrito ao lado.

**Por quê.** Os três roteiros feitos antes do registro da casa, todos no modelo LHTO, chegaram com fato assumido:
estatística que nenhuma pesquisa sustenta (caso A), âncora de preço sem fonte (caso B), garantia assumida e bônus
que some "nas próximas horas" num perpétuo (caso C). O método externo de roteiro de VSL (o "PROMPT PARA CRIAÇÃO DE
VSL", que não faz parte deste kit) manda assumir e marcar `[[ASSUMIDO]]`; a casa manda perguntar e parar
(`sirius-scale/REGRAS.md` §2; `sirius-scale/frameworks/lhto.md` §10). Onde as duas instruções colidem, a casa vence:
o método foi escrito pra quem escreve sozinho, e aqui o dado real do cliente está a um arquivo de distância. Nos
três roteiros escritos no registro da casa não há nenhum `[[ASSUMIDO]]`.

**Variações aceitáveis.** Lapidação: o roteiro existe e o `copy` mexe só no que o briefing pede, deixando como está
o que já foi aprovado e não viola nada (caso A, v2). Peça nova: direção e teleprompter do zero (caso B). Prova que
só o expert tem pode virar andaime: a frase escrita, com o buraco do dado no meio, pra ele preencher sem reescrever
(a Lead 2 do caso A, em volta de um documento público).

**Trecho real.**
- `[[ASSUMIDO]]` "fica valendo só pra decisão de forma (duração de bloco, ordem de dois argumentos), nunca pra
  número, preço, depoimento ou dor de avatar" (regra da casa)
- "Prazo de garantia: assumi 7 dias. Confirmar se será 7 ou 15 dias." (Fonte C, VSL v1.0, notas pra equipe)
- [Frase que prende um bônus às próximas horas.] (mesmo arquivo, Seção 14; o briefing do caso C lista
  isso como escassez falsa se a página não tirar o bônus)
- "Número inventado no script atual, sem fonte." (Fonte B, direção §6, sobre a âncora de preço da VSL que estava no
  ar)
- [Percentual atribuído a uma pesquisa da casa] (Fonte A, v1, Seção 10), que saiu na v2 porque "os dois números
  não rastreiam até nenhuma pesquisa da casa." (registro da v2, item 22)
- "Preencher com dado inventado era o erro mais caro possível aqui." (mesmo registro, "O que NÃO mudou", item 3)
- Na v5, a frase que fica em volta do `[[INSERIR]]` da Lead 2 diz onde o dado está publicado, em número, antes do
  momento em que ele pesa, pra qualquer pessoa conferir (Fonte A, v5, Lead 2).
- "`[[INSERIR]]` novo só com o motivo escrito." (regra do agente `copy` da casa)

---

## Etapa 5 — Fechar cada versão e abrir a seguinte · PADRÃO CONSISTENTE (proposto), base de um cliente (7 passadas)

**O que entra.** Cada versão é o roteiro inteiro, num arquivo novo (`<nome>-v<N>.md`), com o registro ao lado
(`<nome>-v<N>-mudancas.md`). A anterior nunca é sobrescrita, e o cabeçalho de cada versão diz o que ela aplica e
onde está o registro. O registro tem:

1. **Uma entrada por mudança**, numerada numa sequência que atravessa as versões (Frente A: 1 a 36 na v2, 37 a 54
   na v3, 55 a 72 na v4, 73 a 83 na v5), com onde, o que (antes → depois, quando a mudança é de fala), por quê e a
   fonte.
2. **O que ficou igual**, conferido trecho a trecho, e as **regras conferidas antes de fechar**: termos proibidos,
   número falado, verbatim, nome de aluno, contagem de credencial e de "centenas" por visualização.
3. **A conferência do orquestrador** depois da entrega do `copy` (diff contra a versão anterior e entre blocos
   compartilhados, número contra a fonte, verbatim contra o catálogo), com as correções dele como entradas novas
   (31 a 33; 52 a 54), e as correções que o `/revisar` achar no próprio registro (34 a 36).
4. **O que, fora do arquivo, depende dele**: doc de gravação a regenerar, ficha de outra peça a corrigir.

A passada seguinte é aberta por **um gatilho só e aplica só ele**: o briefing com as pendências do avatar (v2), as
decisões do Rodrigo depois do `/revisar` (v3), a revisão de leads aprovada (v4), uma regra nova de depoimento (v5),
uma mudança de oferta (Frente B, v3).

**Por quê.** Foram sete passadas em três dias, com o Rodrigo decidindo em cima de cada uma. A revisão dele é a
parte cara do processo, e o registro existe pra ela render: sem ele, ninguém saberia o que mudou, e não daria pra
provar que mexer numa decisão não mexeu no resto do que já estava aprovado. O registro também pega erro: o
`/revisar` da v2 achou o registro impreciso em dois pontos, uma remoção feita e não registrada e uma entrada que
dizia "mantido inteiro" sobre um trecho que tinha mudado.

**Variações aceitáveis.** Registro por seção em vez de por entrada (Frente B, v1, peça nova sobre blocos copiados).
Decisão pequena do Rodrigo depois da entrega vira entrada no mesmo registro, não versão nova (item 72, um detalhe
do presente). Doc de gravação regenerado no mesmo link a cada passada.

**Trecho real.**
- "a regra da peça era lapidar o que o briefing pediu, não reescrever por gosto" (Fonte A, registro da v2,
  cabeçalho)
- "Esta passada aplica só as decisões que o Rodrigo tomou depois do /revisar da v2" (Fonte A, registro da v3)
- "Nenhuma versão sobrescreve a anterior, e quem abrir o arquivo precisa saber em qual está." (mesmo registro,
  item 51)
- "Checklist errado é pior que checklist ausente." (Fonte A, registro da v4, item 71)
- "Conferir por diff que Leads, História e PL1–6 são idênticos à v4." (Fonte A, arquitetura da Frente B §6)
- "atualiza no lugar, mesmos links" (Fonte A, histórico de decisões, sobre os docs de gravação)
- Rodrigo, D2, sobre o custo de revisar copy: "eu tenho que pegar parágrafo, parágrafo, mandar, discutir, falar,
  reescrever e tal, pra arrumar."

⚠️ Depois disso, o Rodrigo decidiu, pros docs que vão pra equipe e pro expert, uma peça por doc, corrigida no mesmo
link, sem "V1/V2" no nome (Fonte E). Os docs de gravação da VSL já eram assim. Se o arquivo-fonte de uma VSL nova
também deve perder o número de versão é ponto em aberto (§6, item 5).

---

## Etapa 6 — Revisar leads e hooks contra o público · VARIAÇÃO ISOLADA (2 revisões, 2 clientes)

**O que entra.**

1. Onde o público está: nível de consciência lido do avatar e quanto dele é saturado.
2. O tipo de cada lead (`sirius-scale/frameworks/copy/great-leads.md`) ou o que o dado mediu de cada hook.
3. Os furos: lead que repete o corpo; proclamação que afirma e não prova dentro dela (a lead roda sozinha no
   anúncio, então a prova tem que estar lá); tipo que falta; hook escrito pra dor de lead e não pra dor de quem
   compra; todos da mesma origem.
4. Propostas numeradas, **sem reescrever**. O texto novo sai do `copy` na passada seguinte, depois que o dono
   decide.

**Por quê.** A lead é o pedaço que mais roda sozinho (vira anúncio) e o que decide quem chega ao corpo. Uma revisão
fora do texto, contra o público, pega o que a lapidação linha a linha não pega: no caso A, a Lead 1 contava a mesma
história que o corpo fixo contava três minutos depois.

**Variações aceitáveis.** Sem dado de hook (VSL nunca gravada): revisão por tipo, pelo Great Leads (caso A, 8
leads: 4 Problema-Solução, 2 Proclamação, 1 mista, 1 História, nenhum Segredo; três propostas, as três aprovadas).
Com dado: nota por hook contra o teste e contra o comprador (caso B, 6 hooks: 2 prioridade, 2 testar, 2 segurar;
três correções antes de gravar, e a que propunha falar com quem já conhecia o expert foi vetada pela decisão de
escrever pra frio).

**Trecho real.**
- "a nossa termina onde o corpo recomeça." (Fonte A, revisão das leads §3.1)
- "Nos anúncios, a lead roda sozinha." (mesmo arquivo, §3.2)
- "o texto novo sai pelo agente copy" (mesmo arquivo, cabeçalho)
- "o framework diz que tipo testar, não qual vence" (mesmo arquivo, §4)
- "Rodrigo aprovou as três propostas das leads" (Fonte A, histórico de decisões)
- "Nota por hook, contra o que o teste mediu e contra o comprador real" e "Nenhum dos 6 vem do [...]" (Fonte B,
  análise de hooks §6; o colchete é o anúncio campeão de venda direta, que não leva pra VSL)

---

## Etapa 7 — Hooks: quantos (PADRÃO CONSISTENTE, proposto), de que tamanho e como escolher (VARIAÇÃO ISOLADA)

**O que entra.**

- **Quantos — PADRÃO CONSISTENTE (proposto).** De 5 a 10 por gravação, pra testar. É o que o Rodrigo faz e ensina
  (D6 e D7), e foi o que as três VSLs da base tiveram (5, 8 e 10). Hook novo é produção recorrente, não só da
  primeira sessão: a rodada 2 do caso B foi gravada meses depois do corpo e montada nele, que já rodava, e a
  proposta de trabalho ao caso C põe hook novo na lista do que o expert grava com constância (D3).
- **De que tamanho — VARIAÇÃO ISOLADA, com hipótese INCONCLUSIVA.** Curto. No único caso medido, a retenção é lida
  em 01:00, os hooks do split tinham de 72 a 87 segundos, e 82% das pessoas saíram no meio do hook. A rodada 2 foi
  escrita com 33 a 44 segundos e ficou com 26 a 31 na versão vertical editada. O `sirius-scale/frameworks/lhto.md`
  §5.6 pede de 30 segundos a 1 minuto. Que encurtar aumenta a venda é PADRÃO INCONCLUSIVO: os hooks curtos foram
  gravados e editados, e o número deles não está registrado.
- **De onde vem — VARIAÇÃO ISOLADA.** Versão curta do hook que mais vendeu (os hooks 1 e 4 da rodada 2 são o H1 e o
  H4 encurtados, mesma cena), ângulo tirado da pesquisa de comprador, a palavra literal de quem compra. Ainda não
  usado em nenhuma das três: hook nascido de anúncio que já vendeu (`sirius-scale/frameworks/lhto.md` §5.1).
- **Como escolher — VARIAÇÃO ISOLADA (1 medição).** Pela venda e pela receita por play, num split simultâneo; hook
  rodado em período diferente não se compara com outro. Retenção diz onde a peça perde gente, não quem ganha. O
  alerta veio do caso B: na série de 5 hooks, o de melhor retenção ao pitch ficou em 4º em conversão, com o pior
  play rate (menos gente apertava play, quem apertava era mais comprometida). Mas essa série mistura janelas (H1 e
  H2 rodaram antes do H3 ao H5) e, contra o H1 da mesma janela, a diferença de conversão não foi conclusiva
  (p=0,086). Dentro do split simultâneo, retenção e conversão concordaram. É alerta de método, não medida.
- **Que ângulo — PADRÃO INCONCLUSIVO.** No split simultâneo, o hook de história datada converteu mais que o de
  violação de expectativa e o de future pacing (0,71% contra 0,39% e 0,21% por play), sem teste de significância da
  conversão registrado. O hook de cena do dia de trabalho do público (H1) teve o melhor número da série, mas rodou
  em outra janela e não entra na comparação.

- **Hook curto com ponte fixa — VARIAÇÃO ISOLADA (desenho de 1 caso, ainda sem número).** No caso A, as leads longas
  (de 1:30 a 3 minutos) saíram da gravação. Entraram aberturas de até 45 s e uma ponte de 30 a 40 s, gravada uma vez,
  que diz o nome e a credencial do expert, tira a culpa da pessoa e diz o que ela vê até o fim, quase toda com frases
  que o expert já tinha validado. A ponte existe porque o corpo da VSL nunca dizia o nome do expert: hook emendado
  direto na História deixaria o vídeo sem quem fala. Uma lead longa ficou como controle contra o hook curto da mesma
  cena, pro teste medir só o tamanho.
**Por quê.** É o maior vazamento medido e o pedaço mais barato de regravar: o corpo fica.

**Variações aceitáveis.** Lead de troca longa (2 a 4 minutos no caso A) no lugar do hook de até 1 minuto: não
testado. Testar o ângulo no anúncio antes de gravar a VSL (`sirius-scale/frameworks/lhto.md` §5.7) foi recomendado
no caso B e invertido pelo Rodrigo ("escreve e grava tudo hoje"); qual ordem rende mais não foi medido.

**Trecho real.**
- Rodrigo, D6: "quando você for gravar a VSL já faz uns 5 a 10 hooks diferentes no primeiro minuto, pra você ficar
  testando"
- Rodrigo, D7: "Então quando eu vou gravar uma VSL, eu gravo de 5 a 10 hooks versões diferentes" e "quando tem
  hook ruim, eu já descarto, tem que manter 60% acima do primeiro minuto"
- Rodrigo, D3: "Ah, VSL, um hook da VSL novo, ah, uma oferta nova."
- "A retenção de 01:00 é medida antes de qualquer um deles terminar." (Fonte B, análise de hooks §1)
- "Julgar por conversão e receita por play, não por retenção." (mesma análise, §3.4)
- "Só split simultâneo compara" (mesma análise, §8)
- "retenção e conversão concordaram e o H4 venceu nos dois" (mesma análise, §3.2, sobre o split simultâneo)
- "converte mais que violação de expectativa e que future pacing" (mesma análise, §8, item 1, que a análise
  registrou como VARIAÇÃO ISOLADA; aqui fica INCONCLUSIVO pelos dois motivos acima)
- "A lead que fica é a que vende, não a que retém" (Fonte A, registro da v2, item 29)

---

## Etapa 8 — Duas VSLs com tronco comum · VARIAÇÃO ISOLADA (1 caso, caso A; não gravado)

**O que entra.** Quando o mesmo avatar entra por dois produtos (Frente A pelo livro, Frente B pelo curso), a
gravação de uma serve à outra até onde nenhum bloco cita produto: as leads, a História e os pontos lógicos 1 a 6. A
segunda diverge no ponto lógico que canaliza pro mecanismo do produto dela (PL7), na conclusão inevitável, na
oferta inteira, no pós-pitch, nos CTAs e nas headlines. Como foi feito:

1. Antes do `copy`, um documento de arquitetura: o que se copia verbatim (com a faixa IDÊNTICO À FRENTE A no topo de
   cada bloco), onde diverge, a tabela das 14 seções com a fonte de cada uma, a lista fechada de números que entram
   e que não entram, a entrega esperada e a conferência de depois.
2. O `copy` escreve; o orquestrador confere por diff que o tronco ficou idêntico.
3. Frase do tronco que parecer conflitar com a segunda frente não é adaptada: vira ponto de atenção no registro
   (seis, na v1 da B).
4. Mudança posterior num bloco do tronco entra igual nos dois arquivos, na mesma passada.
5. O roteiro traz uma ficha de gravação compartilhada: o que se grava uma vez, o que é só da segunda, e as regras
   de continuidade.

**Por quê.** São duas VSLs com uma diária a mais só pra parte exclusiva. E o ganho acaba no primeiro ajuste de uma
frase do tronco pra servir só a um dos produtos.

**Variações aceitáveis.** A frente de ticket maior pediu prova mais pesada e uma prova que só o produto dela tem (um
trecho de aula real). A lead que vencer numa frente é testada de novo na outra. O mesmo depoimento pode aparecer nas
duas frentes; a regra de não repetir vale entre a VSL e o upsell dela.

**Trecho real.**
- "Motivo: nenhum desses blocos cita produto. Uma gravação serve às duas VSLs." (Fonte A, arquitetura da Frente B
  §1)
- "Se alguma frase parecer conflitar com a B, não alterar: registrar como ponto de atenção no arquivo de mudanças."
  (mesmo arquivo, §1)
- "adaptar teria destruído exatamente o ganho que justifica copiar" (Fonte A, registro da Frente B v1 §1)
- "Se mudar, deixa de ser um take só e vira duas gravações." (Fonte A, Frente B v3, ficha de gravação
  compartilhada)
- "Se um dia mudar num arquivo, muda no outro." (Fonte A, registro da v5 §W)
- "a lead que vencer na A não é automaticamente a que vence na B." (Fonte A, Frente B v3, notas de produção)

---

## Etapa 9 — Doc de gravação, direção e teleprompter · PADRÃO CONSISTENTE (proposto); itens 1, 4, 5 e 6 em 2 clientes, 2 e 3 em 1

**O que entra.**

1. **O que vai pro expert é só texto de gravação** (2 clientes na prática, casos A e B; no caso C é regra escrita,
   ver Por quê). Um documento por vídeo (duas VSLs com tronco comum dividem um), com título, uma linha de contexto,
   como ler, a fala e a rubrica curta. Notas de produção, provas a inserir, rastreio de número, decisões e estrutura
   de página ficam num documento interno e no arquivo-fonte.
2. **O arquivo-fonte manda, o doc é a cópia** (caso A). O doc é gerado do roteiro, nunca editado à mão, com
   convenção fixa: itálico entre colchetes é cena e tom e não se fala; o sinal ► marca o que entra na tela ou uma
   pergunta pro expert; marcador interno vira aviso curto. Correção regenera o doc no mesmo link.
3. **Teleprompter e direção em dois arquivos** (caso B, em toda a copy dele). O teleprompter tem frase curta, quebra
   onde se respira e nenhuma cena; a direção leva plano, insert, b-roll, gráfico, costuras e ordem de gravação.
   Correção num tem que ir pro outro. No caso A a direção ficou no documento interno de produção, e o doc de
   gravação guarda só a rubrica curta.
4. **Escrito pra ser lido em voz alta, na voz do expert** (2 clientes, e a fala do Rodrigo em D9). Sai a frase que
   trava a leitura (sobra de versão anterior, objeto antes do sujeito). Rubrica entra só quando o expert precisa
   saber o que está fazendo, como ler um print em voz alta. Texto novo usa o bordão medido dele.
5. **Ordem de gravação escrita** (2 clientes). Caso A: leads separadas, depois o tronco comum, depois a parte
   exclusiva de cada frente, com o mesmo figurino, fundo e enquadramento onde a gravação é compartilhada. Caso B: o
   corpo principal inteiro na sequência, depois os blocos de preço, depois as costuras.
6. **Duração estimada e ordem de corte** (2 clientes). A estimativa por palavra vale até gravar; o roteiro já diz o
   que sai primeiro se passar do tempo e o que não sai (caso A, Frente B; caso B, direção §7).

**Por quê.** O expert abre o doc pra gravar. O Rodrigo devolveu o primeiro doc do caso A por vir com notas e página
junto; o expert do caso B grava com teleprompter, e por isso a copy dele saiu em dois arquivos. No projeto do caso C
a regra estava escrita, mas a VSL dele ainda traz "NOTAS PARA A EQUIPE" no fim do mesmo arquivo do roteiro (Fonte
C, VSL v1.0): lá a regra é escrita, não prática observada na VSL. E o jeito de o expert soar natural lendo é o
texto já estar no jeito que ele fala (D9).

**Variações aceitáveis.** Rubrica curta de cena pode ficar no doc (caso A, em itálico); no teleprompter do caso B,
não. Um doc pras duas VSLs quando têm tronco comum; um doc por vídeo nos outros casos.

**Trecho real.**
- "esse documento é importante ter só o texto para a [...] revisar e depois gravar" (Rodrigo, Fonte E)
- "notas de edição, visual e gravação ficam em documento separado, para não poluir o teleprompter." (Fonte C, forma
  de trabalho)
- "Frases curtas, quebra de linha onde respira, zero colchete, zero indicação de cena." (Fonte B, plano de produção
  §3.4)
- "o que está em itálico entre colchetes é indicação de cena e tom, não se fala." (a convenção do doc de gravação do
  caso A)
- "Mesmo figurino, fundo e enquadramento das partes 3 e 4." (doc de gravação do caso A, ordem de gravação)
- "corpo enxuto inteiro na sequência → os [...] blocos de preço → só depois os blocos de costura" (Fonte B, direção
  §9)
- "Num teleprompter isso trava a leitura." (Fonte A, registro da v2, item 9)
- "Correção em teleprompter precisa se propagar pro arquivo de direção irmão" (Fonte B, pente fino)
- "A VSL é a única com direção de cena dentro do teleprompter" (Fonte B, achado da revisão)
- "Não cortar, em nenhuma hipótese:" (Fonte B, direção §7)
- Rodrigo, D9: "liga a câmera ali, liga o teleprompter e sai lendo daí tem que escrever de uma maneira que é falada
  da maneira que ele fala também, então a gente cria aí DNA do expert aí a cópia sai bem do jeito que ele fala é
  assim que eu faço com os experts"

---

## Etapa 10 — Do roteiro à câmera · VARIAÇÃO ISOLADA (2 clientes)

**O que entra.**

1. O Rodrigo lê o doc antes de mandar. Foi dessa leitura que saíram as decisões sobre depoimento, analogia, um doc
   por vídeo e botão. No negócio de vocês, quem lê antes de mandar é quem aprova a copy.
2. O expert valida o que é dele (conteúdo, voz, o que o produto entrega) e completa o que só ele tem: o documento
   público, a cena, a mensagem real. Preço, página e checkout não entram na validação dele (Fonte E).
3. Grava com teleprompter.
4. O bruto é conferido contra o roteiro pela transcrição, antes de editar: improviso que não muda fato fica, falsa
   largada sai, e número falado diferente do roteiro é apontado. No caso B a fala de um hook disse o número de
   autoridade diferente do roteiro, e a legenda seguiu a fala, com o aviso na entrega (evidência no caso de
   origem).
5. A edição segue o mapa (`sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`).

**Por quê.** É a última trava de fato antes da câmera, e ela só funciona se a revisão do dono veio antes. No caso B,
o pacote escrito de uma vez (criativos, VSL, upsell e downsell) foi pra gravação sem a revisão do Rodrigo; o expert
gravou alguns criativos, parou e reclamou de um termo de dor que o produto não resolve (D2). A VSL do mesmo pacote
ficou esperando revisão antes de ir pra ele gravar.

**Variações aceitáveis.** O ajuste pendente sai da casa antes de o expert validar (caso B, D2) ou o próprio expert
põe os acréscimos e grava direto, sem outra volta (caso A, D5). Quem lê antes de mandar pode ser o gerente do
projeto: no caso B, o gerente ficou de "revisar a VSL que o Claude escreveu (no Drive) e mandar pro [...] gravar"
(ata de D2).

**Trecho real.**
- "Rodrigo manda as VSLs pra [...] hoje." (ata de D1)
- "Reclamou de um termo na copy" (ata de D2; o termo estava nos criativos do pacote) e, do Rodrigo, na mesma call:
  "Eu criei em cima da hora ali."
- "corrigir a copy, [...] valida, [...] grava, sobe e liga o tráfego." (ata de D2)
- A ata de D5 registra que o expert do caso A pode gravar a VSL direto com os acréscimos, sem passar pelo Rodrigo
  antes.
- O expert do caso A, na mesma call, sobre os marcadores do doc: "naquelas caixinhas que você mandou, naqueles
  adesivos"
- "pediu documento no Drive pra revisar e mandar pra [...] gravar" (Fonte A, histórico de decisões)
- A tarefa que fechou o ciclo do caso B foi editar os hooks que o expert gravou (registro do projeto do caso B).

---

## 3. Regras transversais

1. **O gargalo é a gravação do expert, não a escrita. PADRÃO CONSISTENTE (proposto), 3 clientes.** As sete versões
   do caso A saíram em três dias; 17 dias depois da última a VSL ainda não tinha sido gravada, e a gravação foi
   posta depois das peças da Black. O expert do caso B gravou alguns criativos e parou antes dos hooks, e o Rodrigo
   decidiu não criar material novo pra ele enquanto ele não gravasse o que faltava. A proposta ao caso C amarra a
   meta de resultado à constância de gravação. Por isso o plano conta sessões e a etapa 3 existe.
   Trechos: "O recurso escasso aqui é o tempo de gravação do [...]" (Fonte B, plano de produção §4); "que ela já tá
   com duas VSL pra gravar" (Rodrigo, D2); "a gente promete gerar um resultado e você promete gravar com
   constância" (Rodrigo, D3).
2. **Nenhum fato assumido. Regra da casa (`sirius-scale/REGRAS.md` §2), CONSISTENTE.** Ver etapa 4.
3. **Afirmação sobre o expert só se for verdade. PADRÃO CONSISTENTE (proposto), base de um cliente (3 casos).**
   Saíram: uma memória que o expert não tinha (v2, item 31), uma cena que não existia em arquivo (v4, item 57, virou
   pergunta) e o "antes" de um aluno que o catálogo não detalhava (v5, item 75).
   Trecho: "Afirmação sobre a expert que não é verdadeira não entra, mesmo que soe bem" (Fonte A, registro da v2).
4. **Número falado sai de lista fechada, com rastreio. VARIAÇÃO ISOLADA (2 clientes).** Na Frente B, a lista do que
   entra e do que não entra veio na arquitetura, e o roteiro fecha com a tabela de rastreio de cada número. No caso
   B, a prova social usou o número medido (522 compradores, falado como mais de 500) e não somou públicos de
   sobreposição desconhecida. Número que deixa de ser verdade sai sem ser trocado por outro: "Não tem valor
   declarado em arquivo nenhum, então não foi trocado por outro número." (Fonte A, Frente B v3, rastreio).
5. **A voz do expert vence a forma do template. PADRÃO CONSISTENTE (proposto), base de um cliente (4 casos).** A
   anáfora do "não importa se" foi quebrada (`sirius-scale/frameworks/oferta-14-secoes.md` §4), a credencial passou
   a uma por bloco em roteiro longo (ficha de voz do expert), o "apenas" antes do preço saiu, a tríade da fonte não
   entrou no texto novo. Trecho: "Repetição assim é paia mesmo" (Rodrigo, registro da v3 §I).
6. **Analogia sai do mundo do avatar. VARIAÇÃO ISOLADA (1 reprovação).** Trecho: "ficou bem estranha, eu não
   entendi nada e acho que não tem nada a ver com o avatar" (Rodrigo sobre a analogia da costureira, Fonte A,
   registro da Frente B v2). A regra ficou no agente `copy` (`.claude/agents/copy.md`).
7. **Decisão que muda a oferta propaga pra todas as peças, fichas e docs. VARIAÇÃO ISOLADA, com um furo
   registrado.** A decisão sobre o downsell da Frente A chegou na VSL B e no doc de gravação, e não chegou nas duas
   fichas da v5 da A, que ainda descrevem o downsell antigo. A regra geral veio depois: produto primeiro, depois
   busca do preço velho em todas as peças (Fonte E).
8. **Escassez só a verdadeira, e a verdade muda de página pra página. Regra da casa**
   (`sirius-scale/frameworks/oferta-14-secoes.md` §14, `sirius-scale/frameworks/lhto.md` §11). No funil do caso A, o
   botão de um clique sumir é verdade nas páginas de upsell e downsell e não na página da VSL, e por isso não entrou
   na VSL. Trecho: "Isso é verdade nas páginas de upsell e downsell (botão de um clique dentro da compra ativa), não
   na página da VSL" (Fonte A, registro da v2, item 32).
9. **`/humanizer` antes de dar por final. Regra da casa** (`sirius-scale/REGRAS.md` §3). Ela entrou em vigor depois
   das candidatas do caso A, que não passaram por ela.
10. **Quem faz o quê. VARIAÇÃO ISOLADA (1 cliente), sobre regra da casa (`sirius-scale/REGRAS.md` §3).** O
    orquestrador monta o briefing, desenha a arquitetura e confere; o `copy` escreve; o `/revisar` confere de olhos
    frescos; o Rodrigo decide (no negócio de vocês, quem aprova a copy); o expert valida e grava. Trecho: "É a
    decisão de arquitetura; a escrita é do copy, em Opus, como nas peças anteriores." (Fonte A, arquitetura da
    Frente B).

### Checklist de saída pra gravação — PADRÃO CONSISTENTE (proposto) só nos dois primeiros blocos

**Se repetiu nos dois clientes** (nas conferências do caso A e na revisão das peças do caso B):

- [ ] Todo número falado está na lista fechada e tem fonte.
- [ ] Termos e provas proibidos do cliente: zero (no caso A, promessa de resultado garantido, "apenas" antes de
      preço, "carrinho", "lançamento"; no caso B, a prova social sem fonte).
- [ ] Nenhuma frase do corpo compartilhado que só vale numa versão: produto da outra frente (caso A), mercado ou
      gênero (no caso B, o Rodrigo barrou a promessa de entrega física numa peça que também ia virar a versão do
      segundo mercado).
- [ ] Linguagem de IA da lista de tom da casa (`sirius-scale/REGRAS.md` §1): zero.

**Se repetiu de passada em passada, mas só no caso A** (base de um cliente):

- [ ] Nenhum nome de aluno na fala (da v4 em diante); em depoimento de vídeo, nenhum detalhe do caso (da v5 em
      diante).
- [ ] Escassez só a que é verdade na página onde ela é dita.
- [ ] Afirmação sobre o expert: só o que ele viveu e está em arquivo ou na fala dele.
- [ ] Bloco compartilhado idêntico, por diff, nas duas frentes.

**De um cliente só, VARIAÇÃO ISOLADA:**

- [ ] Teleprompter sem cena, e direção sincronizada com ele (caso B).

**Regra da casa que ainda não rodou em VSL nenhuma:**

- [ ] Decisão posterior à versão aplicada em todas as peças, fichas e docs (Fonte E; o furo da regra 7).
- [ ] `/humanizer` rodado no texto inteiro (`sirius-scale/REGRAS.md` §3; regra 9).

Trecho: "Todo número falado no script rastreia" (Fonte A, registro da v2, regras conferidas antes de fechar).

---

## 4. Exemplos consolidados (em molde: o colchete diz o que a frase faz)

**A. Lead que repetia o corpo → lead que conta outro momento** (caso A, v3 → v4). Pedido do Rodrigo: "Repetir fica
ruim" (registro da v4 §N). A Lead 1 deixou de contar a virada que a História conta e passou a contar outro momento
da trajetória do expert, o convite que mudou a carreira dele, com frases tiradas do roteiro de uma live anterior,
do jeito que ele disse lá. No molde: [o convite que mudou a carreira] + [o que ele passou a fazer] + [o que ele
passou a fazer], em frases curtas.

**B. Proclamação que afirmava sem provar → prova dentro da lead** (caso A, v4). Depois de uma afirmação forte, com
número, sobre como o público é avaliado, entrou [uma frase que diz que aquilo não é opinião do expert], seguida do `[[INSERIR]]` da fonte
pública e de uma frase que diz onde a pessoa confere. No molde: [afirmação forte, com número] + [não é opinião do
expert] + `[[INSERIR: a fonte pública, na tela]]` + [onde está publicado, pra pessoa conferir]. O expert ficou de buscar a fonte e gravar direto (D5).

**C. Depoimento contado → depoimento lido** (caso A, v4 → v5). Antes, a fala contava quem era a aluna (a profissão
dela e a crença que ela tinha). Depois: [frase que apresenta a mensagem de uma aluna] + a leitura do print + uma
frase sobre o que o resultado prova, sem contar o caso (registro da v5, item 77). A frase de depois, no molde:
[o que o trabalho feito com critério muda no resultado].

**D. Analogia de ofício alheio → analogia do dia do avatar** (caso A, Frente B, v1 → v2). Antes: [uma analogia com um
ofício que o público não vive]. Depois, uma cena que o público vive toda semana, errar e conferir a resposta (registro da Frente B v2,
item 4). No molde: [convida a lembrar de uma cena do dia a dia dele] + [o erro nessa cena] e, no fecho,
[a diferença entre saber que o critério existe e enxergar ele no próprio trabalho, que é o que o produto dá].

**E. Soma que deixou de ser verdade → recapitulação sem soma** (caso A, Frente B, v2 → v3). Antes: [a soma do que
tem preço, comprado separado] + [o preço] + [a garantia].
Depois: [o preço] + [a garantia], sem a soma (registro da Frente B v3, item 2).

**F. Hook que mais vendeu → a mesma cena, em versão curta** (caso B, VSL no ar → rodada 2). O H1 (1,05% de conversão
por play) abria com [um pedido de sinceridade] e só depois de algumas frases chegava à cena do
problema técnico que o público vive no trabalho. O hook 1 da rodada 2, escrito pelo Rodrigo com 40 segundos, abre
direto na cena. No molde: [o sinal visível do problema] + [o retrabalho que a pessoa já sabe que vem].

**G. Estatística sem fonte → número da pesquisa** (caso A, v1 → v2). Antes: [percentual atribuído a uma pesquisa
da casa] (v1, Seção 10), sem pesquisa que sustentasse. Depois: [N de cada 100 responderam o que a pesquisa mediu, em
linguagem de gente] (registro da v2, item 22).

**H. A ficha de gravação compartilhada** (caso A, Frente B, v3). "O corpo compartilhado não muda de figurino,
fundo, enquadramento nem marcação de chão entre as duas VSLs." e "Nenhum bloco compartilhado cita produto."

---

## 5. O que é reutilizável e o que é do caso

**Transfere (é processo, não depende do nicho):**

- As etapas 0 a 7, 9 e 10, o checklist de saída e as regras transversais. A etapa 8 só transfere quando dois
  produtos que não se contêm vão pro mesmo avatar.
- O desenho de gravação da etapa 3: leads de troca sobre corpo fixo, o que muda fora da fala, bloco compartilhado
  sem o que varia.
- Escolher hook por venda em split simultâneo, com retenção como diagnóstico (etapa 7).
- O que a sequência do caso A deixou pronto pra próxima VSL: as regras que nasceram nas passadas 3 a 5 (nome fora da
  fala, depoimento não contado, botão não falado, credencial por bloco, anáfora quebrada) já estão escritas em
  `sirius-scale/frameworks/oferta-14-secoes.md` §4 e §5, na ficha de voz do expert (no negócio de vocês,
  `expert/dna-expert.md`) e no agente `copy` (`.claude/agents/copy.md`), e entram no briefing da primeira versão.

**Transfere como mecanismo, com o valor do caso:** o número de hooks (5 a 10), o tamanho do hook, a proporção entre
tronco comum e parte exclusiva, a ordem de gravação.

**É do caso (não generalizar sem medir):**

- A credencial do expert do caso A e a cota dela por bloco; "centenas" ou "milhares"; os termos proibidos do caso
  A. São da voz e da marca dele.
- As 8 leads de 2 a 4 minutos do caso A.
- O tronco comum entre duas frentes: depende de dois produtos que não se contêm, vendidos ao mesmo avatar.
- O corpo neutro de gênero e o bloco de preço por mercado: vêm do caso B vender em mais de um mercado, e o segundo
  mercado tinha outro público.
- O botão de um clique como escassez verdadeira: é mecânica da Hotmart e vale só nas páginas de upsell e downsell.
- Todo número: os 1,05% e os 16% a 20% do caso B, o ROAS de 2,19 do caso C.

---

## 6. Pontos em aberto

1. **Nenhuma VSL feita pelo processo inteiro tinha sido gravada quando este arquivo fechou.** As duas do caso A eram
   candidatas desde a semana das versões, e quase três semanas depois ficou combinado que a gravação viria depois
   das peças da Black. A enxuta do caso B não tinha sido gravada duas semanas e meia depois de escrita, e mais de um
   mês depois não existia corpo horizontal gravado. O processo foi executado; o resultado dele é desconhecido.
2. **Os seis hooks curtos do caso B** foram gravados, editados e entregues em duas levas. Se rodaram e quanto
   venderam não está registrado. É o teste que diria se encurtar o hook melhora a venda (PADRÃO INCONCLUSIVO), e a
   pergunta H1 × H4 em split simultâneo continua aberta.
3. **Lead de troca de 2 a 4 minutos (caso A) × hook de até 1 minuto** (caso B, `sirius-scale/frameworks/lhto.md`
   §5.6). Nunca testados lado a lado. Se as leads do caso A forem gravadas como estão, a retenção do minuto 1 é
   medida no meio delas.
4. **O piso de 60% no minuto 1 descarta o hook ou só aponta onde mexer?** Na fala de D7 ele descarta. No caso B todos
   os hooks ficaram entre 16% e 20%, e o que mais vendeu estava entre eles.
5. **Nome do arquivo de uma VSL nova:** versões lado a lado (`-v2` a `-v5`, como no caso A) ou nome único com a
   versão velha numa pasta de anteriores, como a correção do Rodrigo sobre docs sugere pro arquivo-fonte? O registro
   de mudanças serve aos dois jeitos.
6. **Antes de o expert do caso A gravar**, as candidatas (A v5 e B v3) precisam de três ajustes que vieram depois
   delas: a passada do `/humanizer`, "centenas" virando "milhares" (a ficha de voz mudou) e as fichas da v5 da A com
   o downsell novo. E as pendências de prova continuam abertas: a fonte pública (PL1 e Lead 2), dois materiais de
   critério (PL3 e PL4), um antes e depois (PL5, que na Frente B "deixa de ser pendência média e vira bloqueio da
   Frente B"), a cena da Lead 1, as mensagens das Leads 7 e 8, parcela, boleto, número de páginas, um vídeo de
   depoimento a localizar e o trecho de aula real. A lição: marcador de prova se acumula, e a gravação espera por
   todos eles.
7. **Origem das leads.** O `sirius-scale/frameworks/lhto.md` §5.4 pede 4 leads de 4 origens. A base teve 5, 8 e 10,
   e as 6 novas do caso B saíram da mesma origem. Lead nascida de anúncio que já vendeu não foi feita em nenhuma das
   três.
8. **Testar o ângulo no anúncio antes de gravar** (`sirius-scale/frameworks/lhto.md` §5.7) **ou gravar tudo de uma
   vez** (decisão do Rodrigo no caso B): não medido.
9. **VSL enxuta com LHTO completo e 14 seções não coube em 11 minutos** na estimativa (12:54 a 150 palavras por
   minuto). PADRÃO INCONCLUSIVO, 1 peça, não gravada.
10. **Gravação única** (tronco comum, bloco por mercado): não se sabe se o corpo genérico perde conversão. Nada
    gravado ainda (`sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §0.1 tem a mesma pendência).
11. **Expert que não lê bem no teleprompter.** Em D9 o Rodrigo disse "A gente tem umas técnicas para a pessoa ler e
    tal, mas aí tem que conversar com ele, né?", sem dizer quais. Não há evidência delas no registro da casa.
12. **Qual versão da VSL do caso C está no ar:** não confirmado (Fonte C, briefing).
13. **Os dois projetos em que o LHTO foi validado** (`sirius-scale/frameworks/lhto.md`, cabeçalho) não estão
    nomeados. As duas VSLs da base que foram ao ar (casos B e C) seguem o mesmo modelo de roteiro, mas não há registro
    de que sejam esses dois.
14. **Nível de consciência:** o framework da Escada de Consciência (não faz parte deste kit) não existe na casa; nos
    roteiros novos o nível foi lido do dado e declarado como leitura (Fonte A, avatar §9; Fonte B, direção §8).
15. **Botão falado ou não:** a decisão de não falar o botão nos roteiros de vídeo não está em
    `sirius-scale/frameworks/oferta-14-secoes.md`, que no §9, no §13 e no checklist do §15 manda nomear o botão e
    casar a fala com a página. A v5 do caso A carrega as duas instruções, e o gerador dos docs de página da casa
    ainda diz que trocar o botão obriga a regravar.
