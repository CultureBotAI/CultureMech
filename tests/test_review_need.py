"""Tests for the review-need scorer.

The scorer is the inverse of `prioritize_deep_research_candidates`: that one ranks
by expected research yield and hard-filters zero-ingredient records, so the
damaged tail is invisible to it. These tests pin the signals that surface that
tail, and — more importantly — pin that ordinary records score low, since a
ranking that flags everything ranks nothing.
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
def srn():
    return _load("score_review_need")


def _ing(name, grounded=True):
    d = {"preferred_term": name}
    if grounded:
        d["term"] = {"id": "CHEBI:12345"}
    return d


def _healthy():
    """A record with nothing wrong with it."""
    return {
        "name": "lb_broth",
        "original_name": "LB broth",
        "media_term": {"preferred_term": "DSMZ Medium 381"},
        "notes": "Source: DSMZ",
        "ph_value": 7.0,
        "ingredients": [_ing("Tryptone"), _ing("Yeast extract"), _ing("NaCl")],
    }


# --- the signals ----------------------------------------------------------


def test_a_healthy_record_scores_zero(srn):
    """The load-bearing test: a ranking that flags everything ranks nothing."""
    score, reasons = srn.score_record(_healthy())
    assert score == 0, reasons


def test_no_ingredients_scores_highest_single_signal(srn):
    doc = _healthy() | {"ingredients": []}
    score, reasons = srn.score_record(doc)
    assert "no ingredients" in "; ".join(reasons)
    assert score >= 30


def test_placeholder_ingredient_text_is_flagged(srn):
    doc = _healthy() | {"ingredients": [_ing("See source for composition", grounded=False)]}
    score, reasons = srn.score_record(doc)
    joined = "; ".join(reasons)
    assert "placeholder" in joined and "grounded" in joined


def test_unparsed_recipe_in_an_ingredient_name_is_flagged(srn):
    """The NBRC_1197 shape (#166): a whole composition block in one field."""
    doc = _healthy() | {"ingredients": [
        _ing("Substrates*10mMKH2PO40.85gNa2HPO4x7H2O4.9g(NH4)2SO40.5gMgSO4")]}
    _, reasons = srn.score_record(doc)
    assert "unparsed recipe" in "; ".join(reasons)


def test_ungrounded_ingredients_are_flagged(srn):
    doc = _healthy() | {"ingredients": [_ing("A", False), _ing("B", False), _ing("C", False)]}
    _, reasons = srn.score_record(doc)
    assert "no ingredient is grounded" in "; ".join(reasons)


def test_partial_grounding_scores_less_than_none(srn):
    none_g = _healthy() | {"ingredients": [_ing("A", False), _ing("B", False),
                                           _ing("C", False), _ing("D", False)]}
    half_g = _healthy() | {"ingredients": [_ing("A", True), _ing("B", False),
                                           _ing("C", False), _ing("D", False)]}
    assert srn.score_record(none_g)[0] > srn.score_record(half_g)[0]


def test_a_bare_strain_pointer_name_is_flagged(srn):
    doc = _healthy() | {"original_name": "For DSM 13514"}
    _, reasons = srn.score_record(doc)
    assert "identifies a strain" in "; ".join(reasons)


@pytest.mark.parametrize("name", ["BG11", "JM", "CH"])
def test_short_but_real_medium_names_are_not_flagged(srn, name):
    """BG11 and JM are real media. An earlier draft flagged short names and caught
    284 records, most of them legitimate — so name length is not used as a signal."""
    doc = _healthy() | {"original_name": name}
    _, reasons = srn.score_record(doc)
    assert not any("strain" in r or "name" in r for r in reasons), reasons


def test_missing_provenance_is_flagged(srn):
    doc = _healthy()
    del doc["media_term"]
    del doc["notes"]
    joined = "; ".join(srn.score_record(doc)[1])
    assert "media_term" in joined and "provenance" in joined


def test_missing_conditions_is_weighted_low(srn):
    """It fires on 51% of the corpus, so it must not dominate a rarer, worse signal."""
    no_cond = _healthy()
    del no_cond["ph_value"]
    cond_score = srn.score_record(no_cond)[0]
    worse = _healthy() | {"ingredients": []}
    assert cond_score < srn.score_record(worse)[0]


def test_signals_accumulate(srn):
    """A record that is wrong in several ways must outrank one wrong in a single way."""
    one = _healthy() | {"ingredients": []}
    many = {"name": "x", "original_name": "For DSM 999", "ingredients": []}
    assert srn.score_record(many)[0] > srn.score_record(one)[0]


# --- the corpus -----------------------------------------------------------


def _rank(srn, corpus):
    """Score the session-scoped corpus instead of re-reading it (#189)."""
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    return srn.score_parsed([(str(p.relative_to(normalized)), d) for p, d in corpus])


def test_known_bad_records_rank_near_the_top(srn, corpus):
    """Validation against records independently confirmed broken.

    NBRC_1197 carries an unparsed recipe (#166); test_medium_123 is a literal test
    fixture sitting in the production corpus.
    """
    rows = _rank(srn, corpus)
    assert rows, "scorer returned nothing"
    top = [r["file_path"] for r in rows[:60]]
    assert "bacterial/NBRC_1197.yaml" in top, "NBRC_1197 (unparsed recipe) not in the worst 60"

    # test_medium_123 is checked by SCORE, not rank. #175 lifted its "See source
    # for composition" placeholder to `ingredients: []`, so it scores `no
    # ingredients` (30) instead of `placeholder text` (25) + `only 1-2` (15); the
    # reshuffle drops it just outside the worst 60 (score 45, ~rank 106). Still
    # severe, which is the property this test defends — rank is brittle to corpus
    # size, the score is the signal.
    by_score = {r["file_path"]: int(r["score"]) for r in rows}
    assert by_score.get("bacterial/test_medium_123.yaml", 0) >= 40, (
        "test_medium_123 (empty test fixture) should still score as severely broken")


def test_most_of_the_corpus_is_not_flagged_as_severe(srn, corpus):
    """If a large share scored severe, the ranking would carry no information."""
    rows = _rank(srn, corpus)
    severe = [r for r in rows if r["score"] >= 50]
    assert len(severe) < 500, f"{len(severe)} records scored >=50; the weights are too loose"


def test_a_norm_level_signal_alone_does_not_qualify_a_record(srn, tmp_path):
    """#177: any non-zero score used to emit a row, so 4,332 records appeared in
    the report solely for lacking a pH value — a slot 51% of the corpus omits.

    That is the failure this whole scorer exists to avoid, one layer up: 60% of the
    corpus in a "needs review" file buries the 42 that are genuinely broken.
    Conditions refine the ranking among already-suspect records; they must not
    qualify one on their own.
    """
    import yaml as _yaml

    d = tmp_path / "bacterial"
    d.mkdir()
    healthy_but_no_conditions = {
        "id": "CultureMech:1", "name": "x", "original_name": "Nutrient Agar",
        "media_term": {"preferred_term": "DSMZ 1"}, "notes": "Source: DSMZ",
        # 3 ingredients: fewer would also trip the "only 1-2 ingredients" signal
        # and the record would no longer be conditions-only.
        "ingredients": [{"preferred_term": n, "term": {"id": "CHEBI:1"}}
                        for n in ("Peptone", "Yeast extract", "NaCl")],
    }
    (d / "a.yaml").write_text(_yaml.dump(healthy_but_no_conditions))

    score, reasons = srn.score_record(healthy_but_no_conditions)
    assert score > 0 and reasons == ["no pH and no temperature"], reasons
    assert srn.collect(tmp_path) == [], "a conditions-only record must not be emitted"


def test_conditions_still_contribute_when_something_else_is_wrong(srn, tmp_path):
    """The signal is a tiebreaker, not deleted — a suspect record missing
    conditions should outrank an otherwise identical one that has them."""
    import yaml as _yaml

    d = tmp_path / "bacterial"
    d.mkdir()
    broken = {"id": "CultureMech:2", "name": "y", "original_name": "Y",
              "media_term": {"preferred_term": "z"}, "notes": "n", "ingredients": []}
    (d / "b.yaml").write_text(_yaml.dump(broken))
    rows = srn.collect(tmp_path)
    assert len(rows) == 1
    assert "no pH and no temperature" in rows[0]["reasons"]
    assert rows[0]["score"] > srn.score_record(broken | {"ph_value": 7.0})[0]
