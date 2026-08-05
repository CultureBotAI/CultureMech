"""Tests for the medium_type curator (#165).

`medium_type` is a maintained axis: kgx_export emits one edge per record from it,
so a missing or wrong value is invisible in every artifact until someone counts
edges. These pin the derivation, and — more carefully — pin what the curator must
NOT touch.
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
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def cmt():
    return _load("curate_medium_type")


@pytest.fixture(scope="module")
def maps(cmt):
    m = cmt.schema_mapping()
    return m, cmt.inverse_mapping(m)


def test_the_derivation_comes_from_the_schema(maps):
    """Hardcoding a second copy of the mapping is how the slots disagreed in #164."""
    mapping, inv = maps
    assert mapping["DEFINED"] == "DEFINED" and mapping["COMPLEX"] == "UNDEFINED"
    assert inv["DEFINED"] == "DEFINED"
    assert inv["UNDEFINED"] == "COMPLEX"


def test_semi_defined_collapses_to_complex(maps):
    """#171's refinement has no single-valued equivalent. Recording the collapse is
    the point: it is why composition_type, not this slot, is the primary axis."""
    _, inv = maps
    assert inv["SEMI_DEFINED"] == "COMPLEX"


def test_a_missing_value_is_reported(cmt, maps):
    mapping, inv = maps
    assert cmt.assess({"composition_type": "UNDEFINED"}, mapping, inv)


def test_a_contradiction_is_reported(cmt, maps):
    mapping, inv = maps
    r = cmt.assess({"composition_type": "DEFINED", "medium_type": "COMPLEX"}, mapping, inv)
    assert r and "contradicts" in r


@pytest.mark.parametrize("ct,mt", [("DEFINED", "DEFINED"), ("UNDEFINED", "COMPLEX"),
                                   ("SEMI_DEFINED", "COMPLEX")])
def test_a_correct_record_is_left_alone(cmt, maps, ct, mt):
    mapping, inv = maps
    assert cmt.assess({"composition_type": ct, "medium_type": mt}, mapping, inv) is None


@pytest.mark.parametrize("value", ["BUFFER", "NEGATIVE_CONTROL"])
def test_directly_curated_values_are_never_derived_over(cmt, maps, value):
    """pbs.yaml and water.yaml have NO composition_type, so a deriver that ignored
    this would overwrite the only classification they carry — losing information
    while appearing to tidy up."""
    mapping, inv = maps
    assert cmt.assess({"medium_type": value}, mapping, inv) is None
    assert cmt.assess({"medium_type": value, "composition_type": None}, mapping, inv) is None


def test_a_record_with_neither_axis_is_reported_not_guessed(cmt, maps):
    mapping, inv = maps
    r = cmt.assess({"name": "x"}, mapping, inv)
    assert r and "no composition_type" in r


def test_apply_stamps_missing_and_fixes_contradictions(cmt, tmp_path):
    d = tmp_path / "bacterial"
    d.mkdir(parents=True)
    (d / "a.yaml").write_text("id: CultureMech:1\nname: a\ncomposition_type: UNDEFINED\n")
    (d / "b.yaml").write_text(
        "id: CultureMech:2\nname: b\ncomposition_type: DEFINED\nmedium_type: COMPLEX\n")
    assert cmt.main(["--normalized-dir", str(d.parent), "--apply"]) == 0
    assert yaml.safe_load((d / "a.yaml").read_text())["medium_type"] == "COMPLEX"
    assert yaml.safe_load((d / "b.yaml").read_text())["medium_type"] == "DEFINED"


def test_report_only_by_default(cmt, tmp_path):
    """The default must not write. A curator that edits on a bare invocation is how
    20 records got false chemistry in #166."""
    d = tmp_path / "bacterial"
    d.mkdir(parents=True)
    before = "id: CultureMech:1\nname: a\ncomposition_type: UNDEFINED\n"
    (d / "a.yaml").write_text(before)
    assert cmt.main(["--normalized-dir", str(d.parent)]) == 0
    assert (d / "a.yaml").read_text() == before


def test_the_corpus_needs_no_stamping(cmt, maps):
    """If this fails, `just curate-medium-type --apply` was not run before commit."""
    mapping, inv = maps
    drift = cmt.scan(REPO_ROOT / "data" / "normalized_yaml", mapping, inv)
    assert not drift, f"{len(drift)} records drifted, e.g. {[str(p) for p,_,_,_ in drift[:5]]}"
