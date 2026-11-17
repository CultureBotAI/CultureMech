"""Audit exact reviewed variant successors without exempting earlier science.

Purpose: bridge historical recipe receipts to #683 additions (#772, 2026-11-16).
Inputs: digest-pinned retained recipe/proposal snapshots and a proposed edge.
Output: verified structural counters; no writes or scientific certification.
The #775 capsule survives squash merges without depending on unreachable Git
objects. Its producer authenticates the retained bytes against original Git.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from functools import lru_cache
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
PLAN_SHA256 = "daa490e8c97cce85edaf7cb768c9fafe7d25e912c9f84b07af6c3db667943dd4"
CAPSULE = PLAN.parent / "evidence-capsule-775"
CAPSULE_SHA256 = "8f2c7a3b6df6ca9261f752ee9453ac24ec3ba26c34fce0e385cd907c623ca93d"
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


@lru_cache(maxsize=1)
def retained_evidence():
    """Authenticate exact retained bytes before interpreting any historical edge."""
    assert not CAPSULE.is_symlink(), "Capsule directory cannot be a symlink"
    manifest_raw = (CAPSULE / "manifest.json").read_bytes()
    assert sha(manifest_raw) == CAPSULE_SHA256, "Reviewed capsule manifest changed"
    manifest = json.loads(manifest_raw)
    assert manifest["contract"] == "culturemech-variant-successor-capsule-v1"
    assert manifest["base_commit"] == BASE and manifest["applied_commit"] == RESULT
    assert set(manifest["proposals"]) == set(PROPOSALS), "Reviewed proposal membership changed"
    plan_raw = PLAN.read_bytes()
    assert sha(plan_raw) == PLAN_SHA256, "Reviewed plan changed"
    assert manifest["plan"] == {
        "path": str(PLAN.relative_to(ROOT)),
        "sha256": PLAN_SHA256,
        "bytes": len(plan_raw),
    }, "Reviewed plan binding changed"
    plan = json.loads(plan_raw)
    assert plan["base_commit"] == BASE and plan["applied_commit"] == RESULT
    records = {item["path"]: item for item in plan["records"]}
    assert len(records) == len(plan["records"]) == manifest["records"] == 87
    assert sorted(records) == manifest["record_paths"], "Reviewed record membership changed"
    expected_files = {"manifest.json"}
    proposals = {}
    for source_path, fingerprint in manifest["proposals"].items():
        relative = Path(fingerprint["path"])
        assert relative == Path("proposals") / Path(source_path).name, "Unsafe capsule path"
        expected_files.add(relative.as_posix())
        raw = (CAPSULE / relative).read_bytes()
        assert (
            len(raw) == fingerprint["bytes"] and sha(raw) == fingerprint["sha256"]
        ), "Reviewed capsule proposal changed"
        proposals[source_path] = (sha(raw), json.loads(raw))
    actual_files = set()
    for path in CAPSULE.rglob("*"):
        assert not path.is_symlink(), "Capsule cannot contain symlinks"
        if path.is_file():
            actual_files.add(path.relative_to(CAPSULE).as_posix())
    assert actual_files == expected_files, "Reviewed capsule file membership changed"
    return records, proposals


@lru_cache(maxsize=1)
def proposal_records():
    edges, proposals = retained_evidence()
    records = {}
    for path in PROPOSALS:
        digest, proposal = proposals[path]
        for record in proposal["records"]:
            relative = record["path"]
            assert relative not in records, "Duplicate reviewed successor path"
            assert relative.startswith("data/normalized_yaml/") and relative.endswith(".yaml")
            records[relative] = (path, digest, record)
    assert len(records) == 87, "Reviewed successor membership changed"
    assert set(records) == set(edges), "Reviewed proposal/edge membership differs"
    return records


def expected_item(path):
    """Reconstruct an edge from authenticated snapshots and separately pinned proposals."""
    proposal_path, proposal_sha, proposal = proposal_records()[path]
    item = {
        "path": path,
        "id": proposal["recipe_id"],
        "action": ACTION,
        "proposal_path": proposal_path,
        "proposal_sha256": proposal_sha,
    }
    frozen = retained_evidence()[0][path]
    for label in ("before", "after"):
        raw = frozen[label + "_text"].encode("utf-8")
        assert sha(raw) == frozen[label + "_sha256"], "Retained snapshot hash mismatch"
        item[label + "_text"] = raw.decode("utf-8")
        item[label + "_sha256"] = sha(raw)
    assert item["before_sha256"] != item["after_sha256"], "No-op successor"
    return item


def check(before, after, item):
    """Verify the exact edge, addition payload, single event and complete base restoration.

    This audits adoption of already reviewed claims. It does not grant new source
    approval or permit any later changes merely because their hashes were updated.
    """
    assert item == expected_item(item["path"]), "Successor differs from reviewed retained snapshots"
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
