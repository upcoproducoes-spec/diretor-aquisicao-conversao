# ch98 — Tráfego S.A. (Elmer Carneiro): Estrutura de Testes, Escala e Verba

**Livro:** Elmer Carneiro (Tráfego S.A.), "Masterclass Tráfego" | **Autor:** Elmer Carneiro | **Série:** ch96–ch99

> **Nota de proveniência:** ver ch96 (transcrição automática; números do palestrante, não verificados). Foco principal: Meta; Google é só "pincelada".

## Core Idea
Depois de validar ativos, a segunda etapa da pirâmide testa **qual estrutura de campanha escala melhor**. Duas regras de ouro: **isolar variáveis** nos testes e **dimensionar verba pelo CPL/CPA e pelo recurso disponível**, não por "orçamento ideal". A escala em si é gradual (15-20% por semana) e guiada por ROAS ou custo por lead.

## Estruturas de teste
- **Padrão (ABO):** 1 campanha, 1 conjunto **por criativo**, **mesmo público** e **mesma página** em todos os conjuntos: a única variável é o anúncio. Para testar público, mantém-se o mesmo anúncio e variam-se os públicos.
- **Alternativa (CBO):** colocar tudo em uma campanha com orçamento no nível da campanha: mais barato, mas pode não coletar dado de todos os criativos.
- **Limite de custo (bid/cost cap):** evitado em teste (trava a entrega).
- **Orçamento de teste:** captura gratuita = **2 a 3 CPLs por conjunto/dia** (ex.: CPL R$7 → ~R$15-35); perpétuo = **30-40% do CPA** por conjunto/dia; low ticket de R$47 = o suficiente para 1 venda/dia. Em lançamento, 10-20% da verba inicial para teste; perpétuo, ~10% da verba como regra geral (maior no começo).
- **Duração:** em perpétuo, **72 h mínimo** e idealmente 7 dias; em lançamento (captura de 14-21 dias), 2-3 dias; corte rápido quando o conjunto não faz o número esperado (ex.: 2 leads em 3 dias com meta de 4/dia).
- **Menos teste, mais verba por teste:** se a verba é curta, teste em **lotes** em vez de reduzir o orçamento por conjunto.
- **Lançamento com públicos já validados:** teste mais criativo do que público (1-2 públicos novos por campanha).

## Escala
- **Escala padrão:** campanha com **3 a 6 conjuntos**, cada um com **3 a 6 anúncios** vencedores; verba da campanha = 3x o CPL por conjunto, com faixa mais alta (5-6x) quando os ativos já foram validados.
- **ASC (Advantage Shopping Campaign):** campanha totalmente responsiva (sem segmentação; filtro de idade não é respeitado); deixe todos os anúncios ligados; no gratuito marque como "lead" só o **lead qualificado** (pergunta qualificadora), senão traz lead barato e ruim; para um nicho de 45+ ele sugeriu **5% do orçamento** para testar.
- **Outras formas:** bid cap, **escala baiana** (duplicação), 1-50 (orçamento 1 e 50 conjuntos), cluster (duplicar conjuntos): "funcionam em alguns cenários; hoje usamos menos".
- **Escala avançada (orçamento):** planejar a verba diária **20-30% acima da média** para dar folga a falhas de entrega; aumento **15-20% por semana** (50% se o orçamento é muito baixo); em perpétuo, **ROAS ≥ ~2,2** autoriza subir; abaixo, segura; em captura, o CPL projetado guia.
- **Rede e canais:** **Google Search** (palavras de marca e específicas; poucos reais por dia; página de captura perpétua) para todos; **YouTube Ads** só com caixa e audiência (ROAS 50-100% maior e CPL ~30% mais caro, segundo ele); **GDN** (display) para remarketing; **TikTok** (ASC obrigatória para quem roda). Separar **conta e pixel** quando mudar de país (LATAM x Brasil) e considerar perfil institucional.
- **Onde usar o lançamento pago:** ver ch89 e ch99.

## Divergências com o Roas (registrar, não escolher)
| Tema | Carneiro (Tráfego S.A.) | Roas (`estrategia-trafego-funil`) |
|---|---|---|
| Segmentação | Interesse, comportamento e semelhantes ainda testáveis | "Não existe segmentação por público"; tudo Advantage+ |
| Estrutura de teste | ABO isolando variável (1 criativo/conjunto, mesmo público), CBO alternativo | CBO 1x1 ou 1xN, depois Advantage+ e limite de custo |
| Limite de custo | Evita em teste; "escala baiana", cluster ainda usados | Segunda etapa de escala (limite de custo, CPA pelo ticket médio) |
| Teste semanal | 5 criativos, 2 públicos, 1 página | Validar criativo por ROAS ≥2 e ≥10 vendas |
| Decisão de escala | ROAS ≥ ~2,2, +15-20%/semana | +20%/dia; 7-3-1 |
Ambos concordam: criativo é a variável principal, orçamento de teste pequeno, não desligar por um dia ruim, métrica final é dinheiro.

## Anti-patterns
- Testar página com A/B de ferramenta em campanha de produção.
- Mudar público e anúncio juntos.
- Orçamento de teste "ideal" copiado de outro negócio.
- Escalar 100% de uma vez sem ter folga.

## Key Takeaways
1. Isole uma variável por teste e mantenha mesma página.
2. Dimensione verba por CPL/CPA, e teste por lotes quando a verba é curta.
3. Escala padrão = 3-6 conjuntos x 3-6 anúncios vencedores.
4. ASC em porção pequena, com lead qualificado marcado.
5. Planeje o orçamento 20-30% acima da média e aumente gradualmente.

## Connects To
ch96-ch97, ch99 • `estrategia-trafego-funil` (fases de escala, ticket médio) • ch54 (Hormozi, fases de gasto) • ch89-ch95.
