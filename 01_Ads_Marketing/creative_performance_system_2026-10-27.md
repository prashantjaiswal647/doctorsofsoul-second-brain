# Creative Registry & Performance Ledger (2026-10-27)

**Status:** CURRENT — system बना और test हुआ, पर **data शून्य है**: 0 runs, 0 spend, 0 orders.
**Repo branch:** `feat/book-pitch-and-meeting-copy` · commits `525aa9e` (ledger system), `0e82b58` (static01/02 copy revision, 1080×1080), `7ce5038` + `895b525` (static05 safe-copy test and revision)
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

## 2. Creative numbering (5 creatives)

| # | ID | File | Language | Angle | Status | Brand |
|---|---|---|---|---|---|---|
| 1 | `static01` | `/ads/hindi_navratri_v2_1080.png` (1080×1080) | hi | नवरात्रि वापसी, देवी का first-person संवाद | NOT_RUN | **CONFLICT** — देवी चित्र + devotional voice |
| 2 | `static02` | `/ads/global_oracle_v2_1080.png` (1080×1080) | en | "Your Chart Is a Map. Not a Verdict." | NOT_RUN | **CONFLICT** — देवी/ऑरेकल चित्र |
| 3 | `static03` | `/ads/campaign_v2_hindi_1x1.png` (1024×1024) | hi | कुंडली मौसम, नाव आपकी | PREPARED | PASS |
| 4 | `static04` | `/ads/campaign_v2_english_1x1.png` (1024×1024) | en | "Stop Guessing" (brand-safe) | PREPARED | PASS |
| 5 | `static05` | `/ads/hindi_navratri_safe_v2_1080.png` (1080×1080) | hi | "नवरात्रि गई, पर मैं नहीं" — safe-copy test | NOT_RUN | **CONFLICT** — सिर्फ़ देवी चित्र; कॉपी safe |

Owner ने जो दो images भेजीं वे static01/static02 की ही copies थीं (MD5 match), नए assets नहीं।

## 3. Copy संशोधन — owner decision (2026-10-27)

Owner ने graphics वही रखने और सिर्फ़ content बदलने को कहा; copy owner-approved है:

| ID | पुरानी कॉपी (जोखिम) | नई कॉपी (लागू) | क्या हटा |
|---|---|---|---|
| static01 | "Stop Guessing Your Destiny / Vedic Oracle" जैसा service framing | "नवरात्रि खत्म हो गई, / और मैं रुक गई। / स्वयं सबको पढ़ाने के लिए।" + CTA "किताब पढ़ें — ₹9" | oracle service framing, अंग्रेज़ी headline, छिपा CTA |
| static02 | "Your Personal Vedic Oracle", "tailored to your exact chart" | "Stop Guessing Your Destiny. / Your Chart Is a Map. Not a Verdict. / Astrology shows the weather. You still sail the boat." + CTA "Read the Book — $9" | personalised divination दावा, exact-chart promise, छिपा CTA |

**जो जोखिम बचा है (owner को पता है):** दोनों creatives में देवी/ऑरेकल चित्र अभी भी है और Hindi line first-person devotional voice में है — `soul` का "no deity or oracle imagery" नियम अभी टूटता है। इसलिए `brand_check = CONFLICT` ही रहेगा।
**विकल्प:** (a) [[campaign_v2_plan_2026-10-27]] के static03/static04 चलाएँ (PASS), या (b) owner लिखित में brand rule override करे। 1080×1080 resize हो चुका है। Agent ने कुछ चलाया नहीं, हटाया नहीं — सिर्फ़ दर्ज किया।

### static05 — safe-copy test (2026-10-27)

Owner ने यह test copy दी, वही design language और ₹9 offer:

> नवरात्रि गई,
> पर मैं नहीं
>
> सबको पढ़ाना है,
> सबको बढ़ाना है

CTA: **किताब पढ़ें** (₹9 ऊपर अलग) · `/ads/hindi_navratri_safe_v2_1080.png`

**v2 revision (2026-10-27, owner):** type ~10% छोटा, scenery थोड़ा zoom-out, Gemini watermark हटाया, CTA से ₹9 निकाला; पुरानी v1 history के लिए रखी है।

**कॉपी safe:** कोई prediction, oracle, exact-chart या "मैं पढ़ाऊँगी" दावा नहीं। **लेकिन** देवी आकृति अभी भी चित्र में है, इसलिए `brand_check = CONFLICT` (सिर्फ़ imagery)। static01 से अलग ID इसलिए रखा है कि एक ही graphics पर दो कॉपी की performance अलग-अलग मापी जा सके।

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

1. static01/static02/static05 पर सिर्फ़ एक फैसला बचा है: brand rule का लिखित override, या static03/static04 चलाना (दोनों PASS)।
2. 1080×1080 resize हो चुका — static01/static02/static05 की files repo में हैं।
3. पहला run शुरू होते ही `creative-performance.csv` में row; तब पहली बार असली ROAS/CAC बोला जा सकेगा।
