#!/usr/bin/env python3
"""Archive cited PubMed abstracts as original XML and derived Markdown.

Scan all tracked normalized YAML references, including bibliography, variants,
and ingredient evidence. Raw XML, Markdown, and checksummed provenance live in
references_cache/papers/. Existing legacy Markdown is preserved. --resolve-dois
also resolves DOI references by exact cross-check against the returned article.
Unmatched DOIs and metadata-only records remain explicit archival gaps, never
scientific review passes. --report records the full corpus inventory and results.

Used as the data source for `validate_evidence_references.py`. Polite
to NCBI: 3 req/s default, supports NCBI_API_KEY env var for 10 req/s.

Ported from culturebotai-claw / MIM (anti-hallucination evidence gate)
to CultureMech as part of the growth-evidence integration plan.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "references_cache"
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

DEFAULT_RATE = 3.0  # req/s without API key
KEYED_RATE = 10.0  # with NCBI_API_KEY

PMID_RE = re.compile(r"^[0-9]+$")
PMID_REF_RE = re.compile(r"^\s*PMID\s*[:\s]\s*([0-9]+)\s*$", re.IGNORECASE)
MAX_RESPONSE_BYTES = 5 * 1024 * 1024


def extract_pmid(reference: str) -> str | None:
    """Pull the numeric PMID out of a `reference:` string of shape
    `PMID:NNNNNNNN`. Returns None if it isn't a PMID-style reference."""
    if not reference:
        return None
    m = PMID_REF_RE.match(reference)
    if not m:
        return None
    pmid = m.group(1).strip()
    return pmid if PMID_RE.match(pmid) else None


def collect_from_evidence_list(evs, out: set[str]) -> None:
    for ev in evs or []:
        if not isinstance(ev, dict):
            continue
        pmid = extract_pmid((ev.get("reference") or "").strip())
        if pmid:
            out.add(pmid)


def iter_references(node, field=""):
    """Include bibliography and evidence at every nesting level."""
    if isinstance(node, dict):
        for key, value in node.items():
            location = f"{field}.{key}" if field else key
            if key == "reference" and isinstance(value, str):
                yield location, value
            yield from iter_references(value, location)
    elif isinstance(node, list):
        for index, value in enumerate(node):
            yield from iter_references(value, f"{field}[{index}]")


def publication_reference(value: str) -> str | None:
    pmid = extract_pmid(value)
    if pmid:
        return f"PMID:{pmid}"
    doi = re.sub(r"^(?:doi:\s*|https?://(?:dx\.)?doi\.org/)", "", value.strip(), flags=re.I)
    if re.fullmatch(r"10\.\d{4,9}/\S+", doi, flags=re.I):
        return f"doi:{doi.lower()}"
    return None


def citation_inventory(paths=None) -> dict:
    """Snapshot tracked normalized records, without treating a scan as a review."""
    if paths is None:
        listing = (
            subprocess.check_output(
                ["git", "ls-files", "-z", "data/normalized_yaml"], cwd=REPO_ROOT
            )
            .decode()
            .split("\0")
        )
        paths = [REPO_ROOT / path for path in listing if path.endswith((".yaml", ".yml"))]
    records = []
    references = {}
    for path in sorted(paths):
        raw = path.read_bytes()
        record = yaml.load(raw, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
        if not isinstance(record, dict):
            raise ValueError(f"not a recipe mapping: {path}")
        relative = path.relative_to(REPO_ROOT).as_posix()
        found = []
        for field, value in iter_references(record):
            reference = publication_reference(value)
            if reference:
                found.append(reference)
                references.setdefault(reference, []).append({"path": relative, "field": field})
        records.append(
            {
                "path": relative,
                "id": record.get("id"),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "references": sorted(set(found)),
                "citation_review": "not_reviewed",
            }
        )
    return {"records": records, "references": references}


def harvest_pmids() -> set[str]:
    return {
        reference[5:]
        for reference in citation_inventory()["references"]
        if reference.startswith("PMID:")
    }


def cache_path(pmid: str) -> Path:
    return CACHE_DIR / f"PMID_{pmid}.md"


def fetch_pubmed_xml(pmid: str, api_key: str | None) -> bytes:
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml",
        "rettype": "abstract",
    }
    if api_key:
        params["api_key"] = api_key
    url = f"{EUTILS}?{urllib.parse.urlencode(params)}"
    return fetch_bytes(url)


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "CultureMech-evidence-validator/1.0 (https://github.com/CultureBotAI/CultureMech)"
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                raw = response.read(MAX_RESPONSE_BYTES + 1)
            if len(raw) > MAX_RESPONSE_BYTES:
                raise ValueError("PubMed response exceeds size limit")
            return raw
        except urllib.error.HTTPError as error:
            if error.code not in (429, 500, 502, 503, 504) or attempt == 2:
                raise
        except (urllib.error.URLError, TimeoutError):
            if attempt == 2:
                raise
        time.sleep(2 ** (attempt + 1))
    raise RuntimeError("unreachable fetch retry state")


def parse_abstract(xml_text: str | bytes, expected_pmid: str | None = None) -> dict:
    """Extract title, authors, journal, year, abstract from a single
    PubmedArticle XML response."""
    root = ET.fromstring(xml_text)
    entries = root.findall("./PubmedArticle")
    if len(entries) != 1:
        raise ValueError("expected exactly one PubmedArticle")
    entry = entries[0]
    pmid = entry.findtext("MedlineCitation/PMID")
    if not pmid or not PMID_RE.fullmatch(pmid):
        raise ValueError("missing or invalid returned PMID")
    if expected_pmid is not None and pmid != expected_pmid:
        raise ValueError("returned PMID does not match request")
    article = entry.find("MedlineCitation/Article")
    if article is None:
        raise ValueError("missing Article")
    title_el = article.find("ArticleTitle")
    title = "".join(title_el.itertext()).strip() if title_el is not None else ""
    journal_el = article.find("Journal/Title")
    journal = journal_el.text.strip() if journal_el is not None and journal_el.text else ""
    year_el = article.find("Journal/JournalIssue/PubDate/Year")
    year = year_el.text.strip() if year_el is not None and year_el.text else ""
    if not year:
        date = article.findtext("Journal/JournalIssue/PubDate/MedlineDate") or ""
        match = re.match(r"(\d{4})\b", date)
        year = match[1] if match else ""
    abstract_parts: list[str] = []
    for ab in article.findall("Abstract/AbstractText"):
        label = ab.attrib.get("Label", "")
        text = "".join(ab.itertext()).strip()
        if not text:
            continue
        if label:
            abstract_parts.append(f"**{label}:** {text}")
        else:
            abstract_parts.append(text)
    abstract = "\n\n".join(abstract_parts)
    authors: list[str] = []
    for au in article.findall("AuthorList/Author"):
        last = au.findtext("LastName") or ""
        initials = au.findtext("Initials") or ""
        if last:
            authors.append(f"{last} {initials}".strip())
        elif au.findtext("CollectiveName"):
            authors.append(au.findtext("CollectiveName"))
    if not title:
        raise ValueError("missing article title")
    identifiers = {
        element.attrib["IdType"]: element.text
        for element in entry.findall("PubmedData/ArticleIdList/ArticleId")
    }
    notices = [
        {
            "type": element.attrib.get("RefType"),
            "pmid": element.findtext("PMID"),
            "citation": element.findtext("RefSource"),
        }
        for element in entry.findall("MedlineCitation/CommentsCorrectionsList/CommentsCorrections")
    ]
    return {
        "pmid": pmid,
        "title": title,
        "abstract": abstract,
        "journal": journal,
        "year": year,
        "authors": authors,
        "doi": identifiers.get("doi"),
        "pmcid": identifiers.get("pmc"),
        "publication_types": [
            element.text for element in article.findall("PublicationTypeList/PublicationType")
        ],
        "notices": notices,
    }


def render_md(pmid: str, data: dict) -> str:
    md = [f"# PMID:{pmid}"]
    md.append("")
    if data["title"]:
        md.append(f"**Title:** {data['title']}")
    if data["authors"]:
        md.append(f"**Authors:** {', '.join(data['authors'])}")
    if data["journal"]:
        md.append(f"**Journal:** {data['journal']}")
    if data["year"]:
        md.append(f"**Year:** {data['year']}")
    if data.get("doi"):
        md.append(f"**DOI:** {data['doi']}")
    if data.get("pmcid"):
        md.append(f"**PMCID:** {data['pmcid']}")
    md.append(f"**Source:** https://pubmed.ncbi.nlm.nih.gov/{pmid}/")
    md.append("**Content:** PubMed abstract, not the article full text")
    for notice in data.get("notices", []):
        md.append(
            f"**Related notice:** {notice['type']} PMID:{notice['pmid']} {notice['citation'] or ''}"
        )
    md.append("")
    md.append("## Abstract")
    md.append("")
    md.append(data["abstract"] or "*(No abstract)*")
    md.append("")
    return "\n".join(md)


def write_md(pmid: str, data: dict) -> None:
    metadata = {
        "reference_id": f"PMID:{pmid}",
        **{key: data.get(key) for key in ("title", "authors", "journal", "year", "doi")},
        "content_type": "abstract_only",
        "full_text_attempted": False,
    }
    text = "---\n" + yaml.safe_dump(metadata, sort_keys=False, allow_unicode=True)
    text += "---\n\n# " + data["title"] + "\n\n## Content\n\n" + data["abstract"] + "\n"
    cache_path(pmid).write_text(text, encoding="utf-8")


def ensure_validator_cache(pmid: str, data: dict) -> None:
    """Upgrade only this tool's old cache rendering; preserve other/full-text caches."""
    path = cache_path(pmid)
    if not path.exists() or path.read_bytes() == render_md(pmid, data).encode("utf-8"):
        write_md(pmid, data)


def archive_paths(pmid: str) -> tuple[Path, Path, Path]:
    directory = CACHE_DIR / "papers"
    return tuple(directory / f"PMID_{pmid}.{suffix}" for suffix in ("xml", "md", "json"))


def verified_archive(pmid: str) -> dict | None:
    raw_path, md_path, metadata_path = archive_paths(pmid)
    if not metadata_path.exists():
        return None
    metadata = json.loads(metadata_path.read_text())
    for path, key in ((raw_path, "raw_sha256"), (md_path, "markdown_sha256")):
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != metadata[key]:
            raise ValueError(f"archive hash mismatch: {path}")
    data = parse_abstract(raw_path.read_bytes(), pmid)
    if md_path.read_text() != render_md(pmid, data):
        raise ValueError("Markdown does not match archived XML conversion")
    if metadata.get("pmid") != pmid:
        raise ValueError("archive metadata PMID mismatch")
    for key in (
        "title",
        "authors",
        "journal",
        "year",
        "doi",
        "pmcid",
        "publication_types",
        "notices",
    ):
        if metadata.get(key) != data[key]:
            raise ValueError(f"archive metadata does not match XML: {key}")
    if metadata.get("has_abstract") is not bool(data["abstract"]):
        raise ValueError("archive abstract coverage does not match XML")
    return metadata


def fetch_one(pmid: str, api_key: str | None) -> str:
    """Preserve raw XML plus derived Markdown; never trust an orphan MD cache."""
    if not PMID_RE.fullmatch(pmid):
        return "error:invalid PMID"
    try:
        metadata = verified_archive(pmid)
        if metadata:
            ensure_validator_cache(pmid, parse_abstract(archive_paths(pmid)[0].read_bytes(), pmid))
            return "cached" if metadata["has_abstract"] else "metadata_only"
        raw_path, md_path, metadata_path = archive_paths(pmid)
        recovered_raw = raw_path.exists()
        raw = fetch_pubmed_xml(pmid, api_key)
        if recovered_raw and raw_path.read_bytes() != raw:
            raise ValueError("unverified orphan XML differs from the current source")
        data = parse_abstract(raw, pmid)
        markdown = render_md(pmid, data).encode("utf-8")
        raw_path.parent.mkdir(parents=True, exist_ok=True)
        # Keep the upstream response immutable; a partial conversion is resumable.
        if not raw_path.exists():
            with raw_path.open("xb") as stream:
                stream.write(raw)
        md_path.write_bytes(markdown)
        metadata = {
            **data,
            "abstract": None,
            "has_abstract": bool(data["abstract"]),
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "archived_at": datetime.now(timezone.utc).isoformat(),
            "source_url": f"{EUTILS}?db=pubmed&id={pmid}&retmode=xml&rettype=abstract",
            "raw_sha256": hashlib.sha256(raw).hexdigest(),
            "markdown_sha256": hashlib.sha256(markdown).hexdigest(),
            "conversion": "pubmed-xml-to-markdown-v1",
        }
        metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
        ensure_validator_cache(pmid, data)
        return "fetched" if data["abstract"] else "metadata_only"
    except urllib.error.HTTPError as e:
        return f"error:HTTP {e.code}"
    except Exception as e:
        return f"error:{type(e).__name__}"


def parse_doi_search(raw: bytes) -> tuple[int, list[str]]:
    """Reject transient error pages before they can become durable search caches."""
    root = ET.fromstring(raw)
    if (
        root.tag != "eSearchResult"
        or root.find("ERROR") is not None
        or root.find("ErrorList") is not None
    ):
        raise ValueError("invalid DOI search response")
    count = int(root.findtext("Count", "-1"))
    ids = [node.text or "" for node in root.findall("IdList/Id")]
    if count < 0 or any(not PMID_RE.fullmatch(pmid) for pmid in ids):
        raise ValueError("invalid DOI search count or PMID")
    return count, ids


def resolve_doi(reference: str, api_key: str | None, delay: float) -> dict:
    """Resolve a DOI only when the archived PubMed article repeats that exact DOI."""
    canonical = publication_reference(reference)
    if not canonical or not canonical.startswith("doi:"):
        return {"status": "invalid_doi"}
    doi = canonical[4:]
    try:
        matching = set()
        for path in sorted((CACHE_DIR / "papers").glob("PMID_*.json")):
            pmid = path.stem.removeprefix("PMID_")
            metadata = verified_archive(pmid)
            if metadata and str(metadata.get("doi") or "").lower() == doi:
                matching.add(pmid)
        if not matching:
            directory = CACHE_DIR / "papers" / "doi_searches"
            token = hashlib.sha256(doi.encode()).hexdigest()
            raw_path = directory / f"{token}.xml"
            provenance_path = directory / f"{token}.json"
            url = (
                "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?"
                + urllib.parse.urlencode(
                    {
                        "db": "pubmed",
                        "term": f'"{doi}"[AID]',
                        "retmode": "xml",
                        "retmax": 10,
                    }
                )
            )
            if raw_path.exists():
                raw = raw_path.read_bytes()
                provenance = json.loads(provenance_path.read_text())
                if (
                    provenance["doi"] != doi
                    or provenance["sha256"] != hashlib.sha256(raw).hexdigest()
                ):
                    raise ValueError("DOI search cache mismatch")
                count, ids = parse_doi_search(raw)
            else:
                request_url = url
                if api_key:
                    request_url += "&" + urllib.parse.urlencode({"api_key": api_key})
                raw = fetch_bytes(request_url)
                time.sleep(delay)
                count, ids = parse_doi_search(raw)
                directory.mkdir(parents=True, exist_ok=True)
                raw_path.write_bytes(raw)
                provenance_path.write_text(
                    json.dumps(
                        {
                            "doi": doi,
                            "url": url,
                            "retrieved_at": datetime.now(timezone.utc).isoformat(),
                            "sha256": hashlib.sha256(raw).hexdigest(),
                        },
                        indent=2,
                    )
                    + "\n"
                )
            if count != len(ids):
                return {"status": "ambiguous_or_truncated_search", "count": count}
            for pmid in ids:
                outcome = fetch_one(pmid, api_key)
                if outcome.startswith("error"):
                    return {"status": "archive_error", "pmid": pmid, "detail": outcome}
                metadata = verified_archive(pmid)
                if str(metadata.get("doi") or "").lower() == doi:
                    matching.add(pmid)
                time.sleep(delay)
        if not matching:
            return {"status": "unresolved_in_pubmed", "doi": doi}
        if len(matching) != 1:
            return {"status": "ambiguous_doi", "pmids": sorted(matching)}
        pmid = matching.pop()
        metadata = verified_archive(pmid)
        raw_path, md_path, _ = archive_paths(pmid)
        return {
            "status": "archived" if metadata["has_abstract"] else "metadata_only",
            "pmid": pmid,
            "raw": raw_path.relative_to(REPO_ROOT).as_posix(),
            "markdown": md_path.relative_to(REPO_ROOT).as_posix(),
            "raw_sha256": metadata["raw_sha256"],
            "markdown_sha256": metadata["markdown_sha256"],
        }
    except Exception as error:
        return {"status": "resolution_error", "detail": type(error).__name__}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmids", nargs="*", help="explicit PMIDs to fetch (skips harvest)")
    ap.add_argument(
        "--dois", nargs="+", help="explicit DOIs to resolve and archive (skips harvest)"
    )
    ap.add_argument(
        "--resolve-dois", action="store_true", help="also resolve cited DOIs through PubMed"
    )
    ap.add_argument(
        "--limit", type=int, default=None, help="cap how many missing PMIDs to fetch this run"
    )
    ap.add_argument(
        "--rate", type=float, default=None, help="req/s (default: 3.0, or 10.0 with NCBI_API_KEY)"
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="harvest + report counts, do not hit NCBI"
    )
    ap.add_argument(
        "--report", type=Path, help="save corpus citation inventory and archival outcomes as JSON"
    )
    args = ap.parse_args()

    api_key = os.environ.get("NCBI_API_KEY")
    rate = args.rate if args.rate is not None else (KEYED_RATE if api_key else DEFAULT_RATE)
    if not math.isfinite(rate) or rate <= 0 or rate > (KEYED_RATE if api_key else DEFAULT_RATE):
        ap.error("rate must be positive and no higher than the NCBI limit")
    if args.limit is not None and args.limit < 0:
        ap.error("limit must be nonnegative")
    sleep_time = 1.0 / rate
    inventory = {"records": [], "references": {}}
    if args.pmids or args.dois:
        pmids = set(args.pmids or [])
        if not all(PMID_RE.fullmatch(pmid) for pmid in pmids):
            ap.error("--pmids requires numeric identifiers")
        print(f"Using {len(pmids)} explicit PMIDs from command line")
        for value in args.dois or []:
            reference = publication_reference(value)
            if not reference or not reference.startswith("doi:"):
                ap.error("--dois requires DOI identifiers")
            inventory["references"][reference] = []
    else:
        inventory = citation_inventory()
        pmids = {ref[5:] for ref in inventory["references"] if ref.startswith("PMID:")}
        print(f"Harvested {len(pmids)} unique PMIDs from CultureMech YAMLs")
    report = {
        **inventory,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scope": "explicit_identifiers" if args.pmids or args.dois else "tracked_normalized_corpus",
        "scientific_review": False,
        "outcomes": {},
        "doi_pending": sorted(ref for ref in inventory["references"] if ref.startswith("doi:")),
        "doi_outcomes": {},
    }
    if args.dry_run:
        print(
            f"Dry run: {len(pmids)} PMIDs; {len(report['doi_pending'])} DOI identifiers need separate resolution."
        )
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, indent=2) + "\n")
        return 0
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    fetched = errors = metadata_only = 0
    selected = []
    for pmid in sorted(pmids, key=int):
        if archive_paths(pmid)[2].exists():
            result = fetch_one(pmid, api_key)
            report["outcomes"][f"PMID:{pmid}"] = result
            errors += result.startswith("error")
            metadata_only += result == "metadata_only"
        else:
            selected.append(pmid)
    if args.limit is not None:
        selected = selected[: args.limit]
    report["not_attempted"] = [
        f"PMID:{pmid}"
        for pmid in sorted(pmids, key=int)
        if pmid not in selected and f"PMID:{pmid}" not in report["outcomes"]
    ]
    for i, pmid in enumerate(selected, 1):
        result = fetch_one(pmid, api_key)
        report["outcomes"][f"PMID:{pmid}"] = result
        if result == "fetched":
            fetched += 1
        elif result.startswith("error"):
            errors += 1
        elif result == "metadata_only":
            metadata_only += 1
        print(f"  [{i}/{len(selected)}] PMID:{pmid}: {result}", flush=True)
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, indent=2) + "\n")
        if result != "cached":
            time.sleep(sleep_time)
    if args.resolve_dois or args.dois:
        for reference in list(report["doi_pending"]):
            outcome = resolve_doi(reference, api_key, sleep_time)
            report["doi_outcomes"][reference] = outcome
            print(f"  {reference}: {outcome['status']}", flush=True)
            if outcome["status"] == "archived":
                report["doi_pending"].remove(reference)
            else:
                errors += 1
            if args.report:
                args.report.parent.mkdir(parents=True, exist_ok=True)
                args.report.write_text(json.dumps(report, indent=2) + "\n")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(f"\nFetched: {fetched}  Metadata only: {metadata_only}  Errors: {errors}")
    return 0 if errors == 0 and metadata_only == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
