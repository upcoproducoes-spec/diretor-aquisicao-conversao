# Framework — Disparo de WhatsApp (grupo + API oficial + DM automatizada)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** execução e voz
> **Base:** 1 cliente (o caso-base, um expert de educação) · 3 lançamentos · 39 mensagens (piso
> verificado, contado peça a peça)
> **Alcance:** NÃO TESTADO FORA — os rótulos CONSISTENTE abaixo valem *dentro*
> desta base. Antes de aplicar em outro cliente, ler a **seção 6 (o que é
> reutilizável e o que é do caso)**.

Reverse-engineered a partir de 39 mensagens reais produzidas nas conversas de projeto do caso-base (não de documento anexado), em 3 lançamentos gratuitos dele, aqui chamados pela ordem: **L1** (o mais antigo, com captação num mês e carrinho no seguinte), **L2** (alguns meses depois) e **L3** (o mais recente).

> Nos moldes, `*asterisco*` é o negrito do WhatsApp.

> **Por onde sai.** Este arquivo trata do que a mensagem diz. O disparo pra lead sai pela
> ferramenta de automação de vocês (ex.: Full Funnels; acesso e armadilhas em
> `sirius-scale/frameworks/automacao/fullfunnels-highlevel.md`) ou pela API oficial (modo A), e
> segue `sirius-scale/REGRAS.md` §6: nasce pausado ou agendado, com confirmação de quem é dono e
> leitura de volta. Mensagem avulsa e de volume baixo por automação não oficial (Baileys) tem as
> armadilhas em `sirius-scale/frameworks/automacao/whatsapp-baileys.md`, que não serve pra disparo
> em massa: pra isso existem os modos A e B daqui.

## 1. Escopo e base de evidência

**O que foi analisado (5 fontes, tudo trabalho real de conversa, nenhuma peça inventada):**

- **Fonte A — Fluxo de API oficial de boas-vindas (L1).** 5 mensagens: MSG1 utility com botões, MSG2A/2B de roteamento, MSG3 presente, MSG4 indicação.
- **Fonte B — Disparos de grupo de aquecimento (L3).** ~17 mensagens da semana 1: card de domingo, e por dia útil o trio 9h (aluno), 19h ("falta 1h") e 20h ("no ar").
- **Fonte C — Disparos de grupo de carrinho/VIP (L1).** Série VIP progressiva das 07h (6 mensagens), chamada pra carta + grupo VIP (2 versões).
- **Fonte D — Grupo VIP (L2).** 3 versões da mesma mensagem de convite VIP, com correções do Rodrigo.
- **Fonte E — DM automatizada + mensagens de horário de live (L2).** Mensagem de ManyChat pro grupo VIP (versão anterior + reescrita) e o bloco 20h/20h10/20h20/20h35/22h.

Foram contadas **39 mensagens direto nas conversas lidas**. A semana 2 do L3 e disparos de API adicionais elevam o total, mas não foram contados peça a peça, então 39 fica declarado como piso verificado.

**O que ficou de fora de propósito:**

- **E-mail** (artefato separado, framework próprio: `sirius-scale/frameworks/copy/email.md`) e **legenda de Instagram** (idem). Só entra aqui o que é disparo de mensagem, não peça de feed.
- A **DM da Fonte E é Instagram Direct via ManyChat, não WhatsApp.** Incluída porque é disparo 1:1 automatizado e compartilha a mesma lógica, mas o canal fica marcado.
- **Telegram**: o brief do artefato fala "WhatsApp ou Telegram". Não existe nenhuma peça de Telegram no projeto. Só WhatsApp e Direct.

**Ressalva estrutural, com todas as letras:** a base é de **um cliente só, o caso-base.** Não há segundo cliente no projeto. O que sustenta o framework são **3 lançamentos dele** (L1, L2, L3), o que já dá pra cravar padrão de canal, mas não responde se a peça funciona em outro expert ou outro nicho. Além disso, o corpo é puxado pra captação/aquecimento; a fase de **carrinho aberto** tem menos unidades (Fontes C e D) e está concentrada no L1 e no L2.

## 2. A fórmula, em ordem

WhatsApp não é uma fórmula linear única. São **3 modos**, cada um com esqueleto próprio. Abaixo os três e depois o DNA que todos compartilham.

**MODO A — API oficial (fluxo automatizado 1:1, pós-inscrição).** *PADRÃO CONSISTENTE (5 unidades, 1 lançamento)*

1. Confirmação neutra em utility (barata, aprovável na Meta) + roteamento por botão.
2. Ramificação: já está no grupo → entrega; ainda não → link do grupo.
3. Entrega da isca (presente/pesquisa).
4. Pedido de indicação.

**MODO B — Grupo de massa, lembrete de live.** *PADRÃO CONSISTENTE (trio × 5 dias, reforçado no L2)*

1. Gancho no tema da live (dor ou pergunta), sem entregar o conteúdo.
2. Informação prática (horário, onde, quanto falta).
3. CTA único (link + "ativa o lembrete" ou "entra agora").

**MODO B' — Grupo de massa, urgência de carrinho/VIP.** *PADRÃO CONSISTENTE (Fontes C e D, 2 lançamentos)*

1. Abertura/notícia ([o fato novo], [recado pra quem está em dúvida], [a pessoa chegou na hora]).
2. Vantagem ou entregáveis (o que ganha ao entrar / ao ser VIP).
3. Âncora de urgência real (prazo, horário de abertura, antecedência do VIP).
4. CTA único no botão.

**MODO C — DM automatizada (resposta a comentário palavra-gatilho).** *VARIAÇÃO ISOLADA (base = 1 mensagem iterada; canal é IG Direct)*

1. Reconhece a ação do lead sem bajular.
2. Vantagem concreta de entrar no grupo.
3. CTA único no botão.

**DNA compartilhado pelos 3 modos:**

- Uma decisão por mensagem. CTA único (o utility usa botões só pra rotear).
- Voz do expert em 1ª pessoa, curta e direta, quando a mensagem é dele. O utility foge disso de propósito (neutro).
- Roma comprimida no máximo uma vez, e só onde cabe (`sirius-scale/frameworks/lancamentos/roma-e-promessa.md`).
- Negrito com `*asterisco*`, texto pronto pra colar sem formatação de markdown.
- Variação obrigatória de abertura, gancho e CTA entre mensagens da mesma sequência.

## 3. Cada etapa detalhada

Detalhadas as **4 etapas que cruzam os modos** (abertura, corpo, âncora, CTA), mostrando como cada modo preenche cada uma.

### 3.1 Abertura / gancho — *PADRÃO CONSISTENTE (aparece em todas as 39 unidades)*

**O que entra:** a primeira linha muda conforme o modo. Utility abre com confirmação factual. Grupo de aquecimento abre com pergunta ou dor ligada ao tema. Grupo de carrinho abre com notícia/urgência. DM abre reconhecendo a ação do lead.

**Por quê:** a abertura decide se a pessoa lê o resto no meio de um grupo barulhento. Ela também sinaliza a natureza da mensagem (aviso neutro x conteúdo x venda), o que segura a confiança do lead.

**Variações aceitáveis:** pergunta direta, dor, notícia, saudação temporal ("Bom dia, [como o expert chama o público]!"). O que não varia: não abrir com bajulação genérica nem com instrução.

**Molde (Fonte B, 19h, gancho por dor):**

> [Pergunta sobre quantas vezes a pessoa viveu a situação de pressão, com a falta de tempo em negrito.]

**Molde (Fonte C, abertura de carrinho por notícia):**

> 🚨 [Recado pra quem ainda está em dúvida.]

**Molde (Fonte E, DM, reconhece a ação):**

> [Frase que diz que a pessoa chegou na hora.] 🔐

### 3.2 Corpo — a substância — *PADRÃO CONSISTENTE*

**O que entra:** o motivo da mensagem. No aquecimento, uma frase que dá tangibilidade ao tema sem ensinar. No carrinho, os entregáveis ou a vantagem. No fluxo de API, a instrução do próximo passo.

**Por quê:** é onde o lead entende o que ganha se agir. No aquecimento, o corpo cria curiosidade sem resolver; no carrinho, empilha valor real antes de pedir a ação.

**Variações aceitáveis:** uma frase (aquecimento) até uma lista de bullets com check (carrinho/VIP). Bullet só quando há entregáveis reais pra listar, nunca pra encher.

**Molde (Fonte B, corpo de aquecimento, cria curiosidade sem entregar):**

> [Frase que tira o problema de onde a pessoa acha que ele está e aponta a etapa que trava.]

**Molde (Fonte E, corpo VIP com vantagem em bullet):**

> ✅ [a antecedência real do VIP, com o tempo em negrito]
> ✅ [a condição que só o grupo tem]

### 3.3 Âncora — urgência real, valor ou presente — *PADRÃO CONSISTENTE no carrinho; VARIÁVEL no aquecimento*

**O que entra:** o elemento que justifica agir agora. Carrinho usa prazo/horário real. Aquecimento usa o "está no ar agora" ou "daqui a uma hora". API usa o presente como recompensa.

**Por quê:** move o lead do "depois eu vejo" pro clique. A âncora tem que ser fato operacional (janela de inscrição, horário da transmissão, antecedência do VIP), não escassez inventada.

**Variações aceitáveis:** horário de abertura, contagem de horas real, antecedência do VIP, transmissão que acabou de entrar no ar, presente liberado. **Não vale** vaga limitada fabricada nem contagem regressiva sem lastro.

**Molde (Fonte B, âncora por transmissão no ar):**

> 🟢 *[Aviso de uma palavra de que começou.]*
> [Qual live, e que ela entrou no ar agora.]

**Molde (Fonte E, âncora por antecedência real do VIP):**

> [Dia e hora em que as inscrições abrem, em negrito] + [quem está no grupo tem a vantagem antes do público geral].

Observação de honestidade: o original desse trecho da Fonte E ainda falava em vaga e em garantir lugar. Ver seções 4 e 7 sobre a regra de escassez, que endureceu depois destas peças.

### 3.4 CTA único — *PADRÃO CONSISTENTE*

**O que entra:** uma ação só, no botão ou no link. Verbo que já sinaliza o que acontece ao tocar.

**Por quê:** duas ações competindo derrubam a taxa de clique. Um CTA por mensagem mantém o lead num trilho só.

**Variações aceitáveis:** botão nomeado (GRUPO VIP, Acessar PRESENTE), link + "ativa o lembrete", "entra agora". No utility, botões de roteamento contam como decisão única (entrar no grupo ou não).

**Molde (Fonte B, CTA de lembrete):**

> [Pedido pra se preparar pra live e ativar o lembrete.] 👇
> 🔗 *YouTube:* [inserir link]

**Molde (Fonte D, CTA em botão nomeado):**

> 👇 [Convite pra entrar agora.]
> *[botão] GRUPO VIP 🔥*

## 4. Regras transversais

**Tom.** Voz do expert do caso-base: linhas curtas, muita quebra de parágrafo, endereçamento direto, calorosa e firme. O utility é a exceção proposital: neutro, factual, sem copy persuasiva, pra baratear o disparo e passar na aprovação da Meta. Isso é *PADRÃO CONSISTENTE* e veio de instrução explícita do Rodrigo ("Essa mensagem não tem muita copy porque enviamos no modelo utility, mais barato porém menos atrativo. Temos que manter nesse formato, pelo menos a primeira mensagem, para ser aprovada").

**Tamanho.** Curto. Utility mais curto ainda. Nenhuma mensagem de grupo passa de poucos parágrafos.

**O que nunca aparece (e que foi cortado toda vez que apareceu):**

- **CTA instrutivo demais.** Cortado no L2: [a frase que explicava onde apertar e o que estava escrito no botão] tratava o lead como se ele não soubesse usar um botão. *PADRÃO CONSISTENTE* a partir do L2.
- **Bajulação genérica.** Cortado no L2: [o parabéns por um passo grande] foi tirado por ser lisonja vazia pra quem só comentou uma palavra.
- **Explicar demais o que é o grupo** pra quem já tem contexto (quem comentou VIP num post do programa principal já sabe o que é).
- **"estou ao vivo" em transmissão pré-gravada.** Proibido no L3. Formas certas: "começou", "está no ar", "entrando agora". *PADRÃO CONSISTENTE dentro do L3*, veio de instrução do Rodrigo.
- **Travessão.** Tratado como marcador de IA. Ainda aparece em peça antiga (a MSG4 do L1 tem um travessão no meio da promessa), então é regra que só passou a valer depois.

**Escassez fabricada — atenção, ponto que não fecha dentro do WhatsApp.** *PADRÃO INCONCLUSIVO no corpus de WhatsApp.* A regra atual da casa proíbe "vagas limitadas", "garanta sua vaga". Mas as peças de carrinho do WhatsApp são do L1 e do L2 e ainda usam esse tipo de linguagem (vaga e garantir lugar, na Fonte E; escassez explícita na série VIP do L1). A regra "sem escassez" está provada no material do evento pago (um ciclo posterior, fora destes três lançamentos), não nos disparos de WhatsApp lidos. Ou seja: aplique a regra por herança da casa, mas saiba que ela ainda não foi testada num carrinho de WhatsApp do programa principal.

**Formatação de entrega.** Negrito com `*asterisco*`, mensagens enviadas sem formatação de markdown pra colar direto. *PADRÃO CONSISTENTE*, instrução do Rodrigo repetida.

**Subir pro Google Docs apaga o negrito do WhatsApp — fato de ferramenta (medido na casa).** O conversor markdown → Docs do Drive lê `*palavra*` como itálico e some com o asterisco; quem copia do Doc pro WhatsApp perde o negrito sem perceber. O que funciona: na **cópia de upload** (nunca no arquivo-fonte), escapar cada asterisco simples (`*` → `\*`, sem mexer no `**negrito**` de markdown) e **conferir lendo de volta** (exportar o Doc em texto e contar os asteriscos contra o original). Rodou limpo nos 4 documentos de WhatsApp de uma antecipação de Black (56, 8, 30 e 14 asteriscos, todos preservados), com a regex `(?<!\*)\*(?!\*)` pra achar o asterisco simples. **Resolvido na casa depois:** o documento passou a ser montado a partir de HTML, e não pelo conversor de markdown, o que deixa o asterisco simples como está, e um teste em código trava isso. Quem sobe pelo conversor de markdown continua precisando do escape acima, e isso é frágil: depende de alguém lembrar no próximo upload de WhatsApp.

**Disparo de WhatsApp fica registrado em documento antes de sair (decisão do Rodrigo):** "email so sai de doc, e disparos no whatsapp tambem tem que star registrados no drive, grupos e api oficial". Mensagem de grupo e de API oficial pra lead entra como `MENSAGEM - ASSUNTO - TAG` (`sirius-scale/frameworks/operacao/nomenclatura-drive.md` §2), na pasta certa do lançamento, passando primeiro pelo passo de copy (revisão) e depois pelo de programar, como no e-mail (`sirius-scale/frameworks/copy/email.md` §4.1).

## 5. Moldes consolidados do caso-base, por modo

Os moldes mantêm a ordem, o tamanho, os emojis e os horários das mensagens reais. Frase de mensagem enviada não vem literal: o colchete diz o que cada linha faz. `[nome]` é a variável de nome da ferramenta de disparo.

**Modo A — Fluxo de API (Fonte A), MSG1 utility:**

> [Saudação com o `[nome]`.]
> [Confirmação factual da inscrição, com o nome do evento em negrito.] 🎉
> [Por que estar no grupo importa, em negrito.]
> [Instrução curta de tocar no botão.] 👇
> [BOTÃO 1: quer entrar no grupo]
> [BOTÃO 2: já está no grupo]
> [BOTÃO 3: bloquear mensagens]

**Modo A — MSG4, indicação (com Roma comprimida uma vez):**

> [`[nome]` + parabéns pela inscrição.] 🎉
> [O evento como caminho pra Roma, numa frase: o resultado, o prazo e o mecanismo, em negrito.]
> [Convite pra chamar quem sofre com a mesma dor.]
> *[Instrução de copiar o link e encaminhar.]*
> 👉 [LINK DA PÁGINA DE INSCRIÇÃO]
> [A data da primeira aula.]
> [Assinatura do expert.]

**Modo B — Trio de lembrete de um dia (Fonte B), 9h aluno → 19h falta 1h → 20h no ar:**

> ☀️ *[Saudação da manhã, pelo jeito que o expert chama o público.]*
> [Convite pra ouvir uma história antes de começar o dia.]
> [Uma aluna, há quanto tempo ela tentava e a parte que a derrubava, em negrito.]
> [A virada: o que ela entendeu sobre essa parte, pelo mecanismo.]
> [O resultado dela nessa parte, em negrito.]
> [A conversa com ela está no ar agora, e o convite pra ouvir.] 👇
> 🔗 *YouTube:* [inserir link]

> [Pergunta sobre quantas vezes a pessoa viveu a situação de pressão, com a falta de tempo em negrito.]
> [Frase que tira o problema de onde a pessoa acha que ele está e aponta a etapa que trava.]
> [Quanto falta e o horário, em negrito, com o número da live.]
> *[O título da live, com o benefício concreto e o número.]*
> [Pedido pra se preparar pra live e ativar o lembrete.] 👇
> 🔗 *YouTube:* [inserir link]
> [Até o horário da live.]

> 🟢 *[Aviso de uma palavra de que começou.]*
> [Qual live, e que ela entrou no ar agora.]
> [O benefício concreto da live, em negrito, ligado a um hábito que muda.]
> [Convite pra entrar agora.] 👇
> 🔗 *YouTube:* [inserir link]

**Modo B' — Carrinho/VIP (Fonte C), abertura da chamada pra carta:**

> 🚨 [Recado pra quem ainda está em dúvida.]
> 👉 [Dia e hora em que as inscrições abrem] + [a decisão está com a pessoa].

**Modo C — DM automatizada (Fonte E):**

> [Frase que diz que a pessoa chegou na hora.] 🔐
> [O que é o grupo: quem ele reúne e o que essas pessoas decidiram, pela Roma.]
> [Frase que puxa a vantagem.]
> ✅ [a antecedência real do VIP, com o tempo em negrito]
> ✅ [a condição que só o grupo tem]
> [Dia e hora em que as inscrições abrem, em negrito] + [quem está no grupo tem a vantagem antes do público geral].
> 👇 [Convite pra entrar agora.]
> *[botão] GRUPO VIP 🔥*

## 6. O que é reutilizável e o que é do caso

**Reutilizável em qualquer cliente/lançamento:**

- A arquitetura de 3 modos e o fluxo de API utility → grupo → presente → indicação.
- O trio de lembrete de live (gancho no tema, info prática, CTA único) e o padrão 9h/19h/20h.
- Urgência ancorada em fato operacional real, um CTA por mensagem, negrito com asterisco, variação obrigatória entre mensagens da mesma sequência.
- Utility neutro pra baratear e passar na Meta.

**Do caso (o caso-base e o nicho dele):**

- A Roma específica do caso-base.
- As palavras-gatilho do caso-base e a mecânica de comentário → direct.
- A credencial do expert do caso-base e o inimigo que ele combate.
- A proibição de "estou ao vivo" (nasce do formato pré-gravado dele).
- Presente/pesquisa como isca de entrada no grupo e o VIP com 1h de antecedência.

## 7. Pontos em aberto

- **Métrica por mensagem: não existe** no projeto. Não dá pra dizer qual abertura ou CTA converte mais. O único dado é debrief de lançamento (ROAS, conversão), sem recorte por peça.
- **Regra de escassez dentro do WhatsApp: INCONCLUSIVO.** As peças de carrinho são do L1 e do L2 e ainda usam linguagem de vaga. Falta um carrinho do programa principal no WhatsApp já sob a regra nova pra confirmar como fica.
- **Carrinho aberto completo: base fina.** Há VIP de abertura, boleto e chamada pra carta, mas não a régua dia a dia inteira de um carrinho do programa principal no grupo. Precisa de mais um lançamento.
- **Modo C (DM): base de 1 mensagem iterada**, e o canal é IG Direct, não WhatsApp. Marcado como variação isolada de propósito.
- **API marketing (não-utility): quase não produzido.** Só há o utility + o fluxo. A copy de API mais persuasiva aparece como estratégia no doc de LPSG do projeto do caso-base, não como peça pronta.
- **Série VIP progressiva das 07h (Fonte C):** a estrutura está documentada (6 mensagens, urgência crescente das 07h às 07h55), mas o texto literal de cada uma não foi copiado na extração, então não foi citado verbatim. Fica como lacuna do caso de origem.

## 8. Operação pelo SendFlow (MCP): lido na casa

Os grupos do caso-base são disparados pelo SendFlow, e o MCP `sendflow` lê e agenda. Em outra ferramenta de grupo vale a lógica, e muda o comando. Agendar segue `sirius-scale/REGRAS.md` §6.

- **Cada família de grupo é uma campanha** (release): no caso-base, uma pros grupos de eventos, uma pros grupos de alunos e duas pros grupos da Black, de quem se inscreveu (alunos e não alunos).

  A equipe agenda direto no SendFlow e reescreve o texto da peça com o link de cada grupo. Antes de agendar qualquer coisa, listar o que já está agendado na campanha, pra não mandar duas vezes.
- **Ver o que está agendado:** `list-actions` com `releaseId`, `scheduled: true` e `orderBy: scheduledTo`. Sem o `scheduled`, o `orderBy: scheduledTo` volta HTTP 400 (falta índice no banco deles); pro histórico, usar a ordem padrão (`createdAt`). O texto vem com `includeMessages: true`. O `scheduledTo` vem em UTC (12h30 de Brasília = `15:30Z`).
- **Dois ids por grupo:** só o `gid` (número que começa com `12036…`) serve pra mandar mensagem. O `id` curto da campanha é só pra gerenciar o grupo dentro dela (instrução do próprio MCP).
- O registro em documento (`MENSAGEM - ASSUNTO - TAG`, §4) vale também pro que sai por aqui.
