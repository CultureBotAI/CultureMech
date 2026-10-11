# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/Trebouxia_Medium.yaml
- ID: CultureMech:000234
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 428d227f59192ed58fb087ee1586587197bffdc21f1190b5143be5bcdf42effa
- Applied SHA256: b5d933b4953f956ce390dbebe1991f5e8d4c96032a6a8dfdf2fda2bdc7083efe
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Proteose Peptone | ingredients[0].concentration | {"value": "10", "unit": "G_PER_L"} | {"value": "10", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "10 g/L", "component_snippet": "Proteose Peptone(BD 211684)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| ingredients[1].concentration / Glucose | ingredients[1].concentration | {"value": "0.11", "unit": "MOLAR"} | {"value": "0.11", "unit": "MOLAR"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "0.11 M", "component_snippet": "Glucose(BACTO-dextrose or Sigma D 9634)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| solutions[0].concentration / Bristol Medium | solutions[0].notes | {"value": "825", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "Bring total volume to 1 L with the Bristol Medium saved from step 1.", "basis_snippet": "Transfer approximately 825 mL to a 2-L Erlenmeyer flask.", "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Applied exact reviewed proposal. Remove the unsupported final-fraction slot while retaining the source preparation input in notes. |
| solutions[1].concentration / Soilwater: GR+ Medium | solutions[1].concentration | {"value": "140", "unit": "ML_PER_L"} | {"value": "140", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "140 mL/L", "component_snippet": "Soilwater: GR+ Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| variants[0].modifications / agar | variants[0].modifications | null | ["After making up the liquid recipe to 1 L with Bristol Medium, add 15 g agar; do not mix."] | add | {"reference": "https://utex.org/products/trebouxia-medium", "snippet": "For 1.5% (w/v) agar medium: add 15 g of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Applied exact reviewed proposal. Preserve as an inline optional formulation, not a liquid-parent ingredient. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/Trebouxia_Medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/Trebouxia_Medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
