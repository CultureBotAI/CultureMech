"""
UMAP dimensionality reduction for embeddings visualization.
"""

from typing import Dict

import numpy as np
import pandas as pd
from culturemech.embedding.aggregator import MediaEmbedding


def reduce_to_2d(
    embeddings_dict: Dict[str, MediaEmbedding],
    n_neighbors: int = 15,
    min_dist: float = 0.1,
    metric: str = "cosine",
    random_state: int = 42,
    method: str = "pacmap",
) -> pd.DataFrame:
    """
    Reduce embeddings to 2D using PaCMAP (default) or UMAP.

    Args:
        embeddings_dict: Dictionary mapping medium IDs to MediaEmbedding objects
        n_neighbors: UMAP n_neighbors parameter (controls local vs global structure)
        min_dist: UMAP min_dist parameter (controls compactness)
        metric: Distance metric (cosine, euclidean, etc.) — used by the UMAP branch
        random_state: Random seed for reproducibility
        method: Reducer to use, one of "pacmap" (default) or "umap"

    Returns:
        DataFrame with columns [medium_id, umap_x, umap_y]

    Note:
        The output column names are kept as ``umap_x``/``umap_y`` regardless of
        the reducer used, because downstream JSON/template code depends on them.
    """
    if not embeddings_dict:
        return pd.DataFrame(columns=["medium_id", "umap_x", "umap_y"])

    # Prepare data
    medium_ids = list(embeddings_dict.keys())
    embedding_matrix = np.array(
        [embeddings_dict[mid].embedding for mid in medium_ids], dtype=np.float32
    )

    print(
        f"Reducing {len(medium_ids):,} embeddings from {embedding_matrix.shape[1]}D "
        f"to 2D using {method}..."
    )

    if method == "pacmap":
        from sklearn.preprocessing import normalize
        import pacmap

        # L2-normalize rows so Euclidean (PaCMAP's metric) approximates the
        # cosine distance UMAP used.
        X = normalize(embedding_matrix.astype("float32"))
        reducer = pacmap.PaCMAP(n_components=2, random_state=random_state)
        coords = reducer.fit_transform(X, init="pca")
    elif method == "umap":
        import umap

        reducer = umap.UMAP(
            n_neighbors=n_neighbors,
            min_dist=min_dist,
            n_components=2,
            metric=metric,
            random_state=random_state,
            verbose=False,
        )
        coords = reducer.fit_transform(embedding_matrix)
    elif method == "sfdp":
        # Force-directed (Graphviz sfdp) layout of the mutual-kNN graph over the
        # KG embeddings — a global-structure-first graph view.
        from culturemech.embedding.graph_layout import sfdp_layout

        coords = sfdp_layout(embedding_matrix, k=15, seed=random_state)
    else:
        raise ValueError(
            f"Unknown reduction method: {method!r} (expected 'pacmap', 'umap', or 'sfdp')"
        )

    # Create DataFrame (column names kept as umap_x/umap_y for downstream compat)
    df = pd.DataFrame(
        {"medium_id": medium_ids, "umap_x": coords[:, 0], "umap_y": coords[:, 1]}
    )

    print(f"✓ {method} reduction complete")
    return df
