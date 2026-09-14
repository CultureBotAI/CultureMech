#!/usr/bin/env python3
"""Repair TOGO M149 Tryptose Phosphate Agar."""

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
TARGET = Path("bacterial/TOGO_M149_Tryptose_Phosphate_Agar.yaml")
EXPECTED_ID = "CultureMech:008044"
EXPECTED_MEDIA_TERM = "TOGO:M149"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m149_score15.py"
ACTION = "RESOLVED_TOGO_M149_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M149 = "https://togomedium.org/medium/M149"
MEDIADIVE_J158 = "https://mediadive.dsmz.de/rest/medium/J158"

SOURCE = "TOGO M149 / MediaDive J158"
TITLE = "Tryptose Phosphate Agar"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15", "G_PER_L"),
    ("Tryptose phosphate broth (BD-Difco)", "29.5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Bacto agar (BD-Difco)", "15.0", "G_PER_L"),
    ("Tryptose phosphate broth (BD-Difco)", "29.5", "G_PER_L"),
)

REFERENCES = (TOGO_M149, MEDIADIVE_J158)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1.0", "unit": "L"},
        "source": SOURCE,
        "notes": (
            "TOGO M149 lists 1 L distilled water, matching MediaDive J158's " "1000 ml water basis."
        ),
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    },
    {
        "preferred_term": "Bacto agar (BD-Difco)",
        "concentration": {"value": "15.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "TOGO M149 lists 15 g/L Bacto agar (BD-Difco), matching "
            "MediaDive J158's BD-Difco Bacto Agar row; this commercial "
            "agar product is retained as an opaque complex component."
        ),
    },
    {
        "preferred_term": "Tryptose phosphate broth (BD-Difco)",
        "concentration": {"value": "29.5", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "TOGO M149 lists 29.5 g/L Tryptose phosphate broth (BD-Difco), "
            "matching MediaDive J158's BD-Difco broth row; this commercial "
            "broth is retained as an opaque complex component."
        ),
    },
)

NOTES = (
    "TOGO M149 imports JCM_M158 as Tryptose Phosphate Agar and lists 1 L "
    "distilled water, 15 g Bacto agar (BD-Difco), and 29.5 g Tryptose "
    "phosphate broth (BD-Difco). MediaDive J158 preserves the same JCM "
    "formula as 1000 ml water with the same commercial agar and broth "
    "amounts. The JCM GRMD=158 URL named by TOGO and MediaDive no longer "
    "returns the recipe; no pH, incubation condition, or preparation steps "
    "are available from these accessible source records."
)


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


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


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

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if _solution_signatures(doc):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
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
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported water g/L artifact and marked "
            "the accessible JCM-derived formula as curated."
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
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
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
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
