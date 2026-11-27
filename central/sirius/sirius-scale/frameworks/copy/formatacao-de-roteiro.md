# Formatação de copy: versão de leitura, versão de operação e notas

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Força:** PADRÃO CONSISTENTE por decisão do Rodrigo: "se for criar qualquer copy, seja de criativo ou roteiro de live ou de aulas, a gente pode seguir esse estilo de formatação". Isso vale como regra da casa.
> **Alcance:** a forma vale pra qualquer cliente. O gerador de slides da casa era da Black do caso-base, com o logo e as cores fixos no código, e não vai neste kit (§4).
> **Origem:** a live 1 de aquecimento da Black do caso-base (um expert de educação). Duas rodadas de ajuste com o Rodrigo no mesmo dia.
> **Substitui** o §0.1.1 de `sirius-scale/frameworks/copy/criativos.md` nos pontos listados no §6. O resto do §0.1.1 continua valendo.

## 0. Resumo

Toda copy longa sai de **um `.md` fonte**, escrito pelo agente `copy` com marcas de tela. Desse arquivo saem até três documentos:

1. **A versão de leitura**, de quem fala (o expert, no teleprompter). Tem só a fala e as instruções entre parênteses, sem marca de slide.
2. **A versão de operação**, de quem passa o slide ou edita (no caso-base, o editor). É a mesma fala, com o número de cada slide e cada troca de tela marcados antes da fala que acompanham.
3. **As notas da equipe** (a gerente de operação e quem aprova): o que mudou, o que conferir, pendências, fontes e força da evidência. Elas nunca vão no doc do expert.

Ninguém mantém duas cópias à mão. Mudou a fala, muda o `.md` e os docs são gerados de novo a partir dele.

## 1. O `.md` fonte: o que o `copy` escreve

**Cabeçalho, no máximo 4 ou 5 linhas, sem tabela, sem tempo estimado e sem instrução:**

```
# <Nome da peça, que é o título da live/aula/vídeo>

**<Evento> · <peça, ex.: live 1> · <dia, data, hora>**
<Onde passa, ex.: YouTube (principal), Instagram e Facebook ao mesmo tempo>
**<Regra crítica, se houver, ex.: Preço:>** <uma frase>
```

**Corpo:**
- Os blocos são separados por `________________` e titulados como `**N. TÍTULO EM CAIXA ALTA**`, numerados na ordem da fala.
- A primeira linha do bloco 1 explica a convenção: "(O que está entre parênteses é instrução, não é fala. As linhas [SLIDE] e [TELA] mostram o que entra na tela a partir dali.)"
- A **fala** vem em parágrafos curtos, uma ideia por parágrafo e frase curta, porque quem lê está no teleprompter e quem escuta pode ser um público mais velho.
- A **instrução** é uma linha inteira entre parênteses, no bloco onde vale. Fala que o expert pode usar numa resposta vai entre aspas dentro da instrução.
- As **respostas prontas** pro caso de o chat ficar quieto vêm como pergunta entre aspas e a resposta logo depois.
- **Marcas de tela**, numa linha só, logo antes da fala que acompanham:
  - `[SLIDE] Título | linha de apoio`: uma placa;
  - `[SLIDE + Nome da lista] Item | apoio`: um item de lista. Cada item ganha um slide, que repete os anteriores e acende o novo;
  - `[TELA] descrição`: sai do slide pra tela compartilhada, vídeo ou print (não vira slide).
- Sem backtick (no Google Docs vira Roboto Mono, que o Rodrigo reprovou), aspas retas e sem excesso de travessão. Passa pelo `/humanizer` (`sirius-scale/REGRAS.md` §1 e §3).

**Notas da equipe** num `.md` separado (`<peça>-notas-vN.md`), com as seções: o que mudou da versão anterior; conferir antes de gravar ou ir ao ar; pendências abertas; fontes por bloco; força da evidência; passada do humanizer.

## 2. As três versões geradas

| Versão | Pra quem | O que tem | Como sai do `.md` fonte |
|---|---|---|---|
| Leitura | expert (teleprompter) | fala + instruções; `[TELA]` vira "(Na tela: …)"; sem linha de slide | do roteiro numerado, tirando toda linha `[SLIDE]` e trocando `[TELA]` por "(Na tela: …)" |
| Operação | quem passa o slide ou edita | a mesma fala + "▶ SLIDE NN · texto" em faixa dourada e "▶ TELA · …" em faixa azul; aviso no topo dizendo pra quem é e quantos slides tem | do roteiro numerado, com as marcas viradas em faixa e o aviso "Versão de [quem passa o slide], pra passar os slides: …" no topo |
| Notas | a gerente de operação e quem aprova | o `.md` de notas, formatado | do `.md` de notas, sem mexer no conteúdo |

No Docs, a fala sai em corpo grande (13 pt) e a instrução em cinza itálico. O título do Doc é o nome do arquivo, sem extensão.

## 3. Slides (quando o deck nasce da copy)

- **Quadrados (1080 x 1080)**, pra ocupar a tela ao lado da câmera do expert.
- **Uma ideia por slide:** título de até ~12 palavras e uma linha de apoio.
- **Lista acende um item por slide**, porque o app da transmissão não roda animação.
- **Capa sem data** quando a live é no dia. A data que importa (ex.: a abertura) aparece em destaque no slide dela.
- **Logo do produto** quando a fala é do produto (ex.: o programa principal), e logo do evento nos slides do evento.
- **Palavras-chave em dourado** (preço, "pra sempre", "1 ano", data, "condição especial"…). A copy pode forçar o destaque com `**negrito**` na marca. O dourado era a cor de destaque do caso-base; num cliente novo, a cor de destaque sai do `expert/brand.md` dele.
- **Subtexto grande**: 48 px no slide de 1080, pensando em quem assiste pelo celular.
- **Um QR code só, no slide do convite**, com o link de UTM da plataforma principal. Slide repetido de convite com QR foi cortado na revisão do Rodrigo.
- **Título de outra live ou evento é o título oficial**, o das capas. Na v2, um slide com o nome curto do produto no lugar do título oficial foi corrigido.
- O deck sai do roteiro, e o número de cada slide é escrito no `-numerado.md`. **Mudou a ordem ou a quantidade de slides, gere de novo a versão de operação.**

## 4. Geração e entrega (no caso-base, por ferramentas próprias da casa, que não vão neste kit)

Na casa, os slides e as três versões saíam de geradores próprios, presos à Black do caso-base (logo, paleta e pasta fixos no código). Eles não fazem parte deste kit. O que vale levar é o jeito de entregar e as travas:

- **Entrega:** o link principal da entrega é a versão de leitura. As outras versões e os slides vão junto, como anexo ou comentário. O nome do arquivo já vira o título do Doc, então nomeie o arquivo como o título que o expert vai ver.
- **Atualizar no mesmo link:** suba o arquivo novo com o mesmo nome do Doc, por cima do anterior. **Antes, leia o Doc.** Se alguém editou direto nele, leve a edição pro `.md` fonte primeiro (o Rodrigo ajustou a saudação do expert direto no Doc, e isso foi levado pra fonte das 4 lives).
- **Outro cliente:** o template de slides tem que tirar logo, paleta e fonte da marca do cliente (`expert/brand.md`), nunca de um valor fixo herdado do caso-base.
- **Live que vende (live de abertura da Black do caso-base):** o QR vai na placa do link, não na do convite, e a legenda dele não cita a bio quando bio e post só abrem depois da live. No caso-base, ela dizia que o link está no chat e na descrição, e mandava quem estava no Instagram usar o link do YouTube. Na quebra de linha, "R$" não se separa do número. *VARIAÇÃO ISOLADA.*
- **Mural de prints (a mesma live, versão 3):** a marca é `[SLIDE] <título> | mural <chave>`, e um arquivo à parte diz quais prints entram em cada chave e em que desenho: lista (comentários empilhados em zigue-zague) ou grade (cards lado a lado). Cada print é recortado inteiro, como chegou, sem o fundo do lançamento de onde veio; o fundo passa a ser o da Black, no pedido do Rodrigo de "tirar mesmo a identidade visual dos lançamentos e colocar a identidade visual da Black". O expert lê um print por mural, sem o nome, e os outros ficam na tela. Até 4 comentários largos ou 4 cards por mural ficam legíveis no celular; 7 cards num mural só ficaram pequenos demais (teste no mesmo dia). *VARIAÇÃO ISOLADA.*

## 5. Por tipo de peça

| Peça | Leitura | Operação | Notas |
|---|---|---|---|
| Live (aquecimento, abertura, carrinho, downsell), aula, CPL, pitch | teleprompter do expert | slides, pra quem passa | sim |
| VSL e vídeo de venda | teleprompter | o mapa de edição (`sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md`) é a versão de operação | sim |
| Criativo em vídeo | **um arquivo só**, no formato do doc de roteiros de captação da Black do caso-base (abaixo) | não tem: quem edita decide o texto de tela com a copy na mão | não tem |
| Estático, e-mail, WhatsApp, página | o texto final, sem marcas | não tem | sim, em doc separado |

**Criativo em vídeo é um arquivo só (decisão do Rodrigo).** Antes, a linha acima mandava três peças: a versão de leitura, a de `[TELA]` pro editor e as notas. Na Black de um segundo expert isso virou três Docs na pasta, e ele reprovou: "tem que ter um arquivo só dos criativos, da copy, e só", porque o expert vai pegar o texto e jogar no teleprompter. O texto de tela fica com a edição: "na hora de editar, o próprio agente, ele vê o que, que ele faz aí." O modelo é o doc de roteiros de captação da Black do caso-base (evidência no caso de origem; o conteúdo desses roteiros está em `sirius-scale/frameworks/copy/captacao-da-black-roteiro-de-video.md`), subido como markdown:
- cabeçalho de duas ou três linhas (nome, quantos vídeos e pra quem, data da live);
- uma seção por público e um roteiro por título, com uma linha de público e duração;
- **um gancho por vídeo**, a fala corrida em parágrafos curtos e "(final A ou B)" no fim;
- os finais no fim do documento, gravados uma vez;
- sem bloco de "como gravar", sem gancho alternativo, sem `[TELA]`, sem instrução entre parênteses (só o final e, se precisar, uma pausa) e sem nota interna. O que conferir vai na mensagem de entrega, não no doc.

## 6. O que mudou em relação ao §0.1.1 de `sirius-scale/frameworks/copy/criativos.md`

1. **As notas pra quem aprova** saíram do fim do doc do expert e ganharam um doc próprio. Pedido do Rodrigo: o doc que vai pro expert não pode ter "fontes usadas e o que conferir".
2. O título de bloco `[SLIDE N — título]` virou **bloco numerado + marca de slide em cada fala**. O número do slide vem do deck gerado.
3. O **"Como ler"** saiu do cabeçalho e virou a primeira instrução do bloco 1.
4. **O deck nasce da copy.** Antes, a regra era "deixa de slide só com o deck visto". Ela continua valendo quando o deck é de outra pessoa.

## 7. Referência

Primeiro uso: a live 1 de aquecimento da Black do caso-base, que tem a versão do expert, a do editor e as notas (evidência no caso de origem). As lives 2 a 4 seguem o mesmo formato. O que a copy dessas lives diz, bloco a bloco, está em `sirius-scale/frameworks/copy/live-de-aquecimento-da-black.md`.
