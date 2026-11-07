# Budget — from the client's monthly figure to the daily one

## Minimum

**€500/month of ad spend** (excluding our fee). Below that, the numbers don't get
out of the sample: in the case study €350 → €11.50/day → 3 ads at most, first decision
only at day 14. It works for a test, not for a monthly service.

## From monthly to daily

```
daily = (monthly ÷ days in the month) ÷ (1 + country fee)
```

- **Meta's DST fee from 1/07/2026**: Meta passes the digital services tax on
  to the advertiser — **IT/FR/ES +3%**, UK +2%, AT/TR +5%; DE, NL, CH none
  (source: the case study's sector research, MediaPost/eMarketer).
  It's **added on top of** the budget, not inside it. If the audience is mixed, use the expected
  share of spend per country. Check it on the first invoice.
- Round **down** to the nearest 50 cents.
- Example: €500/month, FR+DE audience half and half → 500 ÷ 30 ÷ 1.015 ≈ 16.42 → **€16.00/day**.

## Caps (belt and braces)

| Cap | Where | Value |
|---|---|---|
| Account spending limit | Meta, set by {{OWNER}} | monthly budget + ~2% |
| `ADS_MAX_DAILY_EUR` | the client's `.env`, enforced by ads.py | planned daily × 1.5, rounded (the case study: 30) |
| Ok threshold | `account.md` | above the planned daily, a written ok is needed |

Meta can spend up to **+75%** of the daily budget in one day (week ≤ 7×).
The account cap is the only brake Meta respects to the cent.

## Test / scaling split

| Daily | Structure |
|---|---|
| < €15/day | **1 campaign, 1 adset, 3 ads.** No split: splitting below €5/adset fragments learning |
| €15-30/day | 1 prospecting adset + optional retargeting at €5/day (audiences from Ads Manager) |
| > €30/day | **80% scaling** (proven ads) / **20% test** (new concepts), separate adsets |

Retargeting: only when the warm audience is big enough to spend
(the case study: postponed, never started). Brand/follow campaign: only if the budget can
carry it **on top of** the minimum for leads (the case study: created, never switched on).

## The 4 weeks

| Week | What | Moves allowed |
|---|---|---|
| **1** (d1-7) | 3 ads, 3 angles, at least 1 reel. **Nothing gets touched** | only pausing rejected ads or hook < 15% after €15 |
| **2** (d8-14) | d7: fair-share check. d14: **first real decision**. 1-2 week-2 creatives come in to replace the ones turned off | turn off / rotate |
| **3** (d15-21) | Only what worked. Scale if the engine's conditions are all true | +20%, then 5 days untouched |
| **4** (d22-end) | Pace towards the cap. Prepare the review and next month's content | keep / rotate |

Spend pace: at the end of each week, spent ≈ 25/50/75/100% of the monthly budget.
If it runs faster, say so *before* reaching the cap.

## +20% rule

- One budget increase per adset: **max +20%**, then **5 days** untouched.
  `ads.py budget` refuses anything above +20% and above `ADS_MAX_DAILY_EUR`.
- Never +30% in one move. Raising the engine cap needs a written ok + an edit to `.env`.
- Rollback: if after scaling the qualified CPL goes above 1.5× TCPL → −20/30% right away,
  2 stable weeks, then try again at +10%.
- A decrease doesn't reset learning the way a big increase does, but it's still
  a money move: written ok.

## Stop thresholds

The client may want intermediate thresholds (the case study: €200, then €250).
They're written in `account.md` with two levels:
- 🟡 **early warning** at threshold − ~€10 (about a day before);
- 🛑 **threshold**: a clear alert in #ads, the campaign is **not** turned off by the agent,
  wait for the ok.
