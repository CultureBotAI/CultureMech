# KGX Semantic Model for CultureMech

This document describes the semantic modeling used in CultureMech's KGX export, following the patterns established in the [cmm-ai-automation](https://github.com/turbomam/cmm-ai-automation) project.

## Overview

The KGX export transforms CultureMech media recipes into a knowledge graph format with proper semantic relationships. The model focuses on creating meaningful edges between organisms, media, solutions, and ingredients using standardized ontology predicates.

## Entity Types

### Nodes

1. **Medium** (`culturemech:*`)
   - Growth medium formulations
   - Example: `culturemech:LB_Broth`

2. **Organism/Taxon** (`NCBITaxon:*`)
   - Microorganisms that grow in media
   - Example: `NCBITaxon:562` (Escherichia coli)

3. **Solution** (`culturemech:solution_*`)
   - Pre-made stock solutions used in media preparation
   - Example: `culturemech:solution_Trace_Metal_Solution`

4. **Ingredient** (`CHEBI:*`)
   - Chemical entities in media or solutions
   - Example: `CHEBI:17234` (Glucose)

5. **Medium Type** (`culturemech:medium_type_*`)
   - Type classification nodes
   - Example: `culturemech:medium_type_COMPLEX`

## Primary Edges (cmm-ai-automation semantic model)

### 1. Organism → Medium (grows in)

**Relationship**: Organism grows in a specific medium

```
NCBITaxon:562 --[METPO:2000517 (grows in)]--> culturemech:LB_Broth
```

**Structure**:
- **Subject**: Organism (NCBITaxon ID)
- **Predicate**: `METPO:2000517` (grows in)
- **Object**: Medium (culturemech ID)

**Qualifiers**:
- `biolink:strain` - Strain designation (e.g., "K-12")
- `biolink:growth_phase` - Growth phase (e.g., "exponential")

**Example**:
```json
{
  "subject": "NCBITaxon:562",
  "predicate": "METPO:2000517",
  "object": "culturemech:LB_Broth",
  "qualifiers": [
    {
      "qualifier_type_id": "biolink:strain",
      "qualifier_value": "K-12"
    }
  ]
}
```

### 2. Medium → Solution (has part)

**Relationship**: Medium contains a pre-made solution component

```
culturemech:M9_Minimal --[biolink:has_part]--> culturemech:solution_Trace_Elements
```

**Structure**:
- **Subject**: Medium (culturemech ID)
- **Predicate**: `biolink:has_part`
- **Object**: Solution (culturemech solution ID)

**Qualifiers**:
- `biolink:concentration` - Volume added (e.g., "10 mL/L")

**Example**:
```json
{
  "subject": "culturemech:M9_Minimal",
  "predicate": "biolink:has_part",
  "object": "culturemech:solution_Trace_Elements",
  "qualifiers": [
    {
      "qualifier_type_id": "biolink:concentration",
      "qualifier_value": "10 mL/L"
    }
  ]
}
```

### 3. Solution → Ingredient (has part)

**Relationship**: Solution contains chemical ingredients

```
culturemech:solution_Trace_Elements --[biolink:has_part]--> CHEBI:49976
```

**Structure**:
- **Subject**: Solution (culturemech solution ID)
- **Predicate**: `biolink:has_part`
- **Object**: Ingredient (CHEBI ID)

**Qualifiers**:
- `biolink:concentration` - Amount in solution (e.g., "0.07 g/L")
- `biolink:role` - Functional role (e.g., "trace_element")

**Example**:
```json
{
  "subject": "culturemech:solution_Trace_Elements",
  "predicate": "biolink:has_part",
  "object": "CHEBI:49976",
  "qualifiers": [
    {
      "qualifier_type_id": "biolink:concentration",
      "qualifier_value": "0.07 g/L"
    },
    {
      "qualifier_type_id": "biolink:role",
      "qualifier_value": "trace_element"
    }
  ]
}
```

### 4. Medium → Ingredient (has part)

**Relationship**: Medium directly contains chemical ingredients

```
culturemech:LB_Broth --[biolink:has_part]--> CHEBI:17234
```

**Structure**:
- **Subject**: Medium (culturemech ID)
- **Predicate**: `biolink:has_part`
- **Object**: Ingredient (CHEBI ID)

**Qualifiers**:
- `biolink:concentration` - Amount in medium (e.g., "10 g/L")
- `biolink:role` - Functional role (e.g., "carbon_source")

**Example**:
```json
{
  "subject": "culturemech:LB_Broth",
  "predicate": "biolink:has_part",
  "object": "CHEBI:17234",
  "qualifiers": [
    {
      "qualifier_type_id": "biolink:concentration",
      "qualifier_value": "10 g/L"
    },
    {
      "qualifier_type_id": "biolink:role",
      "qualifier_value": "carbon_source"
    }
  ]
}
```

### 5. Medium → Type (has attribute)

**Relationship**: Medium has a type classification (COMPLEX, DEFINED, etc.)

```
culturemech:LB_Broth --[biolink:has_attribute]--> culturemech:medium_type_COMPLEX
```

**Structure**:
- **Subject**: Medium (culturemech ID)
- **Predicate**: `biolink:has_attribute`
- **Object**: Type node (culturemech medium_type ID)

**Qualifiers**:
- `biolink:attribute_type` - Always "medium_type"

**Example**:
```json
{
  "subject": "culturemech:LB_Broth",
  "predicate": "biolink:has_attribute",
  "object": "culturemech:medium_type_COMPLEX",
  "qualifiers": [
    {
      "qualifier_type_id": "biolink:attribute_type",
      "qualifier_value": "medium_type"
    }
  ]
}
```

## Legacy Edges (backward compatibility)

These edges are maintained for backward compatibility with existing KG-Microbe infrastructure:

6. **Medium → Application**: Links medium to use cases
7. **Medium → Physical State**: Links medium to physical form
8. **Dataset → Medium**: Links omics datasets to media used
9. **Medium → Database Reference**: Links to authoritative source databases
10. **Variant → Base Medium**: Links media variants to parent formulations

## Comparison with cmm-ai-automation

| CultureMech | cmm-ai-automation | Notes |
|-------------|-------------------|-------|
| `MediaRecipe` | `GrowthMedium` | Root entity for media |
| `ingredients` field | `has_ingredient_component` | Direct ingredients |
| `solutions` field | `has_solution_component` | Stock solutions |
| `target_organisms` | `Strain.grows_in_medium` | Organism-medium link |
| `medium_type` enum | `medium_type` attribute | COMPLEX, DEFINED, etc. |
| `IngredientDescriptor` | `IngredientComponent` | Reified ingredient usage |
| `SolutionDescriptor` | `SolutionComponent` | Reified solution usage |

## Usage Example

To export KGX edges from a media recipe YAML file:

```bash
# Test on a single file
python src/culturemech/export/kgx_export.py data/normalized_yaml/bacterial/LB_Broth.yaml

# Export all recipes using Koza
just kgx-export
```

## Ontology References

### Predicates

- **METPO:2000517** - "grows in" (organism-medium relationship)
- **biolink:has_part** - Composition relationship (medium→solution, solution→ingredient, medium→ingredient)
- **biolink:has_attribute** - Attribute relationship (medium→type)

### Entity Namespaces

- **NCBITaxon** - Taxonomic identifiers for organisms
- **CHEBI** - Chemical Entities of Biological Interest
- **culturemech** - CultureMech internal identifiers
- **METPO** - Metabolite Profiling Ontology

## Integration with KG-Microbe

These semantic relationships enable:

1. **Growth Prediction**: Query which organisms can grow in specific media
2. **Media Recommendation**: Find suitable media for specific organisms
3. **Ingredient Analysis**: Identify common ingredients across media
4. **Media Comparison**: Compare media compositions and complexities
5. **Solution Reuse**: Identify reusable stock solutions across formulations

## References

- [cmm-ai-automation schema](https://github.com/turbomam/cmm-ai-automation/blob/main/src/cmm_ai_automation/schema/cmm_ai_automation.yaml)
- [Biolink Model](https://biolink.github.io/biolink-model/)
- [METPO Ontology](http://purl.obolibrary.org/obo/metpo.owl)
- [KG-Microbe](https://github.com/Knowledge-Graph-Hub/kg-microbe)
