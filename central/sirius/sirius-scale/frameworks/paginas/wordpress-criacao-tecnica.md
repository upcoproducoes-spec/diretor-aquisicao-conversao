# WordPress — armadilhas técnicas de escrita via REST API

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma
> **Alcance:** UNIVERSAL no que é mecânica da REST API do WordPress (auth,
> endpoint, formato de payload, o que quebra) — vale pra qualquer site de
> qualquer cliente.
> **Do caso:** o inventário de ambiente (tema, plugins, IDs de página, URL) é
> do site do caso-base (um expert de educação). Em site novo, refazer o
> levantamento — não presumir que o ambiente é igual.
> **Fato de plataforma:** versão de plugin, tela de configuração e
> comportamento de cache são os da época do levantamento. WordPress e plugin
> mudam: conferir antes de confiar.

Mesmo papel que `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md` e
`sirius-scale/frameworks/trafego/google-criacao-tecnica.md`: consultar **antes**
de montar código que lê ou escreve no WordPress, pra não repetir tentativa que
já falhou.

Site de referência: o WordPress do caso-base, levantado na primeira conexão da
automação.

---

## Ambiente do site (no levantamento)

| Item | Valor |
|---|---|
| Hospedagem | hospedagem brasileira compartilhada, com firewall próprio (armadilha 2) |
| Servidor | LiteSpeed + PHP (versão da época, conferir no painel) |
| Tema | Hello Elementor (versão da época, conferir no painel) |
| Builder | Elementor e Elementor Pro (versão da época, conferir no painel) |
| Caminho do `.htaccess` | `/home/<usuário>/public_html/.htaccess` |

---

## Armadilha 1 — o header `Authorization` não chega no PHP

**Sintoma:** toda chamada autenticada volta `401 rest_not_logged_in`
("Você não está logado neste momento"), inclusive com senha correta.

**Diagnóstico que separa header de senha errada:** repetir a chamada com uma
credencial propositalmente falsa. Se o erro for **idêntico**, o header está
sendo descartado; se a senha estivesse errada, o WordPress responderia
`invalid_username` / `incorrect_password`. Sem esse teste, se perde tempo
gerando senha nova atrás de senha nova.

**Causa:** em LiteSpeed/CGI o PHP não popula `PHP_AUTH_USER` / `PHP_AUTH_PW`,
que é de onde o WordPress lê Basic Auth.

**Correção aplicada (PADRÃO CONSISTENTE — é o comportamento padrão do
servidor, não uma variação deste site):** snippet PHP via WPCode, rodando em
`plugins_loaded` com prioridade 1, que reconstrói `PHP_AUTH_USER`/`PHP_AUTH_PW`
a partir de `HTTP_AUTHORIZATION` ou `REDIRECT_HTTP_AUTHORIZATION`.

Alternativa equivalente, se houver acesso ao `.htaccess` (gerenciador de
arquivos do painel — **o LiteSpeed Cache v7.9 só mostra o arquivo, não edita
mais**):

```apache
CGIPassAuth On
<IfModule mod_rewrite.c>
RewriteEngine On
RewriteCond %{HTTP:Authorization} ^(.*)
RewriteRule .* - [E=HTTP_AUTHORIZATION:%1]
</IfModule>
```

## Armadilha 2 — o firewall bane o IP por rajada de chamadas

**Sintoma:** conexão morre no aperto de mão TLS (`Connection reset by peer`,
curl exit 35, HTTP 000) — **inclusive na homepage, sem autenticação**. Parece
site fora do ar, não parece bloqueio.

**Causa:** o anti-brute-force da hospedagem lê várias requisições seguidas em
`/wp-json/` com header de autenticação como ataque, e bane o IP de origem.

**Duração observada:** ~4 minutos, liberação automática. Não precisou de
chamado no suporte.

**Regra dura:** todo script de WordPress segue o mesmo padrão de quem chama API
com limite (o da Meta é o exemplo clássico) — **pausa mínima de 3s entre
chamadas**, sessão HTTP reaproveitada, backoff crescente em falha de conexão.
Nunca loop de chamada por página.

## Armadilha 3 — o LiteSpeed cacheia as respostas da API

`/wp-json/` responde com `x-litespeed-cache: hit`. Leitura devolve dado velho
e alteração publicada parece "não ter pegado".

**Correção:** LiteSpeed Cache → Cache → Excludes → "Do Not Cache URIs" →
`/wp-json`. E, depois de toda publicação, limpar o cache da URL alterada.

## Armadilha 4 — Python antigo não fecha TLS com o servidor

O ambiente virtual do projeto da casa rodava Python 3.9 com **LibreSSL 2.8.3**,
que falha o handshake contra esse servidor. Um Python instalado à parte
(`/usr/local/bin/python3`, 3.14 com OpenSSL 3.5.7) funciona, **mas não traz
CA bundle próprio** — precisa apontar `ssl.create_default_context(cafile=
"/etc/ssl/cert.pem")`, senão dá `CERTIFICATE_VERIFY_FAILED`.

---

## Como a página entra sem passar pelo Elementor

**Achado que destrava a automação (VARIAÇÃO ISOLADA — um site, um cliente):**
**todas as páginas do site usam o template `elementor_canvas`**, sem exceção.
Esse template é tela em branco — não renderiza header nem footer do tema.

Ou seja, a estrutura que o time já usa é a mesma que o padrão de entrega de
página da casa pede (HTML standalone: um arquivo, CSS no `<style>`, como o
agente `webdesigner` entrega). Não há atrito de formato: basta criar a página
com `"template": "elementor_canvas"` e mandar o HTML no campo de conteúdo.

**Cuidado obrigatório:** o WordPress roda `wpautop` no conteúdo e injeta
`<p>`/`<br>` no meio do HTML cru, quebrando o layout. Para evitar, envolver o
HTML em bloco Gutenberg de HTML puro, que não sofre o filtro:

```
<!-- wp:html -->
...o HTML da página...
<!-- /wp:html -->
```

**Nunca** escrever HTML no `content` de uma página **já construída no
Elementor**: ela tem `_elementor_edit_mode = builder` e o Elementor
sobrescreve o conteúdo com o JSON dele na hora de renderizar — a alteração
some sem erro nenhum. Página gerada por nós nasce fora do builder e fica
fora dele.

---

## Duplicar página do Elementor pelo REST

`_elementor_data` **está exposto no REST com `context=edit`** (leitura e
escrita) — então duplicar página de builder pelo script sai fiel, com layout,
formulário e CSS. Testado: a cópia de uma página de inscrição saiu com
46.528/46.528 caracteres idênticos.

Copiar estas chaves de meta, além de title/slug/status/template/content:
`_elementor_data`, `_elementor_edit_mode`, `_elementor_template_type`,
`_elementor_page_settings`, `_elementor_conditions`.

Sem elas, a cópia sai como casca vazia.

**Detectar página de builder — o teste certo:** `_elementor_edit_mode ==
"builder"`. O plugin registra as chaves `_elementor_*` em **toda** página,
inclusive nas que nunca passaram pelo builder (valores vazios). Procurar a
palavra "elementor" no meta dá falso positivo em página nossa — erro cometido
e corrigido no primeiro dia.

Sem autenticação, a API devolve só `footnotes` — a chave de API do Mailchimp
guardada no `_elementor_data` **não** vaza pra visitante. Conferido.

---

## Página B (variante visual) sem quebrar o formulário

**Regra dura descoberta no primeiro dia:** não reconstruir em HTML puro uma
página que tem formulário do Elementor. O envio depende de um **nonce**
gerado pelo WordPress por página, que expira em horas — uma página estática
enviaria lead hoje e falharia amanhã, **em silêncio**. Em lançamento ativo
isso é perda de lead sem alarme.

Caminho certo: **duplicar a página no Elementor e trocar só a pele**, via
`_elementor_page_settings.custom_css`. O formulário fica intocado (mesmo
`form_id`, mesmas 4 ações, mesma tag do Mailchimp) e a variação é 100%
reversível — basta apagar o CSS.

### ✅ RESOLVIDO — o "Cache de elementos" do Elementor engolia toda escrita por API

**Pré-requisito de toda automação de página neste site:** Elementor →
Configurações → Desempenho → **"Cache de elementos" DESATIVADO**. Desligado no
mesmo dia. Se alguém religar, tudo que a API gravar volta a não aparecer —
e sem erro nenhum, o que é a parte perigosa.

Com o cache ligado, a mesma escrita salvava (a leitura confirmava) e **não
renderizava**. Desligado, o widget de CSS passou a renderizar na primeira
tentativa, com o `noindex` junto. Diagnóstico abaixo fica registrado porque o
sintoma é enganoso — parece dado não salvo, e não é.



Na página B, **nada gravado por REST depois da criação apareceu na página
renderizada**, embora a leitura confirmasse tudo salvo:

| Tentativa | Salvou? | Renderizou? |
|---|---|---|
| `custom_css` em `_elementor_page_settings` | sim (9.052 car.) | não |
| widget `html` no `_elementor_data`, id `meutema01` | sim | não |
| mesmo widget, id `<id>` (formato hex do Elementor) | sim | não |

O layout copiado **aparece** — mas ele foi gravado no mesmo POST que criou a
página. Tudo que veio em chamada posterior é ignorado. Os `data-id` do HTML
renderizado pulam direto de um `<id>` pro seguinte, sem o widget injetado.

**Hipótese (não confirmada):** o Elementor guarda o HTML renderizado do
documento em cache (`_elementor_element_cache`, além do cache de CSS) e a
escrita por REST não dispara a invalidação — que só acontece no salvamento
pelo editor dele. Nenhuma das duas chaves de cache está exposta no REST, e
não há rota de regeneração.

**Contornos, do melhor pro pior:**

1. **Desligar o cache de elementos** em Elementor → Configurações →
   Desempenho. Ajuste único que, se a hipótese estiver certa, destrava toda a
   automação futura. **Testar isso antes de qualquer outra coisa.**
2. Abrir a página no editor do Elementor e clicar em Atualizar — funciona,
   mas é manual a cada alteração, o que derruba o propósito.
3. Servir o CSS por fora do Elementor (snippet no plugin Code Snippets, que
   expõe `POST /code-snippets/v1/snippets`). Resolve CSS, não resolve
   alteração de layout.

### ⚠️ `custom_css` gravado por REST NÃO tem efeito

Erro cometido no primeiro dia. Gravar CSS em
`_elementor_page_settings.custom_css` pela API **salva o valor** (volta certo
na leitura) **mas não aparece na página**. O Elementor gera o CSS uma vez e
guarda em cache (`_elementor_css`); a escrita por REST não dispara a
invalidação, que só acontece no salvamento pelo editor dele. E não existe
rota REST pra regerar — conferido em `/wp-json/`: os namespaces
`elementor-ai`, `elementor-one` e `elementor-hello-elementor` não expõem
nada disso, e o LiteSpeed também não expõe purge.

Neste site o CSS do Elementor vem **embutido no HTML**, não em
`/uploads/elementor/css/post-<id>.css` (esse caminho responde 403 de
qualquer forma) — então não dá nem pra conferir por fora se foi gerado.

**Solução que funciona por API:** injetar o CSS como **widget `html` dentro
do `_elementor_data`**, não nas configurações. Vira conteúdo do documento, e
conteúdo o Elementor renderiza sempre, sem passar pelo cache de CSS.

```python
widget = {"id": "meutema01", "elType": "widget", "widgetType": "html",
          "settings": {"html": "<style>…</style>",
                       "_css_classes": "meu-css-holder"},
          "elements": []}
dados[0].setdefault("elements", []).insert(0, widget)   # cedo na página
```

Entrar como primeiro filho do primeiro container faz o estilo aplicar antes
da pintura das seções de baixo. A classe `meu-css-holder` (com
`display:none`) esconde o invólucro do widget. Prefixar o `id` com algo
próprio (`meutema…`) deixa a operação idempotente: dá pra remover e reinjetar
sem duplicar.

### Armadilhas de CSS ao clarear um tema escuro do Elementor

1. **A sobreposição de fundo mora num `::before`, não no container.** O
   `background_overlay` (um azul-escuro, no caso) é pintado em
   `.elementor-element-<id>::before`. Procurar fundo escuro subindo a
   linhagem do elemento **não acha** — e o CSS que mira só o container não
   surte efeito. Neutralizar explicitamente o `::before`.
2. **`.elementor-invisible` com `visibility:hidden`** é animação de entrada:
   o JS do Elementor remove ao rolar. Em cópia local (sem o JS dele) o
   elemento some pra sempre — parece bug de tema e não é. Só afeta prévia.
3. **Fundo de container às vezes é conteúdo.** Aqui o retrato do expert
   era `background_image` de um container. Apagar "as artes escuras"
   em bloco abriu um buraco branco na bio. Conferir imagem por imagem.
4. **Botão avulso é `<a class="elementor-button-link">` e o tema zera o fundo
   dele** (`#61CE7000`). Seletor `.elementor-button` sozinho não vence:
   precisa de `.elementor-widget-button .elementor-button`.
5. **O FAQ tem fundo no próprio `.elementor-tab-title`**, não no
   `.elementor-toggle-item`.
6. **Logo branco some no claro.** Recolorir o arquivo (script PIL: pixel
   saturado → azul da marca; dessaturado → navy) e trocar por
   `img[src*="<nome>"] { content: url(...) }`.

### Como testar variação sem publicar

Baixar o HTML público da página A, injetar `<base href>` + o CSS novo num
arquivo local e servir com `python3 -m http.server`. CSS, fontes e imagens
resolvem contra o site real. **Confiar no DOM (`getComputedStyle`,
`elementFromPoint`), não no screenshot** — o screenshot do navegador
embutido atrasa frames e já apontou "erro" onde o DOM estava certo.

---

## Arquitetura do formulário de captação (Elementor Form)

Lido da página de inscrição do lançamento em curso no levantamento.
**VARIAÇÃO ISOLADA** — um lançamento, um cliente.

**Campos:** nome, e-mail (obrigatório), DDD+telefone (obrigatório) e 6 campos
ocultos de UTM (`utm_source`, `utm_campaign`, `utm_term`, `utm_content`,
`utm_medium`, `utm_id`).

**No envio, dispara 4 ações ao mesmo tempo:**

| Ação | Destino |
|---|---|
| `save-to-database` | Banco do WordPress (Elementor → Envios) |
| `email` | uma caixa de administração do domínio do expert |
| `redirect` | `/obrigado-<lançamento>`, com nome/e-mail/telefone na query string |
| `mailchimp` | a lista do expert, tag `LC-<MODELO>-<MÊS>/<ANO>-INSCRITO` |

**O CRM é o Mailchimp** — não existe ferramenta separada. Mapeamento:
e-mail → Email, nome → Nome, telefone → Telefone. Double opt-in desligado
(certo pra lançamento: opt-in duplo derruba taxa de entrada na lista).

**Os UTMs não vão pro Mailchimp.** Ficam só no banco do WordPress e no e-mail
de notificação. Segmentar e-mail por origem de tráfego exige exportar do WP e
cruzar na mão.

**Padrão de tag:** `LC-<MODELO>-<MÊS>/<ANO>-INSCRITO`. Ao duplicar página pra
lançamento novo, **trocar a tag** — senão o lançamento novo contamina a lista
do anterior.

---

## Nomenclatura das páginas (lida do site, não inventada)

Padrão observado: `<MODELO> – <PEÇA> – <MÊS/ANO>`, com slug
`<peca>-<modelo><mes><ano>`.

- Modelos: dois, o lançamento gratuito e o **LPSG** (ver
  `sirius-scale/frameworks/lancamentos/lpsg.md`)
- Peças: INSCRIÇÃO, OBRIGADO, LIVES, AULA 1–4, CARTA, GRUPO VIP, PV, OB
- Sufixo de edição: o código do modelo + o mês abreviado + o ano com 2 dígitos
  (`-<modelo><mês><aa>`)

No levantamento, o lançamento em andamento tinha inscrição, lives e obrigado
publicados nesse padrão.
