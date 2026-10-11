"""Guarded application of seven source-reviewed UTEX stock proposals."""

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

FOLDER = Path("reports/ingredient_concentration_curation/20261010-utex-seven-stocks")
SOURCE = Path(
    "reports/ingredient_concentration_curation/20261010-utex-seven-stock-preview/"
    "mutation-preview-v2/plan.json"
)
SOURCE_SHA = "9a74e5496124432d48df9f83e4d62b2a6646bae12a6082ebfa534740bcea2f94"
ACTION = "CURATED_UTEX_SEVEN_STOCK_AMOUNTS_FORMS_AND_BOUNDARIES"
IDENTITIES = {
    "DAS_Vitamin_Cocktail": {1: "CHEBI:49105", 4: "CHEBI:31345", 5: "CHEBI:30753"},
    "EDTA_Stock": {0: "CHEBI:4735"},
    "Minor_Nutrients": {6: "CHEBI:86149", 7: "CHEBI:87009", 8: "CHEBI:86465"},
}


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


def check(before, after, item, root=None):
    """Independently invert the allowed changes and account for their exact scope."""
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
    stem = Path(item["path"]).stem
    roots = _take_evidence(restored, counts)
    assert len(roots) == 1 and roots[0]["reference"] == item["reference"]
    if stem == "DAS_Macro_Solution":
        assert restored["composition"] == [] and len(restored["solutions"]) == 2
        for index, stock in enumerate(restored.pop("solutions")):
            old = before["composition"][index]
            assert stock["concentration"] == old["concentration"]
            assert stock["preferred_term"] == old["preferred_term"]
            assert stock["mediaingredientmech_term"] == old["mediaingredientmech_term"]
            assert "term" not in stock and len(stock["composition"]) == 1
            ingredient = stock["composition"][0]
            assert ingredient["concentration"] == {
                "value": "0.70" if index == 0 else "0.02",
                "unit": "MOLAR",
            }
            if index == 0:
                assert ingredient["term"] == old["term"]
            else:
                assert "term" not in ingredient
                assert ingredient["chemical_formula"] == "Na2HPO4.7H2O"
            _take_evidence(ingredient, counts)
        restored["composition"] = deepcopy(before["composition"])
        counts.update(
            stock_nodes_relocated=2,
            stock_dose_basis_corrections=2,
            new_quantity_slots=2,
            unsupported_primary_identities_removed=1,
        )
    else:
        for index, (old, new) in enumerate(
            zip(before["composition"], restored["composition"], strict=True)
        ):
            entries = _take_evidence(new, counts)
            assert entries[0]["reference"] == item["reference"]
            assert f"composition[{index}].concentration" in entries[0]["explanation"]
            assert new["concentration"] == old["concentration"]
            if index in IDENTITIES.get(stem, {}):
                assert new["term"]["id"] == IDENTITIES[stem][index]
                assert new["mediaingredientmech_chebi_term"] == new["term"]
                assert "mediaingredientmech_term" not in new
                counts.update(ingredient_identities_corrected=1, ingredient_mim_links_corrected=1)
                if new["preferred_term"] != old["preferred_term"]:
                    counts["ingredient_labels_corrected"] += 1
                for key in (
                    "preferred_term",
                    "term",
                    "mediaingredientmech_term",
                    "mediaingredientmech_chebi_term",
                ):
                    new.pop(key, None)
                    if key in old:
                        new[key] = deepcopy(old[key])
            if (stem, index) in {("DAS_Vitamin_Cocktail", 3), ("Minor_Nutrients", 6)}:
                new.pop("notes")
                if "notes" in old:
                    new["notes"] = old["notes"]
                    counts["ingredient_context_notes_corrected"] += 1
                else:
                    counts["ingredient_context_notes_added"] += 1
            assert new == old, "Unreviewed ingredient change"
    assert restored["references"][1 : len(before["references"])] == before["references"][1:]
    counts["new_references"] = len(restored["references"]) - len(before["references"])
    if not counts["new_references"]:
        del counts["new_references"]
    restored["references"] = deepcopy(before["references"])
    restored["notes"] = before["notes"]
    counts.update(bibliographic_entries_enriched=1, recipe_context_notes_corrected=1)
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert "/tmp/" not in event["changes"] and "read-only source triage" not in event["changes"]
    assert json.loads(event["changes"])["claims"] == item["claims"]
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
