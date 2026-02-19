"""Recipe merger module for consolidating duplicates.

Merges duplicate recipes into canonical records with synonym tracking
and provenance preservation.
"""

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter


class RecipeMerger:
    """Merge duplicate recipes into canonical records.

    Consolidates recipes with identical ingredient sets by:
    - Selecting canonical name (most common)
    - Building synonyms list from non-canonical names
    - Merging categories into multivalued list
    - Preserving all unique information
    - Tracking provenance via merged_from field
    """

    # Source priority for tie-breaking (higher = preferred)
    SOURCE_PRIORITY = {
        'TOGO': 4,
        'MediaDive': 3,
        'KOMODO': 2,
        'DSMZ': 1,
    }

    def __init__(self):
        """Initialize the merger with a fingerprinter."""
        self.fingerprinter = RecipeFingerprinter()

    def merge_group(
        self,
        recipe_paths: List[Path],
        fingerprint: Optional[str] = None
    ) -> Dict:
        """Merge multiple recipes with identical ingredients.

        Args:
            recipe_paths: List of paths to duplicate recipes
            fingerprint: Optional pre-computed fingerprint (will compute if not provided)

        Returns:
            Merged recipe dictionary with:
            - Canonical name (most common)
            - All categories (multivalued)
            - Synonyms list
            - Merged ingredients (most complete version)
            - Provenance tracking

        Raises:
            ValueError: If recipe_paths is empty or recipes are invalid
        """
        if not recipe_paths:
            raise ValueError("Cannot merge empty recipe list")

        # Load all recipes
        recipes = []
        for path in recipe_paths:
            recipe = self._load_recipe(path)
            recipe['_source_path'] = path  # Track source for debugging
            recipes.append(recipe)

        # If only one recipe, return it as-is with merge metadata
        if len(recipes) == 1:
            merged = recipes[0].copy()
            del merged['_source_path']  # Remove internal field
            merged['merge_fingerprint'] = fingerprint or self.fingerprinter.fingerprint(merged)
            merged['merged_from'] = [self._extract_recipe_id(recipe_paths[0])]
            return merged

        # Select canonical recipe and name
        canonical_recipe, canonical_name = self._select_canonical(recipes)

        # Build merged recipe
        merged = canonical_recipe.copy()
        del merged['_source_path']  # Remove internal field

        # Update name if different
        merged['name'] = canonical_name
        if 'original_name' not in merged:
            merged['original_name'] = canonical_name

        # Build synonyms from non-canonical recipes
        synonyms = self._build_synonyms(recipes, canonical_name)
        if synonyms:
            merged['synonyms'] = synonyms

        # Merge categories (multivalued)
        categories = self._merge_categories(recipes)
        if categories:
            merged['categories'] = categories

        # Add merged_from tracking
        merged['merged_from'] = [
            self._extract_recipe_id(path)
            for path in recipe_paths
        ]

        # Add fingerprint
        merged['merge_fingerprint'] = fingerprint or self.fingerprinter.fingerprint(merged)

        # Merge ingredients (prefer most complete CHEBI annotations)
        merged['ingredients'] = self._merge_ingredients(recipes)

        # Add curation history entry
        self._add_merge_curation(merged, len(recipes))

        return merged

    def _load_recipe(self, path: Path) -> Dict:
        """Load recipe from YAML file.

        Args:
            path: Path to recipe YAML file

        Returns:
            Recipe dictionary

        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If YAML is invalid
        """
        if not path.exists():
            raise FileNotFoundError(f"Recipe file not found: {path}")

        try:
            with open(path, 'r', encoding='utf-8') as f:
                recipe = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Invalid YAML in {path}: {e}")

        if not isinstance(recipe, dict):
            raise ValueError(f"Recipe is not a dictionary: {path}")

        return recipe

    def _select_canonical(self, recipes: List[Dict]) -> tuple[Dict, str]:
        """Select canonical recipe and name.

        Priority:
        1. Most frequently occurring name
        2. Source priority (TOGO > MediaDive > KOMODO > DSMZ > others)
        3. Alphabetically first

        Args:
            recipes: List of recipe dictionaries

        Returns:
            Tuple of (canonical_recipe, canonical_name)
        """
        # Count name frequencies
        name_counts = Counter(recipe['name'] for recipe in recipes)

        # Find most common count
        max_count = max(name_counts.values())

        # Get all names with max count (for tie-breaking)
        top_names = [
            name for name, count in name_counts.items()
            if count == max_count
        ]

        # If single winner by frequency, use it
        if len(top_names) == 1:
            canonical_name = top_names[0]
        else:
            # Tie-break by source priority
            canonical_name = self._select_by_source_priority(recipes, top_names)

        # Find recipe with canonical name (prefer one with most complete annotations)
        canonical_candidates = [r for r in recipes if r['name'] == canonical_name]
        canonical_recipe = self._select_most_complete_recipe(canonical_candidates)

        return canonical_recipe, canonical_name

    def _select_by_source_priority(
        self,
        recipes: List[Dict],
        candidate_names: List[str]
    ) -> str:
        """Select name by source priority.

        Args:
            recipes: List of recipe dictionaries
            candidate_names: Names to choose from

        Returns:
            Selected name
        """
        # Map names to recipes
        name_to_recipe = {
            recipe['name']: recipe
            for recipe in recipes
            if recipe['name'] in candidate_names
        }

        # Score by source priority
        def get_priority(name: str) -> tuple[int, str]:
            recipe = name_to_recipe[name]
            source = self._extract_source(recipe)
            priority = self.SOURCE_PRIORITY.get(source, 0)
            return (priority, name)  # Return tuple for alphabetic tie-break

        # Sort by priority (descending) then alphabetically
        sorted_names = sorted(
            candidate_names,
            key=get_priority,
            reverse=True
        )

        return sorted_names[0]

    def _select_most_complete_recipe(self, recipes: List[Dict]) -> Dict:
        """Select recipe with most complete CHEBI annotations.

        Args:
            recipes: List of recipe dictionaries

        Returns:
            Most complete recipe
        """
        def completeness_score(recipe: Dict) -> int:
            """Count CHEBI terms in recipe."""
            score = 0
            for ingredient in recipe.get('ingredients', []):
                if ingredient.get('term', {}).get('id', '').startswith('CHEBI:'):
                    score += 1
            return score

        return max(recipes, key=completeness_score)

    def _extract_source(self, recipe: Dict) -> str:
        """Extract source database from recipe.

        Checks media_term.term.id for source prefix.

        Args:
            recipe: Recipe dictionary

        Returns:
            Source name (e.g., 'TOGO', 'MediaDive', 'KOMODO', 'DSMZ', 'unknown')
        """
        media_term = recipe.get('media_term', {})
        if isinstance(media_term, dict):
            term = media_term.get('term', {})
            if isinstance(term, dict):
                term_id = term.get('id', '')
                if 'TOGO:' in term_id:
                    return 'TOGO'
                elif 'mediadive.medium:' in term_id:
                    return 'MediaDive'
                elif 'komodo.medium:' in term_id:
                    return 'KOMODO'
                elif 'DSMZ' in term_id:
                    return 'DSMZ'

        return 'unknown'

    def _build_synonyms(
        self,
        recipes: List[Dict],
        canonical_name: str
    ) -> List[Dict]:
        """Build synonyms list from non-canonical recipes.

        Args:
            recipes: List of all recipe dictionaries
            canonical_name: The canonical name to exclude

        Returns:
            List of RecipeSynonym dictionaries
        """
        synonyms = []

        for recipe in recipes:
            name = recipe['name']
            if name == canonical_name:
                continue  # Skip canonical name

            source = self._extract_source(recipe)
            source_id = self._extract_source_id(recipe)
            category = recipe.get('category')

            synonym = {
                'name': name,
                'source': source,
            }

            if source_id:
                synonym['source_id'] = source_id

            if category:
                synonym['original_category'] = category

            synonyms.append(synonym)

        return synonyms

    def _extract_source_id(self, recipe: Dict) -> Optional[str]:
        """Extract source ID from recipe.

        Args:
            recipe: Recipe dictionary

        Returns:
            Source ID or None
        """
        media_term = recipe.get('media_term', {})
        if isinstance(media_term, dict):
            term = media_term.get('term', {})
            if isinstance(term, dict):
                return term.get('id')

        return None

    def _merge_categories(self, recipes: List[Dict]) -> List[str]:
        """Merge categories from all recipes into unique list.

        Args:
            recipes: List of recipe dictionaries

        Returns:
            Sorted list of unique categories
        """
        categories = set()

        for recipe in recipes:
            category = recipe.get('category')
            if category:
                categories.add(category)

        return sorted(categories)

    def _merge_ingredients(self, recipes: List[Dict]) -> List[Dict]:
        """Merge ingredients, preferring most complete CHEBI annotations.

        Since all recipes have identical ingredient sets (by fingerprint),
        we select the version with the most complete annotations.

        Args:
            recipes: List of recipe dictionaries

        Returns:
            Merged ingredients list
        """
        # Find recipe with most complete annotations
        best_recipe = self._select_most_complete_recipe(recipes)

        # Return its ingredients
        return best_recipe.get('ingredients', [])

    def _extract_recipe_id(self, path: Path) -> str:
        """Extract recipe ID from file path.

        Args:
            path: Path to recipe YAML file

        Returns:
            Recipe ID (filename without .yaml extension)
        """
        return path.stem

    def _add_merge_curation(self, recipe: Dict, merge_count: int) -> None:
        """Add curation history entry for merge operation.

        Args:
            recipe: Recipe dictionary to modify
            merge_count: Number of recipes merged
        """
        timestamp = datetime.now(timezone.utc).isoformat()

        curation_event = {
            'timestamp': timestamp,
            'curator': 'recipe-merger',
            'action': f'Merged {merge_count} duplicate recipes into canonical record',
            'notes': f"Sources: {', '.join(recipe.get('merged_from', []))}"
        }

        if 'curation_history' not in recipe:
            recipe['curation_history'] = []

        recipe['curation_history'].append(curation_event)
