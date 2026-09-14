#!/usr/bin/env python3
"""Repair TOGO M2408 Modified Leptospira Medium."""

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
TARGET = Path("bacterial/modified_leptospira_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008991"
EXPECTED_MEDIA_TERM = "TOGO:M2408"

CURATOR = "repair_togo_m2408_leptospira_score15.py"
ACTION = "RESOLVED_TOGO_M2408_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2408 = "https://togomedium.org/medium/M2408"
ATCC_1470 = "https://www.atcc.org/~/media/D1844FEFC4614D7FAFD9CD3C4FE12C43.ashx"
SOURCE = "TOGO M2408 / ATCC Medium 1470"
TITLE = "Modified Leptospira Medium"

NACL = "NaCl"
DI_WATER = "DI Water"
AGAR = "Agar"
BEEF_EXTRACT = "Beef Extract"
PEPTONE = "Peptone"
SUPPLEMENT_A = "Supplement A"
RABBIT_SERUM = "Sterile Rabbit Serum"
HEMIN_SOLUTION = "0.05% Hemin solution"
HEMIN = "Hemin"
NAOH_STOCK = "0.1N NaOH"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...], tuple[Any, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (NACL, "0.5", "G_PER_L"),
    (DI_WATER, "900", "G_PER_L"),
    (AGAR, "1.5", "G_PER_L"),
    (BEEF_EXTRACT, "0.2", "G_PER_L"),
    (PEPTONE, "0.3", "G_PER_L"),
    (SUPPLEMENT_A, "100", "G_PER_L"),
    (RABBIT_SERUM, "100", "G_PER_L"),
    ("Distilled water", "100", "G_PER_L"),
    (HEMIN, "0.05", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    (HEMIN_SOLUTION, "2.5", "G_PER_L", (), ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (NACL, "0.5", "G_PER_L"),
    (DI_WATER, "900.0", "ML_PER_L"),
    (AGAR, "1.5", "G_PER_L"),
    (BEEF_EXTRACT, "0.2", "G_PER_L"),
    (PEPTONE, "0.3", "G_PER_L"),
)

SUPPLEMENT_A_SIGNATURE: tuple[Component, ...] = (
    (RABBIT_SERUM, "100.0", "ML_PER_L"),
)

HEMIN_STOCK_SIGNATURE: tuple[Component, ...] = (
    (HEMIN, "0.05", "PERCENT_W_V"),
    (NAOH_STOCK, "10.0", "ML_PER_L"),
    (DI_WATER, "990.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[SolutionSignature, ...] = (
    (
        SUPPLEMENT_A,
        "100.0",
        "ML_PER_L",
        SUPPLEMENT_A_SIGNATURE,
        ((HEMIN_SOLUTION, "2.5", "ML_PER_L", HEMIN_STOCK_SIGNATURE, ()),),
    ),
)

REFERENCES = (TOGO_M2408, ATCC_1470)

GROUNDINGS: dict[str, tuple[str, str]] = {
    NACL: ("CHEBI:26710", "sodium chloride"),
    DI_WATER: ("CHEBI:15377", "water"),
    AGAR: ("CHEBI:2509", "agar"),
    BEEF_EXTRACT: ("FOODON:03302088", "Beef extract"),
    PEPTONE: ("MICRO:0000178", "Peptone"),
    RABBIT_SERUM: ("MICRO:0002392", "Rabbit serum"),
    HEMIN: ("CHEBI:50385", "hemin"),
}

MEDIAINGREDIENT_CHEBI = frozenset({NACL, DI_WATER, AGAR, HEMIN})

NOTES = (
    "TOGO M2408 imports ATCC Medium 1470 as Modified Leptospira Medium. "
    "ATCC 1470 lists 0.3 g Peptone, 0.2 g Beef Extract, 0.5 g NaCl, "
    "1.5 g Agar, 100 ml Supplement A, and 900 ml DI Water for the base; "
    "Supplement A is prepared from 100 ml Sterile Rabbit Serum and 2.5 ml "
    "0.05% Hemin solution, and the final pH is adjusted to 7.3 +/- 0.1."
)

INGREDIENT_NOTES = {
    NACL: f"{SOURCE} lists 0.5 g/L NaCl.",
    DI_WATER: f"{SOURCE} lists 900 ml/L DI Water in the base medium.",
    AGAR: (
        f"{SOURCE} lists 1.5 g/L Agar and instructs making this as a "
        "thickened broth for all vessel types."
    ),
    BEEF_EXTRACT: f"{SOURCE} lists 0.2 g/L Beef Extract.",
    PEPTONE: f"{SOURCE} lists 0.3 g/L Peptone.",
    RABBIT_SERUM: f"{SOURCE} prepares Supplement A from 100 ml Sterile Rabbit Serum.",
    HEMIN: f"{SOURCE} prepares the 0.05% Hemin solution from 0.05% w/v Hemin.",
    NAOH_STOCK: (
        f"{SOURCE} dissolves Hemin in 0.1N NaOH before adding DI Water; "
        "0.1N NaOH is retained as a source-qualified solution."
    ),
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Dissolve 0.3 g Peptone, 0.2 g Beef Extract, 0.5 g NaCl, and "
            "1.5 g Agar in 900 ml DI Water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the base to pH 7.4.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Cool the base to 50 C and aseptically add sterile Supplement A."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Adjust the final medium to pH 7.3 +/- 0.1.",
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "ATCC Medium 1470 autoclaves the base at 121 C for 15 min; "
        "Supplement A is filter sterilized before aseptic addition."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term in MEDIAINGREDIENT_CHEBI:
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS = tuple(
    _component(
        name,
        value,
        unit,
        source=SOURCE,
        notes=INGREDIENT_NOTES[name],
    )
    for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)

HEMIN_STOCK = {
    "preferred_term": HEMIN_SOLUTION,
    "concentration": {"value": "2.5", "unit": "ML_PER_L"},
    "source": SOURCE,
    "notes": (
        f"{SOURCE} prepares Supplement A with 2.5 ml of 0.05% Hemin solution."
    ),
    "composition": [
        _component(
            HEMIN,
            "0.05",
            "PERCENT_W_V",
            source=f"{SOURCE} 0.05% Hemin solution",
            notes=INGREDIENT_NOTES[HEMIN],
        ),
        _component(
            NAOH_STOCK,
            "10.0",
            "ML_PER_L",
            source=f"{SOURCE} 0.05% Hemin solution",
            notes=INGREDIENT_NOTES[NAOH_STOCK],
        ),
        _component(
            DI_WATER,
            "990.0",
            "ML_PER_L",
            source=f"{SOURCE} 0.05% Hemin solution",
            notes=(
                f"{SOURCE} brings the 0.05% Hemin solution to 100 ml with "
                "99 ml DI Water."
            ),
        ),
    ],
    "preparation_notes": (
        "Dissolve 0.05 g Hemin in 1 ml 0.1N NaOH, add 99 ml DI Water, "
        "then autoclave at 121 C for 15 min or filter sterilize."
    ),
}

SUPPLEMENT_A_SOLUTION = {
    "preferred_term": SUPPLEMENT_A,
    "concentration": {"value": "100.0", "unit": "ML_PER_L"},
    "source": SOURCE,
    "notes": f"{SOURCE} adds 100 ml/L sterile Supplement A to the base medium.",
    "composition": [
        _component(
            RABBIT_SERUM,
            "100.0",
            "ML_PER_L",
            source=SOURCE,
            notes=INGREDIENT_NOTES[RABBIT_SERUM],
        )
    ],
    "solutions": [HEMIN_STOCK],
    "preparation_notes": (
        "Mix 100 ml Sterile Rabbit Serum with 2.5 ml 0.05% Hemin solution and "
        "filter sterilize."
    ),
}


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


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )

        row_label = f"{label}[{index}]"
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{row_label}.composition"),
                _solution_signature(row.get("solutions"), f"{row_label}.solutions"),
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

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _solution_signature(doc.get("solutions"), "solutions")

    if (
        ingredient_signature == IMPORTED_INGREDIENT_SIGNATURE
        and solution_signature == IMPORTED_SOLUTION_SIGNATURE
    ):
        return
    if (
        ingredient_signature == FINAL_INGREDIENT_SIGNATURE
        and solution_signature == FINAL_SOLUTION_SIGNATURE
    ):
        return
    raise ValueError(f"{TARGET}: ingredient or solution signature drifted")


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
            f"{NOTES} Split the migrated Supplement A and 0.05% Hemin solution "
            "rows into nested stocks, corrected milliliter additions, added the "
            "final pH range, and grounded machine-usable components."
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
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.4}, "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = [copy.deepcopy(SUPPLEMENT_A_SOLUTION)]
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(PREPARATION_STEPS)
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
