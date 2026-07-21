#!/usr/bin/env python3
"""Prioritize MIM ingredients for Step 7b Edison role research.

Scans `MediaIngredientMech/data/ingredients/**/*.yaml` (cross-repo via
`--mim-repo`), scores each record by "how much do we gain by researching
the roles here?", and emits a batch JSON compatible with MIM's
`research_ingredient_edison.py --batch`.

Scoring rubric (higher = higher priority):

  base = (# facet slots empty) × log10(1 + total_occurrences)
       × (mapping_status == "MAPPED" ? 1.0 : 0.3)
       × (has_CHEBI_grounding ? 1.0 : 0.4)

  penalty for records that already ran Edison role research
  (existing `research/ingredients/roles/<slug>-edison-*-meta.yaml`)
  reduces score to 0.

Rationale:

  - **Facet gaps count** — every empty facet is an opportunity, weighted
    equally (3 empty vs 2 empty vs 1 empty).
  - **Occurrence matters most on log scale** — glucose (1638 occurrences)
    ranks higher than a rare ingredient (5 occurrences), but not 300×
    higher; log-scale keeps rare-but-empty ingredients on the map.
  - **UNMAPPED downgraded** — role research on an unmapped ingredient
    lands roles the ontology mapping can't tie back to; still worth
    doing but at 0.3× priority.
  - **Non-CHEBI grounding downgraded** — Edison's CHEBI-flavored
    role research is calibrated on CHEBI; FOODON/MICRO/UBERON groundings
    still ok (0.4× multiplier) but ranking-below-equal.

Companion of the existing `scripts/prioritize_deep_research_candidates.py`
which scores CultureMech MEDIA recipes (not MIM INGREDIENTS) with a
different rubric. Two scripts, two different corpora, one output format.

Usage:

    just prioritize-role-research-candidates
    # → data/import_tracking/reports/role_research_priority.json

    # Custom MIM location + smaller top-N:
    uv run python scripts/prioritize_role_research_candidates.py \\
        --mim-repo ../MediaIngredientMech --top 25 \\
        --out data/import_tracking/reports/role_research_priority_top25.json

    # Feed the output straight into MIM's Edison batch runner:
    (cd ../MediaIngredientMech && \\
     just research-ingredient-roles-edison-batch \\
       ../CultureMech/data/import_tracking/reports/role_research_priority.json \\
       --dry-run)
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_MIM_REPO = REPO_ROOT.parent / "MediaIngredientMech"
DEFAULT_OUTPUT = REPO_ROOT / "data" / "import_tracking" / "reports" / "role_research_priority.json"

FACET_SLOTS = ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles")


def _read_ingredient(path: Path) -> dict[str, Any] | None:
    try:
        doc = yaml.safe_load(path.read_text())
    except Exception:
        return None
    if not isinstance(doc, dict):
        return None
    return doc


def _score_record(doc: dict[str, Any]) -> tuple[float, dict[str, Any]]:
    """Return (score, breakdown_dict) for one ingredient record."""
    empty_facets = sum(1 for slot in FACET_SLOTS if not doc.get(slot))
    occurrences = int((doc.get("occurrence_statistics") or {}).get("total_occurrences") or 0)
    mapping_status = str(doc.get("mapping_status") or "").upper()
    identifier = doc.get("identifier") or ""
    ontology_id = (doc.get("ontology_mapping") or {}).get("ontology_id") or ""

    is_chebi = identifier.startswith("CHEBI:") or (isinstance(ontology_id, str) and ontology_id.startswith("CHEBI:"))
    is_mapped = mapping_status == "MAPPED"

    # log10(1 + n) — glucose (1638) → 3.21; a 5-occurrence ingredient → 0.78.
    occurrence_weight = math.log10(1 + occurrences) if occurrences > 0 else 0.0

    mapped_mult = 1.0 if is_mapped else 0.3
    chebi_mult = 1.0 if is_chebi else 0.4

    score = empty_facets * occurrence_weight * mapped_mult * chebi_mult

    breakdown = {
        "empty_facets": empty_facets,
        "total_occurrences": occurrences,
        "occurrence_weight": round(occurrence_weight, 3),
        "mapped_mult": mapped_mult,
        "chebi_mult": chebi_mult,
        "score": round(score, 3),
    }
    return score, breakdown


def _existing_roles_research(mim_repo: Path, slug: str) -> bool:
    """True if any Edison role-research meta yaml already exists for `slug`."""
    roles_dir = mim_repo / "research" / "ingredients" / "roles"
    if not roles_dir.is_dir():
        return False
    for path in roles_dir.glob(f"{slug}-edison-*-meta.yaml"):
        # Skip dry-run stubs; only real runs count as "already researched".
        try:
            meta = yaml.safe_load(path.read_text()) or {}
        except Exception:
            continue
        if str(meta.get("status", "")).lower() != "dry-run" and meta.get("task_id"):
            return True
    return False


def _record_to_batch_entry(path: Path, mim_repo: Path, doc: dict[str, Any], score: float, breakdown: dict[str, Any]) -> dict[str, Any]:
    """Shape one entry for MIM's `research_ingredient_edison.py --batch`."""
    slug = path.stem
    try:
        rel = path.relative_to(mim_repo)
    except ValueError:
        rel = path
    return {
        # research_ingredient_edison.py's load_batch_targets accepts either bare
        # slug strings or dicts with `target`/`slug`/`file_path`/`identifier`.
        "target": str(rel),  # relative-to-mim-repo path — passed as --target
        "slug": slug,
        "identifier": doc.get("identifier"),
        "preferred_term": doc.get("preferred_term"),
        "score": round(score, 3),
        "score_breakdown": breakdown,
    }


def collect_and_score(
    mim_repo: Path,
    include_already_researched: bool = False,
) -> list[dict[str, Any]]:
    """Walk MIM ingredients and return a ranked list of batch entries."""
    ingredients_root = mim_repo / "data" / "ingredients"
    if not ingredients_root.is_dir():
        raise SystemExit(f"MIM ingredients not found at {ingredients_root}. Pass --mim-repo.")

    entries: list[tuple[float, dict[str, Any]]] = []
    for path in sorted(ingredients_root.rglob("*.yaml")):
        doc = _read_ingredient(path)
        if doc is None:
            continue
        score, breakdown = _score_record(doc)
        if score <= 0:
            # Nothing to research: either all 3 facets full or no occurrences.
            continue
        if not include_already_researched and _existing_roles_research(mim_repo, path.stem):
            continue
        entry = _record_to_batch_entry(path, mim_repo, doc, score, breakdown)
        entries.append((score, entry))

    entries.sort(key=lambda t: t[0], reverse=True)
    return [entry for _, entry in entries]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mim-repo", type=Path, default=DEFAULT_MIM_REPO,
                        help="MediaIngredientMech checkout root (default: ../MediaIngredientMech).")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUTPUT,
                        help="Output JSON path.")
    parser.add_argument("--top", type=int, default=None,
                        help="Cap output to top-N candidates.")
    parser.add_argument("--include-already-researched", action="store_true",
                        help="Include ingredients that already have an Edison role-research meta yaml.")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    args.out.parent.mkdir(parents=True, exist_ok=True)

    entries = collect_and_score(args.mim_repo, include_already_researched=args.include_already_researched)
    if args.top is not None:
        entries = entries[: args.top]

    args.out.write_text(json.dumps(entries, indent=2))

    print(f"Scanned MIM ingredients under {args.mim_repo}/data/ingredients")
    print(f"Ranked {len(entries)} candidates → {args.out}")
    if entries:
        print()
        print("Top 5:")
        for e in entries[:5]:
            print(f"  score={e['score']:7.3f}  {e['identifier'] or '(no id)'} — {e['preferred_term']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
