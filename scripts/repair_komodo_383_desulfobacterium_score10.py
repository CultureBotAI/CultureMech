#!/usr/bin/env python3
"""Repair KOMODO 383 Desulfobacterium strain child links."""

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

PARENT = Path("bacterial/KOMODO_383_DESULFOBACTERIUM_MEDIUM.yaml")
PARENT_ID = "CultureMech:005154"
PARENT_NAME = "desulfobacterium_medium"
PARENT_SOURCE_TERM = "komodo.medium:383"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

INGREDIENT_SIGNATURE = (
    ("Na2SO4", "3.08642", "G_PER_L"),
    ("KH2PO4", "0.205761", "G_PER_L"),
    ("NH4Cl", "0.308642", "G_PER_L"),
    ("NaCl", "21.6049", "G_PER_L"),
    ("MgCl2 x 6 H2O", "3.08642", "G_PER_L"),
    ("KCl", "0.514403", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.154321", "G_PER_L"),
    ("Sodium resazurin", "0.000514403", "G_PER_L"),
    ("Na2CO3", "50", "G_PER_L"),
    ("Na2S x 9 H2O", "30.7692", "G_PER_L"),
    ("NaOH", "0.5", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
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


@dataclass(frozen=True)
class SourceDuplicate:
    path: Path
    record_id: str
    source_term: str
    source_label: str


@dataclass(frozen=True)
class StrainChild:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    target: str


SOURCE_DUPLICATES = (
    SourceDuplicate(
        Path("bacterial/KOMODO_383d_DESULFONAUTICUS_medium.yaml"),
        "CultureMech:005159",
        "komodo.medium:383d",
        "KOMODO Medium 383d",
    ),
    SourceDuplicate(
        Path("bacterial/desulfobacula_toluolica_medium.yaml"),
        "CultureMech:005157",
        "komodo.medium:383b",
        "KOMODO Medium 383b",
    ),
    SourceDuplicate(
        Path("bacterial/desulfonauticus_medium.yaml"),
        "CultureMech:001491",
        "mediadive.medium:383b",
        "DSMZ Medium 383b",
    ),
    SourceDuplicate(
        Path("bacterial/desulfovibrio_sax_medium.yaml"),
        "CultureMech:005156",
        "komodo.medium:383a",
        "KOMODO Medium 383a",
    ),
    SourceDuplicate(
        Path("bacterial/desulfovibrio_zosterae_medium.yaml"),
        "CultureMech:005158",
        "komodo.medium:383c",
        "KOMODO Medium 383c",
    ),
)

STRAIN_CHILDREN = (
    StrainChild(
        Path("bacterial/for_dsm_3382.yaml"),
        "CultureMech:005143",
        "komodo.medium:383.1",
        "KOMODO Medium 383.1",
        "DSM 3382",
    ),
    StrainChild(
        Path("bacterial/for_dsm_3383.yaml"),
        "CultureMech:005144",
        "komodo.medium:383.2",
        "KOMODO Medium 383.2",
        "DSM 3383",
    ),
    StrainChild(
        Path("bacterial/for_dsm_3384.yaml"),
        "CultureMech:005145",
        "komodo.medium:383.3",
        "KOMODO Medium 383.3",
        "DSM 3384",
    ),
    StrainChild(
        Path("bacterial/for_dsm_3385.yaml"),
        "CultureMech:005146",
        "komodo.medium:383.4",
        "KOMODO Medium 383.4",
        "DSM 3385",
    ),
    StrainChild(
        Path("bacterial/for_dsm_8541.yaml"),
        "CultureMech:005147",
        "komodo.medium:383.5",
        "KOMODO Medium 383.5",
        "DSM 8541",
    ),
    StrainChild(
        Path("bacterial/for_dsm_9120_dsm_17456_and_dsm_19275.yaml"),
        "CultureMech:005148",
        "komodo.medium:383.6",
        "KOMODO Medium 383.6",
        "DSM 9120, DSM 17456, and DSM 19275",
    ),
    StrainChild(
        Path("bacterial/for_dsm_12861_and_dsm_12883.yaml"),
        "CultureMech:005149",
        "komodo.medium:383.7",
        "KOMODO Medium 383.7",
        "DSM 12861 and DSM 12883",
    ),
    StrainChild(
        Path("bacterial/for_dsm_12888.yaml"),
        "CultureMech:005151",
        "komodo.medium:383.8",
        "KOMODO Medium 383.8",
        "DSM 12888",
    ),
    StrainChild(
        Path("bacterial/for_dsm_14367_dsm_15579_dsm_15816_dsm_19338_dsm_22027.yaml"),
        "CultureMech:005153",
        "komodo.medium:383.9",
        "KOMODO Medium 383.9",
        "DSM 14367, DSM 15579, DSM 15816, DSM 19338, and DSM 22027",
    ),
    StrainChild(
        Path("bacterial/for_dsm_14728.yaml"),
        "CultureMech:005134",
        "komodo.medium:383.11",
        "KOMODO Medium 383.11",
        "DSM 14728",
    ),
    StrainChild(
        Path("bacterial/for_dsm_14982.yaml"),
        "CultureMech:005135",
        "komodo.medium:383.12",
        "KOMODO Medium 383.12",
        "DSM 14982",
    ),
    StrainChild(
        Path("bacterial/for_dsm_15286_and_dsm_21156.yaml"),
        "CultureMech:005136",
        "komodo.medium:383.13",
        "KOMODO Medium 383.13",
        "DSM 15286 and DSM 21156",
    ),
    StrainChild(
        Path("bacterial/for_dsm_16109_and_dsm_17464.yaml"),
        "CultureMech:005137",
        "komodo.medium:383.14",
        "KOMODO Medium 383.14",
        "DSM 16109 and DSM 17464",
    ),
    StrainChild(
        Path("bacterial/for_dsm_17291.yaml"),
        "CultureMech:005138",
        "komodo.medium:383.15",
        "KOMODO Medium 383.15",
        "DSM 17291",
    ),
    StrainChild(
        Path("bacterial/for_dsm_17477.yaml"),
        "CultureMech:005139",
        "komodo.medium:383.16",
        "KOMODO Medium 383.16",
        "DSM 17477",
    ),
    StrainChild(
        Path("bacterial/for_dsm_18378_and_dsm_18379.yaml"),
        "CultureMech:005140",
        "komodo.medium:383.17",
        "KOMODO Medium 383.17",
        "DSM 18378 and DSM 18379",
    ),
    StrainChild(
        Path("bacterial/for_dsm_3379_dsm_3380_dsm_3381.yaml"),
        "CultureMech:005141",
        "komodo.medium:383.18",
        "KOMODO Medium 383.18",
        "DSM 3379, DSM 3380, and DSM 3381",
    ),
    StrainChild(
        Path("bacterial/for_dsm_14454.yaml"),
        "CultureMech:005142",
        "komodo.medium:383.19",
        "KOMODO Medium 383.19",
        "DSM 14454",
    ),
    StrainChild(
        Path("bacterial/for_dsm_18732.yaml"),
        "CultureMech:005155",
        "komodo.medium:383a.1",
        "KOMODO Medium 383a.1",
        "DSM 18732",
    ),
    StrainChild(
        Path("bacterial/medium_383_modified_for_dsm_10085.yaml"),
        "CultureMech:005130",
        "komodo.medium:383_10085",
        "KOMODO Medium 383_10085",
        "DSM 10085",
    ),
    StrainChild(
        Path("bacterial/medium_383_modified_for_dsm_10141.yaml"),
        "CultureMech:005131",
        "komodo.medium:383_10141",
        "KOMODO Medium 383_10141",
        "DSM 10141",
    ),
    StrainChild(
        Path("bacterial/medium_383_modified_for_dsm_10259.yaml"),
        "CultureMech:005132",
        "komodo.medium:383_10259",
        "KOMODO Medium 383_10259",
        "DSM 10259",
    ),
    StrainChild(
        Path("bacterial/medium_383_modified_for_dsm_11384.yaml"),
        "CultureMech:005133",
        "komodo.medium:383_11384",
        "KOMODO Medium 383_11384",
        "DSM 11384",
    ),
    StrainChild(
        Path("bacterial/medium_383_modified_for_dsm_8540.yaml"),
        "CultureMech:005150",
        "komodo.medium:383_8540",
        "KOMODO Medium 383_8540",
        "DSM 8540",
    ),
    StrainChild(
        Path("bacterial/medium_383_modified_for_dsm_9755.yaml"),
        "CultureMech:005152",
        "komodo.medium:383_9755",
        "KOMODO Medium 383_9755",
        "DSM 9755",
    ),
)

SOURCE_DUPLICATE_BY_PATH = {
    source_duplicate.path: source_duplicate for source_duplicate in SOURCE_DUPLICATES
}
STRAIN_CHILD_BY_PATH = {child.path: child for child in STRAIN_CHILDREN}
EXPECTED_SOURCE_DUPLICATE_COUNT = 5
EXPECTED_STRAIN_CHILD_COUNT = 25

CURATOR = "repair_komodo_383_desulfobacterium_score10.py"
ACTION = "RESOLVED_KOMODO_383_DESULFOBACTERIUM_TOPOLOGY"
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
    if len(SOURCE_DUPLICATES) != EXPECTED_SOURCE_DUPLICATE_COUNT or len(SOURCE_DUPLICATES) != len(
        SOURCE_DUPLICATE_BY_PATH
    ):
        raise ValueError(
            f"expected {EXPECTED_SOURCE_DUPLICATE_COUNT} unique duplicates, found "
            f"{len(SOURCE_DUPLICATES)} total and {len(SOURCE_DUPLICATE_BY_PATH)} unique"
        )
    if len(STRAIN_CHILDREN) != EXPECTED_STRAIN_CHILD_COUNT or len(STRAIN_CHILDREN) != len(
        STRAIN_CHILD_BY_PATH
    ):
        raise ValueError(
            f"expected {EXPECTED_STRAIN_CHILD_COUNT} unique strain children, found "
            f"{len(STRAIN_CHILDREN)} total and {len(STRAIN_CHILD_BY_PATH)} unique"
        )


def _duplicate_notes(source_duplicate: SourceDuplicate) -> str:
    return (
        f"{source_duplicate.source_label} has the same 32-component "
        "sulfate-reducing seawater mineral signature as KOMODO Medium 383."
    )


def _strain_notes(child: StrainChild) -> str:
    return f"{child.source_label} applies DESULFOBACTERIUM MEDIUM to {child.target}."


def _source_duplicate_entry(source_duplicate: SourceDuplicate) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{source_duplicate.path}",
        "relationship": SOURCE_DUPLICATE_RELATIONSHIP,
        "id": source_duplicate.record_id,
        "name": source_duplicate.path.stem,
        "notes": _duplicate_notes(source_duplicate),
    }


def _strain_child_entry(child: StrainChild) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": STRAIN_RELATIONSHIP,
        "id": child.record_id,
        "name": child.path.stem,
        "notes": _strain_notes(child),
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


def _require_source_duplicate(
    source_duplicate: SourceDuplicate,
    doc: dict[str, Any],
) -> None:
    _require_record(
        doc,
        source_duplicate.path,
        source_duplicate.record_id,
        source_duplicate.source_term,
    )


def _require_strain_child(child: StrainChild, doc: dict[str, Any]) -> None:
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
        [
            *[_source_duplicate_entry(source_duplicate) for source_duplicate in SOURCE_DUPLICATES],
            *[_strain_child_entry(child) for child in STRAIN_CHILDREN],
        ],
        "curation_history",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Promoted KOMODO Medium 383 as the Desulfobacterium parent",
            "source": "KOMODO and DSMZ Medium 383 exact-signature source records",
            "notes": (
                "Moved exact-signature KOMODO Medium 383 source duplicates and "
                "DSM-specific Medium 383 wrappers under the KOMODO Medium 383 base."
            ),
        },
    )
    return repaired


def repair_source_duplicate(
    relative_path: Path,
    doc: dict[str, Any],
) -> dict[str, Any]:
    source_duplicate = SOURCE_DUPLICATE_BY_PATH.get(relative_path)
    if source_duplicate is None:
        raise ValueError(f"unexpected source duplicate path {relative_path}")
    _require_source_duplicate(source_duplicate, doc)

    notes = _duplicate_notes(source_duplicate)
    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(SOURCE_DUPLICATE_RELATIONSHIP, notes),
        "curation_history",
    )
    _put_after(
        repaired,
        "variant_relationship",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "parent_media",
    )
    _put_after(repaired, "variant_modifications", [notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO Medium 383",
            "source": source_duplicate.source_label,
            "notes": notes,
        },
    )
    return repaired


def repair_strain_child(relative_path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    child = STRAIN_CHILD_BY_PATH.get(relative_path)
    if child is None:
        raise ValueError(f"unexpected strain child path {relative_path}")
    _require_strain_child(child, doc)

    notes = _strain_notes(child)
    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "parent_media",
        _parent_ref(STRAIN_RELATIONSHIP, notes),
        "curation_history",
    )
    _put_after(repaired, "variant_relationship", STRAIN_RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a KOMODO Medium 383 strain-specific variant",
            "source": child.source_label,
            "notes": notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    _validate_targets()
    plans = {normalized / PARENT: repair_parent(_load(normalized / PARENT))}
    for source_duplicate in SOURCE_DUPLICATES:
        plans[normalized / source_duplicate.path] = repair_source_duplicate(
            source_duplicate.path,
            _load(normalized / source_duplicate.path),
        )
    for child in STRAIN_CHILDREN:
        plans[normalized / child.path] = repair_strain_child(
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
