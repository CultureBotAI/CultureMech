"""Focused positive and negative unit tests for CultureMech causal_graphs (#658)."""

from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import apply_causal_graphs  # noqa: E402
import validate_causal_graphs  # noqa: E402
import validate_strict  # noqa: E402

from culturemech.export.kgx_export import (  # noqa: E402
    _QUALIFIER_COLUMNS,
    PROTEIN,
    causal_edge_to_edges,
    nodes,
    to_edge,
    transform,
)
from culturemech.validation.causal_graphs import (  # noqa: E402
    validate_causal_edge_entry,
    validate_recipe_causal_graphs,
)
from culturemech.validation.write_validated import (  # noqa: E402
    LayerBoundaryError,
    validate_recipe,
    write_validated_recipe,
)


def _valid_causal_edge(
    *,
    edge_id: str = "edge_cobalamin_enables_growth",
    subject_id: str = "CHEBI:17439",
    subject_label: str = "cyanocobal(III)alamin",
    predicate: str = "ENABLES_GROWTH",
    object_id: str = "NCBITaxon:83333",
    object_label: str = "Escherichia coli K-12",
    organism_id: str | None = "NCBITaxon:83333",
    organism_label: str = "Escherichia coli K-12",
    protein_terms: list[dict[str, str]] | None = None,
    condition_context: str | None = "Aerobic minimal medium lacking L-methionine at 37 C",
    supports: str = "SUPPORT",
    reference: str = "PMID:12345678",
    snippet: str = (
        "Exogenous cyanocobalamin transported via BtuB enables cobalamin-dependent "
        "growth of E. coli K-12 metE mutants in minimal medium."
    ),
    explanation: str = (
        "Cyanocobalamin supplementation causally rescues growth in minimal medium via BtuB."
    ),
    notes: str | None = None,
) -> dict[str, Any]:
    edge: dict[str, Any] = {
        "id": edge_id,
        "subject_term": {"id": subject_id, "label": subject_label},
        "predicate": predicate,
        "object_term": {"id": object_id, "label": object_label},
        "evidence": [
            {
                "reference": reference,
                "supports": supports,
                "snippet": snippet,
                "explanation": explanation,
            }
        ],
    }
    if organism_id is not None:
        edge["organism_term"] = {"id": organism_id, "label": organism_label}
    if protein_terms is not None:
        edge["protein_terms"] = protein_terms
    if condition_context is not None:
        edge["condition_context"] = condition_context
    if notes is not None:
        edge["notes"] = notes
    return edge


def _minimal_recipe() -> dict[str, Any]:
    return {
        "id": "CultureMech:000001",
        "name": "Test Minimal Medium",
        "medium_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            {
                "preferred_term": "D-glucose",
                "term": {"id": "CHEBI:17634", "label": "D-glucose"},
                "concentration": {"value": "10", "unit": "G_PER_L"},
            }
        ],
        "target_organisms": [
            {
                "preferred_term": "Escherichia coli K-12",
                "term": {"id": "NCBITaxon:83333", "label": "Escherichia coli K-12"},
            }
        ],
    }


def test_valid_causal_graphs_pass_linkml_and_semantic_validation() -> None:
    recipe = _minimal_recipe()
    recipe["causal_graphs"] = [
        _valid_causal_edge(
            edge_id="edge_cobalamin_enables_growth",
            protein_terms=[{"id": "UniProtKB:P06129", "label": "Vitamin B12 transporter BtuB"}],
        )
    ]
    recipe["target_organisms"][0]["causal_graphs"] = [
        _valid_causal_edge(
            edge_id="CausalEdge:glucose_pos_reg_growth",
            subject_id="CHEBI:17634",
            subject_label="D-glucose",
            predicate="POSITIVELY_REGULATES",
            object_id="GO:0040007",
            object_label="growth",
            organism_id="NCBITaxon:83333",
            organism_label="Escherichia coli K-12",
            protein_terms=[
                {
                    "id": "UniProtKB:P69786",
                    "label": "PTS system glucose-specific EIICB component",
                }
            ],
        )
    ]

    assert validate_recipe_causal_graphs(recipe) == []
    assert validate_recipe(recipe) == []


@pytest.mark.parametrize(
    ("bad_id", "expected_rule"),
    [
        ("", "INVALID_CAUSAL_EDGE_ID"),
        ("causal_1", "INVALID_CAUSAL_EDGE_ID"),
        ("CHEBI:17439", "INVALID_CAUSAL_EDGE_ID"),
        ("edge with spaces", "INVALID_CAUSAL_EDGE_ID"),
    ],
)
def test_rejects_invalid_causal_edge_id(bad_id: str, expected_rule: str) -> None:
    edge = _valid_causal_edge(edge_id=bad_id)
    issues = validate_causal_edge_entry(edge, "causal_graphs[0]")
    assert any(i.rule == expected_rule for i in issues)


@pytest.mark.parametrize(
    ("bad_term_id", "expected_rule"),
    [
        ("CARBON_SOURCE", "UNGROUNDED_CAUSAL_ROLE_TOKEN"),
        ("BUFFER", "UNGROUNDED_CAUSAL_ROLE_TOKEN"),
        ("CHEBI:CARBON_SOURCE", "UNGROUNDED_CAUSAL_ROLE_TOKEN"),
        ("UNKNOWN:12345", "INVALID_CAUSAL_TERM_ID"),
        ("CHEBI:0", "INVALID_CAUSAL_TERM_ID"),
        ("GO:123", "INVALID_CAUSAL_TERM_ID"),
        ("CultureMech:000000", "INVALID_CAUSAL_TERM_ID"),
    ],
)
def test_rejects_ungrounded_role_tokens_and_invalid_term_curies(
    bad_term_id: str, expected_rule: str
) -> None:
    edge = _valid_causal_edge(subject_id=bad_term_id)
    issues = validate_causal_edge_entry(edge, "causal_graphs[0]")
    assert any(i.rule == expected_rule for i in issues)


def test_rejects_empty_causal_term_label_and_self_loop() -> None:
    edge = _valid_causal_edge(
        subject_id="CHEBI:17439",
        subject_label="",
        object_id="CHEBI:17439",
        object_label="cyanocobal(III)alamin",
    )
    issues = validate_causal_edge_entry(edge, "causal_graphs[0]")
    rules = {i.rule for i in issues}
    assert "EMPTY_CAUSAL_TERM_LABEL" in rules
    assert "SELF_LOOP_CAUSAL_EDGE" in rules


def test_rejects_invalid_predicate() -> None:
    edge = _valid_causal_edge(predicate="STIMULATES")
    issues = validate_causal_edge_entry(edge, "causal_graphs[0]")
    assert any(i.rule == "INVALID_CAUSAL_PREDICATE" for i in issues)


def test_organism_term_and_enclosing_taxon_consistency() -> None:
    # Missing organism_term when nested under target_organisms
    missing_org = _valid_causal_edge(organism_id=None)
    issues_missing = validate_causal_edge_entry(
        missing_org,
        "target_organisms[0].causal_graphs[0]",
        enclosing_organism_id="NCBITaxon:83333",
    )
    assert any(i.rule == "MISSING_ORGANISM_TERM" for i in issues_missing)

    # Mismatched organism_term without explanatory notes fails
    mismatch = _valid_causal_edge(
        organism_id="NCBITaxon:562",
        organism_label="Escherichia coli",
    )
    issues_mismatch = validate_causal_edge_entry(
        mismatch,
        "target_organisms[0].causal_graphs[0]",
        enclosing_organism_id="NCBITaxon:83333",
    )
    assert any(i.rule == "ORGANISM_CONTEXT_MISMATCH" for i in issues_mismatch)

    # Mismatched organism_term WITH explanatory notes passes
    explained = _valid_causal_edge(
        organism_id="NCBITaxon:562",
        organism_label="Escherichia coli",
        notes="Species-level causal evidence applies to strain K-12 (NCBITaxon:83333).",
    )
    assert (
        validate_causal_edge_entry(
            explained,
            "target_organisms[0].causal_graphs[0]",
            enclosing_organism_id="NCBITaxon:83333",
        )
        == []
    )


def test_rejects_invalid_or_duplicate_protein_terms() -> None:
    edge = _valid_causal_edge(
        protein_terms=[
            {"id": "UniProtKB:P06129-1", "label": "Isoform not allowed"},
            {"id": "UniProtKB:P06129", "label": "Vitamin B12 transporter BtuB"},
            {"id": "UniProtKB:P06129", "label": ""},
        ]
    )
    issues = validate_causal_edge_entry(edge, "causal_graphs[0]")
    rules = {i.rule for i in issues}
    assert "INVALID_UNIPROT_ACCESSION" in rules
    assert "DUPLICATE_PROTEIN_TERM" in rules
    assert "EMPTY_UNIPROT_LABEL" in rules


@pytest.mark.parametrize(
    ("mutator", "expected_rule"),
    [
        (lambda e: e.update({"evidence": []}), "MISSING_EVIDENCE"),
        (
            lambda e: e["evidence"][0].update({"reference": "PMID:abc"}),
            "INVALID_EVIDENCE_REFERENCE",
        ),
        (
            lambda e: e["evidence"][0].update({"supports": "REFUTE"}),
            "UNSUPPORTED_CAUSAL_EDGE",
        ),
        (
            lambda e: e["evidence"][0].update({"supports": "MAYBE"}),
            "INVALID_EVIDENCE_SUPPORTS",
        ),
        (
            lambda e: e["evidence"][0].update({"snippet": "   "}),
            "MISSING_EVIDENCE_SNIPPET",
        ),
        (
            lambda e: e["evidence"][0].update({"explanation": ""}),
            "MISSING_EVIDENCE_EXPLANATION",
        ),
    ],
)
def test_rejects_invalid_or_unsupported_evidence(mutator: Any, expected_rule: str) -> None:
    edge = _valid_causal_edge()
    mutator(edge)
    issues = validate_causal_edge_entry(edge, "causal_graphs[0]")
    assert any(i.rule == expected_rule for i in issues)


def test_rejects_duplicate_causal_edge_id_and_tuple() -> None:
    recipe = _minimal_recipe()
    e1 = _valid_causal_edge(edge_id="edge_dup")
    e2 = _valid_causal_edge(edge_id="edge_dup")
    recipe["causal_graphs"] = [e1, e2]

    issues = validate_recipe_causal_graphs(recipe)
    rules = {i.rule for i in issues}
    assert "DUPLICATE_CAUSAL_EDGE_ID" in rules
    assert "DUPLICATE_CAUSAL_EDGE" in rules


def test_validate_causal_graphs_cli(tmp_path: Path) -> None:
    norm_dir = tmp_path / "data" / "normalized_yaml" / "bacterial"
    norm_dir.mkdir(parents=True)
    valid_path = norm_dir / "valid_recipe.yaml"
    recipe = _minimal_recipe()
    recipe["causal_graphs"] = [_valid_causal_edge()]
    write_validated_recipe(recipe, valid_path)

    assert validate_causal_graphs.main([str(valid_path)]) == 0
    assert validate_strict.validate_one(valid_path) == []

    invalid_path = norm_dir / "invalid_recipe.yaml"
    bad_recipe = copy.deepcopy(recipe)
    bad_recipe["causal_graphs"][0]["subject_term"]["id"] = "CARBON_SOURCE"
    invalid_path.write_text(yaml.safe_dump(bad_recipe, sort_keys=False), encoding="utf-8")

    assert validate_causal_graphs.main([str(invalid_path)]) == 1
    strict_rows = validate_strict.validate_one(invalid_path)
    assert any(r["category"] == "UNGROUNDED_CAUSAL_ROLE_TOKEN" for r in strict_rows)


def test_apply_causal_graphs_writer_dry_run_apply_idempotency_and_layer_guard(
    tmp_path: Path,
) -> None:
    norm_dir = tmp_path / "data" / "normalized_yaml" / "bacterial"
    norm_dir.mkdir(parents=True)
    recipe_path = norm_dir / "test_medium.yaml"
    base_recipe = _minimal_recipe()
    write_validated_recipe(base_recipe, recipe_path)
    original_bytes = recipe_path.read_bytes()

    batch_path = tmp_path / "batch.yaml"
    batch_payload = {
        "proposals": [
            {
                "recipe_id": "CultureMech:000001",
                "target_scope": "recipe",
                "source_note": "PMID:12345678 cobalamin causal mechanism curation",
                "causal_edge": _valid_causal_edge(
                    edge_id="edge_cobalamin_enables_growth",
                    protein_terms=[
                        {
                            "id": "UniProtKB:P06129",
                            "label": "Vitamin B12 transporter BtuB",
                        }
                    ],
                ),
            },
            {
                "recipe_id": "CultureMech:000001",
                "target_scope": "organism",
                "organism_taxon_id": "NCBITaxon:83333",
                "source_note": "PMID:12345678 glucose growth regulation curation",
                "causal_edge": _valid_causal_edge(
                    edge_id="edge_glucose_regulates_growth",
                    subject_id="CHEBI:17634",
                    subject_label="D-glucose",
                    predicate="POSITIVELY_REGULATES",
                    object_id="GO:0040007",
                    object_label="growth",
                ),
            },
        ]
    }
    batch_path.write_text(yaml.safe_dump(batch_payload, sort_keys=False), encoding="utf-8")

    # 1. Default --dry-run does not modify file on disk
    rc_dry = apply_causal_graphs.main([str(batch_path), "--yaml-dir", str(norm_dir), "--dry-run"])
    assert rc_dry == 0
    assert recipe_path.read_bytes() == original_bytes

    # 2. --apply writes validated causal_graphs and appends curation_history
    rc_apply = apply_causal_graphs.main([str(batch_path), "--yaml-dir", str(norm_dir), "--apply"])
    assert rc_apply == 0
    updated = yaml.safe_load(recipe_path.read_text(encoding="utf-8"))
    assert len(updated["causal_graphs"]) == 1
    assert updated["causal_graphs"][0]["id"] == "edge_cobalamin_enables_growth"
    assert len(updated["target_organisms"][0]["causal_graphs"]) == 1
    assert (
        updated["target_organisms"][0]["causal_graphs"][0]["id"] == "edge_glucose_regulates_growth"
    )
    assert len(updated.get("curation_history") or []) == 1
    event = updated["curation_history"][-1]
    assert event["curator"] == "apply_causal_graphs.py"
    assert event["action"] == "ANNOTATED"
    assert "edge_cobalamin_enables_growth" in event["changes"]
    assert "edge_glucose_regulates_growth" in event["changes"]

    # 3. Re-running --apply is idempotent (0 touched, 0 written, no extra history event)
    touched, written = apply_causal_graphs.apply_proposals_to_directory(
        batch_payload["proposals"],
        norm_dir,
        dry_run=False,
    )
    assert (touched, written) == (0, 0)
    reloaded = yaml.safe_load(recipe_path.read_text(encoding="utf-8"))
    assert len(reloaded["curation_history"]) == 1

    # 4. Refuses to write to merge_yaml or outside normalized_yaml
    merge_dir = tmp_path / "data" / "merge_yaml" / "merged"
    merge_dir.mkdir(parents=True)
    with pytest.raises(LayerBoundaryError):
        apply_causal_graphs.apply_proposals_to_directory(
            batch_payload["proposals"],
            merge_dir,
            dry_run=False,
        )

    # 5. Rejects invalid proposal without modifying file
    bad_batch = tmp_path / "bad_batch.yaml"
    bad_edge = _valid_causal_edge(edge_id="edge_bad", subject_id="CARBON_SOURCE")
    bad_batch.write_text(
        yaml.safe_dump(
            {
                "proposals": [
                    {
                        "recipe_id": "CultureMech:000001",
                        "target_scope": "recipe",
                        "causal_edge": bad_edge,
                    }
                ]
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    applied_bytes = recipe_path.read_bytes()
    with pytest.raises(ValueError, match="Invalid CausalEdge"):
        apply_causal_graphs.main([str(bad_batch), "--yaml-dir", str(norm_dir), "--apply"])
    assert recipe_path.read_bytes() == applied_bytes


def test_kgx_export_for_causal_graphs() -> None:
    recipe = _minimal_recipe()
    recipe["causal_graphs"] = [
        _valid_causal_edge(
            edge_id="edge_cobalamin_enables_growth",
            subject_id="CHEBI:17439",
            subject_label="cyanocobal(III)alamin",
            predicate="ENABLES_GROWTH",
            object_id="GO:0040007",
            object_label="growth",
            organism_id="NCBITaxon:83333",
            organism_label="Escherichia coli K-12",
            protein_terms=[{"id": "UniProtKB:P06129", "label": "Vitamin B12 transporter BtuB"}],
            condition_context="Minimal medium lacking methionine",
        )
    ]

    emitted_nodes = list(nodes(recipe))
    protein_nodes = [n for n in emitted_nodes if n["id"] == "UniProtKB:P06129"]
    assert len(protein_nodes) == 1
    assert protein_nodes[0]["category"] == [PROTEIN]
    assert protein_nodes[0]["name"] == "Vitamin B12 transporter BtuB"

    causal_edges = list(causal_edge_to_edges("CultureMech:000001", recipe["causal_graphs"][0]))
    triples = {(e["subject"], e["predicate"], e["object"]) for e in causal_edges}
    assert ("CHEBI:17439", "biolink:positively_regulates", "GO:0040007") in triples
    assert ("CultureMech:000001", "biolink:related_to", "CHEBI:17439") in triples
    assert ("CHEBI:17439", "biolink:affects", "NCBITaxon:83333") in triples
    assert ("CHEBI:17439", "biolink:interacts_with", "UniProtKB:P06129") in triples
    assert ("UniProtKB:P06129", "biolink:in_taxon", "NCBITaxon:83333") in triples

    all_edges = list(transform(recipe))
    for edge_dict in all_edges:
        for qual in edge_dict.get("qualifiers") or []:
            assert qual["qualifier_type_id"] in _QUALIFIER_COLUMNS
        edge_row = to_edge(edge_dict)
        if edge_dict["subject"] == "CHEBI:17439" and edge_dict["object"] == "GO:0040007":
            assert edge_row.relationship_type == "causal_edge:ENABLES_GROWTH"
            assert edge_row.role == "Minimal medium lacking methionine"
            assert edge_row.publications == ["PMID:12345678"]


def test_id_label_targets_and_oak_config_cover_causal_graph_prefixes() -> None:
    repo_root = Path(__file__).resolve().parent.parent
    targets = yaml.safe_load(
        (repo_root / "conf" / "id_label_targets.yaml").read_text(encoding="utf-8")
    )
    oak_cfg = yaml.safe_load((repo_root / "conf" / "oak_config.yaml").read_text(encoding="utf-8"))
    ignored = set(targets.get("ignored_prefixes") or [])
    adapters = set((oak_cfg.get("ontology_adapters") or {}).keys())

    for prefix in ("GO", "RO", "METPO", "PATO", "EC", "KEGG", "UniProtKB", "CausalEdge"):
        assert prefix in ignored
        assert prefix in adapters


def test_apply_causal_graphs_organism_scope_fallback_and_dedup(tmp_path: Path) -> None:
    yaml_dir = tmp_path / "data" / "normalized_yaml" / "bacterial"
    yaml_dir.mkdir(parents=True)
    recipe_path = yaml_dir / "test_multi_org_recipe.yaml"
    recipe = _minimal_recipe()
    recipe["target_organisms"] = [
        {
            "preferred_term": "Bacillus subtilis",
            "term": {"id": "NCBITaxon:1423", "label": "Bacillus subtilis"},
        },
        {
            "preferred_term": "Escherichia coli K-12",
            "term": {"id": "NCBITaxon:83333", "label": "Escherichia coli K-12"},
        },
    ]
    recipe_path.write_text(yaml.safe_dump(recipe, sort_keys=False), encoding="utf-8")

    # 1. Organism-scoped proposal omitting organism_taxon_id resolves via causal_edge.organism_term.id
    #    to target_organisms[1] (NCBITaxon:83333), not target_organisms[0].
    proposals_fallback = [
        {
            "recipe_id": "CultureMech:000001",
            "target_scope": "organism",
            "source_note": "PMID:12345678 organism fallback test",
            "causal_edge": _valid_causal_edge(edge_id="CausalEdge:glucose_pos_reg_growth"),
        }
    ]
    touched, written = apply_causal_graphs.apply_proposals_to_directory(
        proposals_fallback, yaml_dir, dry_run=False
    )
    assert (touched, written) == (1, 1)

    reloaded = yaml.safe_load(recipe_path.read_text(encoding="utf-8"))
    assert "causal_graphs" not in reloaded["target_organisms"][0]
    assert len(reloaded["target_organisms"][1]["causal_graphs"]) == 1
    assert (
        reloaded["target_organisms"][1]["causal_graphs"][0]["id"]
        == "CausalEdge:glucose_pos_reg_growth"
    )

    # 2. Deduplication matches when a second proposal has a different id but identical
    #    (subject, predicate, object, organism) tuple, and _dedup_append also treats an
    #    existing entry without organism_term as inheriting enclosing_org.
    same_tuple_edge = _valid_causal_edge(edge_id="edge_different_id_same_tuple")
    proposals_dedup = [
        {
            "recipe_id": "CultureMech:000001",
            "target_scope": "organism",
            "organism_taxon_id": "NCBITaxon:83333",
            "causal_edge": same_tuple_edge,
        }
    ]
    touched2, written2 = apply_causal_graphs.apply_proposals_to_directory(
        proposals_dedup, yaml_dir, dry_run=False
    )
    assert (touched2, written2) == (0, 0)

    inherited_existing = _valid_causal_edge(edge_id="edge_inherited_org", organism_id=None)
    bucket_with_inherited = [inherited_existing]
    assert (
        apply_causal_graphs._dedup_append(
            bucket_with_inherited,
            same_tuple_edge,
            enclosing_org="NCBITaxon:83333",
        )
        is False
    )

    # 3. Organism-scoped proposal omitting both organism_taxon_id and causal_edge.organism_term.id fails.
    proposals_missing_both = [
        {
            "recipe_id": "CultureMech:000001",
            "target_scope": "organism",
            "causal_edge": inherited_existing,
        }
    ]
    with pytest.raises(
        ValueError,
        match="requires 'organism_taxon_id' or 'causal_edge.organism_term.id'",
    ):
        apply_causal_graphs.apply_proposals_to_directory(
            proposals_missing_both, yaml_dir, dry_run=True
        )
