#!/usr/bin/env python3
"""Prioritize CultureMech media records for Edison deep-research.

Goal: surface records where deep-research is most likely to yield
**confident strain-level taxon-medium associations**, with usable
recipe diffs against the parent record (so the parent-child
MediaVariant hierarchy can be applied when the publication's recipe
differs).

Scoring rubric (all components additive; final score in [0, 110]):

  1. Recipe completeness (0-35)
       - 0 ingredients .................................. 0   (skipped entirely)
       - 1-3 ingredients ................................ 5
       - 4-9 ingredients ................................ 15
       - 10-25 ingredients .............................. 30
       - 26+ ingredients ................................ 25
       +5 if >= 80% of ingredients carry a concentration

  2. Source recognizability (0-25)  -- papers cite these
       - DSMZ Medium (media_term id starts with DSM:) ... 25
       - ATCC Medium (atcc.medium / ATCC) ............... 22
       - JCM Medium ..................................... 20
       - NBRC / NCIMB / IAM / CIP / LMG / CCAP / NCMA ... 18
       - TOGO Medium .................................... 18
       - MediaDive native id (mediadive.medium) ......... 18
       - Any other media_term ........................... 10
       - Filename / original_name carries strain marker . 12 (fallback if no media_term)
       - Generic / auto-generated name .................. 0-5

  3. Organism-association gap (0-20)
       - 0 target_organisms ............................. 20
       - 1-2 organisms, none with NCBITaxon ............. 17
       - 1-2 organisms, with NCBITaxon .................. 12
       - 3-10 organisms ................................. 6
       - 11+ organisms .................................. 2
     (Bogus "organisms" that equal the medium name count as 0.)

  4. Discoverability hints (0-15)
       +3 has description >= 30 chars
       +3 has applications list
       +3 has notes with a URL
       +3 has original_name distinct from auto-slug
       +3 has synonyms

  5. Strain / culture-collection markers in name (0-10)
       +10 if name or original_name matches one of
            DSM, ATCC, JCM, NBRC, NCIMB, IAM, CIP, LMG, CCAP, NCMA
            followed by digits
       +5  if name contains a plausible binomial species name

  6. Category multiplier (literature volume bias)
       bacterial=1.00  archaea=0.95  fungal=0.90  algae=0.85
       specialized=0.85  solutions=excluded entirely

Hard filters (record is dropped before scoring):

  - 0 ingredients
  - stock-solution records (no organism associations expected — see below)
  - already-researched: the slug appears in the TRACKED manifest
    data/import_tracking/researched_media.json

Solution filter (#124): this used to be documented as "category == solutions",
which never fired — `CategoryEnum` has no `solutions` member, so no record can
carry that value. The ~4,784 MediaDive stock-solution records live in
`bacterial/` stamped `category: bacterial`, and 4,772 of them were being scored
and ranked as candidate media (31% of the committed report). They are now
detected structurally via `record_kinds.is_solution_record`, the same rule
`validate_strict.py` uses to route them to `SolutionRecipe`.

Reproducibility (#121): the already-researched filter reads that tracked
manifest, never the gitignored `research/media/` tree. Scanning the latter made
the committed reports a function of whoever last ran the script — regenerating
on another machine reordered the entire top-10, producing a diff that could not
be told apart from a real data change. The outputs here are now a pure function
of tracked inputs: the corpus plus the manifest. Refresh the manifest explicitly
with `just refresh-researched-manifest` and commit that diff separately.

Outputs:

  data/import_tracking/reports/deep_research_priority.json
      Full ranked list (one entry per surviving record).
      Compatible with `research-media-edison-batch` — each entry
      carries `recipe_name` + `file_path` like the existing
      edison_batch.json.

  data/import_tracking/reports/deep_research_priority.md
      Human-readable top-100 table with score breakdowns.

  data/import_tracking/reports/deep_research_priority_top100.json
      First 100 entries from the JSON list, for direct use with:
          just research-media-edison-batch \\
              data/import_tracking/reports/deep_research_priority_top100.json \\
              --limit 10

Usage::

    python scripts/prioritize_deep_research_candidates.py
    # or
    just prioritize-deep-research-candidates
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

try:
    from yaml import CSafeLoader as _Loader  # type: ignore[attr-defined]
except ImportError:
    _Loader = yaml.SafeLoader  # type: ignore[misc, assignment]

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import researched_manifest as rmf  # noqa: E402  -- tracked already-researched set
from record_kinds import is_solution_record  # noqa: E402  -- shared medium/solution rule

NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
REPORTS_DIR = REPO_ROOT / "data" / "import_tracking" / "reports"

# Categories that may contain real microbial culture media
CANDIDATE_CATEGORIES = ("bacterial", "archaea", "algae", "fungal", "specialized")

CATEGORY_MULT = {
    "bacterial": 1.00,
    "archaea": 0.95,
    "fungal": 0.90,
    "algae": 0.85,
    "specialized": 0.85,
}

CULTURE_COLLECTION_RE = re.compile(
    r"\b(DSM|ATCC|JCM|NBRC|NCIMB|IAM|CIP|LMG|CCAP|NCMA)[\s\-]?(\d{2,})", re.IGNORECASE
)

# Loose binomial heuristic: Capitalized + space + lowercase word, length >= 3 each.
BINOMIAL_RE = re.compile(r"\b([A-Z][a-z]{2,})\s+([a-z]{3,})\b")

URL_RE = re.compile(r"https?://[^\s)]+")


def load_yaml(path: Path) -> dict[str, Any] | None:
    """Robust YAML load; returns None on parse failure."""
    try:
        with path.open("r", encoding="utf-8") as f:
            doc = yaml.load(f, Loader=_Loader)
        return doc if isinstance(doc, dict) else None
    except (yaml.YAMLError, OSError):
        return None


def has_existing_research(slug: str, researched: set[str] | None = None) -> bool:
    """True iff `slug` has a completed run, per the TRACKED manifest.

    Reads `data/import_tracking/researched_media.json`, never `research/media/`.
    That directory is gitignored, so scanning it made the generated reports a
    function of whoever last ran the script — regenerating elsewhere reordered
    the whole top-10 (#121). Refresh the manifest explicitly with
    `just refresh-researched-manifest` and commit the diff.

    Pass `researched` to avoid re-reading the manifest per record.
    """
    if researched is None:
        researched = rmf.researched_slugs()
    return slug in researched


def score_ingredients(doc: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    """Component 1: recipe completeness."""
    ingredients = doc.get("ingredients") or []
    n = len(ingredients) if isinstance(ingredients, list) else 0
    if n == 0:
        return 0, {"count": 0}
    if n <= 3:
        base = 5
    elif n <= 9:
        base = 15
    elif n <= 25:
        base = 30
    else:
        base = 25
    with_conc = 0
    for ing in ingredients:
        if isinstance(ing, dict) and ing.get("concentration"):
            with_conc += 1
    bonus = 5 if n > 0 and with_conc / n >= 0.8 else 0
    return base + bonus, {"count": n, "with_concentration": with_conc, "bonus": bonus}


def _source_id_kind(media_term: dict[str, Any] | None) -> str:
    """Return a short source-kind tag for the media_term."""
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if isinstance(term, dict):
        tid = str(term.get("id") or "").lower()
    else:
        tid = ""
    pref = str(media_term.get("preferred_term") or "")
    blob = f"{tid} {pref}".lower()
    if "dsm:" in tid or re.search(r"\bdsm[\s\-]?\d", blob):
        return "DSMZ"
    if "atcc" in blob:
        return "ATCC"
    if "jcm" in blob:
        return "JCM"
    if "nbrc" in blob:
        return "NBRC"
    if "ncimb" in blob:
        return "NCIMB"
    if "ccap" in blob:
        return "CCAP"
    if "ncma" in blob:
        return "NCMA"
    if "togo:" in tid or "togo medium" in blob:
        return "TOGO"
    if "mediadive.medium" in tid:
        return "MediaDive"
    return "OTHER" if (tid or pref) else ""


def score_source(doc: dict[str, Any], file_path: Path) -> tuple[int, dict[str, Any]]:
    """Component 2: source recognizability."""
    media_term = doc.get("media_term")
    kind = _source_id_kind(media_term)
    scores = {
        "DSMZ": 25, "ATCC": 22, "JCM": 20,
        "NBRC": 18, "NCIMB": 18, "CCAP": 18, "NCMA": 18,
        "TOGO": 18, "MediaDive": 18, "OTHER": 10,
    }
    if kind:
        return scores[kind], {"kind": kind, "via": "media_term"}

    # Fallback: strain marker in filename / original_name
    name_blob = " ".join([
        str(doc.get("name") or ""),
        str(doc.get("original_name") or ""),
        file_path.stem,
    ])
    if CULTURE_COLLECTION_RE.search(name_blob):
        return 12, {"kind": "FILENAME_MARKER", "via": "name"}
    # generic
    return 5, {"kind": "GENERIC", "via": "fallback"}


def _organism_has_taxon(org: dict[str, Any]) -> bool:
    if not isinstance(org, dict):
        return False
    term = org.get("term") or {}
    if isinstance(term, dict) and term.get("id"):
        return True
    if org.get("gtdb_term"):
        return True
    if org.get("genome_assembly_id"):
        return True
    return False


def _organism_is_bogus(org: dict[str, Any], medium_name: str, original_name: str) -> bool:
    """Heuristic: the existing corpus has placeholder entries where the
    'organism' is actually the medium name. Treat these as missing data."""
    if not isinstance(org, dict):
        return True
    pref = str(org.get("preferred_term") or "").strip().lower()
    if not pref:
        return True
    haystack = {medium_name.lower(), original_name.lower(),
                medium_name.replace("_", " ").lower(),
                original_name.replace("_", " ").lower()}
    return pref in haystack


def score_organism_gap(doc: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    """Component 3: how much new info we'd gain by adding organisms."""
    orgs = doc.get("target_organisms") or []
    medium_name = str(doc.get("name") or "")
    original_name = str(doc.get("original_name") or "")
    real = [o for o in orgs
            if isinstance(o, dict)
            and not _organism_is_bogus(o, medium_name, original_name)]
    n = len(real)
    with_taxon = sum(1 for o in real if _organism_has_taxon(o))
    if n == 0:
        score = 20
    elif n <= 2 and with_taxon == 0:
        score = 17
    elif n <= 2:
        score = 12
    elif n <= 10:
        score = 6
    else:
        score = 2
    return score, {
        "raw_count": len(orgs),
        "real_count": n,
        "with_taxon": with_taxon,
    }


def score_discoverability(doc: dict[str, Any], file_path: Path) -> tuple[int, dict[str, Any]]:
    """Component 4: hints that the medium is findable in literature."""
    points = 0
    hits: list[str] = []
    desc = str(doc.get("description") or "")
    if len(desc) >= 30:
        points += 3
        hits.append("description")
    apps = doc.get("applications")
    if isinstance(apps, list) and apps:
        points += 3
        hits.append("applications")
    elif isinstance(apps, str) and apps.strip():
        points += 3
        hits.append("applications")
    notes = str(doc.get("notes") or "")
    if URL_RE.search(notes):
        points += 3
        hits.append("notes_url")
    orig = str(doc.get("original_name") or "")
    if orig and orig.lower() != file_path.stem.lower():
        points += 3
        hits.append("original_name")
    syns = doc.get("synonyms")
    if syns and isinstance(syns, (list, tuple)) and len(syns) > 0:
        points += 3
        hits.append("synonyms")
    return points, {"hits": hits}


def score_strain_markers(doc: dict[str, Any], file_path: Path) -> tuple[int, dict[str, Any]]:
    """Component 5: strain / culture-collection markers in the name."""
    blob = " ".join([
        str(doc.get("name") or ""),
        str(doc.get("original_name") or ""),
        file_path.stem,
    ])
    bonus = 0
    markers: list[str] = []
    cc = CULTURE_COLLECTION_RE.findall(blob)
    if cc:
        bonus += 10
        markers.append("culture_collection")
    if BINOMIAL_RE.search(blob):
        # Avoid double-counting words like "M2455 Methanosphaerula" which
        # also match the binomial pattern via "Methanosphaerula peat";
        # the bonus is small so accept some overlap.
        bonus += 5
        markers.append("binomial")
    return bonus, {"markers": markers}


def score_record(doc: dict[str, Any], file_path: Path) -> dict[str, Any] | None:
    """Compute a full score breakdown for one record, or None to drop it."""
    ing_score, ing_info = score_ingredients(doc)
    if ing_info["count"] == 0:
        return None

    src_score, src_info = score_source(doc, file_path)
    org_score, org_info = score_organism_gap(doc)
    disc_score, disc_info = score_discoverability(doc, file_path)
    strain_score, strain_info = score_strain_markers(doc, file_path)

    category = (str(doc.get("category") or "").lower()
                or file_path.parent.name.lower())
    mult = CATEGORY_MULT.get(category, 0.85)

    subtotal = ing_score + src_score + org_score + disc_score + strain_score
    final = round(subtotal * mult, 2)

    return {
        "score": final,
        "subtotal": subtotal,
        "category_multiplier": mult,
        "category": category,
        "breakdown": {
            "ingredients": {"score": ing_score, **ing_info},
            "source": {"score": src_score, **src_info},
            "organism_gap": {"score": org_score, **org_info},
            "discoverability": {"score": disc_score, **disc_info},
            "strain_markers": {"score": strain_score, **strain_info},
        },
    }


def expected_yield(breakdown: dict[str, Any]) -> str:
    """Short verdict for the markdown report."""
    org_gap = breakdown["organism_gap"]["real_count"]
    src_kind = breakdown["source"].get("kind", "GENERIC")
    n_ing = breakdown["ingredients"]["count"]
    markers = breakdown["strain_markers"]["markers"]

    bits = []
    if org_gap == 0:
        bits.append("net-new organism set")
    elif org_gap < 3:
        bits.append("expand thin organism set")
    if src_kind in {"DSMZ", "ATCC", "JCM", "TOGO", "MediaDive"}:
        bits.append(f"{src_kind}-anchored citations")
    elif "culture_collection" in markers:
        bits.append("strain marker in name")
    if n_ing >= 10:
        bits.append("recipe diff feasible")
    return "; ".join(bits) or "low yield"


def collect_records(researched: set[str] | None = None) -> list[dict[str, Any]]:
    """Walk the corpus and score every candidate record.

    `researched` is the tracked already-researched slug set (empty set = exclude
    nothing). Resolved once by the caller so the output depends only on inputs
    passed in — not on whatever happens to be in the local `research/` dir.
    """
    if researched is None:
        researched = rmf.researched_slugs()
    out: list[dict[str, Any]] = []
    for cat in CANDIDATE_CATEGORIES:
        cat_dir = NORMALIZED_DIR / cat
        if not cat_dir.is_dir():
            continue
        for yaml_path in sorted(cat_dir.glob("*.yaml")):
            doc = load_yaml(yaml_path)
            if not doc:
                continue
            # Stock solutions have no organism to associate by construction, so
            # researching one can only ever spend credits for nothing. They sit
            # in bacterial/ stamped `category: bacterial`, so this has to be a
            # structural check — see the module docstring (#124).
            if is_solution_record(doc):
                continue
            slug = yaml_path.stem
            if slug in researched:
                continue
            scored = score_record(doc, yaml_path)
            if not scored:
                continue
            file_path_rel = yaml_path.relative_to(NORMALIZED_DIR).as_posix()
            media_term = doc.get("media_term") or {}
            media_term_label = ""
            if isinstance(media_term, dict):
                pref = str(media_term.get("preferred_term") or "")
                term = media_term.get("term") or {}
                tid = str(term.get("id") if isinstance(term, dict) else "") or ""
                if pref and tid:
                    media_term_label = f"{pref} ({tid})"
                else:
                    media_term_label = pref or tid
            entry = {
                "recipe_name": str(doc.get("name") or slug),
                "file_path": file_path_rel,
                "id": str(doc.get("id") or ""),
                "name": str(doc.get("name") or slug),
                "original_name": str(doc.get("original_name") or ""),
                "category": scored["category"],
                "media_term": media_term_label,
                "score": scored["score"],
                "subtotal": scored["subtotal"],
                "category_multiplier": scored["category_multiplier"],
                "ingredient_count": scored["breakdown"]["ingredients"]["count"],
                "real_organism_count": scored["breakdown"]["organism_gap"]["real_count"],
                "expected_research_yield": expected_yield(scored["breakdown"]),
                "score_breakdown": scored["breakdown"],
            }
            out.append(entry)
    out.sort(key=lambda e: e["score"], reverse=True)
    return out


def write_markdown(entries: list[dict[str, Any]], path: Path, top_n: int = 100) -> None:
    lines: list[str] = []
    lines.append("# Deep-Research Priority List")
    lines.append("")
    lines.append("Generated by `scripts/prioritize_deep_research_candidates.py`.")
    lines.append("")
    lines.append(
        f"Ranked candidates for the `deep-research-medium` skill, optimized for "
        f"finding **confident strain-level taxon-medium associations** with "
        f"recipe diffs against the parent record."
    )
    lines.append("")
    lines.append(f"- Total scored candidates: **{len(entries)}**")
    lines.append(f"- Top-N shown below: **{min(top_n, len(entries))}**")
    lines.append("")
    lines.append("## Scoring rubric (max 110, before category multiplier)")
    lines.append("")
    lines.append(
        "1. **Recipe completeness** (0-35) — ingredient count + concentration coverage. "
        "Records with 10-25 well-quantified ingredients score highest; "
        "needed to diff against a publication's reported formulation."
    )
    lines.append(
        "2. **Source recognizability** (0-25) — DSMZ, ATCC, JCM, TOGO, "
        "MediaDive identifiers earn points because papers cite these."
    )
    lines.append(
        "3. **Organism-association gap** (0-20) — records with no real "
        "`target_organisms` have the largest information gain."
    )
    lines.append(
        "4. **Discoverability hints** (0-15) — description, applications, "
        "synonyms, source URL, distinct original_name."
    )
    lines.append(
        "5. **Strain markers in name** (0-10) — DSM/ATCC/JCM/NBRC/etc. "
        "numbers, or a binomial species name."
    )
    lines.append(
        "6. **Category multiplier** — bacterial 1.00, archaea 0.95, fungal 0.90, "
        "algae/specialized 0.85. Solutions are excluded."
    )
    lines.append("")
    lines.append(
        "Records with an existing non-dry-run Edison meta yaml are filtered "
        "out before scoring (no double-billing)."
    )
    lines.append("")
    lines.append(f"## Top {min(top_n, len(entries))} candidates")
    lines.append("")
    lines.append(
        "| # | Score | Category | Recipe | Ingredients | Orgs | Source ID | Expected yield |"
    )
    lines.append("|--:|------:|----------|--------|------------:|-----:|-----------|----------------|")
    for i, e in enumerate(entries[:top_n], start=1):
        name = e["recipe_name"]
        if len(name) > 50:
            name = name[:47] + "..."
        src_kind = e["score_breakdown"]["source"].get("kind", "")
        lines.append(
            f"| {i} | {e['score']:.1f} | {e['category']} | "
            f"`{name}` ([yaml](../../data/normalized_yaml/{e['file_path']})) | "
            f"{e['ingredient_count']} | {e['real_organism_count']} | "
            f"{src_kind} | {e['expected_research_yield']} |"
        )
    lines.append("")
    lines.append("## How to use this list")
    lines.append("")
    lines.append("```bash")
    lines.append("# Dry-run the top 5 to audit the phase-1 prompts:")
    lines.append("just research-media-edison-batch \\")
    lines.append("    data/import_tracking/reports/deep_research_priority_top100.json \\")
    lines.append("    --limit 5 --dry-run")
    lines.append("")
    lines.append("# Live phase-1 on the top 5:")
    lines.append("just research-media-edison-batch \\")
    lines.append("    data/import_tracking/reports/deep_research_priority_top100.json \\")
    lines.append("    --limit 5")
    lines.append("")
    lines.append("# Then for each result, invoke the deep-research-medium skill,")
    lines.append("# which runs the phase-2 per-organism follow-up.")
    lines.append("```")
    lines.append("")
    path.write_text("\n".join(lines))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--top", type=int, default=100,
                    help="How many entries to include in the markdown report and *_top100.json. Default 100.")
    ap.add_argument("--reports-dir", type=Path, default=REPORTS_DIR)
    ap.add_argument("--researched-manifest", type=Path, default=rmf.DEFAULT_MANIFEST,
                    help="Tracked manifest of already-researched slugs to exclude. "
                         "Refresh it with `just refresh-researched-manifest`.")
    ap.add_argument("--no-exclude-researched", action="store_true",
                    help="Score every record, including already-researched ones.")
    args = ap.parse_args(argv)

    researched: set[str] = set()
    if not args.no_exclude_researched:
        researched = rmf.researched_slugs(args.researched_manifest)
        if not researched:
            print(f"Note: no entries in {args.researched_manifest}; excluding nothing. "
                  f"Run `just refresh-researched-manifest` if local runs exist.",
                  flush=True)

    print(f"Scanning {NORMALIZED_DIR.relative_to(REPO_ROOT)}/ ...", flush=True)
    print(f"Excluding {len(researched)} already-researched record(s) "
          f"(source: tracked manifest, not research/).", flush=True)
    entries = collect_records(researched)
    print(f"Scored {len(entries)} candidate records.")

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.reports_dir / "deep_research_priority.json"
    top_json_path = args.reports_dir / "deep_research_priority_top100.json"
    md_path = args.reports_dir / "deep_research_priority.md"

    json_path.write_text(json.dumps(entries, indent=2))
    top_json_path.write_text(json.dumps(entries[: args.top], indent=2))
    write_markdown(entries, md_path, top_n=args.top)

    print(f"Wrote: {json_path.relative_to(REPO_ROOT)}  ({len(entries)} entries)")
    print(f"Wrote: {top_json_path.relative_to(REPO_ROOT)}  (top {min(args.top, len(entries))})")
    print(f"Wrote: {md_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
