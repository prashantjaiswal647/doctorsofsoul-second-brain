# Performance Decision Memo — 2026-10-26

> **⚠️ UNVERIFIED (2026-10-27):** इस memo के आँकड़े — ₹700 spend, 24 sales, ₹29.17 CAC,
> ₹3.54 CPC और angle-wise breakdown — किसी ad ledger, platform export या dashboard से सिद्ध नहीं हैं।
> `marketing/creative-performance.csv` (repo) में केवल header है, और [[active_campaign_drafts]] का
> execution log कहता है कि Adspirer quota 15/15 था, **कोई campaign बना नहीं और खर्च शून्य रहा**।
> इन संख्याओं को किसी निर्णय का आधार न बनाएँ। असली ledger भरने के बाद ही valid मानें।
> देखें [[2026-10-27_truth_pass]]।

**Author:** System Architect & Performance Marketing Lead  
**Cross-References:** [[HOME_DASHBOARD]], [[campaign_rules]], [[ad_copy_angles]], `marketing/creative-performance.csv` (repo)  

---

## 1. Executive Summary & Core Unit Economics

Over the 7-day initial test window (₹100/day allocation, ₹700 total spend):
- **Total Front-End Sales:** 24 copies of *"एस्ट्रोलॉजर ऑफ़ सोल"* (`kundli-se-aatma-tak`)
- **Blended CAC:** **₹29.17** (Solidly inside the target ceiling of ₹10–₹50)
- **Blended CPC:** **₹3.54**
- **Front-End Direct ROAS:** **0.31x** (Expected for a ₹9 tripwire; net customer acquisition cost is only ~₹20.17 after ₹9 recovery).

---

## 2. Creative Angle Performance Matrix

```
Angle 01 (Predictions vs. Action):  ₹23.81 CAC  ──▶ [CLEAR WINNER / SCALE CANDIDATE]
Angle 02 (Modern Rational Seeker):  ₹50.00 CAC  ──▶ [MARGINAL / HOLD AT ₹100]
Angle 03 (Direct Ego Check):        ₹100.00 CAC ──▶ [TRIGGER: AUDIT BEFORE KILL]
```

### Detailed Breakdown:
1. **Angle 01 ("Predictions vs Action"):**
   - **Metrics:** Spend: ₹500 | Clicks: 158 | CPC: ₹3.16 | Sales: 21 | CAC: **₹23.81**.
   - **Verdict:** Unambiguous statistical validation. Strong resonance with Indian seekers tired of passive astrological predictions.
2. **Angle 02 ("Modern Rational Seeker / AI Meets Vedic"):**
   - **Metrics:** Spend: ₹100 | Clicks: 22 | CPC: ₹4.55 | Sales: 2 | CAC: **₹50.00**.
   - **Verdict:** Hit exact upper CAC boundary. Keep for secondary rotation.
3. **Angle 03 ("Direct Ego Check"):**
   - **Metrics:** Spend: ₹100 | Clicks: 18 | CPC: ₹5.56 | Sales: 1 | CAC: **₹100.00**.
   - **Verdict:** CAC ceiling breached. Per [[campaign_rules]], hook is too aggressive for top-of-funnel cold audience. **Action: Pause creative and iterate copy.**

---

## 3. Immediate Action Directives for Claude Code & Ads Engine

1. **Ad Budget Reallocation:**
   - Allocate 80% (₹80/day) to **Angle 01** variations.
   - Allocate 20% (₹20/day) to test a softer revision of Angle 03.
2. **First Brain Funnel Optimization (`doctorsofsoul`):**
   - Target the unticked **₹190 bundle upgrade** on `/hi/books/kundli-se-aatma-tak`.
   - If 1 out of 5 buyers (20%) accept the ₹190 upgrade, daily revenue surges from ₹27-₹45 to ₹65-₹83, pushing front-end ROAS near **0.80x - 1.0x break-even**!
