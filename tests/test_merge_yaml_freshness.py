"""Unit-test the pure diff at the heart of the merge_yaml freshness audit (#215).

The audit's job is to test the load-bearing assumption that every corpus gate
relies on — that merge_yaml is a current derivation of normalized_yaml. The full
regeneration takes ~3 min and writes ~6.3k files, so it is not run here; only
``compare_corpora``, the side-effect-free diff, is. That is enough to guard the
part with logic in it — the merge itself is exercised by the Merge recipes.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def amf():
    return _load("audit_merge_yaml_freshness")


def _write(d: Path, name: str, body: str) -> None:
    (d / name).write_text(body, encoding="utf-8")


def test_identical_corpora_are_current(amf, tmp_path):
    tracked, fresh = tmp_path / "t", tmp_path / "f"
    tracked.mkdir(), fresh.mkdir()
    for d in (tracked, fresh):
        _write(d, "a.yaml", "id: 1\n")
        _write(d, "b.yaml", "id: 2\n")
    report = amf.compare_corpora(tracked, fresh)
    assert report.is_current
    assert report.drift_count == 0
    assert report.summary()["unchanged"] == 2


def test_detects_added_dropped_and_changed(amf, tmp_path):
    tracked, fresh = tmp_path / "t", tmp_path / "f"
    tracked.mkdir(), fresh.mkdir()
    _write(tracked, "same.yaml", "id: 1\n")
    _write(fresh, "same.yaml", "id: 1\n")
    _write(tracked, "dropped.yaml", "id: 2\n")   # a fresh run no longer emits this
    _write(tracked, "changed.yaml", "id: 3\n")
    _write(fresh, "changed.yaml", "id: 3  # edited\n")
    _write(fresh, "added.yaml", "id: 4\n")       # a fresh run now emits this

    report = amf.compare_corpora(tracked, fresh)
    assert not report.is_current
    assert report.only_in_tracked == ["dropped.yaml"]
    assert report.only_in_fresh == ["added.yaml"]
    assert report.changed == ["changed.yaml"]
    assert report.unchanged == ["same.yaml"]
    assert report.drift_count == 3

    summary = report.summary()
    assert summary["tracked_total"] == 3   # same + dropped + changed
    assert summary["fresh_total"] == 3     # same + added + changed


def test_curation_timestamp_alone_is_not_drift(amf, tmp_path):
    """The merge stamps a fresh now() into curation_history every run; two records
    that differ ONLY by that timestamp must compare as unchanged, or the tool would
    report the whole corpus stale right after a clean regenerate."""
    tracked, fresh = tmp_path / "t", tmp_path / "f"
    tracked.mkdir(), fresh.mkdir()
    _write(tracked, "r.yaml",
           "name: R\ncuration_history:\n- action: MERGED_RECIPES\n  timestamp: '2026-07-20T00:00:00Z'\n")
    _write(fresh, "r.yaml",
           "name: R\ncuration_history:\n- action: MERGED_RECIPES\n  timestamp: '2026-08-05T00:00:00Z'\n")
    report = amf.compare_corpora(tracked, fresh)
    assert report.is_current, "timestamp-only difference should not count as drift"
    assert report.summary()["unchanged"] == 1


def test_real_change_survives_timestamp_normalization(amf, tmp_path):
    """A substantive difference must still be caught even when the timestamp also
    differs — normalization blanks the timestamp, not the payload."""
    tracked, fresh = tmp_path / "t", tmp_path / "f"
    tracked.mkdir(), fresh.mkdir()
    _write(tracked, "r.yaml",
           "name: R\ncategory: bacterial\ncuration_history:\n- action: MERGED_RECIPES\n  timestamp: '2026-07-20T00:00:00Z'\n")
    _write(fresh, "r.yaml",
           "name: R\ncategory: archaeal\ncuration_history:\n- action: MERGED_RECIPES\n  timestamp: '2026-08-05T00:00:00Z'\n")
    report = amf.compare_corpora(tracked, fresh)
    assert report.changed == ["r.yaml"]


def test_only_yaml_files_are_compared(amf, tmp_path):
    """A stray stats JSON or index in the corpus dir must not count as a record."""
    tracked, fresh = tmp_path / "t", tmp_path / "f"
    tracked.mkdir(), fresh.mkdir()
    _write(tracked, "a.yaml", "id: 1\n")
    _write(fresh, "a.yaml", "id: 1\n")
    _write(tracked, "merge_stats.json", "{}")
    _write(fresh, "recipe_index.json", "{}")
    report = amf.compare_corpora(tracked, fresh)
    assert report.is_current
    assert report.summary() == {
        "tracked_total": 1, "fresh_total": 1, "only_in_tracked": 0,
        "only_in_fresh": 0, "changed": 0, "unchanged": 1,
    }
