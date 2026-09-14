#!/usr/bin/env python3
"""Repair KOMODO 135 Acetobacterium pH-variant links."""

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

PARENT = Path("specialized/acetobacterium_medium_marine.yaml")
PARENT_ID = "CultureMech:015340"
PARENT_NAME = "acetobacterium_medium_marine"
PARENT_SOURCE_TERM = "mediadive.medium:135a"
PARENT_PH = {"min": 7.0, "max": 7.2}

BASE_SIGNATURE = (
    ("NaCl", "20.5886", "G_PER_L"),
    ("NH4Cl", "0.979432", "G_PER_L"),
    ("KH2PO4", "0.323213", "G_PER_L"),
    ("K2HPO4", "0.440744", "G_PER_L"),
    ("MgSO4 x 7 H2O", "3.0979432", "G_PER_L"),
    ("Yeast extract", "1.95886", "G_PER_L"),
    ("Resazurin", "0.000489716", "G_PER_L"),
    ("NaHCO3", "4.89716", "G_PER_L"),
    ("Ethylene glycol", "1.22429", "G_PER_L"),
    ("L-Cysteine HCl x H2O", "0.489716", "G_PER_L"),
    ("Na2S x 9 H2O", "0.489716", "G_PER_L"),
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MnSO4 x H2O", "0.5", "G_PER_L"),
    ("FeSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.18", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.1", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.18", "G_PER_L"),
    ("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2 x 12 H2O", "0.02", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.01", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.03", "G_PER_L"),
    ("Na2SeO3 x 5 H2O", "0.0003", "G_PER_L"),
    ("Na2WO4 x 2 H2O", "0.0004", "G_PER_L"),
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
SODIUM_CARBONATE_SIGNATURE = BASE_SIGNATURE + (("Na2CO3", "variable", "VARIABLE"),)

CURATOR = "repair_komodo_135_acetobacterium_score10.py"
ACTION = "RESOLVED_KOMODO_135_ACETOBACTERIUM_PH_TOPOLOGY"
TIMESTAMP = "2026-09-13T00:00:00-07:00"
RELATIONSHIP = "PH_VARIANT"
PARENT_NOTE = "DSMZ Medium 135a is the pH 7.0-7.2 marine Acetobacterium base."


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    ph_value: float
    signature: tuple[tuple[str, str, str], ...]
    context: str

    @property
    def name(self) -> str:
        return self.path.stem

    @property
    def notes(self) -> str:
        extra = (
            " and adds variable sodium carbonate for pH adjustment"
            if self.signature == SODIUM_CARBONATE_SIGNATURE
            else ""
        )
        return (
            f"{self.source_label} applies the marine Acetobacterium signature"
            f"{extra} at pH {self.ph_value:g} for {self.context}."
        )


CHILDREN = (
    Child(
        Path("bacterial/KOMODO_135_ACETOBACTERIUM_medium.yaml"),
        "CultureMech:004107",
        "komodo.medium:135",
        "KOMODO Medium 135",
        8.2,
        SODIUM_CARBONATE_SIGNATURE,
        "ACETOBACTERIUM medium",
    ),
    Child(
        Path("bacterial/for_autotrophic_growth.yaml"),
        "CultureMech:004102",
        "komodo.medium:135.1",
        "KOMODO Medium 135.1",
        8.2,
        SODIUM_CARBONATE_SIGNATURE,
        "autotrophic growth",
    ),
    Child(
        Path("bacterial/for_dsm_1974.yaml"),
        "CultureMech:004103",
        "komodo.medium:135.2",
        "KOMODO Medium 135.2",
        6.5,
        BASE_SIGNATURE,
        "DSM 1974",
    ),
    Child(
        Path("bacterial/for_dsm_4132.yaml"),
        "CultureMech:004104",
        "komodo.medium:135.3",
        "KOMODO Medium 135.3",
        8.2,
        SODIUM_CARBONATE_SIGNATURE,
        "DSM 4132",
    ),
    Child(
        Path("bacterial/medium_135_modified_for_dsm_7417.yaml"),
        "CultureMech:004105",
        "komodo.medium:135_7417",
        "KOMODO Medium 135_7417",
        6.5,
        BASE_SIGNATURE,
        "DSM 7417",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 5


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


def _validate_targets() -> None:
    if len(CHILDREN) != EXPECTED_CHILD_COUNT or len(CHILDREN) != len(CHILD_BY_PATH):
        raise ValueError(
            f"expected {EXPECTED_CHILD_COUNT} unique children, found "
            f"{len(CHILDREN)} total and {len(CHILD_BY_PATH)} unique"
        )


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": RELATIONSHIP,
        "id": child.record_id,
        "name": child.name,
        "notes": child.notes,
    }


def _parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": PARENT_NOTE,
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ph: Any,
    signature: tuple[tuple[str, str, str], ...],
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ph(doc) != ph:
        raise ValueError(f"{relative_path}: expected pH {ph!r}")
    if _ingredient_signature(doc) != signature:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def _require_parent(doc: dict[str, Any]) -> None:
    _require_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_PH, BASE_SIGNATURE)


def _require_child(child: Child, doc: dict[str, Any]) -> None:
    _require_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
        child.ph_value,
        child.signature,
    )


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
            "changes": "Promoted DSMZ Medium 135a to the KOMODO 135 pH parent",
            "source": "DSMZ Medium 135a; KOMODO Medium 135, 135.1, 135.2, 135.3",
            "notes": (
                "Grouped the KOMODO 135 pH 6.5 and pH 8.2 wrappers "
                "under the marine Acetobacterium base."
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
    _put_after(repaired, "parent_media", _parent_ref(), "curation_history")
    _put_after(repaired, "variant_relationship", RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under DSMZ Medium 135a as a pH variant",
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
