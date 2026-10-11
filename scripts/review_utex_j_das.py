"""Guarded application of source-reviewed J and Dasycladales receiving media."""

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

FOLDER = Path("reports/ingredient_concentration_curation/20261010-utex-j-das")
SOURCE = Path(
    "reports/ingredient_concentration_curation/20261010-utex-j-das-preview/"
    "mutation-preview-v3/plan.json"
)
SOURCE_SHA = "6a367592593e5ecab4525f4f1f7434ef152d5c36792929db65684e3730d687db"
ACTION = "CURATED_UTEX_J_DAS_RECEIVING_MEDIA_EVIDENCE"
BASIS = "per liter of starting Pasteurized Seawater before supplement addition"


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
    assert len({r["path"] for r in records}) == len(records) == 2
    assert {r["id"] for r in records} == {"CultureMech:000172", "CultureMech:000161"}
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
    is_j = before["id"] == "CultureMech:000172"
    if is_j:
        variants = restored.pop("variants")
        assert len(variants) == 1 and variants[0]["relationship"] == "SUPPLEMENTED_VARIANT"
        assert variants[0]["modifications"] == [
            "Add 12.5 g agar per 1 L recipe (12.5 g/L; 1.25% w/v) before covering and autoclaving; do not mix at the agar-addition step."
        ]
        counts["inline_variant_options_added"] += 1
    else:
        macro = restored["solutions"][0]
        nested = macro.pop("solutions")
        assert "composition" not in macro and len(nested) == 2
        components = []
        for index, stock in enumerate(nested):
            old = before["solutions"][0]["composition"][index]
            assert set(stock) == {"preferred_term", "concentration", "composition"}
            assert stock["preferred_term"] == old["preferred_term"]
            assert stock["concentration"] == old["concentration"]
            assert len(stock["composition"]) == 1
            ingredient = stock["composition"][0]
            assert ingredient["concentration"] == {
                "value": "0.70" if index == 0 else "0.02",
                "unit": "MOLAR",
            }
            ingredient["concentration"] = deepcopy(old["concentration"])
            if index == 1:
                assert ingredient.pop("chemical_formula") == "Na2HPO4.7H2O"
                assert (
                    "term" not in ingredient and "mediaingredientmech_chebi_term" not in ingredient
                )
                for key in ("term", "mediaingredientmech_chebi_term"):
                    ingredient[key] = deepcopy(old[key])
                counts.update(
                    unsupported_primary_identities_removed=1,
                    unsupported_secondary_identities_removed=1,
                )
            components.append(ingredient)
        macro["composition"] = components
        counts.update(stock_nodes_relocated=2, stock_dose_basis_corrections=2, new_quantity_slots=2)

    original_nodes = _nodes(before)
    new_nodes = _nodes(restored)
    assert set(original_nodes) == set(new_nodes)
    for path, old in original_nodes.items():
        new = new_nodes[path]
        if new.get("concentration") != old.get("concentration"):
            if "concentration" not in new:
                counts["unsupported_quantity_slots_removed"] += 1
            else:
                assert not is_j
                assert path in {"ingredients[1]", "solutions[0]", "solutions[1]", "solutions[2]"}
                assert new["concentration"] == dict(old["concentration"], per_volume=BASIS)
                counts[
                    (
                        "stock_dose_basis_corrections"
                        if path.startswith("solutions[")
                        else "ingredient_dose_basis_corrections"
                    )
                ] += 1
            new["concentration"] = deepcopy(old["concentration"])
        if new.get("term") != old.get("term"):
            assert not is_j and path in {
                "solutions[2].composition[2]",
                "solutions[2].composition[5]",
            }
            expected = "CHEBI:49105" if path.endswith("[2]") else "CHEBI:31345"
            assert new["term"]["id"] == expected
            assert new["mediaingredientmech_chebi_term"] == new["term"]
            for key in ("term", "mediaingredientmech_chebi_term"):
                new[key] = deepcopy(old[key])
            counts.update(ingredient_identities_corrected=1, ingredient_mim_links_corrected=1)
        if new["preferred_term"] != old["preferred_term"]:
            new["preferred_term"] = old["preferred_term"]
            counts["ingredient_labels_corrected"] += 1
        if new.get("notes") != old.get("notes"):
            kind = "stock" if path.split(".")[-1].startswith("solutions[") else "ingredient"
            counts[kind + "_context_notes_corrected"] += 1
            new["notes"] = old["notes"]

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
    assert restored["notes"] != before["notes"]
    restored["notes"] = before["notes"]
    counts["recipe_context_notes_corrected"] += 1
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"])["claims"] == item["claims"]
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
        return {"changed": 0, "pending": len(pending), "already_applied": 2 - len(pending)}
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
    return {"changed": len(pending), "pending": 0, "already_applied": 2 - len(pending)}


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
