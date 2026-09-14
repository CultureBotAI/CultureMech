#!/usr/bin/env python3
"""Repair TOGO Medium M2770 4-YACo media."""

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
TARGET = "bacterial/4_yaco_media.yaml"
EXPECTED_ID = "CultureMech:009318"
EXPECTED_SOURCE_TERM = "TOGO:M2770"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2770_4_yaco_score15.py"
ACTION = "RESOLVED_TOGO_M2770_4_YACO_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2770 = "https://togomedium.org/medium/M2770"
ROSENTHAL_2011_DOI = "https://doi.org/10.1038/ismej.2011.3"
SOURCE = "TOGO Medium M2770 / Rosenthal et al. 2011"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("yeast autolysate", "4", "PERCENT_W_V"),
    ("maltose", "variable", "VARIABLE"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Hydrogen gas", "variable", "VARIABLE"),
    ("Vitamin B7", "variable", "VARIABLE"),
    ("Vitamin B6", "variable", "VARIABLE"),
    ("Vitamin B12", "variable", "VARIABLE"),
    ("Tryptophan", "variable", "VARIABLE"),
    ("biotin (Sigma Aldrich, St Louis, MO, USA)", "variable", "VARIABLE"),
    ("pyridoxal-phosphate (Sigma Aldrich)", "variable", "VARIABLE"),
    ("pyridoxal-HCl (Sigma Aldrich)", "variable", "VARIABLE"),
    ("hydroxocobalamin acetate salt", "variable", "VARIABLE"),
    ("hydroxocobalamin hydrochloride", "variable", "VARIABLE"),
    ("methylcobalamin", "variable", "VARIABLE"),
    ("cyanocobalamin (Sigma Aldrich)", "variable", "VARIABLE"),
    ("tryptophan (Sigma Aldrich)", "variable", "VARIABLE"),
)
IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "yeast autolysate",
        "4",
        "PERCENT_W_V",
        notes="TOGO M2770 lists 4% yeast autolysate for 4-YACo medium.",
    ),
    _component(
        "maltose",
        "20",
        "MILLIMOLAR",
        notes="TOGO M2770 supplements 4-YACo medium with 20 mM maltose.",
        term=("CHEBI:18167", "alpha-maltose"),
    ),
    _component(
        "H2",
        "80",
        "PERCENT_V_V",
        notes="TOGO M2770 uses 80% H2 and 20% CO2 in the Balch-tube headspace.",
        term=("CHEBI:18276", "dihydrogen"),
    ),
    _component(
        "CO2",
        "20",
        "PERCENT_V_V",
        notes="TOGO M2770 uses 80% H2 and 20% CO2 in the Balch-tube headspace.",
        term=("CHEBI:16526", "carbon dioxide"),
    ),
    _component(
        "biotin",
        "60-100",
        "MICROG_PER_L",
        notes=(
            "TOGO M2770 reports 0.3-0.5 ug biotin per 5 ml culture tube, "
            "equivalent to 60-100 ug/L."
        ),
        term=("CHEBI:15956", "biotin"),
    ),
    _component(
        "Vitamin B6 supplement",
        "24-40",
        "MG_PER_L",
        notes=(
            "TOGO M2770 reports 120-200 ug per 5 ml culture tube under the "
            "Vitamin B6 heading and names pyridoxal-HCl and pyridoxal-phosphate; "
            "modeled as an opaque B6 supplement family."
        ),
    ),
    _component(
        "Vitamin B12/corrinoid supplement",
        "6-10",
        "MG_PER_L",
        notes=(
            "TOGO M2770 reports 30-50 ug of one B12/corrinoid form per 5 ml "
            "culture tube, equivalent to 6-10 mg/L; the alternatives are "
            "hydroxocobalamin acetate salt, hydroxocobalamin hydrochloride, "
            "methylcobalamin, or cyanocobalamin."
        ),
    ),
    _component(
        "L-tryptophan",
        "12-20",
        "MG_PER_L",
        notes=(
            "TOGO M2770 reports 60-100 ug tryptophan per 5 ml culture tube, "
            "equivalent to 12-20 mg/L."
        ),
        term=("CHEBI:27897", "tryptophan"),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    _step(
        1,
        "MIX",
        "Prepare 4-YACo medium with 4% yeast autolysate and 20 mM maltose.",
    ),
    _step(
        2,
        "MIX",
        (
            "Supplement each 5 ml culture with the Vitamin B7, Vitamin B6, "
            "Vitamin B12/corrinoid, and tryptophan quantities reported by "
            "TOGO M2770."
        ),
    ),
    _step(
        3,
        "ALIQUOT",
        (
            "Grow cultures in 5 ml volumes in 25 ml Balch tubes with crimp-top "
            "stoppers under an 80% H2 and 20% CO2 headspace in the dark at room "
            "temperature."
        ),
    ),
)

NOTES = (
    "Collapsed TOGO M2770 nested supplement headings into a single curated "
    "4-YACo recipe: 4% yeast autolysate, 20 mM maltose, 80% H2/20% CO2 "
    "headspace, and per-5-ml-tube B7, B6, B12/corrinoid, and tryptophan "
    "supplements converted to per-liter concentrations. Vitamin B6 and "
    "B12/corrinoid supplement families remain explicitly unmapped because the "
    "source groups alternative or multiple molecular forms."
)

FINAL_INGREDIENT_SIGNATURE = tuple(
    (
        str(row["preferred_term"]),
        str(row["concentration"]["value"]),
        str(row["concentration"]["unit"]),
    )
    for row in INGREDIENTS
)
FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = ()


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{TARGET}: expected source term {EXPECTED_SOURCE_TERM}, found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if (ingredient_signature, solution_signature) not in {
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURE),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURE),
    }:
        raise ValueError(
            f"{TARGET}: ingredient/solution signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to "
            f"{ingredient_signature!r} / {solution_signature!r}"
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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

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
    for reference_url in (TOGO_M2770, ROSENTHAL_2011_DOI):
        if reference_url not in existing:
            references.append({"reference": reference_url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": TOGO_M2770,
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    _put_after(repaired, "temperature_range", "room temperature", "physical_state")
    _put_after(
        repaired,
        "aeration",
        "80% H2 and 20% CO2 Balch-tube headspace",
        "temperature_range",
    )
    _put_after(
        repaired,
        "culture_vessel",
        "5 ml culture in a 25 ml Balch tube with a crimp-top stopper",
        "aeration",
    )
    _put_after(repaired, "incubation_atmosphere", "ANAEROBIC", "applications")
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
