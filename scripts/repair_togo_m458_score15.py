#!/usr/bin/env python3
"""Repair TOGO M458 B Medium and its MediaDive J458 duplicate."""

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
TARGET = Path("bacterial/TOGO_M458_B_Medium.yaml")
PARENT = Path("bacterial/b_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009845"
EXPECTED_PARENT_ID = "CultureMech:002807"
EXPECTED_MEDIA_TERM = "TOGO:M458"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J458"

CURATOR = "repair_togo_m458_score15.py"
ACTION = "RESOLVED_TOGO_M458_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_458_B_MEDIUM"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M458 = "https://togomedium.org/medium/M458"
JCM_458 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=458"
MEDIADIVE_J458 = "https://mediadive.dsmz.de/rest/medium/J458"

TOGO_SOURCE = "TOGO M458 / JCM Medium 458"
PARENT_SOURCE = "MediaDive J458 / JCM Medium 458"
TITLE = "B Medium"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "500", "G_PER_L"),
    ("MgSO4・7H2O", "0.05", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("Seawater", "500", "G_PER_L"),
    ("Glucose", "1", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "2", "G_PER_L"),
    ("Bacto peptone (BD-Difco)", "2", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "2", "G_PER_L"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto peptone", "2", "G_PER_L"),
    ("Casamino acids", "2", "G_PER_L"),
    ("Yeast extract", "2", "G_PER_L"),
    ("Glucose", "1", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("MgSO4 x 7 H2O", "0.05", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Sea water", "500", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "500.0", "ML_PER_L"),
    ("MgSO4 x 7H2O", "0.05", "G_PER_L"),
    ("KH2PO4", "0.2", "G_PER_L"),
    ("Seawater", "500.0", "ML_PER_L"),
    ("Glucose", "1.0", "G_PER_L"),
    ("Bacto agar (BD-Difco)", "15.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "2.0", "G_PER_L"),
    ("Bacto peptone (BD-Difco)", "2.0", "G_PER_L"),
    ("Casamino acids (BD-Difco)", "2.0", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Bacto agar (BD-Difco)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

PH_RANGE = {"min": 7.5, "max": 7.8}
REFERENCES = (TOGO_M458, JCM_458, MEDIADIVE_J458)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "b_medium",
    "notes": (
        "TOGO M458 imports the same JCM Medium 458 B Medium formulation "
        "represented by MediaDive J458."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "b_medium",
    "notes": (
        "TOGO M458 imports the same JCM Medium 458 B Medium formulation "
        "represented by MediaDive J458."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same JCM Medium 458 B Medium formulation as the MediaDive J458 source record."
)

RECIPE_NOTES = (
    "JCM Medium 458 B Medium lists, per liter, 500 ml distilled water, "
    "500 ml seawater, 1 g glucose, 0.2 g KH2PO4, 0.05 g MgSO4 x 7H2O, "
    "15 g Bacto agar from BD-Difco, and 2 g each of Bacto peptone, "
    "Casamino acids, and yeast extract from BD-Difco. Adjust pH to 7.5-7.8. "
    "The current JCM GRMD=458 page no longer exposes the recipe, but both "
    "TOGO M458 and MediaDive J458 preserve the JCM formulation."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 7.5-7.8.",
    },
)


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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component("Distilled water", "500.0", "ML_PER_L", source=source),
        _component("MgSO4 x 7H2O", "0.05", "G_PER_L", source=source),
        _component("KH2PO4", "0.2", "G_PER_L", source=source),
        _component(
            "Seawater",
            "500.0",
            "ML_PER_L",
            source=source,
            notes=(
                f"{source} lists 500 ml/L seawater as an undefined mineral "
                "source and solvent."
            ),
        ),
        _component("Glucose", "1.0", "G_PER_L", source=source),
        _component(
            "Bacto agar (BD-Difco)",
            "15.0",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 15.0 g/L Bacto agar from BD-Difco.",
        ),
        _component(
            "Yeast extract (BD-Difco)",
            "2.0",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 2.0 g/L yeast extract from BD-Difco; this "
                "commercial mixture is retained as an opaque complex component."
            ),
        ),
        _component(
            "Bacto peptone (BD-Difco)",
            "2.0",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 2.0 g/L Bacto peptone from BD-Difco; this "
                "peptone is retained as an opaque complex component."
            ),
        ),
        _component(
            "Casamino acids (BD-Difco)",
            "2.0",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 2.0 g/L Casamino acids from BD-Difco; this "
                "amino-acid mixture is retained as an opaque complex component."
            ),
        ),
    ]


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("target ingredient signature drifted")
    if doc.get("solutions"):
        raise ValueError("target solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"expected {EXPECTED_PARENT_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_PARENT_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("parent ingredient signature drifted")
    if doc.get("solutions"):
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


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], *, action: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
        "notes": RECIPE_NOTES,
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


def _ensure_child_link(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    filtered: list[Any] = []
    inserted = False
    for child in children:
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            if not inserted:
                filtered.append(copy.deepcopy(TOGO_CHILD))
                inserted = True
            continue
        filtered.append(child)

    if not inserted:
        filtered.append(copy.deepcopy(TOGO_CHILD))
    doc["variant_children"] = filtered


def _repair_common(
    doc: dict[str, Any],
    *,
    source: str,
    action: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired.pop("ph_value", None)
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    repaired["ingredients"] = _ingredients(source)
    repaired.pop("solutions", None)
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "ingredients")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired, action=action)
    return repaired


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = _repair_common(doc, source=TOGO_SOURCE, action=ACTION)
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [VARIANT_MODIFICATIONS],
        "variant_relationship",
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = _repair_common(doc, source=PARENT_SOURCE, action=PARENT_ACTION)
    _ensure_child_link(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target = normalized / TARGET
    parent = normalized / PARENT
    return {
        target: repair_target(_load(target)),
        parent: repair_parent(_load(parent)),
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
