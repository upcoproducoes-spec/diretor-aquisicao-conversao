# Envio automatizado de WhatsApp (Baileys) — armadilhas técnicas

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma
> **Alcance:** UNIVERSAL — é comportamento do Baileys e do protocolo do
> WhatsApp Web, não do cliente. Vale pra qualquer número, projeto ou empresa.
> Nenhuma das armadilhas (versão quebrada, envio calado pra número inexistente,
> processo zumbi, QR x pairing code) depende do cliente de origem.
> **Do caso:** só o contexto de origem (o grupo interno de um lançamento) e o
> julgamento de risco/volume do §1, que é decisão de operação, não fato técnico.
> ⚠️ O rótulo do §2, *"CONSISTENTE dentro desta montagem"*, está certo e é
> exatamente a distinção dos dois eixos: força alta dentro de uma base, alcance
> ainda não testado fora.

> Montado ao vivo no caso de origem, no número pessoal do Rodrigo, pra mandar o
> panorama diário de um lançamento num grupo de WhatsApp da equipe com o
> cliente. Tudo abaixo foi **medido na tela**, não suposto — cada item custou uma
> tentativa falha. **VARIAÇÃO ISOLADA**: uma montagem, um número, um projeto.
> Se repetir em outro cliente/máquina, subir pra CONSISTENTE.

Segue a regra da casa pra código que escreve em plataforma: armadilha de
plataforma se registra (e se consulta) **antes** de montar código novo, pra não
repetir tentativa que já falhou. Mensagem pra lead ou aluno segue
`sirius-scale/REGRAS.md` §6: só sai com o pedido escrito de quem decide e o
texto final aprovado.

## 1. Por que Baileys e não a API oficial

A **Cloud API oficial da Meta não manda mensagem em grupo** — só 1:1, e só
com quem iniciou conversa. Pra relatório interno em grupo ela não serve, por
mais que seja o caminho "certo" em qualquer outro contexto.

Baileys fala o protocolo do WhatsApp Web direto, sem navegador aberto. É
não-oficial: risco real (pequeno, mas real) de ban do número se a Meta
identificar padrão de bot. **Mitigação adotada: volume baixo e pontual** —
um relatório por dia, pra um grupo. Não usar esse caminho pra disparo em
massa; pra isso existem os modos de disparo de
`sirius-scale/frameworks/copy/disparo-whatsapp.md`.

## 2. A versão `latest` do npm está quebrada — *CONSISTENTE dentro desta montagem*

`npm install @whiskeysockets/baileys` trazia a `7.0.0-rc14`, que era a tag
`latest`. **Ela não conecta:** o servidor do WhatsApp derruba a conexão no
registro, com `Connection Closed` / statusCode 428, tanto no pairing code
quanto no QR. O sintoma engana — parece rede, proxy ou número bloqueado.

A estável era a **`6.7.24`**, publicada sob a tag `legacy` (versões da época
da montagem; a regra de conferir a tag continua valendo):

```
npm install @whiskeysockets/baileys@6.7.24
```

Conferir a tag antes de instalar: `npm view @whiskeysockets/baileys dist-tags`.
Nesta biblioteca **`latest` não quer dizer estável**.

## 3. O "erro" logo depois de parear é normal — não é falha

Assim que o pareamento dá certo, o WhatsApp manda um stream error
**515 (`restartRequired`)** e a conexão cai. Isso **não é erro**: a sessão
está válida e salva. O cliente só precisa **reconectar usando as credenciais
já gravadas**.

O log denuncia a diferença — procurar por esta linha antes de concluir que
falhou:

```
"msg":"pairing configured successfully, expect to restart the connection..."
```

Script que faz `process.exit()` no primeiro `connection: 'close'` joga fora
um pareamento que deu certo. Tratar 515 como "reconectar", não como falha.

## 4. Envio pra número que não existe passa CALADO — *a mais cara das armadilhas*

O WhatsApp **aceita e confirma** o envio pra um JID inexistente. O script
imprime "enviado", o exit code é 0, e a mensagem simplesmente não chega. Não
há erro em lugar nenhum.

Foi o que aconteceu no primeiro teste: o número foi passado com o nono dígito
(55 + DDD + 9 + oito dígitos), mas a conta estava registrada no WhatsApp
**sem o nono dígito** (55 + DDD + oito dígitos). Muito número brasileiro antigo
é assim — o "9" extra existe pra telefonia, não no registro do WhatsApp.

**Regra: todo destino é validado antes do envio.**

- Número (1:1): `sock.onWhatsApp(numero)` → checar `exists`.
- Grupo (`@g.us`): `sock.groupMetadata(jid)` — se o JID estiver errado, erra
  aqui em vez de sumir depois.

O JID real da conta pareada está no `creds.json` da pasta de sessão, campo
`me.id`. É a fonte de verdade pro próprio número — não confiar no que a pessoa
digita.

## 5. Sair rápido demais corta a mensagem

`sendMessage()` resolve quando o nó é despachado, não quando o servidor
confirma. Fechar o socket ou chamar `process.exit()` na sequência pode cortar
o flush. **Esperar ~3s depois do `sendMessage` antes de encerrar.**

Todo script de envio também precisa de **timeout de conexão** (60s no caso de
origem): sem ele, rede fora do ar trava a rotina agendada pra sempre, em vez de
falhar e reportar.

### 5.1 Imagem junto da mensagem — *VARIAÇÃO ISOLADA*

O script de envio do caso de origem aceita uma ou mais imagens e tem um modo de
prévia, que mostra o que sairia sem conectar. Uma imagem: o texto vai como
legenda. Várias: as imagens saem primeiro, sem legenda, com 1,5s entre elas, e o
texto por último, pra o link ficar embaixo, à vista. A miniatura é gerada pelo
Baileys com o `sharp`, que precisa estar instalado no projeto (no caso de origem
já vinha nas dependências). Primeiro uso: o anúncio de uma ferramenta nova num
grupo de cliente, com duas imagens.

Na mesma montagem ficou registrado que link sai **sem cartão de prévia** enquanto
o pacote `link-preview-js` não estiver instalado junto do Baileys.

### 5.2 Vídeo junto da mensagem — *VARIAÇÃO ISOLADA*

O caminho de documento do script de envio marcava tudo como `application/pdf`, e um mp4 mandado por
ele chegava quebrado. Por isso entrou uma opção que manda o mp4 como vídeo do WhatsApp (pode repetir).
Com um vídeo, o texto vai de legenda. Com vários, o texto vai antes, porque é ele que diz o que é cada
um, e os vídeos saem na ordem dos argumentos. Primeiro uso: dois clipes curtos num grupo de cliente,
com 1,5 e 2,6 MB, x264 a 720p e AAC. A saída do envio lista o grupo confirmado e cada vídeo. A
mensagem enviada não aparece na captura local (§7.3), porque a captura não grava o que sai do próprio
número: a prova é a saída do script.

## 6. Processo zumbi de tentativa anterior sabota a próxima

Uma versão inicial do script reconectava sozinha em `connection: 'close'`,
chamando `main()` de novo. Resultado: **várias conexões em paralelo**, todas
tentando registrar o mesmo número, derrubando umas às outras — e o processo
continuou vivo depois de a tentativa "terminar".

Duas consequências, as duas medidas:

1. Pareamento **não leva retry automático**. É operação one-shot, com o
   celular na mão.
2. Antes de tentar de novo, **matar o que sobrou**
   (`pkill -f <nome do script de pareamento>`) e conferir com `ps aux`.
   Tentativa nova concorrendo com processo velho falha sem explicar por quê.

## 7. Pairing code x QR — o QR é mais confiável

O pairing code (`requestPairingCode`) tem duas fragilidades: só pode ser
pedido **depois** que o socket termina o handshake (o sinal é o evento `qr`
em `connection.update` — pedir antes devolve `Connection Closed`), e expira
em cerca de um minuto, o que é pouco pro ciclo "gerar → entregar → digitar".

O **QR aguenta melhor**: rotaciona a cada ~20s mas o script regenera sozinho.
Como saída de terminal não chega confiável no usuário, o script de pareamento
grava o QR em **PNG** pra ser enviado como imagem. Mesmo assim: **gerar e
entregar na mesma janela** — QR de 2 minutos atrás já morreu.

Medido de novo (11/2026): a conexão fecha com status 408 uns 2,5 min depois de pedir o código. Pra parear de novo, guarde
a pasta da sessão antes e devolva na hora se expirar: enquanto o pareamento espera, nenhum outro script consegue enviar.
E duas conexões com a mesma sessão caem com `Stream Errored (conflict)`: não há trava entre processos, então nunca rode
dois scripts conectados ao mesmo tempo.
## 7.1 A agenda (nome dos contatos) não vem nesta sessão — medido no caso de origem

Pra mandar 1:1 pelo nome, um script de busca de contato pede ao WhatsApp a
agenda: o app state, que traz o nome salvo no celular, igual ao WhatsApp Web.
Com a sessão pareada umas seis semanas antes, as cinco coleções voltam e todas
falham com `failed to find key "..." to decode mutation`, e o script lê 0
contatos. As chaves do app state chegam só no pareamento, e a pasta de sessão
tem uma só, que não é a da agenda.

- Sem parear de novo, o número 1:1 vem de quem pediu o envio, **ou de um grupo em comum** (abaixo).
- Pareando de novo pelo QR (§7), as chaves chegam e o script deve passar a achar, mas isso ainda não foi testado.
- O grupo serve de atalho, em dois passos. Uma leitura anterior dizia que não, porque os metadados
  dele não trazem nome. *VARIAÇÃO ISOLADA (1 pessoa, num grupo da operação).*
  1. **Nome → LID, pelo log do grupo.** Toda mensagem gravada no log de grupo (§7.3) traz o nome que a
     pessoa usa e o participante. Em grupo no modo LID, o participante é `<número>@lid`, que não é
     telefone: a validação do §4 recusaria.
  2. **LID → telefone, pelos metadados do grupo.** No Baileys 6.7.24, `groupMetadata(grupo).participants`
     traz, pra cada um, `jid` (o telefone, tirado do `phone_number` que o servidor manda) e `lid`.
     Achado o participante pelo LID, o `jid` é o destino 1:1, e o `onWhatsApp` confirma antes do envio.
  - A leitura foi um script avulso. Ele conecta como o de envio, com a captura ligada, pra a fila que
    chegar nessa conexão não se perder (§7.2), lê os metadados e sai sem mandar nada.

## 7.2 Ler uma conversa: a fila fica semanas atrasada e só anda de 100 em 100 — medido no caso de origem

Pedido: ler o que o expert mandou no 1:1 com o dono do número na véspera (72 mensagens). Custou duas
rodadas perdidas antes de dar certo. O que foi medido:

- **A fila de pendentes do aparelho estava quatro semanas atrás.** Cada conexão rápida (envio, teste)
  recebe um lote só: o Baileys 6.7.24 pede `offline_batch` de 100 quando chega o `offline_preview` e
  não pede mais, e o servidor espera. Então cada conexão consome as 100 mais velhas da fila e mais
  nada. É isso que explicava um "0 mensagens recuperadas depois de 5 dias" anotado semanas antes: as
  100 que vieram eram de outros chats, mais antigas. A conclusão "reconectar não traz o que ficou pra
  trás" estava errada.
- **Pedindo lote atrás de lote** (mandar `offline_batch` de novo quando parar de chegar por 4 s), a
  fila andou as quatro semanas até o presente em 15 min: 160 lotes, cerca de 12.700 mensagens de todos
  os chats, e no fim veio o `CB:ib,,offline`.
- **O Baileys segura os eventos num buffer até a fila acabar.** Na primeira rodada o processo fechou
  aos 330 s com a fila pela metade e gravou zero mensagens. O que já tinha confirmação (ACK) e estava
  no buffer se perdeu pra este aparelho (no celular continua). Por isso `sock.ev.flush()` a cada segundo.
- **O que sai do celular do dono do número não decifra** ("No matching sessions found", "Over 2000
  messages into the future"): foram 2.600 falhas na fila, quase todas `fromMe`. O que os outros mandam
  decifra. Na prática, a resposta dele numa conversa não vem. Hipótese, não testada: parear de novo
  (§7) resolve.
  - **No dia seguinte, sem parear de novo: veio.** Numa captura da mesma conversa, as 7 mensagens dele
    (4 áudios, 3 textos) decifraram junto com as do expert. A conexão recomeçou três semanas atrás
    (reentrega do que não decifrou antes) e chegou ao presente em 8 min, 85 lotes. Não se sabe o que
    mudou. Com uma medição só, tratar "a resposta dele não vem" como "pode não vir" e conferir na
    saída do script.
  - **A libsignal tem mais duas linhas que imprimem a sessão inteira:** "Opening session:" e "Removing
    old closed session:". Passaram pelo filtro e caíram num log de captura (apagado na hora). Filtrar
    as duas também, com teste.
- **Seis dias depois: a "fila atrasada" é o que não decifra, e volta em toda conexão.** Primeira
  leitura de verdade de um grupo de suporte. Com a espera de 4 s por lote: 154 lotes, 8.943 mensagens,
  900 s e o fim da fila não veio, e a conexão seguinte recomeçou quase do mesmo ponto. Trocando a
  espera por 1,2 s e o lote por 300: **fila inteira em 146 s, 21 lotes, 4.452 mensagens, 3.981 sem
  decifrar** (2.624 do celular do dono do número, 1.357 de outras pessoas). O código do Baileys
  explica: chave que falta volta com NACK (`NACK_REASONS.ParsingError`), então o servidor entrega de
  novo; o resto dispara `sendRetryRequest`, até 5 vezes por mensagem, com um contador que só vive
  enquanto o processo vive, a 4 por segundo (`retryRequestDelayMs` 250). Leitura avulsa não faz mal.
  Numa rotina seriam centenas de pedidos de reenvio por leitura saindo do número pessoal do dono, e
  mensagem de gente de fora pode não abrir. Daí a regra: **rotina que lê WhatsApp só liga com a sessão
  pareada de novo** (§7). Hipótese, ainda não testada: aparelho novo começa com a fila vazia e as
  sessões limpas.
- **A libsignal imprime o registro da sessão com a chave privada** no console, a cada sessão que
  fecha. Log de qualquer script que fica conectado precisa filtrar isso.
- **Mídia de semanas atrás trava o download.** O CDN já apagou, e o `reuploadRequest` pede reenvio ao
  celular e espera sem prazo (travou 3 min no segundo arquivo). Por isso o prazo é de 45 s por arquivo,
  do mais novo pro mais velho. A mídia da véspera baixou toda (26 de 27).
- **Mensagem apagada** chega como `messageStubType` 1 (REVOKE), não como falha. **Edição** chega como
  `secretEncryptedMessage`, que o 6.7 não abre.

O caminho que funcionou, no caso de origem, é um script de captura de conversa (não vem no kit). Ele
grava cada 1:1 assim que chega (o bruto traz conversa pessoal de todo mundo, então vai pra pasta
temporária e é apagado depois), acha o alvo pelo nome de perfil, baixa as mídias e aceita rodar só as
mídias quando a conversa já está gravada. A transcrição sai de um Whisper local. **VARIAÇÃO ISOLADA**:
uma sessão, um número.

## 7.3 Grupo com arquivo: guardar a mensagem inteira, em qualquer conexão — *VARIAÇÃO ISOLADA*

Um grupo de pedidos de suporte recebe PDF, print e áudio. O log de texto guardava só "[arquivo: x.pdf]",
e o arquivo só baixa com a mensagem inteira, porque a chave da mídia vem nela. Como a fila é entregue
uma vez só, a qualquer script que conectar, o pedido que chegasse na conexão de envio de outra rotina
não teria mais como baixar.

O que mudou na biblioteca de captura do caso de origem, e vale pra todo script que conecta:
- **Grupo marcado como "com mídia"** (JID → pasta) é gravado inteiro (WebMessageInfo com `BufferJSON`)
  na pasta dele: um `mensagens.jsonl` e uma pasta `midia/`. Esse grupo fica fora do log de texto comum,
  pra o dado do aluno morar num lugar só.
- **O buffer de eventos é solto a cada segundo, ao fechar a conexão e na saída do processo.** Antes, o
  script de envio saía 3 s depois de mandar, e o que estava no buffer, já confirmado ao servidor, nunca
  era gravado (o mesmo mecanismo dos 330 s perdidos no §7.2).
- **O filtro da libsignal mora na biblioteca**, então vale também pra saída do envio que cai no log de
  uma rotina.
- Mensagem que não decifra vai pra um arquivo de falhas da pasta, sem conteúdo. Só o stub 2 (CIPHERTEXT)
  é falha: criar grupo (20) e promover alguém (29) também chegam sem conteúdo, e na primeira leitura
  pareciam "mensagens que não abriram".

A leitura da rotina conecta sem ficar online e pede lote atrás de lote até a fila acabar. Depois baixa
o que falta da pasta inteira, do mais novo pro mais velho, com 45 s e 3 tentativas por arquivo; arquivo
com mais de 14 dias fica pra trás. Uma trava impede duas leituras ao mesmo tempo. O envio ganhou uma
opção de mandar outras mensagens de texto na mesma conexão, depois da principal, e a listagem de grupos,
que era o último script conectando sem a captura, passou a usar a captura e a aceitar um trecho do nome,
pra não despejar a lista inteira dos grupos do número.

## 8. Segurança da sessão

A pasta de sessão do Baileys são credenciais completas: quem tiver aqueles
arquivos manda mensagem **como o dono do número**, sem senha e sem 2FA. Vai no
`.gitignore` junto com `node_modules/`. Nunca versionar, nunca subir pra
nuvem (Drive e afins), nunca copiar pra outra máquina "só pra testar".

Pra revogar: no celular, WhatsApp → Aparelhos conectados → desconectar o
aparelho "Mac OS" (ou o nome com que a sessão aparece ali). A sessão morre na
hora e a pasta de sessão vira lixo.

## 9. Em aberto

- **Durabilidade da sessão não medida.** Não se sabe quanto tempo ela dura
  sem reparear. Se o relatório parar de sair, a primeira hipótese é sessão
  caída — o script reporta isso em vez de tentar parear sozinho.
- **Risco de ban não observado.** Nenhum bloqueio até agora, mas o volume é
  de uma mensagem por dia. Não extrapolar pra disparo em massa.
- **Duas conexões ao mesmo tempo se derrubam.** No caso de origem, a rotina que lê um grupo e a que
  envia rodam em minutos desencontrados de propósito (uma aos :15 e :45, a outra aos :00 e :30). Só que
  não há trava entre o envio e a leitura. Se as duas conexões se cruzarem, a leitura sai com erro e o
  que já chegou fica gravado.
- **Só uma máquina, um número.** Rodar em servidor exigiria mover a pasta de
  sessão pra lá — não testado quando este arquivo foi escrito, e com o custo
  de a sessão viver fora da máquina do dono. Depois, a casa passou a operação
  pra um computador que fica sempre ligado: a sessão foi pra lá e a da máquina
  antiga foi desativada, porque duas máquinas com a mesma sessão brigam pela
  conexão (o mesmo efeito do §6). A sessão vive numa máquina só.
