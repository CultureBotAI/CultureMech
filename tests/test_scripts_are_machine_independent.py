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

Scope is every Python source we ship, `scripts/*.py` and `src/**/*.py`, not
one directory: the first cut globbed `scripts/*.py` and so could not see the
same hardcode sitting in two importable modules that `just import-pfas-roles`
and `just import-pfas-cofactors` run (#432). Python sources only — the
`Documents/` branch is deliberately broad and would fire on prose.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
SRC = ROOT / "src"

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


def _python_sources() -> list[Path]:
    """Every Python source in the repository, both trees."""
    return sorted(SCRIPTS.glob("*.py")) + sorted(SRC.rglob("*.py"))


def test_both_trees_are_covered():
    """Guards the parametrization: an empty glob would pass everything, and a
    glob that reaches only one tree is how #432 stayed invisible."""
    found = _python_sources()
    assert len(found) >= 10, f"only {len(found)} Python sources found"
    for tree in (SCRIPTS, SRC):
        assert any(tree in p.parents for p in found), f"nothing found under {tree.name}/"


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


@pytest.mark.parametrize("path", _python_sources(), ids=lambda p: str(p.relative_to(ROOT)))
def test_no_python_source_hardcodes_a_machine_path(path):
    assert not has_machine_path(path.read_text(encoding="utf-8")), (
        f"{path.relative_to(ROOT)} embeds a path that exists on one machine; derive it from "
        f"the file's own location or take the other checkout's root from its "
        f"environment variable"
    )
