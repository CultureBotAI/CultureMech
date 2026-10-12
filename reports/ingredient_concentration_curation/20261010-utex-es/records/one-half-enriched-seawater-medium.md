# UTEX Enriched Seawater Ingredient Review

- Record: data/normalized_yaml/algae/1_2_Enriched_Seawater.yaml
- ID: CultureMech:000003
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- State: applied locally; claim-specific evidence, not a fully verified formulation
- Before SHA256: 04609b871d0f0fa4f77814ffe19898a095508953abd8288c0a1a10c61c2ed338
- Result SHA256: 06fd83279c46127a17c343dc2c6dd03429609719b7b3b1104c42eb59761422d2

## Source And Scope

The [source ledger](../source-review-v2.json) pins twelve official UTEX recipes, linked stock tables, six visually inspected formulation PDFs and separate chemical identity evidence. Downloaded captures are hash-checked; manually inspected supplier/ChEBI text is explicitly labelled and is not a fabricated HTTP capture. Unknown authors/publication years remain unasserted. Bibliography notes record source type, discovery mode and access date.

Every stored ingredient/stock concentration in this record is listed below. Expanded recipes use absolute seawater and enrichment inputs. ES Fe, P-II and vitamin stocks belong inside the enrichment preparation; their mass concentrations stay stock concentrations. Solvent makeup/carrier totals do not establish fixed pure-water fractions. The dilution recipes retain the explicitly reported 500/500 and 665/335 mL per 1 L total.

| Original field / ingredient | Result field | Before | Applied | Status | Identity | PURL / exact snippet / locator / reasoning |
| --- | --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / dH2O | ingredients[0].concentration | {"unit": "ML_PER_L", "value": "500"} | {"unit": "ML_PER_L", "value": "500"} | evidence_only | unchanged; not separately recertified | {"explanation": "Claim: ingredients[0].concentration. The table gives this aliquot in mL under For 1 L Total; retain the explicitly listed 500/500 mL dilution. Exact component cell: \"sterile dH 2 O\". Locator: Ingredient table row 2, Amount column; component cell quoted separately. ", "locator": "Ingredient table row 2, Amount column; component cell quoted separately.", "reference": "https://utex.org/products/one-half-enriched-seawater-medium", "snippet": "500 mL"} |
| solutions[0].concentration / Enriched Seawater Medium | solutions[0].concentration | {"unit": "ML_PER_L", "value": "500"} | {"unit": "ML_PER_L", "value": "500"} | evidence_only | unchanged; not separately recertified | {"explanation": "Claim: solutions[0].concentration. The table gives this aliquot in mL under For 1 L Total; retain the explicitly listed 500/500 mL dilution. Exact component cell: \"Enriched Seawater Medium\". Locator: Ingredient table row 1, Amount column; component cell quoted separately. ", "locator": "Ingredient table row 1, Amount column; component cell quoted separately.", "reference": "https://utex.org/products/one-half-enriched-seawater-medium", "snippet": "500 mL"} |

## Other Evidenced Changes

The pinned ledger contains exact field operations, stock relocations, chemical identity evidence and relationship-dose notes. Unsupported glycerophosphate identifiers are removed without assigning a substitute; cyanocobalamin and thiamine hydrochloride are separately grounded. Existing curation history and unrelated growth claims are preserved.

## Remaining Issues

- The parent HTML total-volume heading conflicts with the per-liter-of-seawater procedure/PDF. Expanded recipes retain absolute liquid inputs; no measured final volume or final constituent concentrations are inferred.
- The enrichment source lists vitamin doses but omits a later vitamin-addition instruction; no missing step is invented.
- ES Fe formula and Sigma F1513 catalog identity remain unreconciled. Only the source-named ferrous-ammonium-sulfate stock mass is supported; no catalog-based replacement or molar conversion is made.
- The P-II source permits a cobalt sulfate alternative without an exact replacement mass/hydrate. Only the listed cobalt chloride hexahydrate amount is supported.
- No exact glycerophosphate-pentahydrate ontology identifier was established. Unsupported sn-glycerol-3-phosphate assertions are removed; the immutable MIM index remains unchanged.
- Generic lighting, temperature, application and growth claims remain outside this ingredient review; no taxa-media associations are added.
- The 2/3 PDF copyright notice does not establish a publication year for the live HTML. Supplier pages inspected by the web tool are not full downloaded captures.

## Validation

[Preview](../preview-v3.json), [application](../apply.json), [post-edit](../post.json), [references](../references.json), [corpus](../corpus.json), [retention](../reconcile-retention.json) and [checkpoint](../validation.json) record actual outcomes. Pending or failed checks are not passes; report coverage is not full scientific verification. No taxa-media associations added.
