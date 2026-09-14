#!/usr/bin/env python3
"""Repair KOMODO 505 topology rooted at a strain-specific duplicate."""

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

PARENT = Path("bacterial/formivibrio_medium.yaml")
PARENT_ID = "CultureMech:001637"
PARENT_NAME = "formivibrio_medium"
PARENT_SOURCE_TERM = "mediadive.medium:505"
PARENT_PH = {"min": 7.5, "max": 7.8}

INGREDIENT_SIGNATURE = (
    ("KH2PO4", "1.4862", "G_PER_L"),
    ("NH4Cl", "0.530786", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.212314", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.159236", "G_PER_L"),
    ("Sodium resazurin", "0.000530786", "G_PER_L"),
    ("Na2CO3", "50", "G_PER_L"),
    ("Trisodium citrate x 2 H2O", "150", "G_PER_L"),
    ("Na2S x 9 H2O", "30", "G_PER_L"),
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

CURATOR = "repair_komodo_505_formivibrio_score10.py"
ACTION = "RESOLVED_KOMODO_505_FORMIVIBRIO_TOPOLOGY"
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
    notes: str

    @property
    def source_label(self) -> str:
        return source_label(self.source_term)


CHILDREN = (
    Child(
        Path("bacterial/propionivibrio_acetivibrio_formivibrio_medium.yaml"),
        "CultureMech:005697",
        "propionivibrio_acetivibrio_formivibrio_medium",
        "komodo.medium:505",
        "SOURCE_DUPLICATE",
        None,
        "KOMODO Medium 505 exactly mirrors DSMZ Medium 505.",
    ),
    Child(
        Path("bacterial/for_dsm_5885.yaml"),
        "CultureMech:005694",
        "for_dsm_5885",
        "komodo.medium:505.1",
        "PH_VARIANT",
        {"min": 6.7, "max": 6.8},
        "KOMODO Medium 505.1 applies FORMIVIBRIO MEDIUM at pH 6.7-6.8 for DSM 5885.",
    ),
    Child(
        Path("bacterial/for_dsm_6139.yaml"),
        "CultureMech:005695",
        "for_dsm_6139",
        "komodo.medium:505.2",
        "PH_VARIANT",
        {"min": 7.7, "max": 7.9},
        "KOMODO Medium 505.2 applies FORMIVIBRIO MEDIUM at pH 7.7-7.9 for DSM 6139.",
    ),
    Child(
        Path("bacterial/for_dsm_6150.yaml"),
        "CultureMech:005696",
        "for_dsm_6150",
        "komodo.medium:505.3",
        "STRAIN_SPECIFIC_VARIANT",
        {"min": 7.5, "max": 7.7},
        "KOMODO Medium 505.3 applies FORMIVIBRIO MEDIUM for DSM 6150.",
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
        "notes": child.notes,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": "MediaDive Medium 505 is the DSMZ FORMIVIBRIO MEDIUM base.",
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
    _put_after(
        repaired,
        "variant_children",
        [_child_entry(child) for child in CHILDREN],
        "high_metal",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Promoted MediaDive Medium 505 to the Formivibrio family parent",
            "source": "MediaDive Medium 505 and KOMODO Medium 505-505.3",
            "notes": (
                "Moved the family root from strain-specific KOMODO Medium 505.1 "
                "to the DSMZ/MediaDive FORMIVIBRIO MEDIUM record."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_record(doc, child.path, child.record_id, child.source_term, child.ph)

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
            "changes": "Linked under MediaDive Medium 505",
            "source": child.source_label,
            "notes": child.notes,
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
