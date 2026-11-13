# Diretor de Aquisição e Conversão

Repositório (privado): https://github.com/upcoproducoes-spec/diretor-aquisicao-conversao

## Ideia central
É uma empresa de marketing e vendas dentro do Claude Code. O objetivo é trazer pessoas interessadas, convencê-las a comprar e vender mais, com método e não com achismo.

- **Diretor:** o gestor. Diagnostica o pedido, monta o briefing de cada agente, coordena a ordem, junta os pareceres dos revisores e só aplica o que você aprovar.
- **Agentes:** os funcionários que produzem.
- **Revisores:** quem confere. Só leem e avaliam.
- **Skills:** o conhecimento por trás de todos, com 693 capítulos tirados de cerca de 60 livros, aulas e casos reais.

## O que já está construído

| Especialidade | Agente que produz | Revisor |
|---|---|---|
| Estratégia e oferta | `estrategista-negocios` | `revisor-estrategia` |
| Psicologia do consumidor | `analista-psicologia` | `revisor-psicologia` |
| Growth, funil e estratégia de lançamento | `especialista-growth-funil` | `revisor-growth` (mais `revisor-funil-vsl` se houver VSL ou tráfego pago) |
| Tráfego pago (mídia, orçamento, rastreio, testes, relatório) | `gestor-trafego` | `revisor-trafego` (mais `revisor-funil-vsl` se houver VSL) |
| Design e peças visuais | `designer` | `revisor-design` |
| Copy | `copywriter` | `revisor-copy` |
| Persuasão | `especialista-persuasao` | `revisor-persuasao` |
| Vendas | `especialista-vendas` | `revisor-vendas` |
| Conteúdo e social media | `criador-conteudo` | `revisor-conteudo` |

- **Diretor:** o orquestrador, com pipeline de 15 fases, roteamento e Modo Revisão.
- **Conhecimento:** 8 skills, incluindo a de conteúdo e a de tráfego e funil.
- **Casos incorporados:** lançamentos pagos, VSLs, formatos de anúncio, a live e a campanha de Black Friday, o funil de low ticket com a "Teia", StoryBrand.
- **Design:** o agente `designer` (com o `revisor-design`), que o diretor chama depois da copy aprovada. Gera imagens pela OpenAI quando você autoriza. O método dele está na skill `agente-design`.
- **Tráfego pago:** o agente `gestor-trafego` (com o `revisor-trafego`). Planeja mídia, rastreio, testes e relatórios e **só propõe**: ele não tem acesso às contas de anúncios.
- **Skills e agentes de terceiros:** estão no repositório (`skills-terceiros`, 64 skills, e `agents-terceiros`, 25 agentes) e são instalados junto. O arquivo `docs/mapa-skills-por-agente.md` diz qual skill cada agente chama.
- **CLAUDE.md global:** suas regras de trabalho valem em qualquer pasta (arquivo `config/CLAUDE.md`, instalado em `~/.claude/CLAUDE.md`).

## O que já faz hoje
- **Projeto completo:** diagnóstico → posicionamento → oferta → funil → copy → vendas → métricas.
- **Pedido pontual:** uma headline, uma objeção de preço, um roteiro de venda, um mapa de gatilhos, um plano de funil ou de lançamento.
- **Revisão:** os 7 revisores auditam em paralelo e devolvem uma tabela de correções.
- **Conteúdo:** pilares, calendário, roteiros, carrosséis, legendas e criativos, com plano de teste.
- **Fluxo de criativos:** copy → revisão → sua aprovação → design → revisão → sua aprovação final.

## O que ainda falta construir
- **Editor de vídeo:** ainda não iniciado.
- **Instalação guiada pelo diretor:** num computador novo, o diretor conduzir tudo, incluindo ligar a API da OpenAI para gerar imagens (e vídeo, se for preciso). Hoje você cola a chave num arquivo local.
- **Teste de ponta a ponta:** os agentes novos (incluindo `gestor-trafego`, `revisor-trafego` e `designer`) ainda não foram rodados juntos. Eles só aparecem depois de reiniciar o Claude Code.
- **Novas aulas e lançamentos:** continuam entrando conforme forem enviados.

## Como instalar (uma vez)
1. Ter o Claude Code instalado.
2. Baixar o repositório (botão **Code → Download ZIP**) ou clonar.
3. No Windows, abrir o PowerShell na pasta do repositório e rodar `.\instalar.ps1`. Ele instala skills, agentes, skills e agentes de terceiros e o `CLAUDE.md` global. Para instalar também a memória (as regras aprendidas), acrescente `-PastaProjeto "<pasta onde você abre o Claude>"`.
4. Fechar e abrir o Claude Code. Depois disso ele funciona em qualquer pasta ou conversa.
5. Só para quem vai gerar imagens com o design: criar o arquivo `C:\Users\<usuário>\.claude\openai.env` com a linha `OPENAI_API_KEY=...`, colando a chave você mesmo (nunca no chat).

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
