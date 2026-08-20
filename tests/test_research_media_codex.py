"""Tests for scripts/research_media_codex.py (#284).

The two things worth defending are the ones that fail quietly: a prompt shipped with
unfilled placeholders, and a run that cites nothing but exits 0.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from research_media_codex import (  # noqa: E402
    PREAMBLE, build_prompt, preflight, source_count,
)


def test_placeholders_are_actually_filled(tmp_path):
    """The first version substituted `{{key}}` against a `{key}` template and shipped the
    raw template as the prompt. --dry-run caught it; this keeps it caught."""
    tpl = tmp_path / "t.md"
    tpl.write_text("Record: {record_path}\nName: {media_name}\n")
    doc = {"name": "lb_broth", "id": "CultureMech:009646"}
    out = build_prompt(doc, REPO / "data/normalized_yaml/bacterial/lb_broth.yaml", tpl)
    assert "{record_path}" not in out and "{media_name}" not in out
    assert out.startswith(PREAMBLE)


def test_an_unfillable_placeholder_raises_rather_than_shipping_a_hole(tmp_path):
    tpl = tmp_path / "t.md"
    tpl.write_text("Known: {media_name}\nUnknown: {not_a_real_variable}\n")
    with pytest.raises(ValueError, match="not_a_real_variable"):
        build_prompt({"name": "x"}, REPO / "data/normalized_yaml/bacterial/lb_broth.yaml", tpl)


def test_the_preamble_demands_web_search_and_urls():
    """Without this the model answers from memory and the report looks researched."""
    low = PREAMBLE.lower()
    assert "web search" in low
    assert "url" in low
    assert "do not answer from memory" in low


def test_source_count_is_distinct_urls_not_mentions():
    text = ("see https://example.org/a and https://example.org/a again, "
            "plus https://example.org/b).")
    assert source_count(text) == 2
    assert source_count("no links here") == 0
    assert source_count("") == 0


def test_preflight_reports_problems_rather_than_raising():
    """It must be callable even when Codex is absent — --dry-run relies on that."""
    problems = preflight()
    assert isinstance(problems, list)
    assert all(isinstance(p, str) and p for p in problems)
