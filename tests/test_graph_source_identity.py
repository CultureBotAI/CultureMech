"""Ordinary loaders must read replaced graph bytes without an mtime cache hit."""

import gzip
import os
import pickle

import numpy as np

from culturemech.embedding.loader import EmbeddingLoader


def test_same_size_same_mtime_source_replacement_is_not_a_cache_hit(tmp_path):
    path = tmp_path / "same-name.tsv.gz"
    cache = tmp_path / "cache"
    cache.mkdir()

    def replace(a, b):
        path.write_bytes(gzip.compress(f"node\td1\td2\nCHEBI:1\t{a}\t{b}\n".encode(), mtime=0))

    replace(1, 2)
    before = path.stat()
    first = EmbeddingLoader.load_embeddings(path, ["CHEBI"], cache_dir=cache)
    # Existing unbound pickles cannot establish which source supplied vectors.
    (cache / "old-embeddings.pkl").write_bytes(pickle.dumps({"CHEBI:1": np.array([99.0, 99.0])}))
    replace(3, 4)
    assert path.stat().st_size == before.st_size
    os.utime(path, ns=(before.st_atime_ns, before.st_mtime_ns))
    second = EmbeddingLoader.load_embeddings(path, ["CHEBI"], cache_dir=cache)
    np.testing.assert_array_equal(first["CHEBI:1"], [1.0, 2.0])
    np.testing.assert_array_equal(second["CHEBI:1"], [3.0, 4.0])
