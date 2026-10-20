#!/usr/bin/env python3
"""Dependency-free quality checks for the BeInCasinos static site.

Run from the repository root: python3 scripts/check_site.py
This is a source-level check, not a substitute for browser, accessibility,
legal, privacy, or production-host testing.
"""
import csv
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
IGNORE_DIRS = {".git", ".vercel", "node_modules"}
errors = []
warnings = []
pages = sorted(p for p in ROOT.rglob("*.html") if not any(part in IGNORE_DIRS for part in p.parts))
titles = {}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_depth = 0
        self.title = ""
        self.description = ""
        self.h1_depth = 0
        self.h1_count = 0
        self.links = []
        self.resources = []
        self.ids = set()
        self.id_counts = {}
        self.images_missing_alt = 0
        self.html_lang = None
        self.has_viewport = False
        self.unsafe_new_tab_links = []
        self.empty_links = []
        self._link_depth = 0
        self._link_text = []
        self._current_link = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.html_lang = a.get("lang", "").strip()
        if "id" in a:
            self.ids.add(a["id"])
            self.id_counts[a["id"]] = self.id_counts.get(a["id"], 0) + 1
        if tag == "img" and "alt" not in a:
            self.images_missing_alt += 1
        if tag == "title":
            self.title_depth += 1
        if tag == "meta":
            if a.get("name", "").lower() == "description":
                self.description = a.get("content", "").strip()
            if a.get("name", "").lower() == "viewport":
                self.has_viewport = bool(a.get("content", "").strip())
        if tag == "h1":
            self.h1_count += 1
            self.h1_depth += 1
        if tag in ("a", "area") and a.get("href"):
            self.links.append(a["href"].strip())
            if tag == "a":
                if a.get("target", "").lower() == "_blank":
                    rel = {part.lower() for part in a.get("rel", "").split()}
                    if "noopener" not in rel:
                        self.unsafe_new_tab_links.append(a.get("href", ""))
                self._current_link = {"href": a["href"], "has_label": bool(a.get("aria-label", "").strip() or a.get("aria-labelledby", "").strip())}
                self._link_text = []
                self._link_depth = 1
        elif self._link_depth and tag in ("img", "svg", "input"):
            if tag == "img" and a.get("alt", "").strip():
                self._link_text.append("image alt")
            elif a.get("aria-label", "").strip() or a.get("title", "").strip():
                self._link_text.append("accessible label")
        if tag in ("script", "img", "source", "iframe", "audio", "video") and a.get("src"):
            self.resources.append(a["src"].strip())
        if tag == "link" and a.get("href"):
            self.resources.append(a["href"].strip())

    def handle_endtag(self, tag):
        if tag == "title" and self.title_depth:
            self.title_depth -= 1
        if tag == "h1" and self.h1_depth:
            self.h1_depth -= 1
        if tag == "a" and self._link_depth:
            text_content = " ".join(" ".join(self._link_text).split())
            if not text_content and not self._current_link.get("has_label"):
                self.empty_links.append(self._current_link.get("href", ""))
            self._link_depth = 0
            self._current_link = None
            self._link_text = []

    def handle_data(self, data):
        if self.title_depth:
            self.title += data
        if self._link_depth:
            self._link_text.append(data)


def resolve_local_url(page, raw):
    parsed = urlparse(raw)
    if parsed.scheme or parsed.netloc or raw.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None, parsed.fragment
    path = unquote(parsed.path)
    if not path:
        target = page
    elif path.startswith("/"):
        target = ROOT / path.lstrip("/")
    else:
        target = page.parent / path
    if target.is_dir():
        target = target / "index.html"
    elif not target.suffix:
        target = target / "index.html"
    return target.resolve(), parsed.fragment


for page in pages:
    rel = page.relative_to(ROOT).as_posix()
    parser = PageParser()
    try:
        parser.feed(page.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        errors.append(f"{rel}: cannot read HTML ({exc})")
        continue
    title = " ".join(parser.title.split())
    if not title:
        errors.append(f"{rel}: missing <title>")
    else:
        titles.setdefault(title.casefold(), []).append(rel)
    if not parser.description:
        errors.append(f"{rel}: missing meta description")
    elif len(parser.description) < 70 or len(parser.description) > 170:
        warnings.append(f"{rel}: meta description is {len(parser.description)} characters; review for a concise, useful search snippet (rough guide: 70–170)")
    if title and (len(title) < 15 or len(title) > 70):
        warnings.append(f"{rel}: title is {len(title)} characters; review search-result clarity (rough guide: 15–70)")
    if parser.h1_count != 1:
        errors.append(f"{rel}: expected exactly one h1, found {parser.h1_count}")
    if not parser.html_lang:
        errors.append(f"{rel}: missing html lang attribute")
    if not parser.has_viewport:
        errors.append(f"{rel}: missing responsive viewport meta tag")
    duplicate_ids = sorted(identifier for identifier, count in parser.id_counts.items() if count > 1)
    if duplicate_ids:
        errors.append(f"{rel}: duplicate id attribute(s): " + ", ".join(duplicate_ids))
    if parser.images_missing_alt:
        errors.append(f"{rel}: {parser.images_missing_alt} image(s) missing alt attribute")
    for href in parser.unsafe_new_tab_links:
        errors.append(f"{rel}: target=_blank link missing rel=noopener: {href}")
    for href in parser.empty_links:
        errors.append(f"{rel}: link has no text or accessible label: {href}")
    for raw in parser.links + parser.resources:
        target, fragment = resolve_local_url(page, raw)
        if target is None:
            continue
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{rel}: local link escapes site root: {raw}")
            continue
        if not target.exists():
            errors.append(f"{rel}: broken local link: {raw}")
        elif fragment and target.suffix.lower() in (".html", ".htm"):
            try:
                target_parser = PageParser()
                target_parser.feed(target.read_text(encoding="utf-8"))
                if fragment not in target_parser.ids:
                    warnings.append(f"{rel}: fragment target not statically verified: {raw}")
            except (OSError, UnicodeError):
                pass

# Verify canonical and social URL metadata for every indexable HTML page.
PRODUCTION_ORIGIN = "https://beincasinos.online"
for page in pages:
    rel = page.relative_to(ROOT).as_posix()
    if rel == "404.html":
        continue
    source = page.read_text(encoding="utf-8")
    expected_path = "/" if rel == "index.html" else "/" + rel[:-len("index.html")] if rel.endswith("/index.html") else "/" + rel
    expected_url = PRODUCTION_ORIGIN + expected_path
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', source, re.I)
    og_url = re.search(r'<meta property="og:url" content="([^"]+)"', source, re.I)
    if not canonical:
        errors.append(f"{rel}: missing canonical URL metadata")
    elif canonical.group(1) != expected_url:
        errors.append(f"{rel}: canonical URL should be {expected_url}, got {canonical.group(1)}")
    if not og_url:
        errors.append(f"{rel}: missing Open Graph URL metadata")
    elif og_url.group(1) != expected_url:
        errors.append(f"{rel}: og:url should be {expected_url}, got {og_url.group(1)}")
    for pattern, label in (
        (r'<meta property="og:title" content="([^"]+)"', "Open Graph title"),
        (r'<meta property="og:description" content="([^"]+)"', "Open Graph description"),
        (r'<meta name="twitter:card" content="summary"', "Twitter summary card"),
    ):
        if not re.search(pattern, source, re.I):
            errors.append(f"{rel}: missing {label} metadata")

# A custom 404 page should not be indexed as a content page.
not_found_page = ROOT / "404.html"
if not_found_page.exists():
    not_found_source = not_found_page.read_text(encoding="utf-8")
    if not re.search(r'<meta name="robots" content="noindex"', not_found_source, re.I):
        errors.append("404.html must include a robots noindex directive")

for title, paths in titles.items():
    if len(paths) > 1:
        errors.append(f"duplicate title {title!r}: " + ", ".join(paths))

robots = ROOT / "robots.txt"
if not robots.exists():
    errors.append("robots.txt is missing; keep the pre-launch crawl block until launch approval")
elif "Disallow: /" not in robots.read_text(encoding="utf-8"):
    errors.append("robots.txt no longer blocks crawling; update this guard only as part of an explicitly approved launch")
sitemap = ROOT / "sitemap.xml"
if sitemap.exists() and re.search(r"YOUR-DOMAIN|example[.]com|[.]example|localhost|127[.]0[.]0[.]1", sitemap.read_text(encoding="utf-8"), re.I):
    errors.append("sitemap.xml contains a domain placeholder or local URL; production sitemap must use https://beincasinos.online")
# Surface content whose market-specific primary-source review is still pending.
for page in pages:
    rel = page.relative_to(ROOT).as_posix()
    try:
        source = page.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        continue
    if re.search(r"Reviewed for launch: pending|review status: pending", source, re.I):
        warnings.append(f"{rel}: content review is explicitly pending; verify claims against current primary sources before launch")

for rel in ("privacy/index.html", "contact/index.html"):
    page = ROOT / rel
    if page.exists() and re.search(r"pre-launch|not yet been finalised|not yet been finalized|draft", page.read_text(encoding="utf-8"), re.I):
        warnings.append(f"{rel}: contains an explicit pre-launch notice and must be finalised before public launch")

# Validate that every sitemap URL points to an existing local HTML page.
if sitemap.exists():
    try:
        import xml.etree.ElementTree as ET
        sitemap_root = ET.fromstring(sitemap.read_text(encoding="utf-8"))
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        sitemap_urls = [((loc.text or "").strip()) for loc in sitemap_root.findall(".//sm:loc", ns)]
        seen_sitemap_urls = set()
        for url in sitemap_urls:
            if url in seen_sitemap_urls:
                errors.append(f"sitemap.xml: duplicate URL entry: {url}")
            seen_sitemap_urls.add(url)
        for url in sitemap_urls:
            parsed = urlparse(url)
            if parsed.scheme != "https" or parsed.netloc.casefold() != "beincasinos.online":
                errors.append(f"sitemap.xml: URL must use canonical origin https://beincasinos.online: {url}")
            if parsed.query or parsed.fragment:
                warnings.append(f"sitemap.xml: URL should not contain query or fragment: {url}")
            if parsed.scheme not in ("http", "https") or not parsed.netloc:
                errors.append(f"sitemap.xml: invalid absolute URL: {url}")
                continue
            sitemap_path = unquote(parsed.path or "/")
            target = ROOT / sitemap_path.lstrip("/")
            if target.is_dir():
                target = target / "index.html"
            elif not target.suffix:
                target = target / "index.html"
            try:
                target.resolve().relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"sitemap.xml: URL path escapes site root: {url}")
                continue
            if not target.is_file() or target.suffix.lower() not in (".html", ".htm"):
                errors.append(f"sitemap.xml: URL does not map to an HTML page: {url}")
        expected_paths = set()
        for page in pages:
            rel = page.relative_to(ROOT).as_posix()
            if rel == "404.html":
                continue
            if rel == "index.html":
                expected_paths.add("/")
            elif rel.endswith("/index.html"):
                expected_paths.add("/" + rel[:-len("index.html")])
            else:
                expected_paths.add("/" + rel)
        actual_paths = {urlparse(url).path or "/" for url in sitemap_urls}
        missing_paths = sorted(expected_paths - actual_paths)
        extra_paths = sorted(actual_paths - expected_paths)
        if missing_paths:
            errors.append("sitemap.xml: public HTML page(s) missing from sitemap: " + ", ".join(missing_paths))
        if extra_paths:
            errors.append("sitemap.xml: sitemap path(s) have no matching public HTML page: " + ", ".join(extra_paths))
    except (ET.ParseError, OSError, UnicodeError) as exc:
        errors.append(f"sitemap.xml: cannot parse sitemap XML ({exc})")

# Verify security headers in the static-host configuration rather than assuming they are active.
vercel_config = ROOT / "vercel.json"
if vercel_config.exists():
    try:
        import json
        config = json.loads(vercel_config.read_text(encoding="utf-8"))
        configured_headers = {
            item.get("key", "").casefold(): item.get("value", "")
            for rule in config.get("headers", [])
            for item in rule.get("headers", [])
        }
        required_headers = {
            "x-content-type-options": "nosniff",
            "referrer-policy": "strict-origin-when-cross-origin",
            "x-frame-options": "DENY",
            "strict-transport-security": "max-age=31536000",
            "x-permitted-cross-domain-policies": "none",
            "permissions-policy": "camera=(), microphone=(), geolocation=()",
        }
        for name, expected in required_headers.items():
            if configured_headers.get(name) != expected:
                errors.append(f"vercel.json: missing or unexpected security header {name}: expected {expected!r}")
    except (OSError, UnicodeError, ValueError) as exc:
        errors.append(f"vercel.json: cannot validate security headers ({exc})")
else:
    errors.append("vercel.json is missing; review static-host security header configuration")

# Validate the optional Netlify static-host configuration if present.
netlify_config = ROOT / "netlify.toml"
if netlify_config.exists():
    netlify_source = netlify_config.read_text(encoding="utf-8")
    required_netlify_headers = {
        "X-Content-Type-Options": "nosniff",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "X-Frame-Options": "DENY",
        "Permissions-Policy": "camera=(), microphone=(), geolocation=()",
        "Strict-Transport-Security": "max-age=31536000",
        "X-Permitted-Cross-Domain-Policies": "none",
    }
    for name, value in required_netlify_headers.items():
        expected_line = f'{name} = "{value}"'
        if expected_line not in netlify_source:
            errors.append(f"netlify.toml: missing or unexpected security header {name}: expected {value!r}")
    if 'publish = "."' not in netlify_source:
        errors.append('netlify.toml: static publish directory must remain "." for this root-based site')
# Keep the commercial research queue auditable; prospect count is not a publication target.
prospect_csv = ROOT / "docs/brand-research-template.csv"
if prospect_csv.exists():
    try:
        with prospect_csv.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            required_columns = {
                "brand_name", "official_url", "legal_entity", "regulator",
                "official_register_url", "license_scope", "markets_allowed",
                "markets_excluded", "last_checked_utc", "reviewer", "status",
                "publication_decision", "commercial_status", "unresolved_issues",
                "launch_year", "launch_year_source_url", "launch_type",
                "partnership_evidence_url", "listing_fee_fit_score", "fit_rationale",
                "sales_priority", "decision_maker_contact_source",
            }
            columns = reader.fieldnames or []
            missing_columns = sorted(required_columns - set(columns))
            if missing_columns:
                errors.append("docs/brand-research-template.csv: missing required column(s): " + ", ".join(missing_columns))
            if len(columns) != len(set(columns)):
                errors.append("docs/brand-research-template.csv: duplicate column names")
            if len(rows) != 100:
                errors.append(f"docs/brand-research-template.csv: expected 100 prospect rows, found {len(rows)}")
            names = [row.get("brand_name", "").strip().casefold() for row in rows]
            if any(not name for name in names):
                errors.append("docs/brand-research-template.csv: every prospect must have a brand name")
            duplicates = sorted(name for name in set(names) if name and names.count(name) > 1)
            if duplicates:
                errors.append("docs/brand-research-template.csv: duplicate brand name(s): " + ", ".join(duplicates))
            allowed_statuses = {"prospect", "researching", "verified_for_review", "approved_to_publish", "rejected", "published"}
            allowed_commercial = {"none", "paid listing", "affiliate", "both"}
            for index, row in enumerate(rows, start=2):
                status = row.get("status", "").strip()
                commercial = row.get("commercial_status", "").strip().casefold()
                if status not in allowed_statuses:
                    errors.append(f"docs/brand-research-template.csv:{index}: unsupported status {status!r}")
                if commercial not in allowed_commercial:
                    errors.append(f"docs/brand-research-template.csv:{index}: unsupported commercial_status {commercial!r}")
                if status in {"verified_for_review", "approved_to_publish", "published"}:
                    evidence_fields = ("official_url", "legal_entity", "official_register_url", "license_scope", "markets_allowed", "last_checked_utc", "reviewer")
                    missing_evidence = [field for field in evidence_fields if not row.get(field, "").strip()]
                    if missing_evidence:
                        errors.append(f"docs/brand-research-template.csv:{index}: status {status!r} requires evidence fields: " + ", ".join(missing_evidence))
                if status == "published" and row.get("publication_decision", "").strip().casefold() not in {"approved", "approved_to_publish", "publish"}:
                    errors.append(f"docs/brand-research-template.csv:{index}: published status requires an explicit approved publication_decision")
                launch_year = row.get("launch_year", "").strip()
                launch_type = row.get("launch_type", "").strip().casefold()
                launch_source = row.get("launch_year_source_url", "").strip()
                if launch_year:
                    if not launch_year.isdigit() or not 2022 <= int(launch_year) <= 2026:
                        errors.append(f"docs/brand-research-template.csv:{index}: launch_year must be a verified year from 2022 through 2026")
                    if not launch_source:
                        errors.append(f"docs/brand-research-template.csv:{index}: launch_year requires launch_year_source_url")
                    if launch_type not in {"new launch", "rebrand", "new market", "acquisition"}:
                        errors.append(f"docs/brand-research-template.csv:{index}: launch_year requires launch_type (new launch, rebrand, new market, or acquisition)")
                elif launch_source or launch_type:
                    errors.append(f"docs/brand-research-template.csv:{index}: launch source/type must not be set without a verified launch_year")
                score = row.get("listing_fee_fit_score", "").strip()
                if score:
                    try:
                        score_value = int(score)
                        if not 0 <= score_value <= 100:
                            raise ValueError
                    except ValueError:
                        errors.append(f"docs/brand-research-template.csv:{index}: listing_fee_fit_score must be an integer from 0 to 100")
                    if not row.get("fit_rationale", "").strip():
                        errors.append(f"docs/brand-research-template.csv:{index}: a fit score requires documented fit_rationale")
                    if row.get("sales_priority", "").strip().casefold() not in {"priority research/outreach", "further research", "hold", "reject"}:
                        errors.append(f"docs/brand-research-template.csv:{index}: a fit score requires sales_priority (priority research/outreach, further research, hold, reject)")
                elif row.get("fit_rationale", "").strip() or row.get("sales_priority", "").strip():
                    errors.append(f"docs/brand-research-template.csv:{index}: fit_rationale/sales_priority must be backed by a numeric listing_fee_fit_score")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"docs/brand-research-template.csv: cannot validate prospect tracker ({exc})")
else:
    errors.append("docs/brand-research-template.csv is missing")

# Guard the two interactive learning tools against accidental markup regressions.
calculator_path = ROOT / "tools/wagering-calculator/index.html"
if calculator_path.exists():
    calculator_source = calculator_path.read_text(encoding="utf-8")
    for required_id in ("wager-form", "eligible", "currency", "multiplier", "turnover", "result-summary", "calc-error"):
        if f'id="{required_id}"' not in calculator_source and f"id='{required_id}'" not in calculator_source:
            errors.append(f"tools/wagering-calculator/index.html: required calculator control missing: {required_id}")
    if "Number.isFinite(result)" not in calculator_source or "event.preventDefault()" not in calculator_source:
        errors.append("tools/wagering-calculator/index.html: calculation validation or form-submit handling is missing")
    for required_behavior in ("const showError = () =>", "output.textContent = '—'", "Correct the values marked as invalid to calculate required turnover.", "setAttribute('aria-invalid', String(amountInvalid))", "setAttribute('aria-invalid', String(multiplierInvalid))", "amount.addEventListener('input', calculate)", "multiplier.addEventListener('input', calculate"):
        if required_behavior not in calculator_source:
            errors.append(f"tools/wagering-calculator/index.html: invalid-input result reset behavior missing: {required_behavior}")

checklist_path = ROOT / "tools/terms-checklist/index.html"
if checklist_path.exists():
    checklist_source = checklist_path.read_text(encoding="utf-8")
    checkbox_count = len(re.findall(r'<input\b[^>]*type="checkbox"', checklist_source, re.I))
    if checkbox_count != 13:
        errors.append(f"tools/terms-checklist/index.html: expected 13 checklist items, found {checkbox_count}")
    for required_id in ("checked-count", "total-count", "progress-fill", "progress-track", "progress-message", "print-checklist", "reset-checklist"):
        if f'id="{required_id}"' not in checklist_source and f"id='{required_id}'" not in checklist_source:
            errors.append(f"tools/terms-checklist/index.html: required checklist control missing: {required_id}")
    for required_behavior in ("aria-valuenow", "aria-valuemax", "window.print()", "box.checked = false"):
        if required_behavior not in checklist_source:
            errors.append(f"tools/terms-checklist/index.html: expected interaction/accessibility behavior missing: {required_behavior}")

# Guard the shared navigation script against common keyboard/state regressions.
script_path = ROOT / "script.js"
if script_path.exists():
    script_source = script_path.read_text(encoding="utf-8")
    for required_behavior in (
        "document.querySelector('.menu-toggle')",
        "document.querySelector('#primary-nav')",
        "getAttribute('aria-expanded')",
        "setAttribute('aria-expanded', String(!expanded))",
        "nav.classList.toggle('open', !expanded)",
        "nav.classList.remove('open')",
        "document.addEventListener('keydown'",
        "event.key === 'Escape'",
        "closeMenu(true)",
    ):
        if required_behavior not in script_source:
            errors.append(f"script.js: expected responsive navigation behavior missing: {required_behavior}")
else:
    errors.append("script.js: shared navigation script is missing")

# Validate the paid-listing sales tracker before any commercial outreach.
sales_csv = ROOT / "docs/paid-listing-sales-pipeline.csv"
if sales_csv.exists():
    try:
        with sales_csv.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            required_columns = {
                "brand_name", "legal_entity", "target_market", "official_contact_source",
                "qualification_status", "pipeline_stage", "owner", "placement_type",
                "quoted_price", "currency", "agreement_status", "invoice_status",
                "paid_label_confirmed", "market_review_confirmed",
                "privacy_tracking_review", "source_evidence_url", "do_not_contact_reason",
            }
            columns = reader.fieldnames or []
            missing_columns = sorted(required_columns - set(columns))
            if missing_columns:
                errors.append("docs/paid-listing-sales-pipeline.csv: missing required column(s): " + ", ".join(missing_columns))
            if len(columns) != len(set(columns)):
                errors.append("docs/paid-listing-sales-pipeline.csv: duplicate column names")
            stages = {
                "not_contacted", "qualified", "draft_ready", "contacted",
                "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won",
                "lost", "do_not_contact",
            }
            for index, row in enumerate(rows, start=2):
                brand = row.get("brand_name", "").strip()
                stage = row.get("pipeline_stage", "").strip()
                if not brand and not any(value.strip() for value in row.values() if value):
                    continue
                if not brand:
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: populated row requires brand_name")
                if stage not in stages:
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: unsupported pipeline_stage {stage!r}")
                if stage == "do_not_contact" and not row.get("do_not_contact_reason", "").strip():
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: do_not_contact requires a reason")
                if stage in {"qualified", "draft_ready", "contacted", "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won"}:
                    for field in ("legal_entity", "target_market", "official_contact_source", "source_evidence_url", "owner"):
                        if not row.get(field, "").strip():
                            errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: stage {stage!r} requires {field}")
                if stage in {"contacted", "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won"} and not row.get("first_contact_date_utc", "").strip():
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: stage {stage!r} requires first_contact_date_utc")
                if stage == "won":
                    if row.get("agreement_status", "").strip().casefold() not in {"signed", "complete", "executed"}:
                        errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: won requires a signed/complete agreement status")
                    for field in ("paid_label_confirmed", "market_review_confirmed", "privacy_tracking_review"):
                        if row.get(field, "").strip().casefold() not in {"yes", "complete", "approved", "reviewed"}:
                            errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: won requires {field} to be confirmed")
                    if row.get("invoice_status", "").strip().casefold() not in {"paid", "complete"}:
                        errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: won requires invoice_status to be paid/complete")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"docs/paid-listing-sales-pipeline.csv: cannot validate sales tracker ({exc})")
else:
    errors.append("docs/paid-listing-sales-pipeline.csv is missing")

# Keep launch-planning documents present so critical approval gates cannot silently disappear.
for required_doc in ("docs/prelaunch-launch-checklist.md", "docs/audience-growth-measurement-plan.md", "docs/paid-listing-sales-pipeline.md"):
    if not (ROOT / required_doc).is_file():
        errors.append(f"{required_doc} is missing")

print(f"Checked {len(pages)} HTML pages.")
if errors:
    print(f"\nFAIL: {len(errors)} error(s)")
    for item in errors:
        print(f"  ERROR: {item}")
if warnings:
    print(f"\nWARN: {len(warnings)} launch/verification warning(s)")
    for item in warnings:
        print(f"  WARN: {item}")
if not errors:
    print("\nPASS: no structural errors detected by this source-level checker.")
    print("Reminder: this does not test rendering, accessibility, external links, legal compliance, or production behaviour.")
sys.exit(1 if errors else 0)
, netlify_source, re.M):
        errors.append('netlify.toml: static publish directory must remain "." for this root-based site')

# Keep the commercial research queue auditable; prospect count is not a publication target.
prospect_csv = ROOT / "docs/brand-research-template.csv"
if prospect_csv.exists():
    try:
        with prospect_csv.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            required_columns = {
                "brand_name", "official_url", "legal_entity", "regulator",
                "official_register_url", "license_scope", "markets_allowed",
                "markets_excluded", "last_checked_utc", "reviewer", "status",
                "publication_decision", "commercial_status", "unresolved_issues",
                "launch_year", "launch_year_source_url", "launch_type",
                "partnership_evidence_url", "listing_fee_fit_score", "fit_rationale",
                "sales_priority", "decision_maker_contact_source",
            }
            columns = reader.fieldnames or []
            missing_columns = sorted(required_columns - set(columns))
            if missing_columns:
                errors.append("docs/brand-research-template.csv: missing required column(s): " + ", ".join(missing_columns))
            if len(columns) != len(set(columns)):
                errors.append("docs/brand-research-template.csv: duplicate column names")
            if len(rows) != 100:
                errors.append(f"docs/brand-research-template.csv: expected 100 prospect rows, found {len(rows)}")
            names = [row.get("brand_name", "").strip().casefold() for row in rows]
            if any(not name for name in names):
                errors.append("docs/brand-research-template.csv: every prospect must have a brand name")
            duplicates = sorted(name for name in set(names) if name and names.count(name) > 1)
            if duplicates:
                errors.append("docs/brand-research-template.csv: duplicate brand name(s): " + ", ".join(duplicates))
            allowed_statuses = {"prospect", "researching", "verified_for_review", "approved_to_publish", "rejected", "published"}
            allowed_commercial = {"none", "paid listing", "affiliate", "both"}
            for index, row in enumerate(rows, start=2):
                status = row.get("status", "").strip()
                commercial = row.get("commercial_status", "").strip().casefold()
                if status not in allowed_statuses:
                    errors.append(f"docs/brand-research-template.csv:{index}: unsupported status {status!r}")
                if commercial not in allowed_commercial:
                    errors.append(f"docs/brand-research-template.csv:{index}: unsupported commercial_status {commercial!r}")
                if status in {"verified_for_review", "approved_to_publish", "published"}:
                    evidence_fields = ("official_url", "legal_entity", "official_register_url", "license_scope", "markets_allowed", "last_checked_utc", "reviewer")
                    missing_evidence = [field for field in evidence_fields if not row.get(field, "").strip()]
                    if missing_evidence:
                        errors.append(f"docs/brand-research-template.csv:{index}: status {status!r} requires evidence fields: " + ", ".join(missing_evidence))
                if status == "published" and row.get("publication_decision", "").strip().casefold() not in {"approved", "approved_to_publish", "publish"}:
                    errors.append(f"docs/brand-research-template.csv:{index}: published status requires an explicit approved publication_decision")
                launch_year = row.get("launch_year", "").strip()
                launch_type = row.get("launch_type", "").strip().casefold()
                launch_source = row.get("launch_year_source_url", "").strip()
                if launch_year:
                    if not launch_year.isdigit() or not 2022 <= int(launch_year) <= 2026:
                        errors.append(f"docs/brand-research-template.csv:{index}: launch_year must be a verified year from 2022 through 2026")
                    if not launch_source:
                        errors.append(f"docs/brand-research-template.csv:{index}: launch_year requires launch_year_source_url")
                    if launch_type not in {"new launch", "rebrand", "new market", "acquisition"}:
                        errors.append(f"docs/brand-research-template.csv:{index}: launch_year requires launch_type (new launch, rebrand, new market, or acquisition)")
                elif launch_source or launch_type:
                    errors.append(f"docs/brand-research-template.csv:{index}: launch source/type must not be set without a verified launch_year")
                score = row.get("listing_fee_fit_score", "").strip()
                if score:
                    try:
                        score_value = int(score)
                        if not 0 <= score_value <= 100:
                            raise ValueError
                    except ValueError:
                        errors.append(f"docs/brand-research-template.csv:{index}: listing_fee_fit_score must be an integer from 0 to 100")
                    if not row.get("fit_rationale", "").strip():
                        errors.append(f"docs/brand-research-template.csv:{index}: a fit score requires documented fit_rationale")
                    if row.get("sales_priority", "").strip().casefold() not in {"priority research/outreach", "further research", "hold", "reject"}:
                        errors.append(f"docs/brand-research-template.csv:{index}: a fit score requires sales_priority (priority research/outreach, further research, hold, reject)")
                elif row.get("fit_rationale", "").strip() or row.get("sales_priority", "").strip():
                    errors.append(f"docs/brand-research-template.csv:{index}: fit_rationale/sales_priority must be backed by a numeric listing_fee_fit_score")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"docs/brand-research-template.csv: cannot validate prospect tracker ({exc})")
else:
    errors.append("docs/brand-research-template.csv is missing")

# Guard the two interactive learning tools against accidental markup regressions.
calculator_path = ROOT / "tools/wagering-calculator/index.html"
if calculator_path.exists():
    calculator_source = calculator_path.read_text(encoding="utf-8")
    for required_id in ("wager-form", "eligible", "currency", "multiplier", "turnover", "result-summary", "calc-error"):
        if f'id="{required_id}"' not in calculator_source and f"id='{required_id}'" not in calculator_source:
            errors.append(f"tools/wagering-calculator/index.html: required calculator control missing: {required_id}")
    if "Number.isFinite(result)" not in calculator_source or "event.preventDefault()" not in calculator_source:
        errors.append("tools/wagering-calculator/index.html: calculation validation or form-submit handling is missing")
    for required_behavior in ("const showError = () =>", "output.textContent = '—'", "Correct the values marked as invalid to calculate required turnover.", "setAttribute('aria-invalid', String(amountInvalid))", "setAttribute('aria-invalid', String(multiplierInvalid))", "amount.addEventListener('input', calculate)", "multiplier.addEventListener('input', calculate"):
        if required_behavior not in calculator_source:
            errors.append(f"tools/wagering-calculator/index.html: invalid-input result reset behavior missing: {required_behavior}")

checklist_path = ROOT / "tools/terms-checklist/index.html"
if checklist_path.exists():
    checklist_source = checklist_path.read_text(encoding="utf-8")
    checkbox_count = len(re.findall(r'<input\b[^>]*type="checkbox"', checklist_source, re.I))
    if checkbox_count != 13:
        errors.append(f"tools/terms-checklist/index.html: expected 13 checklist items, found {checkbox_count}")
    for required_id in ("checked-count", "total-count", "progress-fill", "progress-track", "progress-message", "print-checklist", "reset-checklist"):
        if f'id="{required_id}"' not in checklist_source and f"id='{required_id}'" not in checklist_source:
            errors.append(f"tools/terms-checklist/index.html: required checklist control missing: {required_id}")
    for required_behavior in ("aria-valuenow", "aria-valuemax", "window.print()", "box.checked = false"):
        if required_behavior not in checklist_source:
            errors.append(f"tools/terms-checklist/index.html: expected interaction/accessibility behavior missing: {required_behavior}")

# Guard the shared navigation script against common keyboard/state regressions.
script_path = ROOT / "script.js"
if script_path.exists():
    script_source = script_path.read_text(encoding="utf-8")
    for required_behavior in (
        "document.querySelector('.menu-toggle')",
        "document.querySelector('#primary-nav')",
        "getAttribute('aria-expanded')",
        "setAttribute('aria-expanded', String(!expanded))",
        "nav.classList.toggle('open', !expanded)",
        "nav.classList.remove('open')",
        "document.addEventListener('keydown'",
        "event.key === 'Escape'",
        "closeMenu(true)",
    ):
        if required_behavior not in script_source:
            errors.append(f"script.js: expected responsive navigation behavior missing: {required_behavior}")
else:
    errors.append("script.js: shared navigation script is missing")

# Validate the paid-listing sales tracker before any commercial outreach.
sales_csv = ROOT / "docs/paid-listing-sales-pipeline.csv"
if sales_csv.exists():
    try:
        with sales_csv.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
            required_columns = {
                "brand_name", "legal_entity", "target_market", "official_contact_source",
                "qualification_status", "pipeline_stage", "owner", "placement_type",
                "quoted_price", "currency", "agreement_status", "invoice_status",
                "paid_label_confirmed", "market_review_confirmed",
                "privacy_tracking_review", "source_evidence_url", "do_not_contact_reason",
            }
            columns = reader.fieldnames or []
            missing_columns = sorted(required_columns - set(columns))
            if missing_columns:
                errors.append("docs/paid-listing-sales-pipeline.csv: missing required column(s): " + ", ".join(missing_columns))
            if len(columns) != len(set(columns)):
                errors.append("docs/paid-listing-sales-pipeline.csv: duplicate column names")
            stages = {
                "not_contacted", "qualified", "draft_ready", "contacted",
                "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won",
                "lost", "do_not_contact",
            }
            for index, row in enumerate(rows, start=2):
                brand = row.get("brand_name", "").strip()
                stage = row.get("pipeline_stage", "").strip()
                if not brand and not any(value.strip() for value in row.values() if value):
                    continue
                if not brand:
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: populated row requires brand_name")
                if stage not in stages:
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: unsupported pipeline_stage {stage!r}")
                if stage == "do_not_contact" and not row.get("do_not_contact_reason", "").strip():
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: do_not_contact requires a reason")
                if stage in {"qualified", "draft_ready", "contacted", "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won"}:
                    for field in ("legal_entity", "target_market", "official_contact_source", "source_evidence_url", "owner"):
                        if not row.get(field, "").strip():
                            errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: stage {stage!r} requires {field}")
                if stage in {"contacted", "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won"} and not row.get("first_contact_date_utc", "").strip():
                    errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: stage {stage!r} requires first_contact_date_utc")
                if stage == "won":
                    if row.get("agreement_status", "").strip().casefold() not in {"signed", "complete", "executed"}:
                        errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: won requires a signed/complete agreement status")
                    for field in ("paid_label_confirmed", "market_review_confirmed", "privacy_tracking_review"):
                        if row.get(field, "").strip().casefold() not in {"yes", "complete", "approved", "reviewed"}:
                            errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: won requires {field} to be confirmed")
                    if row.get("invoice_status", "").strip().casefold() not in {"paid", "complete"}:
                        errors.append(f"docs/paid-listing-sales-pipeline.csv:{index}: won requires invoice_status to be paid/complete")
    except (OSError, UnicodeError, csv.Error) as exc:
        errors.append(f"docs/paid-listing-sales-pipeline.csv: cannot validate sales tracker ({exc})")
else:
    errors.append("docs/paid-listing-sales-pipeline.csv is missing")

# Keep launch-planning documents present so critical approval gates cannot silently disappear.
for required_doc in ("docs/prelaunch-launch-checklist.md", "docs/audience-growth-measurement-plan.md", "docs/paid-listing-sales-pipeline.md"):
    if not (ROOT / required_doc).is_file():
        errors.append(f"{required_doc} is missing")

print(f"Checked {len(pages)} HTML pages.")
if errors:
    print(f"\nFAIL: {len(errors)} error(s)")
    for item in errors:
        print(f"  ERROR: {item}")
if warnings:
    print(f"\nWARN: {len(warnings)} launch/verification warning(s)")
    for item in warnings:
        print(f"  WARN: {item}")
if not errors:
    print("\nPASS: no structural errors detected by this source-level checker.")
    print("Reminder: this does not test rendering, accessibility, external links, legal compliance, or production behaviour.")
sys.exit(1 if errors else 0)
