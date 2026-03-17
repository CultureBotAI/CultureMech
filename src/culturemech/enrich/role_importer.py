"""Import ingredient role assignments from MediaIngredientMech."""

import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

logger = logging.getLogger(__name__)


class RoleImporter:
    """Import ingredient role assignments from MediaIngredientMech."""

    def __init__(self, mim_repo_path: Path):
        """
        Initialize role importer.

        Args:
            mim_repo_path: Path to MediaIngredientMech repository
        """
        self.repo_path = mim_repo_path
        self.roles: Dict[str, List[str]] = {}
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'ingredients_assigned': 0,
            'roles_assigned': 0,
            'already_has_role': 0,
            'no_mim_id': 0,
            'no_roles_found': 0,
            'errors': 0
        }

    def load_roles(self) -> Dict[str, List[str]]:
        """
        Load role assignments from MediaIngredientMech.

        Returns:
            Dictionary mapping MediaIngredientMech ID to list of roles
            Example:
                {
                    'MediaIngredientMech:000042': ['MINERAL', 'SALT'],
                    'MediaIngredientMech:000067': ['MINERAL'],
                    ...
                }
        """
        logger.info("Loading role assignments from MediaIngredientMech...")

        roles_file = self.repo_path / "ingredient_roles.yaml"
        if not roles_file.exists():
            logger.warning(f"Roles file not found: {roles_file}")
            return {}

        with open(roles_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not data:
            logger.warning("Empty roles file")
            return {}

        # Parse roles structure
        # Expected format:
        # roles:
        #   MediaIngredientMech:000042:
        #     - MINERAL
        #     - SALT
        #   MediaIngredientMech:000067:
        #     - MINERAL

        if 'roles' in data:
            self.roles = data['roles']
        else:
            self.roles = data

        logger.info(f"Loaded roles for {len(self.roles)} ingredients")

        # Count total roles
        total_roles = sum(len(role_list) for role_list in self.roles.values())
        logger.info(f"Total role assignments: {total_roles}")

        return self.roles

    def get_roles_for_ingredient(self, mim_id: str) -> List[str]:
        """
        Get roles for a specific MediaIngredientMech ID.

        Args:
            mim_id: MediaIngredientMech ID

        Returns:
            List of role strings (e.g., ['MINERAL', 'SALT'])
        """
        return self.roles.get(mim_id, [])

    def apply_roles_to_ingredient(
        self,
        ingredient: Dict[str, Any],
        inherit_from_parent: bool = True
    ) -> bool:
        """
        Add role field to ingredient based on MediaIngredientMech roles.

        Priority:
        1. Direct role assignment for this ingredient
        2. Inherited from parent (if inherit_from_parent=True)

        Args:
            ingredient: Ingredient descriptor dict
            inherit_from_parent: Whether to inherit roles from parent

        Returns:
            True if roles were added, False otherwise
        """
        # Skip if already has role field
        if 'role' in ingredient:
            self.stats['already_has_role'] += 1
            return False

        # Get MediaIngredientMech ID
        mim_term = ingredient.get('mediaingredientmech_term')
        if not mim_term:
            self.stats['no_mim_id'] += 1
            return False

        mim_id = mim_term.get('id') if isinstance(mim_term, dict) else None
        if not mim_id:
            self.stats['no_mim_id'] += 1
            return False

        # Try to get direct roles
        roles = self.get_roles_for_ingredient(mim_id)

        # If no direct roles, try to inherit from parent
        if not roles and inherit_from_parent:
            parent_ingredient = ingredient.get('parent_ingredient')
            if parent_ingredient:
                parent_id = parent_ingredient.get('mediaingredientmech_id')
                if parent_id:
                    roles = self.get_roles_for_ingredient(parent_id)

        if not roles:
            self.stats['no_roles_found'] += 1
            return False

        # Add role field
        ingredient['role'] = roles

        self.stats['ingredients_assigned'] += 1
        self.stats['roles_assigned'] += len(roles)

        return True

    def apply_roles_to_recipe(
        self,
        recipe_path: Path,
        dry_run: bool = False,
        inherit_from_parent: bool = True
    ) -> bool:
        """
        Apply roles to all ingredients in a recipe.

        Args:
            recipe_path: Path to recipe YAML file
            dry_run: If True, don't save changes
            inherit_from_parent: Whether to inherit roles from parent

        Returns:
            True if file was modified, False otherwise
        """
        try:
            with open(recipe_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data:
                return False

            modified = False

            # Process direct ingredients
            ingredients = data.get('ingredients', [])
            if isinstance(ingredients, list):
                for ingredient in ingredients:
                    if isinstance(ingredient, dict):
                        if self.apply_roles_to_ingredient(ingredient, inherit_from_parent):
                            modified = True

            # Process solution ingredients
            solutions = data.get('solutions', [])
            if isinstance(solutions, list):
                for solution in solutions:
                    if isinstance(solution, dict):
                        composition = solution.get('composition', [])
                        if isinstance(composition, list):
                            for ingredient in composition:
                                if isinstance(ingredient, dict):
                                    if self.apply_roles_to_ingredient(ingredient, inherit_from_parent):
                                        modified = True

            # Add curation history if modified
            if modified and not dry_run:
                if 'curation_history' not in data:
                    data['curation_history'] = []

                data['curation_history'].append({
                    'timestamp': time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
                    'curator': 'role-assignment-v1.0',
                    'action': 'Added ingredient roles from MediaIngredientMech',
                    'notes': f'Assigned functional roles (inherit_from_parent={inherit_from_parent})'
                })

                # Save updated file
                with open(recipe_path, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                logger.debug(f"  ✓ Updated {recipe_path.name}")

            if modified:
                self.stats['files_modified'] += 1

            self.stats['files_processed'] += 1
            return modified

        except Exception as e:
            logger.error(f"  ✗ Failed to process {recipe_path.name}: {e}")
            self.stats['errors'] += 1
            return False

    def run_pipeline(
        self,
        yaml_dir: Path,
        category: Optional[str] = None,
        limit: Optional[int] = None,
        dry_run: bool = False,
        inherit_from_parent: bool = True
    ) -> Dict[str, Any]:
        """
        Apply roles to all recipes.

        Args:
            yaml_dir: Directory containing normalized YAML files
            category: Optional category filter
            limit: Optional limit on number of files
            dry_run: If True, don't save changes
            inherit_from_parent: Whether to inherit roles from parent

        Returns:
            Dictionary with statistics
        """
        logger.info("=" * 60)
        logger.info("Ingredient Role Assignment Pipeline")
        logger.info("=" * 60)

        if dry_run:
            logger.info("DRY RUN MODE - no files will be modified")

        logger.info(f"Roles loaded: {len(self.roles)} ingredients")
        logger.info(f"Inherit from parent: {inherit_from_parent}")

        # Find recipe files
        if category:
            pattern = f"{category}/**/*.yaml"
            logger.info(f"Processing category: {category}")
        else:
            pattern = "**/*.yaml"
            logger.info("Processing all categories")

        yaml_files = list(yaml_dir.glob(pattern))
        logger.info(f"Found {len(yaml_files)} recipe files")

        if limit:
            yaml_files = yaml_files[:limit]
            logger.info(f"Limited to {limit} files for testing")

        # Process files
        for i, yaml_file in enumerate(yaml_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(yaml_files)} files processed...")

            self.apply_roles_to_recipe(yaml_file, dry_run, inherit_from_parent)

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Role Assignment Complete")
        logger.info("=" * 60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Files modified: {self.stats['files_modified']}")
        logger.info(f"Ingredients assigned roles: {self.stats['ingredients_assigned']}")
        logger.info(f"Total roles assigned: {self.stats['roles_assigned']}")
        logger.info(f"Already has role (skipped): {self.stats['already_has_role']}")
        logger.info(f"No MediaIngredientMech ID: {self.stats['no_mim_id']}")
        logger.info(f"No roles found: {self.stats['no_roles_found']}")

        if self.stats['errors'] > 0:
            logger.warning(f"Errors: {self.stats['errors']}")

        # Calculate coverage
        total_potential = (
            self.stats['ingredients_assigned'] +
            self.stats['no_roles_found']
        )
        if total_potential > 0:
            coverage = (self.stats['ingredients_assigned'] / total_potential) * 100
            logger.info(f"Role coverage: {coverage:.1f}% "
                       f"({self.stats['ingredients_assigned']}/{total_potential})")

        logger.info("=" * 60)

        return {'stats': self.stats}
