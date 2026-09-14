#!/usr/bin/env python3
"""Repair KOMODO 390 Pyrobaculum duplicate paths and strain variants."""

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

DSMZ_PARENT = Path("archaea/pyrobaculum_medium.yaml")
DSMZ_PARENT_ID = "CultureMech:001497"
DSMZ_PARENT_NAME = "pyrobaculum_medium"
DSMZ_SOURCE_TERM = "mediadive.medium:390"

KOMODO_PARENT = Path("archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml")
KOMODO_PARENT_ID = "CultureMech:005172"
KOMODO_PARENT_NAME = "pyrobaculum_medium"
KOMODO_SOURCE_TERM = "komodo.medium:390"

INGREDIENT_SIGNATURE = (
    ("(NH4)2SO4", "1.28713", "G_PER_L"),
    ("KH2PO4", "0.277228", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.247525", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.0693069", "G_PER_L"),
    ("FeCl3 x 6 H2O", "0.019802", "G_PER_L"),
    ("Sodium resazurin", "0.00049505", "G_PER_L"),
    ("Trypticase peptone", "0.49505", "G_PER_L"),
    ("Yeast extract", "0.19802", "G_PER_L"),
    ("Na2S2O3 x 5 H2O", "1.9802", "G_PER_L"),
    ("Na2S x 9 H2O", "0.49505", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.18", "G_PER_L"),
    ("Na2B4O7 x 10 H2O", "0.45", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.022", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.005", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.003", "G_PER_L"),
    ("VOSO4 x 2 H2O", "0.003", "G_PER_L"),
    ("CoSO4 x 7 H2O", "0.001", "G_PER_L"),
)

CURATOR = "repair_komodo_390_pyrobaculum_score10.py"
ACTION = "RESOLVED_KOMODO_390_PYROBACULUM_STRAIN_VARIANTS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    context: str

    @property
    def source_label(self) -> str:
        return f"KOMODO Medium {self.source_term.removeprefix('komodo.medium:')}"

    @property
    def notes(self) -> str:
        return f"{self.source_label} applies PYROBACULUM MEDIUM for {self.context}."


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_4184.yaml"),
        "CultureMech:005168",
        "for_dsm_4184",
        "komodo.medium:390.1",
        "DSM 4184",
    ),
    Child(
        Path("bacterial/for_dsm_4185.yaml"),
        "CultureMech:005169",
        "for_dsm_4185",
        "komodo.medium:390.2",
        "DSM 4185",
    ),
    Child(
        Path("bacterial/for_dsm_13380.yaml"),
        "CultureMech:005170",
        "for_dsm_13380",
        "komodo.medium:390.3",
        "DSM 13380",
    ),
    Child(
        Path("bacterial/for_dsm_13514.yaml"),
        "CultureMech:005171",
        "for_dsm_13514",
        "komodo.medium:390.4",
        "DSM 13514",
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
    return tuple(
        (
            str(row.get("preferred_term") or ""),
            str((row.get("concentration") or {}).get("value") or ""),
            str((row.get("concentration") or {}).get("unit") or ""),
        )
        for row in ingredients
        if isinstance(row, dict)
    )


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


def _komodo_source_child_entry() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{KOMODO_PARENT}",
        "relationship": "SOURCE_DUPLICATE",
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT_NAME,
        "notes": (
            "KOMODO record is an exact source duplicate of DSMZ Medium 390; "
            "local ingredient and concentration signatures match."
        ),
    }


def _dsmz_parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{DSMZ_PARENT}",
        "relationship": "SOURCE_DUPLICATE",
        "id": DSMZ_PARENT_ID,
        "name": DSMZ_PARENT_NAME,
        "notes": (
            "KOMODO record explicitly cites DSMZ Medium 390; local physical state, "
            "pH, ingredient, and concentration signatures match exactly."
        ),
    }


def _strain_child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": child.record_id,
        "name": child.name,
        "notes": child.notes,
    }


def _komodo_parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{KOMODO_PARENT}",
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": KOMODO_PARENT_ID,
        "name": KOMODO_PARENT_NAME,
        "notes": "KOMODO Medium 390 is the PYROBACULUM MEDIUM base.",
    }


def repair_dsmz_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, DSMZ_PARENT, DSMZ_PARENT_ID, DSMZ_SOURCE_TERM)
    repaired = copy.deepcopy(doc)
    _put_after(repaired, "variant_children", [_komodo_source_child_entry()], "curation_history")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Corrected KOMODO Medium 390 source-duplicate path",
            "source": "MediaDive Medium 390 and KOMODO Medium 390",
            "notes": "Pointed the DSMZ parent at the actual archaeal KOMODO Medium 390 file.",
        },
    )
    return repaired


def repair_komodo_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, KOMODO_PARENT, KOMODO_PARENT_ID, KOMODO_SOURCE_TERM)
    repaired = copy.deepcopy(doc)
    _put_after(repaired, "parent_media", _dsmz_parent_ref(), "curation_history")
    _put_after(
        repaired,
        "variant_children",
        [_strain_child_entry(child) for child in CHILDREN],
        "variant_modifications",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Reclassified KOMODO Medium 390 DSM children as strain variants",
            "source": "KOMODO Medium 390-390.4",
            "notes": (
                "Corrected the parent path to the archaeal KOMODO base and kept "
                "the four DSM-specific suffixes beneath that base."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_record(doc, child.path, child.record_id, child.source_term)
    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _komodo_parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", "STRAIN_SPECIFIC_VARIANT", "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under KOMODO PYROBACULUM MEDIUM",
            "source": child.source_label,
            "notes": child.notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    repairs = {
        normalized / DSMZ_PARENT: repair_dsmz_parent(_load(normalized / DSMZ_PARENT)),
        normalized / KOMODO_PARENT: repair_komodo_parent(_load(normalized / KOMODO_PARENT)),
    }
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
