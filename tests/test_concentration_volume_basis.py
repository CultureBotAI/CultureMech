"""Carrier and stock volume bases must survive publication without reinterpretation."""

from copy import deepcopy

import pytest
from bs4 import BeautifulSoup

from culturemech.export.kgx_export import _quantity, medium_to_solution_edge, to_edge
from culturemech.render_media_pages import make_env, write_index

BASIS = "per liter of starting Pasteurized Seawater before supplement addition"
AMOUNT = {"value": "10", "unit": "ML_PER_L", "per_volume": BASIS}


@pytest.mark.parametrize("value", ["10", "0", "5e-05", "1-2", "variable"])
def test_qualified_dose_survives_without_a_bare_numeric_pair(value):
    qualifiers, numeric, unit = _quantity({**AMOUNT, "value": value})
    assert qualifiers == [
        {
            "qualifier_type_id": "biolink:concentration",
            "qualifier_value": f"{value} ML_PER_L ({BASIS})",
        }
    ]
    assert numeric is None and unit is None


@pytest.mark.parametrize("basis", [None, "", "   "])
def test_unqualified_amounts_keep_the_existing_numeric_contract(basis):
    qualifiers, numeric, unit = _quantity({**AMOUNT, "per_volume": basis})
    assert qualifiers[0]["qualifier_value"] == "10 ML_PER_L"
    assert (numeric, unit) == ("10", "ML_PER_L")


def test_flattened_kgx_row_retains_the_exact_basis():
    edge = medium_to_solution_edge(
        "CultureMech:000161", {"preferred_term": "Modified P-IV", "concentration": AMOUNT}
    )
    flat = to_edge(edge)
    assert flat.concentration == f"10 ML_PER_L ({BASIS})"
    assert flat.value is None and flat.unit is None


def render_partial(partial, medium):
    env = make_env()
    env.globals["chebi_structure"] = lambda _row: None
    rendered = env.get_template(f"_partials/{partial}.html.j2").render(medium=medium)
    return rendered, BeautifulSoup(rendered, "html.parser")


def test_direct_ingredient_amount_cell_has_its_own_basis():
    _, soup = render_partial(
        "ingredients", {"ingredients": [{"preferred_term": "Soil medium", "concentration": AMOUNT}]}
    )
    cell = soup.select("tbody td")[2].get_text(" ", strip=True)
    assert "10" in cell and "ML_PER_L" in cell and BASIS in cell


@pytest.mark.parametrize("kind", [None, "SOLUTION"])
def test_standalone_solution_composition_is_not_silently_omitted(kind):
    _, soup = render_partial(
        "ingredients",
        {
            "record_kind": kind,
            "composition": [{"preferred_term": "Stock chemical", "concentration": AMOUNT}],
        },
    )
    assert "Stock composition" in soup.h2.get_text()
    assert soup.select_one("tbody") is not None
    assert "Stock chemical" in soup.select_one("tbody").get_text()
    assert BASIS in soup.select_one("tbody").get_text()


def test_curated_solution_keeps_its_media_shaped_ingredients():
    _, soup = render_partial(
        "ingredients",
        {
            "record_kind": "SOLUTION",
            "ingredients": [{"preferred_term": "Retained chemical", "concentration": AMOUNT}],
        },
    )
    assert "Retained chemical" in soup.select_one("tbody").get_text()
    assert BASIS in soup.select_one("tbody").get_text()


def test_standalone_stock_name_is_visible_in_page_and_index(tmp_path):
    medium = {"id": "CultureMech:999999", "preferred_term": "Named stock", "composition": []}
    env = make_env()
    html = env.get_template("media.html.j2").render(medium=medium)
    soup = BeautifulSoup(html, "html.parser")
    assert soup.h1.get_text() == "Named stock"
    assert "Named stock" in soup.title.get_text()
    write_index(env, tmp_path, tmp_path / "records", [{"medium": medium, "slug": "999999"}])
    assert (
        "Named stock"
        in BeautifulSoup((tmp_path / "index.html").read_text(), "html.parser").get_text()
    )


def test_schema_native_nested_stocks_keep_doses_and_composition_separate():
    medium = {
        "solutions": [
            {
                "preferred_term": "Outer stock",
                "concentration": AMOUNT,
                "composition": [
                    {
                        "preferred_term": "Outer chemical",
                        "concentration": {
                            "value": "3",
                            "unit": "G_PER_L",
                            "per_volume": "per liter of outer stock",
                        },
                    }
                ],
                "solutions": [
                    {
                        "preferred_term": "Inner stock",
                        "concentration": {"value": "25", "unit": "PERCENT_V_V"},
                        "composition": [
                            {
                                "preferred_term": "Inner chemical",
                                "concentration": {"value": "0.70", "unit": "MOLAR"},
                            }
                        ],
                    }
                ],
            }
        ]
    }
    old = deepcopy(medium)
    _, soup = render_partial("solutions", medium)
    assert [node.get_text() for node in soup.select("h3, h4")] == ["Outer stock", "Inner stock"]
    doses = [node.get_text(" ", strip=True) for node in soup.select(".solution > p")]
    assert BASIS in doses[0] and "25" in doses[1] and "PERCENT_V_V" in doses[1]
    tables = [node.get_text(" ", strip=True) for node in soup.select("table")]
    assert "Outer chemical" in tables[0] and "per liter of outer stock" in tables[0]
    assert "Inner chemical" not in tables[0]
    assert "Inner chemical" in tables[1] and "0.70" in tables[1] and "MOLAR" in tables[1]
    assert medium == old


def test_legacy_stock_fields_are_still_displayed():
    _, soup = render_partial(
        "solutions",
        {
            "solutions": [
                {
                    "name": "Legacy",
                    "ingredients": [{"name": "Legacy component", "concentration": AMOUNT}],
                }
            ]
        },
    )
    assert soup.h3.get_text() == "Legacy"
    assert "Legacy component" in soup.table.get_text()
    assert BASIS in soup.table.get_text()


@pytest.mark.parametrize("partial", ["ingredients", "solutions"])
def test_untrusted_basis_is_escaped(partial):
    hostile = '<script>alert("basis")</script>'
    medium = {
        partial: [{"preferred_term": "Dose", "concentration": {**AMOUNT, "per_volume": hostile}}]
    }
    html, soup = render_partial(partial, medium)
    assert "&lt;script&gt;" in html and not soup.find("script")
    assert hostile in soup.get_text()
