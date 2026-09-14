#!/usr/bin/env python3
"""Repair TOGO M94 Nutrient Agar with 25% Soil Extract."""

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
TARGET = Path("bacterial/TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:010373"
EXPECTED_MEDIA_TERM = "TOGO:M94"
CURATOR = "repair_togo_m94_soil_extract_score15.py"
ACTION = "RESOLVED_TOGO_M94_SOIL_EXTRACT"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M94 = "https://togomedium.org/medium/M94"
JCM_102 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=102"
SOURCE = "TOGO M94 / JCM Medium 102"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tap water", "751.0", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Beef extract", "3", "G_PER_L"),
    ("Peptone", "5", "G_PER_L"),
    ("Soil extract (see below)", "250", "G_PER_L"),
    ("air-dried garden soil", "400", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Peptone", "5.0", "G_PER_L"),
    ("Beef extract", "3.0", "G_PER_L"),
    ("Tap water", "750.0", "ML_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
)

SOIL_EXTRACT_COMPOSITION: tuple[Component, ...] = (
    ("Air-dried garden soil", "400.0", "G_PER_L"),
    ("Tap water", "1.0", "L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Soil extract", "250.0", "ML_PER_L", SOIL_EXTRACT_COMPOSITION),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Beef extract": ("FOODON:03302088", "Beef extract"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "Tap water": ("CHEBI:15377", "water"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Beef extract": ("PROTEIN_SOURCE",),
    "Peptone": ("PROTEIN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
}

RECIPE_NOTES = (
    "JCM Medium 102 Nutrient Agar with 25% Soil Extract lists, per liter, "
    "5.0 g Peptone, 3.0 g Beef extract, 250 ml Soil extract, 15.0 g Agar, "
    "and 750 ml Tap water, with final pH adjusted to 7.0. Soil extract is "
    "prepared by suspending 400 g air-dried garden soil in 1.0 L tap water, "
    "autoclaving at 121 C for 1 hr, then using the clear supernatant after "
    "a few hours of sedimentation and centrifugation."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Suspend 400 g air-dried garden soil in 1.0 L tap water and "
            "autoclave at 121 C for 1 hr to prepare Soil extract."
        ),
    },
    {
        "step_number": 2,
        "action": "FILTER",
        "description": (
            "Let the soil slurry sediment for a few hours, then centrifuge "
            "and use the clear supernatant as Soil extract."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "Prepare the main liter with 5.0 g Peptone, 3.0 g Beef extract, "
            "250 ml Soil extract, 15.0 g Agar, and 750 ml Tap water."
        ),
    },
    {
        "step_number": 4,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "1 hr",
    "notes": "JCM Medium 102 autoclaves the soil slurry at 121 C for 1 hr.",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _ingredients() -> list[dict[str, Any]]:
    return [_component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE]


def _soil_extract() -> dict[str, Any]:
    return {
        "preferred_term": "Soil extract",
        "concentration": {"value": "250.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": f"{SOURCE} adds 250 ml/L Soil extract to the main liter.",
        "preparation_notes": (
            "Suspend 400 g air-dried garden soil in 1.0 L tap water and "
            "autoclave at 121 C for 1 hr. Use the clear supernatant after "
            "sedimentation for a few hours and centrifugation."
        ),
        "composition": [
            _component(
                "Air-dried garden soil",
                "400.0",
                "G_PER_L",
                notes=(
                    f"{SOURCE} prepares Soil extract from 400 g air-dried "
                    "garden soil in 1.0 L Tap water."
                ),
                term=False,
            ),
            _component(
                "Tap water",
                "1.0",
                "L",
                notes=f"{SOURCE} prepares Soil extract with 1.0 L Tap water.",
            ),
        ],
    }


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


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
            )
        )
    return tuple(signatures)


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
        raise ValueError(f"expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"expected media term {EXPECTED_MEDIA_TERM}, " f"found {_source_term_id(doc)!r}"
        )
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("target ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("target solution signature drifted")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

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


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (TOGO_M94, JCM_102):
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{TOGO_M94}; {JCM_102}",
        "notes": (
            "Corrected the imported water merge and ml-to-g/L artifacts, "
            "moved Soil extract to a 250 ml/L nested solution, added pH 7.0, "
            "and grounded Peptone and Beef extract to complex-source terms."
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


def repair_togo_m94(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired["ingredients"] = _ingredients()
    _put_after(repaired, "solutions", [_soil_extract()], "ingredients")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "solutions")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_togo_m94(_load(path))}


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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
