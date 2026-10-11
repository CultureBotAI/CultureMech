# UTEX Stock Source Triage

- Record: data/normalized_yaml/bacterial/Macro_Component_1_for_J_Medium.yaml
- ID: CultureMech:015447
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 93c8cc231e4430446fe9afd0083c9de056b0464691209d5578be1c3972c5a4b0
- State: preview; no authoritative edits applied

Source: [Macro Component 1 for J Medium Recipe](https://utex.org/products/macro-component-1-for-j-medium). HTTP-200 capture pinned in the source ledger; unknown bibliographic fields are not invented.

| Claim / ingredient | Existing amount | Status | Source and decision |
| --- | --- | --- | --- |
| composition[0].concentration / Sodium nitrate | {"value": "67.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "67 g/L", "basis_snippet": "For 1 L Total", "source_component": "NaNO3(Fisher BP360)", "locator": "formulation table row 1; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |
| composition[1].concentration / Disodium phosphate | {"value": "0.67", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "0.67 g/L", "basis_snippet": "For 1 L Total", "source_component": "Na2HPO4(Sigma S5136)", "locator": "formulation table row 2; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |
| composition[2].concentration / Dipotassium phosphate | {"value": "3.8", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "3.8 g/L", "basis_snippet": "For 1 L Total", "source_component": "K2HPO4(Sigma P 3786)", "locator": "formulation table row 3; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |
| composition[3].concentration / Tricine | {"value": "25.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "25 g/L", "basis_snippet": "For 1 L Total", "source_component": "Tricine(Sigma T-5816-256)", "locator": "formulation table row 4; Amount column and volume heading", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |

## Remaining Work

- The four mass amounts match the source. The separate millimolar column and stock footnote need a discrepancy disposition, not an assumed receiving-medium dilution.
- The pH range is explicit, but exact titrants and a 4 C storage temperature are not established by this recipe.

Identity/role/growth/classification claims are not generally certified by this concentration triage. The baseline checks are in the batch validation receipt. No canonical follow-up coverage increment is counted.
