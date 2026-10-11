# Ingredient Concentration Source-Review Preview

- Record: data/normalized_yaml/algae/bg_11_0_36_nacl_medium.yaml
- ID: CultureMech:000026
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: b28b8b5c1c6185a8d8c2f41174cca216f60f76663db4c77cd40efb5f86c10df3
- State: Preview only; authoritative YAML unchanged.

| Field / ingredient | Old amount / unit / basis | Status | Evidence and arithmetic | Proposed disposition | Action |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "0.062", "unit": "MOLAR"} | evidence_only | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "0.062 M", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No new numerical conversion; the source separately prints 3.6 g/L and 0.062 M.", "source_mass_snippet": "3.6 g/L"} | Retain the source-printed molarity as a source assertion and attach its formulation-specific evidence; no exact mass-to-molar conversion is certified. | Read-only preview; no YAML edit or evidence addition. |
| solutions[0].concentration / BG-11 Medium | {"value": "1000", "unit": "ML_PER_L"} | unsupported | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "Add NaCl then bring total volume to 1 L with dH2O.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No total prepared-base input dose is established. The linked base begins with approximately 900 mL water and stock additions; do not assume that partial preparation equals 1 L prepared medium.", "context_reference": "https://utex.org/products/bg-11-medium", "context_snippet": "To approximately 900 mL of dH2O add the first 9 components in the order specified while stirring continuously."} | Do not certify the current 1000 mL/L prepared-medium dose. The table labels BG-11 as 1 L, but the instructions stop the base recipe after step one and add salt before final makeup. A guarded proposal should distinguish a recipe base from a measured final carrier fraction. | Read-only preview; no YAML edit or evidence addition. |
| variant_modifications[0] / NaCl supplement | Adds 3.6 g/L NaCl to prepared BG-11 Medium. | evidence_only | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "3.6 g/L", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No conversion; the amount is stated per liter and the liquid directions explicitly require final makeup to 1 L."} | The liquid recipe supports this formulation-specific mass concentration. Preserve it without merging the two salt variants. | Read-only preview; no YAML edit or evidence addition. |
| variants[0].modifications (proposed) / optional agar preparation | null | add | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "In a separate container add 15 g of agar to 500 mL of dH2O.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "The source describes two nominal 500 mL portions and a later sterile supplement. Preserve the literal 15 g addition rather than infer final measured volume."} | Keep a separate agar formulation with its own preparation steps; do not insert agar into the liquid parent. | Read-only preview; no YAML edit or evidence addition. |
| variants[0].modifications (proposed thiosulfate context) / agar-only sodium thiosulfate | null | unsupported | {"reference": "https://utex.org/products/bg-11-1-plus-0-point-36-percent-nacl-medium", "snippet": "Add sterile Sodium Thiosulfate to agar solution and mix well.", "basis_snippet": "For 1 L Total", "locator": "#recipe, composition table and Directions", "calculation": "No dose selected or converted from the linked base. Never treat this missing local amount as zero.", "context_reference": "https://utex.org/products/bg-11-medium", "context_snippet": "Sodium Thiosulfate Pentahydrate"} | The variant page instructs this addition but gives no local dose. The linked base lists component 10 separately; resolve inheritance and formulation scope before adding a numeric dose. | Read-only preview; no YAML edit or evidence addition. |

## Findings

- The two NaCl amounts are distinct source formulations, not duplicate quantities to average or merge.
- The current structured BG-11 dose conflates partial base preparation with a separately measured liter of prepared medium. Source table and procedural scope must both be retained.
- Agar instructions and the separate sterile sodium-thiosulfate addition are not represented in this liquid record. The linked base is context, not automatic authorization to import every stock dose.
- Existing sodium-chloride ontology/supplier mappings, salinity and growth/culture-condition claims are not independently certified.
- The source title includes BG-11-1, while the current display name says BG-11. The URL/accession and source table identify the inspected record, but the title difference does not authorize inferring nitrogen omission or renaming the medium.

## Provenance And Validation

The whole target record and exact recipe HTML were inspected. Source URL, title, access time, source type, discovery mode, complete recipe text, table cells and capture hash are retained in review.json. Source type is culture collection page; discovery is existing record reference. Named authors, year and DOI are unknown. No linked PDF inspection is claimed.

Every excerpt matches its pinned captured source. Baseline schema and strict validation pass; this does not certify scientific correctness. Nine existing claims and five additional optional-variant claims are covered across this three-record review. The linked BG-11 source is reviewed only as preparation context, not as a completed whole-record review.

No authoritative mutation, applied evidence, canonical coverage or taxa-media association is added. Guarded proposals, variant-scope resolution and post-edit checks remain outstanding.
