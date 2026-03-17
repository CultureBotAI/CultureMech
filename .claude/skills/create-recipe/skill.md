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

**Your Task**: Understand the input format and extract recipe information

**Actions**:
1. Read the input (file, text, JSON, etc.)
2. Identify recipe type (medium vs solution)
3. Extract key components:
   - Recipe name
   - Ingredients with concentrations
   - pH, temperature, preparation steps
   - Source/reference information
   - Target organisms (if mentioned)

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

### Step 2: Generate YAML Structure

**Your Task**: Create a valid CultureMech YAML record

**Required Fields**:
- `name` - Recipe name
- `medium_type` - DEFINED, COMPLEX, SEMI_DEFINED, etc.
- `physical_state` - LIQUID, SOLID, SEMI_SOLID
- `ingredients` - List with preferred_term and concentration

**Template**:
```yaml
name: Recipe Name
original_name: Recipe Name
category: bacterial  # or algae, archaea, fungal, specialized
medium_type: DEFINED
physical_state: LIQUID

ingredients:
  - preferred_term: Ingredient 1
    concentration: 10 G_PER_L
  - preferred_term: Ingredient 2
    concentration: 5 G_PER_L

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

curation_history:
  - timestamp: CURRENT_TIME
    curator: create-recipe-skill
    action: Created new recipe from input
```

**Schema Validation**: Always validate against `src/culturemech/schema/culturemech.yaml`

### Step 3: Assign CultureMech ID

**Your Task**: Get next available CultureMech ID

**Actions**:
1. Use `manage-identifiers` skill to find highest ID
2. Mint next sequential ID
3. Add to YAML: `id: CultureMech:NNNNNN`

**Example**:
```bash
# Find highest ID
python scripts/find_highest_id.py --prefix CultureMech

# Output: CultureMech:015431
# Next ID: CultureMech:015432
```

### Step 4: Determine File Location

**Your Task**: Choose correct category directory

**Category Mapping**:
- `bacterial/` - Bacterial growth media
- `algae/` - Algae/cyanobacteria media
- `archaea/` - Archaeal media
- `fungal/` - Fungal/yeast media
- `specialized/` - Cross-kingdom or specialized
- `solutions/` - Stock solutions (not complete media)

**Filename Format**:
```
{sanitized_name}.yaml

Example: "LB Broth" → "LB_Broth.yaml"
```

**Full Path**:
```
data/normalized_yaml/{category}/{sanitized_name}.yaml
```

### Step 5: Validate and Save

**Your Task**: Validate schema and write file

**Actions**:
1. Validate YAML against schema
2. Check for duplicate names
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
2. Add source reference if available
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
  - citation: "Smith et al. (2025). Journal of Microbiology."
    doi: "10.1234/jmicro.2025.001"
    notes: "Recipe described in Materials & Methods, page 3"
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
2. Save to `solutions/` directory
3. Mark as stock solution

**Output Location**: `data/normalized_yaml/solutions/10x_PBS.yaml`

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
- ✅ CultureMech ID assigned and unique
- ✅ Correct category directory
- ✅ No duplicate names in category
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

# 2. Run quality pipeline
just fix-all-data-quality

# 3. Enrich (optional)
# Run MediaIngredientMech enrichment if desired

# 4. Regenerate indexes
just generate-indexes

# 5. Commit
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

**Output**: `data/normalized_yaml/bacterial/TSB.yaml` with CultureMech ID

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

**Output**: `data/normalized_yaml/solutions/1M_Tris_HCl_pH8.yaml`

## Tips for Best Results

1. **Provide Complete Information**: More details = better YAML
2. **Include Source**: Always cite where recipe came from
3. **Specify Units**: Clear concentration units help parsing
4. **Note Variations**: Document any modifications from original
5. **Validate Early**: Check schema before committing
6. **Use Templates**: Start from similar recipes when possible

## Related Skills

- `manage-identifiers` - ID assignment and management
- `manage-ingredient-hierarchy` - MediaIngredientMech integration

## Script Support

Helper scripts available:
- `scripts/find_highest_id.py` - Get next CultureMech ID
- `scripts/cleanup_recipe_ingredients.py` - Clean duplicates
- `scripts/generate_recipe_indexes.py` - Regenerate indexes

## Quick Reference

```bash
# Full workflow
1. Parse input → Extract recipe data
2. Generate YAML → Validate against schema
3. Assign ID → Use manage-identifiers skill
4. Save file → data/normalized_yaml/{category}/{name}.yaml
5. Validate → just validate-schema {file}
6. Update indexes → just generate-indexes
```

---

**Remember**: Always validate against the schema and regenerate indexes after creating new recipes!
