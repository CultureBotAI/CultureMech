#!/usr/bin/env python3
"""Repair CCAP/MediaDive C78 PM."""

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
TARGET = Path("bacterial/pm.yaml")
EXPECTED_ID = "CultureMech:000391"
EXPECTED_MEDIA_TERM = "mediadive.medium:C78"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_ccap_c78_pm_score15.py"
ACTION = "RESOLVED_CCAP_C78_PM_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

CCAP_PM = "https://www.ccap.ac.uk/wp-content/uploads/MR_PM.pdf"
MEDIADIVE_C78 = "https://mediadive.dsmz.de/rest/medium/C78"
REFERENCES = (CCAP_PM, MEDIADIVE_C78)
SOURCE = "CCAP Medium C78 / MediaDive C78"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Sodium acetate trihydrate", "2", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Tryptone", "1", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Sodium acetate trihydrate", "2.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Tryptone", "1.0", "G_PER_L"),
    ("Deionized water", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Sodium acetate trihydrate": ("CHEBI:32138", "sodium acetate trihydrate"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "Tryptone": ("MICRO:0000182", "tryptone"),
    "Deionized water": ("CHEBI:15377", "water"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        "Sodium acetate trihydrate",
        "Deionized water",
    }
)

INGREDIENT_NOTES = {
    "Sodium acetate trihydrate": (
        "CCAP PM and MediaDive C78 list 2.0 g/L Sodium acetate trihydrate."
    ),
    "Yeast extract": (
        "CCAP PM and MediaDive C78 list 1.0 g/L Yeast extract; MediaDive "
        "identifies this as Oxoid L21."
    ),
    "Tryptone": (
        "CCAP PM and MediaDive C78 list 1.0 g/L Tryptone; MediaDive identifies "
        "this as Oxoid L42."
    ),
    "Deionized water": (
        "CCAP PM says to make the medium up to 1 litre with deionised water."
    ),
}

NOTES = (
    "CCAP Medium C78 PM (Polytoma Medium) lists 2.0 g sodium acetate trihydrate, "
    "1.0 g yeast extract, 1.0 g tryptone, and deionised water to 1 litre, with "
    "autoclaving at 15 psi for 15 minutes. MediaDive C78 preserves the same "
    "CCAP formulation and identifies the yeast extract as Oxoid L21 and the "
    "tryptone as Oxoid L42. The accessible CCAP and MediaDive records do not "
    "state a pH or incubation temperature."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Make up to 1 litre with deionised water. Autoclave at 15 psi for "
            "15 minutes."
        ),
    },
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
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)
    while "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


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
            "Added the CCAP/MediaDive deionised-water row, grounded every PM "
            "component, and documented that the accessible source records do "
            "not state pH or temperature."
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
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "media_term")
    _put_after(repaired, "notes", NOTES, "preparation_steps")
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
