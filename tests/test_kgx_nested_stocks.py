"""Nested stock structure, volume bases and citations survive KGX publication."""

import hashlib
from copy import deepcopy

import pytest

from culturemech.export import kgx_export as kgx


def stock():
    return {
        "preferred_term": "Outer stock",
        "concentration": {"value": "10", "unit": "ML_PER_L"},
        "solutions": [
            {
                "preferred_term": "Inner stock",
                "concentration": {"value": "25", "unit": "PERCENT_V_V"},
                "composition": [
                    {
                        "preferred_term": "Sodium nitrate",
                        "term": {"id": "CHEBI:63005"},
                        "concentration": {
                            "value": "0.70",
                            "unit": "MOLAR",
                            "per_volume": "per liter of inner stock",
                        },
                        "evidence": [
                            {
                                "reference": "https://utex.org/products/das-macro-solution",
                                "snippet": "0.70 M",
                            }
                        ],
                    }
                ],
            }
        ],
    }


def record(outer):
    return {"id": "CultureMech:900001", "name": "Nested regression", "solutions": [outer]}


@pytest.fixture(autouse=True)
def empty_index(monkeypatch):
    monkeypatch.delenv(kgx.RECORDS_DIR_ENV, raising=False)


def test_nested_stocks_have_distinct_nodes_and_scoped_edges():
    outer = stock()
    inner = outer["solutions"][0]
    outer_id = kgx.nested_solution_target(outer)[0]
    inner_id = kgx.nested_solution_target(inner)[0]
    doc = record(outer)
    saved = deepcopy(doc)
    nodes = {n["id"]: n for n in kgx.nodes(doc)}
    assert nodes[outer_id]["name"] == "Outer stock"
    assert nodes[inner_id]["name"] == "Inner stock"
    edges = list(kgx.transform(doc))
    parent_link = next(e for e in edges if e["subject"] == outer_id and e["object"] == inner_id)
    assert (parent_link["value"], parent_link["unit"]) == ("25", "PERCENT_V_V")
    reagent = next(e for e in edges if e["subject"] == inner_id)
    assert reagent["object"] == "CHEBI:63005"
    assert reagent["value"] is None and reagent["unit"] is None
    assert "per liter of inner stock" in reagent["qualifiers"][0]["qualifier_value"]
    assert doc == saved


def test_stock_component_citations_are_not_dropped():
    ingredient = stock()["solutions"][0]["composition"][0]
    edge = kgx.solution_to_ingredient_edge("CultureMech:900002", ingredient)
    assert edge["publications"] == ["https://utex.org/products/das-macro-solution"]


@pytest.mark.parametrize(
    "change", ["basis", "nested_dose", "nested_strength", "nested_basis", "nested_name"]
)
def test_formulation_distinctions_change_the_stock_fingerprint(change):
    first = stock()
    second = deepcopy(first)
    if change == "basis":
        first = first["solutions"][0]
        second = second["solutions"][0]
        second["composition"][0]["concentration"]["per_volume"] = "per liter of initial water"
    elif change == "nested_dose":
        second["solutions"][0]["concentration"]["value"] = "30"
    elif change == "nested_strength":
        second["solutions"][0]["composition"][0]["concentration"]["value"] = "0.02"
    elif change == "nested_basis":
        second["solutions"][0]["concentration"]["per_volume"] = "per liter of starting carrier"
    else:
        second["solutions"][0]["preferred_term"] = "Different inner stock"
    assert kgx.nested_solution_target(first)[0] != kgx.nested_solution_target(second)[0]


def test_receiving_dose_is_not_part_of_stock_identity():
    first = stock()
    second = deepcopy(first)
    second["concentration"] = {
        "value": "20",
        "unit": "ML_PER_L",
        "per_volume": "per liter of carrier",
    }
    assert kgx.nested_solution_target(first)[0] == kgx.nested_solution_target(second)[0]


def test_permutation_of_nested_stocks_preserves_identity():
    first = stock()
    child = deepcopy(first["solutions"][0])
    child["preferred_term"] = "Second child"
    first["solutions"].append(child)
    second = deepcopy(first)
    second["solutions"].reverse()
    assert kgx.nested_solution_target(first)[0] == kgx.nested_solution_target(second)[0]


def test_flat_unqualified_stocks_keep_legacy_ids():
    value = {
        "preferred_term": "Flat stock",
        "composition": [
            {"preferred_term": "NaCl", "concentration": {"value": "1", "unit": "G_PER_L"}}
        ],
    }
    legacy = hashlib.sha1(repr(("Flat stock", [("NaCl", "1", "G_PER_L")])).encode()).hexdigest()[:8]
    assert kgx.nested_solution_target(value)[0] == "CultureMech:solution_Flat_stock_" + legacy


def test_referenced_child_is_linked_without_reminting_its_composition():
    outer = stock()
    child = outer["solutions"][0]
    child["culturemech_term"] = {"id": "CultureMech:900003", "label": "Referenced stock"}
    doc = record(outer)
    outer_id = kgx.nested_solution_target(outer)[0]
    assert any(
        e["subject"] == outer_id and e["object"] == "CultureMech:900003" for e in kgx.transform(doc)
    )
    assert not any(e["subject"] == "CultureMech:900003" for e in kgx.transform(doc))
    assert not any(n["id"] == "CultureMech:900003" for n in kgx.nodes(doc))


@pytest.mark.parametrize("operation", ["fingerprint", "nodes", "edges"])
def test_inline_cycles_are_rejected_explicitly(operation):
    outer = stock()
    outer["solutions"][0]["solutions"] = [outer]
    with pytest.raises(ValueError, match="[Cc]yclic"):
        if operation == "fingerprint":
            kgx.nested_solution_target(outer)
        elif operation == "nodes":
            list(kgx.nodes(record(outer)))
        else:
            list(kgx.transform(record(outer)))
