# SEO & Generative Engine Optimization (GEO) Audit Report (2026-10-26)

This report is based on a targeted inspection of key Next.js frontend files for SEO and GEO best practices.

## 1. Meeting Page (`frontend/app/[lang]/meeting/page.tsx`)

### Metadata:
*   **Title:** Dynamically set from `MEETING_TEXT[lang].nav`.
*   **Description:** Dynamically set from `MEETING_TEXT[lang].lead`.
*   **OpenGraph:** Not explicitly defined in `generateMetadata` function. Default OpenGraph tags may be inherited or absent.
*   **Canonical URLs:** Not explicitly set.
*   **Robots Meta Tag:** Not explicitly set in this file, but `X-Robots-Tag: noindex, nofollow` is applied by `proxy.ts` middleware for localized routes (`/en`, `/hi`) to prevent crawling of non-canonical versions, which is a good practice for locale isolation.

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