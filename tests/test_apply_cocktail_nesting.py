"""Pin the safety property of the cocktail nesting applier (#150).

The applier restructures real recipes: it moves ingredients out of `ingredients:`
into a `solutions:` entry. The way that goes catastrophically wrong is moving an
ingredient that is NOT part of the stock — a stock's component list overlaps the
medium's own bulk salts (Wolfe's mineral elixir contains NaCl 10 g/l; a marine
medium separately carries NaCl 39.97 g/l as a bulk ingredient).

So matching is on NAME **and** VALUE, and these tests exist to keep it that way.
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
def acn():
    return _load("apply_cocktail_nesting")


def _ing(name, value):
    return {"preferred_term": name, "concentration": {"value": value, "unit": "G_PER_L"}}


STOCK = [  # Wolfe's mineral elixir, as MediaDive returns it
    {"compound": "MnSO4 x H2O", "g_l": 5},
    {"compound": "FeSO4 x 7 H2O", "g_l": 1},
    {"compound": "NaCl", "g_l": 10},
]


def test_a_bulk_ingredient_sharing_a_name_is_not_moved(acn):
    """THE safety test. NaCl appears in the stock at 10 g/l and in the medium at
    39.97 g/l as a bulk salt. Moving the bulk one would destroy the recipe."""
    ingredients = [_ing("NaCl", "39.97"), _ing("MnSO4 x H2O", "5")]
    flagged = {"nacl", "mnso4 x h2o"}
    indices, unmatched = acn.match_components(ingredients, STOCK, flagged)
    assert indices == [1], "only the stock-valued MnSO4 may move"
    assert "nacl" in unmatched


def test_matching_requires_the_flag(acn):
    """An unflagged ingredient is never eligible, even on an exact name+value hit."""
    ingredients = [_ing("MnSO4 x H2O", "5")]
    indices, _ = acn.match_components(ingredients, STOCK, flagged_names=set())
    assert indices == []


def test_exact_value_match_is_required(acn):
    ingredients = [_ing("FeSO4 x 7 H2O", "0.5")]     # stock says 1
    indices, unmatched = acn.match_components(ingredients, STOCK, {"feso4 x 7 h2o"})
    assert indices == [] and unmatched == ["feso4 x 7 h2o"]


def test_hydrate_names_do_not_collapse(acn):
    """"MgSO4" and "MgSO4 x 7 H2O" are different compounds; matching must not be fuzzy."""
    ingredients = [_ing("MnSO4", "5")]               # anhydrous, stock has the monohydrate
    indices, _ = acn.match_components(ingredients, STOCK, {"mnso4"})
    assert indices == []


def test_plan_refuses_a_record_that_already_has_solutions(acn):
    doc = {"solutions": [{"preferred_term": "x"}], "ingredients": [_ing("MnSO4 x H2O", "5")]}
    assert acn.plan_record(Path("x.yaml"), doc,
                           [{"stock_components": STOCK, "solution_name": "s",
                             "addition_volume_ml": 1, "stock_prepared_in_ml": 1000}],
                           {"mnso4 x h2o"}) is None


def test_apply_moves_only_matched_and_keeps_the_rest(acn):
    doc = {"ingredients": [_ing("NaCl", "39.97"), _ing("MnSO4 x H2O", "5"),
                           _ing("FeSO4 x 7 H2O", "1")]}
    plan = acn.plan_record(
        Path("x.yaml"), doc,
        [{"stock_components": STOCK, "solution_name": "Wolfe's mineral elixir",
          "addition_volume_ml": 1, "stock_prepared_in_ml": 1000}],
        {"nacl", "mnso4 x h2o", "feso4 x 7 h2o"})
    acn.apply_plan(doc, plan)

    assert [i["preferred_term"] for i in doc["ingredients"]] == ["NaCl"], "bulk NaCl must stay"
    sol = doc["solutions"][0]
    assert sol["preferred_term"] == "Wolfe's mineral elixir"
    assert sol["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    assert [c["preferred_term"] for c in sol["composition"]] == ["MnSO4 x H2O", "FeSO4 x 7 H2O"]
    assert doc["curation_history"][-1]["action"] == "NESTED_FLATTENED_COCKTAIL"


def test_two_stocks_are_nested_separately(acn):
    """A medium with a trace stock AND a vitamin stock gets one solution each; nesting
    only the first would strand the vitamins and half-repair the record."""
    vitamins = [{"compound": "Biotin", "g_l": 0.02}]
    doc = {"ingredients": [_ing("MnSO4 x H2O", "5"), _ing("Biotin", "0.02")]}
    plan = acn.plan_record(
        Path("x.yaml"), doc,
        [{"stock_components": STOCK, "solution_name": "Trace", "addition_volume_ml": 1,
          "stock_prepared_in_ml": 1000},
         {"stock_components": vitamins, "solution_name": "Vitamins",
          "addition_volume_ml": 10, "stock_prepared_in_ml": 1000}],
        {"mnso4 x h2o", "biotin"})
    acn.apply_plan(doc, plan)
    assert doc["ingredients"] == []
    assert [s["preferred_term"] for s in doc["solutions"]] == ["Trace", "Vitamins"]
    assert doc["solutions"][1]["concentration"]["value"] == "10"


def test_an_ingredient_is_never_claimed_by_two_stocks(acn):
    """If two stocks list the same component at the same value, the first wins —
    duplicating it into both solutions would invent an ingredient."""
    doc = {"ingredients": [_ing("MnSO4 x H2O", "5")]}
    same = [{"compound": "MnSO4 x H2O", "g_l": 5}]
    plan = acn.plan_record(
        Path("x.yaml"), doc,
        [{"stock_components": same, "solution_name": "A", "addition_volume_ml": 1,
          "stock_prepared_in_ml": 1000},
         {"stock_components": same, "solution_name": "B", "addition_volume_ml": 1,
          "stock_prepared_in_ml": 1000}],
        {"mnso4 x h2o"})
    assert len(plan["groups"]) == 1 and plan["moved_total"] == 1
