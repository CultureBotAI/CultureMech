# CAPNOCYTOPHAGA II MEDIUM: liquid blood dose and unresolved volume basis

- Review: 20261028T071105Z-batch059-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T06:48:45.949965Z
- Finished UTC: 2026-10-28T07:11:05.274838Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The primary supplies a liquid horse-blood dose, while all local layers encode it as a mass rate. Its listed water input does not establish a final volume. The current API labels the unchanged batch digits g_l despite reporting solution volume 1050 ml; that conflict must remain explicit. The DSMZ owner already preserves source preparation that the generated record lacks.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch059 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:006440 | data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml | generated | capnocytophaga_ii_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:006440 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:006440 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:006440 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:006440 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact owner and source identity

identity: supported. Targets: CultureMech:006440.

Both contributors identify DSM 779; the explicit duplicate links and full signature establish the selected lineage. The standalone provider solution 1584 is mentioned only as the API solution identity, not imported as a separately inspected local recipe.

### Retained materials and classification

completeness: supported. Targets: CultureMech:006440.

Complex/undefined classification is supported by meat extract, proteose peptone, yeast and blood. Preserve Oxoid Lab-Lemco, Difco proteose peptone no. 3 and Difco/Bacto yeast attributes, soluble starch, and conditional agar. SOLID_AGAR denotes the agar-containing variant; the source also permits omission. No strain-specific growth or pathogenic target is inferred from the title.

### Supplied forms and exact ontology correspondence

grounding: supported. Targets: CultureMech:006440.

Current exact OLS objects support the represented generic glucose, starch, disodium hydrogen phosphate, agar and L-cysteine hydrochloride monohydrate identifiers. The primary says cysteine-HCl monohydrate without stereochemistry; the API explicitly supplies L-cysteine. Retain that narrower provider attribution. Current MIM preferred and synonym mapping statuses are preserved, not treated as proof of historical validity or amounts.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:006440.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Lab-Lemco beef extract", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Lab-Lemco beef extract\",\n                        \"compound_id\": 599,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\": 2.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.4,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Lab-Lemco beef extract", "compound_id": 599, "attribute": "Oxoid", "amount": 2.4, "unit": "g", "g_l": 2.4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.4", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.4", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.4", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q2", "topic": "Proteose peptone no. 3", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Proteose peptone no. 3\",\n                        \"compound_id\": 316,\n                        \"attribute\": \"Difco\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Proteose peptone no. 3", "compound_id": 316, "attribute": "Difco", "amount": 10, "unit": "g", "g_l": 10, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q3", "topic": "Yeast extract", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"Difco, Bacto\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Yeast extract", "compound_id": 16, "attribute": "Difco, Bacto", "amount": 5, "unit": "g", "g_l": 5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q4", "topic": "Na2HPO4", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Na2HPO4", "compound_id": 233, "amount": 4, "unit": "g", "g_l": 4, "mmol_l": 28.1771, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "4", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "4", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "4", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q5", "topic": "Glucose", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 8.32593,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Glucose", "compound_id": 5, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 8.32593, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q6", "topic": "Starch", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"condition\": \"\",\n                        \"attribute\": \"soluble\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Starch", "compound_id": 199, "condition": "", "attribute": "soluble", "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q7", "topic": "L-Cysteine HCl x H2O", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.8468,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 2.8468, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q8", "topic": "Agar", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"if necessary\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "condition": "if necessary", "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water and a separate 50 ml blood addition; it does not declare final volume. API g_l equals the batch digits while solution.volume is 1050. The retained nominal provider rate is traceable but is not independently established as a final-medium concentration. Preserve the batch mass and source discrepancy pending basis resolution."}]}, {"quantity_id": "q9", "topic": "Horse blood", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Horse blood\",\n                        \"compound_id\": 724,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Horse blood", "compound_id": 724, "amount": 50, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose peptone no.3 (Difco)                                   10.0       g\nYeast extract (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch, soluble                                                  0.5       g\nCysteine-HCl x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse blood                                                     50.0      ml\nDistilled water                                               1000.0      ml"}], "decision": "correct", "rationale": "The primary and API supply 50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe stage; density and a measured final volume are not supplied, so no mass conversion or final-medium ml/L replacement is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The primary and API supply 50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe stage; density and a measured final volume are not supplied, so no mass conversion or final-medium ml/L replacement is invented."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The primary and API supply 50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe stage; density and a measured final volume are not supplied, so no mass conversion or final-medium ml/L replacement is invented."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "50", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The primary and API supply 50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe stage; density and a measured final volume are not supplied, so no mass conversion or final-medium ml/L replacement is invented."}]}, {"quantity_id": "q10", "topic": "Water input", "source": {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "Distilled water                                               1000.0      ml"}, "decision": "evidence_only", "rationale": "Preserve the solvent input. It is neither a final-volume statement nor a mandatory water ontology edge.", "layer_assessments": []}, {"quantity_id": "q11", "topic": "Conditional agar", "source": {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "Agar, if necessary                                              15.0       g"}, "decision": "evidence_only", "rationale": "Keep the conditional solid variant; do not remove agar or assert all versions are solid.", "layer_assessments": []}, {"quantity_id": "q12", "topic": "Cooling and blood-addition stage", "source": {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "Add the horse blood to the heat sterilized medium after being cooled to 50"}, "decision": "mixed", "rationale": "The source requires blood addition after cooling. Retain the temperature and ordered stages; the owner description is already accurate although its single HEAT action compresses several operations.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The source requires blood addition after cooling. Retain the temperature and ordered stages; the owner description is already accurate although its single HEAT action compresses several operations.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The source requires blood addition after cooling. Retain the temperature and ordered stages; the owner description is already accurate although its single HEAT action compresses several operations.", "missing": true}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 7.6 - 7.8."}, {"step_number": 2, "action": "HEAT", "description": "Add the horse blood to the heat sterilized medium after being cooled to 50°C. Incubate under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2."}], "decision": "evidence_only", "rationale": "The source requires blood addition after cooling. Retain the temperature and ordered stages; the owner description is already accurate although its single HEAT action compresses several operations."}]}, {"quantity_id": "q13", "topic": "Atmosphere alternatives", "source": {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2."}, "decision": "mixed", "rationale": "Keep both alternatives and all gas fractions. Aerobic Yes alone does not represent the alternative anoxic source scope.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Keep both alternatives and all gas fractions. Aerobic Yes alone does not represent the alternative anoxic source scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Keep both alternatives and all gas fractions. Aerobic Yes alone does not represent the alternative anoxic source scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 7.6 - 7.8."}, {"step_number": 2, "action": "HEAT", "description": "Add the horse blood to the heat sterilized medium after being cooled to 50°C. Incubate under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2."}], "decision": "evidence_only", "rationale": "Keep both alternatives and all gas fractions. Aerobic Yes alone does not represent the alternative anoxic source scope."}]}, {"quantity_id": "q14", "topic": "pH range", "source": {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b", "locator": "Preparation", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote": "Adjust pH to 7.6 - 7.8."}, "decision": "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve the range rather than inventing a point estimate.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision": "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve the range rather than inventing a point estimate."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml", "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision": "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve the range rather than inventing a point estimate."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml", "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision": "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve the range rather than inventing a point estimate."}]}, {"quantity_id": "q15", "topic": "Provider solution volume", "source": {"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314", "locator": "$.data.solutions[0]", "accessed_at": "2026-10-28T06:49:54.045939Z", "quote": "{\n                \"id\": 1584,\n                \"name\": \"Main sol. 779\",\n                \"volume\": 1050,\n                \"recipe\": [\n                    {\n                        \"recipe_order\": 1,\n                        \"compound\": \"Lab-Lemco beef extract\",\n                        \"compound_id\": 599,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\": 2.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.4,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 2,\n                        \"compound\": \"Proteose peptone no. 3\",\n                        \"compound_id\": 316,\n                        \"attribute\": \"Difco\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"g_l\": 10,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\": \"Difco, Bacto\",\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 4,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 5,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 8.32593,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 6,\n                        \"compound\": \"Starch\",\n                        \"compound_id\": 199,\n                        \"condition\": \"\",\n                        \"attribute\": \"soluble\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 7,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.8468,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\": \"if necessary\",\n                        \"amount\": 15,\n                        \"unit\": \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 9,\n                        \"compound\": \"Horse blood\",\n                        \"compound_id\": 724,\n                        \"amount\": 50,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\": [\n                    {\n                        \"step\": \"Adjust pH to 7.6 - 7.8.\"\n                    },\n                    {\n                        \"step\": \"Add the horse blood to the heat sterilized medium after being cooled to 50\\u00b0C. Incubate under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2.\"\n                    }\n                ],\n                \"equipment\": {\n                    \"2485\": \"Autoclave\",\n                    \"4408\": \"Gassing station\"\n                }\n            }", "exact_decoded_object": {"id": 1584, "name": "Main sol. 779", "volume": 1050, "recipe": [{"recipe_order": 1, "compound": "Lab-Lemco beef extract", "compound_id": 599, "attribute": "Oxoid", "amount": 2.4, "unit": "g", "g_l": 2.4, "optional": 0}, {"recipe_order": 2, "compound": "Proteose peptone no. 3", "compound_id": 316, "attribute": "Difco", "amount": 10, "unit": "g", "g_l": 10, "optional": 0}, {"recipe_order": 3, "compound": "Yeast extract", "compound_id": 16, "attribute": "Difco, Bacto", "amount": 5, "unit": "g", "g_l": 5, "optional": 0}, {"recipe_order": 4, "compound": "Na2HPO4", "compound_id": 233, "amount": 4, "unit": "g", "g_l": 4, "mmol_l": 28.1771, "optional": 0}, {"recipe_order": 5, "compound": "Glucose", "compound_id": 5, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 8.32593, "optional": 0}, {"recipe_order": 6, "compound": "Starch", "compound_id": 199, "condition": "", "attribute": "soluble", "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}, {"recipe_order": 7, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 2.8468, "optional": 0}, {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "condition": "if necessary", "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, {"recipe_order": 9, "compound": "Horse blood", "compound_id": 724, "amount": 50, "unit": "ml", "optional": 0}, {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}], "steps": [{"step": "Adjust pH to 7.6 - 7.8."}, {"step": "Add the horse blood to the heat sterilized medium after being cooled to 50°C. Incubate under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2."}], "equipment": {"2485": "Autoclave", "4408": "Gassing station"}}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "conflict", "rationale": "The provider reports 1050 ml, consistent with adding listed water and blood volumes, but this is not a primary measured final-volume declaration. Its g_l values are not amount/1.05; retain the inconsistency without silently dividing all amounts.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:006440.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: concern. Targets: CultureMech:006440.

Complete histories and evidence were read, but malformed/timezone-unspecified historical events and generated evidence omissions remain. Preserve original events and append any verified correction context; current source authentication does not recover the historical access event.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:006440.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:006440.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

### Full historical report scope and rejected recommendations

provenance: concern. Targets: CultureMech:006440.

The Sept22 report is derivative context. Its1050ml final-volume interpretation and broad grounding endorsement do not replace the current distinction between primary water/input volumes, provider volume/g_l conflict and conditional ingredients.

## Findings

### f1: Correct the horse-blood liquid dose

major / open / confirmed; issue key: culturemech-006440-correct-the-horse-blood-liquid-dose.

All three current layers encode the source 50 ml horse-blood input as 50 G_PER_L. Preserve the liquid recipe-stage dose and source evidence. Do not substitute a mass concentration, infer blood density, or declare a final-medium denominator from water plus addition alone.

### f2: Resolve nominal rates against conflicting provider volume

major / open / confirmed; issue key: culturemech-006440-resolve-nominal-rates-against-conflicting-provider-volume.

The eight mass rows retain the provider’s g_l digits, but API solution.volume is 1050 and the primary gives batch masses, 1000 ml water and 50 ml blood without final-volume makeup. Keep these facts distinct; support the source batch masses while marking the unqualified final-medium interpretation unresolved. No automatic 1.05 division or assumption of a final litre is justified.

### f3: Restore scoped preparation and source evidence

major / open / confirmed; issue key: culturemech-006440-restore-scoped-preparation-and-source-evidence.

The DSMZ owner already retains pH adjustment and blood addition after cooling to 50°C with two atmosphere alternatives. The target and KOMODO owner omit that preparation and summarize only Aerobic: Yes. Preserve the existing owner description, retain ordered stages, and add source-specific root evidence before regeneration. Current multi-owner compatibility guards do not establish historical causality.

### f4: Retain uncertain history through append-only correction

minor / open / confirmed; issue key: culturemech-006440-retain-uncertain-history-through-append-only-correction.

The KOMODO contributor and its generated copy retain the literal .fZ event timestamp and a later timestamp without timezone. Keep original history intact; append verified context or a correction event only if authoritative original timing becomes available. Do not assign an inferred timezone or rewrite the original event.

## Recommended Actions And Acceptance Checks

### action1

All three current layers encode the source 50 ml horse-blood input as 50 G_PER_L. Preserve the liquid recipe-stage dose and source evidence. Do not substitute a mass concentration, infer blood density, or declare a final-medium denominator from water plus addition alone.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

The eight mass rows retain the provider’s g_l digits, but API solution.volume is 1050 and the primary gives batch masses, 1000 ml water and 50 ml blood without final-volume makeup. Keep these facts distinct; support the source batch masses while marking the unqualified final-medium interpretation unresolved. No automatic 1.05 division or assumption of a final litre is justified.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

The DSMZ owner already retains pH adjustment and blood addition after cooling to 50°C with two atmosphere alternatives. The target and KOMODO owner omit that preparation and summarize only Aerobic: Yes. Preserve the existing owner description, retain ordered stages, and add source-specific root evidence before regeneration. Current multi-owner compatibility guards do not establish historical causality.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

The KOMODO contributor and its generated copy retain the literal .fZ event timestamp and a later timestamp without timezone. Keep original history intact; append verified context or a correction event only if authoritative original timing becomes available. Do not assign an inferred timezone or rewrite the original event.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch059/record03/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| historical-1 | reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 12 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-2 | reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/capnocytophaga_ii_medium.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 12 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/capnocytophaga_ii_medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-6 | reports/yaml_record_review/20260922T032556Z-CAPNOCYTOPHAGA_II_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch059/record03/historical-reader.json | context_only | Every exact target/owner historical report in the native input manifest is retained in full, with exact parent-row scope where applicable. Prior recommendations are assessed against fresh primary and current code evidence. |
| dsm779 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf; Exact source identity and scoped formulation/preparation | supports | Complete primary DSMZ 779 PDF visually inspected; exact batch amounts, conditional agar, pH and post-cooling blood addition. No final-volume declaration. |
| api779 | https://mediadive.dsmz.de/rest/medium/779; Exact source identity and scoped formulation/preparation | supports | Complete fresh provider response; declared solution volume 1050 ml and explicit g_l rows are retained as conflicting source facts, not silently renormalized. Current raw exactly matches both historical cited response digests. |
| komodo779 | https://komodo.modelseed.org/servlet/Komodo?Mediumnumber=779; Exact source identity and scoped formulation/preparation | context_only | Initial guessed KOMODO endpoint returnedHTTP403. It is retained only as a failed discovery lead; separate exact historical MediaInfo and MediaList route captures also returned403. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28017; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch059/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch059/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch059/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch059/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch059/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch059/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch059/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch059/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch059/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |
| exact-source-route-1 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=779; Exact historical source route, current HTTP response; metadata REVIEW_WORK/batch059/record03-exact-route/komodo779-exact.json | context_only | This exact source route returned HTTP403. No unavailable table or historical access event is authenticated. Original failed lead captures remain distinct. |
| exact-source-route-2 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact historical source route, current HTTP response; metadata REVIEW_WORK/batch059/record01-root-exact-routes/komodo964-list.json | context_only | This exact source route returned HTTP403. No unavailable table or historical access event is authenticated. Original failed lead captures remain distinct. |
| source-route-supplement | REVIEW_WORK/batch059/record03/source-route-supplement.json | context_only | Exact route metadata/raw joins, with original actual retrieval timestamps and failed-lead distinction. |

## Limits And Additional Notes

- The initial guessed KOMODO route and the exact historical MediaInfo and MediaList routes each returned HTTP403. Current DSMZ/API evidence authenticates the matching API bytes and quoted objects, not the unavailable KOMODO table or its historical access event.
- Final volume remains unresolved: the primary water input and provider volume/g_l conflict do not justify an invented corrected final concentration. Blood density is unknown.
- No named strain, growth support or organism identity is supplied by the inspected formulation; genus-like medium naming does not establish a specific biological target.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T071105Z-batch059-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'CAPNOCYTOPHAGA II MEDIUM: liquid blood dose and unresolved volume basis'
started_at: '2026-10-28T06:48:45.949965Z'
finished_at: '2026-10-28T07:11:05.274838Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The primary supplies a liquid horse-blood dose, while all local layers encode
  it as a mass rate. Its listed water input does not establish a final volume. The
  current API labels the unchanged batch digits g_l despite reporting solution volume
  1050 ml; that conflict must remain explicit. The DSMZ owner already preserves source
  preparation that the generated record lacks.
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
  - path: data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
    sha256: 270284227afdf4ca844c2c6210ecacf4db24dafb7aa12c5c970e428c66240df3
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    sha256: 84f50a705beb47805315de6b7d71769dee2ae067eb3382f647ac3af0c350dbc6
    role: context
  - path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    sha256: b7ba26f9091014eb4373f8be34225c3bb52b1348d5a7cfa644f5089f41717b4b
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
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml.md
    sha256: ae0ac76791d5ab666dc326d680645757f60043f95177a32c2dc76eaa0448a273
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/capnocytophaga_ii_medium.yaml.md
    sha256: 23a7cf8876b642213d6af76699add4d1752814bf33f76c369379fadd4b157f85
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.md
    sha256: cc3f19cdd3db3e351053ff4169be52a351a4d24cf45c9fcd30e49cfe4d301f41
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.md
    sha256: 2a45a0378e5baebd50648193978cf7acf31f4fd34538969930cf4683c3db8bb0
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/capnocytophaga_ii_medium.md
    sha256: f3b2252e559bf78edb23a2595789dd90d8acb3cc3b659f8f0cba77b5a825ae75
    role: context
  - path: reports/yaml_record_review/20260922T032556Z-CAPNOCYTOPHAGA_II_MEDIUM.md
    sha256: 7faf121ca275b0ddaa6be2f17908906152037b4b8d3175de6d2426d433542eb4
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
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
scope:
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch059 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:006440
targets:
- target_id: CultureMech:006440
  path: data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
  label: capnocytophaga_ii_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006440
  command: just validate-schema data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006440
  command: just validate-strict data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
    --out REVIEW_WORK/batch059/record03/strict.tsv --workers 1
  exit_code: 0
  evidence_ids:
  - validate-strict
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:006440
  command: just validate-terms data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Native reference checker performed zero reference checks; this is not claim
    authentication.
  target_ids:
  - CultureMech:006440
  command: just validate-references data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 270284227afdf4ca844c2c6210ecacf4db24dafb7aa12c5c970e428c66240df3
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 84f50a705beb47805315de6b7d71769dee2ae067eb3382f647ac3af0c350dbc6
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: b7ba26f9091014eb4373f8be34225c3bb52b1348d5a7cfa644f5089f41717b4b
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch059/record03/identity-search.json
  accessed_at: '2026-10-28T07:01:02.722249Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems resolved uniquely. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: 9b7743d16df28c296e50885c4a724a856dcd349614976c389012398f89e375fd
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Current composition parser restricts ingredients to the primary solution,
    excludes solvent and recognized stock additions, and retains explicit g_l. The
    solution parser preserves referenced or percent-defined stocks and source attributes.
    Preparation parsing still concatenates all solution steps into root preparation_steps;
    source-stage annotation remains important. These present functions do not prove
    the historical execution that produced this record.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Current compatibility preserves scientific fields and list order and rejects
    unequal formulations; only specified provenance/evidence lists are unioned. It
    performs no concentration conversion or stock expansion and does not authenticate
    historical merges.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_duplicate_ingredients, merge_ingredient_group
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-2000-2500/records/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 12 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: ae0ac76791d5ab666dc326d680645757f60043f95177a32c2dc76eaa0448a273
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0500-1000/records/bacterial/capnocytophaga_ii_medium.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 12 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: 23a7cf8876b642213d6af76699add4d1752814bf33f76c369379fadd4b157f85
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: cc3f19cdd3db3e351053ff4169be52a351a4d24cf45c9fcd30e49cfe4d301f41
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 2a45a0378e5baebd50648193978cf7acf31f4fd34538969930cf4683c3db8bb0
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/capnocytophaga_ii_medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: f3b2252e559bf78edb23a2595789dd90d8acb3cc3b659f8f0cba77b5a825ae75
- evidence_id: historical-6
  kind: record_content
  reference: reports/yaml_record_review/20260922T032556Z-CAPNOCYTOPHAGA_II_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T07:01:02.635285Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 7faf121ca275b0ddaa6be2f17908906152037b4b8d3175de6d2426d433542eb4
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch059/record03/historical-reader.json
  accessed_at: '2026-10-28T07:01:02.731507Z'
  support: context_only
  summary: Every exact target/owner historical report in the native input manifest
    is retained in full, with exact parent-row scope where applicable. Prior recommendations
    are assessed against fresh primary and current code evidence.
  snapshot_sha256: a600bbdf590e4a981f34e90a3fec31c38a59ea11319d62375a20ae360107ed83
- evidence_id: dsm779
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:49:54.352235Z'
  support: supports
  summary: Complete primary DSMZ 779 PDF visually inspected; exact batch amounts,
    conditional agar, pH and post-cooling blood addition. No final-volume declaration.
  snapshot_sha256: 212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b
- evidence_id: api779
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/779
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:49:54.045939Z'
  support: supports
  summary: Complete fresh provider response; declared solution volume 1050 ml and
    explicit g_l rows are retained as conflicting source facts, not silently renormalized.
    Current raw exactly matches both historical cited response digests.
  snapshot_sha256: 47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314
- evidence_id: komodo779
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?Mediumnumber=779
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T06:49:54.062019Z'
  support: context_only
  summary: Initial guessed KOMODO endpoint returnedHTTP403. It is retained only as
    a failed discovery lead; separate exact historical MediaInfo and MediaList route
    captures also returned403.
  snapshot_sha256: 809d22f57587ee9bb32687a0594a006b57ce50a21da68d01b0d2c9b37f9a0445
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:49:57.554165Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b8fc153769cf791f5e08680678fe7df66be98486bbfbb734518f3de625596efe
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:49:55.781375Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d78d31a7829da999c31ae102da842c5b5c37a5d334be6389539d92ecd786de7
- evidence_id: chebi28017
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28017
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:49:56.952002Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97d3317b987b817f798f2968ae77d2d550be0f98d072c054f7effa98c58f9d1a
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:49:59.425434Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T06:49:56.431214Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch059/record03/quantity-inventory.json
  accessed_at: '2026-10-28T07:01:02.743120Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 39e7f9f38c21afe8851fe4ae0708b96d8498066aaf770f7179b92c683b975a35
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch059/record03/grounding-inventory.json
  accessed_at: '2026-10-28T07:01:02.743177Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 553e773843859937cf9887f4fb64a40e3f45de2b9c535172201b1dc6cd91a681
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch059/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T07:01:02.743228Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 0dd16f9993b197fd5965fbe5e1a54c24daece023a0170e6bfe9246590e5b04af
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch059/record03/scalar-census.json
  accessed_at: '2026-10-28T07:01:02.743251Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: c215744434cd1ae9c08daa6b76b9db6887d314b93f82cb20b27d700063ddcf1c
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch059/record03/validate-schema.json
  accessed_at: '2026-10-28T06:48:47.044964Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: f1478d5ed62399c66c8322c32cc0d5506c098e86988de5e04d7bbb11bcbbb0da
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch059/record03/validate-strict.json
  accessed_at: '2026-10-28T06:48:48.033864Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch059/record03/strict.tsv\n"
  snapshot_sha256: 4bc17c13a550e6c9f7ff4fdafd07825ce294651be7973ee7fccb5b69fbb1a1cb
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch059/record03/validate-terms.json
  accessed_at: '2026-10-28T06:48:49.100198Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: da343b9776a843904332f1ac7755a87d04f682f1ed6423b735a3f93279f6c45c
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch059/record03/validate-references.json
  accessed_at: '2026-10-28T06:48:49.794682Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: ffe184f668328910cff509deb8b82327d1294eda9b46278d357441ee28bffc88
- evidence_id: exact-source-route-1
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=779
  locator: Exact historical source route, current HTTP response; metadata REVIEW_WORK/batch059/record03-exact-route/komodo779-exact.json
  accessed_at: '2026-10-28T07:09:39.236696Z'
  support: context_only
  summary: This exact source route returned HTTP403. No unavailable table or historical
    access event is authenticated. Original failed lead captures remain distinct.
  snapshot_sha256: 84a31f9235aab1b96dea19cb5a94fce7e9f4efacb25364faa8efca4bfc6ec290
- evidence_id: exact-source-route-2
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact historical source route, current HTTP response; metadata REVIEW_WORK/batch059/record01-root-exact-routes/komodo964-list.json
  accessed_at: '2026-10-28T07:08:35.693802Z'
  support: context_only
  summary: This exact source route returned HTTP403. No unavailable table or historical
    access event is authenticated. Original failed lead captures remain distinct.
  snapshot_sha256: dad86ae019c5da0a88b63143ffde0fbfc65248b341be6c798aa9d0d3c25e6bd5
- evidence_id: source-route-supplement
  kind: record_content
  reference: REVIEW_WORK/batch059/record03/source-route-supplement.json
  accessed_at: '2026-10-28T07:11:05.273766Z'
  support: context_only
  summary: Exact route metadata/raw joins, with original actual retrieval timestamps
    and failed-lead distinction.
  snapshot_sha256: e0e05fbd313c5ab8286f12aee35ce2499ee2686a77ef83d4c274a6392f9ddcdb
assessments:
- assessment_id: a1
  area: identity
  topic: Exact owner and source identity
  outcome: supported
  summary: Both contributors identify DSM 779; the explicit duplicate links and full
    signature establish the selected lineage. The standalone provider solution 1584
    is mentioned only as the API solution identity, not imported as a separately inspected
    local recipe.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - identity-search
  - api779
- assessment_id: a2
  area: completeness
  topic: Retained materials and classification
  outcome: supported
  summary: Complex/undefined classification is supported by meat extract, proteose
    peptone, yeast and blood. Preserve Oxoid Lab-Lemco, Difco proteose peptone no.
    3 and Difco/Bacto yeast attributes, soluble starch, and conditional agar. SOLID_AGAR
    denotes the agar-containing variant; the source also permits omission. No strain-specific
    growth or pathogenic target is inferred from the title.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - dsm779
  - api779
  - local-target
- assessment_id: a3
  area: grounding
  topic: Supplied forms and exact ontology correspondence
  outcome: supported
  summary: Current exact OLS objects support the represented generic glucose, starch,
    disodium hydrogen phosphate, agar and L-cysteine hydrochloride monohydrate identifiers.
    The primary says cysteine-HCl monohydrate without stereochemistry; the API explicitly
    supplies L-cysteine. Retain that narrower provider attribution. Current MIM preferred
    and synonym mapping statuses are preserved, not treated as proof of historical
    validity or amounts.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - dsm779
  - api779
  - chebi91248
  - chebi34683
  - chebi17234
  - chebi28017
  - chebi2509
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Lab-Lemco beef extract", "source": [{"evidence_id":
    "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779", "raw_path":
    "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Lab-Lemco beef extract\",\n                        \"compound_id\": 599,\n                        \"attribute\":
    \"Oxoid\",\n                        \"amount\": 2.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.4,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Lab-Lemco beef extract", "compound_id": 599, "attribute": "Oxoid", "amount":
    2.4, "unit": "g", "g_l": 2.4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "2.4", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.4",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "2.4",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}]}, {"quantity_id": "q2", "topic": "Proteose
    peptone no. 3", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Proteose peptone no. 3\",\n                        \"compound_id\": 316,\n                        \"attribute\":
    \"Difco\",\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 10,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Proteose peptone no. 3", "compound_id": 316, "attribute": "Difco", "amount":
    10, "unit": "g", "g_l": 10, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}]}, {"quantity_id": "q3", "topic": "Yeast
    extract", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"attribute\":
    \"Difco, Bacto\",\n                        \"amount\": 5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 5,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Yeast extract", "compound_id": 16, "attribute": "Difco, Bacto", "amount": 5,
    "unit": "g", "g_l": 5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch
    mass with 1000 ml water and a separate 50 ml blood addition; it does not declare
    final volume. API g_l equals the batch digits while solution.volume is 1050. The
    retained nominal provider rate is traceable but is not independently established
    as a final-medium concentration. Preserve the batch mass and source discrepancy
    pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch
    mass with 1000 ml water and a separate 50 ml blood addition; it does not declare
    final volume. API g_l equals the batch digits while solution.volume is 1050. The
    retained nominal provider rate is traceable but is not independently established
    as a final-medium concentration. Preserve the batch mass and source discrepancy
    pending basis resolution."}]}, {"quantity_id": "q4", "topic": "Na2HPO4", "source":
    [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Na2HPO4\",\n                        \"compound_id\": 233,\n                        \"amount\":
    4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    4,\n                        \"mmol_l\": 28.1771,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Na2HPO4", "compound_id": 233, "amount": 4, "unit": "g", "g_l": 4, "mmol_l": 28.1771,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, {"evidence_id": "dsm779", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf", "raw_path":
    "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "4", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "4", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch
    mass with 1000 ml water and a separate 50 ml blood addition; it does not declare
    final volume. API g_l equals the batch digits while solution.volume is 1050. The
    retained nominal provider rate is traceable but is not independently established
    as a final-medium concentration. Preserve the batch mass and source discrepancy
    pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "4", "unit":
    "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies this batch
    mass with 1000 ml water and a separate 50 ml blood addition; it does not declare
    final volume. API g_l equals the batch digits while solution.volume is 1050. The
    retained nominal provider rate is traceable but is not independently established
    as a final-medium concentration. Preserve the batch mass and source discrepancy
    pending basis resolution."}]}, {"quantity_id": "q5", "topic": "Glucose", "source":
    [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Glucose\",\n                        \"compound_id\": 5,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 8.32593,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Glucose", "compound_id": 5, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l":
    8.32593, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, {"evidence_id": "dsm779",
    "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}]}, {"quantity_id": "q6", "topic": "Starch",
    "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Starch\",\n                        \"compound_id\": 199,\n                        \"condition\":
    \"\",\n                        \"attribute\": \"soluble\",\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 6, "compound": "Starch", "compound_id": 199, "condition": "",
    "attribute": "soluble", "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}]}, {"quantity_id": "q7", "topic": "L-Cysteine
    HCl x H2O", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 2.8468,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.5, "unit": "g", "g_l":
    0.5, "mmol_l": 2.8468, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}]}, {"quantity_id": "q8", "topic": "Agar",
    "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Agar\",\n                        \"compound_id\": 3,\n                        \"condition\":
    \"if necessary\",\n                        \"amount\": 15,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 15,\n                        \"mmol_l\":
    44.5991,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "compound": "Agar", "compound_id": 3, "condition": "if necessary",
    "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "conflict", "rationale": "The primary supplies this batch mass with 1000 ml water
    and a separate 50 ml blood addition; it does not declare final volume. API g_l
    equals the batch digits while solution.volume is 1050. The retained nominal provider
    rate is traceable but is not independently established as a final-medium concentration.
    Preserve the batch mass and source discrepancy pending basis resolution.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"},
    "decision": "conflict", "rationale": "The primary supplies this batch mass with
    1000 ml water and a separate 50 ml blood addition; it does not declare final volume.
    API g_l equals the batch digits while solution.volume is 1050. The retained nominal
    provider rate is traceable but is not independently established as a final-medium
    concentration. Preserve the batch mass and source discrepancy pending basis resolution."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The primary supplies
    this batch mass with 1000 ml water and a separate 50 ml blood addition; it does
    not declare final volume. API g_l equals the batch digits while solution.volume
    is 1050. The retained nominal provider rate is traceable but is not independently
    established as a final-medium concentration. Preserve the batch mass and source
    discrepancy pending basis resolution."}]}, {"quantity_id": "q9", "topic": "Horse
    blood", "source": [{"evidence_id": "api779", "reference": "https://mediadive.dsmz.de/rest/medium/779",
    "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin", "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Horse blood\",\n                        \"compound_id\": 724,\n                        \"amount\":
    50,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Horse blood", "compound_id": 724, "amount": 50, "unit": "ml", "optional": 0},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Complete main table", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "779. CAPNOCYTOPHAGA II MEDIUM\n\n\nLab-lemco meat extract (Oxoid)                                   2.4       g\nProteose
    peptone no.3 (Difco)                                   10.0       g\nYeast extract
    (Difco, Bacto)                                     5.0       g\nNa2HPO4                                                          4.0       g\nGlucose                                                          1.5       g\nStarch,
    soluble                                                  0.5       g\nCysteine-HCl
    x H2O                                               0.5       g\nAgar, if necessary                                              15.0       g\nHorse
    blood                                                     50.0      ml\nDistilled
    water                                               1000.0      ml"}], "decision":
    "correct", "rationale": "The primary and API supply 50 ml horse blood, not 50
    g. Correct the liquid dose representation at the recipe stage; density and a measured
    final volume are not supplied, so no mass conversion or final-medium ml/L replacement
    is invented.", "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The primary and API supply
    50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe
    stage; density and a measured final volume are not supplied, so no mass conversion
    or final-medium ml/L replacement is invented."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The primary and API supply
    50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe
    stage; density and a measured final volume are not supplied, so no mass conversion
    or final-medium ml/L replacement is invented."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "50",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The primary and API supply
    50 ml horse blood, not 50 g. Correct the liquid dose representation at the recipe
    stage; density and a measured final volume are not supplied, so no mass conversion
    or final-medium ml/L replacement is invented."}]}, {"quantity_id": "q10", "topic":
    "Water input", "source": {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "Distilled water                                               1000.0      ml"},
    "decision": "evidence_only", "rationale": "Preserve the solvent input. It is neither
    a final-volume statement nor a mandatory water ontology edge.", "layer_assessments":
    []}, {"quantity_id": "q11", "topic": "Conditional agar", "source": {"evidence_id":
    "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "Agar, if necessary                                              15.0       g"},
    "decision": "evidence_only", "rationale": "Keep the conditional solid variant;
    do not remove agar or assert all versions are solid.", "layer_assessments": []},
    {"quantity_id": "q12", "topic": "Cooling and blood-addition stage", "source":
    {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "Add the horse blood to the heat sterilized medium after being cooled
    to 50"}, "decision": "mixed", "rationale": "The source requires blood addition
    after cooling. Retain the temperature and ordered stages; the owner description
    is already accurate although its single HEAT action compresses several operations.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The source requires blood addition after cooling. Retain the temperature and
    ordered stages; the owner description is already accurate although its single
    HEAT action compresses several operations.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The source requires blood addition after cooling. Retain the temperature and
    ordered stages; the owner description is already accurate although its single
    HEAT action compresses several operations.", "missing": true}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "ADJUST_PH", "description": "Adjust pH to 7.6 - 7.8."}, {"step_number": 2, "action":
    "HEAT", "description": "Add the horse blood to the heat sterilized medium after
    being cooled to 50°C. Incubate under air plus 5% CO2 or anaerobically under 95%
    N2 plus 5% CO2."}], "decision": "evidence_only", "rationale": "The source requires
    blood addition after cooling. Retain the temperature and ordered stages; the owner
    description is already accurate although its single HEAT action compresses several
    operations."}]}, {"quantity_id": "q13", "topic": "Atmosphere alternatives", "source":
    {"evidence_id": "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Main recipe/preparation", "accessed_at": "2026-10-28T06:49:54.352235Z",
    "quote": "under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2."},
    "decision": "mixed", "rationale": "Keep both alternatives and all gas fractions.
    Aerobic Yes alone does not represent the alternative anoxic source scope.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Keep
    both alternatives and all gas fractions. Aerobic Yes alone does not represent
    the alternative anoxic source scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Keep both alternatives and all gas fractions. Aerobic Yes alone does not represent
    the alternative anoxic source scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "ADJUST_PH", "description": "Adjust pH to 7.6 - 7.8."}, {"step_number": 2, "action":
    "HEAT", "description": "Add the horse blood to the heat sterilized medium after
    being cooled to 50°C. Incubate under air plus 5% CO2 or anaerobically under 95%
    N2 plus 5% CO2."}], "decision": "evidence_only", "rationale": "Keep both alternatives
    and all gas fractions. Aerobic Yes alone does not represent the alternative anoxic
    source scope."}]}, {"quantity_id": "q14", "topic": "pH range", "source": {"evidence_id":
    "dsm779", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium779.pdf",
    "raw_path": "REVIEW_WORK/batch059/source01-03/dsm779.bin", "raw_sha256": "212752dcf33e7ba8aead56be0e4ed9b53849b59226753c3b0050d2e349d41d3b",
    "locator": "Preparation", "accessed_at": "2026-10-28T06:49:54.352235Z", "quote":
    "Adjust pH to 7.6 - 7.8."}, "decision": "evidence_only", "rationale": "Both primary
    and API support pH7.6–7.8; preserve the range rather than inventing a point estimate.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CAPNOCYTOPHAGA_II_MEDIUM.yaml",
    "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision":
    "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve
    the range rather than inventing a point estimate."}, {"path": "data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml",
    "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision":
    "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve
    the range rather than inventing a point estimate."}, {"path": "data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml",
    "field_path": "ph_range", "stored_value": {"min": 7.6, "max": 7.8}, "decision":
    "evidence_only", "rationale": "Both primary and API support pH7.6–7.8; preserve
    the range rather than inventing a point estimate."}]}, {"quantity_id": "q15",
    "topic": "Provider solution volume", "source": {"evidence_id": "api779", "reference":
    "https://mediadive.dsmz.de/rest/medium/779", "raw_path": "REVIEW_WORK/batch059/source01-03/api779.bin",
    "raw_sha256": "47aeebcaf2acc9dfe08f16d959e6299a39f18d1b293d5e830bb9c79829895314",
    "locator": "$.data.solutions[0]", "accessed_at": "2026-10-28T06:49:54.045939Z",
    "quote": "{\n                \"id\": 1584,\n                \"name\": \"Main sol.
    779\",\n                \"volume\": 1050,\n                \"recipe\": [\n                    {\n                        \"recipe_order\":
    1,\n                        \"compound\": \"Lab-Lemco beef extract\",\n                        \"compound_id\":
    599,\n                        \"attribute\": \"Oxoid\",\n                        \"amount\":
    2.4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.4,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    2,\n                        \"compound\": \"Proteose peptone no. 3\",\n                        \"compound_id\":
    316,\n                        \"attribute\": \"Difco\",\n                        \"amount\":
    10,\n                        \"unit\": \"g\",\n                        \"g_l\":
    10,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    3,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\":
    16,\n                        \"attribute\": \"Difco, Bacto\",\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    4,\n                        \"compound\": \"Na2HPO4\",\n                        \"compound_id\":
    233,\n                        \"amount\": 4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 4,\n                        \"mmol_l\":
    28.1771,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    5,\n                        \"compound\": \"Glucose\",\n                        \"compound_id\":
    5,\n                        \"amount\": 1.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\":
    8.32593,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    6,\n                        \"compound\": \"Starch\",\n                        \"compound_id\":
    199,\n                        \"condition\": \"\",\n                        \"attribute\":
    \"soluble\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    7,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\":
    770,\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\":
    2.8468,\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    8,\n                        \"compound\": \"Agar\",\n                        \"compound_id\":
    3,\n                        \"condition\": \"if necessary\",\n                        \"amount\":
    15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    15,\n                        \"mmol_l\": 44.5991,\n                        \"optional\":
    0\n                    },\n                    {\n                        \"recipe_order\":
    9,\n                        \"compound\": \"Horse blood\",\n                        \"compound_id\":
    724,\n                        \"amount\": 50,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    },\n                    {\n                        \"recipe_order\":
    10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\":
    4,\n                        \"amount\": 1000,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }\n                ],\n                \"steps\":
    [\n                    {\n                        \"step\": \"Adjust pH to 7.6
    - 7.8.\"\n                    },\n                    {\n                        \"step\":
    \"Add the horse blood to the heat sterilized medium after being cooled to 50\\u00b0C.
    Incubate under air plus 5% CO2 or anaerobically under 95% N2 plus 5% CO2.\"\n                    }\n                ],\n                \"equipment\":
    {\n                    \"2485\": \"Autoclave\",\n                    \"4408\":
    \"Gassing station\"\n                }\n            }", "exact_decoded_object":
    {"id": 1584, "name": "Main sol. 779", "volume": 1050, "recipe": [{"recipe_order":
    1, "compound": "Lab-Lemco beef extract", "compound_id": 599, "attribute": "Oxoid",
    "amount": 2.4, "unit": "g", "g_l": 2.4, "optional": 0}, {"recipe_order": 2, "compound":
    "Proteose peptone no. 3", "compound_id": 316, "attribute": "Difco", "amount":
    10, "unit": "g", "g_l": 10, "optional": 0}, {"recipe_order": 3, "compound": "Yeast
    extract", "compound_id": 16, "attribute": "Difco, Bacto", "amount": 5, "unit":
    "g", "g_l": 5, "optional": 0}, {"recipe_order": 4, "compound": "Na2HPO4", "compound_id":
    233, "amount": 4, "unit": "g", "g_l": 4, "mmol_l": 28.1771, "optional": 0}, {"recipe_order":
    5, "compound": "Glucose", "compound_id": 5, "amount": 1.5, "unit": "g", "g_l":
    1.5, "mmol_l": 8.32593, "optional": 0}, {"recipe_order": 6, "compound": "Starch",
    "compound_id": 199, "condition": "", "attribute": "soluble", "amount": 0.5, "unit":
    "g", "g_l": 0.5, "optional": 0}, {"recipe_order": 7, "compound": "L-Cysteine HCl
    x H2O", "compound_id": 770, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    2.8468, "optional": 0}, {"recipe_order": 8, "compound": "Agar", "compound_id":
    3, "condition": "if necessary", "amount": 15, "unit": "g", "g_l": 15, "mmol_l":
    44.5991, "optional": 0}, {"recipe_order": 9, "compound": "Horse blood", "compound_id":
    724, "amount": 50, "unit": "ml", "optional": 0}, {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}], "steps": [{"step": "Adjust pH to 7.6 - 7.8."}, {"step": "Add the horse blood
    to the heat sterilized medium after being cooled to 50°C. Incubate under air plus
    5% CO2 or anaerobically under 95% N2 plus 5% CO2."}], "equipment": {"2485": "Autoclave",
    "4408": "Gassing station"}}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "conflict",
    "rationale": "The provider reports 1050 ml, consistent with adding listed water
    and blood volumes, but this is not a primary measured final-volume declaration.
    Its g_l values are not amount/1.05; retain the inconsistency without silently
    dividing all amounts.", "layer_assessments": []}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete histories and evidence were read, but malformed/timezone-unspecified
    historical events and generated evidence omissions remain. Preserve original events
    and append any verified correction context; current source authentication does
    not recover the historical access event.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - history
  - scalars
- assessment_id: a7
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: a9
  area: provenance
  topic: Full historical report scope and rejected recommendations
  outcome: concern
  summary: The Sept22 report is derivative context. Its1050ml final-volume interpretation
    and broad grounding endorsement do not replace the current distinction between
    primary water/input volumes, provider volume/g_l conflict and conditional ingredients.
  target_ids:
  - CultureMech:006440
  evidence_ids:
  - historical-reader
findings:
- finding_id: f1
  issue_key: culturemech-006440-correct-the-horse-blood-liquid-dose
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Correct the horse-blood liquid dose
  description: All three current layers encode the source 50 ml horse-blood input
    as 50 G_PER_L. Preserve the liquid recipe-stage dose and source evidence. Do not
    substitute a mass concentration, infer blood density, or declare a final-medium
    denominator from water plus addition alone.
  target_ids:
  - CultureMech:006440
  field_paths:
  - ingredients[8].concentration
  evidence_ids:
  - dsm779
  - api779
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-006440-resolve-nominal-rates-against-conflicting-provider-volume
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Resolve nominal rates against conflicting provider volume
  description: The eight mass rows retain the provider’s g_l digits, but API solution.volume
    is 1050 and the primary gives batch masses, 1000 ml water and 50 ml blood without
    final-volume makeup. Keep these facts distinct; support the source batch masses
    while marking the unqualified final-medium interpretation unresolved. No automatic
    1.05 division or assumption of a final litre is justified.
  target_ids:
  - CultureMech:006440
  field_paths:
  - ingredients
  - evidence
  evidence_ids:
  - dsm779
  - api779
  - writer-mediadive
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-006440-restore-scoped-preparation-and-source-evidence
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Restore scoped preparation and source evidence
  description: 'The DSMZ owner already retains pH adjustment and blood addition after
    cooling to 50°C with two atmosphere alternatives. The target and KOMODO owner
    omit that preparation and summarize only Aerobic: Yes. Preserve the existing owner
    description, retain ordered stages, and add source-specific root evidence before
    regeneration. Current multi-owner compatibility guards do not establish historical
    causality.'
  target_ids:
  - CultureMech:006440
  field_paths:
  - preparation_steps
  - ph_range
  - notes
  - evidence
  evidence_ids:
  - dsm779
  - owner-2
  - writer-merge
  - writer-formulation
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-006440-retain-uncertain-history-through-append-only-correction
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Retain uncertain history through append-only correction
  description: The KOMODO contributor and its generated copy retain the literal .fZ
    event timestamp and a later timestamp without timezone. Keep original history
    intact; append verified context or a correction event only if authoritative original
    timing becomes available. Do not assign an inferred timezone or rewrite the original
    event.
  target_ids:
  - CultureMech:006440
  field_paths:
  - curation_history[0].timestamp
  - curation_history[1].timestamp
  evidence_ids:
  - local-target
  - owner-1
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: All three current layers encode the source 50 ml horse-blood input
    as 50 G_PER_L. Preserve the liquid recipe-stage dose and source evidence. Do not
    substitute a mass concentration, infer blood density, or declare a final-medium
    denominator from water plus addition alone.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:006440
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: The eight mass rows retain the provider’s g_l digits, but API solution.volume
    is 1050 and the primary gives batch masses, 1000 ml water and 50 ml blood without
    final-volume makeup. Keep these facts distinct; support the source batch masses
    while marking the unqualified final-medium interpretation unresolved. No automatic
    1.05 division or assumption of a final litre is justified.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:006440
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: 'The DSMZ owner already retains pH adjustment and blood addition after
    cooling to 50°C with two atmosphere alternatives. The target and KOMODO owner
    omit that preparation and summarize only Aerobic: Yes. Preserve the existing owner
    description, retain ordered stages, and add source-specific root evidence before
    regeneration. Current multi-owner compatibility guards do not establish historical
    causality.'
  finding_ids:
  - f3
  target_ids:
  - CultureMech:006440
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: The KOMODO contributor and its generated copy retain the literal .fZ
    event timestamp and a later timestamp without timezone. Keep original history
    intact; append verified context or a correction event only if authoritative original
    timing becomes available. Do not assign an inferred timezone or rewrite the original
    event.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:006440
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The initial guessed KOMODO route and the exact historical MediaInfo and MediaList
  routes each returned HTTP403. Current DSMZ/API evidence authenticates the matching
  API bytes and quoted objects, not the unavailable KOMODO table or its historical
  access event.
- 'Final volume remains unresolved: the primary water input and provider volume/g_l
  conflict do not justify an invented corrected final concentration. Blood density
  is unknown.'
- No named strain, growth support or organism identity is supplied by the inspected
  formulation; genus-like medium naming does not establish a specific biological target.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
