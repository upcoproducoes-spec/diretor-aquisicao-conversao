# /// script
# requires-python = ">=3.10"
# dependencies = ["google-auth-oauthlib>=1.2"]
# [tool.uv]
# exclude-newer = "2026-11-05T00:00:00Z"
# ///
"""
Gera o refresh token do Google Ads: abre o navegador, a pessoa autoriza com o e-mail que tem
acesso à conta de anúncios, e o token vai direto pro .env como GOOGLE_ADS_REFRESH_TOKEN. O valor
nunca aparece na tela nem no log.

Precisa de GOOGLE_ADS_CLIENT_ID e GOOGLE_ADS_CLIENT_SECRET no .env, de um cliente OAuth do tipo
"app para computador". Espera até 5 minutos pela autorização.

Uso:
  uv run sirius-scale/ferramentas/google/gerar_token.py
"""

import os
import re
import sys
import tempfile
from pathlib import Path

import comum

ESCOPOS = ["https://www.googleapis.com/auth/adwords"]
ESPERA_SEGUNDOS = 300


def gravar_no_env(arquivo, chave, valor):
    """Troca a linha da chave no .env (ou acrescenta), sem mexer nas outras e sem imprimir nada.
    Grava em arquivo temporário e troca de uma vez: queda no meio não deixa o .env pela metade."""
    arq = Path(arquivo)
    texto = arq.read_text(encoding="utf-8") if arq.exists() else ""
    linha = f"{chave}={valor}"
    padrao = re.compile(rf"^[ \t]*(?:export[ \t]+)?{re.escape(chave)}[ \t]*=.*$", re.M)
    if padrao.search(texto):
        texto = padrao.sub(lambda _: linha, texto)     # função: token com \ não vira escape de regex
    else:
        if texto and not texto.endswith("\n"):
            texto += "\n"
        texto += linha + "\n"
    fd, tmp = tempfile.mkstemp(dir=str(arq.parent), prefix=".env-")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(texto)
    os.replace(tmp, arq)
    os.chmod(arq, 0o600)


def main():
    env = comum.ler_env()
    comum.exigir(env, ("GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET"))
    from google_auth_oauthlib.flow import InstalledAppFlow, WSGITimeoutError
    config = {"installed": {"client_id": env["GOOGLE_ADS_CLIENT_ID"], "client_secret": env["GOOGLE_ADS_CLIENT_SECRET"],
                            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                            "token_uri": "https://oauth2.googleapis.com/token"}}
    fluxo = InstalledAppFlow.from_client_config(config, scopes=ESCOPOS)
    try:
        credenciais = fluxo.run_local_server(
            port=0, prompt="consent", access_type="offline", timeout_seconds=ESPERA_SEGUNDOS,
            authorization_prompt_message="Autorize no navegador que abriu. Se não abriu, use este endereço:\n{url}",
            success_message="Pronto. Pode fechar esta aba e voltar pro Claude.")
    except WSGITimeoutError:
        sys.exit(f"PAREI: a autorização não veio em {ESPERA_SEGUNDOS // 60} minutos. Nada foi gravado.")
    if not credenciais.refresh_token:
        sys.exit("PAREI: o Google não devolveu refresh token. Revogue o acesso em "
                 "https://myaccount.google.com/permissions e rode de novo. Nada foi gravado.")
    gravar_no_env(comum.raiz() / ".env", "GOOGLE_ADS_REFRESH_TOKEN", credenciais.refresh_token)
    print("Refresh token gravado no .env, em GOOGLE_ADS_REFRESH_TOKEN. O valor não aparece aqui de propósito.")


if __name__ == "__main__":
    main()
