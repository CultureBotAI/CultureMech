"""Safety tests for explicit MIM dependency refreshes (#260)."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

pytestmark = pytest.mark.fast
ROOT = Path(__file__).resolve().parent.parent


def _load_refresh_module():
    path = ROOT / "scripts" / "refresh_mim_label_index.py"
    spec = importlib.util.spec_from_file_location("refresh_mim_label_index", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _isolated_pin(module, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> bytes:
    data = module.INDEX_PATH.read_bytes()
    metadata = module.METADATA_PATH.read_bytes()
    index_path = tmp_path / "label_index.csv"
    metadata_path = tmp_path / "label_index.metadata.json"
    index_path.write_bytes(data)
    metadata_path.write_bytes(metadata)
    monkeypatch.setattr(module, "INDEX_PATH", index_path)
    monkeypatch.setattr(module, "METADATA_PATH", metadata_path)
    return data


def test_refresh_is_preview_only_unless_apply_is_explicit(tmp_path, monkeypatch, capsys):
    module = _load_refresh_module()
    data = _isolated_pin(module, tmp_path, monkeypatch)
    before = module.METADATA_PATH.read_bytes()

    assert module.refresh("0" * 40, data) == (0, 0, 0)
    assert module.METADATA_PATH.read_bytes() == before
    assert "Preview only" in capsys.readouterr().out


def test_apply_updates_only_the_isolated_pin_after_validation(tmp_path, monkeypatch):
    module = _load_refresh_module()
    data = _isolated_pin(module, tmp_path, monkeypatch)

    module.refresh("0" * 40, data, apply=True)
    metadata = json.loads(module.METADATA_PATH.read_text(encoding="utf-8"))
    assert metadata["source_commit"] == "0" * 40
    assert module.INDEX_PATH.read_bytes() == data


def test_short_or_moving_revision_is_rejected(tmp_path, monkeypatch):
    module = _load_refresh_module()
    data = _isolated_pin(module, tmp_path, monkeypatch)
    with pytest.raises(SystemExit, match="full lowercase 40-character"):
        module.refresh("main", data)
