#!/usr/bin/env python3
"""Repair KOMODO 843 Helmutkoenigia exact and strain child links."""

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

PARENT = Path("bacterial/helmutkoenigia_medium.yaml")
PARENT_ID = "CultureMech:001999"
PARENT_NAME = "helmutkoenigia_medium"
PARENT_SOURCE_TERM = "mediadive.medium:843"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

SIGNATURE = (
    ("NaCl", "0.997009", "G_PER_L"),
    ("KCl", "0.498504", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.398804", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.0997009", "G_PER_L"),
    ("NH4Cl", "0.299103", "G_PER_L"),
    ("KH2PO4", "0.199402", "G_PER_L"),
    ("Na2SO4", "0.149551", "G_PER_L"),
    ("Trypticase peptone", "0.997009", "G_PER_L"),
    ("Sodium resazurin", "0.000498504", "G_PER_L"),
    ("Na2CO3", "1.49551", "G_PER_L"),
    ("DL-Dithiothreitol", "0.398804", "G_PER_L"),
    ("Cellobiose", "56.7", "G_PER_L"),
    ("Sucrose", "56.7", "G_PER_L"),
    ("Maltose x H2O", "60", "G_PER_L"),
    ("Trehalose", "63.3", "G_PER_L"),
    ("D-Xylose", "25", "G_PER_L"),
    ("Yeast extract", "280", "G_PER_L"),
    ("Thiamine pyrophosphate", "2.5", "G_PER_L"),
    ("Pyridoxal hydrochloride", "0.25", "G_PER_L"),
    ("Pyridoxal phosphate", "0.25", "G_PER_L"),
    ("Ca-folinate", "0.05", "G_PER_L"),
    ("ß-NAD", "0.05", "G_PER_L"),
    ("Coenzyme A", "0.05", "G_PER_L"),
    ("FAD", "0.05", "G_PER_L"),
    ("Haemin", "0.065", "G_PER_L"),
    ("Nicotinamide", "0.025", "G_PER_L"),
    ("Folic acid", "0.0025", "G_PER_L"),
    ("Riboflavin", "0.0005", "G_PER_L"),
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


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    relationship: str
    notes: str


CHILDREN = (
    Child(
        Path("bacterial/treponema_zas_medium.yaml"),
        "CultureMech:006648",
        "komodo.medium:843",
        "KOMODO Medium 843",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "KOMODO Medium 843 has the same 47-ingredient signature as DSMZ Medium 843.",
    ),
    Child(
        Path("bacterial/for_dsm_13862.yaml"),
        "CultureMech:006647",
        "komodo.medium:843.1",
        "KOMODO Medium 843.1",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 843.1 applies Helmutkoenigia medium to DSM 13862.",
    ),
    Child(
        Path("bacterial/medium_843_modified_for_dsm_18056.yaml"),
        "CultureMech:006646",
        "komodo.medium:843_18056",
        "KOMODO Medium 843_18056",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 843_18056 applies Helmutkoenigia medium to DSM 18056.",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 3

CURATOR = "repair_komodo_843_helmutkoenigia_score10.py"
ACTION = "RESOLVED_KOMODO_843_HELMUTKOENIGIA_TOPOLOGY"
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
    if len(CHILDREN) != EXPECTED_CHILD_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_CHILD_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": child.notes,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": child.notes,
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


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)


def _require_child(child: Child, doc: dict[str, Any]) -> None:
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
        [_child_entry(child) for child in CHILDREN],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Re-rooted KOMODO Medium 843 Helmutkoenigia exact topology",
            "source": "DSMZ Medium 843; KOMODO Medium 843, 843.1, 843_18056",
            "notes": (
                "Moved exact KOMODO Medium 843 and its DSM-specific wrappers "
                "under DSMZ Medium 843."
            ),
        },
    )
    return repaired


def repair_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected child path {relative_path}")
    _require_child(child, doc)

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
            "changes": f"Linked under DSMZ Medium 843 as {child.relationship}",
            "source": child.source_label,
            "notes": child.notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for child in CHILDREN:
        plans[normalized / child.path] = repair_child(
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
