"""Guarded application of source-reviewed UTEX soil/seawater recipe inputs."""

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

FOLDER = Path("reports/ingredient_concentration_curation/20261010-utex-soil-seawater")
SOURCE = Path(
    "reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/"
    "mutation-preview-v2/plan.json"
)
SOURCE_SHA = "780bc103ce61d3aa302b1d37c56399144a90570e1fb2a4ada4b816e825e019ac"
ACTION = "CURATED_UTEX_SOIL_SEAWATER_INPUT_AMOUNTS_AND_OPTIONAL_CARBONATE"
BASIS = "per liter of the combined stated seawater and dH2O input volumes, before soil addition"


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
    assert len({r["path"] for r in records}) == len(records) == 7
    assert {r["id"] for r in records} == {
        "CultureMech:000221",
        "CultureMech:000005",
        "CultureMech:000007",
        "CultureMech:000009",
        "CultureMech:000011",
        "CultureMech:000016",
        "CultureMech:000019",
    }
    for item in records:
        assert item["action"] == ACTION
        for key in ("before", "after"):
            assert runner.sha(item[f"{key}_text"].encode()) == item[f"{key}_sha256"]
            assert runner.load_yaml(item[f"{key}_text"])["id"] == item["id"]
    return {"source_sha256": SOURCE_SHA, "records": records}


def _take_evidence(node, counts):
    entries = node.pop("evidence")
    assert len({e["reference"] for e in entries}) == len(entries)
    for item in entries:
        assert item["reference"].startswith("https://")
        assert item["snippet"] and item["explanation"] and item["supports"] == "SUPPORT"
    counts["new_evidence"] += len(entries)
    return entries


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
    """Invert the permitted amount, identity, context and evidence changes."""
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
                _take_evidence(node, counts)
            for value in node.values():
                strip_evidence(value)
        elif isinstance(node, list):
            for child in node:
                strip_evidence(child)

    strip_evidence(restored)
    identity = before["id"]
    removed = None
    if "variants" in restored:
        variants = restored.pop("variants")
        assert len(variants) == 1 and variants[0]["relationship"] == "SUPPLEMENTED_VARIANT"
        assert variants[0]["modifications"] == [
            "Optionally add 1 mg calcium carbonate (Fisher C 64) to the source 200 mL recipe before steaming."
        ]
        assert identity in {
            "CultureMech:000221",
            "CultureMech:000005",
            "CultureMech:000007",
            "CultureMech:000009",
            "CultureMech:000011",
        }
        index = 2 if identity == "CultureMech:000221" else 1
        removed = deepcopy(before["ingredients"][index])
        assert removed["preferred_term"] == "CaCO3"
        assert removed["concentration"] == {"value": "0.005", "unit": "G_PER_L"}
        restored["ingredients"].insert(index, removed)
        counts.update(supplement_nodes_moved_to_variants=1, inline_variant_options_added=1)

    original_nodes = _nodes(before)
    new_nodes = _nodes(restored)
    assert set(original_nodes) == set(new_nodes)
    for path, old in original_nodes.items():
        new = new_nodes[path]
        if new.get("concentration") != old.get("concentration"):
            if "concentration" not in new:
                allowed = (
                    old["preferred_term"] == "Green House Soil"
                    and old["concentration"]["unit"] == "VARIABLE"
                ) or old["preferred_term"] in {
                    "Pasteurized Seawater",
                    "Supplemented Seawater",
                    "Soil+Seawater Medium",
                }
                assert allowed
                counts["unsupported_quantity_slots_removed"] += 1
            else:
                basis = BASIS
                if identity == "CultureMech:000016":
                    assert path == "ingredients[0]"
                    basis = "per liter of Supplemented Seawater before soil addition"
                elif identity == "CultureMech:000019":
                    assert path == "ingredients[1]"
                    basis = (
                        "per liter of prepared Soil+Seawater Medium before salt and agar additions"
                    )
                else:
                    assert identity in {
                        "CultureMech:000005",
                        "CultureMech:000007",
                        "CultureMech:000009",
                        "CultureMech:000011",
                    }
                    assert path in {"ingredients[2]", "ingredients[3]"}
                assert new["concentration"] == dict(old["concentration"], per_volume=basis)
                counts["ingredient_dose_basis_corrections"] += 1
            new["concentration"] = deepcopy(old["concentration"])
        if new.get("notes") != old.get("notes"):
            kind = "stock" if path.split(".")[-1].startswith("solutions[") else "ingredient"
            suffix = "corrected" if "notes" in old else "added"
            counts[kind + "_context_notes_" + suffix] += 1
            if "notes" in old:
                new["notes"] = old["notes"]
            else:
                new.pop("notes")
    for old, new in zip(before["preparation_steps"], restored["preparation_steps"], strict=True):
        assert {k: v for k, v in old.items() if k != "description"} == {
            k: v for k, v in new.items() if k != "description"
        }
        if old["description"] != new["description"]:
            counts["preparation_descriptions_corrected"] += 1
            new["description"] = old["description"]
    if identity == "CultureMech:000007":
        assert restored["notes"] == restored["parent_media"]["notes"]
        assert restored["variant_modifications"] == [restored["notes"]]
        assert "67 mL" in restored["notes"] and "133 mL" in restored["notes"]
        restored["notes"] = before["notes"]
        restored["parent_media"]["notes"] = before["parent_media"]["notes"]
        restored["variant_modifications"] = deepcopy(before["variant_modifications"])
        counts.update(
            recipe_context_notes_corrected=1,
            parent_links_corrected=1,
            variant_quantity_texts_corrected=1,
        )
    if identity == "CultureMech:000221":
        child = restored["variant_children"][1]
        assert child["id"] == "CultureMech:000007"
        assert "67 mL" in child["notes"] and "133 mL" in child["notes"]
        child["notes"] = before["variant_children"][1]["notes"]
        counts["child_link_notes_corrected"] += 1

    for index, reference in enumerate(restored["references"]):
        if index < len(before["references"]):
            old = before["references"][index]
            assert reference["reference"] == old["reference"]
            if reference != old:
                assert set(reference) == set(old) | {"title", "notes"}
                counts["bibliographic_entries_enriched"] += 1
        else:
            assert set(reference) == {"reference", "title", "notes"}
            counts["new_references"] += 1
    restored["references"] = deepcopy(before["references"])
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    event_changes = json.loads(event["changes"])
    assert event_changes["claims"] == item["claims"]
    assert event_changes["removed_optional_ingredient"] == removed
    assert event_changes["counts"] == item["counts"]
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
        return {"changed": 0, "pending": len(pending), "already_applied": 7 - len(pending)}
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
    return {"changed": len(pending), "pending": 0, "already_applied": 7 - len(pending)}


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
