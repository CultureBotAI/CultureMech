#!/usr/bin/env python3
"""Reclassify KOMODO 298b.1 DSM 8271 as a strain-specific variant."""

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

PARENT = Path("bacterial/KOMODO_298e_LuPhet1_medium.yaml")
CHILD = Path("bacterial/for_dsm_8271.yaml")

PARENT_ID = "CultureMech:004768"
CHILD_ID = "CultureMech:004764"
PARENT_NAME = "luphet1_medium"
CHILD_NAME = "for_dsm_8271"
PARENT_SOURCE_TERM = "komodo.medium:298e"
CHILD_SOURCE_TERM = "komodo.medium:298b.1"

SIGNATURE = (
    ("KH2PO4", "0.2", "G_PER_L"),
    ("NH4Cl", "0.25", "G_PER_L"),
    ("NaCl", "1", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.4", "G_PER_L"),
    ("KCl", "0.5", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.15", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Sodium resazurin", "0.0005", "G_PER_L"),
    ("Na2CO3", "1.5", "G_PER_L"),
    ("Na-DL-lactate", "1.5", "G_PER_L"),
    ("Na2S x 9 H2O", "0.36", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
    ("NaOH", "0.5", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
    ("Vitamin B12", "0.1", "G_PER_L"),
    ("p-Aminobenzoic acid", "0.08", "G_PER_L"),
    ("D-(+)-biotin", "0.02", "G_PER_L"),
    ("Nicotinic acid", "0.2", "G_PER_L"),
    ("Calcium pantothenate", "0.1", "G_PER_L"),
    ("Pyridoxine hydrochloride", "0.3", "G_PER_L"),
    ("Thiamine-HCl x 2 H2O", "0.2", "G_PER_L"),
)

CURATOR = "repair_komodo_298b1_luphet1_score10.py"
ACTION = "RESOLVED_KOMODO_298B1_LUPHET1_STRAIN_VARIANT"
TIMESTAMP = "2026-09-13T00:00:00-07:00"
RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
NOTE = "KOMODO Medium 298b.1 applies the reviewed LuPhet1 signature to DSM 8271."


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
        "notes": NOTE,
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": NOTE,
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


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    children = repaired.get("variant_children") or []
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")
    repaired["variant_children"] = [
        _child_entry()
        if isinstance(child, dict) and child.get("id") == CHILD_ID
        else child
        for child in children
    ]
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO 298b.1 as strain-specific",
            "source": "KOMODO Medium 298b.1",
            "notes": NOTE,
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, CHILD, CHILD_ID, CHILD_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    repaired["parent_media"] = _parent_ref()
    repaired["variant_relationship"] = RELATIONSHIP
    repaired["variant_modifications"] = [NOTE]
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified under LuPhet1 as strain-specific",
            "source": "KOMODO Medium 298b.1",
            "notes": NOTE,
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
