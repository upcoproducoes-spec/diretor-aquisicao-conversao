# Lessons from the case study — Meta Ads, September-October 2026

The first client run with `ads.py` (a real, anonymised client). Only facts from the
reports, the logs, the launch TOMLs and that campaign's `leads.csv`.

Product: two off-plan houses for sale (permit granted, still to be built) abroad.
Audience: northern Europeans + FR. One project lead on the client's side.

---

## 1 · Results

**At 12/10 (report v1, day 19):** €221.53 · 90 leads · **CPL €2.46** ·
14,964 impressions · 13,211 reach · 729 clicks · **link CTR 4.87%** · **CPM €14.80**.

**Close on 14/10 (day 21):** €242.43 · 101 leads · **CPL €2.40** · CPM €14.49 ·
16,735 impressions · average frequency 1.79 · €11.54/day on average. All 101 leads contacted.

Pre-launch estimate (research, sector benchmark): CPL €15-60, CPM €8-20.
Result: **CPL ~10 times below** the benchmark, CPM within the range.

### By creative (leads.csv, 101 leads)
| Ad | Leads | Note |
|---|---|---|
| **A3 9:16 reel "the island and the houses"** (39 s) | 86 | **86% of leads at day 13**, ~85% at close. Hook 93-95%, CTR 7-9%, freq 1.2-1.4 for the whole campaign: never burned out |
| A8 tour reel (24.5 s) | 10 | came in on 03/10, CPL €2.5-4.5 |
| A1 6-slide carousel | 4 | CPL €3.22, stopped delivering, turned off 03/10 |
| A4 drawings carousel | 1 | €1.82 / 165 impr in 7 d: Meta wasn't serving it. Paused 08/10 |
| A2 vertical post (2-card carousel) | 0 | €5 spent, CTR 2.5%, turned off 28/09 |
| A5 A6 A7 | — | never switched on |

**Lesson:** the reel wins on its own. Carousels to a cold audience, with 3 ads on €11.50/day,
get starved by the ad Meta prefers.

### By country (close)
| Country | Spend | Leads | CPL |
|---|---|---|---|
| FR | €94.46 | 42 | €2.25 |
| IT (out from 28/09) | €24.61 | 17 | **€1.45** |
| DE | €39.30 | 15 | €2.62 |
| SE | €30.08 | 14 | €2.15 (CTR 12% at d13) |
| NL | €31.57 | 7 | €4.51 |
| CH | €22.42 | 6 | €3.74 |

**Italy dropped on 28/09** (ok from {{OWNER}}, to shift the weight to the north):
CPM from ~€13 to €16-18 (**+40%**), leads/day from 8-12 to 1-7. A decision taken
with no quality data per country: we didn't know whether the Italians were worse.

### Platform
Instagram 65 leads · Facebook 36. At d13: IG CPL €2.34, FB €2.53.

### Followers (side effect, no brand campaign active)
IG 366 → 408 (+42, ~+11%). FB ~0.

### Quality — the blind spot
- Outcomes tracked only **from 06/10** (the `outcome`/`outcome_at` columns were added that day).
- At close: 36 `replied`, 1 `not-interested`, 64 with no outcome.
  **0 out of 101 classified `serious`/`call`/`visit`.**
- The only qualification on the phone: they were looking for a house **already built**, not an off-plan project.
- Form: "Which house?" → `Both` 88 out of 101 (the default answer, zero signal).
- Preferred contact: Email 76 · WhatsApp 24 · Call 1. But follow-ups went
  **99 by email**: those who asked for WhatsApp (the warmest group) got an email.
- Response time: 1 h target, repeatedly missed (leads waiting 10-43 h).

**Lesson:** a very low CPL ≠ a successful campaign. From day 7 the bottleneck
was downstream (reply, qualification), not volume. The daily report
said so for a week and proposed *keep, don't scale*: correct.

---

## 2 · Housing category (HOUSING) constraints in Europe

- Mandatory for homes for sale with an audience in the EU, **including** the brand campaign.
- Blocked: **age, gender, lookalikes**. ads.py refuses `age_min/age_max/gender` with HOUSING.
- Interests: only **Villa · Vacation home · Real estate investing · Property finder** allowed
  (tested 23/09). The destination country, luxury and travel were rejected.
- Custom audiences (page/IG engagement) allowed, but **only when created from Ads Manager**:
  via API the rule is rejected. The A4 retargeting never started because of this.
- `special_ad_category_country` = **the audience's countries**, not the property's. At the first
  launch it was `["GR"]`, then corrected to the target countries.
- Housing ads end up in the Ad Library: visible to competitors.
- Outside the EU/USA/CA (e.g. Israel, the Emirates) you can declare `NONE` and get
  targeting back, but only in a separate campaign with no European countries.

---

## 3 · API errors we hit and their fixes (now inside ads.py)

| Problem | Fix |
|---|---|
| Lead ads rejected without an external link | `link` at the top of the TOML (the client's website/landing page) |
| EU DSA: who benefits and who pays are required | `beneficiary` + `payer` → `dsa_beneficiary`/`dsa_payor`; the validator blocks if missing |
| Campaign creation rejected without the budget sharing flag | `is_adset_budget_sharing_enabled=false` always |
| Creatives rejected with the app in development | app in **Live mode** (needs the app's privacy URL) |
| Lead form can't be created | the **page must accept the lead ads TOS** |
| Leads can't be read | `leads_retrieval` permission added later, token regenerated |
| Engagement custom audience via API rejected | create them in Ads Manager, paste the IDs into the TOML |
| Rate limit (code 17 / 613 / 80004) on a new account | retry waiting 90 s × attempt, 1.2 s between writes |
| PAGE_ID gone from `.env` (TextEdit rewrites it) | ads.py finds it again via `me/accounts` if there's only one page |
| `promoted_object` immutable on an existing adset | `launch` updates only the targeting, not the object |
| Reels uploaded silent | Pixabay music edited in (loudnorm −16 LUFS), ads recreated with audio |
| Re-running `launch` on a live adset | the ads go back into review (28/09, 03/10): only do it if needed |
| "AI content" tick | not exposed: by hand in Ads Manager on every ad |
| Scheduled close via a session cron | the cron dies with the session: needs a persistent job or a manual close |

---

## 4 · The lead form, v1 → v3

**Higher intent** type (`is_optimized_for_quality`), in English,
privacy policy at `{{CLIENT_PRIVACY_URL}}`.

- **v1** (22/09): first form, created with the paused launch.
- **v2** (24/09): final copy from the client's project lead ("permitted, ready to build"); name,
  email, phone + house, **budget, timing**, preferred contact. This is the one that went live.
- **v3** (25/09, {{OWNER}}'s choice): **budget and timing removed**, house + preferred contact remain.
  The 7 ads recreated on v3 (ad-level learning restarted; the adset's didn't).

Effect: more volume, zero signal. On v2 the 2 leads from the first day had
budget and timing filled in; on v3 all the qualification moves to the first contact,
and the first contact (email) didn't qualify.

---

## 5 · Budget and governance

- Account cap **€350** set by {{OWNER}} → **€11.50/day** (350 ÷ 30) instead of the plan's €20/day.
- Campaign B · Brand (engagement, €5/day) created paused and **never switched on**: at that
  budget it took money away from leads.
- Stop thresholds decided by the client along the way: €200 → €250 ("the leads are growing"),
  with an early warning at €240. Rule: at the threshold **you alert, you don't turn things off on your own**.
- Close on the project lead's explicit ok (14/10, 23:00).
- Fine-grained delegation (27/09): length/rotation of creatives handled by the agent **within** plan and budget;
  countries and budget above the threshold always with an ok.

---

## 6 · What we'd do differently

1. **Outcomes from day 1.** `outcome` in `leads.csv` before the "go", and whoever replies
   marks it right away. Without it, no decision on country or budget holds up.
2. **Reply on the channel asked for.** WhatsApp → WhatsApp within 1 h. Who
   replies is decided before switching on.
3. **One qualifying question in the form**, not zero: for an off-plan project,
   "Ready-built or off-plan?" or the timing. Lower volume, real signal.
4. **An explicit message about "to be built"** in the ads, so as not to attract people looking for a finished house.
5. **3 ads at a time, reel first.** Cold carousels only as a test, not as the base.
6. **Don't drop a country without outcomes per country.** Italy cost 40% less.
7. **Retargeting with audiences created in Ads Manager on setup day**, not "later".
8. **Re-read `status` before every proposal**: turning off A4 was proposed again
   for days after it had already been paused.
9. **Closes and thresholds on a persistent job**, not a session cron.
10. **Final report with the same structure from day 1** (`generate-final-report.py` → generalise it).
