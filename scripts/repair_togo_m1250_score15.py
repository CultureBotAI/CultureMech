#!/usr/bin/env python3
"""Repair TOGO M1250 LB agar with kanamycin and rifampicin."""

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
TARGET = Path("bacterial/TOGO_M1250_LB_Luria-Bertani_Agar_With_Kanamycin_And_Rifampicin.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1250_score15.py"
ACTION = "RESOLVED_TOGO_M1250_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:007781"
MEDIA_TERM = "TOGO:M1250"

TOGO_M1250 = "https://togomedium.org/medium/M1250"
MEDIADIVE_J1168 = "https://mediadive.dsmz.de/rest/medium/J1168"
SOURCE = "MediaDive J1168"

Component = tuple[str, str, str]
Term = tuple[str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("NaCl", "10", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "5", "G_PER_L"),
    ("Tryptone (BD-Difco)", "10", "G_PER_L"),
    ("Kanamycin sulfate (dissolved in distilled water)", "50", "G_PER_L"),
    ("Rifampicin (dissolved in methanol)", "25", "G_PER_L"),
)

NACL = ("CHEBI:26710", "sodium chloride")
AGAR = ("CHEBI:2509", "agar")
WATER = ("CHEBI:15377", "water")
KANAMYCIN_SULFATE = ("CHEBI:6109", "kanamycin A sulfate")
RIFAMPICIN = ("CHEBI:28077", "rifampicin")


@dataclass(frozen=True)
class Ingredient:
    preferred_term: str
    value: str
    unit: str
    source: str
    notes: str
    term: Term | None = None


REPAIRED_INGREDIENTS: tuple[Ingredient, ...] = (
    Ingredient(
        "Tryptone (BD-Difco)",
        "10",
        "G_PER_L",
        SOURCE,
        (
            "MediaDive J1168 lists 10 g/L Tryptone with the BD-Difco "
            "attribute; the product is source-disclosed but not reducible "
            "to one ChEBI molecule."
        ),
    ),
    Ingredient(
        "Yeast extract (BD-Difco)",
        "5",
        "G_PER_L",
        SOURCE,
        (
            "MediaDive J1168 lists 5 g/L Yeast extract with the BD-Difco "
            "attribute; the product is source-disclosed but not reducible "
            "to one ChEBI molecule."
        ),
    ),
    Ingredient(
        "NaCl",
        "10",
        "G_PER_L",
        SOURCE,
        "MediaDive J1168 lists 10 g/L sodium chloride.",
        NACL,
    ),
    Ingredient(
        "Agar",
        "15",
        "G_PER_L",
        SOURCE,
        "MediaDive J1168 lists 15 g/L agar as the solidifying component.",
        AGAR,
    ),
    Ingredient(
        "Distilled water",
        "1000",
        "ML_PER_L",
        SOURCE,
        "MediaDive J1168 lists 1000 ml distilled water in the 1 L main solution.",
        WATER,
    ),
    Ingredient(
        "Kanamycin sulfate",
        "0.05",
        "G_PER_L",
        SOURCE,
        (
            "MediaDive J1168 lists 50 mg Kanamycin sulfate, dissolved in "
            "distilled water and filter-sterilized before aseptic post-autoclave "
            "addition; 50 mg/L equals 0.05 g/L."
        ),
        KANAMYCIN_SULFATE,
    ),
    Ingredient(
        "Rifampicin",
        "0.025",
        "G_PER_L",
        SOURCE,
        (
            "MediaDive J1168 lists 25 mg Rifampicin, dissolved in methanol "
            "and filter-sterilized before aseptic post-autoclave addition; "
            "25 mg/L equals 0.025 g/L."
        ),
        RIFAMPICIN,
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: Any) -> tuple[Component, ...]:
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _repaired_signature() -> tuple[Component, ...]:
    return tuple((row.preferred_term, row.value, row.unit) for row in REPAIRED_INGREDIENTS)


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != RECORD_ID:
        raise ValueError(f"{TARGET}: expected id {RECORD_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {MEDIA_TERM}")

    signature = _signature(doc.get("ingredients"))
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, _repaired_signature()):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: unexpected solutions")


def _component(spec: Ingredient) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": spec.preferred_term,
        "concentration": {"value": spec.value, "unit": spec.unit},
        "source": spec.source,
        "notes": spec.notes,
    }
    if spec.term is not None:
        row["term"] = _term(*spec.term)
        if spec.term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*spec.term)
    return row


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        del doc[key]

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _preparation_steps() -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust the LB agar base to pH 7.0 before autoclaving.",
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": (
                "After autoclaving, aseptically add the kanamycin sulfate and "
                "rifampicin antibiotics as filter-sterilized stocks."
            ),
        },
    ]


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _references() -> tuple[str, ...]:
    return (
        TOGO_M1250,
        MEDIADIVE_J1168,
    )


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references():
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(_references()),
        "notes": (
            "MediaDive J1168 records pH 7.0 LB agar with 10 g/L Tryptone "
            "(BD-Difco), 5 g/L Yeast extract (BD-Difco), 10 g/L NaCl, "
            "15 g/L agar, and filter-sterilized post-autoclave additions of "
            "50 mg/L kanamycin sulfate and 25 mg/L rifampicin."
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
    repaired["composition_type"] = "SEMI_DEFINED"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired["ingredients"] = [_component(row) for row in REPAIRED_INGREDIENTS]
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", _preparation_steps(), "ingredients")
    _ensure_flags(repaired)
    _ensure_references(repaired)
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
