# Applied UTEX Ingredient Concentration Review

- Record: data/normalized_yaml/algae/1_4_erdschreibers_medium.yaml
- ID: CultureMech:000008
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Baseline SHA256: 099df487d9f9abf468f4443d41326bae186bf856a22ac02e5a2476422ea5780e
- Applied SHA256: b72e76be2b393f21050d9ec3e7cefb19472e1a1f9c49211d4ce15dc6445375c0
- State: applied locally; all-record review incomplete

| Original field / ingredient | Applied field | Old amount / unit / basis | Applied amount / unit / basis | Review status | Source evidence, locator and arithmetic | Action |
| --- | --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Erdschreiber's Medium | solutions[0].concentration | {"value": "250", "unit": "ML_PER_L"} | {"value": "250", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-fourth-erdschreibers-medium", "snippet": "250 mL", "component_snippet": "Erdschreiber's Medium", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "250 mL / 1 L total = 250 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "The UTEX composition table specifies 250 mL Erdschreiber's Medium and 750 mL sterile dH2O for 1 L total (1:3 by input volume), whereas its introductory prose says 1:4. Retained quantities follow the explicit table; the source ratio conflict remains unresolved."} | Applied exact reviewed proposal. Retain quantity and attach exact source evidence. |
| ingredients[0].concentration / dH2O | ingredients[0].concentration | {"value": "750", "unit": "ML_PER_L"} | {"value": "750", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/one-fourth-erdschreibers-medium", "snippet": "750 mL", "component_snippet": "sterile dH2O", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table, Amount column", "calculation": "750 mL / 1 L total = 750 mL/L; the 1 L basis is explicitly stated by the recipe, not assumed.", "unresolved": "The UTEX composition table specifies 250 mL Erdschreiber's Medium and 750 mL sterile dH2O for 1 L total (1:3 by input volume), whereas its introductory prose says 1:4. Retained quantities follow the explicit table; the source ratio conflict remains unresolved."} | Applied exact reviewed proposal. Retain quantity and attach exact source evidence. |

## Provenance

Changed claims have scoped source-URL and snippet evidence in the YAML. Reference metadata retains inspected source titles, culture-collection-page type, discovery mode and access date. Authors, publication year and DOI remain unknown where not established; no identifiers are fabricated. This review uses HTML, not claimed inspection of linked PDFs.

## Verification

Baseline/proposed and actual post-edit schema/strict checks pass. Guarded application, exact readback and repeat no-op pass. The proposal source checks independently verify retained amounts and bases against captured tables and reject altered values, units, bases, evidence or history.

All eighteen unchanged proposals passed ninety fresh-source checks with the isolated UTEX parser: 69 snippets and 21 titles. That parser is not installed because broader corpus compatibility issues remain open. Its pass is not an installed-reference-CLI pass. Actual installed reference gates, corpus tests and generated-output checks are reported separately in the batch receipts and README.

- `just validate-schema data/normalized_yaml/algae/1_4_erdschreibers_medium.yaml` -> 0
- `just validate-strict data/normalized_yaml/algae/1_4_erdschreibers_medium.yaml` -> 0

## Remaining Scope

Source-printed molarities are source assertions, not independently certified conversions. Unresolved final-volume and source-ratio conflicts are retained. Linked parent composition, unrelated ontology, growth, organism, role, salinity and culture-condition assertions are unchanged and not newly certified. No taxa-media associations are added. Canonical report presence is not full scientific verification or publication readiness.

The quarter-strength table gives 250 mL plus 750 mL (1:3), while its prose says 1:4. The evidence and notes preserve this unresolved conflict.
