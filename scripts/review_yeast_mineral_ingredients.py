"""Apply only the exact, source-pinned yeast mineral preview after full preflight."""

import argparse
import collections
import json
import os
import stat
import subprocess
import tempfile
from pathlib import Path

import review_solution_concentration_evidence as runner
from review_utex_f2_concentrations import safe_path

from culturemech.validation.write_validated import validate_recipe

FOLDER = Path("reports/ingredient_concentration_curation/20261010-yeast-mineral-source-preview")
SOURCE = FOLDER / "claim-review-preview.json"
PLAN = FOLDER / "mutation-preview-v2/plan.json"
SOURCE_SHA = "f8fc139c6c37261eed3e543224ea652ac81bc4701374b3c872bd119970d2a1b9"
PLAN_SHA = "413ab653a133f8b37d2d89b1f2f39fff23baab998bbdf05f78ae0c80fab06560"
KEYS = ("397", "398", "399", "400")
ACTION = "CURATED_YEAST_MINERAL_SOURCED_INGREDIENTS"


def approved(root):
    if not __debug__:
        raise RuntimeError("Guarded curation requires assertions; do not use -O")
    root = Path(root).resolve()
    assert not (root / SOURCE).is_symlink() and not (root / PLAN).is_symlink()
    source_raw, plan_raw = (root / SOURCE).read_bytes(), (root / PLAN).read_bytes()
    assert runner.sha(source_raw) == SOURCE_SHA, "Source ledger drift"
    assert runner.sha(plan_raw) == PLAN_SHA, "Reviewed preview drift"
    source, plan = json.loads(source_raw), json.loads(plan_raw)
    assert plan["source_sha256"] == SOURCE_SHA
    assert tuple(item["key"] for item in plan["records"]) == KEYS
    records = {item["key"]: item for item in source["records"]}
    assert set(records) == set(KEYS) and len(source["records"]) == 4
    assert collections.Counter(c["status"] for r in records.values() for c in r["claims"]) == {
        "correct": 56,
        "unsupported": 26,
        "conflict": 2,
    }
    for item in plan["records"]:
        record = records[item["key"]]
        before, after = (runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
        assert item["path"] == record["path"]
        assert before == record["original_record"]
        assert runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["sha256"]
        assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
        assert before["id"] == after["id"] == item["id"] == record["id"]
        assert item["claims"] == record["claims"]
        assert after["curation_history"][:-1] == before["curation_history"]
        assert len(after["ingredients"]) == len(before["ingredients"]) + 1 == 22
        for claim in record["claims"]:
            index = claim["pointer"][1]
            old, new = before["ingredients"][index], after["ingredients"][index]
            assert old["preferred_term"] == claim["ingredient"]
            assert old["concentration"] == claim["old"]
            expected = claim["proposed"] if claim["status"] == "correct" else claim["old"]
            assert new["concentration"] == expected
            evidence = next(e for e in new["evidence"] if e["reference"] == "doi:" + claim["doi"])
            assert evidence["snippet"] == claim["snippet"]
            assert claim["basis_snippet"] in evidence["explanation"]
            assert evidence["supports"] == (
                "SUPPORT" if claim["status"] == "correct" else "PARTIAL"
            )
    return plan


def check(before, after, item, root=None):
    """Check an audit-registry entry against the pinned snapshot and recount changes."""
    plan = approved(Path.cwd() if root is None else root)
    reviewed = next(record for record in plan["records"] if record["key"] == item["key"])
    expected = dict(reviewed, action=ACTION)
    assert json.dumps(item, sort_keys=True) == json.dumps(
        expected, sort_keys=True
    ), "Unreviewed audit entry"
    assert before == runner.load_yaml(reviewed["before_text"])
    assert after == runner.load_yaml(reviewed["after_text"]), "Unreviewed record content"
    counts = collections.Counter()
    for old, new in zip(before["ingredients"], after["ingredients"][:21], strict=True):
        for field, counter in (
            ("concentration", "quantity_corrections"),
            ("preferred_term", "ingredient_labels_corrected"),
            ("notes", "ingredient_context_notes_corrected"),
            ("mediaingredientmech_chebi_term", "ingredient_mim_links_corrected"),
        ):
            if old.get(field) != new.get(field):
                counts[counter] += 1
        if old.get("term") != new.get("term"):
            counts[
                (
                    "ingredient_identities_corrected"
                    if "term" in new
                    else "unsupported_ingredient_identity_slots_removed"
                )
            ] += 1
    added = after["ingredients"][21]
    counts[
        "new_quantity_slots" if "concentration" in added else "unquantified_ingredient_nodes_added"
    ] += 1
    for old, new in zip(before["preparation_steps"], after["preparation_steps"][:3], strict=True):
        if old["description"] != new["description"]:
            counts["preparation_descriptions_corrected"] += 1
        if old["action"] != new["action"]:
            counts["preparation_actions_corrected"] += 1
    counts["preparation_steps_added"] = len(after["preparation_steps"]) - len(
        before["preparation_steps"]
    )
    if before.get("variant_children") != after.get("variant_children"):
        counts["child_link_notes_corrected"] += 1
    for field in ("parent_media", "variant_modifications"):
        if before.get(field) != after.get(field):
            counts["relationship_dose_descriptions_corrected"] += 1
    counts["new_evidence"] = sum(
        len(node.get("evidence", [])) for node in after["ingredients"] + [after]
    ) - sum(len(node.get("evidence", [])) for node in before["ingredients"] + [before])
    for field in ("references", "curation_history"):
        counts["new_" + field] = len(after.get(field, [])) - len(before.get(field, []))
    assert dict(counts) == reviewed["counts"], "Count mismatch"
    return counts


def preflight(plan, root, *, verify=False):
    root = Path(root).resolve()
    assert json.dumps(plan, sort_keys=True) == json.dumps(
        approved(root), sort_keys=True
    ), "Only the exact reviewed plan is permitted"
    tracked = set(
        subprocess.check_output(
            ["git", "ls-files", "-z", "data/normalized_yaml"],
            cwd=root,
            text=True,
        ).split("\0")
    )
    paths = [item["path"] for item in plan["records"]]
    assert len(paths) == len(set(paths)) == 4
    pending = []
    for item in plan["records"]:
        assert item["path"] in tracked, "Untracked or non-exact path"
        assert item["path"].startswith("data/normalized_yaml/") and item["path"].endswith(".yaml")
        target = safe_path(root, item["path"])
        assert target.is_file() and target.stat().st_nlink == 1, "Non-regular or hardlinked recipe"
        before, after = (runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
        assert not validate_recipe(before, target_class="MediaRecipe"), "Invalid baseline"
        assert not validate_recipe(after, target_class="MediaRecipe"), "Invalid proposal"
        old, new = item["before_text"].encode(), item["after_text"].encode()
        current = target.read_bytes()
        if current == new:
            continue
        assert not verify and current == old, "Concurrent record edit or unapplied verify target"
        pending.append((target, old, new))
    for target, old, _ in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == old, "Concurrent edit during preflight"
    return pending


def _stage(target, content):
    handle = tempfile.NamedTemporaryFile(
        dir=target.parent, prefix="." + target.name + ".", suffix=".tmp", delete=False
    )
    staged = Path(handle.name)
    try:
        with handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        staged.chmod(stat.S_IMODE(target.stat().st_mode))
        return staged
    except BaseException:
        staged.unlink(missing_ok=True)
        raise


def apply(plan, root, *, dry_run=True, verify=False):
    root = Path(root).resolve()
    pending = preflight(plan, root, verify=verify)
    result = {"changed": 0, "pending": len(pending), "already_applied": 4 - len(pending)}
    if dry_run or verify:
        return result
    staged, written = [], []
    try:
        for target, old, new in pending:
            safe_path(root, target.relative_to(root))
            staged.append((_stage(target, new), target, old, new))
        # Recheck the entire batch after staging, before the first recipe replacement.
        assert preflight(plan, root) == pending, "Batch changed during staging"
        for temporary, target, old, new in staged:
            safe_path(root, target.relative_to(root))
            assert target.read_bytes() == old, "Concurrent edit during write"
            os.replace(temporary, target)
            written.append((target, old, new))
            assert target.read_bytes() == new, "Readback mismatch"
        assert preflight(plan, root, verify=True) == []
    except BaseException as error:
        rollback_errors = []
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
                rollback_errors.append(f"{target.relative_to(root)}: {rollback_error}")
            finally:
                if backup is not None:
                    backup.unlink(missing_ok=True)
        if rollback_errors:
            raise RuntimeError(
                "Partial application; manual inspection required: " + "; ".join(rollback_errors)
            ) from error
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
    plan = approved(args.root)
    result = apply(plan, args.root, dry_run=not args.apply, verify=args.verify)
    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "verify" if args.verify else "preview",
                "source_sha256": SOURCE_SHA,
                "reviewed_plan_sha256": PLAN_SHA,
                **result,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
