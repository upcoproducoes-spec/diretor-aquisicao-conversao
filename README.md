# Diretor de Aquisição e Conversão — Sistema de Skills e Agentes

Sistema de agente de marketing/vendas para Claude Code: um orquestrador (`diretor-aquisicao-conversao`) que comanda 6 skills especializadas — estratégia de negócio, psicologia do consumidor, marketing digital/growth, persuasão e gatilhos mentais, copywriting, e vendas — através de um pipeline de 15 fases (diagnóstico → pesquisa → psicologia → posicionamento → oferta → funil → copy → vendas → métricas → otimização → escala).

Inclui também um **Modo Revisão de Projeto**: 7 agentes revisores (um por especialidade) que auditam um projeto em paralelo, cada um com a lente da sua skill, e devolvem correções sugeridas para aprovação antes de qualquer alteração.

## O que tem aqui

```
skills/
  diretor-aquisicao-conversao/   orquestrador mestre
  estrategia-negocios/           118 capítulos — Sun Tzu, Porter, Rumelt, Collins, Kim & Mauborgne, Lafley & Martin, Mintzberg, Ries & Trout (Positioning), Hormozi ($100M Offers + Lost Chapters)
  psicologia-consumidor/         52 capítulos — Freud (Interpretação dos Sonhos, O Eu e o Id, Cinco Lições) + Kahneman (Rápido e Devagar)
  marketing-digital-growth/      65 capítulos — Hacking Growth, Marketing na Era Digital, Unbound Marketing, Jeff Walker, Seth Godin, Hormozi ($100M Leads + Money Models)
  persuasao-gatilhos/            94 capítulos — Cialdini (As Armas da Persuasão + Pré-Suasão), Carnegie, Gustavo Ferreira
  copywriting-publicidade/       180 capítulos — Ferreira, Maccedo, Ogilvy, Bencivenga, Carlton, Halbert, Schwartz, Makepeace, Sugarman, Collier, Kennedy, Thiago Filemon (aulas de VSL)
  vendas-metodologia/            61 capítulos — Dixon & Adamson, Gitomer, Ross & Tyler, Rackham, Pink, Chris Voss
  funil-vsl-thiago-roas/         metodologia de funil de VSL perpétuo

  Total: 570 capítulos sintetizados de ~48 obras e aulas.

agents/
  revisor-estrategia.md
  revisor-psicologia.md
  revisor-growth.md
  revisor-persuasao.md
  revisor-copy.md
  revisor-vendas.md
  revisor-funil-vsl.md
```

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

## Como usar

Peça diretamente em português — não precisa citar o nome da skill:
- **Projeto novo do zero**: "preciso vender X", "crie uma campanha para X" → o diretor ativa o pipeline completo.
- **Pedido pontual**: "escreve uma headline", "como respondo essa objeção de preço" → vai direto na skill certa, sem passar pelo pipeline inteiro.
- **Revisão de projeto**: "revisa esse projeto", "audita isso antes de eu lançar" → ativa o Modo Revisão (os 7 agentes revisores rodam em paralelo, leem os materiais, e devolvem uma tabela de correções sugeridas — nada é alterado sem sua aprovação explícita).

## Ferramentas web (opcionais, fora deste repositório)

- **Chat rápido** (sem precisar do Claude Code instalado): responde com base nos frameworks centrais das 6 skills.
- **Painel de tarefas** (tipo Trello, por projeto, atualiza em tempo real para a equipe).

Peça os links atualizados na conversa com o Diretor caso precise reenviar para alguém.

## Aviso sobre direitos autorais

O conteúdo destas skills é **sintetizado** (frameworks, princípios e técnicas reescritos, nunca texto copiado literalmente) a partir de ~48 obras e aulas, a maioria ainda sob direitos autorais ativos (Ogilvy, Halbert, Schwartz, Kennedy, Cialdini, Porter, etc.). Isso torna este repositório adequado para **uso privado/interno** (você, sua equipe, colaboradores autorizados), mas não para distribuição pública livre. Mantenha este repositório **privado**.
