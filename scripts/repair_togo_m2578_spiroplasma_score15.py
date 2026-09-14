#!/usr/bin/env python3
"""Repair TOGO M2578 Spiroplasma Medium."""

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
TARGET = Path("bacterial/spiroplasma_medium.yaml")
EXPECTED_ID = "CultureMech:009147"
EXPECTED_MEDIA_TERM = "TOGO:M2578"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2578_spiroplasma_score15.py"
ACTION = "RESOLVED_TOGO_M2578_SPIROPLASMA_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2578 = "https://togomedium.org/medium/M2578"
REFERENCES = (TOGO_M2578,)
SOURCE = "TOGO M2578"
TITLE = "Spiroplasma Medium"

WATER = "DI Water"
AGAR = "Agar"
TRYPTONE = "Tryptone (Difco)"
PPLO = "PPLO Broth w/o  Crystal Violet (Difco)"
FBS = "Fetal bovine serum (heat-inactivated)"
TC_YEASTOLATE_STOCK = "TC Yeastolate (2% soln.) (BD 255772)"
TC_YEASTOLATE = "TC Yeastolate (BD 255772)"
GLUCOSE = "Glucose"
MGS_STOCK = "Mycoplasma Growth Supplement (CMRL 1066)(10X)"
MGS_WATER = "Distilled water"
CMRL = "CMRL-1066 (ATCC 20-2206)"
YEAST_EXTRACT_STOCK = "Yeast Extract Solution"
YEAST_WATER = "Distilled deionized water"
BAKERS_YEAST = "Bakers\u2019 yeast (live, pressed, starch-free)"
PHENOL_RED_STOCK = "Phenol red solution (0.1% soln.)"
PHENOL_RED = "Phenol red"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "700.0", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (TRYPTONE, "10", "G_PER_L"),
    (PPLO, "11", "G_PER_L"),
    (FBS, "170", "G_PER_L"),
    (TC_YEASTOLATE_STOCK, "100", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (MGS_STOCK, "50", "G_PER_L"),
    (MGS_WATER, "100", "G_PER_L"),
    (CMRL, "98", "G_PER_L"),
    (YEAST_WATER, "1", "G_PER_L"),
    (BAKERS_YEAST, "250", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (PHENOL_RED_STOCK, "20", "G_PER_L", ()),
    (YEAST_EXTRACT_STOCK, "35", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "700.0", "ML_PER_L"),
    (AGAR, "15.0", "G_PER_L"),
    (TRYPTONE, "10.0", "G_PER_L"),
    (PPLO, "11.0", "G_PER_L"),
    (FBS, "170.0", "ML_PER_L"),
    (GLUCOSE, "5.0", "G_PER_L"),
)

PHENOL_RED_SIGNATURE: tuple[Component, ...] = ((PHENOL_RED, "0.1", "PERCENT_W_V"),)
TC_YEASTOLATE_SIGNATURE: tuple[Component, ...] = ((TC_YEASTOLATE, "2.0", "PERCENT_W_V"),)
MGS_SIGNATURE: tuple[Component, ...] = (
    (MGS_WATER, "1000.0", "ML_PER_L"),
    (CMRL, "98.0", "G_PER_L"),
)
YEAST_EXTRACT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_WATER, "1000.0", "ML_PER_L"),
    (BAKERS_YEAST, "250.0", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (PHENOL_RED_STOCK, "20.0", "ML_PER_L", PHENOL_RED_SIGNATURE),
    (TC_YEASTOLATE_STOCK, "100.0", "ML_PER_L", TC_YEASTOLATE_SIGNATURE),
    (MGS_STOCK, "50.0", "ML_PER_L", MGS_SIGNATURE),
    (YEAST_EXTRACT_STOCK, "35.0", "ML_PER_L", YEAST_EXTRACT_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    AGAR: ("CHEBI:2509", "agar"),
    TRYPTONE: ("MICRO:0000182", "Tryptone"),
    FBS: ("mediadive.compound:954", "Fetal bovine serum"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    MGS_WATER: ("CHEBI:15377", "water"),
    CMRL: ("mediadive.compound:1680", "CMRL 1066"),
    YEAST_WATER: ("CHEBI:15377", "water"),
    PHENOL_RED: ("CHEBI:31991", "phenol red"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

NOTES = (
    "TOGO M2578 defines Spiroplasma Medium with a basal medium containing "
    "500 ml DI Water, 15 g optional Agar, 10 g Tryptone, and 11 g PPLO Broth "
    "without crystal violet. Its additive solution supplies 170 ml "
    "heat-inactivated fetal bovine serum, 20 ml 0.1% Phenol red solution, "
    "100 ml 2% TC Yeastolate, 200 ml DI Water, 5 g Glucose, 50 ml "
    "Mycoplasma Growth Supplement made from 98 g CMRL-1066 in 1.0 L water, "
    "and 35 ml Yeast Extract Solution made from 250 g baker's yeast in 1.0 L "
    "water. The basal medium is adjusted to pH 7.3-7.4, autoclaved at 121 C "
    "for 15 minutes, combined with the filter-sterilized additive solution, "
    "and readjusted if needed to pH 7.35 +/- 0.1."
)


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
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        term = _term(*grounding)
        row["term"] = term
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _stock_component_note(
    stock: str,
    component: str,
    amount: str,
    unit: str,
) -> str:
    return f"{SOURCE} identifies {stock} as containing {amount} {UNIT_LABELS[unit]} {component}."


def _stock(
    preferred_term: str,
    value: str,
    composition: tuple[Component, ...],
    *,
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": [
            _component(
                component,
                amount,
                unit,
                notes=_stock_component_note(preferred_term, component, amount, unit),
            )
            for component, amount, unit in composition
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        WATER,
        "700.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 500 ml/L DI Water in the basal medium and 200 ml/L "
            "DI Water in the additive solution."
        ),
    ),
    _component(
        AGAR,
        "15.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 15 g/L Agar if solid medium is required.",
    ),
    _component(
        TRYPTONE,
        "10.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 10 g/L Tryptone from Difco.",
    ),
    _component(
        PPLO,
        "11.0",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 11 g/L PPLO Broth without crystal violet from "
            "Difco; this commercial broth is retained as an opaque complex "
            "component."
        ),
    ),
    _component(
        FBS,
        "170.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 170 ml/L heat-inactivated fetal bovine serum; "
            "this serum is retained as an opaque complex component."
        ),
    ),
    _component(GLUCOSE, "5.0", "G_PER_L"),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        PHENOL_RED_STOCK,
        "20.0",
        PHENOL_RED_SIGNATURE,
        notes=f"{SOURCE} lists 20 ml/L 0.1% Phenol red solution.",
    ),
    _stock(
        TC_YEASTOLATE_STOCK,
        "100.0",
        TC_YEASTOLATE_SIGNATURE,
        notes=(
            f"{SOURCE} lists 100 ml/L 2% TC Yeastolate from BD 255772; "
            "the yeastolate is retained as an opaque complex component."
        ),
    ),
    _stock(
        MGS_STOCK,
        "50.0",
        MGS_SIGNATURE,
        notes=(
            f"{SOURCE} lists 50 ml/L Mycoplasma Growth Supplement and directs "
            "preparing its 10x stock from 98 g CMRL-1066 powder in 1.0 L "
            "water, then filter-sterilizing it."
        ),
    ),
    _stock(
        YEAST_EXTRACT_STOCK,
        "35.0",
        YEAST_EXTRACT_SIGNATURE,
        notes=(
            f"{SOURCE} lists 35 ml/L Yeast Extract Solution prepared from "
            "250 g live baker's yeast in 1.0 L water; the source autoclaves "
            "this stock, removes the supernatant, and adjusts the pH to 6.6-6.8."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix DI Water, Agar if required, Tryptone, and PPLO Broth without "
            "crystal violet as the basal medium."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the basal medium to pH 7.3-7.4.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave the basal medium at 121 C for 15 minutes, then cool to "
            "50-55 C in a water bath if agar is used."
        ),
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": (
            "Prepare the additive solution from heat-inactivated fetal bovine "
            "serum, Phenol red solution, TC Yeastolate, DI Water, Glucose, "
            "Mycoplasma Growth Supplement, and Yeast Extract Solution, then "
            "filter-sterilize it."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Combine the filter-sterilized additive solution with the basal "
            "medium and, if needed, readjust the pH to 7.35 +/- 0.1."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "Autoclave the basal medium before adding the filter-sterilized additive solution.",
}


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


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

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(
            f"{TARGET}: solution signature drifted from "
            f"{IMPORTED_SOLUTION_SIGNATURES!r} to {solution_signatures!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected imported milliliter quantities, restored "
            "the Mycoplasma Growth Supplement and Yeast Extract Solution "
            "stock compositions, moved TC Yeastolate from the ingredient list "
            "to a 2% stock solution, and added the TOGO pH and sterilization "
            "instructions."
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
    _put_after(repaired, "ph_range", {"min": 7.25, "max": 7.45}, "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "ingredients",
    )
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
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
