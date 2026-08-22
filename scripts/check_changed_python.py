#!/usr/bin/env python3
"""Run Ruff and Black on changed hand-written Python files."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {"src/culturemech/schema/culturemech_dataclasses.py"}


def select_python_files(paths: Sequence[str]) -> list[str]:
    """Keep existing, hand-written Python files in deterministic order."""
    return sorted(
        {
            path
            for path in paths
            if path.endswith(".py") and path not in EXCLUDED and (ROOT / path).is_file()
        }
    )


def default_base() -> str:
    base_ref = os.environ.get("GITHUB_BASE_REF")
    if base_ref:
        return f"origin/{base_ref}"
    before = os.environ.get("GITHUB_EVENT_BEFORE", "")
    if before and set(before) != {"0"}:
        return before
    return "HEAD^"


def changed_paths(base: str) -> list[str]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--no-renames",
            "--name-only",
            "--diff-filter=ACMR",
            f"{base}...HEAD",
            "--",
            "*.py",
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or f"could not diff against {base}")
    return result.stdout.splitlines()


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default=default_base())
    args = parser.parse_args(argv)
    try:
        files = select_python_files(changed_paths(args.base))
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    if not files:
        print("No changed hand-written Python files.")
        return 0
    print(f"Checking {len(files)} changed Python file(s).")
    ruff = subprocess.run([sys.executable, "-m", "ruff", "check", *files], cwd=ROOT).returncode
    black = subprocess.run([sys.executable, "-m", "black", "--check", *files], cwd=ROOT).returncode
    return 1 if ruff or black else 0


if __name__ == "__main__":
    raise SystemExit(main())
