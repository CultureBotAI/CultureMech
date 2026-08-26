#!/usr/bin/env python3
"""Verify CultureMech's vendored MediaIngredientMech label-index pin."""

from __future__ import annotations

from pathlib import Path

from culturemech.ingredients.mim_label_index import MIMLabelIndex

REPO_ROOT = Path(__file__).resolve().parent.parent
RESOURCE_DIR = REPO_ROOT / "src" / "culturemech" / "data" / "mediaingredientmech"
INDEX_PATH = RESOURCE_DIR / "label_index.csv"
METADATA_PATH = RESOURCE_DIR / "label_index.metadata.json"


def main() -> int:
    index = MIMLabelIndex.from_paths(INDEX_PATH, METADATA_PATH)
    answers = index.semantic_answers()
    states: dict[str, int] = {}
    for _identifier, state, _ambiguity in answers.values():
        states[state] = states.get(state, 0) + 1

    print(
        "MIM label index OK: "
        f"{len(index.rows):,} rows, {len(answers):,} labels, "
        f"commit {index.metadata['source_commit']}"
    )
    print("Decisions: " + ", ".join(f"{key}={states[key]:,}" for key in sorted(states)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
