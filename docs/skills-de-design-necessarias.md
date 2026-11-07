# Skills de design de terceiros (já incluídas neste repositório)

O `agente-design` orquestra outras skills de design. Elas são de terceiros, mas fazem parte do processo, por isso **estão na pasta `skills-terceiros/`** e o `instalar.ps1` as instala junto com o resto. Não é preciso baixar nada separado.

A ordem de uso de cada uma está em `skills/agente-design/references/roteamento-skills.md`.

## O que está em `skills-terceiros/` (19 skills)

**Web (site, landing page, página)**
- `design-taste-frontend` (sempre primeiro), `ui-ux-pro-max`
- Direção estética (uma delas): `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `stitch-design-taste`
- Construção: `frontend-design`, `ui-styling`
- Referência visual: `imagegen-frontend-web`, `image-to-code`
- Melhorar o que existe: `redesign-existing-projects`
- Revisão: `impeccable`

**Criativos, conteúdo, YouTube, Hotmart**
- `banner-design`
- Revisão de criativo de anúncio: `ads-creative`

**Marca e logo**
- `brandkit`, `design`, `brand`, `design-system`

**Apresentação**
- `slides`

## O que NÃO está no repositório
- **Skills que vêm de plugins** (`anthropic-skills:*`, `design:*`, como `design:accessibility-review`, `emil-design-eng` e `animate`): chegam pela instalação dos plugins no Claude, não por cópia de arquivos. Se faltarem num computador novo, o agente de design segue sem elas nessas etapas pontuais.
- **Chave da OpenAI** do gerador de imagens: arquivo `C:\Users\<usuário>\.claude\openai.env` com a linha `OPENAI_API_KEY=...`. Crie você mesmo no computador novo; **nunca** cole a chave no chat nem no repositório.
- **Caminhos fixos:** o agente de design e o gerador de imagens citam `C:\Users\User\...`. Se o usuário do Windows no computador novo tiver outro nome, peça ao Claude: "ajusta os caminhos do agente de design para este computador".
- **O Up** (onde as peças e páginas são enviadas) é um projeto à parte, com seu próprio repositório.

## Origem e atualização
Segundo `skills/agente-design/references/atualizacao.md`, as originais vêm de repositórios públicos como `anthropics/skills`, `Leonxlnx/taste-skill`, `nextlevelbuilder/ui-ux-pro-max-skill` e `pbakaus/impeccable`. As cópias deste repositório são as versões instaladas no computador do usuário na data do commit. Para buscar versões novas, peça "atualizar o agente de design" (o processo está em `atualizacao.md`) e depois sincronize o repositório.

Uso interno e privado: parte dessas skills tem licença própria (por exemplo, `frontend-design` e `ui-styling` trazem `LICENSE.txt`). Não distribua o repositório fora da equipe.
