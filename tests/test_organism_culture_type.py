"""Guard the organism_culture_type backfill and its recurrence (#142).

`organism_culture_type` is `recommended:`, so validate-strict never flags a record
that names target_organisms but leaves it unset. This backfilled the 40 such
records: 39 to `isolate` (specific strains named), and one syntrophic co-culture
left for a curator. These tests pin the inference and guard against a fresh import
reintroducing the gap.
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
def oct():
    return _load("curate_organism_culture_type")


def test_specific_strains_are_isolate(oct):
    doc = {"target_organisms": [{"preferred_term": "Escherichia coli", "strain": "K-12"}]}
    value, _ = oct.classify(doc)
    assert value == "isolate"


def test_multiple_named_strains_are_still_isolate(oct):
    """The enum is `Pure culture of one or more specific strains` — count is not
    the axis. Seven named gut strains is an isolate medium, not a community."""
    doc = {"target_organisms": [{"preferred_term": n} for n in
                                ["Bacteroides ureolyticus", "Prevotella bivia",
                                 "Fusobacterium nucleatum"]]}
    assert oct.classify(doc)[0] == "isolate"


@pytest.mark.parametrize("name", [
    "medium_for_co_culture_of_strain_jt",      # underscore — the #142 slip
    "medium for co-culture of strain jt",       # hyphen
    "medium for co culture of strain jt",       # space
    "cocultivation medium",                     # closed-up (cocultur)
])
def test_coculture_is_left_for_a_curator(oct, name):
    """A co-culture is a community case; the separator between `co` and `culture`
    must not decide whether it is caught (it did in #142). None of these may be
    auto-set to isolate."""
    doc = {"name": name, "target_organisms": [{"preferred_term": "Pelotomaculum sp."},
                                              {"preferred_term": "Methanospirillum hungatei"}]}
    value, reason = oct.classify(doc)
    assert value is None
    assert reason.startswith("community")


@pytest.mark.parametrize("signal", ["consortium", "microbial community",
                                     "activated sludge", "rumen fluid", "microbiome"])
def test_community_signals_are_left_for_a_curator(oct, signal):
    doc = {"name": f"{signal} medium", "target_organisms": [{"preferred_term": "mixed"}]}
    assert oct.classify(doc)[0] is None


def test_already_set_and_no_organisms_are_skipped(oct):
    assert oct.classify({"target_organisms": [{"preferred_term": "E. coli"}],
                         "organism_culture_type": "isolate"})[0] is None
    assert oct.classify({"name": "no organisms here"})[0] is None


def test_slot_is_placed_before_target_organisms(oct):
    doc = {"name": "x", "category": "bacterial",
           "target_organisms": [{"preferred_term": "E. coli"}],
           "ingredients": []}
    out = oct._set_before(doc, "organism_culture_type", "isolate", before="target_organisms")
    keys = list(out.keys())
    assert keys.index("organism_culture_type") == keys.index("target_organisms") - 1
    assert out["organism_culture_type"] == "isolate"
    # every original key survives, none duplicated
    assert set(keys) == set(doc) | {"organism_culture_type"}


def test_no_inferable_record_is_left_unset(oct, corpus):
    """Recurrence guard (#142): after the backfill, no record that names specific
    strains should still be missing organism_culture_type. A fresh import that
    reintroduces the shape fails here. Community-signal records are excluded — the
    script deliberately leaves those for a curator, so they are not in this set."""
    pending = oct.scan_parsed(corpus)
    assert pending == [], (
        "records name target_organisms (specific strains) but lack "
        f"organism_culture_type: {[str(p) for p, _d, _v in pending]}. "
        "Run `just curate-organism-culture-type --apply`.")
