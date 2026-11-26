---
name: estrategias-trafego
description: Catálogo das estratégias de tráfego pago que o time usa. Cada estratégia diz o que ela manda (métrica, estrutura, o que pode e o que não pode mexer na conta) e para quais funis vale. Use no início de qualquer trabalho de tráfego para definir QUAL estratégia vale naquele funil; o gestor-trafego opera em cima da estratégia escolhida e não cria estratégia própria. Também use para registrar uma estratégia nova ou atualizar uma existente.
---

# Estratégias de tráfego (catálogo)

**Princípio (decisão do usuário, 2026-11-24):** o gestor de tráfego **executa e monitora**; ele não inventa estratégia. Primeiro se **decide a estratégia** do funil; depois o gestor trabalha em cima dela. Estratégia nova entra aqui como um arquivo; estratégia existente é atualizada no próprio arquivo (atualizar, não substituir).

## Como usar
1. No início de um trabalho de tráfego, o diretor pergunta ao usuário (ou lê no registro abaixo) **qual estratégia vale para aquele funil**.
2. O diretor passa ao gestor, no briefing: nome da estratégia, o arquivo dela e o que ela **proíbe** mexer.
3. O gestor lê o arquivo da estratégia, a skill de método que ela indica, e segue só isso. Faltou estratégia definida: o gestor devolve a pendência, não escolhe por conta própria.
4. A estratégia vence qualquer padrão geral do gestor (rotina genérica, regras gerais de leitura).

## Estratégias cadastradas
| Código | Estratégia | Vale para | Status |
|---|---|---|---|
| `thiago-roas-perpetuo` | Funil de VSL perpétuo (Thiago Roas) | Perpétuos de público frio com VSL | **Em uso** no perpétuo do Pedro; será usada no da Beatriz. Não é regra para todos os funis |
| `sirius-lancamento` | Rotinas de lançamento da Sirius Scale | Só pastas de cliente que têm o kit instalado | Material licenciado: fica na pasta do cliente, nunca aqui |

## Decisões de reunião (vivas, não são estratégia)
O que os sócios definem nas reuniões fica em `decisoes-de-reuniao.md`, com data, e muda a cada reunião. O gestor trata a entrada mais recente como orientação do momento, sem contrariar a estratégia ativa do funil. Conflito: avisa e espera o usuário.

## Registro por funil (preencher conforme o usuário decidir)
| Cliente | Funil | Estratégia | Decidido em | Observação |
|---|---|---|---|---|
| Pedro Sachet | Perpétuos (MORFOGUIDE-BR, MORFOGUIDE-ES e os demais) | `thiago-roas-perpetuo` | 2026-11-24 | Em uso hoje; reavaliar quando entrar estratégia nova |
| Beatriz | Perpétuo | `thiago-roas-perpetuo` (a usar) | 2026-11-24 | Confirmar ao começar |
| Pedro Sachet | Carrinho da Black (campanha 032.1, nov/26) | Plano próprio do carrinho: `projeto-black-morfologic/15-plano-trafego-carrinho-black.md` (na pasta do cliente), seções 2.3 e 7 | 2026-11-18 | Aprovado pelo Anderson (faixa B, ABO). Decide pela Dash Fácil (vendas e ROAS bruto por utm_content) comparada ao Meta; corte de peça, corte de conjunto e escala na seção 7; o quente não desliga antes do fechamento. CPA alvo da frente no Up: R$ 300 |

## Estratégia nova: modelo
Crie `<codigo>.md` nesta pasta com: **o que ela é** (em palavras próprias, fonte e data), **para que funil vale**, **métrica mestre**, **estrutura**, **o que o gestor pode propor e executar**, **o que o gestor NÃO pode mexer**, **como lê o dia** (o que olhar e em que ordem), **critérios de decisão** (com a fonte; número de aula é "não verificado") e **o que ainda falta confirmar**. Material de terceiros licenciado não entra aqui: só ponteiro para a pasta do cliente.
