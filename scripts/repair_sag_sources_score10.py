#!/usr/bin/env python3
"""Normalize SAG source provenance for score-10 algae records."""

from __future__ import annotations

import argparse
import copy
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_sag_sources_score10.py"
ACTION = "NORMALIZED_SAG_SOURCE_SCORE10"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

SAG_REFERENCE = re.compile(r"^SAG:(?P<source_id>[^/]+)$")
PDF_URL = re.compile(r"^http://sagdb\.uni-goettingen\.de/culture_media/.+\.pdf$")
SAG_IMPORT = re.compile(
    r"Source ID: (?P<source_id>[^,]+), PDF URL: "
    r"(?P<pdf_url>http://sagdb\.uni-goettingen\.de/culture_media/.+?\.pdf)"
)

EXPECTED_TARGET_COUNT = 29


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _references(doc: dict[str, Any]) -> list[str]:
    rows = doc.get("references") or []
    if not isinstance(rows, list):
        raise ValueError("references is not a list")
    return [
        str(row.get("reference") or "")
        for row in rows
        if isinstance(row, dict) and row.get("reference")
    ]


def _sag_reference(refs: list[str]) -> tuple[str, str]:
    sag_refs = []
    pdf_refs = []
    for reference in refs:
        sag_match = SAG_REFERENCE.fullmatch(reference)
        if sag_match:
            sag_refs.append(sag_match.group("source_id"))
        if PDF_URL.fullmatch(reference):
            pdf_refs.append(reference)

    if len(sag_refs) != 1 or len(pdf_refs) != 1:
        raise ValueError(
            f"expected one SAG reference and one SAG PDF URL, found "
            f"{sag_refs!r} and {pdf_refs!r}"
        )
    return sag_refs[0], pdf_refs[0]


def _sag_import(doc: dict[str, Any]) -> tuple[str, str]:
    history = doc.get("curation_history") or []
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    matches: list[tuple[str, str]] = []
    for event in history:
        if not isinstance(event, dict) or event.get("curator") != "sag-import":
            continue
        match = SAG_IMPORT.search(str(event.get("notes") or ""))
        if match:
            matches.append((match.group("source_id"), match.group("pdf_url")))

    if len(matches) != 1:
        raise ValueError(f"expected one sag-import Source ID/PDF URL, found {matches!r}")
    return matches[0]


def _require_target(path: Path, doc: dict[str, Any]) -> tuple[str, str]:
    refs = _references(doc)
    source_id, pdf_url = _sag_reference(refs)
    import_source_id, import_pdf_url = _sag_import(doc)
    if (source_id, pdf_url) != (import_source_id, import_pdf_url):
        raise ValueError(
            f"{path}: SAG reference {(source_id, pdf_url)!r} does not match "
            f"sag-import {(import_source_id, import_pdf_url)!r}"
        )
    return source_id, pdf_url


def _ensure_source(doc: dict[str, Any], source_id: str, pdf_url: str) -> None:
    source = {"database": "SAG", "database_id": source_id, "url": pdf_url}
    sources = doc.setdefault("sources", [])
    if not isinstance(sources, list):
        raise ValueError("sources is not a list")
    if source not in sources:
        sources.append(source)


def _ensure_event(doc: dict[str, Any], source_id: str, pdf_url: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Normalized SAG provenance",
        "source": f"SAG:{source_id}; {pdf_url}",
        "notes": (
            "Copied the SAG source identity from references and the original "
            "sag-import event into the structured sources slot recognized by "
            "review scoring."
        ),
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    source_id, pdf_url = _require_target(path, doc)

    repaired = copy.deepcopy(doc)
    _put_after(repaired, "sources", [], "category")
    _ensure_source(repaired, source_id, pdf_url)
    _ensure_event(repaired, source_id, pdf_url)
    return repaired


def find_targets(normalized: Path = NORMALIZED) -> list[Path]:
    targets: list[Path] = []
    for path in sorted((normalized / "algae").glob("*.yaml")):
        doc = _load(path)
        refs = _references(doc)
        if any(SAG_REFERENCE.fullmatch(reference) for reference in refs):
            targets.append(path)
    if len(targets) != EXPECTED_TARGET_COUNT:
        raise ValueError(
            f"expected {EXPECTED_TARGET_COUNT} SAG algae targets, found {len(targets)}"
        )
    return targets


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {path: repair_record(path, _load(path)) for path in find_targets(normalized)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
