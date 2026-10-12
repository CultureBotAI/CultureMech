# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/Malt_Medium.yaml
- ID: CultureMech:000175
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: ec1cd464850a1c7eff6e1c8cb8ecac5919216619d9e829597de3041174ee85cd
- Applied SHA256: ccd72158dddffb1f292d7cede17497b34ce47c56f4e12a60b981b3b873a55ff6
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Malt extract | ingredients[0].concentration | {"value": "67.2", "unit": "G_PER_L"} | {"value": "67.2", "unit": "G_PER_L", "per_volume": "per liter of starting dH2O before malt extract addition"} | correct | {"reference": "https://utex.org/products/malt-medium", "snippet": "33.6 g/500 mL dH2O", "component_snippet": "Malt extract(Sigma M-0383)", "basis_snippet": "For 500 mL Total", "locator": "#recipe, composition table and Directions", "calculation": "33.6 g / 0.500 L starting water = 67.2 g per liter of starting water. The heading says 500 mL total but no final makeup instruction is given; final concentration remains unresolved."} | Applied exact reviewed proposal. Retain the numeric value with exact source evidence and any explicitly stated preparation basis. |
| variants[0].modifications / agar | variants[0].modifications | null | ["Add 7.5 g agar to the source batch starting with 500 mL dH2O; do not mix. This is an input dose, not a measured final-volume concentration."] | add | {"reference": "https://utex.org/products/malt-medium", "snippet": "For 1.5% agar medium add 7.5 g of agar into the flask; do not mix.", "basis_snippet": "For 500 mL Total", "locator": "#recipe, Directions, optional agar instruction", "calculation": "Literal source batch dose; no universal final concentration is derived."} | Applied exact reviewed proposal. Preserve as an inline optional formulation, not a liquid-parent ingredient. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/Malt_Medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/Malt_Medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
