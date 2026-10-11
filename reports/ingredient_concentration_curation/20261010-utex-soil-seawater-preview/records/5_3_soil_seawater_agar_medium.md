# UTEX Ingredient Concentration Review Preview

- Record: data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml
- ID: CultureMech:000019
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 98fc2daa7e4f8fb3c3220696aff4f26c294316c72c7b99e8a9166808bd50d7c7
- Proposed SHA256: f475c2abb8d6727f39f076ade2f2cd5dfbc0f29f5b9fb6695af000ac9f168e1b
- State: preview; authoritative record unchanged
- Proposal: mutation-preview-v1
- Canonical follow-up coverage increment: 0

| Original field / ingredient | Proposed field | Old value / unit / basis | Proposed value / unit / basis | Status | Source evidence | Planned action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Natural sea-salt | ingredients[0].concentration | {"value": "15", "unit": "G_PER_L"} | {"value": "15", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "15 g/L", "basis_snippet": "For 1 L Total", "locator": "Formulation table row position 2; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Attach source evidence; numerical concentration unchanged. |
| ingredients[1].concentration / Agar | ingredients[1].concentration | {"value": "15", "unit": "G_PER_L"} | {"value": "15", "unit": "G_PER_L", "per_volume": "per liter of prepared Soil+Seawater Medium before salt and agar additions"} | correct | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "Add 15 g of agar into the flask; do not mix.", "basis_snippet": "Filter 1 L of Soil+Seawater Medium to remove soil particles.", "locator": "Directions step 3 (agar addition); step 1 (prepared-medium input volume)", "calculation": "15 g agar / 1 L prepared input medium = 15 g per liter of input medium, not a newly measured final-volume concentration."} | Add the explicit source-input volume basis; numerical amount unchanged. |
| solutions[0].concentration / Soil+Seawater Medium | solutions[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/five-thirds-soil-plus-seawater-agar-medium", "snippet": "1 L", "basis_snippet": "Filter 1 L of Soil+Seawater Medium to remove soil particles.", "locator": "Formulation table row position 1; Directions total-volume heading", "calculation": "No numerical conversion applied"} | Remove the unsupported structured concentration; preserve the literal input in notes and evidence. |

## Source Metadata

Each proposed YAML reference includes the inspected source title, source type, discovery mode and access date. Named authors, publication year and DOI remain unknown where not established; a persistent source URL is supplied instead.

## Proposed Changes

{
  "ingredient_dose_basis_corrections": 1,
  "unsupported_quantity_slots_removed": 1,
  "preparation_descriptions_corrected": 2,
  "ingredient_context_notes_added": 1,
  "stock_context_notes_corrected": 1,
  "new_evidence": 3,
  "bibliographic_entries_enriched": 1,
  "new_curation_history": 1
}

## Validation

All four baseline/proposed CLI schema/strict checks for this record pass. No authoritative write or post-edit/reference-validation pass is claimed. The cohort validation receipt separately records literal-source arithmetic and altered-proposal rejection checks.

- `just validate-schema data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/5_3_soil_seawater_agar_medium.yaml` -> 0
- `just validate-schema reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v1/proposed/5_3_soil_seawater_agar_medium.yaml` -> 0
- `just validate-strict reports/ingredient_concentration_curation/20261010-utex-soil-seawater-preview/mutation-preview-v1/proposed/5_3_soil_seawater_agar_medium.yaml` -> 0

## Remaining Work

This is a concentration/ingredient preview, not certification of unrelated organism, role, salinity or culture-condition assertions. The full-record goal remains incomplete. Preserve source conflicts, identity-ledger access limits and unquantified recipe inputs. The volume-basis consumer patch remains unapplied. Guarded application, post-edit checks, canonical reports and required generated-artifact validation are still required.

The source-triage ledger retains the initial disposition; this report reflects the current proposal version named above.
