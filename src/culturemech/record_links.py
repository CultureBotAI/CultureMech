"""Verified published record membership for renderer and report links."""

from __future__ import annotations

import csv
import re
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=4)
def normalized_records(root: Path) -> dict[str, str]:
    """Stable IDs with an exact, still-present normalized source path."""
    registry = root / "data/culturemech_id_registry.tsv"
    if not registry.is_file():
        return {}
    candidates: dict[str, set[str]] = {}
    with registry.open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            path = Path(row["file_path"])
            identifier = row["culturemech_id"]
            if (
                path.parts[:2] == ("data", "normalized_yaml")
                and re.fullmatch(r"CultureMech:\d{6}", identifier)
                and (root / path).is_file()
            ):
                candidates.setdefault(identifier, set()).add(path.as_posix())
    return {
        identifier: next(iter(paths)) for identifier, paths in candidates.items() if len(paths) == 1
    }
