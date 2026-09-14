#!/usr/bin/env python3
"""Add the omitted 50x BBM stock component to JCM Medium 1481."""

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
TARGET = "algae/JCM_J1481_Bold_s_Basal_Medium_BBM.yaml"
EXPECTED_ID = "CultureMech:015878"
EXPECTED_MEDIA_TERM = "jcm.grmd:1481"
SOURCE_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1481"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_1481_bbm_score20.py"
ACTION = "RESOLVED_JCM_1481_BBM_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

NOTES = (
    "JCM Medium 1481 lists 20 g agar and 980 ml distilled water for one liter of "
    "Bold's Basal Medium (BBM) and instructs adding 20 ml Sigma-Aldrich Bold "
    "Modified Basal Freshwater Nutrient Solution, 50x, after autoclaving."
)

PREPARATION_STEPS: list[dict[str, Any]] = [
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Mix 20 g agar into 980 ml distilled water.",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After autoclaving, aseptically add 20 ml Sigma-Aldrich Bold Modified "
            "Basal Freshwater Nutrient Solution, 50x."
        ),
    },
]


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated", "has_unmapped_ingredients"):
        if flag not in flags:
            flags.append(flag)


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if SOURCE_URL not in found:
        references.append({"reference": SOURCE_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Added omitted 50x BBM stock to JCM Medium 1481",
        "source": SOURCE_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _check_source(doc: dict[str, Any]) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{TARGET}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: missing expected media term {EXPECTED_MEDIA_TERM}")


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["ingredients"] = [
        {
            "preferred_term": "Agar",
            "concentration": {"value": "20", "unit": "G_PER_L"},
            "source": "JCM Medium 1481",
            "term": _term("CHEBI:2509", "agar"),
            "mediaingredientmech_chebi_term": _term("CHEBI:2509", "agar"),
            "notes": "JCM Medium 1481 lists 20 g agar per liter.",
        },
        {
            "preferred_term": "Distilled water",
            "concentration": {"value": "980", "unit": "ML_PER_L"},
            "source": "JCM Medium 1481",
            "term": _term("CHEBI:15377", "water"),
            "mediaingredientmech_chebi_term": _term("CHEBI:15377", "water"),
            "notes": "JCM Medium 1481 lists 980 ml distilled water per liter.",
        },
        {
            "preferred_term": (
                "Sigma-Aldrich Bold Modified Basal Freshwater Nutrient Solution, 50x"
            ),
            "concentration": {"value": "20", "unit": "ML_PER_L"},
            "source": "JCM Medium 1481",
            "notes": (
                "JCM Medium 1481 says to add 20 ml of this 50x commercial BBM "
                "stock after autoclaving."
            ),
        },
    ]
    _put_after(repaired, "preparation_steps", copy.deepcopy(PREPARATION_STEPS), "ingredients")
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
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
    for path, doc in sorted(plans.items()):
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
