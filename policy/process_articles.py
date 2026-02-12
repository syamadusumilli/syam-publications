#!/usr/bin/env python3
"""
RHTP Hugo Processing Pipeline
Reads RHTP markdown articles and generates Hugo page bundles with:
  - PaperMod front matter
  - AI cover images (Claude prompts -> Replicate flux-schnell)
  - Executive summaries (Claude API)
  - Section index files and date staggering

Forked from:
  - parse_article_metadata.py (RHTP filename parsing, metadata extraction)
  - pipeline.py (BGM image generation pipeline)

Usage:
  Full pipeline:          python process_articles.py ./rural-health/
  Dry run (no API calls):  python process_articles.py ./rural-health/ --dry-run
  Prompts only:           python process_articles.py ./rural-health/ --prompts-only
  From reviewed prompts:  python process_articles.py --from-prompts prompts/
  Summaries only:         python process_articles.py ./rural-health/ --summaries-only
  Images only:            python process_articles.py ./rural-health/ --images-only
  Skip images:            python process_articles.py ./rural-health/ --no-images
  Skip summaries:         python process_articles.py ./rural-health/ --no-summaries
"""

import os
import sys
import json
import re
import time
import argparse
from pathlib import Path
from datetime import datetime, timedelta


# ============================================================
# .ENV LOADING
# ============================================================

def load_env():
    """Load .env from script directory or pipeline/ directory."""
    candidates = [
        Path(__file__).parent / ".env",
        Path(__file__).parent / "pipeline" / ".env",
    ]
    for env_path in candidates:
        if env_path.exists():
            with open(env_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, value = line.split("=", 1)
                        os.environ.setdefault(key.strip(), value.strip())
            print(f"  Loaded env from {env_path}")
            return
    print("  WARNING: No .env file found")

load_env()


# ============================================================
# CONFIGURATION
# ============================================================

# --- Series titles (for Hugo front matter) ---
SERIES_TITLES = {
    1: "Understanding Rural and Deep Rural America",
    2: "The Federal Architecture of Rural Health",
    3: "State-by-State Analysis",
    4: "Evidence-Based Strategies",
    5: "State Agency Structures",
    6: "Intermediary Organizations",
    7: "Rural Provider Landscape",
    8: "Community Infrastructure",
    9: "Special Populations",
    10: "Regional Profiles",
    11: "Clinical Reality",
    12: "Coverage and Financing",
    13: "Trust and Navigation",
    14: "Infrastructure Models",
    15: "Regulatory and Workforce",
    16: "Integration and Scenarios",
}

# --- Series short names (for Notion-style mapping, tags) ---
SERIES_SHORT = {
    1: "The Terrain",
    2: "Policy Framework",
    3: "State Implementation",
    4: "Transformation Approaches",
    5: "State Agencies",
    6: "Intermediaries",
    7: "Providers",
    8: "Community Organizations",
    9: "Special Populations",
    10: "Regional Deep Dives",
    11: "Clinical Reality",
    12: "Policy Earthquake",
    13: "Human Experience",
    14: "Innovation Landscape",
    15: "Paradigm Shifts",
    16: "Synthesis and Scenarios",
}

# --- Category groupings ---
CATEGORY_MAP = {
    1: "Foundations", 2: "Policy & Process", 3: "Foundations", 4: "Foundations",
    5: "Stakeholders", 6: "Stakeholders", 7: "Stakeholders", 8: "Stakeholders",
    9: "Populations", 10: "Populations",
    11: "The Bridge", 12: "The Bridge", 13: "The Bridge",
    14: "The Future", 15: "The Future", 16: "The Future",
}

# --- Default tags by series ---
SERIES_TAGS = {
    1: ["rural-health"],
    2: ["rural-health", "rhtp"],
    3: ["rural-health", "rhtp", "state-policy"],
    4: ["rural-health", "rhtp"],
    5: ["rural-health", "rhtp", "state-policy"],
    6: ["rural-health", "rhtp"],
    7: ["rural-health", "rhtp"],
    8: ["rural-health", "rhtp", "social-care"],
    9: ["rural-health", "rhtp", "health-equity"],
    10: ["rural-health", "rhtp"],
    11: ["rural-health", "rhtp"],
    12: ["rural-health", "rhtp", "medicaid"],
    13: ["rural-health", "rhtp", "health-equity"],
    14: ["rural-health", "rhtp"],
    15: ["rural-health", "rhtp", "state-policy"],
    16: ["rural-health", "rhtp"],
}

# --- State abbreviation to full name ---
STATE_NAMES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho",
    "IL": "Illinois", "IN": "Indiana", "IA": "Iowa", "KS": "Kansas",
    "KY": "Kentucky", "LA": "Louisiana", "ME": "Maine", "MD": "Maryland",
    "MA": "Massachusetts", "MI": "Michigan", "MN": "Minnesota", "MS": "Mississippi",
    "MO": "Missouri", "MT": "Montana", "NE": "Nebraska", "NV": "Nevada",
    "NH": "New Hampshire", "NJ": "New Jersey", "NM": "New Mexico", "NY": "New York",
    "NC": "North Carolina", "ND": "North Dakota", "OH": "Ohio", "OK": "Oklahoma",
    "OR": "Oregon", "PA": "Pennsylvania", "RI": "Rhode Island", "SC": "South Carolina",
    "SD": "South Dakota", "TN": "Tennessee", "TX": "Texas", "UT": "Utah",
    "VT": "Vermont", "VA": "Virginia", "WA": "Washington", "WV": "West Virginia",
    "WI": "Wisconsin", "WY": "Wyoming",
}

# --- State to region ---
STATE_REGIONS = {
    "CT": "Northeast", "DE": "Northeast", "MA": "Northeast", "MD": "Northeast",
    "ME": "Northeast", "NH": "Northeast", "NJ": "Northeast", "NY": "Northeast",
    "PA": "Northeast", "RI": "Northeast", "VT": "Northeast", "VA": "Northeast",
    "AL": "Southeast", "AR": "Southeast", "FL": "Southeast", "GA": "Southeast",
    "KY": "Southeast", "LA": "Southeast", "MS": "Southeast", "NC": "Southeast",
    "SC": "Southeast", "TN": "Southeast", "WV": "Southeast",
    "IA": "Midwest", "IL": "Midwest", "IN": "Midwest", "KS": "Midwest",
    "MI": "Midwest", "MN": "Midwest", "MO": "Midwest", "ND": "Midwest",
    "NE": "Midwest", "OH": "Midwest", "SD": "Midwest", "WI": "Midwest",
    "AZ": "Southwest", "NM": "Southwest", "OK": "Southwest", "TX": "Southwest",
    "AK": "West", "CA": "West", "CO": "West", "HI": "West", "ID": "West",
    "MT": "West", "NV": "West", "OR": "West", "UT": "West", "WA": "West",
    "WY": "West",
}

LETTER_ORDER = {chr(i): i - 64 for i in range(65, 91)}

# --- Files to exclude ---
EXCLUDE_PATTERNS = [
    r"Series_\d+_", r"Series\d+_", r"_Outline_", r"_Strategy_",
    r"LinkedIn", r"^GGH_", r"^RHT_L", r"^RHT_Priority", r"^RHT_LinkedIn",
    r"Data_Tables", r"Disruptive_Frameworks", r"Known_Context",
    r"^free_app", r"^target_states", r"^secondary_target", r"^rural_health_gaps",
    r"National-Market", r"Intel_Brief", r"One_Pager", r"CIE_Market",
    r"_Enhanced\.", r"Stack_Ranking", r"RHTP_Analysis", r"GTM_", r"Rural_GTM",
    r"RHTP_Article_Series", r"^SKILL", r"^full_manifest", r"^parse_article",
    r"Continuation_Context", r"README",
]

SUPERSEDED_FILES = {
    "Article_2C_Medicare_Rural_Provisions.md",
    "RHTP_3ME_Maine_V3.md",
    "RHTP_4_Companion_Beyond_Optimization_Outline_V1.md",
    "RHTP_8_Companion_Building_What_Doesnt_Exist_Outline_V1.md",
    "RHTP_3_TD_E_Research_Strategy_Gap_Analysis.md",
}

# --- Image generation settings ---
IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
MODEL_IMAGE_PROMPT = "claude-haiku-4-5-20251001"
MODEL_SUMMARY = "claude-sonnet-4-5-20250929"

IMAGE_PROMPT_STYLE = """You are generating an image prompt for Flux-Schnell, an AI image model.
The image will accompany a policy article about rural health transformation in America
for a publication analyzing the $50 billion Rural Health Transformation Program.

Visual style guidelines:
- Documentary photography feel, not stock photography
- Warm, muted earth tones. Morning or golden hour light preferred.
- Rural American settings: county roads, farmland, small-town main streets,
  community centers, rural clinics, porches, kitchen tables, church halls.
- Never show faces clearly (privacy, universality). Use hands, silhouettes,
  over-shoulder shots, overhead views, wide landscape angles.
- No sterile clinical settings unless the article specifically requires it.
- No cliched "concerned doctor with clipboard" or "sad rural person" compositions.
- No overly bright, cheerful, or generic aesthetics.
- Convey quiet weight, dignity, resilience, and the texture of rural daily life.
- Think photojournalism and documentary, not advertising or stock photography.

Read the article excerpt below and generate a single image prompt for Flux-Schnell.
The prompt should be 2-4 sentences of specific, descriptive language covering:
composition, lighting, key objects, mood, and photographic style.
Do not include any explanation, just the prompt itself."""

SUMMARY_STYLE = """You are writing an executive summary of a policy analysis article
about the Rural Health Transformation Program (RHTP), a $50 billion federal initiative
to transform rural healthcare while $911 billion in simultaneous Medicaid cuts proceed.

Write 800-1000 words. Preserve the article's argument structure and analytical rigor.

Rules:
- No bullet points. Flowing analytical prose only.
- No em dashes. Use commas, semicolons, colons, parentheses.
- No "it's important to note," "groundbreaking," "game-changing," "delve into,"
  "shed light on," "pave the way," "paradigm shift," "leverage," "synergy,"
  "robust," "utilize," or any AI slop phrases.
- Bold key phrases that carry analytical weight (3-5 per section).
- Preserve specific data points, dollar figures, and percentages from the original.
- Maintain the article's analytical voice: pragmatic realism, not advocacy.
- End with the core tension or open question the full article explores.
- Do not add headers or section breaks. One continuous analytical piece."""

# --- Date staggering ---
START_DATE = datetime(2026, 1, 1)


# ============================================================
# FILENAME PARSING (from parse_article_metadata.py)
# ============================================================

def should_exclude(filename):
    """Check if file should be excluded from processing."""
    if filename in SUPERSEDED_FILES:
        return True
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, filename):
            return True
    return False


def extract_series_number(filename):
    """Extract series number from filename."""
    # Technical documents: 1-TD-A, 2-TD-A, etc.
    m = re.match(r"^(\d+)-TD-", filename)
    if m:
        return int(m.group(1))

    # Series 1-2: Article_1A_, Article_2B_, Article_1_Synthesis
    m = re.match(r"^Article_(\d+)[A-Z_]", filename)
    if m:
        return int(m.group(1))

    # Series 3+: RHTP_3AL_, RHTP_10A_, RHTP_4_Synthesis, RHTP_3_TD_
    m = re.match(r"^RHTP_(\d+)", filename)
    if m:
        return int(m.group(1))

    return None


def extract_article_id(filename):
    """Generate article ID from filename (e.g., RHTP-4A, RHTP-3AL-1)."""
    # TD: 1-TD-A, 2-TD-B
    m = re.match(r"^(\d+)-TD-([A-Z])", filename)
    if m:
        return f"RHTP-{m.group(1)}-TD-{m.group(2)}"

    # Series 1-2 articles: Article_1A -> RHTP-1A
    m = re.match(r"^Article_(\d+)([A-Z])_", filename)
    if m:
        return f"RHTP-{m.group(1)}{m.group(2)}"

    # Series 1-2 synthesis: Article_1_Synthesis -> RHTP-1-Syn
    m = re.match(r"^Article_(\d+)_Synthesis", filename)
    if m:
        return f"RHTP-{m.group(1)}-Syn"

    # Series 3 state multi-part: RHTP_3AL_1 -> RHTP-3AL-1
    m = re.match(r"^RHTP_3([A-Z]{2})_(\d+)_", filename)
    if m:
        return f"RHTP-3{m.group(1)}-{m.group(2)}"

    # Series 3 state single: RHTP_3CO -> RHTP-3CO
    m = re.match(r"^RHTP_3([A-Z]{2})_", filename)
    if m:
        return f"RHTP-3{m.group(1)}"

    # Series 3+ TD: RHTP_3_TD_A -> RHTP-3-TD-A
    # For multi-document TDs (e.g., multiple 3-TD-E files), append disambiguator
    m = re.match(r"^RHTP_(\d+)_TD_([A-Z])_(.+?)(?:_V\d+)?(?:_Updated)?\.md$", filename)
    if m:
        series, letter, remainder = m.group(1), m.group(2), m.group(3)
        base_id = f"RHTP-{series}-TD-{letter}"
        # Known multi-document TDs that need disambiguation
        multi_doc_tds = {("3", "E")}
        if (series, letter) in multi_doc_tds:
            suffix_parts = remainder.split("_")[:2]
            suffix = "-".join(p.lower() for p in suffix_parts)
            return f"{base_id}-{suffix}"
        return base_id
    # Fallback for TDs without version suffix or compressed
    m = re.match(r"^RHTP_(\d+)_TD_([A-Z])_", filename)
    if m:
        return f"RHTP-{m.group(1)}-TD-{m.group(2)}"

    # Series 4+ articles: RHTP_4A -> RHTP-4A
    m = re.match(r"^RHTP_(\d+)([A-Z])_", filename)
    if m:
        return f"RHTP-{m.group(1)}{m.group(2)}"

    # Synthesis: RHTP_4_Synthesis -> RHTP-4-Syn
    m = re.match(r"^RHTP_(\d+)_Synthesis", filename)
    if m:
        return f"RHTP-{m.group(1)}-Syn"

    # Companion: RHTP_4_Companion_A -> RHTP-4-Comp-A
    m = re.match(r"^RHTP_(\d+)_Companion_([A-Z])", filename)
    if m:
        return f"RHTP-{m.group(1)}-Comp-{m.group(2)}"

    # Companion without letter: RHTP_5_Companion -> RHTP-5-Comp
    m = re.match(r"^RHTP_(\d+)_Companion_", filename)
    if m:
        return f"RHTP-{m.group(1)}-Comp"

    return filename.replace(".md", "")


def extract_article_type(filename, article_id):
    """Determine article type from filename."""
    if "-TD-" in article_id or "_TD_" in filename:
        return "technical_document"
    if "Synthesis" in filename or "-Syn" in article_id:
        return "synthesis"
    if "Companion" in filename or "-Comp" in article_id:
        return "companion"
    if re.match(r"^RHTP_3[A-Z]{2}_", filename):
        return "state_profile"
    return "article"


def extract_state_info(filename):
    """Extract state code, name, part number, and part title for Series 3."""
    # Multi-part: RHTP_3AL_1_Alabama_The_Problem_V3.md
    m = re.match(r"^RHTP_3([A-Z]{2})_(\d+)_(.+?)_V\d+", filename)
    if m:
        code = m.group(1)
        part = int(m.group(2))
        # Extract part title from the remaining filename
        remainder = m.group(3)
        # Remove state name prefix (e.g., "Alabama_The_Problem" -> "The Problem")
        state_name = STATE_NAMES.get(code, "")
        if state_name:
            remainder = remainder.replace(state_name.replace(" ", "_") + "_", "")
        part_title = remainder.replace("_", " ")
        return code, STATE_NAMES.get(code, code), part, part_title

    # Single: RHTP_3CO_Colorado_V3.md or RHTP_3NH_New_Hampshire_V3_Updated.md
    m = re.match(r"^RHTP_3([A-Z]{2})_(.+?)_V\d+", filename)
    if m:
        code = m.group(1)
        return code, STATE_NAMES.get(code, code), None, None

    # Compressed: RHTP_3XX_Name_Compressed.md (no _V suffix)
    m = re.match(r"^RHTP_3([A-Z]{2})_(.+?)_Compressed", filename)
    if m:
        code = m.group(1)
        return code, STATE_NAMES.get(code, code), None, None

    return None, None, None, None


def extract_series_order(filename, series_num):
    """Calculate sort order within a series."""
    base = series_num * 100

    # TD documents: 90+ offset
    m = re.search(r"_TD_([A-Z])", filename)
    if not m:
        m = re.match(r"^\d+-TD-([A-Z])", filename)
    if m:
        return base + 90 + LETTER_ORDER.get(m.group(1), 0)

    # Synthesis: 80
    if "Synthesis" in filename:
        return base + 80

    # Companion: 85+
    m = re.search(r"Companion_([A-Z])", filename)
    if m:
        return base + 85 + LETTER_ORDER.get(m.group(1), 0)
    if "Companion" in filename:
        return base + 85

    # Series 3 state articles: sort by state code + part
    if series_num == 3:
        m = re.match(r"RHTP_3([A-Z]{2})_(\d+)_", filename)
        if m:
            state = m.group(1)
            part = int(m.group(2))
            # Alphabetical by state code, then by part
            state_offset = (ord(state[0]) - 65) * 26 + (ord(state[1]) - 65)
            return base + state_offset * 4 + part
        m = re.match(r"RHTP_3([A-Z]{2})_", filename)
        if m:
            state = m.group(1)
            state_offset = (ord(state[0]) - 65) * 26 + (ord(state[1]) - 65)
            return base + state_offset * 4 + 1

    # Standard articles: letter offset
    m = re.match(r"(?:Article_\d+|RHTP_\d+)([A-Z])_", filename)
    if m:
        return base + LETTER_ORDER.get(m.group(1), 0)

    return base


# ============================================================
# CONTENT EXTRACTION
# ============================================================

def _is_id_only(text):
    """Check if text is just an article ID label with no descriptive content.
    Matches: 'RHTP 5.A', 'RHTP 3.NC.1: North Carolina', 'Technical Document 3-TD-E'
    Does NOT match: 'RHTP 5.E: Federal-State Relationship...' (has descriptive text after state/ID)
    """
    # Pure ID labels: "RHTP 5.A", "RHTP 16.B"
    if re.match(r"^(?:Article|RHTP|Technical Document)\s+[\d.A-Z-]+$", text):
        return True
    # ID with just a state name: "RHTP 3.NC.1: North Carolina" (no part title embedded)
    if re.match(r"^RHTP\s+3\.[A-Z]{2}\.\d+:\s+[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?$", text):
        return True
    return False


def extract_content(filepath):
    """Extract title, subtitle, series line, excerpt, and full text.
    Handles multiple header patterns found in RHTP articles:
      Pattern A (two H1):  # RHTP 16.B  /  # The Transformation Scenario
      Pattern B (H1+H2):   # RHTP 5.A   /  ## Lead Agency Structures...
      Pattern C (headerless): RHTP 5.C  /  Procurement and Contracting...
      Pattern D (state+H2):  # RHTP 3.NC.1: North Carolina  /  ## The Problem
    """
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    h1_lines = []
    subtitle = ""
    series_line = ""
    body_lines = []
    past_header = False

    # --- Detect headerless files (no # markers in first 5 content lines) ---
    first_content_lines = [l.strip() for l in lines if l.strip()][:5]
    has_md_headers = any(l.startswith("#") for l in first_content_lines)

    if not has_md_headers and first_content_lines:
        # Pattern C: plain text headers (Series 5C, 5D)
        # Line 1 is ID label, line 2 is title/subtitle, rest is body
        id_line = first_content_lines[0] if first_content_lines else ""
        title_line = first_content_lines[1] if len(first_content_lines) > 1 else ""

        # Check if first line is an ID label
        if re.match(r"^(?:RHTP|Article|Technical Document)\s+[\d.A-Z-]+", id_line):
            h1_lines.append(id_line)
            # Second line is the real title; treat as subtitle initially
            if title_line and not title_line.startswith("*"):
                subtitle = title_line
            # Collect body from line 3 onward
            found_title = False
            for line in lines:
                stripped = line.strip()
                if not stripped:
                    continue
                if not found_title:
                    if stripped == title_line:
                        found_title = True
                        continue
                    if stripped == id_line:
                        continue
                    continue
                # Italic series lines
                if stripped.startswith("*") and not stripped.startswith("**"):
                    candidate = stripped.strip("*").strip()
                    if "Series" in candidate and not series_line:
                        series_line = candidate
                        continue
                body_lines.append(stripped)
        else:
            # Unknown headerless format, use filename
            pass
    else:
        # --- Standard markdown parsing ---
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue

            # Collect H1 lines (before hitting H2 or body)
            if stripped.startswith("# ") and not stripped.startswith("## ") and not past_header:
                h1_lines.append(stripped[2:].strip())
                continue

            # H2 as subtitle
            if stripped.startswith("## ") and not subtitle and h1_lines:
                subtitle = stripped[3:].strip()
                past_header = True
                continue

            # Italic line handling
            if stripped.startswith("*") and not stripped.startswith("**"):
                candidate = stripped.strip("*").strip()
                if "Series" in candidate and not series_line:
                    series_line = candidate
                    past_header = True
                    continue
                # Non-series italic: treat as subtitle (descriptive tagline)
                elif not subtitle and h1_lines:
                    subtitle = candidate
                    continue

            # Everything else is body
            if h1_lines:
                past_header = True
            if stripped and not stripped.startswith("#") and past_header:
                body_lines.append(stripped)

    # --- Build display title ---

    if len(h1_lines) >= 2:
        # Two H1 pattern: first is ID prefix, second is title
        display_title = h1_lines[1]
    elif len(h1_lines) == 1:
        raw = h1_lines[0]

        if _is_id_only(raw) and subtitle:
            # ID-only H1: promote H2/subtitle to title
            # Pattern B: "RHTP 5.A" with subtitle "Lead Agency Structures..."
            # Pattern C: "RHTP 5.C" with subtitle "Procurement and Contracting..."
            # Pattern D: "RHTP 3.NC.1: North Carolina" with subtitle "The Problem"
            display_title = subtitle
            subtitle = ""  # consumed as title

        elif re.match(r"^Technical Document\s+\d+-TD-[A-Z]", raw) and subtitle:
            # Technical document label: use subtitle as title
            display_title = subtitle
            subtitle = ""

        else:
            # Strip ID prefix: "Article 1E: Healthcare Access" -> "Healthcare Access"
            m = re.match(r"^(?:Article|RHTP|Technical Document)\s+[\d.A-Z-]+[:\s]+(.+)", raw)
            if m:
                display_title = m.group(1).strip()
            else:
                display_title = raw
    else:
        display_title = Path(filepath).stem

    # --- State profile part title integration ---
    # If this is a state multi-part article and display_title is just a part name
    # like "The Problem", combine with state name for the display
    fname = Path(filepath).name
    state_info = extract_state_info(fname)
    if state_info[0] and state_info[2]:  # has state_code and part number
        state_name = state_info[1]
        part_title_raw = state_info[3] or ""
        # If display_title is a short part label (e.g., "The Problem", "The Plan"),
        # build the proper combined title
        if display_title in ("The Problem", "The Plan", "The Analysis"):
            display_title = f"{state_name}, {display_title}"

    # Excerpt: first 500 words of body
    body_text = " ".join(body_lines)
    words = body_text.split()[:500]
    excerpt = " ".join(words)

    return {
        "display_title": display_title,
        "subtitle": subtitle,
        "series_line": series_line,
        "excerpt": excerpt,
        "full_text": content,
        "h1_lines": h1_lines,
    }


def generate_slug(display_title, article_id, state_info=None):
    """Generate URL-friendly slug."""
    # For state articles, use state-name-part-title format
    state_code, state_name, part, part_title = state_info or (None, None, None, None)
    if state_name and part and part_title:
        raw = f"{state_name} {part_title}"
    elif state_name:
        raw = state_name
    elif display_title:
        raw = display_title
    else:
        raw = article_id

    slug = raw.lower()
    slug = slug.replace("/", "-")  # SDOH/HRSN/CHW/CIE -> SDOH-HRSN-CHW-CIE
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug[:80]


def generate_tags(series_num, article_type, state_code=None, filepath=None):
    """Generate tags based on series, type, and content scanning."""
    tags = list(SERIES_TAGS.get(series_num, ["rural-health", "rhtp"]))
    tags.append(f"series-{series_num}")

    if article_type == "technical_document":
        tags.append("technical-document")
    elif article_type == "synthesis":
        tags.append("synthesis")
    elif article_type == "companion":
        tags.append("companion")
    elif article_type == "state_profile" and state_code:
        tags.append("state-profile")
        tags.append(STATE_NAMES.get(state_code, "").lower().replace(" ", "-"))

    # Content-based tag enrichment
    if filepath:
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read().lower()
            if text.count("medicaid") > 5 and "medicaid" not in tags:
                tags.append("medicaid")
            if text.count("medicare") > 5 and "medicare" not in tags:
                tags.append("medicare")
            if "sdoh" in text or "social determinants" in text:
                tags.append("sdoh")
            if "telehealth" in text or "virtual care" in text:
                tags.append("telehealth")
        except Exception:
            pass

    return list(dict.fromkeys(tags))  # deduplicate preserving order


# ============================================================
# HUGO FRONT MATTER
# ============================================================

def build_front_matter(meta, date_str, summary_text=""):
    """Build YAML front matter string for a Hugo page bundle."""
    fm = []
    fm.append("---")
    fm.append(f'title: "{escape_yaml(meta["display_title"])}"')
    fm.append(f"date: {date_str}")
    fm.append(f'author: "Syam Adusumilli"')

    # Summary for list pages (first 200 chars of subtitle or excerpt)
    if meta.get("subtitle"):
        fm.append(f'summary: "{escape_yaml(meta["subtitle"][:200])}"')
    elif summary_text:
        fm.append(f'summary: "{escape_yaml(summary_text[:200])}"')

    fm.append(f'description: "RHTP Series {meta["series_num"]}: {escape_yaml(meta["display_title"])}"')

    # Tags
    tags_str = ", ".join(f'"{t}"' for t in meta["tags"])
    fm.append(f"tags: [{tags_str}]")
    fm.append(f'categories: ["Rural Health Transformation"]')
    fm.append(f'series: ["Series {meta["series_num"]}: {SERIES_TITLES.get(meta["series_num"], "")}"]')

    # Display settings
    fm.append("showtoc: true")
    fm.append("tocopen: false")
    fm.append("ShowReadingTime: true")
    fm.append("ShowWordCount: true")
    fm.append("ShowBreadCrumbs: true")
    fm.append("ShowPostNavLinks: true")

    # Cover image
    fm.append("cover:")
    fm.append('  image: "cover.webp"')
    fm.append(f'  alt: "{escape_yaml(meta["display_title"])}"')
    fm.append("  relative: true")
    fm.append("  hidden: false")

    # Custom params
    fm.append("params:")
    fm.append(f'  article_id: "{meta["article_id"]}"')
    fm.append(f'  article_type: "{meta["article_type"]}"')
    fm.append(f'  series_number: {meta["series_num"]}')
    fm.append(f'  series_title: "{SERIES_TITLES.get(meta["series_num"], "")}"')

    # Summary URL (points to sibling summary page)
    fm.append(f'  summary_url: "../{meta["slug"]}-summary/"')

    # State-specific params
    if meta.get("state_code"):
        fm.append(f'  state: "{STATE_NAMES.get(meta["state_code"], "")}"')
        fm.append(f'  state_code: "{meta["state_code"]}"')
        if meta.get("part"):
            fm.append(f'  part: {meta["part"]}')
        if meta.get("part_title"):
            fm.append(f'  part_title: "{escape_yaml(meta["part_title"])}"')

    # LinkedIn lead-in (stored for future use)
    if meta.get("linkedin_lead_in"):
        fm.append(f'  linkedin_lead_in: "{escape_yaml(meta["linkedin_lead_in"][:500])}"')

    fm.append(f'  collection: "rural-health"')
    fm.append("---")
    return "\n".join(fm)


def build_summary_front_matter(meta, date_str):
    """Build front matter for an executive summary page."""
    fm = []
    fm.append("---")
    fm.append(f'title: "Executive Summary: {escape_yaml(meta["display_title"])}"')
    fm.append(f"date: {date_str}")
    fm.append(f'author: "Syam Adusumilli"')
    fm.append(f'summary: "Executive summary of {escape_yaml(meta["display_title"])}"')
    tags_str = ", ".join(f'"{t}"' for t in meta["tags"][:4])
    fm.append(f"tags: [{tags_str}, \"summary\"]")
    fm.append("showtoc: false")
    fm.append("ShowReadingTime: true")
    fm.append("ShowBreadCrumbs: true")
    fm.append("params:")
    fm.append("  is_summary: true")
    fm.append(f'  full_article_url: "../{meta["slug"]}/"')
    fm.append(f'  article_id: "{meta["article_id"]}-Summary"')
    fm.append(f'  collection: "rural-health"')
    fm.append("weight: 999")
    fm.append("---")
    return "\n".join(fm)


def escape_yaml(text):
    """Escape special characters for YAML strings."""
    if not text:
        return ""
    return text.replace('"', '\\"').replace("\n", " ").strip()


# ============================================================
# IMAGE GENERATION (from pipeline.py, adapted for Hugo)
# ============================================================

def generate_image_prompt(meta, model=None):
    """Use Claude to generate a Flux-Schnell image prompt."""
    import anthropic
    client = anthropic.Anthropic()

    user_message = f"""Article title: {meta['display_title']}
Subtitle: {meta.get('subtitle', '')}
Series: Series {meta['series_num']}: {SERIES_TITLES.get(meta['series_num'], '')}
Article type: {meta['article_type']}

Article excerpt:
{meta['excerpt'][:2000]}"""

    response = client.messages.create(
        model=model or MODEL_IMAGE_PROMPT,
        max_tokens=300,
        system=IMAGE_PROMPT_STYLE,
        messages=[{"role": "user", "content": user_message}]
    )
    return response.content[0].text.strip()


def generate_image(prompt, output_path, max_retries=5):
    """Generate image via Replicate flux-schnell and save as webp.
    Retries on 429 rate limit errors with backoff."""
    import replicate
    import requests

    for attempt in range(max_retries):
        try:
            output = replicate.run(
                "black-forest-labs/flux-schnell",
                input={
                    "prompt": prompt,
                    "width": IMAGE_WIDTH,
                    "height": IMAGE_HEIGHT,
                    "num_outputs": 1,
                    "output_format": "webp",
                    "output_quality": 80,
                }
            )

            if output and len(output) > 0:
                image_url = output[0].url if hasattr(output[0], 'url') else str(output[0])
                response = requests.get(image_url)
                with open(output_path, "wb") as f:
                    f.write(response.content)
                print(f"    Image saved: {output_path}")
                return True
            else:
                print(f"    ERROR: No output from Replicate")
                return False

        except Exception as e:
            error_str = str(e)
            if "429" in error_str or "throttled" in error_str.lower():
                # Extract wait time from error if available
                wait_match = re.search(r"resets in ~(\d+)s", error_str)
                wait_time = int(wait_match.group(1)) + 2 if wait_match else 12
                print(f"    Rate limited (attempt {attempt + 1}/{max_retries}), waiting {wait_time}s...")
                time.sleep(wait_time)
                continue
            else:
                print(f"    ERROR generating image: {e}")
                return False

    print(f"    ERROR: Max retries exceeded for rate limiting")
    return False


def save_prompt_json(meta, prompt, prompts_dir):
    """Save image prompt for review before generation."""
    prompt_file = Path(prompts_dir) / f"{meta['article_id']}_prompt.json"
    data = {
        "article_id": meta["article_id"],
        "filename": meta["filename"],
        "title": meta["display_title"],
        "slug": meta["slug"],
        "prompt": prompt,
        "generated_at": datetime.now().isoformat(),
        "status": "pending_review",
    }
    with open(prompt_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return prompt_file


# ============================================================
# EXECUTIVE SUMMARY GENERATION
# ============================================================

def generate_executive_summary(meta, model=None):
    """Use Claude to generate an 800-1000 word executive summary."""
    import anthropic
    client = anthropic.Anthropic()

    user_message = f"""Article ID: {meta['article_id']}
Title: {meta['display_title']}
Subtitle: {meta.get('subtitle', '')}
Series: Series {meta['series_num']}: {SERIES_TITLES.get(meta['series_num'], '')}
Type: {meta['article_type']}

Full article text:
{meta['full_text']}"""

    response = client.messages.create(
        model=model or MODEL_SUMMARY,
        max_tokens=2000,
        system=SUMMARY_STYLE,
        messages=[{"role": "user", "content": user_message}]
    )
    return response.content[0].text.strip()


# ============================================================
# PAGE BUNDLE ASSEMBLY
# ============================================================

def strip_article_header(full_text):
    """Remove the H1/H2/series header from article content for Hugo.
    Hugo renders the title from front matter, so we strip the redundant header."""
    lines = full_text.split("\n")
    result = []
    past_header = False

    for line in lines:
        stripped = line.strip()

        if not past_header:
            # Skip H1 lines
            if stripped.startswith("# ") and not stripped.startswith("## "):
                continue
            # Skip H2 that is the subtitle (first H2 only)
            if stripped.startswith("## ") and not result:
                continue
            # Skip italic series line
            if stripped.startswith("*") and not stripped.startswith("**"):
                if "Series" in stripped:
                    continue
            # Skip separator lines
            if stripped == "---":
                continue
            # Skip empty lines before content starts
            if not stripped:
                continue
            # First real content line marks end of header
            past_header = True

        result.append(line)

    return "\n".join(result)


def write_page_bundle(meta, date_str, content_dir, summary_text=None,
                      prompt=None, dry_run=False, skip_images=False, skip_summaries=False):
    """Write a complete Hugo page bundle for one article."""
    series_dir = Path(content_dir) / f"series-{meta['series_num']}"
    article_dir = series_dir / meta["slug"]
    summary_dir = series_dir / f"{meta['slug']}-summary"

    if dry_run:
        print(f"    [DRY RUN] Would create: {article_dir}/")
        return article_dir

    # Create directories
    article_dir.mkdir(parents=True, exist_ok=True)

    # Write main article index.md
    body = strip_article_header(meta["full_text"])
    front_matter = build_front_matter(meta, date_str, summary_text or "")
    article_path = article_dir / "index.md"
    with open(article_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write("\n\n")
        f.write(body)
    print(f"    Article: {article_path}")

    # Write executive summary if provided
    if summary_text and not skip_summaries:
        summary_dir.mkdir(parents=True, exist_ok=True)
        summary_fm = build_summary_front_matter(meta, date_str)
        summary_path = summary_dir / "index.md"
        with open(summary_path, "w", encoding="utf-8") as f:
            f.write(summary_fm)
            f.write("\n\n")
            f.write(summary_text)
        print(f"    Summary: {summary_path}")

    return article_dir


def write_section_indexes(content_dir):
    """Write _index.md files for the rural-health section and each series."""
    rh_dir = Path(content_dir)
    rh_dir.mkdir(parents=True, exist_ok=True)

    # Main section index
    rh_index = rh_dir / "_index.md"
    if not rh_index.exists():
        with open(rh_index, "w") as f:
            f.write("---\n")
            f.write('title: "Rural Health Transformation Project"\n')
            f.write('description: "Systematic analysis of the $50 billion Rural Health Transformation Program"\n')
            f.write("---\n")
        print(f"  Created: {rh_index}")

    # Series indexes
    for num, title in SERIES_TITLES.items():
        series_dir = rh_dir / f"series-{num}"
        series_dir.mkdir(parents=True, exist_ok=True)
        index_path = series_dir / "_index.md"
        if not index_path.exists():
            with open(index_path, "w") as f:
                f.write("---\n")
                f.write(f'title: "Series {num}: {title}"\n')
                f.write(f'description: "RHTP Series {num}: {title}"\n')
                f.write("---\n")
            print(f"  Created: {index_path}")


# ============================================================
# DATE STAGGERING
# ============================================================

def assign_dates(articles):
    """Assign sequential dates across all articles, grouped by series."""
    current_date = START_DATE
    for article in articles:
        article["date"] = current_date.strftime("%Y-%m-%d")
        current_date += timedelta(days=1)


# ============================================================
# BATCH ORCHESTRATION
# ============================================================

def scan_articles(source_dir):
    """Scan source directory and return parsed, sorted article metadata list."""
    articles = []
    skipped = []

    # Collect all .md files recursively
    all_files = []
    for root, dirs, files in os.walk(source_dir):
        for f in files:
            if f.endswith(".md"):
                all_files.append((f, os.path.join(root, f)))
    all_files.sort(key=lambda x: x[0])

    for f, filepath in all_files:
        if should_exclude(f):
            skipped.append(f)
            continue
        series_num = extract_series_number(f)
        if not series_num:
            skipped.append(f)
            continue

        # Parse metadata
        article_id = extract_article_id(f)
        article_type = extract_article_type(f, article_id)
        state_code, state_name, part, part_title = extract_state_info(f)
        content = extract_content(filepath)
        series_order = extract_series_order(f, series_num)
        slug = generate_slug(content["display_title"], article_id,
                           (state_code, state_name, part, part_title))
        tags = generate_tags(series_num, article_type, state_code, filepath)

        meta = {
            "filename": f,
            "filepath": filepath,
            "article_id": article_id,
            "article_type": article_type,
            "series_num": series_num,
            "series_order": series_order,
            "display_title": content["display_title"],
            "subtitle": content["subtitle"],
            "series_line": content["series_line"],
            "excerpt": content["excerpt"],
            "full_text": content["full_text"],
            "slug": slug,
            "tags": tags,
            "state_code": state_code,
            "state_name": state_name,
            "part": part,
            "part_title": part_title,
        }
        articles.append(meta)

    # Sort by series number, then by series order
    articles.sort(key=lambda a: (a["series_num"], a["series_order"]))

    # Assign dates
    assign_dates(articles)

    print(f"\n  Found {len(articles)} articles, skipped {len(skipped)} files")
    print(f"  Series breakdown:")
    series_counts = {}
    for a in articles:
        s = a["series_num"]
        series_counts[s] = series_counts.get(s, 0) + 1
    for s in sorted(series_counts):
        print(f"    Series {s}: {series_counts[s]} articles")

    return articles, skipped


def process_batch(articles, content_dir, prompts_dir, args):
    """Process all articles according to CLI flags."""
    content_dir = Path(content_dir)
    prompts_dir = Path(prompts_dir)
    prompts_dir.mkdir(parents=True, exist_ok=True)

    # Write section indexes first
    if not args.dry_run:
        write_section_indexes(content_dir)

    processed = 0
    img_generated = 0
    img_skipped = 0
    sum_generated = 0
    errors = 0

    for meta in articles:
        print(f"\n  [{processed+1}/{len(articles)}] {meta['article_id']}: {meta['display_title']}")

        # --- Image prompt ---
        prompt = None
        cover_path = content_dir / f"series-{meta['series_num']}" / meta["slug"] / "cover.webp"

        if not args.no_images and not args.summaries_only:
            if cover_path.exists() and not args.prompts_only:
                print(f"    Image exists, skipping")
                img_skipped += 1
            else:
                try:
                    if not args.dry_run:
                        prompt = generate_image_prompt(meta, model=args.model)
                        print(f"    Prompt: {prompt[:100]}...")
                        save_prompt_json(meta, prompt, prompts_dir)

                        if not args.prompts_only:
                            # Ensure directory exists
                            cover_path.parent.mkdir(parents=True, exist_ok=True)
                            success = generate_image(prompt, cover_path)
                            if success:
                                img_generated += 1
                            else:
                                errors += 1
                    else:
                        print(f"    [DRY RUN] Would generate image prompt + image")
                except Exception as e:
                    print(f"    ERROR (image): {e}")
                    errors += 1

        # --- Executive summary ---
        summary_text = None
        if not args.no_summaries and not args.images_only and not args.prompts_only:
            summary_path = (content_dir / f"series-{meta['series_num']}"
                          / f"{meta['slug']}-summary" / "index.md")
            if summary_path.exists():
                print(f"    Summary exists, skipping")
            else:
                try:
                    if not args.dry_run:
                        print(f"    Generating executive summary...")
                        summary_text = generate_executive_summary(meta, model=args.model)
                        sum_generated += 1
                        print(f"    Summary: {len(summary_text.split())} words")
                    else:
                        print(f"    [DRY RUN] Would generate executive summary")
                except Exception as e:
                    print(f"    ERROR (summary): {e}")
                    errors += 1

        # --- Write page bundle ---
        if not args.prompts_only:
            write_page_bundle(
                meta, meta["date"], content_dir,
                summary_text=summary_text,
                prompt=prompt,
                dry_run=args.dry_run,
                skip_images=args.no_images,
                skip_summaries=args.no_summaries,
            )

        processed += 1
        # Rate limiting for API calls
        if not args.dry_run and not args.prompts_only:
            time.sleep(0.5)

    print(f"\n{'='*60}")
    print(f"  COMPLETE")
    print(f"  Articles processed: {processed}")
    print(f"  Images generated: {img_generated}, skipped: {img_skipped}")
    print(f"  Summaries generated: {sum_generated}")
    print(f"  Errors: {errors}")
    print(f"{'='*60}")


def process_from_prompts(prompts_dir, content_dir):
    """Generate images from previously saved and reviewed prompt files."""
    import requests

    prompt_files = sorted(Path(prompts_dir).glob("*_prompt.json"))
    print(f"  Found {len(prompt_files)} prompt files")

    generated = 0
    skipped = 0
    errors = 0

    for prompt_file in prompt_files:
        with open(prompt_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if data.get("status") == "skip":
            print(f"\n  Skipping (marked skip): {data['article_id']}")
            skipped += 1
            continue

        # Determine output path from slug
        slug = data.get("slug", data["article_id"].lower().replace("-", "-"))
        # We need series number to find the right directory
        # Extract from article_id: RHTP-4A -> 4, RHTP-3AL-1 -> 3
        m = re.match(r"RHTP-(\d+)", data["article_id"])
        series_num = int(m.group(1)) if m else 0

        cover_path = Path(content_dir) / f"series-{series_num}" / slug / "cover.webp"

        if cover_path.exists():
            print(f"\n  Exists, skipping: {data['article_id']}")
            skipped += 1
            continue

        print(f"\n  Generating: {data['article_id']}")
        print(f"    Prompt: {data['prompt'][:100]}...")

        cover_path.parent.mkdir(parents=True, exist_ok=True)
        success = generate_image(data["prompt"], cover_path)

        if success:
            data["status"] = "generated"
            data["generated_at"] = datetime.now().isoformat()
            with open(prompt_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            generated += 1
        else:
            errors += 1

        time.sleep(11)  # Stay under 6 req/min rate limit

    print(f"\n  Complete: {generated} generated, {skipped} skipped, {errors} errors")


# ============================================================
# MANIFEST EXPORT
# ============================================================

def export_manifest(articles, output_path):
    """Export article manifest as JSON for debugging and verification."""
    manifest = {
        "generated_at": datetime.now().isoformat(),
        "total_articles": len(articles),
        "articles": [
            {
                "article_id": a["article_id"],
                "display_title": a["display_title"],
                "subtitle": a.get("subtitle", ""),
                "series_num": a["series_num"],
                "article_type": a["article_type"],
                "slug": a["slug"],
                "date": a.get("date", ""),
                "state_code": a.get("state_code"),
                "tags": a["tags"],
                "filename": a["filename"],
            }
            for a in articles
        ],
    }
    with open(output_path, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"  Manifest written to {output_path}")


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="RHTP Hugo Processing Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python process_articles.py ./rural-health/                  Full pipeline
  python process_articles.py ./rural-health/ --dry-run        Preview without API calls
  python process_articles.py ./rural-health/ --prompts-only   Generate prompts for review
  python process_articles.py --from-prompts prompts/          Images from reviewed prompts
  python process_articles.py ./rural-health/ --no-images      Skip image generation
  python process_articles.py ./rural-health/ --no-summaries   Skip summary generation
  python process_articles.py ./rural-health/ --images-only    Only generate images
  python process_articles.py ./rural-health/ --summaries-only Only generate summaries
  python process_articles.py ./rural-health/ --manifest-only  Export manifest JSON

Cost estimates (229 articles):
  Image prompts (Haiku):    ~$0.50
  Cover images (Schnell):   ~$0.50
  Exec summaries (Sonnet):  ~$25-30
  Total:                    ~$26-31
        """
    )
    parser.add_argument("input", nargs="?",
                        help="Source directory of markdown files")
    parser.add_argument("--content-dir", default="content/rural-health",
                        help="Hugo content output directory (default: content/rural-health)")
    parser.add_argument("--prompts-dir", default="prompts",
                        help="Directory for image prompt JSON files (default: prompts)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Preview processing without API calls or file writes")
    parser.add_argument("--prompts-only", action="store_true",
                        help="Generate image prompts for review, skip generation")
    parser.add_argument("--from-prompts", type=str,
                        help="Generate images from reviewed prompt files in this directory")
    parser.add_argument("--no-images", action="store_true",
                        help="Skip all image generation")
    parser.add_argument("--no-summaries", action="store_true",
                        help="Skip all executive summary generation")
    parser.add_argument("--images-only", action="store_true",
                        help="Only generate images, skip summaries and page bundles")
    parser.add_argument("--summaries-only", action="store_true",
                        help="Only generate summaries, skip images")
    parser.add_argument("--manifest-only", action="store_true",
                        help="Export article manifest JSON, no processing")
    parser.add_argument("--model", type=str, default=None,
                        help="Override Claude model for ALL API calls")

    args = parser.parse_args()

    print("=" * 60)
    print("  RHTP Hugo Processing Pipeline")
    print("=" * 60)

    # Mode: generate from existing prompts
    if args.from_prompts:
        process_from_prompts(args.from_prompts, args.content_dir)
        return

    # Mode: process articles
    if not args.input:
        parser.print_help()
        return

    source_dir = Path(args.input)
    if not source_dir.is_dir():
        print(f"  ERROR: {source_dir} is not a directory")
        sys.exit(1)

    # Scan and parse all articles
    articles, skipped = scan_articles(source_dir)

    if not articles:
        print("  No articles found")
        return

    # Manifest-only mode
    if args.manifest_only:
        export_manifest(articles, "manifest.json")
        return

    # Process
    process_batch(articles, args.content_dir, args.prompts_dir, args)

    # Always export manifest after processing
    if not args.dry_run:
        export_manifest(articles, "manifest.json")

    # Post-processing instructions
    if args.prompts_only:
        print(f"\n  Image prompts saved to: {args.prompts_dir}/")
        print(f"  Review and edit prompt JSON files as needed.")
        print(f"  Set 'status' to 'skip' for any to skip.")
        print(f"  Then generate images:")
        print(f"    python process_articles.py --from-prompts {args.prompts_dir}/")


if __name__ == "__main__":
    main()
