# Campaign Operational Rules & Decision Framework

**Status:** ACTIVE & RATIFIED (Multi-Bucket Test Launch)  
**Core Mission:** Validate ₹9 Book Tripwire across GEO/Locale/Platform segments  
**Primary Conversion Asset:** *"एस्ट्रोलॉजर ऑफ़ सोल"* (`https://doctorsofsoul.co.in/hi/books/kundli-se-aatma-tak`)  
**Cross-References:** [[HOME_DASHBOARD]], [[icp_consciousness_ladder]], [[active_campaign_drafts]]  

---

## 1. Budget Discipline & Testing Window (Strict 10-Day Lockdown)
- **Total Daily Ad Spend:** Strictly **₹400 / day** (₹100 per bucket, total).
- **Mandatory Discovery Window:** **10 Days Minimum** (2026-10-26 to 2026-11-05).
  - Claude Code or any automation is **FORBIDDEN** from increasing or changing the budget during this 10-day period.
  - The objective is pure data collection, audience discovery, and creative angle testing across buckets.
- **Budget Scaling Gate:**
  - Any budget increase will ONLY be considered **after day 10**, post-analysis of real conversion rates, CPC, and checkout drop-offs.

---

## 2. Multi-Bucket Test Matrix (4 x ₹100/day = ₹400/day Total)

This matrix enforces strict isolation and budget caps for each test bucket.

### 2.1 IN_HI_META (India / Hindi / Meta Ads)
- **Daily Cap:** ₹100
- **Target Audience:** India, Hindi-speaking, Meta platforms.
- **Conversion Goal:** ₹9 Book Purchase (kundli-se-aatma-tak)

### 2.2 IN_HI_GOOGLE (India / Hindi / Google Ads)
- **Daily Cap:** ₹100
- **Target Audience:** India, Hindi-speaking, Google platforms.
- **Conversion Goal:** ₹9 Book Purchase (kundli-se-aatma-tak)

### 2.3 GLOBAL_EN_META (USA, UK / English / Meta Ads)
- **Daily Cap:** ₹100
- **Target Audience:** USA, UK, English-speaking, Meta platforms.
- **Conversion Goal:** ₹9 Book Purchase (kundli-se-aatma-tak)

### 2.4 GLOBAL_EN_GOOGLE (USA, UK / English / Google Ads)
- **Daily Cap:** ₹100
- **Target Audience:** USA, UK, English-speaking, Google platforms.
- **Conversion Goal:** ₹9 Book Purchase (kundli-se-aatma-tak)

---

## 3. Core Funnel Mechanics: Book First, Meeting as Upsell Bonus
```
[Paid Ad: ₹400/day total, split across 4 buckets]
   │
   ▼
[Landing Page: /hi/books/kundli-se-aatma-tak] ──▶ Goal: ₹9 Book Purchase (Core Conversion)
   │
   ├── [Immediate Order Bump / Thank-You Page]
   │     └── Unticked ₹190 Bundle Upgrade + 1:1 Clarity Session Upsell (BONUS)
   ▼
[High-Potential Clients]: If someone books a 1:1 session (₹999 live fee; $53 international), it is a massive positive ROAS bonus!
```

---


## 4. Primary Conversion Tracking Hierarchy (Funnel Metrics)

This hierarchy defines the primary metrics for evaluating campaign success, shifting focus from a single book purchase to holistic funnel engagement.

- **Level 1: Page Engagement** (Scroll depth 50%+, Time-on-page > 45s).
    - **Why:** Validates the core funnel landing page's ability to capture initial audience interest and hold attention.
    - **Action:** Optimize landing page content, initial hooks, and visual design.
- **Level 2: Book Click-through** (Click to `/books/...` from the main page).
    - **Why:** Measures direct interest in the foundational book offer after initial page engagement.
    - **Action:** Optimize book presentation on the funnel page, CTA clarity, and perceived value of the ₹9 book.
- **Level 3: 1:1 Meeting Bookings** (`/meeting`).
    - **Why:** The ultimate indicator of high-intent, qualified leads, reflecting trust and deep engagement with the Doctor of Soul philosophy.
    - **Action:** Optimize the 1:1 session offer, clarity of benefits, and booking flow.

---

## 5. Downside Protection: "Audit Before Kill" Protocol
- **Trigger:** Cumulative spend on any *single bucket* reaches **₹100 with 0 sales**.
- **Action:** **DO NOT BLIND-KILL**.
  1. Inspect **Link CTR**: If CTR >= 1.5% and CPC <= ₹4, traffic is cheap and interested. Check landing page text and Razorpay checkout friction.
  2. Inspect **Hook**: If CTR < 1.0%, tweak the headline/image text in [[ad_copy_angles]].
  3. Hard Stop: Only pause if spend crosses ₹200 with 0 conversions after creative revision for that *specific bucket*.

---

## 6. Contingency Rule for 1:1 Meeting Ads (Future Only)
- Currently: **NO direct ads for 1:1 meetings.**
- If ever tested in the future for high-potential segments, the absolute hard cap is **₹200 / day maximum** (never ₹500).
