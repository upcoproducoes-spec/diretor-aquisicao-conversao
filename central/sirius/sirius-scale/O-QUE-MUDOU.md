# O que mudou

Cada versão diz o que trocar, o que veio e se mexe em algum arquivo de vocês. A mais nova fica em
cima.

## v0.6 · 23/11/2026 · lançamento clássico de ponta a ponta, CPL reescrito e mais armadilhas de plataforma

**Pra atualizar:** peçam ao Claude, como está na seção 6 do `COMECE-AQUI.md`. Este zip traz só as peças da
Sirius Scale (`sirius-scale/`, `.claude/` e `COMECE-AQUI.md`). O resto é de vocês e fica como está.

Vai nesta versão:
1. **Lançamento clássico:** dois frameworks novos. O `lancamentos/lancamento-classico.md` traz o calendário em D± de
   ponta a ponta, as regras do carrinho, a ordem reabertura → downsell e com quantos dias de antecedência sai cada
   copy. O `lancamentos/live-de-domingo.md` traz a live de encerramento em 11 blocos, com o sorteio. O
   `lancamentos/cpl-3-aulas.md` foi reescrito: a ordem dos blocos de cada aula, o que já se repetiu em mais de um
   caso e as checagens antes de fechar a oferta. A Roma ganhou o "escovar" e o DSA. O agente `copy` já aponta pros
   arquivos novos.
2. **Tráfego:** a UTM fica num lugar só (o item 6 do `/preflight` procura o id no link e usa a tabela de UTM do Dash
   como prova), numeração de criativo em série por funil, o quente com um conjunto por degrau e rotação diária, e o
   teste vencedor sobe a verba junto com a pré-escala. A conferência do Google passou a comparar os canais do grupo
   com os da campanha de referência. Mais armadilhas de Meta, Google, Dash, Clarity e Hotmart: recompra pelo CPF e
   compra de teste que chega como venda.
3. **Copy e página:** o nome do lead no assunto do e-mail, aberturas curtas de VSL com uma ponte gravada uma vez só,
   e página sem cara de IA (manda o design system de vocês, com um item novo no `/revisar` de página).
4. **Design e vídeo:** a arte com cena gerada sem letra e o texto posto por código virou o padrão do `designer`,
   independente do gerador que vocês usam. Entraram 34 armadilhas novas de vídeo, a transição do corpo pro CTA que
   foi aprovada e a revisão de ISBN e ficha no impresso.
5. **Atualização pulando versão:** quem ficou em versão antiga recebe, junto, o "Nos arquivos de vocês" de cada
   versão que pulou.

Nos arquivos de vocês: nada muda.

## v0.5 · 16/11/2026 · pixel do anúncio, página na otimização e o que se aprendeu em duas semanas

**Pra atualizar:** peçam ao Claude, como está na seção 6 do `COMECE-AQUI.md`. Este zip traz só as peças da
Sirius Scale (`sirius-scale/`, `.claude/` e `COMECE-AQUI.md`). O resto é de vocês e fica como está.

Vai nesta versão:
1. **`/preflight` com 12 itens:** entram o anúncio que leva pra site sem o pixel no rastreio (anúncio de tráfego criado
   por API sai sem, e aí a Meta mostra zero de compra mesmo vendendo) e a queda na nota do pixel. O item de UTM passa a
   acusar id no lugar do nome.
2. **Otimização em quatro níveis:** a página entrou junto com orçamento, público e criativo, lida pelo Microsoft
   Clarity (`trafego/otimizacao-em-tres-niveis.md` §7.1), e o relatório passa a pedir criativo novo quando o funil fica
   com poucos no ar. O `webdesigner` põe a tag do Clarity em toda página e cuida do fim dela (redirecionar, nunca deixar
   a página aberta do jeito que foi divulgada).
3. **Lançamento gratuito:** rampa de verba na captação, um criativo por campanha em todos os degraus, os públicos
   quentes que entram e o quente em hierarquia (00, 01, 02), e como começar numa conta que já tem histórico: replicar o
   que vendeu e testar o resto em paralelo (`trafego/lancamento-gratuito.md` §2.1.1, §2.2 e §2.5).
4. **Armadilhas novas de plataforma:** Meta (UTM presa no criativo reaproveitado, público de site com `www`, erro 613,
   quatro leituras de insights que enganam), Dash (aba Remarketing só pela tela, limite por minuto, venda contestada
   contada como venda), Google (histórico de 30 dias), Full Funnels (dez fatos da montagem de fluxo, pré-cabeçalho
   duplicado, custo e falha do WhatsApp oficial), Cloudflare (duas falhas de segurança das Functions) e o radar das
   versões de API.
5. **Vídeo, design e copy:** 18 armadilhas de ffmpeg, HyperFrames e transcrição, a conferência de áudio e OCR, a
   revisão de livro com o expert, o portão dos estáticos em HTML, mais regras de e-mail, conteúdo, criativo, MQL,
   debriefing e organização do Drive.

Nos arquivos de vocês: nada muda. Quem quiser a página na otimização cria um projeto no Microsoft Clarity e passa o id
pro Claude anotar no `CLAUDE.md` de vocês.

## v0.4 · 05/11/2026 · o Claude sobe o vídeo do anúncio no Google

**Pra atualizar:** peçam ao Claude, como está na seção 6 do `COMECE-AQUI.md`. Este zip traz só as peças da
Sirius Scale (`sirius-scale/`, `.claude/` e `COMECE-AQUI.md`). O resto é de vocês e fica como está.

Vai nesta versão:
1. **Subida de vídeo no Google:** o comando `videos` do `subir_campanha.py` leva o arquivo até o YouTube pela
   própria conexão do Google Ads, sempre não listado, espera o processamento e grava o id no registro. Não precisa
   de chave do YouTube. O vídeo fica num canal do Google ligado à conta de anúncios, a não ser que o registro
   aponte o canal de vocês. Foi testado com um vídeo real no caso de origem; o caminho pro canal de vocês ainda
   não. O passo a passo está em `sirius-scale/ferramentas/google/LEIA-ME.md`.
2. **Windows:** o Git for Windows continua necessário, mas agora é o próprio Claude que instala, num comando só.
   Os agentes `video`, `designer` e `webdesigner` passam a aceitar também o PowerShell, pra não ficarem sem
   terminal, e a atualização instala o Git na hora, se faltar.

Nos arquivos de vocês: nada muda. Os registros de campanha que já existem continuam valendo. Só quem quiser que o
Claude suba o vídeo acrescenta o campo `arquivo` no criativo.

## v0.3 · 05/11/2026 · preflight, Google, vídeo e rotina de tráfego

**Pra atualizar:** peçam ao Claude, como está na seção 6 do `COMECE-AQUI.md`. Este zip traz só as peças da
Sirius Scale (`sirius-scale/`, `.claude/` e `COMECE-AQUI.md`). O resto é de vocês e fica como está.

Vai nesta versão:
1. **`/preflight`:** a saúde das contas virou comando próprio, com 10 itens lidos da Meta e do Google. Rodem
   antes de subir campanha. O `/revisar` e o `gestor-trafego` chamam ele sozinhos.
2. **Google Ads:** agora o Claude pode ler a conta direto e montar campanha pausada, como na Meta. O guia é
   `sirius-scale/instalacao/google-ads.md`, e as ferramentas estão em `sirius-scale/ferramentas/google/`. Pede
   credencial própria de vocês: façam com a consultoria. A montagem foi validada a seco, mas ainda não rodou de
   verdade em conta de cliente: na primeira campanha, confiram tudo na tela. Ligar continua com vocês.
3. **Edição de vídeo:** o guia `sirius-scale/instalacao/video.md` instala o HyperFrames. Com ele, o agente
   `video` monta a primeira versão aí mesmo. Sem ele, continua entregando o mapa de edição pro CapCut.
4. **Rotina de tráfego:** `sirius-scale/rotinas/trafego-diario.md` traz a tarefa agendada pronta. Lê o dia que
   fechou, roda o preflight, aplica a régua e deixa o relatório. Não aplica nada. Cobre lançamento; perpétuo
   ainda não. Foi testada à mão e nunca rodou agendada fora da casa, então a primeira semana é de conferência.
5. **Passo a passo de instalação:** `sirius-scale/instalacao/mac.md` e `windows.md`.
6. **Frameworks novos:** `trafego/otimizacao-em-tres-niveis.md` (orçamento, público e criativo, sempre os três),
   `trafego/radar-plataformas.md`, `copy/padrao-de-copy.md` (ficha do pedido e documento-padrão) e
   `operacao/nomenclatura-drive.md`.
7. **Frameworks atualizados:** perto de 30, entre eles Google, Meta, públicos, leitura do Dash, e-mail,
   WhatsApp, Black, low ticket e rotinas. O `email.md` agora manda assunto com a primeira letra maiúscula. Os
   exemplos que vinham de peça real viraram molde.
8. **Agentes e checagens:** `copy`, `video`, `designer`, `webdesigner` e `gestor-trafego` atualizados, e os
   checklists do `/revisar` também.
9. **Regras:** `sirius-scale/REGRAS.md` ganhou "dúvida de forma não trava" (§2), a escrita no Google e o cuidado
   com credenciais (§6).
10. **Uma versão só pra todos:** os arquivos da Sirius Scale não levam mais o nome do cliente. O contrato continua
    valendo como antes.

Ainda não vem: o agente de automação, pra montar e-mail e WhatsApp dentro do Full Funnels. Até lá, o `copy`
escreve os textos e vocês montam no Full Funnels.

O que não vai: os programas e as rotinas da operação de origem que dependem das contas e do servidor de lá. A
exceção são as ferramentas do Google, adaptadas pra rodar com as credenciais de vocês.

Nos arquivos de vocês: acrescentem no `CLAUDE.md`, na seção de ferramentas, o teto de verba combinado (por
campanha e, se houver, da conta). O `/preflight` confere o gasto contra ele; sem isso, o item 1 sai como não
verificado. Perguntem o valor a quem decide a verba, não preencham por suposição.

## v0.2 · 29/10/2026 · o sistema inteiro

**Pra atualizar:** peçam ao Claude, como está na seção 6 do `COMECE-AQUI.md`. Este zip traz só as
peças da Sirius Scale (`sirius-scale/`, `.claude/` e `COMECE-AQUI.md`). O resto é de vocês e fica
como está.

Vai nesta versão:
1. Agentes novos: `designer`, `webdesigner`, `gestor-trafego` e `video`. O `gestor-trafego` lê o
   Dash e a Meta, monta o pacote e, com a Meta conectada, monta a campanha pausada; ativar e mexer
   em verba é com vocês. O `copy` passou a cobrir todas as peças de texto.
2. Checagens: `/revisar` (que em tráfego começa pelo preflight: país, Advantage e idade),
   `/debriefing`, `/mapa-edicao` e `/pente-fino`.
3. Regras: `sirius-scale/REGRAS.md` ganhou a legenda completa de força e alcance (§4), a ordem de
   fechamento de peça grande (§5) e a escrita em plataforma (§6: na Meta, o Claude monta pausado e
   vocês ativam).
4. Frameworks, em `sirius-scale/frameworks/`:
   - **Oferta e lead:** LHTO (lead, história, tese e oferta), Arquitetura de Oferta em 14 seções e
     Great Leads.
   - **Tráfego:** metodologia, nomenclatura, lançamento gratuito, públicos e Advantage, MQL e
     qualificação, leitura do Dash Fácil, técnico de criação na Meta e no Google.
   - **Lançamento:** briefing, CPL de 3 aulas, lançamento pago (LPSG), aquecimento e lives, live de
     downsell, Black da casa, Black Friday, as peças de uma Black por fase, low ticket, perpétuo,
     produto de entrada, upsell e downsell, pós-compra e suporte, metas e base de faturamento,
     Roma e promessa, diagnóstico de operação, rotinas de lançamento e o prompt de debriefing.
   - **Copy:** criativos, criativos de venda de ingresso, e-mail, disparo de WhatsApp, produção de
     VSL, vídeo de upsell e formatação de roteiro, além dos cinco da Black que já estavam aqui.
   - **Vídeo:** receita de edição, edição de criativos, técnico de vídeo, mapa de edição (VSL e
     vídeo curto), edição da captação da Black e como medir uma peça de referência.
   - **Design:** arte do estático da Black, estático em HTML, margens de segurança no vertical,
     estilos de sticker do Instagram e material impresso.
   - **Base:** pesquisa e avatar, ficha do expert, conteúdo que alimenta o funil e como extrair
     framework do trabalho de vocês (pra `frameworks-da-casa/`).
   - **Técnico de plataforma:** Hotmart (configuração de produto e API), Full Funnels, WhatsApp por
     Baileys e páginas no Cloudflare e no WordPress.
5. Modelo em branco novo: `sirius-scale/modelos/desempenho.md`, pro funil perpétuo.
6. `COMECE-AQUI.md` novo: conexões (Dash Fácil e Meta pelo claude.ai), a atualização pedida ao
   Claude (sem apagar nada de vocês, pelo `atualizar.sh` que vem no zip e confere tudo antes) e o
   aviso da linha do `CLAUDE.md` que liga as regras.
7. Licença: os agentes no plural e a nota das metodologias de terceiros.

Ainda não vem: o agente de automação, pra montar e-mail e WhatsApp dentro do Full Funnels. Até lá,
o `copy` escreve os textos e vocês montam no Full Funnels.

O que não vai: os scripts e as rotinas automáticas da operação de origem, que dependem das contas e
do servidor de lá. Aqui os agentes fazem a mesma checagem conversando, e a leitura vem pelos
conectores.

Nos arquivos de vocês: nada nesta versão.

## v0.1 · 27/10/2026 · primeira instalação

Vai nesta versão:
1. Agente `copy`.
2. Skill `/humanizer`.
3. Frameworks da Black: captação (as regras de conteúdo, o roteiro de vídeo, o texto de anúncio e
   o texto do estático) e live de aquecimento.
4. Modelos em branco: DNA da expert, marca, produto, briefing, pesquisa, avatar e banco de
   ângulos.
