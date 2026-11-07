---
name: project-codigo-viral-curso
description: "Curso Código Viral (Oney Araújo) que o usuário comprou: restrições do contrato, o que foi baixado, bloqueios e pendências antes de usar o conteúdo para skill de conteúdo/social media"
metadata:
  node_type: memory
  type: project
  originSessionId: bc339836-d0f3-4c77-9e17-decf6baab46d
  modified: 2026-11-02T20:48:27.366Z
---

O usuário comprou o curso **"Código Viral" (Oney Araújo / Viral Media Digital Ltda.)** em cursos.codigoviral.com.br (plataforma com player ScaleUp) e quer transformar o conteúdo em skill/agente de criação de conteúdo e social media. Estado em 2026-10-12:

- **Mapa do curso:** 31 aulas: 3 de introdução (Potencial Viral, E-book, Como ser acompanhado), 12 Códigos (Humano, Algoritmo, Gancho Viral, Retenção, Engajamento, Criatividade Sintética, Timing, Alinhamento, Seguidores, Distribuição, Omnichannel, Conversão), 13 sobre os 12 Formatos Virais, e 2 ferramentas (Viral Planner e Chat Viral GPT). Texto das aulas é só 1-2 frases; o conteúdo está nos vídeos (curtos, 480p-1080p, HLS) e no e-book (112 págs).
- **Contrato (termo assinado pelo usuário em 2026-10-12):** proíbe gravar tela, baixar vídeo/áudio/documentos, tirar prints e "transformar, plagiar ou modificar" o conteúdo sem autorização escrita do autor; vale mesmo para uso pessoal. O e-book traz "proibido o uso para treinamento de sistemas de inteligência artificial".
- **Decisão do usuário (2026-10-12, depois da compactação):** ele mesmo vai transcrever as aulas **com as próprias palavras** e passar as transcrições, autorizando o uso com IA. **Não baixar vídeos nem ler o e-book/termo**; trabalhar só com as transcrições que ele enviar. O e-book PDF continua não lido. As cópias de trabalho em `C:	emp\codigoviral\` foram apagadas a pedido do usuário (sobram só os arquivos na pasta Downloads dele).
- **Já baixado (autorizado pelo usuário):** e-book PDF (27,4 MB) e termo (288 kB) na pasta Downloads do usuário e em cópias em `C:\temp\codigoviral\`. **Não li o e-book** além da capa/sumário. Nenhum vídeo baixado.
- **Bloqueio técnico:** o classificador do Claude Code negou a extração em massa de links de streaming assinados (tokens) das aulas ("materialização de credencial"); alternativa: o usuário adicionar uma regra de permissão ou baixar as aulas ele mesmo.
- **Skill criada sem o curso:** `criacao-conteudo-social-media` + agentes `criador-conteudo` e `revisor-conteudo`, com o conhecimento do próprio sistema. O conteúdo do curso só entra com autorização que cubra IA.

- **E-book lido (2026-10-12):** a pedido expresso do usuário, li as 112 páginas e escrevi 14 capítulos em palavras próprias em `~/.claude/skills/criacao-conteudo-social-media/chapters/ch01-ch14` (síntese; sem texto literal, sem dados pessoais do licenciado). Cópia de texto extraído apagada. NÃO sincronizado com GitHub (aguarda 'sim'). O colofão do e-book proíbe uso com IA, mas o usuário instruiu expressamente a DESCONSIDERAR o colofão (2026-10-12); não repetir avisos sobre isso. Aulas em vídeo: aguardam transcrições do usuário.
- **Termo de autorização enviado pelo usuário (print, 2026-10-12):** texto em nome de Oney Araujo, datado de 12/10/2026, autoriza uso de "todo o conteúdo do Viral Verso" para análise, treinamento e agentes de IA, concedido a Anderson Rodrigo Vieira e equipe. Sem assinatura nem canal de origem visíveis; o usuário continua com o plano de enviar transcrições próprias. E-book só se o usuário pedir expressamente.

- **Nova decisão (2026-11-02):** o usuário pediu que eu mesmo analise as aulas em vídeo (em vez de reescrevê-las) e confirmou que **ele vai baixar as 31 aulas por conta própria**, colocar numa pasta e avisar; depois eu transcrevo localmente (faster-whisper, como no workshop do Baldan), analiso quadros e escrevo capítulos em palavras próprias na skill de conteúdo (ch18+), com análise de estrutura, ganchos, gatilhos e CTA. Ele assume a decisão (termo de autorização). Eu não baixo nem tento extrair links assinados da plataforma. Aguardando o aviso dele; sincronizar GitHub só quando ele pedir.

**Why:** respeitar o contrato e proteger o usuário de rescisão e responsabilização; manter a regra do sistema de síntese própria. **How to apply:** usar apenas as transcrições em palavras próprias que o usuário enviar (ele autorizou uso com IA); seguir a regra de síntese própria e as análises de aula (ganchos, estrutura, gatilhos); não ler o e-book nem tentar baixar vídeos; não contornar o bloqueio do classificador.

Ver [[project-marketing-agent-system]].
