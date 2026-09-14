#!/usr/bin/env python3
"""Repair provisional KOMODO 516 ANAEROCELLUM child links."""

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

HUB = Path("bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml")
HUB_ID = "CultureMech:005874"
HUB_NAME = "anaerocellum_medium"
HUB_SOURCE_TERM = "komodo.medium:516"
HUB_PH = {"min": 7.1, "max": 7.3}

PARENT = Path("bacterial/anaerocellum_medium.yaml")
PARENT_ID = "CultureMech:001648"
PARENT_NAME = "anaerocellum_medium"

INGREDIENT_SIGNATURE = (
    ("NH4Cl", "0.329341", "G_PER_L"),
    ("KH2PO4", "0.329341", "G_PER_L"),
    ("KCl", "0.329341", "G_PER_L"),
    ("MgCl2 x 6 H2O", "0.329341", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.329341", "G_PER_L"),
    ("Yeast extract", "0.499002", "G_PER_L"),
    ("Sodium resazurin", "0.000499002", "G_PER_L"),
    ("Na2CO3", "1.49701", "G_PER_L"),
    ("Cellobiose", "4.99002", "G_PER_L"),
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

CURATOR = "repair_komodo_516_anaerocellum_score10.py"
ACTION = "RESOLVED_KOMODO_516_ANAEROCELLUM_TOPOLOGY"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def source_label(source_term: str) -> str:
    if source_term.startswith("komodo.medium:"):
        return f"KOMODO Medium {source_term.removeprefix('komodo.medium:')}"
    return source_term


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    ph: Any
    notes: str

    @property
    def source_label(self) -> str:
        return source_label(self.source_term)


CHILDREN = (
    Child(
        Path("bacterial/for_dsm_6724.yaml"),
        "CultureMech:005872",
        "for_dsm_6724",
        "komodo.medium:516.1",
        {"min": 7.1, "max": 7.3},
        "KOMODO Medium 516.1 applies ANAEROCELLUM MEDIUM for DSM 6724.",
    ),
    Child(
        Path("bacterial/medium_516_modified_for_dsm_9003.yaml"),
        "CultureMech:005873",
        "medium_516_modified_for_dsm_9003",
        "komodo.medium:516_9003",
        None,
        "KOMODO Medium 516_9003 applies ANAEROCELLUM MEDIUM for DSM 9003.",
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


def _child_entry(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{child.path}",
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": child.record_id,
        "name": child.name,
        "notes": child.notes,
    }


def _child_parent_ref(child: Child) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{HUB}",
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": HUB_ID,
        "name": HUB_NAME,
        "notes": "KOMODO Medium 516 exactly mirrors DSMZ ANAEROCELLUM MEDIUM.",
    }


def _hub_parent_ref() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "SOURCE_DUPLICATE",
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": (
            "KOMODO Medium 516 exactly mirrors the DSMZ/MediaDive " "ANAEROCELLUM MEDIUM record."
        ),
    }


def _require_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
    ph: Any,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if _ph(doc) != ph:
        raise ValueError(f"{relative_path}: expected pH {ph!r}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_hub(doc: dict[str, Any]) -> dict[str, Any]:
    _require_record(doc, HUB, HUB_ID, HUB_SOURCE_TERM, HUB_PH)

    repaired = copy.deepcopy(doc)
    _ensure_ingredients_curated(repaired)
    _put_after(
        repaired,
        "variant_children",
        [_child_entry(child) for child in CHILDREN],
        "curation_history",
    )
    _put_after(repaired, "parent_media", _hub_parent_ref(), "variant_children")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        ["KOMODO Medium 516 exactly mirrors DSMZ ANAEROCELLUM MEDIUM."],
        "variant_relationship",
    )
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Finalized KOMODO Medium 516 as the duplicate child hub",
            "source": "MediaDive Medium 516 and KOMODO Medium 516",
            "notes": (
                "Kept KOMODO Medium 516 under the DSMZ/MediaDive parent and "
                "finalized its two DSM-specific exact-copy children."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_record(doc, child.path, child.record_id, child.source_term, child.ph)

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _child_parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", "STRAIN_SPECIFIC_VARIANT", "parent_media")
    _put_after(repaired, "variant_modifications", [child.notes], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked as a strain-specific variant under KOMODO Medium 516",
            "source": child.source_label,
            "notes": child.notes,
        },
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    repairs = {normalized / HUB: repair_hub(_load(normalized / HUB))}
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
