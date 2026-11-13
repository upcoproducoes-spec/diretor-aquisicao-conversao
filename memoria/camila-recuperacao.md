---
name: camila-recuperacao
description: "Camila = agente de recuperação de vendas no WhatsApp, uma só no Up para todos os projetos; v1 só carrinho abandonado; modelos utility sem cara de venda"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-13T12:20:34.734Z
---

Decisões do Anderson (12/11/2026):
- **Uma Camila para todos os projetos.** A construção é geral no Up; cada projeto entra só com a inteligência dele (produtos, ofertas, preços, links, objeções, tom).
- **v1 = só carrinho abandonado** (Hotmart), que vale para qualquer projeto, inclusive perpétuo (morfoGuide), onde não há inscrição.
- **Depois:** em eventos (gratuitos, pagos, Black) a Camila chama também os **inscritos que não compraram**, no dia seguinte à abertura do carrinho. Na Black do Pedro (carrinho 25/11) isso já entra. As regras vão sendo melhoradas.
- **Abertura só com modelo UTILITY**, sem soar como venda: aviso real ("seu pedido ficou em aberto", "temos uma atualização sobre o evento em que você se inscreveu", "o pagamento venceu, quer que eu gere outro?") e botão "Ver detalhes"; a conversa (e a venda) vem depois do clique, dentro da janela de 24 h. Saudação simples, sem "equipe do Pedro" ([[whatsapp-utility-e-saudacao]]).
- Modelos do Pedro enviados à Meta em 13/11 (PENDING): `pedido_em_aberto` (carrinho), `atualizacao_inscricao` (inscritos), `pagamento_vencido` (boleto/Pix, para depois).
- **Construída no Up em 13/11** (commit 6a0695e, migração 0089): tela Camila, passo "Passar para a Camila", modo treino/automático, link só do Conhecimento. Pedro: Camila DESLIGADA até a chave de IA (o projeto só tem OpenAI; Claude não cadastrado). Automações de carrinho abandonado criadas DESLIGADAS: Físico (tag morfoguide-br-abandono-de-carrinho, id 32fa170f) e Híbrido (tag morfoguide-br-hibrido-abandono-de-carrinho, id 0ded4190): espera 30 min 8h-21h → se comprou qualquer versão encerra → pedido_em_aberto → Ver detalhes → Camila. Ligar só com o modelo aprovado e teste no número do dono.
- Conhecimento "Links de checkout (Camila)": Físico https://pay.hotmart.com/P104766999J?off=wctgpqk5 (sem cupom); Híbrido com cupom CAMILA15OFF (15%, criado em 13/11 no combo morfo.Guide híbrido + 7377587, R$ 349 → R$ 296,65) https://pay.hotmart.com/F104889989N?off=u4gmvjw3&checkoutMode=10&offDiscount=CAMILA15OFF (o checkoutMode=10 é o que aplica o cupom sozinho). Uma oferta por vez. Morfoguide Físico e Híbrido são COMBOS na Hotmart (Produtos > Combos).
- "Carta do curso" nas instruções da Camila (13/11): só no um a um, se a pessoa queria o morfoLogic e o valor cheio pesa, ela diz que ao concluir o morfoGuide aparece na página a condição do curso (1 ano R$ 1.197; se ainda caro, 6 meses R$ 697). O funil de upsell/downsell aparece depois da compra das DUAS versões (Físico e Híbrido), confirmado pelo Anderson.
- Modelos: os 3 primeiros vieram MARKETING (13/11); Anderson pediu revisão à Meta e quer só utility. Criadas 8 versões utility (status_pedido_pendente, pedido_pagamento_nao_confirmado, pedido_nao_finalizado, boleto_pix_vencido, prazo_pagamento_expirado, aviso_inscricao_evento, lembrete_evento_inscrito, inscricao_evento_atualizada), enviadas em 13/11. Usar na automação a primeira de carrinho que vier UTILITY.
- Camila com áudio (commit b933cb7, migração 0090): transcreve áudio (OpenAI) e, se ligado em Configurações, responde em áudio (voz coral/nova). Pedro: ligada, treino, OpenAI gpt-4.1, resposta em áudio desligada.
- Depois (tarefa no quadro do Pedro, com o diretor): Camila vender o morfoLogic para quem comprou o morfoGuide e não pegou upsell/downsell (funil low ticket de 2 ciclos e webinário semanal).
- **13/11 (tarde):** link da Camila sai sempre com UTM própria: utm_source=whatsapp, utm_medium=recuperacao, utm_content=camila, utm_term=camila (mantém utm_campaign/utm_id do link; sem campanha vira recuperacao_camila) e sck=camila no checkout da Hotmart (commit f34b88c). Pedido do Anderson: saber que a venda veio da Camila.
- **Regras de recontato construídas em 13/11** (commit 3188875, migração 0093): valem no passo send_template marcado como "aviso de recuperação" (recovery: true, com product). R1 compra/não quero encerra o produto; R2 1 aviso/24 h e abandonos seguidos viram 1 (teto 2 h); R3 2 sem resposta = pausa 30 dias; R4 até 4 em 30 dias; R5 qualidade Média/Baixa só a 1ª tentativa, 2 falhas de entrega param. Ficha da pessoa no detalhe da conversa e no contexto da IA. Falta: Pix/boleto e Instagram.
- **Boleto/Pix vencido ativado em 13/11** (automação c1dc4acc): gatilho hotmart.purchase_expired do produto 7330221 (morfoGuide Físico) → espera 30 min 8h-21h → se comprou encerra → modelo utility boleto_pix_vencido (aviso de recuperação, regras de recontato) → Ver detalhes → Camila (motivo pagamento_vencido). Híbrido: fazer igual quando ligar o carrinho do Híbrido.

**Why:** recuperar vendas em todos os projetos sem depender de outra ferramenta ([[fullfunnel-encerrado]]).
**How to apply:** construir genérico (configuração por projeto), começar pelo carrinho abandonado; nunca inventar prazo, escassez ou desconto; se perguntarem, ela diz que é assistente virtual. Meta pode reclassificar aviso de carrinho como marketing: conferir a categoria aprovada.
