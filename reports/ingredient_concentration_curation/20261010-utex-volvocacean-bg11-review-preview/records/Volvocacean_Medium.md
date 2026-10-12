# Ingredient Concentration Source-Review Preview

- Record: data/normalized_yaml/algae/Volvocacean_Medium.yaml
- ID: CultureMech:000236
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: da64183ae931e08745daf8a9e228f734859d9c26970dffe53616790dfe4c92c8
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old amount / unit / basis | Status | Evidence and arithmetic | Proposed disposition | Action |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Waris Medium | {"value": "800", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "800 mL", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "800 mL / stated 1 L liquid recipe = 800 mL/L. No molecular or stock-strength conversion."} | Retain this source-supported input amount and add scoped evidence in a later guarded proposal. | Read-only preview; no YAML edit or evidence addition. |
| solutions[1].concentration / Euglena Medium | {"value": "200", "unit": "ML_PER_L"} | evidence_only | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "200 mL", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "200 mL / stated 1 L liquid recipe = 200 mL/L. No molecular or stock-strength conversion."} | Retain this source-supported input amount and add scoped evidence in a later guarded proposal. | Read-only preview; no YAML edit or evidence addition. |
| variant_modifications[0] / prepared-medium blend | Blends 800 mL Waris Medium with 200 mL Euglena Medium per liter. | evidence_only | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "Transfer the remaining 800 mL to a 2 L Erlenmeyer flask.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "800 mL remaining Waris + 200 mL prepared Euglena = the stated 1 L liquid recipe.", "additional_snippet": "Transfer 200 mL of the previously prepared Euglena Medium into the flask."} | Retain the 800/200 mL blend text; capture the unadjusted-pH Waris preparation separately. | Read-only preview; no YAML edit or evidence addition. |
| variants[0].modifications (proposed) / optional agar | null | add | {"reference": "https://utex.org/products/volvocacean-medium", "snippet": "For agar add 10.0 grams of agar into the flask; do not mix.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "Keep the literal 10.0 g addition after the one-liter liquid mixture. Do not assert a measured final-volume concentration."} | Propose a separate optional agar formulation, not an ingredient in the liquid parent. | Read-only preview; no YAML edit or evidence addition. |

## Findings

- The source requires Waris Medium without pH adjustment; the current preparation description omits this qualification. Do not infer a final pH or silently treat this as an unchanged prepared Waris formulation.
- The optional 10.0 g agar formulation is absent. Preserve its do-not-mix and subsequent autoclave instructions in any guarded proposal.
- Linked Waris and Euglena ingredient compositions and all unrelated growth/culture-condition claims are not newly certified.

## Provenance And Validation

The whole target record and exact recipe HTML were inspected. Source URL, title, access time, source type, discovery mode, complete recipe text, table cells and capture hash are retained in review.json. Source type is culture collection page; discovery is existing record reference. Named authors, year and DOI are unknown. No linked PDF inspection is claimed.

Every excerpt matches its pinned captured source. Baseline schema and strict validation pass; this does not certify scientific correctness. Nine existing claims and five additional optional-variant claims are covered across this three-record review. The linked BG-11 source is reviewed only as preparation context, not as a completed whole-record review.

No authoritative mutation, applied evidence, canonical coverage or taxa-media association is added. Guarded proposals, variant-scope resolution and post-edit checks remain outstanding.
