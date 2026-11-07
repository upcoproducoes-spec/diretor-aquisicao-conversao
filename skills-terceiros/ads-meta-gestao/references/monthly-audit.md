# Monthly audit — Meta Ads

A reduced checklist for the end-of-month report. Inspired by the Meta M01-M32 matrix
in `AgriciDaniel/claude-ads` (MIT): same idea, tuned for real-estate lead-gen
with an instant form.

**Statuses:** `pass` · `fail` · `unknown` · `n/a`.
**`unknown` when the proof is missing**, never `pass` by deduction. An `unknown` doesn't
lower the score but must be written down, with what's needed to close it. `n/a` only with the
reason (e.g. "instant form only, no website").

Proof = output of a command (`status`, `numbers`, `leads.csv`) or a screenshot from
{{OWNER}}, with a date. It's cited next to the status.

---

## Tracking

| # | Check | pass if | proof |
|---|---|---|---|
| T1 | Pixel/dataset | installed on the domain and receiving `Lead` in the last 7 d · `n/a` if instant form only | Events Manager (screenshot) |
| T2 | CAPI | active, deduplicates `event_id` with the pixel · `n/a` as T1 | Events Manager |
| T3 | Verified domain | the `link` domain is verified in the portfolio | Brand safety (screenshot) |
| T4 | Conversion defined | "qualified lead" written in `account.md` + numeric TCPL | `account.md` |

## Account

| # | Check | pass if | proof |
|---|---|---|---|
| A1 | Healthy account | ACTIVE, payment method present, cap set, IG connected | `status` |
| A2 | Spend within plan | spent ≤ the month's budget, no day above `ADS_MAX_DAILY_EUR` × 1.75 | `numbers --level campaign` + `api-log.md` |
| A3 | Every move with an ok | every POST in `api-log.md` has a matching ok in `daily-log.md` | the two logs |
| A4 | Rejected ads | 0 open `DISAPPROVED` / `WITH_ISSUES` | `ad-status` |

## Creatives

| # | Check | pass if | proof |
|---|---|---|---|
| C1 | Format variety | at least 2 formats active in the month, at least 1 9:16 video | `status` + TOML |
| C2 | Angle variety | at least 3 angles tested in the month | TOML / `ads-matrix.md` |
| C3 | Fatigue | no active ad with freq > 2.5 (cold) or CTR −20% from peak without a replacement ready | `numbers --days 7` vs `--days 30` |
| C4 | Hook | every active video with hook% ≥ 15 | `numbers` |
| C5 | Concentration | no ad > 80% of leads **without** a variant in the queue (the case study: A3 86%, no variant produced) | `numbers` + queue |
| C6 | Replacements | 1-2 creatives ready, paused | `status` |
| C7 | Content rules | verified claims, AI disclosure, no prices if forbidden | the client's rules |

## Form and leads

| # | Check | pass if | proof |
|---|---|---|---|
| L1 | Form | Higher intent + reachable privacy URL + ≥ 1 qualifying question | TOML + opening the URL |
| L2 | Form signal | no option chosen by > 80% (the case study: "Both" 88/101 → fail) | `leads.csv` |
| L3 | Uncontacted leads | 0 in `open-leads` | `open-leads` |
| L4 | Response time | median `contacted_at − received` ≤ 1 h | `leads.csv` |
| L5 | Right channel | those who asked for WhatsApp/Call contacted on that channel ≥ 80% | `leads.csv` (`preferred_contact` vs `channel`) |
| L6 | Outcomes tracked | ≥ 80% of leads contacted > 3 d ago have an `outcome` | `leads.csv` |
| L7 | Quality | `call`+`serious`+`visit` leads ≥ 5% of leads · `unknown` if L6 fails | `leads.csv` |

---

## Format in the report

```
Audit 2026-MM · 18 checks · pass 11 · fail 3 · unknown 2 · n/a 2
FAIL  L2 form with no signal (88% "Both") → add a ready/off-plan question
FAIL  L5 WhatsApp requested 24, contacted via WhatsApp 1 → reply rule
UNKN  L7 quality: outcomes missing on 64 leads → track from now on
```

`fail`s first, each with **one** action. Then the `unknown`s with what's needed.
The `pass`es only as a count.
