# 2026-10-27 — Truth Pass (verified status)

**Status:** CURRENT as of 2026-10-27. Numbers here were checked against the live site and Git, not copied from older notes.
**Repo copy:** `docs/CURRENT-STATUS-2026-10-27-HI.md` was planned but is not in the repo; this note is the current status.

Cross-references: [[HOME_DASHBOARD]], [[campaign_rules]], [[active_campaign_drafts]], [[funnel_architecture]], [[campaign_v2_plan_2026-10-27]].

---

## 1. Verified live facts

| Item | Verified value |
|---|---|
| Site | https://doctorsofsoul.co.in — `/hi` 200 |
| Payments | Razorpay **live** (`payment_mode: razorpay`, production) |
| Razorpay Live webhook | **delivery observed 2026-10-24 (owner screenshots)** — only `payment.captured` and `order.paid` evidenced |
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
- SEO/UTM branch `fix/technical-seo-and-utm`, head `a0a87eb` (local, not pushed): preserves `utm_*`/`fbclid`/`gclid` through book redirects, adds sitemap/robots/canonical/hreflang/JSON-LD, and removes the proxy's site-wide `noindex` on `/hi` and `/en`.
- Frontend: 55/55 tests pass, `tsc` clean, production build passes.
- Backend: 686 tests collect; representative subset 144 passed + 1 xfailed. Full local suite did not finish on Windows — CI is the proof, not a green claim.

## 4. Unverified or contradicted claims

1. **[[2026-10-26_decision_memo]] is UNVERIFIED.** ₹700 spend, 24 sales, ₹29.17 CAC, CPC and angle breakdown have no ledger or platform export behind them. `ad_spend_logs.csv` has only a header. The Adspirer log says quota 15/15, **no campaigns created, zero spend**. A banner was added to the memo.
2. **₹1,000 meeting fee was wrong.** Live fee is ₹999 / $53. Fixed in [[campaign_rules]].
3. **Budget conflict RESOLVED 2026-10-27.** Owner chose Option A: ₹100/day total, Hindi Meta only, 7 days, static03 creative only. [[campaign_rules]], [[funnel_architecture]], and [[campaign_v2_plan_2026-10-27]] all updated.
4. **UTM violations.** [[active_campaign_drafts]] destinations use `utm_medium=cpc` and `utm_campaign=in_hi_funnel` / `gl_en_funnel`, which violate `docs/UTM-CONVENTION-HI.md`. They are kept as history; corrected links live in [[campaign_v2_plan_2026-10-27]].
5. **PR #59 closed 2026-10-27** (superseded by PR #61, owner decision). **PR #63 merged** (feat: campaign v2 creatives, creative registry and ledger). **PR #64 merged and deployed** (fix: technical SEO + UTM; `/sitemap.xml` 200).

## 5. What changed on 2026-10-27

- Planned a repo status page `docs/CURRENT-STATUS-2026-10-27-HI.md` (never committed).
- Corrected prices and UTM links in `marketing/ads.md`; added a historical-status banner.
- Added the UNVERIFIED banner to [[2026-10-26_decision_memo]].
- Fixed ₹1,000 → ₹999 in [[campaign_rules]].
- Prepared [[campaign_v2_plan_2026-10-27]]: 2 brand-aligned creatives, corrected UTMs, paused-only launch rules. **No campaign created, no ad spend.**
- Removed the proxy's `X-Robots-Tag: noindex, nofollow` on all `/hi` and `/en` routes (it would have de-indexed both canonical landings); regression test added first. Verified locally with the proxy active: `/admin` → `404` without the gate cookie, `/<ADMIN_PATH>` → `307 /admin`, `/hi` and `/en/meeting` send no robots header, `/sitemap.xml` → `200`.
- Annotated [[SEO_Audit_Report]] with what is fixed vs open and corrected its wrong "noindex is good practice" advice.
- No merge, deploy, payment change, DNS change or production flag change was made.

**Deploy check:** production must set `SITE_URL=https://doctorsofsoul.co.in`; otherwise canonical and sitemap URLs emit `http://localhost:3000`.

## 6. Open owner decisions

- Ad budget: ₹100/day total or ₹400/day (4 × ₹100)?
- Push/merge `fix/technical-seo-and-utm` and the ad-creatives branch.
- Meta review → `META_TRACKING_ENABLED`.
- Razorpay Live webhook delivery history.
- Any real ad campaign creation or activation.
