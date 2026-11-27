"""
Base das ferramentas do Google Ads: acha a pasta do sistema, lê o .env dela e monta o
cliente da API. Não é script: quem roda são os arquivos ao lado, com `uv run`.

Nada aqui imprime valor do .env. O que falta é dito pelo NOME da variável, nunca pelo
conteúdo. A biblioteca do Google só é importada dentro de `cliente()`: o `gerar_token.py`
e o `mcp_google.py` não precisam dela.

Variáveis do .env (na raiz da pasta do sistema):
  GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
  GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_LOGIN_CUSTOMER_ID (só com conta gerente),
  GOOGLE_PROJECT_ID (o servidor de leitura pede) e TETO_CAMPANHA_DIA.
"""

import os
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

# No Windows a saída por tubo não é UTF-8, e seta ou acento derrubariam o print.
for _saida in (sys.stdout, sys.stderr):
    if hasattr(_saida, "reconfigure"):
        _saida.reconfigure(encoding="utf-8", errors="replace")

CREDENCIAIS = ("GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_CLIENT_ID", "GOOGLE_ADS_CLIENT_SECRET",
               "GOOGLE_ADS_REFRESH_TOKEN")
_LINHA = re.compile(r"^\s*(?:export\s+)?([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.*)$")
_raiz = None


def achar_raiz(partida=None):
    """A pasta do sistema: a primeira, subindo a partir deste arquivo, que tem CLAUDE.md e
    sirius-scale/ dentro. Exigir os dois é de propósito: CLAUDE.md sozinho aparece em qualquer
    projeto, e subir até o projeto errado leria o .env errado, de outra conta."""
    for pasta in Path(partida or __file__).resolve().parents:
        if (pasta / "CLAUDE.md").is_file() and (pasta / "sirius-scale").is_dir():
            return pasta
    sys.exit("PAREI: não achei a pasta do sistema (a que tem CLAUDE.md e sirius-scale/). "
             "Estas ferramentas rodam de dentro dela, em sirius-scale/ferramentas/google/.")


def raiz():
    global _raiz
    if _raiz is None:
        _raiz = achar_raiz()
    return _raiz


def caminho(rel):
    """Caminho do registro e dos arquivos dele: relativo à raiz da pasta do sistema."""
    return str(rel) if os.path.isabs(rel) else str(raiz() / rel)


def _valor(bruto):
    v = bruto.strip()
    if v[:1] in ("'", '"'):
        fim = v.find(v[0], 1)
        if fim > 0:
            return v[1:fim]
    if v.startswith("#"):
        return ""
    return re.split(r"\s+#", v, maxsplit=1)[0].strip()


def ler_env(arquivo=None):
    """Lê o .env sem dependência externa e devolve um dict. Não toca em os.environ e não imprime
    nada: valor de variável do shell não entra, pra um export esquecido não apontar outra conta."""
    arq = Path(arquivo) if arquivo else raiz() / ".env"
    if not arq.is_file():
        return {}
    out = {}
    for linha in arq.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        if linha.lstrip().startswith("#"):
            continue
        m = _LINHA.match(linha)
        if m:
            out[m.group(1)] = _valor(m.group(2))
    return out


def exigir(env, nomes):
    """Para e diz o NOME do que falta no .env. Valor nenhum vai pra tela."""
    faltam = [n for n in nomes if not env.get(n)]
    if faltam:
        sys.exit("PAREI: falta no .env da pasta do sistema: " + ", ".join(faltam) + ". Nada foi feito.")


def teto_campanha(env=None, obrigatorio=True):
    """O teto em reais por campanha, por dia. Ele é combinado com quem é dono da verba: sem ele,
    escrita nenhuma sai, e não existe número padrão aqui. `obrigatorio=False` é pra leitura e
    prévia, que seguem sem teto e dizem que ele falta."""
    env = ler_env() if env is None else env
    bruto = (env.get("TETO_CAMPANHA_DIA") or "").strip()
    if not bruto:
        if obrigatorio:
            sys.exit("PAREI: falta TETO_CAMPANHA_DIA no .env (reais por dia, por campanha). O teto é "
                     "combinado com quem é dono da verba, então não escolho um número. Nada foi escrito.")
        return None
    m = re.fullmatch(r"(\d+)(?:[.,](\d{1,2}))?", bruto)
    teto = float(f"{m.group(1)}.{m.group(2) or 0}") if m else 0
    if teto <= 0:
        sys.exit("PAREI: TETO_CAMPANHA_DIA no .env tem que ser reais por dia, maior que zero e sem "
                 "ponto de milhar (exemplo: 300 ou 300,50). Nada foi escrito.")
    return teto


def so_digitos(valor):
    """A tela do Google mostra 123-456-7890; a API quer só os dígitos."""
    return re.sub(r"\D", "", str(valor or ""))


def brl(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def cliente(env=None):
    env = ler_env() if env is None else env
    exigir(env, CREDENCIAIS)
    from google.ads.googleads.client import GoogleAdsClient
    cfg = {"developer_token": env["GOOGLE_ADS_DEVELOPER_TOKEN"], "client_id": env["GOOGLE_ADS_CLIENT_ID"],
           "client_secret": env["GOOGLE_ADS_CLIENT_SECRET"], "refresh_token": env["GOOGLE_ADS_REFRESH_TOKEN"],
           "use_proto_plus": True}
    gerente = so_digitos(env.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"))
    if gerente:
        cfg["login_customer_id"] = gerente
    return GoogleAdsClient.load_from_dict(cfg)
