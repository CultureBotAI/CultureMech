#!/usr/bin/env python3
"""Repair KOMODO Medium 1069 strain and pH variants mislinked as duplicates."""

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

PARENT = Path("bacterial/KOMODO_1069_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml")
PARENT_ID = "CultureMech:003657"
PARENT_NAME = "modified_biebl_and_pfennigs_medium"
PARENT_SOURCE_TERM = "komodo.medium:1069"
PARENT_PH = 7.0

INGREDIENT_SIGNATURE = (
    ("KH2PO4", "0.5", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.15", "G_PER_L"),
    ("MgSO4 x 7 H2O", "2", "G_PER_L"),
    ("NH4Cl", "0.34", "G_PER_L"),
    ("NaCl", "20", "G_PER_L"),
    ("Yeast extract", "0.4", "G_PER_L"),
    ("Ferric citrate", "0.005", "G_PER_L"),
    ("HCl", "0.25", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.06", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.02", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.02", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.04", "G_PER_L"),
)

CURATOR = "repair_komodo_1069_ph_score10.py"
ACTION = "RESOLVED_KOMODO_1069_PH_VARIANTS"
STRAIN_ACTION = "RESOLVED_KOMODO_1069_STRAIN_VARIANTS"
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
                f"{self.source_label} preserves KOMODO Medium 1069 components "
                f"and pH {self.ph_value:g} but applies the recipe for {self.dsm}."
            )
        return (
            f"{self.source_label} preserves KOMODO Medium 1069 components and "
            f"concentrations but records pH {self.ph_value:g} for {self.dsm}."
        )

    @property
    def notes(self) -> str:
        return (
            f"{self.source_label} applies MODIFIED BIEBL AND PFENNIG'S MEDIUM "
            f"at pH {self.ph_value:g} for {self.dsm}."
        )

    @property
    def action(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return STRAIN_ACTION
        return ACTION

    @property
    def changes(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return "Linked as a KOMODO 1069 strain-specific variant"
        return "Linked as a KOMODO 1069 pH variant"


CHILDREN = (
    Child(
        path=Path("bacterial/for_dsm_18064.yaml"),
        record_id="CultureMech:003651",
        name="for_dsm_18064",
        source_term="komodo.medium:1069.1",
        ph_value=6.8,
        relationship="PH_VARIANT",
        dsm="DSM 18064",
    ),
    Child(
        path=Path("bacterial/for_dsm_18985.yaml"),
        record_id="CultureMech:003654",
        name="for_dsm_18985",
        source_term="komodo.medium:1069.4",
        ph_value=6.8,
        relationship="PH_VARIANT",
        dsm="DSM 18985",
    ),
    Child(
        path=Path("bacterial/for_dsm_24766.yaml"),
        record_id="CultureMech:003656",
        name="for_dsm_24766",
        source_term="komodo.medium:1069.6",
        ph_value=7.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 24766",
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
        "notes": (f"KOMODO Medium 1069 is the pH {PARENT_PH:g} base for " f"{child.source_label}."),
    }


def _upsert_child_entry(children: list[Any], child: Child) -> None:
    path = f"data/normalized_yaml/{child.path}"
    for index, existing in enumerate(children):
        if isinstance(existing, dict) and existing.get("path") == path:
            children[index] = _child_entry(child)
            return
    raise ValueError(f"{PARENT}: missing variant child {path}")


def _require_1069_record(
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
    _require_1069_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_PH)
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
            "changes": "Linked KOMODO 1069 pH variant children",
            "source": "KOMODO Medium 1069.1 and KOMODO Medium 1069.4",
            "notes": (
                "Changed DSM 18064 and DSM 18985 from SOURCE_DUPLICATE to "
                "PH_VARIANT children of KOMODO Medium 1069."
            ),
        },
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": STRAIN_ACTION,
            "changes": "Linked KOMODO 1069 strain-specific children",
            "source": "KOMODO Medium 1069.6",
            "notes": (
                "Changed DSM 24766 from SOURCE_DUPLICATE to a "
                "STRAIN_SPECIFIC_VARIANT child of KOMODO Medium 1069."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_1069_record(
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
