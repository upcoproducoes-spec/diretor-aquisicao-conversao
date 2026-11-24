#!/usr/bin/env python3
"""
caption_pt.py - confere uma legenda em portugues antes de postar.

Camada fina sobre ig-caption/caption.py (instagram-agent-skill, Jake
Schincariol, MIT): reaproveita a janela de 125 caracteres, o limite de
hashtags, a checagem de link e de emoji, e troca so o que e de idioma: o que
conta como "concreto", as chamadas para acao (ASKS) e as hashtags genericas.
Ver NOTICE.md.

Os rotulos da saida continuam em ingles (PASS/WARN/FAIL, nomes das checagens):
quem entrega o resultado ao usuario traduz.

ATENCAO: o limite de 5 hashtags e a janela de ~125 caracteres sao regras de
plataforma citadas pelo autor do original (a de 5 hashtags, desde 18/12/2025).
Plataforma muda. Confirme na documentacao atual antes de tratar como fato.

Uso
  python caption_pt.py legenda.txt --keywords "protese total,dentista"
  python caption_pt.py legenda.txt --truncate 125 --json
"""

import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ptlib as P  # noqa: E402

ORIGINAL = os.path.join(HERE, "..", "ig-caption", "caption.py")


def load_original():
    if not os.path.exists(ORIGINAL):
        print("erro: ig-caption/caption.py (pacote original) não está instalado em "
              + os.path.normpath(ORIGINAL), file=sys.stderr)
        sys.exit(3)
    spec = importlib.util.spec_from_file_location("ig_caption_original", ORIGINAL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def patch(C):
    C.HASHTAG_RE = re.compile(r"(?:^|\s)(#\w+)")
    C.MENTION_RE = re.compile(r"(?:^|\s)(@[\w.]+)")
    C.CONCRETE_RE = re.compile(
        r"R\$\s?\d|\b\d[\d.,]*\b|(?<!^)\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]{2,}\b", re.MULTILINE)
    C.ASKS = [
        # a palavra-chave precisa estar em MAIUSCULAS (comente BLACK), senao "comente isso" contaria
        (re.compile(r"\b[Cc]oment(?:e|a|ar)\s+(?:a palavra\s+|[\"“])?[A-ZÁÉÍÓÚÂÊÔÃÕÇ0-9]{2,}\b"),
         "comentar uma palavra-chave"),
        (re.compile(r"(?i)\b(?:me chama|me manda|chama|manda|mande|envie)\s+(?:uma\s+)?(?:no\s+)?(?:direct|dm|mensagem)\b"),
         "chamar no direct"),
        (re.compile(r"(?i)\bsalv[ae]r?\s+(?:esse|essa|este|esta|isso)\b"), "salvar"),
        (re.compile(r"(?i)\bcompartilh[ae]\s+(?:esse|essa|este|esta|isso)\b|"
                    r"\b(?:manda|mande|envie)\s+(?:isso\s+)?(?:pra|para)\s+(?:alguem|alguém|um amigo|uma amiga|quem)\b"),
         "compartilhar"),
        (re.compile(r"(?i)\b(?:me segue|me siga|segue|siga)\s+(?:pra|para|o perfil|a conta|aqui)\b"), "seguir"),
        (re.compile(r"(?i)\blink (?:na|da|no) (?:bio|biografia|perfil)\b"), "link na bio"),
        (re.compile(r"(?i)\b(?:arrasta|arraste|desliza|deslize)\s+(?:pro|para|pra|o)?\s*(?:lado|carrossel|slide|proximo|próximo)\b|"
                    r"\bpasse? pro lado\b"), "arrastar"),
        (re.compile(r"(?i)\bme (?:conta|diz|responde|fala)\b|\bqual (?:voce|você|dessas|dos|das)\b|\bcomente abaixo\b|\bcomenta (?:aqui|abaixo)\b"),
         "responder uma pergunta"),
    ]
    C.FILLER_TAGS = set(C.FILLER_TAGS) | {
        "#viralizar", "#explorar", "#reelsbrasil", "#brasil", "#seguidores", "#dicas",
        "#instagram", "#reelsviral", "#instabrasil", "#sucesso", "#motivacao", "#foco"}
    return C


def main():
    P.utf8_stdio()
    C = patch(load_original())
    ap = argparse.ArgumentParser(description="Confere uma legenda em português.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo da legenda, ou - para stdin")
    ap.add_argument("--truncate", type=int, default=C.TRUNCATE,
                    help="onde o feed corta em '... mais' (padrão 125; é aproximado)")
    ap.add_argument("--keywords", default="", help="termos de busca, separados por vírgula")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    a = C.analyse(raw, cut=args.truncate, keywords=keywords)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        C.render(a)
    sys.exit(0 if a.get("verdict") in ("READY", "REVIEW") else 1)


if __name__ == "__main__":
    main()
