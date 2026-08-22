"""Curation timestamps reject absurd years without consulting the wall clock."""

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _curation_timestamp_patterns() -> list[str]:
    patterns = []
    for path in sorted(ROOT.glob("src/*/schema/*.yaml")):
        schema = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        event = (schema.get("classes") or {}).get("CurationEvent")
        if event:
            timestamp = (event.get("attributes") or {}).get("timestamp") or {}
            patterns.append(timestamp.get("pattern", ""))
    return patterns


def test_one_curation_event_schema_has_the_deterministic_year_guard():
    patterns = _curation_timestamp_patterns()
    assert patterns == [r"^20[0-9]{2}-"]


def test_year_guard_accepts_21st_century_and_rejects_the_2206_typo():
    pattern = _curation_timestamp_patterns()[0]
    assert re.match(pattern, "2026-08-22T12:00:00Z")
    assert not re.match(pattern, "2206-08-22T12:00:00Z")
