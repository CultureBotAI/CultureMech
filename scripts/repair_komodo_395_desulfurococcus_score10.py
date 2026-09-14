#!/usr/bin/env python3
"""Repair KOMODO 395 Desulfurococcus strain and pH child links."""

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

PARENT = Path("archaea/KOMODO_395_DESULFUROCOCCUS_AMYLOLYTICUS_medium.yaml")
PARENT_ID = "CultureMech:005182"
PARENT_NAME = "desulfurococcus_amylolyticus_medium"
PARENT_SOURCE_TERM = "komodo.medium:395"

STRAIN_SPECIFIC = "STRAIN_SPECIFIC_VARIANT"
PH_VARIANT = "PH_VARIANT"

SOURCE_DUPLICATE_CHILD = {
    "path": "data/normalized_yaml/bacterial/fervidicoccus_medium.yaml",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:001504",
    "name": "fervidicoccus_medium",
    "notes": "Same ingredient and concentration signature; review as possible duplicate source record.",
}


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    strain: str
    relationship: str
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None


BASE_PH_RANGE = {"min": 6.2, "max": 6.4}

CHILDREN = (
    Child(
        Path("bacterial/for_dsm_16532.yaml"),
        "CultureMech:005179",
        "komodo.medium:395.1",
        "KOMODO Medium 395.1",
        "DSM 16532",
        STRAIN_SPECIFIC,
        ph_range=BASE_PH_RANGE,
    ),
    Child(
        Path("bacterial/for_dsm_18924.yaml"),
        "CultureMech:005180",
        "komodo.medium:395.2",
        "KOMODO Medium 395.2",
        "DSM 18924",
        PH_VARIANT,
        ph_value=6.5,
    ),
    Child(
        Path("bacterial/for_dsm_19380.yaml"),
        "CultureMech:005181",
        "komodo.medium:395.3",
        "KOMODO Medium 395.3",
        "DSM 19380",
        STRAIN_SPECIFIC,
        ph_range=BASE_PH_RANGE,
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_TARGET_COUNT = 3

INGREDIENT_SIGNATURE = (
    ("NH4Cl", "0.329341", "G_PER_L"),
    ("KH2PO4", "0.329341", "G_PER_L"),
    ("KCl", "0.329341", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.439122", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.698603", "G_PER_L"),
    ("NaCl", "0.499002", "G_PER_L"),
    ("Yeast extract", "0.499002", "G_PER_L"),
    ("Sodium resazurin", "0.000499002", "G_PER_L"),
    ("NaHCO3", "0.798403", "G_PER_L"),
    ("Trypticase peptone", "1.99601", "G_PER_L"),
    ("Na2S x 9 H2O", "0.499002", "G_PER_L"),
    ("HCl", "2.5", "G_PER_L"),
    ("FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("ZnCl2", "0.07", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("H3BO3", "0.006", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
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

CURATOR = "repair_komodo_395_desulfurococcus_score10.py"
ACTION = "RESOLVED_KOMODO_395_DESULFUROCOCCUS_TOPOLOGY"
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
    if len(CHILDREN) != EXPECTED_TARGET_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def _child_notes(child: Child) -> str:
    if child.relationship == PH_VARIANT:
        return (
            f"{child.source_label} applies DESULFUROCOCCUS AMYLOLYTICUS medium "
            f"at pH {child.ph_value:g} to {child.strain}."
        )
    return (
        f"{child.source_label} applies DESULFUROCOCCUS AMYLOLYTICUS medium " f"to {child.strain}."
    )


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": child.relationship,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": _child_notes(child),
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": child.relationship,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": (
            "KOMODO Medium 395 is the DESULFUROCOCCUS AMYLOLYTICUS base "
            f"for {child.source_label}."
        ),
    }


def _require_base_record(doc: dict[str, Any]) -> None:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT}: expected {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != PARENT_SOURCE_TERM:
        raise ValueError(f"{PARENT}: expected {PARENT_SOURCE_TERM}")
    if doc.get("ph_range") != BASE_PH_RANGE:
        raise ValueError(f"{PARENT}: expected pH range {BASE_PH_RANGE!r}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{PARENT}: ingredient signature drifted")


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    if doc.get("id") != child.record_id:
        raise ValueError(f"{child.path}: expected {child.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != child.source_term:
        raise ValueError(f"{child.path}: expected {child.source_term}")
    if child.ph_range is not None and doc.get("ph_range") != child.ph_range:
        raise ValueError(f"{child.path}: expected pH range {child.ph_range!r}")
    if child.ph_value is not None and doc.get("ph_value") != child.ph_value:
        raise ValueError(f"{child.path}: expected pH {child.ph_value!r}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{child.path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_base_record(doc)

    repaired = copy.deepcopy(doc)
    _put_after(
        repaired,
        "variant_children",
        [SOURCE_DUPLICATE_CHILD, *[_child_entry(child) for child in CHILDREN]],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 395.1, 395.2, and 395.3 variants",
            "source": "KOMODO Medium 395, 395.1, 395.2, and 395.3",
            "notes": (
                "Linked the KOMODO Medium 395.1, 395.2, and 395.3 records under "
                "the KOMODO Medium 395 DESULFUROCOCCUS AMYLOLYTICUS base."
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
    _put_after(
        repaired,
        "variant_modifications",
        [_child_notes(child)],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 395",
            "source": child.source_label,
            "notes": _child_notes(child),
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
