"""Tests for the MIM SSSOM divergence audit (#256).

The join is the whole risk here. Matching CultureMech ingredients to MIM subjects
by name is easy to get subtly wrong in a way that manufactures disagreements —
and because this is a ratchet, a manufactured disagreement gets baked into the
baseline. So the tests concentrate on the two places the join can lie: which slot
holds our CHEBI, and which SSSOM predicates count as a grounding verdict.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load():
    path = REPO_ROOT / "scripts" / "audit_mim_sssom_divergence.py"
    spec = importlib.util.spec_from_file_location("audit_mim_sssom_divergence", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["audit_mim_sssom_divergence"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def aud():
    return _load()


SSSOM_HEADER = """\
# curie_map:
#   CHEBI: "http://purl.obolibrary.org/obo/CHEBI_"
# mapping_set_version: "2026-08-18"
"""
COLUMNS = "subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\n"


def _sssom(tmp_path: Path, rows: list[tuple[str, str, str, str]]) -> Path:
    path = tmp_path / "ingredient_mappings.sssom.tsv"
    body = "".join(
        f"MIM:{label.replace(' ', '_')}\t{label}\t{pred}\t{obj}\t{obj_label}\n"
        for label, pred, obj, obj_label in rows
    )
    path.write_text(SSSOM_HEADER + COLUMNS + body)
    return path


def _corpus(tmp_path: Path, docs: list[dict]) -> Path:
    root = tmp_path / "corpus"
    (root / "bacterial").mkdir(parents=True)
    for i, doc in enumerate(docs):
        (root / "bacterial" / f"r{i}.yaml").write_text(yaml.safe_dump(doc))
    return root


def _by_finding(rows):
    return {r["finding"]: r for r in rows}


# --- which slot holds our CHEBI -------------------------------------------


def test_a_mediadive_term_id_does_not_hide_the_chebi_grounding(aud, tmp_path):
    """The bug that made 24,400 rows look divergent when they are not.

    MediaDive-derived records keep the source's own id in `term.id` and the
    ontology grounding in `chebi_term.id`. Reading only `term.id` compares
    `mediadive.compound:5` against MIM's CHEBI and reports a disagreement that
    does not exist.
    """
    sssom = _sssom(tmp_path, [("Glucose", "skos:exactMatch", "CHEBI:17234", "glucose")])
    corpus = _corpus(tmp_path, [{"ingredients": [{
        "preferred_term": "Glucose",
        "term": {"id": "mediadive.compound:5", "label": "Glucose"},
        "chebi_term": {"id": "CHEBI:17234", "label": "glucose"},
    }]}])

    rows, version = aud.audit(corpus, sssom)
    assert rows == []
    assert version == "2026-08-18"


def test_a_chebi_in_the_term_slot_is_still_found(aud, tmp_path):
    """Records without a MediaDive lineage put CHEBI directly in `term`."""
    sssom = _sssom(tmp_path, [("Glucose", "skos:exactMatch", "CHEBI:17234", "glucose")])
    corpus = _corpus(tmp_path, [{"ingredients": [
        {"preferred_term": "Glucose", "term": {"id": "CHEBI:17234", "label": "glucose"}}]}])
    rows, _ = aud.audit(corpus, sssom)
    assert rows == []


def test_a_real_divergence_is_reported(aud, tmp_path):
    sssom = _sssom(tmp_path, [("EDTA", "skos:exactMatch", "CHEBI:4735",
                               "ethylenediaminetetraacetic acid")])
    corpus = _corpus(tmp_path, [{"ingredients": [
        {"preferred_term": "EDTA", "chebi_term": {"id": "CHEBI:64755", "label": "EDTA(2-)"}}]}])
    rows, _ = aud.audit(corpus, sssom)
    finding = _by_finding(rows)["DIVERGENT"]
    assert finding["mim_id"] == "CHEBI:4735"
    assert "CHEBI:64755" in finding["our_ids"]
    assert finding["our_label_asserted"] == "CHEBI:64755=EDTA(2-)"


# --- which SSSOM predicates count -----------------------------------------


@pytest.mark.parametrize("predicate",
                         ["skos:narrowMatch", "skos:broadMatch", "skos:closeMatch"])
def test_only_exact_matches_are_treated_as_a_grounding_verdict(aud, tmp_path, predicate):
    """A narrowMatch asserts a relationship, not an identity.

    MIM maps `Dry cow-manure` narrowMatch to `ENVO:00003031 animal manure`.
    Treating that as a grounding would manufacture a disagreement with any
    sensible CHEBI we hold.
    """
    sssom = _sssom(tmp_path, [("EDTA", predicate, "CHEBI:4735", "EDTA acid")])
    corpus = _corpus(tmp_path, [{"ingredients": [
        {"preferred_term": "EDTA", "chebi_term": {"id": "CHEBI:64755", "label": "EDTA(2-)"}}]}])
    assert aud.audit(corpus, sssom)[0] == []


def test_a_name_mim_maps_two_ways_is_skipped_not_guessed(aud, tmp_path):
    """MIM has not settled it, so there is no verdict to compare against."""
    sssom = _sssom(tmp_path, [
        ("Citrate", "skos:exactMatch", "CHEBI:16947", "citrate(3-)"),
        ("Citrate", "skos:exactMatch", "CHEBI:30769", "citric acid"),
    ])
    corpus = _corpus(tmp_path, [{"ingredients": [
        {"preferred_term": "Citrate", "chebi_term": {"id": "CHEBI:99999", "label": "x"}}]}])
    assert aud.audit(corpus, sssom)[0] == []


def test_a_non_chebi_object_is_not_a_chebi_verdict(aud, tmp_path):
    sssom = _sssom(tmp_path, [("Dry cow-manure", "skos:exactMatch",
                               "kgmicrobe.ingredient:dry_cow-manure", "Dry cow-manure")])
    corpus = _corpus(tmp_path, [{"ingredients": [
        {"preferred_term": "Dry cow-manure",
         "chebi_term": {"id": "CHEBI:12345", "label": "x"}}]}])
    assert aud.audit(corpus, sssom)[0] == []


# --- the other two findings -----------------------------------------------


def test_one_name_grounded_two_ways_is_an_internal_split(aud, tmp_path):
    """Independent of MIM, and the class most often a plain mistake:
    `dipotassium phosphate` is CHEBI:131527 on 475 rows and CHEBI:63036 on 1."""
    sssom = _sssom(tmp_path, [])
    corpus = _corpus(tmp_path, [
        {"ingredients": [{"preferred_term": "Vitamin B12",
                          "chebi_term": {"id": "CHEBI:17439", "label": "a"}}]},
        {"ingredients": [{"preferred_term": "vitamin b12",
                          "chebi_term": {"id": "CHEBI:176843", "label": "b"}}]},
    ])
    finding = _by_finding(aud.audit(corpus, sssom)[0])["INTERNAL_SPLIT"]
    assert finding["rows"] == "2"
    assert "CHEBI:17439" in finding["our_ids"] and "CHEBI:176843" in finding["our_ids"]
    assert "MIM has no opinion" in finding["detail"]


def test_a_split_says_whether_mim_adjudicates_it(aud, tmp_path):
    sssom = _sssom(tmp_path, [("Citric Acid", "skos:exactMatch", "CHEBI:30769",
                               "citric acid")])
    corpus = _corpus(tmp_path, [
        {"ingredients": [{"preferred_term": "Citric Acid",
                          "chebi_term": {"id": "CHEBI:30769", "label": "citric acid"}}]},
        {"ingredients": [{"preferred_term": "Citric acid",
                          "chebi_term": {"id": "CHEBI:53258", "label": "other"}}]},
    ])
    finding = _by_finding(aud.audit(corpus, sssom)[0])["INTERNAL_SPLIT"]
    assert "MIM matches one of them" in finding["detail"]


def test_a_name_mim_grounds_and_we_do_not_is_reported(aud, tmp_path):
    sssom = _sssom(tmp_path, [("Biotin", "skos:exactMatch", "CHEBI:15956", "biotin")])
    corpus = _corpus(tmp_path, [{"ingredients": [{"preferred_term": "Biotin"}]}])
    finding = _by_finding(aud.audit(corpus, sssom)[0])["MISSING_GROUNDING"]
    assert finding["mim_id"] == "CHEBI:15956"
    assert finding["our_ids"] == ""


def test_hydrates_are_not_folded_into_their_anhydrous_form(aud, tmp_path):
    """Normalization folds whitespace and hyphens only.

    `CaCl2 x 2 H2O` and `CaCl2` are different substances, and #256 records that
    the hydrate is sometimes the term we model better than MIM. Folding digits or
    punctuation would hide exactly that.
    """
    assert aud.normalize_name("CaCl2 x 2 H2O") != aud.normalize_name("CaCl2")
    assert aud.normalize_name("Sodium-acetate") == aud.normalize_name("sodium acetate")
    assert aud.normalize_name("  Yeast   extract ") == aud.normalize_name("yeast_extract")


# --- reagents live in three places ----------------------------------------


@pytest.mark.parametrize("doc", [
    {"ingredients": [{"preferred_term": "EDTA",
                      "chebi_term": {"id": "CHEBI:64755", "label": "EDTA(2-)"}}]},
    {"composition": [{"preferred_term": "EDTA",
                      "chebi_term": {"id": "CHEBI:64755", "label": "EDTA(2-)"}}]},
    {"solutions": [{"preferred_term": "S", "composition": [
        {"preferred_term": "EDTA",
         "chebi_term": {"id": "CHEBI:64755", "label": "EDTA(2-)"}}]}]},
])
def test_every_reagent_location_is_compared(aud, tmp_path, doc):
    """Stock-solution records keep reagents in a top-level `composition:`, so an
    ingredients-only comparison would silently exempt them from the gate."""
    sssom = _sssom(tmp_path, [("EDTA", "skos:exactMatch", "CHEBI:4735", "EDTA acid")])
    rows, _ = aud.audit(_corpus(tmp_path, [doc]), sssom)
    assert _by_finding(rows)["DIVERGENT"]["mim_id"] == "CHEBI:4735"


# --- the gate -------------------------------------------------------------


def test_the_gate_fails_when_a_baseline_is_exceeded(aud, tmp_path):
    sssom = _sssom(tmp_path, [("EDTA", "skos:exactMatch", "CHEBI:4735", "EDTA acid")])
    corpus = _corpus(tmp_path, [{"ingredients": [
        {"preferred_term": "EDTA", "chebi_term": {"id": "CHEBI:64755", "label": "x"}}]}])
    argv = ["--normalized-dir", str(corpus), "--sssom", str(sssom),
            "--out", str(tmp_path / "r.tsv")]
    assert aud.main([*argv, "--max-divergent", "1"]) == 0
    assert aud.main([*argv, "--max-divergent", "0"]) == 1


def test_a_missing_sssom_fails_with_a_usable_message(aud, tmp_path):
    with pytest.raises(SystemExit, match="MIM SSSOM not found"):
        aud.audit(tmp_path, tmp_path / "absent.tsv")
