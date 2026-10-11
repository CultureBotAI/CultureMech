# UTEX Stock Ingredient Follow-Up

- Record: data/normalized_yaml/bacterial/G9_Trace_Metals_for_J_medium.yaml
- ID: CultureMech:015446
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; source and mapping limitations retained explicitly
- Input SHA256: d2506f286828e0cd6011ab468e62870a7ec7744577df7b6ba6a49bace8e2fa92
- Result SHA256: bfe7caccb79818aedfb700f2b4e73d26e2f735778bbb956edde22aee95779c63
- Record kind: SolutionRecipe; category and permanent identifiers unchanged
- Source: https://utex.org/products/g9-trace-metals-for-j-medium
- Source capture SHA256: 2a290772a1228e384cd08c75050fcd34cdd5e0e391b7f1548d5496d4b1450458

| Original field / ingredient | Current field | Old amount | Current amount | Disposition | Exact source evidence | Action / calculation |
| --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Boric acid | composition[0].concentration | {"unit": "G_PER_L", "value": "3.25"} | {"unit": "G_PER_L", "value": "3.25"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 1; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "3.25 g/L", "source_component": "H3BO3(Baker 0084)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[1].concentration / Manganese sulfate monohydrate | composition[1].concentration | {"unit": "G_PER_L", "value": "1.5"} | {"unit": "G_PER_L", "value": "1.5"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 2; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "1.5 g/L", "source_component": "MnSO4\u2022H2O(Sigma M8179)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[2].concentration / Zinc sulfate heptahydrate | composition[2].concentration | {"unit": "G_PER_L", "value": "0.3"} | {"unit": "G_PER_L", "value": "0.3"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 3; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "0.3 g/L", "source_component": "ZnSO4\u20227H2O(Sigma Z 0251)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[3].concentration / Ammonium molybdate tetrahydrate | composition[3].concentration | {"unit": "G_PER_L", "value": "0.08"} | {"unit": "G_PER_L", "value": "0.08"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 4; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "0.08 g/L", "source_component": "(NH4)6Mo7O24\u20224H2O(Mallinckrodt 3420)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[4].concentration / Copper sulfate pentahydrate | composition[4].concentration | {"unit": "G_PER_L", "value": "0.05"} | {"unit": "G_PER_L", "value": "0.05"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 5; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "0.05 g/L", "source_component": "CuSO4\u20225H2O(MCIB 3M11)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[5].concentration / Cobalt nitrate hexahydrate | composition[5].concentration | {"unit": "G_PER_L", "value": "0.15"} | {"unit": "G_PER_L", "value": "0.15"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 6; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "0.15 g/L", "source_component": "Co(NO3)2\u20226H2O(Mallinckroft 4544)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[6].concentration / Potassium iodide | composition[6].concentration | {"unit": "G_PER_L", "value": "0.01"} | {"unit": "G_PER_L", "value": "0.01"} | evidence_only | {"basis_snippet": "For 1 L Total", "locator": "formulation table row 7; Amount column and volume heading", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "0.01 g/L", "source_component": "KI(Sigma P 4286)"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |

## Preparation And Stock Context

{"explanation": "Supports notes: exact preparation volume/stage and storage wording; source concentration annotations are not independently promoted. Separate source excerpts (Directions/table headings/footnote): 'approximately 900 mL'; 'Store at refrigerator temperature.'; 'For 1 L Total'; 'Final concentration listed is for the stock solution.'; 'total volume to 1 Liter'", "reference": "https://utex.org/products/g9-trace-metals-for-j-medium", "snippet": "approximately 900 mL", "supports": "SUPPORT"}

The applied root notes retain exact preparation and storage scope without invented titrants or exact freezer/refrigerator temperatures.

## Remaining Scope

The printed Final Concentration column and stock footnote are not silently promoted to verified stock molarities or receiving-medium doses. Structured mass amounts remain those in the explicit g/L Amount column.

No organism-medium association or role assignment is added. Numerical mass concentrations are unchanged. All new concentration assertions in this batch are the two source-explicit DAS component-stock strengths; its existing dose fractions are moved to stock descriptors. Bibliographic authors, publication year and DOI remain absent when not established.

## Validation

See [preview](../preview.json), [formatting follow-up](../preview-style.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The proposal passes 28 baseline/proposed schema/strict commands and 99 guard tests. The independent source audit checks all 36 cohort concentration fields and rejects 92 altered proposals. It distinguishes captured-source snippet checks from manual identity-ledger provenance. Application, readback and repeat no-op pass. Missing, running and failed later receipts are not passes.

Report presence does not assert that every source annotation, ontology mapping or preparation conflict is resolved.
