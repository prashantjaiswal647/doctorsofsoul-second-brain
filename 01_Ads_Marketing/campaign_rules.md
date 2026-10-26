# Campaign Operational Rules & Decision Framework

**Status:** ACTIVE & RATIFIED (Multi-Tier Architecture)  
**Parent Blueprint:** [[funnel_architecture]] | [[HOME_DASHBOARD]]  

---

## 🏛️ TIER A: Direct 1:1 Clarity Session Campaign (High-Ticket / Consultation)
*Governs Direct Bookings at `doctorsofsoul.co.in/hi/meeting`*

### 1. Budget & Allocation
- **Daily Test Budget:** **₹500 / angle / day**
- **Concurrent Active Angles:** Max 2 angles (Advaita/Nervous System vs. Roadmap 2027)

### 2. Hard-Kill Protocol (Downside Protection)
- **Hard-Kill Trigger:** Any ad set reaching **₹500 cumulative spend with 0 confirmed session bookings** is **AUTOMATICALLY PAUSED**.
- **No manual extension** without creative angle overhaul.

### 3. Scaling Engine (Upside Capture)
- **Qualification Criteria:**
  - **CAC (Cost per Booking) < ₹350 INR**
  - **ROAS > 1.5x** (Accounting for 1:1 consultation fees and backend masterminds)
- **Scale Increment:** **+20% daily budget increase** allowed every 48 hours as long as CAC holds below ₹350.

---

## 📦 TIER B: Front-End ₹9 Tripwire Book Campaign (Mass Top-of-Funnel)
*Governs "एस्ट्रोलॉजर ऑफ़ सोल" at `doctorsofsoul.co.in/hi/books/kundli-se-aatma-tak`*

### 1. Budget & Allocation
- **Daily Discovery Budget:** **₹100 / day** total (Lean Testing)

### 2. "Audit Before Kill" Protocol
- **Trigger:** Spend reaches **₹100 with 0 book sales**.
- **Diagnostic Tree:**
  - If Link CTR >= 1.5% and CPC <= ₹4: Ad copy is working; inspect landing page / Razorpay drop-off.
  - If Link CTR < 1.0%: Hook failure; replace text overlay in [[ad_copy_angles]].
  - Hard Stop: Pause only if cumulative spend reaches ₹200 with 0 conversions.

### 3. Target Economics
- **Target CAC:** ₹10.00 – ₹30.00 INR (Hard ceiling ₹50 INR).
- **Backend Ascension:** ₹190 Bundle completion + 1:1 meeting booking.

---

## 🤖 Directives for Claude Code & Cloud Automation
1. When evaluating campaigns directed to `/hi/meeting`, apply **Tier A Rules** (₹500 kill / ₹350 CAC scale).
2. When evaluating campaigns directed to `/hi/books/*`, apply **Tier B Rules** (₹100 test / ₹10–₹50 CAC).
3. Always update [[ad_spend_logs.csv]] before triggering any scale/pause decision.
