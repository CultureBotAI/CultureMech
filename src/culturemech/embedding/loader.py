"""Load graph source vectors directly; legacy unbound caches are not reused."""

import gzip
import hashlib
import pickle
from pathlib import Path

import numpy as np
from tqdm import tqdm

from culturemech.graph_embedding_receipts import GraphSource


class EmbeddingLoader:
    """Read KG-Microbe node vectors directly from the selected source."""

    @staticmethod
    def load_embeddings(
        embeddings_path: Path,
        node_prefixes: list[str] | None = None,
        cache_dir: Path | None = None,
        force_reload: bool = False,
    ) -> dict[str, np.ndarray]:
        """
        Load vectors directly; legacy caches cannot establish source identity.

        Args:
            embeddings_path: Path to embeddings TSV.gz file
            node_prefixes: List of node prefixes to load (e.g., ['CHEBI', 'NCBITaxon'])
                          If None, uses the supported biological/ingredient prefixes
            cache_dir: Retained for API compatibility; legacy caches are ignored
            force_reload: Retained for API compatibility; source is always read

        Returns:
            Dictionary mapping node IDs to embedding vectors (np.ndarray)
        """
        if node_prefixes is None:
            node_prefixes = [
                "CHEBI",
                "NCBITaxon",
                "mediadive.medium",
                "mediadive.solution",
                "FOODON",
                "mediadive.ingredient",
                "mediadive.compound",
            ]
        # Legacy pickle caches have no immutable source binding (#472).
        # Keep their private helpers for compatibility, but never reuse them.
        source = GraphSource(embeddings_path, node_prefixes)
        return {node: np.asarray(vector, dtype=np.float32) for node, vector in source}

    @staticmethod
    def _cache_key(embeddings_path: Path, node_prefixes: list[str]) -> str:
        """Historical cache key retained only for compatibility.

        Basename, size and mtime cannot bind source content. Public loading
        never consults these old cache files.
        """
        try:
            stat = embeddings_path.stat()
            fp = f"{stat.st_size}-{int(stat.st_mtime)}"
        except FileNotFoundError:
            fp = "missing"
        prefix_tag = "_".join(sorted(node_prefixes))
        digest = hashlib.sha1(f"{embeddings_path.name}|{fp}|{prefix_tag}".encode()).hexdigest()[:12]
        return f"{prefix_tag}__{digest}_embeddings.pkl"

    @staticmethod
    def _try_load_from_cache(cache_file: Path) -> dict[str, np.ndarray] | None:
        """Try to load embeddings from a pickle cache file."""
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
    def _load_from_source(embeddings_path: Path, node_prefixes: list[str]) -> dict[str, np.ndarray]:
        """Load embeddings from TSV.gz source file."""
        embeddings: dict[str, np.ndarray] = {}

        with gzip.open(embeddings_path, "rt") as f:
            # Count total lines for progress bar
            print("Counting lines...")
            total_lines = sum(1 for _ in f) - 1  # Subtract header
            f.seek(0)

            # Skip header
            next(f)

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
    def _save_to_cache(cache_file: Path, embeddings: dict[str, np.ndarray]) -> None:
        """Save embeddings to pickle cache. Cache filename is provided by
        the caller (already keyed on source identity + prefix set)."""
        try:
            with open(cache_file, "wb") as f:
                pickle.dump(embeddings, f, protocol=pickle.HIGHEST_PROTOCOL)
            print(f"✓ Saved cache: {cache_file}")
        except Exception as e:
            print(f"⚠ Cache save failed: {e}")
