#!/usr/bin/env python3
"""Repair KOMODO 1011 MJ Medium child links."""

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

PARENT = Path("bacterial/mj_medium.yaml")
PARENT_ID = "CultureMech:003521"
PARENT_NAME = "mj_medium"
PARENT_SOURCE_TERM = "komodo.medium:1011"
PARENT_PH = 6.7

STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
PH_RELATIONSHIP = "PH_VARIANT"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"

SOURCE_DUPLICATE_CHILD = {
    "path": "data/normalized_yaml/bacterial/thiobacter_mj_medium.yaml",
    "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
    "id": "CultureMech:000428",
    "name": "thiobacter_mj_medium",
    "notes": (
        "DSMZ Medium 1011a is an independent MediaDive import with the same "
        "32-component MJ Medium signature as KOMODO Medium 1011."
    ),
}

SOURCE_DUPLICATE_PATH = Path("bacterial/thiobacter_mj_medium.yaml")
SOURCE_DUPLICATE_ID = "CultureMech:000428"
SOURCE_DUPLICATE_SOURCE_TERM = "mediadive.medium:1011a"

INGREDIENT_SIGNATURE = (
    ("NaCl", "3.96736", "G_PER_L"),
    ("K2HPO4", "0.138477", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.238477", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.336301", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.41543", "G_PER_L"),
    ("KCl", "0.326409", "G_PER_L"),
    ("NH4Cl", "0.24728", "G_PER_L"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "0.0098912", "G_PER_L"),
    ("NaHCO3", "1.48368", "G_PER_L"),
    ("Na2S2O3 x 5 H2O", "1.48368", "G_PER_L"),
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MnSO4 x H2O", "0.5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.18", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.18", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.02", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.03", "G_PER_L"),
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
    target: str
    relationship: str
    ph: float


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_17375.yaml"),
        "CultureMech:003517",
        "komodo.medium:1011.1",
        "KOMODO Medium 1011.1",
        "DSM 17375",
        STRAIN_RELATIONSHIP,
        6.7,
    ),
    Child(
        Path("bacterial/for_dsm_22050.yaml"),
        "CultureMech:003518",
        "komodo.medium:1011.2",
        "KOMODO Medium 1011.2",
        "DSM 22050",
        PH_RELATIONSHIP,
        6.0,
    ),
    Child(
        Path("bacterial/for_dsm_23290.yaml"),
        "CultureMech:003519",
        "komodo.medium:1011.3",
        "KOMODO Medium 1011.3",
        "DSM 23290",
        STRAIN_RELATIONSHIP,
        6.7,
    ),
    Child(
        Path("bacterial/for_dsm_24660.yaml"),
        "CultureMech:003520",
        "komodo.medium:1011.4",
        "KOMODO Medium 1011.4",
        "DSM 24660",
        PH_RELATIONSHIP,
        6.5,
    ),
    Child(
        Path("bacterial/mj_medium_for_thiobacter_subterraneus.yaml"),
        "CultureMech:003522",
        "komodo.medium:1011a",
        "KOMODO Medium 1011a",
        "Thiobacter subterraneus",
        STRAIN_RELATIONSHIP,
        6.7,
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 5

CURATOR = "repair_komodo_1011_mj_medium_score10.py"
ACTION = "RESOLVED_KOMODO_1011_MJ_MEDIUM_TOPOLOGY"
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


def _child_notes(child: Child) -> str:
    if child.relationship == PH_RELATIONSHIP:
        return (
            f"{child.source_label} applies MJ MEDIUM to {child.target} at pH "
            f"{child.ph:.1f}, not the pH {PARENT_PH:.1f} KOMODO Medium 1011 base."
        )
    return f"{child.source_label} applies MJ MEDIUM to {child.target}."


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": _child_notes(child),
    }


def _source_duplicate_entry() -> dict[str, str]:
    return dict(SOURCE_DUPLICATE_CHILD)


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 1011 is the MJ MEDIUM base for this record.",
    }


def _source_duplicate_parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": SOURCE_DUPLICATE_CHILD["notes"],
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


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    if doc.get("ph_value") != PARENT_PH:
        raise ValueError(f"{PARENT}: expected pH {PARENT_PH!r}")


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)
    if doc.get("ph_value") != child.ph:
        raise ValueError(f"{child.path}: expected pH {child.ph!r}")


def _require_source_duplicate(doc: dict[str, Any]) -> None:
    _require_record(
        doc,
        SOURCE_DUPLICATE_PATH,
        SOURCE_DUPLICATE_ID,
        SOURCE_DUPLICATE_SOURCE_TERM,
    )
    if doc.get("ph_value") != PARENT_PH:
        raise ValueError(f"{SOURCE_DUPLICATE_PATH}: expected pH {PARENT_PH!r}")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "variant_children",
        [_child_entry(child) for child in CHILDREN] + [_source_duplicate_entry()],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 1011 children",
            "source": "KOMODO Medium 1011, 1011.1-1011.4, and 1011a",
            "notes": (
                "Linked the KOMODO 1011 strain and pH children under the "
                "KOMODO Medium 1011 MJ MEDIUM base while preserving the "
                "matching DSMZ Medium 1011a source-duplicate child."
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
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", child.relationship, "parent_media")
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
            "changes": "Linked under KOMODO Medium 1011",
            "source": child.source_label,
            "notes": _child_notes(child),
        },
    )
    return repaired


def repair_source_duplicate(doc: dict[str, Any]) -> dict[str, Any]:
    _require_source_duplicate(doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _source_duplicate_parent_ref(), "curation_history")
    _put_after(
        repaired,
        "variant_relationship",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "parent_media",
    )
    _put_after(
        repaired,
        "variant_modifications",
        [SOURCE_DUPLICATE_CHILD["notes"]],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Documented as a KOMODO Medium 1011 duplicate",
            "source": "DSMZ Medium 1011a",
            "notes": SOURCE_DUPLICATE_CHILD["notes"],
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
    plans[normalized / SOURCE_DUPLICATE_PATH] = repair_source_duplicate(
        _load(normalized / SOURCE_DUPLICATE_PATH)
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
