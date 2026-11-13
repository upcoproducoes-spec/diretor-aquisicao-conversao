---
name: up-email-and-client-onboarding
description: "Decisões de e-mail do Up (custo zero, Hostinger SMTP, teto diário) e lembrete do checklist de cadastro de cliente"
metadata:
  node_type: memory
  type: project
  originSessionId: ab2fdac0-b08c-4b0d-93b2-73582b7c6c6b
  modified: 2026-11-03T11:35:44.446Z
---

**Atualização 16/10/2026: Amazon SES decidido** (o usuário vai assinar). Uma conta AWS só para o Up inteiro; cada cliente verifica o próprio domínio no SES. Código pronto (commit ed1731b, migração 0062 ainda não rodada/publicada em 16/10): provedor `ses` (host = região, username = id da chave, secret_enc = chave secreta), envio pela API SES v2 com SigV4 próprio (conferido com o caso get-vanilla da AWS), avisos pelo SNS em `/webhooks/ses/<SES_WEBHOOK_TOKEN>` (assinatura do SNS conferida; SES_SNS_TOPIC_ARN opcional; SES_CONFIGURATION_SET para publicar eventos), cadastro por `add-email-account --provider ses --region us-east-1` (chaves digitadas ocultas; confere modo de teste e domínio verificado). Antes era: custo zero, SES descartado.
**Estado em 16/10 (manhã):** região us-east-2 (Ohio; us-east-1 bloqueada na conta), conta 817139100039. Migração 0062 rodada e publicada. No Render: SES_WEBHOOK_TOKEN, SES_SNS_TOPIC_ARN (up-ses-eventos), SES_CONFIGURATION_SET=up-eventos. Conjunto up-eventos com destino SNS "up-sns" (rejeição, entrega, devolução, reclamação, atraso, abertura, clique). Inscrição HTTPS no tópico CONFIRMADA. Domínio pedrosachet.com.br JÁ VERIFICADO no SES (Easy DKIM 2048, criado 16/10 08:49). Conta FORA do sandbox em 16/10 (50.000/dia, 14/s). Usuário IAM up-ses-envio (política em linha só SendEmail/GetAccount/GetEmailIdentity). Conta SES do Pedro cadastrada (id ba8bb697…, teto 2.000/dia para aquecer); Resend e SMTP do Pedro desligados. Comando novo: `npm.cmd run email-account -w @up/api -- --workspace X [--id Y --on|--off --cap N]` (teto máx. 5.000 pelo banco). No Windows usar npm.cmd (PowerShell bloqueia npm.ps1). Envio automático usa a conta ativa MAIS ANTIGA e disparo a MAIS NOVA: manter só uma ativa por cliente.

Decisão (2026-10-03): o Up envia e-mail pelo SMTP da Hostinger com contato@pedrosachet.com.br (smtp.hostinger.com:465 SSL, imap.hostinger.com:993), teto inicial de 100 por dia, sem mudar DNS (SPF/DKIM/DMARC da Hostinger já ok; DNS no Cloudflare). A senha da caixa nunca vai pelo chat: comando com leitura escondida, guardada criptografada. Não mexer em nada do FullFunnel/WordPress que já roda.

Para cada cliente novo as conexões são sempre novas (e-mail, WhatsApp, Meta, etc.); o usuário pediu um checklist do que o cliente precisa trazer, rascunho em docs/07-checklist-novo-cliente.md do repo Up, para revisar quando o app estiver finalizado. Opção por cliente: plano de e-mail existente ou SES para volume maior.

Descoberta (2026-10-03): a conta SMTP da Hostinger foi cadastrada e o login funciona, mas o plano grátis do Render BLOQUEIA saída SMTP (25/465/587), então o envio dá "Connection timeout" lá (localmente funciona). Saídas: provedor por API HTTPS (Brevo/Resend, grátis, exige conta criada pelo usuário e registros DNS aditivos no Cloudflare), relay em Cloudflare Worker, ou Render pago. O transporte é trocável (TransportFactory em packages/db/src/email.ts).

**Why:** evitar custo e não quebrar o que já roda no FullFunnel.
**How to apply:** ao construir envio de e-mail, usar provedor trocável (SMTP agora, SES/Brevo depois); ao cadastrar cliente, seguir o checklist. Veja [[up-operating-model]].

**ManyChat (30/10/2026):** a API não busca por WhatsApp. O Up procura o contato nos campos personalizados da conta cujo nome pareça WhatsApp (ex.: "WhatsApp" na conta da Beatriz, 3 mil contatos antigos) e no `up_whatsapp`, com e sem o 9; depois tenta pelo nome. Falhas aparecem em Integrações (resumo com motivo, lista retrátil, "Reenviar falhas") e no sininho. Pendente: conectar o e-mail da Beatriz no Up.

**E-mail da Beatriz (30/10/2026):** fullconceptacademy.com.br verificado no SES (us-east-2, Easy DKIM 2048, 3 CNAMEs no Cloudflare da conta do Rodrigo, 487c5435...; DNS/MX da Hostinger intactos). Conta contato@fullconceptacademy.com.br cadastrada no projeto beatriz-vieira (id 5329c73a, teto 2.000/dia). Chave 2 do usuário IAM up-ses-envio criada para isso; a chave 1 segue no Pedro. Alteração de DNS pelo Claude é bloqueada pelo modo automático: o usuário faz. Ideia aprovada para construir: tela no Up para conectar domínio de e-mail sem abrir a AWS (exige ampliar a política IAM com ses:CreateEmailIdentity).

**Leads da Black da Beatriz perdidos (03/11/2026):** 84 de 192 inscritos do Dash (subconta 19, lançamento 2273) nunca chegaram ao Up; o formulário posta em paginas-beatriz.pages.dev/api/inscrever (código fora das pastas do usuário, conta Cloudflare do Rodrigo), que chama o webhook do Up; causa provável não confirmada: Render free dormindo. Recuperados pela automação "Boas vindas — recuperação" (id 2c4023bc, gatilho tag black-nov/26-recuperado, aprovada pelo usuário). Decisão do usuário: repetir DIARIAMENTE; tarefa agendada bia-recuperar-leads-dash (20h) roda Full Concepty Academy/recuperar-leads-dash.cjs e se desliga após 09/11. Correção definitiva pendente (código da função ou Render Starter).

**Neon (02/11/2026):** o adicional "limit increase" (US$ 10/mês, ligado em 21/10) gerou cobrança proporcional de ~US$ 3,55 em 1º/11; a pedido do usuário voltei a conta para o plano Free (100 CU-h/mês, 1 GB). Banco do Up: 69 MB; consumo projetado ~55–65 CU-h/mês. Se passar de ~80 CU-h, avisar o usuário.
