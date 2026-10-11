"""Mutation probes for the independent source-to-merge retention comparator."""

import importlib.util
from copy import deepcopy
from pathlib import Path

import pytest

PATH = (
    Path(__file__).resolve().parents[1]
    / "reports/ingredient_concentration_curation/20261008-formulation-merge/audit.py"
)
SPEC = importlib.util.spec_from_file_location("formulation_retention_audit", PATH)
audit = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(audit)


def record():
    return {
        "ingredients": [
            {
                "preferred_term": "Salt",
                "concentration": {"value": "1", "unit": "G_PER_L"},
                "evidence": [{"reference": "https://example.org", "snippet": "Exact quote"}],
            }
        ]
    }


@pytest.mark.parametrize("mutation", ["amount", "unit", "quote", "lost", "extra", "stage"])
def test_scientific_mutations_are_detected(mutation):
    before = record()
    after = deepcopy(before)
    ingredient = after["ingredients"][0]
    if mutation == "amount":
        ingredient["concentration"]["value"] = "2"
    elif mutation == "unit":
        ingredient["concentration"]["unit"] = "L"
    elif mutation == "quote":
        ingredient["evidence"][0]["snippet"] = "Different quote"
    elif mutation == "lost":
        ingredient.pop("evidence")
    elif mutation == "extra":
        ingredient["chemical_formula"] = "Unasserted"
    else:
        after["solutions"] = after.pop("ingredients")
    assert audit.compare(before, after, root=True)


def test_new_numeric_assertion_cannot_hide_in_a_previously_unquantified_node():
    before = record()
    after = deepcopy(before)
    before["ingredients"][0].pop("concentration")
    assert audit.compare(before, after, root=True)


def test_additional_evidence_is_allowed_but_does_not_replace_existing_quotes():
    before = record()
    after = deepcopy(before)
    after["ingredients"][0]["evidence"].append(
        {"reference": "https://example.org/2", "snippet": "Second quote"}
    )
    assert audit.compare(before, after, root=True) == []
