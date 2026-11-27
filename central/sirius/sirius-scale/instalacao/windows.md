# Sirius Scale: instalação no Windows

(Passo a passo pra instalar o sistema da Sirius Scale no Claude Code, no Windows 10 ou 11. As etapas 1 a 3 são o básico. As etapas 4 a 6 ligam edição de vídeo, Google Ads e a rotina de tráfego, e podem ficar pra sessão de instalação com a consultoria.)

## O que vocês vão ter no fim

O sistema que a Sirius usa na própria operação, rodando no computador de vocês, com a conta de vocês:

- Agentes: copy, design, página, tráfego e vídeo.
- Checagens: `/preflight`, `/revisar`, `/debriefing`, `/mapa-edicao`, `/pente-fino` e `/humanizer`.
- Os frameworks da casa, as regras e os modelos em branco.
- Com as etapas 4 a 6: edição de vídeo aqui mesmo, leitura e montagem de campanha no Google e a leitura diária do tráfego.

Nenhum dado que identifique outro cliente vem junto, e o que vocês escreverem fica só com vocês.

A operação da Sirius roda em Mac, e o caminho do Windows ainda não foi testado do começo ao fim. Se alguma etapa travar, mandem o print pra consultoria: a correção entra neste guia.

## Como usar este guia

Cada etapa diz quem faz. Onde estiver **Cole no Claude**, é só colar o texto na conversa e acompanhar. Onde estiver **Vocês fazem**, é uma tela ou uma senha que só vocês podem abrir. Quando o Claude pedir permissão pra rodar um comando, leiam o que ele vai fazer e permitam.

## Etapa 1. Instalar o Claude e o sistema

**Vocês fazem:**

1. Assinem o plano Pro ou maior do Claude. O gratuito não roda o Claude Code.
2. Baixem o app em claude.ai/download, instalem e entrem com a conta de vocês.
3. Baixem o arquivo "Sirius Scale - instalação", do link que a consultoria mandou, cliquem com o botão direito e escolham Extrair tudo.
4. Movam pra Documentos a pasta que tem o arquivo COMECE-AQUI dentro. O Extrair tudo pode criar uma pasta dentro da outra: a certa é a de dentro. Não deixem em Downloads: é nela que vocês vão trabalhar todo dia.
5. No app, abram a aba **Code** e escolham essa pasta. Se o app perguntar se confia nesta pasta, confirmem.

**Cole no Claude:**

```
Instale o Git for Windows com este comando: winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements
```

É ele que dá ao Claude o terminal que os agentes de vídeo, design e página usam. Se o Windows pedir permissão, cliquem em Sim. Terminou, fechem e abram o app na mesma pasta. Se não der certo, baixem em git-scm.com e instalem com as opções padrão.

**Cole no Claude:**

```
Leia o COMECE-AQUI e me faça as perguntas pra preencher o CLAUDE.md.
```

Se a resposta não falar do COMECE-AQUI, a pasta aberta é a errada.

## Etapa 2. Conectar Dash Fácil, Meta e Hotmart

Conectado, o Claude lê os números direto da ferramenta em vez de pedir print. Sem conexão tudo funciona igual: vocês mandam o print ou o arquivo exportado.

**Vocês fazem**, no claude.ai, pelo navegador: Personalizar, Conectores, botão +, Adicionar conector personalizado. Se aparecerem campos de Client ID ou OAuth, deixem em branco.

1. **Dash Fácil:** nome Dash Fácil, endereço https://mcp.dashfacil.com/mcp. Entrem com a conta do Dash e autorizem.
2. **Meta:** nome Meta Ads, endereço https://mcp.facebook.com/ads. Entrem com o Facebook que tem acesso à conta de anúncios e aprovem as permissões.
3. **Hotmart:** tem conector oficial, mas pede credencial de desenvolvedor da conta. Façam junto com a consultoria.

Se preferirem, façam a da Meta também na sessão com a consultoria.

Depois abram uma conversa nova na aba Code, pra os conectores aparecerem nela.

**Cole no Claude:**

```
Liste minhas subcontas no Dash Fácil, minhas contas de anúncio na Meta e o gasto de ontem.
```

## Etapa 3. Montar a ficha do negócio

Os agentes leem essa ficha antes de escrever qualquer coisa. Sem ela, eles param e perguntam. É de propósito: peça sem dado real sai bonita e não vende.

**Cole no Claude:**

```
Monte comigo a ficha da expert: DNA, marca e um arquivo por produto, usando os modelos de sirius-scale/modelos/. Me pergunte o que faltar.
```

## Etapa 4. Edição de vídeo (HyperFrames)

Com isto, o agente de vídeo monta a primeira versão aqui mesmo, com corte, legenda, gráfico animado e som. Sem isto, ele entrega um mapa de edição pra quem edita no CapCut. No Windows, a transcrição automática ainda não foi testada, e a legenda pode precisar de outro caminho.

**Cole no Claude:**

```
Instale o módulo de vídeo seguindo sirius-scale/instalacao/video.md.
```

**Vocês fazem**, se o Windows pedir: clicar em Sim na janela de permissão de instalação. O Claude usa o winget, o instalador de programas do próprio Windows.

Num Mac que já tinha o básico, levou 6 minutos e baixou uns 380 MB. Pode parecer parado por alguns minutos. No fim ele gera um vídeo de teste de 10 segundos. Gerou, está pronto: abram uma conversa nova.

## Etapa 5. Google Ads

A Meta se liga pelo site. O Google pede uma credencial própria da conta de vocês, por isso esta etapa rende mais na sessão com a consultoria. Depois dela, o Claude lê a conta direto e monta campanha pausada. Ligar a campanha continua com vocês, na tela do Google Ads.

**Cole no Claude:**

```
Vamos ligar o Google Ads seguindo sirius-scale/instalacao/google-ads.md. Me passe uma etapa por vez.
```

**Vocês fazem:** as telas do Google Ads e do Google Cloud, e o login no fim. O Claude diz onde clicar. As chaves vão direto num arquivo do computador de vocês, nunca na conversa.

A montagem foi validada a seco no Google, mas ainda não rodou de verdade em conta de cliente. Na primeira campanha, confiram tudo na tela antes de ligar.

**Vídeo de anúncio:** o Google Ads só roda vídeo que está no YouTube. O Claude sobe o vídeo por esta mesma conexão, sempre não listado, e ele fica num canal do Google ligado à conta de anúncios de vocês, não no canal de vocês. Quem preferir subir à mão em youtube.com, como Não listado, só passa o link pro Claude.

## Etapa 6. Rotina de tráfego (quando a leitura diária ficar repetitiva)

Todo dia, no horário marcado, o Claude lê Dash, Meta e Google, roda o preflight, aplica a régua e deixa o relatório com o que sugere mexer. Ele não aplica nada: quem mexe em verba são vocês, nas plataformas.

**Cole no Claude:**

```
Crie a rotina de tráfego seguindo sirius-scale/rotinas/trafego-diario.md.
```

A rotina só roda com o computador acordado e o app do Claude aberto no horário. Em notebook, escolham um horário em que ele costuma estar aberto. Ela foi testada à mão e ainda não rodou agendada fora da casa: na primeira semana, alguém confere o relatório contra a tela. Por enquanto cobre lançamento. Perpétuo se lê numa conversa, com o agente de tráfego.

## Quando chegar uma versão nova

O arquivo tem "atualização" no nome. Deixem em Downloads, abram o Claude na pasta do sistema e **cole no Claude:**

```
Atualize o sistema com o arquivo de atualização da Sirius Scale que está em Downloads, seguindo a seção 6 do COMECE-AQUI que vem dentro dele.
```

Nada do que é de vocês é tocado: `CLAUDE.md`, `expert/`, `lancamentos/`, `funis/`, `frameworks-da-casa/` e `entregas/` ficam como estão.

## Se travar

- **Comando não encontrado logo depois de instalar algo:** fechem e abram o app do Claude. No Windows isso é comum, porque o programa recém-instalado só aparece depois de reabrir.
- **Faltou o Git ou o Bash:** é o Git for Windows da etapa 1. Colem o pedido de instalação no Claude e reabram o app.
- **Conector pedindo login de novo:** é normal de tempos em tempos. Abram o claude.ai e entrem de novo.
- **Qualquer outra coisa:** peçam ao Claude pra explicar o erro em português e mandem o print pra consultoria.
