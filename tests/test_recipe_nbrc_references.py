"""NBRC table quotations require the exact requested medium and literal quantities."""

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

FIXTURE = Path(__file__).parent / "fixtures/recipe_references/NBRC1219.json"
BASE = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet"
TITLE = "Catalogue Detail Medium | NITE - NBRC Culture Catalogue"


def capture():
    return json.loads(FIXTURE.read_text())


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def fail(*args, **kwargs):
        pytest.fail("Unexpected network access in offline NBRC reference tests")

    monkeypatch.setattr(requests.Session, "get", fail)


@pytest.fixture
def config(tmp_path):
    return ReferenceValidationConfig(cache_dir=tmp_path, rate_limit_delay=0)


def seeded(config, value=None):
    value = value or capture()
    source = rr.recipe_source(value["url"])
    cache = rr.RecipeSourceCache(config)
    cache.directory.mkdir(parents=True, exist_ok=True)
    cache.path(source).write_text(json.dumps(value))
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    return validator, source


def mutate(soup):
    value = capture()
    value["raw"] = str(soup)
    value["sha256"] = hashlib.sha256(value["raw"].encode()).hexdigest()
    return value


@pytest.mark.parametrize(
    "quote",
    [
        "Medium No. 1219",
        "Medium Middlebrook 7H11 Agar",
        "Pancreatic digest of casein 1.0 g",
        "Magnesium sulfate 0.05 g",
        "Malachite green 0.25 mg",
        "OADC enrichment* 100 mL",
        "Glycerol 5.0 mL",
        "Distilled water 900 mL",
        "Bovine albumin (Fraction V) 50.0 g",
        "Catalase 0.03 g",
        "Oleic acid 0.6 mL",
        "Distilled water 1 L",
    ],
)
def test_real_recipe_and_original_failed_quote(config, quote):
    value = capture()
    assert hashlib.sha256(value["raw"].encode()).hexdigest() == value["sha256"]
    assert not rr.literal_match(quote, value["raw"])
    validator, source = seeded(config)
    result = validator.validate(quote, "url:" + source.url, expected_title=TITLE, path="evidence")
    assert result.is_valid, result.message
    assert result.path == "evidence" and result.match_result.similarity_score == 1.0
    assert validator.validate_title(source.url, TITLE).is_valid
    assert not validator.validate_title(source.url, "Invented medium title").is_valid
    validator.fallback.validate.assert_not_called()
    validator.fallback.validate_title.assert_not_called()


@pytest.mark.parametrize("accession", ["1", "1219", "1604"])
def test_source_urls(accession):
    source = rr.recipe_source(BASE + "?NO=" + accession)
    assert source.provider == "nbrc" and source.accession == accession


@pytest.mark.parametrize(
    "url",
    [
        BASE,
        BASE + "?NO=",
        BASE + "?NO=0",
        BASE + "?NO=01219",
        BASE + "?NO=-1",
        BASE + "?NO=1219a",
        BASE + "?NO=1219%0A",
        BASE + "?NO=1219#composition",
        BASE + "?NO=1219&NO=1219",
        BASE + "?NO=1219&lang=en",
        BASE + "?no=1219",
        BASE + "/extra?NO=1219",
        BASE.replace("https:", "http:") + "?NO=1219",
        BASE.replace("nite.go.jp", "nite.go.jp.evil.invalid") + "?NO=1219",
        BASE.replace("//www", "//user:pass@www") + "?NO=1219",
        BASE.replace(".jp/", ".jp:443/") + "?NO=1219",
    ],
)
def test_out_of_scope_urls(url):
    assert rr.recipe_source(url) is None


@pytest.mark.parametrize(
    "mutation,error",
    [
        ("wrong_id", "source_identity"),
        ("empty_name", "source_identity"),
        ("wrong_title", "source_metadata"),
        ("duplicate_title", "source_metadata"),
        ("missing_main", "source_format"),
        ("duplicate_main", "source_format"),
        ("missing_composition", "source_format"),
        ("duplicate_composition", "source_format"),
        ("wrong_heading", "source_format"),
        ("duplicate_heading", "source_format"),
        ("extra_identity_row", "source_format"),
        ("wrong_identity_label", "source_format"),
        ("swapped_identity", "source_format"),
        ("identity_nested_table", "source_format"),
        ("missing_recipe_table", "source_format"),
        ("duplicate_recipe_table", "source_format"),
        ("nested_recipe_table", "source_format"),
        ("empty_recipe", "source_unavailable"),
        ("empty_row", "source_format"),
        ("rowspan", "source_format"),
        ("composition_outside_main", "source_format"),
        ("challenge", "source_metadata"),
    ],
)
def test_malformed_recipe_fails_closed(config, mutation, error):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    comp = soup.find(id="medium-comp")
    detail, recipe = comp.find_parent("table"), comp.find("table")
    identity = detail.find_all("tr")[:2]
    if mutation == "wrong_id":
        identity[0].find("td").string = "1220"
    elif mutation == "empty_name":
        identity[1].find("td").string = ""
    elif mutation == "wrong_title":
        soup.title.string = "Access denied"
    elif mutation == "duplicate_title":
        soup.title.insert_after(copy.copy(soup.title))
    elif mutation == "missing_main":
        soup.main.unwrap()
    elif mutation == "duplicate_main":
        soup.main.insert_after(copy.copy(soup.main))
    elif mutation == "missing_composition":
        del comp["id"]
    elif mutation == "duplicate_composition":
        comp.insert_after(copy.copy(comp))
    elif mutation == "wrong_heading":
        soup.main.h3.string = "Search results"
    elif mutation == "duplicate_heading":
        soup.main.h3.insert_after(copy.copy(soup.main.h3))
    elif mutation == "extra_identity_row":
        identity[0].insert_after(copy.copy(identity[0]))
    elif mutation == "wrong_identity_label":
        identity[0].find("th").string = "Strain No."
    elif mutation == "swapped_identity":
        identity[0].insert_before(identity[1].extract())
    elif mutation == "identity_nested_table":
        identity[0].find("td").append(soup.new_tag("table"))
    elif mutation == "missing_recipe_table":
        recipe.unwrap()
    elif mutation == "duplicate_recipe_table":
        recipe.insert_after(copy.copy(recipe))
    elif mutation == "nested_recipe_table":
        recipe.find("td").append(soup.new_tag("table"))
    elif mutation == "empty_recipe":
        recipe.clear()
    elif mutation == "empty_row":
        recipe.find("tr").clear()
    elif mutation == "rowspan":
        recipe.find("td")["rowspan"] = "2"
    elif mutation == "composition_outside_main":
        soup.main.insert_after(detail.extract())
    elif mutation == "challenge":
        soup = BeautifulSoup("<html><body>Verify browser</body></html>", "html.parser")
    validator, source = seeded(config, mutate(soup))
    result = validator.validate("Distilled water 900 mL", source.url)
    assert not result.is_valid and error in result.message, result.message
    validator.fallback.validate.assert_not_called()


@pytest.mark.parametrize(
    "attribute,value",
    [
        ("hidden", ""),
        ("aria-hidden", "true"),
        ("style", "display: none"),
        ("style", "visibility: hidden"),
        ("class", "d-none"),
        ("class", "invisible"),
    ],
)
@pytest.mark.parametrize("location", ["main", "detail", "composition", "ingredient"])
def test_hidden_recipe_is_rejected(config, attribute, value, location):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    comp = soup.find(id="medium-comp")
    target = {
        "main": soup.main,
        "detail": comp.find_parent("table"),
        "composition": comp,
        "ingredient": comp.find("td"),
    }[location]
    target[attribute] = value
    validator, source = seeded(config, mutate(soup))
    result = validator.validate("Distilled water 900 mL", source.url)
    assert not result.is_valid and "hidden" in result.message


@pytest.mark.parametrize(
    "quote",
    [
        "Distilled water 895 mL",
        "Distilled water 900 ml",
        "Distilled water 900 g",
        "Distilled water 90 mL",
        "Distilled water 900.0 mL",
        "Distilled water -900 mL",
        "Catalase 0.003 g",
        "Catalase 0.03 mg",
        "Catalase 0.03 g/L",
        "Bovine albumin 50.0 g",
        "Glycerol 5 mL",
        "Oleic acid 0.6 g",
    ],
)
def test_quantities_units_precision_and_forms_are_not_normalized(config, quote):
    validator, source = seeded(config)
    assert not validator.validate(quote, source.url).is_valid


def test_nonrecipe_text_cannot_supply_evidence(config):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    for tag in ("p", "script", "style", "noscript", "template"):
        extra = soup.new_tag(tag)
        extra.string = "Invented ingredient 999 g/L"
        soup.main.append(extra)
    validator, source = seeded(config, mutate(soup))
    assert not validator.validate("Invented ingredient 999 g/L", source.url).is_valid
    assert not validator.validate("Contact", source.url).is_valid


def test_inline_chemical_formula_and_comment_preserve_literal_text(config):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    node = soup.find(string="Magnesium sulfate")
    node.replace_with(BeautifulSoup("MgSO<sub>4</sub>&middot;7H<sub>2</sub>O", "html.parser"))
    comment = soup.find(id="medium-comp").find_parent("table").find_all("tr")[-1]
    comment.find("td").string = "Final pH 6.6 +/- 0.2 at 25 C."
    validator, source = seeded(config, mutate(soup))
    assert validator.validate("MgSO4\u00b77H2O 0.05 g", source.url).is_valid
    assert validator.validate("Final pH 6.6 +/- 0.2 at 25 C.", source.url).is_valid
    assert not validator.validate("MgSO4\u00b76H2O 0.05 g", source.url).is_valid


@pytest.mark.parametrize("status,url", [(302, None), (403, None), (200, "https://example.org/")])
def test_access_failures_do_not_fall_back_or_cache(config, status, url):
    value = capture()
    response = Mock(status_code=status, url=url or value["url"])
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    session = Mock()
    session.get.return_value = response
    cache = rr.RecipeSourceCache(config, session=session)
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    result = validator.validate("Distilled water 900 mL", value["url"])
    assert not result.is_valid and "source_access" in result.message
    assert not cache.path(rr.recipe_source(value["url"])).exists()
    validator.fallback.validate.assert_not_called()
