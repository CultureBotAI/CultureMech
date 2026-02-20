"""Build cross-references between multiple media databases.

Creates mappings between:
- TOGO ↔ DSMZ/MediaDive
- JCM ↔ DSMZ
- NBRC ↔ DSMZ
- ATCC ↔ All databases
- KOMODO ↔ MediaDive

Uses name similarity, ingredient fingerprinting, and known patterns.
"""

import json
import logging
import re
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MultiDatabaseCrossRef:
    """Build cross-references across multiple media databases."""

    def __init__(self):
        """Initialize cross-reference builder."""
        self.media_by_source = defaultdict(dict)  # {source: {id: metadata}}
        self.crossrefs = defaultdict(dict)  # {source_id: {target_source: target_id}}

        # Minimum similarity thresholds for different matching strategies
        self.NAME_SIMILARITY_THRESHOLD = 0.85
        self.INGREDIENT_SIMILARITY_THRESHOLD = 0.75

    def load_media_files(self, yaml_dir: Path):
        """
        Load all media files and organize by source database.

        Args:
            yaml_dir: Directory containing YAML files
        """
        logger.info("Loading media files...")

        patterns = {
            "DSMZ": "DSMZ_*.yaml",
            "TOGO": "TOGO_*.yaml",
            "JCM": "JCM_*.yaml",
            "NBRC": "NBRC_*.yaml",
            "ATCC": "ATCC_*.yaml",
            "KOMODO": "KOMODO_*.yaml",
            "MEDIADB": "MEDIADB_*.yaml",
        }

        for source, pattern in patterns.items():
            files = list(yaml_dir.glob(f"**/{pattern}"))
            logger.info(f"  Loading {len(files)} {source} files...")

            for yaml_file in files:
                try:
                    with open(yaml_file, 'r', encoding='utf-8') as f:
                        data = yaml.safe_load(f)

                    # Extract ID from filename or media_term
                    media_id = self._extract_media_id(yaml_file, data, source)
                    if not media_id:
                        continue

                    self.media_by_source[source][media_id] = {
                        "name": data.get("name", ""),
                        "original_name": data.get("original_name", ""),
                        "ingredients": self._extract_ingredient_names(data),
                        "medium_type": data.get("medium_type", ""),
                        "category": data.get("category", ""),
                        "file_path": str(yaml_file)
                    }

                except Exception as e:
                    logger.warning(f"Failed to load {yaml_file}: {e}")
                    continue

        total = sum(len(media) for media in self.media_by_source.values())
        logger.info(f"Loaded {total} total media files from {len(self.media_by_source)} sources")

    def _extract_media_id(self, yaml_file: Path, data: Dict, source: str) -> Optional[str]:
        """Extract media ID from filename or data."""
        # Try filename pattern first
        patterns = {
            "DSMZ": r'DSMZ_(\d+[a-z]?)_',
            "TOGO": r'TOGO_M(\d+)_',
            "JCM": r'JCM_(\d+)_',
            "NBRC": r'NBRC_(\d+)_',
            "ATCC": r'ATCC_(\d+)_',
            "KOMODO": r'KOMODO_(\d+)_',
            "MEDIADB": r'MEDIADB_(\d+)_',
        }

        if source in patterns:
            match = re.search(patterns[source], yaml_file.stem)
            if match:
                return match.group(1)

        # Try media_term field
        media_term = data.get("media_term", {}).get("term", {})
        if media_term.get("id"):
            term_id = media_term["id"]
            # Extract numeric ID from various formats
            match = re.search(r':([^:]+)$', term_id)
            if match:
                return match.group(1)

        return None

    def _extract_ingredient_names(self, data: Dict) -> List[str]:
        """Extract normalized ingredient names for comparison."""
        ingredients = []
        for ing in data.get("ingredients", []):
            name = ing.get("preferred_term", "").upper().strip()
            if name:
                ingredients.append(name)
        return sorted(ingredients)

    def normalize_name(self, name: str) -> str:
        """Normalize media name for comparison."""
        normalized = name.upper().strip()

        # Remove common prefixes/suffixes
        normalized = re.sub(r'^(DSMZ|TOGO|JCM|NBRC|ATCC|KOMODO|MEDIADB)\s+MEDIUM\s+\d+:?\s*', '', normalized)
        normalized = re.sub(r'\s+(AGAR|BROTH|MEDIUM)$', '', normalized)
        normalized = re.sub(r'\s+', ' ', normalized)

        return normalized

    def name_similarity(self, name1: str, name2: str) -> float:
        """Calculate similarity between two media names."""
        norm1 = self.normalize_name(name1)
        norm2 = self.normalize_name(name2)
        return SequenceMatcher(None, norm1, norm2).ratio()

    def ingredient_similarity(self, ing1: List[str], ing2: List[str]) -> float:
        """
        Calculate Jaccard similarity between ingredient lists.

        Args:
            ing1: First ingredient list
            ing2: Second ingredient list

        Returns:
            Similarity score (0.0 to 1.0)
        """
        if not ing1 or not ing2:
            return 0.0

        set1 = set(ing1)
        set2 = set(ing2)

        intersection = len(set1 & set2)
        union = len(set1 | set2)

        return intersection / union if union > 0 else 0.0

    def find_cross_references(
        self,
        source1: str,
        source2: str,
        min_name_similarity: Optional[float] = None,
        min_ingredient_similarity: Optional[float] = None
    ) -> List[Dict[str, Any]]:
        """
        Find cross-references between two databases.

        Args:
            source1: First database (e.g., "TOGO")
            source2: Second database (e.g., "DSMZ")
            min_name_similarity: Minimum name similarity (default: 0.85)
            min_ingredient_similarity: Minimum ingredient similarity (default: 0.75)

        Returns:
            List of candidate cross-references
        """
        if min_name_similarity is None:
            min_name_similarity = self.NAME_SIMILARITY_THRESHOLD
        if min_ingredient_similarity is None:
            min_ingredient_similarity = self.INGREDIENT_SIMILARITY_THRESHOLD

        if source1 not in self.media_by_source or source2 not in self.media_by_source:
            logger.warning(f"Source {source1} or {source2} not loaded")
            return []

        logger.info(f"Finding {source1} ↔ {source2} cross-references...")

        candidates = []

        for id1, media1 in self.media_by_source[source1].items():
            for id2, media2 in self.media_by_source[source2].items():
                # Name similarity
                name_sim = self.name_similarity(media1["name"], media2["name"])

                # Ingredient similarity
                ing_sim = self.ingredient_similarity(
                    media1["ingredients"],
                    media2["ingredients"]
                )

                # Consider it a match if either name OR ingredients are very similar
                is_match = (
                    name_sim >= min_name_similarity or
                    ing_sim >= min_ingredient_similarity
                )

                if is_match:
                    # Calculate overall confidence
                    confidence_score = max(name_sim, ing_sim)

                    if name_sim >= 0.95 or ing_sim >= 0.90:
                        confidence = "high"
                    elif name_sim >= 0.85 or ing_sim >= 0.75:
                        confidence = "medium"
                    else:
                        confidence = "low"

                    candidates.append({
                        f"{source1}_id": id1,
                        f"{source2}_id": id2,
                        f"{source1}_name": media1["name"],
                        f"{source2}_name": media2["name"],
                        "name_similarity": round(name_sim, 3),
                        "ingredient_similarity": round(ing_sim, 3),
                        "confidence": confidence,
                        "verified": False,
                        "notes": ""
                    })

        # Sort by confidence
        candidates.sort(key=lambda x: max(x["name_similarity"], x["ingredient_similarity"]), reverse=True)

        logger.info(f"  Found {len(candidates)} {source1}↔{source2} candidates")
        return candidates

    def find_all_cross_references(self) -> Dict[str, List[Dict]]:
        """Find cross-references for all database pairs."""
        logger.info("Finding all cross-reference pairs...")

        all_refs = {}

        # Define database pairs to cross-reference
        pairs = [
            ("TOGO", "DSMZ"),
            ("JCM", "DSMZ"),
            ("NBRC", "DSMZ"),
            ("ATCC", "DSMZ"),
            ("ATCC", "TOGO"),
            ("KOMODO", "DSMZ"),
            ("MEDIADB", "DSMZ"),
        ]

        for source1, source2 in pairs:
            key = f"{source1}_{source2}"
            candidates = self.find_cross_references(source1, source2)
            if candidates:
                all_refs[key] = candidates

        return all_refs

    def export_candidates(self, output_file: Path, max_per_pair: int = 50):
        """
        Export cross-reference candidates for manual review.

        Args:
            output_file: Path to save JSON file
            max_per_pair: Maximum candidates per database pair
        """
        all_refs = self.find_all_cross_references()

        # Limit candidates per pair
        for key in all_refs:
            all_refs[key] = all_refs[key][:max_per_pair]

        total_candidates = sum(len(refs) for refs in all_refs.values())

        export_data = {
            "generated_date": "2026-02-19",
            "total_pairs": len(all_refs),
            "total_candidates": total_candidates,
            "pairs": all_refs
        }

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

        logger.info(f"\n✓ Exported {total_candidates} candidates to {output_file}")
        logger.info(f"  Database pairs: {len(all_refs)}")
        for key, refs in all_refs.items():
            high = sum(1 for r in refs if r["confidence"] == "high")
            logger.info(f"    {key}: {len(refs)} candidates ({high} high confidence)")

    def import_verified_candidates(
        self,
        candidates_file: Path,
        output_file: Path,
        dry_run: bool = False
    ):
        """
        Import verified cross-references from candidates file.

        Args:
            candidates_file: JSON file with verified candidates
            output_file: Where to save cross-reference database
            dry_run: If True, only show what would be added
        """
        with open(candidates_file, 'r') as f:
            data = json.load(f)

        # Load existing cross-references
        if output_file.exists():
            with open(output_file, 'r') as f:
                crossref_db = json.load(f)
        else:
            crossref_db = {}

        added_count = 0

        for pair_key, candidates in data["pairs"].items():
            for candidate in candidates:
                if not candidate.get("verified"):
                    continue

                source1, source2 = pair_key.split("_")
                id1 = str(candidate[f"{source1}_id"])
                id2 = str(candidate[f"{source2}_id"])

                # Create cross-reference key
                key = f"{source1}:{id1}"

                if dry_run:
                    logger.info(f"  Would add: {key} → {source2}:{id2}")
                    continue

                if key not in crossref_db:
                    crossref_db[key] = {}

                crossref_db[key][source2] = {
                    "id": id2,
                    "name": candidate[f"{source2}_name"],
                    "name_similarity": candidate["name_similarity"],
                    "ingredient_similarity": candidate["ingredient_similarity"],
                    "verified": True,
                    "verification_date": "2026-02-19"
                }

                added_count += 1
                logger.info(f"  ✓ Added: {key} → {source2}:{id2}")

        if not dry_run and added_count > 0:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(crossref_db, f, indent=2, ensure_ascii=False)

            logger.info(f"\n✓ Added {added_count} cross-references")
            logger.info(f"  Total entries: {len(crossref_db)}")
            logger.info(f"  Saved to: {output_file}")
        elif dry_run:
            logger.info(f"\nDRY RUN - would add {added_count} cross-references")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Build multi-database cross-references"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate candidates
    gen_parser = subparsers.add_parser("generate", help="Generate cross-reference candidates")
    gen_parser.add_argument(
        "-d", "--yaml-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Directory with YAML files (default: data/normalized_yaml)"
    )
    gen_parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("data/curation/multi_db_crossref_candidates.json"),
        help="Output candidates file"
    )
    gen_parser.add_argument(
        "-m", "--max-per-pair",
        type=int,
        default=50,
        help="Maximum candidates per database pair (default: 50)"
    )

    # Import verified
    imp_parser = subparsers.add_parser("import", help="Import verified cross-references")
    imp_parser.add_argument(
        "candidates_file",
        type=Path,
        help="Candidates JSON with verified=true entries"
    )
    imp_parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("data/processed/media_crossref_db.json"),
        help="Output cross-reference database file"
    )
    imp_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be added without modifying files"
    )

    args = parser.parse_args()

    builder = MultiDatabaseCrossRef()

    if args.command == "generate":
        builder.load_media_files(args.yaml_dir)
        builder.export_candidates(args.output, max_per_pair=args.max_per_pair)
    elif args.command == "import":
        builder.import_verified_candidates(
            args.candidates_file,
            args.output,
            dry_run=args.dry_run
        )


if __name__ == "__main__":
    main()
