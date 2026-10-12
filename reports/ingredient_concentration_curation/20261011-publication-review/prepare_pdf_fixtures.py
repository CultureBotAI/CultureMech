"""Promote hash-verified PDFs used by review guards and independent audits."""

import base64
import hashlib
import importlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MODULES = (
    "repair_allisonella_acids",
    "repair_desulfurobacterium_family",
    "repair_linked_middlebrook",
    "repair_methanobacterium_family",
    "repair_methanofollis_family",
    "repair_middlebrook_stages",
    "repair_oteb_family",
    "repair_rumen_bacteria_family",
    "repair_ruminococcus_albus_family",
    "repair_synthrophomonas_family",
)


def main():
    fixtures = {}
    contexts = []
    for name in MODULES:
        context = importlib.import_module(name).frozen()
        if isinstance(context, tuple):
            context = context[0]
        contexts.append(context)
    # Resazurin reuses captures above; medium323 has one additional PDF.
    path = (
        ROOT
        / "reports/ingredient_concentration_curation/20261009-synthrophomonas-family/next-323-captures-approved.json"
    )
    raw = path.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "8c802303cf38982bebc07777a71a7d2dab5d4c01d44c0cc1d1c8136d866a39a4"
    )
    contexts.append(json.loads(raw))
    for context in contexts:
        for capture in context["sources"].values():
            meta = capture["metadata"]
            if not meta.get("pdf_path"):
                continue
            path = (ROOT / meta["pdf_path"]).resolve()
            assert path.is_relative_to(ROOT / "references_cache"), path
            payload = path.read_bytes()
            digest = hashlib.sha256(payload).hexdigest()
            assert digest == meta["pdf_sha256"] and payload.startswith(b"%PDF-")
            assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
            fixture = {
                key: meta[key]
                for key in ("url", "response_url", "http_status", "accessed_at", "pdf_sha256")
            }
            fixture["pdf_base64"] = base64.b64encode(payload).decode("ascii")
            if digest in fixtures:
                assert fixtures[digest]["url"] == fixture["url"]
            else:
                fixtures[digest] = fixture
    output = ROOT / "tests/fixtures/curation_pdfs"
    for digest, fixture in sorted(fixtures.items()):
        path = output / f"{digest}.json"
        if path.exists():
            assert json.loads(path.read_text()) == fixture
        else:
            with path.open("x") as stream:
                stream.write(json.dumps(fixture, indent=2) + "\n")
    print(
        json.dumps(
            {
                "fixtures": len(fixtures),
                "bytes": sum(p.stat().st_size for p in output.glob("*.json")),
            }
        )
    )


if __name__ == "__main__":
    main()
