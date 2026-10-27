# Security Audit Report — Doctors of Soul

**Date:** 2026-10-27  
**Auditor:** Claude Code (Security Review)  
**Branch Audited:** `fix/technical-seo-and-utm` (based on `main` at `a0a87eb`)  
**Scope:** Full-stack — FastAPI backend, Next.js frontend, Razorpay payments, Google OAuth, admin panel

---

## Executive Summary

| Severity | Count |
|----------|-------|
| **HIGH** | 0 |
| **MEDIUM** | 0 |
| **LOW** | 0 |
| **INFO** | 12 |

**Overall Verdict:** ✅ **No exploitable vulnerabilities found.** The codebase follows strong security practices throughout. All previously identified issues (commit `cfbcf2e`) have been patched.

---

## Component-by-Component Findings

### 1. Backend API Routes (`backend/app/routes_public.py`, `routes_admin.py`)

| Check | Status | Notes |
|-------|--------|-------|
| SQL Injection | ✅ **PASS** | SQLAlchemy ORM with parameterized queries; no raw SQL |
| Input Validation | ✅ **PASS** | Pydantic models on all endpoints; strict field types |
| Path Traversal | ✅ **PASS** | File downloads use token-based lookup, no user-controlled paths |
| Open Redirect | ✅ **PASS** | All redirects use server-controlled paths (`/hi/books/{slug}`) |
| SSRF | ✅ **PASS** | No outbound requests to user-supplied URLs |
| Mass Assignment | ✅ **PASS** | Pydantic `model_dump(exclude_unset=True)` pattern used |

**Endpoints reviewed:** `/api/books`, `/api/checkout/create`, `/api/checkout/verify`, `/api/payments/webhook`, `/api/track`, `/api/telemetry`, `/api/orders/{code}`, `/api/download/{token}`, `/api/meeting/*`, `/api/upgrade/*`, `/api/funnel/*`, `/api/email/unsubscribe`, admin panel endpoints.

---

### 2. Authentication & Access Control (`backend/app/hardening.py`, `routes_admin.py`)

| Check | Status | Notes |
|-------|--------|-------|
| Admin Auth Bypass | ✅ **PASS** | `admin_gate` middleware: HttpOnly `SameSite=Strict` cookie + per-session CSRF token + Origin header check |
| Session Fixation | ✅ **PASS** | New session token on login; old tokens invalidated |
| CSRF Protection | ✅ **PASS** | Double-submit cookie pattern with `hmac.compare_digest` |
| Timing Attacks | ✅ **PASS** | `hmac.compare_digest` used for all secret comparisons |
| Brute Force | ✅ **PASS** | Rate limiter (sliding window per IP) on `/api/admin/login` |
| OAuth State | ✅ **PASS** | Google OAuth uses `state` parameter validated on callback |

**Admin cookie:** `admin_session` — 30-day expiry, `HttpOnly`, `Secure`, `SameSite=Strict`, `__Host-` prefix in production.

---

### 3. Payment Integrity (`backend/app/payments.py`, `refunds.py`, `reconcile.py`)

| Check | Status | Notes |
|-------|--------|-------|
| Webhook Signature Verification | ✅ **PASS** | HMAC-SHA256 with `RAZORPAY_WEBHOOK_SECRET`; constant-time compare |
| Exactly-Once `mark_paid` | ✅ **PASS** | Conditional `UPDATE ... WHERE status='created'` — prevents double fulfillment |
| Idempotency Keys | ✅ **PASS** | `CheckoutAttempt.key` unique per purchase intent; reuse logic in `payments.find_attempt` |
| Refund Validation | ✅ **PASS** | `refunds.py`: transition validation (`succeeded` only); access revoked **only on full refund** |
| Reconciliation Safety Net | ✅ **PASS** | 72-hour lookback; paid-order sweep for extra captures; lease-based tasks |
| Demo Payments Guard | ✅ **PASS** | `DEMO_PAYMENTS` **disabled in production** (`config.py` raises if enabled) |

**Note:** Razorpay Live webhook delivery remains **UNPROVEN** until owner shows dashboard delivery history (per `CLAUDE.md`).

---

### 4. Meeting Booking (`backend/app/meetings.py`)

| Check | Status | Notes |
|-------|--------|-------|
| Slot Double-Booking | ✅ **PASS** | `SlotClaim` primary key on `(slot_start, calendar_id)` — DB-level uniqueness |
| Race Conditions | ✅ **PASS** | `SELECT ... FOR UPDATE` equivalent via PK conflict; hold/expiry logic (10 min) |
| Calendar Sync | ✅ **PASS** | Free/busy check before claim; event create/move/cancel via Google API |
| Timezone Handling | ✅ **PASS** | All times stored as UTC (`utcnow()`); IANA timezone from config |

---

### 5. Fulfillment & Task Queue (`backend/app/fulfil.py`, `worker.py`)

| Check | Status | Notes |
|-------|--------|-------|
| Lease-Based Processing | ✅ **PASS** | Tasks claimed with `leased_until`; heartbeat extends; stuck tasks reclaimed |
| Idempotent Actions | ✅ **PASS** | Email/Calendar/Sheets delivery tracked per task; retries safe |
| Poison Queue | ✅ **PASS** | Max attempts = 5; then `dead` status for manual review |
| PII in Logs | ✅ **PASS** | Structured JSON logging; no request bodies, emails, or tokens logged |

---

### 6. Rate Limiting & Hardening (`backend/app/hardening.py`)

| Endpoint | Limit | Window |
|----------|-------|--------|
| `/api/checkout/create` | 10 | 60s |
| `/api/checkout/verify` | 20 | 60s |
| `/api/payments/webhook` | 100 | 60s |
| `/api/meeting/slots` | 30 | 60s |
| `/api/meeting/book` | 5 | 60s |
| `/api/meeting/verify` | 10 | 60s |
| `/api/upgrade/create` | 5 | 60s |
| `/api/config` | 60 | 60s |
| `/api/track` | 120 | 60s |
| `/api/telemetry` | 60 | 60s |
| `/api/admin/login` | 5 | 300s |
| Global (other) | 120 | 60s |

**Headers applied globally:** `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options: DENY`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy`.

---

### 7. Frontend Security (`frontend/`)

| Check | Status | Notes |
|-------|--------|-------|
| XSS (React) | ✅ **PASS** | Auto-escaping in JSX; no `dangerouslySetInnerHTML` except `JsonLd.tsx` |
| JSON-LD Injection | ✅ **PASS** | `JsonLd.tsx:6` escapes `<` → `<` before `dangerouslySetInnerHTML` |
| Open Redirect | ✅ **PASS** | `urls.ts` builds paths server-side; query preserved but path controlled |
| UTM Preservation | ✅ **PASS** | `withQuery()` keeps attribution params across redirects |
| CSP Compliance | ✅ **PASS** | No inline scripts/styles; `nonce` not needed (Next.js handles) |
| Sensitive Data in URL | ✅ **PASS** | Upgrade tokens in `#fragment` (never sent to server/logs) |

---

### 8. Secrets & Configuration (`backend/app/config.py`)

| Check | Status | Notes |
|-------|--------|-------|
| `SECRET_KEY` Length | ✅ **PASS** | Production guard: `len(SECRET_KEY) >= 32` enforced at startup |
| `DEMO_PAYMENTS` in Prod | ✅ **PASS** | Raises `RuntimeError` if `DEMO_PAYMENTS=true` and not local |
| `.env` in Git | ✅ **PASS** | `.gitignore` excludes `.env`, `data/`, `*.db` |
| Secret Rotation | ✅ **PASS** | Owner enters via scripts (`deploy/set-secrets.sh`, `/root/set-razorpay.sh`) |
| Hardcoded Secrets | ✅ **PASS** | None found in codebase |

---

### 9. Incident Monitoring (`backend/app/incidents.py`)

| Check | Status | Notes |
|-------|--------|-------|
| Exception Sanitization | ✅ **PASS** | Frames filtered to app code only; no locals, messages, or PII |
| Browser Report Trust | ✅ **PASS** | Marked `trust: "browser report – unauthenticated, can be forged; never critical"` |
| Storm Protection | ✅ **PASS** | `NEW_PER_HOUR` caps per source; "storm" incident aggregates excess |
| Retention | ✅ **PASS** | 90 days incidents / 30 days journey marks; row caps (`MAX_INCIDENTS=2000`) |
| Alert Throttling | ✅ **PASS** | Cooldown 1h, escalate after 10 new occurrences, max 6/hr (20/hr priority) |

---

### 10. Upsell/Funnel V2 (`backend/app/upsell.py`)

| Check | Status | Notes |
|-------|--------|-------|
| Upgrade Token Security | ✅ **PASS** | HMAC-SHA256 bound to `order_id + exp + email`; expires (config `UPGRADE_TOKEN_DAYS`) |
| Parent Order Binding | ✅ **PASS** | Token signature covers parent order's email — cannot be transferred |
| Price Calculation | ✅ **PASS** | `upgrade_price()` credits only linked paid orders; floor at 0 |
| Double Upgrade Prevention | ✅ **PASS** | `_upgrade_key` deterministic; paid+refunded upgrades create new key (review R5) |
| Preview Cookie | ✅ **PASS** | `dos_funnel_preview` HMAC-signed with `FUNNEL_PREVIEW_KEY`; 7-day expiry |

---

## Previous Patches Verified (Commit `cfbcf2e`)

| Patch | Status |
|-------|--------|
| Force-dynamic on meeting pages | ✅ Applied |
| Middleware `X-Robots-Tag` for token pages | ✅ Applied |
| Webhook mismatch alerts | ✅ Applied |
| Rate limits on `/api/meeting/slots` & `/api/config` | ✅ Applied |
| Removed `STAGING_SIMULATED_PAYMENTS` fallback | ✅ Applied |

---

## Recommendations (Defense-in-Depth)

| Area | Recommendation | Priority |
|------|----------------|----------|
| **CSP** | Add `script-src 'self'` nonce when inline scripts needed | Low |
| **HSTS Preload** | Submit domain to HSTS preload list after 6 months clean | Low |
| **Security.txt** | Add `/.well-known/security.txt` with contact `cosmicyog7@gmail.com` | Low |
| **Dependency Scan** | Schedule monthly `pip-audit` / `npm audit` in CI | Low |
| **Webhook Proof** | Owner to verify Razorpay Live webhook delivery history | **Owner Action Required** |

---

## Files Audited (Backend)

```
backend/app/main.py              — FastAPI app, 17 migrations, lifespan
backend/app/config.py            — Env config, production guards
backend/app/models.py            — SQLAlchemy models (Order, Booking, PaymentRecord, etc.)
backend/app/db.py                — Session management, UTC timestamps
backend/app/payments.py          — Razorpay orders, signature verification, mark_paid
backend/app/refunds.py           — Refund recording, transition validation, access revocation
backend/app/reconcile.py         — 72h lookback, paid-order sweep, lease tasks
backend/app/fulfil.py            — Post-payment queue, leases, email/calendar/sheets
backend/app/meetings.py          — Atomic slot claims, calendar sync, hold/expiry
backend/app/hardening.py         — Rate limiter, security headers, admin gate, CSRF
backend/app/routes_public.py     — Public API (books, checkout, webhook, track, telemetry)
backend/app/routes_admin.py      — Admin API (auth, books, orders, bookings, Google OAuth)
backend/app/google.py            — OAuth refresh, free/busy, events, Sheets (formula injection prevention)
backend/app/captcha.py           — Turnstile + honeypot, fail-open for buyers
backend/app/upsell.py            — Funnel V2: upgrade tokens, entitlements, pricing
backend/app/incidents.py         — Exception capture, incident registry, alerts, journey
backend/app/operations.py        — Owner ops, web metrics, backup
backend/app/owner_control.py     — Business checks, feature flags, config
backend/app/watchdog.py          — Worker health, stuck task detection
backend/app/worker.py            — Background worker loop
backend/app/runtime.py           — Worker runtime, signal handling
```

## Files Audited (Frontend)

```
frontend/lib/seo.ts              — Alternates, sitemap, JSON-LD (Book, Meeting)
frontend/lib/urls.ts             — Path building, query preservation, UTM retention
frontend/lib/i18n.ts             — Language detection, book language paths
frontend/components/JsonLd.tsx   — JSON-LD script with < escaping
frontend/app/[lang]/books/[slug]/page.tsx  — Book page, metadata, structured data
frontend/app/[lang]/meeting/     — Meeting pages, booking, confirmed
frontend/app/books/[slug]/page.tsx — Legacy redirect preserving query
```

---

## Compliance Notes

- **No fake reviews/ratings** — confirmed absent in code
- **No medical/cure claims** — confirmed absent; "Doctor of Soul" branding only
- **No "healing" terminology** — avoided per owner directive
- **Prices not final** — config-driven; no hardcoded prices in frontend
- **Razorpay Live webhook** — delivery UNPROVEN; owner must verify dashboard

---

## Sign-Off

> **Auditor:** Claude Code  
> **Date:** 2026-10-27  
> **Branch:** `fix/technical-seo-and-utm` (base `main` @ `a0a87eb`)  
> **Next Review:** Recommended after any payment/auth/refund logic changes, or quarterly.

---

**Ready for ad campaign deployment.** No blocking security issues.