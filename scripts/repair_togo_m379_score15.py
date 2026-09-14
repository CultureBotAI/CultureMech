#!/usr/bin/env python3
"""Repair TOGO M379 Glycerol-Soil Medium and its JCM J384 duplicate."""

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
TARGET = Path("bacterial/TOGO_M379_Glycerol-Soil_Medium.yaml")
PARENT = Path("bacterial/JCM_J384_GLYCEROL-SOIL_MEDIUM.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009760"
EXPECTED_PARENT_ID = "CultureMech:002741"
EXPECTED_MEDIA_TERM = "TOGO:M379"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J384"

CURATOR = "repair_togo_m379_score15.py"
ACTION = "RESOLVED_TOGO_M379_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_384_SOIL_EXTRACT"
LINK_ACTION = "LINKED_TOGO_M379_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M379 = "https://togomedium.org/medium/M379"
MEDIADIVE_J384 = "https://mediadive.dsmz.de/medium/J384"
JCM_384 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=384"

TOGO_SOURCE = "TOGO M379 / JCM Medium 384"
PARENT_SOURCE = "MediaDive J384 / JCM Medium 384"
TITLE = "Glycerol-Soil Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Glycerol", "20", "G_PER_L"),
    ("Tap water", "1810.0", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Bacto peptone (BD-Difco)", "5", "G_PER_L"),
    ("Beef extract (BD-Difco)", "3", "G_PER_L"),
    ("Soil extract (See below)", "150", "G_PER_L"),
    ("air--dried garden soil", "400", "G_PER_L"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto peptone", "5", "G_PER_L"),
    ("Beef extract", "3", "G_PER_L"),
    ("Glycerol", "20", "G_PER_L"),
    ("Soil extract", "150", "G_PER_L"),
    ("Tap water", "850", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto peptone (BD-Difco)", "5.0", "G_PER_L"),
    ("Beef extract (BD-Difco)", "3.0", "G_PER_L"),
    ("Glycerol", "20.0", "G_PER_L"),
    ("Tap water", "850.0", "ML_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
)

SOIL_EXTRACT_SIGNATURE: tuple[Component, ...] = (
    ("Tap water", "960.0", "ML_PER_L"),
    ("Air-dried garden soil", "400.0", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Soil extract", "150.0", "ML_PER_L", SOIL_EXTRACT_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "Tap water": ("CHEBI:15377", "water"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

TARGET_REFERENCES = (TOGO_M379, MEDIADIVE_J384)
PARENT_REFERENCES = (MEDIADIVE_J384, JCM_384)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "glycerol_soil_medium",
    "notes": (
        "TOGO M379 imports the same JCM Medium 384 Glycerol-Soil "
        "Medium formulation represented by MediaDive J384."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "glycerol_soil_medium",
    "notes": (
        "TOGO M379 imports the same JCM Medium 384 Glycerol-Soil "
        "Medium formulation represented by MediaDive J384."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same JCM Medium 384 Glycerol-Soil Medium formulation as the "
    "MediaDive J384 source record."
)

RECIPE_NOTES = (
    "JCM Medium 384 Glycerol-Soil Medium lists, per liter, 5.0 g "
    "Bacto peptone (BD-Difco), 3.0 g Beef extract (BD-Difco), "
    "20.0 g Glycerol, 150 ml Soil extract, 850 ml Tap water, and "
    "15.0 g Agar. The final pH is 7.0. Soil extract is prepared by "
    "autoclaving 400 g air-dried garden soil in 960 ml tap water "
    "at 121 C for 1 hr, cooling and settling the slurry, decanting "
    "and paper-filtering the supernatant, then autoclaving and "
    "storing it at room temperature until cleared by sedimentation."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Suspend 400 g air-dried garden soil in 960 ml tap water "
            "and autoclave at 121 C for 1 hr to prepare Soil extract."
        ),
    },
    {
        "step_number": 2,
        "action": "FILTER",
        "description": (
            "After the soil slurry is cooled and settled, decant the "
            "supernatant and filter it through paper."
        ),
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave the filtered Soil extract and store it at room "
            "temperature until cleared by sedimentation."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Prepare the main liter with Bacto peptone, Beef extract, "
            "Glycerol, 150 ml Soil extract, 850 ml Tap water, and Agar."
        ),
    },
    {
        "step_number": 5,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.0.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "1 hr",
    "notes": (
        "The soil slurry is autoclaved at 121 C for 1 hr; the "
        "decanted and paper-filtered supernatant is autoclaved again "
        "before room-temperature storage."
    ),
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
    source: str,
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for preferred_term, value, unit in FINAL_INGREDIENT_SIGNATURE:
        rows.append(
            _component(
                preferred_term,
                value,
                unit,
                source=source,
                term=preferred_term
                not in {"Bacto peptone (BD-Difco)", "Beef extract (BD-Difco)"},
            )
        )
    return rows


def _soil_extract(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "Soil extract",
        "concentration": {"value": "150.0", "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds 150 ml/L Soil extract to the main liter.",
        "preparation_notes": (
            "Suspend 400 g air-dried garden soil in 960 ml tap water and "
            "autoclave at 121 C for 1 hr. Cool, settle, decant the "
            "supernatant, filter it through paper, autoclave it again, "
            "and store it at room temperature until cleared by sedimentation."
        ),
        "composition": [
            _component(
                "Tap water",
                "960.0",
                "ML_PER_L",
                source=source,
                notes=(
                    f"{source} prepares Soil extract from 960 ml Tap water "
                    "with 400 g air-dried garden soil."
                ),
            ),
            _component(
                "Air-dried garden soil",
                "400.0",
                "G_PER_L",
                source=source,
                notes=(
                    f"{source} prepares Soil extract from 400 g "
                    "air-dried garden soil in 960 ml Tap water."
                ),
                term=False,
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
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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
            f"expected media term {EXPECTED_MEDIA_TERM}, "
            f"found {_source_term_id(doc)!r}"
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


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"expected {EXPECTED_PARENT_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(
            f"expected media term {EXPECTED_PARENT_MEDIA_TERM}, "
            f"found {_source_term_id(doc)!r}"
        )
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("parent ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("parent solution signature drifted")


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
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in references_to_add:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            children[index] = copy.deepcopy(TOGO_CHILD)
            return
    children.append(copy.deepcopy(TOGO_CHILD))


def _repair_recipe(
    doc: dict[str, Any],
    *,
    source: str,
    references: tuple[str, ...],
    action: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    repaired["ingredients"] = _ingredients(source)
    repaired["solutions"] = [_soil_extract(source)]
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_curation_event(
        repaired,
        action=action,
        references=references,
        notes=(
            f"{RECIPE_NOTES} Corrected the imported water merge and ml-to-g/L "
            "artifacts, moved Soil extract to a 150 ml/L nested solution, "
            "and retained source-disclosed Bacto peptone and Beef extract "
            "as intentionally ungrounded products."
        ),
    )
    return repaired


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = _repair_recipe(
        doc,
        source=TOGO_SOURCE,
        references=TARGET_REFERENCES,
        action=ACTION,
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = _repair_recipe(
        doc,
        source=PARENT_SOURCE,
        references=PARENT_REFERENCES,
        action=PARENT_ACTION,
    )
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        references=TARGET_REFERENCES,
        notes="Linked TOGO M379 as a same-source duplicate of MediaDive J384.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / PARENT
    return {
        target_path: repair_target(_load(target_path)),
        parent_path: repair_parent(_load(parent_path)),
    }


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
