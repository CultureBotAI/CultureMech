#!/usr/bin/env python3
"""Repair TOGO M2966 modified Luria broth."""

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
TARGET = Path("bacterial/modified_luria_broth.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009490"
EXPECTED_MEDIA_TERM = "TOGO:M2966"

CURATOR = "repair_togo_m2966_modified_luria_score15.py"
ACTION = "RESOLVED_TOGO_M2966_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2966 = "https://togomedium.org/medium/M2966"
MOBLEY_DOI = "https://doi.org/10.1128/iai.58.5.1281-1289.1990"
SOURCE = "TOGO M2966 / Mobley et al. 1990"
TITLE = "modified Luria broth"

WATER = "Distilled water"
YEAST_EXTRACT = "yeast extract"
NACL = "NaCl"
HEPES = "HEPES"
TRYPTONE = "tryptone [Difco]"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1", "G_PER_L"),
    (YEAST_EXTRACT, "5", "G_PER_L"),
    (NACL, "8.5", "G_PER_L"),
    (
        "N-2-hydroxy- ethylpiperazine-N'-2-ethanesulfonic acid "
        "[HEPES; pH 7.2])",
        "100",
        "MILLIMOLAR",
    ),
    (TRYPTONE, "10", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "1.0", "L"),
    (YEAST_EXTRACT, "5.0", "G_PER_L"),
    (NACL, "8.5", "G_PER_L"),
    (HEPES, "100.0", "MILLIMOLAR"),
    (TRYPTONE, "10.0", "G_PER_L"),
)

REFERENCES = (TOGO_M2966, MOBLEY_DOI)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    NACL: ("CHEBI:26710", "sodium chloride"),
    HEPES: ("CHEBI:42334", "HEPES"),
    TRYPTONE: ("MICRO:0000182", "Tryptone"),
}

MEDIAINGREDIENT_CHEBI = frozenset({WATER, NACL, HEPES})

NOTES = (
    "TOGO M2966 extracts the modified Luria broth formulation used by Mobley "
    "et al. 1990: per liter, 10 g tryptone from Difco, 5 g yeast extract, "
    "8.5 g NaCl, and 100 mM HEPES at pH 7.2, diluted to 300 mosmol."
)

INGREDIENT_NOTES = {
    WATER: f"TOGO M2966 records the formulation with 1 L {WATER}.",
    YEAST_EXTRACT: f"{SOURCE} lists 5 g/L yeast extract.",
    NACL: f"{SOURCE} lists 8.5 g/L NaCl.",
    HEPES: (
        f"{SOURCE} lists 100 mM N-2-hydroxyethylpiperazine-N'-"
        "2-ethanesulfonic acid [HEPES; pH 7.2]."
    ),
    TRYPTONE: f"{SOURCE} lists 10 g/L tryptone from Difco.",
}

PREPARATION_STEPS = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the modified Luria broth from 1 L distilled water, "
            "10 g/L tryptone, 5 g/L yeast extract, 8.5 g/L NaCl, and "
            "100 mM HEPES at pH 7.2."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": "Dilute the medium to 300 mosmol.",
    },
]


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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if preferred_term in MEDIAINGREDIENT_CHEBI:
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS = tuple(
    _component(
        name,
        value,
        unit,
        notes=INGREDIENT_NOTES[name],
    )
    for name, value, unit in FINAL_INGREDIENT_SIGNATURE
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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    if "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported 1 L water row from grams per liter "
            "to liters and grounded yeast extract, tryptone, and HEPES."
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
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(PREPARATION_STEPS)
    repaired.pop("solutions", None)
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
