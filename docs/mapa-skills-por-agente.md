# Mapa: qual skill cada agente chama

Regra do sistema: o **diretor** coordena; cada **agente** de especialidade carrega só as skills da sua área quando precisa; cada agente tem o seu **revisor**. Este mapa diz o que já existe, o que está instalado para cada agente que ainda vamos criar e o que está sugerido.

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
| `criador-conteudo` | `revisor-conteudo` | `criacao-conteudo-social-media` (roteia para as demais) |

### Ferramentas de terceiros que ajudam o copy e o conteúdo (já instaladas)
- `humanizer`: tira as marcas de "texto escrito por IA" de um texto pronto. Foi feita com base em padrões do inglês; em português, use como revisão final e confira o resultado, não aplique às cegas.
- `mkt-ad-creative`: gera e itera criativos e textos de anúncio em escala (em inglês).
- `ads-create`: conceitos de campanha, mensagens e briefings de criativo a partir de perfil de marca e objetivo.
- Plugins do Claude (não estão no repositório, vêm pela instalação do plugin): `marketing:content-creation`, `marketing:draft-content`, `marketing:email-sequence`, `marketing:campaign-plan`, `marketing:brand-review`.

---

## 2. Design (hoje é a skill `agente-design`; falta virar agente da equipe)

Revisor: `revisor-design`. Skills que ele chama, por tipo de trabalho (ordem detalhada em `skills/agente-design/references/roteamento-skills.md`):

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

## 3. Gestor de tráfego (futuro agente; hoje o sistema só planeja)

Revisores que já existem: `revisor-growth` e `revisor-funil-vsl`. Skills já instaladas, todas de terceiros (pacote "Claude Ads"):

- **Base e planejamento:** `ads` (skill principal, com referências e scripts), `ads-setup`, `ads-plan`, `ads-budget`, `ads-math`, `ads-research`.
- **Auditoria:** `ads-audit`, `ads-attribution`, `ads-server-side-tracking`, `ads-landing`, `ads-creative`, `ads-competitor`.
- **Plataformas:** `ads-meta`, `ads-google`, `ads-youtube`, `ads-tiktok`, `ads-linkedin`, `ads-microsoft`, `ads-apple`, `ads-amazon`, `ads-pinterest`, `ads-reddit`, `ads-snapchat`, `ads-x`.
- **Operação:** `ads-test` (experimentos), `ads-optimize`, `ads-monitor`, `ads-report`, `ads-launch`, `ads-validate`.
- **Gestão de Meta:** `ads-meta-gestao` (modelo de gestão mensal de Meta Ads, com regra "nenhum euro muda sem OK escrito" e caso anonimizado).
- **Concorrência:** `util-competitive-ads-extractor` (extrai anúncios de bibliotecas de anúncios).
- **Os nossos:** `estrategia-trafego-funil` (funil de VSL perpétuo e estrutura de tráfego) e `marketing-digital-growth` (lançamento pago, Black Friday, métricas).
- **Agentes de apoio de terceiros** (`agents-terceiros/`): `audit-meta`, `audit-google`, `audit-youtube`, `audit-tiktok`, `audit-linkedin`, `audit-microsoft`, `audit-apple`, `audit-amazon`, `audit-pinterest`, `audit-reddit`, `audit-snapchat`, `audit-x`, `audit-tracking`, `audit-budget`, `audit-creative`, `audit-policy-compliance`, `audit-regulatory-compliance`.

**Regra de segurança para esse agente (vale desde já):** `ads-launch` e `ads-optimize` podem "aplicar" mudanças em contas. No nosso sistema o gestor de tráfego **só rascunha e propõe**. Qualquer mudança real em conta de anúncios (ativar, pausar, mudar orçamento, publicar) depende de aprovação escrita do usuário, para aquela ação naquele dia.

**Conectores (não são skills e não vão no repositório):** o Claude desta conta tem conectores de Meta Ads, de um painel de lançamentos e perpétuos e de uma plataforma de vídeo com player e testes A/B (pelo nome das ferramentas; confirme o que cada um faz antes de ligar a um agente). Quando o agente de tráfego for criado, ele deve usá-los em modo leitura por padrão. Credenciais e permissões ficam na sua conta, nunca no GitHub.

**Ambiente Python da skill `ads`:** os scripts de apoio (análise de landing page, screenshots, relatório em PDF) precisam de um ambiente Python que não cabe no repositório (cerca de 270 MB). O `instalar.ps1 -CriarAmbienteAds` recria esse ambiente a partir de `requirements.lock`, se houver Python 3.12+.

---

## 4. Editor de vídeo (futuro agente; ainda não há skill instalada)

Nada de terceiros instalado para isso. O que já usamos no sistema (como ferramenta, não como skill): `ffmpeg` (cortes e quadros), `faster-whisper` (transcrição local) e Python com Pillow. Sugestões a avaliar **antes de baixar** (preciso da sua autorização para baixar e vou ler o conteúdo antes de instalar):
- Uma skill de vídeo programático (por exemplo, a do projeto Remotion, que gera vídeo a partir de código).
- Uma skill ou script de legendas automáticas e cortes por transcrição.
- Roteiro de edição para Reels e anúncios em vídeo, apoiado em `criacao-conteudo-social-media` e nos capítulos de criativos de vídeo (`copywriting-publicidade` ch231).

---

## 5. Manutenção do próprio sistema (diretor)

- `book-to-skill-master`: transforma livros e documentos (PDF, EPUB, DOCX etc.) em capítulos de skill. Serve de apoio para incorporar livros novos; o formato dos nossos capítulos continua o do sistema.
- `find-skills`: busca e instala skills novas quando precisarmos de uma capacidade que ainda não existe.
- Agentes de terceiros úteis para manter a qualidade: `skill-reviewer` (revisa roteamento e contratos de skills e agentes), `source-verifier` (verifica fatos e fontes), `research-worker` (pesquisa uma fatia específica), `release-verifier` (confere um pacote antes de publicar).

---

## 6. Sugestões novas (nada foi baixado; só entra com o seu OK)
1. **Skill de vídeo programático** e **legendas/cortes** para o agente editor de vídeo (seção 4).
2. **Agente `gestor-trafego`**, no mesmo padrão dos outros (produz plano, rascunho de campanha, diagnóstico e relatório; revisor = `revisor-growth` + `revisor-funil-vsl`), amarrando as skills `ads-*` da seção 3 e a regra de aprovação.
3. **Transformar `agente-design` em agente da equipe** (`designer` + `revisor-design`), com a lista de skills da seção 2 no cabeçalho.
4. **`CLAUDE.md` global** com as suas regras de trabalho, para valerem em qualquer pasta e não só na pasta atual.
