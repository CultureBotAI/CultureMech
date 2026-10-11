# UTEX Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/2x_soil_seawater_medium.yaml
- ID: CultureMech:000016
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 7d8c38a83e3e6f1452567b49cd9a41417f91b0f4a49a481d110c7691eee9cacd
- Proposed SHA256: 43ec2016d58cd4d42d56ff7085963a1df186b1ab9aee264e4cc380a67af298a4
- State: preview; authoritative record unchanged
- Proposal: mutation-preview-v1
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old value / unit / basis | Proposed value / unit / basis | Status | Source evidence | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Green House Soil | ingredients[0].concentration | {"value": "25", "unit": "ML_PER_L"} | {"value": "25", "unit": "ML_PER_L", "per_volume": "per liter of Supplemented Seawater before soil addition"} | correct | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "5 mL/200 mL of Supplemented Seawater", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "5 mL soil / 0.2 L Supplemented Seawater = 25 mL per liter of carrier."} | Add the explicit source-input volume basis; numerical amount unchanged. |
| ingredients[1].concentration / CaCO3 | ingredients[1].concentration | {"value": "0.05", "unit": "MILLIMOLAR"} | {"value": "0.05", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "0.05 mM", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Attach source evidence; numerical concentration unchanged. |
| solutions[0].concentration / Supplemented Seawater | solutions[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/2x-soil-plus-seawater-medium", "snippet": "200 mL", "basis_snippet": "For 200 mL Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Remove the unsupported structured concentration; preserve the literal input in notes and evidence. |
| solutions[0].composition[0].concentration / Pasteurized Seawater | solutions[0].composition[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "900 mL", "basis_snippet": "Bring total volume to 1 L with Pasteurized Seawater.", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Remove the unsupported structured concentration; preserve the literal input in notes and evidence. |
| solutions[0].composition[1].concentration / NaCl | solutions[0].composition[1].concentration | {"value": "23", "unit": "G_PER_L"} | {"value": "23", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "23 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Attach source evidence; numerical concentration unchanged. |
| solutions[0].composition[2].concentration / MgCl2 x 6 H2O | solutions[0].composition[2].concentration | {"value": "5", "unit": "G_PER_L"} | {"value": "5", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "5 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 3; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Attach source evidence; numerical concentration unchanged. |
| solutions[0].composition[3].concentration / Na2SO4 | solutions[0].composition[3].concentration | {"value": "4", "unit": "G_PER_L"} | {"value": "4", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/supplemented-seawater", "snippet": "4 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 4; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Attach source evidence; numerical concentration unchanged. |

## Source Metadata

Each proposed YAML reference includes the inspected source title, source type, discovery mode and access date. Named authors, publication year and DOI remain unknown where not established; a persistent source URL is supplied instead.

## Proposed Changes

{
  "ingredient_dose_basis_corrections": 1,
  "unsupported_quantity_slots_removed": 2,
  "preparation_descriptions_corrected": 1,
  "ingredient_context_notes_corrected": 3,
  "stock_context_notes_corrected": 1,
  "new_evidence": 7,
  "bibliographic_entries_enriched": 2,
  "new_curation_history": 1
}

## Validation

All four baseline/proposed CLI schema/strict checks for this record pass. No authoritative write or post-edit/reference-validation pass is claimed. The cohort validation receipt separately records literal-source arithmetic and altered-proposal rejection checks.

- `just validate-schema data/normalized_yaml/algae/2x_soil_seawater_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/2x_soil_seawater_medium.yaml` -> 0
- `just validate-schema reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v1/proposed/2x_soil_seawater_medium.yaml` -> 0
- `just validate-strict reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v1/proposed/2x_soil_seawater_medium.yaml` -> 0

## Remaining Work

This is a concentration/ingredient preview, not certification of unrelated organism, role, salinity or culture-condition assertions. The full-record goal remains incomplete. Preserve source conflicts, identity-ledger access limits and unquantified recipe inputs. The volume-basis consumer patch remains unapplied. Guarded application, post-edit checks, canonical reports and required generated-artifact validation are still required.

The source-triage ledger retains the initial disposition; this report reflects the current proposal version named above.
