#!/usr/bin/env python3
"""Repair KOMODO 874 strain-specific Ferroplasma child links."""

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

PARENT = Path("archaea/KOMODO_874_FERROPLASMA_ACIDIPHILUM_medium.yaml")
PARENT_ID = "CultureMech:006711"
PARENT_NAME = "ferroplasma_acidiphilum_medium"
PARENT_SOURCE_TERM = "komodo.medium:874"
RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    strain: str


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_16651.yaml"),
        "CultureMech:006709",
        "komodo.medium:874.1",
        "KOMODO Medium 874.1",
        "DSM 16651",
    ),
    Child(
        Path("bacterial/for_dsm_18409.yaml"),
        "CultureMech:006710",
        "komodo.medium:874.2",
        "KOMODO Medium 874.2",
        "DSM 18409",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_TARGET_COUNT = 2

PH_RANGE = {"min": 1.6, "max": 1.8}
INGREDIENT_SIGNATURE = (
    ("MgSO4 x 7 H2O", "0.430108", "G_PER_L"),
    ("(NH4)2SO4", "0.215054", "G_PER_L"),
    ("KCl", "0.107527", "G_PER_L"),
    ("K2HPO4", "0.107527", "G_PER_L"),
    ("FeSO4 x 7 H2O", "500", "G_PER_L"),
    ("H2SO4", "40", "G_PER_L"),
    ("Yeast extract", "20", "G_PER_L"),
    ("FeCl3 x 6 H2O", "1.93", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.18", "G_PER_L"),
    ("Na2B4O7 x 10 H2O", "0.45", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.022", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.005", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.003", "G_PER_L"),
    ("VOSO4 x 5 H2O", "0.0038", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.002", "G_PER_L"),
)

CURATOR = "repair_komodo_874_ferroplasma_score10.py"
ACTION = "RESOLVED_KOMODO_874_FERROPLASMA_TOPOLOGY"
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
    if len(CHILDREN) != EXPECTED_TARGET_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def _child_notes(child: Child) -> str:
    return f"{child.source_label} applies FERROPLASMA ACIDIPHILUM medium to {child.strain}."


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": RELATIONSHIP,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": _child_notes(child),
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": (
            "KOMODO Medium 874 is the FERROPLASMA ACIDIPHILUM base for "
            f"{child.source_label}."
        ),
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
    if doc.get("ph_range") != PH_RANGE:
        raise ValueError(f"{relative_path}: expected pH range {PH_RANGE!r}")
    if doc.get("high_metal") is not True:
        raise ValueError(f"{relative_path}: expected high_metal true")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "variant_children",
        [_child_entry(child) for child in CHILDREN],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 874.1 and 874.2 as strain variants",
            "source": "KOMODO Medium 874, 874.1, and 874.2",
            "notes": (
                "Linked the strain-specific KOMODO Medium 874.1 and 874.2 records "
                "under the KOMODO Medium 874 FERROPLASMA ACIDIPHILUM base."
            ),
        },
    )
    return repaired


def repair_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected child path {relative_path}")
    _require_record(doc, child.path, child.record_id, child.source_term)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", RELATIONSHIP, "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [_child_notes(child)],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 874",
            "source": child.source_label,
            "notes": _child_notes(child),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
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
