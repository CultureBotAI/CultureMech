"""Tests for scripts/fulltext_access.py in CultureMech."""

from __future__ import annotations

import sqlite3
import sys
from contextlib import closing
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import fulltext_access  # noqa: E402


def test_no_email_disclosure_in_fulltext_access() -> None:
    """External API scripts must call CrossRef, OpenAlex, and Europe PMC anonymously."""
    source = (SCRIPTS_DIR / "fulltext_access.py").read_text(encoding="utf-8")
    assert "mailto:" not in source
    assert "@gmail.com" not in source
    assert "@lbl.gov" not in source
    ua = fulltext_access.UA.get("User-Agent", "")
    assert "@" not in ua
    assert "mailto" not in ua.lower()


def test_try_zotero_local_resolves_pdf_by_doi_and_pmid(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    zotero_dir = tmp_path / "Zotero"
    storage_dir = zotero_dir / "storage" / "ABCD1234"
    storage_dir.mkdir(parents=True)
    pdf_file = storage_dir / "paper.pdf"
    pdf_file.write_bytes(b"%PDF-1.4\n%test\n")

    db_path = zotero_dir / "zotero.sqlite"
    with closing(sqlite3.connect(db_path)) as conn:
        conn.executescript("""
            CREATE TABLE fields (fieldID INTEGER PRIMARY KEY, fieldName TEXT);
            CREATE TABLE itemDataValues (valueID INTEGER PRIMARY KEY, value TEXT);
            CREATE TABLE itemData (itemID INTEGER, fieldID INTEGER, valueID INTEGER);
            CREATE TABLE items (itemID INTEGER PRIMARY KEY, key TEXT);
            CREATE TABLE itemAttachments (
                itemID INTEGER PRIMARY KEY,
                parentItemID INTEGER,
                contentType TEXT,
                path TEXT
            );
            INSERT INTO fields VALUES (1, 'DOI'), (2, 'extra');
            INSERT INTO itemDataValues VALUES
                (10, '10.1038/s41564-024-01234-5'),
                (11, 'PMID: 38999999');
            INSERT INTO items VALUES (100, 'PARENT01'), (101, 'ABCD1234');
            INSERT INTO itemData VALUES (100, 1, 10), (100, 2, 11);
            INSERT INTO itemAttachments VALUES
                (101, 100, 'application/pdf', 'storage:paper.pdf');
            """)

    monkeypatch.setenv("ZOTERO_DATA_DIR", str(zotero_dir))

    hit_by_doi = fulltext_access.try_zotero_local(doi="https://doi.org/10.1038/s41564-024-01234-5")
    assert hit_by_doi == f"file://{pdf_file.resolve()}"

    hit_by_pmid = fulltext_access.try_zotero_local(pmid="38999999")
    assert hit_by_pmid == f"file://{pdf_file.resolve()}"

    miss = fulltext_access.try_zotero_local(doi="10.1038/nonexistent")
    assert miss is None

    monkeypatch.delenv("ZOTERO_DATA_DIR", raising=False)
    assert fulltext_access.try_zotero_local(doi="10.1038/s41564-024-01234-5") is None


def test_try_openalex_oa_rejects_doi_resolver_and_picks_real_oa_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured_urls: list[str] = []

    def fake_get_json(url: str, headers: dict | None = None):
        captured_urls.append(url)
        return {
            "open_access": {"is_oa": True, "oa_url": "https://doi.org/10.1016/j.biortech.2026.1"},
            "best_oa_location": {
                "is_oa": True,
                "url": "https://doi.org/10.1016/j.biortech.2026.1",
                "pdf_url": None,
            },
            "locations": [
                {
                    "is_oa": True,
                    "landing_page_url": "https://doi.org/10.1016/j.biortech.2026.1",
                    "pdf_url": None,
                },
                {
                    "is_oa": True,
                    "landing_page_url": "https://escholarship.org/uc/item/12345",
                    "pdf_url": "https://escholarship.org/content/qt12345/qt12345.pdf",
                },
            ],
        }

    monkeypatch.setattr(fulltext_access, "_get_json", fake_get_json)
    hit = fulltext_access.try_openalex_oa("10.1016/j.biortech.2026.1")
    assert hit == "https://escholarship.org/content/qt12345/qt12345.pdf"
    assert captured_urls and "mailto" not in captured_urls[0]


def test_try_osti_extracts_fulltext_href(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        fulltext_access,
        "_get_json",
        lambda url, headers=None: [
            {
                "osti_id": "1999999",
                "links": [
                    {"rel": "citation", "href": "https://www.osti.gov/biblio/1999999"},
                    {"rel": "fulltext", "href": "https://www.osti.gov/servlets/purl/1999999"},
                ],
            }
        ],
    )
    assert (
        fulltext_access.try_osti("10.2172/1999999") == "https://www.osti.gov/servlets/purl/1999999"
    )


def test_try_springer_tdm_does_not_leak_api_key_in_returned_url(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("SPRINGER_API_KEY", "secret-springer-key-123")
    probed: list[str] = []

    def fake_prefix(url: str, headers: dict | None = None, max_bytes: int = 32768) -> str:
        probed.append(url)
        return "<article><body><sec><title>Methods</title></sec></body></article>"

    monkeypatch.setattr(fulltext_access, "_get_text_prefix", fake_prefix)
    url = fulltext_access.try_springer_tdm("10.1038/s41586-024-00001-1")
    assert url is not None
    assert "secret-springer-key-123" not in url
    assert "api_key" not in url
    assert probed and "secret-springer-key-123" in probed[0]


def test_try_elsevier_tdm_requires_body_elements(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ELSEVIER_API_KEY", "secret-elsevier-key")

    meta_xml = "<full-text-retrieval-response><coredata/></full-text-retrieval-response>"
    monkeypatch.setattr(
        fulltext_access,
        "_get_text_prefix",
        lambda url, headers=None, max_bytes=32768: meta_xml,
    )
    assert fulltext_access.try_elsevier_tdm("10.1016/j.biortech.2026.134417") is None

    body_xml = (
        "<full-text-retrieval-response><originalText>"
        "<ce:sections>...</ce:sections></originalText>"
        "</full-text-retrieval-response>"
    )
    monkeypatch.setattr(
        fulltext_access,
        "_get_text_prefix",
        lambda url, headers=None, max_bytes=32768: body_xml,
    )
    hit = fulltext_access.try_elsevier_tdm("10.1016/j.biortech.2026.134417")
    expected_url = (
        "https://api.elsevier.com/content/article/doi/"
        "10.1016/j.biortech.2026.134417?httpAccept=text/xml"
    )
    assert hit == expected_url


def test_access_ladder_stops_at_first_hit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(fulltext_access, "try_zotero_local", lambda pmid, doi: None)
    monkeypatch.setattr(fulltext_access, "try_europepmc", lambda rec: None)
    monkeypatch.setattr(
        fulltext_access,
        "try_openalex_oa",
        lambda doi, pmid=None: "https://zenodo.org/record/1/files/paper.pdf",
    )
    method, url = fulltext_access.access_ladder(
        {"pmid": "12345"}, "10.5281/zenodo.1", "Test Paper", pmid="12345"
    )
    assert method == "openalex_oa"
    assert url == "https://zenodo.org/record/1/files/paper.pdf"


def test_fetch_to_staging_rejects_references_cache(tmp_path: Path) -> None:
    bad_dest = tmp_path / "references_cache" / "PMID_12345.xml"
    with pytest.raises(ValueError, match="references_cache"):
        fulltext_access.fetch_to_staging(
            "elsevier_tdm",
            "https://api.elsevier.com/content/article/doi/10.1016/j.biortech.2026.1?httpAccept=text/xml",
            bad_dest,
        )


def test_fetch_to_staging_attaches_tdm_headers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("ELSEVIER_API_KEY", "els-key-999")
    monkeypatch.setenv("WILEY_TDM_TOKEN", "wiley-tok-888")
    captured_headers: list[dict] = []

    class DummyResp:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

        def read(self) -> bytes:
            return (
                b"<full-text-retrieval-response><body>Methods</body></full-text-retrieval-response>"
            )

    def fake_urlopen(req, timeout=60):
        captured_headers.append(dict(req.header_items()))
        return DummyResp()

    monkeypatch.setattr(fulltext_access.urllib.request, "urlopen", fake_urlopen)

    els_out = tmp_path / ".temp" / "elsevier.xml"
    saved = fulltext_access.fetch_to_staging(
        "elsevier_tdm",
        "https://api.elsevier.com/content/article/doi/10.1016/j.biortech.2026.1?httpAccept=text/xml",
        els_out,
    )
    assert saved.is_file()
    assert any(
        k.lower() == "x-els-apikey" and v == "els-key-999" for k, v in captured_headers[-1].items()
    )

    wiley_out = tmp_path / ".temp" / "wiley.pdf"
    fulltext_access.fetch_to_staging(
        "wiley_tdm",
        "https://api.wiley.com/onlinelibrary/tdm/v1/articles/10.1002%2Fbit.1",
        wiley_out,
    )
    assert any(
        k.lower() == "wiley-tdm-client-token" and v == "wiley-tok-888"
        for k, v in captured_headers[-1].items()
    )


def test_try_acs_figshare_si_resolves_handle(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_get_json(url: str, headers: dict | None = None):
        if "doi.org/api/handles/10.1021/acssynbio.5b00123.s001" in url:
            return {
                "responseCode": 1,
                "values": [
                    {
                        "type": "URL",
                        "data": {
                            "value": (
                                "https://figshare.com/articles/journal_contribution/"
                                "Supporting_Information/12345678"
                            )
                        },
                    }
                ],
            }
        if "api.figshare.com/v2/articles/12345678" in url:
            return {
                "files": [
                    {
                        "name": "sb5b00123_si_002.xlsx",
                        "download_url": "https://ndownloader.figshare.com/files/99999998",
                    },
                    {
                        "name": "sb5b00123_si_001.pdf",
                        "download_url": "https://ndownloader.figshare.com/files/99999999",
                    },
                ]
            }
        return {}

    monkeypatch.setattr(fulltext_access, "_get_json", fake_get_json)
    assert fulltext_access.try_acs_figshare_si("10.1038/s41586-024-00001-1") is None
    assert (
        fulltext_access.try_acs_figshare_si("https://doi.org/10.1021/acssynbio.5b00123")
        == "https://ndownloader.figshare.com/files/99999999"
    )
    assert (
        fulltext_access.try_acs_figshare_si("10.1021/acssynbio.5b00123.s001")
        == "https://ndownloader.figshare.com/files/99999999"
    )

