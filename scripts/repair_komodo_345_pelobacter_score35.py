#!/usr/bin/env python3
"""Repair KOMODO 345 Pelobacter acetylenicus Medium."""

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

KOMODO_345 = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=345"
)
TOGO_M1791 = "https://togomedium.org/medium/M1791"
NBRC_1016 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1016"

SOURCE_NBRC_1016 = "NBRC Medium 1016"

CURATOR = "repair_komodo_345_pelobacter_score35.py"
ACTION = "RESOLVED_KOMODO_345_PELOBACTER_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "L": "L",
    "VARIABLE": "variable",
}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "incubation_atmosphere",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    recipe: dict[str, Any]
    references: tuple[str, ...]
    notes: str
    accepted_signatures: frozenset[frozenset[str]]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str = SOURCE_NBRC_1016,
    notes: str | None = None,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


def _solution(
    preferred_term: str,
    value: str,
    *,
    notes: str,
    composition: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": SOURCE_NBRC_1016,
        "notes": notes,
        "composition": copy.deepcopy(composition),
    }


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str],
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        notes=f"{SOURCE_NBRC_1016} prints this component in the SL-10 stock.",
        term=term,
    )


def _sl10_trace_elements() -> list[dict[str, Any]]:
    return [
        _stock_component("HCl (25%; 7.7 M)", "10", "ML_PER_L", term=("CHEBI:17883", "hydrogen chloride")),
        _stock_component("FeCl2 x 4H2O", "1.5", "G_PER_L", term=("CHEBI:86249", "iron dichloride tetrahydrate")),
        _stock_component("ZnCl2", "70", "MG_PER_L", term=("CHEBI:49976", "zinc dichloride")),
        _stock_component("MnCl2 x 4H2O", "100", "MG_PER_L", term=("CHEBI:86368", "manganese(II) chloride tetrahydrate")),
        _stock_component("H3BO3", "6", "MG_PER_L", term=("CHEBI:33118", "boric acid")),
        _stock_component("CoCl2 x 6H2O", "190", "MG_PER_L", term=("CHEBI:53503", "cobalt chloride hexahydrate")),
        _stock_component("CuCl2 x 2H2O", "2", "MG_PER_L", term=("CHEBI:86318", "copper(II) chloride dihydrate")),
        _stock_component("NiCl2 x 6H2O", "24", "MG_PER_L", term=("CHEBI:53542", "nickel chloride hexahydrate")),
        _stock_component("Na2MoO4 x 2H2O", "36", "MG_PER_L", term=("CHEBI:75213", "sodium molybdate dihydrate")),
        _stock_component("Distilled water", "990", "ML_PER_L", term=("CHEBI:15377", "water")),
    ]


def _pelobacter_recipe() -> dict[str, Any]:
    return {
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.2,
        "incubation_atmosphere": "ANAEROBIC",
        "ingredients": [
            _component("Distilled water", "1.0", "L", term=("CHEBI:15377", "water")),
            _component(
                "KH2PO4",
                "0.2",
                "G_PER_L",
                term=("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _component(
                "NH4Cl",
                "0.25",
                "G_PER_L",
                term=("CHEBI:31206", "ammonium chloride"),
            ),
            _component("NaCl", "1.0", "G_PER_L", term=("CHEBI:26710", "sodium chloride")),
            _component(
                "MgCl2 x 6H2O",
                "0.4",
                "G_PER_L",
                term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
            ),
            _component("KCl", "0.5", "G_PER_L", term=("CHEBI:32588", "potassium chloride")),
            _component(
                "CaCl2 x 2H2O",
                "0.15",
                "G_PER_L",
                term=("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _component("Resazurin", "1", "MG_PER_L", term=("CHEBI:8806", "Resazurin")),
            _component(
                "NaHCO3",
                "2.5",
                "G_PER_L",
                term=("CHEBI:32139", "sodium hydrogencarbonate"),
            ),
            _component("Acetoin", "1.0", "G_PER_L", term=("CHEBI:15688", "acetoin")),
            _component(
                "CO2",
                "variable",
                "VARIABLE",
                notes=(
                    "NBRC Medium 1016 dispenses the medium under an N2/CO2 "
                    "gas stream at 80:20 by volume."
                ),
                term=("CHEBI:16526", "carbon dioxide"),
            ),
            _component(
                "N2",
                "variable",
                "VARIABLE",
                notes=(
                    "NBRC Medium 1016 dispenses the medium under an N2/CO2 "
                    "gas stream at 80:20 by volume."
                ),
                term=("CHEBI:17997", "dinitrogen"),
            ),
        ],
        "solutions": [
            _solution(
                "Trace element solution SL-10",
                "1",
                notes="NBRC Medium 1016 adds 1 ml/L Trace element solution SL-10.",
                composition=_sl10_trace_elements(),
            ),
            _solution(
                "3.6% Na2S x 9H2O solution",
                "10",
                notes=(
                    "NBRC Medium 1016 autoclaves Na2S x 9H2O separately as a "
                    "3.6% anoxic stock solution for a 0.36 g/L final amount."
                ),
                composition=[
                    _component(
                        "Na2S x 9H2O",
                        "36",
                        "G_PER_L",
                        notes=(
                            "NBRC Medium 1016 lists Na2S x 9H2O as a 3.6% "
                            "separately autoclaved solution."
                        ),
                        term=("CHEBI:76209", "sodium sulfide nonahydrate"),
                    )
                ],
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Mix all ingredients except Acetoin and Na2S x 9H2O, "
                    "including 1 ml/L Trace element solution SL-10."
                ),
            },
            {
                "step_number": 2,
                "action": "MIX",
                "description": (
                    "Dispense the medium into suitable culture vessels under "
                    "an N2/CO2 gas stream at 80:20 by volume and seal with "
                    "butyl rubber stoppers."
                ),
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": (
                    "Autoclave the dispensed medium, and separately autoclave "
                    "the 3.6% Na2S x 9H2O solution under an N2 atmosphere."
                ),
            },
            {
                "step_number": 4,
                "action": "FILTER_STERILIZE",
                "description": "Prepare a filter-sterile Acetoin solution.",
            },
            {
                "step_number": 5,
                "action": "MIX",
                "description": (
                    "Aseptically and anaerobically add the sterile Na2S x 9H2O "
                    "solution, and add filter-sterile Acetoin just before "
                    "inoculation."
                ),
            },
            {
                "step_number": 6,
                "action": "ADJUST_PH",
                "description": "Adjust the complete medium to pH 7.2.",
            },
        ],
    }


def _signature(recipe: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in recipe.get(key, [])
        if isinstance(row, dict)
    )


PELOBACTER_RECIPE = _pelobacter_recipe()

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/pelobacter_acetylenicus_medium.yaml",
        record_id="CultureMech:005057",
        source_term="komodo.medium:345",
        recipe=PELOBACTER_RECIPE,
        references=(KOMODO_345, TOGO_M1791, NBRC_1016),
        notes=(
            "NBRC Medium 1016 records Pelobacter acetylenicus Medium as a "
            "defined freshwater medium with acetoin, Trace element solution "
            "SL-10, a separately autoclaved 3.6% Na2S x 9H2O solution, an "
            "80:20 N2/CO2 gas phase, and pH 7.2."
        ),
        accepted_signatures=frozenset({frozenset(), _signature(PELOBACTER_RECIPE)}),
    ),
)
TARGET_BY_PATH: dict[str, Target] = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _top_level_signature(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in doc.get(key) or []
        if isinstance(row, dict)
    )


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, "
            f"found {source_term!r}"
        )

    if _top_level_signature(doc) not in target.accepted_signatures:
        raise ValueError(f"{target.path}: component signature drifted")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": target.notes,
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

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = target.notes
    repaired["data_quality_flags"] = ["has_ontology_mappings", "ingredients_curated"]
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
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
