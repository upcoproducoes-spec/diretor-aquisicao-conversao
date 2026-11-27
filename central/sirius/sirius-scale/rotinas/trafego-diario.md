# Rotina de tráfego diária

> Guia pro Claude seguir, a pedido: "Crie a rotina de tráfego seguindo
> `sirius-scale/rotinas/trafego-diario.md`". É o desenho de
> `sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md`, adaptado pros conectores. Testada uma vez à mão,
> com os conectores, numa Black do caso de origem, e corrigida com o que apareceu. **Nunca rodou agendada nem
> fora da casa:** a primeira semana é de conferência, com alguém lendo o relatório contra a tela.

Todo dia, no horário marcado, o Claude lê o que fechou, roda o preflight, aplica a régua e deixa um relatório
com o que sugere mexer. Ele nunca aplica nada. Serve pra quem já está fazendo essa leitura à mão e cansou: quem
ainda não faz, comece com o agente `gestor-trafego` numa conversa.

## Antes de criar

1. **Conectores:** Dash Fácil e Meta ligados. Google, se a conta rodar Google (`sirius-scale/instalacao/google-ads.md`).
2. **Um `rotinas.json`** na pasta de cada lançamento em andamento (modelo em
   `sirius-scale/modelos/rotinas.json`). É ele que liga e desliga a rotina: uma rotina serve pra todos, e
   lançamento novo é só um arquivo novo. Nunca crie rotina com o nome do lançamento. Funil perpétuo ainda não
   entra nesta rotina: a leitura dele é pedida ao `gestor-trafego` numa conversa.
3. **Um `briefing.md`** com país, idade mínima e decisões temporárias (modelo em
   `sirius-scale/modelos/briefing.md`). Sem isso, três itens do preflight saem NÃO VERIFICADOS todo dia.
4. **Teto de verba** escrito no `CLAUDE.md`.
5. **Uma rodada à mão:** rode a `/preflight` numa conversa antes. Se ela não fecha aqui, não vai fechar sozinha.

## Como criar

Crie uma tarefa agendada com o nome `trafego-diario`, todo dia às 5h, com a pasta do sistema como pasta de
trabalho, e o texto abaixo como instrução, sem mudar nada. 5h porque o dia anterior já fechou e assentou nas
plataformas. Em notebook, que dorme de madrugada, use um horário em que ele costuma estar aberto, de manhã
cedo. Se a ferramenta de criar tarefa agendada não existir na sessão, mostre o passo a passo: na aba
Code do app, abrir as tarefas agendadas, nova tarefa, colar o texto.

Depois de criar, rode uma vez à mão com alguém olhando. Toda ação vai pedir permissão na primeira vez. Permitam
sempre as leituras dos conectores e só estas três coisas além delas: o `atualizar_dados_lancamento` do Dash, o
`curl` que baixa a página e gravar em `entregas/analises/`. Rodada curta e sem resumo quer dizer que parou pedindo
permissão. A máquina tem que estar acordada e com o app aberto no horário: computador dormindo não roda.

## A instrução da tarefa

```
Rotina de TRÁFEGO DIÁRIA. Você carrega o método. Os números moram no rotinas.json de cada lançamento. O que o relatório de ontem concluiu não vale como verdade hoje: confira de novo.

PASSO 0. Quem está em fase hoje
Leia os rotinas.json de lancamentos/. Trabalhe só em quem tem fase com inicio <= hoje <= fim e "trafego" nas rotinas da fase. Arquivo com data fora do formato ou sem o id do Dash fica de fora: diga qual e por quê. Ninguém em fase: responda "Nenhum lançamento em fase hoje." e pare.

PASSO 1. Saúde da conta
Siga .claude/skills/preflight/SKILL.md inteiro. O que acusar abre o resumo. Item que não deu pra ler vira NÃO VERIFICADO, nunca OK.

PASSO 2. Dado novo
Pra cada lançamento em fase:
1. Em configuracoes_lancamento, anote atualizacao_cap e add_meta_tax.
2. Peça atualizar_dados_lancamento, com secao captacao. Sem isso, os inscritos do fim do dia podem faltar com o gasto já completo.
3. Leia configuracoes_lancamento de novo até atualizacao_cap mudar, no máximo 10 minutos. Espere lendo de novo, sem comando de sleep longo, que pode ser bloqueado. Se estado_atualizacao_lancamentos mostrar error, ou o Dash pedir login ou não responder, diga isso no topo do relatório e siga só com o que veio das plataformas, sem calcular custo por lead.
Leia, do início da fase até ontem, passando data_inicio e data_fim com T23:59:59-03:00 (as datas do Dash podem diferir das da fase):
- captacao_geral e pesquisa_lancamento, pelos denominadores do Dash (sirius-scale/frameworks/trafego/leitura-dash-facil.md §2.1.1).
- tabela_utm_captacao, por fonte e nível. Meta: utm_campaign é a campanha, utm_content é o conjunto, utm_term é o anúncio (a descrição da ferramenta diz outra coisa; vale esta). Google: utm_campaign é a campanha, utm_content é o anúncio, utm_term é o grupo.
- Criativo dentro do conjunto: a tabela não cruza conjunto com anúncio. Use leads_lancamento, um par por chamada, e leia só o total. Essa ferramenta traz nome, e-mail e telefone: nunca copie isso pro relatório.
- Gasto por campanha, conjunto e anúncio na Meta e no Google, do dia que fechou e do acumulado da fase.

PASSO 3. A régua
Leia sirius-scale/frameworks/lancamentos/rotinas-de-lancamento.md §5 e sirius-scale/frameworks/trafego/otimizacao-em-tres-niveis.md. O que está em frameworks-da-casa/ vale mais.
As linhas de cada segmento estão em segmentos no rotinas.json: unidade é o conjunto na Meta e a campanha no Google, e o segmento sai de filtro_no_nome. Linha null: mostre o número ao lado das irmãs e não sugira subir nem cortar por ela.
Regras que você não fura:
- Lead vem do Dash. Hoje parcial não decide.
- Gasto da Meta sempre com imposto. Com add_meta_tax ligado, o gasto do Dash já vem com imposto: use ele. Sem isso, some o percentual de sirius-scale/frameworks/trafego/leitura-dash-facil.md e diga qual usou. verba_dia e o teto são com imposto; orçamento sugerido sai no valor que se digita no Gerenciador, sem imposto.
- Custo por MQL decide verba, nunca o CPL sozinho. Sem pesquisa, ou com menos de 25 respondentes na unidade, vale o CPL, e o relatório diz isso. "Qualifica mais" só com teste z.
- Corte só com volume. Nunca proponha pausar uma frente inteira pelo número de um dia.
- Uma mexida por objeto por dia, contada da última edição real: updated_time do conjunto na Meta, change_event no Google.
- Orçamento, público e criativo, sempre os três, com o criativo antes da verba. Públicos disponíveis: ads_get_ad_account_custom_audiences.
- Compare só com a irmã de mesma fase.
- Verba dentro de verba_dia do rotinas.json e abaixo do teto do CLAUDE.md. Passou, vira decisão do dono da verba, com o número.

PASSO 4. Relatório
Salve em entregas/analises/trafego-<lançamento>-<AAAA-MM-DD>.md, com a data, as contas lidas e a fonte de cada número. No topo, um "Resumo do dia" de no máximo 10 linhas, em português informal e sem jargão:
- saúde da conta (o que o preflight acusou);
- ritmo da fase contra o piso e o alvo;
- o que está barato e o que está caro;
- as mexidas sugeridas (de quanto pra quanto, por quê);
- público e criativo, em uma linha cada, mesmo que seja "nada a mexer";
- as decisões que são do dono da verba;
- um risco.
A mensagem final desta rodada é esse resumo inteiro, em texto, com o caminho do relatório.

PROIBIDO nesta rotina: criar, ativar, pausar ou editar qualquer coisa em plataforma; mudar configuração no Dash (pedir atualização de dado não é mudar configuração); mandar mensagem; editar rotinas.json, sirius-scale/ ou .claude/. Sugestão vira item do relatório, e quem aplica é o dono da conta, na plataforma.
```

## Três leituras que enganam (valem pra rotina e pra quem confere à mão)

1. **`ENABLED` no Google e `ACTIVE` na Meta não provam que a campanha entrega.** O Google para sozinho no fim da campanha
   e o status continua `ENABLED`; a Meta deixa `ACTIVE` o conjunto e o anúncio que já acabaram. Pra dizer que algo roda,
   olhe o fim (`end_date_time`, `end_time`) e o gasto por dia.
2. **O histórico de mudanças do Google aceita 30 dias contados do relógio de verdade**, não da data que se está lendo.
   Refazer um dia anterior pedindo "data − 29" dá erro de data antiga.
3. **Zero de compra num anúncio da Meta pode ser falta de pixel no rastreio**, não falta de venda (item 11 do
   `/preflight`). Quem decide venda é a venda casada no Dash.
## Quando mexer

- **Lançamento novo:** um `rotinas.json` novo. A rotina não muda.
- **Mudar a régua:** escreva em `frameworks-da-casa/` ou no `rotinas.json`, com a data e quem decidiu.
- **Algo saiu errado:** conte pro Claude e peça pra registrar a correção. A regra fica em `frameworks-da-casa/`,
  e a rotina lê de lá na próxima rodada.
