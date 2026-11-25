---
name: feedback-trafego-analise-manual-nao-apaga-rotina
description: "Análise manual de tráfego no Up não pode apagar as sugestões da rotina diária: publicar a frente de novo faz as pendentes expirarem; junte as da rotina antes"
metadata:
  type: feedback
---

Em 25/11/2026 rodei uma análise manual e publiquei com `trafego-analise`. Isso fez expirar as sugestões da rotina diária (`up-trafego-pedro-analise`, 9h48 e 13h33): pausar o ADV01, levar o ADV07 para a 029.2 e arrumar o play da VSL. O Anderson mostrou o histórico e reclamou ("isso aqui não é para ser feito"). Republiquei o Funil BR com as três.

**Why:** publicar a mesma frente substitui as pendentes. A rotina lê o vturb e tem contexto que a análise manual pode não ter.

**How to apply:** antes de publicar uma análise manual, leia as sugestões pendentes da rotina (JSONs da rotina na pasta temporária, ou a aba) e junte as que ainda valem. Se descartar alguma, diga o motivo no resumo. Relacionado: [[reference-up-aba-trafego]], [[feedback-limite-perda-rotacao]].
