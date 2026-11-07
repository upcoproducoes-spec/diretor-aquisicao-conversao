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
- **Nunca invente** número, escassez, prazo, prova social, depoimento ou promessa de resultado.
- **Contas de anúncios reais:** só o usuário aprova e executa qualquer mudança (ativar, pausar, orçamento, publicar, excluir). A aprovação vale para aquela ação naquele dia. Agentes só planejam e propõem.
- **Credenciais:** nunca no chat nem em arquivos do repositório. O usuário cola chaves em arquivos locais (por exemplo `~/.claude/openai.env`). Nunca imprima chaves.
- Peça permissão antes de baixar arquivos, enviar mensagens ou publicar algo.

## GitHub e memória
- **Commits e PRs sem linhas de atribuição.**
- Mantenha o repositório atualizado: depois de mudar skills, agentes ou memória, espelhe tudo (`skills`, `skills-terceiros`, `agents`, `agents-terceiros`, `memoria`, `docs`), confira se não há chaves ou dados sensíveis, faça commit e push, e avise o usuário.
- Nunca suba para o repositório: chaves e senhas, vídeos, áudios, PDFs ou transcrições originais de aulas e livros (só capítulos em palavras próprias).
- A memória do Claude é espelhada em `memoria/` do repositório; ao mudar a memória, atualize o espelho.

## Planejado (ainda não feito)
- Agente editor de vídeo (por enquanto, não mexer).
- O diretor deve guiar a instalação completa num computador novo, incluindo ligar a API da OpenAI para gerar imagens (e vídeo, se for preciso). Hoje: a chave fica em `~/.claude/openai.env`, colada pelo usuário.
