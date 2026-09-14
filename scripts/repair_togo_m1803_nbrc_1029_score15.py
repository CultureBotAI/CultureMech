#!/usr/bin/env python3
"""Repair TOGO M1803 / NBRC Medium 1029 Alkaline yeast extract-malt extract agar."""

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
TARGET = Path("bacterial/alkaline_yeast_extract_malt_extract_agar.yaml")
EXPECTED_ID = "CultureMech:008373"
EXPECTED_MEDIA_TERM = "TOGO:M1803"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1803_nbrc_1029_score15.py"
ACTION = "RESOLVED_TOGO_M1803_NBRC_1029"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1803 = "https://togomedium.org/medium/M1803"
NBRC_1029 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1029"
REFERENCES = (TOGO_M1803, NBRC_1029)
SOURCE = "TOGO M1803 / NBRC Medium 1029"
TITLE = "Alkaline yeast extract-malt extract agar"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto Malt Extract (Difco)", "10", "G_PER_L"),
    ("Artificial seawater", "1", "G_PER_L"),
    ("Glucose", "4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Bacto Yeast Extract (Difco)", "4", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto Yeast Extract (Difco)", "4.0", "G_PER_L"),
    ("Bacto Malt Extract (Difco)", "10.0", "G_PER_L"),
    ("Glucose", "4.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Artificial seawater", "1000.0", "ML_PER_L"),
)

NA2CO3_SIGNATURE: tuple[Component, ...] = (("Na2CO3", "10.0", "PERCENT_W_V"),)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Na2CO3 solution", "variable", "VARIABLE", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("10% Na2CO3 solution", "variable", "VARIABLE", NA2CO3_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Bacto Malt Extract (Difco)": ("FOODON:03301056", "malt extract"),
    "Bacto Yeast Extract (Difco)": ("FOODON:03315426", "yeast extract"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "NBRC Medium 1029 defines Alkaline yeast extract-malt extract agar with "
    "4 g Bacto Yeast Extract (Difco), 10 g Bacto Malt Extract (Difco), "
    "4 g glucose, 15 g agar, and 1 L artificial seawater, then adjusts the "
    "autoclaved medium to pH 10.0 with sterilized 10% Na2CO3 solution."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix Bacto Yeast Extract (Difco), Bacto Malt Extract (Difco), "
            "glucose, and agar in artificial seawater."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the basal medium.",
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "After autoclaving, adjust pH to 10.0 with sterilized 10% " "Na2CO3 solution."
        ),
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "notes": (
        "Autoclave the basal medium and sterilize the 10% Na2CO3 solution "
        "separately before pH adjustment."
    ),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str = SOURCE,
    notes: str | None = None,
    nutritional_roles: tuple[str, ...] = (),
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)

    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _ingredients() -> list[dict[str, Any]]:
    return [
        _component(
            "Bacto Yeast Extract (Difco)",
            "4.0",
            "G_PER_L",
            notes=f"{SOURCE} lists 4 g/L Bacto Yeast Extract (Difco).",
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            "Bacto Malt Extract (Difco)",
            "10.0",
            "G_PER_L",
            notes=f"{SOURCE} lists 10 g/L Bacto Malt Extract (Difco).",
            nutritional_roles=("CARBON_SOURCE", "NITROGEN_SOURCE"),
        ),
        _component(
            "Glucose",
            "4.0",
            "G_PER_L",
            nutritional_roles=("CARBON_SOURCE",),
        ),
        _component(
            "Agar",
            "15.0",
            "G_PER_L",
            physicochemical_roles=("SOLIDIFYING_AGENT",),
        ),
        {
            "preferred_term": "Artificial seawater",
            "concentration": {"value": "1000.0", "unit": "ML_PER_L"},
            "source": SOURCE,
            "notes": (
                "NBRC Medium 1029 lists 1 L artificial seawater per liter; "
                "the artificial seawater mixture is retained without a "
                "single-compound ontology grounding."
            ),
        },
    ]


def _na2co3_solution() -> dict[str, Any]:
    na2co3 = _component(
        "Na2CO3",
        "10.0",
        "PERCENT_W_V",
        notes=(
            "NBRC Medium 1029 specifies the pH-adjusting sodium carbonate " "solution as 10% w/v."
        ),
        physicochemical_roles=("BUFFER",),
    )

    return {
        "preferred_term": "10% Na2CO3 solution",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 1029 uses sterilized 10% Na2CO3 solution to adjust "
            "the autoclaved medium to pH 10.0; the final addition volume is "
            "not specified."
        ),
        "term": _term(*GROUNDINGS["Na2CO3"]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS["Na2CO3"]),
        "composition": [na2co3],
        "preparation_notes": "Sterilize the 10% Na2CO3 solution before pH adjustment.",
    }


INGREDIENTS: tuple[dict[str, Any], ...] = tuple(_ingredients())
SOLUTIONS: tuple[dict[str, Any], ...] = (_na2co3_solution(),)


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
        raise ValueError(f"{TARGET}: ingredient signature drifted")

    solution_signature = _solution_signatures(doc)
    if solution_signature not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError(f"{TARGET}: solution signature drifted")


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
            "Verified TOGO M1803 against NBRC Medium 1029, corrected the "
            "imported artificial-seawater row from 1 g/L to 1000 ml/L, "
            "grounded the Bacto yeast extract, Bacto malt extract, glucose, "
            "agar, and 10% Na2CO3 solution, added pH 10.0, removed the stale "
            "MediaDive 7 match, and kept Artificial seawater as an "
            "intentionally unmapped input."
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
    repaired.pop("ph_range", None)
    _put_after(repaired, "ph_value", 10.0, "physical_state")
    repaired.pop("kg_microbe_match", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [copy.deepcopy(step) for step in PREPARATION_STEPS],
        "notes",
    )
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _ensure_references(repaired)
    _ensure_flags(repaired)
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
