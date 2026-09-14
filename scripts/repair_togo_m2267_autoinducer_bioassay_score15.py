#!/usr/bin/env python3
"""Repair TOGO M2267 Autoinducer Bioassay (AB) Medium."""

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
TARGET = Path("bacterial/autoinducer_bioassay_ab_medium.yaml")
EXPECTED_ID = "CultureMech:008854"
EXPECTED_MEDIA_TERM = "TOGO:M2267"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2267_autoinducer_bioassay_score15.py"
ACTION = "RESOLVED_TOGO_M2267_AUTOINDUCER_BIOASSAY_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2267 = "https://togomedium.org/medium/M2267"
ATCC_2746 = "https://www.atcc.org/~/media/F0C5AC9D96C345049F8AA78CCC2AB46A.ashx"
REFERENCES = (TOGO_M2267, ATCC_2746)

SOURCE = "ATCC Medium 2746"
TITLE = "Autoinducer Bioassay (AB) Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Base Medium", "970", "G_PER_L"),
    ("NaCl", "17.5", "G_PER_L"),
    ("MgSO4", "12.3", "G_PER_L"),
    ("DI Water", "970", "G_PER_L"),
    ("Casamino Acids", "2", "G_PER_L"),
    ("3N NaOH", "variable", "VARIABLE"),
    ("1M Potassium Phosphate (pH 7.0)", "10", "G_PER_L"),
    ("0.1M L-arginine", "10", "G_PER_L"),
    ("Glycerol", "10", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Stock Solutions", "30", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "17.5", "G_PER_L"),
    ("MgSO4", "12.3", "G_PER_L"),
    ("Casamino Acids", "2.0", "G_PER_L"),
    ("DI Water", "970.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("3 N NaOH", "variable", "VARIABLE", (("NaOH", "3.0", "MOLAR"),)),
    ("Potassium phosphate buffer", "10.0", "ML_PER_L", ()),
    (
        "L-Arginine solution",
        "10.0",
        "ML_PER_L",
        (("L-Arginine", "0.1", "MOLAR"),),
    ),
    ("Glycerol", "10.0", "ML_PER_L", ()),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "DI Water": ("CHEBI:15377", "water"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "L-Arginine": ("CHEBI:16467", "L-arginine"),
    "MgSO4": ("CHEBI:32599", "magnesium sulfate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "VARIABLE": "variable",
}

NOTES = (
    "TOGO M2267 imports ATCC Medium 2746, Autoinducer Bioassay (AB) "
    "Medium. ATCC prepares a 970 ml base from NaCl, MgSO4, Casamino "
    "Acids, and DI Water, adjusts the pH to 7.5 with 3 N NaOH, "
    "autoclaves the base at 121 C, cools it completely, and adds 10 ml "
    "each 1 M Potassium Phosphate (pH 7.0), 0.1 M L-arginine, and "
    "Glycerol from separate sterile stocks."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Dissolve NaCl, MgSO4, and Casamino Acids in DI Water.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Bring the pH of the base solution to 7.5 with 3 N NaOH.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base at 121 C.",
    },
    {
        "step_number": 4,
        "action": "COOL",
        "description": "Cool the autoclaved base completely.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Add 10.0 ml/L each 1 M Potassium Phosphate (pH 7.0), "
            "0.1 M L-arginine, and Glycerol from separate sterile stocks."
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


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        row["term"] = _term(*GROUNDINGS[preferred_term])
        row["mediaingredientmech_chebi_term"] = _term(*GROUNDINGS[preferred_term])
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("NaCl", "17.5", "G_PER_L"),
    _component("MgSO4", "12.3", "G_PER_L"),
    _component("Casamino Acids", "2.0", "G_PER_L", term=False),
    _component(
        "DI Water",
        "970.0",
        "ML_PER_L",
        notes=f"{SOURCE} lists 970 ml DI Water in the base.",
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "3 N NaOH",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE,
        "notes": f"{SOURCE} adjusts the base to pH 7.5 with 3 N NaOH.",
        "term": _term(*GROUNDINGS["NaOH"]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS["NaOH"]),
        "composition": [
            _component(
                "NaOH",
                "3.0",
                "MOLAR",
                notes=(
                    "The source uses 3 N NaOH for pH adjustment; for this "
                    "monovalent base the stock is represented as 3.0 M NaOH."
                ),
            )
        ],
    },
    {
        "preferred_term": "Potassium phosphate buffer",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "ATCC Medium 2746 adds 10 ml/L 1 M Potassium Phosphate "
            "(pH 7.0) from a separate sterile stock; the KH2PO4/K2HPO4 "
            "ratio is not disclosed."
        ),
    },
    {
        "preferred_term": "L-Arginine solution",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 10 ml/L 0.1 M L-arginine.",
        "term": _term(*GROUNDINGS["L-Arginine"]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS["L-Arginine"]),
        "composition": [
            _component(
                "L-Arginine",
                "0.1",
                "MOLAR",
                notes=f"{SOURCE} lists 0.1 M L-arginine as a sterile stock.",
            )
        ],
    },
    _component(
        "Glycerol",
        "10.0",
        "ML_PER_L",
        notes=f"{SOURCE} adds 10 ml/L Glycerol from a separate sterile stock.",
    ),
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
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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
    if "references" not in doc:
        _put_after(doc, "references", [], "notes")

    references = doc["references"]
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
            "Corrected TOGO's imported Base Medium and Stock Solutions "
            "wrappers into ATCC's base recipe plus sterile stock additions, "
            "fixed ml rows imported as g/L, added pH 7.5 and source "
            "preparation steps, grounded NaOH and L-arginine stocks, and "
            "kept the pH 7.0 potassium phosphate buffer ratio intentionally "
            "unexpanded."
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "ph_value", 7.5, "physical_state")
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
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
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
