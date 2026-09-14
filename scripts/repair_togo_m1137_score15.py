#!/usr/bin/env python3
"""Repair TOGO M1137 Saltwater Iron-Oxidizing Bacteria Medium-II."""

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
TARGET = Path("bacterial/TOGO_M1137_Saltwater_Iron-Oxidizing_Bacteria_Medium-II.yaml")
EXPECTED_ID = "CultureMech:007659"
EXPECTED_MEDIA_TERM = "TOGO:M1137"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1137_score15.py"
ACTION = "RESOLVED_TOGO_M1137_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1137 = "https://togomedium.org/medium/M1137"
TOGO_M642 = "https://togomedium.org/medium/M642"
TOGO_M257 = "https://togomedium.org/medium/M257"
TOGO_M190 = "https://togomedium.org/medium/M190"
JCM_1068 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1068"
JCM_629 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=629"
JCM_265 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=265"
JCM_151 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"

SOURCE = "TOGO M1137 / JCM Medium 1068"
SALTWATER_SOURCE = "TOGO M642 / JCM Medium 629"
WOLFE_SOURCE = "TOGO M257 / JCM Medium 265"
TRACE_MINERALS_SOURCE = "JCM Medium 151"
VITAMINS_SOURCE = "TOGO M190 / JCM Medium 197"
TITLE = "Saltwater Iron-Oxidizing Bacteria  Medium-II"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = IMPORTED_INGREDIENT_SIGNATURE

ARTIFICIAL_SALTWATER_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "27.5", "G_PER_L"),
    ("MgCl2 x 6H2O", "5.38", "G_PER_L"),
    ("MgSO4 x 7H2O", "6.78", "G_PER_L"),
    ("KCl", "0.72", "G_PER_L"),
    ("NaHCO3", "0.2", "G_PER_L"),
    ("CaCl2 x 2H2O", "1.4", "G_PER_L"),
    ("NH4Cl", "1.0", "G_PER_L"),
    ("KH2PO4", "0.05", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

TRACE_MINERALS_SIGNATURE: tuple[Component, ...] = (
    ("Nitrilotriacetic acid", "1.5", "G_PER_L"),
    ("MgSO4 x 7H2O", "3.0", "G_PER_L"),
    ("MnSO4 x xH2O", "0.5", "G_PER_L"),
    ("NaCl", "1.0", "G_PER_L"),
    ("FeSO4 x 7H2O", "0.1", "G_PER_L"),
    ("CoSO4 x 7H2O", "0.1", "G_PER_L"),
    ("CaCl2 x 2H2O", "0.1", "G_PER_L"),
    ("ZnSO4 x 7H2O", "0.1", "G_PER_L"),
    ("CuSO4 x 5H2O", "0.01", "G_PER_L"),
    ("AlK(SO4)2", "0.01", "G_PER_L"),
    ("H3BO3", "0.01", "G_PER_L"),
    ("Na2MoO4 x 2H2O", "0.01", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

WOLFE_ADDITION_SIGNATURE: tuple[Component, ...] = (
    ("NiCl2 x 6H2O", "0.02", "G_PER_L"),
    ("Na2SeO3", "0.001", "G_PER_L"),
    ("Na2WO4 x 2H2O", "0.01", "G_PER_L"),
)

WOLFE_SIGNATURE: tuple[Component, ...] = (
    *TRACE_MINERALS_SIGNATURE,
    *WOLFE_ADDITION_SIGNATURE,
)

BICARBONATE_SIGNATURE: tuple[Component, ...] = (
    ("NaHCO3", "8.0", "PERCENT_W_V"),
)

FECL2_SIGNATURE: tuple[Component, ...] = (
    ("FeCl2", "0.2", "MOLAR"),
)

VITAMIN_SIGNATURE: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1.0", "L"),
)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Artificial saltwater (see Medium [M642])", "1", "G_PER_L", ()),
    ("Wolfe's mineral solution (see Medium [M257])", "10", "G_PER_L", ()),
    ("8% NaHCO3 solution", "12.5", "G_PER_L", ()),
    ("0.2 M FeCl2 solution (freshly prepared)", "10", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Artificial saltwater", "1000.0", "ML_PER_L", ARTIFICIAL_SALTWATER_SIGNATURE),
    ("Wolfe's mineral solution", "10.0", "ML_PER_L", WOLFE_SIGNATURE),
    ("8% NaHCO3 solution", "12.5", "ML_PER_L", BICARBONATE_SIGNATURE),
    ("0.2 M FeCl2 solution", "10.0", "ML_PER_L", FECL2_SIGNATURE),
    ("Trace vitamins", "10.0", "ML_PER_L", VITAMIN_SIGNATURE),
)

REFERENCES = (
    TOGO_M1137,
    JCM_1068,
    TOGO_M642,
    JCM_629,
    TOGO_M257,
    JCM_265,
    JCM_151,
    TOGO_M190,
    JCM_197,
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "AlK(SO4)2": ("CHEBI:86463", "potassium aluminium sulfate"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoSO4 x 7H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "CuSO4 x 5H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2": ("CHEBI:30812", "iron dichloride"),
    "FeSO4 x 7H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnSO4 x xH2O": ("CHEBI:86360", "manganese(II) sulfate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SeO3": ("CHEBI:48843", "disodium selenite"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NiCl2 x 6H2O": ("CHEBI:34887", "nickel dichloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Nitrilotriacetic acid": ("CHEBI:44557", "nitrilotriacetic acid"),
    "Oxygen gas": ("CHEBI:15379", "dioxygen"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
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
    notes: str,
) -> dict[str, Any]:
    grounding = GROUNDINGS[preferred_term]
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
        "term": _term(*grounding),
        "mediaingredientmech_chebi_term": _term(*grounding),
    }


def _listed_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    )


def _gas(preferred_term: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes=(
            "JCM Medium 1068 replaces the gas phase with "
            "N2-CO2-O2 (80:20:3, v/v/v) and pressurizes it to 200 kPa."
        ),
    )


def _stock(
    preferred_term: str,
    dose: str,
    composition: tuple[Component, ...],
    *,
    source: str,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": dose, "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": notes,
        "composition": [
            _listed_component(name, value, unit, source=source)
            for name, value, unit in composition
        ],
    }
    if preparation_notes:
        row["preparation_notes"] = preparation_notes
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _gas("Carbon dioxide gas"),
    _gas("Nitrogen gas"),
    _gas("Oxygen gas"),
)

WOLFE_COMPOSITION: tuple[dict[str, Any], ...] = (
    *(
        _listed_component(name, value, unit, source=TRACE_MINERALS_SOURCE)
        for name, value, unit in TRACE_MINERALS_SIGNATURE
    ),
    *(
        _listed_component(name, value, unit, source=WOLFE_SOURCE)
        for name, value, unit in WOLFE_ADDITION_SIGNATURE
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _stock(
        "Artificial saltwater",
        "1000.0",
        ARTIFICIAL_SALTWATER_SIGNATURE,
        source=SALTWATER_SOURCE,
        notes="JCM Medium 1068 lists 1.0 L Artificial saltwater.",
    ),
    {
        "preferred_term": "Wolfe's mineral solution",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": "JCM Medium 1068 lists 10.0 ml/L Wolfe's mineral solution.",
        "composition": list(WOLFE_COMPOSITION),
        "preparation_notes": (
            "JCM Medium 265 prepares Wolfe's mineral solution from Trace "
            "minerals from JCM Medium 151, NiCl2 x 6H2O, Na2SeO3, and "
            "Na2WO4 x 2H2O."
        ),
    },
    {
        "preferred_term": "8% NaHCO3 solution",
        "concentration": {"value": "12.5", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 1068 adds 12.5 ml/L filter-sterilized 8% NaHCO3 "
            "solution after autoclaving."
        ),
        "composition": [
            _component(
                "NaHCO3",
                "8.0",
                "PERCENT_W_V",
                source=SOURCE,
                notes=(
                    "8% NaHCO3 solution is represented from the stock label as "
                    "8.0% w/v NaHCO3."
                ),
            )
        ],
        "preparation_notes": "Filter-sterilize before aseptic addition.",
    },
    {
        "preferred_term": "0.2 M FeCl2 solution",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE,
        "notes": (
            "JCM Medium 1068 adds 10.0 ml/L freshly prepared and "
            "filter-sterilized 0.2 M FeCl2 solution after autoclaving."
        ),
        "composition": [
            _component(
                "FeCl2",
                "0.2",
                "MOLAR",
                source=SOURCE,
                notes=(
                    "0.2 M FeCl2 solution is represented from the stock label as "
                    "0.2 M FeCl2."
                ),
            )
        ],
        "preparation_notes": "Prepare freshly and filter-sterilize before use.",
    },
    _stock(
        "Trace vitamins",
        "10.0",
        VITAMIN_SIGNATURE,
        source=VITAMINS_SOURCE,
        notes=(
            "JCM Medium 1068 adds 10.0 ml/L filter-sterilized Trace vitamins "
            "after autoclaving."
        ),
        preparation_notes="Filter-sterilize before aseptic addition.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix Artificial saltwater and Wolfe's mineral solution, distribute "
            "the medium into culture vessels, and seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 degrees C for 15 min.",
    },
    {
        "step_number": 3,
        "action": "FILTER_STERILIZE",
        "description": (
            "Aseptically add filter-sterilized Trace vitamins, 8% NaHCO3 "
            "solution, and freshly prepared 0.2 M FeCl2 solution per liter."
        ),
    },
    {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Replace the gas phase with an N2-CO2-O2 (80:20:3, v/v/v) gas "
            "mixture and pressurize to 200 kPa with the same gas mixture."
        ),
    },
)

NOTES = (
    "TOGO M1137 records JCM Medium 1068 as a saltwater iron-oxidizing bacteria "
    "medium. JCM 1068 mixes Artificial saltwater from JCM Medium 629 with "
    "Wolfe's mineral solution from JCM Medium 265, autoclaves the sealed "
    "vessels, aseptically adds filter-sterilized Trace vitamins from JCM "
    "Medium 197, 8% NaHCO3 solution, and freshly prepared 0.2 M FeCl2 "
    "solution, then replaces the gas phase with N2-CO2-O2 (80:20:3, v/v/v) "
    "and pressurizes it to 200 kPa."
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
    if ingredient_signature != FINAL_INGREDIENT_SIGNATURE:
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{FINAL_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
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
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
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
                "Filter-sterilize Trace vitamins, 8% NaHCO3 solution, and "
                "freshly prepared 0.2 M FeCl2 solution separately."
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
