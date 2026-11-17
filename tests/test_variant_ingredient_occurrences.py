"""Native variant occurrence, lossless ledger and bundle boundaries (#683)."""

from __future__ import annotations

import copy
import csv
import importlib
import json
from pathlib import Path

import ingredient_occurrences as occurrences
import ingredient_release_bundle as bundle
import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml.validator.report import Severity


def variant_medium():
    """Synthetic scientific statements only; never a production curation claim."""
    modifications = [
        'Add synthetic reagent "A"\nwith a quoted\ttreatment context.',
        "Remove synthetic removed-only reagent.",
        "Replace synthetic old-only reagent with EDTA.",
        "Set the water concentration for this synthetic assay.",
    ]
    changes = []
    for index, (action, ingredient) in enumerate(
        [
            ("ADD", {"preferred_term": "Synthetic variant-only reagent 683"}),
            ("REMOVE", {"preferred_term": "Synthetic removed-only reagent 683"}),
            ("REPLACE", {"preferred_term": "EDTA"}),
            (
                "SET_CONCENTRATION",
                {
                    "preferred_term": "water",
                    "term": {"id": "CHEBI:15377"},
                    "concentration": {"value": "0", "unit": "G_PER_L", "per_volume": "per liter"},
                },
            ),
        ]
    ):
        change = {
            "action": action,
            "ingredient": ingredient,
            "stage": "synthetic assay treatment",
            "source_modification_index": index,
            "source_text": modifications[index],
            "evidence": [
                {
                    "reference": "https://example.org/synthetic-variant-fixture",
                    "supports": "SUPPORT",
                    "snippet": modifications[index],
                    "explanation": "Synthetic fixture asserts this exact change and stage.",
                }
            ],
            "notes": "Synthetic provenance stays lossless.",
        }
        if action == "REPLACE":
            change["replaced_ingredient"] = {"preferred_term": "Synthetic old-only reagent 683"}
        changes.append(change)
    variant = {
        "name": "Synthetic assay",
        "modifications": modifications,
        "ingredient_changes": changes,
    }
    other = copy.deepcopy(variant)
    other["name"] = "Synthetic stock"
    other["ingredient_changes"] = [copy.deepcopy(changes[0])]
    other["ingredient_changes"][0]["stage"] = "synthetic stock preparation"
    return {
        "id": "CultureMech:000001",
        "name": "Synthetic variant occurrence fixture",
        "physical_state": "LIQUID",
        "category": "bacterial",
        "ingredients": [{"preferred_term": "water", "term": {"id": "CHEBI:15377"}}],
        "variants": [variant, other, {"name": "Uncurated prose", "modifications": ["Other prose"]}],
    }


@pytest.fixture
def corpus(tmp_path):
    root = tmp_path / "inputs"
    root.mkdir()
    (root / "medium.yaml").write_text(
        yaml.safe_dump(variant_medium(), sort_keys=False), encoding="utf-8"
    )
    return root


def read_rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def test_native_scan_preserves_all_changes_without_materializing_variant_formulations(corpus):
    result = occurrences.scan_ingredient_occurrences(corpus)
    assert not result.errors
    assert len(result.occurrences) == 5  # one base, three first-variant targets, one stock target
    assert len(result.variant_changes) == 6  # five events; REPLACE retains both descriptors
    assert len({row.key for row in result.occurrences}) == 5
    assert len({(row.recipe_id, row.descriptor_path) for row in result.variant_changes}) == 6
    assert [row.preferred_term for row in result.occurrences if not row.change_action] == ["water"]
    context_only = [row for row in result.variant_changes if not row.counts_as_presence]
    assert {(row.change_action, row.descriptor_role) for row in context_only} == {
        ("REMOVE", "ingredient"),
        ("REPLACE", "replaced_ingredient"),
    }
    assert all(row.resolved_identifier == "" for row in context_only)
    assert all(
        row.preferred_term not in {item.preferred_term for item in result.occurrences}
        for row in context_only
    )
    repeated_label = [row for row in result.occurrences if row.change_action == "ADD"]
    assert {row.variant_index for row in repeated_label} == {0, 1}
    assert {row.change_stage for row in repeated_label} == {
        "synthetic assay treatment",
        "synthetic stock preparation",
    }
    for row in result.variant_changes:
        source = variant_medium()["variants"][row.variant_index]["ingredient_changes"][
            row.change_index
        ]
        assert json.loads(row.change_json) == source
        assert json.loads(row.ingredient_json) == source[row.descriptor_role]
        assert json.loads(row.evidence_json) == source["evidence"]
        assert row.source_text == source["source_text"]
        assert (
            row.descriptor_path
            == f"/{row.component_field}/{row.component_index}/{row.descriptor_role}"
        )
    zero = next(row for row in result.occurrences if row.change_action == "SET_CONCENTRATION")
    assert (
        zero.concentration_value == "0"
    )  # explicit target, no numerical or base-formulation inference
    assert json.loads(zero.ingredient_json)["concentration"]["per_volume"] == "per liter"
    # Defense in depth: even passing the whole ledger to a summary cannot admit removals.
    present = occurrences.build_ingredient_list(result.variant_changes)
    assert sum(row["occurrence_count"] for row in present) == 4
    assert not any(
        "removed-only" in row["preferred_term"] or "old-only" in row["preferred_term"]
        for row in present
    )


def test_native_variant_summaries_validate_against_closed_schemas(corpus):
    result = occurrences.scan_ingredient_occurrences(corpus)
    assert not result.errors
    schema_root = Path(occurrences.__file__).resolve().parents[1] / "src/culturemech/schema"
    for builder, schema, target in (
        (
            occurrences.build_mapped_output,
            "mapped_ingredients_schema.yaml",
            "MappedIngredientsCollection",
        ),
        (
            occurrences.build_unmapped_output,
            "unmapped_ingredients_schema.yaml",
            "UnmappedIngredientsCollection",
        ),
    ):
        output = builder(result.occurrences)
        report = Validator(
            schema=str(schema_root / schema),
            validation_plugins=[JsonschemaValidationPlugin(closed=True)],
        ).validate(output, target_class=target)
        assert not [item for item in report.results if item.severity == Severity.ERROR]
        entries = next(value for key, value in output.items() if key.endswith("_ingredients"))
        rows = [row for entry in entries for row in entry["recipe_occurrences"]]
        assert any(row.get("change_action") and row["evidence_json"] for row in rows)


@pytest.mark.parametrize(
    "script",
    ["aggregate_ingredients", "aggregate_mapped_ingredients", "aggregate_unmapped_ingredients"],
)
def test_all_cli_entry_points_preserve_same_ledger_and_positive_counts(corpus, tmp_path, script):
    output = tmp_path / script
    output.mkdir()
    args = [
        "--input-dir",
        str(corpus),
        "--occurrences-output",
        str(output / "occurrences.tsv"),
        "--errors-output",
        str(output / "errors.tsv"),
    ]
    if script == "aggregate_ingredients":
        args += [
            "--mapped-output",
            str(output / "mapped.yaml"),
            "--unmapped-output",
            str(output / "unmapped.yaml"),
        ]
    else:
        args += ["--output", str(output / "summary.yaml")]
    assert importlib.import_module(script).main(args) == 0
    rows = read_rows(output / "occurrences.tsv")
    ledger = read_rows(output / "variant_ingredient_changes.tsv")
    assert len(rows) == 5 and len(ledger) == 6
    assert sum(row["counts_as_presence"] == "false" for row in ledger) == 2
    assert (
        sum(int(row["occurrence_count"]) for row in read_rows(output / "ingredients_list.tsv")) == 5
    )
    native = occurrences.scan_ingredient_occurrences(corpus)
    assert ledger == [
        {
            **{key: str(value) for key, value in row.as_dict().items()},
            "counts_as_presence": "true" if row.counts_as_presence else "false",
        }
        for row in native.variant_changes
    ]
    first_bytes = (output / "variant_ingredient_changes.tsv").read_bytes()
    assert importlib.import_module(script).main(args) == 0
    assert (output / "variant_ingredient_changes.tsv").read_bytes() == first_bytes


@pytest.mark.parametrize(
    "script",
    ["aggregate_ingredients", "aggregate_mapped_ingredients", "aggregate_unmapped_ingredients"],
)
def test_ledger_output_collision_refuses_before_touching_existing_artifact(
    corpus, tmp_path, script
):
    shared = tmp_path / "shared.tsv"
    shared.write_text("retained original\n")
    args = [
        "--input-dir",
        str(corpus),
        "--occurrences-output",
        str(shared),
        "--changes-output",
        str(shared),
        "--errors-output",
        str(tmp_path / "errors.tsv"),
    ]
    if script == "aggregate_ingredients":
        args += [
            "--mapped-output",
            str(tmp_path / "mapped.yaml"),
            "--unmapped-output",
            str(tmp_path / "unmapped.yaml"),
        ]
    else:
        args += ["--output", str(tmp_path / "summary.yaml")]
    with pytest.raises(ValueError, match="distinct"):
        importlib.import_module(script).main(args)
    assert shared.read_text() == "retained original\n"
    assert not (tmp_path / "errors.tsv").exists()


def test_invalid_source_binding_is_fatal_before_success_artifacts_change(corpus, tmp_path):
    output = tmp_path / "invalid"
    output.mkdir()
    outputs = {name: output / name for name in bundle.PRODUCTS}
    for path in outputs.values():
        path.write_text("retained original\n")
    source = variant_medium()
    source["variants"][0]["ingredient_changes"][0]["source_text"] = "Not the retained source text"
    (corpus / "medium.yaml").write_text(yaml.safe_dump(source))
    assert (
        occurrences.run_aggregation(
            corpus,
            outputs["ingredient_occurrences.tsv"],
            outputs["mapped_ingredients.yaml"],
            outputs["unmapped_ingredients.yaml"],
            outputs["ingredient_aggregation_errors.tsv"],
            list_output=outputs["ingredients_list.tsv"],
        )
        == 1
    )
    errors = read_rows(outputs["ingredient_aggregation_errors.tsv"])
    assert any(row["layer"] == "semantic" and "source_text" in row["path"] for row in errors)
    for name, path in outputs.items():
        if name != "ingredient_aggregation_errors.tsv":
            assert path.read_text() == "retained original\n"


def test_context_only_resolver_error_is_not_silently_dropped(corpus):
    def resolver(descriptor):
        if "old-only" in descriptor["preferred_term"]:
            raise ValueError("Synthetic old descriptor resolution failure")
        return occurrences.resolve_ingredient(descriptor)

    result = occurrences.scan_ingredient_occurrences(corpus, resolver=resolver)
    assert any(
        error.category == "resolver_error" and error.path.endswith("/replaced_ingredient")
        for error in result.errors
    )


def test_bundle_v3_reconciles_and_pins_positive_and_context_only_products(corpus, tmp_path):
    directory = tmp_path / "bundle"
    manifest = bundle.build(corpus, directory)
    assert manifest["contract"] == "culturemech-direct-ingredients-v3"
    assert manifest["counts"]["occurrences"] == 5
    assert manifest["counts"]["base_direct_occurrences"] == 1
    assert manifest["counts"]["variant_positive_occurrences"] == 4
    assert manifest["counts"]["variant_change_events"] == 5
    assert manifest["counts"]["variant_change_mentions"] == 6
    assert manifest["counts"]["variant_context_only_mentions"] == 2
    assert manifest["counts"]["variant_changes_by_action"] == {
        "ADD": 2,
        "REMOVE": 1,
        "REPLACE": 1,
        "SET_CONCENTRATION": 1,
    }
    assert manifest["products"]["variant_ingredient_changes.tsv"]["data_rows"] == 6
    assert bundle.verify(directory, corpus)["status"] == "VERIFIED_CANDIDATE"
    ledger = directory / "variant_ingredient_changes.tsv"
    rows = read_rows(ledger)
    rows = [row for row in rows if row["descriptor_role"] != "replaced_ingredient"]
    with ledger.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=occurrences.VARIANT_CHANGE_FIELDS, delimiter="\t"
        )
        writer.writeheader()
        writer.writerows(rows)
    with pytest.raises(bundle.BundleError, match="membership/context"):
        bundle.artifact_accounting(directory, manifest["inputs"])
    with pytest.raises(bundle.BundleError):
        bundle.verify(directory, corpus)


def test_remove_only_recipe_stays_zero_positive_but_is_discoverable(corpus, tmp_path):
    source = variant_medium()
    source["ingredients"] = []
    source["variants"] = source["variants"][:1]
    source["variants"][0]["ingredient_changes"] = [source["variants"][0]["ingredient_changes"][1]]
    (corpus / "medium.yaml").write_text(yaml.safe_dump(source))
    manifest = bundle.build(corpus, tmp_path / "remove-only")
    assert manifest["counts"]["occurrences"] == 0
    assert manifest["counts"]["ingredient_groups"] == 0
    assert manifest["counts"]["variant_context_only_mentions"] == 1
    assert manifest["counts"]["records_without_direct_occurrences"] == 1
    assert (
        read_rows(tmp_path / "remove-only" / "variant_ingredient_changes.tsv")[0]["change_action"]
        == "REMOVE"
    )
