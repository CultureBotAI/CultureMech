#!/usr/bin/env python3
"""
Migrate Solutions from Ingredients to Solutions Array

Scans all media YAML files and:
1. Identifies solution-like ingredients
2. Resolves them to the solution library
3. Moves them from `ingredients:` to `solutions:` array
4. Preserves all metadata and curation history

Patterns identified:
- Cross-references: "(see Medium [M###])"
- Explicit solutions: "Trace elements solution", "Vitamin solution"
- Solution markers: "*", "**", etc.

Usage:
    python scripts/migrate_solutions_from_ingredients.py [--dry-run] [--limit N]
"""

import json
import yaml
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any, Tuple
from collections import Counter
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class SolutionMigrator:
    """Migrate solutions from ingredients array to solutions array."""

    # Patterns that indicate an ingredient is likely a solution
    SOLUTION_PATTERNS = [
        r'(?i)solution',  # Contains "solution"
        r'(?i)see\s+medium\s+\[',  # Cross-reference
        r'(?i)trace.*element',  # Trace elements
        r'(?i)vitamin.*sol',  # Vitamin solution
        r'(?i)mineral.*sol',  # Mineral solution
        r'(?i)salt.*sol',  # Salt solution
        r'\*{1,3}$',  # Ends with asterisk markers
    ]

    # Pattern to extract medium reference from cross-reference
    MEDIUM_REF_PATTERN = r'(?i)\(see\s+medium\s+\[([^\]]+)\]\)'

    def __init__(
        self,
        media_dir: Path,
        solution_index_file: Path,
        dry_run: bool = False
    ):
        self.media_dir = Path(media_dir)
        self.solution_index_file = Path(solution_index_file)
        self.dry_run = dry_run

        self.stats = {
            'total_media': 0,
            'media_with_solutions': 0,
            'media_modified': 0,
            'solutions_migrated': 0,
            'cross_refs_found': 0,
            'cross_refs_resolved': 0,
            'solution_patterns': Counter(),
        }

        # Load solution index
        if solution_index_file.exists():
            with open(solution_index_file) as f:
                index_data = json.load(f)
                self.solution_index = index_data.get('solutions', {})
            logger.info(f"Loaded {len(self.solution_index)} solutions from index")
        else:
            logger.warning(f"Solution index not found: {solution_index_file}")
            self.solution_index = {}

        # Create reverse index by name
        self.solutions_by_name = {}
        for solution_id, solution_data in self.solution_index.items():
            name = solution_data.get('name', '').lower()
            self.solutions_by_name[name] = solution_id

    def _is_solution(self, ingredient: dict) -> bool:
        """
        Determine if an ingredient is actually a solution.

        Args:
            ingredient: IngredientDescriptor dictionary

        Returns:
            True if ingredient appears to be a solution
        """
        preferred_term = ingredient.get('preferred_term', '')

        # Check against patterns
        for pattern in self.SOLUTION_PATTERNS:
            if re.search(pattern, preferred_term):
                return True

        return False

    def _extract_medium_reference(self, text: str) -> Optional[str]:
        """
        Extract medium ID from cross-reference.

        Examples:
            "(see Medium [M278])" -> "M278"
            "(see Medium [M1745])" -> "M1745"

        Args:
            text: Text potentially containing reference

        Returns:
            Medium ID if found, None otherwise
        """
        match = re.search(self.MEDIUM_REF_PATTERN, text)
        if match:
            return match.group(1).strip()
        return None

    def _resolve_solution(self, ingredient: dict) -> Optional[Dict[str, Any]]:
        """
        Resolve an ingredient to a solution descriptor.

        Args:
            ingredient: Ingredient dictionary potentially representing a solution

        Returns:
            SolutionDescriptor dictionary if resolvable, None otherwise
        """
        preferred_term = ingredient.get('preferred_term', '')

        # Try to extract cross-reference
        medium_ref = self._extract_medium_reference(preferred_term)
        if medium_ref:
            self.stats['cross_refs_found'] += 1
            # For now, create a stub solution with the reference
            # Full resolution would require loading the referenced medium
            solution = {
                'preferred_term': preferred_term,
                'composition': [],  # Will be populated later
                'notes': f'Cross-reference to Medium {medium_ref}'
            }

            # Copy concentration if present
            if ingredient.get('concentration'):
                solution['concentration'] = ingredient['concentration']

            logger.debug(f"Cross-reference found: {medium_ref} in '{preferred_term}'")
            return solution

        # Try to match by name in solution index
        clean_name = re.sub(r'\*+$', '', preferred_term).strip().lower()

        if clean_name in self.solutions_by_name:
            solution_id = self.solutions_by_name[clean_name]
            solution_data = self.solution_index[solution_id]

            self.stats['cross_refs_resolved'] += 1

            solution = {
                'preferred_term': preferred_term,
                'term': {
                    'id': solution_id,
                    'label': solution_data['name']
                }
            }

            # Copy concentration from ingredient
            if ingredient.get('concentration'):
                solution['concentration'] = ingredient['concentration']

            # Add reference to full definition
            solution['notes'] = f'See {solution_data["filename"]} for composition'

            logger.debug(f"Resolved '{clean_name}' to {solution_id}")
            return solution

        # Create stub for unresolved solutions
        solution = {
            'preferred_term': preferred_term,
            'composition': []
        }

        # Copy concentration if present
        if ingredient.get('concentration'):
            solution['concentration'] = ingredient['concentration']

        # Copy notes if present
        if ingredient.get('notes'):
            solution['notes'] = ingredient['notes']

        return solution

    def _migrate_media_file(self, media_file: Path) -> bool:
        """
        Migrate solutions in a single media file.

        Args:
            media_file: Path to media YAML file

        Returns:
            True if file was modified, False otherwise
        """
        try:
            with open(media_file) as f:
                media = yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load {media_file}: {e}")
            return False

        if not media or not isinstance(media, dict):
            return False

        # Get ingredients
        ingredients = media.get('ingredients', [])
        if not ingredients:
            return False

        # Separate solutions from regular ingredients
        regular_ingredients = []
        solutions = []

        for ingredient in ingredients:
            if self._is_solution(ingredient):
                # This is a solution - try to resolve it
                solution = self._resolve_solution(ingredient)
                if solution:
                    solutions.append(solution)
                    self.stats['solutions_migrated'] += 1

                    # Track pattern that matched
                    for pattern in self.SOLUTION_PATTERNS:
                        if re.search(pattern, ingredient.get('preferred_term', '')):
                            self.stats['solution_patterns'][pattern] += 1
                            break
            else:
                # Regular ingredient
                regular_ingredients.append(ingredient)

        # Check if any changes were made
        if not solutions:
            return False

        # Update media dictionary
        media['ingredients'] = regular_ingredients

        # Add or merge into solutions array
        existing_solutions = media.get('solutions', [])
        media['solutions'] = existing_solutions + solutions

        # Add curation history entry
        curation_entry = {
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'curator': 'solution-migrator-v1.0',
            'action': 'Migrated solutions from ingredients to solutions array',
            'notes': f'Moved {len(solutions)} solution(s) from ingredients'
        }

        curation_history = media.get('curation_history', [])
        curation_history.append(curation_entry)
        media['curation_history'] = curation_history

        # Write back to file
        if not self.dry_run:
            with open(media_file, 'w') as f:
                yaml.dump(
                    media,
                    f,
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True
                )

        self.stats['media_modified'] += 1
        logger.info(f"Migrated {len(solutions)} solutions from {media_file.name}")

        return True

    def migrate_all(self, limit: Optional[int] = None):
        """
        Migrate solutions in all media files.

        Args:
            limit: Maximum number of files to process (for testing)
        """
        logger.info(f"Scanning media directory: {self.media_dir}")

        # Find all YAML files recursively
        media_files = list(self.media_dir.rglob('*.yaml'))
        self.stats['total_media'] = len(media_files)

        if limit:
            media_files = media_files[:limit]
            logger.info(f"Processing first {limit} files")

        logger.info(f"Found {len(media_files)} media files")

        # Process each file
        for idx, media_file in enumerate(media_files):
            if (idx + 1) % 100 == 0:
                logger.info(f"Processed {idx + 1}/{len(media_files)} files...")

            modified = self._migrate_media_file(media_file)
            if modified:
                self.stats['media_with_solutions'] += 1

        logger.info(f"\nProcessing complete!")

    def print_stats(self):
        """Print migration statistics."""
        logger.info("\n" + "=" * 60)
        logger.info("Solution Migration Statistics")
        logger.info("=" * 60)
        logger.info(f"Total media files:           {self.stats['total_media']}")
        logger.info(f"Media with solutions:        {self.stats['media_with_solutions']}")
        logger.info(f"Media modified:              {self.stats['media_modified']}")
        logger.info(f"Solutions migrated:          {self.stats['solutions_migrated']}")
        logger.info(f"Cross-references found:      {self.stats['cross_refs_found']}")
        logger.info(f"Cross-references resolved:   {self.stats['cross_refs_resolved']}")
        logger.info("")
        logger.info("Solution patterns matched:")
        for pattern, count in self.stats['solution_patterns'].most_common():
            logger.info(f"  {pattern:40s} → {count:5d}")
        logger.info("=" * 60)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Migrate solutions from ingredients to solutions array"
    )
    parser.add_argument(
        '--media-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory containing media YAML files'
    )
    parser.add_argument(
        '--solution-index',
        type=Path,
        default=Path('data/normalized_yaml/solutions/mediadive_solution_index.json'),
        help='Solution index JSON file'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of files to process (for testing)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview without writing files'
    )

    args = parser.parse_args()

    # Verify media directory exists
    if not args.media_dir.exists():
        logger.error(f"Media directory not found: {args.media_dir}")
        return 1

    # Create migrator
    migrator = SolutionMigrator(
        media_dir=args.media_dir,
        solution_index_file=args.solution_index,
        dry_run=args.dry_run
    )

    # Migrate solutions
    migrator.migrate_all(limit=args.limit)

    # Print statistics
    migrator.print_stats()

    if args.dry_run:
        logger.info("\n🔍 DRY RUN - No files were modified")
    else:
        logger.info(f"\n✓ Migration complete!")

    return 0


if __name__ == '__main__':
    exit(main())
