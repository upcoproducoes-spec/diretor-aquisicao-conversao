---
name: pente-fino
description: Varre uma sessão de trabalho já terminada (otimização de tráfego, subida de campanha, peça de copy, página, análise) e extrai o que foi aprendido mas não ficou registrado. Use quando pedirem "pente fino", "o que a gente aprendeu hoje", "passa um pente", ou ao fechar uma sessão longa. O objetivo principal é registrar, sempre em `frameworks-da-casa/`: o conhecimento tem que servir no PRÓXIMO lançamento, funil e produto, deixando a próxima peça pronta pra sair certa de primeira. Também tem o modo consulta, pra rodar ANTES de diagnosticar: mostra o que `frameworks-da-casa/` e `sirius-scale/frameworks/` já sabem sobre o tema e evita redescobrir o que já está escrito.
---

> Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
> são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
> ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.


# Pente fino — o que a sessão ensinou e ninguém anotou

O `sirius-scale/REGRAS.md` §5 manda registrar em `frameworks-da-casa/` o que foi corrigido
numa peça grande e vale pra próxima. Só que isso depende de eu **lembrar**, no fim de uma
sessão longa, do que apareceu no meio dela. Sessão de 4 horas com 30 leituras de
plataforma não sobrevive à memória. Esta skill é a varredura sistemática que substitui o
"lembrar".

**Onde o registro mora, sempre: `frameworks-da-casa/`.** Nunca em `sirius-scale/` nem em
`.claude/`: a atualização do sistema troca a `sirius-scale/` inteira e copia a `.claude/` por
cima, então o que fosse escrito lá se perderia ou seria sobrescrito (`sirius-scale/REGRAS.md` §4). Cada linha registrada entra com a
**data**, a **peça ou sessão de origem**, o **porquê** e o **rótulo de força** (nasce
VARIAÇÃO ISOLADA ou PADRÃO INCONCLUSIVO).

## A lição que originou esta skill (leia antes de rodar)

No caso de origem, o agente reportou por **quatro relatórios seguidos** que as campanhas
do Google estavam com a meta de conversão quebrada. Estava errado: lia
`selective_optimization` quando Demand Gen usa `campaign_conversion_goal`.

**O framework já dizia isso.** `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`
§2, escrito dez dias antes, registrava exatamente esse erro, cometido pelo mesmo agente,
com a tabela de qual campo vale em cada plataforma. Na mesma sessão, o §8 do mesmo
arquivo evitou outra rodada perdida — porque dessa vez o arquivo foi aberto.

📌 **O gargalo não é registrar, é consultar.** O conhecimento estava escrito,
acessível e correto. Por isso esta skill tem **dois modos**, e o de consulta é
tão importante quanto o de varredura.

---

# MODO 1 — VARREDURA (o padrão)

Roda ao fechar a sessão. Objetivo: nada do que foi aprendido morre no chat.

## Passo 1 — Extrair os candidatos (isto é comigo, não com subagente)

**Um subagente não enxerga esta conversa.** Então a extração é minha: eu percorro
a sessão e listo os candidatos. O subagente entra depois, pra verificar.

Percorra a sessão inteira procurando as **sete categorias** abaixo. Elas estão em
ordem de valor — a primeira é a que mais dói e a que mais escapa.

### 1. Conhecimento que JÁ EXISTIA e não foi consultado 🔴
Algum erro, diagnóstico ou descoberta desta sessão já estava escrito em
`frameworks-da-casa/`, `sirius-scale/frameworks/`, `sirius-scale/REGRAS.md` ou no
`CLAUDE.md` de vocês?
- Se sim, **não é aprendizado novo — é falha de consulta**, e o registro correto
  é um gatilho, não mais um parágrafo.
- Sinal típico: "ah, o framework já dizia isso".
- O que registrar: **quando** aquele arquivo devia ter sido aberto. Regra de
  consulta, não conteúdo novo.

### 2. Correção incompleta
Algo foi consertado pela metade e ninguém conferiu a cobertura.
- Exemplo real: no caso de origem, a estratégia de lance foi corrigida nas campanhas
  `[TESTE]` e ficou errada nas duas `[ESCALA]` — que eram o maior gasto. Só apareceu
  uma semana depois.
- Sinal típico: "corrigido em <data>" num registro, sem a lista do que foi coberto.

### 3. Armadilha técnica de plataforma
Erro de plataforma que custou uma rodada. Vai pra `frameworks-da-casa/`, num arquivo
técnico por plataforma (`frameworks-da-casa/<plataforma>-criacao-tecnica.md`), com a
mensagem de erro literal e o que resolveu. Ele complementa
`sirius-scale/frameworks/trafego/meta-criacao-tecnica.md` e
`sirius-scale/frameworks/trafego/google-criacao-tecnica.md`, que não se editam.
- Alcance: quase sempre `UNIVERSAL` (fato de plataforma, sem dimensão de negócio).

### 4. Padrão novo de performance
Algo que a análise mostrou e ainda não está em framework. Nasce **VARIAÇÃO ISOLADA**
ou **PADRÃO INCONCLUSIVO**, com o dado que sustenta.
- ⚠️ Se **contradiz** linha marcada CONSISTENTE (em `sirius-scale/frameworks/` ou em
  `frameworks-da-casa/`): **para e pergunta**. Sem exceção.

### 5. Decisão de vocês que virou regra
Alguém decidiu algo que vale pras próximas vezes e não foi anotado.
- Vai pra `frameworks-da-casa/`, com o **porquê**, não só o quê.
- Sinal forte: a pessoa repetiu. Se ela disse "eu já falei isso", é bandeira vermelha —
  registre e diga na entrega que era repetido.

### 6. Número levantado que não foi salvo
Dado apurado no meio da sessão que só existe no chat.
- Anexo de conversa e conta em planilha não são fonte. Salvar na hora, na pasta do
  lançamento ou do funil (`lancamentos/<AAAA-MM-nome>/dados/` ou `funis/<nome>/dados/`),
  dizendo de onde veio e quando.

### 7. Contradição
Algo dito nesta sessão contradiz o que está registrado.
- Pode ser: o registro envelheceu, ou a fala de hoje estava errada. **As duas
  possibilidades vão na entrega** — não escolha sozinho.

## Passo 2 — Verificar com olhos frescos (subagente)

Candidato extraído **não vira registro sem verificação**. Dispare um subagente
`general-purpose` com a lista. Ele não viu a sessão — e é justamente por isso que
serve: ele testa se o candidato se sustenta sozinho.

```
Você é verificador de aprendizados. Não registre nada, não edite arquivo: sua
saída é o parecer sobre cada candidato.

CANDIDATOS (extraídos de uma sessão que você NÃO viu — cada um vem com o dado
que o sustenta, você não precisa da conversa)
<lista numerada: o que se afirma, o dado/erro que sustenta, arquivo de destino
sugerido em frameworks-da-casa/, nível de confiança sugerido>

PARA CADA CANDIDATO, RESPONDA
1. JÁ EXISTE? Procure em frameworks-da-casa/, sirius-scale/frameworks/,
   sirius-scale/REGRAS.md e no CLAUDE.md. Cite arquivo e seção se achar.
   - Se já existe idêntico: DESCARTAR (e dizer onde está).
   - Se existe parecido mas incompleto: dizer o que falta.
2. CONTRADIZ algo registrado? Se contradiz linha marcada CONSISTENTE, marque
   PARAR — quem decide é a pessoa, não você; não registrar.
3. O DADO SUSTENTA a afirmação? N suficiente? A conclusão não vai além do dado?
4. DESTINO CERTO: qual arquivo de frameworks-da-casa/, e por quê esse. Nunca
   sirius-scale/ nem .claude/ (a atualização troca ou sobrescreve).
5. FORÇA E ALCANCE, separados (são eixos diferentes): a força é VARIAÇÃO ISOLADA ou
   PADRÃO INCONCLUSIVO (registro novo nunca nasce CONSISTENTE); o alcance, em
   frameworks-da-casa/, é DA CASA (o negócio de vocês) ou UNIVERSAL (fato de
   plataforma).

VEREDITO por candidato: REGISTRAR / DESCARTAR (já existe) / PARAR (contradiz
CONSISTENTE) / FRACO (dado não sustenta).

Não invente candidato novo. Seu trabalho é julgar os que vieram.
```

## Passo 3 — Registrar

Só o que voltou **REGISTRAR**, e sempre em `frameworks-da-casa/`:

| Situação | Ação |
|---|---|
| Padrão novo, não contradiz nada | Registra direto, como ISOLADA ou INCONCLUSIVO |
| Armadilha técnica de plataforma | Registra direto, no arquivo técnico da plataforma |
| Decisão de vocês | Registra direto, com o porquê |
| Sobe de ISOLADA pra CONSISTENTE | **Pergunta antes** |
| Muda o alcance de um arquivo | **Pergunta antes** |
| Contradiz linha CONSISTENTE | **Pergunta antes** |

Toda linha registrada cita **o dado que a sustenta** e leva o rótulo de confiança
na própria linha, junto com a data, a peça ou sessão de origem e o porquê.

Quando a resposta for manter a regra de vocês contra uma linha de
`sirius-scale/frameworks/`, a linha registrada diz qual seção ela substitui (arquivo e §).
Sem isso, quem lê os dois não sabe qual vale.

Framework novo inteiro, e não uma linha: o método de extração está em
`sirius-scale/frameworks/_extracao-de-frameworks.md`.

📌 **As três linhas "Pergunta antes" acima são julgamento que vira regra pra todo
lançamento futuro.** Ao chegar num candidato desses três tipos, sinalize antes de
perguntar: "isso é decisão de regra; quer trocar pro modelo mais forte (Opus) antes de
seguir?". As demais linhas da tabela (registro direto) rodam bem no modelo padrão —
extração e registro de padrão novo que não contradiz nada é trabalho de rotina.

## Passo 4 — Entregar

Curto, em lista numerada (`sirius-scale/REGRAS.md` §1). Nessa ordem:

```
PENTE FINO — sessão de <data>, <tema>

JÁ ESTAVA ESCRITO E NÃO FOI CONSULTADO  (o mais caro)
1. <o quê> — estava em <arquivo §>. Gatilho registrado: <quando abrir>.

REGISTRADO AGORA
2. <o quê> -> frameworks-da-casa/<arquivo> [VARIAÇÃO ISOLADA] — dado: <o que sustenta>

PRECISA DA PALAVRA DE VOCÊS
3. <o quê> — contradiz <arquivo §>, marcado CONSISTENTE.

DESCARTADO
4. <o quê> — já estava em <arquivo §>, sem novidade.

NÃO SOBREVIVEU AO DADO
5. <o quê> — N=<n>, fraco demais pra virar linha.
```

---

# O PRODUTO FINAL: conhecimento que serve no próximo trabalho

**Decisão do Rodrigo, e é o objetivo principal da skill.** Registrar não é arquivar o
que aconteceu — é deixar o próximo trabalho pronto. O teste de qualidade de todo
registro é:

> Daqui a dois meses, num lançamento diferente, eu vou conseguir **montar a peça ou a
> campanha certa de primeira** lendo isto?

Se a resposta for não, o registro é diário de bordo, não conhecimento.

## Separe o que transfere do que é do caso

Todo candidato aprovado é classificado antes de escrever (é o eixo do alcance, do
`sirius-scale/REGRAS.md` §4, aplicado no ato do registro):

| Tipo | Vai pra | Exemplo da base de origem |
|---|---|---|
| **Fato de plataforma** | `frameworks-da-casa/`, no arquivo técnico da plataforma, `UNIVERSAL` | miniatura obrigatória no criativo de vídeo da Meta |
| **Método / régua de decisão** | `frameworks-da-casa/`, no arquivo do domínio | topo com N baixo infla a escada inteira |
| **Jeito de vocês trabalharem** | `frameworks-da-casa/`, com o porquê | investimento se define como faixa, não número travado |
| **Número deste lançamento** | `lancamentos/<AAAA-MM-nome>/dados/` + citado na linha | conversão por faixa de uma edição |

⚠️ **Fato de plataforma e método transferem. Número de lançamento NÃO.** Ao escrever
um número numa linha de framework, ele entra como *evidência que sustenta*, nunca
como constante a reaplicar. Quem promove padrão a regra geral é o alcance, nunca a
força (`sirius-scale/REGRAS.md` §4).

## Mantenha o playbook de configuração

Existe um artefato que a skill **atualiza toda vez**, e é ele que faz o conhecimento
render no próximo lançamento: a receita de criação de vocês por plataforma, em
`frameworks-da-casa/`, que complementa

- `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`
- `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`

Eles não são só lista de armadilhas: são **a receita de como criar certo**. Ao
fechar uma varredura, pergunte:

1. Alguma coisa desta sessão muda **como se cria** campanha, conjunto ou anúncio?
2. A receita continua completa? (lance, meta de conversão, segmentação
   automática, públicos, campos obrigatórios novos, validação a seco)
3. Um erro desta sessão teria sido evitado se a receita estivesse seguida?

Se sim pra qualquer uma, a receita de vocês em `frameworks-da-casa/` se atualiza — não
só a lista de erros.

📌 **Instrução permanente carrega MÉTODO, nunca diagnóstico.** Texto que fica valendo em
toda sessão — o `CLAUDE.md` de vocês, uma regra em `frameworks-da-casa/`, a instrução de
uma rotina agendada (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md`) — que
congela uma conclusão apurada ("a conta está com X errado, não faça Y") reinjeta a
premissa a cada uso, muito depois de ela ter deixado de ser verdade. Diagnóstico
envelhece; instrução automática não. A instrução diz **como conferir**, o relatório diz
**o que foi achado**. Toda varredura confere se alguma instrução permanente está
carregando conclusão em vez de método.

---

# MODO 2 — CONSULTA (antes de diagnosticar)

`/pente-fino consulta <tema>` — roda **antes** de afirmar diagnóstico, não depois.

É o remédio direto pro erro que originou a skill. Dispare quando for:
- afirmar que uma configuração de plataforma está errada
- explicar por que um custo subiu ou caiu
- criar campanha, conjunto ou anúncio novo
- dizer "isso é um bug" sobre qualquer ferramenta
- **afirmar que uma ação CABE no teto**
- **atribuir uma variação a uma causa**

**Os dois últimos gatilhos, e por que entraram:**

**Teto.** No caso de origem, o agente somou orçamento de cabeça no chat, disse que a
ativação cabia, e ela foi barrada pelo teto. As regras de segurança de lá tinham um
aviso dizendo exatamente que aquele teto já barrava operação normal — o arquivo tinha
sido lido e mesmo assim ninguém conectou na hora de fazer a conta.
→ **Nunca somar teto de cabeça.** A soma sai da plataforma (o orçamento diário de cada
campanha ativa, lido pelo conector ou na tela), com a fonte dita na resposta: no caso de
origem, três leituras diferentes devolveram três totais diferentes pra mesma conta no
mesmo dia. A `/preflight` (`.claude/skills/preflight/SKILL.md`) faz essa conta no item 1:
rode ela em vez de refazer a soma na mão.

**Causa.** Afirmou-se que a audiência "explodiu no orgânico" usando a contagem pública
de views, que inclui as pagas, num período que o YouTube Analytics nem tinha processado.
Quem pegou foi o Rodrigo, olhando o número bruto — terceira vez que isso acontecia.
→ Antes de escrever "por causa de X": que outra causa explicaria o mesmo movimento, a
métrica separa as duas, e a janela tem dado até o fim? (As armadilhas de medição do
YouTube estão em `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.1.)

**O que fazer, em 30 segundos:**

1. Abrir o arquivo técnico da plataforma envolvida
   (`sirius-scale/frameworks/trafego/meta-criacao-tecnica.md` ou
   `sirius-scale/frameworks/trafego/google-criacao-tecnica.md`, mais o de vocês em
   `frameworks-da-casa/`, se existir) e varrer os títulos de seção. Só os títulos já
   pegam a maioria.
2. Procurar o termo central (nome do campo, código do erro, nome da métrica) nas duas
   pastas de regra: `grep -rn "<termo>" frameworks-da-casa/ sirius-scale/frameworks/`
   (e no `CLAUDE.md` de vocês).
3. Conferir se o **lançamento de referência** (o último que funcionou) tem o mesmo
   "defeito". Se tem, o errado provavelmente é a leitura, não a conta.
4. Se o tema é configuração de conta de anúncio, rodar a `/preflight`: ela lê da plataforma,
   sempre os mesmos 12 itens, e não depende de ninguém lembrar.

**Três reflexos que teriam evitado o erro que originou a skill:**

| Reflexo | Por quê |
|---|---|
| Campo vazio não é prova | Primeira hipótese é "estou lendo o recurso errado", não "não está configurado" |
| Confere pelo efeito | Se a campanha entrega lead barato com MQL normal, ela **não** está otimizando pra outra coisa — o efeito contradiz a leitura do campo |
| Compare com a referência | Se o lançamento anterior que funcionou mostra o mesmo, é a sua leitura |

---

## Regras duras

1. **Não infla.** Sessão longa não significa muitos aprendizados. A maioria do que
   acontece numa sessão é execução, não conhecimento novo. Registrar ruído
   envenena o framework — quem lê depois não distingue o que importa.
2. **Não registra o que já está escrito.** Duplicata é pior que ausência: cria
   duas fontes que divergem com o tempo.
3. **Aprendizado sem dado é dúvida.** Se não dá pra citar o número, o erro literal
   ou a decisão explícita, vai pra "precisa da palavra de vocês", não pro framework.
4. **Falha de consulta ≠ conhecimento novo.** Quando o kit ou `frameworks-da-casa/` já
   sabia, o registro é um **gatilho** (quando consultar), nunca outro parágrafo do mesmo
   conteúdo.
5. **Não edita framework em confiança alta sem perguntar.** Quem sobe uma regra pra
   CONSISTENTE é quem é dono da operação, nunca o Claude sozinho
   (`sirius-scale/REGRAS.md` §4). Mexer em alcance ou apagar linha existente também
   passa por quem decide.
6. **Registro só em `frameworks-da-casa/`.** Nunca em `sirius-scale/` nem em `.claude/`:
   a atualização troca a `sirius-scale/` inteira e sobrescreve a `.claude/`.
7. **Salva a varredura.** `entregas/pente-fino/<AAAA-MM-DD>-<tema>.md`. É o que permite
   ver qual erro se repete — e erro que aparece três vezes vira linha de framework, não
   correção manual eterna.
