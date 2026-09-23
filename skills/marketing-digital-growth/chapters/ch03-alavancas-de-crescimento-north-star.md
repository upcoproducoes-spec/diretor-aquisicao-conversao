# ch03 — Identificando Alavancas de Crescimento e a North Star Metric

**Livro:** Hacking Growth | **Autores:** Sean Ellis & Morgan Brown

## Core Idea
Antes de testar táticas, a equipe precisa identificar quais variáveis (alavancas) realmente movem o crescimento do negócio, e escolher UMA métrica-guia — a **North Star Metric (NSM)** — que capture o valor central entregue ao cliente e que sirva de bússola para priorizar todos os experimentos subsequentes.

## Frameworks Introduzidos
- **North Star Metric (NSM)**: métrica única que representa o valor central que o produto entrega aos usuários (ex.: "número de viagens completadas com sucesso" para um app de transporte, não "downloads"). Toda a equipe se alinha em torno de mover essa métrica.
- **Mapeamento do Funil de Alavancas**: decompor a jornada do usuário em etapas mensuráveis (aquisição → ativação → retenção → monetização → recomendação) e identificar, com dados reais, em qual etapa está o maior ponto de vazamento (maior perda percentual) — essa etapa é a alavanca prioritária.

## Key Concepts
- A NSM difere de métricas de vaidade porque está causalmente ligada à retenção e à receita, não apenas ao volume de topo de funil.
- Alavancas de crescimento mudam ao longo do tempo: o gargalo prioritário de uma empresa em estágio inicial (geralmente ativação) é diferente do gargalo em estágio de escala (geralmente retenção ou monetização).
- Escolher a alavanca errada desperdiça o ciclo inteiro de testes — por isso a análise de dados (funil quantificado) precede a geração de ideias.

## Mental Models
- "Métrica única, não painel de 30 KPIs": a NSM força priorização e evita que a equipe se disperse otimizando métricas que não se conectam ao valor real do cliente.
- Isolar antes de otimizar: nunca atacar uma etapa do funil "porque parece óbvia" — sempre confirmar com dados qual etapa concentra a maior perda relativa antes de alocar esforço de teste.

## Anti-patterns
- Escolher uma NSM que é fácil de mover mas não correlaciona com receita ou retenção real (ex.: número de contas criadas em vez de contas ativas).
- Pular a etapa de mapeamento do funil e ir direto para "boas ideias" de marketing sem saber em qual etapa elas atuam.
- Trocar de NSM com frequência, o que impede a equipe de acumular aprendizado sobre o que realmente move aquela métrica.

## Key Takeaways
- Definir a North Star Metric é o primeiro ato estratégico da equipe de crescimento — sem ela, o ICE score (ch04) não tem contra o que ser calibrado.
- O funil quantificado (com taxas de conversão reais entre etapas) é o mapa que revela onde investir esforço de teste.
- Esta é a aplicação operacional direta da regra "métrica não é resposta, é sintoma": o funil decompõe o sintoma (ex.: "poucas vendas") até a causa (ex.: "queda de 70% entre clique e página").

## Connects To
- ch04 (Ciclo de Growth Hacking e ICE Score): a alavanca identificada aqui alimenta diretamente o backlog de hipóteses priorizadas.
- ch23 (Data-Driven Marketing, Métricas e KPIs — livro 2): expande o tema de métricas com frameworks complementares de atribuição.
- Skill `diretor-aquisicao-conversao`, fase 8 (Arquitetura do Funil) e regra permanente sobre isolar o gargalo real impressão→clique→página→checkout→compra antes de agir.
