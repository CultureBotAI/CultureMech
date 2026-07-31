"""Tests for the media-type axis migration (#153).

`scripts/migrate_medium_type_axes.py` rewrote 11,088 corpus records in #148 with
no tests at all, while `research_media.py` — which writes nothing — had three
test files. These cover the behaviors that make the migration safe to re-run:
idempotency, insertion position, the deliberate non-mappings, and dry-run
actually not writing.

The bulk pass used `--text`, which splices lines in rather than round-tripping,
so that path is exercised most heavily here.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "migrate_medium_type_axes.py"


@pytest.fixture(scope="module")
def mig():
    spec = importlib.util.spec_from_file_location("migrate_medium_type_axes", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


RECORD = """\
id: CultureMech:000001
name: Test Medium
# a comment that must survive
medium_type: COMPLEX
physical_state: LIQUID
ingredients:
- name: yeast extract
  concentration: 1.0
"""


def _write(tmp_path: Path, text: str = RECORD) -> Path:
    path = tmp_path / "rec.yaml"
    path.write_text(text)
    return path


# --- the mapping table itself -------------------------------------------------


@pytest.mark.parametrize(
    "medium_type,expected",
    [
        ("DEFINED", {"composition_type": "DEFINED"}),
        ("COMPLEX", {"composition_type": "UNDEFINED"}),
        ("MINIMAL", {"nutritional_class": "MINIMAL"}),
        ("SELECTIVE", {"functional_role": ["SELECTIVE"]}),
        ("DIFFERENTIAL", {"functional_role": ["DIFFERENTIAL"]}),
        ("ENRICHMENT", {"functional_role": ["ENRICHMENT"]}),
    ],
)
def test_plan_record_maps_each_source_value(mig, medium_type, expected) -> None:
    assert mig.plan_record({"medium_type": medium_type})[0] == expected


@pytest.mark.parametrize("medium_type", ["BUFFER", "NEGATIVE_CONTROL"])
def test_non_media_values_are_deliberately_unmapped(mig, medium_type) -> None:
    """BUFFER and NEGATIVE_CONTROL are not growth media — they get no axes."""
    assert mig.plan_record({"medium_type": medium_type})[0] == {}


def test_record_without_medium_type_is_untouched(mig) -> None:
    assert mig.plan_record({"name": "x"})[0] == {}


def test_functional_role_is_wrapped_in_a_list(mig) -> None:
    """The slot is multivalued; a bare string would be schema-invalid."""
    additions, _ = mig.plan_record({"medium_type": "SELECTIVE"})
    assert isinstance(additions["functional_role"], list)


# --- idempotency --------------------------------------------------------------


def test_existing_axis_value_is_never_overwritten(mig) -> None:
    """The idempotency guarantee: only absent slots are written."""
    doc = {"medium_type": "COMPLEX", "composition_type": "SEMI_DEFINED"}
    assert mig.plan_record(doc)[0] == {}


def test_second_run_is_a_no_op(mig, tmp_path: Path) -> None:
    path = _write(tmp_path)
    additions, _ = mig.plan_record(yaml.safe_load(path.read_text()))
    assert mig.apply_additions_text(path, additions) is True
    after_first = path.read_text()

    again, _ = mig.plan_record(yaml.safe_load(path.read_text()))
    assert again == {}
    assert path.read_text() == after_first


# --- the --text path, which the 11,088-record pass used -----------------------


def test_text_mode_adds_exactly_one_line_and_deletes_none(mig, tmp_path: Path) -> None:
    """The property that made the bulk diff +1/-0 on every file."""
    path = _write(tmp_path)
    before = path.read_text().splitlines()
    mig.apply_additions_text(path, {"composition_type": "UNDEFINED"})
    after = path.read_text().splitlines()

    assert len(after) == len(before) + 1
    assert [line for line in before] == [
        line for line in after if line != "composition_type: UNDEFINED"
    ]


def test_text_mode_preserves_comments(mig, tmp_path: Path) -> None:
    path = _write(tmp_path)
    mig.apply_additions_text(path, {"composition_type": "UNDEFINED"})
    assert "# a comment that must survive" in path.read_text()


def test_axis_lines_land_directly_after_medium_type(mig, tmp_path: Path) -> None:
    path = _write(tmp_path)
    mig.apply_additions_text(path, {"composition_type": "UNDEFINED"})
    lines = path.read_text().splitlines()
    assert lines[lines.index("medium_type: COMPLEX") + 1] == "composition_type: UNDEFINED"


def test_multivalued_role_is_rendered_as_a_yaml_list(mig, tmp_path: Path) -> None:
    path = _write(tmp_path)
    mig.apply_additions_text(path, {"functional_role": ["SELECTIVE"]})
    assert yaml.safe_load(path.read_text())["functional_role"] == ["SELECTIVE"]


def test_text_mode_refuses_a_record_with_no_top_level_medium_type(mig, tmp_path: Path) -> None:
    """Returns False and leaves the file byte-identical rather than guessing."""
    path = _write(tmp_path, "id: CultureMech:000002\ningredients:\n- name: glucose\n")
    before = path.read_text()
    assert mig.apply_additions_text(path, {"composition_type": "UNDEFINED"}) is False
    assert path.read_text() == before


def test_an_indented_medium_type_is_not_mistaken_for_the_top_level_slot(
    mig, tmp_path: Path
) -> None:
    """`medium_type:` nested under another key must not anchor the insertion."""
    nested = "id: CultureMech:000003\nvariants:\n  medium_type: COMPLEX\n"
    path = _write(tmp_path, nested)
    before = path.read_text()
    assert mig.apply_additions_text(path, {"composition_type": "UNDEFINED"}) is False
    assert path.read_text() == before


# --- write safety -------------------------------------------------------------


def test_write_yaml_refuses_rather_than_reflowing_without_ruamel(
    mig, tmp_path: Path, monkeypatch
) -> None:
    """#153: the old pyyaml fallback silently reflowed whole records."""
    path = _write(tmp_path)
    before = path.read_text()
    monkeypatch.setattr(mig, "ROUND_TRIP_YAML", None)

    with pytest.raises(RuntimeError, match="reflows records"):
        mig.write_yaml(path, {"id": "CultureMech:000001"})
    assert path.read_text() == before, "refused write must leave the file untouched"


def test_dry_run_writes_nothing(mig, tmp_path: Path) -> None:
    path = _write(tmp_path)
    before = path.read_text()
    assert mig.main([str(path), "--text"]) == 0
    assert path.read_text() == before


def test_apply_actually_writes(mig, tmp_path: Path) -> None:
    """Guards against the dry-run test above passing vacuously."""
    path = _write(tmp_path)
    assert mig.main([str(path), "--text", "--apply"]) == 0
    assert yaml.safe_load(path.read_text())["composition_type"] == "UNDEFINED"


def test_unparseable_record_is_skipped_not_fatal(mig, tmp_path: Path) -> None:
    bad = tmp_path / "bad.yaml"
    bad.write_text("id: [unclosed\n")
    assert mig.main([str(bad), "--text", "--apply"]) == 0
