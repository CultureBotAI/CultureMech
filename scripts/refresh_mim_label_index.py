#!/usr/bin/env python3
"""Refresh the vendored MIM label index from one immutable Git commit.

This is an explicit dependency bump, not part of ordinary builds.  It requires
a full 40-character SHA, validates the downloaded artifact before writing, and
reports semantic answer changes for review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

from culturemech.ingredients.mim_label_index import (
    CONTRACT_VERSION,
    INDEX_HEADER,
    MIM_REPOSITORY,
    MIM_SOURCE_PATH,
    MIMLabelIndex,
)

REPO_ROOT = Path(__file__).resolve().parent.parent
RESOURCE_DIR = REPO_ROOT / "src" / "culturemech" / "data" / "mediaingredientmech"
INDEX_PATH = RESOURCE_DIR / "label_index.csv"
METADATA_PATH = RESOURCE_DIR / "label_index.metadata.json"
RAW_URL = (
    "https://raw.githubusercontent.com/CultureBotAI/MediaIngredientMech/{commit}/" + MIM_SOURCE_PATH
)
FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")


def download(commit: str) -> bytes:
    """Download the publisher artifact at an immutable revision."""

    url = RAW_URL.format(commit=commit)
    request = urllib.request.Request(url, headers={"User-Agent": "CultureMech-MIM-pin-refresh"})
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return bytes(response.read())
    except (urllib.error.URLError, TimeoutError) as exc:
        raise SystemExit(f"failed to download {url}: {exc}") from exc


def build_metadata(commit: str, data: bytes, row_count: int) -> dict[str, object]:
    """Build deterministic provenance and integrity metadata."""

    return {
        "byte_count": len(data),
        "consumer_contract_version": CONTRACT_VERSION,
        "data_row_count": row_count,
        "header": list(INDEX_HEADER),
        "repository": MIM_REPOSITORY,
        "sha256": hashlib.sha256(data).hexdigest(),
        "source_commit": commit,
        "source_path": MIM_SOURCE_PATH,
    }


def semantic_delta(
    old: MIMLabelIndex, new: MIMLabelIndex
) -> tuple[list[str], list[str], list[str]]:
    """Return added, removed, and changed normalized label keys."""

    old_answers = old.semantic_answers()
    new_answers = new.semantic_answers()
    added = sorted(new_answers.keys() - old_answers.keys())
    removed = sorted(old_answers.keys() - new_answers.keys())
    changed = sorted(
        key
        for key in old_answers.keys() & new_answers.keys()
        if old_answers[key] != new_answers[key]
    )
    return added, removed, changed


def _atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _display(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def refresh(commit: str, data: bytes, *, apply: bool = False) -> tuple[int, int, int]:
    """Validate, report impact, and optionally replace the vendored pin."""

    if not FULL_SHA.fullmatch(commit):
        raise SystemExit("commit must be a full lowercase 40-character Git SHA")

    new_unverified = MIMLabelIndex.from_csv_bytes(data)
    metadata = build_metadata(commit, data, len(new_unverified.rows))
    new = MIMLabelIndex.from_csv_bytes(data, metadata=metadata, verify_metadata=True)
    old = MIMLabelIndex.from_paths(INDEX_PATH, METADATA_PATH)
    added, removed, changed = semantic_delta(old, new)

    print(
        f"MIM pin {old.metadata['source_commit']} -> {commit}: "
        f"labels +{len(added)} -{len(removed)} changed={len(changed)}"
    )
    for kind, labels in (("ADDED", added), ("REMOVED", removed), ("CHANGED", changed)):
        for label in labels[:20]:
            print(f"{kind}\t{label}")
        if len(labels) > 20:
            print(f"{kind}\t... {len(labels) - 20} more")

    if not apply:
        print("Preview only: vendored artifact not changed. Pass --apply to update the pin.")
        return len(added), len(removed), len(changed)

    metadata_bytes = (json.dumps(metadata, indent=2, sort_keys=True) + "\n").encode("utf-8")
    old_data = INDEX_PATH.read_bytes()
    old_metadata = METADATA_PATH.read_bytes()
    try:
        _atomic_write(INDEX_PATH, data)
        _atomic_write(METADATA_PATH, metadata_bytes)
        MIMLabelIndex.from_paths(INDEX_PATH, METADATA_PATH)
    except Exception:
        # A two-file dependency update must not intentionally leave one half of
        # the old pin beside one half of the new pin.
        _atomic_write(INDEX_PATH, old_data)
        _atomic_write(METADATA_PATH, old_metadata)
        raise
    print(f"Updated {_display(INDEX_PATH)} and {_display(METADATA_PATH)}")
    return len(added), len(removed), len(changed)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("commit", help="full immutable MediaIngredientMech Git SHA")
    parser.add_argument(
        "--apply", action="store_true", help="replace the vendored artifact after validation"
    )
    args = parser.parse_args()

    if not FULL_SHA.fullmatch(args.commit):
        parser.error("commit must be a full lowercase 40-character Git SHA")
    refresh(args.commit, download(args.commit), apply=args.apply)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
