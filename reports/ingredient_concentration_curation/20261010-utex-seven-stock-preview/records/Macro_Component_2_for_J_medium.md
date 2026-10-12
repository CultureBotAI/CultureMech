# UTEX Stock Source Triage

- Record: data/normalized_yaml/bacterial/Macro_Component_2_for_J_medium.yaml
- ID: CultureMech:015448
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: f3dd325c3f6c778b79ae16705c09843f93a8d804f62cf3a9c3bb3ecc5a9700ba
- State: preview; no authoritative edits applied

Source: [Macro Component 2 for J Medium Recipe](https://utex.org/products/macro-component-2-for-j-medium). HTTP-200 capture pinned in the source ledger; unknown bibliographic fields are not invented.

| Claim / ingredient | Existing amount | Status | Source and decision |
| --- | --- | --- | --- |
| composition[0].concentration / Disodium EDTA dihydrate | {"value": "4.4", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "4.4 g/L", "basis_snippet": "For 1 L Total", "source_component": "Na2EDTA\u20222H2O(Sigma ED255)", "locator": "formulation table row 1; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |
| composition[1].concentration / Magnesium sulfate heptahydrate | {"value": "10.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "10 g/L", "basis_snippet": "For 1 L Total", "source_component": "MgSO4\u20227H2O(Sigma 230391)", "locator": "formulation table row 2; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |
| composition[2].concentration / Magnesium chloride hexahydrate | {"value": "5.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "5 g/L", "basis_snippet": "For 1 L Total", "source_component": "MgCl2\u20226H2O(Fisher M 33)", "locator": "formulation table row 3; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |
| composition[3].concentration / Ferric chloride hexahydrate | {"value": "0.5", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "0.5 g/L", "basis_snippet": "For 1 L Total", "source_component": "FeCl3\u20226H2O(Sigma F 1513)", "locator": "formulation table row 4; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |

## Remaining Work

- The four mass amounts and printed hydrate names match. The copied molar narrative is not independently certified by that match.
- The pH target is explicit, but exact titrants and a 4 C storage temperature are not established by this recipe.

Identity/role/growth/classification claims are not generally certified by this concentration triage. The baseline checks are in the batch validation receipt. No canonical follow-up coverage increment is counted.
