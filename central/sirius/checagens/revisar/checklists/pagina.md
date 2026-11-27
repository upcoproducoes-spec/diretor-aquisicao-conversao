# Checklist — Página de lançamento (HTML standalone)

## Leia antes de abrir o entregável

1. `sirius-scale/REGRAS.md` §1 (tom) e §2 (nada inventado), e o padrão de entrega de
   página do agente `webdesigner` (`.claude/agents/webdesigner.md`)
2. `frameworks-da-casa/` — o que vocês já corrigiram em página vale mais que o resto
3. `expert/dna-expert.md`, `expert/brand.md`, `expert/produtos/<produto>.md`
4. A pasta do lançamento, `lancamentos/<AAAA-MM-nome>/` — `briefing.md`, `pesquisa.md`,
   `avatar.md`, e `identidade-visual.md` se existir (prevalece sobre `expert/brand.md`)
5. `sirius-scale/frameworks/paginas/estrutura-de-pagina.md` — os blocos por tipo de
   página (§4) e a lista de conferência antes de publicar (§7.2)
6. O modelo de lançamento aplicável em `sirius-scale/frameworks/lancamentos/`

---

## A. Conteúdo rastreável

- [ ] **Toda afirmação forte rastreia** até `pesquisa.md`, `avatar.md` ou
      `expert/produtos/`. Cite a linha pra cada uma.
- [ ] Preço, parcelamento, garantia, bônus e entregáveis batem **exatamente** com
      `expert/produtos/<produto>.md`.
- [ ] **Nenhum depoimento fabricado.** Depoimento sem fonte nos arquivos de vocês
      é 🔴.
- [ ] Nenhum número de prova social (alunos, resultados, anos) sem fonte.
- [ ] Data, horário e prazo batem com o `briefing.md` do lançamento.
- [ ] Zero linguagem de IA (`sirius-scale/REGRAS.md` §1) — headline e subheadline são
      onde mais escapa.

## B. Estrutura

- [ ] Segue o LHTO (`sirius-scale/frameworks/lhto.md`) e a hierarquia: dobra (headline +
      subheadline + CTA) → prova → mecanismo → oferta → garantia → FAQ → CTA final.
      Exceção: low ticket pra público frio não tem botão no topo; o primeiro vem depois
      do valor (`sirius-scale/frameworks/lancamentos/low-ticket.md` §5). Nesse caso,
      botão no topo é que é o achado.
- [ ] Nível de consciência do avatar define a abertura — frio não começa na oferta.
- [ ] CTAs repetidos nos pontos certos, não só um no fim.
- [ ] Bloco de oferta segue a Arquitetura de Oferta em 14 seções
      (`sirius-scale/frameworks/oferta-14-secoes.md`).

## C. Técnico

- [ ] **Um único arquivo `.html`**, CSS dentro do `<style>`.
- [ ] Mobile-first e responsivo de verdade — confira `<meta name="viewport">` e as
      media queries.
      Conferir 375 px **no navegador com viewport emulado** (ou numa página de teste
      com `<iframe width=390>`): o Chrome sem janela no macOS não abre janela com menos
      de 500 px e entrega 500 px recortados sem avisar (medido no caso de origem,
      `sirius-scale/frameworks/paginas/cloudflare-pages-tecnica.md` §9).
- [ ] Sem framework pesado, sem lib desnecessária, sem CDN que não precisa estar
      ali. Google Fonts só se justificar.
- [ ] HTML semântico. Nada de `<div>` empilhado onde cabia `<section>`/`<h2>`.
- [ ] Abre sem erro. Rode uma checagem rápida no arquivo e olhe o console.
- [ ] Bloco que aparece ao rolar tem a rede de segurança: prazo de 2 s que o observador
      cancela (`estrutura-de-pagina.md` §7.1). Confere sem disparar pixel (prévia com o
      rastreio bloqueado): quebre o script de propósito ou desligue o JavaScript, role
      até o rodapé, e todo bloco tem que aparecer sozinho em até 3 s; com o script
      funcionando, nada aparece antes de a rolagem chegar nele. Contar só elemento com
      opacidade zero não basta: não pega bloco escondido com `visibility: hidden`.
- [ ] Os itens da lista de conferência de `estrutura-de-pagina.md` §7.2 que se aplicam a
      esta página (rolar no celular do topo ao rodapé, formulário de ponta a ponta,
      nada vencido nem "em breve").
- [ ] Visual sem cara de IA: a fonte é a do design system de vocês ou a da identidade do
      lançamento; se não for, o resumo do `webdesigner` diz por quê. Nenhum sinal de página
      genérica (rótulo em caixa alta em cima de cada título, seta no fim do botão, o mesmo card
      com a mesma sombra repetido) sem motivo.

## D. Links e rastreio

- [ ] Todo CTA aponta pro **destino real do briefing** (checkout, formulário,
      grupo). Nenhum `href="#"`, `href=""` ou link de exemplo esquecido.
- [ ] UTM nos links de saída, batendo com o padrão do lançamento.
- [ ] Pixel / tag de conversão presente se o briefing pedir.
- [ ] Formulário de página nova: manda pro CRM que o briefing define, com a tag do
      briefing; o pixel do Dash está na própria página, sem depender de gerenciador de
      tags (`cloudflare-pages-tecnica.md` §7); e um envio de teste na prévia foi lido de
      volta no CRM, com as UTMs (`cloudflare-pages-tecnica.md` §4.2; se o CRM for o Full
      Funnels, `sirius-scale/frameworks/automacao/fullfunnels-highlevel.md`).
- [ ] Página de vendas com formulário antes do pagamento manda pro **checkout já
      preenchido** com o que a pessoa digitou, mais as UTMs, o `src` e o `sck`
      (`cloudflare-pages-tecnica.md` §4.3). Teste na prévia, lendo o link do checkout.
      Low ticket não entra aqui: lá o clique vai puro pro checkout da oferta.
- [ ] Link externo não quebra o funil (abre onde deveria).

## E. Imagens

- [ ] **Nenhuma imagem inventada.** Cada uma é slot marcado
      (`<!-- IMAGEM: hero, 1200x800 -->`) com placeholder na dimensão certa.
- [ ] A entrega inclui a lista de slots com prompt pronto pro ChatGPT + dimensão
      exata + onde entra na página.
- [ ] Nenhum `src` apontando pra URL externa aleatória ou placeholder de stock.

## F. Sujeira esquecida (busca literal no arquivo)

- [ ] `lorem`, `ipsum`, `TODO`, `XXX`, `FIXME`, `[inserir`, `preencher`
- [ ] `exemplo.com`, `#`, `href=""`
- [ ] Texto de outro produto ou de outro lançamento copiado e não trocado
- [ ] Comentário de desenvolvimento que não era pra ficar

## G. Entrega

- [ ] Salvo em `entregas/<lançamento>/<nome-da-pagina>.html`.
- [ ] A entrega veio com o resumo em lista numerada: o que montou, as decisões de
      copy rastreadas ao dado real, e a lista de imagens pra gerar.
