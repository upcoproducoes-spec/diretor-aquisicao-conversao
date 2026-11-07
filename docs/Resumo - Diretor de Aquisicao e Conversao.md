# Diretor de Aquisição e Conversão

Repositório (privado): https://github.com/upcoproducoes-spec/diretor-aquisicao-conversao

## Ideia central
É uma empresa de marketing e vendas dentro do Claude Code. O objetivo é trazer pessoas interessadas, convencê-las a comprar e vender mais, com método e não com achismo.

- **Diretor:** o gestor. Diagnostica o pedido, monta o briefing de cada agente, coordena a ordem, junta os pareceres dos revisores e só aplica o que você aprovar.
- **Agentes:** os funcionários que produzem.
- **Revisores:** quem confere. Só leem e avaliam.
- **Skills:** o conhecimento por trás de todos, com 691 capítulos tirados de cerca de 60 livros, aulas e casos reais.

## O que já está construído

| Especialidade | Agente que produz | Revisor |
|---|---|---|
| Estratégia e oferta | `estrategista-negocios` | `revisor-estrategia` |
| Psicologia do consumidor | `analista-psicologia` | `revisor-psicologia` |
| Growth, funil e tráfego | `especialista-growth-funil` | `revisor-growth` (mais `revisor-funil-vsl` se houver VSL ou tráfego pago) |
| Copy | `copywriter` | `revisor-copy` |
| Persuasão | `especialista-persuasao` | `revisor-persuasao` |
| Vendas | `especialista-vendas` | `revisor-vendas` |
| Conteúdo e social media | `criador-conteudo` | `revisor-conteudo` |

- **Diretor:** o orquestrador, com pipeline de 15 fases, roteamento e Modo Revisão.
- **Conhecimento:** 8 skills, incluindo a de conteúdo e a de tráfego e funil.
- **Casos incorporados:** lançamentos pagos, VSLs, formatos de anúncio, a live e a campanha de Black Friday, StoryBrand.
- **Design:** já existe a skill `agente-design`, com o `revisor-design`, que também está no repositório. O diretor a chama depois da copy aprovada. Ela usa skills de design de terceiros, que também estão no repositório (pasta `skills-terceiros`, 64 skills no total, incluindo as de tráfego pago `ads-*`, `humanizer` e outras) e são instaladas junto. O arquivo `docs/mapa-skills-por-agente.md` diz qual skill cada agente chama.

## O que já faz hoje
- **Projeto completo:** diagnóstico → posicionamento → oferta → funil → copy → vendas → métricas.
- **Pedido pontual:** uma headline, uma objeção de preço, um roteiro de venda, um mapa de gatilhos, um plano de funil ou de lançamento.
- **Revisão:** os 7 revisores auditam em paralelo e devolvem uma tabela de correções.
- **Conteúdo:** pilares, calendário, roteiros, carrosséis, legendas e criativos, com plano de teste.
- **Fluxo de criativos:** copy → revisão → sua aprovação → design → revisão → sua aprovação final.

## O que ainda falta construir
- **Agente de design completo:** hoje é uma skill. Falta transformá-lo em agente da equipe (imagens, criativos e web design), no mesmo padrão dos outros.
- **Editor de vídeo.**
- **Gestor de tráfego:** hoje o sistema só planeja e nenhum agente altera conta de anúncios. Qualquer mudança real continua dependendo de você.
- **Teste de ponta a ponta:** os agentes novos ainda não foram rodados juntos. Eles só aparecem depois de reiniciar o Claude Code.
- **Novas aulas e lançamentos:** continuam entrando conforme forem enviados.

## Como instalar (uma vez)
1. Ter o Claude Code instalado.
2. Baixar o repositório (botão **Code → Download ZIP**) ou clonar.
3. Copiar a pasta `skills` para `C:\Users\<usuário>\.claude\skills\` e a pasta `agents` para `C:\Users\<usuário>\.claude\agents\`. No Windows, também dá com:
   - `Copy-Item -Recurse skills\* "$env:USERPROFILE\.claude\skills\"`
   - `Copy-Item agents\* "$env:USERPROFILE\.claude\agents\"`
4. Fechar e abrir o Claude Code. Depois disso ele funciona em qualquer pasta ou conversa.

## Como usar
Converse em português, sem citar nomes de agentes. Quanto mais contexto (produto, preço, público, objetivo, prazo), melhor.
- **Projeto novo:** "preciso vender X" ou "crie uma campanha para X".
- **Pedido pontual:** "escreve uma headline" ou "como respondo a objeção de preço".
- **Revisão:** "revisa esse projeto antes de eu lançar".
- **Conteúdo:** "plano de conteúdo de 4 semanas" ou "roteiros de Reels".
- **Criativos:** converse com o diretor com estratégia e oferta já definidas. Ele conduz o fluxo e pede sua aprovação nos pontos certos.

## Regras que valem sempre
- Nada é alterado ou publicado sem aprovação.
- Não se inventa número, escassez, prova social ou promessa de resultado.
- Números de aulas e casos são marcados como "não verificados".
- Agentes gastam mais do limite de uso que as skills. Para tarefas pequenas, prefira pedidos pontuais.
- O repositório é **privado**: o conteúdo é sintetizado de obras com direitos autorais e serve só para uso interno da equipe. Não compartilhe fora dela.
