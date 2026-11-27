# Checklist — Copy (conceito, criativo, e-mail, WhatsApp, roteiro)

## Leia antes de abrir o entregável

1. `sirius-scale/REGRAS.md` §1 (tom), §2 (nada inventado) e §3 (copy pelo agente `copy`
   e depois `/humanizer`)
2. `frameworks-da-casa/` — o que vocês já corrigiram em copy vale mais que o resto
   (`sirius-scale/REGRAS.md` §4)
3. `expert/dna-expert.md` — a voz
4. `expert/produtos/<produto>.md` — oferta, promessa, mecanismo
5. `lancamentos/<AAAA-MM-nome>/pesquisa.md` e `lancamentos/<AAAA-MM-nome>/avatar.md`
   (perpétuo: os mesmos arquivos em `funis/<nome>/`)
6. `sirius-scale/frameworks/copy/padrao-de-copy.md` — a ficha do pedido (§1), o caminho em
   ordem (§2) e o documento-padrão de quem lê ou grava (§3)
7. `sirius-scale/frameworks/copy/criativos.md` — DNA comum e o **mapa de CTA por funil e
   fase** (§0.9)
8. O framework específico da peça:
   - estático de venda de ingresso → `sirius-scale/frameworks/copy/criativos-venda-ingresso.md`
   - e-mail → `sirius-scale/frameworks/copy/email.md`
   - WhatsApp / DM → `sirius-scale/frameworks/copy/disparo-whatsapp.md`
   - qualquer outra peça → o que `sirius-scale/frameworks/copy/` tiver pra ela (a tabela
     do agente `copy`, em `.claude/agents/copy.md`, diz qual)
9. O modelo de lançamento, se houver (`sirius-scale/frameworks/lancamentos/lpsg.md`,
   `sirius-scale/frameworks/lancamentos/cpl-3-aulas.md` e os outros modelos de
   `sirius-scale/frameworks/lancamentos/`)
10. `lancamentos/<AAAA-MM-nome>/banco-angulos.md`, se existir

---

## A. Rastreabilidade (o mais importante)

- [ ] **Cada dor, desejo, objeção e número tem fonte.** Aponte, pra cada afirmação
      forte, a linha de `pesquisa.md`, `avatar.md` ou `expert/produtos/`. Afirmação que
      não rastreia é 🔴, não 🔵 — é a regra do `sirius-scale/REGRAS.md` §2.
- [ ] **A palavra é do público**, não do copywriter. Dor parafraseada pra soar
      melhor perdeu a linguagem real do avatar.
- [ ] **Verbatim real usado fora do contexto original é 🟡** (sem fonte é 🔴). Conferir
      na linha de origem sobre o quê a pessoa falava. *(Achado real no caso de origem:
      uma fala da pesquisa, "vira uma salada na minha cabeça", era sobre a matéria em
      geral e entrou na peça como se fosse sobre um tópico específico do curso.)*
- [ ] **Nenhum depoimento, número de pesquisa ou resultado inventado.** Nem
      "arredondado pra ficar redondo".
- [ ] Preço, garantia e bônus batem com `expert/produtos/<produto>.md`, caractere a
      caractere.
- [ ] **Se a peça afirma que um produto NÃO entrega algo** (base de upsell,
      "isso não está no seu kit", limitação declarada), essa afirmação foi
      conferida contra a lista de **bônus/entregáveis reais** daquele produto
      (manual do vendedor ou equivalente) — não só contra a descrição geral do
      produto em `expert/produtos/<produto>.md`. O produto pode já entregar, como
      bônus, exatamente o que a peça diz que falta. *(Achado real no caso de origem, com um
      segundo expert: o upsell do produto mais caro afirmava que o produto de entrada "não dá"
      um tópico, e o manual do vendedor já listava essa aula como presente/bônus do
      produto de entrada, em todas as versões.)*

## B. Voz e tom

- [ ] Soa como o expert do `expert/dna-expert.md`, não como IA genérica.
- [ ] **Zero linguagem de IA** (`sirius-scale/REGRAS.md` §1). Caça explícita por: "no
      mundo de hoje", "não é apenas X, é Y", "mergulhe", "desvende", "eleve", "descubra o
      segredo", adjetivo empilhado, frase de efeito vazia. Cada ocorrência é um
      achado com o trecho citado.
- [ ] **O `/humanizer` passou no texto inteiro depois do `copy`** (`sirius-scale/REGRAS.md`
      §3). Travessão em excesso, "-ndo" decorativo, regra dos três forçada, atribuição
      vaga ("especialistas apontam") e vocabulário de IA sobrando são sinal de que não
      passou.
- [ ] Português brasileiro informal e natural, do jeito que o expert fala.

## C. Funil e oferta

- [ ] **O CTA é a próxima ação possível naquele ponto do funil** — confira contra o
      mapa de CTA de `criativos.md` §0.9. CTA de compra em peça de captação é 🔴.
- [ ] A peça **não promete o que a etapa não entrega**. Copy que entrega adiantado
      o que ainda está sendo retido quebra o funil.
- [ ] **Front-end não carrega entregável nem bônus do backend.** O banco de ângulos
      separa isso de propósito.
- [ ] Nível de consciência coerente com o público real da peça — frio precisa de
      gancho antes; quente aguenta oferta direta. Os cinco níveis e o tipo de lead que
      cabe em cada um estão em `sirius-scale/frameworks/copy/great-leads.md` (a Escada de
      Consciência de Schwartz não faz parte deste kit).

## D. Regras por formato

**E-mail** (`sirius-scale/frameworks/copy/email.md`, régua de entregabilidade):
- [ ] Sem preço no assunto
- [ ] Um link só
- [ ] Assunto com a primeira letra maiúscula, sem palavra em caixa alta, sem "!" e sem
      "última chance"
- [ ] Tem pedido de resposta
- [ ] Esqueleto bate com a fase (captação / boas-vindas / carrinho aberto / fechando)

**WhatsApp / DM** (`sirius-scale/frameworks/copy/disparo-whatsapp.md`):
- [ ] Modo certo dos 3 (API oficial, grupo de massa, DM automatizada)
- [ ] Negrito com `*asterisco*`, nunca markdown
- [ ] Texto pronto pra colar, sem sintaxe que vaze na tela do lead

**Criativo:**
- [ ] Formato e dimensão declarados
- [ ] Direção visual é direção, não prompt técnico de imagem (isso é do `designer`)
- [ ] O ID `VDNN`/`IMG NN` foi **definido aqui** — a copy é quem numera, o tráfego
      nunca renumera na subida (`sirius-scale/frameworks/trafego/nomenclatura.md` §1)
- [ ] Número segue a série contínua do negócio, sem reciclar

## E. Força e alcance do framework usado (`sirius-scale/REGRAS.md` §4)

Força e alcance são eixos diferentes: a força (o rótulo de cada seção) conta
repetições; o alcance (o cabeçalho do arquivo) conta negócios. Cada um tem a sua
conferência.

- [ ] Elemento marcado **PADRÃO CONSISTENTE** foi seguido à risca.
- [ ] Elemento **PADRÃO CONSISTENTE (proposto)** foi tratado como **VARIAÇÃO
      ISOLADA** (se repetiu, mas o Rodrigo ainda não confirmou): usado só porque o
      contexto pediu, não como regra.
- [ ] Elemento **VARIAÇÃO ISOLADA** só foi usado porque o contexto pediu — não como
      default.
- [ ] Elemento **PADRÃO INCONCLUSIVO** foi entregue **declarado como hipótese**, não
      como padrão validado. Se não foi declarado, é achado. O "é hipótese" vale só
      pra essa força.
- [ ] **Alcance, sempre, qualquer que seja a força:** a entrega diz "baseado em
      framework de outro negócio, ainda sem teste aqui" (cabeçalho `NÃO TESTADO FORA`,
      `TESTADO EM N CLIENTES` ou `PROJETOS`). Seção CONSISTENTE não dispensa o aviso:
      ela se repetiu lá, não aqui. Base de `METODOLOGIA EXTERNA`: a entrega diz de qual
      tipo é a base. Se não foi dito, é achado.
- [ ] Onde `frameworks-da-casa/` e `sirius-scale/frameworks/` divergem, a peça seguiu a
      de `frameworks-da-casa/`.
- [ ] Não existe framework pra esse tipo de peça? Isso foi dito, e os ângulos vieram
      só do avatar e da pesquisa de vocês.

## F. Entrega

- [ ] Salvo em `entregas/<lançamento>/<peça>-v1.md`, como o agente `copy` manda;
      revisão vira `-v2`, `-v3`, sem sobrescrever o original.
- [ ] Doc que vai pro expert é **enxuto**: roteiro, CTA e instrução de gravação.
      Análise e operação ficam em arquivo separado.
- [ ] **O documento segue o padrão** (`padrao-de-copy.md` §3): título, uma linha de
      contexto, o aviso de que o que está entre parênteses é instrução, e o texto. Nota
      interna, fonte, "o que conferir" ou "como gravar" dentro dele é achado: isso mora
      no `NOTAS - <peça>`.
- [ ] Documento que sobe pro Drive tem o nome `TIPO - ASSUNTO - TAG`, sem versão no nome
      (`sirius-scale/frameworks/operacao/nomenclatura-drive.md` §2): um documento por
      peça, com a correção no mesmo link.
- [ ] A ficha do pedido foi fechada antes de escrever (`padrao-de-copy.md` §1): fase,
      público, objetivo com um CTA só e limite da plataforma. Dúvida de forma resolvida
      pelo agente veio listada na entrega; dúvida de dado (número, preço, data, promessa)
      parou e foi perguntada.
- [ ] Cada conceito traz ângulo, nível de consciência, headline, corpo, CTA,
      direção visual e formato.
- [ ] **Se a peça tem par de arquivos `-teleprompter.md` + `-direcao.md`** (ou
      qualquer par copy/execução), toda correção factual ou numérica aplicada
      no teleprompter foi conferida no arquivo irmão. Corrigir um e esquecer o
      outro deixa a versão errada viva em headline de página, card de vídeo ou
      declaração de ângulo — e só aparece numa revisão separada, não na
      correção original. *(Achado real no caso de origem, com um segundo expert: "metade do
      preço" foi corrigido no teleprompter do downsell e sobreviveu 4 vezes no
      arquivo de direção.)*
