# Sirius Scale na central

A inteligência da Sirius é construída em conjunto pelo Anderson e pelo Rodrigo e vale para **todos os projetos** da UP e para todos os agentes, subagentes e revisores (decisão do Anderson, 27/11/2026). APIs e chaves são sempre as nossas.

## Onde está
Desde 27/11/2026 o kit fica **aqui na central** (versão v0.6, de 23/11/2026):
- `sirius-scale/`: REGRAS.md, COMECE-AQUI.md, O-QUE-MUDOU.md, LICENCA.md, modelos/, rotinas/trafego-diario.md, instalacao/, ferramentas/google/ e **frameworks/** (66 arquivos).
- `sirius-scale-agentes/`: manuais dos 5 agentes da Sirius (copy, designer, webdesigner, gestor-trafego, video).
- `checagens/`: /preflight, /revisar, /debriefing, /mapa-edicao, /pente-fino, /sirius-humanizer.
- `ADAPTADOR-SIRIUS-SCALE.md`: como atualizar sem estragar nada (nunca rodar o atualizar.sh).

Cada projeto (Pedro, Bia e a central) tem **atalhos** com os mesmos nomes: `sirius-scale/`, `sirius-scale-agentes/` e `.claude/skills/<checagem>`, além do próprio `sirius-scale-mapa.md` (onde moram expert, produtos, lançamentos, funis e entregas naquele projeto). Projeto novo: criar os atalhos e o mapa.

Material novo do Rodrigo: trazer para a central, atualizar seguindo o ADAPTADOR e registrar aqui o que mudou (versão, data, arquivos). A `LICENCA.md` do kit ainda traz o texto restritivo antigo; vale a decisão do Anderson de 27/11/2026 (Sirius liberada para todos os projetos, agentes e GitHub).

## Equivalência de agentes
copy → `copywriter` · designer e webdesigner → `designer` · gestor-trafego → `gestor-trafego` · video → `editor-video`. Ordem de prioridade: regra do projeto > playbook da central > Sirius > skills gerais.

## Que parte alimenta cada agente
| Agente nosso | Ler da Sirius (em `sirius-scale\frameworks\`) |
|---|---|
| diretor | `REGRAS.md`; lancamentos/ (lancamento-classico, black-da-casa, perpetuo, low-ticket, briefing, diagnostico-de-operacao) |
| estrategista-negocios | lancamentos/roma-e-promessa, oferta-14-secoes, lancamentos/produto-de-entrada, low-ticket, metas-e-base-de-faturamento, diagnostico-de-operacao |
| analista-psicologia | pesquisa/pesquisa-e-avatar, copy/great-leads |
| especialista-growth-funil | lancamentos/ (todos), rotinas-de-lancamento, pos-compra-e-suporte, upsell-e-downsell, conteudo/, trafego/lancamento-gratuito |
| copywriter / especialista-persuasao | `sirius-scale-agentes\copy.md`, copy/ (sem vídeo), lhto, oferta-14-secoes, padrao-de-copy, email, disparo-whatsapp, producao-de-vsl |
| especialista-vendas | pos-compra-e-suporte, copy/disparo-whatsapp, lancamentos/live-de-downsell |
| criador-conteudo | conteudo/, copy/criativos, design/estilos-sticker-instagram, design/margens-seguranca-vertical |
| designer | `sirius-scale-agentes\designer.md` e `webdesigner.md`, design/, paginas/ |
| editor-video | `sirius-scale-agentes\video.md`, copy/mapa-de-edicao-vsl e edicao-video-*, /mapa-edicao |
| gestor-trafego / up-trafego | `sirius-scale-agentes\gestor-trafego.md`, trafego/ (todos), rotinas\trafego-diario.md, /preflight |
| revisores | checklists de /revisar (copy, criativo, página, tráfego) |

## O que a Sirius tem e o time ainda não tinha
Debriefing ranqueado em reais; preflight de 12 itens; regra da casa com força e alcance (/pente-fino); pesquisa e avatar obrigatórios antes da copy; webdesigner com técnica própria; montagem de campanha no Google por script (só validada a seco); modelos detalhados de lançamento (LPSG, live de domingo, live de downsell, vídeo de upsell); rotina por função com rotinas.json; técnica de Hotmart, Cloudflare, WordPress.

## Depende de ferramenta (aqui, com as nossas contas)
Dash Fácil, Meta Ads, Hotmart (conectores já ligados); Google Ads (credenciais próprias no .env, ainda não configuradas); HyperFrames (nunca rodou no Windows); Clarity (um id por cliente). FullFunnel e Baileys ficam só como referência (FullFunnel encerrado em 12/11).

## Diferença de regra
O kit da Sirius só monta campanha pausada e deixa ligar/verba com o dono. Aqui vale a regra do Anderson de 24/11: executar quando ele pedir ou aprovar (ver `playbook/04-trafego.md`).
