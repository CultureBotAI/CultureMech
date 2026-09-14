#!/usr/bin/env python3
"""Repair TOGO M2252 artificial seawater with thiosulfate."""

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
TARGET = Path("bacterial/artificial_seawater_base_with_thiosulfate_as_the_electron_donor.yaml")
EXPECTED_ID = "CultureMech:008841"
EXPECTED_MEDIA_TERM = "TOGO:M2252"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2252_artificial_seawater_thiosulfate_score15.py"
ACTION = "RESOLVED_TOGO_M2252_ARTIFICIAL_SEAWATER_THIOSULFATE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2252 = "https://togomedium.org/medium/M2252"
WILLIAMS_2006 = "https://pmc.ncbi.nlm.nih.gov/articles/PMC1392968/"
REFERENCES = (TOGO_M2252, WILLIAMS_2006)

SOURCE = "TOGO M2252"
TITLE = "Artificial seawater base with thiosulfate as the electron donor"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Artificial seawater", "1", "G_PER_L"),
    ("thiosulfate", "10", "MILLIMOLAR"),
    ("O2", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Artificial seawater", "1000.0", "ML_PER_L"),
    ("thiosulfate", "10.0", "MILLIMOLAR"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Oxygen gas": ("CHEBI:15379", "dioxygen"),
    "thiosulfate": ("CHEBI:26977", "thiosulfate"),
}

UNIT_LABELS = {
    "MILLIMOLAR": "mM",
    "ML_PER_L": "ml/L",
    "VARIABLE": "variable",
}

NOTES = (
    "TOGO M2252 reports a liquid artificial seawater base with 10 mM "
    "thiosulfate as the electron donor for microaerobic strain MC-1 growth. "
    "Its comments cite PMID:16461683 for the cultivation context and state "
    "that cultures were incubated statically under an O2 gradient at 25 C in "
    "the dark."
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
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        row["term"] = _term(*GROUNDINGS[preferred_term])
        row["mediaingredientmech_chebi_term"] = _term(*GROUNDINGS[preferred_term])
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Artificial seawater",
        "1000.0",
        "ML_PER_L",
        notes=(
            "TOGO M2252 lists 1 L Artificial seawater as the base; this "
            "artificial seawater mixture is retained without a single-compound "
            "ontology grounding."
        ),
        term=False,
    ),
    _component(
        "thiosulfate",
        "10.0",
        "MILLIMOLAR",
        notes="TOGO M2252 lists 10 mM thiosulfate as the electron donor.",
    ),
    _component(
        "Oxygen gas",
        "variable",
        "VARIABLE",
        notes=(
            "TOGO M2252 lists O2 and states that cultures were incubated "
            "statically under an O2 gradient."
        ),
    ),
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

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")


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
    if "references" not in doc:
        _put_after(doc, "references", [], "notes")

    references = doc["references"]
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Corrected Artificial seawater from TOGO's imported 1 g/L row to "
            "a 1000.0 ml/L base, grounded thiosulfate and O2, added the "
            "25 C static O2-gradient incubation condition, and retained "
            "Artificial seawater as intentionally unmapped."
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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "temperature_value", 25.0, "physical_state")
    _put_after(repaired, "aeration", "static O2 gradient", "temperature_value")
    _put_after(repaired, "incubation_atmosphere", "MICROAEROPHILIC", "aeration")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
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
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
