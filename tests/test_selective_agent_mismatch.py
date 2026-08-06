"""Tests for the selective-agent name/composition mismatch audit (#181).

Most of these pin FALSE POSITIVES rather than detections. That is deliberate: the
first version of this check reported 28 records and more than half were artifacts
of substring matching. A checker that cries wolf on the genus *Streptomyces* gets
switched off, and then the 17 real defects go unnoticed too.
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
def aud():
    return _load("audit_selective_agent_mismatch")


def _rec(name, ingredients):
    return ("bacterial/x.yaml", {
        "id": "CultureMech:1", "name": "x", "original_name": name,
        "ingredients": [{"preferred_term": i} for i in ingredients]})


# --- detection --------------------------------------------------------------


def test_agent_in_name_but_not_in_ingredients_is_reported(aud):
    rows = aud.audit_parsed([_rec("LB + Rifampicin medium",
                                  ["Distilled water", "Yeast extract", "NaCl"])])
    assert len(rows) == 1 and "rifampicin" in rows[0]["missing_agents"]


def test_agent_present_in_ingredients_is_not_reported(aud):
    rows = aud.audit_parsed([_rec("LB + Rifampicin medium",
                                  ["Yeast extract", "Rifampicin"])])
    assert rows == []


def test_a_partial_match_reports_only_the_missing_agent(aud):
    rows = aud.audit_parsed([_rec("LB + Ampicillin, Kanamycin medium",
                                  ["Yeast extract", "Ampicillin"])])
    assert rows[0]["missing_agents"] == "kanamycin"


# --- the false positives that made the first version useless ----------------


def test_the_genus_streptomyces_is_not_the_drug_streptomycin(aud):
    """`streptomyc` as a substring matched 8 GYM Streptomyces media."""
    rows = aud.audit_parsed([_rec("GYM Streptomyces Medium",
                                  ["Glucose", "Yeast extract", "Malt extract"])])
    assert rows == [], f"flagged the genus as an antibiotic: {rows}"


def test_mobile_does_not_contain_bile(aud):
    """`bile` as a substring matched `alkalispirillum_mobile_medium`, 8 times over."""
    rows = aud.audit_parsed([_rec("Alkalispirillum mobile medium", ["NaCl", "Yeast extract"])])
    assert rows == [], f"matched 'bile' inside 'mobile': {rows}"


def test_either_or_formulations_are_not_defects(aud):
    """"tetracycline (10 ug/ml) OR rifampin (100 ug/ml)" names two alternatives.
    The record holds one of them and is complete."""
    rows = aud.audit_parsed([_rec(
        "M2SGC broth containing tetracycline (10 ug/ml) or rifampin (100 ug/ml)",
        ["Tetracycline", "Glucose"])])
    assert rows == []


def test_either_or_with_neither_agent_present_is_still_a_defect(aud):
    """The suppression must not become a blanket excuse for any name with 'or'."""
    rows = aud.audit_parsed([_rec(
        "M2SGC broth containing tetracycline or rifampin", ["Glucose", "Yeast extract"])])
    assert len(rows) == 1


# --- spelling variants ------------------------------------------------------


def test_ampicilin_one_l_is_matched(aud):
    """The source spells it "Ampicilin" in two records; the name is the evidence,
    so the matcher accommodates the misspelling rather than losing the record."""
    rows = aud.audit_parsed([_rec("LB + Ampicilin, Hygromycin medium", ["Yeast extract"])])
    assert "ampicillin" in rows[0]["missing_agents"]


def test_rifampin_is_the_us_name_for_rifampicin_not_a_typo(aud):
    rows = aud.audit_parsed([_rec("LB + rifampin medium", ["Yeast extract"])])
    assert "rifampicin" in rows[0]["missing_agents"]


# --- recoverable concentrations --------------------------------------------


def test_a_concentration_kept_in_the_name_is_surfaced(aud):
    """"LB + 50 ug/ml Kanamycin medium" — the value survived upstream and was lost
    in transform, so it is recoverable from tracked data rather than invented."""
    rows = aud.audit_parsed([_rec("LB + 50 ug/ml Kanamycin medium", ["Yeast extract"])])
    assert rows[0]["named_conc"] == "kanamycin=50 ug/ml"


def test_no_concentration_in_the_name_means_no_claim(aud):
    """Absence must stay empty. A guessed concentration is the #166 failure."""
    rows = aud.audit_parsed([_rec("LB + Kanamycin medium", ["Yeast extract"])])
    assert rows[0]["named_conc"] == ""


# --- corpus -----------------------------------------------------------------


def test_solution_records_are_skipped(aud):
    """A stock solution named for the agent it IS must not be reported as a medium
    missing that agent. Keyed on `term.id`, matching `record_kinds` — the shared
    rule both this audit and validate_strict import, so they cannot drift."""
    rows = aud.audit_parsed([("bacterial/s.yaml", {
        "id": "CultureMech:9", "original_name": "Kanamycin stock solution",
        "term": {"id": "mediadive.solution:1"},
        "ingredients": [{"preferred_term": "Water"}]})])
    assert rows == []


def test_corpus_count_matches_the_documented_baseline(aud, corpus):
    """The gate's --max-allowed is set from this number; if it drifts, one of them
    is wrong.

    Uses the session-scoped `corpus` fixture rather than `aud.collect()`. Calling
    collect() re-parsed all ~15,900 records for this one test, costing 118s and
    making it the fifth full-corpus scan in the suite — enough to push the pytest
    job past the 40-minute CI ceiling (#189).
    """
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    rows = aud.audit_parsed([(str(p.relative_to(normalized)), d) for p, d in corpus])
    assert len(rows) == 0, (
        f"{len(rows)} records name a listed selective agent absent from their "
        "composition, above the baseline of 0 (the DSMZ 309 pair was repaired in "
        "#181). A new import reintroduced the defect, or the agent list grew; add "
        "the agent from the record's own name/preparation_steps, or file it.")


# --- #188: the concentration must belong to ITS agent ----------------------


def test_a_second_agents_concentration_is_not_stolen(aud):
    """A +/-40 character window reached back across the comma and reported
    `ampicillin=50 ug/ml` for a name that plainly says 100 — the #166 failure
    inside the tool written to prevent it."""
    rows = aud.audit_parsed([_rec("LB + 50 ug/ml Kanamycin, 100 ug/ml Ampicillin medium", [])])
    assert rows[0]["named_conc"] == "ampicillin=100 ug/ml; kanamycin=50 ug/ml"


def test_only_the_agent_that_has_a_concentration_gets_one(aud):
    rows = aud.audit_parsed([_rec("LB + Ampicillin, 100 ug/ml Kanamycin medium", [])])
    assert rows[0]["named_conc"] == "kanamycin=100 ug/ml"


def test_the_unit_slash_does_not_split_a_segment(aud):
    """Units are written "ug/ml". An early fix treated "/" as a segment separator,
    which turned every concentration into "50 ug" + "ml" and silently emptied the
    column — a regression that looked exactly like "no data available"."""
    rows = aud.audit_parsed([_rec("LB + 50 ug/ml Kanamycin medium", [])])
    assert rows[0]["named_conc"] == "kanamycin=50 ug/ml"


# --- the slot that made 15 of 17 findings false ----------------------------


def test_an_agent_supplied_as_a_solution_is_not_missing(aud):
    """The correction that shrank this audit from 17 records to 2.

    A stock-supplied antibiotic is a SOLUTION, not an ingredient.
    `lb_rifampicin_medium`'s `ingredients` really are plain LB — the rifampicin
    sits in `solutions`. Checking only `ingredients` called 15 complete records
    defective.
    """
    rows = aud.audit_parsed([("x.yaml", {
        "id": "CultureMech:1", "original_name": "LB + Rifampicin medium",
        "ingredients": [{"preferred_term": "Yeast extract"},
                        {"preferred_term": "NaCl"}],
        "solutions": [{"preferred_term": "Rifampicin solution (50 mg/ml)*"}]})])
    assert rows == [], f"agent present in `solutions` reported as missing: {rows}"


def test_an_agent_nested_in_a_solution_composition_is_not_missing(aud):
    rows = aud.audit_parsed([("x.yaml", {
        "id": "CultureMech:1", "original_name": "LB + Kanamycin medium",
        "ingredients": [{"preferred_term": "Yeast extract"}],
        "solutions": [{"preferred_term": "Antibiotic stock",
                       "composition": [{"preferred_term": "Kanamycin sulfate"}]}]})])
    assert rows == []


def test_an_agent_in_neither_slot_is_still_reported(aud):
    """The suppression must not swallow the genuine case — DSMZ 309 has no
    `solutions` entry and no neomycin anywhere."""
    rows = aud.audit_parsed([("x.yaml", {
        "id": "CultureMech:1", "original_name": "NEOMYCIN AGAR",
        "ingredients": [{"preferred_term": "Beef extract"},
                        {"preferred_term": "Peptone"}],
        "solutions": []})])
    assert len(rows) == 1 and "neomycin" in rows[0]["missing_agents"]
