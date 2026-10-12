# UTEX Stock Concentration Follow-Up

- Record: data/normalized_yaml/bacterial/Beijerinck_Solution.yaml
- ID: CultureMech:015440
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; unresolved claims retained explicitly
- Input SHA256: 29fd4eed1cdb8bc47bc528dc997039f10827fb4ddb54d6a5defd8a139ef78ffd
- Result SHA256: 864038943b93045b96eeb919bbfc351bae50a094105c98a1c12a6df36c329429
- Record kind: SolutionRecipe; original category and permanent identifiers unchanged
- Source: https://utex.org/products/beijerincks-solution
- Source capture SHA256: 3e76e8157ea31cd07b8840acde2f38afde19df63c0a5dfa49facf82bacb5caab

| Field / Ingredient | Old and retained amount | Disposition | Exact snippet / basis / locator | Action and calculation |
| --- | --- | --- | --- | --- |
| composition[0].concentration / Ammonium chloride | {"unit": "G_PER_L", "value": "8.0"} | verified; scoped evidence added | {"basis_snippet": "bring total volume to 1.0 Liters", "locator": "Directions; table row 1", "reference": "https://utex.org/products/beijerincks-solution", "snippet": "8 g/L", "source_component": "NH4Cl(CAS: 12125-02-9)"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[1].concentration / Calcium chloride dihydrate | {"unit": "G_PER_L", "value": "1.0"} | verified; scoped evidence added | {"basis_snippet": "bring total volume to 1.0 Liters", "locator": "Directions; table row 2", "reference": "https://utex.org/products/beijerincks-solution", "snippet": "1 g/L", "source_component": "CaCl2\u20222H2O(CAS: 10035-04-8)"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[2].concentration / Magnesium sulfate heptahydrate | {"unit": "G_PER_L", "value": "2.0"} | verified; scoped evidence added | {"basis_snippet": "bring total volume to 1.0 Liters", "locator": "Directions; table row 3", "reference": "https://utex.org/products/beijerincks-solution", "snippet": "2 g/L", "source_component": "MgSO4\u20227H2O(CAS: 10034-99-8)"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |

## Context Correction

{"explanation": "Supports correcting the final-stock/receiving-medium distinction in notes. The separate table heading is 'Stock Solution Concentration'; the quoted heading labels a different column. Directions specify 'approximately 800 mL' starting water and 'bring total volume to 1.0 Liters'; the preparation narrative is corrected from 900 to 800 mL starting water. No working dose is inferred.", "reference": "https://utex.org/products/beijerincks-solution", "snippet": "Final Concentration in TAP Medium", "supports": "SUPPORT"}

The root notes now distinguish supported stock preparation amounts from unverified or receiving-medium annotations. Beijerinck starting water is corrected from 900 to the source's approximately 800 mL; no final concentration is recalculated.

## Remaining Scope

All three stored stock mass amounts have scoped source evidence. No stock working dose or replacement molarity is inferred. Other legacy usage and storage assertions were not promoted to verified claims.

No organism-medium association, role, identity, structured concentration or working dilution was added. No named author, publication year or DOI is invented; institutional source and discovery metadata are stored on the existing bibliography entry.

## Validation

See [preview](../preview.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The reviewed proposal passes twelve baseline/proposed schema/strict commands and 43 guard tests. Application, readback and repeat no-op pass. A missing, running or failed later receipt is not a pass.

This report covers every structured concentration claim in this stock; report presence does not assert that all claims are resolved.
