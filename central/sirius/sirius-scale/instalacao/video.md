# Instalar o módulo de vídeo (HyperFrames)

> Guia pro Claude seguir, a pedido: "Instale o módulo de vídeo seguindo `sirius-scale/instalacao/video.md`".
> Testado num Mac com a pasta de usuário vazia: skills, navegador, diagnóstico e um vídeo de 10 segundos em
> 6 minutos, uns 380 MB baixados. Node, ffmpeg e whisper já estavam na máquina. No Windows ainda não rodou.

O HyperFrames é uma ferramenta aberta (licença Apache 2.0) que renderiza vídeo a partir de HTML. Ela não vem
no zip porque depende da máquina e muda toda semana: o jeito certo é instalar a versão atual. Não troque
nenhum programa que já funciona, e diga antes o que vai instalar.

## O que precisa existir

| Peça | Pra quê | Como conferir |
|---|---|---|
| Node 22 ou mais novo | roda o HyperFrames | `node --version` |
| ffmpeg e ffprobe | cortar, juntar, exportar e medir | `ffmpeg -version` |
| whisper-cpp | transcrever com o tempo de cada palavra | `whisper-cli --help` |
| Navegador do HyperFrames | renderizar | `npx --yes hyperframes@latest browser ensure` |
| Skills do HyperFrames | ensinar o Claude a montar | `npx --yes hyperframes@latest skills check` |

## Passo a passo

1. **Descubra o sistema.** No Mac, `uname -s` responde `Darwin`. No Windows, siga a parte Windows abaixo.
2. **Instale só o que faltou.**
   - **Mac:** confira `brew --version`. Sem Homebrew, pare e mostre esta linha pra pessoa colar no Terminal.
     Ela pede a senha do Mac, e senha não se digita pelo Claude:

     ```
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     ```

     No fim, o instalador mostra duas linhas de "Next steps": a pessoa cola as duas também. Depois disso:
     `brew install node ffmpeg whisper-cpp`.
   - **Windows:** `winget install OpenJS.NodeJS.LTS` e `winget install Gyan.FFmpeg`. Peça pra reabrir o app
     do Claude se o comando não aparecer depois de instalar. O whisper-cpp no Windows não foi testado: se não
     houver caminho simples, siga sem ele e diga que a transcrição vai precisar de outro meio.
3. **Skills:** `npx --yes hyperframes@latest skills`. Esse é o passo mais longo: em silêncio por vários
   minutos é normal. Ele instala o conjunto principal, e as outras skills entram sob demanda quando o
   próprio HyperFrames pedir.
4. **Navegador:** `npx --yes hyperframes@latest browser ensure`.
5. **Diagnóstico:** `npx --yes hyperframes@latest doctor`. Leia a saída. Marca de erro em TTS, MusicGen e
   Docker é opcional e não trava nada. Node, ffmpeg, ffprobe e Chrome têm que estar com o sinal de certo.
6. **Vídeo de teste**, numa pasta temporária fora da pasta do sistema:

   ```
   npx --yes hyperframes@latest init teste-video --non-interactive --example blank --skip-skills --resolution portrait
   cd teste-video
   npx --yes hyperframes@latest render --quality draft -o teste.mp4
   ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 teste.mp4
   ```

   Tem que voltar 1080 por 1920 e uma duração maior que zero. Apague a pasta de teste depois.
7. **Encerre.** Diga o que instalou, o resultado do teste e peça pra abrir uma conversa nova: as skills só
   aparecem na próxima conversa.

## Depois de instalado

- **Atualizar:** `npx --yes hyperframes@latest skills update`.
- **Disco:** o HyperFrames guarda uma cópia do vídeo a cada comando, e uma peça vertical de 73 segundos pediu
  18 GB de quadros temporários no caso de origem. Com render parado, `npx --yes hyperframes@latest clean`
  libera. Confira o espaço livre antes de uma leva.
- **Como editar:** o agente `video` e `sirius-scale/frameworks/copy/edicao-video-receita.md`.
