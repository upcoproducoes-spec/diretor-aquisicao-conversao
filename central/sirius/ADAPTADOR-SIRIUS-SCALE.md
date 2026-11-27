# Adaptador da Sirius Scale pra este repositório

> Este arquivo é do repositório, não do sistema: nenhuma atualização troca ele. Ele vale por cima da seção 6 do
> `COMECE-AQUI.md` que vem em cada zip.

O sistema da Sirius Scale foi feito pra uma pasta que só tem ele. Este repositório já tem organização própria,
`CLAUDE.md`, pastas de cliente e, talvez, agentes e permissões próprios. Este adaptador diz como encaixar o sistema
aqui, e como aplicar cada atualização, sem apagar nem trocar nada que já é do repositório.

## Quando usar

Sempre que chegar um zip com "Sirius Scale" e "atualização" no nome, e alguém pedir pra instalar ou atualizar o
sistema, inclusive com o texto padrão ("Atualize o sistema [...] seguindo a seção 6 do COMECE-AQUI"). O pedido vale;
o caminho é este.

**Nunca rode o `atualizar.sh` do zip aqui.** Ele foi feito pra pasta que só tem o sistema e grava por cima da `.claude/`
inteira, das permissões aos agentes.

## Regras que valem sempre

1. Nada do repositório é apagado, trocado ou editado, exceto o que este adaptador manda acrescentar.
2. Abra o zip numa pasta temporária fora do repositório e leia o que vem nele. Depois, antes de copiar qualquer coisa,
   mostre o plano e espere o ok de quem pediu.
3. Copie e troque arquivos por comando (bash ou PowerShell), não pela ferramenta de editar arquivo: a permissão
   `Edit(./sirius-scale/**)` barra essa ferramenta na `sirius-scale/`, de propósito.
4. No Windows, use o PowerShell ou o bash do Git, o que estiver disponível. Os passos são os mesmos.
5. Se o zip vier diferente do que este adaptador descreve, pare e explique o que mudou.
6. Se havia mais de um zip em Downloads, use o de versão mais nova.

## Primeira vez: instalar

Vale quando nenhuma pasta do repositório tem `sirius-scale/VERSAO.md`. O zip de atualização serve pra instalar: o
`CLAUDE.md` e as pastas de cliente o repositório já tem.

1. **Leia o zip.** `COMECE-AQUI.md`, `sirius-scale/REGRAS.md` e `sirius-scale/O-QUE-MUDOU.md`.
2. **Escolha a pasta do sistema.** É a pasta onde o Claude é aberto pra trabalhar.
   - Se cada cliente tem a própria pasta e o Claude é aberto dentro dela, o sistema entra em cada pasta de cliente.
   - Se o Claude é aberto na raiz, entra uma vez, na raiz.
   - Na dúvida, pergunte.
3. **Em cada pasta do sistema:**
   1. Copie `sirius-scale/` inteira, e o `COMECE-AQUI.md` pra dentro dela (`sirius-scale/COMECE-AQUI.md`).
   2. Copie os agentes (`.claude/agents/*.md`) e as skills (`.claude/skills/*/`) pra `.claude/` da pasta. Se já existir
      um arquivo ou pasta com o mesmo nome, na `.claude/` da pasta ou na `~/.claude/` da conta, o que está lá é de
      vocês e fica. O nosso entra com o prefixo `sirius-`: o agente `copy` vira `sirius-copy.md`, a skill `revisar`
      vira `sirius-revisar/`. Troque também o `name:` do cabeçalho pro nome novo. Por isso o mesmo agente pode ter
      nome diferente em pastas diferentes: o mapa de cada pasta diz qual é.
   3. Não copie o `.claude/settings.json` do zip. No `settings.json` da pasta (crie, se não houver), acrescente em
      `permissions.deny` só o que faltar destes: `Read(./.env)`, `Read(./.env.*)`, `Read(./.credenciais/**)` e
      `Edit(./sirius-scale/**)`. Os outros itens do nosso (como o bloqueio de editar a `.claude/`) não entram: aqui a
      `.claude/` é do repositório.
   4. Não copie o `atualizar.sh`.
4. **Monte o mapa** em `sirius-scale-mapa.md`, na pasta do sistema e fora da `sirius-scale/`, porque essa pasta é
   trocada a cada versão. O sistema procura cinco pastas a partir da pasta do sistema, e o mapa diz onde cada uma mora
   aqui. Com o pacote "Conhecimento Beatriz e Pedro" do jeito que foi instalado, o ponto de partida é este. Confira no
   disco, porque o repositório pode ter mudado:

   | O sistema procura | Beatriz | Pedro |
   |---|---|---|
   | `expert/dna-expert.md` | `clientes/sirius/beatriz-vieira/dna-expert.md` | `clientes/estrategista/pedro-sachet/dna-expert.md` |
   | `expert/brand.md` | não existe ainda | `clientes/estrategista/pedro-sachet/brand.md` |
   | `expert/produtos/` | `clientes/sirius/beatriz-vieira/produtos/` | `clientes/estrategista/pedro-sachet/produtos/` |
   | `lancamentos/` | `clientes/sirius/beatriz-vieira/lancamentos/` | `clientes/estrategista/pedro-sachet/lancamentos/` |
   | `funis/` | `clientes/sirius/beatriz-vieira/funis/` | `clientes/estrategista/pedro-sachet/funis/` |
   | `entregas/` | `outputs/beatriz-vieira/` | `outputs/pedro-sachet/` |
   | `frameworks-da-casa/` | a pasta de frameworks do repositório, se houver; senão, crie `frameworks-da-casa/` com um `LEIA-ME.md` de uma linha, pra pasta não sumir no git | idem |
   | `COMECE-AQUI.md` | `sirius-scale/COMECE-AQUI.md` | idem |

   Os caminhos do mapa partem da pasta do sistema. Se o sistema estiver na raiz, com mais de um cliente, o mapa tem uma
   coluna por cliente, e o agente usa a do cliente da tarefa; se não der pra saber qual é, ele pergunta.

   O mapa também guarda:
   - os agentes e skills que ganharam o prefixo `sirius-`, com o nome de antes;
   - a lista de todo arquivo nosso copiado pra `.claude/`, com o hash (sha256) dele já com o aviso do passo 5.
5. **Ponha o aviso nos nossos agentes e skills.** Em cada arquivo nosso que entrou na `.claude/`, logo depois do
   cabeçalho (`---` ... `---`), acrescente:

   ```
   > Neste repositório, `expert/`, `lancamentos/`, `funis/`, `entregas/`, `frameworks-da-casa/` e `COMECE-AQUI.md`
   > são lidos pelo `sirius-scale-mapa.md`, na pasta do sistema. Leia o mapa antes de abrir qualquer um deles. Agente
   > ou skill citado pelo nome: confira no mapa se ele ganhou o prefixo `sirius-` aqui.
   ```

   É a única mudança permitida num arquivo nosso. Ela se refaz a cada atualização. Arquivo sem cabeçalho (os checklists
   do `/revisar`, o `LICENSE` do humanizer) entra como veio, sem aviso, e também vai pro mapa com o hash.
6. **Ligue no `CLAUDE.md`.** No fim do `CLAUDE.md` da pasta do sistema (crie, se não houver), sem mexer no resto e com
   uma linha em branco antes:

   ```
   ## Sistema da Sirius Scale
   @sirius-scale/REGRAS.md

   As pastas que o sistema cita estão no `sirius-scale-mapa.md`. Instalação e atualização da Sirius Scale seguem o
   `ADAPTADOR-SIRIUS-SCALE.md`, mesmo quando o pedido citar a seção 6 do COMECE-AQUI. Nunca rode o `atualizar.sh`.
   ```

   Se o adaptador ficar numa pasta acima, escreva o caminho dele no lugar do nome.
7. **Guarde este adaptador** na raiz do repositório, como `ADAPTADOR-SIRIUS-SCALE.md`.
8. **Leia "Nos arquivos de vocês"** de todas as versões do `O-QUE-MUDOU.md`. Liste o que cada uma pede, já traduzido
   pelo mapa, e aplique só o que quem pediu aprovar. O que uma versão mandar pôr no `CLAUDE.md` (como o teto de verba)
   entra na seção "Sistema da Sirius Scale" do `CLAUDE.md` da pasta do sistema.
9. **Relate em lista numerada:** onde o sistema entrou, o que ganhou prefixo, o mapa, as permissões acrescentadas e o
   que ficou pendente. Peça pra abrir uma conversa nova.

## Toda atualização

Vale quando a pasta do sistema já tem `sirius-scale/VERSAO.md`.

1. **Ache todas as pastas do sistema.** São as que têm `sirius-scale/VERSAO.md`, inclusive as vizinhas, quando o Claude
   foi aberto numa pasta de cliente. A atualização vale pra todas na mesma conversa: mostre a lista no plano.
2. **Confira a versão.** A do zip tem que ser mais nova que a de cada pasta do sistema. Na pasta em que for igual ou mais
   velha, não mexa em nada.
3. **Leia o `O-QUE-MUDOU.md` novo**, das versões entre a instalada e a do zip.
4. **Em cada pasta do sistema:**
   1. Troque a `sirius-scale/` inteira pela nova, e o `sirius-scale/COMECE-AQUI.md` pelo do zip.
   2. Pra cada agente e skill do zip:
      - nome com prefixo no mapa: vai pro nome do mapa;
      - arquivo que ainda não existe: copie e anote no mapa, pela regra do passo 3.2 da instalação;
      - arquivo nosso cujo hash bate com o do mapa: troque pelo novo;
      - arquivo nosso cujo hash não bate, porque alguém mexeu: não grave por cima. Guarde o novo ao lado, com `.novo` no
        fim do nome, e avise.
   3. Refaça o passo 5 da instalação nos arquivos trocados e atualize os hashes no mapa.
   4. Não toque no `settings.json`, no `CLAUDE.md`, no mapa nem neste adaptador. Se a versão nova trouxer uma regra de
      permissão nova, liste e pergunte.
5. **Aplique "Nos arquivos de vocês"** de cada versão nova, traduzido pelo mapa, só com o ok de quem pediu.
6. **Relate:** a versão de antes e a de agora em cada pasta do sistema, o que entrou, o que ficou com `.novo` e o que
   ficou pendente. Peça pra abrir uma conversa nova.
