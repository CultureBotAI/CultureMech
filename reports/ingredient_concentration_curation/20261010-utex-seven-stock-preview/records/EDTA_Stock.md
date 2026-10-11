# UTEX Stock Source Triage

- Record: data/normalized_yaml/bacterial/EDTA_Stock.yaml
- ID: CultureMech:015443
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 8745eab4afaedac566f0700e9f7dddee967b8dcb890052ff39bd05cbe2d007b8
- State: preview; no authoritative edits applied

Source: [BBM EDTA Stock Solution Recipe](https://utex.org/products/bbm-edta-stock-solution). HTTP-200 capture pinned in the source ledger; unknown bibliographic fields are not invented.

| Claim / ingredient | Existing amount | Status | Source and decision |
| --- | --- | --- | --- |
| composition[0].concentration / EDTA (acid form) | {"value": "50.0", "unit": "G_PER_L"} | conflict | {"reference": "https://utex.org/products/bbm-edta-stock-solution", "snippet": "50 grams of EDTA, acid form", "basis_snippet": "Bring the total volume to 1 Liter", "source_component": "EDTA, acid form", "locator": "Directions; ingredient item 1 and final-volume instruction", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "Source specifies EDTA acid form; the record assigns EDTA(4-). Supplied-form identity needs correction with ontology evidence before approving the complete claim.", "action_taken": "none; read-only source triage"} |
| composition[1].concentration / Potassium hydroxide | {"value": "31.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-edta-stock-solution", "snippet": "31 grams of KOH", "basis_snippet": "Bring the total volume to 1 Liter", "source_component": "KOH", "locator": "Directions; ingredient item 2 and final-volume instruction", "calculation": "Direct g/L source amount, or grams per explicit one-liter total; no molecular-weight or working-dilution calculation.", "reason": "The current mass amount and named supplied form match this source row; add scoped evidence after full review.", "action_taken": "none; read-only source triage"} |

## Remaining Work

- The approximate 8.5 micromolar source parenthetical is not promoted to verified stock molarity.
- The narrative asserts primarily disodium EDTA although the inspected formulation lists EDTA acid and KOH. No sodium-containing ingredient or resulting solution speciation is established; do not invent a replacement salt.

Identity/role/growth/classification claims are not generally certified by this concentration triage. The baseline checks are in the batch validation receipt. No canonical follow-up coverage increment is counted.
