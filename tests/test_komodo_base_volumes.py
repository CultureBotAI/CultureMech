"""Tests for scripts/fetch_komodo_base_volumes.py and its routing through the applier (#150).

The KOMODO path exists because `apply_cocktail_nesting.source_medium` refuses
`komodo.medium:` ids outright — KOMODO 294 stamps "DSMZ Medium: 294" on a record whose
DSMZ 294 is a different medium (#244). These tests pin the two things that make
resolving them safe anyway: the medium number must be derivable twice and agree, and
anything short of reading this record's own medium must stay a candidate.
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fetch_komodo_base_volumes import classify, komodo_key, resolve_base  # noqa: E402
from apply_cocktail_nesting import apply_plan, plan_record  # noqa: E402


KMAP = {"142": "142", "142_12346": "142", "87a": "87a", "294": "294", "69": "69"}


def _medium(name):
    return {"medium": {"name": name}}


def _doc(name, komodo=None):
    d = {"original_name": name, "name": name}
    if komodo:
        d["media_term"] = {"term": {"id": f"komodo.medium:{komodo}"}}
    return d


# --- resolving the medium number ------------------------------------------------

def test_bare_key_resolves_to_itself():
    assert resolve_base("142", KMAP) == ("142", "")


def test_variant_key_resolves_to_its_base():
    assert resolve_base("142_12346", KMAP) == ("142", "")


def test_disagreement_between_derivations_is_refused():
    """The #244 shape: a key whose export mapping is not its own leading number."""
    base, why = resolve_base("294", {"294": "1203"})
    assert base is None
    assert "refusing to choose" in why


def test_key_absent_from_the_export_is_refused():
    base, why = resolve_base("999", {})
    assert base is None and "absent" in why


def test_komodo_key_extraction():
    assert komodo_key(_doc("x", "298f")) == "298f"
    assert komodo_key({"media_term": {"term": {"id": "mediadive.medium:503"}}}) is None


# --- evidence classification ----------------------------------------------------

def test_bare_id_with_agreeing_name_is_assertable():
    basis, support, counter = classify(
        "1042", _doc("VULCANIBACILLUS MEDIUM"), _medium("VULCANIBACILLUS MEDIUM"), "1042")
    assert basis == "READ_FROM_THIS_MEDIUM"
    assert counter == ""


def test_bare_id_with_conflicting_name_stays_an_inference():
    """KOMODO 294 is PELOBACTER here and SYNTROPHUS upstream — the #244 collision."""
    basis, support, counter = classify(
        "294", _doc("PELOBACTER ACIDIGALLICI MEDIUM"), _medium("SYNTROPHUS HQGo1 MEDIUM"),
        "294")
    assert basis == "CROSS_MEDIUM_INFERENCE"
    assert "SYNTROPHUS" in counter and "PELOBACTER" in counter


def test_variant_records_are_never_assertable():
    """Its own recipe was never published; the volume comes from the base medium."""
    basis, _support, counter = classify(
        "142_12346", _doc("MEDIUM 142 MODIFIED FOR DSM 12346"),
        _medium("THIOMICROSPIRA PELOPHILA MEDIUM"), "142")
    assert basis == "CROSS_MEDIUM_INFERENCE"
    assert "142" in counter


def test_counterevidence_carries_the_observed_spread():
    """A reviewer should see that this stock varies 25x across media without digging."""
    _b, _s, counter = classify("294", _doc("A"), _medium("B"), "294")
    assert "0.2 ml" in counter and "5 ml" in counter


# --- routing into the record ----------------------------------------------------

STOCK = [{"compound": "FeCl2 x 4 H2O", "amount": 1.5, "unit": "g", "g_l": 1.5},
         {"compound": "ZnCl2", "amount": 0.07, "unit": "g", "g_l": 0.07}]


def _record():
    return {"ingredients": [
        {"preferred_term": "FeCl2 x 4 H2O", "concentration": {"value": "1.5", "unit": "G_PER_L"}},
        {"preferred_term": "ZnCl2", "concentration": {"value": "0.07", "unit": "G_PER_L"}},
    ]}


def _addition(basis):
    return {"solution_name": "Trace element solution SL-10", "addition_volume_ml": 1,
            "stock_prepared_in_ml": 1000, "stock_components": STOCK,
            "volume_basis": basis, "volume_support": "s", "volume_counterevidence": "c"}


def test_asserted_basis_writes_concentration():
    doc = _record()
    plan = plan_record(Path("x.yaml"), doc, [_addition("READ_FROM_THIS_MEDIUM")],
                       {"fecl2 x 4 h2o", "zncl2"}, False)
    apply_plan(doc, plan)
    sol = doc["solutions"][0]
    assert sol["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    assert "concentration_candidates" not in sol


def test_inferred_basis_writes_only_a_candidate():
    """The whole point of #255: nothing a tool concluded may look like a source's word."""
    doc = _record()
    plan = plan_record(Path("x.yaml"), doc, [_addition("CROSS_MEDIUM_INFERENCE")],
                       {"fecl2 x 4 h2o", "zncl2"}, False)
    apply_plan(doc, plan)
    sol = doc["solutions"][0]
    assert "concentration" not in sol
    cand = sol["concentration_candidates"][0]
    assert cand["basis"] == "CROSS_MEDIUM_INFERENCE"
    assert cand["counterevidence"] == "c" and cand["support"] == "s"


def test_split_rows_do_not_alias_their_source_ingredient():
    """A shallow copy shared nested dicts across two solutions, and yaml.dump emitted
    them as &id001/*id001 — two solutions aliasing one object."""
    doc = {"ingredients": [
        {"preferred_term": "Nicotinic acid", "term": {"id": "CHEBI:15940"},
         "concentration": {"value": "0.25", "unit": "G_PER_L"}},
    ]}
    additions = [
        {"solution_name": "Seven vitamins solution", "addition_volume_ml": 1,
         "stock_prepared_in_ml": 1000,
         "stock_components": [{"compound": "Nicotinic acid", "g_l": 0.2}]},
        {"solution_name": "Wolin's vitamin solution", "addition_volume_ml": 1,
         "stock_prepared_in_ml": 1000,
         "stock_components": [{"compound": "Nicotinic acid", "g_l": 0.05}]},
    ]
    plan = plan_record(Path("x.yaml"), doc, additions, {"nicotinic acid"}, True)
    assert plan is not None, "0.25 = 0.2 + 0.05 should decompose"
    apply_plan(doc, plan)
    terms = [c["term"] for s in doc["solutions"] for c in s["composition"] if "term" in c]
    assert len(terms) == 2
    assert terms[0] is not terms[1], "nested term dicts must not be shared between solutions"
