"""Records live only in the schema's category directories (#422).

The create-recipe skill told curators to save stock solutions under
`data/normalized_yaml/solutions/`. That directory held the MediaDive solution
records until `fe5b2f016d` (2026-04-04) moved them into `bacterial/`; since
then it has held one legacy index and nothing scans it. A record written there
would validate, be assigned an id, and be invisible to every corpus gate.

This pins the layout the rest of the tooling assumes: every directory under
the normalized corpus that holds a record is a `CategoryEnum` value.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
NORMALIZED = ROOT / "data" / "normalized_yaml"
SCHEMA = ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"


def _category_values() -> set[str]:
    schema = yaml.safe_load(SCHEMA.read_text())
    return set(schema["enums"]["CategoryEnum"]["permissible_values"])


def _directories_holding_records() -> set[str]:
    """Directories with a TRACKED record. Git, not the filesystem, is the oracle:
    a local import run can leave an untracked directory of YAML beside the
    corpus (an `imported/` tree was sitting here when this test was written),
    and that is a workstation state, not the repository's layout (#419)."""
    listing = subprocess.run(
        ["git", "ls-files", "-z", "--", "data/normalized_yaml"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    holding: set[str] = set()
    for entry in listing.split("\0"):
        parts = Path(entry).parts
        if len(parts) >= 4 and entry.endswith(".yaml"):
            holding.add(parts[2])
    return holding


def test_every_directory_holding_records_is_a_schema_category() -> None:
    categories = _category_values()
    holding = _directories_holding_records()
    assert holding, "no record directories found; is this the right checkout?"
    assert holding <= categories, (
        f"records found outside the schema's categories: {sorted(holding - categories)}. "
        f"Stock solutions carry `record_kind: SOLUTION` and live in the category "
        f"directory of the media they serve, not in a directory of their own (#422)."
    )


def test_the_guard_is_not_vacuous() -> None:
    """Five populated category directories is what the corpus looks like today.
    The enum also carries `imported`, a transitional value ("to be
    recategorized") that no record and no directory uses."""
    populated = {"bacterial", "fungal", "archaea", "specialized", "algae"}
    assert _directories_holding_records() == populated
    assert _category_values() == populated | {"imported"}


def test_the_legacy_solutions_directory_holds_no_records() -> None:
    assert "solutions" not in _directories_holding_records()
    assert (
        NORMALIZED / "solutions" / "mediadive_solution_index.json"
    ).is_file(), "the legacy index is gone; update DATA_LAYERS.md, which says it is still there"
