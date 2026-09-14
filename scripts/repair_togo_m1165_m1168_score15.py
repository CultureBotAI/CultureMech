#!/usr/bin/env python3
"""Repair TOGO M1165-M1168 Bicarbonate Buffered Medium records."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1165_m1168_score15.py"
ACTION = "RESOLVED_TOGO_M1165_M1168_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M180 = "https://togomedium.org/medium/M180"
TOGO_M190 = "https://togomedium.org/medium/M190"
TOGO_M431 = "https://togomedium.org/medium/M431"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"
JCM_1095 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1095"

SOURCE = "JCM Medium 1095"
TITLE = "Bicarbonate Buffered Medium"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term: str
    togo_url: str
    imported_substrate: str
    substrate_solution: str
    substrate: str


TARGETS: tuple[Target, ...] = (
    Target(
        Path("bacterial/TOGO_M1165_Bicarbonate_Buffered_Medium.yaml"),
        "CultureMech:007689",
        "TOGO:M1165",
        "https://togomedium.org/medium/M1165",
        "glycerin solution",
        "1 M glycerin solution",
        "Glycerol",
    ),
    Target(
        Path("bacterial/TOGO_M1166_Bicarbonate_Buffered_Medium.yaml"),
        "CultureMech:007690",
        "TOGO:M1166",
        "https://togomedium.org/medium/M1166",
        "glycerin solution",
        "1 M glycerin solution",
        "Glycerol",
    ),
    Target(
        Path("bacterial/TOGO_M1167_Bicarbonate_Buffered_Medium.yaml"),
        "CultureMech:007691",
        "TOGO:M1167",
        "https://togomedium.org/medium/M1167",
        "trisodium citrate solution",
        "1 M trisodium citrate solution",
        "Trisodium citrate",
    ),
    Target(
        Path("bacterial/TOGO_M1168_Bicarbonate_Buffered_Medium.yaml"),
        "CultureMech:007692",
        "TOGO:M1168",
        "https://togomedium.org/medium/M1168",
        "maltose solution",
        "1 M maltose solution",
        "Maltose",
    ),
)

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "930", "G_PER_L"),
    ("Yeast extract", "0.1", "G_PER_L"),
    ("NaCl", "0.3", "G_PER_L"),
    ("KH2PO4", "0.41", "G_PER_L"),
    ("NH4Cl", "0.3", "G_PER_L"),
    ("Resazurin", "0.5", "G_PER_L"),
    ("Na2HPO4・2H2O", "0.53", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Na2HPO4 x 2H2O", "0.53", "G_PER_L"),
    ("KH2PO4", "0.41", "G_PER_L"),
    ("NH4Cl", "0.3", "G_PER_L"),
    ("NaCl", "0.3", "G_PER_L"),
    ("Yeast extract", "0.1", "G_PER_L"),
    ("Resazurin", "0.5", "MG_PER_L"),
    ("Distilled water", "930.0", "ML_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
)

IMPORTED_COMMON_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("FeCl2 solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Trace element solution (see Medium [M180])", "1", "G_PER_L", ()),
    ("Selenite--tungstate solution (see Medium [M431])", "0.5", "G_PER_L", ()),
    ("8% NaHCO3 solution*", "50", "G_PER_L", ()),
    ("10% CaCl2・2H2O solution", "1", "G_PER_L", ()),
    ("10% MgCl2・6H2O solution", "1", "G_PER_L", ()),
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("Substrate solution (see below)", "10", "G_PER_L", ()),
    ("5% Na2S・9H2O solution", "10", "G_PER_L", ()),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "CoCl2 x 6H2O": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper(II) chloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "FeCl2 x 4H2O": ("CHEBI:86249", "iron dichloride tetrahydrate"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glycerol": ("CHEBI:17754", "glycerol"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HCl": ("CHEBI:17883", "hydrogen chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "Maltose": ("CHEBI:18167", "alpha-maltose"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2HPO4 x 2H2O": ("CHEBI:91258", "disodium hydrogenphosphate dihydrate"),
    "Na2MoO4 x 2H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2SeO3 x 5H2O": ("CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2WO4 x 2H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaOH": ("CHEBI:32145", "sodium hydroxide"),
    "NiCl2 x 6H2O": ("CHEBI:53542", "nickel chloride hexahydrate"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Trisodium citrate": ("CHEBI:53258", "sodium citrate"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "L": "L",
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


def _stock(
    preferred_term: str,
    value: str,
    composition: list[dict[str, Any]],
    *,
    source: str = SOURCE,
    notes: str,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": composition,
    }
    if preparation_notes is not None:
        row["preparation_notes"] = preparation_notes
    return row


def _percent_stock(preferred_term: str, value: str, solute: str, percent: str) -> dict[str, Any]:
    return _stock(
        preferred_term,
        value,
        [
            _component(
                solute,
                percent,
                "PERCENT_W_V",
                source=SOURCE,
                notes=(
                    f"{preferred_term} is represented from the stock label as "
                    f"{percent}% w/v {solute}."
                ),
            )
        ],
        notes=f"JCM Medium 1095 adds {value} ml/L {preferred_term}.",
    )


def _molar_stock(target: Target) -> dict[str, Any]:
    return _stock(
        target.substrate_solution,
        "10.0",
        [
            _component(
                target.substrate,
                "1.0",
                "MOLAR",
                source=SOURCE,
                notes=(
                    f"JCM Medium 1095 lists {target.substrate_solution} as a "
                    "Substrate solution option."
                ),
            )
        ],
        notes=(
            "JCM Medium 1095 adds 10.0 ml/L Substrate solution and lists "
            f"{target.substrate_solution} as this substrate option."
        ),
    )


def _gas(preferred_term: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=SOURCE,
        notes="JCM Medium 1095 uses an N2-CO2 (4:1, v/v) gas mixture.",
    )


def _ingredients() -> list[dict[str, Any]]:
    return [
        _listed_component("Na2HPO4 x 2H2O", "0.53", "G_PER_L", source=SOURCE),
        _listed_component("KH2PO4", "0.41", "G_PER_L", source=SOURCE),
        _listed_component("NH4Cl", "0.3", "G_PER_L", source=SOURCE),
        _listed_component("NaCl", "0.3", "G_PER_L", source=SOURCE),
        _listed_component("Yeast extract", "0.1", "G_PER_L", source=SOURCE, term=False),
        _listed_component("Resazurin", "0.5", "MG_PER_L", source=SOURCE),
        _listed_component("Distilled water", "930.0", "ML_PER_L", source=SOURCE),
        _gas("Carbon dioxide gas"),
        _gas("Nitrogen gas"),
    ]


def _fecl2_solution() -> dict[str, Any]:
    source = "JCM Medium 187"
    return _stock(
        "FeCl2 solution",
        "1.0",
        [
            _listed_component("HCl", "10.0", "ML_PER_L", source=source),
            _listed_component("FeCl2 x 4H2O", "1.5", "G_PER_L", source=source),
            _listed_component("Distilled water", "990.0", "ML_PER_L", source=source),
        ],
        notes="JCM Medium 1095 adds 1.0 ml/L FeCl2 solution from JCM Medium 187.",
        preparation_notes="JCM Medium 187 prepares the stock with 25% HCl (7.7 M).",
    )


def _jcm_187_trace_elements() -> dict[str, Any]:
    source = "JCM Medium 187"
    return _stock(
        "Trace element solution",
        "1.0",
        [
            _listed_component("ZnCl2", "70.0", "MG_PER_L", source=source),
            _listed_component("MnCl2 x 4H2O", "100.0", "MG_PER_L", source=source),
            _listed_component("H3BO3", "6.0", "MG_PER_L", source=source),
            _listed_component("CoCl2 x 6H2O", "190.0", "MG_PER_L", source=source),
            _listed_component("CuCl2 x 2H2O", "2.0", "MG_PER_L", source=source),
            _listed_component("NiCl2 x 6H2O", "24.0", "MG_PER_L", source=source),
            _listed_component("Na2MoO4 x 2H2O", "36.0", "MG_PER_L", source=source),
            _listed_component("Distilled water", "1.0", "L", source=source),
        ],
        notes=("JCM Medium 1095 adds 1.0 ml/L Trace element solution from " "JCM Medium 187."),
    )


def _selenite_tungstate() -> dict[str, Any]:
    source = "JCM Medium 431"
    return _stock(
        "Selenite-tungstate solution",
        "0.5",
        [
            _listed_component("NaOH", "0.4", "G_PER_L", source=source),
            _listed_component("Na2SeO3 x 5H2O", "6.0", "MG_PER_L", source=source),
            _listed_component("Na2WO4 x 2H2O", "8.0", "MG_PER_L", source=source),
            _listed_component("Distilled water", "1.0", "L", source=source),
        ],
        notes=("JCM Medium 1095 adds 0.5 ml/L Selenite-tungstate solution from " "JCM Medium 431."),
    )


def _trace_vitamins() -> dict[str, Any]:
    source = "JCM Medium 197"
    return _stock(
        "Trace vitamins",
        "10.0",
        [
            _listed_component("Biotin", "2.0", "MG_PER_L", source=source),
            _listed_component("Folic acid", "2.0", "MG_PER_L", source=source),
            _listed_component("Pyridoxine HCl", "10.0", "MG_PER_L", source=source),
            _listed_component("Thiamine HCl", "5.0", "MG_PER_L", source=source),
            _listed_component("Riboflavin", "5.0", "MG_PER_L", source=source),
            _listed_component("Nicotinic acid", "5.0", "MG_PER_L", source=source),
            _listed_component("Calcium pantothenate", "5.0", "MG_PER_L", source=source),
            _listed_component("Vitamin B12", "0.1", "MG_PER_L", source=source),
            _listed_component("p-Aminobenzoic acid", "5.0", "MG_PER_L", source=source),
            _listed_component("Lipoic acid", "5.0", "MG_PER_L", source=source),
            _listed_component("Distilled water", "1.0", "L", source=source),
        ],
        notes="JCM Medium 1095 adds 10.0 ml/L filter-sterilized Trace vitamins.",
        preparation_notes="JCM Medium 1095 marks Trace vitamins as filter-sterilized.",
    )


def _solutions(target: Target) -> list[dict[str, Any]]:
    nahco3 = _percent_stock("8% NaHCO3 solution", "50.0", "NaHCO3", "8.0")
    nahco3["preparation_notes"] = "Filter-sterilize before adding after cooling."

    return [
        _fecl2_solution(),
        _jcm_187_trace_elements(),
        _selenite_tungstate(),
        _percent_stock("10% MgCl2 x 6H2O solution", "1.0", "MgCl2 x 6H2O", "10.0"),
        _percent_stock("10% CaCl2 x 2H2O solution", "1.0", "CaCl2 x 2H2O", "10.0"),
        _trace_vitamins(),
        nahco3,
        _molar_stock(target),
        _percent_stock("5% Na2S x 9H2O solution", "10.0", "Na2S x 9H2O", "5.0"),
    ]


PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Mix the salts, yeast extract, Resazurin, FeCl2 solution, Trace "
            "element solution, Selenite-tungstate solution, and distilled water."
        ),
    },
    {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave the base medium under an N2-CO2 (4:1, v/v) gas mixture.",
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": (
            "After cooling, add MgCl2, CaCl2, Trace vitamins, NaHCO3, and " "Substrate solutions."
        ),
    },
    {
        "step_number": 4,
        "action": "ALIQUOT",
        "description": (
            "Aseptically and anaerobically distribute medium into culture "
            "vessels under N2-CO2 (4:1, v/v) and seal with butyl rubber stoppers."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "Prior to use, add 10.0 ml/L 5% Na2S x 9H2O solution autoclaved " "and stored under N2."
        ),
    },
)

NOTES = (
    "TOGO {media_number} records JCM Medium 1095 with a bicarbonate-buffered "
    "base containing FeCl2 and Trace element stocks from JCM Medium 187, "
    "Selenite-tungstate solution from JCM Medium 431, filter-sterilized "
    "Trace vitamins from JCM Medium 197, filter-sterilized 8% NaHCO3, "
    "10% MgCl2 x 6H2O, 10% CaCl2 x 2H2O, 5% Na2S x 9H2O, "
    "{substrate}, and an N2-CO2 (4:1, v/v) gas phase."
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


def _imported_solution_signatures(target: Target) -> tuple[SolutionSignature, ...]:
    return IMPORTED_COMMON_SOLUTIONS + ((target.imported_substrate, "variable", "VARIABLE", ()),)


def _final_solution_signatures(target: Target) -> tuple[SolutionSignature, ...]:
    return _solution_signatures({"solutions": _solutions(target)})


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term:
        raise ValueError(f"{target.path}: expected media term {target.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (IMPORTED_INGREDIENT_SIGNATURE, FINAL_INGREDIENT_SIGNATURE):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        _imported_solution_signatures(target),
        _final_solution_signatures(target),
    ):
        raise ValueError(f"{target.path}: solution signature drifted")


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


def _references(target: Target) -> tuple[str, ...]:
    return (target.togo_url, JCM_1095, TOGO_M180, JCM_187, TOGO_M431, JCM_431, TOGO_M190, JCM_197)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in _references(target):
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(_references(target)),
        "notes": notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    notes = NOTES.format(
        media_number=target.media_term.removeprefix("TOGO:"),
        substrate=target.substrate_solution,
    )
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired["ingredients"] = _ingredients()
    repaired["solutions"] = _solutions(target)
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(
        repaired,
        "sterilization",
        {
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": (
                "Autoclave the base under N2-CO2; filter-sterilize Trace vitamins "
                "and NaHCO3 before adding after cooling."
            ),
        },
        "preparation_steps",
    )
    _put_after(repaired, "notes", notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target, notes)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
    }


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
