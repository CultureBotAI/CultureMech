#!/usr/bin/env python3
"""Repair score-15 TOGO/JCM archaeal stock-solution wrappers."""

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

CURATOR = "repair_togo_jcm_archaea_score15.py"
ACTION = "RESOLVED_TOGO_JCM_ARCHAEA_SCORE15"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

TOGO_M1150 = "https://togomedium.org/medium/M1150"
TOGO_M1162 = "https://togomedium.org/medium/M1162"
TOGO_M1265 = "https://togomedium.org/medium/M1265"
TOGO_M1266 = "https://togomedium.org/medium/M1266"
TOGO_M1371 = "https://togomedium.org/medium/M1371"
TOGO_M279 = "https://togomedium.org/medium/M279"
TOGO_M970 = "https://togomedium.org/medium/M970"

JCM_151 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=151"
JCM_165 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=165"
JCM_197 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197"
JCM_285 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=285"
JCM_431 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431"
JCM_574 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574"
JCM_923 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=923"
JCM_924 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=924"
JCM_1079 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1079"
JCM_1081 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1081"
JCM_1092 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1092"
JCM_1181 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1181"
JCM_1275 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1275"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
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
    notes: str
    recipe: dict[str, Any]
    references: tuple[str, ...]
    accepted_names: frozenset[frozenset[str]]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {unit} {preferred_term}.",
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _solution(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    composition: list[dict[str, Any]] | None = None,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
    }
    if composition is not None:
        row["composition"] = copy.deepcopy(composition)
    if preparation_notes is not None:
        row["preparation_notes"] = preparation_notes
    return row


def _source_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} prints this component in its stock solution.",
        term=term,
    )


def _stock_addition(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        "ML_PER_L",
        source=source,
        notes=notes,
        term=term,
    )


def _raw_stock_volume(
    preferred_term: str,
    value: str,
    *,
    source: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        "variable",
        "VARIABLE",
        source=source,
        notes=(
            f"{source} prints {value} ml {preferred_term} in its 83 mM "
            "TiNTA stock; no final stock volume is stated."
        ),
        term=term,
    )


def _molar_stock(
    preferred_term: str,
    value: str,
    *,
    molarity: str,
    solute: str,
    source: str,
    term: tuple[str, str],
    notes: str,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        source=source,
        notes=notes,
        composition=[
            _component(
                solute,
                molarity,
                "MOLAR",
                source=source,
                notes=f"{source} identifies this as a {molarity} M stock solution.",
                term=term,
            )
        ],
    )


def _percent_stock(
    preferred_term: str,
    value: str,
    *,
    percent: str,
    solute: str,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        value,
        source=source,
        notes=notes,
        composition=[
            _component(
                solute,
                percent,
                "PERCENT_W_V",
                source=source,
                notes=f"{source} identifies this as a {percent}% w/v stock solution.",
                term=term,
            )
        ],
    )


def _water(source: str, value: str = "1.0", unit: str = "L") -> dict[str, Any]:
    return _source_component(
        "Distilled water",
        value,
        unit,
        source=source,
        term=("CHEBI:15377", "water"),
    )


def _trace_vitamins(source: str, value: str) -> dict[str, Any]:
    jcm_197 = "JCM Medium 197"
    return _solution(
        "Trace vitamins",
        value,
        source=source,
        notes=f"{source} adds {value} ml/L Trace vitamins from JCM Medium 197.",
        composition=[
            _source_component(
                "Biotin", "2.0", "MG_PER_L", source=jcm_197, term=("CHEBI:15956", "biotin")
            ),
            _source_component(
                "Folic acid", "2.0", "MG_PER_L", source=jcm_197, term=("CHEBI:27470", "folic acid")
            ),
            _source_component(
                "Pyridoxine HCl",
                "10.0",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:30961", "pyridoxine hydrochloride"),
            ),
            _source_component(
                "Thiamine HCl",
                "5.0",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:49105", "thiamine hydrochloride"),
            ),
            _source_component(
                "Riboflavin", "5.0", "MG_PER_L", source=jcm_197, term=("CHEBI:17015", "riboflavin")
            ),
            _source_component(
                "Nicotinic acid",
                "5.0",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:15940", "nicotinic acid"),
            ),
            _source_component(
                "Calcium pantothenate",
                "5.0",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:31345", "Calcium pantothenate"),
            ),
            _source_component(
                "Vitamin B12",
                "0.1",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:176843", "vitamin B12"),
            ),
            _source_component(
                "p-Aminobenzoic acid",
                "5.0",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:30753", "4-aminobenzoic acid"),
            ),
            _source_component(
                "Lipoic acid",
                "5.0",
                "MG_PER_L",
                source=jcm_197,
                term=("CHEBI:16494", "lipoic acid"),
            ),
            _water(jcm_197),
        ],
        preparation_notes="JCM Medium 197 prints the Trace vitamins subrecipe per liter.",
    )


def _selenite_tungstate(value: str, source: str) -> dict[str, Any]:
    jcm_431 = "JCM Medium 431"
    return _solution(
        "Selenite-tungstate solution",
        value,
        source=source,
        notes=f"{source} adds {value} ml/L Selenite-tungstate solution from JCM Medium 431.",
        composition=[
            _source_component(
                "NaOH", "0.4", "G_PER_L", source=jcm_431, term=("CHEBI:32145", "sodium hydroxide")
            ),
            _source_component(
                "Na2SeO3 x 5H2O",
                "6.0",
                "MG_PER_L",
                source=jcm_431,
                term=("CHEBI:131361", "disodium selenite pentahydrate"),
            ),
            _source_component(
                "Na2WO4 x 2H2O",
                "8.0",
                "MG_PER_L",
                source=jcm_431,
                term=("CHEBI:63939", "sodium tungstate dihydrate"),
            ),
            _water(jcm_431),
        ],
    )


def _jcm_1079_trace_elements() -> list[dict[str, Any]]:
    source = "JCM Medium 1079"
    return [
        _source_component(
            "EDTA",
            "5.0",
            "G_PER_L",
            source=source,
            term=("CHEBI:4735", "ethylenediaminetetraacetic acid"),
        ),
        _source_component(
            "FeSO4 x 7H2O",
            "2.0",
            "G_PER_L",
            source=source,
            term=("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        ),
        _source_component(
            "ZnSO4 x 7H2O",
            "0.10",
            "G_PER_L",
            source=source,
            term=("CHEBI:32312", "zinc sulfate heptahydrate"),
        ),
        _source_component(
            "MnCl2 x 4H2O",
            "0.03",
            "G_PER_L",
            source=source,
            term=("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        ),
        _source_component(
            "H3BO3", "0.3", "G_PER_L", source=source, term=("CHEBI:33118", "boric acid")
        ),
        _source_component(
            "CoCl2 x 6H2O",
            "0.2",
            "G_PER_L",
            source=source,
            term=("CHEBI:53503", "cobalt chloride hexahydrate"),
        ),
        _source_component(
            "CuCl2 x 2H2O",
            "0.01",
            "G_PER_L",
            source=source,
            term=("CHEBI:86318", "copper(II) chloride dihydrate"),
        ),
        _source_component(
            "NiCl2 x 6H2O",
            "0.02",
            "G_PER_L",
            source=source,
            term=("CHEBI:53542", "nickel chloride hexahydrate"),
        ),
        _source_component(
            "Na2MoO4 x 2H2O",
            "0.03",
            "G_PER_L",
            source=source,
            term=("CHEBI:75213", "sodium molybdate dihydrate"),
        ),
        _water(source),
    ]


def _jcm_1079_trace_solution(source: str) -> dict[str, Any]:
    return _solution(
        "Trace element solution",
        "1.0",
        source=source,
        notes=f"{source} adds 1.0 ml/L Trace element solution from JCM Medium 1079.",
        composition=_jcm_1079_trace_elements(),
    )


def _soda_based_mineral_medium(source: str, value: str = "750.0") -> dict[str, Any]:
    jcm_1081 = "JCM Medium 1081"
    return _solution(
        "Soda based mineral medium",
        value,
        source=source,
        notes=f"{source} adds {value} ml/L sterilized Soda based mineral medium from JCM Medium 1081.",
        composition=[
            _source_component(
                "Na2CO3",
                "185.0",
                "G_PER_L",
                source=jcm_1081,
                term=("CHEBI:29377", "sodium carbonate"),
            ),
            _source_component(
                "NaHCO3",
                "35.0",
                "G_PER_L",
                source=jcm_1081,
                term=("CHEBI:32139", "sodium hydrogencarbonate"),
            ),
            _source_component(
                "NaCl", "16.0", "G_PER_L", source=jcm_1081, term=("CHEBI:26710", "sodium chloride")
            ),
            _source_component(
                "K2HPO4",
                "1.0",
                "G_PER_L",
                source=jcm_1081,
                term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
            ),
            _source_component(
                "KCl", "5.0", "G_PER_L", source=jcm_1081, term=("CHEBI:32588", "potassium chloride")
            ),
            _stock_addition(
                "4 M NH4Cl solution",
                "1.0",
                source=jcm_1081,
                notes="JCM Medium 1081 adds 1.0 ml/L 4 M NH4Cl solution to the soda based mineral medium.",
                term=("CHEBI:31206", "ammonium chloride"),
            ),
            _stock_addition(
                "Selenite-tungstate solution",
                "1.0",
                source=jcm_1081,
                notes="JCM Medium 1081 adds 1.0 ml/L JCM 431 Selenite-tungstate solution.",
            ),
            _stock_addition(
                "Trace element solution",
                "1.0",
                source=jcm_1081,
                notes="JCM Medium 1081 adds 1.0 ml/L JCM 1079 Trace element solution.",
            ),
            _stock_addition(
                "1 M MgCl2 solution",
                "1.0",
                source=jcm_1081,
                notes="JCM Medium 1081 adds 1.0 ml/L 1 M MgCl2 solution to the soda based mineral medium.",
                term=("CHEBI:6636", "magnesium dichloride"),
            ),
            _water(jcm_1081),
        ],
        preparation_notes=(
            "Autoclave and let stand for three days; decant the clear solution into "
            "another empty sterile bottle before adding the stock solutions."
        ),
    )


def _modified_brock_base() -> dict[str, Any]:
    source = "JCM Medium 165"
    return _solution(
        "Modified Brock's salt base solution",
        "1000.0",
        source="JCM Medium 1275",
        notes="JCM Medium 1275 uses 1.0 L Modified Brock's salt base solution from JCM Medium 165.",
        composition=[
            _source_component(
                "(NH4)2SO4",
                "1.3",
                "G_PER_L",
                source=source,
                term=("CHEBI:62946", "ammonium sulfate"),
            ),
            _source_component(
                "KH2PO4",
                "0.28",
                "G_PER_L",
                source=source,
                term=("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _source_component(
                "MgSO4 x 7H2O",
                "0.25",
                "G_PER_L",
                source=source,
                term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
            ),
            _source_component(
                "CaCl2 x 2H2O",
                "0.07",
                "G_PER_L",
                source=source,
                term=("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _source_component(
                "FeCl3 x 6H2O",
                "2.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:86254", "iron trichloride hexahydrate"),
            ),
            _source_component(
                "MnCl2 x 4H2O",
                "1.8",
                "MG_PER_L",
                source=source,
                term=("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
            ),
            _source_component(
                "Na2B4O7 x 10H2O",
                "4.5",
                "MG_PER_L",
                source=source,
                term=("CHEBI:131366", "disodium tetraborate decahydrate"),
            ),
            _source_component(
                "ZnSO4 x 7H2O",
                "0.22",
                "MG_PER_L",
                source=source,
                term=("CHEBI:32312", "zinc sulfate heptahydrate"),
            ),
            _source_component(
                "CuCl2 x 2H2O",
                "0.05",
                "MG_PER_L",
                source=source,
                term=("CHEBI:86318", "copper(II) chloride dihydrate"),
            ),
            _source_component(
                "Na2MoO4 x 2H2O",
                "0.03",
                "MG_PER_L",
                source=source,
                term=("CHEBI:75213", "sodium molybdate dihydrate"),
            ),
            _source_component("VOSO4 x H2O", "0.03", "MG_PER_L", source=source),
            _source_component(
                "CoSO4 x 7H2O",
                "0.01",
                "MG_PER_L",
                source=source,
                term=("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
            ),
            _water(source),
        ],
    )


def _mds_salt_water() -> dict[str, Any]:
    source = "JCM Medium 574"
    return _solution(
        "MDS salt water",
        "833.0",
        source="JCM Medium 1181",
        notes="JCM Medium 1181 adds 833.0 ml/L MDS salt water from JCM Medium 574.",
        composition=[
            _source_component(
                "NaCl", "240.0", "G_PER_L", source=source, term=("CHEBI:26710", "sodium chloride")
            ),
            _source_component(
                "MgCl2 x 6H2O",
                "30.0",
                "G_PER_L",
                source=source,
                term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
            ),
            _source_component(
                "MgSO4 x 7H2O",
                "35.0",
                "G_PER_L",
                source=source,
                term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
            ),
            _source_component(
                "KCl", "7.0", "G_PER_L", source=source, term=("CHEBI:32588", "potassium chloride")
            ),
            _stock_addition(
                "1 M CaCl2 solution",
                "5.0",
                source=source,
                notes="JCM Medium 574 adds 5.0 ml/L 1 M CaCl2 solution to MDS salt water.",
                term=("CHEBI:3312", "calcium dichloride"),
            ),
            _water(source),
        ],
        preparation_notes="JCM Medium 574 adjusts the MDS salt water to pH 7.5 with 1 M Tris base.",
    )


def _potassium_phosphate_buffer() -> dict[str, Any]:
    source = "JCM Medium 574"
    return _solution(
        "Potassium phosphate buffer",
        "2.0",
        source="JCM Medium 1181",
        notes="JCM Medium 1181 adds 2.0 ml/L Potassium phosphate buffer from JCM Medium 574.",
        composition=[
            _stock_addition(
                "1 M K2HPO4",
                "417.0",
                source=source,
                notes=(
                    "JCM Medium 574 prepares Potassium phosphate buffer from "
                    "83.4 volumes of 1 M K2HPO4, 16.6 volumes of 1 M KH2PO4, "
                    "and an equal volume of distilled water."
                ),
                term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
            ),
            _stock_addition(
                "1 M KH2PO4",
                "83.0",
                source=source,
                notes=(
                    "JCM Medium 574 prepares Potassium phosphate buffer from "
                    "83.4 volumes of 1 M K2HPO4, 16.6 volumes of 1 M KH2PO4, "
                    "and an equal volume of distilled water."
                ),
                term=("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _source_component(
                "Distilled water", "500.0", "ML_PER_L", source=source, term=("CHEBI:15377", "water")
            ),
        ],
        preparation_notes="Combine the two phosphate solutions, check pH near 7.5, and add an equal volume of distilled water.",
    )


def _m1181_recipe(*, solid: bool) -> dict[str, Any]:
    ingredients = [
        _component(
            "Distilled water",
            "124.0",
            "ML_PER_L",
            source="JCM Medium 1181",
            notes="JCM Medium 1181 brings the MDS salt water, trace elements, and yeast extract to 958 ml with distilled water.",
            term=("CHEBI:15377", "water"),
        )
    ]
    if solid:
        ingredients.append(
            _component(
                "Agar",
                "20.0",
                "G_PER_L",
                source="JCM Medium 1181",
                notes="JCM Medium 1181 adds 20 g/L agar for solid medium.",
                term=("CHEBI:2509", "agar"),
            )
        )
    ingredients.append(
        _component(
            "Yeast extract (BD-Difco)",
            "0.1",
            "G_PER_L",
            source="JCM Medium 1181",
            notes="JCM Medium 1181 lists 0.1 g/L Yeast extract (BD-Difco).",
        )
    )

    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR" if solid else "LIQUID",
        "ph_value": 7.0,
        "ingredients": ingredients,
        "solutions": [
            _mds_salt_water(),
            _jcm_1079_trace_solution("JCM Medium 1181"),
            _molar_stock(
                "1 M NH4Cl",
                "5.0",
                molarity="1.0",
                solute="NH4Cl",
                source="JCM Medium 1181",
                notes="JCM Medium 1181 adds 5.0 ml/L 1 M NH4Cl after autoclaving.",
                term=("CHEBI:31206", "ammonium chloride"),
            ),
            _potassium_phosphate_buffer(),
            _trace_vitamins("JCM Medium 1181", "5.0"),
            _molar_stock(
                "0.2 M Cellobiose solution",
                "30.0",
                molarity="0.2",
                solute="Cellobiose",
                source="JCM Medium 1181",
                notes="JCM Medium 1181 adds 30.0 ml/L 0.2 M Cellobiose solution after autoclaving.",
                term=("CHEBI:17057", "cellobiose"),
            ),
            _percent_stock(
                "10% Na2CO3 solution",
                "variable",
                percent="10",
                solute="Na2CO3",
                source="JCM Medium 1181",
                notes="JCM Medium 1181 readjusts pH to 7.0 with sterilized 10% Na2CO3 solution if necessary.",
                term=("CHEBI:29377", "sodium carbonate"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Combine MDS salt water, JCM 1079 Trace element solution, yeast extract, and distilled water.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave the base medium before adding sterile NH4Cl, phosphate, vitamin, and cellobiose stocks.",
            },
            {
                "step_number": 3,
                "action": "ADJUST_PH",
                "description": "Readjust pH to 7.0 with sterilized 10% Na2CO3 solution if necessary.",
            },
        ],
    }


def _jcm_151_trace_minerals() -> dict[str, Any]:
    source = "JCM Medium 151"
    return _solution(
        "Trace minerals",
        "10.0",
        source="JCM Medium 285",
        notes="JCM Medium 285 adds 10.0 ml/L Trace minerals from JCM Medium 151.",
        composition=[
            _source_component(
                "Nitrilotriacetic acid",
                "1.5",
                "G_PER_L",
                source=source,
                term=("CHEBI:44557", "nitrilotriacetic acid"),
            ),
            _source_component(
                "MgSO4 x 7H2O",
                "3.0",
                "G_PER_L",
                source=source,
                term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
            ),
            _source_component(
                "MnSO4 x H2O",
                "0.5",
                "G_PER_L",
                source=source,
                term=("CHEBI:86360", "manganese(II) sulfate"),
            ),
            _source_component(
                "NaCl", "1.0", "G_PER_L", source=source, term=("CHEBI:26710", "sodium chloride")
            ),
            _source_component(
                "FeSO4 x 7H2O",
                "0.1",
                "G_PER_L",
                source=source,
                term=("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
            ),
            _source_component(
                "CoSO4 x 7H2O",
                "0.1",
                "G_PER_L",
                source=source,
                term=("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
            ),
            _source_component(
                "CaCl2 x 2H2O",
                "0.1",
                "G_PER_L",
                source=source,
                term=("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _source_component(
                "ZnSO4 x 7H2O",
                "0.1",
                "G_PER_L",
                source=source,
                term=("CHEBI:32312", "zinc sulfate heptahydrate"),
            ),
            _source_component(
                "CuSO4 x 5H2O",
                "0.01",
                "G_PER_L",
                source=source,
                term=("CHEBI:31440", "copper(II) sulfate pentahydrate"),
            ),
            _source_component("AlK(SO4)2", "0.01", "G_PER_L", source=source),
            _source_component(
                "H3BO3", "0.01", "G_PER_L", source=source, term=("CHEBI:33118", "boric acid")
            ),
            _source_component(
                "Na2MoO4 x 2H2O",
                "0.01",
                "G_PER_L",
                source=source,
                term=("CHEBI:75213", "sodium molybdate dihydrate"),
            ),
            _water(source),
        ],
        preparation_notes="Dissolve nitrilotriacetic acid, adjust pH to 6.5 with KOH, add minerals, then adjust final pH to 7.0.",
    )


def _jcm_923_major_metals(source: str = "JCM Medium 924") -> dict[str, Any]:
    jcm_923 = "JCM Medium 923"
    return _solution(
        "Major metals",
        "10.0",
        source=source,
        notes=f"{source} adds 10.0 ml/L Major metals from JCM Medium 923.",
        composition=[
            _source_component(
                "KCl", "0.15", "G_PER_L", source=jcm_923, term=("CHEBI:32588", "potassium chloride")
            ),
            _source_component(
                "KH2PO4",
                "1.36",
                "G_PER_L",
                source=jcm_923,
                term=("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _source_component(
                "NH4Cl",
                "2.68",
                "G_PER_L",
                source=jcm_923,
                term=("CHEBI:31206", "ammonium chloride"),
            ),
            _water(jcm_923),
        ],
    )


def _jcm_923_trace_metal_1_components() -> list[dict[str, Any]]:
    jcm_923 = "JCM Medium 923"
    return [
        _source_component(
            "CoCl2 x 6H2O",
            "24.0",
            "MG_PER_L",
            source=jcm_923,
            term=("CHEBI:53503", "cobalt chloride hexahydrate"),
        ),
        _source_component(
            "ZnCl2", "75.0", "MG_PER_L", source=jcm_923, term=("CHEBI:49976", "zinc dichloride")
        ),
        _source_component(
            "H3BO3", "19.0", "MG_PER_L", source=jcm_923, term=("CHEBI:33118", "boric acid")
        ),
        _source_component(
            "NiCl2 x 6H2O",
            "24.0",
            "MG_PER_L",
            source=jcm_923,
            term=("CHEBI:53542", "nickel chloride hexahydrate"),
        ),
        _source_component(
            "Na2MoO4 x 2H2O",
            "24.0",
            "MG_PER_L",
            source=jcm_923,
            term=("CHEBI:75213", "sodium molybdate dihydrate"),
        ),
        _source_component(
            "FeCl2 x 4H2O",
            "1.344",
            "G_PER_L",
            source=jcm_923,
            term=("CHEBI:86249", "iron dichloride tetrahydrate"),
        ),
        _source_component(
            "MnSO4 x H2O",
            "26.0",
            "MG_PER_L",
            source=jcm_923,
            term=("CHEBI:86360", "manganese(II) sulfate"),
        ),
        _source_component(
            "MgSO4 x 7H2O",
            "1.556",
            "G_PER_L",
            source=jcm_923,
            term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
        ),
        _source_component(
            "CaCl2 x 2H2O",
            "2.336",
            "G_PER_L",
            source=jcm_923,
            term=("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _source_component(
            "CuSO4 x 5H2O",
            "9.0",
            "MG_PER_L",
            source=jcm_923,
            term=("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        ),
        _source_component(
            "AlK(SO4)2 x 12H2O",
            "3.446",
            "G_PER_L",
            source=jcm_923,
            term=("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        ),
        _water(jcm_923),
    ]


def _jcm_923_trace_metal_1(value: str = "1000.0", source: str = "JCM Medium 924") -> dict[str, Any]:
    return _solution(
        "Trace metal 1 solution",
        value,
        source=source,
        notes=f"{source} adds Trace metal 1 solution from JCM Medium 923.",
        composition=_jcm_923_trace_metal_1_components(),
    )


def _jcm_923_vitamins() -> dict[str, Any]:
    source = "JCM Medium 923"
    return _solution(
        "Vitamin solution",
        "10.0",
        source="JCM Medium 924",
        notes="JCM Medium 924 adds 0.05 ml Vitamin solution from JCM Medium 923 to each 5 ml tube; this is 10 ml/L.",
        composition=[
            _source_component(
                "Biotin", "20.0", "MG_PER_L", source=source, term=("CHEBI:15956", "biotin")
            ),
            _source_component(
                "Folic acid", "20.0", "MG_PER_L", source=source, term=("CHEBI:27470", "folic acid")
            ),
            _source_component(
                "Pyridoxine HCl",
                "100.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:30961", "pyridoxine hydrochloride"),
            ),
            _source_component(
                "Thiamine HCl",
                "50.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:49105", "thiamine hydrochloride"),
            ),
            _source_component(
                "Riboflavin", "50.0", "MG_PER_L", source=source, term=("CHEBI:17015", "riboflavin")
            ),
            _source_component(
                "Nicotinic acid",
                "50.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:15940", "nicotinic acid"),
            ),
            _source_component(
                "DL-Calcium pantothenate",
                "50.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:31345", "Calcium pantothenate"),
            ),
            _source_component(
                "Vitamin B12",
                "1.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:176843", "vitamin B12"),
            ),
            _source_component(
                "p-Aminobenzoic acid",
                "50.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:30753", "4-aminobenzoic acid"),
            ),
            _source_component(
                "Lipoic acid",
                "50.0",
                "MG_PER_L",
                source=source,
                term=("CHEBI:16494", "lipoic acid"),
            ),
            _water(source),
        ],
        preparation_notes="Filter-sterilize and store under N2 at 4C in the dark.",
    )


def _jcm_923_tinta() -> dict[str, Any]:
    source = "JCM Medium 923"
    return _solution(
        "83 mM TiNTA solution",
        "10.0",
        source="JCM Medium 924",
        notes="JCM Medium 924 adds 0.05 ml 83 mM TiNTA solution to each 5 ml tube; this is 10 ml/L.",
        composition=[
            _raw_stock_volume(
                "1 M Tris base (pH 8)",
                "7.2",
                source=source,
                term=("CHEBI:9754", "tris"),
            ),
            _raw_stock_volume(
                "0.5 M Nitrilotriacetic acid, disodium salt",
                "4.8",
                source=source,
                term=("CHEBI:132766", "sodium nitrilotriacetate"),
            ),
            _raw_stock_volume(
                "15% TiCl3 solution",
                "0.55",
                source=source,
            ),
        ],
    )


def _m1150_recipe() -> dict[str, Any]:
    source = "JCM Medium 1081"
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "solutions": [
            _solution(
                "Basal mineral NaCl medium",
                "250.0",
                source=source,
                notes="JCM Medium 1081 adds 250.0 ml/L sterilized Basal mineral NaCl medium from JCM Medium 1079.",
                composition=[
                    _source_component(
                        "NaCl",
                        "240.0",
                        "G_PER_L",
                        source="JCM Medium 1079",
                        term=("CHEBI:26710", "sodium chloride"),
                    ),
                    _source_component(
                        "K2HPO4",
                        "2.5",
                        "G_PER_L",
                        source="JCM Medium 1079",
                        term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
                    ),
                    _source_component(
                        "NH4Cl",
                        "0.5",
                        "G_PER_L",
                        source="JCM Medium 1079",
                        term=("CHEBI:31206", "ammonium chloride"),
                    ),
                    _source_component(
                        "HEPES",
                        "7.0",
                        "G_PER_L",
                        source="JCM Medium 1079",
                        term=("CHEBI:46756", "HEPES"),
                    ),
                    _water("JCM Medium 1079"),
                ],
            ),
            _soda_based_mineral_medium(source),
            _molar_stock(
                "2 M Sodium pyruvate solution",
                "5.0",
                molarity="2.0",
                solute="Sodium pyruvate",
                source=source,
                notes="JCM Medium 1081 adds 5.0 ml/L filter-sterilized 2 M Sodium pyruvate solution.",
                term=("CHEBI:50144", "sodium pyruvate"),
            ),
            _trace_vitamins(source, "10.0"),
            _percent_stock(
                "10% Yeast extract solution",
                "0.2",
                percent="10",
                solute="Yeast extract",
                source=source,
                notes="JCM Medium 1081 adds 0.2 ml/L 10% Yeast extract solution.",
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Prepare and sterilize Basal mineral NaCl medium and Soda based mineral medium.",
            },
            {
                "step_number": 2,
                "action": "MIX",
                "description": "Mix 250 ml Basal mineral NaCl medium with 750 ml Soda based mineral medium.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": "Aseptically add sodium pyruvate, Trace vitamins, and yeast extract solutions.",
            },
        ],
    }


def _m1162_recipe() -> dict[str, Any]:
    source = "JCM Medium 1092"
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _component(
                "N2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 1092 replaces the gas phase with N2 containing 5% O2 by volume.",
                term=("CHEBI:17997", "dinitrogen"),
            ),
            _component(
                "O2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 1092 replaces the gas phase with N2 containing 5% O2 by volume.",
                term=("CHEBI:15379", "dioxygen"),
            ),
        ],
        "solutions": [
            _soda_based_mineral_medium(source, "1000.0"),
            _trace_vitamins(source, "10.0"),
            _percent_stock(
                "10% Yeast extract solution",
                "0.2",
                percent="10",
                solute="Yeast extract",
                source=source,
                notes="JCM Medium 1092 adds 0.2 ml/L 10% Yeast extract solution.",
            ),
            _molar_stock(
                "1 M Sodium butyrate",
                "20.0",
                molarity="1.0",
                solute="Sodium butyrate",
                source=source,
                notes="JCM Medium 1092 adds 20.0 ml/L 1 M Sodium butyrate.",
                term=("CHEBI:64103", "sodium butyrate"),
            ),
            _molar_stock(
                "1 M Sodium acetate",
                "20.0",
                molarity="1.0",
                solute="Sodium acetate",
                source=source,
                notes="JCM Medium 1092 adds 20.0 ml/L 1 M Sodium acetate.",
                term=("CHEBI:32954", "sodium acetate"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Prepare 1.0 L of sterilized JCM 1081 Soda based mineral medium.",
            },
            {
                "step_number": 2,
                "action": "MIX",
                "description": "Aseptically add Trace vitamins, yeast extract, sodium butyrate, and sodium acetate stocks.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": "Distribute into culture vessels, replace the gas phase with N2 containing 5% O2, and seal with butyl rubber stoppers.",
            },
        ],
    }


def _m1371_recipe() -> dict[str, Any]:
    source = "JCM Medium 1275"
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 1.5,
        "ingredients": [
            _component(
                "Tryptone",
                "0.5",
                "G_PER_L",
                source=source,
                notes="JCM Medium 1275 lists 0.5 g/L Tryptone.",
            ),
            _component(
                "H2SO4",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 1275 adjusts pH to 1.5 with H2SO4.",
                term=("CHEBI:26836", "sulfuric acid"),
            ),
        ],
        "solutions": [_modified_brock_base()],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Prepare Modified Brock's salt base solution from JCM Medium 165 and add Tryptone.",
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 1.5 with H2SO4.",
            },
        ],
    }


def _m279_recipe() -> dict[str, Any]:
    source = "JCM Medium 285"
    return {
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.5,
        "ingredients": [
            _component(
                "NH4Cl", "0.5", "G_PER_L", source=source, term=("CHEBI:31206", "ammonium chloride")
            ),
            _component(
                "K2HPO4",
                "0.4",
                "G_PER_L",
                source=source,
                term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
            ),
            _component(
                "MgCl2 x 6H2O",
                "0.1",
                "G_PER_L",
                source=source,
                term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
            ),
            _component(
                "Resazurin", "1.0", "MG_PER_L", source=source, term=("CHEBI:8806", "Resazurin")
            ),
            _component("Distilled water", "1.0", "L", source=source, term=("CHEBI:15377", "water")),
            _component(
                "N2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 285 cools the boiled medium under N2-CO2 (80:20, v/v).",
                term=("CHEBI:17997", "dinitrogen"),
            ),
            _component(
                "CO2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 285 cools the boiled medium under N2-CO2 and adds CO2 to 30% of the gas phase.",
                term=("CHEBI:16526", "carbon dioxide"),
            ),
        ],
        "solutions": [
            _jcm_151_trace_minerals(),
            _percent_stock(
                "5% NaHCO3 solution",
                "20.0",
                percent="5",
                solute="NaHCO3",
                source=source,
                notes="JCM Medium 285 adds 20.0 ml/L sterile anaerobic 5% NaHCO3 solution.",
                term=("CHEBI:32139", "sodium hydrogencarbonate"),
            ),
            _percent_stock(
                "1% CaCl2 x 2H2O solution",
                "10.0",
                percent="1",
                solute="CaCl2 x 2H2O",
                source=source,
                notes="JCM Medium 285 adds 10.0 ml/L sterile anaerobic 1% CaCl2 x 2H2O solution.",
                term=("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _percent_stock(
                "33% Sodium acetate solution",
                "10.0",
                percent="33",
                solute="Sodium acetate",
                source=source,
                notes="JCM Medium 285 adds 10.0 ml/L sterile anaerobic 33% Sodium acetate solution.",
                term=("CHEBI:32954", "sodium acetate"),
            ),
            _trace_vitamins(source, "10.0"),
            _percent_stock(
                "1.42% Coenzyme M solution",
                "10.0",
                percent="1.42",
                solute="Coenzyme M",
                source=source,
                notes="JCM Medium 285 adds 10.0 ml/L sterile anaerobic 1.42% Coenzyme M solution.",
                term=("CHEBI:17905", "coenzyme M"),
            ),
            _percent_stock(
                "5% Na2S x 9H2O solution",
                "5.0",
                percent="5",
                solute="Na2S x 9H2O",
                source=source,
                notes="JCM Medium 285 adds 5.0 ml/L sterile anaerobic 5% Na2S x 9H2O solution.",
                term=("CHEBI:76209", "sodium sulfide nonahydrate"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Mix direct ingredients and Trace minerals, boil for 5 minutes, and cool under N2-CO2.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Dispense under N2-CO2, seal with butyl rubber stoppers, and autoclave.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": "After autoclaving, add sterile anaerobic NaHCO3, CaCl2, acetate, vitamin, Coenzyme M, and Na2S stocks.",
            },
            {
                "step_number": 4,
                "action": "ADJUST_PH",
                "description": "Add filter-sterilized CO2 to 30% of the gas phase and check final pH at 6.5.",
            },
        ],
    }


def _trace_metal_2() -> dict[str, Any]:
    source = "JCM Medium 924"
    return _solution(
        "Trace metal 2 solution",
        "1.0",
        source=source,
        notes="JCM Medium 924 adds 1.0 ml/L Trace metal 2 solution.",
        composition=_jcm_923_trace_metal_1_components()
        + [
            _source_component(
                "EDTA x 2Na",
                "37.23",
                "G_PER_L",
                source=source,
                term=("CHEBI:64734", "EDTA disodium salt (anhydrous)"),
            ),
            _component(
                "NaOH",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 924 adjusts Trace metal 2 solution to pH 7.0 with NaOH.",
                term=("CHEBI:32145", "sodium hydroxide"),
            ),
        ],
        preparation_notes="Adjust pH to 7.0 with NaOH.",
    )


def _m970_recipe() -> dict[str, Any]:
    source = "JCM Medium 924"
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 5.7,
        "ingredients": [
            _component("Distilled water", "1.0", "L", source=source, term=("CHEBI:15377", "water")),
            _component(
                "N2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 924 uses N2-CO2 (80:20, v/v) during cooling and dispensing.",
                term=("CHEBI:17997", "dinitrogen"),
            ),
            _component(
                "CO2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 924 uses N2-CO2 during cooling and H2-CO2 during pressurization.",
                term=("CHEBI:16526", "carbon dioxide"),
            ),
            _component(
                "H2",
                "variable",
                "VARIABLE",
                source=source,
                notes="JCM Medium 924 pressurizes the tubes to 70 kPa H2-CO2 (80:20, v/v).",
                term=("CHEBI:18276", "dihydrogen"),
            ),
        ],
        "solutions": [
            _jcm_923_major_metals(),
            _trace_metal_2(),
            _jcm_923_tinta(),
            _molar_stock(
                "1.0 M MES solution",
                "20.0",
                molarity="1.0",
                solute="MES",
                source=source,
                notes="JCM Medium 924 adds 0.10 ml 1.0 M MES solution to each 5 ml tube; this is 20 ml/L.",
                term=("CHEBI:39010", "MES"),
            ),
            _jcm_923_vitamins(),
            _percent_stock(
                "1% Yeast extract solution",
                "2.0",
                percent="1",
                solute="Yeast extract",
                source=source,
                notes="JCM Medium 924 adds 0.01 ml 1% Yeast extract solution to each 5 ml tube; this is 2 ml/L.",
            ),
            _molar_stock(
                "50 mM Coenzyme M solution",
                "5.0",
                molarity="0.05",
                solute="Coenzyme M",
                source=source,
                notes="JCM Medium 924 adds 0.025 ml 50 mM Coenzyme M solution to each 5 ml tube; this is 5 ml/L.",
                term=("CHEBI:17905", "coenzyme M"),
            ),
            _solution(
                "10 mM Sodium acetate",
                "3.0",
                source=source,
                notes="JCM Medium 924 adds 0.015 ml 10 mM Sodium acetate to each 5 ml tube; this is 3 ml/L.",
                composition=[
                    _component(
                        "Sodium acetate",
                        "10",
                        "MILLIMOLAR",
                        source=source,
                        notes="JCM Medium 924 identifies this as a 10 mM stock solution.",
                        term=("CHEBI:32954", "sodium acetate"),
                    )
                ],
            ),
            _solution(
                "4 mM Na2S x 9H2O solution",
                "10.0",
                source=source,
                notes="JCM Medium 924 adds 0.05 ml 4 mM Na2S x 9H2O solution to each 5 ml tube; this is 10 ml/L.",
                composition=[
                    _component(
                        "Na2S x 9H2O",
                        "4",
                        "MILLIMOLAR",
                        source=source,
                        notes="JCM Medium 924 identifies this as a 4 mM stock solution.",
                        term=("CHEBI:76209", "sodium sulfide nonahydrate"),
                    )
                ],
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Mix Major metals, Trace metal 2 solution, and distilled water thoroughly.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Boil for 5 minutes, cool under N2-CO2, dispense under the same gas mixture, seal, and autoclave.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": "For each 5 ml tube, add sterile anaerobic TiNTA, MES, vitamin, yeast extract, Coenzyme M, sodium acetate, and Na2S stocks.",
            },
            {
                "step_number": 4,
                "action": "ADJUST_PH",
                "description": "Pressurize tubes to 70 kPa H2-CO2 (80:20, v/v), stand at least 7 hr, and check final pH at about 5.7.",
            },
        ],
    }


def _new_names(recipe: dict[str, Any]) -> frozenset[str]:
    names: set[str] = set()
    for key in ("ingredients", "solutions"):
        for row in recipe.get(key) or []:
            if isinstance(row, dict):
                names.add(str(row.get("preferred_term") or ""))
    return frozenset(names)


def _accepted(*old_names: str, recipe: dict[str, Any]) -> frozenset[frozenset[str]]:
    return frozenset((frozenset(old_names), _new_names(recipe)))


M1150_RECIPE = _m1150_recipe()
M1162_RECIPE = _m1162_recipe()
M1265_RECIPE = _m1181_recipe(solid=False)
M1266_RECIPE = _m1181_recipe(solid=True)
M1371_RECIPE = _m1371_recipe()
M279_RECIPE = _m279_recipe()
M970_RECIPE = _m970_recipe()

UPDATES: dict[str, Target] = {
    "archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml": Target(
        path="archaea/TOGO_M1150_Natranaeroarchaeum_Medium.yaml",
        record_id="CultureMech:007674",
        source_term="TOGO:M1150",
        notes=(
            "JCM Medium 1081 composes Natranaeroarchaeum Medium from sterilized "
            "JCM 1079 Basal mineral NaCl medium, JCM 1081 Soda based mineral "
            "medium, 2 M sodium pyruvate, Trace vitamins from JCM 197, and "
            "10% yeast extract."
        ),
        recipe=M1150_RECIPE,
        references=(TOGO_M1150, JCM_1081, JCM_1079, JCM_431, JCM_197),
        accepted_names=_accepted(
            "Soda based mineral medium (sterilized, see below)",
            "Distilled water",
            "NaCl",
            "K2HPO4",
            "KCl",
            "NaHCO3",
            "Na2CO3",
            "Basal mineral NaCl medium (see Medium [M1148])",
            "10% Yeast extract solution",
            "2 M Sodium pyruvate solution*",
            "Trace vitamins (see Medium [M190])",
            "4 M NH4Cl solution",
            "1 M MgCl2 solution",
            "Selenite--tungstate solution (see Medium [M431])",
            "Trace element solution (see Medium [M1148])",
            recipe=M1150_RECIPE,
        ),
    ),
    "archaea/TOGO_M1162_Natronolimnobius_AHT32_Medium_B.yaml": Target(
        path="archaea/TOGO_M1162_Natronolimnobius_AHT32_Medium_B.yaml",
        record_id="CultureMech:007686",
        source_term="TOGO:M1162",
        notes=(
            "JCM Medium 1092 composes Natronolimnobius AHT32 Medium (B) from "
            "1 L sterilized JCM 1081 Soda based mineral medium plus Trace "
            "vitamins, yeast extract, sodium butyrate, and sodium acetate stocks."
        ),
        recipe=M1162_RECIPE,
        references=(TOGO_M1162, JCM_1092, JCM_1081, JCM_1079, JCM_431, JCM_197),
        accepted_names=_accepted(
            "1 M Sodium acetate",
            "1 M Sodium butyrate",
            "Nitrogen gas",
            "Oxygen gas",
            "Soda based mineral medium (see Medium [M1150])",
            "10% Yeast extract solution",
            "Trace vitamins (see Medium [M190])",
            recipe=M1162_RECIPE,
        ),
    ),
    "archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml": Target(
        path="archaea/TOGO_M1265_Modified_Cellulolytic_Haloarchaea_Medium.yaml",
        record_id="CultureMech:007797",
        source_term="TOGO:M1265",
        notes=(
            "JCM Medium 1181 liquid Modified Cellulolytic Haloarchaea Medium "
            "uses MDS salt water and Potassium phosphate buffer from JCM 574, "
            "JCM 1079 Trace element solution, JCM 197 Trace vitamins, NH4Cl, "
            "cellobiose, and a Na2CO3 pH-adjustment stock."
        ),
        recipe=M1265_RECIPE,
        references=(TOGO_M1265, JCM_1181, JCM_574, JCM_1079, JCM_197),
        accepted_names=_accepted(
            "distilled water",
            "Yeast extract (BD-Difco)",
            "1 M NH4Cl",
            "MDS salt water (see Medium [M578])",
            "Trace element solution (see Medium [M1148])",
            "0.2 M Cellobiose solution",
            "Potassium phosphate buffer (see Medium [M578])",
            "Trace vitamins (see Medium [M190])",
            "Na2CO3 solution",
            recipe=M1265_RECIPE,
        ),
    ),
    "archaea/TOGO_M1266_Modified_Cellulolytic_Haloarchaea_Medium.yaml": Target(
        path="archaea/TOGO_M1266_Modified_Cellulolytic_Haloarchaea_Medium.yaml",
        record_id="CultureMech:007798",
        source_term="TOGO:M1266",
        notes=(
            "TOGO M1266 records the solid-agar JCM Medium 1181 preparation of "
            "Modified Cellulolytic Haloarchaea Medium with washed agar plus the "
            "same MDS, trace-element, phosphate, vitamin, NH4Cl, cellobiose, "
            "and Na2CO3 stocks used by the liquid recipe."
        ),
        recipe=M1266_RECIPE,
        references=(TOGO_M1266, JCM_1181, JCM_574, JCM_1079, JCM_197),
        accepted_names=_accepted(
            "distilled water",
            "agar",
            "Yeast extract (BD-Difco)",
            "1 M NH4Cl",
            "MDS salt water (see Medium [M578])",
            "Trace element solution (see Medium [M1148])",
            "0.2 M Cellobiose solution",
            "Potassium phosphate buffer (see Medium [M578])",
            "Trace vitamins (see Medium [M190])",
            "Na2CO3 solution",
            recipe=M1266_RECIPE,
        ),
    ),
    "archaea/TOGO_M1371_Sulfolobus_Medium_With_Tryptone.yaml": Target(
        path="archaea/TOGO_M1371_Sulfolobus_Medium_With_Tryptone.yaml",
        record_id="CultureMech:007910",
        source_term="TOGO:M1371",
        notes=(
            "JCM Medium 1275 adds 0.5 g/L Tryptone to the JCM 165 Modified "
            "Brock's salt base solution and adjusts pH to 1.5 with H2SO4."
        ),
        recipe=M1371_RECIPE,
        references=(TOGO_M1371, JCM_1275, JCM_165),
        accepted_names=_accepted(
            "Tryptone",
            "H2SO4",
            "Modified Brock's salt base solution (see Medium [M156])",
            recipe=M1371_RECIPE,
        ),
    ),
    "archaea/TOGO_M279_Methanosaeta_Thermophila_Medium.yaml": Target(
        path="archaea/TOGO_M279_Methanosaeta_Thermophila_Medium.yaml",
        record_id="CultureMech:009347",
        source_term="TOGO:M279",
        notes=(
            "JCM Medium 285 prepares Methanosaeta Thermophila Medium with "
            "NH4Cl, K2HPO4, MgCl2, resazurin, Trace minerals from JCM 151, "
            "distilled water, and sterile post-autoclave NaHCO3, CaCl2, "
            "acetate, vitamin, Coenzyme M, and Na2S stocks."
        ),
        recipe=M279_RECIPE,
        references=(TOGO_M279, JCM_285, JCM_151, JCM_197),
        accepted_names=_accepted(
            "Distilled water",
            "NH4Cl",
            "K2HPO4",
            "Resazurin",
            "MgCl2・6H2O",
            "Carbon dioxide gas",
            "Nitrogen gas",
            "CO2 gas",
            "Trace minerals (see Medium [M142])",
            "5% NaHCO3 solution",
            "1% CaCl2・2H2O solution",
            "33% Sodium acetate solution",
            "1.42% Coenzyme M solution",
            "5% Na2S・9H2O solution",
            "Trace vitamins (see Medium [M190])",
            recipe=M279_RECIPE,
        ),
    ),
    "archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml": Target(
        path="archaea/TOGO_M970_Peat_Medium_2_For_Methanobacteria.yaml",
        record_id="CultureMech:010396",
        source_term="TOGO:M970",
        notes=(
            "JCM Medium 924 prepares Peat Medium 2 For Methanobacteria from "
            "Major metals and TiNTA/Vitamin subrecipes in JCM 923 plus a "
            "JCM 924 Trace metal 2 stock; the culture-tube additions are "
            "scaled from per-5-ml additions to ml/L."
        ),
        recipe=M970_RECIPE,
        references=(TOGO_M970, JCM_924, JCM_923),
        accepted_names=_accepted(
            "Distilled water",
            "Carbon dioxide gas",
            "Nitrogen gas",
            "10 mM Sodium acetate",
            "Hydrogen gas",
            "EDTA・2Na",
            "NaOH",
            "Major metals (see Medium [M969])",
            "Trace metal 2 solution (see below)",
            "1% Yeast extract solution",
            "50 mM Coenzyme M solution",
            "4 mM Na2S・9H2O solution*",
            "1.0 M MES solution* (pH 7.45)",
            "83 mM TiNTA solution (see Medium [M969])",
            "Vitamin solution (see Medium [M969])",
            "Trace metal 1 solution (see Medium [M969])",
            recipe=M970_RECIPE,
        ),
    ),
}


def _load(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.load(handle, Loader=YAML_LOADER)
    if not isinstance(data, dict):
        raise TypeError(f"{path} did not contain a mapping")
    return data


def _source_term_id(doc: dict[str, Any]) -> str | None:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return None
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return None
    term_id = term.get("id")
    return str(term_id) if term_id is not None else None


def _component_names(doc: dict[str, Any]) -> frozenset[str]:
    names: set[str] = set()
    for key in ("ingredients", "solutions"):
        for row in doc.get(key) or []:
            if isinstance(row, dict):
                names.add(str(row.get("preferred_term") or ""))
    return frozenset(names)


def _grounded(component: dict[str, Any]) -> bool:
    return any(
        isinstance(component.get(key), dict) and bool(component[key].get("id"))
        for key in (
            "term",
            "mediaingredientmech_term",
            "mediaingredientmech_chebi_term",
            "culturemech_term",
        )
    )


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        composition = solution.get("composition")
        nested = (
            [row for row in composition if isinstance(row, dict)]
            if isinstance(composition, list)
            else []
        )
        components.extend(nested or [solution])
    return components


def _require_target(doc: dict[str, Any], update: Target) -> None:
    if doc.get("id") != update.record_id:
        raise ValueError(f"{update.path}: expected id {update.record_id}, found {doc.get('id')!r}")
    source_term = _source_term_id(doc)
    if source_term != update.source_term:
        raise ValueError(
            f"{update.path}: expected source term {update.source_term}, found {source_term!r}"
        )
    if _component_names(doc) not in update.accepted_names:
        raise ValueError(f"{update.path}: component signature drifted")


def _ensure_references(doc: dict[str, Any], update: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in update.references:
        if reference not in seen:
            references.append({"reference": reference})
            seen.add(reference)


def _ensure_flags(doc: dict[str, Any], update: Target) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{update.path}: data_quality_flags is not a list")

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _composition_components(doc)
    if any(_grounded(component) for component in components):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")
    elif "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if any(not _grounded(component) for component in components):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_event(doc: dict[str, Any], update: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(update.references),
        "notes": update.notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{update.path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_document(doc: dict[str, Any], update: Target) -> dict[str, Any]:
    _require_target(doc, update)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in update.recipe:
            repaired[field] = copy.deepcopy(update.recipe[field])
        else:
            repaired.pop(field, None)

    repaired["notes"] = update.notes
    _ensure_references(repaired, update)
    _ensure_flags(repaired, update)
    _ensure_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / update.path: repair_document(_load(normalized / update.path), update)
        for update in UPDATES.values()
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
        print(f"{status} {path.relative_to(args.normalized_dir)}")

    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
