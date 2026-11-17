# Scientific review: DESULFONATRONUM medium

- Review: 20261028T202356Z-culturemech-006536-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:15:17.654745Z
- Finished UTC: 2026-10-28T20:23:56.081180Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected merge collapses a maintained strain-specific wrapper and loses DSM preparation while carrying unresolved KOMODO pH/atmosphere. Preserve eleven supported DSM provider rates, restore nineteen stock-stage entries, resolve source identity and chemical-form mismatches, and retain explicit provenance limits.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch077 index 03
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006536 | data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml | generated | desulfonatronum_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:006536 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:006536 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:006536 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:006536 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### DSM813, KOMODO813 and DSM14708 wrapper

identity: concern. Targets: CultureMech:006536.

Three maintained contributors have equal copied ingredient lists but different source conditions and current relationships. The current catalogue points DSM14708 to813a; it does not retroactively authenticate the historical813 link. The selected merge loses the maintained strain boundary. Exact KOMODO routes403 limit completion; no source-growth claim is inferred.

### Complex liquid representation

representation: supported. Targets: CultureMech:006536.

Yeast extract supports complex/undefined classification and the generic DSM formulation lacks a solidifier. This classification does not resolve the separate pH/atmosphere or strain-link issue.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:006536.

120 current concentration fields are covered by 41 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b077-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","quantity_field_count":120,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 3-3","quote":"KH2PO4                                                     0.20         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 1.46674,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q2","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 4-4","quote":"MgCl2 x 6 H2O                                              0.10         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\": 0.490895,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 5-5","quote":"NH4Cl                                                      1.00         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\": 18.6578,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 6-6","quote":"KCl                                                        0.20         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\": 2.67741,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q5","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 7-7","quote":"Na2SO4                                                     5.00         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\": 35.1311,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 8-8","quote":"NaCl                                                      10.00         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 9.98004,\n                        \"mmol_l\": 170.774,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q7","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 10-10","quote":"Yeast extract                                              1.00         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q8","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible; neutral CHEBI grounding is a separate issue.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 11-11","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible; neutral CHEBI grounding is a separate issue."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible; neutral CHEBI grounding is a separate issue."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible; neutral CHEBI grounding is a separate issue."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible; neutral CHEBI grounding is a separate issue."}]},{"quantity_id":"q9","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 12-12","quote":"Na2CO3                                                     3.50         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 3.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.49301,\n                        \"mmol_l\": 32.9567,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q10","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 13-13","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\": 2.0776,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q11","label":"Na-formate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 14-14","quote":"Na-formate                                                 4.00         g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\": 144,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.99202,\n                        \"mmol_l\": 58.6999,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"Exact DSM branch: The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar agrees with the exact current provider main g_l and source batch mass. Credit that declared API1002ml normalization without claiming a measured primary final volume: this exact primary lists1000ml water but does not state a main final make-up. The target and two KOMODO contributors copy the same scalar, but their different pH/atmosphere and unresolved exact source branch prevent transferring DSM quantity support. Preserve all numbers while resolving identity; do not silently change the KOMODO branch to the base."}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L scalar does not establish percent basis or density; do not endorse its conversion, and correct the DSM stock placement. Target and KOMODO copies remain unsupported pending exact branch identity. Preserve the source volume/percent assertions without guessing w/v.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 32-32","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L scalar does not establish percent basis or density; do not endorse its conversion, and correct the DSM stock placement. Target and KOMODO copies remain unsupported pending exact branch identity. Preserve the source volume/percent assertions without guessing w/v."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L scalar does not establish percent basis or density; do not endorse its conversion, and correct the DSM stock placement. Target and KOMODO copies remain unsupported pending exact branch identity. Preserve the source volume/percent assertions without guessing w/v."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"Exact DSM branch: The primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L scalar does not establish percent basis or density; do not endorse its conversion, and correct the DSM stock placement. Target and KOMODO copies remain unsupported pending exact branch identity. Preserve the source volume/percent assertions without guessing w/v."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L scalar does not establish percent basis or density; do not endorse its conversion, and correct the DSM stock placement. Target and KOMODO copies remain unsupported pending exact branch identity. Preserve the source volume/percent assertions without guessing w/v."}]},{"quantity_id":"q13","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 33-33","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 34-34","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 35-35","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 36-36","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 37-37","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 38-38","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 39-39","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 40-40","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes up to1000ml."}]},{"quantity_id":"q21","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 57-57","quote":"Biotin                                     20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q22","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 58-58","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q23","label":"Pyridoxine hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 59-59","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q24","label":"Thiamine HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 60-60","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q25","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 61-61","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q26","label":"Nicotinic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 62-62","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q27","label":"Calcium D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 63-63","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q28","label":"Vitamin B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 64-64","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q29","label":"p-Aminobenzoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 65-65","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q30","label":"(DL)-alpha-Lipoic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 66-66","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"Exact DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Unresolved KOMODO/generated branch: numerical equality with DSM813 does not establish its formulation; preserve existing values pending exact source reconciliation. The DSM owner scalar matches provider stock g_l and source mass, but the current root ingredient placement is wrong; restore its exact stock and1ml batch dose. The copied target/KOMODO values remain unsupported until their branch formulation is resolved, even though their numbers match the DSM stock. The vitamin table lists1000ml water and API declares1000ml stock volume; retain this declared basis without inventing measured make-up."}]},{"quantity_id":"q31","label":"SL-10 source receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The exact DSM813 primary specifies1ml into its stated batch. Restore this dose for the DSM branch with its stock definition; do not call bare ml a primary ml/L assertion or transfer it to unresolved KOMODO variants.","source_stage":"DSM813 source-only batch stock dose","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 9-9","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q32","label":"Wolin10x source receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The exact DSM813 primary specifies1ml into its stated batch. Restore this dose for the DSM branch with its stock definition; do not call bare ml a primary ml/L assertion or transfer it to unresolved KOMODO variants.","source_stage":"DSM813 source-only batch stock dose","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 15-15","quote":"Wolin's vitamin solution (10x)                             1.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q33","label":"DSM sodium-resazurin stock controls","local_fields":[],"decision":"evidence_only","rationale":"The primary explicitly gives0.5ml of0.1% w/v sodium-resazurin stock, supplying0.5mg in the DSM batch. Preserve these controls separately from API final-rate normalization and unresolved KOMODO identity.","source_stage":"DSM813 source-only dye stock","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 11-11","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q34","label":"DSM main water","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact solvent input in its source section. Main1000ml input water is not a measured final-volume statement. SL-10 separately makes up to1000ml; the vitamin provider volume is a declared normalization basis.","source_stage":"DSM813 source-only water","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 16-16","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"DSM SL-10 water","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact solvent input in its source section. Main1000ml input water is not a measured final-volume statement. SL-10 separately makes up to1000ml; the vitamin provider volume is a declared normalization basis.","source_stage":"DSM813 source-only water","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 41-41","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"DSM vitamin water","local_fields":[],"decision":"evidence_only","rationale":"Retain the exact solvent input in its source section. Main1000ml input water is not a measured final-volume statement. SL-10 separately makes up to1000ml; the vitamin provider volume is a declared normalization basis.","source_stage":"DSM813 source-only water","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 67-67","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"DSM SL-10 final make-up","local_fields":[],"decision":"evidence_only","rationale":"The source explicitly makes up SL-10 to1000ml after acid/water inputs. This is a stock final-volume instruction, not the main medium denominator.","source_stage":"DSM813 stock final volume","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 32-32","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 41-44","quote":"Distilled water                                           990.00      ml\n\nFirst dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Retained DSM pH","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ph_range","stored":{"min":8.8,"max":9.0}}],"decision":"evidence_only","rationale":"The DSM owner range8.8–9.0 is supported by the generic primary preparation and current API. Retain it only for that source branch; the primary9.5 adjustment is explicitly for DSM26308, not the selected DSM14708 wrapper.","source_stage":"Generic DSM813 pH","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 18-23","quote":"Dissolve the ingredients (except carbonate, sulfide, formate and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate\nand sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into\nanoxic Hungate-type tubes or serum vials and autoclave. Before use add formate and\nvitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100%\nN2 gas.","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.medium","quote":"{\n            \"id\": 813,\n            \"name\": \"DESULFONATRONUM MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 8.8,\n            \"max_pH\": 9,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf\"\n        }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The DSM owner range8.8–9.0 is supported by the generic primary preparation and current API. Retain it only for that source branch; the primary9.5 adjustment is explicitly for DSM26308, not the selected DSM14708 wrapper."}]},{"quantity_id":"q39","label":"Unresolved KOMODO pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ph_value","stored":9.5},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ph_value","stored":9.5},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ph_value","stored":9.5}],"decision":"unsupported","rationale":"These existing9.5 values agree with historical KOMODO mapping metadata but their exact current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not automatically overwrite these values from the DSM base.","source_stage":"Unresolved KOMODO branch pH","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 18-27","quote":"Dissolve the ingredients (except carbonate, sulfide, formate and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate\nand sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into\nanoxic Hungate-type tubes or serum vials and autoclave. Before use add formate and\nvitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100%\nN2 gas.\n\n\nFor DSM 26308: Replace formate with 2.0 g/l Na-L-lactate and adjust pH of the complete\nmedium to 9.5.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ph_value","decision":"unsupported","rationale":"These existing9.5 values agree with historical KOMODO mapping metadata but their exact current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not automatically overwrite these values from the DSM base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ph_value","decision":"unsupported","rationale":"These existing9.5 values agree with historical KOMODO mapping metadata but their exact current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not automatically overwrite these values from the DSM base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ph_value","decision":"unsupported","rationale":"These existing9.5 values agree with historical KOMODO mapping metadata but their exact current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not automatically overwrite these values from the DSM base."}]},{"quantity_id":"q40","label":"Retained DSM main preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve the ingredients (except carbonate, sulfide,  formate and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add  formate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas."}}],"decision":"evidence_only","rationale":"The existing AUTOCLAVE step preserves generic DSM813 carbonate/sulfide order,100%N2 for30–45min,pH8.8–9.0,anoxic dispensing and later filtered formate/vitamins. The target and KOMODO owners lack it, but direct transfer awaits branch resolution; current generated loss and source ambiguity are distinct.","source_stage":"DSM813 main preparation","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 18-23","quote":"Dissolve the ingredients (except carbonate, sulfide, formate and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate\nand sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into\nanoxic Hungate-type tubes or serum vials and autoclave. Before use add formate and\nvitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100%\nN2 gas.","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Dissolve the ingredients (except carbonate, sulfide,  formate and vitamins) and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Before use add  formate and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared under 100% N2 gas.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The existing AUTOCLAVE step preserves generic DSM813 carbonate/sulfide order,100%N2 for30–45min,pH8.8–9.0,anoxic dispensing and later filtered formate/vitamins. The target and KOMODO owners lack it, but direct transfer awaits branch resolution; current generated loss and source ambiguity are distinct."}]},{"quantity_id":"q41","label":"Retained DSM SL-10 preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The complete DISSOLVE text and1000ml make-up are supported, but their root sequence placement lacks SL-10 stock scope. Bind this step to SL-10 while retaining the existing main preparation and its different volume context.","source_stage":"DSM813 SL-10 stock preparation","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The complete DISSOLVE text and1000ml make-up are supported, but their root sequence placement lacks SL-10 stock scope. Bind this step to SL-10 while retaining the existing main preparation and its different volume context."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml":null,"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml":null,"data/normalized_yaml/bacterial/for_dsm_14708.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:006536.

All asserted ontology objects were checked for current labels, formulas, hydrate and stereo scope. Catalogue synonyms and preferred rows were joined exactly; broad extra synonym mappings do not certify a different salt or hydrate. Exact rejected spellings can coexist with mapped equivalent names. Missing yeast secondary links are a bounded completeness follow-up, without inventing a new asserted identifier. All current assertions were inspected across all four layers. Neutral resazurin and anhydrous nickel are confirmed supplied-name mismatches. D-calcium pantothenate31345 is positively supported by current synonyms/stereochemistry; generic16494 is compatible with retained DL-lipoic wording without encoding an exact racemate. B12 remains a class. No molar-rate conversion or unrelated catalogue hydrate is endorsed.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:006536.

All seven full reports and five selected historical objects were read, including three complete concentration plans and two older topology proposals. Every unchanged local/relationship claim and all111 current API source objects in those plans join; their raw digest equals the fresh response. The historical mapping-table excerpts remain unrecovered403 context, not current catalogue proof. The repaired maintained strain boundary is credited; the older ingredient-only SOURCE_DUPLICATE proposal is not adopted. Present repair, resolver and merger behavior is assessed separately from the historical execution, with malformed/naive events and fixed-time replacement left as explicit provenance concerns.

## Findings

### f1: The generated merge collapses a strain-specific contributor and unresolved source conditions

major / open / confirmed; issue key: culturemech-006536-identity-and-staleness.

The generated child relationship still says SOURCE_DUPLICATE for DSM14708, while current maintained relationships correctly preserve a STRAIN_SPECIFIC_VARIANT under the DSM owner. Current DSM14708 catalogue identifies environmental Desulfonatronum thiodismutans and points to813a, whereas the historical KOMODO813.1 link points to813. Both exact KOMODO routes fail403. Keep the branch unresolved and preserve its historical linkage; do not transfer813a or the primary DSM26308 exception. Regenerate only after source identity is reconciled, using the current conservative merger which distinguishes notes,pH,preparation and relationship fields.

### f2: Nineteen stock strengths are unqualified main ingredients

major / open / confirmed; issue key: culturemech-006536-stock-stage.

For the DSM owner, preserve eleven provider main rates on declared API1002ml basis and restore nineteen SL-10/vitamin stock entries plus their separate1ml batch doses. The primary itself does not state a main final volume. Target and KOMODO copies retain unresolved branch support rather than receiving automatic DSM evidence. Existing numerical agreement is not stage or formulation equivalence. Current API composition and solution parsing improve stock separation, but bare-ml normalization still requires explicit source basis.

### f3: SL-10 HCl mass conversion remains unsupported

major / open / confirmed; issue key: culturemech-006536-acid-percent-basis.

Retain the exact10ml HCl(25%) input and1000ml SL-10 final make-up. The provider2.5g/L assertion does not establish percent basis or density, and must not be treated as primary-certified mass or a final-medium rate. Resolve stock representation separately from KOMODO branch identity.

### f4: Asserted sodium resazurin and nickel hydrate use incompatible chemical forms

major / open / confirmed; issue key: culturemech-006536-supplied-forms.

The current supplied name sodium resazurin is paired with neutral CHEBI:8806; resolve the exact sodium-salt ID/label without guessing. CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do not reject the whole identifier. Correct both actual nickel slots while retaining source-stage quantity limits. These name-versus-identifier defects are assessable even where branch quantities remain unresolved.

### f5: Supported DSM preparation is lost in the merge and SL-10 lacks stock scope

major / open / confirmed; issue key: culturemech-006536-preparation-scope.

Preserve the DSM owner main preparation and pH8.8–9.0. Bind its existing SL-10 DISSOLVE/make-up step only to the trace stock. The generated target omits both despite listing the DSM owner; address this through source-resolved regeneration, not by blindly assigning DSM conditions to unresolved KOMODO branches. Current preparation parser still concatenates solution-stage steps, while current resolver does not copy ph_range or preparation.

### f6: Historical timestamp defects and a replacing repair writer limit provenance

minor / open / confirmed; issue key: culturemech-006536-event-metadata.

Preserve existing historical strings, including2026-01-27T01:15:03.fZ and naive February resolver timestamps. Current importer uses a %f format with time.strftime; current resolver uses naive datetime.now().isoformat(). The topology repair also fixes TIMESTAMP and replaces matching curator/action events. Future writers should emit actual timezone-aware timestamps and append new clarification events without altering prior entries; do not invent original times or claim historical code execution from present bodies.

### f7: No attached evidence distinguishes supported and unresolved layers

minor / open / confirmed; issue key: culturemech-006536-claim-evidence.

Attach literal ingredient evidence for supported DSM amounts/forms and root evidence with exact field/stage scope for stock doses,water,pH and preparation. Keep KOMODO quantity support unresolved until exact branch sources are recovered. Historical API byte matches and parent proposals are separate evidence, not attached recipe claims or proof of original execution.

## Recommended Actions And Acceptance Checks

### a1

The generated child relationship still says SOURCE_DUPLICATE for DSM14708, while current maintained relationships correctly preserve a STRAIN_SPECIFIC_VARIANT under the DSM owner. Current DSM14708 catalogue identifies environmental Desulfonatronum thiodismutans and points to813a, whereas the historical KOMODO813.1 link points to813. Both exact KOMODO routes fail403. Keep the branch unresolved and preserve its historical linkage; do not transfer813a or the primary DSM26308 exception. Regenerate only after source identity is reconciled, using the current conservative merger which distinguishes notes,pH,preparation and relationship fields.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

For the DSM owner, preserve eleven provider main rates on declared API1002ml basis and restore nineteen SL-10/vitamin stock entries plus their separate1ml batch doses. The primary itself does not state a main final volume. Target and KOMODO copies retain unresolved branch support rather than receiving automatic DSM evidence. Existing numerical agreement is not stage or formulation equivalence. Current API composition and solution parsing improve stock separation, but bare-ml normalization still requires explicit source basis.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Retain the exact10ml HCl(25%) input and1000ml SL-10 final make-up. The provider2.5g/L assertion does not establish percent basis or density, and must not be treated as primary-certified mass or a final-medium rate. Resolve stock representation separately from KOMODO branch identity.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

The current supplied name sodium resazurin is paired with neutral CHEBI:8806; resolve the exact sodium-salt ID/label without guessing. CHEBI:34887 is anhydrous nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542 explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704 is MAPPED. These spelling-specific statuses do not reject the whole identifier. Correct both actual nickel slots while retaining source-stage quantity limits. These name-versus-identifier defects are assessable even where branch quantities remain unresolved.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

Preserve the DSM owner main preparation and pH8.8–9.0. Bind its existing SL-10 DISSOLVE/make-up step only to the trace stock. The generated target omits both despite listing the DSM owner; address this through source-resolved regeneration, not by blindly assigning DSM conditions to unresolved KOMODO branches. Current preparation parser still concatenates solution-stage steps, while current resolver does not copy ph_range or preparation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

Preserve existing historical strings, including2026-01-27T01:15:03.fZ and naive February resolver timestamps. Current importer uses a %f format with time.strftime; current resolver uses naive datetime.now().isoformat(). The topology repair also fixes TIMESTAMP and replaces matching curator/action events. Future writers should emit actual timezone-aware timestamps and append new clarification events without altering prior entries; do not invent original times or claim historical code execution from present bodies.

- Original history entries remain byte-preserved; any clarification is append-only and supported by an exact verified source.
- Future importer/resolver timestamps parse as actual timezone-aware instants; repeated topology operations do not replace prior events or reuse a fixed event date.
- Recheck generated provenance and all affected native diagnostic scopes after maintained-source curation.

### a7

Attach literal ingredient evidence for supported DSM amounts/forms and root evidence with exact field/stage scope for stock doses,water,pH and preparation. Keep KOMODO quantity support unresolved until exact branch sources are recovered. Historical API byte matches and parent proposals are separate evidence, not attached recipe claims or proof of original execution.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz813 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf; REVIEW_WORK/batch077/source01-03-supplement/dsmz813.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api813 | https://mediadive.dsmz.de/rest/medium/813; REVIEW_WORK/batch077/source01-03-supplement/api813.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo813 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=813; REVIEW_WORK/batch077/source01-03-supplement/komodo813.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo813.1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=813.1; REVIEW_WORK/batch077/source01-03-supplement/komodo813.1.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodolist | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch077/source01-03-supplement/komodolist.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| dsm14708 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-14708; REVIEW_WORK/batch077/source01-03-supplement/dsm14708.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch077/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/desulfonatronum_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-3 | data/normalized_yaml/bacterial/for_dsm_14708.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_14708.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_14708.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/media_variant_link_proposals.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-28 | reports/media_variant_parent_group_proposals.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| historical-reading | REVIEW_WORK/batch077/record03/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch077/record03/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch077/record03/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_composition_ingredients; _parse_api_composition; _is_api_stock_addition; _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps; _classify_preparation_action | context_only | Current composition parsing reads the first API solution only, skips water and explicit stock or percent-bearing ml references, and prioritizes supplied g_l. Solution parsing preserves the first-section stock references but normalizes bare ml to ML_PER_L. Preparation parsing concatenates every solution step without stage labels. For all-stock primary tables, API composition returns None and PDF fallback or a placeholder remains possible; no regeneration outcome is presumed. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| full-history-pool | REVIEW_WORK/batch077/validation-authors/full-history-pool.json; Complete artifact | context_only | All thirteen reports across these three records are losslessly routed through 619 exact cells; each selected record retains its own complete report reader. No neighboring formulation transfer. |
| full-catalog | REVIEW_WORK/batch077/validation-authors/mim-full-scope.json; Complete artifact | context_only | All exact asserted identifier/ontology_id and supplied-name catalogue joins, plus candidate nickel hexahydrate; preferred-label statuses are interpreted separately from chemical identity. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver._build_dsmz_index; extract_dsmz_id; merge_composition; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver indexes DSMZ_* files, strips alphabetic suffixes, copies ingredients/solutions and only fills absent scalar ph_value. It does not copy ph_range or preparation. Its event uses naive datetime.now().isoformat(). Historical events record a DSM813 ingredient copy; current body does not prove the old execution. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current converter carries table pH and aerobic metadata and formats the timestamp with time.strftime using %f. Existing historical bytes contain literal .fZ, a different statement from the code format string; old values must remain append-only. |
| writer-repair813 | scripts/repair_komodo_813_desulfonatronum_score10.py; SIGNATURE; CHILDREN; _require_record; repair_parent; repair_child; _upsert_event; TIMESTAMP | context_only | Current repair guards all three IDs/source terms and a30-ingredient signature, then re-roots the DSM owner with a source duplicate and a separate strain-specific child; it excludes813a/813b. It does not verify external formulation equivalence, pH or atmosphere. TIMESTAMP is fixed and _upsert_event replaces a matching curator/action event, requiring an append-only future-writer correction. |
| selected-parent-authentication | REVIEW_WORK/batch077/record03/selected-parent-authentication.json; Complete artifact | context_only | Exact selected parent objects, unchanged current local fields and all literal/decoded current API claims checked separately from attached evidence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch077/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch077/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch077/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch077/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch077/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch077/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806; REVIEW_WORK/batch077/source01-03-supplement/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch077/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209; REVIEW_WORK/batch077/source01-03-supplement/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62965; REVIEW_WORK/batch077/source01-03-supplement/chebi62965.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch077/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch077/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch077/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch077/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch077/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch077/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch077/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch077/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch077/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; REVIEW_WORK/batch077/source01-03-supplement/chebi15956.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; REVIEW_WORK/batch077/source01-03-supplement/chebi27470.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; REVIEW_WORK/batch077/source01-03-supplement/chebi30961.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; REVIEW_WORK/batch077/source01-03-supplement/chebi49105.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; REVIEW_WORK/batch077/source01-03-supplement/chebi17015.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; REVIEW_WORK/batch077/source01-03-supplement/chebi15940.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; REVIEW_WORK/batch077/source01-03-supplement/chebi31345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843; REVIEW_WORK/batch077/source01-03-supplement/chebi176843.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; REVIEW_WORK/batch077/source01-03-supplement/chebi30753.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; REVIEW_WORK/batch077/source01-03-supplement/chebi16494.json; exact original raw/text/hash/time metadata | context_only | Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch077/record03/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch077/record03/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch077/record03/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch077/record03/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch077/record03/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch077/record03/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch077/record03/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch077/record03/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch077/record03/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch077/record03/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch077/record03/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch077/record03/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Exact KOMODO MediaInfo813/813.1 and MediaList GETs returned403. Their historical mapping snippets remain context; quantity support is not inherited from the DSM base.
- Current DSM14708 catalogue is identity/risk/source-link evidence only. Its813a formulation and cultivation conditions are not imported; publisher captures of813a are not recipe evidence for this record.
- The generic primary DSM26308 lactate/pH9.5 exception is excluded; it does not resolve the separate DSM14708 wrapper.
- Main API1002ml normalization is declared provider basis, while the primary1000ml water is input. SL-10 alone explicitly makes up to1000ml; HCl25% basis is unresolved.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T202356Z-culturemech-006536-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFONATRONUM medium'
started_at: '2026-10-28T20:15:17.654745Z'
finished_at: '2026-10-28T20:23:56.081180Z'
reviewer:
  identity: Codex batch006_validation
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, exact
    captured sources, fresh scoped primary sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: The selected merge collapses a maintained strain-specific wrapper and loses
  DSM preparation while carrying unresolved KOMODO pH/atmosphere. Preserve eleven
  supported DSM provider rates, restore nineteen stock-stage entries, resolve source
  identity and chemical-form mismatches, and retain explicit provenance limits.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/SKILL.md
    sha256: a67993ef11cf374ac579c53252bc603f9894ebd69cad711b11f293714c76621e
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
    sha256: d9c98e679fbb6944fc63e9b687298293a410552e1ab848eb973d7145a402cf98
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    sha256: 3d13f65856319a102817dbc0b887f49dbddff51f5bac490bc13b9ebd76eb9919
    role: context
  - path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    sha256: 0f781872ebc2e1cd91cda0a5bf872e3cf31cd0981e19490d30fae2e3bafa2580
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    sha256: c1578adbd637b8fbc992cd8ac1525a8184d20878ac91bee07ef29c892c0ab5ac
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
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
    sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml.md
    sha256: a87fa9ca47f23c6cb3fe5909e5ea7c0257d775d285d991c5b0098d5d5e0759cb
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_14708.yaml.md
    sha256: 389a94a352d3d0605781283d12e2b17308d94430e00a1c56fcac48e4e33a38f5
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_medium.yaml.md
    sha256: 8d4fefc09436aa34c9874bbb9eb038b9f16f92a4250831c219d7fcb5026fac04
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_MEDIUM.md
    sha256: 6a8d0814eea62adfa9791cd19650e5b4085a60f0bed98f7f1ea52f3e190b4867
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.md
    sha256: a705a7f75e5c40266a34329156ea3e3b56a23b65f0e9aa0ef6f46126c07976e7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_medium.md
    sha256: a72ec75aac1ac85e637778923fe64c73c267630edb79471fbd10be9214996fb0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_14708.md
    sha256: a4ec238f21264c0e3ded5beba54f4ec0a303f608b758f82ae5883ed9d1475220
    role: context
  - path: reports/media_variant_link_proposals.json
    sha256: e677817f1c836813f771acdc7208cc820c4bca30e1022e62d4d89d8bf21a69c2
    role: context
  - path: reports/media_variant_parent_group_proposals.json
    sha256: 1baefa1e8b0e9b9eee23f5daac577f978c528680b940f14ecd6361fc7425b67a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_komodo_813_desulfonatronum_score10.py
    sha256: 31cd10cce6947e50d402f8dc8cfa9606bbf3037bc0b8e9f1c0248950f76ddca2
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
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
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Whole exact target/owner with explicit scoped dependencies, current
    sources and historical claims.
  selection: Authoritative batch077 index 03
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006536
targets:
- target_id: CultureMech:006536
  path: data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
  label: desulfonatronum_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:006536
  command: just validate-schema data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:006536
  command: just validate-strict data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
    --out REVIEW_WORK/batch077/record03/strict.tsv --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:006536
  command: just validate-terms data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:006536
  command: just validate-references data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz813
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf
  accessed_at: '2026-10-28T20:15:33.772748Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/dsmz813.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161
- evidence_id: api813
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/813
  accessed_at: '2026-10-28T20:15:33.481908Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/api813.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122
- evidence_id: komodo813
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=813
  accessed_at: '2026-10-28T20:15:33.230368Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/komodo813.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 881adc87c878250648c0feca3174071f668b6946de9bcb312618c82f926d394f
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=813;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo813.1
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=813.1
  accessed_at: '2026-10-28T20:15:33.234474Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/komodo813.1.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e23b5de33afa788457990396d46e5471cd571a8e1a58303dc94139ec83eec5a
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=813.1;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodolist
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T20:15:33.337832Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/komodolist.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 417fcfc20b41f371f0f0ca89948e14e4c61993e6c49c899bdc7358077d7cdfd9
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: dsm14708
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-14708
  accessed_at: '2026-10-28T20:15:35.006006Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/dsm14708.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d7f029d7c4abb9e0fa9feb6422ce8ff2e10533ac9691bd4f5cf7a98d0b9091ca
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T20:15:38.694861Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:23:55.742426Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: d9c98e679fbb6944fc63e9b687298293a410552e1ab848eb973d7145a402cf98
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:23:55.742597Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 3d13f65856319a102817dbc0b887f49dbddff51f5bac490bc13b9ebd76eb9919
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T20:23:55.742627Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T20:23:55.742936Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T20:23:55.742960Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T20:23:55.742981Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:23:55.743006Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 0f781872ebc2e1cd91cda0a5bf872e3cf31cd0981e19490d30fae2e3bafa2580
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_14708.yaml
  locator: Complete file
  accessed_at: '2026-10-28T20:23:55.743028Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: c1578adbd637b8fbc992cd8ac1525a8184d20878ac91bee07ef29c892c0ab5ac
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:23:55.743050Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1eec521fb8743316925ed3d629323b5c1312db0b35497db1e8bbe560a13e3508
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.750586Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a87fa9ca47f23c6cb3fe5909e5ea7c0257d775d285d991c5b0098d5d5e0759cb
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_14708.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.750645Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 389a94a352d3d0605781283d12e2b17308d94430e00a1c56fcac48e4e33a38f5
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:23:55.750682Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfonatronum_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.757268Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 8d4fefc09436aa34c9874bbb9eb038b9f16f92a4250831c219d7fcb5026fac04
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFONATRONUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.757350Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 6a8d0814eea62adfa9791cd19650e5b4085a60f0bed98f7f1ea52f3e190b4867
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.757385Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a705a7f75e5c40266a34329156ea3e3b56a23b65f0e9aa0ef6f46126c07976e7
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfonatronum_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.757415Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a72ec75aac1ac85e637778923fe64c73c267630edb79471fbd10be9214996fb0
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_14708.md
  locator: Complete report
  accessed_at: '2026-10-28T20:23:55.757439Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a4ec238f21264c0e3ded5beba54f4ec0a303f608b758f82ae5883ed9d1475220
- evidence_id: report-27
  kind: prior_review
  reference: reports/media_variant_link_proposals.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:23:55.757467Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: e677817f1c836813f771acdc7208cc820c4bca30e1022e62d4d89d8bf21a69c2
- evidence_id: report-28
  kind: prior_review
  reference: reports/media_variant_parent_group_proposals.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:23:55.758005Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1baefa1e8b0e9b9eee23f5daac577f978c528680b940f14ecd6361fc7425b67a
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/historical-reading.json
  accessed_at: '2026-10-28T20:23:55.758141Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: 6c9dbfb20c33b3ac88581ca25660574a11a7c89031c589311668eedf59a2b595
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T20:23:55.758483Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: f15d5565025914634c9dcbe9c376a258850789fe642d7f9b232095f4fa51252a
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/complete-document-reader.json
  accessed_at: '2026-10-28T20:23:55.758579Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 4b472cbad0225c294f9e7be6f5fb29865f6bab2f47ecc41928bb9ca19f90aa9f
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_composition_ingredients; _parse_api_composition; _is_api_stock_addition;
    _api_stock_name; _parse_api_solutions; _normalize_unit; _parse_preparation_steps;
    _classify_preparation_action
  accessed_at: '2026-10-28T20:23:55.758763Z'
  support: context_only
  summary: Current composition parsing reads the first API solution only, skips water
    and explicit stock or percent-bearing ml references, and prioritizes supplied
    g_l. Solution parsing preserves the first-section stock references but normalizes
    bare ml to ML_PER_L. Preparation parsing concatenates every solution step without
    stage labels. For all-stock primary tables, API composition returns None and PDF
    fallback or a placeholder remains possible; no regeneration outcome is presumed.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T20:23:55.758825Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: full-history-pool
  kind: record_content
  reference: REVIEW_WORK/batch077/validation-authors/full-history-pool.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:23:55.758864Z'
  support: context_only
  summary: All thirteen reports across these three records are losslessly routed through
    619 exact cells; each selected record retains its own complete report reader.
    No neighboring formulation transfer.
  snapshot_sha256: 35d1e79d61d4d348a952a6faa00bfb1a397d30f96995ea913be0822f2024612e
- evidence_id: full-catalog
  kind: record_content
  reference: REVIEW_WORK/batch077/validation-authors/mim-full-scope.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:23:55.758962Z'
  support: context_only
  summary: All exact asserted identifier/ontology_id and supplied-name catalogue joins,
    plus candidate nickel hexahydrate; preferred-label statuses are interpreted separately
    from chemical identity.
  snapshot_sha256: 741b684f47194d97bb0a782ece7136465d7c31c2d1c94480aad6d3518ef55158
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver._build_dsmz_index; extract_dsmz_id; merge_composition;
    _add_enrichment_metadata
  accessed_at: '2026-10-28T20:23:55.759061Z'
  support: context_only
  summary: Current DSMZCompositionResolver indexes DSMZ_* files, strips alphabetic
    suffixes, copies ingredients/solutions and only fills absent scalar ph_value.
    It does not copy ph_range or preparation. Its event uses naive datetime.now().isoformat().
    Historical events record a DSM813 ingredient copy; current body does not prove
    the old execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T20:23:55.759088Z'
  support: context_only
  summary: Current converter carries table pH and aerobic metadata and formats the
    timestamp with time.strftime using %f. Existing historical bytes contain literal
    .fZ, a different statement from the code format string; old values must remain
    append-only.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-repair813
  kind: record_content
  reference: scripts/repair_komodo_813_desulfonatronum_score10.py
  locator: SIGNATURE; CHILDREN; _require_record; repair_parent; repair_child; _upsert_event;
    TIMESTAMP
  accessed_at: '2026-10-28T20:23:55.759112Z'
  support: context_only
  summary: Current repair guards all three IDs/source terms and a30-ingredient signature,
    then re-roots the DSM owner with a source duplicate and a separate strain-specific
    child; it excludes813a/813b. It does not verify external formulation equivalence,
    pH or atmosphere. TIMESTAMP is fixed and _upsert_event replaces a matching curator/action
    event, requiring an append-only future-writer correction.
  snapshot_sha256: 31cd10cce6947e50d402f8dc8cfa9606bbf3037bc0b8e9f1c0248950f76ddca2
- evidence_id: selected-parent-authentication
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/selected-parent-authentication.json
  locator: Complete artifact
  accessed_at: '2026-10-28T20:23:55.892562Z'
  support: context_only
  summary: Exact selected parent objects, unchanged current local fields and all literal/decoded
    current API claims checked separately from attached evidence.
  snapshot_sha256: 61e3226352fc0f5daadf9b70ad9e3272de965fa3f30f9dded9c128eb48cb0880
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T20:15:38.928795Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T20:15:40.018436Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T20:15:36.517340Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T20:15:37.461125Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T20:15:37.110930Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T20:15:35.818421Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:8806
  accessed_at: '2026-10-28T20:15:40.227947Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi8806.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f2530ec9c15f59a3d132a466c9c3a899497bab0f85b996d3e27bef8612f89982
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T20:15:35.931240Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:76209
  accessed_at: '2026-10-28T20:15:39.562551Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi76209.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4896ec517123ebeb1afcbac7bc30a7103976f03891af0c86c992196b5f0db969
- evidence_id: chebi62965
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62965
  accessed_at: '2026-10-28T20:15:38.826774Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi62965.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: cfd1c5de376b9874afbc0c231dfd94f0b4954f4b69c40062783876093e7f0354
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T20:15:35.346986Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T20:15:39.644345Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T20:15:38.325603Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T20:15:40.167533Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T20:15:37.732850Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T20:15:38.429348Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T20:15:39.888563Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T20:15:37.828199Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T20:15:39.301964Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  accessed_at: '2026-10-28T20:15:34.591885Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi15956.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  accessed_at: '2026-10-28T20:15:35.966282Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi27470.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  accessed_at: '2026-10-28T20:15:36.413596Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi30961.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  accessed_at: '2026-10-28T20:15:38.248432Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi49105.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  accessed_at: '2026-10-28T20:15:35.268960Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi17015.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  accessed_at: '2026-10-28T20:15:34.543633Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi15940.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  accessed_at: '2026-10-28T20:15:36.590790Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi31345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:176843
  accessed_at: '2026-10-28T20:15:35.188321Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi176843.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9c73ea31864abce6b9ed6328e9ed491bc1cad2ba27f40adb5c00f0f192838e63
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  accessed_at: '2026-10-28T20:15:36.260740Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi30753.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  accessed_at: '2026-10-28T20:15:34.708700Z'
  locator: REVIEW_WORK/batch077/source01-03-supplement/chebi16494.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch077 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.078824Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 99792ffcbcf8a163e2fabfe70900a683a3a892632a3ae99dbbe0ebc88b68a79f
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.078948Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: e1149d217e8d4b60e60d24fb3418ca1a47d1cca311dfe0ee56cd76b40aac9641
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.079119Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: 3d07de3912cd042017446ab179ea86e60072c6dca329b930e3c17b6f6303e99d
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.079210Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 18444fdef4bd7e7f9ba570e9a42280e4821af23da726cf27747cff8405f556de
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.079300Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 2ba808450768c1babdb4f943cb43d8a317b64c5689e154aa3d5ace2a908a2751
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.079327Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: ed016289c07d5d9348a4fa405908f7cc5c1a0c0e1b576be76ad548fd99dc3e3a
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T20:23:56.079348Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch077/record03/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T20:23:56.079366Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: 676da98e1d8b9ac00553b538f8d2f93f74940f2938825006698bfa9a5903ceef
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch077/record03/validate-schema.json
  accessed_at: '2026-10-28T20:15:18.723529Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 6611d7bcc9474fa4c375f69c0a1081c3e3ed08e10176c980ca022fa58cd66e4f
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch077/record03/validate-strict.json
  accessed_at: '2026-10-28T20:15:19.651329Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 4c6e9e239af0cb9a2e4080b6ca6663ba7d77666cc81a3fb803d5dce79ef8d777
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch077/record03/validate-terms.json
  accessed_at: '2026-10-28T20:15:20.674091Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c76087000c2db833bb3a6ccfb6fd65540a687200de348648dd1aedb5ecc7ac96
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch077/record03/validate-references.json
  accessed_at: '2026-10-28T20:15:21.411932Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 9f9d1690368c6a46ecad9e7e5edbb2b20c5dbdd5f466a03b39fe5c8bf66b749e
assessments:
- assessment_id: identity
  area: identity
  topic: DSM813, KOMODO813 and DSM14708 wrapper
  outcome: concern
  summary: Three maintained contributors have equal copied ingredient lists but different
    source conditions and current relationships. The current catalogue points DSM14708
    to813a; it does not retroactively authenticate the historical813 link. The selected
    merge loses the maintained strain boundary. Exact KOMODO routes403 limit completion;
    no source-growth claim is inferred.
  target_ids:
  - CultureMech:006536
  evidence_ids:
  - target
  - owner
  - owner-2
  - owner-3
  - dsm14708
  - dsmz813
  - komodo813
  - komodo813.1
  - historical-selected-parent-rows
  - writer-repair813
- assessment_id: classification
  area: representation
  topic: Complex liquid representation
  outcome: supported
  summary: Yeast extract supports complex/undefined classification and the generic
    DSM formulation lacks a solidifier. This classification does not resolve the separate
    pH/atmosphere or strain-link issue.
  target_ids:
  - CultureMech:006536
  evidence_ids:
  - target
  - dsmz813
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 120 current concentration fields are covered by 41 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:006536
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b077-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","quantity_field_count":120,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 3-3","quote":"KH2PO4                                                     0.20         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    1.46674,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[0].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q2","label":"MgCl2 x
    6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.0998004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 4-4","quote":"MgCl2 x 6 H2O                                              0.10         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0998004,\n                        \"mmol_l\":
    0.490895,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[1].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q3","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 5-5","quote":"NH4Cl                                                      1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"mmol_l\":
    18.6578,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[2].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q4","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.199601","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 6-6","quote":"KCl                                                        0.20         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199601,\n                        \"mmol_l\":
    2.67741,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[3].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q5","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[4].concentration","stored":{"value":"4.99002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 7-7","quote":"Na2SO4                                                     5.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4.99002,\n                        \"mmol_l\":
    35.1311,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[4].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[5].concentration","stored":{"value":"9.98004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 8-8","quote":"NaCl                                                      10.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 9.98004,\n                        \"mmol_l\":
    170.774,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[5].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q7","label":"Yeast extract","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.998004","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 10-10","quote":"Yeast extract                                              1.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.998004,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[6].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q8","label":"Sodium
    resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.000499002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin
    stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible;
    neutral CHEBI grounding is a separate issue.","source_stage":"DSM813 main medium
    / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 11-11","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin
    stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible;
    neutral CHEBI grounding is a separate issue."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin
    stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible;
    neutral CHEBI grounding is a separate issue."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[7].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base. The primary0.5ml
    of0.1% w/v sodium-resazurin stock gives0.5mg in the DSM batch. Its exact dose/strength
    must remain visible; neutral CHEBI grounding is a separate issue."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base. The primary0.5ml of0.1% w/v sodium-resazurin
    stock gives0.5mg in the DSM batch. Its exact dose/strength must remain visible;
    neutral CHEBI grounding is a separate issue."}]},{"quantity_id":"q9","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[8].concentration","stored":{"value":"3.49301","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 12-12","quote":"Na2CO3                                                     3.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 3.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.49301,\n                        \"mmol_l\":
    32.9567,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[8].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q10","label":"Na2S x
    9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[9].concentration","stored":{"value":"0.499002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 13-13","quote":"Na2S x 9 H2O                                               0.50         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.499002,\n                        \"mmol_l\":
    2.0776,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[9].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q11","label":"Na-formate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[10].concentration","stored":{"value":"3.99202","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base.","source_stage":"DSM813 main medium / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 14-14","quote":"Na-formate                                                 4.00         g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[11]","quote":"{\n                        \"recipe_order\":
    12,\n                        \"compound\": \"Na-formate\",\n                        \"compound_id\":
    144,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.99202,\n                        \"mmol_l\":
    58.6999,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[10].concentration","decision":"evidence_only","rationale":"Exact
    DSM branch: The DSM owner scalar agrees with the exact current provider main g_l
    and source batch mass. Credit that declared API1002ml normalization without claiming
    a measured primary final volume: this exact primary lists1000ml water but does
    not state a main final make-up. The target and two KOMODO contributors copy the
    same scalar, but their different pH/atmosphere and unresolved exact source branch
    prevent transferring DSM quantity support. Preserve all numbers while resolving
    identity; do not silently change the KOMODO branch to the base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar agrees with the exact current provider main g_l and source batch
    mass. Credit that declared API1002ml normalization without claiming a measured
    primary final volume: this exact primary lists1000ml water but does not state
    a main final make-up. The target and two KOMODO contributors copy the same scalar,
    but their different pH/atmosphere and unresolved exact source branch prevent transferring
    DSM quantity support. Preserve all numbers while resolving identity; do not silently
    change the KOMODO branch to the base."}]},{"quantity_id":"q12","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[11].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L
    scalar does not establish percent basis or density; do not endorse its conversion,
    and correct the DSM stock placement. Target and KOMODO copies remain unsupported
    pending exact branch identity. Preserve the source volume/percent assertions without
    guessing w/v.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 32-32","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L
    scalar does not establish percent basis or density; do not endorse its conversion,
    and correct the DSM stock placement. Target and KOMODO copies remain unsupported
    pending exact branch identity. Preserve the source volume/percent assertions without
    guessing w/v."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L
    scalar does not establish percent basis or density; do not endorse its conversion,
    and correct the DSM stock placement. Target and KOMODO copies remain unsupported
    pending exact branch identity. Preserve the source volume/percent assertions without
    guessing w/v."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"Exact
    DSM branch: The primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up.
    The provider2.5g/L scalar does not establish percent basis or density; do not
    endorse its conversion, and correct the DSM stock placement. Target and KOMODO
    copies remain unsupported pending exact branch identity. Preserve the source volume/percent
    assertions without guessing w/v."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    primary specifies10ml HCl(25%) in SL-10 and a final1000ml make-up. The provider2.5g/L
    scalar does not establish percent basis or density; do not endorse its conversion,
    and correct the DSM stock placement. Target and KOMODO copies remain unsupported
    pending exact branch identity. Preserve the source volume/percent assertions without
    guessing w/v."}]},{"quantity_id":"q13","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[12].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 33-33","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q14","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 34-34","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q15","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 35-35","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q16","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 36-36","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q17","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 37-37","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q18","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 38-38","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q19","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 39-39","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q20","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[19].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml.","source_stage":"DSM813 SL-10 / unresolved KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 40-40","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[19].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. SL-10
    explicitly makes up to1000ml."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[19].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. SL-10 explicitly makes
    up to1000ml."}]},{"quantity_id":"q21","label":"Biotin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[20].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 57-57","quote":"Biotin                                     20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[20].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[20].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q22","label":"Folic acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[21].concentration","stored":{"value":"0.02","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 58-58","quote":"Folic acid                                 20.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[21].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[21].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q23","label":"Pyridoxine
    hydrochloride","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[22].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 59-59","quote":"Pyridoxine hydrochloride                  100.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[22].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[22].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q24","label":"Thiamine
    HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[23].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 60-60","quote":"Thiamine HCl                               50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[23].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[23].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q25","label":"Riboflavin","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[24].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 61-61","quote":"Riboflavin                                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[24].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[24].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q26","label":"Nicotinic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[25].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 62-62","quote":"Nicotinic acid                             50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[25].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[25].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q27","label":"Calcium
    D-(+)-pantothenate","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[26].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 63-63","quote":"Calcium D-(+)-pantothenate                 50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[26].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[26].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q28","label":"Vitamin
    B12","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[27].concentration","stored":{"value":"0.001","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 64-64","quote":"Vitamin B12                                 1.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[27].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[27].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q29","label":"p-Aminobenzoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[28].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 65-65","quote":"p-Aminobenzoic acid                        50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[28].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[28].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q30","label":"(DL)-alpha-Lipoic
    acid","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[29].concentration","stored":{"value":"0.05","unit":"G_PER_L"}}],"decision":"mixed","rationale":"The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up.","source_stage":"DSM813 Wolin10x / unresolved
    KOMODO copies","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 66-66","quote":"(DL)-alpha-Lipoic acid                     50.00   mg","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ingredients[29].concentration","decision":"correct","rationale":"Exact
    DSM branch: The DSM owner scalar matches provider stock g_l and source mass, but
    the current root ingredient placement is wrong; restore its exact stock and1ml
    batch dose. The copied target/KOMODO values remain unsupported until their branch
    formulation is resolved, even though their numbers match the DSM stock. The vitamin
    table lists1000ml water and API declares1000ml stock volume; retain this declared
    basis without inventing measured make-up."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ingredients[29].concentration","decision":"unsupported","rationale":"Unresolved
    KOMODO/generated branch: numerical equality with DSM813 does not establish its
    formulation; preserve existing values pending exact source reconciliation. The
    DSM owner scalar matches provider stock g_l and source mass, but the current root
    ingredient placement is wrong; restore its exact stock and1ml batch dose. The
    copied target/KOMODO values remain unsupported until their branch formulation
    is resolved, even though their numbers match the DSM stock. The vitamin table
    lists1000ml water and API declares1000ml stock volume; retain this declared basis
    without inventing measured make-up."}]},{"quantity_id":"q31","label":"SL-10 source
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The
    exact DSM813 primary specifies1ml into its stated batch. Restore this dose for
    the DSM branch with its stock definition; do not call bare ml a primary ml/L assertion
    or transfer it to unresolved KOMODO variants.","source_stage":"DSM813 source-only
    batch stock dose","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 9-9","quote":"Trace element solution SL-10                               1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q32","label":"Wolin10x source
    receiving dose","local_fields":[],"decision":"evidence_only","rationale":"The
    exact DSM813 primary specifies1ml into its stated batch. Restore this dose for
    the DSM branch with its stock definition; do not call bare ml a primary ml/L assertion
    or transfer it to unresolved KOMODO variants.","source_stage":"DSM813 source-only
    batch stock dose","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 15-15","quote":"Wolin''s vitamin solution (10x)                             1.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[12]","quote":"{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q33","label":"DSM sodium-resazurin
    stock controls","local_fields":[],"decision":"evidence_only","rationale":"The
    primary explicitly gives0.5ml of0.1% w/v sodium-resazurin stock, supplying0.5mg
    in the DSM batch. Preserve these controls separately from API final-rate normalization
    and unresolved KOMODO identity.","source_stage":"DSM813 source-only dye stock","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 11-11","quote":"Sodium resazurin (0.1% w/v)                                0.50        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000499002,\n                        \"mmol_l\": 0.00198671,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}],"layer_assessments":[]},{"quantity_id":"q34","label":"DSM
    main water","local_fields":[],"decision":"evidence_only","rationale":"Retain the
    exact solvent input in its source section. Main1000ml input water is not a measured
    final-volume statement. SL-10 separately makes up to1000ml; the vitamin provider
    volume is a declared normalization basis.","source_stage":"DSM813 source-only
    water","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 16-16","quote":"Distilled water                                         1000.00        ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].recipe[13]","quote":"{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q35","label":"DSM SL-10 water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact solvent input in its source section. Main1000ml input water is not a
    measured final-volume statement. SL-10 separately makes up to1000ml; the vitamin
    provider volume is a declared normalization basis.","source_stage":"DSM813 source-only
    water","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 41-41","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q36","label":"DSM vitamin water","local_fields":[],"decision":"evidence_only","rationale":"Retain
    the exact solvent input in its source section. Main1000ml input water is not a
    measured final-volume statement. SL-10 separately makes up to1000ml; the vitamin
    provider volume is a declared normalization basis.","source_stage":"DSM813 source-only
    water","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 67-67","quote":"Distilled water                          1000.00   ml","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[2].recipe[10]","quote":"{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q37","label":"DSM SL-10 final
    make-up","local_fields":[],"decision":"evidence_only","rationale":"The source
    explicitly makes up SL-10 to1000ml after acid/water inputs. This is a stock final-volume
    instruction, not the main medium denominator.","source_stage":"DSM813 stock final
    volume","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 32-32","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 41-44","quote":"Distilled water                                           990.00      ml\n\nFirst
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[]},{"quantity_id":"q38","label":"Retained DSM pH","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ph_range","stored":{"min":8.8,"max":9.0}}],"decision":"evidence_only","rationale":"The
    DSM owner range8.8–9.0 is supported by the generic primary preparation and current
    API. Retain it only for that source branch; the primary9.5 adjustment is explicitly
    for DSM26308, not the selected DSM14708 wrapper.","source_stage":"Generic DSM813
    pH","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 18-23","quote":"Dissolve the ingredients (except carbonate, sulfide, formate
    and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Add and dissolve carbonate\nand sulfide, then adjust pH to 8.8 - 9.0, dispense
    under 100% N2 gas atmosphere into\nanoxic Hungate-type tubes or serum vials and
    autoclave. Before use add formate and\nvitamins (sterilized by filtration) from
    sterile anoxic stock solutions prepared under 100%\nN2 gas.","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.medium","quote":"{\n            \"id\":
    813,\n            \"name\": \"DESULFONATRONUM MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 8.8,\n            \"max_pH\": 9,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf\"\n        }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"ph_range","decision":"evidence_only","rationale":"The
    DSM owner range8.8–9.0 is supported by the generic primary preparation and current
    API. Retain it only for that source branch; the primary9.5 adjustment is explicitly
    for DSM26308, not the selected DSM14708 wrapper."}]},{"quantity_id":"q39","label":"Unresolved
    KOMODO pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ph_value","stored":9.5},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ph_value","stored":9.5},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ph_value","stored":9.5}],"decision":"unsupported","rationale":"These
    existing9.5 values agree with historical KOMODO mapping metadata but their exact
    current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed
    DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not
    automatically overwrite these values from the DSM base.","source_stage":"Unresolved
    KOMODO branch pH","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 18-27","quote":"Dissolve the ingredients (except carbonate, sulfide, formate
    and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Add and dissolve carbonate\nand sulfide, then adjust pH to 8.8 - 9.0, dispense
    under 100% N2 gas atmosphere into\nanoxic Hungate-type tubes or serum vials and
    autoclave. Before use add formate and\nvitamins (sterilized by filtration) from
    sterile anoxic stock solutions prepared under 100%\nN2 gas.\n\n\nFor DSM 26308:
    Replace formate with 2.0 g/l Na-L-lactate and adjust pH of the complete\nmedium
    to 9.5.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml","field_path":"ph_value","decision":"unsupported","rationale":"These
    existing9.5 values agree with historical KOMODO mapping metadata but their exact
    current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed
    DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not
    automatically overwrite these values from the DSM base."},{"path":"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml","field_path":"ph_value","decision":"unsupported","rationale":"These
    existing9.5 values agree with historical KOMODO mapping metadata but their exact
    current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed
    DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not
    automatically overwrite these values from the DSM base."},{"path":"data/normalized_yaml/bacterial/for_dsm_14708.yaml","field_path":"ph_value","decision":"unsupported","rationale":"These
    existing9.5 values agree with historical KOMODO mapping metadata but their exact
    current routes return403. They differ from generic DSM813 pH8.8–9.0. The printed
    DSM26308 exception cannot establish DSM14708 or base-KOMODO equivalence; do not
    automatically overwrite these values from the DSM base."}]},{"quantity_id":"q40","label":"Retained
    DSM main preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Dissolve
    the ingredients (except carbonate, sulfide,  formate and vitamins) and sparge
    medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and dissolve carbonate
    and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100% N2 gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Before use add  formate
    and vitamins (sterilized by filtration) from sterile anoxic stock solutions prepared
    under 100% N2 gas."}}],"decision":"evidence_only","rationale":"The existing AUTOCLAVE
    step preserves generic DSM813 carbonate/sulfide order,100%N2 for30–45min,pH8.8–9.0,anoxic
    dispensing and later filtered formate/vitamins. The target and KOMODO owners lack
    it, but direct transfer awaits branch resolution; current generated loss and source
    ambiguity are distinct.","source_stage":"DSM813 main preparation","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 18-23","quote":"Dissolve the ingredients (except carbonate, sulfide, formate
    and vitamins) and sparge\nmedium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Add and dissolve carbonate\nand sulfide, then adjust pH to 8.8 - 9.0, dispense
    under 100% N2 gas atmosphere into\nanoxic Hungate-type tubes or serum vials and
    autoclave. Before use add formate and\nvitamins (sterilized by filtration) from
    sterile anoxic stock solutions prepared under 100%\nN2 gas.","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Dissolve the ingredients (except carbonate, sulfide,  formate and vitamins)
    and sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Add and
    dissolve carbonate and sulfide, then adjust pH to 8.8 - 9.0, dispense under 100%
    N2 gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Before use add  formate and vitamins (sterilized by filtration) from sterile anoxic
    stock solutions prepared under 100% N2 gas.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    existing AUTOCLAVE step preserves generic DSM813 carbonate/sulfide order,100%N2
    for30–45min,pH8.8–9.0,anoxic dispensing and later filtered formate/vitamins. The
    target and KOMODO owners lack it, but direct transfer awaits branch resolution;
    current generated loss and source ambiguity are distinct."}]},{"quantity_id":"q41","label":"Retained
    DSM SL-10 preparation","local_fields":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The complete
    DISSOLVE text and1000ml make-up are supported, but their root sequence placement
    lacks SL-10 stock scope. Bind this step to SL-10 while retaining the existing
    main preparation and its different volume context.","source_stage":"DSM813 SL-10
    stock preparation","sources":[{"evidence_id":"dsmz813","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium813.pdf","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/dsmz813.bin","raw_sha256":"f9a065d4123ad93fa97d9c044d47f79984a0cd27507a4ae8ce8f67a7f83f1161","text_sha256":"aead82d13ddad4ae2df4121e3c16dc731f3902633a15918645c7fc563c5c60fc","accessed_at":"2026-10-28T20:15:33.772748Z","locator":"dsmz813.txt
    lines 43-44","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api813","reference":"https://mediadive.dsmz.de/rest/medium/813","raw_path":"REVIEW_WORK/batch077/source01-03-supplement/api813.bin","raw_sha256":"0b201410b13bc94e639230c1c09ab08396a3dce3347d0375fc446668f3413122","text_sha256":"4eea883983842444b0d72053bab27a45168075c9c8d79de67a3aa1b3677ec5dd","accessed_at":"2026-10-28T20:15:33.481908Z","locator":"data.solutions[1].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}],"layer_assessments":[{"path":"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml","field_path":"preparation_steps[1]","decision":"correct","rationale":"The
    complete DISSOLVE text and1000ml make-up are supported, but their root sequence
    placement lacks SL-10 stock scope. Bind this step to SL-10 while retaining the
    existing main preparation and its different volume context."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFONATRONUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml":null,"data/normalized_yaml/bacterial/desulfonatronum_medium.yaml":null,"data/normalized_yaml/bacterial/for_dsm_14708.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All asserted ontology objects were checked for current labels, formulas,
    hydrate and stereo scope. Catalogue synonyms and preferred rows were joined exactly;
    broad extra synonym mappings do not certify a different salt or hydrate. Exact
    rejected spellings can coexist with mapped equivalent names. Missing yeast secondary
    links are a bounded completeness follow-up, without inventing a new asserted identifier.
    All current assertions were inspected across all four layers. Neutral resazurin
    and anhydrous nickel are confirmed supplied-name mismatches. D-calcium pantothenate31345
    is positively supported by current synonyms/stereochemistry; generic16494 is compatible
    with retained DL-lipoic wording without encoding an exact racemate. B12 remains
    a class. No molar-rate conversion or unrelated catalogue hydrate is endorsed.
  target_ids:
  - CultureMech:006536
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All seven full reports and five selected historical objects were read,
    including three complete concentration plans and two older topology proposals.
    Every unchanged local/relationship claim and all111 current API source objects
    in those plans join; their raw digest equals the fresh response. The historical
    mapping-table excerpts remain unrecovered403 context, not current catalogue proof.
    The repaired maintained strain boundary is credited; the older ingredient-only
    SOURCE_DUPLICATE proposal is not adopted. Present repair, resolver and merger
    behavior is assessed separately from the historical execution, with malformed/naive
    events and fixed-time replacement left as explicit provenance concerns.
  target_ids:
  - CultureMech:006536
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-source-joins
  - historical-reading
  - historical-selected-parent-rows
  - selected-parent-authentication
  - writer-mediadive
  - writer-resolver
  - writer-komodo
  - writer-repair813
findings:
- finding_id: f1
  issue_key: culturemech-006536-identity-and-staleness
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The generated merge collapses a strain-specific contributor and unresolved
    source conditions
  description: The generated child relationship still says SOURCE_DUPLICATE for DSM14708,
    while current maintained relationships correctly preserve a STRAIN_SPECIFIC_VARIANT
    under the DSM owner. Current DSM14708 catalogue identifies environmental Desulfonatronum
    thiodismutans and points to813a, whereas the historical KOMODO813.1 link points
    to813. Both exact KOMODO routes fail403. Keep the branch unresolved and preserve
    its historical linkage; do not transfer813a or the primary DSM26308 exception.
    Regenerate only after source identity is reconciled, using the current conservative
    merger which distinguishes notes,pH,preparation and relationship fields.
  target_ids:
  - CultureMech:006536
  field_paths:
  - variant_children
  - synonyms
  - merged_from
  - ph_value
  - notes
  evidence_ids:
  - target
  - owner
  - owner-2
  - owner-3
  - dsm14708
  - dsmz813
  - komodo813
  - komodo813.1
  - komodolist
  - writer-repair813
  - writer-formulation
  - writer-merger
  - historical-selected-parent-rows
  rule_id: custom/identity-and-staleness
  native_severity: P2
  normalization_reason: Exact source-specific identity issue, normalized major; this
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_komodo_813_desulfonatronum_score10.py
    role: current topology repair and history-event writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
- finding_id: f2
  issue_key: culturemech-006536-stock-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Nineteen stock strengths are unqualified main ingredients
  description: For the DSM owner, preserve eleven provider main rates on declared
    API1002ml basis and restore nineteen SL-10/vitamin stock entries plus their separate1ml
    batch doses. The primary itself does not state a main final volume. Target and
    KOMODO copies retain unresolved branch support rather than receiving automatic
    DSM evidence. Existing numerical agreement is not stage or formulation equivalence.
    Current API composition and solution parsing improve stock separation, but bare-ml
    normalization still requires explicit source basis.
  target_ids:
  - CultureMech:006536
  field_paths:
  - ingredients[11:30].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz813
  - api813
  - quantities
  - writer-mediadive
  - writer-resolver
  rule_id: custom/stock-stage
  native_severity: P2
  normalization_reason: Exact source-specific quantity issue, normalized major; this
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
- finding_id: f3
  issue_key: culturemech-006536-acid-percent-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: SL-10 HCl mass conversion remains unsupported
  description: Retain the exact10ml HCl(25%) input and1000ml SL-10 final make-up.
    The provider2.5g/L assertion does not establish percent basis or density, and
    must not be treated as primary-certified mass or a final-medium rate. Resolve
    stock representation separately from KOMODO branch identity.
  target_ids:
  - CultureMech:006536
  field_paths:
  - ingredients[11].concentration
  - solutions
  - evidence
  evidence_ids:
  - dsmz813
  - api813
  - quantities
  rule_id: custom/acid-percent-basis
  native_severity: P2
  normalization_reason: Exact source-specific quantity issue, normalized major; this
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
- finding_id: f4
  issue_key: culturemech-006536-supplied-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Asserted sodium resazurin and nickel hydrate use incompatible chemical forms
  description: The current supplied name sodium resazurin is paired with neutral CHEBI:8806;
    resolve the exact sodium-salt ID/label without guessing. CHEBI:34887 is anhydrous
    nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542
    explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride
    hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704
    is MAPPED. These spelling-specific statuses do not reject the whole identifier.
    Correct both actual nickel slots while retaining source-stage quantity limits.
    These name-versus-identifier defects are assessable even where branch quantities
    remain unresolved.
  target_ids:
  - CultureMech:006536
  field_paths:
  - ingredients[7].term
  - ingredients[18].term
  - ingredients[18].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz813
  - api813
  - groundings
  - chebi53542
  - full-catalog
  rule_id: custom/supplied-forms
  native_severity: P2
  normalization_reason: Exact source-specific grounding issue, normalized major; this
    custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-006536-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Supported DSM preparation is lost in the merge and SL-10 lacks stock scope
  description: Preserve the DSM owner main preparation and pH8.8–9.0. Bind its existing
    SL-10 DISSOLVE/make-up step only to the trace stock. The generated target omits
    both despite listing the DSM owner; address this through source-resolved regeneration,
    not by blindly assigning DSM conditions to unresolved KOMODO branches. Current
    preparation parser still concatenates solution-stage steps, while current resolver
    does not copy ph_range or preparation.
  target_ids:
  - CultureMech:006536
  field_paths:
  - preparation_steps
  - ph_value
  - data/normalized_yaml/bacterial/desulfonatronum_medium.yaml::preparation_steps[1]
  evidence_ids:
  - dsmz813
  - api813
  - quantities
  - writer-mediadive
  - writer-resolver
  - writer-merger
  rule_id: custom/preparation-scope
  native_severity: P2
  normalization_reason: Exact source-specific completeness issue, normalized major;
    this custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
- finding_id: f6
  issue_key: culturemech-006536-event-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamp defects and a replacing repair writer limit provenance
  description: Preserve existing historical strings, including2026-01-27T01:15:03.fZ
    and naive February resolver timestamps. Current importer uses a %f format with
    time.strftime; current resolver uses naive datetime.now().isoformat(). The topology
    repair also fixes TIMESTAMP and replaces matching curator/action events. Future
    writers should emit actual timezone-aware timestamps and append new clarification
    events without altering prior entries; do not invent original times or claim historical
    code execution from present bodies.
  target_ids:
  - CultureMech:006536
  field_paths:
  - curation_history
  evidence_ids:
  - history
  - writer-komodo
  - writer-resolver
  - writer-repair813
  rule_id: custom/event-metadata
  native_severity: P3
  normalization_reason: Exact source-specific provenance issue, normalized minor;
    this custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current source metadata and timestamp importer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_komodo_813_desulfonatronum_score10.py
    role: current topology repair and history-event writer
- finding_id: f7
  issue_key: culturemech-006536-claim-evidence
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: No attached evidence distinguishes supported and unresolved layers
  description: Attach literal ingredient evidence for supported DSM amounts/forms
    and root evidence with exact field/stage scope for stock doses,water,pH and preparation.
    Keep KOMODO quantity support unresolved until exact branch sources are recovered.
    Historical API byte matches and parent proposals are separate evidence, not attached
    recipe claims or proof of original execution.
  target_ids:
  - CultureMech:006536
  field_paths:
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - old-claims
  - historical-source-joins
  - selected-parent-authentication
  - dsmz813
  - api813
  rule_id: custom/claim-evidence
  native_severity: P3
  normalization_reason: Exact source-specific completeness issue, normalized minor;
    this custom rule does not redefine a narrower native rubric rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
actions:
- action_id: a1
  description: The generated child relationship still says SOURCE_DUPLICATE for DSM14708,
    while current maintained relationships correctly preserve a STRAIN_SPECIFIC_VARIANT
    under the DSM owner. Current DSM14708 catalogue identifies environmental Desulfonatronum
    thiodismutans and points to813a, whereas the historical KOMODO813.1 link points
    to813. Both exact KOMODO routes fail403. Keep the branch unresolved and preserve
    its historical linkage; do not transfer813a or the primary DSM26308 exception.
    Regenerate only after source identity is reconciled, using the current conservative
    merger which distinguishes notes,pH,preparation and relationship fields.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_komodo_813_desulfonatronum_score10.py
    role: current topology repair and history-event writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: For the DSM owner, preserve eleven provider main rates on declared
    API1002ml basis and restore nineteen SL-10/vitamin stock entries plus their separate1ml
    batch doses. The primary itself does not state a main final volume. Target and
    KOMODO copies retain unresolved branch support rather than receiving automatic
    DSM evidence. Existing numerical agreement is not stage or formulation equivalence.
    Current API composition and solution parsing improve stock separation, but bare-ml
    normalization still requires explicit source basis.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Retain the exact10ml HCl(25%) input and1000ml SL-10 final make-up.
    The provider2.5g/L assertion does not establish percent basis or density, and
    must not be treated as primary-certified mass or a final-medium rate. Resolve
    stock representation separately from KOMODO branch identity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: The current supplied name sodium resazurin is paired with neutral CHEBI:8806;
    resolve the exact sodium-salt ID/label without guessing. CHEBI:34887 is anhydrous
    nickel dichloride, whereas the source specifies NiCl2 x 6 H2O. Current CHEBI:53542
    explicitly describes the hexahydrate. MIM preferred row6668 (Nickel (II) chloride
    hexahydrate) is MAPPED; row6703 (NiCl2 x 6 H2O) is REJECTED and synonym row6704
    is MAPPED. These spelling-specific statuses do not reject the whole identifier.
    Correct both actual nickel slots while retaining source-stage quantity limits.
    These name-versus-identifier defects are assessable even where branch quantities
    remain unresolved.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: Preserve the DSM owner main preparation and pH8.8–9.0. Bind its existing
    SL-10 DISSOLVE/make-up step only to the trace stock. The generated target omits
    both despite listing the DSM owner; address this through source-resolved regeneration,
    not by blindly assigning DSM conditions to unresolved KOMODO branches. Current
    preparation parser still concatenates solution-stage steps, while current resolver
    does not copy ph_range or preparation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/mediadive_importer.py
    role: current composition, stock-reference, unit and preparation writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a6
  description: Preserve existing historical strings, including2026-01-27T01:15:03.fZ
    and naive February resolver timestamps. Current importer uses a %f format with
    time.strftime; current resolver uses naive datetime.now().isoformat(). The topology
    repair also fixes TIMESTAMP and replaces matching curator/action events. Future
    writers should emit actual timezone-aware timestamps and append new clarification
    events without altering prior entries; do not invent original times or claim historical
    code execution from present bodies.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current source metadata and timestamp importer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current DSM composition resolver and timestamp writer
  - repository: CultureBotAI/CultureMech
    path: scripts/repair_komodo_813_desulfonatronum_score10.py
    role: current topology repair and history-event writer
  acceptance_checks:
  - Original history entries remain byte-preserved; any clarification is append-only
    and supported by an exact verified source.
  - Future importer/resolver timestamps parse as actual timezone-aware instants; repeated
    topology operations do not replace prior events or reuse a fixed event date.
  - Recheck generated provenance and all affected native diagnostic scopes after maintained-source
    curation.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a7
  description: Attach literal ingredient evidence for supported DSM amounts/forms
    and root evidence with exact field/stage scope for stock doses,water,pH and preparation.
    Keep KOMODO quantity support unresolved until exact branch sources are recovered.
    Historical API byte matches and parent proposals are separate evidence, not attached
    recipe claims or proof of original execution.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:006536
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_813_DESULFONATRONUM_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfonatronum_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_14708.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Exact KOMODO MediaInfo813/813.1 and MediaList GETs returned403. Their historical
  mapping snippets remain context; quantity support is not inherited from the DSM
  base.
- Current DSM14708 catalogue is identity/risk/source-link evidence only. Its813a formulation
  and cultivation conditions are not imported; publisher captures of813a are not recipe
  evidence for this record.
- The generic primary DSM26308 lactate/pH9.5 exception is excluded; it does not resolve
  the separate DSM14708 wrapper.
- Main API1002ml normalization is declared provider basis, while the primary1000ml
  water is input. SL-10 alone explicitly makes up to1000ml; HCl25% basis is unresolved.
- No strain-growth claim, optimization or experimental recommendation is inferred
  from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent
  rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed
  only on their declared normalization basis; unspecified percent bases and hydrate
  numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was
  performed by this author.
```
