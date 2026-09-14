#!/usr/bin/env python3
"""Repair TOGO M1485 Modified Hayflick Medium."""

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
TARGET = Path("bacterial/modified_hayflick_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008029"
EXPECTED_MEDIA_TERM = "TOGO:M1485"

CURATOR = "repair_togo_m1485_modified_hayflick_score15.py"
ACTION = "RESOLVED_TOGO_M1485_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1485 = "https://togomedium.org/medium/M1485"
NBRC_267 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=267"
SOURCE = "TOGO M1485 / NBRC Medium 267"
TITLE = "Modified Hayflick Medium"

WATER = "Distilled water"
BACTO_AGAR = "Bacto Agar (Difco, if needed)"
HEART_INFUSION = "Bacto Heart Infusion Broth (Difco)"
CALF_THYMUS_DNA = "calf thymus DNA (Sigma, Type I)"
THALLIUM_ACETATE = "thallium acetate"
HORSE_SERUM = "horse serum (heat inactivated, 56℃ for 30 minutes)"
PENICILLIN_G = "Penicillin G"
FRESH_YEAST_EXTRACT = "fresh yeast extract (25% solution)"
BAKERS_YEAST = "dried baker's yeast"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "701.0", "G_PER_L"),
    (BACTO_AGAR, "15", "G_PER_L"),
    (HEART_INFUSION, "25", "G_PER_L"),
    (CALF_THYMUS_DNA, "12", "G_PER_L"),
    (THALLIUM_ACETATE, "10", "G_PER_L"),
    (HORSE_SERUM, "200", "G_PER_L"),
    (PENICILLIN_G, "25", "G_PER_L"),
    (BAKERS_YEAST, "250", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = ((FRESH_YEAST_EXTRACT, "100", "G_PER_L"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "700.0", "ML_PER_L"),
    (BACTO_AGAR, "15.0", "G_PER_L"),
    (HEART_INFUSION, "25.0", "G_PER_L"),
    (CALF_THYMUS_DNA, "12.0", "ML_PER_L"),
    (THALLIUM_ACETATE, "10.0", "ML_PER_L"),
    (HORSE_SERUM, "200.0", "ML_PER_L"),
    (PENICILLIN_G, "25.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = ((FRESH_YEAST_EXTRACT, "100.0", "ML_PER_L"),)

YEAST_STOCK_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1.0", "L"),
    (BAKERS_YEAST, "250.0", "G_PER_L"),
)

REFERENCES = (TOGO_M1485, NBRC_267)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    BACTO_AGAR: ("CHEBI:2509", "agar"),
    THALLIUM_ACETATE: ("CHEBI:75192", "Thallium(I) acetate"),
    HORSE_SERUM: ("MICRO:0001235", "Horse serum"),
    PENICILLIN_G: ("CHEBI:51765", "benzylpenicillin sodium"),
    BAKERS_YEAST: ("FOODON:03413797", "Baker's yeast"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        WATER,
        BACTO_AGAR,
        THALLIUM_ACETATE,
        PENICILLIN_G,
    }
)

NOTES = (
    "TOGO M1485 imports NBRC Medium 267 as Modified Hayflick Medium. NBRC 267 "
    "lists 25 g Bacto Heart Infusion Broth, 700 ml distilled water, 15 g Bacto "
    "Agar if needed, pH 7.8, autoclaving at 121 C for 20 min, and aseptic "
    "addition of 200 ml heat-inactivated horse serum, 100 ml fresh yeast "
    "extract, 12 ml calf thymus DNA, 10 ml thallium acetate, and 25 ml "
    "Penicillin G."
)

INGREDIENT_NOTES = {
    WATER: "TOGO M1485 / NBRC Medium 267 lists 700 ml/L Distilled water.",
    BACTO_AGAR: (
        "TOGO M1485 / NBRC Medium 267 lists 15 g/L Bacto Agar from Difco "
        "if a solid medium is needed."
    ),
    HEART_INFUSION: (
        "TOGO M1485 / NBRC Medium 267 lists 25 g/L Bacto Heart Infusion "
        "Broth from Difco; this catalog broth is retained as an opaque component."
    ),
    CALF_THYMUS_DNA: (
        "TOGO M1485 / NBRC Medium 267 lists 12 ml/L calf thymus DNA from "
        "Sigma Type I as a 0.2% w/v stock; this source-qualified DNA product "
        "remains intentionally unmapped."
    ),
    THALLIUM_ACETATE: (
        "TOGO M1485 / NBRC Medium 267 lists 10 ml/L thallium acetate as a " "1% w/v stock."
    ),
    HORSE_SERUM: (
        "TOGO M1485 / NBRC Medium 267 lists 200 ml/L horse serum heat "
        "inactivated at 56 C for 30 minutes."
    ),
    PENICILLIN_G: (
        "TOGO M1485 / NBRC Medium 267 lists 25 ml/L Penicillin G as a " "20,000 IU/ml stock."
    ),
}

SOLUTION_NOTES = {
    FRESH_YEAST_EXTRACT: (
        "TOGO M1485 / NBRC Medium 267 adds 100 ml/L fresh yeast extract "
        "prepared as a 25% solution."
    ),
    WATER: (
        "TOGO M1485 / NBRC Medium 267 prepares the 25% fresh yeast extract "
        "with 1 L Distilled water."
    ),
    BAKERS_YEAST: (
        "TOGO M1485 / NBRC Medium 267 boils 250 g dried baker's yeast per "
        "liter to prepare 25% fresh yeast extract."
    ),
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Combine 25 g Bacto Heart Infusion Broth and 700 ml distilled water; "
            "add 15 g Bacto Agar if a solid medium is needed."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the base to pH 7.8.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 20 min.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Aseptically add heat-inactivated horse serum, fresh yeast extract, "
            "calf thymus DNA, thallium acetate, and Penicillin G."
        ),
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": "NBRC Medium 267 autoclaves the base at 121 C for 20 min.",
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

FRESH_YEAST_SOLUTION = {
    "preferred_term": FRESH_YEAST_EXTRACT,
    "concentration": {"value": "100.0", "unit": "ML_PER_L"},
    "source": SOURCE,
    "notes": SOLUTION_NOTES[FRESH_YEAST_EXTRACT],
    "composition": [
        _component(
            name,
            value,
            unit,
            source=f"{SOURCE} fresh yeast extract stock",
            notes=SOLUTION_NOTES[name],
        )
        for name, value, unit in YEAST_STOCK_SIGNATURE
    ],
    "preparation_notes": (
        "Boil 250 g of dried baker's yeast suspended in 1 L of distilled water "
        "for 30 min, remove yeast cells by centrifugation, and sterilize by "
        "filtration."
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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_composition_signature(rows: Any) -> tuple[Component, ...]:
    if not rows:
        return ()
    if not isinstance(rows, list) or len(rows) != 1:
        raise ValueError(f"{TARGET}: expected exactly one fresh yeast solution")
    solution = rows[0]
    if not isinstance(solution, dict):
        raise ValueError(f"{TARGET}: solution row is not a mapping")
    return _signature(solution.get("composition"), "solutions[0].composition")


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
    solution_signature = _signature(doc.get("solutions"), "solutions")
    solution_composition_signature = _solution_composition_signature(doc.get("solutions"))

    if (
        ingredient_signature == IMPORTED_INGREDIENT_SIGNATURE
        and solution_signature == IMPORTED_SOLUTION_SIGNATURE
        and not solution_composition_signature
    ):
        return
    if (
        ingredient_signature == FINAL_INGREDIENT_SIGNATURE
        and solution_signature == FINAL_SOLUTION_SIGNATURE
        and solution_composition_signature == YEAST_STOCK_SIGNATURE
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
            f"{NOTES} Split the merged water row back into the 700 ml/L "
            "base water and the 1 L fresh-yeast-extract stock water, restored "
            "the fresh yeast extract stock composition, corrected stock "
            "addition volumes, added pH 7.8, and grounded machine-usable "
            "ingredients."
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
    _put_after(repaired, "ph_value", 7.8, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = [copy.deepcopy(FRESH_YEAST_SOLUTION)]
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
