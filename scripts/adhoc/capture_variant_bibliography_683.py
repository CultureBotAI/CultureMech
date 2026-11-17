#!/usr/bin/env python3
"""Capture an exact primary citation anonymously for variant review (2026-11-16).

Inputs: one explicit PMID or DOI and a new ignored output directory.
Outputs: Europe PMC metadata/abstract, available full XML, and hash receipts.
Serves CultureMech #683; no scientific inference, credentials or recipe edits.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


def retrieve(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "CultureMech-source-review/1.0"})
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--pmid")
    group.add_argument("--doi")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if args.output_dir.exists() or args.output_dir.is_symlink():
        parser.error("output directory must be new")
    query = f"EXT_ID:{args.pmid} AND SRC:MED" if args.pmid else f'DOI:"{args.doi}"'
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": query, "resultType": "core", "format": "json", "pageSize": 10}
    )
    raw = retrieve(url)
    hits = json.loads(raw).get("resultList", {}).get("result", [])
    exact = (
        [
            item
            for item in hits
            if (item.get("id") == args.pmid and item.get("source") == "MED")
            if args.pmid
        ]
        if args.pmid
        else [item for item in hits if item.get("doi", "").lower() == args.doi.lower()]
    )
    if len(exact) != 1:
        raise ValueError(f"expected one exact citation, received {len(exact)}")
    record = exact[0]
    args.output_dir.mkdir(parents=True, exist_ok=False)
    (args.output_dir / "metadata.json").write_bytes(raw)
    text = "\n\n".join(
        str(record.get(key, "")) for key in ("title", "doi", "pmid", "pmcid", "abstractText")
    )
    (args.output_dir / "abstract.txt").write_text(text + "\n", encoding="utf-8")
    receipt = {
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "metadata_url": url,
        "metadata_sha256": hashlib.sha256(raw).hexdigest(),
        "title": record.get("title"),
        "doi": record.get("doi"),
        "pmid": record.get("id"),
        "pmcid": record.get("pmcid"),
        "scientific_review": False,
        "full_text_status": "not_available",
    }
    pmcid = record.get("pmcid")
    if pmcid:
        full_url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
        try:
            full = retrieve(full_url)
            document = ET.fromstring(full)
            if document.tag != "article":
                raise ValueError("not an article XML document")
            (args.output_dir / "source.xml").write_bytes(full)
            blocks = document.findall(".//article-title") + document.findall(".//sec/title")
            blocks += document.findall(".//p") + document.findall(".//table-wrap")
            inspection = "\n\n".join(
                " ".join("".join(block.itertext()).split()) for block in blocks
            )
            (args.output_dir / "inspection.txt").write_text(inspection + "\n", encoding="utf-8")
            receipt.update(
                full_text_status="captured",
                url=full_url,
                sha256=hashlib.sha256(full).hexdigest(),
                bytes=len(full),
            )
        except (urllib.error.URLError, ET.ParseError, ValueError) as exc:
            receipt["full_text_status"] = "retrieval_failed"
            receipt["failure_class"] = type(exc).__name__
    (args.output_dir / "receipt.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
