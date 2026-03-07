"""Build ATCC cross-references by finding equivalencies with DSMZ media.

Searches for potential ATCC-DSMZ media matches based on:
- Name similarity
- Ingredient composition
- Known equivalencies from literature

Outputs candidates for manual verification.
"""

import json
import logging
import os
import re
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ATCCCrossReferenceBuilder:
    """
    Build ATCC-DSMZ cross-references using name matching and composition analysis.

    Since ATCC has no public API, we rely on:
    1. Known equivalencies from literature/documentation
    2. Name similarity matching
    3. Manual verification of candidates
    """

    # Known ATCC media names and common equivalencies from literature
    KNOWN_EQUIVALENCIES = {
        # Format: "atcc_id": {"dsmz": "dsmz_id", "name": "Medium Name"}
        "1": {"dsmz": "1", "name": "NUTRIENT AGAR"},
        "3": {"dsmz": "92", "name": "TRYPTICASE SOY AGAR/BROTH"},
        "18": {"dsmz": "92", "name": "TRYPTICASE SOY BROTH"},
        "416": {"dsmz": "4", "name": "GYM MEDIUM"},  # Glucose-Yeast-Malt
        "632": {"dsmz": "1", "name": "NUTRIENT BROTH"},
        "745": {"dsmz": "63", "name": "KING'S MEDIUM B"},
        "1306": {"dsmz": "632", "name": "NITRATE MINERAL SALTS MEDIUM (NMS)"},  # Already verified
        "2": {"dsmz": "15", "name": "POTATO DEXTROSE AGAR"},
        "325": {"dsmz": "65", "name": "CZAPEK-DOX AGAR"},
        "28": {"dsmz": "1", "name": "EMERSON YpSs AGAR"},
        "200": {"dsmz": "14", "name": "YM AGAR/BROTH"},  # Yeast-Malt
    }

    # Common media name patterns that indicate equivalence
    NAME_PATTERNS = {
        r'NUTRIENT\s+(?:AGAR|BROTH)': ['NUTRIENT AGAR', 'NUTRIENT BROTH'],
        r'TRYPTIC(?:ASE)?\s+SOY': ['TSA', 'TSB', 'TRYPTIC SOY', 'TRYPTICASE SOY'],
        r'POTATO\s+DEXTROSE': ['PDA', 'POTATO DEXTROSE AGAR'],
        r'LB\s+(?:AGAR|BROTH|MEDIUM)': ['LB', 'LURIA BERTANI', 'LYSOGENY BROTH'],
        r'CZAPEK': ['CZAPEK-DOX', 'CZAPEK AGAR'],
        r'KING.*B': ["KING'S MEDIUM B", "KING B"],
        r'YM\s+(?:AGAR|BROTH)': ['YEAST MALT', 'YM AGAR'],
        r'M9\s+MINIMAL': ['M9', 'M9 MINIMAL MEDIUM'],
    }

    def __init__(self, enable_literature_verification: bool = False):
        """
        Initialize cross-reference builder.

        Args:
            enable_literature_verification: Enable literature-based verification
        """
        self.verified_refs = self.load_verified_refs()
        self.dsmz_media = self.load_dsmz_media()

        if enable_literature_verification:
            from culturemech.enrich.literature_verifier import LiteratureVerifier
            from culturemech.enrich.atcc_crossref_verifier import ATCCCrossRefVerifier

            use_scihub = os.getenv("ENABLE_SCIHUB_FALLBACK", "false").lower() == "true"
            email = os.getenv("LITERATURE_EMAIL", "noreply@example.com")

            self.lit_verifier = LiteratureVerifier(
                use_fallback_pdf=use_scihub,
                email=email
            )
            self.crossref_verifier = ATCCCrossRefVerifier(self.lit_verifier)
        else:
            self.crossref_verifier = None

    def load_verified_refs(self) -> Dict[str, Any]:
        """Load existing verified cross-references."""
        crossref_file = Path("data/raw/atcc/atcc_crossref.json")
        if crossref_file.exists():
            with open(crossref_file, 'r') as f:
                return json.load(f)
        return {}

    def load_dsmz_media(self) -> Dict[str, Dict[str, Any]]:
        """
        Load DSMZ media from normalized YAML files.

        Returns:
            Dict mapping DSMZ ID to media metadata
        """
        dsmz_media = {}
        yaml_dir = Path("data/normalized_yaml")

        for yaml_file in yaml_dir.glob("**/DSMZ_*.yaml"):
            # Extract DSMZ ID from filename
            match = re.search(r'DSMZ_(\d+[a-z]?)_', yaml_file.stem)
            if not match:
                continue

            dsmz_id = match.group(1)

            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)

                dsmz_media[dsmz_id] = {
                    "name": data.get("name", ""),
                    "original_name": data.get("original_name", ""),
                    "ingredients": data.get("ingredients", []),
                    "medium_type": data.get("medium_type", ""),
                    "ph_value": data.get("ph_value"),
                    "file_path": str(yaml_file)
                }
            except Exception as e:
                logger.warning(f"Failed to load {yaml_file}: {e}")
                continue

        logger.info(f"Loaded {len(dsmz_media)} DSMZ media")
        return dsmz_media

    def normalize_name(self, name: str) -> str:
        """
        Normalize media name for comparison.

        Args:
            name: Original media name

        Returns:
            Normalized name (uppercase, standardized spacing)
        """
        # Convert to uppercase
        normalized = name.upper()

        # Remove extra whitespace
        normalized = re.sub(r'\s+', ' ', normalized).strip()

        # Remove common suffixes/prefixes
        normalized = re.sub(r'\s*(AGAR|BROTH|MEDIUM)\s*$', '', normalized)
        normalized = re.sub(r'^DSMZ\s+MEDIUM\s+\d+:?\s*', '', normalized)
        normalized = re.sub(r'^ATCC\s+MEDIUM\s+\d+:?\s*', '', normalized)

        return normalized

    def name_similarity(self, name1: str, name2: str) -> float:
        """
        Calculate similarity between two media names.

        Args:
            name1: First name
            name2: Second name

        Returns:
            Similarity score (0.0 to 1.0)
        """
        norm1 = self.normalize_name(name1)
        norm2 = self.normalize_name(name2)

        return SequenceMatcher(None, norm1, norm2).ratio()

    def find_candidates(
        self,
        min_similarity: float = 0.8,
        max_candidates: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Find potential ATCC-DSMZ cross-reference candidates.

        Args:
            min_similarity: Minimum name similarity threshold (0.0-1.0)
            max_candidates: Maximum number of candidates to return

        Returns:
            List of candidate matches with scores
        """
        candidates = []

        # First, add all known equivalencies that aren't already verified
        for atcc_id, info in self.KNOWN_EQUIVALENCIES.items():
            if atcc_id in self.verified_refs:
                continue  # Skip already verified

            dsmz_id = info["dsmz"]
            if dsmz_id in self.dsmz_media:
                candidates.append({
                    "atcc_id": atcc_id,
                    "dsmz_id": dsmz_id,
                    "atcc_name": info["name"],
                    "dsmz_name": self.dsmz_media[dsmz_id]["name"],
                    "similarity": 1.0,  # Known match
                    "source": "literature",
                    "confidence": "high"
                })

        # Then find name-based matches
        for dsmz_id, dsmz_info in self.dsmz_media.items():
            dsmz_name = dsmz_info["name"]

            # Check against known ATCC names
            for atcc_id, info in self.KNOWN_EQUIVALENCIES.items():
                if atcc_id in self.verified_refs:
                    continue

                atcc_name = info["name"]
                similarity = self.name_similarity(atcc_name, dsmz_name)

                if similarity >= min_similarity:
                    # Check if already in candidates
                    existing = next((c for c in candidates if c["atcc_id"] == atcc_id and c["dsmz_id"] == dsmz_id), None)
                    if not existing:
                        candidates.append({
                            "atcc_id": atcc_id,
                            "dsmz_id": dsmz_id,
                            "atcc_name": atcc_name,
                            "dsmz_name": dsmz_name,
                            "similarity": similarity,
                            "source": "name_match",
                            "confidence": "medium" if similarity > 0.9 else "low"
                        })

        # Sort by similarity score
        candidates.sort(key=lambda x: x["similarity"], reverse=True)

        return candidates[:max_candidates]

    def generate_candidates_report(
        self,
        output_file: Path,
        min_similarity: float = 0.8,
        verify_literature: bool = False
    ):
        """
        Generate a report of candidate ATCC-DSMZ cross-references for manual review.

        Args:
            output_file: Path to save candidates JSON
            min_similarity: Minimum similarity threshold
            verify_literature: Enable literature verification for medium-confidence candidates
        """
        logger.info("Finding ATCC-DSMZ cross-reference candidates...")

        candidates = self.find_candidates(min_similarity=min_similarity)

        # Literature verification for medium-confidence candidates
        if verify_literature and self.crossref_verifier:
            logger.info("\nVerifying medium-confidence candidates via literature...")

            medium_confidence = [
                c for c in candidates
                if 0.85 <= c["similarity"] < 0.95
            ]

            verified = self.crossref_verifier.batch_verify_candidates(
                medium_confidence,
                min_similarity=0.85,
                max_similarity=0.95
            )

            # Update candidates with verification results
            for v in verified:
                for c in candidates:
                    if c["atcc_id"] == v["atcc_id"] and c["dsmz_id"] == v["dsmz_id"]:
                        c["verified"] = True
                        c["confidence"] = "high"  # Upgrade confidence
                        c["verification_notes"] = f"Literature verified: {v['doi']}"
                        c["evidence_snippet"] = v["evidence_snippet"]
                        c["pdf_source"] = v["source_tier"]
                        break

        # Format for manual review
        review_data = {
            "generated_date": "2026-02-20",
            "total_candidates": len(candidates),
            "verified_count": len(self.verified_refs),
            "literature_verified": sum(1 for c in candidates if c.get("verified") == True) if verify_literature else 0,
            "candidates": [
                {
                    "atcc_id": c["atcc_id"],
                    "dsmz_id": c["dsmz_id"],
                    "atcc_name": c["atcc_name"],
                    "dsmz_name": c["dsmz_name"],
                    "similarity_score": round(c["similarity"], 3),
                    "source": c["source"],
                    "confidence": c["confidence"],
                    "verified": c.get("verified", False),
                    "verification_notes": c.get("verification_notes", ""),
                    "evidence_snippet": c.get("evidence_snippet", ""),
                    "pdf_source": c.get("pdf_source", ""),
                    "notes": ""  # For manual notes
                }
                for c in candidates
            ]
        }

        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(review_data, f, indent=2, ensure_ascii=False)

        logger.info(f"\n✓ Saved {len(candidates)} candidates to {output_file}")
        logger.info(f"  Literature matches: {sum(1 for c in candidates if c['source'] == 'literature')}")
        logger.info(f"  Name matches: {sum(1 for c in candidates if c['source'] == 'name_match')}")
        logger.info(f"  High confidence: {sum(1 for c in candidates if c['confidence'] == 'high')}")
        logger.info(f"  Medium confidence: {sum(1 for c in candidates if c['confidence'] == 'medium')}")
        if verify_literature:
            logger.info(f"  Literature verified: {review_data['literature_verified']}")

        return review_data

    def add_verified_crossrefs(
        self,
        candidates_file: Path,
        dry_run: bool = False
    ):
        """
        Add verified cross-references from reviewed candidates file.

        Args:
            candidates_file: Path to candidates JSON with verified=true entries
            dry_run: If True, only show what would be added
        """
        with open(candidates_file, 'r') as f:
            data = json.load(f)

        # Find verified candidates
        verified_new = [c for c in data["candidates"] if c.get("verified") == True]

        if not verified_new:
            logger.info("No verified candidates found in file")
            return

        logger.info(f"Found {len(verified_new)} verified candidates")

        # Load current cross-references
        crossref_file = Path("data/raw/atcc/atcc_crossref.json")
        if crossref_file.exists():
            with open(crossref_file, 'r') as f:
                crossrefs = json.load(f)
        else:
            crossrefs = {}

        # Add new verified entries
        added_count = 0
        for candidate in verified_new:
            atcc_id = str(candidate["atcc_id"])

            if atcc_id in crossrefs:
                logger.info(f"  Skipping ATCC {atcc_id} (already exists)")
                continue

            if dry_run:
                logger.info(f"  Would add: ATCC {atcc_id} = DSMZ {candidate['dsmz_id']} ({candidate['atcc_name']})")
                continue

            crossrefs[atcc_id] = {
                "dsmz": str(candidate["dsmz_id"]),
                "name": candidate["atcc_name"],
                "verified": True,
                "verification_date": "2026-02-19",
                "verification_notes": f"Verified via {candidate['source']} (similarity: {candidate['similarity_score']}). {candidate.get('notes', '')}".strip(),
                "composition_match": "verified"
            }

            added_count += 1
            logger.info(f"  ✓ Added: ATCC {atcc_id} = DSMZ {candidate['dsmz_id']}")

        if not dry_run and added_count > 0:
            # Save updated cross-references
            with open(crossref_file, 'w', encoding='utf-8') as f:
                json.dump(crossrefs, f, indent=2, ensure_ascii=False)

            logger.info(f"\n✓ Added {added_count} new cross-references")
            logger.info(f"  Total cross-references: {len(crossrefs)}")
            logger.info(f"  Saved to: {crossref_file}")
        elif dry_run:
            logger.info(f"\nDRY RUN - would add {added_count} cross-references")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Build ATCC-DSMZ cross-reference database"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate candidates
    gen_parser = subparsers.add_parser("generate", help="Generate candidate cross-references")
    gen_parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("data/curation/atcc_candidates.json"),
        help="Output file for candidates (default: data/curation/atcc_candidates.json)"
    )
    gen_parser.add_argument(
        "-s", "--similarity",
        type=float,
        default=0.8,
        help="Minimum similarity threshold (default: 0.8)"
    )
    gen_parser.add_argument(
        "--verify-literature",
        action="store_true",
        help="Verify candidates via literature search (uses legal sources by default)"
    )
    gen_parser.add_argument(
        "--enable-scihub-fallback",
        action="store_true",
        help="Enable Sci-Hub fallback for PDF retrieval (opt-in, may violate publisher agreements)"
    )

    # Add verified
    add_parser = subparsers.add_parser("add", help="Add verified cross-references")
    add_parser.add_argument(
        "candidates_file",
        type=Path,
        help="Candidates JSON file with verified=true entries"
    )
    add_parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be added without modifying files"
    )

    args = parser.parse_args()

    # Set environment variable if Sci-Hub fallback enabled
    if hasattr(args, 'enable_scihub_fallback') and args.enable_scihub_fallback:
        os.environ["ENABLE_SCIHUB_FALLBACK"] = "true"
        logger.warning("⚠ Sci-Hub fallback enabled - ensure compliance with institutional policies")

    # Initialize builder with literature verification if requested
    enable_lit = hasattr(args, 'verify_literature') and args.verify_literature
    builder = ATCCCrossReferenceBuilder(enable_literature_verification=enable_lit)

    if args.command == "generate":
        builder.generate_candidates_report(
            output_file=args.output,
            min_similarity=args.similarity,
            verify_literature=enable_lit
        )
    elif args.command == "add":
        builder.add_verified_crossrefs(
            candidates_file=args.candidates_file,
            dry_run=args.dry_run
        )


if __name__ == "__main__":
    main()
