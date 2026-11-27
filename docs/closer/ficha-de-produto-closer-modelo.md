# FICHA DE PRODUTO para o closer (modelo em branco)

## Como usar

- O dono preenche **uma ficha por produto**. A closer (IA ou humana) usa **somente** o que está nesta ficha para falar de produto, oferta, preço, frete, condição, cupom, garantia, bônus, prazo, prova social e esteira pós-compra.
- **Fontes canônicas:** a **ficha é a fonte dos fatos**; o **prompt-base é a fonte das regras**; os **textos prontos** (abertura, espera, passagem, objeções) vêm da copy aprovada do projeto (`camila-mensagens-copy.md`, versão 2) e vão para o Conhecimento. O mapa psicológico é análise do dono; só as 8 regras de comportamento do prompt-base vão à Camila.
- **Onde a ficha vive no Up:** a Camila só enxerga o que está escrito no **Conhecimento** do projeto e **só envia link que esteja escrito lá** [SISTEMA, informado em 13/11, reconfirmar]. Depois de preencher esta ficha, **escreva o conteúdo e os links no Conhecimento**.
- **Campo em branco ou "não sei" significa: a closer não afirma nada sobre aquele ponto e escala.** É melhor escrever "NÃO EXISTE" do que deixar vazio. Exemplo: se não há garantia, escreva "NÃO EXISTE garantia".
- **Ficha com campo obrigatório vazio: a closer não inicia atendimento de venda** daquele produto.
- Escreva fatos, não promessas. Nada de resultado garantido, escassez inventada ou prova social sem autorização.
- **Fonte e data de cada dado** (por exemplo, "[Hotmart, 26/11/2026]", "[manual, 17/09/2026, reconfirmar]"). **Enquanto o dono não confirmar um dado marcado "reconfirmar" ou "aguardando confirmação", a closer usa só a versão mínima autorizada** (por exemplo, "garantia de 7 dias com reembolso") e **não resume nem complementa**; em treino, o dono aprova a resposta.
- Campos marcados com (obrigatório) precisam estar preenchidos antes de ligar a closer.
- Revise a ficha sempre que preço, frete, link, prazo, cupom, promoção, garantia, bônus ou esteira mudar. Registre a data da revisão.
- Este modelo é geral. Substitua os trechos entre colchetes.
- **Corpo e anexo:** o **corpo** da ficha é o que a closer lê. Campos **internos** (**códigos de cupom, preço mínimo, quem aprova, cupons públicos antigos e de teste**) vão num **anexo interno** que **não é colado**. **Os links que carregam código na URL** ficam **só na seção de links do Conhecimento**.
- O **"dono"** é quem decide (no Up, o Anderson). O especialista do produto é o cliente.

---

## 0. Identificação da ficha (obrigatório)

- Nome interno do produto: [ ]
- Expert ou marca: [ ]
- Versão da ficha e data da última revisão: [ ]
- Quem preencheu e quem aprova mudanças: [ ]
- Projeto no Up e tags de abandono do produto (carrinho e Pix/boleto vencido): [ ]

## 1. Nome e promessa real do produto (obrigatório)

Instrução: escreva o que o produto **entrega**, não o que a pessoa vai ganhar. Sem garantia de resultado.
- Nome oficial (como aparece no checkout): [ ]
- Promessa real, em 1 a 2 frases: [ ]
- Em uma frase simples, para quem pergunta "o que é isso?": [ ]

## 2. Para quem serve e para quem NÃO serve (obrigatório)

Instrução: a seção "não serve" é a base do teste da vida melhor. Seja honesto.
- Serve para (perfil, momento, nível): [ ]
- **NÃO serve** para: [ ]

## 3. O que entrega (obrigatório)

- Formato (curso gravado, ao vivo, mentoria, comunidade, material, kit físico, outro): [ ]
- Duração e carga horária estimada: [ ]
- Tempo de acesso: [ ]
- Plataforma e como o acesso chega: [ ]
- **Produto físico:**
  - **O frete é incluso ou cobrado à parte?** [ ] (resultado de teste de checkout, com CEP, valor, prazo e data do teste)
  - **Valor e prazo do frete por região** (o checkout varia por CEP; o que **não** foi testado fica "NÃO TESTADO"): [ ]
  - **O cupom abate o frete?** [ ]
  - **Frase de frete a usar com todo preço** (se cobrado à parte, por exemplo "mais o frete, calculado pelo CEP no checkout"): [ ]
  - **Frases proibidas sobre frete:** "frete grátis", "frete incluso" (salvo se confirmado).
  - **Prazo:** o que a closer pode dizer (por exemplo, "a previsão aparece no checkout depois do CEP, e o rastreio chega por e-mail, direto da plataforma"). **Prazos de páginas ou manuais que divergem do checkout ficam como "informação da página, a reconfirmar" e a closer não os cita.**
- Suporte incluso (existe? como? em que prazo?): [ ]
- Requisitos: [ ]
- O que **não** está incluso: [ ]

## 4. Escada de ofertas (obrigatório)

Instrução: liste todas as ofertas que a closer pode **apresentar para venda**, **na ordem em que ela deve considerá-las**. Cada oferta tem seu **link ou checkout próprio, escrito no Conhecimento**. A closer nunca oferece algo que não esteja aqui. Dados **não reconfirmados** entram como "reconfirmar" e **não ficam ativos**. Uma oferta pode ficar **BLOQUEADA** pelo dono. (As ofertas que o comprador só recebe **depois** de comprar ficam na seção 4.2.)

| Ordem | Tipo (principal, alternativa, versão menor ou downsell, upsell) | Nome da oferta | Link ou checkout (como está no Conhecimento) | Quando apresentar | Quando NÃO apresentar | Status (ativa, aguardando reconfirmação, BLOQUEADA) |
|---|---|---|---|---|---|---|
| 1 | Principal | [ ] | [ ] | [ ] | [ ] | [ ] |
| 2 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

Regras da escada:
- Quando a closer pode descer para a versão menor: [ ]
- Quando a closer escolhe entre versões **equivalentes** (pelo uso, não pelo preço): [ ]
- Quando a closer pode oferecer **upsell da escada** (oferta que ela vende com link próprio, só depois da decisão de comprar a principal): [ ]
- O upsell **nunca** é condição para comprar a principal: [confirmar]

### 4.1 Detalhe de cada oferta (repita o bloco para cada linha da escada)

**Oferta: [nome]**
- Preço de tabela (**e se inclui ou não o frete**): [ ]
- **Exemplo com frete** (CEP de teste, valor do frete, previsão, total à vista, parcela e total parcelado; data do teste): [ ]
- Formas de pagamento **reais** (marque o que existe): cartão à vista [ ] Pix [ ] boleto à vista [ ] cartão parcelado [ ] cartão recorrente [ ] outra: [ ]
- Formas que **NÃO existem** (por exemplo, "boleto parcelado NÃO existe"): [ ]
- Parcelamento: nº máximo de parcelas [ ]; valor de cada parcela [ ]; **total parcelado** [ ]; cobrança **fixa e não assinatura**? [ ]; o que acontece sem limite no cartão [ ]
- Texto aprovado para explicar o parcelamento (**preço final por último, com o total parcelado e o aviso de frete**): [ ]
- O que está incluso: [ ] ; o que **não** está incluso: [ ]
- Link ou checkout (**sem código** na ficha; o link com código fica no Conhecimento): [ ]
- Confirmar que o parâmetro que aplica desconto ou modo de checkout **sobrevive** à UTM e ao `sck` do Up: [ ]

### 4.2 Esteira pós-compra (o que a IA pode informar)

Instrução: ofertas que o comprador recebe **depois** de comprar (um order bump no checkout, ou a oferta de um segundo produto). A closer **só informa** (nunca vende com isso) e **só se você confirmar abaixo que elas realmente aparecem** para quem compra pelo link e pela forma de pagamento que a closer usa. Se não há esteira, escreva "NÃO HÁ esteira pós-compra". **O dono remove a linha da esteira da ficha quando o teste vencer.**

**Regras padrão de citação:**
1. **Order bump:** a closer **só cita se a pessoa pedir mais unidades**.
2. **Upsell ou segundo produto:** **só se a pessoa perguntar o que vem depois da compra**, **só com fatos** e **SEM preço** até o teste (links e formas de pagamento) estar registrado aqui. **Texto a usar:** [ex.: "Depois da compra pode aparecer uma oferta do {produto 2}, um curso online separado e opcional. Não consigo garantir que apareça, nem passar valores por aqui."]
3. **"Dúvida de valor percebido" NÃO é gatilho.**
4. **Qualquer sinal de caixa** ("caro", "parcela", "apertado", "limite") **bloqueia a esteira pelo resto da conversa.**
5. **Nunca** como razão para decidir hoje; **nunca** pedir para comprar o principal "para ter acesso"; **sem** "confidencial", "exclusiva" ou "para aproveitar".
6. **A proativa não existe** sem decisão explícita do dono.

Repita o bloco para cada oferta da esteira:

**Oferta da esteira: [nome]**
- Tipo: [order bump ou upsell ou downsell]
- Preço e **pode citar preço?** [não, até o teste / sim, depois do teste]
- **O frete dessa oferta física está confirmado?** [sim / NÃO CONFIRMADO (a closer diz "o frete eu confirmo")]
- Validade real: [ ]
- Onde e quando aparece: [ ]
- **CONFIRMAÇÃO de que aparece para quem compra pelo link da closer** (quem testou, quando, em qual link e forma de pagamento): [ ]
  - **Resultado por link:** tabela [ ], cupom menor [ ], cupom maior [ ], promoção pública [ ]
  - **Resultado por forma de pagamento:** cartão [ ], Pix [ ], boleto [ ], PayPal [ ] (o que **não** foi testado fica "NÃO TESTADO")
- **A closer só cita a esteira se o link e a forma de pagamento da pessoa estiverem confirmados aqui.**
- **Data do último teste e prazo de revalidação:** [ ]. **Teste vencido: a closer não cita.**
- **Gatilho de citação:** [ ] Bump: só se a pessoa pedir mais unidades. [ ] Upsell: só se perguntar o que vem depois, sem preço. [ ] Proativa (decisão explícita do dono: [ ]).
- O que a closer **pode dizer** (texto aprovado): [ ]
- **Até onde revelar:** só a existência [ ] / existência e fatos [ ] / existência, fatos e preço (só depois do teste) [ ]
- Condições: some se comprar por outro caminho? [ ]. Prazo depois da compra? [ ]

## 5. Regras de preço, condições, cupons e promoções (obrigatório)

Instrução: aqui você define em que casos a closer pode usar um preço, condição ou cupom **diferente** da tabela. **O que não estiver listado, a closer não oferece: ela entra no modo "Aguardar aprovação" (seção 16).** **Códigos de cupom, cupons públicos antigos e cupons de teste ficam só no anexo interno.**

A closer só usa uma condição ou cupom se **as três** forem verdadeiras: (a) o **gatilho de uso** permite, (b) o **critério objetivo** foi cumprido, (c) a **validade** está vigente na data e hora do atendimento.

**Gatilho de uso** (uma opção por cupom) [A DECIDIR por produto]: **"Só se a pessoa pedir"** (padrão) / **"Pode oferecer na barreira de preço ou caixa"** (com o critério objetivo) / **"Critério livre da IA dentro de limites"** (só dentro do critério objetivo).

**Critério objetivo e testável (nunca depende de emoção inferida).** Todas verdadeiras:
- [ ] A **pessoa disse** que o obstáculo é o **preço** e **confirmou**.
- [ ] A closer **já tratou valor e formas de pagamento com fatos**.
- [ ] O **link de tabela já foi oferecido e não foi aceito**.
- [ ] **Não há promoção pública vigente** (ver abaixo) e a **validade** está vigente.
- [ ] **O Up confirma** quantos links de desconto já foram enviados a esta pessoa e a **data e a hora de agora**.
- [ ] **Nunca depois de "vou pensar" ou "não"**, nem na primeira mensagem.

| Nome do cupom | Gatilho de uso | Critério (resumo) | Preço final, total parcelado e aviso de frete | Ordem | Máximo de links por pessoa | **Preço mínimo (INTERNO)** | **Quem aprova (INTERNO)** | **Fim de validade** | Link (**no Conhecimento**) | Estado (ativo, a encerrar, BLOQUEADO) |
|---|---|---|---|---|---|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

**Regras de ordem, limite e fala** (valem em qualquer gatilho):
- [ ] **Cupom menor primeiro**; o **maior** só se, **depois do menor**, a pessoa **continuar falando de preço**; **nunca depois de "vou pensar" ou "não"**. Nunca revelar o maior antes do menor.
- [ ] **No máximo [2] links de desconto por pessoa**; **a promoção pública não conta como link de desconto da escada**; **nunca reiniciar com conversa nova, nunca um 3º.**
- [ ] **A plataforma de pagamento pode não limitar usos por e-mail**: o limite só é controlado pelo Up e pela closer. Como o Up garante: [ ]
- [ ] **Em automático, o cupom fica DESLIGADO até o Up entregar a ficha da pessoa e o braço sorteado.** **Sem ficha da pessoa confirmando zero links anteriores, a closer oferece só o link de tabela ou o público vigente.** Em treino, o dono confere.
- [ ] A closer cita **o preço final por último, com o total parcelado e o aviso de frete**.
- [ ] Se perguntarem **"tem outro cupom?" depois do primeiro**, a closer **não afirma que ele é o único** e faz **pergunta de diagnóstico**.
- [ ] **Cada uso é registrado**; métricas: uso de cupom, margem, reembolso, ponto de equilíbrio.
- [ ] O **fim de validade do cupom existe, mas não é urgência: a closer não cita a data.**

**Plano de lançamento em fases:** fase atual [0, treino / 1, teste sorteado (sem contato, tabela, menor, maior) / 2, liberado]: [ ]. Critério e volume mínimo: [ ]

**Promoção pública vigente (o dono preenche e mantém)**
- Existe promoção pública vigente? [sim / não]. Preço público, **link da promoção** e **data de fim de cada promoção**: [ ]
- **Regra única:** com promoção pública vigente **e o link dela no Conhecimento**, o **"link de tabela" é o link da promoção vigente**, **em todas as vias** (pedido de link, espera, mensagens). **Sem o link da promoção no Conhecimento, a closer não envia link de nenhuma oferta** (Aguardar aprovação ou Transferência).
- **Nesses períodos, os cupons da closer NÃO são oferecidos** (a closer nunca vende acima do preço público).
- A closer **nunca afirma que "{preço de tabela} é o único preço"**.
- **"Até quando vai esse preço?" ou "tenho que decidir hoje?"**, **só se perguntarem**: com promoção vigente, "Pelo que está registrado aqui, essa condição pública vai até {data do Conhecimento}. Depois disso não sei qual valor vale. A decisão é sua."; **sem** promoção, "Não conheço nenhum prazo para essa oferta." **Nunca proativa**, sem "última".

**Preço mínimo (margem unitária):** preço menos custo do produto, frete e taxas. **Não pode ser derivado do cupom.** Custos: [ ] → margem unitária: [ ]

**Como gerar um link especial** (passo a passo, e quem gera): [ ]

**O que a closer NUNCA pode oferecer:**
- Desconto, preço, cupom ou condição fora da tabela acima, com gatilho não liberado, fora do critério, vencido, ou **acima do preço público vigente**.
- Bônus fora da seção 8; garantia diferente da seção 7; parcelamento diferente do descrito.
- Reembolso fora do que a seção 7 prevê.
- **Código de cupom, preço mínimo e quem aprova** (internos).
- [acrescentar]: [ ]

## 6. Políticas de preço: o que **não** fazer

- [ ] Nunca citar preço "de" e "por" se o preço de tabela nunca foi praticado de verdade.
- [ ] Nunca citar **preço sem o aviso de frete** (quando cobrado à parte).
- [ ] Nunca usar o fim de validade de cupom como urgência; nunca "tenho outro cupom maior" nem "o cupom é o único".
- [ ] Outras restrições: [ ]

## 7. Garantia (obrigatório)

Instrução: se **não existe** garantia, escreva "NÃO EXISTE garantia". **Quando existir, a closer só diz o que a ficha libera.**
- Existe garantia? [sim / NÃO EXISTE]
- **Texto mínimo liberado** (o que a closer pode dizer **enquanto o texto completo não estiver confirmado**; por exemplo, "garantia de 7 dias com reembolso"): [ ]
- **Texto completo** (prazo, de quando conta, condição do produto, o que não cobre, como pedir): [ ]
- **Estado do texto completo:** [CONFIRMADO em {data} / **AGUARDANDO CONFIRMAÇÃO DO DONO** (prioridade 1)]. Enquanto aguardar: a closer **não resume nem complementa** condições; em treino o dono aprova a resposta.
- Prazo e **a partir de quando conta** (compra ou recebimento): [ ]
- Condições e o que **não** cobre: [ ]
- Como pedir (canal e e-mail): [ ]
- **Frases proibidas:** "teste sem risco", "se não gostar, devolve", "se você não sentir resultado em X dias".
- **Validação jurídica:** a condição do texto completo (por exemplo, "produto sem uso") é compatível com o direito de arrependimento do consumidor? [A VERIFICAR com assessoria jurídica]
- Política de reembolso: o pedido de reembolso é sempre transferido a um humano.

## 8. Bônus reais

Instrução: liste só o que **de fato** é entregue. Se não há, "NÃO HÁ bônus". Valores em reais de bônus só com autorização. **Use "grupo de alunos" e não "grupo exclusivo" ou "canal exclusivo"** (palavra proibida).

| Bônus | Está em qual oferta | Condições | Prazo | Como é entregue |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] |

## 9. Prazos, vagas e itens da página não confirmados

- Existe prazo de oferta? Data e hora de fim: [ ]; como verificar: [ ]
- Existe limite de vagas? [ ]
- **Itens da página ou do checkout que o dono ainda NÃO confirmou** (por exemplo, cronômetro, "estoque limitado", números de alunos), **inclusive os que aparecem na página que a closer envia**: [listar]. **Para cada um: ou o dono dá a prova, ou remove da página.**
- Resposta-padrão: ver §12.

## 10. Prova social autorizada

Instrução: só com autorização documentada e data. **Números de alunos ou de vendas só com extrato da plataforma.** O que aparece em manuais ou na página sem autorização fica "NÃO AUTORIZADO".

| O que pode ser citado | Data | Autorização / fonte (extrato) | Pode citar o nome? | Observação |
|---|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] | [ ] |

## 11. Objeções específicas do produto e a resposta factual

Instrução: objeções gerais já estão no playbook. **Indique a origem** (conversa real ou mapeamento, com data). As "evidências" genéricas de árvores de objeção não entram sem prova autorizada.

| Objeção frequente | Origem | Resposta factual (só fatos da ficha) | O que a closer pergunta depois |
|---|---|---|---|
| [ ] | [ ] | [ ] | [ ] |

## 12. FAQ, respostas-padrão e frases proibidas

### 12.1 FAQ
| Pergunta | Resposta aprovada |
|---|---|
| [ ] | [ ] |

### 12.2 Respostas-padrão (a closer segue ao pé da letra; textos vêm da copy aprovada)
| Situação | Resposta |
|---|---|
| "Vi mais barato" ou "vi R$ X" | Com promoção vigente: usar só a condição pública (enviar o link dela). Sem promoção ou sem link: frase de espera (X1) e escalar. Nunca "o único preço" |
| Cronômetro, "estoque limitado", números de alunos da página | "Essa informação da página eu não consigo confirmar. Posso te confirmar {fato da ficha}. Não conheço nenhum prazo para essa oferta." |
| "Se eu comprar, o curso complementar fica mais barato?" | "Não consigo prometer o que aparece depois da compra. Posso te confirmar {fato da ficha}." |
| "Tenho que decidir hoje?" / "Até quando vai esse preço?" | Ver §5 (promoção vigente ou "Não conheço nenhum prazo para essa oferta.") |
| "É robô?" | "Sou a {nome_closer}, assistente virtual. Se preferir falar com uma pessoa da equipe, eu te passo." |
| "Tô desempregado" ou aflição | Acolher em uma frase, sem oferta, Transferência |
| "O {nome} liberou {desconto}" | Frase de espera (X1) e Aguardar aprovação (ou Transferência) |
| "Quanto é o frete?" / "É frete grátis?" | Frase de frete da §3; nunca "grátis" nem "incluso" |
| Garantia (qualquer pergunta) | Só o texto liberado da §7 |

### 12.3 Frases proibidas (a closer nunca escreve)
"melhor condição", "a condição disponível é aquela", "última", "só pra você", "liberei", "consegui liberar", "falei com a equipe", "só hoje", "última chance", "exclusivo", "exclusiva", "confidencial", "para aproveitar", "tenho um cupom maior", "teste sem risco", "se não gostar, devolve", "se não funcionar, devolve", "frete grátis", "frete incluso" (salvo confirmado), e **qualquer prazo ou data como pressão**. Acrescente as do produto: [ ]

## 13. Insight para ensinar (opcional)

- Insight (1 a 2 frases): [ ]. Fonte: [ ]. Quando usar: [ ]

## 14. Dúvida frequente para texto de follow-up (opcional)

- Pergunta frequente: [ ]. Resposta factual: [ ]

## 15. Quando NÃO vender (obrigatório)

**Estas situações valem também quando a pessoa pede o link: a closer não envia o link e transfere ou encerra.**
- A pessoa não se encaixa em "para quem serve": [ ]
- A pessoa busca algo que o produto **não** faz: [ ]
- Dificuldade financeira séria, crise emocional ou **vulnerabilidade emocional explícita**: acolher em uma frase, não oferecer nada, transferir; nunca usar como alavanca.
- Menor de idade: transferir.
- Já comprou: pós-venda.
- **Problema aberto** com compra anterior: resolver ou transferir antes de vender.
- Outros: [ ]

## 16. Escalonamento: dois modos e gatilhos específicos deste produto

**Modo 1: Aguardar aprovação.** A closer **não vende nem negocia**, responde só fatos da ficha e avisa a pessoa. Usado para: pedido fora da ficha, desconto ou cupom não liberado, condição especial, autoridade alegada, cupom citado que a ficha não lista, promoção pública sem link vigente no Conhecimento, dado NÃO CONFIRMADO. **Depende de o Up abrir o pedido ao dono e devolver a decisão: se não tiver, a closer usa a frase de Transferência (nunca "te respondo aqui").** [A VERIFICAR]
- Quem recebe o pedido e em que canal: [ ]; **SLA:** [ ]
- **Frases de espera (da copy aprovada):** **X1** (primeira vez): "Isso eu prefiro confirmar pra não te passar errado. Vou verificar e te respondo aqui." **X1b** (vezes seguintes): "Isso também eu confirmo e te respondo aqui." **X2** (SLA estourado): "Ainda estou aguardando a confirmação. Te aviso assim que souber." [editar com o dono]
- **Se a pessoa pedir o link durante a espera:** envia o **link de tabela** (ou o da promoção vigente), dizendo que é o valor de tabela e que a verificação segue.
- **Quem retoma depois da aprovação:** o Up devolve a conversa à IA com a **decisão do dono**; formato e canal: [ ]. Se a decisão chegar depois de a janela de 24 h fechar, a mensagem **não sai**.

**Modo 2: Transferência.** A closer escreve **uma única frase de passagem, sem prazo e sem pergunta**, e fica **em silêncio**. **Frase padrão (9a da copy):** "Isso é melhor alguém da equipe ver com você. Vou passar a nossa conversa pra essa pessoa, e te respondem por aqui mesmo." Há variantes para reembolso, reclamação, dificuldade financeira, fora do Brasil e "já paguei" ou "não recebi" (copy blocos 8 e 9). Usado para: reembolso, reclamação, ameaça ou Procon, dado sensível, crise ou vulnerabilidade emocional, menor de idade, golpe, pedido de humano, loop, erro de pagamento, nota fiscal ou compra em nome de empresa, "já paguei" ou "não recebi", acesso ou entrega, pergunta que a ficha não responde, condição que não existe e a pessoa insiste, "quando NÃO vender".
- **Estes gatilhos prevalecem sobre o pedido de link.**
- Gatilhos específicos deste produto: [ ]; quem recebe: [ ]
- Resumo entregue ao humano (o Up monta): quem é, produto, onde parou, barreira dita, o que foi oferecido, o que foi pedido, urgência e motivo.

## 17. Operação (obrigatório)

**Fatos do sistema (Up)** [SISTEMA, informado em 13/11, reconfirmar]: espera de 30 min, **só entre 8h e 21h**; encerra se comprou qualquer versão; aviso por **modelo UTILITY** com botão "Ver detalhes"; a Camila entra depois do clique ou da resposta, **janela de 24 h**; conversa de **48 h**; regras R1 a R5; **não mudar R3 e R4 sem dado**; **"sair" é a única palavra de saída reconhecida hoje**; link só do Conhecimento, com UTM e `sck=camila`; modo treino; o dono pode assumir. **A confirmar** [A VERIFICAR]: "Aguardar aprovação"; ficha da pessoa e **data e hora de agora** entregues à Camila; **braço sorteado**; evento de cartão recusado; conferência de compra por e-mail OU telefone normalizado antes de cada texto livre.

**Identificação e canais**
- Nome da closer: [ ]. A **primeira mensagem** se identifica como assistente virtual.
- **Opt-out:** "Se preferir que eu não escreva mais, é só responder SAIR." (o Up só reconhece "sair"; ampliar para linguagem natural é pendência)
- **Modelo(s) UTILITY de abertura** (nome, texto aprovado, **categoria atual**, estado): [ ]
- Política de ligação: [ ]
- Canal de **suporte pós-compra** (e-mail ou link, horário, prazo): [ ]
- Como o acesso chega depois do pagamento: [ ]

**Cadência**
- O aviso e as regras de recontato são do Up. **Follow-ups por tempo não existem no sistema**; **as retomadas por tempo da copy (5.2, 5.3, 7a e 7b) só valem se o Up disparar o toque.** Agendador de retornos: [sim / não].

**Textos-base (da copy aprovada)**
- **Abertura 1A:** "Oi, {nome}! Sou a {nome_closer}, assistente virtual, sobre o seu pedido do {produto}. O que ficou faltando pra você finalizar? Se preferir que eu não escreva mais, é só responder SAIR." (uma pergunta)
- Abertura para Pix/boleto vencido (1D), despedida (7a), via 2 ("Quer que eu te mande o link?"), retomadas e frases de passagem: [apontar a copy aprovada]

## 18. Checklist antes de ativar a closer neste produto

- [ ] Seções 0, 1, 2, 3, 4, 5, 7, 15, 16 e 17 com campos obrigatórios completos.
- [ ] Seções 8, 9, 10 e 4.2 preenchidas ou marcadas com "NÃO HÁ".
- [ ] Cada dado tem **fonte e data**; dados antigos estão "reconfirmar", e a closer usa só a versão mínima autorizada.
- [ ] A ficha e **todos os links** estão no **Conhecimento** (os com código só lá); testados, **aplicam** o desconto quando devem, mostram oferta, preço e **frete** corretos **depois** da UTM e do `sck`.
- [ ] Parcelamento, **frete por região** e **total parcelado** conferidos no checkout real.
- [ ] **Promoções públicas** com link e **data de fim** no Conhecimento.
- [ ] Prova social com data e autorização; números com extrato; **itens da página não confirmados: prova ou remoção**.
- [ ] Esteira testada por link e por forma de pagamento; data do último teste; preço do upsell só depois do teste.
- [ ] Cupons: critério objetivo, limite de links, escalonamento, validade, plano em fases; **o Up entrega a ficha da pessoa, o braço sorteado e a data e hora (senão o cupom fica desligado em automático)**.
- [ ] **Margem unitária** preenchida.
- [ ] SLA combinado e formato de devolução da decisão definido (ou o Up usa Transferência).
- [ ] **Os 25 testes de aceitação** (`camila-testes-aceitacao.md`) aprovados: 100% em 2 rodadas seguidas, cada teste rodado pelo menos 3 vezes por rodada.
- [ ] Revisão pelo `revisor-vendas` e jurídica.
- [ ] Data da próxima revisão: [ ]

Regra final: **na dúvida, a closer não afirma e escala.**

**O que bloqueia o treino hoje:** [ ]
**O que bloqueia o automático:** [ ]
