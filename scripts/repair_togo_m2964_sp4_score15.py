#!/usr/bin/env python3
"""Repair TOGO M2964 SP-4 medium."""

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
TARGET = Path("bacterial/sp_4_medium.yaml")
EXPECTED_ID = "CultureMech:009489"
EXPECTED_MEDIA_TERM = "TOGO:M2964"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2964_sp4_score15.py"
ACTION = "RESOLVED_TOGO_M2964_SP4_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2964 = "https://togomedium.org/medium/M2964"
REFERENCES = (TOGO_M2964,)
SOURCE = "TOGO M2964"
TITLE = "SP-4 medium"

WATER = "De-ionized water"
GLUCOSE = "Glucose"
BACTO_TRYPTONE = "Bacto Tryptone"
BACTO_PEPTONE = "Bacto Peptone"
MYCOPLASMA_BROTH = "Mycoplasma Broth Base"
FBS = "Fetal bovine serum (heated 56\u00b0C- I hour)"
PHENOL_RED_STOCK = "Phenol red (0.1% aqueous)"
YEASTOLATE_STOCK = "Yeastolate (2% solution) (Difco)"
PENICILLIN_STOCK = "Penicillin G (100,000 units/ml)"
POLYMYXIN_STOCK = "Polymyxin B (100,000 units/ml) (optional)"
FRESH_YEAST_STOCK = "Fresh yeast extract (25% solution)"
THALLIUM_STOCK = "Thallium acetate (1:50 solution)"
CMRL = "CMRL 1066 tissue culture supplement- (10x)(with glutamine)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "560", "G_PER_L"),
    (GLUCOSE, "5", "G_PER_L"),
    (BACTO_TRYPTONE, "10", "G_PER_L"),
    (BACTO_PEPTONE, "5.3", "G_PER_L"),
    (MYCOPLASMA_BROTH, "3.5", "G_PER_L"),
    (FBS, "170", "G_PER_L"),
    (PHENOL_RED_STOCK, "20", "G_PER_L"),
    (PENICILLIN_STOCK, "10", "G_PER_L"),
    (POLYMYXIN_STOCK, "5", "G_PER_L"),
    (CMRL, "50", "G_PER_L"),
)
IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (YEASTOLATE_STOCK, "100", "G_PER_L", ()),
    (FRESH_YEAST_STOCK, "35", "G_PER_L", ()),
    (THALLIUM_STOCK, "50", "G_PER_L", ()),
)

PHENOL_RED_SIGNATURE: tuple[Component, ...] = (("Phenol red", "0.1", "PERCENT_W_V"),)
YEASTOLATE_SIGNATURE: tuple[Component, ...] = (("Yeastolate", "2.0", "PERCENT_W_V"),)
PENICILLIN_SIGNATURE: tuple[Component, ...] = (("Penicillin G", "variable", "VARIABLE"),)
POLYMYXIN_SIGNATURE: tuple[Component, ...] = (("Polymyxin B", "variable", "VARIABLE"),)
FRESH_YEAST_SIGNATURE: tuple[Component, ...] = (("Fresh yeast extract", "25.0", "PERCENT_W_V"),)
THALLIUM_SIGNATURE: tuple[Component, ...] = (("Thallium acetate", "2.0", "PERCENT_W_V"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "560.0", "ML_PER_L"),
    (GLUCOSE, "5.0", "G_PER_L"),
    (BACTO_TRYPTONE, "10.0", "G_PER_L"),
    (BACTO_PEPTONE, "5.3", "G_PER_L"),
    (MYCOPLASMA_BROTH, "3.5", "G_PER_L"),
    (FBS, "170.0", "ML_PER_L"),
    (CMRL, "50.0", "ML_PER_L"),
)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (PHENOL_RED_STOCK, "20.0", "ML_PER_L", PHENOL_RED_SIGNATURE),
    (YEASTOLATE_STOCK, "100.0", "ML_PER_L", YEASTOLATE_SIGNATURE),
    (PENICILLIN_STOCK, "10.0", "ML_PER_L", PENICILLIN_SIGNATURE),
    (POLYMYXIN_STOCK, "5.0", "ML_PER_L", POLYMYXIN_SIGNATURE),
    (FRESH_YEAST_STOCK, "35.0", "ML_PER_L", FRESH_YEAST_SIGNATURE),
    (THALLIUM_STOCK, "50.0", "ML_PER_L", THALLIUM_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    BACTO_PEPTONE: ("MICRO:0000178", "Bacto peptone"),
    FBS: ("mediadive.compound:954", "Fetal bovine serum"),
    CMRL: ("mediadive.compound:1680", "CMRL 1066"),
    "Phenol red": ("CHEBI:31991", "phenol red"),
    "Penicillin G": ("CHEBI:51765", "benzylpenicillin sodium"),
    "Polymyxin B": ("CHEBI:759086", "polymyxin b"),
    "Thallium acetate": ("CHEBI:75192", "thallium(I) acetate"),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable amount of",
}

NOTES = (
    "TOGO M2964 defines SP-4 medium with 560 ml De-ionized water, 5 g Glucose, "
    "10 g Bacto Tryptone, 5.3 g Bacto Peptone, 3.5 g Mycoplasma Broth Base, "
    "170 ml heat-treated Fetal bovine serum, 20 ml 0.1% Phenol red, 100 ml "
    "2% Difco Yeastolate, 10 ml Penicillin G at 100000 units/ml, optional "
    "5 ml Polymyxin B at 100000 units/ml, 35 ml Fresh yeast extract at 25%, "
    "50 ml 1:50 Thallium acetate, and 50 ml CMRL 1066 tissue culture "
    "supplement. The TOGO comments direct adjusting to pH 7.5-7.6, "
    "sterilizing at 121 C for 15 minutes, and record a final pH of 7.4-7.5."
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
    if unit == "VARIABLE":
        return (
            f"{SOURCE} identifies {stock} as an activity-unit {component} stock; "
            "the exact mass concentration is variable."
        )
    return f"{SOURCE} identifies {stock} as {amount} {UNIT_LABELS[unit]} {component}."


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
    _component(WATER, "560.0", "ML_PER_L"),
    _component(GLUCOSE, "5.0", "G_PER_L"),
    _component(
        BACTO_TRYPTONE,
        "10.0",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 10 g/L Bacto Tryptone; this commercial pancreatic "
            "casein digest is retained as an opaque complex component."
        ),
    ),
    _component(BACTO_PEPTONE, "5.3", "G_PER_L"),
    _component(
        MYCOPLASMA_BROTH,
        "3.5",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 3.5 g/L Mycoplasma Broth Base; this commercial "
            "broth base is retained as an opaque complex component."
        ),
    ),
    _component(
        FBS,
        "170.0",
        "ML_PER_L",
        notes=(f"{SOURCE} lists 170 ml/L fetal bovine serum heated at 56 C for 1 hour."),
    ),
    _component(
        CMRL,
        "50.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 50 ml/L CMRL 1066 tissue culture supplement; this "
            "10x commercial supplement is retained as an opaque complex component."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        PHENOL_RED_STOCK,
        "20.0",
        PHENOL_RED_SIGNATURE,
        notes=f"{SOURCE} lists 20 ml/L 0.1% aqueous Phenol red.",
    ),
    _stock(
        YEASTOLATE_STOCK,
        "100.0",
        YEASTOLATE_SIGNATURE,
        notes=(
            f"{SOURCE} lists 100 ml/L 2% Yeastolate solution from Difco; the "
            "yeastolate is retained as an opaque complex component."
        ),
    ),
    _stock(
        PENICILLIN_STOCK,
        "10.0",
        PENICILLIN_SIGNATURE,
        notes=(
            f"{SOURCE} lists 10 ml/L Penicillin G at 100000 units/ml; the "
            "stock concentration is retained as variable because the schema "
            "has no activity-unit concentration."
        ),
    ),
    _stock(
        POLYMYXIN_STOCK,
        "5.0",
        POLYMYXIN_SIGNATURE,
        notes=(
            f"{SOURCE} lists optional 5 ml/L Polymyxin B at 100000 units/ml; "
            "the stock concentration is retained as variable because the "
            "schema has no activity-unit concentration."
        ),
    ),
    _stock(
        FRESH_YEAST_STOCK,
        "35.0",
        FRESH_YEAST_SIGNATURE,
        notes=(
            f"{SOURCE} lists 35 ml/L 25% Fresh yeast extract; the fresh yeast "
            "extract is retained as an opaque complex component."
        ),
    ),
    _stock(
        THALLIUM_STOCK,
        "50.0",
        THALLIUM_SIGNATURE,
        notes=f"{SOURCE} lists 50 ml/L 1:50 Thallium acetate solution.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix De-ionized water, Glucose, Bacto Tryptone, Bacto Peptone, "
            "and Mycoplasma Broth Base as the basal medium."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the basal medium to pH 7.5-7.6.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Sterilize the basal medium at 121 C for 15 minutes.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Add fetal bovine serum, Phenol red, Yeastolate, Penicillin G, "
            "optional Polymyxin B, Fresh yeast extract, Thallium acetate, and "
            "CMRL 1066 tissue culture supplement."
        ),
    },
)


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

    kg_match = doc.get("kg_microbe_match")
    if kg_match not in (None, "mediadive.medium:21"):
        raise ValueError(f"{TARGET}: unexpected kg_microbe_match {kg_match!r}")


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
            f"{NOTES} Corrected imported ml additions, moved stock solutions "
            "into the solutions array with disclosed compositions where "
            "available, added the source pH and autoclave instructions, and "
            "removed kg_microbe_match mediadive.medium:21 because MediaDive "
            "medium 21 is Sarcina Medium."
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
    _put_after(repaired, "ph_range", {"min": 7.4, "max": 7.6}, "physical_state")
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
    repaired["sterilization"] = {"method": "AUTOCLAVE"}
    repaired.pop("kg_microbe_match", None)
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
