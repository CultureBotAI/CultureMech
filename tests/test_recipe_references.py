"""Literal source checks must preserve scientific notation and source identity."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from unittest.mock import Mock

import pytest
import requests
from linkml_reference_validator.models import ReferenceValidationConfig, ValidationResult
from validate_recipe_references import main, validate_data

from culturemech.validation import recipe_references as rr
from culturemech.validation.write_validated import DEFAULT_SCHEMA_PATH

FIXTURES = Path(__file__).parent / "fixtures" / "recipe_references"


def capture(name="JCM1084"):
    return json.loads((FIXTURES / f"{name}.json").read_text())


@pytest.fixture(autouse=True)
def no_network(monkeypatch):
    def fail(*args, **kwargs):
        pytest.fail("Unexpected network access in offline recipe-reference tests")

    monkeypatch.setattr(requests.Session, "get", fail)


@pytest.fixture
def config(tmp_path):
    return ReferenceValidationConfig(cache_dir=tmp_path, rate_limit_delay=0)


def seed(config, name="JCM1084"):
    value = capture(name)
    cache = rr.RecipeSourceCache(config)
    source = rr.recipe_source(value["url"])
    cache.directory.mkdir(parents=True, exist_ok=True)
    cache.path(source).write_text(json.dumps(value))
    return cache, source


@pytest.mark.parametrize(
    "name,title,quote",
    [
        ("M1124", "Acetomicrobium Faecale Medium", "[M190]"),
        ("JCM1084", "Medium data", "NaWO4\u00b72H2O 0.4 mg"),
        ("JCM1282", "Medium data", "8% (w/v)"),
        ("J151", "PYROCOCCUS MEDIUM", '"id": "J151"'),
        ("solution118", "Main sol. 73", '"compound": "Casamino acids"'),
    ],
)
def test_real_captures(config, name, title, quote):
    cache, source = seed(config, name)
    value = capture(name)
    assert hashlib.sha256(value["raw"].encode()).hexdigest() == value["sha256"]
    validator = rr.RecipeTextValidator(config, cache=cache)
    result = validator.validate(quote, "url:" + source.url, expected_title=title)
    assert result.is_valid, result.message
    assert validator.validate_title(source.url, title).is_valid
    assert len(validator.results) == 2
    assert cache.memory[source.url].metadata["sha256"] == value["sha256"]


@pytest.mark.parametrize(
    "quote,text,expected",
    [
        ("NaCl 0.1 g", "NaCl\n 0.1\t g", True),
        ("1 g", "0.1 g", False),
        ("1 g", "11 g", False),
        ("1 g", "-1 g", False),
        ("1 g", "\u22121 g", False),
        ("1 g", "\u00b11 g", False),
        ("1 g", "0,1 g", False),
        ("1", "1,5", False),
        ("1 g", "1 g\u207b\u00b9", False),
        ("1 g", "+1 g", False),
        ("1 g", "1 g/L", False),
        ("NaCl 0.1 g", "NaCl 0.1 mg", False),
        ("NaCl 0.1 g", "NaCl 0.01 g", False),
        ("[M190]", "[M191]", False),
        ("[M190]", "M190", False),
        ("[M190]", "See [M190] here", True),
        ("CoCl2", "COCl2", False),
        ("FeSO4", "FeSO4\u00b77H2O", False),
        ("FeSO4\u00b77H2O", "FeSO4\u00b76H2O", False),
        ("NaCl ... 1 g", "NaCl anything 1 g", False),
        ("NaCl [editorial] 1 g", "NaCl 1 g", False),
        ("NaCl 1 g", "NaCl 1\u00a0g", True),
        ("", "Anything", False),
        (" \t", "Anything", False),
        ("1 g", "11 g then 1 g", True),
    ],
)
def test_literal_matching(quote, text, expected):
    assert rr.literal_match(quote, text) is expected


def test_html_rendering_is_not_chemical_normalization():
    text, title = rr.html_recipe_text(
        "<title>Recipe title</title><script>FAKE AMOUNT 99 g</script>"
        "<style>FAKE STYLE</style><table><tr><td>FeSO<sub>4</sub>"
        "&#183;7H<sub>2</sub>O</td><td>0.1</td><td>g</td></tr></table>"
        "<p>Next<br>line</p>"
    )
    assert title == "Recipe title"
    assert "FeSO4\u00b77H2O 0.1 g" in text
    assert "FAKE" not in text
    assert "Next line" in text


@pytest.mark.parametrize(
    "url",
    [
        "https://example.org/recipe",
        "doi:10.1234/example",
        "PMID:1234",
        "https://togomedium.org.evil.invalid/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1",
        "https://user:pass@mediadive.dsmz.de/rest/medium/1",
        "https://mediadive.dsmz.de/rest/medium/1/extra",
        "https://[broken",
        "https://mediadive.dsmz.de/rest/medium/1#other",
        "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1&gm_id=M2",
    ],
)
def test_adapter_scope_is_explicit(url):
    assert rr.recipe_source(url) is None


@pytest.mark.parametrize("name", ["M1124", "J151", "solution118"])
@pytest.mark.parametrize("raw", ["<html>error</html>", "null", "[]", "{}", '{"meta": []}'])
def test_malformed_json_fails_closed(name, raw):
    source = rr.recipe_source(capture(name)["url"])
    with pytest.raises(rr.RecipeReferenceError, match="source_format"):
        rr.parse_recipe(source, raw, {})


@pytest.mark.parametrize("name", ["M1124", "JCM1084", "J151", "solution118"])
def test_wrong_accession_is_rejected(name):
    value = capture(name)
    source = rr.recipe_source(value["url"])
    wrong = rr.RecipeSource(source.url, source.provider, "999999")
    with pytest.raises(rr.RecipeReferenceError, match="source_identity"):
        rr.parse_recipe(wrong, value["raw"], {})


@pytest.mark.parametrize("name", ["M1124", "J151", "solution118"])
def test_empty_recipe_not_treated_as_a_valid_source(name):
    value = capture(name)
    body = json.loads(value["raw"])
    if name == "M1124":
        body["components"] = []
    elif name == "J151":
        body["data"]["solutions"] = []
    else:
        body["data"]["recipe"] = []
    with pytest.raises(rr.RecipeReferenceError, match="source_unavailable"):
        rr.parse_recipe(rr.recipe_source(value["url"]), json.dumps(body), {})


def test_jcm_no_result_and_mediadive_api_error():
    source = rr.recipe_source(capture()["url"])
    with pytest.raises(rr.RecipeReferenceError, match="source_unavailable"):
        rr.parse_recipe(
            source,
            "<title>Medium data</title>" "Search for medium no. = [1084]. Nothing found.",
            {},
        )
    source = rr.recipe_source(capture("J151")["url"])
    with pytest.raises(rr.RecipeReferenceError, match="source_unavailable"):
        rr.parse_recipe(source, '{"status": 404}', {})


@pytest.mark.parametrize(
    "field,value",
    [
        ("version", 0),
        ("url", "https://example.org"),
        ("sha256", "bad"),
        ("response_url", "https://example.org"),
        ("http_status", 302),
        ("accessed_at", "not a date"),
        ("raw", None),
        ("raw", "tampered"),
    ],
)
def test_corrupt_cache_is_an_error_not_a_generic_fallback(config, field, value):
    cache, source = seed(config)
    entry = capture()
    entry[field] = value
    cache.path(source).write_text(json.dumps(entry))
    validator = rr.RecipeTextValidator(config, cache=cache)
    validator.fallback = Mock()
    result = validator.validate("NaCl 0.5 g", source.url)
    assert not result.is_valid and "source_cache" in result.message
    validator.fallback.validate.assert_not_called()


@pytest.mark.parametrize("refresh", [False, True])
def test_dangling_symlink_is_rejected_before_fetch(config, refresh):
    cache = rr.RecipeSourceCache(config, refresh=refresh)
    source = rr.recipe_source(capture()["url"])
    cache.directory.mkdir(parents=True)
    cache.path(source).symlink_to(config.cache_dir / "absent")
    with pytest.raises(rr.RecipeReferenceError, match="symlink"):
        cache.fetch(source)


def session_for(value, *, status=200, url=None, payload=None):
    response = Mock(status_code=status, url=url or value["url"])
    response.iter_content.return_value = [payload if payload is not None else value["raw"].encode()]
    response.__enter__ = Mock(return_value=response)
    response.__exit__ = Mock(return_value=False)
    session = Mock()
    session.get.return_value = response
    return session


def test_fetch_refresh_and_memoization(config):
    value = capture()
    session = session_for(value)
    cache = rr.RecipeSourceCache(config, session=session)
    source = rr.recipe_source(value["url"])
    first = cache.fetch(source)
    assert cache.fetch(source) is first
    session.get.assert_called_once()
    assert session.get.call_args.kwargs["allow_redirects"] is False
    stored = json.loads(cache.path(source).read_text())
    assert stored["sha256"] == value["sha256"]
    assert not list(cache.directory.glob(".capture-*"))
    assert rr.RecipeSourceCache(config).fetch(source).content == first.content
    cache.path(source).write_text("broken cache")
    assert (
        rr.RecipeSourceCache(config, session=session, refresh=True).fetch(source).content
        == first.content
    )
    assert session.get.call_count == 2


@pytest.mark.parametrize(
    "options,error",
    [
        ({"status": 302}, "source_access"),
        ({"url": "https://example.org/redirect"}, "source_access"),
        ({"payload": b"\xff"}, "source_access"),
        ({"payload": b"<html>Maintenance</html>"}, "source_identity"),
        ({"payload": b"x" * (rr.MAX_RESPONSE_BYTES + 1)}, "source_format"),
    ],
)
def test_bad_http_responses_are_not_cached(config, options, error):
    value = capture()
    session = session_for(value, **options)
    cache = rr.RecipeSourceCache(config, session=session)
    source = rr.recipe_source(value["url"])
    for _ in range(2):
        with pytest.raises(rr.RecipeReferenceError, match=error):
            cache.fetch(source)
    session.get.assert_called_once()
    assert not cache.path(source).exists()


def test_network_error_is_memoized(config):
    session = Mock()
    session.get.side_effect = requests.Timeout("offline")
    cache = rr.RecipeSourceCache(config, session=session)
    source = rr.recipe_source(capture()["url"])
    for _ in range(2):
        with pytest.raises(rr.RecipeReferenceError, match="source_access"):
            cache.fetch(source)
    session.get.assert_called_once()


def test_nonofficial_sources_delegate_without_modification(config):
    validator = rr.RecipeTextValidator(config)
    validator.fallback = Mock()
    passed = ValidationResult(is_valid=True, reference_id="PMID:123", supporting_text="[quote]")
    validator.fallback.validate.return_value = passed
    validator.fallback.validate_title.return_value = passed
    assert validator.validate("[quote]", "PMID:123", expected_title="Title", path="e[0]") is passed
    validator.fallback.validate.assert_called_once_with(
        "[quote]", "PMID:123", expected_title="Title", path="e[0]"
    )
    assert validator.validate_title("doi:10.123/a", "Title", path="r[0]") is passed
    validator.fallback.validate_title.assert_called_once_with("doi:10.123/a", "Title", path="r[0]")


def test_official_quotes_cannot_be_waived_by_skip_prefixes(config):
    config.skip_prefixes = ["url"]
    cache, source = seed(config)
    validator = rr.RecipeTextValidator(config, cache=cache)
    assert not validator.validate("invented 999 g", "url:" + source.url).is_valid
    assert not validator.validate_title(source.url, "").is_valid


@pytest.mark.parametrize("name", ["M1124", "J151", "solution118"])
def test_missing_official_title_is_not_a_url_fallback(name):
    value = capture(name)
    body = json.loads(value["raw"])
    identity = (
        body["meta"]
        if name == "M1124"
        else body["data"]["medium"] if name == "J151" else body["data"]
    )
    identity["name"] = ""
    with pytest.raises(rr.RecipeReferenceError, match="source_metadata"):
        rr.parse_recipe(rr.recipe_source(value["url"]), json.dumps(body), {})


def evidence(quote="NaWO4\u00b72H2O 0.4 mg"):
    return {
        "reference": capture()["url"],
        "snippet": quote,
        "supports": "SUPPORT",
        "explanation": "Literal occurrence test only",
    }


def test_schema_plugin_checks_nested_evidence_and_titles(config):
    cache, _ = seed(config)
    validator = rr.RecipeTextValidator(config, cache=cache)
    item = {"preferred_term": "salt", "evidence": [evidence()]}
    medium = {
        "name": "test recipe",
        "evidence": [evidence()],
        "ingredients": [item],
        "solutions": [
            {
                "composition": [copy.deepcopy(item)],
                "solutions": [{"composition": [copy.deepcopy(item)]}],
            }
        ],
        "variants": [{"name": "variant", "evidence": [evidence()]}],
        "references": [{"reference": capture()["url"], "title": "Medium data"}],
    }
    solution = {"term": {"id": "mediadive.solution:1"}, "composition": [item]}
    issues = validate_data([medium, solution], DEFAULT_SCHEMA_PATH, validator)
    assert not issues, issues
    assert len(validator.results) == 7
    assert {r.path for r in validator.results} >= {
        "solutions[0].solutions[0].composition[0].evidence[0].snippet",
        "variants[0].evidence[0].snippet",
        "references[0].title",
        "composition[0].evidence[0].snippet",
    }
    bad = copy.deepcopy(medium)
    bad["ingredients"][0]["evidence"][0]["snippet"] = "NaWO4\u00b72H2O 0.04 mg"
    issues = validate_data(bad, DEFAULT_SCHEMA_PATH, validator)
    assert len(issues) == 1 and "snippet_mismatch" in issues[0].message


@pytest.mark.parametrize("data", [None, [], "not a recipe", [1]])
def test_bad_input_shape(config, data):
    with pytest.raises(ValueError, match="mapping"):
        validate_data(data, DEFAULT_SCHEMA_PATH, rr.RecipeTextValidator(config))


def test_unknown_class_is_not_an_empty_success(config):
    with pytest.raises(ValueError, match="Unknown target class"):
        validate_data({}, DEFAULT_SCHEMA_PATH, rr.RecipeTextValidator(config), "Typo")


@pytest.mark.parametrize("title,expected", [("Medium data", 0), ("Invented title", 1)])
def test_cli_reports_actual_checks_and_failures(config, tmp_path, capsys, title, expected):
    seed(config)
    path = tmp_path / "input.yaml"
    path.write_text(
        json.dumps(
            {
                "evidence": [evidence()],
                "references": [{"reference": capture()["url"], "title": title}],
            }
        )
    )
    assert main([str(path), "--cache-dir", str(config.cache_dir), "--json"]) == expected
    result = json.loads(capsys.readouterr().out)
    assert len(result["checks"]) == 2
    assert result["valid"] is (expected == 0)
    assert len(result["issues"]) == expected


def test_cli_invalid_yaml_is_nonzero(tmp_path, capsys):
    path = tmp_path / "bad.yaml"
    path.write_text("a: [unterminated")
    assert main([str(path), "--cache-dir", str(tmp_path)]) == 2
    assert "[ERROR] reference_validation" in capsys.readouterr().err


def test_validator_entry_points_use_recipe_adapter(monkeypatch):
    import validate_strict

    run = Mock(return_value=[])
    monkeypatch.setattr(validate_strict, "_run_external_validator", run)
    validate_strict.validate_references(Path("input.yaml"), "SolutionRecipe")
    command = run.call_args.args[0]
    assert command[:3] == ["uv", "run", "python"]
    assert Path(command[3]).name == "validate_recipe_references.py"
    assert command[-2:] == ["--target-class", "SolutionRecipe"]
    justfile = (Path(__file__).parents[1] / "project.justfile").read_text()
    for name in ("validate file:", "validate-references file:"):
        body = justfile.split(name, 1)[1].split("[group(", 1)[0]
        assert "scripts/validate_recipe_references.py" in body
