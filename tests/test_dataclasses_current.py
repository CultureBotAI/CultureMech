"""Guard that the generated dataclasses match the schema (#149).

`culturemech_dataclasses.py` is produced from `culturemech.yaml` by pythongen,
but nothing regenerated it and nothing checked it. When #148 split `medium_type`
into three axis slots, the dataclasses kept June's shape and every one of the
11,088 backfilled records failed to load:

    MediaRecipe(**yaml.safe_load(record))
    TypeError: unexpected keyword argument 'composition_type'

`linkml-validate` reads the *schema*, so validate-strict passed on all 15,878
files while the dataclass API was broken — the same blind spot the id registry
(#144) and the recipe indexes (#125) had before they were guarded.

Regenerate with `just gen-dataclasses`.
"""
from __future__ import annotations

import dataclasses
import re
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"
GENERATED = REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech_dataclasses.py"
CORPUS = REPO_ROOT / "data" / "normalized_yaml"

STALE_HINT = "stale dataclasses — regenerate with `just gen-dataclasses`"

# The header carries a wall-clock timestamp, so it differs on every run and is
# not evidence of drift.
HEADER_NOISE = re.compile(r"^# Generation date:.*$", re.M)


def _normalize(text: str) -> str:
    return HEADER_NOISE.sub("# Generation date: <stripped>", text)


@pytest.fixture(scope="module")
def regenerated() -> str:
    proc = subprocess.run(
        [sys.executable, "-m", "linkml.generators.pythongen", str(SCHEMA)],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        pytest.skip(f"pythongen unavailable: {proc.stderr[-300:]}")
    return proc.stdout


def test_generated_dataclasses_match_schema(regenerated: str) -> None:
    """The tracked file is what the current schema generates."""
    assert _normalize(GENERATED.read_text()) == _normalize(regenerated), STALE_HINT


def _dataclasses_module():
    sys.path.insert(0, str(REPO_ROOT / "src"))
    import culturemech.schema.culturemech_dataclasses as module

    return module


def test_every_schema_slot_reaches_the_dataclasses() -> None:
    """Catches drift even if pythongen itself is unavailable in this env.

    Narrower than the full text comparison above, but it runs everywhere. Reads
    the real dataclass fields rather than grepping the source — pythongen emits
    inlined slots as `slot_name="x"` rather than `self.x`, so a text search
    reports false drift on them.
    """
    schema = yaml.safe_load(SCHEMA.read_text())
    declared = set(schema["classes"]["MediaRecipe"]["attributes"])
    generated = {f.name for f in dataclasses.fields(_dataclasses_module().MediaRecipe)}
    missing = sorted(declared - generated)
    assert not missing, f"{STALE_HINT}: MediaRecipe slots absent: {missing}"


def test_every_schema_enum_reaches_the_dataclasses() -> None:
    """Same, for enums — a new enum with no generated class is drift."""
    schema = yaml.safe_load(SCHEMA.read_text())
    module = _dataclasses_module()
    missing = sorted(name for name in schema.get("enums", {}) if not hasattr(module, name))
    assert not missing, f"{STALE_HINT}: enums absent: {missing}"


def test_a_real_record_loads_through_the_dataclasses() -> None:
    """The failure #149 actually reported, pinned so it cannot return.

    The two checks above compare text; this one exercises the API the way
    callers do. A record can only be constructed if every key it carries is a
    real field on the dataclass.
    """
    sys.path.insert(0, str(REPO_ROOT / "src"))
    from culturemech.schema.culturemech_dataclasses import MediaRecipe

    record = CORPUS / "bacterial" / "r2a_medium.yaml"
    if not record.exists():  # pragma: no cover - corpus reshuffles
        pytest.skip(f"{record} not present")
    data = yaml.safe_load(record.read_text())

    MediaRecipe(**data)  # raises TypeError on an unknown slot


def test_the_guard_is_not_vacuous() -> None:
    """A typo in the paths above would make every assertion pass trivially."""
    assert SCHEMA.exists() and GENERATED.exists()
    assert "MediaRecipe" in GENERATED.read_text()
