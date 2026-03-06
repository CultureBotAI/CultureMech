# Unmapped Ingredients Aggregation Guide

## Overview

This guide describes the system for aggregating and tracking unmapped media ingredients that need ontology term mapping.

## What are Unmapped Ingredients?

Unmapped ingredients are media components that lack proper ontology term mappings in the `preferred_term` field. They are identified by:

- **Numeric placeholders**: '1', '2', '3', etc.
- **Generic placeholders**: 'See source for composition', 'variable', etc.
- **Empty values**: Missing or blank `preferred_term` fields

## Components

### 1. LinkML Schema

**Location**: `src/culturemech/schema/unmapped_ingredients_schema.yaml`

Defines the structured format for aggregated unmapped ingredients with the following key classes:

- `UnmappedIngredientsCollection`: Root container with metadata and summaries
- `UnmappedIngredient`: Individual unmapped ingredient with occurrences and parsed info
- `MediaOccurrence`: Reference to specific media containing the ingredient
- `ConcentrationInfo`: Concentration data for ingredients
- `SuggestedMapping`: Future ontology term suggestions
- `CategorySummary`: Statistics by media category

### 2. Aggregation Script

**Location**: `scripts/aggregate_unmapped_ingredients.py`

Python script that:
- Scans all media YAML files in `data/normalized_yaml/`
- Identifies unmapped ingredients
- Extracts chemical names from notes fields
- Aggregates occurrences across media
- Generates structured YAML output

### 3. Output File

**Location**: `output/unmapped_ingredients.yaml`

Structured YAML file conforming to the schema, containing:
- Generation timestamp
- Total counts and statistics
- Detailed unmapped ingredient entries
- Category-wise summaries

## Usage

### Basic Usage

```bash
# Generate unmapped ingredients aggregation
python scripts/aggregate_unmapped_ingredients.py

# With custom options
python scripts/aggregate_unmapped_ingredients.py \
    --output output/unmapped_ingredients.yaml \
    --input-dir data/normalized_yaml \
    --min-occurrences 2 \
    --verbose
```

### Options

- `--output PATH`: Output file path (default: `output/unmapped_ingredients.yaml`)
- `--input-dir PATH`: Input directory with media YAML files (default: `data/normalized_yaml`)
- `--min-occurrences N`: Only include ingredients appearing at least N times (default: 1)
- `--verbose`: Enable verbose logging

### Example Output Structure

```yaml
generation_date: '2026-03-05T23:04:00.677404'
total_unmapped_count: 136
media_count: 522
unmapped_ingredients:
- placeholder_id: '1'
  raw_ingredient_text:
  - 'Original amount: NaNO3(Fisher BP360-500)'
  parsed_chemical_name: NaNO3
  occurrence_count: 243
  media_occurrences:
  - medium_name: BG-11 Medium
    medium_category: ALGAE
    medium_file_path: normalized_yaml/algae/BG-11_Medium.yaml
    ingredient_index: 0
  concentration_info:
  - value: variable
    unit: G_PER_L
  mapping_status: UNMAPPED

summary_by_category:
- category: ALGAE
  media_with_unmapped: 235
  total_unmapped_instances: 641
  unique_unmapped_count: 14
- category: BACTERIAL
  media_with_unmapped: 270
  total_unmapped_instances: 2439
  unique_unmapped_count: 139
```

## Current Statistics (as of 2026-03-05)

- **Total unmapped ingredients**: 136 (appearing ≥2 times)
- **Media with unmapped ingredients**: 522 out of 10,657 total
- **Breakdown by category**:
  - ALGAE: 235 media, 641 instances, 14 unique
  - BACTERIAL: 270 media, 2,439 instances, 139 unique
  - FUNGAL: 11 media, 11 instances, 1 unique
  - SPECIALIZED: 8 media, 8 instances, 1 unique
  - ARCHAEA: 1 medium, 1 instance, 1 unique

## Workflow for Mapping

### 1. Generate Current Aggregation

```bash
python scripts/aggregate_unmapped_ingredients.py --verbose
```

### 2. Review Unmapped Ingredients

Open `output/unmapped_ingredients.yaml` and review:
- Most frequent unmapped ingredients (sorted by occurrence_count)
- Parsed chemical names extracted from notes
- Media where each ingredient appears

### 3. Map to Ontology Terms

For each unmapped ingredient:

1. **Identify the chemical**: Use `parsed_chemical_name` and `raw_ingredient_text`
2. **Search ontologies**: Look in CHEBI, FOODON, or other appropriate ontologies
3. **Update media files**: Replace numeric placeholder with proper ontology term
4. **Verify**: Re-run aggregation to confirm mapping

Example mapping in media YAML:

```yaml
# Before (unmapped)
ingredients:
- preferred_term: '1'
  concentration:
    value: 1.5
    unit: G_PER_L
  notes: 'Original amount: NaNO3'

# After (mapped)
ingredients:
- preferred_term: sodium nitrate
  term:
    id: CHEBI:63041
    label: sodium nitrate
  concentration:
    value: 1.5
    unit: G_PER_L
  notes: 'Original amount: NaNO3'
```

### 4. Track Progress

Re-run the aggregation periodically to track progress:

```bash
# Check progress
python scripts/aggregate_unmapped_ingredients.py --verbose

# Compare counts over time
diff previous_unmapped.yaml output/unmapped_ingredients.yaml
```

## Integration with Data Quality

The unmapped ingredients system integrates with the existing data quality framework:

- Media with unmapped ingredients are tagged with `incomplete_composition` flag
- The aggregation helps prioritize mapping efforts
- Statistics guide resource allocation for curation

## Future Enhancements

Planned improvements:

1. **Automated mapping suggestions**: Use text matching and ML to suggest CHEBI/FOODON terms
2. **Batch mapping tool**: UI/CLI tool to map multiple ingredients at once
3. **Confidence scoring**: Score mapping suggestions based on string similarity
4. **Integration with ontology APIs**: Query CHEBI/FOODON APIs for candidate terms
5. **Tracking system**: Monitor mapping progress over time with metrics

## Support

For questions or issues:
- File an issue: https://github.com/CultureBotAI/CommunityMech/issues
- See main README: `README.md`
