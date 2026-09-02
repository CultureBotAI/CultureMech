"""What the KGX export drops, and what kind of thing it is (#372).

`kgx_export` mints an edge only when an ingredient resolves, and neither of its
two `if not chem_id: return None` sites counts what it discarded — so the
export's totals read as complete while 14,793 rows leave no trace anywhere.

The classification is the load-bearing part. #372 proposes emitting these rows
under kg-microbe's `INGREDIENT_CATEGORY`, and most of them are not ingredients:
one placeholder string accounts for 4,775 rows. Minting thousands of
`biolink:ChemicalEntity` nodes called "See source for composition" would be
worse than dropping them.

Every literal is a real `preferred_term` from the corpus.
"""

from __future__ import annotations

import pytest
from audit_ungrounded_ingredients import classify_name


@pytest.mark.parametrize(
    ("name", "kind"),
    [
        ("See source for composition", "PLACEHOLDER"),
        ("Trace vitamins (see Medium [M190])", "CROSS_REFERENCE"),
        ("Trace element solution (see Medium [M180])", "CROSS_REFERENCE"),
        ("Seven vitamins solution", "SOLUTION_NAME"),
        ("5% Na2S・9H2O solution", "SOLUTION_NAME"),
        ("Wolfe's mineral elixir", "SOLUTION_NAME"),
        ("Sodium phosphate buffer", "SOLUTION_NAME"),
        ("Calf brains", "UNRESOLVED_CHEMICAL"),
        ("Agar (if needed)", "UNRESOLVED_CHEMICAL"),
        ("", "EMPTY"),
    ],
)
def test_a_name_is_classified_by_what_it_actually_is(name, kind):
    assert classify_name(name) == kind


def test_a_cross_reference_outranks_the_word_solution():
    """`Trace element solution (see Medium [M180])` points at a medium.

    It is both a solution name and a cross-reference; the cross-reference is the
    actionable fact, because the target is a record we already hold.
    """
    assert classify_name("Trace element solution (see Medium [M180])") == "CROSS_REFERENCE"


def test_a_plain_chemical_is_not_swept_into_a_bucket():
    for name in ("Glucose", "NaCl", "MgSO4 x 7 H2O", "Yeast extract"):
        assert classify_name(name) == "UNRESOLVED_CHEMICAL"


def test_whitespace_only_is_empty_not_a_chemical():
    assert classify_name("   ") == "EMPTY"
