# Recipe Enrichment Guide

This guide shows how to enrich media recipes with the new PFAS-based schema extensions.

## Quick Start

### Option 1: Automatic Enrichment (Recommended)

Use the import scripts to automatically add roles to ingredients:

```bash
# Preview what would change (dry-run)
just import-pfas-roles --dry-run

# Apply the changes
just import-pfas-roles

# Import cofactor reference data
just import-pfas-cofactors

# Or do both at once
just import-pfas-all
```

This automatically adds `role` fields to ingredients with matching CHEBI IDs.

### Option 2: Manual Enrichment

Edit YAML files directly to add new fields. See examples below.

---

## New Fields Available

### 1. Ingredient Roles

Add functional role annotations to ingredients:

```yaml
ingredients:
  - preferred_term: Glucose
    concentration:
      value: '10.0'
      unit: G_PER_L
    term:
      id: CHEBI:17234
      label: glucose
    # NEW: Functional roles (multivalued)
    role:
      - CARBON_SOURCE
      - ENERGY_SOURCE
```

**Available roles:**
- `CARBON_SOURCE` - Primary carbon source
- `NITROGEN_SOURCE` - Nitrogen source
- `MINERAL` - Major mineral nutrient
- `TRACE_ELEMENT` - Micronutrient
- `BUFFER` - pH buffering agent
- `VITAMIN_SOURCE` - Provides vitamins
- `SALT` - Osmotic balance/ionic strength
- `PROTEIN_SOURCE` - Complex protein source
- `AMINO_ACID_SOURCE` - Amino acids
- `SOLIDIFYING_AGENT` - Gelling agent (agar)
- `ENERGY_SOURCE` - Energy source
- `ELECTRON_ACCEPTOR` - Terminal electron acceptor
- `ELECTRON_DONOR` - Electron donor
- `COFACTOR_PROVIDER` - Supplies cofactors

---

### 2. Cofactors Provided by Ingredients

Annotate which cofactors an ingredient provides:

```yaml
ingredients:
  - preferred_term: MgSO4·7H2O
    concentration:
      value: '1.0'
      unit: G_PER_L
    term:
      id: CHEBI:31795
      label: MgSO4·7H2O
    role:
      - MINERAL
      - COFACTOR_PROVIDER
    # NEW: Cofactors provided
    cofactors_provided:
      - preferred_term: Magnesium ion
        term:
          id: CHEBI:18420
          label: magnesium(2+)
        category: METALS
        bioavailability: Readily available as Mg2+ ion
        notes: Essential cofactor for hundreds of enzymes
```

**Cofactor categories:**
- `VITAMINS` - Vitamins and vitamin-derived cofactors
- `METALS` - Metal ions (Fe, Mg, Ca, Zn, etc.)
- `NUCLEOTIDES` - NAD, NADH, NADP, ATP, etc.
- `ENERGY_TRANSFER` - CoA, SAM, acetyl-CoA, etc.
- `OTHER_SPECIALIZED` - PQQ, F420, methanofuran, etc.

**Cofactor attributes:**
- `preferred_term` (required) - Human-readable name
- `term` - CHEBI ontology term
- `category` - One of the categories above
- `precursor` - Precursor molecule name
- `precursor_term` - CHEBI term for precursor
- `ec_associations` - List of EC numbers
- `kegg_pathways` - List of KEGG pathway IDs
- `enzyme_examples` - Example enzymes using this cofactor
- `biosynthesis_genes` - Genes for biosynthesis
- `bioavailability` - Uptake characteristics
- `notes` - Additional information

---

### 3. Community Roles for Organisms

Annotate organisms with their functional role in microbial communities:

```yaml
target_organisms:
  - preferred_term: Methylobacterium extorquens
    term:
      id: NCBITaxon:408
      label: Methylobacterium extorquens
    strain: AM1

    # NEW: Community role annotation
    community_role:
      - PRIMARY_DEGRADER

    # NEW: Target abundance in community
    target_abundance: 0.6  # 60% of community

    # NEW: Functional contributions
    community_function:
      - C1 metabolism
      - Methanol oxidation
```

**Available community roles:**
- `PRIMARY_DEGRADER` - Direct substrate degradation (40-60% abundance)
- `REDUCTIVE_DEGRADER` - Reductive degradation pathways
- `OXIDATIVE_DEGRADER` - Oxidative degradation pathways
- `BIOTRANSFORMER` - Converts without complete degradation
- `SYNERGIST` - Complementary functions (15-30% abundance)
- `BRIDGE_ORGANISM` - Provides essential cofactors to community
- `ELECTRON_SHUTTLE` - Facilitates electron transfer
- `DETOXIFIER` - Handles toxic intermediates
- `COMMENSAL` - General commensal
- `COMPETITOR` - Competitive organism

---

### 4. Organism Cofactor Requirements

Specify which cofactors an organism requires:

```yaml
target_organisms:
  - preferred_term: Methylobacterium extorquens
    term:
      id: NCBITaxon:408
      label: Methylobacterium extorquens

    # NEW: Cofactor requirements
    cofactor_requirements:
      # Example 1: Auxotroph (cannot synthesize)
      - cofactor:
          preferred_term: Cobalamin (Vitamin B12)
          term:
            id: CHEBI:16335
            label: cobalamin
          category: VITAMINS
          notes: Required for C1 metabolism
        can_biosynthesize: false
        confidence: 0.95

      # Example 2: Prototroph (can synthesize)
      - cofactor:
          preferred_term: Tetrahydrofolate
          term:
            id: CHEBI:20506
            label: tetrahydrofolate
          category: VITAMINS
        can_biosynthesize: true
        confidence: 0.90
        genes:
          - folA
          - folB
          - folC
```

**CofactorRequirement attributes:**
- `cofactor` (required) - CofactorDescriptor (see above)
- `can_biosynthesize` (required) - true/false
- `confidence` - Confidence score (0.0-1.0)
- `evidence` - List of EvidenceItems
- `genes` - Related gene names

---

### 5. Transporter Annotations

Annotate organism transport systems:

```yaml
target_organisms:
  - preferred_term: Methylobacterium extorquens
    term:
      id: NCBITaxon:408
      label: Methylobacterium extorquens

    # NEW: Transporter systems
    transporters:
      - name: Methanol dehydrogenase (MDH)
        transporter_type: DEHALOGENASE
        substrates:
          - methanol
        substrate_terms:
          - id: CHEBI:17790
            label: methanol
        direction: import
        genes:
          - mxaF
          - mxaI
        ec_number: 1.1.2.7
        notes: PQQ-dependent methanol dehydrogenase

      - name: Nitrate transporter (NarK)
        transporter_type: MFS
        substrates:
          - nitrate
          - nitrite
        substrate_terms:
          - id: CHEBI:17632
            label: nitrate
        direction: import
        genes:
          - narK
```

**Available transporter types:**
- `ABC` - ATP-binding cassette
- `MFS` - Major facilitator superfamily
- `PTS` - Phosphotransferase system
- `TONB` - TonB-dependent receptor
- `SYMPORTER` - Co-transporter
- `ANTIPORTER` - Exchanger
- `UNIPORTER` - Channel
- `PORIN` - Outer membrane protein
- `SIDEROPHORE_RECEPTOR` - Iron uptake receptor
- `DEHALOGENASE` - Dehalogenase enzyme
- `FLUORIDE_EXPORTER` - Fluoride exporter

---

## Complete Example

See the fully enriched example at:
```
normalized_yaml/bacterial/Nitrate_Mineral_Salts_Medium_(NMS)_ENRICHED_EXAMPLE.yaml
```

This shows all new fields in action.

---

## Validation

Always validate after enriching:

```bash
# Validate a single recipe
just validate normalized_yaml/bacterial/MyRecipe.yaml

# Validate all recipes
just validate-all
```

---

## Programmatic Enrichment

For batch enrichment, you can create Python scripts:

```python
#!/usr/bin/env python
"""
Custom enrichment script example
"""
import yaml
from pathlib import Path

def add_roles_to_recipe(recipe_path: Path):
    """Add ingredient roles to a recipe."""
    with open(recipe_path) as f:
        recipe = yaml.safe_load(f)

    # Example: Add roles based on ingredient names
    for ingredient in recipe.get('ingredients', []):
        name = ingredient['preferred_term'].lower()

        if 'glucose' in name:
            ingredient['role'] = ['CARBON_SOURCE', 'ENERGY_SOURCE']
        elif 'kno3' in name or 'nitrate' in name:
            ingredient['role'] = ['NITROGEN_SOURCE', 'ELECTRON_ACCEPTOR']
        elif 'buffer' in name or 'phosphate' in name:
            ingredient['role'] = ['BUFFER', 'MINERAL']
        # Add more mappings...

    # Write back
    with open(recipe_path, 'w') as f:
        yaml.dump(recipe, f, default_flow_style=False,
                  allow_unicode=True, sort_keys=False)

# Use it
recipe_dir = Path("normalized_yaml/bacterial")
for recipe_file in recipe_dir.glob("*.yaml"):
    add_roles_to_recipe(recipe_file)
```

---

## Best Practices

1. **Start with automatic enrichment**: Run `just import-pfas-all` first
2. **Use CHEBI terms**: Always include ontology terms for validation
3. **Be specific with roles**: Use multiple roles when appropriate
4. **Document changes**: Add curation history entries
5. **Validate frequently**: Run validation after each change
6. **Review imported data**: The PFAS import is semi-automatic - review results

---

## Common Patterns

### Pattern 1: Carbon/Nitrogen Source

```yaml
- preferred_term: Glucose
  role: [CARBON_SOURCE, ENERGY_SOURCE]

- preferred_term: NH4Cl
  role: [NITROGEN_SOURCE]
```

### Pattern 2: Buffer System

```yaml
- preferred_term: KH2PO4
  role: [BUFFER, MINERAL]

- preferred_term: Na2HPO4
  role: [BUFFER, MINERAL]
```

### Pattern 3: Metal Cofactor Provider

```yaml
- preferred_term: FeSO4
  role: [TRACE_ELEMENT, COFACTOR_PROVIDER]
  cofactors_provided:
    - preferred_term: Iron(II) ion
      term:
        id: CHEBI:29033
        label: iron(2+)
      category: METALS
```

### Pattern 4: Community Design

```yaml
target_organisms:
  - preferred_term: Primary degrader
    community_role: [PRIMARY_DEGRADER]
    target_abundance: 0.5

  - preferred_term: Cofactor provider
    community_role: [BRIDGE_ORGANISM, SYNERGIST]
    target_abundance: 0.3
    cofactor_requirements:
      - cofactor:
          preferred_term: Vitamin B12
          category: VITAMINS
        can_biosynthesize: true
```

---

## Data Sources

The enrichment data comes from:

- **PFAS Repository**: `/Users/marcin/Documents/VIMSS/ontology/PFAS/PFASCommunityAgents`
  - Ingredient roles: `data/sheets_pfas/PFAS_Data_for_AI_media_ingredients_extended.tsv`
  - Cofactor hierarchy: `data/reference/cofactor_hierarchy.yaml`
  - Cofactor mappings: `data/reference/ingredient_cofactor_mapping.csv`

Generated reference data:
- **Cofactors**: `data/reference/cofactors.yaml` (generated by `just import-pfas-cofactors`)

---

## Questions?

- Check the schema: `src/culturemech/schema/culturemech.yaml`
- View the enriched example: `normalized_yaml/bacterial/Nitrate_Mineral_Salts_Medium_(NMS)_ENRICHED_EXAMPLE.yaml`
- Run import scripts with `--help` for options
