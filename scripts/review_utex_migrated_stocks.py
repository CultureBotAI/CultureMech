"""Apply the reviewed three-stock UTEX evidence proposal, with no numeric changes."""

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

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

FOLDER = Path("reports/ingredient_concentration_curation/20261010-utex-migrated-stocks")
SOURCE = Path(
    "reports/ingredient_concentration_curation/20261010-utex-migrated-stock-preview/"
    "mutation-preview-v1/plan.json"
)
SOURCE_SHA = "0cf3a08ff882d4bb2fd8d46b4cd3f376d1ad17939ccb9640ad402b1edd086b5b"
ACTION = "CURATED_UTEX_MIGRATED_STOCK_CONCENTRATION_EVIDENCE"
TIMESTAMP = "2026-10-10T06:43:40+00:00"


def serialized(value):
    return json.dumps(value, sort_keys=True)


def approved(root):
    if not __debug__:
        raise RuntimeError("Guarded curation requires assertions; do not use -O")
    root = Path(root).resolve()
    path = root / SOURCE
    assert path.resolve().is_relative_to(root)
    assert all(
        not (root / Path(*SOURCE.parts[:index])).is_symlink()
        for index in range(1, len(SOURCE.parts) + 1)
    )
    raw = path.read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Reviewed source proposal drift"
    source = json.loads(raw)
    records = []
    for original in source["records"]:
        item = deepcopy(original)
        before, after = (runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
        assert before["id"] == after["id"] == item["id"]
        assert runner.sha(item["before_text"].encode()) == item["before_sha256"]
        assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
        event = after["curation_history"].pop()
        assert after["curation_history"] == before["curation_history"]
        changes = json.loads(event["changes"])
        for claim in item["claims"]:
            claim["action_taken"] = (
                "Added scoped PARTIAL evidence; existing amount and identity remain unresolved"
                if claim["status"] == "conflict"
                else "Added scoped SUPPORT evidence; numeric value retained"
            )
        changes["claims"] = item["claims"]
        record_curation_event(
            after,
            curator="codex",
            action=ACTION,
            timestamp=TIMESTAMP,
            source=item["reference"],
            notes=event["notes"],
            changes=serialized(changes),
        )
        output = runner.render(item["before_text"], after)
        item.update(after_text=output.decode(), after_sha256=runner.sha(output))
        records.append(item)
    assert len({r["path"] for r in records}) == len(records) == 3
    return {"source_sha256": SOURCE_SHA, "records": records}


def check(before, after, item, root=None):
    """Restore only the allowed evidence, notes, bibliography and appended event."""
    reviewed = next(
        r
        for r in approved(Path.cwd() if root is None else root)["records"]
        if r["path"] == item["path"]
    )
    assert serialized(item) == serialized(reviewed), "Unreviewed audit entry"
    assert serialized(before) == serialized(runner.load_yaml(reviewed["before_text"]))
    assert serialized(after) == serialized(
        runner.load_yaml(reviewed["after_text"])
    ), "Unreviewed content"
    restored = deepcopy(after)
    counts = Counter()
    for index, (old, new) in enumerate(
        zip(before["composition"], restored["composition"], strict=True)
    ):
        evidence = new.pop("evidence")
        assert len(evidence) == 1 and evidence[0]["reference"] == item["reference"]
        claim = item["claims"][index]
        assert evidence[0]["snippet"] == claim["snippet"]
        assert evidence[0]["supports"] == (
            "PARTIAL" if claim["status"] == "conflict" else "SUPPORT"
        )
        assert claim["field"] in evidence[0]["explanation"]
        assert claim["basis_snippet"] in evidence[0]["explanation"]
        assert new == old
        counts["new_evidence"] += 1
    assert len(restored.pop("evidence")) == 1
    counts["new_evidence"] += 1
    restored["notes"] = before["notes"]
    counts["recipe_context_notes_corrected"] += 1
    restored["references"] = deepcopy(before["references"])
    counts["bibliographic_entries_enriched"] += 1
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"])["claims"] == item["claims"]
    assert "preview only" not in event["changes"]
    counts["new_curation_history"] += 1
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
        target = safe_path(root, item["path"])
        assert target.is_file() and target.stat().st_nlink == 1, "Non-regular or hardlinked recipe"
        before, after = (runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
        assert not validate_recipe(before, target_class="SolutionRecipe"), "Invalid baseline"
        assert not validate_recipe(after, target_class="SolutionRecipe"), "Invalid proposal"
        old, new = (item[key].encode() for key in ("before_text", "after_text"))
        current = target.read_bytes()
        if current == new:
            continue
        assert not verify and current == old, "Concurrent edit or unapplied verify target"
        pending.append((target, old, new))
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
            assert target.read_bytes() == old, "Concurrent edit during write"
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
