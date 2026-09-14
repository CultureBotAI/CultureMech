#!/usr/bin/env python3
"""Repair TOGO M1733 Modified 802 (pH 10.0)."""

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
TARGET = Path("bacterial/modified_802_ph_10_0.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:008297"
EXPECTED_MEDIA_TERM = "TOGO:M1733"

CURATOR = "repair_togo_m1733_modified_802_score15.py"
ACTION = "RESOLVED_TOGO_M1733_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1733 = "https://togomedium.org/medium/M1733"
NBRC_942 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=942"
SOURCE = "TOGO M1733 / NBRC Medium 942"
TITLE = "Modified 802 (pH 10.0)"
MGSO4_HEPTAHYDRATE = "MgSO4\u00b77H2O"
PH_VALUE = 10.0

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "900", "G_PER_L"),
    (MGSO4_HEPTAHYDRATE, "1", "G_PER_L"),
    ("Yeast extract", "2", "G_PER_L"),
    ("K2HPO4", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3 solution", "100", "G_PER_L"),
    ("Hipolypepton*", "10", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3 solution", "100.0", "ML_PER_L"),
    ("Distilled water", "900.0", "ML_PER_L"),
    (MGSO4_HEPTAHYDRATE, "1.0", "G_PER_L"),
    ("Yeast extract", "2.0", "G_PER_L"),
    ("K2HPO4", "1.0", "G_PER_L"),
    ("Agar (if needed)", "15.0", "G_PER_L"),
    ("Hipolypepton*", "10.0", "G_PER_L"),
)

REFERENCES = (TOGO_M1733, NBRC_942)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Na2CO3 solution": ("CHEBI:29377", "sodium carbonate"),
    "Distilled water": ("CHEBI:15377", "water"),
    MGSO4_HEPTAHYDRATE: ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Hipolypepton*": ("FOODON:03315306", "Polypeptone"),
}

MEDIAINGREDIENT_CHEBI = frozenset(
    {
        "Na2CO3 solution",
        "Distilled water",
        MGSO4_HEPTAHYDRATE,
        "K2HPO4",
        "Agar (if needed)",
    }
)

NOTES = (
    "TOGO M1733 imports NBRC Medium 942 as Modified 802 (pH 10.0). The NBRC "
    "formula lists 100 ml of 10% Na2CO3 solution, 900 ml distilled water, "
    "1 g MgSO4 x 7H2O, 2 g yeast extract, 1 g K2HPO4, 15 g agar if needed, "
    "10 g Hipolypepton, and a final pH near 10.0."
)

INGREDIENT_NOTES = {
    "Na2CO3 solution": (
        "TOGO M1733 / NBRC Medium 942 lists 100 ml/L of 10% Na2CO3 solution, "
        "added aseptically after autoclaving."
    ),
    "Distilled water": ("TOGO M1733 / NBRC Medium 942 lists 900 ml/L Distilled water."),
    MGSO4_HEPTAHYDRATE: ("TOGO M1733 / NBRC Medium 942 lists 1 g/L MgSO4 x 7H2O."),
    "Yeast extract": "TOGO M1733 / NBRC Medium 942 lists 2 g/L Yeast extract.",
    "K2HPO4": "TOGO M1733 / NBRC Medium 942 lists 1 g/L K2HPO4.",
    "Agar (if needed)": ("TOGO M1733 / NBRC Medium 942 lists 15 g/L Agar if needed."),
    "Hipolypepton*": (
        "TOGO M1733 / NBRC Medium 942 lists 10 g/L Hipolypepton with an "
        "asterisked Wako Pure Chemical Industries note."
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": INGREDIENT_NOTES[preferred_term],
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if preferred_term in MEDIAINGREDIENT_CHEBI:
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(
    _component(*component) for component in FINAL_INGREDIENT_SIGNATURE
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
    solution_signature = _signature(doc.get("solutions"), "solutions")
    if ingredient_signature == FINAL_INGREDIENT_SIGNATURE and not solution_signature:
        return
    if (
        ingredient_signature != IMPORTED_INGREDIENT_SIGNATURE
        or solution_signature != IMPORTED_SOLUTION_SIGNATURE
    ):
        raise ValueError(f"{TARGET}: ingredient or solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
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
            f"{NOTES} Corrected the imported water and Na2CO3 solution units, "
            "restored Hipolypepton as an ingredient, removed empty solution "
            "stubs, added the source pH, and grounded every ingredient."
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
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired.pop("preparation_steps", None)
    repaired.pop("sterilization", None)
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
