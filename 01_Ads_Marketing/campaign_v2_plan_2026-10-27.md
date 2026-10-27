# Campaign v2 Plan — 2026-10-27

**Status:** PREPARED — **not published, not created, zero spend.**
**Source of truth for numbers:** [[2026-10-27_truth_pass]].
**Owner-only:** every step in §7 needs the owner. Adspirer quota is 15/15 until **2026-11-19**, so no campaign can be created through it before then.

Cross-references: [[HOME_DASHBOARD]], [[campaign_rules]], [[active_campaign_drafts]], [[2026-10-27_truth_pass]].

---

## 1. What changed from the earlier drafts

| Earlier | v2 |
|---|---|
| Hook: "Your Personal Vedic Oracle Is Here" / "Stop Guessing Your Destiny" | Hook: **"Astrology can tell you the weather. You still have to sail the boat."** |
| Deity / navratri imagery | No deities, no oracle figure, no prediction promise |
| Destination: `/hi` or `/en` home | Destination: the **Kundli book page** (the ₹9 tripwire) |
| `utm_medium=cpc`, `utm_campaign=in_hi_funnel` | `utm_medium=paid`, `<lang>_<book-slug>_sales`, creative ID in `utm_content` |
| Budget unclear (₹100 vs ₹400) | Two explicit options in §5 — **owner decides**, nothing assumed |

The line is the owner's own framing: the chart describes conditions; agency stays with the reader. It fits the brand's "right understanding" position and avoids medical or fate claims.

---

## 2. Assets (committed, not live yet)

Branch: `feat/book-pitch-and-meeting-copy`, commit `d0b499c`.

- `frontend/public/ads/campaign_v2_hindi_1x1.png`
- `frontend/public/ads/campaign_v2_english_1x1.png`

Public URLs will work **only after this branch is merged and deployed**:

- https://doctorsofsoul.co.in/ads/campaign_v2_hindi_1x1.png
- https://doctorsofsoul.co.in/ads/campaign_v2_english_1x1.png

Until then, upload the local files directly in Ads Manager rather than pointing at a URL that may 404.

Design: deep indigo (#2a1a45) night sky with faint star-chart lines, warm-cream/gold serif text, small paper boat on still water. No faces, no palms, no crystal ball, no planets, no testimonials, no ratings, no watermark.

---

## 3. Hindi creative (IN_HI_META)

**Primary text (≈100 chars):**
> कुंडली मौसम बता सकती है। नाव आपको चलानी है।
> ₹9 में अपनी कुंडली ख़ुद पढ़िए — बिना डर, बिना भविष्यवाणी।

**Headline (≈18 chars):** कुंडली ₹9 में पढ़िए
**Description (≈20 chars):** ₹9 · तुरंत PDF डाउनलोड
**CTA:** अभी ख़रीदें
**Destination:**
`https://doctorsofsoul.co.in/hi/books/kundli-se-aatma-tak?utm_source=meta&utm_medium=paid&utm_campaign=hi_kundli-se-aatma-tak_sales&utm_content=campaign_v2_hindi_1x1`

---

## 4. English creative (GLOBAL_EN_META)

**Primary text (≈118 chars):**
> Astrology can tell you the weather. You still have to sail the boat.
> Read your kundli for $9 — no fear, no predictions.

**Headline (≈22 chars):** You still sail the boat
**Description (≈25 chars):** $9 · Instant PDF download
**CTA:** Shop now
**Destination:**
`https://doctorsofsoul.co.in/en/books/from-kundli-to-soul?utm_source=meta&utm_medium=paid&utm_campaign=en_from-kundli-to-soul_sales&utm_content=campaign_v2_english_1x1`

---

## 5. Budget — **OWNER DECISION 2026-10-27: Option A**

| Option | Structure | When it makes sense |
|---|---|---|
| **A (SELECTED 2026-10-27)** | **₹100/day total**, Hindi Meta only, 7 days, **static03 creative only** | Cheapest clean read on hook + landing + checkout; one variable at a time |
| **B (DEFERRED)** | **₹400/day** = 4 × ₹100 (IN_HI_META, IN_HI_GOOGLE, GLOBAL_EN_META, GLOBAL_EN_GOOGLE) | Only if the owner confirms ₹400/day and both account currencies; otherwise the four buckets cannot be compared |

Rules either way:

- Budget is a platform daily budget, not a guaranteed spend ceiling.
- Account currency is **unverified**. `100` in a USD account is not ₹100. Confirm currency before setting any number.
- No budget change for the first 7 days.
- The old note "₹1,000 session" is wrong; the live fee is ₹999 / $53.

---

## 6. Targeting and policy (create paused)

- **IN_HI_META:** India, Hindi, age 21–45, broad. No health-condition targeting, no "anxiety/depression" interest stacks.
- **GLOBAL_EN_META:** US + UK, English, age 25–45, broad.
- Objective: Sales / Purchase. Do not optimise for a custom event that is not yet verified.
- No claims of cure, treatment, guaranteed outcomes, or "know your future".
- No fake scarcity, no invented testimonials, no star ratings.
- Creative text is already inside the image; do not let the platform auto-generate additional claims.

---

## 7. Launch sequence (owner-only)

1. Owner approves branch merges/deploy (SEO branch + creatives branch).
2. Confirm each asset URL returns 200 after deploy.
3. Confirm tracking state: GA4 live; Meta Pixel still off until owner review. Decide whether to launch without pixel or wait.
4. Create campaign **PAUSED** with the exact copy, destination and budget option above.
5. Owner verifies: status PAUSED, budget, geo, language, destination URL (all four UTM parameters present), creative.
6. Owner activates. Nothing before this point spends money.
7. Adspirer path is blocked until **2026-11-19**; if the owner launches earlier, it must be done manually in Ads Manager.

---

## 8. Measurement (no invented numbers)

- Read first-party attribution in `/admin → Traffic` (source / medium / campaign / content) and purchases in `/admin`.
- GA4 is live (`G-695DZ3HPT1`). Meta conversion data is incomplete until the pixel review is done.
- Log every rupee in [[ad_spend_logs.csv]] the day it is spent. The ledger is the only accepted spend record.
- Per-creative numbers (spend, CTR, CTA clicks, orders, revenue, ROAS) go into [[creative_performance_system_2026-10-27|the creative ledger]]; the report ranks creatives inside each currency.
- Do **not** use the numbers in [[2026-10-26_decision_memo]] — they are UNVERIFIED and no campaign ever ran.
- After 7 days, decide with: spend, visits, checkout starts, purchases, upgrade acceptance, meeting bookings. Currency totals stay separate (₹ and $ are never added).

## 9. Kill / keep rules

- 0 purchases after ₹100 in one bucket: inspect link CTR and checkout before pausing (existing "Audit Before Kill" rule).
- CTR ≥ 1.5% with no sales: suspect landing/checkout, not the hook.
- CTR < 1.0%: change hook, keep the same destination.
- Pause only after ₹200 with 0 conversions and one creative revision.
- Any claim that cannot be traced to the ledger or a platform export stays out of decision notes.
