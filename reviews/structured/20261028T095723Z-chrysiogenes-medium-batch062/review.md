# Scientific review of chrysiogenes_medium

- Review: 20261028T095723Z-chrysiogenes-medium-batch062
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T09:29:39.326718Z
- Finished UTC: 2026-10-28T09:57:23.050558Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The base recipe and current partial stock/topology repairs are identifiable, but the generated target is stale, stock strengths remain flattened, and DSM 16346 is incorrectly represented as an unchanged base. Preserve supported provider values and correct existing nested rows while reconstructing exact stock stages, preparation and scoped evidence.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch062 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006543 | data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml | generated | chrysiogenes_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006543 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:006543 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:006543 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:006543 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Base versus DSM 16346 branch

identity: concern. Targets: CultureMech:006543.

Source 818 identity is explicit, and the current maintained child relationship correction is credited. Its statement that components are preserved conflicts with the current primary branch prescription. Generated SOURCE_DUPLICATE relationships and synonym consolidation predate that repair.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:006543.

Seven complete historical reports were read; all 138 quoted API objects equal current objects. Their blanket conflict status on every base row was overbroad: current provider nominal main values and already nested stock rows are explicitly credited here. No attached formulation claims exist in the selected documents. All historical API excerpts with matching current raw digests are independently authenticated in historical-authentication.json. Matching bytes do not verify old execution or the separate KOMODO catalogue. Current MediaDive code separates stock additions but gathers all solution preparation into a root list; current conservative merging preserves scientific fields and rejects incompatible formulations. Those present behaviors do not prove how the old generated records were produced.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:006543.

All 150 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006543", "selected_concentration_field_count": 150, "selected_concentration_fields_covered": 150, "decisions": [{"decision_id": "q1", "subject": "NaCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.19641", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.19641", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.19641", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "1.19641", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.19641,\n                        \"mmol_l\": 20.4725,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 3-3", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "NaCl                                                     1.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 4.01211,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "KCl                                                      0.30        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 5.59175,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "NH4Cl                                                    0.30        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.199402", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\": 1.46527,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "KH2PO4                                                   0.20        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.299103", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\": 110,\n                        \"amount\": 0.3,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\": 2.10576,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "Na2SO4                                                   0.30        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.398804", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\": 1.96162,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "MgCl2 x 6 H2O                                            0.40        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "CaCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.149551", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.149551", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.149551", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "0.149551", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\": 1.01725,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "CaCl2 x 2 H2O                                            0.15        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Sodium resazurin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration. The source is 0.5 ml of explicit 0.1% w/v stock, giving 0.5 mg per listed batch; this is separate from neutral-resazurin grounding.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "Sodium resazurin (0.1% w/v)                              0.50       ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "NaHCO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.598205", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.598205", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.598205", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[8].concentration", "original": {"value": "0.598205", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[9]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 0.6,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.598205,\n                        \"mmol_l\": 7.1209,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "NaHCO3                                                   0.60        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "KNO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[9].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[10]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\": 191,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 4.93066,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "KNO3                                                     0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Na-acetate", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider normalization with explicit denominator limit", "interpretation": "The stored value exactly matches current API 818 g_l on its declared 1003 ml provider basis. The PDF supports the stated batch input but lists 1000 ml water plus stock additions, not a measured final volume; retain the provider basis explicitly rather than silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[13]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\": 23,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\": 6.07682,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "Na-acetate                                               0.50        g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "DSM 16346 acetate replacement", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[10].concentration", "original": {"value": "0.498504", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "strain-specific branch", "interpretation": "The current primary explicitly replaces acetate with 1.10 g/l sodium L-lactate and adds 0.80 g/l yeast extract for DSM 16346. The local variant still copies the base acetate row. This primary branch statement does not authenticate the unavailable historical KOMODO page or justify merging the branch back into its base.", "sources": [{"locator": "extracted-text lines 28-29", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346: Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10 g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q15", "subject": "ZnCl2", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q16", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q17", "subject": "H3BO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q18", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q19", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q20", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q21", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q22", "subject": "Biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q23", "subject": "Folic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q24", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.4", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The generated value is the sum of two distinct vitamin-stock strengths; their recipes and additions must remain separate. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q25", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q26", "subject": "Riboflavin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q27", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The generated value is the sum of two distinct vitamin-stock strengths; their recipes and additions must remain separate. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q28", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q29", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "original": {"value": "0.101", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The generated value is the sum of two distinct vitamin-stock strengths; their recipes and additions must remain separate. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q30", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "original": {"value": "0.13", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The generated value is the sum of two distinct vitamin-stock strengths; their recipes and additions must remain separate. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q31", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q32", "subject": "D-(+)-biotin", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q33", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q34", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q35", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q36", "subject": "ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q37", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q38", "subject": "H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q39", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q40", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q41", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q42", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q43", "subject": "Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q44", "subject": "Folic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q45", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q46", "subject": "Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q47", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q48", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q49", "subject": "D-(+)-biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q50", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q51", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q52", "subject": "ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q53", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q54", "subject": "H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q55", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q56", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q57", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q58", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q59", "subject": "Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q60", "subject": "Folic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q61", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q62", "subject": "Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q63", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q64", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q65", "subject": "D-(+)-biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q66", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q67", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q68", "subject": "ZnCl2", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q69", "subject": "MnCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q70", "subject": "H3BO3", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q71", "subject": "CoCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q72", "subject": "CuCl2 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q73", "subject": "NiCl2 x 6 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q74", "subject": "Na2MoO4 x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q75", "subject": "Biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[19].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q76", "subject": "Folic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q77", "subject": "Thiamine HCl", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[21].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q78", "subject": "Riboflavin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[22].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q79", "subject": "Calcium D-(+)-pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q80", "subject": "(DL)-alpha-Lipoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q81", "subject": "D-(+)-biotin", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q82", "subject": "Calcium pantothenate", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation": "This direct ingredient is a stock component, not a demonstrated main-medium concentration. The scalar matches a source stock value, but its direct-medium placement omits the receiving dilution. Retain supplied form and batch units, complete the proper stock, and preserve the source addition with an explicit denominator. No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q83", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q84", "subject": "Trace element solution SL-11 addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus final-litre denominator", "interpretation": "Primary and API specify 1 ml for the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis; final volume is not independently established from 1000 ml water. The target lacks these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q85", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[1].composition[0].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q86", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q87", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[1].composition[2].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q88", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[1].composition[3].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q89", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[1].composition[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q90", "subject": "Seven vitamins solution addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus final-litre denominator", "interpretation": "Primary and API specify 1 ml for the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis; final volume is not independently established from 1000 ml water. The target lacks these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q91", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[2].composition[0].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q92", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[2].composition[1].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q93", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[2].composition[2].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q94", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[2].composition[3].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q95", "subject": "Wolin's vitamin solution (10x) addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus final-litre denominator", "interpretation": "Primary and API specify 1 ml for the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis; final volume is not independently established from 1000 ml water. The target lacks these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q96", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q97", "subject": "Trace element solution SL-11 addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[0].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus final-litre denominator", "interpretation": "Primary and API specify 1 ml for the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis; final volume is not independently established from 1000 ml water. The target lacks these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q98", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[1].composition[0].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q99", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q100", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[1].composition[2].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q101", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[1].composition[3].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q102", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[1].composition[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q103", "subject": "Seven vitamins solution addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[1].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus final-litre denominator", "interpretation": "Primary and API specify 1 ml for the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis; final volume is not independently established from 1000 ml water. The target lacks these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q104", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[2].composition[0].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q105", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[2].composition[1].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q106", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[2].composition[2].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q107", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[2].composition[3].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q108", "subject": "Wolin's vitamin solution (10x) addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "solutions[2].concentration", "original": {"value": "1", "unit": "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus final-litre denominator", "interpretation": "Primary and API specify 1 ml for the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis; final volume is not independently established from 1000 ml water. The target lacks these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q109", "subject": "FeCl2 x 4 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q110", "subject": "Trace element solution SL-11 candidate addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[0].concentration_candidates", "original": [{"value": "1", "unit": "ML_PER_L", "basis": "CROSS_MEDIUM_INFERENCE", "support": "This record is a variant of medium 818 (KOMODO key '818.1'); volume read from base medium 818 ('CHRYSIOGENES MEDIUM').", "counterevidence": "The variant's own recipe was never read — only base medium 818's — so the modification may change this volume. A stock's addition volume varies by citing medium: MediaDive medium 142 adds 'Trace element solution (Vishniac &amp; Santer)' at 0.2 ml and medium 69 adds the same stock at 5 ml.", "proposed_by": "apply_cocktail_nesting.py"}]}], "decision": "evidence_only", "stage": "preserved cross-medium candidate", "interpretation": "The variant deliberately retains an unasserted candidate. Current DSM 818 explicitly identifies the DSM 16346 branch and its modifications, but the unavailable KOMODO route remains a separate identity limit. Do not automatically promote this proposed per-litre denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\": 1474,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 28-29", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346: Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10 g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q111", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[1].composition[0].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[6]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q112", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q113", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[1].composition[2].concentration", "original": {"value": "0.08", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q114", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[1].composition[3].concentration", "original": {"value": "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q115", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[1].composition[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q116", "subject": "Seven vitamins solution candidate addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[1].concentration_candidates", "original": [{"value": "1", "unit": "ML_PER_L", "basis": "CROSS_MEDIUM_INFERENCE", "support": "This record is a variant of medium 818 (KOMODO key '818.1'); volume read from base medium 818 ('CHRYSIOGENES MEDIUM').", "counterevidence": "The variant's own recipe was never read — only base medium 818's — so the modification may change this volume. A stock's addition volume varies by citing medium: MediaDive medium 142 adds 'Trace element solution (Vishniac &amp; Santer)' at 0.2 ml and medium 69 adds the same stock at 5 ml.", "proposed_by": "apply_cocktail_nesting.py"}]}], "decision": "evidence_only", "stage": "preserved cross-medium candidate", "interpretation": "The variant deliberately retains an unasserted candidate. Current DSM 818 explicitly identifies the DSM 16346 branch and its modifications, but the unavailable KOMODO route remains a separate identity limit. Do not automatically promote this proposed per-litre denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[12]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 13,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\": 1038,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 28-29", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346: Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10 g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q117", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[2].composition[0].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[5]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q118", "subject": "p-Aminobenzoic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[2].composition[1].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[8]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q119", "subject": "Pyridoxine hydrochloride", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[2].composition[2].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q120", "subject": "Vitamin B12", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[2].composition[3].concentration", "original": {"value": "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component", "interpretation": "The current nested value matches the exact stock recipe on the provider-declared 1000 ml stock basis. This existing partial repair is credited; stock membership is still incomplete. Listed vitamin-stock water alone is not independently measured final volume. The claim remains a stock value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q121", "subject": "Wolin's vitamin solution (10x) candidate addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[2].concentration_candidates", "original": [{"value": "1", "unit": "ML_PER_L", "basis": "CROSS_MEDIUM_INFERENCE", "support": "This record is a variant of medium 818 (KOMODO key '818.1'); volume read from base medium 818 ('CHRYSIOGENES MEDIUM').", "counterevidence": "The variant's own recipe was never read — only base medium 818's — so the modification may change this volume. A stock's addition volume varies by citing medium: MediaDive medium 142 adds 'Trace element solution (Vishniac &amp; Santer)' at 0.2 ml and medium 69 adds the same stock at 5 ml.", "proposed_by": "apply_cocktail_nesting.py"}]}], "decision": "evidence_only", "stage": "preserved cross-medium candidate", "interpretation": "The variant deliberately retains an unasserted candidate. Current DSM 818 explicitly identifies the DSM 16346 branch and its modifications, but the unavailable KOMODO route remains a separate identity limit. Do not automatically promote this proposed per-litre denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[11]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 28-29", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf", "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08", "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c", "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346: Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10 g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q122", "subject": "Main sol. 818 water", "local_fields": [], "decision": "evidence_only", "stage": "source-only solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe, separately from its stock additions. Only SL11 additionally has an explicit instruction to bring the stock to 1000 ml; do not promote listed water in other sections to a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[0].recipe[14]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q123", "subject": "Trace element solution SL-11 water", "local_fields": [], "decision": "evidence_only", "stage": "source-only solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe, separately from its stock additions. Only SL11 additionally has an explicit instruction to bring the stock to 1000 ml; do not promote listed water in other sections to a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[1].recipe[9]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q124", "subject": "Wolin's vitamin solution (10x) water", "local_fields": [], "decision": "evidence_only", "stage": "source-only solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe, separately from its stock additions. Only SL11 additionally has an explicit instruction to bring the stock to 1000 ml; do not promote listed water in other sections to a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[2].recipe[10]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q125", "subject": "Seven vitamins solution water", "local_fields": [], "decision": "evidence_only", "stage": "source-only solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe, separately from its stock additions. Only SL11 additionally has an explicit instruction to bring the stock to 1000 ml; do not promote listed water in other sections to a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[3].recipe[7]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q126", "subject": "Complete three stock memberships", "local_fields": [], "decision": "evidence_only", "stage": "source-only missing structure", "interpretation": "SL11 has nine compounds, Wolin ten and seven-vitamin stock seven. Current owners nest only 1/4/5 of these respectively, leaving the remainder flat; generated target has no nested stocks. Completing the stocks must move, not duplicate, all corresponding rows and preserve each stock water and receiving dose.", "sources": [{"locator": "$.data.solutions[1]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                \"id\": 1474,\n                \"name\": \"Trace element solution SL-11\",\n                \"volume\": 1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\": 676,\n                        \"amount\": 5.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\": 15.4667,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }\n                ]\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                \"id\": 5980,\n                \"name\": \"Wolin's vitamin solution (10x)\",\n                \"volume\": 1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ]\n            }", "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                \"id\": 1038,\n                \"name\": \"Seven vitamins solution\",\n                \"volume\": 1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.073779,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 80,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\": 0.583345,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\": 1359,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 1.62456,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\": 518,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.209849,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 300,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\": 1.45886,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\": 77,\n                        \"amount\": 200,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.535761,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ]\n            }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q127", "subject": "Base anoxic preparation and final pH", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path": "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients except bicarbonate, nitrate, vitamins and acetate. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, adjust pH to 7.0 - 7.4, then dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add nitrate, vitamins and acetate from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. The pH of the complete medium should be adjusted to 7.4 - 7.8, if necessary."}], "decision": "evidence_only", "stage": "main preparation versus missing copied preparation", "interpretation": "The final 7.4–7.8 range and full DSM owner prose agree with the primary. Preserve 30–45 min nitrogen treatment, pre-autoclave pH 7.0–7.4, separate nitrate/vitamin/acetate stocks, distinct bicarbonate gas and filtered vitamins. The generated and KOMODO layers omit that preparation and their Aerobic: Yes notes contradict this base prescription.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve ingredients except bicarbonate, nitrate, vitamins and acetate. Sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic, adjust pH to 7.0 - 7.4, then dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add nitrate, vitamins and acetate from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration. The pH of the complete medium should be adjusted to 7.4 - 7.8, if necessary.\"\n                    }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q128", "subject": "SL11 stock pH and solvent preparation", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml."}], "decision": "evidence_only", "stage": "stock-specific preparation", "interpretation": "Preserve EDTA in 800 ml, pH 7 using 2 N NaOH, ferrous then remaining compounds, final pH 6 and bring to 1000 ml as the SL11 stock procedure. Root-list placement must not turn this into a main-medium pH 6 instruction. The supplied compounds remain hydrated forms despite several provider mmol_l values using different molar masses.", "sources": [{"locator": "$.data.solutions[1].steps[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"step\": \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation": "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch062/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:006543.

data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml: primary 33/33, secondary 30/33; data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml: primary 27/27, secondary 24/27; data/normalized_yaml/bacterial/chrysiogenes_medium.yaml: primary 27/27, secondary 24/27; data/normalized_yaml/bacterial/for_dsm_16346.yaml: primary 27/27, secondary 24/27. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 4 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:006543.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:006543.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Partial stock repair is missing from the generated recipe

major / open / confirmed; issue key: culturemech-006543-stock-flattening-and-stale-sums.

The generated target still flattens all stock components and sums four distinct vitamin-stock pairs. Maintained owners correctly restore ten nested stock rows, but sixteen stock components remain direct ingredients and the receiving ML_PER_L basis is not independently established. Stock values must not be treated as final-medium values.

### f2: The copied DSM 16346 branch lacks its explicit modifications

major / open / confirmed; issue key: culturemech-006543-strain-branch-and-preparation-loss.

Current DSM 818 prescribes yeast extract and lactate replacement for DSM 16346; its owner retains base acetate and says components are preserved. The generated record still calls the branch a duplicate. The current repair script changes topology against a hardcoded copied signature without implementing this prescription.

### f3: Anoxic preparation and stock controls are absent from copied layers

major / open / confirmed; issue key: culturemech-006543-anoxic-preparation-and-stage-evidence.

The DSM owner retains correct main and SL11 preparation, while the target and KOMODO owners omit those instructions and carry Aerobic: Yes. SL11 pH 6 belongs to the stock, not the main medium. None of the selected layers attaches claim-level formulation evidence.

### f4: Nickel hydrate and sodium resazurin have mismatched chemical forms

major / open / confirmed; issue key: culturemech-006543-chemical-form-grounding.

Nickel chloride hexahydrate is linked to anhydrous CHEBI:34887 in both slots. Sodium resazurin has only a primary CHEBI:8806 neutral-form link. Correct copper, cobalt, manganese and magnesium hydrates are credited; D-calcium pantothenate is supported by the current CHEBI:31345 stereochemical object, while generic stock pantothenate remains source-specific.

### f5: Legacy nitrate links and malformed timestamps remain

minor / open / confirmed; issue key: culturemech-006543-legacy-link-and-history-traceability.

Four selected nitrate secondary links use legacy MediaIngredientMech:000170, absent from the current packaged exact-ID index; their primary CHEBI:63043 is correct. KOMODO original timestamps contain literal .fZ. Current source bytes authenticate historical API excerpts but not the separate catalogue or past execution.

## Recommended Actions And Acceptance Checks

### action1

Complete all three stocks in the maintained owners from their exact source sections, retain source batch amounts and explicit denominator limits, preserve repaired nested values and candidates, then regenerate through the conservative merge path.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Keep the base and strain branch distinct; reconcile the exact current primary modifications and uncertain KOMODO provenance. Review repair_parent/repair_child and Child.modification so future repairs do not enforce the old copied signature. Preserve historical events and append a new verified corrective event.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Preserve the DSM owner preparation, assign each instruction to its correct stage, reconcile copied aerobic metadata, and attach scoped root evidence for preparation and stock additions plus ingredient evidence for mass claims.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Resolve the supplied hydrate and sodium-salt mappings against authoritative ontology and MIM, retaining exact source forms and unresolved mappings where needed. Do not change doses through anhydrous molecular-weight inference.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Review the current valid nitrate correspondence without declaring historical invalidity. Preserve malformed original events unchanged; append an evidence-supported context or correction event with the actual current curation date, and fix the timestamp writer for future output.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/chrysiogenes_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/for_dsm_16346.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch062/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch062/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch062/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch062/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz818 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api818 | https://mediadive.dsmz.de/rest/medium/818; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| komodo818 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=818; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodo818variant | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=818.1; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O']; mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic compound that consists of 2-oxohexahydro-1&lt;em&gt;H&lt;/em&gt;-thieno[3,4-&lt;em&gt;d&lt;/em&gt;]imidazole having a valeric acid substituent attached to the tetrahydrothiophene ring. The parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the 5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17015 = riboflavin; definition ['&lt;small&gt;D&lt;/small&gt;-Ribitol in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[&lt;em&gt;g&lt;/em&gt;]pteridin-10(2&lt;em&gt;H&lt;/em&gt;)-yl moiety. It is a nutritional factor found in milk, eggs, malted barley, liver, kidney, heart, and leafy vegetables, but the richest natural source is yeast. The free form occurs only in the retina of the eye, in whey, and in urine; its principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of a group of cobalamin vitamers that exhibit biological activity against vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency. Vitamin B&lt;small&gt;&lt;sub&gt;12&lt;/sub&gt;&lt;/small&gt; deficiency is associated with low red blood cell count and anemia. The vitamers are found in foods such as cereals, meat, fish, and poultry. The vitamers include adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:27470 = folic acid; definition ['An &lt;em&gt;N&lt;/em&gt;-acyl-amino acid that is a form of the water-soluble vitamin B&lt;small&gt;&lt;sub&gt;9&lt;/sub&gt;&lt;/small&gt;. Its biologically active forms (tetrahydrofolate and others) are essential for nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6']; mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic acid in which the amino group is &lt;em&gt;para&lt;/em&gt; to the carboxy group.']; formula ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition []; formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32954 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32954 = sodium acetate; definition []; formula ['C2H3O2.Na']; mass ['82.034']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3']; mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound of nickel and chloride in which the ratio of nickel (in the +2 oxidation state) to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A hydrochloride obtained by combining thiamine chloride with one molar equivalent of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms, in each of which the Zn&lt;small&gt;&lt;sup&gt;2+&lt;/small&gt;&lt;/sup&gt; ions are trigonal planar coordinated to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi63043 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:63043 = potassium nitrate; definition ['The inorganic nitrate salt of potassium.']; formula ['K.NO3']; mass ['101.102']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi64758 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na']; mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na']; mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O']; mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O']; mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg']; mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4']; mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch062/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/chrysiogenes_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api818 raw bytes exactly match the cited historical SHA, and 46 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api818 raw bytes exactly match the cited historical SHA, and 46 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_16346.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api818 raw bytes exactly match the cited historical SHA, and 46 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_16346.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chrysiogenes_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHRYSIOGENES_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch062/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer52 | scripts/apply_cocktail_nesting.py; relevant functions named in summary | context_only | Current match_components and match_stock_signature compare source-stock names and stored values; plan_record retains matched groups and can split exact cross-stock sums when requested. apply_plan moves those groups and asserts receiving volumes only on READ_FROM_THIS_MEDIUM, retaining weaker volumes as candidates. Existing partial nesting is credited; scalar matching alone does not establish complete stock membership or strain-variant equivalence. |
| writer53 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace legacy secondary MIM links or authenticate quantities. |
| writer54 | scripts/cleanup_media_quality.py; relevant functions named in summary | context_only | Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical quantities and flags conflicting quantities rather than summing them. Persisted old duplicate sums require independent source review; they do not establish that this current implementation still sums unequal stages. |
| writer55 | scripts/migrate_legacy_mim_to_chebi.py; relevant functions named in summary | context_only | Full _resolve_chebi/_rewrite_entry/migrate_file read. Existing primary CHEBI is reused if present in MIM; exact-name/synonym resolution is limited by a stereo-prefix guard, and unresolved links remain. The code does not prove chemical equivalence or historical validity merely because an ID has a current row. |
| writer56 | scripts/propose_cocktail_nesting.py; relevant functions named in summary | context_only | Current cocktail_components selects audit-flagged rows, recover_volume extracts addition-volume candidates from preparation prose, and build_proposals prefers the first structured addition from saved MediaDive volume input when present. This proposal stage does not itself perform the exact component matching and candidate-versus-asserted-volume guard implemented by apply_cocktail_nesting.py. Complete stock membership and source scope still require scientific review. |
| writer57 | scripts/repair_komodo_818_chrysiogenes_score10.py; relevant functions named in summary | context_only | Full repair_parent/repair_child and Child.modification read. The code requires an exact copied ingredient signature and changes relationships to STRAIN_SPECIFIC_VARIANT while saying components are preserved. It does not implement the current DSM16346 yeast/lactate prescription. _upsert_event replaces a matching curator/action event, so future remediation should append verified events and preserve old bytes rather than overwrite history. This is current behavior, not proof of historical execution. |
| writer58 | scripts/resolve_komodo_compositions.py; relevant functions named in summary | context_only | Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents copied ingredients/solutions but does not independently authenticate a particular past execution or variant. The underlying resolver is an inspected input and is assessed separately. |
| writer59 | src/culturemech/enrich/dsmz_resolver.py; relevant functions named in summary | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients, solutions, pH, physical state and medium type; it does not copy preparation or independently establish source equivalence. resolve_recipe skips already populated ingredient lists. Current behavior does not authenticate the historical enrichment execution. |
| writer60 | src/culturemech/import/komodo_web_importer.py; relevant functions named in summary | context_only | Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes and initially empty ingredients for later DSMZ enrichment; its strftime format uses literal %f. Read code does not authenticate the past table values or source-copy execution. |
| writer61 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition uses only the primary recipe and prefers provider g_l; it excludes a fixed list of solvent names, which does not include Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes, but not molar-only attributes such as 1M. _parse_preparation_steps collects prose from all solution sections without separate stage fields. These present behaviors do not establish historical execution. |
| writer62 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer63 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer64 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch062/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Exact historical KOMODO 818 and 818.1 routes returned HTTP 403; current DSM 818 supplies a direct DSM 16346 prescription but does not authenticate the inaccessible KOMODO pages.
- Provider1003 ml normalization is documented but not a measured final volume; stock liquid additions and vitamin-stock listed water retain explicit basis limits.
- Current MIM absence of legacy MediaIngredientMech:000170 is a current-snapshot result, not proof of historical invalidity. No experimental growth measurement is asserted from a collection recipe.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T095723Z-chrysiogenes-medium-batch062
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of chrysiogenes_medium
started_at: '2026-10-28T09:29:39.326718Z'
finished_at: '2026-10-28T09:57:23.050558Z'
reviewer:
  identity: Codex independent record reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh review of existing unchanged repository records; this
    reviewer did not author or curate the selected target/owners. Historical reports
    were independently reassessed against current exact sources.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The base recipe and current partial stock/topology repairs are identifiable,
  but the generated target is stale, stock strengths remain flattened, and DSM 16346
  is incorrectly represented as an unchanged base. Preserve supported provider values
  and correct existing nested rows while reconstructing exact stock stages, preparation
  and scoped evidence.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml
    sha256: 496676365602b3ec95915d7cc33a1f5fb439724ef68aa7ad7e2f7049e7a08247
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    sha256: 5780db78833fbcce962e168ac83bd7012e56e55925f63c7b7fd8887b4b108910
    role: context
  - path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    sha256: 4108d92eb0d384f51b95dfb291f31077219bc5870ed96ad09443ae93caca1adf
    role: context
  - path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    sha256: 9d970552d7b985e7be5e65ddaedf31e0aee8fce138041a27a4618b0638bbb552
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml.md
    sha256: 3e94bff28110ee486d487674d41e7c1aa620dd73d3f345adef8312508104a927
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_16346.yaml.md
    sha256: 8ad0bbc562aad55caf5c7ea357212885ef43fbfbb76eb78cc8f902b3ea615696
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/chrysiogenes_medium.yaml.md
    sha256: 8d1e11e617a05ae257d7585cc859f0b29a16ad9a298aa1fabc14380b67cf34fb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHRYSIOGENES_MEDIUM.md
    sha256: ae3a161eabe8e1724d3b727b42c7871c40787764b0efac1bb1e8784604e03d3b
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.md
    sha256: 585b1cfa0939a80d9a7ef019a5de88a52f67ae9109fc532285844392cf9f3efa
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chrysiogenes_medium.md
    sha256: f54c4eb677ea54ecd86fb1594f2b1ee479fa602a9185091910fd186386260764
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_16346.md
    sha256: 6a291ca0b68f61aa020e53d242e83d554e09e0778df0dd8973503eb993f1c3ea
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
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/propose_cocktail_nesting.py
    sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
    role: context
  - path: scripts/repair_komodo_818_chrysiogenes_score10.py
    sha256: 34d3deee84bdc60300b03850975e231d6923975bdffe56a3b9e1711593ffee13
    role: context
  - path: scripts/resolve_komodo_compositions.py
    sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
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
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch062 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006543
targets:
- target_id: CultureMech:006543
  path: data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml
  label: chrysiogenes_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006543
  command: just validate-schema data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006543
  command: just validate-strict data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch062/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006543
  command: just validate-terms data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:006543
  command: just validate-references data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T09:34:59.416205Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 496676365602b3ec95915d7cc33a1f5fb439724ef68aa7ad7e2f7049e7a08247
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T09:34:59.416355Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 5780db78833fbcce962e168ac83bd7012e56e55925f63c7b7fd8887b4b108910
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T09:34:59.416377Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 4108d92eb0d384f51b95dfb291f31077219bc5870ed96ad09443ae93caca1adf
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/for_dsm_16346.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T09:34:59.416397Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 9d970552d7b985e7be5e65ddaedf31e0aee8fce138041a27a4618b0638bbb552
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch062/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:40.552562Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 346ae1b2516ec8547c0ee57cc42a316bffbabf23bc245b38b66e67d1d3b33b3f
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch062/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:41.496374Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 77234359dc7b8c5124a079b2746f34e54025373e3f353a3476a0b300e6d957fa
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch062/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:42.913658Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: b8f0d7e89e0a15e074fb217bc0d688592356ec1052ddad82a8c4345a176a9451
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch062/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T09:29:43.762027Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: f5ae7b82ad8f6abd21812648a6ce327ac8640ecff4b3b1000d1cb258df8e8581
- evidence_id: dsmz818
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:23.316471Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08
- evidence_id: api818
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/818
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:23.292920Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: 5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb
- evidence_id: komodo818
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=818
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:23.265787Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: fbf2ea73b13cea68c452a128328f74aad50cdbe9159e9dd4791bae64fc264ab8
- evidence_id: komodo818variant
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=818.1
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T09:30:23.216080Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 4aa5714a27e26e5756ad7cb6b0696fd4623f8c98d3670484de4c0d4b959bc31f
- evidence_id: chebi132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.742590Z'
  support: supports
  summary: OLS current exact CHEBI:132751 = thiamine hydrochloride dihydrate; definition
    ['A hydrate that is the dihydrate form of thiamine hydrochloride.']; formula ['C12H18N4OS.2Cl.2H2O'];
    mass ['373.306']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.409645Z'
  support: supports
  summary: OLS current exact CHEBI:15940 = nicotinic acid; definition ['A pyridinemonocarboxylic
    acid that is pyridine in which the hydrogen at position 3 is replaced by a carboxy
    group.']; formula ['C6H5NO2']; mass ['123.111']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 3330ed782e73526a087fb250ed5895ff232f117a896d45d541dff431e5c1f0e1
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.398530Z'
  support: supports
  summary: OLS current exact CHEBI:15956 = biotin; definition ['An organic heterobicyclic
    compound that consists of 2-oxohexahydro-1<em>H</em>-thieno[3,4-<em>d</em>]imidazole
    having a valeric acid substituent attached to the tetrahydrothiophene ring. The
    parent of the class of biotins.']; formula ['C10H16N2O3S']; mass ['244.316'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d2d51887df4de92642b66e9d15086ef82eccbc476dd4077d514ca709181ab4bd
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:23.197948Z'
  support: supports
  summary: OLS current exact CHEBI:16494 = lipoic acid; definition ['A heterocyclic
    thia fatty acid comprising pentanoic acid with a 1,2-dithiolan-3-yl group at the
    5-position.']; formula ['C8H14O2S2']; mass ['206.332']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:23.131655Z'
  support: supports
  summary: OLS current exact CHEBI:17015 = riboflavin; definition ['<small>D</small>-Ribitol
    in which the hydroxy group at position 5 is substituted by a 7,8-dimethyl-2,4-dioxo-3,4-dihydrobenzo[<em>g</em>]pteridin-10(2<em>H</em>)-yl
    moiety. It is a nutritional factor found in milk, eggs, malted barley, liver,
    kidney, heart, and leafy vegetables, but the richest natural source is yeast.
    The free form occurs only in the retina of the eye, in whey, and in urine; its
    principal forms in tissues and cells are as flavin mononucleotide and flavin-adenine
    dinucleotide.']; formula ['C17H20N4O6']; mass ['376.369']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42bc5bbd29b208bfd3062acb11dfa63ccebf81f77ffd72ab596de863cb68aa4
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.385686Z'
  support: supports
  summary: OLS current exact CHEBI:176843 = vitamin B12; definition ['Any member of
    a group of cobalamin vitamers that exhibit biological activity against vitamin
    B<small><sub>12</sub></small> deficiency. Vitamin B<small><sub>12</sub></small>
    deficiency is associated with low red blood cell count and anemia. The vitamers
    are found in foods such as cereals, meat, fish, and poultry. The vitamers include
    adenosylcobalamin, hydroxocobalamin, cyanocobalamin, aquacobalamin, nitritocobalamin
    and methylcobabalamin (also includes their ionized, salt and phosphate derivatives).'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:18.890091Z'
  support: supports
  summary: OLS current exact CHEBI:26710 = sodium chloride; definition ['An inorganic
    chloride salt having sodium(1+) as the counterion.']; formula ['Cl.Na']; mass
    ['58.443']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:23.073812Z'
  support: supports
  summary: OLS current exact CHEBI:27470 = folic acid; definition ['An <em>N</em>-acyl-amino
    acid that is a form of the water-soluble vitamin B<small><sub>9</sub></small>.
    Its biologically active forms (tetrahydrofolate and others) are essential for
    nucleotide biosynthesis and homocysteine remethylation.']; formula ['C19H19N7O6'];
    mass ['441.404']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: fe3e4a2f0f0fa51f94efe6bbf0fa8883d43eafef8db73cfd37bc25ce15fdd12f
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.350111Z'
  support: supports
  summary: OLS current exact CHEBI:30753 = 4-aminobenzoic acid; definition ['An aminobenzoic
    acid in which the amino group is <em>para</em> to the carboxy group.']; formula
    ['C7H7NO2']; mass ['137.138']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:21.196677Z'
  support: supports
  summary: OLS current exact CHEBI:30961 = pyridoxine hydrochloride; definition ['The
    hydrochloride salt of pyridoxine.']; formula ['C8H11NO3.HCl']; mass ['205.641'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: f1c95b83f5396067c3959c20ee4715c78f7895f5084dd214b3a4bf01e064f21d
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:18.544435Z'
  support: supports
  summary: OLS current exact CHEBI:31206 = ammonium chloride; definition ['An inorganic
    chloride having ammonium as the counterion.']; formula ['Cl.H4N']; mass ['53.492'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.904169Z'
  support: supports
  summary: OLS current exact CHEBI:31345 = Calcium pantothenate; definition []; formula
    ['2C9H16NO5.Ca']; mass ['476.536']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32139
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:22.741164Z'
  support: supports
  summary: OLS current exact CHEBI:32139 = sodium hydrogencarbonate; definition [];
    formula ['CHO3.Na']; mass ['84.006']; obsolete=False. Literal label is distinct
    from supplied-form equivalence.
  snapshot_sha256: 2a41873aa455dc8563a47d36add836fffb6fb758ce7a2d1c28295e77646315fe
- evidence_id: chebi32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:22.702475Z'
  support: supports
  summary: OLS current exact CHEBI:32149 = sodium sulfate; definition []; formula
    ['2Na.O4S']; mass ['142.043']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 49c4b3ee63a59ea3acba0006afd53c6050dd13cd2210a15e3395b100bc6749b8
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:18.144684Z'
  support: supports
  summary: OLS current exact CHEBI:32588 = potassium chloride; definition ['A metal
    chloride salt with a K(+) counterion.']; formula ['Cl.K']; mass ['74.551']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 536d6e3b5f2a3f1cb36d9c04b1502c4a6f00f4d770cd87b05b481e66ea43a411
- evidence_id: chebi32954
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32954
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:22.602450Z'
  support: supports
  summary: OLS current exact CHEBI:32954 = sodium acetate; definition []; formula
    ['C2H3O2.Na']; mass ['82.034']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 573cba85f57c363463610a20b17be618893d6432ba239604fbd8aa562f98161b
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:17.947089Z'
  support: supports
  summary: OLS current exact CHEBI:33118 = boric acid; definition []; formula ['H3BO3'];
    mass ['61.833']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.775488Z'
  support: supports
  summary: OLS current exact CHEBI:34887 = nickel dichloride; definition ['A compound
    of nickel and chloride in which the ratio of nickel (in the +2 oxidation state)
    to chloride is 1:2.']; formula ['Cl2Ni']; mass ['129.599']; obsolete=False. Literal
    label is distinct from supplied-form equivalence.
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:22.510267Z'
  support: supports
  summary: OLS current exact CHEBI:49105 = thiamine hydrochloride; definition ['A
    hydrochloride obtained by combining thiamine chloride with one molar equivalent
    of hydrochloric acid.']; formula ['C12H17N4OS.Cl.HCl']; mass ['337.276']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 0b923c215888606038af1e3f0c1b1bcc35e4ab84966d1733a91fdfcbee8f2ae4
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.726940Z'
  support: supports
  summary: OLS current exact CHEBI:49976 = zinc dichloride; definition ['A compound
    of zinc and chloride ions in the ratio 1:2. It exists in four crystalline forms,
    in each of which the Zn<small><sup>2+</small></sup> ions are trigonal planar coordinated
    to four chloride ions.']; formula ['2Cl.Zn']; mass ['136.296']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: d27644ae0df5935f8f18a28faa1ba6096fefeb9d0cb951b39751d442c92bd321
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.691698Z'
  support: supports
  summary: OLS current exact CHEBI:53503 = cobalt chloride hexahydrate; definition
    ['A hydrate of cobalt chloride containing cobalt (in +2 oxidation state), chloride
    and water moieties in the ratio 1:2:6.']; formula ['2Cl.Co.6H2O']; mass ['237.929'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:17.341751Z'
  support: supports
  summary: OLS current exact CHEBI:63036 = potassium dihydrogen phosphate; definition
    ['A potassium salt in which dihydrogen phosphate(1−) is the counterion.']; formula
    ['H2O4P.K']; mass ['136.084']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 48f13d8c6f55837c16b5909790ad7b78496b0bd8d04b8b47e3d0926d9ff602a3
- evidence_id: chebi63043
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63043
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:22.503808Z'
  support: supports
  summary: OLS current exact CHEBI:63043 = potassium nitrate; definition ['The inorganic
    nitrate salt of potassium.']; formula ['K.NO3']; mass ['101.102']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: c324450e6330a169c708c32a7908b6df0276f4dc76da413e473b563928f61c13
- evidence_id: chebi64758
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64758
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.171246Z'
  support: supports
  summary: OLS current exact CHEBI:64758 = EDTA disodium salt dihydrate; definition
    ['A hydrate that is the dihydrate form of EDTA disodium salt.']; formula ['C10H14N2O8.2H2O.2Na'];
    mass ['372.238']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 5432921ff4fea3479e93ce6392a2654e3d5560255beb96022793102e776d9647
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:17.036791Z'
  support: supports
  summary: OLS current exact CHEBI:75213 = sodium molybdate dihydrate; definition
    ['A hydrate that is the dihydrate form of sodium molybdate.']; formula ['2H2O.MoO4.2Na'];
    mass ['241.946']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:15.999531Z'
  support: supports
  summary: OLS current exact CHEBI:86158 = calcium chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of calcium chloride.']; formula ['Ca.2Cl.2H2O'];
    mass ['147.014']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.118004Z'
  support: supports
  summary: OLS current exact CHEBI:86249 = iron dichloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of iron dichloride.']; formula ['Cl2Fe.4H2O'];
    mass ['198.811']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.049072Z'
  support: supports
  summary: OLS current exact CHEBI:86318 = copper(II) chloride dihydrate; definition
    ['A hydrate that is the dihydrate form of copper(II) chloride. It occurs naturally
    as the mineral eriochalcite.']; formula ['Cl2Cu.2H2O']; mass ['170.482']; obsolete=False.
    Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:15.999491Z'
  support: supports
  summary: OLS current exact CHEBI:86345 = magnesium dichloride hexahydrate; definition
    ['A hydrate that is the hexahydrate form of magnesium dichloride.']; formula ['2Cl.6H2O.Mg'];
    mass ['203.301']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 08a75ab7c89066e54998e26bfba46e579358aa1a0ee5611430577d7c38e25133
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:20.009797Z'
  support: supports
  summary: OLS current exact CHEBI:86368 = manganese(II) chloride tetrahydrate; definition
    ['A hydrate that is the tetrahydrate form of manganese(II) chloride.']; formula
    ['Cl2Mn.4H2O']; mass ['197.904']; obsolete=False. Literal label is distinct from
    supplied-form equivalence.
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T09:30:15.999282Z'
  support: supports
  summary: OLS current exact CHEBI:8806 = Resazurin; definition []; formula ['C12H7NO4'];
    mass ['229.191']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch062/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T09:34:59.428599Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 4cdeedbb1e6f1cb6362b9fd46af934b4e357be1f5e56a9c366ccb49bc8d9f2c1
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/chrysiogenes_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430545Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api818 raw bytes exactly match the cited historical SHA, and 46
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 8d1e11e617a05ae257d7585cc859f0b29a16ad9a298aa1fabc14380b67cf34fb
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430582Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api818 raw bytes exactly match the cited historical SHA, and 46
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 3e94bff28110ee486d487674d41e7c1aa620dd73d3f345adef8312508104a927
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2500-3000/records/bacterial/for_dsm_16346.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430617Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api818 raw bytes exactly match the cited historical SHA, and 46
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 8ad0bbc562aad55caf5c7ea357212885ef43fbfbb76eb78cc8f902b3ea615696
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430638Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 585b1cfa0939a80d9a7ef019a5de88a52f67ae9109fc532285844392cf9f3efa
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/for_dsm_16346.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430658Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 6a291ca0b68f61aa020e53d242e83d554e09e0778df0dd8973503eb993f1c3ea
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chrysiogenes_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430677Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: f54c4eb677ea54ecd86fb1594f2b1ee479fa602a9185091910fd186386260764
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHRYSIOGENES_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T09:34:59.430700Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: ae3a161eabe8e1724d3b727b42c7871c40787764b0efac1bb1e8784604e03d3b
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch062/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T09:34:59.430728Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: 7f19a229f91da9248d00093fefb104ee6e8b2b2bf0e065f0ff4d3802f74d477f
- evidence_id: writer52
  kind: record_content
  reference: scripts/apply_cocktail_nesting.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430755Z'
  support: context_only
  summary: Current match_components and match_stock_signature compare source-stock
    names and stored values; plan_record retains matched groups and can split exact
    cross-stock sums when requested. apply_plan moves those groups and asserts receiving
    volumes only on READ_FROM_THIS_MEDIUM, retaining weaker volumes as candidates.
    Existing partial nesting is credited; scalar matching alone does not establish
    complete stock membership or strain-variant equivalence.
  snapshot_sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
- evidence_id: writer53
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430774Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace legacy secondary MIM links or
    authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer54
  kind: record_content
  reference: scripts/cleanup_media_quality.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430794Z'
  support: context_only
  summary: Current merge_duplicate_ingredients/_merge_ingredient_group collapses identical
    quantities and flags conflicting quantities rather than summing them. Persisted
    old duplicate sums require independent source review; they do not establish that
    this current implementation still sums unequal stages.
  snapshot_sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
- evidence_id: writer55
  kind: record_content
  reference: scripts/migrate_legacy_mim_to_chebi.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430812Z'
  support: context_only
  summary: Full _resolve_chebi/_rewrite_entry/migrate_file read. Existing primary
    CHEBI is reused if present in MIM; exact-name/synonym resolution is limited by
    a stereo-prefix guard, and unresolved links remain. The code does not prove chemical
    equivalence or historical validity merely because an ID has a current row.
  snapshot_sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
- evidence_id: writer56
  kind: record_content
  reference: scripts/propose_cocktail_nesting.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430830Z'
  support: context_only
  summary: Current cocktail_components selects audit-flagged rows, recover_volume
    extracts addition-volume candidates from preparation prose, and build_proposals
    prefers the first structured addition from saved MediaDive volume input when present.
    This proposal stage does not itself perform the exact component matching and candidate-versus-asserted-volume
    guard implemented by apply_cocktail_nesting.py. Complete stock membership and
    source scope still require scientific review.
  snapshot_sha256: e886c446a8398f08f1cc735b1c3a9812c5fc6371a36b69ef5325f1c53f14e6c0
- evidence_id: writer57
  kind: record_content
  reference: scripts/repair_komodo_818_chrysiogenes_score10.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430848Z'
  support: context_only
  summary: Full repair_parent/repair_child and Child.modification read. The code requires
    an exact copied ingredient signature and changes relationships to STRAIN_SPECIFIC_VARIANT
    while saying components are preserved. It does not implement the current DSM16346
    yeast/lactate prescription. _upsert_event replaces a matching curator/action event,
    so future remediation should append verified events and preserve old bytes rather
    than overwrite history. This is current behavior, not proof of historical execution.
  snapshot_sha256: 34d3deee84bdc60300b03850975e231d6923975bdffe56a3b9e1711593ffee13
- evidence_id: writer58
  kind: record_content
  reference: scripts/resolve_komodo_compositions.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430863Z'
  support: context_only
  summary: 'Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment
    to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents
    copied ingredients/solutions but does not independently authenticate a particular
    past execution or variant. The underlying resolver is an inspected input and is
    assessed separately.'
  snapshot_sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
- evidence_id: writer59
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430884Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients, solutions,
    pH, physical state and medium type; it does not copy preparation or independently
    establish source equivalence. resolve_recipe skips already populated ingredient
    lists. Current behavior does not authenticate the historical enrichment execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer60
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430907Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes
    and initially empty ingredients for later DSMZ enrichment; its strftime format
    uses literal %f. Read code does not authenticate the past table values or source-copy
    execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer61
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430933Z'
  support: context_only
  summary: Current _parse_api_composition uses only the primary recipe and prefers
    provider g_l; it excludes a fixed list of solvent names, which does not include
    Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator
    check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes,
    but not molar-only attributes such as 1M. _parse_preparation_steps collects prose
    from all solution sections without separate stage fields. These present behaviors
    do not establish historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer62
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430950Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer63
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430968Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer64
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T09:34:59.430987Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch062/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T09:52:03.423050Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: e3252a25c14ade3d430203436b88ccfdaa68c34e86521a0a54dc60d993114e2c
assessments:
- assessment_id: a1
  area: identity
  topic: Base versus DSM 16346 branch
  outcome: concern
  summary: Source 818 identity is explicit, and the current maintained child relationship
    correction is credited. Its statement that components are preserved conflicts
    with the current primary branch prescription. Generated SOURCE_DUPLICATE relationships
    and synonym consolidation predate that repair.
  target_ids:
  - CultureMech:006543
  evidence_ids:
  - dsmz818
  - api818
  - local0
  - local3
- assessment_id: a2
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: 'Seven complete historical reports were read; all 138 quoted API objects
    equal current objects. Their blanket conflict status on every base row was overbroad:
    current provider nominal main values and already nested stock rows are explicitly
    credited here. No attached formulation claims exist in the selected documents.
    All historical API excerpts with matching current raw digests are independently
    authenticated in historical-authentication.json. Matching bytes do not verify
    old execution or the separate KOMODO catalogue. Current MediaDive code separates
    stock additions but gathers all solution preparation into a root list; current
    conservative merging preserves scientific fields and rejects incompatible formulations.
    Those present behaviors do not prove how the old generated records were produced.'
  target_ids:
  - CultureMech:006543
  evidence_ids:
  - history-auth
  - writer52
  - writer53
  - writer54
  - writer55
  - writer56
  - writer57
  - writer58
  - writer59
  - writer60
  - writer61
  - writer62
  - writer63
  - writer64
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 150 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:006543
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006543",
    "selected_concentration_field_count": 150, "selected_concentration_fields_covered":
    150, "decisions": [{"decision_id": "q1", "subject": "NaCl", "local_fields": [{"record_path":
    "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path": "ingredients[0].concentration",
    "original": {"value": "1.19641", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1.19641",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1.19641",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "1.19641",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\":
    43,\n                        \"amount\": 1.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.19641,\n                        \"mmol_l\":
    20.4725,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 3-3", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "NaCl                                                     1.20        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject":
    "KCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"KCl\",\n                        \"compound_id\":
    61,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    4.01211,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "KCl                                                      0.30        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "NH4Cl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\":
    42,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    5.59175,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "NH4Cl                                                    0.30        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "KH2PO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.199402",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\":
    11,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.199402,\n                        \"mmol_l\":
    1.46527,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "KH2PO4                                                   0.20        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject":
    "Na2SO4", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.299103",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Na2SO4\",\n                        \"compound_id\":
    110,\n                        \"amount\": 0.3,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.299103,\n                        \"mmol_l\":
    2.10576,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "Na2SO4                                                   0.30        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject":
    "MgCl2 x 6 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.398804",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.398804",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.398804",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.398804",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\":
    79,\n                        \"amount\": 0.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.398804,\n                        \"mmol_l\":
    1.96162,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 8-8", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "MgCl2 x 6
    H2O                                            0.40        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q7", "subject": "CaCl2 x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.149551",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.149551",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.149551",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "0.149551",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\":
    7,\n                        \"amount\": 0.15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.149551,\n                        \"mmol_l\":
    1.01725,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "CaCl2 x 2
    H2O                                            0.15        g", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q8", "subject": "Sodium resazurin",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[7].concentration", "original": {"value": "0.000498504",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration. The source is 0.5 ml of explicit
    0.1% w/v stock, giving 0.5 mg per listed batch; this is separate from neutral-resazurin
    grounding.", "sources": [{"locator": "$.data.solutions[0].recipe[8]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\":
    1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.000498504,\n                        \"mmol_l\": 0.00198473,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 11-11", "source_key": "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "Sodium resazurin
    (0.1% w/v)                              0.50       ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q9", "subject": "NaHCO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[8].concentration", "original": {"value": "0.598205", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.598205",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.598205",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[8].concentration", "original": {"value": "0.598205",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[9]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\":
    55,\n                        \"amount\": 0.6,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.598205,\n                        \"mmol_l\":
    7.1209,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "NaHCO3                                                   0.60        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject":
    "KNO3", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[9].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[10]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"KNO3\",\n                        \"compound_id\":
    191,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    4.93066,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "KNO3                                                     0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject":
    "Na-acetate", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main-medium provider
    normalization with explicit denominator limit", "interpretation": "The stored
    value exactly matches current API 818 g_l on its declared 1003 ml provider basis.
    The PDF supports the stated batch input but lists 1000 ml water plus stock additions,
    not a measured final volume; retain the provider basis explicitly rather than
    silently round to a one-litre final concentration.", "sources": [{"locator": "$.data.solutions[0].recipe[13]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    14,\n                        \"compound\": \"Na-acetate\",\n                        \"compound_id\":
    23,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.498504,\n                        \"mmol_l\":
    6.07682,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 16-16", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "Na-acetate                                               0.50        g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject":
    "DSM 16346 acetate replacement", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[10].concentration", "original": {"value": "0.498504",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "strain-specific branch",
    "interpretation": "The current primary explicitly replaces acetate with 1.10 g/l
    sodium L-lactate and adds 0.80 g/l yeast extract for DSM 16346. The local variant
    still copies the base acetate row. This primary branch statement does not authenticate
    the unavailable historical KOMODO page or justify merging the branch back into
    its base.", "sources": [{"locator": "extracted-text lines 28-29", "source_key":
    "dsmz818", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346:
    Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10
    g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "Na2-EDTA x 2 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q14", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "1.5", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q15", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q16", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q17", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q18", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q19", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q20", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q21", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q22", "subject": "Biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q23", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q24", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.4", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The generated value is the sum of two distinct vitamin-stock
    strengths; their recipes and additions must remain separate. Retain supplied form
    and batch units, complete the proper stock, and preserve the source addition with
    an explicit denominator. No final-medium replacement rate is inferred.", "sources":
    [{"locator": "$.data.solutions[2].recipe[2]", "source_key": "api818", "reference":
    "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[5]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q25", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q26", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q27", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[25].concentration", "original": {"value": "0.25", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The generated value is the sum of two distinct vitamin-stock strengths; their
    recipes and additions must remain separate. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[3]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q28", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q29", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[27].concentration", "original": {"value": "0.101", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The generated value is the sum of two distinct vitamin-stock strengths; their
    recipes and additions must remain separate. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q30", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[28].concentration", "original": {"value": "0.13", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The generated value is the sum of two distinct vitamin-stock
    strengths; their recipes and additions must remain separate. Retain supplied form
    and batch units, complete the proper stock, and preserve the source addition with
    an explicit denominator. No final-medium replacement rate is inferred.", "sources":
    [{"locator": "$.data.solutions[2].recipe[8]", "source_key": "api818", "reference":
    "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "$.data.solutions[3].recipe[1]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q31", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[29].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q32", "subject": "D-(+)-biotin", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ingredients[30].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q33", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[31].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q34", "subject": "Thiamine-HCl x 2 H2O",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[32].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q35", "subject": "Na2-EDTA x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "original": {"value": "5.2", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q36", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "original": {"value": "0.07", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q37", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q38", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "original": {"value": "0.006",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus
    main medium", "interpretation": "This direct ingredient is a stock component,
    not a demonstrated main-medium concentration. The scalar matches a source stock
    value, but its direct-medium placement omits the receiving dilution. Retain supplied
    form and batch units, complete the proper stock, and preserve the source addition
    with an explicit denominator. No final-medium replacement rate is inferred.",
    "sources": [{"locator": "$.data.solutions[1].recipe[4]", "source_key": "api818",
    "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q39", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "original": {"value": "0.19", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q40", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "original": {"value": "0.002",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus
    main medium", "interpretation": "This direct ingredient is a stock component,
    not a demonstrated main-medium concentration. The scalar matches a source stock
    value, but its direct-medium placement omits the receiving dilution. Retain supplied
    form and batch units, complete the proper stock, and preserve the source addition
    with an explicit denominator. No final-medium replacement rate is inferred.",
    "sources": [{"locator": "$.data.solutions[1].recipe[6]", "source_key": "api818",
    "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q41", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[17].concentration", "original": {"value": "0.024",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus
    main medium", "interpretation": "This direct ingredient is a stock component,
    not a demonstrated main-medium concentration. The scalar matches a source stock
    value, but its direct-medium placement omits the receiving dilution. Retain supplied
    form and batch units, complete the proper stock, and preserve the source addition
    with an explicit denominator. No final-medium replacement rate is inferred.",
    "sources": [{"locator": "$.data.solutions[1].recipe[7]", "source_key": "api818",
    "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q42", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "original": {"value": "0.036",
    "unit": "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus
    main medium", "interpretation": "This direct ingredient is a stock component,
    not a demonstrated main-medium concentration. The scalar matches a source stock
    value, but its direct-medium placement omits the receiving dilution. Retain supplied
    form and batch units, complete the proper stock, and preserve the source addition
    with an explicit denominator. No final-medium replacement rate is inferred.",
    "sources": [{"locator": "$.data.solutions[1].recipe[8]", "source_key": "api818",
    "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q43", "subject": "Biotin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[19].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q44", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[20].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q45", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q46", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[22].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q47", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q48", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q49", "subject": "D-(+)-biotin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[25].concentration", "original": {"value": "0.02", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q50", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q51", "subject": "Na2-EDTA x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q52", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q53", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q54", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q55", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q56", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q57", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q58", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q59", "subject": "Biotin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q60", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q61", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q62", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[22].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q63", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q64", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q65", "subject": "D-(+)-biotin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q66", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q67", "subject": "Na2-EDTA x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[11].concentration", "original": {"value": "5.2", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q68", "subject": "ZnCl2", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[12].concentration", "original": {"value": "0.07", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q69", "subject": "MnCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[13].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q70", "subject": "H3BO3", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[14].concentration", "original": {"value": "0.006", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q71", "subject": "CoCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[15].concentration", "original": {"value": "0.19", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q72", "subject": "CuCl2 x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[16].concentration", "original": {"value": "0.002", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q73", "subject": "NiCl2 x 6 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[17].concentration", "original": {"value": "0.024", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q74", "subject": "Na2MoO4 x 2 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[18].concentration", "original": {"value": "0.036", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[1].recipe[8]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q75", "subject": "Biotin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[19].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q76", "subject": "Folic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[20].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q77", "subject": "Thiamine HCl", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[21].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q78", "subject": "Riboflavin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[22].concentration", "original": {"value": "0.05", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q79", "subject": "Calcium D-(+)-pantothenate",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[23].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q80", "subject": "(DL)-alpha-Lipoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[24].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[2].recipe[9]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q81", "subject": "D-(+)-biotin", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "ingredients[25].concentration", "original": {"value": "0.02", "unit": "G_PER_L"}}],
    "decision": "conflict", "stage": "flattened stock versus main medium", "interpretation":
    "This direct ingredient is a stock component, not a demonstrated main-medium concentration.
    The scalar matches a source stock value, but its direct-medium placement omits
    the receiving dilution. Retain supplied form and batch units, complete the proper
    stock, and preserve the source addition with an explicit denominator. No final-medium
    replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q82", "subject": "Calcium pantothenate",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "ingredients[26].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "conflict", "stage": "flattened stock versus main medium",
    "interpretation": "This direct ingredient is a stock component, not a demonstrated
    main-medium concentration. The scalar matches a source stock value, but its direct-medium
    placement omits the receiving dilution. Retain supplied form and batch units,
    complete the proper stock, and preserve the source addition with an explicit denominator.
    No final-medium replacement rate is inferred.", "sources": [{"locator": "$.data.solutions[3].recipe[4]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q83", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[0].composition[0].concentration", "original": {"value":
    "1.5", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q84", "subject": "Trace element solution
    SL-11 addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus
    final-litre denominator", "interpretation": "Primary and API specify 1 ml for
    the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis;
    final volume is not independently established from 1000 ml water. The target lacks
    these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q85", "subject": "Thiamine-HCl x 2 H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[1].composition[0].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q86", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[1].composition[1].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q87", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[1].composition[2].concentration", "original": {"value":
    "0.08", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q88", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[1].composition[3].concentration", "original": {"value":
    "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q89", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[1].composition[4].concentration", "original": {"value":
    "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q90", "subject": "Seven vitamins solution
    addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus
    final-litre denominator", "interpretation": "Primary and API specify 1 ml for
    the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis;
    final volume is not independently established from 1000 ml water. The target lacks
    these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[12]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q91", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[2].composition[0].concentration", "original": {"value":
    "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q92", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[2].composition[1].concentration", "original": {"value":
    "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[8]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q93", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[2].composition[2].concentration", "original": {"value":
    "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q94", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[2].composition[3].concentration", "original": {"value":
    "0.001", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q95", "subject":
    "Wolin''s vitamin solution (10x) addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus
    final-litre denominator", "interpretation": "Primary and API specify 1 ml for
    the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis;
    final volume is not independently established from 1000 ml water. The target lacks
    these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[11]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q96", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q97", "subject": "Trace element solution
    SL-11 addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[0].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus
    final-litre denominator", "interpretation": "Primary and API specify 1 ml for
    the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis;
    final volume is not independently established from 1000 ml water. The target lacks
    these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q98", "subject": "Thiamine-HCl x 2 H2O",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[1].composition[0].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q99", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q100", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[1].composition[2].concentration", "original": {"value":
    "0.08", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q101", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[1].composition[3].concentration", "original": {"value":
    "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q102", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "solutions[1].composition[4].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q103", "subject": "Seven vitamins solution
    addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[1].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus
    final-litre denominator", "interpretation": "Primary and API specify 1 ml for
    the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis;
    final volume is not independently established from 1000 ml water. The target lacks
    these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[12]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q104", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "solutions[2].composition[0].concentration", "original": {"value": "0.05", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[5]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q105", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[2].composition[1].concentration", "original": {"value":
    "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[8]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q106", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[2].composition[2].concentration", "original": {"value":
    "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q107", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml", "field_path":
    "solutions[2].composition[3].concentration", "original": {"value": "0.001", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[7]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q108", "subject":
    "Wolin''s vitamin solution (10x) addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "solutions[2].concentration", "original": {"value": "1", "unit":
    "ML_PER_L"}}], "decision": "unsupported", "stage": "stock addition volume versus
    final-litre denominator", "interpretation": "Primary and API specify 1 ml for
    the listed recipe. The local 1 ML_PER_L descriptor must retain that recipe basis;
    final volume is not independently established from 1000 ml water. The target lacks
    these stocks altogether.", "sources": [{"locator": "$.data.solutions[0].recipe[11]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q109", "subject": "FeCl2 x 4 H2O", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "solutions[0].composition[0].concentration", "original": {"value": "1.5", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[1].recipe[1]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q110", "subject": "Trace element solution
    SL-11 candidate addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[0].concentration_candidates", "original": [{"value":
    "1", "unit": "ML_PER_L", "basis": "CROSS_MEDIUM_INFERENCE", "support": "This record
    is a variant of medium 818 (KOMODO key ''818.1''); volume read from base medium
    818 (''CHRYSIOGENES MEDIUM'').", "counterevidence": "The variant''s own recipe
    was never read — only base medium 818''s — so the modification may change this
    volume. A stock''s addition volume varies by citing medium: MediaDive medium 142
    adds ''Trace element solution (Vishniac & Santer)'' at 0.2 ml and medium 69 adds
    the same stock at 5 ml.", "proposed_by": "apply_cocktail_nesting.py"}]}], "decision":
    "evidence_only", "stage": "preserved cross-medium candidate", "interpretation":
    "The variant deliberately retains an unasserted candidate. Current DSM 818 explicitly
    identifies the DSM 16346 branch and its modifications, but the unavailable KOMODO
    route remains a separate identity limit. Do not automatically promote this proposed
    per-litre denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"solution\": \"Trace element solution SL-11\",\n                        \"solution_id\":
    1474,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 28-29", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346:
    Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10
    g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q111", "subject": "Thiamine-HCl x 2 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[1].composition[0].concentration", "original": {"value":
    "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[6]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q112", "subject": "Nicotinic acid", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "solutions[1].composition[1].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[3]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q113", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[1].composition[2].concentration", "original": {"value":
    "0.08", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q114", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[1].composition[3].concentration", "original": {"value":
    "0.3", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q115", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "solutions[1].composition[4].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[3].recipe[0]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q116", "subject": "Seven vitamins solution
    candidate addition", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[1].concentration_candidates", "original": [{"value":
    "1", "unit": "ML_PER_L", "basis": "CROSS_MEDIUM_INFERENCE", "support": "This record
    is a variant of medium 818 (KOMODO key ''818.1''); volume read from base medium
    818 (''CHRYSIOGENES MEDIUM'').", "counterevidence": "The variant''s own recipe
    was never read — only base medium 818''s — so the modification may change this
    volume. A stock''s addition volume varies by citing medium: MediaDive medium 142
    adds ''Trace element solution (Vishniac & Santer)'' at 0.2 ml and medium 69 adds
    the same stock at 5 ml.", "proposed_by": "apply_cocktail_nesting.py"}]}], "decision":
    "evidence_only", "stage": "preserved cross-medium candidate", "interpretation":
    "The variant deliberately retains an unasserted candidate. Current DSM 818 explicitly
    identifies the DSM 16346 branch and its modifications, but the unavailable KOMODO
    route remains a separate identity limit. Do not automatically promote this proposed
    per-litre denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[12]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    13,\n                        \"solution\": \"Seven vitamins solution\",\n                        \"solution_id\":
    1038,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 28-29", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346:
    Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10
    g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q117", "subject": "Nicotinic acid", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[2].composition[0].concentration", "original": {"value":
    "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[5]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q118", "subject": "p-Aminobenzoic acid",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[2].composition[1].concentration", "original": {"value":
    "0.05", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly
    nested stock component", "interpretation": "The current nested value matches the
    exact stock recipe on the provider-declared 1000 ml stock basis. This existing
    partial repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[8]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q119", "subject": "Pyridoxine hydrochloride",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml",
    "field_path": "solutions[2].composition[2].concentration", "original": {"value":
    "0.1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested
    stock component", "interpretation": "The current nested value matches the exact
    stock recipe on the provider-declared 1000 ml stock basis. This existing partial
    repair is credited; stock membership is still incomplete. Listed vitamin-stock
    water alone is not independently measured final volume. The claim remains a stock
    value, not a receiving-medium concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q120", "subject": "Vitamin B12", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path":
    "solutions[2].composition[3].concentration", "original": {"value": "0.001", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "properly nested stock component",
    "interpretation": "The current nested value matches the exact stock recipe on
    the provider-declared 1000 ml stock basis. This existing partial repair is credited;
    stock membership is still incomplete. Listed vitamin-stock water alone is not
    independently measured final volume. The claim remains a stock value, not a receiving-medium
    concentration.", "sources": [{"locator": "$.data.solutions[2].recipe[7]", "source_key":
    "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818", "source_raw_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "source_text_sha256":
    "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb", "accessed_at":
    "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q121", "subject":
    "Wolin''s vitamin solution (10x) candidate addition", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "solutions[2].concentration_candidates",
    "original": [{"value": "1", "unit": "ML_PER_L", "basis": "CROSS_MEDIUM_INFERENCE",
    "support": "This record is a variant of medium 818 (KOMODO key ''818.1''); volume
    read from base medium 818 (''CHRYSIOGENES MEDIUM'').", "counterevidence": "The
    variant''s own recipe was never read — only base medium 818''s — so the modification
    may change this volume. A stock''s addition volume varies by citing medium: MediaDive
    medium 142 adds ''Trace element solution (Vishniac & Santer)'' at 0.2 ml and medium
    69 adds the same stock at 5 ml.", "proposed_by": "apply_cocktail_nesting.py"}]}],
    "decision": "evidence_only", "stage": "preserved cross-medium candidate", "interpretation":
    "The variant deliberately retains an unasserted candidate. Current DSM 818 explicitly
    identifies the DSM 16346 branch and its modifications, but the unavailable KOMODO
    route remains a separate identity limit. Do not automatically promote this proposed
    per-litre denominator.", "sources": [{"locator": "$.data.solutions[0].recipe[11]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    12,\n                        \"solution\": \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 28-29", "source_key": "dsmz818",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium818.pdf",
    "source_raw_sha256": "80e835e34cfca164a2680f91143dfff16499f967959f1d8638056a8715922b08",
    "source_text_sha256": "7e322aab7537509fa2a7eec7b97eea7dfe3684d8ed2becfbdaf580e61d0e2b1c",
    "accessed_at": "2026-10-28T09:30:23.316471Z", "exact_source_quote": "For DSM 16346:
    Supplement medium with 0.80 g/l yeast extract and replace Na-acetate\nwith 1.10
    g/l Na-L-lactate.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q122", "subject": "Main sol. 818 water", "local_fields": [], "decision": "evidence_only",
    "stage": "source-only solvent/basis", "interpretation": "Preserve 1000 ml water
    in this named recipe, separately from its stock additions. Only SL11 additionally
    has an explicit instruction to bring the stock to 1000 ml; do not promote listed
    water in other sections to a measured final-medium volume.", "sources": [{"locator":
    "$.data.solutions[0].recipe[14]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q123", "subject": "Trace element solution
    SL-11 water", "local_fields": [], "decision": "evidence_only", "stage": "source-only
    solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe,
    separately from its stock additions. Only SL11 additionally has an explicit instruction
    to bring the stock to 1000 ml; do not promote listed water in other sections to
    a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[1].recipe[9]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q124", "subject": "Wolin''s vitamin solution
    (10x) water", "local_fields": [], "decision": "evidence_only", "stage": "source-only
    solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe,
    separately from its stock additions. Only SL11 additionally has an explicit instruction
    to bring the stock to 1000 ml; do not promote listed water in other sections to
    a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[2].recipe[10]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q125", "subject": "Seven vitamins solution
    water", "local_fields": [], "decision": "evidence_only", "stage": "source-only
    solvent/basis", "interpretation": "Preserve 1000 ml water in this named recipe,
    separately from its stock additions. Only SL11 additionally has an explicit instruction
    to bring the stock to 1000 ml; do not promote listed water in other sections to
    a measured final-medium volume.", "sources": [{"locator": "$.data.solutions[3].recipe[7]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q126", "subject": "Complete three stock
    memberships", "local_fields": [], "decision": "evidence_only", "stage": "source-only
    missing structure", "interpretation": "SL11 has nine compounds, Wolin ten and
    seven-vitamin stock seven. Current owners nest only 1/4/5 of these respectively,
    leaving the remainder flat; generated target has no nested stocks. Completing
    the stocks must move, not duplicate, all corresponding rows and preserve each
    stock water and receiving dose.", "sources": [{"locator": "$.data.solutions[1]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                \"id\":
    1474,\n                \"name\": \"Trace element solution SL-11\",\n                \"volume\":
    1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Na2-EDTA x 2 H2O\",\n                        \"compound_id\":
    676,\n                        \"amount\": 5.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5.2,\n                        \"mmol_l\":
    15.4667,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\":
    260,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    7.54482,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\":
    64,\n                        \"amount\": 70,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\":
    0.513573,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\":
    36,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.505293,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\":
    37,\n                        \"amount\": 6,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\":
    0.0970246,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\":
    38,\n                        \"amount\": 190,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\":
    1.46335,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\":
    39,\n                        \"amount\": 2,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\":
    0.0117314,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\":
    40,\n                        \"amount\": 24,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\":
    0.185187,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\":
    9,\n                        \"amount\": 36,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\":
    0.148791,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Dissolve EDTA in
    800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0 and bring volume to 1000 ml. \"\n                    }\n                ]\n            }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[2]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                \"id\":
    5980,\n                \"name\": \"Wolin''s vitamin solution (10x)\",\n                \"volume\":
    1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\":
    46,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\":
    138,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0453104,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.486287,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\":
    1207,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.148236,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\":
    136,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.132837,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.406141,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\":
    1512,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.209846,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 1,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\":
    0.00073779,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.364591,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\":
    252,\n                        \"amount\": 50,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\":
    0.24233,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ]\n            }",
    "quote_representation": "raw JSON object"}, {"locator": "$.data.solutions[3]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                \"id\":
    1038,\n                \"name\": \"Seven vitamins solution\",\n                \"volume\":
    1000,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\":
    18,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.073779,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\":
    47,\n                        \"amount\": 80,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.08,\n                        \"mmol_l\":
    0.583345,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"D-(+)-biotin\",\n                        \"compound_id\":
    1359,\n                        \"amount\": 20,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\":
    0.0818632,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\":
    139,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    1.62456,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Calcium pantothenate\",\n                        \"compound_id\":
    518,\n                        \"amount\": 100,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\":
    0.209849,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\":
    519,\n                        \"amount\": 300,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.3,\n                        \"mmol_l\":
    1.45886,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thiamine-HCl x 2 H2O\",\n                        \"compound_id\":
    77,\n                        \"amount\": 200,\n                        \"unit\":
    \"mg\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.535761,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ]\n            }",
    "quote_representation": "raw JSON object"}]}, {"decision_id": "q127", "subject":
    "Base anoxic preparation and final pH", "local_fields": [{"record_path": "data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml",
    "field_path": "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path":
    "data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml", "field_path":
    "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "ph_range", "original": {"min": 7.4, "max": 7.8}}, {"record_path":
    "data/normalized_yaml/bacterial/for_dsm_16346.yaml", "field_path": "ph_range",
    "original": {"min": 7.4, "max": 7.8}}, {"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Dissolve ingredients
    except bicarbonate, nitrate, vitamins and acetate. Sparge medium with 100% N2
    gas for 30 - 45 min to make it anoxic, adjust pH to 7.0 - 7.4, then dispense under
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add nitrate, vitamins and acetate from sterile anoxic stock solutions prepared
    under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared
    under 80% N2 and 20% CO2 gas atmosphere. Vitamins should be sterilized by filtration.
    The pH of the complete medium should be adjusted to 7.4 - 7.8, if necessary."}],
    "decision": "evidence_only", "stage": "main preparation versus missing copied
    preparation", "interpretation": "The final 7.4–7.8 range and full DSM owner prose
    agree with the primary. Preserve 30–45 min nitrogen treatment, pre-autoclave pH
    7.0–7.4, separate nitrate/vitamin/acetate stocks, distinct bicarbonate gas and
    filtered vitamins. The generated and KOMODO layers omit that preparation and their
    Aerobic: Yes notes contradict this base prescription.", "sources": [{"locator":
    "$.data.solutions[0].steps[0]", "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve ingredients except bicarbonate, nitrate, vitamins and acetate. Sparge
    medium with 100% N2 gas for 30 - 45 min to make it anoxic, adjust pH to 7.0 -
    7.4, then dispense under same gas atmosphere into anoxic Hungate-type tubes or
    serum vials and autoclave. Add nitrate, vitamins and acetate from sterile anoxic
    stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Vitamins should
    be sterilized by filtration. The pH of the complete medium should be adjusted
    to 7.4 - 7.8, if necessary.\"\n                    }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q128", "subject": "SL11 stock pH and solvent
    preparation", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chrysiogenes_medium.yaml",
    "field_path": "preparation_steps[1].description", "original": "Dissolve EDTA in
    800 ml distilled water, adjust pH to 7 using 2 N NaOH and add ferrous chloride.
    After ferrous chloride has dissolved add other compounds. Finally adjust pH to
    6.0 and bring volume to 1000 ml."}], "decision": "evidence_only", "stage": "stock-specific
    preparation", "interpretation": "Preserve EDTA in 800 ml, pH 7 using 2 N NaOH,
    ferrous then remaining compounds, final pH 6 and bring to 1000 ml as the SL11
    stock procedure. Root-list placement must not turn this into a main-medium pH
    6 instruction. The supplied compounds remain hydrated forms despite several provider
    mmol_l values using different molar masses.", "sources": [{"locator": "$.data.solutions[1].steps[0]",
    "source_key": "api818", "reference": "https://mediadive.dsmz.de/rest/medium/818",
    "source_raw_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "source_text_sha256": "5b20ae6fc000b01d026c450f28e9ad1be96c62851fa021919202d270c6b66aeb",
    "accessed_at": "2026-10-28T09:30:23.292920Z", "exact_source_quote": "{\n                        \"step\":
    \"Dissolve EDTA in 800 ml distilled water, adjust pH to 7 using 2 N NaOH and add
    ferrous chloride. After ferrous chloride has dissolved add other compounds. Finally
    adjust pH to 6.0 and bring volume to 1000 ml. \"\n                    }", "quote_representation":
    "raw JSON object"}]}], "local_field_census_reference": "REVIEW_WORK/batch062/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml: primary 33/33, secondary
    30/33; data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml: primary
    27/27, secondary 24/27; data/normalized_yaml/bacterial/chrysiogenes_medium.yaml:
    primary 27/27, secondary 24/27; data/normalized_yaml/bacterial/for_dsm_16346.yaml:
    primary 27/27, secondary 24/27. These are ingredient-instance linkage fractions,
    not accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    4 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:006543
  evidence_ids:
  - grounding
- assessment_id: a5
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:006543
  evidence_ids:
  - local0
- assessment_id: a6
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:006543
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006543-stock-flattening-and-stale-sums
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Partial stock repair is missing from the generated recipe
  description: The generated target still flattens all stock components and sums four
    distinct vitamin-stock pairs. Maintained owners correctly restore ten nested stock
    rows, but sixteen stock components remain direct ingredients and the receiving
    ML_PER_L basis is not independently established. Stock values must not be treated
    as final-medium values.
  target_ids:
  - CultureMech:006543
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - dsmz818
  - api818
  rule_id: P2.3
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-006543-strain-branch-and-preparation-loss
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The copied DSM 16346 branch lacks its explicit modifications
  description: Current DSM 818 prescribes yeast extract and lactate replacement for
    DSM 16346; its owner retains base acetate and says components are preserved. The
    generated record still calls the branch a duplicate. The current repair script
    changes topology against a hardcoded copied signature without implementing this
    prescription.
  target_ids:
  - CultureMech:006543
  field_paths:
  - merged_from
  - variant_children
  - parent_media
  - variant_relationship
  - data/normalized_yaml/bacterial/for_dsm_16346.yaml::ingredients[10].concentration
  evidence_ids:
  - dsmz818
  - local3
  rule_id: review-yaml-record/source-variant-identity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the asserted strain/source
    equivalence conflicts with the primary variant prescription; this custom rule
    does not claim native P2.1 invalid-ID semantics.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-006543-anoxic-preparation-and-stage-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Anoxic preparation and stock controls are absent from copied layers
  description: 'The DSM owner retains correct main and SL11 preparation, while the
    target and KOMODO owners omit those instructions and carry Aerobic: Yes. SL11
    pH 6 belongs to the stock, not the main medium. None of the selected layers attaches
    claim-level formulation evidence.'
  target_ids:
  - CultureMech:006543
  field_paths:
  - notes
  - preparation_steps
  - evidence
  - data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml::notes
  - data/normalized_yaml/bacterial/for_dsm_16346.yaml::notes
  evidence_ids:
  - dsmz818
  - api818
  rule_id: review-yaml-record/preparation-and-atmosphere-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major under this custom rule because omitted
    preparation and contradictory atmosphere metadata materially misrepresent the
    source; this is not attributed to the native concentration-mismatch rule.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-006543-chemical-form-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium resazurin have mismatched chemical forms
  description: Nickel chloride hexahydrate is linked to anhydrous CHEBI:34887 in both
    slots. Sodium resazurin has only a primary CHEBI:8806 neutral-form link. Correct
    copper, cobalt, manganese and magnesium hydrates are credited; D-calcium pantothenate
    is supported by the current CHEBI:31345 stereochemical object, while generic stock
    pantothenate remains source-specific.
  target_ids:
  - CultureMech:006543
  field_paths:
  - data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml::ingredients[18].term
  - data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml::ingredients[18].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/chrysiogenes_medium.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/for_dsm_16346.yaml::ingredients[17].term
  - data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/chrysiogenes_medium.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/normalized_yaml/bacterial/for_dsm_16346.yaml::ingredients[17].mediaingredientmech_chebi_term
  - data/merge_yaml/merged/CHRYSIOGENES_MEDIUM.yaml::ingredients[7].term
  - data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml::ingredients[7].term
  - data/normalized_yaml/bacterial/chrysiogenes_medium.yaml::ingredients[7].term
  - data/normalized_yaml/bacterial/for_dsm_16346.yaml::ingredients[7].term
  evidence_ids:
  - dsmz818
  - chebi34887
  - chebi8806
  - chebi31345
  - grounding
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the asserted chemical forms
    conflict with supplied hydrate or sodium-salt identity; this custom rule does
    not claim native P2.1 invalid-ID semantics.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-006543-legacy-link-and-history-traceability
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy nitrate links and malformed timestamps remain
  description: Four selected nitrate secondary links use legacy MediaIngredientMech:000170,
    absent from the current packaged exact-ID index; their primary CHEBI:63043 is
    correct. KOMODO original timestamps contain literal .fZ. Current source bytes
    authenticate historical API excerpts but not the separate catalogue or past execution.
  target_ids:
  - CultureMech:006543
  field_paths:
  - ingredients[9].mediaingredientmech_term
  - data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml::curation_history[0].timestamp
  - data/normalized_yaml/bacterial/for_dsm_16346.yaml::curation_history[0].timestamp
  evidence_ids:
  - grounding
  - chebi63043
  - history-auth
  rule_id: P3.2
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Complete all three stocks in the maintained owners from their exact
    source sections, retain source batch amounts and explicit denominator limits,
    preserve repaired nested values and candidates, then regenerate through the conservative
    merge path.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006543
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action2
  description: Keep the base and strain branch distinct; reconcile the exact current
    primary modifications and uncertain KOMODO provenance. Review repair_parent/repair_child
    and Child.modification so future repairs do not enforce the old copied signature.
    Preserve historical events and append a new verified corrective event.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006543
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action3
  description: Preserve the DSM owner preparation, assign each instruction to its
    correct stage, reconcile copied aerobic metadata, and attach scoped root evidence
    for preparation and stock additions plus ingredient evidence for mass claims.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006543
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action4
  description: Resolve the supplied hydrate and sodium-salt mappings against authoritative
    ontology and MIM, retaining exact source forms and unresolved mappings where needed.
    Do not change doses through anhydrous molecular-weight inference.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006543
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
- action_id: action5
  description: Review the current valid nitrate correspondence without declaring historical
    invalidity. Preserve malformed original events unchanged; append an evidence-supported
    context or correction event with the actual current curation date, and fix the
    timestamp writer for future output.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006543
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chrysiogenes_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/for_dsm_16346.yaml
    role: maintained normalized contributor
  generator: Review the relevant inspected maintained writer and repair normalized
    inputs, then regenerate the generated target through the current conservative
    merge path. Do not hand-edit generated YAML.
  acceptance_checks:
  - Compare exact source identity, supplied form, amount, unit, denominator and preparation
    stage for every changed claim; preserve all correct current fields and old evidence.
  - Attach claim-scoped source excerpts and references; rerun the four canonical checks
    on changed maintained inputs and inspect regenerated output for freshness.
limitations:
- Exact historical KOMODO 818 and 818.1 routes returned HTTP 403; current DSM 818
  supplies a direct DSM 16346 prescription but does not authenticate the inaccessible
  KOMODO pages.
- Provider1003 ml normalization is documented but not a measured final volume; stock
  liquid additions and vitamin-stock listed water retain explicit basis limits.
- Current MIM absence of legacy MediaIngredientMech:000170 is a current-snapshot result,
  not proof of historical invalidity. No experimental growth measurement is asserted
  from a collection recipe.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
