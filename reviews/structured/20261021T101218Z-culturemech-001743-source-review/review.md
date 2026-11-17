# Source and formulation review: acetobacterium_fimetarium_medium (CultureMech:001743)

- Review: 20261021T101218Z-culturemech-001743-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T09:56:53Z
- Finished UTC: 2026-10-21T10:12:18Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSMZ 614 base formulation is accessible, but mineral and vitamin stocks are flattened and calcium amounts from two stages are incorrectly summed. The generated target also retains an obsolete duplicate relation to the separately maintained pH 7.5 KOMODO 614.1 variant. Salt/hydrate grounding and provenance need curation; full variant formulation verification remains limited by its inaccessible detail page.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 147; batch 015 item 7 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding fourteen task batches contain 140 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 142 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001743 | data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml | generated | acetobacterium_fimetarium_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001743 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001743 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/147/strict.tsv |
| validate-terms | passed | True | CultureMech:001743 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001743 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001743 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Exact KOMODO 614.1 formulation and preparation | unavailable | True | CultureMech:001743 | Exact public request returned HTTP 403; the captured MediaList supplies identity and pH only. No successful variant recipe retrieval is asserted. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001743.

The four documented recipes completed; interpret the scope of each separately.

### Exact primary labels and current secondary linkage coverage

grounding: supported. Targets: CultureMech:001743.

33 unique asserted CHEBI identifiers resolve with exact labels. Primary linkage 33/34 (97.06%); verified current secondary linkage 31/34 (91.18%). This is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing current secondary keys: []. Legacy links and chemical-form correctness are assessed separately.

### Full history and timezone audit

provenance: concern. Targets: CultureMech:001743.

History event counts: [('target', 11), ('data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml', 10), ('data/normalized_yaml/bacterial/for_dsm_8238.yaml', 10)]. Explicit timestamp defects: [('data/normalized_yaml/bacterial/for_dsm_8238.yaml', 0, '2026-01-27T01:15:03.fZ', 'malformed ISO timestamp'), ('data/normalized_yaml/bacterial/for_dsm_8238.yaml', 1, '2026-02-03T11:19:01.299702', 'timezone absent')]. Historical bytes are assessed as observed; no inferred timezone or retroactive replacement timestamp is supplied.

### Every direct, stock, stock-addition and preparation quantity

quantity: concern. Targets: CultureMech:001743.

Fifty-one literal-source decisions cover all 40 main/mineral/vitamin rows, ten preparation/stock quantity contexts and the exact KOMODO variant pH. All 40 provider row objects are literal raw excerpts; base-source support and unresolved variant claims remain separate.

[{"field_path": "ingredients[0].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "KCl 0.33 g", "source_locator": "DSMZ 614 main table; exact entry KCl 0.33 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 4.3784,\n                        \"optional\": 0\n                    }", "source_amount": 0.33, "source_unit": "g", "provider_g_l": 0.326409, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[1].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "MgCl2 x 6 H2O 0.52 g", "source_locator": "DSMZ 614 main table; exact entry MgCl2 x 6 H2O 0.52 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.52,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.514342,\n                        \"mmol_l\": 2.52993,\n                        \"optional\": 0\n                    }", "source_amount": 0.52, "source_unit": "g", "provider_g_l": 0.514342, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[2].concentration", "decision": "correct", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "CaCl2 x 2 H2O 0.22 g", "source_locator": "DSMZ 614 main table; exact entry CaCl2 x 2 H2O 0.22 g", "explanation": "Source main calcium is 0.22 g and provider main g_l=0.217606. Local 0.317606 instead adds a separate mineral-stock 0.1 g/L without its 10 ml dilution. On provider basis, (0.22 g + 0.1 g/L*0.010 L)/1.011 L=0.218595450 g/L; this arithmetic explains the stage error, not an authorized replacement or measured final concentration.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.22,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.217606,\n                        \"mmol_l\": 1.48016,\n                        \"optional\": 0\n                    }", "source_amount": 0.22, "source_unit": "g", "provider_g_l": 0.217606, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[3].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "NH4Cl 0.33 g", "source_locator": "DSMZ 614 main table; exact entry NH4Cl 0.33 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[3]", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 6.10225,\n                        \"optional\": 0\n                    }", "source_amount": 0.33, "source_unit": "g", "provider_g_l": 0.326409, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[4].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "KH2PO4 0.33 g", "source_locator": "DSMZ 614 main table; exact entry KH2PO4 0.33 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[4]", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.33,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\": 2.39857,\n                        \"optional\": 0\n                    }", "source_amount": 0.33, "source_unit": "g", "provider_g_l": 0.326409, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[5].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Yeast extract 0.50 g", "source_locator": "DSMZ 614 main table; exact entry Yeast extract 0.50 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[5]", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49456,\n                        \"optional\": 0\n                    }", "source_amount": 0.5, "source_unit": "g", "provider_g_l": 0.49456, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "solutions (missing source stock dose)", "decision": "add", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Modified Wolin's mineral solution 10.00 ml", "source_locator": "DSMZ 614 main table; exact entry Modified Wolin's mineral solution 10.00 ml", "explanation": "This exact stock volume addition is missing in all local layers. Restore its relationship to the separately prepared source stock, keeping the dose and stock concentration distinct.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[6]", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 10, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[6].concentration", "decision": "correct", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml", "source_locator": "DSMZ 614 main table; exact entry Sodium resazurin (0.1% w/v) 0.50 ml", "explanation": "The source stock is explicitly 0.1% w/v, so 0.50 ml supplies 0.0005 g. Provider normalization 0.0005 g/1.011 L=0.000494559842 g/L matches local 0.00049456. The numeric mass is consistent; the missing stock strength and dose require representation correction, and the sodium salt identity is a separate grounding issue.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[7]", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "source_amount": 0.5, "source_unit": "ml", "provider_g_l": 0.00049456, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[7].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "NaHCO3 1.00 g", "source_locator": "DSMZ 614 main table; exact entry NaHCO3 1.00 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[8]", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\": 11.7743,\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "g", "provider_g_l": 0.98912, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[8].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "D-Fructose 10.00 g", "source_locator": "DSMZ 614 main table; exact entry D-Fructose 10.00 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[9]", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"D-Fructose\",\n                        \"compound_id\": 33,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\": 54.9023,\n                        \"optional\": 0\n                    }", "source_amount": 10, "source_unit": "g", "provider_g_l": 9.8912, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "solutions (missing source stock dose)", "decision": "add", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Wolin's vitamin solution (10x) 1.00 ml", "source_locator": "DSMZ 614 main table; exact entry Wolin's vitamin solution (10x) 1.00 ml", "explanation": "This exact stock volume addition is missing in all local layers. Restore its relationship to the separately prepared source stock, keeping the dose and stock concentration distinct.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[10]", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[9].concentration", "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Na2S x 9 H2O 0.70 g", "source_locator": "DSMZ 614 main table; exact entry Na2S x 9 H2O 0.70 g", "explanation": "The generated target and DSMZ owner match provider-declared main g/L but lack claim-level source evidence. Preserve original mass and normalization basis. The KOMODO variant owner copies base values, but variant-specific formulation support remains unavailable; do not label that distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[11]", "provider_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.692384,\n                        \"mmol_l\": 2.88275,\n                        \"optional\": 0\n                    }", "source_amount": 0.7, "source_unit": "g", "provider_g_l": 0.692384, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "preparation_steps (missing scoped source water)", "decision": "add", "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 614 main table; exact entry Distilled water 1000.00 ml", "explanation": "The source water volume is missing at this precise main or stock stage. Retain ml and scope; do not treat water alone as measured final volume or collapse three independent solvent additions.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[0].recipe[12]", "provider_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[10].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Nitrilotriacetic acid 1.50 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry Nitrilotriacetic acid 1.50 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "source_amount": 1.5, "source_unit": "g", "provider_g_l": 1.5, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[11].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "MgSO4 x 7 H2O 3.00 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry MgSO4 x 7 H2O 3.00 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "source_amount": 3, "source_unit": "g", "provider_g_l": 3, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[12].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "MnSO4 x H2O 0.50 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry MnSO4 x H2O 0.50 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }", "source_amount": 0.5, "source_unit": "g", "provider_g_l": 0.5, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[13].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "NaCl 1.00 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry NaCl 1.00 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[3]", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "g", "provider_g_l": 1, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[14].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "FeSO4 x 7 H2O 0.10 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry FeSO4 x 7 H2O 0.10 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[4]", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l": 0.1, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[15].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "CoSO4 x 7 H2O 0.18 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry CoSO4 x 7 H2O 0.18 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[5]", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }", "source_amount": 0.18, "source_unit": "g", "provider_g_l": 0.18, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[2].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "CaCl2 x 2 H2O 0.10 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry CaCl2 x 2 H2O 0.10 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. The local calcium 0.317606 g/L sums direct 0.217606 and undiluted stock 0.1. The stock contribution on the provider basis would instead be 0.1*0.010/1.011=0.000989119683 g/L; keep the two source calcium additions separate.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[6]", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "source_amount": 0.1, "source_unit": "g", "provider_g_l": 0.1, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[16].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "ZnSO4 x 7 H2O 0.18 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry ZnSO4 x 7 H2O 0.18 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[7]", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }", "source_amount": 0.18, "source_unit": "g", "provider_g_l": 0.18, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[17].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "CuSO4 x 5 H2O 0.01 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry CuSO4 x 5 H2O 0.01 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[8]", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "source_amount": 0.01, "source_unit": "g", "provider_g_l": 0.01, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[18].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "AlK(SO4)2 x 12 H2O 0.02 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry AlK(SO4)2 x 12 H2O 0.02 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[9]", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }", "source_amount": 0.02, "source_unit": "g", "provider_g_l": 0.02, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[19].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "H3BO3 0.01 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry H3BO3 0.01 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[10]", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "source_amount": 0.01, "source_unit": "g", "provider_g_l": 0.01, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[20].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Na2MoO4 x 2 H2O 0.01 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry Na2MoO4 x 2 H2O 0.01 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[11]", "provider_quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "source_amount": 0.01, "source_unit": "g", "provider_g_l": 0.01, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[21].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "NiCl2 x 6 H2O 0.03 g", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry NiCl2 x 6 H2O 0.03 g", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[12]", "provider_quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }", "source_amount": 0.03, "source_unit": "g", "provider_g_l": 0.03, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[22].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Na2SeO3 x 5 H2O 0.30 mg", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry Na2SeO3 x 5 H2O 0.30 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 0.3 mg equals 0.0003 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[13]", "provider_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }", "source_amount": 0.3, "source_unit": "mg", "provider_g_l": 0.0003, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[23].concentration", "decision": "correct", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Na2WO4 x 2 H2O 0.40 mg", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry Na2WO4 x 2 H2O 0.40 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 0.4 mg equals 0.0004 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[14]", "provider_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }", "source_amount": 0.4, "source_unit": "mg", "provider_g_l": 0.0004, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "preparation_steps (missing scoped source water)", "decision": "add", "stage": "Modified Wolin's mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 614 Modified Wolin's mineral solution subsection; exact entry Distilled water 1000.00 ml", "explanation": "The source water volume is missing at this precise main or stock stage. Retain ml and scope; do not treat water alone as measured final volume or collapse three independent solvent additions.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[1].recipe[15]", "provider_quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[24].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Biotin 20.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Biotin 20.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 20 mg equals 0.02 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[0]", "provider_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "source_amount": 20, "source_unit": "mg", "provider_g_l": 0.02, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[25].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Folic acid 20.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Folic acid 20.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 20 mg equals 0.02 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[1]", "provider_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "source_amount": 20, "source_unit": "mg", "provider_g_l": 0.02, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[26].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Pyridoxine hydrochloride 100.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Pyridoxine hydrochloride 100.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 100 mg equals 0.1 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[2]", "provider_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "source_amount": 100, "source_unit": "mg", "provider_g_l": 0.1, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[27].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Thiamine HCl 50.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Thiamine HCl 50.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[3]", "provider_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "source_amount": 50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[28].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Riboflavin 50.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Riboflavin 50.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[4]", "provider_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "source_amount": 50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[29].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Nicotinic acid 50.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Nicotinic acid 50.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[5]", "provider_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "source_amount": 50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[30].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Calcium D-(+)-pantothenate 50.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Calcium D-(+)-pantothenate 50.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[6]", "provider_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "source_amount": 50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[31].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Vitamin B12 1.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Vitamin B12 1.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 1 mg equals 0.001 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[7]", "provider_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "source_amount": 1, "source_unit": "mg", "provider_g_l": 0.001, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[32].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "p-Aminobenzoic acid 50.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry p-Aminobenzoic acid 50.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[8]", "provider_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "source_amount": 50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "ingredients[33].concentration", "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "(DL)-alpha-Lipoic acid 50.00 mg", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry (DL)-alpha-Lipoic acid 50.00 mg", "explanation": "This source amount belongs to the separate stock, not directly to the main medium. Its local g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations, not measured final concentrations. Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[9]", "provider_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "source_amount": 50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "preparation_steps (missing scoped source water)", "decision": "add", "stage": "10x Wolin vitamin stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 614 Wolin's vitamin solution (10x) subsection; exact entry Distilled water 1000.00 ml", "explanation": "The source water volume is missing at this precise main or stock stage. Retain ml and scope; do not treat water alone as measured final volume or collapse three independent solvent additions.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator": "$.data.solutions[2].recipe[10]", "provider_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "source_amount": 1000, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not independently establish variant equivalence."}, {"field_path": "preparation_steps[0]", "decision": "evidence_only", "stage": "base main sparging atmosphere", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "medium with 100% N2 gas", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "Target and DSMZ owner retain the exact gas fraction. This is preparation metadata, not a demonstrated biological oxygen preference or an absolute gas dose."}, {"field_path": "preparation_steps[0]", "decision": "evidence_only", "stage": "base main sparging duration", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "for 30 - 45 min", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "Retained range is correct; it is sparging time, not incubation or autoclave time."}, {"field_path": "preparation_steps[0]", "decision": "evidence_only", "stage": "separate bicarbonate stock atmosphere", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "80% N2 and 20% CO2 gas atmosphere.", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "The base procedure explicitly distinguishes this mixture from the 100% N2 used for other stocks. Both target and DSMZ owner preserve it; no gas flow is specified."}, {"field_path": "ph_range; preparation_steps[0]", "decision": "evidence_only", "stage": "complete base-medium target pH", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "of complete medium to 6.8 - 7.0, if necessary.", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "Target and DSMZ owner retain the correct target range and conditional adjustment. This does not apply to the distinct pH 7.5 variant or represent measured final pH."}, {"field_path": "preparation_steps[1]", "decision": "correct", "stage": "mineral stock: NTA dissolution before other minerals", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "adjust pH to 6.5 with KOH", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "The literal value is retained but its top-level placement loses stock scope. Preserve it as the first mineral-stock adjustment, not as a second main-medium target."}, {"field_path": "preparation_steps[1]", "decision": "correct", "stage": "mineral stock after adding minerals", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "final to pH 7.0 with KOH.", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "This is the final target pH of the mineral stock, not the main medium. Move the source scope while retaining the exact value."}, {"field_path": "solutions (mineral stock preparation)", "decision": "not_quantified", "stage": "mineral-stock pH adjustments", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "with KOH", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "KOH is specified as titrant, with no dose or stock strength. Preserve the instruction and unresolved quantity; do not invent an added concentration."}, {"field_path": "preparation_steps[0]", "decision": "evidence_only", "stage": "vitamin stock before post-sterilization addition", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Vitamins should be sterilized by filtration.", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "The source filtration exception is retained in target and DSMZ owner. No filter pore size or sterilization temperature is supplied."}, {"field_path": "preparation_steps[0]; solutions", "decision": "not_quantified", "stage": "base additions after main sterilization", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "Before use add vitamins, fructose and sulfide from sterile anoxic stock solutions prepared", "source_locator": "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation": "The separately defined vitamin recipe/dose is quantified above. Additional fructose and sulfide stocks are required but their strength/dose volumes are not supplied; retain source main masses and the preparation requirement without fabricating those stock parameters."}, {"field_path": "parent_media; variant_relationship; synonyms; owner-1.ph_value", "decision": "correct", "stage": "KOMODO 614.1 variant, not base DSMZ 614", "source_reference": "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList", "source_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a", "source_quote": "7.5", "source_locator": "MediaList exact accession 614.1 row, pH column; full literal row retained in evidence komodo", "explanation": "The table explicitly displays variant pH 7.5 and the owner correctly retains it as PH_VARIANT after September repair, but the generated target still calls the variant a source duplicate. Do not replace the correct base range 6.8–7.0 or assume all variant ingredients from the shared link.", "provider_quote": "&lt;TR&gt;\n\t\t\t\t\t&lt;TD width=\"50\"&gt;&lt;a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=614.1' &gt;614.1&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; For DSM 8238&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt; 7.5&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;true&lt;/TD&gt;\n\t\t\t\t\t&lt;TD&gt;false&lt;/TD&gt;\n&lt;TD&gt;&lt;a href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf' &gt;http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf&lt;/a&gt;&lt;/TD&gt;\n\t\t\t\t&lt;/TR&gt;", "owner_decisions": ["evidence_only", "evidence_only"]}, {"field_path": "preparation_steps[0]", "decision": "evidence_only", "stage": "DSMZ 614 base: separate vitamin, fructose and sulfide stocks before their post-sterilization addition", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote": "under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under", "source_locator": "DSMZ 614 page 1 main preparation paragraph; later vitamin, fructose and sulfide stock atmosphere, before the separate bicarbonate-stock clause", "explanation": "The target and DSMZ base owner retain the explicit 100% N2 atmosphere for these later stocks. This is distinct from initial main-medium sparging and from the bicarbonate stock under 80% N2/20% CO2. It supplies no gas flow or absolute gas dose. The unavailable KOMODO 614.1 variant formulation is not verified by this base instruction.", "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit": "The variant owner lacks preparation and its exact detail remains HTTP 403."}]

### Base accession, exact variant metadata and inaccessible detail

identity: concern. Targets: CultureMech:001743.

DSMZ/MediaDive 614 identifies ACETOBACTERIUM FIMETARIUM MEDIUM with pH 6.8–7.0. KOMODO 614.1 is explicitly For DSM 8238 at pH 7.5 and links that base PDF. Current owners separate these as PH_VARIANT, while the generated August target retains reversed SOURCE_DUPLICATE topology and a synonym. The table verifies the pH distinction but not full variant formulation.

### Every direct amount, nested stock and repeated calcium

quantity: concern. Targets: CultureMech:001743.

Nine non-calcium main g/L values agree with provider declarations, including the indicator mass calculated from its stated stock. Fifteen mineral and ten vitamin source components are flattened; mineral calcium is additionally summed with main calcium, leaving 34 local ingredient rows. Exact source doses and all three water quantities are absent. The local 0.317606 calcium value is not a defensible sum across these stages.

### All asserted forms and structures

grounding: concern. Targets: CultureMech:001743.

Explicit nickel hexahydrate maps to unhydrated Cl2Ni, and sodium resazurin maps to neutral C12H7NO4. Other named hydrates match their source forms. The primary explicitly uses D-(+)-calcium pantothenate, so its stereospecified CHEBI:31345 is not the DL mismatch seen in other formulations. DL-alpha-lipoic acid maps to the stereounspecified CHEBI:16494 structure, retaining DL in its preferred term; generic B12 remains broad without inferring cyanocobalamin. Yeast extract remains a mixture.

### Main versus stock preparation and gas context

completeness: concern. Targets: CultureMech:001743.

The target and DSMZ owner correctly retain main gas/time context, different bicarbonate atmosphere, vitamin filtration and main target pH. The mineral-stock pH 6.5 then 7.0 adjustments are retained as an unscoped second main step. The variant owner has no preparation and says Aerobic: Yes; that copied metadata cannot substitute for the base anoxic preparation and its variant-specific meaning remains unresolved.

### Composition, physical state and organism claims

scope: supported. Targets: CultureMech:001743.

COMPLEX/SEMI_DEFINED and LIQUID fit yeast extract plus enumerated salts/vitamins and no solidifier. No target-organism experimental growth, incubation claim or KG match is asserted. For DSM 8238 is a collection-specific label, not evidence of a strain taxonomy identity or experimental growth under every base/variant condition.

### September owner topology and unchanged ingredient claims

provenance: concern. Targets: CultureMech:001743.

All owner ingredient arrays equal the target, including the flattened stocks and summed calcium. The September owner repair changes topology and flags the child ingredients_curated while leaving those ingredient claims unchanged. The generated target ends at August and omits the corrected family links. No layer has claim-level amount/preparation evidence; generic links do not replace it. Historical timestamp defects remain explicit in the separate history audit.

## Findings

### f1: Stock concentrations are flattened and calcium from two stages is summed

blocker / open / confirmed; issue key: CM001743-stock-and-calcium-collapse.

Mineral and vitamin stocks become direct medium ingredients at undiluted stock strength; the main calcium 0.217606 and stock calcium 0.1 g/L are added as 0.317606. Missing 10 ml and 1 ml stock doses, indicator-stock representation, solvent stages and unscoped mineral preparation make this a materially different formulation.

### f2: A pH 7.5 variant is still represented as a duplicate-source synonym

major / open / confirmed; issue key: CM001743-ph-variant-merge.

Current maintained owners and public KOMODO metadata distinguish 614.1 at pH 7.5 from base 614 at pH 6.8–7.0. The generated target still contains obsolete SOURCE_DUPLICATE topology and a synonym, obscuring the pH distinction. Exact variant formulation remains unavailable rather than proven equal.

### f3: Nickel hexahydrate is mapped to unhydrated nickel dichloride

major / open / confirmed; issue key: CM001743-nickel-hydrate.

Source and preferred term specify NiCl2 x 6 H2O; CHEBI:34887 in both primary and secondary links has formula Cl2Ni. Live labels and MIM linkage do not verify hydration.

### f4: Sodium resazurin is mapped to the neutral molecule

major / open / confirmed; issue key: CM001743-resazurin-salt.

The exact primary and provider name sodium resazurin, but CHEBI:8806 encodes C12H7NO4 without sodium. The quantity conversion does not validate this salt mismatch.

### f5: Curated-status and source links do not substantiate the unchanged formulation

minor / open / confirmed; issue key: CM001743-evidence-and-status.

The variant owner received ingredients_curated in a topology-only repair that retained the flattened signature. Target and owners lack narrow source evidence for formulation/preparation. The variant oxygen metadata has no scoped experimental support and its detail page is inaccessible.

### f6: Variant history has malformed and timezone-free events

minor / open / confirmed; issue key: CM001743-owner-timestamp-defects.

The original KOMODO import timestamp ends .fZ and its resolver timestamp has no timezone. Later well-formed September events do not establish those original instants.

## Recommended Actions And Acceptance Checks

### a1

Restore separate main/mineral/vitamin stages and exact doses, preserving original units and solvent basis. Reconcile the calcium additions before any calculation; retain the numerically consistent resazurin mass alongside its missing stock strength/dose. Scope mineral preparation to its stock.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the separately identified pH variant and updated parent/child ownership. Resolve its exact formulation before claiming full equivalence; regenerate only after ingredient and family corrections, using current compatibility guards.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Resolve the exact hexahydrate identity or explicitly retain unresolved grounding, preserving its mineral-stock quantity and hydration.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a4

Resolve the source sodium salt with verified ontology evidence or retain an explicit unresolved mapping; do not substitute neutral resazurin or invent a replacement ID.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a5

Attach source-specific excerpts to corrected base claims and qualify the variant limitations; reconcile the curated-status scope and oxygen metadata without asserting unsupported growth or complete variant verification.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a6

Preserve existing events and append a supported clarification; repair writer serialization separately without fabricating historical times.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/for_dsm_8238.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch015/147/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch015/147/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| id-search | repository checkout; Exact top-level ID lookup | supports | ./data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml:1:id: CultureMech:001743<br>./data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml:1:id: CultureMech:001743<br> |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:131361 resolves to disodium selenite pentahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396", "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"], "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"], "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]} |
| chebi15824 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15824; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15824 resolves to D-fructose; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:57-48-7", "hmdb:HMDB0000660", "kegg.compound:C00095", "metacyc.compound:FRU", "pdb-ccd:FRU", "pubmed:22735334"], "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:12923", "CHEBI:20929", "CHEBI:4118"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15824"], "mass": ["180.156"], "monoisotopic_mass": ["180.06339"]} |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15940 resolves to nicotinic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND607088605", "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014", "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049", "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE", "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870", "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990", "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771", "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271", "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152", "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335", "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411", "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240", "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762", "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686", "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105", "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912", "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula": ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string": ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"], "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]} |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:15956 resolves to biotin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962", "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703", "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756", "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577", "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419", "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839", "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846", "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467", "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119", "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411", "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274", "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550", "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272", "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878", "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838", "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id": ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"], "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"], "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]} |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:16494 resolves to lipoic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4", "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725", "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853", "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula": ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string": ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"], "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]} |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:17015 resolves to riboflavin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981", "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244", "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084", "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF", "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259", "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098", "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891", "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110", "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405", "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358", "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825", "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103", "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225", "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula": ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214", "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string": ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"], "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]} |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:176843 resolves to vitamin B12; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]} |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:26710 resolves to sodium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5", "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL", "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula": ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string": ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"], "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]} |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:27470 resolves to folic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3", "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504", "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539", "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938", "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400", "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531", "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678", "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630", "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562", "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383", "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393", "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"], "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075", "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string": ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"], "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]} |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:30753 resolves to 4-aminobenzoic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:150-13-0", "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392", "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB", "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145", "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283", "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007", "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595", "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula": ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315", "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"], "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"], "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]} |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:30961 resolves to pyridoxine hydrochloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND500675659", "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575", "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511", "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551", "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292", "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"], "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]} |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31206 resolves to ammonium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9", "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"], "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"], "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]} |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31345 resolves to Calcium pantothenate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:137-08-6", "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011", "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula": ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"], "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"], "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]} |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31440 resolves to copper(II) sulfate pentahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481", "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460", "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264", "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"], "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741", "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"], "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"], "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]} |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505", "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222", "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"], "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]} |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32139 resolves to sodium hydrogencarbonate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:144-55-8", "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203", "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"], "generalized_empirical_formula": ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32139"], "inchi_key_string": ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "monoisotopic_mass": ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]} |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32312 resolves to zinc sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0", "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula": ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"], "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"], "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]} |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:32588 resolves to potassium chloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7", "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881", "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula": ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string": ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"], "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]} |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:33118 resolves to boric acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3", "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089", "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula": ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string": ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"], "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]} |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:34887 resolves to nickel dichloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9", "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331", "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317", "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula": ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string": ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"], "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]} |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:44557 resolves to nitrilotriacetic acid; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["beilstein:1710776", "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"], "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889", "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"], "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"], "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]} |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:49105 resolves to thiamine hydrochloride; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND605711145", "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967", "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133", "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197", "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984", "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117", "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula": ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"], "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"], "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]} |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"], "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"], "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]} |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:63939 resolves to sodium tungstate dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2", "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula": ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"], "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"], "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]} |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:75213 resolves to sodium molybdate dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6", "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996", "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string": ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"], "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]} |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:75836 resolves to iron(2+) sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890", "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id": ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"], "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]} |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:76209 resolves to sodium sulfide nonahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4", "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula": ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"], "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"], "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]} |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8", "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"], "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass": ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]} |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86345 resolves to magnesium dichloride hexahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969", "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass": ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]} |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86364 resolves to manganese(II) sulfate monohydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"], "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"], "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]} |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula": ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"], "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"], "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]} |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:8806 resolves to Resazurin; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"], "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"], "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]} |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244; Exact OLS term identifier, canonical label, definition, formula and structure annotations | supports | CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate; canonical label and live status alone do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202", "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"], "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"], "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]} |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary CHEBI key | supports | {"CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier": "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158": [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158", "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type": "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id": "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036": [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036", "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term", "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15824": [{"label": "D-Fructose", "match_type": "preferred_term", "identifier": "CHEBI:15824", "preferred_term": "D-Fructose", "ontology_id": "CHEBI:15824", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term", "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id": "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557": [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier": "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label": "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label": "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term": "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label": "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836", "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term": "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id": "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440": [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440", "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term": "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term", "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label": "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213", "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type": "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id": "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361": [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361", "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term": "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term", "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label": "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term": "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type": "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride", "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier": "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label": "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term": "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term", "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id": "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843": [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843", "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status": "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term": "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type": "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| api | https://mediadive.dsmz.de/rest/medium/614; $.data.medium; all main/mineral/vitamin recipe rows and steps | supports | MediaDive separates main solution 1320, mineral stock 241 and 10x vitamin stock 5980. All 40 source rows are independently inventoried with their original units and stage. |
| primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf; Both DSMZ 614 PDF pages, including complete main/mineral/vitamin tables and associated preparation | supports | The primary defines the base medium plus 10 ml mineral and 1 ml vitamin additions. Stock definitions are printed in the same PDF; no unrelated medium 141 or 120 formulations are imported. |
| komodo | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; MediaList exact ID=614.1 row; accession/name/pH/original-recipe link only | supports | The exact table row supports the linked source identity and displayed pH; it does not supply ingredient amounts or prove a strain-specific recipe is identical to its linked base. |
| variant-detail | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=614.1; Exact KOMODO 614.1 detail request; captured HTTP 403 response | context_only | The exact detail endpoint was inaccessible. Its error body supplies no usable formulation content; public list metadata and the base DSMZ PDF cannot fill that variant-specific evidence gap. |
| quantities | /private/tmp/culturemech-review-work-batch015/147/quantity-inventory.json; Complete source-linked quantity decision inventory | context_only | Fifty-one literal-source decisions cover all 40 main/mineral/vitamin rows, ten preparation/stock quantity contexts and the exact KOMODO variant pH. All 40 provider row objects are literal raw excerpts; base-source support and unresolved variant claims remain separate. |
| writer | src/culturemech/import/mediadive_importer.py; src/culturemech/enrich/dsmz_resolver.py; scripts/cleanup_media_quality.py; scripts/repair_komodo_614_acetobacterium_score10.py; src/culturemech/merge/formulation.py; _parse_api_composition/_parse_api_solutions/_parse_preparation_steps; merge_composition; _merge_ingredient_group; repair_parent/repair_child/_require_record; formulation_content/merge_formulation_evidence | context_only | Current importer separates main and stock additions but concatenates preparation. Resolver copies base composition without preparation. Current cleanup no longer sums conflicting duplicates; this does not erase the observed historical summed-calcium note. September topology repair requires the same 34-item flattened signature and changes family links while adding ingredients_curated to the child; it does not scientifically repair ingredients. Current merge compatibility includes pH and variant relations, so these current owners should not be collapsed as identical. No exact historical execution is inferred solely from current code. |

## Limits And Additional Notes

- The exact KOMODO 614.1 detail request returned HTTP 403. The public MediaList verifies the accession, name For DSM 8238, pH 7.5 and link to DSMZ 614; it does not establish all variant ingredients or preparation. Review of the complete merged family therefore remains partial, while the accessible DSMZ base and its two printed stock definitions are fully assessed.
- Provider main volume 1011 ml and g/L are preserved as provider declarations. The primary separately lists 1000 ml water, 10 ml mineral stock, 1 ml vitamin stock and 0.50 ml indicator stock; these additions are not proof of a measured final volume. Unspecified post-sterilization stock strengths, KOH dose, gas flow and autoclave time/temperature are not invented.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101218Z-culturemech-001743-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: acetobacterium_fimetarium_medium (CultureMech:001743)'
started_at: '2026-10-21T09:56:53Z'
finished_at: '2026-10-21T10:12:18Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The DSMZ 614 base formulation is accessible, but mineral and vitamin stocks
  are flattened and calcium amounts from two stages are incorrectly summed. The generated
  target also retains an obsolete duplicate relation to the separately maintained
  pH 7.5 KOMODO 614.1 variant. Salt/hydrate grounding and provenance need curation;
  full variant formulation verification remains limited by its inaccessible detail
  page.
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
    sha256: 1cb1917838e33759dbfbd8f366651d7d599b1538e3ec15cddd5ff359d8276807
    role: target
  - path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    sha256: e36858423d7579b4fb35f2c9d4ea373b92abce489dc09fa654fab2e26399b923
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    sha256: c3e16e3f94ae357ca1d8e47ad1a58335ae9b8d62977fa2fd5569f8e101f2b6ee
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/repair_komodo_614_acetobacterium_score10.py
    sha256: 209d3c8bd3da4ad66886998de7090328e4e05d060228d551d0d2a50e49a06314
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/export/kgx_export.py
    sha256: d7553aff8f5f026f00765298e436e7cb001b0cdce25b0841e92a5764b4481a70
    role: context
  - path: src/culturemech/import/komodo_importer.py
    sha256: 702733bd580e4ba28f77e183e1e8268f17ea2c1041cf7b3addd92919624f2706
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 147; batch 015 item 7 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding fourteen task batches
    contain 140 ledger-owned validated record reviews; their complete validated lists
    also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 142 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001743
targets:
- target_id: CultureMech:001743
  path: data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  label: acetobacterium_fimetarium_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/147/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/147/strict.tsv"
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - validate-references
- check_id: structured-source-adapter
  name: iModulonDB applicability
  required: false
  status: not_applicable
  summary: The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic
    dataset requiring an iModulonDB cross-check; expression-module membership cannot
    establish this formulation.
  target_ids:
  - CultureMech:001743
- check_id: variant-formulation-source
  name: Exact KOMODO 614.1 formulation and preparation
  required: true
  status: unavailable
  summary: Exact public request returned HTTP 403; the captured MediaList supplies
    identity and pH only. No successful variant recipe retrieval is asserted.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - variant-detail
  - komodo
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T10:12:17Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:12:17Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_8238.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T10:12:17Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:51.751054Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch015/147/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:55.364214Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-015/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch015/147/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:57:59.190336Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T09:58:01.607219Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: id-search
  kind: record_content
  reference: repository checkout
  locator: Exact top-level ID lookup
  accessed_at: '2026-10-21T10:12:17Z'
  support: supports
  summary: './data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml:1:id:
    CultureMech:001743

    ./data/merge_yaml/merged/ACETOBACTERIUM_FIMETARIUM_MEDIUM.yaml:1:id: CultureMech:001743

    '
  search_scope: Whole checkout with rg --no-ignore --hidden; maintained and generated
    layers distinguished.
- evidence_id: chebi131361
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:33:27.980786Z'
  support: supports
  summary: 'CHEBI:131361 resolves to disodium selenite pentahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:26970-82-1", "pubmed:15259772", "pubmed:15559373", "pubmed:16126997", "pubmed:17873396",
    "pubmed:24479345", "pubmed:24716537", "reaxys:14666014", "wikipedia.en:Sodium_selenite"],
    "generalized_empirical_formula": ["5H2O.2Na.O3Se"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:131361"], "inchi_key_string": ["TUANAMBRHOLYTH-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/2Na.H2O3Se.5H2O/c;;1-4(2)3;;;;;/h;;(H2,1,2,3);5*1H2/q2*+1;;;;;;/p-2"],
    "mass": ["263.012"], "monoisotopic_mass": ["263.93363"], "smiles_string": ["O.O.O.O.O.O=[Se]([O-])[O-].[Na+].[Na+]"]}'
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: chebi15824
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15824
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T09:49:54.991959Z'
  support: supports
  summary: 'CHEBI:15824 resolves to D-fructose; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:57-48-7", "hmdb:HMDB0000660",
    "kegg.compound:C00095", "metacyc.compound:FRU", "pdb-ccd:FRU", "pubmed:22735334"],
    "generalized_empirical_formula": ["C6H12O6"], "has_alternative_id": ["CHEBI:12923",
    "CHEBI:20929", "CHEBI:4118"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15824"],
    "mass": ["180.156"], "monoisotopic_mass": ["180.06339"]}'
  snapshot_sha256: f1b16e5f8df6a97d58c27df8ef70df47f270fdb4c70e4d97d0b1c2443705f0c1
- evidence_id: chebi15940
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:11.874279Z'
  support: supports
  summary: 'CHEBI:15940 resolves to nicotinic acid; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND607088605",
    "cas:59-67-6", "chemspider:913", "drugbank:DB00627", "drugcentral:2835", "foodb.food:FDB001014",
    "gmelin:3340", "hmdb:HMDB0001488", "kegg.compound:C00253", "kegg.drug:D00049",
    "knapsack:C00000208", "lincs.smallmolecule:LSM-4676", "metacyc.compound:NIACINE",
    "pdb-ccd:NIO", "pubmed:10540864", "pubmed:113218", "pubmed:12563315", "pubmed:12789870",
    "pubmed:135660", "pubmed:14550884", "pubmed:15037193", "pubmed:15183629", "pubmed:15205990",
    "pubmed:15311728", "pubmed:15627518", "pubmed:15651982", "pubmed:16018787", "pubmed:16172771",
    "pubmed:16322787", "pubmed:16400392", "pubmed:16449845", "pubmed:16767301", "pubmed:16877271",
    "pubmed:16945375", "pubmed:18037924", "pubmed:182198", "pubmed:186078", "pubmed:18993152",
    "pubmed:18996527", "pubmed:19369827", "pubmed:19592242", "pubmed:19678716", "pubmed:19779335",
    "pubmed:20979384", "pubmed:21632263", "pubmed:22116693", "pubmed:22155410", "pubmed:22229411",
    "pubmed:22366213", "pubmed:22458880", "pubmed:22770225", "pubmed:24029555", "pubmed:24568240",
    "pubmed:24675661", "pubmed:24848081", "pubmed:24975217", "pubmed:25040591", "pubmed:25241762",
    "pubmed:25429652", "pubmed:32954525", "pubmed:33273654", "pubmed:33932650", "pubmed:34066686",
    "pubmed:34085526", "pubmed:34117670", "pubmed:4033386", "pubmed:4259917", "pubmed:582105",
    "pubmed:699281", "pubmed:7217784", "pubmed:7581845", "pubmed:8306147", "pubmed:8423912",
    "pubmed:8679452", "pubmed:9107536", "reaxys:109591", "wikipedia.en:Niacin"], "generalized_empirical_formula":
    ["C6H5NO2"], "has_alternative_id": ["CHEBI:25538", "CHEBI:44319", "CHEBI:7559"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:15940"], "inchi_key_string":
    ["PVNIIMVLHYAWGP-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H5NO2/c8-6(9)5-2-1-3-7-4-5/h1-4H,(H,8,9)"],
    "mass": ["123.111"], "monoisotopic_mass": ["123.03203"], "smiles_string": ["O=C(O)c1cccnc1"]}'
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:30.425993Z'
  support: supports
  summary: 'CHEBI:15956 resolves to biotin; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:58-85-5", "chemspider:149962",
    "drugbank:DB00121", "drugcentral:373", "foodb.food:FDB014510", "gmelin:1918703",
    "hmdb:HMDB0000030", "kegg.compound:C00120", "kegg.drug:D00029", "knapsack:C00000756",
    "lincs.smallmolecule:LSM-3994", "metacyc.compound:BIOTIN", "pdb-ccd:BTN", "pmc:PMC8089577",
    "pubmed:10064317", "pubmed:10215065", "pubmed:10577274", "pubmed:11435506", "pubmed:11481419",
    "pubmed:11800048", "pubmed:12055344", "pubmed:12070309", "pubmed:12603856", "pubmed:12803839",
    "pubmed:15012185", "pubmed:15202718", "pubmed:15272000", "pubmed:15690449", "pubmed:15863846",
    "pubmed:15899401", "pubmed:15992684", "pubmed:16011464", "pubmed:16195795", "pubmed:16419467",
    "pubmed:16676358", "pubmed:16677798", "pubmed:16704206", "pubmed:16769720", "pubmed:17297119",
    "pubmed:1814646", "pubmed:18202531", "pubmed:18452485", "pubmed:18509457", "pubmed:19212411",
    "pubmed:19319844", "pubmed:19727438", "pubmed:19928962", "pubmed:20967359", "pubmed:20974274",
    "pubmed:2100006", "pubmed:21248194", "pubmed:21356565", "pubmed:21373679", "pubmed:21596550",
    "pubmed:21871906", "pubmed:25515858", "pubmed:33346513", "pubmed:33461365", "pubmed:34077272",
    "pubmed:8333586", "pubmed:8750932", "pubmed:9022537", "pubmed:9038855", "pubmed:9094878",
    "pubmed:9164991", "pubmed:9176832", "pubmed:9371938", "pubmed:9416479", "reaxys:86838",
    "wikipedia.en:Biotin"], "generalized_empirical_formula": ["C10H16N2O3S"], "has_alternative_id":
    ["CHEBI:13905", "CHEBI:22882", "CHEBI:22884", "CHEBI:3108", "CHEBI:41236"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:15956"], "inchi_key_string": ["YBJHBAHKTGYVGT-ZKWXMUAHSA-N"],
    "inchi_string": ["InChI=1S/C10H16N2O3S/c13-8(14)4-2-1-3-7-9-6(5-16-7)11-10(15)12-9/h6-7,9H,1-5H2,(H,13,14)(H2,11,12,15)/t6-,7-,9-/m0/s1"],
    "mass": ["244.316"], "monoisotopic_mass": ["244.08816"], "smiles_string": ["[H][C@]12CS[C@@H](CCCCC(=O)O)[C@@]1([H])NC(=O)N2"]}'
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:13.001958Z'
  support: supports
  summary: 'CHEBI:16494 resolves to lipoic acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["beilstein:122410", "cas:62-46-4",
    "drugbank:DB00166", "drugcentral:4732", "ecmdb:ECMDB01451", "gmelin:720915", "kegg.compound:C00725",
    "kegg.drug:D00086", "pubmed:15328413", "pubmed:7519986", "pubmed:7548757", "reaxys:81853",
    "wikipedia.en:Lipoic_acid", "ymdb:YMDB00334"], "generalized_empirical_formula":
    ["C8H14O2S2"], "has_alternative_id": ["CHEBI:146958", "CHEBI:25058", "CHEBI:6492"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:16494"], "inchi_key_string":
    ["AGBQKNBQESQNJD-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C8H14O2S2/c9-8(10)4-2-1-3-7-5-6-11-12-7/h7H,1-6H2,(H,9,10)"],
    "mass": ["206.332"], "monoisotopic_mass": ["206.04352"], "smiles_string": ["O=C(O)CCCCC1CCSS1"]}'
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:11.583596Z'
  support: supports
  summary: 'CHEBI:17015 resolves to riboflavin; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:83-88-5", "chemspider:431981",
    "drugbank:DB00140", "drugcentral:2834", "foodb.food:FDB012160", "hmdb:HMDB0000244",
    "kegg.compound:C00255", "kegg.drug:D00050", "knapsack:C00001552", "lincs.smallmolecule:LSM-4084",
    "metacyc.compound:RIBOFLAVIN", "patent:US2807611", "patent:US2876169", "pdb-ccd:RBF",
    "pubmed:10566553", "pubmed:11399071", "pubmed:11606856", "pubmed:12083520", "pubmed:12354259",
    "pubmed:12927541", "pubmed:14963913", "pubmed:16273338", "pubmed:16460756", "pubmed:16658098",
    "pubmed:182198", "pubmed:18832377", "pubmed:19169240", "pubmed:19212411", "pubmed:19854891",
    "pubmed:22770225", "pubmed:2369885", "pubmed:23818044", "pubmed:24643482", "pubmed:24816110",
    "pubmed:25108762", "pubmed:25468971", "pubmed:25887755", "pubmed:2631092", "pubmed:29937405",
    "pubmed:3142982", "pubmed:33154451", "pubmed:33304888", "pubmed:33886098", "pubmed:33892358",
    "pubmed:34156642", "pubmed:3592624", "pubmed:3878498", "pubmed:4019261", "pubmed:6475825",
    "pubmed:6546833", "pubmed:6650303", "pubmed:7101408", "pubmed:7883462", "pubmed:8487103",
    "pubmed:8604671", "pubmed:8678471", "pubmed:8976642", "pubmed:9184778", "pubmed:9808225",
    "pubmed:9874201", "reaxys:97831", "wikipedia.en:Riboflavin"], "generalized_empirical_formula":
    ["C17H20N4O6"], "has_alternative_id": ["CHEBI:15044", "CHEBI:27299", "CHEBI:45214",
    "CHEBI:529204", "CHEBI:8843"], "has_obo_namespace": ["chebi_ontology"], "id":
    ["CHEBI:17015"], "inchi_key_string": ["AUNGANRZJHBGPY-SCRDCRAPSA-N"], "inchi_string":
    ["InChI=1S/C17H20N4O6/c1-7-3-9-10(4-8(7)2)21(5-11(23)14(25)12(24)6-22)15-13(18-9)16(26)20-17(27)19-15/h3-4,11-12,14,22-25H,5-6H2,1-2H3,(H,20,26,27)/t11-,12+,14-/m0/s1"],
    "mass": ["376.369"], "monoisotopic_mass": ["376.13828"], "smiles_string": ["Cc1cc2nc3c(=O)nc(=O)nc-3n(C[C@H](O)[C@H](O)[C@H](O)CO)c2cc1C"]}'
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:26.997779Z'
  support: supports
  summary: 'CHEBI:176843 resolves to vitamin B12; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:176843"]}'
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:42.219040Z'
  support: supports
  summary: 'CHEBI:26710 resolves to sodium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7647-14-5",
    "gmelin:13673", "kegg.compound:C13563", "kegg.drug:D02056", "metacyc.compound:NACL",
    "ppdb:595", "reaxys:3534976", "wikipedia.en:Sodium_Chloride"], "generalized_empirical_formula":
    ["Cl.Na"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:26710"], "inchi_key_string":
    ["FAPWRFPIFSIZLT-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.Na/h1H;/q;+1/p-1"],
    "mass": ["58.443"], "monoisotopic_mass": ["57.95862"], "smiles_string": ["[Cl-].[Na+]"]}'
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:10.450814Z'
  support: supports
  summary: 'CHEBI:27470 resolves to folic acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["agr:IND606960789", "cas:59-30-3",
    "chemspider:5815", "drugbank:DB00158", "drugcentral:1231", "foodb.food:FDB014504",
    "hmdb:HMDB0000121", "kegg.compound:C00504", "kegg.drug:D00070", "knapsack:C00001539",
    "lincs.smallmolecule:LSM-5355", "metacyc.compound:CPD-12826", "pdb-ccd:FOL", "pubmed:10138938",
    "pubmed:10897644", "pubmed:10958818", "pubmed:11261364", "pubmed:11451208", "pubmed:11959400",
    "pubmed:14387833", "pubmed:15321809", "pubmed:15523939", "pubmed:15754725", "pubmed:15797531",
    "pubmed:15797685", "pubmed:15831910", "pubmed:15990733", "pubmed:16093404", "pubmed:16277678",
    "pubmed:16380297", "pubmed:16871332", "pubmed:17784727", "pubmed:18788725", "pubmed:19121630",
    "pubmed:19335717", "pubmed:19355913", "pubmed:24650098", "pubmed:33624660", "pubmed:33965562",
    "pubmed:33968971", "pubmed:34207319", "pubmed:34219855", "pubmed:7738698", "pubmed:8235383",
    "pubmed:9040515", "pubmed:9420019", "pubmed:9565830", "pubmed:9683174", "pubmed:9781393",
    "pubmed:9808640", "pubmed:9808641", "reaxys:100781", "wikipedia.en:Folic_Acid"],
    "generalized_empirical_formula": ["C19H19N7O6"], "has_alternative_id": ["CHEBI:24075",
    "CHEBI:42610", "CHEBI:5140", "CHEBI:569217"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:27470"], "inchi_key_string": ["OVBPIULPVIDEAO-LBPRGKRZSA-N"], "inchi_string":
    ["InChI=1S/C19H19N7O6/c20-19-25-15-14(17(30)26-19)23-11(8-22-15)7-21-10-3-1-9(2-4-10)16(29)24-12(18(31)32)5-6-13(27)28/h1-4,8,12,21H,5-7H2,(H,24,29)(H,27,28)(H,31,32)(H3,20,22,25,26,30)/t12-/m0/s1"],
    "mass": ["441.404"], "monoisotopic_mass": ["441.13968"], "smiles_string": ["Nc1nc(=O)c2nc(CNc3ccc(C(=O)N[C@@H](CCC(=O)O)C(=O)O)cc3)cnc2n1"]}'
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:12.829785Z'
  support: supports
  summary: 'CHEBI:30753 resolves to 4-aminobenzoic acid; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:150-13-0",
    "drugbank:DB02362", "drugcentral:2049", "ecmdb:ECMDB01392", "gmelin:50150", "hmdb:HMDB0001392",
    "kegg.compound:C00568", "kegg.drug:D02456", "knapsack:C00001401", "pdb-ccd:PAB",
    "pubmed:12039592", "pubmed:14745019", "pubmed:15115392", "pubmed:1527790", "pubmed:16290145",
    "pubmed:17149871", "pubmed:17743450", "pubmed:17800214", "pubmed:19469519", "pubmed:22767283",
    "pubmed:22994574", "pubmed:23063996", "pubmed:23084339", "pubmed:23144588", "pubmed:23471007",
    "pubmed:3599019", "pubmed:3820215", "pubmed:3950915", "pubmed:8411009", "pubmed:9406595",
    "reaxys:471605", "wikipedia.en:4-Aminobenzoic_acid", "ymdb:YMDB00493"], "generalized_empirical_formula":
    ["C7H7NO2"], "has_alternative_id": ["CHEBI:113372", "CHEBI:1783", "CHEBI:20315",
    "CHEBI:44778"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:30753"],
    "inchi_key_string": ["ALYNCZNDIQEVRV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C7H7NO2/c8-6-3-1-5(2-4-6)7(9)10/h1-4H,8H2,(H,9,10)"],
    "mass": ["137.138"], "monoisotopic_mass": ["137.04768"], "smiles_string": ["Nc1ccc(C(=O)O)cc1"]}'
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:44.571163Z'
  support: supports
  summary: 'CHEBI:30961 resolves to pyridoxine hydrochloride; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND500675659",
    "beilstein:3632435", "cas:58-56-0", "drugbank:DBSALT000151", "foodb.food:FDB000575",
    "gmelin:1067921", "kegg.drug:D02179", "pubmed:15098856", "pubmed:17416572", "pubmed:17891511",
    "pubmed:18243627", "pubmed:19481898", "pubmed:20645279", "pubmed:21781646", "pubmed:24421551",
    "pubmed:27468034", "pubmed:28095734", "pubmed:32460509", "pubmed:33209152", "pubmed:33936292",
    "pubmed:34140989"], "generalized_empirical_formula": ["C8H11NO3.HCl"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:30961"], "inchi_key_string": ["ZUFQODAHGAHPFQ-UHFFFAOYSA-N"],
    "inchi_string": ["InChI=1S/C8H11NO3.ClH/c1-5-8(12)7(4-11)6(3-10)2-9-5;/h2,10-12H,3-4H2,1H3;1H"],
    "mass": ["205.641"], "monoisotopic_mass": ["205.05057"], "smiles_string": ["Cc1ncc(CO)c(CO)c1O.Cl"]}'
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:28.439407Z'
  support: supports
  summary: 'CHEBI:31206 resolves to ammonium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:12125-02-9",
    "gmelin:10120", "kegg.compound:C12538", "kegg.drug:D01139", "wikipedia.en:Ammonium_Chloride"],
    "generalized_empirical_formula": ["Cl.H4N"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31206"], "inchi_key_string": ["NLXLAEXVIDQMFP-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/ClH.H3N/h1H;1H3"], "mass": ["53.492"], "monoisotopic_mass": ["53.00323"],
    "smiles_string": ["[Cl-].[H][N+]([H])([H])[H]"]}'
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:12.450283Z'
  support: supports
  summary: 'CHEBI:31345 resolves to Calcium pantothenate; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:137-08-6",
    "kegg.compound:C12276", "kegg.drug:D01082", "pubmed:18701278", "pubmed:20553011",
    "pubmed:20843939", "pubmed:24814884", "pubmed:37468498"], "generalized_empirical_formula":
    ["2C9H16NO5.Ca"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31345"],
    "inchi_key_string": ["FAPWYRCQGJNNSJ-UBKPKTQASA-L"], "inchi_string": ["InChI=1S/2C9H17NO5.Ca/c2*1-9(2,5-11)7(14)8(15)10-4-3-6(12)13;/h2*7,11,14H,3-5H2,1-2H3,(H,10,15)(H,12,13);/q;;+2/p-2/t2*7-;/m00./s1"],
    "mass": ["476.536"], "monoisotopic_mass": ["476.16829"], "smiles_string": ["CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].CC(C)(CO)[C@@H](O)C(=O)NCCC(=O)[O-].[Ca+2]"]}'
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi31440
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31440
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:28.489501Z'
  support: supports
  summary: 'CHEBI:31440 resolves to copper(II) sulfate pentahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7758-99-8", "kegg.drug:D03613", "pubmed:11407502", "pubmed:12209195", "pubmed:12484481",
    "pubmed:15040745", "pubmed:15607472", "pubmed:15824790", "pubmed:19346702", "pubmed:2002460",
    "pubmed:20132934", "pubmed:2913309", "pubmed:3351847", "pubmed:7615984", "pubmed:8878264",
    "pubmed:9521458", "pubmed:9776063", "reaxys:16499970", "wikipedia.en:Copper(II)_sulfate"],
    "generalized_empirical_formula": ["Cu.5H2O.O4S"], "has_alternative_id": ["CHEBI:121741",
    "CHEBI:370227"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:31440"],
    "inchi_key_string": ["JZCCFEFSEZPSOG-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Cu.H2O4S.5H2O/c;1-5(2,3)4;;;;;/h;(H2,1,2,3,4);5*1H2/q+2;;;;;;/p-2"],
    "mass": ["249.684"], "monoisotopic_mass": ["248.93415"], "smiles_string": ["O=S(=O)([O-])[O-].[Cu+2].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H]"]}'
  snapshot_sha256: e8ac76313670beb01b2eea5bf76bd0e4a341d0798c99d947484fbdd280d297f9
- evidence_id: chebi31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:42:45.232212Z'
  support: supports
  summary: 'CHEBI:31795 resolves to magnesium sulfate heptahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:10034-99-8", "drugbank:DBSALT001240", "foodb.food:FDB015432", "kegg.compound:C12505",
    "kegg.drug:D01108", "metacyc.compound:CPD0-2387", "pubmed:12078740", "pubmed:21595222",
    "pubmed:26281883", "pubmed:28970193", "pubmed:30510660", "pubmed:5492983", "wikipedia.en:Epsomite"],
    "generalized_empirical_formula": ["7H2O.Mg.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:31795"], "inchi_key_string": ["WRUGWIBCXHJTDG-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Mg.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["246.473"], "monoisotopic_mass": ["246.01072"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Mg+2]"]}'
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32139
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:16:24.226823Z'
  support: supports
  summary: 'CHEBI:32139 resolves to sodium hydrogencarbonate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:144-55-8",
    "drugbank:DB01390", "kegg.compound:C12603", "kegg.drug:D01203", "ppdb:2873", "wikipedia.en:Sodium_Bicarbonate"],
    "generalized_empirical_formula": ["CHO3.Na"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:32139"], "inchi_key_string": ["UIIMBOGNXHQVGW-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/CH2O3.Na/c2-1(3)4;/h(H2,2,3,4);/q;+1/p-1"], "mass": ["84.006"], "monoisotopic_mass":
    ["83.98234"], "smiles_string": ["O=C([O-])O.[Na+]"]}'
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32312
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32312
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:28.879505Z'
  support: supports
  summary: 'CHEBI:32312 resolves to zinc sulfate heptahydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7446-20-0",
    "gmelin:47216", "kegg.drug:D01081", "wikipedia.en:Zinc_Sulfate"], "generalized_empirical_formula":
    ["7H2O.O4S.Zn"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32312"],
    "inchi_key_string": ["RZLVQBNCHSJZPX-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/H2O4S.7H2O.Zn/c1-5(2,3)4;;;;;;;;/h(H2,1,2,3,4);7*1H2;/q;;;;;;;;+2/p-2"],
    "mass": ["287.558"], "monoisotopic_mass": ["285.95482"], "smiles_string": ["O=S(=O)([O-])[O-].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[H]O[H].[Zn+2]"]}'
  snapshot_sha256: eb5cc2a6fbb2e99d39aadb9cc7099a29eaab78e8d45f524c76648390a9c960d9
- evidence_id: chebi32588
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.045588Z'
  support: supports
  summary: 'CHEBI:32588 resolves to potassium chloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7447-40-7",
    "drugbank:DB00761", "kegg.drug:D02060", "metacyc.compound:KCL", "molbase:881",
    "reaxys:3534978", "wikipedia.en:Potassium_Chloride"], "generalized_empirical_formula":
    ["Cl.K"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:32588"], "inchi_key_string":
    ["WCUXLLCKKVVCTQ-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/ClH.K/h1H;/q;+1/p-1"],
    "mass": ["74.551"], "monoisotopic_mass": ["73.93256"], "smiles_string": ["[Cl-].[K+]"]}'
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi33118
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.364390Z'
  support: supports
  summary: 'CHEBI:33118 resolves to boric acid; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["bpdb:2136", "cas:10043-35-3",
    "cas:11113-50-1", "drugcentral:3035", "gmelin:1585", "kegg.compound:C12486", "kegg.drug:D01089",
    "molbase:1644", "pdb-ccd:BO3", "ppdb:2136"], "generalized_empirical_formula":
    ["H3BO3"], "has_alternative_id": ["CHEBI:22911", "CHEBI:31299", "CHEBI:41248"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33118"], "inchi_key_string":
    ["KGBXLFKZBHKPEV-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/BH3O3/c2-1(3)4/h2-4H"],
    "mass": ["61.833"], "monoisotopic_mass": ["62.01752"], "smiles_string": ["[H]OB(O[H])O[H]"]}'
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:04:44.093348Z'
  support: supports
  summary: 'CHEBI:34887 resolves to nickel dichloride; canonical label and live status
    alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:7718-54-9",
    "kegg.compound:C14711", "pubmed:11739495", "pubmed:12603851", "pubmed:21928331",
    "pubmed:23179351", "pubmed:23622879", "pubmed:23702803", "pubmed:23735035", "pubmed:7671317",
    "reaxys:3902827", "reaxys:8128171", "wikipedia.en:Nickel_dichloride"], "generalized_empirical_formula":
    ["Cl2Ni"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:34887"], "inchi_key_string":
    ["QMMRZOWCJAIUJA-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/2ClH.Ni/h2*1H;/q;;+2/p-2"],
    "mass": ["129.599"], "monoisotopic_mass": ["127.87305"], "smiles_string": ["[Cl][Ni][Cl]"]}'
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi44557
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_44557
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:46:15.250117Z'
  support: supports
  summary: 'CHEBI:44557 resolves to nitrilotriacetic acid; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["beilstein:1710776",
    "cas:139-13-9", "drugbank:DB03040", "gmelin:3726", "kegg.compound:C14695", "pdb-ccd:NTA"],
    "generalized_empirical_formula": ["C6H9NO6"], "has_alternative_id": ["CHEBI:34889",
    "CHEBI:44555"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:44557"],
    "inchi_key_string": ["MGFYIUFZLHCRTH-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/C6H9NO6/c8-4(9)1-7(2-5(10)11)3-6(12)13/h1-3H2,(H,8,9)(H,10,11)(H,12,13)"],
    "mass": ["191.139"], "monoisotopic_mass": ["191.04299"], "smiles_string": ["O=C(O)CN(CC(=O)O)CC(=O)O"]}'
  snapshot_sha256: de62dde44d3e28362211eddd4e16e41f6b748508618c828ac760036f8024f6c2
- evidence_id: chebi49105
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:10.911379Z'
  support: supports
  summary: 'CHEBI:49105 resolves to thiamine hydrochloride; canonical label and live
    status alone do not verify source grade, hydration, stereochemistry or stock identity.
    Formula/structure: {"charge": [0.0], "database_cross_reference": ["agr:IND605711145",
    "agr:IND606057536", "beilstein:3642937", "beilstein:3851771", "cas:67-03-8", "chemspider:5967",
    "drugbank:DBSALT000205", "foodb.food:FDB008416", "gmelin:31154", "gmelin:691133",
    "kegg.drug:D02094", "pubmed:11548854", "pubmed:12224421", "pubmed:21212548", "pubmed:22305197",
    "pubmed:24399744", "pubmed:25977858", "pubmed:26616989", "pubmed:27163892", "pubmed:28763984",
    "pubmed:28784494", "pubmed:30131156", "pubmed:31270735", "pubmed:31664290", "pubmed:32009117",
    "pubmed:32562525", "pubmed:32824791", "reaxys:17124533"], "generalized_empirical_formula":
    ["C12H17N4OS.Cl.HCl"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:49105"],
    "inchi_key_string": ["DPJRMOMPQZCRJU-UHFFFAOYSA-M"], "inchi_string": ["InChI=1S/C12H17N4OS.2ClH/c1-8-11(3-4-17)18-7-16(8)6-10-5-14-9(2)15-12(10)13;;/h5,7,17H,3-4,6H2,1-2H3,(H2,13,14,15);2*1H/q+1;;/p-1"],
    "mass": ["337.276"], "monoisotopic_mass": ["336.05784"], "smiles_string": ["Cc1ncc(C[n+]2csc(CCO)c2C)c(N)n1.Cl.[Cl-]"]}'
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi63036
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.666916Z'
  support: supports
  summary: 'CHEBI:63036 resolves to potassium dihydrogen phosphate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7778-77-0", "pubmed:21130014", "pubmed:21931886", "reaxys:15935277", "wikipedia.en:Monopotassium_phosphate"],
    "generalized_empirical_formula": ["H2O4P.K"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:63036"], "inchi_key_string": ["GNSKLFRGEWLPPA-UHFFFAOYSA-M"], "inchi_string":
    ["InChI=1S/K.H3O4P/c;1-5(2,3)4/h;(H3,1,2,3,4)/q+1;/p-1"], "mass": ["136.084"],
    "monoisotopic_mass": ["135.93278"], "smiles_string": ["O=P([O-])(O)O.[K+]"]}'
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63939
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:09.796192Z'
  support: supports
  summary: 'CHEBI:63939 resolves to sodium tungstate dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10213-10-2",
    "reaxys:13157884", "wikipedia.en:Sodium_tungstate"], "generalized_empirical_formula":
    ["2H2O.2Na.O4W"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:63939"],
    "inchi_key_string": ["WPZFLQRLSGVIAA-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.2H2O.4O.W/h;;2*1H2;;;;;/q2*+1;;;;;2*-1;"],
    "mass": ["329.846"], "monoisotopic_mass": ["329.93126"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[W](=[O])([O-])[O-]"]}'
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: chebi75213
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:29.756647Z'
  support: supports
  summary: 'CHEBI:75213 resolves to sodium molybdate dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10102-40-6",
    "pubmed:20645132", "pubmed:20813395", "pubmed:22663766", "pubmed:3382795", "reaxys:19032996",
    "wikipedia.en:Sodium_molybdate"], "generalized_empirical_formula": ["2H2O.MoO4.2Na"],
    "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75213"], "inchi_key_string":
    ["FDEIWTXVNPKYDL-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/Mo.2Na.2H2O.4O/h;;;2*1H2;;;;/q;2*+1;;;;;2*-1"],
    "mass": ["241.946"], "monoisotopic_mass": ["243.88573"], "smiles_string": ["O.O.[Na+].[Na+].[O]=[Mo](=[O])([O-])[O-]"]}'
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi75836
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75836
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:07.038393Z'
  support: supports
  summary: 'CHEBI:75836 resolves to iron(2+) sulfate heptahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7782-63-0", "kegg.drug:D01725", "metacyc.compound:CPD0-2418", "pubmed:3729890",
    "reaxys:11322534"], "generalized_empirical_formula": ["Fe.7H2O.O4S"], "has_alternative_id":
    ["CHEBI:31609"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:75836"],
    "inchi_key_string": ["SURQXAFEQWPFPV-UHFFFAOYSA-L"], "inchi_string": ["InChI=1S/Fe.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["278.013"], "monoisotopic_mass": ["277.96062"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Fe+2]"]}'
  snapshot_sha256: 14b56bdc09964796c959bcdb19159b03ddf37dcc0ccfc4b489ec1303a272d525
- evidence_id: chebi76209
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:04.847843Z'
  support: supports
  summary: 'CHEBI:76209 resolves to sodium sulfide nonahydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:1313-84-4",
    "kegg.drug:D09001", "pubmed:19810706", "reaxys:14636099"], "generalized_empirical_formula":
    ["9H2O.2Na.S"], "has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:76209"],
    "inchi_key_string": ["ZGHLCBJZQLNUAZ-UHFFFAOYSA-N"], "inchi_string": ["InChI=1S/2Na.9H2O.S/h;;9*1H2;/q2*+1;;;;;;;;;;-2"],
    "mass": ["240.182"], "monoisotopic_mass": ["240.04669"], "smiles_string": ["O.O.O.O.O.O.O.O.O.[Na+].[Na+].[S-2]"]}'
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi86158
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.011607Z'
  support: supports
  summary: 'CHEBI:86158 resolves to calcium chloride dihydrate; canonical label and
    live status alone do not verify source grade, hydration, stereochemistry or stock
    identity. Formula/structure: {"charge": [0.0], "database_cross_reference": ["cas:10035-04-8",
    "drugbank:DBSALT000772", "kegg.drug:D02256", "metacyc.compound:CPD0-2507", "reaxys:11343730"],
    "generalized_empirical_formula": ["Ca.2Cl.2H2O"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86158"], "inchi_key_string": ["LLSDKQJKOVVTOJ-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Ca.2ClH.2H2O/h;2*1H;2*1H2/q+2;;;;/p-2"], "mass": ["147.014"], "monoisotopic_mass":
    ["145.92143"], "smiles_string": ["O.O.[Ca+2].[Cl-].[Cl-]"]}'
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86345
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.382026Z'
  support: supports
  summary: 'CHEBI:86345 resolves to magnesium dichloride hexahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7791-18-6", "kegg.drug:D04834", "pubmed:24831644", "pubmed:25148974", "pubmed:25430969",
    "reaxys:11343754"], "generalized_empirical_formula": ["2Cl.6H2O.Mg"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86345"], "inchi_key_string": ["DHRRIBDTHFBPNG-UHFFFAOYSA-L"],
    "inchi_string": ["InChI=1S/2ClH.Mg.6H2O/h2*1H;;6*1H2/q;;+2;;;;;;/p-2"], "mass":
    ["203.301"], "monoisotopic_mass": ["201.98614"], "smiles_string": ["O.O.O.O.O.O.[Cl-].[Cl-].[Mg+2]"]}'
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86364
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86364
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T07:33:35.036768Z'
  support: supports
  summary: 'CHEBI:86364 resolves to manganese(II) sulfate monohydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:10034-96-5", "kegg.drug:D04854", "pubmed:26097037", "reaxys:13153017", "wikipedia.en:Manganese(II)_sulfate"],
    "generalized_empirical_formula": ["H2O.Mn.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:86364"], "inchi_key_string": ["ISPYRSDWRDQNSW-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Mn.H2O4S.H2O/c;1-5(2,3)4;/h;(H2,1,2,3,4);1H2/q+2;;/p-2"], "mass": ["169.016"],
    "monoisotopic_mass": ["168.90034"], "smiles_string": ["O.O=S(=O)([O-])[O-].[Mn+2]"]}'
  snapshot_sha256: f1da0a281e1fa2263226a8548afc0bf76db61dd36828240b47d83431bd182069
- evidence_id: chebi86465
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86465
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:08.054799Z'
  support: supports
  summary: 'CHEBI:86465 resolves to potassium aluminium sulfate dodecahydrate; canonical
    label and live status alone do not verify source grade, hydration, stereochemistry
    or stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:7784-24-9", "reaxys:14851666", "wikipedia.en:Potassium_alum"], "generalized_empirical_formula":
    ["Al.12H2O.K.2O4S"], "has_alternative_id": ["CHEBI:31192"], "has_obo_namespace":
    ["chebi_ontology"], "id": ["CHEBI:86465"], "inchi_key_string": ["GNHOJBNSNUXZQA-UHFFFAOYSA-J"],
    "inchi_string": ["InChI=1S/Al.K.2H2O4S.12H2O/c;;2*1-5(2,3)4;;;;;;;;;;;;/h;;2*(H2,1,2,3,4);12*1H2/q+3;+1;;;;;;;;;;;;;;/p-4"],
    "mass": ["474.386"], "monoisotopic_mass": ["473.97548"], "smiles_string": ["O.O.O.O.O.O.O.O.O.O.O.O.O=S(=O)([O-])[O-].O=S(=O)([O-])[O-].[Al+3].[K+]"]}'
  snapshot_sha256: 5e74b8136b972b18b427c70e758e12dfe013a6ca671501cddc936038299f7c2c
- evidence_id: chebi8806
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-21T08:17:30.774007Z'
  support: supports
  summary: 'CHEBI:8806 resolves to Resazurin; canonical label and live status alone
    do not verify source grade, hydration, stereochemistry or stock identity. Formula/structure:
    {"charge": [0.0], "database_cross_reference": ["cas:550-82-3", "kegg.compound:C11178"],
    "generalized_empirical_formula": ["C12H7NO4"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:8806"], "inchi_key_string": ["PLXBWHJQWKZRKG-UHFFFAOYSA-N"], "inchi_string":
    ["InChI=1S/C12H7NO4/c14-7-1-3-9-11(5-7)17-12-6-8(15)2-4-10(12)13(9)16/h1-6,14H"],
    "mass": ["229.191"], "monoisotopic_mass": ["229.03751"], "smiles_string": ["O=c1ccc2[n+]([O-])c3ccc(O)cc3oc-2c1"]}'
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi91244
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_91244
  locator: Exact OLS term identifier, canonical label, definition, formula and structure
    annotations
  accessed_at: '2026-10-20T06:55:07.079384Z'
  support: supports
  summary: 'CHEBI:91244 resolves to cobalt(2+) sulfate heptahydrate; canonical label
    and live status alone do not verify source grade, hydration, stereochemistry or
    stock identity. Formula/structure: {"charge": [0.0], "database_cross_reference":
    ["cas:10026-24-1", "pubmed:10504146", "pubmed:12187935", "pubmed:12209163", "pubmed:12579202",
    "pubmed:12948248", "pubmed:2227161", "pubmed:24359163", "pubmed:25896363", "wikipedia.en:Cobalt(II)_sulfate"],
    "generalized_empirical_formula": ["Co.7H2O.O4S"], "has_obo_namespace": ["chebi_ontology"],
    "id": ["CHEBI:91244"], "inchi_key_string": ["MEYVLGVRTYSQHI-UHFFFAOYSA-L"], "inchi_string":
    ["InChI=1S/Co.H2O4S.7H2O/c;1-5(2,3)4;;;;;;;/h;(H2,1,2,3,4);7*1H2/q+2;;;;;;;;/p-2"],
    "mass": ["281.101"], "monoisotopic_mass": ["280.95888"], "smiles_string": ["O.O.O.O.O.O.O.O=S(=O)([O-])[O-].[Co+2]"]}'
  snapshot_sha256: dd763e0620a8afe61626951123a4de5d100bfa4534ee26ba0a39dad4e7e9bcaa
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Entire pinned CSV; preferred-term MAPPED rows for every asserted secondary
    CHEBI key
  accessed_at: '2026-10-21T10:12:17Z'
  support: supports
  summary: '{"CHEBI:32588": [{"label": "KCl", "match_type": "preferred_term", "identifier":
    "CHEBI:32588", "preferred_term": "KCl", "ontology_id": "CHEBI:32588", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86345": [{"label": "Magnesium chloride",
    "match_type": "preferred_term", "identifier": "CHEBI:86345", "preferred_term":
    "Magnesium chloride", "ontology_id": "CHEBI:86345", "mapping_status": "MAPPED",
    "ambiguity": "unique"}, {"label": "MgCl2 x 6 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:86345", "preferred_term": "MgCl2 x 6 H2O", "ontology_id":
    "CHEBI:86345", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86158":
    [{"label": "CaCl2 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:86158",
    "preferred_term": "CaCl2 x 2 H2O", "ontology_id": "CHEBI:86158", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:31206": [{"label": "NH4Cl", "match_type":
    "preferred_term", "identifier": "CHEBI:31206", "preferred_term": "NH4Cl", "ontology_id":
    "CHEBI:31206", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:63036":
    [{"label": "KH2PO4", "match_type": "preferred_term", "identifier": "CHEBI:63036",
    "preferred_term": "KH2PO4", "ontology_id": "CHEBI:63036", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:32139": [{"label": "NaHCO3", "match_type": "preferred_term",
    "identifier": "CHEBI:32139", "preferred_term": "NaHCO3", "ontology_id": "CHEBI:32139",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:15824": [{"label":
    "D-Fructose", "match_type": "preferred_term", "identifier": "CHEBI:15824", "preferred_term":
    "D-Fructose", "ontology_id": "CHEBI:15824", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:76209": [{"label": "Na2S x 9 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:76209", "preferred_term": "Na2S x 9 H2O", "ontology_id":
    "CHEBI:76209", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:44557":
    [{"label": "Nitrilotriacetic acid", "match_type": "preferred_term", "identifier":
    "CHEBI:44557", "preferred_term": "Nitrilotriacetic acid", "ontology_id": "CHEBI:44557",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31795": [{"label":
    "MgSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31795",
    "preferred_term": "MgSO4 x 7 H2O", "ontology_id": "CHEBI:31795", "mapping_status":
    "MAPPED", "ambiguity": "unique"}, {"label": "MgSO4·H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:31795", "preferred_term": "MgSO4·H2O", "ontology_id": "CHEBI:31795",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:86364": [{"label":
    "MnSO4 x H2O", "match_type": "preferred_term", "identifier": "CHEBI:86364", "preferred_term":
    "MnSO4 x H2O", "ontology_id": "CHEBI:86364", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term",
    "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75836": [{"label":
    "FeSO4 x 7 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75836",
    "preferred_term": "FeSO4 x 7 H2O", "ontology_id": "CHEBI:75836", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:91244": [{"label": "CoSO4 x 7 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:91244", "preferred_term":
    "CoSO4 x 7 H2O", "ontology_id": "CHEBI:91244", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:32312": [{"label": "ZnSO4 x 7 H2O", "match_type": "preferred_term",
    "identifier": "CHEBI:32312", "preferred_term": "ZnSO4 x 7 H2O", "ontology_id":
    "CHEBI:32312", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:31440":
    [{"label": "CuSO4 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:31440",
    "preferred_term": "CuSO4 x 5 H2O", "ontology_id": "CHEBI:31440", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:86465": [{"label": "AlK(SO4)2 x 12 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:86465", "preferred_term":
    "AlK(SO4)2 x 12 H2O", "ontology_id": "CHEBI:86465", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:33118": [{"label": "H3BO3", "match_type": "preferred_term",
    "identifier": "CHEBI:33118", "preferred_term": "H3BO3", "ontology_id": "CHEBI:33118",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:75213": [{"label":
    "Na2MoO4 x 2 H2O", "match_type": "preferred_term", "identifier": "CHEBI:75213",
    "preferred_term": "Na2MoO4 x 2 H2O", "ontology_id": "CHEBI:75213", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:34887": [{"label": "NiCl2", "match_type":
    "preferred_term", "identifier": "CHEBI:34887", "preferred_term": "NiCl2", "ontology_id":
    "CHEBI:34887", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:131361":
    [{"label": "Na2SeO3 x 5 H2O", "match_type": "preferred_term", "identifier": "CHEBI:131361",
    "preferred_term": "Na2SeO3 x 5 H2O", "ontology_id": "CHEBI:131361", "mapping_status":
    "MAPPED", "ambiguity": "unique"}], "CHEBI:63939": [{"label": "Na2WO4 x 2 H2O",
    "match_type": "preferred_term", "identifier": "CHEBI:63939", "preferred_term":
    "Na2WO4 x 2 H2O", "ontology_id": "CHEBI:63939", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15956": [{"label": "Biotin", "match_type": "preferred_term",
    "identifier": "CHEBI:15956", "preferred_term": "Biotin", "ontology_id": "CHEBI:15956",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:27470": [{"label":
    "Folic acid", "match_type": "preferred_term", "identifier": "CHEBI:27470", "preferred_term":
    "Folic acid", "ontology_id": "CHEBI:27470", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:30961": [{"label": "Pyridoxine hydrochloride", "match_type":
    "preferred_term", "identifier": "CHEBI:30961", "preferred_term": "Pyridoxine hydrochloride",
    "ontology_id": "CHEBI:30961", "mapping_status": "MAPPED", "ambiguity": "unique"}],
    "CHEBI:49105": [{"label": "Thiamine HCl", "match_type": "preferred_term", "identifier":
    "CHEBI:49105", "preferred_term": "Thiamine HCl", "ontology_id": "CHEBI:49105",
    "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17015": [{"label":
    "Riboflavin", "match_type": "preferred_term", "identifier": "CHEBI:17015", "preferred_term":
    "Riboflavin", "ontology_id": "CHEBI:17015", "mapping_status": "MAPPED", "ambiguity":
    "unique"}], "CHEBI:15940": [{"label": "Nicotinic acid", "match_type": "preferred_term",
    "identifier": "CHEBI:15940", "preferred_term": "Nicotinic acid", "ontology_id":
    "CHEBI:15940", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:176843":
    [{"label": "Vitamin B12", "match_type": "preferred_term", "identifier": "CHEBI:176843",
    "preferred_term": "Vitamin B12", "ontology_id": "CHEBI:176843", "mapping_status":
    "MAPPED", "ambiguity": "resolved:owned"}], "CHEBI:30753": [{"label": "p-Aminobenzoic
    acid", "match_type": "preferred_term", "identifier": "CHEBI:30753", "preferred_term":
    "p-Aminobenzoic acid", "ontology_id": "CHEBI:30753", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:16494": [{"label": "(DL)-alpha-Lipoic acid", "match_type":
    "preferred_term", "identifier": "CHEBI:16494", "preferred_term": "(DL)-alpha-Lipoic
    acid", "ontology_id": "CHEBI:16494", "mapping_status": "MAPPED", "ambiguity":
    "unique"}]}'
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/614
  locator: $.data.medium; all main/mineral/vitamin recipe rows and steps
  accessed_at: '2026-10-21T09:49:53.218427Z'
  support: supports
  summary: MediaDive separates main solution 1320, mineral stock 241 and 10x vitamin
    stock 5980. All 40 source rows are independently inventoried with their original
    units and stage.
  snapshot_sha256: d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d
- evidence_id: primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf
  locator: Both DSMZ 614 PDF pages, including complete main/mineral/vitamin tables
    and associated preparation
  accessed_at: '2026-10-21T09:49:54.067968Z'
  support: supports
  summary: The primary defines the base medium plus 10 ml mineral and 1 ml vitamin
    additions. Stock definitions are printed in the same PDF; no unrelated medium
    141 or 120 formulations are imported.
  snapshot_sha256: 05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe
- evidence_id: komodo
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: MediaList exact ID=614.1 row; accession/name/pH/original-recipe link only
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: The exact table row supports the linked source identity and displayed pH;
    it does not supply ingredient amounts or prove a strain-specific recipe is identical
    to its linked base.
  quote: "<TR>\n\t\t\t\t\t<TD width=\"50\"><a href='/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=614.1'\
    \ >614.1</a></TD>\n\t\t\t\t\t<TD> For DSM 8238</TD>\n\t\t\t\t\t<TD> 7.5</TD>\n\
    \t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a\
    \ href='http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf</a></TD>\n\
    \t\t\t\t</TR>"
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: variant-detail
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=614.1
  locator: Exact KOMODO 614.1 detail request; captured HTTP 403 response
  accessed_at: '2026-10-21T09:51:04.602677Z'
  support: context_only
  summary: The exact detail endpoint was inaccessible. Its error body supplies no
    usable formulation content; public list metadata and the base DSMZ PDF cannot
    fill that variant-specific evidence gap.
  snapshot_sha256: c57c8c404fdeb13c2b9e07658580af6b0549f3f7c56d747a72746e0b88a9ab38
- evidence_id: quantities
  kind: record_content
  reference: /private/tmp/culturemech-review-work-batch015/147/quantity-inventory.json
  locator: Complete source-linked quantity decision inventory
  accessed_at: '2026-10-21T10:12:17Z'
  support: context_only
  summary: Fifty-one literal-source decisions cover all 40 main/mineral/vitamin rows,
    ten preparation/stock quantity contexts and the exact KOMODO variant pH. All 40
    provider row objects are literal raw excerpts; base-source support and unresolved
    variant claims remain separate.
  snapshot_sha256: 5a034ca73cfc466a9ab27ba4b76580ec2e7142d1db3562fee4fa8c22d88d0603
- evidence_id: writer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py; src/culturemech/enrich/dsmz_resolver.py;
    scripts/cleanup_media_quality.py; scripts/repair_komodo_614_acetobacterium_score10.py;
    src/culturemech/merge/formulation.py
  locator: _parse_api_composition/_parse_api_solutions/_parse_preparation_steps; merge_composition;
    _merge_ingredient_group; repair_parent/repair_child/_require_record; formulation_content/merge_formulation_evidence
  accessed_at: '2026-10-21T10:12:17Z'
  support: context_only
  summary: Current importer separates main and stock additions but concatenates preparation.
    Resolver copies base composition without preparation. Current cleanup no longer
    sums conflicting duplicates; this does not erase the observed historical summed-calcium
    note. September topology repair requires the same 34-item flattened signature
    and changes family links while adding ingredients_curated to the child; it does
    not scientifically repair ingredients. Current merge compatibility includes pH
    and variant relations, so these current owners should not be collapsed as identical.
    No exact historical execution is inferred solely from current code.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding-coverage
  area: grounding
  topic: Exact primary labels and current secondary linkage coverage
  outcome: supported
  summary: '33 unique asserted CHEBI identifiers resolve with exact labels. Primary
    linkage 33/34 (97.06%); verified current secondary linkage 31/34 (91.18%). This
    is a 0–100 ingredient-instance linkage scale, not scientific correctness. Missing
    current secondary keys: []. Legacy links and chemical-form correctness are assessed
    separately.'
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - mim
  - chebi131361
  - chebi15824
  - chebi15940
  - chebi15956
  - chebi16494
  - chebi17015
  - chebi176843
  - chebi26710
  - chebi27470
  - chebi30753
  - chebi30961
  - chebi31206
  - chebi31345
  - chebi31440
  - chebi31795
  - chebi32139
  - chebi32312
  - chebi32588
  - chebi33118
  - chebi34887
  - chebi44557
  - chebi49105
  - chebi63036
  - chebi63939
  - chebi75213
  - chebi75836
  - chebi76209
  - chebi86158
  - chebi86345
  - chebi86364
  - chebi86465
  - chebi8806
  - chebi91244
- assessment_id: history-time
  area: provenance
  topic: Full history and timezone audit
  outcome: concern
  summary: 'History event counts: [(''target'', 11), (''data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml'',
    10), (''data/normalized_yaml/bacterial/for_dsm_8238.yaml'', 10)]. Explicit timestamp
    defects: [(''data/normalized_yaml/bacterial/for_dsm_8238.yaml'', 0, ''2026-01-27T01:15:03.fZ'',
    ''malformed ISO timestamp''), (''data/normalized_yaml/bacterial/for_dsm_8238.yaml'',
    1, ''2026-02-03T11:19:01.299702'', ''timezone absent'')]. Historical bytes are
    assessed as observed; no inferred timezone or retroactive replacement timestamp
    is supplied.'
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
- assessment_id: quantities
  area: quantity
  topic: Every direct, stock, stock-addition and preparation quantity
  outcome: concern
  summary: Fifty-one literal-source decisions cover all 40 main/mineral/vitamin rows,
    ten preparation/stock quantity contexts and the exact KOMODO variant pH. All 40
    provider row objects are literal raw excerpts; base-source support and unresolved
    variant claims remain separate.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - quantities
  details: '[{"field_path": "ingredients[0].concentration", "decision": "evidence_only",
    "stage": "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256":
    "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote":
    "KCl 0.33 g", "source_locator": "DSMZ 614 main table; exact entry KCl 0.33 g",
    "explanation": "The generated target and DSMZ owner match provider-declared main
    g/L but lack claim-level source evidence. Preserve original mass and normalization
    basis. The KOMODO variant owner copies base values, but variant-specific formulation
    support remains unavailable; do not label that distinct variant claim verified.",
    "provider_reference": "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256":
    "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d", "provider_locator":
    "$.data.solutions[0].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    4.3784,\n                        \"optional\": 0\n                    }", "source_amount":
    0.33, "source_unit": "g", "provider_g_l": 0.326409, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[1].concentration",
    "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume
    1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "MgCl2 x 6 H2O 0.52 g", "source_locator": "DSMZ 614 main table;
    exact entry MgCl2 x 6 H2O 0.52 g", "explanation": "The generated target and DSMZ
    owner match provider-declared main g/L but lack claim-level source evidence. Preserve
    original mass and normalization basis. The KOMODO variant owner copies base values,
    but variant-specific formulation support remains unavailable; do not label that
    distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.52,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.514342,\n                        \"mmol_l\":
    2.52993,\n                        \"optional\": 0\n                    }", "source_amount":
    0.52, "source_unit": "g", "provider_g_l": 0.514342, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[2].concentration",
    "decision": "correct", "stage": "DSMZ 614 base main recipe / provider volume 1011
    ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "CaCl2 x 2 H2O 0.22 g", "source_locator": "DSMZ 614 main table;
    exact entry CaCl2 x 2 H2O 0.22 g", "explanation": "Source main calcium is 0.22
    g and provider main g_l=0.217606. Local 0.317606 instead adds a separate mineral-stock
    0.1 g/L without its 10 ml dilution. On provider basis, (0.22 g + 0.1 g/L*0.010
    L)/1.011 L=0.218595450 g/L; this arithmetic explains the stage error, not an authorized
    replacement or measured final concentration.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.22,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.217606,\n                        \"mmol_l\":
    1.48016,\n                        \"optional\": 0\n                    }", "source_amount":
    0.22, "source_unit": "g", "provider_g_l": 0.217606, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[3].concentration",
    "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume
    1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "NH4Cl 0.33 g", "source_locator": "DSMZ 614 main table; exact
    entry NH4Cl 0.33 g", "explanation": "The generated target and DSMZ owner match
    provider-declared main g/L but lack claim-level source evidence. Preserve original
    mass and normalization basis. The KOMODO variant owner copies base values, but
    variant-specific formulation support remains unavailable; do not label that distinct
    variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[3]", "provider_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    6.10225,\n                        \"optional\": 0\n                    }", "source_amount":
    0.33, "source_unit": "g", "provider_g_l": 0.326409, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[4].concentration",
    "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume
    1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "KH2PO4 0.33 g", "source_locator": "DSMZ 614 main table; exact
    entry KH2PO4 0.33 g", "explanation": "The generated target and DSMZ owner match
    provider-declared main g/L but lack claim-level source evidence. Preserve original
    mass and normalization basis. The KOMODO variant owner copies base values, but
    variant-specific formulation support remains unavailable; do not label that distinct
    variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[4]", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.33,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.326409,\n                        \"mmol_l\":
    2.39857,\n                        \"optional\": 0\n                    }", "source_amount":
    0.33, "source_unit": "g", "provider_g_l": 0.326409, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[5].concentration",
    "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume
    1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Yeast extract 0.50 g", "source_locator": "DSMZ 614 main table;
    exact entry Yeast extract 0.50 g", "explanation": "The generated target and DSMZ
    owner match provider-declared main g/L but lack claim-level source evidence. Preserve
    original mass and normalization basis. The KOMODO variant owner copies base values,
    but variant-specific formulation support remains unavailable; do not label that
    distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[5]", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.49456,\n                        \"optional\":
    0\n                    }", "source_amount": 0.5, "source_unit": "g", "provider_g_l":
    0.49456, "owner_decisions": ["evidence_only", "unsupported"], "variant_owner_limit":
    "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail
    is HTTP 403. This base-source row does not independently establish variant equivalence."},
    {"field_path": "solutions (missing source stock dose)", "decision": "add", "stage":
    "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Modified Wolin''s mineral solution 10.00 ml", "source_locator":
    "DSMZ 614 main table; exact entry Modified Wolin''s mineral solution 10.00 ml",
    "explanation": "This exact stock volume addition is missing in all local layers.
    Restore its relationship to the separately prepared source stock, keeping the
    dose and stock concentration distinct.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[6]", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    10, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[6].concentration",
    "decision": "correct", "stage": "DSMZ 614 base main recipe / provider volume 1011
    ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Sodium resazurin (0.1% w/v) 0.50 ml", "source_locator": "DSMZ
    614 main table; exact entry Sodium resazurin (0.1% w/v) 0.50 ml", "explanation":
    "The source stock is explicitly 0.1% w/v, so 0.50 ml supplies 0.0005 g. Provider
    normalization 0.0005 g/1.011 L=0.000494559842 g/L matches local 0.00049456. The
    numeric mass is consistent; the missing stock strength and dose require representation
    correction, and the sodium salt identity is a separate grounding issue.", "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[7]", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\":
    0\n                    }", "source_amount": 0.5, "source_unit": "ml", "provider_g_l":
    0.00049456, "owner_decisions": ["correct", "unsupported"], "variant_owner_limit":
    "KOMODO 614.1 ingredient values are copied from DSMZ 614; exact variant detail
    is HTTP 403. This base-source row does not independently establish variant equivalence."},
    {"field_path": "ingredients[7].concentration", "decision": "evidence_only", "stage":
    "DSMZ 614 base main recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "NaHCO3 1.00 g", "source_locator": "DSMZ 614 main table; exact
    entry NaHCO3 1.00 g", "explanation": "The generated target and DSMZ owner match
    provider-declared main g/L but lack claim-level source evidence. Preserve original
    mass and normalization basis. The KOMODO variant owner copies base values, but
    variant-specific formulation support remains unavailable; do not label that distinct
    variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[8]", "provider_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.98912,\n                        \"mmol_l\":
    11.7743,\n                        \"optional\": 0\n                    }", "source_amount":
    1, "source_unit": "g", "provider_g_l": 0.98912, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[8].concentration",
    "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume
    1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "D-Fructose 10.00 g", "source_locator": "DSMZ 614 main table;
    exact entry D-Fructose 10.00 g", "explanation": "The generated target and DSMZ
    owner match provider-declared main g/L but lack claim-level source evidence. Preserve
    original mass and normalization basis. The KOMODO variant owner copies base values,
    but variant-specific formulation support remains unavailable; do not label that
    distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[9]", "provider_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"D-Fructose\",\n                        \"compound_id\":
    33,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.8912,\n                        \"mmol_l\":
    54.9023,\n                        \"optional\": 0\n                    }", "source_amount":
    10, "source_unit": "g", "provider_g_l": 9.8912, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "solutions (missing
    source stock dose)", "decision": "add", "stage": "DSMZ 614 base main recipe /
    provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Wolin''s vitamin solution (10x) 1.00 ml", "source_locator": "DSMZ
    614 main table; exact entry Wolin''s vitamin solution (10x) 1.00 ml", "explanation":
    "This exact stock volume addition is missing in all local layers. Restore its
    relationship to the separately prepared source stock, keeping the dose and stock
    concentration distinct.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[10]", "provider_quote": "{\n                        \"recipe_order\":
    11,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    1, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[9].concentration",
    "decision": "evidence_only", "stage": "DSMZ 614 base main recipe / provider volume
    1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Na2S x 9 H2O 0.70 g", "source_locator": "DSMZ 614 main table;
    exact entry Na2S x 9 H2O 0.70 g", "explanation": "The generated target and DSMZ
    owner match provider-declared main g/L but lack claim-level source evidence. Preserve
    original mass and normalization basis. The KOMODO variant owner copies base values,
    but variant-specific formulation support remains unavailable; do not label that
    distinct variant claim verified.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[11]", "provider_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.692384,\n                        \"mmol_l\":
    2.88275,\n                        \"optional\": 0\n                    }", "source_amount":
    0.7, "source_unit": "g", "provider_g_l": 0.692384, "owner_decisions": ["evidence_only",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "preparation_steps
    (missing scoped source water)", "decision": "add", "stage": "DSMZ 614 base main
    recipe / provider volume 1011 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 614 main
    table; exact entry Distilled water 1000.00 ml", "explanation": "The source water
    volume is missing at this precise main or stock stage. Retain ml and scope; do
    not treat water alone as measured final volume or collapse three independent solvent
    additions.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[0].recipe[12]", "provider_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    1000, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[10].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Nitrilotriacetic acid 1.50 g", "source_locator": "DSMZ 614 Modified
    Wolin''s mineral solution subsection; exact entry Nitrilotriacetic acid 1.50 g",
    "explanation": "This source amount belongs to the separate stock, not directly
    to the main medium. Its local g/L value retains undiluted stock scale. On provider
    volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L;
    a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional
    provider-basis calculations, not measured final concentrations.", "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\":
    189,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.84765,\n                        \"optional\": 0\n                    }", "source_amount":
    1.5, "source_unit": "g", "provider_g_l": 1.5, "owner_decisions": ["correct", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[11].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "MgSO4 x 7 H2O 3.00 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry MgSO4 x 7 H2O 3.00 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\":
    12.1716,\n                        \"optional\": 0\n                    }", "source_amount":
    3, "source_unit": "g", "provider_g_l": 3, "owner_decisions": ["correct", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[12].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "MnSO4 x H2O 0.50 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry MnSO4 x H2O 0.50 g", "explanation": "This
    source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\":
    14,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.9583,\n                        \"optional\": 0\n                    }", "source_amount":
    0.5, "source_unit": "g", "provider_g_l": 0.5, "owner_decisions": ["correct", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[13].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "NaCl 1.00 g", "source_locator": "DSMZ 614 Modified Wolin''s mineral
    solution subsection; exact entry NaCl 1.00 g", "explanation": "This source amount
    belongs to the separate stock, not directly to the main medium. Its local g/L
    value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock
    contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is
    stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations,
    not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[3]", "provider_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\":
    17.1116,\n                        \"optional\": 0\n                    }", "source_amount":
    1, "source_unit": "g", "provider_g_l": 1, "owner_decisions": ["correct", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[14].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "FeSO4 x 7 H2O 0.10 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry FeSO4 x 7 H2O 0.10 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[4]", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\":
    12,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.359693,\n                        \"optional\": 0\n                    }", "source_amount":
    0.1, "source_unit": "g", "provider_g_l": 0.1, "owner_decisions": ["correct", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[15].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "CoSO4 x 7 H2O 0.18 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry CoSO4 x 7 H2O 0.18 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[5]", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\":
    198,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    1.16132,\n                        \"optional\": 0\n                    }", "source_amount":
    0.18, "source_unit": "g", "provider_g_l": 0.18, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[2].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "CaCl2 x 2 H2O 0.10 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry CaCl2 x 2 H2O 0.10 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. The local calcium 0.317606 g/L
    sums direct 0.217606 and undiluted stock 0.1. The stock contribution on the provider
    basis would instead be 0.1*0.010/1.011=0.000989119683 g/L; keep the two source
    calcium additions separate.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[6]", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.680203,\n                        \"optional\": 0\n                    }", "source_amount":
    0.1, "source_unit": "g", "provider_g_l": 0.1, "owner_decisions": ["correct", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[16].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "ZnSO4 x 7 H2O 0.18 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry ZnSO4 x 7 H2O 0.18 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[7]", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\":
    35,\n                        \"amount\": 0.18,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\":
    0.625954,\n                        \"optional\": 0\n                    }", "source_amount":
    0.18, "source_unit": "g", "provider_g_l": 0.18, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[17].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "CuSO4 x 5 H2O 0.01 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry CuSO4 x 5 H2O 0.01 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[8]", "provider_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\":
    121,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0400503,\n                        \"optional\": 0\n                    }", "source_amount":
    0.01, "source_unit": "g", "provider_g_l": 0.01, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[18].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "AlK(SO4)2 x 12 H2O 0.02 g", "source_locator": "DSMZ 614 Modified
    Wolin''s mineral solution subsection; exact entry AlK(SO4)2 x 12 H2O 0.02 g",
    "explanation": "This source amount belongs to the separate stock, not directly
    to the main medium. Its local g/L value retains undiluted stock scale. On provider
    volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L;
    a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional
    provider-basis calculations, not measured final concentrations.", "provider_reference":
    "https://mediadive.dsmz.de/rest/medium/614", "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[9]", "provider_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\":
    908,\n                        \"amount\": 0.02,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0421596,\n                        \"optional\": 0\n                    }", "source_amount":
    0.02, "source_unit": "g", "provider_g_l": 0.02, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[19].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "H3BO3 0.01 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry H3BO3 0.01 g", "explanation": "This source
    amount belongs to the separate stock, not directly to the main medium. Its local
    g/L value retains undiluted stock scale. On provider volume 1011 ml, a mineral-stock
    contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock contribution is
    stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis calculations,
    not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[10]", "provider_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.161708,\n                        \"optional\": 0\n                    }", "source_amount":
    0.01, "source_unit": "g", "provider_g_l": 0.01, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[20].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Na2MoO4 x 2 H2O 0.01 g", "source_locator": "DSMZ 614 Modified
    Wolin''s mineral solution subsection; exact entry Na2MoO4 x 2 H2O 0.01 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[11]", "provider_quote": "{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 0.01,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\":
    0.0413309,\n                        \"optional\": 0\n                    }", "source_amount":
    0.01, "source_unit": "g", "provider_g_l": 0.01, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[21].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "NiCl2 x 6 H2O 0.03 g", "source_locator": "DSMZ 614 Modified Wolin''s
    mineral solution subsection; exact entry NiCl2 x 6 H2O 0.03 g", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[12]", "provider_quote": "{\n                        \"recipe_order\":
    13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 0.03,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\":
    0.231483,\n                        \"optional\": 0\n                    }", "source_amount":
    0.03, "source_unit": "g", "provider_g_l": 0.03, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[22].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Na2SeO3 x 5 H2O 0.30 mg", "source_locator": "DSMZ 614 Modified
    Wolin''s mineral solution subsection; exact entry Na2SeO3 x 5 H2O 0.30 mg", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 0.3 mg equals 0.0003
    g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[13]", "provider_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\":
    107,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\":
    0.00114062,\n                        \"optional\": 0\n                    }",
    "source_amount": 0.3, "source_unit": "mg", "provider_g_l": 0.0003, "owner_decisions":
    ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values
    are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row
    does not independently establish variant equivalence."}, {"field_path": "ingredients[23].concentration",
    "decision": "correct", "stage": "Modified Wolin''s mineral stock / source water
    1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Na2WO4 x 2 H2O 0.40 mg", "source_locator": "DSMZ 614 Modified
    Wolin''s mineral solution subsection; exact entry Na2WO4 x 2 H2O 0.40 mg", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 0.4 mg equals 0.0004
    g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[14]", "provider_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\":
    249,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\":
    0.00121267,\n                        \"optional\": 0\n                    }",
    "source_amount": 0.4, "source_unit": "mg", "provider_g_l": 0.0004, "owner_decisions":
    ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values
    are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row
    does not independently establish variant equivalence."}, {"field_path": "preparation_steps
    (missing scoped source water)", "decision": "add", "stage": "Modified Wolin''s
    mineral stock / source water 1000 ml; added at 10 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 614 Modified
    Wolin''s mineral solution subsection; exact entry Distilled water 1000.00 ml",
    "explanation": "The source water volume is missing at this precise main or stock
    stage. Retain ml and scope; do not treat water alone as measured final volume
    or collapse three independent solvent additions.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[1].recipe[15]", "provider_quote": "{\n                        \"recipe_order\":
    16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    1000, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "ingredients[24].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Biotin 20.00 mg", "source_locator": "DSMZ 614 Wolin''s vitamin
    solution (10x) subsection; exact entry Biotin 20.00 mg", "explanation": "This
    source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 20 mg equals 0.02 g
    within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[0]", "provider_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "source_amount":
    20, "source_unit": "mg", "provider_g_l": 0.02, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[25].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Folic acid 20.00 mg", "source_locator": "DSMZ 614 Wolin''s vitamin
    solution (10x) subsection; exact entry Folic acid 20.00 mg", "explanation": "This
    source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 20 mg equals 0.02 g
    within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[1]", "provider_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "source_amount":
    20, "source_unit": "mg", "provider_g_l": 0.02, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[26].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Pyridoxine hydrochloride 100.00 mg", "source_locator": "DSMZ
    614 Wolin''s vitamin solution (10x) subsection; exact entry Pyridoxine hydrochloride
    100.00 mg", "explanation": "This source amount belongs to the separate stock,
    not directly to the main medium. Its local g/L value retains undiluted stock scale.
    On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010
    L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These
    are conditional provider-basis calculations, not measured final concentrations.
    Original 100 mg equals 0.1 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[2]", "provider_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "source_amount":
    100, "source_unit": "mg", "provider_g_l": 0.1, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[27].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Thiamine HCl 50.00 mg", "source_locator": "DSMZ 614 Wolin''s
    vitamin solution (10x) subsection; exact entry Thiamine HCl 50.00 mg", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 50 mg equals 0.05 g
    within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[3]", "provider_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "source_amount":
    50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[28].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Riboflavin 50.00 mg", "source_locator": "DSMZ 614 Wolin''s vitamin
    solution (10x) subsection; exact entry Riboflavin 50.00 mg", "explanation": "This
    source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 50 mg equals 0.05 g
    within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[4]", "provider_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "source_amount":
    50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[29].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Nicotinic acid 50.00 mg", "source_locator": "DSMZ 614 Wolin''s
    vitamin solution (10x) subsection; exact entry Nicotinic acid 50.00 mg", "explanation":
    "This source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 50 mg equals 0.05 g
    within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[5]", "provider_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "source_amount":
    50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[30].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Calcium D-(+)-pantothenate 50.00 mg", "source_locator": "DSMZ
    614 Wolin''s vitamin solution (10x) subsection; exact entry Calcium D-(+)-pantothenate
    50.00 mg", "explanation": "This source amount belongs to the separate stock, not
    directly to the main medium. Its local g/L value retains undiluted stock scale.
    On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010
    L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These
    are conditional provider-basis calculations, not measured final concentrations.
    Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[6]", "provider_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "source_amount":
    50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[31].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Vitamin B12 1.00 mg", "source_locator": "DSMZ 614 Wolin''s vitamin
    solution (10x) subsection; exact entry Vitamin B12 1.00 mg", "explanation": "This
    source amount belongs to the separate stock, not directly to the main medium.
    Its local g/L value retains undiluted stock scale. On provider volume 1011 ml,
    a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L; a vitamin-stock
    contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional provider-basis
    calculations, not measured final concentrations. Original 1 mg equals 0.001 g
    within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[7]", "provider_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "source_amount": 1, "source_unit": "mg", "provider_g_l": 0.001, "owner_decisions":
    ["correct", "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values
    are copied from DSMZ 614; exact variant detail is HTTP 403. This base-source row
    does not independently establish variant equivalence."}, {"field_path": "ingredients[32].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "p-Aminobenzoic acid 50.00 mg", "source_locator": "DSMZ 614 Wolin''s
    vitamin solution (10x) subsection; exact entry p-Aminobenzoic acid 50.00 mg",
    "explanation": "This source amount belongs to the separate stock, not directly
    to the main medium. Its local g/L value retains undiluted stock scale. On provider
    volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010 L / 1.011 L;
    a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These are conditional
    provider-basis calculations, not measured final concentrations. Original 50 mg
    equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[8]", "provider_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "source_amount":
    50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "ingredients[33].concentration",
    "decision": "correct", "stage": "10x Wolin vitamin stock / source water 1000 ml;
    added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "(DL)-alpha-Lipoic acid 50.00 mg", "source_locator": "DSMZ 614
    Wolin''s vitamin solution (10x) subsection; exact entry (DL)-alpha-Lipoic acid
    50.00 mg", "explanation": "This source amount belongs to the separate stock, not
    directly to the main medium. Its local g/L value retains undiluted stock scale.
    On provider volume 1011 ml, a mineral-stock contribution is stock_g/L * 0.010
    L / 1.011 L; a vitamin-stock contribution is stock_g/L * 0.001 L / 1.011 L. These
    are conditional provider-basis calculations, not measured final concentrations.
    Original 50 mg equals 0.05 g within this stock only.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[9]", "provider_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "source_amount":
    50, "source_unit": "mg", "provider_g_l": 0.05, "owner_decisions": ["correct",
    "unsupported"], "variant_owner_limit": "KOMODO 614.1 ingredient values are copied
    from DSMZ 614; exact variant detail is HTTP 403. This base-source row does not
    independently establish variant equivalence."}, {"field_path": "preparation_steps
    (missing scoped source water)", "decision": "add", "stage": "10x Wolin vitamin
    stock / source water 1000 ml; added at 1 ml", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Distilled water 1000.00 ml", "source_locator": "DSMZ 614 Wolin''s
    vitamin solution (10x) subsection; exact entry Distilled water 1000.00 ml", "explanation":
    "The source water volume is missing at this precise main or stock stage. Retain
    ml and scope; do not treat water alone as measured final volume or collapse three
    independent solvent additions.", "provider_reference": "https://mediadive.dsmz.de/rest/medium/614",
    "provider_sha256": "d9d04046a28bcc6a5d93cac640a037ac292bc55200a94b9d48418a938682d71d",
    "provider_locator": "$.data.solutions[2].recipe[10]", "provider_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "source_amount":
    1000, "source_unit": "ml", "provider_g_l": null, "owner_decisions": ["add", "unsupported"],
    "variant_owner_limit": "KOMODO 614.1 ingredient values are copied from DSMZ 614;
    exact variant detail is HTTP 403. This base-source row does not independently
    establish variant equivalence."}, {"field_path": "preparation_steps[0]", "decision":
    "evidence_only", "stage": "base main sparging atmosphere", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256":
    "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote":
    "medium with 100% N2 gas", "source_locator": "DSMZ 614 main preparation or mineral-stock
    paragraph, as explicitly staged", "explanation": "Target and DSMZ owner retain
    the exact gas fraction. This is preparation metadata, not a demonstrated biological
    oxygen preference or an absolute gas dose."}, {"field_path": "preparation_steps[0]",
    "decision": "evidence_only", "stage": "base main sparging duration", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256":
    "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote":
    "for 30 - 45 min", "source_locator": "DSMZ 614 main preparation or mineral-stock
    paragraph, as explicitly staged", "explanation": "Retained range is correct; it
    is sparging time, not incubation or autoclave time."}, {"field_path": "preparation_steps[0]",
    "decision": "evidence_only", "stage": "separate bicarbonate stock atmosphere",
    "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "80% N2 and 20% CO2 gas atmosphere.", "source_locator": "DSMZ
    614 main preparation or mineral-stock paragraph, as explicitly staged", "explanation":
    "The base procedure explicitly distinguishes this mixture from the 100% N2 used
    for other stocks. Both target and DSMZ owner preserve it; no gas flow is specified."},
    {"field_path": "ph_range; preparation_steps[0]", "decision": "evidence_only",
    "stage": "complete base-medium target pH", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "of complete medium to 6.8 - 7.0, if necessary.", "source_locator":
    "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged",
    "explanation": "Target and DSMZ owner retain the correct target range and conditional
    adjustment. This does not apply to the distinct pH 7.5 variant or represent measured
    final pH."}, {"field_path": "preparation_steps[1]", "decision": "correct", "stage":
    "mineral stock: NTA dissolution before other minerals", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "adjust pH to 6.5 with KOH", "source_locator": "DSMZ 614 main
    preparation or mineral-stock paragraph, as explicitly staged", "explanation":
    "The literal value is retained but its top-level placement loses stock scope.
    Preserve it as the first mineral-stock adjustment, not as a second main-medium
    target."}, {"field_path": "preparation_steps[1]", "decision": "correct", "stage":
    "mineral stock after adding minerals", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "final to pH 7.0 with KOH.", "source_locator": "DSMZ 614 main
    preparation or mineral-stock paragraph, as explicitly staged", "explanation":
    "This is the final target pH of the mineral stock, not the main medium. Move the
    source scope while retaining the exact value."}, {"field_path": "solutions (mineral
    stock preparation)", "decision": "not_quantified", "stage": "mineral-stock pH
    adjustments", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "with KOH", "source_locator": "DSMZ 614 main preparation or mineral-stock
    paragraph, as explicitly staged", "explanation": "KOH is specified as titrant,
    with no dose or stock strength. Preserve the instruction and unresolved quantity;
    do not invent an added concentration."}, {"field_path": "preparation_steps[0]",
    "decision": "evidence_only", "stage": "vitamin stock before post-sterilization
    addition", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Vitamins should be sterilized by filtration.", "source_locator":
    "DSMZ 614 main preparation or mineral-stock paragraph, as explicitly staged",
    "explanation": "The source filtration exception is retained in target and DSMZ
    owner. No filter pore size or sterilization temperature is supplied."}, {"field_path":
    "preparation_steps[0]; solutions", "decision": "not_quantified", "stage": "base
    additions after main sterilization", "source_reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf",
    "source_sha256": "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe",
    "source_quote": "Before use add vitamins, fructose and sulfide from sterile anoxic
    stock solutions prepared", "source_locator": "DSMZ 614 main preparation or mineral-stock
    paragraph, as explicitly staged", "explanation": "The separately defined vitamin
    recipe/dose is quantified above. Additional fructose and sulfide stocks are required
    but their strength/dose volumes are not supplied; retain source main masses and
    the preparation requirement without fabricating those stock parameters."}, {"field_path":
    "parent_media; variant_relationship; synonyms; owner-1.ph_value", "decision":
    "correct", "stage": "KOMODO 614.1 variant, not base DSMZ 614", "source_reference":
    "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList",
    "source_sha256": "d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a",
    "source_quote": "7.5", "source_locator": "MediaList exact accession 614.1 row,
    pH column; full literal row retained in evidence komodo", "explanation": "The
    table explicitly displays variant pH 7.5 and the owner correctly retains it as
    PH_VARIANT after September repair, but the generated target still calls the variant
    a source duplicate. Do not replace the correct base range 6.8–7.0 or assume all
    variant ingredients from the shared link.", "provider_quote": "<TR>\n\t\t\t\t\t<TD
    width=\"50\"><a href=''/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=614.1''
    >614.1</a></TD>\n\t\t\t\t\t<TD> For DSM 8238</TD>\n\t\t\t\t\t<TD> 7.5</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>true</TD>\n\t\t\t\t\t<TD>false</TD>\n<TD><a
    href=''http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf'' >http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf</a></TD>\n\t\t\t\t</TR>",
    "owner_decisions": ["evidence_only", "evidence_only"]}, {"field_path": "preparation_steps[0]",
    "decision": "evidence_only", "stage": "DSMZ 614 base: separate vitamin, fructose
    and sulfide stocks before their post-sterilization addition", "source_reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium614.pdf", "source_sha256":
    "05b3ede814fc7bdfb55a88b7c1674ecfb56338bcaab5cf72fb285bf8205151fe", "source_quote":
    "under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared
    under", "source_locator": "DSMZ 614 page 1 main preparation paragraph; later vitamin,
    fructose and sulfide stock atmosphere, before the separate bicarbonate-stock clause",
    "explanation": "The target and DSMZ base owner retain the explicit 100% N2 atmosphere
    for these later stocks. This is distinct from initial main-medium sparging and
    from the bicarbonate stock under 80% N2/20% CO2. It supplies no gas flow or absolute
    gas dose. The unavailable KOMODO 614.1 variant formulation is not verified by
    this base instruction.", "owner_decisions": ["evidence_only", "unsupported"],
    "variant_owner_limit": "The variant owner lacks preparation and its exact detail
    remains HTTP 403."}]'
- assessment_id: identity
  area: identity
  topic: Base accession, exact variant metadata and inaccessible detail
  outcome: concern
  summary: DSMZ/MediaDive 614 identifies ACETOBACTERIUM FIMETARIUM MEDIUM with pH
    6.8–7.0. KOMODO 614.1 is explicitly For DSM 8238 at pH 7.5 and links that base
    PDF. Current owners separate these as PH_VARIANT, while the generated August target
    retains reversed SOURCE_DUPLICATE topology and a synonym. The table verifies the
    pH distinction but not full variant formulation.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - id-search
  - primary
  - api
  - komodo
  - variant-detail
  - writer
- assessment_id: stocks
  area: quantity
  topic: Every direct amount, nested stock and repeated calcium
  outcome: concern
  summary: Nine non-calcium main g/L values agree with provider declarations, including
    the indicator mass calculated from its stated stock. Fifteen mineral and ten vitamin
    source components are flattened; mineral calcium is additionally summed with main
    calcium, leaving 34 local ingredient rows. Exact source doses and all three water
    quantities are absent. The local 0.317606 calcium value is not a defensible sum
    across these stages.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - quantities
- assessment_id: forms
  area: grounding
  topic: All asserted forms and structures
  outcome: concern
  summary: Explicit nickel hexahydrate maps to unhydrated Cl2Ni, and sodium resazurin
    maps to neutral C12H7NO4. Other named hydrates match their source forms. The primary
    explicitly uses D-(+)-calcium pantothenate, so its stereospecified CHEBI:31345
    is not the DL mismatch seen in other formulations. DL-alpha-lipoic acid maps to
    the stereounspecified CHEBI:16494 structure, retaining DL in its preferred term;
    generic B12 remains broad without inferring cyanocobalamin. Yeast extract remains
    a mixture.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - chebi34887
  - chebi8806
  - chebi31345
  - chebi16494
  - chebi176843
  - mim
- assessment_id: preparation
  area: completeness
  topic: Main versus stock preparation and gas context
  outcome: concern
  summary: 'The target and DSMZ owner correctly retain main gas/time context, different
    bicarbonate atmosphere, vitamin filtration and main target pH. The mineral-stock
    pH 6.5 then 7.0 adjustments are retained as an unscoped second main step. The
    variant owner has no preparation and says Aerobic: Yes; that copied metadata cannot
    substitute for the base anoxic preparation and its variant-specific meaning remains
    unresolved.'
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - komodo
  - variant-detail
  - quantities
- assessment_id: classification
  area: scope
  topic: Composition, physical state and organism claims
  outcome: supported
  summary: COMPLEX/SEMI_DEFINED and LIQUID fit yeast extract plus enumerated salts/vitamins
    and no solidifier. No target-organism experimental growth, incubation claim or
    KG match is asserted. For DSM 8238 is a collection-specific label, not evidence
    of a strain taxonomy identity or experimental growth under every base/variant
    condition.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - komodo
- assessment_id: provenance
  area: provenance
  topic: September owner topology and unchanged ingredient claims
  outcome: concern
  summary: All owner ingredient arrays equal the target, including the flattened stocks
    and summed calcium. The September owner repair changes topology and flags the
    child ingredients_curated while leaving those ingredient claims unchanged. The
    generated target ends at August and omits the corrected family links. No layer
    has claim-level amount/preparation evidence; generic links do not replace it.
    Historical timestamp defects remain explicit in the separate history audit.
  target_ids:
  - CultureMech:001743
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - writer
  - primary
  - api
  - validate-references
findings:
- finding_id: f1
  issue_key: CM001743-stock-and-calcium-collapse
  category: quantity
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock concentrations are flattened and calcium from two stages is summed
  description: Mineral and vitamin stocks become direct medium ingredients at undiluted
    stock strength; the main calcium 0.217606 and stock calcium 0.1 g/L are added
    as 0.317606. Missing 10 ml and 1 ml stock doses, indicator-stock representation,
    solvent stages and unscoped mineral preparation make this a materially different
    formulation.
  target_ids:
  - CultureMech:001743
  field_paths:
  - ingredients[*].concentration
  - ingredients[2].notes
  - solutions
  - preparation_steps[1]
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - quantities
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P1
  native_severity: P1
  normalization_reason: P1 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM001743-ph-variant-merge
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: A pH 7.5 variant is still represented as a duplicate-source synonym
  description: Current maintained owners and public KOMODO metadata distinguish 614.1
    at pH 7.5 from base 614 at pH 6.8–7.0. The generated target still contains obsolete
    SOURCE_DUPLICATE topology and a synonym, obscuring the pH distinction. Exact variant
    formulation remains unavailable rather than proven equal.
  target_ids:
  - CultureMech:001743
  field_paths:
  - parent_media
  - variant_relationship
  - variant_modifications
  - synonyms
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - komodo
  - variant-detail
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM001743-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hexahydrate is mapped to unhydrated nickel dichloride
  description: Source and preferred term specify NiCl2 x 6 H2O; CHEBI:34887 in both
    primary and secondary links has formula Cl2Ni. Live labels and MIM linkage do
    not verify hydration.
  target_ids:
  - CultureMech:001743
  field_paths:
  - ingredients[21].term
  - ingredients[21].mediaingredientmech_chebi_term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - chebi34887
  - mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f4
  issue_key: CM001743-resazurin-salt
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin is mapped to the neutral molecule
  description: The exact primary and provider name sodium resazurin, but CHEBI:8806
    encodes C12H7NO4 without sodium. The quantity conversion does not validate this
    salt mismatch.
  target_ids:
  - CultureMech:001743
  field_paths:
  - ingredients[6].term
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - chebi8806
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f5
  issue_key: CM001743-evidence-and-status
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Curated-status and source links do not substantiate the unchanged formulation
  description: The variant owner received ingredients_curated in a topology-only repair
    that retained the flattened signature. Target and owners lack narrow source evidence
    for formulation/preparation. The variant oxygen metadata has no scoped experimental
    support and its detail page is inaccessible.
  target_ids:
  - CultureMech:001743
  field_paths:
  - references
  - ingredients[*].evidence
  - data_quality_flags
  - notes
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - primary
  - api
  - komodo
  - variant-detail
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f6
  issue_key: CM001743-owner-timestamp-defects
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Variant history has malformed and timezone-free events
  description: The original KOMODO import timestamp ends .fZ and its resolver timestamp
    has no timezone. Later well-formed September events do not establish those original
    instants.
  target_ids:
  - CultureMech:001743
  field_paths:
  - curation_history
  - merged_from
  evidence_ids:
  - owner-1
  - writer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P3
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore separate main/mineral/vitamin stages and exact doses, preserving
    original units and solvent basis. Reconcile the calcium additions before any calculation;
    retain the numerically consistent resazurin mass alongside its missing stock strength/dose.
    Scope mineral preparation to its stock.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a2
  description: Preserve the separately identified pH variant and updated parent/child
    ownership. Resolve its exact formulation before claiming full equivalence; regenerate
    only after ingredient and family corrections, using current compatibility guards.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a3
  description: Resolve the exact hexahydrate identity or explicitly retain unresolved
    grounding, preserving its mineral-stock quantity and hydration.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a4
  description: Resolve the source sodium salt with verified ontology evidence or retain
    an explicit unresolved mapping; do not substitute neutral resazurin or invent
    a replacement ID.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a5
  description: Attach source-specific excerpts to corrected base claims and qualify
    the variant limitations; reconcile the curated-status scope and oxygen metadata
    without asserting unsupported growth or complete variant verification.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a6
  description: Preserve existing events and append a supported clarification; repair
    writer serialization separately without fabricating historical times.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:001743
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/acetobacterium_fimetarium_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_8238.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
limitations:
- The exact KOMODO 614.1 detail request returned HTTP 403. The public MediaList verifies
  the accession, name For DSM 8238, pH 7.5 and link to DSMZ 614; it does not establish
  all variant ingredients or preparation. Review of the complete merged family therefore
  remains partial, while the accessible DSMZ base and its two printed stock definitions
  are fully assessed.
- Provider main volume 1011 ml and g/L are preserved as provider declarations. The
  primary separately lists 1000 ml water, 10 ml mineral stock, 1 ml vitamin stock
  and 0.50 ml indicator stock; these additions are not proof of a measured final volume.
  Unspecified post-sterilization stock strengths, KOH dose, gas flow and autoclave
  time/temperature are not invented.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-015
- generated-medium
```
