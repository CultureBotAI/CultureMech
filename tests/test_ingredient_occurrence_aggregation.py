"""Contract tests for lossless ingredient occurrence aggregation (#337).

The mapped and unmapped summaries are projections of one occurrence table.  The
table is the load-bearing artifact: it retains the stable recipe id and component
coordinate for every direct ingredient, while MIM decides whether the row belongs
to the mapped or unmapped projection.

These tests deliberately use tiny temporary corpora.  They exercise both recipe
shapes without paying for another parse of the normalized production corpus (the
shared corpus fixture already makes that parse once for the corpus test tier).
"""

from __future__ import annotations

import csv
import importlib.util
import sys
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_script(name: str):
    path = REPO_ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def occurrence_module():
    return _load_script("ingredient_occurrences")


@pytest.fixture(scope="module")
def cli_module():
    return _load_script("aggregate_ingredients")


@pytest.fixture(scope="module")
def stats_module():
    return _load_script("unmapped_ingredients_stats")


def _write(root: Path, relative: str, document: dict[str, Any] | str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    text = document if isinstance(document, str) else yaml.safe_dump(document, sort_keys=False)
    path.write_text(text, encoding="utf-8")
    return path


def _mapping(value: Any) -> dict[str, Any]:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, dict):
        return value
    return vars(value)


def _rows(result: Any) -> list[dict[str, Any]]:
    return [_mapping(row) for row in result.occurrences]


def _coordinate(row: dict[str, Any]) -> tuple[str, str, int]:
    return row["recipe_id"], row["component_field"], int(row["component_index"])


def _ingredient_label(row: dict[str, Any]) -> str:
    return row["preferred_term"]


def _resolved_identifier(row: dict[str, Any]) -> str:
    return row["resolved_identifier"]


def _mapped_entry(output: dict[str, Any], label: str) -> dict[str, Any]:
    return next(row for row in output["mapped_ingredients"] if row["preferred_term"] == label)


def _unmapped_entry(output: dict[str, Any], label: str) -> dict[str, Any]:
    return next(
        row
        for row in output["unmapped_ingredients"]
        if row.get("preferred_term", row.get("parsed_chemical_name", row.get("placeholder_id")))
        == label
    )


def _output_args(root: Path, stem: str) -> dict[str, Path]:
    out = root / stem
    out.mkdir(parents=True, exist_ok=True)
    return {
        "occurrences_output": out / "ingredient_occurrences.tsv",
        "mapped_output": out / "mapped_ingredients.yaml",
        "unmapped_output": out / "unmapped_ingredients.yaml",
        "errors_output": out / "ingredient_occurrence_errors.tsv",
        "list_output": out / "ingredients_list.tsv",
    }


def test_structural_shape_selects_one_direct_component_field(occurrence_module, tmp_path):
    """Shape, not the semantic ``record_kind``, selects the authoritative field.

    The curated solution is intentionally MediaRecipe-shaped.  Routing it via
    ``is_solution_record`` would select its absent composition and drop the real
    ingredient.  Conversely, a true SolutionRecipe must ignore its legacy
    ``ingredients`` placeholder.  Nested in-recipe solution composition is not a
    direct root containment and therefore is never expanded here.
    """

    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/media.yaml",
        {
            "id": "CultureMech:000001",
            "name": "legacy_medium_name",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}],
            "solutions": [
                {
                    "preferred_term": "Nested stock",
                    "composition": [{"preferred_term": "NESTED MUST NOT EXPAND"}],
                }
            ],
        },
    )
    _write(
        corpus,
        "bacterial/solution_with_placeholder.yaml",
        {
            "id": "CultureMech:000002",
            "preferred_term": "Canonical stock label",
            "term": {"id": "mediadive.solution:2"},
            "composition": [{"preferred_term": "Biotin"}],
            "ingredients": [{"preferred_term": "See source for composition"}],
        },
    )
    _write(
        corpus,
        "bacterial/solution_without_ingredients.yaml",
        {
            "id": "CultureMech:000003",
            "preferred_term": "Stock without stub",
            "term": {"id": "mediadive.solution:3"},
            "composition": [{"preferred_term": "Nicotinic acid"}],
        },
    )
    _write(
        corpus,
        "bacterial/curated_solution_media_shape.yaml",
        {
            "id": "CultureMech:000004",
            "record_kind": "SOLUTION",
            "name": "Curated solution retaining media shape",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "PABA"}],
        },
    )

    result = occurrence_module.scan_ingredient_occurrences(corpus)
    rows = _rows(result)

    assert [(row["recipe_id"], row["component_field"], _ingredient_label(row)) for row in rows] == [
        ("CultureMech:000001", "ingredients", "EDTA"),
        ("CultureMech:000002", "composition", "Biotin"),
        ("CultureMech:000003", "composition", "Nicotinic acid"),
        ("CultureMech:000004", "ingredients", "PABA"),
    ]
    assert {row["recipe_label"] for row in rows if row["recipe_id"] == "CultureMech:000001"} == {
        "legacy_medium_name"
    }
    assert {row["label_source"] for row in rows if row["recipe_id"] == "CultureMech:000001"} == {
        "legacy_name"
    }
    assert {row["recipe_label"] for row in rows if row["recipe_id"] == "CultureMech:000002"} == {
        "Canonical stock label"
    }
    assert {row["label_source"] for row in rows if row["recipe_id"] == "CultureMech:000002"} == {
        "preferred_term"
    }
    assert not result.errors

    paba = next(
        entry
        for entry in occurrence_module.build_mapped_output(result.occurrences)["mapped_ingredients"]
        if entry["resolved_identifier"] == "CHEBI:30753"
    )
    assert paba["preferred_term"] == "p-Aminobenzoic acid"
    assert paba["mapping_quality"] == "SYNONYM_MATCH"


def test_recipe_preferred_term_precedes_legacy_media_name(occurrence_module):
    assert occurrence_module._recipe_label(
        {"preferred_term": "Canonical recipe label", "name": "Legacy recipe name"},
        "MediaRecipe",
    ) == ("Canonical recipe label", "preferred_term")


def test_repeated_positions_and_duplicate_names_keep_stable_coordinates(
    occurrence_module, tmp_path
):
    corpus = tmp_path / "corpus"
    for suffix, recipe_id in (("a", "CultureMech:000011"), ("b", "CultureMech:000012")):
        ingredients = [{"preferred_term": "EDTA"}]
        if suffix == "a":
            ingredients.append({"preferred_term": "EDTA"})
        _write(
            corpus,
            f"bacterial/{suffix}.yaml",
            {
                "id": recipe_id,
                "name": "Duplicate display name",
                "physical_state": "LIQUID",
                "ingredients": ingredients,
            },
        )

    rows = _rows(occurrence_module.scan_ingredient_occurrences(corpus))
    assert [_coordinate(row) for row in rows] == [
        ("CultureMech:000011", "ingredients", 0),
        ("CultureMech:000011", "ingredients", 1),
        ("CultureMech:000012", "ingredients", 0),
    ]
    assert len({_coordinate(row) for row in rows}) == len(rows)
    assert {row["recipe_id"] for row in rows} == {
        "CultureMech:000011",
        "CultureMech:000012",
    }
    assert all(not Path(row["source_path"]).is_absolute() for row in rows)


def test_more_than_fifty_occurrences_remain_lossless_and_counts_use_full_rows(
    occurrence_module, tmp_path
):
    corpus = tmp_path / "corpus"
    for index in range(51):
        ingredients = [{"preferred_term": "EDTA"}]
        if index == 0:
            ingredients.append({"preferred_term": "EDTA"})
        _write(
            corpus,
            f"bacterial/{50 - index:03d}.yaml",  # reverse filenames versus ids
            {
                "id": f"CultureMech:{index + 1000:06d}",
                "name": f"Recipe {index:02d}",
                "physical_state": "LIQUID",
                "ingredients": ingredients,
            },
        )

    result = occurrence_module.scan_ingredient_occurrences(corpus)
    rows = _rows(result)
    edta = [row for row in rows if _ingredient_label(row) == "EDTA"]
    assert len(edta) == 52
    assert len({_coordinate(row) for row in edta}) == 52

    mapped = occurrence_module.build_mapped_output(result.occurrences)
    entry = _mapped_entry(mapped, "EDTA")
    assert entry["occurrence_count"] == 52
    assert entry["distinct_recipe_count"] == 51
    assert len(entry["recipe_occurrences"]) == 52

    out = tmp_path / "occurrences.tsv"
    occurrence_module.write_occurrences_tsv(out, result.occurrences)
    with out.open(encoding="utf-8", newline="") as stream:
        written = list(csv.DictReader(stream, delimiter="\t"))
    assert len(written) == 52


def test_real_mim_decisions_partition_rows_and_preserve_source_ids(occurrence_module, tmp_path):
    """The projection follows #260, not the presence of a colon in ``term.id``."""

    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/resolver_canary.yaml",
        {
            "id": "CultureMech:000021",
            "name": "Resolver canary",
            "physical_state": "LIQUID",
            "ingredients": [
                {"preferred_term": "EDTA", "term": {"id": "CHEBI:64755"}},
                {"preferred_term": "Beef heart", "term": {"id": "UBERON:0000948"}},
                {"preferred_term": "Calf brains", "term": {"id": "UBERON:0000955"}},
                {
                    "preferred_term": "CultureMech test-only local reagent 337",
                    "term": {"id": "mediadive.compound:337001"},
                    "chebi_term": {"id": "CHEBI:12345"},
                },
                {
                    "preferred_term": "CultureMech test-only source reagent 337",
                    "term": {"id": "mediadive.compound:337002"},
                },
            ],
        },
    )

    result = occurrence_module.scan_ingredient_occurrences(corpus)
    rows = {_ingredient_label(row): row for row in _rows(result)}
    assert _resolved_identifier(rows["EDTA"]) == "CHEBI:4735"
    assert _resolved_identifier(rows["Beef heart"]).startswith("FOODON:")
    assert _resolved_identifier(rows["Calf brains"]) == ""
    assert _resolved_identifier(rows["CultureMech test-only local reagent 337"]) == "CHEBI:12345"
    assert rows["CultureMech test-only local reagent 337"]["source_compound_id"] == (
        "mediadive.compound:337001"
    )
    assert _resolved_identifier(rows["CultureMech test-only source reagent 337"]) == ""
    assert rows["CultureMech test-only source reagent 337"]["source_compound_id"] == (
        "mediadive.compound:337002"
    )

    mapped = occurrence_module.build_mapped_output(result.occurrences)
    unmapped = occurrence_module.build_unmapped_output(result.occurrences)
    mapped_count = sum(row["occurrence_count"] for row in mapped["mapped_ingredients"])
    unmapped_count = sum(row["occurrence_count"] for row in unmapped["unmapped_ingredients"])
    assert mapped_count == 3
    assert unmapped_count == 2
    assert mapped_count + unmapped_count == len(result.occurrences)
    assert _unmapped_entry(unmapped, "Calf brains")["occurrence_count"] == 1


def test_complete_runs_are_byte_identical(cli_module, tmp_path):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/z.yaml",
        {
            "id": "CultureMech:000032",
            "name": "Same count Z",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "Biotin"}],
        },
    )
    _write(
        corpus,
        "bacterial/a.yaml",
        {
            "id": "CultureMech:000031",
            "name": "Same count A",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}],
        },
    )

    first = _output_args(tmp_path, "first")
    second = _output_args(tmp_path, "second")

    def run(outputs: dict[str, Path]) -> int:
        return cli_module.main(
            [
                "--input-dir",
                str(corpus),
                "--occurrences-output",
                str(outputs["occurrences_output"]),
                "--mapped-output",
                str(outputs["mapped_output"]),
                "--unmapped-output",
                str(outputs["unmapped_output"]),
                "--errors-output",
                str(outputs["errors_output"]),
                "--list-output",
                str(outputs["list_output"]),
            ]
        )

    assert run(first) == 0
    assert run(second) == 0
    for name in first:
        assert first[name].read_bytes() == second[name].read_bytes(), name
        assert first[name].stat().st_mode & 0o777 == 0o644
    assert b"\r\n" not in first["occurrences_output"].read_bytes()


def test_fatal_errors_are_reported_without_replacing_success_artifacts(cli_module, tmp_path):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/good.yaml",
        {
            "id": "CultureMech:000041",
            "name": "Good record",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}],
        },
    )
    _write(corpus, "bacterial/bad.yaml", "id: [unclosed\n")
    invalid_utf8 = corpus / "bacterial" / "invalid_utf8.yaml"
    invalid_utf8.write_bytes(b"\xff\xfe\x00")
    _write(
        corpus,
        "bacterial/missing_id.yaml",
        {
            "name": "Schema-invalid record",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "Biotin"}],
        },
    )

    outputs = _output_args(tmp_path, "out")
    sentinels = {
        name: f"existing {name}\n".encode()
        for name in ("occurrences_output", "mapped_output", "unmapped_output", "list_output")
    }
    for name, content in sentinels.items():
        outputs[name].write_bytes(content)

    rc = cli_module.main(
        [
            "--input-dir",
            str(corpus),
            "--occurrences-output",
            str(outputs["occurrences_output"]),
            "--mapped-output",
            str(outputs["mapped_output"]),
            "--unmapped-output",
            str(outputs["unmapped_output"]),
            "--errors-output",
            str(outputs["errors_output"]),
            "--list-output",
            str(outputs["list_output"]),
        ]
    )
    assert rc != 0
    for name, content in sentinels.items():
        assert outputs[name].read_bytes() == content, f"fatal run replaced {name}"

    with outputs["errors_output"].open(encoding="utf-8", newline="") as stream:
        errors = list(csv.DictReader(stream, delimiter="\t"))
    assert errors
    parse_error = next(row for row in errors if row["category"] == "yaml_parse_error")
    assert parse_error["file"].endswith("bacterial/bad.yaml")
    assert parse_error["message"]
    decode_error = next(row for row in errors if row["category"] == "input_decode_error")
    assert decode_error["file"].endswith("bacterial/invalid_utf8.yaml")
    schema_error = next(row for row in errors if row["category"] == "missing_required")
    assert schema_error["file"].endswith("bacterial/missing_id.yaml")


def test_blank_labels_are_preserved_as_separate_occurrences(occurrence_module, tmp_path):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/blanks.yaml",
        {
            "id": "CultureMech:000051",
            "name": "Blank label canary",
            "physical_state": "LIQUID",
            "ingredients": [
                {"preferred_term": "", "notes": "first blank"},
                {"preferred_term": "", "notes": "second blank"},
            ],
        },
    )

    result = occurrence_module.scan_ingredient_occurrences(corpus)
    blank_rows = [row for row in _rows(result) if _ingredient_label(row) == ""]
    assert len(blank_rows) == 2
    assert {_coordinate(row) for row in blank_rows} == {
        ("CultureMech:000051", "ingredients", 0),
        ("CultureMech:000051", "ingredients", 1),
    }
    assert all(_resolved_identifier(row) == "" for row in blank_rows)

    unmapped = occurrence_module.build_unmapped_output(result.occurrences)
    blank_entries = [row for row in unmapped["unmapped_ingredients"] if row["preferred_term"] == ""]
    assert len(blank_entries) == 2
    assert [row["occurrence_count"] for row in blank_entries] == [1, 1]
    assert {
        (
            row["recipe_occurrences"][0]["recipe_id"],
            row["recipe_occurrences"][0]["component_field"],
            row["recipe_occurrences"][0]["component_index"],
        )
        for row in blank_entries
    } == {
        ("CultureMech:000051", "ingredients", 0),
        ("CultureMech:000051", "ingredients", 1),
    }


def test_unmapped_stats_consumes_recipe_level_summary(stats_module, tmp_path, capsys):
    report = {
        "total_unmapped_count": 1,
        "total_instances": 2,
        "recipe_count": 2,
        "unmapped_ingredients": [
            {
                "preferred_term": "Unknown reagent",
                "placeholder_id": "Unknown reagent",
                "raw_ingredient_text": [],
                "parsed_chemical_name": "Unknown reagent",
                "occurrence_count": 2,
            }
        ],
        "summary_by_category": [
            {
                "category": "BACTERIAL",
                "recipes_with_unmapped": 2,
                "total_unmapped_instances": 2,
                "unique_unmapped_count": 1,
            }
        ],
    }
    report_path = tmp_path / "unmapped_ingredients.yaml"
    report_path.write_text(yaml.safe_dump(report, sort_keys=False), encoding="utf-8")

    assert stats_module.main(["--input", str(report_path), "--top", "1"]) == 0
    output = capsys.readouterr().out
    assert "Total direct occurrences: 2" in output
    assert "Recipes with unresolved ingredients: 2" in output
    assert "2 occurrences across 2 recipes" in output


def test_empty_input_is_a_machine_readable_failure(occurrence_module, tmp_path):
    result = occurrence_module.scan_ingredient_occurrences(tmp_path)
    assert not result.occurrences
    assert [error.category for error in result.errors] == ["no_input_files"]


def test_multi_output_replace_failure_rolls_back_and_preserves_modes(
    occurrence_module, tmp_path, monkeypatch
):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000061",
            "name": "Rollback canary",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}],
        },
    )
    result = occurrence_module.scan_ingredient_occurrences(corpus)
    mapped = occurrence_module.build_mapped_output(result.occurrences)
    occurrences_path = tmp_path / "ingredient_occurrences.tsv"
    mapped_path = tmp_path / "mapped_ingredients.yaml"
    occurrences_path.write_text("old occurrences\n", encoding="utf-8")
    mapped_path.write_text("old mapped\n", encoding="utf-8")
    occurrences_path.chmod(0o640)
    mapped_path.chmod(0o640)

    real_replace = occurrence_module.os.replace
    replace_count = 0

    def fail_second_replace(source, destination):
        nonlocal replace_count
        replace_count += 1
        if replace_count == 2:
            raise OSError("synthetic second replacement failure")
        return real_replace(source, destination)

    monkeypatch.setattr(occurrence_module.os, "replace", fail_second_replace)
    with pytest.raises(OSError, match="synthetic second replacement failure"):
        occurrence_module.write_occurrences_and_yaml(
            occurrences_path,
            result.occurrences,
            mapped_path,
            mapped,
        )

    assert occurrences_path.read_text(encoding="utf-8") == "old occurrences\n"
    assert mapped_path.read_text(encoding="utf-8") == "old mapped\n"
    assert occurrences_path.stat().st_mode & 0o777 == 0o640
    assert mapped_path.stat().st_mode & 0o777 == 0o640


def test_imported_category_outputs_validate_against_closed_summary_schemas(
    occurrence_module, tmp_path
):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "imported/one.yaml",
        {
            "id": "CultureMech:000071",
            "name": "Imported category canary",
            "category": "imported",
            "physical_state": "LIQUID",
            "ingredients": [
                {"preferred_term": "EDTA"},
                {
                    "preferred_term": "CultureMech test-only source reagent 337 schema",
                    "term": {"id": "mediadive.compound:337071"},
                },
            ],
        },
    )
    result = occurrence_module.scan_ingredient_occurrences(corpus)
    assert not result.errors
    jobs = [
        (
            occurrence_module.build_mapped_output(result.occurrences),
            REPO_ROOT / "src/culturemech/schema/mapped_ingredients_schema.yaml",
            "MappedIngredientsCollection",
        ),
        (
            occurrence_module.build_unmapped_output(result.occurrences),
            REPO_ROOT / "src/culturemech/schema/unmapped_ingredients_schema.yaml",
            "UnmappedIngredientsCollection",
        ),
    ]
    for index, (output, schema, target_class) in enumerate(jobs):
        path = tmp_path / f"summary-{index}.yaml"
        occurrence_module.write_yaml_output(path, output)
        report = Validator(
            schema=str(schema),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        ).validate(yaml.safe_load(path.read_text(encoding="utf-8")), target_class=target_class)
        assert not [result for result in report.results if result.severity == Severity.ERROR]


def test_output_paths_must_be_distinct_before_publication(occurrence_module, tmp_path):
    shared = tmp_path / "shared.tsv"
    with pytest.raises(ValueError, match="output paths must be distinct"):
        occurrence_module.run_aggregation(
            input_dir=tmp_path,
            occurrences_output=shared,
            mapped_output=shared,
            unmapped_output=tmp_path / "unmapped.yaml",
            errors_output=tmp_path / "errors.tsv",
        )
    assert not shared.exists()


def _read_list(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def test_ingredient_list_reconciles_with_mapped_and_unmapped_views(occurrence_module, tmp_path):
    """One list row per view group; counts reconcile with the uncapped table."""

    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000051",
            "name": "List one",
            "category": "bacterial",
            "physical_state": "LIQUID",
            "ingredients": [
                {"preferred_term": "EDTA"},
                {"preferred_term": "EDTA"},
                {"preferred_term": "Calf brains"},
                {"preferred_term": ""},
            ],
        },
    )
    _write(
        corpus,
        "algae/two.yaml",
        {
            "id": "CultureMech:000052",
            "name": "List two",
            "category": "algae",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}, {"preferred_term": "Calf brains"}],
        },
    )

    outputs = _output_args(tmp_path, "out")
    assert occurrence_module.run_aggregation(input_dir=corpus, **outputs) == 0
    rows = _read_list(outputs["list_output"])
    mapped = yaml.safe_load(outputs["mapped_output"].read_text(encoding="utf-8"))
    unmapped = yaml.safe_load(outputs["unmapped_output"].read_text(encoding="utf-8"))

    with outputs["occurrences_output"].open(encoding="utf-8", newline="") as stream:
        occurrence_rows = list(csv.DictReader(stream, delimiter="\t"))

    assert list(rows[0]) == list(occurrence_module.INGREDIENT_LIST_FIELDS)
    assert len(rows) == mapped["total_mapped_count"] + unmapped["total_unmapped_count"]
    assert sum(int(row["occurrence_count"]) for row in rows) == len(occurrence_rows)
    # Same groups as the views, not merely the same number of groups.
    assert sorted(
        (row["resolved_identifier"], int(row["occurrence_count"]))
        for row in rows
        if row["mapping_status"] == "MAPPED"
    ) == sorted(
        (entry["resolved_identifier"], entry["occurrence_count"])
        for entry in mapped["mapped_ingredients"]
    )
    assert sorted(
        (row["preferred_term"], int(row["occurrence_count"]))
        for row in rows
        if row["mapping_status"] != "MAPPED"
    ) == sorted(
        (entry["placeholder_id"], entry["occurrence_count"])
        for entry in unmapped["unmapped_ingredients"]
    )

    edta = next(row for row in rows if row["resolved_identifier"] == "CHEBI:4735")
    assert edta["mapping_status"] == "MAPPED"
    assert edta["identifier_prefix"] == "CHEBI"
    assert (edta["occurrence_count"], edta["distinct_recipe_count"]) == ("3", "2")
    assert edta["recipe_categories"] == "ALGAE | BACTERIAL"
    assert rows[0]["resolved_identifier"] == "CHEBI:4735"

    calf = next(row for row in rows if row["preferred_term"] == "Calf brains")
    assert calf["resolved_identifier"] == ""
    assert calf["mapping_status"] == "UNMAPPED"

    blank = next(row for row in rows if row["preferred_term"].startswith("blank:"))
    assert blank["preferred_term"] == "blank:CultureMech:000051:ingredients:3"
    assert blank["label_variant_count"] == "0"


def test_ingredient_list_ignores_min_occurrences(occurrence_module, tmp_path):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000061",
            "name": "Singletons",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}, {"preferred_term": "Calf brains"}],
        },
    )
    outputs = _output_args(tmp_path, "out")
    assert occurrence_module.run_aggregation(input_dir=corpus, min_occurrences=2, **outputs) == 0
    mapped = yaml.safe_load(outputs["mapped_output"].read_text(encoding="utf-8"))
    assert mapped["total_mapped_count"] == 0
    assert len(_read_list(outputs["list_output"])) == 2


def test_list_output_must_be_distinct(occurrence_module, tmp_path):
    outputs = _output_args(tmp_path, "out")
    outputs["list_output"] = outputs["occurrences_output"]
    with pytest.raises(ValueError, match="output paths must be distinct"):
        occurrence_module.run_aggregation(input_dir=tmp_path, **outputs)


def test_ingredient_list_marks_ambiguous_and_whitespace_labels(occurrence_module, tmp_path):
    # Resolve through a fixed index: which real labels are ambiguous changes with
    # every MIM pin bump ("Sea Salt" stopped being one at 6643131b).
    from culturemech.ingredients.mim_label_index import MIMLabelIndex

    index = MIMLabelIndex.from_csv_text(
        "label,match_type,identifier,preferred_term,ontology_id,mapping_status,ambiguity\n"
        "Sea Salt,ontology_label,MICRO:0001647,Artificial Sea Salt,MICRO:0001647,MAPPED,"
        "unresolved:no_chemistry\n"
        "Sea Salt,ontology_label,NCIT:C75874,Sea salts,NCIT:C75874,MAPPED,"
        "unresolved:no_chemistry\n"
    )
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000071",
            "name": "Ambiguous and blank",
            "physical_state": "LIQUID",
            "ingredients": [
                {"preferred_term": "Sea Salt"},
                {"preferred_term": "   "},
                {"preferred_term": "   "},
            ],
        },
    )
    result = occurrence_module.scan_ingredient_occurrences(corpus, resolver=index.resolve)
    assert not result.errors
    rows = occurrence_module.build_ingredient_list(result.occurrences)

    sea_salt = next(row for row in rows if row["preferred_term"] == "Sea Salt")
    assert sea_salt["mapping_status"] == "AMBIGUOUS"
    assert sea_salt["resolved_identifier"] == ""

    blanks = sorted(
        row["preferred_term"]
        for row in rows
        if row["label_variant_count"] == 1 and row["label_variants"] == "   "
    )
    assert blanks == [
        "blank:CultureMech:000071:ingredients:1",
        "blank:CultureMech:000071:ingredients:2",
    ]
    unmapped = occurrence_module.build_unmapped_output(result.occurrences)
    assert (
        sorted(
            entry["placeholder_id"]
            for entry in unmapped["unmapped_ingredients"]
            if entry["placeholder_id"].startswith("blank:")
        )
        == blanks
    )


def test_list_output_is_optional_for_library_callers(occurrence_module, tmp_path):
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000081",
            "name": "No list",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}],
        },
    )
    outputs = _output_args(tmp_path, "out")
    list_path = outputs.pop("list_output")
    assert occurrence_module.run_aggregation(input_dir=corpus, **outputs) == 0
    assert outputs["occurrences_output"].exists()
    assert not list_path.exists()


def _scanned_rows(occurrence_module, tmp_path, labels: list[str]) -> list[Any]:
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/terms.yaml",
        {
            "id": "CultureMech:000091",
            "name": "Canonical terms",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": label} for label in labels],
        },
    )
    result = occurrence_module.scan_ingredient_occurrences(corpus)
    assert not result.errors
    return list(result.occurrences)


def test_canonical_term_ignores_fallback_mim_terms(occurrence_module, tmp_path):
    """#509: a fallback row's MIM term must not rename a trusted identity."""

    from dataclasses import replace

    rows = _scanned_rows(occurrence_module, tmp_path, ["CaCl2 x 2 H2O", "CaCl2 x 2 H2O"])
    assert {row.resolution_source for row in rows} == {"mim_exact"}
    identifier = rows[0].resolved_identifier
    fallback = replace(
        rows[0],
        component_index=99,
        preferred_term="CaCl2",
        resolution_source="ambiguous_local_fallback",
        mim_preferred_term="CaCl2",
    )
    group = [*rows, fallback]

    assert occurrence_module._canonical_term(group) == "CaCl2 x 2 H2O"
    mapped = occurrence_module.build_mapped_output(group)
    entry = next(e for e in mapped["mapped_ingredients"] if e["resolved_identifier"] == identifier)
    assert entry["preferred_term"] == entry["ontology_label"] == "CaCl2 x 2 H2O"
    assert entry["synonyms"] == ["CaCl2"]
    listed = occurrence_module.build_ingredient_list(group)
    assert listed[0]["preferred_term"] == "CaCl2 x 2 H2O"


@pytest.mark.parametrize(
    "wrapper", ["aggregate_mapped_ingredients", "aggregate_unmapped_ingredients"]
)
def test_standalone_wrappers_refresh_ingredient_list(occurrence_module, tmp_path, wrapper):
    """#512: rewriting the occurrence table also rewrites the list derived from it."""

    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000101",
            "name": "Wrapper",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}, {"preferred_term": "Calf brains"}],
        },
    )
    reference = _output_args(tmp_path, "reference")
    assert occurrence_module.run_aggregation(input_dir=corpus, **reference) == 0

    out = tmp_path / "wrapper"
    out.mkdir()
    list_path = out / "ingredients_list.tsv"
    list_path.write_text("stale\n", encoding="utf-8")
    rc = _load_script(wrapper).main(
        [
            "--input-dir",
            str(corpus),
            "--output",
            str(out / "view.yaml"),
            "--occurrences-output",
            str(out / "occurrences.tsv"),
            "--errors-output",
            str(out / "errors.tsv"),
            "--list-output",
            str(list_path),
        ]
    )
    assert rc == 0
    assert list_path.read_bytes() == reference["list_output"].read_bytes()
    assert (out / "occurrences.tsv").read_bytes() == reference["occurrences_output"].read_bytes()


def test_canonical_term_prefers_dominant_trusted_term_and_breaks_ties_by_code_point(
    occurrence_module, tmp_path
):
    """#509/#533: frequency, not alphabetical order, picks the name."""

    from dataclasses import replace

    rows = _scanned_rows(occurrence_module, tmp_path, ["CaCl2 x 2 H2O"] * 3)
    minority = replace(rows[0], component_index=99, mim_preferred_term="A minority term")
    assert occurrence_module._canonical_term([*rows, minority]) == "CaCl2 x 2 H2O"

    # The old rule took the alphabetically first term from any row, including the
    # fallback row's "A fallback term"; the new rule ignores it and breaks the 1:1
    # tie between trusted terms by code point (uppercase before lowercase).
    fallback = replace(
        rows[0],
        component_index=97,
        resolution_source="ambiguous_local_fallback",
        mim_preferred_term="A fallback term",
    )
    upper = replace(rows[0], component_index=98, mim_preferred_term="Z upper")
    lower = replace(rows[0], component_index=96, mim_preferred_term="b lower")
    assert occurrence_module._canonical_term([fallback, lower, upper]) == "Z upper"


def test_canonical_term_prefers_mim_mapped_over_rejected_terms(occurrence_module, tmp_path):
    """#529: an accepted hydrate term beats a more frequent REJECTED generic term."""

    from dataclasses import replace

    base = _scanned_rows(occurrence_module, tmp_path, ["CaCl2 x 2 H2O"])[0]
    assert base.mim_mapping_status == "MAPPED"
    rejected = [
        replace(
            base,
            component_index=index,
            mim_preferred_term="Calcium chloride",
            mim_mapping_status="REJECTED",
        )
        for index in range(1, 4)
    ]
    assert occurrence_module._canonical_term([base, *rejected]) == "CaCl2 x 2 H2O"
    # REJECTED trusted terms still outrank source labels when nothing is MAPPED.
    assert occurrence_module._canonical_term(rejected) == "Calcium chloride"


def test_canonical_term_counts_mim_normalized_as_trusted(occurrence_module, tmp_path):
    from dataclasses import replace

    base = _scanned_rows(occurrence_module, tmp_path, ["CaCl2 x 2 H2O"])[0]
    normalized = [
        replace(base, component_index=index, resolution_source="mim_normalized")
        for index in range(2)
    ]
    fallback = replace(
        base,
        component_index=5,
        preferred_term="Other label",
        resolution_source="ambiguous_local_fallback",
        mim_preferred_term="Other label",
    )
    assert occurrence_module._canonical_term([*normalized, fallback]) == "CaCl2 x 2 H2O"


def test_canonical_term_falls_back_to_dominant_source_label(occurrence_module, tmp_path):
    """Without directly resolved rows, fallback MIM terms are ignored (#534)."""

    from dataclasses import replace

    base = _scanned_rows(occurrence_module, tmp_path, ["CaCl2 x 2 H2O"])[0]
    rows = [
        replace(
            base,
            component_index=index,
            preferred_term=label,
            resolution_source="ambiguous_local_fallback",
            mim_preferred_term="A different identity's term",
        )
        for index, label in enumerate(["b label", "b label", "a label"])
    ]
    assert occurrence_module._canonical_term(rows) == "b label"
    no_labels = [replace(row, preferred_term="") for row in rows]
    assert occurrence_module._canonical_term(no_labels) == base.resolved_identifier


def _wrapper_corpus(tmp_path: Path) -> Path:
    corpus = tmp_path / "corpus"
    _write(
        corpus,
        "bacterial/one.yaml",
        {
            "id": "CultureMech:000111",
            "name": "Wrapper defaults",
            "physical_state": "LIQUID",
            "ingredients": [{"preferred_term": "EDTA"}],
        },
    )
    return corpus


@pytest.mark.parametrize(
    "script",
    ["aggregate_ingredients", "aggregate_mapped_ingredients", "aggregate_unmapped_ingredients"],
)
def test_default_list_output_sits_beside_occurrence_table(tmp_path, script, monkeypatch):
    """#532: without --list-output, the list follows --occurrences-output."""

    corpus = _wrapper_corpus(tmp_path)
    monkeypatch.chdir(tmp_path)
    out = tmp_path / "custom"
    out.mkdir()
    view_args = (
        ["--mapped-output", str(out / "m.yaml"), "--unmapped-output", str(out / "u.yaml")]
        if script == "aggregate_ingredients"
        else ["--output", str(out / "view.yaml")]
    )
    rc = _load_script(script).main(
        [
            "--input-dir",
            str(corpus),
            *view_args,
            "--occurrences-output",
            str(out / "occurrences.tsv"),
            "--errors-output",
            str(out / "errors.tsv"),
        ]
    )
    assert rc == 0
    assert (out / "ingredients_list.tsv").exists()
    assert not (tmp_path / "output").exists()


@pytest.mark.parametrize(
    "wrapper", ["aggregate_mapped_ingredients", "aggregate_unmapped_ingredients"]
)
def test_wrapper_input_errors_leave_list_untouched(tmp_path, wrapper):
    corpus = _wrapper_corpus(tmp_path)
    _write(corpus, "bacterial/bad.yaml", "id: [unclosed\n")
    out = tmp_path / "out"
    out.mkdir()
    list_path = out / "ingredients_list.tsv"
    list_path.write_text("existing\n", encoding="utf-8")
    rc = _load_script(wrapper).main(
        [
            "--input-dir",
            str(corpus),
            "--output",
            str(out / "view.yaml"),
            "--occurrences-output",
            str(out / "occurrences.tsv"),
            "--errors-output",
            str(out / "errors.tsv"),
            "--list-output",
            str(list_path),
        ]
    )
    assert rc != 0
    assert list_path.read_text(encoding="utf-8") == "existing\n"


@pytest.mark.parametrize(
    "wrapper", ["aggregate_mapped_ingredients", "aggregate_unmapped_ingredients"]
)
def test_wrapper_rejects_aliased_list_output(tmp_path, wrapper):
    out = tmp_path / "out"
    out.mkdir()
    with pytest.raises(ValueError, match="output paths must be distinct"):
        _load_script(wrapper).main(
            [
                "--input-dir",
                str(_wrapper_corpus(tmp_path)),
                "--output",
                str(out / "view.yaml"),
                "--occurrences-output",
                str(out / "occurrences.tsv"),
                "--errors-output",
                str(out / "errors.tsv"),
                "--list-output",
                str(out / "occurrences.tsv"),
            ]
        )
