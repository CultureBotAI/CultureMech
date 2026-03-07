"""
Embedding loader for KG-Microbe embeddings with caching support.

Loads embeddings from TSV.gz file and caches as pickle for fast reloading.
"""

import gzip
import pickle
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
from tqdm import tqdm


class EmbeddingLoader:
    """Load and cache KG-Microbe node embeddings."""

    @staticmethod
    def load_embeddings(
        embeddings_path: Path,
        node_prefixes: Optional[List[str]] = None,
        cache_dir: Optional[Path] = None,
        force_reload: bool = False,
    ) -> Dict[str, np.ndarray]:
        """
        Load embeddings from TSV.gz file with pickle caching.

        Args:
            embeddings_path: Path to embeddings TSV.gz file
            node_prefixes: List of node prefixes to load (e.g., ['CHEBI', 'NCBITaxon'])
                          If None, loads all nodes
            cache_dir: Directory for pickle cache files
            force_reload: If True, bypass cache and reload from source

        Returns:
            Dictionary mapping node IDs to embedding vectors (np.ndarray)
        """
        if node_prefixes is None:
            node_prefixes = ["CHEBI", "NCBITaxon", "mediadive.medium", "FOODON"]

        if cache_dir is None:
            cache_dir = Path(".umap_cache")

        cache_dir.mkdir(exist_ok=True)

        # Load from cache if available
        if not force_reload:
            embeddings = EmbeddingLoader._try_load_from_cache(cache_dir, node_prefixes)
            if embeddings is not None:
                print(f"✓ Loaded {len(embeddings):,} embeddings from cache")
                return embeddings

        # Load from source file
        print(f"Loading embeddings from {embeddings_path}...")
        embeddings = EmbeddingLoader._load_from_source(embeddings_path, node_prefixes)

        # Save to cache
        EmbeddingLoader._save_to_cache(cache_dir, embeddings, node_prefixes)

        print(f"✓ Loaded {len(embeddings):,} embeddings")
        return embeddings

    @staticmethod
    def _try_load_from_cache(
        cache_dir: Path, node_prefixes: List[str]
    ) -> Optional[Dict[str, np.ndarray]]:
        """Try to load embeddings from pickle cache."""
        cache_file = cache_dir / f"{'_'.join(sorted(node_prefixes))}_embeddings.pkl"

        if not cache_file.exists():
            return None

        try:
            with open(cache_file, "rb") as f:
                embeddings = pickle.load(f)
            print(f"✓ Loaded from cache: {cache_file}")
            return embeddings
        except Exception as e:
            print(f"⚠ Cache load failed: {e}")
            return None

    @staticmethod
    def _load_from_source(
        embeddings_path: Path, node_prefixes: List[str]
    ) -> Dict[str, np.ndarray]:
        """Load embeddings from TSV.gz source file."""
        embeddings: Dict[str, np.ndarray] = {}

        with gzip.open(embeddings_path, "rt") as f:
            # Count total lines for progress bar
            print("Counting lines...")
            total_lines = sum(1 for _ in f) - 1  # Subtract header
            f.seek(0)

            # Skip header
            header = next(f)

            # Parse embeddings
            for line in tqdm(f, total=total_lines, desc="Loading embeddings"):
                node_id, embedding = EmbeddingLoader._parse_embedding_line(line)

                # Filter by prefix
                if any(node_id.startswith(prefix) for prefix in node_prefixes):
                    embeddings[node_id] = embedding

        return embeddings

    @staticmethod
    def _parse_embedding_line(line: str) -> tuple[str, np.ndarray]:
        """Parse a single line from embeddings TSV."""
        parts = line.strip().split("\t")
        node_id = parts[0]
        embedding = np.array([float(x) for x in parts[1:]], dtype=np.float32)
        return node_id, embedding

    @staticmethod
    def _save_to_cache(
        cache_dir: Path, embeddings: Dict[str, np.ndarray], node_prefixes: List[str]
    ) -> None:
        """Save embeddings to pickle cache."""
        cache_file = cache_dir / f"{'_'.join(sorted(node_prefixes))}_embeddings.pkl"

        try:
            with open(cache_file, "wb") as f:
                pickle.dump(embeddings, f, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"✓ Saved cache: {cache_file}")
        except Exception as e:
            print(f"⚠ Cache save failed: {e}")
