"""Unit-test the MediaDive addition-volume extraction (#150).

The cocktail repair turns on ONE number per record: the volume at which a stock
trace/vitamin solution is added to the medium. MediaDive states it structurally, as
a solution-to-solution reference inside a medium's recipe. These tests pin that
extraction — offline, against the real response shape — because the two volumes in
play are easy to confuse:

    addition_volume_ml    what the medium takes      (1 ml)      <- the one we need
    stock_prepared_in_ml  what the stock is made up to (1000 ml)

Using the second as the first would understate every concentration by ~1000x, which
is the same class of error the whole audit exists to find.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def fsv():
    return _load("fetch_mediadive_solution_volumes")


# The real shape of /rest/medium/1083 (ACIDULIPROFUNDUM MEDIUM), trimmed.
MEDIUM_1083 = {
    "medium": {"id": 1083, "name": "ACIDULIPROFUNDUM MEDIUM"},
    "solutions": [
        {
            "id": 2192, "name": "Main sol. 1083", "volume": 1001,
            "recipe": [
                {"recipe_order": 1, "compound": "NaCl", "amount": 30, "unit": "g", "g_l": 29.97},
                {"recipe_order": 9, "solution": "Wolfe's mineral elixir",
                 "solution_id": 1605, "amount": 1, "unit": "ml"},
                {"recipe_order": 16, "compound": "Distilled water", "amount": 1000, "unit": "ml"},
            ],
        },
        {
            "id": 1605, "name": "Wolfe's mineral elixir", "volume": 1000,
            "recipe": [
                {"compound": "MnSO4 x H2O", "amount": 5, "unit": "g", "g_l": 5},
                {"compound": "FeSO4 x 7 H2O", "amount": 1, "unit": "g", "g_l": 1},
                {"compound": "CoCl2 x 6 H2O", "amount": 1.8, "unit": "g", "g_l": 1.8},
            ],
        },
    ],
}


def test_extracts_the_addition_volume_not_the_stock_volume(fsv):
    """1 ml (what the medium takes), NOT 1000 ml (what the stock is prepared in)."""
    additions = fsv.extract_additions(MEDIUM_1083)
    assert len(additions) == 1
    a = additions[0]
    assert a["solution_name"] == "Wolfe's mineral elixir"
    assert a["addition_volume_ml"] == 1
    assert a["stock_prepared_in_ml"] == 1000


def test_carries_the_stock_composition(fsv):
    """The stock's own recipe is what gets nested under the solution."""
    comps = fsv.extract_additions(MEDIUM_1083)[0]["stock_components"]
    assert [c["compound"] for c in comps] == ["MnSO4 x H2O", "FeSO4 x 7 H2O", "CoCl2 x 6 H2O"]
    assert comps[0]["g_l"] == 5


def test_a_plain_compound_is_not_an_addition(fsv):
    """NaCl and distilled water are components, not stock-solution references."""
    names = [a["solution_name"] for a in fsv.extract_additions(MEDIUM_1083)]
    assert "NaCl" not in names and "Distilled water" not in names


def test_a_non_cocktail_solution_reference_is_ignored(fsv):
    """Only trace/vitamin/elixir-type stocks are cocktails; a buffer reference is not."""
    medium = {"solutions": [{
        "id": 1, "name": "Main", "volume": 1000,
        "recipe": [{"solution": "Phosphate buffer", "solution_id": 9, "amount": 50, "unit": "ml"}],
    }]}
    assert fsv.extract_additions(medium) == []


def test_a_reference_without_ml_units_is_ignored(fsv):
    """No ml unit means no volume can be read; silence beats a wrong number."""
    medium = {"solutions": [{
        "id": 1, "name": "Main", "volume": 1000,
        "recipe": [{"solution": "Trace element solution", "solution_id": 9,
                    "amount": 2, "unit": "g"}],
    }]}
    assert fsv.extract_additions(medium) == []


def test_mediadive_id_accepts_only_mediadive_numeric_ids(fsv):
    """A komodo.medium id is NOT a MediaDive id — they collide numerically (#239:
    KOMODO 3136 is MediaDive 1203), so treating one as the other fetches the wrong
    medium's composition."""
    assert fsv.mediadive_id({"media_term": {"term": {"id": "mediadive.medium:1083"}}}) == "1083"
    assert fsv.mediadive_id({"media_term": {"term": {"id": "mediadive.medium:734a"}}}) == "734a"
    assert fsv.mediadive_id({"media_term": {"term": {"id": "komodo.medium:3136"}}}) is None
    assert fsv.mediadive_id({"media_term": {"term": {"id": "mediadive.medium:J390"}}}) is None
    assert fsv.mediadive_id({}) is None
