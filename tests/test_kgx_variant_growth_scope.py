"""Variant evidence must never become a parent-medium growth assertion."""

import pytest

from culturemech.export.kgx_export import GROWS_IN_MEDIUM, organism_grows_in_medium_edge, transform


def organism(**extra):
    return {
        "preferred_term": "Test organism",
        "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
        "evidence": [
            {"reference": "doi:10.1234/example", "supports": "SUPPORT", "snippet": "Test evidence"}
        ],
        **extra,
    }


@pytest.mark.parametrize("scope", ["Study variant", "Missing variant", " "])
def test_variant_scope_cannot_be_exported_as_parent_growth(scope):
    with pytest.warns(RuntimeWarning, match="variant-scoped growth"):
        assert (
            organism_grows_in_medium_edge(organism(scoped_to_variant=scope), "CultureMech:900001")
            is None
        )


def test_transform_omits_scoped_growth_but_keeps_unscoped_growth():
    record = {
        "id": "CultureMech:900001",
        "name": "Test medium",
        "variants": [{"name": "Study variant"}],
        "target_organisms": [
            organism(scoped_to_variant="Study variant"),
            organism(strain="parent-supported"),
        ],
    }
    with pytest.warns(RuntimeWarning, match="variant-scoped growth"):
        edges = list(transform(record))
    growth = [edge for edge in edges if edge["predicate"] == GROWS_IN_MEDIUM]
    assert len(growth) == 1
    assert growth[0]["object"] == record["id"]
    assert growth[0]["publications"] == ["doi:10.1234/example"]
    assert growth[0]["qualifiers"][0]["qualifier_value"] == "parent-supported"


def test_linked_child_can_retain_its_own_unscoped_growth():
    edge = organism_grows_in_medium_edge(organism(), "CultureMech:900002")
    assert edge["object"] == "CultureMech:900002"


def test_parent_rank_only_mapping_does_not_invent_taxon_edge():
    assert (
        organism_grows_in_medium_edge(
            {"preferred_term": "Unresolved species"}, "CultureMech:900001"
        )
        is None
    )
