---
name: up-criativos-conjuntos-agendamento
description: "Como entregar carrossel e sequência de stories no Up (conjuntos em Criativos, fase do Drive), figurinha, legenda e agendamento pelo dono (novidades de 27 e 28/11/2026)"
metadata:
  node_type: memory
  type: reference
  originSessionId: c69244ff-d5ef-4c64-9bd6-21b0cd6309a4
  modified: 2026-11-28T12:37:32.343Z
---

No Up, desde 27-28/11/2026:
- Carrossel e sequência de stories vão para Criativos como **conjunto**: `POST v1/asset-sets {title, format: "carousel"|"story", asset_ids na ordem, campaign_id, phase, notes}`. **phase** = captacao, aquecimento, venda ou conteudo: decide a subpasta do Drive (CAPTAÇÃO, AQUECIMENTO, VENDA, CONTEÚDO ORGÂNICO); as telas vão com o nome do conjunto + "· 01, · 02…". Trocar ordem, imagem ou fase: `PUT v1/asset-sets/<id>`. Aprovar conjunto é [DONO].
- Na janela do conjunto, o dono marca as imagens que valem; as desmarcadas ficam guardadas, sem excluir. Agendar, "Baixar / enviar" (WhatsApp no celular) e "Copiar links do Drive" valem só para as marcadas, e as marcadas aprovadas podem ser agendadas mesmo com o conjunto em revisão.
- Ajuste pedido em uma imagem ("Imagem 3: ...") → refazer só ela e subir como versão nova (`POST v1/assets` com o `group_id` dela), depois apontar o conjunto para o id novo.
- Story com figurinha (enquete, contagem regressiva, link): escrever "Figurinha: ..." na observação (`notes`) do criativo; o Up manda lembrete para postar à mão. Observação só muda criando versão nova (volta para revisão).
- **Legenda no agendamento:** o Up puxa de uma tarefa ligada ao criativo (`links: [{kind:"asset", id}]`) com um texto de rótulo "Legenda". Uma tarefa = uma legenda; vários posts do feed = uma tarefa curta por post. (Observação com "Legenda...:" também serve, mas só pega até a primeira linha em branco.)
- O dono agenda direto em Criativos (feed, carrossel, stories). Tamanhos: feed 1080x1350, stories 1080x1920.
- Criar conjunto com a chave de dono (up.cjs da central) já nasce aprovado; com a chave de agente (up.cjs do projeto) nasce em revisão. Prefira a do projeto para não aprovar o próprio trabalho.
