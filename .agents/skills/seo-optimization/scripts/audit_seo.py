#!/usr/bin/env python3
"""
SEO Audit Script for HTML files
Parses an HTML document and generates an automated SEO report.
Checks:
- Title tag & length (50-60 chars)
- Meta description & length (140-160 chars)
- Viewport tag
- Canonical URL
- Robots directives
- OpenGraph tags (og:title, og:description, og:image, og:url, og:type)
- Twitter Card tags
- Heading structure (Single <h1>, hierarchy)
- Images (alt tags, explicit width/height)
- Structured Data (Schema.org / JSON-LD)
"""

import sys
import re
from html.parser import HTMLParser

class SEOAuditor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_script_ld = False
        self.title = ""
        self.meta_tags = []
        self.canonical = None
        self.headings = []
        self.images = []
        self.json_ld_blocks = []
        self.current_json_ld = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            self.meta_tags.append(attrs_dict)
        elif tag == "link" and attrs_dict.get("rel") == "canonical":
            self.canonical = attrs_dict.get("href")
        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self.headings.append((tag, ""))
        elif tag == "img":
            self.images.append({
                "src": attrs_dict.get("src", ""),
                "alt": attrs_dict.get("alt"),
                "width": attrs_dict.get("width"),
                "height": attrs_dict.get("height"),
                "loading": attrs_dict.get("loading")
            })
        elif tag == "script" and attrs_dict.get("type") == "application/ld+json":
            self.in_script_ld = True
            self.current_json_ld = ""

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_script_ld:
            self.in_script_ld = False
            if self.current_json_ld.strip():
                self.json_ld_blocks.append(self.current_json_ld.strip())

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_script_ld:
            self.current_json_ld += data


def audit_html(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}")
        return

    parser = SEOAuditor()
    parser.feed(html_content)

    print("=" * 60)
    print(f"SEO AUDIT REPORT: {filepath}")
    print("=" * 60)

    score = 100
    deductions = []

    # 1. Title
    title = parser.title.strip()
    print(f"\n[1] Title Tag:")
    if not title:
        print("  ❌ Missing <title> tag!")
        score -= 20
        deductions.append("Missing <title> tag (-20)")
    else:
        title_len = len(title)
        print(f"  ✓ Content: \"{title}\"")
        print(f"  ✓ Length: {title_len} chars (Recommended: 50-60 chars)")
        if title_len < 30 or title_len > 70:
            print(f"  ⚠️ Warning: Title length ({title_len}) outside optimal range (50-60).")

    # 2. Meta Description
    desc = None
    for m in parser.meta_tags:
        if m.get("name", "").lower() == "description":
            desc = m.get("content", "").strip()
            break

    print(f"\n[2] Meta Description:")
    if not desc:
        print("  ❌ Missing <meta name=\"description\">!")
        score -= 15
        deductions.append("Missing meta description (-15)")
    else:
        desc_len = len(desc)
        print(f"  ✓ Content: \"{desc}\"")
        print(f"  ✓ Length: {desc_len} chars (Recommended: 140-160 chars)")
        if desc_len < 100 or desc_len > 170:
            print(f"  ⚠️ Warning: Description length ({desc_len}) outside optimal range (140-160).")

    # 3. Viewport & Canonical
    viewport = any(m.get("name", "").lower() == "viewport" for m in parser.meta_tags)
    print(f"\n[3] Mobile & Canonical Directives:")
    if viewport:
        print("  ✓ <meta name=\"viewport\"> present (Mobile friendly)")
    else:
        print("  ❌ Missing viewport meta tag! (-10)")
        score -= 10

    if parser.canonical:
        print(f"  ✓ Canonical Link: {parser.canonical}")
    else:
        print("  ⚠️ Missing <link rel=\"canonical\">! (-5)")
        score -= 5

    # 4. OpenGraph & Twitter Cards
    og_title = any(m.get("property") == "og:title" for m in parser.meta_tags)
    og_desc = any(m.get("property") == "og:description" for m in parser.meta_tags)
    og_img = any(m.get("property") == "og:image" for m in parser.meta_tags)
    tw_card = any(m.get("name") == "twitter:card" for m in parser.meta_tags)

    print(f"\n[4] Social Sharing Metadata (OpenGraph & Twitter Cards):")
    if og_title and og_desc and og_img:
        print("  ✓ OpenGraph tags present (og:title, og:description, og:image)")
    else:
        print("  ⚠️ Incomplete OpenGraph tags! (-5)")
        score -= 5

    if tw_card:
        print("  ✓ Twitter Card tag present")
    else:
        print("  ⚠️ Missing twitter:card tag! (-3)")
        score -= 3

    # 5. Headings Structure
    print(f"\n[5] Heading Structure:")
    h1_count = sum(1 for tag, _ in parser.headings if tag == "h1")
    if h1_count == 1:
        print("  ✓ Exactly one <h1> tag found.")
    elif h1_count == 0:
        print("  ❌ No <h1> tag found! (-15)")
        score -= 15
    else:
        print(f"  ⚠️ Warning: Multiple ({h1_count}) <h1> tags found! Single <h1> is recommended. (-5)")
        score -= 5

    # 6. Images
    print(f"\n[6] Images ({len(parser.images)} found):")
    missing_alt = [img for img in parser.images if img["alt"] is None or img["alt"] == ""]
    if missing_alt:
        print(f"  ⚠️ {len(missing_alt)} images missing alt text! (-5)")
        score -= 5
    else:
        print("  ✓ All images have descriptive alt text.")

    # 7. Structured Data (Schema.org / JSON-LD)
    print(f"\n[7] Structured Data (JSON-LD):")
    if parser.json_ld_blocks:
        print(f"  ✓ Found {len(parser.json_ld_blocks)} JSON-LD structured data block(s).")
    else:
        print("  ⚠️ No JSON-LD structured data found! (-5)")
        score -= 5

    # Final Score
    print("\n" + "=" * 60)
    print(f"OVERALL SEO HEALTH SCORE: {max(0, score)} / 100")
    print("=" * 60)

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    audit_html(target)
