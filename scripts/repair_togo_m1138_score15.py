#!/usr/bin/env python3
"""Repair TOGO M1138 Microaerophilic Lutibacter Medium."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import repair_togo_m1137_score15 as m1137  # noqa: E402
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/TOGO_M1138_Microaerophilic_Lutibacter_Medium.yaml")
EXPECTED_ID = "CultureMech:007660"
EXPECTED_MEDIA_TERM = "TOGO:M1138"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1138_score15.py"
ACTION = "RESOLVED_TOGO_M1138_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1138 = "https://togomedium.org/medium/M1138"
JCM_1069 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1069"

SOURCE = "TOGO M1138 / JCM Medium 1069"
TITLE = "Microaerophilic Lutibacter Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("MES", "1.95", "G_PER_L"),
    ("Tryptone (BD-Difco)", "2", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("MES", "1.95", "G_PER_L"),
    ("Tryptone (BD-Difco)", "2.0", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Artificial saltwater (see Medium [M642])", "1", "G_PER_L", ()),
    ("Wolfe's mineral solution (see Medium [M257])", "1", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (
        "Artificial saltwater",
        "1000.0",
        "ML_PER_L",
        m1137.ARTIFICIAL_SALTWATER_SIGNATURE,
    ),
    ("Wolfe's mineral solution", "1.0", "ML_PER_L", m1137.WOLFE_SIGNATURE),
    ("Trace vitamins", "10.0", "ML_PER_L", m1137.VITAMIN_SIGNATURE),
)

REFERENCES = (
    TOGO_M1138,
    JCM_1069,
    m1137.TOGO_M642,
    m1137.JCM_629,
    m1137.TOGO_M257,
    m1137.JCM_265,
    m1137.JCM_151,
    m1137.TOGO_M190,
    m1137.JCM_197,
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    **m1137.GROUNDINGS,
    "MES": ("CHEBI:39010", "MES"),
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
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
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
    source: str,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {m1137.UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _gas(preferred_term: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes=("JCM Medium 1069 replaces the gas phase with " "N2-CO2-O2 (90:10:2, v/v/v)."),
    )


def _stock(
    preferred_term: str,
    dose: str,
    composition: tuple[dict[str, Any], ...],
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": dose, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": copy.deepcopy(list(composition)),
    }
    if preparation_notes:
        row["preparation_notes"] = preparation_notes
    return row


ARTIFICIAL_SALTWATER = tuple(
    _listed_component(name, value, unit, source=m1137.SALTWATER_SOURCE)
    for name, value, unit in m1137.ARTIFICIAL_SALTWATER_SIGNATURE
)

WOLFE_COMPOSITION = tuple(
    _listed_component(name, value, unit, source=m1137.TRACE_MINERALS_SOURCE)
    for name, value, unit in m1137.TRACE_MINERALS_SIGNATURE
) + tuple(
    _listed_component(name, value, unit, source=m1137.WOLFE_SOURCE)
    for name, value, unit in m1137.WOLFE_ADDITION_SIGNATURE
)

TRACE_VITAMINS = tuple(
    _listed_component(name, value, unit, source=m1137.VITAMINS_SOURCE)
    for name, value, unit in m1137.VITAMIN_SIGNATURE
)

INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("MES", "1.95", "G_PER_L", source=SOURCE),
    _listed_component("Tryptone (BD-Difco)", "2.0", "G_PER_L", source=SOURCE, term=False),
    _gas("Carbon dioxide gas"),
    _gas("Nitrogen gas"),
    _gas("Oxygen gas"),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        "Artificial saltwater",
        "1000.0",
        ARTIFICIAL_SALTWATER,
        "JCM Medium 1069 lists 1.0 L Artificial saltwater.",
    ),
    _stock(
        "Wolfe's mineral solution",
        "1.0",
        WOLFE_COMPOSITION,
        "JCM Medium 1069 lists 1.0 ml/L Wolfe's mineral solution.",
        (
            "JCM Medium 265 prepares Wolfe's mineral solution from Trace "
            "minerals from JCM Medium 151, NiCl2 x 6H2O, Na2SeO3, and "
            "Na2WO4 x 2H2O."
        ),
    ),
    _stock(
        "Trace vitamins",
        "10.0",
        TRACE_VITAMINS,
        "JCM Medium 1069 lists 10.0 ml/L Trace vitamins.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix Artificial saltwater, MES, Wolfe's mineral solution, Trace "
            "vitamins, and Tryptone."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 6.2-6.5.",
    },
    {
        "step_number": 3,
        "action": "ALIQUOT",
        "description": (
            "Distribute the medium into culture vessels, replace the gas phase "
            "with N2-CO2-O2 (90:10:2, v/v/v), and seal with butyl rubber "
            "stoppers."
        ),
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
)

NOTES = (
    "TOGO M1138 records JCM Medium 1069 with Artificial saltwater from JCM "
    "Medium 629, MES, Wolfe's mineral solution from JCM Medium 265, Trace "
    "vitamins from JCM Medium 197, Tryptone, and an N2-CO2-O2 gas phase. JCM "
    "1069 adjusts the medium to pH 6.2-6.5, distributes it into culture "
    "vessels, replaces the gas phase with N2-CO2-O2 (90:10:2, v/v/v), seals "
    "with butyl rubber stoppers, and autoclaves."
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
        raise ValueError(f"{TARGET}: ingredient signature drifted")

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
    _put_after(repaired, "ph_range", {"min": 6.2, "max": 6.5}, "physical_state")
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
            "notes": "Autoclave the sealed culture vessels.",
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
