"""KOMODO quotes must match the identified recipe, not raw tags or SEED totals."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from unittest.mock import Mock

import pytest
import requests
from bs4 import BeautifulSoup
from linkml_reference_validator.models import ReferenceValidationConfig

from culturemech.validation import recipe_references as rr

FIXTURES = Path(__file__).parent / "fixtures" / "recipe_references"
BASE = "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed"


def capture(name="K1021"):
    return json.loads((FIXTURES / (name + ".json")).read_text())


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def fail(*args, **kwargs):
        pytest.fail("Unexpected network access in offline KOMODO reference tests")

    monkeypatch.setattr(requests.Session, "get", fail)


@pytest.fixture
def config(tmp_path):
    return ReferenceValidationConfig(cache_dir=tmp_path, rate_limit_delay=0)


def seeded(config, name="K1021", value=None):
    value = value or capture(name)
    source = rr.recipe_source(value["url"])
    cache = rr.RecipeSourceCache(config)
    cache.directory.mkdir(parents=True, exist_ok=True)
    cache.path(source).write_text(json.dumps(value))
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    return validator, source


@pytest.mark.parametrize("name", ["K1021", "K1021_16929"])
def test_real_pages(config, name):
    value = capture(name)
    assert hashlib.sha256(value["raw"].encode()).hexdigest() == value["sha256"]
    validator, source = seeded(config, name)
    assert validator.validate_title(source.url, "KOMODO - the Known Media Database").is_valid
    assert validator.validate(
        "Gram & Mol amounts are per Liter of medium.", "url:" + source.url
    ).is_valid
    assert not validator.validate("cpd00971 Na+ 0.12394119060972678", source.url).is_valid
    assert not validator.validate_title(source.url, "An invented recipe title").is_valid
    validator.fallback.validate.assert_not_called()
    validator.fallback.validate_title.assert_not_called()


@pytest.mark.parametrize("case", json.loads((FIXTURES / "komodo_failed_excerpts.json").read_text()))
def test_all_31_prior_failures(config, case):
    validator, source = seeded(config, case["capture"])
    assert not rr.literal_match(case["snippet"], capture(case["capture"])["raw"])
    result = validator.validate(case["snippet"], source.url, path=case["path"])
    assert result.is_valid, result.message
    assert result.path == case["path"]
    assert result.match_result.similarity_score == 1.0
    validator.fallback.validate.assert_not_called()


@pytest.mark.parametrize(
    "accession",
    [
        "1021",
        "1021_16929",
        "645a",
        "679.1",
        "488_replace_DESULFOVIBRIO%20medium_with_DESULFOBULBUS%20MEDIUM",
    ],
)
@pytest.mark.parametrize("prefix", ["/komodo/servlet/", "/servlet/"])
def test_supported_urls(accession, prefix):
    url = (
        "https://komodo.modelseed.org"
        + prefix
        + "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
        + accession
    )
    source = rr.recipe_source(url)
    assert source and source.provider == "komodo"
    assert source.url == url


@pytest.mark.parametrize(
    "url",
    [
        BASE + "?MediaList",
        BASE + "?MediaInfo=",
        BASE + "?MediaInfo=0",
        BASE + "?MediaInfo=1021&MediaInfo=1021",
        BASE + "?MediaInfo=1021&other=1",
        BASE + "?MediaInfo=1021#other",
        BASE + "?MediaInfo=1021%0A",
        BASE + "?MediaInfo=1021%2F16929",
        BASE + "?MediaInfo=1021_<script>",
        BASE.replace("https:", "http:") + "?MediaInfo=1021",
        BASE.replace("modelseed.org", "modelseed.org.evil.invalid") + "?MediaInfo=1021",
        BASE.replace("//komodo", "//user:pass@komodo") + "?MediaInfo=1021",
        BASE.replace(".org/", ".org:443/") + "?MediaInfo=1021",
        BASE + "/other?MediaInfo=1021",
    ],
)
def test_out_of_scope_urls(url):
    assert rr.recipe_source(url) is None


def tables(soup):
    return soup.find_all("table")[1:3]


@pytest.mark.parametrize(
    "mutation,error",
    [
        ("wrong_id", "source_identity"),
        ("variant_for_base", "source_identity"),
        ("duplicate_features", "source_format"),
        ("duplicate_recipe", "source_format"),
        ("duplicate_id", "source_format"),
        ("duplicate_ingredient", "source_format"),
        ("conflicting_ingredient", "source_format"),
        ("missing_recipe", "source_format"),
        ("empty_recipe", "source_unavailable"),
        ("missing_column", "source_format"),
        ("reordered_columns", "source_format"),
        ("short_row", "source_format"),
        ("extra_cell", "source_format"),
        ("blank_cell", "source_format"),
        ("merged_cell", "source_format"),
        ("nested_table", "source_format"),
        ("nonnumeric_amount", "source_format"),
        ("name_mismatch", "source_identity"),
        ("missing_basis", "source_format"),
        ("wrong_basis", "source_format"),
        ("wrong_title", "source_metadata"),
        ("duplicate_title", "source_metadata"),
        ("challenge", "source_metadata"),
        ("swapped_tables", "source_format"),
    ],
)
def test_malformed_sources_fail_closed(config, mutation, error):
    value = capture()
    soup = BeautifulSoup(value["raw"], "html.parser")
    features, ingredients = tables(soup)
    first = ingredients.find_all("tr")[1]
    if mutation == "wrong_id":
        features.find_all("tr")[0].find_all("td")[1].string = "9999"
    elif mutation == "variant_for_base":
        soup = BeautifulSoup(capture("K1021_16929")["raw"], "html.parser")
    elif mutation == "duplicate_features":
        features.insert_after(copy.copy(features))
    elif mutation == "duplicate_recipe":
        ingredients.insert_after(copy.copy(ingredients))
    elif mutation == "duplicate_id":
        features.append(copy.copy(features.find("tr")))
    elif mutation in {"duplicate_ingredient", "conflicting_ingredient"}:
        duplicate = copy.copy(first)
        if mutation == "conflicting_ingredient":
            duplicate.find_all("td")[3].string = "999.99"
        ingredients.append(duplicate)
    elif mutation == "missing_recipe":
        ingredients.decompose()
    elif mutation == "empty_recipe":
        for row in ingredients.find_all("tr")[1:]:
            row.decompose()
    elif mutation == "missing_column":
        ingredients.find("tr").find_all("td")[-1].decompose()
    elif mutation == "reordered_columns":
        cells = ingredients.find("tr").find_all("td")
        cells[3].string, cells[4].string = "Mol Amount", "Gram Amount"
    elif mutation == "short_row":
        first.find_all("td")[-1].decompose()
    elif mutation == "extra_cell":
        first.append(soup.new_tag("td"))
    elif mutation == "blank_cell":
        first.find_all("td")[3].string = ""
    elif mutation == "merged_cell":
        first.find("td")["colspan"] = "2"
    elif mutation == "nested_table":
        first.find("td").append(soup.new_tag("table"))
    elif mutation == "nonnumeric_amount":
        first.find_all("td")[3].string = "200 mg"
    elif mutation == "name_mismatch":
        features.find_all("tr")[1].find_all("td")[1].string = "Other medium"
    elif mutation in {"missing_basis", "wrong_basis"}:
        text = soup.find(string=lambda s: s and "Gram & Mol amounts" in s)
        text.replace_with(
            "" if mutation == "missing_basis" else str(text).replace("per Liter", "per mL")
        )
    elif mutation == "wrong_title":
        soup.title.string = "Access denied"
    elif mutation == "duplicate_title":
        soup.title.insert_after(copy.copy(soup.title))
    elif mutation == "challenge":
        soup = BeautifulSoup("<html><body>Verify your browser</body></html>", "html.parser")
    elif mutation == "swapped_tables":
        features.insert_before(ingredients.extract())
    value["raw"] = str(soup)
    value["sha256"] = hashlib.sha256(value["raw"].encode()).hexdigest()
    validator, source = seeded(config, value=value)
    result = validator.validate("SODALIS GLOSSINIDIUS medium", source.url)
    assert not result.is_valid and error in result.message, result.message
    validator.fallback.validate.assert_not_called()


@pytest.mark.parametrize(
    "old,new",
    [
        ("6.48", "6.4"),
        ("6.48", "6.480"),
        ("6.48", "-6.48"),
        ("casein", "lactalbumin"),
        ("null", "0"),
    ],
)
def test_scientific_mismatches_are_not_normalized(config, old, new):
    validator, source = seeded(config)
    quote = "casein hydrolysate casein hydrolysate rich-peptone# 6.48 null"
    assert not validator.validate(quote.replace(old, new), source.url).is_valid


def test_formula_inline_tags_exponents_signs_and_nulls(config):
    value = capture()
    value["raw"] = (
        value["raw"]
        .replace("NaHCO3", "NaHCO<sub>3</sub>")
        .replace("<TD>0.12</TD>", "<TD>-1.20E-3</TD>")
    )
    value["sha256"] = hashlib.sha256(value["raw"].encode()).hexdigest()
    validator, source = seeded(config, value=value)
    assert validator.validate(
        "NaHCO3 sodium bicarbonate SEED-cpd00242#cpd00971#cpd09249# -1.20E-3 0.00", source.url
    ).is_valid
    assert not validator.validate("NaHCO 3", source.url).is_valid
    assert not validator.validate("1.20E-3", source.url).is_valid


def test_nonrecipe_text_cannot_supply_recipe_claims(config):
    value = capture()
    value["raw"] = value["raw"].replace(
        "</body>",
        "<p>Invented ingredient 999 g/L</p><script>False ingredient 999 g/L</script></body>",
    )
    value["sha256"] = hashlib.sha256(value["raw"].encode()).hexdigest()
    validator, source = seeded(config, value=value)
    assert not validator.validate("Invented ingredient 999 g/L", source.url).is_valid
    assert not validator.validate("False ingredient 999 g/L", source.url).is_valid


@pytest.mark.parametrize(
    "status,url", [(302, None), (403, None), (200, "https://example.org/challenge")]
)
def test_http_redirects_errors_do_not_fall_back(config, status, url):
    value = capture()
    response = Mock(status_code=status, url=url or value["url"])
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    session = Mock()
    session.get.return_value = response
    cache = rr.RecipeSourceCache(config, session=session)
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    result = validator.validate("casein hydrolysate", value["url"])
    assert not result.is_valid and "source_access" in result.message
    validator.fallback.validate.assert_not_called()
    assert not cache.path(rr.recipe_source(value["url"])).exists()


@pytest.mark.parametrize(
    "attribute,value",
    [
        ("hidden", ""),
        ("aria-hidden", "true"),
        ("style", "display: none"),
        ("style", "visibility: hidden"),
    ],
)
@pytest.mark.parametrize("location", ["ancestor", "table", "cell"])
def test_hidden_recipe_content_is_not_evidence(config, attribute, value, location):
    entry = capture()
    soup = BeautifulSoup(entry["raw"], "html.parser")
    _, table = tables(soup)
    target = {"ancestor": table.parent, "table": table, "cell": table.find("td")}[location]
    target[attribute] = value
    entry["raw"] = str(soup)
    entry["sha256"] = hashlib.sha256(entry["raw"].encode()).hexdigest()
    validator, source = seeded(config, value=entry)
    result = validator.validate("casein hydrolysate", source.url)
    assert not result.is_valid and "hidden" in result.message
    validator.fallback.validate.assert_not_called()
