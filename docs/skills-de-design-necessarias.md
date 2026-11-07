# Skills de design de terceiros que o agente de design usa

O `agente-design` (neste repositório) **orquestra** outras skills de design. Elas são de terceiros, por isso **não foram copiadas para cá**: o que está listado abaixo precisa ser reinstalado em `C:\Users\<usuário>\.claude\skills\` num computador novo.

Se alguma estiver faltando, o agente de design ainda abre, mas pula essa etapa. A ordem de uso de cada uma está em `skills/agente-design/references/roteamento-skills.md`.

## Web (site, landing page, página)
- `design-taste-frontend` (sempre primeiro), `ui-ux-pro-max`
- Direção estética (uma delas): `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `stitch-design-taste`
- Construção: `frontend-design`, `ui-styling`
- Referência visual: `imagegen-frontend-web`, `image-to-code`
- Melhorar o que existe: `redesign-existing-projects`
- Revisão: `impeccable` e `design:accessibility-review` (plugin Design)

## Criativos, conteúdo, YouTube, Hotmart
- `banner-design`
- Revisão de criativo de anúncio: `ads-creative`

## Marca e logo
- `brandkit`, `design`, `brand`, `design-system`

## Apresentação e movimento
- `slides`
- `anthropic-skills:emil-design-eng`, `anthropic-skills:animate`

## De onde vieram (segundo `skills/agente-design/references/atualizacao.md`)
- `anthropics/skills`
- `Leonxlnx/taste-skill`
- `nextlevelbuilder/ui-ux-pro-max-skill`
- `pbakaus/impeccable`
- Coleções "awesome-claude-skills" (para as demais)

Antes de instalar qualquer coisa baixada, leia o conteúdo. Nunca rode um script de terceiros sem conferir.

## O que também fica de fora do GitHub (de propósito)
- **Chave da OpenAI** do gerador de imagens: arquivo `C:\Users\<usuário>\.claude\openai.env` com a linha `OPENAI_API_KEY=...`. Crie você mesmo no computador novo; **nunca** cole a chave no chat nem no repositório.
- **Caminhos fixos:** o agente de design e o gerador de imagens citam `C:\Users\User\...`. Se o usuário do Windows no computador novo tiver outro nome, ajuste esses caminhos (peça ao Claude: "ajusta os caminhos do agente de design para este computador").
- **O Up** (a ferramenta onde as peças e páginas são enviadas) é um projeto à parte, com seu próprio repositório.
