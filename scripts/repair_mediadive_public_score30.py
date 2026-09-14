#!/usr/bin/env python3
"""Repair score-30 public MediaDive placeholder records."""

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

CURATOR = "repair_mediadive_public_score30.py"
ACTION = "RESOLVED_MEDIADIVE_PUBLIC_SCORE30"
TIMESTAMP = "2026-09-08T00:00:00-07:00"

P1_HAHA = "bacterial/haha_agar.yaml"
P3_KING_B = "bacterial/king_b.yaml"
P6_MTA10 = "bacterial/mta10.yaml"
P7_N27_RHODOSPIRILLACEAE = "bacterial/n27_rhodospirillaceae_medium_modified.yaml"
P8_M9_SNG = "bacterial/m9_sng_medium.yaml"
P9_PDB_SNG = "bacterial/pdb_sng_medium.yaml"
P10_BEKISOLID = "bacterial/bekisolidmedium_hydrogenovibrio_crunogenus_quimiolitotrofo.yaml"

EXPECTED_IDS = {
    P1_HAHA: "CultureMech:010431",
    P3_KING_B: "CultureMech:010433",
    P6_MTA10: "CultureMech:010436",
    P7_N27_RHODOSPIRILLACEAE: "CultureMech:010437",
    P8_M9_SNG: "CultureMech:010438",
    P9_PDB_SNG: "CultureMech:010439",
    P10_BEKISOLID: "CultureMech:010430",
}

EXPECTED_SOURCE_TERMS = {
    P1_HAHA: "mediadive.medium:P1",
    P3_KING_B: "mediadive.medium:P3",
    P6_MTA10: "mediadive.medium:P6",
    P7_N27_RHODOSPIRILLACEAE: "mediadive.medium:P7",
    P8_M9_SNG: "mediadive.medium:P8",
    P9_PDB_SNG: "mediadive.medium:P9",
    P10_BEKISOLID: "mediadive.medium:P10",
}

P1_DOI = "10.1016/j.syapm.2013.06.006"
P6_DOI = "10.1016/j.foodcont.2012.06.029"
P8_DOI = "10.1007/s11104-022-05822-6"
P9_DOI = "10.1007/s11104-022-05822-6"

P1_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P1"
P3_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P3"
P6_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P6"
P7_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P7"
P8_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P8"
P9_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P9"
P10_PUBLIC = "https://www.bacmedia.dsmz.de/medium/P10"

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "salinity",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
    "parent_media",
    "variant_relationship",
    "variant_modifications",
    "variant_children",
)


@dataclass(frozen=True)
class RecipeUpdate:
    path: str
    notes: str
    recipe: dict[str, Any]
    reference_urls: tuple[str, ...]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    identifier: str | None = None,
    label: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    component: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
    }
    if notes:
        component["notes"] = notes
    if identifier and label:
        component["term"] = _term(identifier, label)
        if identifier.startswith("CHEBI:"):
            component["mediaingredientmech_chebi_term"] = _term(identifier, label)
    return component


def _solution(
    preferred_term: str,
    value: str,
    *,
    composition: list[dict[str, Any]],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
        "composition": composition,
    }


def _stock(
    preferred_term: str,
    added: str,
    solute: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    identifier: str | None = None,
    label: str | None = None,
) -> dict[str, Any]:
    return _solution(
        preferred_term,
        added,
        notes=notes,
        composition=[
            _component(
                solute,
                value,
                unit,
                source=source,
                identifier=identifier,
                label=label,
            ),
        ],
    )


def _variable_solution(
    preferred_term: str,
    *,
    composition: list[dict[str, Any]],
    notes: str,
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "notes": notes,
        "composition": composition,
    }


def _sl6(source: str) -> dict[str, Any]:
    return _solution(
        "Trace element solution SL-6",
        "1",
        notes=f"{source} adds 1 ml Trace element solution SL-6 per 1 L medium.",
        composition=[
            _component("ZnSO4 x 7 H2O", "0.1", "G_PER_L", source=source),
            _component("MnCl2 x 4 H2O", "0.03", "G_PER_L", source=source),
            _component("H3BO3", "0.3", "G_PER_L", source=source, identifier="CHEBI:33118", label="boric acid"),
            _component("CoCl2 x 6 H2O", "0.2", "G_PER_L", source=source),
            _component("CuCl2 x 2 H2O", "0.01", "G_PER_L", source=source),
            _component("NiCl2 x 6 H2O", "0.02", "G_PER_L", source=source),
            _component(
                "Na2MoO4 x 2 H2O",
                "0.03",
                "G_PER_L",
                source=source,
                identifier="CHEBI:75213",
                label="sodium molybdate dihydrate",
            ),
        ],
    )


def _sl10(source: str) -> dict[str, Any]:
    return _solution(
        "Trace element solution SL-10",
        "1",
        notes=f"{source} adds 1 ml Trace element solution SL-10 per 1 L medium.",
        composition=[
            _component("HCl", "2.5", "G_PER_L", source=source, identifier="CHEBI:17883", label="hydrogen chloride"),
            _component("FeCl2 x 4 H2O", "1.5", "G_PER_L", source=source),
            _component("ZnCl2", "0.07", "G_PER_L", source=source, identifier="CHEBI:49976", label="zinc dichloride"),
            _component("MnCl2 x 4 H2O", "0.1", "G_PER_L", source=source),
            _component("H3BO3", "0.006", "G_PER_L", source=source, identifier="CHEBI:33118", label="boric acid"),
            _component("CoCl2 x 6 H2O", "0.19", "G_PER_L", source=source),
            _component("CuCl2 x 2 H2O", "0.002", "G_PER_L", source=source),
            _component("NiCl2 x 6 H2O", "0.024", "G_PER_L", source=source),
            _component(
                "Na2MoO4 x 2 H2O",
                "0.036",
                "G_PER_L",
                source=source,
                identifier="CHEBI:75213",
                label="sodium molybdate dihydrate",
            ),
        ],
    )


SRC_P1 = "MediaDive public Medium P1"
SRC_P3 = "MediaDive public Medium P3"
SRC_P6 = "MediaDive public Medium P6"
SRC_P7 = "MediaDive public Medium P7"
SRC_P8 = "MediaDive public Medium P8"
SRC_P9 = "MediaDive public Medium P9"
SRC_P10 = "MediaDive public Medium P10"

ASW_2X = _solution(
    "Artificial sea water (ASW) 2x",
    "500",
    notes="P1 adds 350 ml Artificial sea water (ASW) 2x to a 700 ml main solution.",
    composition=[
        _component("NaCl", "52.74", "G_PER_L", source=SRC_P1, identifier="CHEBI:26710", label="sodium chloride"),
        _component(
            "NaHCO3",
            "1000",
            "G_PER_L",
            source=SRC_P1,
            identifier="CHEBI:32139",
            label="sodium hydrogencarbonate",
        ),
        _component(
            "CaCl2 x 2 H2O",
            "2.94",
            "G_PER_L",
            source=SRC_P1,
            identifier="CHEBI:86158",
            label="calcium chloride dihydrate",
        ),
        _component("KCl", "1.44", "G_PER_L", source=SRC_P1, identifier="CHEBI:32588", label="potassium chloride"),
        _component("KBr", "0.20", "G_PER_L", source=SRC_P1),
        _component("H3BO3", "0.040", "G_PER_L", source=SRC_P1, identifier="CHEBI:33118", label="boric acid"),
        _component("SrCl2", "0.040", "G_PER_L", source=SRC_P1),
        _component("NaF", "0.006", "G_PER_L", source=SRC_P1, identifier="CHEBI:28741", label="sodium fluoride"),
    ],
)

SL8 = _solution(
    "Trace element solution SL-8",
    "2",
    notes="P1 adds 1.4 ml Trace element solution SL-8 to a 700 ml main solution.",
    composition=[
        _component("Na2-EDTA", "5.2", "G_PER_L", source=SRC_P1),
        _component("FeSO4 x 7 H2O", "2", "G_PER_L", source=SRC_P1),
        _component("CoCl2 x 6 H2O", "0.190", "G_PER_L", source=SRC_P1),
        _component("MnCl2 x 2 H2O", "0.100", "G_PER_L", source=SRC_P1),
        _component("ZnSO4 x 7 H2O", "0.150", "G_PER_L", source=SRC_P1),
        _component("NiCl2 x 6 H2O", "0.024", "G_PER_L", source=SRC_P1),
        _component("Na2MoO4 x 2 H2O", "0.036", "G_PER_L", source=SRC_P1),
        _component("H3BO3", "0.062", "G_PER_L", source=SRC_P1, identifier="CHEBI:33118", label="boric acid"),
        _component("CuCl2 x 2 H2O", "0.017", "G_PER_L", source=SRC_P1),
    ],
)

SELENITE_TUNGSTATE = _solution(
    "Selenite-tungstate solution II",
    "1",
    notes="P1 adds 0.7 ml Selenite-tungstate solution II to a 700 ml main solution.",
    composition=[
        _component("NaOH", "0.2", "G_PER_L", source=SRC_P1, identifier="CHEBI:32145", label="sodium hydroxide"),
        _component("Na2SeO3 x 5 H2O", "0.018", "G_PER_L", source=SRC_P1),
        _component("Na2WO4 x 2 H2O", "0.018", "G_PER_L", source=SRC_P1),
    ],
)

P1_SINGLE_SOLUTE_STOCKS = (
    _stock(
        "KH2PO4 stock",
        "10",
        "KH2PO4",
        "50",
        "G_PER_L",
        source=SRC_P1,
        identifier="CHEBI:63036",
        label="potassium dihydrogen phosphate",
        notes="P1 adds 7 ml of a 50 g/L autoclaved KH2PO4 stock to a 700 ml main solution.",
    ),
    _stock(
        "NH4Cl stock",
        "5",
        "NH4Cl",
        "50",
        "G_PER_L",
        source=SRC_P1,
        identifier="CHEBI:31206",
        label="ammonium chloride",
        notes="P1 adds 3.5 ml of a 50 g/L autoclaved NH4Cl stock to a 700 ml main solution.",
    ),
    _stock(
        "Glucose stock",
        "5",
        "Glucose",
        "100",
        "G_PER_L",
        source=SRC_P1,
        identifier="CHEBI:17234",
        label="glucose",
        notes="P1 adds 3.5 ml of a sterile-filtered 100 g/L glucose stock to a 700 ml main solution.",
    ),
    _stock(
        "Cellobiose stock",
        "5",
        "Cellobiose",
        "100",
        "G_PER_L",
        source=SRC_P1,
        identifier="CHEBI:17057",
        label="cellobiose",
        notes="P1 adds 3.5 ml of a sterile-filtered 100 g/L cellobiose stock to a 700 ml main solution.",
    ),
    _stock(
        "Yeast extract stock",
        "5",
        "Yeast extract",
        "100",
        "G_PER_L",
        source=SRC_P1,
        identifier="FOODON:03315426",
        label="yeast extract",
        notes="P1 adds 3.5 ml of a sterile-filtered 100 g/L yeast extract stock to a 700 ml main solution.",
    ),
    _stock(
        "Casamino acids stock",
        "5",
        "Casamino acids",
        "100",
        "G_PER_L",
        source=SRC_P1,
        identifier="FOODON:03315719",
        label="casamino acids",
        notes="P1 adds 3.5 ml of a sterile-filtered 100 g/L Casamino acids stock to a 700 ml main solution.",
    ),
    _stock(
        "Tryptone peptone stock",
        "5",
        "Tryptone peptone",
        "100",
        "G_PER_L",
        source=SRC_P1,
        identifier="MICRO:0000182",
        label="tryptone",
        notes="P1 adds 3.5 ml of a sterile-filtered 100 g/L Tryptone peptone stock to a 700 ml main solution.",
    ),
    _stock(
        "MgCl2 x 6 H2O stock",
        "11.2857",
        "MgCl2 x 6 H2O",
        "500",
        "G_PER_L",
        source=SRC_P1,
        identifier="CHEBI:86345",
        label="magnesium dichloride hexahydrate",
        notes="P1 adds 7.9 ml of a 500 g/L autoclaved MgCl2 x 6 H2O stock to a 700 ml main solution.",
    ),
    _stock(
        "MgSO4 x 7 H2O stock",
        "13.5714",
        "MgSO4 x 7 H2O",
        "500",
        "G_PER_L",
        source=SRC_P1,
        identifier="CHEBI:31795",
        label="magnesium sulfate heptahydrate",
        notes="P1 adds 9.5 ml of a 500 g/L autoclaved MgSO4 x 7 H2O stock to a 700 ml main solution.",
    ),
)

P8_STOCKS = (
    _stock(
        "MgSO4 stock",
        "327.8689",
        "MgSO4",
        "24.65",
        "G_PER_L",
        source=SRC_P8,
        identifier="CHEBI:32599",
        label="magnesium sulfate",
        notes="P8 adds 2 ml MgSO4 stock to a 6.1 ml main solution.",
    ),
    _stock(
        "CaCl2 stock",
        "1.63934",
        "CaCl2",
        "14.7",
        "G_PER_L",
        source=SRC_P8,
        identifier="CHEBI:3312",
        label="calcium dichloride",
        notes="P8 adds 10 uL CaCl2 stock to a 6.1 ml main solution.",
    ),
    _stock(
        "Sinigrin stock",
        "327.8689",
        "Sinigrin",
        "10",
        "G_PER_L",
        source=SRC_P8,
        notes=(
            "P8 adds 2 ml of a 10 g/L sinigrin stock filtered at 0.22 um in "
            "sterile water at pH 7.2 to a 6.1 ml main solution."
        ),
    ),
    _solution(
        "M9 stock",
        "327.8689",
        notes=(
            "P8 adds 2 ml M9 stock to a 6.1 ml main solution. The official "
            "public JSON represented this stock with a malformed solution id "
            "'NaN'; CultureMech preserves the named stock and drops that id."
        ),
        composition=[
            _component("Na2HPO4", "64", "G_PER_L", source=SRC_P8, identifier="CHEBI:34683", label="disodium hydrogenphosphate"),
            _component("KH2PO4", "51", "G_PER_L", source=SRC_P8, identifier="CHEBI:63036", label="potassium dihydrogen phosphate"),
            _component("NaCl", "2.5", "G_PER_L", source=SRC_P8, identifier="CHEBI:26710", label="sodium chloride"),
            _component("NH4Cl", "5", "G_PER_L", source=SRC_P8, identifier="CHEBI:31206", label="ammonium chloride"),
        ],
    ),
)

UPDATES = (
    RecipeUpdate(
        path=P1_HAHA,
        notes=(
            "MediaDive public Medium P1 provides a complete HaHa agar test "
            "recipe with a 700 ml main solution, washed Bacto agar, ASW 2x, "
            "Trace element solution SL-8, Selenite-tungstate solution II, and "
            "sterile stock additions; water fill-up rows were omitted."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ph_value": 7.5,
            "ingredients": [
                _component(
                    "HEPES",
                    "14.1714",
                    "G_PER_L",
                    source=SRC_P1,
                    identifier="CHEBI:42334",
                    label="2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid",
                    notes="P1 adds 9.92 g HEPES to a 700 ml main solution.",
                ),
                _component(
                    "Bacto agar",
                    "18",
                    "G_PER_L",
                    source=SRC_P1,
                    notes="P1 adds 18 g/L washed Bacto agar.",
                ),
            ],
            "solutions": [ASW_2X, SL8, SELENITE_TUNGSTATE, *P1_SINGLE_SOLUTE_STOCKS],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Mix Artificial sea water (ASW) 2x, HEPES, and a "
                        "magnetic stir bar, then fill to 650 ml with MilliQ water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": (
                        "Wash the Bacto agar with ultrapure water, allow the "
                        "agar to settle, remove the overlaying water, and "
                        "repeat the wash twice."
                    ),
                },
                {
                    "step_number": 3,
                    "action": "AUTOCLAVE",
                    "description": (
                        "Directly before autoclaving, mix agar and liquid, "
                        "autoclave, cool to 60 C, and hold at 55 C."
                    ),
                },
                {
                    "step_number": 4,
                    "action": "MIX",
                    "description": (
                        "Add sterile Trace element solution SL-8, "
                        "Selenite-tungstate solution II, phosphate, ammonium, "
                        "glucose, cellobiose, yeast extract, Casamino acids, "
                        "Tryptone peptone, magnesium chloride, and magnesium "
                        "sulfate stocks."
                    ),
                },
                {
                    "step_number": 5,
                    "action": "MIX",
                    "description": (
                        "Adjust to pH 7.5 with sterile 1 M HCl or 1 M NaOH, "
                        "then add sterile MilliQ water to a final volume of "
                        "700 ml while avoiding bubbles."
                    ),
                },
            ],
        },
        reference_urls=(P1_DOI, P1_PUBLIC),
    ),
    RecipeUpdate(
        path=P3_KING_B,
        notes=(
            "MediaDive public Medium P3 provides King B as a 1 L solid agar "
            "recipe at pH 7.2."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ph_value": 7.2,
            "ingredients": [
                _component("K2HPO4", "1.5", "G_PER_L", source=SRC_P3, identifier="CHEBI:131527", label="dipotassium hydrogen phosphate"),
                _component("MgSO4 x 7 H2O", "1.5", "G_PER_L", source=SRC_P3, identifier="CHEBI:31795", label="magnesium sulfate heptahydrate"),
                _component(
                    "Proteose peptone no. 3",
                    "20",
                    "G_PER_L",
                    source=SRC_P3,
                    identifier="MICRO:0000180",
                    label="proteose peptone",
                ),
                _component("Glycerol", "10", "ML_PER_L", source=SRC_P3, identifier="CHEBI:17754", label="glycerol"),
                _component("Agar", "15", "G_PER_L", source=SRC_P3, identifier="CHEBI:2509", label="agar"),
            ],
        },
        reference_urls=(P3_PUBLIC,),
    ),
    RecipeUpdate(
        path=P6_MTA10,
        notes=(
            "MediaDive public Medium P6 provides mTA10 as a complete 1 L "
            "liquid recipe at pH 7.2."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.2,
            "ingredients": [
                _component("Tryptose", "10", "G_PER_L", source=SRC_P6),
                _component("Beef extract", "5", "G_PER_L", source=SRC_P6),
                _component(
                    "Yeast extract",
                    "5",
                    "G_PER_L",
                    source=SRC_P6,
                    identifier="FOODON:03315426",
                    label="yeast extract",
                ),
                _component("NaCl", "5", "G_PER_L", source=SRC_P6, identifier="CHEBI:26710", label="sodium chloride"),
                _component(
                    "KH2PO4",
                    "3.4",
                    "G_PER_L",
                    source=SRC_P6,
                    identifier="CHEBI:63036",
                    label="potassium dihydrogen phosphate",
                ),
                _component(
                    "Na2HPO4",
                    "19.3",
                    "G_PER_L",
                    source=SRC_P6,
                    identifier="CHEBI:34683",
                    label="disodium hydrogenphosphate",
                ),
            ],
        },
        reference_urls=(P6_DOI, P6_PUBLIC),
    ),
    RecipeUpdate(
        path=P7_N27_RHODOSPIRILLACEAE,
        notes=(
            "MediaDive public Medium P7 provides the current N27 "
            "Rhodospirillaceae 1 L recipe with Fe(III) citrate, Vitamin B12, "
            "and Trace element solution SL-6 stocks."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 6.8,
            "ingredients": [
                _component(
                    "Yeast extract",
                    "0.3",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="FOODON:03315426",
                    label="yeast extract",
                ),
                _component("Disodium succinate", "1", "G_PER_L", source=SRC_P7),
                _component(
                    "Ammonium acetate",
                    "0.5",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="CHEBI:62947",
                    label="ammonium acetate",
                ),
                _component(
                    "KH2PO4",
                    "0.5",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="CHEBI:63036",
                    label="potassium dihydrogen phosphate",
                ),
                _component(
                    "MgSO4 x 7 H2O",
                    "0.4",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="CHEBI:31795",
                    label="magnesium sulfate heptahydrate",
                ),
                _component("NaCl", "0.4", "G_PER_L", source=SRC_P7, identifier="CHEBI:26710", label="sodium chloride"),
                _component("NH4Cl", "0.4", "G_PER_L", source=SRC_P7, identifier="CHEBI:31206", label="ammonium chloride"),
                _component(
                    "CaCl2 x 2 H2O",
                    "0.05",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="CHEBI:86158",
                    label="calcium chloride dihydrate",
                ),
                _component("Ethanol", "0.5", "ML_PER_L", source=SRC_P7, identifier="CHEBI:16236", label="ethanol"),
            ],
            "solutions": [
                _stock(
                    "Fe(III) citrate stock",
                    "5",
                    "Fe(III) citrate",
                    "1",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="CHEBI:144421",
                    label="Fe(III) citrate",
                    notes="P7 adds 5 ml of a 0.1% Fe(III) citrate stock in H2O.",
                ),
                _stock(
                    "Vitamin B12 stock",
                    "0.4",
                    "Vitamin B12",
                    "0.1",
                    "G_PER_L",
                    source=SRC_P7,
                    identifier="CHEBI:176843",
                    label="vitamin B12",
                    notes="P7 adds 0.4 ml of a 10 mg Vitamin B12 per 100 ml H2O stock.",
                ),
                _sl6(SRC_P7),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Mix the main solution, Fe(III) citrate stock, Vitamin B12 stock, and Trace element solution SL-6.",
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": "Adjust pH to 6.8.",
                },
                {
                    "step_number": 3,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
        },
        reference_urls=(P7_PUBLIC,),
    ),
    RecipeUpdate(
        path=P8_M9_SNG,
        notes=(
            "MediaDive public Medium P8 provides M9-SNG medium at pH 7.2 "
            "with MgSO4, CaCl2, sinigrin, and M9 stock additions. The public "
            "JSON assigned the M9 stock the malformed id 'NaN'; this record "
            "preserves the named M9 composition and drops that id."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.2,
            "ingredients": [],
            "solutions": list(P8_STOCKS),
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Prepare M9-SNG with MgSO4, CaCl2, sinigrin, and M9 "
                        "stock additions; use 0.22 um filtered sinigrin stock "
                        "prepared in sterile water at pH 7.2."
                    ),
                },
            ],
        },
        reference_urls=(P8_DOI, P8_PUBLIC),
    ),
    RecipeUpdate(
        path=P9_PDB_SNG,
        notes=(
            "MediaDive public Medium P9 currently downloads as Modified Medio "
            "Azunol and provides a 1 L agar recipe for methane-oxidizing "
            "cultivation with SL-10 and SL-6 trace element solutions. The "
            "legacy imported CultureMech label for P9 was PDB-SNG medium, but "
            "the DOI and current official public P9 recipe are retained here."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ph_range": {"min": 6.8, "max": 8.0},
            "ingredients": [
                _component(
                    "(NH4)2SO4",
                    "2",
                    "G_PER_L",
                    source=SRC_P9,
                    identifier="CHEBI:62946",
                    label="ammonium sulfate",
                ),
                _component(
                    "Fe(III) citrate",
                    "1",
                    "MICROG_PER_L",
                    source=SRC_P9,
                    identifier="CHEBI:144421",
                    label="Fe(III) citrate",
                ),
                _component(
                    "CuSO4",
                    "1",
                    "MICROG_PER_L",
                    source=SRC_P9,
                    identifier="CHEBI:23414",
                    label="copper(II) sulfate",
                ),
                _component("Agar", "20", "G_PER_L", source=SRC_P9, identifier="CHEBI:2509", label="agar"),
            ],
            "solutions": [_sl10(SRC_P9), _sl6(SRC_P9)],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Dissolve ingredients in distilled water and bring the "
                        "medium to 1 L."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": (
                        "Add 1-2 ml of the selected SL-10 or SL-6 trace element "
                        "solution; the official component table lists each "
                        "stock at 1 ml/L."
                    ),
                },
                {
                    "step_number": 3,
                    "action": "MIX",
                    "description": "Mix well and adjust pH with base or acid if necessary.",
                },
                {
                    "step_number": 4,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
                {
                    "step_number": 5,
                    "action": "MIX",
                    "description": "Use 10% CH4 gas as the methane source.",
                },
            ],
        },
        reference_urls=(P9_DOI, P9_PUBLIC),
    ),
    RecipeUpdate(
        path=P10_BEKISOLID,
        notes=(
            "MediaDive public Medium P10 provides the current Modified "
            "BekiSolidMedium agar recipe at pH 6.8-7.4. The official JSON "
            "lists an Elemento traza row in the main solution with amount 0 "
            "and a blank unit, so the trace-element solution composition is "
            "preserved with a variable addition volume rather than an invented "
            "ml/L dose."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ph_range": {"min": 6.8, "max": 7.4},
            "ingredients": [
                _component("NaCl", "25", "G_PER_L", source=SRC_P10, identifier="CHEBI:26710", label="sodium chloride"),
                _component(
                    "CaCl2 x 2 H2O",
                    "0.5",
                    "G_PER_L",
                    source=SRC_P10,
                    identifier="CHEBI:86158",
                    label="calcium chloride dihydrate",
                ),
                _component("NaHCO3", "0.2", "G_PER_L", source=SRC_P10, identifier="CHEBI:32139", label="sodium hydrogencarbonate"),
                _component("Phosphate buffer", "4", "G_PER_L", source=SRC_P10),
                _component("Na2S2O4", "0.5", "G_PER_L", source=SRC_P10, identifier="CHEBI:66870", label="sodium dithionite"),
                _component("KNO3", "1", "G_PER_L", source=SRC_P10, identifier="CHEBI:63043", label="potassium nitrate"),
                _component("Agar", "15", "G_PER_L", source=SRC_P10, identifier="CHEBI:2509", label="agar"),
            ],
            "solutions": [
                _variable_solution(
                    "Elemento traza",
                    notes=(
                        "P10 lists Elemento traza in the main solution with "
                        "amount 0 and a blank unit; the official recipe does "
                        "not disclose the stock volume added per liter."
                    ),
                    composition=[
                        _component("ZnSO4 x 7 H2O", "0.05", "G_PER_L", source=SRC_P10),
                        _component(
                            "FeSO4 x 7 H2O",
                            "0.01",
                            "G_PER_L",
                            source=SRC_P10,
                            identifier="CHEBI:75836",
                            label="iron(2+) sulfate heptahydrate",
                        ),
                        _component("MnCl2 x 4 H2O", "0.05", "G_PER_L", source=SRC_P10),
                        _component(
                            "CuSO4 x 5 H2O",
                            "0.05",
                            "G_PER_L",
                            source=SRC_P10,
                            identifier="CHEBI:31440",
                            label="copper(II) sulfate pentahydrate",
                            notes="The P10 stock table omits the unit, but the preparation text specifies 0.05 g.",
                        ),
                        _component("CuCl2", "0.01", "G_PER_L", source=SRC_P10, identifier="CHEBI:49553", label="CuCl2"),
                        _component("Fe(III)NH4-EDTA", "0.05", "G_PER_L", source=SRC_P10),
                        _component(
                            "(NH4)2MoO4",
                            "0.005",
                            "G_PER_L",
                            source=SRC_P10,
                            identifier="CHEBI:91249",
                            label="ammonium molybdate",
                        ),
                    ],
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Prepare the base in 1 L distilled water with NaCl, "
                        "CaCl2 x 2 H2O, NaHCO3, and phosphate buffer."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": (
                        "Add Na2S2O4 and prepare the Elemento traza solution "
                        "from ZnSO4 x 7 H2O, FeSO4 x 7 H2O, MnCl2 x 4 H2O, "
                        "CuSO4 x 5 H2O, CuCl2, Fe(III)NH4-EDTA, and "
                        "(NH4)2MoO4."
                    ),
                },
                {
                    "step_number": 3,
                    "action": "MIX",
                    "description": "Add KNO3 and agar to complete the solid medium.",
                },
            ],
        },
        reference_urls=(P10_PUBLIC,),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term") or {}
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term") or {}
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _require_target(doc: dict[str, Any], relative_path: str) -> None:
    expected_id = EXPECTED_IDS[relative_path]
    if doc.get("id") != expected_id:
        raise ValueError(
            f"{relative_path}: found id {doc.get('id')!r}, expected {expected_id!r}"
        )

    expected_source_term = EXPECTED_SOURCE_TERMS[relative_path]
    if _source_term_id(doc) != expected_source_term:
        raise ValueError(
            f"{relative_path}: found source term {_source_term_id(doc)!r}, "
            f"expected {expected_source_term!r}"
        )


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _composition_components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    components = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        nested = solution.get("composition") or []
        nested_components = (
            [i for i in nested if isinstance(i, dict)]
            if isinstance(nested, list)
            else []
        )
        components.extend(nested_components or [solution])
    return components


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    components = _composition_components(doc)
    if any(_grounded(component) for component in components):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    has_unmapped = any(not _grounded(component) for component in components)
    if has_unmapped:
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any], update: RecipeUpdate) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")

    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in update.reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _append_curation_event(doc: dict[str, Any], update: RecipeUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-30 public MediaDive placeholder graph",
        "source": "; ".join(update.reference_urls),
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


def _repair_with_recipe(doc: dict[str, Any], update: RecipeUpdate) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        if field in update.recipe:
            repaired[field] = copy.deepcopy(update.recipe[field])
        else:
            repaired.pop(field, None)
    repaired["notes"] = update.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for update in UPDATES:
        path = normalized / update.path
        doc = _load(path)
        _require_target(doc, update.path)
        plans[path] = _repair_with_recipe(doc, update)
    return plans


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
            changed = dump_record(doc) != path.read_text(encoding="utf-8")
        if changed:
            changed_count += 1
            print(path.relative_to(args.normalized_dir))

    action = "Updated" if args.apply else "Would update"
    print(f"{action} {changed_count} public MediaDive score-30 records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
