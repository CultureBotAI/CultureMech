#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 170 Yeast Extract - Skim Milk Medium."""

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

BACTERIAL = "bacterial/yeast_extract_skim_milk_medium.yaml"
FUNGAL = "fungal/yeast_extract_skim_milk_medium.yaml"

EXPECTED_IDS = {
    BACTERIAL: "CultureMech:004197",
    FUNGAL: "CultureMech:010459",
}

EXPECTED_SOURCE_TERMS = {
    BACTERIAL: "komodo.medium:170",
    FUNGAL: "mediadive.medium:170",
}

DSMZ_170_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium170.pdf"
MEDIADIVE_170 = "https://mediadive.dsmz.de/medium/170"
MEDIADIVE_170_REST = "https://mediadive.dsmz.de/rest/medium/170"
REFERENCES = (DSMZ_170_PDF, MEDIADIVE_170, MEDIADIVE_170_REST)

SOURCE = "DSMZ Medium 170"
TITLE = "Yeast extract - SKIM MILK medium"
CURATOR = "repair_dsmz_170_yeast_extract_skim_milk_score15.py"
ACTION = "RESOLVED_DSMZ_170_YEAST_EXTRACT_SKIM_MILK_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Skim milk", "10", "G_PER_L"),
    ("Yeast extract", "1", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Skim milk (Difco)", "10.0", "G_PER_L"),
    ("Yeast extract", "1.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

NOTES = (
    "DSMZ Medium 170 defines Yeast Extract - Skim Milk Medium as "
    "10.0 g Difco skim milk, 1.0 g yeast extract, 15.0 g agar, and "
    "1000.0 ml distilled water."
)


@dataclass(frozen=True)
class Target:
    path: str
    original_name: str


TARGETS = (
    Target(BACTERIAL, TITLE),
    Target(FUNGAL, TITLE.upper()),
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    notes: str,
    term: tuple[str, str] | None = None,
    *,
    physicochemical_roles: tuple[str, ...] = (),
    nutritional_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Skim milk (Difco)",
        "10.0",
        "G_PER_L",
        (
            "DSMZ Medium 170 lists 10.0 g/L Skim milk from Difco; the "
            "commercial milk product is retained as an opaque component."
        ),
    ),
    _ingredient(
        "Yeast extract",
        "1.0",
        "G_PER_L",
        "DSMZ Medium 170 lists 1.0 g/L Yeast extract.",
        ("FOODON:03315426", "yeast extract"),
        nutritional_roles=("PROTEIN_SOURCE",),
    ),
    _ingredient(
        "Agar",
        "15.0",
        "G_PER_L",
        "DSMZ Medium 170 lists 15.0 g/L Agar.",
        ("CHEBI:2509", "agar"),
        physicochemical_roles=("SOLIDIFYING_AGENT",),
    ),
    _ingredient(
        "Distilled water",
        "1000.0",
        "ML_PER_L",
        "DSMZ Medium 170 lists 1000.0 ml distilled water.",
        ("CHEBI:15377", "water"),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix 10.0 g Skim milk (Difco), 1.0 g yeast extract, 15.0 g "
            "agar, and 1000.0 ml distilled water."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    expected_id = EXPECTED_IDS[target.path]
    if doc.get("id") != expected_id:
        raise ValueError(f"{target.path}: expected id {expected_id}")

    expected_source = EXPECTED_SOURCE_TERMS[target.path]
    source_term = _source_term_id(doc)
    if source_term != expected_source:
        raise ValueError(
            f"{target.path}: expected source term {expected_source}, "
            f"found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(f"{target.path}: ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Added the explicit water row, grounded yeast extract, "
            "agar, and water, and retained Difco skim milk as an opaque "
            "commercial product. Removed a false kg_microbe_match to "
            "DSMZ Medium 12 / Soil Extract Medium."
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["original_name"] = target.original_name
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    repaired.pop("kg_microbe_match", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
    return plans


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
        print(f"{status} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
