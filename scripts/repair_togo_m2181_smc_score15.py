#!/usr/bin/env python3
"""Repair TOGO M2181 / ATCC Medium 668 SMC medium."""

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
TARGET = Path("bacterial/smc_medium.yaml")
EXPECTED_ID = "CultureMech:008776"
EXPECTED_MEDIA_TERM = "TOGO:M2181"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2181_smc_score15.py"
ACTION = "RESOLVED_TOGO_M2181_SMC_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2181 = "https://togomedium.org/medium/M2181"
ATCC_668 = "https://www.atcc.org/~/media/6ACA1A2B1C7A47EFA575372A421E1E77.ashx"
REFERENCES = (TOGO_M2181, ATCC_668)
SOURCE = "TOGO M2181 / ATCC Medium 668"
TITLE = "SMC medium"

WATER = "Distilled water"
SORBITOL = "Sorbitol"
TRYPTONE = "Tryptone (BD 211705)"
PPLO = "PPLO Broth w/o CV (Mycoplasma Broth) (BD 255420)"
ARGININE_STOCK = "42% L-Arginine HCl"
HORSE_SERUM = "Horse serum"
YEAST_STOCK = "Yeast Extract Solution (GIBCO 360-8180)"
PHENOL_RED_STOCK = "0.1% Phenol red solution"
FRUCTOSE_STOCK = "50% Fructose solution"
GLUCOSE_STOCK = "50% Glucose solution"
SUCROSE_STOCK = "50% Sucrose solution"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "650", "G_PER_L"),
    (SORBITOL, "70", "G_PER_L"),
    (TRYPTONE, "10", "G_PER_L"),
    (PPLO, "21", "G_PER_L"),
    (ARGININE_STOCK, "10", "G_PER_L"),
    (HORSE_SERUM, "200", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (PHENOL_RED_STOCK, "20", "G_PER_L", ()),
    (FRUCTOSE_STOCK, "2", "G_PER_L", ()),
    (GLUCOSE_STOCK, "2", "G_PER_L", ()),
    (SUCROSE_STOCK, "20", "G_PER_L", ()),
    (YEAST_STOCK, "100", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (PPLO, "21.0", "G_PER_L"),
    (TRYPTONE, "10.0", "G_PER_L"),
    (SORBITOL, "70.0", "G_PER_L"),
    (WATER, "650.0", "ML_PER_L"),
    (HORSE_SERUM, "200.0", "ML_PER_L"),
)

ARGININE_SIGNATURE: tuple[Component, ...] = (("L-Arginine HCl", "42.0", "PERCENT_W_V"),)
PHENOL_RED_SIGNATURE: tuple[Component, ...] = (("Phenol red", "0.1", "PERCENT_W_V"),)
FRUCTOSE_SIGNATURE: tuple[Component, ...] = (("Fructose", "50.0", "PERCENT_W_V"),)
GLUCOSE_SIGNATURE: tuple[Component, ...] = (("Glucose", "50.0", "PERCENT_W_V"),)
SUCROSE_SIGNATURE: tuple[Component, ...] = (("Sucrose", "50.0", "PERCENT_W_V"),)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (YEAST_STOCK, "100.0", "ML_PER_L", ()),
    (FRUCTOSE_STOCK, "2.0", "ML_PER_L", FRUCTOSE_SIGNATURE),
    (SUCROSE_STOCK, "20.0", "ML_PER_L", SUCROSE_SIGNATURE),
    (GLUCOSE_STOCK, "2.0", "ML_PER_L", GLUCOSE_SIGNATURE),
    (ARGININE_STOCK, "10.0", "ML_PER_L", ARGININE_SIGNATURE),
    (PHENOL_RED_STOCK, "20.0", "ML_PER_L", PHENOL_RED_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    SORBITOL: ("CHEBI:30911", "glucitol"),
    TRYPTONE: ("MICRO:0000182", "Tryptone"),
    HORSE_SERUM: ("MICRO:0001235", "Horse serum"),
    "L-Arginine HCl": ("CHEBI:31235", "L-Arginine x HCl"),
    "Phenol red": ("CHEBI:31991", "phenol red"),
    "Fructose": ("CHEBI:28757", "fructose"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Sucrose": ("CHEBI:17992", "sucrose"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

NOTES = (
    "TOGO M2181 cites ATCC Medium 668 SMC medium. ATCC Medium 668 lists a "
    "basal recipe with 21.0 g PPLO Broth w/o CV from BD 255420, 10.0 g "
    "Tryptone from BD 211705, 70.0 g Sorbitol, and 650.0 ml Distilled water; "
    "the pH is adjusted to 7.5 and the base is autoclaved at 121 C for 15 "
    "minutes. The source then filter-sterilizes and aseptically adds 200.0 ml "
    "Horse serum, 100.0 ml Yeast Extract Solution from GIBCO 360-8180, 2.0 ml "
    "50% Fructose solution, 20.0 ml 50% Sucrose solution, 2.0 ml 50% Glucose "
    "solution, 10.0 ml 42% L-Arginine HCl, and 20.0 ml 0.1% Phenol red "
    "solution."
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
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _stock_solution(
    preferred_term: str,
    value: str,
    signature: tuple[Component, ...],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} aseptically adds {value} ml/L {preferred_term}.",
        "composition": [
            _component(
                component,
                amount,
                unit,
                notes=(
                    f"{SOURCE} identifies {preferred_term} as a "
                    f"{amount} {UNIT_LABELS[unit]} {component} stock."
                ),
            )
            for component, amount, unit in signature
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        PPLO,
        "21.0",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 21.0 g PPLO Broth w/o CV from BD catalog 255420; "
            "the commercial broth is retained as an opaque complex component."
        ),
    ),
    _component(TRYPTONE, "10.0", "G_PER_L"),
    _component(SORBITOL, "70.0", "G_PER_L"),
    _component(WATER, "650.0", "ML_PER_L"),
    _component(
        HORSE_SERUM,
        "200.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 200.0 ml horse serum; this serum is retained as "
            "an opaque complex component."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": YEAST_STOCK,
        "concentration": {"value": "100.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"{SOURCE} lists 100.0 ml {YEAST_STOCK}; this GIBCO yeast extract "
            "solution is retained as an opaque complex component because the "
            "ATCC source does not disclose its stock composition."
        ),
        "composition": [],
    },
    _stock_solution(FRUCTOSE_STOCK, "2.0", FRUCTOSE_SIGNATURE),
    _stock_solution(SUCROSE_STOCK, "20.0", SUCROSE_SIGNATURE),
    _stock_solution(GLUCOSE_STOCK, "2.0", GLUCOSE_SIGNATURE),
    _stock_solution(ARGININE_STOCK, "10.0", ARGININE_SIGNATURE),
    _stock_solution(PHENOL_RED_STOCK, "20.0", PHENOL_RED_SIGNATURE),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix PPLO Broth w/o CV, Tryptone, Sorbitol, and Distilled water as the basal medium."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the basal medium to pH 7.5.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal medium at 121 C for 15 minutes.",
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": (
            "Filter-sterilize the serum, yeast extract, sugar, arginine HCl, "
            "and phenol red additions."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": "Aseptically add the filtered stocks to the sterile basal medium.",
    },
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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported ml additions, added the ATCC pH "
            "and sterilization instructions, moved disclosed stocks into "
            "solutions with compositions, and kept PPLO broth, horse serum, "
            "and the GIBCO yeast extract solution as curated opaque inputs."
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
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}
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
