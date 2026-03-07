"""
Embedding module for loading and processing KG-Microbe embeddings.
"""

from culturemech.embedding.loader import EmbeddingLoader
from culturemech.embedding.aggregator import MediaVectorAggregator
from culturemech.embedding.dimensionality import reduce_to_2d

__all__ = ["EmbeddingLoader", "MediaVectorAggregator", "reduce_to_2d"]
