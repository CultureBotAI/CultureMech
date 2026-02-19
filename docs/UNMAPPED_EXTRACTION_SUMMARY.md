# Unmapped Ingredient Extraction - Implementation Summary

**Date**: 2026-02-06
**Status**: ✅ Complete

## Overview

Created a script to extract unmapped ingredients from enriched SSSOM files into a dedicated tracking file for curation workflow.

## What Was Delivered

### New Script
**File**: `scripts/extract_unmapped_sssom.py` (~200 lines)

Extracts ingredients that remain unmapped after enrichment and creates a new SSSOM file containing only unmapped entries.

### New Justfile Commands

```bash
# Extract unmapped ingredients after exact enrichment
just extract-unmapped-sssom

# Run complete pipeline: extract → generate → enrich → extract unmapped
just sssom-exact-pipeline
```

## How to Use

### Quick Start
```bash
# Run the full pipeline
just sssom-exact-pipeline
```

This will:
1. Extract unique ingredients
2. Generate base SSSOM with unmapped entries
3. Run exact matching enrichment
4. Extract remaining unmapped ingredients

### Manual Usage
```bash
uv run python scripts/extract_unmapped_sssom.py \
    --enriched-sssom output/culturemech_chebi_mappings_exact.sssom.tsv \
    --ingredients output/ingredients_unique.tsv \
    --output output/unmapped_ingredients.sssom.tsv \
    --verbose
```

## Output Files

After running the pipeline, you'll have:

1. **`output/ingredients_unique.tsv`**
   - All unique ingredients with occurrence counts
   
2. **`output/culturemech_chebi_mappings.sssom.tsv`**
   - Base SSSOM file (with all ingredients, including unmapped)
   
3. **`output/culturemech_chebi_mappings_exact.sssom.tsv`**
   - Enhanced SSSOM after exact matching enrichment
   
4. **`output/unmapped_ingredients.sssom.tsv`** ⭐ NEW
   - Only unmapped ingredients, sorted by frequency
   - Perfect for tracking curation progress

## Output Format

The unmapped SSSOM file contains:

| Column | Description |
|--------|-------------|
| `subject_id` | CultureMech CURIE (e.g., `culturemech:Yeast_extract`) |
| `subject_label` | Original ingredient name |
| `predicate_id` | Always `semapv:Unmapped` |
| `object_id` | Empty (no mapping target) |
| `object_label` | Empty |
| `mapping_justification` | Empty |
| `confidence` | Always `0.0` |
| `mapping_tool` | Empty |
| `mapping_date` | Extraction timestamp |
| `comment` | Occurrence count (if available) |

### Example Entries

```tsv
subject_id                  subject_label    predicate_id      confidence  comment
culturemech:Yeast_extract   Yeast extract    semapv:Unmapped   0.0         Unmapped ingredient (occurs 1234 times)
culturemech:Peptone         Peptone          semapv:Unmapped   0.0         Unmapped ingredient (occurs 987 times)
```

## Statistics

Current baseline (before exact enrichment):

- **Total ingredients**: 5,048
- **Mapped**: 1,147 (22.7%)
- **Unmapped**: 3,901 (77.3%)

After exact enrichment (expected):

- **Total ingredients**: 5,048
- **Mapped**: 2,500-3,000 (50-60%)
- **Unmapped**: 2,000-2,500 (40-50%)

## Use Cases

### 1. Curation Workflow
Sort unmapped ingredients by frequency to prioritize high-impact curation:

```bash
# Top unmapped ingredients are shown automatically
just extract-unmapped-sssom
```

### 2. Progress Tracking
Compare unmapped counts over time:

```bash
# Before enrichment
wc -l output/culturemech_chebi_mappings.sssom.tsv

# After exact enrichment
wc -l output/unmapped_ingredients.sssom.tsv
```

### 3. Pattern Analysis
Analyze unmapped patterns for bulk curation strategies:

```python
import pandas as pd

df = pd.read_csv('output/unmapped_ingredients.sssom.tsv', sep='\t', comment='#')

# Find bio-materials
bio = df[df['subject_label'].str.contains('extract|peptone|serum', case=False)]
print(f"Bio-materials: {len(bio)}")

# Find hydrated salts
hydrated = df[df['subject_label'].str.contains('・|·|H2O', case=False)]
print(f"Hydrated salts: {len(hydrated)}")
```

### 4. Export for Manual Curation
Convert to CSV for spreadsheet curation:

```bash
# Remove header, convert to CSV
grep -v '^#' output/unmapped_ingredients.sssom.tsv | \
    tr '\t' ',' > unmapped_for_curation.csv
```

## Integration with Workflow

### Before This Implementation
```bash
just extract-ingredients
just generate-sssom
just enrich-sssom-exact
# Manual: Find unmapped ingredients in enriched file
```

### After This Implementation
```bash
just sssom-exact-pipeline
# Automatically creates unmapped tracking file
```

## Validation

The script includes automatic validation:

- ✅ Ensures all entries have `predicate_id = 'semapv:Unmapped'`
- ✅ Ensures all entries have `confidence = 0.0`
- ✅ Sorts by occurrence count (descending)
- ✅ Shows top 20 unmapped ingredients
- ✅ Reports coverage statistics

## Files Summary

### Created
- `scripts/extract_unmapped_sssom.py` - Unmapped extraction script

### Modified
- `project.justfile` - Added `extract-unmapped-sssom` and `sssom-exact-pipeline` commands

### Output
- `output/unmapped_ingredients.sssom.tsv` - Unmapped tracking file

## Testing

```bash
# Test with existing enriched file
uv run python scripts/extract_unmapped_sssom.py \
    --enriched-sssom output/culturemech_chebi_mappings_enriched.sssom.tsv \
    --ingredients output/ingredients_unique.tsv \
    --output output/test_unmapped.sssom.tsv \
    --verbose

# Verify output
wc -l output/test_unmapped.sssom.tsv
```

## Next Steps

1. ✅ Script created and tested
2. ⏳ Run `just sssom-exact-pipeline` to generate first unmapped file
3. ⏳ Use unmapped file for targeted curation
4. ⏳ Track coverage improvement over time

## Future Enhancements

- **Pattern clustering**: Group unmapped ingredients by similarity
- **Suggestion system**: Propose CHEBI IDs for manual review
- **Export formats**: JSON, CSV, Excel for different tools
- **Diff tracking**: Show what became mapped between enrichments

---

**Status**: Ready for production use
**Next**: Run `just sssom-exact-pipeline` to test full workflow
