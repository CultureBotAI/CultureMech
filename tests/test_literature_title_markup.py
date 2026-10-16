"""Inline publisher formatting is not a different bibliographic title."""

from unittest.mock import Mock

import pytest
from linkml_reference_validator.models import ReferenceContent, ReferenceValidationConfig

from culturemech.validation.recipe_references import RecipeTextValidator


def validator_with_title(tmp_path, title):
    validator = RecipeTextValidator(ReferenceValidationConfig(cache_dir=tmp_path))
    validator.fallback.fetcher.fetch = Mock(return_value=ReferenceContent(
        reference_id="doi:10.1234/example", title=title, content="A literal abstract."
    ))
    return validator


@pytest.mark.parametrize("actual,expected", [
    ("A study of <i>Escherichia coli</i>", "A study of Escherichia coli"),
    ("Growth of\n <i>Escherichia coli</i>\n O157:H7", "Growth of Escherichia coli O157:H7"),
    ("Media for<i>Bacteroides</i>", "Media forBacteroides"),
    ("FeSO<sub>4</sub> &amp; MgSO<sub>4</sub>", "FeSO4 & MgSO4"),
    ("<em>Carbon</em> response", "Carbon response"),
    ("<b>Two</b> types", "Two types"),
    ("CO<sub>2</sub> and Ca<sup>2+</sup>", "CO2 and Ca2+"),
    ("A <strong>nested <i>title</i></strong>", "A nested title"),
])
def test_inline_markup_title_equivalence(tmp_path, actual, expected):
    validator = validator_with_title(tmp_path, actual)
    result = validator.validate_title("doi:10.1234/example", expected, path="references[0].title")
    assert result.is_valid, result.message
    assert result.path == "references[0].title"
    assert validator.results == [result]
    assert validator.fallback.fetcher.fetch.return_value.title == actual


@pytest.mark.parametrize("actual,expected", [
    ("<i>Escherichia coli</i> K-12", "Escherichia coli O157:H7"),
    ("<i>Growth</i> in M9", "Growth in M8"),
    ("FeSO<sub>4</sub>", "FeSO3"),
    ("<i>Growth</i> at 90?C", "Growth at 90\u00b0C"),
    ("<i>alpha</i>-amylase", "beta-amylase"),
    ("<script>discarded</script>Real title", "Real title"),
    ("<!-- hidden -->Real title", "Real title"),
    ("<span style='display:none'>hidden</span>Real title", "Real title"),
    ("<i style='display:none'>Real</i> title", "Real title"),
    ("<i></i>", ""),
    ("<!DOCTYPE html>Real title", "Real title"),
    ("<?discarded value?>Real title", "Real title"),
    ("Fe<sup>2+</sup>", "Fe2"),
    ("A<sub>2</sub>B", "A 2 B"),
])
def test_markup_does_not_hide_title_conflicts(tmp_path, actual, expected):
    result = validator_with_title(tmp_path, actual).validate_title("doi:10.1234/example", expected)
    assert not result.is_valid


def test_unavailable_reference_stays_invalid(tmp_path):
    validator = validator_with_title(tmp_path, None)
    validator.fallback.fetcher.fetch.return_value = None
    assert not validator.validate_title("doi:10.1234/example", "Real title").is_valid
    assert validator.fallback.fetcher.fetch.call_count == 1


def test_missing_title_stays_invalid(tmp_path):
    validator = validator_with_title(tmp_path, None)
    assert not validator.validate_title("doi:10.1234/example", "Real title").is_valid
    assert validator.fallback.fetcher.fetch.call_count == 1


def test_skipped_prefix_does_not_fetch(tmp_path):
    validator = validator_with_title(tmp_path, "<i>Real</i> title")
    validator.config.skip_prefixes = ["DOI"]
    assert validator.validate_title("doi:10.1234/example", "Real title").is_valid
    validator.fallback.fetcher.fetch.assert_not_called()


def test_other_prefix_keeps_upstream_failure(tmp_path):
    validator = validator_with_title(tmp_path, "<i>Real</i> title")
    assert not validator.validate_title("PMID:12345", "Real title").is_valid
    assert validator.fallback.fetcher.fetch.call_count == 1


def test_markup_rule_does_not_change_quote_validation(tmp_path):
    validator = validator_with_title(tmp_path, "<i>Real</i> title")
    validator.fallback.validate = Mock()
    result = validator.validate("An invented quote", "doi:10.1234/example", expected_title="Real title")
    assert result is validator.fallback.validate.return_value
    validator.fallback.validate.assert_called_once_with(
        "An invented quote", "doi:10.1234/example", expected_title="Real title", path=None
    )
