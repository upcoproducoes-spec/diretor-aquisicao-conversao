# Meta setup for a new client

How it was done in the case study (21-24/09/2026), in order. Real time: ~1 h of
clicks from {{OWNER}} + 1 agent session. **Who** column: `O` = {{OWNER}} (Meta UI,
client login, payments) · `C` = client (access, card, privacy) · `A` = agent.

Rule: **never client credentials in chat or in files**. The token lives only in `.env`.

---

## 0 · Before opening Meta

| # | What | Who |
|---|---|---|
| 0.1 | Budget and cap decided (see `budget.md`), written in `account.md` | O + A |
| 0.2 | Who replies to leads, on which channel, within 1 h | O + C |
| 0.3 | **The client's privacy policy** online at a public URL (controller, purpose "contacting you back about your request", legal basis, retention, rights, contact). If the client doesn't have one: a static page of ours (the case study: `{{CLIENT_PRIVACY_URL}}`, public repo) | A writes, C approves |
| 0.4 | External link for the lead ads (client's website or landing page) | A |
| 0.5 | `06-ads/` folder created, `.env` already covered by `.gitignore` (`git check-ignore -v 06-ads/.env`) **before** pasting the token | A |

## 1 · Business portfolio (Business Manager)

Two routes. Pick one and write it in `account.md`.

- **A · The client's portfolio, {{BRAND}} as a partner** (preferred for real clients):
  the client stays the owner of everything; they add the {{BRAND}} portfolio as a
  *partner* on the ad account, page and IG (Settings → Partners).
- **B · A portfolio created for the client with one of the client's admins** (as in the case study:
  portfolio "the case-study client", admin = the client's FB profile, {{OWNER}} with access).

| # | What | Who |
|---|---|---|
| 1.1 | Existing or new portfolio; **2FA on** for all admins | C (login) + O |
| 1.2 | {{OWNER}} added as admin, or the {{BRAND}} portfolio as a partner | C |
| 1.3 | Facebook Page inside the portfolio | O |
| 1.4 | Professional Instagram account connected to the page and the portfolio | O |
| 1.5 | **Ad account** created in the portfolio (currency EUR, time zone Europe/Rome) | O |
| 1.6 | IG connected to the ad account (Business Suite → Instagram accounts → Connected assets). `status` checks it | O, A checks |
| 1.7 | Domain verification for the link/landing page (Settings → Brand safety → Domains, DNS TXT record or meta tag) | O, A prepares the meta tag if the site is ours |

## 2 · Payment and caps

| # | What | Who |
|---|---|---|
| 2.1 | **The client's** payment method on the ad account (the case study: the client's card) | C (they enter it, never us) |
| 2.2 | **Account spending limit** = monthly budget + ~2% margin (the case study: €350) | O |
| 2.3 | "AI content" tick on every ad: done in Ads Manager, after launch | O |

## 3 · App on developers.facebook.com

One app per client (the case study: `client-ads`). No App Review or Business
Verification needed as long as we work on the portfolio's assets (managed, not self-serve).

| # | What | Who |
|---|---|---|
| 3.1 | Create app → **Business** type (Marketing API use case / "Other → Business"), connected to the client's portfolio | O |
| 3.2 | **Marketing API** product added | O |
| 3.3 | Basic settings: **privacy URL** (the one from step 0.3), category, icon | O |
| 3.4 | **Live mode**. In development, creatives get rejected | O |
| 3.5 | `META_APP_ID` in `.env` (ads.py doesn't use it, it's there for reference) | A |

## 4 · System user and token

| # | What | Who |
|---|---|---|
| 4.1 | Portfolio → Users → **System users** → new, **Admin** role (the case study: `agency-bot`) | O |
| 4.2 | Assign assets to the system user: **ad account** (full control), **page** (full control), **IG**, **app** | O |
| 4.3 | Generate token: the app from step 3, expiry **never**, permissions: `ads_management` · `ads_read` · `business_management` · `pages_read_engagement` · `pages_manage_ads` · `pages_show_list` · **`leads_retrieval`** (it was missing in the case study: without it, leads can't be read) | O |
| 4.4 | Token pasted by {{OWNER}} straight into `.env` (not in chat) | O |

## 5 · Lead ads

| # | What | Who |
|---|---|---|
| 5.1 | The **page accepts the lead ads TOS** (`facebook.com/ads/leadgen/tos`, logged in as a page admin). Without it, the form can't be created | O |
| 5.2 | The form is created by `ads.py launch` from the TOML's `[form]` block (Higher intent, `privacy_url` required) | A |
| 5.3 | At least **1 qualifying question** in the form (lesson from the case study, v3) | A proposes, O decides |

## 6 · Pixel / dataset

- Instant form only (as in the case study): **pixel not needed** for the first month. Write it in `account.md`.
- If traffic goes to a website: Events Manager → dataset/pixel on the verified domain,
  `Lead` event on the thank-you page, then **CAPI** (server or gateway) with `event_id` deduplication.
  Without a pixel, no Traffic/Conversions campaigns: they optimise for poor clicks.

## 7 · DSA (EU)

Every adset aimed at the EU must declare a **beneficiary** and a **payer**. They're written
in the TOML (`beneficiary`, `payer`) and ads.py sends them as `dsa_beneficiary` /
`dsa_payor`. The validator blocks if the beneficiary is missing. The case study: beneficiary
= the brand, payer = the person/company that pays the card.

## 8 · The client's `.env` (`06-ads/.env`)

The variables `ads.py` reads (from `load_env` / `Meta.__init__`):

```
META_APP_ID=…            # reference, not used by the code
META_ACCESS_TOKEN=…      # REQUIRED · system user token
AD_ACCOUNT_ID=act_…      # REQUIRED · with the act_ prefix
PAGE_ID=…                # if missing and the token sees only 1 page, ads.py finds it and writes it back
IG_USER_ID=…             # optional, but needed to run on IG with the client's account
ADS_MAX_DAILY_EUR=30     # engine cap, total €/day (default 30 if absent)
```

Values starting with `PASTE` = missing (ads.py stops). Open `.env`
with a plain text editor: TextEdit rewrites it and drops lines.

## 9 · Check (agent)

```bash
A="python3 03_ADS/pipeline/ads/ads.py --client <client>/06-ads"
$A status                       # ACTIVE · payment present · cap set · IG connected
$A launch launch-01.toml --dry-run
```

`status` must show: account **ACTIVE**, payment **not** "NONE", cap
**not** "NOT SET", IG listed. If any of the four is missing, setup isn't finished.

## 10 · `account.md` (agent)

Fill in: app ID, portfolio and admins, ad account, page ID, IG, system user,
who has access, **who approves spend**, pixel yes/no, conversion = what
(qualified lead = outcome `call`/`serious`/`visit`), **TCPL**, monthly budget,
account cap, stop/early-warning thresholds, spending rules, privacy link, Ads Manager link.

## 11 · Bot

The client's line in `ADS_CLIENTS` of the Discord bot (`04_ENGINEERING/discord-os`)
→ leads every 10 min, ad status every 30 min, 09:00 report in #ads.

## New account = fragile

First launch at a low budget (€10-20/day), no bursts of edits, 2FA on.
Rate limits (code 17) are frequent in the first days: ads.py waits and retries on its own.
