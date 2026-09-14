#!/usr/bin/env python3
"""Repair DSMZ Medium 1670 BME/CTVM2 cell-line medium imports."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

PARENT_PATH = Path("bacterial/bme_ctvm2_cell_line_medium_occidentia_massiliensis.yaml")
SOLUTION_PATH = Path("bacterial/mediadive_3465_Main_sol_1670.yaml")

PARENT_ID = "CultureMech:001155"
SOLUTION_ID = "CultureMech:012590"
MEDIA_TERM = "mediadive.medium:1670"
SOLUTION_TERM = "mediadive.solution:3465"

DSMZ_1670 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1670.pdf"
MEDIADIVE_1670 = "https://mediadive.dsmz.de/medium/1670"
SOURCE = "DSMZ Medium 1670"

CURATOR = "repair_dsmz_1670_bme_score15.py"
ACTION = "RESOLVED_DSMZ_1670_BME_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

L15 = ("mediadive.compound:1504", "L-15 medium")
TRYPT_PHOS = ("mediadive.compound:1165", "Tryptose-phosphate")
FBS = ("mediadive.compound:954", "Fetal bovine serum")
GLUTAMINE = ("CHEBI:18050", "L-glutamine")

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_PARENT_INGREDIENTS: tuple[Component, ...] = (
    ("L-15 medium", "70", "G_PER_L"),
    ("Tryptose-phosphate", "10", "G_PER_L"),
    ("Fetal bovine serum", "20", "G_PER_L"),
    ("L-Glutamine", "0.029228", "G_PER_L"),
)

IMPORTED_SOLUTION_COMPOSITION: tuple[Component, ...] = (
    ("L-15 medium", "693.0693069306931", "PERCENT_V_V"),
    ("Tryptose-phosphate", "99.00990099009901", "PERCENT_V_V"),
    ("Fetal bovine serum", "198.01980198019803", "PERCENT_V_V"),
    ("L-Glutamine", "0.029228", "G_PER_L"),
)

FINAL_INGREDIENTS: tuple[Component, ...] = (
    ("L-15 (Leibovitz) medium", "693.069307", "ML_PER_L"),
    ("Tryptose phosphate broth", "99.009901", "ML_PER_L"),
    ("Foetal calf serum", "198.019802", "ML_PER_L"),
)

GLUTAMINE_STOCK_COMPOSITION: tuple[Component, ...] = (("L-Glutamine", "200.0", "MILLIMOLAR"),)

FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = (
    (
        "200 mM L-glutamine stock",
        "9.90099",
        "ML_PER_L",
        GLUTAMINE_STOCK_COMPOSITION,
    ),
)

UNIT_LABELS = {
    "ML_PER_L": "ml/L",
    "MILLIMOLAR": "mM",
}

REFERENCES = (DSMZ_1670, MEDIADIVE_1670)


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
    term: tuple[str, str],
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
    }
    if term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _ingredients() -> list[dict[str, Any]]:
    return [
        _component(
            "L-15 (Leibovitz) medium",
            "693.069307",
            "ML_PER_L",
            term=L15,
            notes=(
                "DSMZ Medium 1670 lists 70 ml L-15 (Leibovitz) medium "
                "in a 101 ml BME/CTVM2 cell-culture medium batch."
            ),
        ),
        _component(
            "Tryptose phosphate broth",
            "99.009901",
            "ML_PER_L",
            term=TRYPT_PHOS,
            notes=(
                "DSMZ Medium 1670 lists 10 ml tryptose phosphate broth "
                "in a 101 ml BME/CTVM2 cell-culture medium batch."
            ),
        ),
        _component(
            "Foetal calf serum",
            "198.019802",
            "ML_PER_L",
            term=FBS,
            notes=(
                "DSMZ Medium 1670 lists 20 ml foetal calf serum "
                "in a 101 ml BME/CTVM2 cell-culture medium batch."
            ),
        ),
    ]


def _glutamine_stock() -> dict[str, Any]:
    return {
        "preferred_term": "200 mM L-glutamine stock",
        "concentration": {"value": "9.90099", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "DSMZ Medium 1670 lists 1 ml 200 mM L-glutamine stock "
            "in a 101 ml BME/CTVM2 cell-culture medium batch."
        ),
        "composition": [
            _component(
                "L-Glutamine",
                "200.0",
                "MILLIMOLAR",
                term=GLUTAMINE,
                notes=("DSMZ Medium 1670 discloses this stock as 200 mM " "L-glutamine."),
            )
        ],
    }


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare the BME/CTVM2 cell-culture medium from 70 ml "
                "L-15 (Leibovitz) medium, 10 ml tryptose phosphate broth, "
                "20 ml foetal calf serum, and 1 ml 200 mM L-glutamine."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": (
                "Use the medium for BME/CTVM2 cells incubated in ordinary air "
                "in sealed flasks or flat-sided tubes in dry incubators."
            ),
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                "For Occidentia massiliensis infection, add 3 ml fresh medium "
                "and 1 ml thawed Occidentia strain to a 25 cm2 flask with "
                "5 ml residual medium, then incubate at 28 C with the lid "
                "closed and without CO2."
            ),
        },
    ]


def _notes() -> str:
    return (
        "DSMZ Medium 1670 prepares a 101 ml BME/CTVM2 tick-cell medium for "
        "Occidentia massiliensis cultivation from 70 ml L-15 (Leibovitz) "
        "medium, 10 ml tryptose phosphate broth, 20 ml foetal calf serum, "
        "and 1 ml 200 mM L-glutamine stock."
    )


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _record_term_id(doc: dict[str, Any]) -> str:
    term = doc.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{label} is not a list")

    signature = []
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


def _solution_signature(rows: Any) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signature = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), "solution composition"),
            )
        )
    return tuple(signature)


def _ensure_parent_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT_PATH}: expected id {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != MEDIA_TERM:
        raise ValueError(f"{PARENT_PATH}: expected media term {MEDIA_TERM}")

    signature = (
        _signature(doc.get("ingredients"), "ingredients"),
        _solution_signature(doc.get("solutions")),
    )
    if signature not in (
        (IMPORTED_PARENT_INGREDIENTS, ()),
        (FINAL_INGREDIENTS, FINAL_SOLUTIONS),
    ):
        raise ValueError(f"{PARENT_PATH}: composition drifted from importer or repaired form")


def _ensure_solution_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != SOLUTION_ID:
        raise ValueError(f"{SOLUTION_PATH}: expected id {SOLUTION_ID}, found {doc.get('id')!r}")
    if _record_term_id(doc) != SOLUTION_TERM:
        raise ValueError(f"{SOLUTION_PATH}: expected solution term {SOLUTION_TERM}")

    signature = (
        _signature(doc.get("composition"), "composition"),
        _solution_signature(doc.get("solutions")),
    )
    if signature not in (
        (IMPORTED_SOLUTION_COMPOSITION, ()),
        (FINAL_INGREDIENTS, FINAL_SOLUTIONS),
    ):
        raise ValueError(f"{SOLUTION_PATH}: composition drifted from importer or repaired form")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        del doc[key]

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


def _ensure_flags(doc: dict[str, Any], *, no_unmapped: bool = True) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)
    if no_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Corrected DSMZ Medium 1670 liquid batch volumes, retained the "
            "opaque L-15, tryptose phosphate, and serum products with MediaDive "
            "source identities, and represented the 200 mM L-glutamine stock "
            "as a measured stock addition."
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


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["temperature_value"] = 28.0
    repaired.pop("temperature_range", None)
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", [_glutamine_stock()], "ingredients")
    _put_after(repaired, "preparation_steps", _preparation_steps(), "solutions")
    _put_after(repaired, "notes", _notes(), "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def repair_solution(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _ingredients()
    _put_after(repaired, "solutions", [_glutamine_stock()], "composition")
    _put_after(repaired, "preparation_notes", _notes(), "solutions")
    repaired.pop("ingredients", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    candidates = {
        normalized / PARENT_PATH: repair_parent(_load(normalized / PARENT_PATH)),
        normalized / SOLUTION_PATH: repair_solution(_load(normalized / SOLUTION_PATH)),
    }
    return {
        path: doc
        for path, doc in candidates.items()
        if path.read_bytes() != dump_record(doc).encode("utf-8")
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    for path, doc in plans.items():
        if args.apply:
            write_record(path, doc)
        print(f"{'wrote' if args.apply else 'would'} {path.relative_to(args.normalized_dir)}")
    print(f"\n{'wrote' if args.apply else 'would write'} {len(plans)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
