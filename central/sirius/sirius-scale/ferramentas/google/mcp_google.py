# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Abre o servidor oficial do Google Ads (pacote google-ads-mcp) em modo stdio, pro Claude Code
iniciar sozinho: sem terminal aberto e sem porta de rede. É o que o `.mcp.json` da pasta chama.

O QUE FAZ, EM ORDEM:
  1. Lê o .env e escreve a credencial do tipo authorized_user em .credenciais/google-adc.json,
     na raiz, com permissão 600. É o formato que o servidor lê.
  2. Monta o ambiente do processo com a lista curta do que o servidor precisa. As variáveis
     GOOGLE_ADS_MCP_OAUTH_* ficam de fora mesmo que existam no shell: com elas o pacote troca
     pra HTTP e abre porta em todas as interfaces da máquina.
  3. Roda o pacote pelo uvx, com versão e data de resolução fixas. Versão nova entra trocando
     as duas constantes abaixo, depois de ler o que mudou.

Só leitura: `mcp_somente_leitura.yaml` desliga labels e assets. stdout é o canal do protocolo,
então nada daqui imprime nele; aviso e erro vão pro stderr.

Uso (o Claude Code chama sozinho; à mão, só pra preparar):
  uv run sirius-scale/ferramentas/google/mcp_google.py --preparar
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import comum

VERSAO = "0.0.6"
RESOLVER_ATE = "2026-11-05T00:00:00Z"    # dependências de até esta data: o que foi testado é o que roda
PYTHON = "3.12"
NECESSARIAS = comum.CREDENCIAIS + ("GOOGLE_PROJECT_ID",)
SOMENTE_LEITURA = Path(__file__).resolve().with_name("mcp_somente_leitura.yaml")
FORA_DO_FILHO = ("PYTHONPATH", "PYTHONHOME", "VIRTUAL_ENV", "GOOGLE_APPLICATION_CREDENTIALS", "GOOGLE_PROJECT_ID")


def escrever_adc(raiz, env):
    """Credencial no formato que o Google lê. Temporário + troca: o arquivo nunca existe aberto
    pra outro usuário, nem pela metade. A pasta ganha um .gitignore próprio, pra não subir pra git."""
    pasta = Path(raiz) / ".credenciais"
    pasta.mkdir(mode=0o700, exist_ok=True)
    os.chmod(pasta, 0o700)
    ignora = pasta / ".gitignore"
    if not ignora.exists():
        ignora.write_text("*\n", encoding="utf-8")
    dados = {"type": "authorized_user", "client_id": env["GOOGLE_ADS_CLIENT_ID"],
             "client_secret": env["GOOGLE_ADS_CLIENT_SECRET"], "refresh_token": env["GOOGLE_ADS_REFRESH_TOKEN"]}
    fd, tmp = tempfile.mkstemp(dir=str(pasta), prefix=".adc-")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(dados, f)
    alvo = pasta / "google-adc.json"
    os.replace(tmp, alvo)
    os.chmod(alvo, 0o600)
    return alvo


def ambiente_do_servidor(env, adc, base=None):
    """O ambiente do processo do servidor. Nada com prefixo GOOGLE_ADS_ passa do shell: só o que
    está na lista de baixo, e o segredo do OAuth vai no arquivo da credencial, nunca aqui."""
    base = os.environ if base is None else base
    filho = {k: v for k, v in base.items() if not k.startswith("GOOGLE_ADS_") and k not in FORA_DO_FILHO}
    filho.update({"GOOGLE_APPLICATION_CREDENTIALS": str(adc),
                  "GOOGLE_ADS_DEVELOPER_TOKEN": env["GOOGLE_ADS_DEVELOPER_TOKEN"],
                  "GOOGLE_PROJECT_ID": env["GOOGLE_PROJECT_ID"],
                  "GOOGLE_ADS_MCP_TOOLS_CONFIG": str(SOMENTE_LEITURA)})
    gerente = comum.so_digitos(env.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"))
    if gerente:
        filho["GOOGLE_ADS_LOGIN_CUSTOMER_ID"] = gerente
    return filho


def achar_uvx():
    """O app do Claude nem sempre herda o PATH do terminal, por isso procura também onde o uv se instala."""
    extras = [Path.home() / ".local" / "bin", Path("/opt/homebrew/bin"), Path("/usr/local/bin")]
    caminho = os.pathsep.join([os.environ.get("PATH", "")] + [str(p) for p in extras])
    uvx = shutil.which("uvx", path=caminho)
    if not uvx:
        sys.exit("PAREI: não achei o uvx. Ele vem junto com o uv; veja o LEIA-ME desta pasta.")
    return uvx


def comando(uvx, *rodar):
    return [uvx, "--quiet", "--python", PYTHON, "--exclude-newer", RESOLVER_ATE,
            "--from", f"google-ads-mcp=={VERSAO}", *rodar]


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--preparar", action="store_true",
                   help="só baixa o servidor e sai: a primeira abertura leva minutos e estoura a espera do Claude Code")
    a = p.parse_args()
    env = comum.ler_env()
    comum.exigir(env, NECESSARIAS)
    uvx = achar_uvx()
    if a.preparar:
        r = subprocess.call(comando(uvx, "python", "-c", "import ads_mcp.config"), stdout=sys.stderr)
        print("Servidor pronto." if r == 0 else f"PAREI: a preparação terminou com erro {r}.", file=sys.stderr)
        sys.exit(r)
    adc = escrever_adc(comum.raiz(), env)
    filho = ambiente_do_servidor(env, adc)
    cmd = comando(uvx, "google-ads-mcp")
    if os.name == "nt":                     # no Windows exec não herda o stdio direito
        sys.exit(subprocess.call(cmd, env=filho))
    os.execve(uvx, cmd, filho)


if __name__ == "__main__":
    main()
