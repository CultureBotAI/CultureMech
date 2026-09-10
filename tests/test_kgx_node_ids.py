"""A KGX node is keyed on the record's permanent id, never on its name (#438).

Node emission dedupes on id, so the name-keyed ids the export used until #438
collapsed every record sharing a name into one node with merged edges — 3,181
media and 4,787 solution records on the 2026-09-09 corpus. The 4,784 MediaDive
solution records carry ``preferred_term`` and no ``name`` at all, so they
sanitized to the empty string and emitted no node while their ``has_part``
edges still pointed at ``culturemech:``.

Kept free of corpus paths on purpose: conftest tiers a module by substring, and
these cases need no records.
"""

from __future__ import annotations

import pytest

from culturemech.export.kgx_export import (
    is_solution_record,
    nodes,
    record_label,
    record_node_id,
    transform,
)

MEDIUM = {
    "id": "CultureMech:900101",
    "name": "Defined freshwater medium (CoSO4)",
    "medium_type": "DEFINED",
    "ingredients": [{"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"}}],
}
# The #392 shape: a second record whose name sanitizes to the same string.
TWIN = {**MEDIUM, "id": "CultureMech:900102"}

# The MediaDive solution-record shape: preferred_term, no name, upstream term id.
SOLUTION = {
    "id": "CultureMech:900103",
    "preferred_term": "SL10 elements",
    "term": {"id": "mediadive.solution:4367"},
    "composition": [{"preferred_term": "ZnSO4", "term": {"id": "CHEBI:32312"}}],
}


def _record_node(record):
    by_id = {n["id"]: n for n in nodes(record)}
    return by_id[record_node_id(record)]


def test_the_node_id_is_the_record_id():
    assert record_node_id(MEDIUM) == "CultureMech:900101"
    assert _record_node(MEDIUM)["id"] == "CultureMech:900101"


def test_records_sharing_a_name_keep_distinct_nodes_and_edges():
    """The collapse: same name, different records, one node before #438."""
    assert record_node_id(MEDIUM) != record_node_id(TWIN)
    subjects = {e["subject"] for e in transform(MEDIUM)} | {e["subject"] for e in transform(TWIN)}
    assert subjects == {"CultureMech:900101", "CultureMech:900102"}


def test_a_solution_record_with_no_name_gets_a_node_labelled_by_preferred_term():
    node = _record_node(SOLUTION)
    assert node["name"] == "SL10 elements"
    assert node["category"] == ["biolink:ChemicalMixture"]


def test_a_solution_record_is_recognised_by_either_explicit_signal():
    assert is_solution_record(SOLUTION)
    assert is_solution_record({"id": "CultureMech:900104", "name": "x", "record_kind": "SOLUTION"})
    assert not is_solution_record(MEDIUM)


def test_a_medium_is_a_growth_medium_not_a_bare_mixture():
    assert "biolink:GrowthMedium" in _record_node(MEDIUM)["category"]


def test_label_falls_back_from_name_to_preferred_term():
    assert record_label(MEDIUM) == "Defined freshwater medium (CoSO4)"
    assert record_label(SOLUTION) == "SL10 elements"


@pytest.mark.parametrize("bad", [{}, {"id": ""}, {"id": "   "}, {"name": "LB"}])
def test_a_record_without_an_id_is_an_error_not_a_name_keyed_node(bad):
    """Falling back to the name would quietly reinstate the collapse."""
    with pytest.raises(ValueError, match="no id"):
        record_node_id(bad)
    with pytest.raises(ValueError):
        list(nodes(bad))
    with pytest.raises(ValueError):
        list(transform(bad))


# The curated `record_kind: SOLUTION` shape (#175): MediaRecipe fields, no name.
CURATED_SOLUTION = {
    "id": "CultureMech:900105",
    "preferred_term": "Trace salt solution",
    "record_kind": "SOLUTION",
    "ingredients": [{"preferred_term": "ZnSO4", "term": {"id": "CHEBI:32312"}}],
}


def test_edges_from_a_solution_record_use_its_id_not_the_empty_local_id():
    subjects = {e["subject"] for e in transform(CURATED_SOLUTION)}
    assert subjects == {"CultureMech:900105"}
    assert _record_node(CURATED_SOLUTION)["category"] == ["biolink:ChemicalMixture"]
