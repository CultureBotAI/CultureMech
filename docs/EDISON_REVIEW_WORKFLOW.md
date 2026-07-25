# Edison Deep Research Workflow for Media Review

## Overview

This guide explains how to use **Edison Scientific's Deep Research** platform to systematically review, correct, and enrich CultureMech media records.

**Edison Platform**: https://platform.edisonscientific.com/

## Pre-Analysis: Identify Priority Media

We've analyzed all 15,827 media recipes and identified those with the most critical data quality issues.

### Quality Analysis Results

**Top Issues**:
- 🔴 **Unmapped ingredients**: 9,690+ occurrences (no CHEBI IDs)
- 🔴 **Missing descriptions**: 500+ recipes
- 🔴 **Missing pH values**: 510+ recipes
- 🔴 **Missing/unmapped organisms**: 500+ recipes

**Quality Distribution**:
- **Critical** (< 50 score): 500+ recipes need immediate attention
- **Needs Work** (50-69): Moderate quality issues
- **Good** (70-89): Minor gaps
- **Excellent** (≥ 90): High quality, minimal issues

### Generated Files

1. **Quality Report**: `data/import_tracking/reports/quality_analysis.md`
   - Detailed analysis of top 500 priority recipes
   - Specific issues identified for each recipe
   - Recommended Edison queries

2. **Edison Batch File**: `data/import_tracking/reports/edison_batch.json`
   - 100 highest-priority recipes
   - 400 structured queries for Edison processing
   - Fields to update: description, pH, organisms, ingredient mappings

## Workflow

### Phase 1: Setup & Prioritization

#### 1.1 Run Quality Analysis

```bash
# Analyze all recipes and generate priority list
python scripts/analyze_media_quality.py \
  --yaml-dir data/normalized_yaml \
  --output data/import_tracking/reports/quality_analysis.md \
  --edison-batch data/import_tracking/reports/edison_batch.json \
  --batch-size 100
```

**Output**:
- `quality_analysis.md`: Prioritized list with specific issues
- `edison_batch.json`: Structured queries for Edison

#### 1.2 Review Priority List

```bash
# View top 20 priority recipes
head -200 data/import_tracking/reports/quality_analysis.md
```

Identify:
- Recipes with score < 30 (highest priority)
- Common patterns (e.g., all TOGO media missing descriptions)
- Batch-able queries (e.g., all Dehalospirillum media)

### Phase 2: Edison Deep Research

#### 2.1 Load Edison Batch

Open `data/import_tracking/reports/edison_batch.json` to see structured queries.

Each recipe has 4 query types:
1. **Description query**: "What is [medium] used for?"
2. **pH query**: "What is the pH of [medium]?"
3. **Organisms query**: "What organisms are cultivated using [medium]?"
4. **Ingredient mapping**: "What are CHEBI IDs for ingredients in [medium]?"

#### 2.2 Execute Edison Queries

**Approach 1: Single Recipe Deep Dive**

For highest-priority recipe (e.g., `dehalospirillum_medium`):

1. **Go to Edison**: https://platform.edisonscientific.com/
2. **Start New Research Project**: "Dehalospirillum Medium Review"
3. **Run Comprehensive Query**:

```
Research the Dehalospirillum culture medium (also known as Dehalospirillum Medium, TOGO M2455):

1. What is this medium used for? What organisms does it cultivate?
2. What is the standard pH value?
3. What are the exact chemical ingredients and their concentrations?
4. Map each ingredient to CHEBI IDs where possible
5. Provide NCBITaxon IDs for target organisms

Focus on peer-reviewed literature and authoritative microbiology databases (DSMZ, ATCC, culture collection catalogs).
```

4. **Wait for Edison Research** (typically 5-15 minutes)
5. **Review Results**: Edison will return comprehensive findings with citations

**Approach 2: Batch Processing**

For systematic review of 10-20 similar media:

1. **Group by Source**: Process all TOGO media together, all MediaDive together
2. **Create Batch Query**:

```
Research the following 10 bacterial culture media and provide for each:
- Description (2-3 sentences)
- pH value
- Target organisms (with NCBITaxon IDs)
- Key ingredients (with CHEBI IDs)

Media list:
1. Dehalospirillum Medium (TOGO M2455)
2. Methanosphaerula Peat Medium (TOGO M2655)
3. [... 8 more media ...]

Format results as structured data for each medium.
```

3. **Process Results**: Edison returns findings for all 10 media
4. **Validate**: Cross-check against original sources

### Phase 3: Update Recipe Files

#### 3.1 Create Update Script

Use Edison results to update YAML files:

```bash
# Example: Update description for dehalospirillum_medium
# (Manual editing or script-based)

# Open file
code data/normalized_yaml/bacterial/TOGO_M2455_Dehalospirillum_Medium.yaml
```

**Before**:
```yaml
name: dehalospirillum_medium
category: bacterial
medium_type: DEFINED
physical_state: LIQUID
# No description
# No ph_value
# No target_organisms
ingredients:
  - name: unknown
    # No ingredient_term (CHEBI)
```

**After** (enriched with Edison results):
```yaml
name: dehalospirillum_medium
category: bacterial
medium_type: DEFINED
physical_state: LIQUID
description: >-
  Medium for cultivation of Dehalospirillum multivorans, a dehalorespirating
  bacterium capable of using chlorinated compounds as electron acceptors.
  Designed for anaerobic growth with organic acids and chlorinated compounds.
ph_value: 7.2
target_organisms:
  - name: Dehalospirillum multivorans
    organism_term:
      id: NCBITaxon:65702
      label: Dehalospirillum multivorans
ingredients:
  - name: sodium formate
    ingredient_term:
      id: CHEBI:62024
      label: sodium formate
    amount: 3.4 g/L
  - name: yeast extract
    ingredient_term:
      id: CHEBI:77642
      label: yeast extract
    amount: 0.5 g/L
  # ... (continue with Edison-mapped ingredients)

curation_history:
  - timestamp: '2026-03-18T10:30:00Z'
    curator: edison-deep-research
    action: ENRICHED
    fields_changed: [description, ph_value, target_organisms, ingredients]
    notes: "Enriched with Edison deep research findings from peer-reviewed literature"
```

#### 3.2 Automated Update Script

For batch updates, create a script:

```python
# scripts/apply_edison_results.py

import yaml
import json
from pathlib import Path

def apply_edison_results(recipe_file: Path, edison_results: dict):
    """Apply Edison research results to recipe YAML."""

    # Load recipe
    with open(recipe_file) as f:
        recipe = yaml.safe_load(f)

    # Update fields
    if 'description' in edison_results:
        recipe['description'] = edison_results['description']

    if 'ph_value' in edison_results:
        recipe['ph_value'] = float(edison_results['ph_value'])

    if 'target_organisms' in edison_results:
        recipe['target_organisms'] = edison_results['target_organisms']

    # Update ingredients with CHEBI mappings
    if 'ingredient_mappings' in edison_results:
        for ing in recipe.get('ingredients', []):
            chebi_id = edison_results['ingredient_mappings'].get(ing['name'])
            if chebi_id:
                ing['ingredient_term'] = {
                    'id': chebi_id,
                    'label': ing['name']
                }

    # Add curation history
    if 'curation_history' not in recipe:
        recipe['curation_history'] = []

    recipe['curation_history'].append({
        'timestamp': datetime.now().isoformat(),
        'curator': 'edison-deep-research',
        'action': 'ENRICHED',
        'fields_changed': list(edison_results.keys()),
        'notes': 'Enriched with Edison deep research findings'
    })

    # Write back
    with open(recipe_file, 'w') as f:
        yaml.dump(recipe, f, sort_keys=False, allow_unicode=True)
```

### Phase 4: Validation & Commit

#### 4.1 Validate Updates

```bash
# Schema validation
just validate-recipes

# Check for duplicates
python scripts/validate_duplicate_ids.py

# Verify ingredient mappings
python scripts/validate_ingredient_mappings.py
```

#### 4.2 Quality Re-Assessment

```bash
# Re-run quality analysis on updated files
python scripts/analyze_media_quality.py \
  --yaml-dir data/normalized_yaml \
  --output data/import_tracking/reports/quality_analysis_post_edison.md
```

Compare before/after:
- Completeness scores should increase
- Unmapped ingredients should decrease
- Missing descriptions should be filled

#### 4.3 Commit Changes

```bash
git add data/normalized_yaml/
git commit -m "Enrich media records with Edison deep research

- Added descriptions for 50 bacterial media
- Mapped 200+ ingredients to CHEBI IDs
- Added target organism NCBITaxon IDs
- Filled pH values from literature

Source: Edison deep research with peer-reviewed citations
Curator: edison-deep-research
"
```

## Best Practices

### Query Formulation

**Good Edison Query**:
```
Research the "Dehalospirillum Medium" (TOGO ID: M2455):

1. Primary use: What organisms does this medium cultivate?
2. pH: What is the standard pH value?
3. Composition: List all ingredients with exact concentrations
4. Chemical IDs: Map ingredients to CHEBI identifiers
5. Organism taxonomy: Provide NCBITaxon IDs for target organisms

Focus on:
- Peer-reviewed microbiology literature
- Authoritative culture collection databases (DSMZ, ATCC, TOGO)
- Original medium formulation papers

Prioritize accuracy over completeness. Include citations.
```

**Bad Query**:
```
Tell me about dehalospirillum medium
```

### Verification

Always verify Edison results against:
1. **Original source databases** (TOGO, MediaDive, DSMZ)
2. **Peer-reviewed literature** (check Edison citations)
3. **Existing CultureMech data** (don't overwrite correct data)

### Batch Processing Tips

1. **Group by Category**: Process all bacterial media together
2. **Group by Source**: Process all TOGO media together
3. **Start Small**: Test workflow on 5-10 recipes first
4. **Validate Frequently**: Don't accumulate 100s of unvalidated updates

## Metrics & Progress Tracking

### Track Progress

Create tracking sheet:

| Batch | Recipes | Status | Completeness Before | Completeness After | Date |
|-------|---------|--------|---------------------|-------------------|------|
| 1 | 10 TOGO media | ✓ Complete | 15/100 | 85/100 | 2026-03-18 |
| 2 | 20 MediaDive | In Progress | 25/100 | - | - |

### Success Metrics

**Target Goals**:
- ✓ 90%+ recipes have descriptions
- ✓ 85%+ ingredients mapped to CHEBI
- ✓ 90%+ recipes have pH values
- ✓ 80%+ recipes have target organisms with NCBITaxon IDs
- ✓ Average completeness score > 75/100

### Current Status (March 2026)

- Total recipes: 15,827
- Average completeness: 35.7/100
- Critical priority: 500+ recipes
- Target: Improve 100 recipes per week with Edison

**12-Week Goal**: 1,200+ recipes enriched, average score > 60/100

## Edison Platform Tips

### Effective Research Strategies

1. **Use "Deep Research" Mode**: Most thorough, best for complex media
2. **Provide Context**: Include source database ID, category, organism type
3. **Request Citations**: Always ask for peer-reviewed sources
4. **Structured Output**: Request JSON or YAML format for easy parsing
5. **Batch Similar Items**: Process 5-10 related media per query

### Example Advanced Query

```
Conduct deep research on the following 5 bacterial culture media from the TOGO database.
For each medium, provide structured output in JSON format:

{
  "medium_name": "...",
  "togo_id": "...",
  "description": "2-3 sentence description",
  "ph_value": numeric,
  "target_organisms": [
    {"name": "...", "ncbitaxon_id": "..."}
  ],
  "ingredients": [
    {"name": "...", "chebi_id": "...", "concentration": "..."}
  ],
  "citations": ["DOI or PMID"]
}

Media to research:
1. Dehalospirillum Medium (M2455)
2. Methanosphaerula Peat Medium (M2655)
3. [... 3 more ...]

Prioritize authoritative microbiology sources and culture collection databases.
```

## Troubleshooting

### Edison Returns Conflicting Data

**Problem**: Edison finds pH 7.2 but original source says 7.5

**Solution**:
1. Check Edison citations - are they authoritative?
2. Preserve original value in `notes` field
3. Use most recent/authoritative source
4. Document discrepancy in `curation_history`

### Ingredient Mapping Ambiguity

**Problem**: "Yeast extract" could map to multiple CHEBI IDs

**Solution**:
1. Use most general CHEBI ID (CHEBI:77642 for yeast extract)
2. Note specificity in ingredient `notes`
3. Consult MediaIngredientMech for canonical mapping
4. When in doubt, leave unmapped with note

### Batch Results Too Generic

**Problem**: Edison gives same description for 10 different media

**Solution**:
1. Reduce batch size (5 instead of 10)
2. Request "distinctive characteristics" for each
3. Provide more context (organism type, source database)
4. Review individual literature for each medium

## Role Research (Step 7b Literature Lane)

This document describes the manual per-recipe review workflow. For **ingredient
role facets** (nutritional / physicochemical / cellular-metabolic), Step 7b of
the ingredient-roles migration adds a fully SDK-driven pipeline that
supersedes the browser-based workflow for role assignments:

- `just prioritize-role-research-candidates` — rank MIM ingredients by facet-gap × occurrence
- MIM `just research-ingredient-roles-edison-batch` — dispatch Edison against the top-N
- `just extract-roles-from-edison` — parse the fenced YAML block into dual applier batches
- MIM `just apply-role-research-results` — write rich per-facet RoleAssignments to MIM
- `just apply-ingredient-roles` — populate scalar facet tokens on CultureMech recipe descriptors

See the runbook in `.claude/skills/research-ingredient-roles/SKILL.md` for the
full sequence, dry-run flags, and the mechanistic-vs-literature merge policy.

Use the manual workflow below for **medium-level** enrichment (descriptions,
pH values, target organisms, ingredient identity mapping) that the SDK pipeline
does not cover.

## Next Steps

1. **Review quality report**: `data/import_tracking/reports/quality_analysis.md`
2. **Select batch**: Choose 10-20 priority recipes
3. **Run Edison queries**: Use platform to research selected media
4. **Apply results**: Update YAML files with findings
5. **Validate**: Run validation and re-assess quality
6. **Commit**: Push enriched data
7. **Repeat**: Process next batch

## Resources

- **Edison Platform**: https://platform.edisonscientific.com/
- **Quality Report**: `data/import_tracking/reports/quality_analysis.md`
- **Edison Batch**: `data/import_tracking/reports/edison_batch.json`
- **CultureMech Schema**: `src/culturemech/schema/culturemech.yaml`
- **MediaIngredientMech**: For canonical ingredient mappings
