# Scientific review of chi_1776_medium

- Review: 20261028T083819Z-chi-1776-medium-batch061
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:33:11.635751Z
- Finished UTC: 2026-10-28T08:38:19.718494Z
- Reviewer: Codex independent record reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact DSM source and two scoped basal rates are supported, including existing DSM-owner evidence and preparation. Five stock additions lose essential dose/strength/stage distinctions, and the generated record omits valid owner details. KOMODO equivalence and percent-stock bases remain explicitly unresolved.

## Scope And Provenance

Full selected target and maintained owners, every quantity and unchanged claim; separately scoped source dependencies and current writers.

Selection: Authoritative batch061 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3. Fresh review, not reconstruction of lost historical bundles.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005178 | data/merge_yaml/merged/CHI_1776_MEDIUM.yaml | generated | chi_1776_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005178 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-strict | passed | True | CultureMech:005178 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-terms | passed | True | CultureMech:005178 | Exit 0; original full stdout/stderr read. Structural check only. |
| validate-references | passed | True | CultureMech:005178 | Exit 0; original full stdout/stderr read. Zero reference checks. |

## Scientific And Domain Assessments

### DSM 394 and KOMODO 394 source scope

identity: supported. Targets: CultureMech:005178.

The exact current DSM PDF and API both identify CHI 1776 medium. The KOMODO mapping is an explicit local/historical link, but its current independent recipe is unavailable. No target organism or growth outcome is inferred from the medium name.

### Historical assertions and current writers

provenance: concern. Targets: CultureMech:005178.

Five complete historical reports and all 20 quoted API objects were read; current raw bytes authenticate the cited API payload and the DSM owner's two attached claims. The broad historical KOMODO conflict across all basal rows is not adopted: their declared provider rates are credited separately from unresolved stock semantics. All historical API excerpts with matching current raw digests are independently authenticated in historical-authentication.json. Matching bytes do not verify old execution or the separate KOMODO catalogue. Current MediaDive code separates stock additions but gathers all solution preparation into a root list; current conservative merging preserves scientific fields and rejects incompatible formulations. Those present behaviors do not prove how the old generated records were produced.

### Every concentration and source-only amount/stage

quantity: concern. Targets: CultureMech:005178.

All 21 selected target/owner concentration fields have explicit decisions; source-only stock, liquid, control and denominator gaps are retained separately.

{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:005178", "selected_concentration_field_count": 21, "selected_concentration_fields_covered": 21, "decisions": [{"decision_id": "q1", "subject": "Tryptone", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "23.3645", "unit": "G_PER_L"}}], "decision": "verified", "stage": "main basal mixture; provider-declared normalization", "interpretation": "The primary gives 25 g and the current API explicitly gives 23.3645 g/L on its declared volume of 1070 ml. Retain that provider basis separately from measured final volume, which the PDF does not state. The existing DSM-owner claim has the exact current raw digest and literal snippet, so it is verified; the reported old retrieval event is not recreated. Tryptone and yeast extract are mixtures; provider tryptone mmol_l is not endorsed.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 23.3645,\n                        \"mmol_l\": 328.707,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Tryptone                                                        25.0       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject": "Tryptone", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "23.3645", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[0].concentration", "original": {"value": "23.3645", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main basal mixture; provider-declared normalization", "interpretation": "The primary gives 25 g and the current API explicitly gives 23.3645 g/L on its declared volume of 1070 ml. Retain that provider basis separately from measured final volume, which the PDF does not state. These layers reproduce the rate but lack the DSM owner's scoped evidence. KOMODO access remains unavailable; copied chemistry is not independent source equivalence. Tryptone and yeast extract are mixtures; provider tryptone mmol_l is not endorsed.", "sources": [{"locator": "$.data.solutions[0].recipe[0]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\": 71,\n                        \"amount\": 25,\n                        \"unit\": \"g\",\n                        \"g_l\": 23.3645,\n                        \"mmol_l\": 328.707,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Tryptone                                                        25.0       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject": "Yeast extract", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "7.00935", "unit": "G_PER_L"}}], "decision": "verified", "stage": "main basal mixture; provider-declared normalization", "interpretation": "The primary gives 7.5 g and the current API explicitly gives 7.00935 g/L on its declared volume of 1070 ml. Retain that provider basis separately from measured final volume, which the PDF does not state. The existing DSM-owner claim has the exact current raw digest and literal snippet, so it is verified; the reported old retrieval event is not recreated. Tryptone and yeast extract are mixtures; provider tryptone mmol_l is not endorsed.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 7.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.00935,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Yeast extract                                                    7.5       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject": "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "7.00935", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[1].concentration", "original": {"value": "7.00935", "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main basal mixture; provider-declared normalization", "interpretation": "The primary gives 7.5 g and the current API explicitly gives 7.00935 g/L on its declared volume of 1070 ml. Retain that provider basis separately from measured final volume, which the PDF does not state. These layers reproduce the rate but lack the DSM owner's scoped evidence. KOMODO access remains unavailable; copied chemistry is not independent source equivalence. Tryptone and yeast extract are mixtures; provider tryptone mmol_l is not endorsed.", "sources": [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 7.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 7.00935,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 5-5", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Yeast extract                                                    7.5       g", "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject": "Tris-HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "20", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[2].concentration", "original": {"value": "20", "unit": "G_PER_L"}}], "decision": "correct", "stage": "buffer stock dose before basal autoclaving", "interpretation": "20 G_PER_L is a dimensional misrepresentation of a 20 ml dose of 1 M Tris-HCl stock at pH 7.5. Represent the absolute stock dose and molarity separately; do not convert it to 20 g/L or infer a measured final-volume concentration. The API mmol_l=20 is a separate provider field, not evidence for 20 g/L.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Tris-HCl\",\n                        \"compound_id\": 452,\n                        \"attribute\": \"pH 7.5, 1M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"mmol_l\": 20,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1M Tris-HCl (pH 7.5)                                            20.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q6", "subject": "Magnesium chloride", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.47605", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.47605", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[3].concentration", "original": {"value": "0.47605", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "separately autoclaved 1 M stock after cooling", "interpretation": "The primary specifies 5 ml of 1 M MgCl2, giving 0.005 mol delivered, not an explicit final g/L. The API reports 0.47605 g/L and 5 mmol/L, but its 1070 ml nominal medium metadata would require another denominator for a final rate. Preserve the source stock molarity and absolute dose instead of silently endorsing the flat value or replacing it with an assumed final concentration. Generic MgCl2 identity is retained; the source does not specify a weighed hydrate.", "sources": [{"locator": "$.data.solutions[0].recipe[4]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\": 453,\n                        \"attribute\": \"1M\",\n                        \"amount\": 5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.47605,\n                        \"mmol_l\": 5,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 10-10", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1M MgCl2                                                        5.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject": "Diaminopimelic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[4].concentration", "original": {"value": "0.1", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "separately filter-sterilized stock added after cooling", "interpretation": "The primary gives 10 ml of 1% stock. The percent basis is not stated and the PDF does not establish a measured final volume. Current API g_l values remain provider interpretations; they cannot authenticate a unique mass or final rate from a bare percent. Retain the exact source percentage and absolute dose as distinct facts, with the basis unresolved. Do not assume w/v, density or a stereoisomer absent from the source.", "sources": [{"locator": "$.data.solutions[0].recipe[5]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Diaminopimelic acid\",\n                        \"compound_id\": 454,\n                        \"attribute\": \"1%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.525762,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 11-11", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1% Diaminopimelic acid                                         10.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q8", "subject": "Thymidine", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.04", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.04", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[5].concentration", "original": {"value": "0.04", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "separately filter-sterilized stock added after cooling", "interpretation": "The primary gives 10 ml of 0.4% stock. The percent basis is not stated and the PDF does not establish a measured final volume. Current API g_l values remain provider interpretations; they cannot authenticate a unique mass or final rate from a bare percent. Retain the exact source percentage and absolute dose as distinct facts, with the basis unresolved. Do not assume w/v, density or a stereoisomer absent from the source.", "sources": [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Thymidine\",\n                        \"compound_id\": 455,\n                        \"attribute\": \"0.4%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.04,\n                        \"mmol_l\": 0.165132,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 12-12", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "0.4% Thymidine                                                 10.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject": "Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "5", "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "ingredients[6].concentration", "original": {"value": "5", "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "separately filter-sterilized stock added after cooling", "interpretation": "The primary gives 25 ml of 20% stock. The percent basis is not stated and the PDF does not establish a measured final volume. Current API g_l values remain provider interpretations; they cannot authenticate a unique mass or final rate from a bare percent. Retain the exact source percentage and absolute dose as distinct facts, with the basis unresolved. Do not assume w/v, density or a stereoisomer absent from the source.", "sources": [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"attribute\": \"20%\",\n                        \"amount\": 25,\n                        \"unit\": \"ml\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 13-13", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "20% Glucose                                                    25.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject": "Distilled water", "local_fields": [], "decision": "add", "stage": "basal solvent input", "interpretation": "The primary specifies 1000 ml distilled water. Preserve this absolute input in preparation context, separate from later liquid stocks. Adding the listed liquid volumes arithmetically gives 1070 ml, matching provider metadata, but is not a measured final-volume instruction.", "sources": [{"locator": "$.data.solutions[0].recipe[3]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Distilled water                                               1000.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q11", "subject": "Tris stock pH", "local_fields": [], "decision": "add", "stage": "buffer stock only", "interpretation": "pH 7.5 qualifies the 1 M Tris-HCl stock. It is not an asserted final medium pH and must not be promoted to root ph_value.", "sources": [{"locator": "$.data.solutions[0].recipe[2]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Tris-HCl\",\n                        \"compound_id\": 452,\n                        \"attribute\": \"pH 7.5, 1M\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"mmol_l\": 20,\n                        \"optional\": 0\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1M Tris-HCl (pH 7.5)                                            20.0      ml", "quote_representation": "captured extracted text"}]}, {"decision_id": "q12", "subject": "Basal autoclaving and cooling", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "preparation_steps[0].description", "original": "Autoclave, cool, and then add:"}], "decision": "verified", "stage": "basal before the four later stocks", "interpretation": "The DSM owner retains the exact autoclave/cool instruction; target and KOMODO owner omit it. The source supplies no temperature, time or cooling endpoint, so none is filled by convention.", "sources": [{"locator": "$.data.solutions[0].steps[0]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\": 5,\n                        \"step\": \"Autoclave, cool, and then add: \"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 9-9", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Autoclave, cool, and then add:", "quote_representation": "captured extracted text"}]}, {"decision_id": "q13", "subject": "Separate stock sterilization", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "preparation_steps[1].description", "original": "Magnesium chloride should be sterilized separately by autoclaving, and the other ingredients should be sterilized separately by filtration."}], "decision": "verified", "stage": "magnesium stock autoclave; remaining later stocks filtration", "interpretation": "The DSM owner correctly preserves separate magnesium autoclaving and filtration for the other later stock additions. Retain the ordered source boundary and attach root evidence scoped to preparation; PreparationStep has no evidence slot. Target and KOMODO owner require recovery of this supported detail.", "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"step\": \"Magnesium chloride should be sterilized separately by autoclaving, and the other ingredients should be sterilized separately by filtration.\"\n                    }", "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines 15-16", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf", "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975", "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0", "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Magnesium chloride should be sterilized separately by autoclaving, and the other\ningredients should be sterilized separately by filtration.", "quote_representation": "captured extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch061/record04/grounding-inventory.json", "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization, stock composition, working dose and preparation controls are separate. No source edits or automatic curation performed."}

### Primary, secondary and legacy linkage census

grounding: supported. Targets: CultureMech:005178.

data/merge_yaml/merged/CHI_1776_MEDIUM.yaml: primary 4/7, secondary 4/7; data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml: primary 4/7, secondary 4/7; data/normalized_yaml/bacterial/chi_1776_medium.yaml: primary 4/7, secondary 4/7. These are ingredient-instance linkage fractions, not accuracy scores. Solution terms are audited separately. Every actually asserted CHEBI term is joined to its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech mentions occur across the complete selected documents, with exact locators in the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product components are not forced to pure-compound IDs.

### Scope and source limits

scope: supported. Targets: CultureMech:005178.

Complete selected target and exact maintained owners reviewed. Dependencies transfer only their explicitly named stock subsection; unrelated parent media and source prescriptions are not growth evidence.

### Native structural checks

schema: supported. Targets: CultureMech:005178.

All four canonical commands passed once; strict schema TSV contains only its header and reference validation checked zero references on the generated target. This does not certify quantities or chemical forms.

## Findings

### f1: Stock doses are flattened into incompatible mass concentrations

major / open / confirmed; issue key: culturemech-005178-stock-dose-mass-and-final-basis.

Tris-HCl 20 G_PER_L is a 20 ml stock dose misrepresented as mass. Magnesium and three percentage-stock rows also lose stock strength, addition stage and denominator limits. The two basal provider rates remain valid within their explicitly declared basis; they are not included in a blanket numerical-error claim.

### f2: The generated target omits existing owner preparation and evidence

major / open / confirmed; issue key: culturemech-005178-generated-preparation-and-evidence-loss.

The DSM owner already retains both source preparation instructions and two authenticated concentration claims. The generated record and KOMODO owner omit these; all layers omit the absolute solvent input and buffer-stock pH context. Current exact-formulation merging rejects incompatible scientific projections and preserves scoped evidence, so this is stale generated content and incomplete maintained ownership, not proof that the current merger still drops such fields.

### f3: Copied chemistry does not independently verify the KOMODO equivalence claim

minor / open / confirmed; issue key: culturemech-005178-copied-source-identity-and-timestamp.

KOMODO history explicitly says ingredients were copied from DSM 394; exact local signatures are therefore not independent equivalence evidence. The precise historical MediaInfo route currently returns HTTP 403. The stored timestamp ending .fZ is malformed, while current importer code uses a %f strftime format. Preserve these old events; a verified current context event must be appended rather than rewriting their time.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct the five separately specified stock additions in maintained inputs using exact absolute doses, molarity or unresolved percent basis and preparation stage. Preserve the two authenticated basal rates with their provider basis; avoid a guessed final volume or mixture molarity.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action2

Preserve the existing DSM owner evidence and preparation, add supported stage and solvent details with root-scoped preparation/stock-dose evidence, and reassess distinct owner identity before regeneration. Do not force the currently incompatible records through the conservative merge guard.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

### action3

Retain source identities and the unresolved equivalence limit until exact KOMODO evidence is available. Fix future writer timestamp formatting separately; preserve original historical events and append any verified correction with the actual current curation date.

- Compare exact source identity, supplied form, amount, unit, denominator and preparation stage for every changed claim; preserve all correct current fields and old evidence.
- Attach claim-scoped source excerpts and references; rerun the four canonical checks on changed maintained inputs and inspect regenerated output for freshness.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local0 | data/merge_yaml/merged/CHI_1776_MEDIUM.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local1 | data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| local2 | data/normalized_yaml/bacterial/chi_1776_medium.yaml; entire YAML | supports | Entire current selected document, including all ingredients, source notes, history, relationships and preparation. No record edits. |
| validate-schema | REVIEW_WORK/batch061/record04/validate-schema-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-strict | REVIEW_WORK/batch061/record04/validate-strict-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Strict TSV is header-only. |
| validate-terms | REVIEW_WORK/batch061/record04/validate-terms-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Native bound-slot validation does not authenticate ingredient amounts or all chemical forms. |
| validate-references | REVIEW_WORK/batch061/record04/validate-references-result.json; argv, timestamps, exit_code, stdout, stderr | supports | Actual canonical command exit 0; full physical stdout/stderr read. Zero references checked, not scientific source verification. |
| dsmz394 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current primary captured text and available rendered PDF pages read: exact main recipe, separate stock tables, preparation and any strain-specific prescriptions. A source formulation is distinct from experimental growth evidence. |
| api394 | https://mediadive.dsmz.de/rest/medium/394; raw source; exact captured text/DOM/JSON locators in quantity inventory | supports | Complete current MediaDive API identity, primary recipe, separate stock recipes and preparation read. Explicit g_l values are provider normalization; solution volume metadata and listed water do not establish a measured final medium volume. Supplied mass/form takes priority over unverified mmol_l conversions. |
| komodo394 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=394; raw source; exact captured text/DOM/JSON locators in quantity inventory | unknown | Actual retrieval HTTP 403, error &lt;HTTPError 403: 'Forbidden'&gt;. This response does not authenticate a recipe. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi17748 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17748; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:17748 = thymidine; definition ["A pyrimidine 2'-deoxyribonucleoside having thymine as the nucleobase."]; formula ['C10H14N2O5']; mass ['242.231']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi23673 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23673; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:23673 = 2,6-diaminopimelic acid; definition ['The amino dicarboxylic acid that is heptanedioic acid with amino substituents at C-2 and C-6.']; formula ['C7H14N2O4']; mass ['190.199']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| chebi6636 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_6636; $._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete | supports | OLS current exact CHEBI:6636 = magnesium dichloride; definition ['A magnesium salt comprising of two chlorine atoms bound to a magnesium atom.']; formula ['2Cl.Mg']; mass ['95.211']; obsolete=False. Literal label is distinct from supplied-form equivalence. |
| grounding | REVIEW_WORK/batch061/record04/grounding-inventory.json; documents; ols_scientific_projection; mim_index | supports | Complete selected-layer term slots and current packaged MIM CSV exact-identifier joins with row locators and metadata commit; includes separately scoped dependency context. No fuzzy mapping or historical-validity inference. |
| history0 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chi_1776_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api394 raw bytes exactly match the cited historical SHA, and 10 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history1 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_394_CHI_1776_medium.yaml.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. Current api394 raw bytes exactly match the cited historical SHA, and 10 quoted objects match both decoded locators and literal current raw substrings. This authenticates the cited API payload and excerpts, not the reported historical access time, execution or separate KOMODO catalogue/page. |
| history2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chi_1776_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history3 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history4 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHI_1776_MEDIUM.md; entire report; historical-authentication.json | supports | Entire historical report read, including every unchanged and unresolved field. This narrative or zero-source-check report is a derivative lead, not new primary-source authentication. |
| history-auth | REVIEW_WORK/batch061/record04/historical-authentication.json; reports | supports | Exact report headers, source digest and every quoted API object reconciled; all reports fully read with duplicate cells pooled. Current primary sources independently govern scientific decisions. |
| writer21 | scripts/apply_mim_groundings.py; relevant functions named in summary | context_only | target_slot preserves existing CHEBI assertions, groundable excludes conflicting corpus opinions and apply_to_record fills only ungrounded names. This current CHEBI-only writer does not automatically replace deprecated secondary MIM links or authenticate quantities. |
| writer22 | scripts/propose_media_variant_links.py; relevant functions named in summary | context_only | Current infer_relationship/modification_text compares names and concentration signatures to propose source-duplicate or variant links for review. A copied signature cannot authenticate equivalence, and the proposal language explicitly calls for source verification. |
| writer23 | scripts/resolve_komodo_compositions.py; relevant functions named in summary | context_only | Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents copied ingredients/solutions but does not independently authenticate a particular past execution or variant. The underlying resolver is an inspected input and is assessed separately. |
| writer24 | src/culturemech/enrich/dsmz_resolver.py; relevant functions named in summary | context_only | Current DSMZCompositionResolver.merge_composition copies ingredients, solutions, pH, physical state and medium type; it does not copy preparation or independently establish source equivalence. resolve_recipe skips already populated ingredient lists. Current behavior does not authenticate the historical enrichment execution. |
| writer25 | src/culturemech/import/komodo_web_importer.py; relevant functions named in summary | context_only | Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes and initially empty ingredients for later DSMZ enrichment; its strftime format uses literal %f. Read code does not authenticate the past table values or source-copy execution. |
| writer26 | src/culturemech/import/mediadive_importer.py; relevant functions named in summary | context_only | Current _parse_api_composition uses only the primary recipe and prefers provider g_l; it excludes a fixed list of solvent names, which does not include Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes, but not molar-only attributes such as 1M. _parse_preparation_steps collects prose from all solution sections without separate stage fields. These present behaviors do not establish historical execution. |
| writer27 | src/culturemech/merge/formulation.py; relevant functions named in summary | context_only | Current formulation_content retains scientific fields, quantities, notes and preparation; merge_formulation_evidence rejects incompatible scientific projections and unions scoped evidence. Ingredient-set similarity does not prove scientific equivalence. |
| writer28 | src/culturemech/merge/matcher.py; relevant functions named in summary | context_only | Current group_formulations uses full formulation fingerprints for compatible automatic merging; broader group_recipes discovers ingredient-set candidates only. Neither grouping path substitutes for source verification. |
| writer29 | src/culturemech/merge/merger.py; relevant functions named in summary | context_only | Current merge_group returns a single owner with routing metadata, and calls conservative merge_formulation_evidence for multiple owners. Current code supports regenerating stale content after owner repair but does not authenticate old generated outputs. |
| quantity-inventory | REVIEW_WORK/batch061/record04/quantity-inventory.json; decisions | supports | Complete explicit decisions with exact current local values, per-layer locators, source quotes/hash/time, stage and arithmetic limits. |

## Limits And Additional Notes

- The exact historical KOMODO MediaInfo route returned HTTP 403; no guessed alternate recipe or blanket source equivalence is asserted.
- The PDF does not state a measured final volume or percentage basis. API 1070 ml and mixed g_l/mmol_l values remain provider metadata rather than a physical final-volume measurement.
- Current raw-byte equality authenticates payload content and snippets, not the old retrieval time, catalogue bytes or historical writer execution.
- The source does not establish a final medium pH, incubation conditions, strain-specific growth or sterility time/temperature. Tris pH 7.5 is stock-only.
- Read-only scientific review. No source edits, native save, Git mutation or publication. All raw captures, failed access bodies, commands, times and original stdout/stderr remain in the adjacent private evidence directory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T083819Z-chi-1776-medium-batch061
kind: record
repository: CultureBotAI/CultureMech
title: Scientific review of chi_1776_medium
started_at: '2026-10-28T08:33:11.635751Z'
finished_at: '2026-10-28T08:38:19.718494Z'
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
summary: The exact DSM source and two scoped basal rates are supported, including
  existing DSM-owner evidence and preparation. Five stock additions lose essential
  dose/strength/stage distinctions, and the generated record omits valid owner details.
  KOMODO equivalence and percent-stock bases remain explicitly unresolved.
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
  - path: data/merge_yaml/merged/CHI_1776_MEDIUM.yaml
    sha256: 44a5a2af7a475d64f41044cf134e3b31fac0201a71cdb28ddae973c9ec5ace04
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    sha256: c92d061f615c4adf9803b6874236924bc62b0ad1fb8088d85de96b516e260df7
    role: context
  - path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
    sha256: 6d40f0a92eae66f23d500cac6f4bc43bb4c185d00a752dc41c37b4463f875211
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_394_CHI_1776_medium.yaml.md
    sha256: 9250351b5a3db56ccb774b9108e9456316e244be9438aa0abbcdca3fe04c5411
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chi_1776_medium.yaml.md
    sha256: d904cbce44d6106395def39a74120a2d57d8655a6cef76e96623b8131ac7fddb
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHI_1776_MEDIUM.md
    sha256: ba510dbcc838885e10de76d83d677a44b1120ea621e965bc60b81ced0ace7bc5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.md
    sha256: 57bfd5dc1489e5fe5cd4036128488a9eca99f988cd8a92af3ebaf168df7af8e1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chi_1776_medium.md
    sha256: f66e9c04eb8f2d09baf962ce0710b81f90c43ddf3b6e6361c6caf7bbdb15cd32
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/propose_media_variant_links.py
    sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
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
  selection: Authoritative batch061 selection index 4 at base 9ea7ff33d354e37b791df96a880005153e446ce3.
    Fresh review, not reconstruction of lost historical bundles.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005178
targets:
- target_id: CultureMech:005178
  path: data/merge_yaml/merged/CHI_1776_MEDIUM.yaml
  label: chi_1776_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:005178
  command: just validate-schema data/merge_yaml/merged/CHI_1776_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:005178
  command: just validate-strict data/merge_yaml/merged/CHI_1776_MEDIUM.yaml --workers
    1 --out REVIEW_WORK/batch061/record04/strict.tsv
  exit_code: 0
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Structural check only.
  target_ids:
  - CultureMech:005178
  command: just validate-terms data/merge_yaml/merged/CHI_1776_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Exit 0; original full stdout/stderr read. Zero reference checks.
  target_ids:
  - CultureMech:005178
  command: just validate-references data/merge_yaml/merged/CHI_1776_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
evidence:
- evidence_id: local0
  kind: record_content
  reference: data/merge_yaml/merged/CHI_1776_MEDIUM.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:38:19.708966Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 44a5a2af7a475d64f41044cf134e3b31fac0201a71cdb28ddae973c9ec5ace04
- evidence_id: local1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:38:19.709115Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: c92d061f615c4adf9803b6874236924bc62b0ad1fb8088d85de96b516e260df7
- evidence_id: local2
  kind: record_content
  reference: data/normalized_yaml/bacterial/chi_1776_medium.yaml
  locator: entire YAML
  accessed_at: '2026-10-28T08:38:19.709142Z'
  support: supports
  summary: Entire current selected document, including all ingredients, source notes,
    history, relationships and preparation. No record edits.
  snapshot_sha256: 6d40f0a92eae66f23d500cac6f4bc43bb4c185d00a752dc41c37b4463f875211
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record04/validate-schema-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:12.635379Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: c0457bf32e781efc0f6b36b32627bac7459f4b611d57c426b509ed94859f76b3
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record04/validate-strict-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:13.542824Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Strict
    TSV is header-only.
  snapshot_sha256: a9e77f889784a5b4dfbe9cbcf8824ffbada7822d141c2ea2373256d2c93260ff
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record04/validate-terms-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:14.551062Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Native
    bound-slot validation does not authenticate ingredient amounts or all chemical
    forms.
  snapshot_sha256: 842b61da09c1186e3fa094eb1029e092c36236589062d15858a91bac359331ca
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch061/record04/validate-references-result.json
  locator: argv, timestamps, exit_code, stdout, stderr
  accessed_at: '2026-10-28T08:33:15.203023Z'
  support: supports
  summary: Actual canonical command exit 0; full physical stdout/stderr read. Zero
    references checked, not scientific source verification.
  snapshot_sha256: 1b10241c13f6644044e8872fd13430e8df2de8ed929765d133750aedffdf2fc3
- evidence_id: dsmz394
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:56.955578Z'
  support: supports
  summary: 'Complete current primary captured text and available rendered PDF pages
    read: exact main recipe, separate stock tables, preparation and any strain-specific
    prescriptions. A source formulation is distinct from experimental growth evidence.'
  snapshot_sha256: 94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975
- evidence_id: api394
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/394
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:56.904484Z'
  support: supports
  summary: Complete current MediaDive API identity, primary recipe, separate stock
    recipes and preparation read. Explicit g_l values are provider normalization;
    solution volume metadata and listed water do not establish a measured final medium
    volume. Supplied mass/form takes priority over unverified mmol_l conversions.
  snapshot_sha256: eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6
- evidence_id: komodo394
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=394
  locator: raw source; exact captured text/DOM/JSON locators in quantity inventory
  accessed_at: '2026-10-28T08:33:56.798712Z'
  support: unknown
  summary: 'Actual retrieval HTTP 403, error <HTTPError 403: ''Forbidden''>. This
    response does not authenticate a recipe.'
  snapshot_sha256: b9954cd325a3303462c0fbd91467083c97062c2980d05b532fc011a652f86b71
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:56.514572Z'
  support: supports
  summary: OLS current exact CHEBI:17234 = glucose; definition ['An aldohexose used
    as a source of energy and metabolic intermediate.']; formula ['C6H12O6']; mass
    ['180.156']; obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi17748
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17748
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:56.501121Z'
  support: supports
  summary: OLS current exact CHEBI:17748 = thymidine; definition ["A pyrimidine 2'-deoxyribonucleoside
    having thymine as the nucleobase."]; formula ['C10H14N2O5']; mass ['242.231'];
    obsolete=False. Literal label is distinct from supplied-form equivalence.
  snapshot_sha256: 9b1ee03f278f291821da43b3520fc3ff4ae694bfa5a972733a7a6f6cf027495a
- evidence_id: chebi23673
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_23673
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:56.305901Z'
  support: supports
  summary: OLS current exact CHEBI:23673 = 2,6-diaminopimelic acid; definition ['The
    amino dicarboxylic acid that is heptanedioic acid with amino substituents at C-2
    and C-6.']; formula ['C7H14N2O4']; mass ['190.199']; obsolete=False. Literal label
    is distinct from supplied-form equivalence.
  snapshot_sha256: 018989c1a0b111aa15bdada94373987524a35d210842150dcd6eedcd27238a7d
- evidence_id: chebi6636
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_6636
  locator: '$._embedded.terms[0]: obo_id,label,description,annotation,synonyms,is_obsolete'
  accessed_at: '2026-10-28T08:33:56.198037Z'
  support: supports
  summary: OLS current exact CHEBI:6636 = magnesium dichloride; definition ['A magnesium
    salt comprising of two chlorine atoms bound to a magnesium atom.']; formula ['2Cl.Mg'];
    mass ['95.211']; obsolete=False. Literal label is distinct from supplied-form
    equivalence.
  snapshot_sha256: 62283ffd3dce5ed835af343e697602b91b9230da436a122769d7821dee39a272
- evidence_id: grounding
  kind: authority
  reference: REVIEW_WORK/batch061/record04/grounding-inventory.json
  locator: documents; ols_scientific_projection; mim_index
  accessed_at: '2026-10-28T08:38:19.710992Z'
  support: supports
  summary: Complete selected-layer term slots and current packaged MIM CSV exact-identifier
    joins with row locators and metadata commit; includes separately scoped dependency
    context. No fuzzy mapping or historical-validity inference.
  snapshot_sha256: 33306b5651907e67358a87533de14a7cfaade48fefba8da31ccfc5098aa90cf3
- evidence_id: history0
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/chi_1776_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:38:19.711648Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api394 raw bytes exactly match the cited historical SHA, and 10
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: d904cbce44d6106395def39a74120a2d57d8655a6cef76e96623b8131ac7fddb
- evidence_id: history1
  kind: prior_review
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_394_CHI_1776_medium.yaml.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:38:19.711676Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. Current api394 raw bytes exactly match the cited historical SHA, and 10
    quoted objects match both decoded locators and literal current raw substrings.
    This authenticates the cited API payload and excerpts, not the reported historical
    access time, execution or separate KOMODO catalogue/page.
  snapshot_sha256: 9250351b5a3db56ccb774b9108e9456316e244be9438aa0abbcdca3fe04c5411
- evidence_id: history2
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/chi_1776_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:38:19.711695Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: f66e9c04eb8f2d09baf962ce0710b81f90c43ddf3b6e6361c6caf7bbdb15cd32
- evidence_id: history3
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:38:19.711714Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: 57bfd5dc1489e5fe5cd4036128488a9eca99f988cd8a92af3ebaf168df7af8e1
- evidence_id: history4
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHI_1776_MEDIUM.md
  locator: entire report; historical-authentication.json
  accessed_at: '2026-10-28T08:38:19.711731Z'
  support: supports
  summary: Entire historical report read, including every unchanged and unresolved
    field. This narrative or zero-source-check report is a derivative lead, not new
    primary-source authentication.
  snapshot_sha256: ba510dbcc838885e10de76d83d677a44b1120ea621e965bc60b81ced0ace7bc5
- evidence_id: history-auth
  kind: record_content
  reference: REVIEW_WORK/batch061/record04/historical-authentication.json
  locator: reports
  accessed_at: '2026-10-28T08:38:19.711752Z'
  support: supports
  summary: Exact report headers, source digest and every quoted API object reconciled;
    all reports fully read with duplicate cells pooled. Current primary sources independently
    govern scientific decisions.
  snapshot_sha256: a783d92158cf6567bc65481d0cb54e474e8e359b48f7405bfc76e9935a5099ae
- evidence_id: writer21
  kind: record_content
  reference: scripts/apply_mim_groundings.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711775Z'
  support: context_only
  summary: target_slot preserves existing CHEBI assertions, groundable excludes conflicting
    corpus opinions and apply_to_record fills only ungrounded names. This current
    CHEBI-only writer does not automatically replace deprecated secondary MIM links
    or authenticate quantities.
  snapshot_sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
- evidence_id: writer22
  kind: record_content
  reference: scripts/propose_media_variant_links.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711798Z'
  support: context_only
  summary: Current infer_relationship/modification_text compares names and concentration
    signatures to propose source-duplicate or variant links for review. A copied signature
    cannot authenticate equivalence, and the proposal language explicitly calls for
    source verification.
  snapshot_sha256: bd5b0b86c9457e42ca52ba2b253e5842c7f414093ba15aaeb4f9f0d682b5f4c2
- evidence_id: writer23
  kind: record_content
  reference: scripts/resolve_komodo_compositions.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711816Z'
  support: context_only
  summary: 'Full CLI wrapper read: it delegates empty KOMODO ingredient enrichment
    to DSMZCompositionResolver and exposes dry-run/report modes. The wrapper documents
    copied ingredients/solutions but does not independently authenticate a particular
    past execution or variant. The underlying resolver is an inspected input and is
    assessed separately.'
  snapshot_sha256: f45bc52a8efaa66c9a93c109a40c7d2763ac9f49c9009d92a4c0a0a41b7c28da
- evidence_id: writer24
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711836Z'
  support: context_only
  summary: Current DSMZCompositionResolver.merge_composition copies ingredients, solutions,
    pH, physical state and medium type; it does not copy preparation or independently
    establish source equivalence. resolve_recipe skips already populated ingredient
    lists. Current behavior does not authenticate the historical enrichment execution.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: writer25
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711856Z'
  support: context_only
  summary: Current _convert_to_culturemech builds KOMODO identity, is_aerobic notes
    and initially empty ingredients for later DSMZ enrichment; its strftime format
    uses literal %f. Read code does not authenticate the past table values or source-copy
    execution.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer26
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711883Z'
  support: context_only
  summary: Current _parse_api_composition uses only the primary recipe and prefers
    provider g_l; it excludes a fixed list of solvent names, which does not include
    Tap water. The ml fallback maps to ML_PER_L, requiring an independent denominator
    check. _is_api_stock_addition recognizes explicit stock IDs and percentage attributes,
    but not molar-only attributes such as 1M. _parse_preparation_steps collects prose
    from all solution sections without separate stage fields. These present behaviors
    do not establish historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer27
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711901Z'
  support: context_only
  summary: Current formulation_content retains scientific fields, quantities, notes
    and preparation; merge_formulation_evidence rejects incompatible scientific projections
    and unions scoped evidence. Ingredient-set similarity does not prove scientific
    equivalence.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer28
  kind: record_content
  reference: src/culturemech/merge/matcher.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711919Z'
  support: context_only
  summary: Current group_formulations uses full formulation fingerprints for compatible
    automatic merging; broader group_recipes discovers ingredient-set candidates only.
    Neither grouping path substitutes for source verification.
  snapshot_sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
- evidence_id: writer29
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: relevant functions named in summary
  accessed_at: '2026-10-28T08:38:19.711938Z'
  support: context_only
  summary: Current merge_group returns a single owner with routing metadata, and calls
    conservative merge_formulation_evidence for multiple owners. Current code supports
    regenerating stale content after owner repair but does not authenticate old generated
    outputs.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: quantity-inventory
  kind: record_content
  reference: REVIEW_WORK/batch061/record04/quantity-inventory.json
  locator: decisions
  accessed_at: '2026-10-28T08:38:19.718345Z'
  support: supports
  summary: Complete explicit decisions with exact current local values, per-layer
    locators, source quotes/hash/time, stage and arithmetic limits.
  snapshot_sha256: 63db4a0d1137cf2930ee717be90bd18fa805a4e0352197e1d11ab1a227e30f07
assessments:
- assessment_id: a1
  area: identity
  topic: DSM 394 and KOMODO 394 source scope
  outcome: supported
  summary: The exact current DSM PDF and API both identify CHI 1776 medium. The KOMODO
    mapping is an explicit local/historical link, but its current independent recipe
    is unavailable. No target organism or growth outcome is inferred from the medium
    name.
  target_ids:
  - CultureMech:005178
  evidence_ids:
  - api394
  - dsmz394
  - komodo394
- assessment_id: a2
  area: provenance
  topic: Historical assertions and current writers
  outcome: concern
  summary: 'Five complete historical reports and all 20 quoted API objects were read;
    current raw bytes authenticate the cited API payload and the DSM owner''s two
    attached claims. The broad historical KOMODO conflict across all basal rows is
    not adopted: their declared provider rates are credited separately from unresolved
    stock semantics. All historical API excerpts with matching current raw digests
    are independently authenticated in historical-authentication.json. Matching bytes
    do not verify old execution or the separate KOMODO catalogue. Current MediaDive
    code separates stock additions but gathers all solution preparation into a root
    list; current conservative merging preserves scientific fields and rejects incompatible
    formulations. Those present behaviors do not prove how the old generated records
    were produced.'
  target_ids:
  - CultureMech:005178
  evidence_ids:
  - history-auth
  - writer21
  - writer22
  - writer23
  - writer24
  - writer25
  - writer26
  - writer27
  - writer28
  - writer29
- assessment_id: a3
  area: quantity
  topic: Every concentration and source-only amount/stage
  outcome: concern
  summary: All 21 selected target/owner concentration fields have explicit decisions;
    source-only stock, liquid, control and denominator gaps are retained separately.
  target_ids:
  - CultureMech:005178
  evidence_ids:
  - quantity-inventory
  details: '{"schema": "private explicit quantity decisions v1", "target_id": "CultureMech:005178",
    "selected_concentration_field_count": 21, "selected_concentration_fields_covered":
    21, "decisions": [{"decision_id": "q1", "subject": "Tryptone", "local_fields":
    [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path":
    "ingredients[0].concentration", "original": {"value": "23.3645", "unit": "G_PER_L"}}],
    "decision": "verified", "stage": "main basal mixture; provider-declared normalization",
    "interpretation": "The primary gives 25 g and the current API explicitly gives
    23.3645 g/L on its declared volume of 1070 ml. Retain that provider basis separately
    from measured final volume, which the PDF does not state. The existing DSM-owner
    claim has the exact current raw digest and literal snippet, so it is verified;
    the reported old retrieval event is not recreated. Tryptone and yeast extract
    are mixtures; provider tryptone mmol_l is not endorsed.", "sources": [{"locator":
    "$.data.solutions[0].recipe[0]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\":
    71,\n                        \"amount\": 25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 23.3645,\n                        \"mmol_l\":
    328.707,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz394",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Tryptone                                                        25.0       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q2", "subject":
    "Tryptone", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "23.3645",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[0].concentration", "original": {"value": "23.3645",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main basal mixture;
    provider-declared normalization", "interpretation": "The primary gives 25 g and
    the current API explicitly gives 23.3645 g/L on its declared volume of 1070 ml.
    Retain that provider basis separately from measured final volume, which the PDF
    does not state. These layers reproduce the rate but lack the DSM owner''s scoped
    evidence. KOMODO access remains unavailable; copied chemistry is not independent
    source equivalence. Tryptone and yeast extract are mixtures; provider tryptone
    mmol_l is not endorsed.", "sources": [{"locator": "$.data.solutions[0].recipe[0]",
    "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Tryptone\",\n                        \"compound_id\":
    71,\n                        \"amount\": 25,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 23.3645,\n                        \"mmol_l\":
    328.707,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 4-4", "source_key": "dsmz394",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Tryptone                                                        25.0       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q3", "subject":
    "Yeast extract", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "7.00935",
    "unit": "G_PER_L"}}], "decision": "verified", "stage": "main basal mixture; provider-declared
    normalization", "interpretation": "The primary gives 7.5 g and the current API
    explicitly gives 7.00935 g/L on its declared volume of 1070 ml. Retain that provider
    basis separately from measured final volume, which the PDF does not state. The
    existing DSM-owner claim has the exact current raw digest and literal snippet,
    so it is verified; the reported old retrieval event is not recreated. Tryptone
    and yeast extract are mixtures; provider tryptone mmol_l is not endorsed.", "sources":
    [{"locator": "$.data.solutions[0].recipe[1]", "source_key": "api394", "reference":
    "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 7.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 7.00935,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 5-5", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Yeast extract                                                    7.5       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q4", "subject":
    "Yeast extract", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "7.00935",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[1].concentration", "original": {"value": "7.00935",
    "unit": "G_PER_L"}}], "decision": "evidence_only", "stage": "main basal mixture;
    provider-declared normalization", "interpretation": "The primary gives 7.5 g and
    the current API explicitly gives 7.00935 g/L on its declared volume of 1070 ml.
    Retain that provider basis separately from measured final volume, which the PDF
    does not state. These layers reproduce the rate but lack the DSM owner''s scoped
    evidence. KOMODO access remains unavailable; copied chemistry is not independent
    source equivalence. Tryptone and yeast extract are mixtures; provider tryptone
    mmol_l is not endorsed.", "sources": [{"locator": "$.data.solutions[0].recipe[1]",
    "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"amount\": 7.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 7.00935,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 5-5", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Yeast extract                                                    7.5       g",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q5", "subject":
    "Tris-HCl", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "ingredients[2].concentration", "original": {"value": "20", "unit":
    "G_PER_L"}}], "decision": "correct", "stage": "buffer stock dose before basal
    autoclaving", "interpretation": "20 G_PER_L is a dimensional misrepresentation
    of a 20 ml dose of 1 M Tris-HCl stock at pH 7.5. Represent the absolute stock
    dose and molarity separately; do not convert it to 20 g/L or infer a measured
    final-volume concentration. The API mmol_l=20 is a separate provider field, not
    evidence for 20 g/L.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Tris-HCl\",\n                        \"compound_id\":
    452,\n                        \"attribute\": \"pH 7.5, 1M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"mmol_l\":
    20,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz394",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1M Tris-HCl
    (pH 7.5)                                            20.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q6", "subject": "Magnesium chloride",
    "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.47605",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.47605",
    "unit": "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "ingredients[3].concentration", "original": {"value": "0.47605",
    "unit": "G_PER_L"}}], "decision": "unsupported", "stage": "separately autoclaved
    1 M stock after cooling", "interpretation": "The primary specifies 5 ml of 1 M
    MgCl2, giving 0.005 mol delivered, not an explicit final g/L. The API reports
    0.47605 g/L and 5 mmol/L, but its 1070 ml nominal medium metadata would require
    another denominator for a final rate. Preserve the source stock molarity and absolute
    dose instead of silently endorsing the flat value or replacing it with an assumed
    final concentration. Generic MgCl2 identity is retained; the source does not specify
    a weighed hydrate.", "sources": [{"locator": "$.data.solutions[0].recipe[4]",
    "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"compound\": \"MgCl2\",\n                        \"compound_id\":
    453,\n                        \"attribute\": \"1M\",\n                        \"amount\":
    5,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.47605,\n                        \"mmol_l\": 5,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 10-10", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1M MgCl2                                                        5.0      ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q7", "subject":
    "Diaminopimelic acid", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "ingredients[4].concentration", "original": {"value": "0.1", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "separately filter-sterilized
    stock added after cooling", "interpretation": "The primary gives 10 ml of 1% stock.
    The percent basis is not stated and the PDF does not establish a measured final
    volume. Current API g_l values remain provider interpretations; they cannot authenticate
    a unique mass or final rate from a bare percent. Retain the exact source percentage
    and absolute dose as distinct facts, with the basis unresolved. Do not assume
    w/v, density or a stereoisomer absent from the source.", "sources": [{"locator":
    "$.data.solutions[0].recipe[5]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Diaminopimelic acid\",\n                        \"compound_id\":
    454,\n                        \"attribute\": \"1%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.525762,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 11-11", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1% Diaminopimelic
    acid                                         10.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q8", "subject": "Thymidine", "local_fields":
    [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "original": {"value": "0.04", "unit": "G_PER_L"}},
    {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.04", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "ingredients[5].concentration", "original": {"value": "0.04", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "separately filter-sterilized
    stock added after cooling", "interpretation": "The primary gives 10 ml of 0.4%
    stock. The percent basis is not stated and the PDF does not establish a measured
    final volume. Current API g_l values remain provider interpretations; they cannot
    authenticate a unique mass or final rate from a bare percent. Retain the exact
    source percentage and absolute dose as distinct facts, with the basis unresolved.
    Do not assume w/v, density or a stereoisomer absent from the source.", "sources":
    [{"locator": "$.data.solutions[0].recipe[6]", "source_key": "api394", "reference":
    "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    7,\n                        \"compound\": \"Thymidine\",\n                        \"compound_id\":
    455,\n                        \"attribute\": \"0.4%\",\n                        \"amount\":
    10,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    0.04,\n                        \"mmol_l\": 0.165132,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 12-12", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "0.4% Thymidine                                                 10.0      ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q9", "subject":
    "Glucose", "local_fields": [{"record_path": "data/merge_yaml/merged/CHI_1776_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}, {"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "ingredients[6].concentration", "original": {"value": "5", "unit":
    "G_PER_L"}}], "decision": "unsupported", "stage": "separately filter-sterilized
    stock added after cooling", "interpretation": "The primary gives 25 ml of 20%
    stock. The percent basis is not stated and the PDF does not establish a measured
    final volume. Current API g_l values remain provider interpretations; they cannot
    authenticate a unique mass or final rate from a bare percent. Retain the exact
    source percentage and absolute dose as distinct facts, with the basis unresolved.
    Do not assume w/v, density or a stereoisomer absent from the source.", "sources":
    [{"locator": "$.data.solutions[0].recipe[7]", "source_key": "api394", "reference":
    "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"attribute\": \"20%\",\n                        \"amount\":
    25,\n                        \"unit\": \"ml\",\n                        \"g_l\":
    5,\n                        \"mmol_l\": 27.7531,\n                        \"optional\":
    0\n                    }", "quote_representation": "raw JSON object"}, {"locator":
    "extracted-text lines 13-13", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "20% Glucose                                                    25.0      ml",
    "quote_representation": "captured extracted text"}]}, {"decision_id": "q10", "subject":
    "Distilled water", "local_fields": [], "decision": "add", "stage": "basal solvent
    input", "interpretation": "The primary specifies 1000 ml distilled water. Preserve
    this absolute input in preparation context, separate from later liquid stocks.
    Adding the listed liquid volumes arithmetically gives 1070 ml, matching provider
    metadata, but is not a measured final-volume instruction.", "sources": [{"locator":
    "$.data.solutions[0].recipe[3]", "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 7-7", "source_key": "dsmz394",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Distilled
    water                                               1000.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q11", "subject": "Tris stock pH",
    "local_fields": [], "decision": "add", "stage": "buffer stock only", "interpretation":
    "pH 7.5 qualifies the 1 M Tris-HCl stock. It is not an asserted final medium pH
    and must not be promoted to root ph_value.", "sources": [{"locator": "$.data.solutions[0].recipe[2]",
    "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Tris-HCl\",\n                        \"compound_id\":
    452,\n                        \"attribute\": \"pH 7.5, 1M\",\n                        \"amount\":
    20,\n                        \"unit\": \"ml\",\n                        \"mmol_l\":
    20,\n                        \"optional\": 0\n                    }", "quote_representation":
    "raw JSON object"}, {"locator": "extracted-text lines 6-6", "source_key": "dsmz394",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "1M Tris-HCl
    (pH 7.5)                                            20.0      ml", "quote_representation":
    "captured extracted text"}]}, {"decision_id": "q12", "subject": "Basal autoclaving
    and cooling", "local_fields": [{"record_path": "data/normalized_yaml/bacterial/chi_1776_medium.yaml",
    "field_path": "preparation_steps[0].description", "original": "Autoclave, cool,
    and then add:"}], "decision": "verified", "stage": "basal before the four later
    stocks", "interpretation": "The DSM owner retains the exact autoclave/cool instruction;
    target and KOMODO owner omit it. The source supplies no temperature, time or cooling
    endpoint, so none is filled by convention.", "sources": [{"locator": "$.data.solutions[0].steps[0]",
    "source_key": "api394", "reference": "https://mediadive.dsmz.de/rest/medium/394",
    "source_raw_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "source_text_sha256": "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6",
    "accessed_at": "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"recipe_order\":
    5,\n                        \"step\": \"Autoclave, cool, and then add: \"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    9-9", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Autoclave,
    cool, and then add:", "quote_representation": "captured extracted text"}]}, {"decision_id":
    "q13", "subject": "Separate stock sterilization", "local_fields": [{"record_path":
    "data/normalized_yaml/bacterial/chi_1776_medium.yaml", "field_path": "preparation_steps[1].description",
    "original": "Magnesium chloride should be sterilized separately by autoclaving,
    and the other ingredients should be sterilized separately by filtration."}], "decision":
    "verified", "stage": "magnesium stock autoclave; remaining later stocks filtration",
    "interpretation": "The DSM owner correctly preserves separate magnesium autoclaving
    and filtration for the other later stock additions. Retain the ordered source
    boundary and attach root evidence scoped to preparation; PreparationStep has no
    evidence slot. Target and KOMODO owner require recovery of this supported detail.",
    "sources": [{"locator": "$.data.solutions[0].steps[1]", "source_key": "api394",
    "reference": "https://mediadive.dsmz.de/rest/medium/394", "source_raw_sha256":
    "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "source_text_sha256":
    "eadb359a816fe26f4b8a24fcfa57f3d6df3cb04f15d2c12e4a5d0fe82fda5bd6", "accessed_at":
    "2026-10-28T08:33:56.904484Z", "exact_source_quote": "{\n                        \"step\":
    \"Magnesium chloride should be sterilized separately by autoclaving, and the other
    ingredients should be sterilized separately by filtration.\"\n                    }",
    "quote_representation": "raw JSON object"}, {"locator": "extracted-text lines
    15-16", "source_key": "dsmz394", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf",
    "source_raw_sha256": "94d13e3f293952062acbcfb8a5ce7c58ae252ee2e753154741bf4d1302bbc975",
    "source_text_sha256": "07d3321e44a18397bd9b103181895041c747238f6c954f85b39a1c521bc13ba0",
    "accessed_at": "2026-10-28T08:33:56.955578Z", "exact_source_quote": "Magnesium
    chloride should be sterilized separately by autoclaving, and the other\ningredients
    should be sterilized separately by filtration.", "quote_representation": "captured
    extracted text"}]}], "local_field_census_reference": "REVIEW_WORK/batch061/record04/grounding-inventory.json",
    "source_only_gaps_are_explicit": true, "note": "Batch amounts, provider normalization,
    stock composition, working dose and preparation controls are separate. No source
    edits or automatic curation performed."}'
- assessment_id: a4
  area: grounding
  topic: Primary, secondary and legacy linkage census
  outcome: supported
  summary: 'data/merge_yaml/merged/CHI_1776_MEDIUM.yaml: primary 4/7, secondary 4/7;
    data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml: primary 4/7, secondary
    4/7; data/normalized_yaml/bacterial/chi_1776_medium.yaml: primary 4/7, secondary
    4/7. These are ingredient-instance linkage fractions, not accuracy scores. Solution
    terms are audited separately. Every actually asserted CHEBI term is joined to
    its exact current OLS object and packaged MIM CSV rows. 0 numeric legacy MediaIngredientMech
    mentions occur across the complete selected documents, with exact locators in
    the inventory; NNNNNN is a historical placeholder, not an ID. Complex commercial/product
    components are not forced to pure-compound IDs.'
  target_ids:
  - CultureMech:005178
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
  - CultureMech:005178
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
  - CultureMech:005178
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-005178-stock-dose-mass-and-final-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Stock doses are flattened into incompatible mass concentrations
  description: Tris-HCl 20 G_PER_L is a 20 ml stock dose misrepresented as mass. Magnesium
    and three percentage-stock rows also lose stock strength, addition stage and denominator
    limits. The two basal provider rates remain valid within their explicitly declared
    basis; they are not included in a blanket numerical-error claim.
  target_ids:
  - CultureMech:005178
  field_paths:
  - ingredients[2].concentration
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - solutions
  evidence_ids:
  - dsmz394
  - api394
  - quantity-inventory
  rule_id: stock-stage-and-dimensional-correspondence
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
    role: maintained normalized contributor
- finding_id: f2
  issue_key: culturemech-005178-generated-preparation-and-evidence-loss
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated target omits existing owner preparation and evidence
  description: The DSM owner already retains both source preparation instructions
    and two authenticated concentration claims. The generated record and KOMODO owner
    omit these; all layers omit the absolute solvent input and buffer-stock pH context.
    Current exact-formulation merging rejects incompatible scientific projections
    and preserves scoped evidence, so this is stale generated content and incomplete
    maintained ownership, not proof that the current merger still drops such fields.
  target_ids:
  - CultureMech:005178
  field_paths:
  - preparation_steps
  - evidence
  - references
  - ingredients[0].evidence
  - ingredients[1].evidence
  evidence_ids:
  - local0
  - local1
  - local2
  - api394
  - dsmz394
  rule_id: scientific-field-retention-and-preparation-scope
  native_severity: P2
  normalization_reason: P2 is normalized to major because the represented scientific
    units or source-supported content are materially wrong or stale.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
    role: maintained normalized contributor
- finding_id: f3
  issue_key: culturemech-005178-copied-source-identity-and-timestamp
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Copied chemistry does not independently verify the KOMODO equivalence claim
  description: KOMODO history explicitly says ingredients were copied from DSM 394;
    exact local signatures are therefore not independent equivalence evidence. The
    precise historical MediaInfo route currently returns HTTP 403. The stored timestamp
    ending .fZ is malformed, while current importer code uses a %f strftime format.
    Preserve these old events; a verified current context event must be appended rather
    than rewriting their time.
  target_ids:
  - CultureMech:005178
  field_paths:
  - parent_media
  - variant_modifications
  - data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml::curation_history[1].timestamp
  - data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml::notes
  evidence_ids:
  - komodo394
  - history-auth
  - local1
  rule_id: source-equivalence-and-append-only-history
  native_severity: P3
  normalization_reason: P3 is normalized to minor because this is a bounded completeness,
    traceability or presentation gap without a contradicted source recipe.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
    role: maintained normalized contributor
actions:
- action_id: action1
  description: Reconstruct the five separately specified stock additions in maintained
    inputs using exact absolute doses, molarity or unresolved percent basis and preparation
    stage. Preserve the two authenticated basal rates with their provider basis; avoid
    a guessed final volume or mixture molarity.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005178
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
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
  description: Preserve the existing DSM owner evidence and preparation, add supported
    stage and solvent details with root-scoped preparation/stock-dose evidence, and
    reassess distinct owner identity before regeneration. Do not force the currently
    incompatible records through the conservative merge guard.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005178
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
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
  description: Retain source identities and the unresolved equivalence limit until
    exact KOMODO evidence is available. Fix future writer timestamp formatting separately;
    preserve original historical events and append any verified correction with the
    actual current curation date.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005178
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/chi_1776_medium.yaml
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
- The exact historical KOMODO MediaInfo route returned HTTP 403; no guessed alternate
  recipe or blanket source equivalence is asserted.
- The PDF does not state a measured final volume or percentage basis. API 1070 ml
  and mixed g_l/mmol_l values remain provider metadata rather than a physical final-volume
  measurement.
- Current raw-byte equality authenticates payload content and snippets, not the old
  retrieval time, catalogue bytes or historical writer execution.
- The source does not establish a final medium pH, incubation conditions, strain-specific
  growth or sterility time/temperature. Tris pH 7.5 is stock-only.
notes:
- Read-only scientific review. No source edits, native save, Git mutation or publication.
  All raw captures, failed access bodies, commands, times and original stdout/stderr
  remain in the adjacent private evidence directory.
```
