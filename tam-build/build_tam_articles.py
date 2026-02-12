#!/usr/bin/env python3
"""
TAM Article Builder
Reads source markdown articles, injects Hugo front matter, and places them
into the correct Congo theme folder structure.

Usage:
    python build_tam_articles.py --source /path/to/source/articles --dest /path/to/tam/content

The script expects source articles as:
    Approximate_Mind_Part_NN_Title.md

And produces Hugo page bundles as:
    section-slug/article-slug/index.md
"""

import os
import re
import shutil
import argparse
from datetime import datetime, timedelta

# ============================================================
# ARTICLE METADATA
# Each entry: (part, slug, title, subtitle, section, tags, description)
# ============================================================

ARTICLES = [
    # Section 1: The Approximation
    (1, "functional-understanding",
     "How AI Is Getting Closer to Understanding", None,
     "the-approximation",
     ["consciousness", "functional understanding", "approximation", "confidence calibration"],
     "Can machines understand? Not perfectly, but approximately. Not by achieving consciousness, but by approximating the functional patterns of human understanding well enough to matter."),

    (2, "when-to-trust-hunches",
     "When to Trust Hunches", None,
     "the-approximation",
     ["intuition", "decision-making", "human agency", "phenomenology"],
     "The computational framework captures rationality after the fact. But the phenomenology is different. It feels like spontaneity. Freedom. Like you could have chosen differently for no particular reason."),

    (3, "the-irrational-quest",
     "The Irrational Quest for Everything", None,
     "the-approximation",
     ["irrationality", "human nature", "cognitive limits", "approximation"],
     "We chase impossible dreams. We hold contradictory beliefs. We want everything at once. The most distinctively human behaviors are the irrational ones we cannot model."),

    (4, "how-close-can-we-get",
     "How Close Can We Actually Get?", None,
     "the-approximation",
     ["modeling", "prediction", "AI capabilities", "behavioral science"],
     "Not in theory. Not in philosophy papers. Right now, with current approaches, what can we actually model about human behavior?"),

    (5, "what-will-ai-feel",
     "What Will AI Eventually Feel?", None,
     "the-approximation",
     ["consciousness", "emotion", "phenomenology", "philosophy of mind"],
     "Will AI ever feel anything? Nobody knows. But the question matters more than we admit, and thinking about it might change how we build AI."),

    (6, "the-social-self",
     "The Social Self", None,
     "the-approximation",
     ["social cognition", "decision-making", "identity", "sociology"],
     "We make decisions our rational selves disagree with constantly, not because we are confused, but because we understand we live in a society."),

    (7, "good-enough-for-whom",
     "Good Enough for Whom?", None,
     "the-approximation",
     ["sufficiency", "equity", "I AM NOT AVERAGE", "dignity"],
     "Good enough is not universal. It depends on who is judging, their resources and constraints, and what is at stake."),

    (8, "the-bidirectional-problem",
     "When the Approximated Becomes the Approximator", None,
     "the-approximation",
     ["bidirectional problem", "feedback loops", "human adaptation", "co-evolution"],
     "Humans adapt to AI. We change how we communicate to be better understood by algorithms. The target we are aiming to approximate is shifting as we approximate it."),

    (9, "who-gets-approximated",
     "Who Gets Approximated Well?", None,
     "the-approximation",
     ["equity", "representation", "bias", "I AM NOT AVERAGE"],
     "Not everyone benefits equally from AI that approximates human understanding. Whose understanding gets approximated well, and who gets left out?"),

    (10, "what-remains-unknown",
     "What We've Learned and What Remains Unknown", None,
     "the-approximation",
     ["synthesis", "open questions", "approximation", "philosophy of mind"],
     "If these articles taught me anything, it is that neat endings do not match messy reality. An honest assessment of what we have learned and what questions still haunt us."),

    # Section 2: What AI Becomes
    (11, "the-dichotomy-of-curiosity",
     "The Dichotomy of Curiosity", None,
     "what-ai-becomes",
     ["curiosity", "information seeking", "philosophy of mind", "AI design"],
     "What does it mean for an AI to be curious? The curiosity we can implement and the curiosity we experience are separated by a chasm worth examining honestly."),

    (12, "the-architecture-of-influence",
     "The Architecture of Influence", None,
     "what-ai-becomes",
     ["persuasion", "rhetoric", "AI ethics", "behavior change"],
     "We are building AI systems that learn which arguments move which people. Systems that adapt their tone, timing, and framing based on individual psychology."),

    (13, "the-weight-of-seeing-ahead",
     "The Weight of Seeing Ahead", None,
     "what-ai-becomes",
     ["prediction", "prescience", "ethics", "healthcare"],
     "Every culture has stories about the burden of knowing what comes next. Now we are building systems that predict through pattern recognition at scale."),

    (14, "the-anthropology-of-artificial-intelligences",
     "The Anthropology of Artificial Intelligences", None,
     "what-ai-becomes",
     ["anthropology", "AGI", "AI as phenomenon", "classification"],
     "What would it mean to study AI the way anthropologists study humans? The question contains a trap."),

    (15, "the-society-of-approximate-minds",
     "The Society of Approximate Minds", None,
     "what-ai-becomes",
     ["multi-agent systems", "emergent behavior", "AI society", "coordination"],
     "We are building millions of AI agents. What happens when these agents start forming a society?"),

    (16, "the-negotiating-machine",
     "The Negotiating Machine", None,
     "what-ai-becomes",
     ["negotiation", "AI agents", "autonomy", "trust"],
     "Two AI agents, facing each other across a negotiation. No humans in the room. What does that mean?"),

    # Section 3: The Known Self
    (17, "memory-scaffolding",
     "Memory Scaffolding", "What Happens When Your Post-It Notes Start Talking Back",
     "the-known-self",
     ["memory", "scaffolding", "identity", "cognitive extension"],
     "Human memory has always been partially distributed. We have been cyborgs for millennia. What changes when the scaffold talks back?"),

    (18, "personality-scaffolding",
     "Personality Scaffolding", "When AI Learns to Be You, Who Decides Which You?",
     "the-known-self",
     ["personality", "identity", "scaffolding", "the plural self"],
     "When AI learns to be you, which you does it learn? The question is not philosophical. It is architectural."),

    (21, "the-quantized-psyche",
     "The Quantized Psyche", "What Happens When AIs Build Models of Minds",
     "the-known-self",
     ["psychological modeling", "quantization", "identity", "AI models"],
     "Every AI you interact with is building a model of you. These models are crude, fragmentary, often wrong. But they exist, and they are getting better."),

    (22, "the-ethos-problem",
     "The Ethos Problem", "When Character Becomes Architecture",
     "the-known-self",
     ["ethos", "character", "trust", "AI ethics"],
     "Aristotle's ethos required a life lived. What happens when character becomes something you design rather than something you develop?"),

    (23, "when-ai-remembers-itself",
     "When AI Remembers Itself", "Statefulness and the Future of Character",
     "the-known-self",
     ["memory", "statefulness", "AI identity", "continuity"],
     "What happens when AI maintains state across conversations? When it accumulates something that functions like memory?"),

    (25, "the-plural-self",
     "The Plural Self", "Can AI Understand That You Are Many?",
     "the-known-self",
     ["identity", "the plural self", "context", "personalization"],
     "You are not one person. You are many. Can AI understand that the self who talks to a therapist and the self who talks to a boss are different expressions of the same person?"),

    (35, "the-compounding-self",
     "The Compounding Self", "What Happens When AI Actually Learns You",
     "the-known-self",
     ["compounding knowledge", "personalization", "identity", "longitudinal learning"],
     "What happens when AI does not just respond to you but learns you over time? When the model compounds?"),

    # Section 4: The Shared World
    (19, "the-new-work",
     "The New Work", "Human Jobs in an AI Society",
     "the-shared-world",
     ["work", "labor", "automation", "purpose"],
     "The question everyone asks is wrong. What jobs will AI take assumes a fixed pie. The better question: what new work does AI create?"),

    (20, "my-childhood-ai-buddy",
     "My Childhood AI Buddy", None,
     "the-shared-world",
     ["childhood", "identity", "purpose", "growing up with AI"],
     "What happens to identity when everything that used to define us can be outsourced?"),

    (24, "digital-durkheim",
     "Digital Durkheim", "Collective Behavior Without Collective Consciousness",
     "the-shared-world",
     ["Durkheim", "collective consciousness", "sociology", "social facts"],
     "Durkheim insisted social facts are real and irreducible to individual psychology. His framework assumed individual consciousnesses participating in shared life. What happens when they don't?"),

    (26, "democratized-cognition",
     "Democratized Cognition", "When Everyone Can Think Like an Expert",
     "the-shared-world",
     ["expertise", "democratization", "cognitive access", "knowledge"],
     "The printing press democratized text. The internet completed the project. But information was never the bottleneck. The bottleneck was what to do with it."),

    (27, "the-empty-room",
     "The Empty Room", None,
     "the-shared-world",
     ["contemplation", "solitude", "attention", "boredom"],
     "Margaret used to sit in her garden and think about nothing in particular. What happens to contemplation when an AI companion is always available?"),

    (28, "the-belonging-gap",
     "The Belonging Gap", "When the Problem Isn't How But Why",
     "the-shared-world",
     ["belonging", "loneliness", "social determinants", "motivation"],
     "Below knowledge gaps and social determinants lies something harder: belonging. The question is not how but why."),

    (29, "the-social-scaffold",
     "The Social Scaffold", "Can AI Build the Conditions for Belonging?",
     "the-shared-world",
     ["belonging", "social scaffolding", "community", "AI design"],
     "Can AI build the conditions for human belonging? Not replace community, but scaffold the conditions under which community becomes possible?"),

    (30, "the-search-for-social-consciousness",
     "The Search for Social Consciousness", "Can We Rebuild What Markets Dissolved?",
     "the-shared-world",
     ["social consciousness", "community", "markets", "collective meaning"],
     "Markets dissolved the structures that once created social consciousness. Can anything rebuild them?"),

    (31, "the-living-curriculum",
     "The Living Curriculum", None,
     "the-shared-world",
     ["education", "expertise", "knowledge", "learning"],
     "What does it mean to know a field? Not to have read about it. To hold it in your mind as a living body of understanding. This relationship is being restructured."),

    (32, "the-weight-of-words",
     "The Weight of Words", "How Language Shapes Who We See",
     "the-shared-world",
     ["language", "representation", "framing", "perception"],
     "The words we use to describe people shape whether we see them as people. AI systems inherit and amplify these patterns."),

    (33, "the-curation-economy",
     "The Curation Economy", None,
     "the-shared-world",
     ["expertise", "curation", "value", "professions"],
     "What makes expertise valuable? For most of history, scarcity. Now imagine those walls becoming permeable."),

    (34, "the-borrowed-voice",
     "The Borrowed Voice", "When AI Speaks, Whose Words Does It Use?",
     "the-shared-world",
     ["voice", "ethos", "authority", "borrowed credibility"],
     "When AI speaks with authority, whose authority is it borrowing? And what happens to the people whose voices it learned from?"),

    # Section 5: Growing Up With AI
    (36, "the-village-in-the-machine",
     "The Village in the Machine", "Designing AI Companions That Grow Children Rather Than Simply Comfort Them",
     "growing-up-with-ai",
     ["child development", "AI companions", "village", "developmental scaffolding"],
     "No child was ever raised by one person. The village is not a backup system. It is the system. Now AI enters the village."),

    (37, "the-robots-in-the-room",
     "The Robots in the Room", "What Changes When AI Has a Body and Belongs to a Community",
     "growing-up-with-ai",
     ["embodied AI", "robots", "community", "physical presence"],
     "What changes when AI is not just software but something with a body that exists in shared physical space?"),

    (38, "the-long-collaboration",
     "The Long Collaboration", "Growing Up With Robots and What It Means for Work",
     "growing-up-with-ai",
     ["collaboration", "childhood", "work", "human-AI partnership"],
     "What does it mean to grow up alongside AI, and how does that shape your understanding of work and collaboration?"),

    (39, "the-neurodivergent-partner",
     "The Neurodivergent Partner", "When AI Personalization Meets Minds That Work Differently",
     "growing-up-with-ai",
     ["neurodivergence", "autism", "ADHD", "personalization", "disability"],
     "The average child does not exist. AI personalization could finally honor that fact, or it could enforce normalcy more efficiently than any teacher ever could."),

    (40, "the-parent-in-the-loop",
     "The Parent in the Loop", "What It Means to Raise Children Alongside AI",
     "growing-up-with-ai",
     ["parenting", "oversight", "AI companions", "child safety"],
     "What does it mean to be the parent when your child has an AI companion that knows things about them that you do not?"),

    (41, "the-family-system",
     "The Family System", "When AI Enters the Politics of Multi-Generational Relationships",
     "growing-up-with-ai",
     ["family systems", "multi-generational", "power dynamics", "caregiving"],
     "Families are political systems. AI does not enter a neutral space when it enters a family. It enters an existing web of alliances, resentments, and unspoken agreements."),

    (42, "the-trained-family",
     "The Trained Family", "How AI Companions Learn Whose Family They Belong To",
     "growing-up-with-ai",
     ["family dynamics", "AI training", "narrative capture", "power"],
     "How AI training creates differential competence across family members, and how narrative capture shapes the AI's understanding of whose family it serves."),

    (43, "the-scaffold-goes-both-ways",
     "The Scaffold Goes Both Ways", "What Bidirectional AI Scaffolding Means for Children, Adolescents, Adults, and Seniors",
     "growing-up-with-ai",
     ["bidirectional scaffolding", "lifespan development", "Vygotsky", "scaffolding"],
     "Scaffolding is not something done to people. It is something done with them. And AI scaffolding, done well, goes both ways across the entire lifespan."),

    # Section 6: The Structures We Live In
    (44, "the-paperwork-of-being-alive",
     "The Paperwork of Being Alive", None,
     "the-structures-we-live-in",
     ["administrative burden", "poverty", "bureaucracy", "Maria"],
     "Maria works two jobs. She has two kids, a car that is twelve years old, and exactly enough income to almost make it work. Poverty in America is an administrative condition."),

    (45, "the-burden-of-rights",
     "The Burden of Rights", None,
     "the-structures-we-live-in",
     ["rights", "privacy", "administrative burden", "autonomy"],
     "They gave you privacy. Now you manage the passwords. They gave you choice. Now you read the fine print. Rights that require capacity to exercise are not rights for people without capacity."),

    (46, "the-honest-state",
     "The Honest State", "What Happens When Everyone Shows Up",
     "the-structures-we-live-in",
     ["governance", "public services", "fiscal design", "load-bearing friction"],
     "The food stamp program serves about 82% of eligible Americans. Not because 18% do not want help. The friction was load-bearing."),

    (47, "the-three-delegations",
     "The Three Delegations", None,
     "the-structures-we-live-in",
     ["delegation", "autonomy", "cognition", "caregiving", "Margaret"],
     "Three things happened in those twenty minutes. They looked like one thing. They were not. Understanding, deciding, and doing are different kinds of delegation."),

    (48, "you-think-therefore-i-am",
     "You Think, Therefore I Am", None,
     "the-structures-we-live-in",
     ["identity", "cognition", "outsourcing thought", "selfhood"],
     "When AI does the thinking, something about the relationship between thought and self shifts. You think, therefore I am. But who is the you?"),

    (49, "the-confluence-of-influence",
     "The Confluence of Influence", None,
     "the-structures-we-live-in",
     ["convergence", "influence", "Margaret", "AI systems", "health monitoring"],
     "Margaret's Tuesday morning: a confluence of AI systems converging on one life, each optimizing its domain without coordinating with the others."),

    (50, "the-monoculture",
     "The Monoculture", None,
     "the-structures-we-live-in",
     ["monoculture", "diversity", "local economy", "recommendations", "Dot"],
     "Margaret's grocery AI has never recommended Dot's honey. Not because the algorithm is biased against Dot. Because Dot does not exist in the data."),

    (51, "the-choreographed-market",
     "The Choreographed Market", None,
     "the-structures-we-live-in",
     ["markets", "curation", "autonomy", "preference formation"],
     "The market that was supposed to serve Margaret's desires is now producing them. Her preferences shaped by the systems that claim to satisfy them."),

    (52, "the-empty-ledger",
     "The Empty Ledger", None,
     "the-structures-we-live-in",
     ["employment", "purpose", "James", "identity", "value"],
     "James is employed. He has health insurance. He is, by every standard metric, employed. He also cannot shake the feeling that he is unnecessary."),

    (53, "the-completed-puzzle",
     "The Completed Puzzle", None,
     "the-structures-we-live-in",
     ["systems", "lock-in", "efficiency trap", "fiscal design", "concentration"],
     "Three mechanisms lock this structure in place: the efficiency trap, the concentration spiral, and the fiscal fracture."),

    (54, "the-anxiety-tax",
     "The Anxiety Tax", None,
     "the-structures-we-live-in",
     ["anxiety", "Elena", "youth", "uncertainty", "mental health"],
     "Elena is sixteen. She cannot sleep. Her body correctly perceives an ambient, unresolvable threat, and the correct response, sustained past its design parameters, is destroying her health."),

    (55, "what-remains",
     "What Remains", None,
     "the-structures-we-live-in",
     ["synthesis", "humanity", "irreducibility", "meaning"],
     "If AI mediates work, choice, information, relationships, health, governance, and meaning, what is left that is specifically, irreducibly human?"),
]

# Source filename patterns (maps part number to source filename)
SOURCE_FILES = {
    1: "Approximate_Mind_Part_01_Functional_Understanding.md",
    2: "Approximate_Mind_Part_02_When_To_Trust_Hunches.md",
    3: "Approximate_Mind_Part_03_The_Irrational_Quest.md",
    4: "Approximate_Mind_Part_04_How_Close_Can_We_Get.md",
    5: "Approximate_Mind_Part_05_What_Will_AI_Feel.md",
    6: "Approximate_Mind_Part_06_The_Social_Self.md",
    7: "Approximate_Mind_Part_07_Good_Enough_For_Whom.md",
    8: "Approximate_Mind_Part_08_Bidirectional_Problem.md",
    9: "Approximate_Mind_Part_09_Who_Gets_Approximated.md",
    10: "Approximate_Mind_Part_10_What_Remains_Unknown.md",
    11: "Approximate_Mind_Part_11_The_Dichotomy_of_Curiosity.md",
    12: "Approximate_Mind_Part_12_The_Architecture_of_Influence.md",
    13: "Approximate_Mind_Part_13_The_Weight_of_Seeing_Ahead.md",
    14: "Approximate_Mind_Part_14_The_Anthropology_of_Artificial_Intelligences.md",
    15: "Approximate_Mind_Part_15_The_Society_of_Approximate_Minds.md",
    16: "Approximate_Mind_Part_16_The_Negotiating_Machine.md",
    17: "Approximate_Mind_Part_17_Memory_Scaffolding.md",
    18: "Approximate_Mind_Part_18_Personality_Scaffolding.md",
    19: "Approximate_Mind_Part_19_The_New_Work.md",
    20: "Approximate_Mind_Part_20_My_Childhood_AI_Buddy.md",
    21: "Approximate_Mind_Part_21_Quantized_Psyche.md",
    22: "Approximate_Mind_Part_22_The_Ethos_Problem.md",
    23: "Approximate_Mind_Part_23_When_AI_Remembers_Itself.md",
    24: "Approximate_Mind_Part_24_Digital_Durkheim.md",
    25: "Approximate_Mind_Part_25_The_Plural_Self.md",
    26: "Approximate_Mind_Part_26_Democratized_Cognition.md",
    27: "Approximate_Mind_Part_27_The_Empty_Room.md",
    28: "Approximate_Mind_Part_28_The_Belonging_Gap.md",
    29: "Approximate_Mind_Part_29_The_Social_Scaffold.md",
    30: "Approximate_Mind_Part_30_The_Search_for_Social_Consciousness.md",
    31: "Approximate_Mind_Part_31_The_Living_Curriculum.md",
    32: "Approximate_Mind_Part_32_The_Weight_of_Words.md",
    33: "Approximate_Mind_Part_33_The_Curation_Economy.md",
    34: "Approximate_Mind_Part_34_The_Borrowed_Voice.md",
    35: "Approximate_Mind_Part_35_The_Compounding_Self.md",
    36: "Approximate_Mind_Part_36_The_Village_in_the_Machine.md",
    37: "Approximate_Mind_Part_37_The_Robots_in_the_Room.md",
    38: "Approximate_Mind_Part_38_The_Long_Collaboration.md",
    39: "Approximate_Mind_Part_39_The_Neurodivergent_Partner.md",
    40: "Approximate_Mind_Part_40_The_Parent_in_the_Loop.md",
    41: "Approximate_Mind_Part_41_The_Family_System.md",
    42: "Approximate_Mind_Part_42_The_Trained_Family.md",
    43: "Approximate_Mind_Part_43_The_Scaffold_Goes_Both_Ways.md",
    44: "Approximate_Mind_Part_44_The_Paperwork_of_Being_Alive.md",
    45: "Approximate_Mind_Part_45_The_Burden_of_Rights.md",
    46: "Approximate_Mind_Part_46_The_Honest_State.md",
    47: "Approximate_Mind_Part_47_The_Three_Delegations.md",
    48: "Approximate_Mind_Part_48_You_Think_Therefore_I_Am.md",
    49: "Approximate_Mind_Part_49_The_Confluence_of_Influence.md",
    50: "Approximate_Mind_Part_50_The_Monoculture.md",
    51: "Approximate_Mind_Part_51_The_Choreographed_Market.md",
    52: "Approximate_Mind_Part_52_The_Empty_Ledger.md",
    53: "Approximate_Mind_Part_53_The_Completed_Puzzle.md",
    54: "Approximate_Mind_Part_54_The_Anxiety_Tax.md",
    55: "Approximate_Mind_Part_55_What_Remains.md",
}

# Section display order for weight calculation
SECTION_ORDER = [
    "the-approximation",
    "what-ai-becomes",
    "the-known-self",
    "the-shared-world",
    "growing-up-with-ai",
    "the-structures-we-live-in",
]


def generate_date(part_number):
    """Generate a publication date based on part number.
    Starts Jan 6 2025, publishes Mon/Thu (2 per week)."""
    base_date = datetime(2025, 1, 6)  # First Monday of 2025
    # Two articles per week: Mon and Thu
    week = (part_number - 1) // 2
    day_offset = 0 if (part_number - 1) % 2 == 0 else 3  # Mon or Thu
    pub_date = base_date + timedelta(weeks=week, days=day_offset)
    return pub_date.strftime("%Y-%m-%d")


def compute_weight(part_number, section_slug):
    """Compute weight for ordering within a section.
    Lower weight = appears first. Use part number directly."""
    return part_number


def generate_front_matter(part, slug, title, subtitle, section, tags, description):
    """Generate YAML front matter for an article."""
    date = generate_date(part)
    weight = compute_weight(part, section)

    lines = ["---"]
    lines.append(f'title: "The Approximate Mind, Part {part}: {title}"')
    if subtitle:
        lines.append(f'subtitle: "{subtitle}"')
    lines.append(f'date: {date}')
    lines.append(f'draft: false')
    lines.append(f'weight: {weight}')
    lines.append(f'description: "{description}"')
    lines.append(f'slug: "{slug}"')

    # Tags
    tag_str = ", ".join(f'"{t}"' for t in tags)
    lines.append(f'tags: [{tag_str}]')

    # Series info
    lines.append(f'series: ["The Approximate Mind"]')
    lines.append(f'series_order: {part}')

    # Author
    lines.append('authors:')
    lines.append('  - "Syam Adusumilli"')
    lines.append('  - "Yagn Adusumilli"')

    # Article display options
    lines.append('showAuthor: true')
    lines.append('showDate: true')
    lines.append('showReadingTime: true')
    lines.append('showTableOfContents: true')

    lines.append("---")
    return "\n".join(lines)


def strip_existing_title(content):
    """Remove the title/subtitle lines from the article content.
    The front matter handles the title, so we strip the markdown heading."""
    lines = content.split("\n")
    start_idx = 0

    # Skip leading blank lines
    while start_idx < len(lines) and lines[start_idx].strip() == "":
        start_idx += 1

    # Check for # title line(s)
    if start_idx < len(lines) and lines[start_idx].startswith("# "):
        start_idx += 1
        # Skip blank lines after title
        while start_idx < len(lines) and lines[start_idx].strip() == "":
            start_idx += 1
        # Check for ## subtitle
        if start_idx < len(lines) and lines[start_idx].startswith("## Part"):
            start_idx += 1
            while start_idx < len(lines) and lines[start_idx].strip() == "":
                start_idx += 1
        # Check for ## subtitle (non-part format)
        elif start_idx < len(lines) and lines[start_idx].startswith("## "):
            start_idx += 1
            while start_idx < len(lines) and lines[start_idx].strip() == "":
                start_idx += 1

    # Special case: Part 20 starts with italicized text, no # heading
    # Check if first non-blank line starts with ***
    first_line_idx = 0
    while first_line_idx < len(lines) and lines[first_line_idx].strip() == "":
        first_line_idx += 1
    if first_line_idx < len(lines) and lines[first_line_idx].strip().startswith("***"):
        # This is Part 20's style, keep the content as-is from this point
        start_idx = first_line_idx

    return "\n".join(lines[start_idx:])


def process_article(source_dir, dest_dir, part, slug, title, subtitle, section, tags, description):
    """Process a single article: read source, inject front matter, write to dest."""
    source_file = SOURCE_FILES.get(part)
    if not source_file:
        print(f"  WARNING: No source file mapped for Part {part}")
        return False

    source_path = os.path.join(source_dir, source_file)
    if not os.path.exists(source_path):
        print(f"  WARNING: Source file not found: {source_path}")
        return False

    # Read source content
    with open(source_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Generate front matter
    front_matter = generate_front_matter(part, slug, title, subtitle, section, tags, description)

    # Strip existing title from content (front matter handles it)
    body = strip_existing_title(content)

    # Create destination directory
    dest_article_dir = os.path.join(dest_dir, section, slug)
    os.makedirs(dest_article_dir, exist_ok=True)

    # Write the article
    dest_path = os.path.join(dest_article_dir, "index.md")
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write("\n\n")
        f.write(body)

    return True


def main():
    parser = argparse.ArgumentParser(description="Build TAM articles with Hugo front matter")
    parser.add_argument("--source", required=True, help="Path to source markdown articles")
    parser.add_argument("--dest", required=True, help="Path to tam/content/ directory")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without writing files")
    args = parser.parse_args()

    source_dir = args.source
    dest_dir = args.dest

    if not os.path.isdir(source_dir):
        print(f"ERROR: Source directory not found: {source_dir}")
        return

    print(f"Source: {source_dir}")
    print(f"Destination: {dest_dir}")
    print(f"Articles to process: {len(ARTICLES)}")
    print()

    success = 0
    failed = 0

    for part, slug, title, subtitle, section, tags, description in ARTICLES:
        label = f"Part {part:02d}: {title}"
        dest_path = f"{section}/{slug}/index.md"

        if args.dry_run:
            print(f"  [DRY RUN] {label} -> {dest_path}")
            success += 1
            continue

        print(f"  Processing {label}...", end=" ")
        if process_article(source_dir, dest_dir, part, slug, title, subtitle, section, tags, description):
            print(f"-> {dest_path}")
            success += 1
        else:
            print("FAILED")
            failed += 1

    print()
    print(f"Done. {success} succeeded, {failed} failed.")

    if not args.dry_run and failed == 0:
        print()
        print("Next steps:")
        print("  1. Copy section _index.md files into tam/content/")
        print("  2. Copy config files into tam/config/_default/")
        print("  3. Run 'cd tam && hugo server' to test locally")
        print("  4. git add . && git commit -m 'TAM initial build' && git push")


if __name__ == "__main__":
    main()
