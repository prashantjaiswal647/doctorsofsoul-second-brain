# Adspirer & Cloud Code Autonomous Protocol

**Operating Mandate for Claude Code / Cloud Agent:**  
Before executing any Adspirer API call, modifying ad campaigns, or altering budgets, the agent **MUST** read and adhere strictly to the protocols defined in this document.

Cross-References: [[HOME_DASHBOARD]], [[campaign_rules]], [[funnel_architecture]], [[cross_platform_creative_brief]]

---

## 1. The Adspirer 15-Call Conservation Rule
Adspirer currently provides **15 free API calls/credits**. Every API call represents valuable operational runway and must be guarded against unnecessary polling:

- **Batch Execution Only:** Never invoke Adspirer for single-metric queries.
- **Max Call Frequency:** No more than **1 call per 24 hours** for performance telemetry pull and budget modulation.
- **Call Allocation Map:**
  - Call 1–2: Initial Campaign Creation & Pixel/URL Validation (Meta + Google).
  - Call 3–10: Daily telemetry ingest (1 call per evening to pull aggregate impressions, clicks, spend, and sales).
  - Call 11–15: Emergency pauses or scaling triggers.

---

## 2. Multi-Platform Mandate (Meta + Google Ads)
The campaign operates with a unified mission across two primary engines:

```
[Total Daily Allocation: ₹100 INR / day]
             │
   ┌─────────┴─────────┐
   ▼                   ▼
[Meta Ads (FB/IG)]   [Google Ads (Search/PMax)]
• High Impressions   • High-Intent Capture
• Low CPM Reach      • Direct Keyword Searches
• Text-Image Hooks   • "कुंडली समाधान", "मानसिक शांति"
```

### Allocation Policy:
- **Phase 1 (Discovery):** Split evenly (₹50 Meta / ₹50 Google) OR run in alternate 3-day discovery blocks to ensure statistical density without over-fragmentation.
- **Audience Filtering:** Both platforms must enforce the **Digital Payer Filter** (Engaged shoppers / UPI / Online payment history) to ensure visitors have the intent and ability to complete the ₹9 transaction.

---

## 3. The 10x Scaled Economics Rule
Claude Code is **FORBIDDEN** from arbitrarily increasing the daily ad budget beyond ₹100 unless the **10x Value Flywheel Benchmark** is triggered:

```
Flywheel Equation:
Spend: ₹100/day ──▶ Target Pipeline Value: ₹1,000/day
├── Front-end: 5–8 x ₹9 book sales (~₹45–₹72)
├── Mid-funnel: 1–2 x ₹190 bundle upgrades (~₹190–₹380)
└── Back-end: 1 lead in pipeline for 1:1 Clarity Session (~₹1,000)
```

### Execution Directives for Claude Code:
1. **Hold Steady at ₹100:** If daily return is positive or neutral (covering front-end cost), keep budget at ₹100.
2. **Scale Trigger (+20% only):** If 3 consecutive days demonstrate consistent bundle upgrades and CAC < ₹30, increase budget by 15–20% maximum.
3. **Audit Rule:** If spend reaches ₹100 with 0 sales, do NOT kill blindly. First check CTR and landing page bounce rate in `03_Reports_Insights/`.
