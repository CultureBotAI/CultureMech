"""Guarded application of five source-reviewed UTEX organic-medium proposals."""

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

FOLDER = Path("reports/ingredient_concentration_curation/20261010-utex-organic-five")
SOURCE = Path(
    "reports/ingredient_concentration_curation/20261010-utex-organic-five-preview/"
    "mutation-preview-v3/plan.json"
)
SOURCE_SHA = "a6f04f14f656cc1b9c8f7d7d65e0f7a30d7b762c6acb09e629c5fc6a25a6dd80"
ACTION = "CURATED_UTEX_ORGANIC_MEDIUM_INPUT_BASES_AND_CONCENTRATION_EVIDENCE"


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
    records = json.loads(raw)["records"]
    assert len({r["path"] for r in records}) == len(records) == 5
    assert {r["id"] for r in records} == {
        "CultureMech:000175",
        "CultureMech:000168",
        "CultureMech:000186",
        "CultureMech:000184",
        "CultureMech:000234",
    }
    for item in records:
        assert item["action"] == ACTION
        for key in ("before", "after"):
            assert runner.sha(item[f"{key}_text"].encode()) == item[f"{key}_sha256"]
            assert runner.load_yaml(item[f"{key}_text"])["id"] == item["id"]
    return {"source_sha256": SOURCE_SHA, "records": records}


def _nodes(doc):
    result = {}

    def walk(node, path=""):
        if path:
            result[path] = node
        for key in ("ingredients", "composition", "solutions"):
            for index, child in enumerate(node.get(key, [])):
                walk(child, (path + "." if path else "") + f"{key}[{index}]")

    walk(doc)
    return result


def check(before, after, item, root=None):
    """Invert only the pinned dose, optional formulation, notes and evidence edits."""
    reviewed = next(
        r
        for r in approved(Path.cwd() if root is None else root)["records"]
        if r["path"] == item["path"]
    )
    assert serialized(item) == serialized(reviewed), "Unreviewed audit entry"
    assert serialized(before) == serialized(runner.load_yaml(reviewed["before_text"]))
    assert serialized(after) == serialized(runner.load_yaml(reviewed["after_text"]))
    restored = deepcopy(after)
    counts = Counter()

    def strip_evidence(node):
        if isinstance(node, dict):
            if "evidence" in node:
                entries = node.pop("evidence")
                assert len(entries) == len({entry["reference"] for entry in entries})
                for entry in entries:
                    assert entry["reference"].startswith("https://utex.org/products/")
                    assert (
                        entry["snippet"] and entry["explanation"] and entry["supports"] == "SUPPORT"
                    )
                counts["new_evidence"] += len(entries)
            for value in node.values():
                strip_evidence(value)
        elif isinstance(node, list):
            for child in node:
                strip_evidence(child)

    strip_evidence(restored)
    identity = before["id"]
    if "variants" in restored:
        variants = restored.pop("variants")
        assert identity != "CultureMech:000184"
        assert len(variants) == 1 and variants[0]["relationship"] == "SUPPLEMENTED_VARIANT"
        amount = "7.5" if identity == "CultureMech:000175" else "15"
        assert amount + " g agar" in variants[0]["modifications"][0]
        assert "do not mix" in variants[0]["modifications"][0]
        counts["inline_variant_options_added"] += 1
    else:
        assert identity == "CultureMech:000184"
    original_nodes, new_nodes = _nodes(before), _nodes(restored)
    assert set(original_nodes) == set(new_nodes)
    for path, old in original_nodes.items():
        new = new_nodes[path]
        if new.get("concentration") != old.get("concentration"):
            if "concentration" not in new:
                assert old["preferred_term"] == "dH2O" or (
                    identity == "CultureMech:000234"
                    and path == "solutions[0]"
                    and old["preferred_term"] == "Bristol Medium"
                )
                counts["unsupported_quantity_slots_removed"] += 1
            else:
                if identity == "CultureMech:000175":
                    assert path == "ingredients[0]"
                    basis = "per liter of starting dH2O before malt extract addition"
                else:
                    assert (
                        identity == "CultureMech:000184" and path == "solutions[0].composition[1]"
                    )
                    basis = "per liter of prepared stock before heating and filtration"
                assert new["concentration"] == dict(old["concentration"], per_volume=basis)
                counts["ingredient_dose_basis_corrections"] += 1
            new["concentration"] = deepcopy(old["concentration"])
        if new.get("notes") != old.get("notes"):
            kind = "stock" if path.split(".")[-1].startswith("solutions[") else "ingredient"
            counts[kind + "_context_notes_corrected"] += 1
            new["notes"] = old["notes"]
    assert len(restored["references"]) == len(before["references"])
    for old, new in zip(before["references"], restored["references"], strict=True):
        assert new["reference"] == old["reference"]
        if new != old:
            assert set(new) == set(old) | {"title", "notes"}
            assert "source_type=culture_collection_page" in new["notes"]
            assert "discovery_mode=existing_record_reference" in new["notes"]
            assert "accessed_on=2026-10-10" in new["notes"]
            counts["bibliographic_entries_enriched"] += 1
    restored["references"] = deepcopy(before["references"])
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    event_changes = json.loads(event["changes"])
    assert event_changes["claims"] == item["claims"] and event_changes["counts"] == item["counts"]
    counts["new_curation_history"] += 1
    assert serialized(restored) == serialized(before), "Out-of-scope change"
    assert dict(counts) == item["counts"], (counts, item["counts"])
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
        check(before, after, item, root)
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
        return {"changed": 0, "pending": len(pending), "already_applied": 5 - len(pending)}
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
    return {"changed": len(pending), "pending": 0, "already_applied": 5 - len(pending)}


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
