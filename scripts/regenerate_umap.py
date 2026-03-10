#!/usr/bin/env python3
"""Regenerate UMAP visualization with updated solution mappings."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from culturemech.visualization.umap_generator import UMAPVisualizationGenerator

def main():
    generator = UMAPVisualizationGenerator()

    generator.generate_both_plots(
        media_dir=Path("data/normalized_yaml"),
        embeddings_path=Path("data/kgm/merged-kg_node_embeddings.tsv.gz"),
        output_html=Path("app/umap.html"),
        cache_dir=Path(".umap_cache"),
        force_reload=False,
        n_neighbors=15,
        min_dist=0.1,
        min_coverage=0.0,  # Set to 0 to include solutions with any coverage
    )

    print("\n✓ UMAP visualization regenerated!")

if __name__ == "__main__":
    main()
