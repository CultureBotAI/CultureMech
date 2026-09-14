#!/usr/bin/env python3
"""Repair the recovered NBRC Medium 936 Hydrogen-oxidizing bacteria record."""

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

CURATOR = "repair_nbrc_937_score15.py"
ACTION = "RESOLVED_NBRC_937_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TARGET_PATH = "bacterial/NBRC_937.yaml"
TARGET_ID = "CultureMech:007506"
REQUIRED_ACTION = "Recovered composition from source HTML"

SOURCE = "NBRC Medium 936"
NBRC_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=936"
TITLE = "Hydrogen-oxidizing bacteria medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("KP buffer*", "10", "ML_PER_L"),
    ("MgCl2·6H2O", "0.75", "G_PER_L"),
    ("CaCl2·2H2O", "0.15", "G_PER_L"),
    ("NH4Cl", "0.54", "G_PER_L"),
    ("Na2S2O3", "1.6", "G_PER_L"),
    ("Trace elements solution**", "2", "ML_PER_L"),
    ("Vitamin solution***", "2", "ML_PER_L"),
    ("Na2CO3", "0.5", "G_PER_L"),
    ("Distilled water", "1", "L"),
)

KP_BUFFER_SIGNATURE: tuple[Component, ...] = (
    ("KH2PO4", "119", "G_PER_L"),
    ("K2HPO4", "21", "G_PER_L"),
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
    ("KAl(SO4)2·12H2O", "0.02", "G_PER_L"),
    ("Distilled water", "1", "L"),
)
FINAL_TRACE_SIGNATURE: tuple[Component, ...] = IMPORTED_TRACE_SIGNATURE + (
    ("NaOH", "variable", "VARIABLE"),
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

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("KP buffer", KP_BUFFER_SIGNATURE),
    ("Trace elements solution", IMPORTED_TRACE_SIGNATURE),
    ("Vitamin solution", VITAMIN_SIGNATURE),
)
FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("KP buffer", KP_BUFFER_SIGNATURE),
    ("Trace elements solution", FINAL_TRACE_SIGNATURE),
    ("Vitamin solution", VITAMIN_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "Ca-pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "CaCl2·2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2·6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2·2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl3·6H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KAl(SO4)2·12H2O": (
        "CHEBI:86465",
        "potassium aluminium sulfate dodecahydrate",
    ),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgCl2·6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2·4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na2MoO4·2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S2O3": ("CHEBI:132112", "sodium thiosulfate"),
    "Na2SeO4": ("CHEBI:77775", "sodium selenate"),
    "Na2WO4": ("CHEBI:63940", "sodium tungstate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NiCl2·6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrilotriacetic acid (NTA)": ("CHEBI:44557", "nitrilotriacetic acid"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine-HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine-HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNMAPPED_COMPONENTS = {
    "KP buffer*",
    "Trace elements solution**",
    "Vitamin solution***",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": "Mix ingredients except KP buffer and vitamin solution.",
    },
    {
        "step_number": 2,
        "action": "ALIQUOT",
        "description": (
            "Dispense the medium into suitable culture vessels under a stream "
            "of H2/CO2/O2 (75/20/5) and seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 3,
        "action": "AUTOCLAVE",
        "description": "Separately autoclave KP buffer under an N2 atmosphere.",
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": "Sterilize vitamin solution by filtration.",
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": "Prior to inoculation, aseptically add KP buffer and vitamin solution.",
    },
    {
        "step_number": 6,
        "action": "MIX",
        "description": ("Pressurize inoculated vessels to 150 kPa with H2/CO2/O2 (75/20/5)."),
    },
    {
        "step_number": 7,
        "action": "ADJUST_PH",
        "description": (
            "For the trace elements solution, first dissolve NTA, adjust pH to "
            "6.5 with NaOH, then add minerals; final pH is 7.0."
        ),
    },
)

NOTES = (
    "Source: NBRC Medium 936 | Link: "
    "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=936\n\n"
    "NBRC lists Hydrogen-oxidizing bacteria medium with KP buffer, "
    "MgCl2·6H2O, CaCl2·2H2O, NH4Cl, Na2S2O3, trace element and vitamin "
    "stocks, Na2CO3, and distilled water. The basal medium is dispensed "
    "under H2/CO2/O2, KP buffer is autoclaved separately under N2, vitamin "
    "solution is filter-sterilized, and inoculated vessels are pressurized to "
    "150 kPa with H2/CO2/O2. NBRC does not list a final medium pH."
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": (
            "NBRC Medium 936 uses NaOH to adjust the trace elements solution "
            "to pH 6.5 before mineral addition."
        ),
    }
    term = GROUNDINGS[preferred_term]
    row["term"] = _term(*term)
    row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
    if doc.get("name") not in {"937", TITLE}:
        raise ValueError(f"{TARGET_PATH}: NBRC title/name drifted")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature != IMPORTED_INGREDIENT_SIGNATURE:
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


def _ensure_trace_naoh(doc: dict[str, Any]) -> None:
    trace = next(
        solution
        for solution in doc.get("solutions") or []
        if solution.get("preferred_term") == "Trace elements solution"
    )
    composition = trace.get("composition")
    if not isinstance(composition, list):
        raise ValueError(f"{TARGET_PATH}: Trace elements solution lacks composition")
    if not any(
        isinstance(row, dict) and row.get("preferred_term") == "NaOH" for row in composition
    ):
        composition.append(_component("NaOH", "variable", "VARIABLE"))


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

    chemical_rows = [
        row
        for row in _iter_components(doc)
        if (
            isinstance(row, dict)
            and str(row.get("preferred_term") or "") not in UNMAPPED_COMPONENTS
        )
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
        "changes": "Grounded recovered NBRC Medium 936 formula",
        "source": NBRC_URL,
        "notes": (
            "Added the NBRC Medium 936 source term and official title, "
            "grounded the recovered formula and stocks, added the "
            "source-defined NaOH trace-stock adjuster, converted preparation "
            "instructions into ordered steps, and added the official NBRC "
            "reference."
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
            "term": _term("nbrc.medium:936", SOURCE),
        },
        "physical_state",
    )
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("sterilization", None)
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["notes"] = NOTES

    _ground_components(repaired)
    _ensure_trace_naoh(repaired)
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
    print(f"{action} {changed_count} NBRC 937 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
