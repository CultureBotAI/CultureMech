# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/1_2_Erdschreiber_Medium.yaml
- ID: CultureMech:000004
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: c4156563715931d73979f2cb762d335466290a23525c4104dc229e5d41886498
- Applied SHA256: abace84870a563cff878c5e8c414a5f98442b5bb79620e53f14bd188ac173fb2
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Erdschreiber's Medium | solutions[0].concentration | {"value": "500", "unit": "ML_PER_L"} | {"value": "500", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-half-erdschreibers-medium", "snippet": "500 mL", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "500 mL / 1 L total = 500 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Applied exact reviewed proposal. Retain quantity and attach exact source evidence. |
| ingredients[0].concentration / dH2O | ingredients[0].concentration | {"value": "500", "unit": "ML_PER_L"} | {"value": "500", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-half-erdschreibers-medium", "snippet": "500 mL", "component_snippet": "sterile dH2O", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "500 mL / 1 L total = 500 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "None for this input amount and volume basis."} | Applied exact reviewed proposal. Retain quantity and attach exact source evidence. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/1_2_Erdschreiber_Medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/1_2_Erdschreiber_Medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.
