#!/usr/bin/env python3
"""
auditoria_pt.py - auditoria mensal de um perfil de Instagram a partir de uma
tabela de posts (TSV). Fecha o ciclo: o que ja foi postado vira evidencia para o
plano do mes seguinte. Companheira da skill ig-audit (instagram-agent-skill,
Jake Schincariol, MIT); ver NOTICE.md. A conta aqui e nova, em portugues.

Regra que o script impoe: com menos de 30 posts, NAO ha conclusao, so hipotese.
Views brutas sao a metrica menos util; ranqueia por multiplo sobre a mediana da
propria conta e por compartilhamentos por alcance (o sinal mais forte que um
post consegue: alguem pos o nome nele).

Colunas do TSV (cabecalho obrigatorio; so data e views sao obrigatorias):
  data  formato  formula  duracao  tema  views  alcance  nao_seguidores_pct
  hold3s_pct  envios  salvamentos  comentarios  seguidores  resposta_1h
Nomes em ingles tambem servem (date, format, hook, length, views, reach, ...).

Uso
  python auditoria_pt.py posts.tsv                    # relatorio no terminal
  python auditoria_pt.py posts.tsv --out CLIENTE/instagram/auditoria-2026-11.md
  python auditoria_pt.py posts.tsv --json
"""

import argparse
import json
import os
import re
import statistics
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ptlib as P  # noqa: E402

MIN_CONCLUSAO = 30
ALIAS = {
    "data": "data", "date": "data", "formato": "formato", "format": "formato",
    "formula": "formula", "hook": "formula", "gancho": "formula",
    "duracao": "duracao", "length": "duracao", "tema": "tema", "theme": "tema",
    "views": "views", "visualizacoes": "views", "alcance": "alcance", "reach": "alcance",
    "nao_seguidores_pct": "nao_seguidores", "nonfollower": "nao_seguidores", "nao_seguidores": "nao_seguidores",
    "hold3s_pct": "hold3s", "hold3s": "hold3s", "envios": "envios", "shares": "envios", "sends": "envios",
    "compartilhamentos": "envios", "salvamentos": "salvamentos", "saves": "salvamentos",
    "comentarios": "comentarios", "comments": "comentarios", "seguidores": "seguidores",
    "follows": "seguidores", "resposta_1h": "resposta_1h",
}
NUM = ("views", "alcance", "nao_seguidores", "hold3s", "envios", "salvamentos", "comentarios", "seguidores", "duracao")


def num(v):
    v = (v or "").strip().replace("%", "")
    v = re.sub(r"(?<=\d)\.(?=\d{3}\b)", "", v).replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return None


def read(path):
    raw = sys.stdin.read() if path == "-" else open(path, encoding="utf-8").read()
    lines = [l for l in raw.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    head = [ALIAS.get(P.norm(c.strip()).replace(" ", "_"), P.norm(c.strip())) for c in lines[0].split("\t")]
    rows = []
    for line in lines[1:]:
        cells = line.split("\t") + [""] * len(head)
        r = dict(zip(head, [c.strip() for c in cells]))
        for k in NUM:
            r[k] = num(r.get(k))
        if r.get("views") is not None:
            rows.append(r)
    return rows


def ratio(a, b):
    return (a / b) if (a is not None and b) else None


def bucket(d):
    if d is None:
        return None
    return "ate 15s" if d < 15 else "15 a 30s" if d < 30 else "30 a 60s" if d < 60 else "mais de 60s"


def med(vals):
    vals = [v for v in vals if v is not None]
    return statistics.median(vals) if vals else None


def analyse(rows):
    n = len(rows)
    base = statistics.median([r["views"] for r in rows])
    for r in rows:
        r["mult"] = ratio(r["views"], base)
        r["envios_alc"] = ratio(r.get("envios"), r.get("alcance"))
        r["salv_alc"] = ratio(r.get("salvamentos"), r.get("alcance"))
        r["seg_alc"] = ratio(r.get("seguidores"), r.get("alcance"))
        r["duracao_faixa"] = bucket(r.get("duracao"))
    # nota composta: posto no multiplo + posto em envios/alcance (quando ha)
    def rank(key):
        vals = sorted([r for r in rows if r.get(key) is not None], key=lambda x: -x[key])
        return {id(r): i for i, r in enumerate(vals)}
    r1, r2 = rank("mult"), rank("envios_alc")
    for r in rows:
        a = r1.get(id(r), n)
        b = r2.get(id(r), a)
        r["posto"] = (a + b) / 2
    ranked = sorted(rows, key=lambda r: r["posto"])
    k = min(5, max(1, n // 6))
    top, bottom = ranked[:k], ranked[-k:]

    def grupos(chave):
        g = {}
        for r in rows:
            v = r.get(chave)
            if v:
                g.setdefault(v, []).append(r)
        out = []
        for v, items in g.items():
            if len(items) >= 2:
                out.append({"valor": v, "n": len(items), "mult_mediano": round(med([i["mult"] for i in items]), 2),
                            "envios_alc_mediano": (round(med([i["envios_alc"] for i in items]), 4)
                                                   if med([i["envios_alc"] for i in items]) is not None else None)})
        return sorted(out, key=lambda x: -x["mult_mediano"])

    nf, sa = med([r.get("nao_seguidores") for r in rows]), med([r["seg_alc"] for r in rows])
    diag = []
    if nf is not None and sa is not None and nf >= 40 and sa < 0.002:
        diag.append("Alcance chega a quem nao segue, mas poucos seguem: problema de PERFIL (use ig-profile), nao de gancho.")
    h_top, h_bot = med([r.get("hold3s") for r in top]), med([r.get("hold3s") for r in bottom])
    if h_top is not None and h_bot is not None and h_top - h_bot >= 15:
        diag.append(f"Retencao aos 3s separa os melhores ({h_top:.0f}%) dos piores ({h_bot:.0f}%): o gancho decide o resultado.")
    resp = [r for r in rows if r.get("resposta_1h")]
    return {
        "n": n, "mediana_views": base, "conclusivo": n >= MIN_CONCLUSAO,
        "top": top, "bottom": bottom, "k": k,
        "por_formato": grupos("formato"), "por_formula": grupos("formula"),
        "por_duracao": grupos("duracao_faixa"), "por_tema": grupos("tema"),
        "diagnostico": diag, "com_resposta_1h": len(resp),
    }


def fmt(r):
    def p(x, f="{:.1f}"):
        return f.format(x) if x is not None else "-"
    return (f"{p(r['mult'], '{:.1f}x'):>6}  {int(r['views']):>8,} views  envios/alcance {p(r['envios_alc'], '{:.2%}')}  "
            f"hold3s {p(r.get('hold3s'), '{:.0f}%')}  {r.get('formato') or '-'} | {r.get('formula') or '-'} | {r.get('tema') or '-'}  ({r.get('data') or ''})")


def render(a):
    L = []
    sel = "CONCLUSIVO" if a["conclusivo"] else f"SEM CONCLUSÃO (menos de {MIN_CONCLUSAO} posts): tudo abaixo é HIPÓTESE"
    L += [f"# Auditoria do Instagram: {a['n']} posts, mediana de {a['mediana_views']:,.0f} views", "", f"**Estado da amostra:** {sel}.", "",
          "Base de comparação: mediana de views da própria conta. Ranking por múltiplo sobre a mediana e por envios/alcance (não por views brutas).", ""]
    L += [f"## Melhores {a['k']}", ""] + [f"- {fmt(r)}" for r in a["top"]] + ["", f"## Piores {a['k']}", ""] + [f"- {fmt(r)}" for r in a["bottom"]] + [""]
    for titulo, chave in (("Por formato", "por_formato"), ("Por fórmula de gancho", "por_formula"),
                          ("Por duração", "por_duracao"), ("Por tema", "por_tema")):
        if a[chave]:
            L += [f"## {titulo} (só grupos com 2 posts ou mais)", ""]
            L += [f"- {g['valor']}: {g['n']} posts, múltiplo mediano {g['mult_mediano']}x, envios/alcance mediano {g['envios_alc_mediano']}" for g in a[chave]] + [""]
    if a["diagnostico"]:
        L += ["## O que os dados dizem", ""] + [f"- {d}" for d in a["diagnostico"]] + [""]
    L += ["## Como usar", "",
          "- Conclusão (PARAR / FAZER MAIS) só se a amostra for conclusiva e o padrão aparecer no melhor e no pior grupo.",
          "- Diferença pequena entre temas ou formatos com poucos posts é ruído. Só a diferença grande vira conclusão.",
          "- Dia e horário só se olham por último, e quase nunca são a causa.",
          "- Entregue ao `ig-plan` as conclusões e as hipóteses separadas, e registre no `log.md`.", ""]
    return "\n".join(L)


def main():
    P.utf8_stdio()
    ap = argparse.ArgumentParser(description="Auditoria mensal do Instagram a partir de uma tabela de posts.")
    ap.add_argument("input", nargs="?", default="-")
    ap.add_argument("--out", help="grava o relatório em markdown aqui")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    rows = read(args.input)
    if len(rows) < 3:
        print("poucos posts para auditar (mínimo 3, ideal 30+).", file=sys.stderr)
        sys.exit(2)
    a = analyse(rows)
    if args.json:
        slim = {k: v for k, v in a.items() if k not in ("top", "bottom")}
        slim["top"] = [fmt(r) for r in a["top"]]
        slim["bottom"] = [fmt(r) for r in a["bottom"]]
        print(json.dumps(slim, indent=2, ensure_ascii=False))
    else:
        txt = render(a)
        print(txt)
        if args.out:
            path = os.path.expanduser(args.out)
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            open(path, "w", encoding="utf-8").write(txt)
            print(f"gravado em {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
