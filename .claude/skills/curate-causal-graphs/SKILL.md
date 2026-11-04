---
name: curate-causal-graphs
description: Curate and validate typed, evidence-backed growth-media causal mechanism edges (CausalEdge / CausalTerm / CausalPredicateEnum) on CultureMech records in data/normalized_yaml/. Use when adding, reviewing, or repairing medium-to-organism causal relationships on MediaRecipe or OrganismDescriptor; not for static ingredient-role diagrams or intracellular metabolic pathways owned by PathwayMech/EnzymeMech.
version: 1.0.0
---

# Curate Growth-Media Causal Graphs (`curate-causal-graphs`)

Curate typed, evidence-backed growth-media causal mechanism edges (`CausalEdge`) on CultureMech records in `data/normalized_yaml/`.

## Domain & Ownership Boundary Decision (#658)

1. **CultureMech-owned growth-media causal mechanisms (in scope)**:
   - Directed, literature-supported causal relationships demonstrating how a medium ingredient, stock solution, cofactor, medium perturbation, or strain modification in a specific growth medium causally supports, limits, regulates, or alters organism growth, survival, substrate transport, cofactor provisioning, or physiological state (`ENABLES_GROWTH`, `INHIBITS_GROWTH`, `PROVIDES_COFACTOR_FOR`, `TRANSPORTS_SUBSTRATE`, `POSITIVELY_REGULATES`, `NEGATIVELY_REGULATES`, `CAUSES`, `AFFECTS`).
2. **Static composition and ingredient-role diagrams (out of scope for `causal_graphs`)**:
   - Bipartite medium/ingredient/role diagrams rendered by `scripts/render_media_role_graph.py` from `nutritional_roles`, `physicochemical_roles`, and `cellular_metabolic_roles` represent static formulation roles (`CARBON_SOURCE`, `BUFFER`, `MINERAL_SOURCE`), not directed causal mechanism edges. Bare role tokens are rejected by `src/culturemech/validation/causal_graphs.py`.
3. **Intracellular pathway and enzyme reaction graphs owned by sibling Mechs (out of scope)**:
   - Multi-step intracellular metabolic pathway topologies (`PathwayMech`), catalytic reaction stoichiometries (`EnzymeMech`), and medium-independent chemical role assertions (`MediaIngredientMech`) belong to their respective sibling repositories and must not be duplicated as `CausalEdge` items unless the cited publication directly establishes a medium-specific growth, transport, cofactor, or perturbation causal effect.

## Scope & Validation Rules

1. **Authoritative input layer**: Write only to `data/normalized_yaml/` via `scripts/apply_causal_graphs.py` (which validates via `src/culturemech/validation/write_validated.py` and appends a `curation_history` event). Never edit `data/merge_yaml/`, `app/`, `pages/`, or `output/kgx/` directly.
2. **Ontology-grounded causal endpoints**:
   - `id` MUST be a unique non-empty edge identifier within the record matching `^(edge_[A-Za-z0-9_.-]+|CausalEdge:[A-Za-z0-9_.-]+)$` (e.g., `edge_methane_enables_growth`).
   - `subject_term` and `object_term` MUST be `CausalTerm` mappings (`id` + non-empty `label`) using an allowed CURIE prefix (`CHEBI`, `NCBITaxon`, `GO`, `UniProtKB`, `EC`, `KEGG`, `METPO`, `ENVO`, `PATO`, `NCIT`, `FOODON`, `UBERON`, `MICRO`, `CultureMech`, `MediaIngredientMech`).
   - Self-loops (`subject_term.id == object_term.id`) and bare ingredient-role enum tokens (`CARBON_SOURCE`, `BUFFER`, etc.) are rejected.
   - For ontologies with local OAK SQLite adapters (`CHEBI`, `NCBITaxon`, `ENVO`, `UBERON`, `NCIT`, `FOODON`), `label` MUST match the canonical ontology label (verified by `scripts/validate_id_label_correspondence.py`).
3. **Organism and protein scoping**:
   - When `organism_term` is provided, `organism_term.id` MUST be a valid `NCBITaxon:` CURIE with its canonical NCBI Taxonomy scientific name.
   - When a `CausalEdge` is nested under `target_organisms[i].causal_graphs`, `organism_term.id` (if present) must match `target_organisms[i].term.id` unless `notes` explicitly explains the strain-vs-species or community relationship.
   - Optional `protein_terms` MUST be canonical `UniProtKB:` accessions (`UniProtTerm`).
4. **Claim-level evidence required**:
   - Every `CausalEdge` MUST carry at least one `EvidenceItem` in `evidence` with `supports: SUPPORT` or `supports: PARTIAL`.
   - Each `EvidenceItem` MUST include a valid `reference` (`PMID:...` or `DOI:...`), a non-empty verbatim `snippet` from the source publication, and a non-empty `explanation` connecting the subject, causal predicate, object, and medium context.
   - Never fabricate ontology IDs, `UniProtKB:` accessions, `PMID:`/`DOI:` citations, or quote snippets.

## Schema Structure (`src/culturemech/schema/culturemech.yaml`)

`causal_graphs` (`multivalued: true`, `range: CausalEdge`) can be attached at:
- `MediaRecipe.causal_graphs` (`target_scope: recipe`)
- `OrganismDescriptor.causal_graphs` (`target_scope: organism`, matched by `organism_taxon_id`)

### Example `CausalEdge` Entry

```yaml
id: edge_methane_enables_growth
subject_term:
  id: CHEBI:16183
  label: methane
predicate: ENABLES_GROWTH
object_term:
  id: NCBITaxon:414
  label: Methylococcus capsulatus
organism_term:
  id: NCBITaxon:414
  label: Methylococcus capsulatus
protein_terms:
  - id: UniProtKB:P22868
    label: Methane monooxygenase component A alpha chain
condition_context: Aerobic growth in Nitrate Mineral Salts (NMS) medium with methane headspace
evidence:
  - reference: PMID:2113044
    supports: SUPPORT
    snippet: "Methylococcus capsulatus (Bath) oxidizes methane to methanol via soluble methane monooxygenase during growth on methane as sole carbon and energy source."
    explanation: "Establishes that methane (CHEBI:16183) causally enables growth of Methylococcus capsulatus (NCBITaxon:414) in NMS medium via sMMO (UniProtKB:P22868)."
```

## Workflow

### Step 1: Prepare Proposal Payload

Create a YAML batch file listing each target record and attachment scope (`recipe` or `organism`):

```yaml
proposals:
  - recipe_id: CultureMech:001645
    target_scope: organism
    organism_taxon_id: NCBITaxon:414
    source_note: PMID:2113044 methane growth mechanism in NMS medium
    causal_edge:
      id: edge_methane_enables_growth
      subject_term:
        id: CHEBI:16183
        label: methane
      predicate: ENABLES_GROWTH
      object_term:
        id: NCBITaxon:414
        label: Methylococcus capsulatus
      organism_term:
        id: NCBITaxon:414
        label: Methylococcus capsulatus
      protein_terms:
        - id: UniProtKB:P22868
          label: Methane monooxygenase component A alpha chain
      condition_context: Aerobic growth in Nitrate Mineral Salts (NMS) medium
      evidence:
        - reference: PMID:2113044
          supports: SUPPORT
          snippet: "Methylococcus capsulatus (Bath) oxidizes methane to methanol via soluble methane monooxygenase."
          explanation: "Demonstrates causal growth support by methane (CHEBI:16183) for M. capsulatus (NCBITaxon:414) via sMMO (UniProtKB:P22868)."
```

### Step 2: Dry-Run and Apply via Maintained Writer

Always run `scripts/apply_causal_graphs.py` in `--dry-run` mode first:

```bash
just apply-causal-graphs <proposals.yaml> data/normalized_yaml --dry-run
```

Once dry-run validation passes with zero errors, apply the changes:

```bash
just apply-causal-graphs <proposals.yaml> data/normalized_yaml --apply
```

### Step 3: Run Validation Gates

Verify schema, semantic causal-graph rules, and ontology ID-label correspondence:

```bash
just validate-causal-graphs data/normalized_yaml
.venv/bin/python scripts/validate_strict.py <record.yaml>
.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
```

### Step 4: Downstream KGX Export Behavior

`src/culturemech/export/kgx_export.py` automatically exports curated `causal_graphs` as:
- `Subject -> biolink:<predicate> -> Object` edges (`relationship_type=causal_edge:<PREDICATE>`)
- `Medium -> biolink:related_to -> Subject` edges (`relationship_type=causal_mechanism_component`)
- `Subject -> biolink:affects -> Organism` edges (`relationship_type=causal_edge_organism_context`, when organism is distinct from subject/object)
- `Subject -> biolink:interacts_with -> Protein` edges (`relationship_type=causal_edge_protein_mediator`) and `biolink:Protein` nodes for any `protein_terms`
All emitted edges carry the curated `publications` and `condition_context` qualifiers. See `tests/test_causal_graphs.py` for unit test coverage.
