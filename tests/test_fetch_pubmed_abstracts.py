"""Raw-source archival must not mistake old Markdown or error XML for evidence."""

import importlib.util
import json
import urllib.parse
from pathlib import Path

import pytest
import yaml

SCRIPT = Path(__file__).parents[1] / "scripts/fetch_pubmed_abstracts.py"
SPEC = importlib.util.spec_from_file_location("pubmed_archive", SCRIPT)
archive = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(archive)


def article(pmid="123", abstract="An exact abstract."):
    return f"""<PubmedArticleSet><PubmedArticle><MedlineCitation>
    <PMID>{pmid}</PMID><Article><ArticleTitle>A <i>test</i> title</ArticleTitle>
    <Journal><Title>Test journal</Title><JournalIssue><PubDate>
    <MedlineDate>1985 Jan-Feb</MedlineDate></PubDate></JournalIssue></Journal>
    <AuthorList><Author><CollectiveName>Study group</CollectiveName></Author></AuthorList>
    <Abstract><AbstractText Label="METHODS">{abstract}</AbstractText></Abstract>
    </Article></MedlineCitation><PubmedData><ArticleIdList>
    <ArticleId IdType="doi">10.1234/example</ArticleId></ArticleIdList>
    <ReferenceList><Reference><ArticleIdList><ArticleId IdType="doi">10.5678/other</ArticleId>
    </ArticleIdList></Reference></ReferenceList></PubmedData>
    </PubmedArticle></PubmedArticleSet>""".encode()


@pytest.fixture
def cache(tmp_path, monkeypatch):
    monkeypatch.setattr(archive, "CACHE_DIR", tmp_path)
    monkeypatch.setattr(archive, "REPO_ROOT", tmp_path)
    monkeypatch.setattr(archive, "fetch_pubmed_xml", lambda pmid, api_key: article(pmid))
    return tmp_path


def test_nested_inventory_includes_bibliography_variants_and_ingredients(tmp_path, monkeypatch):
    monkeypatch.setattr(archive, "REPO_ROOT", tmp_path)
    path = tmp_path / "recipe.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "id": "CultureMech:000001",
                "references": [{"reference": "PMID:123"}],
                "variants": [{"evidence": [{"reference": "PMID:456"}]}],
                "ingredients": [{"evidence": [{"reference": "https://doi.org/10.1234/EXAMPLE"}]}],
            }
        )
    )
    inventory = archive.citation_inventory([path])
    assert set(inventory["references"]) == {"PMID:123", "PMID:456", "doi:10.1234/example"}
    assert inventory["references"]["PMID:456"][0]["field"] == "variants[0].evidence[0].reference"
    assert inventory["records"][0]["citation_review"] == "not_reviewed"


def test_inventory_fails_on_unreadable_yaml(tmp_path, monkeypatch):
    monkeypatch.setattr(archive, "REPO_ROOT", tmp_path)
    path = tmp_path / "invalid.yaml"
    path.write_text("references: [")
    with pytest.raises(yaml.YAMLError):
        archive.citation_inventory([path])


def test_identity_and_mixed_content_are_preserved():
    data = archive.parse_abstract(article(), "123")
    assert data["title"] == "A test title"
    assert data["authors"] == ["Study group"]
    assert data["year"] == "1985"
    assert data["doi"] == "10.1234/example"
    assert data["abstract"] == "**METHODS:** An exact abstract."


@pytest.mark.parametrize(
    "raw",
    [b"<ERROR>invalid id</ERROR>", article("999"), b"<html>challenge</html>", b"broken"],
    ids=["error", "wrong-pmid", "html", "malformed"],
)
def test_invalid_sources_cannot_be_archived(cache, monkeypatch, raw):
    monkeypatch.setattr(archive, "fetch_pubmed_xml", lambda *args: raw)
    assert archive.fetch_one("123", None).startswith("error")
    assert not list(cache.rglob("*.xml"))
    assert not list(cache.rglob("*.md"))


def test_old_markdown_is_preserved_but_not_trusted_as_raw_evidence(cache):
    legacy = cache / "PMID_123.md"
    legacy.write_text("Existing full text must not be overwritten")
    assert archive.fetch_one("123", None) == "fetched"
    raw, md, meta = archive.archive_paths("123")
    assert raw.read_bytes() == article()
    assert "An exact abstract." in md.read_text()
    assert legacy.read_text() == "Existing full text must not be overwritten"
    assert archive.verified_archive("123")["has_abstract"] is True
    before = [p.read_bytes() for p in (raw, md, meta)]
    assert archive.fetch_one("123", None) == "cached"
    assert before == [p.read_bytes() for p in (raw, md, meta)]


def test_corrupt_archive_is_refused_not_overwritten(cache):
    archive.fetch_one("123", None)
    raw, md, _ = archive.archive_paths("123")
    md.write_text("tampered")
    assert archive.fetch_one("123", None) == "error:ValueError"
    assert md.read_text() == "tampered"
    assert raw.read_bytes() == article()


@pytest.mark.parametrize(
    "field,value", [("doi", "10.9999/wrong"), ("has_abstract", False)], ids=["doi", "coverage"]
)
def test_metadata_must_be_derived_from_raw_source(cache, field, value):
    archive.fetch_one("123", None)
    _, _, path = archive.archive_paths("123")
    metadata = json.loads(path.read_text())
    metadata[field] = value
    path.write_text(json.dumps(metadata))
    assert archive.fetch_one("123", None) == "error:ValueError"


def test_empty_labeled_abstract_is_not_content():
    assert archive.parse_abstract(article(abstract=""))["abstract"] == ""


def test_orphan_raw_file_requires_online_confirmation(cache):
    raw, _, metadata = archive.archive_paths("123")
    raw.parent.mkdir(parents=True)
    raw.write_bytes(article(abstract="Unverified replacement content"))
    assert archive.fetch_one("123", None) == "error:ValueError"
    assert not metadata.exists()


def test_interrupted_conversion_can_resume_from_matching_source(cache):
    raw, _, metadata = archive.archive_paths("123")
    raw.parent.mkdir(parents=True)
    raw.write_bytes(article())
    assert archive.fetch_one("123", None) == "fetched"
    assert metadata.is_file()


def test_validator_can_read_title_and_abstract_from_compatibility_cache(cache):
    from linkml_reference_validator.etl.reference_fetcher import ReferenceFetcher
    from linkml_reference_validator.models import ReferenceValidationConfig

    archive.fetch_one("123", None)
    source = ReferenceFetcher(ReferenceValidationConfig(cache_dir=cache)).fetch("PMID:123")
    assert source.title == "A test title"
    assert source.content == "**METHODS:** An exact abstract."
    assert source.content_type == "abstract_only"


def test_only_own_old_compatibility_rendering_is_upgraded(cache):
    archive.fetch_one("123", None)
    raw, markdown, metadata = archive.archive_paths("123")
    before = [p.read_bytes() for p in (raw, markdown, metadata)]
    archive.cache_path("123").write_bytes(markdown.read_bytes())
    assert archive.fetch_one("123", None) == "cached"
    assert archive.cache_path("123").read_text().startswith("---\n")
    assert before == [p.read_bytes() for p in (raw, markdown, metadata)]


def test_no_abstract_is_not_reported_as_completed_source(cache, monkeypatch):
    raw = article().replace(
        b'<Abstract><AbstractText Label="METHODS">An exact abstract.</AbstractText></Abstract>', b""
    )
    monkeypatch.setattr(archive, "fetch_pubmed_xml", lambda *args: raw)
    assert archive.fetch_one("123", None) == "metadata_only"
    assert archive.verified_archive("123")["has_abstract"] is False


def test_limit_applies_to_missing_archives_and_cached_report_is_written(cache, monkeypatch):
    archive.fetch_one("123", None)
    report = cache / "report.json"
    monkeypatch.setattr(
        "sys.argv",
        [str(SCRIPT), "--pmids", "123", "124", "125", "--limit", "1", "--report", str(report)],
    )
    monkeypatch.setattr(archive.time, "sleep", lambda _: None)
    assert archive.main() == 0
    data = json.loads(report.read_text())
    assert data["outcomes"] == {"PMID:123": "cached", "PMID:124": "fetched"}
    assert data["not_attempted"] == ["PMID:125"]


@pytest.mark.parametrize(
    "pmid", ["../outside", "123&api_key=secret", ""], ids=["path", "query", "empty"]
)
def test_invalid_pmid_never_reaches_network(cache, monkeypatch, pmid):
    def unexpected(*args):
        pytest.fail("network called for invalid PMID")

    monkeypatch.setattr(archive, "fetch_pubmed_xml", unexpected)
    assert archive.fetch_one(pmid, None) == "error:invalid PMID"


def test_doi_reuses_verified_identifier_from_existing_xml(cache, monkeypatch):
    archive.fetch_one("123", None)
    monkeypatch.setattr(archive, "fetch_bytes", lambda _: pytest.fail("unnecessary search"))
    result = archive.resolve_doi("https://doi.org/10.1234/EXAMPLE", None, 0)
    assert result["status"] == "archived" and result["pmid"] == "123"
    assert (cache / result["raw"]).is_file()
    assert (cache / result["markdown"]).is_file()


def test_doi_search_must_cross_check_returned_article_doi(cache, monkeypatch):
    monkeypatch.setattr(
        archive,
        "fetch_bytes",
        lambda _: b"<eSearchResult><Count>1</Count><IdList><Id>123</Id></IdList></eSearchResult>",
    )
    result = archive.resolve_doi("doi:10.1234/different", None, 0)
    assert result["status"] == "unresolved_in_pubmed"


@pytest.mark.parametrize(
    "payload,status",
    [
        (b"<eSearchResult><Count>0</Count><IdList/></eSearchResult>", "unresolved_in_pubmed"),
        (
            b"<eSearchResult><Count>20</Count><IdList><Id>123</Id></IdList></eSearchResult>",
            "ambiguous_or_truncated_search",
        ),
        (b"<html>challenge</html>", "resolution_error"),
    ],
    ids=["no-hit", "truncated", "invalid"],
)
def test_doi_search_does_not_report_missing_or_invalid_content_as_archived(
    cache, monkeypatch, payload, status
):
    monkeypatch.setattr(archive, "fetch_bytes", lambda _: payload)
    assert archive.resolve_doi("doi:10.1234/example", None, 0)["status"] == status


def test_same_doi_for_multiple_articles_stays_ambiguous(cache):
    archive.fetch_one("123", None)
    archive.fetch_one("124", None)
    assert archive.resolve_doi("doi:10.1234/example", None, 0)["status"] == "ambiguous_doi"


@pytest.mark.parametrize(
    "invalid",
    [
        b"<html>temporary challenge</html>",
        b"<eSearchResult><ERROR>temporary error</ERROR></eSearchResult>",
        b"<eSearchResult><Count>invalid</Count><IdList/></eSearchResult>",
        b"<eSearchResult><Count>-1</Count><IdList/></eSearchResult>",
        b"<eSearchResult><Count>1</Count><IdList><Id>bad-id</Id></IdList></eSearchResult>",
    ],
)
def test_invalid_doi_search_is_not_persisted_and_retry_recovers(cache, monkeypatch, invalid):
    responses = iter([invalid, b"<eSearchResult><Count>0</Count><IdList/></eSearchResult>"])
    requests = []

    def fetch(url):
        requests.append(url)
        return next(responses)

    monkeypatch.setattr(archive, "fetch_bytes", fetch)
    assert archive.resolve_doi("doi:10.1234/example", None, 0)["status"] == "resolution_error"
    assert not list((cache / "papers/doi_searches").glob("*"))
    assert archive.resolve_doi("doi:10.1234/example", None, 0)["status"] == "unresolved_in_pubmed"
    assert archive.resolve_doi("doi:10.1234/example", None, 0)["status"] == "unresolved_in_pubmed"
    assert len(requests) == 2


def test_keyed_doi_search_uses_key_without_archiving_it(cache, monkeypatch):
    requested = []

    def fetch(url):
        requested.append(urllib.parse.parse_qs(urllib.parse.urlsplit(url).query))
        return b"<eSearchResult><Count>1</Count><IdList><Id>123</Id></IdList></eSearchResult>"

    monkeypatch.setattr(archive, "fetch_bytes", fetch)
    result = archive.resolve_doi("doi:10.1234/example", "synthetic-test-secret", 0)
    assert result["status"] == "archived"
    assert requested[0]["api_key"] == ["synthetic-test-secret"]
    for path in (cache / "papers").rglob("*"):
        if path.is_file():
            assert b"synthetic-test-secret" not in path.read_bytes()


@pytest.mark.parametrize("rate", ["nan", "inf", "0", "-1"])
def test_invalid_rates_fail_before_network(cache, monkeypatch, rate):
    monkeypatch.setattr("sys.argv", [str(SCRIPT), "--pmids", "123", "--rate", rate])
    monkeypatch.setattr(archive, "fetch_one", lambda *args: pytest.fail("unexpected fetch"))
    with pytest.raises(SystemExit) as error:
        archive.main()
    assert error.value.code == 2
