# Nomenclatura e organização do Drive

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Força:** decisão do Rodrigo, que pediu um padrão único pra nomenclatura e organização do Drive. A estrutura de pastas já existia na casa; este arquivo acrescenta o que faltava: a ordem dentro de cada pasta e o nome dos documentos. Os nomes de tipo e o desenho da pasta de copy nasceram como proposta e mudam se ele quiser.
> **Alcance:** vale pra qualquer cliente e negócio. Primeira aplicação: a pasta de copy da Black de um expert da casa.
> **Por que existe:** nome é o que deixa a gente achar, ordenar e cruzar. Sem padrão, quem pede copy de um jeito recebe uma peça e quem pede de outro recebe outra, e a pasta vira lista solta.

## 1. Pastas

1. **Formato:** `N) NOME EM CAIXA ALTA`, em todos os níveis. A numeração segue a ordem em que o trabalho acontece (do que vem antes pro que vem depois), nunca ordem alfabética.
2. **O nível de cima já diz o lançamento.** Pasta não leva a tag (`[TAG]`) no nome, porque o caminho já tem. Quem abre a pasta de dentro de um link vê o caminho.
3. **Sem id de tarefa, sem data e sem versão no nome da pasta.** `criativos-estaticos-<id da tarefa>` vira `3) ESTÁTICOS`.
4. **Lançamento e perpétuo seguem uma estrutura fixa.** Não inventa pasta de primeiro nível fora dela:
   - **Lançamento:** 1) DOCUMENTOS DO LANÇAMENTO, 2) PÁGINAS, 3) CRIATIVOS (1 COPY, 2 DESIGNER, 3 VIDEOMAKER), 4) NOTIFICAÇÕES E AUTOMAÇÕES (1 EMAIL, 2 GRUPOS WHATSAPP, 3 API E MANYCHAT), 5) AQUECIMENTO, LIVES E CPLS, 6) RECUPERAÇÃO DE VENDAS, 7) TRÁFEGO, 8) REABERTURA E DOWNSELL, 9) LISTAS.
   - **Funil perpétuo:** 1) DOCUMENTOS DO PRODUTO, 2) PÁGINAS, 3) CRIATIVOS (1 COPY, 2 DESIGNER, 3 VIDEOMAKER), 4) NOTIFICAÇÕES E AUTOMAÇÕES, 5) TRÁFEGO, 6) LISTAS.
5. **Pasta nova nasce numerada e entra na ordem certa.** Se a ordem muda, renumera.
6. **Entregue ainda não aprovado mora em `0) EM APROVAÇÃO`** e só vai pra pasta do projeto depois do aprovado.

### 1.1 Dentro de `3) CRIATIVOS/1) COPY`

A pasta de copy se organiza **pela fase do lançamento**, na ordem do calendário, e dentro da fase pelo tipo de peça:

```
1) COPY
  1) ANTECIPAÇÃO
  2) CAPTAÇÃO
    1) ROTEIROS DE VÍDEO
    2) TEXTOS DE ANÚNCIO E POST
    3) ESTÁTICOS
  3) CARRINHO ABERTO
  4) SUPORTE, MENSAGENS E HOTMART
```

Fase que o lançamento não tem não ganha pasta vazia. Fase nova entra na posição do calendário (ex.: `5) REABERTURA E DOWNSELL`).
Arte e vídeo pronto moram em `2) DESIGNER` e `3) VIDEOMAKER`. Na pasta de copy fica o texto.

**Exceção: live.** O roteiro de live não mora em `1) COPY`, mora na pasta da live (§1.2). No caso de origem o roteiro
caiu na raiz de `1) COPY`, a pasta da live ficou vazia e ninguém achou.

### 1.2 Dentro de `5) AQUECIMENTO, LIVES E …` — VARIAÇÃO ISOLADA (11/2026)

```
2) LIVES DE AQUECIMENTO
  1) LIVE 01 - <TEMA>
  2) LIVE 02 - <TEMA>
  …
  _ANTERIORES
  CAPAS DAS N LIVES (…)          ← o que serve a todas fica na raiz
  DESCRIÇÃO - YOUTUBE DAS LIVES DE AQUECIMENTO - TAG
3) LIVE DE ABERTURA
4) LIVES DE CARRINHO
```

1. **Uma pasta por live**, numerada na ordem do calendário. Live avulsa entra na posição da data.
2. **Tudo da live fica junto:** o roteiro do expert, a versão dos slides (a do operador), os slides (pdf e pptx), a
   capa e os vídeos que passam nela (depoimento, metralhadora, cronômetro).
3. **Notificação da live mora em `4) NOTIFICAÇÕES E AUTOMAÇÕES`**, não na pasta da live.
4. **As notas da equipe vão pra pasta de estratégia**, como `NOTAS NN - LIVE DE AQUECIMENTO - TAG`.
## 2. Documentos

```
TIPO - ASSUNTO - TAG
```

1. **TIPO** em caixa alta, de uma lista curta e fixa (§2.1). É o que ordena e o que deixa filtrar.
2. **ASSUNTO** em caixa alta, curto, dizendo o que é e pra quem. Série numerada leva `TIPO NN - ASSUNTO`, com dois dígitos (`ROTEIRO 01 - ...`), na ordem de uso.
3. **TAG** é a do lançamento (`[TAG]`). Fica no nome mesmo com o caminho dizendo o lançamento, porque o documento sai da pasta: vai por link, anexo e e-mail.
4. **Sem extensão no nome de Google Docs** (`.md` no título era sobra do upload). Arquivo que não é Doc (zip, png, mp4) mantém a extensão.
5. **Sem versão no nome** (V1, V2, "final", "novo"). Correção entra no mesmo documento, no mesmo link (decisão do Rodrigo). Versão antiga que precisa ficar vai pra uma subpasta `_ANTERIORES`.
6. **Rascunho** leva o prefixo `[RASCUNHO] ` e o tira quando é aprovado. É o único estado que vai no nome, porque é o único que o time precisa ver de relance.
7. **Doc de notas da equipe** é separado e leva `NOTAS - <peça>`. Nunca vai na pasta que o expert abre misturado com o roteiro dele.
8. **Sem acento duplicado, sem dois-pontos, sem barra.** `:` e `/` quebram nome em alguns lugares.

### 2.1 Tipos

| TIPO | Quando |
|---|---|
| `ROTEIRO` / `ROTEIROS` | fala pra gravar ou apresentar (vídeo, live, aula). Plural quando o doc junta vários |
| `ANÚNCIO` | texto de anúncio (Meta, Google) |
| `POST` | texto de post orgânico |
| `LEGENDA` | legenda de reel, carrossel, short |
| `EMAIL` | e-mail ou sequência |
| `MENSAGEM` | WhatsApp, grupo, DM, fluxo de API |
| `ORIENTAÇÃO` | texto de orientação pro time ou pro suporte |
| `DESCRIÇÃO` | texto de página, produto ou checkout (Hotmart) |
| `BRIEFING` | pedido pro designer ou pro editor |
| `VÍDEO` | vídeo já gravado ou editado que ficou na pasta de copy (o lugar dele é `3) VIDEOMAKER`) |
| `NOTAS` | o que a equipe confere (nunca vai pro expert) |
| `ANÁLISE` | relatório, diagnóstico ou auditoria interna. Mora numa pasta de estratégia interna, por lançamento, nunca na pasta que o expert lê |
| `PLANO` | sequência ou calendário proposto pra decisão (o que mandar, quando, pra quem, por quê), antes de virar peça. Mora na mesma pasta de estratégia |
| `ESTRATÉGIA` | as peças estratégicas de uma VSL ou de um lançamento, escritas antes do roteiro e validadas por quem decide: ponto A, B e C, crenças, desejos, mecanismo, conclusão inevitável, tese, pontos lógicos e a oferta. Mora na pasta de estratégia interna |
| `REVISÃO` | lista de pontos ou prova marcada pro expert conferir um material dele e responder ali mesmo. Sem lançamento, a TAG é o nome do produto |
| `SLIDES` | slides de live, aula ou apresentação, em pdf e pptx (`SLIDES 01 - LIVE DE AQUECIMENTO - TAG.pdf`) |
| `CAPA` | capa de live, vídeo ou e-mail (`CAPA - LIVE DE ABERTURA, YOUTUBE 1280x720 - TAG.png`) |
| `PESQUISA` | perguntas ou respostas de pesquisa (`PESQUISA - RESPOSTAS - TAG`) |
| `CORTES` | proposta de cortes de um vídeo bruto (depoimento, live) pra aprovar antes da edição: início e fim no bruto, fala literal, produto e dor ou desejo de cada corte |

Tipo novo só entra se nenhum desses cobre. Entra aqui primeiro e depois no nome.

**Documentos de uma VSL saem numerados, na ordem do trabalho** (decisão do Rodrigo no caso de origem: "Todos os documentos que a gente for criando, vamos salvar no Drive, numerado, nomenclatura bem certinho, começando pelo primeiro documento, que é as peças estratégicas"). VARIAÇÃO ISOLADA.

1. `1) ESTRATÉGIA - FUNDAÇÃO ESTRATÉGICA DA <VSL> - TAG`: as peças, pra validar, uma frase por peça e a explicação
   curta, sem fonte nem tabela de dado no corpo: fonte no meio do texto deixa a leitura pesada e com cara de IA. As fontes
   ficam num arquivo de notas à parte.
2. `2) ROTEIRO - <VSL> POR PEÇA ESTRATÉGICA - TAG`: a copy inteira, dividida pelas peças, pra validar olhando a estrutura.
3. `3) ROTEIRO - <VSL> - TAG`: o roteiro do expert, só com fala e ação (sem rótulo, nota nem nome de aluno), tirado do 2
   depois da validação.

Os 1 e 2 moram na pasta de estratégia, que o expert não lê. O 3 mora na pasta do funil, que o expert lê, e na pasta da
estratégia entra um atalho com o número. Análise de apoio (mapa de cortes, depoimentos) fica na mesma pasta, sem
número. Até validar, o nome leva `[RASCUNHO] ` na frente.

**`COPY - …` saiu de uso (11/2026).** Cada documento leva o tipo do canal: `COPY - E-MAILS` vira `EMAIL`, `COPY - API`
e `COPY - GRUPOS` viram `MENSAGEM`, e `COPY - PÁGINA` vira `DESCRIÇÃO`.
## 3. O que isso mudou na primeira pasta

As 14 peças soltas foram pra fase certa e todos os documentos foram renomeados. **Nenhum link mudou**, porque renomear e mover no Drive mantém o id.
⚠️ Um efeito colateral: quem sobe um HTML com "o mesmo nome do Doc" pra sobrescrever (`sirius-scale/frameworks/copy/formatacao-de-roteiro.md` §4) não casa mais com o nome antigo. Atualize pelo id do arquivo, que é o caminho mais seguro de qualquer jeito.

## 4. O que ainda não tem padrão

1. **Nome dos arquivos locais** (no caso de origem, com id de tarefa no nome). O padrão do Drive pede outro tipo de nome.
2. **Pastas da `2) DESIGNER` e `3) VIDEOMAKER`**: seguem a mesma lógica por fase, mas o desenho interno ainda não foi escrito.
3. **Nome de arquivo de arte e vídeo**, que vem do gerador.
