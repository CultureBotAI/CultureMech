#!/usr/bin/env python3
"""Repair TOGO M1127 PYGV Marine Medium B."""

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
TARGET = Path("bacterial/TOGO_M1127_PYGV_Marine_Medium_B.yaml")
EXPECTED_ID = "CultureMech:007648"
EXPECTED_MEDIA_TERM = "TOGO:M1127"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1127_score15.py"
ACTION = "RESOLVED_TOGO_M1127_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1127 = "https://togomedium.org/medium/M1127"
TOGO_M299 = "https://togomedium.org/medium/M299"
JCM_1059 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1059"
JCM_304 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=304"
JCM_149 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=149"

SOURCE = "TOGO M1127 / JCM Medium 1059"
STOCK_SOURCE = "TOGO M299 / JCM Medium 304"
METALS_44_SOURCE = "JCM Medium 149"
TITLE = "PYGV Marine Medium (B)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "710", "G_PER_L"),
    ("agar", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.25", "G_PER_L"),
    ("Bacto peptone (BD-Difco)", "0.25", "G_PER_L"),
    ("KOH", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto peptone (BD-Difco)", "0.25", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "0.25", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Distilled water", "710.0", "ML_PER_L"),
    ("KOH", "variable", "VARIABLE"),
)

GLUCOSE_SIGNATURE: tuple[Component, ...] = (("Glucose", "2.5", "PERCENT_W_V"),)

MINERAL_SALT_SIGNATURE: tuple[Component, ...] = (
    ("MgSO4 x 7H2O", "29.7", "G_PER_L"),
    ("Nitrilotriacetic acid", "10.0", "G_PER_L"),
    ("CaCl2 x 2H2O", "3.34", "G_PER_L"),
    ("FeSO4 x 7H2O", "99.0", "MG_PER_L"),
    ("Na2MoO4 x 2H2O", "13.0", "MG_PER_L"),
    ("Metals 44", "50.0", "ML_PER_L"),
    ("Distilled water", "950.0", "ML_PER_L"),
)

VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Nicotinamide", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

SEAWATER_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "23.477", "G_PER_L"),
    ("Na2SO4", "3.917", "G_PER_L"),
    ("MgCl2 x 6H2O", "4.981", "G_PER_L"),
    ("CaCl2 x 2H2O", "1.102", "G_PER_L"),
    ("NaHCO3", "192.0", "MG_PER_L"),
    ("KCl", "664.0", "MG_PER_L"),
    ("KBr", "6.0", "MG_PER_L"),
    ("H3BO3", "26.0", "MG_PER_L"),
    ("SrCl2 x 6H2O", "24.0", "MG_PER_L"),
    ("NaF", "3.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("2.5% Glucose solution", "10", "G_PER_L", ()),
    ("Mineral salt solution (see Medium [M299])", "20", "G_PER_L", ()),
    ("Vitamin solution (see Medium [M299])", "10", "G_PER_L", ()),
    ("Artificial seawater (see Medium [M299])", "250", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Mineral salt solution", "20.0", "ML_PER_L", MINERAL_SALT_SIGNATURE),
    ("2.5% Glucose solution", "10.0", "ML_PER_L", GLUCOSE_SIGNATURE),
    ("Vitamin solution", "10.0", "ML_PER_L", VITAMIN_SIGNATURE),
    ("Artificial seawater", "250.0", "ML_PER_L", SEAWATER_SIGNATURE),
)

REFERENCES = (TOGO_M1127, JCM_1059, TOGO_M299, JCM_304, JCM_149)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KBr": ("CHEBI:32030", "potassium bromide"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KOH": ("CHEBI:32035", "potassium hydroxide"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaF": ("CHEBI:28741", "sodium fluoride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Nicotinamide": ("CHEBI:17154", "nicotinamide"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "SrCl2 x 6H2O": ("CHEBI:36385", "strontium dichloride hexahydrate"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
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
    notes: str,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: bool = True,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        term=term,
    )


def _stock_reference(
    preferred_term: str,
    value: str,
    source: str,
    notes: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        source=source,
        notes=notes,
        term=False,
    )


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _listed_component("Bacto peptone (BD-Difco)", "0.25", "G_PER_L", source=SOURCE, term=False),
    _listed_component("Yeast extract (BD-Difco)", "0.25", "G_PER_L", source=SOURCE, term=False),
    _listed_component("Agar", "15.0", "G_PER_L", source=SOURCE),
    _listed_component("Distilled water", "710.0", "ML_PER_L", source=SOURCE),
    _component(
        "KOH",
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes=(
            "JCM Medium 1059 adjusts the medium to pH 7.2-7.4 with sterile KOH, " "if necessary."
        ),
    ),
)


def _solution(
    preferred_term: str,
    dose: str,
    composition: tuple[Component, ...],
    source: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": dose, "unit": "ML_PER_L"},
        "source": SOURCE if source == STOCK_SOURCE else source,
        "notes": f"JCM Medium 1059 adds {dose} ml/L {preferred_term}.",
        "composition": [
            _listed_component(name, value, unit, source=source, term=name in GROUNDINGS)
            for name, value, unit in composition
        ],
    }


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution("Mineral salt solution", "20.0", MINERAL_SALT_SIGNATURE, STOCK_SOURCE),
    _solution("2.5% Glucose solution", "10.0", GLUCOSE_SIGNATURE, SOURCE),
    _solution("Vitamin solution", "10.0", VITAMIN_SIGNATURE, STOCK_SOURCE),
    _solution("Artificial seawater", "250.0", SEAWATER_SIGNATURE, STOCK_SOURCE),
)
SOLUTIONS[0]["composition"][5] = _stock_reference(
    "Metals 44",
    "50.0",
    METALS_44_SOURCE,
    "JCM Medium 304 adds 50.0 ml/L Metals 44 from JCM Medium 149.",
)
SOLUTIONS[1]["preparation_notes"] = "Filter-sterilize before aseptic addition."
SOLUTIONS[2]["preparation_notes"] = "Filter-sterilize before aseptic addition."

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix peptone, yeast extract, mineral salt solution, artificial seawater, "
            "agar, and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "HEAT",
        "description": "Gently heat and bring to a boil.",
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 4,
        "action": "COOL",
        "description": "Cool to 45-50 degrees C.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Aseptically add the filter-sterilized glucose solution and vitamin " "solution."
        ),
    },
    {
        "step_number": 6,
        "action": "ADJUST_PH",
        "description": "Adjust to pH 7.2-7.4 with sterile KOH, if necessary.",
    },
)

NOTES = (
    "TOGO M1127 records JCM Medium 1059 with Bacto peptone, yeast extract, "
    "mineral salt solution from JCM Medium 304, 2.5% glucose solution, vitamin "
    "solution from JCM Medium 304, artificial seawater from JCM Medium 304, "
    "distilled water, KOH for optional pH adjustment, and 15 g/L agar for the "
    "solid formulation. JCM 1059 gently heats the base, autoclaves it, cools it "
    "to 45-50 degrees C, adds filter-sterilized glucose and vitamin solutions "
    "aseptically, and adjusts pH to 7.2-7.4 with sterile KOH if necessary."
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
        "notes": NOTES,
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
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_range", {"min": 7.2, "max": 7.4}, "physical_state")
    repaired.pop("ph_value", None)
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
            "notes": "Filter-sterilize glucose and vitamin solutions separately.",
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
