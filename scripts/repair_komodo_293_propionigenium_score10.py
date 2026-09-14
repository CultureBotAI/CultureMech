#!/usr/bin/env python3
"""Repair KOMODO 293 Propionigenium child and duplicate links."""

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

PARENT = Path("bacterial/propionigenium_modestum_medium.yaml")
PARENT_ID = "CultureMech:004756"
PARENT_NAME = "propionigenium_modestum_medium"
PARENT_SOURCE_TERM = "komodo.medium:293"
PARENT_PH = 7.2

STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"

INGREDIENT_SIGNATURE = (
    ("KH2PO4", "0.1998", "G_PER_L"),
    ("NH4Cl", "0.24975", "G_PER_L"),
    ("NaCl", "19.98", "G_PER_L"),
    ("MgCl2 x 6 H2O", "2.997", "G_PER_L"),
    ("KCl", "0.499501", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.14985", "G_PER_L"),
    ("Sodium resazurin", "0.0004995", "G_PER_L"),
    ("Na2CO3", "1.24875", "G_PER_L"),
    ("Disodium succinate", "3.24675", "G_PER_L"),
    ("Na2S x 9 H2O", "0.35964", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
)


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    target: str


@dataclass(frozen=True)
class SourceDuplicate:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None


CHILD = Child(
    Path("bacterial/for_dsm_2376.yaml"),
    "CultureMech:004755",
    "komodo.medium:293.1",
    "KOMODO Medium 293.1",
    "DSM 2376",
)

DUPLICATES = (
    SourceDuplicate(
        Path("bacterial/ven_chi2_medium.yaml"),
        "CultureMech:004757",
        "komodo.medium:293a",
        "KOMODO Medium 293a",
        ph_value=7.2,
    ),
    SourceDuplicate(
        Path("specialized/propionigenium_modestum_medium_marine.yaml"),
        "CultureMech:015351",
        "mediadive.medium:293",
        "DSMZ Medium 293",
        ph_range={"min": 7.2, "max": 7.5},
    ),
)
DUPLICATE_BY_PATH = {duplicate.path: duplicate for duplicate in DUPLICATES}
EXPECTED_DUPLICATE_COUNT = 2

CURATOR = "repair_komodo_293_propionigenium_score10.py"
ACTION = "RESOLVED_KOMODO_293_PROPIONIGENIUM_TOPOLOGY"
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
    if len(DUPLICATES) != EXPECTED_DUPLICATE_COUNT or len(DUPLICATES) != len(
        DUPLICATE_BY_PATH
    ):
        raise ValueError(
            f"expected {EXPECTED_DUPLICATE_COUNT} unique duplicates, found "
            f"{len(DUPLICATES)} total and {len(DUPLICATE_BY_PATH)} unique"
        )


def _child_notes() -> str:
    return f"{CHILD.source_label} applies PROPIONIGENIUM MODESTUM MEDIUM to {CHILD.target}."


def _duplicate_notes(duplicate: SourceDuplicate) -> str:
    return (
        f"{duplicate.source_label} has the same 19-component "
        "Propionigenium modestum medium signature as KOMODO Medium 293."
    )


def _child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{CHILD.path}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": CHILD.record_id,
        "name": CHILD.path.stem,
        "notes": _child_notes(),
    }


def _duplicate_entry(duplicate: SourceDuplicate) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{duplicate.path}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": duplicate.record_id,
        "name": duplicate.path.stem,
        "notes": _duplicate_notes(duplicate),
    }


def _parent_ref(relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": notes,
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
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)
    if doc.get("ph_value") != PARENT_PH:
        raise ValueError(f"{PARENT}: expected pH {PARENT_PH!r}")


def _require_child(doc: dict[str, Any]) -> None:
    _require_record(doc, CHILD.path, CHILD.record_id, CHILD.source_term)
    if doc.get("ph_value") != PARENT_PH:
        raise ValueError(f"{CHILD.path}: expected pH {PARENT_PH!r}")


def _require_duplicate(duplicate: SourceDuplicate, doc: dict[str, Any]) -> None:
    _require_record(doc, duplicate.path, duplicate.record_id, duplicate.source_term)
    if duplicate.ph_value is not None and doc.get("ph_value") != duplicate.ph_value:
        raise ValueError(f"{duplicate.path}: expected pH {duplicate.ph_value!r}")
    if duplicate.ph_range is not None and doc.get("ph_range") != duplicate.ph_range:
        raise ValueError(f"{duplicate.path}: expected pH range {duplicate.ph_range!r}")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_parent(doc)

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "variant_children",
        [_child_entry()]
        + [_duplicate_entry(duplicate) for duplicate in DUPLICATES],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked KOMODO Medium 293 child and duplicate records",
            "source": "KOMODO Medium 293, 293.1, and 293a; DSMZ Medium 293",
            "notes": (
                "Linked KOMODO Medium 293.1 under the KOMODO Medium 293 "
                "Propionigenium modestum base and documented the exact-signature "
                "KOMODO 293a and DSMZ 293 duplicate records."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any]) -> dict[str, Any]:
    _require_child(doc)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(
            STRAIN_RELATIONSHIP,
            "KOMODO Medium 293 is the PROPIONIGENIUM MODESTUM MEDIUM base.",
        ),
        "curation_history",
    )
    _put_after(repaired, "variant_relationship", STRAIN_RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [_child_notes()], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 293",
            "source": CHILD.source_label,
            "notes": _child_notes(),
        },
    )
    return repaired


def repair_duplicate(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    duplicate = DUPLICATE_BY_PATH.get(relative_path)
    if duplicate is None:
        raise ValueError(f"unexpected duplicate path {relative_path}")
    _require_duplicate(duplicate, doc)

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(SOURCE_DUPLICATE_RELATIONSHIP, _duplicate_notes(duplicate)),
        "curation_history",
    )
    _put_after(
        repaired,
        "variant_relationship",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "parent_media",
    )
    _put_after(
        repaired,
        "variant_modifications",
        [_duplicate_notes(duplicate)],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Documented as a KOMODO Medium 293 duplicate",
            "source": duplicate.source_label,
            "notes": _duplicate_notes(duplicate),
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {
        normalized / PARENT: repair_parent(_load(normalized / PARENT)),
        normalized / CHILD.path: repair_child(_load(normalized / CHILD.path)),
    }
    for duplicate in DUPLICATES:
        plans[normalized / duplicate.path] = repair_duplicate(
            duplicate.path,
            _load(normalized / duplicate.path),
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
