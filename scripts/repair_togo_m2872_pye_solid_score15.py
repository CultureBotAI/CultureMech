#!/usr/bin/env python3
"""Repair TOGO M2872 PYE Solid medium ingredient grounding."""

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
TARGET = Path("bacterial/pye_solid_medium.yaml")
EXPECTED_ID = "CultureMech:009406"
EXPECTED_MEDIA_TERM = "TOGO:M2872"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2872_pye_solid_score15.py"
ACTION = "RESOLVED_TOGO_M2872_PYE_SOLID_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2872 = "https://togomedium.org/medium/M2872"
TOGO_M2872_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2872"
MARKS_DOI = "https://doi.org/10.1128/JB.00255-10"
MARKS_PMC = "https://pmc.ncbi.nlm.nih.gov/articles/PMC2897358/"
REFERENCES = (TOGO_M2872, TOGO_M2872_API, MARKS_DOI, MARKS_PMC)
SOURCE = "TOGO M2872 / Marks et al. 2010"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("yeast extract", "0.1", "PERCENT_W_V"),
    ("CaCl2", "0.5", "MILLIMOLAR"),
    ("MgSO4", "1", "MILLIMOLAR"),
    ("Bacto agar", "1.5", "PERCENT_W_V"),
    ("Bacto peptone", "0.2", "PERCENT_W_V"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto peptone", "0.2", "PERCENT_W_V"),
    ("Yeast extract", "0.1", "PERCENT_W_V"),
    ("MgSO4", "1", "MILLIMOLAR"),
    ("CaCl2", "0.5", "MILLIMOLAR"),
    ("Agar", "1.5", "PERCENT_W_V"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Bacto peptone": ("MICRO:0000178", "Bacto peptone"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "MgSO4": ("CHEBI:32599", "magnesium sulfate"),
    "CaCl2": ("CHEBI:3312", "calcium dichloride"),
    "Agar": ("CHEBI:2509", "agar"),
}

MEDIAINGREDIENT_CHEBI = frozenset({"MgSO4", "CaCl2", "Agar"})

INGREDIENT_NOTES = {
    "Bacto peptone": "Marks et al. 2010 lists 0.2% Bacto peptone in rich PYE.",
    "Yeast extract": "Marks et al. 2010 lists 0.1% yeast extract in rich PYE.",
    "MgSO4": "Marks et al. 2010 lists 1 mM MgSO4 in rich PYE.",
    "CaCl2": "Marks et al. 2010 lists 0.5 mM CaCl2 in rich PYE.",
    "Agar": (
        "Marks et al. 2010 lists PYE solid medium as PYE with 1.5% Bacto "
        "agar; the source-disclosed agar solidifier is grounded to agar."
    ),
}

NOTES = (
    "TOGO M2872 imports PYE Solid medium from Marks et al. 2010. The article "
    "defines rich PYE as 0.2% Bacto peptone, 0.1% yeast extract, 1 mM MgSO4, "
    "and 0.5 mM CaCl2, then defines solid medium as PYE with 1.5% Bacto agar."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": INGREDIENT_NOTES[preferred_term],
        "term": _term(*GROUNDINGS[preferred_term]),
    }
    if preferred_term in MEDIAINGREDIENT_CHEBI:
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(*component) for component in FINAL_INGREDIENT_SIGNATURE
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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

    solutions = doc.get("solutions") or []
    if solutions:
        raise ValueError(f"{TARGET}: unexpected solutions block")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    doc.pop(key, None)
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

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "has_unmapped_ingredients",
    ):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Grounded all five source-listed PYE Solid components to "
            "MediaIngredientMech, FoodOn, or ChEBI terms using TOGO M2872 and "
            "Marks et al. 2010. Left pH and recipe temperature unset because "
            "the source does not report a formulation pH and reports 30 C as "
            "a study incubation condition."
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
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
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
