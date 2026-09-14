#!/usr/bin/env python3
"""Repair the recovered NBRC Medium 1356 haloalkaliphilic methanogen record."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_nbrc_1358_score15.py"
ACTION = "RESOLVED_NBRC_1358_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_1358.yaml"
TARGET_ID = "CultureMech:007474"
REQUIRED_ACTION = "Recovered composition from source HTML"

SOURCE = "NBRC Medium 1356"
NBRC_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1356"
TITLE = "Medium for haloalkaliphilic methanogen"
DITHIONITE_WRAPPER = "Sodium dithionite solution in 1 M NaHCO3"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Mineral base 1*", "500", "ML_PER_L"),
    ("Mineral base 2**", "500", "ML_PER_L"),
    ("MgCl2·6H2O", "0.2", "G_PER_L"),
    ("Bacto Yeast Extract (Difco)", "0.02", "G_PER_L"),
    ("Coenzyme M", "0.014", "G_PER_L"),
    ("Vitamin solution***", "5", "ML_PER_L"),
    ("Trace element solution****", "10", "ML_PER_L"),
    ("Methanol", "2", "ML_PER_L"),
    ("Sodium formate", "3.4", "G_PER_L"),
    ("Sodium acetate", "0.16", "G_PER_L"),
    ("FeS slurry solution*****", "2", "ML_PER_L"),
    ("Na2S·9H2O", "0.12", "G_PER_L"),
)
FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    *IMPORTED_INGREDIENT_SIGNATURE,
    (DITHIONITE_WRAPPER, "variable", "VARIABLE"),
)

MINERAL_BASE_1_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3", "185", "G_PER_L"),
    ("NaHCO3", "35", "G_PER_L"),
    ("NaCl", "16", "G_PER_L"),
    ("K2HPO4", "1", "G_PER_L"),
    ("Distilled water", "1", "L"),
)
MINERAL_BASE_2_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "240", "G_PER_L"),
    ("NH4Cl", "0.5", "G_PER_L"),
    ("K2HPO4", "2.5", "G_PER_L"),
    ("KCl", "5", "G_PER_L"),
    ("Distilled water", "1", "L"),
)
VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2", "MG_PER_L"),
    ("Folic acid", "2", "MG_PER_L"),
    ("Pyridoxine-HCl", "10", "MG_PER_L"),
    ("Thiamine-HCl", "5", "MG_PER_L"),
    ("Riboflavin", "5", "MG_PER_L"),
    ("Nicotinic acid", "5", "MG_PER_L"),
    ("Ca-pantothenate", "5", "MG_PER_L"),
    ("p-Aminobenzoic acid", "1", "MG_PER_L"),
    ("Vitamin B12", "0.01", "MG_PER_L"),
    ("Distilled water", "1", "L"),
)
IMPORTED_TRACE_SIGNATURE: tuple[Component, ...] = (
    ("Nitrilotriacetic acid (NTA)", "12.8", "G_PER_L"),
    ("FeCl3·6H2O", "1.35", "G_PER_L"),
    ("MnCl2·4H2O", "0.1", "G_PER_L"),
    ("CoCl2·6H2O", "0.024", "G_PER_L"),
    ("CaCl2·2H2O", "0.1", "G_PER_L"),
    ("ZnCl2", "0.1", "G_PER_L"),
    ("CuCl2·2H2O", "0.025", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4·2H2O", "0.024", "G_PER_L"),
    ("NaCl", "1", "G_PER_L"),
    ("NiCl2·6H2O", "0.12", "G_PER_L"),
    ("Na2SeO4", "0.004", "G_PER_L"),
    ("Na2WO4", "0.004", "G_PER_L"),
    ("Distilled water", "1", "L"),
)
FINAL_TRACE_SIGNATURE: tuple[Component, ...] = IMPORTED_TRACE_SIGNATURE + (
    ("NaOH", "variable", "VARIABLE"),
)
FES_SLURRY_SIGNATURE: tuple[Component, ...] = (
    ("FeSO4·7H2O", "0.5", "MOLAR"),
    ("Na2S·9H2O", "0.5", "MOLAR"),
)
DITHIONITE_SIGNATURE: tuple[Component, ...] = (
    ("Sodium dithionite", "10", "PERCENT_W_V"),
    ("NaHCO3", "1", "MOLAR"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Mineral base 1", MINERAL_BASE_1_SIGNATURE),
    ("Mineral base 2", MINERAL_BASE_2_SIGNATURE),
    ("Vitamin solution", VITAMIN_SIGNATURE),
    ("Trace elements solution", IMPORTED_TRACE_SIGNATURE),
)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Mineral base 1", MINERAL_BASE_1_SIGNATURE),
    ("Mineral base 2", MINERAL_BASE_2_SIGNATURE),
    ("Vitamin solution", VITAMIN_SIGNATURE),
    ("Trace elements solution", FINAL_TRACE_SIGNATURE),
    ("FeS slurry solution", FES_SLURRY_SIGNATURE),
    ("Sodium dithionite solution", DITHIONITE_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "Ca-pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CaCl2·2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2·6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "Coenzyme M": ("CHEBI:17905", "coenzyme M"),
    "CuCl2·2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl3·6H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "FeSO4·7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "Methanol": ("CHEBI:17790", "methanol"),
    "MgCl2·6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2·4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na2MoO4·2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S·9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO4": ("CHEBI:77775", "sodium selenate"),
    "Na2WO4": ("CHEBI:63940", "sodium tungstate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NiCl2·6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrilotriacetic acid (NTA)": ("CHEBI:44557", "nitrilotriacetic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine-HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Sodium acetate": ("CHEBI:32954", "sodium acetate"),
    "Sodium dithionite": ("CHEBI:66870", "sodium dithionite"),
    "Sodium formate": ("CHEBI:62965", "sodium formate"),
    "Thiamine-HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "Mix Mineral base 1 ingredients and autoclave under an N2 "
            "atmosphere; after 1 day, use only the supernatant. Final pH "
            "should be 10."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": (
            "Mix Mineral base 2 ingredients and autoclave under an N2 "
            "atmosphere. Final pH should be 7.3."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": (
            "For the trace elements solution, first dissolve NTA, adjust pH "
            "to 6.5 with NaOH, then add minerals; final pH is 7.0."
        ),
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": (
            "Prepare the FeS slurry from 0.5 M FeSO4·7H2O and 0.5 M "
            "Na2S·9H2O, wash with pure water, resuspend the FeS precipitate "
            "as a 20% solution, and autoclave at 110 C for 30 min under N2."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Mix Mineral base 1 and Mineral base 2 in a 1:1 proportion in "
            "tightly closed vessels under an N2 atmosphere."
        ),
    },
    {
        "step_number": 6,
        "action": "AUTOCLAVE",
        "description": (
            "Separately autoclave concentrated Bacto Yeast Extract, "
            "coenzyme M, sodium acetate, Na2S·9H2O, and FeS slurry under "
            "an N2 atmosphere in tightly closed vessels."
        ),
    },
    {
        "step_number": 7,
        "action": "FILTER_STERILIZE",
        "description": (
            "Filter-sterilize concentrated MgCl2·6H2O, vitamin solution, "
            "trace element solution, methanol, and sodium formate solution."
        ),
    },
    {
        "step_number": 8,
        "action": "MIX",
        "description": (
            "After re-exchanging with N2, add one drop of filter-sterile 10% "
            "sodium dithionite in 1 M NaHCO3 by syringe. Final pH of the "
            "complete medium should be 9."
        ),
    },
)

NOTES = (
    "Source: NBRC Medium 1356 | Link: "
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1356\n\n"
    "NBRC lists Medium for haloalkaliphilic methanogen as a 1:1 mix of two "
    "N2-autoclaved mineral bases with MgCl2, Bacto Yeast Extract, coenzyme M, "
    "vitamin and trace-element stocks, methanol, formate, acetate, FeS slurry, "
    "Na2S, and a 10% sodium dithionite solution in 1 M NaHCO3. The complete "
    "medium is adjusted anaerobically and has final pH 9."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str,
) -> dict[str, Any]:
    term = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
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


def _solution_signature(solution: dict[str, Any]) -> SolutionSignature:
    return (
        str(solution.get("preferred_term") or ""),
        _signature(solution.get("composition"), "solution composition"),
    )


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if any(not isinstance(solution, dict) for solution in solutions):
        raise ValueError("solutions contains a non-mapping row")
    return tuple(_solution_signature(solution) for solution in solutions)


def _has_history_action(doc: dict[str, Any], action: str) -> bool:
    return any(
        isinstance(event, dict) and event.get("action") == action
        for event in doc.get("curation_history") or []
    )


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != TARGET_ID:
        raise ValueError(f"{TARGET_PATH}: found id {doc.get('id')!r}, expected {TARGET_ID!r}")
    if not _has_history_action(doc, REQUIRED_ACTION):
        raise ValueError(f"{TARGET_PATH}: missing recovery action {REQUIRED_ACTION!r}")
    if doc.get("name") not in {"1358", TITLE}:
        raise ValueError(f"{TARGET_PATH}: NBRC title/name drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(
            f"{TARGET_PATH}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in {
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    }:
        raise ValueError(f"{TARGET_PATH}: nested solution signature drifted")


def _iter_components(doc: dict[str, Any]):
    yield from doc.get("ingredients") or []
    for solution in doc.get("solutions") or []:
        yield from solution.get("composition") or []


def _ground_components(doc: dict[str, Any]) -> None:
    for row in _iter_components(doc):
        name = str(row.get("preferred_term") or "")
        term = GROUNDINGS.get(name)
        if not term:
            continue
        row["term"] = _term(*term)
        row["mediaingredientmech_chebi_term"] = _term(*term)


def _ensure_dithionite_ingredient(doc: dict[str, Any]) -> None:
    ingredients = doc.get("ingredients")
    if not isinstance(ingredients, list):
        raise ValueError(f"{TARGET_PATH}: ingredients is not a list")
    if any(
        isinstance(row, dict) and row.get("preferred_term") == DITHIONITE_WRAPPER
        for row in ingredients
    ):
        return
    ingredients.append(
        {
            "preferred_term": DITHIONITE_WRAPPER,
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": SOURCE,
            "notes": (
                "NBRC Medium 1356 adds one drop of filter-sterile 10% sodium "
                "dithionite solution in 1 M NaHCO3 by syringe."
            ),
        }
    )


def _ensure_trace_naoh(doc: dict[str, Any]) -> None:
    trace = next(
        solution
        for solution in doc.get("solutions") or []
        if solution.get("preferred_term") == "Trace elements solution"
    )
    composition = trace.get("composition")
    if not isinstance(composition, list):
        raise ValueError(f"{TARGET_PATH}: Trace elements solution lacks composition")
    if any(isinstance(row, dict) and row.get("preferred_term") == "NaOH" for row in composition):
        return
    composition.append(
        _component(
            "NaOH",
            "variable",
            "VARIABLE",
            notes=(
                "NBRC Medium 1356 uses NaOH to adjust the trace elements "
                "solution to pH 6.5 before mineral addition."
            ),
        )
    )


def _ensure_solution(
    doc: dict[str, Any],
    preferred_term: str,
    rows: list[dict[str, Any]],
) -> None:
    solutions = doc.get("solutions")
    if not isinstance(solutions, list):
        raise ValueError(f"{TARGET_PATH}: solutions is not a list")
    if any(
        isinstance(solution, dict) and solution.get("preferred_term") == preferred_term
        for solution in solutions
    ):
        return
    solutions.append(
        {
            "preferred_term": preferred_term,
            "composition": rows,
            "name": preferred_term,
        }
    )


def _ensure_fes_slurry(doc: dict[str, Any]) -> None:
    _ensure_solution(
        doc,
        "FeS slurry solution",
        [
            _component(
                "FeSO4·7H2O",
                "0.5",
                "MOLAR",
                notes=(
                    "NBRC Medium 1356 prepares FeS slurry by mixing 0.5 M "
                    "FeSO4·7H2O and 0.5 M Na2S·9H2O solutions."
                ),
            ),
            _component(
                "Na2S·9H2O",
                "0.5",
                "MOLAR",
                notes=(
                    "NBRC Medium 1356 prepares FeS slurry by mixing 0.5 M "
                    "FeSO4·7H2O and 0.5 M Na2S·9H2O solutions."
                ),
            ),
        ],
    )


def _ensure_dithionite_solution(doc: dict[str, Any]) -> None:
    _ensure_solution(
        doc,
        "Sodium dithionite solution",
        [
            _component(
                "Sodium dithionite",
                "10",
                "PERCENT_W_V",
                notes=(
                    "NBRC Medium 1356 adds one drop of filter-sterile 10% "
                    "sodium dithionite solution in 1 M NaHCO3."
                ),
            ),
            _component(
                "NaHCO3",
                "1",
                "MOLAR",
                notes=(
                    "NBRC Medium 1356 uses 1 M NaHCO3 as the solvent for "
                    "the 10% sodium dithionite solution."
                ),
            ),
        ],
    )


def _grounded(component: dict[str, Any]) -> bool:
    term = component.get("term")
    return isinstance(term, dict) and bool(term.get("id"))


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

    known_unmapped = {
        "Bacto Yeast Extract (Difco)",
        DITHIONITE_WRAPPER,
    }
    chemical_rows = [
        row
        for row in _iter_components(doc)
        if isinstance(row, dict)
        and not str(row.get("preferred_term") or "").endswith("*")
        and str(row.get("preferred_term") or "") not in known_unmapped
    ]
    if any(not _grounded(row) for row in chemical_rows):
        raise ValueError(f"{TARGET_PATH}: not all source chemical rows were grounded")


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if NBRC_URL not in found:
        references.append({"reference": NBRC_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": ("Grounded recovered NBRC Medium 1356 haloalkaliphilic " "methanogen formula"),
        "source": NBRC_URL,
        "notes": (
            "Added the NBRC Medium 1356 source term and official title, "
            "grounded the recovered formula and stocks, structured the FeS "
            "and sodium dithionite solutions, and converted anaerobic "
            "preparation instructions into ordered steps."
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


def repair_document(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "name", TITLE, "id")
    _put_after(repaired, "original_name", TITLE, "name")
    _put_after(
        repaired,
        "media_term",
        {
            "preferred_term": SOURCE,
            "term": _term("nbrc.medium:1356", SOURCE),
        },
        "physical_state",
    )
    _put_after(repaired, "ph_value", 9.0, "media_term")
    _put_after(repaired, "notes", NOTES, "description")

    _ensure_dithionite_ingredient(repaired)
    _ground_components(repaired)
    _ensure_trace_naoh(repaired)
    _ensure_fes_slurry(repaired)
    _ensure_dithionite_solution(repaired)
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["sterilization"] = {"method": "AUTOCLAVE"}

    _ensure_flags(repaired)
    _ensure_reference(repaired)
    _ensure_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET_PATH
    return {path: repair_document(_load(path))}


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

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} NBRC 1358 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
