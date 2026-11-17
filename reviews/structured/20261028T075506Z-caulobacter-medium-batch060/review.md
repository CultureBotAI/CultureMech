# Scientific review of caulobacter_medium

- Review: 20261028T075506Z-caulobacter-medium-batch060
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T07:42:13.966068Z
- Finished UTC: 2026-10-28T07:55:06.779116Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM 595 source rates and six attached owner claims are supported, but water is encoded as mass, one secondary hydrate link is stale, and a K31 paper observation is attached to an unverified parent formulation. Generated evidence/preparation loss and malformed provenance also require bounded curation.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch060 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006076 | data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml | generated | caulobacter_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006076 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:006076 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:006076 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:006076 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### Exact selected source identities and variant boundaries

identity: supported. Targets: CultureMech:006076.

DSM 595 and TOGO M2356 identify the same added-agar formulation; KOMODO 595 identity is represented by the retained historical mapping row and copied-DSM provenance, with current endpoint unavailable. Paper PYE/PYEGGR is a separate formulation, not a synonym of this group. The target remains specifically the DSM 595-derived solid record, not a generic Caulobacter recipe.

### Direct source claims and paper limitation

evidence: concern. Targets: CultureMech:006076.

All six attached API claims are current literal and hash matches; no such attached claims exist on the generated or TOGO layer. The catalogue identity excerpt does not support amounts. The two PMID claims accurately name K31 and its reported low-temperature observation but overextend that evidence to DSM 595. Only the paper abstract and full Methods3.1 were scientifically assessed.

### Seven historical reports and current code

provenance: concern. Targets: CultureMech:006076.

Seven complete reports and 12 current-equal historical API objects were read. Their current matching payload authenticates the quoted bytes, not historical retrieval time or catalogue access. The September recommendation to propagate K31 claims is not accepted without exact formulation evidence; its description of the merger is superseded by the current conservative guard. The October six accepted ingredient claims remain credited.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:006076.

All 20 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006076", "selected_concentration_field_count": 20, "selected_concentration_fields_covered": 20, "decisions": [{"decision_id": "q1", "subject": "Bacto peptone", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM 595 main recipe; solid branch for agar", "interpretation": "Current API 595 declares 2 g/L, matching these exact local rows. The two maintained owners each have a literal source object and the exact matching current raw SHA; credit all six attached claims independently. The listed water is not independently measured final volume; use the explicit provider rate with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\": 19,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Bacto peptone                               2.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Bacto peptone", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe; solid branch for agar", "interpretation": "Current API 595 declares 2 g/L, matching these exact local rows. These layers have no attached claim for the row; source support is available but is not transferred as though already present. The listed water is not independently measured final volume; use the explicit provider rate with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\": 19,\n                        \"amount\": 2,\n                        \"unit\": \"g\",\n                        \"g_l\": 2,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Bacto peptone                               2.0    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM 595 main recipe; solid branch for agar", "interpretation": "Current API 595 declares 0.2 g/L, matching these exact local rows. The two maintained owners each have a literal source object and the exact matching current raw SHA; credit all six attached claims independently. The listed water is not independently measured final volume; use the explicit provider rate with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "MgSO4 x 7 H2O                               0.2    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe; solid branch for agar", "interpretation": "Current API 595 declares 0.2 g/L, matching these exact local rows. These layers have no attached claim for the row; source support is available but is not transferred as though already present. The listed water is not independently measured final volume; use the explicit provider rate with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.2,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\": 0.811438,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "MgSO4 x 7 H2O                               0.2    g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "Agar", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "15", "unit": "G_PER_L"}}], "decision": "verified", "stage": "DSM 595 main recipe; solid branch for agar", "interpretation": "Current API 595 declares 15 g/L, matching these exact local rows. The two maintained owners each have a literal source object and the exact matching current raw SHA; credit all six attached claims independently. The primary explicitly gives 15 g/l agar for the solid branch selected here; no polymer molarity is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Add 15.0 g/l agar for solid medium.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "Agar", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "15", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "15", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe; solid branch for agar", "interpretation": "Current API 595 declares 15 g/L, matching these exact local rows. These layers have no attached claim for the row; source support is available but is not transferred as though already present. The primary explicitly gives 15 g/l agar for the solid branch selected here; no polymer molarity is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\": 15,\n                        \"unit\": \"g/l\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Add 15.0 g/l agar for solid medium.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Yeast extract and source qualifier", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe", "interpretation": "All four 1 G_PER_L rows match the explicit API rate and primary 1 g batch mass. API additionally names BD212750; this absent supplier attribute does not contradict the amount and should be recorded as source metadata, not converted to an invented defined compound.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"BD 212750\",\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Yeast extract                               1.0    g", "quote_representation": "captured extracted text"}, {"locator": "$.components[0].items[1]", "source_key": "togoM2356", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2356", "source_raw_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909", "source_text_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909", "accessed_at": "2026-10-28T07:43:05.720204Z", "exact_source_quote": "{\n          \"component_name\": \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\": \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\": \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q8", "subject": "Tap water", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "1000", "unit": "G_PER_L"}}], "decision": "correct", "stage": "absolute preparation solvent input", "interpretation": "All four layers assert 1000 G_PER_L. The primary and providers specify 1000 ml, with no g_l water value. Preserve the absolute solvent input without density conversion or a claimed measured final volume. The water ontology is not itself wrong.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\": 322,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Tap water                                1000.0   ml", "quote_representation": "captured extracted text"}, {"locator": "$.components[0].items[2]", "source_key": "togoM2356", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2356", "source_raw_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909", "source_text_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909", "accessed_at": "2026-10-28T07:43:05.720204Z", "exact_source_quote": "{\n          \"component_name\": \"Tap water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\": \"http://purl.jp/bio/10/gmo/GMO_001131\",\n          \"gmo_id\": \"GMO_001131\",\n          \"label\": \"Tap water\",\n          \"properties\": [\n            {\n              \"id\": \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\": \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\": \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\": \"Solvating media\"\n            }\n          ]\n        }", "quote_representation": "raw JSON object"}]}, {"decision_id": "q9", "subject": "Solid-medium agar preparation", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Add 15.0 g/l agar for solid medium."}], "decision": "verified", "stage": "conditional solid-medium preparation", "interpretation": "The maintained DSM owner already retains the exact instruction to add 15 g/l agar for solid medium. Credit it; the generated target and other owners lack the preparation step although their selected solid agar amounts agree.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"step\": \"Add 15.0 g/l agar for solid medium.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf", "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6", "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea", "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Add 15.0 g/l agar for solid medium.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "K31 doubling time", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "target_organisms[0].growth_metrics[0].doubling_time_minutes", "original": 2400.0}], "decision": "unsupported", "stage": "paper strain-specific observation; parent-medium link unresolved", "interpretation": "The paper supports about40 h for K31 at 4°C; 40×60=2400 min is correct. The precise value is approximate, and the attached placement asserts the DSM 595 parent without formulation evidence. Methods3.1 describes PYE/PYEGGR with calcium and a different magnesium basis, not this tap-water DSM 595 recipe. Do not promote the numeric agreement to a DSM 595 growth claim.", "sources": [{"locator": "extracted-text lines 259-259", "source_key": "pmc4221894", "reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4221894/", "source_raw_sha256": "40011880ed3d9aebab2647cf1cd70ba4729e7301262cb5027e7c4cfd4f0ce72c", "source_text_sha256": "fa47d1c3dd183d0b0ce211bb28f2a266e047655054db74a75ee553f4236a4900", "accessed_at": "2026-10-28T07:44:08.001108Z", "exact_source_quote": "Our experiments also revealed the ability for K31 to grow at 4°C with a doubling time of about 40 h.", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "K31 temperature and inline variant", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "target_organisms[0].growth_metrics[0].perturbations[0].level", "original": 4.0}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "variants[0].modifications", "original": ["Incubate at 4 C.", "Use Caulobacter sp. K31 as the target strain."]}], "decision": "unsupported", "stage": "paper observation and proposed parent variant", "interpretation": "The paper reports4°C and the taxon is correct, but the claim is not shown to be on DSM 595. Preserve the observation with its actual experimental context and uncertainty; neither the parent linkage nor the current BATCH label is authenticated solely by the abstract. Do not copy these claims into the generated target as if supported.", "sources": [{"locator": "extracted-text lines 259-259", "source_key": "pmc4221894", "reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4221894/", "source_raw_sha256": "40011880ed3d9aebab2647cf1cd70ba4729e7301262cb5027e7c4cfd4f0ce72c", "source_text_sha256": "fa47d1c3dd183d0b0ce211bb28f2a266e047655054db74a75ee553f4236a4900", "accessed_at": "2026-10-28T07:44:08.001108Z", "exact_source_quote": "Our experiments also revealed the ability for K31 to grow at 4°C with a doubling time of about 40 h.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch060/record05/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: concern. Targets: CultureMech:006076.

data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml: primary 3/5, secondary 3/5; data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml: primary 3/5, secondary 3/5; data/normalized_yaml/bacterial/caulobacter_medium.yaml: primary 3/5, secondary 3/5; data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml: primary 3/5, secondary 3/5. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:006076.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:006076.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Tap-water volume is encoded as a mass concentration

major / open / confirmed; issue key: culturemech-006076-water-volume-as-mass.

The target and all three maintained owners encode 1000 ml tap water as 1000 G_PER_L. The current primary and both providers supply a volume, not a mass concentration; a density or final-volume assumption is unnecessary and unsupported.

### f2: K31 paper evidence does not establish the DSM 595 growth variant

major / open / confirmed; issue key: culturemech-006076-paper-growth-misattributed-to-dsm595.

PMID25274120 and NCBITaxon366602 are correct, and 40 h corresponds to 2400 min. However Methods3.1 describes PYE/PYEGGR, including calcium and a different magnesium formulation. It does not establish the maintained DSM 595 cold-growth variant or parent growth metric. The generated target currently omits these owner claims; that omission must not be repaired by propagating an unsupported formulation link.

### f3: The TOGO secondary magnesium link remains anhydrous

minor / open / confirmed; issue key: culturemech-006076-togo-secondary-magnesium-hydrate-divergence.

The TOGO owner correctly names the heptahydrate and now uses primary CHEBI:31795, but its secondary CHEBI:32599 has MgSO4 without seven waters. The primary repair is credited; generated/other owners already use31795 in both slots. This is a bounded secondary mismatch, not a request to change the mass.

### f4: Generated content omits valid source evidence and preparation

major / open / confirmed; issue key: culturemech-006076-stale-generated-evidence-preparation.

The current DSM and KOMODO owners carry six valid API ingredient claims; the DSM owner also preserves the solid-agar step. The generated target has neither. The yeast BD212750 source attribute is absent from all selected layers. Current merge_formulation_evidence preserves compatible evidence and rejects incompatible scientific projections; present owners differ in notes, chemistry, preparation and paper assertions, so the old three-way output cannot be treated as current compatible consolidation.

### f5: Historical timestamps and KOMODO interpretation need bounded context

minor / open / confirmed; issue key: culturemech-006076-historical-time-and-komodo-provenance-limits.

The generated target and KOMODO owner retain the malformed literal timestamp2026-01-27T01:15:03.fZ and a timezone-free enrichment timestamp. Current importer code uses time.strftime with%f; the resolver uses naive datetime.now(). The exact current KOMODO route and catalogue return403, so Aerobic:No and the old catalogue digest remain unverified. Correcting time provenance must not rewrite old events.

## Recommended Actions And Acceptance Checks

### action1

Represent the source water as an absolute preparation input in each owner and remove the mass interpretation. Review the current importer Tap-water name path and its ml-to-per-litre fallback; preserve the four supported solute rates.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Reassess the K31 observation in its actual paper formulation and variant context, preserve the verified taxon and approximate40 h observation, and remove or qualify the unsupported DSM 595 linkage. Do not invent a replacement recipe or automatic growth assertion.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Align only the stale secondary supplied-form correspondence after current ontology/MIM review, preserving the correct primary and existing amount. The historical primary-only migration intentionally left the secondary slot unchanged.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action4

Repair and source-review maintained owners first, retaining valid attached claims and the agar instruction and adding the supplier detail where appropriate. Then use the current conservative merge path; do not force the former three-way group or propagate the unsupported paper claim.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action5

Preserve original events unchanged. Recover only evidence-backed context and append a new verified event with actual current curation time when correcting content; fix future writer timestamp formatting/timezone behavior. Keep unavailable KOMODO semantics qualified until the exact source is available.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/caulobacter_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local3 | data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch060/record05/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch060/record05/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch060/record05/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch060/record05/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz595 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api595 | https://mediadive.dsmz.de/rest/medium/595; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| togoM2356 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2356; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Current TOGO source identity, complete component paragraphs, units, stock references and comments read; exact primary collection source checked independently. Batch inputs and bare percentages are not silently normalized. |
| komodo595 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=595; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| komodoList | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| pmid25274120 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25274120%20AND%20SRC:MED&amp;format=json&amp;resultType=core; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Exact Europe PMC core metadata and abstract: PMID25274120, PMC4221894, DOI10.1098/rsob.140128, Ash et al. 2014. Bibliographic identity and abstract K31 statement checked; abstract alone does not identify DSM595 as the tested formulation. |
| tax366602 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=366602&amp;retmode=xml; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Full official taxonomy XML read: NCBITaxon366602 is Caulobacter sp. K31, with the stated bacterial lineage. Taxon identity does not establish growth on DSM595. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O']; mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of polysaccharides extracted from species of red algae. Its two main components are agarose and agaropectin. Agarose is the component responsible for the high-strength gelling properties of agar, while agaropectin provides the viscous properties.']; formula None; mass None; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S']; mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi32599 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| pmc4221894 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4221894/; Abstract and complete section 3.1 Media and growth conditions | supports | Exact PMC4221894 metadata, abstract and complete Methods3.1 read. K31 cold-growth and PYE/PYEGGR contexts are separated from DSM595. Other genomic results and experimental sections are outside this review. |
| grounding | REVIEW_WORK/batch060/record05/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/yaml_record_review/20260922T062119Z-CAULOBACTER_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history1 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/caulobacter_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api595 raw bytes exactly match the cited historical SHA, and 6 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_595_CAULOBACTER_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api595 raw bytes exactly match the cited historical SHA, and 6 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caulobacter_medium_add_agar.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caulobacter_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history6 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAULOBACTER_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch060/record05/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer29 | scripts/resolve_komodo_compositions.py; relevant functions named in summary | context_only | Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents copied ingredients/solutions but does not independently authenticate a particular past execution or variant. The underlying resolver is an inspected input and is assessed separately. |
| writer30 | src/culturemech/enrich/dsmz_resolver.py; relevant functions named in summary | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients, solutions, pH, physical state and medium type; it does not copy preparation or independently establish source equivalence. resolve_recipe skips already populated ingredient lists. Current behavior does not authenticate the historical enrichment execution. |
| writer31 | src/culturemech/import/komodo_web_importer.py; relevant functions named in summary | context_only | Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes and initially empty ingredients for later DSMZ enrichment; its strftime format uses literal %f. Read code does not authenticate the past table values or source-copy execution. |
| writer32 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition uses only the primary recipe and prefers provider g_l; it excludes a fixed list of solvent names, which does not include Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator check. _parse_preparation_steps retains source prose but cannot enforce conditional ingredient presence; historical execution is not inferred from present code. |
| writer33 | src/culturemech/import/togo_importer.py; relevant functions named in summary | context_only | Current _extract_primary_components/_solution_from_item preserve main versus nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps retains comments. Bare units mapped to per-litre enums still require source-basis review. Current fixed code is not proof of historical execution. |
| writer34 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer35 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer36 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| writer37 | scripts/apply_growth_evidence.py; relevant functions named in summary | context_only | Current apply_candidate appends candidate organism evidence, metrics and strain modifications from the supplied proposal; it does not independently retrieve or compare the cited experimental formulation. A candidate paper claim requires source/strain/medium review before application. |
| writer38 | scripts/curate_organism_culture_type.py; relevant functions named in summary | context_only | Current classify and apply_value use named strains and community signals to set isolate/community metadata; that classification cannot authenticate medium-specific growth claims. |
| writer39 | scripts/migrate_mgso4_heptahydrate_term.py; relevant functions named in summary | context_only | iter_ingredients and main make a label-conditional primary-term-only 32599 to 31795 repair; secondary annotations are untouched. The current primary is credited while stale secondary linkage requires separate review. |
| inspection-addendum-inspect | REVIEW_WORK/batch060/record05/inspection-addendum-current-writers/inspect.json; entire JSON | context_only | Append-only native inspection adds exact current MgSO4 migration, growth-evidence application and culture-type writers. Original inputs and canonical results are preserved. |
| inspection-addendum-lineage | REVIEW_WORK/batch060/record05/inspection-addendum-current-writers/lineage.json; entire JSON | context_only | Append-only native inspection adds exact current MgSO4 migration, growth-evidence application and culture-type writers. Original inputs and canonical results are preserved. |
| inspection-addendum-result | REVIEW_WORK/batch060/record05/inspection-addendum-current-writers/result.json; entire JSON | context_only | Append-only native inspection adds exact current MgSO4 migration, growth-evidence application and culture-type writers. Original inputs and canonical results are preserved. |
| attached-claims | REVIEW_WORK/batch060/record05/attached-claim-audit.json; claims and other_claims | supports | All nine actual attached claims classified: six independently authenticated API literals/digests, separate catalogue identity, and two paper claims with unsupported DSM595 linkage. |
| quantity-inventory | REVIEW_WORK/batch060/record05/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- Current KOMODO 595 and the exact catalogue route return403. Their older mapping row is retained as identity context, not newly authenticated historical full-catalogue bytes or atmosphere guidance.
- The primary lists water input rather than measured final volume. Explicit API rates are credited with that separate provenance; no water density or agar molarity is inferred.
- The paper abstract and complete Methods3.1 were read, not the entire genomic study. Verified K31 taxonomy and 40 h-to 2400 min arithmetic do not establish DSM 595 as the tested medium.
- No pH, sterilization, incubation temperature or atmosphere is supplied by the DSM 595 primary; no generic default is invented.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T075506Z-caulobacter-medium-batch060
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of caulobacter_medium
started_at: '2026-10-28T07:42:13.966068Z'
finished_at: '2026-10-28T07:55:06.779116Z'
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
summary: DSM 595 source rates and six attached owner claims are supported, but water
  is encoded as mass, one secondary hydrate link is stale, and a K31 paper observation
  is attached to an unverified parent formulation. Generated evidence/preparation
  loss and malformed provenance also require bounded curation.
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
  - path: data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
    sha256: 73c2e7034b1effe92266d489c696898c747081400047f0897aaf420bfc707de3
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    sha256: 7de6ae7976778f784205c2a53ec2629df407f5f17111a786fb3820209e5880d0
    role: context
  - path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    sha256: 60aed6eeb007c37424d5da4d5286c372ab137dfc8ffec161d45cfd36f308325a
    role: context
  - path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    sha256: 8dc33c071d0b66979d80772f54f71941c31a947ca10493e83b04f8541e102564
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_595_CAULOBACTER_medium.yaml.md
    sha256: 8d9b33c344c93b7a5a0c835ad262837d351e5e7944d9ff107ab90b1541912bf3
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/caulobacter_medium.yaml.md
    sha256: 81b4efabf42f0009c3dd5cca6d978f3bc4ac5b140ac3b29b28abc20274b1d928
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAULOBACTER_MEDIUM.md
    sha256: 19fda7a67a2e54e639a27fbcd6aa84821fe38c9bf0121ec927e69a61a0d51c0a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.md
    sha256: fb2ec30d7b5ce9c5cfd52f5a76fa74f7a559fda1585b6532706289e67e485c90
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caulobacter_medium.md
    sha256: 4326a1295f8c31b7ae261d3e0e5fa3e68cec69383c57b807996870742f6f164a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caulobacter_medium_add_agar.md
    sha256: 61eb9041195babe20a7a140dc3c292447f68096ed2f4bd5dd7a574d116c06680
    role: context
  - path: reports/yaml_record_review/20260922T062119Z-CAULOBACTER_MEDIUM.md
    sha256: 89450bab298569bb856777831fe947d9385ba0fb9897de8c5b137af4b164cdce
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_growth_evidence.py
    sha256: 5aabe2ad3a82ecdc82436979d4d60f396294c9e6ee905a9ff2800d2b8b35d754
    role: context
  - path: scripts/curate_organism_culture_type.py
    sha256: 8686de3d3736eaaf3702e2009a299a53819a5ba321966ab2ea01104538ca6a65
    role: context
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
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
scope:
  description: Full selected target and maintained owners, every quantity and unchanged
    claim; separately scoped source dependencies and current writers.
  selection: Authoritative batch060 selection index 5 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006076
targets:
- target_id: CultureMech:006076
  path: data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
  label: caulobacter_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006076
  command: just validate-schema data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006076
  command: just validate-strict data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch060/record05/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:006076
  command: just validate-terms data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:006076
  command: just validate-references data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:55:06.768922Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 73c2e7034b1effe92266d489c696898c747081400047f0897aaf420bfc707de3
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:55:06.769084Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 7de6ae7976778f784205c2a53ec2629df407f5f17111a786fb3820209e5880d0
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/caulobacter_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:55:06.769112Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 60aed6eeb007c37424d5da4d5286c372ab137dfc8ffec161d45cfd36f308325a
- evidence_id: local3
  kind: record_content
  reference: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T07:55:06.769134Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 8dc33c071d0b66979d80772f54f71941c31a947ca10493e83b04f8541e102564
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch060/record05/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:14.988956Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 030f12af14a6cfa15d7ab18cba12b2d420f26021f0cccc08a169b217424ced29
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch060/record05/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:15.986998Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: 3d31df43aac666aa404c220d50f3c728f924b3cab561325dbd47677a37996adc
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch060/record05/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:17.056592Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: bd501e808df544d3f97325426a3bc82df1e22f3d97bc1bcd793e03271d7edcb3
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch060/record05/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T07:42:17.728218Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: ba7b1bf26b512f4ca8241dbf118e279b7097f38c4a91fdf548601bdabf058e05
- evidence_id: dsmz595
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:05.391560Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6
- evidence_id: api595
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/595
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:05.391620Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00
- evidence_id: togoM2356
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2356
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:05.720204Z'
  support: supports
  summary: Current TOGO source identity, complete component paragraphs, units, stock
    references and comments read; exact primary collection source checked independently.
    Batch inputs and bare percentages are not silently normalized.
  snapshot_sha256: 1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909
- evidence_id: komodo595
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=595
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:05.944782Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: 5f1487255ab7307e0bbe3605e227ea5af1b00e479e502b609b48f3647e38c163
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:05.944854Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: eb922ebc33f93139d313a2443cdc23da70f97ba5964d1b9ab7b9f40c18058171
- evidence_id: pmid25274120
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25274120%20AND%20SRC:MED&format=json&resultType=core
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:05.959320Z'
  support: supports
  summary: 'Exact Europe PMC core metadata and abstract: PMID25274120, PMC4221894,
    DOI10.1098/rsob.140128, Ash et al. 2014. Bibliographic identity and abstract K31
    statement checked; abstract alone does not identify DSM595 as the tested formulation.'
  snapshot_sha256: fbed6c8b296aae0f331ad416093e9eab85dc79b76e10e23d4ada852133983fda
- evidence_id: tax366602
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=366602&retmode=xml
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T07:43:06.066725Z'
  support: supports
  summary: 'Full official taxonomy XML read: NCBITaxon366602 is Caulobacter sp. K31,
    with the stated bacterial lineage. Taxon identity does not establish growth on
    DSM595.'
  snapshot_sha256: 054add0a8c9e2714f3a149c82f7185907bff03622b01a2d9787a54e40369c001
- evidence_id: chebi15377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:06.087872Z'
  support: supports
  summary: OLS current exact CHEBI:15377 = water; definition ['An oxygen hydride consisting
    of an oxygen atom that is covalently bonded to two hydrogen atoms']; formula ['H2O'];
    mass ['18.015']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:06.092961Z'
  support: supports
  summary: OLS current exact CHEBI:2509 = agar; definition ['A complex mixture of
    polysaccharides extracted from species of red algae. Its two main components are
    agarose and agaropectin. Agarose is the component responsible for the high-strength
    gelling properties of agar, while agaropectin provides the viscous properties.'];
    formula None; mass None; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:06.340331Z'
  support: supports
  summary: OLS current exact CHEBI:31795 = magnesium sulfate heptahydrate; definition
    ['A hydrate that is the heptahydrate form of magnesium sulfate.']; formula ['7H2O.Mg.O4S'];
    mass ['246.473']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi32599
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32599
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T07:43:06.388158Z'
  support: supports
  summary: OLS current exact CHEBI:32599 = magnesium sulfate; definition ['A magnesium
    salt having sulfate as the counterion.']; formula ['Mg.O4S']; mass ['120.368'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 5da4e37c63d52d06c19a75da5c03a8ba42e81db8b537a053285d895de8f2b9ff
- evidence_id: pmc4221894
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4221894/
  locator: Abstract and complete section 3.1 Media and growth conditions
  accessed_at: '2026-10-28T07:44:08.001108Z'
  support: supports
  summary: Exact PMC4221894 metadata, abstract and complete Methods3.1 read. K31 cold-growth
    and PYE/PYEGGR contexts are separated from DSM595. Other genomic results and experimental
    sections are outside this review.
  snapshot_sha256: 40011880ed3d9aebab2647cf1cd70ba4729e7301262cb5027e7c4cfd4f0ce72c
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch060/record05/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T07:55:06.771886Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 7cc5b014e45e379caf316df38bc755f45678e7dd4d0d65335b6729f09716ffd2
- evidence_id: history0
  kind: prior_review
  reference: reports/yaml_record_review/20260922T062119Z-CAULOBACTER_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772670Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 89450bab298569bb856777831fe947d9385ba0fb9897de8c5b137af4b164cdce
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/caulobacter_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772697Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api595 raw bytes exactly match the cited historical SHA, and 6
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 81b4efabf42f0009c3dd5cca6d978f3bc4ac5b140ac3b29b28abc20274b1d928
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_595_CAULOBACTER_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772720Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api595 raw bytes exactly match the cited historical SHA, and 6
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 8d9b33c344c93b7a5a0c835ad262837d351e5e7944d9ff107ab90b1541912bf3
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772739Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: fb2ec30d7b5ce9c5cfd52f5a76fa74f7a559fda1585b6532706289e67e485c90
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caulobacter_medium_add_agar.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772757Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 61eb9041195babe20a7a140dc3c292447f68096ed2f4bd5dd7a574d116c06680
- evidence_id: history5
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caulobacter_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772775Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 4326a1295f8c31b7ae261d3e0e5fa3e68cec69383c57b807996870742f6f164a
- evidence_id: history6
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAULOBACTER_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T07:55:06.772794Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 19fda7a67a2e54e639a27fbcd6aa84821fe38c9bf0121ec927e69a61a0d51c0a
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch060/record05/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T07:55:06.772814Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: e45793762e288db61cb47ea94fd3884da1266229a006d9ba6ac2e9b921d36f8c
- evidence_id: writer29
  kind: record_content
  reference: scripts/resolve_komodo_compositions.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772834Z'
  support: context_only
  summary: 'Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment
    to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents
    copied ingredients/solutions but does not independently authenticate a particular
    past execution or variant. The underlying resolver is an inspected input and is
    assessed separately.'
  snapshot_sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
- evidence_id: writer30
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772856Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients, solutions,
    pH, physical state and medium type; it does not copy preparation or independently
    establish source equivalence. resolve_recipe skips already populated ingredient
    lists. Current behavior does not authenticate the historical enrichment execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer31
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772877Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes
    and initially empty ingredients for later DSMZ enrichment; its strftime format
    uses literal %f. Read code does not authenticate the past table values or source-copy
    execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer32
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772904Z'
  support: context_only
  summary: Current _parse_api_composition uses only the primary recipe and prefers
    provider g_l; it excludes a fixed list of solvent names, which does not include
    Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator
    check. _parse_preparation_steps retains source prose but cannot enforce conditional
    ingredient presence; historical execution is not inferred from present code.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer33
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772932Z'
  support: context_only
  summary: Current _extract_primary_components/_solution_from_item preserve main versus
    nested stocks; _parse_unit distinguishes mg/ml and _extract_preparation_steps
    retains comments. Bare units mapped to per-litre enums still require source-basis
    review. Current fixed code is not proof of historical execution.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: writer34
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772950Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer35
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772970Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer36
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.772989Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer37
  kind: record_content
  reference: scripts/apply_growth_evidence.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.773010Z'
  support: context_only
  summary: Current apply_candidate appends candidate organism evidence, metrics and
    strain modifications from the supplied proposal; it does not independently retrieve
    or compare the cited experimental formulation. A candidate paper claim requires
    source/strain/medium review before application.
  snapshot_sha256: 5aabe2ad3a82ecdc82436979d4d60f396294c9e6ee905a9ff2800d2b8b35d754
- evidence_id: writer38
  kind: record_content
  reference: scripts/curate_organism_culture_type.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.773029Z'
  support: context_only
  summary: Current classify and apply_value use named strains and community signals
    to set isolate/community metadata; that classification cannot authenticate medium-specific
    growth claims.
  snapshot_sha256: 8686de3d3736eaaf3702e2009a299a53819a5ba321966ab2ea01104538ca6a65
- evidence_id: writer39
  kind: record_content
  reference: scripts/migrate_mgso4_heptahydrate_term.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T07:55:06.773046Z'
  support: context_only
  summary: iter_ingredients and main make a label-conditional primary-term-only 32599
    to 31795 repair; secondary annotations are untouched. The current primary is credited
    while stale secondary linkage requires separate review.
  snapshot_sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
- evidence_id: inspection-addendum-inspect
  kind: validation
  reference: REVIEW_WORK/batch060/record05/inspection-addendum-current-writers/inspect.json
  locator: entire JSON
  accessed_at: '2026-10-28T07:55:06.773074Z'
  support: context_only
  summary: Append-only native inspection adds exact current MgSO4 migration, growth-evidence
    application and culture-type writers. Original inputs and canonical results are
    preserved.
  snapshot_sha256: eec8a475a940707ae156f8fd45a7d82bb4a01d0c71b236988488480f58313b27
- evidence_id: inspection-addendum-lineage
  kind: validation
  reference: REVIEW_WORK/batch060/record05/inspection-addendum-current-writers/lineage.json
  locator: entire JSON
  accessed_at: '2026-10-28T07:55:06.773267Z'
  support: context_only
  summary: Append-only native inspection adds exact current MgSO4 migration, growth-evidence
    application and culture-type writers. Original inputs and canonical results are
    preserved.
  snapshot_sha256: 762aeadcc1b001b7ebea1193298b32234d531b5a03e59fd5f3a2739bb895601e
- evidence_id: inspection-addendum-result
  kind: validation
  reference: REVIEW_WORK/batch060/record05/inspection-addendum-current-writers/result.json
  locator: entire JSON
  accessed_at: '2026-10-28T07:55:06.773410Z'
  support: context_only
  summary: Append-only native inspection adds exact current MgSO4 migration, growth-evidence
    application and culture-type writers. Original inputs and canonical results are
    preserved.
  snapshot_sha256: 721579f1ba1ed958071a1beab91a7f2bf2876f839659213ba84f4d7c5c77c83f
- evidence_id: attached-claims
  kind: record_content
  reference: REVIEW_WORK/batch060/record05/attached-claim-audit.json
  locator: claims and other_claims
  accessed_at: '2026-10-28T07:55:06.778473Z'
  support: supports
  summary: 'All nine actual attached claims classified: six independently authenticated
    API literals/digests, separate catalogue identity, and two paper claims with unsupported
    DSM595 linkage.'
  snapshot_sha256: be8727c8db7556bb4c708b849897d2687b0fe05b107a6a17626eeb755092a3e8
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch060/record05/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T07:55:06.778976Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: b455107c83f9df14585df91a11cc1ea5fefb47b1d63b1706e8a9e6a39bfdb9d3
assessments:
- assessment_id: a1
  area: identity
  topic: Exact selected source identities and variant boundaries
  outcome: supported
  summary: DSM 595 and TOGO M2356 identify the same added-agar formulation; KOMODO
    595 identity is represented by the retained historical mapping row and copied-DSM
    provenance, with current endpoint unavailable. Paper PYE/PYEGGR is a separate
    formulation, not a synonym of this group. The target remains specifically the
    DSM 595-derived solid record, not a generic Caulobacter recipe.
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - dsmz595
  - api595
  - togoM2356
  - attached-claims
- assessment_id: a2
  area: evidence
  topic: Direct source claims and paper limitation
  outcome: concern
  summary: All six attached API claims are current literal and hash matches; no such
    attached claims exist on the generated or TOGO layer. The catalogue identity excerpt
    does not support amounts. The two PMID claims accurately name K31 and its reported
    low-temperature observation but overextend that evidence to DSM 595. Only the
    paper abstract and full Methods3.1 were scientifically assessed.
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - attached-claims
  - pmc4221894
  - pmid25274120
  - tax366602
- assessment_id: a3
  area: provenance
  topic: Seven historical reports and current code
  outcome: concern
  summary: Seven complete reports and 12 current-equal historical API objects were
    read. Their current matching payload authenticates the quoted bytes, not historical
    retrieval time or catalogue access. The September recommendation to propagate
    K31 claims is not accepted without exact formulation evidence; its description
    of the merger is superseded by the current conservative guard. The October six
    accepted ingredient claims remain credited.
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - history-auth
  - writer29
  - writer30
  - writer31
  - writer32
  - writer33
  - writer34
  - writer35
  - writer36
  - writer37
  - writer38
  - writer39
- assessment_id: a4
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 20 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:006076",
    "selected_concentration_field_count": 20, "selected_concentration_fields_covered":
    20, "decisions": [{"decision_id": "q1", "subject": "Bacto peptone", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "DSM 595 main recipe; solid branch
    for agar", "interpretation": "Current API 595 declares 2 g/L, matching these exact
    local rows. The two maintained owners each have a literal source object and the
    exact matching current raw SHA; credit all six attached claims independently.
    The listed water is not independently measured final volume; use the explicit
    provider rate with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595",
    "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\":
    19,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-4", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Bacto peptone                               2.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject":
    "Bacto peptone", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe; solid
    branch for agar", "interpretation": "Current API 595 declares 2 g/L, matching
    these exact local rows. These layers have no attached claim for the row; source
    support is available but is not transferred as though already present. The listed
    water is not independently measured final volume; use the explicit provider rate
    with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key":
    "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at":
    "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Bacto peptone\",\n                        \"compound_id\":
    19,\n                        \"amount\": 2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 4-4", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Bacto peptone                               2.0    g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "MgSO4 x 7 H2O", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "verified", "stage": "DSM 595 main recipe; solid branch
    for agar", "interpretation": "Current API 595 declares 0.2 g/L, matching these
    exact local rows. The two maintained owners each have a literal source object
    and the exact matching current raw SHA; credit all six attached claims independently.
    The listed water is not independently measured final volume; use the explicit
    provider rate with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595",
    "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.811438,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz595",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "MgSO4 x 7
    H2O                               0.2    g", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q4", "subject": "MgSO4 x 7 H2O", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "original": {"value": "0.2", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "0.2", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe; solid
    branch for agar", "interpretation": "Current API 595 declares 0.2 g/L, matching
    these exact local rows. These layers have no attached claim for the row; source
    support is available but is not transferred as though already present. The listed
    water is not independently measured final volume; use the explicit provider rate
    with provenance.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key":
    "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at":
    "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\":
    8,\n                        \"amount\": 0.2,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.2,\n                        \"mmol_l\":
    0.811438,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz595",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "MgSO4 x 7
    H2O                               0.2    g", "quote_representation": "captured
    extracted text"}]}, {"decision_id": "q5", "subject": "Agar", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "15", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path":
    "ingredients[4].concentration", "original": {"value": "15", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "DSM 595 main recipe; solid branch for agar",
    "interpretation": "Current API 595 declares 15 g/L, matching these exact local
    rows. The two maintained owners each have a literal source object and the exact
    matching current raw SHA; credit all six attached claims independently. The primary
    explicitly gives 15 g/l agar for the solid branch selected here; no polymer molarity
    is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at":
    "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\":
    15,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 9-9", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Add 15.0
    g/l agar for solid medium.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q6", "subject": "Agar", "local_fields": [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "15", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "15", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe; solid
    branch for agar", "interpretation": "Current API 595 declares 15 g/L, matching
    these exact local rows. These layers have no attached claim for the row; source
    support is available but is not transferred as though already present. The primary
    explicitly gives 15 g/l agar for the solid branch selected here; no polymer molarity
    is inferred.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key":
    "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at":
    "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"for solid medium\",\n                        \"amount\":
    15,\n                        \"unit\": \"g/l\",\n                        \"g_l\":
    15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 9-9", "source_key": "dsmz595", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Add 15.0
    g/l agar for solid medium.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q7", "subject": "Yeast extract and source qualifier", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "original": {"value": "1", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "1", "unit":
    "G_PER_L"}}], "decision": "evidence_only", "stage": "DSM 595 main recipe", "interpretation":
    "All four 1 G_PER_L rows match the explicit API rate and primary 1 g batch mass.
    API additionally names BD212750; this absent supplier attribute does not contradict
    the amount and should be recorded as source metadata, not converted to an invented
    defined compound.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key":
    "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595", "source_raw_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "source_text_sha256":
    "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00", "accessed_at":
    "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"BD 212750\",\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz595",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Yeast extract                               1.0    g",
    "quote_representation": "captured extracted text"}, {"locator": "$.components[0].items[1]",
    "source_key": "togoM2356", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2356",
    "source_raw_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909",
    "source_text_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909",
    "accessed_at": "2026-10-28T07:43:05.720204Z", "exact_source_quote": "{\n          \"component_name\":
    \"Yeast extract\",\n          \"volume\": 1,\n          \"unit\": \"g\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001003\",\n          \"gmo_id\": \"GMO_001003\",\n          \"label\":
    \"Yeast extract\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000042\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000042\",\n              \"label\":
    \"Nutrient source\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q8", "subject": "Tap water", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "original": {"value": "1000", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "1000", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "absolute preparation solvent input",
    "interpretation": "All four layers assert 1000 G_PER_L. The primary and providers
    specify 1000 ml, with no g_l water value. Preserve the absolute solvent input
    without density conversion or a claimed measured final volume. The water ontology
    is not itself wrong.", "sources": [{"locator": "$.data.solutions[0].recipe[3]",
    "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595",
    "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Tap water\",\n                        \"compound_id\":
    322,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz595",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Tap water                                1000.0   ml",
    "quote_representation": "captured extracted text"}, {"locator": "$.components[0].items[2]",
    "source_key": "togoM2356", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2356",
    "source_raw_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909",
    "source_text_sha256": "1f4d46ac6c1a969193fca6fb980526fa2a685f664b2017d8978bb70690145909",
    "accessed_at": "2026-10-28T07:43:05.720204Z", "exact_source_quote": "{\n          \"component_name\":
    \"Tap water\",\n          \"volume\": 1000,\n          \"unit\": \"ml\",\n          \"gmo\":
    \"http://purl.jp/bio/10/gmo/GMO_001131\",\n          \"gmo_id\": \"GMO_001131\",\n          \"label\":
    \"Tap water\",\n          \"properties\": [\n            {\n              \"id\":
    \"GMO_000047\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000047\",\n              \"label\":
    \"Undefined component\"\n            }\n          ],\n          \"roles\": [\n            {\n              \"id\":
    \"GMO_000044\",\n              \"uri\": \"http://purl.jp/bio/10/gmo/GMO_000044\",\n              \"label\":
    \"Solvating media\"\n            }\n          ]\n        }", "quote_representation":
    "raw JSON object"}]}, {"decision_id": "q9", "subject": "Solid-medium agar preparation",
    "local_fields": [{"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Add 15.0 g/l agar
    for solid medium."}], "decision": "verified", "stage": "conditional solid-medium
    preparation", "interpretation": "The maintained DSM owner already retains the
    exact instruction to add 15 g/l agar for solid medium. Credit it; the generated
    target and other owners lack the preparation step although their selected solid
    agar amounts agree.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api595", "reference": "https://mediadive.dsmz.de/rest/medium/595",
    "source_raw_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "source_text_sha256": "f6c063885e40e3c81ab6a7da9152809f6764b8d74801c443183b77f34eb08d00",
    "accessed_at": "2026-10-28T07:43:05.391620Z", "exact_source_quote": "{\n                        \"step\":
    \"Add 15.0 g/l agar for solid medium.\"\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz595",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium595.pdf",
    "source_raw_sha256": "f9701a6235ebabcecf853756b95dc782d05f1871610e1c7368146d0a5e2972a6",
    "source_text_sha256": "f7b4de5636cf50604390d0530519158c25b58f930b14d7e13c724dba8fdb2dea",
    "accessed_at": "2026-10-28T07:43:05.391560Z", "exact_source_quote": "Add 15.0
    g/l agar for solid medium.", "quote_representation": "captured extracted text"}]},
    {"decision_id": "q10", "subject": "K31 doubling time", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "target_organisms[0].growth_metrics[0].doubling_time_minutes",
    "original": 2400.0}], "decision": "unsupported", "stage": "paper strain-specific
    observation; parent-medium link unresolved", "interpretation": "The paper supports
    about40 h for K31 at 4°C; 40×60=2400 min is correct. The precise value is approximate,
    and the attached placement asserts the DSM 595 parent without formulation evidence.
    Methods3.1 describes PYE/PYEGGR with calcium and a different magnesium basis,
    not this tap-water DSM 595 recipe. Do not promote the numeric agreement to a DSM
    595 growth claim.", "sources": [{"locator": "extracted-text lines 259-259", "source_key":
    "pmc4221894", "reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4221894/",
    "source_raw_sha256": "40011880ed3d9aebab2647cf1cd70ba4729e7301262cb5027e7c4cfd4f0ce72c",
    "source_text_sha256": "fa47d1c3dd183d0b0ce211bb28f2a266e047655054db74a75ee553f4236a4900",
    "accessed_at": "2026-10-28T07:44:08.001108Z", "exact_source_quote": "Our experiments
    also revealed the ability for K31 to grow at 4°C with a doubling time of about
    40 h.", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q11", "subject": "K31 temperature and inline variant", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/caulobacter_medium.yaml", "field_path": "target_organisms[0].growth_metrics[0].perturbations[0].level",
    "original": 4.0}, {"record_path": "data/normalized_yaml/bacterial/caulobacter_medium.yaml",
    "field_path": "variants[0].modifications", "original": ["Incubate at 4 C.", "Use
    Caulobacter sp. K31 as the target strain."]}], "decision": "unsupported", "stage":
    "paper observation and proposed parent variant", "interpretation": "The paper
    reports4°C and the taxon is correct, but the claim is not shown to be on DSM 595.
    Preserve the observation with its actual experimental context and uncertainty;
    neither the parent linkage nor the current BATCH label is authenticated solely
    by the abstract. Do not copy these claims into the generated target as if supported.",
    "sources": [{"locator": "extracted-text lines 259-259", "source_key": "pmc4221894",
    "reference": "https://pmc.ncbi.nlm.nih.gov/articles/PMC4221894/", "source_raw_sha256":
    "40011880ed3d9aebab2647cf1cd70ba4729e7301262cb5027e7c4cfd4f0ce72c", "source_text_sha256":
    "fa47d1c3dd183d0b0ce211bb28f2a266e047655054db74a75ee553f4236a4900", "accessed_at":
    "2026-10-28T07:44:08.001108Z", "exact_source_quote": "Our experiments also revealed
    the ability for K31 to grow at 4°C with a doubling time of about 40 h.", "quote_representation":
    "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch060/record05/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a5
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: concern
  summary: 'data/merge_yaml/merged/CAULOBACTER_MEDIUM.yaml: primary 3/5, secondary
    3/5; data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml: primary
    3/5, secondary 3/5; data/normalized_yaml/bacterial/caulobacter_medium.yaml: primary
    3/5, secondary 3/5; data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml:
    primary 3/5, secondary 3/5. These are ingredient-instance linkage fractions, not
    accuracy scores. Solution terms are audited separately. Every actually asserted
    CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows.
    0 numeric legacy MediaIngredientMech mentions occur across the complete selected
    documents, with exact locators in the inventory; NNNNNN is a historical placeholder,
    not an ID. Complex commercial/product components are not forced to pure-compound
    IDs.'
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - grounding
- assessment_id: a6
  area: scope
  topic: Scope and source limits
  outcome: supported
  summary: Complete selected target and exact maintained owners reviewed. Dependencies
    transfer only their explicitly named stock subsection; unrelated parent media
    and source prescriptions are not growth evidence.
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - local0
- assessment_id: a7
  area: schema
  topic: Native structural checks
  outcome: supported
  summary: All four canonical commands passed once; strict schema TSV contains only
    its header and reference validation checked zero references on the generated target.
    This does not certify quantities or chemical forms.
  target_ids:
  - CultureMech:006076
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-006076-water-volume-as-mass
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Tap-water volume is encoded as a mass concentration
  description: The target and all three maintained owners encode 1000 ml tap water
    as 1000 G_PER_L. The current primary and both providers supply a volume, not a
    mass concentration; a density or final-volume assumption is unnecessary and unsupported.
  target_ids:
  - CultureMech:006076
  field_paths:
  - ingredients[3].concentration
  - data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml::ingredients[2].concentration
  evidence_ids:
  - dsmz595
  - api595
  - togoM2356
  rule_id: source-solvent-unit-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-006076-paper-growth-misattributed-to-dsm595
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: K31 paper evidence does not establish the DSM 595 growth variant
  description: PMID25274120 and NCBITaxon366602 are correct, and 40 h corresponds
    to 2400 min. However Methods3.1 describes PYE/PYEGGR, including calcium and a
    different magnesium formulation. It does not establish the maintained DSM 595
    cold-growth variant or parent growth metric. The generated target currently omits
    these owner claims; that omission must not be repaired by propagating an unsupported
    formulation link.
  target_ids:
  - CultureMech:006076
  field_paths:
  - data/normalized_yaml/bacterial/caulobacter_medium.yaml::variants[0]
  - data/normalized_yaml/bacterial/caulobacter_medium.yaml::target_organisms[0].growth_metrics[0]
  evidence_ids:
  - pmc4221894
  - pmid25274120
  - tax366602
  - local2
  rule_id: strain-formulation-evidence-scope
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-006076-togo-secondary-magnesium-hydrate-divergence
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The TOGO secondary magnesium link remains anhydrous
  description: The TOGO owner correctly names the heptahydrate and now uses primary
    CHEBI:31795, but its secondary CHEBI:32599 has MgSO4 without seven waters. The
    primary repair is credited; generated/other owners already use31795 in both slots.
    This is a bounded secondary mismatch, not a request to change the mass.
  target_ids:
  - CultureMech:006076
  field_paths:
  - data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml::ingredients[0].mediaingredientmech_chebi_term
  evidence_ids:
  - chebi31795
  - chebi32599
  - grounding
  rule_id: supplied-form-secondary-correspondence
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    role: maintained normalized contributor
- finding_id: f4
  issue_key: culturemech-006076-stale-generated-evidence-preparation
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Generated content omits valid source evidence and preparation
  description: The current DSM and KOMODO owners carry six valid API ingredient claims;
    the DSM owner also preserves the solid-agar step. The generated target has neither.
    The yeast BD212750 source attribute is absent from all selected layers. Current
    merge_formulation_evidence preserves compatible evidence and rejects incompatible
    scientific projections; present owners differ in notes, chemistry, preparation
    and paper assertions, so the old three-way output cannot be treated as current
    compatible consolidation.
  target_ids:
  - CultureMech:006076
  field_paths:
  - ingredients[*].evidence
  - preparation_steps
  - references
  - merged_from
  evidence_ids:
  - attached-claims
  - local0
  - local1
  - local2
  - local3
  - api595
  rule_id: generated-freshness-and-evidence-retention
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    role: maintained normalized contributor
- finding_id: f5
  issue_key: culturemech-006076-historical-time-and-komodo-provenance-limits
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Historical timestamps and KOMODO interpretation need bounded context
  description: The generated target and KOMODO owner retain the malformed literal
    timestamp2026-01-27T01:15:03.fZ and a timezone-free enrichment timestamp. Current
    importer code uses time.strftime with%f; the resolver uses naive datetime.now().
    The exact current KOMODO route and catalogue return403, so Aerobic:No and the
    old catalogue digest remain unverified. Correcting time provenance must not rewrite
    old events.
  target_ids:
  - CultureMech:006076
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  - notes
  - data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml::curation_history[0].timestamp
  evidence_ids:
  - komodo595
  - komodoList
  - local0
  - local1
  rule_id: historical-provenance-precision
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Represent the source water as an absolute preparation input in each
    owner and remove the mass interpretation. Review the current importer Tap-water
    name path and its ml-to-per-litre fallback; preserve the four supported solute
    rates.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006076
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
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
  description: Reassess the K31 observation in its actual paper formulation and variant
    context, preserve the verified taxon and approximate40 h observation, and remove
    or qualify the unsupported DSM 595 linkage. Do not invent a replacement recipe
    or automatic growth assertion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006076
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
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
  description: Align only the stale secondary supplied-form correspondence after current
    ontology/MIM review, preserving the correct primary and existing amount. The historical
    primary-only migration intentionally left the secondary slot unchanged.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006076
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
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
  description: Repair and source-review maintained owners first, retaining valid attached
    claims and the agar instruction and adding the supplier detail where appropriate.
    Then use the current conservative merge path; do not force the former three-way
    group or propagate the unsupported paper claim.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006076
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
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
  description: Preserve original events unchanged. Recover only evidence-backed context
    and append a new verified event with actual current curation time when correcting
    content; fix future writer timestamp formatting/timezone behavior. Keep unavailable
    KOMODO semantics qualified until the exact source is available.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:006076
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caulobacter_medium_add_agar.yaml
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
- Current KOMODO 595 and the exact catalogue route return403. Their older mapping
  row is retained as identity context, not newly authenticated historical full-catalogue
  bytes or atmosphere guidance.
- The primary lists water input rather than measured final volume. Explicit API rates
  are credited with that separate provenance; no water density or agar molarity is
  inferred.
- The paper abstract and complete Methods3.1 were read, not the entire genomic study.
  Verified K31 taxonomy and 40 h-to 2400 min arithmetic do not establish DSM 595 as
  the tested medium.
- No pH, sterilization, incubation temperature or atmosphere is supplied by the DSM
  595 primary; no generic default is invented.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
