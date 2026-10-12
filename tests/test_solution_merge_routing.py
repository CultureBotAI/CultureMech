"""Standalone preparations are not media, even with legacy ingredient fields."""

import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

from culturemech.merge import merge_recipes as cli
from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger
from culturemech.validation.write_validated import infer_target_class

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def solution():
    # Synthetic recipe; only the record-class and preparation boundaries matter.
    return {
        "term": {"id": "mediadive.solution:190"},
        "preferred_term": "Standalone preparation",
        "ingredients": [{"preferred_term": "See source for composition"}],
        "composition": [{"preferred_term": "Basal ingredient"}],
        "solutions": [{"composition": [{"preferred_term": "Stock ingredient"}]}],
    }


def write_recipe(tmp_path, name, recipe):
    path = tmp_path / name
    path.write_text(yaml.safe_dump(recipe), encoding="utf-8")
    return path


@pytest.mark.parametrize("prefix", ["mediadive.solution:", "MediaIngredientMech:"])
@pytest.mark.parametrize("ingredients", [None, [], [{"preferred_term": "Glucose"}]])
def test_standalone_solution_never_gets_medium_fingerprint(solution, prefix, ingredients):
    solution["term"]["id"] = prefix + "190"
    solution["name"] = "A name does not change the root class"
    if ingredients is None:
        del solution["ingredients"]
    else:
        solution["ingredients"] = ingredients
    assert infer_target_class(solution) == "SolutionRecipe"
    before = copy.deepcopy(solution)
    with pytest.raises(ValueError, match="SolutionRecipe"):
        RecipeFingerprinter().fingerprint(solution)
    assert solution == before


def test_medium_with_nested_stock_keeps_full_fingerprint(solution):
    medium = {
        "term": {"id": "mediadive.medium:111"},
        "ingredients": [],
        "solutions": [solution],
    }
    flat = {"ingredients": solution["composition"] + solution["solutions"][0]["composition"]}
    assert infer_target_class(medium) == "MediaRecipe"
    assert RecipeFingerprinter().fingerprint(medium) == RecipeFingerprinter().fingerprint(flat)


def test_matcher_reports_solution_exclusion_separately(tmp_path, solution):
    stock = write_recipe(tmp_path, "stock.yaml", solution)
    medium = {"ingredients": [{"preferred_term": "Stock ingredient"}]}
    media = [write_recipe(tmp_path, f"medium{i}.yaml", medium) for i in range(2)]
    placeholder = write_recipe(
        tmp_path, "placeholder.yaml", {"ingredients": solution["ingredients"]}
    )
    matcher = RecipeMatcher()
    assert list(matcher.group_recipes([stock, *media, placeholder]).values()) == [media]
    assert matcher._last_skip_stats == {
        "total_processed": 4,
        "excluded_solutions": 1,
        "skipped_no_fingerprint": 1,
        "skipped_error": 0,
        "successfully_fingerprinted": 2,
        "reasons": {"no_valid_ingredients": 1},
    }


@pytest.mark.parametrize("supplied_fingerprint", [None, "precomputed"])
@pytest.mark.parametrize("include_medium", [False, True])
def test_direct_merger_cannot_bypass_root_class(
    tmp_path, solution, supplied_fingerprint, include_medium
):
    stock = write_recipe(tmp_path, "stock.yaml", solution)
    paths = [stock]
    if include_medium:
        medium = {"name": "Medium", "ingredients": [{"preferred_term": "Stock ingredient"}]}
        paths.insert(0, write_recipe(tmp_path, "medium.yaml", medium))
    before = {path: path.read_bytes() for path in paths}
    with pytest.raises(ValueError, match="SolutionRecipe"):
        RecipeMerger().merge_group(paths, fingerprint=supplied_fingerprint)
    assert {path: path.read_bytes() for path in paths} == before


def test_curated_solution_190_remains_unchanged_and_outside_medium_groups():
    plan = json.loads(
        (
            ROOT
            / "reports/ingredient_concentration_curation/20261007-dsmz111-preparation/plan.json"
        ).read_text()
    )
    item = next(item for item in plan["records"] if item["key"] == "solution")
    path = ROOT / item["path"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == item["after_sha256"]
    record = yaml.safe_load(path.read_text())
    assert infer_target_class(record) == "SolutionRecipe"
    assert len(record["composition"]) == 10
    assert record["solutions"][0]["composition"]
    with pytest.raises(ValueError, match="SolutionRecipe"):
        RecipeFingerprinter().fingerprint_file(path)
    matcher = RecipeMatcher()
    assert matcher.group_recipes([path]) == {}
    assert matcher._last_skip_stats["excluded_solutions"] == 1


def test_previous_retention_audit_reports_excluded_solution_without_crashing(monkeypatch):
    folder = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz111-preparation"
    spec = importlib.util.spec_from_file_location("dsmz111_retention", folder / "retention.py")
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    plan = json.loads((folder / "plan.json").read_text())
    monkeypatch.setattr(
        audit, "find_all_recipes", lambda _: [ROOT / r["path"] for r in plan["records"]]
    )
    result = audit.check()
    stock = next(row for row in result["records"] if "mediadive_190_" in row["path"])
    assert stock["status"] == "outside_medium_scope"
    assert stock["fingerprint"] is None
    assert not stock["all_checked_fields_retained"]
    assert not result["all_retained"]


@pytest.mark.parametrize("medium_kind", ["none", "valid", "invalid"])
def test_cli_routes_solutions_and_reports_partial_failure(
    tmp_path, solution, medium_kind, monkeypatch, capsys
):
    inputs = tmp_path / "normalized" / "bacterial"
    inputs.mkdir(parents=True)
    write_recipe(inputs, "solution.yaml", solution)
    if medium_kind != "none":
        medium = {"ingredients": [{"preferred_term": "Different ingredient"}]}
        if medium_kind == "valid":
            medium["name"] = "Synthetic medium"
        write_recipe(inputs, "medium.yaml", medium)
    outputs = tmp_path / "merged"
    stats_path = tmp_path / "stats.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "merge_recipes",
            "--normalized-dir",
            str(inputs.parent),
            "--output-dir",
            str(outputs),
            "--stats-file",
            str(stats_path),
        ],
    )
    assert cli.main() == (1 if medium_kind == "invalid" else 0)
    captured = capsys.readouterr()
    assert "Excluded 1 standalone SolutionRecipe inputs" in captured.out
    stats = json.loads(stats_path.read_text())
    assert stats["input_routing"]["excluded_solutions"] == 1
    assert stats["input_routing"]["skipped_error"] == 0
    assert stats["written_recipes"] == (1 if medium_kind == "valid" else 0)
    assert len(stats["merge_errors"]) == (1 if medium_kind == "invalid" else 0)
    outputs = list(outputs.glob("*.yaml"))
    assert len(outputs) == stats["written_recipes"]
    assert all(infer_target_class(yaml.safe_load(p.read_text())) == "MediaRecipe" for p in outputs)
