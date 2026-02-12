# RHTP Hugo: Consolidated Fix Plan

## Ground Rules

**No regeneration.** Summaries, images, and lead-ins stay as generated. All fixes operate on existing files through post-processing scripts, CSS/layout changes, and Hugo config. Zero API calls. Zero cost.

**Previously resolved:** Cover images render (Bug 6). Pagination syntax is current (Bug 7). This plan addresses **eight remaining bugs** plus **six enhancement requests** plus **three newly identified issues**.


## Part A: Hugo Configuration Fixes

### A1: Series Pages Beyond Series 3 Show No Articles

**Root Cause:** `process_articles.py` line 236 sets `START_DATE = datetime(2026, 1, 1)` and assigns sequential daily dates. With 238 articles, anything past article ~43 gets a future date. Hugo's default `buildFuture = false` means those articles never appear in the build output. Series 1 has 14 articles, Series 2 has 11, Series 3 starts at article 26. Only the first ~18 articles of Series 3 fall before today's date. Everything from mid-Series 3 onward is invisible.

**Fix:** Add one line to `hugo.toml` at the top level, outside any `[params]` block:

```toml
buildFuture = true
```

**Later improvement:** When regenerating bundles for other reasons, backdate `START_DATE` to `datetime(2025, 1, 1)` so dates look more natural. The `buildFuture = true` flag is the instant fix with zero regeneration.


### A2: Missing Search, Archives, and About Pages

PaperMod requires specific content files for these routes. The menu links exist in `hugo.toml` but the content pages were never created.

**Search Page.** Create `content/search.md`:

```markdown
---
title: "Search"
layout: "search"
url: "/search/"
summary: "Search all articles"
placeholder: "Search articles by title, topic, or keyword..."
---
```

PaperMod's built-in search layout handles everything. The `fuseOpts` in `hugo.toml` are already configured. The `[outputs] home = ["HTML", "RSS", "JSON"]` is already set, generating the `index.json` that Fuse.js needs.

**Archives Page.** Create `content/archives.md`:

```markdown
---
title: "Archives"
layout: "archives"
url: "/archives/"
summary: "All articles by date"
---
```

PaperMod's built-in archives layout lists all posts grouped by year and month.

**About Page.** Create `content/about.md`:

```markdown
---
title: "About"
url: "/about/"
summary: "About the author"
showtoc: false
ShowReadingTime: false
ShowWordCount: false
ShowBreadCrumbs: true
hidemeta: true
---

## Syam Adusumilli

52 years old. MPH from Brown University. 33 years in technology and healthcare globally, primarily in the US.

Currently **Chief Strategy Officer at GroundGame.Health**, focused on go-to-market strategy, business strategy, and public policy for a platform that manages complex connections between health plans, providers, employers, and community-based organizations.

Previously **Chief Healthcare Transformation Officer at UST Global**, **VP of Product Management and Architecture at HealthPlan Services**, **VP of Technology at UnitedHealth Group**, and **Director of Technology at Wellpoint Inc.** Started career as a **Senior Consulting Architect at IBM Global Services**.

Deep expertise in **Data Science and AI, Blockchain, Medical IoT, Voice Biometrics, Computational Epidemiology, Digital Therapeutics, Human Centric Design, Behavioral Nudge, and Care Plan Personalization**.

Member of **Forbes Technology Council**. Research interests in epidemiology and public health education through Brown University's School of Public Health.

### About This Site

This site hosts two long-form analytical series:

**Rural Health Transformation Project** examines the $50 billion federal Rural Health Transformation Program across all 50 states. The analysis covers federal policy architecture, state implementation strategies, evidence-based interventions, stakeholder ecosystems, special populations, and regional variation. The series asks whether rural health transformation can succeed when federal investment is accompanied by simultaneous Medicaid coverage erosion.

**Medicaid Work Requirements** analyzes the policy, implementation, and population impact of Medicaid work requirement programs across states pursuing these waivers.

Both series prioritize **honest assessment over advocacy**, documenting what evidence supports versus what represents aspirational goals.

### Other Projects

**[The Approximate Mind](https://theapproximatemind.com)** explores the intersections of Philosophy, Psychology, Anthropology, and Artificial Intelligence. Co-authored with Yagn Adusumilli.

**[Blue Gray Matters](https://bluegraymatters.com)** covers neurodivergent perspectives on technology and society.

### Contact

[LinkedIn](https://www.linkedin.com/in/syamadusumilli/)
```

Adjust any details that need updating. The bio pulls from TAM's project hub, The Org profile, and the HLTH podcast bio.


## Part B: Post-Processing Script (Fix Existing Files In-Place)

A single Python script, `fix_hugo_bundles.py`, runs against the existing `content/rural-health/` directory. No API keys needed. No network calls. Pure file manipulation.

### B1: Summary Pages Missing Cover Images

Walk every `-summary/` directory. Copy `cover.webp` from the sibling article directory. Patch the summary `index.md` front matter to add the `cover:` block.

```python
# For each summary_dir in content/rural-health/series-*/
#   article_slug = summary_dir.name.replace("-summary", "")
#   article_dir = summary_dir.parent / article_slug
#   if article_dir / "cover.webp" exists:
#       shutil.copy2(article_dir / "cover.webp", summary_dir / "cover.webp")
#   Inject cover block into summary index.md front matter (after ShowBreadCrumbs line)
```

### B2: Summary Title Displayed Twice

For every summary `index.md`, strip any leading H1 or bold title line from the content body below the closing `---`. The front matter `title:` already renders the heading via PaperMod. The duplicate must go.

```python
# Read content after second "---"
# If first non-empty line starts with "# " or "**Executive Summary" or matches the title:
#   Remove that line
# Write back
```

### B3: Broken Slugs (7-8 Articles)

The root cause for **Series 5A/5B** is that `extract_content()` returns `display_title = "RHTP 5.A"` because the H1 is just an ID label (`# RHTP 5.A`) with no title text after it. The real title lives in the H2 which gets captured as `subtitle`. The slug generator then uses the ID-style display_title.

For **5C/5D**, the same pattern applies but the slug also retains version suffixes.

For **3-TD-E files**, acronyms like `SDOHHRSNCHWCIE` collapse into one slug segment without hyphens.

For **9P**, `intellectualdevelopm` is a truncation of the full title.

**Fix approach:** Rename directories directly. No re-parsing needed.

| Current Directory | New Directory |
|---|---|
| `series-5/rhtp-5a/` | `series-5/lead-agency-structures/` |
| `series-5/rhtp-5b/` | `series-5/stakeholder-coordination/` |
| `series-5/rhtp5cprocurementcontractingv1/` | `series-5/procurement-and-contracting/` |
| `series-5/rhtp5dperformancemeasurementv1/` | `series-5/performance-measurement/` |
| `series-5/rhtp-5a-summary/` | `series-5/lead-agency-structures-summary/` |
| `series-5/rhtp-5b-summary/` | `series-5/stakeholder-coordination-summary/` |
| `series-5/rhtp5cprocurementcontractingv1-summary/` | `series-5/procurement-and-contracting-summary/` |
| `series-5/rhtp5dperformancemeasurementv1-summary/` | `series-5/performance-measurement-summary/` |

For 3-TD-E and 9P, verify exact current directory names first, then rename similarly.

After renaming, patch the `slug` references inside each article's `params.summary_url` and each summary's `params.full_article_url` in front matter.

### B4: Summaries Appearing in Article Listings

Patch every summary `index.md` front matter to add `_build: list: never` before the closing `---`. This tells Hugo to render the page but hide it from all list views, archives, and RSS.

```python
# For each summary index.md:
#   If "_build:" not in front_matter:
#       Insert before closing "---":
#           _build:
#             list: never
```

### B5: Cross-References as Plain Text (201 Articles Affected)

The Cross-References sections use varied plain-text formats referencing other articles by ID, state name, or title. These need to become clickable links to the actual Hugo pages.

**Cross-reference patterns found in source articles:**

| Pattern | Example | Target Article ID |
|---|---|---|
| `**2A (Title):**` | `**2A (RHTP Structure and Rules):**` | RHTP-2A |
| `2B (Title):` | `2B (Medicaid Architecture):` | RHTP-2B |
| `Article 2C:` | `Article 2C: Medicare Rural Provisions` | RHTP-2C |
| `3-VT (State):` | `3-VT (Vermont):` | RHTP-3VT |
| `RHTP 3.XX (State):` | `RHTP 3.KY (Kentucky):` | RHTP-3KY |
| `State profile` | `Montana profile` | RHTP-3MT |
| `TD-X:` | `TD-B: Provider Reimbursement` | Context-dependent |
| `N-TD-X:` | `8-TD-A: Community Org Capacity` | RHTP-8-TD-A |
| `RHTP N.X (Title):` | `RHTP 9.H (Appalachian Communities):` | RHTP-9H |
| `Article NA:` | `Article 4C: Telehealth` | RHTP-4C |
| `Synthesis:` | `Synthesis: Which State Agency...` | RHTP-5-Syn |

**Approach:** Build a lookup table from the manifest mapping article_id to `(series_num, slug)`. For each Hugo `index.md`, find the `## Cross-References` section. For each bullet line, extract the article ID using regex, look up the Hugo URL, and wrap the reference in a markdown link.

Before:
```markdown
- **2A (RHTP Structure and Rules):** Federal statutory framework
```

After:
```markdown
- [**2A (RHTP Structure and Rules)**](/rural-health/series-2/rhtp-structure-and-rules/): Federal statutory framework
```

Lines that cannot be resolved (generic references like "3 State Profiles" pointing to an entire series) get linked to the series index page instead: `/rural-health/series-3/`.

The script builds the ID-to-URL map from the existing `manifest.json` generated by Pass 3, then processes all Hugo `index.md` files.


## Part C: CSS Customizations

All CSS goes in `assets/css/extended/custom.css`. PaperMod auto-loads this file.

### C1: Title and H1 Font Size Reduction

```css
.post-single .post-title {
    font-size: 1.8rem;
    line-height: 1.25;
}

.post-single .post-content h1 {
    font-size: 1.5rem;
}

.post-single .post-content h2 {
    font-size: 1.3rem;
}
```

### C2: Cover Image Sizing on Article Pages

Currently images consume nearly the full viewport width. Constrain them.

```css
.post-single .entry-cover {
    max-width: 720px;
    margin: 0 auto 1.5rem;
}

.post-single .entry-cover img {
    max-width: 100%;
    height: auto;
    border-radius: 6px;
}
```

### C3: Tiled Two-Column List Layout with Small Thumbnails

PaperMod's default list renders full-width entries stacked vertically with large images. Override with a two-column tile grid showing small thumbnails alongside the title and summary link.

```css
.post-entry {
    display: grid;
    grid-template-columns: 120px 1fr;
    gap: 0.75rem;
    align-items: start;
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--border);
}

.post-entry .entry-cover {
    width: 120px;
    height: 80px;
    overflow: hidden;
    border-radius: 4px;
    flex-shrink: 0;
}

.post-entry .entry-cover img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.post-entry .entry-header h2 {
    font-size: 1rem;
    line-height: 1.3;
    margin: 0 0 0.25rem;
}

.post-entry .entry-content {
    font-size: 0.85rem;
    line-height: 1.4;
    color: var(--secondary);
    margin: 0;
}

.post-entry .entry-header,
.post-entry .entry-footer {
    padding: 0;
}

@media (min-width: 900px) {
    .main .post-entry {
        grid-template-columns: 140px 1fr;
    }
}

@media (max-width: 600px) {
    .post-entry {
        grid-template-columns: 80px 1fr;
    }
    .post-entry .entry-cover {
        width: 80px;
        height: 55px;
    }
}
```

### C4: Executive Summary Link Styling

```css
.summary-link-inline {
    font-size: 0.75rem;
    color: var(--secondary);
    text-decoration: none;
    display: inline-block;
    margin-top: 0.25rem;
}

.summary-link-inline:hover {
    color: var(--primary);
}
```

### C5: Numbered Pagination

```css
.pagination ul {
    display: flex;
    list-style: none;
    padding: 0;
    gap: 4px;
    justify-content: center;
    flex-wrap: wrap;
}

.pagination li a,
.pagination li span {
    display: block;
    padding: 6px 12px;
    border-radius: 4px;
    text-decoration: none;
    font-size: 0.9rem;
}

.pagination li a {
    color: var(--primary);
    border: 1px solid var(--border);
}

.pagination li a:hover {
    background: var(--primary);
    color: var(--theme);
}

.pagination li.active span {
    background: var(--primary);
    color: var(--theme);
    border: 1px solid var(--primary);
}

.pagination li.dots span {
    border: none;
    padding: 6px 4px;
}
```


## Part D: Hugo Layout Overrides

### D1: Numbered Pagination Partial

PaperMod's default list template only renders prev/next navigation with no numbered page links.

**File:** `layouts/partials/pagination.html`

```html
{{ $pag := .Paginator }}
{{ if gt $pag.TotalPages 1 }}
<nav class="pagination" role="navigation" aria-label="Pagination">
  <ul>
    {{ if $pag.HasPrev }}
    <li><a href="{{ $pag.First.URL }}" aria-label="First page">&laquo;</a></li>
    <li><a href="{{ $pag.Prev.URL }}" aria-label="Previous page">&lsaquo;</a></li>
    {{ end }}

    {{ $adjacent := 2 }}
    {{ $start := math.Max 1 (sub $pag.PageNumber $adjacent) }}
    {{ $end := math.Min $pag.TotalPages (add $pag.PageNumber $adjacent) }}

    {{ if gt $start 1 }}
    <li><a href="{{ (index $pag.Pagers 0).URL }}">1</a></li>
    {{ if gt $start 2 }}<li class="dots"><span>...</span></li>{{ end }}
    {{ end }}

    {{ range $pag.Pagers }}
      {{ if and (ge .PageNumber $start) (le .PageNumber $end) }}
        {{ if eq .PageNumber $pag.PageNumber }}
        <li class="active"><span>{{ .PageNumber }}</span></li>
        {{ else }}
        <li><a href="{{ .URL }}">{{ .PageNumber }}</a></li>
        {{ end }}
      {{ end }}
    {{ end }}

    {{ if lt $end $pag.TotalPages }}
    {{ if lt (add $end 1) $pag.TotalPages }}<li class="dots"><span>...</span></li>{{ end }}
    <li><a href="{{ (index $pag.Pagers (sub $pag.TotalPages 1)).URL }}">{{ $pag.TotalPages }}</a></li>
    {{ end }}

    {{ if $pag.HasNext }}
    <li><a href="{{ $pag.Next.URL }}" aria-label="Next page">&rsaquo;</a></li>
    <li><a href="{{ $pag.Last.URL }}" aria-label="Last page">&raquo;</a></li>
    {{ end }}
  </ul>
</nav>
{{ end }}
```

Renders as: **first | prev | 1 ... 4 5 [6] 7 8 ... 12 | next | last**

### D2: Summary Link on Article Pages

**File:** `layouts/partials/summary-link.html`

```html
{{ with .Params.summary_url }}
<div style="margin: 0.75rem 0 1.5rem; padding: 0.5rem 0.75rem;
     background: var(--code-bg); border-radius: 4px; font-size: 0.85rem;">
  <a href="{{ . }}" style="text-decoration: none; color: var(--primary);">
    Read the Executive Summary
  </a>
</div>
{{ end }}
```

### D3: Single Page Layout Override

**File:** `layouts/_default/single.html`

Copy PaperMod's `themes/PaperMod/layouts/_default/single.html` and insert the summary link partial after the post header/meta block, before `.Content`:

```html
{{- partial "summary-link.html" . -}}
```

This is also where the sidebar injection goes later (confirmed decision: sidebar with series navigation).

### D4: List Template Override for Tiled View with Summary Links and Numbered Pagination

**File:** `layouts/_default/list.html`

Override PaperMod's list template. For each entry, render a small thumbnail, article title, one-line summary text, and inline "Executive Summary" link. Replace PaperMod's default pagination with the numbered pagination partial.

```html
{{- define "main" }}
<header class="page-header">
  <h1>{{ .Title }}</h1>
  {{- if .Description }}
  <div class="post-description">{{ .Description }}</div>
  {{- end }}
</header>

{{- $pages := where .Pages "Params.is_summary" "ne" true }}
{{- range $pages }}
<article class="post-entry">
  {{- $cover := .Resources.GetMatch "cover.*" }}
  {{- if $cover }}
  <div class="entry-cover">
    <a href="{{ .Permalink }}">
      <img src="{{ $cover.RelPermalink }}" alt="{{ .Title }}" loading="lazy" />
    </a>
  </div>
  {{- end }}
  <div class="entry-content-wrapper">
    <header class="entry-header">
      <h2><a href="{{ .Permalink }}">{{ .Title }}</a></h2>
    </header>
    {{- if .Summary }}
    <div class="entry-content">
      <p>{{ .Summary | plainify | truncate 120 }}</p>
    </div>
    {{- end }}
    {{- with .Params.summary_url }}
    <a href="{{ . }}" class="summary-link-inline">Executive Summary</a>
    {{- end }}
  </div>
</article>
{{- end }}

{{ partial "pagination.html" . }}
{{- end }}
```

This template filters out summary pages from lists (the `where` clause checks `is_summary`), providing a backup to the `_build: list: never` front matter fix. It also calls the numbered pagination partial instead of PaperMod's default prev/next navigation.


## Part E: Script Patches for Future Runs (process_articles.py)

These patches fix root causes so any future re-run (for WR pipeline or corrections) produces correct output. They do not trigger re-generation of existing content.

### E1: extract_content() Title Extraction Fix

The current code fails when H1 is just an ID label like `# RHTP 5.A` with no title text. The actual title lives in the H2 subtitle.

**Line ~486-501, replace the `elif len(h1_lines) == 1:` block:**

```python
    elif len(h1_lines) == 1:
        raw = h1_lines[0]
        if re.match(r"^Technical Document\s+\d+-TD-[A-Z]", raw) and subtitle:
            display_title = subtitle
            subtitle = ""
        elif re.match(r"^RHTP\s+[\d.]+[A-Z]?$", raw) and subtitle:
            display_title = subtitle
            subtitle = ""
        else:
            m = re.match(r"^(?:Article|RHTP|Technical Document)\s+[\d.A-Z-]+[:\s]+(.+)", raw)
            if m:
                display_title = m.group(1).strip()
            else:
                display_title = raw
```

### E2: generate_slug() Improvements

```python
def generate_slug(display_title, article_id, state_info=None):
    """Generate URL-friendly slug."""
    state_code, state_name, part, part_title = state_info or (None, None, None, None)
    if state_name and part and part_title:
        raw = f"{state_name} {part_title}"
    elif state_name:
        raw = state_name
    elif display_title and not re.match(r"^RHTP[\s_.-]?\d+", display_title, re.IGNORECASE):
        raw = display_title
    else:
        raw = article_id

    slug = raw.lower()

    # Strip version suffixes before cleanup
    slug = re.sub(r'[_\s]?v\d+\s*$', '', slug)

    # Insert hyphens between known adjacent acronyms
    acronyms = r'(sdoh|hrsn|chw|cie|idd|fqhc|ems|pca|ahec|rhio)'
    slug = re.sub(f'({acronyms})({acronyms})', r'\1-\3', slug)
    slug = re.sub(f'({acronyms})({acronyms})', r'\1-\3', slug)  # second pass

    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug[:80]
```

### E3: Cost Optimization (for WR Pipeline)

The current script makes individual API calls per article. For the Work Requirements pipeline (~140 articles), add these optimizations:

**Message Batches API.** Anthropic's batch endpoint processes up to 10,000 requests asynchronously at 50% cost. Collect all prompt-generation requests into a batch, submit, poll for completion, then process results.

**Prompt Caching.** The system prompts (`IMAGE_PROMPT_STYLE`, `SUMMARY_STYLE`) are identical across all calls. Use Anthropic's prompt caching to cache the system message on the first call, reducing input token costs by ~90% for subsequent calls.

```python
system_message = [
    {
        "type": "text",
        "text": IMAGE_PROMPT_STYLE,
        "cache_control": {"type": "ephemeral"}
    }
]
```

**Model Assignment.** Image prompts are simple creative tasks. Summaries require analytical quality but are condensation not original analysis. Both tasks use `claude-haiku-4-5` for cost priority.

**Token Limit Awareness.** Some articles exceed 10,000 words. Truncate to first 150K characters (~37K tokens) to stay within Haiku's context window with margin.

**Rate Limiting.** For batched operation, no per-call delay needed. For sequential fallback, 1s delay with exponential backoff on 429s.

**Cost Estimate for WR Pipeline (140 articles):**

| Component | Model | Est. Input Tokens | Est. Output Tokens | Est. Cost |
|---|---|---|---|---|
| Image prompts (batched) | Haiku | ~2.8M | ~42K | ~$0.15 |
| Exec summaries (batched) | Haiku | ~14M | ~1.4M | ~$1.75 |
| Cover images (Replicate) | flux-schnell | n/a | n/a | ~$0.35 |
| **Total** | | | | **~$2.25** |

With batching at 50% discount: **~$1.30 total.**


## Part F: Execution Sequence

### Step 1: Hugo Config (Instant)

Add `buildFuture = true` to `hugo.toml`. All series pages immediately populate.

### Step 2: Create Content Pages (Under 5 Minutes)

Create `content/search.md`, `content/archives.md`, and `content/about.md` per Part A2.

### Step 3: Run `fix_hugo_bundles.py` (Single Script, All File Fixes)

A standalone Python script that runs locally against `content/rural-health/`. Does all of the following in one pass:

1. **Rename broken slug directories** (7-8 articles + their summaries)
2. **Copy cover.webp** from article dirs to summary dirs
3. **Patch summary front matter:** add `cover:` block, add `_build: list: never`
4. **Strip duplicate title lines** from summary content bodies
5. **Update internal URL references** (`summary_url`, `full_article_url`) for renamed slugs
6. **Convert cross-references to links** using manifest-based lookup

Run as: `python fix_hugo_bundles.py content/rural-health/`

### Step 4: Create CSS and Layout Files

| File | Purpose |
|---|---|
| `assets/css/extended/custom.css` | Title size, image sizing, tiled list, summary link styling, pagination |
| `layouts/partials/pagination.html` | Numbered page navigation |
| `layouts/partials/summary-link.html` | "Read the Executive Summary" link on article pages |
| `layouts/_default/single.html` | PaperMod override injecting summary-link partial |
| `layouts/_default/list.html` | Tiled two-column list with thumbnails, inline summary links, numbered pagination |

### Step 5: Test Locally

```bash
hugo server
```

Verify:
- All series pages show their articles (not just Series 1-3)
- Search, Archives, and About pages load correctly
- Titles and H1s render at reduced size
- Cover images render at constrained width on article pages
- List pages show tiled two-column layout with small thumbnails
- Executive summary link appears on article pages and in list entries
- Summaries have cover images
- Summary title not doubled
- Summaries hidden from list pages
- Cross-references are clickable links
- Broken slug URLs resolve correctly
- Numbered pagination shows page numbers with first/prev/next/last

### Step 6: Deploy

```bash
git add -A && git commit -m "RHTP: all bugs fixed, tiled lists, cross-ref links, pagination, content pages" && git push
```

### Step 7: Verify at syamadusumilli.com

Cloudflare Pages auto-builds. Check live site matches local testing.


## Part G: Continuation Context for Work Requirements

After all fixes are verified, update `RHTP_Continuation_Context.md` with:

1. **Resolved bugs list** (all bugs resolved, with method used)
2. **Completed Hugo customizations** (CSS, layouts, pagination, content pages)
3. **Cross-reference linking approach** (reusable for WR articles)
4. **Cost optimization patterns** (batching, caching, model selection)
5. **File tree update** showing all new layout/CSS/content files
6. **WR-specific adaptation notes:**
   - Different `SERIES_TITLES` dict
   - Different filename regex patterns
   - No state sub-grouping (unless WR has state-specific articles)
   - Same image style prefix, different content descriptions
   - Same sidebar partial, second collection section
   - Same cross-reference linking approach with WR manifest

### Files to Package for WR Project

| File | Purpose | WR Adaptation Needed |
|---|---|---|
| `process_articles.py` | Processing pipeline | Clone as `process_wr_articles.py`, change SERIES_TITLES, filename patterns, exclude patterns |
| `fix_hugo_bundles.py` | Post-processing fixes | Reusable with path parameter change |
| `hugo.toml` | Site config | Already includes `work-requirements` in mainsections and menu |
| `layouts/` directory | All layout overrides | Shared across collections |
| `assets/css/extended/` | All CSS | Shared across collections |
| `RHTP_Continuation_Context.md` | Full project state | Update with WR-specific sections |

The WR pipeline uses the same three-pass workflow (prompts, images, bundles) with cost-optimized batch mode enabled from the start.


## Summary of All Fixes

| # | Issue | Fix Method | Effort |
|---|---|---|---|
| A1 | Series 4+ pages invisible | `buildFuture = true` in hugo.toml | 10 seconds |
| A2 | Missing Search/Archives/About | Create 3 content markdown files | 5 minutes |
| B1 | Summary pages missing covers | Copy cover.webp + patch front matter | Script |
| B2 | Summary title doubled | Strip duplicate H1 from content body | Script |
| B3 | Broken slugs (7-8 articles) | Rename directories + patch URLs | Script |
| B4 | Summaries in article listings | Add `_build: list: never` to front matter | Script |
| B5 | Cross-references as plain text | Manifest-based link conversion | Script |
| C1 | Titles/H1s too large | CSS font-size reduction | CSS |
| C2 | Cover images too wide | CSS max-width constraint | CSS |
| C3 | List view unstacked | Two-column tiled grid layout | CSS |
| C4 | No summary link styling | Inline link CSS | CSS |
| C5 | No page numbers | Numbered pagination CSS | CSS |
| D1 | Prev/next only pagination | Custom pagination partial | Layout |
| D2 | No summary link on articles | Summary-link partial | Layout |
| D3 | Single page needs partial | PaperMod single override | Layout |
| D4 | List needs tiles + pagination | PaperMod list override | Layout |
| E1 | ID-label title extraction bug | extract_content() patch | Future runs |
| E2 | Slug generation failures | generate_slug() patch | Future runs |
| E3 | Per-article API cost | Batching + caching + Haiku | WR pipeline |

**API calls required:** Zero for all existing content fixes.
**Estimated cost for fixes:** $0.
**Estimated cost for WR pipeline (140 articles):** ~$1.30 with batching.
