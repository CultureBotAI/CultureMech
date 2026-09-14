#!/usr/bin/env python3
"""Repair TOGO M1385 Natroniella Medium For ANB-PHB2."""

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
TARGET = Path("bacterial/TOGO_M1385_Natroniella_Medium_For_ANB-PHB2.yaml")
EXPECTED_ID = "CultureMech:007919"
EXPECTED_MEDIA_TERM = "TOGO:M1385"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1385_score15.py"
ACTION = "RESOLVED_TOGO_M1385_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1385 = "https://togomedium.org/medium/M1385"
MEDIADIVE_J1289 = "https://mediadive.dsmz.de/rest/medium/J1289"

SOURCE = "TOGO M1385 / MediaDive J1289"
TITLE = "Natroniella Medium For ANB-PHB2"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("NaCl", "18", "G_PER_L"),
    ("K2HPO4", "1", "G_PER_L"),
    ("NaHCO3", "40", "G_PER_L"),
    ("Na2CO3", "64", "G_PER_L"),
    ("HCl", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3", "64.0", "G_PER_L"),
    ("NaHCO3", "40.0", "G_PER_L"),
    ("NaCl", "18.0", "G_PER_L"),
    ("K2HPO4", "1.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
    ("HCl", "variable", "VARIABLE"),
    ("Ar", "variable", "VARIABLE"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1 N NH4Cl solution", "4", "G_PER_L", ()),
    ("1 M MgCl2 solution", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M1148])", "1", "G_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "1", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "1", "G_PER_L", ()),
    ("1.0% Yeast extract solution", "2", "G_PER_L", ()),
    ("5% Na2S\u30fb9H2O solution", "2.5", "G_PER_L", ()),
    ("2.0 M Sodium crotonate solution*", "10", "G_PER_L", ()),
    ("0.1% Sodium dithionite solution (in 1 M NaHCO3)*", "2", "G_PER_L", ()),
)

NH4CL_STOCK_SIGNATURE: tuple[Component, ...] = (("NH4Cl", "1.0", "MOLAR"),)
MGCL2_STOCK_SIGNATURE: tuple[Component, ...] = (("MgCl2", "1.0", "MOLAR"),)
TRACE_ELEMENT_SIGNATURE: tuple[Component, ...] = (
    ("EDTA", "5.0", "G_PER_L"),
    ("FeSO4 x 7H2O", "2.0", "G_PER_L"),
    ("ZnSO4 x 7H2O", "0.1", "G_PER_L"),
    ("MnCl2 x 4H2O", "0.03", "G_PER_L"),
    ("H3BO3", "0.3", "G_PER_L"),
    ("CoCl2 x 6H2O", "0.2", "G_PER_L"),
    ("CuCl2 x 2H2O", "0.01", "G_PER_L"),
    ("NiCl2 x 6H2O", "0.02", "G_PER_L"),
    ("Na2MoO4 x 2H2O", "0.03", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)
SELENITE_TUNGSTATE_SIGNATURE: tuple[Component, ...] = (
    ("NaOH", "0.4", "G_PER_L"),
    ("Na2SeO3 x 5H2O", "6.0", "MG_PER_L"),
    ("Na2WO4 x 2H2O", "8.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
TRACE_VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine hydrochloride", "10.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)
YEAST_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "1.0", "PERCENT_W_V"),
)
NA2S_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Na2S x 9H2O", "5.0", "PERCENT_W_V"),
)
CROTONATE_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Sodium crotonate", "2.0", "MOLAR"),
)
DITHIONITE_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Sodium dithionite", "0.1", "PERCENT_W_V"),
    ("NaHCO3", "1.0", "MOLAR"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("1 N NH4Cl solution", "4.0", "ML_PER_L", NH4CL_STOCK_SIGNATURE),
    ("1 M MgCl2 solution", "1.0", "ML_PER_L", MGCL2_STOCK_SIGNATURE),
    ("Trace element solution", "1.0", "ML_PER_L", TRACE_ELEMENT_SIGNATURE),
    (
        "Selenite-tungstate solution",
        "1.0",
        "ML_PER_L",
        SELENITE_TUNGSTATE_SIGNATURE,
    ),
    ("Trace vitamins", "1.0", "ML_PER_L", TRACE_VITAMIN_SIGNATURE),
    ("1.0% Yeast extract solution", "2.0", "ML_PER_L", YEAST_STOCK_SIGNATURE),
    ("5% Na2S x 9H2O solution", "2.5", "ML_PER_L", NA2S_STOCK_SIGNATURE),
    (
        "2.0 M Sodium crotonate solution",
        "10.0",
        "ML_PER_L",
        CROTONATE_STOCK_SIGNATURE,
    ),
    (
        "0.1% Sodium dithionite solution (in 1 M NaHCO3)",
        "2.0",
        "ML_PER_L",
        DITHIONITE_STOCK_SIGNATURE,
    ),
)

REFERENCES = (TOGO_M1385, MEDIADIVE_J1289)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Ar": ("CHEBI:49474", "argon(0)"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "EDTA": ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgCl2": ("CHEBI:6636", "magnesium dichloride"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO3 x 5H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NiCl2 x 6H2O": ("CHEBI:34887", "nickel dichloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine hydrochloride": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Sodium crotonate": ("CHEBI:35899", "crotonate"),
    "Sodium dithionite": ("CHEBI:66870", "sodium dithionite"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "ZnSO4 x 7H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS[preferred_term]
    row["term"] = _term(*grounding)
    if grounding[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _one_component_stock(
    preferred_term: str,
    value: str,
    signature: tuple[Component, ...],
    *,
    notes: str,
    preparation_notes: str,
) -> dict[str, Any]:
    stock_component, stock_value, stock_unit = signature[0]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": [
            _component(
                stock_component,
                stock_value,
                stock_unit,
                source=SOURCE,
                notes=(
                    f"{preferred_term} is represented from the stock label as "
                    f"{stock_value} {UNIT_LABELS[stock_unit]} {stock_component}."
                ),
            )
        ],
        "preparation_notes": preparation_notes,
    }


def _solution(
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
        "composition": [
            _component(component, amount, unit, source=SOURCE)
            for component, amount, unit in signature
        ],
        "preparation_notes": preparation_notes,
    }


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component("Na2CO3", "64.0", "G_PER_L", source=SOURCE),
    _component("NaHCO3", "40.0", "G_PER_L", source=SOURCE),
    _component("NaCl", "18.0", "G_PER_L", source=SOURCE),
    _component("K2HPO4", "1.0", "G_PER_L", source=SOURCE),
    _component(
        "Distilled water",
        "1.0",
        "L",
        source=SOURCE,
        notes=(
            "MediaDive J1289 records the base salts as brought to 1.0 L with "
            "distilled water before pH adjustment and autoclaving."
        ),
    ),
    _component(
        "HCl",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes="MediaDive J1289 adjusts the base to pH 9.6 with 6N HCl.",
    ),
    _component(
        "Ar",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes=(
            "MediaDive J1289 distributes the completed medium into culture vessels "
            "under an argon gas stream."
        ),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _one_component_stock(
        "1 N NH4Cl solution",
        "4.0",
        NH4CL_STOCK_SIGNATURE,
        notes="MediaDive J1289 adds 4.0 ml/L 1 N NH4Cl solution.",
        preparation_notes="Autoclave before aseptic addition.",
    ),
    _one_component_stock(
        "1 M MgCl2 solution",
        "1.0",
        MGCL2_STOCK_SIGNATURE,
        notes="MediaDive J1289 adds 1.0 ml/L 1 M MgCl2 solution.",
        preparation_notes="Autoclave before aseptic addition.",
    ),
    _solution(
        "Trace element solution",
        "1.0",
        TRACE_ELEMENT_SIGNATURE,
        notes=(
            "MediaDive J1289 adds 1.0 ml/L Trace element solution and preserves "
            "the stock recipe as a 1.0 L solution."
        ),
        preparation_notes="Adjust the stock to pH 3.6 and autoclave before aseptic addition.",
    ),
    _solution(
        "Selenite-tungstate solution",
        "1.0",
        SELENITE_TUNGSTATE_SIGNATURE,
        notes=(
            "MediaDive J1289 adds 1.0 ml/L filter-sterilized "
            "Selenite-tungstate solution."
        ),
        preparation_notes="Filter-sterilize before aseptic addition.",
    ),
    _solution(
        "Trace vitamins",
        "1.0",
        TRACE_VITAMIN_SIGNATURE,
        notes="MediaDive J1289 adds 1.0 ml/L filter-sterilized Trace vitamins.",
        preparation_notes="Filter-sterilize before aseptic addition.",
    ),
    _one_component_stock(
        "1.0% Yeast extract solution",
        "2.0",
        YEAST_STOCK_SIGNATURE,
        notes="MediaDive J1289 adds 2.0 ml/L 1.0% Yeast extract solution.",
        preparation_notes="Autoclave before aseptic addition.",
    ),
    _one_component_stock(
        "5% Na2S x 9H2O solution",
        "2.5",
        NA2S_STOCK_SIGNATURE,
        notes="MediaDive J1289 adds 2.5 ml/L 5% Na2S x 9H2O solution.",
        preparation_notes="Autoclave before aseptic addition.",
    ),
    _one_component_stock(
        "2.0 M Sodium crotonate solution",
        "10.0",
        CROTONATE_STOCK_SIGNATURE,
        notes=(
            "MediaDive J1289 adds 10.0 ml/L filter-sterilized 2.0 M "
            "Sodium crotonate solution."
        ),
        preparation_notes="Filter-sterilize before aseptic addition.",
    ),
    _solution(
        "0.1% Sodium dithionite solution (in 1 M NaHCO3)",
        "2.0",
        DITHIONITE_STOCK_SIGNATURE,
        notes=(
            "MediaDive J1289 adds 2.0 ml/L filter-sterilized 0.1% "
            "Sodium dithionite solution in 1 M NaHCO3."
        ),
        preparation_notes="Filter-sterilize before aseptic addition.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Add Na2CO3, NaHCO3, NaCl, and K2HPO4 to distilled water and "
            "bring the volume to 1.0 L."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 9.6 with 6N HCl.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base medium.",
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "After cooling, aseptically add autoclaved and filter-sterilized "
            "stock solutions."
        ),
    },
    {
        "step_number": 5,
        "action": "ALIQUOT",
        "description": (
            "Aseptically and anaerobically distribute the medium into culture "
            "vessels under an argon gas stream and seal with butyl rubber stoppers."
        ),
    },
)

NOTES = (
    "TOGO M1385 imports JCM Medium 1289. MediaDive J1289 preserves the pH "
    "9.6 base carbonate-phosphate recipe, the nine per-liter stock additions, "
    "and anaerobic distribution under an argon gas stream."
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

    for obsolete in (
        "has_unmapped_ingredients",
        "incomplete_composition",
        "needs_manual_curation",
    ):
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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Expanded the empty TOGO stock wrappers with the nested "
            "stock compositions and corrected stock additions from g/L artifacts "
            "to ml/L volumes."
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
    _put_after(repaired, "ph_value", 9.6, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "notes": (
                "Autoclave the base medium. Add the indicated autoclaved or "
                "filter-sterilized stocks aseptically after cooling."
            ),
        },
        "preparation_steps",
    )
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
