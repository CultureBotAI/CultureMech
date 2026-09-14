#!/usr/bin/env python3
"""Repair KOMODO 36 topology rooted at a strain-specific duplicate."""

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

PARENT = Path("bacterial/thiobacillus_thioparus_medium.yaml")
PARENT_ID = "CultureMech:005091"
PARENT_NAME = "thiobacillus_thioparus_medium"
PARENT_SOURCE_TERM = "komodo.medium:36"
PARENT_PH = 6.6

INGREDIENT_SIGNATURE = (
    ("(NH4)2SO4", "0.1", "G_PER_L"),
    ("K2HPO4", "4", "G_PER_L"),
    ("KH2PO4", "4", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CaCl2", "0.1", "G_PER_L"),
    ("FeCl3 x 6 H2O", "0.02", "G_PER_L"),
    ("MnSO4 x H2O", "0.02", "G_PER_L"),
    ("Agar", "12", "G_PER_L"),
    ("Na2S2O3 x 5 H2O", "10", "G_PER_L"),
)

CURATOR = "repair_komodo_36_thiobacillus_score10.py"
ACTION = "RESOLVED_KOMODO_36_THIOBACILLUS_TOPOLOGY"
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
    context: str
    ph_value: float

    @property
    def source_label(self) -> str:
        return source_label(self.source_term)

    @property
    def notes(self) -> str:
        if self.relationship == "SOURCE_DUPLICATE":
            return (
                f"{self.source_label} exactly matches the KOMODO Medium 36 "
                "THIOBACILLUS THIOPARUS MEDIUM base."
            )
        return (
            f"{self.source_label} applies THIOBACILLUS THIOPARUS MEDIUM "
            f"at pH {self.ph_value:g} for {self.context}."
        )


CHILDREN = (
    Child(
        Path("bacterial/thiobacillus_medium.yaml"),
        "CultureMech:001471",
        "thiobacillus_medium",
        "mediadive.medium:36",
        "SOURCE_DUPLICATE",
        "MediaDive Medium 36",
        PARENT_PH,
    ),
    Child(
        Path("bacterial/for_dsm_18181.yaml"),
        "CultureMech:005082",
        "for_dsm_18181",
        "komodo.medium:36.1",
        "PH_VARIANT",
        "DSM 18181",
        7.5,
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
        "notes": "KOMODO Medium 36 is the THIOBACILLUS THIOPARUS MEDIUM base.",
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ph_value: float,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if doc.get("ph_value") != ph_value:
        raise ValueError(f"{relative_path}: expected pH {ph_value:g}")
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
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Promoted KOMODO Medium 36 to the Thiobacillus family parent",
            "source": "KOMODO Medium 36-36.1 and MediaDive Medium 36",
            "notes": (
                "Moved the family root from strain-specific KOMODO Medium 36.1 "
                "to base KOMODO Medium 36 and reclassified DSM 18181 as a pH "
                "variant."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_record(doc, child.path, child.record_id, child.source_term, child.ph_value)

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
            "changes": "Linked under THIOBACILLUS THIOPARUS MEDIUM",
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
