# SEO & Generative Engine Optimization (GEO) Audit Report (2026-10-26)

**Status (updated 2026-10-27): PARTIALLY RESOLVED.** The original audit text below is kept as the record; §0 says what has since shipped on branch `fix/technical-seo-and-utm` (head `a0a87eb`) and what is still open. Cross-references: [[HOME_DASHBOARD]], [[2026-10-27_truth_pass]].

This report is based on a targeted inspection of key Next.js frontend files for SEO and GEO best practices.

---

## 0. Resolution status (2026-10-27)

| Audit finding | Status | Where |
|---|---|---|
| XML sitemap missing | **FIXED** — dynamic `/sitemap.xml` built from the live catalogue, bilingual `hreflang` alternates; verified `200` locally | `frontend/app/sitemap.ts`, `frontend/lib/seo.ts` |
| `robots.txt` gaps | **FIXED** — disallows `/admin`, `/api/`, `/checkout`, `/thank-you`, `/upgrade`, `/*/meeting/confirmed`; references sitemap | `frontend/public/robots.txt` |
| Canonical URLs missing | **FIXED** — home, language home, meeting, AI-engineering, book and policy pages | `frontend/lib/seo.ts` |
| `hreflang` missing | **FIXED** — `en`/`hi` pairs on every static page and paired book page | `frontend/lib/seo.ts` |
| Book / Product / Offer JSON-LD missing | **FIXED** — `@type: ["Book","Product"]`, live price/currency, `InStock`/`OutOfStock`; **no fabricated ratings or reviews** | `frontend/lib/seo.ts`, `frontend/components/JsonLd.tsx` |
| Service JSON-LD missing (meeting) | **FIXED** — provider Prashant Jaiswal, no `offers` block | same |
| FAQPage / QAPage schema | **OPEN** | — |
| `og:type` = book/product | **OPEN** | — |
| `llms.txt` / `ai-catalog.json` | **OPEN** | — |
| Image `alt` text, content depth ≥500 words, contextual internal linking | **OPEN** | — |
| `X-Robots-Tag: noindex, nofollow` on every `/hi` and `/en` route described below as "good practice" | **WRONG AND REMOVED** — those are the canonical language landings; de-indexing them would remove the site from search. Regression test added, block removed in `a0a87eb`. Proxy verified active locally: `/admin` → `404` without the gate cookie, `/<ADMIN_PATH>` → `307 /admin`, and `/hi` / `/en/meeting` send **no** `X-Robots-Tag`. | `frontend/proxy.ts`, `frontend/lib/adsLanding.test.ts` |

**Deploy check (owner):** `SITE_URL` must be set to `https://doctorsofsoul.co.in` in production, otherwise canonical and sitemap URLs fall back to `http://localhost:3000`.

## 1. Meeting Page (`frontend/app/[lang]/meeting/page.tsx`)

### Metadata:
*   **Title:** Dynamically set from `MEETING_TEXT[lang].nav`.
*   **Description:** Dynamically set from `MEETING_TEXT[lang].lead`.
*   **OpenGraph:** Not explicitly defined in `generateMetadata` function. Default OpenGraph tags may be inherited or absent.
*   **Canonical URLs:** Not explicitly set.
*   **Robots Meta Tag:** Not explicitly set in this file. *(Correction 2026-10-27: the audit originally called the proxy's site-wide `X-Robots-Tag: noindex, nofollow` on `/en` and `/hi` "good practice". It was the opposite — those routes are the canonical pages. The block has been removed and is covered by a regression test.)*

### Structured Data (JSON-LD):
*   **Status:** Missing.
*   **Recommendation:** Implement `Service` or `Event` schema for the 1:1 Clarity Meeting session to enable rich snippets in SERPs, including price, currency, provider (Prashant Jaiswal / Cosmic Yog), and area served.

### Generative Engine Optimization (GEO):
*   **`llms.txt` / AI Agent Access Policy:** Not directly related to this page, but a site-wide `llms.txt` and `ai-catalog.json` are currently missing (as identified in the previous comprehensive audit), which limits AI crawler access.

## 2. Book Detail Page (`frontend/app/[lang]/books/[slug]/page.tsx`)

### Metadata:
*   **Title:** Dynamically set from `book.title`.
*   **Description:** Dynamically set from `book.short_description`.
*   **OpenGraph:** Partially defined, includes `og:title` (book.title), `og:description` (book.short_description), and `og:image` (book.cover_url). Missing `og:type` (should be `book` or `product`).
*   **Canonical URLs:** Not explicitly set. `permanentRedirect` is used for language mismatches, which helps with canonicalization but an explicit `<link rel="canonical" href="...">` is still beneficial.
*   **hreflang:** Implicitly handled by `permanentRedirect` for language mismatches, but explicit `hreflang` tags in the `<head>` are missing (as identified in the previous comprehensive audit).

### Structured Data (JSON-LD):
*   **Status:** Missing.
*   **Recommendation:** Implement `Book` schema, `Product` schema, and `Offer` schema for the featured book pages. This would enable rich results like price, availability, and potentially reviews directly in SERPs.
*   **FAQPage / QAPage Schema:** The page renders `book.faqs`, but no corresponding `FAQPage` or `QAPage` schema is present.

### Generative Engine Optimization (GEO):
*   **`llms.txt` / AI Agent Access Policy:** Not directly related to this page, but a site-wide `llms.txt` and `ai-catalog.json` are currently missing (as identified in the previous comprehensive audit), which limits AI crawler access.

## General Observations & Recommendations:

*   **XML Sitemap:** The site is missing an XML sitemap, which is critical for efficient page discovery by search engines, especially for bilingual and dynamic content.
*   **`robots.txt`:** The `robots.txt` needs to be updated to include disallows for `/admin/*`, `/api/*`, and explicitly reference the sitemap.
*   **Image Optimization:** `alt` text optimization for book covers and responsive image sources are still opportunities.
*   **Content Depth:** Book pages could benefit from ensuring ≥500 words of unique content to improve ranking potential.
*   **Internal Linking:** Contextual internal linking (e.g., related books) is an opportunity.

Co-Authored-By: Claude Code <noreply@anthropic.com>