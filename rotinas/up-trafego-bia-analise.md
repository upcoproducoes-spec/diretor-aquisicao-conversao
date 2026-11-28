---
name: up-trafego-bia-analise
description: Todo dia: lê Meta, Dashfácil, Hotmart e vturb e publica na aba Tráfego do Up da Bia a análise e as sugestões de cada frente (Funil Livro PTN, Black). Só lê e sugere.
---

Use a skill **up-trafego** no **modo ANÁLISE** e siga o processo dela do começo ao fim, sem parar para perguntar.

- **Projeto:** Bia (Beatriz Vieira). Pasta: C:\Users\User\Documents\Claude\Full Concepty Academy (rode todos os comandos de dentro dela).
- **Skill de método (obrigatória; definida com o Anderson em 23 e 24/11):** estratégia **Thiago Roas adaptada** para o perpétuo do livro, escrita em `clientes\sirius\beatriz-vieira\funis\vsl-livro-ptn\regras-campanha-teste-22nov26.md` (leia o arquivo inteiro antes de sugerir) e a skill `estrategia-trafego-funil`, com o agente gestor-trafego. Precedência: (1) decisões do Anderson nesse arquivo e no registro; (2) Thiago Roas; (3) heurísticas gerais. Não use regra do Pedro aqui.
- **Números de decisão do livro (régua do Anderson de 28/11, seção 3 do arquivo; Dash, com imposto):** o que fica para o Anderson, o Rodrigo e a Bia é o **faturamento menos o tráfego**. ROAS bruto 2: **alvo = ticket ÷ 2; máximo (empate) = ticket**.
  - **Até 30/11 (Black, livro a R$ 178):** alvo **R$ 89**, máximo **R$ 178**, checkout alvo R$ 18.
  - **A partir de 01/12 (livro a R$ 297):** alvo **R$ 180**, máximo **R$ 359**, checkout alvo R$ 36. Na primeira rodada de 01/12 em diante, se a frente "Funil Livro PTN" no Up ainda mostrar alvo 89, troque para 180: grave `{"cpa_target":180}` com Write no scratchpad e rode `node "C:\Users\User\Documents\Claude\Full Concepty Academy\up.cjs" api PATCH v1/traffic/fronts/16570ba6-fccc-487b-87d4-290b94b08627 "<caminho do json>"`; diga no resumo que trocou.
  - Diga no resumo qual régua usou e o lucro estimado por venda (ticket − CPA). Nunca use o "faturamento líquido" do Dash como régua.
  - **Corte (seção 5):** não julgar antes de 24 h e de metade do alvo gasto no criativo; sai com o máximo gasto sem venda, ou com 2× o máximo gasto e CPA acima do máximo; entre o alvo e o máximo fica e acompanha. Gancho, CTR e CPC só diagnosticam. Nunca tirar criativo sem o substituto da fila (seção 4) e sugerir a troca junto (pausar um e ligar o próximo da fila, que já está criado pausado na 001.1).
  - **Escala (seção 4):** criativo só vai para a Escala 1 (001.2, ainda não criada) com **10 vendas e CPA ≤ o alvo do período na Dash**. Com menos, fica no teste e o resumo diz quantas vendas faltam. Criar a 001.2 é pendência para o Anderson, não sugestão. Teto da escala: R$ 200/dia; orçamento sobe no máximo 20% por dia. Não promova criativo só com vendas da Black.
  - **Ritmo (seção 6):** decisão a cada 3 a 4 dias de teste; fora dos cortes, não mexer em orçamento nem anúncio na janela.
  - **Parar e revisar o funil (seção 9):** 7 dias seguidos com CPA do conjunto acima do máximo do período, connect rate abaixo de 65% ou checkout → compra abaixo de 12%: vai nas Pendências, não em sugestão de anúncio.
- **Conta de anúncios:** Beatriz Vieira (535326207056162).
- **Frentes:** Funil Livro PTN e Black (cursos) (veja `node up.cjs trafego`). O Up mostra o alvo fixo do livro (R$ 89 até 30/11; R$ 180 depois). **Black (cursos):** sem campanha paga desde 22/11 (o Anderson desligou a CURSOS-BF por falta de venda; a Black dos cursos segue só no orgânico até 30/11). Publique o resumo curto (vendas da Hotmart, sem sugestão) e não sugira religar campanha; a frente acaba em 30/11.
- **Documentos de tráfego a ler:** trafego-black-nov26.md (registro das decisões, inclusive o que o Anderson mandou NÃO propor de novo) e clientes\sirius\beatriz-vieira\funis\vsl-livro-ptn\ (perpétuo do livro). O material licenciado da pasta só é lido aqui; nunca copie para fora.

Responda em português do Brasil. No fim, uma linha por frente: CPA real × alvo e quantas sugestões publicou.