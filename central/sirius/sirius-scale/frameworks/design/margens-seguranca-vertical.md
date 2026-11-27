# Margens de segurança — formato vertical (Reels / Stories)

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** técnica de plataforma
> **Alcance:** UNIVERSAL — é a UI do Instagram/Meta cobrindo a arte, não
> preferência de cliente. Vale pra qualquer cliente e qualquer negócio.
> Revalidar quando a Meta mudar a interface (os números vêm de um teste
> empírico feito pela casa numa conta real, antes da primeira versão deste kit).

⚠️ **Zona segura não é zona livre de rosto.** Este arquivo diz o que a **UI da
plataforma** cobre. Em vídeo de expert falando, o **enquadramento** impõe uma
segunda restrição, que não está aqui: uma peça inteira posicionada só por estes
números pôs texto em cima da boca do expert e custou 3 renders. Antes de
posicionar texto em vídeo, ler também
`sirius-scale/frameworks/copy/mapa-de-edicao-vsl.md` §4.1 — as duas restrições
se somam.

> Reusável pra qualquer cliente. Vale pra Reels, Stories e edição de vídeo
> vertical. **Não se aplica** a post estático de feed (1080x1080 ou 1080x1350)
> — lá não tem UI sobreposta cobrindo a arte, então o
> `sirius-scale/frameworks/copy/criativos-venda-ingresso.md` e os primeiros
> criativos de teste do caso de origem não precisaram dessa margem.

## Fonte

- **Primária:** imagem de teste empírico feita numa conta real (print enviado
  pelo Rodrigo) — números validados na prática, não é só spec teórica.
- **Complementar:** busca na web, no mesmo ano do teste, sobre safe zones de
  Reels, pra cruzar ordem de grandeza. Ver Fontes no fim.

## Canvas

**1080 × 1920px** (proporção 9:16) é o tamanho de exportação padrão, sempre
o mesmo independente de onde a peça vai ser vista depois.

## Altura visível por contexto (dado do teste real)

O mesmo vídeo de 1920px de altura mostra uma fatia diferente dependendo de
onde é exibido. Isso significa: **elemento importante fora da fatia mais
apertada (linha "com legenda") pode não aparecer** dependendo de como o
espectador está vendo.

| Onde é exibido | Altura visível | Cortado (topo+base) |
|---|---|---|
| Reels, sem legenda | 1465px | 455px |
| Reels, **com legenda** (pior caso) | **1330px** | **590px** |
| Exibido no Feed (fora da aba Reels) | 1350px | 570px |
| Capa/thumbnail na bio (grade do perfil) | 1080px (quadrado, centralizado) | resto todo |

## Caso medido: o end card de um criativo de vídeo do caso-base

O end card do kit de vídeo vertical do caso-base tinha o logo em `top: 1560px`.
Com 520px de largura o logo tem 186px de altura, então ele terminava em
**1746px** — 121px **fora** da zona de 1330px central (que vai de 295 a 1625).

Ninguém tinha visto porque **no arquivo cheio ele aparece inteiro**: o corte só
existe no player. Foi o Rodrigo que percebeu olhando a peça pronta ("a logo está
muito lá embaixo, depende do posicionamento pode ser que corta").

📌 **Como conferir sem depender de olhar:** desenhar as duas linhas da zona
segura no próprio frame antes de aprovar —

```bash
ffmpeg -ss <t> -i <peça>.mp4 -frames:v 1 \
  -vf "drawbox=0:295:1080:3:red@0.9:t=fill,drawbox=0:1622:1080:3:red@0.9:t=fill" \
  -y /tmp/zona.png
```

Elemento que cruza a linha não está na peça — está no arquivo. Layout corrigido:
bloco 560, CTA 940, seta 1120, logo 1300 (termina em 1486, 139px de folga).

## Regra prática de uso

1. **Zona seguro-garantido: os 1330px centrais do canvas de 1920px.**
   Qualquer texto, rosto, logo ou CTA essencial tem que caber aí — é o pior
   caso real testado (Reels com legenda ligada, que é o mais comum).
2. **Zona da capa/bio: quadrado central de 1080×1080.** Se a peça também vai
   servir de capa de perfil ou preview, o elemento mais importante (rosto,
   headline principal) precisa estar centralizado dentro desse quadrado, não
   só dentro da faixa de 1330px.
3. **Coluna direita reservada.** Like, comentário, compartilhar, salvar e o
   avatar do perfil ficam empilhados na lateral direita, por cima do vídeo.
   Não confirmado com teste próprio (não estava na imagem), mas é padrão
   conhecido da interface — reservar ~120–150px da borda direita livre de
   texto/CTA, e não confiar só nisso sem checar visualmente.
4. **Fundo pode ir de ponta a ponta (1080×1920).** A restrição é só de
   elemento crítico (texto, rosto, CTA), não da arte de fundo.

## Onde a margem "some" (topo vs base)

O teste enviado não separa quanto é cortado em cima e quanto embaixo —
só dá o total. Fontes da web (não testadas por nós, usar como estimativa,
não como número cravado) sugerem que o corte de baixo é maior que o de
cima, coerente com legenda + ícones + player ficarem concentrados na parte
inferior:

- Topo: por volta de 220–290px reservado pra UI superior.
- Base: por volta de 320–480px reservado pra legenda, ícones, barra de
  áudio/progresso.

Como o teste próprio já dá o total confiável (590px no pior caso), usar essa
estimativa de distribuição só quando for necessário decidir se um elemento
específico deve ir mais pra cima ou mais pra baixo dentro da margem de
corte — não como substituto do número testado.

## Lição de prompt: não inflar a margem "pra garantir"

Testado com geração de imagem via IA (prompt completo, texto embutido), no
mesmo dia do teste de margem: pedir margem de segurança MAIOR que a testada
(ex: 400px topo / 700px base, em vez dos ~290/~340 reais) não deixa a peça
"mais segura" — deixa a peça com barra vazia grande em cima e embaixo, sem
graça, porque o modelo tende a respeitar literalmente a margem pedida em vez
de preencher com conteúdo. **Usar os números reais testados (290/340, total
630px), não arredondar pra cima "por precaução".** E pedir explicitamente que
o fundo/foto preencha a tela inteira (y=0 a y=1920) mesmo dentro da margem —
só o texto/UI fica de fora dela, a arte de fundo não.

## Aplicação no `designer`

- Ao montar SVG/arte pra Reels ou Story, definir o `viewBox` em 1080×1920,
  mas manter headline, rosto e CTA dentro de uma faixa central de
  aproximadamente 1080×1330 (verticalmente centralizada).
- Se a mesma peça também for usada como capa/thumbnail, checar que o
  elemento principal sobrevive num crop quadrado 1080×1080 centralizado.
- Isso vale também pra roteiro de vídeo e edição: enquadramento de rosto e
  legenda embutida (burned-in) tem que respeitar a mesma faixa.

## Imagem gerada por IA joga texto pra fora da faixa — *VARIAÇÃO ISOLADA (2 ocorrências, 1 cliente)*

O gpt-image-2 põe o nome colado no topo e a data colada na base de um story
1080×1920, justo na área que a interface do Instagram cobre — mesmo com a
margem pedida no prompt. Aconteceu duas vezes no caso-base, com dois dias de
diferença: em três peças de um lançamento pago e em duas das direções de
identidade visual de uma Black.
O que resolveu, as duas vezes: **pedir todo o texto num bloco só** e, se
ainda sobrar, **descer a peça inteira alguns pixels** sem redesenhar.
Conferir a faixa em pixel depois de gerar, nunca confiar no prompt. Sobe pra
CONSISTENTE na terceira ocorrência — e aí vale virar checagem no portão do
designer.

Outro defeito visto na mesma rodada da Black: **ornamento assimétrico** — a
linha de enfeite de um lado do texto contínua e do outro tracejada. A
auditoria de "texto inventado" não pega isso; olhar os enfeites também.

## Story de anúncio: o botão da Meta cobre os 20% de baixo — *VARIAÇÃO ISOLADA (1 caso, um segundo expert)*

A faixa de 295 a 1625 desta página vem do Reels com legenda. No story **de anúncio**, a Meta põe o
perfil e o "Patrocinado" nos ~14% de cima e o botão do anúncio (Saiba mais) nos ~20% de baixo. Então o
texto da arte acaba em **y 1536**, não em 1625. Os 14% e 20% vieram como orientação da Meta pra anúncio
de Stories; não foram medidos com print próprio.

O caso: nos estáticos da Black de um segundo expert, o botão desenhado na arte terminava em y 1602.
Estava dentro da faixa de 1625 e passou no portão. Quem cuidava do projeto viu no story que as
informações pediam outra distribuição. Na versão seguinte o bloco termina em 1532, com 65 px entre logo,
frase e data e 32 px entre data e botão, e a cena se ajusta em cima. O portão dessa versão usa y 295 a
1536 no story e reprova botão abaixo disso, com um caso de teste que prova.

Regra prática: story que vai rodar como anúncio usa o limite de baixo em 1536. Os 20% de baixo ficam só
com fundo (cena ou degradê), sem texto, logo ou botão desenhado.

## Pontos em aberto

- Distribuição exata topo/base não testada por nós, só estimada por fonte
  externa.
- Coluna de ícones à direita não veio no teste enviado — vale confirmar com
  teste próprio antes de tratar como regra dura.
- Números podem mudar se o Instagram alterar a interface — vale re-testar
  periodicamente em vez de tratar como constante permanente.

## Fontes (busca web, no ano do teste, cruzamento de ordem de grandeza)

- [Zeely AI — Instagram safe zones explained](https://zeely.ai/blog/master-instagram-safe-zones/)
- [Outfy — Instagram Safe Zone Guide: Sizes & Best Practices](https://www.outfy.com/blog/instagram-safe-zone/)
- [Kreatli — Instagram Reels Safe Zone Guide](https://kreatli.com/guides/instagram-reels-safe-zone)
