# Checklist — Tráfego (campanha, conjunto, anúncio, análise)

## Leia antes de abrir o entregável

Antes de tudo, `frameworks-da-casa/`: o que vocês já corrigiram em tráfego vale mais que
o resto (`sirius-scale/REGRAS.md` §4).

1. `sirius-scale/frameworks/trafego/_metodologia.md` — regras de leitura e a régua de otimização
2. `sirius-scale/frameworks/trafego/nomenclatura.md` — padrão de nome e ID de criativo
3. `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` — o que MQL sustenta e o que não
4. `lancamentos/<AAAA-MM-nome>/briefing.md` — **inteiro**, com atenção à meta, à verba e
   às diretrizes de tráfego, e às ressalvas (no template de
   `sirius-scale/frameworks/lancamentos/briefing.md`, os blocos `metas` e `trafego`).
   Perpétuo: `funis/<nome>/briefing.md` e `funis/<nome>/desempenho.md`
5. `sirius-scale/REGRAS.md` §6 — se o entregável criou, ativou ou editou algo na
   plataforma
6. `sirius-scale/frameworks/trafego/lancamento-gratuito.md` — só se for lançamento gratuito
7. `sirius-scale/frameworks/trafego/publicos-e-advantage.md` — se houver segmentação nova
8. `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md` e
   `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` — o da plataforma que foi
   tocada, **sempre**. Não é só lista de armadilha: é a receita de como se cria certo, ou
   seja, o que o objeto revisado deveria ter.
9. `sirius-scale/frameworks/trafego/leitura-dash-facil.md` — se a revisão encosta em
   qualquer número de Dash. Os denominadores da §2.1.1 (CPA e taxa de pesquisa sobre
   leads **PAGOS**, faixa A/B sobre quem **TEM** faixa) são o que faz o número bater com
   a tela. Usar a base toda erra os três, e sempre pro lado bonito.
10. `sirius-scale/frameworks/trafego/otimizacao-em-tres-niveis.md` — se o entregável é uma
    rodada de otimização, ou mexeu em verba, público ou criativo de campanha rodando

📌 **Cada letra abaixo tem "Aplica quando".** Antes de montar o prompt do
subagente (`SKILL.md` Passo 2), confira o inventário e ative só as letras cujo
gatilho apareceu. Letra sem gatilho no inventário não entra no prompt — nem o
framework que ela citaria é lido. G, H e I já se auto-escopam pelo próprio título.

---

## A. Nomenclatura

**Aplica quando:** campanha, conjunto ou anúncio novo/renomeado apareceu no
inventário. Sem objeto novo ou renomeado, não há nome pra conferir — pula.

- [ ] **Estrutura por nível** bate com `nomenclatura.md` §1 — campanha, conjunto
      (`00 - [PÚBLICO] detalhe`) e anúncio (`AD - TIPO NN - SLUG`).
- [ ] **Vocabulário fixo** (§2): TIPO, FASE, ETAPA, PÚBLICO só com os valores das
      tabelas. Sigla inventada é achado, mesmo que faça sentido.
- [ ] **Bloco CANAL** presente no Google, ausente na Meta.
- [ ] **Sem acento e sem barra** dentro dos colchetes e no slug. `CAPTACAO`, nunca
      `CAPTAÇÃO`. Confira caractere a caractere — é o erro que mais passa.
- [ ] **Uma tag por lançamento**, sempre a mesma. Duas tags pro mesmo lançamento na
      mesma leva já aconteceu no caso de origem.
- [ ] **ID do criativo (VDNN)**: série contínua por negócio, número nunca
      reciclado, regravação vira `.1` e não número novo, ID não carrega lançamento
      nem plataforma.
- [ ] **O mesmo NN em três lugares**: documento de copy, nome do anúncio e
      `utm_term`. Divergência aqui quebra o cruzamento de venda no debriefing.
- [ ] Variação numérica (teste 2, teste 3) no fim do nome, fora dos colchetes.

## B. O que está sendo medido (a regra que já mordeu duas vezes)

**Aplica quando:** campanha ou conjunto novo, ou objetivo/ação de conversão foi
tocado no inventário.

- [ ] **Ação de conversão real confirmada na plataforma**, não inferida do nome nem
      do objetivo do nível de cima. Meta: `promoted_object.custom_event_type`.
      Google: `segments.conversion_action_name` + `conversion_action_category`.
- [ ] O **nome bate com o que a campanha de fato mede**. Se não bate (erro
      herdado tipo `[INSCRIÇÃO]` que rastreia compra), a divergência foi
      declarada — não corrigida caladamente nem ignorada.
- [ ] **Nenhuma soma de conversões de objetivos diferentes** num total só. Compra
      e inscrito de canal no mesmo número já deu 10x de diferença.

## C. Verba e metas

**Aplica quando:** orçamento diário mudou, ou houve realocação/criação de conjunto
com orçamento.

- [ ] Orçamento por conjunto **bate com o briefing** (verba e distribuição
      aprovadas). Campo vazio no briefing = ninguém decidiu, não é pra preencher.
- [ ] Soma dos orçamentos = verba aprovada. Confira a soma na mão.
- [ ] Performance comparada contra a meta do briefing — nunca contra benchmark
      de fora nem meta inventada.
- [ ] Se houve **realocação de verba**: seguiu a escada de `_metodologia.md`
      §3.1.1 (degrau de +30% pra cima, corte com **piso**, não proporcional), e
      respeitou "pausar não é o padrão".
- [ ] Conjunto em `LEARNING` não levou corte.
- [ ] Aumento acima de +30% não foi aplicado sem justificativa (reseta aprendizado
      do Advantage+).

## D. Decisão por custo por MQL

**Aplica quando:** a mudança de verba (letra C) veio de uma decisão de
performance — não de ajuste manual sem análise por trás.

- [ ] A decisão de verba usou **custo por MQL / lead score**, não o CPL do
      gerenciador sozinho.
- [ ] Taxa de MQL projetada pro total foi **declarada como projeção** (é sobre
      quem respondeu a pesquisa, não sobre a base).
- [ ] **Volume suficiente** antes de agir. Poucas dezenas de leads não decidem
      nada; diferença pequena com base fina = observar, não cortar.
- [ ] Se comparou criativo entre plataformas: usou **UTM CAMPAIGN ou CONTENT**, não
      UTM TERM (que soma Meta + Google quando o nome do anúncio se repete,
      `_metodologia.md` §3.2).
- [ ] Ranquear criativo por MQL só afirmou qualidade se passou no teste z.
- [ ] O dado do Dash é **de hoje** (lido pelo conector ou export do dia) — ou a idade
      dele foi avisada.

## E. Segmentação e fase

**Aplica quando:** público novo, edição de segmentação, ou interruptor de
expansão/segmentação otimizada apareceu no inventário.

- [ ] Cada público rastreia a uma diretriz de tráfego do briefing ou a um dado real
      de pesquisa/avatar. Público "que faz sentido" sem fonte é achado.
- [ ] Se contraria uma diretriz do briefing, isso foi **dito na cara**, com o
      motivo — não feito calado.
- [ ] As ressalvas do briefing foram lidas antes de usar os números dele.
- [ ] Fase e etapa coerentes com o momento real do lançamento.
- [ ] **Geo conferido de verdade**, não presumido. Grupo de anúncios sem critério de
      localização entrega no mundo inteiro e não avisa ninguém — no caso de origem,
      uma campanha subiu assim e gastou 83% do dia fora do Brasil
      (`google-criacao-tecnica.md` §6/§7).
- [ ] **Expansão de público / segmentação otimizada desligada em fase de
      remarketing.** Ligada, ela fura o público de retargeting. Na Meta são dois
      interruptores (`publicos-e-advantage.md` §4.3). Confira o estado real na
      plataforma, não o que se pretendia fazer.
- [ ] **Idade conferida na plataforma (Meta).** A idade mínima é controle (a
      plataforma respeita) e bate com o briefing. A faixa etária é sugestão: com o
      Advantage+ ligado, a Meta entrega fora dela (`publicos-e-advantage.md` §1). Se o
      briefing trata a faixa como limite e o Advantage+ está ligado, isso foi dito na
      entrega.
- [ ] **Nutrição não está rodando junto da captação** (briga com o aquecimento).

## F. UTM e rastreio

**Aplica quando:** anúncio novo, ou parâmetro de UTM foi editado.

- [ ] Mapa de UTM completo: source / medium / campaign / content / term por anúncio.
- [ ] `utm_term` = `VDNN-SLUG`, sem acento, sem barra, caixa alta.
- [ ] `utm_campaign` carrega tag de plataforma, pra não colidir entre Meta e Google
      no Dash.
- [ ] UTM bate com o nome real do objeto na plataforma.

## G. Segurança (se montou, subiu ou vai subir algo)

Regra de origem: `sirius-scale/REGRAS.md` §6. A única escrita do Claude é montar, sempre
pausado: na Meta pelo conector oficial, no Google pelas ferramentas do sistema. Sem as
ferramentas ligadas, o Google chega só pelo Dash e quem sobe são vocês. Ativar, pausar o que
está rodando e mexer em orçamento ou lance é com vocês, na plataforma.

- [ ] Tudo nasceu **PAUSED**.
- [ ] Se foi montado pelo Claude (conector da Meta ou ferramentas do Google): teve o
      pedido escrito de quem decide e o pacote aprovado, e a soma do orçamento ficou
      dentro do teto combinado antes (lida da plataforma, no escopo do teto, nunca de
      cabeça). No Google, a prévia foi mostrada antes de escrever.
- [ ] Ativação foi ação separada da criação, feita por vocês na plataforma, depois de
      ver o resumo **lido da conta** (não o que se pretendia criar). Ativação, pausa
      de algo rodando ou mudança de orçamento ou lance feita pelo Claude é 🔴, mesmo
      com pedido.
- [ ] Nenhum objeto ficou ativo sem alguém ter visto o orçamento diário que ia rodar.
- [ ] **Campanha nova do Google, montada pelo Claude ou subida por vocês, passou pela
      conferência antes de ativar** de
      `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §32 (itens 1 a 11),
      contra uma campanha de referência que funciona, da mesma fase e etapa, com a
      config lida da plataforma. Diferença fora do que a fase explica = não ativa.
      Subiu sem conferir é 🔴, mesmo que esteja rodando bem agora.
- [ ] A `/preflight` (`.claude/skills/preflight/SKILL.md`, Passo 0 da revisão) rodou e o
      que ela acusou está na entrega, na seção Saúde da conta. Conjunto novo passou pelo
      preflight do pacote (país, Advantage, idade) do agente `gestor-trafego` antes de
      ativar.
- [ ] Se foi montado pelo Claude: o que foi escrito foi **lido de volta** da plataforma.
      Na Meta, com uma linha por conjunto (nome, status PAUSADO, orçamento, idade mínima
      e faixa, país, Advantage e "usar como sugestão" ligados ou não, quantos públicos
      inclui e exclui). Escrita só conta com leitura de volta.

## H. Armadilhas de contexto (checar antes de reportar como erro)

Estas coisas **parecem** erro e normalmente não são. Confira o histórico antes de
transformar em achado:

- **Criativo `PAUSED` na Meta** costuma ser fila de troca de propósito, não corte.
- **Campanhas de teste, pré-escala e escala rodando juntas** é o desenho correto,
  não duplicação.
- **Campanha ou anúncio criado antes de vocês adotarem a nomenclatura atual** segue o
  padrão antigo de nome (anúncio antigo, por exemplo, sem slug de ângulo: `AD - VD 01`)
  — não é violação da nomenclatura nova.
- **Nunca sugerir pausar campanha por padrão estrutural** (nome repetido, criativo
  parecido). Só custo por MQL real decide.

## I. Se o entregável for uma análise (não uma campanha)

- [ ] Segmentou por ação de conversão real **antes** de agregar qualquer coisa.
- [ ] Toda aproximação, mapeamento ou suposição está **declarada no resultado**.
- [ ] Período correto: lançamento por edição; LPSG (lançamento pago semanal gravado,
      `sirius-scale/frameworks/lancamentos/lpsg.md`) de segunda 00:00 a domingo 23:59
      (não "últimos 7 dias").
- [ ] Nenhum número aparece como exato quando foi inferido.
- [ ] Foi salva em `entregas/analises/<lançamento-ou-funil>-<tema>-<AAAA-MM-DD>.md`,
      com a data da análise no cabeçalho e o período coberto.

## J. Otimização em três níveis

**Aplica quando:** o entregável é uma rodada de otimização ou mexeu em verba, público ou
criativo de campanha rodando. Regra de
`sirius-scale/frameworks/trafego/otimizacao-em-tres-niveis.md`, que vale pra qualquer
campanha: muda a régua de cada nível (CPL, custo por MQL, ROI), não os três níveis. Os
limiares e números de lá são de um lançamento só e, aplicados aqui, vêm ditos como
vindos de outro negócio.

- [ ] **Os três níveis foram olhados, nessa ordem de leitura:** orçamento (tira do caro,
      põe no barato, dentro da faixa da fase), público (testa o que não rodou, junta,
      abre) e criativo (desliga o caro, liga o que não rodou). Rodada que só mexeu em
      verba, sem dizer nada de público e de criativo, é achado.
- [ ] **Público cansado: criativo antes de verba.** Num conjunto saturado, a subida de
      verba ficou segurada enquanto a troca de criativo estava em curso. Frequência é a
      do gerenciador.
- [ ] **Ligar não é testar.** Em conjunto com vários anúncios, a fatia de gasto de cada
      criativo foi olhada (criativo que entrou tarde se mede a partir do primeiro dia
      com gasto). Criativo ligado que quase não levou verba aparece como "sem verba",
      nunca como "observar" nem como perdedor, e o que se propõe é teste com verba
      própria, montado pausado: na Meta, um conjunto por criativo com o mesmo público;
      no Google, uma campanha por criativo, porque o Demand Gen não tem orçamento por
      grupo.
- [ ] **Teste lido direito.** Célula que gastou menos de 70% do orçamento fica "não
      testada", nunca perdedora.
- [ ] **A troca não tirou quem não foi visto.** Só sai criativo que já levou uma fatia
      real do gasto do conjunto. E ligar tem custo: na Meta, anúncio novo num conjunto
      faz ele voltar pro aprendizado, então a proposta liga no máximo um por conjunto
      por dia.
- [ ] **Sugestão de público só com gatilho:** sobra de verba até o alvo ou público
      saturado. Sem nenhum dos dois, é ruído. A exclusão da família vem junto (aluno fora
      do não aluno, lead fora do envolvimento, inscrito da fase fora de tudo), e Advantage
      de público só em captação fria.
