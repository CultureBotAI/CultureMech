# UTEX Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/1_5_soil_seawater_medium.yaml
- ID: CultureMech:000011
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: d2839c884d9988a65f95eb0ae5508e72ceb4faea546c90d7f1f26858f6ab1d70
- Proposed SHA256: 6cf1b3611f8f28202f71db13646da805ba8042f6fd140d89037d3836defc3dd9
- State: preview; authoritative record unchanged
- Proposal: mutation-preview-v1
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old value / unit / basis | Proposed value / unit / basis | Status | Source evidence | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Green House Soil | ingredients[0].notes | {"value": "1 tsp per 200 mL recipe", "unit": "VARIABLE"} | null | schema_gap | {"reference": "https://utex.org/products/one-fifth-soil-plus-seawater-medium", "snippet": "1 tsp", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Remove the unsupported structured concentration; preserve the literal input in notes and evidence. |
| ingredients[1].concentration / CaCO3 | variants[0].modifications | {"value": "0.005", "unit": "G_PER_L"} | ["Optionally add 1 mg calcium carbonate (Fisher C 64) to the source 200 mL recipe before steaming."] | correct | {"reference": "https://utex.org/products/one-fifth-soil-plus-seawater-medium", "snippet": "1 mg", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No new concentration inferred; the source-literal amount belongs only to the optional formulation."} | Relocate the optional carbonate dose from mandatory composition to a source-supported inline variant. |
| ingredients[2].concentration / Pasteurized Seawater | ingredients[1].concentration | {"value": "200", "unit": "ML_PER_L"} | {"value": "200", "unit": "ML_PER_L", "per_volume": "per liter of the combined stated seawater and dH2O input volumes, before soil addition"} | correct | {"reference": "https://utex.org/products/one-fifth-soil-plus-seawater-medium", "snippet": "40 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "40 mL / 0.2 L combined stated liquid inputs = 200 mL/L of input liquids."} | Add the explicit source-input volume basis; numerical amount unchanged. |
| ingredients[3].concentration / dH2O | ingredients[2].concentration | {"value": "800", "unit": "ML_PER_L"} | {"value": "800", "unit": "ML_PER_L", "per_volume": "per liter of the combined stated seawater and dH2O input volumes, before soil addition"} | correct | {"reference": "https://utex.org/products/one-fifth-soil-plus-seawater-medium", "snippet": "160 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 4; Directions total-volume heading", "calculation": "160 mL / 0.2 L combined stated liquid inputs = 800 mL/L of input liquids."} | Add the explicit source-input volume basis; numerical amount unchanged. |

## Source Metadata

Each proposed YAML reference includes the inspected source title, source type, discovery mode and access date. Named authors, publication year and DOI remain unknown where not established; a persistent source URL is supplied instead.

## Proposed Changes

{
  "unsupported_quantity_slots_removed": 1,
  "supplement_nodes_moved_to_variants": 1,
  "inline_variant_options_added": 1,
  "ingredient_dose_basis_corrections": 2,
  "preparation_descriptions_corrected": 3,
  "ingredient_context_notes_corrected": 3,
  "new_evidence": 5,
  "bibliographic_entries_enriched": 1,
  "new_curation_history": 1
}

## Validation

All four baseline/proposed CLI schema/strict checks for this record pass. No authoritative write or post-edit/reference-validation pass is claimed. The cohort validation receipt separately records literal-source arithmetic and altered-proposal rejection checks.

- `just validate-schema data/normalized_yaml/algae/1_5_soil_seawater_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/1_5_soil_seawater_medium.yaml` -> 0
- `just validate-schema reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v1/proposed/1_5_soil_seawater_medium.yaml` -> 0
- `just validate-strict reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v1/proposed/1_5_soil_seawater_medium.yaml` -> 0

## Remaining Work

This is a concentration/ingredient preview, not certification of unrelated organism, role, salinity or culture-condition assertions. The full-record goal remains incomplete. Preserve source conflicts, identity-ledger access limits and unquantified recipe inputs. The volume-basis consumer patch remains unapplied. Guarded application, post-edit checks, canonical reports and required generated-artifact validation are still required.

The source-triage ledger retains the initial disposition; this report reflects the current proposal version named above.
