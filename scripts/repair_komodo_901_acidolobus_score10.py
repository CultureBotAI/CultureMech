#!/usr/bin/env python3
"""Repair KOMODO 901 Acidolobus exact and strain child links."""

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

DSMZ_PARENT = Path("archaea/acidolobus_aceticus_medium.yaml")
DSMZ_PARENT_ID = "CultureMech:002067"
DSMZ_PARENT_NAME = "acidolobus_aceticus_medium"
DSMZ_PARENT_SOURCE_TERM = "mediadive.medium:901"

KOMODO_PARENT = Path("archaea/KOMODO_901_ACIDOLOBUS_ACETICUS_medium.yaml")
KOMODO_PARENT_ID = "CultureMech:006771"
KOMODO_PARENT_NAME = "acidolobus_aceticus_medium"
KOMODO_PARENT_SOURCE_TERM = "komodo.medium:901"

CHILD = Path("bacterial/for_dsm_16705.yaml")
CHILD_ID = "CultureMech:006770"
CHILD_SOURCE_TERM = "komodo.medium:901.1"

SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
SOURCE_DUPLICATE_NOTES = (
    "KOMODO Medium 901 has the same 28-ingredient signature as DSMZ Medium 901."
)
STRAIN_NOTES = "KOMODO Medium 901.1 applies KOMODO Medium 901 to DSM 16705."

SIGNATURE = (
    ("NH4Cl", "0.324484", "G_PER_L"),
    ("KCl", "0.324484", "G_PER_L"),
    ("KH2PO4", "0.324484", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.324484", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.324484", "G_PER_L"),
    ("Sodium resazurin", "0.000491642", "G_PER_L"),
    ("Sulfur", "9.83284", "G_PER_L"),
    ("Yeast extract", "2.94985", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
    ("Biotin", "0.02", "G_PER_L"),
    ("Folic acid", "0.02", "G_PER_L"),
    ("Pyridoxine hydrochloride", "0.1", "G_PER_L"),
    ("Thiamine HCl", "0.05", "G_PER_L"),
    ("Riboflavin", "0.05", "G_PER_L"),
    ("Nicotinic acid", "0.05", "G_PER_L"),
    ("Calcium D-(+)-pantothenate", "0.05", "G_PER_L"),
    ("Vitamin B12", "0.001", "G_PER_L"),
    ("p-Aminobenzoic acid", "0.05", "G_PER_L"),
    ("(DL)-alpha-Lipoic acid", "0.05", "G_PER_L"),
    ("Na2S x 9 H2O", "30", "G_PER_L"),
)

CURATOR = "repair_komodo_901_acidolobus_score10.py"
ACTION = "RESOLVED_KOMODO_901_ACIDOLOBUS_TOPOLOGY"
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


def _komodo_child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{KOMODO_PARENT}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT.name,
        "notes": SOURCE_DUPLICATE_NOTES,
    }


def _strain_child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": CHILD_ID,
        "name": CHILD.stem,
        "notes": STRAIN_NOTES,
    }


def _dsmz_parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{DSMZ_PARENT}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": DSMZ_PARENT_ID,
        "name": DSMZ_PARENT_NAME,
        "notes": SOURCE_DUPLICATE_NOTES,
    }


def _komodo_parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{KOMODO_PARENT}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT_NAME,
        "notes": STRAIN_NOTES,
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
    if _ingredient_signature(doc) != SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_dsmz_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, DSMZ_PARENT, DSMZ_PARENT_ID, DSMZ_PARENT_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "variant_children", [_komodo_child_entry()], "curation_history")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Corrected DSMZ Medium 901 source-duplicate child path",
            "source": "DSMZ Medium 901; KOMODO Medium 901",
            "notes": "Pointed the KOMODO Medium 901 child link at the archaeal file.",
        },
    )
    return repaired


def repair_komodo_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, KOMODO_PARENT, KOMODO_PARENT_ID, KOMODO_PARENT_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "variant_children", [_strain_child_entry()], "curation_history")
    _put_after(repaired, "parent_media", _dsmz_parent_ref(), "variant_children")
    _put_after(
        repaired,
        "variant_relationship",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "parent_media",
    )
    _put_after(
        repaired,
        "variant_modifications",
        [SOURCE_DUPLICATE_NOTES],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Changed KOMODO Medium 901 DSM wrapper to a strain variant",
            "source": "KOMODO Medium 901.1",
            "notes": "Kept KOMODO Medium 901 as the DSMZ Medium 901 source duplicate parent.",
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _komodo_parent_ref(), "curation_history")
    _put_after(repaired, "variant_relationship", STRAIN_RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [STRAIN_NOTES], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 901 as STRAIN_SPECIFIC_VARIANT",
            "source": "KOMODO Medium 901.1",
            "notes": STRAIN_NOTES,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    dsmz_path = normalized / DSMZ_PARENT
    parent_path = normalized / KOMODO_PARENT
    child_path = normalized / CHILD
    return {
        dsmz_path: repair_dsmz_parent(_load(dsmz_path)),
        parent_path: repair_komodo_parent(_load(parent_path)),
        child_path: repair_child(_load(child_path)),
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
