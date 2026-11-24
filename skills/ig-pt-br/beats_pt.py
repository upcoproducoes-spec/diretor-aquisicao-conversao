#!/usr/bin/env python3
"""
beats_pt.py - cronometra um roteiro de Reel em portugues em batidas.

Camada fina sobre ig-reel/beats.py (instagram-agent-skill, Jake Schincariol,
MIT): reaproveita o calculo de tempo, os alertas (gancho acima de 3s, batida
acima de 4s, trecho abstrato, falta de laco) e troca so o que e de idioma:
o que conta como palavra e como "concreto", as palavras vazias usadas para
achar o laco e a exibicao do milhar com ponto. Ver NOTICE.md.

Os textos dos alertas continuam em ingles: quem entrega ao usuario traduz.
Informe o seu ritmo real com --wpm (veja voice.md): em portugues, a maior
parte das pessoas fica entre 150 e 190 palavras por minuto.

Uso
  python beats_pt.py roteiro.txt --target 30
  python beats_pt.py roteiro.txt --wpm 175 --target 45
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

ORIGINAL = os.path.join(HERE, "..", "ig-reel", "beats.py")


def load_original():
    if not os.path.exists(ORIGINAL):
        print("erro: ig-reel/beats.py (pacote original) não está instalado em "
              + os.path.normpath(ORIGINAL), file=sys.stderr)
        sys.exit(3)
    spec = importlib.util.spec_from_file_location("ig_beats_original", ORIGINAL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def patch(B):
    B.WORD_RE = P.WORD_RE
    B.words = P.words
    B.CONCRETE_RE = re.compile(
        r"R\$\s?\d|\b\d[\d.,]*\b|(?<!^)\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]{2,}\b", re.MULTILINE)
    B.STOPWORDS = P.STOPWORDS
    B.pretty = lambda tok: re.sub(r"(\d)(?=(\d{3})+$)", r"\1.", tok)
    return B


def main():
    P.utf8_stdio()
    B = patch(load_original())
    ap = argparse.ArgumentParser(description="Cronometra um roteiro de Reel em português.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo do roteiro, ou - para stdin")
    ap.add_argument("--wpm", type=float, default=165, help="ritmo de fala (padrão 165)")
    ap.add_argument("--target", type=float, help="duração alvo em segundos")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    a = B.analyse(raw, wpm=args.wpm, target=args.target)
    if not a:
        print("roteiro vazio", file=sys.stderr)
        sys.exit(2)
    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        B.render(a)


if __name__ == "__main__":
    main()
