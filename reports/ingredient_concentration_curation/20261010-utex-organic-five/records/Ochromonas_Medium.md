# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/Ochromonas_Medium.yaml
- ID: CultureMech:000184
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: f3c8faa3384ce5e50bcdc4e6d96313c2b4139dee81c3be528d418bea9b893697
- Applied SHA256: 5390b664cd836f885ebe751b9d7e32c26df1b7b28d62737250d6651dfee17b95
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / dH2O | ingredients[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/ochromonas-medium", "snippet": "Bring total volume to 1 L with dH2O.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Applied exact reviewed proposal. Remove the unsupported final-fraction slot while retaining the source preparation input in notes. |
| ingredients[1].concentration / Glucose | ingredients[1].concentration | {"value": "5.6", "unit": "MILLIMOLAR"} | {"value": "5.6", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/ochromonas-medium", "snippet": "5.6 mM", "component_snippet": "Glucose(BACTO-dextrose or Sigma D 9634)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| ingredients[2].concentration / Tryptone | ingredients[2].concentration | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/ochromonas-medium", "snippet": "1 g/L", "component_snippet": "Tryptone (Sigma T 9410)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| ingredients[3].concentration / Yeast extract | ingredients[3].concentration | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/ochromonas-medium", "snippet": "1 g/L", "component_snippet": "Yeast extract(Bacto, Difco)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| solutions[0].concentration / Liver extract infusion | solutions[0].concentration | {"value": "40", "unit": "ML_PER_L"} | {"value": "40", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/ochromonas-medium", "snippet": "40 mL/L", "component_snippet": "Liver extract infusion", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| solutions[0].composition[0].concentration / dH2O | solutions[0].composition[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/liver-extract-infusion", "snippet": "Bring the total volume to 50 mL with dH2O.", "basis_snippet": "For 50 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Applied exact reviewed proposal. Remove the unsupported final-fraction slot while retaining the source preparation input in notes. |
| solutions[0].composition[1].concentration / Liver extract | solutions[0].composition[1].concentration | {"value": "50", "unit": "G_PER_L"} | {"value": "50", "unit": "G_PER_L", "per_volume": "per liter of prepared stock before heating and filtration"} | correct | {"reference": "https://utex.org/products/liver-extract-infusion", "snippet": "2.5 g/50 mL", "component_snippet": "Liver extract(Difco Bacto 0133)", "basis_snippet": "For 50 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "2.5 g / 0.050 L prepared stock = 50 g/L before heating and filtration. No recovery or filtrate concentration is inferred."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/Ochromonas_Medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/Ochromonas_Medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
