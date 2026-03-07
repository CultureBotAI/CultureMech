"""
UMAP dimensionality reduction for embeddings visualization.
"""

from typing import Dict

import numpy as np
import pandas as pd
import umap
from culturemech.embedding.aggregator import MediaEmbedding


def reduce_to_2d(
    embeddings_dict: Dict[str, MediaEmbedding],
    n_neighbors: int = 15,
    min_dist: float = 0.1,
    metric: str = "cosine",
    random_state: int = 42,
) -> pd.DataFrame:
    """
    Reduce embeddings to 2D using UMAP.

    Args:
        embeddings_dict: Dictionary mapping medium IDs to MediaEmbedding objects
        n_neighbors: UMAP n_neighbors parameter (controls local vs global structure)
        min_dist: UMAP min_dist parameter (controls compactness)
        metric: Distance metric (cosine, euclidean, etc.)
        random_state: Random seed for reproducibility

    Returns:
        DataFrame with columns [medium_id, umap_x, umap_y]
    """
    if not embeddings_dict:
        return pd.DataFrame(columns=["medium_id", "umap_x", "umap_y"])

    # Prepare data
    medium_ids = list(embeddings_dict.keys())
    embedding_matrix = np.array(
        [embeddings_dict[mid].embedding for mid in medium_ids], dtype=np.float32
    )

    print(f"Reducing {len(medium_ids):,} embeddings from {embedding_matrix.shape[1]}D to 2D...")

    # Apply UMAP
    reducer = umap.UMAP(
        n_neighbors=n_neighbors,
        min_dist=min_dist,
        n_components=2,
        metric=metric,
        random_state=random_state,
        verbose=False,
    )

    umap_coords = reducer.fit_transform(embedding_matrix)

    # Create DataFrame
    df = pd.DataFrame(
        {"medium_id": medium_ids, "umap_x": umap_coords[:, 0], "umap_y": umap_coords[:, 1]}
    )

    print(f"✓ UMAP reduction complete")
    return df
