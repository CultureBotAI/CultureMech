#!/usr/bin/env python3
"""
Enrich SSSOM Mappings with EBI OLS API

Verifies existing CHEBI mappings and discovers new mappings using the
EBI Ontology Lookup Service API.

Usage:
    uv run python scripts/enrich_sssom_with_ols.py [options]
"""

import argparse
import sys
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, List, Dict, Tuple

import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
from culturemech.ontology.ols_client import OLSClient
from culturemech.ontology.oak_client import OAKClient


# ================================================================
# PREPROCESSING AND NORMALIZATION
# Integrates MicroMediaParam's battle-tested normalization methods
# Source: MicroMediaParam/src/mapping/compound_normalizer.py
# Last updated: 2026-02-09
# ================================================================

# Gas abbreviation expansion lookup
GAS_ABBREVIATIONS = {
    'N2': ['nitrogen gas', 'molecular nitrogen', 'dinitrogen'],
    'O2': ['oxygen gas', 'molecular oxygen', 'dioxygen'],
    'CO2': ['carbon dioxide', 'CO2'],
    'H2': ['hydrogen gas', 'molecular hydrogen', 'dihydrogen'],
    'H2S': ['hydrogen sulfide', 'H2S'],
    'NH3': ['ammonia', 'NH3'],
}

# Bio-material keywords for multi-ontology routing
BIO_MATERIAL_KEYWORDS = [
    'extract', 'peptone', 'tryptone', 'casein', 'yeast',
    'serum', 'blood', 'meat', 'beef', 'soy', 'whey',
    'malt', 'agar', 'gelatin', 'digest'
]

# Brand name patterns to strip
BRAND_PATTERNS = [
    r'\(BD-Difco\)',
    r'\(Difco\)',
    r'\(Sigma\)',
    r'\(Merck\)',
    r'Bacto\s+',
    r'BD\s+',
]

# Solution concentration pattern
CONCENTRATION_PATTERN = re.compile(
    r'(\d+(?:\.\d+)?)\s*(%|mM|M|g/L|mg/mL|µM|μM)\s*',
    re.IGNORECASE
)

# ================================================================
# MICROMEDIAPARAM DICTIONARIES (Curated Mappings)
# Source: MicroMediaParam/src/mapping/compound_normalizer.py
# ================================================================

# Biological products - verified mappings (100+ entries)
# These are complex biological mixtures with known ontology IDs
BIOLOGICAL_PRODUCTS = {
    # Extracts (FOODON)
    'Yeast extract': 'FOODON:03315426',
    'yeast extract': 'FOODON:03315426',
    'Beef extract': 'FOODON:03302088',
    'beef extract': 'FOODON:03302088',
    'Meat extract': 'FOODON:03315424',
    'meat extract': 'FOODON:03315424',
    'Malt extract': 'FOODON:03301056',
    'malt extract': 'FOODON:03301056',
    'Malt extract powder': 'FOODON:03301056',

    # Peptones (FOODON)
    'Tryptone': 'FOODON:03310375',
    'tryptone': 'FOODON:03310375',
    'Bacto Tryptone': 'FOODON:03310375',
    'Trypticase peptone': 'FOODON:03310375',
    'Tryptone peptone': 'FOODON:03310375',
    'Peptone': 'FOODON:03302071',
    'peptone': 'FOODON:03302071',
    'Peptone Oxoid': 'FOODON:03302071',
    'Proteose peptone': 'FOODON:03302071',
    'Proteose peptone no. 3': 'FOODON:03302071',
    'Universal peptone': 'FOODON:03302071',
    'Meat peptone': 'FOODON:03302071',
    'Phytone peptone': 'FOODON:03302071',
    'Soy peptone': 'FOODON:03302071',
    'soy peptone': 'FOODON:03302071',
    'Neopeptone': 'FOODON:03302071',
    'Peptone (Oxoid)': 'FOODON:03302071',
    'Polypeptone': 'FOODON:03302071',
    'polypeptone': 'FOODON:03302071',
    'Casitone': 'FOODON:03302071',
    'casitone': 'FOODON:03302071',

    # Dairy/Protein (FOODON/CHEBI)
    'Casein': 'FOODON:03420180',
    'casein': 'FOODON:03420180',
    'Casein peptone': 'FOODON:03420180',
    'Whey': 'FOODON:03420244',
    'whey': 'FOODON:03420244',
    'Milk': 'UBERON:0001913',

    # Blood products (UBERON)
    'Blood': 'UBERON:0000178',
    'blood': 'UBERON:0000178',
    'Horse blood': 'UBERON:0000178',
    'Sheep blood': 'UBERON:0000178',
    'Bovine blood': 'UBERON:0000178',
    'Serum': 'UBERON:0001977',
    'serum': 'UBERON:0001977',
    'Blood serum': 'UBERON:0001977',

    # Organs (UBERON)
    'Liver': 'UBERON:0002107',
    'liver': 'UBERON:0002107',
    'Liver extract': 'UBERON:0002107',
    'Bile': 'UBERON:0001970',
    'bile': 'UBERON:0001970',
    'Ox bile': 'UBERON:0001970',

    # Nucleic acids (CHEBI)
    'DNA': 'CHEBI:16991',
    'dna': 'CHEBI:16991',
    'Fish-Sperm DNA': 'CHEBI:16991',
    'Salmon sperm DNA': 'CHEBI:16991',
    'RNA': 'CHEBI:33697',
    'rna': 'CHEBI:33697',

    # Gelling/thickening agents (CHEBI)
    'Agar': 'CHEBI:2509',
    'agar': 'CHEBI:2509',
    'Gelatin': 'CHEBI:5291',
    'gelatin': 'CHEBI:5291',
    'Starch': 'CHEBI:28017',
    'starch': 'CHEBI:28017',

    # Water variants (all map to CHEBI:15377 - water)
    'Water': 'CHEBI:15377',
    'water': 'CHEBI:15377',
    'Distilled water': 'CHEBI:15377',
    'distilled water': 'CHEBI:15377',
    'Double distilled water': 'CHEBI:15377',
    'double distilled water': 'CHEBI:15377',
    'Demineralized water': 'CHEBI:15377',
    'demineralized water': 'CHEBI:15377',
    'Deionized water': 'CHEBI:15377',
    'deionized water': 'CHEBI:15377',
    'Tap water': 'CHEBI:15377',
    'tap water': 'CHEBI:15377',
    'Sterile water': 'CHEBI:15377',
    'sterile water': 'CHEBI:15377',

    # Enzymes (CHEBI)
    'Catalase': 'CHEBI:75078',
    'catalase': 'CHEBI:75078',

    # Corn-derived products (FOODON)
    'Corn steep liquor': 'FOODON:03309991',
    'corn steep liquor': 'FOODON:03309991',
    'Corn steep powder': 'FOODON:03309991',
    'Corn meal': 'FOODON:03311737',
    'corn meal': 'FOODON:03311737',

    # Other biological extracts
    'Soil extract': 'ENVO:00001998',
    'soil extract': 'ENVO:00001998',
    'Bovine albumin': 'CHEBI:3136',
    'bovine albumin': 'CHEBI:3136',
    'BSA': 'CHEBI:3136',
    'Bovine serum albumin': 'CHEBI:3136',

    # Commercial growth media
    'Trypticase soy broth': 'FOODON:03302071',
    'Nutrient broth': 'FOODON:03302071',
    'Brain heart infusion': 'FOODON:03302088',
    'BHI': 'FOODON:03302088',
}

# Chemical formula to common name mappings (subset of 400+ from MicroMediaParam)
# PubChem and CHEBI work better with common names than formulas
FORMULA_TO_NAME = {
    # Iron compounds
    'Fe2(SO4)3': 'iron(III) sulfate',
    'FeSO4': 'iron(II) sulfate',
    'FeCl2': 'iron(II) chloride',
    'FeCl3': 'iron(III) chloride',
    'Fe(NO3)3': 'iron(III) nitrate',
    'Fe(NH4)2(SO4)2': 'ammonium iron(II) sulfate',
    'FeNH4(SO4)2': 'ammonium iron(III) sulfate',

    # Ammonium compounds
    '(NH4)2SO4': 'ammonium sulfate',
    '(NH4)2CO3': 'ammonium carbonate',
    '(NH4)2HPO4': 'diammonium hydrogen phosphate',
    'NH4Cl': 'ammonium chloride',
    'NH4NO3': 'ammonium nitrate',
    '(NH4)6Mo7O24': 'ammonium molybdate',
    'NH42HPO4': 'diammonium hydrogen phosphate',
    'NH42MoO4': 'ammonium molybdate',
    'NH46Mo7O24': 'ammonium heptamolybdate',

    # Calcium compounds
    'Ca(NO3)2': 'calcium nitrate',
    'CaCl2': 'calcium chloride',
    'CaSO4': 'calcium sulfate',
    'Ca(OH)2': 'calcium hydroxide',

    # Magnesium compounds
    'MgSO4': 'magnesium sulfate',
    'MgCl2': 'magnesium chloride',
    'Mg(NO3)2': 'magnesium nitrate',

    # Sodium compounds
    'Na2SO4': 'sodium sulfate',
    'Na2CO3': 'sodium carbonate',
    'NaHCO3': 'sodium bicarbonate',
    'Na2HPO4': 'disodium hydrogen phosphate',
    'NaH2PO4': 'sodium dihydrogen phosphate',
    'Na2MoO4': 'sodium molybdate',
    'Na2SeO3': 'sodium selenite',
    'Na2SeO4': 'sodium selenate',
    'Na2WO4': 'sodium tungstate',
    'Na3citrate': 'trisodium citrate',
    'Na3-citrate': 'trisodium citrate',
    'Na3PO4': 'trisodium phosphate',
    'Na2S': 'sodium sulfide',
    'Na2S2O3': 'sodium thiosulfate',
    'NaSiO3': 'sodium silicate',
    'Na2SiO3': 'sodium silicate',

    # Potassium compounds
    'K2SO4': 'potassium sulfate',
    'K2CO3': 'potassium carbonate',
    'KH2PO4': 'potassium dihydrogen phosphate',
    'K2HPO4': 'dipotassium hydrogen phosphate',
    'KNO3': 'potassium nitrate',
    'K3citrate': 'tripotassium citrate',
    'K3PO4': 'tripotassium phosphate',
    'KIO3': 'potassium iodate',
    'KBr': 'potassium bromide',

    # Zinc compounds
    'ZnSO4': 'zinc sulfate',
    'ZnCl2': 'zinc chloride',
    'Zn(NO3)2': 'zinc nitrate',

    # Copper compounds
    'CuSO4': 'copper(II) sulfate',
    'CuCl2': 'copper(II) chloride',
    'Cu(NO3)2': 'copper(II) nitrate',

    # Manganese compounds
    'MnSO4': 'manganese(II) sulfate',
    'MnCl2': 'manganese(II) chloride',
    'Mn(NO3)2': 'manganese(II) nitrate',
    'MnCl4': 'manganese(II) chloride',  # Common typo

    # Cobalt compounds
    'CoCl2': 'cobalt(II) chloride',
    'CoSO4': 'cobalt(II) sulfate',
    'Co(NO3)2': 'cobalt(II) nitrate',

    # Nickel compounds
    'NiCl2': 'nickel(II) chloride',
    'NiSO4': 'nickel(II) sulfate',
    'Ni(NO3)2': 'nickel(II) nitrate',

    # Aluminum compounds
    'Al2(SO4)3': 'aluminum sulfate',
    'AlCl3': 'aluminum chloride',
    'Al(NO3)3': 'aluminum nitrate',
    'AlK(SO4)2': 'potassium aluminum sulfate',

    # Chromium compounds
    'CrCl3': 'chromium(III) chloride',
    'Cr(NO3)3': 'chromium(III) nitrate',
    'Cr2(SO4)3': 'chromium(III) sulfate',

    # Other common salts
    'H3BO3': 'boric acid',
    'Na2B4O7': 'sodium tetraborate',
    'NaF': 'sodium fluoride',
    'NaBr': 'sodium bromide',
    'BaCl2': 'barium chloride',
    'Ba(NO3)2': 'barium nitrate',

    # Typo corrections
    'Na2Mo4': 'sodium molybdate',  # Missing O
    'NH42SO4': 'ammonium sulfate',  # Should be (NH4)2SO4
    'FeSO43': 'iron(III) sulfate',  # Typo for Fe2(SO4)3
}

# Buffer compounds - map abbreviations to full chemical names
BUFFER_COMPOUNDS = {
    'HEPES': '4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid',
    'MES': '2-(N-morpholino)ethanesulfonic acid',
    'PIPES': "piperazine-N,N'-bis(2-ethanesulfonic acid)",
    'MOPS': '3-(N-morpholino)propanesulfonic acid',
    'Tris': 'tris(hydroxymethyl)aminomethane',
    'TRIS': 'tris(hydroxymethyl)aminomethane',
    'TES': "N-[tris(hydroxymethyl)methyl]-2-aminoethanesulfonic acid",
    'CAPS': '3-(cyclohexylamino)-1-propanesulfonic acid',
    'CHES': '2-(cyclohexylamino)ethanesulfonic acid',
    'EPPS': '4-(2-hydroxyethyl)-1-piperazinepropanesulfonic acid',
    'HEPPSO': '4-(2-hydroxyethyl)piperazine-1-(2-hydroxypropanesulfonic acid)',
    'Bicine': 'N,N-bis(2-hydroxyethyl)glycine',
    'Tricine': 'N-[tris(hydroxymethyl)methyl]glycine',
    'ADA': 'N-(2-acetamido)iminodiacetic acid',
    'BIS-TRIS': 'bis(2-hydroxyethyl)amino-tris(hydroxymethyl)methane',
}

# Greek letter mappings
GREEK_TO_LATIN = {
    'α': 'alpha',
    'β': 'beta',
    'ß': 'beta',  # German eszett (often used for beta in copy-paste)
    'γ': 'gamma',
    'δ': 'delta',
    'ε': 'epsilon',
    'λ': 'lambda',
    'ω': 'omega',
}

# Stereochemistry prefix fixes
STEREO_FIXES = [
    (r'^D\+-', 'D-'),       # D+-Glucose → D-Glucose
    (r'^L\+-', 'L-'),       # L+-Tartaric → L-Tartaric
    (r'^D-\+-', 'D-'),      # D-+-biotin → D-biotin
    (r'^L-\+-', 'L-'),
    (r'^DL\+-', 'DL-'),
    (r'^\(\+\)-', ''),      # (+)-compound → compound
    (r'^\(-\)-', ''),       # (-)-compound → compound
    (r'^\(±\)-', 'DL-'),    # (±)-compound → DL-compound
]

# Formula notation fixes - add missing parentheses
FORMULA_FIXES = [
    (r'NH4(\d)', r'(NH4)\1'),          # NH42 → (NH4)2
    (r'NO3(\d)', r'(NO3)\1'),          # NO32 → (NO3)2
    (r'SO4(\d)', r'(SO4)\1'),          # SO43 → (SO4)3
    (r'PO4(\d)', r'(PO4)\1'),          # PO42 → (PO4)2
    (r'MoO4(\d)', r'(MoO4)\1'),
    (r'OH(\d)', r'(OH)\1'),
    (r'CO3(\d)', r'(CO3)\1'),
]

# Atom symbol to name mappings for salt notation
ATOM_TO_NAME = {
    'Na': 'sodium',
    'Na2': 'disodium',
    'Na3': 'trisodium',
    'K': 'potassium',
    'K2': 'dipotassium',
    'K3': 'tripotassium',
    'Ca': 'calcium',
    'Mg': 'magnesium',
    'Fe': 'iron',
    'Cu': 'copper',
    'Zn': 'zinc',
    'NH4': 'ammonium',
}


# ================================================================
# NORMALIZATION FUNCTIONS (from MicroMediaParam)
# Source: MicroMediaParam/src/mapping/compound_normalizer.py
# ================================================================

def lookup_biological_product(name: str) -> Optional[str]:
    """
    Look up a biological product in the curated dictionary.

    Returns the ontology ID (FOODON, UBERON, CHEBI) if found.

    Examples:
        "Yeast extract" → "FOODON:03315426"
        "Blood" → "UBERON:0000178"
        "DNA" → "CHEBI:16991"

    Args:
        name: Ingredient name

    Returns:
        Ontology ID if found, None otherwise
    """
    if not name or not isinstance(name, str):
        return None

    # Try exact match first
    if name in BIOLOGICAL_PRODUCTS:
        return BIOLOGICAL_PRODUCTS[name]

    # Try case-insensitive match
    name_lower = name.lower()
    for product_name, ontology_id in BIOLOGICAL_PRODUCTS.items():
        if product_name.lower() == name_lower:
            return ontology_id

    # Try partial match for common patterns (e.g., "Yeast extract (Difco)")
    for product_name, ontology_id in BIOLOGICAL_PRODUCTS.items():
        if product_name.lower() in name_lower:
            return ontology_id

    return None


def convert_formula_to_name(name: str) -> str:
    """
    Convert chemical formula to common name.

    Examples:
        "Fe2(SO4)3" → "iron(III) sulfate"
        "(NH4)2CO3" → "ammonium carbonate"
        "Ca(NO3)2" → "calcium nitrate"

    Args:
        name: Chemical formula or name

    Returns:
        Common name if found in mapping, original name otherwise
    """
    if not name or not isinstance(name, str):
        return name

    # Try direct lookup
    if name in FORMULA_TO_NAME:
        return FORMULA_TO_NAME[name]

    # Try case-insensitive lookup
    name_clean = name.strip()
    for formula, common_name in FORMULA_TO_NAME.items():
        if formula.lower() == name_clean.lower():
            return common_name

    return name


def expand_buffer_name(name: str) -> str:
    """
    Expand buffer abbreviation to full chemical name.

    Examples:
        "HEPES buffer" → "4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid"
        "MES" → "2-(N-morpholino)ethanesulfonic acid"
        "Tris-HCl" → "tris(hydroxymethyl)aminomethane"

    Args:
        name: Buffer name or abbreviation

    Returns:
        Full chemical name or original name
    """
    if not name or not isinstance(name, str):
        return name

    # Remove 'buffer' keyword
    clean_name = re.sub(r'\s*buffer\s*', ' ', name, flags=re.IGNORECASE).strip()

    # Look for known buffer compounds
    for buffer_abbrev, full_name in BUFFER_COMPOUNDS.items():
        if buffer_abbrev.lower() in clean_name.lower():
            return full_name

    return name


def normalize_greek_letters(name: str) -> str:
    """
    Convert Greek letters to their Latin equivalents.

    Examples:
        "α-D-Glucose" → "alpha-D-Glucose"
        "ß-NAD" → "beta-NAD"
        "γ-aminobutyric acid" → "gamma-aminobutyric acid"

    Args:
        name: Compound name with potential Greek letters

    Returns:
        Name with Greek letters converted to Latin
    """
    if not name or not isinstance(name, str):
        return name

    result = name
    for greek, latin in GREEK_TO_LATIN.items():
        result = result.replace(greek, latin)

    return result


def normalize_stereochemistry_prefixes(name: str) -> str:
    """
    Normalize stereochemistry prefixes.

    Examples:
        "D+-Glucose" → "D-Glucose"
        "L+-Tartaric acid" → "L-Tartaric acid"
        "D-+-biotin" → "D-biotin"
        "(+)-alpha-tocopherol" → "alpha-tocopherol"

    Args:
        name: Compound name with stereochemistry prefixes

    Returns:
        Name with normalized stereochemistry prefixes
    """
    if not name or not isinstance(name, str):
        return name

    result = name
    for pattern, replacement in STEREO_FIXES:
        result = re.sub(pattern, replacement, result)

    return result


def fix_formula_notation(name: str) -> str:
    """
    Fix missing parentheses in chemical formulas.

    Examples:
        "NH42SO4" → "(NH4)2SO4"
        "CaNO32" → "Ca(NO3)2"
        "Fe2SO43" → "Fe2(SO4)3"

    Args:
        name: Chemical compound name or formula

    Returns:
        Formula with corrected parentheses
    """
    if not name or not isinstance(name, str):
        return name

    result = name
    for pattern, replacement in FORMULA_FIXES:
        result = re.sub(pattern, replacement, result)

    return result


def normalize_atom_salt_notation(name: str) -> str:
    """
    Convert atom symbol salt notation to proper chemical names.

    Examples:
        "Na-benzoate" → "sodium benzoate"
        "Na3 citrate" → "trisodium citrate"
        "K acetate" → "potassium acetate"

    Args:
        name: Compound name with atom-salt notation

    Returns:
        Compound name with proper chemical names
    """
    if not name or not isinstance(name, str):
        return name

    result = name

    # Sort by length (longest first) to match Na3 before Na
    sorted_atoms = sorted(ATOM_TO_NAME.items(), key=lambda x: -len(x[0]))

    # Pattern 1: Hyphenated notation (Na-benzoate, Na2-EDTA)
    for atom, full_name in sorted_atoms:
        pattern = rf'^{atom}-(\w+)'
        match = re.match(pattern, result)
        if match:
            compound_part = match.group(1)
            rest_of_name = result[match.end():]
            result = f'{full_name} {compound_part}{rest_of_name}'
            break

    # Pattern 2: Space-separated notation (Na acetate, Na3 citrate)
    if result == name:
        for atom, full_name in sorted_atoms:
            pattern = rf'^{atom}\s+([A-Za-z]\w*)'
            match = re.match(pattern, result)
            if match:
                compound_part = match.group(1)
                rest_of_name = result[match.end():]
                result = f'{full_name} {compound_part}{rest_of_name}'
                break

    # Pattern 3: Reverse notation with dot separator (EDTA·2Na, EDTA·4Na)
    # Common in EDTA salts where the metal comes after
    if result == name:
        edta_pattern = r'^(EDTA)[·\-\s]+(\d*)([A-Z][a-z]?)'
        edta_match = re.match(edta_pattern, result, re.IGNORECASE)
        if edta_match:
            compound_name = edta_match.group(1)
            count = edta_match.group(2)
            metal = edta_match.group(3)
            rest_of_name = result[edta_match.end():]

            # Build the metal+count key for ATOM_TO_NAME lookup
            # Note: ATOM_TO_NAME uses "Na2" but EDTA notation has "2Na"
            # So we need to flip: "2Na" → "Na2"
            metal_key = metal + count if count else metal
            if metal_key in ATOM_TO_NAME:
                full_name = ATOM_TO_NAME[metal_key]
                result = f'{full_name} {compound_name}{rest_of_name}'

    # Remove hydration from result for cleaner mapping
    result = re.sub(r'\s*[x×]\s*\d+\s*H2O$', '', result, flags=re.IGNORECASE)

    return result.strip()


def normalize_iron_oxidation(name: str) -> str:
    """
    Normalize iron oxidation state notation.

    Examples:
        "FeIII citrate" → "iron(III) citrate"
        "IronII chloride" → "iron(II) chloride"
        "FeIIIPO4" → "iron(III) phosphate"

    Args:
        name: Compound name with iron oxidation notation

    Returns:
        Normalized compound name
    """
    if not name or not isinstance(name, str):
        return name

    result = name

    # IronIII → iron(III), IronII → iron(II)
    result = re.sub(r'\bIronIII\b', 'iron(III)', result, flags=re.IGNORECASE)
    result = re.sub(r'\bIronII\b', 'iron(II)', result, flags=re.IGNORECASE)

    # FeIII → iron(III), FeII → iron(II)
    result = re.sub(r'\bFeIII\b', 'iron(III)', result)
    result = re.sub(r'\bFeII\b', 'iron(II)', result)

    # Iron III → iron(III), Iron II → iron(II)
    result = re.sub(r'\bIron\s+III\b', 'iron(III)', result, flags=re.IGNORECASE)
    result = re.sub(r'\bIron\s+II\b', 'iron(II)', result, flags=re.IGNORECASE)

    return result


def normalize_formula_spaces(name: str) -> str:
    """
    Remove spaces within chemical formulas.

    Examples:
        "Fe SO4 x 7 H2O" → "FeSO4 x 7 H2O"
        "Na Cl" → "NaCl"
        "Mg SO4" → "MgSO4"

    Args:
        name: Chemical formula with potential internal spaces

    Returns:
        Formula with spaces removed between chemical elements
    """
    if not name or not isinstance(name, str):
        return name

    result = name

    # Pattern: Element symbol + space + Element/formula part
    element_space_pattern = r'\b([A-Z][a-z]?)\s+([A-Z][a-z]?\d*(?:\([^)]+\)\d*)?)'

    # Keep applying until no more changes (handles multiple spaces)
    prev_result = None
    while prev_result != result:
        prev_result = result
        result = re.sub(element_space_pattern, r'\1\2', result)

    return result


def normalize_hcl_salt(name: str) -> str:
    """
    Normalize HCl salt notation to hydrochloride form.

    Examples:
        "Cystein-HCl x 2 H2O" → "Cysteine hydrochloride"
        "Thiamine-HCl" → "Thiamine hydrochloride"
        "L-Cysteine HCl x H2O" → "L-Cysteine hydrochloride"

    Args:
        name: Compound name with HCl salt notation

    Returns:
        Compound name with hydrochloride suffix
    """
    if not name or not isinstance(name, str):
        return name

    result = name

    # Pattern: compound-HCl (with optional hydration) → compound hydrochloride
    result = re.sub(r'-HCl\b\s*(?:[x×]\s*\d*\s*H2O)?', ' hydrochloride', result, flags=re.IGNORECASE)

    # Pattern: compound x HCl → compound hydrochloride
    result = re.sub(r'\s+x\s+HCl\b', ' hydrochloride', result, flags=re.IGNORECASE)

    # Pattern: compound HCl x H2O (space separated, with hydration)
    result = re.sub(r'\s+HCl\s*[x×]\s*\d*\s*H2O\b', ' hydrochloride', result, flags=re.IGNORECASE)

    # Pattern: compound HCl (space separated, no hydration)
    result = re.sub(r'\s+HCl\b', ' hydrochloride', result)

    return result.strip()


def normalize_for_mapping(name: str) -> str:
    """
    Apply all normalizations to prepare a compound name for mapping.

    This is the main 16-step normalization pipeline from MicroMediaParam.

    Normalization order:
    1. Remove prefix symbols (--compound)
    2. Clean malformed entries
    3. Fix formula notation (NH42SO4 → (NH4)2SO4)
    4. Normalize formula spaces (Fe SO4 → FeSO4)
    5. Normalize Greek letters (α→alpha, ß→beta)
    6. Normalize stereochemistry prefixes (D+→D-, L+→L-)
    7. Remove 'Elemental' prefix
    8. Normalize iron oxidation (IronIII, FeIII)
    9. Normalize HCl salt (-HCl, x HCl)
    10. Convert atom-salt notation (Na acetate)
    11. Normalize buffer synonyms (expand abbreviations)
    12. Extract base from hydrated salts
    13. Remove named hydrate suffixes (monohydrate, dihydrate)
    14. Remove hydration notation (x N H2O)
    15. Clean up whitespace
    16. Convert formulas to names (Fe2(SO4)3→iron(III) sulfate)

    Args:
        name: Raw compound name from source data

    Returns:
        Fully normalized compound name ready for API lookups
    """
    if not name or not isinstance(name, str):
        return ""

    result = name.strip()

    # Step 1: Remove prefix symbols (--compound)
    result = re.sub(r'^--+', '', result)

    # Step 2: Clean malformed entries
    result = re.sub(r'^\([0-9]+\)\s*', '', result)  # Remove leading numbers in parens
    result = re.sub(r'^[#\*\+\-]\s*', '', result)   # Remove special chars
    result = re.sub(r'^\d+\.?\d*%\s*(?:\(?[wvWV]/[wvWV]\)?)?\s*', '', result)  # Remove concentration (10%, 25% w/v, etc.)

    # Step 2.5: Normalize Unicode dots to standard ASCII
    # Handle various Unicode dot characters used in chemical formulas
    unicode_dots = {
        '·': '·',   # Middle dot (U+00B7) - keep for hydration
        '・': '·',   # Katakana middle dot (U+30FB) → middle dot
        '•': '·',   # Bullet (U+2022) → middle dot
        '∙': '·',   # Bullet operator (U+2219) → middle dot
        '⋅': '·',   # Dot operator (U+22C5) → middle dot
    }
    for unicode_char, replacement in unicode_dots.items():
        result = result.replace(unicode_char, replacement)

    # Step 3: Fix formula notation (NH42SO4 → (NH4)2SO4)
    result = fix_formula_notation(result)

    # Step 4: Normalize formula spaces (Fe SO4 → FeSO4)
    result = normalize_formula_spaces(result)

    # Step 5: Normalize Greek letters (α→alpha, ß→beta)
    result = normalize_greek_letters(result)

    # Step 6: Normalize stereochemistry prefixes (D+→D-, L+→L-)
    result = normalize_stereochemistry_prefixes(result)

    # Step 7: Remove 'Elemental' and 'anhydrous' prefixes
    result = re.sub(r'^Elemental\s+', '', result, flags=re.IGNORECASE)
    result = re.sub(r'^anhydrous\s+', '', result, flags=re.IGNORECASE)

    # Step 8: Normalize iron oxidation (IronIII→iron(III), FeIII→iron(III))
    result = normalize_iron_oxidation(result)

    # Step 9: Normalize HCl salt (Thiamine-HCl → Thiamine hydrochloride)
    result = normalize_hcl_salt(result)

    # Step 10: Convert atom-salt notation (Na acetate → sodium acetate)
    result = normalize_atom_salt_notation(result)

    # Step 11: Normalize buffer synonyms (expand abbreviations)
    result = expand_buffer_name(result)

    # Step 12-13: Remove hydrated salt suffixes (monohydrate, dihydrate, etc.)
    named_hydrates = [
        'monohydrate', 'dihydrate', 'trihydrate', 'tetrahydrate',
        'pentahydrate', 'hexahydrate', 'heptahydrate', 'octahydrate',
        'nonahydrate', 'decahydrate', 'hydrate'
    ]
    for hydrate_name in named_hydrates:
        pattern = rf'\s+{hydrate_name}$'
        result = re.sub(pattern, '', result, flags=re.IGNORECASE)

    # Step 14: Remove hydration notation (x N H2O, x n H2O)
    result = re.sub(r'\s*[x×·•\.]\s*[\dn]*\s*H2O$', '', result, flags=re.IGNORECASE)

    # Common typo fixes
    result = re.sub(r'\bHC1\b', 'HCl', result)  # HC1 → HCl
    result = re.sub(r'--+', '-', result)  # Double dashes → single dash

    # Step 15: Clean up whitespace
    result = re.sub(r'\s+', ' ', result).strip()

    # Step 16: Convert chemical formulas to common names
    result = convert_formula_to_name(result)

    return result


def normalize_ingredient_name(name: str) -> str:
    """
    Basic normalization for ingredient names (legacy function).

    This is kept for backward compatibility but now delegates
    to the comprehensive normalize_for_mapping() function.

    Args:
        name: Original ingredient name

    Returns:
        Normalized ingredient name
    """
    return normalize_for_mapping(name)


def strip_brand_names(ingredient_name: str) -> str:
    """Remove brand names from ingredient names."""
    cleaned = ingredient_name
    for pattern in BRAND_PATTERNS:
        cleaned = re.sub(pattern, '', cleaned, flags=re.IGNORECASE)
    return cleaned.strip()


def parse_solution(ingredient_name: str) -> Tuple[str, Optional[str], Optional[str]]:
    """
    Parse solution/concentration notation.

    Examples:
    - "5% Na2S・9H2O solution" → ("Na2S・9H2O", "5", "%")
    - "0.1 mM CaCl2" → ("CaCl2", "0.1", "mM")

    Args:
        ingredient_name: Original ingredient name

    Returns:
        Tuple of (base_chemical, concentration_value, concentration_unit)
    """
    # Extract concentration
    match = CONCENTRATION_PATTERN.search(ingredient_name)
    if match:
        concentration_value = match.group(1)
        concentration_unit = match.group(2)

        # Remove concentration from name to get base chemical
        base_chemical = CONCENTRATION_PATTERN.sub('', ingredient_name)
        base_chemical = base_chemical.replace('solution', '').strip()

        return base_chemical, concentration_value, concentration_unit

    return ingredient_name, None, None


def expand_gas_abbreviation(name: str) -> List[str]:
    """Expand gas abbreviations to full names for searching."""
    return GAS_ABBREVIATIONS.get(name, [name])


def generate_search_variants(name: str) -> List[str]:
    """
    Generate multiple search variants for an ingredient name.

    Tries different representations to maximize matching:
    - Original form
    - Without hydration numbers
    - With expanded salt notation
    - Alternative separators

    Args:
        name: Normalized ingredient name

    Returns:
        List of search variants (most likely first)
    """
    variants = [name]  # Start with normalized form

    # Try without hydration numbers
    # E.g., "MgSO4·7H2O" → "MgSO4"
    without_hydration = re.sub(r'[·・]\s*\d+\s*H2O', '', name)
    if without_hydration != name and without_hydration.strip():
        variants.append(without_hydration.strip())

    # Try converting salt notation to word form
    # E.g., "L-Cysteine·HCl" → "L-cysteine hydrochloride"
    if 'HCl' in name:
        with_word = name.replace('·HCl', ' hydrochloride').replace(' HCl', ' hydrochloride')
        if with_word != name:
            variants.append(with_word)

    if 'H2SO4' in name:
        with_word = name.replace('·H2SO4', ' sulfate').replace(' H2SO4', ' sulfate')
        if with_word != name:
            variants.append(with_word)

    # Try with parentheses for hydration (alternative CHEBI format)
    # E.g., "MgSO4·7H2O" → "MgSO4 (hydrate)"
    if re.search(r'[·・]\d+H2O', name):
        with_parens = re.sub(r'[·・]\d+H2O', ' (hydrate)', name)
        variants.append(with_parens.strip())

    # Remove duplicates while preserving order
    seen = set()
    unique_variants = []
    for v in variants:
        if v not in seen and v.strip():
            seen.add(v)
            unique_variants.append(v)

    return unique_variants


def is_bio_material(ingredient_name: str) -> bool:
    """Check if ingredient is likely a biological material."""
    name_lower = ingredient_name.lower()
    return any(keyword in name_lower for keyword in BIO_MATERIAL_KEYWORDS)


def load_sssom_file(sssom_path: Path) -> pd.DataFrame:
    """
    Load SSSOM TSV file, skipping metadata header.

    Args:
        sssom_path: Path to SSSOM file

    Returns:
        DataFrame with mapping data
    """
    # Find where data starts (after metadata comments)
    with open(sssom_path) as f:
        for i, line in enumerate(f):
            if not line.startswith('#'):
                skip_rows = i
                break
        else:
            raise ValueError("No data found in SSSOM file (all lines are comments)")

    # Load TSV data
    df = pd.read_csv(sssom_path, sep='\t', skiprows=skip_rows)

    return df


def extract_sssom_metadata(sssom_path: Path) -> str:
    """
    Extract metadata header from SSSOM file.

    Args:
        sssom_path: Path to SSSOM file

    Returns:
        Metadata header as string
    """
    metadata_lines = []

    with open(sssom_path) as f:
        for line in f:
            if line.startswith('#'):
                metadata_lines.append(line.rstrip())
            else:
                break

    return '\n'.join(metadata_lines)


def calculate_confidence(ingredient_name: str, ols_match: dict) -> float:
    """
    Calculate confidence score for OLS match.

    Args:
        ingredient_name: Original ingredient name
        ols_match: OLS search result

    Returns:
        Confidence score (0.0-1.0)
    """
    base_confidence = 0.5  # Base confidence for OLS matches

    # Boost for exact label match
    if ols_match['label'].lower() == ingredient_name.lower():
        base_confidence = 0.9

    # Boost for synonym match
    elif any(syn.lower() == ingredient_name.lower()
             for syn in ols_match.get('synonyms', [])):
        base_confidence = 0.85

    # Factor in OLS search score if available
    if 'score' in ols_match and ols_match['score'] > 0:
        # Normalize OLS score (typically 0-100) to 0-1
        normalized_score = min(ols_match['score'] / 100.0, 1.0)
        # Weighted average with base confidence
        base_confidence = (base_confidence * 0.6) + (normalized_score * 0.4)

    return round(base_confidence, 2)


def verify_existing_mappings(
    sssom_df: pd.DataFrame,
    ols_client: OLSClient,
    verbose: bool = False
) -> pd.DataFrame:
    """
    Verify existing CHEBI mappings using OLS API.

    Args:
        sssom_df: SSSOM DataFrame
        ols_client: OLS API client
        verbose: Show progress messages

    Returns:
        DataFrame with verified mappings
    """
    verified_mappings = []
    invalid_ids = []
    not_found = []

    # Count mapped entries to verify (skip unmapped)
    mapped_count = len(sssom_df[sssom_df['predicate_id'] != 'semapv:Unmapped'])
    unmapped_count = len(sssom_df[sssom_df['predicate_id'] == 'semapv:Unmapped'])

    if verbose:
        print(f"\nVerifying {mapped_count} mapped entries (skipping {unmapped_count} unmapped)...")
        print("=" * 70)

    verified_count = 0  # Track mapped entries processed
    for i, row in sssom_df.iterrows():
        # Skip unmapped entries - they don't have CHEBI IDs to verify
        if row['predicate_id'] == 'semapv:Unmapped':
            verified_mappings.append(row.to_dict())
            continue

        verified_count += 1
        chebi_id = row['object_id']

        # Verify with OLS
        ols_term = ols_client.verify_chebi_id(chebi_id)

        if ols_term:
            # Update with OLS metadata
            row_dict = row.to_dict()
            # Preserve existing mapping_method if present, otherwise mark as manual_curation
            if 'mapping_method' not in row_dict or pd.isna(row_dict.get('mapping_method')):
                row_dict['mapping_method'] = 'manual_curation'

            verified_mappings.append({
                **row_dict,
                'object_label': ols_term['label'],  # Update with official label
                'mapping_justification': 'semapv:ManualMappingCuration',
                'confidence': 1.0,  # Verified by OLS
                'comment': f"Verified via EBI OLS API - {row.get('comment', '')}"
            })
        else:
            # Check if it was invalid format or just not found
            if not chebi_id.startswith('CHEBI:'):
                invalid_ids.append(chebi_id)
            else:
                not_found.append(chebi_id)

            # Mark as potentially invalid
            row_dict = row.to_dict()
            if 'mapping_method' not in row_dict or pd.isna(row_dict.get('mapping_method')):
                row_dict['mapping_method'] = 'manual_curation'

            verified_mappings.append({
                **row_dict,
                'confidence': 0.1,
                'comment': f"CHEBI ID not found in OLS (invalid or deprecated) - {row.get('comment', '')}"
            })

        if verbose and verified_count % 100 == 0:
            valid_count = sum(1 for m in verified_mappings if m['confidence'] >= 0.5)
            print(f"Progress: {verified_count}/{mapped_count} "
                  f"({verified_count/mapped_count*100:.1f}%) - "
                  f"Valid: {valid_count}, Not found: {len(not_found)}, Invalid: {len(invalid_ids)}")

    if verbose:
        valid_count = sum(1 for m in verified_mappings if m['confidence'] >= 0.5)
        print(f"\nVerification complete:")
        print(f"  Valid: {valid_count}/{len(verified_mappings)}")
        print(f"  Not found in OLS: {len(not_found)}")
        print(f"  Invalid format: {len(invalid_ids)}")

        if invalid_ids and len(invalid_ids) <= 10:
            print(f"\nInvalid CHEBI IDs found:")
            for cid in invalid_ids[:10]:
                print(f"  - {cid}")

    return pd.DataFrame(verified_mappings)


def find_new_mappings(
    ingredients_df: pd.DataFrame,
    ols_client: OLSClient,
    oak_client: Optional[OAKClient] = None,
    search_threshold: float = 0.8,
    use_exact: bool = True,
    verbose: bool = False
) -> pd.DataFrame:
    """
    Find new CHEBI mappings for unmapped ingredients using multi-stage search.

    Search strategy:
    1. OLS exact match (fast, cached, high confidence)
    2. OAK synonym match (comprehensive, exact synonyms)
    3. Multi-ontology for bio-materials (FOODON, etc.)
    4. OLS fuzzy match (fallback, lower confidence)

    Args:
        ingredients_df: DataFrame with unique ingredients
        ols_client: OLS API client
        oak_client: OAK client for multi-ontology search (optional)
        search_threshold: Minimum confidence for mappings
        use_exact: Try exact matching first (default: True)
        verbose: Show progress messages

    Returns:
        DataFrame with new mappings
    """
    new_mappings = []
    stats = {
        'ols_exact': 0,
        'oak_synonym': 0,
        'multi_ontology': 0,
        'ols_fuzzy': 0,
        'normalized': 0,
        'solution_parsed': 0,
        'gas_expanded': 0,
        'brand_stripped': 0
    }

    # Filter to unmapped ingredients
    unmapped = ingredients_df[ingredients_df['has_chebi_mapping'] == False]

    if verbose:
        print(f"\nSearching for mappings for {len(unmapped)} unmapped ingredients...")
        print(f"Using exact-first strategy: {use_exact}")
        print(f"OAK client available: {oak_client is not None}")
        print("=" * 70)

    # Track Stage 0 (biological products) stats
    stats['bio_product_dict'] = 0

    for i, row in unmapped.iterrows():
        ingredient_name = row['ingredient_name']
        original_name = ingredient_name

        # ============================================================
        # STAGE 0: Pre-check biological products dictionary
        # High confidence (0.98), instant lookup, no API calls
        # ============================================================
        bio_product_id = lookup_biological_product(original_name)
        if bio_product_id:
            mapping = create_mapping(
                original_name,
                bio_product_id,
                original_name,  # Use original name as label
                confidence=0.98,
                predicate='skos:exactMatch',
                tool='BioProductDict',
                comment="Curated biological product mapping (MicroMediaParam)"
            )
            new_mappings.append(mapping)
            stats['bio_product_dict'] += 1
            continue  # Skip to next ingredient

        # Preprocessing: strip brand names
        ingredient_name = strip_brand_names(ingredient_name)
        if ingredient_name != original_name:
            stats['brand_stripped'] += 1

        # Preprocessing: parse solutions
        base_chemical, conc_value, conc_unit = parse_solution(ingredient_name)
        if conc_value:
            ingredient_name = base_chemical
            stats['solution_parsed'] += 1

        # Preprocessing: normalize with MicroMediaParam pipeline
        normalized_name = normalize_for_mapping(ingredient_name)
        if normalized_name != ingredient_name:
            stats['normalized'] += 1

        # Generate search variants (gas expansion + chemical variants)
        search_variants = []

        # Try gas abbreviation expansion first
        if normalized_name in GAS_ABBREVIATIONS:
            search_variants.extend(expand_gas_abbreviation(normalized_name))
            stats['gas_expanded'] += 1
        else:
            # Generate multiple search variants for chemicals
            search_variants = generate_search_variants(normalized_name)

        # Search each variant
        mapping_found = False
        for search_name in search_variants:
            if mapping_found:
                break

            # Stage 1: OLS exact match
            if use_exact:
                exact_results = ols_client.search_chebi(search_name, exact=True)
                if exact_results and exact_results[0].get('score', 0) > 80:
                    best_match = exact_results[0]
                    mapping = create_mapping(
                        original_name,
                        best_match['chebi_id'],
                        best_match['label'],
                        confidence=0.95,
                        predicate='skos:exactMatch',
                        tool='EBI_OLS_API|exact',
                        comment=f"OLS exact match (normalized: {search_name})"
                    )
                    new_mappings.append(mapping)
                    stats['ols_exact'] += 1
                    mapping_found = True
                    continue

            # Stage 2: OAK synonym match
            if oak_client:
                oak_results = oak_client.synonym_search(search_name, 'chebi')
                if oak_results:
                    result = oak_results[0]
                    mapping = create_mapping(
                        original_name,
                        result.curie,
                        result.label,
                        confidence=0.92,
                        predicate='skos:exactMatch',
                        tool='OAK|synonym',
                        comment=f"OAK synonym match: '{result.matched_term}'"
                    )
                    new_mappings.append(mapping)
                    stats['oak_synonym'] += 1
                    mapping_found = True
                    continue

            # Stage 3: Multi-ontology for bio-materials
            if oak_client and is_bio_material(original_name):
                # IMPORTANT: FOODON requires lowercase!
                search_name_lower = search_name.lower()
                multi_results = oak_client.multi_ontology_search(
                    search_name_lower,
                    ontologies=['chebi', 'foodon']
                )

                # Prefer CHEBI, fallback to FOODON
                for ontology in ['chebi', 'foodon']:
                    if multi_results.get(ontology):
                        result = multi_results[ontology][0]
                        mapping = create_mapping(
                            original_name,
                            result.curie,
                            result.label,
                            confidence=0.85 if ontology == 'chebi' else 0.80,
                            predicate='skos:closeMatch',
                            tool=f'OAK|{ontology}',
                            comment=f"Multi-ontology match ({ontology.upper()})"
                        )
                        new_mappings.append(mapping)
                        stats['multi_ontology'] += 1
                        mapping_found = True
                        break

        # Stage 4: OLS fuzzy fallback (only if nothing found yet)
        if not mapping_found:
            fuzzy_results = ols_client.search_chebi(normalized_name, exact=False)
            if fuzzy_results:
                best_match = fuzzy_results[0]
                confidence = calculate_confidence(normalized_name, best_match)

                if confidence >= search_threshold:
                    mapping = create_mapping(
                        original_name,
                        best_match['chebi_id'],
                        best_match['label'],
                        confidence=confidence,
                        predicate='skos:closeMatch',
                        tool='EBI_OLS_API|fuzzy',
                        comment=f"OLS fuzzy match (score: {best_match.get('score', 0):.2f})"
                    )
                    new_mappings.append(mapping)
                    stats['ols_fuzzy'] += 1

        if verbose and (i + 1) % 50 == 0:
            print(f"Progress: {i+1}/{len(unmapped)} "
                  f"({(i+1)/len(unmapped)*100:.1f}%) - "
                  f"Found {len(new_mappings)} new mappings")

    if verbose:
        print(f"\nSearch complete: {len(new_mappings)} new mappings found")
        print("\nMapping strategy breakdown:")
        print(f"  Bio product dict: {stats['bio_product_dict']} (Stage 0 - instant)")
        print(f"  OLS exact:        {stats['ols_exact']}")
        print(f"  OAK synonym:      {stats['oak_synonym']}")
        print(f"  Multi-ontology:   {stats['multi_ontology']}")
        print(f"  OLS fuzzy:        {stats['ols_fuzzy']}")
        print("\nPreprocessing statistics:")
        print(f"  Normalized:       {stats['normalized']} (MicroMediaParam pipeline)")
        print(f"  Solution parsed:  {stats['solution_parsed']}")
        print(f"  Gas expanded:     {stats['gas_expanded']}")
        print(f"  Brand stripped:   {stats['brand_stripped']}")

    return pd.DataFrame(new_mappings)


def create_mapping(
    ingredient_name: str,
    chebi_id: str,
    label: str,
    confidence: float,
    predicate: str,
    tool: str,
    comment: str = "",
    mapping_method: Optional[str] = None
) -> Dict:
    """
    Create a mapping dictionary in SSSOM format.

    Args:
        ingredient_name: Original ingredient name
        chebi_id: CHEBI ID (or other ontology CURIE)
        label: Ontology term label
        confidence: Confidence score (0.0-1.0)
        predicate: SKOS predicate (exactMatch, closeMatch, etc.)
        tool: Tool identifier
        comment: Additional comment
        mapping_method: Method category (auto-determined if not provided)

    Returns:
        Mapping dictionary
    """
    # Auto-determine mapping method if not provided
    if mapping_method is None:
        if 'BioProductDict' in tool:
            mapping_method = 'curated_dictionary'
        elif 'OLS' in tool and 'exact' in tool:
            mapping_method = 'ontology_exact'
        elif 'OAK' in tool and 'synonym' in tool:
            mapping_method = 'ontology_exact'
        elif 'OLS' in tool and 'fuzzy' in tool:
            mapping_method = 'ontology_fuzzy'
        elif 'OAK' in tool or 'MultiOntology' in tool:
            mapping_method = 'ontology_fuzzy'
        else:
            mapping_method = 'manual_curation'

    # Create CURIE for subject
    subject_id = re.sub(r'[^\w\-]', '_', ingredient_name)
    subject_id = re.sub(r'_+', '_', subject_id).strip('_')
    subject_id = f"culturemech:{subject_id}"

    return {
        'subject_id': subject_id,
        'subject_label': ingredient_name,
        'predicate_id': f'skos:{predicate.split(":")[-1]}',
        'object_id': chebi_id,
        'object_label': label,
        'mapping_justification': 'semapv:LexicalMatching',
        'confidence': confidence,
        'mapping_tool': tool,
        'mapping_method': mapping_method,
        'mapping_date': datetime.now(timezone.utc).isoformat(),
        'comment': comment
    }


def merge_mappings(
    verified_df: pd.DataFrame,
    new_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Merge verified and new mappings, removing duplicates.

    Args:
        verified_df: Verified existing mappings
        new_df: New OLS-discovered mappings

    Returns:
        Merged DataFrame
    """
    # Concatenate
    merged = pd.concat([verified_df, new_df], ignore_index=True)

    # Remove duplicates (prefer higher confidence)
    merged = merged.sort_values('confidence', ascending=False)
    merged = merged.drop_duplicates(subset=['subject_id', 'object_id'], keep='first')

    # Sort by confidence
    merged = merged.sort_values('confidence', ascending=False).reset_index(drop=True)

    return merged


def save_sssom_file(df: pd.DataFrame, output_path: Path, metadata_header: str):
    """
    Save DataFrame as SSSOM file with metadata header.

    Args:
        df: SSSOM DataFrame
        output_path: Output file path
        metadata_header: Metadata header string
    """
    # Create output directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write file
    with open(output_path, 'w') as f:
        # Write metadata
        f.write(metadata_header)
        f.write('\n')

        # Write TSV data
        df.to_csv(f, sep='\t', index=False)


def main():
    parser = argparse.ArgumentParser(
        description="Enrich SSSOM mappings using EBI OLS API and OAK"
    )
    parser.add_argument(
        '--input-sssom',
        type=Path,
        default=Path('output/culturemech_chebi_mappings.sssom.tsv'),
        help="Input SSSOM file"
    )
    parser.add_argument(
        '--input-ingredients',
        type=Path,
        default=Path('output/ingredients_unique.tsv'),
        help="Unique ingredient list TSV"
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('output/culturemech_chebi_mappings_enriched.sssom.tsv'),
        help="Output enriched SSSOM file"
    )
    parser.add_argument(
        '--verify-only',
        action='store_true',
        help="Only verify existing mappings (skip search)"
    )
    parser.add_argument(
        '--search-threshold',
        type=float,
        default=0.8,
        help="Minimum confidence for new mappings (0.0-1.0)"
    )
    parser.add_argument(
        '--rate-limit',
        type=float,
        default=5.0,
        help="Requests per second for OLS API"
    )
    parser.add_argument(
        '--cache-dir',
        type=Path,
        help="Cache directory for OLS responses"
    )
    parser.add_argument(
        '--use-oak',
        action='store_true',
        help="Enable OAK for multi-ontology search and synonym matching"
    )
    parser.add_argument(
        '--exact-first',
        action='store_true',
        help="Try exact matching before fuzzy search (recommended)"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show progress messages"
    )

    args = parser.parse_args()

    # Check input files exist
    if not args.input_sssom.exists():
        print(f"Error: Input SSSOM file not found: {args.input_sssom}")
        sys.exit(1)

    if not args.verify_only and not args.input_ingredients.exists():
        print(f"Error: Input ingredients file not found: {args.input_ingredients}")
        sys.exit(1)

    print("=" * 70)
    print("CultureMech SSSOM Enrichment with EBI OLS and OAK")
    print("=" * 70)
    print(f"Input SSSOM: {args.input_sssom}")
    if not args.verify_only:
        print(f"Input ingredients: {args.input_ingredients}")
    print(f"Output: {args.output}")
    print(f"Rate limit: {args.rate_limit} req/s")
    print(f"Search threshold: {args.search_threshold}")
    print(f"OAK enabled: {args.use_oak}")
    print(f"Exact-first: {args.exact_first}")
    print()

    # Initialize OLS client
    if args.verbose:
        print("Initializing OLS client...")

    ols_client = OLSClient(
        cache_dir=args.cache_dir,
        rate_limit=args.rate_limit
    )

    # Initialize OAK client if requested
    oak_client = None
    if args.use_oak:
        if args.verbose:
            print("Initializing OAK client...")
        try:
            oak_client = OAKClient(cache_dir=args.cache_dir)
            if args.verbose:
                print("✓ OAK client initialized")
        except Exception as e:
            print(f"⚠ Warning: Could not initialize OAK client: {e}")
            print("  Continuing with OLS only...")
            args.use_oak = False

    # Load existing SSSOM file
    if args.verbose:
        print(f"Loading SSSOM file: {args.input_sssom}")

    sssom_df = load_sssom_file(args.input_sssom)
    metadata_header = extract_sssom_metadata(args.input_sssom)

    if args.verbose:
        print(f"Loaded {len(sssom_df)} existing mappings")

    # Verify existing mappings
    verified_df = verify_existing_mappings(sssom_df, ols_client, verbose=args.verbose)

    # Find new mappings (if not verify-only)
    if args.verify_only:
        enriched_df = verified_df
    else:
        # Load ingredient list
        if args.verbose:
            print(f"\nLoading ingredient list: {args.input_ingredients}")

        ingredients_df = pd.read_csv(args.input_ingredients, sep='\t')

        if args.verbose:
            print(f"Loaded {len(ingredients_df)} unique ingredients")

        # Search for new mappings
        new_df = find_new_mappings(
            ingredients_df,
            ols_client,
            oak_client=oak_client,
            search_threshold=args.search_threshold,
            use_exact=args.exact_first,
            verbose=args.verbose
        )

        # Merge verified and new mappings
        if args.verbose:
            print("\nMerging mappings...")

        enriched_df = merge_mappings(verified_df, new_df)

    # Save enriched SSSOM file
    if args.verbose:
        print(f"\nSaving enriched SSSOM file: {args.output}")

    save_sssom_file(enriched_df, args.output, metadata_header)

    # Print summary
    print("\n" + "=" * 70)
    print("Enrichment Summary")
    print("=" * 70)
    print(f"Original mappings: {len(sssom_df)}")
    print(f"Verified mappings: {len(verified_df[verified_df['confidence'] >= 0.5])}")
    print(f"Invalid/deprecated: {len(verified_df[verified_df['confidence'] < 0.5])}")

    if not args.verify_only:
        new_count = len(enriched_df) - len(sssom_df)
        print(f"New OLS mappings: {new_count}")

    print(f"Total enriched mappings: {len(enriched_df)}")
    print()
    print("Confidence distribution:")
    for conf_range in [(0.9, 1.0), (0.8, 0.9), (0.5, 0.8), (0.0, 0.5)]:
        count = len(enriched_df[
            (enriched_df['confidence'] >= conf_range[0]) &
            (enriched_df['confidence'] < conf_range[1])
        ])
        print(f"  {conf_range[0]:.1f}-{conf_range[1]:.1f}: {count}")
    print()

    # Mapping method breakdown
    if 'mapping_method' in enriched_df.columns:
        print("Mapping method breakdown:")
        method_counts = enriched_df['mapping_method'].value_counts()
        method_labels = {
            'curated_dictionary': 'Curated Dictionary (BioProductDict)',
            'ontology_exact': 'Ontology Exact Match (OLS/OAK)',
            'ontology_fuzzy': 'Ontology Fuzzy Match (OLS/OAK)',
            'manual_curation': 'Manual Curation (Original)'
        }
        for method in ['curated_dictionary', 'ontology_exact', 'ontology_fuzzy', 'manual_curation']:
            count = method_counts.get(method, 0)
            if count > 0:
                label = method_labels.get(method, method)
                pct = count / len(enriched_df) * 100
                print(f"  {label}: {count} ({pct:.1f}%)")
        print()

    # OLS client statistics
    stats = ols_client.get_statistics()
    print("OLS API Statistics:")
    print(f"  Total requests: {stats['requests']}")
    print(f"  Cache hits: {stats['cache_hits']}")
    print(f"  Cache misses: {stats['cache_misses']}")
    print(f"  Cache hit rate: {stats['cache_hit_rate']*100:.1f}%")
    print(f"  Errors: {stats['errors']}")

    # OAK client statistics
    if oak_client:
        oak_stats = oak_client.get_statistics()
        print()
        print("OAK Client Statistics:")
        print(f"  Total searches: {oak_stats['searches']}")
        print(f"  Exact matches: {oak_stats['exact_matches']}")
        print(f"  Synonym matches: {oak_stats['synonym_matches']}")
        print(f"  No matches: {oak_stats['no_matches']}")
        print(f"  Success rate: {oak_stats['success_rate']*100:.1f}%")
        print(f"  Errors: {oak_stats['errors']}")

    print()
    print(f"Output saved to: {args.output}")
    print("=" * 70)


if __name__ == "__main__":
    main()
