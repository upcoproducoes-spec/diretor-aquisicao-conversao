# Diretor de Aquisição e Conversão — Sistema de Skills e Agentes

Sistema para Claude Code que funciona como uma **empresa de marketing e vendas**: um **diretor** (orquestrador) comanda um time de **agentes especialistas** (quem produz) e de **revisores** (quem avalia), todos apoiados em **skills de conhecimento** sintetizadas de cerca de 60 livros, aulas, masterclasses e casos reais.

**Ideia central:** trazer pessoas interessadas, convencê-las a comprar e vender mais, com método e não com achismo. O diretor diagnostica o pedido, monta o briefing de cada especialista, coordena a ordem do trabalho, passa pelos revisores e **só aplica o que o usuário aprovar**. Pipeline completo de 15 fases: diagnóstico → pesquisa → psicologia → posicionamento → oferta → funil → copy → vendas → métricas → otimização → escala.

## O que tem aqui

```
skills/   (conhecimento: 691 capítulos)
  diretor-aquisicao-conversao/   orquestrador mestre (pipeline, roteamento, fluxo de entrega, Modo Revisão)
  estrategia-negocios/           118 capítulos — Sun Tzu, Porter, Rumelt, Collins, Kim & Mauborgne, Lafley & Martin, Mintzberg, Ries & Trout (Positioning), Hormozi ($100M Offers + Lost Chapters)
  psicologia-consumidor/         52 capítulos — Freud (Interpretação dos Sonhos, O Eu e o Id, Cinco Lições) + Kahneman (Rápido e Devagar)
  marketing-digital-growth/      117 capítulos — Hacking Growth, Marketing na Era Digital, Unbound Marketing, Jeff Walker, Seth Godin, Hormozi ($100M Leads + Money Models), Russell Brunson (DotCom Secrets + Expert Secrets), masterclass de Lançamento Pago (Ferrari e Lima), masterclass de Tráfego (Carneiro), workshop de Lançamento Pago (Baldan), StoryBrand (Donald Miller: funil, lead generator e e-mails) e caso de Black Friday (live e campanha em fases)
  persuasao-gatilhos/            94 capítulos — Cialdini (As Armas da Persuasão + Pré-Suasão), Carnegie, Gustavo Ferreira
  copywriting-publicidade/       231 capítulos — Ferreira, Maccedo, Ogilvy, Bencivenga, Carlton, Halbert, Schwartz, Makepeace, Sugarman, Collier, Kennedy, Claude Hopkins, John Caples, Donald Miller (StoryBrand), Thiago Filemon (aulas de VSL e análise do lançamento pago de 2 dias), Thiago Roas (análise do evento de 4 dias, copy LHTCO, criativos), casos analisados (VSL, formatos de anúncio, live e roteiros de Black Friday)
  vendas-metodologia/            61 capítulos — Dixon & Adamson, Gitomer, Ross & Tyler, Rackham, Pink, Chris Voss
  estrategia-trafego-funil/      metodologia de funil de VSL perpétuo e tráfego (inclui atualização do evento de 4 dias e caso de VSL de ticket baixo)
  criacao-conteudo-social-media/ playbook aplicado (fluxo de 8 passos + modelos) que roteia para as skills acima; 18 capítulos próprios (vídeo curto, modelo SHARE de redes sociais e caso de carrossel de captação)

  agente-design/                 agente de design (imagens, criativos, web design, identidade): confere o briefing, produz, passa pelo revisor-design

skills-terceiros/   (19 skills de design de terceiros que o agente de design usa; instaladas junto pelo instalar.ps1)
  design-taste-frontend, ui-ux-pro-max, high-end-visual-design, minimalist-ui, industrial-brutalist-ui, stitch-design-taste,
  frontend-design, ui-styling, imagegen-frontend-web, image-to-code, redesign-existing-projects, impeccable,
  banner-design, brandkit, design, brand, design-system, slides, ads-creative

  Total: 691 capítulos sintetizados de ~60 obras, aulas e casos analisados (inclui 18 da skill de conteúdo).

agents/   (equipe: cada especialidade tem um agente que produz e um revisor)
  estrategista-negocios.md       produz diagnóstico, posicionamento e oferta          → revisor-estrategia.md
  analista-psicologia.md         produz o mapa psicológico do público                 → revisor-psicologia.md
  especialista-growth-funil.md   produz funil, lançamento, tráfego, métricas e testes → revisor-growth.md (+ revisor-funil-vsl.md)
  copywriter.md                  produz headlines, páginas, VSL, e-mails, anúncios    → revisor-copy.md
  especialista-persuasao.md      produz o mapa de gatilhos (trabalha com o copy)      → revisor-persuasao.md
  especialista-vendas.md         produz processo, roteiros e scripts de venda         → revisor-vendas.md
  criador-conteudo.md            produz conteúdo e social media                       → revisor-conteudo.md
  (skill agente-design)          produz peças visuais, criativos, páginas e identidade → revisor-design.md

memoria/  espelho da memória do Claude (regras de trabalho, preferências e estado do projeto): é o que o sistema "aprendeu" com o uso
docs/     resumo do diretor para a equipe e a lista das skills de design de terceiros
instalar.ps1  instala skills, agentes e memória num computador novo
```

## Como funciona (a empresa)

- **Diretor** = o gestor. Roda na conversa principal (é uma skill), diagnostica o pedido, monta o briefing de cada agente (os agentes não veem a conversa), coordena a ordem, consolida os revisores e apresenta ao usuário.
- **Agentes** = os funcionários que produzem. Cada um carrega a skill da sua área e escreve a entrega.
- **Revisores** = quem confere. Só leem e avaliam; nunca editam.
- Os agentes **não acionam uns aos outros**: a ordem é do diretor.

**Fluxo de criativos e peças:** base pronta (estratégia, oferta, público) → briefing por agente → copy (`analista-psicologia` e `especialista-persuasao`, depois `copywriter`) → revisão (`revisor-copy`, `revisor-persuasao` e os de funil quando for o caso) → **aprovação da copy pelo usuário** → Pacote para o Design → design e revisão de design → **aprovação final** antes de publicar ou ativar qualquer coisa em conta de anúncios. As demais entregas seguem o mesmo desenho: agente produz → revisor → diretor consolida → usuário aprova → próxima etapa.

## O que já faz hoje

- **Projeto completo:** diagnóstico, posicionamento, oferta, funil, copy, vendas e plano de métricas, com documento de projeto entre as fases.
- **Pedidos pontuais:** headline, objeção de preço, roteiro de venda, mapa de gatilhos, plano de funil ou de lançamento, plano de conteúdo.
- **Modo Revisão de Projeto:** os 7 revisores auditam em paralelo e devolvem uma tabela de correções, aplicadas só com a aprovação do usuário.
- **Conteúdo e social media:** pilares, calendário, roteiros de vídeo curto, carrosséis, legendas e criativos, com plano de teste.
- **Casos analisados e incorporados:** lançamentos pagos, VSLs, formatos de anúncio, live e campanha de Black Friday, StoryBrand.

## Ainda por construir

- **Agente de design completo:** hoje o design é a skill `agente-design` (com o `revisor-design`), que o diretor aciona depois da copy aprovada e que usa skills de design de terceiros (lista em `docs/skills-de-design-necessarias.md`). Falta transformá-lo em agente da equipe, no mesmo padrão dos demais.
- **Editor de vídeo.**
- **Gestor de tráfego:** hoje o sistema só planeja tráfego (estrutura, orçamento, testes); nenhum agente altera conta de anúncios, e isso exige aprovação do usuário.
- **Testes de ponta a ponta** do fluxo completo com os agentes novos, e glossário/cheatsheet de alguns casos recentes.
- Novas aulas, lançamentos e livros continuam sendo analisados e incorporados ("atualizar, não substituir").

## Como instalar

Copie as pastas para os diretórios pessoais do Claude Code:

```bash
# Windows (PowerShell)
Copy-Item -Recurse skills\* "$env:USERPROFILE\.claude\skills\"
Copy-Item agents\* "$env:USERPROFILE\.claude\agents\"

# macOS/Linux
cp -r skills/* ~/.claude/skills/
cp agents/*.md ~/.claude/agents/
```

Reinicie a sessão do Claude Code (ou abra uma nova) para que as novas skills/agentes sejam carregados. Elas ficam disponíveis em qualquer projeto/conversa, não só no que você estava usando.

### Computador novo (instalação completa, com a memória)

```powershell
git clone https://github.com/upcoproducoes-spec/diretor-aquisicao-conversao.git
cd diretor-aquisicao-conversao
.\instalar.ps1 -PastaProjeto "C:\caminho\da\pasta\onde\voce\vai\abrir\o\Claude"
```

O script instala skills e agentes e copia a **memória** (as regras e preferências que o sistema foi aprendendo) para a pasta de memória do projeto informado. Memória que já existir no computador não é sobrescrita (use `-SobrescreverMemoria` para forçar). Depois: abra o Claude Code nessa pasta e recrie a chave da OpenAI (se for usar o agente de design). As skills de design de terceiros já são instaladas pelo script (`skills-terceiros/`).

### O que este repositório NÃO guarda (de propósito)
- Vídeos, transcrições e PDFs originais de aulas e livros: só entram os capítulos escritos em palavras próprias (direitos autorais).
- Chaves e senhas, como a da OpenAI (`openai.env`). O `.gitignore` bloqueia esses arquivos.
- As skills que vêm de plugins do Claude (`anthropic-skills:*`, `design:*`) e as ferramentas web (chat e painel).

### Manter atualizado
Sempre que skills, agentes ou a memória mudarem, o repositório precisa ser atualizado (copiar `skills`, `agents` e `memoria`, commitar e dar push). O Claude avisa quando o GitHub estiver desatualizado.

## Como usar

Peça diretamente em português — não precisa citar o nome da skill ou do agente. Quanto mais contexto no pedido (produto, preço, público, objetivo, prazo, o que já existe), melhor o resultado.
- **Projeto novo do zero**: "preciso vender X", "crie uma campanha para X" → o diretor ativa o pipeline completo.
- **Pedido pontual**: "escreve uma headline", "como respondo essa objeção de preço" → o diretor aciona direto o agente da especialidade e, depois, o revisor dele.
- **Revisão de projeto**: "revisa esse projeto", "audita isso antes de eu lançar" → ativa o Modo Revisão (os 7 revisores rodam em paralelo e devolvem uma tabela de correções — nada é alterado sem sua aprovação explícita).
- **Conteúdo e social media**: "plano de conteúdo de 4 semanas", "roteiros de Reels", "carrossel", "ganchos" → o diretor aciona o `criador-conteudo` e, antes de publicar, o `revisor-conteudo`.
- **Criativos de ponta a ponta**: converse com o diretor com a estratégia e a oferta já definidas; ele conduz copy → revisão → sua aprovação → design → revisão → sua aprovação final.

**Regras do sistema:** nada é alterado ou publicado sem aprovação; nunca se mexe em conta de anúncios real sem autorização; não se inventa número, escassez, prova social ou promessa de resultado; números vindos de aulas e casos são marcados como "não verificados".

**Atenção ao uso:** agentes rodam em contexto separado e gastam mais do limite de uso do que as skills; para tarefas pequenas, prefira pedidos pontuais.

## Ferramentas web (opcionais, fora deste repositório)

- **Chat rápido** (sem precisar do Claude Code instalado): responde com base nos frameworks centrais das 6 skills.
- **Painel de tarefas** (tipo Trello, por projeto, atualiza em tempo real para a equipe).

Peça os links atualizados na conversa com o Diretor caso precise reenviar para alguém.

## Aviso sobre direitos autorais

O conteúdo destas skills é **sintetizado** (frameworks, princípios e técnicas reescritos, nunca texto copiado literalmente) a partir de ~60 obras e aulas, a maioria ainda sob direitos autorais ativos (Ogilvy, Halbert, Schwartz, Kennedy, Cialdini, Porter, etc.). Isso torna este repositório adequado para **uso privado/interno** (você, sua equipe, colaboradores autorizados), mas não para distribuição pública livre. Mantenha este repositório **privado**.
