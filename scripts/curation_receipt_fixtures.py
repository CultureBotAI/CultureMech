"""Resolve historical validation receipts by digest, never by workstation path."""

from __future__ import annotations

import base64
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def receipt_name(recorded_path: str) -> str:
    if not isinstance(recorded_path, str):
        raise ValueError("Invalid curation receipt path")
    parts = PurePosixPath(recorded_path).parts
    starts = [
        i
        for i in range(len(parts) - 1)
        if parts[i : i + 2] == ("reports", "ingredient_concentration_curation")
    ]
    if ".." in parts or len(starts) != 1:
        raise ValueError("Invalid curation receipt path")
    return PurePosixPath(*parts[starts[0] :]).as_posix()


def read_receipt_capture(recorded_path: str, digest: str, *, root: Path = ROOT) -> bytes:
    """Retain exact historical bytes while relocating only a registered receipt."""
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ValueError("Invalid curation receipt digest")
    name = receipt_name(recorded_path)
    root = root.resolve()
    path = root / "tests/fixtures/curation_receipts" / f"{digest}.json"
    if any(p.is_symlink() for p in (path, *path.parents) if p != root and p.is_relative_to(root)):
        raise ValueError("Curation receipt fixture symlink")
    try:
        fixture = json.loads(path.read_text(encoding="utf-8"))
        if (
            fixture["sha256"] != digest
            or not isinstance(fixture["source_paths"], list)
            or name not in fixture["source_paths"]
        ):
            raise ValueError("Curation receipt provenance mismatch")
        raw = base64.b64decode(fixture["payload_base64"], validate=True)
        if hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError("Curation receipt content mismatch")
        return raw
    except (OSError, KeyError, TypeError, ValueError) as error:
        raise ValueError("Invalid or unavailable curation receipt fixture") from error
