#!/usr/bin/env python3
"""
ptlib.py - pecas comuns da camada PT-BR do pacote ig-*.

Derivado em parte do pacote instagram-agent-skill (Jake Schincariol, MIT).
Ver NOTICE.md. Os arquivos originais do pacote NAO sao alterados: esta camada
so le deles (por caminho) ou reimplementa a logica com regras de portugues.

O que muda em relacao ao original:
  - palavras com acento ("clausula", "voce") contam como UMA palavra;
  - numero falado e escrito em portugues: "R$ 18.000", "18 mil", "tres";
  - listas de tensao, abertura fraca e imperativo em portugues;
  - comparacao sem acento: quem digita "nao" e "não" recebe o mesmo resultado.
"""

import re
import sys
import unicodedata


def utf8_stdio():
    """Terminal do Windows pode usar outra codificacao: forca UTF-8 na saida."""
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass


# Palavra: letras (com acento), digitos, $ % apostrofo e hifen.
WORD_RE = re.compile(r"R\$\d+(?:[.,]\d+)*|\d+(?:[.,]\d+)*%?|[\w$%'’-]+", re.UNICODE)

# Numero escrito: "R$ 18.000", "R$ 2 mil", "3x", "40%", "5 horas", "90 dias".
NUMBER_RE = re.compile(
    r"R\$\s?\d[\d.,]*(?:\s?(?:mil|k|milh[ãa]o|milh[õo]es))?"
    r"|\b\d[\d.,]*\s?(?:%|k\b|x\b|h\b|hrs?\b|horas?\b|mins?\b|minutos?\b|"
    r"segundos?\b|dias?\b|semanas?\b|m[eê]s(?:es)?\b|anos?\b|mil\b|reais\b)?",
    re.IGNORECASE)

# Nome proprio no meio da frase (maiuscula acentuada incluida).
PROPER_RE = re.compile(r"(?<!^)\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ][a-záéíóúâêôãõç]{2,}\b")
HASHTAG_RE = re.compile(r"(?:^|\s)#\w+")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF☀-➿]")


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def norm(s):
    """minusculas e sem acento: base de toda comparacao de vocabulario."""
    return strip_accents(s.lower())


def variants(terms):
    """conjunto com a forma acentuada e a sem acento de cada termo."""
    out = set()
    for t in terms:
        t = t.lower()
        out.add(t)
        out.add(strip_accents(t))
    return out


def words(text):
    """Palavras do texto. "R$ 18.000" e "1,500" viram uma palavra so;
    "3,14" e "12,50" (decimais) ficam como estao."""
    t = re.sub(r"(?<=\d)[.,](?=\d{3}(?!\d))", "", text)
    t = re.sub(r"R\$\s+(?=\d)", "R$", t)          # "R$ 18000" e uma palavra so
    return WORD_RE.findall(t)


def token(w):
    """token minusculo, sem acento e sem aspas, para consulta em listas."""
    return norm(w).strip("'’")


# ---------------------------------------------------------------- vocabulario

SPOKEN_NUMBERS = variants([
    "zero", "dois", "duas", "três", "quatro", "cinco", "seis", "sete", "oito",
    "nove", "dez", "onze", "doze", "treze", "quinze", "vinte", "trinta",
    "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa",
    "cem", "cento", "duzentos", "mil", "milhão", "milhões", "bilhão", "dúzia",
    "metade", "dobro", "triplo",
])
# "um" e "uma" ficam de fora de proposito: sao enchimento quase sempre.

MONEY_WORDS = variants([
    "reais", "real", "dólar", "dólares", "grana", "centavos", "milionário",
    "faturamento", "faturei", "lucro", "salário", "aluguel", "receita",
    "mensalidade", "caixa", "prejuízo",
])

# Palavras que colocam algo em jogo na linha.
STAKES = variants([
    "pare", "parar", "nunca", "jamais", "errado", "errada", "errados", "erro",
    "erros", "errei", "perdi", "perde", "perder", "perdendo", "perdeu", "custou",
    "custa", "custar", "quebrou", "quebrado", "falhou", "falha", "falhar",
    "fracasso", "flop", "flopar", "flopou", "ninguém", "nenhum", "nenhuma",
    "nada", "não", "nem", "desisti", "desistir", "demitido", "demiti",
    "apaguei", "apagar", "matou", "mata", "matar", "substituiu", "substitui",
    "cortei", "cortar", "venci", "grátis", "pago", "cobrei", "cobro",
    "contratei", "economizei", "proibido", "ilegal", "pior", "odeio", "odiei",
    "desperdício", "desperdicei", "golpe", "mentira", "menti", "mentiu",
    "verdade", "segredo", "escondido", "roubei", "roubar", "antes", "até",
    "mas", "exceto", "problema", "risco", "perigo", "aviso", "arrependo",
    "arrependi", "deveria", "ainda", "já", "só", "somente", "sem", "contra",
    "versus", "vs", "dor", "medo", "culpa", "cuidado", "atenção", "chega",
    "caro", "difícil", "impossível",
])

# Aberturas que gastam o primeiro segundo sem dizer nada (sem acento).
WEAK_OPENERS = [
    "oi", "ola", "e ai", "fala", "salve", "pessoal", "galera", "gente", "bom",
    "entao", "hoje", "basicamente", "sinceramente", "olha", "escuta", "eu queria",
    "eu quero", "um dos", "uma das", "voce ja", "voce sabia", "voce sabe",
    "neste", "nesse", "no video", "a coisa", "muita", "tem uma", "isso e",
    "como um", "sabe", "tipo", "ai", "vamos", "deixa eu", "pra comecar",
    "para comecar", "bem vindo", "bem vindos",
]

IMPERATIVES = variants([
    "pare", "roube", "rouba", "copie", "copia", "apague", "teste", "veja",
    "vê", "assista", "leia", "salve", "use", "faça", "escreva", "envie",
    "comece", "desista", "nunca", "sempre", "coloque", "rode", "confira",
    "pega", "pegue", "olha", "mande", "tire", "vire", "corte", "abra", "ligue",
    "evite", "esqueça", "repara", "perceba",
])

DEALBREAKERS = [
    (re.compile(r"^\s*(?:pare|para|parem) de (?:rolar|scrollar)|^\s*nao (?:role|scrolle)"),
     "Abre com \"pare de rolar\". Pedir atenção prova que você ainda não a mereceu."),
    (re.compile(r"\b(?:neste|nesse|no) (?:video|reels?)\b|\bvideo de hoje\b|"
                r"\bvou (?:te )?(?:mostrar|ensinar|explicar)\b|\bhoje eu (?:vou|queria|quero)\b"),
     "Preâmbulo de vídeo. Apague e abra no ganho."),
    (re.compile(r"^\s*(?:oi|ola|e ai|fala|salve|bem[- ]vindos?|bom dia|boa tarde|boa noite)\b|"
                r"^\s*(?:pessoal|galera|gente)\b"),
     "Saudação. Ninguém abriu o feed para ser cumprimentado."),
]
# hashtag e emoji sao testados no texto original (nao normalizado):
HASHTAG_MSG = "Hashtag no gancho. Hashtag vai no fim da legenda, se for."
EMOJI_MSG = "Emoji no gancho. Na tela, no tamanho do gancho, cabe palavra ou emoji, não os dois."

# Stopwords para detectar repeticao de palavra (laco) no roteiro.
STOPWORDS = variants([
    "o", "a", "os", "as", "um", "uma", "uns", "umas", "e", "ou", "mas", "se",
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas", "por",
    "pra", "para", "com", "sem", "que", "isso", "isto", "esse", "essa", "este",
    "esta", "eu", "voce", "você", "vc", "meu", "minha", "seu", "sua", "nos",
    "nós", "ele", "ela", "eles", "elas", "te", "me", "lhe", "ao", "aos", "as",
    "foi", "era", "e", "é", "sao", "são", "ser", "ter", "tem", "tinha", "ja",
    "já", "so", "só", "nao", "não", "tambem", "também", "mais", "muito", "como",
    "quando", "onde", "ai", "aí", "la", "lá", "aqui", "ali", "tudo", "todo",
    "toda", "todos", "todas", "num", "numa", "pro", "pros", "pras", "ate", "até",
])
