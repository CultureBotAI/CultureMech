"""PDF fixture lookup must be offline, exact and independent of local captures."""

import base64
import hashlib
import importlib
import json
from pathlib import Path

import pytest
from curation_source_fixtures import read_pdf_capture


@pytest.fixture
def capture(tmp_path):
    raw = b"%PDF-1.4\nfixture for byte-integrity checks\n"
    digest = hashlib.sha256(raw).hexdigest()
    metadata = {
        "url": "https://example.org/recipe.pdf",
        "response_url": "https://example.org/recipe.pdf",
        "http_status": 200,
        "pdf_sha256": digest,
        "pdf_path": "/unavailable/local/cache/recipe.pdf",
    }
    path = tmp_path / "tests/fixtures/curation_pdfs" / f"{digest}.json"
    path.parent.mkdir(parents=True)
    fixture = {**metadata, "pdf_base64": base64.b64encode(raw).decode("ascii")}
    path.write_text(json.dumps(fixture))
    return tmp_path, metadata, path, raw


def test_reads_pinned_bytes_without_using_historical_path(capture):
    root, metadata, _, raw = capture
    assert read_pdf_capture(metadata, root=root) == raw


def test_missing_fixture_does_not_fall_back_to_cache(capture):
    root, metadata, path, raw = capture
    cache = root / "available.pdf"
    cache.write_bytes(raw)
    metadata["pdf_path"] = str(cache)
    path.unlink()
    with pytest.raises(FileNotFoundError):
        read_pdf_capture(metadata, root=root)


@pytest.mark.parametrize("digest", ["../outside", "f" * 63, "A" * 64, None, []])
def test_bad_digest_rejected_before_read(capture, digest):
    root, metadata, _, _ = capture
    metadata["pdf_sha256"] = digest
    with pytest.raises(ValueError, match="digest"):
        read_pdf_capture(metadata, root=root)


@pytest.mark.parametrize(
    "field", ["url", "response_url", "http_status", "pdf_sha256", "pdf_base64"]
)
def test_altered_fixture_fails_closed(capture, field):
    root, metadata, path, _ = capture
    fixture = json.loads(path.read_text())
    fixture[field] = "altered"
    path.write_text(json.dumps(fixture))
    with pytest.raises(ValueError):
        read_pdf_capture(metadata, root=root)


def test_reencoded_wrong_pdf_does_not_pass(capture):
    root, metadata, path, _ = capture
    fixture = json.loads(path.read_text())
    fixture["pdf_base64"] = base64.b64encode(b"%PDF-1.4\nother recipe").decode("ascii")
    path.write_text(json.dumps(fixture))
    with pytest.raises(ValueError, match="content mismatch"):
        read_pdf_capture(metadata, root=root)


@pytest.mark.parametrize(
    "name",
    [
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
    ],
)
def test_all_affected_source_readers_work_without_reference_cache(name, monkeypatch):
    module = importlib.import_module(name)
    original_open = Path.open

    def no_cache(path, *args, **kwargs):
        assert "references_cache" not in path.parts, f"Ignored cache read: {path}"
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", no_cache)
    context = module.frozen()
    if isinstance(context, tuple):
        context = context[0]
    module.sources(context)
