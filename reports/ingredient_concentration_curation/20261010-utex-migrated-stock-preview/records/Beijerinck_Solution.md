# UTEX Migrated Stock Source Triage

- Record: data/normalized_yaml/bacterial/Beijerinck_Solution.yaml
- ID: CultureMech:015440
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 29fd4eed1cdb8bc47bc528dc997039f10827fb4ddb54d6a5defd8a139ef78ffd
- State: preview; no recipe changes applied

Source: [Beijerinck's Solution Recipe](https://utex.org/products/beijerincks-solution). Manually inspected official page; no raw capture asserted.

| Field / ingredient | Existing amount | Status | Snippet / basis / locator / calculation / action |
| --- | --- | --- | --- |
| composition[0].concentration / Ammonium chloride | {"value": "8.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/beijerincks-solution", "snippet": "8 g/L", "basis_snippet": "bring total volume to 1.0 Liters", "locator": "Directions; table row 1", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[1].concentration / Calcium chloride dihydrate | {"value": "1.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/beijerincks-solution", "snippet": "1 g/L", "basis_snippet": "bring total volume to 1.0 Liters", "locator": "Directions; table row 2", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[2].concentration / Magnesium sulfate heptahydrate | {"value": "2.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/beijerincks-solution", "snippet": "2 g/L", "basis_snippet": "bring total volume to 1.0 Liters", "locator": "Directions; table row 3", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |

## Open Decisions

- The record's narrative calls the receiving TAP-medium millimolar values final stock concentrations. The official table separates these columns.
- The narrative calcium value also differs from the current receiving-medium column; do not certify or retain that numeric summary as a verified stock molarity.
- Keep source-supported stock mass concentrations; revise the misleading narrative with field-scoped evidence. Do not infer a universal stock dose.

Existing IDs, category, identity mappings and unrelated role/growth claims are not certified by this triage. No new molarity or working-stock dose is inferred. Baseline validation is recorded separately; no application or canonical-coverage increment is asserted.
