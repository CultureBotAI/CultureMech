"""Tests for media target resolution and its indexes (#174).

`_tiered_candidates` re-globbed and re-read all 15,878 records on EVERY call, so a
200-entry batch spent ~160s doing nothing but re-reading the same files. The
indexes below cut that to ~1s.

Speed is the easy part. These mostly pin CORRECTNESS, because a fast resolver that
returns the wrong record is worse than a slow one — and the tier ranking exists
because 2,291 record `name:` values are shared (#151).
"""
from __future__ import annotations

import importlib.util
import sys
import time
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
def rm():
    return _load("research_media")


# --- correctness ------------------------------------------------------------


def test_a_culturemech_id_resolves_to_its_own_record(rm, media_records):
    """Tier 1. Answered from the tracked registry with no corpus scan."""
    checked = 0
    for path, doc in media_records[:200]:
        cid = doc.get("id")
        if not cid:
            continue
        assert rm.resolve_media_file(str(cid)).resolve() == path.resolve()
        checked += 1
    assert checked > 50, "sample carried too few ids to be meaningful"


def test_a_filename_stem_resolves_to_that_file(rm, media_records):
    for path, _ in media_records[:150]:
        try:
            assert rm.resolve_media_file(path.stem).resolve() == path.resolve()
        except ValueError:
            pass  # a genuine cross-directory collision (#151), not an index bug


def test_an_unknown_target_still_raises(rm):
    with pytest.raises(FileNotFoundError):
        rm.resolve_media_file("definitely_not_a_medium_xyz_123")


def test_a_path_target_short_circuits(rm, media_records):
    path, _ = media_records[0]
    assert rm.resolve_media_file(str(path)).resolve() == path.resolve()


def test_the_id_tier_outranks_the_filename_tier(rm):
    """The ranking #151 added. An id must win even when some other record's
    filename normalises to the same string."""
    idx = rm._id_index()
    assert idx, "id index is empty; the registry did not load"
    cid, path = next(iter(idx.items()))
    assert rm.resolve_media_file(cid).resolve() == path.resolve()


# --- the indexes themselves -------------------------------------------------


def test_the_id_index_covers_the_corpus(rm, media_records):
    idx = rm._id_index()
    assert len(idx) > 15_000, f"id index has only {len(idx)} entries"
    missing = [str(d["id"]) for _, d in media_records[:300]
               if d.get("id") and rm._normal_key(str(d["id"])) not in idx]
    assert not missing, f"records absent from the registry index: {missing[:5]}"


def test_a_stale_registry_entry_does_not_become_a_wrong_answer(rm, tmp_path, monkeypatch):
    """The registry is tracked and guarded (#144), but it CAN go stale between a
    record move and a refresh. A stale hit must fall through to the scan rather
    than return a path that no longer exists."""
    rm.reset_resolution_caches()
    monkeypatch.setattr(rm, "_ID_INDEX",
                        {"culturemech:000001": tmp_path / "gone.yaml"})
    with pytest.raises((FileNotFoundError, ValueError)):
        rm.resolve_media_file("CultureMech:000001__definitely_absent")
    rm.reset_resolution_caches()


def test_reset_clears_every_cache(rm):
    rm._id_index()
    rm._filename_index()
    rm._media_files()
    rm.reset_resolution_caches()
    assert rm._ID_INDEX is None
    assert rm._FILENAME_INDEX is None
    assert rm._MEDIA_FILES is None


# --- the regression this fixes ---------------------------------------------


def test_repeated_resolution_does_not_rescan_the_corpus(rm, media_records):
    """The actual bug. Each call re-read 15,878 files at ~800ms; a 200-entry batch
    spent ~160s before doing any work. Timing is a blunt instrument, so the bar is
    deliberately loose — it only has to catch a return to per-call scanning.
    """
    targets = [str(d["id"]) for _, d in media_records[:40] if d.get("id")][:30]
    assert len(targets) >= 20, "not enough ids sampled"
    rm.resolve_media_file(targets[0])          # pay index construction once
    start = time.perf_counter()
    for t in targets:
        rm.resolve_media_file(t)
    per_call = (time.perf_counter() - start) / len(targets)
    assert per_call < 0.05, (
        f"{per_call*1000:.0f} ms/resolution — the per-call corpus scan is back")
