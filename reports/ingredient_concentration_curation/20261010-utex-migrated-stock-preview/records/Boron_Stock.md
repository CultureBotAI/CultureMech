# UTEX Migrated Stock Source Triage

- Record: data/normalized_yaml/bacterial/Boron_Stock.yaml
- ID: CultureMech:015442
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 95a4a27a93e886f3cf6b83369044354b827d7e451ed81033d3bd7fb6d31939e7
- State: preview; no recipe changes applied

Source: [BBM Boron Stock Solution Recipe](https://utex.org/products/bbm-boron-stock-solution). Manually inspected official page; no raw capture asserted.

| Field / ingredient | Existing amount | Status | Snippet / basis / locator / calculation / action |
| --- | --- | --- | --- |
| composition[0].concentration / Boric acid | {"value": "11.0", "unit": "G_PER_L"} | evidence_only | {"reference": "https://utex.org/products/bbm-boron-stock-solution", "snippet": "11 g", "basis_snippet": "Bring the total volume to 1 Liter", "locator": "Directions items 1 and 2", "calculation": "No numeric change proposed; preparation amount per explicitly stated one-liter total stock volume.", "action_taken": "none; source triage only"} |

## Open Decisions

- The official preparation states eleven grams of boric acid and final one-liter volume, supporting the stored mass concentration.
- The same source supplies the approximate micromolar parenthetical copied into the record. Keep this as an explicit source discrepancy; no replacement molarity or unverified receiving-medium explanation is proposed.

Existing IDs, category, identity mappings and unrelated role/growth claims are not certified by this triage. No new molarity or working-stock dose is inferred. Baseline validation is recorded separately; no application or canonical-coverage increment is asserted.
