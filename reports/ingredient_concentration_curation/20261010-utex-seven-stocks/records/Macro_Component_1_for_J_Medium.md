# UTEX Stock Ingredient Follow-Up

- Record: data/normalized_yaml/bacterial/Macro_Component_1_for_J_Medium.yaml
- ID: CultureMech:015447
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; source and mapping limitations retained explicitly
- Input SHA256: 93c8cc231e4430446fe9afd0083c9de056b0464691209d5578be1c3972c5a4b0
- Result SHA256: 0fd633702b56a1ce0f7a44b7f94db133445aaf84dcc1e8dba78135bcf7353748
- Record kind: SolutionRecipe; category and permanent identifiers unchanged
- Source: https://utex.org/products/macro-component-1-for-j-medium
- Source capture SHA256: 0007ba35faed70a280137fac984e28b374cfb481eeb79fe7d66742c37e8fb4c9

| Original field / ingredient | Current field | Old amount | Current amount | Disposition | Exact source evidence | Action / calculation |
| --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Sodium nitrate | composition[0].concentration | {"unit": "G_PER_L", "value": "67.0"} | {"unit": "G_PER_L", "value": "67.0"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 1; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "67 g/L", "source_component": "NaNO3(Fisher BP360)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[1].concentration / Disodium phosphate | composition[1].concentration | {"unit": "G_PER_L", "value": "0.67"} | {"unit": "G_PER_L", "value": "0.67"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 2; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "0.67 g/L", "source_component": "Na2HPO4(Sigma S5136)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[2].concentration / Dipotassium phosphate | composition[2].concentration | {"unit": "G_PER_L", "value": "3.8"} | {"unit": "G_PER_L", "value": "3.8"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 3; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "3.8 g/L", "source_component": "K2HPO4(Sigma P 3786)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[3].concentration / Tricine | composition[3].concentration | {"unit": "G_PER_L", "value": "25.0"} | {"unit": "G_PER_L", "value": "25.0"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 4; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "25 g/L", "source_component": "Tricine(Sigma T-5816-256)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |

## Preparation And Stock Context

{"explanation": "Supports notes: exact preparation volume/stage and storage wording; source concentration annotations are not independently promoted. Separate source excerpts (Directions/table headings/footnote): 'approximately 900 mL'; 'Store at refrigerator temperature.'; 'For 1 L Total'; 'Final concentration listed is for the stock solution.'; 'Adjust the pH 8.5 to 8.8.'; 'total volume to 1 Liter'", "reference": "https://utex.org/products/macro-component-1-for-j-medium", "snippet": "approximately 900 mL", "supports": "SUPPORT"}

The applied root notes retain exact preparation and storage scope without invented titrants or exact freezer/refrigerator temperatures.

## Remaining Scope

The source supports pH 8.5-8.8 but not a specific titrating reagent. Printed concentration annotations remain outside independently verified stock-molarity claims.

No organism-medium association or role assignment is added. Numerical mass concentrations are unchanged. All new concentration assertions in this batch are the two source-explicit DAS component-stock strengths; its existing dose fractions are moved to stock descriptors. Bibliographic authors, publication year and DOI remain absent when not established.

## Validation

See [preview](../preview.json), [formatting follow-up](../preview-style.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The proposal passes 28 baseline/proposed schema/strict commands and 99 guard tests. The independent source audit checks all 36 cohort concentration fields and rejects 92 altered proposals. It distinguishes captured-source snippet checks from manual identity-ledger provenance. Application, readback and repeat no-op pass. Missing, running and failed later receipts are not passes.

Report presence does not assert that every source annotation, ontology mapping or preparation conflict is resolved.
