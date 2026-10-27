# Creative Registry & Performance Ledger (2026-10-27)

**Status:** CURRENT — system बना और test हुआ, पर **data शून्य है**: 0 runs, 0 spend, 0 orders.
**Repo branch:** `feat/book-pitch-and-meeting-copy` · commit `525aa9e`
**Files:** `marketing/creative-registry.csv`, `marketing/creative-performance.csv`, `marketing/CREATIVE-LEDGER-HI.md`, `deploy/devtools/creative_report.py`, `backend/tests/test_creative_ledger.py`.

Cross-references: [[HOME_DASHBOARD]], [[campaign_rules]], [[campaign_v2_plan_2026-10-27]], [[2026-10-27_truth_pass]], [[ad_spend_logs.csv]].

---

## 1. क्या बना

| हिस्सा | काम |
|---|---|
| Registry (`creative-registry.csv`) | हर creative का स्थायी ID, file, language, platform, angle, status, brand check, `utm_content` |
| Ledger (`creative-performance.csv`) | एक row = creative × platform × run: dates, spend, impressions, clicks, CTA clicks, sessions, orders, revenue, currency |
| Tool (`creative_report.py`) | Registry/ledger validate करता है और CTR, CPC, CTA rate, CVR, CAC, ROAS निकालता है; **INR और USD कभी नहीं जोड़ता** |
| Tests (`test_creative_ledger.py`) | 8 tests: metrics, blank denominators, unknown creative, UTM mismatch, missing stop date, currency isolation, ranking, real empty ledger |

Verified: 8/8 tests pass, tool खाली ledger पर exit 0 के साथ "No runs recorded yet" देता है। कोई संख्या नहीं बनाई गई।

## 2. Creative numbering (4 creatives)

| # | ID | Language | Angle | Status | Brand |
|---|---|---|---|---|---|
| 1 | `static01` | hi | नवरात्रि वापसी, देवी का संवाद | NOT_RUN | **CONFLICT** — देवी चित्र |
| 2 | `static02` | en | "Vedic Oracle / exact chart" | NOT_RUN | **CONFLICT** — deity/oracle + personalised claim |
| 3 | `static03` | hi | कुंडली मौसम, नाव आपकी | PREPARED | PASS |
| 4 | `static04` | en | "Stop Guessing" (brand-safe) | PREPARED | PASS |

Owner ने जो दो images भेजीं वे static01/static02 की ही copies हैं (MD5 match), नए assets नहीं।

## 3. खुला owner decision — brand conflict

`soul` और campaign rules: कोई देवी/ऑरेकल चित्र नहीं, कोई prediction promise नहीं। static01/static02 दोनों इसके विरुद्ध हैं; [[campaign_v2_plan_2026-10-27]] ने इसी कारण static03/static04 बनाए थे। दोनों 800×800 भी हैं (Meta feed recommendation 1080×1080)।
**विकल्प:** (a) static03/static04 चलाएँ, या (b) owner लिखित में brand rule override करे और फिर 1080×1080 पर resize कराए। Agent ने कुछ चलाया नहीं, हटाया नहीं — सिर्फ़ दर्ज किया।

## 4. Performance sheet भरने का तरीका

- spend / impressions / clicks — Meta या Google का export।
- cta_clicks — landing page के CTA button clicks।
- sessions / orders / revenue — Admin → Traffic, `content` row; INR और USD अलग।
- `utm_content` हमेशा `creative_id` के बराबर — इसी से हर order उस creative तक पहुँचता है (`backend/app/models.py` का `attribution` JSON + `backend/app/stats.py`)।
- Tool चलाएँ: `backend/.venv/Scripts/python.exe deploy/devtools/creative_report.py`

## 5. Per-person attribution की सच्चाई

Click → order mapping पहले से है: UTM/click-ID checkout पर order के साथ सुरक्षित होते हैं और Admin → Traffic में creative-level revenue दिखती है। सीमाएँ: tracking block, दूसरा device, और Meta/Google के reported conversions से matching (उसके लिए API/offline conversion चाहिए; Meta Pixel अभी बंद, Adspirer quota 15/15, reset 2026-11-19)।

## 6. Weekly ritual

हर सोमवार: platform export + Admin Traffic भरें → report चलाएँ → एक ही currency में ROAS/CAC तुलना → 10-दिन से पहले creative न मारें ([[campaign_rules]]) → decision की वजह note में लिखें।

## 7. अगला कदम

1. static01/static02 पर owner का फैसला।
2. जो creatives चलें, उन्हें 1080×1080 में resize करना।
3. पहला run शुरू होते ही ledger में row; तब पहली बार असली ROAS/CAC बोला जा सकेगा।
