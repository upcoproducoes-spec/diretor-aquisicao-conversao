---
name: up-neon-plano
description: Neon do Up passou para o plano Launch (pago por uso) em 26/11/2026 depois de o gratuito pausar o banco
metadata:
  type: project
---

Em 26/11/2026 ~15h o projeto UP no Neon (org "up", AWS us-east-2) estourou as 100 CU-horas do plano gratuito (110 usadas desde 02/11) e foi pausado: o Up inteiro caiu (erro 500 "exceeded the quota" em todo login/API). O Anderson fez upgrade para o **Launch** (US$ 0,106/CU-h + US$ 0,35/GB-mês; estimativa ~US$ 15/mês), cartão final 2054.

**Why:** o gratuito pausa o banco sem aviso quando acaba a cota; o Up é produção.
**How to apply:** se o Up der 500 em tudo, olhar primeiro o log do Render por "exceeded the quota"/Neon. Custo do Neon entra nos recibos mensais e no custo por projeto. Sugerido alerta de gasto em US$ 25 (Spending notifications), ainda não ligado.
