"""Unit conversion utilities for media ingredient concentrations.

Converts various concentration units (G_PER_L, MOLAR, PERCENT, etc.) to molar
for quantitative comparison in similarity calculations.
"""

from typing import Optional, Dict
import json
from pathlib import Path


class UnitConverter:
    """Convert ingredient concentrations to molar for comparison."""

    def __init__(self, mw_cache_path: Optional[Path] = None):
        """
        Initialize unit converter.

        Args:
            mw_cache_path: Path to ChEBI molecular weight cache JSON.
                         If None, uses default location.
        """
        self.mw_cache_path = mw_cache_path or Path(__file__).parent.parent.parent.parent / 'data/chebi_molecular_weights.json'
        self.mw_cache: Dict[str, float] = {}
        self._load_mw_cache()

    def _load_mw_cache(self):
        """Load molecular weight cache from JSON file."""
        if self.mw_cache_path.exists():
            with open(self.mw_cache_path) as f:
                self.mw_cache = json.load(f)
        # If cache doesn't exist, will be empty dict (graceful degradation)

    def to_molar(self, value: float, unit: str, ingredient: Dict) -> Optional[float]:
        """
        Convert concentration to molar based on unit and ingredient properties.

        Args:
            value: Concentration value
            unit: ConcentrationUnitEnum value (e.g., 'G_PER_L', 'MOLAR', 'PERCENT')
            ingredient: Ingredient dict with CHEBI ID (for MW lookup)

        Returns:
            Concentration in molar, or None if not convertible

        Examples:
            >>> converter = UnitConverter()
            >>> # 58.44 g/L NaCl (MW=58.44) = 1.0 M
            >>> ing = {'term': {'id': 'CHEBI:26710'}}
            >>> converter.to_molar(58.44, 'G_PER_L', ing)
            1.0
        """
        # Handle already molar
        if unit in ('MOLAR', 'M'):
            return value

        # Handle units that don't need molecular weight
        elif unit in ('MILLIMOLAR', 'mM'):
            # mM / 1000 = M
            return value / 1000

        elif unit in ('MICROMOLAR', 'μM', 'uM'):
            # μM / 1,000,000 = M
            return value / 1_000_000

        elif unit in ('ML_PER_L', 'mL/L'):
            # Cannot convert volume to molar without density
            return None

        elif unit in ('VARIABLE', 'variable', 'UNKNOWN', 'unknown'):
            # Cannot convert variable/unknown concentrations
            return None

        # For units that need molecular weight, get it first
        mw = self._get_molecular_weight(ingredient)
        if mw is None:
            return None

        # Convert based on unit (requires MW)
        if unit in ('G_PER_L', 'g/L'):
            # g/L / (g/mol) = mol/L = M
            return value / mw

        elif unit in ('PERCENT', '%'):
            # Assume w/v: 1% = 10 g/L
            # 1% = 10 g/L, so convert to g/L first
            g_per_l = value * 10
            return g_per_l / mw

        elif unit in ('MG_PER_L', 'mg/L'):
            # mg/L / 1000 = g/L, then divide by MW
            g_per_l = value / 1000
            return g_per_l / mw

        elif unit in ('UG_PER_L', 'μg/L', 'ug/L'):
            # μg/L / 1,000,000 = g/L, then divide by MW
            g_per_l = value / 1_000_000
            return g_per_l / mw

        else:
            # Unknown unit
            return None

    def _get_molecular_weight(self, ingredient: Dict) -> Optional[float]:
        """
        Lookup molecular weight from CHEBI ID or compute from formula.

        Args:
            ingredient: Ingredient dict with 'term' field containing CHEBI ID

        Returns:
            Molecular weight in g/mol, or None if not available

        Priority:
            1. ChEBI ID lookup in cache
            2. Fallback to None (future: formula parser)
        """
        # Try CHEBI ID lookup
        chebi_id = ingredient.get('term', {}).get('id')
        if chebi_id:
            # Handle both 'CHEBI:12345' and '12345' formats
            if ':' in chebi_id:
                chebi_id_normalized = chebi_id.split(':')[1]
            else:
                chebi_id_normalized = chebi_id

            # Check cache with both formats
            if chebi_id in self.mw_cache:
                return self.mw_cache[chebi_id]
            elif chebi_id_normalized in self.mw_cache:
                return self.mw_cache[chebi_id_normalized]

        # Try MediaIngredientMech ID lookup (if populated with MW data)
        mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')
        if mim_id and mim_id in self.mw_cache:
            return self.mw_cache[mim_id]

        # Future: parse chemical formula if available
        # formula = ingredient.get('formula')
        # if formula:
        #     return self._compute_mw_from_formula(formula)

        return None

    def get_conversion_success_rate(self, ingredients: list) -> float:
        """
        Calculate percentage of ingredients that can be converted to molar.

        Args:
            ingredients: List of ingredient dicts

        Returns:
            Fraction of ingredients with convertible concentrations (0.0-1.0)
        """
        if not ingredients:
            return 0.0

        convertible = 0
        total = 0

        for ing in ingredients:
            conc = ing.get('concentration', {})
            value_str = conc.get('value', '0')
            unit = conc.get('unit', 'UNKNOWN')

            # Skip variable/unknown values
            if value_str in ('variable', 'unknown', 'VARIABLE', 'UNKNOWN'):
                continue

            total += 1

            try:
                value = float(value_str)
                molar = self.to_molar(value, unit, ing)
                if molar is not None:
                    convertible += 1
            except (ValueError, TypeError):
                pass

        return convertible / total if total > 0 else 0.0


# Common molecular weights for fallback (g/mol)
# These are approximate values for common ingredients
COMMON_MW = {
    # Salts
    'NaCl': 58.44,
    'KCl': 74.55,
    'CaCl2': 110.98,
    'MgSO4': 120.37,
    'Na2HPO4': 141.96,
    'KH2PO4': 136.09,
    'FeCl3': 162.20,

    # Sugars
    'glucose': 180.16,
    'sucrose': 342.30,
    'fructose': 180.16,
    'lactose': 342.30,

    # Organic acids
    'acetic acid': 60.05,
    'citric acid': 192.12,
    'lactic acid': 90.08,

    # Nitrogen sources
    'NH4Cl': 53.49,
    'NaNO3': 84.99,
    'urea': 60.06,
}
