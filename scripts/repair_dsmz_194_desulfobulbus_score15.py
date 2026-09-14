#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 194 Desulfobulbus variants."""

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

DSMZ_194 = "bacterial/desulfobulbus_sp_medium_freshwater.yaml"
DSMZ_194A = "bacterial/desulfovirga_medium.yaml"
KOMODO_194 = "bacterial/KOMODO_194_DESULFOBULBUS_MEDIUM.yaml"
KOMODO_194_1 = "bacterial/for_dsm_1744.yaml"
KOMODO_194_2 = "bacterial/for_dsm_14880.yaml"
KOMODO_194_3 = "bacterial/for_dsm_21556.yaml"
KOMODO_194_13527 = "bacterial/medium_194_modified_for_dsm_13527.yaml"
KOMODO_194_5092 = "bacterial/medium_194_modified_for_dsm_5092.yaml"
KOMODO_194_6523 = "bacterial/medium_194_modified_for_dsm_6523.yaml"

EXPECTED_IDS = {
    DSMZ_194: "CultureMech:001288",
    DSMZ_194A: "CultureMech:001289",
    KOMODO_194: "CultureMech:004235",
    KOMODO_194_1: "CultureMech:004230",
    KOMODO_194_2: "CultureMech:004231",
    KOMODO_194_3: "CultureMech:004232",
    KOMODO_194_13527: "CultureMech:004229",
    KOMODO_194_5092: "CultureMech:004233",
    KOMODO_194_6523: "CultureMech:004234",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_194: "mediadive.medium:194",
    DSMZ_194A: "mediadive.medium:194a",
    KOMODO_194: "komodo.medium:194",
    KOMODO_194_1: "komodo.medium:194.1",
    KOMODO_194_2: "komodo.medium:194.2",
    KOMODO_194_3: "komodo.medium:194.3",
    KOMODO_194_13527: "komodo.medium:194_13527",
    KOMODO_194_5092: "komodo.medium:194_5092",
    KOMODO_194_6523: "komodo.medium:194_6523",
}

DSMZ_194_REST = "https://mediadive.dsmz.de/rest/medium/194"
DSMZ_194_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium194.pdf"
DSMZ_194A_REST = "https://mediadive.dsmz.de/rest/medium/194a"
DSMZ_194A_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium194a.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

SOURCE_KOMODO_194 = "KOMODO Medium 194"
SOURCE_DSMZ_194 = "DSMZ Medium 194"

CURATOR = "repair_dsmz_194_desulfobulbus_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_194_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
DATA_QUALITY_FLAGS = ["ingredients_curated", "has_ontology_mappings"]
PH_RANGE = {"min": 7.1, "max": 7.4}


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    term: tuple[str, str]
    source: str
    notes: str


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    record_notes: str
    curation_notes: str
    composition_type: str
    components: tuple[Component, ...] | None = None
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()
    extra_references: tuple[str, ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    identifier: str,
    label: str,
    source: str,
    notes: str,
) -> Component:
    return Component(preferred_term, value, (identifier, label), source, notes)


def _ingredient(component: Component) -> dict[str, Any]:
    term = _term(*component.term)
    row: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": "G_PER_L"},
        "term": term,
    }
    if component.term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _komodo_note(source: str, preferred_term: str, value: str) -> str:
    return f"{source} lists {value} g/L {preferred_term} in the final-component table."


def _dsmz_note(preferred_term: str, value: str, dsm: str) -> str:
    return (
        f"DSMZ Medium 194 specifies {value} g/L {preferred_term} for {dsm} "
        "as a replacement for sodium propionate."
    )


def _komodo_component(
    source: str,
    preferred_term: str,
    value: str,
    identifier: str,
    label: str,
) -> Component:
    return _component(
        preferred_term,
        value,
        identifier,
        label,
        source,
        _komodo_note(source, preferred_term, value),
    )


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


def _base_components(source: str = SOURCE_KOMODO_194) -> tuple[Component, ...]:
    return (
        _komodo_component(source, "Na2SO4", "3.00", "CHEBI:32149", "sodium sulfate"),
        _komodo_component(
            source, "KH2PO4", "0.20", "CHEBI:63036", "potassium dihydrogen phosphate"
        ),
        _komodo_component(source, "NH4Cl", "0.30", "CHEBI:31206", "ammonium chloride"),
        _komodo_component(source, "NaCl", "1.00", "CHEBI:26710", "sodium chloride"),
        _komodo_component(
            source, "MgCl2 x 6 H2O", "0.40", "CHEBI:86345", "magnesium dichloride hexahydrate"
        ),
        _komodo_component(source, "KCl", "0.50", "CHEBI:32588", "potassium chloride"),
        _komodo_component(
            source, "CaCl2 x 2 H2O", "0.15", "CHEBI:86158", "calcium chloride dihydrate"
        ),
        _komodo_component(source, "Resazurin", "0.000999", "CHEBI:8806", "Resazurin"),
        _komodo_component(source, "NaHCO3", "5.00", "CHEBI:32139", "sodium hydrogencarbonate"),
        _komodo_component(source, "Sodium propionate", "1.50", "CHEBI:132106", "sodium propionate"),
        _komodo_component(
            source, "Na2S x 9 H2O", "0.40", "CHEBI:76209", "sodium sulfide nonahydrate"
        ),
        _komodo_component(source, "HCl", "0.000671", "CHEBI:17883", "hydrogen chloride"),
        _komodo_component(
            source, "FeCl2 x 4 H2O", "0.00149", "CHEBI:86249", "iron dichloride tetrahydrate"
        ),
        _komodo_component(source, "ZnCl2", "0.0000698", "CHEBI:49976", "zinc dichloride"),
        _komodo_component(
            source,
            "MnCl2 x 4 H2O",
            "0.0000997",
            "CHEBI:86368",
            "manganese(II) chloride tetrahydrate",
        ),
        _komodo_component(source, "H3BO3", "0.00000598", "CHEBI:33118", "boric acid"),
        _komodo_component(
            source, "CoCl2 x 6 H2O", "0.000189", "CHEBI:53503", "cobalt chloride hexahydrate"
        ),
        _komodo_component(
            source, "CuCl2 x 2 H2O", "0.00000199", "CHEBI:86318", "copper(II) chloride dihydrate"
        ),
        _komodo_component(
            source, "NiCl2 x 6 H2O", "0.0000239", "CHEBI:53542", "nickel chloride hexahydrate"
        ),
        _komodo_component(
            source, "Na2MoO4 x 2 H2O", "0.0000359", "CHEBI:75213", "sodium molybdate dihydrate"
        ),
        _komodo_component(source, "Folic acid", "0.0000200", "CHEBI:27470", "folic acid"),
        _komodo_component(source, "Biotin", "0.0000200", "CHEBI:15956", "biotin"),
        _komodo_component(
            source, "Pyridoxine HCl", "0.0000999", "CHEBI:30961", "pyridoxine hydrochloride"
        ),
        _komodo_component(
            source,
            "Thiamine-HCl x 2 H2O",
            "0.0000500",
            "CHEBI:132751",
            "thiamine hydrochloride dihydrate",
        ),
        _komodo_component(source, "Riboflavin", "0.0000500", "CHEBI:17015", "riboflavin"),
        _komodo_component(source, "Nicotinic acid", "0.0000500", "CHEBI:15940", "nicotinic acid"),
        _komodo_component(
            source, "D-Ca-pantothenate", "0.0000500", "CHEBI:31345", "Calcium pantothenate"
        ),
        _komodo_component(source, "Vitamin B12", "0.000000999", "CHEBI:176843", "vitamin B12"),
        _komodo_component(
            source, "p-Aminobenzoic acid", "0.0000500", "CHEBI:30753", "4-aminobenzoic acid"
        ),
        _komodo_component(source, "Lipoic acid", "0.0000500", "CHEBI:16494", "lipoic acid"),
    )


def _without_propionate(components: tuple[Component, ...]) -> tuple[Component, ...]:
    return tuple(row for row in components if row.preferred_term != "Sodium propionate")


BASE_COMPONENTS = _base_components()

KOMODO_194_1_COMPONENTS = (
    *(
        row
        for row in _without_propionate(_base_components("KOMODO Medium 194.1"))
        if row.preferred_term != "NaCl"
    ),
    _komodo_component("KOMODO Medium 194.1", "NaCl", "11.00", "CHEBI:26710", "sodium chloride"),
    _komodo_component(
        "KOMODO Medium 194.1", "Yeast extract", "1.00", "FOODON:03315426", "yeast extract"
    ),
    _komodo_component(
        "KOMODO Medium 194.1", "Sodium lactate", "2.50", "CHEBI:75228", "sodium lactate"
    ),
)

KOMODO_194_2_COMPONENTS = (
    *_without_propionate(_base_components("KOMODO Medium 194.2")),
    _component(
        "Yeast extract",
        "0.50",
        "FOODON:03315426",
        "yeast extract",
        SOURCE_DSMZ_194,
        "DSMZ Medium 194 specifies 0.50 g/L yeast extract for DSM 14880.",
    ),
    _component(
        "Sodium pyruvate",
        "2.20",
        "CHEBI:50144",
        "sodium pyruvate",
        SOURCE_DSMZ_194,
        "DSMZ Medium 194 specifies 2.20 g/L sodium pyruvate for DSM 14880.",
    ),
)

KOMODO_194_3_COMPONENTS = (
    *_without_propionate(_base_components("KOMODO Medium 194.3")),
    _component(
        "Na-butyrate",
        "1.00",
        "CHEBI:64103",
        "sodium butyrate",
        SOURCE_DSMZ_194,
        _dsmz_note("Na-butyrate", "1.00", "DSM 21556"),
    ),
)

KOMODO_194_13527_COMPONENTS = (
    *(
        row
        for row in _without_propionate(_base_components("KOMODO Medium 194_13527"))
        if row.preferred_term != "NaHCO3"
    ),
    _komodo_component(
        "KOMODO Medium 194_13527", "NaHCO3", "2.50", "CHEBI:32139", "sodium hydrogencarbonate"
    ),
    _component(
        "Na-butyrate",
        "1.00",
        "CHEBI:64103",
        "sodium butyrate",
        SOURCE_DSMZ_194,
        _dsmz_note("Na-butyrate", "1.00", "DSM 13527"),
    ),
)

KOMODO_194_5092_COMPONENTS = (
    *_without_propionate(_base_components("KOMODO Medium 194_5092")),
    _component(
        "putrescine",
        "0.90",
        "CHEBI:17148",
        "putrescine",
        SOURCE_DSMZ_194,
        _dsmz_note("putrescine", "0.90", "DSM 5092"),
    ),
)

KOMODO_194_6523_COMPONENTS = (
    _komodo_component("KOMODO Medium 194_6523", "Na2SO4", "2.72", "CHEBI:32149", "sodium sulfate"),
    _komodo_component(
        "KOMODO Medium 194_6523", "KH2PO4", "0.18", "CHEBI:63036", "potassium dihydrogen phosphate"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "NH4Cl", "0.27", "CHEBI:31206", "ammonium chloride"
    ),
    _komodo_component("KOMODO Medium 194_6523", "NaCl", "0.91", "CHEBI:26710", "sodium chloride"),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "MgCl2 x 6 H2O",
        "0.36",
        "CHEBI:86345",
        "magnesium dichloride hexahydrate",
    ),
    _komodo_component("KOMODO Medium 194_6523", "KCl", "0.45", "CHEBI:32588", "potassium chloride"),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "CaCl2 x 2 H2O",
        "0.14",
        "CHEBI:86158",
        "calcium chloride dihydrate",
    ),
    _komodo_component("KOMODO Medium 194_6523", "Resazurin", "0.000908", "CHEBI:8806", "Resazurin"),
    _komodo_component(
        "KOMODO Medium 194_6523", "NaHCO3", "4.54", "CHEBI:32139", "sodium hydrogencarbonate"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "Sodium propionate", "1.36", "CHEBI:132106", "sodium propionate"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "Na2S x 9 H2O",
        "0.36",
        "CHEBI:76209",
        "sodium sulfide nonahydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "HCl", "0.000610", "CHEBI:17883", "hydrogen chloride"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "FeCl2 x 4 H2O",
        "0.00136",
        "CHEBI:86249",
        "iron dichloride tetrahydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "ZnCl2", "0.0000634", "CHEBI:49976", "zinc dichloride"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "MnCl2 x 4 H2O",
        "0.0000906",
        "CHEBI:86368",
        "manganese(II) chloride tetrahydrate",
    ),
    _komodo_component("KOMODO Medium 194_6523", "H3BO3", "0.00000544", "CHEBI:33118", "boric acid"),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "CoCl2 x 6 H2O",
        "0.000172",
        "CHEBI:53503",
        "cobalt chloride hexahydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "CuCl2 x 2 H2O",
        "0.00000181",
        "CHEBI:86318",
        "copper(II) chloride dihydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "NiCl2 x 6 H2O",
        "0.0000217",
        "CHEBI:53542",
        "nickel chloride hexahydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "Na2MoO4 x 2 H2O",
        "0.0000326",
        "CHEBI:75213",
        "sodium molybdate dihydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "Folic acid", "0.0000182", "CHEBI:27470", "folic acid"
    ),
    _komodo_component("KOMODO Medium 194_6523", "Biotin", "0.0000182", "CHEBI:15956", "biotin"),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "Pyridoxine HCl",
        "0.0000908",
        "CHEBI:30961",
        "pyridoxine hydrochloride",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "Thiamine-HCl x 2 H2O",
        "0.0000454",
        "CHEBI:132751",
        "thiamine hydrochloride dihydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "Riboflavin", "0.0000454", "CHEBI:17015", "riboflavin"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "Nicotinic acid", "0.0000454", "CHEBI:15940", "nicotinic acid"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "D-Ca-pantothenate",
        "0.0000454",
        "CHEBI:31345",
        "Calcium pantothenate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "Vitamin B12", "0.000000908", "CHEBI:176843", "vitamin B12"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "p-Aminobenzoic acid",
        "0.0000454",
        "CHEBI:30753",
        "4-aminobenzoic acid",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523", "Lipoic acid", "0.0000454", "CHEBI:16494", "lipoic acid"
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "Na2WO4 x 2 H2O",
        "0.000364",
        "CHEBI:63939",
        "sodium tungstate dihydrate",
    ),
    _komodo_component(
        "KOMODO Medium 194_6523",
        "Na2SeO3 x 5 H2O",
        "0.000273",
        "CHEBI:131361",
        "disodium selenite pentahydrate",
    ),
    _komodo_component("KOMODO Medium 194_6523", "NaOH", "0.05", "CHEBI:32145", "sodium hydroxide"),
)


PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "DSMZ Medium 194 sparges Solution A with an 80% N2 and 20% CO2 "
            "gas mixture to reach pH below 6, distributes it under the same "
            "gas atmosphere into anoxic Hungate-type tubes or serum vials, "
            "and autoclaves it."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "DSMZ Medium 194 autoclaves Solution B under 80% N2 and 20% CO2, "
            "autoclaves Solutions C and E under 100% N2, filter-sterilizes "
            "Solution D under 100% N2, then adds Solutions B to E to sterile "
            "cooled Solution A in sequence."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "DSMZ Medium 194 adjusts the final pH to 7.1-7.4.",
    },
    {
        "step_number": 4,
        "action": "FILTER_STERILIZE",
        "description": (
            "DSMZ Medium 194 notes that growth of some strains may be "
            "stimulated with 10-20 mg/L sodium dithionite from a freshly "
            "prepared anoxic 5% w/v solution sterilized by filtration."
        ),
    },
)

DSM_14880_STEPS = PREPARATION_STEPS + (
    {
        "step_number": 5,
        "action": "FILTER_STERILIZE",
        "description": (
            "For DSM 14880, DSMZ Medium 194 replaces sodium propionate with "
            "0.50 g/L yeast extract and 2.20 g/L sodium pyruvate added after "
            "autoclaving from anoxic stock solutions sterilized by filtration."
        ),
    },
)

DSM_21556_STEPS = PREPARATION_STEPS + (
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "For DSM 21556, DSMZ Medium 194 replaces sodium propionate with "
            "1.00 g/L sodium butyrate added after autoclaving from a sterile "
            "anoxic stock solution prepared under N2."
        ),
    },
)

DSM_13527_STEPS = PREPARATION_STEPS + (
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "For DSM 13527, DSMZ Medium 194 replaces sodium propionate with "
            "1.00 g/L sodium butyrate added after autoclaving from a sterile "
            "anoxic stock solution prepared under N2."
        ),
    },
)

DSM_5092_STEPS = PREPARATION_STEPS + (
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "For DSM 5092, DSMZ Medium 194 replaces sodium propionate with "
            "0.90 g/L putrescine added after autoclaving from a sterile "
            "anoxic stock solution prepared under N2."
        ),
    },
)


DSMZ_194_CHILDREN = (
    _recipe_ref(
        KOMODO_194,
        "SOURCE_DUPLICATE",
        "KOMODO Medium 194 is a source-catalogue duplicate of DSMZ Medium 194.",
    ),
    _recipe_ref(
        KOMODO_194_1,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 194.1 applies a DSM 1744-specific final-component table.",
    ),
    _recipe_ref(
        KOMODO_194_2,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 194.2 applies the DSMZ Medium 194 DSM 14880 substitution.",
    ),
    _recipe_ref(
        KOMODO_194_3,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 194.3 applies the DSMZ Medium 194 DSM 21556 substitution.",
    ),
    _recipe_ref(
        KOMODO_194_13527,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 194_13527 applies the DSMZ Medium 194 DSM 13527 substitution.",
    ),
    _recipe_ref(
        KOMODO_194_5092,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 194_5092 applies the DSMZ Medium 194 DSM 5092 substitution.",
    ),
    _recipe_ref(
        KOMODO_194_6523,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 194_6523 applies the explicit KOMODO DSM 6523 table.",
    ),
)

DSMZ_194_PARENT = _recipe_ref(
    DSMZ_194,
    "STRAIN_SPECIFIC_VARIANT",
    "DSMZ Medium 194 is the official Desulfobulbus freshwater parent.",
)

KOMODO_TARGETS = (
    Target(
        path=KOMODO_194,
        source_label="KOMODO Medium 194",
        source_url=f"{KOMODO_BASE}194",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga stock rows with "
            "the explicit KOMODO Medium 194 final-component table."
        ),
        composition_type="DEFINED",
        components=BASE_COMPONENTS,
        parent_media=_recipe_ref(
            DSMZ_194,
            "SOURCE_DUPLICATE",
            "DSMZ Medium 194 is the official Desulfobulbus freshwater formulation.",
        ),
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=("KOMODO source-catalogue duplicate of DSMZ Medium 194.",),
    ),
    Target(
        path=KOMODO_194_1,
        source_label="KOMODO Medium 194.1",
        source_url=f"{KOMODO_BASE}194.1",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194.1 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga rows with the "
            "explicit KOMODO Medium 194.1 final-component table for DSM 1744."
        ),
        composition_type="UNDEFINED",
        components=KOMODO_194_1_COMPONENTS,
        parent_media=DSMZ_194_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Uses the KOMODO DSM 1744 table with 11.00 g/L NaCl, "
            "1.00 g/L yeast extract, and 2.50 g/L sodium lactate."
        ),
    ),
    Target(
        path=KOMODO_194_2,
        source_label="KOMODO Medium 194.2",
        source_url=f"{KOMODO_BASE}194.2",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194.2 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga rows with the DSMZ "
            "Medium 194 DSM 14880 pyruvate and yeast-extract substitution."
        ),
        composition_type="UNDEFINED",
        components=KOMODO_194_2_COMPONENTS,
        parent_media=DSMZ_194_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Replaces sodium propionate with 0.50 g/L yeast extract and "
            "2.20 g/L sodium pyruvate for DSM 14880."
        ),
    ),
    Target(
        path=KOMODO_194_3,
        source_label="KOMODO Medium 194.3",
        source_url=f"{KOMODO_BASE}194.3",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194.3 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga rows with the DSMZ "
            "Medium 194 DSM 21556 butyrate substitution."
        ),
        composition_type="DEFINED",
        components=KOMODO_194_3_COMPONENTS,
        parent_media=DSMZ_194_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Replaces sodium propionate with 1.00 g/L Na-butyrate for DSM 21556.",
        ),
    ),
    Target(
        path=KOMODO_194_13527,
        source_label="KOMODO Medium 194_13527",
        source_url=f"{KOMODO_BASE}194_13527",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194_13527 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga rows with the DSMZ "
            "Medium 194 DSM 13527 butyrate substitution."
        ),
        composition_type="DEFINED",
        components=KOMODO_194_13527_COMPONENTS,
        parent_media=DSMZ_194_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Keeps the 2.50 g/L NaHCO3 from KOMODO Medium 194_13527 and "
            "applies the DSMZ 1.00 g/L Na-butyrate substitution for DSM 13527."
        ),
    ),
    Target(
        path=KOMODO_194_5092,
        source_label="KOMODO Medium 194_5092",
        source_url=f"{KOMODO_BASE}194_5092",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194_5092 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga rows with the DSMZ "
            "Medium 194 DSM 5092 putrescine substitution."
        ),
        composition_type="DEFINED",
        components=KOMODO_194_5092_COMPONENTS,
        parent_media=DSMZ_194_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Replaces sodium propionate with 0.90 g/L putrescine for DSM 5092.",
        ),
    ),
    Target(
        path=KOMODO_194_6523,
        source_label="KOMODO Medium 194_6523",
        source_url=f"{KOMODO_BASE}194_6523",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 194_6523 | "
            "DSMZ Medium: 194 (mediadive.medium:194) | Aerobic: No"
        ),
        curation_notes=(
            "Replaced stale DSMZ Medium 194a Desulfovirga rows with the "
            "explicit KOMODO Medium 194_6523 final-component table."
        ),
        composition_type="DEFINED",
        components=KOMODO_194_6523_COMPONENTS,
        parent_media=DSMZ_194_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Uses the explicit KOMODO Medium 194_6523 final-component table.",),
    ),
)

TARGETS = (
    Target(
        path=DSMZ_194,
        source_label="DSMZ Medium 194",
        source_url=DSMZ_194_REST,
        record_notes=f"Source: DSMZ | Link: {DSMZ_194_PDF}",
        curation_notes=(
            "Added resolved KOMODO Medium 194 source duplicate and strain "
            "variants as children of the official DSMZ Medium 194 record."
        ),
        composition_type="UNDEFINED",
        variant_children=DSMZ_194_CHILDREN,
        extra_references=(DSMZ_194_PDF,),
    ),
    Target(
        path=DSMZ_194A,
        source_label="DSMZ Medium 194a",
        source_url=DSMZ_194A_REST,
        record_notes=f"Source: DSMZ | Link: {DSMZ_194A_PDF}",
        curation_notes=(
            "Removed erroneous SOURCE_DUPLICATE variant metadata that linked "
            "DSMZ Medium 194a Desulfovirga Medium to KOMODO Medium 194."
        ),
        composition_type="DEFINED",
        extra_references=(DSMZ_194A_PDF,),
    ),
    *KOMODO_TARGETS,
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
            f"{target.path}: found source term {source_term!r}, expected "
            f"{EXPECTED_SOURCE_TERMS[target.path]!r}"
        )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    urls = [target.source_url, *target.extra_references]
    if target.path not in (DSMZ_194, DSMZ_194A):
        urls.append(DSMZ_194_REST)
        urls.append(DSMZ_194_PDF)

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in urls:
        if url not in seen:
            references.append({"reference": url})
            seen.add(url)


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 194 chemistry and variant metadata",
        "source": target.source_url,
        "notes": target.curation_notes,
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


def _set_variant_fields(repaired: dict[str, Any], target: Target) -> None:
    for field in (
        "parent_media",
        "variant_relationship",
        "variant_modifications",
        "variant_children",
    ):
        repaired.pop(field, None)

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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["notes"] = target.record_notes

    if target.components is not None:
        repaired["medium_type"] = "COMPLEX"
        repaired["composition_type"] = target.composition_type
        repaired["physical_state"] = "LIQUID"
        repaired["ingredients"] = [_ingredient(component) for component in target.components]
        repaired.pop("ph_value", None)
        _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
        _put_after(
            repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients"
        )
        if target.path == KOMODO_194_2:
            repaired["preparation_steps"] = copy.deepcopy(list(DSM_14880_STEPS))
        elif target.path == KOMODO_194_3:
            repaired["preparation_steps"] = copy.deepcopy(list(DSM_21556_STEPS))
        elif target.path == KOMODO_194_13527:
            repaired["preparation_steps"] = copy.deepcopy(list(DSM_13527_STEPS))
        elif target.path == KOMODO_194_5092:
            repaired["preparation_steps"] = copy.deepcopy(list(DSM_5092_STEPS))
        _put_after(repaired, "data_quality_flags", list(DATA_QUALITY_FLAGS), "preparation_steps")

    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")
    _set_variant_fields(repaired, target)
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
