#!/usr/bin/env python3
"""Repair NCG, NSSM, Nutrient Agar, and adjacent DSMZ/JCM score-15 records."""

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

CURATOR = "repair_nutrient_ncg_nssm_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2842 = "https://togomedium.org/medium/M2842"
TOGO_M2040 = "https://togomedium.org/medium/M2040"
TOGO_M2341 = "https://togomedium.org/medium/M2341"
TOGO_M1186 = "https://togomedium.org/medium/M1186"
DSMZ_1 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf"
DSMZ_605 = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium605.pdf"
DSMZ_605A = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium605a.pdf"
NBRC_1338 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1338"
JCM_1109 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1109"

Component = tuple[str, str, str]


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


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


@dataclass(frozen=True)
class RecipeRepair:
    path: Path
    record_id: str
    source_term: str
    imported_ingredient_signature: tuple[Component, ...]
    ingredients: tuple[dict[str, Any], ...]
    notes: str
    references: tuple[str, ...]
    action: str
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None
    temperature_value: float | None = None
    imported_solution_signature: tuple[Component, ...] = ()
    solutions: tuple[dict[str, Any], ...] = ()
    preparation_steps: tuple[dict[str, Any], ...] = ()
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    has_unmapped_ingredients: bool = False
    remove_kg_microbe_match: bool = False

    @property
    def final_ingredient_signature(self) -> tuple[Component, ...]:
        return _signature(self.ingredients, "ingredients")

    @property
    def final_solution_signature(self) -> tuple[Component, ...]:
        return _signature(self.solutions, "solutions")


NCG = Path("bacterial/ncg_minimum_medium.yaml")
NSSM = Path("bacterial/nssm_medium.yaml")
SPORULATION = Path("bacterial/nutrient_agar_for_sporulation.yaml")
M2340 = Path("bacterial/TOGO_M2340_Nutrient_Agar.yaml")
DSMZ_605_PATH = Path("bacterial/nutrient_agar_oxoid_cm3.yaml")
DSMZ_605A_PATH = Path("bacterial/nutrient_agar_oxoid_cm3_with_phosphate.yaml")
KOMODO_605A_PATH = Path("bacterial/KOMODO_605a_NUTRIENT_AGAR_OXOID_CM3_WITH_PHOSPHATE.yaml")
M1186 = Path("bacterial/nutrient_agar_with_0_05_yeast_extract_and_3_nacl.yaml")
JCM_J74 = Path("bacterial/JCM_J74_NUTRIENT_AGAR.yaml")

DSMZ_605A_PARENT = {
    "path": f"data/normalized_yaml/{DSMZ_605_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:001732",
    "name": "nutrient_agar_oxoid_cm3",
    "notes": (
        "DSMZ Medium 605a adds KH2PO4 and Na2HPO4 x 12 H2O to DSMZ "
        "Medium 605 and sets the final pH to 6.8."
    ),
}

DSMZ_605A_CHILD = {
    "path": f"data/normalized_yaml/{DSMZ_605A_PATH}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:001733",
    "name": "nutrient_agar_oxoid_cm3_with_phosphate",
    "notes": DSMZ_605A_PARENT["notes"],
}

M2341_PARENT = {
    "path": f"data/normalized_yaml/{M2340}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:008928",
    "name": "nutrient_agar",
    "notes": (
        "TOGO M2341 and TOGO M2340 both represent the DSMZ Medium 1 "
        "Bacillus-sporulation Nutrient Agar formulation with 10 mg/L "
        "MnSO4 x H2O."
    ),
}

M2341_CHILD = {
    "path": f"data/normalized_yaml/{SPORULATION}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:008929",
    "name": "nutrient_agar_for_sporulation",
    "notes": M2341_PARENT["notes"],
}

JCM_1109_PARENT = {
    "path": f"data/normalized_yaml/{JCM_J74}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:003093",
    "name": "nutrient_agar",
    "notes": (
        "JCM Medium 1109 starts from JCM Medium 74 Nutrient Agar and "
        "adds 0.5 g/L Yeast extract plus 30.0 g/L NaCl."
    ),
}

JCM_1109_CHILD = {
    "path": f"data/normalized_yaml/{M1186}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": "CultureMech:007712",
    "name": "nutrient_agar_with_0_05_yeast_extract_and_3_nacl",
    "notes": JCM_1109_PARENT["notes"],
}

DSMZ_605A_MODIFICATION = (
    "Add 0.45 g/L KH2PO4 and 2.39 g/L Na2HPO4 x 12 H2O to DSMZ "
    "Medium 605; final pH is 6.8."
)

M2341_MODIFICATION = (
    "Same ingredient and concentration signature as TOGO M2340 Nutrient Agar."
)

JCM_1109_MODIFICATION = (
    "Add 0.5 g/L Yeast extract (BD-Difco) and 30.0 g/L NaCl to "
    "1.0 L JCM Medium 74 Nutrient Agar."
)

DSMZ_605_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Lab-Lemco beef extract",
        "1.0",
        "G_PER_L",
        source="DSMZ Medium 605",
        notes="DSMZ Medium 605 lists 1.0 g/L Lab-Lemco beef extract.",
        term=("FOODON:03302088", "Beef extract"),
    ),
    _ingredient(
        "Yeast extract",
        "2.0",
        "G_PER_L",
        source="DSMZ Medium 605",
        notes="DSMZ Medium 605 lists 2.0 g/L Yeast extract.",
        term=("FOODON:03315426", "Yeast extract"),
    ),
    _ingredient(
        "Peptone",
        "5.0",
        "G_PER_L",
        source="DSMZ Medium 605",
        notes="DSMZ Medium 605 lists 5.0 g/L Peptone.",
        term=("MICRO:0000178", "Peptone"),
    ),
    _ingredient(
        "NaCl",
        "5.0",
        "G_PER_L",
        source="DSMZ Medium 605",
        notes="DSMZ Medium 605 lists 5.0 g/L NaCl.",
        term=("CHEBI:26710", "sodium chloride"),
    ),
    _ingredient(
        "Agar",
        "15.0",
        "G_PER_L",
        source="DSMZ Medium 605",
        notes="DSMZ Medium 605 lists 15.0 g/L Agar.",
        term=("CHEBI:2509", "agar"),
    ),
    _ingredient(
        "Distilled water",
        "1.0",
        "L",
        source="DSMZ Medium 605",
        notes="DSMZ Medium 605 lists 1000.0 ml Distilled water.",
        term=("CHEBI:15377", "water"),
    ),
)

DSMZ_605A_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "KH2PO4",
        "0.45",
        "G_PER_L",
        source="DSMZ Medium 605a",
        notes="DSMZ Medium 605a adds 0.45 g/L KH2PO4 to DSMZ Medium 605.",
        term=("CHEBI:63036", "potassium dihydrogen phosphate"),
    ),
    _ingredient(
        "Na2HPO4 x 12 H2O",
        "2.39",
        "G_PER_L",
        source="DSMZ Medium 605a",
        notes="DSMZ Medium 605a adds 2.39 g/L Na2HPO4 x 12 H2O to DSMZ Medium 605.",
        term=("CHEBI:91259", "disodium hydrogenphosphate dodecahydrate"),
    ),
    *DSMZ_605_INGREDIENTS,
)

REPAIRS: tuple[RecipeRepair, ...] = (
    RecipeRepair(
        path=NCG,
        record_id="CultureMech:009384",
        source_term="TOGO:M2842",
        imported_ingredient_signature=(
            ("glycerol", "2", "PERCENT_W_V"),
            ("yeast nitrogen base (BD Difco, Franklin Lakes, NJ, USA)", "0.5", "PERCENT_W_V"),
            ("casamino acid (BD Difco)", "0.5", "PERCENT_W_V"),
        ),
        ingredients=(
            _ingredient(
                "glycerol",
                "2.0",
                "PERCENT_W_V",
                source="TOGO M2842",
                notes="TOGO M2842 lists 2% glycerol.",
                term=("CHEBI:17754", "glycerol"),
            ),
            _ingredient(
                "yeast nitrogen base (BD Difco, Franklin Lakes, NJ, USA)",
                "0.5",
                "PERCENT_W_V",
                source="TOGO M2842",
                notes=(
                    "TOGO M2842 lists 0.5% yeast nitrogen base from BD Difco; "
                    "the commercial mixture is retained without an ontology grounding."
                ),
            ),
            _ingredient(
                "casamino acid (BD Difco)",
                "0.5",
                "PERCENT_W_V",
                source="TOGO M2842",
                notes=(
                    "TOGO M2842 lists 0.5% casamino acid from BD Difco; the "
                    "source-specific product is retained without an ontology grounding."
                ),
            ),
        ),
        notes=(
            "TOGO M2842 NCG minimum medium lists 2% glycerol, 0.5% yeast "
            "nitrogen base from BD Difco, and 0.5% casamino acid from BD Difco; "
            "the TOGO comment states that the culture was routinely grown at 30 C."
        ),
        references=(TOGO_M2842,),
        action="RESOLVED_TOGO_M2842_SCORE15",
        temperature_value=30.0,
        has_unmapped_ingredients=True,
        remove_kg_microbe_match=True,
    ),
    RecipeRepair(
        path=NSSM,
        record_id="CultureMech:008630",
        source_term="TOGO:M2040",
        imported_ingredient_signature=(
            ("NaCl", "132", "G_PER_L"),
            ("K2HPO4", "0.6", "G_PER_L"),
            ("Sodium pyruvate", "0.05", "G_PER_L"),
            ("Artificial seawater", "1", "G_PER_L"),
            ("Glucose", "1", "G_PER_L"),
            ("Agar (if needed)", "20", "G_PER_L"),
            ("Bacto Yeast Extract (Difco)", "1", "G_PER_L"),
            ("Casamino acids", "1", "G_PER_L"),
            ("Bacto Proteose Peptone No. 3 (Difco)", "3", "G_PER_L"),
        ),
        ingredients=(
            _ingredient(
                "NaCl",
                "132.0",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes="TOGO M2040 and NBRC Medium 1338 list 132 g/L NaCl.",
                term=("CHEBI:26710", "sodium chloride"),
            ),
            _ingredient(
                "K2HPO4",
                "0.6",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes="TOGO M2040 and NBRC Medium 1338 list 0.6 g/L K2HPO4.",
                term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
            ),
            _ingredient(
                "Sodium pyruvate",
                "0.05",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes="TOGO M2040 and NBRC Medium 1338 list 0.05 g/L Sodium pyruvate.",
                term=("CHEBI:50144", "sodium pyruvate"),
            ),
            _ingredient(
                "Artificial seawater",
                "1.0",
                "L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes=(
                    "TOGO M2040 and NBRC Medium 1338 list 1 L Artificial "
                    "seawater as the solvent matrix."
                ),
            ),
            _ingredient(
                "Glucose",
                "1.0",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes="TOGO M2040 and NBRC Medium 1338 list 1.0 g/L Glucose.",
                term=("CHEBI:17234", "glucose"),
            ),
            _ingredient(
                "Agar",
                "20.0",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes="TOGO M2040 and NBRC Medium 1338 list 20.0 g/L Agar.",
                term=("CHEBI:2509", "agar"),
            ),
            _ingredient(
                "Bacto Yeast Extract (Difco)",
                "1.0",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes=(
                    "TOGO M2040 and NBRC Medium 1338 list 1.0 g/L Bacto "
                    "Yeast Extract from Difco; the commercial product is "
                    "retained without an ontology grounding."
                ),
            ),
            _ingredient(
                "Casamino acids",
                "1.0",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes="TOGO M2040 and NBRC Medium 1338 list 1.0 g/L Casamino acids.",
                term=("FOODON:03315719", "Casamino acids"),
            ),
            _ingredient(
                "Bacto Proteose Peptone No. 3 (Difco)",
                "3.0",
                "G_PER_L",
                source="TOGO M2040 / NBRC Medium 1338",
                notes=(
                    "TOGO M2040 and NBRC Medium 1338 list 3.0 g/L Bacto "
                    "Proteose Peptone No. 3 from Difco."
                ),
                term=("MICRO:0000180", "Proteose Peptone"),
            ),
        ),
        notes=(
            "TOGO M2040 imports NBRC Medium 1338 NSSM medium. The NBRC source "
            "lists 132 g NaCl, 0.6 g K2HPO4, 0.05 g sodium pyruvate, 1 L "
            "artificial seawater, 1 g glucose, 20 g agar, 1 g Bacto Yeast "
            "Extract, 1 g Casamino acids, and 3 g Bacto Proteose Peptone No. 3; "
            "pH is 7.0-7.2."
        ),
        references=(TOGO_M2040, NBRC_1338),
        action="RESOLVED_TOGO_M2040_SCORE15",
        ph_range={"min": 7.0, "max": 7.2},
        preparation_steps=(
            _step(1, "ADJUST_PH", "Adjust pH to 7.0-7.2."),
        ),
        has_unmapped_ingredients=True,
    ),
    RecipeRepair(
        path=SPORULATION,
        record_id="CultureMech:008929",
        source_term="TOGO:M2341",
        imported_ingredient_signature=(
            ("Distilled water", "1000", "G_PER_L"),
            ("MnSO4 x H2O", "10", "G_PER_L"),
            ("Agar, if necessary", "15", "G_PER_L"),
            ("Meat extract", "3", "G_PER_L"),
            ("Peptone", "5", "G_PER_L"),
        ),
        ingredients=(
            _ingredient(
                "Distilled water",
                "1.0",
                "L",
                source="TOGO M2341 / DSMZ Medium 1",
                notes="TOGO M2341 and DSMZ Medium 1 list 1000 ml Distilled water.",
                term=("CHEBI:15377", "water"),
            ),
            _ingredient(
                "MnSO4 x H2O",
                "10.0",
                "MG_PER_L",
                source="TOGO M2341 / DSMZ Medium 1",
                notes=(
                    "TOGO M2341 and DSMZ Medium 1 recommend adding 10 mg/L "
                    "MnSO4 x H2O for sporulation of Bacillus strains."
                ),
                term=("CHEBI:86364", "manganese(II) sulfate monohydrate"),
            ),
            _ingredient(
                "Agar, if necessary",
                "15.0",
                "G_PER_L",
                source="TOGO M2341 / DSMZ Medium 1",
                notes="TOGO M2341 and DSMZ Medium 1 list 15.0 g/L Agar if necessary.",
                term=("CHEBI:2509", "agar"),
            ),
            _ingredient(
                "Meat extract",
                "3.0",
                "G_PER_L",
                source="TOGO M2341 / DSMZ Medium 1",
                notes=(
                    "TOGO M2341 and DSMZ Medium 1 list 3.0 g/L Meat extract; "
                    "this generic complex extract is retained without an "
                    "ontology grounding."
                ),
            ),
            _ingredient(
                "Peptone",
                "5.0",
                "G_PER_L",
                source="TOGO M2341 / DSMZ Medium 1",
                notes="TOGO M2341 and DSMZ Medium 1 list 5.0 g/L Peptone.",
                term=("MICRO:0000178", "Peptone"),
            ),
        ),
        notes=(
            "TOGO M2341 reports the DSMZ Medium 1 sporulation variant for "
            "Bacillus strains: 1000 ml distilled water, 5 g peptone, 3 g Meat "
            "extract, 15 g agar if necessary, and 10 mg MnSO4 x H2O, adjusted "
            "to pH 7.0."
        ),
        references=(TOGO_M2341, DSMZ_1),
        action="RESOLVED_TOGO_M2341_SCORE15",
        ph_value=7.0,
        preparation_steps=(
            _step(1, "ADJUST_PH", "Adjust pH to 7.0."),
        ),
        parent_media=M2341_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(M2341_MODIFICATION,),
        has_unmapped_ingredients=True,
    ),
    RecipeRepair(
        path=DSMZ_605_PATH,
        record_id="CultureMech:001732",
        source_term="mediadive.medium:605",
        imported_ingredient_signature=(
            ("Lab-Lemco beef extract", "1", "G_PER_L"),
            ("Yeast extract", "2", "G_PER_L"),
            ("Peptone", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=DSMZ_605_INGREDIENTS,
        notes=(
            "DSMZ Medium 605 Nutrient Agar (Oxoid CM3) lists 1.0 g "
            "Lab-Lemco beef extract, 2.0 g yeast extract, 5.0 g peptone, "
            "5.0 g NaCl, 15.0 g agar, and 1000.0 ml distilled water."
        ),
        references=(DSMZ_605,),
        action="RESOLVED_DSMZ_605_SCORE15",
        remove_kg_microbe_match=True,
    ),
    RecipeRepair(
        path=DSMZ_605A_PATH,
        record_id="CultureMech:001733",
        source_term="mediadive.medium:605a",
        imported_ingredient_signature=(
            ("KH2PO4", "0.45", "G_PER_L"),
            ("Na2HPO4 x 12 H2O", "2.39", "G_PER_L"),
            ("Lab-Lemco beef extract", "1", "G_PER_L"),
            ("Yeast extract", "2", "G_PER_L"),
            ("Peptone", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=DSMZ_605A_INGREDIENTS,
        notes=(
            "DSMZ Medium 605a supplements DSMZ Medium 605 with 0.45 g/L KH2PO4 "
            "and 2.39 g/L Na2HPO4 x 12 H2O; the final pH is 6.8."
        ),
        references=(DSMZ_605A, DSMZ_605),
        action="RESOLVED_DSMZ_605A_SCORE15",
        ph_value=6.8,
        preparation_steps=(
            _step(1, "MIX", DSMZ_605A_MODIFICATION),
        ),
        parent_media=DSMZ_605A_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=(DSMZ_605A_MODIFICATION,),
    ),
    RecipeRepair(
        path=KOMODO_605A_PATH,
        record_id="CultureMech:006094",
        source_term="komodo.medium:605a",
        imported_ingredient_signature=(
            ("KH2PO4", "0.45", "G_PER_L"),
            ("Na2HPO4 x 12 H2O", "2.39", "G_PER_L"),
            ("Lab-Lemco beef extract", "1", "G_PER_L"),
            ("Yeast extract", "2", "G_PER_L"),
            ("Peptone", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=DSMZ_605A_INGREDIENTS,
        notes=(
            "KOMODO Medium 605a is a DSMZ Medium 605a source duplicate. "
            "DSMZ Medium 605a supplements DSMZ Medium 605 with 0.45 g/L "
            "KH2PO4 and 2.39 g/L Na2HPO4 x 12 H2O; the final pH is 6.8."
        ),
        references=(DSMZ_605A, DSMZ_605),
        action="RESOLVED_KOMODO_605A_SOURCE_DUPLICATE",
        ph_value=6.8,
        preparation_steps=(
            _step(1, "MIX", DSMZ_605A_MODIFICATION),
        ),
        parent_media={
            "path": f"data/normalized_yaml/{DSMZ_605A_PATH}",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:001733",
            "name": "nutrient_agar_oxoid_cm3_with_phosphate",
            "notes": (
                "KOMODO Medium 605a states DSMZ Medium 605a provenance and "
                "matches the curated DSMZ phosphate formulation."
            ),
        },
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(
            "Same ingredient and concentration signature as DSMZ Medium 605a.",
        ),
    ),
    RecipeRepair(
        path=M1186,
        record_id="CultureMech:007712",
        source_term="TOGO:M1186",
        imported_ingredient_signature=(
            ("NaCl", "30", "G_PER_L"),
            ("Yeast extract (BD--Difco)", "0.5", "G_PER_L"),
        ),
        imported_solution_signature=(
            ("Nutrient agar (see Medium [M65])", "1", "G_PER_L"),
        ),
        ingredients=(
            _ingredient(
                "NaCl",
                "30.0",
                "G_PER_L",
                source="TOGO M1186 / JCM Medium 1109",
                notes="TOGO M1186 and JCM Medium 1109 list 30.0 g/L NaCl.",
                term=("CHEBI:26710", "sodium chloride"),
            ),
            _ingredient(
                "Yeast extract (BD-Difco)",
                "0.5",
                "G_PER_L",
                source="TOGO M1186 / JCM Medium 1109",
                notes="TOGO M1186 and JCM Medium 1109 list 0.5 g/L Yeast extract from BD-Difco.",
                term=("FOODON:03315426", "Yeast extract"),
            ),
        ),
        solutions=(
            {
                "preferred_term": "Nutrient agar (JCM Medium 74)",
                "concentration": {"value": "1.0", "unit": "L"},
                "source": "TOGO M1186 / JCM Medium 1109",
                "notes": (
                    "TOGO M1186 and JCM Medium 1109 list 1.0 L Nutrient agar "
                    "from JCM Medium 74."
                ),
                "composition": [],
            },
        ),
        notes=(
            "TOGO M1186 imports JCM Medium 1109, which adds 0.5 g Yeast "
            "extract from BD-Difco and 30 g NaCl to 1 L Nutrient agar from "
            "JCM Medium 74."
        ),
        references=(TOGO_M1186, JCM_1109),
        action="RESOLVED_TOGO_M1186_SCORE15",
        parent_media=JCM_1109_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=(JCM_1109_MODIFICATION,),
        has_unmapped_ingredients=True,
        remove_kg_microbe_match=True,
    ),
)

REPAIRS_BY_PATH = {repair.path: repair for repair in REPAIRS}


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(repair: RecipeRepair, doc: dict[str, Any]) -> None:
    if doc.get("id") != repair.record_id:
        raise ValueError(
            f"{repair.path}: expected id {repair.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != repair.source_term:
        raise ValueError(f"{repair.path}: expected media term {repair.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        repair.imported_ingredient_signature,
        repair.final_ingredient_signature,
    ):
        raise ValueError(
            f"{repair.path}: ingredient signature drifted from "
            f"{repair.imported_ingredient_signature!r} to {ingredient_signature!r}"
        )

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in (
        repair.imported_solution_signature,
        repair.final_solution_signature,
    ):
        raise ValueError(
            f"{repair.path}: solution signature drifted from "
            f"{repair.imported_solution_signature!r} to {solution_signature!r}"
        )


def _ensure_parent(doc: dict[str, Any], path: Path, record_id: str, media_term: str) -> None:
    if doc.get("id") != record_id:
        raise ValueError(f"{path}: expected id {record_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != media_term:
        raise ValueError(f"{path}: expected media term {media_term}")


def _ensure_flags(doc: dict[str, Any], *, has_unmapped_ingredients: bool) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)

    if not has_unmapped_ingredients and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)
    if has_unmapped_ingredients and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for url in references:
        if url not in existing:
            rows.append({"reference": url})


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(source),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_variant_child(doc: dict[str, Any], child: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    for index, existing in enumerate(children):
        if not isinstance(existing, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if existing.get("id") == child["id"] or existing.get("path") == child["path"]:
            children[index] = copy.deepcopy(child)
            return
    children.append(copy.deepcopy(child))


def repair_target(repair: RecipeRepair, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(repair, doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    _put_after(repaired, "ingredients", copy.deepcopy(list(repair.ingredients)), "notes")
    if repair.solutions:
        repaired["solutions"] = copy.deepcopy(list(repair.solutions))
    else:
        repaired.pop("solutions", None)

    if repair.ph_value is not None:
        _put_after(repaired, "ph_value", repair.ph_value, "physical_state")
        repaired.pop("ph_range", None)
    elif repair.ph_range is not None:
        _put_after(repaired, "ph_range", copy.deepcopy(repair.ph_range), "physical_state")
        repaired.pop("ph_value", None)
    else:
        repaired.pop("ph_value", None)
        repaired.pop("ph_range", None)

    if repair.temperature_value is not None:
        _put_after(repaired, "temperature_value", repair.temperature_value, "physical_state")
        repaired.pop("temperature_range", None)
    else:
        repaired.pop("temperature_value", None)
        repaired.pop("temperature_range", None)

    if repair.preparation_steps:
        repaired["preparation_steps"] = copy.deepcopy(list(repair.preparation_steps))
    else:
        repaired.pop("preparation_steps", None)

    _put_after(repaired, "notes", repair.notes, "media_term")
    if repair.remove_kg_microbe_match:
        repaired.pop("kg_microbe_match", None)

    if repair.parent_media is not None:
        repaired["parent_media"] = copy.deepcopy(repair.parent_media)
        repaired["variant_relationship"] = repair.variant_relationship
        repaired["variant_modifications"] = list(repair.variant_modifications)

    _ensure_flags(
        repaired,
        has_unmapped_ingredients=repair.has_unmapped_ingredients,
    )
    _ensure_references(repaired, repair.references)
    _append_curation_event(
        repaired,
        action=repair.action,
        source=repair.references,
        notes=repair.notes,
    )
    return repaired


def repair_dsmz_605_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(
        doc,
        DSMZ_605_PATH,
        "CultureMech:001732",
        "mediadive.medium:605",
    )

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired, DSMZ_605A_CHILD)
    _append_curation_event(
        repaired,
        action="LINKED_DSMZ_605A_PHOSPHATE_VARIANT",
        source=(DSMZ_605, DSMZ_605A),
        notes="Linked DSMZ Medium 605a as the phosphate-supplemented variant of DSMZ Medium 605.",
    )
    return repaired


def repair_togo_m2340_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(
        doc,
        M2340,
        "CultureMech:008928",
        "TOGO:M2340",
    )

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired, M2341_CHILD)
    _append_curation_event(
        repaired,
        action="LINKED_TOGO_M2341_SOURCE_DUPLICATE",
        source=(TOGO_M2341, DSMZ_1),
        notes=(
            "Linked TOGO M2341 as a source duplicate of the TOGO M2340 "
            "Bacillus-sporulation Nutrient Agar formulation."
        ),
    )
    return repaired


def repair_jcm_j74_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(
        doc,
        JCM_J74,
        "CultureMech:003093",
        "mediadive.medium:J74",
    )

    repaired = copy.deepcopy(doc)
    _ensure_variant_child(repaired, JCM_1109_CHILD)
    _append_curation_event(
        repaired,
        action="LINKED_JCM_1109_SUPPLEMENTED_VARIANT",
        source=(TOGO_M1186, JCM_1109),
        notes=(
            "Linked JCM Medium 1109 / TOGO M1186 as the NaCl and yeast-extract "
            "supplemented variant of JCM Medium 74 Nutrient Agar."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for repair in REPAIRS:
        path = normalized / repair.path
        plans[path] = repair_target(repair, _load(path))

    dsmz_605_path = normalized / DSMZ_605_PATH
    plans[dsmz_605_path] = repair_dsmz_605_parent(plans[dsmz_605_path])

    m2340_path = normalized / M2340
    plans[m2340_path] = repair_togo_m2340_parent(_load(m2340_path))

    jcm_j74_path = normalized / JCM_J74
    plans[jcm_j74_path] = repair_jcm_j74_parent(_load(jcm_j74_path))
    return plans


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
