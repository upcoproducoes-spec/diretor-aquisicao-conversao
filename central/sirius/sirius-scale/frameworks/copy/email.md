# Framework — Sequência de e-mail (captação, boas-vindas, carrinho aberto, carrinho fechando)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** execução e voz
> **Base:** 1 cliente (o caso-base, um expert de educação) · 3 lançamentos · ~10 e-mails completos
> **Alcance:** NÃO TESTADO FORA — os rótulos CONSISTENTE abaixo valem *dentro*
> desta base, não são regra geral. Antes de aplicar em outro cliente, ler a
> **seção 6 (o que é reutilizável e o que é do caso)**.
> **Desigual por fase:** carrinho fechando tem 2 lançamentos; captação,
> boas-vindas e carrinho aberto têm 1 cada. A força não é uniforme no arquivo.

Reverse-engineered a partir de ~10 e-mails completos e dezenas de variações de assunto/preview produzidos nas conversas de projeto do caso-base, em 3 lançamentos: um lançamento gratuito mais antigo (captação num mês, carrinho no seguinte; aqui, **o ciclo antigo**) e o ciclo de um evento pago, bem depois, em que fecharam duas ofertas (a turma do programa principal e um curso menor; aqui, **o ciclo recente**).

## 1. Escopo e base de evidência

**O que foi analisado (3 fontes, tudo trabalho real de conversa):**

- **Fonte A — Captação + boas-vindas do ciclo antigo.** Uma conversa de copy do lançamento. Dois e-mails de convite pra lista antiga (com variações de título A/B/C cada) e o e-mail de boas-vindas/reforço pós-inscrição.
- **Fonte B — Carrinho do ciclo antigo.** E-mail de "inscrições abertas" (carrinho aberto do programa principal) e e-mail de boleto parcelado (fechando hoje).
- **Fonte C — Carrinho fechando do ciclo recente.** Duas ofertas na mesma conversa:
  - **C1 — um curso menor:** sequência quinta/sexta, com duas versões cada (a do Claude e a reescrita a partir das mensagens fechadas do Rodrigo).
  - **C2 — a turma do programa principal:** e-mails de fechamento (meio-dia identidade, 20h consequência) e o banco de variações de assunto/preview.

Foram contados **~10 e-mails completos distintos** e dezenas de variações de assunto/preview. Deduplicação: a Fonte C tem versões concorrentes do mesmo e-mail (Claude x Rodrigo); o e-mail contou uma vez, e as duas versões ficaram como variação.

**O que ficou de fora de propósito:**

- **Disparo de WhatsApp** e **legenda de Instagram** (artefatos separados, frameworks próprios; o de WhatsApp é `sirius-scale/frameworks/copy/disparo-whatsapp.md`). Onde a mesma conversa tinha WhatsApp e e-mail (Fonte C), só o e-mail entrou aqui.
- **Carta de vendas longa por e-mail:** aparece citada como estratégia nos docs, mas não há carta de vendas por e-mail produzida no projeto. Não foi inventada. Vai pra Pontos em aberto.

**Ressalva estrutural, com todas as letras:** a base é de **um cliente só, o caso-base.** Não há segundo cliente no projeto. Sustentam o framework **3 lançamentos dele**. A distribuição é desigual por fase: **carrinho fechando** é a fase forte (2 lançamentos, o ciclo antigo e o recente, vários e-mails). **Captação, boas-vindas e carrinho aberto** têm um lançamento só cada.

## 2. A fórmula, em ordem

O e-mail se organiza por **fase do funil**. São 4 fases, cada uma com função e esqueleto próprios. Depois, a anatomia de um e-mail isolado (seção 3) e o DNA compartilhado.

**FASE 1 — Captação / convite (reativar lista antiga pro evento).** *VARIAÇÃO ISOLADA (1 lançamento, 2 e-mails)*

1. Assunto que promete acesso/benefício ou fisga por dor.
2. Convite pro evento gratuito, ancorado na Roma (`sirius-scale/frameworks/lancamentos/roma-e-promessa.md`).
3. Reforço num segundo e-mail com ângulo diferente (dor, prova social, quebra de padrão pra quem não abriu).

**FASE 2 — Boas-vindas / nutrição pós-inscrição.** *VARIAÇÃO ISOLADA (1 lançamento, 2 e-mails)*

1. Confirmação + próximos passos (grupo, pesquisa/presente).
2. Reforço pra quem não completou, com linha de escape ("se já fez, ignore").

**FASE 3 — Carrinho aberto.** *VARIAÇÃO ISOLADA (1 lançamento, base fina)*

1. Anúncio da abertura + [frase que abre o jogo com a pessoa].
2. Retomada da jornada do lead (o que ele viu/sentiu na semana).
3. Oferta completa (entregáveis + bônus) + Roma.
4. Urgência real (prazo/bônus estendido) + CTA.

**FASE 4 — Carrinho fechando.** *PADRÃO CONSISTENTE (2 lançamentos, o ciclo antigo e o recente)*

1. Abertura direta pela urgência do encerramento (ou por um ângulo novo do dia).
2. Um argumento só, bem escolhido (dor de agir no escuro, escolha comigo x sozinho, custo de não agir).
3. Recap enxuto da oferta (sem repetir tudo).
4. Âncora de prazo real (meia-noite / a turma fecha).
5. CTA único + pedido de resposta.

**DNA compartilhado pelas fases:**

- Um e-mail = um ângulo. E-mails do mesmo dia ou da mesma sequência nunca repetem abertura, gancho ou fórmula.
- Voz do expert em 1ª pessoa, direta e honesta, com fecho assinado: [a despedida que ele usa] + [nome do expert].
- Roma comprimida no máximo uma vez, quando cabe.
- Credencial do expert no máximo uma vez, de leve, com a formulação variada entre e-mails.
- CTA único em botão nomeado.

## 3. Cada etapa detalhada (anatomia de um e-mail)

### 3.1 Assunto + preview text — *PADRÃO CONSISTENTE (par que não repete)*

**O que entra:** um assunto curto e um preview text que **complementa**, não repete. O par é pensado junto.

**Por quê:** assunto e preview são o único espaço que decide a abertura. Se o preview só ecoa o assunto, desperdiça metade do gancho.

**Variações aceitáveis:** ângulos rotativos, testados em banco. Pergunta [sobre o que a pessoa vai fazer sem o produto], identidade [quem ela deixou de ser, e o que vem agora], consequência [o que muda quando o prazo acabar], direto com nome, curiosidade/loop aberto [o que o expert vai fazer antes de fechar], sóbrio [o fato do encerramento, sem adjetivo].

**O nome do lead vai no assunto e no preview sempre que der** (decisão do Rodrigo no caso de origem: "sempre que possível, chamar pelo nome, no título, até naquela descrição do e-mail"). VARIAÇÃO ISOLADA.
- No texto do e-mail, a marca é `[nome]`, também no pré-cabeçalho. Na ferramenta de envio ela vira o campo do primeiro nome do contato (no Full Funnels/HighLevel, `{{contact.first_name}}`).
- Antes de mandar, confira que o assunto e o preview levam a marca.
- Quem chega sem nome (ou com o e-mail ou uma letra só no lugar dele) é pouco, mas existe: pra esses a marca sai, e "[nome], sua inscrição…" vira "Sua inscrição…".
- Com o nome nos dois, o par continua sem repetir a ideia (a regra acima).
- Sem nome, a marca sai junto com a vírgula de antes dela: `Até lá, [nome], você entra…` vira `Até lá, você entra…`. Antes de pôr o nome entre vírgulas no meio da frase, leia a frase sem ele. `O boleto parcelado, [nome], vale…` viraria `O boleto parcelado, vale…`; aí o nome vai no fim (`…para quem ainda não é, [nome].`) ou abre a frase.

**Molde (Fonte C1, par assunto+preview):**

> **Assunto:** [o fato do encerramento, sem adjetivo]
> **Preview text:** [o que muda pra quem aprende pelo critério de quem avalia]

**Molde (Fonte C2, banco de ângulos pro mesmo e-mail de fechamento):**

> Pergunta direta: [pergunta sobre tentar de novo sem ajuda]
> Identidade/virada: [o que a pessoa deixou de ser] + [pergunta sobre o que vem agora]
> Consequência: [o que muda depois do prazo]

### 3.2 Abertura — *PADRÃO CONSISTENTE*

**O que entra:** a primeira linha carrega o ângulo do dia. Carrinho fechando abre pela urgência ou por uma virada; captação abre por benefício ou dor.

**Por quê:** define o contrato de leitura já na primeira linha e evita que dois e-mails da mesma sequência soem iguais.

**Variações aceitáveis:** urgência [quanto falta], empatia [frase curta que diz que o expert ouviu a objeção], continuidade [retoma o que viveram juntos no evento].

**Molde (Fonte B, boleto, abertura por empatia):**

> [Frase curta que diz que o expert ouviu a objeção.]

**Molde (Fonte C2, 20h, abertura por urgência seca):**

> [Saudação com o nome.]
> [Quanto falta, numa frase.]

### 3.3 Corpo / oferta — *PADRÃO CONSISTENTE*

**O que entra:** o argumento do dia + a oferta (entregáveis, acesso, garantia, bônus). No carrinho fechando o corpo é enxuto e não repete tudo; no carrinho aberto ele empilha a oferta completa.

**Por quê:** é onde o lead entende o que ganha e por que agora. Um argumento forte por e-mail converte mais que muitos argumentos empilhados.

**Variações aceitáveis:** lista de entregáveis com check/emoji, ou argumento corrido sem lista. Prova social só em texto e só se for real (nome de aluno verdadeiro), nunca print (imagem pesa na entrega).

**Molde (Fonte C1, corpo com entregáveis):**

> [Frase que liga o argumento do dia ao curso, pelo nome, e puxa a lista.]
> ✓ [o que o curso tem, com quantidade]
> ✓ [o prazo de acesso]
> ✓ [o prazo de garantia]
> 🎁 [bônus 1, pelo nome]
> 🎁 [bônus 2, pelo nome]
> [O preço, parcelado e à vista.]

**Molde (Fonte C2, corpo por decisão, sem repetir a oferta):**

> [Frase que avisa que a oferta não vai ser repetida.] [Frase que lembra o que a pessoa já sabe sobre o método.] [Frase que diz que o que falta agora é decidir.]

### 3.4 Âncora de urgência real — *PADRÃO CONSISTENTE na fase de fechamento*

**O que entra:** o prazo verdadeiro. Meia-noite, "a turma fecha", "só até hoje". Fato operacional, não escassez inventada.

**Por quê:** a urgência é o motor do e-mail de fechamento, mas só sustenta se for real. Se a turma reabre logo ou vira evergreen, a linha vira urgência fabricada e tem que suavizar.

**Variações aceitáveis:** encerramento à meia-noite, último dia, quanto falta. A regra que acompanha: se o cenário de reabertura muda, o texto muda ([diz que não há data pra próxima turma]).

**Molde (Fonte C2, âncora de fechamento):**

> [Quando as inscrições encerram e a turma fecha.] [O que continua existindo depois disso e o que deixa de existir.]

### 3.5 CTA único — *PADRÃO CONSISTENTE*

**O que entra:** um botão nomeado, com verbo de ação. Um link só no e-mail inteiro.

**Por quê:** link repetido em botão e texto sobe risco de entrega e dilui o clique. Um CTA mantém o trilho.

**Variações aceitáveis:** [BOTÃO: a ação de se inscrever, na 1ª pessoa], [BOTÃO: a ação de entrar no programa, na 1ª pessoa], [BOTÃO: ver como funciona]. O texto do CTA pode se repetir entre e-mails de propósito, desde que corpo e ângulo mudem.

**Molde (Fonte C1):**

> [BOTÃO: a ação de se inscrever, na 1ª pessoa]

### 3.6 Fecho — P.S. + pedido de resposta + assinatura — *PADRÃO CONSISTENTE no ciclo recente; parcial antes*

**O que entra:** assinatura do expert ([a despedida que ele usa] + [nome do expert]), muitas vezes um P.S. com um empurrão ou um vídeo do grupo, e um pedido de resposta.

**Por quê:** o pedido de resposta é o sinal de engajamento que mais protege a entrega, e ainda resgata quem está a uma dúvida de comprar. O P.S. é lido mesmo por quem pula o corpo.

**Variações aceitáveis:** P.S. que aponta um vídeo curto no grupo, P.S. de custo de inação, ou pedido de resposta direto no corpo.

**Molde (Fonte C1, pedido de resposta):**

> [Pergunta direta sobre o tema do curso.] [Convite pra responder o e-mail, dizendo que o expert lê.]

**Molde (Fonte B, P.S. por custo de inação):**

> P.S.: [Quanto custa adiar, comparado ao investimento.] [O que a pessoa perde a cada tentativa sem o resultado.]

## 4. Regras transversais

**Entregabilidade (o coração do framework).** *PADRÃO CONSISTENTE a partir do ciclo recente.* Regras enunciadas de forma explícita na Fonte C:

- **Sem número de dinheiro no assunto ou no preview.** Número de dinheiro (o cifrão, "12x", o valor da parcela) é gatilho forte. Quem clica vê o preço na página, que é onde ele converte de verdade. O preço fica só no corpo.
- **Um único link por e-mail.** "Nada de link repetido em botão e texto. O guia pede no máximo 1 a 2; fico em 1."
- **Assunto com a primeira letra maiúscula, sem palavra em caixa alta, sem "!", sem cifrão, sem "última chance".** Antes o assunto saía todo em minúscula; o Rodrigo trocou ("Tem que alterar isso aí nos disparos"), e no caso de origem uma checagem em código barra assunto que começa com minúscula.
- **Pedido de resposta**, o sinal de engajamento que mais protege a entrega.

**Atenção, evolução real:** essas regras **só valem a partir do ciclo recente**. Os e-mails do ciclo antigo (Fontes A e B) quebram quase todas: assunto com "!" e caixa alta, "última chance" no assunto, escassez de vaga no corpo. Aplique a régua de entregabilidade por herança do ciclo recente, sabendo que o corpus antigo não a seguia.

**Emoji/lista de ícones.** *PADRÃO INCONCLUSIVO.* A regra da casa diz "sem lista de emoji", mas os entregáveis aparecem com check/gift emoji mesmo no ciclo recente (✓/✅/🎁). Ou seja, a proibição não está cumprida no material produzido. Estado real: lista de entregáveis com check leve é tolerada; enfileirar emoji decorativo, não.

**Tom.** Voz do expert do caso-base: honesta, direta, calorosa e firme. A assinatura do tom no fechamento é [abrir o jogo com a pessoa] e [dizer que o que falta é decidir, não saber mais].

**Tamanho.** Curto no fechamento, um pouco mais longo no carrinho aberto (oferta completa). Ninguém empilha argumento.

**O que nunca aparece (a partir do ciclo recente):** escassez fabricada, "última chance", preço no assunto, mais de um link, print de depoimento (imagem pesa na entrega; prova social vai em texto e só se real).

**Processo de produção (regra do Rodrigo, registrada).** Os e-mails de fechamento nasceram como **versão-e-mail das mensagens que o Rodrigo já tinha fechado** no grupo, não de rascunho novo do zero. Instrução literal dele: "Escreva baseado nas minhas mensagens. Não nas que você criou." Cada e-mail vira a versão-e-mail do arco daquele dia.

### 4.1 Como o e-mail sai: do documento aprovado, em dois passos, do mais quente pro menos — *decisão do Rodrigo; como padrão, VARIAÇÃO ISOLADA (1 cliente)*

Vale junto com `sirius-scale/REGRAS.md` §6: pedido escrito de quem decide e texto final aprovado. O checklist antes de programar e a mecânica no Full Funnels estão em `sirius-scale/frameworks/automacao/fullfunnels-highlevel.md` §4.1.

1. **E-mail só sai de documento.** Nas palavras do Rodrigo: "Primeiro tem que ser feito, escrito, na verdade, no Google Docs e colocado na pasta certa, no Drive, com a nomenclatura certa." O texto que sai é o do documento aprovado, lido na hora de programar: nada de texto colado no pedido nem montado na conversa. O nome segue `EMAIL NN - ASSUNTO - TAG` (`sirius-scale/frameworks/operacao/nomenclatura-drive.md` §2). Documento fora da pasta do lançamento ou com pendência marcada (`[[CONFIRMAR…]]`, `[LINK…]`) não sai. Documento ainda em revisão só sai se quem decide mandar, por escrito.
2. **Escrever e agendar são dois passos**, em duas tarefas. A primeira entrega o documento pra revisão. A segunda espera a primeira, só roda depois do aprovado e manda um teste do mesmo texto pra uma caixa da equipe antes de agendar.
3. **Todo envio sai do mais quente pro menos**, em ondas de 30 minutos, uma por camada: quem clicou em e-mail, quem abriu, e o resto. Nas palavras do Rodrigo: "todos disparos devem ir segmentados do mais quente para o menos". A base é o corte do §6.2 (quem abriu o anterior abriu 19,0%; quem não abriu, 0,4%). Leia o resultado de cada onda separado. As etiquetas de quem abriu e de quem clicou têm que estar em dia antes do envio. Lista nova quase não tem histórico (numa lista de inscritos da Black, só 1,4% tinha a etiqueta), e a primeira onda cresce conforme os envios.

## 5. Moldes consolidados do caso-base, por fase

Os moldes abaixo mantêm a ordem e o tamanho das peças reais. Frase de e-mail enviado não vem literal: o colchete diz o que cada linha faz, e o texto sai na voz do expert de vocês.

**Fase 1 — Captação (Fonte A), os títulos dos dois e-mails de convite, por ângulo:**

> E-mail 1 — A: [acesso gratuito] + [a promessa e o prazo]
> E-mail 1 — B: [o primeiro nome] + [uma vaga guardada pra pessoa] + ([o evento e o assunto])
> E-mail 1 — C (reenvio): [última chance] + [a vaga ainda reservada]
> E-mail 2 — A: [pergunta sobre seguir preso à dor]
> E-mail 2 — B: [o método que leva ao resultado no prazo] + ([acesso liberado])
> E-mail 2 — C: [o primeiro nome] + [o que pode mudar o resultado] + [nota de que a pessoa não abriu o anterior]

(Nota: esses títulos são do ciclo antigo e usam escassez e "!" que a régua do ciclo recente proíbe. Ficam como registro da evolução.)

**Fase 2 — Boas-vindas (Fonte A), e-mail de reforço com linha de escape:**

> [Frase que lembra que ainda faltam passos.]
> ⬜ **[Passo 1: entrar no grupo]**
> [Por que o grupo importa: o que sai só por ali.]
> 👉 **[botão do passo 1]**
> [LINK DO GRUPO]
> ⬜ **[Passo 2: responder a pesquisa e pegar o presente]**
> [Quanto tempo leva e o que a pessoa ganha.]
> 👉 **[botão do passo 2]**
> [LINK DO FORMULÁRIO]
> [Linha de escape: quem já fez os dois pode ignorar o e-mail.]
> [Despedida curta, com o convite pro grupo.]
> [Assinatura do expert.]

**Fase 3 — Carrinho aberto (Fonte B), abertura do e-mail de inscrições abertas:**

> [Frase que anuncia que as inscrições abriram.]
> [Frase que abre o jogo com a pessoa.]
> [Recapitula a semana: o que ela viu, o que entendeu da tese e que o resultado é possível no prazo.]
> [Um caso real, com o resultado concreto.]
> [Outro caso real, com o antes e o depois.]
> [A soma dos alunos com o resultado.]
> [Frase curta de identificação.]

**Fase 4 — Carrinho fechando (Fonte C1, o curso menor), e-mail de quinta:**

> **Assunto:** [o mecanismo do evento também vale no tema do curso]
> **Preview text:** [um vídeo gravado pra quem esteve no evento]
>
> [Saudação com o nome.]
> [Retoma o que o expert mostrou no evento: o mecanismo e como ele aparece na avaliação.]
> [Liga esse mecanismo ao tema do curso e mostra a vantagem de quem enxerga isso.]
> [Frase que liga o argumento do dia ao curso, pelo nome, e puxa a lista.]
> ✓ [o que o curso tem, com quantidade]
> ✓ [o prazo de acesso]
> ✓ [o prazo de garantia]
> 🎁 [bônus 1, pelo nome]
> 🎁 [bônus 2, pelo nome]
> [O preço, parcelado e à vista.]
> [BOTÃO: a ação de se inscrever, na 1ª pessoa]
> [Até quando as inscrições ficam abertas.]
> [Despedida + assinatura do expert.]
> **P.S.** [Aponta o vídeo curto no grupo, com o porquê de o tema pesar, e diz que é rápido de ver.]

**Fase 4 — Carrinho fechando (Fonte C1), e-mail de sexta, mostrando ângulo distinto do de quinta:**

> **Assunto:** [o fato do encerramento, sem adjetivo]
> **Preview text:** [o que muda pra quem aprende pelo critério de quem avalia]
>
> [Saudação com o nome.]
> [Último dia e a hora em que fecha.]
> [O que muda pra quem aprende pelo critério de quem avalia, e o custo de fazer sem saber.]
> [O que os módulos mostram, ligado ao resultado.]
> [O preço parcelado, ligado à segurança que a pessoa ganha e à dor que some.]
> [Puxa o resto da lista.]
> ✅ [o prazo de acesso]
> ✅ [o prazo de garantia]
> 🎁 [os dois bônus, pelo nome]
> [BOTÃO: a ação de se inscrever, na 1ª pessoa]
> [Fecha com o prazo e o convite pra entrar agora.]

**Fase 4 — Carrinho fechando (Fonte C2, a turma do programa principal), e-mail das 20h por consequência:**

> **Assunto:** [o que muda depois do prazo]
> **Preview text:** [quanto falta] + [o expert não quer a pessoa de fora]
>
> [Saudação com o nome.]
> [Quanto falta, numa frase.]
> [Quando as inscrições encerram e a turma fecha.] [O que continua existindo depois disso e o que deixa de existir.]
> [Frase que avisa que a oferta não vai ser repetida.] [Frase que lembra o que a pessoa já sabe sobre o método.] [Frase que diz que o que falta agora é decidir.]
> [O pedido do dia: decidir, e entrar enquanto há tempo.]
> [BOTÃO: a ação de entrar no programa, na 1ª pessoa]

## 6. O que é reutilizável e o que é do caso

**Reutilizável em qualquer cliente/lançamento:**

- A divisão por fase (captação, boas-vindas, carrinho aberto, carrinho fechando) e o esqueleto de cada uma.
- A anatomia do e-mail: par assunto+preview que não repete, um ângulo por e-mail, corpo com um argumento forte, âncora real, CTA único, fecho com pedido de resposta.
- A régua de entregabilidade inteira (sem dinheiro no assunto, um link, primeira letra maiúscula sem palavra em caixa alta, sem "!", pedido de resposta).
- O banco de ângulos de assunto (pergunta, identidade, consequência, curiosidade, sóbrio) pra não repetir fórmula em disparos do mesmo dia.
- O processo de derivar o e-mail da mensagem já validada em outro canal.

**Do caso (o caso-base e o nicho dele):**

- A Roma do caso-base e o inimigo que o expert dele combate.
- A credencial do expert do caso-base como argumento de autoridade.
- Os produtos, os preços e os bônus nomeados.
- As dores que são da linguagem do avatar daquele curso.

## 6.1 Trial de SaaS: o gatilho do e-mail e o relógio da oferta podem ser eventos diferentes — *VARIAÇÃO ISOLADA (1 fluxo, 1 cliente, ainda não medido)*

> Nasceu no fluxo de um SaaS de outra empresa do Rodrigo, o primeiro uso deste arquivo fora
> do caso-base e fora de lançamento. Não contradiz nada aqui: em lançamento o carrinho fecha na
> mesma hora pra todo mundo, então o caso nunca apareceu.

Em lançamento, quem entra na sequência e quem chega no fechamento vivem o mesmo calendário.
Em **trial**, não: o relógio da oferta começa no **cadastro**, e a sequência costuma disparar
num evento posterior (terminar o onboarding, criar a primeira coisa, fazer a primeira ação).
Quem demora três dias pra configurar tem quatro dias de teste, não sete.

**O erro que isso produz**, se a cadência for contada a partir do gatilho: os últimos e-mails
caem **depois** do prazo acabar. O e-mail de "último dia" chega quando a conta já travou, e o
de boas-vindas promete um "amanhã" que não existe.

**A régua:**

1. **Conte de trás pra frente**, a partir do fim do prazo, não do gatilho.
2. **Os e-mails do meio ganham condição de tempo restante** ("só dispara se ainda faltam N
   dias"). Quem entrou tarde pula e cai direto nos que decidem.
3. **Os e-mails de decisão acontecem sempre**, ancorados no fim ("faltam dois dias", "é o
   último dia"), nunca no número do dia.
4. **O primeiro e-mail não promete o dia seguinte**: ele pode estar sendo lido por quem
   entrou no último dia.
5. **Quem entra com zero tempo útil não recebe a sequência**, só o e-mail do fim. Mandar
   "está tudo pronto, agora acompanhe" pra quem tem algumas horas é pior que não mandar.

⚠️ **Pré-requisito técnico que costuma faltar:** a data de fim do prazo precisa existir como
**campo de data** na ferramenta, não como texto. No caso de origem, o campo `Iniciou Trial`
estava gravado como texto, e campo de texto não serve pra calcular espera.

---

## 6.2 O que a primeira medição mostrou

Fonte: uma análise de abertura e clique do caso-base, feita durante a captação de uma Black. Base: 105 campanhas da ferramenta de e-mail anterior (cerca de dez meses) e cerca de 66 mil e-mails da ferramenta atual, na captação.

- **O público decide a abertura, o assunto quase não.** *VARIAÇÃO ISOLADA (1 cliente; 13 pares no mesmo lançamento, o que pode subir a CONSISTENTE com o ok do Rodrigo).* Mesmo e-mail, mesmo assunto, 15 min de diferença: quem abriu o anterior abriu 19,0%, quem não abriu, 0,4%. Com o público controlado, nenhum tipo de assunto passou de 1 ponto com N suficiente, e manhã ficou de 0,1 a 1,3 ponto acima da noite.
- **Comprador abre e clica mais que a base.** *VARIAÇÃO ISOLADA.* Compradores/alunos: 8,7% de abertura e 1,73% de clique (N=17); base inteira, nos dois meses anteriores à Black: 2,2% e 0,33% (N=9).
- **Reenvio pra quem não abriu, com o assunto B, recupera.** *VARIAÇÃO ISOLADA.* Mediana de 9,3% (N=6) na ferramenta anterior; 7,0% de abertura e 2,4% de clique num reenvio da Black.
- **E-mail sem link não gera clique, e teaser costuma vir sem link.** *PADRÃO INCONCLUSIVO* (o efeito na entrega não está medido). Os três e-mails de antecipação da Black (94% do volume do período) não tinham botão: clique zero por desenho. Regra: todo e-mail leva um botão ou um pedido de resposta.
- **Dois e-mails pra mesma lista no mesmo dia derrubaram a abertura.** *PADRÃO INCONCLUSIVO* (confundido com o volume alto num domínio sem histórico): 7,7% no primeiro e-mail de antecipação, 3,2% e 3,8% nos dois que saíram juntos, dois dias depois.
- A régua de entregabilidade da §4 continua valendo; o que mais pesou na entrega, nessa análise, foi o Gmail, a base fria e o remetente novo. Como ler a estatística e conferir o domínio de envio: `sirius-scale/frameworks/automacao/fullfunnels-highlevel.md` §4.2 e §4.3.
- **Bônus por ordem de chegada: o e-mail com o link sai no fim da contagem regressiva da live, não antes.** *VARIAÇÃO ISOLADA (revisão de uma Black do caso-base, ainda não enviada).* Se o e-mail chega antes do link da live, quem lê compra antes de quem assiste e a contagem dos primeiros (um bônus pros N primeiros, por exemplo) não fecha.
- **Prazo de bônus no e-mail vai com dia da semana e data** ("até [hora] de [dia da semana], [dia] de [mês]"), nunca só "hoje" ou "amanhã": e-mail é lido com atraso. *VARIAÇÃO ISOLADA (mesma revisão).*
- **Segundo e-mail de uma sequência espera até as 9h do dia seguinte**, em vez de sair no mesmo horário da inscrição. *VARIAÇÃO ISOLADA (regra do Rodrigo, 11/2026, ainda sem medição).* Quem se inscreve à 1h da manhã receberia o e-mail 2 à 1h da manhã. No fluxo, é uma espera "até a janela das 9h" depois do primeiro e-mail (como montar no Full Funnels: `automacao/fullfunnels-highlevel.md`, "Montagem do fluxo pela tela"). Alcance `NÃO TESTADO FORA`.

## 7. Pontos em aberto

- **Métrica por e-mail: começou** (§6.2). Ainda não dá pra dizer qual ângulo converte mais: nenhum envio da Black levou UTM automática, então não há venda por e-mail. O banco de ângulos continua hipótese testável.
- **Régua de entregabilidade: PADRÃO CONSISTENTE só no ciclo recente.** Um lançamento novo já sob a régua confirma se ela pegou de vez no fluxo inteiro (captação e boas-vindas ainda não passaram por ela).
- **Captação, boas-vindas e carrinho aberto: 1 lançamento cada.** Base fina. Precisa de mais um lançamento pra virar padrão consistente por fase.
- **Carta de vendas longa por e-mail:** citada como estratégia, nunca produzida no projeto. Fica como lacuna.
- **Duas ofertas na Fonte C.** O material de fechamento cobre a turma do programa principal e um curso menor. Os padrões batem entre os dois, mas ainda é um único ciclo de lançamento; generalizar pra qualquer oferta segue inconclusivo.
- **"Sem lista de emoji": não cumprido.** A regra da casa e a prática divergem. No caso de origem, decidir qual vence é do Rodrigo; no negócio de vocês, de quem aprova a copy, antes de cravar no framework (`frameworks-da-casa/`).
