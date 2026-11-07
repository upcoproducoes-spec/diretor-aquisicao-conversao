---
name: ads-meta-gestao
description: The skill for running a client's Meta Ads (real estate in the EU) from setup through a month of management — budget, app/account setup, launching from TOML, daily management with a single proposal, end-of-month review. Built on top of our own client 03_ADS/pipeline/ads/ads.py (no Meta MCP). ALWAYS use it when the talk is about a client's Meta campaigns, ad numbers or metrics, lead form leads, budget, creatives to turn off/scale, a new client to connect to Meta, or the end-of-month ads report.
---

# {{BRAND}} Ads · Meta

One client = one `06-ads/` folder. One API client: `03_ADS/pipeline/ads/ads.py`.
The agent reads, calculates, proposes. {{OWNER}} presses the button.

Reference case: **a real, anonymised real-estate client** (24/09 → 14/10/2026, €242, 101 leads, CPL €2.40).
Everything we learned: [`references/case-study-lessons.md`](references/case-study-lessons.md).

---

## Golden rule

**No euro moves without a written ok from {{OWNER}}** (or from the project lead
{{OWNER}} named for that client, written in `account.md`).

- On its own: `status`, `numbers`, `leads`, `sync-leads`, `open-leads`, `mark-lead`,
  `preview`, `ad-status`, `launch --dry-run`, writing in the logs.
- Only with a written ok in chat/#ads: `launch` (without dry-run), `go`, `activate`,
  `pause`, `budget`, `delete`, `create-audience`. Even a pause is a money
  move: it changes where the budget goes.
- The ok holds **for that action, that day**. It doesn't generalise.
- Every ok and every move → `daily-log.md` (who, when, text of the ok).
- Belt and braces, always: **spending limit on the ad account** ({{OWNER}} sets it in the UI,
  the API can't exceed it) + `ADS_MAX_DAILY_EUR` in `.env` (ads.py refuses anything above).

We don't use the Meta MCPs: they give full write access to the account without our brakes.
To be reconsidered once the process is validated on 2-3 clients.

---

## Commands

```bash
A="python3 03_ADS/pipeline/ads/ads.py --client <folder>/06-ads"
$A status                                   # account, payment, cap, IG, campaigns→adsets→ads
$A numbers --days 7 --level ad              # spent impr freq CTR CPM hook% leads CPL
$A numbers --days 14 --by country|platform|placement
$A sync-leads                               # new leads → leads.csv
$A open-leads                               # who is waiting for a reply, for how many hours
$A mark-lead <email> --by {{OWNER}} --channel whatsapp --outcome serious --note "..."
$A ad-status                                # review / rejections
$A launch launch-01.toml --dry-run          # validates, doesn't create
# --- with a written ok ---
$A launch launch-01.toml                    # creates EVERYTHING PAUSED, idempotent (reuses by name)
$A go launch-01.toml --week 1               # switches on the week's campaign+adset+ads
$A pause <id> | activate <id>
$A budget <adset_id> <eur/day>              # refuses > +20% and > ADS_MAX_DAILY_EUR
```

Outcomes allowed in `leads.csv`: `replied` · `call` · `serious` · `visit` ·
`not-interested` · `no-reply` · `fake`.

---

## The 5 phases

| # | Phase | What comes out | Reference |
|---|---|---|---|
| 1 | **Budget** | monthly, daily, account cap, stop thresholds | [`budget.md`](references/budget.md) |
| 2 | **Setup** | portfolio, Live app, system user, token, `.env`, form, privacy | [`meta-setup-new-client.md`](references/meta-setup-new-client.md) |
| 3 | **Launch** | `launch-01.toml` → `--dry-run` → `launch` (paused) → previews → ok → `go` | below |
| 4 | **Daily management** | reading, one proposal, alerts, log | below |
| 5 | **End-of-month review** | audit, what to keep/drop, new content, client report | [`monthly-audit.md`](references/monthly-audit.md) · [`monthly-review.md`](references/monthly-review.md) |

### Launch — checklist
- [ ] `account.md` filled in: who approves, TCPL, cap, stop thresholds.
- [ ] TOML: `special_category = ["HOUSING"]` for homes in the EU; `special_category_countries` = **the audience's countries**; `beneficiary` + `payer` (DSA); a real `privacy_url`; external `link`.
- [ ] Ad texts checked against the client's content rules (verified claims, no prices if forbidden, AI disclosure in the caption).
- [ ] Week 1 = **max 3 ads** (3 different angles, at least 1 9:16 reel). The rest paused with `week = 2`.
- [ ] Clean `--dry-run` → `launch` → `preview <creative_id>` → send to {{OWNER}}.
- [ ] Tick "AI content" on every ad in Ads Manager (by hand, {{OWNER}}).
- [ ] Who replies to leads **within 1 h**, on which channel. Decided BEFORE the "go".
- [ ] Written ok → `go --week 1` → log.
- [ ] Then **7 days without touching anything**. First reading at 7, first decision at 14.

---

## How to read the numbers

**Gate before judging** (below it = "insufficient data", and you say exactly that):
- an ad with **< 1,000 impressions** or **spend < 2× TCPL** is not judged;
- "4 leads" is not a result: it's a sample;
- day 1 and the last day are partial (overlapping Meta windows): use 7 days.

**What to know about Meta:**
- **Learning**: Meta wants ~50 events/week per adset. At €10-15/day and a CPL
  of €2-5 we never get there: it's *learning limited* by design, not a fault.
  Don't chase it with edits: every significant edit restarts it.
- **Re-running `launch` on a live adset reopens review** of the ads (happened
  on 03/10). Only do it when it's really needed.
- Meta can spend up to **+75% of the daily budget** in one day; the week
  doesn't exceed 7× the daily budget. A €20 day on €11.50 is not an alarm.
- **Units**: `daily_budget`, `amount_spent`, `spend_cap` are in **cents**;
  insights `spend` is in **euros**. ads.py converts; by hand, check twice.
- Before every move: **ID + name** must match `status`. Never an ID from memory.

**Reading the signals (lead-gen, cold audience):**

| Signal | Diagnosis | Move |
|---|---|---|
| hook% < 15 after €15 | the first 2 s don't stop people | turn off, new hook |
| low CTR, high hook | the video holds, the promise doesn't | change text/CTA |
| high CTR, few leads | the form is the brake (intro, questions) | rework the form |
| many leads, zero serious outcomes | **downstream problem** or wrong audience | don't scale; qualification and message |
| freq > 2.5 (cold) | creative burned out, not the audience | rotate in a new execution of the same concept |
| CPM +30% in 2 wks | auction/countries more expensive, or fatigue | look at `--by country` before touching anything |
| CTR −20% from peak in 7 d | fatigue on the way | get the replacement ready |

Real-estate sector benchmarks (CPL €15-60, CTR ~3.75%) are US/global averages:
they only serve as an order of magnitude. The real reference is the client itself.

---

## Decision engine

**TCPL** = target cost per *qualified* lead (outcome `call`/`serious`/`visit`).
It's written in `account.md`. First month with no history: TCPL = 10× the form's
target CPL (in the case study 10-25% were estimated to be qualified). From the second month: real
qualified CPL of the last 30 d × 0.8. **With no TCPL written: stop and ask.**

**Active ads cap** = daily budget × 14 / (2 × TCPL), rounded down, max 4
under €15/day. Every ad must be able to spend 2× TCPL in 14 days, otherwise
it never gets out of the sample. (The case study: 11.50 × 14 / (2 × ~€24) = 3 → indeed
3 ads ran, the fourth was starved.)

**Fair-share at day 7** = (daily budget ÷ active ads) × 7 × 0.5.
An ad that spent less in 7 d = Meta discarded it → turn off and replace.
(The case study, A4: €1.82 against a fair-share of €13.40 → turned off.)

| Decision | When (all true) |
|---|---|
| **TURN OFF** | hook% < 15 after €15 · or 0 leads after 3× target CPL · or below fair-share at d7 · or CPL > 1.5× target for 3 days in a row |
| **ROTATE** | freq > 2.5 · or CTR −20% from peak in 7 d · or CPL +40% over 2 weeks with targeting unchanged → a variant of the same concept comes in (new hook), not a random concept |
| **SCALE** (+20%, then 5 days untouched) | CPL ≤ target for 2 weeks · freq < 2.5 · at least **1 serious/call outcome** in the period · 1-2 replacements ready · account cap that holds the new pace until the end of the month |
| **KEEP** | everything else. Keeping is a decision, not the absence of one |

Budget split once you go past ~€20/day: **80% scaling** (proven ads) / **20% test**
(new concepts) in separate adsets, so the proven ones don't starve the tests.
Promotion from test → scaling: ≥ 14 d, ≥ 3 qualified leads, qualified CPL ≤ TCPL.

Rules from the case study not to forget:
- 3 "serious" leads are worth more than 30 leads at €2: **quality decides scaling, CPL doesn't.**
- Never turn off without a replacement ready (exception: hook < 15%).
- Don't drop a country until there are outcomes per country (Italy: lowest CPL, dropped with no quality data).

---

## Proactive alerts (right away, not in the report)

In #ads (`node 04_ENGINEERING/discord-os/src/notify.js "msg"`) as soon as:
- a creative triggers a **TURN OFF** or **ROTATE** rule → message with a proposal;
- an ad is `DISAPPROVED` / `WITH_ISSUES` (`ad-status`);
- a lead has been waiting **> 1 h** (`open-leads`);
- account spend hits a threshold in `account.md` (early warning + stop: **don't turn things off on your own**);
- `status` shows a missing payment method, cap not set, account not ACTIVE.

If a proposal gets no answer: **repeat it once, then ask for a plain yes/no.**
Before proposing it again, re-read `status`: in the case study the agent kept proposing for days
to turn off A4, which had already been paused on 08/10.

---

## A typical day (09:00, 15 minutes)

1. `status` → `numbers --days 7` and `--days 1` → `sync-leads` → `open-leads`.
2. Re-read the last entry in `daily-log.md`: what was decided, was it done?
3. Apply the engine. **One** proposal, the most important one.
4. Write the entry in `daily-log.md` (at the top) and post in #ads.

### Daily proposal format

```
## 2026-MM-DD — morning report, no money moved
Spend: €X / cap €Y (Z%) · +€N in 24 h · day D/30
Ads (7d): A3 · spent · impr · freq · CTR · hook · leads · CPL — one line per ad
Leads: total · new in 24 h · no reply (> 1 h) · serious/call/visit outcomes out of total

**Proposal:** [precise action, with ID and number — e.g. "pause A4 (1202…0332)"]
**Why:** [the number that justifies it, against the threshold]
**If I'm wrong:** [what's lost, in how many days it shows, how to go back]
```

If no rule triggers: **Proposal: keep.** It still gets written, with the why.
Never estimated numbers: an invented number in the log is worse than an empty log.

---

## Client files (`06-ads/`)

`.env` (gitignored) · `account.md` (setup, who approves, TCPL, thresholds) ·
`launch-XX.toml` + `.ids.json` · `leads.csv` · `daily-log.md` (decisions) ·
`api-log.md` (every POST, written by ads.py) · `report-*.md`.

Lead data: stays in `leads.csv`. Never in client reports beyond the
counts, never in memory, never in knowledge files.

---

Inspiration (MIT, ideas rewritten): `coreyhaines31/marketingskills` (ads skill +
meta-decision-system: TCPL, ads cap, 80/20, d7 fair-share, fatigue bands) ·
`AgriciDaniel/claude-ads` (Meta checklist, `unknown` status without proof) ·
`mugurc/meta-ads-skill` (safe reading and writing rules).
