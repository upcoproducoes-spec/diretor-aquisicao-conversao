# Framework — Estrutura de página (captura, obrigado, vendas e o que vem depois do clique)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered das páginas que a casa pôs no ar ao longo de uns três meses, dos documentos de estrutura que vieram junto e do que o Rodrigo decidiu ou explicou sobre página em reunião. Base: 28 páginas no ar de um cliente (24 unidades, juntando as versões da mesma página), em 4 funis, mais uma página de VSL de outro cliente.

> **ALCANCE: NÃO TESTADO FORA.** Captura, lista, obrigado, venda, carta, aulas, lives e link da bio
> vêm de um cliente só (o caso-base, um expert de educação): 28 páginas no ar (24 unidades), de 4 funis
> (um lançamento gratuito, o LPSG, a Black e o perpétuo do link da bio). A página de VSL vem de um segundo
> expert da casa, uma página só. A lição de conferência de clone nasceu numa página de um SaaS, produto de
> outra empresa do Rodrigo. Nenhuma página teve teste A/B rodado, e a conversão por página não está medida
> nos debriefings. Ao aplicar no negócio de vocês, ler a §10 e dizer na entrega que a estrutura ainda não
> foi testada aqui (`sirius-scale/REGRAS.md` §4).
>
> **O que este arquivo é:** a estrutura (que tipo de página, que blocos, em que ordem, o que cada um
> carrega, pra onde o clique leva) e a conferência antes de publicar. **O que ele não é:** copy. Texto
> de página é sempre do agente `copy`, com o `/humanizer` depois (`sirius-scale/REGRAS.md` §3); aqui
> fica o que o bloco precisa conter, não a frase.
>
> **Vizinhos, que este arquivo cita e não repete:**
> - como publicar, formulário por dentro, pixel, domínio e receita de clone:
>   `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` e
>   `sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md`;
> - o padrão do HTML (um arquivo, CSS no `<style>`, mobile-first, imagem como slot com prompt): o agente
>   `webdesigner` (`.claude/agents/webdesigner.md`);
> - o bloco de oferta: `sirius-scale/frameworks/oferta-14-secoes.md`;
> - a ordem da página de venda e da VSL (Lead, História, Tese, Oferta): `sirius-scale/frameworks/lhto.md`;
>   como a página abre, pelo nível de consciência do público: `sirius-scale/frameworks/copy/great-leads.md`;
> - a página de low ticket (13 blocos): `sirius-scale/frameworks/lancamentos/low-ticket.md` §5 e §12 a §14.5;
> - o destino do clique por fase: `sirius-scale/frameworks/copy/criativos.md` §0.9.
>
> **Publicar, do lado de vocês.** A casa publica por um script próprio, que não vem no kit. Vocês publicam
> pelo Lovable ou pela hospedagem de vocês. Onde este arquivo fala em publicar, vale o checklist de antes
> da produção do `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2 (subir só o que foi
> aprovado, conferir que nenhum bloco ficou escondido, ler de volta no endereço publicado), feito à mão ou
> pedido ao Claude. Página de Lovable nasce no JavaScript, e isso muda a conferência
> (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §10).
>
> Contagens e rótulos são os da base completa da casa; alguns dos casos não aparecem neste kit.

---

## 0. Escopo e base de evidência

### 0.1 Fontes

| Fonte | O que é | Unidades | Peso |
|---|---|---:|---|
| **A** | Páginas no ar do caso-base, numa hospedagem estática (Cloudflare Pages), com o manifesto do que está publicado e o log de publicação. 17 copiadas com fidelidade do WordPress de uma vez (feitas antes pelo designer da casa), 2 do segundo WordPress (o das páginas de venda), poucos dias depois, e as que a casa montou nas semanas seguintes (a lista VIP do LPSG; as da Black; low ticket, bio e lista de espera do programa principal) | 34 endereços; 28 entram aqui | forte: foi ao ar, e as publicações mais recentes têm no log o pedido do Rodrigo ou da gerente de operação |
| **B** | Documentos de estrutura e copy de página com decisão registrada: os da Black (cadastro, obrigado, notas, vendas e a troca de CTA das lives), a copy da inscrição do LPSG, os da bio (lista de espera e bio) e a estrutura da página de aquecimento do lançamento gratuito; mais os montadores das páginas (bio, página de low ticket, links de checkout) e o briefing do lançamento gratuito | 10 documentos | forte onde virou página no ar; médio na página de vendas da Black (não tinha ido ao ar) |
| **C** | Fala do Rodrigo em reunião (transcrição): 7 reuniões em pouco mais de duas semanas. Quatro dessas são ele explicando a própria prática pra gente de fora da casa | 7 reuniões | forte |
| **D** | Memórias de correção e decisão do Rodrigo: animações do original, clone se confere rolando, o que vai pra validação do expert, duplicar a última peça aprovada, depoimento só com print real (arte estática), promessa flexível em teste A/B, home nova, linha de low ticket, frente de páginas no WordPress e publicação de página liberada | 10 memórias | forte |
| **E** | Página de VSL do perpétuo do livro de um segundo expert da casa: o checklist do funil e o debriefing do perpétuo (§3 de lá) | 1 página | forte pra "rodou" (164 livros); a página em si não está nos arquivos da casa |
| **F** | Clone de uma página de captação de um SaaS (produto de outra empresa do Rodrigo), o texto dela e o diagnóstico daquele funil (§6 de lá) | 1 página | a estrutura e a copy são do time do SaaS; entra só pela lição de conferência e pelo diagnóstico |
| **G** | Números ligados a página: taxa de resposta da pesquisa do obrigado (lançamento gratuito), vendas de quem respondeu (o lançamento gratuito anterior), visita → ingresso na inscrição do LPSG (uma turma), página da VSL do segundo expert, a página do SaaS | 5 medições | forte, cada uma com a fonte citada onde aparece |

Os lançamentos aparecem aqui pelo papel, não pelo código: **o lançamento gratuito** é o mais recente do caso-base (o da captura que serviu de molde pra Black); **o lançamento gratuito anterior** é o que veio antes dele; **o LPSG** é o funil de evento pago semanal, com uma turma por semana (`sirius-scale/frameworks/lancamentos/lpsg.md`); **a Black** é a Black de colheita do caso-base (`sirius-scale/frameworks/lancamentos/black-da-casa.md`).

As 28 páginas da Fonte A, por tipo:

| Tipo | Páginas | Funis |
|---|---|---|
| Captura de evento gratuito | a captura do lançamento gratuito; a da Black, em três versões (aluno, não aluno e bio) | lançamento gratuito, Black |
| Captura de lista | a lista VIP do lançamento gratuito; duas listas VIP do LPSG (uma com data, uma fixa); a lista de espera do programa principal | lançamento gratuito, LPSG, perpétuo |
| Obrigado | com pesquisa: o do lançamento gratuito, o do ingresso do LPSG e o da Black em duas versões (aluno e não aluno); de lista: o da lista VIP, o da lista do LPSG e o da lista de espera | lançamento gratuito, LPSG, Black, perpétuo |
| Venda | a de reabertura do programa principal, a do downsell (um curso menor) e a de venda do ingresso do evento pago | lançamento gratuito, LPSG |
| Carta de pré-abertura | a do lançamento gratuito e a do LPSG | lançamento gratuito, LPSG |
| Aulas e lives | as 4 páginas de aula e a página de lives do lançamento gratuito | lançamento gratuito |
| Link da bio | o hub novo da bio, nas versões do Instagram e do YouTube, e a página de links antiga da bio do YouTube | perpétuo |

**Deduplicação.** Versões simultâneas da mesma página, pra públicos ou canais diferentes, contam como uma unidade, porque o método não conta a mesma peça duas vezes: as três versões da captura da Black, as duas do obrigado da Black e as duas do hub da bio (Instagram e YouTube, montadas do mesmo registro). Páginas de turmas ou lançamentos diferentes contam separado. Por isso são 28 páginas e 24 unidades, e as contagens abaixo são por unidade.

### 0.2 Excluído de propósito

1. **Página de low ticket (13 blocos).** Já está em `sirius-scale/frameworks/lancamentos/low-ticket.md` §5, §12, §13, §14 e §14.5 (metodologia externa de um vendedor de low ticket, com as adaptações da casa e a primeira aplicação). A copy e os montadores das páginas foram lidos; o que ensinam de estrutura já está lá. As 4 páginas no ar (os quatro guias da linha) contam aqui só como evidência de regra transversal.
2. **O bloco de oferta por dentro.** É o `sirius-scale/frameworks/oferta-14-secoes.md`. Aqui só aparece onde ele entra na página.
3. **Como publicar, o formulário por dentro, pixel, domínio, UTM e receita de clone.** Moram no `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md`, no `sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md` e no `sirius-scale/frameworks/trafego/nomenclatura.md`.
4. **Copy de cada bloco.** É do agente `copy` (`sirius-scale/REGRAS.md` §3).
5. **Páginas de upsell e downsell pós-checkout e o roteiro da VSL.** Têm framework próprio: `sirius-scale/frameworks/lancamentos/upsell-e-downsell.md` (as páginas, §4.13) e `sirius-scale/frameworks/copy/producao-de-vsl.md`. Daqui sai só a casca da página de VSL (§4.10).
6. **Obrigado de compra do low ticket.** Existe a proposta (no plano de pós-compra da linha) e a copy v1, nunca publicadas. Fraco; vai pra §11.
7. **Home nova do caso-base.** Prévia não publicada. O que o Rodrigo decidiu numa reunião com o expert entra na §4.9 como variação, e o resto na §11.
8. **Variantes B e C da inscrição do LPSG.** Estão publicadas no endereço, mas não foram aprovadas: o backlog de ideias da casa registra que "o Rodrigo disse que ainda não estava gostando" da B, e a C tem texto provisório. Não sustentam regra.
9. **Rascunho da captura da Black** (bloqueado no manifesto de publicação). Virou as três versões da captura da Black.
10. **Páginas de outros donos:** as de um cliente de outra empresa (feitas pelo time dele; a casa só tem os textos de referência e roteiro de vídeo), estruturas que terceiros explicaram em reunião e páginas citadas de passagem. Não são página da casa.
11. **Telas de um app de produto e as páginas legais do SaaS.** Produto e página legal, sem estrutura de conversão.

### 0.3 Ressalva da base

- **Um cliente, quatro funis.** Tudo, menos a VSL, é do caso-base, num intervalo de uns três meses.
- **Repetição por duplicação.** As páginas de lançamento nasceram no WordPress e foram copiadas com fidelidade; a Black saiu da cópia da captura do lançamento gratuito. Quando o mesmo esqueleto aparece em dois lançamentos, isso mostra que a casa escolheu mantê-lo, não que ele foi testado contra outro.
- **Nenhum A/B rodou.** O da inscrição do LPSG foi adiado (evidência no caso de origem).
- **Conversão de página não medida.** Os debriefings dizem com todas as letras: o do lançamento gratuito (§17 de lá) e o de três turmas do LPSG (§14 de lá).

### 0.4 Veredito da base (FASE 1 de `sirius-scale/frameworks/_extracao-de-frameworks.md`)

**EXTRAÍVEL FORTE** pelo critério de unidades (24 unidades no ar, 4 funis), **com a ressalva de cliente único** no eixo 2. Por tipo: obrigado com pesquisa (3 unidades, 3 funis) e captura de lista (4, 3 funis) sustentam padrão. Captura de evento são 2 unidades (a do lançamento gratuito e a da Black, esta em três versões) e fica como variação. Venda tem 3 páginas no ar mais a definição do Rodrigo, e sai como variação. Carta (2 de um molde), aulas (4 de um molde), lives (1), link da bio (1 molde novo) e VSL (1, outro cliente) ficam como VARIAÇÃO ISOLADA.

---

## 1. A fórmula, em ordem

O artefato aqui é um processo: montar uma página. Os passos valem pra qualquer tipo; o que muda por tipo são os blocos do passo 3.

1. **Dizer qual é a única ação da página.** O tipo sai daí: inscrever, entrar na lista, responder a pesquisa, comprar, ler a carta, assistir.
2. **Partir da última página aprovada do mesmo tipo**, trocando só o que muda.
3. **Montar os blocos do tipo, na ordem** (§4.1 a §4.10).
4. **Ligar o depois do clique** antes de escrever: pra onde o botão leva, que dado vai junto, onde a pessoa termina.
5. **Pedir o texto ao `copy`**, com o que é do expert separado do que é decisão comercial.
6. **Conferir antes de publicar:** no celular, rolando até o fim, com o formulário testado de ponta a ponta e nada vencido.
7. **Publicar e ler de volta.** Na casa, por um script de publicação (não vem no kit). Do lado de vocês, pelo Lovable ou pela hospedagem, com o checklist de antes da produção (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2): subir só o que foi aprovado, a conferência rolando do §7.1 feita antes, e a leitura de volta no endereço publicado.

Os tipos, que são os modos da fórmula: captura de evento, captura de lista, obrigado, venda, venda de ingresso, carta, aula e lives, link da bio, VSL. O que todos compartilham está na §8.

---

## 2. Passo 1 — Uma ação por página, e todo botão leva até ela — PADRÃO CONSISTENTE (proposto)

**O que entra.** Antes de qualquer bloco, a página ganha uma ação só. Todos os botões apontam pro mesmo lugar: o formulário do topo, o popup da lista ou o bloco do preço.
- Em 7 unidades todo botão leva ao mesmo lugar: as 2 capturas de evento (a da Black nas três versões), a lista de espera e as 4 de low ticket. As 3 da lista VIP têm um botão só.
- Nas 3 páginas de venda com o preço mais embaixo (as 2 de programa e o ingresso), os botões de cima descem até o bloco do preço, onde estão os de compra.
- As 2 cartas mandam os 5 botões pro popup da lista e fecham com um link pras aulas liberadas.
- As exceções claras são a página de lives e as de aula (§4.8).

No obrigado, a mesma regra vira só a pesquisa.

**Por quê.** O Rodrigo disse isso duas vezes: ao tirar as lives de aquecimento da captação da Black e ao explicar o obrigado numa consultoria. Na consultoria, a pergunta foi se o lead não ia se perder com dois lugares pra ir, e a resposta foi que não pode ter dois. Na estrutura da página de lives, o argumento pra pôr a grade no topo foi parecido: é a ação que a pessoa veio fazer.

**Variações aceitáveis.**
- O assunto pode ser maior que a ação. Dois dias depois de saírem, as quatro lives voltaram pra página da Black como programação, mas o botão continuou um só, o da inscrição na live de abertura (decisão registrada na ata da reunião com a gerente de operação).
- Link de suporte no WhatsApp no fim da página de vendas (2 de 2 páginas de venda de programa). É a segunda saída tolerada; a casa não decidiu se fica (§11).

**Trecho real.**
- Fonte B, a troca de CTA da captação da Black, mensagem do Rodrigo: "uma coisa é uma coisa, outra coisa é outra coisa, vamos manter o foco somente na inscrição para a live black. o aquecimento será comunicação à parte que pode ser até um remarketing nosso"
- Fonte C, numa consultoria, o Rodrigo, sobre mandar o lead do obrigado pro grupo: "É, aí não pode ter dois. Tipo assim, a pessoa cai na página de obrigado, só com a pesquisa direto para ele ir respondendo."
- Fonte B, a copy da página de cadastro da Black, bloco 6: "Fica no topo, dentro do BLOCO 1, como no [lançamento gratuito]. Todos os botões da página levam pra ele."
- Fonte B, a estrutura da página de aquecimento do lançamento gratuito: "é exatamente o que o anúncio pago promete e a ação que a pessoa veio fazer"

---

## 3. Passo 2 — Começar da última página aprovada do mesmo tipo — PADRÃO CONSISTENTE (proposto)

**O que entra.** A página nova é a cópia da última aprovada do mesmo tipo, com as configurações dela, e muda só o que precisa mudar (do lado de vocês, a última aprovada mora em `entregas/`). É a regra que o Rodrigo deu pra peça nova, e aparece em 4 casos de página: a captura e o obrigado da Black saíram da cópia dos do lançamento gratuito; a página de vendas da Black manda duplicar a captura da Black e toma a do lançamento gratuito anterior como referência; as páginas do segundo, do terceiro e do quarto guia de low ticket saíram do mesmo construtor da do primeiro, com a mesma conferência de estrutura; a lista VIP do lançamento gratuito foi a do anterior reaproveitada (registrado no briefing do lançamento).

**Por quê.** A peça aprovada guarda decisões que nunca voltaram pro documento. Montar do zero pelo documento traz de volta o que já tinha sido corrigido.

**Variações aceitáveis.** O que sempre muda ao duplicar, e já custou erro quando ficou:
1. tag do formulário e registro dele (`sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md`, padrão de tag; `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §3);
2. datas, cronômetro e título da aba (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §8);
3. imagem que só existe no disco (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2: dá 404 no ar);
4. o que a regra da casa não aceita mais. A cópia fiel guarda o original como estava; a derivação limpa. A captura do lançamento gratuito no ar ainda tem o aviso de "vagas limitadas" do WordPress; na Black ele saiu.

**Trecho real.**
- Fonte D, memória "duplicar a última peça aprovada": o Rodrigo "duplica a última já feita e revisada, com todas as configurações certas, e troca só o que muda"; e o porquê: "a última peça aprovada carrega todas as decisões, inclusive as que nunca voltaram pro documento."
- Fonte B, notas das páginas da lista da Black, §1: "Duplicar as duas últimas páginas aprovadas em vez de montar do zero:"
- Fonte B, notas da página de vendas da Black, §1: "A estrutura de página de vendas de referência já aprovada é a do [lançamento gratuito anterior]"
- Fonte B, notas das páginas da lista da Black, §3, sobre o aviso de exclusividade herdado: "remover. É escassez falsa"

---

## 4. Passo 3 — Os blocos, por tipo de página (força em cada tipo, de VARIAÇÃO ISOLADA a PADRÃO CONSISTENTE)

### 4.1 Captura de evento gratuito — VARIAÇÃO ISOLADA (2 unidades de um molde: o lançamento gratuito e a Black, esta em três versões)

**O que entra, na ordem.**

| # | Bloco | O que carrega | Visto em |
|---|---|---|---|
| 1 | Topo com o formulário | logo do evento; headline com a promessa; linha de informação (data, horário, gratuito); formulário com primeiro nome, e-mail e WhatsApp e o botão da ação | 2 de 2 (na versão da bio da Black, dois botões no lugar do formulário, cada um abre o seu) |
| 1a | Em volta do botão | acima, a vantagem de se inscrever; abaixo, o micro-texto de privacidade; na versão de aluno, também uma linha pra quem já é aluno | 1 de 2 (a Black) |
| 2 | O que é e o que vai ter | o que é o evento ou a oferta, e os itens com etiqueta de prazo de acesso, sem preço | 1 de 2 (a Black) |
| 3 | Programação | um card por aula ou live: data, dia, horário e o título real, e o botão | 2 de 2 |
| 3a | Caixa do aluno | "[pergunta se a pessoa já é aluna e chama pra se inscrever também]", com o que conta como aluno | 1 de 2 (a Black, nas versões de aluno e da bio) |
| 4 | Quem é o expert | bio curta com a credencial e um "Saiba mais" que abre e fecha, e o botão | 2 de 2 |
| 5 | FAQ | 3 a 4 perguntas em acordeão (preciso pagar, tem replay, recebo material; na Black, quem já é aluno, preço, prazo de acesso e se serve pro caso da pessoa) | 2 de 2 |
| 6 | Rodapé | copyright | 2 de 2 |

O esqueleto está escrito nas notas da Black, que mandam manter o do lançamento gratuito e encaixar as seções novas no meio.

**Por quê.** A ação mora na primeira tela e todos os botões descem até ela (§2). A programação diz quando é e o que a pessoa ganha ao se inscrever. Na Black, a página não mostra preço nem nome de bônus porque o preço é revelado na live de abertura, e a linha logo acima do botão transforma isso em motivo pra se inscrever.

**Variações aceitáveis.**
- **Três versões da mesma página quando a oferta muda por público** (Black): uma pra aluno, uma pra quem não é aluno (sem a caixa do aluno) e uma pra bio, com dois botões no topo que abrem dois formulários. Cada uma leva pro seu obrigado e pro seu grupo (§5.2).
- O WhatsApp no formulário. A captura do lançamento gratuito anterior não pedia telefone; da captura do lançamento gratuito em diante, pede (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.9). O motivo da troca não está registrado.

**Trecho real.**
- Fonte B, notas das páginas da lista da Black, §2, o esqueleto do lançamento gratuito: "topo com formulário, faixa, seção escura com cards"
- Fonte A, o FAQ da captura do lançamento gratuito, em molde: "[pergunta se precisa pagar pra participar]"
- Fonte B, notas das páginas da lista da Black, §3, sobre a caixa do aluno: "É a mensagem que o comprador só do ingresso precisa ver sem fazer conta"
- Fonte C, reunião com o expert do caso-base sobre o preço da Black, o Rodrigo: "aí na página vai ter dois botões, sou aluno e não sou aluno."
- Fonte C, reunião da equipe sobre os grupos da Black, sobre as três páginas: "A diferença é um só leva pro grupo de aluno, o outro só leva pro grupo de não aluno e o da bio, você escolhe se você é aluno ou não."

**Exemplos (em molde).**
- O topo da captura do lançamento gratuito: headline com o resultado, o prazo e o jeito do método ("[o resultado que o público quer] em [prazo], [com o diferencial do método]"); a linha de informação com "[datas] às [hora]" e "100% on-line e gratuito".
- A linha acima do botão, na captura da Black: "[o que só a live de abertura revela: o preço e os bônus]". E o micro-texto: "[diz que a inscrição é gratuita]. [diz pra que servem o WhatsApp e o e-mail: o link do evento e os avisos]."
- Nas notas, o motivo de a página não ter preço: o preço é o da live de abertura (§8 das notas).

### 4.2 Captura de lista (lista VIP e lista de espera) — PADRÃO CONSISTENTE (proposto) no esqueleto curto; VARIAÇÃO ISOLADA na lista de espera

**O que entra.**

| Página | Blocos |
|---|---|
| Lista VIP (3 páginas: a do lançamento gratuito e as duas do LPSG) | headline curta com a vantagem, um parágrafo com o fato verificável (o link de matrícula sai antes, a que horas e por que isso importa), formulário de três campos, botão com o horário. Mais nada. |
| Lista de espera (do programa principal) | topo com a situação (inscrições fechadas), o que a pessoa ganha (fica sabendo primeiro) e o formulário; depois o que é o programa, por que entrar na lista e uma prova de alunos, com o botão de novo |

**Por quê.** A página de lista vende uma coisa só: estar na frente. Na VIP, a vantagem é concreta (o link sai uma hora ou dez minutos antes) e tem motivo real (o brinde físico é só pros primeiros), o que o `sirius-scale/frameworks/lancamentos/cpl-3-aulas.md` já chama de micro-compromisso. Na lista de espera, quem chega pela bio já conhece o expert, então a dobra vai direto pra situação e pra ação.

**Variações aceitáveis.**
- O que a lista de espera deixou de fora de propósito: data da próxima turma, preço, desconto e bônus, porque nenhum arquivo dava vantagem à lista além de saber primeiro. E o grupo de WhatsApp saiu da página: virou formulário, com o grupo como botão opcional no obrigado (decisão do Rodrigo).
- No funil semanal (evento pago), a versão mais nova da lista VIP troca a data pelo dia da semana, pra mesma página servir toda turma; a anterior ainda trazia a data, como as do lançamento gratuito.

**Trecho real.**
- Fonte A, a lista VIP fixa do LPSG: "10 min antes". A mesma lógica na inscrição do ingresso, na copy da página: "vale pra qualquer turma, sem data fixa".
- Fonte A, botão da lista de espera, em molde: "[a ação: entrar na lista]".
- Fonte B, a copy da lista de espera: "Por isso a dobra vai direto na situação (inscrições fechadas) e na ação (entrar na lista), sem gancho de dor antes." E o que ficou fora: "Data da próxima turma, preço, desconto, bônus e condição especial pra quem está na lista."
- Fonte B, a copy das artes da bio: "a lista de espera virou formulário no Full Funnels [...], não grupo"

**Exemplos (em molde).**
- Lista VIP do lançamento gratuito: headline com "[a vantagem de chegar antes quando as inscrições abrirem]"; "[quanto tempo] antes de [todo mundo]"; botão "[a ação: receber o link] às [hora]". Na fixa do evento pago: "Na próxima [dia da semana]".
- Lista de espera: "[diz que as inscrições do [programa] estão fechadas]".

### 4.3 Obrigado — PADRÃO CONSISTENTE (proposto) no obrigado com pesquisa; VARIAÇÃO ISOLADA nos de lista

**O que entra.**

Obrigado de cadastro e de ingresso (3 unidades: o do lançamento gratuito, o do ingresso do LPSG e o da Black, em duas versões, aluno e não aluno):

| # | Bloco | O que carrega | Visto em |
|---|---|---|---|
| 1 | Título | confirma o que a pessoa garantiu e diz que falta um passo | 3 de 3 |
| 2 | Barra de progresso | em 70% | 3 de 3 |
| 3 | Motivo pra responder | por que o expert quer saber; no lançamento gratuito, com um presente pra quem responde | 3 de 3 (presente em 1) |
| 4 | Pesquisa embutida | o formulário da pesquisa dentro da página | 3 de 3 |
| 4a | Dados da captura repassados pra pesquisa | nome, e-mail e telefone, que chegam na URL do obrigado e um script põe nos campos ocultos da pesquisa | 2 de 3. O do lançamento gratuito manda o telefone com o nome errado; o do ingresso não tem o script; o da Black manda o telefone com os dois nomes |
| 5 | Depois de responder | data e hora do evento e por onde os links chegam | 1 de 3 (a Black) |
| 6 | Rodapé | copyright | 3 de 3 |

⚠️ **Armadilha medida: o nome do parâmetro tem que casar com o do campo oculto.** O obrigado do lançamento gratuito repassava o número como `telefone`, e o campo da pesquisa se chama `whatsapp`: a pesquisa ficou sem telefone em todas as 7.741 respostas, e o Dash, que pega o telefone da pesquisa, também (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.9; conferência em `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.1). O da Black, montado depois, manda os dois nomes; o nome do campo nas pesquisas da Black não está conferido nos arquivos da casa.

⚠️ **Os dados na URL vão pro pixel da Meta.** O redirect leva e-mail, nome e telefone na URL do obrigado, e o pixel manda a URL inteira em todo evento. É dado pessoal indo pra terceiro. No caso-base o achado ficou registrado e não corrigido, com o caminho: ler os dados e limpar a URL antes do pixel (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7). O conserto foi feito depois, numa página de um segundo cliente (mesmo arquivo, §11.1). Página nova de vocês já nasce com ele.

Obrigado de lista (3 páginas): confirmação, o que acontece agora (o horário do link antecipado, ou o aviso de que a pessoa fica sabendo primeiro quando a turma abrir) e a próxima ação possível (assistir às aulas liberadas, ou entrar no grupo, opcional).

**Por quê.** A pesquisa mora no obrigado porque é ali que a resposta vem alta, e a resposta alimenta o MQL, que é a régua de verba (`sirius-scale/frameworks/trafego/mql-e-qualificacao.md`). O Rodrigo explicou isso em três conversas diferentes. Os números que sustentam: no lançamento gratuito, 68,49% dos leads pagos responderam (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.1.1); no anterior, 70,7% das vendas vieram de quem respondeu (mesmo arquivo, §2.9). O repasse dos dados da captura é o que amarra a resposta ao lead, quando funciona (ver a armadilha acima). O título e a barra de 70% vieram do original do WordPress e o porquê não está registrado (§11).

**Variações aceitáveis.**
- Pós-ingresso (evento pago): o mesmo molde, com o pedido de responder pra finalizar a inscrição no lugar do presente.
- Presente pela resposta: só quando existe de verdade. Na Black não existia, e a frase ficou sem ele.
- Grupo de WhatsApp: segundo o Rodrigo, entra no fim da pesquisa, no botão de enviar da última pergunta, e não como segundo botão na página. O obrigado da lista de espera põe o grupo como botão, dizendo que é opcional.

**Trecho real.**
- Fonte A, o obrigado do lançamento gratuito, em molde: "[diz que falta só uma coisa, em tom de conversa]"
- Fonte A, o obrigado do ingresso, em molde: "[confirma que o ingresso está garantido]! [avisa que falta um passo pra confirmar a participação]." e "[pede a resposta da pesquisa como o passo que fecha a inscrição]."
- Fonte A, o obrigado da Black, em molde: "[depois de responder: o que anotar na agenda]" e "[por onde os links chegam]."
- Fonte C, numa consultoria, o Rodrigo, sobre por que a pesquisa fica no obrigado: "Pra ter mais taxa de resposta e otimizar melhor as campanhas também, baseado no MQR." Depois: "Mas, depois, na última pergunta, o botão de enviar vai para o grupo." e "As minhas pesquisas aqui batem entre 60% e 80% de resposta."
- Fonte C, numa reunião com gente de fora da casa, o Rodrigo: "quando você tem uma taxa de resposta alta, o teu MQL vai ficar mais assertivo, porque o MQL é baseado em quem responde a pesquisa"
- Fonte C, noutra reunião com gente de fora da casa, o Rodrigo: "70% taxa de resposta na pesquisa, que também coloco na página obrigado, igual vocês."
- Fonte G, `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.9: "~71% das vendas vieram de quem respondeu a pesquisa"
- Fonte B, notas das páginas da lista da Black, §2, sobre o script que repassa os dados pra pesquisa: "é o que amarra a resposta da pesquisa ao e-mail do lead"
- `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.1, a falha do repasse: "a coluna WhatsApp da planilha da pesquisa ficou vazia nas 7.741 respostas"
- `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7: "E-mail na URL vai pra Meta." e "Achado e não corrigido no caso-base"
- Fonte A, obrigado da lista de espera, em molde: "[confirma que a pessoa está na lista]" e "[avisa que o grupo é opcional e que o lugar na lista não depende dele]."

**Exemplos (em molde).**
- O motivo pra responder, no obrigado do lançamento gratuito: "[diz que saber mais da pessoa ajuda o expert a levá-la até [o objetivo dela]]."
- O obrigado da lista VIP: "[parabeniza e nomeia a [lista VIP]]" e "[pede uma coisa só: estar pronto [no dia], [na hora]]."

### 4.4 Página de vendas — VARIAÇÃO ISOLADA na ordem (2 páginas no ar); o conteúdo mínimo é decisão do Rodrigo

**O que entra.** O mínimo, dito pelo Rodrigo numa reunião com o expert do caso-base: depoimento, grade (o que tem dentro), preço, garantia e o botão que vai pro checkout. Cada produto tem a sua página. As duas páginas de venda de programa no ar (molde do segundo WordPress) fazem assim:

| # | Bloco | Reabertura (programa principal) | Downsell (um curso menor) |
|---|---|---|---|
| 0 | Cronômetro do fechamento | sim | não |
| 1 | Topo: promessa e botão pra âncora do preço (na da reabertura, com a quebra de objeção logo abaixo da promessa) | sim | sim |
| 2 | O que tem dentro: módulos em acordeão | sim | sim |
| 3 | Suporte e como se aprende | sim | não |
| 4 | Depoimentos em vídeo, com botão | sim | não |
| 5 | Bônus, com a soma | sim | sim (sem soma) |
| 6 | Pra quem é | não | sim |
| 7 | Preço, com a parcela em destaque | sim, dois cards (cartão; boleto ou Pix) | sim, um card |
| 8 | Garantia | sim | sim |
| 9 | Sobre o expert | sim | sim |
| 10 | FAQ | não | sim |
| 11 | Dúvida → suporte no WhatsApp; rodapé com política | sim | sim |

Em comum nas duas: os botões de cima descem até o preço, bônus antes do preço, garantia logo depois do preço, o expert depois da garantia, parcela grande e à vista menor. Da lista do Rodrigo, o único item que falta numa delas é o depoimento, na do downsell.

**Por quê.** Quem só viu uma chamada vai ter dúvida, e a página existe pra responder antes do checkout (fala do Rodrigo na mesma reunião). O preço vem depois do que a pessoa recebe, que é a regra da ordem das 14 seções (`sirius-scale/frameworks/oferta-14-secoes.md` §0).

**Variações aceitáveis.**
- **Página de vendas de oferta grande (Black, rascunho v2):** os blocos são as 14 seções, uma por bloco, com uma faixa no alto que só aparece quando existe prazo real, FAQ, rodapé e prévia do link. Nenhum valor antes do preço. Não tinha ido ao ar quando este arquivo foi escrito (a Black abria semanas depois).
- **Reabertura:** a decisão do Rodrigo foi página de vendas com o vídeo da aula inaugural embutido, e não checkout direto. A página nos arquivos da casa não mostra esse vídeo; não dá pra afirmar que foi ao ar assim.
- **Low ticket pra público frio:** sem botão no topo, primeiro botão no bloco 9 de 13 (`sirius-scale/frameworks/lancamentos/low-ticket.md` §5 e §14.1).

**Trecho real.**
- Fonte C, reunião com o expert do caso-base, o Rodrigo: "Se na Home tiver só a chamada para o curso, é o ideal que vai para a página, a pessoa vai ter dúvidas." / "Ela vai querer ler o cronograma e na página a coloca depoimento do curso, coloca a grade, preço, garantia, tudo mais, e o botão para comprar que vai para o checkout." / "Então, cada produto tem uma página de vendas." E sobre o peso dela: "o que mais importa para nós mesmos são as páginas de vendas, estarem boas"
- Fonte A, a página da reabertura, em molde: "[cronômetro até o fim das matrículas]", "[a objeção de estudar sozinho, respondida no título]", "[a garantia dita como risco nenhum]", "[último convite pra tirar dúvida]"
- Fonte A, a página do downsell, em molde: "[pra quem é o curso, em lista]"
- Fonte B, notas da página de vendas da Black, §2: nenhum valor em reais antes do bloco 9 do rascunho. E na copy da página, bloco 0: "A faixa só aparece quando existe um prazo real pra mostrar."
- Fonte B, briefing do lançamento gratuito, reabertura (decisão do Rodrigo): "Página de vendas COM o vídeo de boas-vindas embutido — não é checkout direto."

**Exemplos (em molde).**
- A quebra de objeção logo abaixo da promessa, na reabertura: "[mesmo que + o que hoje mais trava a pessoa]."
- A soma dos bônus: "[a soma dos bônus, com o valor]", e logo depois "[entrando agora, a pessoa leva todos sem pagar a mais]."
- O preço do downsell, com a parcela em destaque: "Por apenas 12x de [parcela] ou [preço] à vista".

### 4.5 Página de venda do ingresso de evento pago — VARIAÇÃO ISOLADA (1 página, a inscrição do LPSG)

**O que entra, na ordem.** Cronômetro até a primeira aula → topo com a promessa, o formato (dias, horas, horário, credencial) e a lista do que se aprende → **a oferta logo em seguida**, com o prazo real e dois botões (ingresso; ingresso com a gravação) → garantia → autoridade → o que se aprende aula por aula → FAQ (9 perguntas) → depoimentos em print → popup de entrada com um desconto extra.

**Por quê.** É ticket baixo: a oferta vem cedo, logo depois do topo. O `sirius-scale/frameworks/lancamentos/low-ticket.md` §5 registra a exceção que permite isso (público quente ou preço que é o próprio incentivo). O porquê específico desta página não está registrado.

**Variações aceitáveis.** O que a casa mexeu, em cima de decisões do Rodrigo da véspera e do mesmo dia (preço novo, aulas gravadas, sem escassez falsa): tirou a barra de 88% dos ingressos (não existia limite) e trocou o "Oportunidade única!" do popup pelo prazo real. A faixa do popup no ar diz "Desconto desta turma".

**Trecho real.**
- Fonte A, a inscrição do ingresso, em molde: dois botões, "[quero + a inscrição]" e "[a inscrição + o que vem a mais: a gravação]"; e a garantia com um nome próprio, em caixa alta.
- Fonte B, a copy da inscrição do ingresso, sobre tirar a barra: "uma barra de progresso sempre implica um total/capacidade por trás, e não existe nenhum pra mostrar com honestidade"
- Fonte G, a análise de tráfego de uma turma do LPSG (§16 de lá): "A queda [...] foi no frio da Meta e depois do clique": a visita que vira ingresso caiu de 4,8% pra 2,1%, com o custo por visita igual. Ou seja, a perda foi no passo da página, mas sem defeito nela: a página e os dois checkouts foram conferidos e estavam funcionando.

**Exemplos (em molde).** O prazo real no lugar da escassez: "[até quando a inscrição fica aberta: dia e hora], [o motivo real: é quando a primeira aula começa]." O contraste com o que o público já conhece: "[nega que seja mais um [tipo de curso que o público já fez]]". O popup de entrada oferece um desconto extra pequeno, de valor fixo.

### 4.6 Página de low ticket — VARIAÇÃO ISOLADA na casa (está em `sirius-scale/frameworks/lancamentos/low-ticket.md`)

Os 13 blocos, a régua de UX e as quatro páginas no ar estão no `sirius-scale/frameworks/lancamentos/low-ticket.md` §5 e §12 a §14.5, inclusive as reprovações do Rodrigo na v1 ("precisa ter mais vida") e as correções da v2.1 e da v2.2. Este arquivo não repete. O que delas entra nas regras transversais (§8): primeiro botão depois do valor, prova em print real, parcela em destaque e conferência de estrutura em código.

### 4.7 Carta de pré-abertura — VARIAÇÃO ISOLADA (2 páginas, um molde: a do lançamento gratuito e a do LPSG)

**O que entra, na ordem.** Cronômetro até a abertura → topo com a promessa e o botão da lista → "leia até o final" e a carta em primeira pessoa → abertura: dia, hora e a condição do primeiro dia → o que é o programa → bônus exclusivos da turma (só pra quem está na lista) → condições especiais do primeiro dia → prova em vídeo → como é a jornada → preço com o desconto do primeiro dia → garantia de 7 dias → sobre o expert → aulas liberadas do evento → popup com o formulário da lista.

**Por quê.** É a fase entre o fim das aulas e a abertura do carrinho: ainda não dá pra comprar, então a ação é entrar na lista (`sirius-scale/frameworks/copy/criativos.md` §0.9). A carta antecipa a oferta inteira com data e preço, e o botão leva pra lista, não pro checkout.

**Variações aceitáveis.** A antecedência da lista muda por funil: uma hora no lançamento gratuito, dez minutos no evento pago.

**Trecho real.**
- Fonte A, a carta do lançamento gratuito, em molde: "[cronômetro até a abertura]", "[pede a leitura até o fim]", "[os bônus desta turma]", "[como vai ser a jornada]", "[a garantia como teste de [dias]]"; e o último link da página leva pras aulas liberadas.
- `sirius-scale/frameworks/copy/criativos.md` §0.9, destino do clique na fase da carta: "página da carta → grupo VIP (não matrícula)"

**Exemplos (em molde).** A abertura em primeira pessoa: "[o expert se apresenta e diz que escreveu a carta pra quem está lendo]." Os cinco botões levam o nome da lista: "ENTRAR NA LISTA [VIP]".

### 4.8 Páginas do evento: aula e lives — VARIAÇÃO ISOLADA (4 páginas de aula de um molde; 1 de lives)

**O que entra.**

**Página de aula** (as 4 do lançamento gratuito): faixa com as datas e o aviso de que é on-line e gratuito → a aula do dia, com o vídeo que abre no clique → botão pro programa → a lista das quatro aulas com o estado de cada uma. É o destino dos criativos de aula liberada (a gravação no blog de lançamento, `sirius-scale/frameworks/copy/criativos.md` §0.9).

**Página de lives** (a do lançamento gratuito): topo com o contexto, a plataforma e o convite pra quem ainda não se inscreveu → um card por live, alternando conversa com aluno e live de conteúdo, cada um com etiqueta de estado → convite final pra inscrição. A estrutura escrita pra ela pediu três coisas que estão no ar (dizer a plataforma, rótulo público no lugar do interno, etiqueta de estado) e duas que não estão (inscrição rebaixada pra depois da grade e fecho no grupo de WhatsApp). A página de lives também está, do lado do aquecimento, em `sirius-scale/frameworks/lancamentos/aquecimento-e-lives.md` §3.11.

**Por quê.** A página de aula é o destino de quem vai assistir à gravação depois da aula (`sirius-scale/frameworks/copy/criativos.md` §0.9); a de lives junta numa URL só tudo o que o anúncio de aquecimento promete. O botão pro programa na página de aula é a exceção à regra de uma ação (§11).

**Variações aceitáveis.** A página de lives cresce durante o aquecimento: cada live entra quando acontece, uma abaixo da outra. As quatro páginas de aula são a mesma, com a aula do dia no topo.

**Trecho real.**
- Fonte A, a página da aula 1, em molde: "[aponta o botão que leva pra aula]", "[etiqueta de estado: disponível, com a ação]".
- Fonte A, a página de lives, em molde: "[quantas lives por dia e em que plataforma]", "[etiqueta do tipo de live + número]", "[etiqueta de estado: replay]".
- Fonte B, a estrutura da página de aquecimento: "Hoje a página não diz onde a live acontece." e, sobre a etiqueta, "precisa distinguir com clareza 3 momentos possíveis"
- Fonte D, memória da frente de páginas no WordPress, sobre a página de lives: "hospeda TODAS as lives de aquecimento, em sequência, uma abaixo da outra"

**Exemplos (em molde).** O botão da página de aula: "ENTRAR NO [PROGRAMA]". O topo da página de lives: "[diz que a preparação pro [evento] começa nesta página]".

### 4.9 Página-hub do link da bio — VARIAÇÃO ISOLADA (1 molde, nas versões do Instagram e do YouTube)

**O que entra.** Uma arte no topo com o que está em destaque agora (no lançamento, o lançamento) e o botão dele; embaixo, um card horizontal por produto, cada um levando pra página de vendas do produto ou pra lista de espera, conforme o que estiver aberto. Sem preço, sem prazo e sem escassez nas artes. Um produto aparece com uma oferta por vez: no carrinho da Black, o card da lista de espera do programa principal sai.

**Por quê.** O link da bio envelhecia no dia em que o evento acabava. O formato veio de referência externa (a bio do mesmo vendedor de low ticket cujo método está em `sirius-scale/frameworks/lancamentos/low-ticket.md`), pedido do Rodrigo; o movimento no botão do topo e o texto dele foram ajustes dele no dia seguinte (log de publicação).

**Variações aceitáveis.** A home nova (prévia, não publicada) segue a mesma ideia, com decisões do Rodrigo e do expert numa reunião: vitrine de produtos, cada um com a sua página de vendas, e um botão de "já sou aluno" no topo que leva pro login. Vai pra §11 até ir ao ar.

**Trecho real.**
- Fonte C, reunião com o expert do caso-base, o Rodrigo: "Então, vai para a página de vendas ou lista de espera, depende do que estiver rolando." e "E aí, sempre vai estar, por exemplo, está em lançamento, em destaque vai estar o lançamento no topo."
- Fonte B, o montador da bio: "arte-hero de ponta a ponta no topo e, embaixo, um card horizontal (arte 2,5:1 com o texto embutido) por link." e "No carrinho da Black o card do [programa principal] some"
- Fonte B, a copy das artes da bio: "Sem preço, sem prazo e sem escassez em nenhuma arte."
- Fonte D, memória da home nova: "link de bio envelhece no dia em que o evento acaba porque alguém precisa lembrar de trocar"

### 4.10 Página de VSL — VARIAÇÃO ISOLADA (outro cliente, 1 página)

**O que entra.** Headline e o vídeo, e nada mais na primeira visita: sem botão e sem a página de venda aparente. Na hora da oferta, no vídeo, a página abre (o botão aparece). Depois do checkout vêm as páginas de upsell e downsell, que estão fora deste arquivo (§0.2, item 5). O roteiro da VSL está em `sirius-scale/frameworks/copy/producao-de-vsl.md`.

**Por quê.** Quem vem do criativo de conteúdo chega pra assistir a uma aula, não pra ler uma página de venda. A headline é testável no próprio player.

**Variações aceitáveis.** Quem chega pelo link da bio vê a página já aberta, porque quer comprar (fala do Rodrigo numa consultoria).

**Trecho real.**
- Fonte C, numa reunião com gente de fora da casa, o Rodrigo: "Aí, a aula completa é o vídeo de venda, só que a pessoa cai na página, só tem uma headline e o vídeo, não tem botão, não vê que é uma página de vendas." e "Aí, na hora da oferta, a página abre."
- Fonte C, numa consultoria, o Rodrigo: "Só tem uma headline, que a gente pode testar várias" e "Aí você programa, na hora que ela chega na oferta, a página aparece."
- Fonte E, o checklist do funil da VSL: "Implementar botão com delay (aparece só no momento do pitch)"
- Fonte G, o debriefing do perpétuo do livro, §3: connect de 75,7%, conversão página → livro de 0,81%, carregamento médio de 3,8 s.

---

## 5. Passo 4 — Depois do clique — PADRÃO CONSISTENTE (proposto) na cadeia captura → obrigado → pesquisa; VARIAÇÃO ISOLADA no resto

**O que entra.** Antes de escrever, fica decidido pra onde cada botão leva, o que vai junto e onde a pessoa termina:

| Página | O clique leva a | O que vai junto | Visto em |
|---|---|---|---|
| Captura de evento | formulário da própria página → obrigado do evento | tag do CRM do formulário; nome, e-mail e telefone na URL do obrigado (⚠️ a URL vai inteira pro pixel da Meta, §4.3) | 2 de 2 |
| Obrigado com pesquisa | a pesquisa; no fim dela, o grupo | os dados da URL, nos campos ocultos da pesquisa, quando a página tem o script e o nome casa (2 de 3; o telefone só pode chegar no da Black) | 3 de 3 (o grupo no fim: fala do Rodrigo) |
| Captura de lista | obrigado da lista | tag da lista | 4 de 4 |
| Venda de programa (molde do 2º WordPress) | popup com nome, e-mail e WhatsApp → checkout da Hotmart já preenchido | tag de checkout no CRM; na da reabertura, um popup por forma de pagamento | 2 de 2 |
| Venda de low ticket | checkout puro da oferta própria do tráfego pago | as UTMs entram no clique pelo rastreio do Dash, não no HTML | 4 de 4 |
| Ingresso do evento pago | checkout direto, dois botões (ingresso; combo) | — | 1 |
| Carta | popup da lista → obrigado da lista | tag da lista | 2 de 2 |
| VSL | checkout → upsell → downsell | — | 1 (Fonte E) |

A mecânica do formulário (o registro por chave, o redirect com os dados, a cópia de segurança) está no `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §3, §4 e §4.2; o rastreio do clique no §5 de lá; o parâmetro do checkout que mostra os order bumps no `sirius-scale/frameworks/hotmart/hotmart-configuracao-produto.md` §1.

**Regra (decisão do Rodrigo): página de vendas com formulário antes do pagamento manda pro checkout já preenchido.** A linha "Venda de programa" da tabela deixa de ser só o que se viu e passa a valer pra toda página de vendas nova: o que a pessoa digitou (nome, e-mail, WhatsApp) vai no link do checkout da Hotmart, junto com as UTMs, o `src` e o `sck`. Fala dele: "tem que adicionar sempre nas paginas de vendas o checkout pro populado da hotmart, pra que ja venha preenchido o que ela digitar no formulario anterior". Os parâmetros estão no `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.3. O low ticket fica como está (sem formulário, checkout puro).

**Por quê.** A cadeia da captura existe pra pesquisa chegar no mesmo lead e alimentar o MQL (§4.3). Na venda, o checkout vai puro pra origem da venda ficar legível pela oferta e pelo rastreio do Dash.

**Variações aceitáveis.** Ver §5.1 e §5.2.

**Trecho real.**
- Fonte B, o montador de links de checkout do low ticket: "checkout puro da Hotmart com a oferta própria do pago (off=)" e, sobre o parâmetro dos bumps, "Sem ele abre o checkout padrão, sem bump nenhum"
- Fonte A, a página da reabertura, título do popup antes do checkout, em molde: "[pede o formulário como o passo pra garantir a compra]."
- Fonte C, numa consultoria: "Mas, depois, na última pergunta, o botão de enviar vai para o grupo."

### 5.1 Quem já ouviu a oferta vai pro checkout; quem só viu a chamada vai pra página — PADRÃO CONSISTENTE (proposto)

**O que entra.** O destino do clique depende do que a pessoa já viu. Quem assistiu ao pitch (carrinho aberto do lançamento) ou é base quente com oferta simples (o single shot do evento pago) vai direto pro checkout. Quem só viu uma chamada (home, bio, anúncio de reabertura pra quem não viu a live) vai pra página de vendas ou pro vídeo.

**Por quê.** A página existe pra responder a dúvida de quem só viu a chamada (fala do Rodrigo numa reunião com o expert). Quem assistiu ao pitch já ouviu essas respostas na aula ou na live.

**Variações aceitáveis.** Reabertura: o destino foi a página de vendas com o vídeo, e não o checkout, porque o pitch estava no vídeo.

**Trecho real.**
- `sirius-scale/frameworks/copy/criativos.md` §0.9: no carrinho aberto, o destino do clique é o checkout.
- `sirius-scale/frameworks/lancamentos/lpsg.md`: "Single shot (o ingresso mais barato, checkout direto) é a compra mais barata das duas contas"
- Fonte C, reunião com o expert do caso-base: "Se na Home tiver só a chamada para o curso, é o ideal que vai para a página, a pessoa vai ter dúvidas."
- Fonte B, briefing do lançamento gratuito, reabertura: "Página de vendas COM o vídeo de boas-vindas embutido — não é checkout direto."

### 5.2 Aluno e não aluno em caminhos separados — VARIAÇÃO ISOLADA (Black)

**O que entra.** Quando a condição muda por grupo, cada grupo tem a sua página (ou o seu botão), a sua tag, o seu obrigado e o seu grupo de WhatsApp. A página da bio põe a escolha na mão da pessoa, com dois botões. A Black como um todo está em `sirius-scale/frameworks/lancamentos/black-da-casa.md`.

**Por quê.** A Black tinha preço diferente pra aluno. A captação de aluno corria em público próprio, e a separação nos grupos também segurava o risco de golpe na lista de alunos (reunião da equipe sobre os grupos da Black).

**Variações aceitáveis.** Um validador de e-mail com um botão só foi cogitado e ficou pra venda, não pra captação (mesma reunião).

**Trecho real.** Fonte C, reunião da equipe sobre os grupos da Black: "A diferença é um só leva pro grupo de aluno, o outro só leva pro grupo de não aluno e o da bio, você escolhe se você é aluno ou não."

---

## 6. Passo 5 — O texto é do `copy`; página, checkout e preço são de quem decide a oferta — PADRÃO CONSISTENTE (regra da casa) + VARIAÇÃO ISOLADA (decisão do Rodrigo)

**O que entra.** O agente `copy` escreve o texto de cada bloco a partir da estrutura e passa pelo `/humanizer` (`sirius-scale/REGRAS.md` §3). Na hora de pedir validação, o que é do expert (conteúdo, bônus feito com aula dele, o que ele precisa gravar) vai pra ele; página de vendas, checkout e preço vão pra quem decide a oferta (na casa, o Rodrigo), em outra mensagem.

**Por quê.** A estrutura sem o dado real do cliente vira texto genérico, e foi assim que uma copy escrita direto na conversa foi reprovada pelo Rodrigo. E pedir ao expert que decida a oferta comercial mistura papel e atrasa o que de fato precisa do sim dele.

**Variações aceitáveis.**
- Troca pontual num texto que o `copy` já escreveu (data, número, uma palavra) não volta pro agente (`sirius-scale/REGRAS.md` §3). Exemplo: o texto do botão do topo da bio, que o próprio Rodrigo ditou, entrou direto no montador da página.
- Mudança de preço, formato ou escassez volta pro `copy`, mesmo em poucos trechos. Os nove trechos da inscrição do ingresso (preço novo, aula gravada no lugar de ao vivo, escassez falsa fora) foram escritos pelo agente, com escopo fechado e o resto da página intocado.

**Trecho real.**
- `sirius-scale/REGRAS.md` §3: "Todo texto que o público final lê (anúncio, e-mail, WhatsApp, roteiro, página, legenda) é escrito pelo agente `copy`, nunca direto na conversa."
- Fonte D, memória "validação do expert só com o que é dele": "Página de vendas, checkout e preço são decisão do Rodrigo"; e a fala dele: "isso é decisão minha [...]"

---

## 7. Passo 6 — Conferir antes de publicar — PADRÃO CONSISTENTE (proposto) em ver a página no celular, rolando até o fim; o resto já mora nos vizinhos

**O que entra.** A página só está pronta depois de vista na tela do celular, do topo ao rodapé, além de conferida por código. Três vezes a conferência por código ou por documento deixou passar o que a tela mostrava: o clone do SaaS com 59 blocos invisíveis, a seção branca com letra branca na página do primeiro guia de low ticket (o Rodrigo achou pela tela) e a primeira tela do celular refeita na v2.1 da mesma página, depois do retorno dele vendo a prévia no ar.

**Por quê.** `querySelector` acha elemento invisível do mesmo jeito que acha um visível, e página longa estoura onde o texto não estoura (na revisão da página do primeiro guia, o primeiro botão estava a 77% da página no celular).

**Variações aceitáveis.** Em teste de variação visual, o `sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md` manda confiar no estilo computado e não no screenshot do navegador embutido, que atrasa frames. As duas coisas valem juntas: estilo computado no código e o olho na tela (§11).

**Trecho real.**
- Fonte D, memória "clone de página se confere rolando": "clone de página só está pronto depois de rolar do topo ao rodapé e comparar com o original"; e o que cegou: "encontra um elemento com opacity: 0 do mesmo jeito que encontra um visível"
- Fonte B, o montador da página do primeiro guia: "uma troca de texto apagou o fim de um bloco e o começo do seguinte" e "o Rodrigo achou pela tela"
- A revisão da página do primeiro guia: "Comprimento no celular: 16.565 px, primeiro botão a 12.720 px (77%)."
- `sirius-scale/frameworks/lancamentos/low-ticket.md` §14.5 (v2.1): "A imagem do avatar cabe na primeira tela do celular."

### 7.1 Clone: rolar até o fim, trazer a animação junto e pôr rede de segurança — VARIAÇÃO ISOLADA (três correções em pouco mais de um mês; na casa, virou trava de código)

**O que entra.** Clone de página leva as animações do original (entrada dos blocos, abrir e fechar de acordeão), respeitando quem desligou movimento no aparelho. E, se o original revela os blocos ao rolar, o clone traz o código que revela e um prazo que acende tudo se esse código falhar. Na conferência, além do olho, contar os elementos com opacidade zero: acima de zero num clone estático é suspeito.

Essa contagem não basta. Ela não pega bloco escondido com `visibility: hidden`, que era o caso de 4 das 5 páginas vivas do caso-base que revelavam ao rolar. O teste que pega os dois jeitos é quebrar o script de propósito e ver se a página se salva sozinha. Na casa isso roda em toda publicação de produção, dentro do script de publicação, e na prévia só avisa (o script não vem no kit; como ele funciona por dentro está no `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2, passo 3, e §9). A conferência para a página em três casos:
- bloco que não aparece sozinho em até 3 s com o script quebrado ou sem JavaScript;
- bloco no fluxo da página invisível do começo ao fim, mesmo rolando até o rodapé;
- bloco que, com o script funcionando, aparece antes de a rolagem chegar nele.

"Escondido", pra ela, é `visibility: hidden` ou opacidade zero, os dois jeitos que as páginas da casa usam. Bloco deslocado pra fora da tela (`transform`) ou com altura zero não é pego, e ela só olha a tela de celular.

**Do lado de vocês, antes de publicar no Lovable ou na hospedagem,** a mesma conferência, à mão ou pedida ao Claude:
1. abrir a prévia em tela de celular, com o rastreio bloqueado (visita de conferência conta como tráfego: `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §9);
2. quebrar de propósito o script que revela os blocos (ou desligar o JavaScript) e rolar até o rodapé: todo bloco aparece sozinho em até 3 s;
3. com o script funcionando, rolar de novo: nada aparece antes de a rolagem chegar nele, e nenhum bloco fica invisível do começo ao fim;
4. procurar os dois jeitos de esconder (`visibility: hidden` e opacidade zero), não só um.

⚠️ Página feita no Lovable nasce inteira no JavaScript (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §10): sem JavaScript, ela fica em branco de qualquer jeito. Ali, o teste que sobra é o do passo 2 com só o código que revela os blocos quebrado. A casa nunca conferiu uma página de Lovable assim: é hipótese, não regra.

A rede mora no CSS: um prazo de 2 s que o próprio observador cancela quando responde (`.js:not(.observador-ok)`), pra não mudar nada na tela quando o script funciona. Num aparelho que demore mais de 2 s pra rodar o script, o bloco aparece parado e depois faz a entrada. Isso só foi visto em simulação: com o processador 20 vezes mais lento, o observador respondeu em 0,8 s. Um `setTimeout` dentro do mesmo script, como o do clone do SaaS, cai junto quando o script quebra.

**Por quê.** Pro Rodrigo, fidelidade inclui movimento. E a página do SaaS rodou quatro dias com tráfego pago (320 visitas) mostrando só a primeira dobra, porque o DOM capturado trouxe o estado inicial invisível sem o JavaScript que acende. Seis dias depois desse achado, o mesmo risco estava nas três páginas de inscrição da Black, com tráfego pago: com o script quebrado, o formulário e os quatro botões de inscrição nunca apareciam (medido no ar, com o rastreio bloqueado).

**Variações aceitáveis.** O que a plataforma não deixa reproduzir fica fora, dito na entrega. Em página nova de low ticket, a régua é outra: movimento só no botão de compra (`sirius-scale/frameworks/lancamentos/low-ticket.md` §12, passo 3).

**Trecho real.**
- Fonte D, memória das animações do original, resposta do Rodrigo: "eu quero sim, sempre que possível"; e "Pra ele, fidelidade inclui movimento, não só layout."
- Fonte D, memória "clone de página se confere rolando": "Página em branco não pode depender de um script dar certo."
- Fonte F, comentário no clone corrigido do SaaS: "Pagina em branco nunca mais pode depender de um script dar certo."
- Fonte A, comentário do conserto nas 5 páginas do caso-base (no ar dois dias depois de desenhado): "o bloco aparece sozinho, parado"

### 7.2 A lista de conferência, com a fonte de cada item — força item a item (CONSISTENTE, ISOLADA, INCONCLUSIVO ou UNIVERSAL na coluna)

| # | Conferir | Força | Onde está |
|---|---|---|---|
| 1 | Rolar no celular do topo ao rodapé; no clone, comparar com o original em três alturas | CONSISTENTE (proposto) | §7 e §7.1 |
| 1a | Bloco que aparece ao rolar aparece sozinho com o script quebrado e sem JavaScript; nenhum bloco no fluxo fica invisível do começo ao fim; com o script funcionando, nada aparece antes da rolagem | VARIAÇÃO ISOLADA (2 casos: o SaaS e o caso-base, seis dias depois); na casa virou trava de código, que roda sozinha na publicação de produção | §7.1 (a conferência do lado de vocês); como a trava da casa funciona: `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2, passo 3, e §9 |
| 2 | 375 px de verdade (o Chrome sem janela no macOS não desce de 500 px) | UNIVERSAL | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §9 |
| 3 | Estrutura conferida por código antes de gravar (seção abre e fecha, fundos alternam, componente no fundo certo, proporção da imagem) | VARIAÇÃO ISOLADA (low ticket) | o montador da página do primeiro guia de low ticket (evidência no caso de origem); peça ao Claude a mesma conferência no HTML |
| 4 | Formulário de ponta a ponta na prévia, com tag de teste, lido de volta no CRM | VARIAÇÃO ISOLADA | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2, §3 e §4.2 |
| 5 | Nome do parâmetro igual ao do campo oculto da pesquisa | VARIAÇÃO ISOLADA (custou o telefone de 7.741 respostas) | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.1 |
| 5a | E-mail, nome e telefone na URL não podem chegar no pixel | VARIAÇÃO ISOLADA (achado no caso-base e não corrigido lá; consertado depois num segundo cliente) | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7 e §11.1 |
| 6 | Evento de cadastro no obrigado antes de campanha de cadastro | VARIAÇÃO ISOLADA | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7 |
| 7 | Imagem que a página usa já existe em produção | VARIAÇÃO ISOLADA | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2 |
| 8 | Ao reaproveitar: datas, cronômetro, tag, título da aba e o que a regra da casa não aceita mais | VARIAÇÃO ISOLADA | §3 deste arquivo |
| 9 | Nada vencido nem "em breve" na página no ar | VARIAÇÃO ISOLADA (o SaaS) | Fonte F, diagnóstico §6 |
| 10 | Peso e carregamento medidos | INCONCLUSIVO no efeito (nunca testado) | a VSL do segundo expert, 3,8 s; a página do SaaS, 7,9 s; a saída do WordPress, no backlog de ideias da casa; o perpétuo de outro expert, com uma página de 5,9–6,8 s e 36% de visita por clique contra outra de 2,9–3,3 s e 58% (correlação, páginas e públicos diferentes, sem teste) |
| 11 | Conferir em prévia sem rastreio, porque visita de conferência dispara pixel e entra como tráfego | VARIAÇÃO ISOLADA | `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §9; a trava da casa já confere com o rastreio bloqueado |
| 12 | Revisão de olhos frescos | regra da casa | `/revisar` (`sirius-scale/REGRAS.md` §5), com o checklist de página (`.claude/skills/revisar/checklists/pagina.md`) |
| 13 | Publicar só pelo caminho combinado e conferir no endereço do deploy | VARIAÇÃO ISOLADA | na casa, um script de publicação (não vem no kit), com registro de quem pode pedir publicação; do lado de vocês, o Lovable ou a hospedagem, com o checklist do `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §2 |
| 14 | Produto físico com frete pago pelo comprador: a página diz o frete antes do botão (o checkout da Hotmart marca `shipmentCostsPaidByShopper`) | VARIAÇÃO ISOLADA (outro expert: a página dizia só o preço, e o checkout cobrava o frete a mais; efeito na conversão não medido) | o diagnóstico daquele perpétuo (evidência no caso de origem) |

Trecho real dos itens 9 e 10:
- Fonte F, o diagnóstico do funil do SaaS, §6: "O bônus está vencido há 22 dias e continua no ar."
- Fonte E, o debriefing do perpétuo do livro, §3: "3,8 s de carregamento é lento pra tráfego de celular."
- Fonte C, numa reunião com um expert de fora da casa, o Rodrigo, sobre a página no Cloudflare: "Cara, a página carrega em um segundo, velho."

---

## 8. Regras transversais

1. **Uma ação por página.** *PADRÃO CONSISTENTE (proposto)*, §2.
2. **Escassez só quando é real.** *PADRÃO CONSISTENTE (regra da casa, `sirius-scale/frameworks/copy/criativos.md` §0.5; nas páginas, as 3 vezes em que a casa mexeu num texto herdado, tirou).* Saíram a barra de 88% e o "Oportunidade única!" do ingresso e o aviso de vagas limitadas na derivação da Black; o low ticket já nasceu sem cronômetro. A cópia fiel da captura do lançamento gratuito ainda tem o aviso (§11). Trecho, `sirius-scale/frameworks/copy/criativos.md` §0.5: "Não usar linguagem de escassez falsa."
3. **Cronômetro conta pra um horário real.** *PADRÃO CONSISTENTE (proposto), 4 páginas.* Abertura das inscrições (as 2 cartas), fechamento das matrículas (a página da reabertura, que contava até o fechamento dela), primeira aula (ingresso). Sem horário real, não tem cronômetro (low ticket, perpétuo) e a faixa de prazo some (Black, rascunho). Trecho, `sirius-scale/frameworks/lancamentos/live-de-downsell.md` §0: "a reabertura do programa principal fechava às 23h59"
4. **Prova é print ou vídeo real de aluno.** *PADRÃO CONSISTENTE (proposto), 9 unidades, e na Black o bloco saiu por falta de print.* Prints no ingresso e nas 4 de low ticket, vídeos de aluno na página de vendas da reabertura e nas 2 cartas, conversa com aluno na página de lives. Na Black, o espaço de prints ficou fora porque o catálogo não tinha print, só entrevista em vídeo. Trechos: a copy da página de cadastro da Black, "Só print, nada de cartão com a frase entre aspas."; comentário no HTML da captura da Black, "o catálogo só tem entrevistas em vídeo, nenhum print." Se o veto ao cartão com aspas (arte estática, `sirius-scale/frameworks/copy/criativos.md` §0.7.4) vale pra página, não está decidido (§11).
5. **O expert se apresenta em toda página longa.** *PADRÃO CONSISTENTE (proposto), 12 unidades* (as 2 capturas de evento, as 2 de venda de programa, as 2 cartas, o ingresso, a lista de espera e as 4 de low ticket). Credencial uma vez, com a formação e o que só ele tem (`sirius-scale/frameworks/copy/criativos.md` §0.4). O "Saiba mais" que abre e fecha guarda a história.
6. **FAQ em acordeão perto do fim.** *PADRÃO CONSISTENTE (proposto), 8 unidades* (as 2 capturas de evento, o ingresso, o downsell e as 4 de low ticket; a página de vendas da reabertura não tem). As perguntas são as objeções do tipo: na captura, pagar, replay e material; na venda, talento, iniciante, se serve pro caso da pessoa e formato.
7. **O botão se repete depois de cada bloco grande e desce sempre pro mesmo lugar.** *PADRÃO CONSISTENTE (proposto)*, as mesmas páginas do §2.
8. **Parcela em destaque, à vista menor.** *PADRÃO CONSISTENTE (proposto), 3 páginas no ar + o rascunho da Black* (as 2 de venda de programa; low ticket, com valor medido em `sirius-scale/frameworks/lancamentos/low-ticket.md` §14.5; Black só em 12x, decisão do Rodrigo).
9. **Mobile primeiro, leve, um arquivo.** *Regra da casa* (o padrão técnico do agente `webdesigner`, `.claude/agents/webdesigner.md`). A ida pro Cloudflare foi por velocidade e custo (decisão do Rodrigo).
10. **Teste de headline não trava a regra de uma promessa por peça.** *VARIAÇÃO ISOLADA (decisão do Rodrigo).* Fonte D, memória da promessa flexível em teste A/B, o Rodrigo: "essa regra não precisa ser tão rígida, tudo é teste." Nenhum teste rodou até hoje (§11).

---

## 9. Exemplos consolidados (em molde)

**Captura de evento, versão de quem não é aluno** (a da Black), os títulos na ordem:
1. "[dia, data e hora em que o expert abre a [nome da Black]]." + formulário + "[botão: a ação de se inscrever na live de abertura]"
2. "[o que é a [nome da Black]]"
3. "[o que vai ter nela]"
4. "[o que a pessoa ganha ao se inscrever]" e "[a programação]"
5. "[quem é o expert]" com "[botão que abre a bio]"
6. "[perguntas frequentes]": "[a do preço]", "[a do prazo de acesso]", "[a de quem acha que o caso dele não entra]"

**Obrigado com pesquisa** (o da Black), o texto visível inteiro, em ordem:
"[confirma o lugar no evento]! [diz que falta só uma coisa]" · barra em 70% · "[o motivo pra responder: saber mais da pessoa ajuda o expert a levá-la até [o objetivo]]. [pede sinceridade e aponta a pesquisa]" · a pesquisa · "[depois de responder: o que anotar na agenda]" · "[dia], [data], às [hora]" · "[o nome do evento]" · "[por onde os links chegam]" · rodapé.

**Lista de espera e o obrigado dela:**
"[diz que as inscrições do [programa] estão fechadas]" · "[pede o contato e diz o que a pessoa ganha: saber antes de todo mundo quando a turma abrir]" · três campos (nome, e-mail e WhatsApp) · "[botão: a ação de entrar na lista]" · "[diz pra que os dados servem]". Obrigado: "[confirma que a pessoa está na lista]" · "[agradece]" · "[botão pro grupo]" · "[avisa que o grupo é opcional e que o lugar na lista não depende dele]".

**Lista VIP e o obrigado dela:**
"[a vantagem de chegar antes, em caixa alta]" · "[quanto tempo] antes de [todo mundo]" · três campos · "[botão: a ação de receber o link, com a hora]". Obrigado: "[parabeniza e nomeia a [lista VIP]]" · "[pede uma coisa só: estar pronto [no dia], [na hora]]" · "[botão pras aulas]".

**Página de vendas do downsell**, os títulos na ordem:
"[o resultado do curso, com quem [a credencial que só o expert tem]]." · "[botão com o resultado]" · "[o que a pessoa vai aprender]" · "[quantos bônus ela ainda leva]" · "[botão de entrada]" · "[pra quem é o curso, em lista]" · "[o preço: a parcela em destaque, depois o à vista]" · "[botão de compra]" · "[selo com os dias de garantia]" · "[sobre o expert]" · "[perguntas frequentes]" · "[último convite pra tirar dúvida]"

---

## 10. O que é reutilizável e o que é do caso

**Transfere (é de formato, não do cliente). Hipótese até rodar em outro cliente:**
- Uma ação por página, e todo botão descendo até ela.
- Começar da última página aprovada e listar o que muda ao duplicar.
- A cadeia captura → obrigado com a pesquisa embutida, já preenchida com os dados da captura, e o grupo no fim da pesquisa. É a peça que mais carrega número: a resposta alimenta o MQL, e o MQL é a régua de verba. **Com duas ressalvas, as duas medidas:** o nome de cada parâmetro tem que casar com o do campo oculto (no lançamento gratuito o telefone se perdeu em todas as respostas), e, do jeito que estava no caso-base, o e-mail e o telefone na URL vão pro pixel da Meta (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7, não corrigido lá; o conserto está no §11.1 do mesmo arquivo). Transferir só com a URL limpa antes do pixel.
- O destino do clique pelo que a pessoa já viu (§5.1).
- Separar caminhos quando a condição muda por grupo.
- O mínimo da página de vendas que o Rodrigo listou (depoimento, grade, preço, garantia, botão pro checkout) e o preço depois do valor.
- As regras transversais 2 a 8.
- A conferência: rolar no celular, e no clone, animação e rede de segurança.

**É do caso (não generalizar sem medir):**
- Todos os textos, a promessa do topo e os nomes de evento e de produto.
- O que veio do WordPress do caso-base sem razão registrada: o título do obrigado ("falta uma coisa"), a barra de 70%, a entrada animada dos blocos, o popup de desconto extra do ingresso.
- A antecedência da lista VIP (uma hora, dez minutos) e o brinde físico pros primeiros.
- A separação aluno × não aluno, que existe porque a Black tinha preço por grupo.
- As ferramentas: Tally na pesquisa, Full Funnels no CRM, Hotmart no checkout, Cloudflare na hospedagem, Dash Fácil no rastreio. Vocês publicam pelo Lovable ou pela hospedagem de vocês: muda a técnica (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §10), não a estrutura.
- As taxas: 68,49% de resposta (lançamento gratuito), 4,8% de visita → ingresso (um dia, LPSG), 0,81% na VSL do segundo expert. Um funil cada.

---

## 11. Pontos em aberto

1. **Conversão de página não está medida.** Nenhum debriefing tem visita → ação por página nem por bloco (o do lançamento gratuito, §17 de lá; o das três turmas do LPSG, §14 de lá). O Clarity estava previsto no low ticket e já deu uma primeira leitura lá (`sirius-scale/frameworks/lancamentos/low-ticket.md` §5); nas páginas de lançamento, nenhuma.
2. **Nenhum A/B rodou.** O da inscrição do LPSG foi adiado; o de headline do low ticket (a versão alternativa por parâmetro) não tem resultado. Toda escolha de ordem aqui é de uma execução.
3. ✅ **Rede de segurança nas páginas vivas do caso-base que revelam ao rolar: resolvido.** Eram 5 (a captura do lançamento gratuito, as três versões da captura da Black e a lista de espera), feitas antes da correção, sem o prazo que acende tudo; as quatro do molde do lançamento gratuito escondiam o bloco com `visibility: hidden` e traziam a classe que ativa isso fixa no HTML. Com o ok do Rodrigo, as 5 ganharam o prazo de 2 s e foram conferidas no ar com o script quebrado de propósito: tudo aparece em cerca de 2 s, e com o script funcionando a tela não mudou. Na casa, a publicação ganhou a trava de código (§7.1), que só se pula por ordem do Rodrigo, e o pulo fica no log. O que ela não vê está no §7.1. As páginas do SaaS não passam por essa trava.
4. **O título e a barra de 70% do obrigado** vieram do original e não têm razão registrada. A proposta do obrigado de compra do low ticket tira a barra; ninguém decidiu.
5. **Onde o grupo entra.** O Rodrigo diz que é no botão de enviar da última pergunta. O obrigado da Black não tem botão de grupo, e a configuração da pesquisa não está nos arquivos da casa pra confirmar.
6. **O obrigado do ingresso não tem o script de repasse.** Ele só carrega o embed oficial da pesquisa. Se esse embed leva sozinho os parâmetros da URL da página, e se a Hotmart manda algum parâmetro no redirect depois da compra, os arquivos da casa não dizem. Conferir numa compra de teste, olhando a resposta na planilha da pesquisa.
7. **Dado pessoal na URL do obrigado vai pro pixel da Meta** em todas as páginas do caso-base com repasse (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §7, não corrigido lá; o conserto, feito num segundo cliente, está no §11.1 do mesmo arquivo). Enquanto não for, a cadeia captura → obrigado manda e-mail e telefone pra terceiro.
8. **Popup de dados antes do checkout** (página de vendas do molde do segundo WordPress): o porquê não está registrado, e o low ticket vai direto pro checkout.
9. **O veto ao cartão de depoimento com aspas** (arte estática, `sirius-scale/frameworks/copy/criativos.md` §0.7.4) vale pra página? A copy da lista de espera levantou a dúvida e ficou sem resposta.
10. **Página de lives:** a estrutura escrita pra ela pedia a inscrição depois da grade e o fecho no grupo; a página no ar manteve a inscrição no topo e fecha na inscrição. Qual converte, não se sabe.
11. **Página de aula com botão pro programa:** é segunda ação numa página cuja ação é assistir. Não há decisão registrada sobre isso. O mesmo vale pro link de suporte no WhatsApp no fim das páginas de venda de programa: o `sirius-scale/frameworks/lancamentos/low-ticket.md` §12 diz que botão de WhatsApp só entra se for o canal de venda, e a casa não decidiu se essa saída fica.
12. **Título da aba com o código interno** (padrão `<MODELO> – <PEÇA> – <MÊS/ANO>` mais a sigla da marca, na nomenclatura das páginas do `sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md`). A estrutura de aquecimento pedia nenhum código visível, "nem no título da aba"; a Black manteve o código.
13. **A raiz do domínio das páginas ainda mandava pra captura do lançamento gratuito**, que já tinha acabado, com as datas vencidas e o aviso de vagas limitadas. Apontar pra outra página é decisão do Rodrigo (notas das páginas da lista da Black, §4).
14. **WhatsApp no formulário de captura:** passou a ser pedido no lançamento gratuito. Não há registro do motivo nem do efeito na taxa de inscrição.
15. **Página de VSL:** uma página, de outro cliente, que não está nos arquivos da casa. A estrutura vem da fala do Rodrigo e do checklist. Os 3,8 s de carregamento estão como hipótese de venda perdida, sem teste.
16. **Home e vitrine:** as decisões da reunião com o expert (vitrine, cada produto com a sua página, "já sou aluno" no topo, sem preço) só valem como regra quando a página for ao ar.
17. **Obrigado de compra (pós-compra):** só proposta. Vai pro framework de pós-compra (`sirius-scale/frameworks/lancamentos/pos-compra-e-suporte.md` §3.3).
18. **Página de vendas de oferta grande** com as 14 seções em blocos (Black): só vai ter evidência depois da abertura, com a venda.
19. **Captura e obrigado do segundo expert:** a pesquisa de um lançamento gratuito dele teve 81% de resposta, mas os arquivos da casa não dizem se ela estava no obrigado. Se estava, a §4.3 ganha um segundo cliente.
20. **Na página da bio da Black, se o script quebrar, os botões SOU ALUNO e NÃO SOU ALUNO aparecem, mas não abrem o formulário.** O código que abre o popup está no mesmo `<script>` do observador, depois dele, e sem JavaScript o `<dialog>` não abre (medido com o observador quebrado; sem JavaScript, por leitura do código). Conserto possível: o popup num `<script>` próprio, ou o botão virar link pras páginas de aluno e de não aluno, com o JavaScript abrindo o popup por cima. Mexer em página no ar é decisão do Rodrigo.
21. **O rascunho da captura da Black (bloqueado no manifesto) tem o mesmo defeito das 5** (`.anima-entrada` sem `observador-ok`). Quando o Rodrigo liberar, a trava da casa para a publicação até ele ganhar o prazo de 2 s.
