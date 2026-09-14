#!/usr/bin/env python3
"""Repair a KOMODO artificial seawater strain variant mislinked as a duplicate."""

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

PARENT = Path("bacterial/KOMODO_1010_Artificial_SEAWATER_MEDIUM.yaml")
PARENT_ID = "CultureMech:003516"
PARENT_NAME = "artificial_seawater_medium"
PARENT_SOURCE_TERM = "komodo.medium:1010"
PH_RANGE = {"min": 7.2, "max": 7.5}
PH_LABEL = "7.2-7.5"

INGREDIENT_SIGNATURE = (
    ("NaCl", "26.2948", "G_PER_L"),
    ("MgCl2 x 6 H2O", "5.67729", "G_PER_L"),
    ("MgSO4 x 7 H2O", "6.77291", "G_PER_L"),
    ("KCl", "0.657371", "G_PER_L"),
    ("CaCl2 x 2 H2O", "1.46414", "G_PER_L"),
    ("KBr", "0.0896414", "G_PER_L"),
    ("Sodium resazurin", "0.000498008", "G_PER_L"),
    ("KH2PO4", "0.199203", "G_PER_L"),
    ("NH4Cl", "0.249004", "G_PER_L"),
    ("Na2CO3", "0.996016", "G_PER_L"),
    ("Na-DL-lactate", "2.29084", "G_PER_L"),
    ("Na2S x 9 H2O", "0.298805", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
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
    ("Thiamine HCl", "0.05", "G_PER_L"),
    ("Riboflavin", "0.05", "G_PER_L"),
    ("Calcium D-(+)-pantothenate", "0.05", "G_PER_L"),
    ("(DL)-alpha-Lipoic acid", "0.05", "G_PER_L"),
    ("D-(+)-biotin", "0.02", "G_PER_L"),
    ("Calcium pantothenate", "0.1", "G_PER_L"),
)

CURATOR = "repair_komodo_1010_artificial_seawater_score10.py"
ACTION = "RESOLVED_KOMODO_1010_ARTIFICIAL_SEAWATER_STRAIN_VARIANT"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    dsm: str

    @property
    def source_label(self) -> str:
        return f"KOMODO Medium {self.source_term.removeprefix('komodo.medium:')}"

    @property
    def modification(self) -> str:
        return (
            f"{self.source_label} preserves ARTIFICIAL SEAWATER MEDIUM components "
            f"and pH {PH_LABEL} but applies the recipe for {self.dsm}."
        )

    @property
    def notes(self) -> str:
        return (
            f"{self.source_label} applies ARTIFICIAL SEAWATER MEDIUM at pH {PH_LABEL} "
            f"for {self.dsm}."
        )


CHILD = Child(
    path=Path("bacterial/for_dsm_15769.yaml"),
    record_id="CultureMech:003515",
    name="for_dsm_15769",
    source_term="komodo.medium:1010.1",
    dsm="DSM 15769",
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
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": child.record_id,
        "name": child.name,
        "notes": child.notes,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": (
            f"KOMODO Medium 1010 is the pH {PH_LABEL} "
            "ARTIFICIAL SEAWATER MEDIUM base."
        ),
    }


def _upsert_child_entry(children: list[Any], child: Child) -> None:
    path = f"data/normalized_yaml/{child.path}"
    for index, existing in enumerate(children):
        if isinstance(existing, dict) and existing.get("path") == path:
            children[index] = _child_entry(child)
            return
    raise ValueError(f"{PARENT}: missing variant child {path}")


def _require_artificial_seawater_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if doc.get("ph_range") != PH_RANGE:
        raise ValueError(f"{relative_path}: expected pH {PH_LABEL}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_artificial_seawater_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    children = doc.get("variant_children") or []
    if not isinstance(children, list):
        raise ValueError(f"{PARENT}: variant_children is not a list")

    repaired = copy.deepcopy(doc)
    _upsert_child_entry(repaired["variant_children"], CHILD)
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked an ARTIFICIAL SEAWATER MEDIUM strain-specific child",
            "source": CHILD.source_label,
            "notes": (
                "Changed DSM 15769 from SOURCE_DUPLICATE to a "
                "STRAIN_SPECIFIC_VARIANT child of KOMODO Medium 1010."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child = CHILD) -> dict[str, Any]:
    _require_artificial_seawater_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
    )

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", "STRAIN_SPECIFIC_VARIANT", "parent_media")
    _put_after(repaired, "variant_modifications", [child.modification], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as an ARTIFICIAL SEAWATER MEDIUM strain-specific variant",
            "source": child.source_label,
            "notes": child.modification,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / PARENT: repair_parent(_load(normalized / PARENT)),
        normalized / CHILD.path: repair_child(_load(normalized / CHILD.path)),
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
