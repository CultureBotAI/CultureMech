#!/usr/bin/env python3
"""Repair TOGO M1297 Marinitoga Hydrogenitolerans Medium."""

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
TARGET = Path("bacterial/TOGO_M1297_Marinitoga_Hydrogenitolerans_Medium.yaml")
EXPECTED_ID = "CultureMech:007830"
EXPECTED_MEDIA_TERM = "TOGO:M1297"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1297_score15.py"
ACTION = "RESOLVED_TOGO_M1297_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1297 = "https://togomedium.org/medium/M1297"
JCM_1210 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1210"
MEDIADIVE_J1210 = "https://mediadive.dsmz.de/rest/medium/J1210"

SOURCE = "TOGO M1297 / JCM Medium 1210"
TITLE = "Marinitoga Hydrogenitolerans Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("MES", "4", "G_PER_L"),
    ("Sea salts (Sigma)", "30", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1", "G_PER_L"),
    ("Yeast extract (Oxoid)", "1", "G_PER_L"),
    ("N2", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Sea salts (Sigma)", "30.0", "G_PER_L"),
    ("MES", "4.0", "G_PER_L"),
    ("Yeast extract (Oxoid)", "1.0", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1.0", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("N2", "variable", "VARIABLE"),
)

GLUCOSE_STOCK_SIGNATURE: tuple[Component, ...] = (("Glucose", "1.0", "MOLAR"),)
NA2S_STOCK_SIGNATURE: tuple[Component, ...] = (("Na2S x 9H2O", "5.0", "PERCENT_W_V"),)
CYSTEINE_STOCK_SIGNATURE: tuple[Component, ...] = (("L-Cysteine HCl H2O", "5.0", "PERCENT_W_V"),)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1.0 M Glucose solution", "14", "G_PER_L", ()),
    ("5% Na2S\u30fb9H2O solution", "10", "G_PER_L", ()),
    ("5% L-Cysteine\u30fbHCl\u30fbH2O solution", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1.0 M Glucose solution", "14.0", "ML_PER_L", GLUCOSE_STOCK_SIGNATURE),
    ("5% Na2S x 9H2O solution", "10.0", "ML_PER_L", NA2S_STOCK_SIGNATURE),
    (
        "5% L-Cysteine HCl H2O solution",
        "10.0",
        "ML_PER_L",
        CYSTEINE_STOCK_SIGNATURE,
    ),
)

REFERENCES = (TOGO_M1297, JCM_1210, MEDIADIVE_J1210)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "MES": ("CHEBI:39005", "2-(N-morpholino)ethanesulfonic acid"),
    "N2": ("CHEBI:17997", "dinitrogen"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
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
    notes: str,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        notes=f"JCM Medium 1210 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _stock(
    preferred_term: str,
    value: str,
    signature: tuple[Component, ...],
) -> dict[str, Any]:
    stock_component, stock_value, stock_unit = signature[0]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            f"JCM Medium 1210 adds {value} ml/L {preferred_term} aseptically and "
            "anaerobically after autoclaving and cooling."
        ),
        "composition": [
            _component(
                stock_component,
                stock_value,
                stock_unit,
                notes=(
                    f"{preferred_term} is represented from the stock label as "
                    f"{stock_value} {UNIT_LABELS[stock_unit]} {stock_component}."
                ),
            )
        ],
        "preparation_notes": "Autoclave and store under an N2 gas atmosphere.",
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("Sea salts (Sigma)", "30.0", "G_PER_L", term=False),
    _listed_component("MES", "4.0", "G_PER_L"),
    _listed_component("Yeast extract (Oxoid)", "1.0", "G_PER_L", term=False),
    _listed_component("Tryptone (BD-Difco)", "1.0", "G_PER_L", term=False),
    _listed_component("Resazurin", "0.5", "MG_PER_L"),
    _listed_component("Distilled water", "1.0", "L"),
    _component(
        "N2",
        "variable",
        "VARIABLE",
        notes=(
            "JCM Medium 1210 bubbles the medium with N2 for 5 min, distributes "
            "the medium into culture vessels under N2, and stores supplement "
            "stocks under an N2 gas atmosphere."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock("1.0 M Glucose solution", "14.0", GLUCOSE_STOCK_SIGNATURE),
    _stock("5% Na2S x 9H2O solution", "10.0", NA2S_STOCK_SIGNATURE),
    _stock("5% L-Cysteine HCl H2O solution", "10.0", CYSTEINE_STOCK_SIGNATURE),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix sea salts, MES, yeast extract, tryptone, resazurin, and " "distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 6.0.",
    },
    {
        "step_number": 3,
        "action": "ALIQUOT",
        "description": (
            "Bubble the medium with N2 for 5 min, distribute under N2, and seal "
            "with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 5,
        "action": "COOL",
        "description": "Cool after autoclaving.",
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": (
            "Add autoclaved and N2-stored glucose, Na2S x 9H2O, and "
            "L-cysteine HCl H2O stock solutions aseptically and anaerobically."
        ),
    },
)

NOTES = (
    "TOGO M1297 records JCM Medium 1210 with sea salts, MES, yeast extract, "
    "tryptone, resazurin, distilled water, and an N2 gas atmosphere. JCM 1210 "
    "adjusts the base medium to pH 6.0, bubbles it with N2 for 5 min, "
    "distributes it into culture vessels under N2, seals with butyl rubber "
    "stoppers, autoclaves, then adds autoclaved glucose, Na2S x 9H2O, and "
    "L-cysteine HCl H2O stock solutions aseptically and anaerobically."
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
        raise ValueError(f"{TARGET}: solution signature drifted")


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
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
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
    _put_after(repaired, "ph_value", 6.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": "Autoclave stocks separately and store under an N2 gas atmosphere.",
        },
        "preparation_steps",
    )
    _put_after(repaired, "notes", NOTES, "media_term")
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
