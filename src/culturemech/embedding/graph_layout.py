"""Force-directed 2D layout of a mutual-kNN graph over embeddings, via Graphviz sfdp.

Self-contained: scikit-learn (kNN) + the `sfdp` binary (Graphviz). No pygraphviz/
pydot needed. Deterministic-ish via -Gstart=<seed>. Rows are L2-normalized so the
Euclidean kNN mirrors the cosine metric used elsewhere. Output row order == input.
"""
import subprocess
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.neighbors import kneighbors_graph


def sfdp_layout(matrix, k=15, seed=42, sfdp_bin="sfdp"):
    """Return an (n, 2) float32 array of 2D coordinates for the rows of `matrix`."""
    matrix = normalize(np.asarray(matrix, dtype="float32"))
    n = matrix.shape[0]
    if n == 0:
        return np.zeros((0, 2), dtype="float32")
    k = min(k, max(1, n - 1))
    A = kneighbors_graph(matrix, n_neighbors=k, mode="connectivity")
    A = A.maximum(A.T)  # symmetric union-kNN graph
    coo = A.tocoo()
    edges = {(min(i, j), max(i, j)) for i, j in zip(coo.row.tolist(), coo.col.tolist()) if i != j}
    dot = "\n".join(["graph G {"] + [f"{i};" for i in range(n)]
                    + [f"{i}--{j};" for i, j in edges] + ["}"])
    out = subprocess.run(
        [sfdp_bin, "-Tplain", f"-Gstart={seed}", "-Goverlap=prism", "-Gsmoothing=triangle"],
        input=dot, capture_output=True, text=True, timeout=900,
    )
    if out.returncode != 0:
        raise RuntimeError(f"sfdp failed (is graphviz installed?): {out.stderr[:300]}")
    xy = np.zeros((n, 2), dtype="float32")
    for ln in out.stdout.splitlines():
        if ln.startswith("node "):
            p = ln.split()
            idx = int(p[1]); xy[idx, 0] = float(p[2]); xy[idx, 1] = float(p[3])
    return xy
