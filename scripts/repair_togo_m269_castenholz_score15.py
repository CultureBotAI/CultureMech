#!/usr/bin/env python3
"""Repair TOGO M269 JCM Castenholz Medium."""

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
TARGET = Path("bacterial/TOGO_M269_Castenholz_Medium.yaml")
PARENT = Path("bacterial/JCM_J276_CASTENHOLZ_MEDIUM.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009252"
EXPECTED_MEDIA_TERM = "TOGO:M269"
EXPECTED_PARENT_ID = "CultureMech:002633"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J276"

CURATOR = "repair_togo_m269_castenholz_score15.py"
ACTION = "RESOLVED_TOGO_M269_CASTENHOLZ_SCORE15"
LINK_ACTION = "LINKED_TOGO_M269_JCM276_SOURCE_DUPLICATE"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M269 = "https://togomedium.org/medium/M269"
JCM_276 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=276"
JCM_273 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=273"

SOURCE = "TOGO M269 / JCM Medium 276"
REFERENCES = (TOGO_M269, JCM_276, JCM_273)

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "900", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1", "G_PER_L"),
    ("Tryptone (BD-Difco)", "1", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Castenholz basal salt solution (see Medium [M266])", "100", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tryptone (BD-Difco)", "1.0", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Distilled water", "900.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Castenholz basal salt solution (see Medium No. 273)", "100.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Tryptone (BD-Difco)": ("MICRO:0000182", "tryptone"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
}

NOTES = (
    "TOGO M269 imports JCM Medium 276 Castenholz Medium. JCM Medium 276 "
    "lists 1.0 g Tryptone, 1.0 g Yeast extract, 100.0 ml Castenholz basal "
    "salt solution from JCM Medium 273, and 900.0 ml Distilled water, then "
    "adjusts pH to 8.2 with NaOH."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 8.2 with NaOH.",
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 minutes.",
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str, notes: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Tryptone (BD-Difco)",
        "1.0",
        "G_PER_L",
        "JCM Medium 276 lists 1.0 g/L Tryptone from BD-Difco.",
    ),
    _component(
        "Yeast extract (BD-Difco)",
        "1.0",
        "G_PER_L",
        "JCM Medium 276 lists 1.0 g/L Yeast extract from BD-Difco.",
    ),
    _component(
        "Distilled water",
        "900.0",
        "ML_PER_L",
        "JCM Medium 276 lists 900.0 ml/L Distilled water.",
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Castenholz basal salt solution (see Medium No. 273)",
        "concentration": {"value": "100.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 276 adds 100.0 ml/L Castenholz basal salt solution from " "JCM Medium 273."
        ),
        "culturemech_term": {
            "id": "CultureMech:013022",
            "label": "Castenholz basal salt solution",
        },
    },
)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signatures = (
        _signature(doc.get("ingredients"), "ingredients"),
        _signature(doc.get("solutions"), "solutions"),
    )
    expected = (
        (IMPORTED_INGREDIENT_SIGNATURE, IMPORTED_SOLUTION_SIGNATURE),
        (FINAL_INGREDIENT_SIGNATURE, FINAL_SOLUTION_SIGNATURE),
    )
    if signatures not in expected:
        raise ValueError(
            f"{TARGET}: ingredient/solution signature drifted from "
            f"{expected!r} to {signatures!r}"
        )


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {EXPECTED_PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {EXPECTED_PARENT_MEDIA_TERM}")


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
    for flag in ("has_ontology_mappings", "ingredients_curated"):
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


def _parent_media() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT}",
        "relationship": "SOURCE_DUPLICATE",
        "id": EXPECTED_PARENT_ID,
        "name": "castenholz_medium",
        "notes": "TOGO M269 imports JCM Medium 276 and retains its basal-salt stock reference.",
    }


def _variant_child() -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{TARGET}",
        "relationship": "SOURCE_DUPLICATE",
        "id": EXPECTED_ID,
        "name": "castenholz_medium",
        "notes": "TOGO M269 is a source duplicate of JCM Medium 276.",
    }


def _ensure_variant_child(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    child_ref = _variant_child()
    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == child_ref["path"]:
            children[index] = child_ref
            return
    children.append(child_ref)


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 8.2, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
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
            f"{NOTES} Corrected the imported water and basal-salt solution "
            "unit artifacts, removed NaOH from the ingredient list because it "
            "is only the pH titrant, grounded yeast extract and tryptone, and "
            "linked the record to its existing JCM Medium 276 source duplicate."
        ),
    )
    repaired["parent_media"] = _parent_media()
    repaired["variant_relationship"] = "SOURCE_DUPLICATE"
    repaired["variant_modifications"] = [
        "Same JCM Medium 276 formulation, with the basal-salt stock retained as a linked solution.",
    ]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        source="; ".join((TOGO_M269, JCM_276, JCM_273)),
        notes="Linked TOGO M269 as a source duplicate of JCM Medium 276.",
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
