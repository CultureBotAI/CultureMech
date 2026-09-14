#!/usr/bin/env python3
"""Repair TOGO M2884 glucose streptococcal broth medium."""

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
TARGET = Path("bacterial/glucose_streptococcal_broth_medium.yaml")
EXPECTED_ID = "CultureMech:009419"
EXPECTED_MEDIA_TERM = "TOGO:M2884"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2884_score15.py"
ACTION = "RESOLVED_TOGO_M2884_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2884 = "https://togomedium.org/medium/M2884"
PMID = "PMID:8031083"
DOI = "doi:10.1128/aem.60.6.1875-1883.1994"
SOURCE = "TOGO M2884"
TITLE = "Glucose streptococcal broth medium"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("Sodium-β-glycerophosphate", "7.2", "G_PER_L"),
    ("Glucose", "10", "G_PER_L"),
    ("Meat extract", "10", "G_PER_L"),
    ("Tryptose", "5", "G_PER_L"),
    ("Tryptone", "5", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1.0", "L"),
    ("Yeast extract", "5.0", "G_PER_L"),
    ("Sodium beta-glycerophosphate", "7.2", "G_PER_L"),
    ("Glucose", "10.0", "G_PER_L"),
    ("Meat extract", "10.0", "G_PER_L"),
    ("Tryptose", "5.0", "G_PER_L"),
    ("Tryptone", "5.0", "G_PER_L"),
)

REFERENCES = (TOGO_M2884, PMID, DOI)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "Sodium beta-glycerophosphate": (
        "CHEBI:132089",
        "sodium glycerol 2-phosphate",
    ),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Tryptone": ("MICRO:0000182", "tryptone"),
}

COMPONENT_NOTES: dict[str, str] = {
    "Distilled water": "TOGO M2884 lists 1 L distilled water.",
    "Yeast extract": "TOGO M2884 lists 5 g/L yeast extract.",
    "Sodium beta-glycerophosphate": ("TOGO M2884 lists 7.2 g/L Sodium-beta-glycerophosphate."),
    "Glucose": "TOGO M2884 lists 10 g/L glucose.",
    "Meat extract": (
        "TOGO M2884 lists 10 g/L meat extract; this biological extract is "
        "retained as an opaque complex component."
    ),
    "Tryptose": (
        "TOGO M2884 lists 5 g/L tryptose; this Bacto Tryptose-like peptone "
        "product is retained as an opaque complex component."
    ),
    "Tryptone": "TOGO M2884 lists 5 g/L tryptone.",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve 5.0 g yeast extract, 7.2 g sodium beta-glycerophosphate, "
            "10.0 g glucose, 10.0 g meat extract, 5.0 g tryptose, and 5.0 g "
            "tryptone in 1.0 L distilled water."
        ),
    },
)

NOTES = (
    "TOGO M2884 lists glucose streptococcal broth as 1 L distilled water, "
    "5 g yeast extract, 7.2 g Sodium-beta-glycerophosphate, 10 g glucose, "
    "10 g meat extract, 5 g tryptose, and 5 g tryptone. TOGO cites "
    "Arendt et al. 1994 for Lactococcus lactis strains grown at 30 C in "
    "M17 medium supplemented with glucose or glucose streptococcal broth."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": COMPONENT_NOTES[preferred_term],
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
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

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {signature!r}"
        )

    if doc.get("solutions"):
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
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported distilled-water unit from g/L "
            "to 1 L and grounded water, yeast extract, sodium "
            "beta-glycerophosphate, glucose, and tryptone."
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
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    _put_after(repaired, "temperature_value", 30.0, "physical_state")
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "ingredients")
    repaired.pop("sterilization", None)
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
