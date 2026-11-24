#!/usr/bin/env python3
"""
humanize_pt.py - tira a marca de maquina de um rascunho em portugues.

Camada fina sobre ig-human/humanize.py (instagram-agent-skill, Jake
Schincariol, MIT): reaproveita as tres passadas do original (caracteres
invisiveis, tipografia, lexico) mas com o lexico em portugues (slop.pt.json) e
com a correcao de maiuscula que entende acento. Ver NOTICE.md.

Passadas:
  1. INVISIVEL    apaga caracteres que o teclado nao produz (espaco de largura
                  zero, junta-palavras, hifen suave, BOM, caracteres de tag).
  2. TIPOGRAFIA   travessao -> virgula, aspas curvas -> retas, reticencias -> tres pontos.
  3. LEXICO       troca/apaga expressoes de enchimento e de video (slop.pt.json),
                  so as que sao seguras de trocar (expressoes fixas).

O que depende de julgamento (estrutura "nao e so X, e Y", saudacao, isca de
seguir, vocabulario de IA) NAO e reescrito: e SINALIZADO para voce reescrever.

Uso
  python humanize_pt.py rascunho.txt
  python humanize_pt.py rascunho.txt --report
  python humanize_pt.py rascunho.txt -o limpo.txt
  python humanize_pt.py rascunho.txt --json
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

LEX = os.path.join(HERE, "slop.pt.json")
ORIGINAL = os.path.join(HERE, "..", "ig-human", "humanize.py")


def load_original():
    if not os.path.exists(ORIGINAL):
        print("erro: ig-human/humanize.py (pacote original) não está instalado em "
              + os.path.normpath(ORIGINAL), file=sys.stderr)
        sys.exit(3)
    spec = importlib.util.spec_from_file_location("ig_human_original", ORIGINAL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def restore_capitals_pt(original, text):
    """Apagar uma abertura deixa a proxima palavra em minuscula. So corrige para
    quem capitaliza as frases (voz toda em minuscula e estilo, nao defeito)."""
    starts = re.findall(r"(?:^|[.!?]\s+|\n)\s*([^\W\d_])", original)
    if not starts or sum(1 for c in starts if c.isupper()) * 2 < len(starts):
        return text
    return re.sub(r"(?:^|(?<=[.!?] )|(?<=[.!?]\n)|(?<=\n))\s*([^\W\d_])",
                  lambda m: m.group(0)[:-1] + m.group(1).upper(), text)


def cleanup_dangling_pt(text):
    """Depois de apagar dois pedidos ligados por "e", sobra "E!" ou "... e.".
    Tira a conjuncao que ficou sozinha ou pendurada no fim da frase."""
    text = re.sub(r"(?im)(?:^|(?<=[.!?]\s))[ \t]*(?:e|ou|mas|que)[ \t]*[.!?]+[ \t]*", "", text)
    text = re.sub(r"(?i)[ \t]+(?:e|ou|mas)[ \t]*([.!?])", r"\1", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text


def humanize(text, lex, H):
    # a funcao original ja faz as tres passadas; a correcao de maiuscula dela so
    # entende A-Z, entao limpamos conjuncao solta e refazemos a nossa por cima.
    clean, report = H.humanize(text, lex)
    clean = cleanup_dangling_pt(clean)
    clean = restore_capitals_pt(text, clean).strip() + "\n"
    return clean, report


def render_report(report, out=sys.stderr):
    def head(title):
        print(f"\n{title}\n" + "-" * len(title), file=out)

    total = sum(h["count"] for h in report["invisible"]) \
        + sum(h["count"] for h in report["typographic"]) \
        + sum(h["count"] for h in report["lexical"])
    head("RELATÓRIO DO HUMANIZADOR (PT-BR)")
    print(f"{total} marca(s) de máquina removida(s), "
          f"{len(report['structures'])} estrutura(s) sinalizada(s) para você reescrever", file=out)
    if report["invisible"]:
        head("1. CARACTERES INVISÍVEIS")
        for h in report["invisible"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['action']}", file=out)
    if report["typographic"]:
        head("2. TIPOGRAFIA")
        for h in report["typographic"]:
            print(f"  {h['count']:>3}x  {h['name']}  -> {h['to']}", file=out)
    if report["lexical"]:
        head("3. LÉXICO DE ENCHIMENTO")
        for h in report["lexical"]:
            print(f"  {h['count']:>3}x  {h['find']}  -> {h['replace']}   [{h['family']}]", file=out)
    if report["structures"]:
        head("4. ESTRUTURAS SINALIZADAS  (não são corrigidas sozinhas: reescreva)")
        for h in report["structures"]:
            print(f"  {h['count']:>3}x  {h['name']}\n        {h['fix']}", file=out)
    if not any(report.values()):
        head("LIMPO")
        print("  Nada a tirar.", file=out)
    print("", file=out)


def main():
    P.utf8_stdio()
    ap = argparse.ArgumentParser(description="Tira a marca de máquina de um rascunho em português.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo, ou - para stdin")
    ap.add_argument("-o", "--out", help="grava o texto limpo aqui em vez de imprimir")
    ap.add_argument("--report", action="store_true", help="mostra o que mudou (em stderr)")
    ap.add_argument("--json", action="store_true", help="devolve {text, report} em JSON")
    ap.add_argument("--lexicon", default=LEX, help="caminho do slop.pt.json")
    args = ap.parse_args()

    H = load_original()
    raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
    lex = H.load_lexicon(args.lexicon)
    clean, report = humanize(raw, lex, H)

    if args.json:
        print(json.dumps({"text": clean, "report": report}, indent=2, ensure_ascii=False))
        return
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(clean)
        print(f"gravado em {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(clean)
    if args.report:
        render_report(report)


if __name__ == "__main__":
    main()
