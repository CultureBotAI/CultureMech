#!/usr/bin/env python3
"""Repair TOGO M1119 573C Medium."""

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
TARGET = Path("bacterial/TOGO_M1119_573C_Medium.yaml")
EXPECTED_ID = "CultureMech:007639"
EXPECTED_MEDIA_TERM = "TOGO:M1119"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1119_score15.py"
ACTION = "RESOLVED_TOGO_M1119_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1119 = "https://togomedium.org/medium/M1119"
JCM_1052 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1052"

SOURCE = "TOGO M1119 / JCM Medium 1052"
TITLE = "573C Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("KH2PO4", "0.37", "G_PER_L"),
    ("(NH4)2SO4", "1.3", "G_PER_L"),
    ("Glucose", "1", "G_PER_L"),
    ("Carboxymethyl cellulose, sodium salt", "2.5", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.25", "G_PER_L"),
    ("Tryptone (BD-Difco)", "0.9", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Carboxymethyl cellulose, sodium salt", "2.5", "G_PER_L"),
    ("(NH4)2SO4", "1.3", "G_PER_L"),
    ("KH2PO4", "0.37", "G_PER_L"),
    ("Glucose", "1.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.25", "G_PER_L"),
    ("Tryptone (BD-Difco)", "0.9", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

MGSO4_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4 x 7H2O", "25.0", "PERCENT_W_V"),
)
CACL2_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2H2O", "7.0", "PERCENT_W_V"),
)
FECL3_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("FeCl3 x 6H2O", "2.0", "PERCENT_W_V"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("7% CaCl2\u30fb2H2O solution", "1", "G_PER_L", ()),
    ("25% MgSO4\u30fb7H2O solution", "1", "G_PER_L", ()),
    ("2% FeCl3\u30fb6H2O solution", "1", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("25% MgSO4 x 7H2O solution", "1.0", "ML_PER_L", MGSO4_STOCK_SIGNATURE),
    ("7% CaCl2 x 2H2O solution", "1.0", "ML_PER_L", CACL2_STOCK_SIGNATURE),
    ("2% FeCl3 x 6H2O solution", "1.0", "ML_PER_L", FECL3_STOCK_SIGNATURE),
)

REFERENCES = (TOGO_M1119, JCM_1052)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl3 x 6H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
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
        notes=f"JCM Medium 1052 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
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
            f"JCM Medium 1052 lists {value} ml/L {preferred_term}, autoclaved "
            "separately and added aseptically to the medium."
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
        "preparation_notes": "Autoclave separately and add aseptically.",
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component(
        "Carboxymethyl cellulose, sodium salt",
        "2.5",
        "G_PER_L",
        term=False,
    ),
    _listed_component("(NH4)2SO4", "1.3", "G_PER_L"),
    _listed_component("KH2PO4", "0.37", "G_PER_L"),
    _listed_component("Glucose", "1.0", "G_PER_L"),
    _listed_component("Yeast extract (BD-Difco)", "0.25", "G_PER_L", term=False),
    _listed_component("Tryptone (BD-Difco)", "0.9", "G_PER_L", term=False),
    _listed_component("Distilled water", "1.0", "L"),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock("25% MgSO4 x 7H2O solution", "1.0", MGSO4_STOCK_SIGNATURE),
    _stock("7% CaCl2 x 2H2O solution", "1.0", CACL2_STOCK_SIGNATURE),
    _stock("2% FeCl3 x 6H2O solution", "1.0", FECL3_STOCK_SIGNATURE),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix carboxymethyl cellulose sodium salt, ammonium sulfate, KH2PO4, "
            "glucose, yeast extract, tryptone, and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 4.8-5.0.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave the base medium and the MgSO4 x 7H2O, CaCl2 x 2H2O, "
            "and FeCl3 x 6H2O stock solutions separately at 121 degrees C for "
            "15 min."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": "Aseptically add all stock solutions to the medium.",
    },
)

NOTES = (
    "TOGO M1119 records JCM Medium 1052 with carboxymethyl cellulose sodium "
    "salt, ammonium sulfate, KH2PO4, glucose, yeast extract, tryptone, 25% "
    "MgSO4 x 7H2O solution, 7% CaCl2 x 2H2O solution, 2% FeCl3 x 6H2O "
    "solution, and distilled water. JCM 1052 adjusts the medium to pH 4.8-5.0, "
    "autoclaves those stock solutions separately, and adds all solutions "
    "aseptically to the medium."
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
    _put_after(repaired, "ph_range", {"min": 4.8, "max": 5.0}, "physical_state")
    repaired.pop("ph_value", None)
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
            "notes": "Autoclave the MgSO4, CaCl2, and FeCl3 stock solutions separately.",
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
