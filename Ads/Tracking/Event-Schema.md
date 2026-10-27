---
type: tracking
title: Event Schema
brand: Doctors of Soul
status: active
tags:
  - ads
  - tracking
  - meta
  - ga4
created: 2026-10-27
updated: 2026-10-27
---

# Event Schema

Up: [[Ads/Reports/Campaign-Performance-Tracker]] · QA: [[Ads/Tracking/Tracking-QA]]

Code में जाँचे गए नियम (repo audit, 2026-10-27; असली delivery सिर्फ़ Events Manager में साबित होती है):

| Event | कब | Dedup / नियम |
|---|---|---|
| PageView | हर सार्वजनिक पेज | token वाले पेजों (`/thank-you`, upgrade, meeting-confirmed, admin) पर कोई pixel नहीं |
| ViewContent | किताब का पेज | value/currency/book id; कोई ईमेल/फ़ोन नहीं |
| AddToCart | cart में डालना | — |
| InitiateCheckout | checkout खुलना | — |
| Purchase | सिर्फ़ captured payment पर | browser और server दोनों `event_id = purchase-<order code>`; राशि और INR/USD order से |

Meta payload में कच्चा ईमेल/फ़ोन, meeting notes या token नहीं जाता; server CAPI में ईमेल/फ़ोन hash होते हैं (hash का मतलब नाम-रहित होना नहीं है)। UTM की चाबियाँ: `utm_source=meta`, `utm_medium=paid`, `utm_campaign`, `utm_content` (= creative ID)।
