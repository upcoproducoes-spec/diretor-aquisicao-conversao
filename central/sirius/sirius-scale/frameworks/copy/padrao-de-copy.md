# Padrão de copy: o mesmo caminho e o mesmo documento pra qualquer peça

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Força:** decisão do Rodrigo. A copy saía diferente conforme a forma como era pedida; ele pediu um padrão de formatação e de framework pra qualquer peça, inclusive pro expert se acostumar sempre com o mesmo formato.
> **Alcance:** qualquer cliente. É uma camada por cima dos frameworks que já existem: ela não substitui nenhum, ela diz em que ordem eles entram e em que embalagem a peça sai.
> **O que é novo aqui:** a ficha do pedido (§1) e o documento-padrão do expert (§3). O resto é o que já estava em `sirius-scale/REGRAS.md` §3 e nos arquivos de `sirius-scale/frameworks/copy/`, reunido num lugar só.

## 0. Por que a copy saía diferente

A peça mudava conforme o jeito de pedir: pedido curto saía com um formato, pedido detalhado saía com outro, e o agente decidia sozinho o que perguntar. Dois motivos: o pedido não tinha campos fixos, e a embalagem (cabeçalho, notas, marcas) não era a mesma entre as peças. As duas coisas ficam travadas abaixo.

## 1. A ficha do pedido

Toda peça nasce com estes campos. O que faltar o `copy` **pergunta e para** (`sirius-scale/REGRAS.md` §2). Dúvida de forma não conta: ele decide, entrega e avisa o que decidiu.

| Campo | Exemplo |
|---|---|
| Cliente e produto | [nome do expert] · [produto] |
| Lançamento ou funil | [tag do lançamento] |
| Fase | captação, carrinho aberto, antecipação |
| Tipo de peça | roteiro de vídeo, anúncio, e-mail, WhatsApp, legenda… |
| Público | aluno, não aluno, lead frio |
| Objetivo e CTA único | inscrever na live; um CTA só |
| Quantas variações | 3 |
| Limite | caracteres da plataforma, duração do vídeo |

Quem pede pode mandar a ficha incompleta. O `copy` completa o que dá com o briefing do lançamento e pergunta o resto.

## 2. O caminho, sempre na mesma ordem

1. **Ler os arquivos do cliente:** `expert/dna-expert.md`, `expert/produtos/<produto>.md` e, na pasta do lançamento ou do funil, `pesquisa.md`, `avatar.md` e `banco-angulos.md`. Faltou dado: para (`sirius-scale/REGRAS.md` §2).
2. **Escolher o ângulo** no banco de ângulos. Cada afirmação forte rastreia até um dado real. Não rastreia, não entra.
3. **Pegar o framework do tipo de peça** (tabela abaixo; `frameworks-da-casa/` vem antes) e seguir a fórmula dele. A estrutura de venda vem do LHTO e das 14 seções; o framework do tipo diz a ordem das partes.
4. **Escrever no documento-padrão** do §3.
5. **Rodar `/humanizer`** no texto inteiro, depois do `copy`.
6. **Conferir a fonte de cada afirmação** e escrever as notas da equipe, **em documento separado**.
7. **Entregar** com o nome de `sirius-scale/frameworks/operacao/nomenclatura-drive.md` §2.

| Tipo de peça | Framework que manda na estrutura |
|---|---|
| Live, aula, CPL, pitch | `sirius-scale/frameworks/copy/formatacao-de-roteiro.md` + LHTO (`sirius-scale/frameworks/lhto.md`) |
| VSL | `sirius-scale/frameworks/copy/producao-de-vsl.md` + `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` |
| Roteiro de criativo em vídeo | `sirius-scale/frameworks/copy/criativos.md`, e `sirius-scale/frameworks/copy/captacao-da-black-roteiro-de-video.md` na Black |
| Texto de anúncio | `sirius-scale/frameworks/copy/captacao-da-black-texto-de-anuncio.md`, e `sirius-scale/frameworks/copy/criativos.md` |
| Texto da arte (estático) | `sirius-scale/frameworks/copy/captacao-da-black-texto-do-estatico.md`, `sirius-scale/frameworks/copy/criativos-venda-ingresso.md` |
| E-mail | `sirius-scale/frameworks/copy/email.md` |
| WhatsApp | `sirius-scale/frameworks/copy/disparo-whatsapp.md` |
| Página | `sirius-scale/frameworks/paginas/estrutura-de-pagina.md` + `sirius-scale/frameworks/oferta-14-secoes.md` |

⚠️ Os arquivos `captacao-da-black-*` são `NÃO TESTADO FORA` da Black do caso-base. Em outro negócio, siga a estrutura e sinalize na entrega (`sirius-scale/REGRAS.md` §4).

## 3. O documento-padrão (o que o expert abre)

O expert recebe **sempre o mesmo documento**, e ele tem só o que ele lê ou grava:

```
<TÍTULO DA PEÇA>

<uma linha de contexto: pra quem é, quanto dura, quando vai ao ar>

(o que está entre parênteses é instrução, não é fala)

<o texto>
```

1. **Título** é o nome do documento no Drive, sem `TIPO -` nem tag. O nome do arquivo segue `sirius-scale/frameworks/operacao/nomenclatura-drive.md` §2.
2. **Contexto em uma linha.** Sem tabela, sem tempo estimado, sem lista de requisitos.
3. **Corpo em parágrafos curtos**, uma ideia por parágrafo, pensando em quem lê no teleprompter. Aspas retas, sem backtick, sem excesso de travessão.
4. **Vários itens no mesmo doc** (roteiros, variações de anúncio) ganham título numerado, `ROTEIRO 01`, `VARIAÇÃO 01`, na ordem de uso, e o mesmo desenho do começo ao fim.
5. **Nada de nota interna, fonte, "o que conferir" ou "como gravar" no documento do expert.** Isso vai no `NOTAS - <peça>`, que é da gerente de operação e de quem aprova.
6. **Um documento por peça**, sem versão no nome. Correção entra no mesmo link.

**O visual do Doc sai de um lugar só** (decisão do Rodrigo). No caso de origem isto é um gerador em código, que não vai neste kit. O padrão é: título, seção (`EMAIL NN - X`, `MENSAGEM NN - X`, `ROTEIRO NN - X`), instrução entre parênteses em cinza, rótulo (`Assunto:`, `Pré-cabeçalho:`, `Título:`) em negrito, botão (`[TEXTO] → link`) em destaque e pendência `[[...]]` grifada em amarelo. Ninguém sobe `.md` cru.

O que muda por tipo é o miolo (§2), não a embalagem. Live e aula acrescentam as marcas de tela e geram a versão de operação, por `sirius-scale/frameworks/copy/formatacao-de-roteiro.md`. Criativo em vídeo é um arquivo só, sem marca de tela (decisão do Rodrigo).

### 3.1 A forma de cada tipo dentro dessa embalagem

| Tipo | O que tem no corpo |
|---|---|
| Roteiro de vídeo (criativo) | uma seção por público, um roteiro por título, um gancho só, fala corrida, "(final A ou B)" no fim; finais gravados uma vez no fim do doc |
| Live, aula | blocos numerados `N. TÍTULO`, fala + instrução entre parênteses (`sirius-scale/frameworks/copy/formatacao-de-roteiro.md` §1) |
| Texto de anúncio | uma variação por bloco, na ordem da plataforma (título, texto, CTA), com os limites de caractere respeitados |
| E-mail | assunto + preview, abertura, corpo, CTA único, fecho, na ordem de `sirius-scale/frameworks/copy/email.md` §2 |
| WhatsApp | uma mensagem por bloco, gancho na primeira linha, CTA único (`sirius-scale/frameworks/copy/disparo-whatsapp.md` §2) |
| Legenda e post | o texto final, pronto pra colar |
| Texto da arte | o texto exato que vai escrito na arte, linha por linha, e nada além |

## 4. O que fica com cada pessoa

1. **Quem pede** preenche a ficha (§1) como conseguir. Não precisa lembrar de formato.
2. **O `copy`** completa, pergunta o que falta e escreve no padrão.
3. **O `/humanizer`** passa depois.
4. **A equipe** abre o `NOTAS - <peça>`, confere e aprova. O expert abre só o documento dele.

## 5. O que ainda não está resolvido

1. **Tipos sem framework:** o `copy` segue com a ficha, a pesquisa e o avatar, e diz na entrega que não havia framework pra peça.
2. **A ficha do pedido** ainda não é um formulário. Hoje é uma lista no próprio pedido; vale virar campos fixos se a equipe sentir falta.
3. **A conferência de formato** (título no padrão, sem nota dentro do doc, um doc por peça) ainda é manual. Dá pra entrar no `/revisar` como checklist.
