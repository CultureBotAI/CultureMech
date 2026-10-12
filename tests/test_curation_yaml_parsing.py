"""Native safe parsing must preserve the historical writer's data and source spans."""

import json
from pathlib import Path

import pytest
import yaml
from repair_mediadive_stock_concentration_evidence import preserve_unchanged

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    "before,after",
    [
        ("name: old\nnotes: 'retained text'\n", "name: new\nnotes: retained text\n"),
        ("name: '\u03b1'\nitems: [a, b]\n", "name: \u03b1\nitems: [a, b, c]\n"),
        ("notes: |\n  first\n  second\nvalue: 1\n", "notes: |\n  first\n  second\nvalue: 2\n"),
        (
            "left: &x {value: 1}\nright: *x\ncount: 1\n",
            "left: &x {value: 1}\nright: *x\ncount: 2\n",
        ),
        ("date: 2026-10-09\nvalue: null\nflag: true\n", "date: 2026-10-09\nvalue: 2\nflag: true\n"),
    ],
)
def test_native_marks_preserve_python_writer_bytes(before, after, monkeypatch):
    native = preserve_unchanged(before, after)
    with monkeypatch.context() as patch:
        patch.setattr(yaml, "CSafeLoader", yaml.SafeLoader)
        reference = preserve_unchanged(before, after)
    assert native == reference
    assert yaml.safe_load(native) == yaml.safe_load(after)


@pytest.mark.parametrize(
    "cohort,plan",
    [
        ("20261009-desulfurobacterium-family", "plan-v2.json"),
        ("20261009-synthrophomonas-family", "plan-v2.json"),
        ("20261009-halobacteria-variants", "plan.json"),
    ],
)
def test_large_review_records_have_identical_data_and_source_spans(cohort, plan, monkeypatch):
    packet = json.loads(
        (ROOT / "reports/ingredient_concentration_curation" / cohort / plan).read_text()
    )
    record = max(packet["records"], key=lambda row: len(row["after_text"]))
    before, after = record["before_text"], record["after_text"]
    for raw in (before, after):
        assert yaml.load(raw, Loader=yaml.CSafeLoader) == yaml.safe_load(raw)
    native = preserve_unchanged(before, after)
    with monkeypatch.context() as patch:
        patch.setattr(yaml, "CSafeLoader", yaml.SafeLoader)
        reference = preserve_unchanged(before, after)
    assert native == reference


@pytest.mark.parametrize("loader", [yaml.SafeLoader, yaml.CSafeLoader])
def test_both_safe_loaders_reject_python_object_tags(loader):
    with pytest.raises(yaml.constructor.ConstructorError):
        yaml.load("!!python/object/apply:os.getpid []", Loader=loader)
