#!/usr/bin/env python3
"""Repair KOMODO 133 topology rooted at a strain-specific duplicate."""

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

PARENT = Path("bacterial/medium_for_carbon_monoxide_oxidizers.yaml")
PARENT_ID = "CultureMech:004098"
PARENT_NAME = "medium_for_carbon_monoxide_oxidizers"
PARENT_SOURCE_TERM = "komodo.medium:133"
PARENT_PH = 7.0

INGREDIENT_SIGNATURE = (
    ("Na2HPO4 x 12 H2O", "4.5", "G_PER_L"),
    ("KH2PO4", "0.75", "G_PER_L"),
    ("NH4Cl", "1.5", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.2", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.03", "G_PER_L"),
    ("Ferric ammonium citrate", "0.018", "G_PER_L"),
    ("Na-acetate", "3", "G_PER_L"),
    ("Agar", "12", "G_PER_L"),
    ("ZnSO4 x 7 H2O", "0.1", "G_PER_L"),
    ("MnCl2 x 4 H2O", "0.03", "G_PER_L"),
    ("H3BO3", "0.3", "G_PER_L"),
    ("CoCl2 x 6 H2O", "0.2", "G_PER_L"),
    ("CuCl2 x 2 H2O", "0.01", "G_PER_L"),
    ("NiCl2 x 6 H2O", "0.02", "G_PER_L"),
    ("Na2MoO4 x 2 H2O", "0.03", "G_PER_L"),
)

CURATOR = "repair_komodo_133_carbon_monoxide_topology_score10.py"
ACTION = "RESOLVED_KOMODO_133_CARBON_MONOXIDE_TOPOLOGY"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def source_label(source_term: str) -> str:
    if source_term.startswith("komodo.medium:"):
        return f"KOMODO Medium {source_term.removeprefix('komodo.medium:')}"
    if source_term.startswith("mediadive.medium:"):
        return f"MediaDive Medium {source_term.removeprefix('mediadive.medium:')}"
    return source_term


@dataclass(frozen=True)
class Child:
    path: Path
    record_id: str
    name: str
    source_term: str
    relationship: str
    context: str

    @property
    def source_label(self) -> str:
        return source_label(self.source_term)

    @property
    def notes(self) -> str:
        if self.relationship == "SOURCE_DUPLICATE":
            return (
                f"{self.source_label} exactly matches the KOMODO Medium 133 "
                "MEDIUM FOR CARBON MONOXIDE OXIDIZERS base."
            )
        return (
            f"{self.source_label} applies MEDIUM FOR CARBON MONOXIDE OXIDIZERS "
            f"at pH {PARENT_PH:g} for {self.context}."
        )

    @property
    def modification(self) -> str:
        return self.notes


CHILDREN = (
    Child(
        path=Path("bacterial/carbon_monoxide_oxidizer_medium.yaml"),
        record_id="CultureMech:000797",
        name="carbon_monoxide_oxidizer_medium",
        source_term="mediadive.medium:133",
        relationship="SOURCE_DUPLICATE",
        context="DSMZ Medium 133",
    ),
    Child(
        path=Path("bacterial/for_chemoautotrophic_growth.yaml"),
        record_id="CultureMech:004086",
        name="for_chemoautotrophic_growth",
        source_term="komodo.medium:133.1",
        relationship="SOURCE_DUPLICATE",
        context="chemoautotrophic growth",
    ),
    Child(
        path=Path("bacterial/for_chemoorganotrophic_growth.yaml"),
        record_id="CultureMech:004087",
        name="for_chemoorganotrophic_growth",
        source_term="komodo.medium:133.2",
        relationship="SOURCE_DUPLICATE",
        context="chemoorganotrophic growth",
    ),
    Child(
        path=Path("bacterial/for_dsm_1083.yaml"),
        record_id="CultureMech:004088",
        name="for_dsm_1083",
        source_term="komodo.medium:133.3",
        relationship="STRAIN_SPECIFIC_VARIANT",
        context="DSM 1083",
    ),
    Child(
        path=Path("bacterial/for_dsm_1083_chemoorganotrophic_growth.yaml"),
        record_id="CultureMech:004089",
        name="for_dsm_1083_chemoorganotrophic_growth",
        source_term="komodo.medium:133.4",
        relationship="STRAIN_SPECIFIC_VARIANT",
        context="DSM 1083, chemoorganotrophic growth",
    ),
    Child(
        path=Path("bacterial/for_dsm_1085.yaml"),
        record_id="CultureMech:004090",
        name="for_dsm_1085",
        source_term="komodo.medium:133.5",
        relationship="STRAIN_SPECIFIC_VARIANT",
        context="DSM 1085",
    ),
    Child(
        path=Path("bacterial/for_dsm_1085_chemoorganotrophic_growth.yaml"),
        record_id="CultureMech:004091",
        name="for_dsm_1085_chemoorganotrophic_growth",
        source_term="komodo.medium:133.6",
        relationship="STRAIN_SPECIFIC_VARIANT",
        context="DSM 1085, chemoorganotrophic growth",
    ),
    Child(
        path=Path("bacterial/for_dsm_13294.yaml"),
        record_id="CultureMech:004092",
        name="for_dsm_13294",
        source_term="komodo.medium:133.7",
        relationship="STRAIN_SPECIFIC_VARIANT",
        context="DSM 13294",
    ),
    Child(
        path=Path("bacterial/for_dsm_13294_chemoorganotrophic_growth.yaml"),
        record_id="CultureMech:004093",
        name="for_dsm_13294_chemoorganotrophic_growth",
        source_term="komodo.medium:133.8",
        relationship="STRAIN_SPECIFIC_VARIANT",
        context="DSM 13294, chemoorganotrophic growth",
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
        "notes": (
            f"KOMODO Medium 133 is the pH {PARENT_PH:g} "
            "MEDIUM FOR CARBON MONOXIDE OXIDIZERS base."
        ),
    }


def _require_carbon_monoxide_record(
    doc: dict[str, Any],
    relative_path: Path,
    record_id: str,
    source_term: str,
) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{relative_path}: expected {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != source_term:
        raise ValueError(f"{relative_path}: expected {source_term}")
    if doc.get("ph_value") != PARENT_PH:
        raise ValueError(f"{relative_path}: expected pH {PARENT_PH:g}")
    if _ingredient_signature(doc) != INGREDIENT_SIGNATURE:
        raise ValueError(f"{relative_path}: ingredient signature drifted")


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_carbon_monoxide_record(doc, PARENT, PARENT_ID, PARENT_SOURCE_TERM)

    repaired = copy.deepcopy(doc)
    repaired.pop("parent_media", None)
    repaired.pop("variant_relationship", None)
    repaired.pop("variant_modifications", None)
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
            "changes": (
                "Promoted KOMODO Medium 133 to the carbon monoxide oxidizer "
                "family parent"
            ),
            "source": "KOMODO Medium 133-133.8 and MediaDive Medium 133",
            "notes": (
                "Moved the family root from strain-specific KOMODO Medium 133.3 "
                "to base KOMODO Medium 133 and reclassified DSM-specific submedia "
                "as strain-specific variants."
            ),
        },
    )
    return repaired


def repair_child(doc: dict[str, Any], child: Child) -> dict[str, Any]:
    _require_carbon_monoxide_record(
        doc,
        child.path,
        child.record_id,
        child.source_term,
    )

    repaired = copy.deepcopy(doc)
    repaired.pop("variant_children", None)
    _ensure_ingredients_curated(repaired)
    _put_after(repaired, "parent_media", _parent_ref(child), "curation_history")
    _put_after(repaired, "variant_relationship", child.relationship, "parent_media")
    _put_after(repaired, "variant_modifications", [child.modification], "variant_relationship")
    _upsert_event(
        repaired,
        {
            "timestamp": TIMESTAMP,
            "curator": CURATOR,
            "action": ACTION,
            "changes": "Linked under MEDIUM FOR CARBON MONOXIDE OXIDIZERS",
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
