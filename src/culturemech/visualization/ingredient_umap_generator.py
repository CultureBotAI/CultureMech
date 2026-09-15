"""
Ingredient-level graph embedding visualization generator.

Each point in the plot is a unique CHEBI ingredient observed across CultureMech media,
positioned by its KG-Microbe DeepWalk embedding reduced to 2D via PaCMAP by default.

Point size encodes occurrence frequency; color encodes occurrence tier.
"""

from __future__ import annotations

import csv
import json
import math
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from tqdm import tqdm

from culturemech.graph_embedding_receipts import (
    GraphSource,
    corpus_receipt,
    file_sha256,
    make_receipt,
    matrix_receipt,
    projection_receipt,
    publish_artifacts,
)


@dataclass
class IngredientInfo:
    """Metadata for a single CHEBI ingredient."""

    chebi_id: str
    preferred_term: str
    cas_rn: str = ""
    kg_node_id: str = ""
    occurrence_count: int = 0
    example_media: list[str] = field(default_factory=list)
    tier: str = "other"  # top100 / top500 / other


class IngredientUMAPGenerator:
    """Generate interactive ingredient embedding UMAP visualization."""

    def __init__(
        self,
        name_to_chebi_path: Path | None = None,
        unified_mapping_path: Path | None = None,
    ):
        self.auxiliary_paths = {
            name: path
            for name, path in (
                ("name_to_chebi", name_to_chebi_path),
                ("unified_mapping", unified_mapping_path),
            )
            if path is not None and path.is_file()
        }
        self.auxiliary_receipts = {
            name: {"filename": path.name, "sha256": file_sha256(path)}
            for name, path in self.auxiliary_paths.items()
        }
        self.occurrences = []
        # Optional: name-based CHEBI fallback
        self.name_to_chebi: dict[str, str] = {}
        if name_to_chebi_path and name_to_chebi_path.exists():
            with open(name_to_chebi_path) as f:
                raw = json.load(f)
            self.name_to_chebi = {k.lower().strip(): v for k, v in raw.items()}
            print(f"  Loaded {len(self.name_to_chebi)} name→CHEBI fallback entries")

        # Optional: unified mapping for CAS-RN and KG node annotation
        self.cas_rn_index: dict[str, str] = {}
        self.kg_node_index: dict[str, str] = {}
        if unified_mapping_path and unified_mapping_path.exists():
            with open(unified_mapping_path) as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    chebi = row.get("chebi_id", "").strip()
                    if chebi.startswith("CHEBI:"):
                        self.cas_rn_index[chebi] = row.get("cas_rn", "").strip()
                        self.kg_node_index[chebi] = row.get("kg_microbe_node_id", "").strip()
            print(f"  Loaded CAS-RN/KG annotations for {len(self.cas_rn_index)} CHEBI IDs")

    # ------------------------------------------------------------------
    # Step 1: Collect ingredients from CultureMech YAML files
    # ------------------------------------------------------------------

    def collect_ingredients(self, media_dir: Path) -> dict[str, IngredientInfo]:
        """
        Scan all CultureMech normalized_yaml files and collect unique CHEBI ingredients.

        CHEBI extraction priority:
          1. term.id (if starts with CHEBI:)
          2. chebi_term.id (enriched field)
          3. Name-based fallback via name_to_chebi mapping

        Returns: chebi_id → IngredientInfo
        """
        ingredients: dict[str, IngredientInfo] = {}
        yaml_files = sorted(media_dir.rglob("*.yaml"))
        self.corpus = corpus_receipt(yaml_files, media_dir)
        self.occurrences = []
        print(f"  Collecting ingredients from {len(yaml_files)} YAML files...")

        for yaml_file in tqdm(yaml_files, desc="Scanning media"):
            data = yaml.safe_load(yaml_file.read_text())
            if not data or not isinstance(data, dict):
                raise ValueError(f"invalid media record: {yaml_file}")

            media_id = data.get("id", yaml_file.stem)

            for index, ing in enumerate(data.get("ingredients", []) or []):
                if not isinstance(ing, dict):
                    raise ValueError(f"invalid ingredient in {yaml_file}")
                chebi_id = self._extract_chebi(ing)
                direct_term = ing.get("term")
                chebi_term = ing.get("chebi_term")
                match_method = (
                    "unresolved"
                    if not chebi_id
                    else (
                        "direct_term"
                        if isinstance(direct_term, dict) and direct_term.get("id") == chebi_id
                        else (
                            "chebi_term"
                            if isinstance(chebi_term, dict) and chebi_term.get("id") == chebi_id
                            else "name_mapping"
                        )
                    )
                )
                self.occurrences.append(
                    {
                        "source_path": yaml_file.relative_to(media_dir).as_posix(),
                        "record_id": str(media_id),
                        "ingredient_index": index,
                        "chebi_id": chebi_id,
                        "match_method": match_method,
                    }
                )
                if not chebi_id:
                    continue

                name = ing.get("preferred_term", "").strip() or chebi_id

                if chebi_id not in ingredients:
                    ingredients[chebi_id] = IngredientInfo(
                        chebi_id=chebi_id,
                        preferred_term=name,
                        cas_rn=self.cas_rn_index.get(chebi_id, ""),
                        kg_node_id=self.kg_node_index.get(chebi_id, ""),
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

    def _extract_chebi(self, ing: dict) -> str | None:
        """Extract CHEBI ID from ingredient dict using priority order."""
        # 1. term.id (CHEBI)
        term = ing.get("term") or {}
        if isinstance(term, dict):
            tid = term.get("id", "")
            if tid.startswith("CHEBI:"):
                return tid

        # 2. chebi_term.id (enriched)
        chebi_term = ing.get("chebi_term") or {}
        if isinstance(chebi_term, dict):
            cid = chebi_term.get("id", "")
            if cid.startswith("CHEBI:"):
                return cid

        # 3. Name fallback
        name = ing.get("preferred_term", "").lower().strip()
        if name and name in self.name_to_chebi:
            val = self.name_to_chebi[name]
            # JSON values may be a list of CHEBI IDs; take the first
            if isinstance(val, list):
                val = val[0] if val else None
            if val and isinstance(val, str) and val.startswith("CHEBI:"):
                return val

        return None

    # ------------------------------------------------------------------
    # Step 2: Embed ingredients
    # ------------------------------------------------------------------

    def embed(
        self,
        ingredients: dict[str, IngredientInfo],
        embeddings_path: Path,
        cache_dir: Path = Path(".umap_cache"),
        force_reload: bool = False,
    ) -> dict[str, np.ndarray]:
        """
        Load KG-Microbe embeddings and look up each CHEBI ingredient.

        Returns: chebi_id → 512-dim embedding vector
        """
        print("Loading KG-Microbe embeddings (CHEBI nodes only)...")
        # Legacy pickle cache keys cannot establish source lineage. Verified
        # generation reads the actual selected source and retains its byte hash.
        source = GraphSource(embeddings_path, ["CHEBI"], node_ids=ingredients)
        embeddings_dict = {node: np.asarray(vector, dtype=np.float32) for node, vector in source}
        self.source_receipt = source.receipt

        found: dict[str, np.ndarray] = {}
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
        embedded: dict[str, np.ndarray],
        n_neighbors: int = 15,
        min_dist: float = 0.1,
        random_state: int = 42,
        method: str = "pacmap",
    ) -> pd.DataFrame:
        """Project graph vectors with an explicit, accurately reported reducer."""
        if method not in {"pacmap", "umap"}:
            raise ValueError(f"Unknown projection method: {method}")
        if not embedded:
            raise ValueError("No ingredient vectors to project")
        chebi_ids = sorted(embedded)
        matrix = np.array([embedded[c] for c in chebi_ids], dtype=np.float32)
        if len(matrix) < 3 or matrix.shape[1] < 2:
            raise ValueError("Projection requires at least three vectors and two dimensions")
        if not np.isfinite(matrix).all():
            raise ValueError("Ingredient vectors must be finite")
        if method == "pacmap":
            import pacmap
            from sklearn.preprocessing import normalize

            parameters = {
                "n_components": 2,
                "random_state": random_state,
                "n_neighbors": min(n_neighbors, len(matrix) - 1),
                "MN_ratio": 0.5,
                "FP_ratio": 2.0,
                "distance": "euclidean",
                "lr": 1.0,
                "num_iters": (100, 100, 250),
                "apply_pca": True,
                "knn_backend": "faiss",
            }
            actual_matrix = normalize(matrix)
            vectors = matrix_receipt(actual_matrix, chebi_ids)
            reducer = pacmap.PaCMAP(**parameters)
            coords = reducer.fit_transform(actual_matrix, init="pca")
            projection = projection_receipt(
                method, parameters, reducer=reducer, normalization="l2", initialization="pca"
            )
            projection["label"] = "PaCMAP"
        else:
            import umap

            parameters = {
                "n_neighbors": min(n_neighbors, len(matrix) - 1),
                "min_dist": min_dist,
                "n_components": 2,
                "metric": "cosine",
                "random_state": random_state,
                "verbose": False,
            }
            vectors = matrix_receipt(matrix, chebi_ids)
            reducer = umap.UMAP(**parameters)
            coords = reducer.fit_transform(matrix)
            projection = projection_receipt(
                method, parameters, reducer=reducer, normalization="none"
            )
            projection["label"] = "UMAP"
        if np.asarray(coords).shape != (len(matrix), 2) or not np.isfinite(coords).all():
            raise ValueError("Projection did not produce finite two-dimensional coordinates")
        projection["input_dimensions"] = matrix.shape[1]

        df = pd.DataFrame(
            {
                "chebi_id": chebi_ids,
                "umap_x": coords[:, 0],
                "umap_y": coords[:, 1],
            }
        )
        df.attrs["projection"] = projection
        df.attrs["matrix"] = vectors
        print(f"  {projection['label']} reduction complete")
        return df

    # ------------------------------------------------------------------
    # Step 4: Render HTML
    # ------------------------------------------------------------------

    def render_html(
        self,
        df: pd.DataFrame,
        ingredients: dict[str, IngredientInfo],
        output_path: Path,
        templates_dir: Path | None = None,
        *,
        graph_receipt: dict | None = None,
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
            points.append(
                {
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
                }
            )

        # Sort: most frequent last so they render on top
        points.sort(key=lambda p: p["count"])

        tier_counts = {
            "top100": sum(1 for p in points if p["tier"] == "top100"),
            "top500": sum(1 for p in points if p["tier"] == "top500"),
            "other": sum(1 for p in points if p["tier"] == "other"),
        }

        env = Environment(
            loader=FileSystemLoader(str(templates_dir)),
            autoescape=select_autoescape(["html"]),
        )
        template = env.get_template("ingredient_umap.html")

        html = template.render(
            projection=df.attrs.get(
                "projection", {"label": "Unverified projection", "input_dimensions": "unknown"}
            ),
            graph_receipt=graph_receipt,
            receipt_filename=output_path.with_suffix(".metadata.json").name,
            ingredient_data=points,
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
        method: str = "pacmap",
    ) -> None:
        """Run the full ingredient UMAP pipeline."""
        print("\n" + "=" * 60)
        print("STEP 1: Collecting ingredients")
        print("=" * 60)
        ingredients = self.collect_ingredients(media_dir)
        all_ingredients = dict(ingredients)

        if min_count > 1:
            before = len(ingredients)
            ingredients = {k: v for k, v in ingredients.items() if v.occurrence_count >= min_count}
            print(
                f"  Filtered to {len(ingredients)} ingredients (≥{min_count} occurrences, was {before})"
            )

        if dry_run:
            print(f"\nDRY RUN — would embed {len(ingredients)} ingredients")
            return

        print("\n" + "=" * 60)
        print("STEP 2: Loading embeddings")
        print("=" * 60)
        embedded = self.embed(ingredients, embeddings_path, cache_dir, force_reload)

        if not embedded:
            raise ValueError("No embeddings found. Check embeddings file path.")

        print("\n" + "=" * 60)
        print(f"STEP 3: {method.upper()} reduction")
        print("=" * 60)
        df = self.reduce(embedded, n_neighbors=n_neighbors, min_dist=min_dist, method=method)

        print("\n" + "=" * 60)
        print("STEP 4: Rendering HTML")
        print("=" * 60)
        ledger = []
        occurrences_by_chebi = {}
        for row in self.occurrences:
            occurrences_by_chebi.setdefault(row["chebi_id"], []).append(row)
        for identifier in sorted(all_ingredients):
            status = (
                "projected"
                if identifier in embedded
                else "below_min_count" if identifier not in ingredients else "missing_vector"
            )
            ledger.append(
                {
                    "identifier": identifier,
                    "source_nodes": [identifier] if identifier in embedded else [],
                    "status": status,
                    "match_method": "direct_graph_node",
                    "occurrences": occurrences_by_chebi.get(identifier, []),
                }
            )
        coverage = {
            "corpus_records": self.corpus["count"],
            "eligible": len(all_ingredients),
            "projected": len(embedded),
            "omitted": len(all_ingredients) - len(embedded),
            "ingredient_occurrences": len(self.occurrences),
            "unresolved_occurrences": sum(row["chebi_id"] is None for row in self.occurrences),
            "component_scope": "top-level ingredients",
            "minimum_occurrences": min_count,
        }
        receipt = make_receipt(
            source=self.source_receipt,
            corpus=self.corpus,
            ledger=ledger,
            matrix=df.attrs["matrix"],
            projection=df.attrs["projection"],
            coverage=coverage,
            auxiliary=self.auxiliary_receipts,
        )
        receipt["unresolved_occurrences"] = [
            row for row in self.occurrences if row["chebi_id"] is None
        ]
        output_html.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix=".ingredient-graph-", dir=output_html.parent
        ) as temporary:
            stage = Path(temporary)
            self.render_html(df, ingredients, stage / output_html.name, graph_receipt=receipt)
            points = stage / output_html.with_suffix(".points.json").name
            points.write_text(df.to_json(orient="records"))
            if corpus_receipt(sorted(media_dir.rglob("*.yaml")), media_dir) != self.corpus:
                raise ValueError("media corpus changed during graph generation")
            if any(
                file_sha256(path) != self.auxiliary_receipts[name]["sha256"]
                for name, path in self.auxiliary_paths.items()
            ):
                raise ValueError("mapping input changed during graph generation")
            publish_artifacts(
                {
                    output_html: stage / output_html.name,
                    output_html.with_suffix(".points.json"): points,
                },
                output_html.with_suffix(".metadata.json"),
                receipt,
            )

        print(f"\n✅ Ingredient graph complete → {output_html}")
