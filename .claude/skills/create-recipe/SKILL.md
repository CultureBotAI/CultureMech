---
name: create-recipe
description: Create new growth media or solution YAML records from input data or documents
category: workflow
requires_database: false
requires_internet: false
version: 1.0.0
---

# Create Recipe Skill

## Overview

**Purpose**: Generate properly formatted CultureMech YAML records for growth media or solutions from various input formats (text descriptions, papers, protocols, structured data).

**Why**: Streamlines recipe creation, ensures schema compliance, maintains data quality, and provides proper ID assignment.

**Scope**: Creates new MediaRecipe or Solution YAML files with full validation and proper placement.

## When to Use This Skill

Use this skill when you need to:
- Create a new growth medium YAML record from a paper or protocol
- Convert a text recipe description into structured YAML
- Import recipes from external sources (papers, databases, lab notes)
- Generate solution records for stock solutions
- Create test/example recipes for development
- Batch import recipes from documents

## Input Formats Supported

### 1. Text Description
```
"LB Broth: Mix 10 g/L tryptone, 5 g/L yeast extract, 10 g/L NaCl in water.
Autoclave at 121°C for 15 min. pH 7.0."
```

### 2. Structured Data (JSON)
```json
{
  "name": "LB Broth",
  "ingredients": [
    {"name": "Tryptone", "concentration": "10 g/L"},
    {"name": "Yeast extract", "concentration": "5 g/L"},
    {"name": "NaCl", "concentration": "10 g/L"}
  ],
  "ph": 7.0,
  "sterilization": "121°C, 15 min"
}
```

### 3. PDF/Document
- Research papers with media recipes
- Lab protocols
- Supplier specifications
- Culture collection datasheets

### 4. Existing Recipe (for modification)
- Path to existing YAML file
- Recipe ID to use as template

## Workflow

### Step 1: Analyze Input

**Your Task**: Understand the input format, extract recipe information, and
preserve enough provenance to reproduce the curation decision

**Actions**:
1. Read the input (file, text, JSON, etc.)
2. Identify recipe type (medium vs solution)
3. Extract key components:
   - Recipe name
   - Ingredients with concentrations
   - pH, temperature, preparation steps
   - Source/reference information
   - Target organisms (if mentioned)
4. Record structured source provenance for every source used:
   - DOI, PMID, stable URL, or culture-collection accession
   - title
   - authors
   - year
   - source type, such as `journal_article`, `culture_collection_page`,
     `web_page`, `database`, `protocol`, or `lab_note`
   - discovery mode, such as `user_supplied`, `pubmed_search`,
     `catalog_page`, `cross_reference`, or `manual_web_search`

**PublicationReference mapping**:

CultureMech `references[]` uses `PublicationReference` entries with a required
`reference` slot plus optional `title`, `authors`, `year`, and `notes`.

- Put a DOI in `reference` as `doi:10...`; put a PubMed identifier there as
  `PMID:12345678`; put web/culture-collection URLs or local source accessions
  there directly when no DOI/PMID exists.
- Always fill `title`, `authors`, and `year` when the source provides them.
- Record `source_type=...` and `discovery_mode=...` in `notes` until the schema
  has dedicated slots for them.
- Prefer the exact recipe/specification source over a secondary page that only
  mentions the medium name.

**Example**:
```markdown
Input: "M9 minimal medium: Na2HPO4 (6 g/L), KH2PO4 (3 g/L), NaCl (0.5 g/L),
NH4Cl (1 g/L), glucose (4 g/L). Autoclave base salts, add sterile glucose."

Extracted:
- Name: M9 minimal medium
- Type: Defined/Minimal medium
- Ingredients: 5 components with concentrations
- Preparation: Autoclave base, add glucose separately
```

### Step 2: Check Existing Media And Variants

**Your Task**: Determine whether the candidate is already present exactly,
present as a close formulation, or should become a variant of an existing
medium before creating a new parent record.

**Required checks**:

1. Search by source accession, DOI/PMID/URL, official name, original name,
   synonyms, and normalized slug across normalized and merged media. Include
   ignored files so a stale generated file or report cannot be missed:

   ```bash
   rg --no-ignore --hidden -n "<source-id>|<doi>|<url>|<exact name>|<slug>" \
     data/normalized_yaml data/merge_yaml reports
   ```

2. Search for ingredient-set matches and candidate variant clusters using the
   maintained manifest workflow:

   ```bash
   just review-media-content
   just propose-media-variant-links
   ```

3. Inspect `reports/media_content_review_manifest.tsv` and
   `reports/media_variant_link_proposals.tsv` for:
   - exact source duplicates with the same source term or stable URL
   - identical ingredient identity signatures
   - identical ingredient concentration signatures
   - close variants sharing a parent ingredient set but differing by pH,
     salinity, physical state, omitted ingredients, substituted ingredients, or
     supplements

4. Compare candidate YAML against all plausible hits manually. Fingerprints are
   concentration-independent and only identify same-ingredient-set records; they
   do not prove exact recipe identity.

**Classification**:

- **Exact duplicate**: same authoritative recipe or same final formulation.
  Update provenance/evidence on the existing record, or preserve a distinct
  source wrapper only when it has a source-specific accession and link it with
  `variant_relationship: SOURCE_DUPLICATE`.
- **Close variant**: recognizable base medium with changed pH, salt,
  physical state, supplement, omission, substitution, or concentration. Keep
  the base formulation as parent and model the new record as a child with
  `parent_media`, `variant_relationship`, and `variant_modifications`; update
  the parent's `variant_children`.
- **Inline study variant**: organism- or study-specific tweak that does not
  need a full source record. Add it to the parent record's `variants[]`.
- **New parent**: use only after source-ID, alias/name, ingredient-signature,
  and close-variant checks do not identify an exact existing record or a
  defensible parent.

After adding or changing parent/child links, run:

```bash
just validate-media-variant-links
```

### Step 3: Generate YAML Structure

**Your Task**: Create a valid CultureMech YAML record

**Required Fields**:
- `name` - Recipe name
- `medium_type` - DEFINED, COMPLEX, SEMI_DEFINED, etc.
- `physical_state` - LIQUID, SOLID, SEMI_SOLID
- `ingredients` - List with preferred_term and concentration
- `references` - List of structured `PublicationReference` entries for every
  source used

**Template**:
```yaml
name: Recipe Name
original_name: Recipe Name
category: bacterial  # or algae, archaea, fungal, specialized
medium_type: DEFINED
physical_state: LIQUID

ingredients:
  - preferred_term: Ingredient 1
    concentration:
      value: "10"
      unit: G_PER_L
  - preferred_term: Ingredient 2
    concentration:
      value: "5"
      unit: G_PER_L

ph_value: 7.0

sterilization:
  method: AUTOCLAVE
  temperature: 121
  duration: 15
  notes: Standard autoclave cycle

preparation_steps:
  - action: DISSOLVE
    description: Dissolve all ingredients in distilled water
  - action: AUTOCLAVE
    description: Sterilize at 121°C for 15 minutes

notes: Additional preparation notes

references:
  - reference: doi:10...
    title: Source title
    authors: Author, A.; Curator, B.
    year: 2026
    notes: source_type=journal_article; discovery_mode=user_supplied

curation_history:
  - timestamp: CURRENT_TIME
    curator: create-recipe-skill
    action: Created new recipe from input
    source: doi:10...
```

**Schema Validation**: Always validate against `src/culturemech/schema/culturemech.yaml`

### Step 4: Assign CultureMech ID

**Your Task**: Get next available CultureMech ID

**Actions**:
1. Use the `manage-identifiers` skill and run the collision check.
2. Preview the repository ID assigner.
3. Apply only after reviewing the preview.

**Example**:
```bash
just assign-ids-check
just assign-ids --dry-run
# After reviewing the proposed assignment:
just assign-ids
```

### Step 5: Determine File Location

**Your Task**: Choose correct category directory

**Category Mapping**:
- `bacterial/` - Bacterial growth media
- `algae/` - Algae/cyanobacteria media
- `archaea/` - Archaeal media
- `fungal/` - Fungal/yeast media
- `specialized/` - Cross-kingdom or specialized

There is no `solutions/` category. A stock solution is a record with
`record_kind: SOLUTION`, saved in the category directory of the media it
serves; most sit in `bacterial/`, as
`data/normalized_yaml/bacterial/DAS_Vitamin_Cocktail.yaml` does. When the
choice is not obvious, follow an existing solution record from the same source
rather than guessing (see `docs/CONTRIBUTING.md`).
`data/normalized_yaml/solutions/` holds one legacy index and no records
(#422).

**Filename Format**:
```
{sanitized_name}.yaml

Example: "LB Broth" → "LB_Broth.yaml"
```

**Full Path**:
```
data/normalized_yaml/{category}/{sanitized_name}.yaml
```

### Step 6: Validate and Save

**Your Task**: Validate schema and write file

**Actions**:
1. Validate YAML against schema
2. Re-run the exact/source/variant checks from Step 2 against the final file
3. Write file to correct location
4. Regenerate indexes

**Validation**:
```bash
# Validate single file
just validate-schema data/normalized_yaml/bacterial/LB_Broth.yaml

# Validate all
just validate-recipes
```

**Complete**:
```bash
# Regenerate indexes
just generate-indexes
```

## Output Format

### Success Output

```yaml
# File: data/normalized_yaml/bacterial/LB_Broth.yaml
id: CultureMech:015432
name: LB Broth
original_name: LB Broth
category: bacterial
medium_type: COMPLEX
physical_state: LIQUID

ingredients:
  - preferred_term: Tryptone
    concentration: 10 G_PER_L
  - preferred_term: Yeast extract
    concentration: 5 G_PER_L
  - preferred_term: Sodium chloride
    concentration: 10 G_PER_L
  - preferred_term: Water
    concentration: 1000 G_PER_L

ph_value: 7.0

sterilization:
  method: AUTOCLAVE
  temperature: 121
  duration: 15
  temperature_unit: CELSIUS
  duration_unit: MINUTE

preparation_steps:
  - action: DISSOLVE
    description: Dissolve all ingredients in distilled water
  - action: ADJUST_PH
    description: Adjust pH to 7.0 if necessary
  - action: AUTOCLAVE
    description: Sterilize at 121°C for 15 minutes

curation_history:
  - timestamp: 2026-03-15T04:30:00.000000+00:00
    curator: create-recipe-skill
    action: Created new recipe from text input
    notes: Generated from user-provided recipe description
```

### Summary Report

```markdown
✅ Recipe Created Successfully

**File**: data/normalized_yaml/bacterial/LB_Broth.yaml
**ID**: CultureMech:015432
**Name**: LB Broth
**Category**: bacterial
**Ingredients**: 4 components
**Validation**: ✅ Schema valid

**Next Steps**:
1. Review the generated YAML file
2. Review `references[]` DOI/PMID/URL/accession, title, authors, year,
   source type, and discovery mode
3. Enrich with MediaIngredientMech (if desired)
4. Run quality pipeline: `just fix-all-data-quality`
```

## Common Patterns

### Pattern 1: From Paper

**Input**: PDF with recipe in methods section

**Process**:
1. Extract text from PDF
2. Parse ingredients and concentrations
3. Generate YAML with source citation
4. Add to `references` field

**Example**:
```yaml
references:
  - reference: doi:10.1234/jmicro.2025.001
    title: Growth medium optimization for Example bacterium
    authors: Smith, A.; Chen, B.; Patel, C.
    year: 2025
    notes: source_type=journal_article; discovery_mode=user_supplied_pdf; recipe
      described in Materials & Methods, page 3
```

### Pattern 2: From Culture Collection

**Input**: ATCC/DSMZ medium specification

**Process**:
1. Extract from datasheet
2. Add media_term with source ID
3. Link to organism if specified

**Example**:
```yaml
media_term:
  preferred_term: ATCC Medium 1
  term:
    id: atcc.medium:1
    name: ATCC Medium 1

target_organisms:
  - preferred_term: Escherichia coli
```

### Pattern 3: Stock Solution

**Input**: "10× PBS: 80 g NaCl, 2 g KCl, 14.4 g Na2HPO4, 2.4 g KH2PO4 per liter"

**Process**:
1. Identify as solution (not complete medium)
2. Save to the category directory of the media it serves (`bacterial/` here)
3. Set `record_kind: SOLUTION`

**Output Location**: `data/normalized_yaml/<category>/<slug>.yaml` (here `bacterial/10x_pbs.yaml`)

### Pattern 4: Batch Import

**Input**: CSV file with multiple recipes

**Process**:
1. Read CSV rows
2. Generate one YAML per row
3. Assign sequential IDs
4. Validate all files
5. Generate batch report

## Validation Checklist

Before saving, verify:

- ✅ Valid YAML syntax
- ✅ Schema compliance
- ✅ Required fields present (name, medium_type, physical_state, ingredients)
- ✅ Structured `references[]` with a DOI/PMID/URL/accession in `reference`,
  plus `title`, `authors`, `year`, and notes that record `source_type` and
  `discovery_mode` where available
- ✅ CultureMech ID assigned and unique
- ✅ Correct category directory
- ✅ No exact source duplicate, exact formulation duplicate, close variant, or
  parent/child variant missed in existing normalized/merged records
- ✅ Concentration units valid
- ✅ Enum values valid (medium_type, physical_state, etc.)
- ✅ Curation history entry added

## Error Handling

### Common Issues

**Issue**: Missing ingredient concentrations
**Solution**: Mark as approximate or add data quality flag

**Issue**: Unclear medium type
**Solution**: Use COMPLEX as default, add note

**Issue**: Multiple recipes in input
**Solution**: Create separate files for each

**Issue**: Incomplete information
**Solution**: Create with data_quality_flags and notes

## Integration with Pipeline

After creating recipe:

```bash
# 1. Validate
just validate-schema data/normalized_yaml/bacterial/New_Recipe.yaml

# 2. Refresh content and variant candidates
just review-media-content
just propose-media-variant-links
just validate-media-variant-links

# 3. Run quality pipeline
just fix-all-data-quality

# 4. Enrich (optional)
# Run MediaIngredientMech enrichment if desired

# 5. Regenerate indexes
just generate-indexes

# 6. Commit
git add data/normalized_yaml/bacterial/New_Recipe.yaml
git commit -m "Add New_Recipe medium"
```

## Examples

### Example 1: Simple Recipe from Text

**Input**:
```
Create a recipe for TSB (Tryptic Soy Broth):
- Tryptone: 17 g/L
- Soy peptone: 3 g/L
- NaCl: 5 g/L
- K2HPO4: 2.5 g/L
- Glucose: 2.5 g/L
pH 7.3, autoclave 121°C for 15 min
```

**Output**: `data/normalized_yaml/bacterial/tsb.yaml` with CultureMech ID

### Example 2: From JSON

**Input**:
```json
{
  "name": "Nutrient Agar",
  "type": "complex",
  "state": "solid",
  "ingredients": [
    {"name": "Peptone", "amount": "5 g/L"},
    {"name": "Beef extract", "amount": "3 g/L"},
    {"name": "Agar", "amount": "15 g/L"}
  ]
}
```

**Output**: Validated YAML with proper enums and structure

### Example 3: Solution

**Input**: "Create 1 M Tris-HCl pH 8.0 stock solution"

**Output**: `data/normalized_yaml/<category>/<slug>.yaml` with `record_kind: SOLUTION` (here `bacterial/1m_tris_hcl_ph8.yaml`)

## Tips for Best Results

1. **Provide Complete Information**: More details = better YAML
2. **Include Source**: Always cite where recipe came from
3. **Specify Units**: Clear concentration units help parsing
4. **Note Variations**: Document any modifications from original
5. **Validate Early**: Check schema before committing
6. **Use Templates**: Start from similar recipes when possible

## Related Skills

- `manage-identifiers` - ID assignment and management
- `review-recipes` - Recipe quality review, exact merge fingerprinting, and
  candidate parent/child variant review

## Script Support

Helper scripts available:
- `scripts/assign_culturemech_ids.py` - Check and assign CultureMech IDs
- `scripts/cleanup_recipe_ingredients.py` - Clean duplicates
- `scripts/generate_recipe_indexes.py` - Regenerate indexes

## Quick Reference

```bash
# Full workflow
1. Parse input → Extract recipe data
2. Capture provenance → DOI/PMID/URL/accession, title, authors, year, source type, discovery mode
3. Check identity → source duplicate / exact formulation / close variant / new parent
4. Generate YAML → Validate against schema
5. Assign ID → Use manage-identifiers skill
6. Save file → data/normalized_yaml/{category}/{name}.yaml
7. Validate → schema plus media variant links
8. Update indexes → just generate-indexes
```

---

**Remember**: Always validate against the schema and regenerate indexes after creating new recipes!
