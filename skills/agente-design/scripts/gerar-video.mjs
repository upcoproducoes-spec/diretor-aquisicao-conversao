#!/usr/bin/env node
// Geração de vídeo animado do agente de Design para Reels/Stories (1080x1920): cada cena é uma ilustração da OpenAI
// (gpt-image-2, vertical) animada no ffmpeg com movimento de câmera, com narração em voz da OpenAI e legenda queimada.
// (A API de vídeo da OpenAI, Sora, foi desligada em 24/09/2026; por isso o vídeo é montado a partir de ilustrações.)
// A chave vem de OPENAI_API_KEY (ambiente), de C:\Users\User\.claude\openai.env ou do .env da pasta atual — e NUNCA é impressa.
//
//   node gerar-video.mjs --spec roteiro.json [--out pasta/video.mp4]
//
// roteiro.json:
// {
//   "style": "animação 2D estilo desenho educativo, traço limpo, fundo marfim, destaque roxo",   // vale para todas as cenas
//   "quality": "medium",                  // ilustrações: low (rascunho) | medium | high
//   "voice": "onyx",                      // voz da OpenAI (onyx, ash, alloy, echo, sage, verse...). Nunca clone de pessoa real.
//   "voice_instructions": "português do Brasil, tom de colega dentista, calmo e direto",
//   "scenes": [
//     { "seconds": 4, "prompt": "o que a ilustração mostra", "narration": "o que a voz fala",
//       "text": "texto grande na tela (opcional)", "move": "zoom|zoom-out|subir|descer (opcional)" }
//   ]
// }
// seconds de cada cena: 2 a 12. Rosto ou mãos do expert NUNCA (regra do agente de Design): use desenho, objetos, modelo de
// gesso, esquemas. O texto da tela entra por cima (ffmpeg), nunca desenhado pela IA.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from "node:fs";
import { dirname, resolve, join } from "node:path";
import { homedir } from "node:os";
import { execFileSync } from "node:child_process";

const args = process.argv.slice(2);
const opt = (name) => {
  const i = args.indexOf(`--${name}`);
  return i >= 0 ? args[i + 1] : undefined;
};
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

if (!opt("spec")) fail("informe --spec roteiro.json");
const spec = JSON.parse(readFileSync(opt("spec"), "utf8"));
const scenes = spec.scenes || [];
if (!scenes.length || scenes.length > 12) fail("de 1 a 12 cenas");
for (const [i, s] of scenes.entries()) {
  if (!(Number(s.seconds) >= 2 && Number(s.seconds) <= 12)) fail(`cena ${i + 1}: seconds de 2 a 12`);
  if (!s.prompt) fail(`cena ${i + 1}: falta o prompt`);
}
const quality = spec.quality || "medium";
const out = resolve(opt("out") ?? `videos-gerados/video-${new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19)}.mp4`);
const work = join(dirname(out), "partes-" + Date.now());
mkdirSync(work, { recursive: true });
const key = readKey();
if (!key) fail("sem chave da OpenAI. Crie C:\\Users\\User\\.claude\\openai.env com a linha OPENAI_API_KEY=... (cole você mesmo; nunca no chat)");
const auth = { authorization: `Bearer ${key}` };
const clean = (t) => String(t ?? "").split(key).join("[chave]").slice(0, 400);
const ff = (a) => execFileSync("ffmpeg", ["-y", "-loglevel", "error", ...a], { stdio: ["ignore", "inherit", "inherit"] });

async function api(path, init) {
  const res = await fetch(`https://api.openai.com/v1/${path}`, { ...init, headers: { ...auth, ...(init?.headers || {}) }, signal: AbortSignal.timeout(300_000) });
  if (!res.ok) {
    const e = await res.json().catch(() => ({}));
    fail(`OpenAI recusou ${path} (${res.status}): ${clean(e?.error?.message)}`);
  }
  return res;
}

const MOVES = (frames) => ({
  zoom: `zoompan=z='1+0.12*on/${frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'`,
  "zoom-out": `zoompan=z='1.12-0.12*on/${frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'`,
  subir: `zoompan=z='1.1':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*(1-on/${frames})'`,
  descer: `zoompan=z='1.1':x='iw/2-(iw/zoom/2)':y='(ih-ih/zoom)*on/${frames}'`,
});

async function clip(s, i) {
  const prompt = `${spec.style ? `Estilo: ${spec.style}. ` : ""}${s.prompt}. Ilustração vertical para vídeo, com espaço livre em cima e embaixo para texto. Sem textos, letras, números, legendas ou logotipos na imagem. Sem rostos nem mãos de pessoas reais.`;
  const body = { model: "gpt-image-2", prompt, size: "1024x1536", quality, n: 1, output_format: "png" };
  const data = await (await api("images/generations", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) })).json();
  const b64 = data?.data?.[0]?.b64_json;
  if (!b64) fail(`cena ${i + 1}: a OpenAI não devolveu imagem`);
  const img = join(work, `cena${i + 1}.png`);
  writeFileSync(img, Buffer.from(b64, "base64"));
  const frames = Math.round(Number(s.seconds) * 30);
  const moves = MOVES(frames);
  const move = moves[s.move] || Object.values(moves)[i % 4];
  const file = join(work, `cena${i + 1}.mp4`);
  // Sobe a resolução antes do zoompan para o movimento não tremer.
  ff(["-loop", "1", "-i", img, "-vf", `scale=2560:3840,${move}:d=${frames}:s=1280x1920:fps=30,crop=1080:1920`, "-frames:v", String(frames), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", file]);
  return file;
}

async function voice(s, i) {
  if (!s.narration) return null;
  const body = { model: "gpt-4o-mini-tts", voice: spec.voice || "onyx", input: s.narration, instructions: spec.voice_instructions || "Fale em português do Brasil, tom natural e direto.", response_format: "mp3" };
  const file = join(work, `voz${i + 1}.mp3`);
  writeFileSync(file, Buffer.from(await (await api("audio/speech", { method: "POST", headers: { "content-type": "application/json" }, body: JSON.stringify(body) })).arrayBuffer()));
  return file;
}

const FONT = "C\\:/Windows/Fonts/arialbd.ttf";
const wrap = (t, n) =>
  String(t)
    .split(/\s+/)
    .reduce((acc, w) => {
      const cur = acc[acc.length - 1];
      if (cur && (cur + " " + w).length > n) acc.push(w);
      else acc[acc.length - 1] = (cur ? cur + " " : "") + w;
      return acc;
    }, [""])
    .join("\n");
const box = (txtFile, y, size) =>
  `drawtext=fontfile='${FONT}':textfile='${txtFile.replace(/\\/g, "/").replace(":", "\\:")}':fontsize=${size}:fontcolor=white:line_spacing=10:box=1:boxcolor=black@0.6:boxborderw=24:x=(w-text_w)/2:y=${y}`;

const parts = [];
for (const [i, s] of scenes.entries()) {
  console.log(`cena ${i + 1}/${scenes.length}: gerando (${s.seconds}s)…`);
  const [v, a] = await Promise.all([clip(s, i), voice(s, i)]);
  const filters = ["setsar=1"];
  if (s.text) {
    const tf = join(work, `texto${i + 1}.txt`);
    writeFileSync(tf, wrap(s.text, 22));
    filters.push(box(tf, 120, 62));
  }
  if (s.narration) {
    const lf = join(work, `legenda${i + 1}.txt`);
    writeFileSync(lf, wrap(s.narration, 30));
    filters.push(box(lf, "h-text_h-220", 44));
  }
  const part = join(work, `parte${i + 1}.mp4`);
  const audio = a ? ["-i", a, "-map", "0:v", "-map", "1:a", "-af", `apad=whole_dur=${s.seconds}`] : ["-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-map", "0:v", "-map", "1:a"];
  ff(["-i", v, ...audio, "-vf", filters.join(","), "-t", String(s.seconds), "-r", "30", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-ar", "44100", "-ac", "2", part]);
  parts.push(part);
}
const list = join(work, "lista.txt");
writeFileSync(list, parts.map((p) => `file '${p.replace(/\\/g, "/")}'`).join("\n"));
mkdirSync(dirname(out), { recursive: true });
ff(["-f", "concat", "-safe", "0", "-i", list, "-c", "copy", "-movflags", "+faststart", out]);
const secs = scenes.reduce((t, s) => t + Number(s.seconds), 0);
console.log(`Vídeo pronto: ${out} (${secs}s, ${scenes.length} ilustrações ${quality} + voz). Lance o custo: up imagem custo gpt-image-2 1024x1536 ${quality} ${scenes.length} "video producao de conteudo"`);
