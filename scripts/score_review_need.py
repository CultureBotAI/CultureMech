#!/usr/bin/env python3
"""Rank media records by how badly they need curation review.

This is the INVERSE of `prioritize_deep_research_candidates.py` and the two are
easy to confuse. That script ranks by expected research *yield* — it rewards
recipe completeness and source recognizability, and hard-filters records with
zero ingredients. It is asking "where will deep research pay off?".

This one asks "which records look broken?", so the records that scorer discards
are exactly the ones this scorer surfaces. Running only the yield ranking leaves
the damaged tail permanently invisible, which is how 362 zero-ingredient records
sat unexamined.

Signals, grouped by what a high score is claiming. Weights reflect severity —
whether the defect makes the record unusable, merely incomplete, or just
unidentifiable — and each was calibrated against its corpus frequency so a
signal firing on half the corpus cannot dominate one firing on 3%.

STRUCTURAL — the composition is absent or unusable:
  no ingredients or solutions  30   no structured composition
  placeholder component text   25   "not specified", "see source", etc.
  mangled component name       25   a whole recipe in one field (#166)
  only 1-2 components          15   suspiciously small composition unless curated

GROUNDING — present but not machine-usable:
  no component grounded        20
  under half grounded          10
  EXCEPT: curated opaque products that intentionally remain unmapped

IDENTITY / PROVENANCE — cannot be traced to a source:
  no media_term or sources     10
  name is a bare strain pointer 10   "For DSM 13514" names a strain
  no notes / provenance         5

CONDITIONS — incomplete rather than wrong:
  no pH and no temperature      5   deliberately low; it is the norm

Deliberately NOT scored here, because a dedicated audit already reports each and
duplicating the logic would let the two drift: implausible concentrations
(`audit-concentration-plausibility`), composition_type contradictions
(`audit-composition-type`), filename collisions (`audit-filename-collisions`).
Join on `file_path` to combine them; this scorer intentionally has no flag for
that, so there is one owner per signal.

Usage::

    just score-review-need                 # writes the ranked TSV
    just score-review-need --top 40        # and prints the worst 40
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "review_need_ranking.tsv"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

PLACEHOLDER = re.compile(
    r"see\s+source|refer\s+to|available\s+at|contact\s+source|not\s+specified|"
    r"\bunknown\b|composition\s+not\s+available|proprietary",
    re.I,
)
# Two or more embedded quantity+unit pairs means a composition block was flattened
# into one name field rather than parsed (#166).
#
# Deliberately NOT `\b` after the unit. These names are concatenated with the
# separators stripped — "0.85gNa2HPO4" puts a letter straight after the unit, so
# there is no word boundary and `\b` misses it. The real NBRC_1197 name matched
# the earlier pattern only because a "(" happened to follow one unit further
# along; a purely alphanumeric run would have slipped through. Requiring the unit
# to be followed by an uppercase letter, a bracket, whitespace or end-of-string
# keeps ordinary prose like "5 g of glucose" from matching.
_QTY_UNIT = r"\d+(?:\.\d+)?\s*(?:mg|ml|kg|g|l)(?=[A-Z(\[]|\s|$)"
MANGLED = re.compile(_QTY_UNIT + r".*?" + _QTY_UNIT)
# "For DSM 13514" identifies a strain, not a medium — the record has no name of
# its own. NOT the same as a short name: BG11 and JM are real media.
STRAIN_POINTER = re.compile(r"\s*(?:for\s+)?(?:dsm|atcc|jcm|nbrc|ncimb)\s*[\s:_-]*\d+\s*", re.I)
CONDITION_SLOTS = ("ph_value", "ph_range", "temperature_value", "temperature_range")
CURATED_STRAIN_POINTER_VARIANT_RELATIONSHIPS = frozenset(
    {
        "CONCENTRATION_VARIANT",
        "PHYSICAL_STATE_VARIANT",
        "SUPPLEMENTED_VARIANT",
        "OMITTED_COMPONENT_VARIANT",
        "SUBSTITUTED_COMPONENT_VARIANT",
        "PH_VARIANT",
        "SALINITY_VARIANT",
        "STRAIN_SPECIFIC_VARIANT",
    }
)

# Signals common enough to be the corpus norm rather than a defect. They refine the
# ranking among records that are ALREADY suspect, but must not qualify a record on
# their own — "no pH" fires on 51% of media, so emitting on it alone made the
# report 60% of the corpus and buried the 42 genuinely broken records (#177).
NORM_LEVEL_SIGNALS = frozenset({"no pH and no temperature"})


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Flatten the media-level composition for structural/grounding review.

    A stock solution is one component when referenced by name or identifier only.
    When its composition is inline, the ingredient entries are the more useful
    grounding surface and replace the wrapper for scoring purposes.
    """
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested_components = solution_components(solution)
        components.extend(nested_components or [solution])
    return components


def solution_components(solution: dict[str, Any]) -> list[dict[str, Any]]:
    components: list[dict[str, Any]] = []

    composition = solution.get("composition")
    legacy_ingredients = solution.get("ingredients")
    nested = composition or legacy_ingredients or []
    if isinstance(nested, list):
        components.extend(i for i in nested if isinstance(i, dict))

    child_solutions = solution.get("solutions") or []
    if isinstance(child_solutions, list):
        for child in child_solutions:
            if isinstance(child, dict):
                components.extend(solution_components(child) or [child])

    return components


def _curated_strain_pointer_variant(doc: dict[str, Any]) -> bool:
    data_quality_flags = doc.get("data_quality_flags") or []
    parent_media = doc.get("parent_media") or {}
    return (
        isinstance(data_quality_flags, list)
        and "ingredients_curated" in data_quality_flags
        and isinstance(parent_media, dict)
        and bool(parent_media.get("id") or parent_media.get("path"))
        and doc.get("variant_relationship") in CURATED_STRAIN_POINTER_VARIANT_RELATIONSHIPS
    )


def _curated_known_unmapped_components(
    doc: dict[str, Any],
    components: list[dict[str, Any]],
) -> bool:
    """Return whether ungrounded components are a deliberate curated endpoint.

    Official sources sometimes disclose only a commercial product, host-cell
    supernatant, or other opaque input. The curation endpoint for those records
    is an explicit sourced component that cannot honestly get a CHEBI term.
    Keep accidental ungrounded imports in the ranking, but stop re-emitting
    these already-reviewed wrappers.
    """
    data_quality_flags = doc.get("data_quality_flags") or []
    return (
        bool(components)
        and isinstance(data_quality_flags, list)
        and "ingredients_curated" in data_quality_flags
        and "has_unmapped_ingredients" in data_quality_flags
    )


def _source_unavailable_empty_record(
    doc: dict[str, Any],
    components: list[dict[str, Any]],
) -> bool:
    """Return whether an empty recipe was reviewed and has no available source data."""
    data_quality_flags = doc.get("data_quality_flags") or []
    return (
        not components
        and isinstance(data_quality_flags, list)
        and "source_information_unavailable" in data_quality_flags
    )


def _curated_legacy_source_url_unavailable(doc: dict[str, Any]) -> bool:
    """Return whether a legacy source URL was reviewed and no longer resolves."""
    data_quality_flags = doc.get("data_quality_flags") or []
    return (
        isinstance(data_quality_flags, list)
        and "ingredients_curated" in data_quality_flags
        and "legacy_source_url_unavailable" in data_quality_flags
    )


def _has_source_provenance(doc: dict[str, Any]) -> bool:
    """Return whether a recipe points to any structured source identity."""
    if doc.get("media_term"):
        return True

    sources = doc.get("sources")
    if not isinstance(sources, list):
        return False

    return any(
        isinstance(source, dict)
        and bool(source.get("database") or source.get("database_id") or source.get("url"))
        for source in sources
    )


def score_record(doc: dict[str, Any]) -> tuple[int, list[str]]:
    """Return (score, reasons). Higher means more in need of review."""
    score = 0
    reasons: list[str] = []

    def hit(points: int, label: str) -> None:
        nonlocal score
        score += points
        reasons.append(label)

    components = composition_components(doc)
    names = [str(component.get("preferred_term") or "") for component in components]

    # --- structural
    data_quality_flags = doc.get("data_quality_flags") or []
    curated_components = (
        isinstance(data_quality_flags, list) and "ingredients_curated" in data_quality_flags
    )

    if not components and not _source_unavailable_empty_record(doc, components):
        hit(30, "no ingredients or solutions")
    elif components and len(components) <= 2 and not curated_components:
        hit(15, f"only {len(components)} composition component(s)")
    if any(PLACEHOLDER.search(n) for n in names):
        hit(25, "placeholder ingredient text")
    if any(len(n) > 40 and MANGLED.search(n) for n in names):
        hit(25, "ingredient name contains an unparsed recipe")

    # --- grounding
    if components and not _curated_known_unmapped_components(doc, components):
        n_grounded = sum(1 for component in components if _grounded(component))
        if n_grounded == 0:
            hit(20, "no composition component is grounded")
        elif n_grounded / len(components) < 0.5:
            hit(10, f"only {n_grounded}/{len(components)} composition components grounded")

    # --- identity / provenance
    if not _has_source_provenance(doc) and not _curated_legacy_source_url_unavailable(doc):
        hit(10, "no media_term (untraceable to a source catalogue)")
    display_name = str(doc.get("original_name") or doc.get("name") or "")
    if STRAIN_POINTER.fullmatch(display_name) and not _curated_strain_pointer_variant(doc):
        hit(10, f"name {display_name!r} identifies a strain, not a medium")
    if not doc.get("notes"):
        hit(5, "no notes/provenance")

    # --- conditions
    if not any(doc.get(k) for k in CONDITION_SLOTS):
        hit(5, "no pH and no temperature")

    return score, reasons


def score_parsed(records: list[tuple[str, dict[str, Any]]]) -> list[dict[str, Any]]:
    """Rank already-parsed records, so callers that hold the corpus need not re-read it.

    Split out from `collect` for the corpus guards: each was calling `collect()`
    and re-parsing ~15,900 files, and five such tests were enough to cancel the
    pytest job at the 40-minute CI ceiling (#189). Tests pass the session-scoped
    `corpus` fixture here instead.
    """
    rows: list[dict[str, Any]] = []
    for rel, doc in records:
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        score, reasons = score_record(doc)
        # A record qualifies only on a signal that is not merely the corpus norm.
        if not any(r not in NORM_LEVEL_SIGNALS for r in reasons):
            continue
        rows.append(
            {
                "score": score,
                "file_path": rel,
                "record_id": str(doc.get("id") or ""),
                "name": str(doc.get("original_name") or doc.get("name") or ""),
                "n_components": str(len(composition_components(doc))),
                "reasons": "; ".join(reasons),
            }
        )
    rows.sort(key=lambda r: (-r["score"], r["file_path"]))
    return rows


def collect(normalized: Path = NORMALIZED) -> list[dict[str, Any]]:
    """Parse the corpus from disk, then score it."""
    records: list[tuple[str, dict[str, Any]]] = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.load(path.read_text(errors="replace"), Loader=YAML_LOADER)
        except (yaml.YAMLError, OSError):
            continue
        records.append((str(path.relative_to(normalized)), doc))
    return score_parsed(records)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--top", type=int, default=0, help="also print the worst N")
    args = ap.parse_args(argv)

    rows = collect(args.normalized_dir)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(
            fh,
            delimiter="\t",
            lineterminator="\n",
            fieldnames=["score", "file_path", "record_id", "name", "n_components", "reasons"],
        )
        w.writeheader()
        w.writerows(rows)

    buckets = {"70+": 0, "50-69": 0, "30-49": 0, "15-29": 0, "1-14": 0}
    for r in rows:
        s = r["score"]
        key = (
            "70+"
            if s >= 70
            else "50-69" if s >= 50 else "30-49" if s >= 30 else "15-29" if s >= 15 else "1-14"
        )
        buckets[key] += 1

    print(f"Records with at least one review signal: {len(rows)}")
    for k, v in buckets.items():
        print(f"  score {k:6s} {v:6d}")
    print(f"\nWrote {args.out.relative_to(REPO) if args.out.is_relative_to(REPO) else args.out}")

    for r in rows[: args.top]:
        print(f"  {r['score']:3d}  {r['file_path'][:48]:50s} {r['reasons'][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
