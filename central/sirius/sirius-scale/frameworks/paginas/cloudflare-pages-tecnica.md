# Cloudflare Pages — publicação de página fora do WordPress

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

**Alcance:** `NÃO TESTADO FORA` — base: o caso-base (um expert de educação), 17 páginas
clonadas do WordPress de uma vez (captura, obrigado, lives, 4 aulas, carta, grupo VIP ×2,
LPSG ×5, bio ×2). A receita do §6 se repetiu em todas → CONSISTENTE dentro da
base; o que é fato de plataforma está marcado como UNIVERSAL.

**Fato de plataforma:** limite de plano, comando do wrangler e comportamento de rota são os
da época da medição. A Cloudflare muda: conferir na doc antes de confiar.

## 1. O que existe

- Conta Cloudflare da casa; um token de API com escopo só de Pages/Workers/KV, guardado como
  variável de ambiente (`CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, os nomes que o
  wrangler lê). Não enxerga zona nenhuma (o domínio do caso-base não estava na Cloudflare, §5).
- Um projeto Pages por cliente: **`<projeto>`** → `https://<projeto>.pages.dev`.
  Branch `main` = produção; qualquer outro branch vira prévia em
  `<branch>.<projeto>.pages.dev` com variáveis próprias (§3).
- Pasta do projeto:
  - `site/` — o que sobe: `<slug>/index.html` (um arquivo por página, CSS no
    `<style>`), `imagens/<lançamento>/`, `_redirects` (raiz →
    captura). **17 páginas no ar na virada**, mesmos slugs do WordPress:
    do lançamento gratuito, inscrição, obrigado, lives, aulas 1 a 4 e carta,
    mais dois grupos VIP; do LPSG, inscrição, carta, obrigado e duas de
    aplicação; da bio, duas. Links internos entre elas são relativos; venda
    (o segundo WordPress, §5), Hotmart, YouTube ficam absolutos.
  - `lib/formularios.js` — registro dos formulários (§3).
  - `functions/api/*.js` — backend (Pages Functions). **Tem que ser irmã de
    `site/`, não filha** (UNIVERSAL): o wrangler procura `functions/` na pasta
    onde é executado; dentro de `site/` ele sobe como arquivo estático e o
    `/api/...` responde 404. Foi o primeiro deploy.
- KV `<projeto>-leads`, ligado como `LEADS` — cópia de todo lead antes de
  falar com o CRM (na época, o Mailchimp).

⚠️ **Plano Free da Cloudflare tem dois tetos que importam pra lançamento com
tráfego pago (checados na época; conferir, a plataforma muda):**
- **Workers/Pages Functions: 100 mil requisições/dia** — a página estática
  (HTML/CSS/imagem) é ilimitada e grátis em qualquer plano; só o `/api/*`
  conta aqui. Um lançamento gratuito do caso-base teve pico de ~2.800
  inscrições/dia — longe do teto.
- **KV: só 1.000 escritas/dia, sem fila — passado isso, `put()` lança erro.**
  Esse teto sim é real: o mesmo lançamento teve dias de ~2.800 leads, quase
  3× o limite. A Function de inscrição grava a cópia de segurança dentro de um
  try/catch exatamente por isso — cota estourada vira só um `console.error`,
  nunca erro pro visitante nem trava do CRM. **Sem esse try/catch, passado o
  milésimo lead do dia, a inscrição inteira falhava** (a chamada não tratada
  derrubava a function antes do CRM e do redirect). Se um lançamento real
  precisar da cópia de segurança completa (não só do CRM), o Workers Paid
  ($5/mês, preço da época) sobe os dois tetos pra 1 milhão de escritas e sem
  limite prático de requisição — decisão de custo do dono, não decisão técnica.

## 2. Publicar

```
cd <pasta do projeto>
# CLOUDFLARE_API_TOKEN e CLOUDFLARE_ACCOUNT_ID exportados no ambiente
npx --yes wrangler@latest pages deploy site --project-name=<projeto> --branch=teste   # prévia
npx --yes wrangler@latest pages deploy site --project-name=<projeto> --branch=main    # produção
```

⚠️ **O deploy de produção sobe a pasta `site/` inteira — inclusive rascunho de outra
sessão que só tinha ido pra prévia.** Aconteceu no caso-base: uma troca de prazo numa página
de inscrição subiu junto duas páginas que nunca tinham sido aprovadas (uma página de venda de
e-book, feita dias antes, e uma página de lista). Ficaram ~3 min no ar no domínio do expert
até a republicação sem elas (sem link apontando pra elas).
Antes de todo deploy de produção: listar o que mudou desde o último deploy de produção
(`GET …/pages/projects/<projeto>/deployments` → data do último `production`, e
`find site -newermt <data>`) e publicar de uma cópia sem o que não foi aprovado
(`rsync --exclude`). É checagem frágil (depende de lembrar) até virar script de
publicação que só sobe o slug pedido — *VARIAÇÃO ISOLADA, 1 ocorrência*.

✅ **Na casa, isso virou um script de publicação** (é por ele que se publica; wrangler direto
não). O script não faz parte do kit; o que ele faz é o checklist que vale antes de qualquer
deploy de produção, à mão ou num script de vocês:
1. Subir só (o que já está no ar, registrado num manifesto de publicados) + (o slug pedido).
2. Parar antes de escrever se: o slug está numa lista de bloqueados; alguma página no ar difere
   do disco (comparação byte a byte, descontando o script de analytics que a Cloudflare injeta no
   fim do HTML — sem esse desconto, 21 de 21 aparecem "diferentes"); ou a página pedida usa
   imagem que não vai subir.
3. Parar se a página pedida esconder bloco que não aparece sozinho, que nunca aparece ou que
   aparece antes da rolagem: o que vai subir abre num Chrome com tela de celular, com rastreio,
   Tally e vídeo bloqueados, com o script quebrado e sem JavaScript; antes, um caso ruim de
   controle tem que falhar nos dois (como funciona, no §9; o que pega e o que não pega:
   `sirius-scale/frameworks/paginas/estrutura-de-pagina.md` §7.1). Na prévia, só avisa.
4. Pular a conferência do passo 3 só com motivo escrito, que vai pro log: é decisão do dono, em
   conversa, quando o Chrome quebrou; rotina nunca pula.
5. Depois da produção, ler de volta, conferir que as bloqueadas seguem fora e só então gravar no
   manifesto e no log de publicações.

⚠️ O endereço `teste.<projeto>.pages.dev` (alias da branch) fica em cache e mostra a prévia
velha por horas; conferir SEMPRE no endereço do deploy (`<hash>.<projeto>.pages.dev`), que o
deploy imprime no fim. *VARIAÇÃO ISOLADA, 1 cliente. O caminho de produção pelo script rodou 15
vezes nas três primeiras semanas.*

⚠️ **Deploy feito por fora some do log, e a página pedida sobe do disco por cima dele sem aviso.**
*VARIAÇÃO ISOLADA, 1 ocorrência.*
- **O caso.** Entraram dois deploys de produção que não estavam no log nem no manifesto da máquina que
  publica. O mais provável é uma pasta antiga do projeto, em outra máquina. Eles puseram o replay de umas
  lives em 3 páginas de inscrição, e o disco da máquina principal não tinha o replay.
- **O buraco.** O passo 2 do checklist só compara com o ar as páginas que NÃO foram pedidas. Pedir uma
  dessas 3 teria subido o disco por cima e tirado o replay do ar. Foi achado por acaso, comparando o
  texto do ar com o do disco antes de publicar.
- **A trava, que roda antes do passo 2:**
  - o `canonical_deployment` da Cloudflare (o deploy que serve a produção) tem que ser o último deploy
    que a publicação gravou no manifesto;
  - se não for, parar. Aí é comparar o ar com o disco página por página (`functions/` e `lib/` também,
    que nenhuma outra checagem compara) e só seguir com o hash do deploy de fora anotado no log.
- **Como alinhar o disco com o ar:**
  - baixar a página, tirar o script do Cloudflare Insights (o mesmo desconto do passo 2), gravar no
    disco e conferir o hash;
  - pra saber o que cada deploy mudou, comparar `https://<hash>.<projeto>.pages.dev/<slug>/` de um com o
    do outro.

✅ **Ajuste no disco que não foi pro ar vira aviso sozinho.** *VARIAÇÃO ISOLADA, 1 cliente.*
- **Por quê.** Uma revisão de páginas de inscrição ficou no disco diferente do ar sem ninguém ver. O
  passo 2 só acusa isso quando alguém tenta publicar outra coisa.
- **A conferência** (na casa, um modo do script de publicação que só lê, não escreve na Cloudflare nem no
  manifesto):
  - repete o passo 2 em todas as páginas do manifesto, e a trava de deploy de fora;
  - compara `functions/`, `lib/` e `_redirects` com uma foto do que subiu (o sha256 de cada arquivo,
    gravado no manifesto a cada produção). A foto existe porque a data sozinha engana: script que regrava
    um arquivo inteiro e `cp -R` mudam a data sem mudar o conteúdo;
  - lista cada pendência com a data do disco e o trecho de texto que mudou («antes» → «depois», ou "a
    diferença está no código");
  - ignora rascunho fora do manifesto;
  - sai 0 (nada), 1 (tem pendência) ou 2 (não deu pra conferir).
- **A rotina.** Na casa, confere uma vez por dia. Pendência com mais de 24h vira um aviso só pro dono,
  que se atualiza quando a lista muda e fecha sozinho quando tudo volta a bater. A rotina não resolve a
  pendência: publicar ou voltar o disco é decisão do dono.
- **O que não pega:**
  - imagem trocada com o mesmo nome em `site/imagens/`: a página não muda, então nada acusa;
  - o que um deploy de fora pôs em `functions/` ou `lib/`: a trava avisa o deploy, não o conteúdo.
- **Medido:** 18 casos de teste, e cada um dos 18 estragos de propósito no código foi pego por pelo menos
  um deles. Na primeira rodada, 35 páginas iguais ao ar e nada pendente.

⚠️ **Página corrigida direto no HTML: o gerador dela fica velho, e a mudança seguinte entra no HTML.**
*Fato do caso (4 páginas de vendas de low ticket do caso-base); não é padrão.*
- **O caso.** As 4 páginas saíram de gerador (um template e um arquivo de conteúdo por guia). As 67
  correções do expert foram feitas direto no HTML e publicadas, e os geradores não acompanharam.
- **O que vale nessas páginas:** a fonte é o HTML publicado, e regenerar desfaz o que o expert corrigiu.
  Mudança nova vai por script que mexe só no trecho e confere o resto:
  - troca exata, que exige o texto antigo uma vez só e para sem gravar a página se não achar;
  - bloco entre marcadores, com a página conferida byte a byte fora dele;
  - variante de teste montada a partir do HTML do controle, que não se edita à mão.
- **Nenhuma checagem do checklist pega isso.** A página regenerada vai pro disco e sobe como página
  pedida; o passo 2 só compara com o ar as que não foram pedidas, e a conferência de pendências acusaria
  a diferença como ajuste a publicar.

Ordem que funcionou: prévia → testar formulário de ponta a ponta (§4) →
produção. `--commit-dirty=true` só cala o aviso de git.

⚠️ **Imagem reaproveitada de página que nunca foi pra produção dá 404 no ar.**
Aconteceu no caso-base: a página da lista da Black ia usar a foto do expert de uma
pasta de imagens do low ticket, mas essa pasta só existia no disco (a página de low
ticket nunca foi aprovada nem publicada), e o `HEAD` em produção devolveu 404. Na
prévia local tudo carrega, então o erro só aparece depois do deploy.
Regra: página nova só aponta pra imagem que já está no ar (conferir com `curl -I` na
URL de produção, que não dispara pixel) ou copia a imagem pra pasta dela
(`/imagens/<slug-do-lançamento>/`). *VARIAÇÃO ISOLADA, 1 ocorrência.*

**Projeto novo: criar pela API, não pelo wrangler (VARIAÇÃO ISOLADA).** No wrangler
4.145, `pages project create` falhou com `missing worker entrypoint or assets directory`: o comando
agora passa pelo caminho de migração de Pages pra Workers. Criar com
`POST /accounts/<CLOUDFLARE_ACCOUNT_ID>/pages/projects` e o corpo `{"name": "...", "production_branch": "main"}`
(mesmo token). O `pages deploy` continuou funcionando normal na mesma versão. Primeiro caso:
o projeto da home nova do caso-base. O `*.pages.dev` de projeto recém-criado levou ~45 s pra resolver.

### 2.1 Ciclo da página: lançamento acabou, a página redireciona — *VARIAÇÃO ISOLADA (decisão do Rodrigo, 11/2026)*

O link fica rodando em grupo, e-mail e post muito depois do lançamento. Nas palavras dele: "O que não pode é estar a
página aberta do jeito que a gente divulgou."
1. Fim do lançamento: inscrição, obrigado, lives, aulas e grupo vão pra página de vendas do produto.
2. Venda fechada: vão pra lista de espera do produto. Melhor apontar direto pra lista e, quando o carrinho abrir,
   redirecionar só a lista pra página de vendas nova: é uma linha, e todo link antigo chega na venda.
3. Oferta pontual sem lista própria: vai pra página de links da bio.
4. Endereço com data só em lançamento gratuito (`inscricao-lc-<mês><aa>`). Lançamento pago semanal, perpétuo e página
   fixa nunca levam data. Página datada que continua vendendo troca de nome, e a antiga redireciona.

**Como se faz:** duas linhas no `_redirects`, `/slug` e `/slug/`, com **302** (temporário de propósito: o destino muda a
cada lançamento, e o 301 fica preso no navegador). O Pages leva a query (a UTM) sozinho; confira lendo os dois endereços
de volta depois do deploy. O HTML fica guardado fora do deploy, pra poder voltar. Toda página de lançamento nasce com a
data de fim e o destino anotados, pra ninguém esquecer.

**Antes de mexer numa página gerada por script, compare a saída do gerador com o HTML do ar.** Tag posta direto no ar
(Clarity, pixel) some na próxima geração, sem aviso.
## 3. Variáveis (por ambiente, via API `PATCH /pages/projects/<projeto>`)

`MAILCHIMP_API_KEY` (secret) e `MAILCHIMP_LIST_ID`, nos dois ambientes. **Só na
prévia: `MAILCHIMP_TAG_TESTE = TESTE-CLOUDFLARE`**, que substitui a tag real de
qualquer formulário — a tag real dispara a automação do lançamento, e teste
não pode acionar sequência de e-mail de verdade. Contato de teste é arquivado
depois (`DELETE /3.0/lists/<id>/members/<md5>`). Variável só vale pra deploy
feito DEPOIS de mudá-la (republicar).

**Um backend, vários formulários:** cada página manda
`<input type="hidden" name="formulario" value="<chave>">`, e `lib/formularios.js`
diz o que a chave faz (tag do CRM, página de obrigado, se o redirect
leva `?email=&nome=&telefone=`). Chave desconhecida cai no padrão
(o formulário de inscrição do lançamento em curso). Formulário novo = uma entrada nesse arquivo, lida do
`_elementor_data` da página original — nunca aceitar tag/redirect vindos do
navegador.

### 3.1 Duas armadilhas de segurança das Functions — *UNIVERSAL (fato de plataforma, medido em 11/2026)*

1. **O roteador não diferencia maiúscula.** `/api/Area/rota` cai na rota `functions/api/area/rota.js` (o wrangler
   4.x monta as rotas sem `sensitive`). Um `_middleware.js` que tranca área por `startsWith("/api/area/")` deixa a
   mesma rota aberta com uma letra maiúscula. O middleware compara o caminho decodificado e em minúsculas, e a rota
   protegida confere a permissão de novo, sozinha.
2. **Deploy antigo não sai do ar.** Cada deploy continua respondendo no endereço próprio (`<hash>.<projeto>.pages.dev`, e
   os apelidos de branch), com as variáveis que tinha quando foi feito. Tirar uma variável só vale pros próximos deploys.
   Pra desligar de verdade, apague o deploy (`DELETE /pages/projects/<p>/deployments/<id>?force=true`).
## 4. Formulário: o que o Elementor fazia e como ficou

Lido do `_elementor_data` (§6): `save-to-database` + e-mail pra caixa de administração do domínio +
Mailchimp (FNAME/PHONE + tag) + redirect
`obrigado-<lançamento>?email=&nome=&telefone=`; 6 hidden `utm_*` vindos da query
string (`request-arg`). A Function de inscrição (`functions/api/inscrever.js`) faz o mesmo
na mesma ordem — grava no KV **antes** do CRM (falha lá não perde lead,
fica `mailchimp_erro` no registro pra reprocessar) e redireciona com
`encodeURIComponent` (espaço = `%20`). O e-mail pra caixa de administração ficou fora até o
dono dizer que alguém lê. Honeypot `site`: preenchido → redireciona sem
gravar. Teste de ponta a ponta: KV ok, Mailchimp `subscribed` com FNAME/PHONE/tag,
redirect na página real de obrigado.

### 4.1 O nome do parâmetro tem que ser o nome do campo oculto do Tally — *VARIAÇÃO ISOLADA (medido uma vez)*

O obrigado de um lançamento do caso-base (widget copiado do Elementor) repassava o número pro Tally
como `telefone`, mas o campo oculto do formulário se chamava `whatsapp`. O Tally
ignora parâmetro que não conhece, sem erro: a coluna WhatsApp da planilha da pesquisa
ficou vazia nas 7.741 respostas, e o Dash, que pega o telefone da pesquisa
(`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §2.9), ficou sem número. O Mailchimp recebia (PHONE), porque
é outro caminho. **Conferir antes de publicar:** ler os campos ocultos do formulário
(`curl -s https://tally.so/r/<id>` → `__NEXT_DATA__` → bloco `HIDDEN_FIELDS`) e bater
com os `addParam` do obrigado. Vale igual pra qualquer formulário que vier no lugar do
Tally (Full Funnels etc.): o nome tem que casar. O obrigado da Black já manda os dois
(`telefone` e `whatsapp`).

### 4.2 Formulário novo vai pro Full Funnels, pelo nosso formulário — *decisão do Rodrigo*

A casa migrou do Mailchimp pro Full Funnels. **Página nova usa o nosso formulário (HTML na
página → `/api/inscrever`) com `crm: "fullfunnels"` em `lib/formularios.js`. Não se embute o
formulário do Full Funnels.** Os motivos: o dele carrega um pacote pesado num iframe de outro
domínio (página mais lenta, pixel e UTM se perdem na janela de fora), perde a cópia de segurança
no KV, a separação aluno × não aluno e o checkout pré-preenchido, e não se cria por API
(`sirius-scale/frameworks/automacao/fullfunnels-highlevel.md` §8), então toda página nova teria
passo manual na tela.

Como funciona (testado de ponta a ponta numa prévia, com um formulário de inscrição da Black,
contato lido de volta):

- `POST /contacts/upsert` com `name`, `email`, `phone` (+55), `source: "pagina <formulario>"`,
  `tags: [<tag do formulário>]` e as 6 UTMs em `customFields` (`{key: "utm_source", field_value}`).
  Upsert não duplica contato que já existe. ⚠️ E o Full Funnels funde contato pelo telefone:
  `sirius-scale/frameworks/automacao/fullfunnels-highlevel.md` §8.2.
- **UTM só vai se veio preenchida.** Inscrição orgânica de quem já é contato não apaga a origem
  anterior; inscrição paga nova sobrescreve (fica a última origem paga; o histórico de
  lançamentos está nas tags).
- Variáveis `FULLFUNNELS_TOKEN` (secret) e `FULLFUNNELS_LOCATION`, nos dois ambientes. No
  caso-base elas ainda não existiam em nenhum ambiente quando os formulários da Black ficaram
  prontos: tudo teria caído só no KV com `fullfunnels_erro`. Nenhum lead real perdido: só havia
  teste. **Conferir as variáveis nos dois ambientes antes de ligar o formulário.**
  Na prévia, `MAILCHIMP_TAG_TESTE` troca a tag dos dois CRMs por `TESTE-CLOUDFLARE`.
- **A automação do Full Funnels dispara por tag adicionada**, não por formulário enviado
  (não existe envio de formulário do lado deles). Cada página manda a tag dela.
- **O Dash Fácil pega o lead pelo pixel dele** (o script de rastreio na página, §7), não
  pelo CRM. Trocar Mailchimp por Full Funnels não mexe no Dash, desde que a página nova leve o
  script do Dash.
- Conferir pela leitura: o `GET /contacts/?query=` do Full Funnels demora alguns segundos pra
  achar contato recém-criado (achados 0 aos 3 s, 1 aos ~10 s). Zero logo depois do envio não é
  falha: olhar antes o `fullfunnels_erro` no registro do KV.
- Contatos de teste ficam na conta com a tag `teste-cloudflare` (não se apagam sozinhos).

### 4.3 Venda: o checkout da Hotmart sai preenchido com o formulário — *decisão do Rodrigo*

Página de vendas que pede dados antes do pagamento manda pro checkout da Hotmart já preenchido com o que
a pessoa digitou. Fala dele: "tem que adicionar sempre nas paginas de vendas o checkout pro populado da
hotmart, pra que ja venha preenchido o que ela digitar no formulario anterior".

- **Parâmetros** (herdados do Elementor de uma reabertura do caso-base; na casa, um modo de redirect da
  Function de inscrição): `name`, `email`, `phone` (como digitado) e o telefone partido em `phoneac` (DDD)
  e `phonenumber`, sem o 55 da frente. As UTMs, o `src` e o `sck` que chegaram na página seguem junto.
- **Com formulário da casa:** o registro em `lib/formularios.js` leva esse modo e o `redirect` com a
  oferta e o `checkoutMode=10` (`sirius-scale/frameworks/hotmart/hotmart-configuracao-produto.md` §1).
- **Quando o link sai no navegador** (uma Black que confere aluno antes de mostrar o preço): uma função
  na página monta o mesmo link a partir do formulário, e o link de aluno, que o verificador devolve,
  passa pela mesma função antes de virar botão. Testado numa prévia: nome, e-mail, DDD, número, UTM e
  `sck` no link.
- **Não vale pro low ticket:** lá não tem formulário antes, e o clique vai puro pro checkout da oferta
  própria (`sirius-scale/frameworks/paginas/estrutura-de-pagina.md` §5).
- Que a Hotmart preenche cada campo com esses nomes foi visto num lançamento do caso-base; num combo de
  Black, só dá pra conferir quando as vendas abrirem (até lá o link cai no erro 049 de vendas suspensas).

## 5. Domínio

✅ **No caso-base, as páginas passaram a responder num subdomínio do domínio do expert**
(custom domain `active` no projeto, resolvendo em IPs da Cloudflare, `cf-ray` presente,
0,4 s). O expert tinha duas versões do domínio (com e sem `.br`), e o mesmo subdomínio na
outra versão continuava sendo um segundo WordPress, o das páginas de venda (a página de
venda respondia em PHP lá; a de inscrição dava 404). Ao apontar anúncio, usar sempre a
versão do domínio ligada ao projeto. Medido na virada: os dois pixels da Meta (PageView e
ViewContent), GTM, Clarity e Dash Fácil disparando; **o script do Dash Fácil
(`rastreio.js`, na época carregado pelo GTM) é quem anexa `utm_*`, `src` e `sck` aos links
do checkout na hora do clique** — o HTML estático não tem nada disso, e a conclusão
"a página não repassa UTM" (tirada só do HTML) estava errada. Conferir
sempre pelo `href` do botão no navegador, depois do carregamento.

A outra versão do domínio **não estava na Cloudflare**: os nameservers eram os da
hospedagem do WordPress, sem `cf-ray`. Ligar domínio que está fora da Cloudflare = um CNAME
do subdomínio → `<projeto>.pages.dev` no painel de DNS da hospedagem + custom domain no
projeto. **Se o subdomínio já está ocupado por outro site** (era o caso do segundo
WordPress, das páginas de venda), escolher outro nome. Não migrar o DNS inteiro com o site
no ar.

## 6. Copiar uma página do Elementor com fidelidade (receita)

1. `GET <WP_URL>/wp-json/wp/v2/pages/<id>?context=edit` com
   `WP_USER:WP_APP_PASSWORD` (senha de aplicativo do WordPress, guardada como
   variável de ambiente): o `meta._elementor_data` vem
   inteiro — textos, widgets, settings do formulário (ações, redirect,
   chave do Mailchimp em texto puro: **redigir antes de salvar em arquivo**).
   `_elementor_page_settings` traz o `custom_css`.
2. O CSS gerado da página + kit global está **inline no HTML renderizado**
   (bloco `<style>` com `.elementor-kit-N` e `.elementor-<id> ...`, 3
   breakpoints: `max-width:1024px`, `max-width:767px`, `min-width:768px`).
   Salvar HTML, esse CSS, o body sem scripts e as imagens na pasta do
   lançamento (`lancamentos/<AAAA-MM-nome>/paginas/<slug>-elementor/`).
3. Página fechada por 301 da plugin **Redirection** (`x-redirect-by:
   redirection`) casa a URL exata: **`?ver=1` passa** e mostra a original —
   serve pra comparar visual. A de obrigado com query string também passa
   (é assim que o redirect pós-formulário continua caindo nela).
4. O `webdesigner` reconstrói do zero a partir disso (valores do CSS, não
   estimativa). **Animações entram junto** (regra do Rodrigo): ler
   `_animation` + `animation_duration` no JSON (`slow` = 2s, padrão 1.25s,
   `fast` = .75s) e reproduzir com keyframes + IntersectionObserver
   (elemento fica `visibility:hidden` até entrar na tela, como o
   `elementor-invisible`); toggle/acordeão viram `<details>` com abrir/fechar
   de 400ms via Web Animations API. `prefers-reduced-motion` desliga tudo.
5. Firewall da hospedagem bane rajada: pausa entre downloads
   (`sirius-scale/frameworks/paginas/wordpress-criacao-tecnica.md`, armadilha 2).

## 7. Pixels — o que o GTM cobre e o que não cobre

⚠️ **No caso-base, as páginas deixaram de usar GTM.** O container foi publicado vazio
(versão "1", zero tags; quem e por quê só o histórico do GTM diz) e o Dash e a
conversão do Google pararam por dois dias sem ninguém ver: 125 leads fora do Dash (reimportados,
`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §11) e o Google Ads gastando com zero
conversão. Agora o rastreio mora direto no `<head>` de cada página (pedido do Rodrigo):
- `rastreio.js` do Dash com `dfq('init', '<id do projeto no Dash>')` (o trecho vem do próprio
  Dash, Configurações → Projetos → Pixel, §10.3);
- `gtag.js` com o id da conta do Google Ads (`AW-<conta>`, remarketing) e, em página cujo
  caminho contém `obrigado`, a conversão de lead (`AW-<conta>/<rótulo>`, a mesma que o GTM
  disparava). O rótulo sai de `conversion_action.tag_snippets` na API do Google Ads.
- O Clarity que importava (o das 4 páginas do low ticket) estava direto no HTML: não dependia
  do GTM e seguiu medindo. O Clarity do GTM, nas outras páginas, não voltou (ninguém usava).
  Também não voltou o PageView de um segundo pixel da Meta, sem uso.
  - **Ler esse Clarity: são duas fontes, e cada uma tem o que falta na outra** (fato de ferramenta,
    medido uma vez):
    - a exportação por API (`project-live-insights`) só volta 1 a 3 dias e dá rolagem e tempo por
      endereço, com a UTM, em até 10 chamadas por dia;
    - a lista de gravações pelo MCP (`list-session-recordings`) voltou pelo menos 11 dias. Por sessão,
      traz o início, as páginas, o tempo ativo e cada clique, com o texto do botão e um código do
      elemento que o Clarity não documenta (nas páginas de low ticket ele separou o 1º botão do 2º,
      inferido pela rolagem). Não traz a rolagem. O clique no botão de compra só aparecia ali;
    - pra ter as duas coisas na mesma sessão, casar pelo endereço: com o `fbclid`, cada endereço pago é
      uma sessão. Horário em UTC, 250 sessões por chamada. Os 11 dias são o que se viu, não o limite.
- **Página nova nasce com esse bloco** (copiar de uma página no ar). Na casa, uma checagem
  automática baixa as páginas publicadas e acusa BLOQUEIO se faltar Dash, Google ou a conversão
  no obrigado. Do lado de vocês, antes de publicar: abrir o HTML e conferir as três coisas
  (script do Dash com o id do projeto, `gtag.js` com o id da conta, conversão de lead no
  obrigado). Isso confere só o HTML; o efeito continua sendo no navegador (abaixo).
  *VARIAÇÃO ISOLADA.*

O texto abaixo é o histórico de quando o GTM existia:

- O GTM no `<head>` + `<noscript>` reproduzia: PageView num pixel secundário da Meta, eventos
  custom no pixel das campanhas, Google Ads, Clarity e **o script do Dash Fácil** (era o GTM
  que carregava `server.dashfacil.com` — atribuição veio junto). Gatilhos do container não
  filtravam hostname (só `path contém "obrigado"`), então funcionaram no `pages.dev`.
- **O PageView do pixel das campanhas NÃO vinha do GTM**: no WordPress quem dispara é o
  plugin oficial da Meta, no site inteiro. Sem ele na página nova, público de site e LPV das
  campanhas ficam cegos. Entra à mão no `<head>` (init + PageView + noscript). Medido na
  virada: antes, só o pixel secundário disparava; depois, os dois.
- PixelYourSite (pixel secundário + CAPI) não foi replicado: pixel marcado como não
  usado na conta.
- Conferir sempre pelo efeito, no navegador: `fbq.instance.pixelsByID` e
  `performance.getEntriesByType("resource")` filtrando `facebook.com/tr`.
- **O Lead do pixel das campanhas também não vinha do GTM** *(VARIAÇÃO ISOLADA)*. No
  WordPress era o plugin da Meta que mandava `Lead` no envio do formulário; a cópia no Cloudflare levou
  só o PageView. Em três dias o pixel recebeu 6 Lead, todos do WordPress, contra 96 pesquisas
  respondidas no obrigado da Black: a captação da Meta, que otimiza por cadastro, ia rodar às cegas. O
  GTM só cobria o Google (a conversão de lead disparava em todo caminho com `obrigado`), e a tag
  da Meta que ficava nesse gatilho estava PAUSADA no container. Conserto: `fbq('track','Lead')` na
  página de obrigado, só com `?email=` na URL (ela só abre pelo redirect do `/api/inscrever`) e uma
  vez por sessão (conferido pela requisição `ev=Lead`). **Página de cadastro nova no Cloudflare: o
  obrigado precisa do Lead antes de campanha de cadastro.** Na casa isso virou trava em código: a
  ativação de campanha de LEAD recusa se o pixel não recebeu Lead do host da página nos últimos 3
  dias. Do lado de vocês, antes de ativar campanha de cadastro: conferir no Gerenciador de Eventos
  que o pixel recebeu `Lead` vindo do domínio da página nos últimos 3 dias. Outras páginas de
  cadastro do caso-base seguiram sem o Lead.
- ⚠️ **E-mail na URL vai pra Meta.** O redirect do formulário leva `?email=&nome=&telefone=` pro obrigado
  (o Tally precisa), e o pixel manda a URL inteira no parâmetro `dl` de todo evento. Achado e não
  corrigido no caso-base: o caminho seria ler os dados e limpar a URL (`history.replaceState`) antes
  do pixel, passando os valores pro Tally por variável. (O conserto foi feito depois, no segundo
  cliente: §11.1.)

**Microsoft Clarity em todas as páginas** (decisão do Rodrigo, 11/2026: "acho q vale a gente sempre instalar o clarity
em todas as paginas"). *VARIAÇÃO ISOLADA.* É o que deixa a otimização olhar também a página
(`trafego/otimizacao-em-tres-niveis.md` §7.1). Um projeto do Clarity por cliente, nunca o de outro; mais página no mesmo
projeto não gasta chamada a mais. A tag vai no `<head>`. Página que sobe sem a tag do projeto do cliente é aviso no
resumo da entrega.
## 7.1 Popups do Elementor

Botão com `href="#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3D<base64>"`
abre um popup; o base64 decodifica pra `{"id":"<id do popup>","toggle":false}`. O
popup é um template (`elementor_library`), lido pela mesma REST
(`/wp-json/wp/v2/elementor_library/<id>?context=edit`), com o markup já
dentro do body renderizado da página (`#elementor-popup-modal-<id>`) e o CSS
num `<style>` próprio. Os gatilhos ficam no `data-elementor-settings` do
`.elementor-location-popup` (ex.: `{"triggers":{"page_load":"yes",
"page_load_delay":1}}`). Na cópia vira `<dialog>` + o mesmo formulário do
backend (§3).

## 8. O que ainda não existia (no caso-base, na época)

- E-mail de aviso por lead (decisão pendente: ninguém confirmou que lia a caixa de administração).
- As páginas de VENDA (no segundo WordPress) — sem acesso (precisa de senha de aplicativo
  criada lá).
- Reprocessar registros do KV com `mailchimp_erro` (era manual).
- Domínio próprio (§5) e, depois dele, `canonical` nas páginas.
- Datas/cronômetros das páginas copiadas são os do lançamento que já
  passou (é cópia): lançamento novo = trocar `data-alvo`, datas nos textos e
  o registro de formulários. As páginas continuam com a copy aprovada, mas o
  conteúdo novo passa pelo agente `copy` (`sirius-scale/REGRAS.md` §3).
- Numa página de aula, o card da aula 4 trazia data e hora do lançamento antigo (sobra do
  original; o Rodrigo ainda não tinha decidido se corrige na cópia).

## 9. Conferir a página antes de publicar (UNIVERSAL, medido uma vez; conferir, a ferramenta muda)

- **Chrome headless no macOS não abre janela com menos de 500 px de largura**:
  `--window-size=390,…` entrega um layout de 500 px recortado, sem avisar
  (`innerWidth` = 500; limiar exato 499 → 500; igual no `--headless` antigo e no
  `=new`, Chrome 153). Pra ver a página em 375 px, usar o navegador embutido do
  Claude com viewport emulado, ou uma
  página de teste com `<iframe width="390" height="844">` dentro de uma janela
  de 800 px. Script de captura que receba largura menor que 500 deve recusar, por isso.
- **Captura em 390 px de verdade, sem janela (VARIAÇÃO ISOLADA, 1 página):**
  emulação pelo DevTools Protocol (`Emulation.setDeviceMetricsOverride` com
  `mobile: true` e `deviceScaleFactor: 2`) não depende do tamanho da janela, então
  o piso de 500 px não se aplica. Na casa isso virou um script de captura com três modos
  (`celular`, `desktop` e `og` 1200×630) que força as imagens `lazy` e o que aparece ao
  rolar antes de capturar (senão a captura sai com buracos), e um segundo que corta a
  captura longa em colunas pra ler a página inteira numa imagem só.
- **Captura de página inteira** funciona com janela alta:
  `--window-size=500,19000 --screenshot=… http://127.0.0.1:8788/<slug>/` (uma
  página de 15.500 px saiu inteira); cortar a sobra abaixo do rodapé com PIL.
- Servir pelo `wrangler pages dev site` (porta 8788) — por `file://` as imagens
  absolutas `/imagens/...` não carregam.
- Toda visita de conferência dispara pixel, GTM e o rastreio do Dash Fácil
  (recebe `sck`), inclusive em prévia: conferência conta como tráfego real.
- **Conferência rolando sem rastreio, automática (VARIAÇÃO ISOLADA):** a exceção ao item
  acima é a conferência automática da casa (um script que não faz parte do kit; o que segue é
  como ela funciona, pra quem montar uma igual). Ela abre a página em 390 px pelo DevTools
  Protocol e barra pixel da Meta, Dash, Google, Clarity, o analytics da Cloudflare, o Tally e
  os players de vídeo. A lista de hosts barrados é o que vale: host fora dela passa. ⚠️ O
  `Network.setBlockedURLs` sozinho NÃO barra a navegação de iframe: na primeira versão, o embed
  do Tally e o do YouTube carregaram em 10 páginas. Por isso toda requisição passa pelo domínio
  `Fetch` do protocolo e a de terceiro conhecido falha antes de sair; se alguma resposta dessa
  lista ainda chegar, a conferência acusa "não deu pra conferir" em vez de seguir. Na calibração
  no modo de trava (34 páginas, 3 rodadas cada), nenhuma requisição dessa lista passou e nenhuma
  página foi barrada sem motivo: as 5 que revelam ao rolar deram 22 blocos, todos aparecendo
  sozinhos. Servindo a pasta no lugar do domínio (`Fetch.fulfillRequest`), ela confere o que VAI
  subir, sem deploy (é o passo 3 do checklist do §2); sem isso, confere o que está no ar.
  O Chrome abre a porta de depuração em menos de 1 s quente e já levou ~7 s frio; a espera vai
  até 36 s. Precisa de Node 22 ou mais.

## Segundo projeto Pages (de um produto de outra empresa)

Segundo projeto Pages da casa, pra um SaaS, produto de outra empresa do Rodrigo, no mesmo desenho
(`site/<slug>/index.html`). Primeira página: `/privacidade/`.

⚠️ **O `wrangler pages project create` quebrou** no wrangler 4.149: ele tenta detectar
um diretório de arquivos estáticos antes de criar e aborta com `Could not detect a
directory containing static files`, mesmo rodando dentro da pasta certa. O caminho que
funciona é criar pela **API REST** e só então usar o wrangler pro deploy:

```bash
curl -s -X POST "https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/pages/projects" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" -H "Content-Type: application/json" \
  -d '{"name":"<projeto>","production_branch":"main"}'

npx wrangler@latest pages deploy site --project-name <projeto> --branch main --commit-dirty=true
```

⚠️ **A URL sem barra final responde 308, não 200.** `/privacidade` redireciona;
`/privacidade/` entrega. Onde a URL vai ser colada em formulário de plataforma (foi o caso
do campo de Política de Privacidade do app da Meta), **usar a versão com barra**.

---

## 10. Clonar uma SPA (Lovable, Vite, React) — *VARIAÇÃO ISOLADA (1 página)*

*(Renumerada: era um segundo §9. Referências de outros arquivos a "§9" deste arquivo são
todas da conferência antes de publicar, acima.)*

> ⚠️ **Fora da base deste arquivo.** As 17 páginas do §6 são Elementor/WordPress,
> do caso-base. Esta seção nasceu da página de um SaaS feita em Lovable, produto de
> **outra empresa** do Rodrigo. O alcance no cabeçalho **não** muda com uma página só; o que transfere
> é o método, não os números.

A receita do §6 não serve: lá o conteúdo mora no banco do WordPress e sai pela
REST. Numa SPA não existe conteúdo no servidor.

**Medido:** `curl` na página original devolve **7,8 KB** e **35
caracteres de texto visível** (só o `<title>`). O corpo inteiro nasce no JS.

### 10.1 A fonte é o DOM depois do render

```
# com a página aberta num navegador automatizado (ou no console do DevTools):
window.__dump = document.documentElement.outerHTML; window.__dump.length
# puxar em fatias de 40k — o shell trunca saída grande
```

O bundle de CSS (`/assets/index-*.css`, 231 KB no caso) vai inteiro: dá
fidelidade quase total sem reconstruir componente por componente, porque o
Tailwind já está compilado ali. As imagens vêm com `src` **relativo**
(`/__l5e/assets-v1/<uuid>/<arquivo>.png`), não absoluto.

Na casa, a montagem é um script; o que ele resolve está em §10.2 a §10.4.

### 10.2 Três coisas que a captura quebra em silêncio

**1. O painel fechado não existe no DOM.** O acordeão é Radix: os 13
`role="region"` vêm **vazios**, e o clone abre a pergunta em branco. Só se
resolve abrindo **uma de cada vez** na página original (acordeão de item único:
abrir uma fecha a anterior), guardando o `innerHTML` de cada painel, e
injetando na montagem.

**2. O identificador de origem vem congelado.** O CTA da página original leva
`?sck=<uuid>|<sessão>|<_fbp>|`, e esse valor é escrito em runtime. O DOM
capturado guarda o **id do navegador que clonou** — se ficar, **todo visitante
entra com o mesmo identificador** e a origem da venda vira uma pessoa só.
Limpar a query na montagem e remontar no load:

| campo | de onde sai |
|---|---|
| 1º | `localStorage.dashfacil_uuid` |
| 2º | `localStorage.dashfacil_session_id` |
| 3º | cookie `_fbp` |

⚠️ **O `rastreio.js` do Dash não reescreve o href sozinho** — medido: 2,5 s
depois do load o link seguia limpo. Quem montava era o React da página. Na
cópia, isso vira um script de 15 linhas.

**3. O link do WhatsApp carrega a origem em caracteres invisíveis.** O texto da
mensagem leva `ZWSP/ZWNJ/ZWJ` codificando o uuid. A função pronta é
`window.dashfacil.WhatsAppTracking.decorateWhatsAppUrl(url)` — e ela devolve
**`{href, changed}`, não uma string**. Atribuir o retorno direto no `href`
falha calado dentro de um `try/catch`.

### 10.3 Pixel do Dash: um `init` por projeto, e o do dono vem junto

O script é `server.dashfacil.com/static/assets/rastreio.js` com
`dfq('init','<id do projeto>')`. O id sai de **Configurações → Projetos →
Pixel**, por projeto (o projeto da casa tinha um id; a página original
carregava outro, do dono dela, injetado pelo GTM dele).

O init do dono **vem capturado no DOM** e precisa sair da cópia: os dois usam o
mesmo `window.dashfacil` e o mesmo `id="dashfacil-js"`, e **dois `init` na mesma
página nunca foi testado**. Na cópia entra um só, declarado no `<head>`.

Conferir pelo efeito, nunca pelo código estar lá:
`performance.getEntriesByType('resource')` tem que mostrar
`server.dashfacil.com/capture-page-view`.

### 10.4 O que conferir antes de dizer que a cópia está pronta

| Checagem | Como |
|---|---|
| CSS carregou | `getComputedStyle(h1).fontSize` bate com o original |
| caminho do CSS | **absoluto** (`/assets/...`): relativo quebra em subpasta |
| acordeão | abre, e `painéis vazios == 0` |
| origem | `a[href*=sck]` igual ao número de CTAs |
| WhatsApp | todos os `wa.me` com `%E2%80%8B` ou `%E2%80%8C` |
| Dash | `capture-page-view` na aba de rede |
| Meta | `fbq.instance.pixelsByID` com o pixel das campanhas |
| texto | diferença de linha só em `text-transform` (o `innerText` devolve em caixa alta o que o HTML tem em caixa baixa — isso não é texto faltando) |

---

## 11. Cópia fiel de WordPress (Elementor + LiteSpeed) servida no próprio domínio — *VARIAÇÃO ISOLADA (um segundo cliente, 17 páginas)*

> ⚠️ **Fora da base deste arquivo.** É um segundo cliente da casa, e outro método: o
> caso-base foi **reconstruído** (§6); aqui a página é **copiada como o site entrega**.

**Quando cabe copiar em vez de reconstruir:** página sem formulário que grave no WordPress. O popup de
uma das páginas tem formulário, mas é iframe do Full Funnels e funciona em qualquer domínio. Com
formulário do Elementor, a cópia perde o envio, e aí vale o §6.

**Como serve:** o domínio do cliente já estava na Cloudflare, na conta da casa, e o token da API cria
rota de Worker na zona (DNS ele não enxerga). Um Worker entra só nas rotas dos slugs copiados e entrega
o HTML do Pages. O resto do site nunca passa por ele. O endereço não muda, então bio, Hotmart (upsell e
obrigado) e UTM seguem iguais. Desligar a rota devolve o WordPress na hora.
- **Os arquivos saem do `*.pages.dev`, não do Worker.** Servida pelo Worker, cada imagem/CSS/JS
  (40 a 160 por página) contaria no limite de 100 mil requisições/dia do Free. O HTML aponta
  `https://<projeto>.pages.dev/wp-content/...`, e o `_headers` põe `Access-Control-Allow-Origin: *`
  em `/wp-content/*` (fonte de outro domínio não carrega sem isso). Medido no domínio real: 0 arquivo
  vindo do WordPress, 0 fonte com erro.
- **Uma rota exata por slug** (`/<slug>` e `/<slug>/*`). Com `/<slug>*`, `/guia*` pegaria também a
  `/guia-bio`, e desligar uma não desligaria a outra.
- Rota com `request_limit_fail_open: true`: estourou o limite, passa pro WordPress em vez de bloquear.
- **A prévia precisa do deploy principal:** o HTML busca os arquivos no endereço principal, então a
  prévia de um projeto sem deploy em `main` abre sem nada.
- **Rota nova leva alguns segundos pra valer em todo lugar.** Na troca, 16 das 17 responderam
  pela cópia na leitura logo depois de criar, e uma ainda veio do WordPress. Segundos depois,
  3 de 3 vieram pela cópia. Ler de volta de novo antes de concluir que a rota falhou.
- **Lançamento que acabou fica guardado, não publicado:** o HTML vai pra uma pasta `arquivo/<slug>/`,
  que não sobe no deploy (sem página pública com pixel disparando). Página fechada por 301 do
  Redirection é copiada pela original, com `?ver=1`. Pra voltar com uma delas: mover a pasta pra `site/`,
  pôr o slug na lista de slugs do Worker, publicar e ligar a rota.

**Quatro armadilhas, todas medidas:**
1. **Modo visitante do LiteSpeed.** A 1ª visita recebe uma versão com os scripts atrasados até a pessoa
   mexer na página, e o navegador recarrega depois de um POST no `guest.vary.php`. Copiar essa versão
   quebrou script (`wp is not defined`) e o redirect do cronômetro. Conserto: fazer o POST antes (com
   `Origin`/`Referer`, senão o firewall dá 406), guardar o cookie `_lscache_vary` e copiar com ele. A
   cópia tem que recusar página que ainda vier com `litespeed_load_delayed`.
2. **O Elementor carrega script sob demanda.** São 69 pedaços (`<nome>.<hash>.bundle.min.js`, os nomes
   estão no runtime do webpack) e 6 bibliotecas do `AssetsLoader` (`lib/dialog`, `swiper`, `share-link`,
   CSS de lightbox e dialog). Nada disso aparece no HTML. Sem o `dialog.min.js`, o popup não abria. Na
   casa, um script tira os nomes dos JS baixados e tenta baixar cada um nos dois plugins (Elementor e Pro).
3. **O redirect do cronômetro vencido exige `http`.** O `countdown.*.bundle.min.js` faz
   `t.redirect_url.startsWith("http")&&(window.location.href=t.redirect_url)`. Trocar por caminho
   relativo matou o redirect em silêncio. URL dentro do JSON escapado do Elementor fica absoluta.
4. **Firewall da hospedagem:** rajada de GET leva 406 (14 de 41 páginas no primeiro inventário).
   Pausa de 1,2 s entre pedidos, com espera crescente.

**Conferir contra o original antes de culpar a cópia.** Dois "defeitos" da cópia eram do original:
- o erro de CORS do GTM server-side (a primeira leitura disse que ele só aceitava o domínio do cliente;
  dá o mesmo erro no WordPress);
- o 404 da `visitorapi`.

Só um era da cópia de verdade: o redirect da armadilha 3. Regra: todo achado na cópia roda do mesmo jeito
no original, no mesmo navegador, antes de virar correção.

⚠️ **No navegador embutido do Claude, o que depende de `IntersectionObserver` só dispara depois de rolar.**
O lazy load do LiteSpeed (`data-lazyloaded`, a imagem fica num gif cinza de 1 px) e as animações de
entrada do Elementor (`elementor-invisible`) ficaram parados em 4–10 s sem rolagem, **no original e na
cópia**. Rolando até o fim e voltando, as 6 imagens de uma das páginas passaram a `loaded` e a logo do
popup apareceu. Antes de comparar, os dois lados precisam passar pela mesma sequência: carregar, rolar até
o fim, voltar, esperar 2 s. Página curta, que não rola (a bio), fica com as imagens cinza no painel pra
sempre. *Medido: a faixa dos upsells, a logo do popup e os banners da bio pareceram defeito e eram o
teste. Num Chrome normal (captura headless e a conferência rolando do §9) tudo aparece ao abrir. Pra
julgar se uma página está quebrada, a palavra final é do Chrome normal, não do painel do app.*

**O custo operacional:** com a rota ligada, editar no Elementor não muda a página no ar. Edição vai pra
cópia: refazer aquele slug, prévia, deploy.

### 11.1 Página nova no projeto do segundo cliente (inscrição de uma Black) — *VARIAÇÃO ISOLADA*

- **Formulário da página, não Tally na página.** O `rastreio.js` do Dash Fácil conta o lead lendo os campos
  do formulário da própria página no envio: varre os `input` (e-mail e telefone por heurística) e manda
  `Lead`. Medido no script. Pesquisa do Tally embutida na página de inscrição fica num
  iframe de outro domínio, e o Dash não enxerga o cadastro. O desenho que segue a Black do caso-base:
  formulário em HTML → `/api/inscrever` → obrigado com o Tally.
- **O obrigado tira nome, e-mail e WhatsApp da URL antes do GTM** (`history.replaceState` num script antes
  do snippet) e repassa pro Tally com os nomes dos campos ocultos dele. Antes de tirar, conferir que nada
  lê esses parâmetros. No segundo cliente: o Dash só lê `sck`, `gclid` e `fbclid` da URL, e o GTM do
  cliente não tinha variável de URL. É o conserto que ficou pendente no §7 ("E-mail na URL vai pra Meta").
- **Hotmart Send não recebe cadastro de fora.** Não há API pública de contato (procurado na época;
  conferir, a plataforma muda). A automação dispara por tag, e a tag entra por formulário do próprio
  Send, criado depois da tag. Por isso, no dia seguinte, a Black do segundo cliente passou a mandar o
  lead por **webhook** pro app de CRM de um parceiro.
- **Webhook de app de terceiro: gravar primeiro, mandar com prazo, reenviar depois.** A Function de
  inscrição manda com prazo de 8 s e grava o lead no KV uma vez só, já com o resultado do envio (o KV
  grátis aceita 1.000 gravações por dia). Falhou ou demorou: a pessoa segue pro obrigado e um reenvio
  manda depois (na casa, um script). O primeiro envio de verdade deu **401** sem dizer o tipo de
  credencial (nem `WWW-Authenticate`). Não se adivinha nome de cabeçalho no app dos outros: a credencial
  entra como segredo do projeto quando o dono do app disser qual é. No app do parceiro era um cabeçalho
  próprio (`X-<nome>-Secret`), que só aparece na tela na hora de criar ou trocar o webhook (trocar muda
  o endereço junto). Corpo no formato do app: `event`, `id` (evita contar duas vezes, então o reenvio
  usa o mesmo), `email`/`phone`, `name` e `data` com o resto. Teste com nome "TESTE … pode apagar" e
  telefone que não existe (`(11) 0000-0000`), pra nenhuma automação do app mandar mensagem pra alguém de
  verdade.
- **Link curto no domínio do cliente, pelo mesmo Worker** (Black do segundo cliente). Um mapa de atalhos
  no código do Worker devolve 302 pra página com a UTM do canal (ex.: `/black` = bio do Instagram,
  `/black-yt` = live do YouTube). Cada atalho ganha a própria rota no Worker. Não depende de encurtador
  de terceiro, o link tem a marca do cliente, e trocar o destino é só mudar o mapa, sem cache preso (302
  com `no-store`). A UTM segue `sirius-scale/frameworks/trafego/nomenclatura.md` §3.7, e os links ficam
  na planilha do lançamento, na aba de links do evento.
- **Formulário de página servida pelo Worker posta direto no `*.pages.dev`.** No domínio do cliente,
  `/api/` cairia no WordPress, porque o Worker só atende os slugs. O `action` aponta pro `pages.dev`, e a
  Function redireciona pro obrigado no domínio do cliente (`SITE_URL`). Assim o Worker que serve as
  páginas antigas não ganha código novo.
- **Lead da Meta pelo GTM do cliente.** O container do segundo cliente tinha um gatilho pra página com
  "obrigado" no endereço, então o obrigado novo não dispara `Lead` na mão (contaria em dobro). O
  container é público (`gtm.js?id=`) e dá pra ler pixels, projeto do Dash e gatilhos sem pedir a ninguém.
