#!/usr/bin/env python3
"""Repair KOMODO 120 Methanosarcina exact and strain child links."""

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

PARENT = Path("archaea/KOMODO_120_METHANOSARCINA_medium.yaml")
PARENT_ID = "CultureMech:003958"
PARENT_NAME = "methanosarcina_medium"
PARENT_SOURCE_TERM = "komodo.medium:120"
SOURCE_DUPLICATE_RELATIONSHIP = "SOURCE_DUPLICATE"
STRAIN_RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

SIGNATURE = (
    ("K2HPO4", "0.341797", "G_PER_L"),
    ("KH2PO4", "0.224609", "G_PER_L"),
    ("NH4Cl", "0.488281", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.488281", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.244141", "G_PER_L"),
    ("NaCl", "2.19727", "G_PER_L"),
    ("Yeast extract", "1.95312", "G_PER_L"),
    ("Casitone", "1.95312", "G_PER_L"),
    ("Sodium resazurin", "0.000488281", "G_PER_L"),
    ("NaHCO3", "0.830078", "G_PER_L"),
    ("Methanol", "15.4688", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.292969", "G_PER_L"),
    ("Na2S x 9 H2O", "0.292969", "G_PER_L"),
    ("FeSO4 x 7 H2O", "1", "G_PER_L"),
    ("H2SO4", "1000", "G_PER_L"),
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
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    relationship: str
    notes: str


CHILDREN = (
    Child(
        Path("bacterial/g_1_medium.yaml"),
        "CultureMech:003959",
        "komodo.medium:120a",
        "KOMODO Medium 120a",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "KOMODO Medium 120a has the same 34-ingredient signature as KOMODO Medium 120.",
    ),
    Child(
        Path("archaea/KOMODO_120b_METHANOMICROCOCCUS_medium.yaml"),
        "CultureMech:003960",
        "komodo.medium:120b",
        "KOMODO Medium 120b",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "KOMODO Medium 120b has the same 34-ingredient signature as KOMODO Medium 120.",
    ),
    Child(
        Path("bacterial/to_adapt_dsm_804_on_acetate.yaml"),
        "CultureMech:003942",
        "komodo.medium:120.1",
        "KOMODO Medium 120.1",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 120.1 applies KOMODO Medium 120 to DSM 804 acetate adaptation.",
    ),
    Child(
        Path(
            "archaea/"
            "for_strains_of_methanosarcina_mazei_and_dsm_1538_dsm_11429_"
            "dsm_11430_dsm11431_dsm_11432_dsm_11433_and_dsm_11434.yaml"
        ),
        "CultureMech:003943",
        "komodo.medium:120.2",
        "KOMODO Medium 120.2",
        STRAIN_RELATIONSHIP,
        (
            "KOMODO Medium 120.2 applies KOMODO Medium 120 to Methanosarcina mazei "
            "strains and DSM 1538, DSM 11429, DSM 11430, DSM 11431, DSM 11432, "
            "DSM 11433 and DSM 11434."
        ),
    ),
    Child(
        Path("bacterial/for_dsm_4556_dsm_10334_and_dsm_13486.yaml"),
        "CultureMech:003944",
        "komodo.medium:120.3",
        "KOMODO Medium 120.3",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 120.3 applies KOMODO Medium 120 to DSM 4556, DSM 10334 and DSM 13486.",
    ),
    Child(
        Path("bacterial/for_dsm_9195.yaml"),
        "CultureMech:003945",
        "komodo.medium:120.4",
        "KOMODO Medium 120.4",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 120.4 applies KOMODO Medium 120 to DSM 9195.",
    ),
    Child(
        Path("bacterial/for_dsm_21571.yaml"),
        "CultureMech:003946",
        "komodo.medium:120.5",
        "KOMODO Medium 120.5",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 120.5 applies KOMODO Medium 120 to DSM 21571.",
    ),
    Child(
        Path("bacterial/medium_120_modified_for_dsm_7058.yaml"),
        "CultureMech:003947",
        "komodo.medium:120_7058",
        "KOMODO Medium 120_7058",
        STRAIN_RELATIONSHIP,
        "KOMODO Medium 120_7058 applies KOMODO Medium 120 to DSM 7058.",
    ),
    Child(
        Path("archaea/methanosarcina_barkeri_medium.yaml"),
        "CultureMech:000661",
        "mediadive.medium:120a",
        "DSMZ Medium 120a",
        SOURCE_DUPLICATE_RELATIONSHIP,
        "DSMZ Medium 120a has the same 34-ingredient signature as KOMODO Medium 120.",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 9

CURATOR = "repair_komodo_120_methanosarcina_score10.py"
ACTION = "RESOLVED_KOMODO_120_METHANOSARCINA_TOPOLOGY"
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
            "changes": "Resolved KOMODO Medium 120 duplicate wrappers and strain links",
            "source": "KOMODO Medium 120a-120b, 120.1-120.5, 120_7058; DSMZ Medium 120a",
            "notes": (
                "Kept exact DSMZ/KOMODO aliases as source duplicates and changed "
                "strain/adaptation wrappers from duplicate links to variants."
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
            "changes": f"Linked under KOMODO Medium 120 as {child.relationship}",
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
