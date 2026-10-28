---
name: seo-optimization
description: |
  Comprehensive SEO audit, technical optimization, structured data (Schema.org / JSON-LD), on-page content strategy, OpenGraph, Core Web Vitals, and search crawler readiness for websites and web applications.
  Use whenever:
  - Performing an SEO audit or optimizing meta tags, headings, and content on any webpage.
  - Adding or validating Schema.org JSON-LD structured data (Person, WebSite, Article, Organization, etc.).
  - Configuring social preview cards (OpenGraph and Twitter Cards).
  - Generating sitemap.xml, robots.txt, or canonical URLs.
  - Improving Core Web Vitals (LCP, INP, CLS) and mobile search engine rankings.
license: MIT
metadata:
  version: v1
  author: drymhd
---

# SEO Audit & Optimization Skill (`seo-optimization`)

This skill provides complete guidelines, automated auditing procedures, and best practices for technical SEO, on-page optimization, rich snippets, and performance tuning for modern web applications and static sites.

---

## 1. Core On-Page SEO Checklist

Every webpage must satisfy these core on-page criteria:

### Title Tag (`<title>`)
- **Length**: 50–60 characters (to prevent truncation in Google SERPs).
- **Format**: `Primary Keyword — Secondary Keyword | Brand Name` or `Name — Professional Title`.
- **Placement**: Inside `<head>`, unique across the entire site.

### Meta Description (`<meta name="description">`)
- **Length**: 140–160 characters.
- **Copy**: Active voice, concise value proposition, includes target keywords naturally, ends with a soft call-to-action (CTA).
- **Rule**: Must accurately describe the page content without keyword stuffing.

### Heading Structure (`<h1>` – `<h6>`)
- **Single `<h1>`**: Exactly one `<h1>` per page representing the main topic.
- **Strict Hierarchy**: Never skip heading levels (e.g., do not jump from `<h1>` to `<h3>` without an intervening `<h2>`).
- **Semantic Grouping**: Wrap sections in `<section>` or `<article>` with descriptive headings.

### Image Optimization & Accessibility
- **Alt Text**: Descriptive `alt` attributes on all meaningful images (e.g., `alt="Dary Mahdi - Senior Fullstack Developer"` instead of `alt="photo"`).
- **Explicit Dimensions**: Always specify `width` and `height` (or CSS `aspect-ratio`) to prevent Cumulative Layout Shift (CLS).
- **Modern Formats**: Prefer WebP, AVIF, or optimized SVG for vector assets.
- **Loading Strategy**:
  - Hero / LCP candidate: `loading="eager"` and `fetchpriority="high"`.
  - Below-the-fold images: `loading="lazy"` and `decoding="async"`.

---

## 2. Technical SEO & Crawler Directives

### Canonical Tag
Prevent duplicate content penalties by explicitly specifying the preferred URL:
```html
<link rel="canonical" href="https://example.com/current-page">
```

### Robots Directives
```html
<meta name="robots" content="index, follow">
```
For pages that should NOT be indexed (e.g. admin panels, draft pages):
```html
<meta name="robots" content="noindex, nofollow">
```

### Robots.txt Template (`robots.txt`)
Place at root: `https://example.com/robots.txt`
```text
User-agent: *
Allow: /
Sitemap: https://example.com/sitemap.xml
```

### XML Sitemap (`sitemap.xml`)
Standard sitemap structure for search engines:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://example.com/</loc>
    <lastmod>2026-10-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```

---

## 3. Social Media Sharing & Previews (OpenGraph & Twitter Cards)

Ensure high click-through rates (CTR) when links are shared on LinkedIn, WhatsApp, X (Twitter), Discord, and Slack:

```html
<!-- Open Graph / Facebook / LinkedIn / WhatsApp -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://example.com/">
<meta property="og:title" content="Page Title (Max 60 chars)">
<meta property="og:description" content="Engaging summary of page content (Max 160 chars)">
<meta property="og:image" content="https://example.com/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Engaging summary of page content">
<meta name="twitter:image" content="https://example.com/og-image.png">
```

---

## 4. Structured Data (Schema.org / JSON-LD)

Structured data unlocks Google Rich Snippets (Knowledge Graph, verified profiles, breadcrumbs). Always use JSON-LD placed inside `<script type="application/ld+json">`.

### Portfolio / Personal CV Schema (`Person` + `WebSite`):
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Person",
      "@id": "https://example.com/#person",
      "name": "Full Name",
      "jobTitle": "Senior Fullstack Developer",
      "url": "https://example.com",
      "image": "https://example.com/profile.png",
      "sameAs": [
        "https://github.com/username",
        "https://www.linkedin.com/in/username"
      ],
      "knowsAbout": ["Laravel", "Flutter", "Go", "Vue.js", "Python", "REST APIs"],
      "alumniOf": {
        "@type": "EducationalOrganization",
        "name": "University Name"
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://example.com/#website",
      "url": "https://example.com",
      "name": "Full Name Portfolio",
      "publisher": {
        "@id": "https://example.com/#person"
      }
    }
  ]
}
```

---

## 5. Core Web Vitals (CWV) for Search Rankings

Google uses Core Web Vitals as a direct search ranking signal:

| Metric | Target | Optimization Strategy |
| :--- | :--- | :--- |
| **LCP** (Largest Contentful Paint) | `< 2.5s` (Ideal `< 1.2s`) | Preload fonts (`preconnect`), set `fetchpriority="high"` on hero images, eliminate render-blocking CSS/JS. |
| **INP** (Interaction to Next Paint) | `< 200ms` (Ideal `< 50ms`) | Avoid heavy synchronous JavaScript execution on user click/scroll; use `requestIdleCallback` or debouncing. |
| **CLS** (Cumulative Layout Shift) | `< 0.1` (Ideal `0`) | Reserve space for images and dynamic content with `aspect-ratio` or explicit dimensions; avoid inserting DOM above existing content. |

---

## 6. Automated Audit Workflow

When auditing any page or repository:
1. **Verify Meta Tags**: Check `<title>`, `<meta name="description">`, `<meta name="viewport">`, `<link rel="canonical">`.
2. **Verify Headings**: Run an outline check to ensure a single `<h1>` and valid nesting.
3. **Verify Structured Data**: Check syntax of JSON-LD scripts and validate against Schema.org types.
4. **Verify Asset Optimization**: Ensure images have `alt` tags and dimensions.
5. **Run Audit Script**: Execute `python3 scripts/audit_seo.py <path-to-html>` to produce an automated report.
