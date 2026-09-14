#!/usr/bin/env python3
"""Repair TOGO M2179 / ATCC Medium 2616 Ureaplasma special medium."""

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
TARGET = Path("bacterial/ureaplasma_medium_special_modified_formulation.yaml")
EXPECTED_ID = "CultureMech:008773"
EXPECTED_MEDIA_TERM = "TOGO:M2179"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2179_ureaplasma_special_score15.py"
ACTION = "RESOLVED_TOGO_M2179_UREAPLASMA_SPECIAL_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2179 = "https://togomedium.org/medium/M2179"
ATCC_2616 = "https://www.atcc.org/~/media/C3316A232AD148D5B8FEA1E36C930A1C.ashx"
REFERENCES = (TOGO_M2179, ATCC_2616)
SOURCE = "TOGO M2179 / ATCC Medium 2616"

WATER = "DI Water"
AGAR = "Agar"
PPLO = "PPLO Broth w/o Crystal Violet (BD 255420)"
CASEIN_DIGEST = "Pancreatic Digest of Casein (Hardy C6530)"
GELATIN_DIGEST = "Pancreatic Digest of Gelatin (Hardy C6540)"
CMRL = "10X CMRL 1066 Medium (ATCC 20-2207)"
UREA = "Urea (Sigma U5218)"
FBS = "Fetal Bovine Serum (ATCC 30-2020)"
YEAST_EXTRACT_STOCK = "Yeast Extract Solution"
YEAST_EXTRACT = "Yeast Extract (Hardy C7340)"
TC_YEASTOLATE_STOCK = "TC Yeastolate 10% solution (BD 255772)"
TC_YEASTOLATE = "TC Yeastolate (BD 255772)"
PHENOL_RED_STOCK = "0.1% Phenol Red Solution"
PHENOL_RED = "Phenol Red"
NAOH = "0.1 N NaOH"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Basal Medium", "500", "G_PER_L"),
    (WATER, "805.0", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (PPLO, "3.5", "G_PER_L"),
    (CASEIN_DIGEST, "10", "G_PER_L"),
    (GELATIN_DIGEST, "5", "G_PER_L"),
    (CMRL, "50", "G_PER_L"),
    (UREA, "1", "G_PER_L"),
    ("Fetal Bovine Serum", "170", "G_PER_L"),
    (YEAST_EXTRACT, "15", "G_PER_L"),
    (FBS, "variable", "VARIABLE"),
    (NAOH, "99.9", "PERCENT_W_V"),
    ("Phenol Red powder", "0.1", "PERCENT_W_V"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Additive Solution", "500", "G_PER_L", ()),
    (TC_YEASTOLATE_STOCK, "20", "G_PER_L", ()),
    (YEAST_EXTRACT_STOCK, "35", "G_PER_L", ()),
    ("Phenol Red Solution", "20", "G_PER_L", ()),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (WATER, "705.0", "ML_PER_L"),
    (AGAR, "15.0", "G_PER_L"),
    (PPLO, "3.5", "G_PER_L"),
    (CASEIN_DIGEST, "10.0", "G_PER_L"),
    (GELATIN_DIGEST, "5.0", "G_PER_L"),
    (CMRL, "50.0", "ML_PER_L"),
    (UREA, "1.0", "G_PER_L"),
    (FBS, "170.0", "ML_PER_L"),
)

YEAST_EXTRACT_SIGNATURE: tuple[Component, ...] = (
    (YEAST_EXTRACT, "15.0", "PERCENT_W_V"),
    (WATER, "1000.0", "ML_PER_L"),
)
TC_YEASTOLATE_SIGNATURE: tuple[Component, ...] = (
    (TC_YEASTOLATE, "10.0", "PERCENT_W_V"),
    (WATER, "1000.0", "ML_PER_L"),
)
PHENOL_RED_SIGNATURE: tuple[Component, ...] = (
    (PHENOL_RED, "0.1", "PERCENT_W_V"),
    (NAOH, "200.0", "ML_PER_L"),
    (WATER, "800.0", "ML_PER_L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    (YEAST_EXTRACT_STOCK, "35.0", "ML_PER_L", YEAST_EXTRACT_SIGNATURE),
    (TC_YEASTOLATE_STOCK, "20.0", "ML_PER_L", TC_YEASTOLATE_SIGNATURE),
    (PHENOL_RED_STOCK, "20.0", "ML_PER_L", PHENOL_RED_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    WATER: ("CHEBI:15377", "water"),
    AGAR: ("CHEBI:2509", "agar"),
    UREA: ("CHEBI:16199", "urea"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    PHENOL_RED: ("CHEBI:31991", "phenol red"),
}

PHYSICOCHEMICAL_ROLES = {AGAR: ("SOLIDIFYING_AGENT",)}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

NOTES = (
    "TOGO M2179 cites ATCC Medium 2616 Ureaplasma Medium - Special "
    "Modified Formulation. ATCC Medium 2616 lists a 500 ml basal recipe "
    "with PPLO Broth w/o Crystal Violet, pancreatic digests of casein and "
    "gelatin, optional agar, and DI Water, adjusts the basal pH to 7.4 +/- "
    "0.2, and autoclaves it at 121 C. The source then prepares a 500 ml "
    "additive solution from CMRL 1066, Yeast Extract Solution, 10% TC "
    "Yeastolate, heat-inactivated fetal bovine serum, 0.1% Phenol Red "
    "Solution, urea, and DI Water; filter-sterilizes the additive; combines "
    "it with the basal medium; and records a final pH of 6.0 +/- 0.2."
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
        "notes": notes or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        term = _term(*grounding)
        row["term"] = term
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if roles:
        row["physicochemical_roles"] = list(roles)
    return row


def _stock(
    preferred_term: str,
    value: str,
    composition: tuple[Component, ...],
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
                notes=(
                    f"{SOURCE} identifies {preferred_term} as containing "
                    f"{amount} {UNIT_LABELS[unit]} {component}."
                ),
            )
            for component, amount, unit in composition
        ],
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        WATER,
        "705.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 500 ml/L DI Water in the basal medium and "
            "205 ml/L DI Water in the additive solution."
        ),
    ),
    _component(AGAR, "15.0", "G_PER_L", notes=f"{SOURCE} lists 15 g/L Agar if desired."),
    _component(
        PPLO,
        "3.5",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 3.5 g/L PPLO Broth w/o Crystal Violet from BD "
            "catalog 255420; this commercial broth is retained as an opaque "
            "complex component."
        ),
    ),
    _component(
        CASEIN_DIGEST,
        "10.0",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 10.0 g/L pancreatic digest of casein from Hardy "
            "catalog C6530; the vendor digest is retained as an opaque "
            "complex component."
        ),
    ),
    _component(
        GELATIN_DIGEST,
        "5.0",
        "G_PER_L",
        notes=(
            f"{SOURCE} lists 5.0 g/L pancreatic digest of gelatin from Hardy "
            "catalog C6540; the vendor digest is retained as an opaque "
            "complex component."
        ),
    ),
    _component(
        CMRL,
        "50.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 50 ml/L 10X CMRL 1066 Medium from ATCC "
            "20-2207; this 10x tissue-culture supplement is retained as an "
            "opaque complex component."
        ),
    ),
    _component(
        UREA,
        "1.0",
        "G_PER_L",
        notes=f"{SOURCE} lists 1.0 g/L urea from Sigma U5218.",
    ),
    _component(
        FBS,
        "170.0",
        "ML_PER_L",
        notes=(
            f"{SOURCE} lists 170 ml/L heat-inactivated fetal bovine serum "
            "from ATCC 30-2020; this serum is retained as an opaque complex "
            "component."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        YEAST_EXTRACT_STOCK,
        "35.0",
        YEAST_EXTRACT_SIGNATURE,
        notes=f"{SOURCE} lists 35 ml/L Yeast Extract Solution.",
        preparation_notes=(
            "Dissolve Hardy C7340 yeast extract in DI Water to 15% w/v with "
            "constant stirring, then filter once through a crepe fluted filter."
        ),
    ),
    _stock(
        TC_YEASTOLATE_STOCK,
        "20.0",
        TC_YEASTOLATE_SIGNATURE,
        notes=f"{SOURCE} lists 20 ml/L 10% TC Yeastolate solution from BD 255772.",
        preparation_notes=(
            "Dissolve TC Yeastolate in DI Water to 10% w/v with constant "
            "stirring, then filter once through a crepe fluted filter."
        ),
    ),
    _stock(
        PHENOL_RED_STOCK,
        "20.0",
        PHENOL_RED_SIGNATURE,
        notes=f"{SOURCE} lists 20 ml/L 0.1% Phenol Red Solution.",
        preparation_notes=(
            "Add Phenol Red powder to 0.1 N NaOH to dissolve, then add DI "
            "Water to volume; if needed, add 6 N NaOH dropwise until the "
            "phenol red dissolves."
        ),
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix PPLO Broth w/o Crystal Violet, pancreatic digests of casein "
            "and gelatin, optional agar, and DI Water as the basal medium."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust the basal medium to pH 7.4 +/- 0.2.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": (
            "Autoclave the basal medium at 121 C and, if agar is used, cool "
            "it to 50-55 C in a water bath."
        ),
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": (
            "Combine the additive solution and filter-sterilize it through a "
            "0.22 micrometer filter."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add the filter-sterilized additive solution to the " "basal medium."
        ),
    },
    {
        "step_number": 6,
        "action": "ADJUST_PH",
        "description": "Confirm a final complete-medium pH of 6.0 +/- 0.2 at 25 C.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "notes": (
        "Autoclave the basal medium before adding the separately "
        "filter-sterilized additive solution."
    ),
}


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
        raise ValueError(
            f"{TARGET}: solution signature drifted from "
            f"{IMPORTED_SOLUTION_SIGNATURES!r} to {solution_signatures!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in REFERENCES:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Corrected imported milliliter quantities, split the "
            "ATCC stock recipes out of the flattened ingredient list, and "
            "added ATCC pH and sterilization instructions."
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
    _put_after(repaired, "ph_range", {"min": 5.8, "max": 6.2}, "physical_state")
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    repaired["sterilization"] = copy.deepcopy(STERILIZATION)
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
