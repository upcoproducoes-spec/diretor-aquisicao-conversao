# Meta Marketing API — notas técnicas de criação/escrita

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma
> **Alcance:** UNIVERSAL — comportamento da API da Meta, igual pra qualquer
> cliente e qualquer negócio. Não tem eixo de força: aqui não existe "padrão que
> se repete", existe campo que funciona ou quebra. Campo descontinuado é
> descontinuado pra todo mundo. (As poucas seções que registram processo, ou uma
> ocorrência só, levam rótulo próprio, como VARIAÇÃO ISOLADA.)

> Diferente de `sirius-scale/frameworks/trafego/_metodologia.md` (que é sobre
> analisar dado existente), este arquivo é sobre **construir**
> campanha/conjunto/anúncio — armadilha técnica real encontrada, não teoria.
> Medido na Graph API v26 e na interface do Gerenciador da mesma época. A Meta
> muda campo e tela sem aviso: se algo daqui não bater com o que vocês veem,
> confira na plataforma antes de seguir. Armadilha nova que vocês acharem vai
> pra `frameworks-da-casa/`.

> **Como usar, pelos dois caminhos.** Pela regra de escrita
> (`sirius-scale/REGRAS.md` §6), o Claude lê a conta e, com a Meta conectada,
> monta campanha, conjunto e anúncio **pausados**; quem ativa e mexe em verba é a
> pessoa dona da conta, no Gerenciador. Por isso cada armadilha traz **"O que
> conferir"**: o que olhar na tela antes de ativar e na leitura de volta. Os nomes
> de campo, os códigos de erro e as receitas de API ficam como estão: servem pro
> Claude ler a conta pelo conector, montar pausado chamando cada coisa pelo nome
> certo e ler de volta o que montou (as travas do §6: pedido escrito, resumo
> confirmado, teto combinado, leitura de volta).

## RECEITA — criar uma campanha de captação do zero, na ordem certa

> **Esta seção é o índice de uso do arquivo.** As outras são armadilhas isoladas,
> na ordem em que foram descobertas; esta é a ordem em que as coisas acontecem.
> Executada de verdade numa campanha de captação do caso-base.

⚠️ **Escreva estágio por estágio.** `execution_options: ['validate_only']` só cobre
o estágio que não depende de ID novo — conjunto, criativo e anúncio referenciam
IDs que ainda não existem. Estágio que falha deixa os anteriores criados; quem
cria tem que continuar de onde parou, não recriar. (À mão vale o mesmo: se o
Gerenciador recusar o anúncio, a campanha e o conjunto já ficaram criados;
continue deles, não duplique.)

| # | Passo | Não esqueça | O que conferir à mão, no Gerenciador | Onde |
|---|---|---|---|---|
| 0 | **Ler campanha + conjunto + criativo da referência** | Nunca do zero — a plataforma preenche o resto com default | Duplicar a campanha que já entrega bem e comparar campo a campo com a original | "Campanha nova se cria DUPLICANDO" |
| 1 | **Vídeo na conta?** | `create_ad_video(params={"source": caminho})`. Conferir `video_status: ready` antes de seguir | O vídeo terminou de processar antes de montar o anúncio | abaixo |
| 2 | `Campaign` | `objective`, `is_adset_budget_sharing_enabled`, `status=PAUSED`. `bid_strategy` mora no mesmo nível do ORÇAMENTO | Objetivo; orçamento na campanha ou no conjunto, decidido antes (diário ↔ total não muda depois); lance no mesmo nível do orçamento; nasce desligada | "`bid_strategy` mora…", "`is_adset_budget_sharing_enabled`…", "Anúncio de janela curta…" |
| 3 | `AdSet` | `promoted_object` (pixel + `custom_event_type`), `optimization_goal`, `billing_event`. **Remontar** o `targeting`, nunca copiar o lido | Pixel e evento de conversão iguais aos da referência; público, exclusões e Advantage+ conferidos (`sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.3) | "Editar `targeting`…" |
| 4 | `AdCreative` | `object_story_spec.video_data` com **`image_url` da miniatura** — sem ela a criação falha | Miniatura de cada vídeo conferida | "Criativo de vídeo exige miniatura" |
| 4b | **Formato do anúncio** | 1 imagem por criativo no DEGREES_OF_FREEDOM; N imagens = anúncios irmãos no mesmo conjunto; carrossel = `child_attachments` com 1 texto. Conferir aqui ANTES de recomendar formato | O mesmo critério: N artes = N anúncios irmãos, cada um com nome próprio | "Anúncio de várias versões…", "Carrossel por API…" |
| 5 | `Ad` | Aponta pro `creative_id` | Nome do anúncio no padrão (`sirius-scale/frameworks/trafego/nomenclatura.md` §1) e UTM com as macros (§3 de lá) | — |
| 6 | **Ativar** | Passo separado, campanha **e** conjunto | Feito por vocês, no Gerenciador, depois do preflight. O Claude não ativa | `sirius-scale/REGRAS.md` §6 |
| — | **Rodada que não vai rodar** | Arquivar com trava (pausada, gasto zero, nome do registro); voltar do arquivado não foi medido | Arquivar só o que está pausado e com gasto zero na vida inteira | "Rodada trocada antes de ligar…" |

**A UTM mora no criativo (passos 4 e 5) — *UNIVERSAL*:**
- Os parâmetros de URL ficam no criativo, num lugar só: no `url_tags` ou no próprio link. Nos dois ao mesmo tempo, a URL
  leva dois valores pro mesmo parâmetro, e cada ferramenta pega um: num caso medido, o Dash leu a do `url_tags` e o
  formulário da pesquisa gravou a do link (*VARIAÇÃO ISOLADA*, 1 conta).
- Reaproveitar um `creative_id` antigo num anúncio novo traz a UTM antiga junto: nome de outro lançamento, ou `{{ad.id}}`
  no lugar do nome. Com id na UTM, o Dash não liga o lead a criativo nenhum (num caso medido, mais de mil leads ficaram
  sem criativo).
- **Criativo novo montado com o link de um criativo antigo também traz a UTM antiga** (*VARIAÇÃO ISOLADA*). Ela mora
  no link, e o `url_tags` novo não a tira. Ao copiar o link, tirar os `utm_*` dele.
- `url_tags` não se edita em criativo que já existe (subcode 1815573).
- Pra reaproveitar peça: criativo novo com o mesmo vídeo ou post, o link sem `utm_*` e o `url_tags` do padrão
  (`nomenclatura.md` §3).
- **Conferir nos dois lugares.** O conector da Meta não devolve o `url_tags`, mas devolve o link do criativo de vídeo
  (`link_url`). Procurar `{{campaign.id}}`, `{{adset.id}}` e `{{ad.id}}` no link; quando o `url_tags` não dá pra ler, a
  prova é a tabela de UTM do Dash.
- **Anúncio de tráfego ou alcance leva o pixel no `tracking_specs`** (seção "Anúncio de tráfego criado por API sai sem o
  pixel", no fim do arquivo).

**Público de site no conjunto (passo 3), *UNIVERSAL*:** ler a regra de cada público de site que entra ou sai do conjunto
e conferir que o valor da URL aparece na URL de destino de verdade, com ou sem www (seção "A forma da regra de público de
site que a v26 aceita").
**Erro que esta ordem teria evitado:** os 5 criativos falharam de uma vez
por falta de miniatura (passo 4), depois de os vídeos já estarem subidos e o
conjunto criado.

### O passo 1 por extenso — vídeo que ainda não está na conta

```python
v = acc.create_ad_video(params={"source": caminho_mp4, "title": os.path.basename(caminho_mp4)})
# depois, antes de criar o criativo:
st = AdVideo(v["id"]).api_get(fields=["status"]).export_all_data()["status"]
# esperar video_status == "ready" (upload, processing e publishing completos)
```

⚠️ `get_ad_videos()` com `limit` alto devolve **HTTP 500** ("Please reduce the
amount of data you're asking for"). Com algumas centenas de vídeos na conta,
`limit=400` estourou e `limit=25` passou. Pra achar vídeo existente, pagine pequeno.

📌 **`video_status: ready` não basta pro criativo** — as duas coisas são
independentes. Vídeo pronto e publicado ainda exige a miniatura explícita; ver a
seção da miniatura.

## Imagem diferente por posicionamento, no mesmo anúncio, com múltiplas variações de texto

**O recurso existe e é usado na conta do caso-base** — confirmado na própria
interface do Gerenciador de Anúncios: dentro de "Mídia" de um anúncio, dá
pra associar imagem diferente por grupo de posicionamento ("Feeds, Anúncios
in-stream para reels" / "Stories, Status e Reels..." / "Coluna da direita...",
cada um com miniatura própria). É o recurso oficial "Placement Asset
Customization" da Meta.

**O que conferir à mão:** em "Mídia", cada grupo de posicionamento com a arte
certa (a vertical 9:16 em Stories e Reels, a de feed nos feeds), e a prévia de
cada posicionamento olhada antes de publicar.

**Tentativa via API que NÃO funcionou, com erro exato:**

1. `optimization_type=PLACEMENT` (roteamento de imagem por posicionamento)
   com 2 `asset_customization_rules` (imagem 1:1 vs 9:16) + os 6 `bodies`
   (variações de texto) **sem `adlabels`**:
   ```
   error_subcode: 1885878
   error_user_msg: "Vários ativos bodies não podem ser aplicados à regra
   nº 1 (número de prioridade, se especificado, ou o índice da regra) no
   feed de ativos do anúncio."
   ```
2. `optimization_type=DEGREES_OF_FREEDOM` (o modo que permite múltiplas
   variações de texto livres, mesmo modo do anúncio original em vídeo) —
   **isso não é questão de rótulo**: esse modo exige que mídia+link fiquem
   em `object_story_spec.link_data`, não em `asset_feed_spec.images`, e por
   isso só aceita 1 imagem fixa por criativo, ponto.

**O que os exemplos reais já existentes na conta mostram funcionando**
(3 criativos encontrados usando o recurso de fato): cada asset (`bodies`,
`titles`, `descriptions`, `link_urls`, `images`) leva `adlabels` com o(s) id(s)
de label que atende, e cada `asset_customization_rules` referencia esses ids
via `body_label`/`title_label`/`description_label`/`link_url_label`/
`image_label`. **Mas em nenhum dos 3 exemplos reais havia mais de 1
variação de texto por regra** — sempre um único body/title/description
compartilhado entre as regras (mesmo texto nos dois posicionamentos),
nunca várias variações candidatas sob o mesmo rótulo.

**Pergunta em aberto, não testada (a investigação parou aqui — a operação
resolveu manual na UI antes):** dá pra rotular os 6 `bodies` originais
todos com os **mesmos dois label ids** das duas regras (testando se a API
aceita um "pool" de várias variações de texto candidatas sob 1 rótulo), ou
cada rótulo só aceita 1 conteúdo fixo (e nesse caso a combinação "várias
variações de texto" + "imagem por posicionamento" simplesmente não é
possível via API, só pela UI, que talvez tenha lógica de rotação diferente
por trás)? Não se sabe ainda.

**Enquanto isso não for testado até o fim:** se precisar dessa combinação
de novo, (a) testa primeiro a hipótese do "pool de labels" acima antes de
repetir as duas tentativas que já falharam; ou (b) monta pela própria
interface do Gerenciador de Anúncios, que comprovadamente suporta (foi
assim que se resolveu desta vez); ou (c) usa a alternativa já validada
via API — dois anúncios separados no mesmo conjunto, um por formato de
imagem, cada um com as variações de texto completas.

---

## `standard_enhancements` em `degrees_of_freedom_spec` foi descontinuado

**Observado no caso-base.** Ao criar criativo novo copiando a estrutura de um
criativo existente da própria conta, as 23 criações falharam de uma vez. O campo
copiado era:

```python
"degrees_of_freedom_spec": {
    "creative_features_spec": {
        "standard_enhancements": {"enroll_status": "OPT_OUT"}}}
```

Erro exato:

```
error_subcode: 3858504
error_user_title: "O criativo não deve incluir aprimoramentos padrão"
error_user_msg: "O recurso de inclusão do campo de aprimoramentos padrão no
criativo foi descontinuado. Defina recursos individuais."
```

**Solução:** omitir `degrees_of_freedom_spec` inteiro na criação. O criativo
sobe normal. Só passar o campo se for pra ligar/desligar um recurso
específico — e aí nomeando o recurso individual, nunca `standard_enhancements`.

⚠️ **A armadilha maior é de método, não de campo:** o criativo antigo da conta
*ainda tem* esse campo (foi criado quando era aceito). Copiar a estrutura de
um objeto existente não garante que ela ainda seja aceita na criação — a Meta
descontinua campo sem remover dos objetos antigos. Testar a criação de **um**
objeto antes de disparar o lote.

📌 **Consequência operacional:** troca de anúncios (criar os novos e tirar os
antigos) se faz em dois passos, e os antigos só saem se **todas** as criações
novas passaram. Sem essa trava, esse erro teria apagado 23 anúncios e deixado os
conjuntos vazios.

**O que conferir à mão:** suba e confira os anúncios novos antes de pausar ou
excluir os antigos. As melhorias automáticas do criativo se escolhem recurso por
recurso (é o "defina recursos individuais" do erro), não num pacote padrão.

---

## `generatepreviews` é a validação a seco da Meta (equivalente ao `validate_only`)

**Descoberto na montagem de um aquecimento do caso-base.**

A regra de escrita da casa pedia "criar 1 objeto de teste na Meta" como validação
prévia, porque se achava que a Meta não tinha um `validate_only` como o Google.
Tem coisa melhor: **`POST act_<id>/generatepreviews`** valida o
`object_story_spec` inteiro e devolve o preview renderizado **sem criar nada** na
conta.

```python
AdAccount(acc).get_generate_previews(params={
    "creative": {"object_story_spec": spec},
    "ad_format": "MOBILE_FEED_STANDARD"})
```

Passa pelas mesmas checagens da criação real (campo faltando, vídeo
inacessível, CTA inválido) e devolve `error_user_title` / `error_user_msg` em
português. Usar isto antes de qualquer lote, em vez de sujar a conta com
objeto de teste que depois precisa ser apagado.

⚠️ Ler o erro pelo `error_user_msg`, não pelo `message` genérico: o `message`
de topo vem como "Invalid parameter", que não diz nada.

⚠️ **Não valida imagem de `asset_feed_spec` — *VARIAÇÃO ISOLADA*.** Com o
criativo de imagem por posicionamento (regras de story + feed), o `generatepreviews`
**aceitou** um hash de imagem que não existe, em `MOBILE_FEED_STANDARD` e em
`INSTAGRAM_STORY`. O verificador que presta é o `create_ad` com
`execution_options: ["validate_only"]` num conjunto válido (não vencido): recusou o hash
inexistente ("Imagem não encontrada") e a mesma imagem nas duas regras ("duplicação de
valores de ativo"), aceitou o criativo bom com `{'id': None}`, e o conjunto ficou com o
mesmo número de anúncios antes e depois. Em conjunto **vencido** ele recusa pelo conjunto,
não pelo criativo. No caso-base, essa validação roda dentro do conjunto novo antes de
gravar cada anúncio.

**Pela API, a imagem por posicionamento num anúncio só funcionou na forma lida dos
criativos da conta que já usavam o recurso:**
`optimization_type: PLACEMENT`, `ad_formats: [AUTOMATIC_FORMAT]`, regra 1 com
`facebook_positions [story, facebook_reels]` e `instagram_positions [story, reels]` apontando
pra imagem 9:16, regra 2 só com a faixa de idade apontando pra 4:5, e **um** texto, título e
link por anúncio, cada um com os dois rótulos. Isso responde a pergunta aberta mais acima
pro caso de um texto só; vários textos por regra continuam não testados.

**O que conferir à mão:** a tela não tem validação a seco. O equivalente é montar
tudo desligado, olhar a prévia de cada posicionamento e só então ligar.

---

## Anúncio de janela curta (horas, não dias) — três recusas na mesma subida

**Medido numa peça "Começa hoje" de um LPSG do caso-base** (conjunto das 6h às 20h
do dia da primeira aula). *UNIVERSAL (regra da plataforma), 1 ocorrência.*

| Erro | O que significa | O que fazer |
|---|---|---|
| `1487793` "A programação da campanha é muito curta" | conjunto com orçamento **diário** precisa de pelo menos **24 h** entre `start_time` e `end_time` | janela menor que 24 h vai com orçamento **total** (`lifetime_budget` na campanha CBO) |
| `1487164` "Alteração do tipo de orçamento não permitida" | diário ↔ total **não muda depois de criada** (mandar `daily_budget: 0` junto também é recusado: "only one of daily budget or lifetime budget can be set") | decidir o tipo antes de criar; a campanha errada fica pausada e vazia (renomeada "(VAZIA, NAO USAR)") e sobe outra |
| `2446218` "Não há peças publicitárias suficientes" | `DEGREES_OF_FREEDOM` exige **algum** campo com mais de um ativo; 1 corpo + 1 título + 1 descrição é recusado | texto único vai em `link_data` (`message`, `name`, `description`) sem `asset_feed_spec` — ou na receita de imagem por posicionamento abaixo |

**Imagem por posicionamento com checkout direto:** a receita de imagem por
posicionamento (fim da seção do `generatepreviews`, acima) funcionou com link da
Hotmart que já tem `?off=…`: o link vai limpo em `link_urls` (só `off` e
`checkoutMode`) e o rastreio inteiro (`sck` e UTM com as macros
`{{campaign.name}}`…) em `url_tags` do criativo. Troca num anúncio que já existe:
`Ad.api_update(creative={"creative_id": novo})`, com leitura de volta das 2
imagens, 2 regras, texto, link e `url_tags` (e ver, mais abaixo, o anúncio de
vídeo que travou depois de uma troca de criativo).

**O que conferir à mão:** janela menor que 24 h vai com orçamento **total** (o
diário é recusado); o tipo de orçamento é escolhido antes de criar, porque não
muda depois; no anúncio, o link de destino limpo e o rastreio no campo de
parâmetros de URL; abrir a prévia e clicar pra ver que chega no checkout com a UTM.

---

## Impulsionar live gravada que está na PÁGINA (não na conta de anúncios)

**Caso-base, aquecimento de um lançamento.** As 10 lives de aquecimento foram
transmitidas na página e existem lá como vídeo — mas nada disso aparece pelos
caminhos óbvios. A sequência que funciona:

**1. O token de System User não enxerga vídeo de página.** `Page(id).get_videos()`
com o token do system user devolve **lista vazia** — sem erro, o que é pior que
erro. É preciso pegar o **Page Access Token** primeiro:

```python
pt = get(f"{PAGE_ID}", fields="access_token")["access_token"]
```

E aí `GET /{page-id}/videos?type=uploaded` com esse token. Sem `type=uploaded`
a lista também volta incompleta.

Permissões necessárias no system user: `pages_read_engagement` (+ o system user
precisa ter a **página adicionada como ativo** no Business Manager). Não passa
por App Review quando é página do próprio negócio.

**2. ⚠️ `post_id = 0` NÃO quer dizer que não há post — é uma pegadinha.**
Consultando `GET /{video_id}?fields=post_id`, as 10 lives voltaram todas com
`post_id = 0`. Conclusão errada tirada disso: "o vídeo foi carregado mas nunca
virou publicação, então só resta criativo novo". **Falso.** As 10 estavam
publicadas no feed normalmente, como "fez uma transmissão ao vivo", com reação e
compartilhamento — o Rodrigo desmentiu com print da tela.

O campo `post_id` simplesmente não é preenchido para vídeo de transmissão ao
vivo. Pra achar o post de verdade, cruzar pelo feed:

```python
GET /{page-id}/posts?fields=id,status_type,attachments{type,target,title}
# casar attachments.data[].target.id  ==  video_id
# o post aparece com status_type = "added_video"
```

O `id` que volta já é o `object_story_id` no formato `{page_id}_{post_id}` —
e, nestes casos, o post_id coincidiu com o próprio video_id nas 10 peças.

**Nunca concluir "não existe post" a partir de `post_id = 0`.** Confirmar pelo
feed, ou olhando a página. Com o `object_story_id` em mãos, o criativo é só:

```python
{"object_story_id": "<page_id>_<post_id>"}
```

Validado em MOBILE_FEED_STANDARD, INSTAGRAM_STANDARD e FACEBOOK_STORY_MOBILE.
Esse é o caminho que a interface chama de **"selecionar uma publicação
existente"** (aba Anúncios do Gerenciador), e é preferível a criar criativo
novo: o anúncio roda em cima do post que já tem prova social acumulada, em vez
de nascer zerado.

**O que conferir à mão:** no anúncio, a publicação existente escolhida (a live, no
feed da Página), e não um upload novo do mesmo vídeo, que nasce sem prova social.

⚠️ **Limitação de campo, não de post:** `likes.summary(true)` e
`comments.summary(true)` em `/posts` devolvem erro `(#10) requires
pages_read_engagement` **mesmo com o escopo concedido** — outros campos do
mesmo endpoint funcionam. Ou seja, dá pra achar o post e usá-lo, mas ler as
contagens de reação pela API pede liberação à parte. Contar pela tela.

**3. Se ainda assim for criar criativo novo, `video_data` exige miniatura
explícita.** (Só necessário quando não houver post — com `object_story_id` o
criativo já vem pronto do post e nada disso se aplica.) Sem ela:

```
error_subcode: 1443226
error_user_title: "Seu anúncio precisa de uma miniatura de vídeo"
error_user_msg: "Especifique image_hash ou image_url no campo video_data
de object_story_spec."
```

A miniatura sai do próprio vídeo, em `GET /{video_id}/thumbnails` (com o page
token) — pegar a que tem `is_preferred: true`, e passar a `uri` como
`image_url`. Vídeo de página não traz thumbnail automática pro criativo, mesmo
tendo uma no feed.

**4. Vídeo da página funciona na conta de anúncios** sem precisar re-upload,
desde que página e conta estejam no mesmo Business Manager e o system user
tenha `pages_manage_ads`. Confirmado por `generatepreviews`.

📌 **Dado bruto, com ressalva:** o campo `views` desses vídeos na Meta é uma
fração do YouTube — numa live, a Meta marcou menos de 2% das views que o YouTube
marcou; noutra, menos de 10%. Duas ressalvas antes de usar isso pra decidir algo:
(a) é esperado, porque o Facebook quase não entrega vídeo longo no orgânico;
(b) `views` de vídeo de live não é métrica comparável a view do YouTube, e as
contagens de reação nem puderam ser lidas pela API (ver limitação acima). Serve
pra dizer "não conte com alcance orgânico da Meta como ponto de partida" — não
serve pra concluir que a peça é fraca lá.

---

## `execution_options: ['validate_only']` também funciona na Meta

Complementa o `generatepreviews` (que valida *criativo*):
`validate_only` valida **campanha e conjunto** — objetivo, meta de otimização,
targeting, orçamento — e devolve `{'id': None}` sem criar nada.

```python
AdAccount(acc).create_campaign(params={..., "execution_options": ["validate_only"]})
AdAccount(acc).create_ad_set(params={...,  "execution_options": ["validate_only"]})
```

Juntando os dois, a Meta tem cobertura de validação a seco equivalente ao
`validate_only` do Google, e **não é mais preciso criar objeto de teste** pra
conferir estrutura antes de um lote.

⚠️ **Pegadinha ao validar conjunto:** ele exige um `campaign_id` real, e a
validação testa a compatibilidade meta-de-otimização × objetivo-da-campanha.
Validar um conjunto THRUPLAY contra uma campanha de captação
(`OUTCOME_LEADS`) devolve *"Você não pode usar a meta de desempenho
selecionada com seu objetivo da campanha"* — que é erro do **par**, não do
conjunto. Validar contra uma campanha do mesmo objetivo que a pretendida.

**O que conferir à mão:** a tela não tem esse modo; o equivalente é montar
desligado (`sirius-scale/REGRAS.md` §6) e ler o que o Gerenciador recusa na hora
de publicar. A mesma pegadinha aparece na tela: meta de desempenho que não
combina com o objetivo da campanha.

---

## `is_adset_budget_sharing_enabled` virou obrigatório na criação de campanha

**Descoberto na montagem de um aquecimento do caso-base**, pego pelo
`validate_only` antes de qualquer escrita.

Criar campanha sem orçamento no nível da campanha (ou seja, com o orçamento no
conjunto — o padrão daquela conta pra aquecimento) agora falha com:

```
error_user_msg: "É necessário especificar True ou False no campo
is_adset_budget_sharing_enabled se você não estiver usando o orçamento da
campanha."
```

**Solução:** passar `"is_adset_budget_sharing_enabled": False` na criação. Não
existe default — a Meta exige a escolha explícita.

📌 Mais um caso da armadilha já registrada acima: os criadores antigos da casa
não tinham esse campo (foram escritos quando não era exigido) e **rodariam com
erro hoje**. Reforça a regra de validar a seco antes de qualquer lote, em vez de
confiar que o que funcionou antes ainda funciona.

**O que conferir à mão:** com orçamento no conjunto, a mesma escolha aparece na
tela (deixar os conjuntos compartilharem até 20% do orçamento). Escolha pela
regra da seção irmã, mais abaixo: não é indiferente.

---

## Somar orçamento da conta exige ler OS DOIS níveis (campanha e conjunto)

**Ao montar a ativação de um aquecimento do caso-base.** O teto de verba
(`sirius-scale/REGRAS.md` §6) compara o gasto atual da conta com um limite — e o
cálculo devolvia **zero por dia** numa conta que gastava todo dia.

Motivo: nesta conta convivem os dois modelos de orçamento.

| Onde mora o orçamento | Quem usa aqui | `daily_budget` da campanha | `daily_budget` do conjunto |
|---|---|---|---|
| Campanha (CBO) | as campanhas de captação | valor real | **0** |
| Conjunto | o aquecimento | **0** | valor real |

Somar só os conjuntos ignora toda a captação; somar só as campanhas ignora o
aquecimento. Nos dois casos o teto de segurança passa a não proteger nada, e
**falha em silêncio** — não há erro, só um número baixo demais que aprova
qualquer ativação.

```python
# campanhas ativas do lançamento (pega o CBO)
total += int(c.get("daily_budget") or 0) / 100
# + conjuntos ativos DESSAS campanhas (pega o não-CBO)
total += int(s.get("daily_budget") or 0) / 100
```

⚠️ Filtrar os conjuntos por `campaign_id` das campanhas já coletadas, não pelo
nome — conjunto não carrega o nome da campanha, e pedir `campaign{name}` em
lote traz o campo mas dobra o custo da chamada.

📌 Vale a mesma checagem em qualquer conta que compare gasto com teto: calcular
uma vez e conferir se o total bate com o Gerenciador. Um teto que lê zero aprova
tudo.

**O que conferir à mão:** a soma da verba diária pega as campanhas com orçamento
de campanha **e** os conjuntos com orçamento próprio, nunca só uma das colunas.

---

## `is_adset_budget_sharing_enabled` virou obrigatório ao criar campanha sem CBO

Medido na v26.0, criando uma campanha de antecipação do caso-base. A criação
falhou com 400 mesmo com todos os campos que sempre funcionaram:

```
error_subcode: 4834011
error_user_title: "É necessário especificar True ou False no campo
                   is_adset_budget_sharing_enabled"
error_user_msg:   "...se você não estiver usando o orçamento da campanha.
                   Com a opção True, seus conjuntos de anúncios poderão
                   compartilhar 20% do orçamento para otimizar o desempenho
                   geral."
```

**Quando aparece:** ao criar campanha cujo orçamento vai ficar no CONJUNTO
(sem CBO). Campanha com `daily_budget` próprio não pede o campo.

**Qual valor usar — não é indiferente:**

- `False` quando cada conjunto precisa gastar exatamente o orçamento dele.
  É o caso de **fase com conjunto agendado por dia** (contagem regressiva):
  com `True`, um conjunto poderia puxar até 20% da verba de outro, e o dia
  que já passou roubaria do que ainda vai rodar.
- `True` quando os conjuntos são alternativas simultâneas do mesmo teste e
  faz sentido a Meta remanejar entre eles.

## `bid_strategy` mora no mesmo nível do ORÇAMENTO

Segundo erro da mesma família, medido logo depois de corrigir o
`is_adset_budget_sharing_enabled`:

```
error_subcode: 1885737
error_user_title: "Nenhum orçamento para a campanha"
error_user_msg:   "Esta campanha não tem orçamento. Adicione um orçamento
                   para editar a estratégia de lance."
```

**Causa:** `bid_strategy` foi enviado na CAMPANHA, mas a campanha não tinha
orçamento próprio (a verba estava nos conjuntos). A Meta só aceita estratégia
de lance no nível onde o orçamento existe.

- Verba na campanha (CBO) → `bid_strategy` na campanha
- Verba no conjunto → `bid_strategy` no conjunto, e a campanha vai sem ele

⚠️ **Armadilha de copiar estrutura existente:** as campanhas de captação do
caso-base têm `bid_strategy` na campanha, e por isso parecem o modelo a seguir
— mas elas usam CBO (`daily_budget` na campanha). Copiar a estrutura delas pra
uma campanha com verba por conjunto reproduz exatamente esse erro. É o mesmo
alerta da regra geral de escrita: nunca copiar objeto existente sem conferir
o que mudou de contexto.

**O que conferir à mão:** com orçamento de campanha, a estratégia de lance fica na
campanha; com orçamento no conjunto, fica em cada conjunto.

## Agendar troca de criativo: só existe no nível do CONJUNTO

A Meta **não** agenda anúncio. `start_time` / `end_time` existem no conjunto,
não no `ad`. Então, quando a arte precisa mudar em data certa (contagem
regressiva, "começa amanhã", virada de fase), a estrutura obrigatória é
**um conjunto por dia**, cada um com sua janela e sua arte.

Consequências que valem saber antes de desenhar assim:

1. **Conjunto de 1 dia nunca sai do aprendizado** (a Meta pede ~50 conversões).
   Em captação isso seria ruim; em remarketing de lista fechada é aceitável,
   porque o trabalho é alcance e frequência, não otimização. O custo por
   resultado sai pior que o da captação — é esperado, não é a campanha
   indo mal.
2. **O agendamento não liga nada sozinho se o objeto estiver PAUSED.** Criar
   agendado e deixar pausado NÃO faz a campanha subir na data: é preciso
   ativar campanha + conjunto + anúncio antes da primeira janela abrir.
3. **Dimensionar a verba pelo tamanho do público, não pelo total ÷ dias.**
   Verba diária ÷ (CPM ÷ 1000) = impressões; impressões ÷ público =
   frequência. Medido no caso-base: a mesma verba diária sobre um público de ~3
   mil pessoas dava 3–5x **no mesmo dia** (saturação), e sobre ~25 mil dava 0,4x
   (a maioria não veria uma vez). O ponto de trabalho ficou em ~1,7x/dia, com
   público de ~6 a 7 mil. Tamanho de público de remarketing se mede com
   `delivery_estimate`, nunca com `approximate_count`: em público de **site**, o
   `approximate_count` devolve um stub ("20 a 20"), não o tamanho; o
   `delivery_estimate` mirando só aquele público (com `optimization_goal` e
   `promoted_object`) devolve o número utilizável.

*Nível de confiança: VARIAÇÃO ISOLADA — um lançamento, um cliente, primeira
vez que a estrutura de conjunto-agendado-por-dia foi montada por API ali.*

**O que conferir à mão:** um conjunto por dia, cada um com início, fim e a arte do
dia; campanha, conjunto e anúncio ativados antes da primeira janela abrir; e a
frequência por dia calculada pela conta acima antes de fechar a verba.

---

## Editar `targeting` de um conjunto: o que a leitura devolve, a escrita recusa

Achado ao desligar o Advantage+ nos conjuntos de antecipação do caso-base.
Custou uma rodada inteira de 6 falhas.

O `targeting` da Meta é **substituído inteiro, nunca mesclado** — mandar só a
chave que você quer mudar apaga o resto do alvo. A saída óbvia é ler o
targeting atual, trocar a chave e devolver o objeto completo. **Isso falha.**

A API devolve, na leitura, campos derivados que ela recusa na escrita, e o erro
é opaco: `Invalid parameter`, sem apontar o campo.

Campos que precisam ser removidos antes de devolver o objeto:

| Campo | Por quê |
|---|---|
| `age_range` | derivado de `age_min`/`age_max`, só leitura |
| `user_age_unknown` | só leitura |
| `brand_safety_content_filter_levels` | recusado em alguns objetivos |

E `custom_audiences` / `excluded_custom_audiences` voltam da leitura como
`{"id": ..., "name": ...}`; a escrita aceita **só o `id`**.

Receita que funciona:

```python
bruto = ad_set["targeting"]
bruto = bruto.export_all_data() if hasattr(bruto, "export_all_data") else dict(bruto)
novo = copy.deepcopy(bruto)
for so_leitura in ("age_range", "user_age_unknown",
                   "brand_safety_content_filter_levels"):
    novo.pop(so_leitura, None)
for chave in ("custom_audiences", "excluded_custom_audiences"):
    if novo.get(chave):
        novo[chave] = [{"id": a["id"]} for a in novo[chave]]
# só agora mexer na chave que interessa
novo["targeting_automation"] = {"advantage_audience": 0}
AdSet(id).api_update(params={"targeting": novo})
```

Nota de SDK: o objeto de leitura é um `Targeting`, não um `dict` — `json.dumps`
nele levanta `TypeError`. Use `export_all_data()`. O mesmo vale pra qualquer
objeto aninhado, por exemplo o `learning_stage_info` do conjunto
(`AdCampaignLearningStageInfo`), ao gravar cache de leitura: `dict(obj)` não
converte o que está dentro.

Depois de editar, o `effective_status` do conjunto pode aparecer como
`IN_PROCESS` por alguns instantes. É processamento pós-edição, não erro:
confirmar relendo `status`, `effective_status` e `issues_info` antes de
concluir que quebrou algo.

*Nível de confiança: PADRÃO CONSISTENTE — é comportamento da API da Meta,
reproduzido nos 6 conjuntos e corrigido com a mesma receita nos 6.*

**O que conferir à mão:** o problema da receita é de quem escreve pela API. Na
tela, o cuidado é outro: editar o público de um conjunto no ar reinicia o
aprendizado (seção "Captação de público interno", mais abaixo). E, depois de
salvar, reabrir o conjunto e conferir público, exclusões e Advantage+; logo depois
da edição ele pode aparecer "em processamento" por alguns instantes, sem ser erro.

## Campanha nova se cria DUPLICANDO a que já funciona, não do zero

**Regra transversal — decisão do Rodrigo.** A evidência que a originou é do Google
(`sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §10: três
configurações de meta de conversão diferentes entre campanhas do mesmo
lançamento, todas herdadas do default da conta na data de criação). O mecanismo
é o mesmo na Meta, então a regra vale nos dois lados.

Ao criar campanha/conjunto novo durante um lançamento, **partir da unidade mais
parecida que já está entregando bem** e replicar a configuração campo a campo, em
vez de montar do zero e confiar no que a plataforma preenche sozinha.

O que precisa vir junto na Meta, no mínimo:

- `bid_strategy` — e lembrar que ele mora **no mesmo nível do orçamento** (ver
  seção própria neste arquivo): campanha se CBO, conjunto se não
- `is_adset_budget_sharing_enabled` (obrigatório na criação, ver seção própria)
- `promoted_object.custom_event_type` — o evento de otimização real do conjunto
  (`sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §2 tem a tabela de
  onde a meta mora em cada plataforma)
- `targeting`, incluindo Advantage+ / expansão de público — e a ressalva de que
  **o que a leitura devolve, a escrita recusa** (seção própria neste arquivo):
  copiar o `targeting` lido cru não funciona, tem que remontar
- exclusões (público de leads já captados, ver
  `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §3)

⚠️ Mesma ressalva do Google: **duplicar não dispensa conferir.** A Meta também
descontinua campo sem removê-lo dos objetos antigos — o
`standard_enhancements` em `degrees_of_freedom_spec`, documentado neste arquivo, é
exatamente um caso de campo que existe no objeto velho e quebra a criação nova. O
ciclo é **duplicar → comparar → `execution_options: ['validate_only']` → escrever**.

**O que conferir à mão:** "Duplicar" no Gerenciador e, antes de publicar, comparar
com a original: orçamento e onde ele mora, lance, evento de conversão, público,
exclusões, Advantage+ e posicionamento.

## Criativo de vídeo exige miniatura explícita — vídeo recém-subido não ganha uma sozinho

**Visto ao criar 5 anúncios com vídeos subidos minutos antes.**
Todos os `create_ad_creative` falharam:

```
code 100, error_subcode 1443226
error_user_title: "Seu anúncio precisa de uma miniatura de vídeo"
error_user_msg: "Especifique image_hash ou image_url no campo video_data
                 de object_story_spec."
```

O vídeo estava com `video_status: ready` e as três fases (upload, processamento,
publicação) completas — **não é problema de processamento.** A Meta simplesmente
não escolhe a miniatura por você na criação via API.

As miniaturas existem e são geradas automaticamente (15 por vídeo, no teste).
Pegar a preferida e passar como `image_url`:

```python
th = AdVideo(video_id).api_get(fields=["thumbnails"]).export_all_data()
ts = th.get("thumbnails", {}).get("data", [])
uri = next((t["uri"] for t in ts if t.get("is_preferred")), ts[0]["uri"])
# ... object_story_spec.video_data.image_url = uri
```

📌 O criativo de referência tinha `image_url` **e** `image_hash` preenchidos, e o
agente copiou tudo do `object_story_spec` menos esses dois — por parecerem cache.
Eram obrigatórios. Reforça a regra de duplicação: **copiar "quase tudo" não é
duplicar.**

**O que conferir à mão:** a miniatura de cada anúncio de vídeo, antes de publicar.

## O Cursor de `get_campaigns()` se esgota — iterar duas vezes devolve VAZIO

*(Só pra quem lê a conta por código, com o SDK da Meta.)*

Escrevendo uma leitura de verba do aquecimento. O código achava a conta inteira
mas **não achava o conjunto de aquecimento**, e estourava com
`TypeError: 'NoneType' object is not subscriptable`.

O código era este, e o erro está em duas linhas que parecem inofensivas:

```python
camps = a.get_campaigns(fields=[...])          # <- Cursor, NAO lista
ativos = [c for c in camps if ...]             # 1a iteracao: funciona
aq     = [c["id"] for c in camps if ...]       # 2a iteracao: VEM VAZIA
```

`AdAccount.get_campaigns()` devolve um **`Cursor`**, não uma lista. Ele se
esgota na primeira iteração. A segunda não dá erro, não avisa, não devolve
nada — só uma lista vazia. Aí o `filtering` seguinte roda com `value: []` e a
consulta de conjuntos volta sem linha nenhuma.

**A correção é uma palavra:**

```python
camps = list(a.get_campaigns(fields=[...]))    # materializa uma vez
```

⚠️ **Por que isso vai acontecer de novo:** a regra pra API da Meta manda batchar —
buscar tudo numa chamada e filtrar em memória
(`sirius-scale/frameworks/trafego/_metodologia.md` §5). É a regra certa, e é
exatamente ela que leva a reusar a mesma resposta várias vezes. Toda vez que
você guardar um retorno da SDK pra filtrar mais de uma vez, **materialize com
`list()` na hora de guardar.** Vale pra `get_campaigns`, `get_ad_sets`,
`get_ads` e `get_insights`.

O sintoma nunca é uma exceção no ponto do erro: é lista vazia, resultado
faltando, ou um `None` estourando bem depois.

## Somar orçamento: ler os dois níveis não basta — o ESCOPO tem que casar com o teto

A seção acima resolveu metade do problema. A outra metade apareceu quando **três
cálculos da casa, na mesma conta e no mesmo dia**, devolveram três totais diários
diferentes:

| método | total |
|---|---:|
| só `daily_budget` de campanha `ACTIVE` | o menor (a base) |
| campanha + conjuntos, **filtrando pelo código do lançamento no nome** | ~44% acima da base |
| campanha quando tem budget próprio, **senão** os conjuntos, sem filtro de nome | **~71% acima da base** |

O primeiro erra pelo motivo da seção anterior (ignora quem tem budget no
conjunto). Mas o segundo e o terceiro **leem os dois níveis** e ainda assim
divergem em quase um quinto — porque um conta **só o lançamento** e o outro conta
**a conta inteira**.

📌 **O teto de segurança da casa é definido como "soma de uma plataforma inteira,
por dia".** Então o cálculo que filtra pelo nome do lançamento está comparando
maçã com laranja e **subestima contra o próprio teto** — que é a falha mais
perigosa possível numa trava de segurança, porque ela aprova o que deveria barrar.

**Regra:** a soma do gasto tem fonte única, com o mesmo escopo do teto. Não
reimplemente a soma a cada script ou planilha — mesmo motivo pelo qual o valor do
teto virou fonte única. Padronizar o teto e deixar a **medição** solta resolve
metade do problema e esconde a outra metade.

**O que conferir à mão:** decidam uma vez se o teto de vocês é da conta inteira ou
de um lançamento, escrevam isso junto do teto, e somem sempre no mesmo escopo.


---

## Buscar anúncio por nome: filtrar na API, nunca listar e filtrar em memória

**Medido na conta de outro cliente da casa (1.080+ anúncios).**

O agente procurou um anúncio pelo código dele listando a conta inteira com
`account.get_ads(params={"limit":500})` e filtrando o nome em Python. **Voltaram
1.080 anúncios e o procurado não estava entre eles** — a conclusão, errada, foi
que o anúncio não existia. Ele existe: são 5 instâncias, todas `ADSET_PAUSED`.

✅ **O que funciona** — filtrar na própria API:

```python
acc.get_ads(fields=["id","name","effective_status","campaign_id"],
            params={"limit":200,
                    "filtering":[{"field":"name","operator":"CONTAIN","value":"<código do anúncio>"}]})
```

Uma chamada, 19 resultados, incluindo os pausados. Também é mais barato pro rate
limit (`sirius-scale/frameworks/trafego/_metodologia.md` §5).

⚠️ **`effective_status` e `filtering` juntos = `Invalid parameter`.** Tentar
ampliar a busca passando
`{"effective_status":["ACTIVE","PAUSED","ARCHIVED","DELETED"], "filtering":[...]}`
faz a chamada falhar inteira. Use **um ou outro** — e o `filtering` por nome já
traz pausado sem precisar do outro.

📌 **A regra que sobra:** quando a pergunta é *"esse objeto existe?"*, listar
tudo e filtrar depois **responde errado silenciosamente** se a paginação parar
antes. Filtro na API responde certo ou dá erro — nunca dá falso negativo mudo.
Vale pra anúncio, conjunto e campanha.

**Alcance:** NÃO TESTADO FORA — medido em uma conta. Mas é comportamento de
plataforma, não de cliente.

**O que conferir à mão:** antes de dizer que um anúncio não existe, buscar pelo
nome com o filtro de status aberto (pausados e arquivados também), em vez de rolar
a lista.

---

## Erro 403 "sem permissão" pode ser TOKEN ERRADO, não conta sem acesso — em operação multi-conta

**Medido conectando a conta de anúncios de outro cliente da casa.**

O token padrão da operação (de um app da casa) devolveu:

```
(#200) Ad account owner has NOT grant ads_management or ads_read permission
```

**Mesmo com os escopos corretos** — conferido via `debug_token`:
`ads_management`, `ads_read`, `business_management` todos presentes.

A causa não era falta de permissão real. Existia um **segundo token**, de outro
app, que tinha acesso a essa conta específica — funcionou de primeira, mesma
chamada.

⚠️ **A mensagem de erro engana.** Ela fala em "owner not grant permission",
que soa como problema de configuração do cliente. O problema real era estar
testando com o app errado pra aquela conta.

✅ **O que fazer:** numa operação com múltiplos tokens/apps Meta (vários
clientes, vários negócios), um 403 de permissão **não prova** que a conta não
liberou acesso — testar todos os tokens disponíveis antes de concluir isso.
`debug_token` confirma escopo, mas não confirma qual token aquela conta
específica autorizou.

**Alcance:** o comportamento da API é UNIVERSAL. A necessidade de testar
múltiplos tokens só existe em operação multi-conta. Com um conector só, o mesmo
raciocínio: um 403 com escopo certo pode ser o app (ou o usuário de sistema)
errado pra aquela conta. Conferir a quem a conta deu acesso antes de pedir
permissão de novo ao dono.

**Na casa, a escolha do token virou tabela, não memória.** Medido com uma leitura
da conta com cada token: um abria a conta do caso-base e dava 403 (#200) na de
outro cliente da casa, e o outro token fazia o inverso. Desde então a leitura
diária, a aplicação de verba e a ativação começam por uma tabela conta → token.
Conta nova de cliente entra com uma linha nessa tabela, conferida com uma leitura
da conta antes de escrever. *VARIAÇÃO ISOLADA (2 contas).*

---

## `subtype` na criação de público: exigido no CRM, **recusado** no de site (v26)

*(Medido criando os dois tipos na mesma sessão. UNIVERSAL — é comportamento da
API v26, não da conta. Vale pra criação de público pela API; pela tela não existe
esse campo.)*

O mesmo parâmetro tem comportamento **oposto** conforme o tipo de público, e as
duas mensagens de erro só aparecem quando você tenta:

| Público | `subtype` | Erro se fizer o contrário |
|---|---|---|
| **WEBSITE** (com `pixel_id` + `rule`) | **NÃO enviar** | `400` — *"O parâmetro 'subtipo' não é aceito na versão atual da API"* |
| **CUSTOM / CRM** (lista de e-mail) | **obrigatório** (`"CUSTOM"`) | `400 (#100) Missing parameter(s): subtype` |

Faz sentido depois de visto: no público de site a Meta **infere** o tipo pela
regra e pelo pixel; numa lista de CRM não há o que inferir.

⚠️ **A mensagem engana — e engana de formas DIFERENTES.** Medido nos dois casos:

| Público | Mensagem que a v26 devolve | Causa real |
|---|---|---|
| WEBSITE | *"O parâmetro 'subtipo' não é aceito"* | `subtype` |
| ENGAGEMENT | *"(#2654) **Nome do evento inválido** para o público personalizado: o nome do evento deve ter menos de 50 caracteres e só pode conter caracteres alfanuméricos e sublinhados"* | **`subtype`** |
| ENGAGEMENT de VÍDEO, regra em lista `{event_name, object_id, context_id}` | *"A sintaxe da regra de público personalizado é muito antiga para a Graph API"* (100/1870029) | **FALTA** de `subtype: "ENGAGEMENT"` — essa forma de regra (a dos públicos de vídeo da conta) só passa COM ele, como num criador anterior da casa que funcionava. A regra nova (`inclusions` + `event_sources`) é a que recusa o subtype |

No segundo caso a mensagem aponta pro `event_name` da regra — que estava
perfeito (`page_engaged`, 12 caracteres, só letras e sublinhado). Tirando o
`subtype`, **a mesma regra passou de primeira**.

📌 **Regra de depuração:** em qualquer `400` ao criar público na v26, **tirar o
`subtype` é o primeiro teste**, independente do que a mensagem disser. Ela vai
culpar a regra, o evento, o que for. Só depois mexer no que ela aponta.

E o inverso segue valendo: no público de **CRM** o `subtype` é obrigatório, e aí
a mensagem é honesta (`Missing parameter(s): subtype`).

📌 **Criador antigo que passe `subtype: "WEBSITE"` vai quebrar se rodar de
novo.** Quando for reutilizar, tirar o campo — a regra dele continua correta.

### A forma da regra de público de site que a v26 aceita

Três detalhes que, faltando qualquer um, derrubam a criação:

1. o `id` do pixel é **inteiro**, não string;
2. o `and` leva um segundo filtro `url i_contains ""` — o painel da Meta sempre
   grava esse termo vazio junto;
3. a regra carrega `"template": "VISITORS_BY_URL"`.

E o `pixel_id` vai **também no topo** do `params`, além de dentro da regra.

**E o valor da URL vai sem `https://` e sem `www` (*UNIVERSAL*).**
- O `i_contains` compara com a URL inteira que o pixel registra. Então `https://dominio.com.br/insc` não casa com
  `https://www.dominio.com.br/insc...`. Escrever `dominio.com.br/insc`.
- A Meta não avisa: público de site volta com tamanho 20 de qualquer jeito.
- Conferir lendo a regra (`ads_get_custom_audience` devolve) contra a URL que a página abre de verdade.

## Enviar hashes com `add_users`: lista PLANA + `pre_hashed`, nunca `is_raw`

*(Já estava documentado dentro de um script da casa — e foi repetido uma semana
depois porque o agente não consultou antes de escrever código novo. Promovido pra
cá justamente por isso: dentro de um script, só acha quem já sabe que existe.)*

Pra schema escalar (`EMAIL_SHA256`, `PHONE_SHA256`), o SDK espera:

```python
CustomAudience(pid).add_users(schema="EMAIL_SHA256", users=lista_plana_de_strings,
                              pre_hashed=True)
```

`users=[[h], [h]]` com `is_raw=True` faz o `format_params` do SDK chamar
`.strip()` num `list` e estourar `AttributeError`.

⚠️ **O custo real disso é o silêncio:** a exceção acontece **depois** de o
público já ter sido criado. Fica um público novo, vazio, com status "pronto para
uso" — e quem não olhar o número acha que deu certo. Sempre conferir
`approximate_count` (ou o log de "N/N enviados") depois de criar.

**O que conferir à mão:** depois de subir uma lista de clientes, conferir o
tamanho do público. "Pronto para uso" não quer dizer que a lista entrou.

## Criação em lote acende o rate limit — backoff em TODA chamada, não só no `create`

*(Medido criando 9 campanhas × 2 conjuntos da fase de CPL de um lançamento do
caso-base. VARIAÇÃO ISOLADA — uma conta, mas o mecanismo é da plataforma. Vale pra
criação pela API.)*

Criar ~20 objetos seguidos derruba a conta com **"A conta de anúncios tem uma
quantidade excessiva de chamadas de API"** — a Meta devolve isso **traduzido e
sem código útil no corpo**, então filtro por `error_code == 17` não pega.
Detectar pelo texto: `excessiv`, `too many`, `rate limit`, `user request limit`.

Medido: passou dos **4 primeiros conjuntos** e derrubou os 14 restantes.

⚠️ **O erro que custou a segunda tentativa:** o backoff entrou só no
`create_ad_set` e a rodada foi refeita — **falhou tudo de novo**, porque o limite
estourava antes, na `Campaign(id).get_ad_sets()` que checa o que já existe. Numa
rodada de criação **toda** chamada à API precisa do retry, inclusive as de leitura
que parecem inofensivas.

Receita que funcionou (retomada completa, esperando até 320s numa das chamadas):

```python
def com_backoff(fn, tentativas=6, base=20):
    for i in range(tentativas):
        try:
            return fn()
        except Exception as e:
            msg = str(e).lower()
            rate = any(k in msg for k in
                       ("excessiv", "too many", "rate limit", "user request limit"))
            if not rate or i == tentativas - 1:
                raise
            time.sleep(base * (2 ** i))
```

Mais **8 segundos de pausa entre campanhas**. Backoff resolve quando o limite
já estourou; a pausa diminui as vezes em que estoura.

**Atualização (lote maior, um mês depois), VARIAÇÃO ISOLADA:** com a pausa de 8 s ligada, arquivar 15 campanhas e
criar 21 anúncios em 13 campanhas, por frente e em sequência, levou ~2 h. Numa das chamadas o backoff fez 6 esperas
seguidas (as duas últimas de 300 s) e passou na tentativa seguinte. A pausa não evita o limite num lote desse tamanho:
planeje sem ninguém esperando o fim, uma frente depois da outra, nunca em paralelo. O backoff que a casa usa hoje é o
mesmo desenho com mais fôlego: 8 tentativas, base de 20 s e teto de 300 s por espera (até 7 esperas, uns 20 min por
chamada). O trecho de código acima é a primeira versão, mantido como histórico.

**Atualização (madrugada de outra subida), VARIAÇÃO ISOLADA:** três fatos medidos criando 4 vídeos de um low ticket.

1. **A cota é da conta de anúncios, não do script.** Na mesma madrugada outra sessão subia 12 vídeos e consultava
   cada um a cada 10 s. As duas disputavam a mesma cota, e cada uma via o limite como se fosse só dela. Antes de lote
   grande, conferir se outra sessão (ou outra pessoa) está escrevendo na mesma conta.
2. **O app da casa estava no nível `development_access` da API de anúncios** (cabeçalho `x-business-use-case-usage`,
   `ads_api_access_tier`). É o nível de cota baixa; o padrão (`standard_access`) pede análise da Meta. O mesmo
   cabeçalho traz `estimated_time_to_regain_access` em minutos: ler antes de tentar de novo, em vez de chutar a espera.
3. **Criar um criativo por vez gasta muito menos que criar por frente.** Por frente, o criador relê cada objeto que
   já existe antes de chegar no novo, e uma das rodadas estourou as 7 esperas relendo os anúncios antigos, sem criar
   nada. Um vídeo por vez e 60 s entre eles, os 4 entraram em ~65 min (cada um ainda pegou de 4 a 6 esperas).

E um quarto, de API: **a Graph v26 recusa `?ids=a,b,c`** ("The ids query parameter is deprecated in v26.0+", HTTP 500).
Leitura de vários objetos: `act_<conta>/<adsets|campaigns|ads>` com `filtering` `id IN [...]` (o padrão de batching
de `sirius-scale/frameworks/trafego/_metodologia.md` §5 já era esse; o atalho é que morreu). O lote POST (`batch`, até 50
pedidos por chamada) serve pra qualquer objeto, inclusive o que não fica debaixo da conta, como a mídia do Instagram.
Script que lê a Meta pelo `ids` falha, e o pior caso é o que engole o erro e segue com a lista vazia: ao revisar script,
procurar `ids=` no código.

📌 **E o criador tem que ser idempotente** — reaproveitar campanha e conjunto que
já existem pelo nome. Sem isso, a retomada duplica o que já entrou. Foi o que
permitiu rodar três vezes sem sujar a conta.

**Conta parada tem limite baixo, e listar a conta inteira estoura.** A conta de outro
cliente da casa, parada havia meses, tem mais de mil campanhas e milhares de conjuntos.
Duas rodadas seguidas da conferência, cada uma listando todas as campanhas (46 páginas de
25), deram erro 17, subcode 2446079 ("A conta de anúncios tem uma quantidade excessiva de
chamadas de API") na terceira leitura. O limite é da CONTA, não do app. Leitura numa conta
assim vai sempre filtrada na API (`effective_status IN [ACTIVE]`, `updated_since`,
`id IN [...]`) e com `limit` de 200. Quem montar campanha nela usa o backoff em toda
chamada, inclusive leitura. VARIAÇÃO ISOLADA (1 conta).

**O 17/2446079 pode barrar só a lista de conjuntos e de anúncios.** Por uns 20 minutos, na
conta do caso-base, `/act_…/adsets`, `/act_…/ads` e até `/<campanha>/adsets` voltavam o
erro, enquanto `/act_…/campaigns`, a leitura por id (campanha, conjunto, anúncio, criativo)
e a escrita por id funcionavam. O `x-ad-account-usage` mostrava 0%, então o cabeçalho não
avisa esse bloqueio. O criador passou depois de 160 s de backoff. Na mesma janela, a
conferência de antes de ativar não conseguiu ler a conta três vezes, porque lê pela lista
de conjuntos. Com a lista travada, ler e pausar por id funciona, e pausar e criar pausado
podem seguir. Ligar espera a conferência voltar, ou a decisão de quem é dono da conta com o
bloqueio no resumo. VARIAÇÃO ISOLADA (1 janela).

---

## Escrita aceita ≠ escrita gravada: campo com nome errado é descartado em SILÊNCIO

*(Medido corrigindo o Advantage+ dos 18 conjuntos da fase CPL.
UNIVERSAL — é comportamento da Graph API.)*

O agente mandou `targeting_relaxation` num `AdSet.api_update()`. O campo correto é
**`targeting_relaxation_types`**. O que aconteceu:

| | |
|---|---|
| A API respondeu | **sucesso** |
| O relatório da correção disse | **"18 corrigidos · 0 falhas"** |
| O que foi gravado | **nada** |
| Como se descobriu | a leitura de volta, numa conferência separada |

A Graph API **não valida nomes de campo desconhecidos dentro do `targeting`** —
ela ignora o que não reconhece e devolve 200. Não há erro, não há aviso, não há
campo `warnings` na resposta.

📌 **A regra que sai daí, e vale pra toda escrita:**
**escrita não conta como feita até a leitura de volta confirmar**
(`sirius-scale/REGRAS.md` §6). O retorno de sucesso da API não é prova de nada.
Toda escrita precisa de um passo de verificação que **relê o objeto** e compara
com o pretendido — de preferência numa conferência separada, que não compartilhe
as constantes com quem escreveu (se o nome do campo está errado nos dois, os dois
concordam e erram junto).

⚠️ **É o mesmo mecanismo do §"subtype"**, por outro caminho: lá a mensagem de
erro mentia sobre a causa; aqui não há mensagem nenhuma. Os dois casos dizem a
mesma coisa — **a resposta da Meta não é fonte confiável sobre o que ela fez.**

**O que conferir à mão:** depois de salvar, reabrir o objeto e conferir que a
mudança ficou — principalmente público, Advantage+ e orçamento.

### E o erro de processo, que é o que se repete

O nome certo estava em **dois lugares** que o agente tinha à mão:

1. `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.3, na tabela —
   seção que ele tinha acabado de ler;
2. um script da casa que **já fazia exatamente isso**, com o campo certo.

Escreveu o nome de memória e criou código novo sem procurar o que existia. É o
mesmo padrão do `add_users` (§ acima): o conhecimento estava registrado, e o que
falhou foi **consultar antes de escrever**, não registrar depois.

**Antes de escrever código de escrita novo:** procurar o nome do campo nos
frameworks (e no que vocês já registraram em `frameworks-da-casa/`), e ver se já
existe quem faça.

## `landing_page_view` e `omni_landing_page_view` são a MESMA ação — nunca somar

**Fato de plataforma, medido em 7 campanhas de remarketing do caso-base.** Em
`actions` dos insights, o tipo `omni_landing_page_view` é o agregado
cross-plataforma que **já contém** o `landing_page_view` — nas 7
campanhas os dois vieram idênticos (426/426, 860/860, 274/274…).

Uma leitura de ritmo do remarketing da casa somava os dois pra "cobrir os nomes
diferentes que a Meta dá à visita conforme o objetivo". Resultado: LPV
**dobrado** e custo por visita da Meta **pela metade** em todo relatório de quatro
dias seguidos — o ranking mostrava um dos momentos do remarketing com metade do
custo por visita real. Mesma lógica vale pra qualquer par `x` / `omni_x`
(`purchase`/`omni_purchase`, `add_to_cart`/`omni_add_to_cart`…).

**Regra:** quando a lista de tipos existe pra cobrir *apelidos* da mesma
ação, o número é o **maior** deles, não a soma. Somar só faz sentido entre
ações de fato diferentes. Conferir sempre olhando o `actions` cru de uma
campanha antes de confiar no total — é uma linha de código e pega o erro na
hora.

**O que conferir à mão:** em export ou planilha que traga as duas colunas, usar
uma só (a maior), nunca a soma.

## Seguidor não existe por anúncio: o resultado de "seguidores" é `profile_visit_view`, e vem no campo `results`

*(medido no debriefing de uma distribuição de conteúdo do caso-base)*

Campanha de "crescer seguidores" na Meta otimiza por `PROFILE_VISIT` (Gerenciador)
ou `VISIT_INSTAGRAM_PROFILE` (botão Impulsionar do app). **Nenhuma das duas
devolve seguidor ganho** — nem em `actions` (não existe `follow`), nem em
lugar nenhum da Insights API. O que existe é **visita ao perfil**, e ela só
aparece pedindo os campos `results` e `cost_per_result`:

```python
account.get_insights(
    fields=["spend", "optimization_goal", "results", "cost_per_result"],
    params={"level": "ad", "time_range": {...}})
# -> "results": [{"indicator": "profile_visit_view", "values": [{"value": "<n>"}]}]
```

O `indicator` acompanha o objetivo do conjunto (`actions:link_click`,
`video_thruplay_watched_actions`, `profile_visit_view`…), e quando o conjunto
não entregou o item vem **sem** a chave `values` — ler com `.get`, não com
índice.

Seguidor de verdade só sai do **Insights do Instagram** (Graph API,
`/{ig_user_id}/insights?metric=follower_count&period=day`, e só pros últimos
30 dias — o histórico anterior a isso não é recuperável), e exige o token com
`instagram_basic` + `instagram_manage_insights`. O token de tráfego da casa **não
tinha** essas duas — a chamada devolve `(#10) Application does not have permission
for this action`. Sem elas, campanha de seguidores tem proxy (custo por visita),
não KPI.

Duas notas do mesmo levantamento: `page_fans` e `page_impressions_unique`
já não são métricas válidas de página na v22 (`(#100) The value must be a
valid insights metric`), e `page_follows` / `page_daily_follows_unique`
aceitam a chamada mas voltaram vazios nesta página — não contar com elas.

**O que conferir à mão:** o resultado que o Gerenciador mostra numa campanha de
seguidores é visita ao perfil. Seguidor por dia sai dos insights do Instagram (pela
API, só os últimos 30 dias: o que ficar mais velho que isso não se recupera, então
registre antes).

## Visita ao perfil do IG por API: `PROFILE_VISIT` cria o conjunto mas RECUSA o anúncio — usar `VISIT_INSTAGRAM_PROFILE`

*(medido com objetos descartáveis, na mesma distribuição de conteúdo. Vale pela
API; pela tela, a campanha de seguidores sai pronta, e o que importa lembrar é a
seção anterior.)*

A campanha "IG Seguidores" feita na tela roda com `optimization_goal =
PROFILE_VISIT` + `destination_type = INSTAGRAM_PROFILE`. Reproduzir isso por
API:

| passo | `PROFILE_VISIT` | `VISIT_INSTAGRAM_PROFILE` |
|---|---|---|
| criar conjunto (`promoted_object = {page_id}`) | **recusa**: "A conta de anúncios não está qualificada para anúncios de Visita ao perfil" (100/2016153) | ok |
| criar conjunto (`promoted_object = {page_id, instagram_profile_id}`) | ok | ok |
| criar anúncio com `object_story_id` do post da página | **recusa** com o mesmo 2016153 — mesmo com `instagram_user_id` no criativo | **ok** |
| resultado na Insights API | `profile_visit_view` | `profile_visit_view` (igual) |

`PROFILE_VISIT` + só `page_id` é o "anúncio de visita ao perfil" do
**Facebook**, recurso liberado por conta ("Entre em contato com o Suporte
Direto"). O `instagram_profile_id` é o id da conta do IG ligada ao ad account
(`act_<conta>/instagram_accounts`, começa com 17841…), **não** o id do event
source do público (`ig_business`, começa com 1209…) — esse volta "must be a valid
instagram profile id". Mesmo assim o anúncio com post da página não passa.
`VISIT_INSTAGRAM_PROFILE` é o objetivo que o botão Impulsionar usa (os posts
impulsionados pelo app rodaram com ele, a um custo por visita praticamente igual
ao do `PROFILE_VISIT`), aceita conjunto e anúncio e devolve o mesmo indicador.
`LINK_CLICKS` + `INSTAGRAM_PROFILE` + post dá "Incompatibilidade entre criativo e
objetivo" (100/1815159).

Dois custos do mesmo dia:

- **Orçamento vitalício tem piso** (valor da época, conferir na plataforma): R$ 35
  em 7 dias foi recusado — "deve ser superior a R$ 36,19" (100/1885272).
  ≈ R$ 5,17/dia por conjunto; R$ 6/dia (R$ 42 em 7 dias) passa.
- **O erro que vem do anúncio aparece com a mesma cara do erro do conjunto.**
  O criador fazia conjunto + anúncio no mesmo `try`; duas rodadas deixaram
  **8 conjuntos órfãos** (sem anúncio) na campanha antes de alguém olhar a
  conta. Criar em dois passos com leitura de volta, ou pelo menos listar os
  conjuntos da campanha antes de tentar de novo.
- **Objeto descartável conta no rate limit**: uma dúzia de conjuntos de
  teste criados e apagados em sequência derrubou a conta em "excessiva
  quantidade de chamadas" (17/2446079) por mais de 10 minutos — um backoff de
  200 s não alcança. Testar UMA hipótese por vez, não a matriz.

## Religar campanha antiga: o que a Meta recusa e o que ninguém conferiu

*(Medido na reativação das campanhas de ingresso de um LPSG do caso-base, pra uma
turma nova. Os dois primeiros itens são UNIVERSAIS — comportamento da Graph API;
o terceiro é regra de processo da casa, nascida de um erro real.)*

### 1. Criativo copiado da leitura vem com `image_url` E `image_hash` — a criação só aceita um

Ao "trocar o texto" de um anúncio (criar `AdCreative` novo copiando o
`object_story_spec` do atual e fazer `Ad.update(creative=...)`), a leitura do
criativo devolve, em `video_data`, **os dois** campos de miniatura. Criar com os
dois dá:

```
error_subcode 1443051 · ObjectStorySpecRedundant
"Só um de image_url e image_hash deve ser especificado no campo video_data"
```

Manter o `image_hash` (estável) e `pop("image_url")`. O `generatepreviews`
pega isso antes de criar — por isso ele entra na prévia de toda reativação. Na
leitura de volta, comparar o **essencial** (page, video_id/image_hash, link) e não
o JSON inteiro — ele volta com os dois campos de novo.

### 2. Conjunto com `end_time` vencido não deixa ligar anúncio — e `0` limpa a data

Campanha de lançamento datado (uma turma de LPSG) sobe com `end_time` no conjunto
e `stop_time` na campanha. Meses depois, ligar um anúncio dela dá:

```
error_subcode 3858750 · "O conjunto de anúncios foi encerrado"
"expirou em <data>. Para activate o anúncio, atualize a data de término"
```

`AdSet.api_update({"end_time": 0})` remove a data (a leitura de volta deixa
de trazer o campo); o `stop_time` da campanha some junto quando era derivado
dos conjuntos. **O status `PAUSED` não avisa que a causa é a data.** No
caso-base, o resumo de toda reativação mostra `end_time`/`stop_time`, e a data é
limpa quando o registro do funil manda. Funil que roda toda semana (LPSG) não
pode ter data de fim: virou regra do registro, não lembrete.

**O que conferir à mão:** antes de religar campanha antiga, abrir cada conjunto e
ler a data de término; funil contínuo fica sem data de fim.

### 3. Vídeo só volta ao ar com transcrição salva — regra da casa

O que a conferência achou nos 10 vídeos que rodavam nas campanhas [LPSG]:
**um deles era o vídeo de um lançamento gratuito anterior** — falava de "evento
online gratuito", com datas fixas e "sempre às vinte horas" — e rodou por semanas
mandando pra página de ingresso **pago**, gastando nas duas plataformas, com
"conversões" contadas. Ninguém tinha ouvido o vídeo: o nome do arquivo não
entregava nada.

Regra: **antes de ligar ou religar campanha com vídeo, todo vídeo mantido tem
transcrição salva** na pasta do funil (`funis/<nome>/`) ou do lançamento, tirada
do próprio anúncio (pela API, `AdVideo(id).api_get(fields=["source"])` na Meta; no
Google o YouTube bloqueia download — usar o arquivo original ou a versão da Meta
do mesmo criativo) e passada por uma transcrição automática (são segundos pra
10 vídeos). Conferir contra a lista do momento: preço, horário, "ao vivo", data
fixa, promessa de gratuito, escassez. Vale o mesmo pra imagem: folha de contato
dos estáticos antes de religar (no caso-base, 8 de 11 estáticos tinham preço
antigo, data vencida ou "ao vivo" gravados na arte). O nome do arquivo não define
a campanha: ouvir ou ler o criativo é o que define.

### 4. Anúncio de vídeo com criativo trocado fica ACTIVE e não entrega — duplicar o anúncio destrava — *VARIAÇÃO ISOLADA (8 anúncios, uma reativação)*

Depois da sequência **troca de criativo em anúncio existente (`Ad.update(creative)`)
→ `end_time: 0` no conjunto → ativação em lote**, os 8 anúncios de **vídeo** do
LPSG ficaram `ACTIVE` em campanha, conjunto, anúncio e criativo, vídeo
`ready`, `issues_info` / `ad_review_feedback` / `recommendations` vazios — e
**zero impressão por 12 horas**, enquanto os 11 anúncios de **imagem** que
passaram pela mesma troca, nos mesmos públicos e posicionamentos, entregavam
desde a meia-noite. Nenhum campo da API explica; o Gerenciador não foi consultado
naquele momento.

O que resolveu: **criar um anúncio NOVO no mesmo conjunto, com o MESMO
criativo e o MESMO nome** (a UTM usa `{{ad.name}}`), nascendo pausado, ligar e
pausar o travado. O novo saiu de `IN_PROCESS` em 6 min e entregou a primeira
impressão ~35 min depois de ligar. Antes disso, um segundo teste (recriar o
criativo com texto único, sem `asset_feed_spec`) ficou pronto mas não foi preciso:
o criativo estava bom; o objeto travado era o anúncio.

Regras que ficam:

- **"ACTIVE" não é entrega.** Depois de religar, medir impressão por hora
  (`breakdowns=hourly_stats_aggregated_by_advertiser_time_zone` pela API; na tela,
  o detalhamento por hora do dia) em cada campanha nas primeiras 2 h — e comparar
  irmãs: se uma entrega e outra não com a mesma config, o problema está no
  objeto, não na conta.
- Os anúncios travados ficam **pausados e listados no registro** do funil, e
  nenhuma reativação os religa, mesmo com o nome igual ao do novo — senão a
  próxima ativação em lote liga o travado junto do novo. À mão, como o novo tem o
  mesmo nome do travado, separar os dois pelo ID antes de ativar em lote.
- **O objeto travado pode ser o CONJUNTO, não o anúncio.** Na campanha ABO
  (`[PF] 01`, dois conjuntos com `end_time: 0`), os 6 anúncios novos ficaram
  mais 2 h em zero; **pausar e religar os dois conjuntos** (só status) destravou
  em 6 min. Nas campanhas CBO (`[PF] 02`, `[PQ] 02`) bastou o
  anúncio novo. Ordem prática: anúncio novo → se em 40 min continua zero,
  pausa/religa o conjunto → só então duplicar o conjunto.
- Hipótese ainda aberta (não testada): trocar o criativo pelo caminho
  "criar anúncio novo + pausar o antigo" desde o início, em vez de
  `Ad.update(creative)`, evita o travamento. Testar na próxima troca de texto.

## Impulsionar post do Instagram por API, com o Advantage+ desligado nos quatro lugares

*(Antecipação de uma Black do caso-base. Os três primeiros itens são UNIVERSAIS,
comportamento da Graph API medido na conta do caso-base; o último é regra de
processo.)*

- **O post do Instagram entra pelo espelho na página.** Criativo só com `object_story_id` do post
  espelhado no Facebook (`/{page_id}/posts`) volta com `effective_instagram_media_id` e
  `instagram_user_id` preenchidos: o anúncio roda NO post do Instagram, e curtida e comentário somam
  lá. Não precisa de `instagram_basic` no token (que a casa não tem) nem de `source_instagram_media_id`.
- **Criativo de post existente nasce com as melhorias automáticas todas em `OPT_OUT`.** Lido em
  `degrees_of_freedom_spec.creative_features_spec` de dois criativos da nutrição da distribuição de
  conteúdo e conferido na leitura de volta. Não passar `degrees_of_freedom_spec` na criação (a seção
  do `standard_enhancements` já explica por quê).
- **`explore` em `instagram_positions` está obsoleto.** A criação do conjunto volta "O posicionamento
  Explorar do Instagram está obsoleto para essa versão da API" (code 100/2490589); `explore_home`
  continua aceito. Posicionamento manual que funcionou: Facebook `feed, story, facebook_reels,
  profile_feed`, Instagram `stream, story, reels, explore_home, profile_feed`.
- **Os quatro lugares do Advantage+ num conjunto de público interno:** `advantage_audience = 0`;
  "usar como sugestão" (`targeting_relaxation_types` custom 0, lookalike 0); posicionamento manual
  (com `publisher_platforms`); melhorias do criativo em `OPT_OUT`. E o orçamento fica no conjunto,
  com `is_adset_budget_sharing_enabled = False` na campanha. No caso-base, um único molde monta os
  quatro e confere lendo da conta, na criação e na ativação.
- **A prévia só valida o conjunto de verdade quando a campanha já existe.** O `explore` passou na
  prévia e foi recusado na escrita; a campanha nasceu vazia e o lote parou (o lote para no primeiro
  erro, `sirius-scale/REGRAS.md` §6). Agora, com a campanha na conta, a prévia roda
  `execution_options=["validate_only"]` em cada conjunto.

**O que conferir à mão, conjunto por conjunto de público interno:** (1) card Público sem o selo
"Advantage+ ativado"; (2) "Usar como sugestão" desmarcado, no público personalizado e no semelhante;
(3) posicionamento manual, sem o Explorar antigo; (4) no anúncio, as melhorias automáticas do criativo
desligadas. Na campanha: orçamento no conjunto e sem o compartilhamento de até 20% entre conjuntos.

---

## Anúncio de várias versões com N imagens: anúncios irmãos no mesmo conjunto, não o criativo dinâmico

*(Low ticket do caso-base, uma rodada. VARIAÇÃO ISOLADA: um cliente, uma subida.)*

O pedido era "as 3 imagens juntas, a Meta escolhe". A seção sobre imagem por posicionamento, mais acima, já
mostra que o `DEGREES_OF_FREEDOM` aceita **1 imagem** por criativo, na `link_data`. Pra 3 imagens num anúncio só,
o caminho mais provável é o criativo dinâmico do conjunto (`is_dynamic_creative`); a imagem por posicionamento
(PLACEMENT, seção do `generatepreviews`) também leva N imagens, mas roteadas por posição, não pra Meta escolher.
Nenhum dos dois foi testado pra isso. O dinâmico tem dois problemas:
- junta as 3 artes num nome de anúncio só, e o `utm_term={{ad.name}}` deixa de separar a venda por arte no Dash
  (`sirius-scale/frameworks/trafego/nomenclatura.md` §1: o ID amarra copy, gasto e venda);
- a casa nunca subiu esse modo por API.

**O que foi feito:** 3 anúncios irmãos no mesmo conjunto, cada um com 1 imagem e os mesmos textos
(DEGREES_OF_FREEDOM com 3 corpos, 3 títulos e 2 descrições). A verba é da campanha (CBO), e a Meta divide
entre os anúncios. Cada um mantém o próprio nome no Dash.

No registro da subida, o grupo é "criativos da mesma campanha", com a mesma verba, frente e posicionamento.

**Nome:** a ETAPA `[TESTE]` da `sirius-scale/frameworks/trafego/nomenclatura.md` pressupõe 1-1-1. Com anúncios
irmãos, a campanha `[TESTE]` vira 1-1-3: a leitura por peça é pelo `utm_term`/nome do anúncio. No nível de
campanha, as 3 artes se misturam.

**Medido:** 12 anúncios em 4 conjuntos, 3 irmãos por conjunto, cada um com o próprio nome `AD - IMG NN - …`,
todos lidos da conta.

⚠️ A leitura por arte dentro do grupo é pista, não teste A/B: a Meta concentra a verba na arte que entrega melhor.

**O que conferir à mão:** N artes = N anúncios no mesmo conjunto, cada um com uma imagem, os mesmos textos e nome
próprio (é o nome que separa a venda por arte).

---

## Rodada trocada antes de ligar: arquivar, não apagar

*(15 campanhas de uma rodada de low ticket, criadas pausadas e substituídas pela rodada seguinte antes de rodar.)*

- **ARCHIVED tira da visão normal e guarda o objeto e o histórico.** DELETED apaga.
  ⚠️ **Voltar do arquivado NÃO foi medido.** A documentação da Meta se contradiz:
  - o guia de gerenciar campanhas diz que dá pra restaurar mudando o status;
  - a página "Manage Your Ad Object's Status" diz que, arquivado, o objeto só aceita mudar o nome e ir pra DELETED.
  Até alguém testar numa campanha morta, trate arquivar como "some da tela e não volta pela API". Pra o que pode
  precisar voltar, a escolha é pausar.
- **As travas, lidas da conta, antes de escrever:**
  - o nome bate com o do registro;
  - a campanha está PAUSED (arquivar não é jeito de desligar o que roda);
  - gasto e impressão de vida inteira são zero (`date_preset=maximum`).
  Uma falha barra o lote.
- **Leitura de volta:** `status == ARCHIVED` campanha por campanha, gravado no estado do registro (com a data em
  que foi arquivada).
- **Nome novo na rodada nova:** as campanhas novas continuaram a numeração (05 em diante), em vez de reusar 01–04.
  Assim, a busca por nome do criador não depende do filtro padrão da API pra ignorar a arquivada de mesmo nome.

**Medido:** 15 de 15 lidas ARCHIVED.

**O que conferir à mão:** arquivar só campanha pausada, com o nome certo e com gasto e impressão zerados na vida
inteira; a rodada nova continua a numeração.

---

## Carrossel por API: `child_attachments` com ordem fixa e 1 texto

*(Low ticket do caso-base, um carrossel. A receita de API é UNIVERSAL; usar 1 texto em vez das variações é
decisão de pacote.)*

O que foi gravado e lido de volta do criativo:
- `object_story_spec.link_data` com `child_attachments`, um item por card, na ordem da arte. Cada card leva:
  - `image_hash`;
  - `name` (título do card, até 40);
  - `link` (a página com a UTM);
  - `call_to_action {type: LEARN_MORE, value: {link}}`.
- **`multi_share_optimized: False`:** a Meta não reordena, e o card 1 abre o carrossel. Voltou `False` na leitura.
- **`multi_share_end_card: False`:** sem o card automático do perfil no fim. Voltou `False`.
- **`message` com 1 texto só, sem `asset_feed_spec`.** Carrossel com `asset_feed_spec` (várias opções de texto)
  **não foi testado**: o 1 texto é decisão de pacote, não limite medido da plataforma.
- `link` e `call_to_action` também no nível da `link_data` (o "ver mais").

**Validação:**
- antes de gravar, `create_ad` com `execution_options: ["validate_only"]` dentro do conjunto novo, pela regra da
  seção "`generatepreviews`… não valida imagem", que foi medida no `asset_feed_spec`; no carrossel ela não foi
  medida, só seguida;
- depois, a leitura de volta compara número e ORDEM dos cards pelo hash, título e link de cada um, texto e as duas
  flags;
- o destino de cada card entra na conferência de antes de ativar.

**Medido:** 4 carrosséis relidos da conta: 5 de 5 cards na ordem do registro, as duas flags `False` e 1 texto. Logo
depois de criado, o anúncio fica `PAUSED` com `effective_status IN_PROCESS` (em análise); horas depois, `PAUSED`.

**O que conferir à mão:** as duas opções equivalentes desligadas na tela (a Meta reordenar os cards sozinha e o
card final automático do perfil), a ordem dos cards conferida na prévia, e o link de cada card com a UTM.

---

## Dois fatos medidos numa subida de low ticket

- **O hash de imagem da Meta não é o md5 do arquivo local.** O `image_hash` devolvido pelo upload de uma imagem não
  bate com o md5 do PNG enviado, e o mesmo vale pros 37 PNGs da subida (17 imagens e 20 cards): 0 de 37 com hash
  igual ao md5. Pra provar qual versão subiu, compare o horário do arquivo com o da subida, ou leia a imagem pela
  URL da Meta. *UNIVERSAL (comportamento da plataforma), 37 de 37, só PNG; JPEG não testado.*
  **O mesmo arquivo subido duas vezes também ganha hash diferente:** uma imagem voltou com um
  hash em cada subida, e as duas baixadas pela URL da Meta têm o mesmo md5. Hash diferente entre
  duas campanhas não prova arte diferente; o que prova é baixar as duas e comparar.
  *VARIAÇÃO ISOLADA (1 arquivo, 2 subidas).*
- **Dá pra testar um criador inteiro sem tocar na conta.** O teste troca os módulos do SDK (`facebook_business.*`)
  por uma Meta falsa em memória antes do import. A falsa devolve arquivada na busca, atrasa a listagem e aceita
  falha injetada na leitura de volta e no lote, e o teste roda o fluxo principal do criador de verdade. É o jeito de
  cumprir, em código de escrita, a regra de que checagem nova só conta depois de ser vista passar num caso bom e
  falhar num ruim. Ele também prova que o verificador se verifica: 10 trechos novos tirados de uma cópia, um de
  cada vez, e todos derrubaram algum cenário. *VARIAÇÃO ISOLADA (1 criador; é método de teste, não fato de
  plataforma). Só serve pra quem escreve código de criação pela API.*

## Captação de público interno: quatro fatos de uma subida de Black

*(VARIAÇÃO ISOLADA: uma subida, 2 campanhas, 3 conjuntos, 34 anúncios. O 1º e o 3º são comportamento da Graph v26
medido na conta do caso-base.)*

- **`?ids=a,b,c` foi descontinuado na v26.** Ler vários objetos num pedido só volta "The ids query parameter is
  deprecated in v26.0+". Pra esperar N vídeos ficarem `ready`: sobe todos primeiro e depois lê o status deles em
  passadas, com 45 s entre elas, tirando da lista os que ficaram prontos. Esperar cada vídeo sozinho logo depois de
  subir, consultando a cada 10 s, levou a conta ao erro 17 com 6 vídeos e deixou a conferência de antes de ativar
  sem conseguir ler a conta.
- **Filtro de rodada não se grava no registro.** Um filtro "tirar este criativo só desta rodada" foi aplicado em
  memória, e o salvamento gravou o registro já filtrado: o criativo sumiu das listas de anúncio e de ligar. A rodada
  seguinte, sem o filtro, não criou nada e não avisou. O filtro passou a ser desfeito antes de gravar. Regra de
  código: o que é "só desta rodada" nunca passa pelo mesmo objeto que vai pro disco.
- **Conjunto de conversão nasce com `targeting_optimization_types.detailed_targeting = 1`**, mesmo sem
  `flexible_spec` e com `advantage_audience = 0`. Os conjuntos [PQ] de captação de um lançamento anterior leem
  igual, e o de THRUPLAY da antecipação lê 0. Sem interesse no público não há o que expandir, e o efeito provável é
  nulo. Mas é um quinto interruptor, que não entra na régua dos quatro lugares acima nem na conferência de antes de
  ativar. Desligar num conjunto no ar é editar a segmentação, o que reinicia o aprendizado: decisão do Rodrigo,
  pendente no caso-base.
- **Leitura de volta de rodada que completa um lote já no ar:** só o que a rodada CRIOU tem que estar PAUSED.
  Exigir PAUSED de tudo acusou como problema os 13 anúncios ligados de propósito, e a mesma regra no Google barrou
  uma campanha já ligada, no meio do lote. A conferência passou a marcar o que foi criado na rodada.

## Última edição do conjunto e gasto acima do orçamento do dia

- **`learning_stage_info.last_sig_edit_ts`** do conjunto é o momento da última
  edição significativa, em timestamp Unix. Nos 3 conjuntos de uma Black do
  caso-base deu exatamente a hora da ativação. A leitura diária de tráfego conta
  a regra das 48h a partir dele quando não há mexida registrada
  (`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §5). Se mudança
  de verba conta como "significativa" não foi medido. *UNIVERSAL (campo da API);
  o exemplo é VARIAÇÃO ISOLADA.*
- **Gasto do dia acima do orçamento diário não é erro de configuração.** Um
  conjunto de público de alunos de uma Black gastou 162% do orçamento diário no
  1º dia, parcial e em aprendizado. As fontes divergem sobre o limite: a
  documentação da API fala em até 25% a mais num dia, e fontes de terceiros
  (blogs especializados em anúncio da Meta) falam em 75% e num teto semanal de 7×
  o diário. A leitura que vale: "uso do orçamento" acima de 100% num dia isolado
  não diz que a verba está errada; o que segura é o teto semanal. *VARIAÇÃO
  ISOLADA (1 conjunto, 1 dia).*
- **Ligar anúncio que nunca rodou e mexer 30–40% na verba não moveram a última
  edição significativa.** Os três conjuntos de vídeo dessa Black passaram por
  isto, e todos seguiram com `learning_stage_info.status = SUCCESS` e o
  `last_sig_edit_ts` na hora da ativação:
  - uma rotação que ligou três vídeos que nunca tinham gastado ali;
  - uma arte nova ligada em dois conjuntos;
  - três mexidas de verba, incluindo um −40%.

  A página oficial de edições significativas lista "adicionar anúncio novo"
  (`sirius-scale/frameworks/trafego/radar-plataformas.md`). O que se mediu é o
  campo da API, não o custo: a leitura diz que o conjunto não voltou pro
  aprendizado, e não diz que o anúncio novo entra sem fase própria de
  exploração. Dois conjuntos criados na mesma semana seguiam em `LEARNING`, com a
  última edição na criação. *VARIAÇÃO ISOLADA (3 conjuntos, 1 conta, 1 semana).*
- **Editar o texto de um anúncio no ar troca o post.** O anúncio aponta pra um
  criativo novo, e a prova social do post antigo fica com ele. No caso, um vídeo
  da Black tinha quase mil reações e dezenas de compartilhamentos (insights por
  anúncio, `actions` `post_reaction` e `post`). Texto novo num criativo que já
  roda entra como **anúncio novo ao lado** (versão com sufixo,
  `sirius-scale/frameworks/trafego/nomenclatura.md` §1, regra 2), e o antigo
  continua entregando enquanto o novo passa pela análise. *VARIAÇÃO ISOLADA.*


## Gastar mais num horário: aumento programado × horário de entrega

**Medido num low ticket do caso-base** (6 das 7 compras entre 0h e 7h, e o Rodrigo pediu "gastar mais de
madrugada ... nas campanhas que já rodam"). *UNIVERSAL (regra da plataforma), 1 ocorrência.* Docs lidos no dia:
Pacing and scheduling, High Demand Period e Advantage campaign budget.

| Caminho | Funciona com | O que faz | O que travou aqui |
|---|---|---|---|
| **Aumento programado de orçamento** (`/budget_schedules`, "high demand periods") | orçamento **diário** | soma verba numa janela de **3 h ou mais**; o resto do dia segue no orçamento normal; até 50 janelas, total até 8× o diário; janela **não repete** (uma por dia) e a doc não traz editar nem apagar | a conta precisa da capacidade `CAN_USE_BUDGET_SCHEDULING_API`, e a conta do caso-base **não tinha** (lido em `capabilities`) |
| **Horário de entrega** (ad scheduling, `adset_schedule`) | orçamento **total** (`lifetime_budget`) e data de fim | o conjunto só entrega nos blocos: minuto cheio, 1 h no mínimo, dias 0 (domingo) a 6, `timezone_type` `ADVERTISER` (fuso da conta) ou `USER` | nada: com orçamento na campanha, `pacing_type: ["day_parting"]` vai **na campanha** e o `adset_schedule` no conjunto; passou na validação a seco e na leitura de volta |

1. **Campanha que já roda com orçamento diário não ganha horário.** O tipo de orçamento não muda depois de criado
   (erro `1487164`, seção "Anúncio de janela curta"). O caminho foi a gêmea: campanha nova com a mesma peça, o mesmo
   nome de anúncio (o `utm_term` segue igual) e orçamento total com horário.
2. **Na criação:** a programação vai em blocos no formato da Meta, exige orçamento total e data de fim; campanha e
   conjunto são validados a seco antes de criar, e o horário é lido de volta (a ativação barra horário perdido).
3. **A leitura diária de verba trabalha com orçamento diário.** Ela lê `daily_budget`: a campanha com orçamento
   total fica sem proposta de verba (só relata), e quem aplica a verba escreve só `daily_budget`. Campanha com
   horário de entrega fica fora dessa régua, e isso precisa estar dito no plano.
4. **Rate limit na criação:** as 3 campanhas pediram backoff de até 300 s duas vezes. Criar em horário de pouco uso e
   não somar leituras paralelas na mesma conta enquanto o criador roda.
5. **O orçamento total não se divide igual por noite** (*VARIAÇÃO ISOLADA*, 1 noite, 2 campanhas). Na primeira noite de
   uma prorrogação, as duas gêmeas gastaram de 1,7 a 1,9× a média planejada por noite. O total da vida segura o gasto
   do período, mas quem lê por noite vê o começo alto. Pra julgar a peça, usar o gasto acumulado contra a régua, não a
   média da noite.

**O que conferir à mão:** horário de entrega só existe com orçamento total e data de fim, por isso a campanha diária
que já roda não ganha horário (a saída é a gêmea); conferir os blocos de horário e o fuso no conjunto antes de ligar.

## Lista de ligar velha no registro: ativar em lote religa o que a troca de criativo pausou

*(VARIAÇÃO ISOLADA: um caso, a captação de uma Black do caso-base. O fato da leitura de insights é comportamento da
plataforma, medido uma vez nessa conta.)*

**O que acontecia.** A troca de criativo mexia só na conta: ligava a reserva, pausava o caro e lia os dois de volta. A
lista de ligar do conjunto, no registro da fase, ficava como antes, e a ativação em lote liga todo anúncio que está
nela. Ativar depois de uma troca (pra ligar um conjunto novo, por exemplo) religava o que a troca pausou, sem aviso.
Medido: a lista estava parada desde a abertura da captação, e a ativação teria religado 4 criativos no conjunto de
aluno, pausados na rotação da noite anterior, e outros nos de não aluno. Foi alinhado à mão naquele dia.

**O conserto, em dois lugares:**

1. **Na fonte.** A troca lida de volta tira da lista o criativo pausado e põe o ligado, com uma linha no histórico do
   registro. Se o caro não pausou na leitura de volta, a reserva entra mesmo assim: o registro segue a conta.
2. **A trava, que pega a lista velha venha de onde vier** (Gerenciador, outro script, registro editado à mão). Na
   ativação, num conjunto que já está ACTIVE, anúncio PAUSED que a lista manda ligar e que já teve impressão na vida
   inteira conta como trocado e barra o lote inteiro. Anúncio novo, sem impressão, continua ligando. Se a leitura de
   impressão falha, barra também, em vez de supor zero.

**Fato da plataforma que a trava usa.** A leitura de insights por anúncio (`level=ad`) traz linha de anúncio que já
está pausado, com a entrega de antes, e não traz linha nenhuma de anúncio que nunca entregou. Medido no dia seguinte à
rotação: um vídeo pausado horas antes voltou com milhares de impressões, e os criativos que nunca ligaram ali não
tinham linha. A trava faz uma chamada só pras campanhas do registro (`date_preset=maximum`, filtro `campaign.id IN`) e
sem cache. ⚠️ Com `maximum` a leitura não rodou na conta ainda; o que está medido acima veio de um `time_range` da
captação.

**O que conferir à mão:** antes de ativar em lote um conjunto que já roda, comparar o que vai ser ligado com o que está
ligado na conta. Anúncio pausado que já teve entrega foi pausado por alguém: só volta com motivo.

## Análise da Meta: arte aprovada num conjunto não pula a fila no outro

*(VARIAÇÃO ISOLADA: dois anúncios, um dia, conta do caso-base.)*

Dois conjuntos novos de uma Black foram ligados juntos à tarde, cada um com uma arte que já rodava aprovada em outro
conjunto da mesma campanha. Uma saiu da análise em 4 minutos. A outra ficou em `PENDING_REVIEW` cerca de 4h35 e saiu
sozinha, sem `ad_review_feedback` nem `issues_info`. Nesse tempo o conjunto ficou ACTIVE com gasto zero, o que no
relatório parece conjunto sem entrega.

**Quando a análise demora:** o Rodrigo perguntou se valia duplicar. Com 3 h não valia: a cópia entra na mesma fila e,
aprovadas as duas, competem dentro do conjunto. A Meta diz que a maior parte sai em até 24 h. Passou disso, duplicar o
**anúncio** dentro do mesmo conjunto, nunca o conjunto (que dobraria a verba e poria dois públicos iguais no mesmo
leilão), e pausar o que for aprovado depois. Quem confirma é o `effective_status` de cada anúncio, não o do conjunto.

**Texto editado também entra na análise, inclusive o de anúncio pausado** (VARIAÇÃO ISOLADA).

- Uma troca de texto em 30 anúncios foi lida segundos depois de feita:
  - 25 estavam pausados e ficaram `PAUSED` no `status`, mas o `effective_status` deles passou a `PENDING_REVIEW` ou
    `IN_PROCESS`;
  - dos 5 ligados, um já voltou `ACTIVE` na mesma leitura, e os outros ficaram em `PENDING_REVIEW` ou `IN_PROCESS`.
- Isso quer dizer que a reserva editada é analisada enquanto espera, e não só quando liga.
- **Anúncio ligado com texto editado para de entregar até sair da análise** (histórico de atividade da conta e gasto
  por hora):
  - um estático ficou quase 5 h em `Análise pendente`, de madrugada. Era o único ligado no conjunto, e o conjunto parou
    de gastar até ele sair;
  - os outros 4 ligados saíram da análise em até 2 minutos. O tempo muda de anúncio para anúncio: na véspera, esse
    mesmo estático tinha saído em 4 minutos, e o outro é que tinha levado 4h35;
  - por isso, conjunto com um anúncio só fica parado enquanto ele está em análise. De madrugada custa pouco. De dia,
    ligar antes outro anúncio já aprovado no mesmo conjunto.
- **A reserva editada liga sem passar de novo pela análise.** 5 estáticos pausados, editados de madrugada, foram ligados
  à tarde: foram de `Inativo` para `Ativo` em 15 a 20 segundos, sem `Análise pendente` no meio (o histórico registra
  `update_ad_run_status_to_be_set_after_review`), e começaram a entregar 11 a 15 minutos depois.

**O que conferir à mão:** conjunto novo ACTIVE e com gasto zero: olhar o status de cada anúncio antes de concluir que o
conjunto não entrega. Antes de editar texto de dia, ver se o conjunto tem outro anúncio aprovado ligado.

## Botão do anúncio em português: o rótulo de cada tipo, e não existe "Inscreva-se" — *UNIVERSAL (rótulo da plataforma)*

Medido na prévia da própria Meta (`act_<id>/generatepreviews` com `locale=pt_BR`, campo `callToAction.title` do HTML
devolvido, que também traz o catálogo inteiro de 162 botões com o texto de cada um):

| Tipo na API | Aparece em pt-BR |
|---|---|
| `LEARN_MORE` | Saiba mais |
| `SIGN_UP` | Cadastre-se |
| `APPLY_NOW` | Inscrever-se agora |
| `REGISTER_NOW` | Registrar-se agora |
| `SUBSCRIBE` | Assinar |

- **Nenhum botão diz "Inscreva-se".** O roteiro de um vídeo de captação mandava apertar um botão com esse nome; o mais
  perto é o `APPLY_NOW` ("Inscrever-se agora"), e foi o que os vídeos usaram. Roteiro que manda apertar um botão tem que
  usar o nome de um que existe.
- Buscar o rótulo por texto solto no HTML da prévia engana: o pacote de tradução traz todos os rótulos em toda prévia.
  O que vale é o `callToAction.title` ou o par `"<TIPO>":{"name":"<TIPO>","text":{"__html":"<rótulo>"}}`.
- O botão é por criativo: vídeo e estático da mesma campanha podem ter botões diferentes, cada um com o que a peça manda
  apertar.

**O que conferir à mão:** a frase final do roteiro contra o botão que aparece na prévia do anúncio.

## Contagem regressiva: um conjunto por dia, com página, texto e horário próprios — *VARIAÇÃO ISOLADA (a contagem de uma Black do caso-base; montada, ainda não rodou)*

A Meta agenda conjunto, não anúncio. Por isso o "faltam 2 dias", o "é amanhã" e o "é hoje" viram um conjunto por dia.
Aluno e não aluno ficam na mesma campanha, cada um com a página dele. O que cada conjunto leva:

- **Início e fim próprios:** viram `start_time` e `end_time` do conjunto. O conjunto nasce PAUSED com o início no futuro
  e só entrega depois de ativado: nada liga sozinho. Ao criar e ao ativar, os dois horários são lidos de volta contra o
  plano, com 2 minutos de folga, e o resumo de ativação separa o que roda na hora do que começa sozinho depois, com data.
- **Página própria:** a página do conjunto, no link e na conferência do anúncio. Sem ela, vale a da campanha.
- **Texto próprio:** o texto principal do conjunto vence o da campanha, com o mesmo limite de 2.200 caracteres e a mesma
  trava de marca de pendência.
- **Otimização por visita na página (`LANDING_PAGE_VIEWS`):** o conjunto vai com `destination_type = WEBSITE` e sem
  `promoted_object`.
- **Orçamento total, obrigatório em janela menor que 24 h.** A Meta recusa orçamento diário com menos de 24 h entre o
  início e o fim (erro `1487793`, seção "Anúncio de janela curta"). Os três dias da contagem tinham de 13 h a 23 h 59 min,
  e o plano ia com orçamento diário: a prévia da casa passou limpa, porque ela não chama a Meta antes de a campanha
  existir, e a recusa só viria na criação. O conjunto vai com `lifetime_budget`, e a prévia passou a barrar orçamento
  diário em janela curta. A leitura de volta compara o orçamento lido com o do plano, diário ou total.
- **Conjunto de hoje vai sem início:** ele começa na ativação. A janela conta de agora até o fim.
- **Público de envolvimento pela API:** Instagram (`ig_business`, evento `ig_business_profile_all`) ou Facebook (`page`,
  `page_engaged`). A fonte e o id saem de um público de envolvimento que já existe na conta.
- **Limite 17 na leitura de volta.** Uma manhã teve várias leituras pesadas (lista de públicos, anúncios com o criativo
  inteiro, criação de 5 públicos), com a criação e uma prévia de ativação rodando juntas. Aí a leitura de volta da criação
  ficou presa no backoff, com a campanha, os conjuntos e os anúncios já criados. O limite era do usuário ("User request
  limit reached" no `/ads`), não do BUC, que marcava 5%. Liberou em uns 15 minutos. O certo é rodar uma coisa de Meta por
  vez e, se travar depois de criar, conferir o que subiu com uma leitura leve (campanha com `adsets{...}` numa chamada)
  antes de rodar de novo.

**O que conferir à mão:** um conjunto por dia, cada um com início, fim, página e texto do dia; em janela menor que 24 h,
orçamento total; no resumo de ativação, o que roda na hora separado do que começa sozinho depois.

## Religar campanha com o fim vencido: prorrogar antes de trocar o público, e o limite de 30 s — *VARIAÇÃO ISOLADA (2 objetos, conta do caso-base; o mecanismo é da plataforma)*

Medido ao religar duas gêmeas de madrugada de um low ticket, com o fim vencido no mesmo dia:

- **Conjunto vencido recusa também a troca de público**, não só ligar anúncio (o item 2 da seção "Religar campanha
  antiga"): mandar as exclusões no `targeting` deu `3858750 · "O conjunto de anúncios foi encerrado"`. A ordem que
  funciona é prorrogar o fim, depois as exclusões, depois ligar. A proposta tinha sido escrita de madrugada, com o fim
  ainda no futuro, e punha as exclusões primeiro: a ordem de um plano vale pro estado de quando foi escrito.
- **Escrita em lote sem `failure=` falha calada.** A SDK não levanta erro de chamada que falha dentro do lote: sem o
  callback, só a leitura de volta mostrou o problema ("exclusão faltando"), sem o motivo. Lote de escrita imprime o erro
  de cada objeto.
- **`#613`, subcódigo `4841018`: "1 calls per 30 seconds" no mesmo objeto.** A validação a seco (`validate_only`) conta
  como chamada: a escrita de verdade logo depois, no mesmo conjunto ou na mesma campanha, voltou com o 613. Ao prorrogar
  (fim do conjunto e orçamento total da campanha), um dos dois objetos bateu no limite e passou na segunda tentativa.
  Esperar 35 s e tentar de novo só o que voltou com 613.

**O que conferir à mão:** antes de executar um plano escrito horas antes, reler o estado dos objetos. Com o fim vencido, a
ordem é prorrogar, trocar o público e só então ligar.

Ordem medida de novo em conjuntos vencidos que recusaram a exclusão (erro 3858750): primeiro a data nova junto com
`PAUSED`, no mesmo envio (assim conjunto com campanha ligada não volta a entregar sem a exclusão); depois o público; por
último ligar, só se as exclusões estiverem na conta. Na leitura de volta, a campanha com orçamento na campanha mostra o
mesmo fim do conjunto: é derivado, não é erro.

## Leitura de insights e públicos: quatro fatos da API — *UNIVERSAL (plataforma, API v26), cada um medido uma vez*

- **`delivery_estimate` com `estimate_dau` responde erro #12 ("deprecated").** Só sai o MAU.
- **"Please reduce the amount of data you're asking for" em listagem pesada.** A lista de públicos com `rule` e
  `approximate_count` recusou até com `limit` 50. Resolve com o lote da SDK, um objeto por subrequisição.
- **`unique_actions` só trouxe `link_click`.** Visita à página e checkout por pessoa não saem, só por evento. O checkout
  do pixel conta evento: num teste de proporção ele infla o N e o z, e conclusão não se apoia nele.
- **A quebra por texto, título e descrição do anúncio de várias variações cobre só parte da entrega** (num caso: 45% do
  gasto no texto, 26% no título, 0,3% na descrição). Não serve pra escolher texto.

## Anúncio de tráfego criado por API sai sem o pixel no rastreio, e a Meta não credita conversão nenhuma a ele — *UNIVERSAL (mecanismo da plataforma), medido uma vez*

No caso medido, os anúncios de um carrinho apareciam com zero compra, zero início de checkout e zero AddToCart, em todas
as janelas de atribuição, enquanto o pixel recebia as compras e os AddToCart da página.
- **A causa estava no anúncio, não no pixel nem na página.** A campanha de cadastro põe o pixel no `tracking_specs`
  (`offsite_conversion` com `fb_pixel`) sozinha, pelo evento de otimização. A de tráfego (`OUTCOME_TRAFFIC`) ou alcance,
  criada por API, não põe.
- **Sem o pixel no rastreio, o anúncio só mostra o que a Meta mede sem pixel:** clique, visita e engajamento. A coluna de
  compra fica zerada, e o zero não diz nada sobre venda.
- **Antes de ler zero de conversão por anúncio, conferir o `tracking_specs`** (uma chamada pra conta inteira com filtro
  de nome). Na tela é o "Rastreamento" do anúncio, com os eventos do site marcados. O `/preflight` confere (item 11).
- **O que não é afetado:** a venda casada do Dash lê a UTM gravada na venda e não depende do pixel.
- **Quem monta anúncio de tráfego manda o pixel no `tracking_specs`** já na criação, ainda pausado, e lê de volta. A
  validação a seco aceita.
- **Pôr o pixel num anúncio que já roda manda o anúncio pra análise** (ACTIVE → `IN_PROCESS`/`PENDING_REVIEW`, de volta
  em minutos). Em anúncio que já entrega, fazer de madrugada, ou com outro anúncio aprovado no conjunto, e escrever
  primeiro num anúncio só, esperar ele sair da análise e só então seguir com os outros.
- **A Meta deixa ACTIVE o anúncio e o conjunto que já acabaram.** Pra saber se roda, olhar também o fim do conjunto
  (`end_time`). É o mesmo engano do `ENABLED` do Google.

## Editar o mesmo anúncio duas vezes em menos de 30 segundos dá o erro 613 — *UNIVERSAL (limite da plataforma), medido uma vez*

A mensagem diz que o limite é de 1 chamada a cada 30 segundos por objeto (aconteceu com a validação a seco seguida da
escrita de verdade). Não é o erro 17 da conta: esperar 31 segundos e tentar de novo resolveu. E o cache de criativo de
quem cria em lote não pode ter só o nome do anúncio na chave: nome repete entre células, e o anúncio sai com o texto de
outra. A chave é o conteúdo (texto, título, descrição, mídia).
