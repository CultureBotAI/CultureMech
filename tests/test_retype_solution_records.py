"""Tests for the solution re-typing (#175).

The dangerous direction here is over-reach: re-typing a genuine medium removes it
from every media-level audit, silently. Most of these pin what must NOT be
re-typed.
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
def rt():
    return _load("retype_solution_records")


@pytest.fixture(scope="module")
def rk():
    return _load("record_kinds")


def _write(d: Path, name: str, doc: dict):
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(yaml.dump(doc, sort_keys=False))


def test_a_named_solution_with_no_composition_is_a_candidate(rt, tmp_path):
    _write(tmp_path / "bacterial", "a.yaml", {
        "id": "CultureMech:1", "name": "x",
        "original_name": "Trace element solution (medium 929)",
        "category": "bacterial", "ingredients": []})
    assert len(rt.candidates(tmp_path)) == 1


def test_a_named_solution_WITH_a_composition_is_left_alone(rt, tmp_path):
    """Ringer's and Hank's BSS are solutions by name but usable media by content.
    Re-typing them would drop them from audits that should still see them — so the
    name alone is never sufficient."""
    _write(tmp_path / "bacterial", "b.yaml", {
        "id": "CultureMech:2", "name": "y",
        "original_name": "Hank's balanced salt solution", "category": "bacterial",
        "ingredients": [{"preferred_term": "NaCl"}, {"preferred_term": "KCl"}]})
    assert rt.candidates(tmp_path) == []


def test_an_empty_record_that_is_NOT_named_like_a_solution_is_left_alone(rt, tmp_path):
    """The 126 genuinely-empty media. They are the real #175 gap and must stay
    visible in the triage report."""
    _write(tmp_path / "bacterial", "c.yaml", {
        "id": "CultureMech:3", "name": "z",
        "original_name": "DESULFOBACTERIUM ANILINI MEDIUM", "category": "bacterial",
        "ingredients": []})
    assert rt.candidates(tmp_path) == []


def test_an_already_typed_solution_is_not_reprocessed(rt, tmp_path):
    _write(tmp_path / "bacterial", "d.yaml", {
        "id": "CultureMech:4", "record_kind": "SOLUTION",
        "original_name": "Trace element solution (medium 929)",
        "category": "bacterial", "ingredients": []})
    assert rt.candidates(tmp_path) == []


def test_stamping_is_idempotent(rt, tmp_path):
    d = tmp_path / "bacterial"
    _write(d, "e.yaml", {"id": "CultureMech:5", "name": "e",
                         "original_name": "Vitamin solution (medium 951)",
                         "category": "bacterial", "ingredients": []})
    assert rt.main(["--normalized-dir", str(tmp_path), "--apply"]) == 0
    once = (d / "e.yaml").read_text()
    assert rt.main(["--normalized-dir", str(tmp_path), "--apply"]) == 0
    assert (d / "e.yaml").read_text() == once
    assert once.count("record_kind:") == 1


def test_report_only_by_default(rt, tmp_path):
    d = tmp_path / "bacterial"
    _write(d, "f.yaml", {"id": "CultureMech:6", "name": "f",
                         "original_name": "Trace element solution (medium 84)",
                         "category": "bacterial", "ingredients": []})
    before = (d / "f.yaml").read_text()
    assert rt.main(["--normalized-dir", str(tmp_path)]) == 0
    assert (d / "f.yaml").read_text() == before


def test_record_kind_makes_is_solution_record_true(rk):
    assert rk.is_solution_record({"record_kind": "SOLUTION"})
    assert not rk.is_solution_record({"record_kind": "MEDIUM"})
    assert not rk.is_solution_record({"name": "lb_broth"})


def test_the_term_id_rule_still_works(rk):
    """The curated assertion is additional, not a replacement — 4,784 records still
    rely on the upstream prefix."""
    assert rk.is_solution_record({"term": {"id": "mediadive.solution:4367"}})
    assert rk.is_solution_record({"term": {"id": "MediaIngredientMech:1"}})


def test_the_corpus_has_no_untyped_solution_stubs_left(rt):
    """If this fails, `just retype-solution-records --apply` was not run."""
    left = rt.candidates()
    assert not left, f"{len(left)} stubs still untyped, e.g. {[p.name for p,_ in left[:5]]}"
