#!/usr/bin/env python3
"""Repair DSMZ/MediaDive Medium 1077 PH MEDIUM."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/ph_medium.yaml")
EXPECTED_ID = "CultureMech:000511"
EXPECTED_MEDIA_TERM = "mediadive.medium:1077"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_mediadive_1077_ph_medium_score15.py"
ACTION = "RESOLVED_MEDIADIVE_1077_PH_MEDIUM_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

MEDIADIVE_1077 = "https://mediadive.dsmz.de/medium/1077"
DSMZ_1077 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1077.pdf"
REFERENCES = (MEDIADIVE_1077, DSMZ_1077)
SOURCE = "DSMZ/MediaDive Medium 1077"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...], tuple["SolutionSignature", ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("PPLO broth", "21", "G_PER_L"),
    ("Horse serum", "18.7", "G_PER_L"),
    ("Yeast extract", "0.234", "G_PER_L"),
    ("Fish-Sperm DNA", "0.187", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Horse serum": ("MICRO:0001235", "Horse serum"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "Distilled water": ("CHEBI:15377", "water"),
}

NOTES = (
    "DSMZ Medium 1077 prepares PH MEDIUM by combining 80 ml Solution 1 with "
    "20 ml Solution 2. Solution 1 is PPLO broth in distilled water adjusted to "
    "pH 6.5 and autoclaved; Solution 2 contains inactivated horse serum, "
    "autoclaved 25% yeast extract solution, filter-sterilized fish sperm DNA "
    "solution, and water adjusted to pH 7.8."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    *,
    ground: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if ground:
        term = _term(*GROUNDINGS[preferred_term])
        row["term"] = term
        if term["id"].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _solution(
    preferred_term: str,
    value: str,
    notes: str,
    *,
    composition: tuple[dict[str, Any], ...] = (),
    solutions: tuple[dict[str, Any], ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
    }
    if composition:
        row["composition"] = copy.deepcopy(list(composition))
    if solutions:
        row["solutions"] = copy.deepcopy(list(solutions))
    return row


SOLUTION_1_COMPOSITION: tuple[dict[str, Any], ...] = (
    _component(
        "PPLO broth",
        "21.0",
        "G_PER_L",
        (
            "DSMZ Medium 1077 Solution 1 lists 1.68 g PPLO broth in 80.00 ml. "
            "PPLO broth is retained ungrounded because the pinned MIM label "
            "index marks it as an intentionally unmapped complex product."
        ),
        ground=False,
    ),
    _component(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        "DSMZ Medium 1077 Solution 1 lists 80.00 ml distilled water per 80 ml.",
    ),
)
YEAST_EXTRACT_25_PERCENT = _solution(
    "Yeast Extract Solution (25%, autoclaved)",
    "46.8",
    (
        "DSMZ Medium 1077 Solution 2 lists 0.936 ml 25% autoclaved yeast "
        "extract solution in 20 ml."
    ),
    composition=(
        _component(
            "Yeast extract",
            "250.0",
            "G_PER_L",
            "The stock name states 25% Yeast Extract Solution.",
        ),
    ),
)
FISH_SPERM_DNA_SOLUTION = _solution(
    "Fish sperm DNA solution (filter-sterilized)",
    "9.35",
    (
        "DSMZ Medium 1077 Solution 2 lists 0.187 ml filter-sterilized fish "
        "sperm DNA solution in 20 ml; the source does not disclose its DNA "
        "concentration."
    ),
)
SOLUTION_2_COMPOSITION: tuple[dict[str, Any], ...] = (
    _component(
        "Horse serum",
        "935.0",
        "ML_PER_L",
        "DSMZ Medium 1077 Solution 2 lists 18.700 ml inactivated horse serum in 20 ml.",
    ),
    _component(
        "Distilled water",
        "9.35",
        "ML_PER_L",
        "DSMZ Medium 1077 Solution 2 lists 0.187 ml distilled water in 20 ml.",
    ),
)
SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "Solution 1",
        "800.0",
        "The final 100 ml PH MEDIUM combines 80 ml Solution 1 with 20 ml Solution 2.",
        composition=SOLUTION_1_COMPOSITION,
    ),
    _solution(
        "Solution 2",
        "200.0",
        "The final 100 ml PH MEDIUM combines 80 ml Solution 1 with 20 ml Solution 2.",
        composition=SOLUTION_2_COMPOSITION,
        solutions=(YEAST_EXTRACT_25_PERCENT, FISH_SPERM_DNA_SOLUTION),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Prepare Solution 1, adjust it to pH 6.5, and autoclave it.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Prepare Solution 2 and adjust it to pH 7.8.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "Combine 80 ml Solution 1 with 20 ml Solution 2.",
    },
)


def _component_signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("component collection is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("component collection contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"component {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(rows: Any) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in rows:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {solution.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _component_signature(solution.get("composition")),
                _solution_signatures(solution.get("solutions")),
            )
        )
    return tuple(signatures)


FINAL_SOLUTION_SIGNATURES = _solution_signatures(list(SOLUTIONS))


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signature = (_component_signature(doc.get("ingredients")), _solution_signatures(doc.get("solutions")))
    if signature not in {
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        ((), FINAL_SOLUTION_SIGNATURES),
    }:
        raise ValueError(f"{TARGET}: ingredient/solution signature drifted")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Restored the DSMZ/MediaDive Solution 1 and Solution 2 stock "
            "structure, corrected milliliter stock additions imported as g/L, "
            "grounded exact MIM-supported components, and retained PPLO broth "
            "and fish sperm DNA solution as intentionally unmapped."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = []
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
