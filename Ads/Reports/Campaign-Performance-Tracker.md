---
type: campaign-performance
title: Doctors of Soul Campaign Performance Tracker
brand: Doctors of Soul
status: active
source: Meta Ads, Google Ads, GA4, GTM, Website Backend
platforms:
  - Meta
  - Google Ads
  - GA4
  - GTM
  - Website
  - Payments
tags:
  - ads
  - campaign
  - performance
  - tracking
  - leads
  - retargeting
  - roi
  - meta
  - google-ads
created: 2026-10-27
updated: 2026-10-27
---

# Doctors of Soul Campaign Performance

Parent: [[Ads/Strategy/Campaign-Strategy]]
Tracking: [[Ads/Tracking/Event-Schema]]
QA: [[Ads/Tracking/Tracking-QA]]
Meta: [[Ads/Reports/Meta-Campaign-Performance]]
Leads: [[Ads/Reports/Leads-and-Retargeting]]
Payments: [[Ads/Reports/Payments-and-Revenue]]
Experiments: [[Ads/Experiments/Experiment-Log]]
Decisions: [[Ads/Decisions/Decision-Log]]

Also see: [[campaign_v2_plan_2026-10-27]] · [[campaign_rules]] · [[2026-10-27_truth_pass]] · [[HOME_DASHBOARD]]

## 🚦 Launch gate (Campaign launch तभी करें जब नीचे दोनों सही हों)

| Gate | Required | Current |
|---|---|---|
| QA status | `passed` | **pending** (Pixel/CAPI अभी off; Events Manager जाँच बाकी) |
| Campaign status | `PAUSED / Ready for review` | **NOT CREATED** (Ads Manager में कोई campaign नहीं है) |

> "Current" की दोनों पंक्तियाँ सिर्फ़ तब बदलें जब नतीजा और तारीख़ [[Ads/Tracking/Tracking-QA]] में दर्ज हो (ID/token/स्क्रीनशॉट का कोड नहीं)।

## 🔁 शुरू से अंत तक की प्रक्रिया

| # | Phase | Owner | Status |
|---|---|---|---|
| 0 | Option A तय (₹100/day, सिर्फ़ Hindi Meta, 7 दिन, static03) | आप | ✅ 2026-10-27 |
| 1 | Code merge + deploy (PR #63–#66), live checks | Claude/आप | ✅ 2026-10-27 |
| 2 | `ADMIN_PATH` सेट, `/admin` बाहर से 404 | आप | ✅ 2026-10-27 |
| 3 | Meta billing: funds/payment method, Page, GST बैनर | आप | ⏳ |
| 4 | Pixel/CAPI: `set-secrets.sh meta`, Test events, असली ₹9 खरीद, dedup जाँच, `meta-test-end` | आप | ⏳ |
| 5 | Campaign **PAUSED** बनाना ([[Ads/Strategy/Campaign-Strategy]] की शीट से) | आप | ⏳ |
| 6 | Activate से पहले screenshot review | Claude | ⏳ |
| 7 | Activate | आप | ⏳ |
| 8 | 7 दिन: कोई बदलाव नहीं, रोज़ खर्च ledger में | आप/Claude | ⏳ |
| 9 | Day 7 रिपोर्ट + फ़ैसला ([[Ads/Decisions/Decision-Log]]) | आप + Claude | ⏳ |

## 📅 Daily tracker (असली आँकड़े सिर्फ़ Meta export / GA4 / backend से)

खर्च का **एकमात्र रिकॉर्ड**: repo की `marketing/creative-performance.csv` (दैनिक कमांड: `docs/AD-LEDGER-HOWTO-HI.md`). यहाँ सिर्फ़ सार लिखें; ₹ और $ कभी जोड़ें नहीं।

| Date | Day | Spend ₹ | Impressions | Clicks | Visits (GA4/admin) | Checkout starts | Orders | Revenue ₹ | Note |
|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | अभी कोई डेटा नहीं (0 runs, ₹0) |

## 🧮 Day 7 के बाद देखने की चीज़ें

Spend, visits, checkout starts, purchases, upgrade acceptance, meeting bookings. Kill/keep नियम: [[campaign_v2_plan_2026-10-27]] (§9). कोई नंबर बिना स्रोत के यहाँ नहीं।

## ⚠️ अभी की सीमाएँ

- Meta Pixel बंद; Google Ads और GTM इस pilot का हिस्सा नहीं (GTM बदलाव `wip/gtm-layout` branch पर अलग रखा है)।
- Adspirer quota 19 नवंबर 2026 तक पूरी; campaign हाथ से Ads Manager में बनेगा।
