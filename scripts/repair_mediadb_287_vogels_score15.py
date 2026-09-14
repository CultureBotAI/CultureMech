#!/usr/bin/env python3
"""Repair MediaDB 287 / Vogels Medium N."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/vogels_medium_n.yaml")
EXPECTED_ID = "CultureMech:007187"
EXPECTED_MEDIA_TERM = "MEDIADB:287"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_mediadb_287_vogels_score15.py"
ACTION = "RESOLVED_MEDIADB_287_VOGELS_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

MEDIA = "https://mediadb.systemsbiology.net/defined_media/media/287/"
MEDIA_TEXT = "https://mediadb.systemsbiology.net/defined_media/media_text/287/"
SOURCE_VOGEL = "https://mediadb.systemsbiology.net/defined_media/sources/98/"
GROWTH = "https://mediadb.systemsbiology.net/defined_media/growthdata/605/"
ORGANISM = "https://mediadb.systemsbiology.net/defined_media/organisms/141/"
VOGEL_ARTICLE = "http://www.jstor.org/stable/2459146"

SOURCE = "MediaDB Medium 287 Vogels medium n"

ORTHOPHOSPHATE = "Orthophosphate"
SULFATE = "Sulfate"
SUCROSE = "Sucrose"
BIOTIN = "Biotin"
CITRATE = "Citrate"
POTASSIUM = "Potassium"
NITRATE = "Nitrate"
MAGNESIUM = "Magnesium"
CHLORIDE = "Cl-"
SODIUM = "Sodium"
AMMONIUM = "NH4+"
IRON_II = "Fe2+"

Component = tuple[str, str, str]

INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (ORTHOPHOSPHATE, "2600.0", "MILLIMOLAR"),
    (SULFATE, "104.1", "MILLIMOLAR"),
    (SUCROSE, "29.21", "MILLIMOLAR"),
    (BIOTIN, "0.00103", "MILLIMOLAR"),
    (CITRATE, "660.0", "MILLIMOLAR"),
    (POTASSIUM, "6390.0", "MILLIMOLAR"),
    (NITRATE, "1610.0", "MILLIMOLAR"),
    (MAGNESIUM, "411.44", "MILLIMOLAR"),
    (CHLORIDE, "141.03", "MILLIMOLAR"),
    (SODIUM, "2170.0", "MILLIMOLAR"),
    (AMMONIUM, "5540.0", "MILLIMOLAR"),
    (IRON_II, "0.01791", "MILLIMOLAR"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    ORTHOPHOSPHATE: ("CHEBI:18367", "phosphate(3-)"),
    SULFATE: ("CHEBI:16189", "sulfate"),
    SUCROSE: ("CHEBI:17992", "sucrose"),
    BIOTIN: ("CHEBI:15956", "biotin"),
    CITRATE: ("CHEBI:16947", "citrate(3-)"),
    POTASSIUM: ("CHEBI:29103", "potassium(1+)"),
    NITRATE: ("CHEBI:17632", "nitrate"),
    MAGNESIUM: ("CHEBI:18420", "magnesium(2+)"),
    CHLORIDE: ("CHEBI:17996", "chloride"),
    SODIUM: ("CHEBI:29101", "sodium(1+)"),
    AMMONIUM: ("CHEBI:28938", "ammonium"),
    IRON_II: ("CHEBI:29033", "iron(2+)"),
}

REFERENCES = (MEDIA, MEDIA_TEXT, SOURCE_VOGEL, GROWTH, ORGANISM, VOGEL_ARTICLE)

NOTES = (
    "MediaDB Medium 287 lists Vogels medium n as a 12-component, mM-scale "
    "defined formulation for Neurospora crassa OR74A and links Vogel et al. "
    "1964 as its source. The linked MediaDB growth-data record reports pH "
    "5.8 and 25 C."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(name: str, value: str, unit: str) -> dict[str, Any]:
    identifier, label = GROUNDINGS[name]
    term = _term(identifier, label)
    return {
        "preferred_term": name,
        "term": copy.deepcopy(term),
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": f"{SOURCE} lists {value} mM {name}.",
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            inserted = True
    if not inserted:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature != INGREDIENT_SIGNATURE:
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{INGREDIENT_SIGNATURE!r} to {signature!r}"
        )


def _target_organisms() -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "Neurospora crassa OR74A",
            "term": {
                "id": "NCBITaxon:5141",
                "label": "Neurospora crassa",
            },
            "strain": "OR74A",
            "evidence": [
                {
                    "reference": MEDIA,
                    "supports": "SUPPORT",
                    "explanation": (
                        "MediaDB Medium 287 lists Neurospora crassa OR74A as "
                        "an organism for Vogels medium n."
                    ),
                },
                {
                    "reference": GROWTH,
                    "supports": "SUPPORT",
                    "explanation": (
                        "MediaDB growth-data record 605 reports Neurospora "
                        "crassa OR74A on Vogels medium n at pH 5.8 and 25 C."
                    ),
                },
            ],
        }
    ]


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Grounded all 12 mM components from MediaDB Medium 287, added "
            "the MediaDB pH 5.8 and 25 C growth conditions, and curated the "
            "Neurospora crassa OR74A organism-medium relationship."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
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
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 5.8, "physical_state")
    _put_after(repaired, "temperature_value", 25.0, "ph_value")
    repaired["ingredients"] = [
        _component(name, value, unit) for name, value, unit in INGREDIENT_SIGNATURE
    ]
    repaired.pop("preparation_steps", None)
    _put_after(repaired, "organism_culture_type", "isolate", "curation_history")
    _put_after(repaired, "target_organisms", _target_organisms(), "organism_culture_type")
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_references(repaired)
    _ensure_flags(repaired)
    _append_curation_event(repaired)
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
