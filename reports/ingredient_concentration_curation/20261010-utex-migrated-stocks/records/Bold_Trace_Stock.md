# UTEX Stock Concentration Follow-Up

- Record: data/normalized_yaml/bacterial/Bold_Trace_Stock.yaml
- ID: CultureMech:015441
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; unresolved claims retained explicitly
- Input SHA256: 8050c406026827ab030a5b37729397d0f99fe958afbae35c0a2f13d69b6938e7
- Result SHA256: 42ab49e7089a42ded0459d9934173827676715feb486f1d18d9da73e3db08e83
- Record kind: SolutionRecipe; original category and permanent identifiers unchanged
- Source: https://utex.org/products/bbm-bold-trace-stock-solution
- Source capture SHA256: 21688e594240b16724b04cd77fdb2899551d3753e35e28129f57f57fd2035f6b

| Field / Ingredient | Old and retained amount | Disposition | Exact snippet / basis / locator | Action and calculation |
| --- | --- | --- | --- | --- |
| composition[0].concentration / Sulfuric acid (concentrated) | {"unit": "ML_PER_L", "value": "10"} | verified; scoped evidence added | {"basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 1", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "10-mL", "source_component": "H2SO4 conc."} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[1].concentration / Zinc sulfate heptahydrate | {"unit": "G_PER_L", "value": "8.82"} | verified; scoped evidence added | {"basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 2", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "8.82 g", "source_component": "ZnSO4\u20227H2O"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[2].concentration / Manganese chloride tetrahydrate | {"unit": "G_PER_L", "value": "1.44"} | conflict; PARTIAL | {"basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 3", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "1.44 g", "source_component": "MnCl\u20224H2O"} | {"action": "Added scoped PARTIAL evidence; existing amount and identity remain unresolved", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[3].concentration / Molybdenum trioxide | {"unit": "G_PER_L", "value": "0.71"} | verified; scoped evidence added | {"basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 4", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "0.71 g", "source_component": "MoO3"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[4].concentration / Copper sulfate pentahydrate | {"unit": "G_PER_L", "value": "1.57"} | verified; scoped evidence added | {"basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 5", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "1.57 g", "source_component": "CuSO4\u20225H2O"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |
| composition[5].concentration / Cobalt nitrate hexahydrate | {"unit": "G_PER_L", "value": "0.49"} | verified; scoped evidence added | {"basis_snippet": "Bring total volume to 1 L", "locator": "Directions; table row 6", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "0.49 g", "source_component": "Co(NO3)2\u20226H2O"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |

## Context Correction

{"explanation": "Supports the source-discrepancy disposition in notes, not the numeric concentration columns. Directions state 'Bring total volume to 1 L'. For example, the zinc Amount cell is '8.82 g' but its Stock Solution Concentration cell is '0.44 mg/L'; these are not equivalent for that volume. The unverified micromolar summary is replaced by this explicit conflict; no replacement molarity, density calculation or receiving-medium dose is inferred.", "reference": "https://utex.org/products/bbm-bold-trace-stock-solution", "snippet": "Final concentration listed is for the stock solution.", "supports": "SUPPORT"}

The root notes now distinguish supported stock preparation amounts from unverified or receiving-medium annotations.

## Remaining Scope

Manganese remains unresolved: the source prints MnCl.4H2O, while the record assigns MnCl2.4H2O. The source concentration columns and footnote also conflict with its explicit preparation amounts. The separately cited Fraunhofer PDF remains an uninspected lead for this exact stock.

No organism-medium association, role, identity, structured concentration or working dilution was added. No named author, publication year or DOI is invented; institutional source and discovery metadata are stored on the existing bibliography entry.

## Validation

See [preview](../preview.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The reviewed proposal passes twelve baseline/proposed schema/strict commands and 43 guard tests. Application, readback and repeat no-op pass. A missing, running or failed later receipt is not a pass.

This report covers every structured concentration claim in this stock; report presence does not assert that all claims are resolved.
