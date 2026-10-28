# Review Clostridium cellulovorans medium and its merged contributors

- Review: 20261028T103139Z-batch063-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T10:18:10.364830Z
- Finished UTC: 2026-10-28T10:31:39.774456Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

DSM320 supports the base-medium identity and separate stock recipes. The generated record and maintained contributors flatten stock inputs, combine yeast-extract stages and lose the explicit rumen/sludge alternative. Existing DSM preparation is credited; exact KOMODO source access remains unresolved.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch063 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005010 | data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml | generated | clostridium_cellulovorans_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005010 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:005010 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:005010 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:005010 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Base identity and named replacement scope

identity: concern. Targets: CultureMech:005010.

The generated file resolves to exact three normalized contributors. DSM320 is verified independently; the replacement label is an explicit variant lead and its old exact catalogue row is derivative evidence only. Current403 responses prevent independently revalidating the historical KOMODO accessions. Identical copied ingredient lists do not establish preparation or variant equivalence.

### Source alternatives and current writer behavior

consistency: concern. Targets: CultureMech:005010.

The base primary distinguishes clarified rumen fluid from optional alternative sludge fluid. The named replacement contributor has the same copied ingredients but lacks a representation of that substitution. Present conservative merge code rejects unequal formulation content; source-aware normalization must preserve alternatives before regeneration. The current MediaDive solution parser also omits source optional/condition fields.

### Preparation, phenotype and claim attachment

completeness: concern. Targets: CultureMech:005010.

Existing DSM owner preparation is retained and credited, while the selected target and KOMODO contributors omit it. No attached evidence or target_organisms exist in the four complete files. Generic cultivation applications and source names do not establish strain-specific growth; iModulonDB is not applicable to this medium-only record. Complex/undefined classification agrees with biological extracts; liquid status is conditional on the selected formulation, with particulate cellulose separately qualified.

### Ingredient linkage metrics

grounding: supported. Targets: CultureMech:005010.

Each of four layers has22ingredient instances:19primary CHEBI IDs (19/22=86.36%) and18mediaingredientmech_chebi_term links (18/22=81.82%); no numeric legacy MIM IDs. These are presence metrics, not scientific accuracy. Peptone, yeast extract and sludge lack primary IDs; current catalog candidates alone do not justify a new exact grounding.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:005010.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Main batch input: K2HPO4 x 3 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "K2HPO4 x 3 H2O", "compound_id": 244, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 5.74132, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q2", "topic": "Main batch input: NH4Cl", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "NH4Cl", "compound_id": 42, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 18.6951, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q3", "topic": "Main batch input: KCl", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 6.70691,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "KCl", "compound_id": 61, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 6.70691, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q4", "topic": "Main batch input: MgSO4 x 7 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 2.02859, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q5", "topic": "Main batch input: Trypticase peptone", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\": \"BD BBL\",\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "Trypticase peptone", "compound_id": 124, "attribute": "BD BBL", "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q6", "topic": "Main batch input: L-Cysteine HCl x H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\": \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 0.854039,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound": "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.15, "unit": "g", "g_l": 0.15, "mmol_l": 0.854039, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q7", "topic": "Main batch input: Na2CO3", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\": \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\": 1,\n                        \"unit\": \"g\",\n                        \"g_l\": 1,\n                        \"mmol_l\": 9.43503,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound": "Na2CO3", "compound_id": 32, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 9.43503, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q8", "topic": "Main batch input: Cellobiose", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\": \"Cellobiose\",\n                        \"compound_id\": 214,\n                        \"amount\": 5,\n                        \"unit\": \"g\",\n                        \"g_l\": 5,\n                        \"mmol_l\": 14.6071,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound": "Cellobiose", "compound_id": 214, "amount": 5, "unit": "g", "g_l": 5, "mmol_l": 14.6071, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q9", "topic": "Main batch input: Na2S x 9 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\": \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\": 0.15,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.15,\n                        \"mmol_l\": 0.624526,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound": "Na2S x 9 H2O", "compound_id": 54, "amount": 0.15, "unit": "g", "g_l": 0.15, "mmol_l": 0.624526, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "unsupported", "rationale": "Batch mass, provider-declared rate and independently established final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The primary gram input and provider g_l numeral agree with the stored digits. Final medium volume is not explicitly stated, so the G_PER_L basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q10", "topic": "Main yeast extract versus sludge-preparation yeast extract", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 0.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "Yeast extract", "compound_id": 16, "amount": 0.5, "unit": "g", "g_l": 0.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\": 4,\n                        \"unit\": \"g\",\n                        \"g_l\": 4,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "Yeast extract", "compound_id": 16, "amount": 4, "unit": "g", "g_l": 4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Keep the two source stages separate; finished sludge composition after processing is not inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The local4.5 sums the0.5g main input and4g separate sludge-preparation input. That sum is neither the main batch addition nor an established final-medium rate."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The local4.5 sums the0.5g main input and4g separate sludge-preparation input. That sum is neither the main batch addition nor an established final-medium rate."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5", "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The local4.5 sums the0.5g main input and4g separate sludge-preparation input. That sum is neither the main batch addition nor an established final-medium rate."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The local4.5 sums the0.5g main input and4g separate sludge-preparation input. That sum is neither the main batch addition nor an established final-medium rate."}]}, {"quantity_id": "q11", "topic": "Required clarified rumen fluid", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\": \"Clarified rumen fluid\",\n                        \"solution_id\": 2618,\n                        \"condition\": \"\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "solution": "Clarified rumen fluid", "solution_id": 2618, "condition": "", "amount": 20, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Restore source additions with explicit choice semantics; shared missing collection is not a claim that each row has the same identity.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Variant-specific source access remains unresolved. The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}]}, {"quantity_id": "q12", "topic": "Optional alternative sludge fluid", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\": \"Sludge fluid\",\n                        \"solution_id\": 208,\n                        \"condition\": \"alternative\",\n                        \"amount\": 20,\n                        \"unit\": \"ml\",\n                        \"optional\": 1\n                    }", "exact_decoded_object": {"recipe_order": 8, "solution": "Sludge fluid", "solution_id": 208, "condition": "alternative", "amount": 20, "unit": "ml", "optional": 1}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Restore source additions with explicit choice semantics; shared missing collection is not a claim that each row has the same identity.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Variant-specific source access remains unresolved. The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing": true}]}, {"quantity_id": "q13", "topic": "Trace solution SL10 addition", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\": \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\": 1,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "solution": "Trace element solution SL-10", "solution_id": 595, "amount": 1, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Restore source additions with explicit choice semantics; shared missing collection is not a claim that each row has the same identity.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 1ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 1ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe explicitly adds 1ml; preserve name, stage and the exact optional/alternative status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Variant-specific source access remains unresolved. The main recipe explicitly adds 1ml; preserve name, stage and the exact optional/alternative status.", "missing": true}]}, {"quantity_id": "q14", "topic": "Sodium-resazurin stock strength and aliquot", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\": \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\": \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5, "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "0.1g/100ml ×0.5ml =0.0005g input. No final-volume denominator is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies0.5ml of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l numeral. It omits the stock and addition stage and does not independently establish final G_PER_L."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies0.5ml of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l numeral. It omits the stock and addition stage and does not independently establish final G_PER_L."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies0.5ml of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l numeral. It omits the stock and addition stage and does not independently establish final G_PER_L."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The source supplies0.5ml of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l numeral. It omits the stock and addition stage and does not independently establish final G_PER_L."}]}, {"quantity_id": "q15", "topic": "Conditional cellulose substrate", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\": \"Cellulose\",\n                        \"compound_id\": 400,\n                        \"condition\": \"MN 301\",\n                        \"amount\": 10,\n                        \"unit\": \"g\",\n                        \"optional\": 1\n                    }", "exact_decoded_object": {"recipe_order": 14, "compound": "Cellulose", "compound_id": 400, "condition": "MN 301", "amount": 10, "unit": "g", "optional": 1}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "10.0 g/l cellulose"}], "decision": "mixed", "rationale": "Retain the exact conditional substrate scope; this is the one explicit primary main-medium g/l statement.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The optional MN301 row and explicit primary10.0g/l adaptation note support the stored rate and optional note. The source does not establish every strain or authorize automatic co-use/replacement of cellobiose."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The optional MN301 row and explicit primary10.0g/l adaptation note support the stored rate and optional note. The source does not establish every strain or authorize automatic co-use/replacement of cellobiose."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The optional MN301 row and explicit primary10.0g/l adaptation note support the stored rate and optional note. The source does not establish every strain or authorize automatic co-use/replacement of cellobiose."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The optional MN301 row and explicit primary10.0g/l adaptation note support the stored rate and optional note. The source does not establish every strain or authorize automatic co-use/replacement of cellobiose."}]}, {"quantity_id": "q16", "topic": "Main distilled-water input", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].recipe[15]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound": "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Keep main solvent distinct from SL10 makeup and sludge volume.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "preparation_steps.water_input", "stored_value": null, "decision": "add", "rationale": "Source water is1000ml input, not a final-medium-volume declaration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "preparation_steps.water_input", "stored_value": null, "decision": "add", "rationale": "Source water is1000ml input, not a final-medium-volume declaration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "preparation_steps.water_input", "stored_value": null, "decision": "add", "rationale": "Source water is1000ml input, not a final-medium-volume declaration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "preparation_steps.water_input", "stored_value": null, "decision": "unsupported", "rationale": "Variant-specific source access remains unresolved. Source water is1000ml input, not a final-medium-volume declaration.", "missing": true}]}, {"quantity_id": "q17", "topic": "SL10 component: HCl", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\": \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\": \"25%\",\n                        \"amount\": 10,\n                        \"unit\": \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\": 68.5683,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound": "HCl", "compound_id": 68, "attribute": "25%", "amount": 10, "unit": "ml", "g_l": 2.5, "mmol_l": 68.5683, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source is10ml of25% HCl within SL10; unspecified percent basis and density do not establish2.5g. The provider g_l2.5 is retained as a provider observation, never transferred to the main medium."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source is10ml of25% HCl within SL10; unspecified percent basis and density do not establish2.5g. The provider g_l2.5 is retained as a provider observation, never transferred to the main medium."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source is10ml of25% HCl within SL10; unspecified percent basis and density do not establish2.5g. The provider g_l2.5 is retained as a provider observation, never transferred to the main medium."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source is10ml of25% HCl within SL10; unspecified percent basis and density do not establish2.5g. The provider g_l2.5 is retained as a provider observation, never transferred to the main medium."}]}, {"quantity_id": "q18", "topic": "SL10 component: FeCl2 x 4 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\": 1.5,\n                        \"unit\": \"g\",\n                        \"g_l\": 1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "FeCl2 x 4 H2O", "compound_id": 260, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l": 7.54482, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q19", "topic": "SL10 component: ZnCl2", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\": \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\": 70,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound": "ZnCl2", "compound_id": 64, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l": 0.513573, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q20", "topic": "SL10 component: MnCl2 x 4 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\": \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\": 100,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound": "MnCl2 x 4 H2O", "compound_id": 36, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l": 0.505293, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q21", "topic": "SL10 component: H3BO3", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\": \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\": 6,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound": "H3BO3", "compound_id": 37, "amount": 6, "unit": "mg", "g_l": 0.006, "mmol_l": 0.0970246, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q22", "topic": "SL10 component: CoCl2 x 6 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\": \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\": 190,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound": "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19, "mmol_l": 1.46335, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q23", "topic": "SL10 component: CuCl2 x 2 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\": \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\": 2,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound": "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l": 0.0117314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q24", "topic": "SL10 component: NiCl2 x 6 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\": \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\": 24,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound": "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024, "mmol_l": 0.185187, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q25", "topic": "SL10 component: Na2MoO4 x 2 H2O", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\": \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\": 36,\n                        \"unit\": \"mg\",\n                        \"g_l\": 0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound": "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 36, "unit": "mg", "g_l": 0.036, "mmol_l": 0.148791, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component strength from receiving aliquot; no final-medium concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. Source mass and explicit SL10 makeup volume support the local numerical rate only for that stock. The main recipe adds1ml of this stock; the stored direct-medium concentration has lost its stage."}]}, {"quantity_id": "q26", "topic": "SL10 solvent and explicit stock makeup", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\": \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\": 990,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound": "Distilled water", "compound_id": 4, "amount": 990, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}, {"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "Finally make up to 1000.00 ml."}], "decision": "mixed", "rationale": "The final-volume instruction belongs only to SL10, not the whole growth medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "solutions.SL10.preparation", "stored_value": null, "decision": "add", "rationale": "The primary lists990ml water and explicit1000ml final stock makeup.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "solutions.SL10.preparation", "stored_value": null, "decision": "add", "rationale": "The primary lists990ml water and explicit1000ml final stock makeup.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "solutions.SL10.preparation", "stored_value": null, "decision": "add", "rationale": "The primary lists990ml water and explicit1000ml final stock makeup.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "solutions.SL10.preparation", "stored_value": null, "decision": "unsupported", "rationale": "Variant-specific source access remains unresolved. The primary lists990ml water and explicit1000ml final stock makeup.", "missing": true}]}, {"quantity_id": "q27", "topic": "Sludge starting volume", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\": \"Sludge\",\n                        \"compound_id\": 2084,\n                        \"amount\": 1000,\n                        \"unit\": \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound": "Sludge", "compound_id": 2084, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}], "decision": "mixed", "rationale": "The receiving main-medium sludge-fluid aliquot is separately documented; do not flatten a raw sludge volume into main-medium mass.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source uses1000ml sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong stage. No density or finished chemical composition is known."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source uses1000ml sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong stage. No density or finished chemical composition is known."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source uses1000ml sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong stage. No density or finished chemical composition is known."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession remains inaccessible; current local value is retained and compared with the base source only. The source uses1000ml sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong stage. No density or finished chemical composition is known."}]}, {"quantity_id": "q28", "topic": "Main staged anaerobic preparation", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "source_scope": "Entire exact source step was read; quantitative control summary is interpretation, not quoted source text.", "quote": "{\n                        \"step\": \"Dissolve ingredients (except cysteine, carbonate, cellobiose and sulfide), bring medium to the boil, then cool to room temperature under 80% N2 and 20% CO2 gas mixture and add cysteine. Dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Sterilize cellobiose separately by filtration under 100% N2 gas. Adjust pH of the complete medium to 7.0, if necessary.\"\n                    }", "exact_decoded_object": {"step": "Dissolve ingredients (except cysteine, carbonate, cellobiose and sulfide), bring medium to the boil, then cool to room temperature under 80% N2 and 20% CO2 gas mixture and add cysteine. Dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Sterilize cellobiose separately by filtration under 100% N2 gas. Adjust pH of the complete medium to 7.0, if necessary."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals existing JSON locator."}], "decision": "evidence_only", "rationale": "Distinct cysteine timing, separately sterilized carbonate/sulfide stocks, separately filtered cellobiose,80/20 nitrogen/carbon-dioxide and100%nitrogen contexts; complete-medium pH7.0. Stock strengths and aliquots for carbonate/sulfide are not supplied.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients (except cysteine, carbonate, cellobiose and sulfide), bring medium to the boil, then cool to room temperature under 80% N2 and 20% CO2 gas mixture and add cysteine. Dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add sulfide from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture. Sterilize cellobiose separately by filtration under 100% N2 gas. Adjust pH of the complete medium to 7.0, if necessary.", "decision": "evidence_only", "rationale": "Existing owner text matches the current source step and is credited; attach source-stage evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}]}, {"quantity_id": "q29", "topic": "Conditional cellulose adaptation", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T10:18:19.996238Z", "source_scope": "Entire exact source step was read; quantitative control summary is interpretation, not quoted source text.", "quote": "{\n                        \"step\": \"Note: Some strains can be adapted to cellulose as substrate using 10.0 g/l cellulose powder MN 301 (MACHEREY-NAGEL).\"\n                    }", "exact_decoded_object": {"step": "Note: Some strains can be adapted to cellulose as substrate using 10.0 g/l cellulose powder MN 301 (MACHEREY-NAGEL)."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals existing JSON locator."}], "decision": "evidence_only", "rationale": "The10.0g/l cellulose adaptation is conditional on some strains and preserves MN301 grade; no particular strain is identified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "Note: Some strains can be adapted to cellulose as substrate using 10.0 g/l cellulose powder MN 301 (MACHEREY-NAGEL).", "decision": "evidence_only", "rationale": "Existing owner text matches the current source step and is credited; attach source-stage evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}]}, {"quantity_id": "q30", "topic": "SL10 preparation", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "source_scope": "Entire exact source step was read; quantitative control summary is interpretation, not quoted source text.", "quote": "{\n                        \"step\": \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.\"\n                    }", "exact_decoded_object": {"step": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals existing JSON locator."}], "decision": "evidence_only", "rationale": "Iron is dissolved first in acid before other salts; explicit1000ml stock makeup.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "preparation_steps[2].description", "stored_value": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally make up to 1000.00 ml.", "decision": "evidence_only", "rationale": "Existing owner text matches the current source step and is credited; attach source-stage evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}]}, {"quantity_id": "q31", "topic": "Sludge-fluid preparation", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "source_scope": "Entire exact source step was read; quantitative control summary is interpretation, not quoted source text.", "quote": "{\n                        \"step\": \"Add 0.4% yeast extract to sludge from an anaerobic digester, and after gassing with nitrogen gas for a few minutes incubate it at 37\\u00b0C for 24 hours. Then centrifuge the sludge at 13000 g and autoclave the resulting, clear supernatant in screw-capped vessels under nitrogen gas. The sludge fluid can be stored at 8-12\\u00b0C in the dark.\"\n                    }", "exact_decoded_object": {"step": "Add 0.4% yeast extract to sludge from an anaerobic digester, and after gassing with nitrogen gas for a few minutes incubate it at 37°C for 24 hours. Then centrifuge the sludge at 13000 g and autoclave the resulting, clear supernatant in screw-capped vessels under nitrogen gas. The sludge fluid can be stored at 8-12°C in the dark."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals existing JSON locator."}], "decision": "evidence_only", "rationale": "The0.4% yeast-extract statement accompanies4g/1000ml starting sludge; nitrogen processing,37°C/24h incubation,13000g clarification, autoclaving and8–12°C dark storage belong to this stock. Process loss and finished composition remain unknown.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "preparation_steps[3].description", "stored_value": "Add 0.4% yeast extract to sludge from an anaerobic digester, and after gassing with nitrogen gas for a few minutes incubate it at 37°C for 24 hours. Then centrifuge the sludge at 13000 g and autoclave the resulting, clear supernatant in screw-capped vessels under nitrogen gas. The sludge fluid can be stored at 8-12°C in the dark.", "decision": "evidence_only", "rationale": "Existing owner text matches the current source step and is credited; attach source-stage evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}]}, {"quantity_id": "q32", "topic": "Rumen-fluid preparation", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "source_scope": "Entire exact source step was read; quantitative control summary is interpretation, not quoted source text.", "quote": "{\n                        \"step\": \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121\\u00b0C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20\\u00b0C.\"\n                    }", "exact_decoded_object": {"step": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently equals existing JSON locator."}], "decision": "evidence_only", "rationale": "Rumen fluid uses121°C/15min sterilization,27000g/20min clarification,100%nitrogen/15min sparging,30%vial fill and−20°C storage. These controls belong to the rumen stock, not main-medium incubation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "preparation_steps[4].description", "stored_value": "Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of volume and then stored frozen at -20°C.", "decision": "evidence_only", "rationale": "Existing owner text matches the current source step and is credited; attach source-stage evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Missing process context; keep exact source and variant scope.", "missing": true}]}, {"quantity_id": "q33", "topic": "Complete-medium pH", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f", "locator": "$.data.medium; $.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z", "quote": "Adjust pH of the complete medium to 7.0, if necessary."}], "decision": "mixed", "rationale": "Do not transfer a stock-preparation or storage condition to the medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Base primary and API agree on complete-medium pH7.0."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Base primary and API agree on complete-medium pH7.0."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Base primary and API agree on complete-medium pH7.0."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale": "Base primary and API establish pH7.0; exact variant source remains inaccessible."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:005010.

All nineteen asserted ingredient CHEBI identifiers resolve to current labels; supplied-form fidelity still fails for phosphate trihydrate, nickel hexahydrate and sodium resazurin. All20 OLS objects including the nickel alternative and current exact preferred catalog rows were read. Catalogue aliases/rejected rows are observations, never automatic grounding approval.

### History and evidence scope

provenance: concern. Targets: CultureMech:005010.

Seven exact historical concentration reports plus the scoped DSM320/KOMODO320 archive row and method were read. Four October5 reports checked zero source claims; three October7 reports leave quantities unresolved. Their identical cited API raw digest matches the fresh response, with exact literal/decoded joins recorded. Old catalogue fragments remain derivative because both current route forms return403. All source histories remain unchanged.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:005010.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:005010.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Separate stock inputs and receiving additions

major / open / confirmed; issue key: culturemech-005010-separate-stock-inputs-and-receiving-additions.

The generated target and two base contributors encode source stock components as direct-medium concentrations. Their yeast4.5 combines two stages, sludge1000G_PER_L misstates a liquid input, and HCl2.5 cannot be authenticated from bare25%. The replacement contributor copies the same values, but its exact source quantities remain unsupported. Missing stock additions and solvent context prevent faithful interpretation. Ordinary primary gram inputs agree with provider numerals but do not establish final-medium volume.

### f2: Retain the explicit rumen-to-sludge variant

major / open / confirmed; issue key: culturemech-005010-retain-the-explicit-rumen-to-sludge-variant.

The named replacement contributor is merged as a synonym while both fluid additions and their choice are absent. The base source already distinguishes them; copied flattened ingredient equality and SOURCE_DUPLICATE metadata do not prove the replacement is an identical formulation.

### f3: Preserve anaerobic preparation and its stock boundaries

major / open / confirmed; issue key: culturemech-005010-preserve-anaerobic-preparation-and-its-stock-boundaries.

The DSM owner already retains all five preparation descriptions, but generated and KOMODO layers omit them and retain Aerobic:Yes. The primary requires anaerobic main-medium handling. Stock processing and storage controls must remain associated with their own fluid or trace recipe.

### f4: Resolve supplied hydrate and sodium-salt forms

major / open / confirmed; issue key: culturemech-005010-resolve-supplied-hydrate-and-sodium-salt-forms.

K2HPO4 trihydrate is mapped to CHEBI:131527 whose formula is anhydrous despite a trihydrate synonym; nickel hexahydrate is mapped to anhydrous CHEBI:34887 instead of the verified53542 candidate; sodium resazurin is mapped to neutral CHEBI:8806. All asserted labels resolve, but label equality and current MIM aliases do not establish exact supplied form.

### f5: Preserve malformed history and add claim-level traceability

minor / open / confirmed; issue key: culturemech-005010-preserve-malformed-history-and-add-claim-level-traceability.

The original KOMODO timestamp2026-01-27T01:15:02.fZ is malformed in the selected record and both KOMODO owners. Historical concentration reports retain unresolved decisions; no attached claim evidence appears in the four files. Their current raw API matches authenticate the quoted bytes only, not old retrieval events.

## Recommended Actions And Acceptance Checks

### action1

Reconstruct explicit main-medium, SL10 and biological-fluid stock stages in the maintained contributors using the complete quantity inventory. Preserve unknown percent basis, density, finished sludge composition and final-medium volume; do not replace them with guessed concentrations.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Resolve the exact replacement accession when available, retain its substitution as a distinct source-scoped formulation or explicit variant, and preserve optional/alternative fields in the importer. Do not transfer all base-medium amounts solely from its name or historical link.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Preserve the existing DSM source text and attach exact source-stage evidence, reconcile the contradictory aerobic metadata, and represent missing base preparation in the maintained KOMODO record. Treat the replacement preparation as unverified until its scope is resolved. Do not reapply stock storage temperatures as organism growth temperatures.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Retain explicit supplied forms, verify form-specific identifiers in authoritative chemical sources, and reconcile both primary and MIM-keyed term slots. Nickel hexahydrate53542 is independently verified; no unverified replacement is proposed for phosphate trihydrate or sodium resazurin.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

Keep original history append-only, document any verified timestamp correction without inventing an old event time, and attach evidence to each curated claim. Repair current timestamp generation before future imports; do not treat old report coverage as source-verified scientific status.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-3 | data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| dsm320 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf; Exact source identity and scoped formulation/preparation | supports | Complete two-page primary recipe and both page images read: distinct main, SL10, sludge and rumen sections; source batch inputs and preparation are preserved without inferring final medium volume. |
| api320 | https://mediadive.dsmz.de/rest/medium/320; Exact source identity and scoped formulation/preparation | supports | Complete current medium320 response read; all four solution objects, every recipe and step inspected. The declared main volume1021 is provider metadata, not an authoritative final-volume instruction. |
| komodo320 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=320; Exact requested URL and actual HTTP result | context_only | Exact bounded public route returned HTTP403; preserved response supplies no source formulation or current accession validation. |
| komodoVariant | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=320_replace_Rumen%20fluid%2C%20clarified_with_Sludge%20fluid%20%28medium%20119%29; Exact requested URL and actual HTTP result | context_only | Exact bounded public route returned HTTP403; preserved response supplies no source formulation or current accession validation. |
| komodoList | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact requested URL and actual HTTP result | context_only | Exact bounded public route returned HTTP403; preserved response supplies no source formulation or current accession validation. |
| komodoHistoricalList | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; Exact requested URL and actual HTTP result | context_only | Exact bounded public route returned HTTP403; preserved response supplies no source formulation or current accession validation. |
| identity-search | REVIEW_WORK/batch063/record01/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| historical-1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Selected cellulovorans pair at line308 plus report purpose/method and validation claims only; other651 pair-specific conclusions are outside scope. | context_only | Selected exact reciprocal DSM320/KOMODO320 relationship row and method support a historical source-duplicate annotation, not current formulation completeness or preparation equality. Other pairs are outside scope. |
| historical-2 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 33 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-3 | reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 33 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-4 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_cellulovorans_medium.yaml.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Current independent capture exactly matches the cited old response digest; 33 historical literal/decoded objects join. Access-event provenance remains historical. |
| historical-5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulovorans_medium.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-8 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.md; Complete exact-header report, including unchanged/unsupported claims, source objects and narrative; repeated literal rows compared losslessly. | context_only | Historical derivative context; current response does not authenticate the old full raw digest. Exact object matches and differences are recorded separately; old conclusions are reassessed. |
| historical-reader | REVIEW_WORK/batch063/record01/historical-reader.json | context_only | Full exact-header historical texts and scoped large report, with literal/decoded current-source joins and explicit mismatches. Historical access events are not reauthenticated. |
| attached-evidence-joins | REVIEW_WORK/batch063/record01/attached-evidence-joins.json | context_only | Every existing attached evidence claim is preserved and compared to the exact freshly captured response. Matching snippets do not authenticate historical access times. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions, _parse_preparation_steps | context_only | Current _parse_api_composition uses only the first solution, excludes solvent and stock additions, and retains provider g_l. _parse_api_solutions preserves solution names/IDs, amounts and percent attributes but does not copy optional or condition, so the rumen/sludge alternative still needs explicit preservation. _parse_preparation_steps concatenates every solution stage into the root list. None establishes historical execution. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole contributor with merge metadata. For multiple contributors it passes records to merge_formulation_evidence, which checks compatibility; it does not authorize merging different preparation assertions. |
| writer-formulation | src/culturemech/merge/formulation.py; formulation_content, merge_formulation_evidence | context_only | Current compatibility preserves scientific fields and list order and rejects unequal formulations; only specified provenance/evidence lists are unioned. It performs no concentration conversion or stock expansion and does not authenticate historical merges. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_duplicate_ingredients, merge_ingredient_group | context_only | Current cleanup groups identical normalized names, keeps the first entry as a base, flags differing concentrations and combines a warning note; it does not sum concentrations. It can still discard distinctions when names repeat, so source stage must be retained. Current behavior does not establish the historical cause of an existing discrepancy. |
| writer-komodo | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current _convert_to_culturemech imports source flags and pH, defaults physical state to LIQUID, leaves composition empty, and uses time.strftime with %f. It neither verifies a formulation nor interprets a replacement variant. The retained malformed old event is not silently rewritten. |
| writer-resolver | src/culturemech/enrich/dsmz_resolver.py; merge_composition; resolve_recipe | context_only | Current merge_composition copies ingredients and existing solutions plus selected type/state/pH fields, but does not copy preparation_steps. resolve_recipe processes only KOMODO-prefixed files with empty ingredients. Re-running it is not a repair for these already populated or renamed variant records. |
| mim-catalog | src/culturemech/data/mediaingredientmech/label_index.csv; Complete document | context_only | Current exact-identifier and ontology-linked preferred rows read; rejected or differently hydrated aliases are not endorsed as supplied-form equivalence. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete document | context_only | Packaged snapshot9077rows, source commit6643131b0f12ab40b66f98135245fca04027e0e9 and exact SHA checked; current availability is distinct from historical migration validity. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542; Exact source identity and scoped formulation/preparation | supports | Exact current nickel chloride hexahydrate alternative: composition includes six waters and is distinct from anhydrous34887. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91248 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17057 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17057; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi18246 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18246; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch063/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch063/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch063/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch063/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch063/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch063/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch063/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch063/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch063/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- Both exact KOMODO MediaInfo routes and both prefixed/historical catalogue routes returned403. The DSM base is independently verified, but exact current replacement-accession identity and variant completeness are unresolved; completion is partial.
- Main water1000ml and provider volume1021 are not an explicit final-medium volume. No total-volume normalization, density-based HCl conversion, reducing-stock concentration or aliquot is inferred.
- SL10 has explicit1000ml final stock makeup. Sludge-fluid input and preparation do not establish its post-processing composition. The optional cellulose statement does not identify strains or unambiguously define co-use versus replacement of cellobiose.
- Only the selected pair/method/validation portions of the broad historical source-duplicate report are assessed; other pairs are outside scope. Current matching raw bytes do not authenticate historical access-event time.
- Exact current MIM preferred-row and ontology matches do not prove historical linkage correctness. No standalone solution dependency is asserted from a matching name alone.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T103139Z-batch063-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: Review Clostridium cellulovorans medium and its merged contributors
started_at: '2026-10-28T10:18:10.364830Z'
finished_at: '2026-10-28T10:31:39.774456Z'
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
summary: DSM320 supports the base-medium identity and separate stock recipes. The
  generated record and maintained contributors flatten stock inputs, combine yeast-extract
  stages and lose the explicit rumen/sludge alternative. Existing DSM preparation
  is credited; exact KOMODO source access remains unresolved.
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
  - path: data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
    sha256: 7a7b704f8bffd8582a58a7564afafe4964538b3696713cfdce09f37df4bceee2
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    sha256: a0be0126bd2f44388d4dcdafaea7e12b155366510458c9c092a4128dd7ba9930
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    sha256: 92165e1e2deb13a27333e4a3015225fdd32a05a79277032c56f6ba89f0a2d344
    role: context
  - path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    sha256: 8393bdb531bc80a32f60fd7d81c44e5f2f34f914c0569ba0c4975f2bfe551da6
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml.md
    sha256: 944219bd73ee5e095e05b0b6ed076afeaf3d39f6ccd7aa0b0a820c5ba778940e
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml.md
    sha256: f2d938c573903d24c3fe1cabd02ea395a5239e05b99b3a7b4db08d6d634aa2c8
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_cellulovorans_medium.yaml.md
    sha256: 8b86136a91ded8f8653b89032010c0cb9d6e5ef39c6b885ad49c816cd27e019f
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.md
    sha256: 142fce87c11385cd1522d6c0e82f78d5a914f728720f3c2ab13953e66dd33ab7
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.md
    sha256: 4acad631dfdcd094a179c27b3758ee239b7cec7e134153d4f69e9dcf02f581c1
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulovorans_medium.md
    sha256: 654a6d3dbd7537e6c00182f80b726d4bb9e7f3dd9202215160f7d532b68ac221
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.md
    sha256: 0501f84257dd627a86530f26bdb7f0874ed22f1a1603cdc69a987edfe008a391
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_media_variant_links.py
    sha256: 2931b0c5d4374cdaa6d256aed8f65f564a8b285bba741ec914f3a516eed50c07
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_media_variant_links.py
    sha256: d18ef71320a0c50abe085e151d0d0d4d963007d1e1c9afbefab97581a983e31e
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
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
scope:
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch063 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005010
targets:
- target_id: CultureMech:005010
  path: data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
  label: clostridium_cellulovorans_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:005010
  command: just validate-schema data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
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
  - CultureMech:005010
  command: just validate-strict data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
    --out REVIEW_WORK/batch063/record01/strict.tsv --workers 1
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
  - CultureMech:005010
  command: just validate-terms data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
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
  - CultureMech:005010
  command: just validate-references data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 7a7b704f8bffd8582a58a7564afafe4964538b3696713cfdce09f37df4bceee2
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: a0be0126bd2f44388d4dcdafaea7e12b155366510458c9c092a4128dd7ba9930
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 92165e1e2deb13a27333e4a3015225fdd32a05a79277032c56f6ba89f0a2d344
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
  locator: Complete document
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 8393bdb531bc80a32f60fd7d81c44e5f2f34f914c0569ba0c4975f2bfe551da6
- evidence_id: dsm320
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium320.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:18:20.196861Z'
  support: supports
  summary: 'Complete two-page primary recipe and both page images read: distinct main,
    SL10, sludge and rumen sections; source batch inputs and preparation are preserved
    without inferring final medium volume.'
  snapshot_sha256: d1fd0f4c9f8460271297a9295b2d1fabae5d4bce3a2fe3ed5f3036e4fa6796f9
- evidence_id: api320
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/320
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:18:19.996238Z'
  support: supports
  summary: Complete current medium320 response read; all four solution objects, every
    recipe and step inspected. The declared main volume1021 is provider metadata,
    not an authoritative final-volume instruction.
  snapshot_sha256: d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f
- evidence_id: komodo320
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=320
  locator: Exact requested URL and actual HTTP result
  accessed_at: '2026-10-28T10:18:19.540237Z'
  support: context_only
  summary: Exact bounded public route returned HTTP403; preserved response supplies
    no source formulation or current accession validation.
  snapshot_sha256: d0ee44fe1155f9f7a9e4500686f1863139ef1d4cbf3b0d1ef77962c2cd9eba47
- evidence_id: komodoVariant
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=320_replace_Rumen%20fluid%2C%20clarified_with_Sludge%20fluid%20%28medium%20119%29
  locator: Exact requested URL and actual HTTP result
  accessed_at: '2026-10-28T10:18:19.464256Z'
  support: context_only
  summary: Exact bounded public route returned HTTP403; preserved response supplies
    no source formulation or current accession validation.
  snapshot_sha256: 0864b8ffee5506b45127d75f4256c62e1377645c56b8e79dc8ea32cca0ece614
- evidence_id: komodoList
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact requested URL and actual HTTP result
  accessed_at: '2026-10-28T10:18:19.515749Z'
  support: context_only
  summary: Exact bounded public route returned HTTP403; preserved response supplies
    no source formulation or current accession validation.
  snapshot_sha256: 1107b7e12429aa85776ad0c647a29b45d9eb53296e271d79b196db6663364508
- evidence_id: komodoHistoricalList
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: Exact requested URL and actual HTTP result
  accessed_at: '2026-10-28T10:21:36.123601Z'
  support: context_only
  summary: Exact bounded public route returned HTTP403; preserved response supplies
    no source formulation or current accession validation.
  snapshot_sha256: d6bfcf3dd92abbb0d6c4ab6a3853efa09ff5fc4db7aeb9940a291c71f8f992dc
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch063/record01/identity-search.json
  accessed_at: '2026-10-28T10:26:05.518474Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: acca0650f82cfa389870680b697047880988bb884add49840369ebdcee7fd01c
- evidence_id: historical-1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Selected cellulovorans pair at line308 plus report purpose/method and validation
    claims only; other651 pair-specific conclusions are outside scope.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Selected exact reciprocal DSM320/KOMODO320 relationship row and method
    support a historical source-duplicate annotation, not current formulation completeness
    or preparation equality. Other pairs are outside scope.
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    33 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 944219bd73ee5e095e05b0b6ed076afeaf3d39f6ccd7aa0b0a820c5ba778940e
- evidence_id: historical-3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-1000-1500/records/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    33 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: f2d938c573903d24c3fe1cabd02ea395a5239e05b99b3a7b4db08d6d634aa2c8
- evidence_id: historical-4
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/clostridium_cellulovorans_medium.yaml.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current independent capture exactly matches the cited old response digest;
    33 historical literal/decoded objects join. Access-event provenance remains historical.
  snapshot_sha256: 8b86136a91ded8f8653b89032010c0cb9d6e5ef39c6b885ad49c816cd27e019f
- evidence_id: historical-5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 142fce87c11385cd1522d6c0e82f78d5a914f728720f3c2ab13953e66dd33ab7
- evidence_id: historical-6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 4acad631dfdcd094a179c27b3758ee239b7cec7e134153d4f69e9dcf02f581c1
- evidence_id: historical-7
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulovorans_medium.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 654a6d3dbd7537e6c00182f80b726d4bb9e7f3dd9202215160f7d532b68ac221
- evidence_id: historical-8
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.md
  locator: Complete exact-header report, including unchanged/unsupported claims, source
    objects and narrative; repeated literal rows compared losslessly.
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Historical derivative context; current response does not authenticate the
    old full raw digest. Exact object matches and differences are recorded separately;
    old conclusions are reassessed.
  snapshot_sha256: 0501f84257dd627a86530f26bdb7f0874ed22f1a1603cdc69a987edfe008a391
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch063/record01/historical-reader.json
  accessed_at: '2026-10-28T10:26:05.523151Z'
  support: context_only
  summary: Full exact-header historical texts and scoped large report, with literal/decoded
    current-source joins and explicit mismatches. Historical access events are not
    reauthenticated.
  snapshot_sha256: 3a1ba6074431fc2051be51ca2fea02480b2b060dd1d40951c8397d6d589e7888
- evidence_id: attached-evidence-joins
  kind: record_content
  reference: REVIEW_WORK/batch063/record01/attached-evidence-joins.json
  accessed_at: '2026-10-28T10:26:05.523636Z'
  support: context_only
  summary: Every existing attached evidence claim is preserved and compared to the
    exact freshly captured response. Matching snippets do not authenticate historical
    access times.
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions, _parse_preparation_steps
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current _parse_api_composition uses only the first solution, excludes solvent
    and stock additions, and retains provider g_l. _parse_api_solutions preserves
    solution names/IDs, amounts and percent attributes but does not copy optional
    or condition, so the rumen/sludge alternative still needs explicit preservation.
    _parse_preparation_steps concatenates every solution stage into the root list.
    None establishes historical execution.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current merge_group copies a sole contributor with merge metadata. For
    multiple contributors it passes records to merge_formulation_evidence, which checks
    compatibility; it does not authorize merging different preparation assertions.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, merge_formulation_evidence
  accessed_at: '2026-10-28T10:26:05.456619Z'
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
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current cleanup groups identical normalized names, keeps the first entry
    as a base, flags differing concentrations and combines a warning note; it does
    not sum concentrations. It can still discard distinctions when names repeat, so
    source stage must be retained. Current behavior does not establish the historical
    cause of an existing discrepancy.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-komodo
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current _convert_to_culturemech imports source flags and pH, defaults physical
    state to LIQUID, leaves composition empty, and uses time.strftime with %f. It
    neither verifies a formulation nor interprets a replacement variant. The retained
    malformed old event is not silently rewritten.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: writer-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: merge_composition; resolve_recipe
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current merge_composition copies ingredients and existing solutions plus
    selected type/state/pH fields, but does not copy preparation_steps. resolve_recipe
    processes only KOMODO-prefixed files with empty ingredients. Re-running it is
    not a repair for these already populated or renamed variant records.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: mim-catalog
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Complete document
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Current exact-identifier and ontology-linked preferred rows read; rejected
    or differently hydrated aliases are not endorsed as supplied-form equivalence.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-metadata
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete document
  accessed_at: '2026-10-28T10:26:05.456619Z'
  support: context_only
  summary: Packaged snapshot9077rows, source commit6643131b0f12ab40b66f98135245fca04027e0e9
    and exact SHA checked; current availability is distinct from historical migration
    validity.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53542
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T10:18:22.184772Z'
  support: supports
  summary: 'Exact current nickel chloride hexahydrate alternative: composition includes
    six waters and is distinct from anhydrous34887.'
  snapshot_sha256: 1e444345efd33c02d5050deadd66637cc6dae004c55e6962c62abd172291e526
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:20.333927Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:20.937516Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: c70055293606f21dcdfb72325a4677661b51efb723ba9357efab43f8ec9b03f7
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:21.488991Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8fc333e98ee953346b5c291b9e5765e77d03cc46740a1282af3e5f4ad355de1a
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:21.235638Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1635f67d01e00cabdef4ed0d9ef6d5383787c56bd0447051deb90ad353b499a2
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:23.105576Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi91248
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91248
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:23.293525Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 98a5682728cfda4162de150a88ae8c4b3a70c2d7c248634a5108be50a888a692
- evidence_id: chebi29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_29377
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:20.920437Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: dee64859233d0b0898eba91901a001f1faaa5eaab37f7beb7e98318ab8c19569
- evidence_id: chebi17057
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17057
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:20.268455Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: d8316efd6b721c17fedfab7c84433253c14c440dac0dfe410f06186f0e7664d4
- evidence_id: chebi18246
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18246
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:20.892792Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a351d1be4b95210d0845961663661606f29ad6140e6c9ada8a8dbe902b150a53
- evidence_id: chebi76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_76209
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:22.440772Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 3eece7d96d2433ff020ece90db55323d138c5c828b78198f91d26b3eafa91f9f
- evidence_id: chebi17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17883
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:20.625332Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 5f7b2f292559b9033f3c62c8403ed552842a28535010d6af5daa018a0977c28d
- evidence_id: chebi86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86249
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:22.689961Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 69797bf2582679b3f621fa4f982077ed90f48f3a5e1293c7444a3aaacbb25ba2
- evidence_id: chebi49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_49976
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:21.847347Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d2305ca671adbbd3b0cc07b2331373a768bb44d41f32f61ba894594ae470eff
- evidence_id: chebi86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86368
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:22.787350Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2bb4588e6734285b5536bdac78701f9800fdb8d17236d12cf5a1c30490f1614d
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:21.577774Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f23e1405347fa9d8a0826d4dd1279b7cdec8361390d20e439154dcbbd386a2d4
- evidence_id: chebi53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_53503
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:22.081376Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 31dc996638b0cc1341ed24fcb38ec344af726c99d376ac94e952210fcb9ed583
- evidence_id: chebi86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86318
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:22.782276Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 8ba4e0a242571ae9a62ca7ba5c0f4af765962a02f5119a96d47dda9df7c9d593
- evidence_id: chebi34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34887
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:21.566743Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a43b8268f70ae50c4cfbc53e12bbd195618c521619cfab8f71d3704b338af95b
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T10:18:22.184810Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 0271a149a298ff837ad8f690ce8cb0acf111f5d25c5efaf6fa828401ab951d56
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch063/record01/quantity-inventory.json
  accessed_at: '2026-10-28T10:31:39.774456Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 99d23aa68573012939814ed66fb390aec51e6f08e35c5365547d6356b137bd4b
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch063/record01/grounding-inventory.json
  accessed_at: '2026-10-28T10:26:05.576669Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 29b538e41d61b3953067a59bda49e617a2ad365cbdcaccda754f4b52b38a906b
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch063/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T10:26:05.576831Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 911dfb423ee5e0dd08e7b17ac805330cc71d1f2cb05800f2814368b76e6b78ac
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch063/record01/scalar-census.json
  accessed_at: '2026-10-28T10:26:05.576854Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: a394eab6236d3e572164052d6eacae0d76d777b699e5452196807a76caa2805e
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch063/record01/validate-schema.json
  accessed_at: '2026-10-28T10:18:11.469525Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: cdaaeb9cb75a2a6dacffd7967ec0c7887d68ae2ace3e66a2a4a1fc516146c016
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch063/record01/validate-strict.json
  accessed_at: '2026-10-28T10:18:12.486211Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch063/record01/strict.tsv\n"
  snapshot_sha256: 3cdb53b5e7a6a5dc4972c0d6476543818f440c1434ac806ce54932ee7121a833
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch063/record01/validate-terms.json
  accessed_at: '2026-10-28T10:18:13.720814Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: adbfe3e0cb29bedea6a92c91f4c07ad825ca2372d95d37f365c5ef388cf68705
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch063/record01/validate-references.json
  accessed_at: '2026-10-28T10:18:14.479032Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 10c313c5afe46631efa7679c17d2804030110987a44c5c1ebd5c6c9275930ffe
assessments:
- assessment_id: a1
  area: identity
  topic: Base identity and named replacement scope
  outcome: concern
  summary: The generated file resolves to exact three normalized contributors. DSM320
    is verified independently; the replacement label is an explicit variant lead and
    its old exact catalogue row is derivative evidence only. Current403 responses
    prevent independently revalidating the historical KOMODO accessions. Identical
    copied ingredient lists do not establish preparation or variant equivalence.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - local-target
  - identity-search
  - dsm320
  - api320
  - historical-reader
  - komodo320
  - komodoVariant
- assessment_id: a2
  area: consistency
  topic: Source alternatives and current writer behavior
  outcome: concern
  summary: The base primary distinguishes clarified rumen fluid from optional alternative
    sludge fluid. The named replacement contributor has the same copied ingredients
    but lacks a representation of that substitution. Present conservative merge code
    rejects unequal formulation content; source-aware normalization must preserve
    alternatives before regeneration. The current MediaDive solution parser also omits
    source optional/condition fields.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - writer-mediadive
  - writer-merge
  - writer-formulation
  - api320
- assessment_id: a3
  area: completeness
  topic: Preparation, phenotype and claim attachment
  outcome: concern
  summary: Existing DSM owner preparation is retained and credited, while the selected
    target and KOMODO contributors omit it. No attached evidence or target_organisms
    exist in the four complete files. Generic cultivation applications and source
    names do not establish strain-specific growth; iModulonDB is not applicable to
    this medium-only record. Complex/undefined classification agrees with biological
    extracts; liquid status is conditional on the selected formulation, with particulate
    cellulose separately qualified.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - owner-2
  - local-target
  - api320
  - attached-evidence-joins
- assessment_id: a4
  area: grounding
  topic: Ingredient linkage metrics
  outcome: supported
  summary: Each of four layers has22ingredient instances:19primary CHEBI IDs (19/22=86.36%)
    and18mediaingredientmech_chebi_term links (18/22=81.82%); no numeric legacy MIM
    IDs. These are presence metrics, not scientific accuracy. Peptone, yeast extract
    and sludge lack primary IDs; current catalog candidates alone do not justify a
    new exact grounding.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - mim-catalog
  - mim-metadata
  - local-target
- assessment_id: a5
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Main batch input: K2HPO4 x 3 H2O", "source":
    [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"K2HPO4 x 3 H2O\",\n                        \"compound_id\": 244,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 5.74132,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 1, "compound":
    "K2HPO4 x 3 H2O", "compound_id": 244, "amount": 1, "unit": "g", "g_l": 1, "mmol_l":
    5.74132, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession
    remains inaccessible; current local value is retained and compared with the base
    source only. The primary gram input and provider g_l numeral agree with the stored
    digits. Final medium volume is not explicitly stated, so the G_PER_L basis is
    not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q2",
    "topic": "Main batch input: NH4Cl", "source": [{"evidence_id": "api320", "reference":
    "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"NH4Cl\",\n                        \"compound_id\": 42,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 18.6951,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "NH4Cl", "compound_id": 42, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 18.6951,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession
    remains inaccessible; current local value is retained and compared with the base
    source only. The primary gram input and provider g_l numeral agree with the stored
    digits. Final medium volume is not explicitly stated, so the G_PER_L basis is
    not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q3",
    "topic": "Main batch input: KCl", "source": [{"evidence_id": "api320", "reference":
    "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"KCl\",\n                        \"compound_id\": 61,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 6.70691,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "KCl", "compound_id": 61, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l": 6.70691,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The primary gram input and provider g_l numeral agree with
    the stored digits. Final medium volume is not explicitly stated, so the G_PER_L
    basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id":
    "q4", "topic": "Main batch input: MgSO4 x 7 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MgSO4 x 7 H2O\",\n                        \"compound_id\": 8,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"mmol_l\": 2.02859,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MgSO4 x 7 H2O", "compound_id": 8, "amount": 0.5, "unit": "g", "g_l": 0.5, "mmol_l":
    2.02859, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The primary gram input and provider g_l numeral agree with
    the stored digits. Final medium volume is not explicitly stated, so the G_PER_L
    basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id":
    "q5", "topic": "Main batch input: Trypticase peptone", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"Trypticase peptone\",\n                        \"compound_id\": 124,\n                        \"attribute\":
    \"BD BBL\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"g\",\n                        \"g_l\": 0.5,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "Trypticase peptone", "compound_id": 124, "attribute": "BD BBL", "amount": 0.5,
    "unit": "g", "g_l": 0.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "unsupported", "rationale": "Batch mass, provider-declared rate and independently
    established final concentration are distinct claims.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The primary gram input and provider g_l
    numeral agree with the stored digits. Final medium volume is not explicitly stated,
    so the G_PER_L basis is not independently verified; no rescaling is proposed."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The primary gram input and provider g_l numeral agree with
    the stored digits. Final medium volume is not explicitly stated, so the G_PER_L
    basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id":
    "q6", "topic": "Main batch input: L-Cysteine HCl x H2O", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[10]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 11,\n                        \"compound\":
    \"L-Cysteine HCl x H2O\",\n                        \"compound_id\": 770,\n                        \"amount\":
    0.15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.15,\n                        \"mmol_l\": 0.854039,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 11, "compound":
    "L-Cysteine HCl x H2O", "compound_id": 770, "amount": 0.15, "unit": "g", "g_l":
    0.15, "mmol_l": 0.854039, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "unsupported", "rationale": "Batch mass, provider-declared rate and independently
    established final concentration are distinct claims.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.15", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "The primary gram input and provider g_l
    numeral agree with the stored digits. Final medium volume is not explicitly stated,
    so the G_PER_L basis is not independently verified; no rescaling is proposed."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The primary gram input and provider g_l numeral agree with
    the stored digits. Final medium volume is not explicitly stated, so the G_PER_L
    basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id":
    "q7", "topic": "Main batch input: Na2CO3", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[11]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 12,\n                        \"compound\":
    \"Na2CO3\",\n                        \"compound_id\": 32,\n                        \"amount\":
    1,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1,\n                        \"mmol_l\": 9.43503,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 12, "compound":
    "Na2CO3", "compound_id": 32, "amount": 1, "unit": "g", "g_l": 1, "mmol_l": 9.43503,
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession
    remains inaccessible; current local value is retained and compared with the base
    source only. The primary gram input and provider g_l numeral agree with the stored
    digits. Final medium volume is not explicitly stated, so the G_PER_L basis is
    not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q8",
    "topic": "Main batch input: Cellobiose", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[12]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 13,\n                        \"compound\":
    \"Cellobiose\",\n                        \"compound_id\": 214,\n                        \"amount\":
    5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    5,\n                        \"mmol_l\": 14.6071,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 13, "compound":
    "Cellobiose", "compound_id": 214, "amount": 5, "unit": "g", "g_l": 5, "mmol_l":
    14.6071, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram input and
    provider g_l numeral agree with the stored digits. Final medium volume is not
    explicitly stated, so the G_PER_L basis is not independently verified; no rescaling
    is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "5", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement accession
    remains inaccessible; current local value is retained and compared with the base
    source only. The primary gram input and provider g_l numeral agree with the stored
    digits. Final medium volume is not explicitly stated, so the G_PER_L basis is
    not independently verified; no rescaling is proposed."}]}, {"quantity_id": "q9",
    "topic": "Main batch input: Na2S x 9 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[14]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 15,\n                        \"compound\":
    \"Na2S x 9 H2O\",\n                        \"compound_id\": 54,\n                        \"amount\":
    0.15,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.15,\n                        \"mmol_l\": 0.624526,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 15, "compound":
    "Na2S x 9 H2O", "compound_id": 54, "amount": 0.15, "unit": "g", "g_l": 0.15, "mmol_l":
    0.624526, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "unsupported",
    "rationale": "Batch mass, provider-declared rate and independently established
    final concentration are distinct claims.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "The primary gram
    input and provider g_l numeral agree with the stored digits. Final medium volume
    is not explicitly stated, so the G_PER_L basis is not independently verified;
    no rescaling is proposed."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The primary gram input and provider g_l numeral agree with
    the stored digits. Final medium volume is not explicitly stated, so the G_PER_L
    basis is not independently verified; no rescaling is proposed."}]}, {"quantity_id":
    "q10", "topic": "Main yeast extract versus sludge-preparation yeast extract",
    "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[5]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    0.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    0.5,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 6, "compound": "Yeast extract", "compound_id": 16, "amount":
    0.5, "unit": "g", "g_l": 0.5, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}, {"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"Yeast extract\",\n                        \"compound_id\": 16,\n                        \"amount\":
    4,\n                        \"unit\": \"g\",\n                        \"g_l\":
    4,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "Yeast extract", "compound_id": 16, "amount":
    4, "unit": "g", "g_l": 4, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Keep the two source stages separate; finished sludge composition
    after processing is not inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The local4.5 sums the0.5g
    main input and4g separate sludge-preparation input. That sum is neither the main
    batch addition nor an established final-medium rate."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The local4.5 sums the0.5g
    main input and4g separate sludge-preparation input. That sum is neither the main
    batch addition nor an established final-medium rate."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5",
    "unit": "G_PER_L"}, "decision": "conflict", "rationale": "The local4.5 sums the0.5g
    main input and4g separate sludge-preparation input. That sum is neither the main
    batch addition nor an established final-medium rate."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The local4.5 sums the0.5g main input and4g separate sludge-preparation
    input. That sum is neither the main batch addition nor an established final-medium
    rate."}]}, {"quantity_id": "q11", "topic": "Required clarified rumen fluid", "source":
    [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[6]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"solution\":
    \"Clarified rumen fluid\",\n                        \"solution_id\": 2618,\n                        \"condition\":
    \"\",\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 7, "solution": "Clarified rumen fluid", "solution_id": 2618,
    "condition": "", "amount": 20, "unit": "ml", "optional": 0}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "mixed", "rationale": "Restore source additions with explicit choice
    semantics; shared missing collection is not a claim that each row has the same
    identity.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Variant-specific source access remains unresolved. The main recipe explicitly
    adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing":
    true}]}, {"quantity_id": "q12", "topic": "Optional alternative sludge fluid",
    "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[7]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"solution\":
    \"Sludge fluid\",\n                        \"solution_id\": 208,\n                        \"condition\":
    \"alternative\",\n                        \"amount\": 20,\n                        \"unit\":
    \"ml\",\n                        \"optional\": 1\n                    }", "exact_decoded_object":
    {"recipe_order": 8, "solution": "Sludge fluid", "solution_id": 208, "condition":
    "alternative", "amount": 20, "unit": "ml", "optional": 1}, "quote_basis": "Literal
    UTF-8 raw-response substring; decoded object independently equals exact JSON locator."}],
    "decision": "mixed", "rationale": "Restore source additions with explicit choice
    semantics; shared missing collection is not a claim that each row has the same
    identity.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 20ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Variant-specific source access remains unresolved. The main recipe explicitly
    adds 20ml; preserve name, stage and the exact optional/alternative status.", "missing":
    true}]}, {"quantity_id": "q13", "topic": "Trace solution SL10 addition", "source":
    [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[8]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"solution\":
    \"Trace element solution SL-10\",\n                        \"solution_id\": 595,\n                        \"amount\":
    1,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "solution":
    "Trace element solution SL-10", "solution_id": 595, "amount": 1, "unit": "ml",
    "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded
    object independently equals exact JSON locator."}], "decision": "mixed", "rationale":
    "Restore source additions with explicit choice semantics; shared missing collection
    is not a claim that each row has the same identity.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "add", "rationale": "The main recipe
    explicitly adds 1ml; preserve name, stage and the exact optional/alternative status.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 1ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "The main recipe explicitly adds 1ml; preserve name, stage and the exact optional/alternative
    status.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Variant-specific source access remains unresolved. The main recipe explicitly
    adds 1ml; preserve name, stage and the exact optional/alternative status.", "missing":
    true}]}, {"quantity_id": "q14", "topic": "Sodium-resazurin stock strength and
    aliquot", "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[9]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Sodium resazurin\",\n                        \"compound_id\": 1852,\n                        \"attribute\":
    \"0.1% w/v\",\n                        \"amount\": 0.5,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 0.0005,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Sodium resazurin", "compound_id": 1852, "attribute": "0.1% w/v", "amount": 0.5,
    "unit": "ml", "g_l": 0.0005, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "0.1g/100ml ×0.5ml =0.0005g input. No final-volume denominator
    is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies0.5ml
    of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l
    numeral. It omits the stock and addition stage and does not independently establish
    final G_PER_L."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies0.5ml
    of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l
    numeral. It omits the stock and addition stage and does not independently establish
    final G_PER_L."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source supplies0.5ml
    of0.1%w/v stock; the encoded0.0005 equals the0.0005g input mass and provider g_l
    numeral. It omits the stock and addition stage and does not independently establish
    final G_PER_L."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.0005",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The source supplies0.5ml of0.1%w/v stock; the encoded0.0005
    equals the0.0005g input mass and provider g_l numeral. It omits the stock and
    addition stage and does not independently establish final G_PER_L."}]}, {"quantity_id":
    "q15", "topic": "Conditional cellulose substrate", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[13]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 14,\n                        \"compound\":
    \"Cellulose\",\n                        \"compound_id\": 400,\n                        \"condition\":
    \"MN 301\",\n                        \"amount\": 10,\n                        \"unit\":
    \"g\",\n                        \"optional\": 1\n                    }", "exact_decoded_object":
    {"recipe_order": 14, "compound": "Cellulose", "compound_id": 400, "condition":
    "MN 301", "amount": 10, "unit": "g", "optional": 1}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals exact JSON locator."},
    {"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "10.0 g/l cellulose"}], "decision": "mixed", "rationale": "Retain the
    exact conditional substrate scope; this is the one explicit primary main-medium
    g/l statement.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The optional MN301
    row and explicit primary10.0g/l adaptation note support the stored rate and optional
    note. The source does not establish every strain or authorize automatic co-use/replacement
    of cellobiose."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The optional MN301
    row and explicit primary10.0g/l adaptation note support the stored rate and optional
    note. The source does not establish every strain or authorize automatic co-use/replacement
    of cellobiose."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The optional MN301
    row and explicit primary10.0g/l adaptation note support the stored rate and optional
    note. The source does not establish every strain or authorize automatic co-use/replacement
    of cellobiose."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The optional MN301 row and explicit primary10.0g/l adaptation
    note support the stored rate and optional note. The source does not establish
    every strain or authorize automatic co-use/replacement of cellobiose."}]}, {"quantity_id":
    "q16", "topic": "Main distilled-water input", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].recipe[15]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 16,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 16, "compound":
    "Distilled water", "compound_id": 4, "amount": 1000, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}], "decision": "mixed", "rationale": "Keep main solvent
    distinct from SL10 makeup and sludge volume.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "preparation_steps.water_input", "stored_value": null, "decision": "add", "rationale":
    "Source water is1000ml input, not a final-medium-volume declaration.", "missing":
    true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "preparation_steps.water_input", "stored_value": null, "decision":
    "add", "rationale": "Source water is1000ml input, not a final-medium-volume declaration.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "preparation_steps.water_input", "stored_value": null, "decision":
    "add", "rationale": "Source water is1000ml input, not a final-medium-volume declaration.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "preparation_steps.water_input", "stored_value": null, "decision":
    "unsupported", "rationale": "Variant-specific source access remains unresolved.
    Source water is1000ml input, not a final-medium-volume declaration.", "missing":
    true}]}, {"quantity_id": "q17", "topic": "SL10 component: HCl", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 1,\n                        \"compound\":
    \"HCl\",\n                        \"compound_id\": 68,\n                        \"attribute\":
    \"25%\",\n                        \"amount\": 10,\n                        \"unit\":
    \"ml\",\n                        \"g_l\": 2.5,\n                        \"mmol_l\":
    68.5683,\n                        \"optional\": 0\n                    }", "exact_decoded_object":
    {"recipe_order": 1, "compound": "HCl", "compound_id": 68, "attribute": "25%",
    "amount": 10, "unit": "ml", "g_l": 2.5, "mmol_l": 68.5683, "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "mixed", "rationale": "Separate stock-component
    strength from receiving aliquot; no final-medium concentration is calculated.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source is10ml of25% HCl
    within SL10; unspecified percent basis and density do not establish2.5g. The provider
    g_l2.5 is retained as a provider observation, never transferred to the main medium."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source is10ml of25% HCl
    within SL10; unspecified percent basis and density do not establish2.5g. The provider
    g_l2.5 is retained as a provider observation, never transferred to the main medium."},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source is10ml of25% HCl
    within SL10; unspecified percent basis and density do not establish2.5g. The provider
    g_l2.5 is retained as a provider observation, never transferred to the main medium."},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "2.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source is10ml of25% HCl within SL10; unspecified percent
    basis and density do not establish2.5g. The provider g_l2.5 is retained as a provider
    observation, never transferred to the main medium."}]}, {"quantity_id": "q18",
    "topic": "SL10 component: FeCl2 x 4 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"FeCl2 x 4 H2O\",\n                        \"compound_id\": 260,\n                        \"amount\":
    1.5,\n                        \"unit\": \"g\",\n                        \"g_l\":
    1.5,\n                        \"mmol_l\": 7.54482,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "FeCl2 x 4 H2O", "compound_id": 260, "amount": 1.5, "unit": "g", "g_l": 1.5, "mmol_l":
    7.54482, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Separate stock-component strength from receiving aliquot; no final-medium
    concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "1.5",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q19", "topic": "SL10 component: ZnCl2", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[2]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 3,\n                        \"compound\":
    \"ZnCl2\",\n                        \"compound_id\": 64,\n                        \"amount\":
    70,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.07,\n                        \"mmol_l\": 0.513573,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 3, "compound":
    "ZnCl2", "compound_id": 64, "amount": 70, "unit": "mg", "g_l": 0.07, "mmol_l":
    0.513573, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Separate stock-component strength from receiving aliquot; no final-medium
    concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.07",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q20", "topic": "SL10 component: MnCl2 x 4 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[3]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 4,\n                        \"compound\":
    \"MnCl2 x 4 H2O\",\n                        \"compound_id\": 36,\n                        \"amount\":
    100,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.1,\n                        \"mmol_l\": 0.505293,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 4, "compound":
    "MnCl2 x 4 H2O", "compound_id": 36, "amount": 100, "unit": "mg", "g_l": 0.1, "mmol_l":
    0.505293, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Separate stock-component strength from receiving aliquot; no final-medium
    concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q21", "topic": "SL10 component: H3BO3", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[4]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 5,\n                        \"compound\":
    \"H3BO3\",\n                        \"compound_id\": 37,\n                        \"amount\":
    6,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.006,\n                        \"mmol_l\": 0.0970246,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 5, "compound":
    "H3BO3", "compound_id": 37, "amount": 6, "unit": "mg", "g_l": 0.006, "mmol_l":
    0.0970246, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Separate stock-component strength from receiving aliquot; no final-medium
    concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.006",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q22", "topic": "SL10 component: CoCl2 x 6 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[5]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 6,\n                        \"compound\":
    \"CoCl2 x 6 H2O\",\n                        \"compound_id\": 38,\n                        \"amount\":
    190,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.19,\n                        \"mmol_l\": 1.46335,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 6, "compound":
    "CoCl2 x 6 H2O", "compound_id": 38, "amount": 190, "unit": "mg", "g_l": 0.19,
    "mmol_l": 1.46335, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Separate stock-component strength from receiving aliquot;
    no final-medium concentration is calculated.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "ingredients[17].concentration", "stored_value": {"value": "0.19", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume
    support the local numerical rate only for that stock. The main recipe adds1ml
    of this stock; the stored direct-medium concentration has lost its stage."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.19",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q23", "topic": "SL10 component: CuCl2 x 2 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[6]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 7,\n                        \"compound\":
    \"CuCl2 x 2 H2O\",\n                        \"compound_id\": 39,\n                        \"amount\":
    2,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.002,\n                        \"mmol_l\": 0.0117314,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 7, "compound":
    "CuCl2 x 2 H2O", "compound_id": 39, "amount": 2, "unit": "mg", "g_l": 0.002, "mmol_l":
    0.0117314, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response substring;
    decoded object independently equals exact JSON locator."}], "decision": "mixed",
    "rationale": "Separate stock-component strength from receiving aliquot; no final-medium
    concentration is calculated.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.002",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q24", "topic": "SL10 component: NiCl2 x 6 H2O", "source": [{"evidence_id": "api320",
    "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path": "REVIEW_WORK/batch063/source01/api320.bin",
    "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[7]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 8,\n                        \"compound\":
    \"NiCl2 x 6 H2O\",\n                        \"compound_id\": 40,\n                        \"amount\":
    24,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.024,\n                        \"mmol_l\": 0.185187,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 8, "compound":
    "NiCl2 x 6 H2O", "compound_id": 40, "amount": 24, "unit": "mg", "g_l": 0.024,
    "mmol_l": 0.185187, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Separate stock-component strength from receiving aliquot;
    no final-medium concentration is calculated.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "ingredients[19].concentration", "stored_value": {"value": "0.024", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume
    support the local numerical rate only for that stock. The main recipe adds1ml
    of this stock; the stored direct-medium concentration has lost its stage."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.024",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q25", "topic": "SL10 component: Na2MoO4 x 2 H2O", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[8]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 9,\n                        \"compound\":
    \"Na2MoO4 x 2 H2O\",\n                        \"compound_id\": 9,\n                        \"amount\":
    36,\n                        \"unit\": \"mg\",\n                        \"g_l\":
    0.036,\n                        \"mmol_l\": 0.148791,\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 9, "compound":
    "Na2MoO4 x 2 H2O", "compound_id": 9, "amount": 36, "unit": "mg", "g_l": 0.036,
    "mmol_l": 0.148791, "optional": 0}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals exact JSON locator."}], "decision":
    "mixed", "rationale": "Separate stock-component strength from receiving aliquot;
    no final-medium concentration is calculated.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "ingredients[20].concentration", "stored_value": {"value": "0.036", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "Source mass and explicit SL10 makeup volume
    support the local numerical rate only for that stock. The main recipe adds1ml
    of this stock; the stored direct-medium concentration has lost its stage."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Source mass and explicit
    SL10 makeup volume support the local numerical rate only for that stock. The main
    recipe adds1ml of this stock; the stored direct-medium concentration has lost
    its stage."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "0.036",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. Source mass and explicit SL10 makeup volume support the
    local numerical rate only for that stock. The main recipe adds1ml of this stock;
    the stored direct-medium concentration has lost its stage."}]}, {"quantity_id":
    "q26", "topic": "SL10 solvent and explicit stock makeup", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].recipe[9]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 10,\n                        \"compound\":
    \"Distilled water\",\n                        \"compound_id\": 4,\n                        \"amount\":
    990,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 10, "compound":
    "Distilled water", "compound_id": 4, "amount": 990, "unit": "ml", "optional":
    0}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals exact JSON locator."}, {"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "Finally make up to 1000.00 ml."}], "decision": "mixed", "rationale":
    "The final-volume instruction belongs only to SL10, not the whole growth medium.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "solutions.SL10.preparation", "stored_value": null, "decision":
    "add", "rationale": "The primary lists990ml water and explicit1000ml final stock
    makeup.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "solutions.SL10.preparation", "stored_value": null, "decision":
    "add", "rationale": "The primary lists990ml water and explicit1000ml final stock
    makeup.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "solutions.SL10.preparation", "stored_value": null, "decision":
    "add", "rationale": "The primary lists990ml water and explicit1000ml final stock
    makeup.", "missing": true}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "solutions.SL10.preparation", "stored_value": null, "decision":
    "unsupported", "rationale": "Variant-specific source access remains unresolved.
    The primary lists990ml water and explicit1000ml final stock makeup.", "missing":
    true}]}, {"quantity_id": "q27", "topic": "Sludge starting volume", "source": [{"evidence_id":
    "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320", "raw_path":
    "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[2].recipe[1]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "{\n                        \"recipe_order\": 2,\n                        \"compound\":
    \"Sludge\",\n                        \"compound_id\": 2084,\n                        \"amount\":
    1000,\n                        \"unit\": \"ml\",\n                        \"optional\":
    0\n                    }", "exact_decoded_object": {"recipe_order": 2, "compound":
    "Sludge", "compound_id": 2084, "amount": 1000, "unit": "ml", "optional": 0}, "quote_basis":
    "Literal UTF-8 raw-response substring; decoded object independently equals exact
    JSON locator."}], "decision": "mixed", "rationale": "The receiving main-medium
    sludge-fluid aliquot is separately documented; do not flatten a raw sludge volume
    into main-medium mass.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source uses1000ml
    sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong
    stage. No density or finished chemical composition is known."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source uses1000ml
    sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong
    stage. No density or finished chemical composition is known."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The source uses1000ml
    sludge to prepare a separate stock;1000G_PER_L is a mass/volume error and wrong
    stage. No density or finished chemical composition is known."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "1000",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Exact replacement
    accession remains inaccessible; current local value is retained and compared with
    the base source only. The source uses1000ml sludge to prepare a separate stock;1000G_PER_L
    is a mass/volume error and wrong stage. No density or finished chemical composition
    is known."}]}, {"quantity_id": "q28", "topic": "Main staged anaerobic preparation",
    "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "source_scope": "Entire exact source step was read; quantitative control summary
    is interpretation, not quoted source text.", "quote": "{\n                        \"step\":
    \"Dissolve ingredients (except cysteine, carbonate, cellobiose and sulfide), bring
    medium to the boil, then cool to room temperature under 80% N2 and 20% CO2 gas
    mixture and add cysteine. Dispense under same gas atmosphere into anoxic Hungate-type
    tubes or serum vials and autoclave. Add sulfide from a sterile anoxic stock solution
    prepared under 100% N2 gas and carbonate from a sterile anoxic stock solution
    prepared under 80% N2 and 20% CO2 gas mixture. Sterilize cellobiose separately
    by filtration under 100% N2 gas. Adjust pH of the complete medium to 7.0, if necessary.\"\n                    }",
    "exact_decoded_object": {"step": "Dissolve ingredients (except cysteine, carbonate,
    cellobiose and sulfide), bring medium to the boil, then cool to room temperature
    under 80% N2 and 20% CO2 gas mixture and add cysteine. Dispense under same gas
    atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. Add sulfide
    from a sterile anoxic stock solution prepared under 100% N2 gas and carbonate
    from a sterile anoxic stock solution prepared under 80% N2 and 20% CO2 gas mixture.
    Sterilize cellobiose separately by filtration under 100% N2 gas. Adjust pH of
    the complete medium to 7.0, if necessary."}, "quote_basis": "Literal UTF-8 raw-response
    substring; decoded object independently equals existing JSON locator."}], "decision":
    "evidence_only", "rationale": "Distinct cysteine timing, separately sterilized
    carbonate/sulfide stocks, separately filtered cellobiose,80/20 nitrogen/carbon-dioxide
    and100%nitrogen contexts; complete-medium pH7.0. Stock strengths and aliquots
    for carbonate/sulfide are not supplied.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Dissolve ingredients
    (except cysteine, carbonate, cellobiose and sulfide), bring medium to the boil,
    then cool to room temperature under 80% N2 and 20% CO2 gas mixture and add cysteine.
    Dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials
    and autoclave. Add sulfide from a sterile anoxic stock solution prepared under
    100% N2 gas and carbonate from a sterile anoxic stock solution prepared under
    80% N2 and 20% CO2 gas mixture. Sterilize cellobiose separately by filtration
    under 100% N2 gas. Adjust pH of the complete medium to 7.0, if necessary.", "decision":
    "evidence_only", "rationale": "Existing owner text matches the current source
    step and is credited; attach source-stage evidence and preserve context."}, {"path":
    "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Missing process context; keep exact source and variant scope.",
    "missing": true}]}, {"quantity_id": "q29", "topic": "Conditional cellulose adaptation",
    "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[0].steps[1]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "source_scope": "Entire exact source step was read; quantitative control summary
    is interpretation, not quoted source text.", "quote": "{\n                        \"step\":
    \"Note: Some strains can be adapted to cellulose as substrate using 10.0 g/l cellulose
    powder MN 301 (MACHEREY-NAGEL).\"\n                    }", "exact_decoded_object":
    {"step": "Note: Some strains can be adapted to cellulose as substrate using 10.0
    g/l cellulose powder MN 301 (MACHEREY-NAGEL)."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals existing JSON locator."}],
    "decision": "evidence_only", "rationale": "The10.0g/l cellulose adaptation is
    conditional on some strains and preserves MN301 grade; no particular strain is
    identified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "Note: Some
    strains can be adapted to cellulose as substrate using 10.0 g/l cellulose powder
    MN 301 (MACHEREY-NAGEL).", "decision": "evidence_only", "rationale": "Existing
    owner text matches the current source step and is credited; attach source-stage
    evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Missing process context; keep exact source and variant scope.",
    "missing": true}]}, {"quantity_id": "q30", "topic": "SL10 preparation", "source":
    [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "source_scope": "Entire exact source step was read; quantitative control summary
    is interpretation, not quoted source text.", "quote": "{\n                        \"step\":
    \"First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve the
    other salts. Finally make up to 1000.00 ml.\"\n                    }", "exact_decoded_object":
    {"step": "First dissolve FeCl2 in the HCl, then dilute in water, add and dissolve
    the other salts. Finally make up to 1000.00 ml."}, "quote_basis": "Literal UTF-8
    raw-response substring; decoded object independently equals existing JSON locator."}],
    "decision": "evidence_only", "rationale": "Iron is dissolved first in acid before
    other salts; explicit1000ml stock makeup.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "preparation_steps[2].description", "stored_value": "First dissolve
    FeCl2 in the HCl, then dilute in water, add and dissolve the other salts. Finally
    make up to 1000.00 ml.", "decision": "evidence_only", "rationale": "Existing owner
    text matches the current source step and is credited; attach source-stage evidence
    and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Missing process context; keep exact source and variant scope.",
    "missing": true}]}, {"quantity_id": "q31", "topic": "Sludge-fluid preparation",
    "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "source_scope": "Entire exact source step was read; quantitative control summary
    is interpretation, not quoted source text.", "quote": "{\n                        \"step\":
    \"Add 0.4% yeast extract to sludge from an anaerobic digester, and after gassing
    with nitrogen gas for a few minutes incubate it at 37\\u00b0C for 24 hours. Then
    centrifuge the sludge at 13000 g and autoclave the resulting, clear supernatant
    in screw-capped vessels under nitrogen gas. The sludge fluid can be stored at
    8-12\\u00b0C in the dark.\"\n                    }", "exact_decoded_object": {"step":
    "Add 0.4% yeast extract to sludge from an anaerobic digester, and after gassing
    with nitrogen gas for a few minutes incubate it at 37°C for 24 hours. Then centrifuge
    the sludge at 13000 g and autoclave the resulting, clear supernatant in screw-capped
    vessels under nitrogen gas. The sludge fluid can be stored at 8-12°C in the dark."},
    "quote_basis": "Literal UTF-8 raw-response substring; decoded object independently
    equals existing JSON locator."}], "decision": "evidence_only", "rationale": "The0.4%
    yeast-extract statement accompanies4g/1000ml starting sludge; nitrogen processing,37°C/24h
    incubation,13000g clarification, autoclaving and8–12°C dark storage belong to
    this stock. Process loss and finished composition remain unknown.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml", "field_path":
    "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Missing
    process context; keep exact source and variant scope.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "preparation_steps[3].description", "stored_value": "Add 0.4% yeast
    extract to sludge from an anaerobic digester, and after gassing with nitrogen
    gas for a few minutes incubate it at 37°C for 24 hours. Then centrifuge the sludge
    at 13000 g and autoclave the resulting, clear supernatant in screw-capped vessels
    under nitrogen gas. The sludge fluid can be stored at 8-12°C in the dark.", "decision":
    "evidence_only", "rationale": "Existing owner text matches the current source
    step and is credited; attach source-stage evidence and preserve context."}, {"path":
    "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Missing process context; keep exact source and variant scope.",
    "missing": true}]}, {"quantity_id": "q32", "topic": "Rumen-fluid preparation",
    "source": [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "source_scope": "Entire exact source step was read; quantitative control summary
    is interpretation, not quoted source text.", "quote": "{\n                        \"step\":
    \"Rumen fluid from cow or sheep (obtained from fistulated animals or abattoir
    refuse) is filtered through muslin, autoclaved at 121\\u00b0C for 15 min and then
    centrifuged at 27,000 g for 20 min. The supernatant is made anoxic by sparging
    with 100% N2 gas for 15 min, dispensed under same gas atmosphere into anoxic serum
    vials to 30% of volume and then stored frozen at -20\\u00b0C.\"\n                    }",
    "exact_decoded_object": {"step": "Rumen fluid from cow or sheep (obtained from
    fistulated animals or abattoir refuse) is filtered through muslin, autoclaved
    at 121°C for 15 min and then centrifuged at 27,000 g for 20 min. The supernatant
    is made anoxic by sparging with 100% N2 gas for 15 min, dispensed under same gas
    atmosphere into anoxic serum vials to 30% of volume and then stored frozen at
    -20°C."}, "quote_basis": "Literal UTF-8 raw-response substring; decoded object
    independently equals existing JSON locator."}], "decision": "evidence_only", "rationale":
    "Rumen fluid uses121°C/15min sterilization,27000g/20min clarification,100%nitrogen/15min
    sparging,30%vial fill and−20°C storage. These controls belong to the rumen stock,
    not main-medium incubation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Missing process context; keep exact source and variant scope.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "preparation_steps[4].description", "stored_value": "Rumen fluid
    from cow or sheep (obtained from fistulated animals or abattoir refuse) is filtered
    through muslin, autoclaved at 121°C for 15 min and then centrifuged at 27,000
    g for 20 min. The supernatant is made anoxic by sparging with 100% N2 gas for
    15 min, dispensed under same gas atmosphere into anoxic serum vials to 30% of
    volume and then stored frozen at -20°C.", "decision": "evidence_only", "rationale":
    "Existing owner text matches the current source step and is credited; attach source-stage
    evidence and preserve context."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Missing process context; keep exact source and variant scope.",
    "missing": true}]}, {"quantity_id": "q33", "topic": "Complete-medium pH", "source":
    [{"evidence_id": "api320", "reference": "https://mediadive.dsmz.de/rest/medium/320",
    "raw_path": "REVIEW_WORK/batch063/source01/api320.bin", "raw_sha256": "d254a28124fef18cfea3de76dd334f1ce035f72563ff1d15281957cd5367cb8f",
    "locator": "$.data.medium; $.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T10:18:19.996238Z",
    "quote": "Adjust pH of the complete medium to 7.0, if necessary."}], "decision":
    "mixed", "rationale": "Do not transfer a stock-preparation or storage condition
    to the medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/CLOSTRIDIUM_CELLULOVORANS_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Base primary and API agree on complete-medium pH7.0."}, {"path": "data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Base primary and API agree on complete-medium pH7.0."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Base primary and API agree on complete-medium pH7.0."}, {"path": "data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale":
    "Base primary and API establish pH7.0; exact variant source remains inaccessible."}]}]'
- assessment_id: a6
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All nineteen asserted ingredient CHEBI identifiers resolve to current labels;
    supplied-form fidelity still fails for phosphate trihydrate, nickel hexahydrate
    and sodium resazurin. All20 OLS objects including the nickel alternative and current
    exact preferred catalog rows were read. Catalogue aliases/rejected rows are observations,
    never automatic grounding approval.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - grounding
- assessment_id: a7
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Seven exact historical concentration reports plus the scoped DSM320/KOMODO320
    archive row and method were read. Four October5 reports checked zero source claims;
    three October7 reports leave quantities unresolved. Their identical cited API
    raw digest matches the fresh response, with exact literal/decoded joins recorded.
    Old catalogue fragments remain derivative because both current route forms return403.
    All source histories remain unchanged.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - history
  - scalars
- assessment_id: a8
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - local-target
- assessment_id: a9
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:005010
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-005010-separate-stock-inputs-and-receiving-additions
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Separate stock inputs and receiving additions
  description: The generated target and two base contributors encode source stock
    components as direct-medium concentrations. Their yeast4.5 combines two stages,
    sludge1000G_PER_L misstates a liquid input, and HCl2.5 cannot be authenticated
    from bare25%. The replacement contributor copies the same values, but its exact
    source quantities remain unsupported. Missing stock additions and solvent context
    prevent faithful interpretation. Ordinary primary gram inputs agree with provider
    numerals but do not establish final-medium volume.
  target_ids:
  - CultureMech:005010
  field_paths:
  - ingredients
  - solutions
  - preparation_steps
  evidence_ids:
  - api320
  - dsm320
  - quantities
  rule_id: review-yaml-record/stock-stage-and-unit
  native_severity: P2
  normalization_reason: P2 is normalized to major under this custom rule because represented
    amounts have demonstrable source-stage or mass/volume errors. Native P2.3 specifically
    concerns units incompatible with physical_state; unsupported final-volume bases
    are separately limited.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-005010-retain-the-explicit-rumen-to-sludge-variant
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Retain the explicit rumen-to-sludge variant
  description: The named replacement contributor is merged as a synonym while both
    fluid additions and their choice are absent. The base source already distinguishes
    them; copied flattened ingredient equality and SOURCE_DUPLICATE metadata do not
    prove the replacement is an identical formulation.
  target_ids:
  - CultureMech:005010
  field_paths:
  - merged_from
  - synonyms
  - solutions
  - variant_relationship
  evidence_ids:
  - api320
  - historical-reader
  - identity-search
  - writer-mediadive
  rule_id: review-yaml-record/variant-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major under this custom rule because a
    declared source substitution is lost; unresolved current catalogue access is not
    asserted as a proven invalid accession.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-005010-preserve-anaerobic-preparation-and-its-stock-boundaries
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Preserve anaerobic preparation and its stock boundaries
  description: The DSM owner already retains all five preparation descriptions, but
    generated and KOMODO layers omit them and retain Aerobic:Yes. The primary requires
    anaerobic main-medium handling. Stock processing and storage controls must remain
    associated with their own fluid or trace recipe.
  target_ids:
  - CultureMech:005010
  field_paths:
  - preparation_steps
  - notes
  evidence_ids:
  - api320
  - owner-2
  - writer-resolver
  - writer-mediadive
  rule_id: review-yaml-record/preparation-fidelity
  native_severity: P2
  normalization_reason: P2 is normalized to major because missing stage context and
    contradictory atmosphere metadata materially misrepresent the primary preparation;
    this is not native P2.3 concentration semantics.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-005010-resolve-supplied-hydrate-and-sodium-salt-forms
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Resolve supplied hydrate and sodium-salt forms
  description: K2HPO4 trihydrate is mapped to CHEBI:131527 whose formula is anhydrous
    despite a trihydrate synonym; nickel hexahydrate is mapped to anhydrous CHEBI:34887
    instead of the verified53542 candidate; sodium resazurin is mapped to neutral
    CHEBI:8806. All asserted labels resolve, but label equality and current MIM aliases
    do not establish exact supplied form.
  target_ids:
  - CultureMech:005010
  field_paths:
  - ingredients[0].term
  - ingredients[0].mediaingredientmech_chebi_term
  - ingredients[6].term
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  evidence_ids:
  - chebi131527
  - chebi34887
  - chebi53542
  - chebi8806
  - dsm320
  - grounding
  rule_id: review-yaml-record/exact-supplied-form
  native_severity: P2
  normalization_reason: P2 is normalized to major because the asserted chemistry does
    not encode the explicit supplied forms; these are valid IDs with wrong or insufficient
    form specificity, not nonexistent-ID findings.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-005010-preserve-malformed-history-and-add-claim-level-traceability
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Preserve malformed history and add claim-level traceability
  description: The original KOMODO timestamp2026-01-27T01:15:02.fZ is malformed in
    the selected record and both KOMODO owners. Historical concentration reports retain
    unresolved decisions; no attached claim evidence appears in the four files. Their
    current raw API matches authenticate the quoted bytes only, not old retrieval
    events.
  target_ids:
  - CultureMech:005010
  field_paths:
  - curation_history
  - ingredients.evidence
  evidence_ids:
  - history
  - historical-reader
  - attached-evidence-joins
  - writer-komodo
  rule_id: review-yaml-record/historical-event-metadata
  native_severity: P3
  normalization_reason: P3 is normalized to minor for a bounded provenance defect;
    native P4.4 concerns history length1 and does not describe these malformed multi-event
    histories.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Reconstruct explicit main-medium, SL10 and biological-fluid stock stages
    in the maintained contributors using the complete quantity inventory. Preserve
    unknown percent basis, density, finished sludge composition and final-medium volume;
    do not replace them with guessed concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Resolve the exact replacement accession when available, retain its
    substitution as a distinct source-scoped formulation or explicit variant, and
    preserve optional/alternative fields in the importer. Do not transfer all base-medium
    amounts solely from its name or historical link.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Preserve the existing DSM source text and attach exact source-stage
    evidence, reconcile the contradictory aerobic metadata, and represent missing
    base preparation in the maintained KOMODO record. Treat the replacement preparation
    as unverified until its scope is resolved. Do not reapply stock storage temperatures
    as organism growth temperatures.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Retain explicit supplied forms, verify form-specific identifiers in
    authoritative chemical sources, and reconcile both primary and MIM-keyed term
    slots. Nickel hexahydrate53542 is independently verified; no unverified replacement
    is proposed for phosphate trihydrate or sodium resazurin.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: Keep original history append-only, document any verified timestamp
    correction without inventing an old event time, and attach evidence to each curated
    claim. Repair current timestamp generation before future imports; do not treat
    old report coverage as source-verified scientific status.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005010
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/clostridium_cellulovorans_medium_replace_rumen_fluid_clarified_with_sludge_fluid_medium_119.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Both exact KOMODO MediaInfo routes and both prefixed/historical catalogue routes
  returned403. The DSM base is independently verified, but exact current replacement-accession
  identity and variant completeness are unresolved; completion is partial.
- Main water1000ml and provider volume1021 are not an explicit final-medium volume.
  No total-volume normalization, density-based HCl conversion, reducing-stock concentration
  or aliquot is inferred.
- SL10 has explicit1000ml final stock makeup. Sludge-fluid input and preparation do
  not establish its post-processing composition. The optional cellulose statement
  does not identify strains or unambiguously define co-use versus replacement of cellobiose.
- Only the selected pair/method/validation portions of the broad historical source-duplicate
  report are assessed; other pairs are outside scope. Current matching raw bytes do
  not authenticate historical access-event time.
- Exact current MIM preferred-row and ontology matches do not prove historical linkage
  correctness. No standalone solution dependency is asserted from a matching name
  alone.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
