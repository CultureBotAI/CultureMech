"""Validate that generated web artifacts cover their declared recipe corpus."""

from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path, PurePosixPath
from typing import Any

DATA_PREFIX = "window.culturemechData = "
DATA_SUFFIX = ";\n\n// Dispatch event"


def load_browser_data(path: Path) -> list[dict[str, Any]]:
    """Parse the JSON payload from the generated external JavaScript file."""
    content = path.read_text()
    start = content.find(DATA_PREFIX)
    end = content.find(DATA_SUFFIX, start)
    if start < 0 or end < 0:
        raise ValueError(f"unrecognized browser data format: {path}")
    payload = json.loads(content[start + len(DATA_PREFIX) : end])
    if not isinstance(payload, list) or not all(isinstance(item, dict) for item in payload):
        raise ValueError(f"browser data must be a list of records: {path}")
    return payload


def validate_web_coverage(corpus_dir: Path, data_file: Path, pages_dir: Path) -> list[str]:
    """Return coverage errors across source YAML, browser data, and HTML pages."""
    source_files = {path.relative_to(corpus_dir).as_posix() for path in corpus_dir.rglob("*.yaml")}
    records = load_browser_data(data_file)
    browser_sources = {str(record.get("source_file", "")) for record in records}
    errors: list[str] = []

    if len(records) != len(source_files):
        errors.append(f"record count differs: corpus={len(source_files)}, browser={len(records)}")
    missing_sources = sorted(source_files - browser_sources)
    stale_sources = sorted(browser_sources - source_files)
    if missing_sources:
        errors.append(
            f"browser data misses {len(missing_sources)} source file(s): {missing_sources[:5]}"
        )
    if stale_sources:
        errors.append(
            f"browser data has {len(stale_sources)} stale source file(s): {stale_sources[:5]}"
        )

    expected_pages: set[str] = set()
    for record in records:
        link = str(record.get("html_page", ""))
        relative = PurePosixPath(link)
        if not link or relative.is_absolute() or ".." in relative.parts:
            errors.append(f"unsafe or missing html_page for {record.get('id')}: {link!r}")
            continue
        expected_pages.add(relative.as_posix())

    if len(expected_pages) != len(records):
        errors.append(
            f"page links are not unique: records={len(records)}, links={len(expected_pages)}"
        )

    page_roots = {PurePosixPath(link).parts[0] for link in expected_pages}
    actual_pages = {
        path.relative_to(pages_dir).as_posix()
        for root in page_roots
        for path in (pages_dir / root).rglob("*.html")
        if path.name != "index.html"
    }
    missing_pages = sorted(expected_pages - actual_pages)
    stale_pages = sorted(actual_pages - expected_pages)
    if missing_pages:
        errors.append(f"missing {len(missing_pages)} rendered page(s): {missing_pages[:5]}")
    if stale_pages:
        errors.append(f"found {len(stale_pages)} stale rendered page(s): {stale_pages[:5]}")
    return errors


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-dir", type=Path, default=Path("data/normalized_yaml"))
    parser.add_argument("--data-file", type=Path, default=Path("app/data.js"))
    parser.add_argument("--pages-dir", type=Path, default=Path("pages"))
    args = parser.parse_args(argv)

    errors = validate_web_coverage(args.corpus_dir, args.data_file, args.pages_dir)
    if errors:
        for error in errors:
            print(f"error: {error}")
        return 1
    count = len(list(args.corpus_dir.rglob("*.yaml")))
    print(f"web artifact coverage is complete for {count} recipes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
