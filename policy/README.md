# Hugo Fixes: Deployment Instructions

## File Map

Drop these files into your Hugo site root. All paths are relative to the site root.

```
hugo.toml                                  <- REPLACE existing
content/search.md                          <- NEW
content/archives.md                        <- NEW
content/about.md                           <- NEW
assets/css/extended/custom.css             <- NEW (PaperMod auto-loads)
layouts/partials/pagination.html           <- NEW
layouts/partials/summary-link.html         <- NEW
layouts/_default/list.html                 <- NEW (overrides PaperMod)
layouts/_default/single.html               <- CREATE via script below
fix_hugo_bundles.py                        <- Run once, then remove
```


## Execution Sequence

### 1. Copy Static Files (2 minutes)

Copy `hugo.toml`, all `content/` files, all `assets/` files, and all `layouts/` files into your Hugo site root, preserving directory structure.

### 2. Create the Single Page Override

```bash
chmod +x create_single_override.sh
./create_single_override.sh
```

This copies PaperMod's `single.html` and injects the summary-link partial. If the sed insertion misses, manually add this line inside the `<div class="post-content">` block, before `{{.Content}}`:

```html
{{- partial "summary-link.html" . -}}
```

### 3. Run the Fix Script

**Dry run first** to see what would change:

```bash
python fix_hugo_bundles.py content/rural-health/ --dry-run
```

**Then run live:**

```bash
python fix_hugo_bundles.py content/rural-health/
```

The script auto-detects `full_manifest.json` in common locations. If it can't find it, pass explicitly:

```bash
python fix_hugo_bundles.py content/rural-health/ --manifest path/to/full_manifest.json
```

### 4. Test Locally

```bash
hugo server
```

**Verify each fix:**

| Check | What to Look For |
|---|---|
| Series 4+ pages | Navigate to /rural-health/series-4/ and confirm articles appear |
| Search page | Click Search in nav, type a query, confirm results |
| Archives page | Click Archives in nav, confirm year/month groupings |
| About page | Click About in nav, confirm bio renders |
| Title sizes | Open any article, confirm smaller H1/H2 |
| Cover image width | Article pages show constrained cover (not full-width) |
| Tiled list view | Series list pages show two-column grid with thumbnails |
| Summary links | Article pages show "Read the Executive Summary" link |
| Summary link in lists | List entries show small "Executive Summary" link |
| Summary covers | Navigate to any -summary/ URL, confirm cover image |
| Summary title not doubled | Summary pages show title once |
| Summaries hidden from lists | Summary pages do not appear in series listings |
| Cross-reference links | Open any article, scroll to Cross-References, confirm links |
| Broken slugs fixed | Navigate to /rural-health/series-5/lead-agency-structures/ |
| Numbered pagination | Any list with 20+ items shows page numbers |

### 5. Deploy

```bash
git add -A
git commit -m "RHTP: all bugs fixed, tiled lists, cross-ref links, pagination, content pages"
git push
```

### 6. Verify Live

Cloudflare Pages auto-builds. Check syamadusumilli.com matches local testing.


## What Changed in hugo.toml

One line added at top level:

```toml
buildFuture = true
```

Everything else is unchanged.
