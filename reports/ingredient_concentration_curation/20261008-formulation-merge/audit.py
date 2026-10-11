"""Independently check full-corpus formulation grouping and claim retention.

No source or derived YAML is written. Every grouped input is compared against its
actual merge result, including every scoped evidence list. The comparator does
not use the production formulation projection as its expected answer.
"""

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter, StandaloneSolutionError
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def compare(source, actual, pointer="", *, root=False):
    failures = []
    if isinstance(source, dict):
        if not isinstance(actual, dict):
            return [pointer + ": mapping lost"]
        for key in actual.keys() - source.keys():
            if key == "evidence" or (
                root
                and key
                in {
                    "id",
                    "id_lineage_token",
                    "name",
                    "original_name",
                    "category",
                    "media_term",
                    "merged_from",
                    "merge_fingerprint",
                    "references",
                    "curation_history",
                    "sources",
                    "synonyms",
                    "categories",
                }
            ):
                continue
            failures.append(pointer + "/" + key + ": unexpected assertion")
        for key, value in source.items():
            if root and key in {
                "id",
                "id_lineage_token",
                "name",
                "original_name",
                "category",
                "media_term",
                "merged_from",
                "merge_fingerprint",
            }:
                continue
            location = pointer + "/" + key
            if key not in actual:
                failures.append(location + ": missing")
            elif key == "evidence" or (
                root
                and key
                in {
                    "references",
                    "curation_history",
                    "sources",
                    "synonyms",
                    "categories",
                }
            ):
                if not isinstance(actual[key], list) or any(
                    item not in actual[key] for item in value
                ):
                    failures.append(location + ": provenance lost")
            else:
                failures.extend(compare(value, actual[key], location))
    elif isinstance(source, list):
        if not isinstance(actual, list) or len(actual) != len(source):
            return [pointer + ": list shape changed"]
        for index, value in enumerate(source):
            failures.extend(compare(value, actual[index], f"{pointer}/{index}"))
    elif source != actual:
        failures.append(pointer + ": value changed")
    return failures


def run():
    code_paths = [
        "src/culturemech/merge/" + p + ".py"
        for p in (
            "fingerprint",
            "formulation",
            "matcher",
            "merger",
            "merge_recipes",
        )
    ]
    code_hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in code_paths}
    paths = [
        ROOT / p
        for p in subprocess.check_output(
            ["git", "ls-files", "-z", "data/normalized_yaml/**/*.yaml"], cwd=ROOT
        )
        .decode("utf-8")
        .split("\0")
        if p
    ]
    assert set(paths) == set(
        find_all_recipes(ROOT / "data/normalized_yaml")
    ), "Tracked/CLI inventory differs"
    hashes, documents, eligible, excluded = {}, {}, set(), Counter()
    candidate = RecipeFingerprinter()
    for path in paths:
        raw = path.read_bytes()
        relative = str(path.relative_to(ROOT))
        hashes[relative] = hashlib.sha256(raw).hexdigest()
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        documents[path] = doc
        try:
            fp = candidate.fingerprint(doc)
            if fp is None:
                excluded["no_valid_ingredients"] += 1
            else:
                eligible.add(path)
        except StandaloneSolutionError:
            excluded["standalone_solutions"] += 1
        except ValueError as error:
            excluded[str(error)] += 1
    matcher = RecipeMatcher()
    groups = matcher.group_formulations(paths)
    represented = [path for members in groups.values() for path in members]
    assert len(represented) == len(set(represented)), "Input assigned to multiple groups"
    assert set(represented) == eligible, "Grouping lost previously eligible input(s)"
    failures, multi_groups, retained, schema_valid = [], [], 0, 0
    merger = RecipeMerger()
    target_results = []
    target_plan = json.loads((HERE.parent / "20261008-togo-methanogens/plan.json").read_text())
    targets = {ROOT / row["path"] for row in target_plan["records"]}
    for number, (fp, members) in enumerate(groups.items(), 1):
        merged = merger.merge_group(members)
        errors = validate_recipe(merged, target_class="MediaRecipe")
        if errors:
            failures.append({"group": fp, "schema_errors": [str(e.message) for e in errors]})
        else:
            schema_valid += 1
        assert merged["merged_from"] == [path.stem for path in members]
        for path in members:
            doc = documents[path]
            errors = compare(doc, merged, root=True)
            if errors:
                failures.append({"path": str(path.relative_to(ROOT)), "errors": errors})
            else:
                retained += 1
            if path in targets:
                target_results.append(
                    {
                        "path": str(path.relative_to(ROOT)),
                        "group_paths": [str(p.relative_to(ROOT)) for p in members],
                        "errors": errors,
                        "ingredients": len(doc.get("ingredients", [])),
                        "stocks": len(doc.get("solutions", [])),
                    }
                )
        if len(members) > 1:
            multi_groups.append({"key": fp, "paths": [str(p.relative_to(ROOT)) for p in members]})
        if number % 1000 == 0:
            print(f"Verified {number}/{len(groups)} groups", flush=True)
    assert len(target_results) == len(targets)
    for relative, sha in hashes.items():
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == sha, relative
    assert code_hashes == {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in code_paths
    }
    return {
        "terminal": True,
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "input_records": len(paths),
        "eligible_records": len(eligible),
        "excluded": dict(excluded),
        "output_groups": len(groups),
        "input_records_retained": retained,
        "schema_valid_outputs": schema_valid,
        "multi_record_groups": multi_groups,
        "target_retention": target_results,
        "routing": matcher._last_skip_stats,
        "failures": failures,
        "input_sha256": hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest(),
        "code_sha256": code_hashes,
        "source_yaml_unchanged": True,
        "derived_yaml_written": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    result = run()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                k: v
                for k, v in result.items()
                if k
                not in {
                    "multi_record_groups",
                    "target_retention",
                    "code_sha256",
                }
            }
        )
    )
    raise SystemExit(bool(result["failures"]))
