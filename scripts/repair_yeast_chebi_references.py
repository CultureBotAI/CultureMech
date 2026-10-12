"""Repair only the source-reviewed ChEBI reference paths in four yeast records."""

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

FOLDER = Path("reports/ingredient_concentration_curation/20261010-yeast-chebi-urls")
SOURCE = FOLDER / "source-review.json"
SOURCE_SHA = "490eaa0ddf3d76f2a8f1fa48e582a25c089ae5978c89c83f4b9915b1a48b600e"
ACTION = "CORRECTED_CHEBI_REFERENCE_URL_ENCODING"
TIMESTAMP = "2026-10-10T06:24:13+00:00"


def serialized(value):
    return json.dumps(value, sort_keys=True)


def at(document, pointer):
    for key in pointer:
        document = document[key]
    return document


def source(root):
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
    assert runner.sha(raw) == SOURCE_SHA, "Source ledger drift"
    return json.loads(raw)


def approved(root):
    ledger = source(root)
    records = []
    for record in ledger["records"]:
        before = runner.load_yaml(record["before_text"])
        assert runner.sha(record["before_text"].encode()) == record["before_sha256"]
        assert before["id"] == record["id"]
        after = deepcopy(before)
        changes = []
        counts = Counter()
        assert len({tuple(op["pointer"]) for op in record["operations"]}) == 20
        for operation in record["operations"]:
            pointer, old, new = (operation[key] for key in ("pointer", "old", "new"))
            evidence = ledger["sources"][old]
            assert new == old.replace("%3A", ":") == evidence["reference"]
            assert operation["snippet"] == evidence["snippet"]
            assert pointer[-1] == "reference" and "curation_history" not in pointer
            parent = at(after, pointer[:-1])
            assert parent["reference"] == old
            if pointer[0] == "ingredients":
                assert pointer[2] == "evidence" and len(pointer) == 5
                assert parent["snippet"] == operation["snippet"]
            else:
                assert pointer[0] == "references" and len(pointer) == 3
                assert parent["title"] == evidence["title"]
            parent["reference"] = new
            changes.append(operation)
            counts[operation["kind"]] += 1
        assert counts == {
            "evidence_reference_urls_corrected": 10,
            "bibliography_reference_urls_corrected": 10,
        }
        record_curation_event(
            after,
            curator="codex",
            action=ACTION,
            timestamp=TIMESTAMP,
            source="; ".join(sorted(item["reference"] for item in ledger["sources"].values())),
            notes=(
                "Encoded-colon paths returned HTTP 404; canonical colon paths returned HTTP 200. "
                "Official page titles and molecular-formula snippets match the cited identities. "
                "Only live reference URLs change; prior history, amounts, identities, snippets and "
                "claim wording are unchanged. ChEBI is identity evidence, not an amount source."
            ),
            changes=serialized(changes),
        )
        counts["new_curation_history"] = 1
        rendered = runner.render(record["before_text"], after)
        records.append(
            dict(
                record,
                action=ACTION,
                after_text=rendered.decode(),
                after_sha256=runner.sha(rendered),
                counts=dict(counts),
                claims=[],
            )
        )
    assert len({r["path"] for r in records}) == len(records) == 4
    return {"source_sha256": SOURCE_SHA, "records": records}


def check(before, after, item, root=None):
    """Reject every change except the reviewed references and appended event."""
    reviewed = next(
        r
        for r in approved(Path.cwd() if root is None else root)["records"]
        if r["path"] == item["path"]
    )
    assert serialized(item) == serialized(reviewed), "Unreviewed audit entry"
    assert serialized(before) == serialized(runner.load_yaml(reviewed["before_text"]))
    expected = runner.load_yaml(reviewed["after_text"])
    assert serialized(after) == serialized(expected), "Unreviewed record content"
    restored = deepcopy(after)
    assert restored["curation_history"].pop() == expected["curation_history"][-1]
    counts = Counter(new_curation_history=1)
    for operation in reviewed["operations"]:
        parent = at(restored, operation["pointer"][:-1])
        assert parent["reference"] == operation["new"]
        parent["reference"] = operation["old"]
        counts[operation["kind"]] += 1
    assert serialized(restored) == serialized(before), "Non-URL change"
    assert dict(counts) == reviewed["counts"]
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
        assert not validate_recipe(before, target_class="MediaRecipe"), "Invalid baseline"
        assert not validate_recipe(after, target_class="MediaRecipe"), "Invalid proposal"
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
        return {"changed": 0, "pending": len(pending), "already_applied": 4 - len(pending)}
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
    return {"changed": len(pending), "pending": 0, "already_applied": 4 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    mode.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = apply(approved(args.root), args.root, dry_run=not args.apply, verify=args.verify)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
