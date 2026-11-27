# Regras de trabalho do usuário (valem em qualquer pasta)

## Idioma
- Responda em português do Brasil.

## Sistema de marketing e vendas (Diretor de Aquisição e Conversão)
- Para qualquer pedido de aquisição, vendas, lançamento, oferta, funil, copy, tráfego pago, conteúdo ou design de peças, comece pelo **diretor** (skill `diretor-aquisicao-conversao`, a de `~/.claude/skills`, não a versão de plugin).
- O diretor coordena; cada especialidade tem um **agente que produz** e um **revisor** que só lê; o usuário aprova. Os agentes não acionam uns aos outros: a ordem é do diretor.
- Skills em `~/.claude/skills`, agentes em `~/.claude/agents`. Repositório privado de backup: `upcoproducoes-spec/diretor-aquisicao-conversao` (local: `C:\Users\User\Documents\diretor-aquisicao-conversao`). O guia de instalação num computador novo está no `README.md` do repositório (`instalar.ps1`).

## Regras permanentes
- **Atualizar, não substituir.** Depois de atualizar, apague os restos antigos.
- **Aula, lançamento, vídeo ou caso novo:** faça análise completa da estratégia (estrutura dia a dia, ganchos, loops abertos, gatilhos, história e prova, construção de crença, oferta e pitch, objeções, ritmo), sem tratar a parte promocional como ruído. Classifique o tema e roteie para as skills certas, com índices, orquestrador, revisores e memória.
- **Conteúdo de terceiros:** sintetize em palavras próprias, nunca copie texto. Números vindos de aulas e casos são "não verificados". Sinalize riscos éticos, de política de plataforma e de LGPD.
- **Sirius Scale (atualizado em 2026-11-27, por decisão do usuário):** a inteligência da Sirius é construída em conjunto pelo Anderson e pelo Rodrigo (sócio) e é do Anderson também: pode ser absorvida em todos os projetos, na central de estratégia, nas skills, nos agentes, subagentes e revisores, e pode ir para o repositório do GitHub. As APIs e chaves são sempre as nossas, nunca as da Sirius.
- **Central de estratégia:** `C:\Users\User\Documents\Claude\Estrategia UP` guarda a estratégia comum de todos os projetos (playbook, Sirius, decisões "levar para o outro projeto?"). Os arquivos de cada projeto ficam na pasta do projeto.
- **Nunca invente** número, escassez, prazo, prova social, depoimento ou promessa de resultado.
- **Contas de anúncios reais (atualizado em 2026-11-24, por decisão do usuário):** o gestor de tráfego **pode executar** na conta, pela conversa principal com o conector (o subagente `gestor-trafego` segue sem acesso e só prepara): montar campanha **pausada**, ligar e desligar, orçamento, edição e otimização, **quando o usuário pedir ou aprovar a sugestão**. Sem pedido ou aprovação, nada é feito; a aprovação vale para **aquela ação naquele dia**. Regras de execução: uma mudança por objeto por dia, registrar cada ação (o quê, antes e depois, motivo, como desfazer, janela de medição), campanha criada nasce pausada e só liga com ordem, **excluir** exige confirmação específica, e nunca ligar ou aumentar verba por iniciativa própria.
- **Credenciais:** nunca no chat nem em arquivos do repositório. O usuário cola chaves em arquivos locais (por exemplo `~/.claude/openai.env`). Nunca imprima chaves.
- Peça permissão antes de baixar arquivos, enviar mensagens ou publicar algo.

## GitHub e memória
- **Commits e PRs sem linhas de atribuição.**
- Mantenha o repositório atualizado: depois de mudar skills, agentes ou memória, espelhe tudo (`skills`, `skills-terceiros`, `agents`, `agents-terceiros`, `memoria`, `docs`), confira se não há chaves ou dados sensíveis, faça commit e push, e avise o usuário.
- Nunca suba para o repositório: chaves e senhas, vídeos, áudios, PDFs ou transcrições originais de aulas e livros (só capítulos em palavras próprias).
- A memória do Claude é espelhada em `memoria/` do repositório; ao mudar a memória, atualize o espelho.

## Planejado (ainda não feito)
- Editor de vídeo: o agente `editor-video` (com `revisor-video`) foi criado em 2026-11-24; falta instalar/testar o módulo de vídeo e a primeira peça de ponta a ponta.
- O diretor deve guiar a instalação completa num computador novo, incluindo ligar a API da OpenAI para gerar imagens (e vídeo, se for preciso). Hoje: a chave fica em `~/.claude/openai.env`, colada pelo usuário.
