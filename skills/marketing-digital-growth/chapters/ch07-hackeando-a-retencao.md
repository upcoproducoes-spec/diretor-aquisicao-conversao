# ch07 — Hackeando a Retenção

**Livro:** Hacking Growth | **Autores:** Sean Ellis & Morgan Brown

## Core Idea
Adquirir usuários para um "balde furado" é o erro mais caro em growth: qualquer ganho de aquisição é anulado se a taxa de churn for alta. Retenção deve ser tratada como a alavanca prioritária antes de escalar aquisição, e se mede por curvas de coorte — não por uma taxa de churn agregada, que esconde padrões.

## Frameworks Introduzidos
- **Análise de Coortes (Cohort Analysis)**: agrupar usuários pela data/evento de entrada e acompanhar a curva de retenção de cada grupo ao longo do tempo — revela se mudanças no produto estão de fato melhorando a retenção (a curva "achata" em um patamar mais alto) ou só adiando o churn.
- **Curva de Retenção "Achatada" (Flattening Curve)**: o padrão saudável é uma curva que cai inicialmente e depois estabiliza em um platô — esse platô representa o núcleo de usuários engajados de longo prazo; o objetivo dos testes de retenção é elevar a altura desse platô.
- **Loops de Engajamento**: mecanismos recorrentes que trazem o usuário de volta (notificações, e-mails de reengajamento, conteúdo novo, funcionalidades sociais) — desenhados para reforçar o hábito criado no Modelo Hook (ch06).

## Key Concepts
- O "balde furado" (leaky bucket): investir em aquisição sem consertar retenção é matematicamente ineficiente — o CAC efetivo sobe porque usuários saem antes de gerar LTV suficiente.
- Campanhas de win-back (recuperação de usuários inativos) são um subconjunto de retenção: usam gatilhos e ofertas segmentadas para trazer de volta quem parou de engajar antes do churn definitivo.
- Testes de retenção geralmente têm ciclo de mensuração mais longo que testes de aquisição/ativação — exigem paciência estatística e definição clara da janela de observação.

## Mental Models
- "Retenção antes de aquisição, sempre": a sequência correta de prioridade de growth, segundo os autores, é Ativação → Retenção → depois Aquisição em escala.
- Cada coorte é um experimento natural: comparar coortes de diferentes períodos (antes/depois de uma mudança de produto) é uma das formas mais confiáveis de medir impacto real.

## Anti-patterns
- Medir "taxa de churn mensal" como número único sem segmentar por coorte, canal de aquisição ou perfil de uso — mistura sinais completamente diferentes.
- Tratar reengajamento e recuperação de carrinho como o mesmo problema: retenção de produto (usuário parou de usar o produto) é conceitualmente diferente de recuperação de carrinho (usuário iniciou uma compra e não concluiu) — mecanismos de gatilho podem se sobrepor, mas a causa raiz e o funil são distintos.
- Comemorar aumento de usuários ativos sem checar se é crescimento líquido (novos menos os que saíram) ou apenas volume bruto de topo.

## Key Takeaways
- A curva de retenção por coorte é a ferramenta de diagnóstico mais importante deste capítulo — sem ela, "melhorar retenção" é um alvo sem mira.
- Loops de engajamento bem desenhados reduzem o custo de reter comparado ao custo de adquirir — geralmente a alavanca de maior ROI de growth hacking em produtos maduros.
- Nota de adjacência (não confundir): a mecânica de urgência de "cart open/close" do Product Launch Formula (ch33, livro 4) é sobre pressão de tempo para decisão de compra, enquanto recuperação de carrinho é sobre reengajar quem já decidiu comprar mas não finalizou — são gatilhos relacionados, mas resolvem problemas de funil diferentes.

## Connects To
- ch08 (Hackeando a Monetização): retenção saudável é pré-condição para monetização sustentável (usuário precisa ficar tempo suficiente para gerar LTV).
- ch33 (livro 4 — Prelaunch, Open Cart e Launch Sequence): ver nota de adjacência acima sobre urgência de lançamento vs. recuperação de carrinho.
- Skill `diretor-aquisicao-conversao`, fase 8/12: retenção é o elo entre "compra" e recompra no funil estendido, e a análise de coorte é a ferramenta recomendada para a fase de Métricas.
