# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/Polytomella_Medium.yaml
- ID: CultureMech:000186
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 675df02f1e1d671655287d9de0ebc4de067cc1cb72def9685e6d84bff4299819
- Applied SHA256: cd5850bc7d73a9623af6cda491368aaa6a0c823f0d8c44322e465a739436234a
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / dH2O | ingredients[0].notes | {"value": "1000", "unit": "ML_PER_L"} | null | unsupported | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "Bring total volume to 1 L with dH2O.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No final water/carrier fraction can be calculated from an initial portion and unspecified makeup dose."} | Applied exact reviewed proposal. Remove the unsupported final-fraction slot while retaining the source preparation input in notes. |
| ingredients[1].concentration / Yeast extract | ingredients[1].concentration | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "1 g/L", "component_snippet": "Yeast extract(Bacto, Difco)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| ingredients[2].concentration / Tryptone | ingredients[2].concentration | {"value": "1", "unit": "G_PER_L"} | {"value": "1", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "1 g/L", "component_snippet": "Tryptone(Sigma T 9410)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| ingredients[3].concentration / Sodium acetate | ingredients[3].concentration | {"value": "24.4", "unit": "MILLIMOLAR"} | {"value": "24.4", "unit": "MILLIMOLAR"} | evidence_only | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "24.4 mM", "component_snippet": "Sodium acetate(Fisher BP 333)", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Directly retain the source table value and unit; no mass/molar conversion is performed. The printed rounded molarity is a source assertion, not an independent certification of molecular weight or supplied chemical identity."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| variants[0].modifications / agar | variants[0].modifications | null | ["After making up the liquid recipe to 1 L, add 15 g agar; do not mix."] | add | {"reference": "https://utex.org/products/polytomella-medium", "snippet": "For 1.5% agar medium add 15 grams of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Applied exact reviewed proposal. Preserve as an inline optional formulation, not a liquid-parent ingredient. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/Polytomella_Medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
