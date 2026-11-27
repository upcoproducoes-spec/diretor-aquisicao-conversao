---
name: sirius-humanizer
description: Remove marcas de texto gerado por IA (linguagem promocional, "-ing" superficial, atribuição vaga, abuso de travessão, regra dos três, vocabulário de IA, paralelismo negativo) e injeta voz humana de verdade. Use ao revisar qualquer copy antes de entregar — é a camada final depois que o agente `copy` escreve, e serve pra qualquer texto lido pelo avatar (anúncio, e-mail, página, roteiro, post). Baseado no guia "Signs of AI writing" da Wikipédia (WikiProject AI Cleanup). Créditos: skill original de @blader (github.com/blader/humanizer).
---

> Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
> são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
> ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.


# Humanizer: remover padrões de escrita de IA

Editor de texto que identifica e remove sinais de texto gerado por IA pra soar
natural e humano. Baseado no guia "Signs of AI writing" da Wikipédia, mantido
pela WikiProject AI Cleanup.

## Tarefa

Ao receber um texto pra humanizar:

1. **Identificar padrões de IA** — varrer pelos padrões listados abaixo.
2. **Reescrever os trechos problemáticos** — trocar "IA-ismos" por alternativas naturais.
3. **Preservar o sentido** — manter a mensagem central intacta.
4. **Manter a voz** — bater com o tom pretendido (formal, casual, técnico etc.) e,
   aqui, com a voz específica da expert (`expert/dna-expert.md`).
5. **Adicionar alma** — não é só tirar o que é ruim; é injetar personalidade de verdade.

## Personalidade e alma

Evitar padrões de IA é só metade do trabalho. Texto estéril e sem voz é tão
óbvio quanto "AI slop". Escrita boa tem gente por trás.

Sinais de escrita sem alma (mesmo que tecnicamente "limpa"):

- Toda frase tem o mesmo tamanho e a mesma estrutura
- Nenhuma opinião, só relato neutro
- Nenhuma incerteza ou sentimento misto reconhecido
- Nenhuma primeira pessoa onde ela caberia
- Nenhum humor, nenhuma aresta, nenhuma personalidade
- Lê como verbete de enciclopédia ou nota de assessoria

Como adicionar voz:

- **Ter opinião.** Não só relatar fato — reagir a ele.
- **Variar o ritmo.** Frase curta e seca. Depois uma mais longa, que demora
  pra chegar no ponto. Alternar.
- **Reconhecer a complexidade.** Gente de verdade tem sentimento misto.
- **Usar primeira pessoa quando cabe** — não é deselegante, é honesto.
- **Deixar alguma bagunça entrar.** Estrutura perfeita demais soa algorítmica.
- **Ser específico no sentimento.** Não "isso preocupa", e sim o que exatamente
  preocupa e por quê.

## Padrões de conteúdo

**1. Ênfase indevida em importância/legado/tendência** — "marca um momento
pivotal", "reflete uma tendência mais ampla", "consolida seu papel". Corta:
afirma o fato, não o "significado" dele.

**2. Ênfase indevida em notoriedade** — listar veículos/menções sem contexto
("foi citado no X, Y, Z e tem presença ativa nas redes"). Troca por uma
citação específica, datada, com fonte.

**3. Análises superficiais terminadas em "-ndo"** — "destacando...",
"reforçando...", "consolidando..." pendurado no fim da frase pra fingir
profundidade. Corta o gerúndio decorativo.

**4. Linguagem promocional/publicitária** — "vibrante", "rico", "de tirar o
fôlego", "referência em", "no coração de". Neutraliza: descreve o fato
verificável, não o adjetivo.

**5. Atribuição vaga / weasel words** — "especialistas acreditam",
"segundo relatos do setor", "diversos estudos apontam" sem citar quem.
Só entra se rastreia até fonte real — e isso já é regra da casa (`sirius-scale/REGRAS.md`
§2): sem fonte, não entra.

**6. Seção formulaica de "desafios e perspectivas"** — "apesar dos desafios,
segue crescendo". Troca por fato concreto e datado.

## Padrões de linguagem e gramática

**7. Vocabulário de IA em excesso** — "adicionalmente", "crucial",
"mergulhar", "fundamental", "aprimorar", "landscape/cenário", "tapeçaria",
"testemunho", "vibrante". Evitar em português vale o mesmo espírito: são as
palavras que a seção 1 do `sirius-scale/REGRAS.md` já proíbe ("mergulhe", "desvende",
"eleve", "descubra o segredo").

**8. Evitar o verbo "ser/estar" (copula avoidance)** — "serve como",
"representa", "configura-se como" no lugar de "é". Troca pela forma direta.

**9. Paralelismo negativo** — "não é só X, é Y". Já é regra proibida na
seção 1 do `sirius-scale/REGRAS.md` ("não é apenas X, é Y") — este padrão é o mesmo,
achado independentemente pela Wikipédia.

**10. Abuso da regra dos três** — forçar tudo em grupos de três pra parecer
completo. Deixa em dois, ou em um só, quando é o que sustenta.

**11. Variação elegante (troca de sinônimo forçada)** — trocar "protagonista"
por "personagem principal" por "figura central" só pra não repetir a palavra.
Repetir a palavra certa é melhor que sinônimo forçado.

**12. Falso intervalo** — "da fundação da empresa ao futuro da indústria"
quando as duas pontas não estão na mesma escala.

## Padrões de estilo

**13. Abuso de travessão** — travessão em excesso imitando "copy vendedora
punchy". Troca por vírgula ou ponto.

**14. Abuso de negrito** — negritar frase inteira mecanicamente.

**15. Lista com cabeçalho em negrito + dois pontos, item a item** — formato
"Performance: a performance foi otimizada." Vira prosa corrida.

**16. Title Case em título** — só a primeira palavra maiúscula, em português.

**17. Emoji decorando título ou bullet** — fora, salvo pedido explícito do
cliente (regra geral do projeto: nada de emoji sem pedido).

**18. Aspas curvas** — usa aspas retas.

## Padrões de comunicação

**19. Artefato de conversa com chatbot colado no texto** — "espero que ajude",
"deixe-me saber", "aqui está uma visão geral". Nunca aparece na peça final.

**20. Disclaimer de corte de conhecimento** — "informações específicas são
limitadas" ou "até onde sei". Se faltou dado, a regra da casa (`sirius-scale/REGRAS.md` §2)
já manda perguntar antes de escrever — não estampar a incerteza no texto final.

**21. Tom servil/bajulador** — "ótima pergunta!", "você está certíssimo".
Fora de qualquer copy pro avatar.

## Preenchimento e ressalva em excesso

**22. Frases de preenchimento** — "com o objetivo de" → "pra"; "devido ao
fato de que" → "porque"; "neste momento" → "agora"; "tem a capacidade de
processar" → "processa".

**23. Ressalva excessiva** — "poderia potencialmente talvez ter algum efeito"
→ "pode afetar".

**24. Conclusão positiva genérica** — "o futuro é promissor, tempos
empolgantes estão por vir". Troca por fato concreto e verificável (o quê,
quando).

## Processo

1. Ler o texto de entrada com atenção.
2. Identificar toda ocorrência dos padrões acima.
3. Reescrever cada trecho problemático.
4. Conferir se o texto revisado:
   - soa natural em voz alta;
   - varia a estrutura da frase de forma orgânica;
   - usa detalhe específico em vez de afirmação vaga;
   - mantém o tom certo pro contexto e pra voz do expert;
   - usa construção simples ("é", "tem") onde cabe.
5. Entregar a versão humanizada.

## Formato de saída

- O texto reescrito.
- Resumo breve do que mudou (opcional, quando ajuda a revisão do Rodrigo).

## Onde essa skill entra no fluxo da casa

A seção 3 do `sirius-scale/REGRAS.md` já manda toda copy passar pelo agente `copy`, que
lê `expert/dna-expert.md`, `expert/produtos/<produto>.md`, `pesquisa.md`, `avatar.md` e o
`banco-angulos.md` antes de escrever. Esta skill é a **passada seguinte**:
depois que a copy está ancorada no dado real do cliente, ela varre o texto
pronto atrás de "cara de IA" — a mesma checagem que a seção 1 do `sirius-scale/REGRAS.md`
já exige ("proibido linguagem de IA... se soar como IA, reescreve"), só que
sistemática, com a lista de padrões acima em vez de depender de notar na
leitura corrida.

**Não substitui a regra da seção 1 do REGRAS.md** — ela é a implementação prática dela.
E não inventa fato nem preenche lacuna: se um padrão de "atribuição vaga" ou
"disclaimer de corte de conhecimento" aparecer, o problema de origem é falta
de dado real, e a regra da seção 2 do REGRAS.md (perguntar, nunca supor) continua valendo.

Créditos: skill original de [@blader](https://github.com/blader/humanizer),
baseada no guia [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
mantido pela WikiProject AI Cleanup.
