#!/usr/bin/env python3
"""Repair KOMODO 1101.1 Desulfonatronospira strain child link."""

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

PARENT = Path("bacterial/KOMODO_1101_DESULFONATRONOSPIRA_medium.yaml")
PARENT_ID = "CultureMech:003802"
PARENT_NAME = "desulfonatronospira_medium"
PARENT_SOURCE_TERM = "komodo.medium:1101"

CHILD = Path("bacterial/for_dsm_19491.yaml")
CHILD_ID = "CultureMech:003801"
CHILD_SOURCE_TERM = "komodo.medium:1101.1"
RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
CHILD_NOTES = "KOMODO Medium 1101.1 applies DESULFONATRONOSPIRA medium to DSM 19491."

SOURCE_DUPLICATE_PARENT = {
    "path": "data/normalized_yaml/bacterial/desulfonatronospira_medium.yaml",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:000534",
    "name": "desulfonatronospira_medium",
    "notes": "Exact DSMZ/KOMODO medium-number match with matching ingredient and concentration signature.",
}

PH = 10.0
INGREDIENT_SIGNATURE = (
    ("NaCl", "14.9551", "G_PER_L"),
    ("K2HPO4", "0.498504", "G_PER_L"),
    ("NaHCO3", "14.9551", "G_PER_L"),
    ("Na2CO3", "94.7159", "G_PER_L"),
    ("NH4Cl", "0.199402", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.199402", "G_PER_L"),
    ("Yeast extract", "0.0498504", "G_PER_L"),
    ("Na-L-lactate", "2.19342", "G_PER_L"),
    ("Na2SO3", "1.29611", "G_PER_L"),
    ("Na2S x 9 H2O", "0.239282", "G_PER_L"),
    ("EDTA", "5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "2.2", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.03", "G_PER_L"),
    ("H3BO3", "0.03", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.03", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.03", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.03", "G_PER_L"),
    ("NaOH", "0.5", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
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

CURATOR = "repair_komodo_1101_desulfonatronospira_score10.py"
ACTION = "RESOLVED_KOMODO_1101_DESULFONATRONOSPIRA_TOPOLOGY"
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


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD}",
        "relationship": RELATIONSHIP,
        "id": CHILD_ID,
        "name": CHILD.stem,
        "notes": CHILD_NOTES,
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "KOMODO Medium 1101 is the DESULFONATRONOSPIRA base for KOMODO Medium 1101.1.",
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
    if doc.get("ph_value") != PH:
        raise ValueError(f"{relative_path}: expected pH {PH!r}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    if doc.get("parent_media") != SOURCE_DUPLICATE_PARENT:
        raise ValueError(f"{PARENT}: expected DSMZ 1101 source-duplicate parent")
    if doc.get("variant_relationship") != "SOURCE_DUPLICATE":
        raise ValueError(f"{PARENT}: expected SOURCE_DUPLICATE parent relationship")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "variant_children", [_child_entry()], "curation_history")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 1101.1 as a strain variant",
            "source": "KOMODO Medium 1101 and 1101.1",
            "notes": (
                "Linked KOMODO Medium 1101.1 under the KOMODO Medium 1101 "
                "DESULFONATRONOSPIRA base while preserving the DSMZ 1101 "
                "duplicate parent relationship."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM)

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
            "changes": "Linked under KOMODO Medium 1101",
            "source": "KOMODO Medium 1101.1",
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
