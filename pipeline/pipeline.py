"""
BGM Image Generation Pipeline v2
Reads markdown articles, generates image prompts via Claude,
generates images via Flux-Schnell on Replicate,
generates LinkedIn packages via Claude,
uploads images to Cloudflare R2,
and optionally updates Notion.

Usage:
  Single article:       python pipeline.py article.md
  Folder of articles:   python pipeline.py ./articles/
  With Notion upload:   python pipeline.py article.md --notion --db bgm
  Review prompts only:  python pipeline.py article.md --prompts-only
  From existing prompts: python pipeline.py --from-prompts prompts/
  LinkedIn only:        python pipeline.py article.md --linkedin-only
  Images only (no LI):  python pipeline.py article.md --no-linkedin
  Upload images to R2:  python pipeline.py --upload-r2
  Full batch workflow:
    python pipeline.py ./articles/ --prompts-only
    (review/edit prompts and linkedin drafts in prompts/ and linkedin/ folders)
    python pipeline.py --from-prompts prompts/
    python pipeline.py --upload-r2
"""

import os
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

# --- Load .env ---

def load_env():
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

load_env()

import anthropic
import replicate
import requests
from PIL import Image
from io import BytesIO


# --- Configuration ---

PROMPT_STYLE = """You are generating an image prompt for Flux-Schnell, an AI image model.
The image will accompany a blog article about aging in America for a publication
called Blue Gray Matters.

Visual style guidelines:
- Documentary photography feel, not stock photography
- Warm, muted tones. Morning light preferred.
- Domestic, lived-in settings. Kitchen tables, living rooms, porches, hands.
- Never show faces clearly (privacy, universality). Hands, silhouettes, over-shoulder, overhead shots.
- No hospital or clinical settings unless the article specifically requires it.
- No cliched "worried senior staring into distance" compositions.
- No overly bright, cheerful, or sterile aesthetics.
- Convey quiet weight, dignity, and the texture of daily life.
- Think photojournalism, not advertising.

Read the article excerpt below and generate a single image prompt for Flux-Schnell.
The prompt should be 2-4 sentences of specific, descriptive language covering:
composition, lighting, key objects, mood, and photographic style.
Do not include any explanation, just the prompt itself."""

LINKEDIN_STYLE = """You are writing a LinkedIn lead-in post and pinned first comment for an article
from Blue Gray Matters, a publication about aging in America.

Voice: Warm, steady, grounded. Not clinical, not cheerful, not pitying. Write as a
trusted companion who is deeply informed. Hope earned through evidence, not manufactured.

ABSOLUTE RULES:
- No em dashes. Use commas, semicolons, colons, parentheses instead.
- No "it's important to note," "groundbreaking," "game-changing," "delve into,"
  "shed light on," "pave the way," "paradigm shift," "leverage," "synergy,"
  "robust," "utilize," "facilitate," or any AI slop phrases.
- No bullet points in the lead-in post. Flowing prose only.
- No "silver tsunami," "burden of care," or "losing the battle."

LEAD-IN POST structure:
- Open with the most striking data point or human moment from the article
- State the core problem or gap in 2-3 sentences
- Frame as systemic, not individual failure (where applicable)
- Name the series and its position within the publication
- Close with a kitchen table line connecting to the reader's life
- End with a [Link] placeholder and hashtags on the last line:
  #aging #retirement #Medicare #healthcare #seniorcare #caregiving #financialplanning #BlueGrayMatters
  (adjust hashtags to match the article's specific topics)

PINNED FIRST COMMENT structure:
- Open with: "A few things I expect to hear, because I've heard them before."
- Preempt 3-4 predictable objections or counterarguments
- Each objection gets a 2-3 sentence response grounded in data from the article
- Reference specific future installments where topics are covered in depth
- Close with: "This is [position] of [total] pieces. I'm not here to provoke.
  I'm here to show the full picture, because you can't plan around a system
  you don't understand."

Output format: Return ONLY a JSON object with two keys:
  "lead_in": the full lead-in post text
  "pinned_comment": the full pinned first comment text
No markdown backticks, no explanation, just the JSON."""

IMAGE_WIDTH = 1200
IMAGE_HEIGHT = 630
NUM_OUTPUTS = 1

# Model defaults (override with --model flag)
MODEL_IMAGE_PROMPT = "claude-haiku-4-5-20251001"
MODEL_LINKEDIN = "claude-sonnet-4-5-20250929"

# Database name mapping for --db flag
DB_PREFIX = "NOTION_DATABASE_ID_"


# --- Helper Functions ---

def get_notion_db_id(db_name):
    """Get Notion database ID from .env using the --db flag value."""
    if not db_name:
        # Fall back to generic key for backward compatibility
        return os.environ.get("NOTION_DATABASE_ID")
    key = f"{DB_PREFIX}{db_name.upper()}"
    db_id = os.environ.get(key)
    if not db_id:
        print(f"  ERROR: No database ID found for '{db_name}'. Expected .env key: {key}")
        print(f"  Available DB keys: {[k for k in os.environ if k.startswith(DB_PREFIX)]}")
    return db_id


def extract_article_content(filepath):
    """Extract title, subtitle, series info, and opening content from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    title = ""
    subtitle = ""
    series_line = ""
    body_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# ") and not title:
            title = stripped.lstrip("# ")
        elif stripped.startswith("## ") and not subtitle:
            subtitle = stripped.lstrip("## ")
        elif (stripped.startswith("*BGM") or stripped.startswith("*Series")) and not series_line:
            series_line = stripped.strip("*")
        elif stripped and not stripped.startswith("#"):
            body_lines.append(stripped)

    body_text = " ".join(body_lines)
    words = body_text.split()[:500]
    body_excerpt = " ".join(words)

    # Extract article ID from filename (e.g., BGM-1A from BGM-1A_The_Price_Tag...)
    filename = Path(filepath).stem
    article_id = ""
    if filename.startswith("BGM-"):
        parts = filename.split("_", 1)
        if parts:
            article_id = parts[0]

    return {
        "title": title,
        "subtitle": subtitle,
        "series_line": series_line,
        "excerpt": body_excerpt,
        "full_text": content,
        "filename": filename,
        "article_id": article_id
    }


def generate_image_prompt(article_data, model=None):
    """Use Claude to generate a Flux-Schnell image prompt from article content."""
    client = anthropic.Anthropic()

    user_message = f"""Article title: {article_data['title']}
Subtitle: {article_data['subtitle']}
Series: {article_data['series_line']}

Article excerpt:
{article_data['excerpt']}"""

    response = client.messages.create(
        model=model or MODEL_IMAGE_PROMPT,
        max_tokens=300,
        system=PROMPT_STYLE,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    return response.content[0].text.strip()


def generate_linkedin_package(article_data, model=None):
    """Use Claude to generate a LinkedIn lead-in post and pinned comment."""
    client = anthropic.Anthropic()

    # Send full article text (not just excerpt) for better LinkedIn content
    user_message = f"""Article ID: {article_data['article_id']}
Article title: {article_data['title']}
Subtitle: {article_data['subtitle']}
Series: {article_data['series_line']}

Full article text:
{article_data['full_text']}"""

    response = client.messages.create(
        model=model or MODEL_LINKEDIN,
        max_tokens=1500,
        system=LINKEDIN_STYLE,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )

    raw = response.content[0].text.strip()

    # Parse JSON response
    try:
        # Strip markdown backticks if model included them despite instructions
        cleaned = raw
        if cleaned.startswith("```"):
            cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned[3:]
        if cleaned.endswith("```"):
            cleaned = cleaned[:-3]
        cleaned = cleaned.strip()

        data = json.loads(cleaned)
        return data
    except json.JSONDecodeError:
        print(f"  WARNING: Could not parse LinkedIn JSON. Saving raw text.")
        return {"lead_in": raw, "pinned_comment": "", "parse_error": True}


def generate_image(prompt, output_path):
    """Generate an image using Flux-Schnell on Replicate."""
    try:
        output = replicate.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": prompt,
                "width": IMAGE_WIDTH,
                "height": IMAGE_HEIGHT,
                "num_outputs": NUM_OUTPUTS,
                "output_format": "png",
                "output_quality": 90
            }
        )

        if output and len(output) > 0:
            image_url = output[0].url if hasattr(output[0], 'url') else str(output[0])
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            img.save(output_path, "PNG")
            print(f"  Image saved: {output_path}")
            return True
        else:
            print(f"  ERROR: No output from Replicate")
            return False

    except Exception as e:
        print(f"  ERROR generating image: {e}")
        return False


def upload_to_r2(filepath, bucket_name=None, public_url_base=None):
    """Upload an image to Cloudflare R2 and return the public URL."""
    try:
        import boto3
    except ImportError:
        print("  ERROR: boto3 not installed. Run: pip install boto3")
        return None

    bucket = bucket_name or os.environ.get("R2_BUCKET_NAME")
    endpoint = os.environ.get("R2_ENDPOINT_URL")
    access_key = os.environ.get("R2_ACCESS_KEY_ID")
    secret_key = os.environ.get("R2_SECRET_ACCESS_KEY")
    url_base = public_url_base or os.environ.get("R2_PUBLIC_URL_BASE", "")

    if not all([bucket, endpoint, access_key, secret_key]):
        missing = []
        if not bucket: missing.append("R2_BUCKET_NAME")
        if not endpoint: missing.append("R2_ENDPOINT_URL")
        if not access_key: missing.append("R2_ACCESS_KEY_ID")
        if not secret_key: missing.append("R2_SECRET_ACCESS_KEY")
        print(f"  ERROR: Missing R2 config: {', '.join(missing)}")
        return None

    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto"
    )

    filename = Path(filepath).name
    r2_key = f"images/{filename}"

    try:
        s3.upload_file(
            str(filepath),
            bucket,
            r2_key,
            ExtraArgs={"ContentType": "image/png"}
        )
        public_url = f"{url_base.rstrip('/')}/{r2_key}" if url_base else r2_key
        print(f"  Uploaded to R2: {public_url}")
        return public_url
    except Exception as e:
        print(f"  ERROR uploading to R2: {e}")
        return None


def update_notion_image(db_id, article_title, image_url):
    """Update matching Notion page with the hosted image URL."""
    try:
        from notion_client import Client
    except ImportError:
        print("  WARNING: notion-client not installed. Run: pip install notion-client")
        return False

    notion_key = os.environ.get("NOTION_API_KEY")
    if not notion_key:
        print("  WARNING: NOTION_API_KEY not set")
        return False

    notion = Client(auth=notion_key)

    # Search by full title, then by first 5 words
    for search_title in [article_title, " ".join(article_title.split()[:5])]:
        results = notion.databases.query(
            database_id=db_id,
            filter={
                "property": "Name",
                "title": {"contains": search_title}
            }
        )
        if results["results"]:
            break

    if not results["results"]:
        print(f"  WARNING: No Notion page found for '{article_title}'")
        return False

    page_id = results["results"][0]["id"]

    # Update the Image property with the R2 URL
    # Adjust property name if your DB uses something other than "Image"
    try:
        notion.pages.update(
            page_id=page_id,
            properties={
                "Image": {
                    "url": image_url
                }
            }
        )
        print(f"  Notion updated: {page_id}")
        return True
    except Exception as e:
        print(f"  WARNING: Could not update Notion image property: {e}")
        print(f"  (Check that your DB has a URL property named 'Image')")
        return False


def save_prompt(article_data, prompt, output_dir):
    """Save the generated image prompt for review."""
    prompt_file = Path(output_dir) / f"{article_data['filename']}_prompt.json"
    data = {
        "filename": article_data["filename"],
        "article_id": article_data["article_id"],
        "title": article_data["title"],
        "subtitle": article_data["subtitle"],
        "prompt": prompt,
        "generated_at": datetime.now().isoformat(),
        "status": "pending_review"
    }
    with open(prompt_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return prompt_file


def save_linkedin(article_data, linkedin_data, output_dir):
    """Save the generated LinkedIn package for review."""
    linkedin_file = Path(output_dir) / f"{article_data['filename']}_linkedin.json"
    data = {
        "filename": article_data["filename"],
        "article_id": article_data["article_id"],
        "title": article_data["title"],
        "lead_in": linkedin_data.get("lead_in", ""),
        "pinned_comment": linkedin_data.get("pinned_comment", ""),
        "generated_at": datetime.now().isoformat(),
        "status": "pending_review"
    }
    if linkedin_data.get("parse_error"):
        data["status"] = "parse_error_review"

    with open(linkedin_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return linkedin_file


def save_linkedin_markdown(article_data, linkedin_data, output_dir):
    """Also save a readable markdown version of the LinkedIn package."""
    md_file = Path(output_dir) / f"{article_data['filename']}_linkedin.md"
    content = f"""# {article_data['article_id']} LinkedIn Package

## Lead-In Post

{linkedin_data.get('lead_in', '')}


## Pinned First Comment

{linkedin_data.get('pinned_comment', '')}
"""
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)
    return md_file


# --- Main Pipeline ---

def process_article(filepath, output_dir, prompts_dir, linkedin_dir,
                    prompts_only=False, linkedin_only=False, no_linkedin=False,
                    db_name=None, model=None):
    """Full pipeline for a single article."""
    print(f"\nProcessing: {filepath}")

    article_data = extract_article_content(filepath)
    print(f"  Title: {article_data['title']}")
    print(f"  ID: {article_data['article_id']}")

    # --- Image prompt ---
    if not linkedin_only:
        img_model = model or MODEL_IMAGE_PROMPT
        print(f"  Generating image prompt via {img_model}...")
        prompt = generate_image_prompt(article_data, model=model)
        print(f"  Prompt: {prompt[:120]}...")

        prompt_file = save_prompt(article_data, prompt, prompts_dir)
        print(f"  Prompt saved: {prompt_file}")

    # --- LinkedIn package ---
    if not no_linkedin:
        li_model = model or MODEL_LINKEDIN
        print(f"  Generating LinkedIn package via {li_model}...")
        linkedin_data = generate_linkedin_package(article_data, model=model)
        li_json = save_linkedin(article_data, linkedin_data, linkedin_dir)
        li_md = save_linkedin_markdown(article_data, linkedin_data, linkedin_dir)
        print(f"  LinkedIn saved: {li_json}")
        print(f"  LinkedIn readable: {li_md}")

    if prompts_only or linkedin_only:
        print("  (Skipping image generation)")
        return

    # --- Image generation ---
    print("  Generating image via Flux-Schnell...")
    output_path = Path(output_dir) / f"{article_data['filename']}.png"
    success = generate_image(prompt, output_path)

    if not success:
        return


def process_from_prompts(prompts_dir, output_dir):
    """Generate images from previously saved and reviewed prompts."""
    prompt_files = sorted(Path(prompts_dir).glob("*_prompt.json"))
    print(f"Found {len(prompt_files)} prompt files")

    generated = 0
    skipped = 0
    errors = 0

    for prompt_file in prompt_files:
        with open(prompt_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        if data.get("status") == "skip":
            print(f"\nSkipping (marked skip): {data['filename']}")
            skipped += 1
            continue

        output_path = Path(output_dir) / f"{data['filename']}.png"

        if output_path.exists():
            print(f"\nExists, skipping: {data['filename']} (delete image to regenerate)")
            skipped += 1
            continue

        print(f"\nGenerating: {data['filename']}")
        print(f"  Prompt: {data['prompt'][:120]}...")

        success = generate_image(data["prompt"], output_path)

        if success:
            data["status"] = "generated"
            data["generated_image"] = str(output_path)
            with open(prompt_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            generated += 1
        else:
            errors += 1

        time.sleep(1)

    print(f"\nComplete: {generated} generated, {skipped} skipped, {errors} errors")


def upload_r2_batch(output_dir, db_name=None):
    """Upload all images in output/ to Cloudflare R2 and optionally update Notion."""
    image_files = sorted(Path(output_dir).glob("*.png"))
    print(f"Found {len(image_files)} images to upload")

    db_id = get_notion_db_id(db_name) if db_name else None
    uploaded = 0
    errors = 0

    for img_path in image_files:
        print(f"\nUploading: {img_path.name}")
        public_url = upload_to_r2(img_path)

        if public_url:
            uploaded += 1

            # Update corresponding prompt JSON with R2 URL
            prompt_json = Path("prompts") / f"{img_path.stem}_prompt.json"
            if prompt_json.exists():
                with open(prompt_json, "r") as f:
                    data = json.load(f)
                data["r2_url"] = public_url
                data["uploaded_at"] = datetime.now().isoformat()
                with open(prompt_json, "w") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

            # Update Notion if DB specified
            if db_id:
                # Extract title from prompt JSON
                if prompt_json.exists():
                    update_notion_image(db_id, data.get("title", img_path.stem), public_url)
        else:
            errors += 1

        time.sleep(0.5)

    print(f"\nR2 upload complete: {uploaded} uploaded, {errors} errors")


def main():
    parser = argparse.ArgumentParser(
        description="BGM Image + LinkedIn Generation Pipeline v2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pipeline.py article.md                     Full pipeline (prompt + image + linkedin)
  python pipeline.py ./articles/ --prompts-only      Batch: generate all prompts and linkedin drafts
  python pipeline.py --from-prompts prompts/         Generate images from reviewed prompts
  python pipeline.py --upload-r2                     Upload all images to Cloudflare R2
  python pipeline.py --upload-r2 --db bgm            Upload to R2 and update BGM Notion database
  python pipeline.py article.md --linkedin-only      Generate only the LinkedIn package
  python pipeline.py article.md --no-linkedin        Generate only the image prompt and image
  python pipeline.py article.md --model claude-sonnet-4-5-20250929   Force Sonnet for everything

Models (default): Haiku for image prompts (~$0.07/350), Sonnet for LinkedIn (~$1.05/350)
        """
    )
    parser.add_argument("input", nargs="?", help="Markdown file or folder of markdown files")
    parser.add_argument("--db", type=str, default=None,
                        help="Notion database name (maps to NOTION_DATABASE_ID_{NAME} in .env)")
    parser.add_argument("--notion", action="store_true",
                        help="Update Notion after R2 upload (use with --upload-r2)")
    parser.add_argument("--prompts-only", action="store_true",
                        help="Generate prompts and LinkedIn only, skip image generation")
    parser.add_argument("--from-prompts", type=str,
                        help="Generate images from reviewed prompt files in this directory")
    parser.add_argument("--upload-r2", action="store_true",
                        help="Upload all images in output/ to Cloudflare R2")
    parser.add_argument("--linkedin-only", action="store_true",
                        help="Generate only LinkedIn packages, skip image prompts")
    parser.add_argument("--no-linkedin", action="store_true",
                        help="Skip LinkedIn generation, do image prompts only")
    parser.add_argument("--model", type=str, default=None,
                        help="Override Claude model for ALL API calls (e.g., claude-sonnet-4-5-20250929). "
                             "Default: Haiku for image prompts, Sonnet for LinkedIn")
    parser.add_argument("--output", type=str, default="output",
                        help="Output directory for images (default: output)")
    parser.add_argument("--prompts-dir", type=str, default="prompts",
                        help="Directory for prompt files (default: prompts)")
    parser.add_argument("--linkedin-dir", type=str, default="linkedin",
                        help="Directory for LinkedIn files (default: linkedin)")

    args = parser.parse_args()

    # Ensure directories exist
    output_dir = Path(args.output)
    prompts_dir = Path(args.prompts_dir)
    linkedin_dir = Path(args.linkedin_dir)
    output_dir.mkdir(exist_ok=True)
    prompts_dir.mkdir(exist_ok=True)
    linkedin_dir.mkdir(exist_ok=True)

    # Mode: upload images to R2
    if args.upload_r2:
        upload_r2_batch(output_dir, args.db if args.notion else None)
        return

    # Mode: generate from existing prompts
    if args.from_prompts:
        process_from_prompts(args.from_prompts, output_dir)
        return

    # Mode: process articles
    if not args.input:
        parser.print_help()
        return

    input_path = Path(args.input)

    if input_path.is_file():
        process_article(
            str(input_path), output_dir, prompts_dir, linkedin_dir,
            args.prompts_only, args.linkedin_only, args.no_linkedin, args.db,
            args.model
        )
    elif input_path.is_dir():
        md_files = sorted(input_path.glob("**/*.md"))
        # Skip files that are clearly not articles (linkedin packages, context files, etc.)
        md_files = [f for f in md_files if not any(skip in f.name.lower()
                    for skip in ["_linkedin", "_context", "_pipeline", "_guide",
                                 "_architecture", "_manifesto", "_outline"])]
        print(f"Found {len(md_files)} article files")
        for md_file in md_files:
            process_article(
                str(md_file), output_dir, prompts_dir, linkedin_dir,
                args.prompts_only, args.linkedin_only, args.no_linkedin, args.db,
                args.model
            )
            time.sleep(1)
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)

    print("\nDone.")
    if args.prompts_only:
        print(f"\nImage prompts in:  {prompts_dir}/")
        print(f"LinkedIn drafts in: {linkedin_dir}/")
        print(f"\nReview and edit as needed:")
        print(f"  - Edit 'prompt' field in JSON files to change image prompts")
        print(f"  - Edit 'lead_in' and 'pinned_comment' in LinkedIn JSONs")
        print(f"  - Set 'status' to 'skip' for any you want to skip")
        print(f"\nThen generate images:")
        print(f"  python pipeline.py --from-prompts {prompts_dir}/")
        print(f"\nThen upload to R2:")
        print(f"  python pipeline.py --upload-r2")
        print(f"  python pipeline.py --upload-r2 --db bgm --notion  (also update Notion)")


if __name__ == "__main__":
    main()
