#!/usr/bin/env python3
"""Repair TOGO M172 Medium 10 Broth."""

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
TARGET = Path("bacterial/TOGO_M172_Medium_10_Broth.yaml")
EXPECTED_ID = "CultureMech:008293"
EXPECTED_MEDIA_TERM = "TOGO:M172"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m172_score15.py"
ACTION = "RESOLVED_TOGO_M172_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M172 = "https://togomedium.org/medium/M172"
TOGO_M124 = "https://togomedium.org/medium/M124"
JCM_179 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=179"
JCM_133 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=133"

SOURCE = "TOGO M172 / JCM Medium 179"
M124_SOURCE = "TOGO M124 / JCM Medium 133"
TITLE = "Medium 10 Broth"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "850", "G_PER_L"),
    ("Cellobiose", "0.5", "G_PER_L"),
    ("Glucose", "0.5", "G_PER_L"),
    ("Soluble starch", "0.5", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.5", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "2", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "850.0", "ML_PER_L"),
    ("Cellobiose", "0.5", "G_PER_L"),
    ("Glucose", "0.5", "G_PER_L"),
    ("Soluble starch", "0.5", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.5", "G_PER_L"),
    ("Trypticase peptone (BD-BBL)", "2.0", "G_PER_L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("0.1% Resazurin solution", "0.5", "G_PER_L", ()),
    ("0.2% Hemin solution", "0.5", "G_PER_L", ()),
    ("4% Na2SO3 solution", "100", "G_PER_L", ()),
    ("25% L--Ascorbic acid solution", "2", "G_PER_L", ()),
    ("5% L--Cysteine\u30fbHCl\u30fbH2O solution", "10", "G_PER_L", ()),
    ("VFA solution (see Medium [M124])", "3.1", "G_PER_L", ()),
    ("Salt solution No. 1 (see Medium [M124])", "37.5", "G_PER_L", ()),
    ("Salt solution No. 2 (see Medium [M124])", "37.5", "G_PER_L", ()),
)

RESAZURIN_SIGNATURE: tuple[Component, ...] = (
    ("Resazurin", "0.1", "PERCENT_W_V"),
)
HEMIN_SIGNATURE: tuple[Component, ...] = (
    ("Hemin", "0.2", "PERCENT_W_V"),
)
SODIUM_SULFITE_SIGNATURE: tuple[Component, ...] = (
    ("Na2SO3", "4.0", "PERCENT_W_V"),
)
ASCORBIC_ACID_SIGNATURE: tuple[Component, ...] = (
    ("L-Ascorbic acid", "25.0", "PERCENT_W_V"),
)
CYSTEINE_SIGNATURE: tuple[Component, ...] = (
    ("L-Cysteine HCl H2O", "5.0", "PERCENT_W_V"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("0.1% Resazurin solution", "0.5", "ML_PER_L", RESAZURIN_SIGNATURE),
    ("0.2% Hemin solution", "0.5", "ML_PER_L", HEMIN_SIGNATURE),
    ("4% Na2SO3 solution", "100.0", "ML_PER_L", SODIUM_SULFITE_SIGNATURE),
    (
        "25% L--Ascorbic acid solution",
        "2.0",
        "ML_PER_L",
        ASCORBIC_ACID_SIGNATURE,
    ),
    (
        "5% L--Cysteine\u30fbHCl\u30fbH2O solution",
        "10.0",
        "ML_PER_L",
        CYSTEINE_SIGNATURE,
    ),
    ("VFA solution (see Medium [M124])", "3.1", "ML_PER_L", ()),
    ("Salt solution No. 1 (see Medium [M124])", "37.5", "ML_PER_L", ()),
    ("Salt solution No. 2 (see Medium [M124])", "37.5", "ML_PER_L", ()),
)

REFERENCES = (TOGO_M172, JCM_179, TOGO_M124, JCM_133)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Cellobiose": ("CHEBI:17057", "cellobiose"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Hemin": ("CHEBI:50385", "hemin"),
    "L-Ascorbic acid": ("CHEBI:29073", "L-Ascorbic acid"),
    "L-Cysteine HCl H2O": ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    "Na2SO3": ("CHEBI:86477", "sodium sulfite"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Soluble starch": ("CHEBI:28017", "starch"),
    "Trypticase peptone (BD-BBL)": ("MICRO:0000175", "Trypticase peptone"),
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
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
    source: str = SOURCE,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _stock(
    preferred_term: str,
    value: str,
    unit: str,
    solute: dict[str, Any] | None,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes or f"{SOURCE} adds {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "composition": [solute] if solute else [],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Distilled water",
        "850.0",
        "ML_PER_L",
        notes=f"{SOURCE} lists 850 ml distilled water.",
    ),
    _component("Cellobiose", "0.5", "G_PER_L"),
    _component("Glucose", "0.5", "G_PER_L"),
    _component("Soluble starch", "0.5", "G_PER_L"),
    _component(
        "Yeast extract (BD-Difco)",
        "0.5",
        "G_PER_L",
        notes=f"{SOURCE} lists 0.5 g/L Yeast extract from BD-Difco.",
    ),
    _component(
        "Trypticase peptone (BD-BBL)",
        "2.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 2 g/L Trypticase peptone from BD-BBL.",
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        "0.1% Resazurin solution",
        "0.5",
        "ML_PER_L",
        _component(
            "Resazurin",
            "0.1",
            "PERCENT_W_V",
            notes=f"{SOURCE} identifies the redox indicator stock as 0.1% Resazurin.",
        ),
    ),
    _stock(
        "0.2% Hemin solution",
        "0.5",
        "ML_PER_L",
        _component(
            "Hemin",
            "0.2",
            "PERCENT_W_V",
            notes=f"{SOURCE} identifies the growth-factor stock as 0.2% Hemin.",
        ),
    ),
    _stock(
        "4% Na2SO3 solution",
        "100.0",
        "ML_PER_L",
        _component(
            "Na2SO3",
            "4.0",
            "PERCENT_W_V",
            notes=f"{SOURCE} identifies the reducing stock as 4% Na2SO3.",
        ),
    ),
    _stock(
        "25% L--Ascorbic acid solution",
        "2.0",
        "ML_PER_L",
        _component(
            "L-Ascorbic acid",
            "25.0",
            "PERCENT_W_V",
            notes=f"{SOURCE} identifies the vitamin stock as 25% L-Ascorbic acid.",
        ),
    ),
    _stock(
        "5% L--Cysteine\u30fbHCl\u30fbH2O solution",
        "10.0",
        "ML_PER_L",
        _component(
            "L-Cysteine HCl H2O",
            "5.0",
            "PERCENT_W_V",
            notes=(
                f"{SOURCE} identifies the cysteine stock as 5% "
                "L-Cysteine HCl H2O."
            ),
        ),
    ),
    _stock(
        "VFA solution (see Medium [M124])",
        "3.1",
        "ML_PER_L",
        None,
        notes=(
            f"{SOURCE} adds 3.1 ml/L VFA solution from Medium 10; "
            f"{M124_SOURCE} defines the source stock."
        ),
    ),
    _stock(
        "Salt solution No. 1 (see Medium [M124])",
        "37.5",
        "ML_PER_L",
        None,
        notes=(
            f"{SOURCE} adds 37.5 ml/L Salt solution No. 1 from Medium 10; "
            f"{M124_SOURCE} defines the source stock."
        ),
    ),
    _stock(
        "Salt solution No. 2 (see Medium [M124])",
        "37.5",
        "ML_PER_L",
        None,
        notes=(
            f"{SOURCE} adds 37.5 ml/L Salt solution No. 2 from Medium 10; "
            f"{M124_SOURCE} defines the source stock."
        ),
    ),
)

PH_RANGE = {"min": 6.7, "max": 6.8}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "ADJUST_PH",
        "description": "Adjust pH to 6.7-6.8.",
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Use Medium 10 from JCM Medium 133 with 0.5 ml/L final 0.2% "
            "hemin solution, and omit agar and Toray silicone solution."
        ),
    },
)

NOTES = (
    "TOGO M172 preserves JCM Medium 179 as Medium 10 Broth. TOGO M172 records "
    "850 ml distilled water, 0.5 g each of cellobiose, glucose, soluble starch, "
    "and Yeast extract from BD-Difco, 2 g Trypticase peptone from BD-BBL, "
    "0.5 ml 0.1% Resazurin solution, 0.5 ml 0.2% Hemin solution, 100 ml 4% "
    "Na2SO3 solution, 2 ml 25% L-Ascorbic acid solution, 10 ml 5% L-Cysteine "
    "HCl H2O solution, and VFA and salt stocks from Medium 10 / TOGO M124, "
    "with pH adjusted to 6.7-6.8. It omits agar and Toray silicone from the "
    "JCM Medium 133 Medium 10 formulation. The current JCM Medium 179 URL no "
    "longer exposes the recipe."
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
    signatures: list[SolutionSignature] = []
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"solution {solution.get('preferred_term')!r} lacks concentration"
            )
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
        raise ValueError(
            f"{TARGET}: solution signatures drifted from "
            f"{IMPORTED_SOLUTION_SIGNATURES!r} to {solution_signatures!r}"
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
            f"{NOTES} Corrected imported ml additions, added the TOGO "
            "pH range and Medium 10 note, represented simple concentration "
            "stocks, and marked the source formula as curated."
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
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
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
