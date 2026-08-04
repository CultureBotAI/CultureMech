"""Tests for the missing-composition triage (#175).

The load-bearing tests here are the two NEGATIVE ones: that `solutions` counts as
a composition, and that a solution record naming a medium is not treated as
repairable from that medium. Both were mistakes made while building this — the
first inflated the count by 35, the second looked like a 214-record fix and would
have written a whole medium's recipe into each solution record.
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
def tmc():
    return _load("triage_missing_compositions")


def _rec(**kw):
    base = {"id": "CultureMech:1", "name": "x", "original_name": "X medium"}
    base.update(kw)
    return ("bacterial/x.yaml", base)


def test_a_record_with_nothing_is_reported(tmc):
    rows = tmc.triage_parsed([_rec(ingredients=[], solutions=[])], set())
    assert len(rows) == 1 and rows[0]["kind"] == "no ingredients and no solutions"


def test_solutions_count_as_a_composition(tmc):
    """#175 originally said 463; it is 428. A record whose composition lives in
    `solutions` is not empty — the same slot that made 15 of 17 findings in #181
    false positives."""
    rows = tmc.triage_parsed([_rec(
        ingredients=[], solutions=[{"preferred_term": "Trace element solution SL-10"}])], set())
    assert rows == [], "a record with solutions was reported as having no composition"


def test_a_placeholder_ingredient_is_reported(tmc):
    rows = tmc.triage_parsed([_rec(
        ingredients=[{"preferred_term": "See source for composition"}], solutions=[])], set())
    assert rows[0]["kind"] == "placeholder ingredient only"


def test_a_real_composition_is_not_reported(tmc):
    rows = tmc.triage_parsed([_rec(
        ingredients=[{"preferred_term": "Peptone"}, {"preferred_term": "NaCl"}])], set())
    assert rows == []


def test_solution_named_records_are_flagged_as_mis_typed(tmc):
    """183 of the 327 KOMODO empties are stock solutions imported as media. They
    are not media missing a recipe, and counting them as such overstates the
    data-quality problem."""
    rows = tmc.triage_parsed([_rec(
        original_name="Trace element solution (medium 929)", ingredients=[], solutions=[])], set())
    assert rows[0]["looks_like_a_solution"] == "yes"


def test_the_cited_medium_is_recorded_but_never_proposed_as_a_fix(tmc):
    """The trap. "Trace element solution (medium 1072)" is the solution defined
    INSIDE medium 1072, and dsmz_1072's composition is the whole medium — KH2PO4,
    NaCl, yeast extract, casamino acids — including a line reading "Trace element
    solution (see below) 2.0ml", which is the part actually wanted.

    The column records that a candidate exists. There must be no column, flag or
    field proposing it as the composition.
    """
    rows = tmc.triage_parsed([_rec(
        original_name="Trace element solution (medium 1072)",
        ingredients=[], solutions=[])], {"1072"})
    row = rows[0]
    assert row["name_cites_medium"] == "1072"
    assert row["cited_medium_in_local_dump"] == "yes"
    assert not any("propos" in k or "repair" in k or "suggest" in k for k in row), \
        "the report must not propose the cited medium as the composition"


def test_solution_records_themselves_are_skipped(tmc):
    rows = tmc.triage_parsed([("s.yaml", {
        "id": "CultureMech:9", "original_name": "Some stock",
        "term": {"id": "mediadive.solution:1"}, "ingredients": []})], set())
    assert rows == []


def test_corpus_baseline(tmc, corpus):
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    rows = tmc.triage_parsed([(str(p.relative_to(normalized)), d) for p, d in corpus])
    assert len(rows) <= 428, (
        f"{len(rows)} records lack a composition, above the documented baseline of "
        "428 — a new import dropped one, or the detector widened.")
