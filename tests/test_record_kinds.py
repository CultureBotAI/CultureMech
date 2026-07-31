"""Tests for the shared medium-vs-stock-solution rule (#124).

`data/normalized_yaml/bacterial/` mixes ~9,500 organism media with ~4,782
MediaDive stock-solution records. `category` cannot tell them apart: `CategoryEnum`
has no `solutions` member, so a solution has no honest value to carry and is
stamped `bacterial` for the directory it lives in.

The prioritizer's documented "category == solutions" hard filter therefore never
fired, and 4,772 solutions (31% of the committed report) were ranked as candidate
media for deep research.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def rk():
    return _load("record_kinds")


# --- the rule itself ------------------------------------------------------


@pytest.mark.parametrize("tid", [
    "mediadive.solution:1000",
    "MediaIngredientMech:0001",
])
def test_solution_term_prefixes_are_detected(rk, tid):
    assert rk.is_solution_record({"term": {"id": tid}}) is True


@pytest.mark.parametrize("doc", [
    {"term": {"id": "mediadive.medium:123"}},
    {"term": {"id": "DSM:1"}},
    {"term": {}},
    {"term": None},
    {"term": "not-a-dict"},
    {},
    None,
    "garbage",
])
def test_non_solutions_are_not_detected(rk, doc):
    assert rk.is_solution_record(doc) is False


def test_category_bacterial_does_not_make_it_a_medium(rk):
    """The exact shape that defeated the old filter."""
    assert rk.is_solution_record(
        {"category": "bacterial", "term": {"id": "mediadive.solution:1000"}}
    ) is True


def test_schema_has_no_solutions_category(rk):
    """The premise of the bug: there is no legal `category: solutions` value.

    If someone adds one to CategoryEnum, the structural rule is still correct but
    this test should be revisited alongside a data migration.
    """
    schema = yaml.safe_load(
        (REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml").read_text()
    )
    values = set(schema["enums"]["CategoryEnum"]["permissible_values"])
    assert "solutions" not in values
    assert "bacterial" in values  # guards the fixture itself


# --- both consumers agree -------------------------------------------------


def test_validate_strict_routing_agrees_with_the_shared_rule(rk):
    """validate_strict and the prioritizer must not drift apart on this.

    Both now import `record_kinds.is_solution_record`; this asserts they agree
    across the same inputs, so a future local re-implementation in either place
    fails here.
    """
    vs = _load("validate_strict")
    cases = [
        {"term": {"id": "mediadive.solution:1000"}},
        {"term": {"id": "MediaIngredientMech:0001"}},
        {"term": {"id": "mediadive.medium:1000"}},
        {"term": {"id": "DSM:1"}},
        {"category": "bacterial", "term": {"id": "mediadive.solution:9"}},
        {"term": {}},
        {},
    ]
    for doc in cases:
        expected = "SolutionRecipe" if rk.is_solution_record(doc) else "MediaRecipe"
        assert vs.infer_target_class(doc) == expected, doc


# --- the corpus-level property --------------------------------------------


def test_prioritizer_ranks_no_solution_records():
    """End-to-end: the ranking must contain zero stock solutions.

    Before the fix this was 4,772 of 15,496 entries.
    """
    rk_mod = _load("record_kinds")
    pdrc = _load("prioritize_deep_research_candidates")

    entries = pdrc.collect_records(set())
    assert entries, "expected a non-empty ranking"

    normalized = REPO_ROOT / "data" / "normalized_yaml"
    offenders = []
    for entry in entries:
        path = normalized / entry["file_path"]
        doc = pdrc.load_yaml(path)
        if rk_mod.is_solution_record(doc):
            offenders.append(entry["file_path"])
            if len(offenders) >= 5:
                break
    assert not offenders, f"stock solutions leaked into the ranking: {offenders}"


def test_corpus_still_contains_the_solutions_this_filters():
    """Guard against the test above passing because the corpus changed shape."""
    rk_mod = _load("record_kinds")
    bacterial = REPO_ROOT / "data" / "normalized_yaml" / "bacterial"
    found = 0
    for path in bacterial.glob("*.yaml"):
        try:
            doc = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if rk_mod.is_solution_record(doc):
            found += 1
            if found >= 100:
                break
    assert found >= 100, f"expected thousands of solution records in bacterial/, found {found}"
