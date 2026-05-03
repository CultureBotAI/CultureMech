#!/usr/bin/env /opt/homebrew/bin/python3.13
"""Fetch PubMed abstracts for every PMID referenced by CultureMech recipe
YAMLs and cache them as Markdown files in
`CultureMech/references_cache/PMID_NNNNNNNN.md`.

Used as the data source for `validate_evidence_references.py`. Polite
to NCBI: 3 req/s default, supports NCBI_API_KEY env var for 10 req/s.

Ported from culturebotai-claw / MIM (anti-hallucination evidence gate)
to CultureMech as part of the growth-evidence integration plan.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "references_cache"
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

DEFAULT_RATE = 3.0  # req/s without API key
KEYED_RATE = 10.0   # with NCBI_API_KEY

PMID_RE = re.compile(r"^[0-9]+$")
PMID_REF_RE = re.compile(r"^\s*PMID\s*[:\s]\s*([0-9]+)\s*$", re.IGNORECASE)


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


def harvest_pmids() -> set[str]:
    """Walk every CultureMech recipe YAML; collect every PMID referenced
    in evidence[].reference, target_organisms[].evidence[].reference, and
    target_organisms[].growth_metrics[].evidence[].reference."""
    pmids: set[str] = set()
    if not YAML_ROOT.is_dir():
        return pmids

    for path in YAML_ROOT.rglob("*.yaml"):
        try:
            with open(path) as f:
                y = yaml.safe_load(f) or {}
        except Exception:
            continue
        if not isinstance(y, dict):
            continue

        # Top-level evidence[] (rare in CultureMech but supported)
        collect_from_evidence_list(y.get("evidence"), pmids)

        # source_data.evidence[] — the common CultureMech container
        sd = y.get("source_data")
        if isinstance(sd, dict):
            collect_from_evidence_list(sd.get("evidence"), pmids)

        # target_organisms[].evidence[] and
        # target_organisms[].growth_metrics[].evidence[]
        for tg in y.get("target_organisms") or []:
            if not isinstance(tg, dict):
                continue
            collect_from_evidence_list(tg.get("evidence"), pmids)
            for gm in tg.get("growth_metrics") or []:
                if not isinstance(gm, dict):
                    continue
                collect_from_evidence_list(gm.get("evidence"), pmids)

    return pmids


def cache_path(pmid: str) -> Path:
    return CACHE_DIR / f"PMID_{pmid}.md"


def fetch_pubmed_xml(pmid: str, api_key: str | None) -> str:
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml",
        "rettype": "abstract",
    }
    if api_key:
        params["api_key"] = api_key
    url = f"{EUTILS}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent":
        "CultureMech-evidence-validator/1.0 (https://github.com/CultureBotAI/CultureMech)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def parse_abstract(xml_text: str) -> dict:
    """Extract title, authors, journal, year, abstract from a single
    PubmedArticle XML response."""
    root = ET.fromstring(xml_text)
    article = root.find(".//PubmedArticle/MedlineCitation/Article")
    if article is None:
        return {"title": "", "abstract": "", "journal": "",
                "year": "", "authors": []}
    title_el = article.find("ArticleTitle")
    title = "".join(title_el.itertext()).strip() if title_el is not None else ""
    journal_el = article.find("Journal/Title")
    journal = journal_el.text.strip() if journal_el is not None and journal_el.text else ""
    year_el = article.find("Journal/JournalIssue/PubDate/Year")
    year = year_el.text.strip() if year_el is not None and year_el.text else ""
    abstract_parts: list[str] = []
    for ab in article.findall("Abstract/AbstractText"):
        label = ab.attrib.get("Label", "")
        text = "".join(ab.itertext()).strip()
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
    return {
        "title": title,
        "abstract": abstract,
        "journal": journal,
        "year": year,
        "authors": authors,
    }


def write_md(pmid: str, data: dict) -> None:
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
    md.append("")
    md.append("## Abstract")
    md.append("")
    md.append(data["abstract"] or "*(No abstract)*")
    md.append("")
    cache_path(pmid).write_text("\n".join(md))


def fetch_one(pmid: str, api_key: str | None) -> str:
    """Returns 'cached' / 'fetched' / 'error:<reason>'."""
    p = cache_path(pmid)
    if p.exists():
        return "cached"
    try:
        xml = fetch_pubmed_xml(pmid, api_key)
    except urllib.error.HTTPError as e:
        return f"error:HTTP {e.code}"
    except Exception as e:
        return f"error:{type(e).__name__}"
    data = parse_abstract(xml)
    write_md(pmid, data)
    return "fetched"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pmids", nargs="*",
                    help="explicit PMIDs to fetch (skips harvest)")
    ap.add_argument("--limit", type=int, default=None,
                    help="cap how many missing PMIDs to fetch this run")
    ap.add_argument("--rate", type=float, default=None,
                    help="req/s (default: 3.0, or 10.0 with NCBI_API_KEY)")
    ap.add_argument("--dry-run", action="store_true",
                    help="harvest + report counts, do not hit NCBI")
    args = ap.parse_args()

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    api_key = os.environ.get("NCBI_API_KEY")
    rate = args.rate or (KEYED_RATE if api_key else DEFAULT_RATE)
    sleep_time = 1.0 / rate

    if args.pmids:
        pmids = set(args.pmids)
        print(f"Using {len(pmids)} explicit PMIDs from command line")
    else:
        pmids = harvest_pmids()
        print(f"Harvested {len(pmids)} unique PMIDs from CultureMech YAMLs")

    missing = [p for p in sorted(pmids) if not cache_path(p).exists()]
    print(f"  cached: {len(pmids) - len(missing)}")
    print(f"  missing: {len(missing)}")
    if args.limit:
        missing = missing[: args.limit]
        print(f"  limited to: {len(missing)} this run")

    if args.dry_run:
        print("Dry run: skipping NCBI fetch.")
        return 0

    if not missing:
        print("Nothing to fetch.")
        return 0

    fetched = errors = 0
    for i, pmid in enumerate(missing, 1):
        result = fetch_one(pmid, api_key)
        if result == "fetched":
            fetched += 1
            print(f"  [{i}/{len(missing)}] PMID:{pmid} → fetched")
        elif result.startswith("error"):
            errors += 1
            print(f"  [{i}/{len(missing)}] PMID:{pmid} → {result}")
        time.sleep(sleep_time)

    print(f"\nFetched: {fetched}  Errors: {errors}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
