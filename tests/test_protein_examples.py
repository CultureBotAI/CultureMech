"""Unit tests for typed UniProt protein examples (#659 / culturemech-infra-0003).

Covers:
1. LinkML schema + semantic validation (positive and negative cases)
2. Maintained writer `scripts/apply_protein_examples.py` (dry-run, apply, history append,
   idempotency, layer boundary refusal, invalid proposal rejection)
3. KGX export `biolink:Protein` nodes and organism/medium/cofactor/substrate edges
4. Reference `data/reference/cofactors.yaml` ChEBI ID uniqueness (`heme C` / `heme d1`)
5. OAK / ID-label configuration for `UniProtKB`
"""

from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import apply_protein_examples  # noqa: E402
import validate_id_label_correspondence  # noqa: E402
import validate_protein_examples  # noqa: E402
import validate_strict  # noqa: E402

from culturemech.export.kgx_export import (  # noqa: E402
    _QUALIFIER_COLUMNS,
    nodes,
    to_edge,
    transform,
)
from culturemech.validation.protein_examples import (  # noqa: E402
    is_valid_uniprot_curie,
    validate_recipe_protein_examples,
)
from culturemech.validation.write_validated import (  # noqa: E402
    LayerBoundaryError,
    validate_recipe,
)


def _valid_protein_example(
    uniprot_id: str = "UniProtKB:P02931",
    uniprot_label: str = "Outer membrane porin F",
    organism_id: str = "NCBITaxon:562",
    organism_label: str = "Escherichia coli",
) -> dict[str, Any]:
    return {
        "uniprot_term": {
            "id": uniprot_id,
            "label": uniprot_label,
        },
        "organism_term": {
            "id": organism_id,
            "label": organism_label,
        },
        "gene_symbol": "ompF",
        "locus_tag": "b0929",
        "ec_number": "EC:1.14.13.25",
        "sequence_scope": "Swiss-Prot reviewed entry for Escherichia coli OmpF porin",
        "functional_role": "Outer membrane diffusion porin facilitating passive nutrient uptake",
        "cofactor_term": {
            "id": "CHEBI:18248",
            "label": "iron atom",
        },
        "substrate_term": {
            "id": "CHEBI:17234",
            "label": "D-glucose",
        },
        "evidence": [
            {
                "reference": "PMID:12345678",
                "supports": "SUPPORT",
                "snippet": "OmpF forms general diffusion pores in the outer membrane of Escherichia coli.",
                "explanation": "Demonstrates OmpF (UniProtKB:P02931) porin function in Escherichia coli (NCBITaxon:562).",
            }
        ],
    }


def _base_recipe() -> dict[str, Any]:
    return {
        "id": "CultureMech:999659",
        "name": "Minimal Glucose Medium",
        "medium_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "D-Glucose",
                "term": {"id": "CHEBI:17234", "label": "D-glucose"},
                "concentration": {"value": "10", "unit": "G_PER_L"},
            }
        ],
        "target_organisms": [
            {
                "preferred_term": "Escherichia coli",
                "term": {"id": "NCBITaxon:562", "label": "Escherichia coli"},
                "cofactor_requirements": [
                    {
                        "cofactor": {
                            "preferred_term": "heme C",
                            "category": "METALS",
                            "term": {"id": "CHEBI:60562", "label": "ferroheme c"},
                        },
                        "can_biosynthesize": True,
                    }
                ],
                "transporters": [
                    {
                        "name": "ompF",
                        "transporter_type": "PORIN",
                        "substrate_terms": [{"id": "CHEBI:17234", "label": "D-glucose"}],
                    }
                ],
            }
        ],
    }


class TestUniProtAccessionPattern:
    """Test canonical UniProtKB CURIE syntax."""

    @pytest.mark.parametrize(
        "curie",
        [
            "UniProtKB:P02931",
            "UniProtKB:Q9I4X3",
            "UniProtKB:O28869",
            "UniProtKB:A0A024RBG1",
        ],
    )
    def test_valid_uniprot_curies(self, curie: str) -> None:
        assert is_valid_uniprot_curie(curie)

    @pytest.mark.parametrize(
        "curie",
        [
            "",
            "P02931",
            "uniprot:P02931",
            "UniProtKB:123456",
            "UniProtKB:P0293",
            "UniProtKB:P02931-1",
            "CHEBI:17234",
        ],
    )
    def test_invalid_uniprot_curies(self, curie: str) -> None:
        assert not is_valid_uniprot_curie(curie)


class TestProteinExampleValidation:
    """Positive and negative validation tests for ProteinExample."""

    def test_valid_protein_examples_across_all_attachment_points(self, tmp_path: Path) -> None:
        recipe = _base_recipe()
        recipe["protein_examples"] = [_valid_protein_example("UniProtKB:P02931")]
        recipe["target_organisms"][0]["protein_examples"] = [
            _valid_protein_example("UniProtKB:P0A910", "Outer membrane protein A")
        ]
        recipe["target_organisms"][0]["cofactor_requirements"][0]["protein_examples"] = [
            _valid_protein_example("UniProtKB:P0ABJ9", "Cytochrome b562")
        ]
        recipe["target_organisms"][0]["cofactor_requirements"][0]["cofactor"][
            "protein_examples"
        ] = [_valid_protein_example("UniProtKB:P0ABK2", "Cytochrome c-type biogenesis protein")]
        recipe["target_organisms"][0]["transporters"][0]["protein_examples"] = [
            _valid_protein_example(
                "UniProtKB:P0AEX9", "Maltose/maltodextrin-binding periplasmic protein"
            )
        ]
        recipe["ingredients"][0]["cofactors_provided"] = [
            {
                "preferred_term": "heme C",
                "category": "METALS",
                "term": {"id": "CHEBI:60562", "label": "ferroheme c"},
                "protein_examples": [
                    _valid_protein_example("UniProtKB:P0ABK5", "Cytochrome c biogenesis protein")
                ],
            }
        ]

        assert validate_recipe_protein_examples(recipe) == []
        assert validate_recipe(recipe) == []

        yaml_path = tmp_path / "valid_recipe.yaml"
        yaml_path.write_text(yaml.safe_dump(recipe, sort_keys=False), encoding="utf-8")
        result = validate_strict.validate_one(yaml_path)
        assert result == [], f"Expected strict validation to pass, got: {result}"

    def test_rejects_invalid_uniprot_accession(self) -> None:
        recipe = _base_recipe()
        bad = _valid_protein_example(uniprot_id="UniProtKB:BAD_ID")
        recipe["protein_examples"] = [bad]

        errors = [i.message for i in validate_recipe_protein_examples(recipe)]
        assert any("invalid UniProtKB accession" in e for e in errors)
        assert validate_recipe(recipe) != []

    def test_rejects_empty_uniprot_label(self) -> None:
        recipe = _base_recipe()
        bad = _valid_protein_example()
        bad["uniprot_term"]["label"] = "   "
        recipe["protein_examples"] = [bad]

        errors = [i.message for i in validate_recipe_protein_examples(recipe)]
        assert any("uniprot_term.label" in e for e in errors)
        assert validate_recipe(recipe) != []

    def test_rejects_non_ncbitaxon_organism_term(self) -> None:
        recipe = _base_recipe()
        bad = _valid_protein_example(organism_id="CHEBI:17234")
        recipe["protein_examples"] = [bad]

        errors = [i.message for i in validate_recipe_protein_examples(recipe)]
        assert any("NCBITaxon" in e for e in errors)
        assert validate_recipe(recipe) != []

    def test_rejects_parent_organism_taxon_mismatch_without_note(self) -> None:
        recipe = _base_recipe()
        mismatch = _valid_protein_example(
            organism_id="NCBITaxon:83333",
            organism_label="Escherichia coli K-12",
        )
        recipe["target_organisms"][0]["protein_examples"] = [mismatch]

        errors = [i.message for i in validate_recipe_protein_examples(recipe)]
        assert any("differs from enclosing target_organisms" in e for e in errors)

        mismatch_with_note = copy.deepcopy(mismatch)
        mismatch_with_note["notes"] = (
            "UniProtKB:P02931 is annotated on reference strain Escherichia coli K-12 (NCBITaxon:83333), "
            "a strain of target organism Escherichia coli (NCBITaxon:562)."
        )
        recipe["target_organisms"][0]["protein_examples"] = [mismatch_with_note]
        assert validate_recipe_protein_examples(recipe) == []

    def test_rejects_invalid_ec_number(self) -> None:
        recipe = _base_recipe()
        bad = _valid_protein_example()
        bad["ec_number"] = "1.14.13.25"
        recipe["protein_examples"] = [bad]

        errors = [i.message for i in validate_recipe_protein_examples(recipe)]
        assert any("ec_number" in e for e in errors)
        assert validate_recipe(recipe) != []

    def test_rejects_missing_or_non_supporting_evidence(self) -> None:
        recipe = _base_recipe()
        no_ev = _valid_protein_example()
        no_ev["evidence"] = []
        recipe["protein_examples"] = [no_ev]
        assert any(
            "at least one claim-scoped EvidenceItem" in i.message
            for i in validate_recipe_protein_examples(recipe)
        )

        refute_only = _valid_protein_example()
        refute_only["evidence"][0]["supports"] = "REFUTE"
        recipe["protein_examples"] = [refute_only]
        assert any(
            "SUPPORT or PARTIAL" in i.message for i in validate_recipe_protein_examples(recipe)
        )

        no_snippet = _valid_protein_example()
        no_snippet["evidence"][0]["snippet"] = ""
        recipe["protein_examples"] = [no_snippet]
        assert any("snippet" in i.message for i in validate_recipe_protein_examples(recipe))

        bad_ref = _valid_protein_example()
        bad_ref["evidence"][0]["reference"] = "invalid-ref-string"
        recipe["protein_examples"] = [bad_ref]
        assert any("expected PMID:" in i.message for i in validate_recipe_protein_examples(recipe))

    def test_rejects_duplicate_uniprot_organism_pair_in_list(self) -> None:
        recipe = _base_recipe()
        ex = _valid_protein_example()
        recipe["protein_examples"] = [ex, copy.deepcopy(ex)]

        errors = [i.message for i in validate_recipe_protein_examples(recipe)]
        assert any("duplicate (uniprot_term.id, organism_term.id)" in e for e in errors)


class TestApplyProteinExamplesWriter:
    """Test maintained history-appending writer scripts/apply_protein_examples.py."""

    def test_dry_run_and_apply_with_history_and_idempotency(self, tmp_path: Path) -> None:
        norm_dir = tmp_path / "data" / "normalized_yaml" / "bacterial"
        norm_dir.mkdir(parents=True)
        record_path = norm_dir / "Minimal_Glucose_Medium.yaml"
        original_recipe = _base_recipe()
        record_path.write_text(yaml.safe_dump(original_recipe, sort_keys=False), encoding="utf-8")

        proposals_path = tmp_path / "proposals.yaml"
        proposals_payload = {
            "proposals": [
                {
                    "recipe_id": "CultureMech:999659",
                    "target_scope": "organism",
                    "organism_taxon_id": "NCBITaxon:562",
                    "source_note": "PMID:12345678 OmpF curation",
                    "protein_example": _valid_protein_example(),
                }
            ]
        }
        proposals_path.write_text(
            yaml.safe_dump(proposals_payload, sort_keys=False), encoding="utf-8"
        )

        # 1. Dry-run does not mutate the file on disk
        rc = apply_protein_examples.main(
            [
                "--input",
                str(proposals_path),
                "--normalized-dir",
                str(tmp_path / "data" / "normalized_yaml"),
                "--dry-run",
            ]
        )
        assert rc == 0
        after_dry = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        assert "protein_examples" not in after_dry["target_organisms"][0]
        assert "curation_history" not in after_dry

        # 2. Apply writes validated protein_examples and appends curation_history
        rc_apply = apply_protein_examples.main(
            [
                "--input",
                str(proposals_path),
                "--normalized-dir",
                str(tmp_path / "data" / "normalized_yaml"),
                "--apply",
            ]
        )
        assert rc_apply == 0
        after_apply = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        examples = after_apply["target_organisms"][0]["protein_examples"]
        assert len(examples) == 1
        assert examples[0]["uniprot_term"]["id"] == "UniProtKB:P02931"
        history = after_apply.get("curation_history") or []
        assert len(history) == 1
        assert history[0]["curator"] == "apply_protein_examples.py"
        assert history[0]["action"] == "ANNOTATED"

        # 3. Re-running apply with the same proposal is idempotent (no duplicate entry or history)
        rc_reapply = apply_protein_examples.main(
            [
                "--input",
                str(proposals_path),
                "--normalized-dir",
                str(tmp_path / "data" / "normalized_yaml"),
                "--apply",
            ]
        )
        assert rc_reapply == 0
        after_reapply = yaml.safe_load(record_path.read_text(encoding="utf-8"))
        assert len(after_reapply["target_organisms"][0]["protein_examples"]) == 1
        assert len(after_reapply["curation_history"]) == 1

    def test_refuses_merge_yaml_layer(self, tmp_path: Path) -> None:
        merge_dir = tmp_path / "data" / "merge_yaml" / "merged_2026"
        merge_dir.mkdir(parents=True)
        merge_file = merge_dir / "Record.yaml"
        merge_file.write_text(yaml.safe_dump(_base_recipe(), sort_keys=False), encoding="utf-8")

        proposals_path = tmp_path / "proposals.yaml"
        proposals_path.write_text(
            yaml.safe_dump(
                {
                    "proposals": [
                        {
                            "recipe_id": "CultureMech:999659",
                            "target_scope": "recipe",
                            "protein_example": _valid_protein_example(),
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )
        with pytest.raises(LayerBoundaryError):
            apply_protein_examples.main(
                [
                    "--input",
                    str(proposals_path),
                    "--normalized-dir",
                    str(merge_dir),
                    "--apply",
                ]
            )

        raw_dir = tmp_path / "data" / "raw_yaml"
        raw_dir.mkdir(parents=True)
        with pytest.raises(LayerBoundaryError):
            apply_protein_examples.main(
                [
                    "--input",
                    str(proposals_path),
                    "--normalized-dir",
                    str(raw_dir),
                    "--apply",
                ]
            )

    def test_refuses_invalid_proposal_without_mutating_file(self, tmp_path: Path) -> None:
        norm_dir = tmp_path / "data" / "normalized_yaml" / "bacterial"
        norm_dir.mkdir(parents=True)
        record_path = norm_dir / "Minimal_Glucose_Medium.yaml"
        record_path.write_text(yaml.safe_dump(_base_recipe(), sort_keys=False), encoding="utf-8")
        before_bytes = record_path.read_bytes()

        bad_example = _valid_protein_example(uniprot_id="UniProtKB:INVALID")
        proposals_path = tmp_path / "bad_proposals.yaml"
        proposals_path.write_text(
            yaml.safe_dump(
                {
                    "proposals": [
                        {
                            "recipe_id": "CultureMech:999659",
                            "target_scope": "recipe",
                            "protein_example": bad_example,
                        }
                    ]
                }
            ),
            encoding="utf-8",
        )

        with pytest.raises(ValueError, match="Invalid ProteinExample"):
            apply_protein_examples.main(
                [
                    "--input",
                    str(proposals_path),
                    "--normalized-dir",
                    str(tmp_path / "data" / "normalized_yaml"),
                    "--apply",
                ]
            )
        assert record_path.read_bytes() == before_bytes


class TestKGXProteinExport:
    """Test KGX node and edge emission for ProteinExample."""

    def test_emits_biolink_protein_node_and_edges(self) -> None:
        recipe = _base_recipe()
        recipe["protein_examples"] = [_valid_protein_example()]
        recipe["target_organisms"][0]["cofactor_requirements"][0]["protein_examples"] = [
            _valid_protein_example()
        ]

        node_list = list(nodes(recipe))
        by_id = {n["id"]: n for n in node_list}
        assert "UniProtKB:P02931" in by_id
        protein_node = by_id["UniProtKB:P02931"]
        assert protein_node["category"] == ["biolink:Protein"]
        assert protein_node["name"] == "Outer membrane porin F"

        edge_list = list(transform(recipe))
        protein_edges = [e for e in edge_list if "UniProtKB:P02931" in (e["subject"], e["object"])]
        assert len(protein_edges) == len({e["id"] for e in protein_edges})
        triples = {(e["subject"], e["predicate"], e["object"]) for e in protein_edges}
        assert ("CultureMech:999659", "biolink:related_to", "UniProtKB:P02931") in triples
        assert ("UniProtKB:P02931", "biolink:in_taxon", "NCBITaxon:562") in triples
        assert ("UniProtKB:P02931", "biolink:interacts_with", "CHEBI:18248") in triples
        assert ("UniProtKB:P02931", "biolink:interacts_with", "CHEBI:17234") in triples

        for edge in protein_edges:
            assert edge["publications"] == ["PMID:12345678"]
            for q in edge.get("qualifiers") or []:
                assert q["qualifier_type_id"] in _QUALIFIER_COLUMNS
            row = to_edge(edge)
            assert row.publications == ["PMID:12345678"]
            assert row.role == "Outer membrane diffusion porin facilitating passive nutrient uptake"


class TestReferenceAndConfigPrerequisites:
    """Test reference cofactor ChEBI uniqueness and OAK/id_label UniProtKB configuration."""

    def test_cofactors_reference_chebi_ids_are_unique(self) -> None:
        cofactors_path = REPO_ROOT / "data" / "reference" / "cofactors.yaml"
        data = yaml.safe_load(cofactors_path.read_text(encoding="utf-8"))
        cofactors = data["cofactors"]
        ids = [c["term"]["id"] for c in cofactors if "term" in c and "id" in c["term"]]
        assert len(ids) == len(set(ids)), f"Duplicate ChEBI IDs in cofactors.yaml: {ids}"

        by_name = {c["preferred_term"]: c["term"]["id"] for c in cofactors}
        assert by_name["heme C"] == "CHEBI:60562"
        assert by_name["heme d1"] == "CHEBI:61147"
        assert by_name["siroheme"] == "CHEBI:28788"

    def test_oak_and_id_label_configs_handle_uniprotkb(self) -> None:
        oak_cfg = yaml.safe_load(
            (REPO_ROOT / "conf" / "oak_config.yaml").read_text(encoding="utf-8")
        )
        assert "UniProtKB" in oak_cfg.get("ontology_adapters", {})

        targets_cfg = yaml.safe_load(
            (REPO_ROOT / "conf" / "id_label_targets.yaml").read_text(encoding="utf-8")
        )
        assert "UniProtKB" in targets_cfg.get("ignored_prefixes", [])

    def test_id_label_correspondence_passes_on_recipe_with_protein_examples(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        monkeypatch.setattr(validate_id_label_correspondence, "REPO_ROOT", tmp_path)
        targets_cfg = yaml.safe_load(
            (REPO_ROOT / "conf" / "id_label_targets.yaml").read_text(encoding="utf-8")
        )
        ignored = list(targets_cfg.get("ignored_prefixes") or []) + ["CHEBI", "NCBITaxon"]

        recipe = _base_recipe()
        recipe["protein_examples"] = [_valid_protein_example()]
        record_file = tmp_path / "recipe_with_protein.yaml"
        record_file.write_text(yaml.safe_dump(recipe, sort_keys=False), encoding="utf-8")

        cfg_path = tmp_path / "id_label_targets.yaml"
        cfg_path.write_text(
            yaml.safe_dump(
                {
                    "adapters": {},
                    "ignored_prefixes": ignored,
                    "synonym_scope": "exact_related",
                    "targets": [
                        {
                            "name": "test_recipe",
                            "kind": "yaml",
                            "glob": "recipe_with_protein.yaml",
                            "required": True,
                            "policy": "canonical",
                            "pairs": [["id", "label"]],
                        }
                    ],
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        assert validate_id_label_correspondence.run(cfg_path, report_path=None) == 0

    def test_validate_protein_examples_cli(self, tmp_path: Path) -> None:
        valid_recipe = _base_recipe()
        valid_recipe["protein_examples"] = [_valid_protein_example()]
        valid_file = tmp_path / "valid.yaml"
        valid_file.write_text(yaml.safe_dump(valid_recipe, sort_keys=False), encoding="utf-8")

        tsv_out = tmp_path / "out.tsv"
        assert (
            validate_protein_examples.main(
                ["--paths", str(valid_file), "--require-examples", "--out", str(tsv_out)]
            )
            == 0
        )
        assert tsv_out.is_file()

        invalid_recipe = _base_recipe()
        invalid_recipe["protein_examples"] = [_valid_protein_example(uniprot_id="UniProtKB:BAD")]
        invalid_file = tmp_path / "invalid.yaml"
        invalid_file.write_text(yaml.safe_dump(invalid_recipe, sort_keys=False), encoding="utf-8")
        assert (
            validate_protein_examples.main(["--paths", str(invalid_file), "--out", str(tsv_out)])
            == 1
        )
        assert "UniProtKB:BAD" in tsv_out.read_text(encoding="utf-8")
