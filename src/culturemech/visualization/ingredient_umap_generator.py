"""
Ingredient-level UMAP visualization generator.

Each point in the plot is a unique CHEBI ingredient observed across CultureMech media,
positioned by its 512-dim KG-Microbe DeepWalk embedding reduced to 2D via UMAP.

Point size encodes occurrence frequency; color encodes occurrence tier.
"""

from __future__ import annotations

import csv
import json
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import pandas as pd
import umap
import yaml
from jinja2 import Environment, FileSystemLoader
from tqdm import tqdm

from culturemech.embedding.loader import EmbeddingLoader


@dataclass
class IngredientInfo:
    """Metadata for a single CHEBI ingredient."""

    chebi_id: str
    preferred_term: str
    cas_rn: str = ""
    kg_node_id: str = ""
    occurrence_count: int = 0
    example_media: List[str] = field(default_factory=list)
    tier: str = "other"  # top100 / top500 / other


class IngredientUMAPGenerator:
    """Generate interactive ingredient embedding UMAP visualization."""

    def __init__(
        self,
        name_to_chebi_path: Optional[Path] = None,
        unified_mapping_path: Optional[Path] = None,
    ):
        # Optional: name-based CHEBI fallback
        self.name_to_chebi: Dict[str, str] = {}
        if name_to_chebi_path and name_to_chebi_path.exists():
            with open(name_to_chebi_path) as f:
                raw = json.load(f)
            self.name_to_chebi = {k.lower().strip(): v for k, v in raw.items()}
            print(f"  Loaded {len(self.name_to_chebi)} name→CHEBI fallback entries")

        # Optional: unified mapping for CAS-RN and KG node annotation
        self.cas_rn_index: Dict[str, str] = {}
        self.kg_node_index: Dict[str, str] = {}
        if unified_mapping_path and unified_mapping_path.exists():
            with open(unified_mapping_path) as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    chebi = row.get('chebi_id', '').strip()
                    if chebi.startswith('CHEBI:'):
                        self.cas_rn_index[chebi] = row.get('cas_rn', '').strip()
                        self.kg_node_index[chebi] = row.get('kg_microbe_node_id', '').strip()
            print(f"  Loaded CAS-RN/KG annotations for {len(self.cas_rn_index)} CHEBI IDs")

    # ------------------------------------------------------------------
    # Step 1: Collect ingredients from CultureMech YAML files
    # ------------------------------------------------------------------

    def collect_ingredients(self, media_dir: Path) -> Dict[str, IngredientInfo]:
        """
        Scan all CultureMech normalized_yaml files and collect unique CHEBI ingredients.

        CHEBI extraction priority:
          1. term.id (if starts with CHEBI:)
          2. chebi_term.id (enriched field)
          3. Name-based fallback via name_to_chebi mapping

        Returns: chebi_id → IngredientInfo
        """
        ingredients: Dict[str, IngredientInfo] = {}
        yaml_files = list(media_dir.rglob("*.yaml"))
        print(f"  Collecting ingredients from {len(yaml_files)} YAML files...")

        for yaml_file in tqdm(yaml_files, desc="Scanning media"):
            try:
                data = yaml.safe_load(yaml_file.read_text())
            except Exception:
                continue
            if not data or not isinstance(data, dict):
                continue

            media_id = data.get('id', yaml_file.stem)

            for ing in (data.get('ingredients', []) or []):
                if not isinstance(ing, dict):
                    continue

                chebi_id = self._extract_chebi(ing)
                if not chebi_id:
                    continue

                name = ing.get('preferred_term', '').strip() or chebi_id

                if chebi_id not in ingredients:
                    ingredients[chebi_id] = IngredientInfo(
                        chebi_id=chebi_id,
                        preferred_term=name,
                        cas_rn=self.cas_rn_index.get(chebi_id, ''),
                        kg_node_id=self.kg_node_index.get(chebi_id, ''),
                    )
                info = ingredients[chebi_id]
                info.occurrence_count += 1
                if len(info.example_media) < 5:
                    info.example_media.append(media_id)

        # Assign tiers by occurrence rank
        ranked = sorted(ingredients.values(), key=lambda x: -x.occurrence_count)
        for i, info in enumerate(ranked):
            if i < 100:
                info.tier = "top100"
            elif i < 500:
                info.tier = "top500"
            else:
                info.tier = "other"

        print(f"  Found {len(ingredients)} unique CHEBI ingredients")
        return ingredients

    def _extract_chebi(self, ing: dict) -> Optional[str]:
        """Extract CHEBI ID from ingredient dict using priority order."""
        # 1. term.id (CHEBI)
        term = ing.get('term') or {}
        if isinstance(term, dict):
            tid = term.get('id', '')
            if tid.startswith('CHEBI:'):
                return tid

        # 2. chebi_term.id (enriched)
        chebi_term = ing.get('chebi_term') or {}
        if isinstance(chebi_term, dict):
            cid = chebi_term.get('id', '')
            if cid.startswith('CHEBI:'):
                return cid

        # 3. Name fallback
        name = ing.get('preferred_term', '').lower().strip()
        if name and name in self.name_to_chebi:
            val = self.name_to_chebi[name]
            # JSON values may be a list of CHEBI IDs; take the first
            if isinstance(val, list):
                val = val[0] if val else None
            if val and isinstance(val, str) and val.startswith('CHEBI:'):
                return val

        return None

    # ------------------------------------------------------------------
    # Step 2: Embed ingredients
    # ------------------------------------------------------------------

    def embed(
        self,
        ingredients: Dict[str, IngredientInfo],
        embeddings_path: Path,
        cache_dir: Path = Path(".umap_cache"),
        force_reload: bool = False,
    ) -> Dict[str, np.ndarray]:
        """
        Load KG-Microbe embeddings and look up each CHEBI ingredient.

        Returns: chebi_id → 512-dim embedding vector
        """
        print("Loading KG-Microbe embeddings (CHEBI nodes only)...")
        embeddings_dict = EmbeddingLoader.load_embeddings(
            embeddings_path=embeddings_path,
            node_prefixes=["CHEBI"],
            cache_dir=cache_dir,
            force_reload=force_reload,
        )

        found: Dict[str, np.ndarray] = {}
        missing = []
        for chebi_id in ingredients:
            if chebi_id in embeddings_dict:
                found[chebi_id] = embeddings_dict[chebi_id]
            else:
                missing.append(chebi_id)

        pct = 100 * len(found) / len(ingredients) if ingredients else 0
        print(f"  Embedded {len(found)}/{len(ingredients)} ingredients ({pct:.1f}% coverage)")
        if missing[:5]:
            print(f"  Sample missing: {missing[:5]}")

        return found

    # ------------------------------------------------------------------
    # Step 3: Reduce to 2D
    # ------------------------------------------------------------------

    def reduce(
        self,
        embedded: Dict[str, np.ndarray],
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        random_state: int = 42,
    ) -> pd.DataFrame:
        """Apply UMAP to reduce 512D ingredient embeddings to 2D."""
        if not embedded:
            return pd.DataFrame(columns=["chebi_id", "umap_x", "umap_y"])

        chebi_ids = list(embedded.keys())
        matrix = np.array([embedded[c] for c in chebi_ids], dtype=np.float32)
        print(f"  Reducing {len(chebi_ids)} ingredients from {matrix.shape[1]}D → 2D...")

        reducer = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            n_components=2,
            metric="cosine",
            random_state=random_state,
            verbose=False,
        )
        coords = reducer.fit_transform(matrix)

        df = pd.DataFrame({
            "chebi_id": chebi_ids,
            "umap_x": coords[:, 0],
            "umap_y": coords[:, 1],
        })
        print("  UMAP reduction complete")
        return df

    # ------------------------------------------------------------------
    # Step 4: Render HTML
    # ------------------------------------------------------------------

    def render_html(
        self,
        df: pd.DataFrame,
        ingredients: Dict[str, IngredientInfo],
        output_path: Path,
        templates_dir: Optional[Path] = None,
    ) -> None:
        """
        Render interactive ingredient UMAP as self-contained HTML.
        """
        if templates_dir is None:
            templates_dir = Path(__file__).parent.parent / "templates"

        # Build JSON data for D3
        points = []
        for _, row in df.iterrows():
            chebi_id = row["chebi_id"]
            info = ingredients.get(chebi_id)
            if info is None:
                continue
            count = info.occurrence_count
            # Log-scale radius: min 5, max 14 (floor raised to 5px for legibility, dataviz #8/#9)
            radius = max(5, min(14, 3 + 3 * math.log10(max(count, 1))))
            points.append({
                "x": float(row["umap_x"]),
                "y": float(row["umap_y"]),
                "chebi_id": chebi_id,
                "name": info.preferred_term,
                "cas_rn": info.cas_rn,
                "kg_node_id": info.kg_node_id,
                "count": count,
                "tier": info.tier,
                "radius": round(radius, 1),
                "example_media": info.example_media[:3],
            })

        # Sort: most frequent last so they render on top
        points.sort(key=lambda p: p["count"])

        tier_counts = {
            "top100": sum(1 for p in points if p["tier"] == "top100"),
            "top500": sum(1 for p in points if p["tier"] == "top500"),
            "other": sum(1 for p in points if p["tier"] == "other"),
        }

        env = Environment(loader=FileSystemLoader(str(templates_dir)))
        template = env.get_template("ingredient_umap.html")

        html = template.render(
            ingredient_data_json=json.dumps(points),
            total_count=len(points),
            tier_counts=tier_counts,
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html)
        print(f"  HTML written to {output_path}  ({len(points)} ingredients)")

    # ------------------------------------------------------------------
    # Full pipeline
    # ------------------------------------------------------------------

    def generate(
        self,
        media_dir: Path,
        embeddings_path: Path,
        output_html: Path,
        cache_dir: Path = Path(".umap_cache"),
        force_reload: bool = False,
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        min_count: int = 1,
        dry_run: bool = False,
    ) -> None:
        """Run the full ingredient UMAP pipeline."""
        print("\n" + "=" * 60)
        print("STEP 1: Collecting ingredients")
        print("=" * 60)
        ingredients = self.collect_ingredients(media_dir)

        if min_count > 1:
            before = len(ingredients)
            ingredients = {k: v for k, v in ingredients.items()
                          if v.occurrence_count >= min_count}
            print(f"  Filtered to {len(ingredients)} ingredients (≥{min_count} occurrences, was {before})")

        if dry_run:
            print(f"\nDRY RUN — would embed {len(ingredients)} ingredients")
            return

        print("\n" + "=" * 60)
        print("STEP 2: Loading embeddings")
        print("=" * 60)
        embedded = self.embed(ingredients, embeddings_path, cache_dir, force_reload)

        if not embedded:
            print("ERROR: No embeddings found. Check embeddings file path.")
            return

        print("\n" + "=" * 60)
        print("STEP 3: UMAP reduction")
        print("=" * 60)
        df = self.reduce(embedded, n_neighbors=n_neighbors, min_dist=min_dist)

        print("\n" + "=" * 60)
        print("STEP 4: Rendering HTML")
        print("=" * 60)
        self.render_html(df, ingredients, output_html)

        print(f"\n✅ Ingredient UMAP complete → {output_html}")
