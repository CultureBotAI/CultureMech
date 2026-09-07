"""No script may hardcode a path that only exists on one machine (#430).

A literal `/Users/<name>/...` runs on one laptop and, when that checkout
moves, nowhere. The same is true of `Path.home() / "Documents/..."` and
`expanduser("~/Documents/...")`, which are the same path with the prefix cut
off; claw's guard missed that shape for a month (culturebotai-claw#365), so
this one refuses it from the start. Derive paths from the file's own location
(`Path(__file__).resolve().parent.parent`) and take another checkout's root
from its fleet environment variable.

A dot-directory under home (`~/.data/oaklib`, `/Users/x/.cache`) is a tool
cache, not a checkout, and stays allowed.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

_MACHINE_PATH = re.compile(
    r"""(
        /(?:Users|home)/[^/\s'"]+/(?!\.)          # /Users/name/x, not /Users/name/.cache
      | Documents/
      | Path\.home\(\)\s*/\s*['"](?!\.)          # Path.home() / "x", not / ".cache"
      | expanduser\(\s*['"]~/(?!\.)              # expanduser("~/x"), not "~/.cache"
    )""",
    re.VERBOSE,
)


def has_machine_path(source: str) -> bool:
    return _MACHINE_PATH.search(source) is not None


def _scripts() -> list[Path]:
    return sorted(SCRIPTS.glob("*.py"))


def test_there_are_scripts_to_check():
    """Guards the parametrization: an empty glob would pass everything."""
    assert len(_scripts()) >= 10, f"only {len(_scripts())} scripts found"


@pytest.mark.parametrize(
    "snippet",
    [
        'OUTPUT_DIR = Path("/Users/someone/Documents/VIMSS/ontology/X/data")',
        "root = Path.home() / 'Documents/VIMSS/ontology/X'",
        'root = os.path.expanduser("~/Documents/X")',
        'p = "/home/someone/checkouts/X/kb"',
    ],
)
def test_the_guard_recognises_each_shape(snippet):
    """Driven by an input the guard must refuse, so a loosened regex goes red."""
    assert has_machine_path(snippet), snippet


@pytest.mark.parametrize(
    "snippet",
    [
        'CACHE = Path.home() / ".data" / "oaklib" / "chebi.db"',
        'db = os.path.expanduser("~/.cache/x.db")',
        "# see /Users/someone/.claude/plans/notes.md",
        "ROOT = Path(__file__).resolve().parent.parent",
    ],
)
def test_the_guard_allows_caches_and_derived_paths(snippet):
    assert not has_machine_path(snippet), snippet


@pytest.mark.parametrize("path", _scripts(), ids=lambda p: p.name)
def test_no_script_hardcodes_a_machine_path(path):
    assert not has_machine_path(path.read_text(encoding="utf-8")), (
        f"{path.name} embeds a path that exists on one machine; derive it from "
        f"the file's own location or take the other checkout's root from its "
        f"environment variable"
    )
