"""
ATCC cross-reference verification using literature evidence.

Verifies ATCC-DSMZ media equivalencies by searching for scientific papers
that confirm the matches.
"""

import re
from typing import List, Dict, Any, Optional
from pathlib import Path
import time
import requests

from culturemech.enrich.literature_verifier import LiteratureVerifier


class ATCCCrossRefVerifier:
    """
    Verify ATCC-DSMZ cross-references using literature evidence.

    Uses LiteratureVerifier to search for and fetch papers that confirm
    media equivalencies.
    """

    def __init__(self, literature_verifier: LiteratureVerifier):
        """
        Initialize verifier.

        Args:
            literature_verifier: LiteratureVerifier instance
        """
        self.verifier = literature_verifier

    def search_for_equivalency_papers(
        self,
        atcc_id: str,
        dsmz_id: str,
        atcc_name: str = "",
        dsmz_name: str = ""
    ) -> List[Dict[str, Any]]:
        """
        Search PubMed for papers mentioning both media.

        Args:
            atcc_id: ATCC medium number (e.g., "1306")
            dsmz_id: DSMZ medium number (e.g., "632")
            atcc_name: ATCC medium name (optional, for better search)
            dsmz_name: DSMZ medium name (optional)

        Returns:
            List of papers with DOI and relevance info
        """
        results = []

        # Query 1: Both media IDs with equivalency terms
        query = f'"ATCC {atcc_id}" AND "DSMZ {dsmz_id}" AND (equivalent OR identical OR same)'

        # Use NCBI E-utilities esearch
        url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        params = {
            "db": "pubmed",
            "term": query,
            "retmode": "json",
            "retmax": 10,  # Top 10 results
            "sort": "relevance",
        }

        try:
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            pmid_list = data.get("esearchresult", {}).get("idlist", [])

            # For each PMID, try to get DOI
            for pmid in pmid_list:
                time.sleep(0.4)  # Rate limiting (3 req/sec)

                # Fetch abstract to get DOI
                abstract_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
                abstract_params = {
                    "db": "pubmed",
                    "id": pmid,
                    "rettype": "abstract",
                    "retmode": "text",
                }

                try:
                    abstract_response = requests.get(abstract_url, params=abstract_params, timeout=30)
                    abstract_response.raise_for_status()
                    abstract_text = abstract_response.text

                    # Extract DOI from abstract text
                    doi_match = re.search(r'DOI:\s*(10\.\S+)', abstract_text)
                    if doi_match:
                        doi = doi_match.group(1).strip()
                        results.append({
                            "pmid": pmid,
                            "doi": doi,
                            "relevance": "high" if f"ATCC {atcc_id}" in abstract_text and f"DSMZ {dsmz_id}" in abstract_text else "medium"
                        })
                    else:
                        # No DOI, just track PMID
                        results.append({
                            "pmid": pmid,
                            "doi": None,
                            "relevance": "medium"
                        })

                except Exception as e:
                    print(f"Error fetching abstract for PMID {pmid}: {e}")
                    continue

        except requests.exceptions.RequestException as e:
            print(f"Error searching PubMed: {e}")

        return results

    def verify_equivalency_from_paper(
        self,
        doi: str,
        atcc_id: str,
        dsmz_id: str
    ) -> Optional[Dict[str, Any]]:
        """
        Download PDF and search for confirmation text.

        Args:
            doi: DOI of paper
            atcc_id: ATCC medium number
            dsmz_id: DSMZ medium number

        Returns:
            Verification dict with evidence or None
        """
        # Download PDF
        pdf_path = self.verifier.download_pdf(doi)
        if not pdf_path:
            # Try abstract as fallback
            abstract = self.verifier.fetch_abstract_for_doi(doi)
            if abstract:
                return self._verify_from_text(abstract, doi, atcc_id, dsmz_id, source="abstract")
            return None

        # Extract text
        text = self.verifier.extract_text_from_pdf(pdf_path)
        if not text:
            return None

        return self._verify_from_text(text, doi, atcc_id, dsmz_id, source="pdf")

    def _verify_from_text(
        self,
        text: str,
        doi: str,
        atcc_id: str,
        dsmz_id: str,
        source: str = "pdf"
    ) -> Optional[Dict[str, Any]]:
        """
        Search text for confirmation patterns.

        Args:
            text: Full text to search
            doi: DOI of source
            atcc_id: ATCC medium number
            dsmz_id: DSMZ medium number
            source: Source type ("pdf" or "abstract")

        Returns:
            Verification dict or None
        """
        # Confirmation patterns
        patterns = [
            # Direct equivalency statements
            rf"ATCC\s+{atcc_id}[^\n{{0,50}}]{{0,50}}DSMZ\s+{dsmz_id}[^\n]{{0,50}}(equivalent|identical|same|equal)",
            rf"DSMZ\s+{dsmz_id}[^\n]{{0,50}}ATCC\s+{atcc_id}[^\n]{{0,50}}(equivalent|identical|same|equal)",
            rf"(equivalent|identical|same)\s+to\s+ATCC\s+{atcc_id}.*DSMZ\s+{dsmz_id}",
            rf"(equivalent|identical|same)\s+to\s+DSMZ\s+{dsmz_id}.*ATCC\s+{atcc_id}",

            # Table or list mentions
            rf"ATCC\s+{atcc_id}\s*[/|,]\s*DSMZ\s+{dsmz_id}",
            rf"DSMZ\s+{dsmz_id}\s*[/|,]\s*ATCC\s+{atcc_id}",

            # Synonym statements
            rf"ATCC\s+{atcc_id}\s*\([^)]*DSMZ\s+{dsmz_id}",
            rf"DSMZ\s+{dsmz_id}\s*\([^)]*ATCC\s+{atcc_id}",
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                # Extract surrounding context (±100 chars)
                start = max(0, match.start() - 100)
                end = min(len(text), match.end() + 100)
                snippet = text[start:end].strip()

                # Clean up snippet
                snippet = " ".join(snippet.split())  # Normalize whitespace

                return {
                    "verified": True,
                    "atcc_id": atcc_id,
                    "dsmz_id": dsmz_id,
                    "doi": doi,
                    "evidence_snippet": snippet,
                    "source_tier": source,
                    "pattern_matched": pattern
                }

        # No match found
        return None

    def batch_verify_candidates(
        self,
        candidates: List[Dict],
        min_similarity: float = 0.85,
        max_similarity: float = 0.95
    ) -> List[Dict[str, Any]]:
        """
        Verify medium-confidence candidates in batch.

        Args:
            candidates: List of candidate cross-references
            min_similarity: Minimum similarity threshold
            max_similarity: Maximum similarity threshold

        Returns:
            List of verified matches with evidence
        """
        results = []

        # Filter to medium-confidence range
        medium_confidence = [
            c for c in candidates
            if min_similarity <= c.get("similarity", 0) < max_similarity
        ]

        print(f"Verifying {len(medium_confidence)} medium-confidence candidates via literature...")

        for i, candidate in enumerate(medium_confidence, 1):
            atcc_id = candidate.get("atcc_id", "")
            dsmz_id = candidate.get("dsmz_id", "")
            atcc_name = candidate.get("atcc_name", "")
            dsmz_name = candidate.get("dsmz_name", "")

            print(f"\n[{i}/{len(medium_confidence)}] Checking ATCC {atcc_id} <-> DSMZ {dsmz_id}")

            # Search for papers
            papers = self.search_for_equivalency_papers(
                atcc_id, dsmz_id, atcc_name, dsmz_name
            )

            if not papers:
                print(f"  No papers found")
                continue

            print(f"  Found {len(papers)} papers")

            # Try to verify from top papers (only those with DOIs)
            verified = False
            for paper in papers[:3]:  # Top 3 results
                if not paper.get("doi"):
                    continue

                print(f"  Checking paper: {paper['doi']}")

                verification = self.verify_equivalency_from_paper(
                    paper["doi"],
                    atcc_id,
                    dsmz_id
                )

                if verification and verification.get("verified"):
                    print(f"  ✓ Verified via literature!")
                    results.append(verification)
                    verified = True
                    break

            if not verified:
                print(f"  ✗ Could not verify from literature")

            # Rate limiting between candidates
            time.sleep(1)

        print(f"\n✓ Verified {len(results)} candidates via literature")
        return results
