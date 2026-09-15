"""Ingredient map labels must describe the algorithm actually invoked."""
import runpy
import sys
import types
from pathlib import Path

import numpy as np
import pytest

from culturemech.visualization.ingredient_umap_generator import (
    IngredientInfo,
    IngredientUMAPGenerator,
)


@pytest.mark.parametrize("method,label", [("pacmap", "PaCMAP"), ("umap", "UMAP")])
def test_projection_dispatch_and_rendered_labels(tmp_path, monkeypatch, method, label):
    calls = []

    def reducer_for(name):
        class Reducer:
            def __init__(self, **kwargs):
                calls.append((name, kwargs))
                self.n_neighbors, self.n_MN, self.n_FP = 2, 1, 1
                self._n_neighbors = kwargs.get("n_neighbors", 2)

            def fit_transform(self, matrix, **kwargs):
                calls.append((matrix.copy(), kwargs))
                return np.arange(len(matrix) * 2).reshape(-1, 2)
        return Reducer

    monkeypatch.setitem(sys.modules, "pacmap", types.SimpleNamespace(PaCMAP=reducer_for("pacmap")))
    monkeypatch.setitem(sys.modules, "umap", types.SimpleNamespace(UMAP=reducer_for("umap")))
    generator = IngredientUMAPGenerator()
    vectors = {f"CHEBI:{i}": np.array([i + 1., 2., 3., 4.]) for i in range(5)}
    frame = generator.reduce(vectors, method=method)
    assert calls[0][0] == method
    assert frame.attrs["projection"]["input_dimensions"] == 4
    assert frame.attrs["projection"]["label"] == label
    if method == "pacmap":
        np.testing.assert_allclose(np.linalg.norm(calls[1][0], axis=1), 1., atol=1e-6)
        assert calls[1][1] == {"init": "pca"}
    else:
        assert calls[0][1]["n_neighbors"] == 4
    ingredients = {key: IngredientInfo(key, key) for key in vectors}
    out = tmp_path / "map.html"
    generator.render_html(frame, ingredients, out)
    html = out.read_text()
    assert f"CultureMech Ingredient {label}" in html
    assert f"4-dim DeepWalk, {label} 2D" in html


def test_default_is_pacmap_and_unsupported_or_small_input_fails(monkeypatch):
    generator = IngredientUMAPGenerator()
    assert generator.reduce.__defaults__[-1] == "pacmap"
    with pytest.raises(ValueError, match="Unknown projection"):
        generator.reduce({}, method="typo")
    with pytest.raises(ValueError, match="No ingredient"):
        generator.reduce({})
    with pytest.raises(ValueError, match="at least three"):
        generator.reduce({"CHEBI:1": np.ones(4)})


def test_cli_explicit_missing_source_does_not_run_generator(tmp_path, monkeypatch):
    script = Path(__file__).resolve().parents[1] / "scripts/generate_ingredient_umap.py"
    monkeypatch.setenv("KG_MICROBE_EMBEDDINGS", str(tmp_path / "missing.tsv.gz"))
    monkeypatch.setattr(sys, "argv", [str(script)])
    with pytest.raises(SystemExit) as error:
        runpy.run_path(str(script), run_name="__main__")
    assert error.value.code == 2


def test_default_graph_release_is_v3(monkeypatch):
    script = Path(__file__).resolve().parents[1] / "scripts/generate_ingredient_umap.py"
    monkeypatch.delenv("KG_MICROBE_EMBEDDINGS", raising=False)
    values = runpy.run_path(str(script))
    assert "512_v3_2026-06-26_12_55_27" in values["_EMBEDDINGS_FILENAME"]
