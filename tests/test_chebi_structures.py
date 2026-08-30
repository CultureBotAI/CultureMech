"""The packaged ChEBI structure table, and how a page decides what to show.

The ingredient tables carried no chemical information: `chemical_formula` and
`molecular_weight` are on `IngredientDescriptor` but populated on 0 of 170,007
ingredients. 85% of those ingredients carry a ChEBI id, and those ids collapse
to 640 distinct terms — so the formula belongs to the term, once, not copied
into every record that cites it.
"""

from __future__ import annotations

import pytest

from culturemech.ingredients.chebi_structures import HEADER, Structure, load, structure_for


def test_the_table_is_packaged_and_populated():
    table = load()
    assert len(table) > 500, "the structure table looks truncated"
    assert all(key.startswith("CHEBI:") for key in table)


def test_the_header_is_the_contract():
    assert HEADER == ["chebi_id", "label", "formula", "molecular_weight", "charge"]


def test_a_known_term_carries_its_formula_and_mass():
    glucose = load()["CHEBI:17234"]
    assert glucose.label == "glucose"
    assert glucose.formula == "C6H12O6"
    assert glucose.molecular_weight == "180.156"


def test_a_term_chebi_gives_no_formula_is_recorded_as_empty_not_guessed():
    """Agar is a mixture; ChEBI asserts no formula. That is data, not a gap."""
    agar = load()["CHEBI:2509"]
    assert agar.label == "agar"
    assert agar.formula == ""
    assert not agar, "a row with nothing to show must be falsy"


def test_an_ingredient_with_a_chebi_id_resolves():
    structure = structure_for({"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"}})
    assert structure is not None
    assert structure.formula == "C6H12O6"


def test_an_ungrounded_ingredient_resolves_to_nothing():
    assert structure_for({"preferred_term": "Pea"}) is None
    assert structure_for({"preferred_term": "Pea", "term": {}}) is None


def test_a_non_chebi_grounding_resolves_to_nothing():
    """FOODON terms are real groundings but carry no formula here."""
    assert (
        structure_for({"preferred_term": "Yeast Extract", "term": {"id": "FOODON:03315426"}})
        is None
    )


def test_a_term_absent_from_the_table_does_not_raise():
    assert structure_for({"term": {"id": "CHEBI:99999999"}}) is None


def test_what_the_record_asserts_beats_the_shared_term():
    """A record may name a hydrate the generic ChEBI term does not distinguish."""
    structure = structure_for(
        {
            "preferred_term": "MgSO4•7H2O",
            "term": {"id": "CHEBI:17234"},
            "chemical_formula": "MgSO4.7H2O",
        }
    )
    assert structure.formula == "MgSO4.7H2O"
    # The mass it did not override still comes from the term.
    assert structure.molecular_weight == "180.156"


def test_a_record_asserting_only_a_weight_keeps_the_terms_formula():
    structure = structure_for({"term": {"id": "CHEBI:17234"}, "molecular_weight": 999.0})
    assert structure.molecular_weight == "999.0"
    assert structure.formula == "C6H12O6"


@pytest.mark.parametrize("bad", [None, "CHEBI:17234", 42, []])
def test_a_non_mapping_ingredient_does_not_raise(bad):
    assert structure_for(bad) is None


def test_a_structure_with_only_a_mass_is_still_worth_showing():
    assert Structure("CHEBI:1", "x", "", "12.0", "0")


def test_an_empty_structure_is_falsy():
    assert not Structure("CHEBI:1", "x", "", "", "0")


@pytest.mark.corpus
def test_the_packaged_table_passes_its_own_offline_check(corpus):
    """`just check-chebi-structure-index`, as a test.

    A stale or truncated table fails quietly — `structure_for` returns None for
    an unknown id, which is right at render time and wrong as the only line of
    defence. Verified non-vacuous by truncating the file to 299 rows, which
    reports both the row-count mismatch and 341 uncovered ids.

    Uses conftest's session-scoped `corpus` fixture rather than re-walking
    `data/normalized_yaml`: walking it here took 484s in CI and tripped the
    120s slow-test budget, for a parse the session had already done.
    """
    from fetch_chebi_properties import DEFAULT_OUT, check, cited_chebi_ids_from_records

    cited = cited_chebi_ids_from_records(record for _, record in corpus)
    assert cited, "the corpus cites no CHEBI ids; the fixture looks empty"
    assert check(None, DEFAULT_OUT, cited=cited) == 0
