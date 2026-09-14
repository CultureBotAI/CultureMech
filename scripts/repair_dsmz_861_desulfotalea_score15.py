#!/usr/bin/env python3
"""Repair the DSMZ/KOMODO 861 Desulfotalea psychrophila stock-solution family."""

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

DSMZ_861 = "bacterial/desulfofrigus_medium.yaml"
DSMZ_861A = "bacterial/desulfotalea_psychrophila_medium.yaml"
KOMODO_861 = "bacterial/srb_psychrophile_medium.yaml"
KOMODO_861_1 = "bacterial/for_dsm_12343.yaml"
KOMODO_861_2 = "bacterial/for_dsm_12341.yaml"
KOMODO_861_3 = "bacterial/for_dsm_12342_dsm_12343_and_dsm_12345.yaml"
KOMODO_861_4 = "bacterial/for_dsm_12344.yaml"

EXPECTED_IDS = {
    DSMZ_861: "CultureMech:002020",
    DSMZ_861A: "CultureMech:002021",
    KOMODO_861: "CultureMech:006692",
    KOMODO_861_1: "CultureMech:006688",
    KOMODO_861_2: "CultureMech:006689",
    KOMODO_861_3: "CultureMech:006690",
    KOMODO_861_4: "CultureMech:006691",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_861: "mediadive.medium:861",
    DSMZ_861A: "mediadive.medium:861a",
    KOMODO_861: "komodo.medium:861",
    KOMODO_861_1: "komodo.medium:861.1",
    KOMODO_861_2: "komodo.medium:861.2",
    KOMODO_861_3: "komodo.medium:861.3",
    KOMODO_861_4: "komodo.medium:861.4",
}

DSMZ_861_REST = "https://mediadive.dsmz.de/rest/medium/861"
DSMZ_861A_REST = "https://mediadive.dsmz.de/rest/medium/861a"
DSMZ_861_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium861.pdf"
DSMZ_861A_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium861a.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_dsmz_861_desulfotalea_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_861_DESULFOTALEA_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
    "data_quality_flags",
    "references",
)


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    notes: str
    solution_profile: str
    solution_c: str = "lactate"
    ph_range: dict[str, float] | None = None
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()
    extra_references: tuple[str, ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _compound(
    preferred_term: str,
    value: str,
    mediadive_id: int | None,
    mediadive_label: str | None,
    chebi_id: str,
    chebi_label: str,
    source: str,
    unit: str = "G_PER_L",
) -> dict[str, Any]:
    row = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {unit} {preferred_term}.",
        "mediaingredientmech_chebi_term": _term(chebi_id, chebi_label),
    }
    if mediadive_id is not None and mediadive_label is not None:
        row["term"] = _term(f"mediadive.compound:{mediadive_id}", mediadive_label)
    return row


def _water(value: str, source: str) -> dict[str, Any]:
    return _compound(
        "Distilled water",
        value,
        4,
        "Distilled water",
        "CHEBI:15377",
        "water",
        source,
        "ML_PER_L",
    )


def _solution(
    preferred_term: str,
    value: str,
    source: str,
    *,
    mediadive_id: int,
    composition: tuple[dict[str, Any], ...] = (),
    solutions: tuple[dict[str, Any], ...] = (),
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes or f"{source} adds {value} ml/L {preferred_term}.",
        "term": _term(f"mediadive.solution:{mediadive_id}", preferred_term),
    }
    if composition:
        row["composition"] = [copy.deepcopy(component) for component in composition]
    if solutions:
        row["solutions"] = [copy.deepcopy(solution) for solution in solutions]
    return row


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


DSMZ_861_CHILD = _recipe_ref(
    KOMODO_861,
    "SOURCE_DUPLICATE",
    "KOMODO Medium 861 cites the DSMZ Medium 861 SRB-psychrophile formulation.",
)
DSMZ_861_PARENT = _recipe_ref(
    DSMZ_861,
    "SOURCE_DUPLICATE",
    "DSMZ Medium 861 is the official SRB-psychrophile source formulation.",
)
DSMZ_861A_12341_CHILD = _recipe_ref(
    KOMODO_861_2,
    "SUBSTITUTED_COMPONENT_VARIANT",
    "KOMODO Medium 861.2 applies the Desulfotalea base to DSM 12341 with acetate as the substrate.",
)
DSMZ_861A_12342_CHILD = _recipe_ref(
    KOMODO_861_3,
    "STRAIN_SPECIFIC_VARIANT",
    "KOMODO Medium 861.3 applies the Desulfotalea base to DSM 12342, DSM 12343, and DSM 12345.",
)
DSMZ_861A_12343_CHILD = _recipe_ref(
    KOMODO_861_1,
    "PH_VARIANT",
    "KOMODO Medium 861.1 applies the Desulfotalea base to DSM 12343 at pH 7.1-7.3.",
)
DSMZ_861A_12344_CHILD = _recipe_ref(
    KOMODO_861_4,
    "SUBSTITUTED_COMPONENT_VARIANT",
    "KOMODO Medium 861.4 applies the Desulfotalea base to DSM 12344 with propionate as the substrate.",
)
DSMZ_861A_PARENT = _recipe_ref(
    DSMZ_861A,
    "STRAIN_SPECIFIC_VARIANT",
    "DSMZ Medium 861a is the official low-salt Desulfotalea psychrophila stock-solution formulation.",
)

BASE = {
    "CaCl2 x 2 H2O": (7, "CaCl2 x 2 H2O", "CHEBI:86158", "calcium chloride dihydrate"),
    "CoCl2 x 6 H2O": (38, "CoCl2 x 6 H2O", "CHEBI:53503", "cobalt chloride hexahydrate"),
    "CuCl2 x 2 H2O": (39, "CuCl2 x 2 H2O", "CHEBI:86318", "copper(II) chloride dihydrate"),
    "FeCl2 x 4 H2O": (260, "FeCl2 x 4 H2O", "CHEBI:86249", "iron dichloride tetrahydrate"),
    "H3BO3": (37, "H3BO3", "CHEBI:33118", "boric acid"),
    "HCl": (68, "HCl", "CHEBI:17883", "hydrogen chloride"),
    "KBr": (174, "KBr", "CHEBI:32030", "potassium bromide"),
    "KCl": (61, "KCl", "CHEBI:32588", "potassium chloride"),
    "KH2PO4": (11, "KH2PO4", "CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgCl2 x 6 H2O": (79, "MgCl2 x 6 H2O", "CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MnCl2 x 4 H2O": (36, "MnCl2 x 4 H2O", "CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "NH4Cl": (42, "NH4Cl", "CHEBI:31206", "ammonium chloride"),
    "Na2CO3": (32, "Na2CO3", "CHEBI:29377", "sodium carbonate"),
    "Na2MoO4 x 2 H2O": (9, "Na2MoO4 x 2 H2O", "CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2S x 9 H2O": (54, "Na2S x 9 H2O", "CHEBI:76209", "sodium sulfide nonahydrate"),
    "Na2S2O4": (653, "Na2S2O4", "CHEBI:66870", "sodium dithionite"),
    "Na2SeO3 x 5 H2O": (107, "Na2SeO3 x 5 H2O", "CHEBI:131361", "disodium selenite pentahydrate"),
    "Na2SO4": (110, "Na2SO4", "CHEBI:32149", "sodium sulfate"),
    "Na2WO4 x 2 H2O": (249, "Na2WO4 x 2 H2O", "CHEBI:63939", "sodium tungstate dihydrate"),
    "Na-DL-lactate": (111, "Na-DL-lactate", "CHEBI:75228", "sodium lactate"),
    "Na-acetate": (None, None, "CHEBI:32954", "sodium acetate"),
    "Na-propionate": (None, None, "CHEBI:132106", "sodium propionate"),
    "NaCl": (43, "NaCl", "CHEBI:26710", "sodium chloride"),
    "NaOH": (256, "NaOH", "CHEBI:32145", "sodium hydroxide"),
    "NiCl2 x 6 H2O": (40, "NiCl2 x 6 H2O", "CHEBI:34887", "nickel dichloride"),
    "Sodium resazurin": (1852, "Sodium resazurin", "CHEBI:8806", "Resazurin"),
    "Vitamin B12": (18, "Vitamin B12", "CHEBI:176843", "vitamin B12"),
    "Biotin": (46, "Biotin", "CHEBI:15956", "biotin"),
    "Calcium D-(+)-pantothenate": (
        1512,
        "Calcium D-(+)-pantothenate",
        "CHEBI:31345",
        "Calcium pantothenate",
    ),
    "Folic acid": (138, "Folic acid", "CHEBI:27470", "folic acid"),
    "Nicotinic acid": (139, "Nicotinic acid", "CHEBI:15940", "nicotinic acid"),
    "Pyridoxine hydrochloride": (
        519,
        "Pyridoxine hydrochloride",
        "CHEBI:30961",
        "pyridoxine hydrochloride",
    ),
    "Riboflavin": (136, "Riboflavin", "CHEBI:17015", "riboflavin"),
    "Thiamine HCl": (1207, "Thiamine HCl", "CHEBI:49105", "thiamine hydrochloride"),
    "p-Aminobenzoic acid": (47, "p-Aminobenzoic acid", "CHEBI:30753", "4-aminobenzoic acid"),
    "(DL)-alpha-Lipoic acid": (252, "(DL)-alpha-Lipoic acid", "CHEBI:16494", "lipoic acid"),
    "ZnCl2": (64, "ZnCl2", "CHEBI:49976", "zinc dichloride"),
}


def _c(name: str, value: str, source: str) -> dict[str, Any]:
    return _compound(name, value, *BASE[name], source)


def _stock_solutions(source: str, profile: str, solution_c: str) -> tuple[dict[str, Any], ...]:
    a_values = {
        "861": {
            "NaCl": "21.0084",
            "Na2SO4": "4.20168",
            "KH2PO4": "0.210084",
            "NH4Cl": "0.262605",
            "MgCl2 x 6 H2O": "3.15126",
            "CaCl2 x 2 H2O": "0.157563",
            "KBr": "0.0945378",
            "KCl": "0.52521",
            "Sodium resazurin": "0.00052521",
            "water": "997.899",
            "solution_a": 1761,
        },
        "861a": {
            "NaCl": "10.6157",
            "Na2SO4": "4.24628",
            "KH2PO4": "0.212314",
            "NH4Cl": "0.265393",
            "MgCl2 x 6 H2O": "3.18471",
            "CaCl2 x 2 H2O": "0.159236",
            "KBr": "0.0955414",
            "KCl": "0.530786",
            "Sodium resazurin": "0.000530786",
            "water": "997.877",
            "solution_a": 1771,
        },
    }[profile]

    trace = _solution(
        "Trace element solution SL-10",
        "1.05042" if profile == "861" else "1.06157",
        source,
        mediadive_id=595,
        composition=(
            _c("HCl", "2.5", source),
            _c("FeCl2 x 4 H2O", "1.5", source),
            _c("ZnCl2", "0.07", source),
            _c("MnCl2 x 4 H2O", "0.1", source),
            _c("H3BO3", "0.006", source),
            _c("CoCl2 x 6 H2O", "0.19", source),
            _c("CuCl2 x 2 H2O", "0.002", source),
            _c("NiCl2 x 6 H2O", "0.024", source),
            _c("Na2MoO4 x 2 H2O", "0.036", source),
            _water("990", source),
        ),
        notes=f"{source} Solution A adds 1 ml/L Trace element solution SL-10.",
    )
    selenite = _solution(
        "Selenite-tungstate solution",
        "1.05042" if profile == "861" else "1.06157",
        source,
        mediadive_id=777,
        composition=(
            _c("NaOH", "0.5", source),
            _c("Na2SeO3 x 5 H2O", "0.003", source),
            _c("Na2WO4 x 2 H2O", "0.004", source),
            _water("1000", source),
        ),
        notes=f"{source} Solution A adds 1 ml/L Selenite-tungstate solution.",
    )
    solution_a = _solution(
        "Solution A",
        "948.207",
        source,
        mediadive_id=a_values["solution_a"],
        composition=(
            _c("NaCl", a_values["NaCl"], source),
            _c("Na2SO4", a_values["Na2SO4"], source),
            _c("KH2PO4", a_values["KH2PO4"], source),
            _c("NH4Cl", a_values["NH4Cl"], source),
            _c("MgCl2 x 6 H2O", a_values["MgCl2 x 6 H2O"], source),
            _c("CaCl2 x 2 H2O", a_values["CaCl2 x 2 H2O"], source),
            _c("KBr", a_values["KBr"], source),
            _c("KCl", a_values["KCl"], source),
            _c("Sodium resazurin", a_values["Sodium resazurin"], source),
            _water(a_values["water"], source),
        ),
        solutions=(trace, selenite),
        notes=f"{source} adds 952 ml/L Solution A to the completed 861-family medium.",
    )

    c_components = {
        "lactate": (_c("Na-DL-lactate", "250", source), _water("1000", source)),
        "acetate": (_c("Na-acetate", "150", source), _water("1000", source)),
        "propionate": (_c("Na-propionate", "150", source), _water("1000", source)),
    }[solution_c]

    wolin = _solution(
        "Wolin's vitamin solution (10x)",
        "1000",
        source,
        mediadive_id=5980,
        composition=(
            _c("Biotin", "0.02", source),
            _c("Folic acid", "0.02", source),
            _c("Pyridoxine hydrochloride", "0.1", source),
            _c("Thiamine HCl", "0.05", source),
            _c("Riboflavin", "0.05", source),
            _c("Nicotinic acid", "0.05", source),
            _c("Calcium D-(+)-pantothenate", "0.05", source),
            _c("Vitamin B12", "0.001", source),
            _c("p-Aminobenzoic acid", "0.05", source),
            _c("(DL)-alpha-Lipoic acid", "0.05", source),
            _water("1000", source),
        ),
        notes=f"{source} Solution D consists of Wolin's vitamin solution.",
    )
    dithionite = _solution(
        "Na-dithionite solution (5% w/v)",
        "1000",
        source,
        mediadive_id=6262,
        composition=(
            _compound(
                "NaOH", "50", 256, "NaOH", "CHEBI:32145", "sodium hydroxide", source, "ML_PER_L"
            ),
            _c("Na2S2O4", "50", source),
            _water("950", source),
        ),
        notes=f"{source} Solution F consists of 5% w/v Na-dithionite solution.",
    )

    b_id = 1764 if profile == "861" else 1774
    c_id = 1766 if profile == "861" else 1776
    d_id = 1765 if profile == "861" else 1775
    e_id = 1767 if profile == "861" else 1777
    f_id = 1768 if profile == "861" else 1778
    return (
        solution_a,
        _solution(
            "Solution B",
            "29.8805",
            source,
            mediadive_id=b_id,
            composition=(_c("Na2CO3", "50", source), _water("1000", source)),
        ),
        _solution("Solution C", "9.96016", source, mediadive_id=c_id, composition=c_components),
        _solution("Solution D", "0.996016", source, mediadive_id=d_id, solutions=(wolin,)),
        _solution(
            "Solution E",
            "9.96016",
            source,
            mediadive_id=e_id,
            composition=(_c("Na2S x 9 H2O", "30", source), _water("1000", source)),
        ),
        _solution("Solution F", "0.996016", source, mediadive_id=f_id, solutions=(dithionite,)),
    )


def _steps(source: str) -> tuple[dict[str, Any], ...]:
    return (
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                f"{source} sparges Solution A with an 80% N2 and 20% CO2 gas "
                "mixture to pH below 6, dispenses it under the same gas "
                "atmosphere into serum vials, and autoclaves it."
            ),
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": (
                f"{source} prepares Solutions B and F under 80% N2 and 20% CO2 "
                "and prepares sterile Solutions C, D, and E under 100% N2; "
                "Solutions D and F are sterilized by filtration."
            ),
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": (
                f"{source} completes the medium by adding appropriate amounts "
                "of Solutions B to F to sterile Solution A in sequence."
            ),
        },
        {
            "step_number": 4,
            "action": "ADJUST_PH",
            "description": f"{source} final pH should be 7.0-7.2.",
        },
    )


TARGETS: tuple[Target, ...] = (
    Target(
        path=DSMZ_861,
        source_label="DSMZ Medium 861",
        source_url=DSMZ_861_REST,
        notes=(
            "MediaDive and DSMZ Medium 861 define Desulfofrigus Medium as a "
            "six-stock anoxic SRB-psychrophile medium, with NaCl-rich Solution A "
            "combined with carbonate, lactate, vitamin, sulfide, and dithionite stocks."
        ),
        solution_profile="861",
        ph_range={"min": 7.0, "max": 7.2},
        extra_references=(DSMZ_861_PDF,),
        variant_children=(DSMZ_861_CHILD,),
    ),
    Target(
        path=DSMZ_861A,
        source_label="DSMZ Medium 861a",
        source_url=DSMZ_861A_REST,
        notes=(
            "MediaDive and DSMZ Medium 861a define Desulfotalea psychrophila "
            "Medium as the lower-NaCl Desulfofrigus 861 stock-solution recipe."
        ),
        solution_profile="861a",
        ph_range={"min": 7.0, "max": 7.2},
        extra_references=(DSMZ_861A_PDF,),
        variant_children=(
            DSMZ_861A_12341_CHILD,
            DSMZ_861A_12342_CHILD,
            DSMZ_861A_12343_CHILD,
            DSMZ_861A_12344_CHILD,
        ),
    ),
    Target(
        path=KOMODO_861,
        source_label="KOMODO Medium 861",
        source_url=f"{KOMODO_BASE}861",
        notes="KOMODO Medium 861 cites the DSMZ Medium 861 SRB-Psychrophile Medium formulation.",
        solution_profile="861",
        parent_media=DSMZ_861_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=("KOMODO source-catalogue duplicate of DSMZ Medium 861.",),
        extra_references=(DSMZ_861_REST, DSMZ_861_PDF),
    ),
    Target(
        path=KOMODO_861_2,
        source_label="KOMODO Medium 861.2",
        source_url=f"{KOMODO_BASE}861.2",
        notes=(
            "KOMODO Medium 861.2 records the DSM 12341 Desulfotalea formulation "
            "with a 150 g/L Na-acetate substrate stock in place of the lactate stock."
        ),
        solution_profile="861a",
        solution_c="acetate",
        parent_media=DSMZ_861A_PARENT,
        variant_relationship="SUBSTITUTED_COMPONENT_VARIANT",
        variant_modifications=(
            "Replaces the 250 g/L Na-DL-lactate Solution C with 150 g/L Na-acetate.",
        ),
        extra_references=(DSMZ_861A_REST, DSMZ_861A_PDF),
    ),
    Target(
        path=KOMODO_861_3,
        source_label="KOMODO Medium 861.3",
        source_url=f"{KOMODO_BASE}861.3",
        notes=(
            "KOMODO Medium 861.3 applies the low-salt Desulfotalea formulation "
            "to DSM 12342, DSM 12343, and DSM 12345 with the lactate stock."
        ),
        solution_profile="861a",
        parent_media=DSMZ_861A_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Applies DSMZ Medium 861a to DSM 12342, DSM 12343, and DSM 12345.",),
        extra_references=(DSMZ_861A_REST, DSMZ_861A_PDF),
    ),
    Target(
        path=KOMODO_861_1,
        source_label="KOMODO Medium 861.1",
        source_url=f"{KOMODO_BASE}861.1",
        notes=(
            "KOMODO Medium 861.1 applies the low-salt Desulfotalea formulation "
            "to DSM 12343 and records pH 7.1-7.3."
        ),
        solution_profile="861a",
        ph_range={"min": 7.1, "max": 7.3},
        parent_media=DSMZ_861A_PARENT,
        variant_relationship="PH_VARIANT",
        variant_modifications=("Applies DSMZ Medium 861a to DSM 12343 at pH 7.1-7.3.",),
        extra_references=(DSMZ_861A_REST, DSMZ_861A_PDF),
    ),
    Target(
        path=KOMODO_861_4,
        source_label="KOMODO Medium 861.4",
        source_url=f"{KOMODO_BASE}861.4",
        notes=(
            "KOMODO Medium 861.4 records the DSM 12344 Desulfotalea formulation "
            "with a 150 g/L Na-propionate substrate stock in place of the lactate stock."
        ),
        solution_profile="861a",
        solution_c="propionate",
        parent_media=DSMZ_861A_PARENT,
        variant_relationship="SUBSTITUTED_COMPONENT_VARIANT",
        variant_modifications=(
            "Replaces the 250 g/L Na-DL-lactate Solution C with 150 g/L Na-propionate.",
        ),
        extra_references=(DSMZ_861A_REST, DSMZ_861A_PDF),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value
    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != EXPECTED_IDS[target.path]:
        raise ValueError(
            f"{target.path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[target.path]!r}"
        )
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[target.path]:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, expected {EXPECTED_SOURCE_TERMS[target.path]!r}"
        )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in (target.source_url, *target.extra_references):
        if url not in seen:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 861 Desulfotalea stock-solution structure",
        "source": target.source_url,
        "notes": target.notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")

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
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        repaired.pop(field, None)

    _put_after(repaired, "medium_type", "DEFINED", "category")
    _put_after(repaired, "composition_type", "DEFINED", "medium_type")
    _put_after(repaired, "physical_state", "LIQUID", "composition_type")
    if target.ph_range is not None:
        _put_after(repaired, "ph_range", copy.deepcopy(target.ph_range), "physical_state")

    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(repaired, "ingredients", [], "notes")
    _put_after(
        repaired,
        "solutions",
        [
            copy.deepcopy(row)
            for row in _stock_solutions(
                target.source_label, target.solution_profile, target.solution_c
            )
        ],
        "ingredients",
    )
    _put_after(repaired, "preparation_steps", list(_steps(target.source_label)), "solutions")
    _put_after(
        repaired,
        "data_quality_flags",
        ["ingredients_curated", "has_ontology_mappings"],
        "preparation_steps",
    )

    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")

    after = "references"
    if target.parent_media is not None:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), after)
        after = "parent_media"
    if target.variant_relationship is not None:
        _put_after(repaired, "variant_relationship", target.variant_relationship, after)
        after = "variant_relationship"
    if target.variant_modifications:
        _put_after(repaired, "variant_modifications", list(target.variant_modifications), after)
        after = "variant_modifications"
    if target.variant_children:
        _put_after(
            repaired,
            "variant_children",
            [copy.deepcopy(row) for row in target.variant_children],
            after,
        )

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
    for path, doc in sorted(plans.items()):
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
