#!/usr/bin/env python3
"""Capture an anonymous primary source for variant curation (#683, 2026-11-16).

Inputs: one explicit HTTPS URL, source format and new output directory.
Outputs: original source bytes, inspection text and URL/hash/time receipt.
No credential use, scientific inference, recipe edits or existing-file overwrite.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


class InspectionText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.suppressed = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.suppressed += 1
        if tag in {"p", "div", "section", "tr", "br", "h1", "h2", "h3", "li"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style"} and self.suppressed:
            self.suppressed -= 1

    def handle_data(self, data):
        if not self.suppressed:
            self.parts.append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--format", choices=["xml", "html", "pdf"], required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    url = urllib.parse.urlsplit(args.url)
    if url.scheme != "https" or url.username or url.password or not url.hostname:
        parser.error("an explicit HTTPS URL without user information is required")
    if args.output_dir.exists() or args.output_dir.is_symlink():
        parser.error("output directory must be new")
    request = urllib.request.Request(
        args.url, headers={"User-Agent": "CultureMech-source-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        raw = response.read()
        final_url = response.url
        content_type = response.headers.get("Content-Type", "")
    if not raw:
        raise ValueError("source response is empty")
    if args.format == "pdf" and not raw.startswith(b"%PDF"):
        raise ValueError("response is not a PDF")
    if args.format == "xml":
        document = ET.fromstring(raw)
        if document.tag not in {"article", "pmc-articleset"}:
            raise ValueError("expected an article XML document")
        blocks = document.findall(".//article-title") + document.findall(".//sec/title")
        blocks += document.findall(".//p") + document.findall(".//table-wrap")
        inspection = "\n\n".join(" ".join("".join(block.itertext()).split()) for block in blocks)
    elif args.format == "html":
        document = InspectionText()
        document.feed(raw.decode("utf-8"))
        inspection = "".join(document.parts)
    args.output_dir.mkdir(parents=True, exist_ok=False)
    source = args.output_dir / f"source.{args.format}"
    source.write_bytes(raw)
    extracted = args.output_dir / "inspection.txt"
    if args.format == "pdf":
        subprocess.run(["pdftotext", "-layout", str(source), str(extracted)], check=True)
    else:
        extracted.write_text(inspection + "\n", encoding="utf-8")
    if not extracted.stat().st_size:
        raise ValueError("inspection text is empty; original source retained")
    receipt = {
        "url": args.url,
        "response_url": final_url,
        "content_type": content_type,
        "retrieved_at": datetime.now(timezone.utc).isoformat(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "inspection_sha256": hashlib.sha256(extracted.read_bytes()).hexdigest(),
        "scientific_review": False,
        "limitation": "Extraction aids inspection; original bytes are authoritative. No claim verified by retrieval.",
    }
    (args.output_dir / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
