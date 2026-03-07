"""
UMAP visualization generator for culture media embeddings.

Orchestrates the full pipeline: loading, aggregation, reduction, and HTML generation.
"""

import json
from pathlib import Path
from typing import Dict, List

import yaml
from jinja2 import Environment, FileSystemLoader

from culturemech.embedding.aggregator import MediaEmbedding, MediaVectorAggregator
from culturemech.embedding.dimensionality import reduce_to_2d
from culturemech.embedding.loader import EmbeddingLoader


class UMAPVisualizationGenerator:
    """Generate interactive UMAP visualizations of media embeddings."""

    def generate_both_plots(
        self,
        media_dir: Path,
        embeddings_path: Path,
        output_html: Path,
        cache_dir: Path = Path(".umap_cache"),
        force_reload: bool = False,
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        min_coverage: float = 0.5,
    ) -> None:
        """
        Generate interactive UMAP visualization with both derived and direct embeddings.

        Args:
            media_dir: Directory containing media YAML files
            embeddings_path: Path to KG-Microbe embeddings TSV.gz
            output_html: Path for output HTML file
            cache_dir: Directory for caching embeddings
            force_reload: Force reload from source (bypass cache)
            n_neighbors: UMAP n_neighbors parameter
            min_dist: UMAP min_dist parameter
            min_coverage: Minimum embedding coverage for derived embeddings
        """
        print("=" * 70)
        print("UMAP Visualization Generator - CultureMech")
        print("=" * 70)

        # Step 1: Load embeddings
        print("\n[1/6] Loading embeddings...")
        embeddings = EmbeddingLoader.load_embeddings(
            embeddings_path=embeddings_path,
            node_prefixes=["CHEBI", "NCBITaxon", "mediadive.medium", "FOODON"],
            cache_dir=cache_dir,
            force_reload=force_reload,
        )

        # Step 2: Collect media YAML files
        print("\n[2/6] Collecting media files...")
        media_yamls = self._collect_media_yamls(media_dir)
        print(f"✓ Found {len(media_yamls):,} media YAML files")

        # Step 3: Generate derived embeddings
        print("\n[3/6] Aggregating derived embeddings...")
        aggregator = MediaVectorAggregator(embeddings)
        derived_embeddings = aggregator.aggregate_derived_embeddings(
            media_yamls, min_coverage=min_coverage
        )

        # Step 4: Extract direct embeddings
        print("\n[4/6] Extracting direct embeddings...")
        direct_embeddings = aggregator.get_direct_embeddings(media_yamls)

        # Step 5: Apply UMAP reduction
        print("\n[5/6] Applying UMAP reduction...")
        derived_df = reduce_to_2d(
            derived_embeddings, n_neighbors=n_neighbors, min_dist=min_dist
        )
        direct_df = reduce_to_2d(
            direct_embeddings, n_neighbors=n_neighbors, min_dist=min_dist
        )

        # Step 6: Generate HTML visualization
        print("\n[6/6] Generating HTML visualization...")
        self._generate_html(
            derived_df=derived_df,
            direct_df=direct_df,
            derived_embeddings=derived_embeddings,
            direct_embeddings=direct_embeddings,
            media_dir=media_dir,
            output_html=output_html,
        )

        print("\n" + "=" * 70)
        print(f"✓ Visualization generated: {output_html}")
        print(f"  - Derived embeddings: {len(derived_embeddings):,} media")
        print(f"  - Direct embeddings: {len(direct_embeddings):,} media")
        print("=" * 70)

    def _collect_media_yamls(self, media_dir: Path) -> List[Path]:
        """Collect all media YAML files from directory tree."""
        media_yamls = []
        for category_dir in media_dir.iterdir():
            if category_dir.is_dir():
                media_yamls.extend(category_dir.glob("*.yaml"))
        return sorted(media_yamls)

    def _generate_html(
        self,
        derived_df,
        direct_df,
        derived_embeddings: Dict[str, MediaEmbedding],
        direct_embeddings: Dict[str, MediaEmbedding],
        media_dir: Path,
        output_html: Path,
    ) -> None:
        """Generate HTML file with embedded D3.js visualization."""
        # Build data structures with metadata
        derived_data = self._build_plot_data(derived_df, derived_embeddings, media_dir)
        direct_data = self._build_plot_data(direct_df, direct_embeddings, media_dir)

        # Load template
        template_dir = Path(__file__).parent.parent / "templates"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("media_umap.html")

        # Render template
        html_content = template.render(
            derived_data_json=json.dumps(derived_data),
            direct_data_json=json.dumps(direct_data),
            derived_count=len(derived_data),
            direct_count=len(direct_data),
        )

        # Write output
        output_html.parent.mkdir(parents=True, exist_ok=True)
        with open(output_html, "w") as f:
            f.write(html_content)

        print(f"✓ HTML generated: {output_html} ({len(html_content):,} bytes)")

    def _build_plot_data(
        self, df, embeddings: Dict[str, MediaEmbedding], media_dir: Path
    ) -> List[dict]:
        """Build plot data structure with metadata for each medium."""
        plot_data = []

        for _, row in df.iterrows():
            medium_id = row["medium_id"]
            embedding = embeddings[medium_id]

            # Load YAML for metadata
            metadata = self._extract_metadata(medium_id, media_dir)

            plot_data.append(
                {
                    "id": medium_id,
                    "x": float(row["umap_x"]),
                    "y": float(row["umap_y"]),
                    "name": metadata.get("name", medium_id),
                    "category": metadata.get("category", "unknown"),
                    "medium_type": metadata.get("medium_type", "unknown"),
                    "physical_state": metadata.get("physical_state", "unknown"),
                    "num_ingredients": embedding.num_ingredients,
                    "num_organisms": embedding.num_organisms,
                    "coverage": round(embedding.coverage, 2),
                    "source_database": metadata.get("source_database", "unknown"),
                    "url": f"pages/{medium_id}.html",
                }
            )

        return plot_data

    def _extract_metadata(self, medium_id: str, media_dir: Path) -> dict:
        """Extract metadata from media YAML file."""
        # Find YAML file in category subdirectories
        for category_dir in media_dir.iterdir():
            if category_dir.is_dir():
                yaml_path = category_dir / f"{medium_id}.yaml"
                if yaml_path.exists():
                    try:
                        with open(yaml_path, "r") as f:
                            data = yaml.safe_load(f)
                            return {
                                "name": data.get("name", medium_id),
                                "category": category_dir.name,
                                "medium_type": data.get("medium_type", "unknown"),
                                "physical_state": data.get("physical_state", "unknown"),
                                "source_database": self._infer_source_database(data),
                            }
                    except Exception:
                        pass

        return {}

    def _infer_source_database(self, media_data: dict) -> str:
        """Infer source database from media term ID."""
        media_term = media_data.get("media_term")
        if isinstance(media_term, dict) and "term" in media_term:
            term = media_term["term"]
            if isinstance(term, dict) and "id" in term:
                term_id = term["id"]
                if ":" in term_id:
                    return term_id.split(":")[0]
        return "unknown"
