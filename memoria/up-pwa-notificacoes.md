---
name: up-pwa-notificacoes
description: Up é app instalável (PWA) com notificações Web Push desde 26/11/2026; como funciona e onde mexer
metadata:
  type: project
---

Desde 26/11/2026 (commit 4f680db, migração 0105) o Up é um app instalável (PWA) em Android, iPhone (Safari → Adicionar à Tela de Início), Windows e Mac, com notificações no aparelho. Escolha do Anderson: PWA em vez de lojas (App Store/Play ficam para depois, se ele quiser o Up "na loja").

- Botões no rodapé do sininho: "Instalar o app" e "Ativar notificações neste aparelho" / "Testar" / "Desativar" (js/pwa.js). iPhone só recebe notificação com o app instalado e aberto pelo ícone.
- Cada aviso do sininho (notify em inbox.ts) sai como notificação (worker "notificações no celular" → processPushes em packages/db/src/push.ts). Expert recebe só o que vê no sininho (sem criativos), com links dele. Aviso novo "post pronto para revisar" (kind 'post') sai ao enviar post para aprovação.
- Chaves VAPID criadas e guardadas pelo próprio servidor (tabela push_vapid, privada criptografada); nada a configurar no Render.
- A API de vídeo da OpenAI (Sora) foi desligada em 24/09/2026: vídeo animado é feito com gerar-video.mjs (ilustrações gpt-image-2 + movimento + voz sintética).

**How to apply:** aviso novo que deva chegar no celular = só chamar notify(); não criar outro canal. Relacionado: [[up-producao-conteudo]], [[up-design-direcao]].
