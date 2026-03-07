"""Tests for literature verifier."""

import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile
import os

from culturemech.enrich.literature_verifier import LiteratureVerifier


class TestLiteratureVerifier:
    """Tests for LiteratureVerifier class."""

    def test_scihub_disabled_by_default(self):
        """Test that Sci-Hub fallback is disabled by default."""
        verifier = LiteratureVerifier()
        assert verifier.use_fallback_pdf == False

    def test_scihub_enabled_with_flag(self):
        """Test that Sci-Hub fallback can be enabled explicitly."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)
        assert verifier.use_fallback_pdf == True

    def test_fallback_mirrors_from_env(self):
        """Test that Sci-Hub mirrors can be configured via environment."""
        os.environ["FALLBACK_PDF_MIRRORS"] = "https://mirror1.test,https://mirror2.test"
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        assert len(verifier.fallback_pdf_urls) == 2
        assert "https://mirror1.test" in verifier.fallback_pdf_urls
        assert "https://mirror2.test" in verifier.fallback_pdf_urls

        # Clean up
        del os.environ["FALLBACK_PDF_MIRRORS"]

    def test_normalize_pdf_url_absolute(self):
        """Test normalizing absolute PDF URLs."""
        verifier = LiteratureVerifier()

        # Already absolute
        url = verifier._normalize_pdf_url("https://example.com/paper.pdf", "https://base.com")
        assert url == "https://example.com/paper.pdf"

    def test_normalize_pdf_url_protocol_relative(self):
        """Test normalizing protocol-relative PDF URLs."""
        verifier = LiteratureVerifier()

        url = verifier._normalize_pdf_url("//cdn.example.com/paper.pdf", "https://base.com")
        assert url == "https://cdn.example.com/paper.pdf"

    def test_normalize_pdf_url_relative(self):
        """Test normalizing relative PDF URLs."""
        verifier = LiteratureVerifier()

        url = verifier._normalize_pdf_url("/downloads/paper.pdf", "https://base.com")
        assert url == "https://base.com/downloads/paper.pdf"

    def test_extract_pdf_from_fallback_html_object_tag(self):
        """Test extracting PDF from Sci-Hub HTML using object tag."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        html = '''
        <html>
        <body>
        <object type="application/pdf" data="/download/12345.pdf"></object>
        </body>
        </html>
        '''

        pdf_url = verifier._extract_pdf_from_fallback_html(html, "https://sci-hub.se")
        assert pdf_url == "https://sci-hub.se/download/12345.pdf"

    def test_extract_pdf_from_fallback_html_download_link(self):
        """Test extracting PDF from Sci-Hub HTML using download link."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        html = '''
        <html>
        <body>
        <a href="/dl/paper.pdf">Download PDF</a>
        </body>
        </html>
        '''

        pdf_url = verifier._extract_pdf_from_fallback_html(html, "https://sci-hub.st")
        assert pdf_url == "https://sci-hub.st/dl/paper.pdf"

    def test_extract_pdf_from_fallback_html_embed_tag(self):
        """Test extracting PDF from Sci-Hub HTML using embed tag."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        html = '''
        <html>
        <body>
        <embed src="//cdn.scihub.org/paper123.pdf" type="application/pdf">
        </body>
        </html>
        '''

        pdf_url = verifier._extract_pdf_from_fallback_html(html, "https://sci-hub.ru")
        assert pdf_url == "https://cdn.scihub.org/paper123.pdf"

    def test_extract_pdf_from_fallback_html_direct_url(self):
        """Test extracting PDF from Sci-Hub HTML using direct URL."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        html = '''
        <html>
        <body>
        <p>PDF available at: https://direct.cdn.com/files/paper.pdf</p>
        </body>
        </html>
        '''

        pdf_url = verifier._extract_pdf_from_fallback_html(html, "https://sci-hub.ren")
        assert pdf_url == "https://direct.cdn.com/files/paper.pdf"

    def test_extract_pdf_from_fallback_html_no_match(self):
        """Test that None is returned when no PDF found in HTML."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        html = '''
        <html>
        <body>
        <p>No PDF here</p>
        </body>
        </html>
        '''

        pdf_url = verifier._extract_pdf_from_fallback_html(html, "https://sci-hub.se")
        assert pdf_url is None

    def test_strip_jats_html(self):
        """Test stripping JATS XML tags from CrossRef abstracts."""
        raw = '<jats:title>Abstract</jats:title><jats:p>This is the abstract text.</jats:p>'
        clean = LiteratureVerifier._strip_jats_html(raw)

        assert clean == "This is the abstract text."
        assert "<jats:" not in clean

    def test_extract_abstract_body_from_pubmed(self):
        """Test extracting abstract from PubMed text format."""
        raw_text = '''
1. J Bacteriol. 2020 Aug 10;202(17):e00123-20. doi: 10.1128/JB.00123-20.

Title of the paper goes here.

Author information:
(1)Department of Biology, University Example.
(2)Institute of Science.

This is the actual abstract text that we want to extract. It continues
for several lines and contains the main content.

PMID: 12345678
DOI: 10.1128/JB.00123-20
        '''

        abstract = LiteratureVerifier._extract_abstract_body_from_pubmed(raw_text)

        assert "This is the actual abstract text" in abstract
        assert "Author information" not in abstract
        assert "PMID:" not in abstract
        assert "DOI:" not in abstract

    def test_validate_evidence_snippet_exact_match(self):
        """Test evidence validation with exact match."""
        verifier = LiteratureVerifier()

        snippet = "ATCC 1306 and DSMZ 632 are equivalent media"
        text = "In our study, we found that ATCC 1306 and DSMZ 632 are equivalent media for growing this organism."

        assert verifier.validate_evidence_snippet(snippet, text) == True

    def test_validate_evidence_snippet_case_insensitive(self):
        """Test evidence validation is case-insensitive."""
        verifier = LiteratureVerifier()

        snippet = "atcc 1306 and dsmz 632 are equivalent media"
        text = "ATCC 1306 AND DSMZ 632 ARE EQUIVALENT MEDIA"

        assert verifier.validate_evidence_snippet(snippet, text) == True

    def test_validate_evidence_snippet_whitespace_normalized(self):
        """Test evidence validation normalizes whitespace."""
        verifier = LiteratureVerifier()

        snippet = "ATCC  1306   and   DSMZ   632"
        text = "ATCC 1306 and DSMZ 632 are used"

        assert verifier.validate_evidence_snippet(snippet, text) == True

    def test_validate_evidence_snippet_no_match(self):
        """Test evidence validation returns False when no match."""
        verifier = LiteratureVerifier()

        snippet = "ATCC 1306 and DSMZ 999"
        text = "ATCC 1306 and DSMZ 632 are equivalent"

        assert verifier.validate_evidence_snippet(snippet, text) == False

    def test_validate_evidence_snippet_empty_inputs(self):
        """Test evidence validation handles empty inputs."""
        verifier = LiteratureVerifier()

        assert verifier.validate_evidence_snippet("", "some text") == False
        assert verifier.validate_evidence_snippet("snippet", "") == False
        assert verifier.validate_evidence_snippet("", "") == False

    @patch('culturemech.enrich.literature_verifier.requests.Session.get')
    def test_fetch_pubmed_abstract_caching(self, mock_get):
        """Test that PubMed abstracts are cached."""
        with tempfile.TemporaryDirectory() as tmpdir:
            verifier = LiteratureVerifier(cache_dir=tmpdir)

            # Mock response
            mock_response = Mock()
            mock_response.text = "Abstract text here\n\nPMID: 12345678"
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response

            # First call - should hit API
            abstract1 = verifier.fetch_pubmed_abstract("12345678")
            assert mock_get.call_count == 1

            # Second call - should use cache
            abstract2 = verifier.fetch_pubmed_abstract("12345678")
            assert mock_get.call_count == 1  # No additional call

            assert abstract1 == abstract2

    @patch('culturemech.enrich.literature_verifier.requests.Session.get')
    def test_fetch_doi_metadata_caching(self, mock_get):
        """Test that DOI metadata is cached."""
        with tempfile.TemporaryDirectory() as tmpdir:
            verifier = LiteratureVerifier(cache_dir=tmpdir)

            # Mock response
            mock_response = Mock()
            mock_response.json.return_value = {"message": {"title": "Test Paper"}}
            mock_response.raise_for_status = Mock()
            mock_get.return_value = mock_response

            # First call - should hit API
            metadata1 = verifier.fetch_doi_metadata("10.1234/test")
            assert mock_get.call_count == 1

            # Second call - should use cache
            metadata2 = verifier.fetch_doi_metadata("10.1234/test")
            assert mock_get.call_count == 1  # No additional call

            assert metadata1 == metadata2

    def test_get_pdf_url_from_publisher_asm(self):
        """Test ASM publisher PDF URL patterns."""
        verifier = LiteratureVerifier()

        with patch('culturemech.enrich.literature_verifier.requests.head') as mock_head:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.headers = {"Content-Type": "application/pdf"}
            mock_head.return_value = mock_response

            pdf_url = verifier._get_pdf_url_from_publisher("10.1128/JB.00123-20")

            assert pdf_url is not None
            assert "10.1128/JB.00123-20" in pdf_url

    def test_fetch_pdf_url_skips_scihub_when_disabled(self):
        """Test that Sci-Hub is skipped when disabled."""
        verifier = LiteratureVerifier(use_fallback_pdf=False)

        with patch.object(verifier, '_get_pdf_url_from_publisher', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_pmc', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_unpaywall', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_semantic_scholar', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_fallback_mirrors') as mock_fallback, \
             patch.object(verifier, '_get_pdf_url_from_web_search', return_value=None):

            verifier.fetch_pdf_url("10.1234/test")

            # Sci-Hub should not be called
            mock_fallback.assert_not_called()

    def test_fetch_pdf_url_tries_scihub_when_enabled(self):
        """Test that Sci-Hub is tried when enabled."""
        verifier = LiteratureVerifier(use_fallback_pdf=True)

        with patch.object(verifier, '_get_pdf_url_from_publisher', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_pmc', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_unpaywall', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_semantic_scholar', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_fallback_mirrors', return_value=None) as mock_fallback, \
             patch.object(verifier, '_get_pdf_url_from_web_search', return_value=None):

            verifier.fetch_pdf_url("10.1234/test")

            # Sci-Hub should be called
            mock_fallback.assert_called_once()

    def test_cascading_stops_at_first_success(self):
        """Test that cascading stops at first successful tier."""
        verifier = LiteratureVerifier()

        with patch.object(verifier, '_get_pdf_url_from_publisher', return_value=None), \
             patch.object(verifier, '_get_pdf_url_from_pmc', return_value="http://pmc.test/paper.pdf") as mock_pmc, \
             patch.object(verifier, '_get_pdf_url_from_unpaywall') as mock_unpaywall, \
             patch.object(verifier, '_get_pdf_url_from_semantic_scholar') as mock_s2:

            result = verifier.fetch_pdf_url("10.1234/test")

            # Should stop at PMC
            assert result == ("http://pmc.test/paper.pdf", "pmc")
            mock_pmc.assert_called_once()
            # Later tiers should not be called
            mock_unpaywall.assert_not_called()
            mock_s2.assert_not_called()


class TestPDFTextExtraction:
    """Tests for PDF text extraction."""

    def test_extract_text_from_pdf_missing_pypdf2(self):
        """Test graceful handling when PyPDF2 is not installed."""
        verifier = LiteratureVerifier()

        with patch('culturemech.enrich.literature_verifier.PyPDF2', None):
            with tempfile.NamedTemporaryFile(suffix='.pdf') as f:
                text = verifier.extract_text_from_pdf(Path(f.name))
                assert text is None
