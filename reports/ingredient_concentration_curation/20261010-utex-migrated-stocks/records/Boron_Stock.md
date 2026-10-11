# UTEX Stock Concentration Follow-Up

- Record: data/normalized_yaml/bacterial/Boron_Stock.yaml
- ID: CultureMech:015442
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; unresolved claims retained explicitly
- Input SHA256: 95a4a27a93e886f3cf6b83369044354b827d7e451ed81033d3bd7fb6d31939e7
- Result SHA256: ae39d6f354d2122d6e3d4a1984170933f2f37ba598926c9e872c236116971a05
- Record kind: SolutionRecipe; original category and permanent identifiers unchanged
- Source: https://utex.org/products/bbm-boron-stock-solution
- Source capture SHA256: 4d63765d3321938fc4f6cb56aa8614e05f56bf7c2d8a96c84626da3ea8ccdbd3

| Field / Ingredient | Old and retained amount | Disposition | Exact snippet / basis / locator | Action and calculation |
| --- | --- | --- | --- | --- |
| composition[0].concentration / Boric acid | {"unit": "G_PER_L", "value": "11.0"} | verified; scoped evidence added | {"basis_snippet": "Bring the total volume to 1 Liter", "locator": "Directions items 1 and 2", "reference": "https://utex.org/products/bbm-boron-stock-solution", "snippet": "11 g", "source_component": "H3BO3"} | {"action": "Added scoped SUPPORT evidence; numeric value retained", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume."} |

## Context Correction

{"explanation": "Supports documenting the source discrepancy in notes, not approving that molarity. Directions separately say 'dissolve 11 g of H3BO3' and 'Bring the total volume to 1 Liter'. The structured 11.0 g/L amount retains its precision and explicit final-volume basis; the inconsistent parenthetical is identified as unverified without an invented replacement.", "reference": "https://utex.org/products/bbm-boron-stock-solution", "snippet": "final solution concentration: ~ 9", "supports": "SUPPORT"}

The root notes now distinguish supported stock preparation amounts from unverified or receiving-medium annotations.

## Remaining Scope

The source prints an inconsistent approximate micromolar parenthetical. The explicit 11 g per final liter supports the stored mass amount, not that molarity; no receiving-medium reinterpretation is asserted.

No organism-medium association, role, identity, structured concentration or working dilution was added. No named author, publication year or DOI is invented; institutional source and discovery metadata are stored on the existing bibliography entry.

## Validation

See [preview](../preview.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The reviewed proposal passes twelve baseline/proposed schema/strict commands and 43 guard tests. Application, readback and repeat no-op pass. A missing, running or failed later receipt is not a pass.

This report covers every structured concentration claim in this stock; report presence does not assert that all claims are resolved.
