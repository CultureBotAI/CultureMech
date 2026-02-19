# SSSOM Mapping Generation Pipeline

This document describes the SSSOM (Simple Standard for Sharing Ontology Mappings) pipeline for generating and enriching ingredient-to-CHEBI mappings in CultureMech.

## Overview

The SSSOM pipeline consists of three main components:

1. **Ingredient Extraction** - Extract unique ingredients from all YAML recipes
2. **SSSOM Generation** - Create SSSOM mapping file from existing CHEBI term assignments
3. **OLS Enrichment** - Verify and expand mappings using the EBI Ontology Lookup Service API

## Quick Start

Run the complete pipeline:

```bash
just sssom-pipeline
```

This will:
1. Extract unique ingredients to `output/ingredients_unique.tsv`
2. Generate base SSSOM file to `output/culturemech_chebi_mappings.sssom.tsv`
3. Enrich with OLS to `output/culturemech_chebi_mappings_enriched.sssom.tsv`

## Component 1: Ingredient Extraction

Extract all unique ingredient names from YAML recipe files with frequency and provenance tracking.

### Usage

```bash
just extract-ingredients
```

Or with custom options:

```bash
uv run python scripts/extract_unique_ingredients.py \
    --normalized-yaml data/normalized_yaml \
    --output output/ingredients_unique.tsv \
    --min-frequency 1 \
    --verbose
```

### Options

- `--normalized-yaml PATH` - Directory to scan (default: `data/normalized_yaml`)
- `--raw-yaml PATH` - Optional raw_yaml directory to include
- `--include-raw` - Include raw_yaml in scan
- `--output PATH` - Output TSV file (default: `output/ingredients_unique.tsv`)
- `--min-frequency N` - Minimum recipe count to include (default: 1)
- `--verbose` - Show progress messages

### Output Format

TSV file with columns:

| Column | Description |
|--------|-------------|
| `ingredient_name` | Unique ingredient name (from `preferred_term`) |
| `frequency` | Number of recipes using this ingredient |
| `has_chebi_mapping` | Boolean indicating CHEBI term presence |
| `chebi_id` | CHEBI CURIE (e.g., `CHEBI:15377`) or empty |
| `sources` | Pipe-separated list of data sources (e.g., `KOMODO\|TOGO\|MediaDive`) |

### Example Output

```tsv
ingredient_name	frequency	has_chebi_mapping	chebi_id	sources
Distilled water	2847	TRUE	CHEBI:15377	KOMODO|MediaDive|TOGO
Yeast extract	1923	FALSE		CCAP|KOMODO|TOGO|UTEX
NaCl	1456	TRUE	CHEBI:26710	KOMODO|MediaDive|TOGO
Agar	1234	TRUE	CHEBI:2509	CCAP|KOMODO|TOGO
```

## Component 2: SSSOM Mapping Generation

Generate SSSOM-compliant TSV file from existing CHEBI term assignments in normalized_yaml.

### Usage

```bash
just generate-sssom
```

Or with custom options:

```bash
uv run python scripts/generate_sssom_mappings.py \
    --normalized-dir data/normalized_yaml \
    --output output/culturemech_chebi_mappings.sssom.tsv \
    --validate
```

### Options

- `--normalized-dir PATH` - Input directory (default: `data/normalized_yaml`)
- `--output PATH` - Output SSSOM file (default: `output/culturemech_chebi_mappings.sssom.tsv`)
- `--confidence-threshold FLOAT` - Minimum confidence (0.0-1.0, default: 0.0)
- `--validate` - Validate SSSOM format after generation
- `--verbose` - Show progress messages

### SSSOM Format

The generated file follows [SSSOM v0.9 specification](https://mapping-commons.github.io/sssom/):

#### Metadata Header (YAML comments)

```yaml
# curie_map:
#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_
#   culturemech: https://w3id.org/culturemech/ingredient/
#   skos: http://www.w3.org/2004/02/skos/core#
#   semapv: https://w3id.org/semapv/vocab/
# mapping_set_id: https://w3id.org/culturemech/mappings/chebi/v1.0
# mapping_set_title: CultureMech to CHEBI Ingredient Mappings
# mapping_set_description: Mappings between CultureMech culture media ingredients and CHEBI chemical entity ontology terms
# license: https://creativecommons.org/publicdomain/zero/1.0/
# mapping_provider: https://github.com/KG-Hub/KG-Microbe/CultureMech
# mapping_date: 2026-02-04T12:00:00Z
```

#### TSV Columns

| Column | Description | Example |
|--------|-------------|---------|
| `subject_id` | CultureMech ingredient CURIE | `culturemech:Distilled_water` |
| `subject_label` | Human-readable ingredient name | `Distilled water` |
| `predicate_id` | Mapping relationship | `skos:exactMatch` |
| `object_id` | CHEBI term CURIE | `CHEBI:15377` |
| `object_label` | CHEBI term label | `water` |
| `mapping_justification` | Mapping method | `semapv:ManualMappingCuration` |
| `confidence` | Confidence score (0.0-1.0) | `0.95` |
| `mapping_tool` | Source tool | `MicrobeMediaParam\|v1.0` |
| `mapping_date` | ISO 8601 timestamp | `2026-02-04T12:00:00+00:00` |
| `comment` | Additional notes | `Curated from MicrobeMediaParam` |

### Mapping Predicates

- `skos:exactMatch` - Exact correspondence between ingredient name and CHEBI term
- `skos:closeMatch` - Close correspondence (used for OLS-discovered mappings)

### Mapping Justifications

- `semapv:ManualMappingCuration` - Curated from MicrobeMediaParam/MediaDive
- `semapv:LexicalMatching` - Discovered via OLS lexical search

## Component 3: EBI OLS API Integration

Verify existing CHEBI mappings and discover new mappings using the EBI Ontology Lookup Service.

### Usage

```bash
just enrich-sssom-with-ols
```

Or with custom options:

```bash
uv run python scripts/enrich_sssom_with_ols.py \
    --input-sssom output/culturemech_chebi_mappings.sssom.tsv \
    --input-ingredients output/ingredients_unique.tsv \
    --output output/culturemech_chebi_mappings_enriched.sssom.tsv \
    --rate-limit 5 \
    --verbose
```

### Options

- `--input-sssom PATH` - Input SSSOM file
- `--input-ingredients PATH` - Unique ingredient list TSV
- `--output PATH` - Output enriched SSSOM file
- `--verify-only` - Only verify existing mappings (skip search)
- `--search-threshold FLOAT` - Minimum confidence for new mappings (default: 0.8)
- `--rate-limit FLOAT` - Requests per second (default: 5.0)
- `--cache-dir PATH` - Cache directory for OLS responses
- `--verbose` - Show progress messages

### EBI OLS API

The pipeline uses the [EBI Ontology Lookup Service API v3](https://www.ebi.ac.uk/ols/docs/api):

**Endpoints:**
- Search: `https://www.ebi.ac.uk/ols/api/search`
- Term lookup: `https://www.ebi.ac.uk/ols/api/ontologies/chebi/terms/{iri}`
- Suggest: `https://www.ebi.ac.uk/ols/api/ontologies/chebi/suggest`

**Features:**
- ✅ Response caching (default: `~/.cache/culturemech/ols`)
- ✅ Rate limiting (configurable, default: 5 req/s)
- ✅ Automatic retry on failure
- ✅ Offline mode via cache

### Verification Process

For each existing CHEBI ID:
1. Convert CURIE to IRI (e.g., `CHEBI:15377` → `http://purl.obolibrary.org/obo/CHEBI_15377`)
2. Query OLS term endpoint
3. Update mapping with official metadata:
   - Official label
   - Synonyms
   - Chemical formula
   - InChI identifier
4. Set confidence to 1.0 (verified)
5. Mark invalid/deprecated IDs (confidence < 0.5)

### Discovery Process

For unmapped ingredients:
1. Search OLS with ingredient name
2. Evaluate matches by:
   - Exact label match (confidence: 0.9)
   - Synonym match (confidence: 0.85)
   - OLS relevance score (weighted)
3. Calculate final confidence score
4. Accept matches above threshold (default: 0.8)
5. Create new mapping with:
   - Predicate: `skos:closeMatch`
   - Justification: `semapv:LexicalMatching`
   - Tool: `EBI_OLS_API|v3`

### Confidence Scoring

```python
def calculate_confidence(ingredient_name, ols_match):
    base = 0.5  # Base for OLS matches

    # Boost for exact label match
    if ols_match['label'].lower() == ingredient_name.lower():
        base = 0.9

    # Boost for synonym match
    elif ingredient_name in ols_match['synonyms']:
        base = 0.85

    # Factor in OLS relevance score
    normalized_score = ols_match['score'] / 100.0
    return (base * 0.6) + (normalized_score * 0.4)
```

## Testing the OLS Client

Test OLS API connectivity:

```bash
# Test search
just test-ols-client "glucose"

# Test CHEBI ID verification
just test-ols-client
# (defaults to verifying CHEBI:15377 - water)
```

Or use the Python module directly:

```bash
# Search for ingredient
uv run python -m culturemech.ontology.ols_client --search "glucose"

# Verify CHEBI ID
uv run python -m culturemech.ontology.ols_client --verify "CHEBI:17234"

# Get suggestions
uv run python -m culturemech.ontology.ols_client --suggest "yeast extract"

# Show statistics
uv run python -m culturemech.ontology.ols_client --stats
```

## Expected Outputs

### Base SSSOM File

- **Rows**: ~3,500 mappings (existing CHEBI-grounded ingredients)
- **Confidence**: 0.95 (high confidence from curated sources)
- **Coverage**: ~33% of total ingredients

### Enriched SSSOM File

- **Rows**: ~5,000-7,000 mappings (verified + new from OLS)
- **Features**:
  - Verified existing mappings (confidence = 1.0)
  - New OLS-discovered mappings (confidence = 0.5-0.9)
  - Invalid/deprecated mappings flagged (confidence < 0.2)
- **Coverage**: ~50%+ of total ingredients (estimated)

## Integration with Existing Pipeline

### Current Enrichment

```bash
just enrich-with-chebi
```

This command uses the existing ChemicalMapper to add CHEBI terms to normalized_yaml files.

### SSSOM Pipeline (New)

```bash
just sssom-pipeline
```

This command generates standalone SSSOM mapping files for:
- FAIR ontology mapping sharing
- Integration with external tools (ROBOT, OAK, sssom-py)
- Cross-database reconciliation
- Knowledge graph construction

### Workflow Integration

```
1. Import recipes → normalized_yaml/
2. Enrich with CHEBI → normalized_yaml/ (in-place)
3. Generate SSSOM → output/ (standalone)
4. Enrich SSSOM with OLS → output/ (expanded coverage)
5. Apply back to normalized_yaml (optional - future work)
```

## Caching and Performance

### OLS Response Cache

- **Location**: `~/.cache/culturemech/ols/` (configurable)
- **Format**: JSON files with SHA256-hashed filenames
- **Persistence**: Permanent (until manual deletion)
- **Benefits**:
  - Offline development
  - Faster re-runs
  - Reduced API load

### Cache Management

```bash
# View cache statistics
uv run python -m culturemech.ontology.ols_client --stats

# Clear cache (manual)
rm -rf ~/.cache/culturemech/ols/
```

### Rate Limiting

Default: 5 requests/second (EBI OLS recommended limit)

Adjust with `--rate-limit`:

```bash
# Conservative (2 req/s)
just enrich-sssom-with-ols --rate-limit 2

# Aggressive (10 req/s) - not recommended
just enrich-sssom-with-ols --rate-limit 10
```

## Validation

### SSSOM Format Validation

```bash
# Built-in validation
uv run python scripts/generate_sssom_mappings.py --validate

# External validation (requires sssom-py)
uv pip install sssom
sssom validate output/culturemech_chebi_mappings.sssom.tsv
```

### Unit Tests

```bash
# Test OLS client
uv run pytest tests/test_ols_client.py -v

# Test SSSOM generation
uv run pytest tests/test_sssom_generation.py -v

# Test all
uv run pytest tests/ -v
```

## Troubleshooting

### Issue: OLS API timeouts

**Solution**: Reduce rate limit
```bash
just enrich-sssom-with-ols --rate-limit 2
```

### Issue: Network errors

**Solution**: Use cached data (don't clear cache)
```bash
# Cache will be used automatically if available
```

### Issue: Low match quality

**Solution**: Increase search threshold
```bash
# Only accept high-confidence matches
uv run python scripts/enrich_sssom_with_ols.py --search-threshold 0.9
```

### Issue: Missing dependencies

**Solution**: Install required packages
```bash
uv pip install requests pandas pyyaml
```

## Future Enhancements

1. **Multi-Ontology Support**
   - Extend beyond CHEBI to NCIT, UBERON for complex ingredients
   - Support for multiple ontology mappings per ingredient

2. **Interactive Review UI**
   - Web interface for manual mapping review
   - Batch approval/rejection of OLS suggestions

3. **Machine Learning**
   - Train ML model on approved mappings
   - Predict CHEBI terms for new ingredients

4. **Continuous Integration**
   - Automated SSSOM regeneration on new imports
   - OLS verification in CI pipeline

5. **Bidirectional Sync**
   - Apply enriched SSSOM mappings back to normalized_yaml
   - Maintain consistency between SSSOM and YAML files

## References

- [SSSOM Specification](https://mapping-commons.github.io/sssom/)
- [EBI OLS API Documentation](https://www.ebi.ac.uk/ols/docs/api)
- [CHEBI Ontology](https://www.ebi.ac.uk/chebi/)
- [SKOS Vocabulary](https://www.w3.org/2004/02/skos/)
- [SEMAPV Vocabulary](https://w3id.org/semapv/vocab/)

## License

CC0 1.0 Universal (Public Domain)
