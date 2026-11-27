#!/usr/bin/env node
// Up pela central de estratégia: opera QUALQUER projeto da conta do Anderson e cria projetos novos.
// Usa a chave de conta de dono (UP_ACCOUNT_KEY no .env desta pasta). Para cada projeto, troca a chave da conta por uma
// chave de sessão do projeto (12 h), guardada só em .sessoes.json desta pasta. Nunca imprime chave.
//
//   node up.cjs projetos                                   lista os projetos da conta (nome, slug, id)
//   node up.cjs projeto criar "<Nome>" [slug]               cria projeto novo, já ligado à conta (só com OK do Anderson)
//   node up.cjs <slug> rotas [texto]                       rotas do Up ([DONO] = ação de dono)
//   node up.cjs <slug> <MÉTODO> v1/<rota> [corpo.json]     chama qualquer rota no projeto (GET, POST, PUT, PATCH, DELETE)
//
// Regras: ações de dono (aprovar, publicar, agendar, disparar, ligar, excluir) só quando o Anderson mandar na conversa,
// para aquela ação. DELETE: dizer antes o que sai e esperar a confirmação. Nunca em rotina agendada.
const fs = require("fs");
const path = require("path");
const DIR = __dirname;
const env = {};
try {
  for (const l of fs.readFileSync(path.join(DIR, ".env"), "utf8").split(/\r?\n/)) {
    const m = /^([A-Z0-9_]+)=(.*)$/.exec(l.trim());
    if (m) env[m[1]] = m[2].trim();
  }
} catch {}
const BASE = (env.UP_API_URL || "").replace(/\/$/, "");
const ACCT = env.UP_ACCOUNT_KEY || "";
if (!BASE || !ACCT) {
  console.error("UP_API_URL ou UP_ACCOUNT_KEY ausente no .env da central.");
  process.exit(1);
}
const CACHE = path.join(DIR, ".sessoes.json");

async function call(method, url, key, body) {
  const r = await fetch(`${BASE}/${url.replace(/^\//, "")}`, {
    method,
    headers: { authorization: `Bearer ${key}`, ...(body !== undefined ? { "content-type": "application/json" } : {}) },
    body: body !== undefined ? JSON.stringify(body) : undefined,
  });
  const text = await r.text();
  let data;
  try { data = JSON.parse(text); } catch { data = text; }
  if (!r.ok) {
    console.error(`Erro ${r.status}: ${typeof data === "string" ? data.slice(0, 500) : JSON.stringify(data)}`);
    process.exit(1);
  }
  return data;
}
const conta = (method, url, body) => call(method, url, ACCT, body);

async function projetos() {
  return (await conta("GET", "account/workspaces")).data;
}
async function sessao(slug) {
  let cache = {};
  try { cache = JSON.parse(fs.readFileSync(CACHE, "utf8")); } catch {}
  const c = cache[slug];
  if (c && Date.parse(c.expires_at) - Date.now() > 30 * 60 * 1000) return c.key;
  const w = (await projetos()).find((p) => p.slug === slug);
  if (!w) {
    console.error(`Projeto "${slug}" não está na conta. Veja: node up.cjs projetos`);
    process.exit(1);
  }
  const r = await conta("POST", "account/enter", { workspace_id: w.id });
  cache[slug] = { key: r.key, expires_at: r.expires_at };
  fs.writeFileSync(CACHE, JSON.stringify(cache));
  return r.key;
}

(async () => {
  const [a, b, c, d] = process.argv.slice(2);
  if (!a) {
    console.log(fs.readFileSync(__filename, "utf8").split("\n").filter((l) => l.startsWith("//")).join("\n"));
    return;
  }
  if (a === "projetos") {
    for (const p of await projetos()) console.log(`${p.slug}\t${p.name}\t${p.id}`);
    return;
  }
  if (a === "projeto" && b === "criar") {
    if (!c) { console.error('Uso: node up.cjs projeto criar "<Nome>" [slug]'); process.exit(1); }
    const r = await conta("POST", "account/workspaces", d ? { name: c, slug: d } : { name: c });
    console.log(`Projeto criado: ${r.name} (slug ${r.slug}, id ${r.id})`);
    return;
  }
  const slug = a;
  const key = await sessao(slug);
  if (b === "rotas") {
    const r = await call("GET", "v1/routes", key);
    const list = Array.isArray(r) ? r : r.data || r.routes || [];
    for (const x of list) {
      const line = typeof x === "string" ? x : `${x.method} ${x.url || x.path}${x.owner_only ? " [DONO]" : ""}`;
      if (!c || line.toLowerCase().includes(c.toLowerCase())) console.log(line);
    }
    return;
  }
  const method = (b || "").toUpperCase();
  if (!["GET", "POST", "PUT", "PATCH", "DELETE"].includes(method) || !c) {
    console.error("Uso: node up.cjs <slug> <MÉTODO> v1/<rota> [corpo.json]");
    process.exit(1);
  }
  const body = d ? JSON.parse(fs.readFileSync(path.resolve(d), "utf8")) : undefined;
  const out = await call(method, c, key, body);
  console.log(typeof out === "string" ? out : JSON.stringify(out, null, 2));
})().catch((e) => {
  console.error(e.message || String(e));
  process.exit(1);
});
