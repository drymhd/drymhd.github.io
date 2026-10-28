---
name: github-pages-portfolio
description: |
  Comprehensive guide and standards for building, auditing, styling, and maintaining professional developer portfolios on GitHub Pages (*.github.io).
  Use whenever:
  - Building, redesigning, or refining a personal developer portfolio or resume website hosted on GitHub Pages.
  - Ensuring the portfolio looks authentic, senior-engineered, human-crafted, and avoids generic "AI-generated template" clichés.
  - Implementing fast performance, modern CSS (fluid type, subgrid, :has()), dark/light themes, SEO, OpenGraph tags, and accessibility (a11y).
license: MIT
metadata:
  version: v2
  author: drymhd
---

# GitHub Pages Developer Portfolio Guide (`github-pages-portfolio`)

This skill provides the definitive engineering and design guidelines for personal portfolio websites hosted on GitHub Pages (`username.github.io`). It prioritizes authentic craftsmanship, senior developer credibility, lightning-fast load times, and an anti-AI aesthetic.

---

## 1. Anti-AI Template Manifesto (How to Never Look AI-Generated)

AI-generated portfolios suffer from recognizable "tells" that immediately flag the site as low-effort or generated:
- **Generic Blue/Purple Gradient Glows**: Radial light beams, purple-to-indigo blobs, and cyan borders on pitch black.
- **Faux UI Chrome**: Fake macOS red/yellow/green window dots around personal photos or cards.
- **Blueprint Grid Overlays**: Cheesy SVG/CSS grid lines behind the hero section.
- **Shiny Gradient Text**: Using `-webkit-text-fill-color: transparent` gradients everywhere instead of confident solid typography.
- **Vague Buzzwords**: Sentences like *"Passionate software engineer crafting digital experiences with high scalability and performant solutions"*.
- **Empty Showcase**: A portfolio without real, concrete projects, problem-solution statements, or architecture details.

### Golden Rules for Authentic Human Craft:
1. **Natural, Tactile Color Palette**:
   - **Dark Mode**: Warm matte graphite (`#111215` / `#17191e`), crisp 1px hairline borders (`#242730`), bone-white typography (`#f4f5f7`), and high-contrast solid buttons (`#f4f5f7` on `#111215`).
   - **Light Mode**: Warm editorial paper (`#fafaf8` / `#ffffff`), slate borders (`#e7e7e2`), and deep ink black typography (`#18181b`).
   - Use a single dignified accent (e.g., warm amber `#f59e0b` or subtle emerald `#10b981` status dot) rather than neon cyber glows.
2. **Featured Projects First**: Concrete systems context, specific technologies (e.g., *Logistics ERP, Go microservices, offline-first Flutter with SQLite*), and measurable business impact (e.g., *30% latency reduction*).
3. **Clean Portrait Presentation**: Present personal headshots with honest editorial framing (clean 1px border, natural radius, subtle caption), never wrapped in fake terminal windows.
4. **Interactive Tactility**: Real micro-interactions such as instant clipboard copying with subtle toast, project category filters, keyboard shortcuts, and smooth theme toggling.

---

## 2. GitHub Pages Architecture & Performance

### Core Constraints & Optimizations
- **Static Hosting**: GitHub Pages serves static files (`index.html`, `style.css`, `script.js`). Keep the core bundle lightweight (< 50KB CSS/JS compressed) for near-instant LCP (< 1.0s).
- **Asset Paths**: Always use relative paths (`style.css`, `profile.png`, `assets/...`) so the site functions both on root domains (`drymhd.github.io`) and subpaths (`user.github.io/repo/`).
- **No Build Bloat**: Prefer Vanilla HTML5, Modern CSS, and modular Vanilla ES6+ JavaScript. No bulky frameworks needed for a static portfolio.
- **Images**: Use responsive dimensions, `loading="lazy"`, `decoding="async"`, and appropriate aspect ratios.

---

## 3. Mandatory SEO & OpenGraph Checklist

Every GitHub Pages portfolio must include:
- [x] Primary `meta` tags: `title`, `description`, `keywords`, `author`, `robots`.
- [x] Canonical link: `<link rel="canonical" href="https://username.github.io/">`.
- [x] OpenGraph (Facebook/LinkedIn) tags: `og:title`, `og:description`, `og:image`, `og:url`, `og:type="website"`.
- [x] Twitter Card tags: `twitter:card="summary_large_image"`, `twitter:title`, `twitter:description`, `twitter:image`.
- [x] JSON-LD Structured Data: Schema.org `Person` with `name`, `jobTitle`, `alumniOf`, `worksFor`, and `sameAs` social profiles.
- [x] Accessible SVG Favicon embedded directly or linked.

---

## 4. Modern CSS & Accessibility (a11y) Standards

- **Semantic HTML**: Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, and `<footer>`.
- **Keyboard Navigation**: Ensure all interactive elements have visible focus indicators (`:focus-visible`). Provide a skip-to-content link.
- **Color Contrast**: All text must meet WCAG AA standards (minimum 4.5:1 ratio against background).
- **Reduced Motion**: Respect `@media (prefers-reduced-motion: reduce)` by disabling aggressive transitions.
- **Theme Persistence**: Support dark and light mode via `data-theme` attribute, synchronized with `prefers-color-scheme` and stored in `localStorage`.
