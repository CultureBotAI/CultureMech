#!/usr/bin/env python3
"""Repair TOGO M2361 YE/10 + Ca Medium."""

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
TARGET = Path("bacterial/TOGO_M2361_YE_10_Ca_Medium.yaml")
DSMZ_PARENT = Path("bacterial/ye_10_ca_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008947"
EXPECTED_PARENT_ID = "CultureMech:000929"
EXPECTED_MEDIA_TERM = "TOGO:M2361"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:1463"

CURATOR = "repair_togo_m2361_score15.py"
ACTION = "RESOLVED_TOGO_M2361_SCORE15"
LINK_ACTION = "LINKED_TOGO_M2361_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2361 = "https://togomedium.org/medium/M2361"
DSMZ_1463 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1463.pdf"

SOURCE = "TOGO M2361 / DSMZ Medium 1463"
PH_VALUE = 7.5
REFERENCES = (TOGO_M2361, DSMZ_1463)

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1000", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.3", "G_PER_L"),
    ("TRIS x HCl", "0.61", "G_PER_L"),
    ("Yeast extract (Difco)", "0.3", "G_PER_L"),
    ("Peptone", "0.06", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract (Difco)", "0.30", "G_PER_L"),
    ("Peptone", "0.06", "G_PER_L"),
    ("TRIS x HCl", "0.61", "G_PER_L"),
    ("CaCl2 x 2 H2O", "0.30", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{DSMZ_PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "ye_10_ca_medium",
    "notes": (
        "TOGO M2361 imports DSMZ Medium 1463 and exactly matches its YE/10 + "
        "Ca Medium formula, with the source distilled-water row retained."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "ye_10_ca_medium",
    "notes": (
        "TOGO M2361 imports DSMZ Medium 1463 and explicitly retains its "
        "distilled-water row."
    ),
}

VARIANT_MODIFICATION = (
    "Same ingredient and concentration signature as DSMZ Medium 1463; TOGO "
    "M2361 explicitly retains the source distilled-water row."
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Peptone": ("MICRO:0000178", "Peptone"),
    "TRIS x HCl": ("CHEBI:9754", "tris"),
    "Yeast extract (Difco)": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Add all components except calcium chloride.",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave the medium; add calcium chloride from a sterilized stock "
            "solution after the autoclaved medium has cooled."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Adjust final pH to 7.5.",
    },
)

NOTES = (
    "TOGO M2361 imports DSMZ Medium 1463, YE/10 + Ca Medium. DSMZ Medium 1463 "
    "lists, per liter, 0.30 g Yeast extract (Difco), 0.06 g Peptone, 0.61 g "
    "Tris-HCl buffer, 0.30 g CaCl2 x 2 H2O, and 1000 ml Distilled water. "
    "Adjust final pH to 7.5."
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
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"DSMZ Medium 1463 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Yeast extract (Difco)",
        "0.30",
        "G_PER_L",
        notes="DSMZ Medium 1463 lists 0.30 g/L Yeast extract (Difco).",
    ),
    _component("Peptone", "0.06", "G_PER_L"),
    _component(
        "TRIS x HCl",
        "0.61",
        "G_PER_L",
        notes="DSMZ Medium 1463 lists 0.61 g/L Tris-HCl buffer.",
    ),
    _component(
        "CaCl2 x 2 H2O",
        "0.30",
        "G_PER_L",
        notes=(
            "DSMZ Medium 1463 lists 0.30 g/L CaCl2 x 2 H2O, added from a "
            "sterilized stock solution after autoclaving."
        ),
    ),
    _component(
        "Distilled water",
        "1.0",
        "L",
        notes="DSMZ Medium 1463 lists 1000 ml Distilled water.",
    ),
)


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


def _component_signature(rows: Any, label: str) -> tuple[Component, ...]:
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
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _component_signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{TARGET}: solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(
            f"{DSMZ_PARENT}: expected id {EXPECTED_PARENT_ID}, "
            f"found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(
            f"{DSMZ_PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}"
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


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
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


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(
        repaired,
        action=ACTION,
        source="; ".join(REFERENCES),
        notes=(
            f"{NOTES} Corrected the imported water unit artifact, grounded all "
            "disclosed components, recorded pH 7.5 and the calcium chloride "
            "stock-addition preparation, and linked the record as a DSMZ "
            "Medium 1463 source duplicate."
        ),
    )
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [VARIANT_MODIFICATION]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        source="; ".join(REFERENCES),
        notes="Linked TOGO M2361 as a source duplicate of DSMZ Medium 1463.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    parent_path = normalized / DSMZ_PARENT
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
