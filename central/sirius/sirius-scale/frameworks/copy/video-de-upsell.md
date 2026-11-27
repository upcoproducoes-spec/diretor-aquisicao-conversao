# Framework — Vídeo de upsell (o vídeo da tela seguinte à compra)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método e execução de copy: o roteiro do vídeo de upsell pós-compra e a página que fica acima dele.
>
> **Base:** o prompt de sistema de vídeo de upsell que o Rodrigo trouxe e adotou como método da casa (origem externa:
> 7 princípios, 3 fases, 11 blocos, uma lista de erros, um diagnóstico da oferta, uma calibragem de tom e uma régua de
> taxa de aceite), mais os 3 roteiros que a casa escreveu com ele em 2 clientes, e 1 roteiro de fora do método, que é o
> único upsell da base que foi ao ar com número (§1).
>
> **Alcance: NÃO TESTADO FORA.** O método foi executado em dois clientes da casa, mas nenhum roteiro feito por ele tem
> resultado medido: é especificação, ainda sem número. Dois roteiros ficaram em roteiro; um foi gravado, editado e
> aprovado, sem publicação confirmada. O único upsell com número rodou um roteiro de fora do método, e ninguém sabe
> qual versão do vídeo estava no ar. Subir o alcance é decisão do Rodrigo, e só faz sentido depois da primeira medição.
>
> **Força:** nada aqui passa de VARIAÇÃO ISOLADA. Regra que veio só do prompt é especificação que o Rodrigo decidiu
> seguir e ainda não mediu: **PADRÃO INCONCLUSIVO**. Onde um roteiro aprovado da casa aplicou a regra, vai
> **VARIAÇÃO ISOLADA**, com a contagem. O framework irmão de upsell e downsell conta estes roteiros junto com os de
> downsell e com o funil medido, e dá força maior a algumas linhas, sempre como (proposto), que pelo
> `sirius-scale/REGRAS.md` §4 ainda é hipótese.
>
> **Quem é quem** (as mesmas letras de `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md`): A, B e C são três
> experts de infoproduto atendidos pela casa. O C tem duas frentes, **C1** e **C2**.
>
> **Onde mora o resto:**
> - A escada (o que vem depois do front e a que preço), o downsell, as páginas de backend e a medição por oferta:
>   `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md`.
> - Upsell de low ticket (o um clique barato, junto com order bump): `sirius-scale/frameworks/lancamentos/low-ticket.md`
>   §3.
> - A VSL do front, que vem antes e decide o que sobra pro upsell: `sirius-scale/frameworks/copy/producao-de-vsl.md`
>   (etapa 3, item 4).
> - A forma do documento (versão de leitura do expert, notas da equipe à parte):
>   `sirius-scale/frameworks/copy/formatacao-de-roteiro.md`.
> - Depoimento na fala: `sirius-scale/frameworks/oferta-14-secoes.md` §5.
> - Este arquivo trata do **vídeo de upsell**: o que ele diz, em que ordem, em quanto tempo, e o que se confere antes de
>   gravar e de publicar.

---

## 1. Escopo e base de evidência

### Fontes

- **Fonte P: o prompt.** Uma instrução de sistema pra colar numa IA, que o Rodrigo trouxe pra escrever os vídeos de
  upsell dos funis de VSL. Tem o comportamento esperado (4 regras), o princípio de não repetir a VSL, os 7 princípios,
  a Fase 1 (28 perguntas em 6 blocos), a Fase 2 (10 decisões), a Fase 3 (11 blocos com tempo, tom e cena), o anexo da
  página, a lista de 10 erros, os 5 checks da oferta, a calibragem de tom e uma régua de taxa de aceite. A nota da casa
  sobre ele dizia que ele só viraria framework depois da primeira copy medida. Este arquivo foi escrito antes dessa
  medição, a pedido do Rodrigo, pro método entrar no kit; quando houver número, o confronto muda as forças daqui.
- **C1, o upsell de degrau do expert C** (educação, nicho de preparação pra prova, perpétuo de VSL). Quem acabou de
  comprar o livro de entrada vê o curso gravado do expert, a 2 vezes o front e abaixo do preço cheio. Passou por:
  diagnóstico da oferta, as 28 respostas com fonte, as 10 decisões, revisão do coordenador (a sessão do Claude que
  organiza o trabalho e chama o `copy`), uma correção do Rodrigo, roteiro v1, `/revisar` (1 bloqueio, corrigido no
  mesmo dia, "pode gravar") e v2 no dia seguinte, porque uma decisão do Rodrigo derrubou uma âncora. Doc de gravação
  pronto. **Não gravado.**
- **C2, o upsell de complemento do expert C.** O mesmo funil tem uma segunda frente em que o curso é o front e o livro
  vira o upsell: o ticket desce (o upsell custa cerca de 30% do front). O coordenador decidiu a arquitetura antes de
  chamar o `copy`; Fases 1 e 2 compactas, uma linha por item; roteiro revisado pelo Rodrigo no mesmo dia (dois
  ajustes). Doc de gravação pronto. **Não gravado.**
- **A, o upsell do expert A** (curso técnico pra profissionais, perpétuo de VSL, vende em mais de um mercado; o vídeo
  foi preparado pra dois: o principal e um segundo mercado). Quem comprou o front (um material físico de apoio) vê o
  curso completo, a cerca de 2,4 vezes o front e menos da metade do preço cheio. Fases 2 e 3 entregues juntas; revisão com bloqueios (dois no upsell); um 2º passe trocou a
  tese; a peça virou gravação única com bloco de preço por mercado. **Gravado pelo expert, editado (4:50) e aprovado
  pelo gestor do projeto.** Publicação não confirmada.
- **B, contraponto: o upsell do expert B** (curso técnico pra profissionais; livro digital de entrada → curso online).
  Roteiro escrito fora deste método, com ordem própria em 11 partes, 6 a 8 minutos e 3 depoimentos. **É o único
  upsell da base que foi ao ar com número**, e não se sabe qual versão do vídeo rodou (§12).
- **Falas e decisões do Rodrigo** nos três funis e numa consultoria, citadas onde entram.

### Excluído de propósito

- O vídeo e a página do downsell, a escada e o preço relativo: estão em
  `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` (§4.1 a §4.7, §4.12 e §4.13).
- Order bump e upsell de low ticket: `sirius-scale/frameworks/lancamentos/low-ticket.md`.
- A live de downsell depois do carrinho de lançamento: outro artefato
  (`sirius-scale/frameworks/lancamentos/live-de-downsell.md`).
- O texto integral do prompt. Aqui ele vira método; a versão colável não faz parte deste kit.
- Os roteiros completos, as fichas de produto e os catálogos de depoimento dos casos: ficam no caso de origem.

### Ressalva estrutural

Três roteiros, dois clientes, o mesmo coordenador e o mesmo agente `copy`, num intervalo de duas semanas. Um bloco
que se repete nos três prova que o método foi seguido, não que ele converte. Só a medição por oferta (§12) diz isso.

### Status

| Roteiro | A escada | Estado | Número |
|---|---|---|---|
| C1 | livro de entrada → curso (sobe 2 vezes) | aprovado pra gravar; doc de gravação pronto | — |
| C2 | curso → livro (desce) | conferido e revisado pelo Rodrigo; doc de gravação pronto | — |
| A | material físico de entrada → curso (sobe cerca de 2,4 vezes) | gravado, editado (4:50), aprovado; publicação não confirmada | — (o número que existia antes era de outro vídeo e de outra base, §12) |
| B (fora do método) | livro digital → curso | no ar por cerca de quatro meses; versão do vídeo não confirmada | cerca de 7% na janela da compra, por oferta (§12) |

---

## 2. O que é o vídeo de upsell e onde entra no funil — VARIAÇÃO ISOLADA (3 de 3 roteiros, mais falas do Rodrigo)

**Onde.** É a tela seguinte ao pagamento do front, dentro da compra, com botão de um clique: a pessoa compra sem
digitar o cartão de novo. Quem recusa vai pro downsell, que o vídeo não anuncia; quem compra segue (pro 2º upsell,
onde houver, ou pro obrigado). Na Hotmart, o botão de um clique só existe dentro do processo de compra ativo: quem
fecha a página e abre o link de novo vê a página, sem o botão. É fato de plataforma, confirmado pelo Rodrigo no
funil do C; conferir na plataforma de vocês antes de escrever a escassez (§9.2, regra 1).

**Quem assiste.** O comprador, não o lead. Ele acabou de ver uma VSL inteira (de 25 a 32 minutos nos funis do A e do
C), decidiu e pagou. O prompt resume: upsell "não é venda comum", é um momento psicológico com tratamento próprio. A
leitura do estado dele mudou com o avatar: alívio com uma dúvida atrás, num público de renda apertada que já tinha
comprado material antes sem resolver (C, escrita como leitura e não como dado); decisão tomada e leve euforia, num
público com outro perfil de renda (A). O que se repetiu nos três roteiros: ele espera confirmação e acesso, não quer
outra VSL, não quer ouvir que a compra está incompleta, e é o momento em que ele mais confia no expert.

**O formato do upsell é diferente do front.** O livro sobe pro curso, o material físico sobe pro curso, o curso desce
pro livro. Rodrigo, numa consultoria: "Só que aqui, o importante é que o formato seja diferente do front." O porquê
está em `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.1.

**O vídeo.** O expert falando pra câmera, no mesmo estúdio e teleprompter da VSL (C1, C2), com inserções de tela. No A,
a direção pediu o contraste de "conversa, não apresentação": sem slide, sem lower third animado, sem trilha épica. Até
6 minutos (§7). Acima dele, uma página curta (§6).

**A ordem do trabalho.** A VSL é escrita primeiro, e o upsell depende do que ela gastou (C). Melhor ainda: separar,
antes de escrever as duas, o que a VSL usa e o que fica guardado pro upsell (A), como manda
`sirius-scale/frameworks/copy/producao-de-vsl.md` (etapa 3, item 4). No A a separação ficou no papel: o número de
autoridade guardado pro upsell já estava na VSL no ar.

**O princípio de tudo: não repetir a VSL.** O comprador já ouviu a história do expert, a autoridade, o mecanismo, as
dores e promessas, os depoimentos e a oferta do front. O prompt diz que repetir qualquer coisa disso "mata a conversão"
e que o upsell precisa de tese, autoridade, gancho e argumentos novos. O efeito na conversão é afirmação do prompt,
não medição (PADRÃO INCONCLUSIVO); a prática de mapear o que a VSL gastou e não repetir está nos 3 roteiros (§4.3,
item 2).

---

## 3. Os 7 princípios — PADRÃO INCONCLUSIVO como princípio (o prompt diz que vêm da análise de upsells que convertem bem; nada medido aqui); a aplicação, VARIAÇÃO ISOLADA na contagem de cada linha

| # | O princípio (prompt) | Como os roteiros aplicaram | Força |
|---|---|---|---|
| 1 | **Curiosidade antes de explicação.** O gancho abre um loop, a autoridade ancora, a tese desenvolve, o produto resolve. O produto não aparece antes da curiosidade. | Nome do produto só no bloco 4; loop aberto no bloco 1 e fechado no bloco 10 (3 de 3). No C2 o produto nem aparece de capa antes do bloco 4. | VARIAÇÃO ISOLADA |
| 2 | **Atribuição mononuclear.** A transformação reduzida a uma causa só, porque atalho vende mais que pacote. | 3 de 3, sem o percentual do modelo ("80% do meu resultado"), que não existia em arquivo. | VARIAÇÃO ISOLADA |
| 3 | **Duas âncoras antes do preço, uma externa e uma interna.** | A interna (o preço cheio fora desta compra) em 3 de 3; a externa em 0 de 3, com a falta declarada (§4.1). | VARIAÇÃO ISOLADA na versão da casa; a externa, INCONCLUSIVO |
| 4 | **Pergunta retórica de dor ativa:** fazer a pessoa buscar uma memória ruim específica ("quantas vezes você já..."). Sem dor ativa o produto vira luxo; com ela, vira saída. | 3 de 3, sempre com uma dor que a VSL não usou. | VARIAÇÃO ISOLADA |
| 5 | **Vender o estado depois da compra:** como o dia a dia muda. | Cena de uso no bloco 5 (3 de 3). Cena de transformação explícita só no A, e só depois que a revisão apontou a falta. | VARIAÇÃO ISOLADA (1 roteiro) |
| 6 | **Escassez real, dita 3 vezes** (esta página, este preço, esta janela). Nunca escassez falsa. | 3 menções em 3 de 3, todas da mesma verdade: o botão que só existe nesta compra e o preço de fora (§5.8). | VARIAÇÃO ISOLADA |
| 7 | **Tempo enxuto e ritmo agressivo:** no máximo 5 a 6 minutos, e cada parágrafo traz informação ou emoção nova. | Teto de 6 minutos nos 3, com escada de cortes escrita. O próprio prompt não fecha na meta de 4 a 5 (§7). | VARIAÇÃO ISOLADA no teto; INCONCLUSIVO no "cada parágrafo" |

---

## 4. O processo: diagnóstico, levantamento, decisões

### 4.0 O comportamento que o prompt pede — VARIAÇÃO ISOLADA (3 de 3), com a regra da casa por cima

1. **Nada de copy antes do contexto.** Faltou informação crítica, pergunta. Nunca inventa número, depoimento, promessa
   ou autoridade do expert. É a mesma regra de `sirius-scale/REGRAS.md` §2, que vence se as duas divergirem: faltou,
   pergunta e para.
2. **Três fases em sequência, cada uma com o ok de quem decide.** Na casa, a parada existe pra decisão. O C1 parou
   depois da Fase 2 e só foi pro roteiro quando o Rodrigo liberou. O C2 teve as decisões tomadas antes, num documento
   de arquitetura, e as Fases 1 e 2 saíram compactas. O A entregou as Fases 2 e 3 juntas porque o dado do cliente já
   estava todo em arquivo. A regra que sai daí: a Fase 2 que abre decisão nova (tese, número de abertura, âncora,
   preço) para e espera; a que só executa decisão registrada não precisa parar.
3. **Adaptar ao nicho.** Os princípios valem pra qualquer nicho; linguagem, exemplo e referência são do nicho.
4. **Ser crítico com oferta frágil** (preço errado, oferta que canibaliza o front, promessa fraca) e apontar antes de
   produzir. É o diagnóstico do §4.1.

Quem escreve é o agente `copy` (`sirius-scale/REGRAS.md` §3), seguindo este arquivo; depois vêm o `/humanizer` e o
`/revisar` (§10).

### 4.1 O diagnóstico da oferta, antes de tudo — VARIAÇÃO ISOLADA (3 de 3; 2 de 3 rodaram antes da Fase 1, como o prompt manda)

**Os 5 checks do prompt:**
1. **A oferta tem razão real de existir?** Não é só "compre mais". No C: o curso não contém o livro e o livro não
   contém o curso.
2. **O preço faz sentido?** Não canibaliza o front e não desvaloriza o cheio. Na base, o upsell custou de 2 a 2,4
   vezes o front nas escadas que sobem e cerca de 30% do front na que desce, sempre abaixo do cheio de fora (de 48% a
   80% dele). O preço relativo está em `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.2.
3. **A diferença entre front e upsell é tangível?** A pessoa consegue dizer numa frase, sem esforço. No C1: "o livro
   eu leio; o curso é [o expert] fazendo na minha frente" (reescrito do caso).
4. **Existe pelo menos uma âncora externa de preço?** Sem ela, diz o prompt, o reveal fica fraco.
5. **Existem provas reais?** Depoimento, dado, caso.

Se um falhar, o prompt manda avisar antes de levantar o contexto: talvez a oferta tenha que mudar antes da copy.

**O que a casa fez com isso:**
- **Os três passaram em 4 de 5, e os três falharam no mesmo check, o da âncora externa.** Nenhum tinha concorrente
  comparável com fonte. Nos três a falha foi declarada e a peça seguiu, porque a falha era decisão registrada, não
  descuido. O único dado de mercado que existia no C1 (o preço de um serviço avulso) foi descartado pelo Rodrigo:
  comparava um serviço com uma aula gravada.
- **O check 2 depende de o preço cheio de fora ser verdade no dia em que o upsell roda.** No C1 o cheio era o preço
  público da outra frente; ficou como pendência "reconferir na véspera de publicar". Se cair, cai a âncora interna e
  cai o caminho 2 do fechamento, e o bloco 7 tem que ser reescrito, não remendado.
- **Um 6º check, que a casa acrescentou depois de errar (A): o que o front entrega de fato?** Não o que o documento do
  produto declara: o que cai no checkout e no e-mail de quem compra (presentes e bônus inclusos). O 1º passe do A leu
  a ficha do produto, que declarava uma limitação do front, e montou a tese em cima dela; o front entregava de presente
  justamente a aula que o vídeo dizia não caber nele. Mentira detectável em um clique por 100% do público, porque o
  vídeo só toca depois da compra. A anotação do caso: o documento de produto diz o que o produto é; a lista do checkout
  diz o que a pessoa recebe, e a tese do upsell depende da segunda. VARIAÇÃO ISOLADA (1 roteiro; o irmão conta o mesmo
  tipo de erro nos 3 clientes, `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.9).

### 4.2 O levantamento (Fase 1, as 28 perguntas) — VARIAÇÃO ISOLADA (2 de 3 responderam as 28 por escrito, com fonte)

Os seis blocos de perguntas do prompt, numerados aqui de 1 a 6 pra não confundir com as letras dos experts:

| Bloco | O que levantar | Onde costuma estar |
|---|---|---|
| 1. O front | o produto, o preço, o formato e a duração da VSL, **tudo o que a VSL entregou** (autoridade, história, mecanismo, dores, promessas, depoimentos) e as frases e números marcantes que não podem voltar | o roteiro da VSL; `expert/produtos/<produto>.md` |
| 2. A oferta do upsell | o produto, o preço cheio em outros canais, o preço aqui, se complementa ou evolui o front, a diferença concreta, os bônus (e quais têm autoridade de fora, como convidado ou parceria), a garantia, alguma restrição de acesso | `expert/produtos/<produto>.md` e a oferta configurada na plataforma |
| 3. O expert | quem é, há quanto tempo atua, e **um número de autoridade que a VSL não usou** (volume de produção, resultado de aluno com dado real, contexto único) | `expert/dna-expert.md` |
| 4. O avatar | quem é, a dor central na linguagem dele, o desejo dominante, a frase que ele repete, o estado emocional na chegada | `avatar.md` e `pesquisa.md` do funil |
| 5. As provas | depoimentos e formato (vídeo, texto, print), dado de transformação, o custo real de não ter o produto, uma âncora externa de mercado | o catálogo de depoimentos, `pesquisa.md`, a ficha do produto |
| 6. Restrições | termos e alegações proibidos, o tom do expert, por onde a pessoa chega ao upsell (logo depois do checkout, por e-mail, outro) | `expert/dna-expert.md`, a plataforma |

**Como a casa responde:** cada resposta sai de arquivo, com a fonte na própria linha. Campo sem dado fica "não
encontrado" e vira pergunta numa lista no fim, em ordem de quanto trava (no C1, as três primeiras mudavam a copy e as
outras, uma frase cada). Nunca se preenche com suposição (`sirius-scale/REGRAS.md` §2).

**O que mais travou na base:**
- **O número de autoridade novo (bloco 3).** Não existia em arquivo no expert C, e o Rodrigo dispensou buscá-lo.
- **O dado de transformação (bloco 5).** Não existia agregado em nenhum dos três roteiros.
- **A âncora externa (bloco 5).** Não existia nos três (§4.1).
- **A parcela do preço do upsell.** Saiu da plataforma ou ficou marcada pra entrar depois (§9.2, regra 7).

### 4.3 As decisões antes do roteiro (Fase 2, os 10 itens) — VARIAÇÃO ISOLADA (3 de 3 escreveram os 10 itens; a força de cada um vai na linha)

1. **O estado mental do comprador** (o que sente, o que espera ver, o que não quer ver, a janela de atenção realista,
   em 2 ou 3 parágrafos). Na casa foi escrito como **leitura, não dado**, e dito assim na entrega (C1, C2). As janelas
   que aparecem nos roteiros ("os primeiros 15 a 20 segundos decidem", "a decisão sai por volta do minuto 4") são
   leitura, não medição: PADRÃO INCONCLUSIVO.

2. **O que não repetir da VSL.** Uma tabela: o elemento da VSL, se já foi entregue, se pode voltar. Na casa (3 de 3):
   - a tabela ganhou uma coluna, "o que entra no lugar" (A);
   - a **garantia** volta como fato de oferta, numa frase (C1), e a fórmula que a VSL usou pra ela entra na lista do
     que não repetir (C2);
   - a **função** da âncora de custo do problema volta (o prompt exige); o conteúdo muda (C1);
   - o **presente que a VSL anunciou** pode voltar, quando o upsell usa ele como prova: é continuidade de entrega, não
     argumento repetido (A);
   - quando a VSL é dona de uma cena, o upsell fica com o momento anterior a ela e não usa a palavra-chave dela (A).

3. **A tese nova.** Não compete com o front e dá uma razão nova pra querer o upsell. O prompt oferece cinco ângulos:
   a limitação estrutural do front, profundidade contra superfície, o quê contra o porquê, o próximo degrau, a mudança
   de identidade. Na base:
   - **C1, a limitação do formato, não do conteúdo:** [o que o formato do front não consegue fazer], em vez de [o que falta nele].
     Escolhida porque fecha um loop que a própria VSL abriu (ela mostrou o expert fazendo, uma vez, num trecho) e
     porque responde à pergunta que o avatar mais fazia.
   - **C2, complemento (fora dos cinco):** com o ticket descendo, "mais profundidade" não cola; o curso é ver o expert
     fazer, o livro é a pessoa fazer.
   - **A, a amostra (fora dos cinco):** o front entregava de presente uma aula do curso; a tese virou [a pessoa já viu
     funcionar, e o que falta ver é o passo seguinte]. Troca pedir que ela acredite no que não viu por mandar
     conferir o que ela já tem. A 1ª tese do A era do tipo "o quê contra o porquê" e caiu por ser falsa (§4.1, 6º check).
   - **O que vale nas três:** a tese elogia o front na mesma frase em que mostra o que o formato dele não faz (3 de 3);
     nunca promete o que o upsell não entrega (no C1, a 1ª versão dava a entender que o curso resolvia os exercícios do
     livro; o Rodrigo cortou: "tem que conferir se ela resolve tudo isso, onde você viu?"); e o vilão continua o mesmo
     da VSL (C1).
   - Força: VARIAÇÃO ISOLADA nessas regras e nos dois ângulos novos (1 roteiro cada); os cinco ângulos do prompt,
     PADRÃO INCONCLUSIVO (só um foi usado).

4. **O número de abertura** (o big claim). O prompt pede 2 a 3 opções de um número específico, não arredondado, ligado
   à autoridade prática do expert, que a VSL não usou e que abra curiosidade junto com a atribuição. Na base:
   - 3 opções propostas, cada uma com fonte e avaliação (C1, A);
   - **número que o expert não sustenta na câmera não entra.** No C1, uma contagem por termo, feita por script numa
     amostra das perguntas da pesquisa, foi rebaixada de número gravável pra leitura qualitativa: serve pra orientar a
     copy, não pro expert responder "como você contou?". E a fala não atribui ao expert uma ação que ele não fez
     ("eu separei as perguntas");
   - **sem número de autoridade novo, entra um número de produto** (C1 e C2: a quantidade de exercícios sem resolução
     que o front já traz), dito e não legendado (§8);
   - **sem o número exato, vai o conservador** ("mais de N", A), em vez de precisão inventada;
   - **número do material de venda que bate de frente com a contagem real fica fora** (A);
   - **número que ainda pode mudar antes de o produto chegar fica fora** (C2: a paginação de um livro em revisão);
     entra o que não muda;
   - ⚠️ **conferir na VSL que está no ar, não só no roteiro novo.** No A, o número guardado pro upsell já estava na VSL
     no ar e voltou num gancho novo; a direção avisou, e o upsell foi gravado com ele assim mesmo.
   - Força: VARIAÇÃO ISOLADA.

5. **A atribuição mononuclear:** a frase que liga o número a uma causa só ("foi essa experiência que me ensinou uma
   verdade que separa X de Y; não é A, não é B, é outra coisa"). Na base (3 de 3): a negação tripla com três tamanhos
   diferentes (no C1, de três, quatro e dezesseis palavras) e sem percentual inventado. As negações não são aleatórias:
   são as explicações que o próprio avatar dá pra si, e nenhuma culpa a pessoa (A). VARIAÇÃO ISOLADA. ⚠️ Ver §15,
   item 6 (o `/humanizer`).

6. **A pergunta de dor ativa,** na linguagem do avatar, sem repetir a dor da VSL. Na base (3 de 3):
   - verbatim da pesquisa (C2) ou do material de venda do próprio cliente (A), quando existe;
   - uma linha a mais pra quem ainda não viveu a situação (no C1, quase metade do avatar ainda não tinha feito a prova,
     e a memória não existia pra buscar);
   - o desarme logo depois, pra pergunta não virar acusação (A).
   - Força: VARIAÇÃO ISOLADA.

7. **A promessa quantificada,** em dois eixos: o que a pessoa deixa de sofrer e o que passa a conquistar. Na base,
   quantifica-se a entrega (aulas, módulos, horas, prazo de acesso); transformação só com dado, e não havia dado em
   nenhum dos três. Sem dado, a promessa fica qualitativa e o número de resultado, se houver, vem do depoimento (C1).
   Ritmo de estudo sem fonte ("dá pra fazer em semanas, 20 minutos por dia") não entra (A). VARIAÇÃO ISOLADA.

8. **As alternativas ruins a fechar** (2 ou 3: aprender sozinho, tentativa e erro, comprar depois), cada uma com o
   lugar em que a copy desativa. Na base: a de menos evidência (objeção sem frequência medida na pesquisa) é a primeira
   a cair quando o tempo aperta (o C1 cortou assim); quando a tese nova cria uma objeção nova ("já ganhei a aula, então
   já tenho o principal"), ela é tratada dentro da própria tese (A). VARIAÇÃO ISOLADA.

9. **A cascata de âncoras:** §5.7.

10. **A dicotomia financeira:** §5.10.

**Dois itens que não estão nos 10 e entraram na Fase 2 (C1):** a frase que protege o ecossistema (§5.4) e as 3
menções de escassez mapeadas antes de escrever (§5.8). **E um que entrou na arquitetura do C2:** a lista fechada dos
números permitidos e dos proibidos na peça, antes de chamar o `copy`. VARIAÇÃO ISOLADA.

---

## 5. Os 11 blocos — VARIAÇÃO ISOLADA na ordem (3 de 3 seguiram a ordem do prompt)

A ordem é a do prompt, e os três roteiros da casa seguiram ela inteira. O B, de fora do método, seguiu outra: parabéns
e gancho, ponte do front pro curso, apresentação, diferencial, prova social, o que mais está incluso, suporte, oferta,
escassez, garantia, fechamento, com 6 a 8 minutos e 3 depoimentos no meio. É a única ordem da base ligada a número, e
não se sabe se foi ela que rodou (§15, item 3).

Cada bloco leva o tempo e a orientação de tom e cena entre colchetes. Os tempos são os do prompt; o que os roteiros
fizeram com eles está no §7. Os exemplos estão em molde: fala de roteiro da base não vai literal, e o colchete diz o
que a frase faz.

### 5.1 Bloco 1 — Interrupção e gancho (20 a 30 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** quebrar o "lá vem outra venda" e abrir o loop.

**O prompt:** a 1ª palavra é uma parada ("Espera.", "Antes.", "Calma."); reconhece o estado da pessoa sem pedir
desculpa; promete uma revelação sem entregar; dá uma janela curta de tempo.

**O que a casa acrescentou:**
- **Confirmar a compra antes de tudo** (3 de 3): a compra está feita, não falta pagar nada, não deu nada errado. Quem
  acabou de pagar espera confirmação; ouvir que falta alguma coisa troca alívio por arrependimento.
- **A janela dita tem que ser verdade** (3 de 3). No A, a revisão pegou "quatro minutos" numa peça estimada em quase
  seis: erro de 30% na frase que mais pede confiança. C1 e C2 deixaram a instrução de produção: se o corte passar de
  5:30, regrava a linha com "seis minutos" ou corta o bloco 11.
- **A palavra de parada não se repete entre dois upsells que a mesma pessoa pode ver** (o C2 abriu com "Antes" porque o
  C1 já tinha gasto "Espera").
- O expert já está falando quando o vídeo abre (C1, C2).

**Exemplos:**
- [Palavra de parada.] [Frase que pede pra não fechar a página.] [Frase que diz que o front já está garantido.] [Frase
  que diz que isto não é cobrança nem etapa pendente.] (C1)
- [Frase que revela que o expert guardou um assunto de propósito.] [Frase que diz pra quem ele não servia antes.]
  [Frase que diz que agora serve.] (C2)
- [Frase que diz pra quem o vídeo foi gravado: só pra quem acabou de fazer essa compra.] [O pedido da janela de tempo,
  em minutos.] (A)

### 5.2 Bloco 2 — Número de abertura e atribuição (30 a 45 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** autoridade nova e curiosidade funda.

**O prompt:** um número específico, não arredondado, que a VSL não usou; a atribuição mononuclear ligada a ele; a
negação tripla.

**Na casa:** o número segue o §4.3, item 4. A credencial que a VSL gastou entra zero vezes, e a autoridade da peça passa
a ser o ato, o expert fazendo na tela (C1, C2). A negação tripla vai com três tamanhos diferentes (§4.3, item 5).

**Exemplos:**
- [O número de produto: quantos itens reais o front traz.] [O que falta neles.] [Frase que diz que isso não é falha do
  front.] [O que o formato do front dá.] [O que esse formato não faz.] (C1)
- [Negação curta.] [Negação curta.] [Negação bem mais longa, com o que todo mundo repete.] (C1)

### 5.3 Bloco 3 — A tese nova (45 a 60 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** o argumento central e a razão nova pra querer o upsell.

**O prompt:** não briga com o front (não desvaloriza o que a pessoa acabou de comprar); traz um insight que ela não
tinha; termina abrindo o reveal do produto.

**Na casa:** é aqui que entra a pergunta de dor ativa (3 de 3), feita devagar e com pausa depois. A tese segue o §4.3,
item 3.

**Exemplos:**
- [Pergunta de memória: quantas vezes a pessoa fez tudo e o resultado veio diferente.] [Frase da reação dela, sem
  entender onde perdeu.] [Pausa.] [Par de frases curtas que contrapõe o resultado que chegou à explicação que não
  veio.] (C1)
- [Frase que nomeia o buraco e diz que ele não é conteúdo, porque conteúdo a pessoa já comprou.] (C1)
- [Frase que troca a culpa da pessoa por uma informação que ninguém deu a ela.] (A)
- [Frase que separa o que a pessoa já garantiu, ver, do que falta, fazer.] (C2)
- [Frase que liga o conceito à aula que veio com a compra.] [Frase que diz que ela foi colocada ali de propósito.]
  [Convite pra assistir hoje, sem pedir que acreditem no expert.] (A)

### 5.4 Bloco 4 — O reveal com prova concreta (45 a 60 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** o produto como resposta à tese, com prova concreta de profundidade ou de escopo.

**O prompt:** o nome do produto aparece aqui, não antes; um exemplo concreto da diferença (no front, X é uma seção; no
upsell, X são várias aulas); nada de lista genérica de recursos.

**Na casa:**
- A prova é o produto real na tela (3 de 3): a lista de aulas da plataforma (C1, A) ou as páginas e o sumário do livro
  (C2), com a contagem conferida item por item (no C1, a soma das aulas em que o expert faz na frente do aluno, contada
  no print da plataforma).
- A diferença dita é a que existe de fato. No C1, o que parecia exclusivo do curso também estava no livro, e só uma
  parte sobrou como diferença; no C2 a peça vende formato e volume de treino, nunca "conteúdo que o outro não tem".
- **A frase que protege o ecossistema** (C1, VARIAÇÃO ISOLADA): uma frase dizendo o que o upsell não é, pra proteger
  o produto maior e ganhar credibilidade.
- **A cena do estado depois da compra** cabe no fim deste bloco (A): a cena da dor do bloco 3, com outro final.

**Exemplos:**
- [Frase que contrapõe o que a pessoa faz no front ao que ela vê o expert fazer no upsell.] (C1)
- [O que o item é no front.] [O que esse item vira no upsell, com o número de aulas.] (A)
- [Frase que diz o que o curso resolve e que ele não é o programa principal.] (C1)
- [A cena do bloco 3, agora com o final bom.] (A)

### 5.5 Bloco 5 — Acesso e praticidade (20 a 30 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** mostrar como a pessoa usa o produto no dia a dia.

**O prompt:** ritmo mais rápido; tempo de acesso, formato, se dá pra usar em qualquer lugar, material de apoio;
descrever, não vender.

**Na casa:**
- Uma cena de uso (3 de 3), que pode também desativar uma alternativa: [frase que diz que o upsell não substitui o
  front, e que a pessoa usa os dois já sabendo o que procurar] (A).
- Frase que depende de configuração só entra confirmada (no C1, a frase sobre onde o acesso aparece ficou marcada pra
  confirmar e, sem confirmação, não entra).
- Prazo de entrega de produto físico só com fonte (C2).
- Em gravação que serve a mais de um mercado, nada que só vale num deles, como entrega física (A; §9.2, regra 8).

**Exemplo:** [o formato] + [quantos módulos e horas] + [por quanto tempo fica com a pessoa] + [pra que ela volta
nele]. (C1)

### 5.6 Bloco 6 — Bônus (30 a 45 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** somar valor, enxuto.

**O prompt:** no máximo 3 bônus (mais que isso vira ruído depois do checkout); bônus com autoridade de fora (convidado,
parceria, marca) é nomeado; bônus genérico ou fraco, melhor cortar do que listar.

**Na casa:**
- No máximo 3 nos três (C1: 2; C2: um presente e 2 bônus; A: 1).
- **Bônus que o front já entrega sai** (o A cortou uma aula que o front já dava, com a regra do próprio prompt: um bônus
  que a pessoa já tem é pior que um fraco).
- **Valor de bônus só se existir valor declarado em arquivo,** e nunca um número igual ao preço do downsell que vem na
  tela seguinte (C1, C2). Sem valor, o bônus entra pelo nome.
- Bônus com autoridade de fora: nenhum na base (PADRÃO INCONCLUSIVO).

**Exemplo:** [frase curta que anuncia quantos bônus entram junto, sem dizer valor]. (C1)

### 5.7 Bloco 7 — Âncoras em cascata e o preço (60 a 75 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** criar contraste antes de revelar o preço.

**O prompt:** o tom muda (mais sério, mais direto); três âncoras antes do número, nesta ordem: a externa (quanto o
mercado cobra por algo equivalente), a interna (o preço cheio normal) e o custo do problema; pausa de 2 segundos;
o reveal com contraste na tela ("de … por …"); e uma tradução prática no fim ("isso dá X por dia").

**Na casa:**
- **Só âncora verdadeira** (3 de 3): antes do preço, duas âncoras nos três (o preço cheio fora desta compra e o custo
  do problema); no segundo mercado do A, só o cheio. Nenhuma externa. A falta vai declarada na ficha da peça, numa nota
  de produção e na entrega, e a lacuna nunca vira número na tela. A anotação do C1: preferimos duas verdadeiras a três
  com uma inventada.
- **O preço cheio "fora desta compra"** é a âncora interna dos três, e só vale se for o preço público no dia (§4.1).
- **O custo do problema é novo.** A VSL gastou o dela, e repetir é o primeiro erro da lista do prompt. Sem número
  quando não existe (C1, C2). Com número só se vier do material do próprio cliente, uma vez, como régua de valor e
  nunca como promessa de ganho; e cortar a frase não derruba a cascata (A).
- **Um detalhe errado sobre o mundo do avatar derruba o bloco.** No C1, a frase do custo dizia que não havia como
  recorrer do resultado; havia, e o avatar sabe disso. A frase saiu.
- **A ordem varia.** O A pôs o custo antes do cheio: sem a externa, o custo é a única régua fora do próprio produto, e
  com o cheio primeiro a peça soa como desconto em vez de contraste. C1 e C2 puseram o cheio antes do custo. Qual
  converte mais: PADRÃO INCONCLUSIVO.
- **Pausa de 2 segundos com a tela limpa, e só então o cartão "de [cheio] por [preço]"** (3 de 3).
- **A parcela sai da plataforma** (§9.2, regra 7). A tradução prática é conta em cima de número real: o preço dividido
  pelos dias de acesso (A), ou a parcela por mês, e esta só depois que a parcela existir (C1, C2).
- Em gravação pra mais de um mercado, o preço vive num bloco gravado à parte, um por mercado (A; §10).

**Exemplos:**
- [Frase que pede atenção ao preço e avisa que ele muda de contexto.] (C1)
- [O preço cheio do upsell fora desta compra.] [De quem é esse preço: de quem chega sem ter o front.] (C1)
- [Frase que abre o custo do problema: um valor que ninguém cobra e a pessoa paga assim mesmo.] (C1)
- [O upsell inteiro, com os bônus.] + [o preço dentro desta compra]. (C1)

### 5.8 Bloco 8 — Escassez real (15 a 20 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** urgência sem mentir.

**O prompt:** escassez da oferta (este preço, esta página, este momento), nunca cronômetro; tom de transparência, não
de pressão; 2 ou 3 frases.

**Na casa:**
- **O que some é o botão, não a página** (C). "A página sai do ar" é falso: quem reabre o link vê a página, sem o botão.
- **As 3 menções são da mesma verdade** (3 de 3): depois do preço (o botão só existe nesta compra), no bloco 8 (fechou a
  página, ele não volta) e no caminho 2 do bloco 10 (fora daqui, o preço é o cheio).
- **Não listar o truque dos outros pra negar** (C1): a frase que negava cronômetro e vaga saiu, porque nomear o truque
  planta a ideia; ainda ganhou uns 3 segundos.
- **A escassez tem que sobreviver ao downsell** (A, PADRÃO INCONCLUSIVO). "Nunca mais" e "o menor preço que existe"
  viram mentira segundos depois, quando o downsell oferece o mesmo curso mais barato. A frase que sobrevive prende a
  escassez ao pacote ([o preço] com [o prazo inteiro de acesso]), não ao preço solto.

**Exemplos:**
- [Frase que anuncia honestidade sobre o botão.] [Frase que diz que é mecanismo, não pressão.] [Frase com o fato: o
  botão só existe com a compra aberta.] [Frase que diz o que acontece se a pessoa fechar a página.] (C1)
- [O preço amarrado ao prazo inteiro de acesso e ao fato de a pessoa ter entrado pelo front.] [Frase que prende esse
  preço a esta página.] [Contraste: o cheio segue no site, este não.] (A)

### 5.9 Bloco 9 — Garantia (15 a 20 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** zerar o risco percebido.

**O prompt:** prazo e condição; linguagem de "sem burocracia"; posicionar como risco zero.

**Na casa (3 de 3):** a garantia diz o que fazer dentro do prazo, uma ação concreta com o produto (entrar e assistir uma
aula inteira; escolher um exercício, fazer e sentir se é isso; ver o primeiro módulo inteiro). O calor humano volta
aqui. A fórmula de garantia que a VSL já usou não se repete (C2).

**Exemplo:** [frase que tira o peso da decisão] + [o prazo da garantia] + [a ação concreta com o produto dentro do
prazo] + [o que fazer se não servir: pedir o reembolso]. (C1)

### 5.10 Bloco 10 — Os três caminhos e o fechamento (45 a 60 s) — VARIAÇÃO ISOLADA (3 de 3)

**Função:** forçar a decisão entre três caminhos concretos.

**O prompt:** os três caminhos, um de cada vez: 1, seguir só com o front (respeitoso, mas concreto sobre o limite); 2,
esperar e comprar depois pelo preço cheio (concreto sobre o custo de esperar); 3, comprar agora (a porta limpa).
Depois, voltar ao gancho do bloco 1 e fechar o loop, e o CTA direto. A dicotomia é financeira, não filosófica.

**Na casa:**
- Os três caminhos têm número (3 de 3). O caminho 2 diz a diferença em reais, e só pode ser dito porque o preço de fora
  é real.
- O caminho 1 elogia o front de novo antes de dizer o limite (3 de 3).
- O loop do bloco 1 fecha com a mesma ideia e, se houver, a mesma imagem (A).
- **O texto do botão não é falado** (decisão do Rodrigo no funil do C): a fala aponta pro botão sem dizer o texto dele, e o
  texto exato fica com a página, que pode mudar sem regravar. Exceção: quando o preço no botão faz parte da âncora
  falada, a fala repete o botão palavra por palavra (C1), e trocar o botão obriga a regravar a linha.

**Exemplos:**
- [Bordão do expert.] [Frase que anuncia os três caminhos, sem enfeite.] (C1)
- [1º caminho: seguir só com o front.] [Elogio: ele faz o que foi prometido.] [O limite, concreto.] (C1)
- [2º caminho: pegar o upsell depois.] [Fora desta compra custa o cheio, e o botão some.] [Frase que diz que esperar
  não informa nada e custa a diferença em reais.] (C1)
- [Frase que diz que esse caminho é legítimo.] [O limite: a pessoa segue sabendo, sem fazer.] (A)
- [Volta ao gancho do bloco 1: a amostra.] [Frase que diz que o upsell é o resto dela.] (A)

### 5.11 Bloco 11 — Depoimentos, opcional (30 a 45 s) — VARIAÇÃO ISOLADA (2 de 3 usaram; o A cortou)

**Função:** um reforço no fim, do tipo "vou te deixar com algumas pessoas".

**O prompt:** só com 2 ou 3 depoimentos com resultado tangível; nunca um que já apareceu na VSL do front; cortes curtos
(10 a 15 s cada); fala leve do expert entre eles; fecho acolhedor, não comercial.

**Na casa:**
- Quem entra na VSL do front não entra no upsell da mesma frente. A divisão é feita numa tabela, antes de escrever (C).
- A regra de depoimento da casa (`sirius-scale/frameworks/oferta-14-secoes.md` §5): print, o expert lê em voz alta,
  palavra por palavra; vídeo, a fala apresenta a categoria e o vídeo carrega o caso; nome de aluno nunca na fala (fica
  só no marcador de produção, pra trocar o depoimento sem regravar).
- C1 e C2 usaram prints lidos (3 e 2), com uma linha de comentário sobre o padrão entre eles. O A ficou sem bloco 11:
  todos os depoimentos disponíveis estavam na VSL.
- **É o primeiro bloco a sair** se o corte passar de 6 minutos (§7).
- Cortes de vídeo de 10 a 15 s: nenhum na base (PADRÃO INCONCLUSIVO).
- ⚠️ O B, o único com número, fez o contrário: 3 depoimentos em vídeo no meio do roteiro e 6 a 8 minutos (§15,
  item 3).

**Exemplos:**
- [Frase que apresenta as mensagens de aluno antes de a pessoa sair.] (C1)
- [Fecho acolhedor, no lugar do CTA.] (C1)

---

## 6. A página acima do vídeo — VARIAÇÃO ISOLADA (3 de 3 escreveram o anexo de página)

**O prompt** pede a estrutura da página como anexo de todo roteiro, de cima pra baixo: uma barra de progresso com
rótulo neutro (front comprado, próximo passo, acesso liberado), a headline no tom do expert e com curiosidade, o player,
e o botão com o benefício e o preço. E proíbe três coisas: cronômetro de urgência, headline do tipo "sua compra ainda
não está completa" (mente tecnicamente) e barra de progresso com rótulo que entrega a oferta.

**O que a casa acrescentou (3 de 3, salvo onde está dito):**
- **Microcopy embaixo do botão:** o que a pessoa leva e a garantia; no C, também que a compra é de um clique, com o cartão já salvo.
- **A recusa como link de texto discreto, sem cor de botão e sem culpa.** Quem recusa vai pro downsell segundos
  depois, e não faz sentido humilhar quem vai ser abordado de novo.
- **O preço do front fora da tela:** já foi pago, e reaparecer confunde a conta que o bloco 7 monta.
- **Nenhuma menção ao downsell,** nem ao preço dele.
- **A capa ou o mockup do upsell não vai acima do player,** porque o reveal é o bloco 4; pode ir no botão ou abaixo do
  vídeo (C2).
- **Headline e vídeo dizem a mesma coisa.** No A, a tese mudou no 2º passe, e a headline antiga, que repetia a frase
  falsa, teve que mudar junto; corrigir só o roteiro deixaria a página mentindo.
- Uma sublinha com a janela de tempo, que também tem que ser verdade.
- Em mais de um mercado, o botão tem uma versão por moeda (A).

**Exemplo, em molde (do C1):**

```
✅ [Front comprado]   ● [Próximo passo]   ○ [Acesso liberado]

[Headline: confirma o front e abre a curiosidade sobre uma coisa dentro dele.]
[Sublinha: a janela de tempo, e que a decisão é da pessoa.]

[PLAYER]

[BOTÃO: O UPSELL E O PREÇO]
[Microcopy: compra de um clique, cartão já salvo, e a garantia.]

[Recusa em link discreto: a pessoa escolhe seguir só com o front.]
```

**O que a casa mandou tirar de uma página que já rodava** (a do expert A, antes da casa): a headline que anunciava uma
condição desbloqueada antes do vídeo, o que mata a curiosidade do bloco 1, e o aviso de que a oferta nunca mais seria
vista, que briga com o downsell. A página do B também entregava o desconto na headline. O resto da página de backend
(a do downsell, o que muda entre as duas) está em `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.13;
quem monta é o agente `webdesigner`.

---

## 7. Tempo e ritmo — VARIAÇÃO ISOLADA no teto de 6 minutos e na escada de cortes; PADRÃO INCONCLUSIVO na meta de 4 a 5

**O que o prompt diz, em três lugares:** a meta é de 4 a 5 minutos (Fase 3); o princípio 7 aceita até 5 ou 6; a lista
de erros marca acima de 6 como erro. E cada bloco tem a sua faixa.

**A meta do prompt não cabe nos blocos do próprio prompt.** A soma dos pisos dos 10 blocos obrigatórios já dá 5:25;
com o bloco 11, 5:55; e a soma dos pontos médios passa de 6 minutos. O C1 e o A chegaram nisso cada um por conta
própria. A nota da casa no prompt: mudar a meta é decisão do Rodrigo. Até lá, a régua que vale é o teto de 6.

**Os tempos dos dois roteiros do C, por bloco:**

| Bloco | Prompt | C1 | C2 |
|---|---|---|---|
| 1 | 20 a 30 s | ~20 s | ~25 s |
| 2 | 30 a 45 s | ~38 s | ~43 s |
| 3 | 45 a 60 s | ~45 s | ~45 s |
| 4 | 45 a 60 s | ~55 s | ~47 s |
| 5 | 20 a 30 s | ~18 s | ~20 s |
| 6 | 30 a 45 s | ~27 s | ~23 s |
| 7 | 60 a 75 s | ~44 s + 2 s de pausa | ~44 s + 2 s de pausa |
| 8 | 15 a 20 s | ~15 s | ~15 s |
| 9 | 15 a 20 s | ~16 s | ~19 s |
| 10 | 45 a 60 s | ~55 s | ~50 s |
| 11 (opcional) | 30 a 45 s | ~35 s | ~25 s |

Pra caber no teto, os dois ficaram abaixo do piso do prompt nos blocos 6 e 7 (e o C1 também no 5). O A contou por
palavras: cerca de 870 no total, com o bloco 3 como o maior (180 palavras), e sem bloco 11.

**A estimativa e o tempo real:**
- A estimativa sai das palavras, numa faixa de ritmo: cerca de 890 palavras nos blocos 1 a 10 deram de 5:15 a 6:00, a
  150 a 170 palavras por minuto (C1, C2); cerca de 870 deram de 5:26 a 6:12, a 140 a 160 (A).
- O único gravado e editado (A) fechou em **4:50**, abaixo da faixa estimada. É uma medida só, e o ritmo real do
  expert não estava registrado antes da gravação.
- Regra: estimar pela faixa e dizer a faixa inteira, não só o ponto médio confortável; cronometrar o corte. VARIAÇÃO
  ISOLADA (1 medida).

**A escada de cortes, escrita antes de gravar (3 de 3):**
1. Passou de 6:00: sai o bloco 11, antes de qualquer outra coisa.
2. Depois, frases autocontidas, em ordem de menor dano, cada uma marcada no roteiro (no C1, uma fala do bloco 3 e a 2ª
   frase da garantia; no C2, uma frase do bloco 3 junto com a 1ª do bloco 4, que depende dela, e depois a última do
   bloco 5).
3. O que entrou por último sai primeiro (A: a cena do estado depois da compra, que tinha acabado de entrar).
4. A frase que responde à objeção nº 1 do avatar é a última a sair (A).
5. Nenhum corte mexe em bloco de preço gravado em mais de uma versão: dobra o trabalho de edição (A).
6. Passou de 5:30: a janela dita no bloco 1 sobe pra "seis minutos" ou o bloco 11 sai (C1, C2).

**O ritmo dentro do vídeo (3 de 3):** bloco 3 devagar, com pausa depois da pergunta; bloco 5 mais rápido, quase
enumerando; bloco 7 mais lento e sério; bloco 8 de voz mais baixa; bloco 10 firme e próximo. O "cada parágrafo traz
informação ou emoção nova" do prompt não foi medido (PADRÃO INCONCLUSIVO).

---

## 8. Tom, imagem e som — VARIAÇÃO ISOLADA (3 de 3 no tom e na imagem; 2 de 3 na trilha)

**Tom.** O prompt calibra o upsell um degrau mais firme que a VSL: a pessoa acabou de decidir e está num momento de
confiança e ação; acolhimento demais desperdiça o embalo, agressividade demais queima o estado bom. Por bloco:
- bloco 1: firme, sério, interrompendo;
- blocos 2 a 4: didático, honesto;
- bloco 7: firme, direto, sem sorriso;
- blocos 9 a 11: suaviza, e o calor humano volta.

Na casa (3 de 3), firme quer dizer objetivo e sem cerimônia, nunca confronto. As proibições de voz da ficha do expert
(`expert/dna-expert.md`) valem dentro do upsell também (no C: um bordão por bloco no máximo, nenhuma promessa de
resultado garantido, nada de vocabulário de lançamento como "vagas" e "últimas").

**Imagem, bloco a bloco (o que entrou na base):**
- **1:** plano fechado ou médio, olho na câmera; no A, sem corte até o fim do bloco. A única inserção é a que prova a
  frase (no A, o cartão da aula que o front deu de presente).
- **2:** o objeto do número na mão ou na tela (C1, C2). Foto real de trajetória só se existir no acervo; se não existir,
  fica no rosto (A).
- **3:** rosto até o desarme; a imagem do conceito depois.
- **4:** o produto real: a lista de aulas na plataforma (C1, A) ou as páginas e o sumário do livro (C2); no A, o
  módulo aberto com a aula da amostra destacada.
- **5:** a área de membros, o material, o celular. Nada de caixa, correio ou embalagem num corpo que serve a um mercado
  onde o produto é digital (A).
- **6:** os bônus, um cartão de cada vez, sem valor.
- **7:** a pausa de 2 segundos com a tela limpa e, só depois dela, o cartão "de … por …" (3 de 3). Antes da pausa, o C
  mostrou o preço cheio na hora em que ele é dito; o A deixou a tela vazia.
- **8:** nada. Sem cronômetro, sem barra vermelha, sem "vagas".
- **9:** o selo da garantia (A).
- **10:** os três caminhos como três linhas na tela, uma de cada vez (3 de 3); o botão visível; quando o loop fecha,
  volta a imagem do bloco 1 (A).
- **11:** os prints, um de cada vez, enquanto o expert lê.
- **Número dito, não legendado,** quando ele sozinho na tela vira promessa de outra coisa (C1, C2: a contagem de
  exercícios sem resolução, legendada, pareceria "exercícios resolvidos").

**Som (C1, C2):** sem vinheta e sem trilha nos primeiros segundos, com o expert já falando; a trilha entra baixa no
bloco 2; sai ou baixa bem no bloco 7.

**Edição:** o mapa de edição sai do roteiro pelo `/mapa-edicao`, e a edição é do agente `video`.

---

## 9. Regras e proibições

### 9.1 Os erros que o prompt lista — VARIAÇÃO ISOLADA (os 3 roteiros conferiram contra a lista)

1. Repetir argumento da VSL do front.
2. Repetir depoimento que já apareceu.
3. Gancho que pede licença ("eu sei que você...").
4. Listar bônus antes de criar desejo pelo produto principal.
5. Revelar o preço sem âncora externa. ⚠️ Os 3 roteiros falharam neste, de forma declarada (§4.1).
6. Dicotomia final filosófica em vez de financeira.
7. Passar de 6 minutos.
8. Inventar número ou depoimento.
9. Promessa qualitativa quando dá pra quantificar.
10. Escassez falsa (cronômetro que recomeça).

### 9.2 O que a casa acrescentou — VARIAÇÃO ISOLADA (a contagem vai em cada regra)

1. **Toda frase confere com a oferta configurada e com o que o front entrega,** na véspera de gravar e na de publicar:
   o preço cheio público, a parcela, a garantia, o prazo de acesso, os presentes e bônus do front, a mecânica do um
   clique (3 de 3; `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.8 e §4.9). Afirmar sobre o front sem
   conferir a entrega foi o erro mais caro da base (A, §4.1).
2. **O downsell não se anuncia** (3 de 3): avisar que existe uma opção mais barata destrói a decisão de agora. E nenhum
   número do upsell, nem valor de bônus, coincide com o preço do downsell (C1, C2).
3. **Nome de aluno nunca na fala** (C1, C2; `sirius-scale/frameworks/oferta-14-secoes.md` §5).
4. **A credencial que a VSL gastou entra zero vezes** (C1, C2).
5. **"A página sai do ar" é proibido:** some o botão (C).
6. **Duas peças que a mesma pessoa pode ver não repetem frase** (o C2 conferiu: nenhuma frase de seis palavras ou mais
   em comum com o C1 nem com a VSL).
7. **A parcela sai da plataforma, nunca de conta.** Sem o número, a fala fica com um marcador `[[INSERIR]]` e entra
   como pick-up depois (C1, C2). No A, a parcela foi derivada por conta e foi pro teleprompter assim, marcada "a
   conferir no checkout": é exatamente o que esta regra evita.
8. **Em gravação única pra mais de um mercado, nada no corpo que só é verdade num deles** (A): preço, moeda, parcela e
   também o que não parece dado, como entrega física. A auditoria que olhou só dinheiro deixou passar duas frases
   assim. A pergunta certa é "essa frase é verdade em todos os mercados?" (PADRÃO INCONCLUSIVO, um cliente; a técnica
   está em `sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §0.1).
9. **A âncora de custo do problema não atravessa mercado** (A). Preço de produto se converte, porque é decisão da casa;
   o que um profissional cobra num país não se converte por câmbio. O mercado sem dado fica com uma âncora a menos, e
   isso vai declarado antes de comparar as taxas.
10. **Número do material de venda do cliente que contradiz a contagem real não entra** (A).

---

## 10. A entrega, a revisão e a gravação — VARIAÇÃO ISOLADA (3 de 3 na forma; as 2 revisões da base acharam bloqueio)

**O que vai na entrega** (C1 e C2; o A em dois arquivos: a direção, com a estratégia, o tempo, a cena, a página e as
auditorias, e o teleprompter, só com a fala):
1. **A ficha da peça,** antes do roteiro: formato; volume de fala em palavras; duração estimada em faixa, dita
   inteira; tom; o que a VSL gastou e aparece zero vezes; os bordões do expert, um por bloco no máximo; quantas
   âncoras e por quê.
2. **Os 11 blocos,** cada um com o tempo, a cena e o tom entre colchetes, e os marcadores de produção: `[[PRODUÇÃO]]`
   (instrução pra gravar ou editar), `[[INSERIR]]` (dado que falta e entra depois), `[[CONFIRMAR]]` (frase que só
   entra confirmada).
3. **O anexo da página** (§6).
4. **A tabela de rastreio de todo número falado,** com a fonte, e a lista dos números que ficaram de fora de propósito
   (gastos na VSL, sem fonte, ou que deixaram de ser verdade).
5. **"O que depende do expert pra gravar",** em ordem de quanto trava.
6. **As decisões de copy,** com o porquê, e as regras do prompt que a peça não cumpriu, declaradas.

**O doc de gravação é outro arquivo, só com o texto,** um por vídeo; página e notas de produção em docs separados
(decisão do Rodrigo no funil do C). No A, o teleprompter não tinha colchete nenhum (o expert trava ou lê o marcador), e
os blocos de preço ficavam no fim, um por mercado, com o ponto de entrada marcado no corpo. A forma do documento hoje
segue `sirius-scale/frameworks/copy/formatacao-de-roteiro.md`; os roteiros da base são anteriores a ele.

**Gravação pra mais de um mercado (A, PADRÃO INCONCLUSIVO):** o corpo é gravado uma vez; o dinheiro sai do texto
corrido e vira bloco de preço gravado à parte, por mercado. Como o dinheiro do upsell não fica num lugar só (as âncoras
no bloco 7, a diferença no caminho 2 do bloco 10), são dois pontos de entrada, e o segundo é uma frase inteira que
começa com conectivo ("E [diferença] a mais."), pra o corte cair numa pausa natural. Ordem sugerida: o corpo inteiro,
depois os blocos de preço de cada mercado, na mesma sessão, roupa e luz, com o mesmo tom no bloco 7.

**Números no teleprompter (A):** dinheiro e parcela por extenso nos blocos de preço, com "reais" e "centavos"
escritos (numa peça irmã, uma parcela escrita sem eles ficou ambígua na leitura); a mesma expressão grafada do mesmo
jeito no arquivo inteiro.

**Revisão.** Depois do `copy` e do `/humanizer`, o `/revisar` com olhos frescos, antes de gravar
(`sirius-scale/REGRAS.md` §5). Na base, as duas revisões acharam bloqueio, e nos dois casos de verdade, não de estilo:
- no C1, a última frase antes do botão dava a entender que o curso resolvia os exercícios do livro, o exagero que o
  Rodrigo já tinha cortado na Fase 2;
- no A, a tese falsa e as frases que só valiam num mercado, além da janela de tempo errada.

**Gravação.** Conferir a fala gravada contra o roteiro e contra a fonte de cada número. No A, o expert falou outro
número de autoridade, outra ponta da âncora de custo e outro preço no bloco do segundo mercado (que não foi usado), e a
legenda seguiu a fala (evidência no caso de origem; `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.14).

**A dependência que a tese cria (A).** Com a tese da amostra, o presente do front não pode sair da oferta do front
enquanto o vídeo estiver no ar, e ele tem que ser liberado na hora (o vídeo pede pra assistir hoje). Quem mexer na
oferta do front precisa saber disso.

---

## 11. Checklist antes de entregar o roteiro — VARIAÇÃO ISOLADA (montado das conferências dos 3 roteiros e da revisão do C1)

1. Os 5 checks do diagnóstico, mais o 6º (o que o front entrega), com veredito e fonte; o que falhou, declarado (§4.1).
2. As 28 perguntas respondidas com fonte; o que faltou, na lista de perguntas, em ordem de quanto trava (§4.2).
3. A tabela do que a VSL gastou, e nada dela na fala: autoridade, história, mecanismo, analogias, dores, promessas,
   depoimentos, números, a fórmula da garantia.
4. Nome do produto só no bloco 4.
5. Todo número falado na tabela de rastreio, com fonte; nenhum que o expert não sustenta na câmera.
6. Escassez 3 vezes, todas verdadeiras (o botão, não a página); nenhum "nunca mais" que o downsell desminta.
7. O downsell não aparece, nem o preço dele.
8. Âncoras: quantas e quais; a externa, se faltou, declarada.
9. Parcela da plataforma ou marcada pra inserir; tradução prática só sobre número real.
10. Bônus: no máximo 3, nenhum que o front já dá, valor só se declarado em arquivo.
11. A janela dita no bloco 1 igual à duração; a faixa estimada inteira; a escada de cortes escrita; teto de 6 minutos.
12. Nome de aluno na fala: zero. Credencial gasta na VSL: zero.
13. A fala aponta pro botão sem dizer o texto dele, ou é idêntica ao botão quando o preço nele faz parte da âncora.
14. A página: barra neutra, headline sem spoiler e coerente com a tese, microcopy com o que a pessoa leva e a garantia,
    recusa discreta e sem culpa, sem preço do front, sem downsell, sem cronômetro.
15. Mais de um mercado: cada frase do corpo é verdade em todos.
16. `/humanizer` no texto inteiro e `/revisar` com olhos frescos (`sirius-scale/REGRAS.md` §3 e §5).

---

## 12. Métricas: o que medir e a régua — PADRÃO INCONCLUSIVO (a régua do prompt é de mercado; a única medição da base é de um roteiro de fora do método)

**A régua do prompt** pra taxa de aceite de upsell depois do checkout, em infoproduto: 5% é o mínimo aceitável; de 8%
a 12%, bom; de 12% a 20%, excelente; acima de 20%, considerar subir o preço. Se ficar abaixo do mínimo depois de 50
vendas do front, suspeitar nesta ordem: do produto (a oferta tem razão de existir?), do preço (cabe no bolso do
comprador?) e só depois da copy (a tese está clara? o gancho funciona?). **É número genérico de mercado, não medido na
casa: serve pra suspeitar de problema, não como meta** (nota da casa no próprio prompt). O roteiro do B trazia outra
faixa de mercado, de 8% a 15%, também sem medição.

**A meta que o Rodrigo usa** numa consultoria é outra: "aí também você quer ter 20% de conversão do upsell, 15% do
downsell". A origem desse número não está registrada.

**O único número da base** (B, roteiro de fora do método, versão do vídeo não confirmada):
- Por oferta, na janela da compra (o mesmo dia): cerca de 6,6% dos compradores do front levaram o upsell, e cerca de
  3,5% dos que não levaram compraram o downsell.
- Contando qualquer compra do curso no período, por qualquer caminho: 11,3%.
- A mesma venda, lida por bases diferentes, cai em faixas diferentes da régua do prompt: 11,3% fica em "bom"; os
  6,6% ficam entre o mínimo e o bom. E as duas leituras ficam bem abaixo da meta do Rodrigo.
- Rodrigo, sobre esse funil: "E a gente testou só um vídeo de upsell, que tava vendendo o curso."

**Como medir** (`sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.15): pela oferta de um clique (o código
da oferta na plataforma), na janela da compra. O denominador são os compradores do front; no downsell, os que
recusaram o upsell. Dizer sempre a base. Contar quem comprou o produto do upsell mistura o um clique com compra
posterior e com lançamento: no A, a taxa que existia antes da casa (7,7%) era cruzamento de e-mails do período inteiro,
metade das vendas do curso vinha de fora do funil, e a direção chegou a compará-la com a faixa "bom" do prompt como se
fosse taxa de um clique. Ninguém mediu quantas pessoas viram cada página, então a taxa do downsell não tem denominador
real. No funil de vocês, o registro fica em `funis/<nome>/desempenho.md`, e a leitura de resultado passa pelo
`/debriefing`.

---

## 13. Onde a casa vence o prompt — VARIAÇÃO ISOLADA (nas 3 peças feitas com ele)

| O prompt manda | A casa faz | Por quê |
|---|---|---|
| Faltou dado crítico, pergunta | o mesmo, e antes procura em arquivo; faltou, pergunta e para | `sirius-scale/REGRAS.md` §2; se divergirem, a casa vence |
| Três fases, cada uma com o ok | a parada é pra decisão nova; decisão já registrada não para (§4.0) | C2 e A juntaram fases e listaram, pra antes de gravar, as decisões que ainda estavam em aberto |
| Negação tripla ("não é A, não é B, não é C") | três negações de tamanhos diferentes | tríade sincronizada é marca de texto de IA |
| Atribuição com percentual ("80% do meu resultado") | atribuição singular, sem percentual | o percentual não existia em arquivo |
| Número de abertura de autoridade, específico, não arredondado | só número com fonte que o expert sustenta; sem ele, um número de produto (C1, C2) ou o conservador (A) | precisão inventada passa pela revisão porque parece dado |
| Três âncoras antes do preço, uma delas externa | duas verdadeiras (o cheio de fora e o custo do problema); a externa não existiu em nenhum roteiro, e a falta vai declarada | `sirius-scale/REGRAS.md` §2 |
| Escassez dita 3 vezes | as 3 menções são da mesma verdade: o botão, a página, o preço de fora | não existe outra escassez verdadeira no backend |
| Promessa quantificada sempre que possível | quantifica a entrega; transformação só com dado | número de resultado sem fonte é invenção |
| Tradução prática do preço ("isso dá X por dia") | só sobre número real: o preço, ou a parcela da plataforma | parcela estimada é número inventado |
| Vídeo de 4 a 5 minutos | teto de 6, com escada de cortes | os pisos dos blocos do próprio prompt somam 5:25 (5:55 com o bloco 11) |
| Botão com benefício e preço, repetido no CTA | a fala não nomeia o botão, salvo quando o preço nele faz parte da âncora falada | o texto do botão muda sem regravar |
| "Esta página" como escassez | o botão some, a página não; e a escassez se prende ao pacote pra sobreviver ao downsell | "a página sai do ar" e "nunca mais" são falsos nesse funil |
| Lista de 10 erros | mais um: afirmar sobre o front sem conferir o que ele entrega | foi o erro mais caro da base (§4.1) |

---

## 14. O que transfere e o que é do caso — PADRÃO INCONCLUSIVO (nada disso foi medido; aplicar avisando, `sirius-scale/REGRAS.md` §4)

**Deve transferir pra qualquer upsell de um clique depois de uma VSL:**
1. A ordem dos 11 blocos e a página acima do vídeo, como especificação.
2. O diagnóstico antes de escrever, com o 6º check (o que o front entrega).
3. A tabela do que a VSL gastou, e nada dela na fala.
4. O gancho que confirma a compra, e a janela de tempo dita verdadeira.
5. A tese que elogia o front e mostra o que o formato dele não faz.
6. Só âncora e escassez verdadeiras, com a falta declarada.
7. O downsell não anunciado.
8. A tabela de rastreio dos números e a escada de cortes.

**É do caso:**
1. O número de abertura de produto (a contagem de exercícios sem resolução que o front já traz): depende de o front
   ter um ativo contável assim.
2. As duas frentes que fazem do preço de fora um fato: depende de o cliente ter dois produtos que são front
   um do outro, no ar ao mesmo tempo (`sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` §4.1).
3. A tese da amostra: só existe quando o front já entrega um pedaço do upsell.
4. A tese de complemento com o ticket descendo: uma peça, não gravada.
5. A gravação única com bloco de preço por mercado: só com venda em mais de um mercado.
6. A frase que protege o ecossistema: quando existe um produto maior pra proteger.
7. As proibições de voz e os bordões de cada expert, e os números de avatar de cada pesquisa.
8. A mecânica do um clique foi conferida na Hotmart; em outra plataforma, conferir antes de escrever a escassez.

---

## 15. Pontos em aberto

1. **Nenhum roteiro deste método tem resultado.** A primeira medição possível é o do A, gravado e aprovado, quando for
   ao ar: medir por oferta, na janela da compra (§12).
2. **A meta de duração.** A do prompt (4 a 5 minutos) não cabe nos blocos dele; o único editado fechou em 4:50. Mudar
   a meta é decisão do Rodrigo.
3. **Depoimento e duração.** O prompt faz do bloco 11 um opcional, o primeiro a sair, com teto de 6 minutos; o B, o
   único com número, usou 3 depoimentos no meio e 6 a 8 minutos, e não se sabe qual versão rodou. Qual caminho converte
   mais: PADRÃO INCONCLUSIVO.
4. **A âncora externa falhou em 3 de 3.** Vale manter como check que reprova a oferta, ou ele vira "declare se não
   existir"?
5. **A ordem das âncoras** (o custo antes ou depois do cheio): dois jeitos na base, nenhum medido.
6. **A negação tripla e o `/humanizer`.** O humanizer caça paralelismo negativo e regra dos três; os roteiros da base
   são anteriores a ele e resolveram só a tríade sincronizada (tamanhos diferentes). Se ele apontar a negação tripla do
   bloco 2, manter ou não a figura é decisão do Rodrigo.
7. **A escassez que sobrevive ao downsell** e o fechamento de pouca pressão como redutor de reembolso: hipóteses do A,
   sem medição.
8. **O mercado com menos âncoras** (no A, o segundo mercado ficou só com o cheio antes do preço): se a taxa dele vier
   abaixo da do outro, é a primeira hipótese a testar, junto com o presente que a tese usa como prova: como ele
   chega na versão do segundo mercado.
9. **A parcela do teleprompter do A** saiu de conta e precisa ser conferida no checkout antes de publicar.
