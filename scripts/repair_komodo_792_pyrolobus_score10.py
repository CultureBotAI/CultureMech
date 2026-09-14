#!/usr/bin/env python3
"""Repair KOMODO 792 Pyrolobus exact and concentration child links."""

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

PARENT = Path("archaea/KOMODO_792_PYROLOBUS_FUMARII_MEDIUM.yaml")
PARENT_ID = "CultureMech:006501"
PARENT_NAME = "pyrolobus_fumarii_medium"
PARENT_SOURCE_TERM = "komodo.medium:792"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
CONCENTRATION_RELATIONSHIP = "CONCENTRATION_VARIANT"

BASE_SIGNATURE = (
    ("NaCl", "40.3337", "G_PER_L"),
    ("MgSO4 x 7 H2O", "33.53893", "G_PER_L"),
    ("MgCl2 x 6 H2O", "2.78059", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1.7583419999999998", "G_PER_L"),
    ("KCl", "0.33367", "G_PER_L"),
    ("NaBr", "0.0505561", "G_PER_L"),
    ("H3BO3", "0.1151668", "G_PER_L"),
    ("SrCl2 x 6 H2O", "0.00707786", "G_PER_L"),
    ("KI", "5.05561e-05", "G_PER_L"),
    ("Sodium resazurin", "0.000505561", "G_PER_L"),
    ("KNO3", "100", "G_PER_L"),
    ("KH2PO4", "50", "G_PER_L"),
    ("Na2S x 9 H2O", "15", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.1", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.18", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.1", "G_PER_L"),
    ("(NH4)2Ni(SO4)2 x 6 H2O", "2.8", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.1", "G_PER_L"),
    ("Na2SeO4", "0.1", "G_PER_L"),
)
THERMOVIBRIO_SIGNATURE = (
    ("NaCl", "30.2224", "G_PER_L"),
    *BASE_SIGNATURE[1:],
)


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    relationship: str
    notes: str
    signature: tuple[tuple[str, str, str], ...]


CHILDREN = (
    Child(
        Path("bacterial/caminibacter_mediatlanticus_medium.yaml"),
        "CultureMech:001934",
        "mediadive.medium:792b",
        "DSMZ Medium 792b",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "DSMZ Medium 792b has the same 19-ingredient signature as KOMODO Medium 792.",
        BASE_SIGNATURE,
    ),
    Child(
        Path("bacterial/dsm_16658.yaml"),
        "CultureMech:006500",
        "komodo.medium:792.2",
        "KOMODO Medium 792.2",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 792.2 applies Pyrolobus fumarii medium to DSM 16658.",
        BASE_SIGNATURE,
    ),
    Child(
        Path("bacterial/for_dsm_15698_and_dsm_24425.yaml"),
        "CultureMech:006499",
        "komodo.medium:792.1",
        "KOMODO Medium 792.1",
        STRAIN_RELATIONSHIP,
        (
            "KOMODO Medium 792.1 applies Pyrolobus fumarii medium to DSM 15698 "
            "and DSM 24425."
        ),
        BASE_SIGNATURE,
    ),
    Child(
        Path("bacterial/thermovibrio_ammonificans_medium.yaml"),
        "CultureMech:001933",
        "mediadive.medium:792a",
        "DSMZ Medium 792a",
        CONCENTRATION_RELATIONSHIP,
        (
            "DSMZ Medium 792a shares the KOMODO Medium 792 ingredient identity "
            "signature with lower NaCl and pH 5.8."
        ),
        THERMOVIBRIO_SIGNATURE,
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 4

CURATOR = "repair_komodo_792_pyrolobus_score10.py"
ACTION = "RESOLVED_KOMODO_792_PYROLOBUS_TOPOLOGY"
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
    signature: tuple[tuple[str, str, str], ...],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ingredient_signature(doc) != signature:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, BASE_SIGNATURE)


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
        child.signature,
    )


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
            "changes": "Resolved KOMODO Medium 792 Pyrolobus child topology",
            "source": "DSMZ Medium 792a, 792b; KOMODO Medium 792.1 and 792.2",
            "notes": (
                "Moved exact DSMZ 792b and KOMODO strain wrappers plus the "
                "DSMZ 792a NaCl/pH concentration variant under the KOMODO "
                "Medium 792 Pyrolobus base."
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
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": f"Linked as a KOMODO Medium 792 {child.relationship}",
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
