# Contributing to CultureMech

Thank you for your interest in contributing to CultureMech! This guide will help you add high-quality media recipes to the knowledge base.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally
3. **Install dependencies**: `just install`
4. **Create a branch**: `git checkout -b add-recipe-name`

## Adding a New Recipe

### 1. Choose the Right Category

Place your recipe in the appropriate directory:

- `normalized_yaml/bacterial/` - Media for bacterial cultures
- `normalized_yaml/fungal/` - Media for fungal/yeast cultures
- `normalized_yaml/archaea/` - Media for archaeal cultures
- `normalized_yaml/specialized/` - Specialized media (anaerobic, phototrophic, etc.)

### 2. Create the YAML File

**File naming convention**: Use `Snake_Case_Name.yaml` matching the medium name.

Example: `Tryptic_Soy_Broth.yaml`

### 3. Required Fields

Every recipe MUST include:

```yaml
name: [Human-readable name]
category: [bacterial/fungal/archaea/specialized]
medium_type: [DEFINED/COMPLEX/MINIMAL/SELECTIVE/DIFFERENTIAL/ENRICHMENT]
physical_state: [LIQUID/SOLID_AGAR/SEMISOLID/BIPHASIC]
ingredients: [At least one ingredient]
```

### 4. Recommended Fields

For high-quality recipes, include:

- `description` - Purpose and context
- `target_organisms` - With NCBITaxon IDs
- `preparation_steps` - Detailed protocol
- `sterilization` - Method and parameters
- `storage` - Conditions and shelf life
- `applications` - Use cases
- `references` - Literature sources

### 5. Ontology Term Guidelines

#### Chemical Ingredients (CHEBI)

Always include CHEBI terms for well-defined chemicals:

```yaml
ingredients:
  - preferred_term: Glucose
    term:
      id: CHEBI:17234
      label: D-glucose
    concentration:
      value: "10"
      unit: G_PER_L
```

**Finding CHEBI IDs**:
- Search at https://www.ebi.ac.uk/chebi/
- Use exact chemical name
- Include label to enable validation

**Undefined components** (e.g., "Yeast Extract") may omit the term field.

#### Target Organisms (NCBITaxon)

Include NCBITaxon IDs for all organisms:

```yaml
target_organisms:
  - preferred_term: Escherichia coli
    term:
      id: NCBITaxon:562
      label: Escherichia coli
    strain: K-12, DH5α, BL21
```

**Finding NCBITaxon IDs**:
- Search at https://www.ncbi.nlm.nih.gov/taxonomy
- Use species-level IDs when possible
- Include strain information separately

#### Media Database References

Link to authoritative sources when available:

```yaml
media_term:
  preferred_term: DSMZ Medium 1
  term:
    id: DSMZ:1
    label: DSMZ Medium 1 - LB Medium
```

Supported databases: DSMZ, TOGO, ATCC, NCIT

### 6. Concentration Units

Use standard units from the enum:

- `G_PER_L` - grams per liter
- `MG_PER_L` - milligrams per liter
- `MICROG_PER_L` - micrograms per liter
- `MOLAR` - moles per liter
- `MILLIMOLAR` - millimoles per liter
- `MICROMOLAR` - micromoles per liter
- `PERCENT_W_V` - percent weight per volume
- `PERCENT_V_V` - percent volume per volume

### 7. Preparation Steps

Provide clear, ordered instructions:

```yaml
preparation_steps:
  - step_number: 1
    action: DISSOLVE
    description: Dissolve all salts in 900 mL distilled water

  - step_number: 2
    action: AUTOCLAVE
    description: Autoclave at 121°C for 20 minutes
    temperature:
      value: 121
      unit: CELSIUS
    duration: "20 minutes"
```

Available actions: DISSOLVE, MIX, HEAT, COOL, AUTOCLAVE, FILTER_STERILIZE, ADJUST_PH, ADD_AGAR, POUR_PLATES, ALIQUOT, STORE

### 8. Evidence and References

Include literature support when available:

```yaml
references:
  - reference: PMID:12345678
    title: Original paper title
    authors: Smith J, Doe A
    year: 2020

evidence:
  - reference: PMID:12345678
    supports: SUPPORT
    snippet: "Exact quote from paper supporting this formulation"
    explanation: Why this evidence matters
```

**Notes**:
- Evidence is optional for historical recipes
- PMID preferred over DOI
- Snippets enable validation (anti-hallucination)

### 9. Curation History

Always add a curation event:

```yaml
curation_history:
  - timestamp: "2026-01-21T20:00:00Z"
    curator: your-github-username
    action: Initial recipe creation
    notes: Based on DSMZ formulation
```

## Validation

Before submitting, validate your recipe:

```bash
# Schema validation (required)
just validate-schema normalized_yaml/bacterial/Your_Recipe.yaml

# Term validation (required if using ontology terms)
just validate-terms normalized_yaml/bacterial/Your_Recipe.yaml

# Full validation (all layers)
just validate normalized_yaml/bacterial/Your_Recipe.yaml
```

Fix any errors before proceeding.

## Testing

Run the test suite to ensure nothing broke:

```bash
just test
```

## Submission

1. **Commit your changes**:
   ```bash
   git add normalized_yaml/bacterial/Your_Recipe.yaml
   git commit -m "Add [Medium Name] recipe"
   ```

2. **Push to your fork**:
   ```bash
   git push origin add-recipe-name
   ```

3. **Create a Pull Request** on GitHub

4. **PR Description** should include:
   - Medium name and category
   - Source (DSMZ, literature, lab protocol, etc.)
   - Any special considerations

## Quality Checklist

Before submitting, verify:

- [ ] File is in correct category directory
- [ ] All required fields present
- [ ] CHEBI IDs for chemicals (where applicable)
- [ ] NCBITaxon IDs for organisms
- [ ] Concentration values and units specified
- [ ] Preparation steps in logical order
- [ ] Recipe passes schema validation
- [ ] Term validation passes (if using ontology terms)
- [ ] Curation history included
- [ ] References cited (if available)

## Common Pitfalls

### ❌ Don't

- Use fake or made-up ontology IDs
- Copy-paste without verifying labels match IDs
- Include personal or unpublished protocols without permission
- Use ambiguous chemical names without CHEBI IDs
- Omit concentration units

### ✅ Do

- Search ontologies carefully for correct terms
- Verify CHEBI labels match the intended chemical
- Use NCBITaxon for all organisms
- Include preparation details (temperature, duration)
- Add historical context in notes
- Link to authoritative media databases
- Cite original literature sources

## Recipe Template

Use this template as a starting point:

```yaml
name: [Medium Name]
category: bacterial

media_term:
  preferred_term: [Database name]
  term:
    id: [DSMZ:X or TOGO:X]
    label: [Full label]

description: |
  [Purpose and context of this medium]

medium_type: [DEFINED/COMPLEX/MINIMAL/SELECTIVE/DIFFERENTIAL/ENRICHMENT]
physical_state: [LIQUID/SOLID_AGAR/SEMISOLID/BIPHASIC]

target_organisms:
  - preferred_term: [Organism name]
    term:
      id: NCBITaxon:[ID]
      label: [Species name]
    strain: [Strain info]

ingredients:
  - preferred_term: [Ingredient name]
    term:
      id: CHEBI:[ID]
      label: [Chemical name]
    concentration:
      value: "[amount]"
      unit: G_PER_L
    notes: [Any special notes]

preparation_steps:
  - step_number: 1
    action: DISSOLVE
    description: [Step description]

sterilization:
  method: AUTOCLAVE
  temperature:
    value: 121
    unit: CELSIUS
  duration: "20 minutes"

storage:
  temperature:
    value: 4
    unit: CELSIUS
  shelf_life: "3 months"

applications:
  - [Use case 1]
  - [Use case 2]

references:
  - reference: PMID:[ID]
    title: [Paper title]
    authors: [Authors]
    year: [Year]

notes: |
  [Any additional notes, tips, or historical context]

curation_history:
  - timestamp: "[ISO 8601 timestamp]"
    curator: [your-username]
    action: Initial creation
    notes: [Source information]
```

## Getting Help

- **Questions**: Open a GitHub issue
- **Schema documentation**: See `src/culturemech/schema/culturemech.yaml`
- **Examples**: Check `normalized_yaml/bacterial/LB_Broth.yaml`
- **Ontology search**:
  - CHEBI: https://www.ebi.ac.uk/chebi/
  - NCBITaxon: https://www.ncbi.nlm.nih.gov/taxonomy

## Code of Conduct

- Be respectful and constructive
- Focus on scientific accuracy
- Cite sources appropriately
- Welcome feedback and collaboration

Thank you for contributing to CultureMech! 🧫
