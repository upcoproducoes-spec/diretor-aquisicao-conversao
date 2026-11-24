#!/usr/bin/env python3
"""
hookscore_pt.py - nota para a primeira linha de um Reel em portugues, nas cinco
propriedades que os ganchos fortes costumam ter, e ranking de varios ganchos.

Derivado de ig-reel/hookscore.py (instagram-agent-skill, Jake Schincariol, MIT).
Mesma ideia e mesma conta final; vocabulario, numeros e mensagens em portugues.
Ver NOTICE.md.

O QUE E: cinco heuristicas locais, calculadas so a partir do texto. Medem
propriedades que ganchos que seguram atencao costumam ter: cabe em ~2-3
segundos, tem algo concreto, tem algo em jogo, o ganho vem na frente e fala com
alguem.

O QUE NAO E: previsao de views. O autor do original testou a versao em ingles
com 74 ganchos reais: separa gancho de verdade de gancho ruim de proposito
(AUC 0,83), mas quase nao separa os acertos de um criador dos erros do mesmo
criador (AUC 0,56, moeda e 0,50). A versao em portugues NAO tem esse teste
publicado; o teste local esta em testes/test_pt.py e e pequeno. Use para barrar
gancho fraco antes de gravar e confie no grafico de retencao para escolher.

Uso
  python hookscore_pt.py ganchos.txt          # um gancho por linha, em ranking
  python hookscore_pt.py --hook "Perdi R$ 18.000 em uma clausula."
  python hookscore_pt.py ganchos.txt --json
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

CHECKS = ["LENGTH", "SPECIFICITY", "STAKES", "FRONTLOAD", "ADDRESS"]
LABEL = {"LENGTH": "COMPRIMENTO", "SPECIFICITY": "ESPECIFICIDADE",
         "STAKES": "O QUE ESTÁ EM JOGO", "FRONTLOAD": "GANHO NA FRENTE",
         "ADDRESS": "FALA COM QUEM"}
VERDICT = {"STRONG": "FORTE", "OK": "OK", "WEAK": "FRACO"}

WPS = 2.75           # ~165 palavras por minuto falado; ajuste com --wpm


def clamp(n):
    return max(0.0, min(100.0, n))


def check_length(text, wps=WPS):
    w = P.words(text)
    n = len(w)
    secs = n / wps
    chars = len(text.strip())
    if 5 <= n <= 12:
        score = 100.0
    elif n < 5:
        score = clamp(100 - (5 - n) * 20)
    else:
        score = clamp(100 - (n - 12) * 11)
    if chars > 60:                         # duas linhas de texto grande na tela
        score -= 12
    return clamp(score), f"{n} palavras, {chars} caracteres, ~{secs:.1f}s falado (ideal: 5 a 12 palavras)"


def check_specificity(text):
    nums = [n.strip() for n in P.NUMBER_RE.findall(text) if n.strip()]
    propers = set(P.PROPER_RE.findall(text))
    low = [P.token(w) for w in P.words(text)]
    spoken = [w for w in low if w in P.SPOKEN_NUMBERS or w in P.MONEY_WORDS]
    hits = len(nums) + len(propers) + len(spoken)
    score = 15.0 if hits == 0 else clamp(45 + hits * 30)
    found = ", ".join(nums[:2] + sorted(propers)[:2] + spoken[:2])
    return score, (f"{hits} marcador(es) concreto(s)" + (f": {found}" if found else
                   " - sem número, sem nome, nada verificável"))


def check_stakes(text):
    w = [P.token(x) for x in P.words(text)]
    markers = sorted(set(x for x in w if x in P.STAKES))
    if re.search(r"R?\$\s?\d", text):
        markers.append("um preço")
    n = len(markers)
    score = {0: 20.0, 1: 70.0}.get(n, 100.0)
    detail = f"{n} marcador(es) de tensão" + (f": {', '.join(markers[:4])}" if markers else
                                             " - nada está em jogo nesta linha")
    return clamp(score), detail


def _weak_opener(low):
    if not low:
        return None
    opener2 = " ".join(low[:2]) + " "
    for weak in P.WEAK_OPENERS:
        if " " in weak:
            if opener2.startswith(weak + " "):
                return weak
        elif low[0] == weak:
            return weak
    return None


def check_frontload(text):
    w = P.words(text)
    if not w:
        return 0.0, "vazio"
    low = [P.token(x) for x in w]
    weak = _weak_opener(low)
    penalty = 30 if weak else 0
    payload = None
    for i, tk in enumerate(low):
        if (tk in P.STAKES or tk in P.SPOKEN_NUMBERS or tk in P.MONEY_WORDS
                or P.NUMBER_RE.match(w[i]) or (i and P.PROPER_RE.match(w[i]))):
            payload = i
            break
    if payload is None:
        base, where = 30.0, "nenhuma palavra de ganho na linha"
    elif payload <= 3:
        base, where = 100.0, f"ganho na palavra {payload + 1}"
    elif payload <= 6:
        base, where = 70.0, f"ganho na palavra {payload + 1}, dá para adiantar"
    else:
        base, where = 40.0, f"ganho na palavra {payload + 1}, tarde demais"
    detail = where + (f"; abertura fraca \"{weak}\"" if weak else "")
    return clamp(base - penalty), detail


# Em portugues o "eu" fica implicito no verbo: "perdi", "postei", "fiz", "tenho".
_NOT_VERB_I = {"aqui", "ali", "ai", "taxi", "hi", "bi", "tri"}
_FIRST_PERSON = {"fiz", "fui", "tive", "pus", "vi", "li", "tenho", "faco", "vendo", "uso",
                 "cobro", "ganho", "gasto", "trabalho", "moro", "sou", "estou", "quero", "preciso"}


def _first_person_verb(tokens):
    for t in tokens:
        if t in _FIRST_PERSON:
            return True
        if len(t) >= 4 and t not in _NOT_VERB_I and (t.endswith("ei") or t.endswith("i")):
            return True
    return False


def check_address(text):
    n = P.norm(text)
    w = [P.token(x) for x in P.words(text)]
    if re.search(r"\b(?:voce|voces|vc|vcs|seu|sua|seus|suas|teu|tua|te|ti|contigo)\b", n):
        return 100.0, "fala com quem assiste"
    if w and (w[0] in P.IMPERATIVES or (w[0] == "para" and len(w) > 1 and w[1] == "de")):
        return 90.0, f"abre com imperativo (\"{w[0]}\")"
    if re.search(r"\b(?:eu|meu|minha|meus|minhas|me|mim|nos|nosso|nossa|a gente)\b", n) or _first_person_verb(w):
        return 70.0, "primeira pessoa, sem nomear quem assiste"
    return 35.0, "terceira pessoa, ninguém na sala"


def run(text, wps=WPS):
    results = {
        "LENGTH": check_length(text, wps),
        "SPECIFICITY": check_specificity(text),
        "STAKES": check_stakes(text),
        "FRONTLOAD": check_frontload(text),
        "ADDRESS": check_address(text),
    }
    n = P.norm(text)
    flags = [msg for pattern, msg in P.DEALBREAKERS if pattern.search(n)]
    if P.HASHTAG_RE.search(text):
        flags.append(P.HASHTAG_MSG)
    if P.EMOJI_RE.search(text):
        flags.append(P.EMOJI_MSG)
    scores = [results[c][0] for c in CHECKS]
    # A propriedade mais fraca limita o gancho: uma so basta para o dedo seguir.
    overall = clamp(statistics.mean(scores) * 0.6 + min(scores) * 0.4 - len(flags) * 15)
    verdict = "STRONG" if overall >= 70 and min(scores) >= 55 and not flags else (
        "OK" if overall >= 50 else "WEAK")
    return results, overall, verdict, flags


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render_one(text, results, overall, verdict, flags, out=sys.stdout):
    print("\nNOTA DO GANCHO", file=out)
    print("=" * 62, file=out)
    print(f"  \"{text.strip()}\"\n", file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {LABEL[name]:<19} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<19} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'NOTA':<19} {bar(overall)} {overall:5.1f}   {VERDICT[verdict]}", file=out)
    for f in flags:
        print(f"\n  ELIMINATÓRIO  {f}", file=out)
    if verdict != "STRONG":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Ponto mais fraco: {LABEL[weakest]}. Arrume esse e rode de novo.", file=out)
    print("", file=out)


def render_table(rows, out=sys.stdout):
    print("\nRANKING DE GANCHOS\n" + "=" * 78, file=out)
    for i, r in enumerate(rows, 1):
        mark = "->" if i == 1 else "  "
        hook = r["hook"] if len(r["hook"]) <= 62 else r["hook"][:59] + "..."
        print(f"{mark} {r['score']:5.1f} {VERDICT[r['verdict']]:<7} {hook}", file=out)
        print(f"        mais fraco: {LABEL[r['weakest']]} ({r['checks'][r['weakest']]['score']:.0f})", file=out)
        for f in r["flags"]:
            print(f"        eliminatório: {f}", file=out)
    print("\nGrave o primeiro. Se o primeiro tem menos de 50, nenhum destes é o gancho.\n",
          file=out)


def main():
    P.utf8_stdio()
    ap = argparse.ArgumentParser(description="Nota de gancho de Reel em portugues.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo com um gancho por linha, ou -")
    ap.add_argument("--hook", help="nota de um gancho dado na linha de comando")
    ap.add_argument("--wpm", type=float, default=165, help="palavras por minuto de fala (padrao 165)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    wps = args.wpm / 60.0

    if args.hook:
        lines = [args.hook]
    else:
        raw = sys.stdin.read() if args.input == "-" else open(args.input, encoding="utf-8").read()
        lines = [l.strip() for l in raw.splitlines() if l.strip()]
    if not lines:
        print("nada para pontuar", file=sys.stderr)
        sys.exit(2)

    payload = []
    for line in lines:
        results, overall, verdict, flags = run(line, wps)
        payload.append({
            "hook": line,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "weakest": min(CHECKS, key=lambda c: results[c][0]),
            "flags": flags,
            "score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if len(payload) > 1 else payload[0], indent=2, ensure_ascii=False))
        return
    if len(payload) == 1:
        results, overall, verdict, flags = run(lines[0], wps)
        render_one(lines[0], results, overall, verdict, flags)
    else:
        render_table(sorted(payload, key=lambda r: -r["score"]))
    sys.exit(0 if max(p["score"] for p in payload) >= 70 else 1)


if __name__ == "__main__":
    main()
