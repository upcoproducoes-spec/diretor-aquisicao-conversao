---
name: up-aba-trafego-decisoes
description: "Respostas do Anderson (24/11/2026) às decisões da aba Tráfego do Up: total da venda, CPA alvo do Pedro, presença na live, Dashfácil como conferência"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-25T03:03:35.793Z
---

Respostas de 24/11/2026 às 7 decisões de `Up/docs/10-aba-trafego.md` (o áudio veio misturado com barulho; o que ficou claro):
1. **Coprodução:** mostrar o **total** da venda.
2. **CPA alvo da Black do Pedro:** R$ 300 (ele disse "pode ser, tipo, R$ 300"; tratar como valor inicial editável).
3. **CPA alvo do morfoguide BR e ES:** 25% a 30% do valor vendido (ticket). Alvo = 25%, limite de alerta = 30%.
4. **Presença na live:** não rastrear pessoa a pessoa (há vários canais: e-mail, WhatsApp, grupo). Registrar só o **número de comparecimento**, puxado do YouTube.
5. **Rastreio até a Hotmart:** Claude confere sozinho (src/sck nas vendas); confirmar sempre com o Dashfácil, que tem dados a mais.
6. Sem resposta: CPA da Bia (R$ 200, todas ou só pago), Morfoguide ES (Espanha ou hispânico) e as 2 semanas ao lado do Dashfácil. Estratégia ele vai tratar na sessão do Pedro.

**Leva 2 (24-25/11/2026, decisão do Anderson):** a aba é onde a **rotina diária** entrega o que o gestor entrega na conversa: panorama por frente (Funil BR, Funil ES, Black; lendo Meta, Dashfácil, Hotmart e **vturb**) e sugestões por campanha/conjunto/anúncio com Aceitar/Recusar/Descartar. **Aceitar = aprovação daquela ação naquele dia**; quem aplica no Gerenciador é a rotina `up-trafego-pedro-aplicar` (a cada 30 min, pelo conector), nunca o Up. Análise: `up-trafego-pedro-analise` (7h30). Só chave de usuário decide. Ele também quer **números ao vivo** na tela: botão "Conectar com Facebook" (config "Up - Tráfego (ads_read)" id 2973397816386311, token de usuário ~60 dias; ligar o app ao negócio do Pedro para usuário do sistema ele achou complicado). Frentes no Pedro, todas na CA01 507486585521313 (o ES está na mesma conta). Commit b08c3c7, migração 0099.

**Why:** destravar a construção; ele pediu "vamos focar na construção do Up aqui".
**How to apply:** CPA alvo e metas são campos configuráveis por projeto/lançamento na aba, nunca fixos no código. Ver [[up-build-order-oct16]].
