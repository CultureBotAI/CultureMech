# Tracking Unmapped Ingredients in SSSOM

## Overview

The SSSOM pipeline can now include **unmapped ingredients** (those without CHEBI IDs) as mapping candidates for future curation. This allows you to track which ingredients need ontology mappings and prioritize curation efforts.

## Usage

### Generate SSSOM with Unmapped Ingredients

```bash
# Include unmapped ingredients
just generate-sssom true

# Or use the full pipeline
just sssom-with-unmapped
```

### Generate SSSOM without Unmapped Ingredients (Default)

```bash
# Only mapped ingredients (default)
just generate-sssom

# Or
just sssom-pipeline
```

## SSSOM Format for Unmapped Ingredients

### Metadata Header

The SSSOM file includes vocabulary for unmapped terms:

```yaml
# Predicates:
#   - skos:exactMatch (mapped ingredients)
#   - semapv:Unmapped (no mapping found)
#
# Justifications:
#   - semapv:ManualMappingCuration (curated mappings)
#   - semapv:Unreviewed (not yet reviewed for mapping)
```

### Mapped Entry Example

```tsv
subject_id                    subject_label    predicate_id        object_id      confidence
culturemech:Distilled_water   Distilled water  skos:exactMatch     CHEBI:15377    0.95
```

### Unmapped Entry Example

```tsv
subject_id                    subject_label           predicate_id      object_id  confidence  comment
culturemech:Yeast_extract     Yeast extract          semapv:Unmapped              0.0         Unmapped ingredient (appears in 523 recipes) - candidate for future curation
```

## Key Fields for Unmapped Ingredients

| Field | Value | Purpose |
|-------|-------|---------|
| `subject_id` | `culturemech:Ingredient_Name` | Unique identifier for ingredient |
| `subject_label` | `Ingredient name` | Human-readable name |
| `predicate_id` | `semapv:Unmapped` | Indicates no mapping exists |
| `object_id` | `` (empty) | No CHEBI term assigned |
| `object_label` | `` (empty) | No label available |
| `mapping_justification` | `semapv:Unreviewed` | Not yet reviewed |
| `confidence` | `0.0` | Zero confidence (no mapping) |
| `mapping_tool` | `CultureMech\|unmapped_detection` | Detected as unmapped |
| `comment` | Frequency and context | How many recipes use this ingredient |

## Current Statistics (After Invalid ID Cleanup)

```
Total unique ingredients: 4,575
  - Mapped:   1,024 (22.4%)
  - Unmapped: 3,664 (77.6%)

CHEBI terms used: 514
```

## Use Cases

### 1. Prioritize Manual Curation

Filter unmapped ingredients by frequency to focus on high-impact mappings:

```python
import pandas as pd

# Load SSSOM file
df = pd.read_csv('output/culturemech_chebi_mappings.sssom.tsv',
                 sep='\t', comment='#')

# Get unmapped ingredients
unmapped = df[df['confidence'] == 0.0]

# Extract frequency from comment
unmapped['frequency'] = unmapped['comment'].str.extract(r'appears in (\d+) recipes')
unmapped['frequency'] = unmapped['frequency'].astype(int)

# Sort by frequency
priority = unmapped.sort_values('frequency', ascending=False)

# Top 20 candidates for curation
print(priority[['subject_label', 'frequency']].head(20))
```

**Output:**
```
subject_label                    frequency
Tryptone (BD-Difco)              99
Fetal bovine serum               94
MnCl2 x 4 H2O                    93
Na-resazurin solution (0.1%)     92
Nickel chloride                  92
Sea Salt                         90
...
```

### 2. Export Curation Work List

Create a spreadsheet for manual curation:

```python
# Export unmapped to CSV for curation
unmapped[['subject_label', 'frequency']].to_csv(
    'unmapped_curation_list.csv',
    index=False
)
```

### 3. Filter for OLS Discovery

Focus on unmapped ingredients for automated OLS search:

```python
# Get list of unmapped ingredient names for OLS search
unmapped_names = unmapped['subject_label'].tolist()

# Use with enrich_sssom_with_ols.py
# The enrichment script will automatically attempt to find mappings
```

### 4. Track Curation Progress

Compare before/after curation:

```python
# Before curation
before = df[df['confidence'] == 0.0]
print(f"Unmapped before: {len(before)}")

# After adding mappings
after = df[df['confidence'] > 0.0]
print(f"Mapped after: {len(after)}")
print(f"Coverage: {len(after)/len(df)*100:.1f}%")
```

## Top Unmapped Ingredients

Based on current data (appears in >90 recipes):

| Ingredient | Recipes | Notes |
|------------|---------|-------|
| Tryptone (BD-Difco) | 99 | Complex peptone - may need NCIT term |
| Fetal bovine serum | 94 | Complex mixture - may need NCIT term |
| MnCl2 x 4 H2O | 93 | Should map to CHEBI (hydrated form) |
| Na-resazurin solution | 92 | Solution/mixture - may need special handling |
| Nickel chloride | 92 | Should map to CHEBI |
| Sea Salt | 90 | Complex mixture - may need NCIT term |

## Integration with OLS Enrichment

When you run the OLS enrichment with unmapped ingredients included:

```bash
just sssom-with-unmapped
```

The pipeline will:
1. ✅ **Generate SSSOM** with 4,688 entries (1,024 mapped + 3,664 unmapped)
2. ✅ **Verify mapped entries** via OLS API (1,024 verifications)
3. ✅ **Search for unmapped entries** via OLS API (3,664 searches)
4. ✅ **Produce enriched SSSOM** with newly discovered mappings

### Expected Enrichment Results

- **Verified mappings**: ~1,020 (95%+ of existing mappings)
- **New OLS discoveries**: ~500-1,000 additional mappings (confidence 0.5-0.9)
- **Still unmapped**: ~2,500-3,100 ingredients (candidates for manual curation)
- **Final coverage**: ~35-45% (up from 22%)

## Workflow: From Unmapped to Mapped

### Step 1: Generate SSSOM with Unmapped

```bash
just generate-sssom true
```

### Step 2: Review Top Candidates

```bash
# Check top unmapped ingredients
grep "semapv:Unmapped" output/culturemech_chebi_mappings.sssom.tsv | \
  sort -t$'\t' -k9 -rn | head -20
```

### Step 3: OLS Discovery

```bash
# Attempt automated discovery
just enrich-sssom-with-ols
```

### Step 4: Manual Curation

For ingredients that OLS can't find:
1. Search CHEBI manually: https://www.ebi.ac.uk/chebi/
2. Consider other ontologies (NCIT for complex mixtures)
3. Update source mapping files
4. Re-run enrichment

### Step 5: Track Progress

```python
# Compare versions
before = pd.read_csv('output/culturemech_chebi_mappings.sssom.tsv',
                     sep='\t', comment='#')
after = pd.read_csv('output/culturemech_chebi_mappings_enriched.sssom.tsv',
                    sep='\t', comment='#')

print(f"Mapped before: {len(before[before['confidence'] > 0])}")
print(f"Mapped after:  {len(after[after['confidence'] > 0])}")
print(f"New mappings:  {len(after[after['confidence'] > 0]) - len(before[before['confidence'] > 0])}")
```

## Benefits

### 1. Complete Inventory
- Track **all** ingredients, not just mapped ones
- Know exactly what needs curation

### 2. Prioritization
- Focus on high-frequency ingredients first
- Maximize impact of curation efforts

### 3. Progress Tracking
- Measure curation coverage over time
- Identify gaps in ontology mappings

### 4. Transparency
- Document what is known vs unknown
- Show data quality metrics

### 5. Collaboration
- Share curation work lists with team
- Assign ingredients to curators

## Commands Reference

```bash
# Generate with unmapped ingredients
just generate-sssom true

# Generate without unmapped (default)
just generate-sssom

# Full pipeline with unmapped
just sssom-with-unmapped

# Full pipeline without unmapped (default)
just sssom-pipeline

# Check unmapped count
grep "semapv:Unmapped" output/*.sssom.tsv | wc -l
```

## SSSOM Vocabulary

### Predicates
- **skos:exactMatch** - Exact correspondence between ingredient and CHEBI term
- **skos:closeMatch** - Close correspondence (from OLS discovery)
- **semapv:Unmapped** - No mapping exists (NEW)

### Justifications
- **semapv:ManualMappingCuration** - Curated from trusted sources
- **semapv:LexicalMatching** - Found via OLS lexical search
- **semapv:Unreviewed** - Not yet reviewed for mapping (NEW)

### Confidence Scores
- **1.0** - Verified by OLS
- **0.95** - Curated from MicrobeMediaParam/MediaDive
- **0.5-0.9** - OLS discovery (quality varies)
- **0.0** - No mapping (unmapped ingredient)

## Future Enhancements

1. **Automated Batch Curation**
   - Process top unmapped ingredients automatically
   - Use ML to suggest likely mappings

2. **Multi-Ontology Support**
   - Map complex ingredients to NCIT, FoodOn
   - Support multiple ontologies per ingredient

3. **Interactive Curation UI**
   - Web interface for reviewing unmapped ingredients
   - Bulk approve/reject OLS suggestions

4. **Curation Tracking**
   - Track who curated each mapping
   - Record curation date and confidence

## References

- **SSSOM Spec**: https://mapping-commons.github.io/sssom/
- **SEMAPV Vocabulary**: https://w3id.org/semapv/vocab/
- **CHEBI Ontology**: https://www.ebi.ac.uk/chebi/
- **NCIT Ontology**: https://ncithesaurus.nci.nih.gov/

---

**Status**: ✅ Implemented
**Date**: February 6, 2026
**Coverage**: 22.4% mapped, 77.6% tracked as unmapped candidates
