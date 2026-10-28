# Scientific review: DESULFOSARCINA CETONICA MEDIUM

- Review: 20261028T211914Z-culturemech-001741-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T20:57:30.468636Z
- Finished UTC: 2026-10-28T21:19:14.335007Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM 612 is a staged A–D formulation with nested SL-10, but all 19 source-stage rates are flattened in target and owners. Retained DSM preparation and final pH are credited; stock-step scope, two supplied-form mappings and unresolved KOMODO identity require curation. No current quantity is silently endorsed or converted.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch078 index 07
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001741 | data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml | generated | desulfosarcina_cetonica_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001741 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001741 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001741 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001741 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Exact source and owner boundaries

identity: concern. Targets: CultureMech:001741.

The selected target and both declared owners are fully read. DSM 612 primary/API agree; KOMODO 612 is only a historically documented mapping with current 403 access failures. The similarly named JCM 395 historical sibling report is context only, not an additional owner or formulation donor.

### Category and formulation classification

consistency: supported. Targets: CultureMech:001741.

The source is liquid and chemically specified; defined classifications agree with provider complex_medium:no. No strain growth association is inferred.

### Original native diagnostics

schema: supported. Targets: CultureMech:001741.

All four original diagnostics exited 0; reference checks counted 0 and therefore do not authenticate the absent source claims.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001741.

57 current concentration fields are covered by 32 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b078-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","quantity_field_count":57,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.727651","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.727651","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.727651","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 20-20","quote":"KH2PO4                                                   0.70        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.727651,\n                        \"mmol_l\": 5.34703,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q2","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.31185","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.31185","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.31185","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 21-21","quote":"NH4Cl                                                    0.30        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.31185,\n                        \"mmol_l\": 5.83007,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q3","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2.9106","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2.9106","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2.9106","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 22-22","quote":"Na2SO4                                                   2.80        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 2.8,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.9106,\n                        \"mmol_l\": 20.4914,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q4","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.76715","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.76715","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.76715","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 23-23","quote":"MgCl2 x 6 H2O                                            1.70        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 1.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.76715,\n                        \"mmol_l\": 8.69221,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q5","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0519751","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0519751","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0519751","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 24-24","quote":"CaCl2 x 2 H2O                                            0.05        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.05,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0519751,\n                        \"mmol_l\": 0.353536,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"10.395","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"10.395","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"10.395","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 25-25","quote":"NaCl                                                    10.00        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10.395,\n                        \"mmol_l\": 177.875,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q7","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000519751","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000519751","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000519751","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution A content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The stated0.1% w/v resazurin stock supports0.0005 g in this addition, while provider0.000519751g/L uses its962ml Solution A basis.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 27-27","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000519751,\n                        \"mmol_l\": 0.00206932,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"50","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"50","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"50","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution B content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution B","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 33-33","quote":"Na2CO3                                                   1.00        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q9","label":"Na-butyrate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"120","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"120","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"120","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution C content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution C","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 39-39","quote":"Na-butyrate                                              1.20        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na-butyrate\",\n                        \"compound_id\": 232,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 120,\n                        \"mmol_l\": 1090.05,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q10","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"30","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"30","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"30","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Solution D content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation.","source_stage":"Solution D","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 45-45","quote":"Na2S x 9 H2O                                             0.30        g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\": 124.905,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q11","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact SL-10 source gives 10 ml HCl labelled25%, with final stock makeup1000 ml. Provider g_l2.5 is recorded, but the primary supplies no percentage basis or density permitting that mass conversion. Preserve the native volume/label, resolve the unsupported mass basis, and correct the root placement; the unresolved KOMODO branch is not certified.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 59-59","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q12","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 60-60","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q13","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 61-61","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q14","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 62-62","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q15","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 63-63","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q16","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 64-64","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q17","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 65-65","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q18","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 66-66","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q19","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The exact primary and provider identify this as Trace element solution SL-10 content. The explicit provider g_l supports that source-stage rate, but every local occurrence is flattened into main ingredients. Restore the named solution and receiving dose; do not reuse its denominator as a final-medium rate. The copied KOMODO branch remains unsupported pending exact source reconciliation. The primary explicitly makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 67-67","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q20","label":"Source receiving dose Solution A","local_fields":[],"decision":"correct","rationale":"Retain the explicitly printed solution addition as a batch volume. The provider lists total1002ml; the primary lists component additions without an explicit measured final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 3-3","quote":"Solution A                                             962.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 1314,\n                        \"amount\": 962,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q21","label":"Source receiving dose Solution B","local_fields":[],"decision":"correct","rationale":"Retain the explicitly printed solution addition as a batch volume. The provider lists total1002ml; the primary lists component additions without an explicit measured final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 4-4","quote":"Solution B                                              20.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 1317,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q22","label":"Source receiving dose Solution C","local_fields":[],"decision":"correct","rationale":"Retain the explicitly printed solution addition as a batch volume. The provider lists total1002ml; the primary lists component additions without an explicit measured final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 5-5","quote":"Solution C                                              10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 1316,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q23","label":"Source receiving dose Solution D","local_fields":[],"decision":"correct","rationale":"Retain the explicitly printed solution addition as a batch volume. The provider lists total1002ml; the primary lists component additions without an explicit measured final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 6-6","quote":"Solution D                                              10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\": 1318,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q24","label":"SL-10 receiving dose","local_fields":[],"decision":"correct","rationale":"Restore the1ml SL-10 addition inside Solution A, separately from its own1000ml stock preparation.","source_stage":"Solution A receives SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 26-26","quote":"Trace element solution SL-10                             1.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q25","label":"Source water input Solution A","local_fields":[],"decision":"evidence_only","rationale":"Preserve the native water volume at its exact preparation stage. Only SL-10 has a separate explicit final makeup statement; listed water volumes are not all measured final volumes.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 28-28","quote":"Distilled water                                        960.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 960,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q26","label":"Source water input Solution B","local_fields":[],"decision":"evidence_only","rationale":"Preserve the native water volume at its exact preparation stage. Only SL-10 has a separate explicit final makeup statement; listed water volumes are not all measured final volumes.","source_stage":"Solution B","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 34-34","quote":"Distilled water                                         20.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q27","label":"Source water input Solution C","local_fields":[],"decision":"evidence_only","rationale":"Preserve the native water volume at its exact preparation stage. Only SL-10 has a separate explicit final makeup statement; listed water volumes are not all measured final volumes.","source_stage":"Solution C","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 40-40","quote":"Distilled water                                         10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q28","label":"Source water input Solution D","local_fields":[],"decision":"evidence_only","rationale":"Preserve the native water volume at its exact preparation stage. Only SL-10 has a separate explicit final makeup statement; listed water volumes are not all measured final volumes.","source_stage":"Solution D","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 46-46","quote":"Distilled water                                         10.00       ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q29","label":"Source water input Trace element solution SL-10","local_fields":[],"decision":"evidence_only","rationale":"Preserve the native water volume at its exact preparation stage. Only SL-10 has a separate explicit final makeup statement; listed water volumes are not all measured final volumes.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 68-68","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}]},{"quantity_id":"q30","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and D are autoclaved under 100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions B to D are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 – 7.4."}},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and D are autoclaved under 100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions B to D are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 – 7.4."}}],"decision":"evidence_only","rationale":"The complete retained description matches the current provider, including atmospheres, initial pH below6, at least30min and ordered separate sterilizations. Credit its text while restoring the named solution topology. KOMODO has no corresponding method; that absence is represented separately.","source_stage":"Main assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 8-14","quote":"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at\nleast 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type\ntubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2\nand 20% CO2 gas atmosphere. Solutions C and D are autoclaved under 100% N2 gas\natmosphere. To complete the medium appropriate amounts of solutions B to D are added\nto the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2\n– 7.4.","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least 30 min), then distributed under the same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solutions C and D are autoclaved under 100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions B to D are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2 \\u2013 7.4.\"\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q31","label":"Retained final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.2,"max":7.4},"decision":"evidence_only"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.2,"max":7.4},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ph_range","stored":{"min":7.2,"max":7.4},"decision":"evidence_only"}],"decision":"mixed","rationale":"The primary supports final pH7.2–7.4 in target/DSM. The identically copied KOMODO range remains unverified for that branch.","source_stage":"Complete medium","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 13-14","quote":"to the sterile solution A in the sequence as indicated. Final pH of the medium should be 7.2\n– 7.4.","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.medium","quote":"{\n            \"id\": 612,\n            \"name\": \"DESULFOSARCINA CETONICA MEDIUM\",\n            \"complex_medium\": \"no\",\n            \"min_pH\": 7.2,\n            \"max_pH\": 7.4,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf\"\n        }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q32","label":"SL-10 makeup text at main level","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."},"decision":"correct"}],"decision":"correct","rationale":"The dissolution text and1000ml makeup are source-supported for SL-10. Its unqualified placement beside main preparation lacks that stock boundary; relocate the unchanged description under SL-10.","source_stage":"SL-10 preparation","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:001741.

All exact asserted slots and packaged mapping rows are assessed. The other stated salts/hydrates agree with current ontology formulas. Nickel has an anhydrous-versus-hexahydrate error; neutral resazurin conflicts with sodium wording. Local preferred nickel spelling NiCl2 x 6 H2O has REJECTED preferred rows, while Nickel (II) chloride hexahydrate has a MAPPED counterpart; cobalt likewise has spelling-specific statuses despite a correct hydrate ID. These mapping statuses and canonical labels are separate from supplied-form correctness.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:001741.

All six complete reports, including the separately scoped JCM 395 sibling, and both exact selected parent rows were read. Current API 612 raw digest equals the historical digest; literal/decoded source objects match independently, whereas null concentration snippets remain unsupported. Current owner bytes equal the recorded unchanged before/after hashes. Current importer preserves primary stock descriptors but maps bare ml to ML_PER_L and flattens preparation steps; current conservative merge does not justify historical signature equivalence. Stored .fZ and missing-offset events remain immutable provenance limitations.

### High-metal classification

consistency: unknown. Targets: CultureMech:001741.

The selected target and both maintained owners retain high_metal: true. Flattened trace-stock concentrations do not establish high final-medium metal exposure, and the reviewed sources do not independently justify this classification. Preserve the flag as unresolved pending explicit classification evidence; no new exposure or growth inference is made.

## Findings

### f1: Restore Solution A–D and nested SL-10 boundaries

major / open / confirmed; issue key: culturemech-001741-stock-stage-flattening.

All 19 ingredient rates are source-stage values flattened into the final-medium list. Reconstruct Solution A–D and the SL-10 substock using the printed receiving volumes. Preserve positive provider stage-rate support and SL-10 explicit 1000 ml makeup; do not infer measured final volume from water or sum rates with different preparation denominators. For HCl 25%, retain the native volume until percentage basis is established. The copied KOMODO formulation needs its own source reconciliation.

### f2: Scope retained stock preparation and resolve the aerobic branch note

major / open / confirmed; issue key: culturemech-001741-stock-preparation-scope.

Target and DSM owner retain the correct complete main preparation, but the SL-10 dissolution/makeup instruction is an unqualified main step. Reattach that unchanged stock text. The KOMODO owner has no main method and asserts Aerobic:Yes, conflicting with the named DSM preparation; resolve that exact branch before inheriting the DSM recipe.

### f3: Correct nickel supplied-form mapping

major / open / confirmed; issue key: culturemech-001741-nickel-hydrate.

All three documents name nickel chloride hexahydrate but assert anhydrous CHEBI:34887 in primary and secondary slots. Fresh CHEBI:53542 explicitly has six waters. Reconcile the asserted form and retain the source stock mass; current MIM spelling status does not override molecular identity.

### f4: Resolve the sodium-resazurin form

major / open / confirmed; issue key: culturemech-001741-resazurin-sodium-form.

All three preferred terms and the source specify sodium resazurin, whereas CHEBI:8806 represents neutral resazurin C12H7NO4. The packaged MIM synonym also conflates sodium wording with that neutral concept. Resolve the supplied sodium-salt identity without changing the printed amount or certifying a guessed replacement.

### f5: Retain unresolved exact KOMODO identity and duplicate relationship

major / open / confirmed; issue key: culturemech-001741-historical-branch-identity.

The historical catalogue row connects KOMODO 612 to DSM 612, but current exact recipe and both catalogue routes return 403. The current parent/variant duplicate relationship is based on copied composition and signature, which does not independently establish source equivalence. Keep the branch, duplicated-source relationship and aerobic contradiction explicitly unresolved while curating the supported DSM formulation.

### f6: Append source claims and preserve prior event history

minor / open / confirmed; issue key: culturemech-001741-history-and-quantity-evidence.

No scoped ingredient claim is attached despite retained amounts. Attach exact current evidence at each source stage. Preserve earlier events and append a new correction; the stored KOMODO timestamp ends .fZ and a later event lacks a UTC offset. Correct future writer timestamp generation using a UTC-capable formatter, distinguishing its current %f directive from stored historical text.

## Recommended Actions And Acceptance Checks

### a1

All 19 ingredient rates are source-stage values flattened into the final-medium list. Reconstruct Solution A–D and the SL-10 substock using the printed receiving volumes. Preserve positive provider stage-rate support and SL-10 explicit 1000 ml makeup; do not infer measured final volume from water or sum rates with different preparation denominators. For HCl 25%, retain the native volume until percentage basis is established. The copied KOMODO formulation needs its own source reconciliation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

Target and DSM owner retain the correct complete main preparation, but the SL-10 dissolution/makeup instruction is an unqualified main step. Reattach that unchanged stock text. The KOMODO owner has no main method and asserts Aerobic:Yes, conflicting with the named DSM preparation; resolve that exact branch before inheriting the DSM recipe.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

All three documents name nickel chloride hexahydrate but assert anhydrous CHEBI:34887 in primary and secondary slots. Fresh CHEBI:53542 explicitly has six waters. Reconcile the asserted form and retain the source stock mass; current MIM spelling status does not override molecular identity.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

All three preferred terms and the source specify sodium resazurin, whereas CHEBI:8806 represents neutral resazurin C12H7NO4. The packaged MIM synonym also conflates sodium wording with that neutral concept. Resolve the supplied sodium-salt identity without changing the printed amount or certifying a guessed replacement.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The historical catalogue row connects KOMODO 612 to DSM 612, but current exact recipe and both catalogue routes return 403. The current parent/variant duplicate relationship is based on copied composition and signature, which does not independently establish source equivalence. Keep the branch, duplicated-source relationship and aerobic contradiction explicitly unresolved while curating the supported DSM formulation.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a6

No scoped ingredient claim is attached despite retained amounts. Attach exact current evidence at each source stage. Preserve earlier events and append a new correction; the stored KOMODO timestamp ends .fZ and a later event lacks a UTC offset. Correct future writer timestamp generation using a UTC-capable formatter, distinguishing its current %f directive from stored historical text.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.
- Verify the current KOMODO importer emits literal UTC Z with actual microseconds without time.strftime %f; existing historical event bytes remain unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsm612 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf; REVIEW_WORK/batch078/source07-08-10/dsm612.json; exact original raw/text/hash/time metadata | context_only | Exact selected primary; whole recipe and embedded stock sections retain their own stages. |
| api612 | https://mediadive.dsmz.de/rest/medium/612; REVIEW_WORK/batch078/source07-08-10/api612.json; exact original raw/text/hash/time metadata | context_only | Exact current selected provider recipe, retaining explicit stage-specific rates. |
| komodo612 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=612; REVIEW_WORK/batch078/source07-08-10/komodo612.json; exact original raw/text/hash/time metadata | context_only | Exact declared historical KOMODO612 identity route; failure leaves branch unverified. |
| komodoList | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch078/source07-08-10/komodoList.json; exact original raw/text/hash/time metadata | context_only | Exact historical catalogue identity context only. |
| komodoHistoricalList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch078/source07-08-10-extra/komodoHistoricalList.json; exact original raw/text/hash/time metadata | context_only | Exact historical catalogue URL printed in the complete selected KOMODO612 review, distinct from the /komodo/servlet lead. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; REVIEW_WORK/batch078/source07-08-10/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| target | data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-18 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json; Entire inspected-candidate context: 69 unrelated objects; no selected medium612 row | context_only | Historical parent context only: the 69 inspected candidate objects contain no selected medium612 row. This artifact provides no selected formulation or claim authentication; selected claims are joined separately to their exact plan rows. |
| report-19 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-21 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-22 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfosarcina_cetonica_medium.yaml.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_cetonicum_medium__33e412bb.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| report-26 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.md; Complete report | context_only | Historical report; exact headers are retained in the reading sidecar and neighboring-record mentions remain comparison-only. Old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch078/record07/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch078/record07/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch078/record07/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions, _normalize_unit, _classify_preparation_action | context_only | Current parser excludes percent-stock additions from primary ingredients, preserves referenced stock amounts/attributes separately and prioritizes explicit provider g_l. It skips source water; bare units alone do not establish a final-volume basis. Current code is not historical execution proof. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| historical-object-joins | REVIEW_WORK/batch078/record07/historical-current-object-joins.json; Complete exact decoded-object comparisons | context_only | Historical object correspondence is distinct from raw-response authentication. |
| historical-parent-authentication | REVIEW_WORK/batch078/record07/historical-parent-authentication.json; Both exact selected parent rows; literal and raw-digest matches separate | context_only | Historical raw-source digests and literal objects are independently joined to fresh API612; null snippets remain null. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current converter writes aerobic metadata and uses time.strftime with unsupported %f directive; the stored malformed event ends .fZ. This current code reading is not proof of the historical execution environment. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; REVIEW_WORK/batch078/source07-08-10/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; REVIEW_WORK/batch078/source07-08-10/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; REVIEW_WORK/batch078/source07-08-10/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; REVIEW_WORK/batch078/source07-08-10/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; REVIEW_WORK/batch078/source07-08-10/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; REVIEW_WORK/batch078/source07-08-10/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; REVIEW_WORK/batch078/source07-08-10/chebi8806.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; REVIEW_WORK/batch078/source07-08-10/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi64103 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103; REVIEW_WORK/batch078/source07-08-10/chebi64103.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; REVIEW_WORK/batch078/source07-08-10/chebi76209.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; REVIEW_WORK/batch078/source07-08-10/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; REVIEW_WORK/batch078/source07-08-10/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; REVIEW_WORK/batch078/source07-08-10/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; REVIEW_WORK/batch078/source07-08-10/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; REVIEW_WORK/batch078/source07-08-10/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; REVIEW_WORK/batch078/source07-08-10/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; REVIEW_WORK/batch078/source07-08-10/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; REVIEW_WORK/batch078/source07-08-10/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; REVIEW_WORK/batch078/source07-08-10/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Exact current ontology object; chemical identity/form, not recipe concentration evidence. |
| quantities | REVIEW_WORK/batch078/record07/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch078/record07/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch078/record07/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch078/record07/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch078/record07/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch078/record07/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch078/record07/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims in this scoped sidecar; historical object joins are separate evidence. |
| check-schema | REVIEW_WORK/batch078/record07/schema-result.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch078/record07/strict-result.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch078/record07/terms-result.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch078/record07/references-result.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Partial completion reflects inaccessible exact KOMODO recipe/catalogue sources. Historical copied DSM content does not certify the KOMODO formulation or duplicate relationship.
- Primary receiving volumes sum 1002 ml, matching provider total metadata, but this is not an independent measured-final-volume statement. Solution A listed inputs sum 961.5 ml while its declared receiving amount/provider basis is 962 ml. Preserve the explicit declarations and source discrepancy.
- No ingredient source claims are attached; new support is evidence_only, not retroactive verified evidence. The 25% HCl basis/density remains unresolved.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T211914Z-culturemech-001741-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOSARCINA CETONICA MEDIUM'
started_at: '2026-10-28T20:57:30.468636Z'
finished_at: '2026-10-28T21:19:14.335007Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Read-only independent review of maintained source records, fresh
    sources and original diagnostics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: DSM 612 is a staged A–D formulation with nested SL-10, but all 19 source-stage
  rates are flattened in target and owners. Retained DSM preparation and final pH
  are credited; stock-step scope, two supplied-form mappings and unresolved KOMODO
  identity require curation. No current quantity is silently endorsed or converted.
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
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
    sha256: eb1559f4bd7b14acf72022f856938fc3321acc4be19262f93df4b0be7c3dff01
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    sha256: e3e3eac91e8e6d3d8b4f097fe1124fd88bcefb69e98ef7071e997aa850163678
    role: context
  - path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    sha256: 4e3402dd3c0ed5a2b23e5d4b212dcb71174534a566c2dd09a1dd22b799a0a52c
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
    sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
    sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml.md
    sha256: ca88a267cd5aac747ec4c4977c2abab13957328f445fe138f640a16658366ca2
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
    sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfosarcina_cetonica_medium.yaml.md
    sha256: e240c05e91e615cf4e903d161c4dbfbb33ebc03252db7bfa4b06d3da04c8f156
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.md
    sha256: 7a8603cf9b6a8d67a19523e4556d7dced2fd60be17678b5f4b2644a589a67be8
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_cetonicum_medium__33e412bb.md
    sha256: a31fdbd78e2ccab69f98906dfd20aba678d0305736fcc8951781c6703521faff
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.md
    sha256: 86f290590e367a41b3ab4b477d0466902dd65e4c194c1b9fe85f85a958135150
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.md
    sha256: 678e04d198df1ea30a3a39a6edcc626fd8eb1839e1a22379dfa4f1a8f7226fb4
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
    role: context
  - path: scripts/fetch_komodo_base_volumes.py
    sha256: 9dad49c380422b2e7d3f40b4ff713d59360d22f6eec9b55068e050099cb9cffa
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
    role: context
  - path: scripts/record_io.py
    sha256: bff4715f85d7ff2ff681b88f0a2de2667e5767d7a2c196bd50a37d5d329957ac
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_jcm_stock_preparations.py
    sha256: 7fbea52819431dcb749d3b44bce35bcddc86d708873fc6eef4e730e5066eb98a
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
  selection: Authoritative batch078 index 07
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001741
targets:
- target_id: CultureMech:001741
  path: data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
  label: desulfosarcina_cetonica_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001741
  command: just validate-schema data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
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
  - CultureMech:001741
  command: just validate-strict data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
    --out REVIEW_WORK/batch078/record07/strict.tsv --workers 1 --quiet
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
  - CultureMech:001741
  command: just validate-terms data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
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
  - CultureMech:001741
  command: just validate-references data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsm612
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf
  accessed_at: '2026-10-28T20:57:52.031883Z'
  locator: REVIEW_WORK/batch078/source07-08-10/dsm612.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact selected primary; whole recipe and embedded stock sections retain
    their own stages.
  snapshot_sha256: 99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27
- evidence_id: api612
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/612
  accessed_at: '2026-10-28T20:57:51.389709Z'
  locator: REVIEW_WORK/batch078/source07-08-10/api612.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current selected provider recipe, retaining explicit stage-specific
    rates.
  snapshot_sha256: e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e
- evidence_id: komodo612
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=612
  accessed_at: '2026-10-28T20:57:52.130567Z'
  locator: REVIEW_WORK/batch078/source07-08-10/komodo612.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact declared historical KOMODO612 identity route; failure leaves branch
    unverified.
  snapshot_sha256: 30df5a6e5481da1a6f158cf7e95cd3f41e8dbd7e91d469bb92cab6a615ca2953
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=612;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T20:57:52.163552Z'
  locator: REVIEW_WORK/batch078/source07-08-10/komodoList.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact historical catalogue identity context only.
  snapshot_sha256: 111e63243322df58760dc87ae22027745eff1475f077c54097592a425718114c
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoHistoricalList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T20:59:55.193220Z'
  locator: REVIEW_WORK/batch078/source07-08-10-extra/komodoHistoricalList.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Exact historical catalogue URL printed in the complete selected KOMODO612
    review, distinct from the /komodo/servlet lead.
  snapshot_sha256: 57f276d6f3810fe9ddf62d3a0bd30160b081d1288a4ee73db1f503a47335c7dd
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  accessed_at: '2026-10-28T20:57:55.582950Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi53542.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:01:06.047082Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: eb1559f4bd7b14acf72022f856938fc3321acc4be19262f93df4b0be7c3dff01
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:01:06.047259Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: e3e3eac91e8e6d3d8b4f097fe1124fd88bcefb69e98ef7071e997aa850163678
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T21:01:06.047294Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T21:01:06.047602Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T21:01:06.047631Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T21:01:06.047660Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T21:01:06.047687Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: 4e3402dd3c0ed5a2b23e5d4b212dcb71174534a566c2dd09a1dd22b799a0a52c
- evidence_id: report-18
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/inspected-candidate-context.json
  locator: 'Entire inspected-candidate context: 69 unrelated objects; no selected
    medium612 row'
  accessed_at: '2026-10-28T21:01:06.047712Z'
  support: context_only
  summary: 'Historical parent context only: the 69 inspected candidate objects contain
    no selected medium612 row. This artifact provides no selected formulation or claim
    authentication; selected claims are joined separately to their exact plan rows.'
  snapshot_sha256: 65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934
- evidence_id: report-19
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:01:06.048483Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T21:01:06.054379Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: ca88a267cd5aac747ec4c4977c2abab13957328f445fe138f640a16658366ca2
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:01:06.054452Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: bc8c96d09770525e6b6ba6dc0c7680354cf9bc6baa5249e79e82b65328203147
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/desulfosarcina_cetonica_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T21:01:06.061105Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: e240c05e91e615cf4e903d161c4dbfbb33ebc03252db7bfa4b06d3da04c8f156
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T21:01:06.061170Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 7a8603cf9b6a8d67a19523e4556d7dced2fd60be17678b5f4b2644a589a67be8
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/desulfobacterium_cetonicum_medium__33e412bb.md
  locator: Complete report
  accessed_at: '2026-10-28T21:01:06.061205Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: a31fdbd78e2ccab69f98906dfd20aba678d0305736fcc8951781c6703521faff
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T21:01:06.061230Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 86f290590e367a41b3ab4b477d0466902dd65e4c194c1b9fe85f85a958135150
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T21:01:06.061254Z'
  support: context_only
  summary: Historical report; exact headers are retained in the reading sidecar and
    neighboring-record mentions remain comparison-only. Old source/check claims are
    not newly executed.
  snapshot_sha256: 678e04d198df1ea30a3a39a6edcc626fd8eb1839e1a22379dfa4f1a8f7226fb4
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/historical-reading.json
  accessed_at: '2026-10-28T21:01:06.066168Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: e6e43f5db3513ccf2ae3380e459c137cdb045e593eea92db0508220bbc0e2d16
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T21:01:06.066219Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: ded4a48ae132b101ffc9565a899fbbfaabe195cadb80400d18600f0b63b9fecc
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/complete-document-reader.json
  accessed_at: '2026-10-28T21:01:06.066277Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: 3d719851a6ec9c5b7adb9a550c46c1116b0ac8667ea9b2c6ae2295968d5f78a3
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _is_api_stock_addition, _api_stock_name, _parse_api_solutions,
    _normalize_unit, _classify_preparation_action
  accessed_at: '2026-10-28T21:01:06.066313Z'
  support: context_only
  summary: Current parser excludes percent-stock additions from primary ingredients,
    preserves referenced stock amounts/attributes separately and prioritizes explicit
    provider g_l. It skips source water; bare units alone do not establish a final-volume
    basis. Current code is not historical execution proof.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T21:01:06.066349Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: historical-object-joins
  kind: prior_review
  reference: REVIEW_WORK/batch078/record07/historical-current-object-joins.json
  accessed_at: '2026-10-28T21:01:06.066379Z'
  locator: Complete exact decoded-object comparisons
  support: context_only
  summary: Historical object correspondence is distinct from raw-response authentication.
  snapshot_sha256: c934e6f7405a732d1981089bdeb5aa9999b3999323e210cd0046b15b66f58416
- evidence_id: historical-parent-authentication
  kind: prior_review
  reference: REVIEW_WORK/batch078/record07/historical-parent-authentication.json
  accessed_at: '2026-10-28T21:01:06.066432Z'
  locator: Both exact selected parent rows; literal and raw-digest matches separate
  support: context_only
  summary: Historical raw-source digests and literal objects are independently joined
    to fresh API612; null snippets remain null.
  snapshot_sha256: 2429a837948ff1d2c32c9644d26c5a6ee07aebc33fd22731efe1dc4be51ea6ee
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T21:01:06.066493Z'
  support: context_only
  summary: Current converter writes aerobic metadata and uses time.strftime with unsupported
    %f directive; the stored malformed event ends .fZ. This current code reading is
    not proof of the historical execution environment.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  accessed_at: '2026-10-28T20:57:55.820751Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi63036.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  accessed_at: '2026-10-28T20:57:53.788390Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi31206.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  accessed_at: '2026-10-28T20:57:54.037990Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi32149.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  accessed_at: '2026-10-28T20:57:57.069072Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86345.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  accessed_at: '2026-10-28T20:57:56.790414Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86158.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  accessed_at: '2026-10-28T20:57:53.394246Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi26710.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  accessed_at: '2026-10-28T20:57:57.653392Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi8806.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  accessed_at: '2026-10-28T20:57:53.407299Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi29377.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 21ae6468f9d087fd7930a263fc44728e31a8babde3576135686278a13bc1d6e1
- evidence_id: chebi64103
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103
  accessed_at: '2026-10-28T20:57:55.848270Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi64103.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 0499238461b934590c83719736c7a30bf942d95c204daee7da061e0ba99f4a74
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  accessed_at: '2026-10-28T20:57:56.416990Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi76209.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  accessed_at: '2026-10-28T20:57:53.185663Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi17883.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  accessed_at: '2026-10-28T20:57:57.016466Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86249.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  accessed_at: '2026-10-28T20:57:55.211394Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi49976.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  accessed_at: '2026-10-28T20:57:57.543008Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86368.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  accessed_at: '2026-10-28T20:57:54.626226Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi33118.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  accessed_at: '2026-10-28T20:57:55.246687Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi53503.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  accessed_at: '2026-10-28T20:57:57.074069Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi86318.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  accessed_at: '2026-10-28T20:57:54.649502Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi34887.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  accessed_at: '2026-10-28T20:57:56.189397Z'
  locator: REVIEW_WORK/batch078/source07-08-10/chebi75213.json; exact original raw/text/hash/time
    metadata
  support: context_only
  summary: Exact current ontology object; chemical identity/form, not recipe concentration
    evidence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.170676Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: 5655a079418f06aca85e70b30770468b01a3d8c27fe6479d4a9949bd50420bed
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.170751Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 7038c5fc9e0d7c453c3cd7849584191307a26ef15d0c14991d2c0b8752f1c26c
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.170856Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: a0fbd070c649c4ffc0f96171d4a009b1dde950fd89bc845c34abff107edc7ac9
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.170919Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 65d6adc008d955dc5609527a012be8f4c7617f4132b4ef89ac370597e35e64f0
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.170973Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 10ff4c25dea6b31123caf18867c5c6a213ea1f0ab8ba55bec9c57f8fefef9654
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.170999Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 2a95906236581d349dce2eec8adf9995fe2fc42b24af778fb6b5ded1334b509a
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch078/record07/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T21:01:06.171020Z'
  support: context_only
  summary: No attached claims in this scoped sidecar; historical object joins are
    separate evidence.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch078/record07/schema-result.json
  accessed_at: '2026-10-28T20:57:31.580631Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: c005e8492523328b4ac601d52fe703231fd8e3051e96c36a1809d71f17d2c292
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch078/record07/strict-result.json
  accessed_at: '2026-10-28T20:57:32.558527Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 026cee94dd88d60a34a9122f88579af85a2f71fdeb05ee39783df3d20f767c2a
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch078/record07/terms-result.json
  accessed_at: '2026-10-28T20:57:33.642331Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: a911cb2641e425d49a80f975b2894f6dd17da01cda5480f0e12222525759f8f0
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch078/record07/references-result.json
  accessed_at: '2026-10-28T20:57:34.386408Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: 8725207b75f8ab0c6f418d202029aa2e7d23426064acb7def1b8ce11d9de495e
assessments:
- assessment_id: identity
  area: identity
  topic: Exact source and owner boundaries
  outcome: concern
  summary: The selected target and both declared owners are fully read. DSM 612 primary/API
    agree; KOMODO 612 is only a historically documented mapping with current 403 access
    failures. The similarly named JCM 395 historical sibling report is context only,
    not an additional owner or formulation donor.
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - target
  - owner
  - owner-2
  - dsm612
  - api612
  - komodo612
  - historical-selected-parent-rows
- assessment_id: classification
  area: consistency
  topic: Category and formulation classification
  outcome: supported
  summary: The source is liquid and chemically specified; defined classifications
    agree with provider complex_medium:no. No strain growth association is inferred.
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - target
  - dsm612
  - api612
- assessment_id: schema
  area: schema
  topic: Original native diagnostics
  outcome: supported
  summary: All four original diagnostics exited 0; reference checks counted 0 and
    therefore do not authenticate the absent source claims.
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 57 current concentration fields are covered by 32 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b078-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","quantity_field_count":57,"decisions":[{"quantity_id":"q1","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.727651","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.727651","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"0.727651","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 20-20","quote":"KH2PO4                                                   0.70        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.727651,\n                        \"mmol_l\":
    5.34703,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q2","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.31185","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.31185","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"0.31185","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 21-21","quote":"NH4Cl                                                    0.30        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.31185,\n                        \"mmol_l\":
    5.83007,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q3","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2.9106","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2.9106","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"2.9106","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 22-22","quote":"Na2SO4                                                   2.80        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 2.8,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.9106,\n                        \"mmol_l\":
    20.4914,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q4","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.76715","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.76715","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"1.76715","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 23-23","quote":"MgCl2 x 6 H2O                                            1.70        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 1.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.76715,\n                        \"mmol_l\":
    8.69221,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q5","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0519751","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0519751","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"0.0519751","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 24-24","quote":"CaCl2 x 2 H2O                                            0.05        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.05,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.0519751,\n                        \"mmol_l\":
    0.353536,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q6","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"10.395","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"10.395","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"10.395","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 25-25","quote":"NaCl                                                    10.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10.395,\n                        \"mmol_l\":
    177.875,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q7","label":"Sodium resazurin","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000519751","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000519751","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.000519751","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution A content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation. The stated0.1% w/v resazurin stock supports0.0005
    g in this addition, while provider0.000519751g/L uses its962ml Solution A basis.","source_stage":"Solution
    A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 27-27","quote":"Sodium resazurin (0.1% w/v)                              0.50       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000519751,\n                        \"mmol_l\": 0.00206932,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"}]},{"quantity_id":"q8","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"50","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"50","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"50","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution B content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution B","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 33-33","quote":"Na2CO3                                                   1.00        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    471.752,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q9","label":"Na-butyrate","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"120","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"120","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"120","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution C content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution C","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 39-39","quote":"Na-butyrate                                              1.20        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na-butyrate\",\n                        \"compound_id\":
    232,\n                        \"amount\": 1.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 120,\n                        \"mmol_l\":
    1090.05,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q10","label":"Na2S x 9 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"30","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"30","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"30","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Solution D content. The explicit provider
    g_l supports that source-stage rate, but every local occurrence is flattened into
    main ingredients. Restore the named solution and receiving dose; do not reuse
    its denominator as a final-medium rate. The copied KOMODO branch remains unsupported
    pending exact source reconciliation.","source_stage":"Solution D","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 45-45","quote":"Na2S x 9 H2O                                             0.30        g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\":
    54,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 30,\n                        \"mmol_l\":
    124.905,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q11","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact SL-10 source gives 10 ml HCl labelled25%, with final stock makeup1000 ml.
    Provider g_l2.5 is recorded, but the primary supplies no percentage basis or density
    permitting that mass conversion. Preserve the native volume/label, resolve the
    unsupported mass basis, and correct the root placement; the unresolved KOMODO
    branch is not certified.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 59-59","quote":"HCl (25%)                                                  10.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q12","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 60-60","quote":"FeCl2 x 4 H2O                                               1.50       g","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q13","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 61-61","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q14","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 62-62","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q15","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 63-63","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q16","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 64-64","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q17","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 65-65","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q18","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 66-66","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q19","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"},"decision":"correct"}],"decision":"mixed","rationale":"The
    exact primary and provider identify this as Trace element solution SL-10 content.
    The explicit provider g_l supports that source-stage rate, but every local occurrence
    is flattened into main ingredients. Restore the named solution and receiving dose;
    do not reuse its denominator as a final-medium rate. The copied KOMODO branch
    remains unsupported pending exact source reconciliation. The primary explicitly
    makes SL-10 up to1000 ml, positively supporting its solid-component stock rates.","source_stage":"Trace
    element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 67-67","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q20","label":"Source receiving dose Solution A","local_fields":[],"decision":"correct","rationale":"Retain
    the explicitly printed solution addition as a batch volume. The provider lists
    total1002ml; the primary lists component additions without an explicit measured
    final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete
    medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 3-3","quote":"Solution A                                             962.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    1314,\n                        \"amount\": 962,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q21","label":"Source receiving dose Solution B","local_fields":[],"decision":"correct","rationale":"Retain
    the explicitly printed solution addition as a batch volume. The provider lists
    total1002ml; the primary lists component additions without an explicit measured
    final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete
    medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 4-4","quote":"Solution B                                              20.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    1317,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q22","label":"Source receiving dose Solution C","local_fields":[],"decision":"correct","rationale":"Retain
    the explicitly printed solution addition as a batch volume. The provider lists
    total1002ml; the primary lists component additions without an explicit measured
    final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete
    medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 5-5","quote":"Solution C                                              10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    1316,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q23","label":"Source receiving dose Solution D","local_fields":[],"decision":"correct","rationale":"Retain
    the explicitly printed solution addition as a batch volume. The provider lists
    total1002ml; the primary lists component additions without an explicit measured
    final-volume statement. No per-litre receiving dose or density is inferred.","source_stage":"Complete
    medium assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 6-6","quote":"Solution D                                              10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution D\",\n                        \"solution_id\":
    1318,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q24","label":"SL-10 receiving dose","local_fields":[],"decision":"correct","rationale":"Restore
    the1ml SL-10 addition inside Solution A, separately from its own1000ml stock preparation.","source_stage":"Solution
    A receives SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 26-26","quote":"Trace element solution SL-10                             1.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q25","label":"Source water input Solution A","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the native water volume at its exact preparation stage. Only SL-10 has a separate
    explicit final makeup statement; listed water volumes are not all measured final
    volumes.","source_stage":"Solution A","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 28-28","quote":"Distilled water                                        960.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 960,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q26","label":"Source water input Solution B","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the native water volume at its exact preparation stage. Only SL-10 has a separate
    explicit final makeup statement; listed water volumes are not all measured final
    volumes.","source_stage":"Solution B","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 34-34","quote":"Distilled water                                         20.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q27","label":"Source water input Solution C","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the native water volume at its exact preparation stage. Only SL-10 has a separate
    explicit final makeup statement; listed water volumes are not all measured final
    volumes.","source_stage":"Solution C","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 40-40","quote":"Distilled water                                         10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q28","label":"Source water input Solution D","local_fields":[],"decision":"evidence_only","rationale":"Preserve
    the native water volume at its exact preparation stage. Only SL-10 has a separate
    explicit final makeup statement; listed water volumes are not all measured final
    volumes.","source_stage":"Solution D","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 46-46","quote":"Distilled water                                         10.00       ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q29","label":"Source water input Trace element solution
    SL-10","local_fields":[],"decision":"evidence_only","rationale":"Preserve the
    native water volume at its exact preparation stage. Only SL-10 has a separate
    explicit final makeup statement; listed water volumes are not all measured final
    volumes.","source_stage":"Trace element solution SL-10","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 68-68","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}]},{"quantity_id":"q30","label":"Retained main preparation","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Solution
    A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least
    30 min), then distributed under the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas atmosphere. Solutions C and D are autoclaved under 100%
    N2 gas atmosphere. To complete the medium appropriate amounts of solutions B to
    D are added to the sterile solution A in the sequence as indicated. Final pH of
    the medium should be 7.2 – 7.4."}},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"Solution
    A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below 6 (at least
    30 min), then distributed under the same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclaved. Solution B is autoclaved separately under
    80% N2 and 20% CO2 gas atmosphere. Solutions C and D are autoclaved under 100%
    N2 gas atmosphere. To complete the medium appropriate amounts of solutions B to
    D are added to the sterile solution A in the sequence as indicated. Final pH of
    the medium should be 7.2 – 7.4."}}],"decision":"evidence_only","rationale":"The
    complete retained description matches the current provider, including atmospheres,
    initial pH below6, at least30min and ordered separate sterilizations. Credit its
    text while restoring the named solution topology. KOMODO has no corresponding
    method; that absence is represented separately.","source_stage":"Main assembly","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 8-14","quote":"Solution A is sparged with 80% N2 and 20% CO2 gas mixture
    to reach a pH below 6 (at\nleast 30 min), then distributed under the same gas
    atmosphere into anoxic Hungate-type\ntubes or serum vials and autoclaved. Solution
    B is autoclaved separately under 80% N2\nand 20% CO2 gas atmosphere. Solutions
    C and D are autoclaved under 100% N2 gas\natmosphere. To complete the medium appropriate
    amounts of solutions B to D are added\nto the sterile solution A in the sequence
    as indicated. Final pH of the medium should be 7.2\n– 7.4.","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"Solution A is sparged with 80% N2 and 20% CO2 gas mixture to reach a pH below
    6 (at least 30 min), then distributed under the same gas atmosphere into anoxic
    Hungate-type tubes or serum vials and autoclaved. Solution B is autoclaved separately
    under 80% N2 and 20% CO2 gas atmosphere. Solutions C and D are autoclaved under
    100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions
    B to D are added to the sterile solution A in the sequence as indicated. Final
    pH of the medium should be 7.2 \\u2013 7.4.\"\n                    }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q31","label":"Retained final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.2,"max":7.4},"decision":"evidence_only"},{"path":"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml","field_path":"ph_range","stored":{"min":7.2,"max":7.4},"decision":"unsupported"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"ph_range","stored":{"min":7.2,"max":7.4},"decision":"evidence_only"}],"decision":"mixed","rationale":"The
    primary supports final pH7.2–7.4 in target/DSM. The identically copied KOMODO
    range remains unverified for that branch.","source_stage":"Complete medium","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 13-14","quote":"to the sterile solution A in the sequence as indicated.
    Final pH of the medium should be 7.2\n– 7.4.","quote_basis":"derivative text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.medium","quote":"{\n            \"id\":
    612,\n            \"name\": \"DESULFOSARCINA CETONICA MEDIUM\",\n            \"complex_medium\":
    \"no\",\n            \"min_pH\": 7.2,\n            \"max_pH\": 7.4,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf\"\n        }","quote_basis":"raw
    UTF-8"}]},{"quantity_id":"q32","label":"SL-10 makeup text at main level","local_fields":[{"path":"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."},"decision":"correct"},{"path":"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."},"decision":"correct"}],"decision":"correct","rationale":"The
    dissolution text and1000ml makeup are source-supported for SL-10. Its unqualified
    placement beside main preparation lacks that stock boundary; relocate the unchanged
    description under SL-10.","source_stage":"SL-10 preparation","sources":[{"evidence_id":"dsm612","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium612.pdf","raw_path":"REVIEW_WORK/batch078/source07-08-10/dsm612.raw","raw_sha256":"99614b4570eb39dd66e6638190fcac466aa3b22b4f3f6a13c782fc19cc634b27","text_sha256":"a45adf3e826d775cb02cb6e5748bc0092a3e963c2dfe732399e613a18f4c5f91","accessed_at":"2026-10-28T20:57:52.031883Z","locator":"dsm612.txt
    lines 70-71","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"},{"evidence_id":"api612","reference":"https://mediadive.dsmz.de/rest/medium/612","raw_path":"REVIEW_WORK/batch078/source07-08-10/api612.raw","raw_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","text_sha256":"e876a448f08aa96e7b2793d90091ae9205e4813095403a8cc8a166e892c3e39e","accessed_at":"2026-10-28T20:57:51.389709Z","locator":"data.solutions[5].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All exact asserted slots and packaged mapping rows are assessed. The other
    stated salts/hydrates agree with current ontology formulas. Nickel has an anhydrous-versus-hexahydrate
    error; neutral resazurin conflicts with sodium wording. Local preferred nickel
    spelling NiCl2 x 6 H2O has REJECTED preferred rows, while Nickel (II) chloride
    hexahydrate has a MAPPED counterpart; cobalt likewise has spelling-specific statuses
    despite a correct hydrate ID. These mapping statuses and canonical labels are
    separate from supplied-form correctness.
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All six complete reports, including the separately scoped JCM 395 sibling,
    and both exact selected parent rows were read. Current API 612 raw digest equals
    the historical digest; literal/decoded source objects match independently, whereas
    null concentration snippets remain unsupported. Current owner bytes equal the
    recorded unchanged before/after hashes. Current importer preserves primary stock
    descriptors but maps bare ml to ML_PER_L and flattens preparation steps; current
    conservative merge does not justify historical signature equivalence. Stored .fZ
    and missing-offset events remain immutable provenance limitations.
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - historical-object-joins
  - writer-mediadive
  - writer-formulation
  - writer-merger
  - historical-selected-parent-rows
  - historical-parent-authentication
  - writer-komodo
- assessment_id: high-metal
  area: consistency
  topic: High-metal classification
  outcome: unknown
  summary: 'The selected target and both maintained owners retain high_metal: true.
    Flattened trace-stock concentrations do not establish high final-medium metal
    exposure, and the reviewed sources do not independently justify this classification.
    Preserve the flag as unresolved pending explicit classification evidence; no new
    exposure or growth inference is made.'
  target_ids:
  - CultureMech:001741
  evidence_ids:
  - target
  - owner
  - owner-2
  - quantities
findings:
- finding_id: f1
  issue_key: culturemech-001741-stock-stage-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore Solution A–D and nested SL-10 boundaries
  description: All 19 ingredient rates are source-stage values flattened into the
    final-medium list. Reconstruct Solution A–D and the SL-10 substock using the printed
    receiving volumes. Preserve positive provider stage-rate support and SL-10 explicit
    1000 ml makeup; do not infer measured final volume from water or sum rates with
    different preparation denominators. For HCl 25%, retain the native volume until
    percentage basis is established. The copied KOMODO formulation needs its own source
    reconciliation.
  target_ids:
  - CultureMech:001741
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - target
  - owner
  - owner-2
  - dsm612
  - api612
  - quantities
  - writer-mediadive
  rule_id: review-ingredient-concentrations/evidence-contract
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
- finding_id: f2
  issue_key: culturemech-001741-stock-preparation-scope
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Scope retained stock preparation and resolve the aerobic branch note
  description: Target and DSM owner retain the correct complete main preparation,
    but the SL-10 dissolution/makeup instruction is an unqualified main step. Reattach
    that unchanged stock text. The KOMODO owner has no main method and asserts Aerobic:Yes,
    conflicting with the named DSM preparation; resolve that exact branch before inheriting
    the DSM recipe.
  target_ids:
  - CultureMech:001741
  field_paths:
  - data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml::preparation_steps[1]
  - preparation_steps[1]
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::notes
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::preparation_steps
  evidence_ids:
  - dsm612
  - api612
  - writer-mediadive
  - writer-komodo
  - owner
  - owner-2
  rule_id: review-yaml-record/representation
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
- finding_id: f3
  issue_key: culturemech-001741-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct nickel supplied-form mapping
  description: All three documents name nickel chloride hexahydrate but assert anhydrous
    CHEBI:34887 in primary and secondary slots. Fresh CHEBI:53542 explicitly has six
    waters. Reconcile the asserted form and retain the source stock mass; current
    MIM spelling status does not override molecular identity.
  target_ids:
  - CultureMech:001741
  field_paths:
  - data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml::ingredients[17].term
  - data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml::ingredients[17].mediaingredientmech_chebi_term
  evidence_ids:
  - dsm612
  - api612
  - chebi34887
  - chebi53542
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
- finding_id: f4
  issue_key: culturemech-001741-resazurin-sodium-form
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve the sodium-resazurin form
  description: All three preferred terms and the source specify sodium resazurin,
    whereas CHEBI:8806 represents neutral resazurin C12H7NO4. The packaged MIM synonym
    also conflates sodium wording with that neutral concept. Resolve the supplied
    sodium-salt identity without changing the printed amount or certifying a guessed
    replacement.
  target_ids:
  - CultureMech:001741
  field_paths:
  - data/merge_yaml/merged/DESULFOSARCINA_CETONICA_MEDIUM.yaml::ingredients[6].term
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::ingredients[6].term
  - data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml::ingredients[6].term
  evidence_ids:
  - dsm612
  - api612
  - chebi8806
  - groundings
  rule_id: review-yaml-record/grounding
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
- finding_id: f5
  issue_key: culturemech-001741-historical-branch-identity
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Retain unresolved exact KOMODO identity and duplicate relationship
  description: The historical catalogue row connects KOMODO 612 to DSM 612, but current
    exact recipe and both catalogue routes return 403. The current parent/variant
    duplicate relationship is based on copied composition and signature, which does
    not independently establish source equivalence. Keep the branch, duplicated-source
    relationship and aerobic contradiction explicitly unresolved while curating the
    supported DSM formulation.
  target_ids:
  - CultureMech:001741
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::media_term
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::variant_children
  - data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml::parent_media
  - parent_media
  - merged_from
  evidence_ids:
  - komodo612
  - komodoHistoricalList
  - historical-selected-parent-rows
  - historical-parent-authentication
  - writer-formulation
  rule_id: review-yaml-record/identity
  native_severity: P2
  normalization_reason: Material scientific stage, amount, supplied-form or source-support
    issue; native shape checks pass, so no critical schema blocker is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
- finding_id: f6
  issue_key: culturemech-001741-history-and-quantity-evidence
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Append source claims and preserve prior event history
  description: No scoped ingredient claim is attached despite retained amounts. Attach
    exact current evidence at each source stage. Preserve earlier events and append
    a new correction; the stored KOMODO timestamp ends .fZ and a later event lacks
    a UTC offset. Correct future writer timestamp generation using a UTC-capable formatter,
    distinguishing its current %f directive from stored historical text.
  target_ids:
  - CultureMech:001741
  field_paths:
  - data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml::curation_history
  - ingredients
  evidence_ids:
  - old-claims
  - history
  - writer-komodo
  - quantities
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded metadata, provenance or unresolved grounding follow-up;
    no critical scientific failure is inferred.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained importer and timestamp writer
actions:
- action_id: a1
  description: All 19 ingredient rates are source-stage values flattened into the
    final-medium list. Reconstruct Solution A–D and the SL-10 substock using the printed
    receiving volumes. Preserve positive provider stage-rate support and SL-10 explicit
    1000 ml makeup; do not infer measured final volume from water or sum rates with
    different preparation denominators. For HCl 25%, retain the native volume until
    percentage basis is established. The copied KOMODO formulation needs its own source
    reconciliation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001741
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: Target and DSM owner retain the correct complete main preparation,
    but the SL-10 dissolution/makeup instruction is an unqualified main step. Reattach
    that unchanged stock text. The KOMODO owner has no main method and asserts Aerobic:Yes,
    conflicting with the named DSM preparation; resolve that exact branch before inheriting
    the DSM recipe.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001741
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: All three documents name nickel chloride hexahydrate but assert anhydrous
    CHEBI:34887 in primary and secondary slots. Fresh CHEBI:53542 explicitly has six
    waters. Reconcile the asserted form and retain the source stock mass; current
    MIM spelling status does not override molecular identity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001741
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: All three preferred terms and the source specify sodium resazurin,
    whereas CHEBI:8806 represents neutral resazurin C12H7NO4. The packaged MIM synonym
    also conflates sodium wording with that neutral concept. Resolve the supplied
    sodium-salt identity without changing the printed amount or certifying a guessed
    replacement.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001741
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a5
  description: The historical catalogue row connects KOMODO 612 to DSM 612, but current
    exact recipe and both catalogue routes return 403. The current parent/variant
    duplicate relationship is based on copied composition and signature, which does
    not independently establish source equivalence. Keep the branch, duplicated-source
    relationship and aerobic contradiction explicitly unresolved while curating the
    supported DSM formulation.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001741
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a6
  description: No scoped ingredient claim is attached despite retained amounts. Attach
    exact current evidence at each source stage. Preserve earlier events and append
    a new correction; the stored KOMODO timestamp ends .fZ and a later event lacks
    a UTC offset. Correct future writer timestamp generation using a UTC-capable formatter,
    distinguishing its current %f directive from stored historical text.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:001741
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_612_DESULFOBACTERIUM_CETONICUM_MEDIUM.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfosarcina_cetonica_medium.yaml
    role: maintained source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: maintained importer and timestamp writer
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  - Verify the current KOMODO importer emits literal UTC Z with actual microseconds
    without time.strftime %f; existing historical event bytes remain unchanged.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- Partial completion reflects inaccessible exact KOMODO recipe/catalogue sources.
  Historical copied DSM content does not certify the KOMODO formulation or duplicate
  relationship.
- Primary receiving volumes sum 1002 ml, matching provider total metadata, but this
  is not an independent measured-final-volume statement. Solution A listed inputs
  sum 961.5 ml while its declared receiving amount/provider basis is 962 ml. Preserve
  the explicit declarations and source discrepancy.
- No ingredient source claims are attached; new support is evidence_only, not retroactive
  verified evidence. The 25% HCl basis/density remains unresolved.
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
