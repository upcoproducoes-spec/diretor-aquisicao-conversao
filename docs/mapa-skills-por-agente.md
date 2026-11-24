# Mapa: qual skill cada agente chama

Regra do sistema: o **diretor** coordena; cada **agente** de especialidade carrega só as skills da sua área quando precisa; cada agente tem o seu **revisor**. Este mapa diz qual skill cada agente chama. O editor de vídeo (seção 4) foi criado em 2026-11-24.

As skills e agentes de terceiros estão neste repositório em `skills-terceiros/` e `agents-terceiros/` (o `instalar.ps1` instala tudo). As descrições abaixo são resumos das descrições das próprias skills; confira o `SKILL.md` de cada uma antes de depender dela.

---

## 1. Agentes que já existem (skills próprias do sistema)

| Agente | Revisor | Skills de conhecimento |
|---|---|---|
| `estrategista-negocios` | `revisor-estrategia` | `estrategia-negocios`, `psicologia-consumidor`, `marketing-digital-growth` |
| `analista-psicologia` | `revisor-psicologia` | `psicologia-consumidor`, `persuasao-gatilhos` |
| `especialista-growth-funil` | `revisor-growth` (+ `revisor-funil-vsl`) | `marketing-digital-growth`, `estrategia-trafego-funil` |
| `copywriter` | `revisor-copy` | `copywriting-publicidade`, `persuasao-gatilhos` |
| `especialista-persuasao` | `revisor-persuasao` | `persuasao-gatilhos`, `psicologia-consumidor` |
| `especialista-vendas` | `revisor-vendas` | `vendas-metodologia`, `persuasao-gatilhos` |
| `criador-conteudo` | `revisor-conteudo` | `criacao-conteudo-social-media` (roteia para as demais) + pacote Instagram `ig-*` com a camada `ig-pt-br` |
| `gestor-trafego` | `revisor-trafego` (+ `revisor-funil-vsl` se houver VSL) | `estrategia-trafego-funil` + as `ads-*` (seção 3) |
| `designer` | `revisor-design` | `agente-design` + as skills de design (seção 2) |

### Ferramentas de terceiros que ajudam o copy e o conteúdo (já instaladas)
- `humanizer`: tira as marcas de "texto escrito por IA" de um texto pronto. Foi feita com base em padrões do inglês; em português, use como revisão final e confira o resultado, não aplique às cegas.
- `mkt-ad-creative`: gera e itera criativos e textos de anúncio em escala (em inglês).
- `ads-create`: conceitos de campanha, mensagens e briefings de criativo a partir de perfil de marca e objetivo.
- **Pacote Instagram (`instagram-agent-skill`, de Jake Schincariol, licença MIT, 13 skills `ig-*`):** `ig-viral` (pesquisa o que funciona no nicho e monta o arquivo de referências), `ig-plan` (semana de posts e engajamento), `ig-reel` (Reel a partir de uma ideia, com gancho pontuado e roteiro cronometrado), `ig-carousel`, `ig-caption`, `ig-story`, `ig-audit` (o que funcionou nos posts já feitos), `ig-profile`, `ig-comment`, `ig-reply`, `ig-dm`, `ig-repurpose` e `ig-human`. Gratuito, sem chave de API, e os 6 scripts Python rodam local, só com a biblioteca padrão e sem rede. Cada cliente guarda o seu estado em `instagram/` (`voice.md`, `swipe.md`, `log.md`). **Camada em português (`ig-pt-br`, nossa, em `skills/`):** as ferramentas originais são em inglês e erravam em português (testado em 2026-11-23: o `hookscore.py` dava 40 para "Ninguém te conta que…", a melhor fórmula, e não marcava "Para de rolar"; o `detect.py` achava 0 termos de clichê numa legenda cheia deles). A camada traz 27 fórmulas de gancho em PT, léxico de clichês em PT e versões em PT dos scripts (`hookscore_pt`, `beats_pt`, `swipe_pt`, `humanize_pt`, `detect_pt`, `caption_pt`), com 42 testes, **sem alterar nenhum arquivo do pacote original**. O próprio autor avisa que a nota de gancho só barra gancho ruim e não escolhe vencedor; em dados reais do nicho do Pedro (17 reels) a camada nomeou fórmula em 9 (o original, em 0) e a correlação com views ficou fraca (0,37, sem significância). Licença do pacote em `docs/licencas/instagram-agent-skill-MIT.txt`.
- **Como entra no time:** o `criador-conteudo` usa o pacote `ig-*` + `ig-pt-br` (Reel, carrossel, legenda, Stories, plano, respostas, DMs, reaproveitamento) e o `revisor-conteudo` confere o uso. `ig-viral` (pesquisa mensal), `ig-audit` e `ig-profile` dependem do navegador e dos insights do usuário e rodam na **conversa principal**, via diretor, nunca num agente isolado. Estado por cliente em `<pasta do cliente>/instagram/` (`voice.md`, `swipe.md`, `log.md`, `plan.md`).
- Plugins do Claude (não estão no repositório, vêm pela instalação do plugin): `marketing:content-creation`, `marketing:draft-content`, `marketing:email-sequence`, `marketing:campaign-plan`, `marketing:brand-review`.

---

## 2. Design (agente `designer`; o método dele é a skill `agente-design`)

Revisor: `revisor-design`. O `designer` roda isolado: devolve pendências de briefing e pedidos de autorização (geração de imagem custa na conta da OpenAI) ao diretor, que fala com o usuário. Skills que ele chama, por tipo de trabalho (ordem detalhada em `skills/agente-design/references/roteamento-skills.md`):

- **Web:** `design-taste-frontend` (sempre primeiro), `ui-ux-pro-max`, uma direção estética (`high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui` ou `stitch-design-taste`), `frontend-design`, `ui-styling`, `redesign-existing-projects`, `senior-frontend`, `full-output-enforcement` (evita código truncado em páginas longas), `gpt-taste`.
- **Referência visual antes de codar:** `imagegen-frontend-web`, `imagegen-frontend-mobile` (telas de app), `image-to-code`.
- **Revisão:** `impeccable` (+ `design:accessibility-review` do plugin Design).
- **Criativos, conteúdo, YouTube, Hotmart:** `banner-design`, `ads-creative` (revisão de criativo de anúncio), `ads-generate` e `ads-photoshoot` (imagens e fotos de produto para anúncio, só com imagem de origem autorizada), `ads-dna` (perfil de marca a partir de um site autorizado).
- **Marca e logo:** `brandkit`, `design`, `brand`, `design-system`.
- **Apresentações:** `slides`.
- **Movimento:** `skills-main` (pacote com `animate`, `animation-vocabulary`, `apple-design`, `emil-design-eng`, `review-animations`, `improve-animations` e outras; algumas também chegam pelo plugin `anthropic-skills`).
- Versão antiga guardada: `design-taste-frontend-v1` (só para projetos que dependam do comportamento exato dela).
- Agentes de apoio de terceiros: `visual-designer` (candidatos visuais), `format-adapter` (confere especificações de formato de cada plataforma), `creative-strategist` (conceitos), `copy-writer` (textos de anúncio com validação).

---

## 3. Gestor de tráfego (agente `gestor-trafego`)

Revisor: `revisor-trafego` (e `revisor-funil-vsl` quando houver VSL ou funil perpétuo). O gestor só tem as ferramentas Read, Glob, Grep e Write: não consegue alterar contas nem rodar scripts. Skills que ele chama, todas de terceiros (pacote "Claude Ads"), além das nossas:

- **Base e planejamento:** `ads` (skill principal, com referências e scripts), `ads-setup`, `ads-plan`, `ads-budget`, `ads-math`, `ads-research`.
- **Auditoria:** `ads-audit`, `ads-attribution`, `ads-server-side-tracking`, `ads-landing`, `ads-creative`, `ads-competitor`.
- **Plataformas:** `ads-meta`, `ads-google`, `ads-youtube`, `ads-tiktok`, `ads-linkedin`, `ads-microsoft`, `ads-apple`, `ads-amazon`, `ads-pinterest`, `ads-reddit`, `ads-snapchat`, `ads-x`.
- **Operação:** `ads-test` (experimentos), `ads-optimize`, `ads-monitor`, `ads-report`, `ads-launch`, `ads-validate`.
- **Gestão de Meta:** `ads-meta-gestao` (modelo de gestão mensal de Meta Ads, com regra "nenhum euro muda sem OK escrito" e caso anonimizado).
- **Concorrência:** `util-competitive-ads-extractor` (extrai anúncios de bibliotecas de anúncios).
- **Os nossos:** `estrategia-trafego-funil` (funil de VSL perpétuo e estrutura de tráfego) e `marketing-digital-growth` (lançamento pago, Black Friday, métricas).
- **Agentes de apoio de terceiros** (`agents-terceiros/`): `audit-meta`, `audit-google`, `audit-youtube`, `audit-tiktok`, `audit-linkedin`, `audit-microsoft`, `audit-apple`, `audit-amazon`, `audit-pinterest`, `audit-reddit`, `audit-snapchat`, `audit-x`, `audit-tracking`, `audit-budget`, `audit-creative`, `audit-policy-compliance`, `audit-regulatory-compliance`.

**Regra de segurança (vale desde já):** `ads-launch` e `ads-optimize` podem "aplicar" mudanças em contas. No nosso sistema o gestor de tráfego **só rascunha e propõe**. Qualquer mudança real em conta de anúncios (ativar, pausar, mudar orçamento, publicar) depende de aprovação escrita do usuário, para aquela ação naquele dia.

**Conectores (não são skills e não vão no repositório):** o Claude desta conta tem conectores de Meta Ads, de um painel de lançamentos e perpétuos e de uma plataforma de vídeo com player e testes A/B (pelo nome das ferramentas; confirme o que cada um faz antes de usar). O `gestor-trafego` não os acessa diretamente: quando for preciso ver números de contas, o **diretor** os busca em modo somente leitura e passa os dados no briefing. Credenciais e permissões ficam na sua conta, nunca no GitHub.

**Ambiente Python da skill `ads`:** os scripts de apoio (análise de landing page, screenshots, relatório em PDF) precisam de um ambiente Python que não cabe no repositório (cerca de 270 MB). O `instalar.ps1 -CriarAmbienteAds` recria esse ambiente a partir de `requirements.lock`, se houver Python 3.12+.

---

## 4. Editor de vídeo (agente `editor-video`, criado em 2026-11-24)

Revisor: `revisor-video` (não assiste ao vídeo: confere mapa, relatório e medições). Faz sempre o **Mapa de Edição** (bloco a bloco, com o trecho literal da copy e o tempo real da gravação) e só monta a primeira versão com ferramentas **confirmadas** no computador (`ffmpeg`, transcrição local em português, e `hyperframes` se estiver instalado), com uma aprovação por etapa. Não instala nada nem baixa arquivo. Dublagem, clone de voz e avatar por IA exigem autorização escrita da pessoa e aviso de custo. Não há skill de terceiros de vídeo neste repositório: se a pasta do cliente tiver o kit da Sirius Scale (licenciado só para a operação daquele cliente), o agente o lê como receita da casa e **nunca o copia** para outros lugares. O que já usamos como ferramenta: `ffmpeg`, `faster-whisper` e Python com Pillow. Pendente: instalar e testar o módulo de vídeo (HyperFrames) e fazer a primeira peça-mãe de ponta a ponta.

---

## 5. Manutenção do próprio sistema (diretor)

- `book-to-skill-master`: transforma livros e documentos (PDF, EPUB, DOCX etc.) em capítulos de skill. Serve de apoio para incorporar livros novos; o formato dos nossos capítulos continua o do sistema.
- `find-skills`: busca e instala skills novas quando precisarmos de uma capacidade que ainda não existe.
- Agentes de terceiros úteis para manter a qualidade: `skill-reviewer` (revisa roteamento e contratos de skills e agentes), `source-verifier` (verifica fatos e fontes), `research-worker` (pesquisa uma fatia específica), `release-verifier` (confere um pacote antes de publicar).

---

## 6. Próximos passos
1. **Editor de vídeo:** não iniciar por enquanto. Quando for a hora, avaliar a skill de vídeo programático e a de legendas e cortes da seção 4 (nada foi baixado; só entra com o OK do usuário).
2. **Instalação guiada pelo diretor** num computador novo, incluindo ligar a API da OpenAI para gerar imagens (e vídeo, se for preciso).
3. **Teste de ponta a ponta** dos agentes novos (`gestor-trafego`, `revisor-trafego`, `designer` e os demais), depois de reiniciar o Claude Code.
