---
name: up-financeiro
description: Aba Financeiro do Up (26/11/2026): mês a mês por expert, divisão 25/25/50, fixo da Bia R$ 2.000, custos compartilhados metade, notas no Drive por projeto/ano/mês
metadata:
  type: project
---

Decidido pelo Anderson em 26/11/2026 (commit cf0f942, migração 0107):
- Aba **Financeiro** no menu do dono (grupo Gestão) e no painel do expert (só leitura). Um mês por vez (pílulas), como planilha: Item · Origem · Valor cheio · Anderson 25% · Rodrigo 25% · expert 50%.
- Receita e custos: resultado = faturamento Hotmart − taxas/reembolsos − custos, dividido pelos percentuais (configuráveis em "Divisão", somam 100%).
- **Bia paga fixo de R$ 2.000/mês** aos sócios: linha "fee", vai inteira para Anderson e Rodrigo (R$ 1.000 cada) e sai da parte dela. Pedro não tem fixo.
- Custos que servem aos dois (Render, Neon, Cloudflare, assinatura do Claude, Resend, AWS): **metade para cada projeto**. Imposto: **não entra por enquanto**.
- O mês aberto mostra ao vivo o que o Up mede (WhatsApp, e-mail, IA de dentro do Up); "Fechar mês" grava e trava. Recibo real do WhatsApp usa source_key up:whatsapp e substitui o estimado.
- Notas: Drive FINANCEIRO › <Projeto> (Pedro Sachet / Beatriz Vieira / Up (geral)) › AAAA › "MM - Mês". A maioria chega no Gmail da UP Coproduções; Meta (anúncios e WhatsApp) é baixada da central de cobrança. A rotina **recibos-mensais** (dia 1) levanta, pede OK para baixar, salva, lança as linhas (source_key fixos) e liga a pasta do mês (PUT finance/months/<mês>/drive).

**How to apply:** valores novos de custo entram como linha com source_key estável (refazer atualiza). Quem fecha o mês é só o Anderson. Relacionado: [[up-custo-meta-whatsapp]], [[up-neon-plano]].

Atualizado em 26/11/2026:
- **Hotmart divide direto** (coprodução): Pedro 50% (PEDRO SACHET ENSINO ODONTOLOGICO LTDA), Rodrigo 25% (RODRIGO GALBIER ESTRATEGISTA DIGITAL LTDA), lado do Anderson 25% (em nome de Ana Paula Cechim da Costa). Vendas entram como "Hotmart dividiu direto" e não entram no acerto. Linhas por produto, taxa por taxa (source_key hotmart:<id>:faturamento|taxa|juros|imposto|frete).
- **Custos de produção do Pedro** (pagos pelo Pedro): Morfo.Guide + = R$ 94,80 (apostila R$ 50 + modelo R$ 44,80); modelo avulso (morfo.Guide ou morfo.Logic) = R$ 44,80; morfo.Logic digital sem custo.
- **Quem paga (acerto entre sócios)**: Pedro — tráfego e produção = Pedro; Up, Claude Code, WhatsApp, e-mail, IA, ferramentas = Anderson. Bia — tráfego, vturb, ManyChat = Rodrigo; Up, WhatsApp, e-mail, IA = Anderson. Rodrigo não adianta nada no Pedro. Aba mostra "Acerto entre sócios" (quem repassa para quem).
- Produto "Black da Lógica" (8800525) é do Pedro. Produtos da Simioni & Casarolli (Black do Analógico ao Digital 8844243, Prótese Total Natural 7437149) são da Bia.
