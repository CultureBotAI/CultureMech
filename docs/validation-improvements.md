# Validation Infrastructure Improvements

## Summary

Integrated LinkML term and reference validators to enable automated validation of ontology terms and literature references, based on best practices from CommunityMech issues #2 and #3.

## Changes Made

### 1. Added Missing Dependencies ✅

Added two critical validation tools to `pyproject.toml`:

```toml
dependencies = [
    ...
    "linkml-term-validator>=0.1.0",  # Validates ontology term references
    "linkml-reference-validator>=0.1.0",  # Validates evidence snippets against PMIDs
]
```

**What these enable:**
- **linkml-term-validator**: Validates that ontology IDs (NCBITaxon, CHEBI, etc.) are real and labels match
- **linkml-reference-validator**: Validates that quoted snippets actually appear in cited papers

### 2. Added Schema Annotations ✅

Enhanced the schema (`src/culturemech/schema/culturemech.yaml`) with `implements` annotations:

#### EvidenceItem Class

```yaml
EvidenceItem:
  attributes:
    reference:
      implements:
        - linkml:authoritative_reference
      comments:
        - This is automatically validated by the linkml-reference-validator tool.
        - Use format PMID:12345678 or doi:10.1038/... for automatic validation.

    snippet:
      implements:
        - linkml:excerpt
      comments:
        - This is automatically validated by the linkml-reference-validator tool.
        - Must be an exact substring of the cited paper's text.
```

#### PublicationReference Class

```yaml
PublicationReference:
  attributes:
    reference:
      implements:
        - linkml:authoritative_reference
      comments:
        - Use format PMID:12345678 or doi:10.1038/... for automatic validation.
```

### 3. Removed Silent Fallbacks ✅

Updated `project.justfile` to enforce validation instead of allowing silent failures:

**Before:**
```just
uv run linkml-term-validator ... || echo "⚠ Term validation failed (may need ontologies downloaded)"
uv run linkml-reference-validator ... || echo "⚠ Reference validation skipped (optional for historical recipes)"
```

**After:**
```just
uv run linkml-term-validator ...
echo "✓ Term validation passed"

uv run linkml-reference-validator ...
echo "✓ Reference validation passed"
```

Now validation failures will properly halt the build process rather than being silently ignored.

## Validation Workflow

### Individual Validation Targets

```bash
# Schema structure validation
just validate-schema data/normalized_yaml/bacterial/some_medium.yaml

# Ontology term validation (NCBITaxon, CHEBI, etc.)
just validate-terms data/normalized_yaml/bacterial/some_medium.yaml

# Evidence reference validation (PMID snippets)
just validate-references data/normalized_yaml/bacterial/some_medium.yaml

# Run all three validators
just validate data/normalized_yaml/bacterial/some_medium.yaml
```

### Batch Validation

```bash
# Validate all recipes
just validate-all

# Full QC pipeline
just qc
```

## What Gets Validated

### Term Validation (`linkml-term-validator`)

Validates ontology term references in:
- **Ingredients**: CHEBI terms for chemical entities
- **Organisms**: NCBITaxon terms (when populated via organism curation)
- **GTDB terms**: GTDB genome identifiers (when available)
- **Media database terms**: MediaDive, DSMZ, JCM, TOGO IDs

**Checks:**
- ✅ Term ID exists in the ontology
- ✅ Label matches the official ontology label
- ✅ ID format follows CURIE pattern (e.g., `NCBITaxon:562`)

**Example validation:**
```bash
$ just validate-terms data/normalized_yaml/bacterial/CCAP_C101_S_W_Ca.yaml
✅ Validation passed
```

### Reference Validation (`linkml-reference-validator`)

Validates evidence items with PMID/DOI references:
- **Reference format**: `PMID:12345678` or `doi:10.1038/...`
- **Snippet accuracy**: Quoted text must appear in the paper

**Checks:**
- ✅ PMID/DOI resolves to a real publication
- ✅ Snippet text is an exact substring of the paper's abstract/full text
- ❌ Catches paraphrased or fabricated quotes

**When it runs:**
- Only validates `EvidenceItem` instances with both `reference` and `snippet` populated
- Skips historical recipes without PMIDs (no error)
- Creates `references_cache/` for downloaded abstracts

## Current Schema Coverage

### Term Classes with Validation

| Term Class | Prefix | Example | Validated |
|------------|--------|---------|-----------|
| `ChemicalEntityTerm` | CHEBI | `CHEBI:17234` (Glucose) | ✅ |
| `OrganismTerm` | NCBITaxon | `NCBITaxon:562` (E. coli) | ✅ |
| `GTDBTerm` | GTDB | `GTDB:GCA_000005845.2` | ✅ |
| `MediaDatabaseTerm` | mediadive.medium | `mediadive.medium:2` | ⚠️ Custom |

### Evidence Classes with Validation

| Class | Reference Field | Snippet Field | Validated |
|-------|----------------|---------------|-----------|
| `EvidenceItem` | ✅ `reference` | ✅ `snippet` | ✅ Full |
| `PublicationReference` | ✅ `reference` | N/A | ✅ Reference only |

## Benefits

### 1. Prevents Data Quality Issues

**Before validators:**
- Wrong NCBITaxon IDs could go undetected (e.g., NCBITaxon:69459 = plant, not bacterium)
- Paraphrased or fabricated quotes accepted
- Label mismatches invisible

**After validators:**
- Automatic detection of mismatched IDs/labels
- Guarantees quotes are from cited papers
- Catches copy-paste errors

### 2. Catches AI Hallucinations

When using LLMs to populate data:
- ❌ LLM invents fake NCBITaxon IDs → **Caught by term validator**
- ❌ LLM paraphrases paper quotes → **Caught by reference validator**
- ❌ LLM uses wrong PMID for quote → **Caught by reference validator**

### 3. Improves Curation Workflow

```bash
# Immediate feedback during curation
just validate data/normalized_yaml/bacterial/new_medium.yaml

# Validates:
# - Schema structure (linkml-validate)
# - Ontology terms (linkml-term-validator)
# - Evidence quotes (linkml-reference-validator)
```

## Example: Organism Curation Integration

The organism curation workflow can now benefit from validation:

```yaml
# data/normalized_yaml/bacterial/DSMZ_2_BACILLUS_PASTEURII_MEDIUM.yaml
organism_culture_type: isolate
target_organisms:
  - preferred_term: Bacillus pasteurii
    term:
      id: NCBITaxon:492670    # ← Term validator checks this exists
      label: Sporosarcina pasteurii  # ← And that label matches
```

If we had used wrong ID or mismatched label:
```bash
$ just validate-terms data/normalized_yaml/bacterial/DSMZ_2_BACILLUS_PASTEURII_MEDIUM.yaml
❌ Error: NCBITaxon:492670 label is "Sporosarcina pasteurii", not "Bacillus pasteurii"
```

## Future Enhancements

### 1. Add Bindings for Semantic Validation

Currently we validate term ID/label correctness. We could add semantic constraints:

```yaml
classes:
  OrganismDescriptor:
    attributes:
      term:
        range: OrganismTerm
        bindings:
          - binds_value_of: id
            range: BacteriaEnum  # Only allow bacterial taxa

enums:
  BacteriaEnum:
    reachable_from:
      source_ontology: obo:ncbitaxon
      source_nodes:
        - NCBITaxon:2  # Bacteria root
      relationship_types:
        - rdfs:subClassOf
```

This would **prevent using fungal or archaeal terms where bacteria are expected**.

### 2. Ingredient Semantic Validation

```yaml
classes:
  IngredientDescriptor:
    attributes:
      term:
        bindings:
          - binds_value_of: id
            range: MetaboliteEnum  # Only small molecules

enums:
  MetaboliteEnum:
    reachable_from:
      source_ontology: obo:chebi
      source_nodes:
        - CHEBI:23367  # molecular entity
      relationship_types:
        - rdfs:subClassOf
```

### 3. Evidence Quality Scoring

Track validation results:
- High quality: Schema + Terms + References all pass
- Medium quality: Schema + Terms pass, no references
- Low quality: Schema only

## Testing

All validators tested and working:

```bash
# Schema validation
$ uv run linkml-validate --schema src/culturemech/schema/culturemech.yaml \
    --target-class MediaRecipe data/normalized_yaml/bacterial/DSMZ_2_BACILLUS_PASTEURII_MEDIUM.yaml
No issues found

# Term validation
$ uv run linkml-term-validator validate-data data/normalized_yaml/bacterial/CCAP_C101_S_W_Ca.yaml \
    -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml
✅ Validation passed

# Reference validation
$ uv run linkml-reference-validator validate data data/normalized_yaml/bacterial/DSMZ_2_BACILLUS_PASTEURII_MEDIUM.yaml \
    --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe
All validations passed!
```

## Related Work

- **CommunityMech Issue #2**: Replace custom term_validator with linkml-term-validator
- **CommunityMech Issue #3**: Replace custom reference_validator with linkml-reference-validator
- **dismech**: Already uses both validators for disease knowledge base

## References

- [linkml-term-validator docs](https://linkml.io/linkml-term-validator/)
- [linkml-reference-validator docs](https://github.com/linkml/linkml-reference-validator)
- [LinkML semantic enumerations](https://linkml.io/linkml/schemas/enums.html)
- [Using ontologies as values](https://linkml.io/linkml/howtos/ontologies-as-values.html)
