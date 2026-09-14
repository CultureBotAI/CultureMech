#!/usr/bin/env python3
"""Repair TOGO M1645 / NBRC 848 BL Agar."""

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
TARGET = Path("bacterial/bl_agar.yaml")
EXPECTED_ID = "CultureMech:008201"
EXPECTED_MEDIA_TERM = "TOGO:M1645"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1645_bl_agar_score15.py"
ACTION = "RESOLVED_TOGO_M1645_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1645 = "https://togomedium.org/medium/M1645"
NBRC_848 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=848"

SOURCE = "TOGO M1645 / NBRC Medium 848"
TITLE = "BL Agar"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "950", "G_PER_L"),
    ("Defibrinated horse blood", "50", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (("BL Agar*", "58", "G_PER_L", ()),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("BL Agar*", "58.0", "G_PER_L"),
    ("Defibrinated horse blood", "50.0", "ML_PER_L"),
    ("Distilled water", "950.0", "ML_PER_L"),
)

REFERENCES = (TOGO_M1645, NBRC_848)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Defibrinated horse blood": ("UBERON:0000178", "blood"),
    "Distilled water": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

INGREDIENTS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "BL Agar*",
        "concentration": {"value": "58.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 848 lists 58 g/L BL Agar and notes that the "
            "asterisk marks Nissui Pharmaceutical Co. Ltd.; this commercial "
            "BL Agar product is retained as an opaque base/solidifying "
            "component."
        ),
    },
    {
        "preferred_term": "Defibrinated horse blood",
        "concentration": {"value": "50.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 848 lists 50 ml/L sterile defibrinated horse blood "
            "added aseptically to a final 5% v/v."
        ),
        "term": {"id": "UBERON:0000178", "label": "blood"},
    },
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "950.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "NBRC Medium 848 lists 950 ml/L distilled water.",
        "term": {"id": "CHEBI:15377", "label": "water"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:15377",
            "label": "water",
        },
    },
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Autoclave the BL Agar base without horse blood.",
    },
    {
        "step_number": 2,
        "action": "COOL",
        "description": "Cool to about 50 C.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Aseptically add sterile defibrinated horse blood to 5% v/v final " "and mix."
        ),
    },
    {
        "step_number": 4,
        "action": "POUR_PLATES",
        "description": "Quickly dispense into sterile test tubes or Petri dishes.",
    },
)

NOTES = (
    "TOGO M1645 imports NBRC Medium 848 as BL Agar. NBRC 848 lists 58 g "
    "BL Agar from Nissui Pharmaceutical, 50 ml defibrinated horse blood, "
    "950 ml distilled water, and no pH. NBRC 848 instructs autoclaving the "
    "base without horse blood, cooling to about 50 C, aseptically adding "
    "sterile defibrinated horse blood to 5% final, then quickly dispensing "
    "into sterile test tubes or Petri dishes."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
    solution_signature = _solution_signatures(doc)
    if (ingredient_signature, solution_signature) not in (
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURE),
        (FINAL_INGREDIENT_SIGNATURE, ()),
    ):
        raise ValueError(
            f"{TARGET}: composition signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} / "
            f"{IMPORTED_SOLUTION_SIGNATURE!r} to "
            f"{ingredient_signature!r} / {solution_signature!r}"
        )


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
            f"{NOTES} Moved the Nissui BL Agar product out of an empty "
            "solution wrapper, corrected water and horse blood liquid units, "
            "and marked the NBRC formula as curated."
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
    repaired["physical_state"] = "SOLID_AGAR"
    for stale_key in (
        "ph_value",
        "ph_range",
        "temperature_value",
        "temperature_range",
        "sterilization",
        "solutions",
    ):
        repaired.pop(stale_key, None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
