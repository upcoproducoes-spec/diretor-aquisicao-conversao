# Briefing de Lançamento — especificação e template

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** método
> **Alcance:** UNIVERSAL — este arquivo é **especificação decidida**, não padrão
> extraído. Transfere pra qualquer cliente e qualquer empresa. O que muda de
> cliente pra cliente são os **valores** preenchidos, nunca a estrutura. Ver
> §"O que transfere" no fim.

Este é o documento que dispara a execução de um lançamento. A regra é simples:
**o que está preenchido aqui, o agente executa; o que está vazio, o agente
pergunta — nunca inventa** (`sirius-scale/REGRAS.md` §2).

Vive em `lancamentos/<AAAA-MM-nome>/briefing.md` (perpétuo: `funis/<nome>/briefing.md`).
O modelo em branco, mais curto, pra começar rápido está em `sirius-scale/modelos/briefing.md`;
este arquivo é a especificação completa.

Reverse-engineered da planilha de planejamento de um lançamento real da casa
(um lançamento gratuito do caso de origem). O que já era padrão consolidado lá
foi mantido; o que faltava pra automação rodar sozinha foi acrescentado e está
marcado com **[NOVO]**.

## Por que dois blocos

O briefing tem duas partes com funções diferentes:

1. **Bloco estruturado (YAML no topo)** — campos que o agente (ou um script)
   lê deterministicamente: datas, tags, budget, links, metas. Sem prosa, sem
   ambiguidade. É o que permite gerar UTM, subir campanha e programar disparo
   sem alguém traduzir na mão.
2. **Bloco de contexto (markdown abaixo)** — o que agente de copy precisa pra
   escrever: ângulo, promessa, o que não pode ser dito, aprendizados do
   lançamento anterior.

Se um dado é número, data ou link → vai no YAML. Se é julgamento, contexto ou
instrução → vai no markdown.

---

## Template

Os comentários "ex.:" mostram como o caso de origem preencheu cada campo, em
termos relativos. Copie o formato, nunca o conteúdo.

```yaml
---
# ─────────────────────────────────────────────────────────────
# IDENTIFICAÇÃO
# ─────────────────────────────────────────────────────────────
cliente: nome-do-cliente
expert: Nome do Expert
modelo: LC                       # LC (clássico) | LPSG | perpetuo
tag_lancamento: LC-MESAA         # usada em pasta, UTM e nome de página
                                 # LC/perpétuo: MODELO-MESAA · LPSG: LPSG-S1MESAA
tag_trafego: lc-mesaa            # [NOVO] nomenclatura de campanha — NUNCA leva
                                 # data quando a campanha é contínua (perpétuo/LPSG).
                                 # Ver `sirius-scale/frameworks/trafego/nomenclatura.md`
nome_evento: Nome do Evento

# Pasta na nuvem (Drive) onde as entregas sobem, se vocês usam uma.
# A automação NÃO adivinha esse caminho — lê daqui.
drive:
  projeto: NOME-DO-PROJETO
  lancamento: LC-MESAA           # nome da pasta, sem o prefixo numérico

# ─────────────────────────────────────────────────────────────
# FONTES DE VERDADE — [NOVO]
# Sem isso o agente de copy não tem em que se apoiar e vai perguntar.
# ─────────────────────────────────────────────────────────────
fontes:
  dna_expert: ../../expert/dna-expert.md
  brand: ../../expert/brand.md
  produto: ../../expert/produtos/<produto-principal>.md
  produto_downsell: ../../expert/produtos/<produto-de-downsell>.md
  pesquisa: ./pesquisa.md
  avatar: ./avatar.md
  banco_angulos: ./banco-angulos.md
  debriefing_anterior: ../../entregas/analises/debriefing-<tag-anterior>-<AAAA-MM-DD>.md

# ─────────────────────────────────────────────────────────────
# CRONOGRAMA — formato brasileiro DD/MM/AAAA em todo o briefing
# ─────────────────────────────────────────────────────────────
datas:
  inicio_captacao_organica: DD/MM/AAAA   # ex.: 19 dias antes do CPL1
  inicio_captacao_paga: DD/MM/AAAA       # ex.: 14 dias antes do CPL1 (uma segunda)
  inicio_aquecimento: DD/MM/AAAA         # ex.: no mesmo dia da captação paga
  cpl1: DD/MM/AAAA                       # ex.: segunda
  cpl2: DD/MM/AAAA                       # ex.: quarta
  cpl3: DD/MM/AAAA                       # ex.: quinta
  cpl4: DD/MM/AAAA                       # ex.: domingo (live de encerramento)
  abertura_carrinho: DD/MM/AAAA          # ex.: a segunda seguinte
  liberacao_boleto: DD/MM/AAAA           # ex.: dia 2 do carrinho
  fechamento_carrinho: DD/MM/AAAA        # ex.: dia 3 do carrinho
  inicio_downsell: DD/MM/AAAA            # ex.: o dia seguinte ao fechamento
  fechamento_downsell: DD/MM/AAAA        # ex.: 2 dias de downsell
  aula_boas_vindas: DD/MM/AAAA           # ex.: a segunda seguinte
  debriefing: DD/MM/AAAA                 # [NOVO] data-limite do debriefing
                                         # ex.: 9 dias depois do fechamento
horario_padrao_cpl: "20h"

# ─────────────────────────────────────────────────────────────
# OFERTA — produto principal
# ─────────────────────────────────────────────────────────────
oferta:
  produto: Nome do Programa
  promessa: >
    [O resultado que o avatar quer] em [prazo]
  ticket_cheio: 0.00              # em reais
  escada_carrinho:                # preço muda por dia de carrinho
    - dia: 1
      data: DD/MM/AAAA
      preco: 0.00                 # ex.: ~23% abaixo do cheio
      gatilho: Tsunami + desconto do primeiro dia
    - dia: 2
      data: DD/MM/AAAA
      preco: 0.00                 # ex.: volta ao cheio
      gatilho: Valor cheio + boleto liberado
    - dia: 3
      data: DD/MM/AAAA
      preco: 0.00                 # ex.: cheio
      gatilho: Último dia + replay das aulas
  efeito_tsunami:
    - 20 primeiros — item físico (ex.: apostila impressa)
    - Até 12h do dia 1 — mais tempo de acesso (ex.: 18 meses em vez de 12)
    - Primeiro dia — desconto (ex.: ~23% do cheio)
  bonus: []                       # preencher
  garantia:                       # [NOVO] prazo e tipo — usado em copy de venda
  entrega_produto:                # [NOVO] formato, duração, acesso

# ─────────────────────────────────────────────────────────────
# OFERTA — downsell
# ─────────────────────────────────────────────────────────────
downsell:
  produto: Nome do Produto de Downsell
  nome_evento: Nome do Evento de Downsell - com Nome do Expert
  data: DD/MM/AAAA
  preco_avista: 0.00              # ex.: ~30% do ticket cheio do principal
  parcelamento: 12x 0.00
  promessa: >
    [Entender o que o resultado exige], enxergando exatamente o que [quem
    avalia] procura. [Aprender a fazer] com a lógica de quem [avalia], e não
    com modelo pronto.

# ─────────────────────────────────────────────────────────────
# METAS — [NOVO] vêm do simulador de cenários
# Cenário PROVÁVEL é a meta de trabalho. Otimista e realizável servem
# de teto e piso, não de promessa.
# ─────────────────────────────────────────────────────────────
metas:
  cenario_trabalho: provavel
  budget_total: 0                 # em reais — tráfego + API + SMS
  cpl_meta: 0                     # reais por lead (CPL real, já com o gap de plataforma)
  leads_meta: 0
  conversao_meta: 0               # fração (0.0114 = 1,14%)
  vendas_meta: 0
  faturamento_meta: 0
  roas_meta: 0
  # Premissas — SEMPRE do histórico real do cliente (Dash Fácil = venda real),
  # nunca de benchmark de outra operação.
  premissas_origem: ""            # de onde saíram (debriefing anterior, tela do Dash)

# ─────────────────────────────────────────────────────────────
# TRÁFEGO
# ─────────────────────────────────────────────────────────────
trafego:
  plataformas: [meta, google, display]

  # ═══ OBRIGATÓRIO — regra do Rodrigo ═══
  # Todo lançamento tem uma PLANILHA DE PLANEJAMENTO DE TRÁFEGO POR FASE, e ela
  # é pré-requisito pra subir qualquer campanha de remarketing. Sem ela, a
  # divisão de verba por fase vira percentual herdado — e percentual herdado
  # não sabe se o dinheiro alcança a base na frequência necessária.
  #
  # Modelo: as 5 abas abaixo (a planilha do caso de origem fica fora do kit).
  # Método: `sirius-scale/frameworks/trafego/lancamento-gratuito.md` §3.7
  # Mora na mesma pasta do planejamento e do simulador, numerada em sequência
  # ("3) PLANEJAMENTO DE TRÁFEGO POR FASE - <TAG>"), e sobe como planilha
  # nativa do Google (não .xlsx) pra abrir no celular.
  planejamento_por_fase:
    planilha_local:     # ./planejamento-trafego-<tag>.xlsx
    planilha_drive:     # link da planilha
    documento:          # entregas/analises/planejamento-trafego-remarketing-<tag>.md
    construida_em:      # data
  # As 5 abas obrigatórias:
  #   1) PAINEL       — a conta do investimento ABERTA, item por item (captação,
  #                     remarketing já gasto, plano, API), contra o teto aprovado.
  #                     Total sem as parcelas não é conferível.
  #   2) BASE MEDIDA  — alcance de cada público (delivery_estimate na Meta,
  #                     user_list no Google) e CPM medido por canal. Nada herdado.
  #   3) RÉGUA        — impactos/dia por canal e por fase, e o custo que sai disso.
  #   4) CAMPANHAS    — nomenclatura, objetivo, cap de frequência, público e
  #                     orçamento diário de cada conjunto. É o que se leva pra
  #                     plataforma.
  #   5) EXECUÇÃO     — o que falta antes de subir, com status.

  distribuicao_budget:            # fração do budget total por finalidade
    # ⚠️ ISTO É PONTO DE PARTIDA, NÃO REGRA. A divisão real por fase sai da
    # planilha acima (alcance x frequência x CPM). No caso de origem, a régua
    # herdada de 22,6% pra remarketing não pagava nem o cenário mais magro — o
    # percentual é CONSEQUÊNCIA da conta, nunca o que a define.
    captacao_quente: 0.28
    captacao_frio: 0.42
    distribuicao: 0.15
    api_oficial: 0.06
    contagem_regressiva: 0.03
    aulas_liberadas: 0.03
    carta_vendas: 0.0175
    remarketing_vendas: 0.0175

# ─────────────────────────────────────────────────────────────
# LINKS E UTM
# O padrão de UTM é determinístico — a automação GERA, não copia na mão.
# Ver seção "Padrão de UTM" abaixo.
# ─────────────────────────────────────────────────────────────
links:
  dominio: https://seudominio.com.br
  pagina_inscricao: /inscricao-<tag>/
  pagina_obrigado: /obrigado-<tag>
  pesquisa: https://tally.so/r/<id-do-formulario>
  respostas_pesquisa:             # planilha das respostas
  grupo_whatsapp:
  checkout:                       # um por faixa de preço da escada
  suporte_whatsapp:
  suporte_email:

# ─────────────────────────────────────────────────────────────
# DISPAROS
# ─────────────────────────────────────────────────────────────
disparos:
  canal_principal: api_oficial    # ver `sirius-scale/frameworks/copy/disparo-whatsapp.md`
  plano:
    - assunto: Boas-vindas captação
      tipo: utility
      volume: 10000
      data: DD/MM/AAAA            # ex.: o 1º dia da captação orgânica
    # ... um item por disparo previsto

# ─────────────────────────────────────────────────────────────
# APROVAÇÕES — [NOVO]
# A automação PARA aqui. Nada avança de fase sem aprovação registrada.
# ─────────────────────────────────────────────────────────────
aprovacoes:
  copy: 
  arte: 
  paginas: 
  campanhas: 
  disparos: 
---
```

---

## Padrão de UTM (determinístico)

Extraído do briefing real. Todo link de captação segue:

```
{dominio}{pagina_inscricao}?utm_id={tag}&utm_campaign={tag}
  &utm_source={canal}&utm_medium={medium}&utm_content={local}&utm_term={peca}-pag{A|B}
```

- `utm_id` e `utm_campaign` = `tag_lancamento` em minúsculo (ex: `lc-mesaa`)
- `utm_medium` = `organico` para tráfego orgânico, `pago_meta` / `pago_google`
  para pago
- **Tráfego pago da Meta usa macro, não valor fixo:**
  `utm_campaign` = macro `campaign.name`, `utm_source` = `placement`,
  `utm_content` = `adset.name`, `utm_term` = `ad.name`. Na Meta, cada macro vai
  cercada por chave dupla, dos dois lados; aqui ela aparece sem as chaves só
  porque este arquivo usa chave dupla como marcador de texto.
- `pagA` / `pagB` marca a variante da página em teste

Canais já mapeados: `instagram` (bio, story, direct, live), `facebook`,
`email`, `whatsapp`, `youtube` (live, orgânico), `api`, `manychat`,
`indicacao`, `site`.

---

## O que NÃO vai no briefing

- **Copy pronta.** O briefing dá insumo; a copy é entregável, mora em `entregas/`
  (e sobe pra nuvem, se vocês usam uma).
- **Dado de pesquisa.** Mora em `pesquisa.md` e `avatar.md`. O briefing só aponta.
- **Aprendizado do lançamento anterior em prosa.** Mora no debriefing do
  lançamento anterior (`entregas/analises/debriefing-<tag>-<AAAA-MM-DD>.md`, a saída
  da skill `/debriefing`); o briefing aponta e o agente lê.

## Como a automação usa

| Fase | Lê do briefing | Produz |
|---|---|---|
| Copy | `fontes`, `oferta`, `datas`, contexto | criativos, e-mails, disparos, páginas, CPLs |
| Criação | `links`, `datas`, `trafego` | páginas publicadas, UTMs, campanhas pausadas |
| Acompanhamento | `metas`, `tag_trafego` | leitura de performance vs meta |
| Fechamento | tudo + realizado | debriefing (`/debriefing`) |

O ciclo fecha: o debriefing de um lançamento atualiza as premissas que
alimentam as `metas` do briefing seguinte.

---

## O que transfere e o que é do caso

**Transfere inteiro (é especificação, não observação):** a divisão em dois
blocos e o critério que a governa (número/data/link → YAML; julgamento/contexto
→ markdown), o template de campos, o padrão determinístico de UTM, a lista do
que **não** vai no briefing, e o ciclo briefing → execução → debriefing →
premissas do próximo. Nada disso depende de nicho, expert ou oferta.

**Preencher por cliente (nasce vazio):** todos os valores — datas, tags,
budget, links, metas, ângulo, promessa, o que não pode ser dito. O briefing é
justamente o lugar onde o dado do cliente entra no sistema.

**Do caso (exemplos, não regra):** os comentários "ex.:" do template saem de um
lançamento gratuito do caso de origem. Servem pra mostrar o formato preenchido —
copiar o formato, nunca o conteúdo.

**Em cliente novo, o que muda de verdade:**

- Campos de **modelo de lançamento** (fases, CPLs, carrinho) pressupõem
  lançamento com evento. Cliente de perpétuo/VSL preenche menos e ganha campos
  próprios — quando isso acontecer pela primeira vez, escreva a variante em
  `frameworks-da-casa/` em vez de deixar campo em branco sem explicação.
- As **metas** dependem do modelo de faturamento acertado com cada cliente (ver
  `sirius-scale/frameworks/lancamentos/metas-e-base-de-faturamento.md`, que nasceu
  de uma base contratual de co-produção e não transfere direto).
