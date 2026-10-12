# UTEX Stock Ingredient Follow-Up

- Record: data/normalized_yaml/bacterial/DAS_Macro_Solution.yaml
- ID: CultureMech:015444
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; source and mapping limitations retained explicitly
- Input SHA256: 2dd1cff4bf6100645cea83a4f409fc6fd9ad6d1ada7de09ea1acd8462734bbb7
- Result SHA256: 15e119555eaf5a25e68b5b9b65da4fa078c8608dacb194e5ea62bbc7a9a92b96
- Record kind: SolutionRecipe; category and permanent identifiers unchanged
- Source: https://utex.org/products/das-macro-solution
- Source capture SHA256: 88fe7b8b01113d9c3b12c3eb41f5b7fab74d53ea661fa2bb9a9a49a3fc217a2c

| Original field / ingredient | Current field | Old amount | Current amount | Disposition | Exact source evidence | Action / calculation |
| --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Sodium nitrate (0.70 M stock) | solutions[0].concentration | {"unit": "PERCENT_V_V", "value": "25.0"} | {"unit": "PERCENT_V_V", "value": "25.0"} | correct | {"basis_snippet": "For 40 mL total", "locator": "formulation table row 1; Amount column and volume heading", "reference": "https://utex.org/products/das-macro-solution", "snippet": "10 mL/3 L", "source_component": "NaNO3*autoclave before adding*(Fisher BP360)"} | {"action": "Relocated prepared-stock dose from pure-ingredient composition to nested stock descriptor", "calculation": "10 mL / 40 mL * 100 = 25.0% prepared-stock volume fraction; not pure-solute percent and not final DAS concentration."} |
| composition[1].concentration / Disodium phosphate heptahydrate (0.02 M stock) | solutions[1].concentration | {"unit": "PERCENT_V_V", "value": "75.0"} | {"unit": "PERCENT_V_V", "value": "75.0"} | correct | {"basis_snippet": "For 40 mL total", "locator": "formulation table row 2; Amount column and volume heading", "reference": "https://utex.org/products/das-macro-solution", "snippet": "30 mL/3 L", "source_component": "Na2HPO4\u20227H2O*autoclave before adding*(Sigma S 9390)"} | {"action": "Relocated prepared-stock dose from pure-ingredient composition to nested stock descriptor", "calculation": "30 mL / 40 mL * 100 = 75.0% prepared-stock volume fraction; not pure-solute percent and not final DAS concentration."} |
| solutions[0].composition[0].concentration / Sodium nitrate | solutions[0].composition[0].concentration | null | {"unit": "MOLAR", "value": "0.70"} | add | {"basis_snippet": "Stock Solution Concentration", "locator": "Table row 1", "reference": "https://utex.org/products/das-macro-solution", "snippet": "0.70 M"} | {"action": "Added source-explicit component stock strength to nested composition", "calculation": "Directly stated component-stock molarity; no final-medium calculation."} |
| solutions[1].composition[0].concentration / Disodium hydrogen phosphate heptahydrate | solutions[1].composition[0].concentration | null | {"unit": "MOLAR", "value": "0.02"} | add | {"basis_snippet": "Stock Solution Concentration", "locator": "Table row 2", "reference": "https://utex.org/products/das-macro-solution", "snippet": "0.02 M"} | {"action": "Added source-explicit component stock strength to nested composition", "calculation": "Directly stated component-stock molarity; no final-medium calculation."} |

## Preparation And Stock Context

{"explanation": "Supports notes and solutions[0].concentration / solutions[1].concentration. Table rows 1 and 2 refer to prepared stocks; the heading fixes the composite volume. Calculation: 10/40*100 = 25.0% v/v and 30/40*100 = 75.0% v/v. The /3 L amount denominator is receiving DAS context, not this composite stock denominator. No component stock quantity is presented as a pure-solute volume percent. Separate source excerpts (Directions/table headings/footnote): 'For 40 mL total'; '10 mL/3 L'; '30 mL/3 L'; 'Stock Solution Concentration'; 'Final Concentration in DAS'; 'autoclave before adding'; 'Aseptically add'; 'Swirl gently'; 'Store at refrigerator temperature.'", "reference": "https://utex.org/products/das-macro-solution", "snippet": "For 40 mL total", "supports": "SUPPORT"}

The applied root notes retain exact preparation and storage scope without invented titrants or exact freezer/refrigerator temperatures.

## Remaining Scope

The phosphate supplied form is established by the UTEX formula and exact supplier product, but an exact heptahydrate ontology ID remains unresolved. The packaged MIM stock label points to an anhydrous ontology term; it is not used as chemical-form evidence. The sodium nitrate label also retains a publication-resolver ambiguity. Existing stock-specific legacy MIM links are retained on the stock descriptors, not copied to pure chemicals.

No organism-medium association or role assignment is added. Numerical mass concentrations are unchanged. All new concentration assertions in this batch are the two source-explicit DAS component-stock strengths; its existing dose fractions are moved to stock descriptors. Bibliographic authors, publication year and DOI remain absent when not established.

## Validation

See [preview](../preview.json), [formatting follow-up](../preview-style.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The proposal passes 28 baseline/proposed schema/strict commands and 99 guard tests. The independent source audit checks all 36 cohort concentration fields and rejects 92 altered proposals. It distinguishes captured-source snippet checks from manual identity-ledger provenance. Application, readback and repeat no-op pass. Missing, running and failed later receipts are not passes.

Report presence does not assert that every source annotation, ontology mapping or preparation conflict is resolved.
