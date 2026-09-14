#!/usr/bin/env python3
"""Repair MediaDive DSMZ Medium 1816 MDA and its main-solution record."""

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
MEDIUM_PATH = Path("bacterial/mda.yaml")
SOLUTION_PATH = Path("bacterial/mediadive_6326_Main_sol_1816.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

MEDIUM_ID = "CultureMech:001249"
SOLUTION_ID = "CultureMech:014986"
MEDIA_TERM = "mediadive.medium:1816"
SOLUTION_TERM = "mediadive.solution:6326"

MEDIADIVE_1816 = "https://mediadive.dsmz.de/medium/1816"
MEDIADIVE_SOLUTION_6326 = "https://mediadive.dsmz.de/solutions/6326"
REFERENCES = (MEDIADIVE_1816, MEDIADIVE_SOLUTION_6326)
SOURCE = "MediaDive DSMZ Medium 1816"

CURATOR = "repair_mediadive_1816_mda_score15.py"
ACTION = "RESOLVED_MEDIADIVE_1816_MDA_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

Component = tuple[str, str, str]

IMPORTED_MEDIUM_SIGNATURE: tuple[Component, ...] = (
    ("Malt extract", "18", "G_PER_L"),
    ("Bacto peptone", "5", "G_PER_L"),
    ("Desicatted Ox-bile", "10", "G_PER_L"),
    ("Tween 40", "5", "G_PER_L"),
    ("Glycerol", "1", "G_PER_L"),
    ("Olive oil", "1", "G_PER_L"),
    ("(-)-Chloramphenicol", "0.25", "G_PER_L"),
    ("Agar", "7.5", "G_PER_L"),
)

FINAL_MEDIUM_SIGNATURE: tuple[Component, ...] = (
    ("Malt extract", "36", "G_PER_L"),
    ("Bacto peptone", "10", "G_PER_L"),
    ("Desicatted Ox-bile", "20", "G_PER_L"),
    ("Tween 40", "10", "G_PER_L"),
    ("Glycerol", "2", "ML_PER_L"),
    ("Olive oil", "2", "ML_PER_L"),
    ("(-)-Chloramphenicol", "0.5", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Distilled water", "1000", "ML_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Malt extract", "36.0", "G_PER_L"),
    ("Bacto peptone", "10.0", "G_PER_L"),
    ("Desicatted Ox-bile", "20.0", "G_PER_L"),
    ("Tween 40", "10.0", "G_PER_L"),
    ("Glycerol", "2.0", "PERCENT_V_V"),
    ("Olive oil", "2.0", "PERCENT_V_V"),
    ("(-)-Chloramphenicol", "0.5", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "PERCENT_V_V"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Malt extract", "36.0", "G_PER_L"),
    ("Bacto peptone", "10.0", "G_PER_L"),
    ("Desicatted Ox-bile", "20.0", "G_PER_L"),
    ("Tween 40", "10.0", "G_PER_L"),
    ("Glycerol", "2.0", "ML_PER_L"),
    ("Olive oil", "2.0", "ML_PER_L"),
    ("(-)-Chloramphenicol", "0.5", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Bacto peptone": ("MICRO:0000178", "Bacto peptone"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "Malt extract": ("FOODON:03301056", "malt extract"),
    "Tween 40": ("CHEBI:53423", "polysorbate 40"),
    "(-)-Chloramphenicol": ("CHEBI:17698", "chloramphenicol"),
}

MEDIADIVE_COMPOUNDS: dict[str, tuple[str, str]] = {
    "Malt extract": ("mediadive.compound:116", "Malt extract"),
    "Bacto peptone": ("mediadive.compound:19", "Bacto peptone"),
    "Desicatted Ox-bile": ("mediadive.compound:2375", "Desicatted Ox-bile"),
    "Tween 40": ("mediadive.compound:503", "Tween 40"),
    "Glycerol": ("mediadive.compound:72", "Glycerol"),
    "Olive oil": ("mediadive.compound:1674", "Olive oil"),
    "(-)-Chloramphenicol": ("mediadive.compound:2191", "(-)-Chloramphenicol"),
    "Agar": ("mediadive.compound:3", "Agar"),
    "Distilled water": ("mediadive.compound:4", "Distilled water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "MediaDive DSMZ Medium 1816 records MDA as an official DSMZ medium whose "
    "Main sol. 1816 formula is a 500 ml source batch: 18 g malt extract, "
    "5 g Bacto peptone, 10 g Desicatted Ox-bile, 5 g Tween 40, 1 ml glycerol, "
    "1 ml olive oil, 0.25 g (-)-Chloramphenicol, 7.5 g agar, and 500 ml "
    "distilled water. Concentrations are normalized here to one liter."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _medium_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _solution_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "term": _term(*MEDIADIVE_COMPOUNDS[preferred_term]),
        "source": SOURCE,
        "notes": f"{SOURCE} solution 6326 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None and grounding[0].startswith("CHEBI:"):
        row["chebi_term"] = _term(*grounding)
    return row


def _medium_ingredients() -> list[dict[str, Any]]:
    return [
        _medium_component(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_MEDIUM_SIGNATURE
    ]


def _solution_composition() -> list[dict[str, Any]]:
    return [
        _solution_component(preferred_term, value, unit)
        for preferred_term, value, unit in FINAL_SOLUTION_SIGNATURE
    ]


def _ensure_medium(doc: dict[str, Any]) -> None:
    if doc.get("id") != MEDIUM_ID:
        raise ValueError(f"{MEDIUM_PATH}: expected id {MEDIUM_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != MEDIA_TERM:
        raise ValueError(f"{MEDIUM_PATH}: expected media term {MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_MEDIUM_SIGNATURE,
        FINAL_MEDIUM_SIGNATURE,
    ):
        raise ValueError(f"{MEDIUM_PATH}: ingredient signature drifted")


def _ensure_solution(doc: dict[str, Any]) -> None:
    if doc.get("id") != SOLUTION_ID:
        raise ValueError(
            f"{SOLUTION_PATH}: expected id {SOLUTION_ID}, found {doc.get('id')!r}"
        )
    if _record_term_id(doc) != SOLUTION_TERM:
        raise ValueError(f"{SOLUTION_PATH}: expected solution term {SOLUTION_TERM}")
    if _signature(doc.get("composition"), "composition") not in (
        IMPORTED_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{SOLUTION_PATH}: composition signature drifted")


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


def _ensure_flags(doc: dict[str, Any], *, has_unmapped: bool) -> None:
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

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)
    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    if not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            rows.append({"reference": reference})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Corrected the MediaDive 500 ml source batch to per-liter "
            "concentrations, restored Distilled water as a measured ml/L "
            "component, preserved source names for the Desicatted Ox-bile and "
            "olive-oil mixture rows, and grounded exact malt extract, Bacto "
            "peptone, Tween 40, glycerol, chloramphenicol, agar, and water "
            "components."
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


def repair_medium(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_medium(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(
        repaired,
        "notes",
        f"{NOTES} MediaDive reports final pH as n.d.",
        "media_term",
    )
    repaired["ingredients"] = _medium_ingredients()
    _ensure_flags(repaired, has_unmapped=True)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def repair_solution(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _solution_composition()
    repaired.pop("ingredients", None)
    _put_after(
        repaired,
        "preparation_notes",
        (
            "MediaDive solution 6326 is the 500 ml Main sol. 1816 import "
            "used by MediaDive DSMZ Medium 1816."
        ),
        "composition",
    )
    _put_after(repaired, "notes", NOTES, "preparation_notes")
    _ensure_flags(repaired, has_unmapped=False)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / MEDIUM_PATH: repair_medium(_load(normalized / MEDIUM_PATH)),
        normalized / SOLUTION_PATH: repair_solution(_load(normalized / SOLUTION_PATH)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
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
