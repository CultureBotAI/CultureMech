# MediaIngredientMech Enrichment

This document describes the MediaIngredientMech enrichment pipeline for linking CultureMech ingredients to MediaIngredientMech identifiers.

## Overview

The MediaIngredientMech enrichment pipeline adds `mediaingredientmech_term` fields to ingredient and solution descriptors in CultureMech recipe YAML files. This enables cross-referencing between CultureMech recipes and the MediaIngredientMech knowledge base.

## Components

### 1. MediaIngredientMechLoader (`src/culturemech/enrich/mediaingredientmech_loader.py`)

Loads and indexes ingredient data from the MediaIngredientMech repository.

**Features:**
- Clones MediaIngredientMech repository from GitHub if not provided
- Loads ingredient data from `unmapped_ingredients.yaml`
- Builds indexes for efficient matching:
  - By CHEBI ID
  - By normalized ingredient name
  - By synonyms
- Implements fuzzy matching with configurable threshold

**Matching Priority:**
1. CHEBI ID (exact match)
2. Exact name match (case-insensitive, normalized)
3. Synonym match
4. Fuzzy name match (default threshold: 0.95)

### 2. MediaIngredientMechLinker (`src/culturemech/enrich/mediaingredientmech_linker.py`)

Enriches CultureMech recipes with MediaIngredientMech identifiers.

**Features:**
- Processes ingredients at recipe level
- Processes solution composition ingredients
- Skips already-linked ingredients
- Tracks detailed statistics:
  - Files processed
  - Ingredients matched
  - Solutions with matched ingredients
  - Match method breakdown
  - Unmatched ingredients
- Adds curation history entries

### 3. CLI Script (`scripts/enrich_with_mediaingredientmech.py`)

Command-line interface for running the enrichment pipeline.

**Features:**
- Automatic repository cloning
- Category filtering
- Dry-run mode
- Limit for testing
- JSON report generation

## Usage

### Basic Usage

```bash
# Dry run on first 10 files to test
python scripts/enrich_with_mediaingredientmech.py --dry-run --limit 10

# Process all bacterial media
python scripts/enrich_with_mediaingredientmech.py --category bacterial

# Process all media with JSON report
python scripts/enrich_with_mediaingredientmech.py --report-output enrichment_report.json
```

### Advanced Usage

```bash
# Use existing MediaIngredientMech repository
python scripts/enrich_with_mediaingredientmech.py \
  --mim-repo /path/to/MediaIngredientMech

# Custom fuzzy matching threshold
python scripts/enrich_with_mediaingredientmech.py \
  --fuzzy-threshold 0.90

# Verbose logging
python scripts/enrich_with_mediaingredientmech.py \
  --verbose --dry-run --limit 5
```

### Command-Line Options

```
--yaml-dir PATH           Directory containing recipe YAML files
                         (default: data/normalized_yaml)

--mim-repo PATH          Path to existing MediaIngredientMech repository
                         (if not provided, will clone from GitHub)

--category CATEGORY      Process only specified category
                         (bacterial, fungal, archaea, algae, specialized, imported)

--limit N                Limit number of files to process (for testing)

--dry-run                Show what would be done without modifying files

--report-output PATH     Save JSON report with statistics

--fuzzy-threshold FLOAT  Fuzzy matching threshold 0.0-1.0 (default: 0.95)

--verbose                Enable verbose logging
```

## MediaIngredientMech Data Format

The pipeline expects a `unmapped_ingredients.yaml` file in the MediaIngredientMech repository with the following structure:

```yaml
- id: MediaIngredientMech:000001
  name: Glucose
  chebi_id: CHEBI:17234
  synonyms:
    - D-Glucose
    - Dextrose
    - Grape sugar

- id: MediaIngredientMech:000002
  name: Yeast Extract
  synonyms:
    - Yeast extract powder
    - YE

- id: MediaIngredientMech:000003
  name: Sodium chloride
  chebi_id: CHEBI:26710
  synonyms:
    - NaCl
    - Table salt
    - Salt
```

**Required fields:**
- `id`: MediaIngredientMech identifier (format: `MediaIngredientMech:XXXXXX`)
- `name`: Primary ingredient name

**Optional fields:**
- `chebi_id`: CHEBI identifier (with or without `CHEBI:` prefix)
- `synonyms`: List of alternative names

## Output Format

The enrichment adds `mediaingredientmech_term` fields to ingredients:

### Before:
```yaml
ingredients:
- preferred_term: Glucose
  term:
    id: CHEBI:17234
    label: glucose
  concentration:
    value: '10'
    unit: G_PER_L
```

### After:
```yaml
ingredients:
- preferred_term: Glucose
  term:
    id: CHEBI:17234
    label: glucose
  mediaingredientmech_term:
    id: MediaIngredientMech:000001
    label: Glucose
  concentration:
    value: '10'
    unit: G_PER_L
```

## Curation History

Each enriched file gets a curation history entry:

```yaml
curation_history:
- timestamp: '2026-03-13T21:45:00.000000Z'
  curator: mediaingredientmech-enrichment-v1.0
  action: Added MediaIngredientMech links
  notes: Linked ingredients to MediaIngredientMech identifiers
```

## Statistics Report

The JSON report includes:

```json
{
  "parameters": {
    "yaml_dir": "data/normalized_yaml",
    "category": "bacterial",
    "limit": null,
    "dry_run": false,
    "fuzzy_threshold": 0.95
  },
  "statistics": {
    "files_processed": 150,
    "ingredients_matched": 450,
    "solutions_matched": 25,
    "already_linked": 10,
    "no_match": 50,
    "errors": 0,
    "match_methods": {
      "chebi_id": 300,
      "exact_name": 100,
      "synonym": 40,
      "fuzzy_0.96": 10
    }
  },
  "unmatched_ingredients": [
    {
      "name": "Unknown ingredient",
      "chebi_id": "N/A"
    }
  ]
}
```

## Testing

Run the test suite:

```bash
python tests/test_mediaingredientmech_enrichment.py
```

Or use pytest:

```bash
pytest tests/test_mediaingredientmech_enrichment.py -v
```

## Dependencies

The enrichment pipeline requires:
- `rapidfuzz>=3.0.0` - Fuzzy string matching
- `pyyaml>=6.0` - YAML parsing
- Standard library: `pathlib`, `subprocess`, `tempfile`, `logging`

## Integration with CultureMech Schema

The schema has been updated to support MediaIngredientMech identifiers:

1. **IngredientDescriptor** - Added `mediaingredientmech_term` slot
2. **SolutionDescriptor** - Added `mediaingredientmech_term` slot
3. **MediaIngredientMechTerm** - New term class with pattern validation

Schema pattern: `^MediaIngredientMech:\\d{6}$`

## Best Practices

1. **Always run dry-run first** to preview changes:
   ```bash
   python scripts/enrich_with_mediaingredientmech.py --dry-run --limit 10
   ```

2. **Start with a category** for incremental enrichment:
   ```bash
   python scripts/enrich_with_mediaingredientmech.py --category bacterial
   ```

3. **Generate reports** to track unmatched ingredients:
   ```bash
   python scripts/enrich_with_mediaingredientmech.py \
     --report-output report.json
   ```

4. **Review unmatched ingredients** and add to MediaIngredientMech

5. **Re-run enrichment** after updating MediaIngredientMech data

## Troubleshooting

### Repository clone fails
- Check network connectivity
- Verify repository URL
- Use `--mim-repo` to provide local path

### No matches found
- Check MediaIngredientMech data format
- Review ingredient names and synonyms
- Adjust `--fuzzy-threshold` if needed

### Permission errors
- Ensure write access to YAML directory
- Check file permissions

## Future Enhancements

- Support for alternative data sources
- Machine learning-based matching
- Automatic synonym generation
- Batch processing optimization
- Integration with CHEBI resolver
