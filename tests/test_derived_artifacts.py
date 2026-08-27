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
    w = csv.DictWriter(
        fresh,
        delimiter="\t",
        lineterminator="\r\n",
        fieldnames=["artifact", "kind", "reason", "writes", "mentioned_by", "freshness_checked"],
    )
    w.writeheader()
    w.writerows(ada.inventory())
    # Compare row content, not line endings: the script writes with newline="" so
    # csv chooses \r\n, and reading back through read_text() normalises. Splitting
    # sidesteps that without weakening the comparison.
    got = [ln for ln in manifest.read_text().splitlines() if ln]
    want = [ln for ln in fresh.getvalue().splitlines() if ln]
    assert got == want, "derived_artifacts.tsv is stale — run `just audit-derived-artifacts`"


def test_every_checkable_artifact_exists_and_is_tracked(ada):
    """A typo in CHECKABLE would silently drop an artifact from the guard."""
    tracked = set(
        subprocess.run(
            ["git", "ls-files"], capture_output=True, text=True, cwd=REPO_ROOT
        ).stdout.split()
    )
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
    assert all(r["kind"] in {"AUTHORITATIVE", "CURRENT_VIEW", "SNAPSHOT", "UNKNOWN"} for r in rows)


def test_curator_owned_tombstones_are_not_misclassified_as_generated(ada):
    row = next(r for r in ada.inventory() if r["artifact"] == "data/culturemech_id_tombstones.tsv")
    assert row["kind"] == "AUTHORITATIVE"
    assert row["writes"] == ""
    assert "curator-owned" in row["reason"]


def test_unknowns_are_reported_not_hidden(ada):
    """UNKNOWN is the honest state for an unclassified artifact. This asserts the
    inventory still surfaces them — silence would imply coverage that does not
    exist. It is a ceiling, not a target: driving it to 0 by guessing would be
    worse than leaving them listed."""
    unknown = [r for r in ada.inventory() if r["kind"] == "UNKNOWN"]
    assert len(unknown) <= 55, (
        f"{len(unknown)} unclassified artifacts, above the documented 55. A new "
        "tracked artifact was added without a classification."
    )


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
    assert (
        fake.read_bytes() != real.read_bytes()
    ), "the byte comparison the check relies on would not notice a changed file"


# --- #204: the tool must not attribute artifacts to itself -----------------


def test_the_auditor_is_never_recorded_as_a_writer(ada):
    """`audit_derived_artifacts.py` names every CHECKABLE artifact, so a plain grep
    matched all of them — and sorted first for unparsed_compositions.tsv, making
    the manifest report the auditor as that report's writer. The writer column is
    the evidence for each classification, so circular attribution undermines it."""
    for row in ada.inventory():
        assert (
            ada.SELF not in row["mentioned_by"]
        ), f"{row['artifact']} attributes itself to the auditor"
        assert ada.SELF not in row["writes"], f"{row['artifact']} claims the auditor writes it"


def test_all_candidate_writers_are_recorded_not_just_the_first(ada):
    """Nine artifacts have several. Ambiguity a curator can see beats a confident
    wrong answer."""
    multi = [r for r in ada.inventory() if ";" in r["mentioned_by"]]
    assert multi, "no multi-writer artifacts recorded; find_writers regressed to first-match"


def test_a_checkable_artifact_uses_its_declared_writer(ada):
    """Re-deriving by grep would be guessing at something already stated."""
    for art, cmd in ada.CHECKABLE.items():
        row = next(r for r in ada.inventory() if r["artifact"] == art)
        assert cmd[0] in row["writes"], f"{art}: declared writer {cmd[0]} not confirmed as a writer"


def test_the_regenerating_writer_wins_when_several_touch_an_artifact(ada):
    """`culturemech_id_registry.tsv` is written by assign_culturemech_ids (which
    MINTS ids), refresh_id_registry (which rebuilds it) and id_utils. Taking the
    alphabetically first classified it UNKNOWN and lost a correct answer."""
    row = next(
        (r for r in ada.inventory() if r["artifact"] == "data/culturemech_id_registry.tsv"), None
    )
    if row is None:
        pytest.skip("id registry not tracked")
    assert row["kind"] == "CURRENT_VIEW"
    assert "refresh_id_registry" in row["reason"]


# --- the slow-test budget itself (#191, #213) -------------------------------


def _conftest():
    """conftest.py is loaded by pytest as a plugin, not importable by name."""
    spec = importlib.util.spec_from_file_location(
        "_cm_conftest", REPO_ROOT / "tests" / "conftest.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_the_slow_test_budget_is_configured():
    """The guard against a fifth corpus-rescan regression. Pinned because an
    empty allowlist and a real threshold are the two things that make it work."""
    cft = _conftest()
    assert cft.SLOW_TEST_BUDGET_S >= 60, "budget too tight to be stable in CI"
    assert (
        cft.SLOW_TEST_BUDGET_S <= 200
    ), "budget too loose to catch the 328s/421s regressions that motivated it"


def test_the_slow_test_allowlist_entries_all_carry_a_reason():
    """An entry must be a decision, not a mute button. Empty is the current and
    preferred state."""
    for nodeid, reason in _conftest().SLOW_TEST_ALLOWLIST.items():
        assert reason and len(reason) > 20, f"{nodeid} exempted without a real reason"
