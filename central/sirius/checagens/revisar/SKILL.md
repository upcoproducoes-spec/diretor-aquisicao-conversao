---
name: revisar
description: Revisa tecnicamente um entregável já pronto — campanha de tráfego, copy, criativo (arte ou vídeo) ou página — conferindo contra os frameworks (os de `frameworks-da-casa/` primeiro) e os dados reais de vocês, com olhos frescos. Use quando pedirem pra "revisar", "conferir", "validar" ou "auditar" o que foi feito, ou depois de fechar uma peça grande — pra rodada inteira de tráfego ("revisa tudo que mexi hoje") o inventário vem da plataforma e dos arquivos, nunca da conversa; pra conferir se ficou faltando algo do que foi combinado no próprio chat ("revisa se fiz tudo que combinamos aqui"), usa a conversa só pra saber o que era esperado, e ainda confere a execução na plataforma. Não produz entregável novo: aponta o que está fora do padrão, sempre citando a regra.
---

> Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
> são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
> ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.


# Revisão técnica de entregável

Segunda passada em cima de trabalho **já pronto**, pra pegar o que passou batido:
número sem fonte, nome fora do padrão, verba que não bate com o briefing, escrita em
plataforma sem confirmação, copy que promete o que a etapa não entrega.

## O que essa revisão é — e o que ela não é

| | |
|---|---|
| **É** | Conformidade técnica: o que foi entregue bate com o framework, o briefing e o dado real de vocês? |
| **Não é** | Análise de estratégia ou de resultado. O resultado do funil é o `/debriefing`; a escolha que vira regra é o registro em `frameworks-da-casa/` (`sirius-scale/REGRAS.md` §5) — outra passada, outro objetivo. |
| **Não é** | Correção. O revisor aponta; corrigir é decisão de quem pediu, num passo separado. |
| **Não é** | Extração de aprendizado. Isso é `/pente-fino` — ver a comparação no fim deste arquivo. |

A ordem completa ao fechar peça grande (`sirius-scale/REGRAS.md` §5) é
**`/revisar` → corrigir → registro em `frameworks-da-casa/` → `/pente-fino`**. A revisão
vem primeiro por um motivo: não adianta registrar padrão novo em cima de execução que
saiu errada.

**Que regra vale.** Achado só se apoia no que está escrito:
1. `frameworks-da-casa/`, o que vocês corrigiram ou criaram. Onde diverge de
   `sirius-scale/frameworks/`, **vale `frameworks-da-casa/`** (`sirius-scale/REGRAS.md` §4): o
   achado cita a regra de lá, e entregável que seguiu `sirius-scale/` contra ela é achado.
2. `sirius-scale/REGRAS.md` e `sirius-scale/frameworks/`.
3. O `CLAUDE.md` de vocês e os arquivos de `expert/`, `lancamentos/` e `funis/`.

## Passo 0 — Preflight (saúde da conta)

Sempre que o escopo tem tráfego pago, rode a skill `/preflight` antes de qualquer coisa
(`.claude/skills/preflight/SKILL.md`). São 12 itens lidos da plataforma, sempre os mesmos. Você não tem a
ferramenta de skill: leia o arquivo e siga.

O que ele acusar abre a entrega, numa seção **Saúde da conta**, antes dos achados do checklist, e entra como
achado de verdade. Item que não deu pra conferir vai em "não consegui verificar".

O agente `gestor-trafego` usa outra lista antes de ativar campanha nova, o preflight do pacote (país,
Advantage, idade). A `/preflight` olha a conta toda.

📌 **O preflight não substitui a revisão, e a revisão não substitui o preflight.** Ele pega o que dá pra
conferir igual toda vez; o checklist pega o que exige julgamento (nome, verba contra briefing, público
contra pesquisa).

## Passo 1 — Definir o escopo

Precisa de duas coisas: **o que revisar** e **de qual domínio é**.

> **Pra saber O QUE FOI FEITO, a revisão nunca se baseia em histórico de
> conversa.** O trabalho se espalha por vários chats e várias pessoas no mesmo dia, e
> nenhum chat tem a foto completa. A fonte da verdade sobre execução é o que está
> **de fato** na plataforma e nos arquivos — nunca "eu fiz X" dito no chat.
>
> Isso é diferente de usar a conversa pra saber **O QUE ERA PRA SER FEITO** — o
> combinado, o plano da sessão. Essa informação só existe no chat, ninguém a recupera
> lendo a plataforma depois, e é exatamente o que o modo (d) abaixo usa. A regra dura
> é: conversa pode dizer o que **deveria** ter acontecido, nunca o que **de fato**
> aconteceu — quem prova isso é sempre a plataforma e os arquivos.

Quatro formas de dar o escopo:

**a) Objeto nomeado** — `/revisar a campanha de captação do lançamento X`, `/revisar a
página de captura em entregas/`. Direto ao ponto quando se sabe o alvo.

**b) O dia** — `/revisar o que mexi hoje`. É o modo mais comum depois de uma rodada de
subida ou otimização. Ver abaixo.

**c) A rodada** — `/revisar a subida dos criativos novos do lançamento`. Um recorte
temático; monte o inventário igual ao modo dia, filtrando pelo tema.

**d) O combinado desta conversa** — `/revisar o que combinamos aqui`, ou `/revisar`
puro no fim de um chat de execução (otimização, subida de campanha, pacote de
criativo). É o modo certo pra pegar "esqueci de fazer uma coisa que a gente
combinou" — as outras três não pegam isso, porque só enxergam o que **existe**,
nunca o que **faltou existir**. Ver "Modo combinado" logo abaixo.

### Modo dia (ou rodada): monte o inventário ANTES de revisar

Não pergunte o que foi feito — descubra, e mostre pra pessoa conferir.

1. **Meta**: campanhas, conjuntos e anúncios da conta com `updated_time` dentro da
   janela, pelo conector. Peça `updated_time`, `created_time`, `status`,
   `effective_status`, `daily_budget` e `name` na mesma chamada, em lote, nunca uma
   chamada por objeto: a conta tem limite de chamadas agressivo
   (`sirius-scale/frameworks/trafego/_metodologia.md` §5). Sem conector: o histórico
   de atividades da conta no Gerenciador, em print ou export.
2. **Google Ads**: o recurso `change_event` na janela, pelo conector — traz o que
   mudou, quem mudou e o campo tocado (a consulta exige `LIMIT` explícito,
   `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §3.1). Sem conector: o
   histórico de alterações da conta, em print ou export.
3. **Arquivos**: o que foi modificado hoje em `entregas/`, `lancamentos/`, `funis/`,
   `expert/` e `frameworks-da-casa/` (`find entregas lancamentos funis expert frameworks-da-casa -mtime -1 -type f`).
   A pasta de vocês, a menos que alguém tenha ligado controle de versão, não guarda
   histórico: use a data de modificação.

Junte tudo numa lista e **mostre pra pessoa antes de disparar os subagentes**:

```
Achei isto tocado hoje (<data>) na conta:

META (7 objetos)
  · 3 campanhas com orçamento alterado — [LC] [PRODUTO] [TAG] [CAPTACAO] ...
  · 2 anúncios novos criados (PAUSED) — AD - VD NN - SLUG, AD - VD NN - SLUG
  · 2 conjuntos com público alterado
GOOGLE (2 mudanças)
  · orçamento de 1 campanha, meta de conversão de 1 campanha
ARQUIVOS (3)
  · entregas/<lançamento>/conceito-vdnn.md
  · entregas/analises/<lançamento>-trafego-<data>.md
  · lancamentos/<AAAA-MM-nome>/briefing.md

Falta alguma coisa que você mexeu e não apareceu aqui?
```

Essa confirmação existe por um motivo: se o inventário estiver furado, a revisão
sai limpa e o erro passa. O "falta alguma coisa?" é a rede — quem mexeu enxerga o
buraco em dois segundos, e é a única coisa que a memória de quem fez faz melhor que a
plataforma.

Mudança feita **na mão pelo Gerenciador** também aparece aqui, porque a plataforma
mostra o objeto alterado independente de quem alterou. Isso é uma vantagem do modo
dia sobre qualquer leitura de conversa.

⚠️ **O inventário enxerga estado, não trajetória.** Se o orçamento subiu e voltou no
mesmo dia, a leitura da Meta mostra só o valor final e o vaivém some — a API dela não
guarda histórico de alteração de campo. No Google o `change_event` pega. Quando a rodada
teve idas e vindas, diga isso na entrega, em vez de deixar a foto final passar por "foi
só isso que mudou".

### Modo combinado: cruze o prometido com o feito

Esse modo roda **em cima** do modo dia/rodada, não no lugar dele — o inventário
continua vindo de plataforma e arquivos, do jeito de sempre.

1. **Eu extraio o combinado, sem subagente.** Mesma lógica do `/pente-fino` passo
   1: um subagente não viu esta conversa, então quem lista "o que ficou decidido
   fazer" sou eu, percorrendo o chat. Cada item vira uma linha objetiva —
   "realocar verba da campanha X pra Y", "criar 2 anúncios novos com o ângulo Z",
   "desligar segmentação otimizada no conjunto W" — não a conversa inteira colada.
2. **Cruzo essa lista com o inventário do Passo 1** (mecânico, não precisa de
   subagente pra isso: é comparar duas listas). Cada item combinado cai numa de
   três colunas:
   - **Apareceu no inventário** → segue pro checklist normal de conformidade.
   - **Não apareceu** → vira achado de **completude**, categoria própria (ver
     Passo 5), separado de achado de conformidade — é um tipo de erro diferente
     (esquecido, não errado).
   - **Apareceu mas fora do que foi combinado** (ex.: combinamos +20% e o
     conjunto está com +45%) → também é achado, e cita os dois números.
3. **A lista do combinado nunca prova execução.** Ela só entra como o "esperado"
   do cruzamento — quem prova que algo foi feito continua sendo a plataforma e os
   arquivos, igual no modo dia. Por isso essa extração não fura a regra do bloco acima.
4. Se a sessão não teve plano claro (foi só leitura/análise, sem decisão de ação),
   diga isso e caia direto no modo dia — não force uma lista de combinado vazia.

### Se o escopo continuar vago

Pergunte. Revisão de escopo vago vira "parece ok", que é pior que revisão nenhuma.

## Passo 2 — Escolher o checklist

| Domínio | Quando | Checklist |
|---|---|---|
| `trafego` | campanha, conjunto, anúncio, análise de performance, realocação de verba | `checklists/trafego.md` |
| `copy` | conceito de criativo, e-mail, WhatsApp, roteiro, doc de copy | `checklists/copy.md` |
| `pagina` | HTML de captura, CPL, vendas, obrigado | `checklists/pagina.md` |
| `criativo` | prompt de imagem, arte, vídeo editado | `checklists/criativo.md` |

Entrega que cruza domínios (ex.: pacote de campanha = estrutura + copy + briefing de
arte) roda **um checklist por domínio**, em paralelo. Não force tudo num só.

Domínio que não tem checklist (automação de escrita, peça financeira e o que mais
aparecer): revise mesmo assim contra `sirius-scale/REGRAS.md`, `frameworks-da-casa/` e o
agente correspondente em `.claude/agents/`, e **avise na entrega** que não existe
checklist próprio pra esse tipo de peça.

📌 **Não dispara domínio sem delta.** O inventário do Passo 1 diz o que de fato foi
tocado — dispara subagente só pros domínios que aparecem nele. Se o dia só teve
tráfego, é 1 subagente, não 3 "pra garantir". Rodar domínio sem pista no inventário
é o oposto do que o Passo 1 existe pra resolver, e é o maior gasto de token da
skill: cada subagente a mais é uma releitura completa de framework do zero.

📌 **Recorte por letra do checklist, não o checklist inteiro.** Cada checklist é
dividido em seções temáticas (A, B, C... em `trafego.md`, por exemplo). Antes de
montar o prompt, olhe o inventário e ative só as letras cujo tema aparece nele —
`checklists/trafego.md` já tem "Aplica quando" em cada letra pra isso ser mecânico,
não julgamento. Letra desativada entra na saída como **fora do escopo desta
rodada**, não como "não verificado" (são coisas diferentes: uma não tinha o que
checar, a outra devia ter sido checada e não deu).

## Passo 3 — Rodar com olhos frescos (obrigatório)

A revisão roda num **subagente `general-purpose`**, um por domínio, disparados em
paralelo. Isso não é firula: quem montou a campanha carrega as próprias suposições
e valida a si mesmo. O subagente começa do zero, lê o arquivo e o framework, e não
sabe o que "era pra ser".

Por isso o prompt tem que ser **autossuficiente** — o subagente não enxerga esta
conversa. E por isso não se usa o agente de domínio (`gestor-trafego`, `copy`,
`designer`, `webdesigner`): eles são os autores, com a mesma cabeça de quem escreveu, e
alguns têm poder de escrita que revisor não precisa.

**Antes de montar o prompt, eu faço o recorte** (é o que mantém a skill barata):
abro o checklist do domínio, ativo só as letras que o inventário do Passo 1 e 2
pediram, e pra cada letra ativada abro o framework citado e copio **só a seção
referenciada** — não o arquivo inteiro. O mesmo vale pro `sirius-scale/REGRAS.md` e pro
que existir em `frameworks-da-casa/` sobre o tema: entrego só o que o domínio pede (pra
tráfego, tipicamente a §6 das regras e o que `frameworks-da-casa/` tiver de tráfego). O subagente
recebe os trechos já prontos no prompt; ele só abre um arquivo por conta própria se
precisar conferir algo que o trecho não cobriu.

Prompt, por domínio:

```
Você é revisor técnico. Não produza entregável novo, não corrija nada:
sua única saída é a lista de achados.

ESCOPO DA REVISÃO
<o que exatamente revisar: caminhos de arquivo, nomes ou IDs de campanha, produto,
lançamento ou funil — completo, você não tem acesso à conversa que gerou isso>

LETRAS DO CHECKLIST ATIVADAS NESTA RODADA
<quais letras de checklists/<domínio>.md se aplicam ao que foi tocado, e por quê.
As demais ficam FORA DO ESCOPO — não avalie contra elas>

REGRAS JÁ RECORTADAS (leia isto antes de olhar o entregável)
<cole aqui só os trechos de frameworks-da-casa/, de sirius-scale/REGRAS.md e dos
frameworks de sirius-scale/frameworks/ que as letras ativadas citam — não o arquivo
inteiro. Onde frameworks-da-casa/ diverge de sirius-scale/, vale frameworks-da-casa/.
Se precisar confirmar algo que não está no trecho, o caminho completo do arquivo está
disponível pra você abrir>
Ler o entregável primeiro, antes da regra, contamina a leitura.

SE HOUVER LISTA DE "COMBINADO" NESTA RODADA (modo d)
<itens que deviam ter sido feitos, extraídos da conversa por mim, não por você —
cruze contra o que você está revisando: aparece? bate com o que foi prometido?
Isso é achado de COMPLETUDE, categoria separada de achado de conformidade>

COMO ACHAR DE VERDADE
- Todo achado cita a REGRA (arquivo:linha ou seção do framework) E o TRECHO do
  entregável que a viola. Sem os dois, não é achado.
- Você não inventa regra. Se algo te cheirou mal mas não tem regra que sustente,
  vai em DÚVIDAS, separado — nunca como violação.
- Verifique de verdade, não por leitura. Número de plataforma se confere na
  plataforma (conector ou print), nomenclatura se confere caractere a caractere,
  fórmula se recalcula por fora.
- Revisão é só leitura. Nunca ative, edite, publique ou dispare nada, nem "só pra
  testar", nem com a entrada fechada. A trava de uma automação de escrita se prova
  lendo a configuração dela; se não houver como provar sem executar, isso é o achado.
- Conte também o que você NÃO conseguiu verificar e por quê. Revisão que só diz
  "ok" sem dizer o que ficou cego é pior que nenhuma.

SEVERIDADE
🔴 BLOQUEIO — dinheiro errado, dado inventado/sem fonte, escrita em plataforma sem
   as travas de sirius-scale/REGRAS.md §6.
🟡 FORA DO PADRÃO — contraria framework marcado PADRÃO CONSISTENTE (o "(proposto)"
   vale como VARIAÇÃO ISOLADA e vira 🔵), regra de frameworks-da-casa/, o briefing
   ou sirius-scale/REGRAS.md.
⬜ NÃO EXECUTADO — só existe se veio lista de "combinado" (modo d): item prometido
   que não apareceu no que foi revisado. Não é violação de regra, é esquecido.
🔵 OBSERVAÇÃO — risco ou melhoria; decisão de quem pediu.
❓ DÚVIDA — estranhou, mas não tem regra pra citar.

SAÍDA
1. O que foi conferido (item por item do checklist: passou / achado / não deu)
2. Achados por severidade, do mais grave pro menos
3. Dúvidas
4. O que ficou sem verificação, e o motivo
5. Veredito em uma linha: PODE SUBIR / CORRIGE ANTES / NÃO SOBE
```

## Passo 4 — Filtrar antes de repassar

Achado de subagente não vai cru pra pessoa. Antes:

1. **Confirme a citação.** Abra o arquivo da regra e confira que ela diz aquilo
   mesmo. Regra citada errado é o jeito mais rápido de a revisão perder confiança.
2. **Derrube o que é falso positivo por contexto que o subagente não tinha.**
   Exemplo real: criativo `PAUSED` na Meta costuma ser fila de troca de propósito,
   não erro — veja o briefing e o histórico do lançamento antes de reportar como
   falha. Falso positivo derrubado assim vale ser mencionado em uma linha, pra pessoa
   saber que foi visto e descartado.
3. **Cheque o nível de confiança.** Achado que se apoia numa linha marcada
   VARIAÇÃO ISOLADA, PADRÃO CONSISTENTE (proposto) ou PADRÃO INCONCLUSIVO não é
   BLOQUEIO — vira OBSERVAÇÃO, com o rótulo dito na cara (o "(proposto)" vale como
   VARIAÇÃO ISOLADA). E regra de framework com alcance `NÃO TESTADO FORA` aplicada
   aqui é dita como tal: força e alcance são eixos diferentes
   (`sirius-scale/REGRAS.md` §4).
4. **Junte duplicata** entre domínios (o mesmo ID de criativo errado aparece na
   campanha e na copy: é um achado, com dois lugares pra corrigir).

## Passo 5 — Entregar

No chat, curto e em lista numerada (`sirius-scale/REGRAS.md` §1). Quem pediu quer a
decisão, não a redação:

```
VEREDITO: CORRIGE ANTES  ·  2 bloqueios, 3 fora do padrão, 1 não executado, 1 dúvida

⬜ NÃO EXECUTADO (só no modo combinado — Passo 1d)
1. Combinamos desligar a segmentação otimizada do conjunto de remarketing B. Não
   apareceu no inventário — continua ligada. Provável esquecido, não erro de config.

🔴 BLOQUEIO
2. utm_term do anúncio novo está "VDNN-ROTINA-DA-MANHÃ" — acento vira %C3%83 na
   URL e suja o Dash. Regra: sirius-scale/frameworks/trafego/nomenclatura.md §3
   (regra 1). Corrigir pra: VDNN-ROTINA-DA-MANHA

🟡 FORA DO PADRÃO
3. ...

❓ DÚVIDA
4. ...

NÃO CONSEGUI VERIFICAR
5. Ação de conversão real dos 3 conjuntos novos — a conta bateu o limite de
   chamadas (erro 17). Ler de novo antes de ativar.
```

⬜ **NÃO EXECUTADO some do exemplo acima quando não veio do modo (d)** — só existe
achado desse tipo se houve lista de combinado pra cruzar. Nos modos (a)/(b)/(c),
sem plano declarado, não tem "esquecido" pra apontar — só "está certo ou errado".

Salve em `entregas/revisoes/<escopo>-<AAAA-MM-DD>.md`, sempre, sem perguntar — é o que
permite ver depois qual erro se repete e vira candidato a regra em
`frameworks-da-casa/`. Cabeçalho com escopo, data e veredito.

Se saiu 🔴, **não corrija de cara**. Mostre e pergunte se é pra corrigir. Se mandarem
corrigir, corrija e rode a revisão de novo só nos itens tocados.

📌 A revisão em si roda bem no modelo padrão (é checklist bem especificado). A correção
depende de onde está o erro (`sirius-scale/REGRAS.md` §6):

- **Em objeto ativo** (ativar, verba, lance, segmentação de algo que está rodando): é com
  vocês, no Gerenciador. O Claude não mexe em conta ativa, nem com pedido urgente. Na
  Meta, com o pedido escrito, o agente `gestor-trafego` pode montar a versão corrigida
  PAUSADA pelo conector, ler de volta e mostrar a linha de cada conjunto, pra vocês
  trocarem. No Google, o mesmo vale pelas ferramentas de `sirius-scale/ferramentas/google/`.
  Montar é escrita em conta de anúncio: pergunte antes se querem trocar pro modelo mais
  forte (Opus).
- **Em arquivo de `entregas/`** (pacote, análise, copy, página): segue normal, como no
  parágrafo acima.

Quando o veredito final for **PODE SUBIR** (limpo, ou já corrigido), ofereça o
próximo passo da ordem do `sirius-scale/REGRAS.md` §5 em vez de esperar alguém lembrar:
"Revisão limpa. Rodo o `/pente-fino` da sessão?" — são motores diferentes (este
aqui olha o entregável, o outro olha o que a sessão ensinou), mas não custa nada
oferecer o encaixe.

## Regras duras do revisor

1. **Não inventa regra.** O único critério válido é o que está escrito em
   `frameworks-da-casa/`, `sirius-scale/frameworks/`, `sirius-scale/REGRAS.md`, no
   `CLAUDE.md` de vocês ou nos arquivos de `expert/`, `lancamentos/` e `funis/`. "Boa
   prática de mercado" não é achado — é dúvida, na seção de dúvidas.
2. **Não inventa problema pra parecer útil.** Revisão limpa é resultado legítimo:
   diga "conferi X, Y e Z, tudo dentro do padrão" e liste o que conferiu. Achado
   inflado gasta o crédito da skill pro dia em que houver um de verdade.
3. **"Parece ok" não existe.** Ou conferiu e passou (diga contra o quê), ou não
   conferiu (diga por quê).
4. **Não corrige por conta própria**, nem o achado que parece trivial. Corrigir é
   passo separado, com quem pediu sabendo.
5. **Não escreve em plataforma externa.** Revisão é leitura. Se precisar consultar a
   plataforma pra conferir um número, só leitura, em lote e sem repetir à toa a mesma
   consulta (`sirius-scale/frameworks/trafego/_metodologia.md` §5). **Também não aciona
   automação nem conector de escrita**, nem pra testar a trava (com a entrada fechada,
   por exemplo). No caso de origem, um revisor rodou o executor de verba em modo de
   escrita "como teste de fail-safe", contra a instrução. Não gravou porque o executor
   parou pedindo confirmação, mas a trava se prova lendo, não executando.
6. **Erro que se repete vira regra.** Se o mesmo achado aparecer numa terceira
   revisão do mesmo tipo, sinalize: isso é candidato a registro em
   `frameworks-da-casa/` (`sirius-scale/REGRAS.md` §5), não a correção manual eterna.

## `/revisar` x `/pente-fino` — não confundir

As duas rodam no fim, as duas usam olhos frescos, e aí param de se parecer.

| | `/revisar` | `/pente-fino` |
|---|---|---|
| **Pergunta** | O que foi feito está certo? | O que a sessão ensinou e não ficou escrito? |
| **Olha pra** | O objeto: campanha, arquivo, número na plataforma | A sessão: o que apareceu no caminho |
| **Fonte do que ACONTECEU** | Plataforma e arquivos — **nunca a conversa** | A conversa — só eu enxergo, subagente não |
| **Produto** | Lista de achados + veredito | Linha nova em `frameworks-da-casa/` |
| **Efeito** | Conserta **esta** entrega | Deixa a **próxima** pronta |
| **Se voltar vazia** | Ótimo: a execução saiu limpa | Ótimo: nada morreu no chat |

O caso que separa os dois: subir campanha sem geo, como aconteceu no caso de origem.
O `/revisar` acha o grupo sem localização e manda corrigir. O `/pente-fino` pergunta
por que isso passou de novo se já estava escrito — e a resposta vira gatilho de
consulta ou item fixo do preflight (Passo 0), pra não depender de ninguém lembrar.

Roda os dois. `/revisar` antes de corrigir; `/pente-fino` depois, com a sessão
inteira já fechada — inclusive os achados da revisão, que são matéria-prima dele.

📌 Uma exceção pontual: no modo (d) do `/revisar` (Passo 1), a conversa entra pra
dizer **o que era esperado** — nunca pra provar **o que foi feito**, que continua
saindo só de plataforma e arquivos. É a mesma régua do `/pente-fino`: conversa serve
pra intenção e aprendizado, nunca como prova de execução.
