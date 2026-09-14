#!/usr/bin/env python3
"""Repair KOMODO 479 topology rooted at a strain-specific duplicate."""

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

PARENT = Path("archaea/methanohalophilus_medium.yaml")
PARENT_ID = "CultureMech:000266"
PARENT_NAME = "methanohalophilus_medium"
PARENT_SOURCE_TERM = "mediadive.medium:479"
PARENT_PH = {"min": 7.0, "max": 7.2}

BASE_INGREDIENT_SIGNATURE = (
    ("NaCl", "87.1386", "G_PER_L"),
    ("KCl", "1.48515", "G_PER_L"),
    ("MgCl2 x 6 H2O", "5.94059", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.49604000000000004", "G_PER_L"),
    ("NH4Cl", "0.990099", "G_PER_L"),
    ("K2HPO4 x 3 H2O", "0.39604", "G_PER_L"),
    ("Yeast extract", "1.9802", "G_PER_L"),
    ("Trypticase peptone", "1.9802", "G_PER_L"),
    ("Sodium resazurin", "0.00049505", "G_PER_L"),
    ("Na2CO3", "1.48515", "G_PER_L"),
    ("Trimethylamine-HCl", "1.9802", "G_PER_L"),
    ("2-Mercaptoethanesulfonate", "0.19802", "G_PER_L"),
    ("Na2S x 9 H2O", "0.247525", "G_PER_L"),
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3", "G_PER_L"),
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
NAOH_INGREDIENT_SIGNATURE = (
    *BASE_INGREDIENT_SIGNATURE,
    ("NaOH", "variable", "VARIABLE"),
)

CURATOR = "repair_komodo_479_methanohalophilus_score10.py"
ACTION = "RESOLVED_KOMODO_479_METHANOHALOPHILUS_TOPOLOGY"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def source_label(source_term: str) -> str:
    if source_term.startswith("komodo.medium:"):
        return f"KOMODO Medium {source_term.removeprefix('komodo.medium:')}"
    if source_term.startswith("mediadive.medium:"):
        return f"MediaDive Medium {source_term.removeprefix('mediadive.medium:')}"
    return source_term


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    relationship: str
    ph: Any
    ingredient_signature: tuple[tuple[str, str, str], ...]
    modification: str

    @property
    def source_label(self) -> str:
        return source_label(self.source_term)


CHILDREN = (
    Child(
        Path("archaea/KOMODO_479_METHANOHALOPHILUS_medium.yaml"),
        "CultureMech:005594",
        "methanohalophilus_medium",
        "komodo.medium:479",
        "SOURCE_DUPLICATE",
        PARENT_PH,
        BASE_INGREDIENT_SIGNATURE,
        "KOMODO Medium 479 exactly mirrors DSMZ Medium 479.",
    ),
    Child(
        Path("bacterial/for_dsm_5219.yaml"),
        "CultureMech:005593",
        "for_dsm_5219",
        "komodo.medium:479.1",
        "PH_VARIANT",
        {"min": 7.4, "max": 7.5},
        NAOH_INGREDIENT_SIGNATURE,
        (
            "KOMODO Medium 479.1 applies METHANOHALOPHILUS MEDIUM at pH "
            "7.4-7.5 for DSM 5219."
        ),
    ),
)


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


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
        "id": child.record_id,
        "name": child.name,
        "notes": child.modification,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "MediaDive Medium 479 is the DSMZ METHANOHALOPHILUS MEDIUM base.",
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ph: Any,
    ingredient_signature: tuple[tuple[str, str, str], ...],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ph(doc) != ph:
        raise ValueError(f"{relative_path}: expected pH {ph!r}")
    if _ingredient_signature(doc) != ingredient_signature:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(
        doc,
        PARENT,
        PARENT_ID,
        PARENT_SOURCE_TERM,
        PARENT_PH,
        BASE_INGREDIENT_SIGNATURE,
    )

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
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
            "changes": (
                "Promoted MediaDive Medium 479 to the Methanohalophilus family "
                "parent"
            ),
            "source": "MediaDive Medium 479 and KOMODO Medium 479-479.1",
            "notes": (
                "Linked the exact KOMODO Medium 479 source duplicate and "
                "reclassified the pH 7.4-7.5 DSM 5219 record as a pH variant."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
        child.ph,
        child.ingredient_signature,
    )

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", child.relationship, "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [child.modification],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under MediaDive Medium 479",
            "source": child.source_label,
            "notes": child.modification,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    repairs = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for child in CHILDREN:
        repairs[normalized / child.path] = repair_child(_load(normalized / child.path), child)
    return repairs


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
