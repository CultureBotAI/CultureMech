#!/usr/bin/env python3
"""Repair KOMODO Desulfurobacterium strain and pH variants mislinked as duplicates."""

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

PARENT = Path("bacterial/KOMODO_829_DESULFUROBACTERIUM_MEDIUM.yaml")
PARENT_ID = "CultureMech:006564"
PARENT_NAME = "desulfurobacterium_medium"
PARENT_SOURCE_TERM = "komodo.medium:829"
PARENT_PH = 6.0

COMPOSITION_SIGNATURE = (
    ("ingredient", "Sea Salt", "29.8507", "G_PER_L"),
    ("ingredient", "NH4Cl", "0.995025", "G_PER_L"),
    ("ingredient", "KH2PO4", "0.348259", "G_PER_L"),
    (
        "ingredient",
        "MES [2-(N-morpholino) ethane sulfonic acid]",
        "1.9403",
        "G_PER_L",
    ),
    ("ingredient", "Sodium resazurin", "0.000497512", "G_PER_L"),
    ("ingredient", "Sulfur", "9.95025", "G_PER_L"),
    ("ingredient", "Na2CO3", "0.497512", "G_PER_L"),
    ("ingredient", "Isobutyric acid", "5", "G_PER_L"),
    ("ingredient", "Valeric acid", "5", "G_PER_L"),
    ("ingredient", "Tryptone", "10.0", "G_PER_L"),
    ("ingredient", "Yeast extract", "5.0", "G_PER_L"),
    ("ingredient", "Sodium chloride", "10.0", "G_PER_L"),
    ("ingredient", "Caproic acid", "2", "G_PER_L"),
    ("ingredient", "Succinic acid", "6", "G_PER_L"),
    ("ingredient", "HCl", "2.5", "G_PER_L"),
    ("ingredient", "ZnCl2", "0.07", "G_PER_L"),
    ("ingredient", "MnCl2 x 4 H2O", "0.1", "G_PER_L"),
    ("ingredient", "H3BO3", "0.006", "G_PER_L"),
    ("ingredient", "CoCl2 x 6 H2O", "0.19", "G_PER_L"),
    ("ingredient", "CuCl2 x 2 H2O", "0.002", "G_PER_L"),
    ("ingredient", "NiCl2 x 6 H2O", "0.024", "G_PER_L"),
    ("ingredient", "Na2MoO4 x 2 H2O", "0.036", "G_PER_L"),
    ("ingredient", "NaOH", "0.5", "G_PER_L"),
    ("ingredient", "Na2SeO3 x 5 H2O", "0.003", "G_PER_L"),
    ("ingredient", "Na2WO4 x 2 H2O", "0.004", "G_PER_L"),
    ("ingredient", "p-Aminobenzoic acid", "0.08", "G_PER_L"),
    ("ingredient", "D-(+)-biotin", "0.02", "G_PER_L"),
    ("ingredient", "Calcium pantothenate", "0.1", "G_PER_L"),
    ("ingredient", "Na2S2O4", "50", "G_PER_L"),
    ("solution", "Trace element solution SL-10", "", ""),
    ("solution_component", "FeCl2 x 4 H2O", "1.5", "G_PER_L"),
    ("solution", "Seven vitamins solution", "", ""),
    ("solution_component", "Vitamin B12", "0.1", "G_PER_L"),
    ("solution_component", "Nicotinic acid", "0.2", "G_PER_L"),
    ("solution_component", "Pyridoxine hydrochloride", "0.3", "G_PER_L"),
    ("solution_component", "Thiamine-HCl x 2 H2O", "0.2", "G_PER_L"),
)

CURATOR = "repair_komodo_829_desulfurobacterium_ph_score10.py"
ACTION = "RESOLVED_KOMODO_829_DESULFUROBACTERIUM_PH_VARIANT"
STRAIN_ACTION = "RESOLVED_KOMODO_829_DESULFUROBACTERIUM_STRAIN_VARIANT"
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
                f"{self.source_label} preserves DESULFUROBACTERIUM MEDIUM "
                f"components and pH {self.ph_value:g} but applies the recipe "
                f"for {self.dsm}."
            )
        return (
            f"{self.source_label} preserves DESULFUROBACTERIUM MEDIUM components "
            f"and concentrations but records pH {self.ph_value:g} for {self.dsm}."
        )

    @property
    def notes(self) -> str:
        return (
            f"{self.source_label} applies DESULFUROBACTERIUM MEDIUM at "
            f"pH {self.ph_value:g} for {self.dsm}."
        )

    @property
    def action(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return STRAIN_ACTION
        return ACTION

    @property
    def changes(self) -> str:
        if self.relationship == "STRAIN_SPECIFIC_VARIANT":
            return "Linked as a Desulfurobacterium strain-specific variant"
        return "Linked as a DESULFUROBACTERIUM MEDIUM pH variant"


CHILDREN = (
    Child(
        path=Path("bacterial/for_dsm_14290.yaml"),
        record_id="CultureMech:006561",
        name="for_dsm_14290",
        source_term="komodo.medium:829.1",
        ph_value=6.5,
        relationship="PH_VARIANT",
        dsm="DSM 14290",
    ),
    Child(
        path=Path("bacterial/for_dsm_21157.yaml"),
        record_id="CultureMech:006563",
        name="for_dsm_21157",
        source_term="komodo.medium:829.3",
        ph_value=6.0,
        relationship="STRAIN_SPECIFIC_VARIANT",
        dsm="DSM 21157",
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
        "notes": (f"KOMODO Medium 829 is the pH {PARENT_PH:g} " "DESULFUROBACTERIUM MEDIUM base."),
    }


def _upsert_child_entry(children: list[Any], child: Child) -> None:
    path = f"data/normalized_yaml/{child.path}"
    for index, existing in enumerate(children):
        if isinstance(existing, dict) and existing.get("path") == path:
            children[index] = _child_entry(child)
            return
    raise ValueError(f"{PARENT}: missing variant child {path}")


def _require_desulfurobacterium_record(
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
    if _composition_signature(doc) != COMPOSITION_SIGNATURE:
        raise ValueError(f"{relative_path}: composition signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_desulfurobacterium_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM, PARENT_PH)
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
            "changes": "Linked a DESULFUROBACTERIUM MEDIUM pH variant child",
            "source": "KOMODO Medium 829.1",
            "notes": (
                "Changed DSM 14290 from SOURCE_DUPLICATE to PH_VARIANT " "under KOMODO Medium 829."
            ),
        },
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": STRAIN_ACTION,
            "changes": "Linked Desulfurobacterium strain-specific children",
            "source": "KOMODO Medium 829.3",
            "notes": (
                "Changed DSM 21157 from SOURCE_DUPLICATE to a "
                "STRAIN_SPECIFIC_VARIANT child of DESULFUROBACTERIUM MEDIUM."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_desulfurobacterium_record(
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
