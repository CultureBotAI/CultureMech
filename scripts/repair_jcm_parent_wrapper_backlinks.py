#!/usr/bin/env python3
"""Add reciprocal links for repaired JCM parent-wrapper variants."""

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

CURATOR = "repair_jcm_parent_wrapper_backlinks.py"
ACTION = "ADDED_JCM_PARENT_WRAPPER_BACKLINKS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"
RELATIONSHIP = "SUPPLEMENTED_VARIANT"


@dataclass(frozen=True)
class Parent:
    path: Path
    record_id: str
    name: str
    source_term: str


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    parent: Parent
    notes: str


RHODOBIUM = Parent(
    Path("bacterial/TOGO_M517_Rhodobium_Gokurnum_Medium.yaml"),
    "CultureMech:009908",
    "rhodobium_gokurnum_medium",
    "TOGO:M517",
)
THIORHODOCOCCUS = Parent(
    Path("bacterial/TOGO_M565_Thiorhodococcus_Bheemlicum_Medium.yaml"),
    "CultureMech:009960",
    "thiorhodococcus_bheemlicum_medium",
    "TOGO:M565",
)

CHILDREN = (
    Child(
        Path("bacterial/TOGO_M518_Marichromatium_Imhoffii_Medium.yaml"),
        "CultureMech:009909",
        "marichromatium_imhoffii_medium",
        "TOGO:M518",
        RHODOBIUM,
        "Supplements Rhodobium gokurnum medium with 0.5 to 1.0 mM Na2S.",
    ),
    Child(
        Path("bacterial/TOGO_M566_Lamprobacter_Roseus_Medium.yaml"),
        "CultureMech:009961",
        "lamprobacter_roseus_medium",
        "TOGO:M566",
        THIORHODOCOCCUS,
        "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/100 ml).",
    ),
    Child(
        Path("bacterial/TOGO_M574_Allochromatium_Renukaii_Medium.yaml"),
        "CultureMech:009970",
        "allochromatium_renukaii_medium",
        "TOGO:M574",
        THIORHODOCOCCUS,
        "Supplements Medium 561 with 1.0 ml/L vitamin B12 solution (2 mg/ml).",
    ),
)
CHILDREN_BY_PARENT: dict[Path, tuple[Child, ...]] = {
    RHODOBIUM.path: tuple(child for child in CHILDREN if child.parent == RHODOBIUM),
    THIORHODOCOCCUS.path: tuple(
        child for child in CHILDREN if child.parent == THIORHODOCOCCUS
    ),
}
PARENTS = (RHODOBIUM, THIORHODOCOCCUS)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _upsert_event(doc: dict[str, Any], parent: Parent) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Added reciprocal variant_children links",
        "source": parent.source_term,
        "notes": "Mirrored curated JCM wrapper parent_media links on the parent record.",
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


def _parent_ref(parent: Parent, child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{parent.path}",
        "relationship": RELATIONSHIP,
        "id": parent.record_id,
        "name": parent.name,
        "notes": child.notes,
    }


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": RELATIONSHIP,
        "id": child.record_id,
        "name": child.name,
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


def _require_parent(parent: Parent, doc: dict[str, Any]) -> None:
    _require_record(doc, parent.path, parent.record_id, parent.source_term)


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)
    if doc.get("parent_media") != _parent_ref(child.parent, child):
        raise ValueError(f"{child.path}: parent_media no longer matches {child.parent.path}")
    if doc.get("variant_relationship") != RELATIONSHIP:
        raise ValueError(f"{child.path}: expected {RELATIONSHIP}")


def repair_parent(parent: Parent, doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(parent, doc)

    repaired = copy.deepcopy(doc)
    existing_children = repaired.get("variant_children") or []
    if not isinstance(existing_children, list):
        raise ValueError(f"{parent.path}: variant_children is not a list")

    by_id = {
        child.get("id"): child
        for child in existing_children
        if isinstance(child, dict) and child.get("id")
    }
    for child in CHILDREN_BY_PARENT[parent.path]:
        by_id[child.record_id] = _child_entry(child)

    repaired["variant_children"] = [
        by_id.pop(child.get("id"), child)
        for child in existing_children
        if isinstance(child, dict)
    ]
    repaired["variant_children"].extend(
        _child_entry(child)
        for child in CHILDREN_BY_PARENT[parent.path]
        if child.record_id in by_id
    )
    _upsert_event(repaired, parent)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    for child in CHILDREN:
        _require_child(child, _load(normalized / child.path))
    return {
        normalized / parent.path: repair_parent(parent, _load(normalized / parent.path))
        for parent in PARENTS
    }


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
