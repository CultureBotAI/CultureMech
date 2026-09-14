#!/usr/bin/env python3
"""Repair TOGO M1155 Peat Medium With Sucrose."""

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
TARGET = Path("bacterial/TOGO_M1155_Peat_Medium_With_Sucrose.yaml")
EXPECTED_ID = "CultureMech:007679"
EXPECTED_MEDIA_TERM = "TOGO:M1155"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1155_score15.py"
ACTION = "RESOLVED_TOGO_M1155_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1155 = "https://togomedium.org/medium/M1155"
TOGO_M969 = "https://togomedium.org/medium/M969"
JCM_1086 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1086"
JCM_923 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=923"

SOURCE = "JCM Medium 1086"
TITLE = "Peat Medium With Sucrose"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Sucrose", "2", "G_PER_L"),
    ("Peptone (BD--Difco)", "0.25", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone (BD-Difco)", "0.25", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Sucrose", "2.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Major metals (see Medium [M969])", "10", "G_PER_L", ()),
    ("Trace metal 1 solution (see Medium [M969])", "0.1", "G_PER_L", ()),
    ("0.5 M MES solution (pH 5.7)", "40", "G_PER_L", ()),
)

FINAL_MAJOR_METALS_SIGNATURE: tuple[Component, ...] = (
    ("KCl", "0.15", "G_PER_L"),
    ("KH2PO4", "1.36", "G_PER_L"),
    ("NH4Cl", "2.68", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

FINAL_TRACE_METAL_1_SIGNATURE: tuple[Component, ...] = (
    ("CoCl2 x 6H2O", "24.0", "MG_PER_L"),
    ("ZnCl2", "75.0", "MG_PER_L"),
    ("H3BO3", "19.0", "MG_PER_L"),
    ("NiCl2 x 6H2O", "24.0", "MG_PER_L"),
    ("Na2MoO4 x 2H2O", "24.0", "MG_PER_L"),
    ("FeCl2 x 4H2O", "1.344", "G_PER_L"),
    ("MnSO4 x H2O", "26.0", "MG_PER_L"),
    ("MgSO4 x 7H2O", "1.556", "G_PER_L"),
    ("CaCl2 x 2H2O", "2.336", "G_PER_L"),
    ("CuSO4 x 5H2O", "9.0", "MG_PER_L"),
    ("AlK(SO4)2 x 12H2O", "3.446", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Major metals", "10.0", "ML_PER_L", FINAL_MAJOR_METALS_SIGNATURE),
    ("Trace metal 1 solution", "0.1", "ML_PER_L", FINAL_TRACE_METAL_1_SIGNATURE),
    ("0.5 M MES solution (pH 5.7)", "40.0", "ML_PER_L", (("MES", "0.5", "MOLAR"),)),
)

REFERENCES = (TOGO_M1155, JCM_1086, TOGO_M969, JCM_923)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "AlK(SO4)2 x 12H2O": (
        "CHEBI:86465",
        "potassium aluminium sulfate dodecahydrate",
    ),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuSO4 x 5H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x H2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "MES": ("CHEBI:39010", "MES"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "NiCl2 x 6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Sucrose": ("CHEBI:17992", "sucrose"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
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
    source: str = SOURCE,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _source_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str = "JCM Medium 923",
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=(
            f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term} "
            "in this stock solution."
        ),
    )


def _gas(preferred_term: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes="JCM Medium 1086 replaces the gas phase with N2-CO2 (4:1, v/v).",
    )


def _mes_stock() -> dict[str, Any]:
    return {
        "preferred_term": "0.5 M MES solution (pH 5.7)",
        "concentration": {"value": "40.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 1086 adds 40.0 ml/L 0.5 M MES solution at pH 5.7 "
            "after autoclaving and cooling."
        ),
        "composition": [
            _component(
                "MES",
                "0.5",
                "MOLAR",
                source=SOURCE,
                notes="JCM Medium 1086 identifies this as a 0.5 M MES stock solution.",
            )
        ],
        "preparation_notes": "Filter-sterilize before addition to the cooled base medium.",
    }


def _major_metals_stock() -> dict[str, Any]:
    return {
        "preferred_term": "Major metals",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "JCM Medium 1086 adds 10.0 ml/L Major metals from JCM Medium 923.",
        "composition": [
            _source_component("KCl", "0.15", "G_PER_L"),
            _source_component("KH2PO4", "1.36", "G_PER_L"),
            _source_component("NH4Cl", "2.68", "G_PER_L"),
            _source_component("Distilled water", "1.0", "L"),
        ],
    }


def _trace_metal_1_stock() -> dict[str, Any]:
    return {
        "preferred_term": "Trace metal 1 solution",
        "concentration": {"value": "0.1", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": ("JCM Medium 1086 adds 0.1 ml/L Trace metal 1 solution from " "JCM Medium 923."),
        "composition": [
            _source_component("CoCl2 x 6H2O", "24.0", "MG_PER_L"),
            _source_component("ZnCl2", "75.0", "MG_PER_L"),
            _source_component("H3BO3", "19.0", "MG_PER_L"),
            _source_component("NiCl2 x 6H2O", "24.0", "MG_PER_L"),
            _source_component("Na2MoO4 x 2H2O", "24.0", "MG_PER_L"),
            _source_component("FeCl2 x 4H2O", "1.344", "G_PER_L"),
            _source_component("MnSO4 x H2O", "26.0", "MG_PER_L"),
            _source_component("MgSO4 x 7H2O", "1.556", "G_PER_L"),
            _source_component("CaCl2 x 2H2O", "2.336", "G_PER_L"),
            _source_component("CuSO4 x 5H2O", "9.0", "MG_PER_L"),
            _source_component("AlK(SO4)2 x 12H2O", "3.446", "G_PER_L"),
            _source_component("Distilled water", "1.0", "L"),
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("Peptone (BD-Difco)", "0.25", "G_PER_L", term=False),
    _listed_component("Yeast extract", "1.0", "G_PER_L", term=False),
    _listed_component("Sucrose", "2.0", "G_PER_L"),
    _listed_component("Distilled water", "1.0", "L"),
    _gas("Carbon dioxide gas"),
    _gas("Nitrogen gas"),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _major_metals_stock(),
    _trace_metal_1_stock(),
    _mes_stock(),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix peptone, yeast extract, sucrose, Major metals, Trace metal 1 "
            "solution, and distilled water thoroughly."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base medium at 121 degrees C for 15 min.",
    },
    {
        "step_number": 3,
        "action": "COOL",
        "description": (
            "Cool the autoclaved base medium, then add filter-sterilized 0.5 M " "MES solution."
        ),
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": (
            "Aseptically distribute the medium into culture vessels and replace "
            "the gas phase with N2-CO2 (4:1, v/v)."
        ),
    },
)

NOTES = (
    "TOGO M1155 records JCM Medium 1086 with peptone, yeast extract, sucrose, "
    "Major metals from JCM Medium 923, Trace metal 1 solution from JCM Medium "
    "923, distilled water, filter-sterilized 0.5 M MES solution at pH 5.7, "
    "and an N2-CO2 (4:1, v/v) gas phase. JCM 1086 autoclaves the base medium "
    "at 121 degrees C for 15 min, adds filter-sterilized MES after cooling, "
    "and then distributes it aseptically into culture vessels under N2-CO2."
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
    repaired.pop("ph_value", None)
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
            "notes": "Autoclave the base medium before adding filter-sterilized MES.",
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
