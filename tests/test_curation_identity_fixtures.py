"""Historical identity replay must neither drift nor fall back to the live index."""

import json

import curation_identity_fixtures as fixtures
import pytest

DIGEST = "a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262"


@pytest.fixture
def capture(tmp_path):
    relative = "tests/fixtures/curation_mim/" + DIGEST + ".json"
    target = tmp_path / relative
    target.parent.mkdir(parents=True)
    target.write_bytes((fixtures.ROOT / relative).read_bytes())
    return tmp_path, target


def test_historical_index_is_loaded_without_live_package_fallback(monkeypatch):
    def forbidden(*args, **kwargs):
        pytest.fail("Historical evidence must not read the live package index")

    monkeypatch.setattr(fixtures.MIMLabelIndex, "from_package", forbidden)
    index = fixtures.read_mim_capture(DIGEST)
    assert index.metadata["sha256"] == DIGEST
    assert index.metadata["source_commit"] == "9f09e4fb97fb0e6cbbd6f25baca40b36512adb88"
    assert index.resolve_label("Casamino acids").ambiguity == "resolved:owned"


@pytest.mark.parametrize("field", ["csv_base64", "metadata"])
def test_historical_capture_and_metadata_tampering_are_rejected(capture, field):
    root, path = capture
    body = json.loads(path.read_text())
    if field == "metadata":
        body[field]["source_commit"] = "0" * 40
    else:
        body[field] = "Zm9yZ2Vk"
    path.write_text(json.dumps(body))
    with pytest.raises(ValueError, match="capture drift"):
        fixtures.read_mim_capture(DIGEST, root=root)


def test_missing_capture_never_falls_back_to_packaged_index(tmp_path):
    with pytest.raises(FileNotFoundError):
        fixtures.read_mim_capture(DIGEST, root=tmp_path)


@pytest.mark.parametrize("digest", [None, [], "../outside", "0" * 64])
def test_unregistered_index_is_rejected(tmp_path, digest):
    with pytest.raises(ValueError, match="Unregistered"):
        fixtures.read_mim_capture(digest, root=tmp_path)


def test_symlink_capture_is_rejected(capture):
    root, path = capture
    saved = root / "saved.json"
    path.rename(saved)
    path.symlink_to(saved)
    with pytest.raises(ValueError, match="symlink"):
        fixtures.read_mim_capture(DIGEST, root=root)
