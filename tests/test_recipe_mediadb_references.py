"""MediaDB evidence must match an identified table row, not markup or nearby prose."""

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

FIXTURE = Path(__file__).parent / "fixtures/recipe_references/MEDIADB288.html"
BASE = "https://mediadb.systemsbiology.net/defined_media/media/"
TITLE = "Media: Song cdm"


def capture(raw=None):
    provenance = json.loads(FIXTURE.with_suffix(".provenance.json").read_text())
    raw = FIXTURE.read_text() if raw is None else str(raw)
    return {
        "version": rr.CACHE_VERSION,
        "url": provenance["url"],
        "response_url": provenance["url"],
        "http_status": 200,
        "raw": raw,
        "sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "accessed_at": provenance["accessed_at"],
    }


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def fail(*args, **kwargs):
        pytest.fail("Unexpected network access in offline MediaDB reference tests")

    monkeypatch.setattr(requests.Session, "get", fail)


@pytest.fixture
def config(tmp_path):
    return ReferenceValidationConfig(cache_dir=tmp_path, rate_limit_delay=0)


def seeded(config, value=None):
    value = capture() if value is None else value
    source = rr.recipe_source(value["url"])
    cache = rr.RecipeSourceCache(config)
    cache.directory.mkdir(parents=True, exist_ok=True)
    cache.path(source).write_text(json.dumps(value))
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    return validator, source


@pytest.mark.parametrize(
    "quote",
    [
        "Compound Amount (mM)",
        "Ammonium sulfate 15.1",
        "Calcium chloride anhydrous 0.205",
        "Calcium pantothenate None",
        "L-Cysteine None",
        "L-Methionine None",
        "Magnesium chloride 0.984",
        "Molybdic acid ammonium salt tetrahydrate 0.000405",
        "Sodium chloride 17.1",
        "dTMP None",
    ],
)
def test_source_rows_and_original_failed_quote(config, quote):
    assert not rr.literal_match(quote, capture()["raw"])
    validator, source = seeded(config)
    result = validator.validate(quote, "url:" + source.url, expected_title=TITLE, path="evidence")
    assert result.is_valid, result.message
    assert result.path == "evidence" and result.match_result.similarity_score == 1.0
    assert validator.validate_title(source.url, TITLE).is_valid
    assert not validator.validate_title(source.url, "Media: Another medium").is_valid
    validator.fallback.validate.assert_not_called()
    validator.fallback.validate_title.assert_not_called()


@pytest.mark.parametrize("accession", ["1", "288", "474"])
def test_source_urls(accession):
    source = rr.recipe_source(BASE + accession + "/")
    assert source.provider == "mediadb" and source.accession == accession


@pytest.mark.parametrize(
    "url",
    [
        BASE,
        BASE + "0/",
        BASE + "0288/",
        BASE + "-1/",
        BASE + "288a/",
        BASE + "288",
        BASE + "288//",
        BASE + "288/extra",
        BASE + "288/?",
        BASE + "288/?format=html",
        BASE + "288/#",
        BASE + "288/#table",
        BASE + "288\n/",
        BASE + "%32%38%38/",
        BASE.replace("https:", "http:") + "288/",
        BASE.replace(".net/", ".net:443/") + "288/",
        BASE.replace(".net/", ".net.evil.invalid/") + "288/",
        BASE.replace("//mediadb", "//user:pass@mediadb") + "288/",
        BASE.replace("/media/", "/media_text/") + "288/",
    ],
)
def test_out_of_scope_urls(url):
    assert rr.recipe_source(url) is None


@pytest.mark.parametrize(
    "mutation,error",
    [
        ("wrong_id", "source_identity"),
        ("duplicate_self", "source_identity"),
        ("missing_self", "source_identity"),
        ("self_label", "source_identity"),
        ("self_outside", "source_identity"),
        ("wrong_title", "source_identity"),
        ("empty_name", "source_metadata"),
        ("duplicate_title", "source_metadata"),
        ("missing_title", "source_metadata"),
        ("missing_section", "source_format"),
        ("duplicate_section", "source_format"),
        ("heading_outside", "source_identity"),
        ("missing_heading", "source_format"),
        ("duplicate_heading", "source_format"),
        ("missing_table", "source_format"),
        ("duplicate_table", "source_format"),
        ("nested_table", "source_format"),
        ("table_outside", "source_format"),
        ("missing_count", "source_format"),
        ("wrong_count", "source_format"),
        ("header_unit", "source_format"),
        ("header_case", "source_format"),
        ("header_td", "source_format"),
        ("extra_header", "source_format"),
        ("row_th", "source_format"),
        ("rowspan", "source_format"),
        ("colspan", "source_format"),
        ("orphan_cell", "source_format"),
        ("empty_table", "source_format"),
        ("extra_cell", "source_format"),
        ("missing_cell", "source_format"),
        ("missing_row", "source_format"),
        ("duplicate_compound_id", "source_identity"),
        ("duplicate_compound_name", "source_identity"),
        ("compound_link", "source_identity"),
        ("missing_compound_link", "source_identity"),
        ("extra_compound_link", "source_identity"),
        ("empty_compound", "source_identity"),
        ("compound_extra_text", "source_identity"),
        ("amount_link", "source_identity"),
        ("nan_amount", "source_format"),
        ("empty_amount", "source_format"),
        ("range_amount", "source_format"),
        ("comma_amount", "source_format"),
        ("embedded_script", "source_format"),
        ("challenge", "source_metadata"),
    ],
)
def test_semantic_mutations_fail_closed(config, mutation, error):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    section, table, link = soup.find(id="contentcol"), soup.table, soup.find("a")
    row = table.find_all("tr")[1]
    name, amount = row.find_all("td")
    if mutation == "wrong_id":
        link["href"] = "/defined_media/media_text/289/"
    elif mutation == "duplicate_self":
        link.insert_after(copy.copy(link))
    elif mutation == "missing_self":
        link.decompose()
    elif mutation == "self_label":
        link.string = "Other media"
    elif mutation == "self_outside":
        section.insert_after(link.extract())
    elif mutation == "wrong_title":
        soup.title.string = "Media: Another medium"
    elif mutation == "empty_name":
        soup.title.string = "Media: "
    elif mutation == "duplicate_title":
        soup.title.insert_after(copy.copy(soup.title))
    elif mutation == "missing_title":
        soup.title.decompose()
    elif mutation == "missing_section":
        section.unwrap()
    elif mutation == "duplicate_section":
        section.insert_after(soup.new_tag("div", id="contentcol"))
    elif mutation == "heading_outside":
        section.insert_after(soup.h2.extract())
    elif mutation == "missing_heading":
        soup.h2.decompose()
    elif mutation == "duplicate_heading":
        soup.h2.insert_after(copy.copy(soup.h2))
    elif mutation == "missing_table":
        table.decompose()
    elif mutation == "duplicate_table":
        table.insert_after(copy.copy(table))
    elif mutation == "nested_table":
        amount.append(soup.new_tag("table"))
    elif mutation == "table_outside":
        section.insert_after(table.extract())
    elif mutation in {"missing_count", "wrong_count"}:
        text = table.parent.find(string=lambda s: s and "17 Compounds:" in s)
        text.replace_with("" if mutation == "missing_count" else "18 Compounds:")
    elif mutation == "header_unit":
        table.find_all("th")[1].string = "Amount (M)"
    elif mutation == "header_case":
        table.find_all("th")[1].string = "Amount (mm)"
    elif mutation == "header_td":
        table.th.name = "td"
    elif mutation == "extra_header":
        table.tr.append(soup.new_tag("th"))
    elif mutation == "row_th":
        name.name = "th"
    elif mutation in {"rowspan", "colspan"}:
        name[mutation] = "2"
    elif mutation == "orphan_cell":
        table.append(soup.new_tag("td"))
    elif mutation == "empty_table":
        table.clear()
    elif mutation == "extra_cell":
        row.append(soup.new_tag("td"))
    elif mutation == "missing_cell":
        amount.decompose()
    elif mutation == "missing_row":
        row.decompose()
    elif mutation == "duplicate_compound_id":
        table.find_all("tr")[2].a["href"] = name.a["href"]
    elif mutation == "duplicate_compound_name":
        table.find_all("tr")[2].a.string = name.a.string
    elif mutation == "compound_link":
        name.a["href"] = "/defined_media/organisms/16401/"
    elif mutation == "missing_compound_link":
        name.a.unwrap()
    elif mutation == "extra_compound_link":
        name.append(copy.copy(name.a))
    elif mutation == "empty_compound":
        name.a.string = ""
    elif mutation == "compound_extra_text":
        name.append(" hydrate")
    elif mutation == "amount_link":
        amount.string.wrap(soup.new_tag("a", href="/defined_media/compounds/16401/"))
    elif mutation.endswith("_amount"):
        amount.string = {
            "nan_amount": "NaN",
            "empty_amount": "",
            "range_amount": "1-2",
            "comma_amount": "15,1",
        }[mutation]
    elif mutation == "embedded_script":
        name.append(soup.new_tag("script"))
    elif mutation == "challenge":
        soup = BeautifulSoup("<p>Verify browser</p>", "html.parser")
    validator, source = seeded(config, capture(soup))
    # Rehash each mutation so these exercise semantic checks, not checksum failure.
    result = validator.validate("Sodium chloride 17.1", source.url)
    assert not result.is_valid and error in result.message, result.message
    assert not validator.validate_title(source.url, TITLE).is_valid
    validator.fallback.validate.assert_not_called()
    validator.fallback.validate_title.assert_not_called()


@pytest.mark.parametrize(
    "attribute,value",
    [
        ("hidden", ""),
        ("aria-hidden", "true"),
        ("style", "display: none"),
        ("style", "visibility: hidden"),
        ("style", "visibility: collapse"),
        ("class", "hidden"),
        ("class", "d-none"),
        ("class", "invisible"),
    ],
)
@pytest.mark.parametrize("location", ["body", "section", "heading", "link", "table", "amount"])
def test_hidden_recipe_rejected(config, attribute, value, location):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    node = {
        "body": soup.body,
        "section": soup.find(id="contentcol"),
        "heading": soup.h2,
        "link": soup.find("a"),
        "table": soup.table,
        "amount": soup.table.find_all("td")[1],
    }[location]
    node[attribute] = value
    validator, source = seeded(config, capture(soup))
    result = validator.validate("Sodium chloride 17.1", source.url)
    assert not result.is_valid and "hidden" in result.message


@pytest.mark.parametrize(
    "quote",
    [
        "Sodium chloride 17",
        "Sodium chloride 17.10",
        "Sodium chloride 17.1 mM",
        "Sodium chloride -17.1",
        "Sodium chloride 17.1 g/L",
        "Sodium Chloride 17.1",
        "Calcium pantothenate 0",
        "Calcium chloride 0.205",
        "Ammonium sulfate 5.1",
        "Molybdic acid ammonium salt 0.000405",
        "dTMP none",
        "L-Methionine NULL",
        "0.205 Calcium pantothenate None",
        "Amount (mM) Ammonium sulfate 15.1",
    ],
)
def test_nonliteral_and_cross_row_quotes_fail(config, quote):
    validator, source = seeded(config)
    assert not validator.validate(quote, source.url).is_valid


@pytest.mark.parametrize("amount", ["0", "0.0", "+0.02", "-0.02", "1.5E-06", ".025"])
def test_zero_precision_and_signs_preserved(config, amount):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    soup.table.find_all("td")[1].string = amount
    validator, source = seeded(config, capture(soup))
    assert validator.validate("Ammonium sulfate " + amount, source.url).is_valid
    assert not validator.validate("Ammonium sulfate None", source.url).is_valid


def test_inline_formula_and_whitespace(config):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    soup.table.a.clear()
    soup.table.a.append(BeautifulSoup("MgSO<sub>4</sub>&middot;7H<sub>2</sub>O", "html.parser"))
    validator, source = seeded(config, capture(soup))
    assert validator.validate("MgSO4\u00b77H2O \n 15.1", source.url).is_valid
    assert not validator.validate("MgSO4\u00b76H2O 15.1", source.url).is_valid


def test_nonrecipe_content_cannot_supply_evidence(config):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    for tag in ("p", "script", "style", "noscript", "template"):
        extra = soup.new_tag(tag)
        extra.string = "Invented ingredient 999 g/L"
        soup.find(id="contentcol").append(extra)
    validator, source = seeded(config, capture(soup))
    assert validator.validate("Sodium chloride 17.1", source.url).is_valid
    assert not validator.validate("Invented ingredient 999 g/L", source.url).is_valid


@pytest.mark.parametrize(
    "wrapper",
    [
        "template",
        "noscript",
        "script",
        "style",
        "head",
        "iframe",
        "object",
        "canvas",
        "details",
        "dialog",
    ],
)
@pytest.mark.parametrize("location", ["section", "heading", "table"])
def test_inert_or_fallback_ancestors_cannot_supply_evidence(config, wrapper, location):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    node = {"section": soup.find(id="contentcol"), "heading": soup.h2, "table": soup.table}[
        location
    ]
    node.wrap(soup.new_tag(wrapper))
    validator, source = seeded(config, capture(soup))
    result = validator.validate("Sodium chloride 17.1", source.url)
    assert not result.is_valid, result.message
    validator.fallback.validate.assert_not_called()


@pytest.mark.parametrize(
    "tag", ["iframe", "object", "svg", "math", "textarea", "select", "canvas", "img"]
)
def test_nontext_table_markup_is_rejected(config, tag):
    soup = BeautifulSoup(capture()["raw"], "html.parser")
    amount = soup.table.find_all("td")[1]
    amount.string.wrap(soup.new_tag(tag))
    validator, source = seeded(config, capture(soup))
    assert not validator.validate("Ammonium sulfate 15.1", source.url).is_valid


@pytest.mark.parametrize("field", ["sha256", "url", "response_url", "version", "http_status"])
def test_corrupt_cache_fails_without_fallback(config, field):
    value = capture()
    # Keep the lookup URL valid, but change the on-disk metadata after seeding.
    validator, source = seeded(config, value)
    value[field] = "invalid"
    validator.cache.path(source).write_text(json.dumps(value))
    result = validator.validate("Sodium chloride 17.1", source.url)
    assert not result.is_valid and "source_cache" in result.message
    validator.fallback.validate.assert_not_called()


@pytest.mark.parametrize("status,url", [(302, None), (403, None), (200, "https://example.org/")])
def test_access_failure_not_cached_or_delegated(config, status, url):
    value = capture()
    response = Mock(status_code=status, url=url or value["url"])
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    session = Mock()
    session.get.return_value = response
    cache = rr.RecipeSourceCache(config, session=session)
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    result = validator.validate("Sodium chloride 17.1", value["url"])
    assert not result.is_valid and "source_access" in result.message
    assert not cache.path(rr.recipe_source(value["url"])).exists()
    validator.fallback.validate.assert_not_called()


def test_literature_and_sql_export_still_use_upstream(config):
    validator = rr.RecipeTextValidator(config)
    validator.fallback = Mock()
    for reference in (
        "doi:10.4148/1941-4765.1175",
        "https://mediadb.systemsbiology.net/static/defined_media/downloads/media_database.07Oct2015.sql.gz",
    ):
        assert rr.recipe_source(reference) is None
        validator.validate("A quote", reference)
        validator.fallback.validate.assert_called_with(
            "A quote", reference, expected_title=None, path=None
        )
