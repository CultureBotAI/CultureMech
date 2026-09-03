"""A source component name must not carry invisible characters (#406).

TOGO serves `Trace metals 'Gaffron\xad+Se'` — with U+00AD SOFT HYPHEN between
`Gaffron` and `+Se`. A discretionary hyphen renders as nothing unless a line
breaks there, so the name looked correct in every editor, diff and report while
being a different string to every matcher: it could not ground, and it was the
last surviving fragment of #387.

The character is a soft-wrap artifact of the source page, not part of the name,
and it came through the import verbatim.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _importer():
    spec = importlib.util.spec_from_file_location(
        "togo_importer", REPO_ROOT / "src" / "culturemech" / "import" / "togo_importer.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def clean():
    return _importer().clean_component_name


def test_the_soft_hyphen_that_started_this_is_removed(clean):
    assert clean("Trace metals 'Gaffron\xad+Se'") == "Trace metals 'Gaffron+Se'"


@pytest.mark.parametrize(
    "code", [0x00AD, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF], ids=lambda c: f"U+{c:04X}"
)
def test_every_zero_width_character_is_stripped(clean, code):
    assert clean(f"Na{chr(code)}Cl") == "NaCl"


def test_a_non_breaking_space_becomes_a_space_rather_than_vanishing(clean):
    """NBSP is *visible*. Deleting it would join two words into one."""
    assert clean("Yeast extract") == "Yeast extract"


def test_a_clean_name_is_returned_unchanged(clean):
    for name in ("NaCl", "MgSO4 x 7 H2O", "Trace metals 'Gaffron+Se'", "PABA(p-aminobenzoic acid)"):
        assert clean(name) == name


def test_meaningful_punctuation_survives(clean):
    """A real hyphen, a middle dot and a bullet are content, not formatting."""
    assert clean("L-cysteine") == "L-cysteine"
    assert clean("CaCl2·2H2O") == "CaCl2·2H2O"
    assert clean("MgSO4•7H2O") == "MgSO4•7H2O"


@pytest.mark.parametrize("empty", [None, "", "   ", "​"])
def test_an_empty_or_invisible_only_name_yields_the_empty_string(clean, empty):
    assert clean(empty) == ""


@pytest.mark.corpus
def test_no_ingredient_name_in_the_corpus_carries_an_invisible_character(corpus):
    """The corpus-side assertion. One record carried one; it is repaired."""
    invisible = {0x00AD, 0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF}
    offenders = []

    def walk(items):
        for ingredient in items or []:
            if not isinstance(ingredient, dict):
                continue
            name = str(ingredient.get("preferred_term", ""))
            if any(ord(ch) in invisible for ch in name):
                offenders.append(ascii(name))
            walk(ingredient.get("composition"))

    for _path, record in corpus:
        walk(record.get("ingredients"))
        walk(record.get("solutions"))

    assert not offenders, f"{len(offenders)} name(s) carry invisible characters: {offenders[:5]}"
