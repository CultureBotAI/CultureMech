"""Apply only the reviewed three-record UTEX concentration proposal."""

import argparse
import json
import os
import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path

import review_solution_concentration_evidence as runner
from review_utex_f2_concentrations import safe_path
from review_yeast_mineral_ingredients import _stage

from culturemech.validation.write_validated import validate_recipe

FOLDER = Path("reports/ingredient_concentration_curation/20261010-utex-volvocacean-bg11")
SOURCE = FOLDER / "plan-v2.json"
SOURCE_SHA = "78ad345b1084bd72ad49ae3235a0f8d0aebb2041f52f8f222e0aef8dc2c194ff"
ACTION = "CURATED_UTEX_VOLVOCACEAN_BG11_CONCENTRATION_EVIDENCE"


def serialized(value):
    return json.dumps(value, sort_keys=True)


def approved(root):
    if not __debug__:
        raise RuntimeError("Guarded curation requires assertions; do not use -O")
    root = Path(root).resolve()
    source = root / SOURCE
    assert source.resolve().is_relative_to(root)
    assert not any(
        root.joinpath(*SOURCE.parts[:i]).is_symlink() for i in range(1, len(SOURCE.parts) + 1)
    )
    raw = source.read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Reviewed proposal drift"
    plan = json.loads(raw)
    assert len(plan["records"]) == len({r["path"] for r in plan["records"]}) == 3
    assert {r["id"] for r in plan["records"]} == {
        "CultureMech:000236",
        "CultureMech:000026",
        "CultureMech:000027",
    }
    for item in plan["records"]:
        assert item["action"] == ACTION
        for key in ("before", "after"):
            assert runner.sha(item[f"{key}_text"].encode()) == item[f"{key}_sha256"]
            assert runner.load_yaml(item[f"{key}_text"])["id"] == item["id"]
    return plan


def evidence_count(node):
    if isinstance(node, dict):
        return sum(
            len(value) if key == "evidence" else evidence_count(value)
            for key, value in node.items()
        )
    return sum(map(evidence_count, node)) if isinstance(node, list) else 0


def check(before, after, item, root=None):
    """Invert exact reviewed paths and independently count evidence additions."""
    pinned = next(
        r
        for r in approved(Path.cwd() if root is None else root)["records"]
        if r["path"] == item["path"]
    )
    assert serialized(item) == serialized(pinned), "Unreviewed audit item"
    assert serialized(before) == serialized(runner.load_yaml(pinned["before_text"]))
    assert serialized(after) == serialized(runner.load_yaml(pinned["after_text"]))
    restored = deepcopy(after)
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"]) == {"fields": item["changes"], "counts": item["counts"]}
    counts = Counter(new_curation_history=1)
    for change in reversed(item["changes"]):
        node = runner.get_node(restored, change["pointer"][:-1])
        key = change["pointer"][-1]
        present = 0 <= key < len(node) if isinstance(node, list) else key in node
        assert present == change["after_present"]
        if present:
            assert serialized(node[key]) == serialized(change["new"])
        if change["before_present"]:
            node[key] = deepcopy(change["old"])
        else:
            del node[key]
        counts[change["counter"]] += 1
    counts["new_evidence"] = evidence_count(after) - evidence_count(before)
    assert serialized(restored) == serialized(before), "Out-of-scope change"
    assert dict(counts) == item["counts"]
    return counts


def preflight(plan, root, *, verify=False):
    root = Path(root).resolve()
    assert serialized(plan) == serialized(approved(root)), "Only the reviewed plan is permitted"
    tracked = set(
        subprocess.check_output(
            ["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root, text=True
        ).split("\0")
    )
    pending = []
    for item in plan["records"]:
        assert item["path"] in tracked, "Untracked or non-exact path"
        path = safe_path(root, item["path"])
        assert path.is_file() and path.stat().st_nlink == 1, "Non-regular or hardlinked target"
        before, after = (runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
        check(before, after, item, root)
        assert not validate_recipe(before, target_class="MediaRecipe"), "Invalid baseline"
        assert not validate_recipe(after, target_class="MediaRecipe"), "Invalid proposal"
        old, new = (item[key].encode() for key in ("before_text", "after_text"))
        current = path.read_bytes()
        if current == new:
            continue
        assert not verify and current == old, "Concurrent edit or unapplied verify target"
        pending.append((path, old, new))
    return pending


def apply(plan, root, *, dry_run=True, verify=False):
    root = Path(root).resolve()
    pending = preflight(plan, root, verify=verify)
    if dry_run or verify:
        return {"changed": 0, "pending": len(pending), "already_applied": 3 - len(pending)}
    staged, written = [], []
    try:
        for target, old, new in pending:
            staged.append((_stage(target, new), target, old, new))
        assert preflight(plan, root) == pending, "Concurrent edit during staging"
        for temporary, target, old, new in staged:
            safe_path(root, target.relative_to(root))
            assert (
                target.stat().st_nlink == 1 and target.read_bytes() == old
            ), "Concurrent edit during write"
            os.replace(temporary, target)
            written.append((target, old, new))
            assert target.read_bytes() == new, "Readback mismatch"
        assert not preflight(plan, root, verify=True)
    except BaseException as error:
        failures = []
        for target, old, new in reversed(written):
            backup = None
            try:
                safe_path(root, target.relative_to(root))
                assert target.read_bytes() == new, "Preserving concurrent edit during rollback"
                backup = _stage(target, old)
                safe_path(root, target.relative_to(root))
                assert target.read_bytes() == new, "Preserving concurrent edit during rollback"
                os.replace(backup, target)
                assert target.read_bytes() == old
            except BaseException as rollback_error:
                failures.append(f"{target.relative_to(root)}: {rollback_error}")
            finally:
                if backup is not None:
                    backup.unlink(missing_ok=True)
        if failures:
            raise RuntimeError("Partial application; inspect: " + "; ".join(failures)) from error
        raise
    finally:
        for temporary, *_ in staged:
            temporary.unlink(missing_ok=True)
    return {"changed": len(pending), "pending": 0, "already_applied": 3 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            apply(approved(args.root), args.root, dry_run=not args.apply, verify=args.verify),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
