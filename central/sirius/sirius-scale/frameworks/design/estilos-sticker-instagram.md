# Estilos de sticker de texto do Instagram — referência pra headline de criativo

> Sirius Scale v0.6 · uso interno · licença em `sirius-scale/LICENCA.md`

> **Camada:** execução visual · **Base:** 7 peças de referência reais mandadas
> pelo Rodrigo (criativos de terceiros, coletados na timeline)
> **Confiança:** VARIAÇÃO ISOLADA — vale como catálogo de formato, e o que
> transfere é o *formato*, não a escolha de qual usar em cada peça.
> **Alcance:** UNIVERSAL na parte de mecânica (é comportamento da UI do
> Instagram, não preferência de cliente); NÃO TESTADO FORA na parte de qual
> estilo converte melhor — isso ninguém mediu ainda.

## Por que este arquivo existe

A primeira headline dos vídeos de remarketing do caso-base foi reprovada pelo
Rodrigo com o diagnóstico exato: *"a maneira que o Instagram junta as linhas
é diferente de como você faz, e não parece que é original"*. As 7 referências
chegaram no mesmo dia.

O erro não era fonte, cor nem posição — era **como as linhas se juntam**.

## A regra que faz parecer nativo (a que estava errada)

**As linhas formam UM BLOCO SÓ.** Cada linha tem a largura do próprio texto e
fica centralizada, mas os cantos **internos** — onde uma linha encosta na
outra — são **quadrados**. Só o contorno **externo** do conjunto é arredondado.

Desenhar raio nos 4 cantos de cada linha, mesmo com as linhas coladas, produz
o efeito de **três etiquetas empilhadas**. É isso que denuncia na hora que o
texto não saiu do app.

Como desenhar (o gerador de headline do caso de origem faz assim; o método
serve em qualquer ferramenta): desenha cada linha com raio nos 4 cantos e
depois preenche, entre linhas vizinhas, um retângulo na largura da interseção
horizontal e altura `±raio` em torno da fronteira. Os cantos internos somem;
os externos ficam.

Dois números que vieram junto, e que a receita antiga subestimava:
**raio 26** (a receita dizia 16) e **padding 34×18** (dizia 26×14). O sticker
do IG é mais "gordo" do que parece.

## Os 4 estilos do catálogo

| Estilo | O que é | Quando as referências usam |
|---|---|---|
| **branca** | Caixa branca, texto quase-preto (`#121212`), sans bold | O mais comum. Pergunta direta ao espectador, promessa, agenda |
| **preta** | Caixa preta, texto branco | Alerta e urgência. A referência usava 🚨 + "ATENÇÃO:" + ❌❌ no fim |
| **serif** | Caixa branca, fonte **serifada** (Times New Roman Bold) | Cita uma fala/pergunta entre aspas. Ar editorial, menos "anúncio" |
| **livre** | Sem caixa: texto branco com sombra preta forte, direto no vídeo | Fundo escuro ou movimentado. Menos intrusivo, mais "story de amigo" |

⚠️ **`livre` só funciona sobre fundo escuro.** Testado no bruto do caso-base
(parede clara), no mesmo dia: a sombra não segura o contraste e o texto some.
Em fundo claro, usar `branca` ou `preta`.

## Detalhes que aparecem nas referências e valem copiar

- **Emoji no fim também**, não só no começo (a referência de alerta fecha com
  ❌❌). O gerador de headline precisa aceitar emoji nas duas pontas.
- **Caixa alta** aparece no estilo `livre` ("O ACESSO TA NO PERFIL NA BIO"),
  raramente nas caixas brancas.
- **Aspas** combinam com `serif` — as duas referências serifadas eram perguntas
  entre aspas.
- A quebra de linha é **decisão de copy**, não do renderizador: quem escreve a
  headline decide onde quebra, porque a quebra muda o ritmo de leitura.

## O que ainda não se sabe

Qual estilo converte melhor, e se alternar estilo entre criativos da mesma
campanha ajuda ou atrapalha o reconhecimento da marca. O Rodrigo pediu pra
**alternar de vez em quando** — decisão de variedade, não de performance
medida. Se um dia isso for medido por criativo, o resultado vira linha aqui.
