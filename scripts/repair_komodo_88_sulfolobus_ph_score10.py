#!/usr/bin/env python3
"""Repair the KOMODO Medium 88.2 Sulfolobus pH variant."""

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

PARENT = Path("archaea/KOMODO_88_SULFOLOBUS_medium.yaml")
CHILD = Path("bacterial/KOMODO_88-2_For_DSM_18786.yaml")

PARENT_ID = "CultureMech:006740"
CHILD_ID = "CultureMech:006726"
PARENT_NAME = "sulfolobus_medium"
CHILD_NAME = "for_dsm_18786"

BASE_SIGNATURE = (
    "(NH4)2SO4",
    "KH2PO4",
    "MgSO4 x 7 H2O",
    "CaCl2 x 2 H2O",
    "FeCl3 x 6 H2O",
    "Sulfur",
    "Yeast extract",
    "Na2S x 9 H2O",
    "MnCl2 x 4 H2O",
    "Na2B4O7 x 10 H2O",
    "ZnSO4 x 7 H2O",
    "CuCl2 x 2 H2O",
    "Na2MoO4 x 2 H2O",
    "VOSO4 x 2 H2O",
    "CoSO4 x 7 H2O",
)
PARENT_SIGNATURE = BASE_SIGNATURE + ("H2SO4",)

CURATOR = "repair_komodo_88_sulfolobus_ph_score10.py"
ACTION = "RESOLVED_KOMODO_88_SULFOLOBUS_PH_VARIANT"
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


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": "PH_VARIANT",
        "id": CHILD_ID,
        "name": CHILD_NAME,
        "notes": "KOMODO Medium 88.2 applies SULFOLOBUS medium at pH 0.8.",
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "PH_VARIANT",
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 88 is the pH 2.0 SULFOLOBUS base.",
    }


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT}: expected {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != "komodo.medium:88":
        raise ValueError(f"{PARENT}: expected komodo.medium:88")
    if doc.get("ph_value") != 2.0:
        raise ValueError(f"{PARENT}: expected pH 2.0")
    if _ingredient_signature(doc) != PARENT_SIGNATURE:
        raise ValueError(f"{PARENT}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "variant_children", [_child_entry()], "kg_microbe_match")
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Added KOMODO 88.2 pH variant child",
            "source": "KOMODO Medium 88.2",
            "notes": "Linked the reviewed pH 0.8 DSM 18786 variant.",
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != CHILD_ID:
        raise ValueError(f"{CHILD}: expected {CHILD_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != "komodo.medium:88.2":
        raise ValueError(f"{CHILD}: expected komodo.medium:88.2")
    if doc.get("ph_value") != 0.8:
        raise ValueError(f"{CHILD}: expected pH 0.8")
    if _ingredient_signature(doc) != BASE_SIGNATURE:
        raise ValueError(f"{CHILD}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(), "kg_microbe_match")
    _put_after(repaired, "variant_relationship", "PH_VARIANT", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        ["KOMODO Medium 88.2 specifies pH 0.8 for DSM 18786."],
        "variant_relationship",
    )
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO 88 pH variant",
            "source": "KOMODO Medium 88.2",
            "notes": "Marked DSM 18786 as a pH 0.8 SULFOLOBUS variant.",
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
