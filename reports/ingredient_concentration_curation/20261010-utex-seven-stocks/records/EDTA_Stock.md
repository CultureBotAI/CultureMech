# UTEX Stock Ingredient Follow-Up

- Record: data/normalized_yaml/bacterial/EDTA_Stock.yaml
- ID: CultureMech:015443
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; source and mapping limitations retained explicitly
- Input SHA256: 8745eab4afaedac566f0700e9f7dddee967b8dcb890052ff39bd05cbe2d007b8
- Result SHA256: baf0f0a7eb95f086378a2f9a1e80e79965a52307dd0cfe3b64b6ee7fd4bde364
- Record kind: SolutionRecipe; category and permanent identifiers unchanged
- Source: https://utex.org/products/bbm-edta-stock-solution
- Source capture SHA256: cc7970c540daf775946a30870eda0b2900c5f7c4658870b44b47973601489d58

| Original field / ingredient | Current field | Old amount | Current amount | Disposition | Exact source evidence | Action / calculation |
| --- | --- | --- | --- | --- | --- | --- |
| composition[0].concentration / EDTA (acid form) | composition[0].concentration | {"unit": "G_PER_L", "value": "50.0"} | {"unit": "G_PER_L", "value": "50.0"} | evidence_only | {"basis_snippet": "Bring the total volume to 1 Liter", "locator": "Directions; ingredient item 1 and final-volume instruction", "reference": "https://utex.org/products/bbm-edta-stock-solution", "snippet": "50 grams of EDTA, acid form", "source_component": "EDTA, acid form"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |
| composition[1].concentration / Potassium hydroxide | composition[1].concentration | {"unit": "G_PER_L", "value": "31.0"} | {"unit": "G_PER_L", "value": "31.0"} | evidence_only | {"basis_snippet": "Bring the total volume to 1 Liter", "locator": "Directions; ingredient item 2 and final-volume instruction", "reference": "https://utex.org/products/bbm-edta-stock-solution", "snippet": "31 grams of KOH", "source_component": "KOH"} | {"action": "Added scoped SUPPORT amount evidence; numeric value unchanged", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation."} |

## Supplied Chemical Forms

| Field | Old identity | Current identity | Identity sources / snippets |
| --- | --- | --- | --- |
| composition[0] | {"id": "CHEBI:42191", "label": "EDTA(4-)"} | {"id": "CHEBI:4735", "label": "EDTA (acid form)"} | [{"locator": "Formula field", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:4735", "snippet": "C10H16N2O8"}, {"locator": "Formula field", "reference": "https://www.ebi.ac.uk/chebi/CHEBI:42191", "snippet": "C10H12N2O8"}] |

## Preparation And Stock Context

{"explanation": "Supports notes: free-acid input and KOH preparation, final-volume basis, storage and explicit molarity/speciation hold. Separate source excerpts (Directions/table headings/footnote): 'approximately 900 mL'; '50 grams of EDTA, acid form'; '31 grams of KOH'; 'Bring the total volume to 1 Liter'; '~ 8.5 \u00b5M'; 'darkness at room temperature'", "reference": "https://utex.org/products/bbm-edta-stock-solution", "snippet": "approximately 900 mL", "supports": "SUPPORT"}

The applied root notes retain exact preparation and storage scope without invented titrants or exact freezer/refrigerator temperatures.

## Remaining Scope

The source's approximate micromolar annotation remains inconsistent with its mass preparation. No replacement molarity or resulting solution speciation is inferred; the former disodium-salt assertion is removed. The maintained resolver's exact acid-form query returns the live free-acid ID despite a REJECTED representative legacy row; no broader ambiguous-label override is made.

No organism-medium association or role assignment is added. Numerical mass concentrations are unchanged. All new concentration assertions in this batch are the two source-explicit DAS component-stock strengths; its existing dose fractions are moved to stock descriptors. Bibliographic authors, publication year and DOI remain absent when not established.

## Validation

See [preview](../preview.json), [formatting follow-up](../preview-style.json), [application](../apply.json), [post-edit checks](../post.json), [references](../references.json) and [corpus checks](../corpus.json). The proposal passes 28 baseline/proposed schema/strict commands and 99 guard tests. The independent source audit checks all 36 cohort concentration fields and rejects 92 altered proposals. It distinguishes captured-source snippet checks from manual identity-ledger provenance. Application, readback and repeat no-op pass. Missing, running and failed later receipts are not passes.

Report presence does not assert that every source annotation, ontology mapping or preparation conflict is resolved.
