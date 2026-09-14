#!/usr/bin/env python3
"""Repair the NBRC Nutrient Agar score-25 source duplicate."""

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

PATH = Path("bacterial/NBRC_NUTRIENT_AGAR.yaml")
EXPECTED_ID = "CultureMech:007511"
EXPECTED_INGREDIENTS = frozenset(
    {
        frozenset({"beef extract", "peptone", "agar"}),
        frozenset({"beef extract", "peptone", "agar", "distilled water"}),
    }
)

CURATOR = "repair_nbrc_nutrient_agar_score25.py"
ACTION = "RESOLVED_NBRC_NUTRIENT_AGAR_SCORE25"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

JCM_74 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=74"
SOURCE = "NBRC No. 1 import, cross-checked against JCM Medium 74"
NOTES = (
    "NBRC No. 1 imported Nutrient Agar as 3.0 g/L beef extract, 5.0 g/L "
    "peptone, and 15.0 g/L agar; live JCM Medium 74 confirms the same "
    "per-liter formulation with distilled water."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


INGREDIENTS = [
    {
        "preferred_term": "Beef extract",
        "concentration": {"value": "3.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "NBRC No. 1 and JCM Medium 74 list 3.0 g/L beef extract.",
        "term": _term("FOODON:03302088", "beef extract"),
    },
    {
        "preferred_term": "Peptone",
        "concentration": {"value": "5.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "NBRC No. 1 and JCM Medium 74 list 5.0 g/L peptone.",
        "term": _term("MICRO:0000178", "peptone"),
    },
    {
        "preferred_term": "Agar",
        "concentration": {"value": "15.0", "unit": "G_PER_L"},
        "source": SOURCE,
        "notes": "NBRC No. 1 and JCM Medium 74 list 15.0 g/L agar.",
        "term": _term("CHEBI:2509", "agar"),
        "mediaingredientmech_chebi_term": _term("CHEBI:2509", "agar"),
    },
    {
        "preferred_term": "Distilled water",
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "NBRC No. 1 and JCM Medium 74 list 1.0 L distilled water.",
        "term": _term("CHEBI:15377", "water"),
        "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
    },
]


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _ingredient_names(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "").lower()
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{PATH}: expected {EXPECTED_ID}, found {doc.get('id')!r}")

    if _ingredient_names(doc) not in EXPECTED_INGREDIENTS:
        raise ValueError(f"{PATH}: ingredient list drifted")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    if not any(isinstance(row, dict) and row.get("reference") == JCM_74 for row in references):
        references.append({"reference": JCM_74})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_74,
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
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "media_term",
        {
            "preferred_term": "NBRC Medium 1",
            "term": _term("nbrc.medium:1", "NBRC Medium 1"),
        },
        "physical_state",
    )
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = copy.deepcopy(INGREDIENTS)
    repaired["data_quality_flags"] = [
        "ingredients_curated",
        "has_ontology_mappings",
    ]

    _ensure_reference(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / PATH
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
