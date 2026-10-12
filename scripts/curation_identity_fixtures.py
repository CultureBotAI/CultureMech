"""Replay historical identity evidence against its original, verified MIM pin."""

from __future__ import annotations

import base64
import hashlib
import json
from pathlib import Path

from culturemech.ingredients.mim_label_index import MIMLabelIndex

ROOT = Path(__file__).resolve().parents[1]
CAPTURE_SHA256 = {
    "a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262": "491958135a662b7d6bb7935784964449e77d90ea61d6a94130b00c41e050d65a"
}


def read_mim_capture(digest: str, *, root: Path = ROOT) -> MIMLabelIndex:
    """Never substitute the current package index for an historical audit input."""
    if not isinstance(digest, str) or digest not in CAPTURE_SHA256:
        raise ValueError("Unregistered historical MIM digest")
    root = root.resolve()
    path = root / "tests/fixtures/curation_mim" / f"{digest}.json"
    if any(p.is_symlink() for p in (path, *path.parents) if p != root and p.is_relative_to(root)):
        raise ValueError("Historical MIM fixture symlink")
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != CAPTURE_SHA256[digest]:
        raise ValueError("Historical MIM capture drift")
    capture = json.loads(raw)
    if capture["metadata"]["sha256"] != digest:
        raise ValueError("Historical MIM metadata drift")
    return MIMLabelIndex.from_csv_bytes(
        base64.b64decode(capture["csv_base64"], validate=True),
        metadata=capture["metadata"],
        verify_metadata=True,
    )
