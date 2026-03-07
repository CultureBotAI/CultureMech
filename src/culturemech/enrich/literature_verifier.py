"""
Literature verification with cascading PDF retrieval for CultureMech.

IMPORTANT: This module includes optional fallback PDF retrieval through
Sci-Hub mirrors. Use may violate publisher agreements or local laws.
DISABLED by default - requires explicit opt-in via:
- CLI: --enable-scihub-fallback
- ENV: ENABLE_SCIHUB_FALLBACK=true

Users responsible for institutional compliance.

Cascading PDF fetch strategy:
1. Direct publisher websites (ASM, PLOS, Frontiers, MDPI, Nature, Science, Elsevier)
2. PubMed Central (PMC)
3. Unpaywall API (open access)
4. Semantic Scholar
5. Fallback PDF mirrors (Sci-Hub, opt-in only)
6. Web search (arXiv, bioRxiv, Europe PMC)
"""

import re
import requests
import os
import time
import json
from pathlib import Path
from typing import Optional, Tuple, Dict, List, Any


class LiteratureVerifier:
    """
    Fetch scientific literature with cascading PDF access including Sci-Hub fallback.

    Features:
    - PubMed abstract fetching
    - DOI metadata from CrossRef
    - Cascading PDF download (publisher → PMC → Unpaywall → Sci-Hub)
    - PDF text extraction
    - Evidence validation
    - Persistent caching
    """

    def __init__(
        self,
        cache_dir: str = "references_cache",
        pdf_cache_dir: str = "pdf_cache",
        email: str = "noreply@example.com",
        use_fallback_pdf: bool = False  # Opt-in for Sci-Hub
    ):
        """
        Initialize literature verifier.

        Args:
            cache_dir: Directory for caching abstracts and metadata
            pdf_cache_dir: Directory for caching downloaded PDFs
            email: Email for API usage (PubMed, Unpaywall)
            use_fallback_pdf: Whether to use Sci-Hub fallback (disabled by default)
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(exist_ok=True)

        self.pdf_cache_dir = Path(pdf_cache_dir)
        self.pdf_cache_dir.mkdir(exist_ok=True)

        self.email = email
        self.use_fallback_pdf = use_fallback_pdf
        self.fallback_pdf_urls = self._get_fallback_pdf_urls()

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "CultureMech/0.1.0 (https://github.com/Knowledge-Graph-Hub/kg-microbe)"
        })

    def _get_fallback_pdf_urls(self) -> List[str]:
        """
        Get list of Sci-Hub mirror URLs.

        Can be configured via FALLBACK_PDF_MIRRORS environment variable (comma-separated).
        Defaults to commonly working mirrors.

        Returns:
            List of fallback PDF base URLs
        """
        # Check environment variable first
        env_mirrors = os.getenv("FALLBACK_PDF_MIRRORS", "")
        if env_mirrors:
            return [url.strip() for url in env_mirrors.split(",") if url.strip()]

        # Default fallback mirrors (these change frequently)
        return [
            "https://sci-hub.se",
            "https://sci-hub.st",
            "https://sci-hub.ru",
            "https://sci-hub.ren",
        ]

    # ========================================================================
    # ABSTRACT & METADATA FETCHING
    # ========================================================================

    @staticmethod
    def _extract_abstract_body_from_pubmed(raw_text: str) -> str:
        """
        Extract just the abstract body from PubMed E-utilities text output.

        PubMed text format has: citation, title, authors, affiliations, ABSTRACT, PMID.
        This method strips everything before the abstract body.

        Args:
            raw_text: Full PubMed E-utilities text response

        Returns:
            Clean abstract text only
        """
        if not raw_text:
            return raw_text

        # Strategy: find the blank line after "Author information:" block
        # then take everything until "PMID:" at the end
        lines = raw_text.split('\n')
        abstract_lines = []
        in_author_section = False
        past_authors = False

        for i, line in enumerate(lines):
            stripped = line.strip()

            if stripped.startswith('Author information:'):
                in_author_section = True
                continue

            if in_author_section:
                # End of author section = blank line or new section
                if stripped == '':
                    in_author_section = False
                    past_authors = True
                continue

            if past_authors:
                # Stop at trailing metadata (PMID, DOI lines at end)
                if re.match(r'^PMID:\s*\d+', stripped):
                    break
                if re.match(r'^DOI:\s*10\.', stripped):
                    break
                abstract_lines.append(line)

        abstract = '\n'.join(abstract_lines).strip()

        # Fallback: if no author section found, try splitting on double-newline
        # The abstract is usually the last large block before PMID
        if not abstract:
            blocks = re.split(r'\n\n+', raw_text)
            # Find the longest block that doesn't look like a citation or author list
            for block in reversed(blocks):
                block = block.strip()
                if (len(block) > 100
                        and not re.search(r'PMID:\s*\d+', block)
                        and not re.search(r'\(\d+\)', block[:50])):
                    abstract = block
                    break

        # Normalize whitespace
        abstract = re.sub(r'\s+', ' ', abstract).strip()
        return abstract

    def fetch_pubmed_abstract(self, pmid: str) -> Optional[str]:
        """
        Fetch abstract from PubMed for a given PMID.

        Returns cleaned abstract body text (strips author info, citation headers).

        Args:
            pmid: PubMed ID (e.g., "32753581")

        Returns:
            Abstract text or None if not found
        """
        # Clean PMID
        pmid = pmid.replace("PMID:", "").strip()

        # Check cache first
        cache_file = self.cache_dir / f"pmid_{pmid}.txt"
        if cache_file.exists():
            raw = cache_file.read_text()
            return self._extract_abstract_body_from_pubmed(raw)

        # Fetch from PubMed E-utilities
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
        params = {
            "db": "pubmed",
            "id": pmid,
            "rettype": "abstract",
            "retmode": "text",
        }

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()

            raw = response.text

            # Cache the raw result
            cache_file.write_text(raw)

            return self._extract_abstract_body_from_pubmed(raw)

        except requests.exceptions.RequestException as e:
            print(f"Error fetching PMID {pmid}: {e}")
            return None

    def fetch_doi_metadata(self, doi: str) -> Optional[dict]:
        """
        Fetch metadata for a DOI from CrossRef.

        Args:
            doi: DOI (e.g., "10.1038/s41467-020-17612-8")

        Returns:
            Metadata dict or None
        """
        # Clean DOI
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Check cache
        cache_file = self.cache_dir / f"doi_{doi.replace('/', '_')}.json"
        if cache_file.exists():
            return json.loads(cache_file.read_text())

        # Fetch from CrossRef
        url = f"https://api.crossref.org/works/{doi}"

        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            metadata = response.json()

            # Cache the result
            cache_file.write_text(json.dumps(metadata, indent=2))

            return metadata

        except requests.exceptions.RequestException as e:
            print(f"Error fetching DOI {doi}: {e}")
            return None

    @staticmethod
    def _strip_jats_html(text: str) -> str:
        """
        Strip JATS XML tags and HTML from CrossRef abstract text.

        CrossRef abstracts use JATS XML format with tags like:
        <jats:title>Abstract</jats:title>
        <jats:p>Text content here...</jats:p>
        <jats:sec>...</jats:sec>

        Args:
            text: Raw abstract text possibly containing JATS/HTML tags

        Returns:
            Clean plain text
        """
        if not text:
            return text
        # Remove all XML/HTML tags (JATS and regular)
        clean = re.sub(r'<[^>]+>', ' ', text)
        # Collapse whitespace
        clean = re.sub(r'\s+', ' ', clean).strip()
        # Remove "Abstract" heading that often remains
        clean = re.sub(r'^Abstract\s*', '', clean, flags=re.IGNORECASE)
        return clean

    def fetch_abstract_from_europepmc(self, doi: str) -> Optional[str]:
        """
        Fetch abstract from Europe PMC by DOI.

        Europe PMC has excellent coverage for life sciences papers and
        returns clean plain-text abstracts.

        Args:
            doi: DOI string (with or without doi: prefix)

        Returns:
            Abstract text or None
        """
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Check cache
        cache_key = f"europepmc_{doi.replace('/', '_')}.txt"
        cache_file = self.cache_dir / cache_key
        if cache_file.exists():
            content = cache_file.read_text()
            return content if content else None

        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
        params = {
            "query": f"DOI:{doi}",
            "resulttype": "core",
            "format": "json",
            "pageSize": 1,
        }

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            results = data.get("resultList", {}).get("result", [])
            if results:
                abstract = results[0].get("abstractText", "")
                if abstract:
                    cache_file.write_text(abstract)
                    return abstract

            # Cache empty result to avoid repeated failed requests
            cache_file.write_text("")
            return None

        except requests.exceptions.RequestException:
            return None

    def fetch_abstract_from_semantic_scholar(self, doi: str) -> Optional[str]:
        """
        Fetch abstract from Semantic Scholar Graph API v1.

        Uses the graph API which returns structured paper data including abstracts.

        Args:
            doi: DOI string (with or without doi: prefix)

        Returns:
            Abstract text or None
        """
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Check cache
        cache_key = f"s2_{doi.replace('/', '_')}.txt"
        cache_file = self.cache_dir / cache_key
        if cache_file.exists():
            content = cache_file.read_text()
            return content if content else None

        url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
        params = {"fields": "abstract,title"}

        try:
            response = self.session.get(url, params=params, timeout=30)
            if response.status_code == 200:
                data = response.json()
                abstract = data.get("abstract", "")
                if abstract:
                    cache_file.write_text(abstract)
                    return abstract

            cache_file.write_text("")
            return None

        except requests.exceptions.RequestException:
            return None

    def fetch_pmid_from_doi(self, doi: str) -> Optional[str]:
        """
        Look up PubMed ID from DOI using PubMed E-utilities esearch.

        Args:
            doi: DOI string (with or without doi: prefix)

        Returns:
            PMID string or None
        """
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Check cache
        cache_key = f"doi2pmid_{doi.replace('/', '_')}.txt"
        cache_file = self.cache_dir / cache_key
        if cache_file.exists():
            content = cache_file.read_text().strip()
            return content if content else None

        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": f"{doi}[DOI]",
            "retmode": "json",
            "retmax": 1,
        }

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            id_list = data.get("esearchresult", {}).get("idlist", [])
            if id_list:
                pmid = id_list[0]
                cache_file.write_text(pmid)
                return pmid

            cache_file.write_text("")
            return None

        except requests.exceptions.RequestException:
            return None

    def fetch_abstract_for_doi(self, doi: str) -> Optional[str]:
        """
        Fetch abstract for a DOI using cascading strategy.

        Tries in order:
        1. CrossRef metadata (strips JATS/HTML tags from abstract)
        2. PubMed DOI search -> abstract (only if CrossRef confirms DOI is valid)
        3. Europe PMC search
        4. Semantic Scholar Graph API

        Note: PubMed DOI search is skipped if CrossRef returns a 404 to avoid
        matching the wrong paper when a DOI is malformed or not in PubMed.

        Args:
            doi: DOI string (with or without doi: prefix)

        Returns:
            Clean abstract text or None
        """
        doi_clean = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Strategy 1: CrossRef (already fetched metadata, extract & clean abstract)
        doi_is_valid = False
        metadata = self.fetch_doi_metadata(doi_clean)
        if metadata:
            doi_is_valid = True  # CrossRef knows this DOI
            # Abstract is in metadata["message"]["abstract"] (JATS-formatted)
            message = metadata.get("message", {})
            raw_abstract = message.get("abstract", "")
            if raw_abstract:
                clean = self._strip_jats_html(raw_abstract)
                if len(clean) > 50:
                    return clean

        # Strategy 2: PubMed DOI -> PMID -> abstract
        # Only if CrossRef confirmed the DOI is real (avoids wrong-paper matches)
        if doi_is_valid:
            pmid = self.fetch_pmid_from_doi(doi_clean)
            if pmid:
                time.sleep(0.4)  # Respect PubMed rate limits (3 req/sec)
                abstract = self.fetch_pubmed_abstract(pmid)
                if abstract:
                    return abstract

        # Strategy 3: Europe PMC (good for life sciences, no DOI-validity requirement)
        abstract = self.fetch_abstract_from_europepmc(doi_clean)
        if abstract:
            return abstract

        # Strategy 4: Semantic Scholar Graph API
        abstract = self.fetch_abstract_from_semantic_scholar(doi_clean)
        if abstract and len(abstract) > 50:
            # Strip any residual HTML from Semantic Scholar abstracts
            return self._strip_jats_html(abstract)

        return None

    # ========================================================================
    # PDF FETCHING (cascading strategy)
    # ========================================================================

    def fetch_pdf_url(self, doi: str) -> Optional[Tuple[str, str]]:
        """
        Fetch PDF URL using cascading strategy.

        Tries multiple sources in order:
        1. Direct publisher website
        2. PubMed Central (PMC)
        3. Unpaywall API
        4. Semantic Scholar
        5. Fallback PDF mirrors (Sci-Hub, if enabled)
        6. Web search

        Args:
            doi: DOI of paper

        Returns:
            Tuple of (pdf_url, source) or None
        """
        doi = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Try 1: Direct publisher website
        print(f"Trying direct publisher access for {doi}...")
        pdf_url = self._get_pdf_url_from_publisher(doi)
        if pdf_url:
            print(f"✓ Found PDF via publisher")
            return (pdf_url, "publisher")

        # Try 2: PubMed Central (PMC)
        print(f"Trying PubMed Central for {doi}...")
        pdf_url = self._get_pdf_url_from_pmc(doi)
        if pdf_url:
            print(f"✓ Found PDF via PubMed Central")
            return (pdf_url, "pmc")

        # Try 3: Unpaywall API
        print(f"Trying Unpaywall API for {doi}...")
        pdf_url = self._get_pdf_url_from_unpaywall(doi)
        if pdf_url:
            print(f"✓ Found PDF via Unpaywall")
            return (pdf_url, "unpaywall")

        # Try 4: Semantic Scholar
        print(f"Trying Semantic Scholar for {doi}...")
        pdf_url = self._get_pdf_url_from_semantic_scholar(doi)
        if pdf_url:
            print(f"✓ Found PDF via Semantic Scholar")
            return (pdf_url, "semantic_scholar")

        # Try 5: Fallback PDF mirrors (Sci-Hub)
        if self.use_fallback_pdf:
            print(f"Trying fallback PDF mirrors for {doi}...")
            pdf_url = self._get_pdf_url_from_fallback_mirrors(doi)
            if pdf_url:
                return (pdf_url, "fallback_mirror")

        # Try 6: Web search (last resort)
        print(f"Trying web search for {doi}...")
        pdf_url = self._get_pdf_url_from_web_search(doi)
        if pdf_url:
            print(f"✓ Found PDF via web search")
            return (pdf_url, "web_search")

        print(f"✗ Could not find PDF for {doi}")
        return None

    def _get_pdf_url_from_publisher(self, doi: str) -> Optional[str]:
        """Try to get PDF directly from publisher website."""
        publisher_patterns = []

        # Publisher-specific patterns
        if doi.startswith("10.1128"):  # ASM
            publisher_patterns.extend([
                f"https://journals.asm.org/doi/pdf/{doi}",
                f"https://journals.asm.org/doi/pdfdirect/{doi}",
            ])
        elif doi.startswith("10.1371"):  # PLOS
            publisher_patterns.append(
                f"https://journals.plos.org/plosone/article/file?id={doi}&type=printable"
            )
        elif doi.startswith("10.3389"):  # Frontiers
            publisher_patterns.append(f"https://www.frontiersin.org/articles/{doi}/pdf")
        elif doi.startswith("10.3390"):  # MDPI
            publisher_patterns.append(f"https://www.mdpi.com/{doi}/pdf")
        elif doi.startswith("10.1038"):  # Nature
            publisher_patterns.append(f"https://www.nature.com/articles/{doi}.pdf")
        elif doi.startswith("10.1126"):  # Science
            publisher_patterns.append(f"https://www.science.org/doi/pdf/{doi}")
        elif doi.startswith("10.1016"):  # Elsevier
            publisher_patterns.append(f"https://www.sciencedirect.com/science/article/pii/{doi}/pdfft")

        # Generic patterns
        publisher_patterns.extend([
            f"https://doi.org/{doi}.pdf",
            f"https://doi.org/{doi}/pdf",
        ])

        # Try each pattern
        for url in publisher_patterns:
            try:
                response = requests.head(url, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    content_type = response.headers.get("Content-Type", "")
                    if "pdf" in content_type.lower():
                        return url
            except Exception:
                continue

        return None

    def _get_pdf_url_from_pmc(self, doi: str) -> Optional[str]:
        """Get PDF URL from PubMed Central."""
        try:
            # Search for PMC ID using DOI
            search_url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"
            params = {
                "ids": doi,
                "format": "json",
                "tool": "culturemech",
                "email": self.email,
            }

            response = requests.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            # Check if we got a PMC ID
            if "records" in data and len(data["records"]) > 0:
                record = data["records"][0]
                pmcid = record.get("pmcid")

                if pmcid:
                    # Construct PDF URL from PMC ID
                    pmc_number = pmcid.replace("PMC", "")
                    pdf_url = f"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC{pmc_number}/pdf/"

                    # Verify it exists
                    head_response = requests.head(pdf_url, timeout=5, allow_redirects=True)
                    if head_response.status_code == 200:
                        return pdf_url

            return None

        except Exception:
            return None

    def _get_pdf_url_from_unpaywall(self, doi: str) -> Optional[str]:
        """Get PDF URL from Unpaywall API."""
        url = f"https://api.unpaywall.org/v2/{doi}"
        params = {"email": self.email}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()

            data = response.json()

            # Check for OA location
            if data.get("is_oa") and data.get("best_oa_location"):
                pdf_url = data["best_oa_location"].get("url_for_pdf")
                return pdf_url

            return None

        except Exception:
            return None

    def _get_pdf_url_from_semantic_scholar(self, doi: str) -> Optional[str]:
        """Get PDF URL from Semantic Scholar API."""
        try:
            url = f"https://api.semanticscholar.org/v1/paper/{doi}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            # Check for open access PDF
            if data.get("isOpenAccess") and data.get("openAccessPdf"):
                pdf_url = data["openAccessPdf"].get("url")
                return pdf_url

            return None

        except Exception:
            return None

    def _get_pdf_url_from_fallback_mirrors(self, doi: str) -> Optional[str]:
        """
        Try Sci-Hub mirrors sequentially.

        Returns:
            PDF URL or None
        """
        for fallback_base in self.fallback_pdf_urls:
            fallback_url = f"{fallback_base}/{doi}"
            try:
                print(f"  Trying mirror: {fallback_base}...")
                response = requests.get(fallback_url, timeout=15, allow_redirects=True)
                if response.status_code == 200:
                    # Mirror returns HTML page with embedded PDF
                    pdf_url = self._extract_pdf_from_fallback_html(response.text, fallback_base)
                    if pdf_url:
                        print(f"  ✓ Found PDF via fallback: {pdf_url}")
                        return pdf_url
                    else:
                        print(f"  ✗ Fallback page loaded but no PDF found")
                else:
                    print(f"  ✗ Fallback returned status {response.status_code}")
            except Exception as e:
                print(f"  ✗ Fallback error: {e}")
                continue

        return None

    def _get_pdf_url_from_web_search(self, doi: str) -> Optional[str]:
        """
        Search for PDF in open repositories.

        Tries: arXiv, bioRxiv, Europe PMC
        """
        # Common open repositories
        open_repositories = [
            f"https://arxiv.org/pdf/{doi}.pdf",
            f"https://www.biorxiv.org/content/{doi}.full.pdf",
            f"https://europepmc.org/article/ppr/{doi}/pdf",
        ]

        for repo_url in open_repositories:
            try:
                response = requests.head(repo_url, timeout=5, allow_redirects=True)
                if response.status_code == 200:
                    content_type = response.headers.get("Content-Type", "")
                    if "pdf" in content_type.lower():
                        return repo_url
            except Exception:
                continue

        return None

    def _extract_pdf_from_fallback_html(self, html: str, base_url: str) -> Optional[str]:
        """
        Extract actual PDF URL from Sci-Hub HTML page using 4 strategies.

        Args:
            html: HTML content from fallback PDF source page
            base_url: Base URL of the fallback mirror

        Returns:
            PDF URL or None
        """
        try:
            # Strategy 1: <object type="application/pdf" data="...">
            object_pattern = r'<object[^>]+type\s*=\s*["\']application/pdf["\'][^>]+data\s*=\s*["\']([^"\'#]+)'
            matches = re.findall(object_pattern, html, re.IGNORECASE)
            if matches:
                pdf_path = matches[0]
                return self._normalize_pdf_url(pdf_path, base_url)

            # Strategy 2: <a href="/download/...pdf">
            download_pattern = r'<a[^>]+href\s*=\s*["\']([^"\']+\.pdf[^"\']*)["\']'
            matches = re.findall(download_pattern, html, re.IGNORECASE)
            if matches:
                pdf_path = matches[0]
                return self._normalize_pdf_url(pdf_path, base_url)

            # Strategy 3: <embed> or <iframe>
            embed_patterns = [
                r'<embed[^>]+src=["\']([^"\']+\.pdf[^"\']*)["\']',
                r'<iframe[^>]+src=["\']([^"\']+\.pdf[^"\']*)["\']',
            ]

            for pattern in embed_patterns:
                matches = re.findall(pattern, html, re.IGNORECASE)
                if matches:
                    pdf_path = matches[0]
                    return self._normalize_pdf_url(pdf_path, base_url)

            # Strategy 4: Direct PDF URLs
            pdf_pattern = r'(https?://[^\s"\'<>]+\.pdf)'
            matches = re.findall(pdf_pattern, html)
            if matches:
                return matches[0]

            return None

        except Exception as e:
            print(f"    Error extracting PDF from fallback HTML: {e}")
            return None

    def _normalize_pdf_url(self, pdf_path: str, base_url: str) -> str:
        """Normalize relative PDF paths to absolute URLs."""
        if pdf_path.startswith('http'):
            return pdf_path
        elif pdf_path.startswith('//'):
            return 'https:' + pdf_path
        else:
            return base_url + pdf_path

    # ========================================================================
    # PDF DOWNLOAD & TEXT EXTRACTION
    # ========================================================================

    def download_pdf(self, doi: str) -> Optional[Path]:
        """
        Download PDF for a given DOI.

        Args:
            doi: DOI of paper

        Returns:
            Path to downloaded PDF or None
        """
        doi_clean = doi.replace("doi:", "").replace("https://doi.org/", "").strip()

        # Check cache first
        cache_file = self.pdf_cache_dir / f"{doi_clean.replace('/', '_')}.pdf"
        if cache_file.exists():
            print(f"✓ PDF already cached: {cache_file}")
            return cache_file

        # Fetch PDF URL
        result = self.fetch_pdf_url(doi_clean)
        if not result:
            return None

        pdf_url, source = result
        print(f"Downloading PDF from {source}: {pdf_url}")

        # Download PDF
        try:
            response = requests.get(pdf_url, timeout=60, stream=True)
            response.raise_for_status()

            # Write to cache
            with open(cache_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            print(f"✓ PDF downloaded: {cache_file}")
            return cache_file

        except Exception as e:
            print(f"✗ Error downloading PDF: {e}")
            return None

    def extract_text_from_pdf(self, pdf_path: Path) -> Optional[str]:
        """
        Extract text from PDF file.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Extracted text or None
        """
        try:
            import PyPDF2

            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"

            return text

        except ImportError:
            print("✗ PyPDF2 not installed. Install with: pip install PyPDF2")
            return None
        except Exception as e:
            print(f"✗ Error extracting PDF text: {e}")
            return None

    # ========================================================================
    # EVIDENCE VALIDATION
    # ========================================================================

    def validate_evidence_snippet(self, snippet: str, text: str) -> bool:
        """
        Check if a snippet appears in the text (fuzzy match).

        Args:
            snippet: Quoted text to validate
            text: Full text to search in (abstract or PDF)

        Returns:
            True if snippet found in text
        """
        if not text or not snippet:
            return False

        # Normalize whitespace
        snippet_normalized = " ".join(snippet.split())
        text_normalized = " ".join(text.split())

        # Check for exact match
        if snippet_normalized.lower() in text_normalized.lower():
            return True

        # Check for fuzzy match (allow minor differences)
        from difflib import SequenceMatcher
        ratio = SequenceMatcher(None, snippet_normalized.lower(), text_normalized.lower()).ratio()
        if ratio > 0.95:
            return True

        return False
