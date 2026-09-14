#!/usr/bin/env python3
"""Repair the KOMODO Medium 945.2 Marinitoga pH variant."""

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
CHILD = Path("bacterial/for_dsm_17373.yaml")

PARENT_ID = "CultureMech:006880"
CHILD_ID = "CultureMech:006879"
PARENT_NAME = "marinitoga_piezophila_medium"
CHILD_NAME = "for_dsm_17373"

PARENT_SIGNATURE = (
    "NH4Cl",
    "MgCl2 x 6 H2O",
    "CaCl2 x 2 H2O",
    "KCl",
    "NaCl",
    "Na-acetate",
    "MES",
    "Yeast extract",
    "Trypticase peptone",
    "K2HPO4",
    "KH2PO4",
    "Sodium resazurin",
    "Sulfur",
    "L-Cysteine HCl x H2O",
    "Na2S x 9 H2O",
    "NaOH",
)
CHILD_SIGNATURE = PARENT_SIGNATURE[:-1]

CURATOR = "repair_komodo_945_marinitoga_ph_score10.py"
ACTION = "RESOLVED_KOMODO_945_MARINITOGA_PH_VARIANT"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _ingredient_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")
    return tuple(
        str(row.get("preferred_term") or "") for row in ingredients if isinstance(row, dict)
    )


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


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


def _ensure_event(doc: dict[str, Any], event: dict[str, Any]) -> None:
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
        if isinstance(existing, dict) and (
            existing.get("id") == entry["id"] or existing.get("path") == entry["path"]
        ):
            children[index] = entry
            return
    children.append(entry)


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": "PH_VARIANT",
        "id": CHILD_ID,
        "name": CHILD_NAME,
        "notes": "KOMODO Medium 945.2 applies MARINITOGA PIEZOPHILA medium at pH 5.5.",
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "PH_VARIANT",
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 945 is the pH 6.0 MARINITOGA PIEZOPHILA base.",
    }


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT}: expected {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != "komodo.medium:945":
        raise ValueError(f"{PARENT}: expected komodo.medium:945")
    if doc.get("ph_value") != 6.0:
        raise ValueError(f"{PARENT}: expected pH 6.0")
    if _ingredient_signature(doc) != PARENT_SIGNATURE:
        raise ValueError(f"{PARENT}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    if "variant_children" not in repaired:
        _put_after(repaired, "variant_children", [], "curation_history")
    children = repaired["variant_children"]
    if not isinstance(children, list):
        raise ValueError(f"{PARENT}: variant_children is not a list")
    _upsert_child_entry(children, _child_entry())
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Added KOMODO 945.2 pH variant child",
            "source": "KOMODO Medium 945.2",
            "notes": "Linked the reviewed pH 5.5 DSM 17373 variant.",
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != CHILD_ID:
        raise ValueError(f"{CHILD}: expected {CHILD_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != "komodo.medium:945.2":
        raise ValueError(f"{CHILD}: expected komodo.medium:945.2")
    if doc.get("ph_value") != 5.5:
        raise ValueError(f"{CHILD}: expected pH 5.5")
    if _ingredient_signature(doc) != CHILD_SIGNATURE:
        raise ValueError(f"{CHILD}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(), "kg_microbe_match")
    _put_after(repaired, "variant_relationship", "PH_VARIANT", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        ["KOMODO Medium 945.2 specifies pH 5.5 for DSM 17373."],
        "variant_relationship",
    )
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO 945 pH variant",
            "source": "KOMODO Medium 945.2",
            "notes": "Marked DSM 17373 as a pH 5.5 MARINITOGA PIEZOPHILA variant.",
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
