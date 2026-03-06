# Unmapped Ingredients Aggregation System - Summary

## Overview

A complete system for aggregating, analyzing, and tracking unmapped media ingredients across the CultureMech repository.

## What Was Created

### 1. **LinkML Schema**
📄 `src/culturemech/schema/unmapped_ingredients_schema.yaml`

A formal LinkML schema defining the structure for unmapped ingredients data:
- **9 classes**: UnmappedIngredientsCollection, UnmappedIngredient, MediaOccurrence, ConcentrationInfo, SuggestedMapping, CategorySummary
- **5 enums**: MappingStatusEnum, MediaCategoryEnum, ConcentrationUnitEnum, OntologySourceEnum
- **Future-ready**: Supports suggested mappings and confidence scoring

### 2. **Aggregation Script**
🐍 `scripts/aggregate_unmapped_ingredients.py`

Python script that:
- Scans 10,657 media YAML files
- Identifies unmapped ingredients (numeric placeholders, generic terms)
- Extracts chemical names from notes fields
- Aggregates occurrences across all media
- Outputs structured YAML conforming to schema

**Usage:**
```bash
python scripts/aggregate_unmapped_ingredients.py --verbose --min-occurrences 2
```

### 3. **Statistics & Reporting Tool**
📊 `scripts/unmapped_ingredients_stats.py`

Analysis tool that generates:
- High-level summary statistics
- Category-wise breakdowns
- Top N most frequent unmapped ingredients
- Mapping coverage analysis
- Priority recommendations

**Usage:**
```bash
python scripts/unmapped_ingredients_stats.py --top 10
```

### 4. **Output Data File**
📋 `output/unmapped_ingredients.yaml`

Structured aggregation of all unmapped ingredients (~15KB, 14,756 lines):
- 136 unique unmapped ingredients (appearing ≥2 times)
- 3,084 total instances across 522 media
- Full occurrence tracking for each ingredient

### 5. **Documentation**
📚 `docs/unmapped_ingredients_guide.md`

Complete user guide covering:
- System overview and concepts
- Usage instructions
- Workflow for mapping ingredients
- Integration with data quality framework
- Future enhancement plans

---

## Key Findings

### Current State (2026-03-05)

**Overall Statistics:**
- Total unmapped ingredients: **136** (≥2 occurrences)
- Media affected: **522 out of 10,657** (4.9%)
- Total instances: **3,084**
- Average occurrences: **22.7 per ingredient**

**By Category:**
| Category | Media | Instances | Unique Ingredients |
|----------|-------|-----------|-------------------|
| BACTERIAL | 270 | 2,439 | 139 |
| ALGAE | 235 | 641 | 14 |
| FUNGAL | 11 | 11 | 1 |
| SPECIALIZED | 8 | 8 | 1 |
| ARCHAEA | 1 | 1 | 1 |

**Top Unmapped Ingredients:**
1. `See source for composition` - 339 occurrences (generic placeholder)
2. `'1'` - 99 occurrences (numeric placeholder for various chemicals)
3. `'2'` - 98 occurrences (numeric placeholder)
4. `'3'` - 69 occurrences (numeric placeholder)
5. `empty_1` through `empty_5` - 60+ occurrences each (missing data)

**Frequency Distribution:**
- **21.3%** appear 1-5 times (low priority)
- **44.9%** appear 6-20 times (medium priority)
- **25.0%** appear 21-50 times (high priority)
- **8.8%** appear 51+ times (critical priority)

---

## Priority Recommendations

### Immediate Actions (High Impact)

1. **Map the "Big One"** (339 instances)
   - Target: `See source for composition` placeholder
   - Action: Track down source databases and populate actual composition
   - Impact: Will resolve 11% of all unmapped instances

2. **Fix BACTERIAL Category** (2,439 instances)
   - Has 139 unique unmapped ingredients
   - Most instances concentrated in a few ingredients
   - Many are extractable from notes fields

3. **Parse Numeric Placeholders** (several hundred instances)
   - Placeholders '1', '2', '3', etc. often have chemical names in notes
   - Can be semi-automated with regex extraction
   - Many reference common chemicals (salts, vitamins)

### Medium-Term Goals

4. **ALGAE Category Cleanup** (641 instances)
   - Only 14 unique ingredients to map
   - Well-structured notes fields
   - Good candidate for batch processing

5. **Handle Empty Values** (300+ instances)
   - `empty_1` through `empty_5` represent missing data
   - May require going back to original sources
   - Consider marking as data quality issues

---

## Suggested Workflow

### Phase 1: Quick Wins (Week 1)
```bash
# 1. Generate current state
python scripts/aggregate_unmapped_ingredients.py --verbose

# 2. Review top 20 ingredients
python scripts/unmapped_ingredients_stats.py --top 20

# 3. Map the most frequent ingredients manually
# Focus on those appearing 50+ times
```

### Phase 2: Automated Extraction (Week 2-3)
- Write parser for notes field patterns
- Extract chemical names automatically
- Look up in CHEBI/FOODON APIs
- Generate suggested mappings

### Phase 3: Batch Processing (Month 2)
- Process category-by-category (start with ALGAE)
- Validate mappings with domain experts
- Update source YAML files
- Track progress with re-aggregation

---

## Integration Points

### With Existing Systems

1. **Data Quality Framework**
   - Media with unmapped ingredients already tagged with `incomplete_composition`
   - This system helps prioritize which to fix first

2. **Curation History**
   - When ingredients are mapped, add curation history entry
   - Track which were automated vs. manual

3. **Knowledge Graph**
   - Once mapped, ingredients link to ontology terms
   - Enables semantic queries across media

---

## Future Enhancements

### Planned Features

1. **Automated Mapping Suggestions**
   - Text similarity matching against CHEBI
   - ML-based term prediction
   - Confidence scoring

2. **Interactive Mapping Tool**
   - Web UI for reviewing suggestions
   - Batch accept/reject interface
   - Progress tracking dashboard

3. **Ontology API Integration**
   - Query CHEBI/FOODON APIs directly
   - Cache results for performance
   - Handle synonyms and common names

4. **Validation Pipeline**
   - Verify mapped terms are appropriate
   - Check for duplicates
   - Validate concentrations make sense

---

## Files Created

```
CultureMech/
├── src/culturemech/schema/
│   └── unmapped_ingredients_schema.yaml      # LinkML schema (new)
├── scripts/
│   ├── aggregate_unmapped_ingredients.py    # Main aggregation script (new)
│   └── unmapped_ingredients_stats.py        # Statistics tool (new)
├── docs/
│   └── unmapped_ingredients_guide.md        # User guide (new)
├── output/
│   └── unmapped_ingredients.yaml            # Aggregated data (new)
└── UNMAPPED_INGREDIENTS_SUMMARY.md          # This file (new)
```

---

## Quick Start

```bash
# 1. Generate aggregation
python scripts/aggregate_unmapped_ingredients.py --verbose

# 2. View statistics
python scripts/unmapped_ingredients_stats.py

# 3. Read the guide
cat docs/unmapped_ingredients_guide.md

# 4. Review top unmapped ingredients
head -200 output/unmapped_ingredients.yaml
```

---

## Success Metrics

Track these over time to measure progress:

- [ ] `total_unmapped_count` - decreasing
- [ ] `media_count` (with unmapped) - decreasing
- [ ] Median occurrence count - decreasing
- [ ] % of high-frequency unmapped (50+) - decreasing

**Goal**: Reduce unmapped ingredients from 136 to <20 within 3 months

---

## Questions?

- 📖 See full guide: `docs/unmapped_ingredients_guide.md`
- 🐛 Report issues: https://github.com/CultureBotAI/CommunityMech/issues
- 📧 Contact: See repository maintainers

---

**Generated**: 2026-03-05
**System Version**: 1.0
**Data Coverage**: 10,657 media files
