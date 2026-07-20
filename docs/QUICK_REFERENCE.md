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

### Ingredient roles — three orthogonal facet slots (all multivalued)

The retired flat `role:` slot has been split into three orthogonal facets so
a single ingredient can carry non-conflicting assignments across axes
(e.g. L-cysteine → `AMINO_ACID_SOURCE + SULFUR_SOURCE` nutritionally,
`REDUCING_AGENT` physicochemically, `SUBSTRATE` metabolically).

```yaml
nutritional_roles: [CARBON_SOURCE, ENERGY_SOURCE]
physicochemical_roles: [BUFFER]
cellular_metabolic_roles: [SUBSTRATE]
role_curie: [CHEBI:35225]        # escape hatch for out-of-vocabulary role terms
```

- `nutritional_roles` (`NutritionalRoleEnum`, 12 values) — what element/macronutrient the ingredient supplies: `CARBON_SOURCE`, `NITROGEN_SOURCE`, `SULFUR_SOURCE`, `PHOSPHATE_SOURCE`, `IRON_SOURCE`, `TRACE_ELEMENT`, `VITAMIN_SOURCE`, `AMINO_ACID_SOURCE`, `PROTEIN_SOURCE`, `COFACTOR_PROVIDER`, `ENERGY_SOURCE`, `LIGHT_SOURCE`.
- `physicochemical_roles` (`PhysicochemicalRoleEnum`, 12 values) — chemical/physical function: `BUFFER`, `SOLIDIFYING_AGENT`, `CHELATOR`, `SURFACTANT`, `REDUCING_AGENT`, `OXIDIZING_AGENT`, `PH_INDICATOR`, `REDOX_INDICATOR`, `SELECTIVE_AGENT`, `ANTIFOAM`, `OSMOTIC_AGENT`, `PRECIPITATION_INHIBITOR`.
- `cellular_metabolic_roles` (`CellularMetabolicRoleEnum`, 10 values) — role inside/on the microbe (often organism-conditional): `SUBSTRATE`, `ELECTRON_DONOR`, `ELECTRON_ACCEPTOR`, `COFACTOR`, `PROSTHETIC_GROUP_PRECURSOR`, `MEMBRANE_COMPONENT`, `OSMOPROTECTANT`, `INDUCER`, `INHIBITOR`, `QUENCHER`.

Enum vocabularies are vendored from MediaIngredientMech via `mim_roles.yaml`.

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
  nutritional_roles: [CARBON_SOURCE, ENERGY_SOURCE]
  cellular_metabolic_roles: [SUBSTRATE]
```

### Full Ingredient Enrichment
```yaml
- preferred_term: MgSO4
  concentration: {value: '1', unit: G_PER_L}
  term: {id: CHEBI:31795, label: MgSO4}
  nutritional_roles: [SULFUR_SOURCE, COFACTOR_PROVIDER]  # Mg is a cofactor cation, sulfate supplies sulfur
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
