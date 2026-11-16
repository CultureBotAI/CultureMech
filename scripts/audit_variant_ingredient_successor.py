"""Audit exact reviewed variant successors without exempting earlier science.

Purpose: bridge historical recipe receipts to #683 additions (#772, 2026-11-16).
Inputs: immutable Git recipe/proposal snapshots and a proposed successor edge.
Output: verified structural counters; no writes or scientific certification.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from functools import cache, lru_cache
from pathlib import Path

import yaml
from adhoc.audit_variant_coverage_683 import check_preservation

ROOT = Path(__file__).resolve().parents[1]
BASE = "02e005db42246b8a04ece9df4b5657e036fa5697"
RESULT = "c03bbcef0a971439a367fcc89fc6a8c86a5b17b8"
ACTION = "REGISTERED_VARIANT_INGREDIENT_SUCCESSOR"
PLAN = (
    ROOT
    / "reports/ingredient_concentration_curation/20261116-variant-ingredient-occurrences/plan.json"
)
PROPOSALS = tuple(
    f"conf/variant_ingredient_curation/{name}.json"
    for name in (
        "bbm-canary-683",
        "utex-optional-683",
        "remaining-families-683",
        "carini-jensen-pinchuk-tang-683",
        "bacterial-specialized-683",
        "algae-archaea-683",
    )
)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


@cache
def snapshot(revision, path):
    """Read only the two explicit immutable revisions, never working-tree recipes."""
    assert revision in {BASE, RESULT}, "Unreviewed successor revision"
    relative = Path(path)
    assert not relative.is_absolute() and ".." not in relative.parts, "Unsafe snapshot path"
    return subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=ROOT)


@lru_cache(maxsize=1)
def proposal_records():
    records = {}
    for path in PROPOSALS:
        raw = snapshot(RESULT, path)
        proposal = json.loads(raw)
        for record in proposal["records"]:
            relative = record["path"]
            assert relative not in records, "Duplicate reviewed successor path"
            assert relative.startswith("data/normalized_yaml/") and relative.endswith(".yaml")
            records[relative] = (path, sha(raw), record)
    assert len(records) == 87, "Reviewed successor membership changed"
    return records


def expected_item(path):
    """Construct one exact edge from reviewed immutable bytes, independent of the plan."""
    proposal_path, proposal_sha, proposal = proposal_records()[path]
    item = {
        "path": path,
        "id": proposal["recipe_id"],
        "action": ACTION,
        "proposal_path": proposal_path,
        "proposal_sha256": proposal_sha,
    }
    for label, revision in (("before", BASE), ("after", RESULT)):
        raw = snapshot(revision, path)
        item[label + "_text"] = raw.decode("utf-8")
        item[label + "_sha256"] = sha(raw)
    assert item["before_sha256"] != item["after_sha256"], "No-op successor"
    return item


def check(before, after, item):
    """Verify the exact edge, addition payload, single event and complete base restoration.

    This audits adoption of already reviewed claims. It does not grant new source
    approval or permit any later changes merely because their hashes were updated.
    """
    assert item == expected_item(item["path"]), "Successor differs from reviewed Git snapshots"
    assert before == yaml.load(item["before_text"], Loader=yaml.CSafeLoader), "Baseline changed"
    assert after == yaml.load(
        item["after_text"], Loader=yaml.CSafeLoader
    ), "Successor content changed"
    assert before["id"] == after["id"] == item["id"], "Successor identity changed"
    _, proposal_sha, proposal = proposal_records()[item["path"]]
    check_preservation(before, after, proposal, proposal_sha, "postapply")
    return Counter(
        {
            "new_variant_ingredient_changes": sum(
                len(variant["ingredient_changes"]) for variant in proposal["variants"]
            ),
            "new_curation_history": 1,
        }
    )


def restore_before(raw, path):
    """Return exact historical bytes only after auditing this one registered successor.

    Unchanged/unrelated records pass through; any drift on a registered path fails.
    Historical source-specific tests can then retain all their original assertions.
    """
    if path not in proposal_records():
        return raw
    item = expected_item(path)
    assert sha(raw) == item["after_sha256"], "Current variant successor hash mismatch"
    before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
    after = yaml.load(raw, Loader=yaml.CSafeLoader)
    check(before, after, item)
    return item["before_text"].encode("utf-8")
