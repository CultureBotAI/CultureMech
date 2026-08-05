"""Guard that curation scripts write records without reflowing them (#141).

`yaml.dump(..., width=120)` re-wraps every long scalar in a file, not just the
field being edited. PR #140 added one organism and one curation event and produced
47 added lines, 24 of them churn in untouched `notes:`. Semantically lossless, but
it buries the real change exactly where a reviewer needs to see it.
"""
from __future__ import annotations

import importlib.util
import pathlib
import random
import re
import sys

import pytest
import yaml

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def rio():
    return _load("record_io")


def test_no_width_override(rio):
    """The whole fix. `width` absent means PyYAML's default (80), which is the
    corpus convention: 279/300 records round-trip byte-identically under it, and
    2/300 under width=120."""
    assert "width" not in rio.DUMP_KWARGS


def test_keys_are_not_sorted(rio):
    """sort_keys=True round-tripped 0/300 records — it rewrites every file."""
    assert rio.DUMP_KWARGS["sort_keys"] is False


def test_dump_round_trips_the_corpus(rio, media_records):
    """The load-bearing measurement. A writer that reflows is the defect.

    Not 100%: some records were already reflowed by a past width=120 run, so their
    `notes:` exceed the corpus convention. Rewriting those normalises the damage.
    """
    sample = random.Random(3).sample(media_records, min(300, len(media_records)))
    identical = sum(1 for path, _ in sample
                    if rio.dump_record(yaml.safe_load(path.read_text(errors="replace")))
                    == path.read_text(errors="replace"))
    assert identical / len(sample) > 0.85, (
        f"only {identical}/{len(sample)} records round-trip byte-identically; the "
        "dump config has drifted from the corpus convention")


def test_write_record_is_a_no_op_when_nothing_changed(rio, tmp_path):
    p = tmp_path / "r.yaml"
    doc = {"id": "CultureMech:1", "name": "x", "notes": "y" * 200}
    rio.write_record(p, doc)
    first = p.read_text()
    mtime = p.stat().st_mtime_ns
    assert rio.write_record(p, doc) is False
    assert p.read_text() == first and p.stat().st_mtime_ns == mtime


def test_write_record_reports_a_real_change(rio, tmp_path):
    p = tmp_path / "r.yaml"
    rio.write_record(p, {"id": "CultureMech:1", "name": "x"})
    assert rio.write_record(p, {"id": "CultureMech:1", "name": "y"}) is True


def test_a_long_note_is_not_rewrapped_by_an_unrelated_edit(rio, tmp_path):
    """The #141 scenario end to end: append a field, and the untouched long note
    must not move."""
    p = tmp_path / "r.yaml"
    note = ("Source: KOMODO ModelSEED | ID: 378 | DSMZ Medium: 378 "
            "(mediadive.medium:378) | Aerobic: No | Notes: a fairly long trailing note")
    doc = {"id": "CultureMech:1", "name": "x", "notes": note}
    rio.write_record(p, doc)
    before = p.read_text().splitlines()
    doc["applications"] = "Microbial cultivation"
    rio.write_record(p, doc)
    after = p.read_text().splitlines()
    note_before = [ln for ln in before if "KOMODO" in ln or "Aerobic" in ln]
    note_after = [ln for ln in after if "KOMODO" in ln or "Aerobic" in ln]
    assert note_before == note_after, "the untouched note was re-wrapped"
    assert len(after) == len(before) + 1


# --- the regression guard ---------------------------------------------------


def test_no_corpus_writer_passes_a_width_override():
    """The specific mistake. `apply_curation_proposals.py` already carried a
    comment warning against it, and two sibling scripts did it anyway — a comment
    is not a guard."""
    # PyYAML's default is 80, so stating it explicitly is equivalent and harmless.
    # Anything else re-wraps.
    CORPUS_DEFAULT = 80
    # Scripts that dump YAML but not corpus records. Listed with the reason, so an
    # addition here is a visible claim rather than a silent exemption.
    NOT_CORPUS_RECORDS = {
        "research_media_edison.py": "writes research/*-meta.yaml, not corpus records",
    }
    offenders = []
    for path in (REPO_ROOT / "scripts").glob("*.py"):
        if path.name == "record_io.py" or path.name in NOT_CORPUS_RECORDS:
            continue
        text = path.read_text(errors="replace")
        if "normalized_yaml" not in text:
            continue
        for m in re.finditer(r"yaml\.(?:safe_)?dump\([^)]*width\s*=\s*(\d+)", text, re.S):
            if int(m.group(1)) != CORPUS_DEFAULT:
                offenders.append(f"{path.name}: width={m.group(1)}")
    assert not offenders, (
        "these scripts write corpus records with a width override, which reflows "
        f"every long scalar: {offenders}. Use `record_io.write_record`.")
