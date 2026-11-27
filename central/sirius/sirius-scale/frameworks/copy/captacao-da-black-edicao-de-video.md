# Framework — Edição do vídeo de captação da Black

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

Reverse-engineered da edição dos 13 vídeos de captação de uma Black do caso-base (uma Black de colheita de base de um expert de educação), feita em seis dias, com as correções do Rodrigo e os pedidos da gerente de operação. É um dos arquivos dos criativos de captação da Black; a entrada é `sirius-scale/frameworks/copy/criativos-captacao-da-black.md`.

> **Alcance: NÃO TESTADO FORA.** A base é 1 cliente, 1 lançamento e uma leva de 13 vídeos, feitos a partir de 3 peças-mãe.
> - Sete estão ligados na Meta, e seis rodam também no Google (entrada, §1).
> - Retenção e ThruPlay não foram medidos (§8).
>
> **Onde mora o resto:**
> - O que o expert fala: `sirius-scale/frameworks/copy/captacao-da-black-roteiro-de-video.md`.
> - A receita de edição da casa (números aprovados no 4K, master em 2 passos, CTA como módulo solto): `sirius-scale/frameworks/copy/edicao-video-receita.md`.
> - As armadilhas técnicas desta leva (câmera, recorte, som, troca de final, portões de conferência): no registro interno de vídeo do caso de origem (não faz parte deste kit). As que mudam decisão de edição estão nos §2, §4 e §5 daqui.
> - O gosto aprovado do kit vertical do caso-base (o "arquivo de gosto": o padrão visual escrito, com o que o Rodrigo aprovou e reprovou, com o motivo): fica no caso de origem (não faz parte deste kit).
> - As falas citadas aqui: no registro de falas dos criativos de captação do caso-base.
> - **Ferramentas:** a leva foi feita com HyperFrames (composição de vídeo em HTML/GSAP) e ffmpeg, ferramentas externas que instalam à parte. Quem edita no CapCut ou com editor humano usa as regras daqui, não os comandos.

## 1. Escopo e base de evidência

### Fontes

- **Fonte A: o projeto de vídeo da leva:**
  - o mapa do projeto, com os brutos, as famílias e as rodadas;
  - as notas de edição de cada família, com os números de cada uma e as escolhas do editor;
  - o relatório da rodada 3;
  - mais dois projetos de troca de final (final C).
- **Fonte B: as correções do Rodrigo no chat** (do 1º ao 6º dia da edição) e **os pedidos da gerente de operação** em duas tarefas, no registro de falas dos criativos.
- **Fonte C: o resultado dos primeiros seis dias de veiculação**, na análise de desempenho dos criativos de captação da Black.

### Excluído de propósito

- **O manifesto de antecipação:** é outra fase. As lições dele ficaram no registro interno de vídeo do caso de origem.
- **O roteiro** (o que o expert fala): tem arquivo próprio.
- **Os cortes de live, os reels de conteúdo e as aulas:** são outros artefatos.

### Ressalva estrutural da base

As 13 peças saíram de três peças-mãe (A1, T2 e T4), uma por família. "13 de 13" quer dizer que a escolha da mãe foi copiada. As rodadas de correção estão registradas no caso de origem como VARIAÇÃO ISOLADA, sem veredito final do Rodrigo, e é assim que ficam aqui. A marcação de força segue a da entrada (§1).

## 2. O que é fixo nas 13 peças · a data por insert e o cartão de bônus são decisões do Rodrigo (VARIAÇÃO ISOLADA); o resto é PADRÃO CONSISTENTE (proposto)

**Decisões dele:**
- **A data por insert.**
  - Os brutos foram gravados falando a data antiga da live de abertura, que mudou depois da gravação.
  - Um cartão de data cobre a frase gravada e leva o áudio novo do expert, no formato DIA DA SEMANA · DATA · HORA. O cartão dura o que a frase nova dura.
  - A decisão é do 1º dia da edição: "pode editar com o audio original mas fazer um insert na tela pra amanha a gente sobrepor com um audio novo dela".
- **O cartão VÁRIOS BÔNUS ESPECIAIS em ouro no final**, desde a rodada 3. Saiu da fala do Rodrigo no 4º dia: "vamos colocar na legenda e nos estaticos quando der".

**O que veio das peças-mãe:**
- **Formato:** 9:16, 1080×1920, 30 quadros por segundo, de 92,9 a 138,4 s, mais uma cópia leve de menos de 28 MB pro celular.
- **A marca na fala:** a pílula do logo aparece quando o expert diz o nome da Black, e um cartão com o símbolo e a palavra-chave do nome da Black aparece quando ele diz essa palavra.
- **A legenda muda com a família:**
  - Nas famílias 1 e 3 (9 peças), é kinetic em HTML, palavra por palavra, com ouro no lugar do cyan do kit, borda de 8 direções no glifo, entre x 100 e x 940, e corpo de pelo menos 64 px.
  - Na família 2 (4 peças), todo texto vai em caixa no estilo Classic do Instagram (Albert Sans 800), e o título abre grande no peito do expert e vira a legenda (evidência no caso de origem).
  - Nas duas, a legenda segue a fala ("e-books"), e os cartões seguem a regra escrita ("livro digital").
- **O fecho:** o logo vertical se monta, vem o botão SAIBA MAIS, e o acorde final da trilha cai no logo.
- **O som:**
  - uma trilha diferente por peça (Mixkit, licença conferida);
  - de 17 a 21 dB abaixo da voz na faixa que o celular toca, de 300 Hz a 4 kHz;
  - sem ducking.

**Por quê:** a legenda e o som seguem o kit vertical do caso-base, que é o que o Rodrigo já tinha aprovado (evidência no caso de origem).

## 3. Três famílias de layout — variar o formato é decisão do Rodrigo (2º dia da edição) · VARIAÇÃO ISOLADA; cada família também é VARIAÇÃO ISOLADA

O pedido veio quando ele aprovou a A1 como peça-mãe: "pode soltar a leva. mas nao seria bom dar uma variada nos formatos? pra nao ficar tudo igualzinho?"

| | Família 1: faixa em cima | Família 2: nativo do Instagram | Família 3: quadro com conteúdo |
|---|---|---|---|
| Peças | A1 (mãe), A2, A3, N6 | T2 (mãe), T3, N5, A4 | T4 (mãe), T1, A5, N4, T5 |
| Tela | faixa da Black de 0 a 480 com a headline, e o expert numa janela 3:4 até o pé | o expert em tela cheia, com o texto em caixas no estilo Classic | o expert em janela de largura inteira com zoom de 1,4×, e o conteúdo em placa curta por cena |
| Headline | o título do roteiro, com uma palavra em ouro, até o fecho | abre grande no peito e vira a legenda; sem headline fixa | em cima; no T5, só o logo |

Fontes: evidência no caso de origem (uma seção por família no registro de vídeo, mais a da família 3 com zoom).

**Por quê:** o motivo dado por ele foi não deixar tudo igual. Cada família é um jeito de pôr texto na tela sem tapar o rosto, partindo de um bruto deitado (1920×1080).

**Variações aceitáveis:** a família 3 nasceu com o expert num quadro 16:9 pequeno, foi reprovada e refeita com zoom (§4).

**Família 2 sem headline fixa** foi escolha do editor, registrada por ele nas notas da leva como decisão a conferir. O arquivo de gosto do kit vertical diz o contrário: a headline fixa fica o vídeo inteiro no vertical, porque é o que o Rodrigo testa em A/B (nas palavras dele: "mesmo vídeo, headlines diferentes, sempre dá diferença"). A divergência está no §10.

## 4. As correções do Rodrigo e o que mudou — decisões com data · VARIAÇÃO ISOLADA (uma leva); a regra que tiro de cada uma é PADRÃO INCONCLUSIVO, proposta minha a confirmar

| Quando | O que ele disse | O que mudou na leva | Regra que tiro disso (hipótese, a confirmar) |
|---|---|---|---|
| 3º dia | "[…] mandou todos os áudios para a gente substituir os criativos. Pode fazer essa edição." | As seis notas de voz do celular foram tratadas pra soar como a lapela e trocadas nas 13 | voz nova colada em fala gravada se trata até casar com a lapela |
| 4º dia | "O segundo eu achei que é música está competindo com a voz dela." | Trilha mais baixa e sem bateria na frente da voz; outra faixa quando não resolve | a trilha não briga com a voz |
| 4º dia | "Essas que você deixou ela pequena, cortada, eu não sei se é uma boa. Você viu alguma referência? Porque senão acho que a gente tem que fazer com zoom." | Família 3 refeita: o expert em largura inteira, a 1,4×, com o rosto de cerca de 245 pra cerca de 341 px. Ele confirmou: "faz todos com zoom, gostei do primeiro" | pessoa em vídeo vertical vai grande |
| 4º dia | "Essa musica de fundo é muito triste, tem que ser mais animada" | Trilhas trocadas por um índice de animação e alegria; em volta do cartão da data, as pausas encurtaram de 0,29–0,59 s pra 0,13–0,32 s (o "lento" era pausa) | trilha de captação é animada |
| 4º dia | "o quadrado é legal, mas toda hora aparecendo fica massivo." | Rodada 3: a placa escura fixa saiu; ficou placa curta, uma por cena, pelo tempo de ler | placa escura só quando precisa |
| 4º dia | "Eu acho que a gente pode manter o insert diferente como se fosse a legenda. Mas daí, nesses casos, não precisaria ter esse quadro escuro no fundo. Pode aplicar essa lógica sempre que possível." | O texto que repete a fala virou legenda em destaque, maior e sem placa. A legenda repetindo texto da tela foi de 31,8–66,0 s por peça pra 0 na família 3, e de até 13,7 s pra 0 nas outras | legenda e texto na tela nunca dizem a mesma coisa ao mesmo tempo |
| 4º dia | "esse primeiro nao fica estranho comecando com o banner?" | O T1 passou a abrir no expert falando, e o cartão da data vem depois | a peça abre na pessoa, não no cartão |
| 4º dia | "vamos colocar na legenda e nos estaticos quando der" (os bônus especiais) | O cartão VÁRIOS BÔNUS ESPECIAIS em ouro entrou no final das 13 | o bônus aparece escrito na tela, uma vez |
| 5º dia | "T1, corte a palavra" (o "gente" do início); "N4 coloca ? no final da headline"; "T5 nao gostei da headline, troca para somente a logo da black" | Rodada 3b, peça a peça | ajuste fino, sem regra nova |
| 5º dia | "no inicio do T4 parece que voz dela falha ou abaixa rapidamente o volume em algumas palavras" | Era o corte de 30 ms derrubando a cauda soprada do fim da frase. O fade passou a acompanhar a cauda | a emenda de voz se mede na cauda (evidência no caso de origem) |

As falas inteiras, as medidas de cada rodada e o relatório da rodada 3 ficam no caso de origem.

## 5. Os finais na edição — VARIAÇÃO ISOLADA; trocar o final sem mexer no corpo confirma a receita da casa

- **O final B (Saiba mais)** está colado nos 13.
- **O final C (comenta BLACK)** existe pra T2, T1, T3, T4 e T5, no orgânico. A T3, a T4 e a T5 saíram cerca de duas semanas depois da leva. A T4 e a T5 saíram sem a composição da leva: a imagem do final veio da irmã aprovada da mesma família, trocando só a faixa de cima, e o som foi remontado com as partes originais (evidência no caso de origem). A irmã certa é a da mesma família, não a citada no pedido. Os dois primeiros foram pedidos pela gerente de operação, em duas tarefas:
  - "Troque somente a parte final, após o banner (perto do tempo 1:35) e encaixe e edite a partir do "comente Black..." do vídeo Final C (perto do tempo 0:08)";
  - "Adaptado para o final C, pedindo pra digitar Black. Seguir como foi feita a adaptação do T2 na tarefa anterior".

  O corpo é copiado sem reencodar, e só o trecho depois do cartão é refeito (evidência no caso de origem).
- **O final A (link do perfil)** nunca foi editado.

**Isso confirma uma regra que já existia.** A receita de edição tem o CTA como módulo solto (`sirius-scale/frameworks/copy/edicao-video-receita.md` §3.3, decisão do Rodrigo): "Assim troca-se o CTA sem reprocessar o corpo." A Black é mais uma aplicação.

## 6. O 16:9 pro YouTube — o pedido é decisão do Rodrigo (6º dia da edição); o molde é VARIAÇÃO ISOLADA, sem aprovação

O pedido: "Talvez para o YouTube nem precisa aparecer uma headline fixa. Dá para deixar só a legenda com motion bem feita. E se, caso apareça a headline, pode colocar no começo, por alguns segundos, depois ela desaparece." E: "Mas sempre centralizado, de uma forma assim, nem que seja na frente dela."

**O molde, feito na mesma noite pra peça-mãe T4** (evidência no caso de origem):
- o bruto inteiro, sem recortar o vertical;
- a assinatura e um logo queimados no bruto, apagados por inpaint;
- legenda de 64 px, palavra por palavra;
- headline só de abertura, centralizada, e só quando ela é a primeira frase falada;
- as cenas num painel escuro à direita, com o vídeo e a legenda indo 400 px pra esquerda juntos.

**Estado no dia do registro (seis dias depois do molde):**
- Os 13 estão prontos no disco.
- Não estão na nuvem nem nos anúncios.
- Não achei o ok do Rodrigo no visual.

**Duas divergências com regras da casa, sem decisão (§10):**
- A receita do 16:9 pede a legenda em frase inteira: "**frase inteira**, 1–2 linhas" (`sirius-scale/frameworks/copy/edicao-video-receita.md` §3.10). O kit vertical do caso-base tem um 16:9 de hipótese com legenda kinetic, que é palavra por palavra (no arquivo de gosto). Receita e kit divergem no 16:9, como no contorno (§10, item 4), e a Black seguiu o kit.
- O kit registra que a coluna de texto à esquerda foi reprovada no 16:9 de um lançamento anterior. A Black abre um painel à direita. Não sei se o Rodrigo leria os dois como o mesmo layout.

## 7. O defeito que passou por todos os portões — VARIAÇÃO ISOLADA (1 família)

O cartão do final da família 2 (T2, T3, N5 e A4) mostra VÁRIOS BÔNUS sem ESPECIAIS. O T2 e o N5 estão ligados; o T3 e o A4 são reserva. A conferência no quadro do arquivo entregue (o da nuvem) mostrou que o ESPECIAIS nunca aparece (evidência no caso de origem). Era um seletor que não alcançava a segunda linha do cartão. A família 3 não tem o defeito.

**Por que passou:** os portões da rodada 3 leem o áudio (whisper) e medem o layout. Nenhum confere o texto desenhado na tela contra a copy aprovada. Isso dá pra virar checagem automática — é regra da casa perguntar, a cada aprendizado, se ele vira checagem que roda sozinha —, e a proposta está no §10.

## 8. O que o resultado mostrou sobre a edição — PADRÃO INCONCLUSIVO

Fonte C, nos primeiros seis dias de veiculação.
- **A família de layout não se separa do resto.** Cada família carrega ângulo, público e dia de entrada diferentes, e a família 2 é, em três das quatro unidades em que roda, só o T2.
- **A duração pode pesar na entrega, mas isso é hipótese.** O T1, o vídeo mais longo (138 s), levou 3,0% do gasto de não aluno na Meta e 33,7% no Google.
- **Retenção e ThruPlay por vídeo não foram medidos.** Nenhuma decisão de edição (legenda, família, final) está ligada a comportamento de quem assiste. A casa já registrou que retenção pode andar ao contrário da venda (num caso medido, o criativo de melhor retenção foi o 4º em venda).

## 9. O que é reutilizável e o que é do caso

**Tende a transferir.** É hipótese até rodar fora.
- A data por insert, quando a data muda depois da gravação.
- Os finais gravados à parte e trocados sem reencodar o corpo.
- Variar o layout entre os vídeos da leva.
- As regras tiradas das correções (§4), quando forem aprovadas:
  - pessoa grande no vertical;
  - trilha animada e abaixo da voz na faixa do celular;
  - texto na tela que não repete a legenda;
  - placa escura curta;
  - a peça abre na pessoa.

**É do caso:**
- O kit vertical do caso-base, o símbolo do nome da Black e a paleta dela.
- Os números de recorte, que são do bruto 1920×1080 com a cabeça a 14% do topo.

## 10. Pontos em aberto

1. **O cartão sem ESPECIAIS na família 2** está em dois vídeos ligados (o T2 e o N5). A decisão de consertar ficou aberta desde que o defeito foi achado, cinco dias depois da subida.
2. **Checagem proposta pro defeito do item 1.** Ler o texto do cartão final no quadro do arquivo entregue e comparar com a copy aprovada, no mesmo desenho da checagem de texto na tela da rodada 3 (que abre a composição sem renderizar e registra cada texto visível) ou por OCR. Não foi construída.
3. **O 16:9 não tem o ok do Rodrigo e não subiu.** Também não está decidido como ele entra no anúncio do Google que já está no ar. A legenda palavra por palavra e o painel à direita divergem de regras da casa (§6).
4. **Dois documentos da casa dizem coisas diferentes sobre o contorno da legenda no vertical.**
   - A receita (legenda queimada em libass no 4K, números aprovados na primeira leva de criativos) manda `Outline: 0`: "Contorno preto é o que dava cara amadora — não usar."
   - O kit vertical do caso-base (no arquivo de gosto: legenda kinetic em HTML, aprovada num lançamento anterior) manda borda de 8 direções no glifo.
   - A Black seguiu o kit nas famílias 1 e 3. As duas são tipos de legenda diferentes, mas nenhum dos dois arquivos diz isso. Qual vira a regra geral é decisão do Rodrigo; nenhum dos dois foi mudado.
5. **A família 2 ficou sem headline fixa**, por escolha do editor, contra a headline fixa do kit (arquivo de gosto). Sem veredito do Rodrigo.
6. **A headline da família 3 e o selo da família 2 começam em y 200.**
   - É o que o kit manda: o Rodrigo escolheu o 200 e reprovou o 295 num lançamento anterior ("muito espaço em cima, pouco embaixo").
   - O `sirius-scale/frameworks/design/margens-seguranca-vertical.md` põe o topo da zona segura do 9:16 (Reels com legenda, o pior caso) em 295. No pior caso, a primeira linha que começa em 200 pode ser cortada (evidência no caso de origem).
   - São duas regras da casa em conflito. A decisão é do Rodrigo.
7. **Retenção, ThruPlay e posicionamento por vídeo** não foram medidos (§8).
8. **Outro cliente:** ao aplicar em outro cliente (vocês incluídos), sinalizar na entrega que a base é de um cliente só (`sirius-scale/REGRAS.md` §4).
