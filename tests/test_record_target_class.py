"""The validation recipes pick a record's LinkML class from its shape (#450).

Kept free of corpus paths: these are fixtures, and conftest tiers a module by
substring.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "record_target_class.py"
sys.path.insert(0, str(REPO / "scripts"))

from record_target_class import target_class  # noqa: E402

SOLUTION = {
    "id": "CultureMech:900001",
    "preferred_term": "SL10",
    "term": {"id": "mediadive.solution:1"},
}
CURATED_SOLUTION = {
    "id": "CultureMech:900002",
    "name": "Trace salts",
    "record_kind": "SOLUTION",
    "ingredients": [],
}
MEDIUM = {"id": "CultureMech:900003", "name": "LB", "medium_type": "COMPLEX"}


def test_shape_decides_the_class():
    assert target_class(SOLUTION) == "SolutionRecipe"
    # a curated SOLUTION with MediaRecipe fields keeps the MediaRecipe shape (#175)
    assert target_class(CURATED_SOLUTION) == "MediaRecipe"
    assert target_class(MEDIUM) == "MediaRecipe"


@pytest.mark.parametrize(
    ("body", "expected"),
    [
        (
            "id: CultureMech:900001\npreferred_term: SL10\nterm:\n  id: mediadive.solution:1\n",
            "SolutionRecipe",
        ),
        ("id: CultureMech:900003\nname: LB\n", "MediaRecipe"),
    ],
)
def test_the_script_prints_the_class_for_a_file(tmp_path, body, expected):
    path = tmp_path / "r.yaml"
    path.write_text(body)
    out = subprocess.run([sys.executable, str(SCRIPT), str(path)], capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    assert out.stdout.strip() == expected


def test_an_unreadable_file_is_an_error_not_a_default_class(tmp_path):
    out = subprocess.run(
        [sys.executable, str(SCRIPT), str(tmp_path / "missing.yaml")],
        capture_output=True,
        text=True,
    )
    assert out.returncode == 1 and out.stdout == ""


def test_batch_mode_prints_one_line_per_record(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "sol.yaml").write_text(
        "id: CultureMech:900001\npreferred_term: SL10\nterm:\n  id: mediadive.solution:1\n"
    )
    (tmp_path / "a" / "med.yaml").write_text("id: CultureMech:900003\nname: LB\n")
    out = subprocess.run(
        [sys.executable, str(SCRIPT), "--all", str(tmp_path)], capture_output=True, text=True
    )
    assert out.returncode == 0, out.stderr
    lines = dict(line.split("\t") for line in out.stdout.splitlines())
    assert lines[str(tmp_path / "a" / "med.yaml")] == "MediaRecipe"
    assert lines[str(tmp_path / "a" / "sol.yaml")] == "SolutionRecipe"
