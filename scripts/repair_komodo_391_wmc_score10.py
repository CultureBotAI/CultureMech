#!/usr/bin/env python3
"""Repair KOMODO 391 WMC / Methanococcus voltae strain child links."""

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

PARENT = Path("archaea/methanococcus_voltae_medium.yaml")
PARENT_ID = "CultureMech:001498"
PARENT_NAME = "methanococcus_voltae_medium"
PARENT_SOURCE_TERM = "mediadive.medium:391"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

INGREDIENT_SIGNATURE = (
    ("Na-acetate", "1", "G_PER_L"),
    ("Sodium resazurin", "0.0005", "G_PER_L"),
    ("Na2CO3", "1.5", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.5", "G_PER_L"),
    ("Na2S x 9 H2O", "0.5", "G_PER_L"),
    ("NaCl", "41.0", "G_PER_L"),
    ("MgCl2 x 6 H2O", "5.6", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.7", "G_PER_L"),
    ("KCl", "0.68", "G_PER_L"),
    ("NH4Cl", "0.5", "G_PER_L"),
    ("K2HPO4", "0.28", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.38", "G_PER_L"),
    ("L-Leucine", "5", "G_PER_L"),
    ("L-Isoleucine", "10", "G_PER_L"),
    ("Pantothenate", "0.1", "G_PER_L"),
    ("Casamino acids", "100", "G_PER_L"),
    ("Yeast extract", "50", "G_PER_L"),
    ("L-Tryptophan", "1", "G_PER_L"),
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
)


@dataclass(frozen=True)
class SourceDuplicate:
    path: Path
    record_id: str
    source_term: str
    source_label: str


@dataclass(frozen=True)
class StrainChild:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    target: str


SOURCE_DUPLICATE = SourceDuplicate(
    Path("bacterial/wmc_medium.yaml"),
    "CultureMech:005175",
    "komodo.medium:391",
    "KOMODO Medium 391",
)

STRAIN_CHILDREN = (
    StrainChild(
        Path("bacterial/KOMODO_391-1_For_DSM_4254.yaml"),
        "CultureMech:005173",
        "komodo.medium:391.1",
        "KOMODO Medium 391.1",
        "DSM 4254",
    ),
    StrainChild(
        Path("bacterial/for_strain_dsm_4310.yaml"),
        "CultureMech:005174",
        "komodo.medium:391.2",
        "KOMODO Medium 391.2",
        "DSM 4310",
    ),
)
STRAIN_CHILD_BY_PATH = {child.path: child for child in STRAIN_CHILDREN}
EXPECTED_STRAIN_CHILD_COUNT = 2

CURATOR = "repair_komodo_391_wmc_score10.py"
ACTION = "RESOLVED_KOMODO_391_WMC_TOPOLOGY"
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
    if len(STRAIN_CHILDREN) != EXPECTED_STRAIN_CHILD_COUNT or len(
        STRAIN_CHILDREN
    ) != len(STRAIN_CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_STRAIN_CHILD_COUNT} unique strain children, "
            f"found {len(STRAIN_CHILDREN)} total and {len(STRAIN_CHILD_BY_PATH)} unique"
        )


def _duplicate_notes() -> str:
    return (
        "KOMODO Medium 391 has the same 30-component WMC/Methanococcus "
        "voltae medium signature as DSMZ Medium 391."
    )


def _strain_notes(child: StrainChild) -> str:
    return f"{child.source_label} applies WMC medium to {child.target}."


def _source_duplicate_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{SOURCE_DUPLICATE.path}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": SOURCE_DUPLICATE.record_id,
        "name": SOURCE_DUPLICATE.path.stem,
        "notes": _duplicate_notes(),
    }


def _strain_child_entry(child: StrainChild) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": _strain_notes(child),
    }


def _parent_ref(relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": notes,
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


def _require_source_duplicate(doc: dict[str, Any]) -> None:
    _require_record(
        doc,
        SOURCE_DUPLICATE.path,
        SOURCE_DUPLICATE.record_id,
        SOURCE_DUPLICATE.source_term,
    )


def _require_strain_child(child: StrainChild, doc: dict[str, Any]) -> None:
    _require_record(doc, child.path, child.record_id, child.source_term)


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
        [
            _source_duplicate_entry(),
            *[_strain_child_entry(child) for child in STRAIN_CHILDREN],
        ],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Promoted DSMZ Medium 391 as the WMC parent",
            "source": "DSMZ Medium 391; KOMODO Medium 391, 391.1, and 391.2",
            "notes": (
                "Moved the exact-signature KOMODO Medium 391 source duplicate "
                "and DSM-specific strain wrappers under the DSMZ Medium 391 base."
            ),
        },
    )
    return repaired


def repair_source_duplicate(doc: dict[str, Any]) -> dict[str, Any]:
    _require_source_duplicate(doc)

    notes = _duplicate_notes()
    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(SOURCE_DUPLICATE_RELATIONSHIP, notes),
        "curation_history",
    )
    _put_after(
        repaired,
        "variant_relationship",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "parent_media",
    )
    _put_after(repaired, "variant_modifications", [notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under DSMZ Medium 391",
            "source": SOURCE_DUPLICATE.source_label,
            "notes": notes,
        },
    )
    return repaired


def repair_strain_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = STRAIN_CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected strain child path {relative_path}")
    _require_strain_child(child, doc)

    notes = _strain_notes(child)
    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(STRAIN_RELATIONSHIP, notes),
        "curation_history",
    )
    _put_after(repaired, "variant_relationship", STRAIN_RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO Medium 391 strain-specific variant",
            "source": child.source_label,
            "notes": notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    plans[normalized / SOURCE_DUPLICATE.path] = repair_source_duplicate(
        _load(normalized / SOURCE_DUPLICATE.path)
    )
    for child in STRAIN_CHILDREN:
        plans[normalized / child.path] = repair_strain_child(
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
