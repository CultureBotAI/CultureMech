#!/usr/bin/env python3
"""Repair KOMODO Medium 670 MS-MEDIUM pH variants."""

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

PARENT = Path("bacterial/KOMODO_670_MS-MEDIUM.yaml")
PARENT_ID = "CultureMech:006265"
PARENT_NAME = "ms_medium"


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    media_term_id: str
    source_label: str
    ph_value: float
    has_h2so4: bool


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_9463.yaml"),
        "CultureMech:006260",
        "komodo.medium:670.1",
        "KOMODO Medium 670.1",
        3.5,
        True,
    ),
    Child(
        Path("bacterial/for_dsm_9466.yaml"),
        "CultureMech:006262",
        "komodo.medium:670.3",
        "KOMODO Medium 670.3",
        3.5,
        True,
    ),
    Child(
        Path("bacterial/for_dsm_9467.yaml"),
        "CultureMech:006263",
        "komodo.medium:670.4",
        "KOMODO Medium 670.4",
        3.0,
        True,
    ),
    Child(
        Path("bacterial/for_dsm_9468.yaml"),
        "CultureMech:006264",
        "komodo.medium:670.5",
        "KOMODO Medium 670.5",
        1.6,
        False,
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}

SOURCE_DUPLICATE_CHILDREN = (
    {
        "path": "data/normalized_yaml/bacterial/acidiferrobacter_ms_medium.yaml",
        "relationship": "SOURCE_DUPLICATE",
        "id": "CultureMech:001811",
        "name": "acidiferrobacter_ms_medium",
        "notes": (
            "Same ingredient and concentration signature; review as possible "
            "duplicate source record."
        ),
    },
    {
        "path": "data/normalized_yaml/bacterial/for_dsm_2392_dsm_9464_and_dsm_9465.yaml",
        "relationship": "SOURCE_DUPLICATE",
        "id": "CultureMech:006261",
        "name": "for_dsm_2392_dsm_9464_and_dsm_9465",
        "notes": (
            "Same ingredient and concentration signature; review as possible "
            "duplicate source record."
        ),
    },
)

BASE_SIGNATURE = (
    "(NH4)2SO4",
    "MgSO4 x 7 H2O",
    "K2HPO4",
    "KCl",
    "FeSO4 x 7 H2O",
)
H2SO4_SIGNATURE = BASE_SIGNATURE + ("H2SO4",)
EXPECTED_TARGET_COUNT = 4

CURATOR = "repair_komodo_670_ms_ph_score10.py"
ACTION = "RESOLVED_KOMODO_670_MS_PH_VARIANTS"
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
        str(row.get("preferred_term") or "")
        for row in ingredients
        if isinstance(row, dict)
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


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": "PH_VARIANT",
        "id": child.record_id,
        "name": child.path.stem,
        "notes": (
            f"{child.source_label} applies MS-MEDIUM at pH {child.ph_value:g} "
            "for the named DSM strain."
        ),
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "PH_VARIANT",
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": (
            f"KOMODO Medium 670 is the pH 2.2 MS-MEDIUM base for "
            f"{child.source_label}."
        ),
    }


def _validate_targets() -> None:
    if len(CHILDREN) != EXPECTED_TARGET_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT}: expected {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != "komodo.medium:670":
        raise ValueError(f"{PARENT}: expected komodo.medium:670")
    if _ingredient_signature(doc) != BASE_SIGNATURE:
        raise ValueError(f"{PARENT}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "variant_children",
        [*SOURCE_DUPLICATE_CHILDREN, *[_child_entry(child) for child in CHILDREN]],
        "kg_microbe_match",
    )
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Added KOMODO 670 pH variant children",
            "source": "KOMODO Medium 670 child records",
            "notes": "Linked reviewed pH-specific KOMODO 670 strain variants.",
        },
    )
    return repaired


def repair_child(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = CHILD_BY_PATH[path]
    if doc.get("id") != child.record_id:
        raise ValueError(f"{path}: expected {child.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != child.media_term_id:
        raise ValueError(f"{path}: expected {child.media_term_id}")

    expected_signature = H2SO4_SIGNATURE if child.has_h2so4 else BASE_SIGNATURE
    if _ingredient_signature(doc) != expected_signature:
        raise ValueError(f"{path}: ingredient signature drifted")

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "parent_media", _parent_ref(child), "kg_microbe_match")
    _put_after(repaired, "variant_relationship", "PH_VARIANT", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [
            f"{child.source_label} specifies pH {child.ph_value:g} "
            "for this DSM-specific MS-MEDIUM variant."
        ],
        "variant_relationship",
    )
    _ensure_ingredients_curated(repaired)
    _ensure_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO 670 pH variant",
            "source": child.source_label,
            "notes": (
                f"Marked {child.source_label} as a pH {child.ph_value:g} "
                "strain-specific MS-MEDIUM variant."
            ),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()

    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for child in CHILDREN:
        path = normalized / child.path
        plans[path] = repair_child(child.path, _load(path))
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
