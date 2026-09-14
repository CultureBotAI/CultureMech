#!/usr/bin/env python3
"""Repair KOMODO 1132.1 LC 2 strain child link."""

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

PARENT = Path("bacterial/KOMODO_1132_LC_2.yaml")
PARENT_ID = "CultureMech:003842"
PARENT_NAME = "lc_2"
PARENT_SOURCE_TERM = "komodo.medium:1132"
PH = 6.8

CHILD = Path("bacterial/for_dsm_22980.yaml")
CHILD_ID = "CultureMech:003841"
CHILD_SOURCE_TERM = "komodo.medium:1132.1"
RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
CHILD_NOTES = "KOMODO Medium 1132.1 applies LC 2 to DSM 22980."

SOURCE_DUPLICATE_PARENT = {
    "path": "data/normalized_yaml/bacterial/lc_2.yaml",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:000568",
    "name": "lc_2",
    "notes": "Exact DSMZ/KOMODO medium-number match with matching ingredient and concentration signature.",
}

INGREDIENT_SIGNATURE = (
    ("MgSO4 x 7 H2O", "1", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.2", "G_PER_L"),
    ("KNO3", "0.05", "G_PER_L"),
    ("HEPES buffer", "0.4766", "G_PER_L"),
    ("Fe(III)NH4-EDTA", "1", "G_PER_L"),
    ("Methanol", "0.2376", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
    ("Na2HPO4", "36", "G_PER_L"),
    ("KH2PO4", "14", "G_PER_L"),
)

CURATOR = "repair_komodo_1132_lc2_score10.py"
ACTION = "RESOLVED_KOMODO_1132_LC2_TOPOLOGY"
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


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": RELATIONSHIP,
        "id": CHILD_ID,
        "name": CHILD.stem,
        "notes": CHILD_NOTES,
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 1132 is the LC 2 base for KOMODO Medium 1132.1.",
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


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    if doc.get("parent_media") != SOURCE_DUPLICATE_PARENT:
        raise ValueError(f"{PARENT}: expected DSMZ 1132 source-duplicate parent")
    if doc.get("variant_relationship") != "SOURCE_DUPLICATE":
        raise ValueError(f"{PARENT}: expected SOURCE_DUPLICATE parent relationship")


def _require_child(doc: dict[str, Any]) -> None:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM)


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "variant_children", [_child_entry()], "curation_history")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 1132.1 as a strain variant",
            "source": "KOMODO Medium 1132 and 1132.1",
            "notes": (
                "Linked KOMODO Medium 1132.1 under the KOMODO Medium 1132 "
                "LC 2 base while preserving the DSMZ 1132 duplicate parent "
                "relationship."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_child(doc)

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
            "changes": "Linked under KOMODO Medium 1132",
            "source": "KOMODO Medium 1132.1",
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
