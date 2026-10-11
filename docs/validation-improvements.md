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

`just validate-references`, the reference phase of `just validate`, and the
layered strict validator now call `scripts/validate_recipe_references.py`.
The wrapper retains the upstream LinkML plugin's schema-driven traversal and
literature-reference handling. For these exact HTTPS endpoints it instead uses
literal official-recipe checks:

- TOGO `sparqlist/api/gmdb_medium_by_gmid?gm_id=M...`
- JCM `cgi-bin/jcm/jcm_grmd?GRMD=...`
- MediaDive `rest/medium/...` and `rest/solution/...`
- MediaDB `mediadb.systemsbiology.net/defined_media/media/<positive integer>/`
- DSMZ `microorganisms/medium/pdf/DSMZ_Medium....pdf`
- KOMODO `(komodo/)servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=...`

These checks verify the returned accession, preserve brackets, chemical case,
hydrate digits, signs, decimals and units, and fold only presentation whitespace.
JCM table cells are separated while inline chemical subscripts stay attached.
Recipe API titles come from their metadata; an invented descriptive title does
not pass merely because the accession matches. Official-source errors never
fall back to fuzzy matching or skipped-prefix success.

KOMODO detail pages require the exact accession and medium heading, one feature
table, one five-column ingredient table and the provider's per-liter statement.
Matching preserves displayed amounts, nulls and inline chemical digits; it does
not interpret the Gram/Mol columns as sufficient evidence for serum density or
other conversions. Duplicate/ambiguous rows, hidden content and changed table
shapes fail closed. Calculated SEED ion totals and unrelated page text are not
included in the recipe matching text. Unsupported page shapes require review.

MediaDB requires matching title/heading and self-accession link, one compound
table with its stated row count, and the exact `Amount (mM)` header. A quote must
match within one title, header, or ingredient row; text from separate rows is
not concatenated into evidence. `None` is preserved, not converted to zero.
Duplicate compounds, malformed amounts/cells, and hidden or inert recipe content
fail closed. Other page prose is excluded. Database-table agreement does not
verify the original article's formulation. MediaDB SQL-export URLs still use the
upstream route; this adapter does not waive missing export metadata.

Raw responses are cached separately under
`references_cache/official-recipes-v1/`, with URL, timestamp and SHA256 integrity
checks. Old generic Markdown captures are not reused. Corrupt caches fail closed;
refresh them explicitly:

```bash
uv run python scripts/validate_recipe_references.py path/to/record.yaml --refresh
uv run python scripts/validate_recipe_references.py path/to/record.yaml --json
```

Use `--cache-dir` or `--config` for a different cache/configuration. The JSON
output includes successful and failed checks, unlike the upstream CLI's count
of issues. MediaRecipe versus SolutionRecipe is inferred unless
`--target-class` is supplied. Reference occurrence checks do not establish
scientific entailment, completeness, stock scope, chemical identity, or correct
concentration arithmetic. Missing snippets still need the separate ingredient
review; zero reference checks is not proof that a record is fully evidenced.

Other references, including `PMID:12345678` and `doi:10.1038/...`, retain the
upstream validator's configured retrieval, normalization and matching behavior.
There is no blanket exemption for historical or non-PMID references: unresolved
sources must be reported according to that configuration. The LinkML plugin
checks populated excerpt/reference pairs and separately checks bibliography
titles where present.

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
