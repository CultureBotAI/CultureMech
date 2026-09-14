#!/usr/bin/env python3
"""Add reciprocal links for repaired JCM direct-wrapper variants."""

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

CURATOR = "repair_jcm_direct_wrapper_backlinks.py"
ACTION = "ADDED_JCM_DIRECT_WRAPPER_BACKLINKS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

SALINITY_VARIANT = "SALINITY_VARIANT"
SUPPLEMENTED_VARIANT = "SUPPLEMENTED_VARIANT"


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
    relationship: str
    notes: str


RAVOT_R101 = Parent(
    Path("bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml"),
    "CultureMech:010153",
    "ravot_modified_medium_for_thermoanaerovibrio_sp_r101",
    "TOGO:M748",
)
DESULFOVIBRIO = Parent(
    Path("bacterial/TOGO_M384_Desulfovibrio_Medium.yaml"),
    "CultureMech:009765",
    "desulfovibrio_medium",
    "TOGO:M384",
)
NE23_3 = Parent(
    Path("bacterial/TOGO_M505_NE23-3_Medium.yaml"),
    "CultureMech:009895",
    "ne23_3_medium",
    "TOGO:M505",
)

CHILDREN = (
    Child(
        Path("bacterial/TOGO_M749_Ravot_Modified_Medium_For_Fervidobacterium_SP._R8.yaml"),
        "CultureMech:010154",
        "ravot_modified_medium_for_fervidobacterium_sp_r8",
        "TOGO:M749",
        RAVOT_R101,
        SALINITY_VARIANT,
        "Uses Medium 725 with 5.0 g/L NaCl and pH adjusted to 6.3.",
    ),
    Child(
        Path("bacterial/TOGO_M750_Ravot_Modified_Medium_For_Thermosipho_SP._G60.yaml"),
        "CultureMech:010156",
        "ravot_modified_medium_for_thermosipho_sp_g60",
        "TOGO:M750",
        RAVOT_R101,
        SALINITY_VARIANT,
        "Uses Medium 725 with 20.0 g/L NaCl and pH adjusted to 7.0.",
    ),
    Child(
        Path("bacterial/TOGO_M775_Desulfovibrio_Marine_Medium.yaml"),
        "CultureMech:010183",
        "desulfovibrio_marine_medium",
        "TOGO:M775",
        DESULFOVIBRIO,
        SALINITY_VARIANT,
        "Supplements Medium 389 with 25.0 g/L NaCl.",
    ),
    Child(
        Path("bacterial/TOGO_M777_Opitutus_Terrae_Medium.yaml"),
        "CultureMech:010185",
        "opitutus_terrae_medium",
        "TOGO:M777",
        NE23_3,
        SUPPLEMENTED_VARIANT,
        "Supplements Medium 504 with 0.72 g/L glucose.",
    ),
)
PARENTS = (RAVOT_R101, DESULFOVIBRIO, NE23_3)
CHILDREN_BY_PARENT: dict[Path, tuple[Child, ...]] = {
    parent.path: tuple(child for child in CHILDREN if child.parent == parent)
    for parent in PARENTS
}


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
        "notes": "Mirrored curated JCM direct-wrapper parent_media links on the parent record.",
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
        "relationship": child.relationship,
        "id": parent.record_id,
        "name": parent.name,
        "notes": child.notes,
    }


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
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
    if doc.get("variant_relationship") != child.relationship:
        raise ValueError(f"{child.path}: expected {child.relationship}")


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
