#!/usr/bin/env python3
"""Repair the KOMODO 78.2 DSM 5566 pH variant."""

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

PARENT = Path("bacterial/KOMODO_78_CHOPPED_MEAT_medium.yaml")
PARENT_ID = "CultureMech:006491"
PARENT_NAME = "chopped_meat_medium"
PARENT_SOURCE_TERM = "komodo.medium:78"
PARENT_PH = 7.0

CHILD = Path("bacterial/for_dsm_5566.yaml")
CHILD_ID = "CultureMech:006471"
CHILD_NAME = "for_dsm_5566"
CHILD_SOURCE_TERM = "komodo.medium:78.2"
CHILD_PH = 7.2
RELATIONSHIP = "PH_VARIANT"

INGREDIENT_SIGNATURE = (
    ("L-Histidine", "12", "G_PER_L"),
    ("L-Serine", "10", "G_PER_L"),
    ("L-Glutamine", "14", "G_PER_L"),
    ("Vitamin B12", "0.05", "G_PER_L"),
    ("Pantothenic acid", "0.05", "G_PER_L"),
    ("Riboflavin", "0.05", "G_PER_L"),
    ("Pyridoxamine hydrochloride", "0.01", "G_PER_L"),
    ("Biotin", "0.02", "G_PER_L"),
    ("Folic acid", "0.02", "G_PER_L"),
    ("Nicotinic acid", "0.025", "G_PER_L"),
    ("Nicotine amide", "0.025", "G_PER_L"),
    ("alpha-lipoic acid", "0.05", "G_PER_L"),
    ("p-Aminobenzoic acid", "0.05", "G_PER_L"),
    ("Thiamine-HCl x 2 H2O", "0.05", "G_PER_L"),
    ("Ground beef", "487.805", "G_PER_L"),
    ("NaOH", "26.0", "G_PER_L"),
    ("Casitone", "29.2683", "G_PER_L"),
    ("Yeast extract", "4.87805", "G_PER_L"),
    ("K2HPO4", "4.87805", "G_PER_L"),
    ("Resazurin", "0.00097561", "G_PER_L"),
    ("L-Cysteine HCl", "0.487805", "G_PER_L"),
    ("Agar", "14.6341", "G_PER_L"),
    ("Haemin", "0.5", "G_PER_L"),
    ("Vitamin K3", "0.05", "G_PER_L"),
    ("Ethanol", "959.5", "G_PER_L"),
    ("Vitamin K1", "0.1", "G_PER_L"),
)

CURATOR = "repair_komodo_78_dsm_5566_score10.py"
ACTION = "RESOLVED_KOMODO_78_DSM_5566_PH_VARIANT"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _ingredient_signature(doc: dict[str, Any]) -> tuple[tuple[str, str, str], ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")

    signature: list[tuple[str, str, str]] = []
    for row in ingredients:
        if not isinstance(row, dict):
            continue
        concentration = row.get("concentration") or {}
        if not isinstance(concentration, dict):
            concentration = {}
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


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


def _upsert_event(doc: dict[str, Any], event: dict[str, Any]) -> None:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == event["curator"]
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_ingredients_curated(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ph_value: float,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if doc.get("ph_value") != ph_value:
        raise ValueError(f"{relative_path}: expected pH {ph_value:g}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _notes() -> str:
    return "KOMODO Medium 78.2 applies CHOPPED MEAT medium at pH 7.2 for DSM 5566."


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": RELATIONSHIP,
        "id": CHILD_ID,
        "name": CHILD_NAME,
        "notes": _notes(),
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 78 is the CHOPPED MEAT medium base.",
    }


def _replace_child_entry(doc: dict[str, Any]) -> None:
    children = doc.get("variant_children") or []
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    child_path = f"data/normalized_yaml/{CHILD}"
    for index, existing in enumerate(children):
        if isinstance(existing, dict) and existing.get("path") == child_path:
            children[index] = _child_entry()
            return
    raise ValueError(f"variant_children does not include {child_path}")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_PH)

    repaired = copy.deepcopy(doc)
    _replace_child_entry(repaired)
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 78.2 as a pH variant",
            "source": "KOMODO Medium 78-78.2",
            "notes": "Kept DSM 5566 beneath the KOMODO 78 CHOPPED MEAT parent.",
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM, CHILD_PH)

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(), "curation_history")
    _put_after(repaired, "variant_relationship", RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [_notes()], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 78 CHOPPED MEAT medium",
            "source": "KOMODO Medium 78.2",
            "notes": _notes(),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / PARENT: repair_parent(_load(normalized / PARENT)),
        normalized / CHILD: repair_child(_load(normalized / CHILD)),
    }


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
