"""Protect source-checked batch volumes and stock boundaries from reimport drift."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BACTERIAL = ROOT / "data/normalized_yaml/bacterial"
J1219 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219"
J284 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=284"
J805 = "https://www.bacmedia.dsmz.de/pdf/J805"


@pytest.fixture(scope="module")
def methylotroph():
    return yaml.safe_load((BACTERIAL / "TOGO_M1308_Methylotroph_Medium.yaml").read_text())


def support(node, reference, field):
    entries = [e for e in node["evidence"] if e["reference"] == reference]
    assert len(entries) == 1
    entry = entries[0]
    assert entry["supports"] == "SUPPORT"
    assert entry["snippet"].strip()
    assert field in entry["explanation"]
    return entry


@pytest.mark.parametrize("index,value", [(0, "0.97"), (8, "0.00081")])
def test_methylotroph_liquids_are_batch_volumes(methylotroph, index, value):
    node = methylotroph["ingredients"][index]
    assert node["concentration"] == {"value": value, "unit": "L"}
    support(node, J1219, f"ingredients[{index}].concentration")


@pytest.mark.parametrize(
    "index,value", [(0, "0.01"), (1, "0.01"), (2, "0.01"), (3, "0.002"), (4, "0.002")]
)
def test_stock_additions_are_not_mass_concentrations(methylotroph, index, value):
    assert methylotroph["solutions"][index]["concentration"] == {"value": value, "unit": "L"}
    support(methylotroph, J1219, f"solutions[{index}].concentration")


@pytest.mark.parametrize("index", [3, 4])
def test_metal_stock_strength_is_separate_from_dose(methylotroph, index):
    node = methylotroph["solutions"][index]["composition"][0]
    assert node["concentration"] == {"value": "10", "unit": "MILLIMOLAR"}
    assert (
        support(node, J1219, f"solutions[{index}].composition[0].concentration")["snippet"]
        == "10 mM"
    )


def test_trace_element_evidence_is_scoped_to_stock_not_medium(methylotroph):
    stock = methylotroph["solutions"][0]
    assert len(stock["composition"]) == 10
    for index, node in enumerate(stock["composition"]):
        entry = support(node, J284, f"solutions[0].composition[{index}].concentration")
        assert "1.0 L" in entry["explanation"]
        assert "not in the final medium" in entry["explanation"]
        assert node["concentration"]["unit"] == "G_PER_L"


def test_koh_remains_a_source_explicit_variable_dose(methylotroph):
    node = methylotroph["ingredients"][7]
    assert node["preferred_term"] == "KOH"
    assert node["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert support(node, J1219, "ingredients[7].concentration")["snippet"] == (
        "Mix components and adjust pH to 7.0 with 6 N KOH."
    )


@pytest.mark.parametrize("filename", ["1_10_r2a_broth.yaml", "TOGO_M840_1_10_R2A_Broth.yaml"])
def test_r2a_evidence_retains_the_verified_concentration(filename):
    doc = yaml.safe_load((BACTERIAL / filename).read_text())
    broth, water = doc["ingredients"]
    assert broth["concentration"] == {"value": "0.32", "unit": "G_PER_L"}
    assert water["concentration"] == {"value": "1.0", "unit": "L"}
    assert support(broth, J805, "ingredients[0].concentration")["snippet"].endswith("0.32 g")
    assert (
        "Final volume: 1000 ml"
        in support(broth, J805, "ingredients[0].concentration")["explanation"]
    )
    assert (
        support(water, J805, "ingredients[1].concentration")["snippet"]
        == "Distilled water 1000.00 ml"
    )


def test_main_medium_denominators_have_not_been_promoted(methylotroph):
    for index in (1, 2, 3, 4, 5, 6):
        refs = {e["reference"] for e in methylotroph["ingredients"][index].get("evidence", [])}
        assert J1219 not in refs


@pytest.mark.parametrize("stock_index,source", [(1, 3981), (2, 3861)])
def test_nested_stock_evidence_does_not_assert_a_receiving_medium_concentration(
    methylotroph, stock_index, source
):
    import json
    from decimal import Decimal

    stock = methylotroph["solutions"][stock_index]
    assert stock["concentration"] == {"value": "0.01", "unit": "L"}
    for index, node in enumerate(stock["composition"]):
        evidence = support(
            node,
            f"https://mediadive.dsmz.de/rest/solution/{source}",
            f"solutions[{stock_index}].composition[{index}].concentration",
        )
        row = json.loads(evidence["snippet"])
        assert node["preferred_term"] == row["compound"]
        assert node["concentration"]["unit"] == "MG_PER_L"
        assert Decimal(node["concentration"]["value"]) == Decimal(str(row["g_l"])) * 1000
        assert "https://mediadive.dsmz.de/rest/medium/J1219" in evidence["explanation"]
        assert "not an independently measured final volume" in evidence["explanation"]


def test_review_reports_cover_each_exact_target_once():
    folder = ROOT / "reports/ingredient_concentration_curation/20261007-jcm"
    for filename, claims in [
        ("TOGO_M1308_Methylotroph_Medium", 38),
        ("1_10_r2a_broth", 2),
        ("TOGO_M840_1_10_R2A_Broth", 2),
    ]:
        lines = (folder / f"{filename}.md").read_text().splitlines()
        assert [line for line in lines if line.startswith("- Record:")] == [
            f"- Record: data/normalized_yaml/bacterial/{filename}.yaml"
        ]
        assert sum(line.startswith("| `") for line in lines) == claims
