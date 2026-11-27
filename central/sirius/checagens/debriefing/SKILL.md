---
name: debriefing
description: Faz o debriefing completo de um funil que já rodou — ou o diagnóstico de um que está rodando — em qualquer modelo (lançamento gratuito/CPL, pago/LPSG, semente, VSL/perpétuo, low ticket), cobrindo tráfego, criativos, copy, narrativa, oferta, remarketing, quem veio × quem comprou, financeiro e operação, sempre com número rastreado à fonte (arquivo ou ferramenta) e terminando em decisão ranqueada pelo valor em reais. Dispara quando pedirem "debriefing", "post-mortem", "analisa o lançamento/funil X", "como foi o lançamento X", "diagnóstico do funil", "o que a gente aprendeu com o lançamento" — mesmo que não citem a skill. Não é revisão técnica (isso é /revisar) nem extração de aprendizado da sessão (isso é /pente-fino): é a análise de resultado do funil em si.
---

> Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
> são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
> ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.


# Debriefing de funil — o que os números realmente dizem

A pessoa diz qual funil. Eu monto a entrada, carrego o prompt-fonte e rodo.
**Ninguém cola prompt nenhum** — as instruções de sistema já estão no kit, em
`sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md`, e esta skill
é quem as carrega. Tudo que é método, trava, formato de entrega e divisão de
trabalho mora lá; aqui só o que é operação da skill.

## Passo 0 — Montar o bloco ENTRADA (eu, não a pessoa)

O prompt-fonte pede um bloco `ENTRADA` (expert e produto, funil ou tag, tipo, status,
período, pergunta principal, análises anteriores, conexões ligadas, fontes de fora).
Preencher a partir do que a pessoa disse e do que a pasta mostra:

- **Tipo e pasta** — `lancamentos/<AAAA-MM-nome>/` é lançamento (por edição);
  `funis/<nome>/` é perpétuo (por período). Confirmar o tipo pelo `briefing.md`,
  nunca pelo nome.
- **Status** — fechou ou rodando? Se o `briefing.md` tem data de fim e ela
  já passou, fechou; senão, perguntar. Isso muda o que sai (debriefing ×
  diagnóstico) e não se deduz.
- **Análises anteriores** — `grep -rli "<tag>" entregas/ lancamentos/ funis/` antes de
  perguntar, em todas as pastas e não só na subpasta de análises (análise salva no lugar
  errado também conta).
  E `frameworks-da-casa/`, pra saber o que vocês já tiraram de edições anteriores.
- **Conexões ligadas e de onde vem o dado** — o que dá pra ler direto e o que vai
  precisar chegar em arquivo:
  - **Dash Fácil**, se o conector estiver ligado: liste as subcontas e o lançamento
    (ou o perpétuo); as ferramentas de debriefing do conector trazem o resumo do
    resultado, o detalhe por UTM, pesquisa × venda, o dia de captação e o rastreio de
    cada comprador.
  - **Hotmart**, se o conector estiver ligado: vendas, comissões, reembolsos e parcelas.
  - **Meta e Google**: pelo conector, se houver; senão, export ou print do gerenciador.
  - **O resto** (planilha da equipe, export, print, transcrição de live): o arquivo que
    a pessoa mandar. Número que não veio de uma dessas fontes não entra.
- **Onde guardar o que for lido** — o que sair do conector fica salvo em
  `lancamentos/<AAAA-MM-nome>/dados/debriefing-<AAAA-MM-DD>/` (ou na pasta do funil), com
  uma linha dizendo de onde veio e quando. Número cuja origem morreu com a sessão não é
  número.
- **Funil rodando com tráfego ligado** — antes de tudo, a saúde da conta do `/revisar`
  (Passo 0 de `.claude/skills/revisar/SKILL.md`). O que ela achar abre o relatório.

Perguntar **só** o que faltou depois disso — normalmente a pergunta
principal (a decisão que a análise precisa sustentar) e o período, quando é
perpétuo.

## Passo 1 — Modelo

Post-mortem de lançamento inteiro é síntese longa em cima de muita fonte: o julgamento
pede o modelo mais forte que o plano de vocês tiver (Opus serve); o modelo padrão serve
pra puxar dado e montar tabela, não pra fechar a leitura. Se a conversa está num modelo
mais leve, **sugerir a troca antes de começar** e seguir só se a pessoa mantiver — a
troca é decisão dela.

## Passo 2 — Carregar e rodar

Ler `sirius-scale/frameworks/lancamentos/prompts-sistema/debriefing-funil.md` inteiro e
seguir o bloco **INSTRUÇÃO DE SISTEMA** do início ao fim: Passo 0 do prompt
(análise anterior, plano, inventário de fontes, parada se faltar o
essencial), tabela de vazamento, dimensões, travas do §5, entrega no formato
do §6, checklist do §10. A divisão em subagentes é a do §9 — o orquestrador
faz o inventário e a tabela de vazamento sozinho e consolida no fim.

Saída: `entregas/analises/debriefing-<tag>-<AAAA-MM-DD>.md` (fechou) ou
`entregas/analises/diagnostico-<tag>-<AAAA-MM-DD>.md` (rodando). Perpétuo atualiza
também o `funis/<nome>/desempenho.md` do funil (modelo em `sirius-scale/modelos/desempenho.md`).

## Passo 3 — Depois

- Os candidatos a regra (item 14 da entrega) seguem `sirius-scale/REGRAS.md` §5:
  registrar em `frameworks-da-casa/` o que é novo e não contradiz nada (nasce VARIAÇÃO
  ISOLADA ou PADRÃO INCONCLUSIVO, com a data, a edição de origem e o porquê); **parar e
  perguntar** no que contradiz linha marcada CONSISTENTE.
- `/pente-fino` na mesma sessão.
- Versão pro expert ou pra quem não estava na operação é peça separada, feita
  depois — não sai daqui.

## Relação com as outras skills

| Skill | Pergunta que responde |
|---|---|
| `/revisar` | a execução saiu conforme o framework e o briefing? |
| `/debriefing` | **o funil deu o resultado que devia, e por quê?** |
| `/pente-fino` | o que esta sessão ensinou e não ficou registrado? |

Ordem natural ao fechar um lançamento: `/revisar` → corrigir → `/debriefing`
→ registro em `frameworks-da-casa/` → `/pente-fino`.
