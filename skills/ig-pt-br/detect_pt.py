#!/usr/bin/env python3
"""
detect_pt.py - painel de cinco checagens que mede o quanto um texto em
portugues parece escrito por maquina. Versao em portugues de ig-human/detect.py
(instagram-agent-skill, Jake Schincariol, MIT). Ver NOTICE.md.

O QUE E: cinco heuristicas locais (variacao do tamanho das frases, concretude,
vocabulario de enchimento, marcas tipograficas e voz), calculadas no seu
computador, so a partir do texto. Nada e enviado para lugar nenhum.

O QUE NAO E: GPTZero, Originality, Copyleaks ou Turnitin. Nao chama nenhuma API
deles e nao promete o veredito deles.

ATENCAO: os limites das notas (variacao 0,22 a 0,70; 4 termos por 100 palavras
etc.) foram herdados do original e calibrados em ingles. Em portugues servem
como regua de comparacao entre rascunhos ("antes e depois"), nao como nota
absoluta. Dois checks nao dependem de idioma e sao confiaveis: FINGERPRINT
(caracteres invisiveis, travessao, aspas curvas) e a variacao de frases.

Cada checagem devolve nota HUMANA de 0 a 100. Mais alto e melhor.

Uso
  python detect_pt.py rascunho.txt
  python detect_pt.py antes.txt depois.txt      # compara dois rascunhos
  python detect_pt.py rascunho.txt --json
"""

import argparse
import json
import os
import re
import statistics
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ptlib as P  # noqa: E402

LEX = os.path.join(HERE, "slop.pt.json")

SENT_RE = re.compile(r"[^.!?\n]+[.!?]*")
WORD_RE = re.compile(r"[\w']+", re.UNICODE)
# Contracoes e fala solta do portugues falado.
CONTRACTIONS = re.compile(
    r"\b(?:pra|pro|pras|pros|tá|ta|tô|to|tava|tamo|né|cê|num|numa|dum|duma|vc|vcs|tbm|mto|pq|a gente)\b",
    re.IGNORECASE)
PRONOUNS = re.compile(
    r"\b(?:eu|me|meu|minha|meus|minhas|mim|comigo|nós|nos|nosso|nossa|a gente|você|voce|vc|seu|sua|seus|suas|te|cê)\b",
    re.IGNORECASE)
NUMBERS = re.compile(r"\b\d[\d.,]*%?\b|R\$\s?\d")
PROPER = re.compile(r"(?<![.!?]\s)(?<!^)\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]{2,}\b", re.MULTILINE)

CHECKS = ["BURSTINESS", "SPECIFICITY", "SLOP DENSITY", "FINGERPRINT", "VOICE"]
LABEL = {"BURSTINESS": "VARIAÇÃO", "SPECIFICITY": "CONCRETUDE", "SLOP DENSITY": "ENCHIMENTO",
         "FINGERPRINT": "MARCAS", "VOICE": "VOZ"}
VERDICT = {"PASS": "PASSA", "REVIEW": "REVISAR", "FLAGGED": "SINALIZADO"}


def clamp(n):
    return max(0.0, min(100.0, n))


def scale(value, human, machine):
    if human == machine:
        return 50.0
    return clamp((value - machine) / (human - machine) * 100)


def sentences(text):
    return [s.strip() for s in SENT_RE.findall(text) if len(s.split()) > 2]


def words(text):
    return WORD_RE.findall(text)


def check_burstiness(text):
    lens = [len(s.split()) for s in sentences(text)]
    if len(lens) < 4:
        return 50.0, "curto demais para julgar"
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0
    return scale(cv, human=0.70, machine=0.22), f"variação {cv:.2f} em {len(lens)} frases (ideal: 0,55+)"


def check_specificity(text):
    w = words(text)
    if len(w) < 25:
        return 50.0, "curto demais para julgar"
    per100 = 100 / len(w)
    hits = len(NUMBERS.findall(text)) + len(set(PROPER.findall(text)))
    density = hits * per100
    return scale(density, human=6.0, machine=0.5), f"{hits} marcadores concretos, {density:.1f} por 100 palavras (ideal: 4+)"


def check_slop(text, lex):
    w = words(text)
    if not w:
        return 50.0, "vazio"
    hits, found = 0, []
    for entry in lex["words"] + lex["phrases"]:
        pattern = re.compile(r"\b" + re.escape(entry["find"]).replace(r"\ ", r"\s+") + r"\b", re.IGNORECASE)
        n = len(pattern.findall(text))
        if n:
            hits += n
            found.append(entry["find"])
    # estruturas sinalizadas tambem contam como enchimento (regex do lexico)
    for s in lex["structures"]:
        if s["id"] in ("vocabulario-ia", "preambulo", "saudacao", "isca-seguir", "isca-marcar", "sabia-que",
                       "mundo-cada-vez", "fecho-resumo"):
            try:
                n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
            except re.error:
                continue
            if n:
                hits += n
                found.append(s["id"])
    density = hits * 100 / len(w)
    detail = f"{hits} termos de enchimento, {density:.1f} por 100 palavras"
    if found:
        detail += " (" + ", ".join(sorted(set(found))[:4]) + (", ..." if len(set(found)) > 4 else "") + ")"
    return scale(density, human=0.0, machine=4.0), detail


def check_fingerprint(text):
    invisible = sum(1 for c in text if unicodedata.category(c) == "Cf")
    em = text.count("—")
    curly = sum(text.count(c) for c in "‘’“”")
    ellip = text.count("…")
    nbsp = sum(text.count(c) for c in "   ")
    total = invisible * 4 + em * 2 + curly + ellip + nbsp
    per1k = total * 1000 / max(len(text), 1)
    detail = (f"{invisible} invisíveis, {em} travessão, {curly} aspas curvas, "
              f"{ellip} reticências, {nbsp} espaço rígido")
    return scale(per1k, human=0.0, machine=12.0), detail


def check_voice(text, lex):
    w = words(text)
    if len(w) < 25:
        return 50.0, "curto demais para julgar"
    per100 = 100 / len(w)
    contractions = len(CONTRACTIONS.findall(text)) * per100
    person = len(PRONOUNS.findall(text)) * per100
    tells, names = 0, []
    for s in lex["structures"]:
        try:
            n = len(re.compile(s["regex"], re.MULTILINE).findall(text))
        except re.error:
            continue
        if n:
            tells += n
            names.append(s["id"])
    bullets = [len(b.split()) for b in re.findall(r"(?m)^\s*[-*•]\s+(.+)$", text)]
    uniform = (len(bullets) >= 3 and statistics.pstdev(bullets) < 1.6)
    score = (scale(contractions, human=3.0, machine=0.0) * 0.35
             + scale(person, human=8.0, machine=1.0) * 0.35
             + clamp(100 - tells * 22) * 0.30)
    if uniform:
        score -= 12
        names.append("lista-uniforme")
    detail = (f"{contractions:.1f} contrações/fala solta, {person:.1f} pronomes pessoais "
              f"por 100 palavras, {tells} marca(s) de estrutura")
    if names:
        detail += " [" + ", ".join(names[:4]) + "]"
    return clamp(score), detail


def run(text, lex):
    results = {
        "BURSTINESS": check_burstiness(text),
        "SPECIFICITY": check_specificity(text),
        "SLOP DENSITY": check_slop(text, lex),
        "FINGERPRINT": check_fingerprint(text),
        "VOICE": check_voice(text, lex),
    }
    scores = [results[c][0] for c in CHECKS]
    overall = statistics.mean(scores) * 0.6 + min(scores) * 0.4
    verdict = "PASS" if overall >= 70 and min(scores) >= 55 else ("REVIEW" if overall >= 50 else "FLAGGED")
    return results, overall, verdict


def bar(score, width=24):
    filled = round(score / 100 * width)
    return "#" * filled + "." * (width - filled)


def render(results, overall, verdict, label=None, out=sys.stdout):
    title = "PAINEL DE CARA DE IA" + (f"  -  {label}" if label else "")
    print("\n" + title, file=out)
    print("=" * max(len(title), 62), file=out)
    for name in CHECKS:
        score, detail = results[name]
        print(f"  {LABEL[name]:<12} {bar(score)} {score:5.1f}", file=out)
        print(f"  {'':<12} {detail}", file=out)
    print("-" * 62, file=out)
    print(f"  {'NOTA HUMANA':<12} {bar(overall)} {overall:5.1f}   {VERDICT[verdict]}", file=out)
    if verdict != "PASS":
        weakest = min(CHECKS, key=lambda c: results[c][0])
        print(f"\n  Sinal mais fraco: {LABEL[weakest]}. Arrume esse primeiro.", file=out)
    print("", file=out)


def main():
    P.utf8_stdio()
    ap = argparse.ArgumentParser(description="Mede o quanto um texto em português parece escrito por máquina.")
    ap.add_argument("input", nargs="?", default="-", help="arquivo, ou - para stdin")
    ap.add_argument("compare", nargs="?", help="segundo arquivo, para mostrar antes/depois")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--lexicon", default=LEX)
    args = ap.parse_args()

    lex = json.load(open(args.lexicon, encoding="utf-8"))
    read = lambda p: sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read()

    targets = [(args.input, read(args.input))]
    if args.compare:
        targets.append((args.compare, read(args.compare)))

    payload = []
    for name, text in targets:
        results, overall, verdict = run(text, lex)
        payload.append({
            "source": name,
            "checks": {k: {"score": round(v[0], 1), "detail": v[1]} for k, v in results.items()},
            "human_score": round(overall, 1),
            "verdict": verdict,
        })

    if args.json:
        print(json.dumps(payload if args.compare else payload[0], indent=2, ensure_ascii=False))
        return

    for (name, text), p in zip(targets, payload):
        results, overall, verdict = run(text, lex)
        render(results, overall, verdict, label=os.path.basename(name) if args.compare else None)
    if args.compare:
        a, b = payload
        delta = b["human_score"] - a["human_score"]
        print(f"  {a['human_score']:.1f} {VERDICT[a['verdict']]}  ->  "
              f"{b['human_score']:.1f} {VERDICT[b['verdict']]}   ({delta:+.1f})\n")

    sys.exit(0 if payload[-1]["verdict"] == "PASS" else 1)


if __name__ == "__main__":
    main()
