#!/usr/bin/env python3
"""Repair TOGO M2273 Marine-Caulobacter SPYEM medium."""

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
TARGET = Path("bacterial/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2273_marine_caulobacter_score15.py"
ACTION = "RESOLVED_TOGO_M2273_MARINE_CAULOBACTER_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:008859"
EXPECTED_MEDIA_TERM = "TOGO:M2273"
TOGO_M2273 = "https://togomedium.org/medium/M2273"
SOURCE = "TOGO Medium M2273"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NH4Cl", "0.5", "G_PER_L"),
    ("Sea salts (Sigma)", "30", "G_PER_L"),
    ("Deionized water", "12.0", "G_PER_L"),
    ("Glucose (50%)", "2", "G_PER_L"),
    ("50xPYE", "20", "G_PER_L"),
    ("Riboflavin (0.2 mg/ml)", "5", "G_PER_L"),
    ("Yeast extract", "50", "G_PER_L"),
    ("Peptone", "100", "G_PER_L"),
    ("Riboflavin", "2", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NH4Cl", "0.5", "G_PER_L"),
    ("Sea salts (Sigma)", "30", "G_PER_L"),
    ("Deionized water", "1000", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Glucose (50%)", "2", "ML_PER_L"),
    ("50xPYE", "20", "ML_PER_L"),
    ("Riboflavin (0.2 mg/ml)", "5", "ML_PER_L"),
)

REFERENCES = (TOGO_M2273,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Deionized water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
}

COMPONENT_NOTES = {
    "NH4Cl": "TOGO M2273 lists 0.5 g/L NH4Cl in the autoclaved base.",
    "Sea salts (Sigma)": (
        "TOGO M2273 lists 30 g/L Sea salts from Sigma without disclosing the "
        "product composition."
    ),
    "Deionized water": "TOGO M2273 lists 1 L deionized water in the autoclaved base.",
}

NOTES = (
    "TOGO Medium M2273 lists an autoclaved base of 0.5 g NH4Cl, 30 g Sea "
    "salts (Sigma), and 1 L deionized water. After autoclaving and cooling, "
    "TOGO adds 2 ml sterile 50% glucose, 20 ml 50xPYE, and 5 ml "
    "filter-sterilized 0.2 mg/ml riboflavin per liter of medium; 50xPYE "
    "contains 100 g peptone and 50 g yeast extract in 1 L deionized water "
    "and is autoclaved."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix 0.5 g NH4Cl and 30 g Sea salts (Sigma) in 1 L deionized "
            "water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base medium and cool it.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave 50xPYE before use.",
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": "Filter-sterilize the 0.2 mg/ml riboflavin solution.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add 20 ml 50xPYE, 2 ml sterile 50% glucose, and "
            "5 ml filter-sterilized 0.2 mg/ml riboflavin per liter."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": COMPONENT_NOTES[preferred_term],
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
) -> dict[str, Any]:
    grounding = GROUNDINGS.get(preferred_term)
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
    }
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _ingredient(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Glucose (50%)",
        "concentration": {"value": "2", "unit": "ML_PER_L"},
        "notes": "TOGO M2273 adds 2 ml/L sterile 50% glucose after cooling.",
        "composition": [_stock_component("Glucose", "50", "PERCENT_W_V")],
    },
    {
        "preferred_term": "50xPYE",
        "concentration": {"value": "20", "unit": "ML_PER_L"},
        "notes": (
            "TOGO M2273 adds 20 ml/L autoclaved 50xPYE containing "
            "100 g/L peptone and 50 g/L yeast extract."
        ),
        "composition": [
            _stock_component("Peptone", "100", "G_PER_L"),
            _stock_component("Yeast extract", "50", "G_PER_L"),
            _stock_component("Deionized water", "1000", "ML_PER_L"),
        ],
    },
    {
        "preferred_term": "Riboflavin (0.2 mg/ml)",
        "concentration": {"value": "5", "unit": "ML_PER_L"},
        "notes": (
            "TOGO M2273 adds 5 ml/L filter-sterilized 0.2 mg/ml "
            "riboflavin solution after cooling."
        ),
        "composition": [
            _stock_component("Riboflavin", "0.2", "MG_PER_ML"),
            _stock_component("Deionized water", "10", "ML_PER_L"),
        ],
    },
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
    if _signature(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": TOGO_M2273,
        "notes": (
            f"{NOTES} Restored top-level deionized water to 1 L, converted "
            "glucose, 50xPYE, and riboflavin from g/L ingredient rows to "
            "ml/L stock-solution additions, and moved stock-only peptone, "
            "yeast extract, riboflavin, and deionized-water rows into "
            "nested stock compositions."
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
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}
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
