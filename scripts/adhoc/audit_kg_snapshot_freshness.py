#!/usr/bin/env python3
"""Read-only freshness audit for CultureMech release tracker #687 (2026-11-13).

Inputs: frozen MIM KG source-manifest.json and explicitly selected current KG roots.
Output: JSON on stdout with frozen-copy integrity and current per-file byte hashes.
Only declared paths are inspected, including ignored files. No inputs are changed,
downloads performed, transforms executed, or completeness beyond those paths claimed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def digest_file(path: Path) -> dict:
    try:
        before = path.stat()
        digest = hashlib.sha256()
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
        after = path.stat()
    except OSError as error:
        return {
            "state": "MISSING" if isinstance(error, FileNotFoundError) else "READ_ERROR",
            "error": str(error),
        }
    stable = (before.st_ino, before.st_size, before.st_mtime_ns) == (
        after.st_ino,
        after.st_size,
        after.st_mtime_ns,
    )
    return {
        "state": "READ" if stable else "CHANGED_DURING_READ",
        "sha256": digest.hexdigest(),
        "bytes": after.st_size,
    }


def git_head(root: Path) -> str | None:
    result = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def compare(root: Path, entries: dict) -> dict:
    results = []
    for relative, expected in sorted(entries.items()):
        if any(part in {"", ".", ".."} for part in relative.split("/")) or "\\" in relative:
            raise ValueError(f"unsafe manifest path: {relative!r}")
        observed = digest_file(root / relative)
        if observed["state"] == "READ":
            observed["state"] = (
                "MATCH"
                if observed["sha256"] == expected["sha256"]
                and observed["bytes"] == expected["bytes"]
                else "DIFFERENT"
            )
        results.append({"path": relative, "expected": expected, "observed": observed})
    counts = {
        state: sum(row["observed"]["state"] == state for row in results)
        for state in ("MATCH", "DIFFERENT", "MISSING", "READ_ERROR", "CHANGED_DURING_READ")
    }
    return {"root": str(root), "declared_files": len(entries), "counts": counts, "files": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-manifest", required=True, type=Path)
    parser.add_argument("--current-root", required=True, action="append", type=Path)
    args = parser.parse_args()
    raw = args.source_manifest.read_bytes()
    manifest = json.loads(raw)
    entries = manifest["files"]
    snapshots = {
        path.removeprefix("snapshots/"): record
        for path, record in entries.items()
        if path.startswith("snapshots/")
    }
    if not entries or not snapshots:
        parser.error("manifest must declare nonempty files and snapshots/")
    report = {
        "schema_version": 1,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "source_manifest": str(args.source_manifest),
        "source_manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "frozen_captured_at": manifest["captured_at"],
        "frozen_upstream_revision": manifest["upstream_revision"],
        "scope": "Only manifest-declared paths; current root may be a different Git revision.",
        "limitations": [
            "Does not discover newly created sources or determine latest upstream data.",
            "Does not establish scientific mapping approval or final SSSOM readiness.",
            "Per-file stability and Git HEAD checks do not constitute an atomic filesystem snapshot.",
        ],
        "frozen_copies": compare(args.source_manifest.parent, entries),
        "current_roots": [],
    }
    for root in args.current_root:
        before = git_head(root)
        comparison = compare(root, snapshots)
        comparison["git_head_before"] = before
        comparison["git_head_after"] = git_head(root)
        report["current_roots"].append(comparison)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
