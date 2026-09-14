#!/usr/bin/env python3
"""Repair KOMODO 282 Methanococcus exact and strain child links."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

DSMZ_PARENT = Path("archaea/methanocaldococcus_medium.yaml")
DSMZ_PARENT_ID = "CultureMech:001378"
DSMZ_PARENT_NAME = "methanocaldococcus_medium"
DSMZ_PARENT_SOURCE_TERM = "mediadive.medium:282"

KOMODO_PARENT = Path("archaea/methanococcus_jannaschii_medium.yaml")
KOMODO_PARENT_ID = "CultureMech:004739"
KOMODO_PARENT_NAME = "methanococcus_jannaschii_medium"
KOMODO_PARENT_SOURCE_TERM = "komodo.medium:282"

SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
SOURCE_DUPLICATE_NOTES = (
    "KOMODO Medium 282 has the same 34-ingredient signature as DSMZ Medium 282."
)

INGREDIENT_SIGNATURE = (
    ("K2HPO4", "0.13834", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.23834", "G_PER_L"),
    ("NH4Cl", "0.247036", "G_PER_L"),
    ("MgSO4 x 7 H2O", "6.35968", "G_PER_L"),
    ("MgCl2 x 6 H2O", "4.05138", "G_PER_L"),
    ("KCl", "0.326087", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.030494070999999998", "G_PER_L"),
    ("NaCl", "30.6443", "G_PER_L"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "0.00988142", "G_PER_L"),
    ("Sodium resazurin", "0.000494071", "G_PER_L"),
    ("NaHCO3", "0.988142", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.494071", "G_PER_L"),
    ("Na2S x 9 H2O", "0.494071", "G_PER_L"),
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MnSO4 x H2O", "0.5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.18", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.18", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.02", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.0003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.0004", "G_PER_L"),
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
)


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    notes: str


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_22549.yaml"),
        "CultureMech:004736",
        "komodo.medium:282.1",
        "KOMODO Medium 282.1",
        "KOMODO Medium 282.1 applies KOMODO Medium 282 to DSM 22549.",
    ),
    Child(
        Path("bacterial/for_dsm_22612.yaml"),
        "CultureMech:004737",
        "komodo.medium:282.2",
        "KOMODO Medium 282.2",
        "KOMODO Medium 282.2 applies KOMODO Medium 282 to DSM 22612.",
    ),
    Child(
        Path("bacterial/medium_282_modified_for_dsm_16983.yaml"),
        "CultureMech:004735",
        "komodo.medium:282_16983",
        "KOMODO Medium 282_16983",
        "KOMODO Medium 282_16983 applies KOMODO Medium 282 to DSM 16983.",
    ),
    Child(
        Path("bacterial/medium_282_modified_for_dsm_5666.yaml"),
        "CultureMech:004738",
        "komodo.medium:282_5666",
        "KOMODO Medium 282_5666",
        "KOMODO Medium 282_5666 applies KOMODO Medium 282 to DSM 5666.",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 4

CURATOR = "repair_komodo_282_methanococcus_score10.py"
ACTION = "RESOLVED_KOMODO_282_METHANOCOCCUS_TOPOLOGY"
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


def _validate_targets() -> None:
    if len(CHILDREN) != EXPECTED_CHILD_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_CHILD_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def _komodo_child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{KOMODO_PARENT}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT_NAME,
        "notes": SOURCE_DUPLICATE_NOTES,
    }


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": child.notes,
    }


def _dsmz_parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{DSMZ_PARENT}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": DSMZ_PARENT_ID,
        "name": DSMZ_PARENT_NAME,
        "notes": SOURCE_DUPLICATE_NOTES,
    }


def _komodo_parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{KOMODO_PARENT}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT_NAME,
        "notes": child.notes,
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
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_dsmz_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, DSMZ_PARENT, DSMZ_PARENT_ID, DSMZ_PARENT_SOURCE_TERM)


def _require_komodo_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, KOMODO_PARENT, KOMODO_PARENT_ID, KOMODO_PARENT_SOURCE_TERM)


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)


def repair_dsmz_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_dsmz_parent(doc)

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
            "changes": "Re-rooted KOMODO Medium 282 exact topology under DSMZ Medium 282",
            "source": "DSMZ Medium 282; KOMODO Medium 282",
            "notes": "Pointed the KOMODO Medium 282 child link at the archaeal file.",
        },
    )
    return repaired


def repair_komodo_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_komodo_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "variant_children",
        [_child_entry(child) for child in CHILDREN],
        "curation_history",
    )
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
            "changes": "Linked exact KOMODO Medium 282 DSM strain wrappers",
            "source": "KOMODO Medium 282 and exact 282 strain wrapper records",
            "notes": "Moved exact strain wrapper records below the KOMODO Medium 282 parent.",
        },
    )
    return repaired


def repair_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected child path {relative_path}")
    _require_child(child, doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _komodo_parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", STRAIN_RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 282 as STRAIN_SPECIFIC_VARIANT",
            "source": child.source_label,
            "notes": child.notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    dsmz_path = normalized / DSMZ_PARENT
    komodo_path = normalized / KOMODO_PARENT
    plans = {
        dsmz_path: repair_dsmz_parent(_load(dsmz_path)),
        komodo_path: repair_komodo_parent(_load(komodo_path)),
    }
    for child in CHILDREN:
        plans[normalized / child.path] = repair_child(
            child.path,
            _load(normalized / child.path),
        )
    return plans


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
