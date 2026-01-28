# Quick Reference: New Schema Fields

## Commands

```bash
# Automatic enrichment (recommended first step)
just import-pfas-all

# Preview changes
just import-pfas-roles --dry-run

# Validate
just validate normalized_yaml/bacterial/MyRecipe.yaml
just validate-all
```

---

## Field Reference

### Ingredient.role (multivalued)
```yaml
role: [CARBON_SOURCE, ENERGY_SOURCE]
```
Values: `CARBON_SOURCE`, `NITROGEN_SOURCE`, `MINERAL`, `TRACE_ELEMENT`, `BUFFER`, `VITAMIN_SOURCE`, `SALT`, `PROTEIN_SOURCE`, `AMINO_ACID_SOURCE`, `SOLIDIFYING_AGENT`, `ENERGY_SOURCE`, `ELECTRON_ACCEPTOR`, `ELECTRON_DONOR`, `COFACTOR_PROVIDER`

### Ingredient.cofactors_provided (multivalued)
```yaml
cofactors_provided:
  - preferred_term: Magnesium ion
    term:
      id: CHEBI:18420
      label: magnesium(2+)
    category: METALS
```
Categories: `VITAMINS`, `METALS`, `NUCLEOTIDES`, `ENERGY_TRANSFER`, `OTHER_SPECIALIZED`

### Organism.community_role (multivalued)
```yaml
community_role: [PRIMARY_DEGRADER]
```
Values: `PRIMARY_DEGRADER`, `REDUCTIVE_DEGRADER`, `OXIDATIVE_DEGRADER`, `BIOTRANSFORMER`, `SYNERGIST`, `BRIDGE_ORGANISM`, `ELECTRON_SHUTTLE`, `DETOXIFIER`, `COMMENSAL`, `COMPETITOR`

### Organism.cofactor_requirements (multivalued)
```yaml
cofactor_requirements:
  - cofactor:
      preferred_term: Cobalamin
      category: VITAMINS
    can_biosynthesize: false
    confidence: 0.95
```

### Organism.transporters (multivalued)
```yaml
transporters:
  - name: NarK
    transporter_type: MFS
    substrates: [nitrate]
    direction: import
```
Types: `ABC`, `MFS`, `PTS`, `TONB`, `SYMPORTER`, `ANTIPORTER`, `UNIPORTER`, `PORIN`, `SIDEROPHORE_RECEPTOR`, `DEHALOGENASE`, `FLUORIDE_EXPORTER`

### MediaRecipe.category
```yaml
category: bacterial
```
Values: `bacterial`, `fungal`, `archaea`, `specialized`, `algae`, `imported`

---

## Examples

### Minimal Ingredient Enrichment
```yaml
- preferred_term: Glucose
  concentration: {value: '10', unit: G_PER_L}
  role: [CARBON_SOURCE]
```

### Full Ingredient Enrichment
```yaml
- preferred_term: MgSO4
  concentration: {value: '1', unit: G_PER_L}
  term: {id: CHEBI:31795, label: MgSO4}
  role: [MINERAL, COFACTOR_PROVIDER]
  cofactors_provided:
    - preferred_term: Magnesium ion
      term: {id: CHEBI:18420, label: magnesium(2+)}
      category: METALS
```

### Organism with Community Role
```yaml
target_organisms:
  - preferred_term: E. coli
    term: {id: NCBITaxon:562, label: Escherichia coli}
    community_role: [PRIMARY_DEGRADER]
    target_abundance: 0.7
```

---

## Files

- **Enrichment guide**: `ENRICHMENT_GUIDE.md`
- **Full example**: `normalized_yaml/bacterial/Nitrate_Mineral_Salts_Medium_(NMS)_ENRICHED_EXAMPLE.yaml`
- **Schema**: `src/culturemech/schema/culturemech.yaml`
- **Import scripts**:
  - `src/culturemech/import/import_ingredient_roles.py`
  - `src/culturemech/import/import_cofactors.py`
