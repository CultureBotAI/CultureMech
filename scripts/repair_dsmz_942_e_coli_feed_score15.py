#!/usr/bin/env python3
"""Repair DSMZ 942 Agar with E. coli as Feed and its MediaDive main solution."""

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
MEDIUM_PATH = Path("bacterial/agar_with_e_coli_as_feed.yaml")
SOLUTION_PATH = Path("bacterial/mediadive_1939_Main_sol_942.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_942_e_coli_feed_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

DSMZ_942 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium942.pdf"
SOURCE = "DSMZ Medium 942"
SOLUTION_SOURCE = "MediaDive solution 1939 / DSMZ Medium 942"

Component = tuple[str, str, str]

IMPORTED_MEDIA_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2 H2O", "1", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2 H2O", "1", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Distilled water", "1000", "PERCENT_V_V"),
)

FINAL_MEDIA_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2 H2O", "1.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("CaCl2 x 2 H2O", "1.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

SOURCE_NOTE = (
    "DSMZ Medium 942 is a CaCl2-agar plate recipe overlaid with autoclaved "
    "Escherichia coli feed suspension lines/drops for myxobacteria; DSMZ "
    "specifies three separate drops of a thick ready-to-pipet suspension and "
    "does not fix an Escherichia coli concentration."
)

PREPARATION_NOTES = (
    "Adjust pH to 7.2, autoclave and pour plates. Grow Escherichia coli in "
    "liquid culture, collect cells by centrifugation, and resuspend them in "
    "enough water to receive a thick but ready-to-pipet suspension. Autoclave "
    "the suspension separately. Place three separate drops on one CaCl2-agar "
    "plate, streak every drop once to receive Escherichia coli lines about "
    "3 cm long, and inoculate the lines/drops with myxobacteria."
)

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Mix 1.0 g/L CaCl2 x 2 H2O with 15.0 g/L agar to prepare the CaCl2-agar base.",
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the CaCl2-agar base to pH 7.2.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the CaCl2-agar base.",
    },
    {
        "step_number": 4,
        "action": "POUR_PLATES",
        "description": "Pour the autoclaved CaCl2-agar base into plates.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Grow Escherichia coli in liquid culture, collect the cells by "
            "centrifugation, and resuspend the pellet in enough water to "
            "produce a thick but ready-to-pipet feed suspension."
        ),
    },
    {
        "step_number": 6,
        "action": "AUTOCLAVE",
        "description": "Autoclave the Escherichia coli feed suspension separately.",
    },
    {
        "step_number": 7,
        "action": "MIX",
        "description": (
            "Place three separate feed-suspension drops on each CaCl2-agar "
            "plate, streak each drop once into an approximately 3 cm line, "
            "and inoculate the Escherichia coli lines/drops with myxobacteria."
        ),
    },
]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": "CaCl2-agar plates and Escherichia coli feed suspension are autoclaved separately.",
}


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


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
) -> dict[str, Any]:
    identifier, label = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "term": _term(identifier, label),
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "mediaingredientmech_chebi_term": _term(identifier, label),
    }
    if preferred_term == "Agar":
        row["physicochemical_roles"] = ["SOLIDIFYING_AGENT"]
    return row


def _composition(
    source: str,
    signature: tuple[Component, ...],
) -> list[dict[str, Any]]:
    return [
        _component(preferred_term, value, unit, source=source)
        for preferred_term, value, unit in signature
    ]


def _ensure_medium(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:002118":
        raise ValueError(f"{MEDIUM_PATH}: expected CultureMech:002118")
    if _source_term_id(doc) != "mediadive.medium:942":
        raise ValueError(f"{MEDIUM_PATH}: expected mediadive.medium:942")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_MEDIA_SIGNATURE,
        FINAL_MEDIA_SIGNATURE,
    ):
        raise ValueError(f"{MEDIUM_PATH}: ingredient signature drifted")


def _ensure_solution(doc: dict[str, Any]) -> None:
    if doc.get("id") != "CultureMech:011348":
        raise ValueError(f"{SOLUTION_PATH}: expected CultureMech:011348")

    term = doc.get("term")
    if not isinstance(term, dict) or term.get("id") != "mediadive.solution:1939":
        raise ValueError(f"{SOLUTION_PATH}: expected mediadive.solution:1939")

    if _signature(doc.get("composition"), "composition") not in (
        IMPORTED_SOLUTION_SIGNATURE,
        FINAL_SOLUTION_SIGNATURE,
    ):
        raise ValueError(f"{SOLUTION_PATH}: solution composition signature drifted")


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
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    if not any(isinstance(row, dict) and row.get("reference") == DSMZ_942 for row in rows):
        rows.append({"reference": DSMZ_942})


def _append_event(doc: dict[str, Any], action: str, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": DSMZ_942,
        "notes": notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def repair_medium(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_medium(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.2, "physical_state")
    repaired.pop("kg_microbe_match", None)
    _put_after(repaired, "notes", SOURCE_NOTE, "media_term")
    repaired["ingredients"] = _composition(SOURCE, FINAL_MEDIA_SIGNATURE)
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "ingredients",
    )
    _put_after(
        repaired,
        "sterilization",
        copy.deepcopy(STERILIZATION),
        "preparation_steps",
    )

    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(
        repaired,
        "RESOLVED_DSMZ_942_E_COLI_FEED",
        (
            "Verified DSMZ Medium 942 as a two-component CaCl2-agar plate "
            "recipe with an unquantified autoclaved Escherichia coli feed "
            "suspension, marked the simple composition as curated, added "
            "structured preparation and sterilization steps, and removed a "
            "stale KG-Microbe match to DSMZ Medium 49."
        ),
    )
    return repaired


def repair_solution(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _composition(SOLUTION_SOURCE, FINAL_SOLUTION_SIGNATURE)
    repaired.pop("ingredients", None)
    repaired.pop("data_quality_flags", None)
    repaired["preparation_notes"] = PREPARATION_NOTES
    _put_after(
        repaired,
        "notes",
        (
            "MediaDive solution 1939 is the DSMZ Medium 942 main-solution "
            "import for Agar with E. coli as Feed."
        ),
        "preparation_notes",
    )

    _ensure_references(repaired)
    _append_event(
        repaired,
        "RESOLVED_MEDIADIVE_1939_DSMZ_942",
        (
            "Corrected Distilled water from a false percent-volume row to an "
            "implicit 1000.0 ml/L solvent, grounded the solution composition "
            "directly to CHEBI, and removed the placeholder ingredient."
        ),
    )
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
