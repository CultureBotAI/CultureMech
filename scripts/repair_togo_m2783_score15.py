#!/usr/bin/env python3
"""Repair TOGO M2783 Nutrient broth."""

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
TARGET = Path("bacterial/TOGO_M2783_Nutrient_broth.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009332"
EXPECTED_MEDIA_TERM = "TOGO:M2783"

CURATOR = "repair_togo_m2783_score15.py"
ACTION = "RESOLVED_TOGO_M2783_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2783 = "https://togomedium.org/medium/M2783"
PMID = "PMID:30754267"
DOI = "doi:10.1094/PDIS-94-2-0236"

SOURCE = "TOGO M2783 / Schroeder et al. 2010"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("1M MgSO4", "1", "G_PER_L"),
    ("20% Glucose", "25", "G_PER_L"),
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "2", "G_PER_L"),
    ("KH2PO4", "0.5", "G_PER_L"),
    ("K2HPO4 (anhydrous)", "2", "G_PER_L"),
    ("Nutrient broth", "8", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Nutrient broth", "8.0", "G_PER_L"),
    ("Yeast extract", "2.0", "G_PER_L"),
    ("K2HPO4 (anhydrous)", "2.0", "G_PER_L"),
    ("KH2PO4", "0.5", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("20% Glucose", "25.0", "ML_PER_L"),
    ("1M MgSO4", "1.0", "ML_PER_L"),
)

REFERENCES = (TOGO_M2783, PMID, DOI)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "1M MgSO4": ("CHEBI:32599", "magnesium sulfate"),
    "20% Glucose": ("CHEBI:17234", "glucose"),
    "Distilled water": ("CHEBI:15377", "water"),
    "K2HPO4 (anhydrous)": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

COMPONENT_NOTES: dict[str, str] = {
    "1M MgSO4": "TOGO M2783 lists 1.0 ml/L 1 M MgSO4 solution.",
    "20% Glucose": "TOGO M2783 lists 25.0 ml/L 20% glucose solution.",
    "Distilled water": "TOGO M2783 lists the formulation per liter of distilled water.",
    "K2HPO4 (anhydrous)": "TOGO M2783 lists 2.0 g/L anhydrous K2HPO4.",
    "KH2PO4": "TOGO M2783 lists 0.5 g/L KH2PO4.",
    "Nutrient broth": (
        "TOGO M2783 lists 8.0 g/L Difco nutrient broth powder; the complex "
        "product remains intentionally unmapped."
    ),
    "Yeast extract": "TOGO M2783 lists 2.0 g/L yeast extract.",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Per liter of distilled water, dissolve 8.0 g Nutrient broth, "
            "2.0 g yeast extract, 2.0 g anhydrous K2HPO4, and 0.5 g KH2PO4, "
            "then add 25.0 ml 20% glucose and 1.0 ml 1 M MgSO4."
        ),
    },
)

NOTES = (
    "TOGO M2783 records the nutrient broth used to grow Enterobacter cloacae "
    "strain EcWSU1 overnight for Schroeder et al., Plant Disease 94:236-243. "
    "The formulation is, per liter of distilled water, 8.0 g nutrient broth, "
    "2.0 g yeast extract, 2.0 g anhydrous K2HPO4, 0.5 g KH2PO4, 25.0 ml 20% "
    "glucose, and 1.0 ml 1 M MgSO4."
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

SOLUTIONS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_SOLUTION_SIGNATURE
)


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

    signatures = (
        _signature(doc.get("ingredients"), "ingredients"),
        _signature(doc.get("solutions"), "solutions"),
    )
    if signatures not in (
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURE),
    ):
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
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "ingredients_curated",
        "has_unmapped_ingredients",
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
            f"{NOTES} Corrected the imported 1 M MgSO4, 20% glucose, and "
            "distilled-water units; moved glucose and MgSO4 stocks to solutions; "
            "grounded the machine-usable salts, glucose, water, and yeast "
            "extract; and left the Difco nutrient broth product intentionally "
            "unmapped."
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


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_target(_load(path))}


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
