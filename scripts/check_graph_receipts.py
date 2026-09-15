#!/usr/bin/env python3
"""Check committed graph artifacts before deployment; no vectors or models are loaded."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from culturemech.graph_embedding_receipts import corpus_receipt, load_receipt  # noqa: E402

CORPUS_RELATIVE = "data/normalized_yaml"
RECEIPTS = [("app/ingredient_umap.metadata.json", ("pacmap", "umap"))]
POINT_ID = "chebi_id"


def check_graph_receipts(root: Path = REPO_ROOT) -> list[dict]:
    """Bind each intended HTML/points pair to its full current corpus and receipt."""
    root = root.resolve()
    corpus = root / CORPUS_RELATIVE
    if corpus.is_symlink() or not corpus.is_dir():
        raise ValueError(f"missing real graph corpus: {corpus}")
    paths = sorted(corpus.rglob("*.yaml"))
    current = corpus_receipt(paths, corpus)
    checked = []
    for relative, allowed_methods in RECEIPTS:
        metadata = root / relative
        receipt = load_receipt(metadata)
        basename = metadata.name.removesuffix(".metadata.json")
        expected = {basename + ".html", basename + ".points.json"}
        if set(receipt["outputs"]) != expected:
            raise ValueError(
                f"graph receipt does not bind the intended HTML/points pair: {metadata}"
            )
        if receipt["projection"]["method"] not in allowed_methods:
            raise ValueError(f"unexpected graph reducer for {metadata}")
        if receipt["corpus"] != current:
            raise ValueError(f"graph corpus changed since generation: {metadata}")
        points = json.loads((metadata.parent / (basename + ".points.json")).read_text())
        if (
            not isinstance(points, list)
            or len(points) != receipt["coverage"]["projected"]
            or any(
                not isinstance(row, dict)
                or not all(
                    isinstance(row.get(axis), (int, float))
                    and not isinstance(row[axis], bool)
                    and math.isfinite(row[axis])
                    for axis in ("umap_x", "umap_y")
                )
                for row in points
            )
            or [row.get(POINT_ID) for row in points] != receipt["matrix"]["row_ids"]
        ):
            raise ValueError(f"graph points differ from the ordered receipt: {metadata}")
        checked.append(
            {
                "receipt": relative,
                "points": len(points),
                "source_sha256": receipt["source"]["sha256"],
            }
        )
    return checked


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    try:
        result = check_graph_receipts(args.root)
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"graph publication refused: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"verified_graphs": result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
