---
name: up-criativos-conjuntos-agendamento
description: "Como entregar carrossel e sequência de stories no Up (conjuntos em Criativos), figurinha e agendamento pelo dono (novidade de 27/11/2026)"
metadata:
  node_type: memory
  type: reference
  originSessionId: c69244ff-d5ef-4c64-9bd6-21b0cd6309a4
  modified: 2026-11-28T11:24:18.568Z
---

Desde 27/11/2026, no Up:
- Carrossel e sequência de stories vão para Criativos como **conjunto**: `POST v1/asset-sets {title, format: "carousel"|"story", asset_ids na ordem, campaign_id, notes}`; trocar a ordem ou uma imagem: `PUT v1/asset-sets/<id> {asset_ids}`. Aprovar conjunto é [DONO].
- Ajuste pedido em uma imagem ("Imagem 3: ...") → refazer só ela e subir como versão nova (`POST v1/assets` com o `group_id` dela), depois apontar o conjunto para o id novo.
- Story com figurinha (enquete, contagem regressiva, link): escrever "Figurinha: ..." na observação (`notes`) do criativo; o Up manda lembrete para postar à mão. Observação só muda criando versão nova (volta para revisão).
- O dono agenda direto em Criativos (feed, carrossel, stories), com a legenda da tarefa ligada. Tamanhos: feed 1080x1350, stories 1080x1920.
- Criar conjunto com a chave de dono (up.cjs da central) já nasce aprovado; com a chave de agente (up.cjs do projeto) nasce em revisão. Prefira a do projeto para não aprovar o próprio trabalho.
