#!/usr/bin/env python3
"""Repair score-20 official simple recipes and additive wrappers."""

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

CURATOR = "repair_official_simple_score20.py"
ACTION = "RESOLVED_OFFICIAL_SIMPLE_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

BL_MALTOSE = "bacterial/bl_with_0_5_maltose.yaml"
BACTERIAL_MARINE_CAULOBACTER = "bacterial/marine_caulobacter_medium.yaml"
GAM_LACTOSE = "bacterial/gam_broth_with_1_lactose.yaml"
GAM_SEMISOLID = "bacterial/gam_semisolid.yaml"
BRUCELLA_DSMZ = "bacterial/brucella_agar.yaml"
BRUCELLA_JCM = "bacterial/brucella_blood_agar_with_hemin_menadione.yaml"
BRUCELLA_TOGO = "bacterial/TOGO_M696_Brucella_Blood_Agar_With_Hemin_Menadione.yaml"
CHOCOLATE_SHEEP_JCM = "bacterial/chocolate_agar_with_5_sheep_blood.yaml"
CHOCOLATE_SHEEP_TOGO = "bacterial/TOGO_M1366_Chocolate_Agar_With_5_Sheep_Blood.yaml"
CHM = "bacterial/chm.yaml"
DILUTE_MALT = "bacterial/dilute_filtered_malt_extract_agar.yaml"
FUNGAL_BL_MALTOSE = "fungal/bl_with_0_5_maltose.yaml"
FUNGAL_DILUTE_MALT = "fungal/dilute_filtered_malt_extract_agar.yaml"
FUNGAL_ISP4_YEAST = "fungal/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml"
FUNGAL_OATMEAL_YEAST = "fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml"
FUNGAL_SABOURAUD = "fungal/sabouraud_glucose_medium.yaml"
ISP_7 = "bacterial/isp_7_medium.yaml"
JCM_69 = "bacterial/jcm_medium_no_69.yaml"
JCM_69_TOGO = "bacterial/togo_medium_m61.yaml"
JCM_247 = "bacterial/jcm_medium_no_247.yaml"
M05 = "bacterial/m_05.yaml"
MODIFIED_GAM_AGAR = "bacterial/modified_gam_agar.yaml"
MODIFIED_GAM = "bacterial/modified_gam_broth.yaml"
MRS_FRUCTOSE = "bacterial/mrs_fructose_medium.yaml"
PBY = "bacterial/pby_medium.yaml"
QUARTER_MARINE = "bacterial/quarter_strength_marine_broth_2216.yaml"
REINFORCED_CLOSTRIDIAL = "bacterial/reinforced_clostridial_medium.yaml"
SEAWATER = "bacterial/seawater_medium.yaml"
SPECIALIZED_MARINE_CAULOBACTER = "specialized/marine_caulobacter_medium.yaml"
TODD_HEWITT_AGAR = "bacterial/todd_hewitt_agar.yaml"
TOMATO_JUICE_MILK = "bacterial/tomato_juice_milk_medium.yaml"
TOGO_M1446_SKIM_MILK = "bacterial/togo_medium_m1446.yaml"
TOGO_M1749_AGAR = "bacterial/togo_medium_m1749.yaml"
WEAK_OATMEAL = "bacterial/weak_oatmeal_agar.yaml"
BREWER_NACL = "specialized/brewer_anaerobic_agar_with_2_nacl.yaml"
HALF_MARINE_AGAR = "specialized/half_strength_marine_agar.yaml"
HALF_MARINE_NACL = "specialized/half_strength_marine_medium_with_1_0_nacl.yaml"
MARINE_CELLOBIOSE = "specialized/marine_broth_2216_with_cellobiose.yaml"

TOGO_M6 = "https://togomedium.org/medium/M6"
TOGO_M61 = "https://togomedium.org/medium/M61"
TOGO_M416 = "https://togomedium.org/medium/M416"
TOGO_M696 = "https://togomedium.org/medium/M696"
TOGO_M1115 = "https://togomedium.org/medium/M1115"
TOGO_M1366 = "https://togomedium.org/medium/M1366"
TOGO_M1446 = "https://togomedium.org/medium/M1446"
TOGO_M1749 = "https://togomedium.org/medium/M1749"
TOGO_M3285 = "https://togomedium.org/medium/M3285"

JCM_13 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=13"
JCM_50 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=50"
JCM_51 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=51"
JCM_58 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=58"
JCM_84 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=84"
JCM_191 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=191"
JCM_217 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=217"
JCM_418 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=418"
JCM_469 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=469"
JCM_68 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=68"
JCM_69_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=69"
JCM_677 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=677"
JCM_697 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=697"
JCM_245 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=245"
JCM_247_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=247"
JCM_612 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=612"
JCM_655 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=655"
JCM_667 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=667"
JCM_762 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=762"
JCM_853 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=853"
JCM_916 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=916"
JCM_1049 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1049"
JCM_1127 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1127"
JCM_1202 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1202"
JCM_1270 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1270"
JCM_1461 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1461"

DSMZ_1429 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1429.pdf"
DSMZ_1427 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1427.pdf"
DSMZ_1447 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1447.pdf"
DSMZ_1619 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1619.pdf"
DSMZ_1752 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1752.pdf"
DSMZ_353 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium353.pdf"
DSMZ_584 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium584.pdf"
DSMZ_601 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium601.pdf"
CCAP_CHM = "https://www.ccap.ac.uk/wp-content/uploads/MR_CHM.pdf"
NBRC_214 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=214"
NBRC_960 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=960"

BL_AGAR = {"id": "CultureMech:010107", "label": "BL Agar (Glucose Blood Liver Agar)"}
GYP_SODIUM_ACETATE = {
    "id": "CultureMech:003035",
    "label": "GYP-Sodium Acetate-Mineral Salts Broth",
}
ISP4 = {"id": "CultureMech:009900", "label": "Inorganic Salts-Starch Agar (ISP-4)"}
OATMEAL_ISP3 = {"id": "CultureMech:009815", "label": "Oatmeal Agar (ISP-3)"}

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
)


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    recipe: dict[str, Any]
    notes: str
    reference_urls: tuple[str, ...]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
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
    notes: str,
    term: dict[str, str] | None = None,
    composition: list[dict[str, Any]] | None = None,
    culturemech_term: dict[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
    }
    if term is not None:
        row["term"] = copy.deepcopy(term)
    if composition is not None:
        row["composition"] = copy.deepcopy(composition)
    if culturemech_term is not None:
        row["culturemech_term"] = copy.deepcopy(culturemech_term)
    return row


def _water(source: str, value: str = "1000") -> dict[str, Any]:
    return _ingredient(
        "Distilled water",
        value,
        "ML_PER_L",
        source=source,
        notes=f"{source} lists {value} ml distilled water.",
        term=("CHEBI:15377", "water"),
    )


def _agar(source: str, value: str = "15.0") -> dict[str, Any]:
    return _ingredient(
        "Agar",
        value,
        "G_PER_L",
        source=source,
        notes=f"{source} lists {value} g agar.",
        term=("CHEBI:2509", "agar"),
    )


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


HEMIN_SOLUTION = _solution(
    "Hemin solution",
    "10.0",
    notes="JCM Medium 677 lists 10.0 ml/L Hemin solution from JCM Medium 469.",
    composition=[
        _stock_component("Hemin", "0.5", "G_PER_L", ("CHEBI:50385", "hemin")),
        _stock_component("1 N NaOH", "10.0", "ML_PER_L", ("CHEBI:32145", "sodium hydroxide")),
    ],
)

MENADIONE_SOLUTION = _solution(
    "Menadione solution",
    "10.0",
    notes="JCM Medium 677 lists 10.0 ml/L Menadione solution from JCM Medium 469.",
    composition=[
        _stock_component("Menadione", "0.05", "G_PER_L", ("CHEBI:28869", "menadione")),
        _stock_component("Ethanol", "10.0", "ML_PER_L", ("CHEBI:16236", "ethanol")),
    ],
)


def _brucella_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(
                "Brucella agar (BD-BBL)",
                "43.0",
                "G_PER_L",
                source="JCM Medium 677",
                notes="JCM Medium 677 lists 43.0 g Brucella agar (BD-BBL).",
            ),
            _ingredient(
                "Horse blood",
                "50.0",
                "ML_PER_L",
                source="JCM Medium 677",
                notes="JCM Medium 677 lists 50.0 ml horse blood.",
            ),
            _water("JCM Medium 677"),
        ],
        "solutions": [HEMIN_SOLUTION, MENADIONE_SOLUTION],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Suspend 43.0 g Brucella agar (BD-BBL) in 1.0 L distilled water.",
            },
            {
                "step_number": 2,
                "action": "MIX",
                "description": "Add 50.0 ml/L horse blood, 10.0 ml/L hemin solution, and 10.0 ml/L menadione solution.",
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


def _brucella_dsmz_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(
                "Brucella agar",
                "1000",
                "ML_PER_L",
                source="DSMZ Medium 584",
                notes=(
                    "DSMZ Medium 584 says to prepare Brucella agar, e.g. "
                    "from Merck, before adding sheep blood."
                ),
                term=("MICRO:0000595", "Brucella agar"),
            ),
            _ingredient(
                "Sheep blood",
                "100",
                "ML_PER_L",
                source="DSMZ Medium 584",
                notes="DSMZ Medium 584 adds 100 ml/L sheep blood.",
                term=("UBERON:0000178", "blood"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Prepare Brucella agar according to the manufacturer's directions.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave the Brucella agar.",
            },
            {
                "step_number": 3,
                "action": "COOL",
                "description": "Cool the autoclaved Brucella agar to 50 C.",
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": "Add 100 ml/L sheep blood.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


def _chocolate_sheep_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(
                "Columbia blood agar base (BD-Difco)",
                "44.0",
                "G_PER_L",
                source="JCM Medium 1270",
                notes="JCM Medium 1270 lists 44.0 g Columbia blood agar base (BD-Difco).",
            ),
            _ingredient(
                "Sheep blood",
                "50.0",
                "ML_PER_L",
                source="JCM Medium 1270",
                notes="JCM Medium 1270 lists 50.0 ml sheep blood.",
                term=("UBERON:0000178", "blood"),
            ),
            _ingredient(
                "Distilled water",
                "950.0",
                "ML_PER_L",
                source="JCM Medium 1270",
                notes="JCM Medium 1270 lists 950.0 ml distilled water.",
                term=("CHEBI:15377", "water"),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Mix 44.0 g Columbia blood agar base (BD-Difco) "
                    "with 950.0 ml distilled water."
                ),
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave and cool to about 70 C.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": (
                    "Aseptically add 50.0 ml sterile defibrinated sheep "
                    "blood and keep at 70 C for 15 min."
                ),
            },
            {
                "step_number": 4,
                "action": "COOL",
                "description": "Cool to about 50 C.",
            },
            {
                "step_number": 5,
                "action": "POUR_PLATES",
                "description": "Mix and quickly dispense into sterile petri dishes.",
            },
        ],
        "sterilization": {"method": "AUTOCLAVE"},
    }


def _jcm_69_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(
                "NaCl",
                "50.0",
                "G_PER_L",
                source="JCM Medium 69",
                notes=(
                    "JCM Medium 69 supplements 1.0 L GYP-sodium acetate-mineral "
                    "salts broth with 50.0 g NaCl."
                ),
                term=("CHEBI:26710", "sodium chloride"),
            )
        ],
        "solutions": [
            _solution(
                "GYP-sodium acetate-mineral salts broth",
                "1000",
                notes=(
                    "JCM Medium 69 uses 1.0 L GYP-sodium acetate-mineral "
                    "salts broth from JCM Medium 68."
                ),
                culturemech_term=GYP_SODIUM_ACETATE,
            )
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Add 50.0 g/L NaCl to 1.0 L GYP-sodium "
                    "acetate-mineral salts broth."
                ),
            }
        ],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/gyp_sodium_acetate_mineral_salts_broth.yaml",
            "relationship": "SALINITY_VARIANT",
            "id": GYP_SODIUM_ACETATE["id"],
            "name": "gyp_sodium_acetate_mineral_salts_broth",
            "notes": (
                "Supplements 1.0 L GYP-sodium acetate-mineral salts broth "
                "with 50.0 g/L NaCl."
            ),
        },
        "variant_relationship": "SALINITY_VARIANT",
        "variant_modifications": [
            "Supplements 1.0 L GYP-sodium acetate-mineral salts broth with 50.0 g/L NaCl."
        ],
    }


TARGETS: tuple[Target, ...] = (
    Target(
        path=BL_MALTOSE,
        expected_id="CultureMech:009801",
        expected_media_term="TOGO:M416",
        notes="TOGO M416 mirrors JCM Medium 418: 1.0 L BL Agar with 5.0 g/L maltose.",
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Maltose",
                    "5.0",
                    "G_PER_L",
                    source="JCM Medium 418",
                    notes="JCM Medium 418 adds 5.0 g maltose to 1.0 L BL Agar.",
                    term=("CHEBI:18167", "alpha-maltose"),
                )
            ],
            "solutions": [
                _solution(
                    "BL Agar",
                    "1000",
                    notes="JCM Medium 418 uses 1.0 L BL Agar from JCM Medium 13.",
                    culturemech_term=BL_AGAR,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use 1.0 L BL Agar with 5.0 g/L maltose.",
                }
            ],
            "parent_media": {
                "path": "data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml",
                "relationship": "SUPPLEMENTED_VARIANT",
                "id": BL_AGAR["id"],
                "name": "bl_agar_glucose_blood_liver_agar",
                "notes": "Supplements 1.0 L BL Agar with 5.0 g/L maltose.",
            },
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": ["Supplements 1.0 L BL Agar with 5.0 g/L maltose."],
        },
        reference_urls=(TOGO_M416, JCM_418, TOGO_M6, JCM_13),
    ),
    Target(
        path=GAM_LACTOSE,
        expected_id="CultureMech:003042",
        expected_media_term="mediadive.medium:J697",
        notes=(
            "JCM Medium 697 contains 59.0 g GAM broth (Nissui), 10.0 g lactose, "
            "and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "GAM broth (Nissui)",
                    "59.0",
                    "G_PER_L",
                    source="JCM Medium 697",
                    notes="JCM Medium 697 lists 59.0 g GAM broth (Nissui).",
                ),
                _ingredient(
                    "Lactose",
                    "10.0",
                    "G_PER_L",
                    source="JCM Medium 697",
                    notes="JCM Medium 697 lists 10.0 g lactose.",
                    term=("CHEBI:17716", "lactose"),
                ),
                _water("JCM Medium 697"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Suspend 59.0 g GAM broth (Nissui) and 10.0 g lactose in 1.0 L distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_697,),
    ),
    Target(
        path=GAM_SEMISOLID,
        expected_id="CultureMech:003195",
        expected_media_term="mediadive.medium:J84",
        notes=(
            "JCM Medium 84 contains 59.0 g GAM broth (Nissui), 2.0 g agar, "
            "and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SEMISOLID",
            "ingredients": [
                _ingredient(
                    "GAM broth (Nissui)",
                    "59.0",
                    "G_PER_L",
                    source="JCM Medium 84",
                    notes="JCM Medium 84 lists 59.0 g GAM broth (Nissui).",
                ),
                _agar("JCM Medium 84", "2.0"),
                _water("JCM Medium 84"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Suspend 59.0 g GAM broth (Nissui) and 2.0 g agar in 1.0 L distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_84,),
    ),
    Target(
        path=BRUCELLA_JCM,
        expected_id="CultureMech:003022",
        expected_media_term="mediadive.medium:J677",
        notes=(
            "JCM Medium 677 contains 43.0 g Brucella agar (BD-BBL), 50.0 ml "
            "horse blood, 10.0 ml hemin solution, 10.0 ml menadione solution, "
            "and 1.0 L distilled water."
        ),
        recipe=_brucella_recipe(),
        reference_urls=(JCM_677, JCM_469),
    ),
    Target(
        path=BRUCELLA_TOGO,
        expected_id="CultureMech:010102",
        expected_media_term="TOGO:M696",
        notes=(
            "TOGO M696 mirrors JCM Medium 677: 43.0 g Brucella agar (BD-BBL), "
            "50.0 ml horse blood, 10.0 ml hemin solution, 10.0 ml menadione "
            "solution, and 1.0 L distilled water."
        ),
        recipe=_brucella_recipe(),
        reference_urls=(TOGO_M696, JCM_677, JCM_469),
    ),
    Target(
        path=BRUCELLA_DSMZ,
        expected_id="CultureMech:001710",
        expected_media_term="mediadive.medium:584",
        notes=(
            "DSMZ Medium 584 directs preparing Brucella agar, cooling it to "
            "50 C after autoclaving, and adding 100 ml/L sheep blood."
        ),
        recipe=_brucella_dsmz_recipe(),
        reference_urls=(DSMZ_584,),
    ),
    Target(
        path=CHOCOLATE_SHEEP_JCM,
        expected_id="CultureMech:002436",
        expected_media_term="mediadive.medium:J1270",
        notes=(
            "JCM Medium 1270 contains 44.0 g Columbia blood agar base "
            "(BD-Difco), 50.0 ml sheep blood, and 950.0 ml distilled water."
        ),
        recipe=_chocolate_sheep_recipe(),
        reference_urls=(JCM_1270,),
    ),
    Target(
        path=CHOCOLATE_SHEEP_TOGO,
        expected_id="CultureMech:007904",
        expected_media_term="TOGO:M1366",
        notes=(
            "TOGO M1366 mirrors JCM Medium 1270: 44.0 g Columbia blood "
            "agar base (BD-Difco), 50.0 ml sheep blood, and 950.0 ml "
            "distilled water."
        ),
        recipe=_chocolate_sheep_recipe(),
        reference_urls=(TOGO_M1366, JCM_1270),
    ),
    Target(
        path=CHM,
        expected_id="CultureMech:000331",
        expected_media_term="mediadive.medium:C23",
        notes=(
            "CCAP CHM contains 1.0 g sodium acetate trihydrate, 1.0 g "
            "Lab-Lemco powder, and 1.0 L deionised water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Sodium acetate x 3 H2O",
                    "1.0",
                    "G_PER_L",
                    source="CCAP CHM",
                    notes="CCAP CHM lists 1.0 g sodium acetate trihydrate.",
                    term=("CHEBI:32954", "sodium acetate"),
                ),
                _ingredient(
                    "Lab-Lemco powder",
                    "1.0",
                    "G_PER_L",
                    source="CCAP CHM",
                    notes="CCAP CHM lists 1.0 g Lab-Lemco powder.",
                ),
                _ingredient(
                    "Deionised water",
                    "1000",
                    "ML_PER_L",
                    source="CCAP CHM",
                    notes="CCAP CHM says to add the constituents to 1 litre of deionised water.",
                    term=("CHEBI:15377", "water"),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Add constituents to 1 litre of deionised water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 15 psi for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(CCAP_CHM,),
    ),
    Target(
        path=DILUTE_MALT,
        expected_id="CultureMech:004153",
        expected_media_term="komodo.medium:1427",
        notes=(
            "DSMZ Medium 1427 prepares a 5.0 g/L malt extract filtrate, fills "
            "to 1.0 L, and adds 15.0 g agar."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Malt extract",
                    "5.0",
                    "G_PER_L",
                    source="DSMZ Medium 1427",
                    notes="DSMZ Medium 1427 extracts 5 g malt extract in 100 ml water and fills the filtered liquid to 1 L.",
                ),
                _agar("DSMZ Medium 1427", "15.0"),
                _water("DSMZ Medium 1427"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Mix 5 g malt extract with 100 ml distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave for 15 min and cool.",
                },
                {
                    "step_number": 3,
                    "action": "FILTER",
                    "description": "Filter until clear and fill to 1 L.",
                },
                {
                    "step_number": 4,
                    "action": "ADD_AGAR",
                    "description": "Add 15 g agar.",
                },
                {
                    "step_number": 5,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(DSMZ_1427,),
    ),
    Target(
        path=ISP_7,
        expected_id="CultureMech:001099",
        expected_media_term="mediadive.medium:1619",
        notes=(
            "DSMZ Medium 1619 contains 23.74 g ISP 7 Medium (Himedia), "
            "15.00 ml glycerol, and 1000.00 ml distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "ISP 7 Medium (Himedia)",
                    "23.74",
                    "G_PER_L",
                    source="DSMZ Medium 1619",
                    notes="DSMZ Medium 1619 lists 23.74 g ISP 7 Medium (Himedia).",
                ),
                _ingredient(
                    "Glycerol",
                    "15.00",
                    "ML_PER_L",
                    source="DSMZ Medium 1619",
                    notes="DSMZ Medium 1619 lists 15.00 ml glycerol.",
                    term=("CHEBI:17754", "glycerol"),
                ),
                _ingredient(
                    "Distilled water",
                    "1000.00",
                    "ML_PER_L",
                    source="DSMZ Medium 1619",
                    notes="DSMZ Medium 1619 lists 1000.00 ml distilled water.",
                    term=("CHEBI:15377", "water"),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Dissolve 23.74 g ISP 7 Medium (Himedia) and 15.00 ml "
                        "glycerol in 1000.00 ml distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(DSMZ_1619,),
    ),
    Target(
        path=JCM_69,
        expected_id="CultureMech:003045",
        expected_media_term="mediadive.medium:J69",
        notes=(
            "JCM Medium 69 contains 1.0 L GYP-sodium acetate-mineral salts broth "
            "from JCM Medium 68 plus 50.0 g/L NaCl."
        ),
        recipe=_jcm_69_recipe(),
        reference_urls=(JCM_69_URL, JCM_68),
    ),
    Target(
        path=JCM_69_TOGO,
        expected_id="CultureMech:010019",
        expected_media_term="TOGO:M61",
        notes=(
            "TOGO M61 points to JCM Medium 69, which contains 1.0 L "
            "GYP-sodium acetate-mineral salts broth from JCM Medium 68 plus "
            "50.0 g/L NaCl."
        ),
        recipe=_jcm_69_recipe(),
        reference_urls=(TOGO_M61, JCM_69_URL, JCM_68),
    ),
    Target(
        path=JCM_247,
        expected_id="CultureMech:002608",
        expected_media_term="mediadive.medium:J247",
        notes=(
            "JCM Medium 247 contains 5.0 g yeast extract, 20.0 g glucose, "
            "and 1.0 L distilled water, with pH 6.8-7.0."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_range": {
                "min": 6.8,
                "max": 7.0,
                "notes": "JCM Medium 247 states pH 6.8-7.0.",
            },
            "ingredients": [
                _ingredient(
                    "Yeast extract",
                    "5.0",
                    "G_PER_L",
                    source="JCM Medium 247",
                    notes="JCM Medium 247 lists 5.0 g yeast extract.",
                    term=("FOODON:03315426", "yeast extract"),
                ),
                _ingredient(
                    "Glucose",
                    "20.0",
                    "G_PER_L",
                    source="JCM Medium 247",
                    notes="JCM Medium 247 lists 20.0 g glucose.",
                    term=("CHEBI:17234", "glucose"),
                ),
                _water("JCM Medium 247"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Dissolve 5.0 g yeast extract and 20.0 g glucose in "
                        "1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 6.8-7.0.",
                },
                {
                    "step_number": 3,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_247_URL,),
    ),
    Target(
        path=TOGO_M1446_SKIM_MILK,
        expected_id="CultureMech:007986",
        expected_media_term="TOGO:M1446",
        notes="TOGO M1446 points to NBRC Medium 214: 100 g skim milk in 1 L distilled water.",
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Skim milk",
                    "100",
                    "G_PER_L",
                    source="NBRC Medium 214",
                    notes="NBRC Medium 214 lists 100 g skim milk.",
                ),
                _water("NBRC Medium 214"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Mix 100 g/L skim milk in 1 L distilled water.",
                }
            ],
        },
        reference_urls=(TOGO_M1446, NBRC_214),
    ),
    Target(
        path=TOGO_M1749_AGAR,
        expected_id="CultureMech:008312",
        expected_media_term="TOGO:M1749",
        notes=(
            "TOGO M1749 points to NBRC Medium 960: 15 g agar in 1 L "
            "distilled water, pH around 5.5."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ph_value": 5.5,
            "ingredients": [
                _ingredient(
                    "Agar",
                    "15",
                    "G_PER_L",
                    source="NBRC Medium 960",
                    notes="NBRC Medium 960 lists 15 g agar.",
                    term=("CHEBI:2509", "agar"),
                ),
                _water("NBRC Medium 960"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Mix 15 g/L agar in 1 L distilled water.",
                }
            ],
        },
        reference_urls=(TOGO_M1749, NBRC_960),
    ),
    Target(
        path=PBY,
        expected_id="CultureMech:002553",
        expected_media_term="mediadive.medium:J191",
        notes=(
            "JCM Medium 191 contains 5.0 g Bacto peptone (BD-Difco), "
            "3.0 g beef extract (BD-Difco), 1.0 g yeast extract (BD-Difco), "
            "and 1.0 L distilled water, adjusted to pH 7.0."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.0,
            "ingredients": [
                _ingredient(
                    "Bacto peptone",
                    "5.0",
                    "G_PER_L",
                    source="JCM Medium 191",
                    notes="JCM Medium 191 lists 5.0 g Bacto peptone (BD-Difco).",
                    term=("MICRO:0000178", "Bacto peptone"),
                ),
                _ingredient(
                    "Beef extract",
                    "3.0",
                    "G_PER_L",
                    source="JCM Medium 191",
                    notes="JCM Medium 191 lists 3.0 g Beef extract (BD-Difco).",
                    term=("FOODON:03302088", "Beef extract"),
                ),
                _ingredient(
                    "Yeast extract",
                    "1.0",
                    "G_PER_L",
                    source="JCM Medium 191",
                    notes="JCM Medium 191 lists 1.0 g Yeast extract (BD-Difco).",
                    term=("FOODON:03315426", "yeast extract"),
                ),
                _water("JCM Medium 191"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Mix Bacto peptone, beef extract, yeast extract, and "
                        "1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 7.0.",
                },
            ],
        },
        reference_urls=(JCM_191,),
    ),
    Target(
        path=SEAWATER,
        expected_id="CultureMech:001225",
        expected_media_term="mediadive.medium:1752",
        notes=(
            "DSMZ Medium 1752 contains 2.5 g Bacto Peptone, 0.5 g "
            "Bacto Yeast extract, and 1000.0 ml Biomaris Seawater, "
            "adjusted to pH 7.5."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.5,
            "ingredients": [
                _ingredient(
                    "Bacto Peptone",
                    "2.5",
                    "G_PER_L",
                    source="DSMZ Medium 1752",
                    notes="DSMZ Medium 1752 lists 2.5 g Bacto Peptone.",
                    term=("MICRO:0000178", "Bacto peptone"),
                ),
                _ingredient(
                    "Bacto Yeast extract",
                    "0.5",
                    "G_PER_L",
                    source="DSMZ Medium 1752",
                    notes="DSMZ Medium 1752 lists 0.5 g Bacto Yeast extract.",
                    term=("FOODON:03315426", "yeast extract"),
                ),
                _ingredient(
                    "Biomaris Seawater",
                    "1000.0",
                    "ML_PER_L",
                    source="DSMZ Medium 1752",
                    notes="DSMZ Medium 1752 lists 1000.0 ml Biomaris Seawater.",
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Mix 2.5 g Bacto Peptone, 0.5 g Bacto Yeast extract, "
                        "and 1000.0 ml Biomaris Seawater."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 7.5.",
                },
            ],
        },
        reference_urls=(DSMZ_1752,),
    ),
    Target(
        path=TOMATO_JUICE_MILK,
        expected_id="CultureMech:001453",
        expected_media_term="mediadive.medium:353",
        notes=(
            "DSMZ Medium 353 contains 100.0 g skim milk, 100.0 ml "
            "tomato juice, 5.0 g yeast extract, and 1000.0 ml distilled "
            "water, adjusted to pH 7.0."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_value": 7.0,
            "ingredients": [
                _ingredient(
                    "Skim milk",
                    "100.0",
                    "G_PER_L",
                    source="DSMZ Medium 353",
                    notes="DSMZ Medium 353 lists 100.0 g skim milk.",
                ),
                _ingredient(
                    "Tomato juice",
                    "100.0",
                    "ML_PER_L",
                    source="DSMZ Medium 353",
                    notes="DSMZ Medium 353 lists 100.0 ml tomato juice.",
                    term=("FOODON:03301454", "Tomato juice"),
                ),
                _ingredient(
                    "Yeast extract",
                    "5.0",
                    "G_PER_L",
                    source="DSMZ Medium 353",
                    notes="DSMZ Medium 353 lists 5.0 g yeast extract.",
                    term=("FOODON:03315426", "yeast extract"),
                ),
                _ingredient(
                    "Distilled water",
                    "1000.0",
                    "ML_PER_L",
                    source="DSMZ Medium 353",
                    notes="DSMZ Medium 353 lists 1000.0 ml distilled water.",
                    term=("CHEBI:15377", "water"),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "FILTER",
                    "description": (
                        "Filter canned tomatoes through paper and leave "
                        "overnight at 10 C."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "MIX",
                    "description": (
                        "Mix 100.0 g skim milk, 100.0 ml tomato juice, "
                        "5.0 g yeast extract, and 1000.0 ml distilled water."
                    ),
                },
                {
                    "step_number": 3,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 7.0.",
                },
            ],
        },
        reference_urls=(DSMZ_353,),
    ),
    Target(
        path=M05,
        expected_id="CultureMech:000910",
        expected_media_term="mediadive.medium:1447",
        notes=(
            "DSMZ Medium 1447 contains 5.0 g malt extract powder, 1.0 L water, "
            "and 15.0 g agar."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Malt extract powder",
                    "5.0",
                    "G_PER_L",
                    source="DSMZ Medium 1447",
                    notes="DSMZ Medium 1447 lists 5.0 g malt extract powder.",
                ),
                _ingredient(
                    "Water",
                    "1000",
                    "ML_PER_L",
                    source="DSMZ Medium 1447",
                    notes="DSMZ Medium 1447 lists 1.0 L water.",
                    term=("CHEBI:15377", "water"),
                ),
                _agar("DSMZ Medium 1447", "15.0"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Dissolve 5.0 g malt extract powder in 1.0 L water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave for 15 min at 121 C.",
                },
                {
                    "step_number": 3,
                    "action": "FILTER",
                    "description": "Filter until entirely clear and fill up to 1.0 L.",
                },
                {
                    "step_number": 4,
                    "action": "ADD_AGAR",
                    "description": "Add 15.0 g agar.",
                },
                {
                    "step_number": 5,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave again.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(DSMZ_1447,),
    ),
    Target(
        path=BACTERIAL_MARINE_CAULOBACTER,
        expected_id="CultureMech:006089",
        expected_media_term="komodo.medium:601",
        notes=(
            "KOMODO Medium 601 resolves to DSMZ Medium 601, which contains "
            "3.0 g yeast extract, 10.0 g Proteose peptone (Difco 0120), "
            "and 1000.0 ml artificial sea water, with pH 7.2-7.4."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_range": {
                "min": 7.2,
                "max": 7.4,
                "notes": "DSMZ Medium 601 states pH 7.2-7.4.",
            },
            "ingredients": [
                _ingredient(
                    "Yeast extract",
                    "3.0",
                    "G_PER_L",
                    source="DSMZ Medium 601",
                    notes="DSMZ Medium 601 lists 3.0 g yeast extract.",
                    term=("FOODON:03315426", "Yeast extract"),
                ),
                _ingredient(
                    "Proteose peptone (Difco 0120)",
                    "10.0",
                    "G_PER_L",
                    source="DSMZ Medium 601",
                    notes="DSMZ Medium 601 lists 10.0 g Proteose peptone (Difco 0120).",
                    term=("MICRO:0000180", "Proteose Peptone"),
                ),
                _ingredient(
                    "Artificial sea water",
                    "1000.0",
                    "ML_PER_L",
                    source="DSMZ Medium 601",
                    notes=(
                        "DSMZ Medium 601 lists 1000.0 ml artificial sea water "
                        "prepared from marine aquarium salt mixtures."
                    ),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Mix 3.0 g yeast extract, 10.0 g Proteose peptone "
                        "(Difco 0120), and 1000.0 ml artificial sea water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 7.2-7.4.",
                },
            ],
        },
        reference_urls=(DSMZ_601,),
    ),
    Target(
        path=SPECIALIZED_MARINE_CAULOBACTER,
        expected_id="CultureMech:015363",
        expected_media_term="mediadive.medium:601",
        notes=(
            "DSMZ Medium 601 contains 3.0 g yeast extract, 10.0 g Proteose "
            "peptone (Difco 0120), and 1000.0 ml artificial sea water, with "
            "pH 7.2-7.4."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ph_range": {
                "min": 7.2,
                "max": 7.4,
                "notes": "DSMZ Medium 601 states pH 7.2-7.4.",
            },
            "ingredients": [
                _ingredient(
                    "Yeast extract",
                    "3.0",
                    "G_PER_L",
                    source="DSMZ Medium 601",
                    notes="DSMZ Medium 601 lists 3.0 g yeast extract.",
                    term=("FOODON:03315426", "Yeast extract"),
                ),
                _ingredient(
                    "Proteose peptone (Difco 0120)",
                    "10.0",
                    "G_PER_L",
                    source="DSMZ Medium 601",
                    notes="DSMZ Medium 601 lists 10.0 g Proteose peptone (Difco 0120).",
                    term=("MICRO:0000180", "Proteose Peptone"),
                ),
                _ingredient(
                    "Artificial sea water",
                    "1000.0",
                    "ML_PER_L",
                    source="DSMZ Medium 601",
                    notes=(
                        "DSMZ Medium 601 lists 1000.0 ml artificial sea water "
                        "prepared from marine aquarium salt mixtures."
                    ),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Mix 3.0 g yeast extract, 10.0 g Proteose peptone "
                        "(Difco 0120), and 1000.0 ml artificial sea water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "ADJUST_PH",
                    "description": "Adjust pH to 7.2-7.4.",
                },
            ],
        },
        reference_urls=(DSMZ_601,),
    ),
    Target(
        path=REINFORCED_CLOSTRIDIAL,
        expected_id="CultureMech:002960",
        expected_media_term="mediadive.medium:J612",
        notes=(
            "JCM Medium 612 contains 38.0 g Reinforced clostridial medium "
            "(BD-Difco), 15.0 g agar, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Reinforced clostridial medium (BD-Difco)",
                    "38.0",
                    "G_PER_L",
                    source="JCM Medium 612",
                    notes=(
                        "JCM Medium 612 lists 38.0 g Reinforced clostridial "
                        "medium (BD-Difco)."
                    ),
                ),
                _agar("JCM Medium 612", "15.0"),
                _water("JCM Medium 612"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 38.0 g Reinforced clostridial medium "
                        "(BD-Difco) and 15.0 g agar in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_612,),
    ),
    Target(
        path=WEAK_OATMEAL,
        expected_id="CultureMech:002371",
        expected_media_term="mediadive.medium:J1202",
        notes=(
            "JCM Medium 1202 contains 15.0 g oatmeal agar (BD-Difco), "
            "12.0 g agar, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Oatmeal agar (BD-Difco)",
                    "15.0",
                    "G_PER_L",
                    source="JCM Medium 1202",
                    notes="JCM Medium 1202 lists 15.0 g oatmeal agar (BD-Difco).",
                ),
                _agar("JCM Medium 1202", "12.0"),
                _water("JCM Medium 1202"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 15.0 g oatmeal agar (BD-Difco) and 12.0 g "
                        "agar in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_1202,),
    ),
    Target(
        path=TODD_HEWITT_AGAR,
        expected_id="CultureMech:002606",
        expected_media_term="mediadive.medium:J245",
        notes=(
            "JCM Medium 245 contains 30.0 g Todd Hewitt Broth (BD-Difco), "
            "15.0 g agar, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Todd Hewitt Broth (BD-Difco)",
                    "30.0",
                    "G_PER_L",
                    source="JCM Medium 245",
                    notes="JCM Medium 245 lists 30.0 g Todd Hewitt Broth (BD-Difco).",
                ),
                _agar("JCM Medium 245", "15.0"),
                _water("JCM Medium 245"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 30.0 g Todd Hewitt Broth (BD-Difco) and 15.0 g "
                        "agar in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_245,),
    ),
    Target(
        path=MRS_FRUCTOSE,
        expected_id="CultureMech:003199",
        expected_media_term="mediadive.medium:J853",
        notes=(
            "JCM Medium 853 contains 55.0 g Lactobacilli MRS broth "
            "(BD-Difco), 10.0 g fructose, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Lactobacilli MRS broth (BD-Difco)",
                    "55.0",
                    "G_PER_L",
                    source="JCM Medium 853",
                    notes="JCM Medium 853 lists 55.0 g Lactobacilli MRS broth (BD-Difco).",
                ),
                _ingredient(
                    "Fructose",
                    "10.0",
                    "G_PER_L",
                    source="JCM Medium 853",
                    notes="JCM Medium 853 lists 10.0 g fructose.",
                    term=("CHEBI:28757", "fructose"),
                ),
                _water("JCM Medium 853"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 55.0 g Lactobacilli MRS broth (BD-Difco) "
                        "and 10.0 g fructose in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_853,),
    ),
    Target(
        path=QUARTER_MARINE,
        expected_id="CultureMech:007635",
        expected_media_term="TOGO:M1115",
        notes=(
            "TOGO M1115 mirrors JCM Medium 1049: 9.35 g Marine broth 2216 "
            "(BD-Difco) in 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Marine broth 2216 (BD-Difco)",
                    "9.35",
                    "G_PER_L",
                    source="JCM Medium 1049",
                    notes="JCM Medium 1049 lists 9.35 g Marine broth 2216 (BD-Difco).",
                ),
                _water("JCM Medium 1049"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 9.35 g Marine broth 2216 (BD-Difco) in "
                        "1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
            "parent_media": {
                "path": "data/normalized_yaml/bacterial/TOGO_M33_Marine_Broth_2216.yaml",
                "relationship": "CONCENTRATION_VARIANT",
                "id": "CultureMech:009718",
                "name": "marine_broth_2216",
                "notes": (
                    "Uses one-quarter-strength Marine broth 2216 at 9.35 g/L "
                    "instead of the full 37.4 g/L."
                ),
            },
            "variant_relationship": "CONCENTRATION_VARIANT",
            "variant_modifications": [
                "Uses 9.35 g/L Marine broth 2216 (BD-Difco)."
            ],
        },
        reference_urls=(TOGO_M1115, JCM_1049),
    ),
    Target(
        path=MODIFIED_GAM,
        expected_id="CultureMech:009699",
        expected_media_term="TOGO:M3285",
        notes=(
            "TOGO M3285 mirrors JCM Medium 1461: 41.7 g GAM broth, modified "
            "(Nissui) in 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "GAM broth, modified (Nissui)",
                    "41.7",
                    "G_PER_L",
                    source="JCM Medium 1461",
                    notes="JCM Medium 1461 lists 41.7 g GAM broth, modified (Nissui).",
                ),
                _water("JCM Medium 1461"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 41.7 g GAM broth, modified (Nissui) in "
                        "1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(TOGO_M3285, JCM_1461),
    ),
    Target(
        path=MODIFIED_GAM_AGAR,
        expected_id="CultureMech:003001",
        expected_media_term="mediadive.medium:J655",
        notes=(
            "JCM Medium 655 contains 56.7 g GAM agar, modified (Nissui), "
            "and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "GAM agar, modified (Nissui)",
                    "56.7",
                    "G_PER_L",
                    source="JCM Medium 655",
                    notes="JCM Medium 655 lists 56.7 g GAM agar, modified (Nissui).",
                ),
                _water("JCM Medium 655"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 56.7 g GAM agar, modified (Nissui), in "
                        "1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_655,),
    ),
    Target(
        path=FUNGAL_BL_MALTOSE,
        expected_id="CultureMech:010526",
        expected_media_term="mediadive.medium:J418",
        notes="JCM Medium 418 contains 1.0 L BL Agar with 5.0 g/L maltose.",
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Maltose",
                    "5.0",
                    "G_PER_L",
                    source="JCM Medium 418",
                    notes="JCM Medium 418 adds 5.0 g maltose to 1.0 L BL Agar.",
                    term=("CHEBI:18167", "alpha-maltose"),
                )
            ],
            "solutions": [
                _solution(
                    "BL Agar",
                    "1000",
                    notes="JCM Medium 418 uses 1.0 L BL Agar from JCM Medium 13.",
                    culturemech_term=BL_AGAR,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Use 1.0 L BL Agar with 5.0 g/L maltose.",
                }
            ],
            "parent_media": {
                "path": "data/normalized_yaml/bacterial/TOGO_M6_BL_Agar_Glucose_Blood_Liver_Agar.yaml",
                "relationship": "SUPPLEMENTED_VARIANT",
                "id": BL_AGAR["id"],
                "name": "bl_agar_glucose_blood_liver_agar",
                "notes": "Supplements 1.0 L BL Agar with 5.0 g/L maltose.",
            },
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": ["Supplements 1.0 L BL Agar with 5.0 g/L maltose."],
        },
        reference_urls=(JCM_418, JCM_13),
    ),
    Target(
        path=FUNGAL_DILUTE_MALT,
        expected_id="CultureMech:010452",
        expected_media_term="mediadive.medium:1427",
        notes=(
            "DSMZ Medium 1427 prepares a 5.0 g/L malt extract filtrate, fills "
            "to 1.0 L, and adds 15.0 g agar."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Malt extract",
                    "5.0",
                    "G_PER_L",
                    source="DSMZ Medium 1427",
                    notes="DSMZ Medium 1427 extracts 5 g malt extract in 100 ml water and fills the filtered liquid to 1 L.",
                ),
                _agar("DSMZ Medium 1427", "15.0"),
                _water("DSMZ Medium 1427"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Mix 5 g malt extract with 100 ml distilled water.",
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave for 15 min and cool.",
                },
                {
                    "step_number": 3,
                    "action": "FILTER",
                    "description": "Filter until clear and fill to 1 L.",
                },
                {
                    "step_number": 4,
                    "action": "ADD_AGAR",
                    "description": "Add 15 g agar.",
                },
                {
                    "step_number": 5,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(DSMZ_1427,),
    ),
    Target(
        path=FUNGAL_OATMEAL_YEAST,
        expected_id="CultureMech:010531",
        expected_media_term="mediadive.medium:J51",
        notes=(
            "JCM Medium 51 contains 1.0 L Oatmeal agar (ISP-3) from JCM "
            "Medium 50 plus 1.0 g/L Yeast extract (BD-Difco)."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Yeast extract",
                    "1.0",
                    "G_PER_L",
                    source="JCM Medium 51",
                    notes=(
                        "JCM Medium 51 supplements 1.0 L Oatmeal agar "
                        "(ISP-3) with 1.0 g Yeast extract (BD-Difco)."
                    ),
                    term=("FOODON:03315426", "yeast extract"),
                )
            ],
            "solutions": [
                _solution(
                    "Oatmeal agar (ISP-3)",
                    "1000",
                    notes=(
                        "JCM Medium 51 uses 1.0 L Oatmeal agar (ISP-3) "
                        "from JCM Medium 50."
                    ),
                    culturemech_term=OATMEAL_ISP3,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Use 1.0 L Oatmeal agar (ISP-3) with 1.0 g/L "
                        "Yeast extract (BD-Difco)."
                    ),
                }
            ],
            "parent_media": {
                "path": "data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml",
                "relationship": "SUPPLEMENTED_VARIANT",
                "id": OATMEAL_ISP3["id"],
                "name": "oatmeal_agar_isp_3",
                "notes": (
                    "Supplements 1.0 L Oatmeal agar (ISP-3) with 1.0 g/L "
                    "Yeast extract (BD-Difco)."
                ),
            },
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": [
                (
                    "Supplements 1.0 L Oatmeal agar (ISP-3) with 1.0 g/L "
                    "Yeast extract (BD-Difco)."
                )
            ],
        },
        reference_urls=(JCM_51, JCM_50),
    ),
    Target(
        path=FUNGAL_ISP4_YEAST,
        expected_id="CultureMech:010510",
        expected_media_term="mediadive.medium:J217",
        notes=(
            "JCM Medium 217 contains 1.0 L Inorganic salts-starch agar "
            "(ISP-4) from JCM Medium 58 plus 0.5 g/L Yeast extract."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Yeast extract",
                    "0.5",
                    "G_PER_L",
                    source="JCM Medium 217",
                    notes=(
                        "JCM Medium 217 supplements 1.0 L Inorganic "
                        "salts-starch agar (ISP-4) with 0.5 g Yeast extract."
                    ),
                    term=("FOODON:03315426", "yeast extract"),
                )
            ],
            "solutions": [
                _solution(
                    "Inorganic salts-starch agar (ISP-4)",
                    "1000",
                    notes=(
                        "JCM Medium 217 uses 1.0 L Inorganic salts-starch "
                        "agar (ISP-4) from JCM Medium 58."
                    ),
                    culturemech_term=ISP4,
                )
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Use 1.0 L Inorganic salts-starch agar (ISP-4) "
                        "with 0.5 g/L Yeast extract."
                    ),
                }
            ],
            "parent_media": {
                "path": (
                    "data/normalized_yaml/bacterial/"
                    "TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml"
                ),
                "relationship": "SUPPLEMENTED_VARIANT",
                "id": ISP4["id"],
                "name": "inorganic_salts_starch_agar_isp_4",
                "notes": (
                    "Supplements 1.0 L Inorganic salts-starch agar (ISP-4) "
                    "with 0.5 g/L Yeast extract."
                ),
            },
            "variant_relationship": "SUPPLEMENTED_VARIANT",
            "variant_modifications": [
                (
                    "Supplements 1.0 L Inorganic salts-starch agar (ISP-4) "
                    "with 0.5 g/L Yeast extract."
                )
            ],
        },
        reference_urls=(JCM_217, JCM_58),
    ),
    Target(
        path=FUNGAL_SABOURAUD,
        expected_id="CultureMech:010453",
        expected_media_term="mediadive.medium:1429",
        notes=(
            "DSMZ Medium 1429 contains 30.0 g SABOURAUD-2% "
            "Glucose-Bouillon (Merck 108339), 15.0 g agar, and 1000.0 ml "
            "distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "SABOURAUD-2% Glucose-Bouillon (Merck 108339)",
                    "30.0",
                    "G_PER_L",
                    source="DSMZ Medium 1429",
                    notes=(
                        "DSMZ Medium 1429 lists 30.0 g SABOURAUD-2% "
                        "Glucose-Bouillon (Merck 108339)."
                    ),
                ),
                _agar("DSMZ Medium 1429", "15.0"),
                _ingredient(
                    "Distilled water",
                    "1000.0",
                    "ML_PER_L",
                    source="DSMZ Medium 1429",
                    notes="DSMZ Medium 1429 lists 1000.0 ml distilled water.",
                    term=("CHEBI:15377", "water"),
                ),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 30.0 g SABOURAUD-2% Glucose-Bouillon "
                        "(Merck 108339) and 15.0 g agar in 1000.0 ml "
                        "distilled water."
                    ),
                }
            ],
        },
        reference_urls=(DSMZ_1429,),
    ),
    Target(
        path=BREWER_NACL,
        expected_id="CultureMech:015412",
        expected_media_term="mediadive.medium:J667",
        notes=(
            "JCM Medium 667 contains 58.0 g Brewer anaerobic agar (BD-Difco), "
            "20.0 g NaCl, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Brewer anaerobic agar (BD-Difco)",
                    "58.0",
                    "G_PER_L",
                    source="JCM Medium 667",
                    notes="JCM Medium 667 lists 58.0 g Brewer anaerobic agar (BD-Difco).",
                ),
                _ingredient(
                    "NaCl",
                    "20.0",
                    "G_PER_L",
                    source="JCM Medium 667",
                    notes="JCM Medium 667 lists 20.0 g NaCl.",
                    term=("CHEBI:26710", "sodium chloride"),
                ),
                _water("JCM Medium 667"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 58.0 g Brewer anaerobic agar (BD-Difco) "
                        "and 20.0 g NaCl in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_667,),
    ),
    Target(
        path=HALF_MARINE_AGAR,
        expected_id="CultureMech:015425",
        expected_media_term="mediadive.medium:J916",
        notes=(
            "JCM Medium 916 contains 18.7 g Marine broth 2216 (BD-Difco), "
            "15.0 g agar, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "SOLID_AGAR",
            "ingredients": [
                _ingredient(
                    "Marine broth 2216 (BD-Difco)",
                    "18.7",
                    "G_PER_L",
                    source="JCM Medium 916",
                    notes="JCM Medium 916 lists 18.7 g Marine broth 2216 (BD-Difco).",
                ),
                _agar("JCM Medium 916", "15.0"),
                _water("JCM Medium 916"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 18.7 g Marine broth 2216 (BD-Difco) and "
                        "15.0 g agar in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_916,),
    ),
    Target(
        path=HALF_MARINE_NACL,
        expected_id="CultureMech:015420",
        expected_media_term="mediadive.medium:J762",
        notes=(
            "JCM Medium 762 contains 18.7 g Marine broth 2216 (BD-Difco), "
            "10.0 g NaCl, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Marine broth 2216 (BD-Difco)",
                    "18.7",
                    "G_PER_L",
                    source="JCM Medium 762",
                    notes="JCM Medium 762 lists 18.7 g Marine broth 2216 (BD-Difco).",
                ),
                _ingredient(
                    "NaCl",
                    "10.0",
                    "G_PER_L",
                    source="JCM Medium 762",
                    notes="JCM Medium 762 lists 10.0 g NaCl.",
                    term=("CHEBI:26710", "sodium chloride"),
                ),
                _water("JCM Medium 762"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 18.7 g Marine broth 2216 (BD-Difco) and "
                        "10.0 g NaCl in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_762,),
    ),
    Target(
        path=MARINE_CELLOBIOSE,
        expected_id="CultureMech:015385",
        expected_media_term="mediadive.medium:J1127",
        notes=(
            "JCM Medium 1127 contains 37.4 g Marine Broth 2216 (BD-Difco), "
            "1.0 g cellobiose, and 1.0 L distilled water."
        ),
        recipe={
            "medium_type": "COMPLEX",
            "composition_type": "UNDEFINED",
            "physical_state": "LIQUID",
            "ingredients": [
                _ingredient(
                    "Marine Broth 2216 (BD-Difco)",
                    "37.4",
                    "G_PER_L",
                    source="JCM Medium 1127",
                    notes="JCM Medium 1127 lists 37.4 g Marine Broth 2216 (BD-Difco).",
                ),
                _ingredient(
                    "Cellobiose",
                    "1.0",
                    "G_PER_L",
                    source="JCM Medium 1127",
                    notes="JCM Medium 1127 lists 1.0 g cellobiose.",
                    term=("CHEBI:17057", "cellobiose"),
                ),
                _water("JCM Medium 1127"),
            ],
            "preparation_steps": [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": (
                        "Suspend 37.4 g Marine Broth 2216 (BD-Difco) and "
                        "1.0 g cellobiose in 1.0 L distilled water."
                    ),
                },
                {
                    "step_number": 2,
                    "action": "AUTOCLAVE",
                    "description": "Autoclave at 121 C for 15 min unless otherwise stated.",
                },
            ],
            "sterilization": {"method": "AUTOCLAVE"},
        },
        reference_urls=(JCM_1127,),
    ),
)


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


def _components(doc: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        row
        for rows in (doc.get("ingredients") or [], doc.get("solutions") or [])
        for row in rows
        if isinstance(row, dict)
    ]


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    if any(_grounded(component) for component in _components(doc)):
        if "has_ontology_mappings" not in flags:
            flags.append("has_ontology_mappings")

    if any(not _grounded(component) for component in _components(doc)):
        if "has_unmapped_ingredients" not in flags:
            flags.append("has_unmapped_ingredients")
    elif "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    doc["data_quality_flags"] = list(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], reference_urls: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    found = {ref.get("reference") for ref in references if isinstance(ref, dict)}
    for reference in reference_urls:
        if reference not in found:
            references.append({"reference": reference})
            found.add(reference)


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.reference_urls),
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
    if doc.get("id") != target.expected_id:
        raise ValueError(f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = target.notes
    _ensure_flags(repaired)
    _ensure_references(repaired, target.reference_urls)
    _ensure_event(repaired, target)
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
    sys.exit(main())
