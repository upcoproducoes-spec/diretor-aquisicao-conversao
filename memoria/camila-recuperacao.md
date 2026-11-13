---
name: camila-recuperacao
description: "Camila = agente de recuperação de vendas no WhatsApp, uma só no Up para todos os projetos; v1 só carrinho abandonado; modelos utility sem cara de venda"
metadata:
  node_type: memory
  type: project
  originSessionId: fb170dd5-bc95-459a-b6db-63cb8781a538
  modified: 2026-11-13T10:50:16.515Z
---

Decisões do Anderson (12/11/2026):
- **Uma Camila para todos os projetos.** A construção é geral no Up; cada projeto entra só com a inteligência dele (produtos, ofertas, preços, links, objeções, tom).
- **v1 = só carrinho abandonado** (Hotmart), que vale para qualquer projeto, inclusive perpétuo (morfoGuide), onde não há inscrição.
- **Depois:** em eventos (gratuitos, pagos, Black) a Camila chama também os **inscritos que não compraram**, no dia seguinte à abertura do carrinho. Na Black do Pedro (carrinho 25/11) isso já entra. As regras vão sendo melhoradas.
- **Abertura só com modelo UTILITY**, sem soar como venda: aviso real ("seu pedido ficou em aberto", "temos uma atualização sobre o evento em que você se inscreveu", "o pagamento venceu, quer que eu gere outro?") e botão "Ver detalhes"; a conversa (e a venda) vem depois do clique, dentro da janela de 24 h. Saudação simples, sem "equipe do Pedro" ([[whatsapp-utility-e-saudacao]]).
- Modelos do Pedro enviados à Meta em 13/11 (PENDING): `pedido_em_aberto` (carrinho), `atualizacao_inscricao` (inscritos), `pagamento_vencido` (boleto/Pix, para depois).
- **Construída no Up em 13/11** (commit 6a0695e, migração 0089): tela Camila, passo "Passar para a Camila", modo treino/automático, link só do Conhecimento. Pedro: Camila DESLIGADA até a chave de IA (o projeto só tem OpenAI; Claude não cadastrado). Automações de carrinho abandonado criadas DESLIGADAS: Físico (tag morfoguide-br-abandono-de-carrinho, id 32fa170f) e Híbrido (tag morfoguide-br-hibrido-abandono-de-carrinho, id 0ded4190): espera 30 min 8h-21h → se comprou qualquer versão encerra → pedido_em_aberto → Ver detalhes → Camila. Ligar só com o modelo aprovado e teste no número do dono.
- Conhecimento "Links de checkout (Camila)": Físico https://pay.hotmart.com/P104766999J?off=wctgpqk5 (sem cupom); Híbrido com cupom CAMILA15OFF (15%, criado em 13/11 no combo morfo.Guide híbrido + 7377587, R$ 349 → R$ 296,65) https://pay.hotmart.com/F104889989N?off=u4gmvjw3&checkoutMode=10&offDiscount=CAMILA15OFF (o checkoutMode=10 é o que aplica o cupom sozinho). Uma oferta por vez. Morfoguide Físico e Híbrido são COMBOS na Hotmart (Produtos > Combos).
- Depois (tarefa no quadro do Pedro, com o diretor): Camila vender o morfoLogic para quem comprou o morfoGuide e não pegou upsell/downsell (funil low ticket de 2 ciclos e webinário semanal).

**Why:** recuperar vendas em todos os projetos sem depender de outra ferramenta ([[fullfunnel-encerrado]]).
**How to apply:** construir genérico (configuração por projeto), começar pelo carrinho abandonado; nunca inventar prazo, escassez ou desconto; se perguntarem, ela diz que é assistente virtual. Meta pode reclassificar aviso de carrinho como marketing: conferir a categoria aprovada.
