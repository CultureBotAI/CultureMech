"""Tests for reader-vs-writer attribution of derived artifacts (#209).

`audit_derived_artifacts` attributed artifacts by grepping for the basename, so
its `writer` column listed readers. `research_media.py` reads the id registry to
build a resolution index and writes nothing, yet appeared among its writers — and
that column is what a curator reads to judge current-view versus snapshot.
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
def aw():
    return _load("artifact_writers")


# --- the patterns this repo actually uses -----------------------------------


def test_a_direct_write_text_is_detected(aw):
    src = '''
from pathlib import Path
OUT = Path("data/x/report.tsv")
def main():
    OUT.write_text("hi")
'''
    assert aw.writes_artifact(src, "report.tsv") == "yes"


def test_a_read_only_module_is_not_a_writer(aw):
    """The #209 case: a module binds the path and only reads it."""
    src = '''
from pathlib import Path
REG = Path("data/culturemech_id_registry.tsv")
def load():
    return REG.read_text()
'''
    assert aw.writes_artifact(src, "culturemech_id_registry.tsv") == "no"


def test_the_argparse_default_pattern_is_followed(aw):
    """The dominant shape here: a module constant used as an --out default, with
    the write going through `args.out`. Tracing only direct assignments scored
    1/6 on real scripts."""
    src = '''
from pathlib import Path
import argparse
DEFAULT_OUT = Path("data/x/report.tsv")
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    args.out.write_text("hi")
'''
    assert aw.writes_artifact(src, "report.tsv") == "yes"


def test_the_handle_to_csv_writer_chain_is_followed(aw):
    """The write goes through the DictWriter, not the handle. Missing this link
    left every DictWriter-based report looking unwritten — 2/8 before, 10/10
    after."""
    src = '''
from pathlib import Path
import argparse, csv
DEFAULT_OUT = Path("data/x/report.tsv")
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args()
    with args.out.open("w", newline="") as fh:
        w = csv.DictWriter(fh, delimiter="\\t", fieldnames=["a"])
        w.writeheader()
        w.writerows([])
'''
    assert aw.writes_artifact(src, "report.tsv") == "yes"


def test_a_read_handle_is_not_a_write(aw):
    src = '''
from pathlib import Path
import csv
REG = Path("data/reg.tsv")
def load():
    with REG.open() as fh:
        return list(csv.DictReader(fh))
'''
    assert aw.writes_artifact(src, "reg.tsv") == "no"


def test_unparseable_source_is_unknown_not_a_guess(aw):
    """A wrong "yes" is worse than an honest "unknown" — the point is to stop
    asserting things that are not established."""
    assert aw.writes_artifact("def broken(:\n", "x.tsv") == "unknown"


# --- against the real repo --------------------------------------------------


@pytest.mark.parametrize("script,artifact,expected", [
    ("research_media.py", "culturemech_id_registry.tsv", "no"),
    ("refresh_id_registry.py", "culturemech_id_registry.tsv", "yes"),
    ("triage_missing_compositions.py", "missing_compositions.tsv", "yes"),
    ("audit_selective_agent_mismatch.py", "selective_agent_mismatch.tsv", "yes"),
    ("score_review_need.py", "review_need_ranking.tsv", "yes"),
    ("report_unparsed_compositions.py", "unparsed_compositions.tsv", "yes"),
    ("audit_filename_collisions.py", "filename_collisions.tsv", "yes"),
    ("audit_composition_type.py", "composition_type_conflicts.tsv", "yes"),
    ("prioritize_deep_research_candidates.py", "deep_research_priority.json", "yes"),
])
def test_known_cases_in_this_repo(aw, script, artifact, expected):
    path = REPO_ROOT / "scripts" / script
    if not path.is_file():
        pytest.skip(f"{script} not present")
    assert aw.classify_file(path, artifact) == expected


def test_the_manifest_separates_writes_from_mentions():
    """The columns must not be conflated again."""
    import csv
    manifest = REPO_ROOT / "data" / "import_tracking" / "derived_artifacts.tsv"
    rows = list(csv.DictReader(manifest.open(), delimiter="\t"))
    assert "writes" in rows[0] and "mentioned_by" in rows[0]
    assert "writer" not in rows[0], "the ambiguous `writer` column is back"
    registry = next(r for r in rows if r["artifact"] == "data/culturemech_id_registry.tsv")
    assert "research_media.py" in registry["mentioned_by"]
    assert "research_media.py" not in registry["writes"], (
        "a reader is listed as a writer again (#209)")
