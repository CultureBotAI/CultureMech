#!/usr/bin/env python3
"""Repair KOMODO 193a PHB/pyruvate child relationships."""

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

PARENT = Path("bacterial/KOMODO_193a_PHB_PYRUVATE_MEDIUM.yaml")
PARENT_ID = "CultureMech:004228"
PARENT_NAME = "phb_pyruvate_medium"
PARENT_SOURCE_TERM = "komodo.medium:193a"
DSMZ_PARENT_ID = "CultureMech:001286"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

SIGNATURE = (
    ("Na2SO4", "3.18471", "G_PER_L"),
    ("KH2PO4", "0.212314", "G_PER_L"),
    ("NH4Cl", "0.318471", "G_PER_L"),
    ("NaCl", "7.431", "G_PER_L"),
    ("MgCl2 x 6 H2O", "1.38004", "G_PER_L"),
    ("KCl", "0.530786", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.159236", "G_PER_L"),
    ("Poly[(R)-3-hydroxybutyric acid]", "1.06157", "G_PER_L"),
    ("Sodium resazurin", "0.000530786", "G_PER_L"),
    ("Na2CO3", "50", "G_PER_L"),
    ("Na-pyruvate", "250", "G_PER_L"),
    ("Na2S x 9 H2O", "40", "G_PER_L"),
    ("NaOH", "0.5", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
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
)


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
        Path("bacterial/desulfobacter_postgatei_medium.yaml"),
        "CultureMech:004227",
        "komodo.medium:193",
        "KOMODO Medium 193",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "KOMODO Medium 193 has the same 34-ingredient signature as KOMODO Medium 193a.",
    ),
    Child(
        Path("bacterial/for_dsm_14956.yaml"),
        "CultureMech:004220",
        "komodo.medium:193.1",
        "KOMODO Medium 193.1",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193.1 applies KOMODO Medium 193a to DSM 14956.",
    ),
    Child(
        Path("bacterial/for_dsm_15249.yaml"),
        "CultureMech:004221",
        "komodo.medium:193.2",
        "KOMODO Medium 193.2",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193.2 applies KOMODO Medium 193a to DSM 15249.",
    ),
    Child(
        Path("bacterial/for_dsm_18843.yaml"),
        "CultureMech:004222",
        "komodo.medium:193.3",
        "KOMODO Medium 193.3",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193.3 applies KOMODO Medium 193a to DSM 18843.",
    ),
    Child(
        Path("bacterial/for_dsm_15102.yaml"),
        "CultureMech:004223",
        "komodo.medium:193.4",
        "KOMODO Medium 193.4",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193.4 applies KOMODO Medium 193a to DSM 15102.",
    ),
    Child(
        Path("bacterial/for_dsm_16697.yaml"),
        "CultureMech:004224",
        "komodo.medium:193.5",
        "KOMODO Medium 193.5",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193.5 applies KOMODO Medium 193a to DSM 16697.",
    ),
    Child(
        Path("bacterial/medium_193_modified_for_dsm_6637.yaml"),
        "CultureMech:004225",
        "komodo.medium:193_6637",
        "KOMODO Medium 193_6637",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193_6637 applies KOMODO Medium 193a to DSM 6637.",
    ),
    Child(
        Path("bacterial/medium_193_modified_for_dsm_8775.yaml"),
        "CultureMech:004226",
        "komodo.medium:193_8775",
        "KOMODO Medium 193_8775",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 193_8775 applies KOMODO Medium 193a to DSM 8775.",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 8

CURATOR = "repair_komodo_193a_desulfobacter_score10.py"
ACTION = "RESOLVED_KOMODO_193A_DESULFOBACTER_TOPOLOGY"
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


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    parent_media = doc.get("parent_media") or {}
    if not isinstance(parent_media, dict) or parent_media.get("id") != DSMZ_PARENT_ID:
        raise ValueError(f"{PARENT}: expected DSMZ 193a SOURCE_DUPLICATE parent")
    if doc.get("variant_relationship") != SOURCE_DUPLICATE_RELATIONSHIP:
        raise ValueError(f"{PARENT}: expected SOURCE_DUPLICATE parent relationship")


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
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
            "changes": "Changed KOMODO Medium 193a DSM wrappers from duplicates to strain variants",
            "source": "KOMODO Medium 193, 193.1-193.5, 193_6637, 193_8775",
            "notes": "Kept KOMODO Medium 193a as the DSMZ Medium 193a source duplicate parent.",
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
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": f"Linked under KOMODO Medium 193a as {child.relationship}",
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
