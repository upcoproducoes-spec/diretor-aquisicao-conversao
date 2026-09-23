# Ch30 — Funil de Vendas e Lead Scoring: o Caso Marketo

**Obra-fonte**: Receita Previsível, Cap. 6 (seção convidada sobre automação de marketing) | Aaron Ross & Marylou Tyler, 2020

## Core Idea

Este capítulo usa a Marketo (empresa de automação de marketing que cresceu de zero a cerca de 3.000 clientes em cinco anos) como estudo de caso de como estruturar um funil de vendas com estágios precisos e um sistema de pontuação (lead scoring) que decide, de forma automatizada, quando um contato deixa de ser "frio" e passa a merecer atenção humana de vendas. A tese central é operacional: "seria muito improdutivo gastar o tempo do pessoal de vendas com todos os leads" — o objetivo do lead scoring é dizer exatamente onde investir tempo escasso de vendas.

O funil da Marketo tem seis estágios (consciência, pesquisa, prospect, lead, oportunidade, cliente), dos quais o livro foca nos quatro primeiros — até o momento em que um "prospect" (frio) se converte em "lead" (quente o suficiente para merecer follow-up humano). A régua de conversão é numérica e simples: pontuação de 0 a 100, sendo 65 o limiar que separa prospect de lead.

## Frameworks Introduzidos

- **Funil de 6 Estágios da Marketo** — consciência → pesquisa → prospect → lead → oportunidade → cliente. Prospects (abaixo de 65 pontos) são "frios" e não merecem tempo humano ainda; leads (65+ pontos) já demonstraram engajamento suficiente para justificar follow-up ativo do time de vendas.
- **Lead Scoring** — sistema de pontuação de 0 a 100 que soma e subtrai pontos conforme o comportamento do contato (visitar páginas de alto interesse, baixar conteúdo, abrir e-mails somam pontos; inatividade prolongada subtrai pontos); acima de 65, o prospect vira lead formal e dispara ação humana; entre 0 e 30 ou acima de 30 sem engajamento, o sistema aplica penalidades específicas de pontuação.
- **Campanhas de Nutrição Automatizada por Estágio** — trilhas diferenciadas: campanha para novos prospects/leads (e-mail automático poucos minutos após um download/visualização, atribuído a um "Market Response Rep" designado pelo sistema); campanha de follow-up de 21 dias (se o MRR validar o prospect como viável); campanhas de manutenção de contato/"conta-gotas" (para quem não engajou após 21 dias, mantendo presença sem gastar tempo humano ativo).

## Key Concepts

- **O MRR (Market Response Rep) não precisa checar cada lead manualmente** — o sistema automatizado faz a triagem inicial; o humano intervém só depois que o sistema já filtrou o que vale revisão manual.
- **Taxa de conversão de leads em oportunidades qualificadas é uma das métricas mais importantes do funil** (retomada em detalhe no Ch33) — sem ela, não há como saber se o volume de topo de funil está se traduzindo em receita real.
- **"Não se preocupe em fazer um sistema tão detalhado quanto o da Marketo desde o início"** — o autor recomenda começar simples, avaliar resultados, e refinar a pontuação ao longo do tempo, em vez de tentar replicar um sistema maduro de uma tacada só.
- **A régua de 65 pontos não é universal** — é o limiar específico calibrado pela Marketo ao longo de anos de experimentação; cada empresa precisa calibrar sua própria régua com base em dados próprios.

## Mental Models

1. **"Automatize a triagem, reserve tempo humano para quem já provou interesse"** — antes de qualquer vendedor gastar tempo em um contato, pergunte se o sistema já validou engajamento suficiente.
2. **"Comece simples, refine com dados"** — não trave a implementação de lead scoring esperando um sistema perfeito; lance uma versão simples e itere com base em taxa de conversão real.
3. **"Trate cada estágio do funil como decisão, não como rótulo"** — a transição de prospect para lead deveria disparar uma ação concreta (follow-up humano), não ser apenas uma categoria descritiva.

## Anti-patterns

- **Gastar tempo de vendas uniformemente em todos os contatos**, sem sistema de priorização por engajamento.
- **Copiar a régua de pontuação de outra empresa sem calibrar com dados próprios.**
- **Tentar implementar um sistema de lead scoring tão sofisticado quanto o de uma empresa madura** logo de início, atrasando o lançamento por perfeccionismo.

## Key Takeaways

- Lead scoring resolve o problema de onde investir tempo escasso de vendas, automatizando a triagem inicial.
- O funil de 6 estágios da Marketo formaliza a transição de "frio" para "quente" com um limiar numérico claro (65 pontos).
- Sistemas de pontuação devem começar simples e ser refinados continuamente com dados reais, não lançados já maduros.

## Connects To

- Ch29 (Tipos de Leads — lead scoring ajuda a priorizar dentro de cada categoria de sementes/redes/alvos)
- Ch33 (7 Erros Fatais — taxa de conversão de leads como uma das 5 métricas mínimas)
- Ch05 (Venda Desafiadora, Personalização — a mesma lógica de tratar diferente quem está em estágio diferente de prontidão)
