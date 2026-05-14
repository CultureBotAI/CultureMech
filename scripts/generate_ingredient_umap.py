#!/usr/bin/env python3
"""
Generate ingredient-level UMAP visualization for CultureMech.

Each point = one unique CHEBI ingredient observed across CultureMech media,
positioned by its 512-dim KG-Microbe DeepWalk embedding reduced to 2D via UMAP.

Usage:
    python scripts/generate_ingredient_umap.py [options]

Example:
    python scripts/generate_ingredient_umap.py \\
        --embeddings-path data/embeddings/DeepWalk...tsv.gz \\
        --output app/ingredient_umap.html

    python scripts/generate_ingredient_umap.py --dry-run
"""

import argparse
import sys
from pathlib import Path

# Add src to path for direct script execution
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from culturemech.visualization.ingredient_umap_generator import IngredientUMAPGenerator

_REPO_ROOT = Path(__file__).parent.parent

_EMBEDDINGS_FILENAME = "DeepWalkSkipGramEnsmallen_degreenorm_embedding_512_v2_2026-04-25_20_44_08.tsv.gz"
# Prefer local data/embeddings/; fall back to sibling CommunityMech location
_LOCAL_EMBEDDINGS = _REPO_ROOT / "data" / "embeddings" / _EMBEDDINGS_FILENAME
_COMMUNITYMECH_EMBEDDINGS = (
    "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CommunityMech"
    "/CommunityMech/data/embeddings/" + _EMBEDDINGS_FILENAME
)
KG_MICROBE_EMBEDDINGS = str(_LOCAL_EMBEDDINGS) if _LOCAL_EMBEDDINGS.exists() else _COMMUNITYMECH_EMBEDDINGS

NAME_TO_CHEBI_PATH = Path("data/chemical_name_to_chebi_mapping_enhanced.json")
# Sibling repo path: CultureMech/../culturebotai-claw/workspace/
UNIFIED_MAPPING_PATH = (
    _REPO_ROOT.parent / "culturebotai-claw" / "workspace" / "unified_ingredient_mapping.tsv"
)


def main():
    parser = argparse.ArgumentParser(
        description="Generate ingredient-level UMAP visualization for CultureMech"
    )
    parser.add_argument(
        "--media-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Directory containing CultureMech YAML files (default: data/normalized_yaml)",
    )
    parser.add_argument(
        "--embeddings-path",
        type=Path,
        default=Path(KG_MICROBE_EMBEDDINGS),
        help="Path to KG-Microbe embeddings TSV/TSV.gz file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("app/ingredient_umap.html"),
        help="Output HTML path (default: app/ingredient_umap.html)",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path(".umap_cache"),
        help="Directory for embedding cache (default: .umap_cache)",
    )
    parser.add_argument(
        "--unified-mapping",
        type=Path,
        default=UNIFIED_MAPPING_PATH,
        help="Path to unified_ingredient_mapping.tsv for CAS-RN/KG annotations",
    )
    parser.add_argument(
        "--name-to-chebi",
        type=Path,
        default=NAME_TO_CHEBI_PATH,
        help="Path to chemical_name_to_chebi_mapping_enhanced.json for name fallback",
    )
    parser.add_argument(
        "--n-neighbors",
        type=int,
        default=15,
        help="UMAP n_neighbors parameter (default: 15)",
    )
    parser.add_argument(
        "--min-dist",
        type=float,
        default=0.1,
        help="UMAP min_dist parameter (default: 0.1)",
    )
    parser.add_argument(
        "--min-count",
        type=int,
        default=1,
        help="Minimum occurrence count to include ingredient (default: 1)",
    )
    parser.add_argument(
        "--force-reload",
        action="store_true",
        help="Force reload embeddings (ignore cache)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Collect and count ingredients but skip embedding/UMAP/render",
    )
    args = parser.parse_args()

    # Resolve optional support files
    name_to_chebi = args.name_to_chebi if args.name_to_chebi.exists() else None
    unified_mapping = args.unified_mapping if args.unified_mapping.exists() else None

    if name_to_chebi:
        print(f"  Name→CHEBI fallback: {name_to_chebi}")
    else:
        print(f"  Name→CHEBI fallback: not found at {args.name_to_chebi} (skipped)")

    if unified_mapping:
        print(f"  Unified mapping: {unified_mapping}")
    else:
        print(f"  Unified mapping: not found at {args.unified_mapping} (CAS-RN/KG annotations will be empty)")

    generator = IngredientUMAPGenerator(
        name_to_chebi_path=name_to_chebi,
        unified_mapping_path=unified_mapping,
    )

    generator.generate(
        media_dir=args.media_dir,
        embeddings_path=args.embeddings_path,
        output_html=args.output,
        cache_dir=args.cache_dir,
        force_reload=args.force_reload,
        n_neighbors=args.n_neighbors,
        min_dist=args.min_dist,
        min_count=args.min_count,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
