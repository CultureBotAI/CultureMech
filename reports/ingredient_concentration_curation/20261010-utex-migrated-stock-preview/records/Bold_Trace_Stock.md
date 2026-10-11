# UTEX Migrated Stock Source Triage

- Record: data/normalized_yaml/bacterial/Bold_Trace_Stock.yaml
- ID: CultureMech:015441
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 8050c406026827ab030a5b37729397d0f99fe958afbae35c0a2f13d69b6938e7
- State: preview; no recipe changes applied

Source: [BBM Bold Trace Stock Solution Recipe](https://utex.org/products/bbm-bold-trace-stock-solution). Manually inspected official page; no raw capture asserted.

| Field / ingredient | Existing amount | Status | Snippet / basis / locator / calculation / action |
| --- | --- | --- | --- |
| composition[0].concentration / Sulfuric acid (concentrated) | {"value": "10", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "10-mL", "basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 1", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[1].concentration / Zinc sulfate heptahydrate | {"value": "8.82", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "8.82 g", "basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 2", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[2].concentration / Manganese chloride tetrahydrate | {"value": "1.44", "unit": "G_PER_L"} | conflict | {"reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "1.44 g", "basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 3", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[3].concentration / Molybdenum trioxide | {"value": "0.71", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "0.71 g", "basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 4", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[4].concentration / Copper sulfate pentahydrate | {"value": "1.57", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "1.57 g", "basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 5", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |
| composition[5].concentration / Cobalt nitrate hexahydrate | {"value": "0.49", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "0.49 g", "basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 6", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |

## Open Decisions

- Use the explicit preparation amounts and final one-liter volume as the stock-mass basis, not the separate concentration columns.
- The current official page prints MnCl followed by four waters, while the record assigns manganese(II) chloride tetrahydrate. Hold that supplied-form concentration claim; do not silently insert the missing chlorine subscript.
- The table concentration columns and stock-solution footnote need a separate discrepancy disposition. Do not promote the stored micromolar narrative or derive a working-stock dilution from them.
- The additional Fraunhofer PDF in the record remains an uninspected lead in this triage.

Existing IDs, category, identity mappings and unrelated role/growth claims are not certified by this triage. No new molarity or working-stock dose is inferred. Baseline validation is recorded separately; no application or canonical-coverage increment is asserted.
