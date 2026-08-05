"""Tests for the missing-composition triage (#175).

The load-bearing tests here are the two NEGATIVE ones: that `solutions` counts as
a composition, and that a solution record naming a medium is not treated as
repairable from that medium. Both were mistakes made while building this — the
first inflated the count by 35, the second looked like a 217-record fix and would
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
    """#175 originally said 463; it was 428, and is 226 once the mis-typed stock
    solutions are excluded. A record whose composition lives in
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
    """202 were stock solutions imported as media, now carrying
    `record_kind: SOLUTION` so `is_solution_record()` excludes them. They
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
    assert len(rows) <= 226, (
        f"{len(rows)} records lack a composition, above the documented baseline of "
        "226 — a new import dropped one, or the detector widened. The figure was "
        "428 before #175 re-typed 202 mis-imported stock solutions.")


def test_the_solution_classifier_does_not_enumerate_reagents(tmc):
    """#194: requiring a known word before "solution" missed 34 records —
    "Amino acid solution", "Haemin solution", "Na-sesquicarbonate solution". The
    reagent list was never completable; the word "solution" is the signal."""
    for name in ("Amino acid solution (medium 78)", "Haemin solution (medium 104)",
                 "Chelated iron solution (medium 737)", "LIP-solution (medium 391)",
                 "Na-sesquicarbonate solution (medium 31)",
                 "Phosphate buffer (10x) (medium 1341)",
                 "Vitamin mixture (medium 1001)", "Trace elements SL-12"):
        rows = tmc.triage_parsed([_rec(original_name=name, ingredients=[], solutions=[])], set())
        assert rows and rows[0]["looks_like_a_solution"] == "yes", name


def test_a_real_medium_name_is_not_called_a_solution(tmc):
    for name in ("DESULFOBACTERIUM ANILINI MEDIUM", "Fastidious Anaerobe Agar",
                 "NEOMYCIN AGAR", "Nutrient broth"):
        rows = tmc.triage_parsed([_rec(original_name=name, ingredients=[], solutions=[])], set())
        assert rows and not rows[0]["looks_like_a_solution"], name


# --- #196: the report must not depend on untracked local state --------------


def test_the_report_does_not_read_the_gitignored_dump(tmc):
    """`data/raw/**/*.json` is gitignored, so a report that lists that directory is
    a function of whoever last ran it: this column gave 217 hits on one machine and
    0 in a fresh worktree of the same commit.

    That is #121's defect — a tracked report scanning an untracked tree, producing
    diffs indistinguishable from real change. Review missed it because the baseline
    test asserts the row COUNT, which is identical either way; the machine
    dependence lived entirely in a column no test read.
    """
    import inspect
    src = inspect.getsource(tmc._mediadive_ids)
    assert "MEDIADIVE_INDEX" in src, "_mediadive_ids must read the TRACKED index"
    assert "listdir" not in src and "glob" not in src, (
        "_mediadive_ids scans a directory again; it must read the tracked index")


def test_the_tracked_index_exists_and_is_populated(tmc):
    ids = tmc._mediadive_ids()
    assert len(ids) > 1000, f"tracked mediadive index looks empty: {len(ids)} ids"
    assert all(i.isdigit() for i in ids)


def test_refreshing_the_index_is_the_only_step_that_reads_untracked_state(tmc):
    """The one crossing from untracked to tracked, matching the #121 pattern:
    an explicit refresh producing a reviewable diff."""
    import inspect
    assert "listdir" in inspect.getsource(tmc._scan_untracked_dump)
    assert "--refresh-mediadive-index" in inspect.getsource(tmc.main)
