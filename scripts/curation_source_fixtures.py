"""Read immutable curation PDF fixtures without relying on ignored caches."""

from __future__ import annotations

import base64
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_pdf_capture(metadata: dict, *, root: Path = ROOT) -> bytes:
    """Resolve an inspected PDF by digest; keep historical cache paths unchanged."""
    digest = metadata.get("pdf_sha256", "")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ValueError("Invalid PDF fixture digest")
    path = root / "tests/fixtures/curation_pdfs" / f"{digest}.json"
    fixture = json.loads(path.read_text(encoding="utf-8"))
    if (
        fixture.get("pdf_sha256") != digest
        or fixture.get("url") != metadata.get("url")
        or fixture.get("http_status") != 200
        or fixture.get("response_url") != fixture.get("url")
    ):
        raise ValueError("PDF fixture provenance mismatch")
    payload = base64.b64decode(fixture["pdf_base64"], validate=True)
    if not payload.startswith(b"%PDF-") or hashlib.sha256(payload).hexdigest() != digest:
        raise ValueError("PDF fixture content mismatch")
    return payload
