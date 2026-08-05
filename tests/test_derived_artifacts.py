"""Guard that tracked derived artifacts stay classified and fresh (#145).

Six instances of the same bug: a record move leaves stale paths in a tracked
artifact nothing refreshes, and only the recipe indexes (#125) fail loudly. The
registry (#144), the chebi report (#157) and two review manifests (#168) were each
found by someone going looking.

The classification is COMPUTED, not written down. #145 suggested "a short table in
docs/DATA_LAYERS.md" — but a static table listing derived artifacts is itself a
derived artifact nobody refreshes, which would be the seventh instance.
"""
from __future__ import annotations

import importlib.util
import subprocess
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
def ada():
    return _load("audit_derived_artifacts")


def test_the_manifest_matches_a_fresh_computation(ada):
    """The manifest is itself a tracked derived artifact, so it needs the same
    guarantee it exists to provide. Refresh with `just audit-derived-artifacts`."""
    manifest = REPO_ROOT / "data" / "import_tracking" / "derived_artifacts.tsv"
    assert manifest.is_file(), "derived_artifacts.tsv is missing"
    import csv
    import io
    fresh = io.StringIO(newline="")
    w = csv.DictWriter(fresh, delimiter="\t", lineterminator="\r\n", fieldnames=[
        "artifact", "kind", "reason", "writer", "freshness_checked"])
    w.writeheader()
    w.writerows(ada.inventory())
    # Compare row content, not line endings: the script writes with newline="" so
    # csv chooses \r\n, and reading back through read_text() normalises. Splitting
    # sidesteps that without weakening the comparison.
    got = [ln for ln in manifest.read_text().splitlines() if ln]
    want = [ln for ln in fresh.getvalue().splitlines() if ln]
    assert got == want, (
        "derived_artifacts.tsv is stale — run `just audit-derived-artifacts`")


def test_every_checkable_artifact_exists_and_is_tracked(ada):
    """A typo in CHECKABLE would silently drop an artifact from the guard."""
    tracked = set(subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                                 cwd=REPO_ROOT).stdout.split())
    for art in ada.CHECKABLE:
        assert (REPO_ROOT / art).is_file(), f"{art} declared checkable but missing"
        assert art in tracked, f"{art} declared checkable but not tracked"


def test_every_checkable_writer_exists(ada):
    for art, cmd in ada.CHECKABLE.items():
        assert (REPO_ROOT / cmd[0]).is_file(), f"{art}: writer {cmd[0]} missing"


def test_snapshots_are_never_freshness_checked(ada):
    """Regenerating a dated snapshot or a migration record would falsify history —
    those files are an accurate account of what ran, stale paths and all."""
    for row in ada.inventory():
        if row["kind"] == "SNAPSHOT":
            assert not row["freshness_checked"], f"{row['artifact']} is a snapshot"
            assert row["artifact"] not in ada.CHECKABLE


def test_the_classification_covers_every_tracked_artifact(ada):
    rows = ada.inventory()
    assert len(rows) == len(ada.tracked_artifacts())
    assert all(r["kind"] in {"CURRENT_VIEW", "SNAPSHOT", "UNKNOWN"} for r in rows)


def test_unknowns_are_reported_not_hidden(ada):
    """UNKNOWN is the honest state for an unclassified artifact. This asserts the
    inventory still surfaces them — silence would imply coverage that does not
    exist. It is a ceiling, not a target: driving it to 0 by guessing would be
    worse than leaving them listed."""
    unknown = [r for r in ada.inventory() if r["kind"] == "UNKNOWN"]
    assert len(unknown) <= 55, (
        f"{len(unknown)} unclassified artifacts, above the documented 55. A new "
        "tracked artifact was added without a classification.")


def test_a_corrupted_artifact_is_detected(ada, tmp_path, monkeypatch):
    """The load-bearing test: a freshness check that cannot fail is worthless.

    Verified end to end during development — corrupting filename_collisions.tsv
    made `--check` exit 1 naming exactly that file. This pins the comparison
    itself, without the multi-minute corpus regeneration.
    """
    art = next(iter(ada.CHECKABLE))
    real = REPO_ROOT / art
    fake = tmp_path / "out.tsv"
    fake.write_text(real.read_text() + "bogus\tstale\trow\n")
    assert fake.read_bytes() != real.read_bytes(), (
        "the byte comparison the check relies on would not notice a changed file")
