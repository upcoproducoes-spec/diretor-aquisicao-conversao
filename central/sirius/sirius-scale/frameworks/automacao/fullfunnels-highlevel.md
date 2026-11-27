# Full Funnels (HighLevel / LeadConnector) — acesso e armadilhas

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma. **Alcance:** UNIVERSAL — é comportamento da
> ferramenta, vale pra qualquer conta.
> **Confiança:** CONSISTENTE no que está medido (testado em duas contas, com
> resposta lida de volta).
> **Fato de plataforma:** endpoint, tela, número de ferramentas do MCP e limite são
> os da época da medição. A ferramenta muda: conferir antes de confiar.

O "Full Funnels" é um whitelabel do **HighLevel**; a API e o MCP são os do
LeadConnector. Doc: `marketplace.leadconnectorhq.com/docs/`.

## 1. Autenticação: token, não OAuth — *e é isso que faz funcionar aqui*

O MCP fica em `https://services.leadconnectorhq.com/mcp/` e aceita **Private
Integration Token** no cabeçalho, além de OAuth. **No Full Funnels, o token é o
caminho certo**: funciona em qualquer sessão do Claude Code e em tarefa agendada.
A regra é só deste MCP: **no Full Funnels, ligue pela chave, não pelo botão de
conectar.** Dash Fácil e Meta se ligam pelo conector, como está em
`sirius-scale/instalacao/mac.md` e `sirius-scale/instalacao/windows.md`.

Dois cabeçalhos, sempre os dois:

```
Authorization: Bearer pit-...      # Configuracoes -> Integracoes Privadas
locationId: <id da sub-conta>      # Configuracoes -> Perfil do Negocio,
                                   # ou o trecho depois de /location/ na URL
```

**O `locationId` é o que separa uma conta da outra**, e por isso duas contas
convivem sem conflito — cada uma é uma entrada própria na configuração de MCP,
com seu par de credenciais. Nomear pelo dono (`fullfunnels-<dono>`), nunca por
número: nome ambíguo é como dado de um cliente vaza pra análise de outro.

Na casa, duas contas ficam ligadas (de duas empresas diferentes), as duas sob a
mesma company (a agência). 36 ferramentas disponíveis em cada: contatos,
conversas, oportunidades, calendário, pagamentos, blog e social.

## 2. O handshake NÃO valida o token — *CONSISTENTE (reproduzido com token falso)*

`initialize` responde `serverInfo: ghl-mcp 1.0.0` **mesmo com um Bearer
inventado**. Quem valida é a chamada de ferramenta. Então "conectou" não prova
nada: pra testar credencial de verdade, chamar `locations_get-location` e
conferir o **nome da conta** que volta. É a mesma regra da casa de sempre —
escrita (e acesso) só conta com leitura de volta.

**E o contrário também engana: 401 no conector não prova chave vencida.** Na
casa, a configuração do MCP montava o cabeçalho a partir de uma variável de
ambiente (`Bearer ${VARIAVEL}`, mais o `locationId` por variável), e o app do
Claude não carregava o arquivo de variáveis: a variável chegava vazia e o
servidor devolvia `AUTH_HEADER_REJECTED` (HTTP 401, `invalid_token`) no início
da sessão. As mesmas chaves, testadas direto na API (`GET /locations/<id>`, com
o cabeçalho `Version: 2021-07-28`), voltavam 200 com o nome da conta, e o
endpoint do MCP (`tools/list`) também respondia. A casa chegou a dizer que a
chave precisava ser renovada — errado.
- **Antes de dizer que a chave venceu:** testar a chave direto na API, sem
  imprimir o token. Se responder 200, o problema é a variável não chegar no app,
  não a chave. Enquanto o conector não estiver consertado, o caminho é a API
  direta com a mesma chave.
- **O conserto da casa:** tirar os servidores do arquivo de MCP versionado do
  repositório (token literal ali vazaria no git) e pôr na configuração de MCP do
  usuário, fora do repositório, com o token literal no cabeçalho, sem depender
  de expansão de variável. Vale a partir da sessão seguinte. Mexer em
  configuração do Claude é decisão do dono.

## 3. `urllib` do Python é barrado pelo Cloudflare; `curl` passa — *CONSISTENTE (2 contas, 2 tentativas)*

Chamada idêntica, credencial idêntica: pelo `urllib.request` volta **HTTP 403
com erro Cloudflare 1010** ("banned based on your browser's signature"), pelo
`curl` volta 200. É bloqueio por assinatura do cliente HTTP, **não é credencial
errada** — e o 403 não diz isso em lugar nenhum, então é fácil perder tempo
procurando erro no token.

Ao escrever script novo pra esta API: usar `curl` (ou `requests` com
User-Agent de navegador), nunca `urllib` puro. Se aparecer 403 aqui, **ler o
corpo da resposta antes de mexer na credencial** — o código 1010 está lá.

## 4. Mensagem e disparo pra lead: o pedido de quem opera é a autorização

**Decisão do Rodrigo, que substituiu a regra antiga deste parágrafo**
("mensagem pra lead sempre é aprovada pelo Rodrigo"): *"isso aí não é verdade… quero tirar todas
essas travas para dar mais liberdade para […]… quando se trata de operação, de lançamento ou
perpétuo, tudo que envolve o marketing, ela não pode ter esse tipo de trava, tem que executar sem
travar."* O pedido escrito da gerente de operação (ou do dono) **é** a autorização: e-mail,
WhatsApp, disparo programado por tag, modelo, automação, tag, contato e pipeline no Full Funnels.
A execução lê de volta e responde por escrito o que ficou programado (quando, pra qual tag,
quantos contatos). Do lado de vocês, quem autoriza o quê segue `sirius-scale/REGRAS.md` §6.

- **Caminho:** API/MCP primeiro; o que a API não cobre (envio em massa, campanha de e-mail,
  automação) vai por navegador automatizado com a sessão logada, conferindo a conta antes e lendo
  de volta depois. Não oferecer "deixo pronto pra alguém programar" quando dá pra programar.
- **Disparo programado por tag sai por API, sem tela (medido num disparo de 291 e-mails):**
  `POST /contacts/search` com filtro `tags contains <tag>` (pageLimit 100, `page`), tira `dnd` e
  `validEmail=false`, e `POST /conversations/messages` por contato com `type=Email`, `emailFrom`
  (`Nome do Expert <e-mail do domínio do expert>`), `subject`, `html` e
  `scheduledTimestamp` (UTC, segundos). Volta `messageId`; `GET /conversations/messages/email/<id>`
  mostra `status: scheduled` até a hora.
  ⚠️ **E-mail programado cancela pelo id do e-mail:** `DELETE /conversations/messages/email/<emailMessageId>/schedule`
  responde 200 ("Cancelled the scheduled email successfully!"). O genérico,
  `DELETE /conversations/messages/<messageId>/schedule`, responde 400 `CONVERSATIONS_MSG_NOT_FOUND` pra
  e-mail: foi assim que as 1.665 mensagens de um envio falharam ao cancelar, com a versão anterior
  desta linha dizendo o contrário. Depois do cancelamento o status do e-mail continua `scheduled`; a
  prova é ele sumir de `GET /conversations/<conversationId>/messages`. UNIVERSAL (é a API).
  ⚠️ **Erro do Full Funnels nem sempre quer dizer que nada aconteceu** (num dia em que a ferramenta
  demorava pra responder). Um caso de cada lado:
  1. Cancelar: 2 de 1.670 voltaram 400 com timeout do Cloud Tasks (`Total timeout of API
     google.cloud.tasks.v2.CloudTasks exceeded 20000`). Na 2ª tentativa veio 400 "No email found with
     id", e o e-mail já tinha saído da conversa. Depois de um erro, conferir a conversa e contar como
     cancelado o que sumiu dela. A API não mostra se a tarefa de envio morreu junto: PADRÃO INCONCLUSIVO
     até um caso desses passar da hora marcada sem o e-mail sair.
  2. Agendar: 1 de 2.023 deu ReadTimeout no `POST /conversations/messages`, e o Full Funnels criou o
     e-mail mesmo assim (estava na conversa, `scheduled`). Contar isso como falha fazia a rodada
     seguinte mandar de novo. Antes de contar falha, procurar o e-mail na conversa (mesmo assunto,
     criado na rodada). VARIAÇÃO ISOLADA.
  3. Agendar com HTTP 500: um envio raro volta 500 em todas as tentativas (repetir 429 e 5xx, inclusive no `POST`). Dessa vez
     o Full Funnels não criou nada: a conversa do contato tinha um e-mail só, o registrado. O risco fica: se um 500
     vier depois de criar, cada nova tentativa deixa um e-mail que nenhum registro conhece e que o cancelamento não
     alcança. Confira lendo a conversa do contato (o cancelado some dela). PADRÃO INCONCLUSIVO (1 caso).
  ⚠️ E-mail pela API **não leva rodapé de descadastro** (campanha e automação levam): pôr no HTML
  `<a href="{{email.unsubscribe_link}}">`, que o servidor preenche (`{{unsubscribe_link}}` sai vazio).
  Mandar antes um teste pra uma caixa da equipe e ler de volta. VARIAÇÃO ISOLADA.
- **Continua com o dono do negócio:** ativar campanha paga e mexer em verba (`sirius-scale/REGRAS.md`
  §6) e o que é financeiro (pagamento, cobrança, reembolso).
- Os cuidados de execução continuam (são de qualidade, não de permissão): conferir a tag e a
  contagem antes, horário no fuso de São Paulo, teste pra uma caixa nossa quando a ferramenta deixar.

### 4.1 E-mail só sai de documento aprovado, nunca de texto colado na conversa

**Decisão do Rodrigo:** *"Primeiro tem que ser feito, escrito, na verdade, no Google Docs e colocado na
pasta certa, no Drive, com a nomenclatura certa."* Só depois disso se programa o envio. Quem autoriza o
envio segue `sirius-scale/REGRAS.md` §6.
A mecânica é VARIAÇÃO ISOLADA: nasceu no caso de origem e rodou pela primeira vez em dois envios (635 e
1.664 contatos), zero falha, leitura de volta `scheduled`.

- **O caminho é um só.** Na casa é um script de envio, que não vem no kit. O texto que sai é o do
  documento, lido na hora: nada de texto colado no pedido nem montado na conversa. O que ele barra em
  código vale como checklist antes de programar, à mão ou pedido ao Claude:
  1. nome fora de `EMAIL NN - ASSUNTO - TAG` (`sirius-scale/frameworks/operacao/nomenclatura-drive.md`
     §2) ou com `[RASCUNHO]`;
  2. documento fora da pasta de notificações e automações do projeto, ou ainda em `0) EM APROVAÇÃO`;
  3. TAG do nome diferente da tag do lançamento;
  4. marcação pendente (`[[CONFIRMAR…]]`, `[LINK…]`);
  5. programar sem um teste do mesmo texto nas últimas 48 h;
  6. horário a menos de 5 min ou a mais de 30 dias;
  7. mais de 10.000 contatos;
  8. o mesmo envio duas vezes;
  9. sem o pedido escrito de quem decide.
- **Formato do documento:** um bloco por e-mail com título `EMAIL NN - <ASSUNTO>`, depois `Assunto:`
  (ou `Assunto (A):` / `Assunto (B):`), `Pré-cabeçalho:`, o corpo, e o botão numa linha só com o texto
  entre colchetes ligado ao link (`[QUERO ASSISTIR À LIVE](https://…)`). Linha inteira entre parênteses
  é instrução e não vai no e-mail (`sirius-scale/frameworks/copy/padrao-de-copy.md` §3); `[nome]` vira o
  primeiro nome do contato. No `.md` que sobe pro Drive, uma linha em branco entre todas as linhas: o
  conversor markdown → Docs junta linha com quebra simples num parágrafo só, e o assunto, o
  pré-cabeçalho e o corpo virariam uma linha.
- **Por que existe:** numa rodada, a rotina montou o envio na hora e o Claude Code barrou ("o sistema
  bloqueou o envio automático desta rodada"), e a gerente de operação cancelou e mandou na mão. Comando
  conhecido entra na lista de permissões do projeto; chamada solta, não. O bloqueio era técnico, não
  regra da casa.
- **Estatística:** o envio é contato a contato, então não aparece em Marketing > E-mails > Campanhas (a
  API pública não cria campanha). O resultado se lê mensagem a mensagem (§4.2): entregue, aberto,
  clicado, falhou. O registro do envio guarda só ids de mensagem, sem dado de lead.
- **Programar contato a contato leva de 1 a 1,6 s por e-mail** (medido com outra varredura dividindo o
  limite da conta): 1.664 levaram uns 45 min. Agendar em paralelo ajuda, mas o limite da conta é 100
  chamadas a cada 10 s, então somar as rodadas que estiverem no ar antes de subir o número. Programar
  uma semana de envios de uma vez é trabalho de horas: começar cedo e pelo que sai primeiro.
- **Dois pedidos (decisão do Rodrigo):** o de copy entrega o documento pra revisão; o de agendar espera
  o de copy e só roda depois do aprovado.
- **Do mais quente pro menos, sempre** (Rodrigo: "todos disparos devem ir segmentados do mais quente para
  o menos"). Uma onda por camada, 30 min entre elas: quem clicou em e-mail (`email-clicou`), quem abriu
  (`email-engajado`, ou `email-abriu`, herdada do Mailchimp) e o resto. Base: no mesmo e-mail, com o
  mesmo assunto, quem tinha aberto o anterior abriu 19,0% e quem não tinha abriu 0,4%, no Mailchimp. O
  resultado se lê por onda. Lista nova não tem histórico (numa lista de 1.713 inscritos, só 24 tinham
  a etiqueta), e a primeira onda cresce conforme os envios.
- **Quem engaja é etiquetado pelo próprio Full Funnels, na hora.** Dois fluxos publicados com o gatilho
  **Email Events** (filtro Event = Opened / Clicked; os outros eventos do filtro são Bounced,
  Complained(SPAM) e Unsubscribed): o de abertura põe `email-engajado`; o de clique põe `email-clicou` e
  `email-engajado`. Reentrada ligada (padrão), sem janela de horário. Fluxo não olha pra trás: o
  histórico vem de uma varredura pela API (§4.2). Se o gatilho pega também o e-mail que sai pela API
  contato a contato ainda **não foi medido**.
- **Inscrição começada e não enviada:** o Dash grava o que a pessoa digita antes do clique, e quem
  desiste fica fora do Full Funnels. Na casa, um script cruza o Dash, as etiquetas e a cópia do
  formulário e põe essas pessoas com uma etiqueta própria, pro e-mail de recuperação (648 pessoas numa
  rodada).
- **Falha permanente sai da lista:** etiquetar quem falhou (`email-falhou`) e tirar do público. Medido
  numa auditoria: 362 endereços que falharam no 1º e-mail de uma sequência receberam o 2º e o 3º.
- **Documento ainda em revisão pode sair, se quem decide mandar.** O Rodrigo: "Já programar todos.
  Mesmo que a gente vai revisar os próximos, se precisar, a gente altera." A frase dele fica no registro
  do envio, e pasta errada continua barrando. O que muda na revisão volta por uma conferência: listar o
  que está por sair com texto diferente do documento, cancelar e reprogramar. O mesmo e-mail não se
  programa de novo enquanto o anterior não sair ou não for cancelado.
- **Envio programado com antecedência congela o público** (a API agenda contato a contato na hora de
  programar). Numa captação que segue até a live, isso deixava de fora quem se inscreve depois e
  mandava convite pra quem já se inscreveu. Antes de cada envio programado com antecedência, uma rodada
  de acerto: quem entrou ganha o mesmo e-mail na onda da camada dele (só se a onda está a mais de 5
  min), quem saiu tem a mensagem cancelada. O registro guarda uma marca de cada contato (hash), não o id.
- **Público cruzado:** dá pra somar etiqueta, tirar etiqueta e cruzar (aluno que já abriu e-mail = as
  etiquetas de aluno, cruzadas com as de engajamento). A busca por etiqueta da API casa a etiqueta exata
  (conferido em 12 etiquetas).
- **Modelo de e-mail por API, pra e-mail que sai por fluxo (medido uma vez):** `POST /emails/builder` com
  `{"locationId", "type": "html", "name", "title", "builderVersion": "2"}` devolve 201 e o `id`; o corpo
  entra com `POST /emails/builder/data` `{"locationId", "templateId", "updatedBy", "html", "editorType":
  "html", "dnd": {…}}` (201, devolve o `previewUrl`, que serve pra ler de volta);
  `GET /emails/builder?locationId=…&search=…` lista; `DELETE /emails/builder/{loc}/{id}` apaga. Acento
  passou com documento HTML completo (`<meta charset="utf-8">`, regra 5 da montagem pelo navegador). O
  assunto vai na ação "Enviar e-mail" do fluxo, com `{{contact.first_name}}` digitado no lugar do nome.
  ⚠️ **Correção medida em 11/2026:** quando o modelo já leva o pré-cabeçalho escondido no começo do corpo, o campo de
  pré-cabeçalho da ação fica **vazio**. Preenchido, o Full Funnels injeta outro (`div data-ghl-preheader`), o e-mail
  sai com os dois e a prévia da caixa de entrada repete a frase.

### 4.2 Estatística de e-mail sai pela API — *medido numa auditoria de conta (~1.550 chamadas, só leitura)*

A API **não cria** campanha, mas **lê** a estatística de tudo.

| O quê | Endpoint | Observação |
|---|---|---|
| Campanhas com números | `GET /emails/schedule?locationId=…&limit=100&showStats=true` (`Version: 2021-07-28`) | `totalCount`, `delivered`, `opened`, `clicked`, `failed`, `successCount` |
| Detalhe da campanha (assunto, remetente, reply-to, HTML) | `GET /emails/locations/{loc}/campaigns/emails` e `/{id}` (`Version: v3`) | 50 de 50 |
| Estatística completa da campanha | `GET /emails/locations/{loc}/campaigns/stats/email-campaigns/{sourceId}` (`Version: v3`) | ⚠️ `sourceId` é o `bulkRequestId`; com o `id` da campanha volta 400 (`Invalid sourceId`) |
| Passo de e-mail de fluxo | `GET /emails/locations/{loc}/campaigns/workflows` e `.../stats/workflow-campaigns/{sourceId}?subSourceId=` | assunto e remetente do passo vêm nulos |
| Status de cada e-mail | `GET /conversations/messages/email/{id}` | vai até `opened` e `clicked` (`clicked` substitui `opened`); bateu exato com uma campanha conferida |
| Todo e-mail que saiu | `GET /conversations/messages/export?channel=Email&startDate=…&limit=500` (`Version: 2021-04-15`) | traz assunto, `source` e corpo; o `status` fica em `sent`, então **não serve pra abertura** |

Armadilhas da mesma leitura:

1. O export às vezes devolve `total: 0` e página vazia; a mesma chamada, segundos depois, traz os dados. Resposta vazia não prova que não houve envio: repetir e conferir o `total`.
2. Pra recortar período no export, o que funcionou sempre: só `startDate`, `sortOrder=asc`, e parar na data de corte.
3. No envio em gotas (drip), o `dateScheduled` da `/emails/schedule` é a hora do **último** lote, não do primeiro.
4. `GET /conversations/messages/{id}` com o id do export volta 400; o de e-mail funciona.
5. `hasTracking` falso nas campanhas lidas não impediu o registro de abertura e clique. O que o campo liga não está documentado.

### 4.3 DNS do domínio de envio: o que olhar e como ligar o relatório de DMARC

O Full Funnels manda do domínio do expert por um subdomínio `mail.` (Mailgun via LeadConnector). Lido
na zona do caso-base, pela API da Cloudflare:

- **SPF:** a raiz tinha o include da hospedagem do e-mail; o `mail.` tem
  `include:mailgun.org include:spf.leadconnectorhq.com`.
- **DKIM:** `k2` e `k3._domainkey` apontavam pro Mailchimp (`dkim2/dkim3.mcsv.net`), herança da conta antiga.
- **DMARC:** era `v=DMARC1; p=none` sem `rua`, então ninguém recebia relatório. Ganhou `rua` apontando
  pro coletor da Cloudflare (`dmarc-reports.cloudflare.net`), e os relatórios aparecem no painel da
  zona, em Email → DMARC Management. A política continuou `p=none`: só monitora, não muda o caminho de
  nenhum e-mail.

**Como ligar, pra outra zona** (UNIVERSAL, fato de plataforma):
`PATCH /zones/{zone}/email/auth/dmarc-reports` com `{"enabled": true, "skip_wizard": true}`. A própria
Cloudflare acrescenta o `rua` no TXT `_dmarc`, e o `GET` do mesmo endereço confere. O token de API que
edita DNS recebeu "Authentication error" nesse endereço; funcionou pelo MCP da Cloudflare, logado com a
conta dona da zona.

**Em aberto:** o Google Postmaster Tools pede que o dono do domínio o adicione em
postmaster.google.com, com o login dele. O TXT de verificação que o Google der entra no DNS do mesmo jeito.

## 5. Em aberto

- Não testado: paginação, limite de chamadas e webhooks.

## 6. Modelo de WhatsApp não se cria por API — *medido uma vez*

- **A API pública não cria modelo de WhatsApp.** Varridos os 88 specs do repositório público
  `highlevel-api-docs`: o único endpoint de modelo é
  `GET/DELETE /locations/{id}/templates` (e-mail/SMS), e com `type=whatsapp` voltou 0 nas
  duas contas, mesmo com o WhatsApp oficial rodando numa delas. Criar é só na tela:
  Configurações → WhatsApp → Modelos (login em `go.fullfunnel.app`).
- **Modelo criado direto na Meta fica invisível pro Full Funnel.** O HighLevel importa os
  modelos da Meta uma vez, quando o número é conectado, e depois só enxerga o que foi criado
  pela tela dele (artigo de ajuda "WhatsApp Template Statuses and Best Practice" e um pedido de
  recurso aberto no portal de ideias). Criar pela API da Meta obriga a disparar pela
  Meta também: a mensagem chega, a resposta cai no Full Funnel, mas o que foi enviado não
  aparece na conversa.
- **Envio de modelo pela API do Full Funnel existe no papel:** `POST /conversations/messages`
  com `type: WhatsApp` + `templateId`. Não testado.
- **Contas e números:** no caso-base, o WhatsApp oficial de uma das contas conversava com os
  leads do expert (576 conversas de WhatsApp, 0 modelos cadastrados). A outra conta, de outra
  empresa, tinha número próprio — lead de um cliente nunca sobe na conta de outra empresa
  (dado de cliente não cruza empresa).
- **Token de usuário de sistema da Meta feito pra anúncio não serve pra WhatsApp.** Os tokens
  da casa só tinham escopo de anúncio, página e negócio. Criar modelo e disparar pela Meta exige
  `whatsapp_business_management` + `whatsapp_business_messaging` e a conta do WhatsApp atribuída
  ao usuário de sistema.

## 7. Pôr contato numa coluna de pipeline — *testado uma vez (1 contato, 1 conta)*

**VARIAÇÃO ISOLADA (1 teste, 1 conta).** Pedido da gerente de operação: subir uma lista num pipeline
e numa coluna. O Rodrigo liberou a primeira escrita no chat; o teste foi com o contato da própria
gerente (1 linha).

- **Sem MCP:** o conector seguiu em 401 (§2: a variável não chegava no app), então foi por API direta
  com o token guardado como variável de ambiente, via `requests` com User-Agent de navegador (§3),
  `Version: 2021-07-28`. Não imprimir o token.
- **Receita (3 leituras, 1 escrita, 1 leitura de volta):**
  1. planilha do Google Drive → CSV (export da API do Drive em `text/csv`);
  2. `GET /contacts/?locationId=…&query=<e-mail>` acha o contato já existente (não criar contato novo);
  3. `GET /opportunities/pipelines?locationId=…` dá `pipelineId` e o id de cada coluna (`stages`);
     `GET /opportunities/search?location_id=…&pipeline_id=…&contact_id=…` confere se já existe (não duplicar);
  4. `POST /opportunities/` com `pipelineId`, `locationId`, `name`, `pipelineStageId`, `status: "open"`, `contactId`
     (resposta 201); 5. `GET /opportunities/{id}` e conferir pipeline, coluna e contato.
- **Nome da coluna:** quem pediu disse "Leads"; no pipeline do comercial a coluna era **"Lead"**
  (singular). Casar por nome ignorando caixa, e mostrar o nome real na resposta.
- **Regra de processo:** antes de escrever numa lista grande, mostrar quantos contatos foram achados e quantos
  não, e só subir depois do ok de quem pediu. Contato que não está na base **não** se cria sozinho.
- Não testado: lista grande (paginação, limite de chamadas), mover oportunidade de coluna, contato sem e-mail
  (só telefone).

## 8. Pesquisa e formulário não se criam por API — *medido uma vez*

- **A API pública só LÊ pesquisa e formulário.** No spec oficial (`GoHighLevel/highlevel-api-docs`,
  `apps/surveys.json` e `apps/forms.json`): `GET /surveys/`, `GET /surveys/submissions`,
  `GET /forms/`, `GET /forms/submissions` e `POST /forms/upload-custom-files`. Não existe endpoint de
  criar ou editar. As 36 ferramentas do MCP também não criam (contatos, conversas, oportunidades,
  calendário, pagamentos, blog e social). **Não é escopo que falta: liberar permissão nova não resolve.**
- **Criar é só na tela** (construtor de pesquisa, login em `go.fullfunnel.app`). Automatizar, só por
  navegador.
- **Depois de criada, a API serve:** `GET /surveys/` dá o id pra pôr na página, e `GET /surveys/submissions`
  confere se a resposta chegou com os campos escondidos preenchidos (teste de ponta a ponta sem abrir a tela).
- **Dash:** o Dash Fácil lê a planilha da pesquisa no Drive, e o Full Funnels também grava a planilha lá
  (Rodrigo). Trocar Tally por Full Funnels não tira MQL e faixa do Dash, desde que a planilha nova
  seja ligada ao lançamento no Dash (nunca reaproveitar a de outro lançamento,
  `sirius-scale/frameworks/trafego/leitura-dash-facil.md` §8.3).


## 8.1 Campo personalizado se cria por API; atribuição nativa é só leitura — *medido uma vez*

- **A atribuição nativa do contato (`attributionSource`: utmSource, utmMedium, campaign, fbclid…)
  só aparece na leitura** (`GET /contacts/{id}`). O `UpsertContactDto` não aceita esse campo: ela
  é preenchida pelos formulários e pelo rastreio do próprio HighLevel. Formulário nosso manda UTM
  em **campo personalizado**.
- **Campo personalizado se cria por API:** `POST /locations/{locationId}/customFields` com
  `{"name", "dataType": "TEXT", "model": "contact"}` (spec `apps/locations.json`). O `fieldKey`
  vira `contact.<nome>`.
- **No upsert, a chave vai sem o prefixo:** `customFields: [{"key": "utm_source", "field_value": "FB"}]`
  gravou certo, lido de volta.
- Na conta da casa foram criados os seis (`utm_source`, `utm_medium`, `utm_campaign`,
  `utm_content`, `utm_term`, `utm_id`); cada um ganha um id próprio, que a leitura devolve. Antes
  deles a conta só tinha um campo de nota herdado do Mailchimp. Uso nas páginas:
  `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.2.

## 8.2 O contato se funde pelo TELEFONE — *VARIAÇÃO ISOLADA (2 cadastros de teste, 1 conta); o mecanismo é da plataforma*

- Dois cadastros de teste com e-mails diferentes e o **mesmo telefone** (o texto de exemplo do campo)
  viraram **um contato só**: o segundo sobrescreveu o e-mail do primeiro no mesmo registro, e um campo
  de data calculado no cadastro (o fim do período de teste grátis) foi recalculado por cima.
- **Por que importa em produção, não só no teste:** lead que digita telefone falso (comum em negócio
  local) se funde com todos os outros que fizeram o mesmo. Os fluxos de e-mail passam a disputar o
  mesmo contato, a data é reescrita a cada novo cadastro, e as esperas ancoradas nela saem erradas
  (a espera por data está em "O contorno do if/else", abaixo).
- **Pra testar:** `+alias` no e-mail não basta pra simular lead novo; o telefone também precisa ser
  diferente. E o contato achado pode ser antigo (o do teste existia havia meses), então "contato
  criado na última hora" não detecta o cadastro: buscar pelo e-mail, ou por `dateUpdated`.
- Conferir isso em todo formulário que escreve no Full Funnels, inclusive o upsert das páginas
  (`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.2).

## 9. Criar tag no Full Funnels

**Decisão do Rodrigo:** a gerente de operação pode pedir criação de tag no Full Funnels sempre que
quiser, sem passar por ele. Vale pra **criar etiqueta** na conta onde estão os leads do expert.
(Depois, contato, pipeline, mensagem e automação também foram liberados: ver §4.)

- **Receita:** `GET /locations/{locationId}/tags` (ler as existentes, comparar sem diferenciar caixa),
  `POST /locations/{locationId}/tags` com `{"name": …}` só pras que faltam, e `GET` de novo pra conferir.
  Token da conta (variável de ambiente), `Version: 2021-07-28`, User-Agent de navegador (§3).
- **Caso de uma Black:** as 7 tags pedidas (inscrito aluno e inscrito não aluno, pesquisa, grupo aluno e
  grupo não aluno, comprador da Black e reembolso da Black) já existiam na conta quando a criação rodou
  (41 tags no total). O Full Funnels guarda o nome em minúsculas — a tag é a mesma, o que muda é só a
  exibição.
- VARIAÇÃO ISOLADA (1 caso).
- **Caso low ticket:** 25 etiquetas `lt-*` criadas (201 em todas). A leitura feita logo em seguida
  mostrou 24 de 25; cinco segundos depois, as 25, sem duplicada. **A lista de etiquetas demora uns segundos pra
  refletir a criação:** esperar e ler de novo antes de concluir que falhou, e nunca recriar no impulso (gera
  duplicata quando a primeira chamada já tinha valido).

---

## Automação (workflow) não se cria por fora

Tentativa de montar dois fluxos sem ninguém clicar. **Não dá, e a causa não é
permissão nem navegador** — é arquitetura. Registrado pra ninguém repetir a investigação.

### As quatro portas, e por que cada uma fecha

| Caminho | O que acontece | Veredito |
|---|---|---|
| **API pública** (`services.leadconnectorhq.com`) com o PIT | `GET /workflows/` lista tudo; `POST /workflows/` responde `Cannot POST /workflows/` (404 de rota) | **lê, não cria** |
| **Clique na tela** (navegador embutido do Claude **ou** o Chrome com a extensão) | A tela de Automações inteira é um `<iframe>` pra `client-app-automation-workflows.leadconnectorhq.com`. Cliques sintéticos não entram; a árvore de acessibilidade só devolve o menu lateral. Testado em dois alvos (botão "Criar fluxo de trabalho" e uma pasta): zero efeito | **bloqueado nos dois navegadores** |
| **Abrir o app do iframe direto** na barra de endereço | Carrega e fica em spinner pra sempre: ele recebe o token do painel-pai por `postMessage` | **não carrega sozinho** |
| **Backend interno** (`backend.leadconnectorhq.com`) | Autentica **só** com o cookie de sessão `access-token-v2` + `Authorization: Bearer`. O PIT leva 401. E o CORS do backend libera o domínio do app de workflows, **não** `go.fullfunnel.app` — então o POST feito de dentro do painel morre no preflight | **leitura sim, escrita não** |

### O que ficou sabido (e serve pra ler, que é permitido)

- Headers do backend interno: `version: 2021-04-15`, `source: WEB_USER`, `channel: APP`,
  `Authorization: Bearer <cookie access-token-v2>`. Rota de listagem:
  `GET /workflow/{locationId}`. Um workflow específico: `GET /workflow/{locationId}/{id}`.
- **Os passos não moram no banco.** O registro traz `filePath`/`fileUrl` apontando pro
  Firebase Storage; o conteúdo é `{"templates":[...]}`, lista encadeada por `next`:
  `{id, order, name, type, attributes, next}`. `if_else` tem `next` como **array** e
  `attributes.branches[].segments[].conditions[]`.
- O Firebase bloqueia `fetch` cross-origin; pra ler, navegue a própria página até o
  `fileUrl` (navegação não passa por CORS).

### A regra prática

**Modelo de e-mail sobe por API; automação é na tela, com alguém clicando.** O que o agente
consegue fazer sozinho: subir e conferir os modelos, ler os workflows que existem e
conferir o que foi montado. O que precisa de mão humana: criar o fluxo e ligar os passos
(ou um navegador automatizado, na seção seguinte).

⚠️ **Não extrair o cookie de sessão pra fora do navegador.** Ele é a sessão inteira da
conta, e a extensão corretamente recusa devolver cookie no retorno do JS. Chamada que
precise dele se faz dentro da página, nunca copiando o valor pra um script.

## Montar automação pelo navegador: o que responde e o que não

Com um navegador automatizado por CDP (no caso, o `agent-browser`) e um perfil permanente logado,
**dá pra montar fluxo sozinho** — o clique entra no iframe, ao contrário da extensão. Mas nem todo
componente do construtor aceita automação. Medido montando o primeiro fluxo inteiro:

| Componente | Responde? | Como |
|---|---|---|
| Campo de texto, nome, assunto, prévia | sim | `fill` por ref |
| Botão comum, aba, salvar, excluir | sim | `click` por ref |
| Checkbox (dias da semana) | sim | `click` por ref |
| Dropdown simples (unidade de tempo) | sim | clique por coordenada |
| **Radio de "Selecionar modelo existente"** | só por teclado | `focus` no radio + `Space` |
| **Seletor de operador do if/else** | **não** | fica em "carregando" pra sempre |
| **Seletor de fluxo em "Remover do fluxo de trabalho"** | **não** | não abre de jeito nenhum |

⚠️ **O seletor de operador funciona no GATILHO e falha no if/else** — então não é a
conta nem a plataforma inteira: é o componente. Testado com dois campos diferentes
(data e tags) e com a página recém-carregada.

### Regras que nasceram disso

1. **A tela mente; o servidor não.** Confira todo passo lendo o workflow de volta:
   `GET /workflow/{loc}/{id}` dá o `fileUrl`, e o arquivo traz `{"templates":[...]}` com
   tipo, nome, `startAfter`, `window` e `template_id` de cada passo. Montando o primeiro fluxo,
   a tela escondeu **dois e-mails duplicados** (que pareciam ter falhado) e **dois
   e-mails sem corpo** (salvos só com assunto, porque o modelo é opcional no save).
2. **O canvas é virtualizado.** Nó fora da área visível some do DOM: ajuste o zoom
   ("Ajustar à tela") antes de procurar um nó ou o `+` final.
3. **O `+` de cima insere ANTES do nó, o de baixo insere DEPOIS.** Pegue sempre o de
   maior `y`; e `get box` devolve decimais com zoom, que quebram comparação de inteiro
   em shell.
4. **O botão que confirma exclusão chama "Apagar"**, não "Delete" — e a exclusão só
   vale depois que o fluxo salva.
5. **Modelo de e-mail subido por API precisa ser documento HTML completo**, com
   `<meta charset="utf-8">`. Fragmento solto quebra todo acento no editor, mesmo com os
   bytes certos na API.

### Pelo navegador embutido do Claude, com a pessoa logada (medido depois da tabela acima)

Montando fluxos de engajamento e um de recuperação de inscrição, com o Rodrigo logado no painel do app
do Claude. Aqui o clique entrou, ao contrário do que a tabela das quatro portas registra pra esse
navegador; não se sabe o que mudou, então testar antes de planejar:

- **O radio "Selecionar modelo existente" respondeu ao clique** (no navegador automatizado por CDP só ia
  por teclado). A lista mostra os modelos subidos por API, com a etiqueta `Editor de código`.
- **Gatilho "Tag de contato" com filtro "Tag adicionada":** a própria tela avisa que só dispara pra
  etiqueta posta depois de publicar (e manda usar a inscrição retroativa pra quem já tem a etiqueta).
  Por isso o envio pra quem já tinha a etiqueta vai por fora, e o fluxo cobre quem entra depois, sem
  duplicar.
- **Gatilho "Email Events":** o filtro Event tem Bounced, Clicked, Complained(SPAM), Opened e
  Unsubscribed, e há um filtro "In workflow" pra restringir a um fluxo.
- **A tela atrasa:** campo digitado logo depois de um clique vai parar no campo anterior (o nome do
  fluxo foi parar na busca de gatilho; duas etiquetas viraram uma só palavra). Clicar, esperar 2 s,
  conferir na captura, só então digitar; em lista, escolher com Enter depois de a opção aparecer destacada.
- **A interface mudou de inglês pra português no meio da sessão:** buscar gatilho e ação pelo nome que
  aparece na tela ("Tag de contato", "Enviar e-mail"), não pelo nome em inglês.

### Passo "Enviar e-mail" salvo sem corpo — VARIAÇÃO ISOLADA na causa, CONSISTENTE no efeito (duas vezes)

Trocando o assunto de um fluxo pra maiúscula, o teste mostrou que o e-mail saía **vazio**: só o
pré-cabeçalho escondido e o rodapé de descadastro. O fluxo estava assim desde a montagem, dois dias
antes, e nunca tinha disparado (0 inscritos), então nenhum lead recebeu. É a mesma armadilha dos dois
e-mails sem corpo da regra 1 acima.

1. **Escolher o modelo é clicar no ✓ à direita da linha, não no nome.** O nome só destaca a linha; o
   passo salva sem corpo. Ligado de verdade, o painel mostra a prévia e "Linked template: <nome do modelo>".
2. **O painel do passo sempre reabre em "Quick compose" com a mensagem vazia**, mesmo com o modelo
   ligado, e já abre com "alterações não salvas". Salvar o passo sem religar o modelo apaga o corpo.
   Regra: qualquer edição no passo de e-mail, até só o assunto, religa o modelo (✓) antes de "Save action".
3. **"Sync Edits to Template" empurra o passo pro modelo e vice-versa.** Com o passo possivelmente
   vazio, ligar pode apagar o modelo. Ficou desligado; por isso atualizar o modelo pela API talvez não
   mude o passo (não medido). Depois de atualizar o modelo, religar o ✓ no passo e testar.
4. **A tela não prova nada; a prova é um envio.** `POST /contacts/{id}/workflow/{wf}`
   (`Version: 2021-07-28`, corpo `{}`) põe um contato da equipe no fluxo e ele dispara na hora;
   `GET /conversations/messages/email/{id}` traz o `body` do que saiu. O fluxo não deixa reentrar
   ("Skipped" no Execution logs): o 2º teste vai pra outro contato da equipe, combinado antes.
5. **Ler o fluxo pelo backend interno ficou bloqueado** pelo classificador do Claude Code ("Browser JS
   Exfil", ler o cookie de sessão na página). O teste por envio substitui a leitura.

### O contorno do if/else, que é melhor que o original

A espera **"Até uma data/hora específica"** aceita **variável do contato** (3 pontinhos →
Dinâmico → seletor de variáveis), e traz dois controles que dispensam condição:

- **"Quando o contato deve proceder?"** — nesta data / **antes desta data** / após esta data
- **"Se esta data já passou"** — prosseguir / sair da automação / ir pra etapa /
  **pular todas as comunicações até a próxima espera** (padrão)

Então "faltando 2 dias pro fim do trial" vira uma espera ancorada em `Fim do trial`, e
quem concluiu tarde é tratado pela própria ferramenta, sem ramo condicional. **Use isso
em vez de if/else sempre que a régua for uma data.**

### Mais seis pegadinhas, medidas montando o segundo fluxo

1. **O botão que confirma exclusão alterna entre "Delete" e "Apagar"**, conforme a
   tradução termina de carregar. Procure os dois, com retry — procurar só um falha
   silenciosamente e a etapa continua lá.
2. **Trocar de fluxo sem reiniciar o navegador quebra o canvas**: os nós param de
   renderizar (só sobram as arestas e os `+`). Fechar todas as sessões do navegador
   automatizado e abrir de novo resolve. Vale também quando o canvas simplesmente para de
   mostrar os nós.
3. **O `+` pode devolver o mesmo ponto de inserção duas vezes seguidas** se o snapshot
   não atualizou entre uma ação e outra — foi assim que dois passos entraram trocados.
   Confira a ordem no servidor depois de **cada** inserção, não no fim.
4. **Para inserir entre dois nós**, pegue o `+` cujo `y` fica entre os `y` dos dois.
   O de maior `y` do canvas inteiro só serve pro fim da fila.
5. **O campo "Do nome" às vezes ignora o primeiro `fill`** (volta vazio na leitura do
   servidor). Clicar no campo por coordenada e digitar com `keyboard type` funciona
   onde o `fill` falha. Confira sempre lendo de volta.
6. **O remetente padrão do fluxo** (Configurações → Detalhes do remetente) **não aceita
   digitação por automação** — nem clique, nem teclado. Resta preencher em cada ação de
   e-mail, onde o campo é um `textbox` de verdade.

### Mais pegadinhas, medidas montando o roteador do low ticket

*VARIAÇÃO ISOLADA: um fluxo (o que recebe o webhook da Hotmart, publicado), 4 ramos de ~25 passos
cada, montados por navegador automatizado com o Rodrigo na conversa.*

1. **A leitura de volta mais direta é o corpo do PUT do próprio construtor.** Depois de "Salvar", a
   requisição PUT no log de rede do navegador traz em `postData` o fluxo inteiro (`workflowData.templates`)
   e as listas `createdSteps` / `modifiedSteps` / `deletedSteps`. Dá pra conferir passo por passo sem
   abrir o `fileUrl`, e o `modifiedSteps` vazio prova que nada fora do ramo mexeu. ⚠️ O mesmo retorno
   traz os cabeçalhos da sessão (`Authorization`): ler só o `postData`, nunca imprimir nem gravar o resto.
2. **"Ajustar à tela" para em 20% e não mostra um fluxo largo inteiro.** Nó fora da tela some do DOM (o canvas é
   virtualizado). Arrastar o canvas (mouse down / move / up numa área vazia do alto) traz o nó; a rodinha não rola.
3. **O seletor de etiquetas carrega devagar e o clique pode pegar o 1º item da lista sem filtro.** No "Remova tag"
   de um dos ramos entrou uma etiqueta de reembolso da Black no lugar da etiqueta de Pix pendente daquele produto
   (e o total de chips subiu igual, então contar chips não pega). Antes de clicar, ler o texto da 1ª opção: o
   menu fica no fim do snapshot, depois do último "Salvar ação". Em 3 de 15 linhas da trava a 1ª opção ainda era
   "No Data" ou outra etiqueta quando a busca foi digitada. O ícone "loading" fica no DOM mesmo parado: esperar
   por ele não serve; espera fixa de 4 s antes e depois de digitar funciona.
4. **O autocompletar "Valores personalizados" abre no campo de valor e cobre o "Adicionar campo".** `Tab` e `Escape`
   não fecham; clicar no rótulo "CAMPOS" (logo acima da 1ª linha) fecha, mas só com o painel no topo (ver o 10).
5. **Variável digitada direto no valor funciona** (`{{inboundWebhookRequest.data.buyer.phone}}`) e é gravada como
   digitada. Se ela não existe no exemplo do gatilho, o construtor pinta de laranja e avisa "nenhuma etapa fornece
   este valor": é só aviso, porque o exemplo é um evento antigo.
6. **Condição por etiqueta:** Contact details → Standard fields → Tags; operadores Inclui / Não inclui / Não está em
   branco / Está em branco. "Não inclui" é gravado como `contact_detail · tags · index-of-false`. Campo personalizado:
   Contact details → Custom Fields; "Está em branco" vira `has_no_value`.
7. **"Remova tag de contato" tem o interruptor "REMOVER TODAS AS TAGS".** Nunca ligar: tira as etiquetas do lançamento
   e da Black do contato. Na casa, a conferência do fluxo reprova se ele aparecer.
8. **O balão do assistente de atendimento da ferramenta cobre o painel da direita.** Esconder só a região dele
   (`aria-label`), no navegador automatizado. Subir 3 níveis no DOM a partir do link do WhatsApp escondeu o app
   inteiro (tela branca); voltar o `display` resolveu.

Mais quatro, da correção do mesmo roteador, na madrugada seguinte:

9. **Com 4 linhas ou mais, o painel da ação rola e o "Adicionar campo" fica abaixo da tela.** O clique por coordenada
   cai fora da janela e não faz nada. Rolar até o elemento (trazer à vista) antes de ler a caixa dele.
10. **Com o painel rolado, o clique do item 4 caiu no botão "Testar fluxo de trabalho".** O rótulo "CAMPOS" rola junto
    com a lista; "30 px acima da 1ª linha" virou o topo da página. Abriu o painel de teste no lugar da ação e a edição
    se perdeu. Nenhum teste rodou, porque nenhum contato estava escolhido, mas num fluxo publicado o teste inscreve
    contato de verdade (seção abaixo). O clique pra fechar o autocompletar passou a ir no subtítulo do cabeçalho do
    painel, que não rola, e logo depois a automação confere que "Salvar ação" continua na tela.
11. **O navegador automatizado recarregou sozinho no meio de uma etapa.** Foi pra raiz do app (painel de controle) e
    voltou com outra altura de tela (857 em vez de 1000, e todas as coordenadas contavam com 1000). O que não estava
    salvo se perdeu; nada ficou salvo pela metade, porque o salvamento só acontece no fim da etapa. Desde então cada
    etapa confere endereço e tamanho da tela antes de começar e salva quando termina. Etapa interrompida se refaz
    inteira, e os passos pulam o que já existe.
12. **A condição de webhook aceita variável no valor, mas ainda não se sabe se o motor resolve.** Digitar
    `{{contact.lt_transacao}}` vira o chip azul "Contact . Custom Fields . lt_transacao" (o campo tem seletor de
    variáveis), e o valor é gravado como texto em `conditionValue`. A ajuda do HighLevel (o artigo sobre condições
    de fluxo) só documenta "valor dinâmico" pra condição de número, data, lista e dinheiro, escolhido no seletor.
    PADRÃO INCONCLUSIVO até um evento real passar por ela: conferir em Registros de execução.

### Montagem do fluxo pela tela: mais dez fatos (11/2026) — *VARIAÇÃO ISOLADA (três fluxos de uma conta)*

1. **Fluxo publicado não grava no "Salvar ação".** Aparece o botão "Salvar" no topo, com um ponto vermelho, e a mudança
   só vale depois do aviso "O workflow foi salvo". Rascunho grava sozinho ("Salvo(a)"). Publicar é a chave
   "Rascunho/Publicar" do topo.
2. **Pré-cabeçalho:** com o corpo vindo de modelo que já leva o pré-cabeçalho escondido, o campo da ação fica vazio (§4.1).
3. **O painel do e-mail pode reabrir com "Modelo associado"** ou em "Composição rápida" vazia. Quando abrir sem o
   "Modelo associado", religar o modelo antes de salvar, senão o passo fica sem corpo.
4. **Espera "Até que uma janela recorrente se abra":** frequência semanal, dias marcados e hora; mostra as 5 próximas
   ocorrências no fuso da conta. Vem com segunda a sexta marcados: marcar sábado e domingo quando a venda é todo dia.
   "9h da manhã seguinte" = espera de 8 horas + janela das 9h.
5. **Dois fluxos com o mesmo gatilho não se esperam.** Se o fluxo B pergunta por uma tag que o fluxo A põe com o mesmo
   gatilho, quem perder a corrida não recebe nada. O certo é o B disparar pela tag que o A põe (dispara em uns 10 s).
6. **No If/else, os blocos ("segmentos") têm um E/OU próprio**, separado do E de dentro de cada bloco. "Mês X e dia ≥ 30"
   **E** "mês Y e dia ≤ 6" nunca é verdade: tem de ser OU.
7. **Excluir:** passo pelo menu ⋯ → "Excluir ação" (vizinho de "Excluir todas as ações a partir daqui", que apaga o resto
   do fluxo); gatilho pela lixeira do cartão → "Apagar".
8. **Reteste sem contato novo:** `DELETE /contacts/{id}/workflow/{wf}` e depois `POST` no mesmo endereço põem o contato de
   novo no começo do fluxo. Sem o DELETE, o fluxo ignora quem ainda está nele.
9. **A busca por tag da API leva uns 20 s pra refletir uma remoção.**
10. **Teste completo de fluxo com passo de WhatsApp manda mensagem pro telefone do contato de teste.** Conferir de quem é
    o número antes. Combine uma vez com quem decide quais contatos da equipe recebem o teste (e-mail e WhatsApp) e use
    sempre esses.
11. **O modelo ligado pelo ✓ vira uma cópia dentro da ação.** O e-mail que o fluxo manda sai com outro `template_id` (está
    no link de descadastro), diferente do id do modelo. Com "Sincronizar edições ao modelo" desligado, atualizar o modelo
    não muda o que o fluxo envia, e comparar o modelo com o documento não prova o que sai. Se o texto mudar: atualizar o
    modelo, religar o ✓ na ação (ou ligar a sincronização) e testar num contato da equipe.
12. **"Remover" o corpo da ação de e-mail limpa também o assunto.** Pra trocar o modelo numa cópia de fluxo: ⋯ do corpo →
    Remover → "Selecionar modelo existente" → buscar pelo nome → ✓ (passar o mouse mostra o nome inteiro). Depois
    redigitar o assunto (com `{{contact.first_name}}`, se levar o nome) antes de salvar. O pré-cabeçalho continua vazio.
13. **Repetir um ramo inteiro em outro ramo:** ⋯ da primeira ação → "Copie todas as ações a partir daqui" → ícone de
    colar ao lado do "+" do ramo novo ("Ações coladas com sucesso"). As cópias são independentes: trocar o link na cópia
    não mexe no original. No mesmo menu ficam "Mover todas as ações a partir daqui" e "Excluir ação".
14. **Construtor pelo navegador:**
    - Clique em opção de lista (operador, tag) às vezes não pega. Digitar na busca da lista e apertar Enter pega.
    - A tela só se redesenha depois da ação seguinte: confira depois de passar o mouse.
    - O endereço direto de um fluxo (`/automation/workflow/<id>`) às vezes abre em branco. Pela lista abre.
    - O login pode cair depois de uma noite parado, e o "Sign in with Google" pode travar numa página em branco: aí
      quem tem a conta entra com e-mail e senha.

### Disparo de WhatsApp pela API oficial: custo, recarga e falha (11/2026) — *VARIAÇÃO ISOLADA*

- **Custo:** só na tela, em Configurações → Faturamento → Carteira e vendas → Por atividade, por mês e em dólar. Por
  mensagem, na medição: marketing US$ 0,075, utilidade US$ 0,008, serviço quase zero. Falha não cobra.
- **Recarga:** com recarga automática pequena ("US$ 10 quando chega a US$ 0"), um envio de 2 mil mensagens de uma vez
  falha por "insufficient funds". Carregar antes do envio grande.
- **O export** (`GET /conversations/messages/export`) traz o número de destino em `to` e o `contactId`. Com `startDate` a
  mais de uns 10 dias de hoje voltou `total: 0`: guarde o histórico enquanto dá. `limit` mínimo é 10.
- **"Message Undeliverable" quase sempre é número sem WhatsApp, não número mal digitado:** 86% dos que falharam estavam
  no formato certo, e números sem o 9 receberam normalmente, então pôr o 9 em massa não resolve. Lista antiga importada
  é onde a falha se concentra.
### Teste de fluxo só roda publicado

O "Executar teste" **não inscreve contato enquanto o fluxo está em rascunho**: a aba
*Histórico de inscrições* fica em "Nenhuma inscrição encontrada". Para testar é preciso
publicar antes — o que torna o teste uma ação com efeito externo, não um ensaio.

## Venda da Hotmart chega por webhook, não pelo ListBoss

Medido na conta do caso-base (detalhe em `sirius-scale/frameworks/hotmart/hotmart-configuracao-produto.md` §3):

- O ListBoss da Hotmart não tem o HighLevel entre os provedores. O que alimenta o Full Funnels é uma
  configuração de webhook da Hotmart: todos os produtos, 5 eventos (abandono de carrinho, aguardando
  pagamento, cancelada, aprovada, expirada), apontando pro gatilho de webhook de um fluxo publicado.
  Entregas com HTTP 200 no histórico.
- Produto novo já cai nesse gatilho sem mexer na Hotmart. Pra ele virar tag e fluxo, o fluxo precisa
  reconhecer o produto ou a oferta. As tags do lançamento seguem o padrão
  `<funil>-<mês/aa>-<modelo>-<produto>-<evento>`, em minúsculas (ex.: `…-compra-aprovada`; lista lida
  pela API).
- Reembolso não está entre os eventos. Fluxo de pós-compra que precisa tirar quem devolveu depende de incluir
  `PURCHASE_REFUNDED` no webhook (mexe numa integração que serve todos os produtos: decisão do dono).
- Ler o fluxo por dentro pede o login no `go.fullfunnel.app` (um estado de sessão salvo dias antes abriu na
  tela de login).
