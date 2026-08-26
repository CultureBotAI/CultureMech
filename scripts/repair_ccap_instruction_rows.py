#!/usr/bin/env python3
"""Repair CCAP preparation text that was flattened into ingredient rows.

The April 2026 CCAP expansion treated every number near a PDF table as an
ingredient concentration. This produced three related failures:

* final preparation instructions became ingredient names;
* text from nested stock or constituent-medium recipes leaked into the parent;
* a few real components following an instruction were swallowed by that text.

Every target below is grounded in the CCAP PDF cited by its record. The migration
is dry-run by default, checks the exact pre-repair row signatures, and records one
curation event per changed record. It deliberately does not attempt the separate
stock-strength concentration migration for otherwise valid CCAP reagent rows.
"""

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
from record_io import write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
ACTION = "REPAIRED_CCAP_INSTRUCTION_ROWS"
TIMESTAMP = "2026-08-25T00:00:00-07:00"


@dataclass(frozen=True)
class RowSignature:
    name: str
    value: str
    unit: str


@dataclass(frozen=True)
class IngredientSpec:
    name: str
    value: str
    unit: str
    notes: str
    term_id: str | None = None
    term_label: str | None = None
    mim_link: bool = False


@dataclass(frozen=True)
class SolutionSpec:
    name: str
    value: str
    unit: str
    culturemech_id: str
    culturemech_label: str
    notes: str


@dataclass(frozen=True)
class StepSpec:
    action: str
    description: str


@dataclass(frozen=True)
class SimpleTarget:
    path: str
    record_id: str
    source: str
    rows: tuple[RowSignature, ...]
    replacements: tuple[IngredientSpec, ...] = ()
    add_solutions: tuple[SolutionSpec, ...] = ()
    steps: tuple[StepSpec, ...] = ()
    field_updates: tuple[tuple[str, str], ...] = ()
    add_variants: tuple[dict[str, Any], ...] = ()


@dataclass(frozen=True)
class RebuildTarget:
    path: str
    record_id: str
    source: str
    current_rows: tuple[RowSignature, ...]
    ingredients: tuple[IngredientSpec, ...]
    solutions: tuple[SolutionSpec, ...]
    steps: tuple[StepSpec, ...]
    add_variants: tuple[dict[str, Any], ...] = ()


def row(name: str, value: str, unit: str) -> RowSignature:
    return RowSignature(name, value, unit)


def step(action: str, description: str) -> StepSpec:
    return StepSpec(action, description)


AUTOCLAVE = step("AUTOCLAVE", "Autoclave at 15 psi for 15 minutes.")


def make_up(solvent: str, volume: str = "1 L") -> StepSpec:
    return step("MIX", f"Bring to {volume} with {solvent}.")


def adjust_ph(target: str, reagent: str = "1 M NaOH or 1 M HCl") -> StepSpec:
    return step("ADJUST_PH", f"Adjust pH to {target} with {reagent} before autoclaving.")


def add_agar(value: str = "15") -> StepSpec:
    return step(
        "ADD_AGAR",
        f"For an agar formulation, add {value} g/L Bacteriological Agar.",
    )


NA2_EDTA = IngredientSpec(
    "Na2EDTA",
    "0.75",
    "G_PER_L",
    "Na2EDTA in the source-defined trace-element stock; this is a stock composition, not a final-medium concentration.",
    "CHEBI:64734",
    "EDTA disodium salt (anhydrous)",
    True,
)


SIMPLE_TARGETS = (
    SimpleTarget(
        "algae/3n_bbm_v.yaml",
        "CultureMech:000039",
        "MR_3N_BBM_V.pdf",
        (row("Make up to 1 litre with deionised water. For agar, add", "15", "G_PER_L"),),
        steps=(make_up("deionised water"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/CCAP_ASW 150 + barley  + barley grain_).yaml",
        "CultureMech:000045",
        "MR_ASW_150.pdf",
        (row("Make up to 1 litre with deionised water. Adjust pH to 7-8 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("7-8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/CCAP_ASW 300 + barley  + barley grain_).yaml",
        "CultureMech:000049",
        "MR_ASW_300.pdf",
        (row("Make up to 1 litre with deionised water. Adjust pH to 7.6-8 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("7.6-8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/CCAP_C Medium_ Modified.yaml",
        "CultureMech:000057",
        "MR_C_Modified.pdf",
        (row("Add to 1000 ml of distilled water", "0.75", "G_PER_L"),),
        replacements=(NA2_EDTA,),
        steps=(
            step(
                "DISSOLVE",
                "Dissolve Tris in 900 mL distilled water, then add the remaining final-medium components.",
            ),
            make_up("distilled water"),
            add_agar(),
            step("ADJUST_PH", "Ensure the final pH is 7.5."),
            AUTOCLAVE,
        ),
    ),
    SimpleTarget(
        "algae/CCAP_TAP Medium.yaml",
        "CultureMech:000139",
        "MR_TAP.pdf",
        (row("Make up to 1 litre with deionised water. For agar, add", "15", "G_PER_L"),),
        steps=(make_up("deionised water"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/asw.yaml",
        "CultureMech:000050",
        "MR_ASW.pdf",
        (row("Make up to", "1", "L"),),
        steps=(make_up("filtered natural seawater"), adjust_ph("7.6-7.8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/asw_150_barley.yaml",
        "CultureMech:000044",
        "MR_ASW_150.pdf",
        (row("Make up to 1 litre with deionised water. Adjust pH to 7-8 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("7-8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/asw_300_barley.yaml",
        "CultureMech:000048",
        "MR_ASW_300.pdf",
        (row("Make up to 1 litre with deionised water. Adjust pH to 7.6-8 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("7.6-8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/asw_barley.yaml",
        "CultureMech:000043",
        "MR_ASW_Barley.pdf",
        (row("HCl. Add", "1", "G_PER_L"),),
        replacements=(
            IngredientSpec(
                "Barley grain",
                "variable",
                "VARIABLE",
                "Source amount: one barley grain per 25 mL prepared medium; the schema has no count-per-volume unit.",
            ),
        ),
        steps=(
            make_up("filtered natural seawater"),
            adjust_ph("7.6-7.8"),
            step("MIX", "Add one barley grain to each 25 mL of prepared medium."),
            AUTOCLAVE,
        ),
    ),
    SimpleTarget(
        "algae/aswp.yaml",
        "CultureMech:000051",
        "MR_ASWP.pdf",
        (
            row(
                "Make up to 1 litre with deionised water and adjust pH to 7.6 - 7.8 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(make_up("deionised water"), adjust_ph("7.6-7.8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/bg.yaml",
        "CultureMech:000055",
        "MR_BG11.pdf",
        (
            row("Make up to 1 litre with deionised water. Adjust pH to 7.1 with", "1", "MOLAR"),
            row("For agar, add", "15.0", "G_PER_L"),
        ),
        steps=(
            make_up("deionised water"),
            adjust_ph("7.1", "1 M NaOH or HCl"),
            add_agar("15.0"),
            AUTOCLAVE,
        ),
    ),
    SimpleTarget(
        "algae/c_medium_modified.yaml",
        "CultureMech:000056",
        "MR_C_Modified.pdf",
        (row("Add to 1000 ml of distilled water", "0.75", "G_PER_L"),),
        replacements=(NA2_EDTA,),
        steps=(
            step(
                "DISSOLVE",
                "Dissolve Tris in 900 mL distilled water, then add the remaining final-medium components.",
            ),
            make_up("distilled water"),
            add_agar(),
            step("ADJUST_PH", "Ensure the final pH is 7.5."),
            AUTOCLAVE,
        ),
    ),
    SimpleTarget(
        "algae/cgm.yaml",
        "CultureMech:000058",
        "MR_CGM.pdf",
        (row("Make up to 1 litre with deionised water. For agar, add", "15", "G_PER_L"),),
        steps=(make_up("deionised water"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/dm.yaml",
        "CultureMech:000063",
        "MR_DM.pdf",
        (row("Make up to 1 litre with deionised water. Adjust to pH 6.9 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("6.9"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/eg.yaml",
        "CultureMech:000070",
        "MR_EG.pdf",
        (
            row(
                "Add the above constituents and make up to 1 litre with deionised water. For agar, add",
                "15",
                "G_PER_L",
            ),
        ),
        steps=(make_up("deionised water"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/f_2.yaml",
        "CultureMech:000149",
        "MR_f2.pdf",
        (
            row(
                "Make up to 1 litre with filtered natural seawater. Adjust pH to 8.0 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(make_up("filtered natural seawater"), adjust_ph("8.0"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/f_2_si.yaml",
        "CultureMech:000148",
        "MR_f2Si.pdf",
        (
            row(
                "Make up to 1 litre with filtered natural seawater. Adjust pH to 8.0 with",
                "1",
                "MOLAR",
            ),
            row("To make this medium, omit stock 5 and instead add", "0.1705", "G_PER_L"),
        ),
        steps=(make_up("filtered natural seawater"), adjust_ph("8.0"), add_agar(), AUTOCLAVE),
        add_variants=(
            {
                "name": "f_2_si_modified",
                "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
                "description": "CCAP's higher-silicate modified formulation.",
                "modifications": [
                    "Omit stock 5 and add 0.1705 g/L sodium metasilicate nonahydrate directly."
                ],
            },
        ),
    ),
    SimpleTarget(
        "algae/f_2_si_for_heterotrophic_growth.yaml",
        "CultureMech:000147",
        "MR_f2Si_heterotrophic.pdf",
        (
            row(
                "Make up to 1 litre with filtered natural seawater. Adjust pH to 8.0 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(
            make_up("filtered natural seawater"),
            adjust_ph("8.0", "1 M NaOH or HCl"),
            AUTOCLAVE,
        ),
    ),
    SimpleTarget(
        "algae/fdmed.yaml",
        "CultureMech:000072",
        "MR_FDMed.pdf",
        (row("Make up to 1 litre with deionised water. Adjust pH to 7.5 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("7.5"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/jm.yaml",
        "CultureMech:000074",
        "MR_JM.pdf",
        (row("Make up to 1 litre with deionised water. For agar, add", "15.0", "G_PER_L"),),
        steps=(make_up("deionised water"), add_agar("15.0"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/k35.yaml",
        "CultureMech:000078",
        "MR_K35.pdf",
        (
            row(
                "Make up to 1 litre with deionised water. Adjust pH to 8.1 - 8.4 with", "1", "MOLAR"
            ),
        ),
        steps=(make_up("deionised water"), adjust_ph("8.1-8.4"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/k_medium.yaml",
        "CultureMech:000076",
        "MR_K.pdf",
        (
            row(
                "Make up to 1 litre with filtered natural seawater. Adjust pH to 8.0 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(make_up("filtered natural seawater"), adjust_ph("8.0"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/k_minimum.yaml",
        "CultureMech:000077",
        "MR_Kmin.pdf",
        (
            row(
                "Make up to 1 litre with filtered natural seawater. Adjust pH to 8.0 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(make_up("filtered natural seawater"), adjust_ph("8.0"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/l1.yaml",
        "CultureMech:000079",
        "MR_L1.pdf",
        (
            row(
                "Make up to 1 litre with filtered natural seawater. Adjust pH to 8.0 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(make_up("filtered natural seawater"), adjust_ph("8.0"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/maf6_se.yaml",
        "CultureMech:000081",
        "MR_MAF6_SE.pdf",
        (
            row("Add to 1000 ml of distilled water", "0.75", "G_PER_L"),
            row("Soil is prepared as above.", "105", "G_PER_L"),
        ),
        replacements=(NA2_EDTA,),
        add_solutions=(
            SolutionSpec(
                "SE2 (Soil Extract 2)",
                "30",
                "ML_PER_L",
                "CultureMech:000129",
                "SE2",
                "Source-asserted addition of constituent soil extract.",
            ),
        ),
        steps=(make_up("distilled water"), step("ADJUST_PH", "Adjust pH to 6.6."), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/masm.yaml",
        "CultureMech:000082",
        "MR_MASM.pdf",
        (row("Make up to 1 litre with deionised water and adjust to pH 8.0 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("8.0"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/mdy_v.yaml",
        "CultureMech:000088",
        "MR_MDY_V.pdf",
        (row("Add to 1000 ml of distilled water", "0.75", "G_PER_L"),),
        replacements=(NA2_EDTA,),
        steps=(
            make_up("distilled water"),
            step("ADJUST_PH", "Adjust pH to 6.8 with NaOH."),
            add_agar(),
            AUTOCLAVE,
        ),
    ),
    SimpleTarget(
        "algae/met_44.yaml",
        "CultureMech:000096",
        "MR_MET44.pdf",
        (row("Make up to 1 litre with filtered natural seawater. For agar, add", "15", "G_PER_L"),),
        steps=(make_up("filtered natural seawater"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/mhy.yaml",
        "CultureMech:000091",
        "MR_MHY.pdf",
        (row("Make up to 1 litre with deionised water. Adjust pH to 6.8 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("6.8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/mp.yaml",
        "CultureMech:000092",
        "MR_MP_Modified_Provasoli.pdf",
        (row("For agar, add", "15", "G_PER_L"),),
        steps=(add_agar(),),
    ),
    SimpleTarget(
        "algae/my75s.yaml",
        "CultureMech:000095",
        "MR_MY75S.pdf",
        (row("Make up the", "75", "PERCENT_W_V"),),
        replacements=(
            IngredientSpec(
                "Filtered natural seawater",
                "750",
                "ML_PER_L",
                "Source-asserted liquid volume in the final medium.",
            ),
            IngredientSpec(
                "Deionised water",
                "250",
                "ML_PER_L",
                "Source-asserted liquid volume in the final medium.",
                "CHEBI:15377",
                "water",
                True,
            ),
        ),
        steps=(
            step("HEAT", "Combine the seawater and deionised water and heat without boiling."),
            step("DISSOLVE", "Dissolve the malt extract and yeast extract."),
            step("ADD_AGAR", "Cool slightly, add 15 g/L Bacteriological Agar, and disperse."),
            AUTOCLAVE,
        ),
        field_updates=(("physical_state", "SOLID_AGAR"),),
    ),
    SimpleTarget(
        "algae/pp.yaml",
        "CultureMech:000115",
        "MR_PP.pdf",
        (row("Make up to 1 litre with deionised water. For agar, add", "15", "G_PER_L"),),
        steps=(make_up("deionised water"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/ucm.yaml",
        "CultureMech:000140",
        "MR_UCM.pdf",
        (row("Make up to 978 ml with deionised water and adjust pH to 8.1 with", "1", "MOLAR"),),
        steps=(make_up("deionised water", "978 mL"), adjust_ph("8.1"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/um.yaml",
        "CultureMech:000141",
        "MR_UM.pdf",
        (
            row(
                "Make up to 1 litre with deionised water and adjust pH to 7.6 - 7.8 with",
                "1",
                "MOLAR",
            ),
        ),
        steps=(make_up("deionised water"), adjust_ph("7.6-7.8"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/waris_h.yaml",
        "CultureMech:000143",
        "MR_Waris_H.pdf",
        (row("Make up to 1 litre with deionised water and adjust pH to 7.0 with", "1", "MOLAR"),),
        steps=(make_up("deionised water"), adjust_ph("7.0"), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/wmy.yaml",
        "CultureMech:000150",
        "MR_wMY.pdf",
        (
            row(
                "Add the above constituents and make up to 1 litre with deionised water. For agar, add",
                "15",
                "G_PER_L",
            ),
        ),
        steps=(make_up("deionised water"), add_agar(), AUTOCLAVE),
    ),
    SimpleTarget(
        "algae/zm_10.yaml",
        "CultureMech:000146",
        "MR_ZM10.pdf",
        (row("Make up to 1 litre with", "75", "PERCENT_W_V"),),
        replacements=(
            IngredientSpec(
                "Filtered natural seawater",
                "750",
                "ML_PER_L",
                "Source-asserted 75% volume fraction in the final medium.",
            ),
            IngredientSpec(
                "Deionised water",
                "250",
                "ML_PER_L",
                "Source-asserted 25% volume fraction in the final medium.",
                "CHEBI:15377",
                "water",
                True,
            ),
        ),
        steps=(
            step("MIX", "Bring to 1 L with 75% filtered natural seawater and 25% deionised water."),
            AUTOCLAVE,
            step(
                "COOL",
                "Cool to approximately 55 deg C before adding sterile marine supplement stock.",
            ),
        ),
        field_updates=(("physical_state", "SOLID_AGAR"),),
    ),
)


REBUILD_TARGETS = (
    RebuildTarget(
        "algae/ajs.yaml",
        "CultureMech:000041",
        "MR_AJS.pdf",
        (
            row("EDTANa", "0.45", "G_PER_L"),
            row("MnCl2 x 4 H2O", "0.278", "G_PER_L"),
            row("Thiamine HCl", "0.008", "G_PER_L"),
            row("Biotin", "0.008", "G_PER_L"),
            row("Make up to 1 litre with deionized water. For agar, add", "15.0", "G_PER_L"),
            row("Soil is prepared as above.", "105", "G_PER_L"),
        ),
        ingredients=(
            IngredientSpec(
                "Concentrated H2SO4",
                "10",
                "ML_PER_L",
                "Source-asserted addition to approximately 1 L final medium.",
                "CHEBI:26836",
                "sulfuric acid",
                True,
            ),
        ),
        solutions=(
            SolutionSpec(
                "JM (Jaworski's Medium)",
                "970",
                "ML_PER_L",
                "CultureMech:000074",
                "JM",
                "97% constituent medium.",
            ),
            SolutionSpec(
                "SE2 (Soil Extract 2)",
                "30",
                "ML_PER_L",
                "CultureMech:000129",
                "SE2",
                "3% constituent medium.",
            ),
        ),
        steps=(
            step("MIX", "Mix 970 mL JM with 30 mL SE2 per approximately 1 L final medium."),
            step("ADJUST_PH", "Add 10 mL concentrated H2SO4 to obtain approximately pH 1.5."),
            AUTOCLAVE,
        ),
    ),
    RebuildTarget(
        "algae/bb_merds.yaml",
        "CultureMech:000054",
        "MR_BB_MErds.pdf",
        (
            row("ZnSO4 x 7 H2O", "8.82", "G_PER_L"),
            row("MnCl2 x 4 H2O", "1.44", "G_PER_L"),
            row("MoO", "0.71", "G_PER_L"),
            row("CuSO4 x 5 H2O", "1.57", "G_PER_L"),
            row("Co(NO3)2.6H2O", "0.49", "G_PER_L"),
            row("KOH", "31.0", "G_PER_L"),
            row("Na2HPO4", "1.2", "G_PER_L"),
            row("Soil is prepared as above.", "105", "G_PER_L"),
        ),
        ingredients=(),
        solutions=(
            SolutionSpec(
                "BB (Bold's Basal Medium)",
                "variable",
                "VARIABLE",
                "CultureMech:000053",
                "BB",
                "Use 800 mL/L in the 8:2 variant or 500 mL/L in the 1:1 variant.",
            ),
            SolutionSpec(
                "MErds (Modified Foyns Erdschreiber Medium)",
                "variable",
                "VARIABLE",
                "CultureMech:000089",
                "MErds",
                "Use 200 mL/L in the 8:2 variant or 500 mL/L in the 1:1 variant.",
            ),
        ),
        steps=(
            step("MIX", "Mix the two constituent media, then autoclave at 15 psi for 15 minutes."),
        ),
        add_variants=(
            {
                "name": "bb_merds_8_2",
                "relationship": "CONCENTRATION_VARIANT",
                "modifications": ["Mix 800 mL BB with 200 mL MErds per litre."],
            },
            {
                "name": "bb_merds_1_1",
                "relationship": "CONCENTRATION_VARIANT",
                "modifications": ["Mix 500 mL BB with 500 mL MErds per litre."],
            },
        ),
    ),
    RebuildTarget(
        "algae/eg_jm.yaml",
        "CultureMech:000071",
        "MR_EG_JM.pdf",
        (
            row("Sodium acetate trihydrate", "1.0", "G_PER_L"),
            row("Lab-Lemco powder", "1.0", "G_PER_L"),
            row("Tryptone", "2.0", "G_PER_L"),
            row("Yeast extract", "2.0", "G_PER_L"),
            row(
                "Add the above constituents and make up to 1 litre with deionised water. For agar, add",
                "15",
                "G_PER_L",
            ),
            row("Na EDTA", "0.45", "G_PER_L"),
            row("MnCl2 x 4 H2O", "0.278", "G_PER_L"),
            row("Thiamine HCl", "0.008", "G_PER_L"),
            row("Biotin", "0.008", "G_PER_L"),
            row("Make up to 1 litre with deionised water. For agar, add", "15.0", "G_PER_L"),
        ),
        ingredients=(),
        solutions=(
            SolutionSpec(
                "EG (Euglena gracilis Medium)",
                "500",
                "ML_PER_L",
                "CultureMech:000070",
                "EG",
                "One half of the final 1:1 mixture.",
            ),
            SolutionSpec(
                "JM (Jaworski's Medium)",
                "500",
                "ML_PER_L",
                "CultureMech:000074",
                "JM",
                "One half of the final 1:1 mixture.",
            ),
        ),
        steps=(step("MIX", "Mix EG and JM in a 1:1 ratio."), AUTOCLAVE),
    ),
    RebuildTarget(
        "algae/mbbm.yaml",
        "CultureMech:000083",
        "MR_MBBM.pdf",
        (
            row("Make up to 1 litre with distilled water. For agar add", "15", "G_PER_L"),
            row("Add to 1000 ml of distilled water", "0.75", "G_PER_L"),
            row("FeCl3 x 6 H2O", "0.097", "G_PER_L"),
            row("MnCl2 x 4 H2O", "0.041", "G_PER_L"),
            row("ZnCl2", "0.005", "G_PER_L"),
            row("CoCl2 x 6 H2O", "0.002", "G_PER_L"),
            row("Na2MoO4 x 2 H2O", "0.004", "G_PER_L"),
        ),
        ingredients=(
            IngredientSpec(
                "Bacto peptone",
                "1",
                "G_PER_L",
                "Direct final-medium ingredient.",
                "MICRO:0000178",
                "peptone",
            ),
            IngredientSpec(
                "Sucrose",
                "5",
                "G_PER_L",
                "Direct final-medium ingredient.",
                "CHEBI:17992",
                "sucrose",
                True,
            ),
        ),
        solutions=(
            SolutionSpec(
                "3N-BBM+V",
                "1000",
                "ML_PER_L",
                "CultureMech:000039",
                "3N-BBM+V",
                "Source-defined base medium to which peptone and sucrose are added.",
            ),
        ),
        steps=(step("MIX", "Add 1 g Bacto peptone and 5 g sucrose to 1 L 3N-BBM+V."),),
    ),
    RebuildTarget(
        "algae/per.yaml",
        "CultureMech:000111",
        "MR_PER.pdf",
        (row("Soil is prepared as above.", "105", "G_PER_L"),),
        ingredients=(
            IngredientSpec(
                "Complan", "1", "G_PER_L", "Source-asserted commercial nutrient powder."
            ),
        ),
        solutions=(
            SolutionSpec(
                "SES (Soil Extract with Added Salts)",
                "1000",
                "ML_PER_L",
                "CultureMech:000130",
                "SES",
                "Source-defined base medium.",
            ),
        ),
        steps=(step("MIX", "Add 1 g Complan to 1 L SES."), AUTOCLAVE),
    ),
    RebuildTarget(
        "algae/sbbm.yaml",
        "CultureMech:000127",
        "MR_SBBM.pdf",
        (
            row("Make up to 1 litre with distilled water. For agar add", "15", "G_PER_L"),
            row("Add to 1000 ml of distilled water", "0.75", "G_PER_L"),
            row("FeCl3 x 6 H2O", "0.097", "G_PER_L"),
            row("MnCl2 x 4 H2O", "0.041", "G_PER_L"),
            row("ZnCl .6H O", "0.005", "G_PER_L"),
            row("CoCl2 x 6 H2O", "0.002", "G_PER_L"),
            row("Na2MoO4 x 2 H2O", "0.004", "G_PER_L"),
            row("Soil is prepared as above.", "105", "G_PER_L"),
        ),
        ingredients=(),
        solutions=(
            SolutionSpec(
                "3N-BBM+V",
                "970",
                "ML_PER_L",
                "CultureMech:000039",
                "3N-BBM+V",
                "97% constituent medium.",
            ),
            SolutionSpec(
                "SE2 (Soil Extract 2)",
                "30",
                "ML_PER_L",
                "CultureMech:000129",
                "SE2",
                "3% constituent medium.",
            ),
        ),
        steps=(
            step(
                "MIX", "Prepare and sterilize both constituent media, then mix aseptically at 97:3."
            ),
        ),
    ),
    RebuildTarget(
        "algae/ses_mp.yaml",
        "CultureMech:000132",
        "MR_SES_MP.pdf",
        (row("Soil is prepared as above.", "105", "G_PER_L"),),
        ingredients=(),
        solutions=(
            SolutionSpec(
                "SES (Soil Extract with Added Salts)",
                "750",
                "ML_PER_L",
                "CultureMech:000130",
                "SES",
                "Three quarters of the final 3:1 mixture.",
            ),
            SolutionSpec(
                "Chapman-Andresen's Modified Pringsheim's Solution",
                "250",
                "ML_PER_L",
                "CultureMech:000062",
                "Modified Pringsheim's Solution",
                "One quarter of the final 3:1 mixture.",
            ),
        ),
        steps=(
            step("MIX", "Autoclave the constituent media separately, then mix aseptically at 3:1."),
        ),
    ),
    RebuildTarget(
        "algae/ses_pj.yaml",
        "CultureMech:000131",
        "MR_SES_PJ.pdf",
        (
            row("KCl", "0.16", "G_PER_L"),
            row("Soil is prepared as above.", "105", "G_PER_L"),
        ),
        ingredients=(),
        solutions=(
            SolutionSpec(
                "SES (Soil Extract with Added Salts)",
                "500",
                "ML_PER_L",
                "CultureMech:000130",
                "SES",
                "One half of the final 1:1 mixture.",
            ),
            SolutionSpec(
                "PJ (Prescott's and James's Solution)",
                "500",
                "ML_PER_L",
                "CultureMech:000112",
                "PJ",
                "One half of the final 1:1 mixture.",
            ),
        ),
        steps=(
            step("MIX", "Autoclave the constituent media separately, then mix aseptically at 1:1."),
        ),
    ),
)


def signature(value: dict[str, Any]) -> RowSignature:
    concentration = value.get("concentration") or {}
    return RowSignature(
        str(value.get("preferred_term") or ""),
        str(concentration.get("value") or ""),
        str(concentration.get("unit") or ""),
    )


def ingredient(spec: IngredientSpec, source: str) -> dict[str, Any]:
    value: dict[str, Any] = {
        "preferred_term": spec.name,
        "concentration": {"value": spec.value, "unit": spec.unit},
        "source": f"CCAP Medium {source}",
        "notes": spec.notes,
    }
    if spec.term_id and spec.term_label:
        value["term"] = {"id": spec.term_id, "label": spec.term_label}
        if spec.mim_link and spec.term_id.startswith("CHEBI:"):
            value["mediaingredientmech_chebi_term"] = {
                "id": spec.term_id,
                "label": spec.term_label,
            }
    return value


def solution(spec: SolutionSpec, source: str) -> dict[str, Any]:
    return {
        "preferred_term": spec.name,
        "culturemech_term": {
            "id": spec.culturemech_id,
            "label": spec.culturemech_label,
        },
        "concentration": {"value": spec.value, "unit": spec.unit},
        "notes": f"{spec.notes} Source: CCAP Medium {source}.",
    }


def _history(doc: dict[str, Any], path: str) -> list[dict[str, Any]]:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{path}: curation_history is not a list")
    return history


def _already_applied(doc: dict[str, Any], path: str) -> bool:
    return any(
        isinstance(event, dict) and event.get("action") == ACTION for event in _history(doc, path)
    )


def _append_steps(doc: dict[str, Any], specs: tuple[StepSpec, ...], path: str) -> None:
    current = doc.setdefault("preparation_steps", [])
    if not isinstance(current, list):
        raise ValueError(f"{path}: preparation_steps is not a list")
    start = max(
        (int(item.get("step_number", 0)) for item in current if isinstance(item, dict)),
        default=0,
    )
    for offset, spec in enumerate(specs, start=1):
        current.append(
            {
                "step_number": start + offset,
                "action": spec.action,
                "description": spec.description,
            }
        )


def _append_event(doc: dict[str, Any], path: str, source: str, before: int, after: int) -> None:
    _history(doc, path).append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_ccap_instruction_rows.py",
            "action": ACTION,
            "changes": f"ingredients {before} -> {after}",
            "notes": (
                f"Repaired preparation text and nested-recipe flattening against CCAP {source}. "
                "Moved process statements to preparation_steps and restored source-asserted "
                "components or constituent-medium references where applicable."
            ),
        }
    )


def repair_simple(doc: dict[str, Any], target: SimpleTarget) -> tuple[dict[str, Any], bool]:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')!r}")
    current = [item for item in (doc.get("ingredients") or []) if isinstance(item, dict)]
    signatures = [signature(item) for item in current]
    if _already_applied(doc, target.path):
        lingering = [expected for expected in target.rows if expected in signatures]
        if lingering:
            raise ValueError(
                f"{target.path}: repaired event exists but old rows remain: {lingering!r}"
            )
        return doc, False

    indexes: list[int] = []
    for expected in target.rows:
        matches = [index for index, observed in enumerate(signatures) if observed == expected]
        if len(matches) != 1:
            raise ValueError(f"{target.path}: expected one {expected!r} row, found {len(matches)}")
        indexes.append(matches[0])

    repaired = copy.deepcopy(doc)
    new_ingredients = [item for index, item in enumerate(current) if index not in set(indexes)]
    insertion = min(indexes)
    new_ingredients[insertion:insertion] = [
        ingredient(spec, target.source) for spec in target.replacements
    ]
    repaired["ingredients"] = new_ingredients

    if target.add_solutions:
        if repaired.get("solutions"):
            raise ValueError(f"{target.path}: unexpected pre-existing solutions")
        repaired["solutions"] = [solution(spec, target.source) for spec in target.add_solutions]
    _append_steps(repaired, target.steps, target.path)
    for field, value in target.field_updates:
        repaired[field] = value
    if target.add_variants:
        variants = repaired.setdefault("variants", [])
        if not isinstance(variants, list):
            raise ValueError(f"{target.path}: variants is not a list")
        variants.extend(copy.deepcopy(target.add_variants))
    _append_event(repaired, target.path, target.source, len(current), len(new_ingredients))
    return repaired, True


def repair_rebuild(doc: dict[str, Any], target: RebuildTarget) -> tuple[dict[str, Any], bool]:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(f"{target.path}: expected {target.record_id}, found {doc.get('id')!r}")
    current = [item for item in (doc.get("ingredients") or []) if isinstance(item, dict)]
    signatures = tuple(signature(item) for item in current)
    if _already_applied(doc, target.path):
        if signatures == target.current_rows:
            raise ValueError(f"{target.path}: repaired event exists but old structure remains")
        return doc, False
    if signatures != target.current_rows:
        raise ValueError(
            f"{target.path}: ingredient signature drifted:\n"
            f"expected {target.current_rows!r}\nobserved {signatures!r}"
        )
    if doc.get("solutions") or doc.get("preparation_steps"):
        raise ValueError(f"{target.path}: unexpected pre-existing solutions or preparation steps")

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = [ingredient(spec, target.source) for spec in target.ingredients]
    repaired["solutions"] = [solution(spec, target.source) for spec in target.solutions]
    _append_steps(repaired, target.steps, target.path)
    if target.add_variants:
        variants = repaired.setdefault("variants", [])
        if not isinstance(variants, list):
            raise ValueError(f"{target.path}: variants is not a list")
        variants.extend(copy.deepcopy(target.add_variants))
    _append_event(repaired, target.path, target.source, len(current), len(target.ingredients))
    return repaired, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans: list[tuple[Path, dict[str, Any]]] = []
    for target, repair in (
        *((target, repair_simple) for target in SIMPLE_TARGETS),
        *((target, repair_rebuild) for target in REBUILD_TARGETS),
    ):
        path = args.normalized_dir / target.path
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            raise SystemExit(f"Could not load {path}: {exc}") from exc
        if not isinstance(doc, dict):
            raise SystemExit(f"{path}: expected a YAML mapping")
        repaired, changed = repair(doc, target)
        print(f"{'fix' if changed else 'skip':4s}  {target.path}")
        if changed:
            plans.append((path, repaired))

    if args.apply:
        for path, repaired in plans:
            write_record(path, repaired)
    mode = "updated" if args.apply else "would update"
    print(f"\n{mode} {len(plans)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
