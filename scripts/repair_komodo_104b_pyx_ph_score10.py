#!/usr/bin/env python3
"""Repair KOMODO PYX-MEDIUM strain and pH variants mislinked as source duplicates."""

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

PARENT = Path("bacterial/KOMODO_104b_PYX-MEDIUM.yaml")
PARENT_ID = "CultureMech:003622"
PARENT_NAME = "pyx_medium"
PARENT_SOURCE_TERM = "komodo.medium:104b"
PARENT_PH = 7.0

INGREDIENT_SIGNATURE = (
    ("Trypticase peptone", "5", "G_PER_L"),
    ("Meat peptone", "5", "G_PER_L"),
    ("Yeast extract", "10", "G_PER_L"),
    ("NaCl", "10.0", "G_PER_L"),
    ("Sodium resazurin", "0.0005", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.5", "G_PER_L"),
    ("D-Glucose", "1", "G_PER_L"),
    ("Na2S2O3 x 5 H2O", "2.5", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.25", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.5", "G_PER_L"),
    ("K2HPO4", "1", "G_PER_L"),
    ("KH2PO4", "1", "G_PER_L"),
    ("NaHCO3", "10", "G_PER_L"),
)

CURATOR = "repair_komodo_104b_pyx_ph_score10.py"
ACTION = "RESOLVED_KOMODO_104B_PYX_PH_VARIANTS"
STRAIN_ACTION = "RESOLVED_KOMODO_104B_PYX_STRAIN_VARIANTS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    ph_value: float
    relationship: str
    dsm: str

    @property
    def source_label(self) -> str:
        return f"KOMODO Medium {self.source_term.removeprefix('komodo.medium:')}"

    @property
    def modification(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return (
                f"{self.source_label} preserves PYX-MEDIUM components and "
                f"pH {self.ph_value:g} but applies the recipe for {self.dsm}."
            )
        return (
            f"{self.source_label} preserves PYX-MEDIUM components and "
            f"concentrations but records pH {self.ph_value:g} for {self.dsm}."
        )

    @property
    def notes(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return (
                f"{self.source_label} applies pH {self.ph_value:g} PYX-MEDIUM " f"for {self.dsm}."
            )
        return f"{self.source_label} applies PYX-MEDIUM at pH {self.ph_value:g} " f"for {self.dsm}."

    @property
    def action(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return STRAIN_ACTION
        return ACTION

    @property
    def changes(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return "Linked as a PYX-MEDIUM strain-specific variant"
        return "Linked as a PYX-MEDIUM pH variant"


CHILDREN = (
    Child(
        path=Path("bacterial/for_dsm_753.yaml"),
        record_id="CultureMech:003614",
        name="for_dsm_753",
        source_term="komodo.medium:104b.2",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 753",
    ),
    Child(
        path=Path("bacterial/for_dsm_7320.yaml"),
        record_id="CultureMech:003615",
        name="for_dsm_7320",
        source_term="komodo.medium:104b.3",
        ph_value=6.3,
        relationship="PH_VARIANT",
        dsm="DSM 7320",
    ),
    Child(
        path=Path("bacterial/for_dsm_5387.yaml"),
        record_id="CultureMech:003616",
        name="for_dsm_5387",
        source_term="komodo.medium:104b.4",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 5387",
    ),
    Child(
        path=Path("bacterial/for_dsm_13181.yaml"),
        record_id="CultureMech:003618",
        name="for_dsm_13181",
        source_term="komodo.medium:104b.6",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 13181",
    ),
    Child(
        path=Path("bacterial/for_dsm_19022.yaml"),
        record_id="CultureMech:003620",
        name="for_dsm_19022",
        source_term="komodo.medium:104b.8",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 19022",
    ),
    Child(
        path=Path("bacterial/for_dsm_21120.yaml"),
        record_id="CultureMech:003621",
        name="for_dsm_21120",
        source_term="komodo.medium:104b.9",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 21120",
    ),
    Child(
        path=Path("bacterial/for_dsm_21761.yaml"),
        record_id="CultureMech:003610",
        name="for_dsm_21761",
        source_term="komodo.medium:104b.11",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 21761",
    ),
    Child(
        path=Path("bacterial/for_dsm_21650.yaml"),
        record_id="CultureMech:003611",
        name="for_dsm_21650",
        source_term="komodo.medium:104b.12",
        ph_value=8.5,
        relationship="PH_VARIANT",
        dsm="DSM 21650",
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
        "notes": f"KOMODO Medium 104b is the pH {PARENT_PH:g} PYX-MEDIUM base.",
    }


def _upsert_child_entry(children: list[Any], child: Child) -> None:
    path = f"data/normalized_yaml/{child.path}"
    for index, existing in enumerate(children):
        if isinstance(existing, dict) and existing.get("path") == path:
            children[index] = _child_entry(child)
            return
    raise ValueError(f"{PARENT}: missing variant child {path}")


def _require_pyx_record(
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
    _require_pyx_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_PH)
    children = doc.get("variant_children") or []
    if not isinstance(children, list):
        raise ValueError(f"{PARENT}: variant_children is not a list")

    repaired = copy.deepcopy(doc)
    variant_children = repaired["variant_children"]
    for child in CHILDREN:
        _upsert_child_entry(variant_children, child)

    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked PYX-MEDIUM pH variant children",
            "source": "KOMODO Medium 104b.3 and KOMODO Medium 104b.12",
            "notes": (
                "Changed DSM 7320 and DSM 21650 from SOURCE_DUPLICATE to "
                "PH_VARIANT children of PYX-MEDIUM."
            ),
        },
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": STRAIN_ACTION,
            "changes": "Linked PYX-MEDIUM strain-specific children",
            "source": ("KOMODO Medium 104b.2, 104b.4, 104b.6, 104b.8, " "104b.9, and 104b.11"),
            "notes": (
                "Changed DSM 753, DSM 5387, DSM 13181, DSM 19022, "
                "DSM 21120, and DSM 21761 from SOURCE_DUPLICATE to "
                "STRAIN_SPECIFIC_VARIANT children of PYX-MEDIUM."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_pyx_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
        child.ph_value,
    )

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", child.relationship, "parent_media")
    _put_after(repaired, "variant_modifications", [child.modification], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": child.action,
            "changes": child.changes,
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
