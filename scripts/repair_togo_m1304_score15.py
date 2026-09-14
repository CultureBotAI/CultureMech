#!/usr/bin/env python3
"""Repair TOGO M1304 BSW3 Agar."""

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
TARGET = Path("bacterial/TOGO_M1304_BSW3_Agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1304_score15.py"
ACTION = "RESOLVED_TOGO_M1304_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

RECORD_ID = "CultureMech:007839"
MEDIA_TERM = "TOGO:M1304"

TOGO_M1304 = "https://togomedium.org/medium/M1304"
MEDIADIVE_J1216 = "https://mediadive.dsmz.de/rest/medium/J1216"
SOURCE = "MediaDive J1216"

Component = tuple[str, str, str]
Term = tuple[str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Malt extract (BD-Difco)", "1", "G_PER_L"),
    ("0.1 x Artificial seawater", "1", "G_PER_L"),
    ("Glucose", "0.4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.4", "G_PER_L"),
)

GLUCOSE = ("CHEBI:17234", "glucose")
AGAR = ("CHEBI:2509", "agar")


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
        "Yeast extract (BD-Difco)",
        "0.4",
        "G_PER_L",
        SOURCE,
        (
            "MediaDive J1216 lists 0.4 g/L Yeast extract with the BD-Difco "
            "attribute; the product is source-disclosed but not reducible "
            "to one ChEBI molecule."
        ),
    ),
    Ingredient(
        "Malt extract (BD-Difco)",
        "1",
        "G_PER_L",
        SOURCE,
        (
            "MediaDive J1216 lists 1 g/L Malt extract with the BD-Difco "
            "attribute; the product is source-disclosed but not reducible "
            "to one ChEBI molecule."
        ),
    ),
    Ingredient(
        "Glucose",
        "0.4",
        "G_PER_L",
        SOURCE,
        "MediaDive J1216 lists 0.4 g/L glucose.",
        GLUCOSE,
    ),
    Ingredient(
        "Agar",
        "15",
        "G_PER_L",
        SOURCE,
        "MediaDive J1216 lists 15 g/L agar as the solidifying component.",
        AGAR,
    ),
    Ingredient(
        "0.1 x Artificial seawater",
        "1000",
        "ML_PER_L",
        SOURCE,
        "MediaDive J1216 lists 1000 ml/L artificial 0.1x Sea water.",
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
    kg_match = doc.get("kg_microbe_match")
    if kg_match not in (None, "mediadive.medium:7"):
        raise ValueError(f"{TARGET}: unexpected kg_microbe_match {kg_match!r}")


def _component(spec: Ingredient) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": spec.preferred_term,
        "concentration": {"value": spec.value, "unit": spec.unit},
        "source": spec.source,
        "notes": spec.notes,
    }
    if spec.term is not None:
        row["term"] = _term(*spec.term)
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
            "description": "Adjust BSW3 Agar to pH 7.3.",
        }
    ]


def _notes() -> str:
    return (
        "MediaDive J1216 records JCM-sourced BSW3 Agar with 0.4 g/L yeast "
        "extract, 1 g/L malt extract, 0.4 g/L glucose, 15 g/L agar, 1 L "
        "artificial 0.1x sea water, and pH 7.3."
    )


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
        TOGO_M1304,
        MEDIADIVE_J1216,
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
            f"{_notes()} Removed kg_microbe_match mediadive.medium:7 because "
            "MediaDive medium 7 is Ancylobacter-Spirosoma Medium, not BSW3 Agar."
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
    _put_after(repaired, "ph_value", 7.3, "physical_state")
    repaired["ingredients"] = [_component(row) for row in REPAIRED_INGREDIENTS]
    _put_after(repaired, "preparation_steps", _preparation_steps(), "ingredients")
    _put_after(repaired, "notes", _notes(), "media_term")
    repaired.pop("kg_microbe_match", None)
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
