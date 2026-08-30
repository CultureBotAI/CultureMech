"""The UTEX composition table must be read by header, not by column position.

Every UTEX recipe in the corpus was corrupted the same way: the tables are
headed `# | Component | Amount | Stock Solution Concentration | Final
Concentration`, and the fetcher read `cols[0]` and `cols[1]`. So the row
ordinal became the ingredient name, the component name became the "amount",
and the real Amount column was never read. 497 ingredients across all 99 UTEX
records ended up named "1", "2", "3"...

The header row below is copied verbatim from
https://utex.org/products/one-to-one-dyiii-pea-gr-plus-medium.
"""

from __future__ import annotations

from culturemech.fetch.utex_fetcher import parse_composition_table

HEADER = ["#", "Component", "Amount", "Stock Solution Concentration", "Final Concentration"]

REAL_TABLE = [
    HEADER,
    ["1", "DYIII Medium", "90 mL", "", ""],
    ["2", "Pea", "1 per 200 mL", "", ""],
    ["3", "Soilwater: GR+ Medium", "90 mL", "", ""],
    ["4", "DAS Vitamin Cocktail", "4 drops", "", ""],
]


def test_the_ordinal_column_is_not_mistaken_for_the_name():
    entries = parse_composition_table(REAL_TABLE)
    assert [e["ingredient"] for e in entries] == [
        "DYIII Medium",
        "Pea",
        "Soilwater: GR+ Medium",
        "DAS Vitamin Cocktail",
    ]


def test_the_amount_column_is_actually_read():
    """The regression that lost every UTEX amount in the corpus."""
    entries = parse_composition_table(REAL_TABLE)
    assert [e["amount"] for e in entries] == ["90 mL", "1 per 200 mL", "90 mL", "4 drops"]


def test_the_header_row_is_not_emitted_as_an_ingredient():
    entries = parse_composition_table(REAL_TABLE)
    assert all(e["ingredient"] != "Component" for e in entries)
    assert len(entries) == 4


def test_a_table_without_a_component_header_is_skipped():
    """UTEX product pages carry cart and badge tables a positional reader eats."""
    assert parse_composition_table([["", "Freshwater Medium | 6 < pH < 8"]]) == []
    assert parse_composition_table([["Add to cart"], ["FAQs: Algal Culture Media"]]) == []


def test_column_order_does_not_matter():
    """The point of reading the header: a reordered table still parses."""
    entries = parse_composition_table(
        [["Amount", "Component"], ["10 g/L", "Glucose"]]
    )
    assert entries == [{"ingredient": "Glucose", "amount": "10 g/L"}]


def test_the_concentration_columns_are_captured_when_present():
    entries = parse_composition_table(
        [HEADER, ["1", "NaNO3", "10 mL", "10 g/400 mL dH2O", "2.94 mM"]]
    )
    assert entries[0]["stock_concentration"] == "10 g/400 mL dH2O"
    assert entries[0]["final_concentration"] == "2.94 mM"


def test_empty_concentration_cells_are_omitted_rather_than_stored_blank():
    entry = parse_composition_table(REAL_TABLE)[0]
    assert "stock_concentration" not in entry
    assert "final_concentration" not in entry


def test_an_empty_component_cell_is_skipped():
    entries = parse_composition_table([HEADER, ["1", "", "90 mL", "", ""]])
    assert entries == []


def test_a_short_row_does_not_raise():
    """Real pages carry ragged rows; a colspan cell makes one shorter."""
    assert parse_composition_table([HEADER, ["1"]]) == []
    assert parse_composition_table([HEADER, ["1", "Glucose"]]) == [
        {"ingredient": "Glucose", "amount": ""}
    ]


def test_no_list_fallback_reads_the_navigation_menu():
    """A `<ul>`/`<ol>` fallback used to split every list item on ':' or '-'.

    On https://utex.org/products/bbm-boron-stock-solution — a page that states
    its composition in prose and has no composition table — it returned 18
    "ingredients" scraped from the site navigation, among them
    `{'RGB': 'LED Lighting Platform'}` and `{'Media Kits & Add': 'Ins'}`. It
    never produced a real ingredient, because all 99 UTEX media pages carry a
    proper table. An uncaptured page is reported, not guessed at.
    """
    import inspect

    from culturemech.fetch import utex_fetcher

    source = inspect.getsource(utex_fetcher.UTEXFetcher.fetch_recipe_details)
    assert "find_all(['ul', 'ol'])" not in source
