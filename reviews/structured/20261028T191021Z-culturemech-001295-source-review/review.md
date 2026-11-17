# Scientific review: DESULFOCAPSA SULFEXIGENS MEDIUM

- Review: 20261028T191021Z-culturemech-001295-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T18:55:09.192814Z
- Finished UTC: 2026-10-28T19:10:21.040819Z
- Reviewer: Codex batch006_validation (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM196 supports separate A/B/C and SL-10 recipes, but their nineteen rates are flattened into main ingredients. Correct stage topology and nickel hydrate assertions, retain supported preparation, and resolve three unavailable modified-strain identities before propagating base corrections.

## Scope And Provenance

Whole exact target/owner with explicit scoped dependencies, current sources and historical claims.

Selection: Authoritative batch075 index 02
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001295 | data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml | generated | desulfocapsa_sulfexigens_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:001295 | Actual exit 0; full original streams retained. |
| Canonical strict | passed | True | CultureMech:001295 | Actual exit 0; full original streams retained. |
| Canonical terms | passed | True | CultureMech:001295 | Actual exit 0; full original streams retained. |
| Canonical references | passed | True | CultureMech:001295 | Actual exit 0; full original streams retained. |

## Scientific And Domain Assessments

### Base and modified source scope

identity: concern. Targets: CultureMech:001295.

The DSM196 base is available in full primary and provider sources, but three strain-modified KOMODO formulations remain unavailable. Their copied equality is not proof of identity. Five exact maintained contributors and the generated record were read in full.

### Retained classification and preparation

representation: supported. Targets: CultureMech:001295.

DEFINED/DEFINED and LIQUID agree with the known base formulation. Current pH7.2 and the two main preparation notes are supported for DSM196; the third text is supported only as SL-10 preparation. No source temperature or strain growth claim is invented.

### Complete amounts, units and preparation stages

quantity: concern. Targets: CultureMech:001295.

114 current concentration fields are covered by 30 decisions, including unchanged support and explicit source-only conditions.

{"schema":"fresh-b075-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","quantity_field_count":114,"decisions":[{"quantity_id":"q1","label":"FeCl3 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\": 82,\n                        \"amount\": 2.7,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.80957,\n                        \"mmol_l\": 10.3944,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 21-21","quote":"FeCl3 x 6 H2O                                           2.70        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q2","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.12175,\n                        \"mmol_l\": 21.978,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 22-22","quote":"Na2SO4                                                  3.00        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q3","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.208117,\n                        \"mmol_l\": 1.52931,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 23-23","quote":"KH2PO4                                                  0.20        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.312175,\n                        \"mmol_l\": 5.83613,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 24-24","quote":"NH4Cl                                                   0.30        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q5","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 21,\n                        \"unit\": \"g\",\n                        \"g_l\": 21.8522,\n                        \"mmol_l\": 373.926,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 25-25","quote":"NaCl                                                   21.00        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3.12175,\n                        \"mmol_l\": 15.3552,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 26-26","quote":"MgCl2 x 6 H2O                                           3.00        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.520291,\n                        \"mmol_l\": 6.97909,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 27-27","quote":"KCl                                                     0.50        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q8","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.156087,\n                        \"mmol_l\": 1.06171,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 28-28","quote":"CaCl2 x 2 H2O                                           0.15        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q9","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution B, provider-declared 30 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\": 471.752,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 35-35","quote":"Na2CO3                                                  1.50        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q10","label":"Na2S2O3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution C, provider-declared 10 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\": 65,\n                        \"amount\": 2.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 250,\n                        \"mmol_l\": 1007.31,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 41-41","quote":"Na2S2O3 x 5 H2O                                         2.50        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q11","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium dose. Preserve reagent volume/strength and the explicit final stock makeup, then separate stock from receiving medium. Modified-strain applicability remains unsupported.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 47-47","quote":"HCl (25%)                                              10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium dose. Preserve reagent volume/strength and the explicit final stock makeup, then separate stock from receiving medium. Modified-strain applicability remains unsupported."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium dose. Preserve reagent volume/strength and the explicit final stock makeup, then separate stock from receiving medium. Modified-strain applicability remains unsupported."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium dose. Preserve reagent volume/strength and the explicit final stock makeup, then separate stock from receiving medium. Modified-strain applicability remains unsupported."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q12","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 48-48","quote":"FeCl2 x 4 H2O                                           1.50        g","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q13","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[2]","quote":"{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 58-58","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q14","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[3]","quote":"{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 59-59","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q15","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[4]","quote":"{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 60-60","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q16","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[5]","quote":"{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 61-61","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q17","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[6]","quote":"{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 62-62","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q18","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[7]","quote":"{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 63-63","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q19","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10 stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 64-64","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The stored rate matches explicit provider g_l for this named solution, but its current unqualified main-medium placement is wrong. Preserve the primary batch mass and the separately stated solution receiving dose; the main 961+30+10 ml table is not an independent measured final-volume statement. The three modified-strain owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q20","label":"Solution A receiving volume","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\": 1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\": 403,\n                        \"amount\": 961,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 3-3","quote":"Solution A                                            961.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q21","label":"Solution B receiving volume","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\": 3,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\": 405,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 4-4","quote":"Solution B                                             30.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q22","label":"Solution C receiving volume","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\": 4,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\": 406,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 5-5","quote":"Solution C                                             10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q23","label":"SL-10 receiving dose in A","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 29-29","quote":"Trace element solution SL-10                            1.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q24","label":"A water input","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 960,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 30-30","quote":"Distilled water                                       960.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q25","label":"B water input","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 30,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 36-36","quote":"Distilled water                                        30.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q26","label":"C water input","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 42-42","quote":"Distilled water                                        10.00       ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q27","label":"SL-10 water input","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only structural control for the exact DSM196 base recipe. Preserve the stated volume at this named stage; input water is not final makeup, and this source does not verify the three modified-strain formulations.","source_stage":"DSM196 exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[9]","quote":"{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 65-65","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative text"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Retained main preparation and final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"First dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0 with 1 N NaOH (about 3 ml). Add and dissolve remaining salts of solution A and sparge medium with 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute under same gas atmosphere in anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution C is autoclaved separately under 100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions B and C are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be adjusted to 7.2."}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"First dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0 with 1 N NaOH (about 3 ml). Add and dissolve remaining salts of solution A and sparge medium with 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute under same gas atmosphere in anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution C is autoclaved separately under 100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions B and C are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be adjusted to 7.2."}},{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"The retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt, pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C atmospheres and ordered addition. Existing support needs linkage; modified-strain transfer remains unverified.","source_stage":"DSM196 main preparation","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\": \"First dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0 with 1 N NaOH (about 3 ml). Add and dissolve remaining salts of solution A and sparge medium with 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute under same gas atmosphere in anoxic Hungate-type tubes or serum vials and autoclave. Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution C is autoclaved separately under 100% N2 gas atmosphere. To complete the medium appropriate amounts of solutions B and C are added to the sterile solution A in the sequence as indicated. Final pH of the medium should be adjusted to 7.2.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 7-14","quote":"1. First dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0 with 1 N\nNaOH (about 3 ml). Add and dissolve remaining salts of solution A and sparge medium\nwith 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute under same gas\natmosphere in anoxic Hungate-type tubes or serum vials and autoclave. Solution B is\nautoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution C is\nautoclaved separately under 100% N2 gas atmosphere. To complete the medium\nappropriate amounts of solutions B and C are added to the sterile solution A in the\nsequence as indicated. Final pH of the medium should be adjusted to 7.2.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt, pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C atmospheres and ordered addition. Existing support needs linkage; modified-strain transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt, pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C atmospheres and ordered addition. Existing support needs linkage; modified-strain transfer remains unverified."},{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt, pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C atmospheres and ordered addition. Existing support needs linkage; modified-strain transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt, pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C atmospheres and ordered addition. Existing support needs linkage; modified-strain transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt, pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C atmospheres and ordered addition. Existing support needs linkage; modified-strain transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ph_value","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ph_value","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ph_value","decision":"unsupported","rationale":"The stored value/text is an exact copy of the DSM196 base content, but the specific modified accession is unavailable. Preserve the copy as historical content; its applicability to this variant is not established by the base recipe or strain catalogue identity."}]},{"quantity_id":"q29","label":"Retained inoculum note","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"Note: For transfers use 5 - 10% (v/v) inoculum."}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"Note: For transfers use 5 - 10% (v/v) inoculum."}}],"decision":"evidence_only","rationale":"The note faithfully preserves the primary5–10%(v/v) inoculum range. It is source context for the exact base recipe, not a new growth assertion or verified prescription for modified-strain records.","source_stage":"DSM196 transfer note","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\": \"Note: For transfers use 5 - 10% (v/v) inoculum.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 15-15","quote":"2. Note: For transfers use 5 - 10% (v/v) inoculum.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"evidence_only","rationale":"The note faithfully preserves the primary5–10%(v/v) inoculum range. It is source context for the exact base recipe, not a new growth assertion or verified prescription for modified-strain records."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[1]","decision":"evidence_only","rationale":"The note faithfully preserves the primary5–10%(v/v) inoculum range. It is source context for the exact base recipe, not a new growth assertion or verified prescription for modified-strain records."}]},{"quantity_id":"q30","label":"Retained SL-10 makeup step","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"DISSOLVE","description":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The text and explicit1000ml final stock makeup are supported, but this is SL-10 preparation and is currently an unqualified main-medium step. Preserve the wording and place it under SL-10; do not treat it as main final volume.","source_stage":"SL-10 stock preparation","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].steps[0]","quote":"{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt lines 67-68","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"The text and explicit1000ml final stock makeup are supported, but this is SL-10 preparation and is currently an unqualified main-medium step. Preserve the wording and place it under SL-10; do not treat it as main final volume."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"The text and explicit1000ml final stock makeup are supported, but this is SL-10 preparation and is currently an unqualified main-medium step. Preserve the wording and place it under SL-10; do not treat it as main final volume."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml":null,"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml":null,"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml":null,"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml":null,"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml":null},"scope":"Every selected target/owner concentration plus explicit dependency fields; source-only rows/conditions and unchanged claims distinguished. Excluded parent quantities are not transferred."}

### Supplied forms and current ontology/MIM scope

grounding: concern. Targets: CultureMech:001295.

All selected primary and secondary chemical slots were compared with current OLS scientific objects and exact packaged MIM rows. Nickel34887 is anhydrous despite explicit hexahydrate naming;53542 supports the source form. Current cobalt53503 is already hexahydrate and should be retained. The preferred NiCl2 x 6 H2O and CoCl2 x 6 H2O MIM rows are REJECTED, while a separate preferred Nickel (II) chloride hexahydrate row is MAPPED. Other exact hydrates and neutral HCl/boric acid assertions agree with their source names; this does not certify an unavailable variant.

### Existing repair credit and writer limits

provenance: concern. Targets: CultureMech:001295.

All eleven scoped report bodies and five selected parent rows were read. October5 zero-source-check triage is not scientific validation. October7 source-table claims authenticate current raw content where exact objects/digests match, not the original retrieval event. Existing resolver histories document DSM196 copying without proving strain modifications. Current parser, conservative grouping and timestamp writers are separately observed; malformed/naive original events remain append-only provenance.

## Findings

### f1: Restore separate A, B, C and SL-10 stages

major / open / confirmed; issue key: culturemech-001295-solution-stage.

Nineteen direct ingredients flatten four distinct source solutions: eight A rates, B carbonate, C thiosulfate and nine SL-10 entries. Preserve their supported source amounts, rebuild exact solution topology and receiving doses, and move the supported1000ml makeup step under SL-10. Do not turn bare25% HCl into a mass dose or the961+30+10ml table into a measured final volume. Restrict this reconstruction to the supported DSM196 base while variant identity remains unresolved.

### f2: Reconcile base and modified-strain identities before co-merging

major / open / provisional; issue key: culturemech-001295-variant-identity.

The generated record lumps DSM196, KOMODO196 and three explicitly modified accessions196_11383/196_13871/196_9700. Exact current KOMODO routes and catalogue returned403; equal copied values and old resolver events do not establish equivalence. Current DSM catalogue identities distinguish the three environmental strains, but those metadata pages do not recover the modifications. Preserve all accessions and histories; resolve exact variants before adopting synonym/duplicate relationships or propagating base corrections. The four KOMODO owners also lack the retained DSM preparation steps. Current conservative merger includes preparation and relationship fields and does not certify this old ingredient-based merge.

### f3: Correct both nickel hydrate assertions

major / open / confirmed; issue key: culturemech-001295-nickel-hydrate.

Both primary and secondary CHEBI:34887 slots describe anhydrous nickel dichloride despite explicit NiCl2·6H2O in the selected name and base primary source. Verify CHEBI:53542 and exact supplied form while preserving source stock amount and unresolved variant applicability. MIM has a MAPPED preferred Nickel (II) chloride hexahydrate row and a distinct REJECTED NiCl2 x 6 H2O row; these spelling-specific statuses are not interchangeable.

### f4: Link retained supported content to exact source stages

minor / open / confirmed; issue key: culturemech-001295-claim-evidence.

No selected ingredient or preparation claim is attached. Add ingredient evidence at ingredients[i].evidence and stage/preparation evidence at root evidence with precise field and solution locators, retaining the supported main paragraph, inoculum note, pH and SL-10 makeup. Historical quoted source objects are separate from attached evidence and do not verify modified-strain recipes.

### f5: Preserve original history and correct future event metadata

minor / open / confirmed; issue key: culturemech-001295-event-metadata.

The four KOMODO owners retain malformed literal .fZ import timestamps and timezone-naive resolver timestamps. Preserve those original events byte-for-byte; append verified context only if authoritative provenance is recovered. Correct the current importer/resolver writers for future timezone-aware UTC events; do not invent historical times or rewrite old strings.

## Recommended Actions And Acceptance Checks

### a1

Nineteen direct ingredients flatten four distinct source solutions: eight A rates, B carbonate, C thiosulfate and nine SL-10 entries. Preserve their supported source amounts, rebuild exact solution topology and receiving doses, and move the supported1000ml makeup step under SL-10. Do not turn bare25% HCl into a mass dose or the961+30+10ml table into a measured final volume. Restrict this reconstruction to the supported DSM196 base while variant identity remains unresolved.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a2

The generated record lumps DSM196, KOMODO196 and three explicitly modified accessions196_11383/196_13871/196_9700. Exact current KOMODO routes and catalogue returned403; equal copied values and old resolver events do not establish equivalence. Current DSM catalogue identities distinguish the three environmental strains, but those metadata pages do not recover the modifications. Preserve all accessions and histories; resolve exact variants before adopting synonym/duplicate relationships or propagating base corrections. The four KOMODO owners also lack the retained DSM preparation steps. Current conservative merger includes preparation and relationship fields and does not certify this old ingredient-based merge.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a3

Both primary and secondary CHEBI:34887 slots describe anhydrous nickel dichloride despite explicit NiCl2·6H2O in the selected name and base primary source. Verify CHEBI:53542 and exact supplied form while preserving source stock amount and unresolved variant applicability. MIM has a MAPPED preferred Nickel (II) chloride hexahydrate row and a distinct REJECTED NiCl2 x 6 H2O row; these spelling-specific statuses are not interchangeable.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a4

No selected ingredient or preparation claim is attached. Add ingredient evidence at ingredients[i].evidence and stage/preparation evidence at root evidence with precise field and solution locators, retaining the supported main paragraph, inoculum note, pH and SL-10 makeup. Historical quoted source objects are separate from attached evidence and do not verify modified-strain recipes.

- Curate only named maintained fields after exact source-stage reconciliation; retain prior history and append a new actual curation event.
- Attach literal source evidence; preserve uncertainty about final volume, unspecified hydrates and percent basis. Recheck all affected quantities and ontology assertions.
- Regenerate the selected target using current conservative merge workflow, check freshness and rerun schema, strict, terms and reference diagnostics.

### a5

The four KOMODO owners retain malformed literal .fZ import timestamps and timezone-naive resolver timestamps. Preserve those original events byte-for-byte; append verified context only if authoritative provenance is recovered. Correct the current importer/resolver writers for future timezone-aware UTC events; do not invent historical times or rewrite old strings.

- Original historical events remain byte-identical; any verified correction/context is appended as a new event with its source.
- Both named current writers emit real timezone-aware UTC timestamps without a literal %f/.fZ or naive local time; validate a representative future event without rewriting existing records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| dsmz196 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf; REVIEW_WORK/batch075/source01-03-supplement/dsmz196.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| api196 | https://mediadive.dsmz.de/rest/medium/196; REVIEW_WORK/batch075/source01-03-supplement/api196.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo196 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196; REVIEW_WORK/batch075/source01-03-supplement/komodo196.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo196_11383 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_11383; REVIEW_WORK/batch075/source01-03-supplement/komodo196_11383.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo196_13871 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_13871; REVIEW_WORK/batch075/source01-03-supplement/komodo196_13871.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodo196_9700 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_9700; REVIEW_WORK/batch075/source01-03-supplement/komodo196_9700.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| komodoList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; REVIEW_WORK/batch075/source01-03-supplement/komodoList.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| identityDSM11383 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-11383; REVIEW_WORK/batch075/source01-03-supplement/identityDSM11383.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| identityDSM13871 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-13871; REVIEW_WORK/batch075/source01-03-supplement/identityDSM13871.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| identityDSM9700 | https://www.dsmz.de/collection/catalogue/details/culture/DSM-9700; REVIEW_WORK/batch075/source01-03-supplement/identityDSM9700.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; REVIEW_WORK/batch075/source01-03-supplement/chebi53542.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| target | data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml; Complete file | context_only | Complete generated target. |
| owner | data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml; Complete file | context_only | Complete exact maintained owner. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Complete file | context_only | Exact packaged current identifier/ontology_id and preferred-term rows. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete file | context_only | Exact packaged snapshot version and checksum. |
| writer-formulation | src/culturemech/merge/formulation.py; Full formulation comparison | context_only | Current scientific-field equality includes quantities, stocks and notes; no chemical equivalence is inferred. |
| writer-merger | src/culturemech/merge/merger.py; RecipeMerger.merge_group | context_only | Current merge_group copies singletons and rejects incompatible multiple formulations. Generated staleness is not evidence that current code permits ingredient-only merging. |
| owner-2 | data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-3 | data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-4 | data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| owner-5 | data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml; Complete file | context_only | Complete exact additional maintained owner. |
| report-20 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-21 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/desulfobulbus_sp_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-22 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_11383.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-23 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_13871.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-24 | reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_9700.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-25 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json; Exact selected row locators in historical-selected-parent-rows.json | context_only | Historical repository parent; only exact selected record objects are joined. Decoded data is not itself original external raw evidence. |
| report-26 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfocapsa_sulfexigens_medium.yaml.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-27 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-28 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_sp_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-29 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-30 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-31 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| report-32 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.md; Complete report | context_only | Prior exact-header assessment; old source/check claims are not newly executed. |
| historical-reading | REVIEW_WORK/batch075/record02/historical-reading.json; Complete artifact; exact original input paths and hashes retained | context_only | Lossless exact report cells and independently joined current decoded source objects. |
| historical-selected-parent-rows | REVIEW_WORK/batch075/record02/historical-selected-parent-rows.json; Complete artifact; exact original input paths and hashes retained | context_only | Exact selected historical parent objects; parent provenance only, not automatic original source authentication. |
| complete-document-reader | REVIEW_WORK/batch075/record02/complete-document-reader.json; Complete artifact; exact original input paths and hashes retained | context_only | Complete exact target and owner parsed documents with lossless long-string pooling. |
| writer-matcher | src/culturemech/merge/matcher.py; group_formulations | context_only | Current group_formulations uses conservative FormulationFingerprinter; ingredient similarity is only candidate discovery. |
| writer-cleanup | scripts/cleanup_media_quality.py; MediaQualityFixer._merge_ingredient_group | context_only | Current _merge_ingredient_group keeps identical duplicate amounts and flags disagreements; it no longer sums duplicate quantities. It cannot establish compatible stock/main bases or repair a historical flattened sum. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; MediaDiveImporter._parse_api_composition; _is_api_stock_addition; _parse_api_solutions; _normalize_unit | context_only | Current _parse_api_composition reads only the first API solution, excludes water and recognized stock additions, and prefers explicit g_l. _parse_api_solutions preserves referenced stocks separately. Thus current code does not flatten all five API196 solutions as these records do; this does not identify the historical execution. Unit normalization alone does not establish final volume. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; KomodoWebImporter._convert_to_culturemech | context_only | Current _convert_to_culturemech uses time.strftime with a literal %f directive, which does not provide microseconds here. Existing malformed history is retained as provenance; current behavior is not independent proof of past execution. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; DSMZCompositionResolver.extract_dsmz_id; merge_composition; _add_enrichment_metadata | context_only | Current DSMZCompositionResolver.merge_composition copies source composition into a new object; extract_dsmz_id strips alphabetic suffixes, and _add_enrichment_metadata emits naive datetime.now().isoformat(). Exact existing events document DSMZ196 copying; current code is separately observed, not authenticated historical execution. |
| chebi86254 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254; REVIEW_WORK/batch075/source01-03-supplement/chebi86254.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149; REVIEW_WORK/batch075/source01-03-supplement/chebi32149.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036; REVIEW_WORK/batch075/source01-03-supplement/chebi63036.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; REVIEW_WORK/batch075/source01-03-supplement/chebi31206.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; REVIEW_WORK/batch075/source01-03-supplement/chebi26710.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345; REVIEW_WORK/batch075/source01-03-supplement/chebi86345.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; REVIEW_WORK/batch075/source01-03-supplement/chebi32588.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; REVIEW_WORK/batch075/source01-03-supplement/chebi86158.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377; REVIEW_WORK/batch075/source01-03-supplement/chebi29377.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi32150 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32150; REVIEW_WORK/batch075/source01-03-supplement/chebi32150.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883; REVIEW_WORK/batch075/source01-03-supplement/chebi17883.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249; REVIEW_WORK/batch075/source01-03-supplement/chebi86249.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976; REVIEW_WORK/batch075/source01-03-supplement/chebi49976.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368; REVIEW_WORK/batch075/source01-03-supplement/chebi86368.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; REVIEW_WORK/batch075/source01-03-supplement/chebi33118.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503; REVIEW_WORK/batch075/source01-03-supplement/chebi53503.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318; REVIEW_WORK/batch075/source01-03-supplement/chebi86318.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887; REVIEW_WORK/batch075/source01-03-supplement/chebi34887.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; REVIEW_WORK/batch075/source01-03-supplement/chebi75213.json; exact original raw/text/hash/time metadata | context_only | Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence after ordinary identity preflight; no variant transfer or growth inference. |
| quantities | REVIEW_WORK/batch075/record02/quantity-inventory.json; Complete sidecar | supports | Complete source-stage quantity decisions. |
| groundings | REVIEW_WORK/batch075/record02/grounding-inventory.json; Complete sidecar | supports | Exact slots, raw OLS scientific objects and current MIM rows. |
| census | REVIEW_WORK/batch075/record02/field-census.json; Complete sidecar | supports | Complete scalar census with explicit dependency exclusions. |
| numeric-census | REVIEW_WORK/batch075/record02/numeric-field-census.json; Complete sidecar | supports | Numeric/text assertions and quantity joins. |
| history | REVIEW_WORK/batch075/record02/history-inventory.json; Complete sidecar | supports | Current exact histories, without replay. |
| old-reports | REVIEW_WORK/batch075/record02/history-report-inventory.json; Complete sidecar | supports | Exact historical report scopes. |
| old-claims | REVIEW_WORK/batch075/record02/existing-claim-authentication.json; Complete sidecar | context_only | No attached claims to authenticate; historical source objects are separately assessed in historical-source-joins.json. |
| historical-source-joins | REVIEW_WORK/batch075/record02/historical-source-joins.json; Every literal/decoded historical source-object row and exact current-source match | context_only | Historical quoted source content and raw-digest equality where actually matched; independent of attached local claims and original access-event recovery. |
| check-schema | REVIEW_WORK/batch075/record02/validate-schema.json | supports | Original once-only canonical schema with complete argv/time/streams; reference count zero does not verify sources. |
| check-strict | REVIEW_WORK/batch075/record02/validate-strict.json | supports | Original once-only canonical strict with complete argv/time/streams; reference count zero does not verify sources. |
| check-terms | REVIEW_WORK/batch075/record02/validate-terms.json | supports | Original once-only canonical terms with complete argv/time/streams; reference count zero does not verify sources. |
| check-references | REVIEW_WORK/batch075/record02/validate-references.json | supports | Original once-only canonical references with complete argv/time/streams; reference count zero does not verify sources. |

## Limits And Additional Notes

- Exact KOMODO196 and all three modified MediaInfo routes plus MediaList returned403. Review is partial: DSM196 corrections cannot automatically replace or certify any modified-strain formulation. Current DSM strain metadata is identity evidence only.
- No strain-growth claim, optimization or experimental recommendation is inferred from the medium name or general source identity.
- The MIM snapshot commit is 6643131b0f12ab40b66f98135245fca04027e0e9; present/absent rows do not establish a historical or live-catalog result.
- Input water is not measured final volume. Explicit provider g_l rates are assessed only on their declared normalization basis; unspecified percent bases and hydrate numbers remain unresolved.
- No source changes, formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T191021Z-culturemech-001295-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Scientific review: DESULFOCAPSA SULFEXIGENS MEDIUM'
started_at: '2026-10-28T18:55:09.192814Z'
finished_at: '2026-10-28T19:10:21.040819Z'
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
summary: DSM196 supports separate A/B/C and SL-10 recipes, but their nineteen rates
  are flattened into main ingredients. Correct stage topology and nickel hydrate assertions,
  retain supported preparation, and resolve three unavailable modified-strain identities
  before propagating base corrections.
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
  - path: data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
    sha256: bb642c6b50f745a57c76b3c53960805676a3be275c27edee7cc07bf4dd776b4b
    role: target
  - path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    sha256: 6743c3d96724ec5d445a4a5892430cd042362f05b728f87f6bb13a6ce084404d
    role: context
  - path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    sha256: e0f8d2045a0d6cfba1f465b321f8d790873408e9bef9f27634148807e947b2bc
    role: context
  - path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    sha256: b0944636d00d087f3a15925840bfa0120cd679ecaf2abe3dab0cd22b0a23e536
    role: context
  - path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    sha256: aed4537cd3d21b9b56aece1d1d80fd7a8e3848bc76c8ca8c15b68b40f8dd55a2
    role: context
  - path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    sha256: b764d20ca2e90b2825caadf29f623e7ae723d05c2a2cabdfd33fa6009ffa14e6
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
    sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/desulfobulbus_sp_medium.yaml.md
    sha256: 9e5aff8155ec3e53a238b3c5d17d60b4a866459707e36a9f720df820dfa16aff
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_11383.yaml.md
    sha256: 7b39389cf89e2fb22e0fa2ffaf7ea0d7275900feed2d31e0e6d134f08b92650f
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_13871.yaml.md
    sha256: e07070efbf61595a9864f039a6ebeeb36344d11b516e40cdacf3dd0fedb13ce3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_9700.yaml.md
    sha256: 214ff3541e51c11ba6011582ef61453102d83df60412afc901a0675ba77f3147
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
    sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfocapsa_sulfexigens_medium.yaml.md
    sha256: 9abfc8fe128a7296998d220459f710b52afdfa60f3d48ab3ca252a1ced117d28
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.md
    sha256: a10db3063a5342864395cc3f56335635043e57b224d60975b4d21af9dbf79ca5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_sp_medium.md
    sha256: 10d6a2aad1030f0e9220f96e66183a9ba9362361e921fc414c38200755414404
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.md
    sha256: 304f3e0d616cfd58a2f57e8cd963ffcd9121064aaf14ecfc77be7e620adc1b66
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.md
    sha256: 886a3e730062c30a5d2d9c16161d47bbd4944660e3ea59d13e46ca924ee72566
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.md
    sha256: 212eb51d4582af0aae3c43bbbdf80a4291403e09abee1260acf526bc52635932
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.md
    sha256: 89f013d4b9381d8dc1287881f4ddc40c3e0e270ad7fdc9b19b2376dee168b9d7
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
  selection: Authoritative batch075 index 02
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001295
targets:
- target_id: CultureMech:001295
  path: data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
  label: desulfocapsa_sulfexigens_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit 0; full original streams retained.
  target_ids:
  - CultureMech:001295
  command: just validate-schema data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
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
  - CultureMech:001295
  command: just validate-strict data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
    --out REVIEW_WORK/batch075/record02/strict.tsv --workers 1 --quiet
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
  - CultureMech:001295
  command: just validate-terms data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
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
  - CultureMech:001295
  command: just validate-references data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: dsmz196
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf
  accessed_at: '2026-10-28T18:55:36.172246Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/dsmz196.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f
- evidence_id: api196
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/196
  accessed_at: '2026-10-28T18:55:35.882016Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/api196.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094
- evidence_id: komodo196
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196
  accessed_at: '2026-10-28T18:55:35.419805Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/komodo196.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 75adde28b9df34197058a967888f1f9710d8ec34e74ebe970411724ae24e1aad
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo196_11383
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_11383
  accessed_at: '2026-10-28T18:55:35.481334Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/komodo196_11383.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4747571576913b02a245ed0974c0a73e63b00d9bb5114e318360b695bb481611
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_11383;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo196_13871
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_13871
  accessed_at: '2026-10-28T18:55:35.637718Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/komodo196_13871.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 0f037c464d822bf755ce3665bc13a78b7c79f12ae971820834c2c35b4d29d1bc
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_13871;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodo196_9700
  kind: search
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_9700
  accessed_at: '2026-10-28T18:55:35.775771Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/komodo196_9700.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 946639ace52c9cc630a3c4bac7ed7986969d4d58513dcea9d976c234432644c1
  search_scope: One exact public GET of https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=196_9700;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: komodoList
  kind: search
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  accessed_at: '2026-10-28T18:55:35.838397Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/komodoList.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 727c842af5ef51539bffb176e1732e3d7b361f54bf3b3add8138a9594ae2a343
  search_scope: One exact public GET of https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList;
    retained status 403. No exhaustive repository or literature absence claim.
- evidence_id: identityDSM11383
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-11383
  accessed_at: '2026-10-28T18:55:37.689422Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/identityDSM11383.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9f7155dd456a4f18db735a8e142152e43e4d571c85369b2190a907cdc5bfb6c2
- evidence_id: identityDSM13871
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-13871
  accessed_at: '2026-10-28T18:55:37.746686Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/identityDSM13871.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 98fe9f9fdb499a825df87562145d7214f95728998a98372db3ccda442b73fba2
- evidence_id: identityDSM9700
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-9700
  accessed_at: '2026-10-28T18:55:37.752234Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/identityDSM9700.json; exact
    original raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3fcc843b187fe769cd3f2c03c35529dcf2f0427791029382ce6b50572b9ff30b
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  accessed_at: '2026-10-28T18:55:43.326276Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi53542.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.818404Z'
  support: context_only
  summary: Complete generated target.
  snapshot_sha256: bb642c6b50f745a57c76b3c53960805676a3be275c27edee7cc07bf4dd776b4b
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.818599Z'
  support: context_only
  summary: Complete exact maintained owner.
  snapshot_sha256: 6743c3d96724ec5d445a4a5892430cd042362f05b728f87f6bb13a6ce084404d
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.818633Z'
  support: context_only
  summary: Exact packaged current identifier/ontology_id and preferred-term rows.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.818958Z'
  support: context_only
  summary: Exact packaged snapshot version and checksum.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full formulation comparison
  accessed_at: '2026-10-28T19:10:20.818987Z'
  support: context_only
  summary: Current scientific-field equality includes quantities, stocks and notes;
    no chemical equivalence is inferred.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: RecipeMerger.merge_group
  accessed_at: '2026-10-28T19:10:20.819010Z'
  support: context_only
  summary: Current merge_group copies singletons and rejects incompatible multiple
    formulations. Generated staleness is not evidence that current code permits ingredient-only
    merging.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.819035Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: e0f8d2045a0d6cfba1f465b321f8d790873408e9bef9f27634148807e947b2bc
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.819060Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: b0944636d00d087f3a15925840bfa0120cd679ecaf2abe3dab0cd22b0a23e536
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.819085Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: aed4537cd3d21b9b56aece1d1d80fd7a8e3848bc76c8ca8c15b68b40f8dd55a2
- evidence_id: owner-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
  locator: Complete file
  accessed_at: '2026-10-28T19:10:20.819106Z'
  support: context_only
  summary: Complete exact additional maintained owner.
  snapshot_sha256: b764d20ca2e90b2825caadf29f623e7ae723d05c2a2cabdfd33fa6009ffa14e6
- evidence_id: report-20
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:10:20.819133Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 6a16e01139a26de5a1ee6b415e8d306249c59c299ac34ade8648b23ce278bfd4
- evidence_id: report-21
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/desulfobulbus_sp_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.824591Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 9e5aff8155ec3e53a238b3c5d17d60b4a866459707e36a9f720df820dfa16aff
- evidence_id: report-22
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_11383.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.824646Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 7b39389cf89e2fb22e0fa2ffaf7ea0d7275900feed2d31e0e6d134f08b92650f
- evidence_id: report-23
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_13871.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.824681Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: e07070efbf61595a9864f039a6ebeeb36344d11b516e40cdacf3dd0fedb13ce3
- evidence_id: report-24
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0500-1000/records/bacterial/medium_196_modified_for_dsm_9700.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.824714Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 214ff3541e51c11ba6011582ef61453102d83df60412afc901a0675ba77f3147
- evidence_id: report-25
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json
  locator: Exact selected row locators in historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:10:20.824746Z'
  support: context_only
  summary: Historical repository parent; only exact selected record objects are joined.
    Decoded data is not itself original external raw evidence.
  snapshot_sha256: 1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c
- evidence_id: report-26
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/desulfocapsa_sulfexigens_medium.yaml.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830560Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 9abfc8fe128a7296998d220459f710b52afdfa60f3d48ab3ca252a1ced117d28
- evidence_id: report-27
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830623Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: a10db3063a5342864395cc3f56335635043e57b224d60975b4d21af9dbf79ca5
- evidence_id: report-28
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfobulbus_sp_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830653Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 10d6a2aad1030f0e9220f96e66183a9ba9362361e921fc414c38200755414404
- evidence_id: report-29
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830677Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 304f3e0d616cfd58a2f57e8cd963ffcd9121064aaf14ecfc77be7e620adc1b66
- evidence_id: report-30
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830700Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 886a3e730062c30a5d2d9c16161d47bbd4944660e3ea59d13e46ca924ee72566
- evidence_id: report-31
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830724Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 212eb51d4582af0aae3c43bbbdf80a4291403e09abee1260acf526bc52635932
- evidence_id: report-32
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.md
  locator: Complete report
  accessed_at: '2026-10-28T19:10:20.830747Z'
  support: context_only
  summary: Prior exact-header assessment; old source/check claims are not newly executed.
  snapshot_sha256: 89f013d4b9381d8dc1287881f4ddc40c3e0e270ad7fdc9b19b2376dee168b9d7
- evidence_id: historical-reading
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/historical-reading.json
  accessed_at: '2026-10-28T19:10:20.830776Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Lossless exact report cells and independently joined current decoded source
    objects.
  snapshot_sha256: ca96eaa2769b67971fb82ab35307c2d54afc94559accc1e04099489bb2cf4b07
- evidence_id: historical-selected-parent-rows
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/historical-selected-parent-rows.json
  accessed_at: '2026-10-28T19:10:20.830876Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Exact selected historical parent objects; parent provenance only, not automatic
    original source authentication.
  snapshot_sha256: cc698f9c490db32f23e318a4b025105d5ced9e1c6200021e8de2896dc6b984ce
- evidence_id: complete-document-reader
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/complete-document-reader.json
  accessed_at: '2026-10-28T19:10:20.830981Z'
  locator: Complete artifact; exact original input paths and hashes retained
  support: context_only
  summary: Complete exact target and owner parsed documents with lossless long-string
    pooling.
  snapshot_sha256: aba78e1e1b5cdc950f5ddc00bfd50f26fbe5dfd7e9c5c69d6230cf705b650e8c
- evidence_id: writer-matcher
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: group_formulations
  accessed_at: '2026-10-28T19:10:20.831070Z'
  support: context_only
  summary: Current group_formulations uses conservative FormulationFingerprinter;
    ingredient similarity is only candidate discovery.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: MediaQualityFixer._merge_ingredient_group
  accessed_at: '2026-10-28T19:10:20.831133Z'
  support: context_only
  summary: Current _merge_ingredient_group keeps identical duplicate amounts and flags
    disagreements; it no longer sums duplicate quantities. It cannot establish compatible
    stock/main bases or repair a historical flattened sum.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: MediaDiveImporter._parse_api_composition; _is_api_stock_addition; _parse_api_solutions;
    _normalize_unit
  accessed_at: '2026-10-28T19:10:20.831162Z'
  support: context_only
  summary: Current _parse_api_composition reads only the first API solution, excludes
    water and recognized stock additions, and prefers explicit g_l. _parse_api_solutions
    preserves referenced stocks separately. Thus current code does not flatten all
    five API196 solutions as these records do; this does not identify the historical
    execution. Unit normalization alone does not establish final volume.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: KomodoWebImporter._convert_to_culturemech
  accessed_at: '2026-10-28T19:10:20.831194Z'
  support: context_only
  summary: Current _convert_to_culturemech uses time.strftime with a literal %f directive,
    which does not provide microseconds here. Existing malformed history is retained
    as provenance; current behavior is not independent proof of past execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: DSMZCompositionResolver.extract_dsmz_id; merge_composition; _add_enrichment_metadata
  accessed_at: '2026-10-28T19:10:20.831218Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies source composition
    into a new object; extract_dsmz_id strips alphabetic suffixes, and _add_enrichment_metadata
    emits naive datetime.now().isoformat(). Exact existing events document DSMZ196
    copying; current code is separately observed, not authenticated historical execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: chebi86254
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86254
  accessed_at: '2026-10-28T18:55:44.578463Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86254.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: b3a79ee6d9359b7b827f6f87134bc166d84d3948ec20c54965c6e706aecde3a4
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32149
  accessed_at: '2026-10-28T18:55:41.464122Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi32149.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 96b73aef765e4edc893460a376cfedd136930f253bbeac639827b1daddb65d71
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63036
  accessed_at: '2026-10-28T18:55:43.321302Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi63036.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 07dec38373731d2125348c574d0f9f2df977e458974100383d3f69c8849a84e0
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  accessed_at: '2026-10-28T18:55:40.854422Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi31206.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  accessed_at: '2026-10-28T18:55:40.160956Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi26710.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86345
  accessed_at: '2026-10-28T18:55:45.225062Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86345.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 94b600ced6e98743e2d1b02c73e1756f8f81b639407a8fdd080c96d8fa563c70
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  accessed_at: '2026-10-28T18:55:42.007602Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi32588.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  accessed_at: '2026-10-28T18:55:44.532538Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86158.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:29377
  accessed_at: '2026-10-28T18:55:40.264818Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi29377.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e0c2a85ab7be9313c564f96ee47b87e1bf3e01ad1e9fd627d1dbddced5d068c4
- evidence_id: chebi32150
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32150
  accessed_at: '2026-10-28T18:55:41.480471Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi32150.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: de317b7c2a67b08783f4123e1f5b67de75d34e2090c25525f45fe2c45f3dcbb2
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17883
  accessed_at: '2026-10-28T18:55:39.682097Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi17883.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: e5ab164ef9ff955da1a504ca34ab4d3b69539d9bf721936c9dd563ccbbd0e3b0
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86249
  accessed_at: '2026-10-28T18:55:44.578308Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86249.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 4d7f48f88badcba85a62e59842c6ec921f5478eb76695098b17847ed62c8530a
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49976
  accessed_at: '2026-10-28T18:55:43.254967Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi49976.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: d3bdc4c6f01d01422fafe433df4e4011e01cf7e55e0329ab341a60ece780946f
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86368
  accessed_at: '2026-10-28T18:55:45.221456Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86368.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 2d5685a4a03c5d730876514b4a7664fb477f63682a60cc7e13d7776a250f68e3
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  accessed_at: '2026-10-28T18:55:42.067236Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi33118.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53503
  accessed_at: '2026-10-28T18:55:43.327411Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi53503.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: a626d2aa210aafd9572221d4893cd206310d5df507e474e1528997048f522250
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86318
  accessed_at: '2026-10-28T18:55:45.229921Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi86318.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: bd88e1499f370a9f474b29fa7a9a83aa5c42c69d0b6772ece8c89d646dfda8d8
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:34887
  accessed_at: '2026-10-28T18:55:42.629892Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi34887.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: 3a37ef35991d24faf578286a7d7557ee1b0646c286dd3f8a555d833e6bf82a57
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  accessed_at: '2026-10-28T18:55:43.920444Z'
  locator: REVIEW_WORK/batch075/source01-03-supplement/chebi75213.json; exact original
    raw/text/hash/time metadata
  support: context_only
  summary: Fresh batch075 capture. Fresh exact scoped primary/provider/ontology evidence
    after ordinary identity preflight; no variant transfer or growth inference.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/quantity-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.038738Z'
  support: supports
  summary: Complete source-stage quantity decisions.
  snapshot_sha256: accef09cf1db842ef4a239415eea656315901c2dc1c8d89b392a8294066b658a
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/grounding-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.038834Z'
  support: supports
  summary: Exact slots, raw OLS scientific objects and current MIM rows.
  snapshot_sha256: 9132d38ee9f3a5bd53bddcb3d0a8175e21ed28d7095b6a94c8cd3d0b7b7c5e2c
- evidence_id: census
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.038979Z'
  support: supports
  summary: Complete scalar census with explicit dependency exclusions.
  snapshot_sha256: fdc8dd930affcd06a072f758997ca1535dbcd8b4326cabb3d8db6e97087f0a6e
- evidence_id: numeric-census
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/numeric-field-census.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.039077Z'
  support: supports
  summary: Numeric/text assertions and quantity joins.
  snapshot_sha256: 6ec07aeaee9c9dde847eb2b96c902eab1113ceb772f6780a58637f3b73bd9455
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/history-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.039165Z'
  support: supports
  summary: Current exact histories, without replay.
  snapshot_sha256: 282b87d44246006d2835e4d7313a41715209feb28d88b1ecf240ad5a3f46d0a0
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/history-report-inventory.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.039192Z'
  support: supports
  summary: Exact historical report scopes.
  snapshot_sha256: 103952cea18991e62cbfab3fd9c9105b6d601397a9ecb0470c9c11e232294e7e
- evidence_id: old-claims
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/existing-claim-authentication.json
  locator: Complete sidecar
  accessed_at: '2026-10-28T19:10:21.039217Z'
  support: context_only
  summary: No attached claims to authenticate; historical source objects are separately
    assessed in historical-source-joins.json.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: historical-source-joins
  kind: record_content
  reference: REVIEW_WORK/batch075/record02/historical-source-joins.json
  locator: Every literal/decoded historical source-object row and exact current-source
    match
  accessed_at: '2026-10-28T19:10:21.039235Z'
  support: context_only
  summary: Historical quoted source content and raw-digest equality where actually
    matched; independent of attached local claims and original access-event recovery.
  snapshot_sha256: 6f45ab13b1ddbcb5c6edf4cd3c7ffc5bd568c766a8749507a5a64374a96b3168
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch075/record02/validate-schema.json
  accessed_at: '2026-10-28T18:55:10.413246Z'
  support: supports
  summary: Original once-only canonical schema with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: 11bbd1b2b7d2597c2d9abef39b4915760d68d996de1721507b5a340fbb80da37
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch075/record02/validate-strict.json
  accessed_at: '2026-10-28T18:55:11.475635Z'
  support: supports
  summary: Original once-only canonical strict with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: a8faa9baaf82c79ffbdde8a26191becf667090ce5a238dd6e8ae05bf1ac9ca3d
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch075/record02/validate-terms.json
  accessed_at: '2026-10-28T18:55:12.672529Z'
  support: supports
  summary: Original once-only canonical terms with complete argv/time/streams; reference
    count zero does not verify sources.
  snapshot_sha256: e63698f32ce9c7614495695ec511c8dc8428301299c934fbbef3da4dcf683113
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch075/record02/validate-references.json
  accessed_at: '2026-10-28T18:55:13.519662Z'
  support: supports
  summary: Original once-only canonical references with complete argv/time/streams;
    reference count zero does not verify sources.
  snapshot_sha256: b9d307a8a783588e636637202da6bc8ce27dd186cdd7142f75e8fc15fc985ed5
assessments:
- assessment_id: identity
  area: identity
  topic: Base and modified source scope
  outcome: concern
  summary: The DSM196 base is available in full primary and provider sources, but
    three strain-modified KOMODO formulations remain unavailable. Their copied equality
    is not proof of identity. Five exact maintained contributors and the generated
    record were read in full.
  target_ids:
  - CultureMech:001295
  evidence_ids:
  - target
  - owner
  - dsmz196
  - api196
  - komodo196_11383
  - komodo196_13871
  - komodo196_9700
- assessment_id: representation
  area: representation
  topic: Retained classification and preparation
  outcome: supported
  summary: DEFINED/DEFINED and LIQUID agree with the known base formulation. Current
    pH7.2 and the two main preparation notes are supported for DSM196; the third text
    is supported only as SL-10 preparation. No source temperature or strain growth
    claim is invented.
  target_ids:
  - CultureMech:001295
  evidence_ids:
  - target
  - dsmz196
  - quantities
- assessment_id: quantities
  area: quantity
  topic: Complete amounts, units and preparation stages
  outcome: concern
  summary: 114 current concentration fields are covered by 30 decisions, including
    unchanged support and explicit source-only conditions.
  target_ids:
  - CultureMech:001295
  evidence_ids:
  - quantities
  - numeric-census
  details: '{"schema":"fresh-b075-quantity-inventory-v1","target":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","quantity_field_count":114,"decisions":[{"quantity_id":"q1","label":"FeCl3
    x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[0].concentration","stored":{"value":"2.80957","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"FeCl3 x 6 H2O\",\n                        \"compound_id\":
    82,\n                        \"amount\": 2.7,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.80957,\n                        \"mmol_l\":
    10.3944,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 21-21","quote":"FeCl3 x 6 H2O                                           2.70        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[0].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[0].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q2","label":"Na2SO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[1].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.12175,\n                        \"mmol_l\":
    21.978,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 22-22","quote":"Na2SO4                                                  3.00        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[1].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[1].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q3","label":"KH2PO4","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[2].concentration","stored":{"value":"0.208117","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.208117,\n                        \"mmol_l\":
    1.52931,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 23-23","quote":"KH2PO4                                                  0.20        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[2].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[2].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q4","label":"NH4Cl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[3].concentration","stored":{"value":"0.312175","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.312175,\n                        \"mmol_l\":
    5.83613,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 24-24","quote":"NH4Cl                                                   0.30        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[3].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[3].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q5","label":"NaCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[4].concentration","stored":{"value":"21.8522","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 21,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 21.8522,\n                        \"mmol_l\":
    373.926,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 25-25","quote":"NaCl                                                   21.00        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[4].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[4].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q6","label":"MgCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[5].concentration","stored":{"value":"3.12175","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 3.12175,\n                        \"mmol_l\":
    15.3552,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 26-26","quote":"MgCl2 x 6 H2O                                           3.00        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[5].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[5].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q7","label":"KCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[6].concentration","stored":{"value":"0.520291","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.520291,\n                        \"mmol_l\":
    6.97909,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 27-27","quote":"KCl                                                     0.50        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[6].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[6].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q8","label":"CaCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[7].concentration","stored":{"value":"0.156087","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    A, provider-declared 961 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.156087,\n                        \"mmol_l\":
    1.06171,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 28-28","quote":"CaCl2 x 2 H2O                                           0.15        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[7].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[7].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q9","label":"Na2CO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[8].concentration","stored":{"value":"50","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    B, provider-declared 30 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[2].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\":
    32,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 50,\n                        \"mmol_l\":
    471.752,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 35-35","quote":"Na2CO3                                                  1.50        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[8].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[8].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q10","label":"Na2S2O3 x 5 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[9].concentration","stored":{"value":"250","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"Solution
    C, provider-declared 10 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[3].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2S2O3 x 5 H2O\",\n                        \"compound_id\":
    65,\n                        \"amount\": 2.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 250,\n                        \"mmol_l\":
    1007.31,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 41-41","quote":"Na2S2O3 x 5 H2O                                         2.50        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[9].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[9].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q11","label":"HCl","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[10].concentration","stored":{"value":"2.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated
    mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium
    dose. Preserve reagent volume/strength and the explicit final stock makeup, then
    separate stock from receiving medium. Modified-strain applicability remains unsupported.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\":
    68,\n                        \"attribute\": \"25%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\":
    0\n                    }","quote_basis":"raw UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 47-47","quote":"HCl (25%)                                              10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated
    mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium
    dose. Preserve reagent volume/strength and the explicit final stock makeup, then
    separate stock from receiving medium. Modified-strain applicability remains unsupported."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated
    mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium
    dose. Preserve reagent volume/strength and the explicit final stock makeup, then
    separate stock from receiving medium. Modified-strain applicability remains unsupported."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[10].concentration","decision":"correct","rationale":"The
    primary specifies 10 ml of 25% HCl in SL-10; the bare percentage has no stated
    mass/volume basis. Do not endorse provider 2.5 g_l as a conversion or main-medium
    dose. Preserve reagent volume/strength and the explicit final stock makeup, then
    separate stock from receiving medium. Modified-strain applicability remains unsupported."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[10].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q12","label":"FeCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[11].concentration","stored":{"value":"1.5","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 48-48","quote":"FeCl2 x 4 H2O                                           1.50        g","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[11].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[11].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q13","label":"ZnCl2","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[12].concentration","stored":{"value":"0.07","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[2]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 58-58","quote":"ZnCl2                                                      70.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[12].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[12].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q14","label":"MnCl2 x 4 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[13].concentration","stored":{"value":"0.1","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[3]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 59-59","quote":"MnCl2 x 4 H2O                                             100.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[13].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[13].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q15","label":"H3BO3","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[14].concentration","stored":{"value":"0.006","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[4]","quote":"{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 60-60","quote":"H3BO3                                                       6.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[14].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[14].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q16","label":"CoCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[15].concentration","stored":{"value":"0.19","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[5]","quote":"{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 61-61","quote":"CoCl2 x 6 H2O                                             190.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[15].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[15].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q17","label":"CuCl2 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[16].concentration","stored":{"value":"0.002","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[6]","quote":"{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 62-62","quote":"CuCl2 x 2 H2O                                               2.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[16].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[16].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q18","label":"NiCl2 x 6 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[17].concentration","stored":{"value":"0.024","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[7]","quote":"{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 63-63","quote":"NiCl2 x 6 H2O                                              24.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[17].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[17].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q19","label":"Na2MoO4 x 2 H2O","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[18].concentration","stored":{"value":"0.036","unit":"G_PER_L"}}],"decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations.","source_stage":"SL-10
    stock, explicit final 1000 ml","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 64-64","quote":"Na2MoO4 x 2 H2O                                            36.00      mg","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ingredients[18].concentration","decision":"correct","rationale":"The
    stored rate matches explicit provider g_l for this named solution, but its current
    unqualified main-medium placement is wrong. Preserve the primary batch mass and
    the separately stated solution receiving dose; the main 961+30+10 ml table is
    not an independent measured final-volume statement. The three modified-strain
    owners remain unsupported against their unavailable exact formulations."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ingredients[18].concentration","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q20","label":"Solution A receiving volume","local_fields":[],"decision":"evidence_only","rationale":"Missing
    source-only structural control for the exact DSM196 base recipe. Preserve the
    stated volume at this named stage; input water is not final makeup, and this source
    does not verify the three modified-strain formulations.","source_stage":"DSM196
    exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].recipe[0]","quote":"{\n                        \"recipe_order\":
    1,\n                        \"solution\": \"Solution A\",\n                        \"solution_id\":
    403,\n                        \"amount\": 961,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 3-3","quote":"Solution A                                            961.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q21","label":"Solution B receiving
    volume","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only
    structural control for the exact DSM196 base recipe. Preserve the stated volume
    at this named stage; input water is not final makeup, and this source does not
    verify the three modified-strain formulations.","source_stage":"DSM196 exact named
    solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].recipe[1]","quote":"{\n                        \"recipe_order\":
    3,\n                        \"solution\": \"Solution B\",\n                        \"solution_id\":
    405,\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 4-4","quote":"Solution B                                             30.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q22","label":"Solution C receiving
    volume","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only
    structural control for the exact DSM196 base recipe. Preserve the stated volume
    at this named stage; input water is not final makeup, and this source does not
    verify the three modified-strain formulations.","source_stage":"DSM196 exact named
    solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].recipe[2]","quote":"{\n                        \"recipe_order\":
    4,\n                        \"solution\": \"Solution C\",\n                        \"solution_id\":
    406,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 5-5","quote":"Solution C                                             10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q23","label":"SL-10 receiving
    dose in A","local_fields":[],"decision":"evidence_only","rationale":"Missing source-only
    structural control for the exact DSM196 base recipe. Preserve the stated volume
    at this named stage; input water is not final makeup, and this source does not
    verify the three modified-strain formulations.","source_stage":"DSM196 exact named
    solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[8]","quote":"{\n                        \"recipe_order\":
    9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\":
    595,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 29-29","quote":"Trace element solution SL-10                            1.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q24","label":"A water input","local_fields":[],"decision":"evidence_only","rationale":"Missing
    source-only structural control for the exact DSM196 base recipe. Preserve the
    stated volume at this named stage; input water is not final makeup, and this source
    does not verify the three modified-strain formulations.","source_stage":"DSM196
    exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[1].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 960,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 30-30","quote":"Distilled water                                       960.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q25","label":"B water input","local_fields":[],"decision":"evidence_only","rationale":"Missing
    source-only structural control for the exact DSM196 base recipe. Preserve the
    stated volume at this named stage; input water is not final makeup, and this source
    does not verify the three modified-strain formulations.","source_stage":"DSM196
    exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[2].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 30,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 36-36","quote":"Distilled water                                        30.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q26","label":"C water input","local_fields":[],"decision":"evidence_only","rationale":"Missing
    source-only structural control for the exact DSM196 base recipe. Preserve the
    stated volume at this named stage; input water is not final makeup, and this source
    does not verify the three modified-strain formulations.","source_stage":"DSM196
    exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[3].recipe[1]","quote":"{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 42-42","quote":"Distilled water                                        10.00       ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q27","label":"SL-10 water input","local_fields":[],"decision":"evidence_only","rationale":"Missing
    source-only structural control for the exact DSM196 base recipe. Preserve the
    stated volume at this named stage; input water is not final makeup, and this source
    does not verify the three modified-strain formulations.","source_stage":"DSM196
    exact named solution","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].recipe[9]","quote":"{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 990,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 65-65","quote":"Distilled water                                           990.00      ml","quote_basis":"derivative
    text"}],"layer_assessments":[]},{"quantity_id":"q28","label":"Retained main preparation
    and final pH","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"First
    dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0 with
    1 N NaOH (about 3 ml). Add and dissolve remaining salts of solution A and sparge
    medium with 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute
    under same gas atmosphere in anoxic Hungate-type tubes or serum vials and autoclave.
    Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution
    C is autoclaved separately under 100% N2 gas atmosphere. To complete the medium
    appropriate amounts of solutions B and C are added to the sterile solution A in
    the sequence as indicated. Final pH of the medium should be adjusted to 7.2."}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[0]","stored":{"step_number":1,"action":"AUTOCLAVE","description":"First
    dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0 with
    1 N NaOH (about 3 ml). Add and dissolve remaining salts of solution A and sparge
    medium with 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute
    under same gas atmosphere in anoxic Hungate-type tubes or serum vials and autoclave.
    Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution
    C is autoclaved separately under 100% N2 gas atmosphere. To complete the medium
    appropriate amounts of solutions B and C are added to the sterile solution A in
    the sequence as indicated. Final pH of the medium should be adjusted to 7.2."}},{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ph_value","stored":7.2},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ph_value","stored":7.2}],"decision":"evidence_only","rationale":"The
    retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt,
    pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C
    atmospheres and ordered addition. Existing support needs linkage; modified-strain
    transfer remains unverified.","source_stage":"DSM196 main preparation","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve 2.7 g FeCl3 x 6 H2O in distilled water and adjust the pH to 7.0
    with 1 N NaOH (about 3 ml). Add and dissolve remaining salts of solution A and
    sparge medium with 80% N2 and 20% CO2 gas mixture for at least 30 min, then distribute
    under same gas atmosphere in anoxic Hungate-type tubes or serum vials and autoclave.
    Solution B is autoclaved separately under 80% N2 and 20% CO2 gas atmosphere. Solution
    C is autoclaved separately under 100% N2 gas atmosphere. To complete the medium
    appropriate amounts of solutions B and C are added to the sterile solution A in
    the sequence as indicated. Final pH of the medium should be adjusted to 7.2.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 7-14","quote":"1. First dissolve 2.7 g FeCl3 x 6 H2O in distilled water
    and adjust the pH to 7.0 with 1 N\nNaOH (about 3 ml). Add and dissolve remaining
    salts of solution A and sparge medium\nwith 80% N2 and 20% CO2 gas mixture for
    at least 30 min, then distribute under same gas\natmosphere in anoxic Hungate-type
    tubes or serum vials and autoclave. Solution B is\nautoclaved separately under
    80% N2 and 20% CO2 gas atmosphere. Solution C is\nautoclaved separately under
    100% N2 gas atmosphere. To complete the medium\nappropriate amounts of solutions
    B and C are added to the sterile solution A in the\nsequence as indicated. Final
    pH of the medium should be adjusted to 7.2.","quote_basis":"derivative text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt,
    pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C
    atmospheres and ordered addition. Existing support needs linkage; modified-strain
    transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[0]","decision":"evidence_only","rationale":"The
    retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt,
    pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C
    atmospheres and ordered addition. Existing support needs linkage; modified-strain
    transfer remains unverified."},{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt,
    pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C
    atmospheres and ordered addition. Existing support needs linkage; modified-strain
    transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt,
    pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C
    atmospheres and ordered addition. Existing support needs linkage; modified-strain
    transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"ph_value","decision":"evidence_only","rationale":"The
    retained paragraph and pH7.2 match DSM196, including initial2.7g ferric salt,
    pH7.0 with1N NaOH about3ml,80/20 gas and at least30min sparging, distinct B/C
    atmospheres and ordered addition. Existing support needs linkage; modified-strain
    transfer remains unverified."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml","field_path":"ph_value","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml","field_path":"ph_value","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."},{"path":"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml","field_path":"ph_value","decision":"unsupported","rationale":"The
    stored value/text is an exact copy of the DSM196 base content, but the specific
    modified accession is unavailable. Preserve the copy as historical content; its
    applicability to this variant is not established by the base recipe or strain
    catalogue identity."}]},{"quantity_id":"q29","label":"Retained inoculum note","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"Note:
    For transfers use 5 - 10% (v/v) inoculum."}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[1]","stored":{"step_number":2,"action":"MIX","description":"Note:
    For transfers use 5 - 10% (v/v) inoculum."}}],"decision":"evidence_only","rationale":"The
    note faithfully preserves the primary5–10%(v/v) inoculum range. It is source context
    for the exact base recipe, not a new growth assertion or verified prescription
    for modified-strain records.","source_stage":"DSM196 transfer note","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[0].steps[1]","quote":"{\n                        \"step\":
    \"Note: For transfers use 5 - 10% (v/v) inoculum.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 15-15","quote":"2. Note: For transfers use 5 - 10% (v/v) inoculum.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[1]","decision":"evidence_only","rationale":"The
    note faithfully preserves the primary5–10%(v/v) inoculum range. It is source context
    for the exact base recipe, not a new growth assertion or verified prescription
    for modified-strain records."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[1]","decision":"evidence_only","rationale":"The
    note faithfully preserves the primary5–10%(v/v) inoculum range. It is source context
    for the exact base recipe, not a new growth assertion or verified prescription
    for modified-strain records."}]},{"quantity_id":"q30","label":"Retained SL-10
    makeup step","local_fields":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[2]","stored":{"step_number":3,"action":"DISSOLVE","description":"First
    dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts.
    Finally make up to 1000.00 ml."}}],"decision":"correct","rationale":"The text
    and explicit1000ml final stock makeup are supported, but this is SL-10 preparation
    and is currently an unqualified main-medium step. Preserve the wording and place
    it under SL-10; do not treat it as main final volume.","source_stage":"SL-10 stock
    preparation","sources":[{"evidence_id":"api196","reference":"https://mediadive.dsmz.de/rest/medium/196","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/api196.bin","raw_sha256":"855efb5893b3717f50664f314cf40be39abb4d057d81e5a2ce81bb0daa17b094","text_sha256":"d30a29ff77393af983418b3f5cc974287879e8206bde1a36ff988d03b6e2ca26","accessed_at":"2026-10-28T18:55:35.882016Z","locator":"data.solutions[4].steps[0]","quote":"{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }","quote_basis":"raw
    UTF-8"},{"evidence_id":"dsmz196","reference":"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium196.pdf","raw_path":"REVIEW_WORK/batch075/source01-03-supplement/dsmz196.bin","raw_sha256":"a440cdca0aa8e256c6d1d7fefb4986d331e16d534c1343a850b54998ee11812f","text_sha256":"ca639fde629b944d7c37edb2bfd397cc7524ec945fec6afd0bf2b549da138675","accessed_at":"2026-10-28T18:55:36.172246Z","locator":"dsmz196.txt
    lines 67-68","quote":"First dissolve FeCl2 in the HCl, then dilute in water, add
    and dissolve the other salts. Finally\nmake up to 1000.00 ml.","quote_basis":"derivative
    text"}],"layer_assessments":[{"path":"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"The
    text and explicit1000ml final stock makeup are supported, but this is SL-10 preparation
    and is currently an unqualified main-medium step. Preserve the wording and place
    it under SL-10; do not treat it as main final volume."},{"path":"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml","field_path":"preparation_steps[2]","decision":"correct","rationale":"The
    text and explicit1000ml final stock makeup are supported, but this is SL-10 preparation
    and is currently an unqualified main-medium step. Preserve the wording and place
    it under SL-10; do not treat it as main final volume."}]}],"document_scopes":{"data/merge_yaml/merged/DESULFOCAPSA_SULFEXIGENS_MEDIUM.yaml":null,"data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml":null,"data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml":null,"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml":null,"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml":null,"data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml":null},"scope":"Every
    selected target/owner concentration plus explicit dependency fields; source-only
    rows/conditions and unchanged claims distinguished. Excluded parent quantities
    are not transferred."}'
- assessment_id: grounding
  area: grounding
  topic: Supplied forms and current ontology/MIM scope
  outcome: concern
  summary: All selected primary and secondary chemical slots were compared with current
    OLS scientific objects and exact packaged MIM rows. Nickel34887 is anhydrous despite
    explicit hexahydrate naming;53542 supports the source form. Current cobalt53503
    is already hexahydrate and should be retained. The preferred NiCl2 x 6 H2O and
    CoCl2 x 6 H2O MIM rows are REJECTED, while a separate preferred Nickel (II) chloride
    hexahydrate row is MAPPED. Other exact hydrates and neutral HCl/boric acid assertions
    agree with their source names; this does not certify an unavailable variant.
  target_ids:
  - CultureMech:001295
  evidence_ids:
  - groundings
  - mim
  - mim-meta
- assessment_id: history
  area: provenance
  topic: Existing repair credit and writer limits
  outcome: concern
  summary: All eleven scoped report bodies and five selected parent rows were read.
    October5 zero-source-check triage is not scientific validation. October7 source-table
    claims authenticate current raw content where exact objects/digests match, not
    the original retrieval event. Existing resolver histories document DSM196 copying
    without proving strain modifications. Current parser, conservative grouping and
    timestamp writers are separately observed; malformed/naive original events remain
    append-only provenance.
  target_ids:
  - CultureMech:001295
  evidence_ids:
  - history
  - old-reports
  - old-claims
  - writer-formulation
  - writer-merger
  - historical-source-joins
  - historical-selected-parent-rows
  - writer-komodo
  - writer-resolver
  - writer-mediadive
  - writer-matcher
findings:
- finding_id: f1
  issue_key: culturemech-001295-solution-stage
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Restore separate A, B, C and SL-10 stages
  description: 'Nineteen direct ingredients flatten four distinct source solutions:
    eight A rates, B carbonate, C thiosulfate and nine SL-10 entries. Preserve their
    supported source amounts, rebuild exact solution topology and receiving doses,
    and move the supported1000ml makeup step under SL-10. Do not turn bare25% HCl
    into a mass dose or the961+30+10ml table into a measured final volume. Restrict
    this reconstruction to the supported DSM196 base while variant identity remains
    unresolved.'
  target_ids:
  - CultureMech:001295
  field_paths:
  - ingredients[0].concentration
  - ingredients[1].concentration
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[8].concentration
  - ingredients[9].concentration
  - ingredients[10].concentration
  - ingredients[11].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - solutions
  - preparation_steps[2]
  evidence_ids:
  - quantities
  - dsmz196
  - api196
  - writer-mediadive
  rule_id: culturemech-scientific-review/solution-stage
  native_severity: P2
  normalization_reason: Custom source-stage, dimensional or supplied-form requirement
    normalized to major because it changes the scientific interpretation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-001295-variant-identity
  category: identity
  severity: major
  status: open
  certainty: provisional
  title: Reconcile base and modified-strain identities before co-merging
  description: The generated record lumps DSM196, KOMODO196 and three explicitly modified
    accessions196_11383/196_13871/196_9700. Exact current KOMODO routes and catalogue
    returned403; equal copied values and old resolver events do not establish equivalence.
    Current DSM catalogue identities distinguish the three environmental strains,
    but those metadata pages do not recover the modifications. Preserve all accessions
    and histories; resolve exact variants before adopting synonym/duplicate relationships
    or propagating base corrections. The four KOMODO owners also lack the retained
    DSM preparation steps. Current conservative merger includes preparation and relationship
    fields and does not certify this old ingredient-based merge.
  target_ids:
  - CultureMech:001295
  field_paths:
  - synonyms
  - merged_from
  - parent_media
  - variant_relationship
  - variant_modifications
  evidence_ids:
  - target
  - owner
  - komodo196
  - komodo196_11383
  - komodo196_13871
  - komodo196_9700
  - komodoList
  - identityDSM11383
  - identityDSM13871
  - identityDSM9700
  - writer-formulation
  - writer-matcher
  - writer-resolver
  rule_id: culturemech-scientific-review/variant-identity
  native_severity: P2
  normalization_reason: Custom source-identity requirement normalized to major because
    unverified strain variants were represented as interchangeable synonyms and may
    receive inappropriate base-formulation changes.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-001295-nickel-hydrate
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Correct both nickel hydrate assertions
  description: Both primary and secondary CHEBI:34887 slots describe anhydrous nickel
    dichloride despite explicit NiCl2·6H2O in the selected name and base primary source.
    Verify CHEBI:53542 and exact supplied form while preserving source stock amount
    and unresolved variant applicability. MIM has a MAPPED preferred Nickel (II) chloride
    hexahydrate row and a distinct REJECTED NiCl2 x 6 H2O row; these spelling-specific
    statuses are not interchangeable.
  target_ids:
  - CultureMech:001295
  field_paths:
  - ingredients[17].term
  - ingredients[17].mediaingredientmech_chebi_term
  evidence_ids:
  - dsmz196
  - chebi53542
  - groundings
  rule_id: culturemech-scientific-review/nickel-hydrate
  native_severity: P2
  normalization_reason: Custom source-stage, dimensional or supplied-form requirement
    normalized to major because it changes the scientific interpretation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-001295-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Link retained supported content to exact source stages
  description: No selected ingredient or preparation claim is attached. Add ingredient
    evidence at ingredients[i].evidence and stage/preparation evidence at root evidence
    with precise field and solution locators, retaining the supported main paragraph,
    inoculum note, pH and SL-10 makeup. Historical quoted source objects are separate
    from attached evidence and do not verify modified-strain recipes.
  target_ids:
  - CultureMech:001295
  field_paths:
  - ingredients[*].evidence
  - evidence
  evidence_ids:
  - quantities
  - old-claims
  - historical-source-joins
  - dsmz196
  rule_id: culturemech-scientific-review/claim-evidence
  native_severity: P3
  normalization_reason: Custom evidence/completeness or unresolved-specificity requirement
    normalized to minor because supported recipe content is retained and no numerical
    replacement is asserted.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-001295-event-metadata
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve original history and correct future event metadata
  description: The four KOMODO owners retain malformed literal .fZ import timestamps
    and timezone-naive resolver timestamps. Preserve those original events byte-for-byte;
    append verified context only if authoritative provenance is recovered. Correct
    the current importer/resolver writers for future timezone-aware UTC events; do
    not invent historical times or rewrite old strings.
  target_ids:
  - CultureMech:001295
  field_paths:
  - data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml::curation_history[1].timestamp
  evidence_ids:
  - history
  - writer-komodo
  - writer-resolver
  rule_id: culturemech-scientific-review/event-metadata
  native_severity: P3
  normalization_reason: Custom event-metadata requirement normalized to minor; preserve
    existing scientific content and original events while correcting future writer
    output.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current future-event timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current future-event timestamp writer
actions:
- action_id: a1
  description: 'Nineteen direct ingredients flatten four distinct source solutions:
    eight A rates, B carbonate, C thiosulfate and nine SL-10 entries. Preserve their
    supported source amounts, rebuild exact solution topology and receiving doses,
    and move the supported1000ml makeup step under SL-10. Do not turn bare25% HCl
    into a mass dose or the961+30+10ml table into a measured final volume. Restrict
    this reconstruction to the supported DSM196 base while variant identity remains
    unresolved.'
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001295
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a2
  description: The generated record lumps DSM196, KOMODO196 and three explicitly modified
    accessions196_11383/196_13871/196_9700. Exact current KOMODO routes and catalogue
    returned403; equal copied values and old resolver events do not establish equivalence.
    Current DSM catalogue identities distinguish the three environmental strains,
    but those metadata pages do not recover the modifications. Preserve all accessions
    and histories; resolve exact variants before adopting synonym/duplicate relationships
    or propagating base corrections. The four KOMODO owners also lack the retained
    DSM preparation steps. Current conservative merger includes preparation and relationship
    fields and does not certify this old ingredient-based merge.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001295
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a3
  description: Both primary and secondary CHEBI:34887 slots describe anhydrous nickel
    dichloride despite explicit NiCl2·6H2O in the selected name and base primary source.
    Verify CHEBI:53542 and exact supplied form while preserving source stock amount
    and unresolved variant applicability. MIM has a MAPPED preferred Nickel (II) chloride
    hexahydrate row and a distinct REJECTED NiCl2 x 6 H2O row; these spelling-specific
    statuses are not interchangeable.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:001295
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
  acceptance_checks:
  - Curate only named maintained fields after exact source-stage reconciliation; retain
    prior history and append a new actual curation event.
  - Attach literal source evidence; preserve uncertainty about final volume, unspecified
    hydrates and percent basis. Recheck all affected quantities and ontology assertions.
  - Regenerate the selected target using current conservative merge workflow, check
    freshness and rerun schema, strict, terms and reference diagnostics.
  generator: Maintained-input curation and repository merge regeneration
- action_id: a4
  description: No selected ingredient or preparation claim is attached. Add ingredient
    evidence at ingredients[i].evidence and stage/preparation evidence at root evidence
    with precise field and solution locators, retaining the supported main paragraph,
    inoculum note, pH and SL-10 makeup. Historical quoted source objects are separate
    from attached evidence and do not verify modified-strain recipes.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:001295
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
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
  description: The four KOMODO owners retain malformed literal .fZ import timestamps
    and timezone-naive resolver timestamps. Preserve those original events byte-for-byte;
    append verified context only if authoritative provenance is recovered. Correct
    the current importer/resolver writers for future timezone-aware UTC events; do
    not invent historical times or rewrite old strings.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:001295
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfobulbus_sp_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfocapsa_sulfexigens_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_11383.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_13871.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_196_modified_for_dsm_9700.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/komodo_web_importer.py
    role: current future-event timestamp writer
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/enrich/dsmz_resolver.py
    role: current future-event timestamp writer
  acceptance_checks:
  - Original historical events remain byte-identical; any verified correction/context
    is appended as a new event with its source.
  - Both named current writers emit real timezone-aware UTC timestamps without a literal
    %f/.fZ or naive local time; validate a representative future event without rewriting
    existing records.
  generator: Maintained-input curation and repository merge regeneration
limitations:
- 'Exact KOMODO196 and all three modified MediaInfo routes plus MediaList returned403.
  Review is partial: DSM196 corrections cannot automatically replace or certify any
  modified-strain formulation. Current DSM strain metadata is identity evidence only.'
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
