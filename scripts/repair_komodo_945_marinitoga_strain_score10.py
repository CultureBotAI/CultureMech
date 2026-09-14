#!/usr/bin/env python3
"""Repair KOMODO 945.1 topology rooted at a strain-specific duplicate."""

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

PARENT = Path("bacterial/KOMODO_945_MARINITOGA_PIEZOPHILA_medium.yaml")
PARENT_ID = "CultureMech:006880"
PARENT_NAME = "marinitoga_piezophila_medium"
PARENT_SOURCE_TERM = "komodo.medium:945"

CHILD = Path("bacterial/for_dsm_14283.yaml")
CHILD_ID = "CultureMech:006878"
CHILD_NAME = "for_dsm_14283"
CHILD_SOURCE_TERM = "komodo.medium:945.1"
RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
CHILD_NOTES = "KOMODO Medium 945.1 applies MARINITOGA PIEZOPHILA medium to DSM 14283."

PH = 6.0
INGREDIENT_SIGNATURE = (
    ("NH4Cl", "1", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("KCl", "0.1", "G_PER_L"),
    ("NaCl", "30", "G_PER_L"),
    ("Na-acetate", "0.83", "G_PER_L"),
    ("MES", "1.95", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("Trypticase peptone", "5", "G_PER_L"),
    ("K2HPO4", "0.3", "G_PER_L"),
    ("KH2PO4", "0.3", "G_PER_L"),
    ("Sodium resazurin", "0.0005", "G_PER_L"),
    ("Sulfur", "10", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.3", "G_PER_L"),
    ("Na2S x 9 H2O", "0.3", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)

CURATOR = "repair_komodo_945_marinitoga_strain_score10.py"
ACTION = "RESOLVED_KOMODO_945_MARINITOGA_STRAIN_TOPOLOGY"
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


def _upsert_child_entry(children: list[Any], entry: dict[str, str]) -> None:
    for index, existing in enumerate(children):
        if (
            isinstance(existing, dict)
            and (
                existing.get("id") == entry["id"]
                or existing.get("path") == entry["path"]
            )
        ):
            children[index] = entry
            return
    children.append(entry)


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": RELATIONSHIP,
        "id": CHILD_ID,
        "name": CHILD_NAME,
        "notes": CHILD_NOTES,
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 945 is the MARINITOGA PIEZOPHILA base.",
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if doc.get("ph_value") != PH:
        raise ValueError(f"{relative_path}: expected pH {PH!r}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    if "variant_children" not in repaired:
        _put_after(repaired, "variant_children", [], "curation_history")
    children = repaired["variant_children"]
    if not isinstance(children, list):
        raise ValueError(f"{PARENT}: variant_children is not a list")
    _upsert_child_entry(children, _child_entry())
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked KOMODO Medium 945.1 as a Marinitoga strain variant",
            "source": "KOMODO Medium 945.1",
            "notes": "Linked the strain-specific DSM 14283 MARINITOGA PIEZOPHILA record.",
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(), "curation_history")
    _put_after(repaired, "variant_relationship", RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [CHILD_NOTES], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 945",
            "source": "KOMODO Medium 945.1",
            "notes": CHILD_NOTES,
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
