#!/usr/bin/env python3
"""Repair TOGO M2840 YPG medium."""

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
TARGET = Path("bacterial/TOGO_M2840_YPG_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009382"
EXPECTED_MEDIA_TERM = "TOGO:M2840"

CURATOR = "repair_togo_m2840_score15.py"
ACTION = "RESOLVED_TOGO_M2840_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M2840 = "https://togomedium.org/medium/M2840"
PMID = "PMID:19638423"
DOI = "doi:10.1093/nar/gkp612"
SOURCE = "TOGO M2840 / Azuma et al. 2009"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("yeast extract", "1", "PERCENT_W_V"),
    ("glycerol", "2", "PERCENT_W_V"),
    ("polypeptone", "1", "PERCENT_W_V"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "1.0", "PERCENT_W_V"),
    ("Polypeptone", "1.0", "PERCENT_W_V"),
    ("Glycerol", "2.0", "PERCENT_W_V"),
)

REFERENCES = (TOGO_M2840, PMID, DOI)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "Polypeptone": ("FOODON:03315306", "Polypeptone"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

COMPONENT_NOTES: dict[str, str] = {
    "Glycerol": "TOGO M2840 lists 2.0% glycerol.",
    "Polypeptone": "TOGO M2840 lists 1.0% polypeptone.",
    "Yeast extract": "TOGO M2840 lists 1.0% yeast extract.",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "DISSOLVE",
        "description": (
            "Dissolve 1.0% yeast extract, 1.0% polypeptone, and "
            "2.0% glycerol to prepare YPG medium."
        ),
    },
)

NOTES = (
    "TOGO M2840 records the YPG medium that Azuma et al. used to grow "
    "Acetobacter pasteurianus IFO 3283 and Gluconacetobacter xylinus "
    "NBRC 3288 routinely at 30 C; the formulation is 1.0% yeast extract, "
    "1.0% polypeptone, and 2.0% glycerol."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    identifier, label = GROUNDINGS[preferred_term]
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": COMPONENT_NOTES[preferred_term],
        "term": _term(identifier, label),
    }
    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(identifier, label)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(name, value, unit) for name, value, unit in FINAL_INGREDIENT_SIGNATURE
)


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
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    kg_match = doc.get("kg_microbe_match")
    if kg_match not in (None, "mediadive.medium:780"):
        raise ValueError(f"{TARGET}: unexpected kg_microbe_match {kg_match!r}")


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
            f"{NOTES} Grounded all three source ingredients and removed "
            "kg_microbe_match mediadive.medium:780 because MediaDive medium 780 "
            "is Middlebrook Medium with Mycobactin, not YPG medium."
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


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("sterilization", None)
    repaired.pop("kg_microbe_match", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_target(_load(path))}


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
