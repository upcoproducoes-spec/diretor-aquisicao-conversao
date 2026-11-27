# Ligar o Google Ads

> Guia pro Claude conduzir, uma etapa por vez, a pedido: "Vamos ligar o Google Ads seguindo
> `sirius-scale/instalacao/google-ads.md`". As telas são da pessoa, os comandos são do Claude. Os detalhes
> de cada ferramenta estão em `sirius-scale/ferramentas/google/LEIA-ME.md`.

No fim, o Claude lê a conta do Google direto, sobe o vídeo do anúncio, não listado, e monta campanha pausada.
Quem liga é o dono da conta, na tela do Google Ads (`sirius-scale/REGRAS.md` §6). A leitura roda por um servidor oficial do Google que o próprio Claude
Code abre, sem terminal aberto. A montagem roda pelas ferramentas de `sirius-scale/ferramentas/google/`, com
as mesmas credenciais.

**O que já foi provado:** leitura na API real, servidor aberto pelo Claude Code, validação a seco de uma
campanha inteira e a subida real de um vídeo de teste, tudo no caso de origem. **O que ainda não:** a primeira
campanha de verdade numa conta de cliente, a subida no canal do próprio cliente, a subida numa conta que nunca
subiu vídeo, o login de ponta a ponta com pessoa clicando, e o Windows. Na primeira campanha, confira tudo na tela.

**As chaves nunca entram na conversa.** Se alguém colar uma no chat, avise pra trocar. O Claude não lê o `.env`.

## Etapa 1. Conta gerente (a pessoa faz)

O acesso pela API passa por uma conta gerente do Google Ads (o nome em inglês é MCC). É grátis.

1. Quem já tem conta gerente pula pra etapa 2.
2. Crie em ads.google.com/home/tools/manager-accounts, com o mesmo e-mail que administra a conta de anúncios.
3. Na conta gerente, em Contas, vincule a conta de anúncios pelo número dela. Na conta de anúncios, aceite o
   convite, em Administrador, Acesso e segurança, Gerentes.

## Etapa 2. Token de desenvolvedor (a pessoa faz)

1. Na **conta gerente**: Administrador, Central de API. Se o menu não aparecer, a conta aberta não é a gerente.
2. Preencha o formulário e aceite os termos.
3. Guarde o token que aparece. É o `GOOGLE_ADS_DEVELOPER_TOKEN`.
4. Confira o nível de acesso ali mesmo. No caso de origem, o nível Explorer lê e escreve em conta real, com
   limite de 2.880 operações por dia. Token só de teste não alcança conta real: se aparecer
   `DEVELOPER_TOKEN_NOT_APPROVED`, peça o nível acima na mesma tela.

## Etapa 3. Projeto no Google Cloud (a pessoa faz)

Em console.cloud.google.com, com o mesmo e-mail:

1. **Projeto:** crie um projeto novo. O id dele é o `GOOGLE_PROJECT_ID`.
2. **API:** em APIs e serviços, Biblioteca, ative a Google Ads API.
3. **Tela de consentimento OAuth:** tipo Externo, com nome do app e e-mail. Depois, **publique o app**. Em modo
   de teste, o Google derruba a autorização a cada 7 dias, e a conexão cai sem aviso. No caso de origem esse foi
   o motivo de meses de conexão instável.
4. **Credenciais:** Criar credenciais, ID do cliente OAuth, tipo **App para computador**. Guarde o ID e o
   segredo: são `GOOGLE_ADS_CLIENT_ID` e `GOOGLE_ADS_CLIENT_SECRET`.

## Etapa 4. O arquivo `.env`

1. **O Claude** cria o arquivo, sem valores: `cp sirius-scale/ferramentas/google/env.exemplo .env`, e abre pra
   pessoa: no Mac, `open -e .env`; no Windows, `notepad .env`.
2. **A pessoa** preenche e salva. `GOOGLE_ADS_LOGIN_CUSTOMER_ID` é a conta gerente, só com números.
   `TETO_CAMPANHA_DIA` é o teto por campanha que quem decide a verba combinou. O Claude não sugere esse número.
3. Escreva também esse teto no `CLAUDE.md`, se ainda não estiver lá.

## Etapa 5. Ligar a conexão (o Claude faz, a pessoa autoriza)

1. **`uv`**, o programa que roda as ferramentas sem precisar instalar Python. Confira com `uv --version`. Se
   faltar: no Mac, `curl -LsSf https://astral.sh/uv/install.sh | sh`, que não pede senha; no Windows,
   `winget install --id=astral-sh.uv -e`. Depois, reabra o app.
2. **Autorizar.** Rode `uv run sirius-scale/ferramentas/google/gerar_token.py`, com espera de 5 minutos. Abre o
   navegador: a pessoa entra com o e-mail que tem acesso à conta de anúncios e autoriza. Se o Google mostrar um
   aviso de app não verificado, é o app de vocês mesmos: Avançado, Continuar.
3. **Preparar o servidor.** `uv run sirius-scale/ferramentas/google/mcp_google.py --preparar`, com espera de 5
   minutos. Baixa uns 400 MB, uma vez só.
4. **`.mcp.json`** na raiz da pasta, com o bloco de `sirius-scale/ferramentas/google/LEIA-ME.md`. Se o arquivo já
   existir, acrescente só o bloco `google-ads-mcp`.
5. **Conversa nova.** Peça pra pessoa abrir uma conversa nova e aprovar o servidor `google-ads-mcp` quando o app
   perguntar. Sem aprovar, ele fica pendente e o Claude não enxerga o Google.

## Etapa 6. Testar

Na conversa nova, a pessoa cola:

```
Liste minhas campanhas do Google que gastaram nos últimos 7 dias e rode a /preflight.
```

A ferramenta de listar contas mostra só as de acesso direto. Conta que vem pela gerente não aparece nela, mas
responde na busca, com o número da conta.

## Na primeira campanha

Siga "Montar no Google", no agente `gestor-trafego`, com alguém olhando a tela do Google Ads. Depois de montar,
confira campanha, grupo, público, país e anúncio na tela antes de ligar. Anote o que fugiu do esperado em
`frameworks-da-casa/`.
