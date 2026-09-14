#!/usr/bin/env python3
"""Repair KOMODO 614.1 topology rooted at a strain-specific duplicate."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

PARENT = Path("bacterial/acetobacterium_fimetarium_medium.yaml")
PARENT_ID = "CultureMech:001743"
PARENT_NAME = "acetobacterium_fimetarium_medium"
PARENT_SOURCE_TERM = "mediadive.medium:614"
PARENT_PH = {"min": 6.8, "max": 7.0}

CHILD = Path("bacterial/for_dsm_8238.yaml")
CHILD_ID = "CultureMech:006104"
CHILD_NAME = "for_dsm_8238"
CHILD_SOURCE_TERM = "komodo.medium:614.1"
CHILD_PH = 7.5
RELATIONSHIP = "PH_VARIANT"
CHILD_NOTES = (
    "KOMODO Medium 614.1 applies ACETOBACTERIUM FIMETARIUM MEDIUM " "at pH 7.5 for DSM 8238."
)

INGREDIENT_SIGNATURE = (
    ("KCl", "0.326409", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.514342", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.317606", "G_PER_L"),
    ("NH4Cl", "0.326409", "G_PER_L"),
    ("KH2PO4", "0.326409", "G_PER_L"),
    ("Yeast extract", "0.49456", "G_PER_L"),
    ("Sodium resazurin", "0.00049456", "G_PER_L"),
    ("NaHCO3", "0.98912", "G_PER_L"),
    ("D-Fructose", "9.8912", "G_PER_L"),
    ("Na2S x 9 H2O", "0.692384", "G_PER_L"),
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3", "G_PER_L"),
    ("MnSO4 x H2O", "0.5", "G_PER_L"),
    ("NaCl", "1", "G_PER_L"),
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

CURATOR = "repair_komodo_614_acetobacterium_score10.py"
ACTION = "RESOLVED_KOMODO_614_ACETOBACTERIUM_TOPOLOGY"
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


def _ph(doc: dict[str, Any]) -> Any:
    if "ph_value" in doc:
        return doc["ph_value"]
    return doc.get("ph_range")


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


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": RELATIONSHIP,
        "id": CHILD_ID,
        "name": CHILD_NAME,
        "notes": CHILD_NOTES,
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": ("MediaDive Medium 614 is the DSMZ ACETOBACTERIUM FIMETARIUM " "MEDIUM base."),
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ph: Any,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ph(doc) != ph:
        raise ValueError(f"{relative_path}: expected pH {ph!r}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_PH)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
    _put_after(repaired, "variant_children", [_child_entry()], "curation_history")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Promoted MediaDive Medium 614 to the Acetobacterium parent",
            "source": "MediaDive Medium 614 and KOMODO Medium 614.1",
            "notes": (
                "Moved the duplicate edge from the strain-specific KOMODO "
                "Medium 614.1 record to the DSMZ/MediaDive ACETOBACTERIUM "
                "FIMETARIUM MEDIUM record."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM, CHILD_PH)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(), "curation_history")
    _put_after(repaired, "variant_relationship", RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [CHILD_NOTES], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under MediaDive Medium 614",
            "source": "KOMODO Medium 614.1",
            "notes": CHILD_NOTES,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / PARENT: repair_parent(_load(normalized / PARENT)),
        normalized / CHILD: repair_child(_load(normalized / CHILD)),
    }


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
