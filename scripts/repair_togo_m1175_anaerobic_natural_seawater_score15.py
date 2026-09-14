#!/usr/bin/env python3
"""Repair TOGO M1175 / JCM 1102 Anaerobic Natural Seawater Medium."""

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
TARGET = Path("bacterial/anaerobic_natural_seawater_medium.yaml")
EXPECTED_ID = "CultureMech:007700"
EXPECTED_MEDIA_TERM = "TOGO:M1175"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1175_anaerobic_natural_seawater_score15.py"
ACTION = "RESOLVED_TOGO_M1175_ANAEROBIC_NATURAL_SEAWATER"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1175 = "https://togomedium.org/medium/M1175"
JCM_1102 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1102"
REFERENCES = (TOGO_M1175, JCM_1102)
SOURCE = "JCM Medium 1102"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "250", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("Natural seawater (filtrated)", "750", "G_PER_L"),
    ("Tryptone", "5", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone", "5.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Natural seawater (filtrated)", "750.0", "ML_PER_L"),
    ("Distilled water", "250.0", "ML_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

NA2S_STOCK_SIGNATURE: tuple[Component, ...] = (("Na2S x 9H2O", "5.0", "PERCENT_W_V"),)
CYSTEINE_STOCK_SIGNATURE: tuple[Component, ...] = (("L-Cysteine HCl H2O", "5.0", "PERCENT_W_V"),)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("5% Na2S\u30fb9H2O solution", "6", "G_PER_L", ()),
    ("5% L-Cysteine\u30fbHCl\u30fbH2O solution", "6", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (
        "5% L-Cysteine HCl H2O solution",
        "6.0",
        "ML_PER_L",
        CYSTEINE_STOCK_SIGNATURE,
    ),
    ("5% Na2S x 9H2O solution", "6.0", "ML_PER_L", NA2S_STOCK_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

NOTES = (
    "TOGO M1175 records JCM Medium 1102 as an anaerobic natural seawater base "
    "containing tryptone, yeast extract, resazurin, filtered natural seawater, "
    "distilled water, and an N2 atmosphere; the source adjusts the base to pH "
    "7.0. After autoclaving and cooling, the source adds 6.0 ml/L each 5% "
    "L-Cysteine HCl H2O and 5% Na2S x 9H2O solutions."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix tryptone, yeast extract, resazurin, natural seawater, and " "distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 7.0.",
    },
    {
        "step_number": 3,
        "action": "COOL",
        "description": "Bring the medium to a boil and cool under an N2 gas atmosphere.",
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": (
            "Distribute the medium in culture vessels under N2 and seal with "
            "butyl rubber stoppers."
        ),
    },
    {
        "step_number": 5,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": (
            "After cooling, aseptically and anaerobically add 6.0 ml/L each "
            "5% L-Cysteine HCl H2O and 5% Na2S x 9H2O solutions autoclaved "
            "and stored under N2."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": (
        "JCM's default sterilization is autoclaving at 121 degrees C for 15 "
        "min; JCM Medium 1102 autoclaves the anaerobic base after "
        "distribution under N2."
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
    source: str = SOURCE,
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        row["term"] = _term(*GROUNDINGS[preferred_term])
        row["mediaingredientmech_chebi_term"] = _term(*GROUNDINGS[preferred_term])
    return row


def _percent_stock(
    preferred_term: str,
    value: str,
    solute: str,
    percent: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds {value} ml/L {preferred_term}.",
        "composition": [
            _component(
                solute,
                percent,
                "PERCENT_W_V",
                notes=(
                    f"{preferred_term} is represented from the stock label as "
                    f"{percent}% w/v {solute}."
                ),
            )
        ],
        "preparation_notes": "Autoclave and store under an N2 gas atmosphere.",
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Tryptone", "5.0", "G_PER_L", term=False),
    _component("Yeast extract", "1.0", "G_PER_L", term=False),
    _component("Resazurin", "0.5", "MG_PER_L"),
    _component("Natural seawater (filtrated)", "750.0", "ML_PER_L", term=False),
    _component("Distilled water", "250.0", "ML_PER_L"),
    _component(
        "N2",
        "variable",
        "VARIABLE",
        notes=(
            "JCM Medium 1102 cools the boiled base, distributes the medium, "
            "and stores reducing stocks under an N2 gas atmosphere."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _percent_stock(
        "5% L-Cysteine HCl H2O solution",
        "6.0",
        "L-Cysteine HCl H2O",
        "5.0",
    ),
    _percent_stock(
        "5% Na2S x 9H2O solution",
        "6.0",
        "Na2S x 9H2O",
        "5.0",
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

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
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
        "notes": NOTES,
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "solutions",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "ph_value", 7.0, "sterilization")
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
