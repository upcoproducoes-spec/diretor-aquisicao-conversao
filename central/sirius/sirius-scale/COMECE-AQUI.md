# Comece aqui · Sirius Scale v0.6

Esta pasta é o sistema da Sirius Scale instalado no Claude Code: os agentes (copy, design, página,
tráfego e vídeo), as checagens (`/preflight`, `/revisar`, `/debriefing`, `/pente-fino`, `/mapa-edicao`,
`/humanizer`), as regras e os frameworks. Roda no computador de vocês, com a conta de vocês.

**Já têm o sistema instalado e chegou uma versão nova? Vão direto pra seção 6, Atualização.**

## 1. Instalar

O passo a passo está em `sirius-scale/instalacao/`, um pra cada computador: `mac.md` e `windows.md`. Ele traz
o que só vocês podem fazer e o que é só colar no Claude. Os módulos que precisam de instalação têm guia próprio,
que o Claude segue:

| Módulo | Pedido |
|---|---|
| Edição de vídeo (HyperFrames) | "Instale o módulo de vídeo seguindo `sirius-scale/instalacao/video.md`" |
| Google Ads (leitura, subida de vídeo e montagem pausada) | "Vamos ligar o Google Ads seguindo `sirius-scale/instalacao/google-ads.md`" |
| Rotina de tráfego diária | "Crie a rotina de tráfego seguindo `sirius-scale/rotinas/trafego-diario.md`" |

## 2. Conectar as ferramentas (uma vez, de preferência junto com a consultoria)

Conectado, o Claude lê os números direto da ferramenta em vez de pedir print. Sem conexão, tudo
funciona igual: vocês mandam o print ou o arquivo exportado.

Os conectores se ligam no claude.ai, pelo navegador: **Personalizar** (em inglês, *Customize*) →
**Conectores** (*Connectors*) → **+** → **Adicionar conector personalizado** (*Add custom
connector*). Se aparecerem campos de "Client ID" ou "OAuth", deixem em branco. Depois de ligar,
abram uma conversa nova na aba Code pra ele aparecer lá.

1. **Dash Fácil (comece por ele).** Nome `Dash Fácil`, endereço `https://mcp.dashfacil.com/mcp`.
   Entre com a conta do Dash e autorize. Teste: "liste minhas subcontas no Dash Fácil".
   - O login expira de tempos em tempos e pede de novo. É normal.
   - O Claude só lê. Criar ou editar lançamento, só com pedido escrito. Conta de anúncio nunca se
     cadastra pelo conector: isso quebra a atualização do Dash. Use a tela.
   - Pra desligar: Dash → Configurações → IA (MCP).
2. **Meta (anúncios).** Nome `Meta Ads`, endereço `https://mcp.facebook.com/ads`. Entre com o
   Facebook que tem acesso à conta de anúncios e aprove as permissões que a Meta pedir. Teste:
   "liste minhas contas de anúncio na Meta e o gasto de ontem".
   - Com a Meta ligada, o Claude lê os números e **monta campanha pausada**. Quem ativa e mexe em
     verba são vocês, no Gerenciador de Anúncios (`sirius-scale/REGRAS.md` §6).
   - Façam a primeira conexão junto com a consultoria.
3. **Hotmart.** Tem conector oficial, mas pede credencial de desenvolvedor da conta. Façam junto
   com a consultoria.
4. **Google Ads.** Sem conexão, o dado chega pelo Dash Fácil, que já cruza anúncio com lead e venda.
   A conexão direta pede credencial própria da conta e roda no computador de vocês: é o guia
   `sirius-scale/instalacao/google-ads.md`, de preferência junto com a consultoria.

## 3. O que dá pra pedir

| Quem | O que faz | Exemplo de pedido |
|---|---|---|
| agente `copy` | todo texto que o público lê: anúncio, roteiro de vídeo, e-mail, WhatsApp, texto de página, VSL, aula, live | "Use o agente copy pra escrever 3 roteiros de captação da Black pra quem já é aluna" |
| agente `designer` | estático de anúncio (prompt pronto pro ChatGPT ou HTML virando PNG), e-book e PDF | "Use o designer pra montar o estático do anúncio 2 em feed e story" |
| agente `webdesigner` | página em HTML de arquivo único (captura, vendas, obrigado) | "Use o webdesigner pra montar a página de captura da Black" |
| agente `gestor-trafego` | lê o Dash, a Meta e o Google, monta o pacote de campanha e, com as conexões ligadas, monta a campanha pausada. Ativar e mexer em verba é com vocês | "Use o gestor-trafego pra ler a captação de ontem e me dizer onde mexer" |
| agente `video` | com o módulo de vídeo instalado, monta a primeira versão aqui. Sem ele, entrega o mapa de edição bloco a bloco pro CapCut ou pro editor | "Use o agente video pra editar este vídeo" |
| `/preflight` | confere a saúde das contas numa lista fixa de 12 itens: gasto contra o teto, entrega restrita, expansão de público, país, idade, lance, UTM, rastreio da página e o pixel dos anúncios. Rodem antes de subir campanha | `/preflight` |
| `/revisar` | confere uma entrega contra os frameworks, com olhos frescos. Em tráfego, começa pelo `/preflight` | `/revisar` e diga o que conferir |
| `/debriefing` | análise do resultado de um lançamento ou funil, terminando em decisão | `/debriefing` da Black |
| `/mapa-edicao` | transforma copy de vídeo em instrução de edição | `/mapa-edicao` e cole o roteiro |
| `/pente-fino` | no fim de uma sessão longa, registra o que se aprendeu em `frameworks-da-casa/` | `/pente-fino` |
| `/humanizer` | tira a cara de IA de um texto | `/humanizer` e cole o texto |

Antes de escrever, os agentes leem a ficha da expert (`expert/`) e a pasta do lançamento
(`lancamentos/<AAAA-MM-nome>/`: briefing, pesquisa, avatar e banco de ângulos) ou do funil
(`funis/<nome>/`). **Se faltar alguma coisa, eles param e perguntam.** É de propósito: peça sem
dado real sai bonita e não vende. Os modelos em branco estão em `sirius-scale/modelos/`.

## 4. Onde fica cada coisa

| Pasta | De quem | O que é |
|---|---|---|
| `sirius-scale/` | Sirius Scale | regras, frameworks, modelos, guias de instalação, a rotina e as ferramentas do Google. A atualização troca a pasta inteira: não editem. |
| `.claude/` | Sirius Scale | os agentes e as checagens. A atualização copia por cima, sem apagar o que é de vocês. |
| `COMECE-AQUI.md` | Sirius Scale | este guia. A atualização troca. |
| `CLAUDE.md` | de vocês | quem é quem, produtos, ferramentas, o que está rodando agora |
| `expert/` | de vocês | DNA da expert, marca e um arquivo por produto |
| `lancamentos/<AAAA-MM-nome>/` | de vocês | briefing, pesquisa, avatar e banco de ângulos de cada lançamento |
| `funis/<nome>/` | de vocês | funil perpétuo: briefing, avatar, pesquisa e desempenho |
| `frameworks-da-casa/` | de vocês | o que vocês corrigirem ou criarem. Vale mais que o framework da Sirius Scale. |
| `entregas/` | de vocês | onde os agentes salvam o que fazem (as análises ficam numa subpasta "analises", que o Claude cria na primeira vez) |
| `.env` e `.credenciais/` | de vocês | as chaves do Google, se ligarem esse módulo. Só existem no computador de vocês, nunca vão pra conversa e o Claude não lê. |

A linha `@sirius-scale/REGRAS.md`, logo abaixo do título do `CLAUDE.md`, é o que liga as regras da
Sirius Scale. O Claude pode escrever à vontade no `CLAUDE.md`, mas essa linha tem que continuar lá.

## 5. Quando uma peça sair errada

Corrija com o Claude e peça: "registre essa correção em frameworks-da-casa". A regra fica lá, e
dali pra frente ele segue a de vocês. No fim de uma sessão longa, rode `/pente-fino` pra não perder
o que apareceu no meio dela. Não editem `sirius-scale/`: a próxima versão apagaria a mudança.

## 6. Atualização

Cada versão nova chega num arquivo .zip só com as peças da Sirius Scale. O que é de vocês não vem
no zip e não é tocado.

1. Baixem o arquivo novo. Ele vai pra pasta Downloads, com "atualização" no nome.
2. Abram o Claude, na aba **Code**, na pasta do sistema (a de sempre).
3. Escrevam: "Atualize o sistema com o arquivo (ou a pasta) de atualização da Sirius Scale que está
   em Downloads, seguindo a seção 6 do COMECE-AQUI que vem dentro dele."
4. Se aparecer um pedido de permissão, cliquem no botão que permite **só desta vez**.
5. No fim, o Claude diz qual versão ficou instalada. Abram uma conversa nova: os agentes e as
   checagens novos aparecem nela.

O que o Claude faz na atualização (ele segue esta lista):

1. Acha o zip (ou a pasta já aberta) de atualização: tem "atualização" no nome e, dentro, não tem
   `CLAUDE.md`. Zip com `CLAUDE.md` dentro é de instalação: esse ele não usa. Se houver mais de um,
   usa o de versão mais nova. Abre o zip numa pasta temporária, fora da pasta do sistema.
2. De dentro da pasta do sistema, roda o script que vem na atualização:
   `bash "<pasta da atualização>/atualizar.sh"`. É o caminho previsto pra troca: a trava do
   `.claude/settings.json` impede o Claude de editar `sirius-scale/` e `.claude/` com as
   ferramentas de arquivo, de propósito, e o script é a exceção combinada. Ele confere antes se a
   pasta é a do sistema e se a versão é mais nova. Se ele disser "PAREI", o Claude para e conta o
   motivo.

   **No Windows** o comando é outro, porque o script precisa do bash do Git for Windows, e o `bash`
   solto pode ser o de outro programa. No PowerShell, de dentro da pasta do sistema:
   - Confere se ele existe: `Test-Path "$env:ProgramFiles\Git\bin\bash.exe"`. Instalado só pro usuário, ele
     fica em `$env:LOCALAPPDATA\Programs\Git\bin\bash.exe`: se esse existir, use esse caminho abaixo.
   - Se não existir, avisa a pessoa que o Windows pode pedir um Sim e instala:
     `winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements`.
     Se o `winget` falhar, pede pra pessoa instalar por git-scm.com, com as opções padrão.
   - Roda: `& "$env:ProgramFiles\Git\bin\bash.exe" "<pasta da atualização>/atualizar.sh"`, com barras
     normais no caminho.
3. O script troca a pasta `sirius-scale/` inteira pela nova.
4. Copia a pasta `.claude/` nova por cima da de vocês, sem apagar nada que já está lá. As
   permissões que vocês já deram e qualquer agente ou checagem que vocês criaram continuam.
5. Troca este `COMECE-AQUI.md` e confere que o `CLAUDE.md` não mudou. Não mexe em mais nada:
   `CLAUDE.md`, `expert/`, `lancamentos/`, `funis/`, `frameworks-da-casa/` e `entregas/` ficam
   como estão.
6. Depois do script, o Claude lê o `sirius-scale/O-QUE-MUDOU.md` novo. Se ele mandar apagar algum arquivo antigo de
   `.claude/`, apaga só esse. Se tiver mudança na seção "Nos arquivos de vocês", aplica juntando com
   o que já existe, mostra o que mexeu e não apaga nada de vocês. Se vocês pularam versões (estavam
   na v0.3 e chegou a v0.6, por exemplo), o Claude aplica o "Nos arquivos de vocês" de cada versão
   pulada, da mais antiga pra mais nova, não só o da última.
7. Diz a versão que está em `sirius-scale/VERSAO.md`.

A mudança num arquivo de vocês (o `CLAUDE.md`, por exemplo) nunca vem como arquivo novo, porque
isso apagaria o que vocês escreveram. Ela vem descrita no `O-QUE-MUDOU.md`, como no item 6.
