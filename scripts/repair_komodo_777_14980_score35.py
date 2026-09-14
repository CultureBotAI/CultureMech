#!/usr/bin/env python3
"""Repair empty KOMODO 777_14980 DSM 14980 strain-specific variant."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402
from repair_komodo_777_score30 import (  # noqa: E402
    COMPONENTS as KOMODO_777_COMPONENTS,
)
from repair_komodo_777_score30 import (  # noqa: E402
    DSMZ_777_URL,
    Component,
    _ingredient,
)

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

TARGET = Path("bacterial/medium_777_modified_for_dsm_14980.yaml")
PARENT = "data/normalized_yaml/bacterial/sporomusa_silvacetica_medium.yaml"
EXPECTED_ID = "CultureMech:006434"
EXPECTED_MEDIA_TERM = "komodo.medium:777_14980"

KOMODO_777_14980_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=777_14980"
)
SOURCE = "KOMODO Medium 777_14980"

CURATOR = "repair_komodo_777_14980_score35.py"
ACTION = "RESOLVED_KOMODO_777_14980_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES = (
    "KOMODO Medium 777_14980 records the DSM 14980-specific DSMZ Medium "
    "777 variant with glucose, Na-pyruvate, and 2.98 g/L each of yeast "
    "extract and Casitone."
)

VALUE_OVERRIDES = {
    "K2HPO4": "0.34",
    "KH2PO4": "0.22",
    "NH4Cl": "0.49",
    "MgSO4 x 7 H2O": "0.49",
    "CaCl2 x 2 H2O": "0.25",
    "NaCl": "2.23",
    "FeSO4 x 7 H2O": "0.00198",
    "HCl": "0.000665",
    "FeCl2 x 4 H2O": "0.00148",
    "ZnCl2": "0.0000691",
    "MnCl2 x 4 H2O": "0.0000987",
    "H3BO3": "0.00000592",
    "CoCl2 x 6 H2O": "0.000187",
    "CuCl2 x 2 H2O": "0.00000197",
    "NiCl2 x 6 H2O": "0.0000237",
    "Na2MoO4 x 2 H2O": "0.0000355",
    "NaHSeO3": "0.0000150",
    "Yeast extract": "2.98",
    "Casitone": "2.98",
    "NaHCO3": "1.50",
    "Resazurin": "0.000989",
    "Cysteine-HCl x H2O": "0.30",
    "Na2S x 9 H2O": "0.30",
    "Biotin": "0.0000198",
    "Folic acid": "0.0000198",
    "Pyridoxine-HCl": "0.0000989",
    "Thiamine-HCl x 2 H2O": "0.0000495",
    "Riboflavin": "0.0000495",
    "Nicotinic acid": "0.0000495",
    "D-Ca-pantothenate": "0.0000495",
    "Vitamin B12": "0.000000989",
    "p-Aminobenzoic acid": "0.0000495",
    "Lipoic acid": "0.0000495",
}

BASE_BY_NAME = {component.preferred_term: component for component in KOMODO_777_COMPONENTS}


def _komodo_note(preferred_term: str, value: str) -> str:
    return (
        f"{SOURCE} lists {value} g/L {preferred_term} for the "
        "DSM 14980-specific DSMZ Medium 777 variant."
    )


def _from_parent(preferred_term: str) -> Component:
    value = VALUE_OVERRIDES[preferred_term]
    component = BASE_BY_NAME[preferred_term]
    return replace(
        component,
        value=value,
        unit="G_PER_L",
        source=SOURCE,
        notes=_komodo_note(preferred_term, value),
    )


def _variable(preferred_term: str) -> Component:
    component = BASE_BY_NAME[preferred_term]
    return replace(
        component,
        source=SOURCE,
        notes=f"{SOURCE} lists {preferred_term} without a fixed gram amount.",
    )


COMPONENTS = [
    _from_parent("K2HPO4"),
    _from_parent("KH2PO4"),
    _from_parent("NH4Cl"),
    _from_parent("MgSO4 x 7 H2O"),
    _from_parent("CaCl2 x 2 H2O"),
    _from_parent("NaCl"),
    _from_parent("FeSO4 x 7 H2O"),
    _from_parent("HCl"),
    _from_parent("FeCl2 x 4 H2O"),
    _from_parent("ZnCl2"),
    _from_parent("MnCl2 x 4 H2O"),
    _from_parent("H3BO3"),
    _from_parent("CoCl2 x 6 H2O"),
    _from_parent("CuCl2 x 2 H2O"),
    _from_parent("NiCl2 x 6 H2O"),
    _from_parent("Na2MoO4 x 2 H2O"),
    _from_parent("NaHSeO3"),
    _from_parent("Yeast extract"),
    _from_parent("Casitone"),
    Component(
        "D-Glucose",
        "8.00",
        "G_PER_L",
        ("CHEBI:17634", "D-glucose"),
        SOURCE,
        _komodo_note("D-Glucose", "8.00"),
    ),
    Component(
        "Na-pyruvate",
        "2.00",
        "G_PER_L",
        ("CHEBI:50144", "sodium pyruvate"),
        SOURCE,
        _komodo_note("Na-pyruvate", "2.00"),
    ),
    _from_parent("NaHCO3"),
    _from_parent("Resazurin"),
    _from_parent("Cysteine-HCl x H2O"),
    _from_parent("Na2S x 9 H2O"),
    _from_parent("Biotin"),
    _from_parent("Folic acid"),
    _from_parent("Pyridoxine-HCl"),
    _from_parent("Thiamine-HCl x 2 H2O"),
    _from_parent("Riboflavin"),
    _from_parent("Nicotinic acid"),
    _from_parent("D-Ca-pantothenate"),
    _from_parent("Vitamin B12"),
    _from_parent("p-Aminobenzoic acid"),
    _from_parent("Lipoic acid"),
    _variable("CO2"),
    _variable("N2"),
    replace(
        BASE_BY_NAME["Distilled water"],
        source=f"{SOURCE}/Archived DSMZ Medium 777",
        notes=(
            f"{SOURCE} lists distilled water; archived DSMZ Medium 777 "
            "inherits 1000 mL distilled water from DSMZ Medium 311."
        ),
    ),
]


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(
            f"{TARGET}: expected immutable id {EXPECTED_ID}, " f"found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"{TARGET}: expected source term {EXPECTED_MEDIA_TERM}, " f"found {source_term!r}"
        )

    ingredients = doc.get("ingredients") or []
    repaired_names = {component.preferred_term for component in COMPONENTS}
    ingredient_names = {
        str(row.get("preferred_term") or "") for row in ingredients if isinstance(row, dict)
    }
    if ingredients and ingredient_names != repaired_names:
        raise ValueError(f"{TARGET}: ingredient list drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    while "incomplete_composition" in flags:
        flags.remove("incomplete_composition")

    for flag in ("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    doc["references"] = [
        {"reference": KOMODO_777_14980_URL},
        {"reference": DSMZ_777_URL},
    ]


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": KOMODO_777_14980_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = [_ingredient(component) for component in COMPONENTS]
    repaired["parent_media"] = {
        "path": PARENT,
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": "CultureMech:006435",
        "name": "sporomusa_silvacetica_medium",
    }
    repaired["variant_relationship"] = "STRAIN_SPECIFIC_VARIANT"
    repaired["variant_modifications"] = [
        "KOMODO 777_14980 records glucose and Na-pyruvate in the DSM 14980-specific DSMZ Medium 777 variant.",
    ]
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
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
