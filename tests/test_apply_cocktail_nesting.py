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


# --- splitting values the flattening SUMMED across two stocks (#150) ---------


VIT_A = [{"compound": "Pyridoxine hydrochloride", "g_l": 0.1},
         {"compound": "Nicotinic acid", "g_l": 0.05}]
VIT_B = [{"compound": "Pyridoxine hydrochloride", "g_l": 0.3},
         {"compound": "Nicotinic acid", "g_l": 0.2}]


def _two_vitamin_stocks():
    return [{"stock_components": VIT_A, "solution_name": "Wolin's", "addition_volume_ml": 1,
             "stock_prepared_in_ml": 1000},
            {"stock_components": VIT_B, "solution_name": "Seven vitamins",
             "addition_volume_ml": 1, "stock_prepared_in_ml": 1000}]


def test_find_summed_recognises_an_exact_two_stock_sum(acn):
    """pyridoxine 0.4 = Wolin's 0.1 + Seven vitamins 0.3."""
    ings = [_ing("Pyridoxine hydrochloride", "0.4")]
    got = acn.find_summed(ings, _two_vitamin_stocks(), ["pyridoxine hydrochloride"])
    assert got == {"pyridoxine hydrochloride": [("Wolin's", 0.1), ("Seven vitamins", 0.3)]}


def test_find_summed_refuses_a_value_that_does_not_reconcile(acn):
    """Silence beats a guessed decomposition: 0.35 is not 0.1 + 0.3."""
    ings = [_ing("Pyridoxine hydrochloride", "0.35")]
    assert acn.find_summed(ings, _two_vitamin_stocks(), ["pyridoxine hydrochloride"]) == {}


def test_split_is_opt_in(acn):
    """Without --split-summed the record is refused, not silently reconstructed."""
    doc = {"ingredients": [_ing("Pyridoxine hydrochloride", "0.4")]}
    plan = acn.plan_record(Path("x.yaml"), doc, _two_vitamin_stocks(),
                           {"pyridoxine hydrochloride"}, split_summed=False)
    assert plan is None or plan["unmatched"] == ["pyridoxine hydrochloride"]


def test_a_stock_contributing_only_summed_rows_still_gets_its_solution(acn):
    """The bug the canary caught. Both stocks' components were merged into one
    ingredient, so neither had a direct name+value match. Creating a group only for
    directly-matched stocks dropped one stock's share entirely — the record would
    silently lose Wolin's contribution."""
    doc = {"ingredients": [_ing("Pyridoxine hydrochloride", "0.4"),
                           _ing("Nicotinic acid", "0.25")]}
    plan = acn.plan_record(Path("x.yaml"), doc, _two_vitamin_stocks(),
                           {"pyridoxine hydrochloride", "nicotinic acid"}, split_summed=True)
    acn.apply_plan(doc, plan)
    names = [s["preferred_term"] for s in doc["solutions"]]
    assert set(names) == {"Wolin's", "Seven vitamins"}, names

    # mass conservation: each component's parts must re-sum to the flattened value
    totals: dict[str, float] = {}
    for s in doc["solutions"]:
        for c in s["composition"]:
            totals[c["preferred_term"]] = totals.get(c["preferred_term"], 0.0) + float(
                c["concentration"]["value"])
    assert abs(totals["Pyridoxine hydrochloride"] - 0.4) < 1e-9
    assert abs(totals["Nicotinic acid"] - 0.25) < 1e-9
    assert doc["ingredients"] == []


# --- researched stocks are gated to the media whose sheet was read (#150) ----


def test_source_medium_prefers_the_dsmz_stamp(acn):
    assert acn.source_medium({"notes": "Source: KOMODO | DSMZ Medium: 503 (mediadive.medium:503)"}) == "503"
    assert acn.source_medium({"notes": "DSMZ Medium: 298a"}) == "298a"
    # no stamp: fall back to the media_term id's local part
    assert acn.source_medium({"media_term": {"term": {"id": "komodo.medium:1083"}}}) == "1083"
    assert acn.source_medium({}) is None


def test_a_researched_stock_is_refused_for_an_unverified_medium(acn):
    """THE gate. An addition volume belongs to the CITING MEDIUM, not to the stock —
    MediaDive observes "Seven vitamins solution" at four different volumes. A record
    whose medium's sheet was never read must not inherit the volume by association."""
    stock = {"solution_name": "Seven vitamins solution", "addition_volume_ml": 1,
             "applies_to_media": ["503", "194"]}
    assert [s["solution_name"] for s in acn.stocks_for_record([stock], {"notes": "DSMZ Medium: 503"})] \
        == ["Seven vitamins solution"]
    assert acn.stocks_for_record([stock], {"notes": "DSMZ Medium: 298b"}) == []
    assert acn.stocks_for_record([stock], {}) == []


def test_a_stock_without_the_gate_stays_universal(acn):
    """`applies_to_media` is optional: a stock verified as medium-independent (or one
    whose citing media were all checked) applies wherever its composition matches."""
    stock = {"solution_name": "Trace salt solution", "addition_volume_ml": 1}
    assert len(acn.stocks_for_record([stock], {"notes": "DSMZ Medium: anything"})) == 1
    assert len(acn.stocks_for_record([stock], {})) == 1
