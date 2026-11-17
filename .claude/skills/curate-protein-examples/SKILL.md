---
name: curate-protein-examples
description: Curate and validate typed, evidence-backed UniProtKB protein examples (ProteinExample / UniProtTerm) on CultureMech growth-media records in data/normalized_yaml/. Use when adding, reviewing, or repairing organism-scoped UniProt protein examples on MediaRecipe, OrganismDescriptor, CofactorDescriptor, CofactorRequirement, or TransporterAnnotation.
version: 1.0.0
---

# Curate Protein Examples (`curate-protein-examples`)

Curate typed, evidence-backed `UniProtKB:` protein examples (`ProteinExample`) on CultureMech growth-media records in `data/normalized_yaml/`.

## Scope & Ownership Rules

1. **Authoritative input layer**: Write only to `data/normalized_yaml/` via `scripts/apply_protein_examples.py` (which uses `src/culturemech/validation/write_validated.py` and appends a `curation_history` event). Never edit `data/merge_yaml/`, `app/`, `pages/`, or `output/kgx/` directly.
2. **Exact organism and accession grounding**:
   - `uniprot_term.id` MUST be a canonical `UniProtKB:` accession matching `^UniProtKB:([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})$`.
   - `uniprot_term.label` MUST be the protein recommended name or entry label (non-empty).
   - `organism_term.id` MUST be an explicit `NCBITaxon:` CURIE whose `organism_term.label` matches the canonical NCBI Taxonomy scientific name (verified by `scripts/validate_id_label_correspondence.py`).
   - When a `ProteinExample` is nested under `target_organisms[i]` or `target_organisms[i].cofactor_requirements[j]`, `organism_term.id` must match the enclosing `target_organisms[i].term.id` unless `notes` explicitly documents the strain-vs-species or closely related taxon relationship.
3. **Claim-level evidence required**:
   - Every `ProteinExample` MUST carry at least one `EvidenceItem` in `evidence` with `supports: SUPPORT` or `supports: PARTIAL`.
   - Each `EvidenceItem` MUST include a valid `reference` (`PMID:...` or `DOI:...`), a non-empty verbatim `snippet` from the paper/source, and a non-empty `explanation` tying the protein accession, organism taxon, and medium/cofactor/substrate role together.
   - Never fabricate `UniProtKB:` accessions, `NCBITaxon:` IDs, `PMID:`/`DOI:` citations, or quote snippets.

## Schema Structure (`src/culturemech/schema/culturemech.yaml`)

`protein_examples` (`multivalued: true`, `range: ProteinExample`) can be attached at:
- `MediaRecipe.protein_examples` (target path: `protein_examples`)
- `OrganismDescriptor.protein_examples` (target path: `target_organisms[i].protein_examples`)
- `CofactorRequirement.protein_examples` (target path: `target_organisms[i].cofactor_requirements[j].protein_examples`)
- `CofactorDescriptor.protein_examples` (target path: `cofactors[i].protein_examples`)
- `TransporterAnnotation.protein_examples` (target path: `transporters[i].protein_examples`)

### Example `ProteinExample` Entry

```yaml
uniprot_term:
  id: UniProtKB:P02931
  label: Outer membrane porin F
organism_term:
  id: NCBITaxon:562
  label: Escherichia coli
gene_symbol: ompF
locus_tag: b0929
ec_number: EC:1.14.13.25
sequence_scope: Swiss-Prot reviewed entry for E. coli K-12 OmpF porin
functional_role: Outer membrane diffusion porin facilitating passive nutrient uptake in minimal and complex media
substrate_term:
  id: CHEBI:17234
  label: D-glucose
evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    snippet: "OmpF forms general diffusion pores in the outer membrane of Escherichia coli."
    explanation: "Demonstrates OmpF (UniProtKB:P02931) function in Escherichia coli (NCBITaxon:562)."
```

## Workflow

### Step 1: Prepare Proposal Payload

Create a YAML/JSON proposal file listing each target record and attachment scope (`recipe`, `organism`, `cofactor_requirement`, or `transporter`):

```yaml
proposals:
  - recipe_id: CultureMech:001645
    target_scope: organism
    organism_taxon_id: NCBITaxon:414
    source_note: PMID:2113044 sMMO curation
    protein_example:
      uniprot_term:
        id: UniProtKB:P22868
        label: Methane monooxygenase component A alpha chain
      organism_term:
        id: NCBITaxon:414
        label: Methylococcus capsulatus
      gene_symbol: mmoX
      ec_number: EC:1.14.13.25
      functional_role: Particulate/soluble methane oxidation in NMS medium
      cofactor_term:
        id: CHEBI:18248
        label: iron atom
      evidence:
        - reference: PMID:2113044
          supports: SUPPORT
          snippet: "The nucleotide sequence of the mmoX gene encoding the alpha subunit of the hydroxylase component of soluble methane monooxygenase from Methylococcus capsulatus (Bath)."
          explanation: "Establishes Methylococcus capsulatus (NCBITaxon:414) sMMO hydroxylase alpha subunit mmoX (UniProtKB:P22868)."
```

### Step 2: Dry-Run and Apply via Maintained Writer

Always run `scripts/apply_protein_examples.py` in `--dry-run` mode first:

```bash
just apply-protein-examples <proposals.yaml> data/normalized_yaml --dry-run
```

Once dry-run validation passes with zero errors, apply the changes:

```bash
just apply-protein-examples <proposals.yaml> data/normalized_yaml --apply
```

### Step 3: Run Validation Gates

Verify schema, semantic protein-example rules, and ontology ID-label correspondence:

```bash
just validate-protein-examples data/normalized_yaml
.venv/bin/python scripts/validate_strict.py <record.yaml>
.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
```

### Step 4: Downstream KGX Export Behavior

`src/culturemech/export/kgx_export.py` automatically exports curated `protein_examples` as:
- `biolink:Protein` nodes keyed by `UniProtKB:...` accession and labeled by `uniprot_term.label`
- `Medium -> biolink:related_to -> Protein` edges (`relationship_type=protein_example`)
- `Protein -> biolink:in_taxon -> Organism` edges (`NCBITaxon:...`)
- `Protein -> biolink:interacts_with -> Cofactor/Substrate` edges (`CHEBI:...`)
All emitted edges carry the curated `publications` and `functional_role` qualifiers. See `tests/test_protein_examples.py` for unit test coverage.
