#!/usr/bin/env node
// Geração de imagem nativa do agente de Design (OpenAI gpt-image-2), para qualquer projeto, dentro ou fora do Up.
// A chave vem de OPENAI_API_KEY (ambiente), de C:\Users\User\.claude\openai.env ou do .env da pasta atual — e NUNCA é impressa.
//
//   node gerar-imagem.mjs --prompt "texto" | --prompt-file prompt.txt
//                         [--size 1024x1024|1024x1536|1536x1024|auto] [--quality low|medium|high]
//                         [--n 1..4] [--transparent] [--ref foto.jpg ...] [--out pasta/nome.png]
//
// --ref: uma ou mais imagens de referência (estiliza/edita a partir delas: ambiente, produto, esboço).
// --transparent: fundo transparente (logo, objeto recortado). Saída sempre PNG.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { dirname, resolve, basename, extname } from "node:path";
import { homedir } from "node:os";

const args = process.argv.slice(2);
const opt = (name) => {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? args[i + 1] : undefined;
};
const flag = (name) => args.includes(`--${name}`);
const many = (name) => args.flatMap((a, i) => (a === `--${name}` && args[i + 1] ? [args[i + 1]] : []));
const fail = (msg) => {
  console.error(`ERRO: ${msg}`);
  process.exit(1);
};

function readKey() {
  if (process.env.OPENAI_API_KEY) return process.env.OPENAI_API_KEY.trim();
  for (const f of [resolve(homedir(), ".claude", "openai.env"), resolve(process.cwd(), ".env")]) {
    if (!existsSync(f)) continue;
    const m = /^OPENAI_API_KEY\s*=\s*"?([^"\r\n]+)"?/m.exec(readFileSync(f, "utf8"));
    if (m) return m[1].trim();
  }
  return null;
}

const prompt = opt("prompt") ?? (opt("prompt-file") ? readFileSync(opt("prompt-file"), "utf8") : undefined);
if (!prompt || prompt.trim().length < 5) fail('informe --prompt "..." ou --prompt-file arquivo.txt');
const size = opt("size") ?? "1024x1024";
if (!["1024x1024", "1024x1536", "1536x1024", "auto"].includes(size)) fail("--size: 1024x1024, 1024x1536, 1536x1024 ou auto");
const quality = opt("quality") ?? "medium";
if (!["low", "medium", "high"].includes(quality)) fail("--quality: low, medium ou high");
const n = Number(opt("n") ?? 1);
if (!Number.isInteger(n) || n < 1 || n > 4) fail("--n de 1 a 4");
const refs = many("ref");
for (const r of refs) if (!existsSync(r)) fail(`referência não encontrada: ${r}`);
const out = resolve(opt("out") ?? `imagens-geradas/imagem-${new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19)}.png`);

const key = readKey();
if (!key) fail("sem chave da OpenAI. Crie C:\\Users\\User\\.claude\\openai.env com a linha OPENAI_API_KEY=... (cole você mesmo; nunca no chat)");

// gpt-image-2 é o atual, mas não faz fundo transparente; para logo/recorte, gpt-image-1.5.
const model = opt("model") ?? (flag("transparent") ? "gpt-image-1.5" : "gpt-image-2");
let res;
try {
  if (refs.length) {
    const form = new FormData();
    form.append("model", model);
    form.append("prompt", prompt);
    form.append("size", size);
    form.append("quality", quality);
    form.append("n", String(n));
    if (flag("transparent")) form.append("background", "transparent");
    const mime = (p) => ({ ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp" })[extname(p).toLowerCase()] ?? "application/octet-stream";
    for (const r of refs) form.append("image[]", new Blob([readFileSync(r)], { type: mime(r) }), basename(r));
    res = await fetch("https://api.openai.com/v1/images/edits", { method: "POST", headers: { authorization: `Bearer ${key}` }, body: form, signal: AbortSignal.timeout(300_000) });
  } else {
    const body = { model, prompt, size, quality, n, output_format: "png", ...(flag("transparent") ? { background: "transparent" } : {}) };
    res = await fetch("https://api.openai.com/v1/images/generations", { method: "POST", headers: { authorization: `Bearer ${key}`, "content-type": "application/json" }, body: JSON.stringify(body), signal: AbortSignal.timeout(300_000) });
  }
} catch (e) {
  fail(`não consegui falar com a OpenAI (${e && e.name === "TimeoutError" ? "tempo esgotado" : "rede"})`);
}
const data = await res.json().catch(() => null);
if (!res.ok) fail(`OpenAI recusou (${res.status}): ${String(data?.error?.message ?? "").split(key).join("[chave]").slice(0, 400)}`);
const items = data?.data ?? [];
if (!items.length) fail("a OpenAI não devolveu imagem");
mkdirSync(dirname(out), { recursive: true });
items.forEach((it, i) => {
  const file = items.length > 1 ? out.replace(/\.png$/i, `-${i + 1}.png`) : out;
  writeFileSync(file, Buffer.from(it.b64_json, "base64"));
  console.log(`OK ${file}`);
});
const u = data.usage;
if (u) console.log(`uso: ${u.input_tokens ?? "?"} tokens de entrada, ${u.output_tokens ?? "?"} de saída (modelo ${model}, ${quality}, ${size})`);
