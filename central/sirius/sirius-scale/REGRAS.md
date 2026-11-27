# Regras da Sirius Scale

> Valem pra todo pedido, em qualquer agente. O `CLAUDE.md` de vocês puxa este arquivo.

## 1. Tom

- Português brasileiro informal e natural. Direto e orientado a resultado.
- Proibido "linguagem de IA": nada de "no mundo de hoje", "não é apenas X, é Y", "mergulhe",
  "desvende", "eleve", "descubra o segredo", frase de efeito vazia ou adjetivo empilhado. Se
  soar como IA, reescreve.
- Confirmação e correção em lista numerada, não em prosa arrastada.

## 2. Nada inventado (inegociável)

- Só usa dado que está nos arquivos de vocês (`expert/`, `lancamentos/`, `funis/`). Nada de
  inventar número de pesquisa, dor de avatar, depoimento ou preço.
- Faltou dado? Pergunta e para. Nunca preenche buraco com suposição.
- Dúvida de forma é outra coisa e não trava entrega. Palavra, título, ordem, layout: aplica a
  recomendação, entrega e lista no fim o que decidiu. O que para é número, preço, data, promessa,
  dado do negócio, verba e o que contradiz decisão registrada.
- Toda afirmação forte de copy rastreia até um dado real (pesquisa, avatar, oferta). Se não
  rastreia, não entra.

## 3. Copy

- Todo texto que o público final lê (anúncio, e-mail, WhatsApp, roteiro, página, legenda) é
  escrito pelo agente `copy`, nunca direto na conversa. O agente lê a ficha da expert e a pasta
  do lançamento antes de escrever; escrever direto pula essa leitura.
- Depois do `copy`, roda o `/humanizer` no texto inteiro. O `copy` garante que o texto está
  ancorado no dado real. O humanizer garante que ele não soa como IA. Um não substitui o outro.
- Ajuste pontual num texto que o `copy` já fez (trocar palavra, cortar caractere pra caber no
  limite) não precisa passar de novo. Peça nova, ângulo novo ou reescrita passa.

## 4. Frameworks

- Ficam em `sirius-scale/frameworks/`. Siga à risca; não troque por "boa prática genérica".
- Cada seção diz a **força** da evidência, ou seja, quantas vezes aquilo se repetiu:
  - **PADRÃO CONSISTENTE:** se repetiu em 3 ou mais casos e foi confirmado. É regra.
  - **PADRÃO CONSISTENTE (proposto):** se repetiu, mas o Rodrigo ainda não confirmou. Vale como
    VARIAÇÃO ISOLADA.
  - **VARIAÇÃO ISOLADA:** apareceu num caso só. Use se o contexto pedir algo parecido.
  - **PADRÃO INCONCLUSIVO:** hipótese. Pode usar como teste, avisando na entrega.
- O cabeçalho de cada arquivo diz o **alcance**, ou seja, em quantos negócios aquilo foi visto:
  - `NÃO TESTADO FORA`: nasceu num negócio só.
  - `TESTADO EM N CLIENTES` (ou `PROJETOS`): se confirmou em N negócios. Com "(proposto)", ainda
    falta o ok do Rodrigo.
  - `UNIVERSAL`: fato de plataforma ou especificação. Vale pra qualquer negócio.
  - `METODOLOGIA EXTERNA`: método de outra pessoa, escrito nas palavras da casa. O que a casa
    mudou está marcado no arquivo.
- Força e alcance são coisas diferentes. Quase tudo aqui nasceu em outros negócios: ao aplicar,
  diga na entrega "baseado em framework de outro negócio, ainda sem teste aqui". E, se a seção for
  PADRÃO INCONCLUSIVO, diga também que é hipótese.
- Quando um arquivo diz que as contagens e os rótulos são os da base completa da casa, vale o
  rótulo: os casos que não aparecem no texto contaram pra ele.
- `frameworks-da-casa/` vale mais que `sirius-scale/frameworks/`. Correção de vocês vai pra lá.
- Nos frameworks de vocês (`frameworks-da-casa/`), o alcance é o negócio de vocês ("DA CASA"),
  menos fato de plataforma, que continua `UNIVERSAL`. A força conta lançamentos ou peças. Regra nova nasce VARIAÇÃO ISOLADA ou PADRÃO
  INCONCLUSIVO e vira CONSISTENTE quando se repete em 3. Quem sobe uma regra pra CONSISTENTE é
  quem é dono da operação, nunca o Claude sozinho.
- Nunca edite `sirius-scale/` nem `.claude/` por conta própria: quem troca essas pastas é a
  atualização (`COMECE-AQUI.md`, seção 6).

## 5. Ao fechar uma peça grande

Peça grande é página, pacote de criativos, sequência de e-mail, campanha, VSL ou lançamento
inteiro. Ajuste pontual não entra.

1. O agente certo faz (texto sempre pelo `copy`, regra 3).
2. O `/humanizer` passa no texto inteiro.
3. O `/revisar` confere a entrega contra os frameworks e o dado de vocês, com olhos frescos. Ele
   aponta e não corrige: corrigir é decisão de vocês.
4. Vocês revisam. O que foi corrigido e vale pra próxima vira regra em `frameworks-da-casa/`, com
   a data, a peça que originou, o porquê e o rótulo de força (regra nova nasce VARIAÇÃO ISOLADA ou
   PADRÃO INCONCLUSIVO).
5. No fim da sessão, o `/pente-fino` procura o que se aprendeu no meio do caminho e ainda não
   ficou escrito.

Ao fechar um lançamento ou um período de funil: `/revisar` → corrigir → `/debriefing` → registro
em `frameworks-da-casa/` → `/pente-fino`.

## 6. Escrita em plataforma (anúncio, checkout, disparo)

**Meta (com o conector ligado).** O Claude monta a campanha e vocês ligam.

1. O Claude pode montar campanha, conjunto e anúncio, **sempre pausados**. Só monta com o pedido
   escrito de quem decide e com o pacote aprovado (estrutura, públicos, nomes, verba, criativos).
2. Antes de montar, ele mostra o resumo do que vai criar e espera o ok escrito.
3. O teto de verba é combinado antes. Nada é montado acima dele.
4. Depois de montar, ele lê de volta da Meta e mostra uma linha por conjunto: status pausado,
   orçamento, idade, país, Advantage e públicos. Escrita só conta com leitura de volta.
5. **Ativar, pausar o que está rodando e mexer em orçamento ou lance é com vocês**, no
   Gerenciador de Anúncios. O Claude não faz isso, nem com pedido urgente. Se algo rodando precisa
   mudar, ele monta a versão corrigida pausada, e vocês trocam.

**Google Ads (com as ferramentas de `sirius-scale/ferramentas/google/`).** Mesma regra da Meta. O Claude
monta campanha, grupo e anúncio **sempre pausados**, com pedido escrito, pacote aprovado e dentro do teto
de verba do `.env` (`TETO_CAMPANHA_DIA`). Antes de escrever, roda a prévia e mostra o resumo. Depois, lê de
volta e roda a conferência. **Ligar, pausar o que está rodando e mexer em orçamento ou lance é com vocês**,
na tela do Google Ads. O vídeo do anúncio sobe sempre não listado, com o mesmo ok escrito. Vídeo público é
decisão de vocês, fora do sistema. Sem as ferramentas ligadas, o dado chega pelo Dash Fácil e quem sobe são
vocês.

**Hotmart.** O Claude não faz reembolso, cupom, cancelamento nem mudança em produto, oferta ou
checkout. Lê e prepara; quem faz são vocês.

**Dash Fácil.** Leitura. Criar ou editar lançamento pelo conector, só com pedido escrito
(`sirius-scale/frameworks/trafego/leitura-dash-facil.md` §9). Conta de anúncio nunca se cadastra
pelo conector.

**Disparo pra lead ou aluno** (e-mail, WhatsApp). Só sai com o pedido escrito de quem decide e com
o texto final aprovado (regra 3 + revisão).

**Credenciais.** Chave e token moram no `.env` e em `.credenciais/`, nunca na conversa nem num arquivo que
vai pra outro lugar. Se alguém colar chave no chat, avise pra trocar. O Claude não lê esses arquivos.

**Dinheiro.** Número de dinheiro (faturamento, gasto, pagamento) sempre com a fonte: a tela ou o
relatório da plataforma. Diga de onde saiu. Número sem fonte não entra em decisão.
