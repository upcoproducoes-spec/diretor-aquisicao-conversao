# Radar das plataformas — o que mudou na Meta e no Google

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma, com data. **Alcance:** UNIVERSAL quando a fonte é oficial (é
> comportamento da plataforma, não de cliente); o que vier de blog ou agência fica marcado como
> opinião de terceiro e não decide nada sozinho.
> **Por que existe:** decisão do Rodrigo, "vale a pena, de vez em quando, também analisar a central de
> ajuda e pesquisar na internet o que vem funcionando no momento, uma nova configuração, porque o Meta
> vive mudando" (`sirius-scale/frameworks/trafego/otimizacao-em-tres-niveis.md` §6).
> **Como se usa:** uma entrada por novidade, a mais nova no topo, com link e a data da fonte (ou a data
> em que foi lida, quando a página não tem data). Antes de afirmar como uma plataforma se comporta,
> o agente de tráfego confere aqui; se a última leitura tiver mais de uma semana, relê a fonte. Página
> mudou e contradiz uma entrada: a entrada ganha a correção com a data, nunca é apagada.
> **Do lado de vocês:** a leitura é feita na casa e chega por este arquivo, junto com a atualização do
> kit. O que vocês acharem por conta própria vai em `frameworks-da-casa/`. Aqui as datas ficam: são
> da plataforma, e sem elas a entrada não serve.

## Leitura de 09/11/2026 — UNIVERSAL nos itens com fonte oficial; o resto marcado

Só leitura: páginas de versão e registro de alterações das duas plataformas, mais buscas de notícia. Nenhuma novidade
oficial de produto que mexa em captação ou remarketing.

- **Meta: a v27.0 da Marketing API saiu em 04/11/2026**, validade a definir. O registro de alterações da Marketing API
  lista v27.0 (04/11/2026), v26.0 (29/07/2026, a definir), v25.0 (até 23/02/2027) e v24.0 (até 10/11/2026). A lista do
  que muda na v27.0 deu página inexistente: não migre pra ela até a lista oficial sair.
  [Registro de alterações da Marketing API](https://developers.facebook.com/docs/marketing-api/marketing-api-changelog)
- **As duas páginas oficiais de versão da Meta não batem.** A página de versões da Graph API traz uma tabela da Marketing
  API sem a v26.0 e a v27.0 e com a v24.0 já vencida. O registro de alterações (acima) é o mais completo. Na dúvida,
  trate a v24.0 como vencida e use a v26.0. [Versões](https://developers.facebook.com/docs/graph-api/changelog/versions)
- **Graph API:** v20.0 venceu em 24/09/2026; v21.0 vale até 21/01/2027; v22.0 até 20/05/2027. Script que fixa versão na
  URL depende da promoção automática quando ela vence.
- **Meta, produto (PADRÃO INCONCLUSIVO):** nada oficial novo sobre teste de criativo, fadiga ou Advantage+ de leads. Um
  blog de terceiros cita um ajuste de medição de conversão nos dispositivos, ligado por padrão a partir de 12/11/2026, sem
  fonte oficial: verificar antes de qualquer decisão de rastreio.
- **Google Ads:** a última versão continua a v26.1 (28/10/2026); nada novo de Demand Gen.
  [Notas de versão](https://developers.google.com/google-ads/api/docs/release-notes)
## Leitura de 02/11/2026 — UNIVERSAL nos itens com fonte oficial; o resto marcado

Só leitura, nas páginas de versão e de descontinuação das duas plataformas e nas buscas de notícia. As
tabelas de versão não mostram data de atualização: a data aqui é a da leitura. Sem novidade oficial de
produto que mexa em captação ou remarketing desde 29/10 (abaixo, o que foi conferido); a novidade desta
semana é de versão de API, e uma entrada anterior estava errada.

### Correção da leitura de 29/10/2026 — UNIVERSAL (fonte oficial)

- A entrada de 29/10 dizia que a v24.0 sai do ar em 10/11/2026. **Errado.** A tabela oficial tem duas
  colunas de validade, uma pra Graph API e outra pra Marketing API, e elas não batem. Na Marketing API
  (anúncio, conjunto, campanha, insights) a v24.0 expirou em 06/10/2026, a v23.0 em 09/06/2026, a v22.0 em
  19/02/2026 e a v21.0 em 09/09/2025. A v25.0 está sem data. Na Graph API (página, post, Instagram) a
  v21.0 vale até 21/01/2027 e a v22.0 até 20/05/2027.
  [Versões da Graph e da Marketing API](https://developers.facebook.com/docs/graph-api/changelog/versions), lida em 02/11/2026
- A tabela da Marketing API não lista a v26.0, só a da Graph API (lançada em 29/07/2026, validade a
  definir). Não existe v27.0 em nenhuma das duas. Não há explicação oficial achada pra ausência da v26.0
  na tabela da Marketing API.

### Meta: versão de API — UNIVERSAL (fonte oficial) + o que se mediu na casa

- **Chamada em versão expirada da Marketing API não quebra sempre.** A Meta sobe a chamada sozinha pra
  próxima versão disponível, menos nos endpoints que mudaram nessa próxima versão, que falham. O exemplo
  oficial: leitura de insights numa versão velha é promovida; edição de conjunto falha. Dá pra conferir
  pelo cabeçalho de resposta `X-Ad-Api-Version-Warning`, e o recurso se desliga nas configurações do app.
  A atualização automática da Marketing API ganhou lançamento próprio em 29/07/2026, junto da v26.0.
  [Versionamento da Marketing API](https://developers.facebook.com/docs/marketing-api/overview/versioning) ·
  [anúncio de 2024](https://developers.facebook.com/blog/post/2024/04/16/upcoming-change-in-marketing-api-version-deprecation) ·
  [v26.0](https://developers.facebook.com/blog/post/2026/07/29/introducing-graph-api-v26-and-marketing-api-v26/)
- **O que se mediu na casa:** a SDK `facebook_business` estava na 26.0.0, mas parte do código chamava a
  API direto por URL, com v21.0 ou v22.0 fixa no endereço. Leitura de anúncio nessas URLs depende da
  promoção automática. Escrita em anúncio por URL velha pode falhar no endpoint que mudou. Não foi
  testado chamada por chamada. Post orgânico é Graph API, que ainda vale (acima).
- **Instagram Explore saiu como posicionamento na v26.0** (29/07/2026) e o Messenger Stories foi
  descontinuado em todas as versões em 27/10/2026. Conjunto que lista posicionamento na mão não pode
  levar os dois. [changelog v26.0](https://developers.facebook.com/docs/graph-api/changelog/version26.0)

### Meta: produto (criativo, Advantage+, públicos) — PADRÃO INCONCLUSIVO (sem fonte oficial nova)

- A Meta anunciou ferramentas de IA pra anúncio no Advertising Week de 06/10/2026 (notícia de terceiro,
  techjuice.pk). A página oficial não foi achada em facebook.com/business/news, nem o detalhe pra leads
  ou teste de criativo. Fica como opinião de terceiro até achar a fonte.
- Teste de criativo, fadiga, edição significativa, públicos personalizados: nada novo nas fontes
  conferidas. Vale a leitura de 29/10.

### Google Ads: versão de API — UNIVERSAL (fonte oficial) + o que se mediu na casa

- **Versões no ar:** v23 (sai em fev/2027), v24 (mai/2027), v25 (ago/2027) e v26, lançada em 14/10/2026
  (nov/2027); v26.1 saiu em 28/10/2026. A v21 e a v22 já não estão na tabela. A meta do Google é tirar
  cada versão um ano depois do lançamento, e a v27 está prevista pra janeiro de 2027.
  [Datas de descontinuação](https://developers.google.com/google-ads/api/docs/sunset-dates), lida em 02/11/2026
- **A biblioteca:** `google-ads==31.4.0` traz v21 a v25, sem v26. Sem versão explícita a biblioteca usa a
  v25: fica até ago/2027. Script que fixa versão por fora da biblioteca envelhece sozinho: na casa, um
  `FieldMask` com `version="v19"`, que não existe mais na biblioteca, deve quebrar na hora de pausar (não
  rodado pra confirmar, porque é escrita).
- **v26 (14/10/2026), mudança que quebra:** `ConversionTrackingSetting.enhanced_conversions_for_leads_enabled`
  saiu (o lugar novo é `enablement_setting`). A casa não usa o campo.
- **v26.1 (28/10/2026):**
  - campanha migrada pra Demand Gen não ativa enquanto a original existir ou outra migrada estiver
    ativa (`DemandGenCampaignError.CANNOT_ACTIVATE_MIGRATED_CAMPAIGN`). Mexe na migração das campanhas
    de Display pra Demand Gen;
  - orçamento por canal (`CampaignBudget.budget_network_settings`): divide a verba entre inventário do
    Google, parceiros de pesquisa e Display, com teto por canal.
  [Notas de versão](https://developers.google.com/google-ads/api/docs/release-notes), lida em 02/11/2026
  (a página é longa; a leitura inteira foi só da parte da v26 e da v26.1)

### Google Ads: Demand Gen, públicos e Customer Match — UNIVERSAL (fonte oficial, sem novidade)

- A página de descontinuações não tem entrada depois de 30/09/2026 (essa é de segmentação por idioma
  em Pesquisa). Orçamento mínimo de US$ 5/dia no Demand Gen e Customer Match pela Data Manager API
  seguem como na leitura de 29/10.
  [descontinuações](https://developers.google.com/google-ads/api/docs/deprecations), lida em 02/11/2026
- Última novidade de produto do Demand Gen achada no blog do Google: conversa por app de mensagem a
  partir do anúncio no YouTube, em teste (27/08/2026). Não mexe na captação por formulário.
  [blog.google](https://blog.google/products/ads-commerce/demand-gen-drop-august-2026/)

### Opinião de terceiro (não decide nada sozinha) — PADRÃO INCONCLUSIVO

- Blogs dizem que a atualização automática da Meta manda chamada sem versão pra versão mais antiga;
  a documentação oficial diz que chamada sem versão falha. Vale a oficial.

### O que isso muda pra quem tem código próprio (02/11/2026) — VARIAÇÃO ISOLADA

1. **Código com versão velha da Meta na URL lê anúncio por causa da promoção automática.** Proposta da
   casa: trocar a URL pra mesma versão da SDK, um script por vez, conferindo a leitura de volta.
2. **Regra pra script novo:** versão da Meta sai de uma constante só, igual à da SDK, nunca escrita na
   URL; e o radar lê as duas colunas da tabela (Graph e Marketing), porque a data que vale pra anúncio
   é a da Marketing.
3. Atualizar a biblioteca do Google pra trazer a v26 não tem pressa: a v25 vale até ago/2027.

## Leitura de 29/10/2026 — UNIVERSAL nos itens com fonte oficial; o resto marcado

Pesquisa feita só com leitura (central de ajuda, documentação de desenvolvedor e notícias). As
páginas da central de ajuda da Meta não mostram data: a data aqui é a da leitura.

### Meta: teste de criativo e anúncios por conjunto — UNIVERSAL (fonte oficial)

- **Existe teste de criativo nativo dentro de uma campanha existente.** No anúncio, `Configurar teste`, com 2 a 7
  cópias; uma parte do orçamento do dia fica separada pros anúncios de teste (a
  Meta sugere no máximo 20%); só aceita a estratégia de lance `volume mais alto`; no fim chega um
  e-mail com os anúncios de alto desempenho, sem nível de confiança; depois do teste nada muda
  sozinho. [Como configurar um teste de criativo](https://www.facebook.com/business/help/1423851372208214)
- **Pela API:** `POST /{business_id}/ad_studies` com `type=SPLIT_TEST_V2`, `creative_test_config`
  (`daily_budget` ou `lifetime_budget_percentage`) e `cells` com um anúncio cada; o resultado sai em
  `objectives` → `results` (`high_performer_ids`; `winner_ad_object_id` vem nulo). O guia diz 2 a 7
  células e a referência diz 2 a 5: as duas páginas oficiais divergem.
  [guia](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/split-testing) ·
  [referência](https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/business/ad_studies)
- **Ligar anúncio novo num conjunto reinicia o aprendizado:** adicionar anúncio novo ao conjunto está
  na lista de edições significativas.
  [Edições significativas](https://www.facebook.com/business/help/316478108955072)
- **Quantos anúncios por conjunto:** a Meta não dá número. Diz que muitos anúncios ao mesmo tempo fazem
  cada um veicular menos e menos sair do aprendizado, e orienta a ter menos anúncios por
  conjunto, com criativos diversos entre eles.
  [Volume de anúncios](https://www.facebook.com/business/help/2720085414702598)
- **Fadiga:** a coluna Veiculação mostra `Criativo limitado` (custo por resultado acima do dos seus
  anúncios anteriores, abaixo do dobro) e `Fadiga do criativo` (o dobro ou mais). As recomendações de
  fadiga só existem pra conjunto com um criativo. Não há campo de fadiga na API: a leitura calcula pela
  frequência e pelo custo por resultado. [Fadiga do criativo](https://www.facebook.com/business/help/1346816142327858)
- **Criativo Advantage+:** alguns aprimoramentos vêm ligados por padrão, inclusive texto gerado por IA;
  desliga recurso por recurso (`degrees_of_freedom_spec.creative_features_spec.<recurso>.enroll_status=OPT_OUT`).
  [Criativo Advantage+](https://www.facebook.com/business/help/297506218282224)
- **Frequência:** a frequência-alvo só vale pras metas Alcance e ThruPlay. Não há recomendação
  oficial de frequência pra remarketing. [Frequência no leilão](https://www.facebook.com/business/help/422853447344162)

### Meta: novidades de 2025–2026 que mexem em captação — UNIVERSAL (fonte oficial)

- **Exclusão por direcionamento detalhado saiu** (31/03/2025) e os interesses foram consolidados
  (23/06/2025); exclusão por público personalizado continua valendo.
  [Direcionamento detalhado](https://www.facebook.com/business/help/458835214668072)
- **Campanha Advantage+ de leads** disponível no mundo todo (anúncio de 30/10/2025), com site e
  formulário instantâneo na mesma campanha e verificação de lead. A Meta diz −14% no custo por lead:
  número da própria Meta, não medido por nós.
  [anúncio](https://www.facebook.com/business/news/more-quality-leads-this-q5-with-metas-latest-ai-enabled-updates)
- **API:** versão atual v26.0 (29/07/2026); a v24.0 sai do ar em 10/11/2026. *(Corrigido em 02/11/2026: na Marketing API a v24.0 expirou em 06/10/2026; ver a leitura de 02/11.)* Quem tem
  código com v21.0 ou v22.0 fixa na URL confere antes da data.
  [changelog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog)

### Google Ads: Demand Gen — UNIVERSAL (fonte oficial)

- **Experimento A/B de criativo:** `A/B test assets` testa criativo com o controle no ar (o Google
  duplica com o mesmo orçamento); de 2 a 10 braços; com lance por conversão pede 50 conversões por
  braço; confiança de 70%, 80% ou 95%. Pela API: `ExperimentType.YOUTUBE_CUSTOM`, subtipo
  `DEMAND_GEN_ASSET`. [Experimentos de Demand Gen](https://support.google.com/google-ads/answer/13719071) ·
  [API](https://developers.google.com/google-ads/api/docs/experiments/overview)
- **Anúncio limitado:** `ad_group_ad.primary_status=LIMITED` com motivo (`AD_GROUP_AD_POOR_QUALITY` e
  outros). Não há sinal oficial de fadiga.
- **Campanha criada por script sai diferente da criada na tela:** a otimização por view-through vem
  ligada na tela e `Campaign.view_through_conversion_optimization_enabled` nasce `false` na API.
  [Otimização por view-through](https://support.google.com/google-ads/answer/16399666)
- **Orçamento mínimo do Demand Gen:** US$ 5/dia desde 01/04/2026 (erro `BUDGET_BELOW_PER_DAY_MINIMUM`;
  o piso em reais de `sirius-scale/frameworks/trafego/google-criacao-tecnica.md` §1 é esse).
  [deprecações](https://developers.google.com/google-ads/api/docs/deprecations)
- **Customer Match:** desde 01/04/2026, token sem envio recente usa a Data Manager API.

### Opinião de terceiro (não decide nada sozinha) — PADRÃO INCONCLUSIVO

- Blogs de 2026 falam em `similarity score` e em anúncios parecidos agrupados pelo sistema de entrega
  da Meta. Sem fonte oficial.
- Limite de frequência "acima de 3" em remarketing é regra de agência, não da Meta.

### O que isso muda no método (29/10/2026) — VARIAÇÃO ISOLADA

1. **O teste de criativo com verba própria tem caminho oficial na Meta** (o teste nativo), além de um
   conjunto por criativo (`sirius-scale/frameworks/trafego/otimizacao-em-tres-niveis.md` §3). Em público
   pequeno e fechado (aluno) o teste quase nunca fecha com confiança: serve pra dar
   verba igual, não pra provar vencedor.
2. **Ligar o que nunca rodou tem custo na Meta:** o conjunto volta pro aprendizado. A proposta diz isso
   no texto, e a leitura não propõe ligar mais de um por unidade por dia.
   - **Medido depois — conta contra a frase acima:** nos três conjuntos de vídeo de uma Black do
     caso-base, uma rotação e uma arte nova não tiraram o conjunto do aprendizado concluído (`SUCCESS`,
     última edição significativa na ativação). Detalhe em
     `sirius-scale/frameworks/trafego/meta-criacao-tecnica.md`, "Última edição do conjunto". A regra de
     um por unidade por dia fica: ela também protege a leitura da troca. VARIAÇÃO ISOLADA.

## Excluído de propósito

- Tutorial de tela (onde clicar no Gerenciador): muda toda semana e não serve pra rotina. Fica o
  nome do recurso e o campo da API.
- Novidade que não mexe em captação de lead nem em remarketing (catálogo, loja, app).

## Pontos em aberto

1. O teste de criativo nativo da Meta nunca rodou na casa: falta o primeiro, com o `business_id` e a
   permissão do token conferidos antes.
2. As duas páginas oficiais divergem no número de células do `ad_studies` (2 a 7 contra 2 a 5).
3. Por que a tabela da Marketing API não lista a v26.0: sem fonte oficial.
