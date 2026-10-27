# 2026-10-27 — Truth Pass (verified status)

**Status:** CURRENT as of 2026-10-27. Numbers here were checked against the live site and Git, not copied from older notes.
**Repo copy (Hindi, detailed):** `docs/CURRENT-STATUS-2026-10-27-HI.md` in the `doctorsofsoul` repo.

Cross-references: [[HOME_DASHBOARD]], [[campaign_rules]], [[active_campaign_drafts]], [[funnel_architecture]], [[campaign_v2_plan_2026-10-27]].

---

## 1. Verified live facts

| Item | Verified value |
|---|---|
| Site | https://doctorsofsoul.co.in — `/hi` 200 |
| Payments | Razorpay **live** (`payment_mode: razorpay`, production) |
| Razorpay Live webhook | **UNPROVEN** — owner must show dashboard delivery history |
| Email / Google | both `live` |
| Meeting | 15 min, **₹999** India / **$53** international, bookings open, 15-min hold |
| GA4 | `G-695DZ3HPT1` present |
| Meta Pixel | **absent** — `META_TRACKING_ENABLED` off until owner review |

## 2. Verified prices (catalogue API)

- Hindi: `kundli-se-aatma-tak` **₹9**; other Hindi singles ₹99; full Hindi library `sabhi-kitabein-hindi` **₹199**.
- English: every single **$9**; full English library `all-books-english` **$17**.
- ₹190 bundle upgrade = ₹199 − ₹9. Correct.

## 3. Code state

- `origin/main` = `802ffed` (2026-10-26).
- Ad creatives branch `feat/book-pitch-and-meeting-copy`, commit `1a5c56b`: `hindi_navratri_1x1.png`, `global_oracle_1x1.png`; **not in main**.
- SEO/UTM branch `fix/technical-seo-and-utm`, commit `055e58b` (local, not pushed): preserves `utm_*`/`fbclid`/`gclid` through book redirects, adds sitemap/robots/canonical/hreflang/JSON-LD.
- Frontend: 54/54 tests pass, `tsc` clean, production build passes.
- Backend: 686 tests collect; representative subset 144 passed + 1 xfailed. Full local suite did not finish on Windows — CI is the proof, not a green claim.

## 4. Unverified or contradicted claims

1. **[[2026-10-26_decision_memo]] is UNVERIFIED.** ₹700 spend, 24 sales, ₹29.17 CAC, CPC and angle breakdown have no ledger or platform export behind them. `ad_spend_logs.csv` has only a header. The Adspirer log says quota 15/15, **no campaigns created, zero spend**. A banner was added to the memo.
2. **₹1,000 meeting fee was wrong.** Live fee is ₹999 / $53. Fixed in [[campaign_rules]].
3. **Budget conflict is open.** [[campaign_rules]] working copy says ₹400/day (4 × ₹100); [[funnel_architecture]] and the last vault commit say ₹100/day total. Owner decision required. No number was changed.
4. **UTM violations.** [[active_campaign_drafts]] destinations use `utm_medium=cpc` and `utm_campaign=in_hi_funnel` / `gl_en_funnel`, which violate `docs/UTM-CONVENTION-HI.md`. They are kept as history; corrected links live in [[campaign_v2_plan_2026-10-27]].
5. **PR #59** looks stale (its work was superseded by merged PR #61). Closing it is a coordinator/owner decision.

## 5. What changed on 2026-10-27

- Added the repo status page `docs/CURRENT-STATUS-2026-10-27-HI.md`.
- Corrected prices and UTM links in `marketing/ads.md`; added a historical-status banner.
- Added the UNVERIFIED banner to [[2026-10-26_decision_memo]].
- Fixed ₹1,000 → ₹999 in [[campaign_rules]].
- Prepared [[campaign_v2_plan_2026-10-27]]: 2 brand-aligned creatives, corrected UTMs, paused-only launch rules. **No campaign created, no ad spend.**
- No merge, deploy, payment change, DNS change or production flag change was made.

## 6. Open owner decisions

- Ad budget: ₹100/day total or ₹400/day (4 × ₹100)?
- Push/merge `fix/technical-seo-and-utm` and the ad-creatives branch.
- Meta review → `META_TRACKING_ENABLED`.
- Razorpay Live webhook delivery history.
- Any real ad campaign creation or activation.
