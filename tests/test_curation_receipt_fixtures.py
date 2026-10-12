"""Historical receipts must be portable without bypassing their original hashes."""

import base64
import hashlib
import json

import pytest
from curation_receipt_fixtures import read_receipt_capture, receipt_name

NAME = "reports/ingredient_concentration_curation/20261009-test/check.log"


def fixture(tmp_path):
    raw = b"All checks passed!\n"
    digest = hashlib.sha256(raw).hexdigest()
    path = tmp_path / "tests/fixtures/curation_receipts" / f"{digest}.json"
    path.parent.mkdir(parents=True)
    body = {
        "sha256": digest,
        "source_paths": [NAME],
        "payload_base64": base64.b64encode(raw).decode(),
    }
    path.write_text(json.dumps(body))
    return path, body, raw, digest


def test_receipts_relocate_without_the_recorded_workstation(tmp_path):
    _, _, raw, digest = fixture(tmp_path)
    assert read_receipt_capture("/absent/workstation/" + NAME, digest, root=tmp_path) == raw
    assert read_receipt_capture(NAME, digest, root=tmp_path) == raw


def test_missing_fixture_never_falls_back_to_an_available_log(tmp_path):
    path, _, raw, digest = fixture(tmp_path)
    path.unlink()
    source = tmp_path / NAME
    source.parent.mkdir(parents=True)
    source.write_bytes(raw)
    with pytest.raises(ValueError, match="unavailable"):
        read_receipt_capture(str(source), digest, root=tmp_path)


@pytest.mark.parametrize("damage", ["digest", "path", "encoding", "content", "path_type"])
def test_receipt_fixture_tampering_is_rejected(tmp_path, damage):
    path, body, _, digest = fixture(tmp_path)
    if damage == "digest":
        body["sha256"] = "0" * 64
    elif damage == "path":
        body["source_paths"] = [NAME + ".other"]
    elif damage == "path_type":
        body["source_paths"] = NAME
    else:
        body["payload_base64"] = "not base64!" if damage == "encoding" else "Zm9yZ2Vk"
    path.write_text(json.dumps(body))
    with pytest.raises(ValueError):
        read_receipt_capture(NAME, digest, root=tmp_path)


@pytest.mark.parametrize("digest", ["", "0" * 63, "G" * 64, None])
def test_invalid_receipt_digest_is_rejected(tmp_path, digest):
    with pytest.raises(ValueError, match="digest"):
        read_receipt_capture(NAME, digest, root=tmp_path)


@pytest.mark.parametrize(
    "path", ["/tmp/check.log", NAME + "/../other.log", NAME + "/" + NAME, None]
)
def test_unknown_or_escaping_receipt_path_is_rejected(path):
    with pytest.raises(ValueError, match="path"):
        receipt_name(path)


def test_symlink_fixture_is_rejected(tmp_path):
    path, _, _, digest = fixture(tmp_path)
    saved = tmp_path / "saved.json"
    path.rename(saved)
    path.symlink_to(saved)
    with pytest.raises(ValueError, match="symlink"):
        read_receipt_capture(NAME, digest, root=tmp_path)
