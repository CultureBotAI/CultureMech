# UTEX Stock Ingredient Follow-Up

- Record: data/normalized_yaml/bacterial/Macro_Component_2_for_J_medium.yaml
- ID: CultureMech:015448
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; source and mapping limitations retained explicitly
- Input SHA256: f3dd325c3f6c778b79ae16705c09843f93a8d804f62cf3a9c3bb3ecc5a9700ba
- Result SHA256: 72d769433da0e67c47cdae85185475bb1732c8ff1d5db4fc3d6a7c2d4df8e53e
- Record kind: SolutionRecipe; category and permanent identifiers unchanged
- Source: https://utex.org/products/macro-component-2-for-j-medium
- Source capture SHA256: fd7fd536d4e600319368bc8ace519746f7155f7ccd66d338ef1e245a568d05b1

| Original field / ingredient | Current field | Old amount | Current amount | Disposition | Exact source evidence | Action / calculation |
| --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Disodium EDTA dihydrate | composition[0].concentration | {"unit": "G_PER_L", "value": "4.4"} | {"unit": "G_PER_L", "value": "4.4"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 1; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "4.4 g/L", "source_component": "Na2EDTA\u20222H2O(Sigma ED255)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[1].concentration / Magnesium sulfate heptahydrate | composition[1].concentration | {"unit": "G_PER_L", "value": "10.0"} | {"unit": "G_PER_L", "value": "10.0"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 2; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "10 g/L", "source_component": "MgSO4\u20227H2O(Sigma 230391)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[2].concentration / Magnesium chloride hexahydrate | composition[2].concentration | {"unit": "G_PER_L", "value": "5.0"} | {"unit": "G_PER_L", "value": "5.0"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 3; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "5 g/L", "source_component": "MgCl2\u20226H2O(Fisher M 33)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[3].concentration / Ferric chloride hexahydrate | composition[3].concentration | {"unit": "G_PER_L", "value": "0.5"} | {"unit": "G_PER_L", "value": "0.5"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 4; Amount column and volume heading", "reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "0.5 g/L", "source_component": "FeCl3\u20226H2O(Sigma F 1513)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |

## Preparation And Stock Context

{"explanation": "Supports notes: exact preparation volume/stage and storage wording; source concentration annotations are not independently promoted. Separate source excerpts (Directions/table headings/footnote): 'approximately 850 mL'; 'Store at refrigerator temperature.'; 'For 1 L Total'; 'Final concentration listed is for the stock solution.'; 'Adjust the pH to 7.5.'; 'total volume to 1 Liter'", "reference": "https://utex.org/products/macro-component-2-for-j-medium", "snippet": "approximately 850 mL", "supports": "SUPPORT"}

The applied root notes retain exact preparation and storage scope without invented titrants or exact freezer/refrigerator temperatures.

## Remaining Scope

The source supports pH 7.5 but not a specific titrating reagent. Printed concentration annotations remain outside independently verified stock-molarity claims.

No organism-medium association or role assignment is added. Numerical mass concentrations are unchanged. All new concentration assertions in this batch are the two source-explicit DAS component-stock strengths; its existing dose fractions are moved to stock descriptors. Bibliographic authors, publication year and DOI remain absent when not established.

## Validation

See [preview](../preview.json), [formatting follow-up](../preview-style.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The proposal passes 28 baseline/proposed schema/strict commands and 99 guard tests. The independent source audit checks all 36 cohort concentration fields and rejects 92 altered proposals. It distinguishes captured-source snippet checks from manual identity-ledger provenance. Application, readback and repeat no-op pass. Missing, running and failed later receipts are not passes.

Report presence does not assert that every source annotation, ontology mapping or preparation conflict is resolved.
