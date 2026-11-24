#!/usr/bin/env python3
"""
swipe_pt.py - ranqueia os reels coletados pelo multiplo sobre a mediana da
PROPRIA conta, nomeia a formula de gancho e mostra o que separa o terco de cima
do terco de baixo. Versao em portugues de ig-viral/swipe.py (instagram-agent-skill,
Jake Schincariol, MIT). Ver NOTICE.md.

Views brutas nao sao evidencia: conta de 2 milhoes de seguidores com 400 mil
views teve uma terca fraca; conta de 4 mil com 400 mil views achou algo
copiavel. Por isso a base de comparacao e a mediana da conta.

Entrada: TSV (colunas separadas por TAB) com cabecalho. Colunas aceitas, em
portugues ou ingles: conta/account, seguidores/followers, mediana/median,
views/visualizacoes, gancho/hook.

  conta<TAB>seguidores<TAB>mediana<TAB>views<TAB>gancho
  @alguem<TAB>48000<TAB>11000<TAB>412000<TAB>ninguem te conta que seus primeiros 30 reels vao flopar

Uso
  python swipe_pt.py coletado.tsv --out CAMINHO/instagram/swipe.md
  python swipe_pt.py coletado.tsv --json
"""

import argparse
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ptlib as P            # noqa: E402
import hookscore_pt as HS    # noqa: E402

HOOKS = os.path.join(HERE, "hooks.pt.json")
ALIASES = {
    "conta": "account", "account": "account",
    "seguidores": "followers", "followers": "followers",
    "mediana": "median", "median": "median",
    "views": "views", "visualizacoes": "views", "visualizações": "views",
    "gancho": "hook", "hook": "hook",
}


def load_formulas(path):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return None
    by_id = {h["id"]: h for h in d["hooks"]}
    order = d.get("classify_order") or sorted(by_id)
    return [(by_id[i]["id"], by_id[i]["name"],
             re.compile(by_id[i]["match"])) for i in order if i in by_id]


def classify(hook, formulas):
    if not formulas:
        return None, "sem fórmula"
    text = P.norm(hook)
    for fid, name, pattern in formulas:
        if pattern.search(text):
            return fid, name
    return None, "sem fórmula"


def read_rows(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    lines = [l for l in raw.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    if not lines:
        return []
    head = [ALIASES.get(P.norm(c.strip()), P.norm(c.strip())) for c in lines[0].split("\t")]
    if "views" in head and "hook" in head:
        cols, body = head, lines[1:]
    else:
        cols, body = ["account", "followers", "views", "hook"], lines
    rows = []
    for line in body:
        cells = line.split("\t")
        if len(cells) < len(cols):
            cells += [""] * (len(cols) - len(cells))
        r = dict(zip(cols, [c.strip() for c in cells]))
        try:
            r["views"] = int(re.sub(r"[^\d]", "", r.get("views", "")) or 0)
        except ValueError:
            continue
        for k in ("followers", "median"):
            digits = re.sub(r"[^\d]", "", r.get(k, "") or "")
            r[k] = int(digits) if digits else None
        if r["views"] and r.get("hook"):
            rows.append(r)
    return rows


def analyse(rows, formulas):
    used_median = any(r.get("median") for r in rows)
    for r in rows:
        base = r.get("median") or r.get("followers") or 0
        r["baseline"] = base
        r["outlier"] = round(r["views"] / base, 2) if base else None
        r["formula_id"], r["formula"] = classify(r["hook"], formulas)
        r["words"] = len(P.words(r["hook"]))
        _, overall, verdict, _ = HS.run(r["hook"])
        r["hook_score"], r["hook_verdict"] = round(overall, 1), verdict
    ranked = sorted(rows, key=lambda r: -(r["outlier"] or 0))
    third = max(1, len(ranked) // 3)
    top, bottom = ranked[:third], ranked[-third:]

    def med(items, key):
        vals = [i[key] for i in items if i.get(key) is not None]
        return round(statistics.median(vals), 1) if vals else None

    counts = {}
    for r in top:
        counts[r["formula"]] = counts.get(r["formula"], 0) + 1
    return {
        "baseline": "mediana da conta" if used_median else "número de seguidores (fraco: informe a mediana)",
        "n": len(ranked),
        "accounts": len({r.get("account", "") for r in ranked}),
        "reels": ranked,
        "top_formulas": sorted(counts.items(), key=lambda kv: -kv[1]),
        "top_hook_score": med(top, "hook_score"),
        "bottom_hook_score": med(bottom, "hook_score"),
        "top_words": med(top, "words"),
        "bottom_words": med(bottom, "words"),
        "unclassified": sum(1 for r in ranked if r["formula_id"] is None),
    }


def render(a, out=sys.stdout):
    head = (f"REFERÊNCIAS  ·  {a['n']} reels  ·  {a['accounts']} contas  ·  "
            f"base: {a['baseline']}")
    print("\n" + head, file=out)
    print("=" * max(len(head), 78), file=out)
    for r in a["reels"]:
        mult = f"{r['outlier']:.1f}x" if r["outlier"] else "   ?"
        fid = f"#{r['formula_id']:<2}" if r["formula_id"] else "-  "
        print(f"  {mult:>7}  gancho {r['hook_score']:>3.0f}  {fid} {r['formula'][:28]:<28} "
              f"{r.get('account', '')[:16]:<16} {r['views']:>9,}", file=out)
        print(f"           \"{r['hook'][:96]}\"", file=out)
    print("-" * max(len(head), 78), file=out)
    print("O QUE FUNCIONA NESTE LOTE", file=out)
    if a["top_formulas"]:
        print("  terço de cima por múltiplo:  "
              + ", ".join(f"{n} x{c}" for n, c in a["top_formulas"][:4]), file=out)
    if a["top_hook_score"] is not None:
        print(f"  nota mediana do gancho:      topo {a['top_hook_score']:.0f}  "
              f"contra fundo {a['bottom_hook_score']:.0f}", file=out)
    print(f"  tamanho mediano do gancho:   topo {a['top_words']} palavras  "
          f"contra fundo {a['bottom_words']} palavras", file=out)
    print(f"  sem fórmula:                 {a['unclassified']} de {a['n']}. Leia essas à mão: "
          "é onde mora uma fórmula que você ainda não tem.", file=out)
    print("\n  Lote coletado à mão é indício, não prova. Doze reels não mostram nada;\n"
          "  quarenta em seis contas mostram alguma coisa. Colete mais antes de acreditar.\n"
          "  Atenção: sem login, o 'gancho' costuma ser a primeira linha da legenda, não a fala.\n",
          file=out)


def to_markdown(a):
    lines = ["# Arquivo de referências (swipe)", "",
             f"{a['n']} reels em {a['accounts']} contas. Ordenados pelo múltiplo sobre a {a['baseline']}.", ""]
    for r in a["reels"]:
        mult = f"{r['outlier']:.1f}x" if r["outlier"] else "?"
        lines += [f"## {mult}  {r['formula']}  ({r.get('account', '')})",
                  f"- views: {r['views']:,}  base: {r['baseline']:,}",
                  f"- nota do gancho: {r['hook_score']}  palavras: {r['words']}",
                  f"- gancho: \"{r['hook']}\"", ""]
    return "\n".join(lines) + "\n"


def main():
    P.utf8_stdio()
    ap = argparse.ArgumentParser(description="Ranqueia reels coletados pelo múltiplo sobre a mediana.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo TSV, ou - para stdin")
    ap.add_argument("--hooks", default=HOOKS, help="caminho do hooks.pt.json")
    ap.add_argument("--out", help="grava também o arquivo de referências em markdown aqui")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    rows = read_rows(args.input)
    if not rows:
        print("nenhuma linha utilizável. Precisa de um TSV com pelo menos views e gancho.", file=sys.stderr)
        sys.exit(2)
    formulas = load_formulas(args.hooks)
    a = analyse(rows, formulas)
    if not formulas:
        print("aviso: hooks.pt.json não encontrado, fórmulas sem nome. Use --hooks.", file=sys.stderr)

    if args.json:
        print(json.dumps(a, indent=2, ensure_ascii=False))
    else:
        render(a)
    if args.out:
        path = os.path.expanduser(args.out)
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        open(path, "w", encoding="utf-8").write(to_markdown(a))
        print(f"gravado em {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
