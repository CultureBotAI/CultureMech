"""Taxonomy classification for media recipes.

Assigns multi-level taxonomy to recipes based on:
- Functional domain (from medium_type and applications)
- Environmental context (from target organisms and ingredient signals)
- Nutritional profile (from ingredient composition analysis)
"""

from typing import Dict, List, Optional, Set
from collections import Counter


class TaxonomyClassifier:
    """Assign taxonomy labels to media recipes."""

    def __init__(self):
        """Initialize taxonomy classifier."""
        # CHEBI IDs for carbon sources (expandable)
        self.carbon_source_chebi = {
            # Simple sugars
            '17234': 'SIMPLE_SUGAR',  # glucose
            '15903': 'SIMPLE_SUGAR',  # fructose
            '17992': 'SIMPLE_SUGAR',  # sucrose
            '28260': 'SIMPLE_SUGAR',  # galactose

            # Organic acids
            '15366': 'ORGANIC_ACID',  # acetic acid/acetate
            '16947': 'ORGANIC_ACID',  # lactic acid/lactate
            '133748': 'ORGANIC_ACID',  # citrate
            '15741': 'ORGANIC_ACID',  # pyruvate
            '30031': 'ORGANIC_ACID',  # succinate
        }

        # Keywords for carbon source detection in names
        self.carbon_keywords = {
            'SIMPLE_SUGAR': ['glucose', 'fructose', 'sucrose', 'galactose', 'dextrose', 'sugar'],
            'COMPLEX_CARBOHYDRATE': ['starch', 'cellulose', 'glycogen', 'polysaccharide'],
            'ORGANIC_ACID': ['acetate', 'lactate', 'citrate', 'succinate', 'pyruvate', 'malate'],
            'HYDROCARBON': ['alkane', 'benzene', 'toluene', 'hexadecane', 'petroleum', 'oil'],
            'UNDEFINED_ORGANIC': ['peptone', 'yeast extract', 'malt extract', 'soil extract', 'beef extract', 'tryptone']
        }

        # Keywords for nitrogen source detection
        self.nitrogen_keywords = {
            'INORGANIC': ['ammonium', 'nitrate', 'nitrite', 'nh4', 'no3', 'no2', '(nh4)2so4', 'nh4cl'],
            'AMINO_ACID': ['glutamate', 'glutamine', 'casein', 'amino acid'],
            'PEPTIDE': ['peptone', 'tryptone', 'casein', 'gelatin', 'protein'],
            'NUCLEOTIDE': ['purine', 'pyrimidine', 'adenine', 'guanine', 'cytosine', 'thymine', 'uracil']
        }

        # Environmental context signals
        self.salinity_threshold_marine = 30.0  # g/L NaCl for marine classification
        self.ph_acidophilic = 4.5
        self.ph_alkaliphilic = 9.0

    def classify_recipe(self, recipe: Dict) -> Dict:
        """
        Assign all taxonomy levels to a recipe.

        Args:
            recipe: Recipe dict with ingredients, medium_type, etc.

        Returns:
            MediaTaxonomy dict with domain, context, profile, formulation
        """
        taxonomy = {
            'domain': self._classify_domain(recipe),
            'context': self._classify_context(recipe),
            'profile': self._classify_profile(recipe),
            'formulation': recipe.get('name'),
            'formulation_id': recipe.get('id'),
            'classification_method': 'RULE_BASED'
        }

        # Calculate confidence score
        taxonomy['confidence_score'] = self._calculate_confidence(recipe, taxonomy)

        return taxonomy

    def _classify_domain(self, recipe: Dict) -> str:
        """
        Classify Level 1 functional domain.

        Args:
            recipe: Recipe dict

        Returns:
            FunctionalDomainEnum value
        """
        medium_type = recipe.get('medium_type', '')
        applications = recipe.get('applications', [])
        category = recipe.get('category', '')

        # Direct mapping from medium_type
        if medium_type == 'MINIMAL':
            return 'MINIMAL'
        elif medium_type == 'COMPLEX':
            return 'COMPLEX'
        elif medium_type == 'SELECTIVE':
            return 'SELECTIVE'
        elif medium_type == 'DIFFERENTIAL':
            return 'DIFFERENTIAL'
        elif medium_type == 'ENRICHMENT':
            return 'ENRICHMENT'

        # Check applications
        if applications:
            app_str = ' '.join(applications).lower()
            if 'enrichment' in app_str:
                return 'ENRICHMENT'
            elif 'selective' in app_str or 'selection' in app_str:
                return 'SELECTIVE'
            elif 'differential' in app_str or 'differentiation' in app_str:
                return 'DIFFERENTIAL'

        # Check category for specialized
        if category in ('algae', 'specialized'):
            return 'SPECIALIZED'

        # Default: try to determine from ingredients
        ingredients = recipe.get('ingredients', [])
        if self._has_undefined_components(ingredients):
            return 'COMPLEX'
        else:
            return 'MINIMAL'  # Default for defined compositions

    def _classify_context(self, recipe: Dict) -> List[str]:
        """
        Classify Level 2 environmental context (multivalued).

        Args:
            recipe: Recipe dict

        Returns:
            List of EnvironmentalContextEnum values
        """
        contexts = set()

        # Check category
        category = recipe.get('category', '')
        if category == 'algae':
            contexts.add('PHOTOTROPHIC')

        # Check salinity
        ingredients = recipe.get('ingredients', [])
        if self._is_high_salinity(ingredients):
            contexts.add('MARINE')
        elif self._has_low_salinity_indicators(recipe):
            contexts.add('FRESHWATER')

        # Check pH
        ph = recipe.get('ph_value')
        if ph:
            try:
                ph_val = float(ph)
                if ph_val < self.ph_acidophilic:
                    contexts.add('ACIDOPHILIC')
                elif ph_val > self.ph_alkaliphilic:
                    contexts.add('ALKALIPHILIC')
            except (ValueError, TypeError):
                pass

        # Check temperature
        temp = recipe.get('incubation_temperature', {})
        if temp:
            temp_val = temp.get('value')
            if temp_val:
                try:
                    temp_float = float(temp_val)
                    if temp_float > 45.0:
                        contexts.add('THERMOPHILIC')
                    elif temp_float < 15.0:
                        contexts.add('PSYCHROPHILIC')
                except (ValueError, TypeError):
                    pass

        # Check atmosphere
        atmosphere = recipe.get('incubation_atmosphere')
        if atmosphere in ('ANAEROBIC', 'MICROAEROPHILIC'):
            contexts.add('ANAEROBIC')

        # Check name for context signals
        name = recipe.get('name', '').lower()
        if 'marine' in name or 'seawater' in name or 'ocean' in name:
            contexts.add('MARINE')
        elif 'soil' in name or 'terrestrial' in name:
            contexts.add('TERRESTRIAL')
        elif 'clinical' in name or 'pathogen' in name or 'diagnostic' in name:
            contexts.add('CLINICAL')
        elif 'industrial' in name or 'fermentation' in name or 'bioreactor' in name:
            contexts.add('INDUSTRIAL')

        # Default: TERRESTRIAL if no specific context found
        if not contexts:
            contexts.add('TERRESTRIAL')

        return sorted(list(contexts))

    def _classify_profile(self, recipe: Dict) -> Dict:
        """
        Classify Level 3 nutritional profile.

        Args:
            recipe: Recipe dict

        Returns:
            NutritionalProfile dict
        """
        ingredients = recipe.get('ingredients', [])

        profile = {
            'carbon_sources': self._classify_carbon_sources(ingredients),
            'nitrogen_sources': self._classify_nitrogen_sources(ingredients),
            'nutrient_density': self._calculate_nutrient_density(ingredients),
            'metal_level': self._classify_metal_level(recipe, ingredients),
            'special_additives': self._identify_special_additives(ingredients, recipe)
        }

        return profile

    def _classify_carbon_sources(self, ingredients: List[Dict]) -> List[str]:
        """Identify carbon source types."""
        carbon_sources = set()

        for ing in ingredients:
            # Check CHEBI ID
            chebi_id = ing.get('term', {}).get('id', '')
            if chebi_id:
                chebi_num = chebi_id.split(':')[-1] if ':' in chebi_id else chebi_id
                if chebi_num in self.carbon_source_chebi:
                    carbon_sources.add(self.carbon_source_chebi[chebi_num])

            # Check preferred term
            term = ing.get('preferred_term', '').lower()
            for source_type, keywords in self.carbon_keywords.items():
                if any(keyword in term for keyword in keywords):
                    carbon_sources.add(source_type)
                    break

            # Check role
            roles = ing.get('role', [])
            if 'Carbon source' in roles:
                # Try to determine type from name
                if not carbon_sources:  # Only if not already classified
                    carbon_sources.add('UNDEFINED_ORGANIC')

        return sorted(list(carbon_sources)) if carbon_sources else ['NONE']

    def _classify_nitrogen_sources(self, ingredients: List[Dict]) -> List[str]:
        """Identify nitrogen source types."""
        nitrogen_sources = set()

        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()

            # Check keywords
            for source_type, keywords in self.nitrogen_keywords.items():
                if any(keyword in term for keyword in keywords):
                    nitrogen_sources.add(source_type)
                    break

            # Check role
            roles = ing.get('role', [])
            if 'Nitrogen source' in roles:
                if not nitrogen_sources:  # Only if not already classified
                    nitrogen_sources.add('UNDEFINED')

        return sorted(list(nitrogen_sources)) if nitrogen_sources else ['NONE']

    def _calculate_nutrient_density(self, ingredients: List[Dict]) -> str:
        """Calculate overall nutrient density."""
        total_organics = 0.0

        for ing in ingredients:
            conc = ing.get('concentration', {})
            value_str = conc.get('value', '0')
            unit = conc.get('unit', '')

            # Only count organic compounds in g/L
            if unit in ('G_PER_L', 'g/L'):
                try:
                    value = float(value_str)
                    # Check if organic (crude heuristic: has C-H bonds, not just salts)
                    term = ing.get('preferred_term', '').lower()
                    if any(org in term for org in ['glucose', 'peptone', 'yeast', 'extract', 'acid', 'tryptone', 'casein', 'malt']):
                        total_organics += value
                except (ValueError, TypeError):
                    pass

        if total_organics < 5.0:
            return 'MINIMAL'
        elif total_organics <= 20.0:
            return 'STANDARD'
        else:
            return 'RICH'

    def _classify_metal_level(self, recipe: Dict, ingredients: List[Dict]) -> str:
        """Classify metal supplementation level."""
        # Check existing flags
        if recipe.get('high_ree'):
            return 'RARE_EARTH'
        elif recipe.get('high_metal'):
            return 'HIGH_METAL'

        # Count trace metals
        metal_count = 0
        metal_keywords = ['iron', 'copper', 'zinc', 'manganese', 'cobalt', 'nickel', 'molybdenum', 'ferric', 'ferrous', 'fe', 'cu', 'zn', 'mn', 'co', 'ni', 'mo']

        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if any(metal in term for metal in metal_keywords):
                metal_count += 1

        if metal_count >= 5:
            return 'STANDARD'
        else:
            return 'MINIMAL'

    def _identify_special_additives(self, ingredients: List[Dict], recipe: Dict) -> List[str]:
        """Identify special additives present."""
        additives = set()

        # Check for buffers
        buffer_keywords = ['buffer', 'phosphate', 'hepes', 'tris', 'carbonate', 'bicarbonate', 'mops', 'mes']
        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if any(buf in term for buf in buffer_keywords):
                additives.add('BUFFERED')
                break

        # Check for vitamins
        vitamin_keywords = ['vitamin', 'biotin', 'thiamine', 'riboflavin', 'cobalamin', 'cyanocobalamin', 'niacin']
        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if any(vit in term for vit in vitamin_keywords):
                additives.add('VITAMIN_SUPPLEMENTED')
                break

        # Check for selective agents
        selective_keywords = ['antibiotic', 'ampicillin', 'kanamycin', 'tetracycline', 'chloramphenicol', 'streptomycin', 'dye', 'crystal violet']
        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if any(sel in term for sel in selective_keywords):
                additives.add('SELECTIVE_AGENTS')
                break

        # Check for redox indicators
        redox_keywords = ['resazurin', 'methylene blue', 'indicator']
        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if any(red in term for red in redox_keywords):
                additives.add('REDOX_INDICATOR')
                break

        # Check for solidifying agents
        if recipe.get('physical_state') in ('SOLID_AGAR', 'SEMISOLID'):
            additives.add('SOLIDIFYING_AGENT')

        return sorted(list(additives))

    def _has_undefined_components(self, ingredients: List[Dict]) -> bool:
        """Check if recipe contains undefined components."""
        undefined_keywords = ['peptone', 'yeast extract', 'malt extract', 'beef extract', 'soil extract', 'tryptone', 'casein hydrolysate']

        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if any(keyword in term for keyword in undefined_keywords):
                return True

        return False

    def _is_high_salinity(self, ingredients: List[Dict]) -> bool:
        """Check if recipe has high salinity (>30 g/L NaCl)."""
        for ing in ingredients:
            term = ing.get('preferred_term', '').lower()
            if 'sodium chloride' in term or 'nacl' in term:
                conc = ing.get('concentration', {})
                value_str = conc.get('value', '0')
                unit = conc.get('unit', '')

                if unit in ('G_PER_L', 'g/L'):
                    try:
                        value = float(value_str)
                        if value >= self.salinity_threshold_marine:
                            return True
                    except (ValueError, TypeError):
                        pass

        return False

    def _has_low_salinity_indicators(self, recipe: Dict) -> bool:
        """Check for freshwater indicators."""
        name = recipe.get('name', '').lower()
        return any(keyword in name for keyword in ['freshwater', 'lake', 'river', 'pond'])

    def _calculate_confidence(self, recipe: Dict, taxonomy: Dict) -> float:
        """
        Calculate confidence score for taxonomy assignment.

        Args:
            recipe: Original recipe dict
            taxonomy: Assigned taxonomy dict

        Returns:
            Confidence score (0.0-1.0)
        """
        confidence = 0.0
        total_signals = 0

        # Domain confidence
        if recipe.get('medium_type'):
            confidence += 0.3
        total_signals += 0.3

        # Context confidence
        ingredients = recipe.get('ingredients', [])
        if ingredients:
            confidence += 0.2
        if recipe.get('ph_value'):
            confidence += 0.1
        if recipe.get('incubation_temperature'):
            confidence += 0.1
        total_signals += 0.4

        # Profile confidence
        if taxonomy['profile']['carbon_sources'] and taxonomy['profile']['carbon_sources'] != ['NONE']:
            confidence += 0.15
        if taxonomy['profile']['nitrogen_sources'] and taxonomy['profile']['nitrogen_sources'] != ['NONE']:
            confidence += 0.15
        total_signals += 0.3

        return min(confidence / total_signals if total_signals > 0 else 0.5, 1.0)
