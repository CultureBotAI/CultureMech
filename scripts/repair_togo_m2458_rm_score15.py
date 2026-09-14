#!/usr/bin/env python3
"""Repair TOGO M2458 / ATCC 1341 RM Medium."""

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
TARGET = Path("bacterial/rm_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2458_rm_score15.py"
ACTION = "RESOLVED_TOGO_M2458_RM_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:009036"
EXPECTED_MEDIA_TERM = "TOGO:M2458"
TOGO_M2458 = "https://togomedium.org/medium/M2458"
ATCC_1341 = "https://www.atcc.org/~/media/C3C9EB3F405C4C4E96F1D44126D4F514.ashx"
TOGO_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2458"
SOURCE = "ATCC Medium 1341 / TOGO M2458"

Component = tuple[str, str, str]
Term = tuple[str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast Extract", "10", "G_PER_L"),
    ("K2HPO4", "2", "G_PER_L"),
    ("DI water", "1000", "G_PER_L"),
    ("Glucose", "20", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glucose", "20.0", "G_PER_L"),
    ("Yeast extract", "10.0", "G_PER_L"),
    ("K2HPO4", "2.0", "G_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
    ("DI water", "1000.0", "ML_PER_L"),
)

REFERENCES = (TOGO_M2458, ATCC_1341, TOGO_API)

GROUNDINGS: dict[str, Term] = {
    "Glucose": ("CHEBI:17234", "glucose"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "DI water": ("CHEBI:15377", "water"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Glucose": ("CARBON_SOURCE",),
    "K2HPO4": ("PHOSPHATE_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "K2HPO4": ("BUFFER",),
    "Agar (if needed)": ("SOLIDIFYING_AGENT",),
}

COMPONENT_NOTES = {
    "Glucose": f"{SOURCE} lists 20.0 g/L glucose.",
    "Yeast extract": f"{SOURCE} lists 10.0 g/L yeast extract.",
    "K2HPO4": f"{SOURCE} lists 2.0 g/L K2HPO4.",
    "Agar (if needed)": f"{SOURCE} lists 15.0 g/L agar if needed.",
    "DI water": f"{SOURCE} lists 1000.0 ml DI water.",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave glucose, yeast extract, K2HPO4, agar if needed, "
            "and DI water as separate components."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Combine the separately autoclaved components.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.0.",
    },
)

NOTES = (
    "ATCC Medium 1341, mirrored by TOGO M2458, lists RM Medium with "
    "20.0 g glucose, 10.0 g yeast extract, 2.0 g K2HPO4, 15.0 g agar if "
    "needed, and 1000.0 ml DI water. ATCC directs separately autoclaving "
    "each component, combining the sterile components, and adjusting pH to "
    "6.0."
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
        "term": _term(*GROUNDINGS[preferred_term]),
    }
    if row["term"]["id"].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])
    if nutritional_roles := NUTRITIONAL_ROLES.get(preferred_term):
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles := PHYSICOCHEMICAL_ROLES.get(preferred_term):
        row["physicochemical_roles"] = list(physicochemical_roles)
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
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: unexpected solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)
    while "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


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
            "Corrected the imported DI-water row from a g/L artifact to "
            "1000.0 ml/L, grounded all five components, added ATCC's pH 6.0 "
            "and separate-autoclaving instructions, and marked the formula "
            "as curated."
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
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 6.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("solutions", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    return {target_path: repair_target(_load(target_path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
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
