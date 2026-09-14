#!/usr/bin/env python3
"""Repair TOGO M1400 Ureaplasma Medium."""

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
TARGET = Path("bacterial/TOGO_M1400_Ureaplasma_Medium.yaml")
EXPECTED_ID = "CultureMech:007937"
EXPECTED_MEDIA_TERM = "TOGO:M1400"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1400_score15.py"
ACTION = "RESOLVED_TOGO_M1400_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1400 = "https://togomedium.org/medium/M1400"
JCM_1303 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1303"
MEDIADIVE_J1303 = "https://mediadive.dsmz.de/rest/medium/J1303"

SOURCE = "TOGO M1400 / JCM Medium 1303"
TITLE = "Ureaplasma Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "185.0", "G_PER_L"),
    ("PPLO broth w/o Crystal Violet (BD-Difco 255420)", "2.1", "G_PER_L"),
    ("Hipolypepton", "1", "G_PER_L"),
    ("Bovine calf serum (heat-inactivated)", "5", "G_PER_L"),
    ("phenol red", "1", "G_PER_L"),
    ("NaOH", "variable", "VARIABLE"),
    ("Yeast extract", "4", "G_PER_L"),
    ("Urea", "1", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("PPLO broth w/o Crystal Violet (BD-Difco 255420)", "21.0", "G_PER_L"),
    ("Hipolypepton", "10.0", "G_PER_L"),
    ("Distilled water", "850.0", "ML_PER_L"),
)

PHENOL_RED_SIGNATURE: tuple[Component, ...] = (
    ("Phenol red", "1.0", "PERCENT_W_V"),
    ("NaOH", "variable", "VARIABLE"),
)
UREA_YEAST_SIGNATURE: tuple[Component, ...] = (
    ("Urea", "1.0", "PERCENT_W_V"),
    ("Yeast extract", "4.0", "PERCENT_W_V"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1% Phenol red solution (see below)", "200", "G_PER_L", ()),
    ("1% Urea - 4% yeast extract solution (see below)", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1% Phenol red solution", "2.0", "ML_PER_L", PHENOL_RED_SIGNATURE),
    ("Bovine calf serum (heat-inactivated)", "50.0", "ML_PER_L", ()),
    (
        "1% Urea - 4% yeast extract solution",
        "100.0",
        "ML_PER_L",
        UREA_YEAST_SIGNATURE,
    ),
)

REFERENCES = (TOGO_M1400, JCM_1303, MEDIADIVE_J1303)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "Phenol red": ("CHEBI:31991", "phenol red"),
    "Urea": ("CHEBI:16199", "urea"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
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
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _stock_solution(
    preferred_term: str,
    value: str,
    signature: tuple[Component, ...],
    *,
    notes: str,
    preparation_notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "preparation_notes": preparation_notes,
        "composition": [
            _component(
                component,
                amount,
                unit,
                source=SOURCE,
                notes=(
                    "JCM Medium 1303 dissolves phenol red in 10-20 ml of 0.1 N "
                    "NaOH before bringing the stock to 100 ml, so the final "
                    "sodium hydroxide carryover varies with the chosen volume."
                    if component == "NaOH"
                    else None
                ),
            )
            for component, amount, unit in signature
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "PPLO broth w/o Crystal Violet (BD-Difco 255420)",
        "21.0",
        "G_PER_L",
        source=SOURCE,
        notes=(
            "JCM Medium 1303 lists 2.1 g PPLO broth w/o Crystal Violet "
            "(BD-Difco 255420) in the 100 ml final recipe; the catalog broth "
            "is not reducible to one ChEBI molecule."
        ),
        term=False,
    ),
    _component(
        "Hipolypepton",
        "10.0",
        "G_PER_L",
        source=SOURCE,
        notes=(
            "JCM Medium 1303 lists 1.0 g Hipolypepton in the 100 ml final "
            "recipe; this peptone product is intentionally left unmapped."
        ),
        term=False,
    ),
    _component(
        "Distilled water",
        "850.0",
        "ML_PER_L",
        source=SOURCE,
        notes=(
            "JCM Medium 1303 uses 85.0 ml distilled water for the base before "
            "post-autoclave additions."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock_solution(
        "1% Phenol red solution",
        "2.0",
        PHENOL_RED_SIGNATURE,
        notes=(
            "JCM Medium 1303 mixes 200 microliter 1% Phenol red solution into "
            "the 100 ml final recipe."
        ),
        preparation_notes=(
            "Dissolve 1.0 g phenol red in 10-20 ml of 0.1 N NaOH, bring to "
            "100 ml, filter-sterilize, and store at 4 C."
        ),
    ),
    {
        "preferred_term": "Bovine calf serum (heat-inactivated)",
        "concentration": {"value": "50.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 1303 aseptically adds 5.0 ml heat-inactivated bovine "
            "calf serum to the 100 ml final recipe after the autoclaved base "
            "cools to 50-55 C."
        ),
        "preparation_notes": "Filter-sterilize before aseptic addition.",
        "composition": [],
    },
    _stock_solution(
        "1% Urea - 4% yeast extract solution",
        "100.0",
        UREA_YEAST_SIGNATURE,
        notes=(
            "JCM Medium 1303 aseptically adds 10.0 ml 1% Urea - 4% yeast "
            "extract solution to the 100 ml final recipe after the "
            "autoclaved base cools to 50-55 C."
        ),
        preparation_notes=(
            "Dissolve 1.0 g urea and 4.0 g yeast extract in distilled water, "
            "bring to 100 ml, filter-sterilize through a 0.22 micrometer "
            "filter, and store at 4 C."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix PPLO broth w/o Crystal Violet, 1% Phenol red solution, "
            "Hipolypepton, and distilled water at the JCM Medium 1303 ratios."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the base to pH 6.0-6.2.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base at 121 C for 15 min.",
    },
    {
        "step_number": 4,
        "action": "COOL",
        "description": "Cool the autoclaved base to 50-55 C.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add filter-sterilized heat-inactivated bovine calf "
            "serum and 1% Urea - 4% yeast extract solution."
        ),
    },
    {
        "step_number": 6,
        "action": "ALIQUOT",
        "description": (
            "Dispense the completed medium into sterilized plastic tubes, "
            "for example 5 ml medium in 15 ml tubes, and inoculate with "
            "100-200 microliter culture solution before incubation."
        ),
    },
)

NOTES = (
    "TOGO M1400 imports JCM Medium 1303. JCM 1303 records the pH 6.0-6.2 "
    "Ureaplasma base, a 1% phenol-red stock dissolved with 0.1 N NaOH, and "
    "post-autoclave additions of filter-sterilized heat-inactivated bovine "
    "calf serum plus 1% Urea - 4% yeast extract solution. MediaDive J1303 "
    "mirrors the same source but flattens the 100 ml urea/yeast stock "
    "recipe into the main ingredient list; this repair keeps that stock "
    "separate from the final medium."
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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
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
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected the imported stock additions from g/L "
            "artifacts to final ml/L additions and moved the printed stock "
            "recipes under solutions."
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
    _put_after(repaired, "ph_range", {"min": 6.0, "max": 6.2}, "physical_state")
    repaired.pop("ph_value", None)
    _put_after(repaired, "temperature_value", 37.0, "ph_range")
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": (
                "Autoclave the base before cooling to 50-55 C and "
                "aseptically adding filter-sterilized bovine calf serum "
                "and 1% Urea - 4% yeast extract solution."
            ),
        },
        "preparation_steps",
    )
    _put_after(repaired, "culture_vessel", "sterilized 15 ml plastic tubes", "sterilization")
    _put_after(repaired, "notes", NOTES, "media_term")
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
