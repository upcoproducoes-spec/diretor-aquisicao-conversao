# Hotmart — configuração de produto na tela (checkout, bump, pixel, integrações)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma.
> **Alcance:** §1 a §4 são mecânica da Hotmart (UNIVERSAL, sem eixo de força). A tabela da §5 é o
> padrão da casa tirado de **um** produto (um desafio pago do caso-base, o "produto de referência"): VARIAÇÃO ISOLADA.
> **Origem:** medido configurando os 4 e-books do low ticket do caso-base (um expert de educação) pela Central de
> colaboradores, com navegador automatizado. As seções 6 a 13 vieram nas duas semanas seguintes (proteção do PDF,
> virada dos e-books pra curso, vitrine, checkout dos cursos), e as seções 14 a 17 na semana seguinte (módulo de
> bônus, combo, Recomenda e a data da compra de quem já era aluno).
> **Fato de plataforma:** tela, campo, endereço e limite são os da época da medição. A Hotmart muda sem avisar:
> conferir antes de confiar.
> A API de vendas está em `sirius-scale/frameworks/hotmart/hotmart-api-tecnica.md`; este arquivo é o que só se faz na tela.

## 1. Order bump mora no Checkout Builder, e só aceita produto aprovado

- **A ferramenta "Order Bump"** (Ferramentas → Order Bump, `app.hotmart.com/cross-sell/order-bump`) só mostra a
  sugestão automática "Deu match!" com o botão **"Ativar combinação com 1 clique!"**. Não clicar: liga um bump que a
  Hotmart escolheu (na medição, era o desafio pago + a gravação dele dentro do checkout do programa principal, produto ativo).
- **Onde o bump se configura:** Aparência da página de pagamento (`custom-checkout.hotmart.com/<id>`) → Criar nova
  página → modelo (o produto de referência usa "Em Branco") → Ferramentas de venda → Order Bump → Escolher produto (até 9).
- **Produto em rascunho não aparece no seletor.** Buscando pelo nome de cada e-book (ainda em rascunho): nada. Só os 3
  produtos aprovados da conta apareceram. Então o bump só entra **depois do "Finalizar cadastro" e da aprovação da
  Hotmart**, do produto principal e de cada produto que vai como bump.
- A oferta do bump (preço próprio, bem abaixo do produto principal no low ticket) se cria antes, em Precificação e
  ofertas → Novo preço, e fica pronta esperando.
- **Montando (depois da aprovação, os 4 e-books):** o seletor deixa marcar **uma oferta por vez** (os
  rádios de todos os produtos são um grupo só: marcar o segundo desmarca o primeiro). É um "Escolher produto" →
  Selecionar → descrição → Inserir por bump, na ordem em que devem aparecer. O cartão do bump não tem campo de
  título: o título é o **nome do produto**; há "De" (opcional, preço riscado) e "Descrição" (até 500 caracteres).
  Depois: Salvar nova Página → Publicar página → **Definir como padrão** → Atualizar publicação.
- **O bump só aparece no link com `checkoutMode=10`.** É assim que a Hotmart serve a página personalizada; o link
  puro (`pay.hotmart.com/<código>?off=<oferta>`) abre o checkout padrão, sem bump. Todos os links que funcionam na
  casa já levam o parâmetro, e a montagem de link de checkout da casa recusa link sem ele. Do lado de vocês: conferir
  o `checkoutMode=10` em todo link de checkout antes de pôr em página, e-mail ou anúncio.
- Na leitura de volta, o bump aparece **desmarcado** ("Adicionar produto"), com as parcelas da própria oferta.
- **Propagação:** a tela diz "até 5 minutos". Num dos e-books, o link da oferta base levou **~12 minutos** pra mostrar os
  bumps (aberto logo depois de publicar), enquanto o mesmo checkout sem `off=` já mostrava. Conferir de novo antes
  de concluir que deu errado; não republicar no impulso.

### 1.1 Celular e computador são duas páginas (medido nos 4 e-books)

- A página personalizada tem **dois layouts**, um por aparelho (`checkoutMode` 1 e 0 dentro do `payloadList` do
  layout). Bump, contador, vantagens e cor de fundo montados na tela do celular **não aparecem no computador**: nos 4
  e-books o computador abriu sem bump nenhum depois de tudo publicado no celular. Conferir sempre nas duas larguras
  (390 e 1440 px, emulando a largura no navegador), lendo o texto da página, não o construtor.
- **O que resolveu foi a API do construtor, de dentro da página:** `GET` e `PUT`
  `api-checkout-builder.hotmart.com/hot-component-layout-web/api/v2/component/checkoutLayout/<id>`, com o token que
  a própria página guarda (chave do `localStorage` que começa com `oidc.user:`), corpo
  `{idProduct, idOffer: 1, name, id, payloadList: [{id, locale, isPublished: true, payloadFileList, checkoutMode,
  payload (texto JSON), editMode: true}]}`. Copiar os componentes do layout do celular pro do computador, com ids
  novos, e publicar. Leitura de volta pelo checkout no ar, nas duas larguras.
- **Cor de fundo pela tela não grava** (o campo aceita e volta ao padrão no salvar). Pela API, grava.
- **Envio de imagem no construtor travou** em "Aguarde, processando imagem..." (banner de topo, JPEG de 80 KB,
  1920 × 640) nas primeiras tentativas. O banner do produto de referência é 1024 × 410. Duas semanas depois o envio
  passou, pelo componente Topo e com a caixa de soltar da §11 (PNG de 1,3 MB, 1920 × 640): ver §12.
- O contador do produto de referência diz "Preencha seus dados antes que o tempo acabe" e não promete preço nenhum.
  Mesmo assim, ⚠️ **cronômetro está na tabela de "onde a casa vence" do
  `sirius-scale/frameworks/lancamentos/low-ticket.md` §9** (urgência sem fato). Os 4 e-books ganharam o contador a
  pedido do Rodrigo ("configurar ali um contador de 10 ou 15 minutos"), igual ao do produto de referência. A
  contradição com o framework está aberta pra ele decidir; não virou regra.

## 2. Pixel da Meta: separar pagamento imediato exige a API de Conversões

- Caminho: Ferramentas → Pixel de rastreamento (`app.hotmart.com/tools/pixel/checkout/<id>`) → facebook + Instagram
  → ID do pixel → eventos → formas de envio (web e/ou API de Conversões, "configuração via token").
- Com **"Quer diferenciar eventos de pagamento imediato e não imediato?" = Sim**, o Salvar recusa sem a API de
  Conversões. Mensagem da tela: "Para a opção 'Quer diferenciar eventos de pagamento imediato e não imediato?', a
  configuração de envio via API de conversão é obrigatória".
- Sem diferenciar e com "Todos os métodos de pagamento", o evento "Vendas realizadas" sai quando a pessoa chega na
  página de obrigado, o que inclui Pix e boleto só gerados. A campanha passaria a otimizar em compra não paga. Por
  isso **não salvar "só web" nesse modo**: ou API + diferenciar (como o produto de referência), ou esperar o token.
- **O token é credencial.** Quem cola é o dono da conta (na casa, o Rodrigo), nunca o agente.
- **Configurado nos 4 e-books na mesma noite em que o tráfego ligou:** o pixel das campanhas, "Vendas realizadas" +
  "Visitas na Página de pagamento", todos os métodos, diferenciar = Sim, valor da transação, envio WEB + API. O agente
  preenche tudo até o campo do token e para; o dono gera o token no Gerenciador de Eventos (pixel → Configurações →
  API de Conversões → "Gerar token de acesso"), cola, clica em "Verificar token" e salva. O mesmo token serve pros 4,
  e gerar outro não derruba o anterior. Leitura de volta: Pixels configurados → "Configurado" (web) + "Token
  configurado" (API) + Detalhes da configuração.
- **O que o pixel manda de fato (medido em 7 compras reais dos 4 e-books, nos primeiros dias de venda):** um Purchase
  **por item** (front + cada bump), não por compra. O gerenciador contou 17 compras pra 7 compradores (7 fronts + 10
  bumps). E o valor somado ficou bem abaixo do que os compradores pagaram: bateu quase no centavo com a comissão de um
  dos coprodutores (a fatia do coprodutor sobre o líquido), não com o preço, mesmo com "valor da transação" na
  configuração. Então o CPA e o ROAS do gerenciador não decidem nada num checkout com bump: decide a venda real da
  Hotmart, casada pela UTM. VARIAÇÃO ISOLADA (1 conta, 4 produtos em coprodução).
  *(11/2026, VARIAÇÃO ISOLADA: o pixel é o mesmo pra todos os produtos da conta, e compra de outro produto entra na
  conta do anúncio pela janela de atribuição (7 dias de clique e 1 de visualização). No caso medido, o gerenciador do
  produto de entrada contou um pedido de valor que não cabia no checkout dele: era venda de outra oferta da conta, no ar
  na mesma semana. Com duas ofertas no ar no mesmo pixel, o custo por compra do gerenciador mistura as duas.)*
- ⚠️ **Até essa noite nenhum dos 4 tinha pixel**, com tudo o mais pronto (checkout, bumps, webhook, páginas). Quem
  pegou foi uma trava do registro de campanhas da casa, conferida antes de ativar. Pixel por produto é configuração
  à parte: produto novo nasce sem, e não aparece em lugar nenhum além desta tela. **Antes de ativar campanha pra um
  produto, conferir nesta tela que ele tem pixel configurado.**
- Na tela, clicar no cartão "facebook + Instagram" abre direto o formulário de pixel novo quando o produto não tem
  nenhum; Cancelar mostra a lista "Pixels configurados" (vazia ou não). O seletor de produto do topo nem sempre
  aparece: quem manda é o id na URL.

## 3. ListBoss não fala com o Full Funnels; o caminho é o Webhook

- **ListBoss** (Ferramentas → Gestão automática de contatos) é configurado **por produto**. Provedores ligados na
  conta do caso-base: Mailchimp e Hotmart Send. **HighLevel/Full Funnels não está entre os 20 provedores** da
  ferramenta.
- **Hotmart → Full Funnels é o Webhook** (Ferramentas → Webhook (API e notificações)): uma configuração com **todos
  os produtos**, versão 2.0.0, 5 eventos (`PURCHASE_OUT_OF_SHOPPING_CART`, `PURCHASE_BILLET_PRINTED`,
  `PURCHASE_CANCELED`, `PURCHASE_APPROVED`, `PURCHASE_EXPIRED`), apontando pro gatilho de webhook de um fluxo do Full
  Funnels. Entregas com HTTP 200 no Histórico.
- Produto novo entra sozinho no webhook ("todos os produtos"). O que precisa mudar é o fluxo do Full Funnels
  reconhecer o produto ou a oferta e pôr a tag certa.
- **Fora do webhook, na configuração do caso-base:** reembolso (`PURCHASE_REFUNDED`), pedido de reembolso
  (`PURCHASE_PROTEST`), chargeback e compra completa (garantia vencida). Sem reembolso, quem devolve continua na régua
  de pós-compra.
- "Aguardando pagamento" na tela = `PURCHASE_BILLET_PRINTED` na API (Pix e boleto gerados).
- Padrão de tag do Mailchimp via ListBoss (o que já existia antes do Full Funnels):
  `<FUNIL>-<PRODUTO>-<MÊS/AA>-<EVENTO>`, ex. `<FUNIL>-<MODELO>-<PRODUTO>-<MÊS/AA>-COMPRA-APROVADA`, com os eventos
  COMPRA-APROVADA, AGUARDANDO-PAGAMENTO, BOLETO-EMITIDO, COMPRA-CANCELADA e ABANDONO-DE-CARRINHO, filtrados pela oferta
  do lançamento. No Full Funnels a mesma ideia em minúsculas (`<funil>-<mês/aa>-<modelo>-<produto>-compra-aprovada`).

⚠️ **Mailchimp saindo (decisão do Rodrigo: "estamos parando de usar").** Integração nova vai pro Full Funnels, e o
ListBoss não tem esse provedor: o caminho é o webhook. As 20 integrações Mailchimp que os 4 e-books ganharam na
madrugada da configuração foram desligadas no mesmo dia; a receita da API abaixo continua valendo pra ler e desligar.

### 3.1 Produto novo nasce com 13 automações do Hotmart Send LIGADAS (medido nos 4 e-books)

- Na aprovação, a Hotmart cria sozinha 13 segmentações `automation-<evento>-product-<id>` no provedor
  **Hotmart Send** (conta "Hotmart Extensões"), todas **ativas**: aprovada, aguardando, abandono, boleto, atrasada,
  completa, download, pedido de reembolso, cancelada, reembolsada, expirada, chargeback e avaliação. Ação
  `klicksend_subscriber_and_add_tag`; `editable: false`, `removable: false` (não se apagam, só se desligam).
- **Padrão da casa: desligadas.** Nos dois cursos que já vendiam no caso-base: 0 de 10 ativas num, 0 de 15 no outro.
  A casa manda e-mail pelo Full Funnels e pelo Mailchimp; deixar ligadas abre um terceiro remetente pro mesmo
  comprador. Nos 4 e-books, desligadas na configuração (52) e lidas de volta: 0 ativas.
- **Pela API do ListBoss, de dentro da página `app-listboss.hotmart.com`** (token na chave `token` do
  `localStorage`): `GET /segmentations?productId=<id>` lê; `POST /segmentations` cria (o mesmo corpo que a tela
  manda; Mailchimp com `add_tag_contact`, a lista da conta, a tag por id e `PHONE:${user.phone}` no merge);
  `PUT /segmentations/<id>?activate=false` desliga (é o que o botão da tela chama). Ler de volta sempre:
  nos 4 e-books, 20 segmentações criadas, as 20 conferidas por evento e por id de tag.

### 3.2 Tudo o que o ListBoss e o webhook oferecem (medido na conta do caso-base)

Pedido do Rodrigo: "investigar todas as opções do ListBoss pra gente configurar e receber o máximo de eventos possíveis
no nosso CRM". Lido pela API do ListBoss (`GET /providers`, `/events?productId=`, `/events/filters?productId=`, só
leitura, credencial das contas omitida) e pelo formulário "Cadastrar Webhook", aberto e fechado sem salvar.

- **Os 20 provedores do ListBoss:** LeadLovers, MailChimp, AWeber, GetResponse, E-Goi, ActiveCampaign, Infusionsoft,
  RDStation, RDStationV2, Hubspot, ConvertKit, Mautic, Ontraport, SendinBlue, Drip, MailingBoss, HotmartSend,
  SgAutorepondeur, Zoho e ConstantContact. Conta ligada só no MailChimp e no HotmartSend. **Nenhum é HighLevel/Full
  Funnels, e nenhum é webhook genérico** (nem Zapier, Make ou n8n). Os comandos são de lista e tag: adicionar, remover,
  pôr tag, mover de grupo; o RDStationV2 tem também oportunidade, conversão e carrinho abandonado.
- **Eventos do ListBoss por produto:** o curso tem 23 e o e-book tinha 13.
  - De compra (11): aprovada, completa, cancelada, aguardando pagamento, boleto impresso, pedido de reembolso
    (`protested`), reembolsada, chargeback, atrasada (`overdue`), expirada e abandono de carrinho.
  - Nos dois: download (`access.download`) e avaliação do produto (`review`).
  - Só do curso, da área de membros (10): cadastro no Club (`club.membership`), primeiro acesso, aula concluída, módulo
    concluído, progresso (%), avaliação de aula, nota de quiz e sem login há 7, 15 e 30 dias.
  - Os eventos de compra aceitam filtro por oferta (`OFFER`; no abandono, `OFFER_KEY`), forma de pagamento, parcela,
    país e moeda. Os do Club filtram por aula, módulo, quiz ou faixa de progresso.
- **Os eventos do webhook (versão 2.0.0), 16 em 5 grupos:**
  - Compras (9): compra cancelada, completa, aguardando pagamento, aprovada, reembolsada, chargeback, expirada, pedido de
    reembolso e compra atrasada.
  - Assinaturas (3): cancelamento, troca de plano e atualização da data de cobrança.
  - Club (2): primeiro acesso e módulo completo.
  - Gestão logística (1): dados logísticos.
  - Outros (1): abandono de carrinho.
  A configuração que alimenta o Full Funnels usa 5 desses 16 (§3).
- **Consequência:** o caminho até o Full Funnels é o webhook, e ele carrega 16 eventos, não 23. Os sinais de engajamento
  que só o ListBoss tem (sem login há 7, 15 e 30 dias, progresso, aula concluída, quiz, avaliação) só saem pelos
  provedores da lista. O Full Funnels consegue reconstruir parte: "sem login" sai do primeiro acesso mais uma espera.
- **A conta do caso-base tinha 9 configurações de webhook**, com os nomes cortados na lista (só o começo aparece): a do
  CRM, a do Dash Fácil, ManyChat, Spedy, uma de depoimentos e quatro com nome de produto (uma delas do Panda).

## 4. Como ler sem clicar em nada

- **ListBoss:** a tela chama `api-listboss.hotmart.com` (`/providers`, `/events?productId=`,
  `/segmentations?productId=`). Ler pelo log de rede do navegador (aba Rede do DevTools, ou o log de rede do navegador
  automatizado). ⚠️ `/providers` devolve a chave de API do Mailchimp e o token do Hotmart Send em texto:
  nunca salvar a resposta sem apagar o `schema` das contas.
- **Webhook:** `api-webhook.hotmart.com/api-postback/v1/configuration-groups` traz a URL inteira e os eventos;
  `/V2/history` traz as entregas, com e-mail do comprador (dado pessoal: ler, não salvar). O histórico é **POST**
  (corpo `{"page": 0, "rows": 50}`; GET dá 405) e cada item traz tipo do evento, produto, transação e status HTTP,
  **sem o conteúdo enviado** (na medição, nenhuma rota de detalhe respondeu). Pra saber o nome exato de um campo do
  evento (link do boleto, indicador de bump), o lugar é o gatilho de webhook do Full Funnels, que mostra o último
  evento recebido.
- **Abas do produto em iframe:** Página do produto, Ferramentas e Afiliados rodam dentro de `app-vlc.hotmart.com`.
  O `innerText` da página não enxerga; o snapshot de acessibilidade do navegador automatizado enxerga, e rolar é
  trazendo o elemento à vista pela referência dele (a roda do mouse não rola o iframe). No navegador embutido do
  Claude, abrir o endereço do iframe direto volta pro `app.hotmart.com`; o que lê é a captura de tela, que funciona
  mesmo com o painel escondido (medido na tela do pixel).
- **Ligar e desligar opção do checkout** (telefone, cupom, suporte por WhatsApp) foi barrado pelo classificador de
  segurança do modo automático do Claude Code, mesmo com o pedido de revisão. Precisa de ok explícito do dono no chat
  pra cada mudança de checkout. Com o ok do Rodrigo no chat ("pode modelar o checkout do desafio... todas as
  configurações iguais"), passou, e o padrão do produto de referência foi aplicado nos 4 e-books.

## 5. O que produto novo não herda do padrão da casa

Produto criado do zero vem com os padrões da Hotmart, não com os do produto de referência. Medido nos 4 e-books contra
o produto de referência (VARIAÇÃO ISOLADA: 1 produto de referência):

| Campo (Configurações da página de pagamento, salvo onde diz) | Produto novo | Produto de referência |
|---|---|---|
| E-mail de suporte ao cliente | vazio | o e-mail comercial do expert |
| Nome na fatura (até 16 letras depois do `HTM*HT`) | vazio | o nome do produto, abreviado |
| Pede telefone no checkout | não | sim |
| Pede CPF e endereço | não | sim |
| Mostra campo de cupom | sim | não |
| Pagamento híbrido (Pix + cartão) e oferta dele na recusa por saldo | desligados | ligados |
| Google Pay | desligado | ligado |
| Suporte por WhatsApp quando o pagamento recusa | desligado | ligado, com número e mensagem |
| Pixel da Meta (Ferramentas) | nenhum | o pixel das campanhas, web + API, 3 eventos, diferencia imediato |
| Parcelamento da oferta | até 12x, juros do comprador | — |
| Coleta de impostos | ESS, sem conteúdo educacional | igual (os dois cursos também) |
| Automações do Hotmart Send (ListBoss, §3.1) | 13 ligadas | desligadas (nos dois cursos também) |
| Página personalizada no computador (§1.1) | só o padrão, sem bump | — conferir nos dois aparelhos |

Boleto é decisão por produto (o produto de referência está sem; os e-books com, vencendo em 1 dia útil, decisão do
Rodrigo).

**Não vira checagem automática:** a API pública da Hotmart não expõe a configuração do checkout, então isso é
conferência na tela, ao criar cada produto, com esta tabela na mão. Frágil, e dito aqui de propósito: o que não vira
checagem automática depende de alguém lembrar.

## 6. Banner da área de membros é outro lugar

A área de membros é um Hotmart Club identificado por um slug (`<área>`); a gestão do e-book abre em
`app.hotmart.com/membership/<área>/products/edit/<id>/ebook/management`. O endereço que o comprador abre tem formato
provável `https://hotmart.com/pt-br/club/<área>/products/<id>` (respondeu 200 sem login; o subdomínio
`<área>.club.hotmart.com` deu 404). Confirmar o link real e o download do PDF na compra de teste antes de pôr em e-mail.

A imagem do produto (800 × 800, Informações básicas) não é o banner da área de acesso. O banner (1920 × 640) fica
no Hotmart Club: Acessar a gestão do eBook → Personalização → Banner, e só aparece depois de **Publicar** a
personalização da área de membros (a do caso-base tinha aluno). Nos 4 e-books ele ficou vazio na configuração inicial.

## 7. Produto "eBooks, Documentos" só entrega arquivo (medido nos 4 e-books do caso-base)

Na área de membros, a gestão do e-book é uma lista de arquivos e mais nada:

- O "Enviar arquivo" aceita `.pdf, .epub, .rar, .zip, .xls, .xlsx, .ods, .csv` (atributo `accept` do campo), **um
  por vez**, até **20 arquivos e 250 MB** no total. Não aceita vídeo.
- Cada arquivo tem só "Baixar" e "Excluir". **Não existe módulo, aula, player nem liberação programada** ("liberar X
  dias depois da compra" é coisa de curso). As configurações do e-book têm só Vitrine (desligada nos 4) e Segurança.
- Arquivo novo aparece pra todos os compradores, antigos e novos, na hora em que sobe.
- **Trocar o arquivo por uma versão corrigida (num dos e-books):** a lista mostra só nome e tamanho. Versão nova com o
  mesmo nome e quase o mesmo tamanho (1,41 MB nas duas) fica indistinguível da antiga na tela. Excluir a antiga e subir a
  nova, nessa ordem, quem fazia era uma pessoa (arquivo do computador não entrava pelo navegador embutido do Claude,
  §8), e quem conferir depois precisa de outro sinal que não a lista: perguntar a quem trocou ou baixar o arquivo.
  - Atualizado na mesma noite, com dois e-books novos (3,46 e 3,03 MB): o PDF sobe pela caixa de soltar do §11, e a
    ordem inverte. **Primeiro sobe o novo, depois sai o antigo**, porque com tamanhos diferentes a lista mostra qual é
    qual e o comprador nunca fica sem arquivo. Excluir continua sendo clique de uma pessoa, não do agente.
- **Endereço da gestão:** `app.hotmart.com/membership/<área>/products/edit/<id>/ebook/management`. Em
  "Conteúdo do Produto" (`/products/manage/<id>/product-content`) o e-book só diz que não usa área de membros.
- "Combos", no menu da área de membros, é pacote **à venda** dentro da área (no caso-base, o desafio pago junto com a
  gravação dele). Não serve pra dar acesso grátis a outro produto.

Consequência: bônus em vídeo, ou bônus que libera depois, pede produto do formato **curso online**. Trocar o formato
de um produto que já vende não apareceu como opção; a ajuda da Hotmart não fala disso (sem confirmar com o suporte).
Recriar como curso refaz checkout, ofertas, bumps, pixel, coprodução, roteador do Full Funnels e Dash.
Sem recriar, o caminho é um PDF com o link da aula (vídeo não listado), subido quando o vídeo existir.

## 8. Criar curso online pelo assistente (medido criando os 4 guias do caso-base como curso)

Os 4 cursos saíram pelo navegador embutido do Claude, na Central de colaboradores (evidência no caso de origem).

- **Caminho:** `app.hotmart.com/products/add` → Curso Online → Informações (nome, descrição até 2.000, idioma, país,
  imagem JPG/PNG até 5 MB, "ideal 600x600", categoria) → Precificação (moeda, prazo de reembolso, forma de
  pagamento, valor) → "Criado com sucesso", em **rascunho**. O curso entra sozinho na área de membros que já existe
  (a do caso-base passou a ter 13 produtos), e rascunho **não aparece** em "Produtos à venda" da vitrine.
- **Copiar texto e imagem do e-book sem redigitar:** a descrição foi lida do campo do e-book e passada pelo
  `localStorage` (mesma origem `app.hotmart.com`), com igualdade conferida por código. A imagem é o PNG 800x800 do
  e-book no S3 (`hotmart.s3.amazonaws.com/product_pictures/...`), buscado com `fetch` e posto no campo de arquivo
  (`DataTransfer`). ⚠️ O primeiro `fetch` falhou por CORS porque a imagem já estava no cache sem cabeçalho CORS;
  com `?cb=<agora>` e `cache: 'no-store'` passou. 800x800 foi aceito.
- **Forma de pagamento não muda depois de criada.** "Parcelado com taxas para seu cliente" é a dos e-books; o valor
  interno do campo (`hot-select`) é `UNIQUE_PAYMENT`. A própria Hotmart limita as parcelas pelo valor da oferta: no
  caso-base, a oferta de entrada saía em até 12x e as dos bumps, de pouco mais de um terço desse preço, em até 5x ou 6x
  (limite da época; conferir na plataforma). Cada oferta nova leva uns 25 s ("Estamos criando sua oferta").
- **"Finalizar cadastro" aceita o Termo de Tratamento de Dados Pessoais da Hotmart:** é clique do dono da conta
  (aceitar termo é decisão de gente; na casa, o Rodrigo autorizou pros 4 cursos). O item "Conteúdo" do painel não tem
  a marca "Opcional". O "Configurar" dele (`/products/manage/<id>/product-content`) pergunta se o conteúdo já existe.
  O "Não, ainda não tenho" vem marcado e mostra um botão "Selecionar arquivo" e um campo de texto, "Não tem um arquivo?
  Descreva o seu curso e as datas planejadas de lançamento" (não confirmado se o comprador vê esse texto; foi escrito
  como se visse), além da declaração "Confirmo que sou o(a) autor(a) desse curso ou tenho a autorização do autor para
  publicação", que também é do dono.
  - Medido nos 4 cursos. Os passos foram: texto preenchido, declaração marcada e "Salvar". O painel
    passa a dizer "Você já pode finalizar o cadastro". O "Finalizar cadastro" manda `POST
    api-product.vulcano.hotmart.com/product/v1/product/<id>/approval` (200) e abre "Enviado para aprovação: estamos
    analisando seu produto, esse processo pode levar até 15 minutos".
  - Em menos de 10 minutos os 4 estavam aprovados, com status "Vendas ativas" e, na área de membros, "Oculto na
    vitrine": aprovar não mostra o curso pra aluno nenhum.
- **Curso em rascunho não tem área de membros pro colaborador** (medido de dia, logado com a conta da casa, que é
  colaboradora na central do expert, no navegador embutido e num navegador automatizado). A lista de módulos dá "Não
  foi possível carregar".
  - A chamada `GET api-club-class.cb.hotmart.com/v5/classes/` volta 403, e a de ofertas da turma
    (`api-club-sales-settings.cb.hotmart.com/v4/offers`) volta 500.
  - O módulo novo exige "Turmas", que não carregam, então "Criar módulo" não sai.
  - Num curso antigo, já publicado, a mesma conta lista os módulos e a turma volta 200: o bloqueio é o rascunho.
  - O passo "Conteúdo" do painel tem duas saídas. "Sim, já tenho" pede pelo menos 1 módulo não gratuito publicado, que o
    rascunho não deixa criar. "Não, ainda não tenho" pede descrição e datas planejadas (o comprador vê) e a declaração
    de autoria.
  - Na prática: finalizar o cadastro pelo "Não, ainda não tenho" e montar o conteúdo depois da aprovação.
  - ⚠️ **Corrigido na mesma noite: o bloqueio não é o rascunho.** Com os 4 cursos já aprovados, as mesmas
    chamadas continuam em 403, e agora também `api-club-content.cb.hotmart.com/v4/modules` ("Não foi possível
    carregar").
  - ⚠️ **Corrigido de novo no dia seguinte, medido pelo navegador embutido: também não é a coprodução nem o papel da
    conta colaboradora.** Com a coprodução dos 4 cursos "Ativado", o conteúdo continuou fechado.
    - O corpo do 403 diz a causa: `{"errorCode":"0017","errorDetail":"UserAreaResolver: user_area is required"}`.
    - O Club identifica cada curso pelo **subdomínio dele**, mandado no cabeçalho `Club` (o de um curso antigo era o
      nome do curso encurtado mais um sufixo aleatório). Com esse cabeçalho `userarea/code` volta 200; sem ele, 403. O
      app dos cursos novos só manda `x-product-id`, porque não acha subdomínio, e o servidor não resolve a área.
    - `GET api-club-user.cb.hotmart.com/v4/users/resources` (mesmo logada como colaboradora, a Hotmart responde como a
      conta do expert) lista **só 2 áreas**: as dos dois cursos antigos. Os 4 cursos novos, o desafio pago e um terceiro
      produto não têm área, e por isso nenhum abre. A lista de produtos do Club só mostra "Visualizar | Editar" nos que
      têm área.
    - A "membership" do curso existe (`GET api-club-hot-club-api.cb.hotmart.com/rest/v3/membership` com
      `x-product-id` devolve um id), e `Club: <área>` dá 404 "Subdomain ... does not exist": o slug da URL é o
      guarda-chuva, não um subdomínio de Club.
    - Um usuário da equipe aparece como "Administrador" na lista de usuários de um curso antigo; a conta colaboradora
      da casa não aparece, e mesmo assim abre ali. Ou seja, o papel de usuário não é o que decide.
    - "Acessar a gestão do curso" e "⋮ → Conteúdo" do cartão da área de membros abrem **aba nova**, que o navegador
      embutido do Claude bloqueia quando o clique é do agente. Só clique de gente abre. Hipótese a testar: o
      primeiro acesso pelo botão oficial cria a área. Teste de sucesso: `users/resources` passar a listar o produto.
    - ⚠️ **Testado dois dias depois, e caiu pra colaboradora.** O botão monta o endereço com o slug que vem de
      `GET api-content-platform-space-gateway.cp.hotmart.com/rest/public/v1/memberships/products/<id>` (pros 4 cursos,
      o slug da área de membros) e abre `app.hotmart.com/membership/<slug>/products/edit/<id>`. Abrir esse endereço
      com `navigate`, na mesma aba, faz o mesmo que o clique, sem precisar da aba nova. A tela de gestão do curso
      abriu, mas o conteúdo seguiu em 403 (`user_area is required`), a configuração deu "Erro inesperado"
      (`api-club-sales-settings` 500) e `users/resources` continuou com as mesmas 2 áreas. Próximo teste: a conta do
      próprio expert (dono), ou o suporte da Hotmart.
    - **Criar turma também não passa pela colaboradora (na mesma madrugada).** A aba Turmas abre e mostra "Criar turma"
      (a lista vazia é a falha, não falta de turma). O formulário abre, a lista de ofertas falha (500) e a chave "Turma
      Padrão" pede confirmação ("Ela contém todas as ofertas que não estão em outra turma"). O `POST
      api-club-class.cb.hotmart.com/v4/classes/` com `{"name","defaultClass":true,"offers":[]}` volta 403 `user_area
      is required`. A pista do porquê: `GET api-club-hot-club-api.cb.hotmart.com/rest/v3/userarea/code`, a chamada que
      resolve a área do curso, responde **"Forbidden access"** pra conta colaboradora. Quem pode resolver é login do
      próprio dono da conta (o expert) ou o suporte.
    - ✅ **Logado como o dono da conta, abre (na tarde seguinte).** Com o login do próprio expert (quem entrou foi o
      Rodrigo, pelo navegador embutido), `membership/<área>/products/edit/<id>/admin/beta/modules` lista o conteúdo e a
      aba Turmas mostra "Turma A · Turma Padrão", criada no mesmo dia do curso. Ou seja, a turma existe desde a
      criação, e o 403 era só da colaboradora. O único conteúdo é o "Cronograma do curso", **publicado**, que a Hotmart
      gerou do texto do "Não, ainda não tenho o conteúdo" (§8, passo Conteúdo): sai do ar quando o módulo de verdade
      subir. Não deu pra testar se a conta colaboradora passou a abrir depois desse primeiro acesso do dono, porque a
      sessão era a dele.
    - **A aula por dentro** ("+" do módulo → Aula; os outros tipos são Quiz, Anúncio e Live): Mídias (vídeo ou áudio
      pelo Hotmart Player, até 20 GB), Texto, Material extra (até 10 arquivos de 100 MB: pdf, zip, rar, epub, doc,
      docx, xls, ppt, imagem, mp3; "Selecionar do Club" ou "Enviar arquivo"), Liberação e expiração, Tags e Miniatura.
      Botões "Criar conteúdo" e "Publicar". Não tem proteção por arquivo ali: a do PDF é a DRM Social do produto (§10).
    - ⚠️ **As rotas `/membership/...` só valem de dentro da central do expert** (ícone de pessoas no topo → "Centrais
      que participo" → o nome do expert). Fora dela, `/membership/<área>/...` cai em "não encontrado", e
      `/membership/list` mostra as áreas da própria conta logada, não as do expert. Conferir em qual central está antes
      de mexer em qualquer área.
  - Importar aluno vive em `app.hotmart.com/membership/<área>/members/add/<produto>` (individual, em lote por CSV,
    histórico e "Atribuir acesso"). A tela de usuários do curso novo abre e lista 0 usuários.
- **Permissão de colaborador no Player** (central do expert): a conta colaboradora da casa tinha só 2 de 6, "Editar
  Informações de Mídias e Pastas" e "Visualizar Mídias e Pastas". Faltavam "Subir (Upload) Mídias", "Apagar", "Baixa" e
  "Compartilhar". Sem o upload, vídeo de aula não sobe pela conta colaboradora. Quem libera é o dono da conta
  (Collaborators-center → permissões). O resto que a migração usa estava liberado: Club 9 de 9, Produtos 3 de 3, Pixel,
  Webhook, ListBoss, Aparência e Configurações da página de pagamento.
  - **Onde se libera (logado como o dono):** Central de colaboradores → Perfis → "Có-produtor" (o perfil da conta
    colaboradora, `collaborators-center/edit-profile?profileId=<id>`) → ⋮ → Editar → Player → "Subir (Upload) Mídias"
    → Salvar alteração. "Detalhes" mostra as permissões sem editar. **Marcar permissão é clique do dono:** a trava do
    modo automático barrou o agente ("Permission Grant"), e nada foi salvo.
- **Arquivo do computador não entra pelo navegador embutido do Claude.** Medido: `fetch` de `https://app.hotmart.com`
  pra um servidor local em `localhost` não sai (o servidor não recebeu nada: bloqueio de rede local do navegador);
  colar imagem com cmd+v pela ferramenta não dispara o evento de colar. Pra PDF e vídeo, o caminho era um navegador
  automatizado com comando de upload, com alguém logado na hora (o login da Hotmart não ficava salvo nele), ou a pessoa
  arrasta o arquivo.
  - ✅ **Resolvido pela caixa de soltar (§11).** A pessoa arrasta tudo de uma vez numa caixa que o agente põe na
    página, os arquivos ficam no IndexedDB, e o agente põe cada um no campo certo. Valeu pra PDF, capa e banner.
- **De onde o vídeo de aula entra** (ajuda da Hotmart, *Como fazer upload de vídeos no Hotmart Player?*; mecânica da
  plataforma). São três caminhos:
  - **upload do computador ou do celular**, até 20 GB por vídeo, pela Biblioteca de Vídeos (`play.hotmart.com`) ou na
    própria aula (aba *Adicionar do dispositivo*);
  - **importação do Vimeo ou do Panda Video** pra Biblioteca, com um token gerado lá, e vêm junto as pastas, os nomes e
    as legendas. Importar do YouTube e do Google Drive aparecia na ajuda como ainda em desenvolvimento;
  - **incorporação de vídeo do YouTube ou do Vimeo** por link ou código, sem subir arquivo: o vídeo continua hospedado lá.
  - **Na casa:** o master mora no Drive, e do Drive não se importa. Ele desce pro computador e sobe de lá, por quem tem
    "Subir (Upload) Mídias" no Player (acima). No caso-base ficou decidido subir as aulas dos guias direto no player da
    Hotmart, sem passar pela Panda, porque a Panda cobra a banda de uso dos alunos e a marca com nome e CPF. A decisão
    da Panda é do caso.

## 9. Checkout Builder dos cursos: o que a tela e a API mostram (medido no navegador embutido)

- **Endereços.** Construtor: `custom-checkout.hotmart.com/<id do produto>`. Configurações da página de pagamento
  (e-mail de suporte, nome na fatura, dados pedidos, formas de pagamento, vendas ativas):
  `app.hotmart.com/products/manage/<id>/tools/checkout/settings`, que roda em iframe, então só se lê por captura de
  tela. A engrenagem do construtor abre essa tela em aba nova, bloqueada pro agente.
- **Salvar uma página nova** abre "Deseja publicar a página?" com "Salvar rascunho" e "Publicar página". O rascunho
  nasce `INACTIVE`. A chamada é `POST api-checkout-builder.hotmart.com/hot-component-layout-web/api/v2/component/checkoutLayout`
  com `{idProduct, idOffer: 1, name, payloadList: [{locale: "PT_BR", isPublished: true, payloadFileList: [],
  checkoutMode: 1|0, payload: "<JSON em texto>"}]}`. Resposta: o layout com `id` e os ids dos dois payloads (celular e
  computador). Em branco, o layout nasce sem bump e com fundo `#fff`.
- **O layout do e-book é cópia fácil pro curso.** Os 4 e-books têm o mesmo desenho: contador de 15 min na primeira
  linha, checkout e vantagens na segunda, fundo escuro da marca, 3 componentes `hotpay-order-bump`. Nada do layout é
  específico do produto além de `data.product` de cada bump: `{category, categoryId, id, image, key (código da oferta),
  currencyCode, price, maxNumberOfInstallments, productName, paymentMode, beta}`. Pra produto curso, `category` é
  `category.online_services.name` e `categoryId` 8 (visto num bump de curso, a gravação do desafio); e-book é
  `category.ebooks.name` e 1. `GET .../component/product/<id>` devolve imagem, categoria e as ofertas (`key`, `price`,
  `maxInstallments`, `offerActivationCode`) de cada curso.
- Um layout em branco criado no teste ficou de rascunho num dos cursos.
- ⚠️ **O classificador do modo automático barrou a escrita por API com o token da página** ("Unrequested Commit in a
  Connected App"), depois de o agente ter lido tudo (leitura passou). A escrita pela tela, com clique, passou (criar
  rascunho). Pra copiar layout por API, o ok do dono no chat precisa dizer isso. Não precisou: a tela copia o layout de
  um produto pro outro em "Duplicar página" (§12).

## 10. Proteção do PDF (DRM Social): o carimbo é nome e e-mail, e a impressão nasce bloqueada (medido nos 8 produtos do low ticket)

Pedido do lado do expert, passado pelo Rodrigo: uma proteção do PDF da Hotmart que, pelo que se esperava, punha o CPF
da pessoa no PDF. Ligada nos 4 e-books e nos 4 cursos, logado como o dono da conta, pelo navegador embutido.

- **Onde:** Ferramentas → Ver todas → "Proteção para ebooks (DRM Social)" → escolher o produto → Continuar. O endereço
  fica `app.hotmart.com/products/manage/<id>/tools/drmsocial`, e dá pra ir direto por ele. É **por produto**. E-book e
  curso com o mesmo nome aparecem duas vezes na lista; o primeiro é o e-book (id menor). O perfil Có-produtor da conta
  colaboradora tem a permissão "Proteção Para Ebooks (DRM Social)".
- **O que estampa:** "a Hotmart estampará nome e e-mail em todas as páginas do seu documento". **CPF não é opção.** No
  ePub, a marca vai no código da página, sem aparecer na leitura.
- **Opções do PDF** (aparecem depois de marcar "Habilitar em: PDF"): tamanho da fonte, cor (padrão preto) e posição
  (Centro como marca d'água, Rodapé, Cabeçalho, que é o padrão, e Cabeçalho à direita).
- ⚠️ **Em "Outras proteções (apenas para PDF)", cópia e impressão vêm desligadas, ou seja, bloqueadas.** O interruptor
  diz "Permitir", então desligado é proibido. Guia que a página vende com "baixe e imprima" precisa de "Permitir a
  impressão do documento" ligado, senão a promessa quebra e vira chamado no suporte. A senha (que seria o e-mail do
  comprador) vem desligada.
- **Como ficou nos 8 do caso-base:** PDF, Cabeçalho, preto, tamanho padrão, impressão permitida, cópia bloqueada, sem
  senha. Cada um conferido recarregando a página depois de salvar.
- **"Teste seu arquivo"** lista os PDFs do produto e gera uma cópia carimbada, pra ver onde o carimbo cai. Não foi
  testado pelo agente, porque baixa arquivo; ficou com uma pessoa da equipe. Curso sem arquivo não mostra o teste.
- Na tela estreita do painel, os interruptores não aparecem na árvore de acessibilidade. O clique é por coordenada, e o
  estado se confere com zoom antes de salvar: depois do clique o interruptor fica uns segundos num azul claro que não
  diz se ligou.

## 11. Vitrine da área de membros: capa, banner, o que fica à venda e pra onde vai o clique (medido no caso-base)

Área de membros do caso-base, logado como o dono da conta, pelo navegador embutido. Pedido do Rodrigo: vitrine
"estilo Netflix", os 4 guias e um curso menor à venda, e o clique levando pra página de vendas de cada produto.

- **Onde mexe:** Área de Membros → Personalização ("Aparência"). A vitrine é a página inicial e tem editor próprio
  (`/membership/<área>/customize-builder/showcase`), com dois painéis: **Banner** e **Seções**. Cada painel publica
  sozinho. Sair de um painel com alteração sem publicar abre "Quer mesmo sair sem publicar?". "Descartar" volta tudo ao
  publicado. A prévia do aluno fica em `hotmart.com/pt-br/club/<área>`, com "Visualizando como": Produtor, Membro com
  acesso, Usuário sem acesso e Usuário deslogado.
- **Capa de cada produto:** Personalizar → Página do produto → "Capas para vitrine". São duas: vertical **720x1040** e
  horizontal **1280x720**, JPG ou PNG de até 5 MB, com texto alternativo. Sem capa, a Hotmart encolhe a imagem quadrada do
  produto no meio de um fundo branco. Endereço: e-book `/customize/ebook/<id>/cover`, curso `/customize/product/<id>/cover`.
  No e-book o campo mostra a imagem atual com uma lixeira, e só depois da lixeira aparece o envio. No curso o envio
  ("Alterar") já está na tela. Publica produto por produto.
- **O cadeado de "à venda" fica no canto de cima à esquerda da capa.** Marca ou texto nesse canto some embaixo dele.
- **Banner da vitrine: 1920x640, uma imagem só pra computador e celular** (JPG, PNG ou GIF, até 10 MB). Tem link da
  imagem inteira, título e botão (texto e link). No computador, título e botão ficam por cima, à esquerda. Com o botão ou
  o título ligados, a Hotmart escurece a metade esquerda e a arte apaga. No celular a imagem aparece inteira na largura,
  e título e botão vão para baixo dela: no tema claro o título sai branco no fundo branco. No caso-base ficaram título e
  botão desligados, o nome e um botão desenhados na própria arte, e o link na imagem inteira.
- **Banner da página do produto não é tela livre** (Personalizar → Página do produto → Banner,
  `/customize/ebook/<id>/banner`, 1920x640, "proporção 3:1", até 5 MB, dá pra arrastar e reposicionar). Na página que o
  comprador abre pra baixar o PDF, a Hotmart escreve o **nome do produto em branco à esquerda**, põe botões embaixo dele
  e a **imagem do produto (o e-book em 3D) no meio, à direita**, tudo por cima do banner e escurecido. Um banner com logo
  à esquerda e rosto à direita fica com o nome em cima da logo e o e-book em cima do rosto (testado e descartado, sem
  publicar). Ali só cabe fundo: cor, textura, no máximo o ícone na ponta direita. Sem banner, o topo é preto e funciona.
- **Seções:**
  - **"Minhas compras"** mostra o que a pessoa comprou, em card pequeno com a imagem do produto. Não tem formato de capa.
  - **"Produtos à venda"** mostra o que ela ainda não comprou, em capa vertical ou horizontal (a vertical é o "estilo
    Netflix").
  - **"Criar seção"** (Produtos, Trilhas ou Módulos, até 12, vertical ou horizontal) só deixou escolher os 5 cursos
    antigos. Os e-books e os cursos novos não apareceram, e não foi investigado o porquê.
- **Produto só aparece à venda com "Exibir produto de vitrine" ligado** (Configurações do produto → Vendas → Vitrine:
  `/membership/<área>/products/edit/<id>/admin/beta/modules?productId=<id>&showModalPrice=true&settingsTab=sales`).
  Ao ligar, o "Preço ativo" já vem na oferta de **preço base**. Dá pra trocar pela lista de ofertas, pôr desconto pra
  aluno e pra não aluno ou esconder o preço. Salvar mostra "Salvo com sucesso!". Nos e-books do caso-base ficou o preço
  base.
- **Pra onde vai o clique na capa.** A capa usa o link de produtor da Hotmart com a marca da área de membros:
  `go.hotmart.com/<código>?sck=HOTMART_MEM_CA&off=<oferta ativa>`. A API da vitrine devolve esse link em `hotlink`
  (`hotmart.com/api/content/showcase/rest/public/v1/products/<área>/sale`). O resto depende da **"Página de Venda Club"**
  (Vendas → Página de Venda Club, um interruptor por produto):
  - **ligada:** a capa abre a página interna da Hotmart, com título, descrição curta e "Comprar agora", que vai pro
    checkout. No e-book ela fica sem imagem;
  - **desligada:** a capa abre o link numa **aba nova**, e ele leva pra página de vendas padrão do produto. Sem página
    cadastrada, é o **marketplace** da Hotmart. Com página externa cadastrada (Produto → Página do produto → "Páginas
    externas" → Configurar Página, `/products/manage/<id>/sales-page/external` → "Salvar página externa" → "Feito!"),
    é a nossa página, com `?sck=HOTMART_MEM_CA&off=<código>` no fim. O redirecionamento mudou na hora (conferido por
    `curl` no link), embora a lista da "Página do produto" não mostre a externa depois de salvar. Isso também muda pra
    onde vão o marketplace e todo link de afiliado do produto.
  - A API mostra `clubSalesPage.pageOnline: false` uns segundos depois de desligar.
  - No programa principal do expert esse interruptor vem travado e manda conferir as páginas de vendas do produto.
  - O cartão da lista não diz o tipo enquanto a linha "eBook / Consultoria Online" não carrega. E-book e curso com o
    mesmo nome aparecem lado a lado, então confirmar pelo "⋮ → Editar Oferta", que abre a URL com o id.
- **A venda que vem da vitrine e passa pela nossa página:** o script do Dash na página pendura `utm_*`, `src` e `sck` da
  URL no clique do checkout. Assim a venda chega com `sck=HOTMART_MEM_CA`, na oferta que o botão da página usa. Nos guias
  é a de tráfego pago, então o painel do Dash conta essa venda, sem UTM de anúncio.
- **A vitrine vendeu sozinha, por outro caminho (VARIAÇÃO ISOLADA, 1 compradora).** Com o low ticket sem anúncio havia
  três dias, a Hotmart registrou 3 vendas dos cursos, da mesma compradora, em 5 minutos. As 3 são na oferta de preço base
  e não passaram pela nossa página: o `tracking` traz só o `source_sck`, e ele não é o `HOTMART_MEM_CA` da capa (item
  acima). Veio `HOTMART_CLUB_TRENDRECOMMENDEROCB` em duas e `HOTMART_CLUB_PRODUCT_PAGE_OCB` na outra (lido no
  `/sales/history`). Pelo nome dos códigos, é compra feita dentro do próprio Club, por recomendação e pela página do
  produto, que a configuração da vitrine acima não mostra (não conferido na tela). Como é oferta base, a venda fica fora
  dos painéis do Dash de propósito (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.7): entra no valor por
  comprador da linha, não no ROI de anúncio.
- **Subir arquivo do computador pelo navegador embutido (deu certo em 16 envios: 2 PDFs, 13 capas, 1 banner).** Numa aba
  de `app.hotmart.com` o agente põe uma caixa "solte os arquivos aqui" (camada fixa na página). A pessoa arrasta tudo de
  uma vez do Finder. Cada arquivo vai pro IndexedDB da origem e o agente confere o SHA-256 de cada um contra o disco.
  Depois, em cada tela, o arquivo entra no campo de envio por `DataTransfer` e um evento `change`: o PDF do e-book (campo
  escondido do "Enviar arquivo"), as capas e a mídia do banner. O IndexedDB sobrevive à navegação entre telas da mesma
  origem. Isso substitui o "a pessoa arrasta em cada campo" do §8 e não põe arquivo em endereço público. No fim, apagar o
  banco criado pra isso.

## 12. Checkout dos cursos pela tela: duplicar a página, bumps nas duas versões, banner no Topo e publicar

Os 4 cursos do caso-base, logado como o dono da conta, pelo navegador embutido. Pedido do Rodrigo: checkout do curso
igual ao do e-book, com os 3 bumps, mais um banner no topo com a promessa e um CTA ("faltava nos pdf, agora podemos
fazer para os novos"). Nenhuma escrita por API: tudo por clique.

- **Copiar o layout do e-book pro curso:** no construtor do e-book (`custom-checkout.hotmart.com/<id>`), clicar no cartão
  da página publicada → "Duplicar página" → "Duplicar para outros produtos" → marcar o curso → Duplicar → "Página
  duplicada com sucesso!". A cópia nasce no curso como rascunho, "Em Branco (clone)", com o layout das duas versões
  (contador, checkout, vantagens, fundo). **Os bumps não vêm**: a cópia chega sem nenhum, nas duas versões.
- ⚠️ **A lista de produtos dessa janela já veio com "Select all" marcado** (1ª vez, no primeiro curso). Nas 3 vezes
  seguintes veio tudo desmarcado. Sem conferir, a página vai pra todos os produtos da conta. Antes de Duplicar, o campo
  tem que mostrar **um nome só**, o do curso.
- **E-book e curso têm o mesmo nome.** A lista tira o próprio produto de onde se está duplicando, então a partir do
  e-book só sobra o curso com aquele nome. Os e-books vêm primeiro, os cursos depois (ordem de criação). Depois de
  duplicar, conferir que o "(clone)" apareceu no curso e em nenhum outro produto.
- **Bump, um por vez, em cada versão** (celular e computador, §1.1): Order Bump → Escolher produto → marcar a oferta pelo
  código (a linha mostra nome da oferta, código, parcelas e preço; "Carregar mais produtos" até achar) → Selecionar →
  "De" → Descrição → Inserir. A ordem na página é a ordem de inserção.
  - **"De"** tem máscara de moeda: só aceita tecla de verdade (clicar no campo e digitar só os algarismos: `9990` vira
    99,90 com o símbolo da moeda). Valor posto por script não grava. O valor lido tem espaço não separável entre o
    símbolo da moeda e o número; comparar com o espaço normalizado. Com o "De" preenchido, a tela calcula e mostra o
    desconto ("Desconto: ~64%", por exemplo).
  - **Descrição** aceita o texto posto por script (setter nativo + eventos `input` e `change`). Como o cartão não tem
    título (§1), o título do kit vai como primeira frase.
- **Banner no topo = componente "Topo"** (Componentes → Topo): "Imagem do topo", "Imagem do produto" e "Título". Só a
  imagem do topo preenchida. Ao subir, abre "Cortar imagem" (Estilo do Corte: Livre, já com a imagem inteira
  selecionada) → Aplicar → Inserir → "Escolha uma área pontilhada": clicar na linha do contador põe o banner **embaixo do
  contador, em cima do formulário**, na mesma linha. Uma vez por versão.
  - A Hotmart guarda o recorte a **1023 × 341** (de um PNG de 1920 × 640) e serve redimensionado (768 de largura num
    celular de 375 px). Letra de 66 px no arquivo de 1920 fica com ~12,6 px no celular e ainda lê (conferido no ar).
  - No celular sobram ~55 px de fundo escuro entre o contador e o banner (espaçamento do próprio componente).
- **Salvar e publicar:** "Salvar alterações" → "Salvar rascunho" ("Rascunho salvo com sucesso!"). Publicar: "Salvar
  alterações" → "Publicar página" → "Definir como padrão" (já vem marcado) → "Atualizar publicação" → "Sua página foi
  publicada com sucesso!". Recarregar o construtor depois de salvar e conferir as duas versões antes de publicar.
- ⚠️ **Uma aba por construtor.** Uma aba aberta antes das mudanças guarda o estado velho; salvar por ela sobrescreve o
  rascunho. A aba velha foi levada pra lista de páginas antes de fechar o trabalho.
- **Leitura de volta, sem escrever:** `GET .../checkoutLayout/<id>` (§9) devolve, em cada versão, os bumps com o código da
  oferta (`data.product.key`). Nos 4 cursos, os 3 códigos de cada checkout bateram com a tabela de bumps do desenho do
  funil, nas duas versões. E o checkout no ar (`pay.hotmart.com/<código>?checkoutMode=10`), lido em 375 e 533 px:
  contador, banner, o produto e os 3 bumps com o preço riscado.
- Os banners saíram do mesmo processo das capas da vitrine, com conferência antes de subir. Os arquivos entraram pela
  caixa de soltar da §11, desta vez no IndexedDB de `custom-checkout.hotmart.com` (o banco é por origem, então a caixa
  tem que estar numa aba dessa origem).

## 13. Virada do e-book pro curso: vitrine, Página de Venda Club e suspensão de vendas

Os 4 guias do caso-base, logado como o dono da conta, pelo navegador embutido com o painel escondido. Pedido do Rodrigo:
"desativar as vendas dos produtos em PDF, ativar do curso online e trocar os checkouts das páginas".

- **Ordem que não deixa ninguém sem caminho:**
  1. botão da página de vendas apontando pro checkout do curso, publicado;
  2. vitrine: o curso entra e o e-book sai;
  3. por último, suspender o e-book.
  Antes de suspender, procurar em todos os arquivos do projeto o código do checkout do e-book. No caso-base ele só
  sobrou em registro: cadastro das campanhas, desenho do funil e e-mails ainda não montados. O anúncio aponta pra
  página, não pro checkout.
- **Página de Venda Club** (`/membership/<área>/sales-page/settings`): uma linha por produto, e e-book e curso com o
  mesmo nome aparecem lado a lado. O id do produto está nas props do React de cada linha (`product.productId`, uns 10
  níveis acima do interruptor). O interruptor é `button[role=switch]` com `aria-checked`. O clique grava na hora, sem
  diálogo. Relido recarregando a tela: `pageOnline: false`.
- **"Exibir produto de vitrine" desligado**
  (`/membership/<área>/products/edit/<id>/admin/beta/modules?productId=<id>&settingsTab=sales`): o diálogo de
  configurações abre sozinho nesse endereço, com o interruptor em `input[type=checkbox]`. Desligar grava sem botão de
  salvar, e a API da vitrine (§11) tirou o produto em segundos.
- **Suspender vendas:** na página do produto (`/products/manage/<id>`), ao lado do id, fica o interruptor
  `input#salesStatus`, "Vendas ativas". Um clique, sem diálogo de confirmação, e o rótulo vira "Ativar vendas" (continua
  assim depois de recarregar). O checkout antigo passa a cair em `pay.hotmart.com/error?errorMessage=049`. Que o acesso
  de quem já comprou continua não foi conferido com um comprador.
- **O MCP da Hotmart não serve pra conferir produto em que a conta dele é só coprodutora.** Ele lista os produtos da
  conta conectada a ele, e produto em que essa conta não é a produtora não aparece
  (`sirius-scale/frameworks/hotmart/hotmart-api-tecnica.md`, armadilha 13): no caso-base, a consulta pelo id do e-book
  voltou vazia. A prova veio do checkout (código 049) e da tela recarregada.
- **Pixel:** a tela (`/tools/pixel/checkout/<id>`) roda no iframe de `app-vlc.hotmart.com` (§4). A captura de tela
  mostra tudo: o card do Facebook com o visto verde abre "Pixels configurados", com o id, "Evento via Web: Configurado" e
  "Evento via API: Token configurado". O checkout público não serve pra conferir. O pixel não está no HTML: ele vem
  depois, de `api-super-pixel.hotmart.com`, com o código do produtor tirado das comissões.
- **O que a virada não troca sozinha** (cada um tem dono e lugar próprio):
  - os códigos de oferta dos painéis do Dash (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §7.7);
  - os ramos do roteador do Full Funnels, que separam produto pelo `data.product.id`;
  - os compradores do e-book, que não ganham o curso sem importação.

## 14. Módulo de bônus com liberação em dias, e a biblioteca do Player (medido no navegador embutido)

Montado logado como o dono da conta, no módulo 2 de três cursos do caso-base: 8 aulas ao todo. Mecânica da plataforma
(UNIVERSAL); o desenho do módulo é o do caso.

- **Módulo:** Conteúdo → Criar → Criar módulo (`.../admin/beta/modules/new`). O tipo vem antes: principal (conta pra
  conclusão do curso), adicional (não conta) ou adicional pago (vendido à parte). Depois: nome, turmas (a Turma A já vem
  marcada), "Módulo gratuito" desligado e capa opcional. **Módulo não tem estado de publicado:** o menu ⋮ só tem Editar,
  Duplicar e Excluir. Quem publica é a aula. Se um módulo só com aula não publicada aparece vazio pro aluno não foi
  conferido.
- **Aula:** o + do módulo → Aula abre `.../modules/<id do módulo>/content/new`. O id do módulo só aparece nesse
  endereço, e abrir o endereço direto também cria aula ali. Campos: título; Mídias (Hotmart Player, até 3, arrasta o
  arquivo ou "Selecionar arquivo" da biblioteca, até 20 GB); Texto (editor Redactor, `.redactor-editor`); Material
  extra; Liberação e expiração; Tags de busca; Miniatura. **"Criar conteúdo" grava sem publicar** (a lista mostra "Não
  publicado"); "Publicar" grava e publica.
- **Liberação em dias:** Liberação e expiração → Agendar liberação e expiração → ligar "Agendar liberação do conteúdo" →
  tipo "Liberar dias após a compra" (as outras opções são data específica e aprovação em quiz, beta) → número de dias →
  turmas "Todas as turmas" (vale pras futuras também) → Agendar. A linha fica "N dias após a compra · Não expirar · Todas
  as turmas", e a lista de aulas mostra "N dias".
- **A API do Club não lê a área nova:** o `hotmart_modules_list` com o subdomínio da área volta 404. Conferir módulo e
  aula é pela tela (o texto da lista de conteúdo traz nome, estado e dias de cada aula).
- **Biblioteca do Player** (`play.hotmart.com/library`): Novo → Nova Pasta ou Novo carregamento. O campo de envio aceita
  vários arquivos (`multiple`, mov, mp4, avi, mkv, aiff, mid, wav, mp3), e o diálogo oferece importar do Vimeo, do
  Panda Video, do YouTube e do Google Drive. Na medição o Drive já aparecia na tela, que a ajuda (§8) ainda chamava de
  "em desenvolvimento". Não foi testado: pede entrar com uma conta Google e autorizar a Hotmart no Drive, decisão do dono
  da conta.
- **Painel do navegador escondido trava a animação.** Com o painel fora da tela, o modal só termina de abrir quando a
  tela é redesenhada. Cada captura de tela redesenha. Um clique dado antes de o formulário abrir caiu na aba Turmas do
  curso, por baixo, sem estrago. A regra: antes de clicar dentro de um modal recém-aberto, conferir por JavaScript que o
  campo tem tamanho e posição estáveis (`getBoundingClientRect` com largura acima de zero, igual em duas leituras).

## 15. Combo (Hotmart Combos) e o checkout dele (medido no combo da Black do caso-base)

O combo (flexível) foi configurado pela conta colaboradora da casa, dentro da central do expert, pelo navegador
embutido. Mecânica da plataforma; os valores escolhidos são da Black.

- **Onde fica:** Produtos → Meus produtos → cartão Combos (`/products/bundle`). Não aparece na lista de produtos. O
  painel é `/products/bundle/manage/<id>/panel`, e o resto usa as mesmas rotas de produto (`/products/manage/<id>/offers`,
  `/tools/checkout/settings`, `/coproduction`). No painel estreito o menu lateral do combo fica fora da tela; os botões
  existem no DOM e respondem a `click()`.
- **O que o combo não herda dos produtos de dentro:**
  - **Coprodução.** A própria tela avisa que a coprodução dos produtos não vale pro combo. O combo nasceu sem coprodutor,
    mesmo com o programa principal tendo a conta colaboradora como coprodutora. Sem cadastrar no combo, a venda não
    divide a comissão. Quem cadastra é o dono da conta.
  - **Configurações da página de pagamento.** Vêm no padrão da Hotmart: boleto ligado, híbrido desligado, sem e-mail de
    suporte, sem nome na fatura, sem pedir telefone, CPF e endereço, e com os meios internacionais ligados (§5).
  - **Pixel.** Nenhum (§2).
  - **ListBoss.** O combo nasce com as 13 automações do Hotmart Send ligadas, igual ao produto novo (§3.1). Na Black
    foram desligadas pela tela (Ferramentas do combo → buscar contatos → Gestão automática de contatos,
    `/tools/manage/<id>/listboss`): um clique por interruptor, sem diálogo, cada um com o aviso de configuração salva.
    Conferido recarregando: 13 de 13 desligadas.
  - **Google Ads.** Também nasce sem. Copiado do programa principal pela tela de pixel (o cartão Google Ads): ID AW, os
    dois eventos com o rótulo de conversão de cada um e as mesmas opções. Os rótulos se leem exatos pelo texto da página
    (busca na árvore de acessibilidade), não pela captura de tela.
- **Ofertas do combo:** a edição mostra a soma dos produtos ("Valor da soma de todos os produtos neste combo") e o mesmo
  recuperador das ofertas de produto, com o limite de parcelas.
- **Vendas suspensas:** o interruptor Ativar vendas fica no topo do combo. Desligado, o link de qualquer oferta cai em
  `pay.hotmart.com/error?errorMessage=049`, então o checkout publicado só se confere no ar depois de ligar.
- **Página personalizada:** o mesmo construtor do §12, em `custom-checkout.hotmart.com/<id do combo>`, a partir do modelo
  Em Branco. Publicada como padrão, o layout fica `ACTIVE_BY_PRODUCT` na leitura de volta (`GET .../checkoutLayout/<id>`).
- **Versão de computador: o botão Copiar celular.** Ao lado do ícone do monitor, ele copia a montagem do celular pro
  computador na hora, sem diálogo, e substitui o que estava lá. Depois do clique ele vira Desfazer cópia. Resolve o
  problema do §1.1 sem precisar da API.
- **No computador, Topo inserido na área do formulário vai pra baixo dele.** No celular do modelo Em Branco existe uma
  linha vazia em cima (Selecione um componente ao lado), e o Topo cai ali, acima do formulário. No computador essa linha
  não existe, e clicar na área do formulário pôs o banner embaixo. Por isso o Copiar celular.
- O recorte guardado foi 1023 × 341 de novo (§12), a partir do PNG de 1920 × 640.
- **Seletor de produto da tela de pixel:** às vezes volta vazio (Sem resultados, mesmo buscando produto que existe).
  Recarregar a página resolveu, e o produto do endereço apareceu sozinho no seletor.
- **Lista de produtos da central** (`/products/list`) ficou em branco com o painel do navegador escondido. Pelo menu
  (Produtos → Meus produtos, `/products/producer`), carregou.

## 16. Recomenda, a prévia do aluno e administrador por importação (medido na conta do caso-base)

Mecânica da plataforma (UNIVERSAL); os números são do caso-base.

- **Recomenda** (Ferramentas → Recomenda, `app.hotmart.com/cross-sell/top-picks`): é a caixa "Seu próximo aprendizado
  está aqui! Muitos alunos também compraram" que aparece no curso e dentro da aula, com "Comprar agora" em um clique.
  No caso-base estava ligada ("Vendas ativas"), com 13 vendas automáticas em 12 meses. A estratégia é por produto
  (`Para clientes que compraram` → `Recomendamos os seguintes produtos`, em ordem; `Visualizar outro produto` só troca o
  produto mostrado, `Personalizar estratégia` muda a ordem). A lista de produtos traz cursos e pacote; os e-books não
  aparecem. Uma janela de apresentação (`Conferir resultados`) fica por cima da tela e só some com a aba do navegador
  embutido na frente.
- **Prévia do aluno com as travas:** na página do curso (`hotmart.com/pt-br/club/<área>/products/<id>`), o seletor do
  topo troca entre Criador, Membro com acesso e Usuário sem acesso. Como Criador as aulas travadas aparecem abertas,
  com a duração; como Membro com acesso aparecem com cadeado e "Data de liberação" (compra de hoje + os dias).
- **Na aula, o PDF fica em "Materiais", embaixo do texto e da caixa da Recomenda.** No celular, o botão de baixar é só uma
  setinha (o rótulo `Download` fica no `aria-label`); no computador aparece escrito `Download` ao lado dela (print do
  Rodrigo). Texto que manda tocar em Download só bate com a tela do computador.
- **Administrador do curso por importação:** Usuários → Importar Usuários → `Importar um membro individualmente`
  (`/membership/<área>/members/add/<id>/individual`): nome, e-mail, idioma, Papel (Administrador, Editor de conteúdo,
  Moderador, Estudante), Turma (obrigatória pro botão ligar), Data de compra e Motivo (obrigatório; o de convidado ou
  parceiro serve). A tela confirma a importação, manda pro histórico e o usuário aparece na lista em segundos. Os
  seletores são `hot-select`: o valor lido por JavaScript às vezes volta vazio com a opção já escolhida; conferir pela
  tela.
- **Ser Administrador do curso não abre o conteúdo pra conta colaboradora.** Ela já era Administrador nos 4 cursos do low
  ticket e, logado nela, o conteúdo seguiu em "Não foi possível carregar" (§8, `user_area is required`). Quem abre é a
  conta do dono.
- **Onde a Recomenda aparece, pela Central de Ajuda:** na página de obrigado da Hotmart, logo depois da compra; na página
  do produto na área de membros, em cima dos módulos; e na sala de aula, entre uma aula e outra. Na página de obrigado
  ela não aparece em dois casos: quando a página de pagamento usa Funil de Vendas com página de obrigado externa, e
  quando o pagamento não é cartão nem Pix. A esteira de cada produto aceita até 10 produtos ativos, e `Ordenação
  automática` desfaz a ordem manual. Combo, evento e serviço não são elegíveis. Colaborador com a permissão de Gestão de
  Produtos pode mexer no painel, sem precisar da conta do dono. A venda aparece no relatório de vendas detalhado, nas
  colunas `Canal usado para venda` e `Ferramenta de venda`.
  - Na prática, num low ticket de outro produtor (print do Rodrigo), a página de obrigado mostrou um botão
    `Você possui (2) recomendações!`. Ele abre uma janela com 2 produtos já marcados, o total e `Comprar agora`.
  - **Página de obrigado externa tira a pessoa da página onde a caixa mora.** A ajuda diz que a externa manda o comprador
    direto pra página criada fora. Antes de trocar a de um produto que vende pela Recomenda, pesar isso.
- **Banner do curso (formato curso, medido na prévia de um dos cursos):**
  - **Computador:** a Hotmart escreve em branco, na metade esquerda da faixa do topo, por cima do banner: `Voltar`, o
    nome em 2 linhas, a descrição em 2 linhas, `Mostrar mais`, o progresso e o botão `Continuar assistindo`. Sem banner,
    a metade direita mostra uma ilustração genérica.
  - **Celular:** a faixa mostra a imagem inteira, e o nome e o resto vão embaixo, sem sobrepor.
  - A capa do módulo (Editar módulo → `Capa do módulo`) é mostrada num quadro 16:9.
- **Bump com Pix (checkout dos cursos):** os 3 bumps continuam na tela quando a pessoa escolhe Pix, e o total do Pix soma
  o bump. No celular o checkout já abre com o Pix marcado; no computador, com o cartão. As 2 vendas seguidas que foram
  lidas saíram no Pix pelo celular e não levaram bump. Isso não prova nada com 2 vendas, mas é o primeiro lugar a olhar se
  a taxa de bump cair.
- **Trocar o texto inteiro de uma aula pelo navegador embutido (6 aulas, todas lidas de volta):**
  - O campo Texto é um Redactor (`.redactor-editor`). Ele espelha o conteúdo num `textarea` escondido, e é esse
    `textarea` que o Salvar manda.
  - `document.execCommand('insertHTML', ...)` devolve `false` e não muda nada enquanto o documento não tem foco.
  - Com o painel escondido, o foco só vem de um clique de verdade dentro do editor, não de script. Medir a posição depois
    de uma captura de tela: antes dela, o desenho da gaveta ainda está pela metade e o clique cai fora.
  - Com o foco, selecionar todo o editor (`Range.selectNodeContents`) e dar `insertHTML` com os `<p>`. O `textarea`
    acompanha sozinho.
  - Link com `target="_blank"` passa. Na tela do aluno, o `wa.me` abre em aba nova.
  - Salvar → `Alterações salvas com sucesso`.
- **Descrição do curso** (Produto → Informações básicas, `app.hotmart.com/products/manage/<id>/info`):
  - É o `textarea#description`, até 2.000 caracteres. O contador conta as quebras de linha.
  - O valor entra pelo setter nativo do `HTMLTextAreaElement`, com os eventos `input` e `change`. O contador muda na
    hora.
  - Salvar mostra `Feito!`.
  - A tela só desenha com a aba larga: com 1440 px de largura funcionou, com a largura do painel ficou em branco.
  - Mudar a descrição não mandou o produto pra análise: `Vendas ativas` continuou ligado nos 4 cursos, lido depois de
    recarregar. Ela aparece no "Detalhes do Curso" e na caixa da Recomenda.

## 17. Aluno antigo que compra o combo: a "data da compra" da turma nova trava as aulas (medido na Black do caso-base)

Mecânica da plataforma (UNIVERSAL); a regra de liberação e os números são da Black. **VARIAÇÃO ISOLADA** (1 lançamento).

- **O problema.** Quem já era aluno e compra o combo é movido pra turma nova e ganha uma **data da compra nova** (a da
  compra do combo). Os módulos com "Liberar N dias após a compra" (§14) contam os dias a partir dessa data, então quem já
  estava no módulo 5 volta a ver as aulas travadas por 7 dias. A prévia "Membro com acesso" (§16) mostrou a primeira aula
  do módulo 5 com contagem de 6 dias e 8 horas na turma nova. A trava de 7 dias foi mantida de propósito pelo Rodrigo:
  evita baixar tudo, gravar a tela e pedir reembolso na garantia. Por isso o conserto é acertar a data de quem já era
  aluno, não tirar a trava.
- **O combo coloca todo comprador em todos os cursos dele.** Num outro curso do combo, os 50 primeiros compradores da
  Black conferidos apareciam com a data da compra do combo e 0% de progresso: ninguém fora o programa principal tinha
  progresso antes. "Já era aluno" não se mede pela data atual do curso, mede-se pela **compra anterior no histórico de
  vendas** (`/sales/history`, todos os produtos, por janelas de 90 dias) cruzada com o e-mail.
- **Onde se acerta.** Área de membros → Produtos → o curso → Usuários → busca pelo e-mail → ficha → "Editar" ao lado da
  Data da compra → calendário. Salva sozinho, sem botão; a ficha fecha o campo depois de gravar. A chamada por trás é
  `PUT api-club-user.cb.hotmart.com/v4/userArea/<id>/changePurchaseDate` com `{"purchaseDate":"AAAA-MM-DDT03:00:00.000Z"}`
  e volta 200. **A chamada autenticada direto não foi feita** (exigiria copiar o token da sessão; o modo automático
  barrou).
- **Armadilha do calendário.** O calendário (react-dates) só abre com **clique real**; `focus()` e eventos simulados por
  JavaScript abrem em alguns casos e falham em outros ("dia não achado" em vários seguidos). O que funcionou: preparar a
  ficha por script, dar o clique de verdade no campo (com a tela rolada pra ele ficar no centro) e escolher o dia por
  script, pelo `aria-label` completo ("13 de abril de 2026", com a vírgula antes pra "3" não casar com "13" e "23").
- **Busca de usuário por script.** Preencher o campo "Procure por nome ou e-mail" com o setter nativo do
  `HTMLInputElement`, `input` e `keydown/keypress/keyup` com Enter; "Total 1" na tela confirma. Às vezes a busca devolve
  vazio por tempo: tentar de novo antes de dizer que o aluno não está no curso (uma aluna foi "não achada" e estava lá).
- **Painel escondido.** O tamanho emulado da janela é desfeito quando o turno acaba; reaplicar.
- **Quem não precisa mexer:** quem tem data atual de mais de 7 dias atrás (já passou da trava).
- **Conferência feita:** 30 alunos do programa principal que já tinham compra anterior, 22 acertados, 8 já estavam
  certos; leitura de volta de todos. Não foi visto um aluno específico abrir a aula (só a prévia da regra).
