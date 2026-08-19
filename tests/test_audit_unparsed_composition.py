"""Tests for the unparsed-composition audit (#299, #273).

The detectors matter more than usual here because the audit is a ratchet: a
false positive raises the baseline and permanently weakens the gate, and a false
negative lets an importer reintroduce the defect. So each detector is tested on
the real shapes from the corpus, and the near-miss cases that must NOT trip it.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load():
    path = REPO_ROOT / "scripts" / "audit_unparsed_composition.py"
    spec = importlib.util.spec_from_file_location("audit_unparsed_composition", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["audit_unparsed_composition"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def aud():
    return _load()


def _findings(aud, doc):
    return {r["finding"] for r in aud.audit_record(doc, REPO_ROOT / "x.yaml")}


# --- NAME_IN_CONCENTRATION ------------------------------------------------


def test_name_landing_in_the_concentration_is_caught(aud):
    """The NBRC_1003 shape: the two fields were swapped on import."""
    doc = {"id": "CultureMech:007449", "ingredients": [
        {"preferred_term": "", "concentration": {"value": "MgSO4·7H2O",
                                                 "unit": "G_PER_L"}}]}
    assert _findings(aud, doc) == {"NAME_IN_CONCENTRATION"}


def test_an_empty_name_with_a_real_number_is_a_different_finding(aud):
    """Reported apart from the swap because the name is NOT recoverable here —
    there is nothing to restore it from."""
    doc = {"ingredients": [
        {"preferred_term": "", "concentration": {"value": "0.5", "unit": "G_PER_L"}}]}
    assert _findings(aud, doc) == {"EMPTY_INGREDIENT_NAME"}


@pytest.mark.parametrize("value", ["10", "0.5", "1.5-2.0", "<0.1", "~5", "variable", 10, 2.5])
def test_legitimate_concentration_values_are_not_names(aud, value):
    doc = {"ingredients": [
        {"preferred_term": "", "concentration": {"value": value, "unit": "G_PER_L"}}]}
    assert _findings(aud, doc) == {"EMPTY_INGREDIENT_NAME"}


@pytest.mark.parametrize("ingredient", [
    {"preferred_term": ""},                                  # no concentration block
    {"preferred_term": "", "concentration": {}},             # block, no value
    {"preferred_term": "", "concentration": {"value": None}},
    {"preferred_term": "", "concentration": {"value": ""}},
])
def test_a_missing_concentration_is_not_evidence_of_a_swap(aud, ingredient):
    """Absence must not be read as a name.

    These reported NAME_IN_CONCENTRATION, which points a curator at a field that
    does not exist. Nothing in the corpus is shaped this way today — which is
    precisely why it needs pinning rather than leaving to chance, since the
    counts would not have moved to reveal it.
    """
    assert _findings(aud, {"ingredients": [ingredient]}) == {"EMPTY_INGREDIENT_NAME"}


def test_a_named_ingredient_is_never_flagged_whatever_its_concentration(aud):
    doc = {"ingredients": [
        {"preferred_term": "Glucose", "concentration": {"value": "10", "unit": "G_PER_L"}}]}
    assert _findings(aud, doc) == set()


# --- coverage: reagents do not all live in `ingredients` ------------------


BAD_ROW = {"preferred_term": "",
           "concentration": {"value": "MgSO4·7H2O", "unit": "G_PER_L"}}


@pytest.mark.parametrize("doc,location", [
    ({"ingredients": [BAD_ROW]}, "ingredients"),
    ({"composition": [BAD_ROW]}, "composition"),
    ({"solutions": [{"preferred_term": "Trace elements",
                     "composition": [BAD_ROW]}]}, "solutions[].composition"),
])
def test_every_reagent_location_is_scanned(aud, doc, location):
    """An ingredients-only scan looks like full coverage and is not.

    The 4,784 standalone stock-solution records keep their reagents in a
    top-level `composition:`, not `ingredients:` — 35,009 rows. Skipping them
    would leave the gate porous exactly where a stock-solution import lands, and
    the miss would be invisible because the totals would not move.
    """
    findings = list(aud.audit_record(doc, REPO_ROOT / "x.yaml"))
    assert [f["finding"] for f in findings] == ["NAME_IN_CONCENTRATION"]
    assert findings[0]["location"] == location


def test_the_location_column_is_always_populated(aud):
    """A curator triaging the report needs to know which field to open."""
    doc = {
        "ingredients": [BAD_ROW],
        "composition": [BAD_ROW],
        "solutions": [{
            "preferred_term": "MgSO4·7H2O0.5g(NH4)2SO40.4gK2HPO40.2gKCl0.1g"
                              "Distilled water1L",
            "composition": []}],
    }
    findings = list(aud.audit_record(doc, REPO_ROOT / "x.yaml"))
    assert len(findings) == 3
    assert all(f.get("location") for f in findings)
    assert {f["location"] for f in findings} == {
        "ingredients", "composition", "solutions[].preferred_term"}


# --- UNPARSED_SOLUTION_TABLE ----------------------------------------------


def test_a_concatenated_composition_table_is_caught(aud):
    doc = {"solutions": [{
        "preferred_term": "MgSO4·7H2O0.5g(NH4)2SO40.4gK2HPO40.2gKCl0.1g"
                          "Distilled water1LAdjust pH to 2.0 with H2SO4.",
        "composition": []}]}
    assert _findings(aud, doc) == {"UNPARSED_SOLUTION_TABLE"}


def test_a_catalogue_cross_reference_is_not_a_corrupt_table(aud):
    """The false positive a letter-followed-by-digit test produces.

    These are legitimate solution entries that point at another record; `M803`
    trips the naive rule. 14 of them were flagged before the detector was
    narrowed to an amount+unit welded onto the next reagent name.
    """
    for name in (
        "MINERAL MEDIUM FOR HYDROGENOPHILUS ISLANDICUM (see Medium [M803])",
        "Yeast extract--malt extract agar (ISP--2) (see Medium [M35])",
        "Trace element solution (filter--sterilized) (see Medium [M773])",
    ):
        assert _findings(aud, {"solutions": [
            {"preferred_term": name, "composition": []}]}) == set(), name


def test_a_solution_that_parsed_correctly_is_not_flagged(aud):
    """A populated `composition` means the table was read, whatever the name."""
    doc = {"solutions": [{
        "preferred_term": "MgSO4·7H2O0.5g(NH4)2SO40.4gK2HPO40.2gKCl0.1gDistilled water1L",
        "composition": [{"preferred_term": "MgSO4·7H2O"}]}]}
    assert _findings(aud, doc) == set()


def test_a_short_solution_name_is_never_a_table(aud):
    assert _findings(aud, {"solutions": [
        {"preferred_term": "Trace Elements SL-10", "composition": []}]}) == set()


# --- PROSE_AS_INGREDIENT --------------------------------------------------


def test_a_preparation_instruction_parsed_as_an_ingredient_is_caught(aud):
    doc = {"ingredients": [{
        "preferred_term": "Make up to 1 litre with deionised water. For agar, add",
        "concentration": {"value": "15", "unit": "G_PER_L"}}]}
    assert _findings(aud, doc) == {"PROSE_AS_INGREDIENT"}


@pytest.mark.parametrize("name", [
    "Sodium acetate",           # contains no instruction verb
    "Yeast extract",
    "Bacto Tryptic Soy Broth w/o Dextrose (Difco)",
    "Adenine",                  # starts with the letters of "Add" but is not one
])
def test_real_reagent_names_do_not_trip_the_prose_detector(aud, name):
    doc = {"ingredients": [
        {"preferred_term": name, "concentration": {"value": "1", "unit": "G_PER_L"}}]}
    assert _findings(aud, doc) == set()


def test_an_instruction_verb_alone_is_not_enough(aud):
    """The conjunction is what keeps this usable: on the real corpus the loose
    filters flag 1,192 ingredient values and the conjunction flags 44."""
    doc = {"ingredients": [
        {"preferred_term": "Agar (if needed)", "concentration": {"value": "15"}}]}
    assert _findings(aud, doc) == set()


# --- the gate -------------------------------------------------------------


def test_the_audit_exits_non_zero_when_a_baseline_is_exceeded(aud, tmp_path):
    import yaml

    corpus = tmp_path / "bacterial"
    corpus.mkdir()
    (corpus / "bad.yaml").write_text(yaml.safe_dump({
        "id": "CultureMech:000001",
        "ingredients": [{"preferred_term": "",
                         "concentration": {"value": "NaCl", "unit": "G_PER_L"}}],
    }))
    out = tmp_path / "report.tsv"
    argv = ["--normalized-dir", str(tmp_path), "--out", str(out)]

    assert aud.main([*argv, "--max-allowed", "1"]) == 0
    assert aud.main([*argv, "--max-allowed", "0"]) == 1
    assert out.exists()


def test_the_export_gate_counts_only_findings_that_reach_the_graph(aud, tmp_path):
    """`--max-exported` is the sharper gate: ingredient findings are ungrounded
    and emit no KGX edge, so only unparsed solution tables can add garbage nodes."""
    import yaml

    corpus = tmp_path / "bacterial"
    corpus.mkdir()
    (corpus / "ing.yaml").write_text(yaml.safe_dump({
        "ingredients": [{"preferred_term": "",
                         "concentration": {"value": "NaCl", "unit": "G_PER_L"}}]}))
    argv = ["--normalized-dir", str(tmp_path), "--out", str(tmp_path / "r.tsv")]

    # One finding, but nothing exported -> the export gate stays quiet at 0.
    assert aud.main([*argv, "--max-exported", "0"]) == 0

    (corpus / "sol.yaml").write_text(yaml.safe_dump({"solutions": [{
        "preferred_term": "MgSO4·7H2O0.5g(NH4)2SO40.4gK2HPO40.2gKCl0.1gDistilled water1L",
        "composition": []}]}))
    assert aud.main([*argv, "--max-exported", "0"]) == 1
