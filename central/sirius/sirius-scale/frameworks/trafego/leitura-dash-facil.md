# Leitura do Dash Fácil — Captação (lançamento gratuito)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma (a plataforma aqui é o **Dash Fácil**)
> **Alcance:** UNIVERSAL **dentro do escopo mapeado** — é comportamento da ferramenta, vale pra
> qualquer conta e qualquer cliente de qualquer negócio que use o Dash. Os bugs de tela, o recompute
> e o seletor de lançamento não têm nada do caso-base.
> ⚠️ **O escopo é estreito e isso importa:** §1 a §6 cobrem só **captação** de **lançamento
> gratuito**. **Lançamento pago (LPSG) tem o §8** — o que ler pelo MCP, ligar a pesquisa e as
> armadilhas de pesquisa e `sck`. **Criar lançamento pelo MCP tem o §9**: o MCP só faz a casca e grava
> a conta da Meta num formato que quebra o Dash. **Perpétuo tem mapa parcial (§7)** — janela,
> configuração, funil e a contagem de venda com order bump; faltam, na tela, as abas Origem das vendas
> e Vendas. **Negócio local continua sem mapa.** Em funil desses, refazer o exercício e escrever a
> parte que falta.
> **Do caso:** todos os números e a subconta. Ver §6.

> Mapeado ao vivo na tela, numa subconta do caso-base (um expert de educação), durante a captação de
> um lançamento gratuito. Procedimento e achados técnicos abaixo = **CONSISTENTE** (testado com número
> real na tela, não suposição). Onde o dado é fraco, está marcado.
>
> Os lançamentos gratuitos do caso-base aparecem como **L1 a L4**, em ordem; o mapeamento foi feito
> no L4. §1 a §6 cobrem a fase de **captação** do funil **lançamento gratuito**. §7 cobre
> **perpétuo**. Negócio local ainda não foi mapeado — repetir o mesmo exercício quando for a vez dele.
>
> **Como ler este arquivo no kit:** do lado de vocês, o Dash se lê pelo MCP oficial (§0) e pela tela,
> que vocês mesmos olham. As armadilhas que a casa achou lendo a tela e automatizando o navegador
> continuam aqui porque o MCP lê a mesma API da tela: o que engana na tela tende a enganar no MCP, até
> medir o contrário.

## 0. Como ler o Dash neste kit: pelo MCP

No caso de origem, o Dash foi lido de três jeitos: pela tela, por automação de navegador e scripts
da casa, e pelo MCP oficial. Do lado de vocês existem o MCP (`https://mcp.dashfacil.com/mcp`, ligado
como conector no Claude) e a tela. **Automação de navegador e script da casa não fazem parte do
kit**: onde o original abria uma aba, exportava CSV ou chamava a API interna da tela, aqui está a
ferramenta do MCP que devolve o mesmo dado.

As regras de leitura valem igual (denominadores, armadilhas, o que cada tela significa), porque o
MCP lê a mesma API que a tela usa: no caso de origem, o `captacao_geral` e a API da tela devolveram
os mesmos 10 números na mesma atualização. *VARIAÇÃO ISOLADA (1 conferência).* Por isso, **na
primeira leitura de um lançamento novo, repita a conferência uma vez**: peça o `captacao_geral` e
compare com os cartões da aba Captação na tela. Bateu, o MCP vale pro resto do lançamento.
(`sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md` §2.4 conta como a casa passou a
ler o Dash só pelo MCP.)

| Na tela | No MCP (nome da ferramenta no conector) | Onde está a regra |
|---|---|---|
| Projeto (a subconta), no topo à direita | `listar_subcontas` — quase toda ferramenta pede `subconta_id` | §1 |
| Lançamentos → seletor de lançamento | `listar_lancamentos` (id, nome, datas) | §4.3 |
| Atualizar → Recomputar | `atualizar_dados_lancamento` + `estado_atualizacao_lancamentos` | §4.2 |
| Captação | `captacao_geral` (leads, investimento, CPL, metas, evolução diária) | §2.1 |
| Origem | `origem_captacao` (totais) + `tabela_utm_captacao` (linhas por UTM) | §2.2 e §3 |
| Pesquisa | `pesquisa_lancamento` | §2.3 |
| Remarketing | `remarketing_lancamento` | §2.4 |
| Aulas | `cpls_lancamento` (só leitura; cadastro é na tela) | §2.5 |
| Leads | `leads_lancamento` e `tabela_leads_lancamento` | §2.8 e §4.1 |
| Debriefing e Vendas | `debriefing_lancamento`, `tabela_utm_debriefing`, `pesquisa_debriefing`, `debriefing_por_dia_captacao`, `vendas_lancamento` | §2.6 e §4 |
| Detalhe de uma venda | `rastreio_venda_lancamento` (pelo e-mail) | §4 |
| Editar lançamento | `configuracoes_lancamento` (leitura); `criar_lancamento` e `editar_lancamento` só pra casca | §9 |
| Saúde e "sem dado de anúncio" | `resumo_saude_lancamento`, `diagnostico_anuncios_lancamento` | §4.2 |
| Comparar lançamentos | `metricas_comparativas_lancamento` | §2.1.2.1 |
| Perpétuos | ver a tabela do §7.4 | §7 |

Os nomes são os da época; conferir no conector, porque o Dash acrescenta ferramenta.

Quatro regras de uso do MCP, cada uma aprendida no caso de origem:

1. **Erro é erro, nunca lista vazia.** Se a ferramenta falhar, dizer que falhou. Dado faltando
   tratado como zero é o pior erro de leitura (o CPL do dia sai inflado ou a captação parece parada).
2. **Lista é paginada.** `leads_lancamento` vem de até 100 por página e `tabela_leads_lancamento` de
   até 2.000: pra base inteira, avançar a página até cobrir o `total` antes de contar qualquer coisa.
3. **Fim de período com hora.** Data de fim só com o dia pode fechar o período na meia-noite do
   começo do dia e devolver vazio pro dia de hoje (medido no `vendas_perpetuo`, §7.7). Passar a hora
   no fim (`T23:59:59-03:00`).
4. **Escrita no Dash só com confirmação.** O MCP também cria e edita (lançamento, perpétuo). Antes,
   mostrar o que vai mudar e esperar o ok de quem é dono; depois, ler de volta
   (`sirius-scale/REGRAS.md` §6). Conta de anúncio nunca se cadastra pelo MCP (§9).

## 1. Onde entrar

Na tela:

- `app.dashfacil.com` — canto superior direito, dropdown "Projeto": trocar pra subconta do cliente
  certo.
- Home → **Lançamentos** → selecionar pela tag no dropdown.
- Botão **Atualizar** (topo direito) abre menu com duas opções: "Atualizar" e **Recomputar**. O
  recompute não é instantâneo: a primeira medição deu ~7 min e depois se corrigiu pra segundos
  (§4.2). A bolinha ao lado do nome do lançamento ficou verde o tempo todo nessa medição — não confie
  nela pra saber se terminou, e nunca decida em cima dela (§4.2).

Pelo MCP: `listar_subcontas` → `listar_lancamentos` → conferir id **e** nome do lançamento antes de
ler qualquer número (§4.3). Pra dado fresco, `atualizar_dados_lancamento` e acompanhar em
`estado_atualizacao_lancamentos` até `ok` (§4.2).

## 2. Ordem de leitura durante a captação

### 2.1 Aba Captação (visão geral)

- Confirmar que o lançamento é do tipo certo (gratuito/personalizado).
- Métricas: leads totais, leads qualificados (MQL %), CPA tráfego geral, taxa de resposta da
  pesquisa, distribuição por faixa de leadscore (A/B/C/D).
- CPA dia a dia: na tela, passando o mouse nas barras do gráfico; no MCP, a evolução diária do
  `captacao_geral`.
- Bloco de Meta/Google nativo (dado do próprio gerenciador): usar só como referência — não bate exato
  com o Dash, que é a fonte de verdade real.
- CPM, CTR e conversão embaixo disso.

No MCP, os cartões se dividem em duas ferramentas: `captacao_geral` (leads, investimento, CPL, metas,
evolução diária) e os cartões do `pesquisa_lancamento` (taxa de resposta, MQL %, faixas A–D).

#### 2.1.1 O denominador de cada métrica da tela NÃO é a base de leads — *CONSISTENTE (4 métricas conferidas no mesmo snapshot)*

Medido no L4, reproduzindo os números da tela a partir da lista de leads exportada no mesmo carimbo
de atualização. **Três das quatro métricas usam um denominador diferente do total de leads** —
reproduzir com a base toda dá número errado, e sempre pro lado bonito:

| Métrica na tela | Valor na tela | Fórmula real | Com a base toda daria |
|---|---:|---|---:|
| CPA tráfego | o CPA da tela | investido ÷ leads **pagos** (os pagos eram ~94% da base) | ~6% mais baixo |
| Taxa resposta pesquisa | 68,49% | respondentes ÷ leads **pagos** ≈ 68,1% | 64,0% |
| Faixa A · B · C · D | 5 · 36 · 46 · 13% | cada faixa ÷ **quem tem faixa** (~64% da base) | 3 · 23 · 29 · 8% |
| MQL % | 23,00% | MQL ÷ **quem respondeu** | 14,8% |

A regra por trás: **lead orgânico sai do denominador sempre que a métrica envolve mídia** (CPA e
taxa de pesquisa), e **quem não respondeu sai do denominador sempre que a métrica vem da pesquisa**
(faixa e MQL). Na casa, o MQL já era recalculado com essa regra; as outras três não.

O erro de faixa é o mais grave dos três: A+B lido sobre a base toda dá **26%**, sobre quem tem faixa
dá **41%** — 15 pontos de diferença numa métrica que é leitura de qualidade da base.

⚠️ Sobra ~0,4pp de resíduo na taxa de pesquisa (68,49% na tela vs 68,06% reproduzido). Pequeno e
estável; a hipótese é que o Dash conte algumas respostas que a lista ainda não casou com o lead. Não
foi fechado.

**Onde isso já mordeu:** um relatório diário automático da casa saiu com CPL ~6% abaixo do real,
pesquisa 64% (era 68%) e A+B 26% (era 41%) — corrigido no dia seguinte. **Todo número que reproduza
a tela de Captação a partir da lista de leads (`leads_lancamento`) confere contra esta tabela antes
de sair.** Os cartões do MCP (`captacao_geral`, `pesquisa_lancamento`) já vêm com o denominador da
tela; o erro nasce quando alguém recalcula por conta própria.

#### 2.1.2 O "Valor investido" da tela só conta a fase CAPTACAO, não a tag do lançamento inteira — *CONSISTENTE (2 plataformas, mesmo snapshot)*

Medido no L4, comparando o CPA/Investido da tela com o gasto lido direto da Meta e do Google
filtrando só pela tag do lançamento:

| | Gasto por tag de lançamento (todas as fases) acima da tela do Dash (só CAPTACAO) |
|---|---:|
| Meta | +5,0% |
| Google | +5,7% |
| Total | +5,4% |

A tag de lançamento pega **todas as fases** da nomenclatura
(`sirius-scale/frameworks/trafego/nomenclatura.md` §2, vocabulário de FASE: `CAPTACAO`,
`AQUECIMENTO`, `ANTECIPACAO`) — e `AQUECIMENTO`/`ANTECIPACAO` já rodam durante a janela de captação,
mirando quem já é lead. Filtrando o gasto por campanha pra manter só as que têm `[CAPTACAO]` no nome,
a diferença cai pra ~0,5% (explicado por gasto rodando entre o snapshot da tela e a consulta à
plataforma, não por erro de fórmula) — confirma que **o "Valor investido"/CPA da tela de Captação
exclui AQUECIMENTO e ANTECIPACAO do denominador**, mesmo essas campanhas rodando na mesma janela de
datas.

**Onde isso já mordeu:** o mesmo relatório diário somava o gasto do lançamento inteiro, e o CPL saiu
~4,5% inflado em dois dias seguidos. Corrigido no mesmo dia, filtrando as duas plataformas por
`[CAPTACAO]` no nome da campanha antes de somar. Todo cálculo que reproduza o CPA/Investido da tela
de Captação — e não o gasto total do lançamento — precisa do mesmo filtro. Pelo MCP: o
`captacao_geral` já traz o investido da tela (só captação); o investimento por fase do lançamento
inteiro vem no `debriefing_lancamento`.

#### 2.1.2.1 Segunda confirmação: a tela de "Resultado" também some com o imposto e a ANTECIPAÇÃO — *CONSISTENTE (2 telas do Dash, mesmo lançamento)*

Medido no L4, comparando o gasto da tela de **Resultado** do Dash (diferente da tela de Captação do
§2.1.2, mas mesmo padrão) com o gasto lido da plataforma por tag, todas as fases, com imposto: a
plataforma deu **11,4% acima da tela**.

Quebrando a diferença: ~6,7 pontos são o **imposto de 12,15% da Meta** que o Dash não aplicava (a
tela mostra o valor cru do gerenciador quando o lançamento não soma o imposto; percentual da época,
conferir na fatura), e ~2,0 pontos são a fase `ANTECIPACAO`, que esta tela também deixa de fora —
igual a tela de Captação do §2.1.2 fazia. Tirando as duas coisas, sobram ~2,7 pontos, dentro da
margem de "a tela tirou foto num instante, a plataforma leu depois".

**Confirma, não contradiz:** o padrão do §2.1.2 (a tela do Dash sempre mostra MENOS que o gasto por
tag de lançamento) se repete numa tela diferente do mesmo Dash. Reforça que **qualquer número de
gasto pra decisão de dinheiro usa o gasto real da plataforma, com imposto e todas as fases** — a tela
do Dash serve pra acompanhar rápido, não pra fechar custo real. Do lado de vocês: o gasto real vem do
gerenciador da plataforma (ou de conector, se ligado). Se ele vier pelo Dash, conferir antes se o
lançamento soma o imposto da Meta (`metricas_comparativas_lancamento` diz isso em
`original_meta_tax` e aceita forçar com `aplicar_taxa_meta`; usar o mesmo valor nos dois lançamentos
quando for comparar) e lembrar que a tela de Captação só conta a fase CAPTACAO.

#### 2.1.2.2 Nome de campanha: montar com os códigos que o Dash do lançamento tem — *VARIAÇÃO ISOLADA (1 caso)*

O Dash separa captação, frio e quente pelos códigos gravados no lançamento (`launch_code`, `codigo_captacao`,
`codigo_frio` e `codigo_quente`, que o `configuracoes_lancamento` devolve), casando pedaço do nome da campanha. Os
códigos são os que foram cadastrados naquele lançamento, e podem não ser os da `nomenclatura.md` nem os do padrão
antigo da conta. Nome fora dos códigos cadastrados deixa a campanha fora do investimento da tela (§2.1.2): conferir antes de ligar.
**Gatilho:** antes de escrever nome de campanha, chamar `configuracoes_lancamento` do lançamento e montar o nome com os
códigos que voltarem. Campanha que já está no ar não se renomeia: a `utm_campaign` dos leads novos muda e a série se
divide no Dash.

#### 2.1.3 A planilha da pesquisa conta SUBMISSÃO, o Dash conta PESSOA — *VARIAÇÃO ISOLADA (1 lançamento)*

Medido no L4 cruzando e-mail a e-mail a planilha da pesquisa contra a lista de leads do Dash. As
duas bases **nunca vão bater**, e a diferença é estrutural:

| | |
|---|---:|
| Respostas repetidas (mesma pessoa 2x ou mais), sobre as submissões | **5,5%** |
| E-mails únicos que responderam mas **não existem como lead** | **6,5%** |
| Submissões que não viram "Respondeu pesquisa = Sim" no Dash | **~11,7%** |

Ou seja, **~11,7% da planilha não vira "Respondeu pesquisa = Sim" no Dash** — e isso é o Dash
estando certo, não errado: ele conta *pessoa da base que respondeu*, que é o que importa pra régua
de qualificação. Conferência rápida, numa leitura posterior: submissões × 0,883 ficou a 0,5% do
número de respondentes que o Dash marcava. Fecha.

**Não é teste interno.** A hipótese natural (respostas de teste feitas pela equipe com e-mail falso)
foi checada e é desprezível: **2 registros** em mais de 4 mil, e ainda por cima com e-mail real. Quem
infla é gente respondendo duas vezes e gente respondendo sem estar na base.

**Consequência prática:** nunca comparar o N da planilha com o total de respondentes do Dash como se
fosse a mesma métrica — o acompanhamento da pesquisa usa o N de submissões de propósito (é o que dá
poder estatístico nos cortes), e o relatório de captação usa o do Dash. Os dois estão certos, medem
coisas diferentes.

### 2.2 Aba Origem — "onde mora o segredo"

Na tela: sub-abas **Meta Ads / Google Ads / Orgânico**. Dentro de cada uma, cascata de tabelas em
UTM: **Source → Medium → Campaign → Content → Term → Id**. Cada tabela tem:

- Coluna **Potencial**: bolinha 🔴 (pausar/reduzir verba) / ⚪ (médio, monitorar) / 🟢 (custo por
  MQL bom vs. média geral da captação) / sem bolinha (volume baixo demais pra calcular — ver §3.2).
- Coluna **Veiculação** (Ativa/Pausada) — mostra se aquele nível ainda está no ar.
- Scroll próprio (ver §3.4).
- Botão **Filtros** (topo): Veiculação, UTM·Source/Medium/Campaign/Content/Term/Id — todos
  combináveis.

No MCP: `origem_captacao` traz os totais (leads pagos, orgânicos e sem UTM) e diz quais fontes e
níveis têm dado; as linhas vêm do `tabela_utm_captacao`, com `fonte` (`meta`, `google`, `organico` =
as sub-abas) e `nivel` (`utm_source` … `utm_id` = as tabelas da cascata). O Potencial vem no campo
`potencial`: 1 = 🟢, 0 = ⚪, −1 = 🔴, `null` = sem bolinha (amostra insuficiente). A Veiculação vem
em `status` e `anuncios_ativos`/`anuncios_total`. ⚠️ **Ler só o `origem_captacao` dá "sem dado"
falso**: ele não traz linha nenhuma por campanha.

Uso prático: ordenar por valor gasto ou leads pra achar padrão (no MCP, `ordenar_por`); isolar
plataforma (na tela, filtro de UTM Medium — ver §3.1, é obrigatório a partir do nível Term); filtrar
por data pra ver tendência recente em vez do período inteiro (ver §3.3). Cruzar o CPA daqui com o
gerenciador (Meta/Google Ads) pra ver se bate.

### 2.3 Aba Pesquisa

Mesmo filtro por UTM, dado segmentado por origem. No MCP, `pesquisa_lancamento`: os cartões
(respostas, taxa de resposta, MQL %, faixas A–D) e, por pergunta, cada resposta com quantidade,
percentual, % de MQL e score médio; os filtros de UTM restringem aos leads daquela origem. Só vêm as
perguntas fechadas: as abertas ficam de fora (medido num lançamento de um segundo expert). Pesquisa
× venda é o `pesquisa_debriefing` (§4).

### 2.4 Aba Remarketing

Acompanha as réguas: aquecimento, antecipação, CPLs, carrinho aberto, downsell (ver
`sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3 pra semântica de cada uma). No MCP,
`remarketing_lancamento` (investimento e resultado das campanhas de remarketing, por plataforma).

**Como a aba é montada** — *VARIAÇÃO ISOLADA (1 lançamento lido, 11/2026)*:
- A aba só mostra o que está em `remarketing_config`: uma lista de fases `{codigo, datas: {startDate, endDate}, orcamento}`,
  com as datas em `DD-MM-AAAA`.
- O código casa por pedaço do nome da campanha, nas duas plataformas (`[CPL`, sem fechar o colchete, junta todas as de
  CPL). O código vira o nome do cartão e a chave das tabelas, então cada fase precisa de um código só dela.
- **O MCP não grava remarketing** (§9). Lançamento criado pelo MCP fica com a aba vazia até alguém preencher pela tela, na
  etapa 5 do assistente: Editar → Remarketing no menu da esquerda → adicionar etapa → tag, datas e orçamento. O
  calendário marca o período com dois cliques (início e fim).
- **O botão sem nome no canto da janela é o X e fecha o assistente sem salvar.**
- **O Salvar grava a configuração inteira**, e pode mexer no que você não tocou (no caso medido, o fim do lançamento foi
  pro fim da última fase). Conferir `configuracoes_lancamento` antes e depois, campo a campo.
- O `conteudo_config` usa o mesmo formato de data; o `sales_period` vem em ISO com hora, em UTC.
- **O filtro de data do `vendas_lancamento` anda um dia** (pedido de 06 a 07 trouxe 05 e 06). Peça com um dia de folga e
  filtre pelo `date` da venda. *Fato de ferramenta, 1 medição.*
### 2.5 Aba Aulas

Link das aulas no YouTube — acompanhado ao vivo durante a semana do evento. No MCP, `cpls_lancamento`
(visualizações e retenção de cada aula).

**Como cadastrar (feito numa turma do lançamento pago, 6 aulas) — *VARIAÇÃO ISOLADA*:**
o MCP não cadastra aula (ele só faz a casca do lançamento, §9), então é na tela: Editar → etapa **6
"CPLs"** → "+ Adicionar vídeo" → colar o link → Buscar, uma aula por vez, na ordem → Próxima etapa →
Revisão → **Salvar lançamento**. Os links saem da playlist da turma, não do registro de upload.

- O Buscar consulta o YouTube **direto do navegador**; nada vai pro Dash até o Salvar. Aula agendada
  (ainda não foi ao ar) entra normal e aparece zerada no funil.
- O Salvar manda a **configuração inteira** do lançamento, e não só as aulas, e depois dispara a
  atualização do lançamento. Por isso: ler a configuração antes (`configuracoes_lancamento`), salvar,
  ler de volta e comparar campo a campo. Na primeira vez, só as aulas mudaram (e o estado do
  lançamento passou por "updating" até voltar a "ok", em menos de 1 min); o padrão de `sck` já
  configurado continuou valendo.
- O Dash guarda o recurso do vídeo do YouTube inteiro (título, duração, estatísticas) com um carimbo
  de última atualização. Numa turma anterior, esse carimbo foi regravado de madrugada, depois das
  aulas, então parece que o próprio Dash atualiza os números (*INCONCLUSIVO*, um caso).
- **"Comparecimento" = visualizações da aula ÷ ingressos**, e passa de 100% (243% na aula 1 de uma
  turma) porque o YouTube conta visualização, não pessoa. Não ler como "quantos compradores
  assistiram".

### 2.6 Carrinho aberto → Debriefing / PDF

**Debriefing é a fonte mais completa** — o PDF espelha o Debriefing mas com menos detalhe. Nessa fase
também dá pra puxar a lista de vendas (compradores) e cruzar com leads. No MCP: `debriefing_lancamento`
(cartões, faturamento por tipo de produto, investimento por fase, vendas por faixa, por temperatura e
por MQL; considera o lançamento inteiro, sem filtro de data), com o detalhe em `tabela_utm_debriefing`,
`pesquisa_debriefing` e `debriefing_por_dia_captacao`; a lista de vendas é o `vendas_lancamento`.

### 2.7 Aba Distribuição

Normalmente não configurada num lançamento — pode ignorar.

### 2.8 Aba Leads

- Tabela: Nome, Email, Telefone, Data, Score (A–D), MQL (Qualificado/Desqualificado), Pesquisa
  (Sim/Não).
- Filtros: busca livre, segmento, MQL, Pesquisa, Score, + os 5 UTMs.
- Na tela, o botão **Exportar CSV** baixa a lista. Pelo kit, a lista se lê pelo MCP (§4.1):
  - `leads_lancamento`: lista paginada (até 100 por página) com origem, pesquisa, MQL e score, e os
    mesmos filtros (busca, segmento, MQL, os 5 UTMs).
  - `tabela_leads_lancamento`: os leads do **rastreio** (e-mail, data, página, UTMs, temperatura,
    tipo `paid`/`organic`/`no_utms`, cidade), uma linha por e-mail na primeira captura, até 2.000 por
    página. Só lançamento grátis; pesquisa e score continuam no `leads_lancamento`.

## 2.9 O telefone do lead vive na pesquisa, não na captação — *VARIAÇÃO ISOLADA (1 lançamento medido)*

> Medido cruzando a lista de leads do L3 com a base da pesquisa, durante um diagnóstico comercial.

A aba Leads tem coluna Telefone, mas ela vem quase vazia — e isso muda quem o comercial consegue
abordar:

| Recorte | Com telefone |
|---|---|
| Todos os leads da lista | **15%** |
| Leads da faixa A (os que mais convertem) | **~12%** |
| MQLs | ~14% |
| **Respostas da pesquisa** | **98%** |

O formulário da pesquisa pede telefone; a página de captação não. Some-se a isso que **~71% das
vendas vieram de quem respondeu a pesquisa**, e a conclusão é operacional:

**A carteira abordável por WhatsApp é a base da pesquisa cruzada com a faixa de score — não "a lista
de leads".** Toda régua de contato 1:1 (comercial, recuperação, SDR) tem que sair desse cruzamento,
senão o volume planejado não existe. E aumentar a taxa de resposta da pesquisa deixa de ser só
diagnóstico: vira aumento direto do tamanho da carteira.

⚠️ Um lançamento medido. Se isso é desenho do funil (a captação nunca pede telefone) ou específico do
L3, confirmar no lançamento seguinte antes de tratar como regra.

**No L4 (medido depois):** a captação passou a pedir WhatsApp e mandar pro formulário da pesquisa por
campo oculto, mas com o nome errado (o parâmetro `telefone` × o campo `whatsapp` do formulário), e a
pesquisa ficou com **zero** telefones. Ou seja, o número chegou na ferramenta de e-mail e se perdeu no
caminho até a pesquisa, e por isso o Dash também não teve. Correção e checagem em
`sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §4.1 (o nome do parâmetro tem que ser
o nome do campo oculto do formulário).

## 3. Achados técnicos confirmados (na tela, Meta Ads, no L4)

Medidos na tela. O MCP lê a mesma API; até medir o contrário, trate cada armadilha daqui como
armadilha do MCP também.

### 3.1 UTM Term e UTM Id vêm contaminados por outra plataforma sem filtro de Medium

Sem nenhum filtro, dentro da sub-aba Meta Ads:

| Nível | Total de leads (Source = 100) |
|---|---|
| Source | 100 |
| Campaign | 99 |
| Content | 99 |
| **Term** | **139** |
| **Id** | **147** |

Term e Id vêm inflados — provavelmente porque `utm_term` (e o rollup de `Id`) não é separado por
plataforma, misturando Meta com Google. Aplicando o filtro **UTM·Medium = pago_meta**, o Term caiu
pra **101**, alinhado com o resto.

**Mais grave: o semáforo (Potencial) muda de cor com esse filtro.** De 5 criativos testados, 3
trocaram de verde/verde para cinza/vermelho quando filtrados corretamente — ou seja, sem o filtro de
Medium, o Term pode estar aprovando criativo que na verdade está ruim.

**Decisão (Rodrigo):** tratar como possível bug do Dash, não regra de leitura. **Workaround até o
Dash corrigir:** não usar Term/Id "soltos" pra decisão nenhuma. Usar **Campaign** ou **Content** como
nível de análise principal. Só abrir Term quando precisar ver criativo específico de UMA campanha —
filtrando por aquela Campaign (+ Medium), o Term aí bate certinho (testado: filtrando 1 campanha
específica, Campaign = Content = Term = Id = 17 leads, os quatro batendo).

**Pelo MCP:** o `tabela_utm_captacao` separa por `fonte` (as sub-abas), mas não tem filtro de
Medium — e a contaminação foi medida *dentro* da sub-aba Meta. Então vale o mesmo workaround: `nivel`
= `utm_campaign` ou `utm_content` pra decidir; criativo de uma campanha só, pela lista de leads
(`leads_lancamento` filtrado por `utm_campaign` + `utm_medium`) contando por `utm_term`, e conferindo
que a soma bate com a linha da campanha. Se o `utm_term` de uma fonte somar mais leads que o
`utm_source` da mesma fonte, é a contaminação. *(Caminho pelo MCP não medido no caso de origem:
conferir a soma toda vez.)*

### 3.2 Semáforo só aparece com volume mínimo

Linhas com 0–1 lead não mostram bolinha (fica "-"; no MCP, `potencial = null`). **PADRÃO
INCONCLUSIVO** — não descobrimos o corte exato de volume. Testar em outro lançamento antes de assumir
um número.

### 3.3 Trocar o filtro de data reseta os filtros de UTM

Na tela, mudar o período (ex.: de "Máximo" pra "Últimos 7 dias") limpa qualquer filtro de
Medium/Campaign/etc. já aplicado. **Ordem certa: aplicar filtro de data primeiro, filtro de UTM
depois** — nunca o contrário. No MCP não há filtro que fique gravado: cada chamada leva as próprias
datas e filtros, então a conferência é ver se a chamada levou os dois.

### 3.4 Cada tabela de UTM tem scroll interno próprio

Na tela, as tabelas (Source, Medium, Campaign, Content, Term, Id) mostram ~6 linhas por vez e têm
scroll independente da página. Rolar com o cursor em cima da tabela rola só ela; é preciso rolar com
o cursor fora da tabela (ex.: na borda direita da página) pra página avançar pra tabela seguinte. No
MCP, o equivalente é o `limite` de linhas (padrão 30, até 200): tabela cortada no limite não é a
tabela inteira.

## 4. Aba Vendas (só com carrinho aberto) — ainda não mapeada na tela, mas já sabemos o que olhar

Apontado pelo Rodrigo, ainda não testado ao vivo na tela. Quando abrir, navegar vendas por:

- UTM (mesmo esquema Source/Medium/Campaign/Content/Term/Id da Origem)
- Last click
- Resposta na pesquisa
- Faixa (de score, A–D)
- Temperatura (quente/frio)
- Qualificação (MQL)
- Data de captação (quando o lead entrou, não quando comprou)

Pelo MCP, cada recorte tem ferramenta:

| Recorte | Ferramenta |
|---|---|
| UTM do lead comprador × last click | `tabela_utm_debriefing` com `atribuicao` = `lead` (a UTM de captação; traz leads, investimento, CPL, CPA, ROAS) ou `ultimo_clique` (a UTM gravada na venda; só vendas e faturamento) |
| Resposta na pesquisa | `pesquisa_debriefing` (conversão por resposta) |
| Faixa, temperatura e MQL | `debriefing_lancamento` |
| Data de captação | `debriefing_por_dia_captacao` (coorte pelo dia em que o comprador virou lead, com `vendas_sem_lead`) |
| Venda a venda | `vendas_lancamento` e, pra uma pessoa, `rastreio_venda_lancamento` |

Repetir aqui o mesmo cuidado do §3.1: se o cruzamento por UTM sofrer do mesmo bug de Term/Id, vale o
mesmo workaround (Campaign/Content como nível principal, Term só filtrado por campanha específica).

## 4.1 A lista de leads se lê pelo MCP, não automatizando a tela

A casa automatizou o download da aba Leads pelo navegador e tropeçou três vezes. O caminho não existe
no kit, mas as lições explicam por que a leitura aqui é pelo MCP:

- **Clique que dispara download trava a automação** (ela fica esperando o clique "assentar", o que
  nunca acontece). Vale pra qualquer botão de export, em qualquer site.
- **O botão "Exportar CSV" nasce desabilitado** por um instante depois de abrir a aba Leads, até a
  lista terminar de carregar. Esperar um tempo fixo não basta; é esperar ele habilitar.
- **Com base grande, o export trava em "Exportando…".** Num lançamento com ~10 mil leads, o botão
  buscava ~11 MB de dados em ~25 s e montava o arquivo no navegador; a automação desistia antes. O
  export de **vendas** (~150 linhas) saiu normal: o problema é o tamanho. A casa saiu disso lendo a
  mesma API que a tela chama, fora do navegador, e conferiu campo a campo contra um export oficial:
  todos os e-mails bateram (categoria, UTM, faixa, pesquisa, data). *VARIAÇÃO ISOLADA (1 lançamento,
  1 dia).*

Do lado de vocês, essa API é o MCP: o `leads_lancamento` (paginado, §0) traz o que o CSV trazia. Os
campos que importam pra leitura:

- a categoria do lead: `paid` / `organic` / `no_utms`;
- a temperatura, os `utm_*` e a data de captação;
- se respondeu a pesquisa (Sim/Não);
- **MQL, que só existe pra quem respondeu** (vazio não é "não MQL");
- o score e a faixa de score.

## 4.2 Atualizar o dado: o clique mente, a rede não

O que segue foi medido na tela com a rede do navegador grampeada, depois de uma primeira conclusão
errada: ela tinha sido tirada em cima de um recompute **que nunca chegou a disparar** — a premissa
estava quebrada, não o carimbo.

### O botão "Atualizar" sozinho não puxa dado — *CONSISTENTE*

Ele só expande um menu com duas opções. Quem recalcula é o **Recomputar** de dentro. **Um clique no
Recomputar basta** — repetir não acelera.

### Clique bem-sucedido NÃO é prova de recompute — *CONSISTENTE*

Esta é a armadilha central, e ela custou caro em silêncio.

O botão pode estar **único na página, visível, habilitado**, com tamanho normal; o clique responde
como feito; e **nenhuma requisição sai**. Medido com três jeitos diferentes de clicar. Nenhum falha,
nenhum avisa, e nada acontece.

**A única prova é o efeito:** um recompute de verdade dispara uma chamada de atualização pro servidor
do Dash, que aparece na aba de rede do navegador. Sem ela, não houve recompute.

⚠️ Controle obrigatório ao investigar isso de novo: clique numa aba que sabidamente busca dado (a
Origem dispara 4 chamadas) e confirme que o registro de rede enche. Registro vazio só vale como "não
disparou" depois desse controle.

### O carimbo "Atualizado" É o sinal de que terminou — *VARIAÇÃO ISOLADA (n=1)*

O único recompute que realmente disparou, na primeira medição, moveu o carimbo **~7 minutos** depois
do disparo.

⚠️ **Corrigido no dia seguinte: são segundos, não minutos.** Com o problema da aba resolvido (abaixo)
e o disparo confirmado, o carimbo assentou em **~31 s** numa rodada, e dentro do mesmo minuto do
clique em outra. O Rodrigo já descrevia assim ("aperta, espera uns 10-15 segundos, recarrega").
Aqueles "~7 min" tinham n=1 e quase certamente mediram a ingestão periódica do Dash, não o recompute.

Controle na mesma noite: **10 minutos de leitura, com a página recarregada de verdade a cada
leitura, sem clique nenhum, e o carimbo não mexeu.** Ou seja, ele não fica andando sozinho de minuto
em minuto — quando mexe, mexeu por causa de algo.

Marcado ISOLADA de propósito: é **um** recompute observado. O que sobe pra CONSISTENTE é a próxima
rodada que repetir disparo → carimbo mexeu.

Continua valendo de uma medição anterior, e não foi refutado: o carimbo já foi visto pular sozinho de
madrugada, pouco mais de 2 horas depois, sem clique. Hipótese aberta: ingestão periódica do Dash, em
janela bem mais larga que 10 min. Não atrapalha o uso como confirmação, mas por isso se compara com o
carimbo **de antes**, não com "é recente, logo recomputou".

Duas armadilhas de leitura do carimbo, ainda válidas:

1. **A tela não re-renderiza sozinha.** Sem recarregar a página a cada leitura, quem olha lê a página
   antiga pra sempre e conclui que nunca terminou.
2. **Abrir de novo o endereço em que a página já está não recarrega.** Recarregar é o comando certo.

### O Recomputar SÓ funciona a partir da aba Captação — *CONSISTENTE (reproduzido nos dois sentidos, mesma sessão)*

**Esta é a causa raiz — e ela enterra as duas hipóteses anteriores desta seção.**

Na aba **Leads** o botão "Recomputar" existe, o menu abre, o clique é aceito e **nada é enviado**: o
registro de rede fica vazio. Na aba **Captação**, o mesmo clique, no mesmo navegador e na mesma
sessão, dispara a atualização em 2 segundos.

| Aba | Menu abre? | Clique aceito? | Rede |
|---|---|---|---|
| Leads | sim | sim | **nada** |
| Captação | sim | sim | **atualização disparada em 2 s** |

Foi isso o tempo todo: a automação da casa trabalhava na aba Leads, que é de onde o CSV sai, e
tentava recomputar de lá.

**O que isso derruba, e vale registrar porque as duas custaram tempo:**

1. **Não era cooldown do servidor.** Dois recomputes disparados com menos de dois minutos entre eles,
   ambos aceitos. O Rodrigo já tinha contestado essa hipótese com a experiência dele; estava certo.
2. **Não era botão desabilitado.** Medido no elemento: habilitado, clicável, sem nada por cima.

⚠️ O botão do topo **fica desabilitado por ~5 s depois de cada recarga da página** — isso é real e foi
medido, só não era a causa. Vale saber pra não clicar cedo demais.

**Corolário:** a linha "clique bem-sucedido NÃO é prova de recompute" não só continua valendo como
agora tem explicação — o clique na aba errada é exatamente isso. E "sem a chamada de atualização não
houve recompute" também se sustentou: na aba Leads não havia recompute mesmo.

### O que isso custou de verdade — *dado real*

Uma rodada automática da casa, de madrugada, exportou a base com o lead mais novo do dia anterior —
nenhum lead do dia corrente. Depois de um recompute que de fato saiu, o mesmo export veio **~2,6%
maior**, com os leads do dia.

**~150 leads que o Dash tinha e a rotina não enxergava.** No público de exclusão, isso é exatamente o
lead que continua sendo readquirido a peso de ouro na captação fria. E nada na saída da rotina
denunciava: ela dizia "Recompute disparado", esperava 20 s e exportava.

### Pelo MCP: o mesmo raciocínio

- `atualizar_dados_lancamento` pede ao Dash pra buscar dado novo nas plataformas (`secao`: `tudo`,
  `captacao`, `cpls`, `remarketing` ou `conteudo`) e **roda em segundo plano**: a resposta só diz que
  o pedido entrou.
- A prova de que terminou é o `estado_atualizacao_lancamentos` sair de `updating` pra `ok`. `error`
  não é "sem dado": é ir pro `resumo_saude_lancamento` e pro `diagnostico_anuncios_lancamento`.
- A prova de que o dado ficou fresco é o efeito: o lead mais novo da lista é do período que você quer
  ler, e a contagem mexeu em relação à leitura anterior.
- **Pra ler o dia que acabou de fechar, peça a atualização antes de ler.** Na rotina diária da casa,
  sem isso os inscritos do fim do dia faltavam enquanto o gasto já estava completo, e o CPL do dia
  saía inflado. A rotina espera até 10 minutos pelo `ok`.

**Regra dura: nunca entregar número declarando que o dado é fresco sem a prova na mão.** Dado velho
anunciado como fresco é pior que leitura que falha, porque ninguém vai conferir.

⚠️ A bolinha ao lado do nome do lançamento (verde/amarela) **não serve como sinal** — pelo menos não
do jeito testado. Durante toda a investigação ela ficou verde, inclusive nos minutos seguintes ao
recompute que disparou. Não foi observada amarela nenhuma vez. Pode ser que ela só marque em
recompute manual, ou que a janela amarela seja curta demais pra quem olha de tempos em tempos —
**não testado**, então não decida em cima dela.

### 4.3 O seletor de LANÇAMENTO é o que quebra a leitura automática — *CONSISTENTE (custou uma rodada inteira)*

Numa rodada automática da casa, a lista baixada era **de um lançamento de meses antes**, lida como se
fosse do lançamento em curso. O Dash estava com o seletor de **Lançamento** preso no lançamento
antigo. O seletor de **Projeto** (topo à direita, a subconta) estava certo — o errado era o de
**Lançamento**, no topo à esquerda, logo abaixo do título "Lançamentos".

**Por que passou batido:** a checagem era "o nome do lançamento aparece na página?". O dropdown de
lançamentos fica **inteiro na página** mesmo fechado (todos os lançamentos da subconta), então esse
teste passa **sempre**. O nome estar na página não quer dizer que está selecionado — quer dizer só que
existe.

**A saída não tem erro nenhum.** A rodada diz "OK" e o relatório sai com números plausíveis, de outro
lançamento. É o tipo de falha que só aparece quando alguém abre o arquivo e olha as datas.

**As duas travas que resolvem:**

1. **Ler o estado do seletor no rótulo do botão, não no texto da página.** O botão mostra
   `Lançamento:<tag>` — é a única leitura confiável do estado. E **confirmar a troca depois de
   clicar**, em vez de confiar no clique; abortar se não conseguir (ler lead de outro lançamento é
   pior que não ter dado nenhum).
2. **Conferir o conteúdo depois de ler.** Lançamento em captação recebe lead todo dia; se o lead mais
   recente tem mais de 3 dias, é dado de outro lançamento. Trava independente da primeira, de
   propósito — naquela rodada a tela mentiu e só o conteúdo do arquivo denunciou.

**Pelo MCP:** não existe seletor, mas o mesmo erro aparece com outra cara: o `lancamento_id` errado.
Antes de ler, confirmar id **e** nome no `listar_lancamentos` (o nome é o do lançamento que você quer,
as datas batem com o calendário dele); depois de ler, aplicar a trava 2 (lead mais recente com mais de
3 dias num lançamento que está captando = lançamento errado).

Vale pra qualquer leitura do Dash: **o estado se confirma pelo que a resposta devolve (rótulo, id,
nome, datas, conteúdo), nunca por "o nome aparece em algum lugar".**

## 4.4 O Score e a Faixa NÃO amadurecem com o tempo — *VARIAÇÃO ISOLADA (1 lançamento, 3 snapshots)*

> Medido no L4 comparando três leituras da lista de leads, com 2 dias entre cada, pela MESMA coorte
> de e-mails (~1 mil leads presentes nas três).

A suspeita razoável era que o score fosse acumulando com o engajamento do lead (abertura de e-mail,
clique, visita), e que por isso um lead novo aparecesse artificialmente pior que um lead velho. **Não
acontece.**

| Leitura | A | B | C | D | Sem faixa | Score médio |
|---|---:|---:|---:|---:|---:|---:|
| 1ª | 3,3% | 23,3% | 27,7% | 8,4% | 37,3% | 228,0 |
| +2 dias | 3,4% | 23,6% | 28,5% | 8,6% | 35,9% | 227,9 |
| +4 dias | 3,4% | 23,8% | 28,6% | 8,6% | 35,7% | **228,0** |

Score médio idêntico na terceira casa decimal, 4 dias depois. A única mudança real é a fatia "sem
faixa" encolhendo 1,6pp — são leads que responderam a pesquisa com atraso, não score subindo. No L4 a
taxa de resposta por coorte de dia fica cravada em ~62% desde o primeiro dia: **quem responde,
responde no mesmo dia.**

### O que isso libera

1. **Dá pra projetar conversão com a base ainda em captação.** A foto de hoje é representativa do que
   aquela base vai ser — não precisa esperar fechar a captação pra ler qualidade. É o que sustenta a
   projeção de faturamento pelo mix da base (`sirius-scale/frameworks/trafego/mql-e-qualificacao.md`
   §3.8).
2. **Comparar faixa entre criativos de idades diferentes é legítimo.** Um criativo que subiu ontem não
   está sendo punido por ser novo.
3. **Corolário:** se a faixa de um criativo piorar entre duas leituras, isso é mudança real de público
   entrando — não maturação. Vale investigar.

⚠️ Um lançamento só, e num intervalo de 4 dias dentro da captação. Não diz nada sobre o que acontece
com o score DEPOIS que as CPLs começam, que é quando o engajamento de verdade acontece. Reconferir na
semana das aulas.

## 4.5 Lista de vendas: duas armadilhas que distorcem faturamento e conversão — *CONSISTENTE* (evidência no caso de origem)

A lista de vendas do Dash **não pode ser somada direto** — as duas correções abaixo mudam conversão e
faturamento em dois dígitos percentuais. Medido no CSV da aba Vendas; pelo MCP, o `vendas_lancamento`
lê as mesmas vendas — na primeira leitura, conferir se as duas armadilhas aparecem nos campos de
valor, parcelas e método de pagamento.

**1. Venda de teste entra na contagem.** Linhas com ticket de valor simbólico (o valor de teste de
checkout; no caso medido, sempre Pix e 1 parcela) são teste, não venda. Aparecem em todos os
lançamentos e o Dash as conta em "Vendas totais". Num lançamento com muito teste, elas chegam a uma
fatia relevante das vendas, e um lançamento pode parecer melhor que outro só por ter mais teste de
checkout. Tirar o teste antes de calcular conversão.

**2. "Parcelamento inteligente" guarda o valor DA PARCELA, não o total.** Quando o método de
pagamento é `Parcelamento inteligente`, o campo de valor (no CSV, `Ticket em Reais`) traz a parcela.
O valor cheio é **valor × parcelas** (com juros, por isso acima do preço de tabela). Somar direto
subestima o faturamento e faz parecer que existe um produto barato no mix que não existe. Cartão de
crédito comum **não** tem esse problema — lá o valor já é o total. Regra de cálculo: se o método
contém "parcelamento inteligente" e as parcelas passam de 1, valor cheio = valor × parcelas; senão, o
valor como veio.

**3. Cruzar venda × lead por e-mail mede o buraco de rastreio.** Uma parcela grande das vendas não
casa com nenhum lead daquele lançamento.

⚠️ **Isso mede falta de rastreio, não origem.** O não-casamento tem várias causas possíveis e a lista
não distingue entre elas: comprar com e-mail diferente do cadastro, entrar por caminho que não gravou
UTM, falha de captura. **Não conclua de onde veio a venda que não casou** (por exemplo, "veio da base
antiga") — esse é exatamente o tipo de causa que o dado não sustenta, e o erro já foi cometido e
corrigido pelo Rodrigo. O que o número sustenta é: uma parcela grande do resultado está fora do que o
funil enxerga, e qualquer leitura de origem está trabalhando com o resto.

Com essa ressalva, a conversão do funil de captação (só quem entrou na lista) é o **piso mensurável**.
Isso vale como leitura da **ferramenta** (a lista permite o cruzamento e o número agregado esconde
isso), não como padrão de cliente. Pelo MCP, o buraco já vem contado: o `tabela_utm_debriefing`
separa as linhas `Sem utm` e `Lead não encontrado` (venda sem lead captado), e o
`debriefing_por_dia_captacao` traz `vendas_sem_lead`.

⚠️ **A UTM source da venda vem vazia (`-`) em boa parte das linhas** e não coincide com a origem do
lead. Pra origem, cruzar por e-mail com a lista de leads (que tem a categoria `paid`/`organic`/
`no_utms`), nunca usar a UTM da venda sozinha. No MCP, isso é o `tabela_utm_debriefing` com
`atribuicao = lead`, não `ultimo_clique`.

## 5. Em aberto (não mapeado ainda)

- Aba **Pesquisa** — na tela, só documentamos que existe o filtro por UTM, não navegamos os dados de
  verdade. (No MCP, o `pesquisa_lancamento` já entrega as perguntas fechadas.)
- Aba **Vendas** — ver §4, mapear na tela quando o carrinho abrir.
- Google Ads dentro de Origem: confirmado que a estrutura de tabelas é igual (a Source naquele
  lançamento só tinha `youtube_ads`), mas não testamos os mesmos filtros/bugs do lado Google.
- **Perpétuo:** §7 cobre janela, configuração e funil. Faltam, na tela, as abas **Origem das vendas**
  (a tabela voltava vazia e não se descobriu com que parâmetro ela preenche) e **Vendas**. O §7.7 já
  leu as duas pelo MCP num caso de produto de entrada: a tabela por campanha estava certa; os totais
  do painel, não.
- Negócio local e outros funis — telas e lógica próprias, ainda por mapear.
- Se o bug do §3.1 é só daquele lançamento/conta ou geral do Dash Fácil.
- **Se as armadilhas da tela (§3) aparecem iguais pelo MCP.** A suposição de trabalho é que sim
  (mesma API); falta medir.

---

## 6. O que transfere e o que é do caso

**Transfere pra qualquer conta/cliente (é a ferramenta, não o cliente):**

- **§0** — ler pelo MCP, conferir MCP × tela na primeira leitura de um lançamento novo, erro ≠ lista
  vazia, paginação, fim de período com hora, escrita só com confirmação.
- **§1 e §2** — o caminho de entrada e a ordem de leitura das abas (ou das ferramentas). Muda só a
  subconta e o lançamento.
- **§2.2** — a cascata de UTM (Source → Medium → Campaign → Content → Term → Id), o significado das
  bolinhas de Potencial (no MCP, o campo `potencial`) e o uso dos filtros.
- **§2.9** — telefone do lead vive na pesquisa, não na captação.
- **§3 inteiro (3.1 a 3.4)** — as armadilhas de leitura: Term/Id contaminados sem filtro de Medium,
  semáforo só com volume mínimo, trocar data reseta filtros de UTM, scroll (ou limite) por tabela.
  Custam análise errada em qualquer conta.
- **§4.2 inteiro** — "Atualizar" sozinho não puxa dado; clique (ou resposta) bem-sucedido não é prova
  de atualização; o carimbo (no MCP, o estado `ok` + o dado novo) é o sinal; repetir o Recomputar não
  acelera, e o que travava era a aba errada, não cooldown. Regra de ouro: **auditar pelo efeito, não
  pelo clique** (mesma lógica de `sirius-scale/frameworks/trafego/publicos-e-advantage.md` §4.3 — o
  Advantage+ tem dois interruptores, e se confere por efeito, nunca por campo).
- **§4.3** — o lançamento lido se confirma pelo que a resposta devolve. Marcado CONSISTENTE porque
  custou uma rodada inteira.
- **§4.4** — score e faixa **não** amadurecem com o tempo. Consequência que transfere: dá pra decidir
  com o score da captação sem esperar maturação.
- **§4.1** — a lista de leads se lê pela API (no kit, o MCP), não automatizando a tela.
- **§4.5** — venda de teste, parcelamento inteligente e o buraco de rastreio são da ferramenta.

**Do caso (números e conta), ignorar em cliente novo:**

- A subconta, o lançamento mapeado, os tempos medidos (~7 min de recompute, n=1, depois corrigido
  pra segundos) e os 3 snapshots do §4.4.
- O tempo de recompute é `VARIAÇÃO ISOLADA (n=1)`: em conta com volume muito diferente, remedir
  antes de calibrar quanto esperar.

**O buraco que mais importa pra quem roda outro modelo de funil:** §1–§6 cobrem só captação de
lançamento gratuito. **Perpétuo saiu do escuro (§7)** e o que está lá é da ferramenta, não do caso —
transfere inteiro. **Negócio local** continua sem mapa.

**Da §7, transfere tudo menos os números:** a janela pela data de criação (§7.2), a divergência da
Visão mensal (§7.3), a leitura pelo MCP e a falta de lista de leads (§7.4), a conferência de produto
principal, imposto e filtro de campanha antes de ler número (§7.5), o aviso do pageview de pixel
misturar pago com orgânico (§7.6) e a contagem de venda por produto com order bump, mais as duas
armadilhas de data do MCP (§7.7). **Do caso:** os perpétuos medidos, os produtos e os números.
Nesse caso o certo é repetir o mapeamento ao vivo e escrever a seção nova, não adaptar esta no chute.

---

## 7. Perpétuo — o que foi mapeado

> §7.1 a §7.6 foram mapeados ao vivo num perpétuo de outro negócio (não do caso-base), numa janela
> de ~4 semanas. Produto e números são do caso; **o comportamento da tela é da ferramenta** e
> transfere. O §7.7 vem de 4 perpétuos de produto de entrada do caso-base.
>
> Isto fecha uma parte do buraco anunciado no cabeçalho e na §6 — **não fecha o buraco inteiro**:
> negócio local continua sem mapa, e do perpétuo faltam, na tela, as abas Origem das vendas (tabela) e
> Vendas.

### 7.1 Onde entrar

Na tela: menu lateral → **Perpétuos**. O seletor de perpétuo fica no topo, abaixo do título, no mesmo
lugar onde o de lançamento fica em Lançamentos — e vale a **mesma trava da §4.3**: ler o rótulo do
botão (`Perpétuo:<nome>`), nunca o texto da página, porque a lista inteira está na página mesmo
fechada. No MCP: `listar_perpetuos`, conferindo id e nome.

Sete abas: Saúde · Visão geral · Funil · Origem das vendas · Visão diária · Visão mensal · Vendas (as
ferramentas do MCP de cada uma estão no §7.4).

### 7.2 A janela real é a da criação do perpétuo, não a do filtro de data — *CONSISTENTE (reconciliação fechada em 3 telas)*

**Esta é a armadilha cara.** O filtro de data aceita qualquer período, e o Dashboard geral e a Visão
diária obedecem — inclusive trazendo **vendas anteriores à existência do perpétuo**. A Visão mensal,
não: ela corta na data em que o perpétuo passou a contar.

Medido: pedindo um período que começava ~4 semanas antes da criação, o Dashboard geral mostrou **8
vendas e ROAS 13,21 no mês da criação**. O perpétuo só existia nos últimos dias daquele mês, e na
janela real as vendas do mês eram **zero**. As 8 eram vendas do mesmo produto vindas de outro funil —
uma delas de uma campanha `[TESTE DE CRIATIVOS]` que nada tem a ver.

**Como achar a data de criação** (o Dash não expõe o campo): comparar a Visão mensal com a soma da
Visão diária, dia a dia, até as duas baterem. No caso medido, a mensal do primeiro mês (gasto e
leads) fechou exatamente com a diária **a partir de um dia específico** — o da criação. É aritmética,
não estimativa. No MCP: `visao_mensal_perpetuo` × a soma do `visao_diaria_perpetuo`.

**Consequência prática:** antes de citar qualquer número de perpétuo, reconciliar Visão mensal × Visão
diária. Sem isso, o ROAS que você lê pode ser de outro funil.

### 7.3 A Visão mensal discorda das outras duas telas, e a tela não avisa — *VARIAÇÃO ISOLADA (1 perpétuo)*

Consequência direta da §7.2: no mesmo mês, a Visão mensal mostra **0 vendas** e o Dashboard
geral/Visão diária mostram **8**. Nenhuma das duas está "errada" — elas respondem perguntas
diferentes e nenhuma das telas diz qual. Achado de produto, reportado pro time do Dash.

### 7.4 Ler perpétuo pelo MCP, não pela tela — *CONSISTENTE (a tela não responde a seletor)*

Na tela, as abas do perpétuo vêm grudadas numa leitura automática da página
(`SaúdeVisão geralFunilOrigem das vendas...`), e procurar a aba pelo texto não acha nada. A casa saiu
disso lendo a API que a própria tela chama. Do lado de vocês, essa API é o MCP:

| Aba | Ferramenta do MCP |
|---|---|
| (lista) | `listar_perpetuos` |
| Saúde | `resumo_saude_perpetuo` (e `diagnostico_anuncios_perpetuo` quando não há dado de anúncio) |
| Visão geral | `dashboard_perpetuo` |
| Funil | `funil_vendas_perpetuo` |
| Origem das vendas | `origem_vendas_perpetuo` |
| Visão diária | `visao_diaria_perpetuo` |
| Visão mensal | `visao_mensal_perpetuo` |
| Vendas | `vendas_perpetuo` |
| Configuração | `configuracoes_perpetuo` |

Na API interna da tela, o nome do parâmetro trocava entre abas, e par errado devolvia erro cru, não
erro explicado. O MCP pede sempre `subconta_id` e `perpetuo_id`.

**Não existe lista de leads do perpétuo** — nem na API da tela (testadas 5 variações), nem no MCP. Ou
seja: **em perpétuo não dá pra casar venda com lead por e-mail** — a trava 9 do
`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` (venda casa com lead por
e-mail; quantas não casaram vai escrito) não tem como ser cumprida, e isso precisa ser declarado na
análise em vez de contornado. O MCP tem o `rastreio_venda_perpetuo` (a jornada de um comprador pelo
e-mail: captações, UTMs, páginas, compras); se ele resolve o casamento venda a venda não foi medido.

### 7.5 A configuração do perpétuo é metade do diagnóstico — *CONSISTENTE (2 erros achados de uma vez)*

A configuração (`configuracoes_perpetuo`) devolve o que o perpétuo está de fato medindo. Conferir
**antes** de olhar número:

- **Produto principal** — o perpétuo conta vendas desse produto no período, **venham de onde vierem**.
  No caso medido, ele estava num produto mais caro da mesma conta, num funil que vende outro: o
  painel creditava ao anúncio duas vendas orgânicas de outro produto. Produto errado aqui invalida
  todo retorno da tela.
- **Somar imposto da Meta** — quando desligado, **todo custo do painel está 12,15% abaixo do caixa**
  (percentual da época; a regra do imposto só na Meta já é CONSISTENTE na casa; o novo é o campo onde
  ela se perde). No caso medido, escondia esses 12,15% por 26 dias de operação.
- **Filtro de campanha** — o trecho do nome que liga campanha ao perpétuo. Campanha renomeada some do
  painel sem aviso, e a aba Saúde reporta isso como "sem dados de anúncios", que é indistinguível de
  tráfego pausado.
- **Só a primeira recorrência**, **páginas**, **contas de anúncio da Meta e do Google**.

No MCP de criar e editar, esses campos se chamam `produto_principal`, `somar_imposto_meta`,
`filtro_campanha` e `apenas_primeira_recorrencia`.

### 7.6 O que o funil de perpétuo entrega de graça

`funil_vendas_perpetuo` devolve a cascata inteira já calculada: impressões → cliques → landing page
view → **pageviews do pixel** → leads → checkouts → vendas, com CPM, CTR, CPC, frequência, alcance,
hook rate 3s/15s, custo por pageview, CPL, CPA e ROAS. Traz também o **tempo médio de carregamento
por página, medido nos visitantes reais**, que não existia em nenhuma outra fonte da casa (no caso
medido: quase 8 s, com o HTML pesando 7,2 KB — o gargalo não era servidor).

⚠️ **Os pageviews do pixel incluem tráfego não pago** e costumam superar os cliques do gerenciador
(~27% acima, no caso medido). Taxa de conversão de página calculada sobre eles **mistura pago e
orgânico** — usar, mas declarar.

### 7.7 Criar e configurar perpétuo: MCP pra casca, tela pro resto — *VARIAÇÃO ISOLADA (4 perpétuos)*

Feito em 4 perpétuos de produto de entrada do caso-base:

1. **Casca pelo MCP** (`criar_perpetuo`): nome, produto principal, bumps, filtro de campanha, imposto.
   **Sem contas da Meta** (o mesmo defeito do §9: grava objeto). A resposta não traz o id;
   `listar_perpetuos` dá.
2. **O resto pela tela.** Páginas e ofertas não existem no MCP (nem no `criar_perpetuo` nem no
   `editar_perpetuo`), e conta de anúncio vai pela tela pelo §9. A casa gravou esse resto pela API
   interna da tela, caminho que o kit não usa. Ler de volta sempre (`configuracoes_perpetuo`);
   comparar sem depender da ordem (o servidor devolve as ofertas em ordem alfabética).
3. As opções de oferta que a tela mostra **só trazem oferta que já teve venda**. A API interna
   aceitava código ainda não visto; pela tela, a oferta nova só aparece pra escolha depois da
   primeira venda nela.

**Como ele conta venda, medido com uma compra de teste (produto principal + 3 bumps):** pelo **nome do
produto** (e pela oferta, se as ofertas estiverem preenchidas), **sem ligar o bump à compra
principal**. Com os 4 produtos no perpétuo e as ofertas vazias, os 4 painéis mostraram as mesmas 4
vendas. Com ofertas, o produto principal fica restrito à oferta do tráfego pago (a venda orgânica pela
oferta base fica fora, de propósito), mas **a oferta de bump é uma por produto e se repete nos 4
checkouts**: o bump de um produto vendido no checkout de outro aparece em 3 painéis. Pra cada painel
contar só os próprios bumps, cada checkout precisa de oferta de bump própria (12 ofertas pra 4
produtos).

Depois de ligar a conta, o painel puxou a Meta sem erro.

No dia seguinte a repetição apareceu como previsto: três painéis mostraram 2 vendas cada, os bumps da
mesma compra de teste.

**Medido dois dias depois, com as 3 compras que existiam** (`vendas_perpetuo` dos 4 painéis cruzado
com o histórico de vendas da Hotmart):

- 10 transações viraram 24 linhas nos painéis: **~1,9× o faturamento real**. Todo bump aparece em 3
  painéis, e as 14 linhas a mais são todas de bump. O produto principal nunca repete.
- Dois painéis mostraram faturamento sem nenhuma venda do próprio produto.
- **A tabela por campanha (Origem) está certa**, porque cruza a venda com a campanha pela UTM: a
  campanha mostra só a compra que ela trouxe. O erro está nos totais do painel e na lista de vendas.
- **O Dash conta cada produto como uma venda.** A compra do produto principal com 2 bumps vira 3
  vendas, e o CPA da campanha sai em **um terço** do CPA por compra (investimento ÷ compras). Pra
  decidir verba em produto de entrada com bump, contar só a venda do produto principal (as réguas do
  low ticket estão em `sirius-scale/frameworks/lancamentos/low-ticket.md` §8).
- A compra de teste, já contestada na Hotmart (`PROTESTED`), continuou nas linhas do painel.
- ⚠️ **Ao trocar o produto entregue mantendo o nome (uma mudança de formato, por exemplo), trocar as
  ofertas no mesmo dia.** Mesmo nome de produto com códigos de oferta diferentes: com as ofertas ainda
  nos códigos antigos, a venda nova não entra em painel nenhum.

**Na virada, somar em vez de substituir.** Quando a troca aconteceu, cada perpétuo ganhou as ofertas
novas (a do tráfego pago e os 3 bumps daquele checkout) e os códigos antigos ficaram, porque o
histórico daquele período é deles. O `editar_perpetuo` do MCP não tem ofertas, então a casa gravou
pela API interna da tela, um perpétuo por vez e com o objeto inteiro. Na leitura de volta só as
ofertas mudaram, e o `vendas_perpetuo` do período deu as mesmas linhas antes e depois.

⚠️ **`vendas_perpetuo` com a data de fim só com o dia devolve vazio pro dia de hoje.** A data sem hora
fecha o período na meia-noite do começo do dia: os 3 painéis deram `total: 0`. Com `T23:59:59-03:00`
no fim, deram as 2 vendas de cada. Pra ler o dia, passar sempre a hora no fim.

⚠️ **`funil_vendas_perpetuo` com o início no dia D devolveu D−1 e D juntos.** As visitas diárias
vieram com os dois dias, o gasto também, e o tempo médio de carregamento misturou os dois (deu ~4,6 s;
o dia D sozinho, subtraindo, deu ~7,8 s). Com início e fim no dia anterior, veio só aquele dia —
porque o dia antes dele não tinha visita (o perpétuo tinha acabado de nascer). Antes de usar o total,
conferir o detalhe diário da resposta. **É o dia anterior inteiro** (medido nos 4 perpétuos, uma
consulta por dia em 4 dias seguidos: cada consulta trouxe o dia pedido e o anterior, onde havia
visita). Pra ler um dia: consultar D e D−1 e subtrair (total = média × visitas). VARIAÇÃO ISOLADA.

---

## 8. Lançamento pago (LPSG) — pesquisa, sck e leitura

> Mapeado ao vivo numa turma do lançamento pago do caso-base (tipo `paid` no Dash). Números são do
> caso; **o comportamento é da ferramenta** e transfere. O modelo de lançamento está em
> `sirius-scale/frameworks/lancamentos/lpsg.md`.

### 8.1 O que ler, pelo MCP

| O quê | Ferramenta |
|---|---|
| Lista de lançamentos | `listar_lancamentos` |
| Configuração | `configuracoes_lancamento` |
| Captação (cartões) | `captacao_geral` |
| Origem | `origem_captacao` (totais) → `tabela_utm_captacao` (linhas) |
| Pesquisa | `pesquisa_lancamento` |
| Ingressos (no pago, o "lead" é quem comprou o ingresso) | `vendas_lancamento` (o próprio MCP manda usar ele no pago; o `tabela_leads_lancamento` é só lançamento grátis) |
| Debriefing | `debriefing_lancamento` |
| Aulas | `cpls_lancamento` (leitura); o cadastro é na tela (§2.5) |

⚠️ Na API da tela, as tabelas de Origem e de Pesquisa chegavam **vazias** na primeira resposta e
vinham numa segunda chamada; ler só a primeira dava "sem dado" falso. No MCP a armadilha tem outra
cara e a mesma lição: o `origem_captacao` não traz linha por campanha; as linhas estão no
`tabela_utm_captacao`.

### 8.2 Ligar a pesquisa: é na tela, pelo botão "Planilhas" — *VARIAÇÃO ISOLADA (1 vez, lida de volta)*

O botão "Planilhas" (Editar → 4 Pesquisa) abre o **seletor de arquivos do Google**, que pede login na
conta Google de quem clica. A casa contornou o seletor gravando a pesquisa pela API interna da tela
(o agente não faz login no Google), caminho que o kit não usa: do lado de vocês, quem tem acesso à
planilha clica "Planilhas" uma vez. O que vale pros dois caminhos:

1. O **servidor** do Dash só lê a planilha pelo id, sem esse login, nos dois casos do §9 (escolhida
   pelo seletor, ou com o link aberto).
2. Depois de salvar, a tela dispara a atualização do lançamento; a pesquisa entrou em ~30 s. Ler a
   configuração antes e depois (`configuracoes_lancamento`) e conferir que nenhum outro campo mudou.

**A regra de MQL com várias perguntas é E** (todas as perguntas com resposta marcada) — conferido em
32 de 32 respondentes (ver `sirius-scale/frameworks/trafego/mql-e-qualificacao.md` §1).

### 8.3 Planilha de pesquisa compartilhada entre turmas + Tally = cartões gerais errados — *VARIAÇÃO ISOLADA*

O Tally grava a data da resposta na coluna **"Submitted at"**, que o Dash **não reconhece** como data
de resposta (a tela avisa "as respostas da sua pesquisa não possuem data de resposta registrada").
Sem data, o filtro de período não se aplica — e como a planilha do lançamento pago era a mesma havia
meses, entre turmas, os cartões gerais somaram todas as turmas: **taxa de resposta de 1.059% e MQL
38%** num lançamento de poucas dezenas de ingressos. O que casa por e-mail fica certo: resposta **frio
74% · quente 75%**, MQL frio/quente, e as colunas Pesquisa/MQL de cada ingresso. Ler por Frio/Quente,
pela lista de ingressos ou por Origem; nunca pelos dois cartões do topo. Não renomear a coluna na
planilha do Tally sem testar — a integração do Tally escreve por cabeçalho.

### 8.4 Checkout direto com origem só no `sck`: o Dash credita a venda à origem ANTIGA da pessoa — *VARIAÇÃO ISOLADA*

O single shot manda o comprador direto pro checkout, com a origem no `sck`
(`<tag>|campanha|posicionamento|mídia|conjunto|anúncio`) e sem `src`/UTM. Com o **padrão de sck** não
configurado (botão amarelo "Padrão de Sck" na Origem), o Dash não lê essa origem e **usa a UTM com que
a pessoa entrou num lançamento anterior**: as vendas de single shot apareceram como orgânicas, como
campanhas do lançamento gratuito anterior ou como "sem UTM". O CPA do Dash saiu **34% acima** do real.
Conserto: configurar o padrão no botão "Padrão de Sck" — o que o modal grava é o separador `|` e a
ordem `utm_id`, `utm_campaign`, `utm_source`, `utm_medium`, `utm_content`, `utm_term`. As vendas que
passam pela página (`src` com UTM) não dependem disso.

**Configurar o padrão não resolve tudo (medido depois, mesma noite):** o Dash passou a ler o sck (as
vendas sem rastreio caíram a zero), mas **só usa o sck quando a pessoa não tinha origem anterior**.
Quem já era inscrito de outro lançamento na mesma subconta segue com a origem de quando entrou na base
— 11 das 17 vendas de single shot (10 eram inscritos do lançamento gratuito anterior). O `src` da
página passa por cima da origem antiga; o sck, não. **Conserto definitivo: o link direto de checkout
levar também o `src` no formato da página** (`posicionamento|campanha|mídia|conjunto|anúncio|id`), na
criação da campanha — trocar link de anúncio no meio da turma não compensa.

**Consequência pra qualquer lançamento pago com link direto de checkout:** conferir a Origem contra a
Hotmart (`purchase.tracking.source_sck`, pelo MCP da Hotmart ou pela tela dela) no primeiro dia; se
venda de campanha nova aparecer com UTM de lançamento velho, é o sck.

---

## 9. Criar lançamento pelo MCP: o que ele grava e o que quebra

> Medido num lançamento do caso-base criado pelo MCP. *VARIAÇÃO ISOLADA (1 lançamento)*; o defeito é
> da ferramenta, então transfere pra qualquer conta. O MCP muda: antes de confiar, conferir se
> continua assim (lendo a configuração de volta).

**O MCP só cobre a casca do lançamento.** `criar_lancamento` e `editar_lancamento` aceitam nome, datas
da captação, investimento planejado, metas de lead, moeda e contas de anúncio. Não existe parâmetro
pra tag, tipo, códigos de fase (captação, frio, quente, orgânico), páginas, pesquisa, MQL, imposto da
Meta, remarketing ou conteúdo. A própria descrição da ferramenta manda configurar o resto "depois no
app". Lançamento criado só pelo MCP fica sem dado nenhum até alguém completar.

**O MCP grava a conta da Meta num formato que o Dash não lê.** O parâmetro pede objeto (`{id, name}`)
e o MCP grava o objeto como veio. O app grava texto:

| Campo | Gravado pelo app | Gravado pelo MCP |
|---|---|---|
| contas da Meta | `["act_<id>"]` | `[{"id": "act_<id>", "name": "<nome da conta>"}]` |
| contas do Google | `[{"id": "<id sem traço>", "mcc_id": null, "name": "…"}]` | `[{"id": "<id com traço>", "name": "…"}]` (com traço, sem `mcc_id`) |

Efeito medido:

- a atualização monta o endereço da API da Meta com o objeto inteiro
  (`graph.facebook.com/…/{'id': 'act_…', 'name': '…'}/campaigns`) e para com erro 400 (code 100,
  subcode 33);
- a tela do assistente quebra no seletor de contas da Meta (aparece `[object Object]`).

Mandar só o texto (`["act_…"]`) pelo MCP não passa: a validação recusa antes de gravar. Esvaziar as
contas pelo MCP destrava a tela. Mas a atualização segue em erro (`object of type 'NoneType' has no
len()`) enquanto a tag, os códigos e as páginas estiverem nulos.

**Regra prática:**

1. Pelo MCP, só nome, datas, investimento e metas. **Nunca contas de anúncio.**
2. Conta, tag, códigos, páginas, pesquisa, MQL e imposto, só pela tela.
3. Ler a configuração de volta (`configuracoes_lancamento`) e conferir o estado depois da primeira
   atualização (`estado_atualizacao_lancamentos`). `ok` é o sinal.

Toda escrita pelo MCP segue `sirius-scale/REGRAS.md` §6: mostrar o que vai mudar, esperar o ok de
quem é dono, ler de volta.

**Como a casa consertou o lançamento quebrado (lido de volta):** regravou só os 11 campos que
faltavam (contas, tag, tipo, códigos, imposto, páginas e conteúdo) no formato do app, pela API interna
da tela, e os 11 voltaram iguais na leitura. Antes de gravar, conferiu que a página era o Dash e que o
lançamento lido era o certo. Do lado de vocês, o mesmo conserto é pela tela: esvaziar as contas pelo
MCP destrava o assistente, e o resto se preenche lá. Isso vale só pra destravar lançamento quebrado:
com a conta já certa pela tela, esvaziar pelo MCP desfaz o conserto (abaixo).

**Medido de novo num lançamento de outro expert da casa, em outra subconta: nada mudou.**

- `editar_lancamento` com contas da Meta gravou o objeto de novo. Mandar a lista vazia pelo mesmo MCP
  desfez, com leitura de volta.
- O schema da ferramenta continua sem tag, tipo, códigos, páginas e imposto.
- Lançamento recém-criado pelo MCP já nasce com estado de erro (`object of type 'NoneType' has no
  len()`).

**A regra 1 vale pro Google, e vale pra tirar a conta.** No mesmo lançamento, a conta do Google foi
ligada pelo `editar_lancamento`, com esta seção já escrita:

- O Dash gravou a conta com traço e sem `mcc_id` (`{"id": "<id com traço>", "name": …}`), e a
  atualização caiu em `INVALID_CUSTOMER_ID`. Pela tela (abaixo), tirar a conta, marcar a certa debaixo
  da MCC e salvar: voltou `{"id": "<id sem traço>", "mcc_id": "<id da MCC>", …}` e o estado `ok`.
- Horas depois o Google tinha sumido de novo (a leitura mostrava a lista de contas do Google vazia): o
  `contas_google: []` mandado pelo MCP pra desfazer o primeiro erro apagou o conserto da tela. Foi
  religado pela tela. **Pelo MCP, nem pra tirar a conta: tirar também grava.**

**Conta de anúncio pela tela.** O assistente de edição tem 8 etapas: Geral, Captação, Grupos,
Pesquisa, Remarketing, CPLs, Conteúdo e Revisão.

- Caminho do Google: Editar → Geral → "Contas Google Ads" → a conta certa, debaixo da MCC → Próxima
  etapa até a Revisão (as outras etapas passam sem mexer) → Salvar lançamento. Ler de volta: o estado
  passa por `updating` e chega em `ok`.
- Na Geral, a busca de contas acha pelo número da conta. O imposto da Meta é um interruptor que
  aparece depois de escolher a conta.
- Na Captação, a página e o orgânico são campos de etiqueta (digita e Enter). Meta de leads e orçamento
  são obrigatórios: sem planejamento, entram provisórios e se trocam depois pelo `editar_lancamento`,
  que grava esses dois sem problema.
- O que a tela gravou voltou certo na leitura: conta como texto (`act_…`), códigos, página, imposto e
  estado `ok`.

Efeito colateral esperado: o início geral do lançamento recua pra data mais antiga entre as fases (no
caso, a antecipação começava um dia antes da captação e puxou o início um dia pra trás). O início da
captação não muda.

**Pesquisa: o servidor do Dash só lê a planilha em dois casos.** O primeiro é ela ter sido escolhida
no botão "Planilhas" da tela, no seletor do Google, com o login Google de quem clica. O segundo é ela
estar com o link aberto pra qualquer pessoa. Fora disso, a leitura das perguntas devolve erro 500 com
"File not found" do Google Drive, mesmo com a planilha no mesmo drive compartilhado e com as mesmas
permissões das outras. Medido com três planilhas do mesmo cliente; a permissão que existia a mais na
que funcionava era "qualquer pessoa com o link pode ler".
⚠️ Planilha de pesquisa tem nome, e-mail e WhatsApp. Abrir o link é decisão do dono, não atalho
técnico. O caminho sem expor dado é alguém clicar "Planilhas" uma vez.

Não ligar a pesquisa na configuração enquanto o Dash não ler a planilha: a atualização tentaria abrir
o arquivo e o lançamento poderia voltar pro estado de erro.

---

## 10. Ler o Dash pelo MCP e o que ele faz com a UTM do Google

**Limite por minuto do MCP (*UNIVERSAL da ferramenta, medido 1 vez*):** 5 lotes em paralelo (71 chamadas) devolveram 11
com "Limite de chamadas por minuto atingido. Aguarde alguns segundos e tente de novo." O erro chega como erro da
ferramenta, não como HTTP 429. Refeitas uma por vez, todas voltaram. **Regra:** lote do Dash roda em sequência, não em
paralelo; o que bater no limite, espera um minuto e refaz só aquela chamada.

**O MCP do Dash é API de dados, e o Claude chama ele direto.** Sem perfil de navegador, sem seletor
de lançamento, sem export. No caso de origem, a leitura pelo MCP foi **conferida contra a tela**: os
mesmos 10 números da API que a tela usa (§0). *UNIVERSAL (ferramenta), 1 conferência.* Três hábitos
que a casa fixou:

- numa leitura, só ferramentas de leitura; escrita é outro passo, com confirmação (§9);
- a lista de leads paginada se junta inteira antes de contar (§0);
- erro vira erro declarado, nunca lista vazia.

**A UTM do Google chega crua na URL e o Dash troca por nome.** Com o padrão de UTM do Google da casa
(`sirius-scale/frameworks/trafego/nomenclatura.md` §3, regra 7), a URL do inscrito leva os ids:
`utm_campaign` = id da campanha, `utm_content` = id do anúncio, `utm_term` = id do grupo. Nos campos
`utm_*` do inscrito, o Dash grava os **nomes**:

| Campo no Dash | Meta (igual à URL) | Google (traduzido pelo Dash) |
|---|---|---|
| `utm_campaign` | nome da campanha | nome da campanha |
| `utm_content` | nome do **conjunto** | nome do **anúncio** |
| `utm_term` | nome do **anúncio** | nome do **grupo** |

Medido na Black do caso-base:

- nos inscritos pagos do Google, o `utm_campaign` cru casou com as 3 campanhas do registro;
- na URL, o id numérico do anúncio; no Dash, o nome do anúncio (`AD - <criativo> - <gancho>`);
- 72 de 72 inscritos da Meta com o campo igual à URL.

Consequências:

1. **Pra casar inscrito com custo no Google, usar o id cru da URL** (o campo de página do lead, que
   guarda a URL com a query), não o nome. Nome de anúncio se repete entre campanhas (três anúncios
   rodavam em duas campanhas, com ids diferentes).
2. **O nome do anúncio fica em TERM na Meta e em CONTENT no Google**, então comparar criativo entre as
   duas plataformas não cabe numa coluna só (ver `sirius-scale/frameworks/trafego/_metodologia.md`
   §3.2).
3. **Inscrito pago sem UTM:** um inscrito com categoria `paid`, sem `utm_medium` e com `gad_campaignid`
   na URL conta como pago no cartão do Dash. Casar ele pela campanha desse id. (A lista do MCP,
   `leads_lancamento`, separa pago de orgânico por `utm_medium`; o cartão separa pela categoria — por
   isso os dois podem divergir num ou noutro inscrito.)
4. **Macro da Meta que não resolve:** 1 inscrito pago da Meta (de 73) chegou com o `utm_campaign` e o
   `utm_content` trazendo o texto cru da macro (`campaign.name` e `adset.name`, ainda entre as chaves)
   e só o `utm_term` (anúncio) resolvido. Não dá pra saber o conjunto, e o anúncio roda em dois. Não
   casar ele com unidade nenhuma; avisar no relatório, sem inventar. *VARIAÇÃO ISOLADA (1 caso).*

## 11. Lead que o pixel não pegou: reimportar — *VARIAÇÃO ISOLADA (1 vez, lida de volta)*

**O caso (na Black do caso-base):** o gerenciador de tags que carregava o script de rastreio do Dash
nas páginas foi publicado vazio (uma versão com zero tags). O Dash pegou o último lead de madrugada e
ficou dois dias contando ~1 lead por dia, com a captação normal (a Meta contou dezenas de leads no
mesmo dia). Quem viu foi o Rodrigo, olhando o gráfico. Diagnóstico de fora, sem acesso ao gerenciador
de tags: baixar o `gtm.js?id=<container>` e procurar `dashfacil` no arquivo; no navegador, conferir
nos recursos carregados pela página (`performance.getEntriesByType('resource')`) se aparece
`server.dashfacil.com`.

**Reimportar:**

1. A fonte é a cópia de cada inscrição que a página guarda fora do Dash (no caso de origem, um
   armazenamento da própria hospedagem das páginas, com nome, telefone e as 6 `utm_*`, uma chave por
   horário UTC + e-mail). Cruzar com o `leads_lancamento` do MCP pelo e-mail e pelos 8 últimos dígitos
   do telefone; sobe só quem não está lá. Data em horário de Brasília (o horário guardado é UTC).
2. Formato: o modelo do próprio Dash (`app.dashfacil.com/import-models/modelo-importacao-de-leads.csv`):
   `Email,Nome,Telefone,Data da criação,utm_campaign,utm_source,utm_medium,utm_content,utm_term,utm_id,url`,
   data no formato `dd/mm/aaaa`, telefone com 55, `url` = página + as UTMs na query (é por ela que o
   lead cai no lançamento certo).
3. Tela `app.dashfacil.com/importacao` → "Importe Leads" → subir o CSV. O mapeamento foi automático
   (pulou da etapa 1 pra 3). Conferir que a importação terminou com sucesso antes de seguir.
4. **O lead só aparece no lançamento depois de `atualizar_dados_lancamento` (seção `captacao`)**. Antes
   disso a contagem não muda e parece que a importação falhou.
5. O Dash junta por e-mail: ~18% das linhas viraram reinscrição da mesma pessoa. Conferir por e-mail
   distinto, não por linha. CSV com dado pessoal fica fora de pasta versionada ou compartilhada.
