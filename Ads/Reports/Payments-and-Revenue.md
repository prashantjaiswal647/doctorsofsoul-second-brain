---
type: revenue
title: Payments and Revenue
brand: Doctors of Soul
status: active
tags:
  - ads
  - payments
  - revenue
created: 2026-10-27
updated: 2026-10-27
---

# Payments and Revenue

Up: [[Ads/Reports/Campaign-Performance-Tracker]] · Meta: [[Ads/Reports/Meta-Campaign-Performance]]

- Revenue का स्रोत: backend के **paid orders** (`/admin`) और Razorpay। विज्ञापन-मंच के आँकड़े revenue नहीं माने जाते।
- ₹ (INR) और $ (USD) हमेशा अलग; कभी जोड़ना नहीं।
- खर्च का रिकॉर्ड: repo की `marketing/creative-performance.csv`; रिपोर्ट: `deploy/devtools/creative_report.py`।
- Razorpay webhook: 2026-10-24 को `payment.captured` और `order.paid` पर HTTP 200 देखा गया (owner screenshots)।

| Date | Orders ₹ | Revenue ₹ | Orders $ | Revenue $ | Refunds |
|---|---|---|---|---|---|
| — | — | — | — | — | — |
