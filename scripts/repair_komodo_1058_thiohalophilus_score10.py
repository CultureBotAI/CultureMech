#!/usr/bin/env python3
"""Repair KOMODO 1058 Thiohalophilus strain child links."""

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

PARENT = Path("bacterial/thiohalophilus_medium.yaml")
PARENT_ID = "CultureMech:003641"
PARENT_NAME = "thiohalophilus_medium"
PARENT_SOURCE_TERM = "komodo.medium:1058"
RELATIONSHIP = "STRAIN_SPECIFIC_VARIANT"

COMPOSITION_SIGNATURE = (
    ("ingredient", "NaCl", "233", "G_PER_L"),
    ("ingredient", "K2HPO4", "1.5", "G_PER_L"),
    ("ingredient", "NH4Cl", "0.5", "G_PER_L"),
    ("ingredient", "CaCl2 x 2 H2O", "0.05", "G_PER_L"),
    ("ingredient", "MgCl2 x 6 H2O", "0.4", "G_PER_L"),
    ("ingredient", "Na2S2O3 x 5 H2O", "5", "G_PER_L"),
    ("ingredient", "NaHCO3", "2.5", "G_PER_L"),
    ("ingredient", "EDTA", "5", "G_PER_L"),
    ("ingredient", "ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("ingredient", "MnCl2 x 4 H2O", "0.03", "G_PER_L"),
    ("ingredient", "H3BO3", "0.03", "G_PER_L"),
    ("ingredient", "CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("ingredient", "CuCl2 x 2 H2O", "0.03", "G_PER_L"),
    ("ingredient", "NiCl2 x 6 H2O", "0.03", "G_PER_L"),
    ("ingredient", "Na2MoO4 x 2 H2O", "0.03", "G_PER_L"),
    ("ingredient", "p-Aminobenzoic acid", "0.08", "G_PER_L"),
    ("ingredient", "D-(+)-biotin", "0.02", "G_PER_L"),
    ("ingredient", "Calcium pantothenate", "0.1", "G_PER_L"),
    ("solution", "Trace elements solution (Pfennig, 1965)", "", ""),
    ("solution_component", "FeSO4 x 7 H2O", "2.2", "G_PER_L"),
    ("solution", "Seven vitamins solution", "", ""),
    ("solution_component", "Vitamin B12", "0.1", "G_PER_L"),
    ("solution_component", "Nicotinic acid", "0.2", "G_PER_L"),
    ("solution_component", "Pyridoxine hydrochloride", "0.3", "G_PER_L"),
    ("solution_component", "Thiamine-HCl x 2 H2O", "0.2", "G_PER_L"),
)


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    source_term: str
    source_label: str
    strains: str
    ph_note: str = ""

    @property
    def notes(self) -> str:
        note = (
            f"{self.source_label} applies the KOMODO Medium 1058 bulk ingredients "
            f"and stock compositions to {self.strains}"
        )
        if self.ph_note:
            note = f"{note} with {self.ph_note}"
        return f"{note}."


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_15070_and_dsm_15071.yaml"),
        "CultureMech:003636",
        "komodo.medium:1058.1",
        "KOMODO Medium 1058.1",
        "DSM 15070 and DSM 15071",
        "recorded pH 7.2",
    ),
    Child(
        Path("bacterial/for_dsm_15074.yaml"),
        "CultureMech:003637",
        "komodo.medium:1058.2",
        "KOMODO Medium 1058.2",
        "DSM 15074",
    ),
    Child(
        Path("bacterial/for_dsm_15699.yaml"),
        "CultureMech:003638",
        "komodo.medium:1058.3",
        "KOMODO Medium 1058.3",
        "DSM 15699",
    ),
    Child(
        Path("bacterial/for_dsm_15841_and_dsm_16925.yaml"),
        "CultureMech:003639",
        "komodo.medium:1058.4",
        "KOMODO Medium 1058.4",
        "DSM 15841 and DSM 16925",
    ),
    Child(
        Path("bacterial/for_dsm_21152.yaml"),
        "CultureMech:003640",
        "komodo.medium:1058.5",
        "KOMODO Medium 1058.5",
        "DSM 21152",
    ),
)
CHILD_BY_PATH = {child.path: child for child in CHILDREN}
EXPECTED_CHILD_COUNT = 5

CURATOR = "repair_komodo_1058_thiohalophilus_score10.py"
ACTION = "RESOLVED_KOMODO_1058_THIOHALOPHILUS_TOPOLOGY"
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


def _composition_signature(doc: dict[str, Any]) -> tuple[tuple[str, str, str, str], ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")

    signature: list[tuple[str, str, str, str]] = []
    for row in ingredients:
        if not isinstance(row, dict):
            continue
        concentration = row.get("concentration") or {}
        if not isinstance(concentration, dict):
            concentration = {}
        signature.append(
            (
                "ingredient",
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    for solution in solutions:
        if not isinstance(solution, dict):
            continue
        signature.append(("solution", str(solution.get("preferred_term") or ""), "", ""))
        composition = solution.get("composition") or []
        if not isinstance(composition, list):
            raise ValueError("solution composition is not a list")
        for row in composition:
            if not isinstance(row, dict):
                continue
            concentration = row.get("concentration") or {}
            if not isinstance(concentration, dict):
                concentration = {}
            signature.append(
                (
                    "solution_component",
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
        "name": child.path.stem,
        "notes": child.notes,
    }


def _parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": RELATIONSHIP,
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
    if _composition_signature(doc) != COMPOSITION_SIGNATURE:
        raise ValueError(f"{relative_path}: composition signature drifted")


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
            "changes": "Re-rooted KOMODO Medium 1058 strain-wrapper topology",
            "source": "KOMODO Medium 1058 and 1058.1-1058.5",
            "notes": (
                "Kept the KOMODO-derived 1058 strain wrappers under the local "
                "KOMODO Medium 1058 formulation."
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
    _put_after(repaired, "variant_relationship", RELATIONSHIP, "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": f"Linked under KOMODO Medium 1058 as {RELATIONSHIP}",
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
