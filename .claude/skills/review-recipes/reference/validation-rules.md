# Validation Rule Definitions

*Reference for the **review-recipes** skill — see [`../SKILL.md`](../SKILL.md) for the overview, workflows, and rule summary.*

---

### Rule Definitions

#### P1 - Critical Errors

**Rule P1.1: Schema Validation Failure**
```yaml
id: P1.1
description: Recipe does not validate against LinkML schema
check: linkml-validate fails
impact: Cannot parse or export to KG
fix: Add missing required fields or correct field types
```

**Rule P1.2: Invalid CultureMech ID**
```yaml
id: P1.2
description: CultureMech ID missing, malformed, or duplicate
check: Regex ^CultureMech:\d{6}$, uniqueness check
impact: Identifier conflicts in KG
fix: Mint new ID or correct format
```

**Rule P1.3: Missing Required Fields**
```yaml
id: P1.3
description: Required fields missing (name, medium_type, physical_state)
check: Schema validation via LinkML
impact: Invalid YAML structure
fix: Add missing required fields
```

**Rule P1.4: Invalid Enum Values**
```yaml
id: P1.4
description: Enum values not in schema (medium_type, physical_state, units)
check: Compare against schema enums
impact: Parser failures
fix: Correct to valid enum value
```

**Rule P1.5: Broken Solution Reference**
```yaml
id: P1.5
description: Referenced solution does not exist
check: Solution CultureMech ID lookup fails
impact: Incomplete recipe composition
fix: Create missing solution or update reference
```

#### P2 - High-Priority Warnings

**Rule P2.1: Invalid MediaIngredientMech ID**
```yaml
id: P2.1
description: MediaIngredientMech ID does not exist
check: Lookup in MediaIngredientMech mapped_ingredients.yaml
impact: Broken ingredient linkage
fix: Update to correct MediaIngredientMech ID or remove
```

**Rule P2.2: Invalid CHEBI ID**
```yaml
id: P2.2
description: CHEBI term ID does not exist
check: OAK/OLS lookup returns 404
impact: Broken ontology linkage
fix: Update to correct CHEBI ID or remove
```

**Rule P2.3: Concentration Mismatch**
```yaml
id: P2.3
description: Concentration units incompatible with physical_state
check: E.g., G_PER_L for SOLID medium (should be percentage)
impact: Incorrect concentration interpretation
fix: Convert to appropriate units
```

**Rule P2.4: Category Mismatch**
```yaml
id: P2.4
description: File category doesn't match target_organisms
check: E.g., bacterial/ directory but target is algae
impact: Organizational confusion
fix: Move to correct category directory
```

**Rule P2.5: Duplicate Recipe**
```yaml
id: P2.5
description: Recipe fingerprint matches existing recipe
check: Ingredient composition + concentrations fingerprinting
threshold: > 95% similarity
impact: Data redundancy
fix: Merge duplicates or document as variant
```

#### P3 - Medium-Priority Warnings

**Rule P3.1: Placeholder Text**
```yaml
id: P3.1
description: Placeholder text in ingredients or notes
patterns: "See source", "original amount:", "Unknown", "TBD"
impact: Incomplete data
fix: Extract actual data from source or research
```

**Rule P3.2: Missing MediaIngredientMech Linkage**
```yaml
id: P3.2
description: Ingredient has no mediaingredientmech_term field
check: Ingredient lacks mediaingredientmech_term.id
impact: Reduced traceability to ontologies
fix: Enrich with MediaIngredientMech ID
```

**Rule P3.3: Non-Standard Ingredient Name**
```yaml
id: P3.3
description: Ingredient preferred_term doesn't match MediaIngredientMech
check: Fuzzy match against MediaIngredientMech preferred terms
impact: Inconsistent naming across recipes
fix: Standardize to MediaIngredientMech preferred term
```

**Rule P3.4: Missing Preparation Steps**
```yaml
id: P3.4
description: No preparation_steps field for complex media
check: medium_type = COMPLEX and preparation_steps empty
impact: Incomplete protocol information
fix: Extract from source or add basic steps
```

**Rule P3.5: Sterilization Not Specified**
```yaml
id: P3.5
description: No sterilization method specified
check: sterilization field missing
impact: Critical safety information missing
fix: Add sterilization from preparation_steps or source
```

**Rule P3.6: pH Not Specified**
```yaml
id: P3.6
description: No pH value for DEFINED or SEMI_DEFINED media
check: medium_type in [DEFINED, SEMI_DEFINED] and ph_value missing
impact: Important growth parameter missing
fix: Extract from source or mark as "not specified"
```

#### P4 - Low-Priority Info

**Rule P4.1: Low MediaIngredientMech Coverage**
```yaml
id: P4.1
description: < 50% of ingredients have MediaIngredientMech IDs
check: Count linked vs total ingredients
impact: Potential enrichment opportunity
fix: Run enrichment script on unmapped ingredients
```

**Rule P4.2: Missing Target Organisms**
```yaml
id: P4.2
description: No target_organisms specified
check: target_organisms field empty
impact: Reduced searchability
fix: Extract from source or media name
```

**Rule P4.3: Missing References**
```yaml
id: P4.3
description: No source references (DOI, URL, citation)
check: references field empty
impact: Reduced provenance
fix: Add source reference
```

**Rule P4.4: Incomplete Curation History**
```yaml
id: P4.4
description: Curation history has only creation event
check: curation_history length = 1
impact: No change tracking
fix: Add curation events as changes are made
```

**Rule P4.5: Solution Could Be Extracted**
```yaml
id: P4.5
description: Complex ingredient used in multiple recipes
check: Same multi-component ingredient in 3+ recipes
impact: Duplication instead of reusable solution
fix: Extract to shared solution record
```

---

