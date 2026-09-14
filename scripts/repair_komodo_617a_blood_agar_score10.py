#!/usr/bin/env python3
"""Repair KOMODO 617a blood agar exact and strain child links."""

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

PARENT = Path("bacterial/blood_agar_base_oxoid_cm55.yaml")
PARENT_ID = "CultureMech:001747"
PARENT_NAME = "blood_agar_base_oxoid_cm55"
PARENT_SOURCE_TERM = "mediadive.medium:617a"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

PARENT_SIGNATURE = (
    ("Beef extract", "10", "G_PER_L"),
    ("Peptone", "10", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Tap water", "1000", "G_PER_L"),
)
STALE_DSMZ_617_SIGNATURE = (
    ("Beef extract", "10", "G_PER_L"),
    ("Peptone", "10", "G_PER_L"),
    ("NaCl", "30", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Tap water", "1000", "G_PER_L"),
)
VALID_CHILD_SIGNATURES = {PARENT_SIGNATURE, STALE_DSMZ_617_SIGNATURE}


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    relationship: str
    notes: str


CHILDREN = (
    Child(
        Path("bacterial/KOMODO_617a_BLOOD_AGAR_BASE_OXOID_CM55.yaml"),
        "CultureMech:006111",
        "komodo.medium:617a",
        "KOMODO Medium 617a",
        SOURCE_DUPLICATE_RELATIONSHIP,
        (
            "KOMODO Medium 617a has the same 5-ingredient signature as DSMZ "
            "Medium 617a after correcting the stale DSMZ 617 NaCl concentration."
        ),
    ),
    Child(
        Path("bacterial/for_dsm_7232.yaml"),
        "CultureMech:006110",
        "komodo.medium:617a.1",
        "KOMODO Medium 617a.1",
        STRAIN_RELATIONSHIP,
        (
            "KOMODO Medium 617a.1 applies DSMZ Medium 617a to DSM 7232 after "
            "correcting the stale DSMZ 617 NaCl concentration."
        ),
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 2

CURATOR = "repair_komodo_617a_blood_agar_score10.py"
ACTION = "RESOLVED_KOMODO_617A_BLOOD_AGAR_TOPOLOGY"
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


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": child.notes,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": child.notes,
    }


def _require_identity(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_identity(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    if _ingredient_signature(doc) != PARENT_SIGNATURE:
        raise ValueError(f"{PARENT}: ingredient signature drifted")


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_identity(doc, child.path, child.record_id, child.source_term)
    if _ingredient_signature(doc) not in VALID_CHILD_SIGNATURES:
        raise ValueError(f"{child.path}: ingredient signature drifted")


def _correct_nacl_to_617a(doc: dict[str, Any]) -> None:
    matches = [
        row
        for row in doc.get("ingredients", [])
        if isinstance(row, dict) and row.get("preferred_term") == "NaCl"
    ]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one NaCl row, found {len(matches)}")

    concentration = matches[0].setdefault("concentration", {})
    if not isinstance(concentration, dict):
        raise ValueError("NaCl concentration is not a mapping")
    if str(concentration.get("value") or "") not in {"5", "30"}:
        raise ValueError("NaCl concentration drifted from DSMZ 617/617a values")
    concentration["value"] = "5"


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _ensure_ingredients_curated(repaired)
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
            "changes": "Re-rooted KOMODO Medium 617a blood agar topology",
            "source": "DSMZ Medium 617a; KOMODO Medium 617a and 617a.1",
            "notes": (
                "Moved exact KOMODO Medium 617a plus its DSM 7232 wrapper "
                "under DSMZ Medium 617a."
            ),
        },
    )
    return repaired


def repair_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected child path {relative_path}")
    _require_child(child, doc)

    repaired = copy.deepcopy(doc)
    _correct_nacl_to_617a(repaired)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", child.relationship, "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": (
                "Corrected stale DSMZ Medium 617 NaCl concentration and linked "
                f"under DSMZ Medium 617a as {child.relationship}"
            ),
            "source": child.source_label,
            "notes": child.notes,
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
