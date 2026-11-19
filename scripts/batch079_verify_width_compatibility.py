"""Verify the issue756 review-draft width repair without executing builders.

Purpose: prove a presentation-only successor and preserve historical bytes, 2026-11-15.
Inputs: --base Git commit, three current builders and their immutable saved reviews.
Outputs: JSON verification on stdout; no files or scientific records are written.
Context: CultureMech issue756; old/new serializer output is compared only in memory.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CASES = (
    ("batch079_build_record08_review.py", 110, "20261115T081711Z-batch079-record08-desulfotignum"),
    (
        "batch079_build_record08_review_v2.py",
        110,
        "20261115T081711Z-batch079-record08-desulfotignum",
    ),
    (
        "batch079_build_record10_review.py",
        100,
        "20261115T082226Z-batch079-record10-desulfotomaculum",
    ),
)


class NoAliasDumper(yaml.SafeDumper):
    """Match the unchanged alias policy of the three draft builders."""

    def ignore_aliases(self, data):
        return True


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    args = parser.parse_args()
    assert re.fullmatch(r"[0-9a-f]{40}", args.base), "Require the exact prior PR commit"
    assert Path.cwd().resolve() == ROOT
    protected = [
        "reviews/structured",
        "scripts/batch079_provenance/history",
        "scripts/batch079_provenance/manifest.json",
        "data",
        "tests/test_record_io.py",
    ]
    subprocess.run(
        ["git", "diff", "--exit-code", args.base, "--", *protected],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    results = []
    for name, old_width, review_id in CASES:
        relative = Path("scripts") / name
        previous = subprocess.check_output(
            ["git", "show", args.base + ":" + str(relative)], cwd=ROOT
        )
        current = (ROOT / relative).read_bytes()
        before_tree, after_tree = ast.parse(previous), ast.parse(current)
        calls = [
            node
            for node in ast.walk(before_tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "yaml"
            and node.func.attr == "dump"
        ]
        assert len(calls) == 1, relative
        removed = [item for item in calls[0].keywords if item.arg == "width"]
        assert len(removed) == 1 and ast.literal_eval(removed[0].value) == old_width, relative
        calls[0].keywords.remove(removed[0])
        assert ast.dump(before_tree) == ast.dump(after_tree), relative
        review_path = Path("reviews/structured") / review_id / "review.yaml"
        review_bytes = (ROOT / review_path).read_bytes()
        review = yaml.safe_load(review_bytes)
        old_text = yaml.dump(
            review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=old_width
        )
        new_text = yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True)
        assert yaml.safe_load(old_text) == yaml.safe_load(new_text) == review, relative
        assert (ROOT / review_path).read_bytes() == review_bytes
        results.append(
            {
                "path": str(relative),
                "before_sha256": sha(previous),
                "after_sha256": sha(current),
                "removed_width": old_width,
                "only_ast_change": "removed yaml.dump width keyword",
                "review_path": str(review_path),
                "review_sha256": sha(review_bytes),
                "old_serialization_sha256": sha(old_text.encode()),
                "new_serialization_sha256": sha(new_text.encode()),
                "parsed_content_equal": True,
            }
        )
    print(
        json.dumps(
            {
                "issue": 756,
                "base": args.base,
                "builders": results,
                "protected_paths_unchanged": protected,
                "builder_execution": False,
                "scope": "Saved review payloads round-trip equally; no author replay or new science review.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
