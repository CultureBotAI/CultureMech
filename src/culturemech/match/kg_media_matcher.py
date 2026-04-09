"""
KG-Microbe Media Matcher

Matches CultureMech recipes against KG-Microbe mediadive media based on ingredient composition.
Handles hierarchical ingredient specifications (commercial products vs. detailed breakdowns).

Key Features:
1. Load KG-Microbe mediadive graph data (edges.tsv, nodes.tsv)
2. Traverse medium→solution→ingredient relationships
3. Extract and normalize CHEBI/FOODON ingredient IDs
4. Compare CultureMech recipes with KG-Microbe media formulations
5. Handle abstraction level differences (commercial products vs constituent chemicals)
"""

import logging
from pathlib import Path
from typing import Dict, Set, List, Tuple, Optional, Any
from collections import defaultdict
import yaml

logger = logging.getLogger(__name__)


class KGMediaMatcher:
    """Match CultureMech recipes with KG-Microbe mediadive media."""

    def __init__(self, kg_microbe_dir: Path):
        """
        Initialize the matcher.

        Args:
            kg_microbe_dir: Path to kg-microbe repository root
                           (e.g., /path/to/kg-microbe/)

        Raises:
            FileNotFoundError: If edges.tsv or nodes.tsv not found
        """
        self.kg_microbe_dir = Path(kg_microbe_dir)
        self.mediadive_dir = self.kg_microbe_dir / "data" / "transformed" / "mediadive"

        self.edges_file = self.mediadive_dir / "edges.tsv"
        self.nodes_file = self.mediadive_dir / "nodes.tsv"

        # Indexes
        self.medium_ingredients: Dict[str, Set[str]] = {}  # medium_id -> set of CHEBI/FOODON IDs
        self.medium_names: Dict[str, str] = {}  # medium_id -> name
        self.solution_ingredients: Dict[str, Set[str]] = {}  # solution_id -> set of ingredient IDs
        self.ingredient_labels: Dict[str, str] = {}  # ingredient_id -> label

        # Load data
        self._load_kg_microbe_data()

    def _load_kg_microbe_data(self):
        """
        Load KG-Microbe mediadive nodes and edges.

        Builds indexes for:
        - Medium names
        - Medium -> Solution relationships
        - Solution -> Ingredient relationships
        - Aggregated Medium -> Ingredient mappings
        """
        if not self.edges_file.exists() or not self.nodes_file.exists():
            raise FileNotFoundError(
                f"KG-Microbe mediadive data not found at {self.mediadive_dir}. "
                f"Expected edges.tsv and nodes.tsv. "
                f"Please ensure kg-microbe repository is cloned and data is transformed."
            )

        logger.info(f"Loading KG-Microbe data from {self.mediadive_dir}")

        # Load nodes for medium names and ingredient labels
        with open(self.nodes_file) as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 2:
                    continue

                node_id = parts[0]
                name = parts[1] if len(parts) > 1 and parts[1] else parts[2] if len(parts) > 2 else ""

                if node_id.startswith('mediadive.medium:'):
                    medium_id = node_id.replace('mediadive.medium:', '')
                    self.medium_names[medium_id] = name
                elif node_id.startswith('CHEBI:') or node_id.startswith('FOODON:'):
                    self.ingredient_labels[node_id] = name

        logger.info(f"Loaded {len(self.medium_names)} media names")
        logger.info(f"Loaded {len(self.ingredient_labels)} ingredient labels")

        # First pass: find medium -> solution relationships
        medium_solutions = defaultdict(set)

        with open(self.edges_file) as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 3:
                    continue

                subject = parts[0]
                predicate = parts[1]
                obj = parts[2]

                # Find has_part edges from media to solutions
                if predicate == 'biolink:has_part' and subject.startswith('mediadive.medium:'):
                    medium_id = subject.replace('mediadive.medium:', '')
                    if obj.startswith('mediadive.solution:'):
                        solution_id = obj.replace('mediadive.solution:', '')
                        medium_solutions[medium_id].add(solution_id)

        logger.info(f"Found solution relationships for {len(medium_solutions)} media")

        # Second pass: find solution -> ingredient relationships
        with open(self.edges_file) as f:
            for line in f:
                parts = line.strip().split('\t')
                if len(parts) < 3:
                    continue

                subject = parts[0]
                predicate = parts[1]
                obj = parts[2]

                # Find has_part edges from solutions to ingredients
                if predicate == 'biolink:has_part' and subject.startswith('mediadive.solution:'):
                    solution_id = subject.replace('mediadive.solution:', '')

                    # Check if this solution belongs to any tracked medium
                    is_relevant = any(solution_id in sols for sols in medium_solutions.values())

                    if is_relevant:
                        if solution_id not in self.solution_ingredients:
                            self.solution_ingredients[solution_id] = set()

                        # Add CHEBI or FOODON IDs (skip mediadive internal IDs and nested solutions)
                        if obj.startswith('CHEBI:') or obj.startswith('FOODON:'):
                            normalized_id = self._normalize_ontology_id(obj)
                            self.solution_ingredients[solution_id].add(normalized_id)

        logger.info(f"Found ingredients for {len(self.solution_ingredients)} solutions")

        # Aggregate ingredients for each medium
        for medium_id, solutions in medium_solutions.items():
            self.medium_ingredients[medium_id] = set()
            for solution_id in solutions:
                if solution_id in self.solution_ingredients:
                    self.medium_ingredients[medium_id].update(self.solution_ingredients[solution_id])

        logger.info(f"Aggregated ingredients for {len(self.medium_ingredients)} media")

        # Log summary stats
        if self.medium_ingredients:
            ingredient_counts = [len(ings) for ings in self.medium_ingredients.values()]
            avg_ingredients = sum(ingredient_counts) / len(ingredient_counts)
            logger.info(f"Average ingredients per medium: {avg_ingredients:.1f}")

    def _normalize_ontology_id(self, ont_id: str) -> str:
        """
        Normalize ontology IDs (remove leading zeros).

        Args:
            ont_id: Raw ontology ID (e.g., CHEBI:0000178, FOODON:03302071)

        Returns:
            Normalized ID (e.g., CHEBI:178, FOODON:3302071)

        Examples:
            >>> matcher._normalize_ontology_id("CHEBI:0000178")
            "CHEBI:178"
            >>> matcher._normalize_ontology_id("FOODON:03302071")
            "FOODON:3302071"
        """
        if ont_id.startswith('CHEBI:'):
            try:
                num = int(ont_id.replace('CHEBI:', ''))
                return f'CHEBI:{num}'
            except ValueError:
                return ont_id
        elif ont_id.startswith('FOODON:'):
            try:
                num = int(ont_id.replace('FOODON:', ''))
                return f'FOODON:{num}'
            except ValueError:
                return ont_id
        return ont_id

    def extract_recipe_ingredients(self, recipe_file: Path) -> Set[str]:
        """
        Extract ingredient CHEBI/FOODON IDs from a CultureMech recipe YAML.

        Supports both:
        - MediaRecipe format (ingredients field)
        - SolutionDescriptor format (composition field)

        Args:
            recipe_file: Path to recipe YAML file

        Returns:
            Set of normalized ontology IDs

        Examples:
            Extracts from ingredients:
            ```yaml
            ingredients:
              - preferred_term: "Glucose"
                term:
                  id: "CHEBI:42758"
            ```

            Extracts from composition:
            ```yaml
            composition:
              - preferred_term: "NaCl"
                chebi_term:
                  id: "CHEBI:26710"
            ```
        """
        with open(recipe_file) as f:
            data = yaml.safe_load(f)

        ingredients = set()

        # Extract from ingredients field (MediaRecipe format)
        if 'ingredients' in data:
            for ing in data['ingredients']:
                if isinstance(ing, dict) and 'term' in ing:
                    term = ing['term']
                    if isinstance(term, dict) and 'id' in term:
                        ont_id = term['id']
                        if ont_id and (ont_id.startswith('CHEBI:') or ont_id.startswith('FOODON:')):
                            ingredients.add(ont_id)

        # Extract from composition field (SolutionDescriptor format)
        if 'composition' in data:
            for comp in data['composition']:
                if isinstance(comp, dict):
                    # Check chebi_term field
                    if 'chebi_term' in comp and isinstance(comp['chebi_term'], dict):
                        chebi_id = comp['chebi_term'].get('id')
                        if chebi_id and chebi_id.startswith('CHEBI:'):
                            ingredients.add(chebi_id)

                    # Check term field
                    if 'term' in comp and isinstance(comp['term'], dict):
                        term_id = comp['term'].get('id')
                        if term_id and (term_id.startswith('CHEBI:') or term_id.startswith('FOODON:')):
                            ingredients.add(term_id)

        return ingredients

    def find_matches(
        self,
        recipe_ingredients: Set[str],
        min_jaccard: float = 0.5,
        max_results: int = 10
    ) -> List[Tuple[str, float, int, int, int]]:
        """
        Find KG-Microbe media matching recipe ingredients.

        Args:
            recipe_ingredients: Set of CHEBI/FOODON IDs from recipe
            min_jaccard: Minimum Jaccard similarity (default 0.5)
            max_results: Maximum number of matches to return

        Returns:
            List of (medium_id, jaccard_score, shared_count, recipe_total, kg_total) tuples,
            sorted by Jaccard similarity (highest first)

        Examples:
            >>> matcher.find_matches({'CHEBI:26710', 'CHEBI:42758'}, min_jaccard=1.0)
            [('514', 1.0, 2, 2, 2)]  # Perfect match
        """
        matches = []

        for medium_id, kg_ingredients in self.medium_ingredients.items():
            # Compute Jaccard similarity
            intersection = recipe_ingredients & kg_ingredients
            union = recipe_ingredients | kg_ingredients

            if len(union) == 0:
                continue

            jaccard = len(intersection) / len(union)

            if jaccard >= min_jaccard:
                matches.append((
                    medium_id,
                    jaccard,
                    len(intersection),
                    len(recipe_ingredients),
                    len(kg_ingredients)
                ))

        # Sort by Jaccard (descending), then by shared count (descending)
        matches.sort(key=lambda x: (x[1], x[2]), reverse=True)

        return matches[:max_results]

    def find_exact_match(self, recipe_ingredients: Set[str]) -> Optional[str]:
        """
        Find exact ingredient match (Jaccard = 1.0) in KG-Microbe.

        Args:
            recipe_ingredients: Set of CHEBI/FOODON IDs from recipe

        Returns:
            medium_id if exact match found, None otherwise

        Note:
            Exact match means same ingredient set, ignoring concentrations.
            Handles cases where KG-Microbe uses commercial products
            (e.g., "Columbia agar base") vs. CultureMech detailed breakdowns.
        """
        matches = self.find_matches(recipe_ingredients, min_jaccard=1.0, max_results=1)

        if matches and matches[0][1] == 1.0:
            return matches[0][0]

        return None

    def get_medium_name(self, medium_id: str) -> str:
        """
        Get human-readable name for a medium ID.

        Args:
            medium_id: Medium ID (e.g., "514", "693")

        Returns:
            Medium name or "Medium {id}" if not found
        """
        return self.medium_names.get(medium_id, f"Medium {medium_id}")

    def get_medium_ingredients(self, medium_id: str) -> Set[str]:
        """
        Get ingredient set for a medium ID.

        Args:
            medium_id: Medium ID (e.g., "514", "693")

        Returns:
            Set of CHEBI/FOODON IDs, or empty set if not found
        """
        return self.medium_ingredients.get(medium_id, set())

    def compare_recipes(
        self,
        recipe1_ingredients: Set[str],
        recipe2_ingredients: Set[str]
    ) -> Tuple[float, Set[str], Set[str], Set[str]]:
        """
        Compare two recipes by ingredient overlap.

        Args:
            recipe1_ingredients: Ingredient set from first recipe
            recipe2_ingredients: Ingredient set from second recipe

        Returns:
            Tuple of (jaccard, shared, recipe1_only, recipe2_only)

        Examples:
            >>> matcher.compare_recipes({'CHEBI:1', 'CHEBI:2'}, {'CHEBI:2', 'CHEBI:3'})
            (0.333, {'CHEBI:2'}, {'CHEBI:1'}, {'CHEBI:3'})
        """
        intersection = recipe1_ingredients & recipe2_ingredients
        union = recipe1_ingredients | recipe2_ingredients

        jaccard = len(intersection) / len(union) if len(union) > 0 else 0.0

        recipe1_only = recipe1_ingredients - recipe2_ingredients
        recipe2_only = recipe2_ingredients - recipe1_ingredients

        return jaccard, intersection, recipe1_only, recipe2_only

    def generate_match_report(
        self,
        recipe_file: Path,
        top_n: int = 5
    ) -> Dict[str, Any]:
        """
        Generate comprehensive match report for a recipe.

        Args:
            recipe_file: Path to CultureMech recipe YAML
            top_n: Number of top matches to include

        Returns:
            Dictionary with match results and statistics
        """
        recipe_ingredients = self.extract_recipe_ingredients(recipe_file)

        if not recipe_ingredients:
            return {
                'recipe': str(recipe_file),
                'error': 'No ingredients found in recipe',
                'ingredient_count': 0
            }

        matches = self.find_matches(recipe_ingredients, min_jaccard=0.0, max_results=top_n)

        exact_match = matches[0][0] if matches and matches[0][1] == 1.0 else None

        report = {
            'recipe': str(recipe_file),
            'ingredient_count': len(recipe_ingredients),
            'exact_match': exact_match,
            'exact_match_name': self.get_medium_name(exact_match) if exact_match else None,
            'top_matches': []
        }

        for medium_id, jaccard, shared, recipe_total, kg_total in matches:
            report['top_matches'].append({
                'medium_id': medium_id,
                'medium_name': self.get_medium_name(medium_id),
                'jaccard_similarity': jaccard,
                'shared_ingredients': shared,
                'recipe_ingredients': recipe_total,
                'kg_ingredients': kg_total,
                'is_exact': jaccard == 1.0
            })

        return report


def match_recipe_to_kg_microbe(
    recipe_file: Path,
    kg_microbe_dir: Path,
    min_jaccard: float = 1.0
) -> Optional[str]:
    """
    Convenience function: Match a single recipe to KG-Microbe.

    Args:
        recipe_file: Path to CultureMech recipe YAML
        kg_microbe_dir: Path to kg-microbe repository root
        min_jaccard: Minimum Jaccard similarity (default 1.0 = exact)

    Returns:
        mediadive.medium:XXX ID if match found, None otherwise

    Examples:
        >>> match_recipe_to_kg_microbe(
        ...     Path("recipe.yaml"),
        ...     Path("/path/to/kg-microbe"),
        ...     min_jaccard=1.0
        ... )
        "mediadive.medium:514"
    """
    matcher = KGMediaMatcher(kg_microbe_dir)

    recipe_ingredients = matcher.extract_recipe_ingredients(recipe_file)

    if not recipe_ingredients:
        logger.warning(f"No ingredients found in {recipe_file}")
        return None

    if min_jaccard == 1.0:
        # Use optimized exact match
        exact_match = matcher.find_exact_match(recipe_ingredients)
        if exact_match:
            return f"mediadive.medium:{exact_match}"
    else:
        # Use general matching
        matches = matcher.find_matches(recipe_ingredients, min_jaccard=min_jaccard, max_results=1)
        if matches:
            return f"mediadive.medium:{matches[0][0]}"

    return None
