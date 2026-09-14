#!/usr/bin/env python3
"""Repair TOGO M2226 / ATCC Medium 247 PPLO broth."""

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
    "pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml"
)
EXPECTED_ID = "CultureMech:008814"
EXPECTED_MEDIA_TERM = "TOGO:M2226"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2226_pplo_horse_yeast_score15.py"
ACTION = "RESOLVED_TOGO_M2226_PPLO_HORSE_YEAST_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2226 = "https://togomedium.org/medium/M2226"
TOGO_M2226_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2226"
ATCC_247 = "https://www.atcc.org/~/media/AD2BC56A0BA94572A40803C02D24D35A.ashx"
REFERENCES = (TOGO_M2226, TOGO_M2226_API, ATCC_247)
SOURCE = "TOGO M2226 / ATCC Medium 247"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "700", "G_PER_L"),
    ("Horse Serum (not inactivated)", "200", "G_PER_L"),
    ("PPLO Broth w/o CV", "21", "G_PER_L"),
    ("Fresh Baker’s Yeast Extract", "100", "G_PER_L"),
)

PRIOR_REPAIR_SIGNATURE: tuple[Component, ...] = (
    ("PPLO Broth w/o CV (Mycoplasma Broth) (BD 255420, pH 7.8)", "21.0", "G_PER_L"),
    ("Distilled water", "700.0", "ML_PER_L"),
    ("Horse Serum (not inactivated)", "200.0", "ML_PER_L"),
    ("Fresh Baker’s Yeast Extract (GIBCO 18180)", "100.0", "ML_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("PPLO broth", "21.0", "G_PER_L"),
    ("Distilled water", "700.0", "ML_PER_L"),
    ("Horse serum", "200.0", "ML_PER_L"),
    ("Fresh Baker’s Yeast Extract (GIBCO 18180)", "100.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Horse serum": ("MICRO:0001235", "Horse serum"),
    "Fresh Baker’s Yeast Extract (GIBCO 18180)": ("FOODON:03315426", "Yeast extract"),
}

NOTES = (
    "TOGO M2226 cites ATCC Medium 247. ATCC Medium 247 lists PPLO broth without "
    "CV at pH 7.8 as 21.0 g PPLO Broth w/o CV from BD catalog 255420, 200.0 ml "
    "non-inactivated horse serum, 100.0 ml Fresh Baker’s Yeast Extract from "
    "GIBCO 18180, and 700.0 ml distilled water. The horse serum and yeast extract "
    "are added aseptically to a sterile PPLO broth and water basal medium."
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
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "PPLO broth",
        "21.0",
        "G_PER_L",
        (
            "ATCC Medium 247 lists 21.0 g PPLO Broth w/o CV from BD catalog "
            "255420, with the commercial product itself specified at pH 7.8; this "
            "catalog broth is retained as an opaque complex component."
        ),
    ),
    _component(
        "Distilled water",
        "700.0",
        "ML_PER_L",
        "ATCC Medium 247 lists 700.0 ml distilled water.",
    ),
    _component(
        "Horse serum",
        "200.0",
        "ML_PER_L",
        (
            "ATCC Medium 247 lists 200.0 ml horse serum and specifies that it is "
            "not inactivated; this serum is retained as an opaque complex "
            "component."
        ),
    ),
    _component(
        "Fresh Baker’s Yeast Extract (GIBCO 18180)",
        "100.0",
        "ML_PER_L",
        (
            "ATCC Medium 247 lists 100.0 ml Fresh Baker’s Yeast Extract from "
            "GIBCO 18180; the broad FOODON Yeast extract term captures the "
            "disclosed extract class, and the source does not disclose the stock "
            "concentration."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare sterile basal medium containing PPLO Broth w/o CV and "
            "distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Aseptically add horse serum and Fresh Baker’s Yeast Extract "
            "(GIBCO 18180)."
        ),
    },
)


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    doc.pop(key, None)
    reordered: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        reordered[existing_key] = existing_value
        if existing_key == after:
            reordered[key] = value
            inserted = True
    if not inserted:
        reordered[key] = value
    doc.clear()
    doc.update(reordered)


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        return ()
    if not isinstance(rows, list):
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

    pair = (
        _signature(doc.get("ingredients"), "ingredients"),
        _signature(doc.get("solutions"), "solutions"),
    )
    allowed = (
        (IMPORTED_INGREDIENT_SIGNATURE, ()),
        (PRIOR_REPAIR_SIGNATURE, ()),
        (FINAL_INGREDIENT_SIGNATURE, ()),
    )
    if pair not in allowed:
        raise ValueError(f"{TARGET}: recipe signature drifted to {pair!r}")


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
            f"{NOTES} Corrected the imported ml/L rows, added the source pH, "
            "grounded water, horse serum, and yeast extract, and kept the ATCC "
            "PPLO broth unmapped as an opaque complex input."
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
    _put_after(repaired, "ph_value", 7.8, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired.pop("solutions", None)
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
