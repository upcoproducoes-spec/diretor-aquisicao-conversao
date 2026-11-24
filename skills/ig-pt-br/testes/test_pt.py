#!/usr/bin/env python3
"""
test_pt.py - testes da camada PT-BR do pacote ig-*.

Roda sem rede e sem dependencias:  python testes/test_pt.py
Sai com codigo 0 se tudo passou, 1 se algo falhou.

IMPORTANTE (honestidade): os ganchos de testes/ganchos_bons.txt e
ganchos_ruins.txt foram ESCRITOS por quem fez esta camada, a partir dos padroes.
Nao sao ganchos reais de criadores. O teste mostra que a camada nao cai nos
erros do original em portugues (acento, R$, "nao te contam", saudacao), e nao
prova poder de predicao. O original mediu 74 ganchos reais em ingles; aqui nao
ha medida equivalente.
"""

import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SK = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, SK)

import ptlib as P            # noqa: E402
import hookscore_pt as HS    # noqa: E402
import swipe_pt as SW        # noqa: E402
import detect_pt as DT       # noqa: E402
import humanize_pt as HZ     # noqa: E402
import caption_pt as CP      # noqa: E402
import beats_pt as BP        # noqa: E402

P.utf8_stdio()
falhas = []
passou = 0


def ok(cond, nome, detalhe=""):
    global passou
    if cond:
        passou += 1
        print(f"  ok    {nome}")
    else:
        falhas.append(nome)
        print(f"  FALHA {nome}  {detalhe}")


def lines(path):
    return [l.strip() for l in io.open(path, encoding="utf-8") if l.strip()]


# ------------------------------------------------------------ 1. ptlib
print("1. ptlib")
ok(len(P.words("Perdi R$ 18.000 por causa de uma cláusula")) == 7,
   "palavra com acento e R$ 18.000 contam certo",
   str(P.words("Perdi R$ 18.000 por causa de uma cláusula")))
ok(P.words("custou 3,14 e 1,500")[1:] == ["3,14", "e", "1500"], "decimal fica, milhar some",
   str(P.words("custou 3,14 e 1,500")))
ok("nao" in P.STAKES and "não" in P.STAKES, "vocabulário com e sem acento")
ok(P.norm("Ninguém Te Conta") == "ninguem te conta", "norm tira acento e caixa")

# ------------------------------------------------------------ 2. hookscore
print("2. hookscore_pt")
ruins = lines(os.path.join(HERE, "ganchos_ruins.txt"))
bons = lines(os.path.join(HERE, "ganchos_bons.txt"))
sr = [HS.run(h)[1] for h in ruins]
sb = [HS.run(h)[1] for h in bons]
pares = sum(1 for b in sb for r in sr if b > r)
total = len(sb) * len(sr)
frac = pares / total
ok(frac >= 0.90, f"bons ganham de ruins em >=90% dos pares ({pares}/{total} = {frac:.0%})")
abaixo50 = sum(1 for s in sr if s < 50)
ok(abaixo50 / len(sr) >= 0.80, f"80% dos ruins ficam abaixo de 50 ({abaixo50}/{len(sr)})",
   str([round(s) for s in sr]))
acima50 = sum(1 for s in sb if s >= 50)
ok(acima50 / len(sb) >= 0.80, f"80% dos bons ficam em 50 ou mais ({acima50}/{len(sb)})",
   str([round(s) for s in sb]))
_, _, _, fl = HS.run("Para de rolar o feed se você quer crescer")
ok(any("pare de rolar" in f for f in fl), "'para de rolar' é eliminatório")
_, _, _, fl = HS.run("Fala, pessoal, hoje eu vou falar sobre estratégia")
ok(len(fl) >= 2, "saudação e preâmbulo são eliminatórios", str(fl))
s_nao = HS.run("Ninguém te conta que seus primeiros 30 reels vão flopar.")[1]
ok(s_nao >= 70, f"'Ninguém te conta que…' pontua alto ({s_nao:.0f}); no original em PT dava 40", "")
s_perdi = HS.run("Perdi R$ 18.000 por causa de uma cláusula que faltou no contrato.")
ok(s_perdi[0]["ADDRESS"][0] >= 70, "primeira pessoa implícita no verbo ('perdi') não é 'terceira pessoa'")
ok(HS.run("Perdi R$ 18.000 por causa de uma cláusula")[0]["SPECIFICITY"][0] >= 75, "R$ 18.000 conta como número")

# ------------------------------------------------------------ 3. swipe / formulas
print("3. fórmulas e swipe_pt")
d = json.load(io.open(os.path.join(SK, "hooks.pt.json"), encoding="utf-8"))
formulas = SW.load_formulas(os.path.join(SK, "hooks.pt.json"))
ok(len(d["hooks"]) == 27 and len(d["classify_order"]) == 27, "27 fórmulas (26 + 1 local) e ordem completa")
errados = []
for h in d["hooks"]:
    fid, _ = SW.classify(h["example"], formulas)
    if fid != h["id"]:
        errados.append((h["id"], fid))
ok(len(errados) <= 4, f"o exemplo de cada fórmula é reconhecido por ela mesma ({27 - len(errados)}/27)",
   f"divergentes (id esperado, id achado): {errados}")
casos = {
    "Ninguém te conta que seus primeiros 30 reels vão flopar.": 3,
    "Perdi R$ 18.000 por causa de uma cláusula que faltou no contrato.": 1,
    "De onde vem a linha branca na margem?": 16,
    "Você não precisa de nicho.": 20,
    "Anatomia do dente 47": 27,
    "(sem fala) close no microscópio, legenda só emoji": 18,
    "33% dos formados nunca mais leem um livro.": 23,
    "Meus primeiros 47 reels tiveram 300 views.": 15,
    "Se seus reels têm views e nenhum seguidor, resolve.": 10,
}
for hook, esperado in casos.items():
    fid, nome = SW.classify(hook, formulas)
    ok(fid == esperado, f"'{hook[:44]}' -> #{esperado}", f"achou #{fid} {nome}")
tsv = "conta\tseguidores\tmediana\tviews\tgancho\n@a\t48000\t11000\t412000\tninguém te conta que seus primeiros 30 reels vão flopar\n@b\t2000000\t400000\t380000\tfala pessoal hoje eu vou falar de marketing\n"
tmp = os.path.join(HERE, "_tmp_swipe.tsv")
io.open(tmp, "w", encoding="utf-8").write(tsv)
rows = SW.read_rows(tmp)
os.remove(tmp)
a = SW.analyse(rows, formulas)
ok(a["reels"][0]["account"] == "@a" and a["reels"][0]["outlier"] > 30, "ranqueia pelo múltiplo sobre a mediana, não pelas views")
ok(a["reels"][0]["formula_id"] == 3, "nomeia a fórmula no ranking")

# ------------------------------------------------------------ 4. humanize
print("4. humanize_pt")
H = HZ.load_original()
lex = H.load_lexicon(os.path.join(SK, "slop.pt.json"))
sujo = "Fala, pessoal! Neste vídeo eu vou te mostrar como crescer — é simples.​ Marque alguém que precisa ver isso e siga para mais conteúdo! “Não é só técnica, é estratégia.”"
limpo, rep = HZ.humanize(sujo, lex, H)
ok("​" not in limpo, "tira caractere invisível")
ok("—" not in limpo, "tira travessão")
ok("Neste vídeo" not in limpo and "Fala, pessoal" not in limpo, "apaga preâmbulo e saudação")
ok("Marque alguém" not in limpo, "apaga isca de marcar")
ok(not re.search(r"(?m)^\s*[Ee]\s*[.!?]", limpo) and not re.search(r"\be\s*[.!?]\s*$", limpo.strip()), "não sobra 'E!' solto", repr(limpo))
ok(len(rep["structures"]) >= 1, "sinaliza 'não é só X, é Y' sem reescrever", str(rep["structures"]))
ok("é estratégia" in limpo or "estratégia" in limpo, "preserva o acento e o resto do texto", repr(limpo))
limpo2, _ = HZ.humanize("Perdi R$ 18.000 em uma cláusula, e aprendi.", lex, H)
ok("R$ 18.000" in limpo2, "não mexe em número nem em R$", repr(limpo2))

# ------------------------------------------------------------ 5. detect
print("5. detect_pt")
lex2 = json.load(io.open(os.path.join(SK, "slop.pt.json"), encoding="utf-8"))
texto = "Neste vídeo eu vou te mostrar como destravar o seu crescimento. Marque alguém que precisa ver isso e siga para mais conteúdo. Não é só técnica, é estratégia. Alavancar resultados é fundamental."
_, ov1, _ = DT.run(texto, lex2)
_, ov2, _ = DT.run(texto.replace(" — ", " ") + "​​", lex2)
r1 = DT.run(texto, lex2)[0]
ok(r1["SLOP DENSITY"][0] < 50, f"acha enchimento em português (nota {r1['SLOP DENSITY'][0]:.0f}; no original dava 100)")
r2 = DT.run(texto + "​​​", lex2)[0]
ok(r2["FINGERPRINT"][0] < DT.run(texto, lex2)[0]["FINGERPRINT"][0], "caractere invisível derruba a nota de marcas")

# ------------------------------------------------------------ 6. caption
print("6. caption_pt")
C = CP.patch(CP.load_original())
leg = "Perdi R$ 18.000 por causa de uma cláusula que faltou no contrato.\n\nSalve esse post.\n\n#odontologia #prótese #dentística #oclusão #estética #clínica"
a = C.analyse(leg, cut=125, keywords=["prótese"])
chk = {c["check"]: c["status"] for c in a["checks"]}
ok(len(a["hashtags"]) == 6, "conta hashtag com acento (#prótese)", str(a["hashtags"]))
ok(chk.get("HASHTAGS") == "FAIL", "6 hashtags passa do limite", str(chk))
ok(a["asks"] == ["salvar"], "reconhece 'salve esse post' como pedido", str(a["asks"]))
ok(chk.get("HOOK IS CONCRETE") == "PASS", "R$ 18.000 conta como concreto na janela visível")
a2 = C.analyse("Comente BLACK e eu te mando o link. Me chama no direct.", cut=125)
ok("comentar uma palavra-chave" in a2["asks"] and "chamar no direct" in a2["asks"], "pedido de palavra-chave e de direct", str(a2["asks"]))

# ------------------------------------------------------------ 7. beats
print("7. beats_pt")
B = BP.patch(BP.load_original())
roteiro = "Perdi R$ 18.000 por causa de uma cláusula.\nEu li o contrato duas vezes antes de assinar.\nA cláusula quatro dizia pagamento na aprovação.\nAprovação é sentimento. Entrega é data.\nHoje coloco essa cláusula em todo contrato e nunca mais perdi R$ 18.000."
r = B.analyse(roteiro, wpm=165, target=25)
ok(r["beats"][0]["words"] == 7, "gancho de 7 palavras (R$ 18.000 = 1 palavra)", str(r["beats"][0]["words"]))
ok(any("Loops" in n for n in r["notes"]), "acha o laço (repete 'perdi'/'R$ 18.000')", str(r["notes"][-2:]))

print(f"\n{passou} verificações passaram, {len(falhas)} falharam.")
if falhas:
    print("Falhas:", "; ".join(falhas))
sys.exit(1 if falhas else 0)
