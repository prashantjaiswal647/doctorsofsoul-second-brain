---
type: qa
title: Tracking QA
brand: Doctors of Soul
status: active
tags:
  - ads
  - tracking
  - qa
created: 2026-10-27
updated: 2026-10-27
---

# Tracking QA

qa_status: **pending**

Up: [[Ads/Reports/Campaign-Performance-Tracker]] · Schema: [[Ads/Tracking/Event-Schema]]

| # | Check | Who | Status | Date |
|---|---|---|---|---|
| 1 | Meta privacy/dataset समीक्षा (`docs/TRACKING-META-REVIEW-HI.md`) | आप | pending | — |
| 2 | `set-secrets.sh meta` चलाया, Test events code के साथ | आप | pending | — |
| 3 | Test events: PageView, ViewContent, AddToCart, InitiateCheckout | आप | pending | — |
| 4 | असली ₹9 Purchase: Browser+Server एक बार (dedup), राशि ₹9, INR | आप | pending | — |
| 5 | Token पेजों पर कोई tag नहीं | आप/Claude | pending | — |
| 6 | Health-नीति की कोई चेतावनी Events Manager में नहीं | आप | pending | — |
| 7 | `meta-test-end` चलाया | आप | pending | — |

`qa_status` को `passed` तभी करें जब 1–7 पूरे हों। कोई ID, token या code यहाँ न लिखें।
