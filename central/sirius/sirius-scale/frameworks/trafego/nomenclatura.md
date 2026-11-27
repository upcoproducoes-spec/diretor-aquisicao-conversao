# Framework de Nomenclatura — Tráfego

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método
> **Alcance:** UNIVERSAL — este arquivo é **convenção decidida**, não padrão
> observado num cliente. Não foi extraído de N peças: foi definido como padrão
> da casa. Por isso transfere inteiro pra qualquer cliente e qualquer negócio —
> o risco aqui não é *será que vale fora?*, é *está sendo seguido?*.
> **O que é por cliente:** o vocabulário de `PRODUTO` (a sigla de cada produto)
> nasce vazio em cliente novo e é preenchido a partir do briefing. Os outros
> vocabulários (TIPO, FASE, ETAPA, PÚBLICO) são fixos e não se remontam.

> **Data de corte.** Numa conta que já tem histórico, registre o dia em que este
> padrão passou a valer. Campanhas anteriores seguem o padrão antigo
> (inconsistente) e **não** batem com estes filtros. Ao analisar histórico,
> considerar a data de corte. *(No caso-base foi assim: a conta tinha um padrão
> antigo e inconsistente, e a análise passou a separar o antes e o depois.)*

> **Sobre os exemplos.** Os códigos de lançamento e as siglas de produto que
> aparecem aqui são inventados (`LC-EXEMPLO`, `CURSO`): mostram o formato, não um
> lançamento real. No lugar vão a tag real do lançamento e a sigla do produto que
> o briefing definir.

## Por que isso importa

O nome não é organização — é o que permite o agente **filtrar, analisar e cruzar**
dados. Nome inconsistente quebra análise e quebra o cruzamento com o Dash (que
identifica origem por UTM).

---

## 1. Estrutura por nível

### Campanha

**Lançamento:**
```
[TIPO] [PRODUTO] [CANAL] [TAG-LANÇAMENTO] [FASE] [ETAPA] [PÚBLICO] variação
```
Ex: `[LC] [CURSO] [LC-EXEMPLO] [CAPTACAO] [TESTE] [PF] 01` (Meta)
Ex: `[LC] [CURSO] [YT] [LC-EXEMPLO] [CAPTACAO] [TESTE] [PF] 01` (Google)

**Perpétuo e distribuição** (sem tag de lançamento — não têm edição):
```
[TIPO] [PRODUTO] [CANAL] [FASE] [ETAPA] [PÚBLICO] variação
```
Ex: `[LPSG] [CURSO] [VENDA] [ESCALA] [PQ]` (Meta)
Ex: `[LPSG] [CURSO] [YT] [VENDA] [TESTE] [PQ]` (Google)
Ex: `[DC] [SHORTS] [DESCOBERTA] [TESTE] [PF] 02` (Google)

⚠️ **Distribuição de conteúdo NÃO leva o bloco PRODUTO** (decisão do Rodrigo):
ela é de marca — alimenta o programa principal, o livro e o LPSG igual —, então
`[DC]` vem direto seguido do canal (Google) ou da fase (Meta):
`[DC] [DESCOBERTA] [TESTE] [PF]`, `[DC] [NUTRICAO] [PQ]`,
`[DC] [SHORTS] [DESCOBERTA] [ESCALA] [PF]`. Perpétuo continua com produto.

### CANAL — só no Google

No Meta o bloco não é usado: a conta já é o canal, e posicionamento é config do
conjunto, não identidade da campanha.

No Google é **obrigatório**, porque o tipo de campanha muda o jogo por completo:

| Valor | Tipo |
|---|---|
| `YT` | YouTube |
| `SHORTS` | YouTube Shorts |
| `DISCOVERY` | Demand Gen / Discovery |
| `SEARCH` | Rede de Pesquisa |
| `PMAX` | Performance Max |
| `DISPLAY` | Rede de Display |

⚠️ **Erro que já aconteceu no caso-base — o nome tem que dizer a conversão
real:** campanhas de LPSG no Google estavam nomeadas `[LPSG] [YT] [INSCRIÇÃO] ...`,
mas rastreavam a ação de conversão **Compra** — "inscrição" ali significava compra
de ingresso do evento pago. O nome engana. No padrão, essas campanhas são
`[LPSG] [CURSO] [YT] [VENDA] ...`.

### Conjunto de anúncios
```
00 - [PÚBLICO] detalhe
```
Ex: `00 - [ENVOLVIMENTO IG 30D] Vídeo 01`
Ex: `01 - [ADVANTAGE+] BR 25-55`

Hierarquia numerada (00, 01, 02...) pra ordenar a leitura no Gerenciador.

### Anúncio

> O bloco do slug do ângulo tem data de corte própria. Se a conta tem anúncios
> de antes de o slug ser adotado, eles seguem o formato curto (`AD - VD 01`) e
> não têm slug. Mesma lógica da data de corte do topo.

```
AD - TIPO NÚMERO - SLUG-DO-ANGULO
```
Ex (inventados): `AD - VD 24 - PRIMEIRO-PASSO-CERTO` · `AD - IMG 07 - NAO-TENHO-TEMPO`

O criativo é identificado **aqui**, não no nome da campanha.

**TIPO:** `VD` (vídeo) · `IMG` (estático) · `CAR` (carrossel).

**NÚMERO = ID do criativo.** É o mesmo número no documento de copy, no nome do
anúncio e no `utm_term`. É ele que amarra copy, gasto e venda na análise.

| Onde | Formato | Exemplo (inventado, criativo número 24) |
|---|---|---|
| Documento de copy | `VD<NN> — "título do ângulo"` | `VD` + `24` colados — "O primeiro passo certo de quem está começando" |
| Nome do anúncio | `AD - VD NN - SLUG` | `AD - VD 24 - PRIMEIRO-PASSO-CERTO` |
| `utm_term` | `VDNN-SLUG` | `VD` + `24` + `-PRIMEIRO-PASSO-CERTO`, tudo colado |

`NN` é o número com dois dígitos. No documento de copy e no `utm_term` ele vem
**colado** no `VD`, sem espaço; no nome do anúncio, separado por espaço.

#### Regras do ID

1. **Série por funil, número nunca reciclado dentro dele.** O funil se compara com
   ele mesmo, e o número diz quantos criativos ele já teve: o VD 16 do pago semanal é
   o 16º vídeo dele.
   - A série é a do **TIPO + PRODUTO** da campanha. O lançamento pago semanal tem uma.
     Os lançamentos clássicos do mesmo produto têm uma só, porque a edição não entra
     no ID (regra 3). Cada produto de low ticket tem a sua.
   - Vídeo que roda em dois funis ganha um ID em cada um.
   - **No nome do anúncio o funil não se repete** (`AD - VD 16 - SLUG`): ele já vem da
     tag da campanha.
   - **Fora do anúncio** (arquivo, pasta, documento de copy, catálogo), o ID leva o
     funil na frente: `LPSG VD 16`, `LT-<PRODUTO> VD 05`.
   - **O próximo número livre** sai do catálogo do funil, conferido contra os nomes de
     anúncio da conta.
   - **Anúncio que já roda fica com o nome antigo.** Renomear muda o `utm_term` e parte
     a venda do mesmo criativo em duas linhas no Dash. A ponte entre o número antigo e
     o novo mora no catálogo do funil.
   *(VARIAÇÃO ISOLADA: a regra antiga era série contínua por cliente; voltou a ser por
   funil porque a comparação que importa é funil contra funil.)*
   *(11/2026, VARIAÇÃO ISOLADA: no caso de origem a série repetiu 9 números. Uma leva reservou números só no
   documento dos roteiros, fora de qualquer registro de campanha, e outra subida usou os mesmos. Antes de numerar,
   procurar o número em todo lugar: roteiro ainda não gravado, registro de campanha e nomes de anúncio na conta.)*
2. **Regravação mantém o número e ganha sufixo de versão** (`.1`, `.2`: o 24
   regravado vira o 24.1), nunca um número novo. Corte curto herda o ID:
   `AD - VD 24 - PRIMEIRO-PASSO-CERTO - 15S`. Estático tirado do mesmo ângulo
   herda o slug: `AD - IMG 07 - PRIMEIRO-PASSO-CERTO`.
3. **O ID não carrega lançamento nem plataforma.** Lançamento vem da tag na
   campanha (`[LC-EXEMPLO]`), plataforma vem do `utm_source` e do bloco CANAL do
   Google. O funil é outra coisa: a série é dele (regra 1), então ele vai na frente
   do ID fora do nome do anúncio. A versão 16:9 do YouTube e a 9:16 da Meta são o
   mesmo criativo, com o mesmo ID.
   ⚠️ *Motivo, com caso real:* num lançamento do caso-base, os anúncios foram
   nomeados com o código do lançamento colado no ID na Meta (no formato
   `<LANÇAMENTO>-VD<NN>-...`) e com o código da plataforma na frente no Google
   (`YT-<LANÇAMENTO>-VD<NN>-...`). O mesmo roteiro virou dois criativos
   diferentes no debriefing, e a comparação YouTube x Meta teve que ser remontada
   somando linha por linha na mão. Com o ID limpo, essa leitura sai direta do Dash.
4. **Slug curto, sem acento, sem barra, caixa alta, ligado por hífen.** Até 4
   palavras, nomeando o ângulo, não a headline inteira. Ele vira URL: acento e
   barra sujam o relatório.
5. **Versão de CTA não entra no ID.** Pago, orgânico e conteúdo se separam por
   campanha e por `utm_source`.
6. **Quem define o ID é o documento de copy.** O criativo nasce numerado na copy
   e sobe com o mesmo número. O agente de tráfego nunca renumera na subida.

---

## 2. Vocabulários fixos

Usar **somente** estes valores. Não inventar variação nova sem atualizar este
documento (do lado de vocês, a variação nova se registra em `frameworks-da-casa/`).

### TIPO

| Sigla | Significado | Família |
|---|---|---|
| `LC` | Lançamento clássico | Lançamento |
| `LP` | Lançamento pago (espaçado, 1–2 por mês) | Lançamento |
| `LS` | Lançamento semente | Lançamento |
| `LPSG` | Lançamento pago semanal gravado | Perpétuo* |
| `PP` | Perpétuo geral | Perpétuo |
| `VSL` | Perpétuo com VSL | Perpétuo |
| `LT` | Low ticket | Perpétuo |
| `HT` | High ticket | Perpétuo |
| `DC` | Distribuição de conteúdo | Distribuição |

\* **LPSG é um híbrido.** As campanhas nunca desligam (comportamento de perpétuo),
por isso o nome é estável e não leva tag de edição. Mas cada semana é um ciclo de
conversão próprio, cadastrado no Dash como S1, S2, S3, S4 — a separação semanal
acontece na **análise por período**, não no nome da campanha.

### TAG-LANÇAMENTO
Só para a família Lançamento. Formato: `TIPO-MESANO` — a sigla do tipo, hífen, o
mês em três letras e o ano em dois dígitos, em caixa alta e sem barra.
Molde: `LC-MMMAA`, `LP-MMMAA`, `LS-MMMAA` (MMM = mês, AA = ano).

⚠️ **Uma tag por lançamento, sempre a mesma.** Nunca duas tags pro mesmo lançamento
(erro que já aconteceu: `[LPSG]` e `[LP-MMMAA]` na mesma leva).

### FASE — Lançamento

| Valor | Quando |
|---|---|
| `CAPTACAO` | Traz lead novo |
| `AQUECIMENTO` | Durante a captação, pra inscritos |
| `ANTECIPACAO` | Última semana da captação (contagem regressiva) |
| `CPL01`, `CPL02`, `CPL03`... | Uma por aula |
| `CPL-GERAL` | "Todas as aulas liberadas" |
| `CARTA` | Sábado antes do carrinho |
| `CARRINHO` | Dias de carrinho aberto |
| `DOWNSELL` | Junto do carrinho |

CPL numerado de propósito: permite analisar qual aula segurou mais gente.
Os destinos diferentes da mesma aula ("é hoje", "liberada", "volta pro grupo")
vão no campo de **variação**, no fim do nome — não viram fase nova.

### FASE — Perpétuo

| Valor |
|---|
| `VENDA` |
| `RMKT` |

### FASE — Distribuição de conteúdo

| Valor |
|---|
| `DESCOBERTA` |
| `NUTRICAO` |

### ETAPA

| Valor | Estrutura |
|---|---|
| `TESTE` | 1-1-1 |
| `PRE-ESCALA` | 1-3-1 |
| `ESCALA` | multiplicação da pré-escala |

Variação numérica (teste 2, teste 3) vai no fim do nome, **não** dentro da tag.

### PÚBLICO

| Valor | Significado |
|---|---|
| `PF` | Público frio |
| `PQ` | Público quente |

---

## 3. Regras de escrita

1. **Sem acento e sem barra** nos blocos entre colchetes. `CAPTACAO`, não
   `CAPTAÇÃO`. `LC-MMMAA`, não `LC-MMM/AA`.
   *Motivo:* esses valores viram UTM. Acento e barra viram `%C3%87` e `%2F` na URL,
   sujam o relatório e às vezes quebram parser.
2. Blocos estruturais sempre entre colchetes, na ordem definida.
3. A variação livre (quando houver) vai no **fim**, fora de colchetes.
4. No nome do anúncio, o slug do ângulo segue a mesma regra: sem acento, sem
   barra, caixa alta, hífen no lugar do espaço.
5. **A UTM de uma campanha nova copia o padrão da campanha que já funciona —
   não se reescreve.** Se as campanhas do lançamento usam macro
   (`{{campaign.name}}`, `{{adset.name}}`, `{{ad.name}}`), a nova usa macro
   também. Trocar de padrão no meio do lançamento quebra o cruzamento, e o
   ganho de escrever certinho nunca paga o dado perdido.
   **VARIAÇÃO ISOLADA** — caso-base, um lançamento.
6. **`+` não entra em nome de campanha, conjunto nem anúncio** (*VARIAÇÃO ISOLADA*, medido numa Black do caso de
   origem). A macro `{{adset.name}}` copia o nome pra UTM, o `+` vira espaço, e o inscrito cai fora do conjunto dele
   no Dash. Conferido no item 6 da `/preflight`.
   **UTM escrita à mão codifica espaço como `%20`, nunca como `+`.**
   *Motivo medido:* uma campanha de captação da Meta saiu com a URL montada à mão
   e espaço como `+`. O Dash Fácil aplica `unquote` (converte `%2B`→`+`) mas
   **não** converte `+`→espaço, enquanto o lead entra com a string decodificada
   corretamente. As duas chaves nunca se juntam: na aba Origem a campanha
   apareceu **com gasto e 0 leads**, e o conjunto saiu como
   `01+-+ADVANTAGE++NOVOS+(guia:+semelhante+de+alunos)` — o `+` duplo é a
   assinatura do bug (`%2B` literal + espaço não convertido).
   ⚠️ **O CSV de export não sofre disso** — só a agregação da tela. Se gasto e
   lead divergirem na Origem mas baterem no CSV, procure `+` na UTM.
   **VARIAÇÃO ISOLADA** — caso-base, medido em dois dias seguidos de um lançamento.
7. **Toda UTM de ação de vendas segue um padrão único, o do lançamento de
   referência (regra do Rodrigo: "sempre que for solicitado qualquer criação de
   UTM para alguma ação de vendas, você deve manter o mesmo padrão").** As fontes
   do padrão são a aba `LINKS DO EVENTO` da planilha de planejamento do
   lançamento e os anúncios que rodaram, lidos na conta. Uma Black do caso-base,
   por exemplo, ganhou um doc com um padrão próprio (`{{site_source_name}}`,
   slugs no Google e conteúdo e termo inventados) e teve que ser refeita. Os
   links ficam **na planilha** (aba `LINKS DO EVENTO`), nunca num doc.

   | Canal | utm_source | utm_medium | utm_content | utm_term |
   |---|---|---|---|---|
   | Instagram, bio | instagram | organico | bio | bio01-pag<X> |
   | Instagram, story | instagram | organico | story | st01-pag<X> |
   | Instagram, direct | instagram | organico | direct | direct-pag<X> |
   | Instagram, live | instagram | organico | live | live01-pag<X> (no lançamento de referência saiu st01, cópia da story: desvio) |
   | Facebook | facebook | organico | bio | bio01-pag<X> |
   | E-mail da base | email | organico | base_alunos (base_leads quando a página é de não aluno) | disparo01-pag<X> |
   | Grupos de WhatsApp | whatsapp | organico | grupos | grupo01-pag<X> |
   | YouTube, vídeo/bio | youtube | organico | video ou bio | yt01-pag<X> |
   | YouTube, live | youtube | organico | live | yt01-pag<X> |
   | API oficial | api | organico | oficial_geral | api01-pag<X> |
   | Manychat | manychat | organico | fluxo | fluxo01-pag<X> |
   | Indicação | indicacao | organico | oficial_geral | indicacao-pag<X> |

   - **Fixos:** `utm_id` e `utm_campaign` (no orgânico) são a tag do
     lançamento em minúscula (exemplo inventado: `lc-exemplo`, `black-exemplo`).
     `<X>` é a página: no lançamento de referência era `A` (uma página só); numa
     Black com páginas separadas, `A` (aluno), `NA` (não aluno) e `BIO`. O
     número (`01`) sobe quando a mesma ação se repete com link diferente.
   - **Meta:**
     `utm_id=<tag>&utm_campaign={{campaign.name}}&utm_source={{placement}}&utm_medium=pago_meta&utm_content={{adset.name}}&utm_term={{ad.name}}`.
     É `{{placement}}`, não `{{site_source_name}}`. Medido nos 54 anúncios de
     captação do lançamento de referência, lidos na conta. O remarketing desse
     lançamento usou `{{site_source_name}}` com termo fixo: é outro desenho, não
     é o padrão de captação.
     A UTM vai num lugar só: no `url_tags` ou no link do criativo, nunca nos
     dois. Link copiado de criativo antigo vai sem os `utm_*` dele
     (`meta-criacao-tecnica.md`, "A UTM mora no criativo").
   - **Google, com as variáveis do próprio Google (ValueTrack):**
     `utm_id=<tag>&utm_campaign={campaignid}&utm_source={network}&utm_medium=pago_google&utm_content={creative}&utm_term={adgroupid}`.
     No Dash, esses ids viram nome nos campos do inscrito: `utm_content` = nome do anúncio e `utm_term` =
     nome do grupo, o contrário da Meta (`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §10).
     Um link só serve pra toda campanha, como as macros da Meta. Correção do
     Rodrigo, com o exemplo de um lançamento pago anterior:
     `utm_id=<TAG>&utm_campaign={campaignid}&utm_source={network}&utm_medium=pago_google&utm_content={creative}&utm_term={adgroupid}`.
     Ele achou estranha a primeira versão dos links de uma Black, com os nomes
     escritos à mão.
     ⚠️ No lançamento de referência, os anúncios do Google saíram com os nomes
     escritos à mão (`youtube_ads`, nome da campanha codificado). Isso foi
     desvio, não padrão: ler a conta mostra o que rodou, e o padrão é o que o
     Rodrigo definiu. Na dúvida entre os dois, pergunta. O slug em caixa alta
     que um renomeador antigo da casa gerava também não é o padrão.

   **Regra do Rodrigo.** O padrão saiu de um lançamento inteiro do caso-base,
   conferido na conta e na planilha. Vale pro caso-base; em cliente de outro
   negócio, pergunta antes. Do lado de vocês: é o ponto de partida, e quem
   decide o tráfego confirma antes de adotar.

---

## 4. O DNA atravessa dois frameworks

O método DNA (Descoberta, Nutrição, Aquecimento) **não** vive todo em distribuição
de conteúdo:

- **Descoberta** → público frio, constrói base → `DC`
- **Nutrição** → público quente (quem já chegou: engajou, segue, viu vídeo, é
  lead), mantém a base aquecida → `DC`, como `[DC] [NUTRICAO] [PQ]`
- **Aquecimento** → inscritos de um lançamento específico → é fase de **lançamento**

*(Correção registrada: uma versão anterior dizia que descoberta e nutrição eram
as duas de público frio. O briefing da distribuição do caso-base trata nutrição
como quente, e o registro das campanhas de distribuição diz "nutrição só atinge
o quente", decisão do Rodrigo.)*

### Regra de calendário (importante)

| Momento | Descoberta | Nutrição | Aquecimento |
|---|---|---|---|
| Entre carrinho fechado e próxima captação | roda forte | roda forte | — |
| Começou a captação | manter, reduzir verba ou pausar **[em aberto]** | **pausar** | foco total |

⚠️ Não deixar nutrição rodando junto da captação — ela briga por atenção com o
aquecimento.

**[EM ABERTO]** Se a descoberta deve continuar, reduzir verba ou pausar durante a
captação ainda não está definido. Testar e atualizar aqui (do lado de vocês, em
`frameworks-da-casa/`).
*(O registro da distribuição do caso-base já adota "descoberta continua no piso"
da faixa de verba durante a captação, marcado como INCONCLUSIVO por ter 1
lançamento observado. A pergunta segue aberta como regra geral até mais
lançamentos.)*

---

## 5. Onde isso é decidido

Todos esses valores (tipo de funil, produto, tag, fase) são definidos no
**briefing do lançamento/funil** (`lancamentos/<AAAA-MM-nome>/briefing.md`, ou a
pasta do funil em `funis/<nome>/`). O agente nunca deve adivinhar nenhum deles —
se faltar no briefing, pergunta.

---

## 6. O que transfere e o que é do caso

**Transfere inteiro (é convenção, não observação):** a estrutura de nome por
nível, os vocabulários fixos (TIPO, FASE, ETAPA, PÚBLICO), as 6 regras de ID de
criativo, a amarração copy ↔ anúncio ↔ `utm_term`, as regras de escrita (sem
acento, sem barra) e a regra de calendário do DNA. Nada disso depende de nicho,
expert ou oferta — depende de a análise conseguir cruzar dado depois.

**Preencher por cliente (nasce vazio):** o vocabulário de `PRODUTO`. Cada
cliente tem os seus, vindos do briefing. Não reaproveitar sigla de outro
cliente.

**Do caso (caso-base, ignorar em cliente novo):**

- A história da data de corte da conta do caso-base (padrão antigo e formato
  curto de anúncio, sem slug). Cliente novo que já nasce no padrão não tem legado
  pra conciliar; cliente que já tem campanhas registra a própria data de corte
  (topo deste arquivo).
- O erro das campanhas `[LPSG] [YT] [INSCRIÇÃO]` — eram campanhas específicas
  daquela conta. A lição que fica é a do bloco FASE: o nome diz a conversão real.
- O caso dos IDs com lançamento e plataforma colados (`<LANÇAMENTO>-VD<NN>` na
  Meta x `YT-<LANÇAMENTO>-VD<NN>` no Google) é **exemplo**, não regra: a regra que
  ele sustenta (ID não carrega lançamento nem plataforma) é universal e fica.
- A nota sobre LPSG ser híbrido pressupõe que o cliente roda LPSG. Cliente que
  não roda esse modelo simplesmente não usa a sigla.
