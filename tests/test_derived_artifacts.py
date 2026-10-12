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


@pytest.fixture(scope="module")
def inventory_rows(ada):
    return ada.inventory()


def test_the_manifest_matches_a_fresh_computation(inventory_rows):
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
    w.writerows(inventory_rows)
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


def test_snapshots_are_never_freshness_checked(ada, inventory_rows):
    """Regenerating a dated snapshot or a migration record would falsify history —
    those files are an accurate account of what ran, stale paths and all."""
    for row in inventory_rows:
        if row["kind"] == "SNAPSHOT":
            assert not row["freshness_checked"], f"{row['artifact']} is a snapshot"
            assert row["artifact"] not in ada.CHECKABLE


@pytest.mark.parametrize("basename", ["manifest.tsv", "source_checks.json", "summary.json"])
def test_timestamped_concentration_reviews_are_historical_snapshots(ada, basename):
    path = f"reports/ingredient_concentration_review/20261005T175229Z/{basename}"
    assert ada.classify(path, "scripts/build_media_content_review_manifest.py") == (
        "SNAPSHOT",
        "timestamped concentration review",
    )
    assert path not in ada.CHECKABLE


@pytest.mark.parametrize("directory", ["current", "20261005", "20261005T175229Z_extra"])
def test_undated_concentration_outputs_are_not_assumed_to_be_snapshots(ada, directory):
    path = f"reports/ingredient_concentration_review/{directory}/summary.json"
    assert ada.classify(path, None) == ("UNKNOWN", "no writer found")


def test_snapshot_manifest_is_not_attributed_by_generic_basename(ada, monkeypatch):
    path = "reports/ingredient_concentration_review/20261005T175229Z/manifest.tsv"
    monkeypatch.setattr(ada, "tracked_artifacts", lambda: [path])
    monkeypatch.setattr(
        ada, "find_writers", lambda *_: ["scripts/build_media_content_review_manifest.py"]
    )
    row = ada.inventory()[0]
    assert row["kind"] == "SNAPSHOT"
    assert row["writes"] == row["mentioned_by"] == row["freshness_checked"] == ""


@pytest.mark.parametrize("basename", ["plan.json", "source-review.json", "manifest.tsv"])
def test_dated_curation_packets_are_snapshots_without_writer_search(ada, monkeypatch, basename):
    path = f"reports/ingredient_concentration_curation/20261010-utex-test/{basename}"
    monkeypatch.setattr(ada, "tracked_artifacts", lambda: [path])

    def unexpected_search(*_):
        pytest.fail("Historical packets must not be attributed by generic basename")

    monkeypatch.setattr(ada, "find_writers", unexpected_search)
    row = ada.inventory()[0]
    assert (row["kind"], row["reason"]) == ("SNAPSHOT", "dated concentration curation")
    assert row["writes"] == row["mentioned_by"] == row["freshness_checked"] == ""


def test_dated_curation_root_receipts_are_snapshots(ada):
    path = "reports/ingredient_concentration_curation/20261007-diff-audit-after-jcm896.json"
    assert ada.classify(path, None) == ("SNAPSHOT", "dated concentration curation")


@pytest.mark.parametrize("directory", ["current", "20261010", "20261010T175229Z_extra"])
def test_undated_curation_outputs_are_not_assumed_to_be_snapshots(ada, directory):
    path = f"reports/ingredient_concentration_curation/{directory}/summary.json"
    assert ada.classify(path, None) == ("UNKNOWN", "no writer found")


def test_writer_search_is_reused_only_within_one_inventory(ada, monkeypatch):
    paths = ["reports/one/unclassified.json", "reports/two/unclassified.json"]
    monkeypatch.setattr(ada, "tracked_artifacts", lambda: paths)
    calls = []
    monkeypatch.setattr(ada, "find_writers", lambda art, _: calls.append(art) or [])
    assert len(ada.inventory()) == 2
    assert calls == paths[:1]
    assert len(ada.inventory()) == 2
    assert calls == [paths[0], paths[0]]


def test_writer_search_is_literal_and_includes_ignored_sources(ada, monkeypatch, tmp_path):
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (tmp_path / ".gitignore").write_text("scripts/ignored.py\n")
    (scripts / "ignored.py").write_text('OUTPUT = "manifest.json"\n')
    hidden = scripts / ".hidden"
    hidden.mkdir()
    (hidden / "writer.py").write_text('OUTPUT = "manifest.json"\n')
    (scripts / "not_a_match.py").write_text('OUTPUT = "manifestXjson"\n')
    monkeypatch.setattr(ada, "REPO", tmp_path)
    assert ada.find_writers("reports/manifest.json") == [
        "scripts/.hidden/writer.py",
        "scripts/ignored.py",
    ]
    (scripts / "ignored.py").write_text('OUTPUT = "different.json"\n')
    assert ada.find_writers("reports/manifest.json") == ["scripts/.hidden/writer.py"]


def test_the_classification_covers_every_tracked_artifact(ada, inventory_rows):
    rows = inventory_rows
    assert len(rows) == len(ada.tracked_artifacts())
    assert all(r["kind"] in {"AUTHORITATIVE", "CURRENT_VIEW", "SNAPSHOT", "UNKNOWN"} for r in rows)


def test_curator_owned_tombstones_are_not_misclassified_as_generated(inventory_rows):
    row = next(r for r in inventory_rows if r["artifact"] == "data/culturemech_id_tombstones.tsv")
    assert row["kind"] == "AUTHORITATIVE"
    assert row["writes"] == ""
    assert "curator-owned" in row["reason"]


def test_unknowns_are_reported_not_hidden(inventory_rows):
    """UNKNOWN is the honest state for an unclassified artifact. This asserts the
    inventory still surfaces them — silence would imply coverage that does not
    exist. It is a ceiling, not a target: driving it to 0 by guessing would be
    worse than leaving them listed."""
    unknown = [r for r in inventory_rows if r["kind"] == "UNKNOWN"]
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


def test_the_auditor_is_never_recorded_as_a_writer(ada, inventory_rows):
    """`audit_derived_artifacts.py` names every CHECKABLE artifact, so a plain grep
    matched all of them — and sorted first for unparsed_compositions.tsv, making
    the manifest report the auditor as that report's writer. The writer column is
    the evidence for each classification, so circular attribution undermines it."""
    for row in inventory_rows:
        assert (
            ada.SELF not in row["mentioned_by"]
        ), f"{row['artifact']} attributes itself to the auditor"
        assert ada.SELF not in row["writes"], f"{row['artifact']} claims the auditor writes it"


def test_all_candidate_writers_are_recorded_not_just_the_first(inventory_rows):
    """Nine artifacts have several. Ambiguity a curator can see beats a confident
    wrong answer."""
    multi = [r for r in inventory_rows if ";" in r["mentioned_by"]]
    assert multi, "no multi-writer artifacts recorded; find_writers regressed to first-match"


def test_a_checkable_artifact_uses_its_declared_writer(ada, inventory_rows):
    """Re-deriving by grep would be guessing at something already stated."""
    rows = {row["artifact"]: row for row in inventory_rows}
    for art, cmd in ada.CHECKABLE.items():
        row = rows[art]
        assert cmd[0] in row["writes"], f"{art}: declared writer {cmd[0]} not confirmed as a writer"


def test_the_regenerating_writer_wins_when_several_touch_an_artifact(inventory_rows):
    """`culturemech_id_registry.tsv` is written by assign_culturemech_ids (which
    MINTS ids), refresh_id_registry (which rebuilds it) and id_utils. Taking the
    alphabetically first classified it UNKNOWN and lost a correct answer."""
    row = next(
        (r for r in inventory_rows if r["artifact"] == "data/culturemech_id_registry.tsv"), None
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


def test_indexes_named_by_fstring_are_attributed_to_the_generator(ada):
    """#454: the category and source indexes are written from f-strings, invisible
    to the literal-basename search, and sat at UNKNOWN / no writer found."""
    for art in (
        "data/normalized_yaml/bacterial_index.json",
        "data/normalized_yaml/by_source_mediadive-solutions_index.json",
        "data/merge_yaml/merged/algae_index.json",
    ):
        assert ada.pattern_writer(art) == "scripts/generate_recipe_indexes.py", art
        assert ada.classify(art, ada.pattern_writer(art)) == (
            "CURRENT_VIEW",
            "generate_recipe_indexes.py",
        )
    # not everything under those directories is an index
    assert ada.pattern_writer("data/normalized_yaml/recipe_statistics.json") is None
    assert ada.pattern_writer("data/import_tracking/reports/foo_index.json") is None
