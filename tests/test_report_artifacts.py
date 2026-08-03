"""Guard that regenerated diagnostics are not tracked (#157).

`reports/chebi_consistency.tsv` was tracked, rewritten by `just
check-chebi-grounding`, and never compared against its committed copy — so it
drifted 73 insertions / 82 deletions behind the corpus while the CI gate stayed
green. The gate passes or fails on `--max-allowed` for the *current* corpus; it
never looks at the file.

That is the #145 pattern, but the remedy here differs from #125 and #144. Those
guarded the indexes and the id registry by asserting they match the corpus,
because those artifacts are *consumed* — things resolve ids and enumerate recipes
through them. This one is a diagnostic nobody reads: no script or document loads
it, and the workflow already uploads a fresh copy on every run via
`if: always()`. Regenerating and committing it on every corpus change would be
churn on a file with no readers.

So the fix is to stop tracking it, and this test keeps it that way — an untracked
file cannot rot, but it can be re-added by someone running the recipe and
`git add -A`.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

# Regenerated from the corpus by a single command, with no reader in the repo.
# Adding to this list means: it must stay untracked AND stay ignored.
REGENERATED_DIAGNOSTICS = [
    "reports/chebi_consistency.tsv",
]


def _tracked(path: str) -> bool:
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "--error-unmatch", path],
        capture_output=True,
    ).returncode == 0


@pytest.mark.parametrize("path", REGENERATED_DIAGNOSTICS)
def test_regenerated_diagnostic_is_not_tracked(path: str):
    assert not _tracked(path), (
        f"{path} is tracked again. It is regenerated from the corpus, so a "
        f"committed copy can only go stale — that is how it drifted 73/82 lines "
        f"behind while CI stayed green (#157). Run `git rm --cached {path}`."
    )


@pytest.mark.parametrize("path", REGENERATED_DIAGNOSTICS)
def test_regenerated_diagnostic_is_gitignored(path: str):
    """Untracking without ignoring leaves it showing up in every `git status`,
    which is how it gets re-added by a `git add -A`."""
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "check-ignore", path], capture_output=True
    )
    assert result.returncode == 0, f"{path} is not gitignored; add it to .gitignore"


def test_the_generator_still_exists():
    """Untracking is only safe while the file remains one command away.

    If the recipe that produces it is ever removed, the reasoning here changes and
    this guard should be revisited rather than silently protecting nothing.
    """
    justfile = (REPO_ROOT / "project.justfile").read_text()
    assert "check-chebi-grounding" in justfile
    assert "reports/chebi_consistency.tsv" in justfile
