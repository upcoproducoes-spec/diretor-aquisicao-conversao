# Framework — Lançamento clássico: o evento gratuito de ponta a ponta

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método (modelo de lançamento: captação, aquecimento, 3 aulas e a live de domingo, carrinho, reabertura,
> downsell e debriefing).
> **Base:** reverse-engineered da operação de quatro lançamentos clássicos do caso-base (um expert de educação num nicho
> de concurso): o planejamento, o briefing, as campanhas, os debriefings e o que o Rodrigo decidiu ao longo deles.
> **ALCANCE:** `NÃO TESTADO FORA`. As aulas têm segunda base (`sirius-scale/frameworks/lancamentos/cpl-3-aulas.md`); o
> resto do lançamento não tem.
> **FORÇA:** PADRÃO CONSISTENTE = 3 ou 4 dos 4 lançamentos. VARIAÇÃO ISOLADA = 1 ou 2. PADRÃO INCONCLUSIVO = hipótese.
> ⚠️ Três dos quatro planejamentos nasceram da cópia do anterior: ali, "3 de 3" quer dizer que o modelo rodou três vezes,
> não que houve três decisões.
>
> Este arquivo amarra as fases e aponta pro framework de cada uma, sem repetir o que já está escrito lá.

## 1. A fórmula, em ordem: o calendário em D± — PADRÃO CONSISTENTE

D0 é a aula 1, numa segunda, às 20h. A coluna da direita diz em quantos dos 4 lançamentos a data aparece.

| Quando | O que acontece | Lançamentos |
|---|---|---|
| D-19 | captação orgânica começa (na live semanal do expert) | 1 |
| D-17 a D-12 | captação paga começa | 4 |
| D-14 a D-3 | lives de aquecimento; a última é a de tira-dúvidas, em D-3 | 2 com data de transmissão |
| última semana | antecipação (contagem regressiva) | 4 |
| D-1 ou D0 | fim da captação paga | 4 |
| D0, segunda | aula 1 | 4 |
| D+2, quarta | aula 2; a lista VIP abre | 4 |
| D+3, quinta | aula 3 | 4 |
| D+4, sexta | todas as aulas liberadas | 3 |
| D+5, sábado | carta de vendas | 1 com data no ar |
| D+6, domingo | live de encerramento com sorteio (`sirius-scale/frameworks/lancamentos/live-de-domingo.md`) | 4 |
| D+7, segunda | carrinho abre: 7h pra lista VIP, 8h pra todo mundo | 4 |
| D+8, terça | boleto parcelado | 2 |
| D+9, quarta | carrinho fecha | 4 |
| D+14 e D+15 | reabertura, com aula de boas-vindas | 1 |
| D+16 ou D+17 | live de downsell | 2 |
| D+13 a D+35 | debriefing | 2 |

O calendário da semana de aulas também está em `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.3.

**Regras de data ditas pelo Rodrigo** (VARIAÇÃO ISOLADA cada uma):
- **o carrinho abre até a metade do mês** quando o avatar depende da renda mensal: depois disso, o dinheiro do mês já foi;
- **duas semanas de tráfego, com uma de orgânico antes;**
- **o lançamento seguinte começa quando o carrinho fecha:** o dia seguinte ao fechamento já é o dia 1 do próximo.

## 2. Cada fase: o que entra e onde o detalhe mora

| Fase | Framework |
|---|---|
| Planejamento, briefing e metas | `sirius-scale/frameworks/lancamentos/briefing.md`, `sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`, `sirius-scale/frameworks/operacao/nomenclatura-drive.md` |
| Captação | `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §2, `sirius-scale/frameworks/paginas/estrutura-de-pagina.md`, `sirius-scale/frameworks/pesquisa/pesquisa-e-avatar.md`, `sirius-scale/frameworks/copy/criativos.md`, `sirius-scale/frameworks/copy/email.md`, `sirius-scale/frameworks/copy/disparo-whatsapp.md` |
| Aquecimento | `sirius-scale/frameworks/lancamentos/aquecimento-e-lives.md`, `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.1 e §3.2 |
| Semana das aulas | `sirius-scale/frameworks/lancamentos/cpl-3-aulas.md`, `sirius-scale/frameworks/lancamentos/live-de-domingo.md`, `sirius-scale/frameworks/lancamentos/roma-e-promessa.md`, `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.3 |
| Carrinho | `sirius-scale/frameworks/lancamentos/cpl-3-aulas.md` §6 e §7, `sirius-scale/frameworks/copy/email.md`, `sirius-scale/frameworks/copy/disparo-whatsapp.md`, `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.5 |
| Reabertura e downsell | `sirius-scale/frameworks/lancamentos/live-de-downsell.md`; a reabertura não tem framework (§2.6) |
| Debriefing | `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` (a skill `/debriefing`) |
| Remarketing, em todas as fases | `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3 |

### 2.0 Planejamento — PADRÃO CONSISTENTE na planilha de planejamento

**O que entra:**
- a planilha de planejamento do lançamento, compartilhada com a equipe, por volta de D-17;
- o produto do programa na plataforma de venda;
- os documentos, as pastas, os papéis do time, o formato do evento e o briefing (*VARIAÇÃO ISOLADA*: a fase própria de
  planejamento apareceu nos dois últimos).

**Decisões do Rodrigo que valem pro modelo:**
1. **A meta é em contratado**, registrada no Dash como está (`sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`).
2. **O conteúdo não entra na conta do lançamento.**
3. **A verba de remarketing por fase sai da conta de alcance, frequência e CPM** (`sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.7).

### 2.1 Captação — PADRÃO CONSISTENTE

**O que entra, nos 4, entre D-20 e D-17:**
- a página de inscrição e variações, e a de obrigado;
- as UTMs das páginas;
- as boas-vindas por API de WhatsApp e os dois e-mails de boas-vindas;
- o e-mail pra base antiga e as mensagens nos grupos antigos de WhatsApp, agendados até D-11;
- o planejamento das publicações no Instagram;
- o Dash da captação e a campanha;
- os criativos em vídeo (o expert grava) e os estáticos.

**Em 3 de 4:** a lista e a tag de inscrição; a pesquisa no obrigado e o presente da pesquisa; o grupo do evento (§2.2);
a automação de inscrição pelo orgânico (ManyChat); a live semanal do expert como porta de captação.

### 2.2 Grupo de WhatsApp e pesquisa, do começo ao fim — PADRÃO CONSISTENTE

**O que entra:**
- o grupo do evento é criado na captação, com capa e descrição;
- a pesquisa fica na página de obrigado, e o envio dela leva pro grupo;
- o presente da pesquisa (um material de acompanhamento, o "CPL zero") fica no grupo;
- durante a semana, o teste do sorteio vai pelo grupo, e quem saiu volta.

**Por quê:** o grupo é o canal da semana inteira.

**Variação aceitável:** grupos pequenos, de uns 150 leads, contra golpe: um golpista que entra alcança 150 pessoas, não a
lista toda. É PADRÃO INCONCLUSIVO: ideia sem execução registrada.

### 2.3 Aquecimento — PADRÃO CONSISTENTE

**O que entra:**
- as lives de aquecimento durante a captação, gravadas uma vez e reprisadas a cada lançamento;
- as mensagens no grupo por dia de live;
- o cronograma das lives, em arte, mensagem e e-mail;
- a contagem regressiva, o "é amanhã" e a campanha de antecipação (3 de 4).

As lives ficam privadas no YouTube quando o evento começa (VARIAÇÃO ISOLADA, 2 lançamentos).

**Por quê:** a pessoa chega na aula 1 com tempo de tela com o expert e com vontade de comprar. A quantidade de lives
cresceu com o arsenal do expert, lançamento a lançamento.

### 2.4 Semana das aulas — PADRÃO CONSISTENTE

**O que entra:**
- as três aulas e a live de domingo;
- por aula (3 de 4 lançamentos): o roteiro e a revisão; os slides e a capa do YouTube; a transmissão (ferramenta e links); a
  página das aulas; os e-mails e as mensagens de cada dia; a mensagem de API de cada aula; a automação do replay;
- a lista VIP, a carta de vendas, o teste do sorteio, o cronômetro e o remarketing de cada aula.

**Por quê:** é a semana em que a pessoa conhece o método e a oferta. As aulas saem gravadas ao vivo e podem ser reprisadas
no lançamento seguinte.

### 2.5 Carrinho — PADRÃO CONSISTENTE

**O que entra (3 de 4):** as integrações da página com a plataforma e o e-mail; a página de vendas; a API do dia 1; os
e-mails e as mensagens de cada dia; o vídeo de vendas, editado a partir da aula 3; a campanha de vendas e os criativos do
carrinho.

**Por quê:** a venda se concentra nas primeiras horas do dia 1 (`sirius-scale/frameworks/lancamentos/cpl-3-aulas.md` §6).
Tudo do carrinho é pra estar pronto antes das 7h da segunda.

**Regras pro carrinho, ditas nas reuniões** (VARIAÇÃO ISOLADA cada uma):
1. **A primeira hora é da lista VIP:** 7h pra lista, 8h oficial.
2. **O boleto parcelado fica fora do dia 1.**
3. **A recuperação de quem não pagou começa com o carrinho aberto**, não depois.
4. **Antes de abrir, um panorama pra quem decide:** quantos estão na lista VIP e como foi a conversão do lançamento
   passado.
5. **Fechar o carrinho desliga só o botão da página, e o checkout fica**, porque o comercial continua vendendo.
6. **Com o carrinho aberto, as páginas do lançamento levam pro carrinho; fechado, pra lista de espera.**
7. **O replay das aulas sai no carrinho.** O dia diverge entre as fontes (dia 2 ou último dia, como gatilho do último
   dia): escolham e escrevam no briefing.

### 2.6 Depois do carrinho: reabertura, downsell e o pago — VARIAÇÃO ISOLADA (a sequência só rodou uma vez)

**O que entra, nesta ordem:**
1. **a reabertura**, com uma aula de boas-vindas e um pitch sem pressão, em D+14 e D+15;
2. **o downsell**, com live, pra quem não comprou (`sirius-scale/frameworks/lancamentos/live-de-downsell.md`), em D+16 ou
   D+17;
3. **a venda do lançamento pago** (`sirius-scale/frameworks/lancamentos/lpsg.md`).

**O downsell vai depois da reabertura**, por decisão do Rodrigo. Antes, ele já rodou dentro do carrinho e uma semana
depois dele, sem reabertura.

**Sem framework:** a reabertura como fase (a aula de boas-vindas, o pitch e a página). A da Black tem
(`sirius-scale/frameworks/lancamentos/black-da-casa.md`).

### 2.7 Debriefing — PADRÃO CONSISTENTE; a régua do evento é VARIAÇÃO ISOLADA

**O que entra:**
- a pesquisa de alunos e o documento de debriefing pro expert (3 de 4);
- a análise completa, pelo `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md`;
- a régua do evento, que compara um lançamento com o anterior: o pico ao vivo da aula 1 em percentual da lista, o tamanho
  da lista VIP na abertura do carrinho e as vendas na primeira hora.

**Variação aceitável:** a remoção dos posts do lançamento entra no debriefing (2 de 4).

### 2.8 Remarketing, em todas as fases — PADRÃO CONSISTENTE por fase; o "é hoje" em campanha própria é regra do Rodrigo

**O que entra, nos 4:** remarketing na antecipação, nas aulas e no carrinho. A divisão foi ficando mais fina a cada
edição: do começo só na Meta, com uma campanha pra antecipação, uma pras aulas e uma pro carrinho, até uma campanha por
momento nas duas plataformas (o "é hoje" e a gravação de cada aula, o "todas as aulas liberadas", a carta, o domingo e o
carrinho por momento: aberto, meio-dia, boleto, último dia e últimas horas).

**Daqui pra frente, o "é hoje" de cada aula roda em campanha própria**, com início e fim no dia, separada das campanhas
com outro objetivo (decisão do Rodrigo). O detalhe está no `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.3.

### 2.9 O lançamento pago junto do clássico — decisão do Rodrigo, VARIAÇÃO ISOLADA

**O que entra:** o lançamento pago (LPSG) pode seguir vendendo ingresso durante o clássico. Antes, a casa pausava o pago
no clássico.

**Por quê:** depois de um clássico, o pago vende ingresso fácil.

**A condição de saída:** se der muito ruim, para de fazer os dois juntos. Se o pago antecipa a demanda do clássico segue
aberto (*PADRÃO INCONCLUSIVO*): a medição pelo e-mail mostrou sobreposição pequena, e a leitura pelo total de compradores
do ciclo não fechou.

## 3. Antecedência: a copy 2 a 3 dias antes, e o agendamento na véspera — VARIAÇÃO ISOLADA (2 lançamentos, o mesmo modelo)

| Disparo | Copy | Agendamento |
|---|---|---|
| E-mail da semana das aulas | 3 dias antes | na véspera |
| WhatsApp da semana das aulas | 2 dias antes | na véspera |
| E-mail e WhatsApp do carrinho | 3 a 4 dias antes | na véspera |
| API do dia 1 do carrinho | 4 dias antes | 3 dias antes |

Escrever e agendar são duas tarefas separadas, e a copy aprovada fica num documento antes de ir pra ferramenta de envio.

## 4. Regras transversais

1. **Tudo é contado a partir da aula 1 (D0) e da abertura do carrinho (D+7)**, como no calendário do §1. Se o lançamento
   tem rotina agendada, ela lê esse calendário de um arquivo do lançamento, e não se cria rotina com o nome do lançamento
   (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md`).
2. **O e-mail sai do mais quente pro menos quente, em ondas** (quem clicou, quem abriu, o resto).
3. **O "é hoje" de cada aula roda em campanha própria**, com início e fim no dia, separada da gravação, que dura vários
   dias.
4. **As lives e as aulas são gravadas pensando em reprisar.** Uma aula reprisada já converteu menos que a original, com
   outras variáveis mudando junto: a reprise não está isolada como causa.

## 5. O que transfere e o que é do caso

**Deve transferir (não testado em outro cliente):**
- o calendário em D±;
- a ordem das fases e o que se repete em cada uma;
- a antecedência de copy e de agendamento;
- a abertura com a lista VIP 1 hora antes;
- a sequência carrinho, reabertura, downsell e pago;
- a régua do debriefing.

**É do caso:** as datas do caso-base; o produto, os preços e a plataforma; o número de lives de aquecimento, que cresceu
com o arsenal do expert; a live semanal dele como porta de captação orgânica; o carrinho até a metade do mês, ligado ao
avatar que depende da renda mensal.

## 6. Pontos em aberto

1. **O lançamento pago antecipa a demanda do clássico?** — *PADRÃO INCONCLUSIVO* (§2.9). O que separa as leituras é um
   clássico depois de um período sem pago.
2. **A aula reprisada converte menos?** (`sirius-scale/frameworks/lancamentos/cpl-3-aulas.md`, Pontos em aberto 2).
3. **Duas melhorias apontadas em mais de um debriefing e ainda não testadas:** os scripts de objeção pro carrinho (que
   viraram a live do muro, `sirius-scale/frameworks/lancamentos/cpl-3-aulas.md` §7) e a UTM de inscrição durante as
   lives ao vivo.
4. **A reabertura** rodou uma vez, e o resultado dela separado não existe.
5. **"Aula 1 nunca em feriado"** é recomendação de um debriefing, não decisão: uma aula 1 caiu num feriado, num lançamento
   que converteu abaixo dos outros.
6. **O dia do replay das aulas no carrinho** (§2.5, regra 7).
