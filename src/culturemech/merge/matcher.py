"""Recipe matching module for finding duplicates.

Groups recipes by fingerprint to identify duplicates with identical ingredients.
"""

from collections import defaultdict
from pathlib import Path
from typing import Dict, List

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter


class RecipeMatcher:
    """Match and group duplicate recipes based on ingredient fingerprints.

    Recipes with identical fingerprints have the same ingredient set
    and are candidates for merging.
    """

    def __init__(self):
        """Initialize the matcher with a fingerprinter."""
        self.fingerprinter = RecipeFingerprinter()

    def group_recipes(
        self,
        recipe_files: List[Path],
        min_group_size: int = 1,
        progress_callback=None
    ) -> Dict[str, List[Path]]:
        """Group recipes by fingerprint.

        Args:
            recipe_files: List of recipe YAML file paths
            min_group_size: Minimum group size to include in results (default: 1)
            progress_callback: Optional callback function called with (current, total)

        Returns:
            Dictionary mapping fingerprint -> list of recipe paths
            Only includes groups with at least min_group_size recipes

        Raises:
            ValueError: If any recipe is invalid
        """
        fingerprint_groups = defaultdict(list)
        total = len(recipe_files)
        skipped_no_fp = 0  # No fingerprint generated
        skipped_error = 0   # Error during processing
        skipped_reasons = defaultdict(int)

        for i, recipe_path in enumerate(recipe_files, 1):
            try:
                fingerprint = self.fingerprinter.fingerprint_file(recipe_path)

                # Skip recipes that can't be fingerprinted (no valid ingredients)
                if fingerprint is None:
                    skipped_no_fp += 1
                    skipped_reasons['no_valid_ingredients'] += 1
                    if progress_callback and i % 500 == 0:
                        progress_callback(i, total)
                    continue

                fingerprint_groups[fingerprint].append(recipe_path)

                if progress_callback and i % 500 == 0:
                    progress_callback(i, total)

            except ValueError as e:
                # Expected errors (no ingredients field, etc.)
                skipped_error += 1
                error_msg = str(e)
                if 'no ingredients' in error_msg.lower():
                    skipped_reasons['no_ingredients_field'] += 1
                else:
                    skipped_reasons['other_error'] += 1

                if progress_callback and i % 500 == 0:
                    progress_callback(i, total)
                continue

            except Exception as e:
                # Unexpected errors
                skipped_error += 1
                skipped_reasons['unexpected_error'] += 1
                if progress_callback and i % 500 == 0:
                    progress_callback(i, total)
                continue

        # Final progress update
        if progress_callback:
            progress_callback(total, total)

        # Store skip statistics as metadata
        self._last_skip_stats = {
            'total_processed': total,
            'skipped_no_fingerprint': skipped_no_fp,
            'skipped_error': skipped_error,
            'successfully_fingerprinted': len(fingerprint_groups),
            'reasons': dict(skipped_reasons)
        }

        # Filter by minimum group size
        if min_group_size > 1:
            fingerprint_groups = {
                fp: paths
                for fp, paths in fingerprint_groups.items()
                if len(paths) >= min_group_size
            }

        return dict(fingerprint_groups)

    def find_duplicates(
        self,
        recipe_files: List[Path],
        progress_callback=None
    ) -> Dict[str, List[Path]]:
        """Find duplicate recipes (groups with 2+ recipes).

        This is a convenience method that calls group_recipes with min_group_size=2.

        Args:
            recipe_files: List of recipe YAML file paths
            progress_callback: Optional callback function called with (current, total)

        Returns:
            Dictionary mapping fingerprint -> list of duplicate recipe paths

        Raises:
            ValueError: If any recipe is invalid
        """
        return self.group_recipes(
            recipe_files=recipe_files,
            min_group_size=2,
            progress_callback=progress_callback
        )

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

    def get_duplicate_stats(
        self,
        recipe_files: List[Path]
    ) -> Dict:
        """Generate statistics about duplicate recipes.

        Args:
            recipe_files: List of recipe YAML file paths

        Returns:
            Dictionary with statistics:
            - total_recipes: Total number of recipes
            - unique_recipes: Number of unique ingredient sets
            - duplicate_groups: Number of groups with 2+ recipes
            - total_duplicates: Total number of duplicate recipes
            - reduction: Number of recipes that would be removed
            - reduction_percentage: Percentage reduction
            - largest_group_size: Size of largest duplicate group
        """
        all_groups = self.group_recipes(recipe_files, min_group_size=1)
        duplicate_groups = {
            fp: paths
            for fp, paths in all_groups.items()
            if len(paths) >= 2
        }

        total_recipes = len(recipe_files)
        unique_recipes = len(all_groups)
        num_duplicate_groups = len(duplicate_groups)

        # Total duplicates = sum of (group_size - 1) for each duplicate group
        total_duplicates = sum(
            len(paths) - 1
            for paths in duplicate_groups.values()
        )

        reduction = total_duplicates
        reduction_percentage = (reduction / total_recipes * 100) if total_recipes > 0 else 0

        largest_group_size = max(
            (len(paths) for paths in all_groups.values()),
            default=0
        )

        return {
            'total_recipes': total_recipes,
            'unique_recipes': unique_recipes,
            'duplicate_groups': num_duplicate_groups,
            'total_duplicates': total_duplicates,
            'reduction': reduction,
            'reduction_percentage': round(reduction_percentage, 1),
            'largest_group_size': largest_group_size,
        }
