#!/usr/bin/env python3
"""Restore the 29 empty SAG records from reviewed SAG source PDFs.

The SAG import retained source URLs but not recipe contents. This migration
encodes the formulations from the reviewed PDFs without flattening stock
solutions into final-medium concentrations. It also treats the separately
imported soil-water note as a source duplicate of SAG medium 3.

Apply mode requires exact local copies of all reviewed PDFs and verifies their
SHA-256 hashes before validating every target and writing any record. Dry-run is
the default.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
MIM_SSSOM = REPO.parent / "MediaIngredientMech" / "mappings" / "ingredient_mappings.sssom.tsv"
ACTION = "RESTORED_SAG_SOURCE_COMPOSITION"
TIMESTAMP = "2026-08-25T00:00:00-07:00"


@dataclass(frozen=True)
class Source:
    file_name: str
    sha256: str
    url: str


def _source(file_stem: str, sha256: str, remote_name: str) -> Source:
    return Source(
        file_name=f"SAG_{file_stem}.pdf",
        sha256=sha256,
        url=f"https://sagdb.uni-goettingen.de/culture_media/{remote_name}",
    )


SOURCES = {
    "01": _source(
        "01_Basal_Medium",
        "375c4f2ec4d27129787ed86636130675cb64faedcaa9d312ff42e1f37d365edb",
        "01%20Basal%20Medium.pdf",
    ),
    "02": _source(
        "02_Spirulina_Medium",
        "21e6036ced504681ada468b15e96f8e4693e13b87e621bcbfabe44be6a2c9cd8",
        "02%20Spirulina%20Medium.pdf",
    ),
    "03": _source(
        "03_Soil_Water_Media",
        "4e5a79e144ff88744e701bb644369ca197704b6a6c1db060652c7229d843f367",
        "03%20Soil%20Water%20Media.pdf",
    ),
    "04": _source(
        "04_Beggiatoa_Medium",
        "cde6074dcbebedfccef59f0af18620f6801dfab48e0e198dd0d281263e8f91bf",
        "04%20%20Beggiatoa%20Medium.pdf",
    ),
    "05": _source(
        "05_Seawater_Medium",
        "7cf200933fc784330baef63aec0e1487eb311247687de5318ec61f38a03c21d0",
        "05%20Seawater%20Medium.pdf",
    ),
    "06": _source(
        "06_Brackish_water_medium",
        "5a92afd0df065d50f348c964857f98e1be43217ecc6173911a7762aa42fe85ae",
        "06%20Brackish%20water%20medium.pdf",
    ),
    "07": _source(
        "07_Desmidiacean_Medium",
        "6d7b4d0f2c2e68d631ccdb0a40666a7981407d46f80de6864c3b9ea28c56b3b5",
        "07%20Desmidiacean%20Medium.pdf",
    ),
    "08": _source(
        "08_Porphyridium_Medium",
        "4af6add4c928721374b38132933f522d01fe62230c2b29747ed59c4291cc69d1",
        "08%20Porphyridium%20Medium.pdf",
    ),
    "09": _source(
        "09_Euglena_Medium",
        "ad2bc915012122e5b69fc524673b5d0131a9c90d6f96ba6dd93dad56a977351f",
        "09%20Euglena%20Medium.pdf",
    ),
    "10": _source(
        "10_Ochromonas_Medium",
        "8b15d4c6303bc0e583d73e8d1e861c6a63ab5374bcadc58fa57af1bf3e83d63e",
        "10%20Ochromonas%20Medium.pdf",
    ),
    "11": _source(
        "11_Bacillariophycean_Medium",
        "e1cacf2bec48469be18d742c84acb08914a2984aa9b3585478c459ea30b9c368",
        "11%20Bacillariophycean%20Medium.pdf",
    ),
    "12": _source(
        "12_Unicellular_Green_Algae",
        "7c767329e2b64fe81d9fe55f28bfcef8245a5ba3b83397824eda9bbcc86164f4",
        "12%20Unicellular%20Green%20Algae%20Medium.pdf",
    ),
    "13": _source(
        "13_Polytoma_Medium",
        "49893ff12751817bc61dd4b326532f46b2964fe407eb4bcc0592a6f5348b9159",
        "13%20Polytoma%20Medium.pdf",
    ),
    "14": _source(
        "14_Dunaliella_Medium",
        "a76f61951039b7b8340473007768b5f71f4c9ea6088d860fcf0b300b63ff2e5e",
        "14%20Dunaliella%20Medium.pdf",
    ),
    "15": _source(
        "15_Polytomella_Medium",
        "a9f3d4ecb556384bf10c73d6ee6ea809a4582e1b4d19dd0c952a4773b9eda5cd",
        "15%20Polytomella%20Medium.pdf",
    ),
    "16": _source(
        "16_Malt_Peptone_Medium",
        "e14903e5c117227f8bb72661a142e55d934dd3befdfe284ec0103d12134cab15",
        "16%20Malt%20Peptone%20Medium.pdf",
    ),
    "17": _source(
        "17_Cyanidium_Medium",
        "d304e35db6b75fc8b639518cf9dc299954b872718d15f1caeb02ca062039976f",
        "17%20Cyanidium%20Medium.pdf",
    ),
    "18": _source(
        "18_Dunaliella_acid_Medium",
        "b06e06941e5bc5a2d26a89796f770c7215523616d3257d927bf9275723797fc4",
        "18%20Dunaliella%20acid%20Medium.pdf",
    ),
    "19": _source(
        "19_Z_Medium_for_Cyanos",
        "4a1c1aa967637b9212a814bd01ebffa554338105e8c1a1bee7d03a93cd07b6d6",
        "19%20Z-Medium%20for%20Cyanos.pdf",
    ),
    "21": _source(
        "21_Chilomonas_Medium",
        "6e03572f3f96ac2ed3138740d7966469494281243d4e95e9b6493077a0668c1a",
        "21%20Chilomonas%20Medium.pdf",
    ),
    "22": _source(
        "22_Volvox_Medium",
        "78a992920c3a2d858a65417013c16b8a3fd4a0b5642b5dd3b417f27046e40a02",
        "22%20Volvox%20Medium.pdf",
    ),
    "23": _source(
        "23_Enriched_Seawater_Medium",
        "a74fc20ffe60e1ab58ec5dc02090fdebd5bede978bec0bb2b9ef9236eec10a20",
        "23%20Enriched%20Seawater%20Medium.pdf",
    ),
    "24": _source(
        "24_WC_Medium",
        "7c53c28713fc1b1b95f6dcc518e3b9e1324a25ee6ccf7a4064a2cd369f7dcaf7",
        "24%20WC%20Medium.pdf",
    ),
    "25": _source(
        "25_Artificial_Seawater_Medium",
        "0735fc07df10bd546b0e10fe21d3ee8cfad830775d7ae8e0afbba9137eb0a128",
        "25%20Artificial%20Seawater%20Medium.pdf",
    ),
    "26": _source(
        "26_Bold_Modified_Basal_Medium",
        "71ff69ab6b5c184ad5777e2c99ebf9be353c536cdba664871edd3bb747378a7f",
        "26%20Bold%20Modified%20Basal%20Medium.pdf",
    ),
    "28": _source(
        "28_WEES_Medium",
        "2ac8f35dfedff05a1d56b0b5e8d48a56e64c681ad47efb4aabe11b2b547ea898",
        "28%20WEES%20Medium.pdf",
    ),
    "29": _source(
        "29_PES_Medium",
        "951aaf669593437fca489369dda2e8e88737f598c3b984da1185e6b0c52e76f1",
        "29%20PES%20Medium.pdf",
    ),
    "30": _source(
        "30_Bold_Modified_Basal_TOM",
        "e6d2940c4685e5c2c16fbb1526d3f7f0f7160747acd37746b50491851e6577c5",
        "30%20Bold%20Modified%20Basal%20Medium%26TOM.pdf",
    ),
    "note": _source(
        "Note_on_biphasic_soilwater_media_20081216",
        "36370756f412e9d6e84491114f59ec91a7fc7099b1657f23a3fe07a484bfd518",
        "Note_on_biphasic_soilwater_media_20081216.pdf",
    ),
}


@dataclass(frozen=True)
class Target:
    relative_path: str
    record_id: str
    recipe_key: str
    source_key: str


TARGETS = (
    Target("algae/artificial_seawater.yaml", "CultureMech:000189", "artificial_seawater", "25"),
    Target("algae/bacillariophycean.yaml", "CultureMech:000192", "bacillariophycean", "11"),
    Target("algae/basal.yaml", "CultureMech:000191", "basal", "01"),
    Target("algae/beggiatoa.yaml", "CultureMech:000193", "beggiatoa", "04"),
    Target("algae/bold_modified_basal.yaml", "CultureMech:000194", "bold_modified_basal", "26"),
    Target(
        "algae/bold_modified_basal_tom.yaml", "CultureMech:000195", "bold_modified_basal_tom", "30"
    ),
    Target("algae/brackish_water_medium.yaml", "CultureMech:000196", "brackish", "06"),
    Target("algae/chilomonas.yaml", "CultureMech:000197", "chilomonas", "21"),
    Target("algae/cyanidium.yaml", "CultureMech:000198", "cyanidium", "17"),
    Target("algae/desmidiacean.yaml", "CultureMech:000199", "desmidiacean", "07"),
    Target("algae/dunaliella.yaml", "CultureMech:000200", "dunaliella", "14"),
    Target("algae/dunaliella_acid.yaml", "CultureMech:000201", "dunaliella_acid", "18"),
    Target("algae/enriched_seawater.yaml", "CultureMech:000202", "enriched_seawater", "23"),
    Target("algae/euglena.yaml", "CultureMech:000203", "euglena", "09"),
    Target("algae/malt_peptone.yaml", "CultureMech:000204", "malt_peptone", "16"),
    Target(
        "algae/note_on_biphasic_soilwater_media_20081216.yaml",
        "CultureMech:000205",
        "soil_water_note",
        "note",
    ),
    Target("algae/ochromonas.yaml", "CultureMech:000206", "ochromonas", "10"),
    Target("algae/pes.yaml", "CultureMech:000207", "pes", "29"),
    Target("algae/polytoma.yaml", "CultureMech:000208", "polytoma", "13"),
    Target("algae/polytomella.yaml", "CultureMech:000209", "polytomella", "15"),
    Target("algae/porphyridium.yaml", "CultureMech:000210", "porphyridium", "08"),
    Target("algae/seawater.yaml", "CultureMech:000211", "seawater", "05"),
    Target("algae/soil_water_media.yaml", "CultureMech:000212", "soil_water", "03"),
    Target("algae/spirulina.yaml", "CultureMech:000213", "spirulina", "02"),
    Target("algae/unicellular_green_algae.yaml", "CultureMech:000214", "unicellular_green", "12"),
    Target("algae/volvox.yaml", "CultureMech:000215", "volvox", "22"),
    Target("algae/wees.yaml", "CultureMech:000216", "wees", "28"),
    Target("algae/woods_hole_mbl_medium.yaml", "CultureMech:000217", "wc", "24"),
    Target("algae/z_medium_for_cyanos.yaml", "CultureMech:000218", "z_medium", "19"),
)


# Selected object mappings from the 2026-08-18 MediaIngredientMech SSSOM. No
# ontology identifier is added for source labels without a defensible SSSOM row.
MIM_TERMS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Asparagine": ("CHEBI:22653", "asparagine"),
    "Bacto-tryptone": ("MICRO:0000182", "tryptone"),
    "Beef extract": ("FOODON:03302088", "beef extract"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "Ca(NO3)2 x 4 H2O": ("CHEBI:86159", "calcium nitrate tetrahydrate"),
    "CaCl2 x 2 H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CaSO4": ("CHEBI:31346", "calcium sulfate"),
    "Cd(NO3)2 x 4 H2O": ("CHEBI:86156", "cadmium nitrate tetrahydrate"),
    "Citric acid": ("CHEBI:30769", "citric acid"),
    "Co(NO3)2 x 6 H2O": ("CHEBI:86214", "cobalt dinitrate hexahydrate"),
    "CoSO4 x 7 H2O": ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    "Cobalt chloride hexahydrate": ("CHEBI:53503", "cobalt chloride hexahydrate"),
    "Cr(NO3)3 x 7 H2O": ("CHEBI:86206", "chromium trinitrate heptahydrate"),
    "CuSO4 x 5 H2O": ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "EDTA": ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    "Fe(III) citrate": ("CHEBI:144421", "iron(III) citrate"),
    "Fe(NH4)2(SO4)2 x 6 H2O": ("CHEBI:76181", "ferrous ammonium sulfate hexahydrate"),
    "FeCl2 x 6 H2O": ("CHEBI:30812", "iron dichloride"),
    "FeCl3 x 6 H2O": ("CHEBI:86254", "iron trichloride hexahydrate"),
    "FeSO4 x 7 H2O": ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    "Filtered Seawater": ("MICRO:0001773", "filtered seawater"),
    "Garden soil": ("ENVO:00002263", "garden soil"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Glycyl-glycine": ("CHEBI:17201", "glycylglycine"),
    "H2SO4": ("CHEBI:26836", "sulfuric acid"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "HEPES": ("CHEBI:42334", "2-[4-(2-hydroxyethyl)piperazin-1-yl]ethanesulfonic acid"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "K2HPO4 x 3 H2O": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "K2SO4": ("CHEBI:32036", "potassium sulfate"),
    "KBr": ("CHEBI:32030", "potassium bromide"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "KI": ("CHEBI:8346", "potassium iodide"),
    "KNO3": ("CHEBI:63043", "potassium nitrate"),
    "KOH": ("CHEBI:32035", "potassium hydroxide"),
    "Liver extract": ("MICRO:0001363", "liver extract"),
    "Malt extract": ("FOODON:03301056", "malt extract"),
    "MgSO4 x 7 H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "MnCl2 x 4 H2O": ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    "MnSO4 x 4 H2O": ("CHEBI:86358", "manganese(II) sulfate tetrahydrate"),
    "MnSO4 x H2O": ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
    "Na-acetate": ("CHEBI:32954", "sodium acetate"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na2HPO4 x 2 H2O": (
        "CHEBI:91258",
        "disodium hydrogenphosphate dihydrate",
    ),
    "Na2MoO4 x 2 H2O": ("CHEBI:75213", "sodium molybdate dihydrate"),
    "Na2SiO3 x 9 H2O": ("CHEBI:132108", "sodium silicate nonahydrate"),
    "Na2WO4 x 2 H2O": ("CHEBI:63939", "sodium tungstate dihydrate"),
    "Na2glycerophosphate x 5 H2O": (
        "CHEBI:15978",
        "sn-glycerol 3-phosphate",
    ),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaH2PO4 x H2O": ("CHEBI:37585", "sodium dihydrogenphosphate"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "NaNO3": ("CHEBI:63005", "sodium nitrate"),
    "Natural sea water": ("ENVO:00002149", "sea water"),
    "(NH4)2HPO4": ("CHEBI:63051", "diammonium hydrogen phosphate"),
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Nicotinamide": ("CHEBI:17154", "nicotinamide"),
    "Pasteurized Seawater": ("ENVO:00002149", "sea water"),
    "Proteose Peptone": ("MICRO:0000180", "proteose peptone"),
    "TES": ("CHEBI:39035", "TES"),
    "Thiamine": ("CHEBI:18385", "thiamine(1+)"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
    "VOSO4 x 2 H2O": ("CHEBI:87009", "vanadyl sulfate dihydrate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
    "ZnCl2": ("CHEBI:49976", "zinc dichloride"),
    "ZnSO4 x 7 H2O": ("CHEBI:32312", "zinc sulfate heptahydrate"),
}


def ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    mapping_key: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
    }
    mapped = MIM_TERMS.get(mapping_key or preferred_term)
    if mapped:
        identifier, label = mapped
        row["term"] = {"id": identifier, "label": label}
        if identifier.startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = {
                "id": identifier,
                "label": label,
            }
    if notes:
        row["notes"] = notes
    return row


def stock(
    preferred_term: str,
    use_ml_per_l: str,
    composition: list[dict[str, Any]],
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "composition": composition,
        "concentration": {"value": use_ml_per_l, "unit": "ML_PER_L"},
    }
    if notes:
        row["notes"] = notes
    return row


def single_stock(
    solute: str,
    stock_value: str,
    use_ml_per_l: str,
    *,
    stock_unit: str = "G_PER_L",
    solution_name: str | None = None,
    mapping_key: str | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    return stock(
        solution_name or f"{solute} stock solution",
        use_ml_per_l,
        [ingredient(solute, stock_value, stock_unit, mapping_key=mapping_key)],
        notes=notes,
    )


def step(number: int, action: str, description: str) -> dict[str, Any]:
    return {"step_number": number, "action": action, "description": description}


def water(value: str, unit: str = "ML_PER_L", *, notes: str | None = None) -> dict[str, Any]:
    return ingredient(
        "Deionized or distilled water",
        value,
        unit,
        mapping_key="Distilled water",
        notes=notes,
    )


def vitamin_b12(*, notes: str = "Add in sterile solution after cooling.") -> dict[str, Any]:
    return ingredient("Vitamin B12", "0.005", "MG_PER_L", notes=notes)


def soil_extract(use_ml_per_l: str, *, peat: bool = False) -> dict[str, Any]:
    material = "Peat soil" if peat else "Garden or leaf soil"
    mapping_key = None if peat else "Garden soil"
    return stock(
        "Peat extract" if peat else "Soil extract",
        use_ml_per_l,
        [
            ingredient(
                material,
                "1",
                "VARIABLE",
                mapping_key=mapping_key,
                notes="Fill one third of a vessel; the source gives a geometric amount.",
            ),
            water(
                "1",
                "VARIABLE",
                notes="Add until water stands 5 cm above the soil.",
            ),
        ],
        notes=(
            "Steam for 1 hour twice at a 24-hour interval, decant and centrifuge, "
            "then autoclave aliquots for 20 minutes at 121 C. Concentrations are "
            "unspecified by the source."
        ),
    )


def micronutrient_1(use_ml_per_l: str = "5") -> dict[str, Any]:
    return stock(
        "SAG medium 1 micronutrient solution",
        use_ml_per_l,
        [
            ingredient("ZnSO4 x 7 H2O", "1", "MG_PER_L"),
            ingredient("MnSO4 x 4 H2O", "2", "MG_PER_L"),
            ingredient("H3BO3", "10", "MG_PER_L"),
            ingredient("Co(NO3)2 x 6 H2O", "1", "MG_PER_L"),
            ingredient("Na2MoO4 x 2 H2O", "1", "MG_PER_L"),
            ingredient("CuSO4 x 5 H2O", "0.005", "MG_PER_L"),
            ingredient("FeSO4 x 7 H2O", "700", "MG_PER_L"),
            ingredient("EDTA", "800", "MG_PER_L"),
            water("981"),
        ],
        notes=(
            "Stock concentrations are calculated from the source primary-stock "
            "volumes into the 1 L applied solution. Prepare as two separately "
            "autoclaved solutions and unite after cooling."
        ),
    )


def saturated_caso4(use_ml_per_l: str) -> dict[str, Any]:
    return stock(
        "Saturated CaSO4 solution",
        use_ml_per_l,
        [
            ingredient(
                "CaSO4",
                "1",
                "VARIABLE",
                notes="Prepare a saturated solution; the source gives no mass concentration.",
            )
        ],
    )


def default_steps(*, heat_labile: bool = False) -> list[dict[str, Any]]:
    rows = [step(1, "MIX", "Prepare the stock solutions and combine them at the stated amounts.")]
    rows.append(
        step(
            2,
            "AUTOCLAVE",
            "Autoclave at 121 C for 15 minutes following the SAG general preparation guidance.",
        )
    )
    if heat_labile:
        rows.append(step(3, "COOL", "Cool before adding sterile heat-labile components."))
    return rows


def liquid_recipe(
    ingredients: list[dict[str, Any]],
    solutions: list[dict[str, Any]],
    *,
    steps: list[dict[str, Any]] | None = None,
    ph_range: dict[str, Any] | None = None,
    sterilization: dict[str, Any] | None = None,
) -> dict[str, Any]:
    recipe: dict[str, Any] = {
        "ingredients": ingredients,
        "solutions": solutions,
        "preparation_steps": steps if steps is not None else default_steps(),
        "physical_state": "LIQUID",
    }
    if ph_range:
        recipe["ph_range"] = ph_range
    recipe["sterilization"] = sterilization or {"method": "AUTOCLAVE"}
    return recipe


def basal_recipe() -> dict[str, Any]:
    recipe = liquid_recipe(
        [water("905")],
        [
            single_stock("KNO3", "10", "20"),
            single_stock("K2HPO4", "1", "20"),
            single_stock("MgSO4 x 7 H2O", "1", "20"),
            soil_extract("30"),
            micronutrient_1(),
        ],
    )
    recipe["preparation_steps"].append(
        step(
            3,
            "MIX",
            "The source also describes beef-extract, peptone, Euglena-plus-vitamin, "
            "and sulfuric-acid variants; these are not part of the base formulation.",
        )
    )
    return recipe


def spirulina_recipe() -> dict[str, Any]:
    solution_i = stock(
        "Spirulina solution I",
        "500",
        [
            ingredient("NaHCO3", "27.22", "G_PER_L"),
            ingredient("Na2CO3", "8.06", "G_PER_L"),
            ingredient("K2HPO4", "1.00", "G_PER_L"),
            water("1", "L", notes="Prepare solution I to 500 mL."),
        ],
        notes="Composition normalized from the source 500 mL batch.",
    )
    solution_ii = stock(
        "Spirulina solution II",
        "500",
        [
            ingredient("NaNO3", "5.00", "G_PER_L"),
            ingredient("K2SO4", "2.00", "G_PER_L"),
            ingredient("NaCl", "2.00", "G_PER_L"),
            ingredient("MgSO4 x 7 H2O", "0.40", "G_PER_L"),
            ingredient("CaCl2 x 2 H2O", "0.08", "G_PER_L"),
            ingredient("FeSO4 x 7 H2O", "0.02", "G_PER_L"),
            ingredient("EDTA", "0.16", "G_PER_L"),
            water("1", "L", notes="Prepare solution II to 500 mL."),
        ],
        notes=(
            "Composition normalized from the source 500 mL batch. Its 5 mL "
            "micronutrient addition is modeled as a separate final-recipe stock "
            "because all of solution II is used."
        ),
    )
    return liquid_recipe(
        [],
        [solution_i, solution_ii, micronutrient_1()],
        steps=[
            step(1, "MIX", "Prepare solutions I and II separately."),
            step(2, "AUTOCLAVE", "Autoclave solutions I and II separately."),
            step(3, "COOL", "Cool, then unite equal 500 mL portions."),
            step(
                4,
                "MIX",
                "If required, add sterile vitamin B12 to 5 x 10^-6 g/L; it is optional in the source.",
            ),
        ],
    )


def soil_water_core() -> dict[str, Any]:
    return {
        "ingredients": [
            ingredient(
                "Garden soil",
                "1",
                "VARIABLE",
                notes="Place a 1-2 cm soil layer in the bottom of the vessel.",
            ),
            water(
                "1",
                "VARIABLE",
                notes="Fill the vessel three-quarters full over the soil layer.",
            ),
        ],
        "solutions": [],
        "preparation_steps": [
            step(
                1,
                "MIX",
                "Optionally place a small amount of the selected insoluble organic or inorganic supplement in the vessel.",
            ),
            step(2, "MIX", "Add 1-2 cm garden soil and overlay with water to three-quarters full."),
            step(3, "HEAT", "Steam for 1 hour on two consecutive days; do not autoclave."),
            step(
                4,
                "MIX",
                "Source variants use CaCO3, NH4MgPO4, soaked pea, barley, wheat, sand, loam, or peat.",
            ),
        ],
        "physical_state": "BIPHASIC",
        "sterilization": {
            "method": "TYNDALLIZATION",
            "duration": "1 hour on two consecutive days",
            "notes": "The source explicitly says not to autoclave so surviving soil bacteria remain.",
        },
    }


def soil_water_recipe() -> dict[str, Any]:
    recipe = soil_water_core()
    recipe["variant_children"] = [
        {
            "id": "CultureMech:000205",
            "name": "note_on_biphasic_soilwater_media_20081216",
            "path": "data/normalized_yaml/algae/note_on_biphasic_soilwater_media_20081216.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "notes": "Separate SAG explanatory document for the same soil-water formulation.",
        }
    ]
    return recipe


def soil_water_note_recipe() -> dict[str, Any]:
    recipe = soil_water_core()
    recipe["parent_media"] = {
        "id": "CultureMech:000212",
        "name": "soil_water_media",
        "path": "data/normalized_yaml/algae/soil_water_media.yaml",
        "relationship": "SOURCE_DUPLICATE",
        "notes": "This record is the separately imported SAG explanatory note for medium 3.",
    }
    recipe["variant_relationship"] = "SOURCE_DUPLICATE"
    recipe["variant_modifications"] = [
        "Adds explanatory background and examples but does not define a distinct base formulation."
    ]
    return recipe


def beggiatoa_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [water("875"), vitamin_b12()],
        [
            single_stock("NH4Cl", "4", "20"),
            single_stock("K2HPO4", "1", "10"),
            saturated_caso4("20"),
            single_stock("MgSO4 x 7 H2O", "1", "10"),
            single_stock("Na-acetate", "10", "10"),
            single_stock("Asparagine", "10", "50"),
            micronutrient_1(),
        ],
        steps=[
            step(1, "MIX", "Combine the stock solutions and water at the stated amounts."),
            step(2, "HEAT", "Steam for 1 hour, or autoclave if axenic culture is desired."),
            step(3, "COOL", "Cool and add vitamin B12 in sterile solution."),
        ],
        sterilization={
            "method": "AUTOCLAVE",
            "notes": "The source permits one-hour steaming instead when axenic culture is not required.",
        },
    )


def seawater_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [
            ingredient("Filtered seawater", "905", "ML_PER_L", mapping_key="Filtered Seawater"),
            vitamin_b12(),
        ],
        [
            single_stock("KNO3", "10", "20"),
            single_stock("K2HPO4", "1", "20"),
            single_stock("MgSO4 x 7 H2O", "1", "20"),
            soil_extract("30"),
            micronutrient_1(),
        ],
        steps=[
            step(1, "MIX", "Combine the stocks with filtered seawater."),
            step(
                2,
                "AUTOCLAVE",
                "Autoclave soil extract separately; steam or autoclave the remaining medium.",
            ),
            step(3, "COOL", "Unite after cooling and add sterile vitamin B12."),
            step(
                4,
                "MIX",
                "Silicate and selenite variants are described separately in the source and are not asserted here.",
            ),
        ],
    )


def brackish_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [
            water("450"),
            ingredient("Filtered seawater", "455", "ML_PER_L", mapping_key="Filtered Seawater"),
            vitamin_b12(),
        ],
        [
            single_stock("KNO3", "10", "20"),
            single_stock("K2HPO4", "1", "20"),
            single_stock("MgSO4 x 7 H2O", "1", "20"),
            soil_extract("30"),
            micronutrient_1(),
        ],
        steps=[
            step(1, "MIX", "Combine the stocks with equal parts water and filtered seawater."),
            step(
                2,
                "AUTOCLAVE",
                "Autoclave soil extract separately; steam or autoclave the remaining medium.",
            ),
            step(3, "COOL", "Unite after cooling and add sterile vitamin B12."),
            step(
                4,
                "MIX",
                "Silicate and selenite variants are described separately in the source and are not asserted here.",
            ),
        ],
    )


def desmidiacean_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [water("930"), vitamin_b12()],
        [
            single_stock("KNO3", "10", "10"),
            single_stock("(NH4)2HPO4", "2", "5"),
            single_stock("MgSO4 x 7 H2O", "1", "10"),
            saturated_caso4("10"),
            soil_extract("20"),
            soil_extract("10", peat=True),
            micronutrient_1(),
        ],
        steps=default_steps(heat_labile=True)
        + [
            step(
                4, "MIX", "Add sterile vitamin B12; a separate source variant also adds vitamin B1."
            )
        ],
    )


def porphyridium_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [
            water("390"),
            ingredient("Filtered seawater", "500", "ML_PER_L", mapping_key="Filtered Seawater"),
        ],
        [
            single_stock("KNO3", "10", "20"),
            single_stock("K2HPO4", "1", "20"),
            single_stock("MgSO4 x 7 H2O", "1", "20"),
            single_stock("Yeast extract", "100", "10"),
            single_stock("Bacto-tryptone", "100", "10"),
            soil_extract("30"),
        ],
    )


def euglena_recipe() -> dict[str, Any]:
    recipe = liquid_recipe(
        [water("910")],
        [
            single_stock("Na-acetate", "100", "10"),
            single_stock("Beef extract", "100", "10"),
            single_stock("Bacto-tryptone", "100", "20"),
            single_stock("Yeast extract", "100", "20"),
            soil_extract("30"),
        ],
    )
    recipe["preparation_steps"].append(
        step(
            3,
            "MIX",
            "Mineral, half-strength, and brackish variants are described separately and are not asserted in the base recipe.",
        )
    )
    return recipe


def ochromonas_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [water("960")],
        [
            single_stock("Glucose", "100", "10"),
            single_stock("Bacto-tryptone", "100", "10"),
            single_stock("Liver extract", "100", "10"),
            single_stock("Yeast extract", "100", "10"),
        ],
    )


def bacillariophycean_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [water("820"), vitamin_b12()],
        [
            single_stock("Ca(NO3)2 x 4 H2O", "2", "20"),
            single_stock("K2HPO4", "1", "10"),
            single_stock("MgSO4 x 7 H2O", "1", "25"),
            single_stock("Na2CO3", "1", "20"),
            single_stock("Na2SiO3 x 9 H2O", "1", "50"),
            single_stock("Fe-citrate", "1", "10", mapping_key="Fe(III) citrate"),
            single_stock("Citric acid", "1", "10"),
            soil_extract("30"),
            micronutrient_1(),
        ],
        steps=default_steps(heat_labile=True)
        + [
            step(4, "MIX", "Add sterile vitamin B12 after cooling."),
            step(
                5,
                "MIX",
                "The vitamin-mix variant is described separately and is not asserted here.",
            ),
        ],
    )


def unicellular_green_recipe() -> dict[str, Any]:
    fe_edta = stock(
        "Fe-EDTA complex",
        "1",
        [
            ingredient("FeSO4 x 7 H2O", "6.9", "G_PER_L"),
            ingredient(
                "Disodium EDTA",
                "9.3",
                "G_PER_L",
                notes="The source specifies disodium EDTA but no hydration state.",
            ),
            water("1", "L", notes="Prepare the stock to 100 mL."),
        ],
        notes=(
            "Boil briefly, cool, and make to volume. The medium table prints "
            "6.95 mg/L FeSO4 x 7 H2O; the stock recipe calculates to 6.9 mg/L."
        ),
    )
    micronutrients = stock(
        "Unicellular green algae micronutrient solution",
        "1",
        [
            ingredient("H3BO3", "61.0", "MG_PER_L"),
            ingredient("MnSO4 x H2O", "169.0", "MG_PER_L"),
            ingredient("ZnSO4 x 7 H2O", "287.0", "MG_PER_L"),
            ingredient("CuSO4 x 5 H2O", "2.5", "MG_PER_L"),
            ingredient(
                "(NH4)6Mo7O24 x 4 H2O",
                "12.5",
                "MG_PER_L",
                mapping_key="ammonium molybdate tetrahydrate",
            ),
            water("1", "L"),
        ],
    )
    return liquid_recipe(
        [
            ingredient("KNO3", "1011.1", "MG_PER_L"),
            ingredient("NaH2PO4 x H2O", "621", "MG_PER_L"),
            ingredient("Na2HPO4 x 2 H2O", "89", "MG_PER_L"),
            ingredient("MgSO4 x 7 H2O", "246.5", "MG_PER_L"),
            ingredient("CaCl2 x 2 H2O", "14.7", "MG_PER_L"),
            water("1", "L", notes="Make the final medium to 1 L."),
        ],
        [fe_edta, micronutrients],
    )


def polytoma_recipe() -> dict[str, Any]:
    recipe = liquid_recipe(
        [water("950")],
        [
            single_stock("Yeast extract", "100", "10"),
            single_stock("Bacto-tryptone", "100", "10"),
            soil_extract("30"),
        ],
    )
    recipe["preparation_steps"].append(
        step(3, "MIX", "The Polytoma-glucose variant adds 20 mL/L of 100 g/L glucose stock.")
    )
    return recipe


def dunaliella_recipe() -> dict[str, Any]:
    artificial_seawater = stock(
        "Artificial seawater",
        "930",
        [
            ingredient("NaCl", "60.0", "G_PER_L"),
            ingredient("MgSO4 x 7 H2O", "10.0", "G_PER_L"),
            ingredient("KCl", "1.5", "G_PER_L"),
            ingredient("CaSO4", "2.0", "G_PER_L"),
            water("1", "L"),
        ],
    )
    return liquid_recipe(
        [],
        [
            single_stock("KNO3", "10", "20"),
            single_stock("K2HPO4", "1", "20"),
            soil_extract("30"),
            artificial_seawater,
        ],
    )


def polytomella_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [water("915")],
        [
            single_stock("KNO3", "10", "10"),
            single_stock("(NH4)2HPO4", "2", "5"),
            single_stock("MgSO4 x 7 H2O", "1", "5"),
            saturated_caso4("10"),
            single_stock("Na-acetate", "100", "10"),
            single_stock("Yeast extract", "100", "5"),
            single_stock("Bacto-tryptone", "100", "5"),
            soil_extract("30"),
            micronutrient_1(),
        ],
    )


def malt_peptone_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [
            ingredient("Malt extract", "10.0", "G_PER_L"),
            ingredient("Proteose Peptone", "2.5", "G_PER_L"),
            water("1", "L"),
        ],
        [],
    )


def cyanidium_recipe() -> dict[str, Any]:
    recipe = liquid_recipe(
        [water("830")],
        [
            single_stock("(NH4)2SO4", "10", "100"),
            single_stock("K2HPO4", "1", "20"),
            single_stock("MgSO4 x 7 H2O", "1", "20"),
            soil_extract("30"),
        ],
        ph_range={"min": 4.0, "max": 4.0},
    )
    recipe["preparation_steps"].append(
        step(
            3,
            "MIX",
            "Vitamin B1, vitamin B12, and combined B1/B12 variants are described separately and are not asserted here.",
        )
    )
    return recipe


def dunaliella_acid_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [
            ingredient("MgSO4 x 7 H2O", "25.00", "G_PER_L"),
            ingredient(
                "NH4NO3",
                "0.25",
                "G_PER_L",
                notes="No defensible MediaIngredientMech SSSOM mapping was asserted.",
            ),
            ingredient("K2HPO4", "0.075", "G_PER_L"),
            ingredient("CaCl2 x 2 H2O", "0.012", "G_PER_L"),
            water("990"),
            vitamin_b12(notes="Add in sterile solution after autoclaving."),
        ],
        [soil_extract("5", peat=True), micronutrient_1()],
        steps=[
            step(1, "MIX", "Combine the salts, peat extract, micronutrients, and water."),
            step(2, "ADJUST_PH", "Adjust to pH 1.5-1.8 with 1 N H2SO4."),
            step(3, "AUTOCLAVE", "Autoclave following the SAG general guidance."),
            step(4, "COOL", "Cool and add vitamin B12 in sterile solution."),
        ],
        ph_range={"min": 1.5, "max": 1.8},
    )


def z_medium_recipe() -> dict[str, Any]:
    fe_edta = stock(
        "Z-medium Fe-EDTA complex",
        "10.0",
        [
            ingredient("FeCl2 x 6 H2O", "0.27", "G_PER_L"),
            ingredient(
                "Disodium EDTA",
                "0.372",
                "G_PER_L",
                notes="The source specifies the disodium salt without a hydration state.",
            ),
            water("1", "L"),
        ],
        notes=(
            "Calculated from 5 mL each of source primary stocks (27 and 37.2 g/L) made to 500 mL."
        ),
    )
    micronutrients = stock(
        "Z-medium micronutrient solution",
        "0.08",
        [
            ingredient("H3BO3", "3100", "MG_PER_L"),
            ingredient("MnSO4 x 4 H2O", "2230", "MG_PER_L"),
            ingredient("Na2WO4 x 2 H2O", "33", "MG_PER_L"),
            ingredient(
                "(NH4)6Mo7O24 x 4 H2O",
                "88",
                "MG_PER_L",
                mapping_key="ammonium molybdate tetrahydrate",
            ),
            ingredient("KBr", "119", "MG_PER_L"),
            ingredient(
                "KI",
                "83",
                "MG_PER_L",
                notes="The PDF prints KJ; interpreted as potassium iodide from the formula context.",
            ),
            ingredient("ZnSO4 x 7 H2O", "287", "MG_PER_L"),
            ingredient("Cd(NO3)2 x 4 H2O", "154", "MG_PER_L"),
            ingredient("Co(NO3)2 x 6 H2O", "146", "MG_PER_L"),
            ingredient("CuSO4 x 5 H2O", "125", "MG_PER_L"),
            ingredient(
                "NiSO4(NH4)2SO4 x 6 H2O",
                "198",
                "MG_PER_L",
                notes="No exact MediaIngredientMech SSSOM mapping was available.",
            ),
            ingredient("Cr(NO3)3 x 7 H2O", "37", "MG_PER_L"),
            ingredient("VOSO4 x 2 H2O", "20", "MG_PER_L"),
            ingredient(
                "Al2(SO4)3K2SO4 x 24 H2O",
                "474",
                "MG_PER_L",
                notes="No exact MediaIngredientMech SSSOM mapping was available.",
            ),
            water("1", "L"),
        ],
        notes="Source amounts per 100 mL were normalized to concentrations per litre.",
    )
    recipe = liquid_recipe(
        [
            ingredient("NaNO3", "467.0", "MG_PER_L"),
            ingredient("Ca(NO3)2 x 4 H2O", "59.0", "MG_PER_L"),
            ingredient("K2HPO4", "31.0", "MG_PER_L"),
            ingredient(
                "MgSO4 x 7 H2O",
                "25.0",
                "MG_PER_L",
                notes="The source prints H20; interpreted as the heptahydrate used throughout the SAG recipes.",
            ),
            ingredient("Na2CO3", "21.0", "MG_PER_L"),
            water("1", "L"),
        ],
        [fe_edta, micronutrients],
    )
    recipe["preparation_steps"].append(
        step(
            3,
            "MIX",
            "The nitrogen-free Z 45/4 variant is listed separately and is not asserted here.",
        )
    )
    return recipe


def chilomonas_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [
            ingredient("Na-acetate", "1", "G_PER_L"),
            ingredient("Beef extract", "1", "G_PER_L"),
            water("1", "L"),
        ],
        [],
        steps=[
            step(1, "MIX", "Dissolve sodium acetate and beef extract in 1 L water."),
            step(2, "AUTOCLAVE", "Autoclave following the SAG general preparation guidance."),
        ],
    )


def volvox_recipe() -> dict[str, Any]:
    micronutrients = stock(
        "Volvox micronutrient solution",
        "6",
        [
            ingredient(
                "Na2EDTA",
                "750",
                "MG_PER_L",
                notes="The source specifies disodium EDTA without a hydration state.",
            ),
            ingredient("FeCl3 x 6 H2O", "97", "MG_PER_L"),
            ingredient("MnCl2 x 4 H2O", "41", "MG_PER_L"),
            ingredient("ZnCl2", "5", "MG_PER_L"),
            ingredient("CoCl2 x 6 H2O", "2", "MG_PER_L", mapping_key="Cobalt chloride hexahydrate"),
            ingredient("Na2MoO4 x 2 H2O", "4", "MG_PER_L"),
            water("1", "L"),
        ],
        notes="Add salts in the order printed by the source.",
    )
    return liquid_recipe(
        [
            ingredient("Na2glycerophosphate x 5 H2O", "60", "MG_PER_L"),
            ingredient("Glycyl-glycine", "500", "MG_PER_L"),
            water("964"),
            vitamin_b12(),
            ingredient(
                "Thiamine", "0.5", "MG_PER_L", notes="Add in sterile solution after autoclaving."
            ),
        ],
        [
            single_stock("Ca(NO3)2 x 4 H2O", "118", "10"),
            single_stock("MgSO4 x 7 H2O", "40", "10"),
            single_stock("KCl", "50", "10"),
            micronutrients,
        ],
        steps=[
            step(1, "MIX", "Combine the stock solutions, direct ingredients, and water."),
            step(
                2,
                "ADJUST_PH",
                "Adjust to pH 7.0 or, for the source alternative, pH 8.0 with 1 N NaOH.",
            ),
            step(3, "AUTOCLAVE", "Autoclave following the SAG general guidance."),
            step(4, "COOL", "Cool and add sterile vitamin B12 and vitamin B1 solutions."),
        ],
        ph_range={"notes": "The source gives two alternatives: pH 7.0 or pH 8.0."},
    )


def f2_micronutrients() -> dict[str, Any]:
    return stock(
        "f/2 micronutrient working stock solution",
        "1",
        [
            ingredient("CuSO4 x 5 H2O", "9.8", "MG_PER_L"),
            ingredient("ZnSO4 x 7 H2O", "22", "MG_PER_L"),
            ingredient(
                "CoCl2 x 6 H2O", "10", "MG_PER_L", mapping_key="Cobalt chloride hexahydrate"
            ),
            ingredient("MnCl2 x 4 H2O", "180", "MG_PER_L"),
            ingredient("Na2MoO4 x 2 H2O", "6.3", "MG_PER_L"),
            ingredient(
                "Na2EDTA",
                "4.36",
                "G_PER_L",
                notes="The source specifies disodium EDTA without a hydration state.",
            ),
            ingredient("FeCl3 x 6 H2O", "3.15", "G_PER_L"),
            water("1", "L"),
        ],
        notes=(
            "Primary-stock additions were calculated into the 1 L working stock; "
            "the primary stock boundary is retained in this derivation note."
        ),
    )


def f2_vitamins() -> dict[str, Any]:
    return stock(
        "f/2 vitamin working stock solution",
        "1",
        [
            ingredient("Vitamin B12", "1", "MG_PER_L"),
            ingredient("Biotin", "1", "MG_PER_L"),
            ingredient("Thiamine HCl", "200", "MG_PER_L"),
            water("1", "L"),
        ],
        notes="Primary-stock additions were calculated into the 1 L working stock.",
    )


def enriched_seawater_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [ingredient("Filtered seawater", "1000", "ML_PER_L", mapping_key="Filtered Seawater")],
        [
            single_stock("NaNO3", "75", "1"),
            single_stock("NaH2PO4 x H2O", "5", "1"),
            f2_micronutrients(),
            f2_vitamins(),
        ],
        steps=[
            step(
                1,
                "MIX",
                "Add the nutrient, micronutrient, and vitamin stocks to filtered seawater.",
            ),
            step(
                2,
                "MIX",
                "For diatom culture, the source recommends 1 mL/L of a 30 g/L Na2SiO3 x 9 H2O stock.",
            ),
            step(3, "FILTER_STERILIZE", "Filter sterilize, or acidify slightly and autoclave."),
            step(4, "COOL", "If autoclaved, add the vitamin working stock after cooling."),
        ],
        sterilization={
            "method": "FILTER",
            "notes": "The source alternatively permits slight acidification followed by autoclaving.",
        },
    )


def wc_recipe() -> dict[str, Any]:
    micronutrients = stock(
        "WC micronutrient solution",
        "1",
        [
            ingredient(
                "Na2EDTA", "4.36", "G_PER_L", notes="Disodium EDTA; hydration state unspecified."
            ),
            ingredient("FeCl3 x 6 H2O", "3.15", "G_PER_L"),
            ingredient("CuSO4 x 5 H2O", "0.01", "G_PER_L"),
            ingredient("ZnSO4 x 7 H2O", "0.022", "G_PER_L"),
            ingredient(
                "CoCl2 x 6 H2O", "0.01", "G_PER_L", mapping_key="Cobalt chloride hexahydrate"
            ),
            ingredient("MnCl2 x 4 H2O", "0.18", "G_PER_L"),
            ingredient("Na2MoO4 x 2 H2O", "0.006", "G_PER_L"),
            ingredient("H3BO3", "1", "G_PER_L"),
            water("1", "L"),
        ],
    )
    vitamins = stock(
        "WC vitamin solution",
        "1",
        [
            ingredient("Thiamine HCl", "0.1", "G_PER_L"),
            ingredient("Biotin", "0.0005", "G_PER_L"),
            water("1", "L"),
        ],
    )
    return liquid_recipe(
        [ingredient("TES", "0.115", "G_PER_L"), water("1", "L")],
        [
            single_stock("CaCl2 x 2 H2O", "36.8", "1"),
            single_stock("MgSO4 x 7 H2O", "37", "1"),
            single_stock(
                "NaHCO3",
                "12.6",
                "1",
                notes="The PDF prints 'NaH CO3'; interpreted as sodium hydrogencarbonate.",
            ),
            single_stock("K2HPO4 x 3 H2O", "11.4", "1"),
            single_stock("NaNO3", "85", "1"),
            single_stock("Na2SiO3 x 9 H2O", "21.2", "1"),
            micronutrients,
            vitamins,
        ],
    )


def piv_metal_solution(use_ml_per_l: str = "6") -> dict[str, Any]:
    return stock(
        "PIV metal solution",
        use_ml_per_l,
        [
            ingredient(
                "Na2EDTA", "750", "MG_PER_L", notes="Disodium EDTA; hydration state unspecified."
            ),
            ingredient("FeCl3 x 6 H2O", "97", "MG_PER_L"),
            ingredient("MnCl2 x 4 H2O", "41", "MG_PER_L"),
            ingredient("ZnCl2", "5", "MG_PER_L"),
            ingredient("CoCl2 x 6 H2O", "2", "MG_PER_L", mapping_key="Cobalt chloride hexahydrate"),
            ingredient("Na2MoO4 x 2 H2O", "4", "MG_PER_L"),
            water("1", "L"),
        ],
        notes="Dissolve EDTA fully, then add salts in the source order.",
    )


def artificial_seawater_recipe() -> dict[str, Any]:
    trace = stock(
        "ASM trace element solution",
        "6",
        [
            ingredient("EDTA", "750", "MG_PER_L"),
            ingredient("FeCl3 x 6 H2O", "97", "MG_PER_L"),
            ingredient("MnCl2 x 4 H2O", "41", "MG_PER_L"),
            ingredient("ZnCl2", "5", "MG_PER_L"),
            ingredient("CoCl2 x 6 H2O", "2", "MG_PER_L", mapping_key="Cobalt chloride hexahydrate"),
            ingredient(
                "NaMoO4 x 2 H2O",
                "4",
                "MG_PER_L",
                notes="Source formula retained; no exact SSSOM mapping was asserted.",
            ),
            water("1", "L"),
        ],
        notes="Add salts in the printed order.",
    )
    b12 = stock(
        "ASM vitamin B12 working stock",
        "0.5",
        [ingredient("Vitamin B12", "10", "MG_PER_L"), water("1", "L")],
        notes="Calculated from the source two-step dilution: 100 mg/100 mL, then 1:100.",
    )
    b1 = stock(
        "ASM vitamin B1 stock",
        "0.5",
        [ingredient("Thiamine", "1.2", "G_PER_L"), water("1", "L")],
    )
    return liquid_recipe(
        [
            ingredient("NaCl", "30", "G_PER_L"),
            ingredient(
                "TRIS",
                "1",
                "G_PER_L",
                notes="No exact MediaIngredientMech SSSOM mapping was available.",
            ),
            water("944"),
        ],
        [
            single_stock("MgSO4 x 7 H2O", "244", "10"),
            single_stock("KCl", "60", "10"),
            single_stock("NaNO3", "100", "10"),
            single_stock("CaCl2 x 2 H2O", "30", "10"),
            single_stock("KH2PO4", "5", "10"),
            trace,
            b12,
            b1,
        ],
        steps=[
            step(
                1, "MIX", "Dissolve NaCl and TRIS in water, then add the mineral and trace stocks."
            ),
            step(2, "ADJUST_PH", "Adjust to pH 8.0 with 1 N HCl."),
            step(3, "AUTOCLAVE", "Autoclave the base medium."),
            step(4, "COOL", "Cool and add sterile vitamin B12 and vitamin B1 stocks."),
            step(
                5,
                "MIX",
                "For half-strength ASM15 use 15 g/L NaCl; agar at 15 g/L is an optional solid variant.",
            ),
        ],
        ph_range={"min": 8.0, "max": 8.0},
    )


def bold_modified_basal_recipe() -> dict[str, Any]:
    return liquid_recipe(
        [water("940")],
        [
            single_stock("NaNO3", "25", "10", notes="Source stock is 10 g in 400 mL."),
            single_stock("CaCl2 x 2 H2O", "2.5", "10", notes="Source stock is 1 g in 400 mL."),
            single_stock("MgSO4 x 7 H2O", "7.5", "10", notes="Source stock is 3 g in 400 mL."),
            single_stock("K2HPO4 x 3 H2O", "7.5", "10", notes="Source stock is 3 g in 400 mL."),
            single_stock("KH2PO4", "17.5", "10", notes="Source stock is 7 g in 400 mL."),
            single_stock("NaCl", "2.5", "10", notes="Source stock is 1 g in 400 mL."),
            single_stock("Thiamine", "1", "1"),
            single_stock("Biotin", "0.25", "1", stock_unit="MG_PER_L"),
            single_stock("Vitamin B12", "0.15", "1", stock_unit="MG_PER_L"),
            piv_metal_solution(),
        ],
        steps=[
            step(1, "MIX", "Add six 10 mL mineral-stock portions to 940 mL water."),
            step(2, "AUTOCLAVE", "Autoclave the mineral base."),
            step(3, "COOL", "Add filter-sterilized vitamin and PIV metal solutions after cooling."),
            step(4, "MIX", "The 3NBBM+V variant uses 30 rather than 10 mL/L NaNO3 stock."),
        ],
        ph_range={"min": 6.4, "max": 6.4},
    )


def wees_recipe() -> dict[str, Any]:
    pii = stock(
        "WEES PII metal mix without Fe",
        "1",
        [
            ingredient("EDTA", "3", "G_PER_L"),
            ingredient("H3BO3", "1.14", "G_PER_L"),
            ingredient("MnCl2 x 4 H2O", "144", "MG_PER_L"),
            ingredient("ZnSO4 x 7 H2O", "21", "MG_PER_L"),
            ingredient("CoCl2 x 6 H2O", "4", "MG_PER_L", mapping_key="Cobalt chloride hexahydrate"),
            water("1", "L"),
        ],
        notes="Source amounts per 100 mL were normalized to concentrations per litre.",
    )
    fe_edta = stock(
        "WEES Fe-EDTA solution",
        "1",
        [
            ingredient("EDTA", "5.2", "G_PER_L"),
            ingredient("FeSO4 x 7 H2O", "5", "G_PER_L"),
            ingredient(
                "1 N KOH",
                "54",
                "ML_PER_L",
                mapping_key="KOH",
                notes="Equivalent to 5.4 mL per source 100 mL stock batch.",
            ),
            water("1", "L"),
        ],
    )
    vitamins = stock(
        "WEES vitamin stock solution",
        "1",
        [
            ingredient("Vitamin B12", "0.2", "MG_PER_L"),
            ingredient("Biotin", "1.0", "MG_PER_L"),
            ingredient("Thiamine HCl", "100", "MG_PER_L"),
            ingredient("Nicotinamide", "0.1", "MG_PER_L"),
            water("1", "L"),
        ],
    )
    source_soil = stock(
        "WEES soil extract",
        "100",
        [
            ingredient("Garden soil", "100", "G_PER_L"),
            water("1", "L"),
        ],
        notes=(
            "Boil 10 g soil with 125 mL water for 5 minutes, filter and centrifuge, "
            "then make the extract to 100 mL."
        ),
    )
    return liquid_recipe(
        [water("1", "L", notes="Prepare the final formulation per litre of water as printed.")],
        [
            single_stock("KNO3", "100", "1"),
            single_stock("MgSO4 x 7 H2O", "20", "1"),
            single_stock("(NH4)2HPO4", "20", "1"),
            saturated_caso4("1"),
            pii,
            fe_edta,
            vitamins,
            source_soil,
        ],
        steps=[
            step(1, "MIX", "Add each stock and the soil extract at the stated amount."),
            step(2, "ADJUST_PH", "Adjust to pH 5.4-6.0 with 0.1 N HCl."),
            step(3, "AUTOCLAVE", "Autoclave at 121 C for 30 minutes."),
        ],
        ph_range={"min": 5.4, "max": 6.0},
        sterilization={"method": "AUTOCLAVE", "duration": "30 minutes"},
    )


def pes_recipe() -> dict[str, Any]:
    enrichment = stock(
        "PES ES-enrichment solution",
        "20",
        [
            ingredient("NaNO3", "3500", "MG_PER_L"),
            ingredient("Na2glycerophosphate x 5 H2O", "500", "MG_PER_L"),
            ingredient("Fe(NH4)2(SO4)2 x 6 H2O", "175.5", "MG_PER_L"),
            ingredient(
                "Na2EDTA",
                "400",
                "MG_PER_L",
                notes=(
                    "Calculated as 150 mg/L from the Fe solution plus 250 mg/L "
                    "from the PII metal solution; hydration state unspecified."
                ),
            ),
            ingredient("H3BO3", "285", "MG_PER_L"),
            ingredient("FeCl3 x 6 H2O", "12.25", "MG_PER_L"),
            ingredient("MnSO4 x H2O", "41", "MG_PER_L"),
            ingredient("ZnSO4 x 7 H2O", "5.5", "MG_PER_L"),
            ingredient("CoSO4 x 7 H2O", "1.2", "MG_PER_L"),
            ingredient("Vitamin B12", "0.1", "MG_PER_L"),
            ingredient("Thiamine", "5", "MG_PER_L"),
            ingredient("Biotin", "0.05", "MG_PER_L"),
            ingredient(
                "TRIS",
                "5",
                "G_PER_L",
                notes="No exact MediaIngredientMech SSSOM mapping was available.",
            ),
            water("1", "L"),
        ],
        notes=(
            "Source amounts per 100 mL were normalized to the enrichment stock. "
            "Fe-solution and PII-solution contributions were calculated into this "
            "one LinkML composition level while retaining their origins in notes. "
            "Adjust this stock to pH 7.8, dispense 20 mL portions, and autoclave."
        ),
    )
    return liquid_recipe(
        [
            ingredient(
                "Pasteurized, filtered seawater",
                "1000",
                "ML_PER_L",
                mapping_key="Pasteurized Seawater",
            )
        ],
        [enrichment],
        steps=[
            step(
                1, "AUTOCLAVE", "Prepare, adjust, dispense, and autoclave the ES-enrichment stock."
            ),
            step(
                2,
                "MIX",
                "Add one 20 mL tube of ES-enrichment to 1000 mL pasteurized, filtered seawater.",
            ),
            step(3, "STORE", "Store ES-enrichment stock at 10 C."),
        ],
        sterilization={
            "method": "NONE",
            "notes": "The enrichment stock is autoclaved separately; the seawater is pasteurized.",
        },
    )


def bold_modified_basal_tom_recipe() -> dict[str, Any]:
    trace_i = stock(
        "MBB trace element stock I",
        "1",
        [ingredient("KOH", "30", "G_PER_L"), ingredient("EDTA", "50", "G_PER_L"), water("1", "L")],
    )
    trace_ii = stock(
        "MBB trace element stock II",
        "1",
        [ingredient("FeSO4 x 7 H2O", "4.98", "G_PER_L"), water("1", "L")],
        notes="The source specifies dissolving with sulfuric acid but gives no amount.",
    )
    trace_iii = stock(
        "MBB trace element stock III",
        "1",
        [ingredient("H3BO3", "11.04", "G_PER_L"), water("1", "L")],
    )
    trace_iv = stock(
        "MBB trace element stock IV",
        "1",
        [
            ingredient("ZnSO4 x 7 H2O", "17.64", "G_PER_L"),
            ingredient("MnCl2 x 4 H2O", "1.44", "G_PER_L"),
            ingredient(
                "NaMoO4",
                "0.72",
                "G_PER_L",
                notes="Source formula retained; no exact SSSOM mapping was asserted.",
            ),
            ingredient("CuSO4 x 5 H2O", "1.58", "G_PER_L"),
            ingredient("Co(NO3)2 x 6 H2O", "0.50", "G_PER_L"),
            water("1", "L"),
        ],
        notes="The source specifies dissolving with sulfuric acid but gives no amount.",
    )
    return liquid_recipe(
        [
            ingredient("HEPES", "0.715", "G_PER_L"),
            ingredient("Glucose", "15", "G_PER_L"),
            ingredient("Proteose Peptone", "20", "G_PER_L"),
            water("1", "L", notes="Make the MBB base to 1 L before TOM supplementation."),
        ],
        [
            single_stock("NaCl", "2.5", "10", notes="Source stock is 1.25 g in 500 mL."),
            single_stock("CaCl2 x 2 H2O", "2.5", "10", notes="Source stock is 1.25 g in 500 mL."),
            single_stock("KNO3", "50", "10", notes="Source stock is 25 g in 500 mL."),
            single_stock("MgSO4 x 7 H2O", "6.5", "10", notes="Source stock is 3.25 g in 500 mL."),
            single_stock("(NH4)2HPO4", "25", "10", notes="Source stock is 12.5 g in 500 mL."),
            trace_i,
            trace_ii,
            trace_iii,
            trace_iv,
        ],
        steps=[
            step(
                1,
                "MIX",
                "Add 10 mL of each mineral stock and 1 mL of each trace stock; make to 1 L.",
            ),
            step(2, "MIX", "Add 0.715 g HEPES, 1.5% glucose, and 2% proteose peptone for TOM."),
            step(3, "ADJUST_PH", "Adjust TOM to pH 7.1."),
            step(
                4,
                "MIX",
                "The PDF lists a vitamin stock but gives no unambiguous final addition rate, so it is not asserted.",
            ),
            step(5, "AUTOCLAVE", "Autoclave following the SAG general preparation guidance."),
        ],
        ph_range={"min": 7.1, "max": 7.1},
    )


RECIPES: dict[str, dict[str, Any]] = {
    "artificial_seawater": artificial_seawater_recipe(),
    "bacillariophycean": bacillariophycean_recipe(),
    "basal": basal_recipe(),
    "beggiatoa": beggiatoa_recipe(),
    "bold_modified_basal": bold_modified_basal_recipe(),
    "bold_modified_basal_tom": bold_modified_basal_tom_recipe(),
    "brackish": brackish_recipe(),
    "chilomonas": chilomonas_recipe(),
    "cyanidium": cyanidium_recipe(),
    "desmidiacean": desmidiacean_recipe(),
    "dunaliella": dunaliella_recipe(),
    "dunaliella_acid": dunaliella_acid_recipe(),
    "enriched_seawater": enriched_seawater_recipe(),
    "euglena": euglena_recipe(),
    "malt_peptone": malt_peptone_recipe(),
    "soil_water_note": soil_water_note_recipe(),
    "ochromonas": ochromonas_recipe(),
    "pes": pes_recipe(),
    "polytoma": polytoma_recipe(),
    "polytomella": polytomella_recipe(),
    "porphyridium": porphyridium_recipe(),
    "seawater": seawater_recipe(),
    "soil_water": soil_water_recipe(),
    "spirulina": spirulina_recipe(),
    "unicellular_green": unicellular_green_recipe(),
    "volvox": volvox_recipe(),
    "wees": wees_recipe(),
    "wc": wc_recipe(),
    "z_medium": z_medium_recipe(),
}


RECIPE_FIELDS = (
    "ingredients",
    "solutions",
    "preparation_steps",
    "ph_range",
    "physical_state",
    "sterilization",
    "parent_media",
    "variant_children",
    "variant_relationship",
    "variant_modifications",
)
COMPONENT_FIELDS = (
    "preferred_term",
    "term",
    "mediaingredientmech_chebi_term",
    "concentration",
    "notes",
    "preparation_notes",
)


def component_projection(row: dict[str, Any]) -> dict[str, Any]:
    projected = {key: copy.deepcopy(row[key]) for key in COMPONENT_FIELDS if key in row}
    if "composition" in row:
        projected["composition"] = [
            component_projection(component) for component in row.get("composition") or []
        ]
    return projected


def recipe_projection(doc: dict[str, Any]) -> dict[str, Any]:
    projected: dict[str, Any] = {}
    for field in RECIPE_FIELDS:
        if field not in doc:
            continue
        if field in {"ingredients", "solutions"}:
            projected[field] = [component_projection(row) for row in doc.get(field) or []]
        else:
            projected[field] = copy.deepcopy(doc[field])
    return projected


def source_note(target: Target) -> str:
    source = SOURCES[target.source_key]
    return f"Composition verified against {source.url} on 2026-08-25 (SHA-256 {source.sha256})."


def history_has_action(doc: dict[str, Any]) -> bool:
    return any(
        isinstance(row, dict) and row.get("action") == ACTION
        for row in doc.get("curation_history") or []
    )


def validate_source_files(source_dir: Path) -> None:
    for source in SOURCES.values():
        path = source_dir / source.file_name
        if not path.is_file():
            raise ValueError(f"missing reviewed SAG source file: {path}")
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != source.sha256:
            raise ValueError(f"{path}: SHA-256 {actual_hash}, expected reviewed {source.sha256}")


def validate_mim_terms(sssom_path: Path) -> None:
    if not sssom_path.is_file():
        raise ValueError(f"missing MediaIngredientMech SSSOM: {sssom_path}")
    with sssom_path.open(encoding="utf-8", newline="") as handle:
        rows = csv.DictReader((line for line in handle if not line.startswith("#")), delimiter="\t")
        objects = {
            (str(row.get("object_id") or ""), str(row.get("object_label") or "")) for row in rows
        }
    missing = sorted(set(MIM_TERMS.values()) - objects)
    if missing:
        rendered = ", ".join(f"{curie} ({label})" for curie, label in missing)
        raise ValueError(f"selected mappings are absent from the MIM SSSOM: {rendered}")


def _validate_precondition(doc: dict[str, Any], target: Target) -> None:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(
            f"{target.relative_path}: id {doc.get('id')!r}, expected {target.record_id}"
        )
    if doc.get("ingredients") or doc.get("solutions"):
        raise ValueError(f"{target.relative_path}: record is no longer composition-empty")
    if "incomplete_composition" not in (doc.get("data_quality_flags") or []):
        raise ValueError(f"{target.relative_path}: missing incomplete_composition flag")


def _assert_applied(doc: dict[str, Any], target: Target) -> None:
    expected = recipe_projection(RECIPES[target.recipe_key])
    if recipe_projection(doc) != expected:
        raise ValueError(f"{target.relative_path}: applied SAG recipe drifted")
    flags = doc.get("data_quality_flags") or []
    if "incomplete_composition" in flags:
        raise ValueError(f"{target.relative_path}: incomplete flag returned")
    if source_note(target) not in str(doc.get("notes") or ""):
        raise ValueError(f"{target.relative_path}: source verification note is missing")


def repair_document(doc: dict[str, Any], target: Target) -> tuple[dict[str, Any], bool]:
    if history_has_action(doc):
        _assert_applied(doc, target)
        return doc, False
    _validate_precondition(doc, target)

    repaired = copy.deepcopy(doc)
    recipe = RECIPES[target.recipe_key]
    for field in RECIPE_FIELDS:
        if field in recipe:
            repaired[field] = copy.deepcopy(recipe[field])
        else:
            repaired.pop(field, None)

    flags = repaired.get("data_quality_flags") or []
    if not isinstance(flags, list):
        raise ValueError(f"{target.relative_path}: data_quality_flags is not a list")
    kept_flags = [
        flag
        for flag in flags
        if flag not in {"incomplete_composition", "source_information_unavailable"}
    ]
    if kept_flags:
        repaired["data_quality_flags"] = kept_flags
    else:
        repaired.pop("data_quality_flags", None)

    note = source_note(target)
    existing_notes = str(repaired.get("notes") or "").rstrip()
    repaired["notes"] = f"{existing_notes}\n{note}" if existing_notes else note

    history = repaired.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.relative_path}: curation_history is not a list")
    history.append(
        {
            "timestamp": TIMESTAMP,
            "curator": "repair_sag_missing_compositions.py",
            "action": ACTION,
            "changes": (
                f"ingredients {len(doc.get('ingredients') or [])} -> "
                f"{len(recipe.get('ingredients') or [])}; solutions "
                f"{len(doc.get('solutions') or [])} -> {len(recipe.get('solutions') or [])}"
            ),
            "notes": (
                "Restored the formulation from the reviewed SAG PDF, preserving "
                "final-medium and stock-solution boundaries. Calculated stock "
                "concentrations are documented in-place. Ingredient identities "
                "were selected from the MediaIngredientMech SSSOM."
            ),
        }
    )
    _assert_applied(repaired, target)
    return repaired, True


def _validate_inventory() -> None:
    paths = [target.relative_path for target in TARGETS]
    ids = [target.record_id for target in TARGETS]
    recipe_keys = [target.recipe_key for target in TARGETS]
    source_keys = [target.source_key for target in TARGETS]
    if len(TARGETS) != 29 or len(SOURCES) != 29 or len(RECIPES) != 29:
        raise ValueError("SAG inventory must contain 29 targets, sources, and recipes")
    if len(paths) != len(set(paths)) or len(ids) != len(set(ids)):
        raise ValueError("SAG target paths and ids must be unique")
    if set(recipe_keys) != set(RECIPES) or set(source_keys) != set(SOURCES):
        raise ValueError("SAG targets do not cover the recipe and source inventories")
    for key, recipe in RECIPES.items():
        if not recipe.get("ingredients") and not recipe.get("solutions"):
            raise ValueError(f"{key}: recipe has no usable composition")
        for row in recipe.get("ingredients") or []:
            if not row.get("preferred_term") or not row.get("concentration"):
                raise ValueError(f"{key}: malformed direct ingredient")
        for row in recipe.get("solutions") or []:
            if (
                not row.get("preferred_term")
                or not row.get("concentration")
                or not row.get("composition")
            ):
                raise ValueError(f"{key}: malformed stock solution")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--source-dir", type=Path)
    parser.add_argument(
        "--sssom",
        type=Path,
        default=MIM_SSSOM,
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    _validate_inventory()
    if args.source_dir is not None:
        validate_source_files(args.source_dir)
    elif args.apply:
        raise ValueError("--apply requires --source-dir with the reviewed SAG PDFs")
    validate_mim_terms(args.sssom)

    pending = []
    for target in TARGETS:
        path = args.normalized_dir / target.relative_path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict):
            raise ValueError(f"{path}: expected a YAML mapping")
        repaired, changed = repair_document(doc, target)
        pending.append((path, repaired, changed, target))
        print(f"{'fix' if changed else 'skip':4s}  {target.relative_path}: SAG {target.source_key}")

    changed_count = sum(changed for _, _, changed, _ in pending)
    if args.apply:
        for path, repaired, changed, _ in pending:
            if changed:
                write_record(path, repaired)
    verb = "updated" if args.apply else "would update"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
