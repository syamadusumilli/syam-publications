#!/usr/bin/env python3
"""
fix_hugo_bundles.py

Post-processing script for RHTP Hugo site. Fixes existing page bundles
in-place without any API calls or regeneration.

Fixes applied:
  1. Rename broken slug directories
  2. Copy cover images from articles to their summaries
  3. Patch summary front matter (cover block, _build: list: never)
  4. Strip duplicate title lines from summary content bodies
  5. Update internal URL references for renamed slugs
  6. Convert cross-references to clickable links

Usage:
  python fix_hugo_bundles.py content/rural-health/
  python fix_hugo_bundles.py content/rural-health/ --dry-run
  python fix_hugo_bundles.py content/rural-health/ --manifest full_manifest.json
"""

import os
import re
import sys
import json
import shutil
import argparse
from pathlib import Path


# ============================================================
# SLUG RENAME MAP
# ============================================================
# Maps current directory names to corrected directory names.
# Applies to both article dirs and their -summary/ siblings.

SLUG_RENAMES = {
    # Series 5: ID-label slugs that should use subtitle-derived names
    "rhtp-5a": "lead-agency-structures",
    "rhtp-5b": "stakeholder-coordination",
    "5c": "procurement-and-contracting",
    "5d": "performance-measurement",
    "rhtp-5e": "federal-state-relationship",
    "rhtp-5synthesis": "state-agency-structures-synthesis",
    "rhtp-5tda": "state-agency-decision-authority-matrix",
    "rhtp-5companion": "seeing-differently",
    # Series 9: truncated slug
    "rhtp-9p": "autism-idd-service-desert",
    # Series 3 TD-E: duplicate slugs need disambiguation
    # These are handled separately because two share the same slug
}

# 3-TD-E articles have duplicate slugs. We disambiguate by checking
# the content/title inside the index.md to determine which is which.
TDTE_RENAMES = {
    "technical-document-3-td-e-regional": "sdoh-hrsn-chw-cie-regional-deep-dives",
    # For the two that share "technical-document-3-td-e", we check content:
    "technical-document-3-td-e": {
        "State Analysis": "sdoh-hrsn-chw-cie-state-analysis",
        "State Inventory": "sdoh-hrsn-chw-cie-state-inventory",
        "default": "sdoh-hrsn-chw-cie-state-analysis",
    },
}


def read_front_matter(index_path):
    """Read and return (front_matter_text, content_body) from an index.md."""
    text = index_path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) >= 3:
        return parts[1], parts[2]
    return "", text


def write_index(index_path, front_matter, content_body):
    """Write front matter and content back to index.md."""
    index_path.write_text(f"---{front_matter}---{content_body}", encoding="utf-8")


def get_front_matter_value(fm_text, key):
    """Extract a value from YAML-like front matter text."""
    pattern = rf'^\s*{re.escape(key)}\s*:\s*["\']?(.+?)["\']?\s*$'
    m = re.search(pattern, fm_text, re.MULTILINE)
    return m.group(1).strip() if m else None


def set_front_matter_value(fm_text, key, value):
    """Set or update a value in front matter text."""
    pattern = rf'^(\s*{re.escape(key)}\s*:\s*).*$'
    replacement = rf'\g<1>"{value}"'
    new_fm, count = re.subn(pattern, replacement, fm_text, count=1, flags=re.MULTILINE)
    if count == 0:
        new_fm = fm_text.rstrip() + f'\n{key}: "{value}"\n'
    return new_fm


# ============================================================
# FIX 1: RENAME BROKEN SLUG DIRECTORIES
# ============================================================

def fix_broken_slugs(content_dir, dry_run=False):
    """Rename directories with broken slugs."""
    renames_done = {}

    for series_dir in sorted(content_dir.iterdir()):
        if not series_dir.is_dir() or not series_dir.name.startswith("series-"):
            continue

        for article_dir in sorted(series_dir.iterdir()):
            if not article_dir.is_dir():
                continue

            dirname = article_dir.name
            base_name = dirname.replace("-summary", "")
            is_summary = dirname.endswith("-summary")

            new_base = None

            # Check standard rename map
            if base_name in SLUG_RENAMES:
                new_base = SLUG_RENAMES[base_name]

            # Check 3-TD-E special handling
            elif base_name in TDTE_RENAMES:
                rename_val = TDTE_RENAMES[base_name]
                if isinstance(rename_val, str):
                    new_base = rename_val
                elif isinstance(rename_val, dict):
                    # Read index.md to disambiguate
                    idx = article_dir / "index.md"
                    if idx.exists():
                        fm, _ = read_front_matter(idx)
                        title = get_front_matter_value(fm, "title") or ""
                        subtitle = get_front_matter_value(fm, "subtitle") or ""
                        combined = f"{title} {subtitle}".lower()
                        if "inventory" in combined:
                            new_base = rename_val["State Inventory"]
                        elif "analysis" in combined:
                            new_base = rename_val["State Analysis"]
                        else:
                            new_base = rename_val["default"]
                    else:
                        new_base = rename_val["default"]

            if new_base:
                new_name = f"{new_base}-summary" if is_summary else new_base
                new_path = series_dir / new_name

                if article_dir != new_path:
                    print(f"  RENAME: {article_dir.name} -> {new_name}")
                    if not dry_run:
                        if new_path.exists():
                            print(f"    WARNING: Target {new_path} already exists, skipping")
                            continue
                        article_dir.rename(new_path)
                    renames_done[dirname] = new_name

    return renames_done


# ============================================================
# FIX 2: COPY COVER IMAGES TO SUMMARY DIRECTORIES
# ============================================================

def fix_summary_covers(content_dir, dry_run=False):
    """Copy cover.webp from article dirs to their summary dirs."""
    count = 0
    for series_dir in sorted(content_dir.iterdir()):
        if not series_dir.is_dir() or not series_dir.name.startswith("series-"):
            continue

        for summary_dir in sorted(series_dir.iterdir()):
            if not summary_dir.is_dir() or not summary_dir.name.endswith("-summary"):
                continue

            # Already has a cover image
            if (summary_dir / "cover.webp").exists():
                continue

            # Find sibling article directory
            article_slug = summary_dir.name.replace("-summary", "")
            article_dir = series_dir / article_slug

            if not article_dir.is_dir():
                # Try finding any dir that matches (in case of renames)
                continue

            source_cover = article_dir / "cover.webp"
            if source_cover.exists():
                print(f"  COVER: {summary_dir.name} <- {article_dir.name}/cover.webp")
                if not dry_run:
                    shutil.copy2(source_cover, summary_dir / "cover.webp")
                count += 1

    return count


# ============================================================
# FIX 3: PATCH SUMMARY FRONT MATTER
# ============================================================

def fix_summary_front_matter(content_dir, dry_run=False):
    """Add cover block and _build: list: never to summary front matter."""
    count = 0
    for series_dir in sorted(content_dir.iterdir()):
        if not series_dir.is_dir() or not series_dir.name.startswith("series-"):
            continue

        for summary_dir in sorted(series_dir.iterdir()):
            if not summary_dir.is_dir() or not summary_dir.name.endswith("-summary"):
                continue

            index_path = summary_dir / "index.md"
            if not index_path.exists():
                continue

            fm, body = read_front_matter(index_path)
            modified = False

            # Add cover block if missing and cover.webp exists
            if "cover:" not in fm and (summary_dir / "cover.webp").exists():
                cover_block = """
cover:
  image: "cover.webp"
  alt: "Cover image"
  relative: true"""
                fm = fm.rstrip() + cover_block + "\n"
                modified = True

            # Add _build: list: never if missing
            if "_build:" not in fm:
                build_block = """
_build:
  list: never"""
                fm = fm.rstrip() + build_block + "\n"
                modified = True

            if modified:
                print(f"  PATCH FM: {summary_dir.name}/index.md")
                if not dry_run:
                    write_index(index_path, fm, body)
                count += 1

    return count


# ============================================================
# FIX 4: STRIP DUPLICATE TITLE LINES FROM SUMMARIES
# ============================================================

def fix_summary_duplicate_titles(content_dir, dry_run=False):
    """Remove leading H1 or bold title lines from summary content bodies."""
    count = 0
    for series_dir in sorted(content_dir.iterdir()):
        if not series_dir.is_dir() or not series_dir.name.startswith("series-"):
            continue

        for summary_dir in sorted(series_dir.iterdir()):
            if not summary_dir.is_dir() or not summary_dir.name.endswith("-summary"):
                continue

            index_path = summary_dir / "index.md"
            if not index_path.exists():
                continue

            fm, body = read_front_matter(index_path)
            title = get_front_matter_value(fm, "title") or ""

            # Find first non-empty line in body
            lines = body.split("\n")
            first_content_idx = None
            for i, line in enumerate(lines):
                if line.strip():
                    first_content_idx = i
                    break

            if first_content_idx is None:
                continue

            first_line = lines[first_content_idx].strip()
            should_remove = False

            # Check if it's a duplicate H1
            if first_line.startswith("# "):
                h1_text = first_line[2:].strip()
                if h1_text.lower() == title.lower() or "executive summary" in h1_text.lower():
                    should_remove = True

            # Check if it's a bold title duplicate
            elif first_line.startswith("**") and first_line.endswith("**"):
                bold_text = first_line.strip("*").strip()
                if bold_text.lower() == title.lower() or "executive summary" in bold_text.lower():
                    should_remove = True

            if should_remove:
                print(f"  DEDUP TITLE: {summary_dir.name} (removed: {first_line[:60]})")
                if not dry_run:
                    lines.pop(first_content_idx)
                    body = "\n".join(lines)
                    write_index(index_path, fm, body)
                count += 1

    return count


# ============================================================
# FIX 5: UPDATE INTERNAL URL REFERENCES FOR RENAMED SLUGS
# ============================================================

def fix_internal_urls(content_dir, renames_done, dry_run=False):
    """Update summary_url and full_article_url params after slug renames."""
    if not renames_done:
        return 0

    count = 0
    for series_dir in sorted(content_dir.iterdir()):
        if not series_dir.is_dir() or not series_dir.name.startswith("series-"):
            continue

        for article_dir in sorted(series_dir.iterdir()):
            if not article_dir.is_dir():
                continue

            index_path = article_dir / "index.md"
            if not index_path.exists():
                continue

            fm, body = read_front_matter(index_path)
            modified = False

            # Check summary_url and full_article_url for old slugs
            for old_name, new_name in renames_done.items():
                if old_name in fm:
                    fm = fm.replace(old_name, new_name)
                    modified = True

            if modified:
                print(f"  URL FIX: {article_dir.name}/index.md")
                if not dry_run:
                    write_index(index_path, fm, body)
                count += 1

    return count


# ============================================================
# FIX 6: CONVERT CROSS-REFERENCES TO LINKS
# ============================================================

def build_xref_lookup(manifest_path, renames_done):
    """Build article_id -> Hugo URL lookup from manifest.json."""
    if not manifest_path or not manifest_path.exists():
        print(f"  WARNING: Manifest not found at {manifest_path}, skipping cross-ref linking")
        return {}

    with open(manifest_path) as f:
        manifest = json.load(f)

    lookup = {}
    for article in manifest["articles"]:
        aid = article["article_id"]
        slug = article["slug"]
        series_num = article["series_number"]

        # Apply renames if any
        for old_name, new_name in renames_done.items():
            base_old = old_name.replace("-summary", "")
            base_new = new_name.replace("-summary", "")
            if slug == base_old:
                slug = base_new

        url = f"/rural-health/series-{series_num}/{slug}/"

        # Handle duplicate IDs (3-TD-E) by keeping all variants
        if aid in lookup and lookup[aid] != url:
            # Store as list for disambiguation
            existing = lookup[aid]
            if isinstance(existing, str):
                lookup[aid] = [existing, url]
            else:
                existing.append(url)
        else:
            lookup[aid] = url

    return lookup


def normalize_article_id(ref_text):
    """Extract an article ID from a cross-reference text string.

    Handles patterns like:
      '2A (RHTP Structure and Rules)' -> '2A'
      'Article 2C: Medicare Rural Provisions' -> '2C'
      '3-VT (Vermont)' -> '3.VT'
      'RHTP 3.KY (Kentucky)' -> '3.KY'
      '8-TD-A: Community Org Capacity' -> '8-TD-A'
      'Synthesis: Which State Agency...' -> context-dependent
      'RHTP 9.H (Appalachian Communities)' -> '9H'
    """
    ref = ref_text.strip()

    # Pattern: "Article NA:" or "Article N.A:"
    m = re.match(r"Article\s+(\d+[A-Z])", ref, re.IGNORECASE)
    if m:
        return m.group(1)

    # Pattern: "RHTP N.X" or "RHTP N.XX"
    m = re.match(r"RHTP\s+(\d+)\.(\w+)", ref, re.IGNORECASE)
    if m:
        series = m.group(1)
        code = m.group(2)
        if code.upper() == "SYN" or code.upper() == "SYNTHESIS":
            return f"{series}.Syn"
        elif code.upper().startswith("COMP"):
            return f"{series}.Comp.S"
        elif code.upper().startswith("TD"):
            return f"{series}-TD-{code[-1].upper()}"
        else:
            return f"{series}{code.upper()}"

    # Pattern: "N-TD-X:" or "N-TD-X"
    m = re.match(r"(\d+-TD-[A-Z])", ref, re.IGNORECASE)
    if m:
        return m.group(1).upper()

    # Pattern: "NA (Title):" like "2A (RHTP Structure)" or "3-VT (Vermont)"
    m = re.match(r"(\d+[A-Z](?:\.\d+)?)\s*[\(:]", ref)
    if m:
        return m.group(1)

    # Pattern: "3-XX (State)" for state profiles
    m = re.match(r"3-([A-Z]{2})\s*[\(:]", ref)
    if m:
        return f"3.{m.group(1)}"

    # Pattern: state profile references like "3.XX"
    m = re.match(r"(\d+\.[A-Z]{2}(?:\.\d)?)", ref)
    if m:
        return m.group(1)

    # Pattern: bare article codes at start
    m = re.match(r"(\d+[A-Z])\b", ref)
    if m:
        return m.group(1)

    return None


def linkify_cross_references(content_dir, lookup, dry_run=False):
    """Convert plain-text cross-references to markdown links."""
    if not lookup:
        return 0

    count = 0
    for series_dir in sorted(content_dir.iterdir()):
        if not series_dir.is_dir() or not series_dir.name.startswith("series-"):
            continue

        for article_dir in sorted(series_dir.iterdir()):
            if not article_dir.is_dir() or article_dir.name.endswith("-summary"):
                continue

            index_path = article_dir / "index.md"
            if not index_path.exists():
                continue

            fm, body = read_front_matter(index_path)

            # Find the Cross-References section
            xref_match = re.search(r"^##\s*Cross[- ]?References", body, re.MULTILINE | re.IGNORECASE)
            if not xref_match:
                continue

            xref_start = xref_match.start()
            # Find the next heading or end of content
            next_heading = re.search(r"^##\s", body[xref_start + 1:], re.MULTILINE)
            if next_heading:
                xref_end = xref_start + 1 + next_heading.start()
            else:
                xref_end = len(body)

            xref_section = body[xref_start:xref_end]
            new_lines = []
            modified = False

            for line in xref_section.split("\n"):
                # Only process bullet lines
                if not line.strip().startswith("- "):
                    new_lines.append(line)
                    continue

                # Skip lines that already have links
                if "](/rural-health/" in line or "](/" in line:
                    new_lines.append(line)
                    continue

                # Extract the reference portion (after "- " and before ":")
                bullet_content = line.strip()[2:].strip()

                # Try to identify the article ID
                # Strip bold markers for ID extraction
                clean_ref = re.sub(r"\*\*", "", bullet_content)
                article_id = normalize_article_id(clean_ref)

                if article_id and article_id in lookup:
                    url = lookup[article_id]
                    # If multiple URLs (duplicate IDs), use the first one
                    if isinstance(url, list):
                        url = url[0]

                    # Find the reference label to wrap in a link
                    # Pattern: **Label:** Description or Label: Description
                    bold_match = re.match(r"^(- \s*)\*\*(.+?)\*\*(:?\s*)(.*)", line)
                    plain_match = re.match(r"^(- \s*)(.+?)(:)(\s.*)", line) if not bold_match else None

                    if bold_match:
                        prefix, label, sep, rest = bold_match.groups()
                        new_line = f"{prefix}[**{label}**]({url}){sep}{rest}"
                        new_lines.append(new_line)
                        modified = True
                    elif plain_match:
                        prefix, label, sep, rest = plain_match.groups()
                        new_line = f"{prefix}[{label}]({url}){sep}{rest}"
                        new_lines.append(new_line)
                        modified = True
                    else:
                        new_lines.append(line)
                else:
                    # Try series-level fallback for unresolved references
                    series_match = re.match(r"(\d+)", clean_ref)
                    if series_match and not article_id:
                        series_num = series_match.group(1)
                        # Don't link generic series references, keep as-is
                        pass
                    new_lines.append(line)

            if modified:
                new_xref_section = "\n".join(new_lines)
                body = body[:xref_start] + new_xref_section + body[xref_end:]
                print(f"  XREF LINK: {article_dir.name}/index.md")
                if not dry_run:
                    write_index(index_path, fm, body)
                count += 1

    return count


# ============================================================
# MAIN
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="Fix RHTP Hugo page bundles in-place")
    parser.add_argument("content_dir", help="Path to content/rural-health/ directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--manifest", default=None, help="Path to full_manifest.json for cross-reference linking")
    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    if not content_dir.is_dir():
        print(f"ERROR: {content_dir} is not a directory")
        sys.exit(1)

    manifest_path = Path(args.manifest) if args.manifest else None
    # Auto-detect manifest in common locations
    if not manifest_path:
        for candidate in [
            content_dir / "../../full_manifest.json",
            content_dir / "../full_manifest.json",
            Path("full_manifest.json"),
        ]:
            if candidate.exists():
                manifest_path = candidate.resolve()
                break

    mode = "DRY RUN" if args.dry_run else "LIVE"
    print(f"\n{'='*60}")
    print(f"RHTP Hugo Bundle Fix Script ({mode})")
    print(f"{'='*60}")
    print(f"Content dir: {content_dir}")
    print(f"Manifest: {manifest_path or 'not found'}")
    print()

    # Fix 1: Rename broken slug directories
    print("[1/6] Renaming broken slug directories...")
    renames_done = fix_broken_slugs(content_dir, args.dry_run)
    print(f"  Done: {len(renames_done)} directories renamed\n")

    # Fix 2: Copy cover images to summaries
    print("[2/6] Copying cover images to summary directories...")
    covers = fix_summary_covers(content_dir, args.dry_run)
    print(f"  Done: {covers} cover images copied\n")

    # Fix 3: Patch summary front matter
    print("[3/6] Patching summary front matter (cover block + _build)...")
    patched = fix_summary_front_matter(content_dir, args.dry_run)
    print(f"  Done: {patched} summaries patched\n")

    # Fix 4: Strip duplicate title lines
    print("[4/6] Stripping duplicate title lines from summaries...")
    deduped = fix_summary_duplicate_titles(content_dir, args.dry_run)
    print(f"  Done: {deduped} duplicate titles removed\n")

    # Fix 5: Update internal URLs for renamed slugs
    print("[5/6] Updating internal URL references...")
    urls_fixed = fix_internal_urls(content_dir, renames_done, args.dry_run)
    print(f"  Done: {urls_fixed} URL references updated\n")

    # Fix 6: Convert cross-references to links
    print("[6/6] Converting cross-references to links...")
    xref_lookup = build_xref_lookup(manifest_path, renames_done)
    xrefs = linkify_cross_references(content_dir, xref_lookup, args.dry_run)
    print(f"  Done: {xrefs} articles with cross-references linked\n")

    print(f"{'='*60}")
    print("COMPLETE")
    print(f"  Directories renamed: {len(renames_done)}")
    print(f"  Cover images copied: {covers}")
    print(f"  Summaries patched:   {patched}")
    print(f"  Duplicate titles:    {deduped}")
    print(f"  URL refs updated:    {urls_fixed}")
    print(f"  Cross-refs linked:   {xrefs}")
    if args.dry_run:
        print("\n  (Dry run: no changes were made)")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
