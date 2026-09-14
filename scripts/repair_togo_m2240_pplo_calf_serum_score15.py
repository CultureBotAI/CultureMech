#!/usr/bin/env python3
"""Repair TOGO M2240 PPLO/calf-serum Mycoplasma medium."""

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
TARGET = Path(
    "bacterial/"
    "medium_containing_pplo_broth_calf_serum_glucose_penicillin_g_and_tris_hc1.yaml"
)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008829"
EXPECTED_MEDIA_TERM = "TOGO:M2240"

CURATOR = "repair_togo_m2240_pplo_calf_serum_score15.py"
ACTION = "RESOLVED_TOGO_M2240_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2240 = "https://togomedium.org/medium/M2240"
SOURCE = "TOGO M2240"
TITLE = "Medium containing PPLO broth, calf serum, glucose, penicillin G, and Tris-HC1"
PH_VALUE = 7.6

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tris-HC1 (pH 7.6)", "50", "MILLIMOLAR"),
    ("Glucose", "0.2", "G_PER_L"),
    ("Calf serum (Gibco)", "1", "G_PER_L"),
    ("PPLO broth (Difco)", "2.2", "G_PER_L"),
    ("Penicillin G", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Tris-HC1 (pH 7.6)", "50.0", "MILLIMOLAR"),
    ("Glucose", "0.2", "PERCENT_W_V"),
    ("Calf serum (Gibco)", "1.0", "PERCENT_V_V"),
    ("PPLO broth (Difco)", "2.2", "PERCENT_W_V"),
    ("Penicillin G", "variable", "VARIABLE"),
)

REFERENCES = (TOGO_M2240,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Glucose": ("CHEBI:17234", "glucose"),
    "Penicillin G": ("CHEBI:51765", "benzylpenicillin sodium"),
}

NOTES = (
    "TOGO M2240 reports a 24 h, 37 C Mycoplasma capricolum ATCC 27343 "
    "growth medium containing 2.2% w/v PPLO broth from Difco, 1% v/v calf "
    "serum from Gibco, 0.2% w/v glucose, 400 units(U)/ml Penicillin G, and "
    "50 mM Tris-HC1 at pH 7.6. The TOGO metadata also records pH 7.6."
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
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if preferred_term == "Glucose":
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Tris-HC1 (pH 7.6)",
        "50.0",
        "MILLIMOLAR",
        notes=(
            "TOGO M2240 lists 50 mM Tris-HC1 (pH 7.6); this pH-specific "
            "buffer is retained without a single-molecule ontology grounding."
        ),
    ),
    _component(
        "Glucose",
        "0.2",
        "PERCENT_W_V",
        notes="TOGO M2240 lists 0.2% w/v Glucose.",
    ),
    _component(
        "Calf serum (Gibco)",
        "1.0",
        "PERCENT_V_V",
        notes=(
            "TOGO M2240 lists 1% v/v Calf serum from Gibco; this liquid "
            "serum is retained as an opaque complex component."
        ),
    ),
    _component(
        "PPLO broth (Difco)",
        "2.2",
        "PERCENT_W_V",
        notes=(
            "TOGO M2240 lists 2.2% w/v PPLO broth from Difco; the "
            "commercial broth is not reducible to one ChEBI molecule."
        ),
    ),
    _component(
        "Penicillin G",
        "variable",
        "VARIABLE",
        notes=(
            "TOGO M2240 lists 400 units(U)/ml Penicillin G, which is "
            "retained as a variable concentration because the schema has no "
            "unit for activity units."
        ),
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
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    kg_match = doc.get("kg_microbe_match")
    if kg_match not in (None, "mediadive.medium:21"):
        raise ValueError(f"{TARGET}: unexpected kg_microbe_match {kg_match!r}")


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
            f"{NOTES} Corrected the imported percent-concentration units, "
            "added the source pH, kept the disclosed opaque products "
            "unmapped, retained Penicillin G as an activity-unit amount, and "
            "removed kg_microbe_match mediadive.medium:21 because MediaDive "
            "medium 21 is Sarcina Medium."
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
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
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
