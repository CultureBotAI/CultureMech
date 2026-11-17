# Caldanaerovirga: preserve stock stages and DSMZ preparation

- Review: 20261028T055459Z-batch057-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T05:42:12.458299Z
- Finished UTC: 2026-10-28T05:54:59.543337Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The current source supports the reported main rates, but both owners flatten stock components and sum calcium across stages. The generated record omits the DSMZ owner preparation. Nickel/indicator forms and a malformed KOMODO timestamp also need curation; current KOMODO access remains limited.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch057 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:003954 | data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml | generated | caldanaerovirga_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:003954 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:003954 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:003954 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:003954 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact source and contributor boundaries

identity: supported. Targets: CultureMech:003954.

The exact DSMZ1206 PDF title, API accession and local source identifiers correspond. All declared maintained contributors were read completely; source-duplicate links are record-identity context, not permission to equate different preparation content. Same-genus and similarly named neighboring media are outside this review.

### Unchanged classification and growth assertions

scope: supported. Targets: CultureMech:003954.

COMPLEX/UNDEFINED/LIQUID and bacterial filing are consistent with the source formulation and undefined extract. The generic Microbial cultivation application is not strain-level growth evidence. No target organism, temperature optimum or strain-specific growth is inferred from the medium name.

### Positive current and historical source support

evidence: supported. Targets: CultureMech:003954.

All primary main/stock rows and provider g_l assertions were read. Current API raw bytes exactly match the cited October report digest and every quoted JSON object; that establishes byte correspondence without proving the earlier access timestamp or accepting its blanket conflict labels. September per-final-liter stock-dose claims are not copied when the current primary source only supplies batch doses.

### Current writer credit and historical limits

provenance: supported. Targets: CultureMech:003954.

Current MediaDive composition and stock parsers avoid flattening later solutions into direct ingredients. Current cleanup does not sum concentrations, and the merger requires formulation compatibility. Those safeguards are credited. Preparation extraction still flattens solution prose into root steps; none of these current functions proves which historical executable produced an old artifact.

### Supplied-form and current catalog precision

grounding: supported. Targets: CultureMech:003954.

Every primary and secondary identifier is inventoried against its current exact OLS object and preferred-term CSV rows, preserving MAPPED and REJECTED statuses. Most source-explicit salts/hydrates agree; the two specific mismatches are findings. Calcium D-(+)-pantothenate is explicitly source-specified and the current31345 object has corresponding D-calcium synonyms. Generic vitaminB12 and DL-lipoic-acid names are not narrowed to an unsupported vitamer or enantiomer.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:003954.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "KH2PO4 at local direct ingredient index 0", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\": 0.27,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.267062,\n                        \"mmol_l\": 1.96247,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "KH2PO4", "compound_id": 11, "amount": 0.27, "unit": "g", "g_l": 0.267062, "mmol_l": 1.96247, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.267062", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.267062", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.267062", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q2", "topic": "NH4Cl at local direct ingredient index 1", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49456,\n                        \"mmol_l\": 9.24584,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "NH4Cl", "compound_id": 42, "amount": 0.5, "unit": "g", "g_l": 0.49456, "mmol_l": 9.24584, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.49456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.49456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.49456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q3", "topic": "(NH4)2SO4 at local direct ingredient index 2", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.49456,\n                        \"mmol_l\": 3.7427,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "(NH4)2SO4", "compound_id": 27, "amount": 0.5, "unit": "g", "g_l": 0.49456, "mmol_l": 3.7427, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.49456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.49456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.49456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q4", "topic": "TAPS sodium salt at local direct ingredient index 3", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"TAPS sodium salt\",\n                        \"compound_id\": 1083,\n                        \"attribute\": \"SIGMA\",\n                        \"amount\": 2.4,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.37389,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "TAPS sodium salt", "compound_id": 1083, "attribute": "SIGMA", "amount": 2.4, "unit": "g", "g_l": 2.37389, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2.37389", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2.37389", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2.37389", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q5", "topic": "MgCl2 x 6 H2O at local direct ingredient index 4", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0098912,\n                        \"mmol_l\": 0.0486525,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "MgCl2 x 6 H2O", "compound_id": 79, "amount": 0.01, "unit": "g", "g_l": 0.0098912, "mmol_l": 0.0486525, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0098912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0098912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0098912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q6", "topic": "CaCl2 x 2 H2O at local direct ingredient index 5", "source": {"sources": [{"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.0197824,\n                        \"mmol_l\": 0.13456,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.02, "unit": "g", "g_l": 0.0197824, "mmol_l": 0.13456, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.680203, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}]}, "decision": "correct", "rationale": "The local value combines source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral stock. These denominators describe different solutions. Split the two occurrences and retain the stock receiving dose; adding the rates does not give a supported final-medium total. No replacement final total is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.11978240000000001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The local value combines source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral stock. These denominators describe different solutions. Split the two occurrences and retain the stock receiving dose; adding the rates does not give a supported final-medium total. No replacement final total is inferred."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.11978240000000001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The local value combines source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral stock. These denominators describe different solutions. Split the two occurrences and retain the stock receiving dose; adding the rates does not give a supported final-medium total. No replacement final total is inferred."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.11978240000000001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The local value combines source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral stock. These denominators describe different solutions. Split the two occurrences and retain the stock receiving dose; adding the rates does not give a supported final-medium total. No replacement final total is inferred."}]}, {"quantity_id": "q7", "topic": "Yeast extract at local direct ingredient index 6", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.98912,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Yeast extract", "compound_id": 16, "amount": 1, "unit": "g", "g_l": 0.98912, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q8", "topic": "Sodium resazurin at local direct ingredient index 7", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456, "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction. Preserve the percent-defined stock strength and mL dose separately; the reported rate alone omits preparation context.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00049456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction. Preserve the percent-defined stock strength and mL dose separately; the reported rate alone omits preparation context."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00049456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction. Preserve the percent-defined stock strength and mL dose separately; the reported rate alone omits preparation context."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00049456", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction. Preserve the percent-defined stock strength and mL dose separately; the reported rate alone omits preparation context."}]}, {"quantity_id": "q9", "topic": "NaHCO3 at local direct ingredient index 8", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.48368,\n                        \"mmol_l\": 17.6614,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "NaHCO3", "compound_id": 55, "amount": 1.5, "unit": "g", "g_l": 1.48368, "mmol_l": 17.6614, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.48368", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.48368", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.48368", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q10", "topic": "D-Xylose at local direct ingredient index 9", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"D-Xylose\",\n                        \"compound_id\": 422,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 2.96736,\n                        \"mmol_l\": 19.7653,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "D-Xylose", "compound_id": 422, "amount": 3, "unit": "g", "g_l": 2.96736, "mmol_l": 19.7653, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "2.96736", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "2.96736", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "2.96736", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q11", "topic": "L-Cysteine HCl x H2O at local direct ingredient index 10", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.24728,\n                        \"mmol_l\": 1.40791,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.25, "unit": "g", "g_l": 0.24728, "mmol_l": 1.40791, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.24728", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.24728", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.24728", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q12", "topic": "Na2S x 9 H2O at local direct ingredient index 11", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.25,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.24728,\n                        \"mmol_l\": 1.02955,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 0.25, "unit": "g", "g_l": 0.24728, "mmol_l": 1.02955, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.24728", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.24728", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.24728", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution row explicitly reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL water input, not an independent final-volume instruction."}]}, {"quantity_id": "q13", "topic": "Nitrilotriacetic acid at local direct ingredient index 12", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Nitrilotriacetic acid", "compound_id": 189, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 7.84765, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q14", "topic": "MgSO4 x 7 H2O at local direct ingredient index 13", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 3,\n                        \"unit\": \"g\",\n                        \"g_l\": 3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 3, "unit": "g", "g_l": 3, "mmol_l": 12.1716, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q15", "topic": "MnSO4 x H2O at local direct ingredient index 14", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "MnSO4 x H2O", "compound_id": 14, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 2.9583, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q16", "topic": "NaCl at local direct ingredient index 15", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "NaCl", "compound_id": 43, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 17.1116, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q17", "topic": "FeSO4 x 7 H2O at local direct ingredient index 16", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\": 0.1,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l": 0.359693, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q18", "topic": "CoSO4 x 7 H2O at local direct ingredient index 17", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoSO4 x 7 H2O", "compound_id": 198, "amount": 0.18, "unit": "g", "g_l": 0.18, "mmol_l": 1.16132, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q19", "topic": "ZnSO4 x 7 H2O at local direct ingredient index 18", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\": 0.18,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.18, "unit": "g", "g_l": 0.18, "mmol_l": 0.625954, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q20", "topic": "CuSO4 x 5 H2O at local direct ingredient index 19", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0400503, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q21", "topic": "AlK(SO4)2 x 12 H2O at local direct ingredient index 20", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\": 0.02,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "AlK(SO4)2 x 12 H2O", "compound_id": 908, "amount": 0.02, "unit": "g", "g_l": 0.02, "mmol_l": 0.0421596, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q22", "topic": "H3BO3 at local direct ingredient index 21", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "H3BO3", "compound_id": 37, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.161708, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q23", "topic": "Na2MoO4 x 2 H2O at local direct ingredient index 22", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[11]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 0.01,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l": 0.0413309, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q24", "topic": "NiCl2 x 6 H2O at local direct ingredient index 23", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[12]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 0.03,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.03, "unit": "g", "g_l": 0.03, "mmol_l": 0.231483, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q25", "topic": "Na2SeO3 x 5 H2O at local direct ingredient index 24", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[13]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\": 0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound": "Na2SeO3 x 5 H2O", "compound_id": 107, "amount": 0.3, "unit": "mg", "g_l": 0.0003, "mmol_l": 0.00114062, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.0003", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.0003", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.0003", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q26", "topic": "Na2WO4 x 2 H2O at local direct ingredient index 25", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[14]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\": 0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound": "Na2WO4 x 2 H2O", "compound_id": 249, "amount": 0.4, "unit": "mg", "g_l": 0.0004, "mmol_l": 0.00121267, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.0004", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.0004", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.0004", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Modified Wolin's mineral solution. It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q27", "topic": "Biotin at local direct ingredient index 26", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Biotin", "compound_id": 46, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q28", "topic": "Folic acid at local direct ingredient index 27", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\": 20,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Folic acid", "compound_id": 138, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l": 0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q29", "topic": "Pyridoxine hydrochloride at local direct ingredient index 28", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "Pyridoxine hydrochloride", "compound_id": 519, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.486287, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q30", "topic": "Thiamine HCl at local direct ingredient index 29", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "Thiamine HCl", "compound_id": 1207, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.148236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q31", "topic": "Riboflavin at local direct ingredient index 30", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Riboflavin", "compound_id": 136, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q32", "topic": "Nicotinic acid at local direct ingredient index 31", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Nicotinic acid", "compound_id": 139, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q33", "topic": "Calcium D-(+)-pantothenate at local direct ingredient index 32", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "Calcium D-(+)-pantothenate", "compound_id": 1512, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.209846, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q34", "topic": "Vitamin B12 at local direct ingredient index 33", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\": 1,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "Vitamin B12", "compound_id": 18, "amount": 1, "unit": "mg", "g_l": 0.001, "mmol_l": 0.00073779, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q35", "topic": "p-Aminobenzoic acid at local direct ingredient index 34", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "p-Aminobenzoic acid", "compound_id": 47, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q36", "topic": "(DL)-alpha-Lipoic acid at local direct ingredient index 35", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[9]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\": 50,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "(DL)-alpha-Lipoic acid", "compound_id": 252, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l": 0.24233, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees exactly with the provider g_l for Wolin's vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium rate. Move the source-specific component into its stock representation and preserve the separately reported receiving dose. The PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id": "q37", "topic": "Main sol. 1206 / Modified Wolin's mineral solution", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Modified Wolin's mineral solution\",\n                        \"solution_id\": 241,\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "solution": "Modified Wolin's mineral solution", "solution_id": 241, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "The source supplies 10mL of Modified Wolin's mineral solution at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 10mL of Modified Wolin's mineral solution at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 10mL of Modified Wolin's mineral solution at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 10mL of Modified Wolin's mineral solution at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}]}, {"quantity_id": "q38", "topic": "Main sol. 1206 / Sodium resazurin", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\": 0.00196902,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456, "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage with attribute 0.1% w/v. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage with attribute 0.1% w/v. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage with attribute 0.1% w/v. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage with attribute 0.1% w/v. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}]}, {"quantity_id": "q39", "topic": "Main sol. 1206 / Wolin's vitamin solution (10x)", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\": \"Wolin's vitamin solution (10x)\",\n                        \"solution_id\": 5980,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "solution": "Wolin's vitamin solution (10x)", "solution_id": 5980, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "The source supplies 1mL of Wolin's vitamin solution (10x) at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 1mL of Wolin's vitamin solution (10x) at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 1mL of Wolin's vitamin solution (10x) at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The source supplies 1mL of Wolin's vitamin solution (10x) at the receiving-medium batch stage. Create the missing solution descriptor and retain this literal dose and source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L without the final-medium denominator; do not double-count the stock and its expanded components.", "missing": true}]}, {"quantity_id": "q40", "topic": "Main sol. 1206 / Distilled water", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "Retain this exact 1000mL water input for Main sol. 1206 in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain this exact 1000mL water input for Main sol. 1206 in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain this exact 1000mL water input for Main sol. 1206 in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "AUTOCLAVE", "description": "Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary."}, {"step_number": 2, "action": "ADJUST_PH", "description": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}], "decision": "add", "rationale": "Retain this exact 1000mL water input for Main sol. 1206 in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row."}]}, {"quantity_id": "q41", "topic": "Modified Wolin's mineral solution / Distilled water", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].recipe[15]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "Retain this exact 1000mL water input for Modified Wolin's mineral solution in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain this exact 1000mL water input for Modified Wolin's mineral solution in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain this exact 1000mL water input for Modified Wolin's mineral solution in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "AUTOCLAVE", "description": "Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary."}, {"step_number": 2, "action": "ADJUST_PH", "description": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}], "decision": "add", "rationale": "Retain this exact 1000mL water input for Modified Wolin's mineral solution in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row."}]}, {"quantity_id": "q42", "topic": "Wolin's vitamin solution (10x) / Distilled water", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[2].recipe[10]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "add", "rationale": "Retain this exact 1000mL water input for Wolin's vitamin solution (10x) in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain this exact 1000mL water input for Wolin's vitamin solution (10x) in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain this exact 1000mL water input for Wolin's vitamin solution (10x) in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action": "AUTOCLAVE", "description": "Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary."}, {"step_number": 2, "action": "ADJUST_PH", "description": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}], "decision": "add", "rationale": "Retain this exact 1000mL water input for Wolin's vitamin solution (10x) in stage-specific preparation or root evidence. It is not a direct solute ingredient or automatically a final-volume makeup. No independent final-volume conversion is made from this row."}]}, {"quantity_id": "q43", "topic": "Main sol. 1206 preparation context", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"step\": \"Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "Read and retain the entire Main sol. 1206 step, including all pH, gas fractions, duration, liquid/normality/filter-pore values where present. Existing matching descriptions are credited; missing descriptions need source-scoped addition. An action enum does not fully encode the multi-operation paragraph.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "This source step is missing from this record; add only the supported stage-specific instruction with root evidence, preserving existing other-stage prose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "This source step is missing from this record; add only the supported stage-specific instruction with root evidence, preserving existing other-stage prose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary.", "decision": "evidence_only", "rationale": "The complete numeric and procedural text matches this source solution step. Retain its contents, but explicitly scope it to Main sol. 1206 rather than treating all stock steps as a sequence on the final medium."}]}, {"quantity_id": "q44", "topic": "Modified Wolin's mineral solution preparation context", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"step\": \"First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.\"\n                    }", "exact_decoded_object": {"step": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "mixed", "rationale": "Read and retain the entire Modified Wolin's mineral solution step, including all pH, gas fractions, duration, liquid/normality/filter-pore values where present. Existing matching descriptions are credited; missing descriptions need source-scoped addition. An action enum does not fully encode the multi-operation paragraph.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "This source step is missing from this record; add only the supported stage-specific instruction with root evidence, preserving existing other-stage prose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "This source step is missing from this record; add only the supported stage-specific instruction with root evidence, preserving existing other-stage prose.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "First dissolve nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with KOH.", "decision": "evidence_only", "rationale": "The complete numeric and procedural text matches this source solution step. Retain its contents, but explicitly scope it to Modified Wolin's mineral solution rather than treating all stock steps as a sequence on the final medium."}]}, {"quantity_id": "q45", "topic": "Main-medium pH", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.medium", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n            \"id\": 1206,\n            \"name\": \"CALDANAEROVIRGA MEDIUM\",\n            \"complex_medium\": \"yes\",\n            \"min_pH\": 8.5,\n            \"max_pH\": 8.5,\n            \"source\": \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1206.pdf\"\n        }", "exact_decoded_object": {"id": 1206, "name": "CALDANAEROVIRGA MEDIUM", "complex_medium": "yes", "min_pH": 8.5, "max_pH": 8.5, "source": "DSMZ", "link": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1206.pdf"}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The stored ph_value matches the exact main-medium pH reported by the PDF and API. This is distinct from the mineral-stock pH adjustment; source titration amounts are not quantified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 8.5, "decision": "evidence_only", "rationale": "The stored ph_value matches the exact main-medium pH reported by the PDF and API. This is distinct from the mineral-stock pH adjustment; source titration amounts are not quantified."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path": "ph_value", "stored_value": 8.5, "decision": "evidence_only", "rationale": "The stored ph_value matches the exact main-medium pH reported by the PDF and API. This is distinct from the mineral-stock pH adjustment; source titration amounts are not quantified."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ph_value", "stored_value": 8.5, "decision": "evidence_only", "rationale": "The stored ph_value matches the exact main-medium pH reported by the PDF and API. This is distinct from the mineral-stock pH adjustment; source titration amounts are not quantified."}]}, {"quantity_id": "q46", "topic": "Unquantified late-stock and sterilization details", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote": "{\n                        \"step\": \"Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if necessary."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, "decision": "not_quantified", "rationale": "The source specifies sterile late stock additions and stage-specific gases/filtration but does not supply fixed concentrations and addition volumes for every late solute stock, titrant amounts, or a numeric autoclave temperature/duration. Preserve these limits; do not infer common settings or concentrations.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:003954.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: supported. Targets: CultureMech:003954.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:003954.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:003954.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Mineral and vitamin stocks are flattened into direct ingredients

major / open / confirmed; issue key: culturemech-003954-mineral-and-vitamin-stocks-are-flattened-into-direct-ingredients.

The exact source defines Modified Wolin's mineral solution and Wolin's vitamin solution (10x) as separate stock formulations with separate receiving mL doses. The selected target and maintained contributors place the stock components directly under ingredients at their stock g/L values and have no solutions descriptors. This is a stage error even where the stock numbers themselves match the provider. Preserve the source stock recipes and receiving doses; do not dilute or sum them by an assumed final liter.

### f2: Repeated chemical occurrences were summed across main and stock stages

major / open / confirmed; issue key: culturemech-003954-repeated-chemical-occurrences-were-summed-across-main-and-stock-stages.

CaCl2 x 2 H2O is stored as 0.11978240000000001 g/L, with a note recording a two-value sum. The current source instead distinguishes a main-medium occurrence and a mineral-stock occurrence. Adding concentrations from different source solutions is invalid as a final-medium total because the concentrations refer to different solution-stage bases; retain two scoped occurrences and resolve the receiving denominator before any final total. The current cleanup implementation does not perform this historical sum.

### f3: Nickel hydrate and sodium indicator forms are not represented by their identifiers

major / open / confirmed; issue key: culturemech-003954-nickel-hydrate-and-sodium-indicator-forms-are-not-represented-by-their-identifiers.

NiCl2 x6H2O is assigned CHEBI:34887, whose current OLS object describes NiCl2 without the six waters. Sodium resazurin uses primary CHEBI:8806 Resazurin, which does not establish the sodium-salt form. The secondary nickel link repeats the mismatch; the resazurin node has no secondary slot to accuse. Current catalog membership and canonical label agreement do not cure supplied-form mismatch. Verify an exact supplied-form mapping or retain the precise source name with an explicit unresolved mapping; no replacement identifier is guessed.

### f4: The generated record omits supported preparation and loses stage boundaries

major / open / confirmed; issue key: culturemech-003954-the-generated-record-omits-supported-preparation-and-loses-stage-boundaries.

The DSMZ owner retains both source preparation paragraphs, including main pH8.5,30–45min gas treatment, late stocks and mineral-stock pH6.5 then7.0. The selected generated record and KOMODO owner have no preparation_steps. Credit the retained DSMZ text while restoring missing supported instructions and stage attribution. Reconcile the two contributors before regeneration; current exact-formulation merging rejects incompatible preparation assertions.

### f5: The KOMODO import timestamp is malformed and its original table remains unauthenticated

minor / open / confirmed; issue key: culturemech-003954-the-komodo-import-timestamp-is-malformed-and-its-original-table-remains-unauthenticated.

The target and KOMODO owner store curation_history[0].timestamp as2026-01-27T01:15:01.fZ, which is not a valid fractional-second timestamp. The original KOMODO table is not authenticated by the current403 endpoint or the derivative catalog excerpt. The current DSMZ response does authenticate the separately cited API bytes. Retain the malformed original event unchanged. If authoritative provenance is recovered, append a new verified correction or context event that explains it; never rewrite the original timestamp or invent a date.

## Recommended Actions And Acceptance Checks

### action1

Curate the maintained contributors to represent each mineral/vitamin stock and its receiving dose separately. Preserve source-specific stock g/L claims and PDF batch amounts with exact evidence. Remove their false direct-medium placement, then regenerate; do not double-count stock expansions or invent a working concentration.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

CaCl2 x 2 H2O is stored as 0.11978240000000001 g/L, with a note recording a two-value sum. The current source instead distinguishes a main-medium occurrence and a mineral-stock occurrence. Adding concentrations from different source solutions is invalid as a final-medium total because the concentrations refer to different solution-stage bases; retain two scoped occurrences and resolve the receiving denominator before any final total. The current cleanup implementation does not perform this historical sum.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

NiCl2 x6H2O is assigned CHEBI:34887, whose current OLS object describes NiCl2 without the six waters. Sodium resazurin uses primary CHEBI:8806 Resazurin, which does not establish the sodium-salt form. The secondary nickel link repeats the mismatch; the resazurin node has no secondary slot to accuse. Current catalog membership and canonical label agreement do not cure supplied-form mismatch. Verify an exact supplied-form mapping or retain the precise source name with an explicit unresolved mapping; no replacement identifier is guessed.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Retain the DSMZ owner preparation text, label the mineral-stock procedure explicitly, and preserve it in the generated result after source-duplicate reconciliation. Add exact root evidence for process and pH claims; leave unquantified late stock strengths and sterilization settings unspecified.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

The target and KOMODO owner store curation_history[0].timestamp as2026-01-27T01:15:01.fZ, which is not a valid fractional-second timestamp. The original KOMODO table is not authenticated by the current403 endpoint or the derivative catalog excerpt. The current DSMZ response does authenticate the separately cited API bytes. Retain the malformed original event unchanged. If authoritative provenance is recovered, append a new verified correction or context event that explains it; never rewrite the original timestamp or invent a date.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| dsm1206 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1206.pdf; Pages1–2, exact numbered medium; main table and separately headed mineral/vitamin subsections | supports | Both complete PDF pages and rendered page images were read. Exact named formulation, all main and stock rows, source-specific chemical forms, water inputs and preparation stages are retained. No neighboring medium is substituted. |
| api1206 | https://mediadive.dsmz.de/rest/medium/1206; $.data.medium and $.data.solutions[0..2] including recipe/steps/volume | supports | Full current official API medium object, every ordered solution recipe and preparation object were read. Explicit g_l reports retain their named stage. PDF water inputs and provider volume metadata are assessed independently. The raw digest also matches the exact October historical report response. |
| komodo1206 | https://komodo.modelseed.org/servlet/Komodo?Mediumnumber=1206; Exact attempted endpoint and HTTP403 response | unknown | The bounded current KOMODO request returned HTTP403. It does not independently authenticate the original KOMODO table; the local cross-reference and historical catalog excerpt remain separately scoped. |
| identity-search | REVIEW_WORK/batch057/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current composition parser restricts ingredients to the primary solution, excludes solvent and recognized stock additions, and retains explicit g_l. The solution parser preserves referenced or percent-defined stocks and source attributes. Preparation parsing still concatenates all solution steps into root preparation_steps; source-stage annotation remains important. These present functions do not prove the historical execution that produced this record. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. The current code is not proof of the earlier summed value. |
| historical-1 | reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/caldanaerovirga_medium.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 44 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-2 | reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml.md; Entire exact Record-header report, every claim row and narrative | context_only | Current independently captured API response has exactly the cited historical raw SHA256; all 44 literal JSON snippets and locators match. This authenticates those response bytes, not the historical access time or recommendations. |
| historical-3 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-4 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caldanaerovirga_medium.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-6 | reports/yaml_record_review/20260922T015523Z-CALDANAEROVIRGA_MEDIUM.md; Entire exact Record-header report, every claim row and narrative | context_only | Full historical report read as derivative context. Its old validation/access claims are not independently authenticated; unsupported fixed-final-liter assumptions are not adopted. |
| historical-reader | REVIEW_WORK/batch057/record01/historical-reader.json | context_only | All exact target/owner historical report texts and current raw/literal/locator joins; historical recommendations remain subject to current stage and volume evidence. |
| source-rows | REVIEW_WORK/batch057/record01/source-row-inventory.json | context_only | Every source main/stock recipe row, including omitted solvents and stock doses, with literal raw object, exact locator and named stage. |
| chebi63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi62946 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62946; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32139 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi65327 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_65327; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi44557 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86364; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91244 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91244; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86465; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131361; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63939; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch057/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch057/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch057/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch057/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch057/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch057/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch057/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch057/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch057/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- No organism-specific growth or missing sterilization settings are inferred. The review addresses the exact source formulation and maintained contributors; neighboring or parent medium recipes are not transferred wholesale.
- Current OLS and the pinned packaged MIM catalog describe current identifier correspondence, not historical mapping validity. No molecular-weight, density or mmol/L conversion was used.
- Historical report raw-digest matches authenticate the current matching API response bytes and exact snippets, not the recorded old access events, old executables, or all historical scientific conclusions.
- No fixed late-stock concentration or addition volume is invented where the source provides only a sterile-addition instruction. Exact source batches and explicitly reported source-stage g/L values remain distinct.
- The current bounded KOMODO request returned403. The old catalog excerpt is derivative identity context; its complete original catalog response was not recovered in this review. The local cross-reference and current DSMZ primary/provider sources remain directly assessed.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T055459Z-batch057-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Caldanaerovirga: preserve stock stages and DSMZ preparation'
started_at: '2026-10-28T05:42:12.458299Z'
finished_at: '2026-10-28T05:54:59.543337Z'
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
summary: The current source supports the reported main rates, but both owners flatten
  stock components and sum calcium across stages. The generated record omits the DSMZ
  owner preparation. Nickel/indicator forms and a malformed KOMODO timestamp also
  need curation; current KOMODO access remains limited.
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
  - path: data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
    sha256: 4e1d48f6739130fc618e9b83102bf80a20f9d4a87b24186b325114a4ec2dbdcc
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    sha256: 57f55c6612d071b9daf88f31853866eeefa4bfe0067a9a93459587741595c170
    role: context
  - path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    sha256: 847f9ffa81b9a3d99f675ce4f71e1ab4818134f8782fa2a9871281f8a0cf1be9
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
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/caldanaerovirga_medium.yaml.md
    sha256: fb9c7d0d7e4d7fce81dd6939af9508a7e260e6aab85919ff8825ec39878d6cc2
    role: context
  - path: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml.md
    sha256: bac5cd2c3a6d281ae54c38d8f8eacc166c5e6d81eefe9f6309f1b8e39f45f6cd
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.md
    sha256: 743be26c89cdc6d824a07cd21889fd033cf07e672cd205cec89c05c2ff00a25a
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.md
    sha256: e4a02358ce029c096727493347cc895c561d50e0d6b03e9f35ee55a02838d65d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caldanaerovirga_medium.md
    sha256: 9b56c39ec4b017e17233bad25aac3021de10e3cf184308aee989bd8d6dbb50d8
    role: context
  - path: reports/yaml_record_review/20260922T015523Z-CALDANAEROVIRGA_MEDIUM.md
    sha256: 14c9b008a2163b07b9a1e90f8c6e5aa5aa45b63f00d5669cc454bfd1e1a974c6
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
  selection: Actual batch057 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:003954
targets:
- target_id: CultureMech:003954
  path: data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
  label: caldanaerovirga_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:003954
  command: just validate-schema data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
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
  - CultureMech:003954
  command: just validate-strict data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
    --out REVIEW_WORK/batch057/record01/strict.tsv --workers 1
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
  - CultureMech:003954
  command: just validate-terms data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
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
  - CultureMech:003954
  command: just validate-references data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 4e1d48f6739130fc618e9b83102bf80a20f9d4a87b24186b325114a4ec2dbdcc
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 57f55c6612d071b9daf88f31853866eeefa4bfe0067a9a93459587741595c170
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 847f9ffa81b9a3d99f675ce4f71e1ab4818134f8782fa2a9871281f8a0cf1be9
- evidence_id: dsm1206
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1206.pdf
  locator: Pages1–2, exact numbered medium; main table and separately headed mineral/vitamin
    subsections
  accessed_at: '2026-10-28T05:42:27.354537Z'
  support: supports
  summary: Both complete PDF pages and rendered page images were read. Exact named
    formulation, all main and stock rows, source-specific chemical forms, water inputs
    and preparation stages are retained. No neighboring medium is substituted.
  snapshot_sha256: 15f435a151f9f3988361d6d24f72bc5dab2b3a5bd6ecf476f7cf3c7354d680cf
- evidence_id: api1206
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1206
  locator: $.data.medium and $.data.solutions[0..2] including recipe/steps/volume
  accessed_at: '2026-10-28T05:42:27.180766Z'
  support: supports
  summary: Full current official API medium object, every ordered solution recipe
    and preparation object were read. Explicit g_l reports retain their named stage.
    PDF water inputs and provider volume metadata are assessed independently. The
    raw digest also matches the exact October historical report response.
  snapshot_sha256: e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a
- evidence_id: komodo1206
  kind: database
  reference: https://komodo.modelseed.org/servlet/Komodo?Mediumnumber=1206
  locator: Exact attempted endpoint and HTTP403 response
  accessed_at: '2026-10-28T05:42:27.425572Z'
  support: unknown
  summary: The bounded current KOMODO request returned HTTP403. It does not independently
    authenticate the original KOMODO table; the local cross-reference and historical
    catalog excerpt remain separately scoped.
  snapshot_sha256: 0d387b6055ec03d4d80005a0089404f501706fdab2efac2607e011504d6d6cf3
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch057/record01/identity-search.json
  accessed_at: '2026-10-28T05:48:36.393665Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems resolved uniquely. Similar names and
    source accessions are not promoted to owners.
  snapshot_sha256: c4f023372af4b61c9f9c66ec8e95143758cf680958fc057b034d4b68044c0c4d
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T05:48:36.331614Z'
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
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T05:48:36.331614Z'
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
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. The current code is not proof of the earlier summed
    value.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-1000-1500/records/bacterial/caldanaerovirga_medium.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 44 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: fb9c7d0d7e4d7fce81dd6939af9508a7e260e6aab85919ff8825ec39878d6cc2
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261008-komodo-media-3000-3633/records/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Current independently captured API response has exactly the cited historical
    raw SHA256; all 44 literal JSON snippets and locators match. This authenticates
    those response bytes, not the historical access time or recommendations.
  snapshot_sha256: bac5cd2c3a6d281ae54c38d8f8eacc166c5e6d81eefe9f6309f1b8e39f45f6cd
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 743be26c89cdc6d824a07cd21889fd033cf07e672cd205cec89c05c2ff00a25a
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: e4a02358ce029c096727493347cc895c561d50e0d6b03e9f35ee55a02838d65d
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/caldanaerovirga_medium.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 9b56c39ec4b017e17233bad25aac3021de10e3cf184308aee989bd8d6dbb50d8
- evidence_id: historical-6
  kind: record_content
  reference: reports/yaml_record_review/20260922T015523Z-CALDANAEROVIRGA_MEDIUM.md
  locator: Entire exact Record-header report, every claim row and narrative
  accessed_at: '2026-10-28T05:48:36.331614Z'
  support: context_only
  summary: Full historical report read as derivative context. Its old validation/access
    claims are not independently authenticated; unsupported fixed-final-liter assumptions
    are not adopted.
  snapshot_sha256: 14c9b008a2163b07b9a1e90f8c6e5aa5aa45b63f00d5669cc454bfd1e1a974c6
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch057/record01/historical-reader.json
  accessed_at: '2026-10-28T05:48:36.397108Z'
  support: context_only
  summary: All exact target/owner historical report texts and current raw/literal/locator
    joins; historical recommendations remain subject to current stage and volume evidence.
  snapshot_sha256: 4da6ca6c4834da078a78f60ce15f73f784de5b0615f75d5c1392a2ec7393e4af
- evidence_id: source-rows
  kind: record_content
  reference: REVIEW_WORK/batch057/record01/source-row-inventory.json
  accessed_at: '2026-10-28T05:48:36.403061Z'
  support: context_only
  summary: Every source main/stock recipe row, including omitted solvents and stock
    doses, with literal raw object, exact locator and named stage.
  snapshot_sha256: 493af1a02f46cbdbf70a50325d90e70bcf9e4f34765de740d6833bfbbebb060f
- evidence_id: chebi63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63036
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:33.017116Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 913baf38abc38dd61f05c5d636fd6532b70a668673a1f5762f290d2b67270164
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:30.448057Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi62946
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62946
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:32.527031Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b52cb60c424f5c8262c2b335bf4b428324d0e53dc8b9cbfbd77494460877275d
- evidence_id: chebi86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:34.302277Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 015a33a158257cc5cba8a8e62de382053399be060366af5d95074883bb22b86e
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:34.092685Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:34.891969Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi32139
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32139
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:31.068713Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 314c75cd12ea5d1343b4c0bafd40e0ad72c15b19d64f8cb9152000c0d8839f56
- evidence_id: chebi65327
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_65327
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:33.496348Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1c3d0bcba6bfbadb2841765845cd5508968318e09c01be95e14c90372ac063a2
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:35.413690Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:33.711303Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: chebi44557
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_44557
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:31.809954Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 371aa3b809db6c5d1ec8f8b8be40011e6b1132b1c0be40e70fb927788728d65a
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:30.715050Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86364
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:34.724384Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0e8fbfc2ee82502bd7a5b4b3ba6cfaaae0ad1779400d07af8e2e0f726af793e9
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:29.428692Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:33.708758Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: e12b865122aab78645385260e1e83ff28f3c45365cb67c9181166628f68974b3
- evidence_id: chebi91244
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91244
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:35.306722Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 4b8d2689d3b68919586644a832e86d7a50b6b619c20295d55212660c7f794a55
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:31.218452Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6bf1390236046f1cb7b21e2fc324fccba6e6eac2bc4e519f12d998f0edce671b
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:30.619943Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 453e496e1e59b82bb42cd3252d410b9dc77d0c11e49f3da70496a82978e80505
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86465
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:34.900885Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a92ebf989cf31be7db75a945ec7fe016d45b72d65e2a8b7f0522d3670209a527
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:31.313739Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:33.627010Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:31.662896Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131361
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:28.104258Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 345cb9c46670b2812cacd12098169f03ea94fe064710e06a7aa545a2717706b0
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_63939
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:33.090976Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f2fb7b5c3e7fec44d19e40f18cfbfa699c6010ad22cb76a9d2acd2b60950d98e
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:28.752945Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0d2e75e0bd98dbffff14d85a41dfd0af8aae2a8d65a945d34a4126a17091c2b8
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:29.839559Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dcee85bb585d3a73341ab66eff772dc6361330b3c899c4daecbda49d5e84e590
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:30.111150Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 491af523ba70d13857fcb828561d0556e46382fa0591011a06693d7db24ad91f
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:31.828852Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: fc6b8e9d8657914ed8fd568c69d8a5b2cf41b26767bd6361a5e2d258883be97d
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:29.185641Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f8bec809c7ba5a36faea58b8fe1b5110f0d75dbd4ac1929a121cd352bce63309
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:28.778119Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2890ef915cd546e70c1e638af285a3cc19b8299ae7722d00b43a40170a57ab8a
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:30.610996Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d2a04309eb6976fd395f9684ec4c3f5192362e2b6b75464b0af128a28e188d25
- evidence_id: chebi176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_176843
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:29.374907Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5c42e2236866d0314bc8d45947ddf9eb2fdf6364d08e802b0fb271011cbfe563
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:30.005514Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 42ea4022bd68e8fa28962bc496ca757174da7bbd18ce06b7f3d521885609a50c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:42:28.831921Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: db6824ffab0d71efc11d1e64b505ae583949e9d5837086a4b0e7b364b2933a22
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch057/record01/quantity-inventory.json
  accessed_at: '2026-10-28T05:48:36.474709Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 5a712726a2c846cb05def6c92840348080fc357897ca1ac4a8baf9163a7a46a5
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch057/record01/grounding-inventory.json
  accessed_at: '2026-10-28T05:48:36.474801Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: e44e346c2ec1088a0d2633cc37c4955f8b306052cb9e0394038ad56ceadf920d
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch057/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T05:48:36.475039Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 47f14c3c5cf58fc8da3a9341e81410e0b64f66ec49a8a3027212f98cc87c9fa9
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch057/record01/scalar-census.json
  accessed_at: '2026-10-28T05:48:36.475066Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 477e3b981ea0c836ee5cb37b9a5ce49770f30193aca25484a0e556a048b5a7eb
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch057/record01/validate-schema.json
  accessed_at: '2026-10-28T05:42:13.556630Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: e947ed37a2db3693b84390d1ce79b1384245d84b048fa71f0c2343703aaf1d25
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch057/record01/validate-strict.json
  accessed_at: '2026-10-28T05:42:14.537615Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch057/record01/strict.tsv\n"
  snapshot_sha256: 57ada32cf41b314be201ed2c298628f753697bb6cf76bb1b25a33dcc965aa2b3
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch057/record01/validate-terms.json
  accessed_at: '2026-10-28T05:42:15.603582Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: d1cf8cc24fa7dfdbdaad107314b63d600859dc8be31acb494837f6fa5bca186b
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch057/record01/validate-references.json
  accessed_at: '2026-10-28T05:42:16.385973Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 756c1d4e3b6f88446c322188f61311393a8a5af562c4135350b451d63d0d6fe4
assessments:
- assessment_id: a1
  area: identity
  topic: Exact source and contributor boundaries
  outcome: supported
  summary: The exact DSMZ1206 PDF title, API accession and local source identifiers
    correspond. All declared maintained contributors were read completely; source-duplicate
    links are record-identity context, not permission to equate different preparation
    content. Same-genus and similarly named neighboring media are outside this review.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - identity-search
  - dsm1206
  - api1206
  - local-target
- assessment_id: a2
  area: scope
  topic: Unchanged classification and growth assertions
  outcome: supported
  summary: COMPLEX/UNDEFINED/LIQUID and bacterial filing are consistent with the source
    formulation and undefined extract. The generic Microbial cultivation application
    is not strain-level growth evidence. No target organism, temperature optimum or
    strain-specific growth is inferred from the medium name.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - local-target
  - dsm1206
- assessment_id: a3
  area: evidence
  topic: Positive current and historical source support
  outcome: supported
  summary: All primary main/stock rows and provider g_l assertions were read. Current
    API raw bytes exactly match the cited October report digest and every quoted JSON
    object; that establishes byte correspondence without proving the earlier access
    timestamp or accepting its blanket conflict labels. September per-final-liter
    stock-dose claims are not copied when the current primary source only supplies
    batch doses.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - historical-reader
  - api1206
  - dsm1206
  - source-rows
- assessment_id: a4
  area: provenance
  topic: Current writer credit and historical limits
  outcome: supported
  summary: Current MediaDive composition and stock parsers avoid flattening later
    solutions into direct ingredients. Current cleanup does not sum concentrations,
    and the merger requires formulation compatibility. Those safeguards are credited.
    Preparation extraction still flattens solution prose into root steps; none of
    these current functions proves which historical executable produced an old artifact.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - writer-mediadive
  - writer-cleanup
  - writer-merge
  - writer-formulation
- assessment_id: a5
  area: grounding
  topic: Supplied-form and current catalog precision
  outcome: supported
  summary: Every primary and secondary identifier is inventoried against its current
    exact OLS object and preferred-term CSV rows, preserving MAPPED and REJECTED statuses.
    Most source-explicit salts/hydrates agree; the two specific mismatches are findings.
    Calcium D-(+)-pantothenate is explicitly source-specified and the current31345
    object has corresponding D-calcium synonyms. Generic vitaminB12 and DL-lipoic-acid
    names are not narrowed to an unsupported vitamer or enantiomer.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - grounding
  - dsm1206
- assessment_id: a6
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "KH2PO4 at local direct ingredient index
    0", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"KH2PO4\",\n                        \"compound_id\": 11,\n                        \"amount\":
    0.27,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.267062,\n                        \"mmol_l\": 1.96247,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "KH2PO4", "compound_id": 11, "amount": 0.27, "unit": "g", "g_l": 0.267062, "mmol_l":
    1.96247, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "evidence_only",
    "rationale": "The exact current main-solution row explicitly reports this g_l
    value. Retain the number with scoped evidence; no mineral/vitamin stock rate is
    transferred into it. The API main-solution volume1011mL is consistent with these
    reported rates; the PDF itself gives a1000mL water input, not an independent final-volume
    instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.267062",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.267062",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.267062",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q2", "topic": "NH4Cl at local direct ingredient index 1", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.49456,\n                        \"mmol_l\": 9.24584,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "NH4Cl", "compound_id": 42, "amount": 0.5, "unit": "g", "g_l": 0.49456, "mmol_l":
    9.24584, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "evidence_only",
    "rationale": "The exact current main-solution row explicitly reports this g_l
    value. Retain the number with scoped evidence; no mineral/vitamin stock rate is
    transferred into it. The API main-solution volume1011mL is consistent with these
    reported rates; the PDF itself gives a1000mL water input, not an independent final-volume
    instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.49456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.49456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "0.49456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q3", "topic": "(NH4)2SO4 at local direct ingredient index 2", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"(NH4)2SO4\",\n                        \"compound_id\": 27,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.49456,\n                        \"mmol_l\": 3.7427,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "(NH4)2SO4", "compound_id": 27, "amount": 0.5, "unit": "g", "g_l": 0.49456, "mmol_l":
    3.7427, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "evidence_only",
    "rationale": "The exact current main-solution row explicitly reports this g_l
    value. Retain the number with scoped evidence; no mineral/vitamin stock rate is
    transferred into it. The API main-solution volume1011mL is consistent with these
    reported rates; the PDF itself gives a1000mL water input, not an independent final-volume
    instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.49456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.49456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.49456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q4", "topic": "TAPS sodium salt at local direct ingredient index 3", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"TAPS sodium salt\",\n                        \"compound_id\": 1083,\n                        \"attribute\":
    \"SIGMA\",\n                        \"amount\": 2.4,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 2.37389,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "TAPS sodium salt", "compound_id": 1083, "attribute": "SIGMA", "amount": 2.4,
    "unit": "g", "g_l": 2.37389, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "evidence_only", "rationale": "The exact current main-solution row explicitly
    reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin
    stock rate is transferred into it. The API main-solution volume1011mL is consistent
    with these reported rates; the PDF itself gives a1000mL water input, not an independent
    final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "2.37389",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "2.37389",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "2.37389",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q5", "topic": "MgCl2 x 6 H2O at local direct ingredient index 4", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"MgCl2 x 6 H2O\",\n                        \"compound_id\": 79,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.0098912,\n                        \"mmol_l\": 0.0486525,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "MgCl2 x 6 H2O", "compound_id": 79, "amount": 0.01, "unit": "g", "g_l": 0.0098912,
    "mmol_l": 0.0486525, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "evidence_only", "rationale": "The exact current main-solution row explicitly
    reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin
    stock rate is transferred into it. The API main-solution volume1011mL is consistent
    with these reported rates; the PDF itself gives a1000mL water input, not an independent
    final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0098912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0098912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.0098912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q6", "topic": "CaCl2 x 2 H2O at local direct ingredient index 5", "source": {"sources":
    [{"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.0197824,\n                        \"mmol_l\": 0.13456,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.02, "unit": "g", "g_l": 0.0197824,
    "mmol_l": 0.13456, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CaCl2 x 2 H2O\",\n                        \"compound_id\": 7,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.680203,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "CaCl2 x 2 H2O", "compound_id": 7, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l":
    0.680203, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}]}, "decision": "correct",
    "rationale": "The local value combines source-stage rates: 0.0197824 g/L in the
    main recipe plus 0.1 g/L in the mineral stock. These denominators describe different
    solutions. Split the two occurrences and retain the stock receiving dose; adding
    the rates does not give a supported final-medium total. No replacement final total
    is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.11978240000000001",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The local value combines
    source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral
    stock. These denominators describe different solutions. Split the two occurrences
    and retain the stock receiving dose; adding the rates does not give a supported
    final-medium total. No replacement final total is inferred."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.11978240000000001",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The local value combines
    source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral
    stock. These denominators describe different solutions. Split the two occurrences
    and retain the stock receiving dose; adding the rates does not give a supported
    final-medium total. No replacement final total is inferred."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.11978240000000001",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The local value combines
    source-stage rates: 0.0197824 g/L in the main recipe plus 0.1 g/L in the mineral
    stock. These denominators describe different solutions. Split the two occurrences
    and retain the stock receiving dose; adding the rates does not give a supported
    final-medium total. No replacement final total is inferred."}]}, {"quantity_id":
    "q7", "topic": "Yeast extract at local direct ingredient index 6", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.98912,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 7, "compound": "Yeast extract", "compound_id": 16, "amount":
    1, "unit": "g", "g_l": 0.98912, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    "decision": "evidence_only", "rationale": "The exact current main-solution row
    explicitly reports this g_l value. Retain the number with scoped evidence; no
    mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL
    is consistent with these reported rates; the PDF itself gives a1000mL water input,
    not an independent final-volume instruction.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "0.98912", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact current main-solution row explicitly reports this g_l
    value. Retain the number with scoped evidence; no mineral/vitamin stock rate is
    transferred into it. The API main-solution volume1011mL is consistent with these
    reported rates; the PDF itself gives a1000mL water input, not an independent final-volume
    instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.98912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.98912",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q8", "topic": "Sodium resazurin at local direct ingredient index 7", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\":
    0.00196902,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 9, "compound": "Sodium resazurin", "compound_id":
    1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456,
    "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "evidence_only", "rationale": "The exact current main-solution row explicitly
    reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin
    stock rate is transferred into it. The API main-solution volume1011mL is consistent
    with these reported rates; the PDF itself gives a1000mL water input, not an independent
    final-volume instruction. Preserve the percent-defined stock strength and mL dose
    separately; the reported rate alone omits preparation context.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.00049456", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current main-solution
    row explicitly reports this g_l value. Retain the number with scoped evidence;
    no mineral/vitamin stock rate is transferred into it. The API main-solution volume1011mL
    is consistent with these reported rates; the PDF itself gives a1000mL water input,
    not an independent final-volume instruction. Preserve the percent-defined stock
    strength and mL dose separately; the reported rate alone omits preparation context."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00049456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction. Preserve the percent-defined
    stock strength and mL dose separately; the reported rate alone omits preparation
    context."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00049456",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction. Preserve the percent-defined
    stock strength and mL dose separately; the reported rate alone omits preparation
    context."}]}, {"quantity_id": "q9", "topic": "NaHCO3 at local direct ingredient
    index 8", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"NaHCO3\",\n                        \"compound_id\": 55,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.48368,\n                        \"mmol_l\": 17.6614,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "NaHCO3", "compound_id": 55, "amount": 1.5, "unit": "g", "g_l": 1.48368, "mmol_l":
    17.6614, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "evidence_only",
    "rationale": "The exact current main-solution row explicitly reports this g_l
    value. Retain the number with scoped evidence; no mineral/vitamin stock rate is
    transferred into it. The API main-solution volume1011mL is consistent with these
    reported rates; the PDF itself gives a1000mL water input, not an independent final-volume
    instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.48368",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.48368",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1.48368",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q10", "topic": "D-Xylose at local direct ingredient index 9", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"D-Xylose\",\n                        \"compound_id\": 422,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    2.96736,\n                        \"mmol_l\": 19.7653,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "D-Xylose", "compound_id": 422, "amount": 3, "unit": "g", "g_l": 2.96736, "mmol_l":
    19.7653, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "evidence_only",
    "rationale": "The exact current main-solution row explicitly reports this g_l
    value. Retain the number with scoped evidence; no mineral/vitamin stock rate is
    transferred into it. The API main-solution volume1011mL is consistent with these
    reported rates; the PDF itself gives a1000mL water input, not an independent final-volume
    instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "2.96736",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "2.96736",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "2.96736",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q11", "topic": "L-Cysteine HCl x H2O at local direct ingredient index 10", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.24728,\n                        \"mmol_l\": 1.40791,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound":
    "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.25, "unit": "g", "g_l":
    0.24728, "mmol_l": 1.40791, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "evidence_only", "rationale": "The exact current main-solution row explicitly
    reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin
    stock rate is transferred into it. The API main-solution volume1011mL is consistent
    with these reported rates; the PDF itself gives a1000mL water input, not an independent
    final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.24728",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.24728",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.24728",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q12", "topic": "Na2S x 9 H2O at local direct ingredient index 11", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.25,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.24728,\n                        \"mmol_l\": 1.02955,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 0.25, "unit": "g", "g_l": 0.24728,
    "mmol_l": 1.02955, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "evidence_only", "rationale": "The exact current main-solution row explicitly
    reports this g_l value. Retain the number with scoped evidence; no mineral/vitamin
    stock rate is transferred into it. The API main-solution volume1011mL is consistent
    with these reported rates; the PDF itself gives a1000mL water input, not an independent
    final-volume instruction.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.24728",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.24728",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.24728",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact current
    main-solution row explicitly reports this g_l value. Retain the number with scoped
    evidence; no mineral/vitamin stock rate is transferred into it. The API main-solution
    volume1011mL is consistent with these reported rates; the PDF itself gives a1000mL
    water input, not an independent final-volume instruction."}]}, {"quantity_id":
    "q13", "topic": "Nitrilotriacetic acid at local direct ingredient index 12", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Nitrilotriacetic acid\",\n                        \"compound_id\": 189,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.84765,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Nitrilotriacetic acid", "compound_id": 189, "amount": 1.5, "unit": "g", "g_l":
    1.5, "mmol_l": 7.84765, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[12].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[12].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q14", "topic": "MgSO4 x 7 H2O at local direct ingredient index
    13", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    3,\n                        \"unit\": \"g\",\n                        \"g_l\":
    3,\n                        \"mmol_l\": 12.1716,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 3, "unit": "g", "g_l": 3, "mmol_l":
    12.1716, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Modified
    Wolin''s mineral solution. It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "3",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "3",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[13].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q15", "topic": "MnSO4 x H2O at local direct ingredient index
    14", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"MnSO4 x H2O\",\n                        \"compound_id\": 14,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 2.9583,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "MnSO4 x H2O", "compound_id": 14, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    2.9583, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Modified
    Wolin''s mineral solution. It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[14].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q16", "topic": "NaCl at local direct ingredient index 15", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"NaCl\",\n                        \"compound_id\": 43,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 17.1116,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "NaCl", "compound_id": 43, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 17.1116,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Modified Wolin''s
    mineral solution. It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[15].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q17", "topic": "FeSO4 x 7 H2O at local direct ingredient index
    16", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"FeSO4 x 7 H2O\",\n                        \"compound_id\": 12,\n                        \"amount\":
    0.1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.359693,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "FeSO4 x 7 H2O", "compound_id": 12, "amount": 0.1, "unit": "g", "g_l": 0.1, "mmol_l":
    0.359693, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Modified
    Wolin''s mineral solution. It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q18", "topic": "CoSO4 x 7 H2O at local direct ingredient index
    17", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoSO4 x 7 H2O\",\n                        \"compound_id\": 198,\n                        \"amount\":
    0.18,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.18,\n                        \"mmol_l\": 1.16132,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoSO4 x 7 H2O", "compound_id": 198, "amount": 0.18, "unit": "g", "g_l": 0.18,
    "mmol_l": 1.16132, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.18",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[17].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q19", "topic": "ZnSO4 x 7 H2O at local direct ingredient index
    18", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"ZnSO4 x 7 H2O\",\n                        \"compound_id\": 35,\n                        \"amount\":
    0.18,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.18,\n                        \"mmol_l\": 0.625954,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "ZnSO4 x 7 H2O", "compound_id": 35, "amount": 0.18, "unit": "g", "g_l": 0.18,
    "mmol_l": 0.625954, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[18].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.18",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[18].concentration", "stored_value": {"value": "0.18", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q20", "topic": "CuSO4 x 5 H2O at local direct ingredient index
    19", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"CuSO4 x 5 H2O\",\n                        \"compound_id\": 121,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0400503,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "CuSO4 x 5 H2O", "compound_id": 121, "amount": 0.01, "unit": "g", "g_l": 0.01,
    "mmol_l": 0.0400503, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[19].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q21", "topic": "AlK(SO4)2 x 12 H2O at local direct ingredient
    index 20", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"AlK(SO4)2 x 12 H2O\",\n                        \"compound_id\": 908,\n                        \"amount\":
    0.02,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0421596,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "AlK(SO4)2 x 12 H2O", "compound_id": 908, "amount": 0.02, "unit": "g", "g_l":
    0.02, "mmol_l": 0.0421596, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[20].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q22", "topic": "H3BO3 at local direct ingredient index 21", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[10]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.161708,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "H3BO3", "compound_id": 37, "amount": 0.01, "unit": "g", "g_l": 0.01, "mmol_l":
    0.161708, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Modified
    Wolin''s mineral solution. It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[21].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q23", "topic": "Na2MoO4 x 2 H2O at local direct ingredient index
    22", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[11]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    0.01,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.01,\n                        \"mmol_l\": 0.0413309,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 0.01, "unit": "g", "g_l": 0.01,
    "mmol_l": 0.0413309, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[22].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "0.01",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[22].concentration", "stored_value": {"value": "0.01", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q24", "topic": "NiCl2 x 6 H2O at local direct ingredient index
    23", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[12]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    0.03,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.03,\n                        \"mmol_l\": 0.231483,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 0.03, "unit": "g", "g_l": 0.03,
    "mmol_l": 0.231483, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[23].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "0.03",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[23].concentration", "stored_value": {"value": "0.03", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q25", "topic": "Na2SeO3 x 5 H2O at local direct ingredient index
    24", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[13]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"Na2SeO3 x 5 H2O\",\n                        \"compound_id\": 107,\n                        \"amount\":
    0.3,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0003,\n                        \"mmol_l\": 0.00114062,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound":
    "Na2SeO3 x 5 H2O", "compound_id": 107, "amount": 0.3, "unit": "mg", "g_l": 0.0003,
    "mmol_l": 0.00114062, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[24].concentration", "stored_value": {"value": "0.0003", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "0.0003",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[24].concentration", "stored_value": {"value": "0.0003", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q26", "topic": "Na2WO4 x 2 H2O at local direct ingredient index
    25", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[14]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Na2WO4 x 2 H2O\",\n                        \"compound_id\": 249,\n                        \"amount\":
    0.4,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.0004,\n                        \"mmol_l\": 0.00121267,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound":
    "Na2WO4 x 2 H2O", "compound_id": 249, "amount": 0.4, "unit": "mg", "g_l": 0.0004,
    "mmol_l": 0.00121267, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Modified Wolin''s mineral solution. It is a stock-composition rate, not
    a direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[25].concentration", "stored_value": {"value": "0.0004", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "0.0004",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Modified Wolin''s mineral solution. It is a
    stock-composition rate, not a direct receiving-medium rate. Move the source-specific
    component into its stock representation and preserve the separately reported receiving
    dose. The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[25].concentration", "stored_value": {"value": "0.0004", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Modified Wolin''s mineral solution. It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."}]},
    {"quantity_id": "q27", "topic": "Biotin at local direct ingredient index 26",
    "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Biotin\",\n                        \"compound_id\": 46,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0818632,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "Biotin", "compound_id": 46, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0818632, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Wolin''s
    vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[26].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id":
    "q28", "topic": "Folic acid at local direct ingredient index 27", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Folic acid\",\n                        \"compound_id\": 138,\n                        \"amount\":
    20,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.02,\n                        \"mmol_l\": 0.0453104,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Folic acid", "compound_id": 138, "amount": 20, "unit": "mg", "g_l": 0.02, "mmol_l":
    0.0453104, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Wolin''s
    vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "0.02",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[27].concentration", "stored_value": {"value": "0.02", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id":
    "q29", "topic": "Pyridoxine hydrochloride at local direct ingredient index 28",
    "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"Pyridoxine hydrochloride\",\n                        \"compound_id\": 519,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.486287,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "Pyridoxine hydrochloride", "compound_id": 519, "amount": 100, "unit": "mg", "g_l":
    0.1, "mmol_l": 0.486287, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate, not a
    direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path":
    "ingredients[28].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[28].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Wolin''s vitamin
    solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume."}]}, {"quantity_id": "q30", "topic": "Thiamine
    HCl at local direct ingredient index 29", "source": {"evidence_id": "api1206",
    "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"Thiamine HCl\",\n                        \"compound_id\": 1207,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.148236,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "Thiamine HCl", "compound_id": 1207, "amount": 50, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.148236, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate, not a
    direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path":
    "ingredients[29].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[29].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Wolin''s vitamin
    solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume."}]}, {"quantity_id": "q31", "topic": "Riboflavin
    at local direct ingredient index 30", "source": {"evidence_id": "api1206", "reference":
    "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Riboflavin\",\n                        \"compound_id\": 136,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.132837,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Riboflavin", "compound_id": 136, "amount": 50, "unit": "mg", "g_l": 0.05, "mmol_l":
    0.132837, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Wolin''s
    vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[30].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id":
    "q32", "topic": "Nicotinic acid at local direct ingredient index 31", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Nicotinic acid\",\n                        \"compound_id\": 139,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.406141,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "Nicotinic acid", "compound_id": 139, "amount": 50, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.406141, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate, not a
    direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path":
    "ingredients[31].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[31].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Wolin''s vitamin
    solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume."}]}, {"quantity_id": "q33", "topic": "Calcium
    D-(+)-pantothenate at local direct ingredient index 32", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"Calcium D-(+)-pantothenate\",\n                        \"compound_id\": 1512,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.209846,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "Calcium D-(+)-pantothenate", "compound_id": 1512, "amount": 50, "unit": "mg",
    "g_l": 0.05, "mmol_l": 0.209846, "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path":
    "ingredients[32].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[32].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Wolin''s vitamin
    solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume."}]}, {"quantity_id": "q34", "topic": "Vitamin
    B12 at local direct ingredient index 33", "source": {"evidence_id": "api1206",
    "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"Vitamin B12\",\n                        \"compound_id\": 18,\n                        \"amount\":
    1,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.001,\n                        \"mmol_l\": 0.00073779,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "Vitamin B12", "compound_id": 18, "amount": 1, "unit": "mg", "g_l": 0.001, "mmol_l":
    0.00073779, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "correct",
    "rationale": "The numerical value agrees exactly with the provider g_l for Wolin''s
    vitamin solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ingredients[33].concentration", "stored_value": {"value": "0.001",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The numerical value agrees
    exactly with the provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition
    rate, not a direct receiving-medium rate. Move the source-specific component into
    its stock representation and preserve the separately reported receiving dose.
    The PDF batch mass is not independently converted using water-input volume."},
    {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path":
    "ingredients[33].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}]}, {"quantity_id":
    "q35", "topic": "p-Aminobenzoic acid at local direct ingredient index 34", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"p-Aminobenzoic acid\",\n                        \"compound_id\": 47,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.364591,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "p-Aminobenzoic acid", "compound_id": 47, "amount": 50, "unit": "mg", "g_l": 0.05,
    "mmol_l": 0.364591, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate, not a
    direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path":
    "ingredients[34].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[34].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Wolin''s vitamin
    solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume."}]}, {"quantity_id": "q36", "topic": "(DL)-alpha-Lipoic
    acid at local direct ingredient index 35", "source": {"evidence_id": "api1206",
    "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[9]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"(DL)-alpha-Lipoic acid\",\n                        \"compound_id\": 252,\n                        \"amount\":
    50,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.05,\n                        \"mmol_l\": 0.24233,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "(DL)-alpha-Lipoic acid", "compound_id": 252, "amount": 50, "unit": "mg", "g_l":
    0.05, "mmol_l": 0.24233, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "correct", "rationale": "The numerical value agrees exactly with the provider
    g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate, not a
    direct receiving-medium rate. Move the source-specific component into its stock
    representation and preserve the separately reported receiving dose. The PDF batch
    mass is not independently converted using water-input volume.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml", "field_path":
    "ingredients[35].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The numerical value agrees exactly with the
    provider g_l for Wolin''s vitamin solution (10x). It is a stock-composition rate,
    not a direct receiving-medium rate. Move the source-specific component into its
    stock representation and preserve the separately reported receiving dose. The
    PDF batch mass is not independently converted using water-input volume."}, {"path":
    "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml", "field_path": "ingredients[35].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The numerical value agrees exactly with the provider g_l for Wolin''s vitamin
    solution (10x). It is a stock-composition rate, not a direct receiving-medium
    rate. Move the source-specific component into its stock representation and preserve
    the separately reported receiving dose. The PDF batch mass is not independently
    converted using water-input volume."}]}, {"quantity_id": "q37", "topic": "Main
    sol. 1206 / Modified Wolin''s mineral solution", "source": {"evidence_id": "api1206",
    "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\":
    \"Modified Wolin''s mineral solution\",\n                        \"solution_id\":
    241,\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "solution": "Modified Wolin''s mineral solution", "solution_id":
    241, "amount": 10, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    "decision": "add", "rationale": "The source supplies 10mL of Modified Wolin''s
    mineral solution at the receiving-medium batch stage. Create the missing solution
    descriptor and retain this literal dose and source-stage basis in root evidence.
    Do not label the unchanged mL amount as mL/L without the final-medium denominator;
    do not double-count the stock and its expanded components.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "The source
    supplies 10mL of Modified Wolin''s mineral solution at the receiving-medium batch
    stage. Create the missing solution descriptor and retain this literal dose and
    source-stage basis in root evidence. Do not label the unchanged mL amount as mL/L
    without the final-medium denominator; do not double-count the stock and its expanded
    components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 10mL of Modified Wolin''s mineral solution at the receiving-medium
    batch stage. Create the missing solution descriptor and retain this literal dose
    and source-stage basis in root evidence. Do not label the unchanged mL amount
    as mL/L without the final-medium denominator; do not double-count the stock and
    its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 10mL of Modified Wolin''s mineral solution at the receiving-medium
    batch stage. Create the missing solution descriptor and retain this literal dose
    and source-stage basis in root evidence. Do not label the unchanged mL amount
    as mL/L without the final-medium denominator; do not double-count the stock and
    its expanded components.", "missing": true}]}, {"quantity_id": "q38", "topic":
    "Main sol. 1206 / Sodium resazurin", "source": {"evidence_id": "api1206", "reference":
    "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.00049456,\n                        \"mmol_l\":
    0.00196902,\n                        \"optional\": 0\n                    }",
    "exact_decoded_object": {"recipe_order": 9, "compound": "Sodium resazurin", "compound_id":
    1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.00049456,
    "mmol_l": 0.00196902, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, "decision":
    "add", "rationale": "The source supplies 0.5mL of Sodium resazurin at the receiving-medium
    batch stage with attribute 0.1% w/v. Create the missing solution descriptor and
    retain this literal dose and source-stage basis in root evidence. Do not label
    the unchanged mL amount as mL/L without the final-medium denominator; do not double-count
    the stock and its expanded components.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage
    with attribute 0.1% w/v. Create the missing solution descriptor and retain this
    literal dose and source-stage basis in root evidence. Do not label the unchanged
    mL amount as mL/L without the final-medium denominator; do not double-count the
    stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage
    with attribute 0.1% w/v. Create the missing solution descriptor and retain this
    literal dose and source-stage basis in root evidence. Do not label the unchanged
    mL amount as mL/L without the final-medium denominator; do not double-count the
    stock and its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 0.5mL of Sodium resazurin at the receiving-medium batch stage
    with attribute 0.1% w/v. Create the missing solution descriptor and retain this
    literal dose and source-stage basis in root evidence. Do not label the unchanged
    mL amount as mL/L without the final-medium denominator; do not double-count the
    stock and its expanded components.", "missing": true}]}, {"quantity_id": "q39",
    "topic": "Main sol. 1206 / Wolin''s vitamin solution (10x)", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"solution\":
    \"Wolin''s vitamin solution (10x)\",\n                        \"solution_id\":
    5980,\n                        \"amount\": 1,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 12, "solution": "Wolin''s vitamin solution (10x)", "solution_id":
    5980, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    "decision": "add", "rationale": "The source supplies 1mL of Wolin''s vitamin solution
    (10x) at the receiving-medium batch stage. Create the missing solution descriptor
    and retain this literal dose and source-stage basis in root evidence. Do not label
    the unchanged mL amount as mL/L without the final-medium denominator; do not double-count
    the stock and its expanded components.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 1mL of Wolin''s vitamin solution (10x) at the receiving-medium
    batch stage. Create the missing solution descriptor and retain this literal dose
    and source-stage basis in root evidence. Do not label the unchanged mL amount
    as mL/L without the final-medium denominator; do not double-count the stock and
    its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 1mL of Wolin''s vitamin solution (10x) at the receiving-medium
    batch stage. Create the missing solution descriptor and retain this literal dose
    and source-stage basis in root evidence. Do not label the unchanged mL amount
    as mL/L without the final-medium denominator; do not double-count the stock and
    its expanded components.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The source supplies 1mL of Wolin''s vitamin solution (10x) at the receiving-medium
    batch stage. Create the missing solution descriptor and retain this literal dose
    and source-stage basis in root evidence. Do not label the unchanged mL amount
    as mL/L without the final-medium denominator; do not double-count the stock and
    its expanded components.", "missing": true}]}, {"quantity_id": "q40", "topic":
    "Main sol. 1206 / Distilled water", "source": {"evidence_id": "api1206", "reference":
    "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "add", "rationale": "Retain this exact
    1000mL water input for Main sol. 1206 in stage-specific preparation or root evidence.
    It is not a direct solute ingredient or automatically a final-volume makeup. No
    independent final-volume conversion is made from this row.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain
    this exact 1000mL water input for Main sol. 1206 in stage-specific preparation
    or root evidence. It is not a direct solute ingredient or automatically a final-volume
    makeup. No independent final-volume conversion is made from this row.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Retain this exact 1000mL water input for Main sol. 1206 in stage-specific preparation
    or root evidence. It is not a direct solute ingredient or automatically a final-volume
    makeup. No independent final-volume conversion is made from this row.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "AUTOCLAVE", "description": "Dissolve ingredients (except bicarbonate, xylose,
    vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100%
    N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins,
    cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2
    gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by
    filtration. Adjust pH of the complete medium to 8.5, if necessary."}, {"step_number":
    2, "action": "ADJUST_PH", "description": "First dissolve nitrilotriacetic acid
    and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with
    KOH."}], "decision": "add", "rationale": "Retain this exact 1000mL water input
    for Main sol. 1206 in stage-specific preparation or root evidence. It is not a
    direct solute ingredient or automatically a final-volume makeup. No independent
    final-volume conversion is made from this row."}]}, {"quantity_id": "q41", "topic":
    "Modified Wolin''s mineral solution / Distilled water", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].recipe[15]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "add", "rationale": "Retain this exact
    1000mL water input for Modified Wolin''s mineral solution in stage-specific preparation
    or root evidence. It is not a direct solute ingredient or automatically a final-volume
    makeup. No independent final-volume conversion is made from this row.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain
    this exact 1000mL water input for Modified Wolin''s mineral solution in stage-specific
    preparation or root evidence. It is not a direct solute ingredient or automatically
    a final-volume makeup. No independent final-volume conversion is made from this
    row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Retain this exact 1000mL water input for Modified Wolin''s mineral solution in
    stage-specific preparation or root evidence. It is not a direct solute ingredient
    or automatically a final-volume makeup. No independent final-volume conversion
    is made from this row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "AUTOCLAVE", "description": "Dissolve ingredients (except bicarbonate, xylose,
    vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100%
    N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins,
    cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2
    gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by
    filtration. Adjust pH of the complete medium to 8.5, if necessary."}, {"step_number":
    2, "action": "ADJUST_PH", "description": "First dissolve nitrilotriacetic acid
    and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with
    KOH."}], "decision": "add", "rationale": "Retain this exact 1000mL water input
    for Modified Wolin''s mineral solution in stage-specific preparation or root evidence.
    It is not a direct solute ingredient or automatically a final-volume makeup. No
    independent final-volume conversion is made from this row."}]}, {"quantity_id":
    "q42", "topic": "Wolin''s vitamin solution (10x) / Distilled water", "source":
    {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[2].recipe[10]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "add", "rationale": "Retain this exact
    1000mL water input for Wolin''s vitamin solution (10x) in stage-specific preparation
    or root evidence. It is not a direct solute ingredient or automatically a final-volume
    makeup. No independent final-volume conversion is made from this row.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Retain
    this exact 1000mL water input for Wolin''s vitamin solution (10x) in stage-specific
    preparation or root evidence. It is not a direct solute ingredient or automatically
    a final-volume makeup. No independent final-volume conversion is made from this
    row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Retain this exact 1000mL water input for Wolin''s vitamin solution (10x) in stage-specific
    preparation or root evidence. It is not a direct solute ingredient or automatically
    a final-volume makeup. No independent final-volume conversion is made from this
    row.", "missing": true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "preparation_steps", "stored_value": [{"step_number": 1, "action":
    "AUTOCLAVE", "description": "Dissolve ingredients (except bicarbonate, xylose,
    vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge medium with 100%
    N2 gas for 30 - 45 min to make it anoxic. Dispense medium under same gas atmosphere
    into anoxic Hungate-type tubes or serum vials and autoclave. Add xylose, vitamins,
    cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2
    gas and bicarbonate from a sterile anoxic stock solution prepared under 80% N2
    and 20% CO2 gas atmosphere. Sterilize stock solutions of xylose and vitamins by
    filtration. Adjust pH of the complete medium to 8.5, if necessary."}, {"step_number":
    2, "action": "ADJUST_PH", "description": "First dissolve nitrilotriacetic acid
    and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0 with
    KOH."}], "decision": "add", "rationale": "Retain this exact 1000mL water input
    for Wolin''s vitamin solution (10x) in stage-specific preparation or root evidence.
    It is not a direct solute ingredient or automatically a final-volume makeup. No
    independent final-volume conversion is made from this row."}]}, {"quantity_id":
    "q43", "topic": "Main sol. 1206 preparation context", "source": {"evidence_id":
    "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path":
    "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients (except
    bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge
    medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of
    xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if
    necessary.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust
    pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock
    solutions of xylose and vitamins by filtration. Adjust pH of the complete medium
    to 8.5, if necessary."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "Read and retain the entire Main sol. 1206 step, including all pH,
    gas fractions, duration, liquid/normality/filter-pore values where present. Existing
    matching descriptions are credited; missing descriptions need source-scoped addition.
    An action enum does not fully encode the multi-operation paragraph.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "This
    source step is missing from this record; add only the supported stage-specific
    instruction with root evidence, preserving existing other-stage prose.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "This source step is missing from this record; add only the supported stage-specific
    instruction with root evidence, preserving existing other-stage prose.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients
    (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5,
    then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense
    medium under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock
    solutions of xylose and vitamins by filtration. Adjust pH of the complete medium
    to 8.5, if necessary.", "decision": "evidence_only", "rationale": "The complete
    numeric and procedural text matches this source solution step. Retain its contents,
    but explicitly scope it to Main sol. 1206 rather than treating all stock steps
    as a sequence on the final medium."}]}, {"quantity_id": "q44", "topic": "Modified
    Wolin''s mineral solution preparation context", "source": {"evidence_id": "api1206",
    "reference": "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"step\": \"First dissolve nitrilotriacetic
    acid and adjust pH to 6.5 with KOH, then add minerals. Adjust final to pH 7.0
    with KOH.\"\n                    }", "exact_decoded_object": {"step": "First dissolve
    nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust
    final to pH 7.0 with KOH."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "mixed",
    "rationale": "Read and retain the entire Modified Wolin''s mineral solution step,
    including all pH, gas fractions, duration, liquid/normality/filter-pore values
    where present. Existing matching descriptions are credited; missing descriptions
    need source-scoped addition. An action enum does not fully encode the multi-operation
    paragraph.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "This source step is missing from this record; add only the supported stage-specific
    instruction with root evidence, preserving existing other-stage prose.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "This source step is missing from this record; add only the supported stage-specific
    instruction with root evidence, preserving existing other-stage prose.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "First dissolve
    nitrilotriacetic acid and adjust pH to 6.5 with KOH, then add minerals. Adjust
    final to pH 7.0 with KOH.", "decision": "evidence_only", "rationale": "The complete
    numeric and procedural text matches this source solution step. Retain its contents,
    but explicitly scope it to Modified Wolin''s mineral solution rather than treating
    all stock steps as a sequence on the final medium."}]}, {"quantity_id": "q45",
    "topic": "Main-medium pH", "source": {"evidence_id": "api1206", "reference": "https://mediadive.dsmz.de/rest/medium/1206",
    "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin", "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.medium", "accessed_at": "2026-10-28T05:42:27.180766Z", "quote":
    "{\n            \"id\": 1206,\n            \"name\": \"CALDANAEROVIRGA MEDIUM\",\n            \"complex_medium\":
    \"yes\",\n            \"min_pH\": 8.5,\n            \"max_pH\": 8.5,\n            \"source\":
    \"DSMZ\",\n            \"link\": \"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1206.pdf\"\n        }",
    "exact_decoded_object": {"id": 1206, "name": "CALDANAEROVIRGA MEDIUM", "complex_medium":
    "yes", "min_pH": 8.5, "max_pH": 8.5, "source": "DSMZ", "link": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1206.pdf"},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, "decision": "evidence_only", "rationale": "The stored
    ph_value matches the exact main-medium pH reported by the PDF and API. This is
    distinct from the mineral-stock pH adjustment; source titration amounts are not
    quantified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CALDANAEROVIRGA_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 8.5, "decision": "evidence_only", "rationale":
    "The stored ph_value matches the exact main-medium pH reported by the PDF and
    API. This is distinct from the mineral-stock pH adjustment; source titration amounts
    are not quantified."}, {"path": "data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml",
    "field_path": "ph_value", "stored_value": 8.5, "decision": "evidence_only", "rationale":
    "The stored ph_value matches the exact main-medium pH reported by the PDF and
    API. This is distinct from the mineral-stock pH adjustment; source titration amounts
    are not quantified."}, {"path": "data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml",
    "field_path": "ph_value", "stored_value": 8.5, "decision": "evidence_only", "rationale":
    "The stored ph_value matches the exact main-medium pH reported by the PDF and
    API. This is distinct from the mineral-stock pH adjustment; source titration amounts
    are not quantified."}]}, {"quantity_id": "q46", "topic": "Unquantified late-stock
    and sterilization details", "source": {"evidence_id": "api1206", "reference":
    "https://mediadive.dsmz.de/rest/medium/1206", "raw_path": "REVIEW_WORK/batch057/source01-03/api1206.bin",
    "raw_sha256": "e1ce92031352518c93f82453e6283cb7d5a12fb91cc908baa8299bc5aa33776a",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T05:42:27.180766Z",
    "quote": "{\n                        \"step\": \"Dissolve ingredients (except
    bicarbonate, xylose, vitamins, cysteine and sulfide), adjust pH to 8.5, then sparge
    medium with 100% N2 gas for 30 - 45 min to make it anoxic. Dispense medium under
    same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave.
    Add xylose, vitamins, cysteine and sulfide from sterile anoxic stock solutions
    prepared under 100% N2 gas and bicarbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock solutions of
    xylose and vitamins by filtration. Adjust pH of the complete medium to 8.5, if
    necessary.\"\n                    }", "exact_decoded_object": {"step": "Dissolve
    ingredients (except bicarbonate, xylose, vitamins, cysteine and sulfide), adjust
    pH to 8.5, then sparge medium with 100% N2 gas for 30 - 45 min to make it anoxic.
    Dispense medium under same gas atmosphere into anoxic Hungate-type tubes or serum
    vials and autoclave. Add xylose, vitamins, cysteine and sulfide from sterile anoxic
    stock solutions prepared under 100% N2 gas and bicarbonate from a sterile anoxic
    stock solution prepared under 80% N2 and 20% CO2 gas atmosphere. Sterilize stock
    solutions of xylose and vitamins by filtration. Adjust pH of the complete medium
    to 8.5, if necessary."}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}, "decision": "not_quantified",
    "rationale": "The source specifies sterile late stock additions and stage-specific
    gases/filtration but does not supply fixed concentrations and addition volumes
    for every late solute stock, titrant amounts, or a numeric autoclave temperature/duration.
    Preserve these limits; do not infer common settings or concentrations.", "layer_assessments":
    []}]'
- assessment_id: a7
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - grounding
- assessment_id: a8
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - history
  - scalars
- assessment_id: a9
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - local-target
- assessment_id: a10
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:003954
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-003954-mineral-and-vitamin-stocks-are-flattened-into-direct-ingredients
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Mineral and vitamin stocks are flattened into direct ingredients
  description: The exact source defines Modified Wolin's mineral solution and Wolin's
    vitamin solution (10x) as separate stock formulations with separate receiving
    mL doses. The selected target and maintained contributors place the stock components
    directly under ingredients at their stock g/L values and have no solutions descriptors.
    This is a stage error even where the stock numbers themselves match the provider.
    Preserve the source stock recipes and receiving doses; do not dilute or sum them
    by an assumed final liter.
  target_ids:
  - CultureMech:003954
  field_paths:
  - solutions
  - ingredients[12].concentration
  - ingredients[13].concentration
  - ingredients[14].concentration
  - ingredients[15].concentration
  - ingredients[16].concentration
  - ingredients[17].concentration
  - ingredients[18].concentration
  - ingredients[19].concentration
  - ingredients[20].concentration
  - ingredients[21].concentration
  - ingredients[22].concentration
  - ingredients[23].concentration
  - ingredients[24].concentration
  - ingredients[25].concentration
  - ingredients[26].concentration
  - ingredients[27].concentration
  - ingredients[28].concentration
  - ingredients[29].concentration
  - ingredients[30].concentration
  - ingredients[31].concentration
  - ingredients[32].concentration
  - ingredients[33].concentration
  - ingredients[34].concentration
  - ingredients[35].concentration
  evidence_ids:
  - dsm1206
  - api1206
  - source-rows
  - quantities
  - writer-mediadive
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-003954-repeated-chemical-occurrences-were-summed-across-main-and-stock-stages
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Repeated chemical occurrences were summed across main and stock stages
  description: CaCl2 x 2 H2O is stored as 0.11978240000000001 g/L, with a note recording
    a two-value sum. The current source instead distinguishes a main-medium occurrence
    and a mineral-stock occurrence. Adding concentrations from different source solutions
    is invalid as a final-medium total because the concentrations refer to different
    solution-stage bases; retain two scoped occurrences and resolve the receiving
    denominator before any final total. The current cleanup implementation does not
    perform this historical sum.
  target_ids:
  - CultureMech:003954
  field_paths:
  - ingredients[5].concentration
  - ingredients[5].notes
  evidence_ids:
  - dsm1206
  - api1206
  - quantities
  - writer-cleanup
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-003954-nickel-hydrate-and-sodium-indicator-forms-are-not-represented-by-their-identifiers
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Nickel hydrate and sodium indicator forms are not represented by their identifiers
  description: NiCl2 x6H2O is assigned CHEBI:34887, whose current OLS object describes
    NiCl2 without the six waters. Sodium resazurin uses primary CHEBI:8806 Resazurin,
    which does not establish the sodium-salt form. The secondary nickel link repeats
    the mismatch; the resazurin node has no secondary slot to accuse. Current catalog
    membership and canonical label agreement do not cure supplied-form mismatch. Verify
    an exact supplied-form mapping or retain the precise source name with an explicit
    unresolved mapping; no replacement identifier is guessed.
  target_ids:
  - CultureMech:003954
  field_paths:
  - ingredients[23].term
  - ingredients[23].mediaingredientmech_chebi_term
  - ingredients[7].term
  evidence_ids:
  - dsm1206
  - chebi34887
  - chebi8806
  - grounding
  rule_id: id-label-supplied-form
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-003954-the-generated-record-omits-supported-preparation-and-loses-stage-boundaries
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: The generated record omits supported preparation and loses stage boundaries
  description: The DSMZ owner retains both source preparation paragraphs, including
    main pH8.5,30–45min gas treatment, late stocks and mineral-stock pH6.5 then7.0.
    The selected generated record and KOMODO owner have no preparation_steps. Credit
    the retained DSMZ text while restoring missing supported instructions and stage
    attribution. Reconcile the two contributors before regeneration; current exact-formulation
    merging rejects incompatible preparation assertions.
  target_ids:
  - CultureMech:003954
  field_paths:
  - preparation_steps
  - data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml::preparation_steps[0]
  - data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml::preparation_steps[1]
  - data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml::preparation_steps
  evidence_ids:
  - dsm1206
  - api1206
  - owner-2
  - writer-merge
  - writer-formulation
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-003954-the-komodo-import-timestamp-is-malformed-and-its-original-table-remains-unauthenticated
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The KOMODO import timestamp is malformed and its original table remains unauthenticated
  description: The target and KOMODO owner store curation_history[0].timestamp as2026-01-27T01:15:01.fZ,
    which is not a valid fractional-second timestamp. The original KOMODO table is
    not authenticated by the current403 endpoint or the derivative catalog excerpt.
    The current DSMZ response does authenticate the separately cited API bytes. Retain
    the malformed original event unchanged. If authoritative provenance is recovered,
    append a new verified correction or context event that explains it; never rewrite
    the original timestamp or invent a date.
  target_ids:
  - CultureMech:003954
  field_paths:
  - curation_history[0].timestamp
  - data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml::curation_history[0].timestamp
  - notes
  evidence_ids:
  - local-target
  - owner-1
  - komodo1206
  - historical-reader
  rule_id: historical-timestamp-and-source-scope
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate the maintained contributors to represent each mineral/vitamin
    stock and its receiving dose separately. Preserve source-specific stock g/L claims
    and PDF batch amounts with exact evidence. Remove their false direct-medium placement,
    then regenerate; do not double-count stock expansions or invent a working concentration.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:003954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: CaCl2 x 2 H2O is stored as 0.11978240000000001 g/L, with a note recording
    a two-value sum. The current source instead distinguishes a main-medium occurrence
    and a mineral-stock occurrence. Adding concentrations from different source solutions
    is invalid as a final-medium total because the concentrations refer to different
    solution-stage bases; retain two scoped occurrences and resolve the receiving
    denominator before any final total. The current cleanup implementation does not
    perform this historical sum.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:003954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: NiCl2 x6H2O is assigned CHEBI:34887, whose current OLS object describes
    NiCl2 without the six waters. Sodium resazurin uses primary CHEBI:8806 Resazurin,
    which does not establish the sodium-salt form. The secondary nickel link repeats
    the mismatch; the resazurin node has no secondary slot to accuse. Current catalog
    membership and canonical label agreement do not cure supplied-form mismatch. Verify
    an exact supplied-form mapping or retain the precise source name with an explicit
    unresolved mapping; no replacement identifier is guessed.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:003954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Retain the DSMZ owner preparation text, label the mineral-stock procedure
    explicitly, and preserve it in the generated result after source-duplicate reconciliation.
    Add exact root evidence for process and pH claims; leave unquantified late stock
    strengths and sterilization settings unspecified.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:003954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: The target and KOMODO owner store curation_history[0].timestamp as2026-01-27T01:15:01.fZ,
    which is not a valid fractional-second timestamp. The original KOMODO table is
    not authenticated by the current403 endpoint or the derivative catalog excerpt.
    The current DSMZ response does authenticate the separately cited API bytes. Retain
    the malformed original event unchanged. If authoritative provenance is recovered,
    append a new verified correction or context event that explains it; never rewrite
    the original timestamp or invent a date.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:003954
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- No organism-specific growth or missing sterilization settings are inferred. The
  review addresses the exact source formulation and maintained contributors; neighboring
  or parent medium recipes are not transferred wholesale.
- Current OLS and the pinned packaged MIM catalog describe current identifier correspondence,
  not historical mapping validity. No molecular-weight, density or mmol/L conversion
  was used.
- Historical report raw-digest matches authenticate the current matching API response
  bytes and exact snippets, not the recorded old access events, old executables, or
  all historical scientific conclusions.
- No fixed late-stock concentration or addition volume is invented where the source
  provides only a sterile-addition instruction. Exact source batches and explicitly
  reported source-stage g/L values remain distinct.
- The current bounded KOMODO request returned403. The old catalog excerpt is derivative
  identity context; its complete original catalog response was not recovered in this
  review. The local cross-reference and current DSMZ primary/provider sources remain
  directly assessed.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
