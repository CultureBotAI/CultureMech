#!/usr/bin/env python3
"""Remove only explicitly ignored generated paths, never tracked content."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from collections.abc import Sequence
from pathlib import Path

GENERATED_DIRECTORIES = (
    "output",
    "pages/media",
    "pages/normalized",
    "pages/single",
    "htmlcov",
    ".pytest_cache",
)
GENERATED_FILES = (
    "pages/index.html",
    "pages/style.css",
    "pages/mermaid-init.js",
    "app/data.js",
)
GENERATED_PATHS = GENERATED_DIRECTORIES + GENERATED_FILES


def git_output(root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip() or "git command failed")
    return result.stdout.strip()


def validate_targets(root: Path) -> None:
    """Refuse the whole cleanup if a target is tracked or not ignored."""
    problems: list[str] = []
    for relative in GENERATED_PATHS:
        tracked = git_output(root, "ls-files", "--", relative)
        if tracked:
            problems.append(f"tracked path: {relative}")
        ignore_probe = (
            f"{relative}/.culturemech-clean-check"
            if relative in GENERATED_DIRECTORIES
            else relative
        )
        ignored = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", "--", ignore_probe],
            cwd=root,
            check=False,
        )
        if ignored.returncode != 0:
            problems.append(f"not ignored: {relative}")
    if problems:
        raise RuntimeError("refusing cleanup:\n  " + "\n  ".join(problems))


def clean(root: Path) -> None:
    validate_targets(root)
    for relative in GENERATED_PATHS:
        target = root / relative
        if target.is_dir() and not target.is_symlink():
            shutil.rmtree(target)
        elif target.exists() or target.is_symlink():
            target.unlink()

    for cache_dir in root.rglob("__pycache__"):
        if ".venv" not in cache_dir.parts and cache_dir.is_dir():
            shutil.rmtree(cache_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        clean(args.root.resolve())
    except RuntimeError as error:
        print(error)
        return 1
    print("Cleaned ignored generated files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
